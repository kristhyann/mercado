"use server";
/**
 * Ações do painel. TODAS verificam no servidor se quem chama é o administrador
 * (requireAdminAction) e o banco verifica de novo (assert_platform_admin).
 */
import { revalidatePath } from "next/cache";
import { headers } from "next/headers";
import { redirect } from "next/navigation";
import fs from "node:fs/promises";
import path from "node:path";
import { AdminAuthError, login, logout, requireAdminAction } from "@/lib/admin/auth";
import { backend, newImageName } from "@/lib/admin/backend";
import { adminMode } from "@/lib/admin/mode";
import { optimizeImage, type ImageKind } from "@/lib/admin/images";
import { clone, imageRefs } from "@/lib/admin/editor";
import { parseStore } from "@/lib/menu";
import { RESERVED_SLUGS, type StoreConfig } from "@/lib/schema";
import { toSyncPayload } from "@/lib/sync-payload";
import { STORES_ROOT } from "@/lib/data";
import template from "../../../stores/_modelo/store.json";

export type ActionResult<T = object> = ({ ok: true } & T) | { ok: false; error: string; issues?: string[] };

const SLUG = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

function fail(e: unknown): { ok: false; error: string } {
  if (e instanceof AdminAuthError) return { ok: false, error: e.message };
  return { ok: false, error: e instanceof Error ? e.message : "Erro inesperado." };
}

function refreshPublic(slug: string) {
  revalidatePath(`/${slug}`);
  revalidatePath(`/${slug}/checkout`);
  revalidatePath(`/${slug}`, "layout");
  revalidatePath("/");
  revalidatePath("/admin", "layout");
}

// ─── Login ──────────────────────────────────────────────────────────────────
export async function loginAction(_prev: { error: string | null }, form: FormData): Promise<{ error: string | null }> {
  const h = await headers();
  const ip = (h.get("x-forwarded-for") ?? "").split(",")[0].trim() || h.get("x-real-ip") || "";
  const error = await login(String(form.get("email") ?? ""), String(form.get("password") ?? ""), ip);
  if (error) return { error };
  redirect("/admin");
}

export async function logoutAction() {
  await logout();
  redirect("/admin/login");
}

// ─── Salvar loja ────────────────────────────────────────────────────────────
export async function saveStoreAction(slug: string, config: StoreConfig, expectedUpdatedAt: string | null): Promise<ActionResult<{ updatedAt: string }>> {
  try {
    await requireAdminAction();
    if (config.slug !== slug) return { ok: false, error: "Para mudar o endereço use a opção 'Alterar endereço'." };
    const { config: parsed, issues } = parseStore(config, { strict: true });
    const errors = issues.filter((i) => !i.startsWith("aviso"));
    if (parsed && !parsed.isDemo && /^5500/.test(parsed.contact.whatsapp)) errors.push("contact.whatsapp: informe o WhatsApp real da loja.");
    if (!parsed || errors.length) return { ok: false, error: "Corrija os itens abaixo antes de salvar.", issues: errors };

    const be = backend();
    const updatedAt = await be.saveStore(toSyncPayload(parsed) as Record<string, unknown>, expectedUpdatedAt);
    refreshPublic(slug);

    // Remove imagens enviadas pelo painel que não são mais usadas (substituídas/excluídas).
    try {
      const used = new Set(imageRefs(parsed));
      const hourAgo = Date.now() - 60 * 60 * 1000;
      const stale = (await be.listImages(slug)).filter((i) => !used.has(i.url) && i.createdAt < hourAgo).map((i) => i.name);
      await be.deleteImages(slug, stale);
    } catch {
      /* limpeza é opcional */
    }
    return { ok: true, updatedAt };
  } catch (e) {
    return fail(e);
  }
}

