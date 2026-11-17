/**
 * Operações administrativas. Só podem ser chamadas DEPOIS de requireAdminAction()/requireAdminPage().
 *  - supabase: usa a sessão do administrador; o banco verifica de novo (assert_platform_admin).
 *  - local:    edita stores/<slug>/store.json (somente desenvolvimento).
 */
import "server-only";
import crypto from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { adminMode } from "./mode";
import { supabaseSession } from "./supabase-session";
import { STORES_ROOT } from "../data";
import { env } from "../env";

export interface AdminStoreRow {
  slug: string;
  name: string;
  isActive: boolean;
  isDemo: boolean;
  logo: string | null;
  primaryColor: string;
  whatsapp: string;
  createdAt: string;
  updatedAt: string;
  productCount: number;
  activeProductCount: number;
  categoryCount: number;
}

export interface AdminStoreDoc {
  config: Record<string, unknown>;
  updatedAt: string;
}

export interface StoredImage {
  name: string;
  url: string;
  createdAt: number;
}

export const BUCKET = process.env.SUPABASE_STORAGE_BUCKET || "store-assets";
const SLUG = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

function assertSlug(slug: string) {
  if (!SLUG.test(slug) || slug.length > 60) throw new Error("Endereço (slug) inválido.");
}

function friendly(message: string): string {
  if (/conflito/i.test(message)) return message.replace(/^.*?conflito/i, "Conflito");
  if (/acesso negado/i.test(message)) return "Acesso negado.";
  if (/duplicate key|unique/i.test(message)) return "Já existe um registro com essa chave.";
  return message;
}

// ════════════════════════════════════════════════════════════════════════════
// Supabase
// ════════════════════════════════════════════════════════════════════════════
const supabaseBackend = {
  async listStores(): Promise<AdminStoreRow[]> {
    const sb = await supabaseSession();
    const { data, error } = await sb.rpc("admin_list_stores");
    if (error) throw new Error(friendly(error.message));
    return (data ?? []).map((r: Record<string, unknown>) => ({
      slug: r.slug as string, name: r.name as string, isActive: r.is_active as boolean, isDemo: r.is_demo as boolean,
      logo: (r.logo_url as string) ?? null, primaryColor: r.primary_color as string, whatsapp: r.whatsapp as string,
      createdAt: r.created_at as string, updatedAt: r.updated_at as string, productCount: r.product_count as number,
      activeProductCount: r.active_product_count as number, categoryCount: r.category_count as number,
    }));
  },
  async getStore(slug: string): Promise<AdminStoreDoc | null> {
    const sb = await supabaseSession();
    const { data, error } = await sb.rpc("admin_get_store", { p_slug: slug });
    if (error) throw new Error(friendly(error.message));
    if (!data) return null;
    return { config: data.config, updatedAt: data.updated_at };
  },
  async saveStore(payload: Record<string, unknown>, expectedUpdatedAt: string | null): Promise<string> {
    const sb = await supabaseSession();
    const { data, error } = await sb.rpc("admin_sync_store", { payload, expected_updated_at: expectedUpdatedAt });
    if (error) throw new Error(friendly(error.message));
    return data.updated_at as string;
  },
  async setActive(slug: string, active: boolean): Promise<string> {
    const sb = await supabaseSession();
    const { data, error } = await sb.rpc("admin_set_store_active", { p_slug: slug, p_active: active });
    if (error) throw new Error(friendly(error.message));
    return data as string;
  },
  async rename(from: string, to: string): Promise<void> {
    const sb = await supabaseSession();
    const { error } = await sb.rpc("admin_rename_store", { p_old: from, p_new: to });
    if (error) throw new Error(friendly(error.message));
  },
  async deleteStore(slug: string): Promise<void> {
    const sb = await supabaseSession();
    const imgs = await this.listImages(slug).catch(() => []);
    const { error } = await sb.rpc("admin_delete_store", { p_slug: slug });
    if (error) throw new Error(friendly(error.message));
    if (imgs.length) await sb.storage.from(BUCKET).remove(imgs.map((i) => `${slug}/${i.name}`));
  },
  async uploadImage(slug: string, fileName: string, data: Buffer, contentType: string): Promise<string> {
    const sb = await supabaseSession();
    const key = `${slug}/${fileName}`;
    const { error } = await sb.storage.from(BUCKET).upload(key, data, { contentType, upsert: false, cacheControl: "31536000" });
    if (error) throw new Error(`Falha ao enviar a imagem: ${error.message}`);
    return sb.storage.from(BUCKET).getPublicUrl(key).data.publicUrl;
  },
  async copyImage(url: string, toSlug: string): Promise<string> {
    const prefix = `${env.supabaseUrl}/storage/v1/object/public/${BUCKET}/`;
    if (!url.startsWith(prefix)) return url;
    const sb = await supabaseSession();
    const src = decodeURIComponent(url.slice(prefix.length));
    const dest = `${toSlug}/${path.basename(src)}`;
    const { error } = await sb.storage.from(BUCKET).copy(src, dest);
    if (error && !/exists/i.test(error.message)) return url;
    return sb.storage.from(BUCKET).getPublicUrl(dest).data.publicUrl;
  },
  async listImages(slug: string): Promise<StoredImage[]> {
    const sb = await supabaseSession();
    const { data, error } = await sb.storage.from(BUCKET).list(slug, { limit: 1000 });
    if (error) throw new Error(error.message);
    return (data ?? [])
      .filter((o) => o.id)
      .map((o) => ({ name: o.name, url: sb.storage.from(BUCKET).getPublicUrl(`${slug}/${o.name}`).data.publicUrl, createdAt: new Date(o.created_at ?? 0).getTime() }));
  },
  async deleteImages(slug: string, names: string[]): Promise<void> {
    if (!names.length) return;
    const sb = await supabaseSession();
    await sb.storage.from(BUCKET).remove(names.map((n) => `${slug}/${n}`));
  },
};