// ─── Criar loja ─────────────────────────────────────────────────────────────
export async function createStoreAction(input: { name: string; slug: string; whatsapp: string; base: string }): Promise<ActionResult<{ slug: string }>> {
  try {
    await requireAdminAction();
    const name = input.name.trim();
    const slug = input.slug.trim();
    const whatsapp = input.whatsapp.replace(/\D/g, "");
    if (name.length < 2) return { ok: false, error: "Informe o nome da loja." };
    if (!SLUG.test(slug) || slug.length > 60 || RESERVED_SLUGS.has(slug)) return { ok: false, error: "Endereço inválido. Use letras minúsculas, números e hífens (ex.: acai-do-joao)." };
    if (!/^\d{12,15}$/.test(whatsapp)) return { ok: false, error: "WhatsApp inválido. Use DDI + DDD + número (ex.: 5511987654321)." };
    const be = backend();
    if (await be.getStore(slug)) return { ok: false, error: `O endereço "${slug}" já está em uso.` };

    let config: Record<string, any>;
    if (input.base && input.base !== "_modelo") {
      const src = await be.getStore(input.base);
      if (!src) return { ok: false, error: "Loja de origem não encontrada." };
      config = clone(src.config) as Record<string, any>;
      if (adminMode() === "local") {
        await fs.cp(path.join(STORES_ROOT, input.base, "images"), path.join(STORES_ROOT, slug, "images"), { recursive: true }).catch(() => {});
      } else {
        const copy = (u: string | null | undefined) => (u ? be.copyImage(u, slug) : Promise.resolve(u ?? null));
        config.branding.logo = await copy(config.branding.logo);
        config.branding.cover = await copy(config.branding.cover);
        if (config.banner) config.banner.image = await copy(config.banner.image);
        if (config.seo) config.seo.image = await copy(config.seo.image);
        for (const p of config.products ?? []) p.image = await copy(p.image);
      }
    } else {
      config = clone(template) as Record<string, any>;
      config.branding.logo = null;
      config.branding.cover = null;
      delete config.$schema;
    }
    config.slug = slug;
    config.name = name;
    config.isDemo = false;
    config.active = false; // começa inativa: ative quando estiver pronta
    config.contact.whatsapp = whatsapp;
    config.seo = { title: `${name} — Cardápio e pedidos pelo WhatsApp`, description: null, image: config.seo?.image ?? null };

    const { config: parsed, issues } = parseStore(config, { strict: true });
    const errors = issues.filter((i) => !i.startsWith("aviso"));
    if (!parsed || errors.length) return { ok: false, error: "Modelo inválido.", issues: errors };
    await be.saveStore(toSyncPayload(parsed) as Record<string, unknown>, null);
    refreshPublic(slug);
    return { ok: true, slug };
  } catch (e) {
    return fail(e);
  }
}

// ─── Ativar / desativar, renomear, excluir ──────────────────────────────────
export async function setStoreActiveAction(slug: string, active: boolean): Promise<ActionResult<{ updatedAt: string }>> {
  try {
    await requireAdminAction();
    const updatedAt = await backend().setActive(slug, active);
    refreshPublic(slug);
    return { ok: true, updatedAt };
  } catch (e) {
    return fail(e);
  }
}

export async function renameStoreAction(from: string, to: string): Promise<ActionResult<{ slug: string }>> {
  try {
    await requireAdminAction();
    const next = to.trim();
    if (!SLUG.test(next) || RESERVED_SLUGS.has(next)) return { ok: false, error: "Endereço inválido." };
    await backend().rename(from, next);
    refreshPublic(from);
    refreshPublic(next);
    return { ok: true, slug: next };
  } catch (e) {
    return fail(e);
  }
}

export async function deleteStoreAction(slug: string, confirmation: string): Promise<ActionResult> {
  try {
    await requireAdminAction();
    if (confirmation.trim() !== slug) return { ok: false, error: "Digite o endereço da loja exatamente para confirmar." };
    await backend().deleteStore(slug);
    refreshPublic(slug);
    return { ok: true };
  } catch (e) {
    return fail(e);
  }
}

// ─── Imagens ────────────────────────────────────────────────────────────────
export async function uploadImageAction(form: FormData): Promise<ActionResult<{ url: string }>> {
  try {
    await requireAdminAction();
    const slug = String(form.get("slug") ?? "");
    const kind = String(form.get("kind") ?? "") as ImageKind;
    const file = form.get("file");
    if (!SLUG.test(slug)) return { ok: false, error: "Loja inválida." };
    if (!(file instanceof File)) return { ok: false, error: "Nenhum arquivo enviado." };
    const data = await optimizeImage(file, kind);
    const url = await backend().uploadImage(slug, newImageName(kind), data, "image/webp");
    return { ok: true, url };
  } catch (e) {
    return fail(e);
  }
}