// ════════════════════════════════════════════════════════════════════════════
// Local (desenvolvimento) — grava em stores/<slug>/
// ════════════════════════════════════════════════════════════════════════════
const file = (slug: string) => path.join(STORES_ROOT, slug, "store.json");
async function mtime(slug: string) {
  return (await fs.stat(file(slug))).mtime.toISOString();
}
async function readJson(slug: string) {
  return JSON.parse(await fs.readFile(file(slug), "utf8")) as Record<string, unknown>;
}

const localBackend = {
  async listStores(): Promise<AdminStoreRow[]> {
    const dirs = (await fs.readdir(STORES_ROOT, { withFileTypes: true })).filter((d) => d.isDirectory() && SLUG.test(d.name));
    const rows: AdminStoreRow[] = [];
    for (const d of dirs) {
      try {
        const c = (await readJson(d.name)) as Record<string, any>;
        const st = await fs.stat(file(d.name));
        rows.push({
          slug: d.name, name: c.name, isActive: c.active !== false, isDemo: Boolean(c.isDemo),
          logo: c.branding?.logo ? `/assets/${d.name}/${c.branding.logo}` : null, primaryColor: c.branding?.primaryColor ?? "#6B21A8",
          whatsapp: c.contact?.whatsapp ?? "", createdAt: st.birthtime.toISOString(), updatedAt: st.mtime.toISOString(),
          productCount: (c.products ?? []).length, activeProductCount: (c.products ?? []).filter((p: any) => p.active !== false).length,
          categoryCount: (c.categories ?? []).length,
        });
      } catch {
        /* pasta sem store.json válido */
      }
    }
    return rows.sort((a, b) => b.createdAt.localeCompare(a.createdAt));
  },
  async getStore(slug: string): Promise<AdminStoreDoc | null> {
    assertSlug(slug);
    try {
      return { config: await readJson(slug), updatedAt: await mtime(slug) };
    } catch {
      return null;
    }
  },
  async saveStore(payload: Record<string, unknown>, expectedUpdatedAt: string | null): Promise<string> {
    const slug = String(payload.slug);
    assertSlug(slug);
    try {
      const cur = await mtime(slug);
      if (expectedUpdatedAt && cur !== expectedUpdatedAt) throw new Error("Conflito: esta loja foi alterada em outro lugar. Recarregue a página para ver a versão atual.");
    } catch (e) {
      if ((e as NodeJS.ErrnoException).code !== "ENOENT") throw e;
    }
    await fs.mkdir(path.dirname(file(slug)), { recursive: true });
    await fs.writeFile(file(slug), JSON.stringify({ $schema: "../store.schema.json", ...payload }, null, 2) + "\n");
    return mtime(slug);
  },
  async setActive(slug: string, active: boolean): Promise<string> {
    const c = await readJson(slug);
    c.active = active;
    await fs.writeFile(file(slug), JSON.stringify(c, null, 2) + "\n");
    return mtime(slug);
  },
  async rename(from: string, to: string): Promise<void> {
    assertSlug(to);
    try {
      await fs.access(path.join(STORES_ROOT, to));
      throw new Error(`O endereço "${to}" já está em uso.`);
    } catch (e) {
      if ((e as NodeJS.ErrnoException).code !== "ENOENT") throw e;
    }
    await fs.rename(path.join(STORES_ROOT, from), path.join(STORES_ROOT, to));
    const c = await readJson(to);
    c.slug = to;
    await fs.writeFile(file(to), JSON.stringify(c, null, 2) + "\n");
  },
  async deleteStore(slug: string): Promise<void> {
    assertSlug(slug);
    await fs.rm(path.join(STORES_ROOT, slug), { recursive: true, force: true });
  },
  async uploadImage(slug: string, fileName: string, data: Buffer): Promise<string> {
    const dir = path.join(STORES_ROOT, slug, "images");
    await fs.mkdir(dir, { recursive: true });
    await fs.writeFile(path.join(dir, fileName), data);
    return `images/${fileName}`;
  },
  async copyImage(url: string): Promise<string> {
    return url; // no modo local a pasta images/ inteira é copiada em createStore
  },
  async listImages(slug: string): Promise<StoredImage[]> {
    const dir = path.join(STORES_ROOT, slug, "images");
    try {
      const names = await fs.readdir(dir);
      return Promise.all(names.filter((n) => n.startsWith("admin-")).map(async (n) => ({ name: n, url: `images/${n}`, createdAt: (await fs.stat(path.join(dir, n))).mtimeMs })));
    } catch {
      return [];
    }
  },
  async deleteImages(slug: string, names: string[]): Promise<void> {
    for (const n of names) if (!n.includes("/") && !n.includes("..")) await fs.rm(path.join(STORES_ROOT, slug, "images", n), { force: true });
  },
};

// ════════════════════════════════════════════════════════════════════════════
// Visualização (hospedado sem Supabase): lê as lojas da pasta /stores e recusa gravações
// ════════════════════════════════════════════════════════════════════════════
export const PREVIEW_MESSAGE = "Modo visualização: nada é salvo. Configure o Supabase para editar as lojas (veja o README).";
const readOnly = async (): Promise<never> => {
  throw new Error(PREVIEW_MESSAGE);
};
const previewBackend = {
  listStores: localBackend.listStores,
  getStore: localBackend.getStore,
  listImages: async () => [] as StoredImage[],
  saveStore: readOnly,
  setActive: readOnly,
  rename: readOnly,
  deleteStore: readOnly,
  uploadImage: readOnly,
  copyImage: readOnly,
  deleteImages: async () => {},
};

export type AdminBackend = typeof supabaseBackend;

export function backend(): AdminBackend {
  const mode = adminMode();
  if (mode === "supabase") return supabaseBackend;
  if (mode === "local") return localBackend as unknown as AdminBackend;
  if (mode === "preview") return previewBackend as unknown as AdminBackend;
  throw new Error("Painel não configurado.");
}

export function newImageName(kind: string) {
  return `admin-${kind}-${Date.now().toString(36)}${crypto.randomBytes(3).toString("hex")}.webp`;
}
