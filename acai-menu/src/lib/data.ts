/**
 * Fonte de dados das lojas.
 *  - supabase: função get_store_menu(slug) com a chave anon (RLS ativo).
 *  - local:    arquivos stores/<slug>/store.json (demonstração/desenvolvimento).
 * Em ambos os casos o resultado passa pelo MESMO schema de validação.
 */
import "server-only";
import fs from "node:fs/promises";
import path from "node:path";
import { cache } from "react";
import { createClient, type SupabaseClient } from "@supabase/supabase-js";
import { activeSource, env } from "./env";
import { parseStore, type StoreMenu } from "./menu";
import { RESERVED_SLUGS, type StoreConfigInput } from "./schema";

const STORES_DIR = path.join(process.cwd(), "stores");
const SLUG_RE = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

let client: SupabaseClient | null = null;
function supabase(): SupabaseClient {
  if (!env.supabaseUrl || !env.supabaseAnonKey) {
    throw new Error("Supabase não configurado: defina SUPABASE_URL e SUPABASE_ANON_KEY (veja .env.example).");
  }
  client ??= createClient(env.supabaseUrl, env.supabaseAnonKey, {
    auth: { persistSession: false, autoRefreshToken: false },
  });
  return client;
}

/** Caminhos relativos (images/x.jpg) viram URLs servidas pelo próprio site no modo local. */
function isRelative(ref: string) {
  return !/^(https?:)?\/\//.test(ref) && !ref.startsWith("/") && !ref.startsWith("data:");
}
export function resolveLocalImages(raw: StoreConfigInput): StoreConfigInput {
  const fix = (v: string | null | undefined) => (v && isRelative(v) ? `/assets/${raw.slug}/${v.replace(/^\.\//, "")}` : v);
  return {
    ...raw,
    seo: raw.seo ? { ...raw.seo, image: fix(raw.seo.image) } : raw.seo,
    branding: { ...raw.branding, logo: fix(raw.branding.logo), cover: fix(raw.branding.cover) },
    banner: raw.banner ? { ...raw.banner, image: fix(raw.banner.image) } : raw.banner,
    products: raw.products?.map((p) => ({ ...p, image: fix(p.image) })),
  };
}

/** Lojas de demonstração usam o WhatsApp da plataforma (se configurado) para nunca enviar mensagem a terceiros. */
function applyDemoRules(menu: StoreMenu): StoreMenu {
  if (!menu.isDemo) return menu;
  return { ...menu, contact: { ...menu.contact, whatsapp: env.platformWhatsapp } };
}

async function readLocal(slug: string): Promise<unknown | null> {
  try {
    const file = await fs.readFile(path.join(STORES_DIR, slug, "store.json"), "utf8");
    return resolveLocalImages(JSON.parse(file));
  } catch (e) {
    if ((e as NodeJS.ErrnoException).code === "ENOENT") return null;
    throw e;
  }
}

async function readSupabase(slug: string): Promise<unknown | null> {
  const { data, error } = await supabase().rpc("get_store_menu", { p_slug: slug });
  if (error) throw new Error(`Supabase get_store_menu("${slug}"): ${error.message}`);
  return data ?? null;
}

export const getStore = cache(async (slug: string): Promise<StoreMenu | null> => {
  if (!SLUG_RE.test(slug) || RESERVED_SLUGS.has(slug)) return null;
  const raw = activeSource() === "supabase" ? await readSupabase(slug) : await readLocal(slug);
  if (!raw) return null;
  const { menu, issues } = parseStore(raw);
  if (!menu) {
    console.error(`[açaí-menu] loja "${slug}" com configuração inválida:\n- ${issues.join("\n- ")}`);
    throw new Error(`Configuração inválida da loja "${slug}".`);
  }
  if (issues.length) console.warn(`[açaí-menu] loja "${slug}": ${issues.length} aviso(s):\n- ${issues.join("\n- ")}`);
  if ((raw as { active?: boolean }).active === false) return null;
  return applyDemoRules(menu);
});

export interface StoreSummary {
  slug: string;
  name: string;
  description: string | null;
  logo: string | null;
  primaryColor: string;
  region: string | null;
}

export async function listShowcaseStores(): Promise<StoreSummary[]> {
  if (activeSource() === "supabase") {
    const { data, error } = await supabase().rpc("list_showcase_stores");
    if (error) {
      console.error("[açaí-menu] list_showcase_stores:", error.message);
      return [];
    }
    return (data ?? []).map((s: { slug: string; name: string; description: string | null; logo_url: string | null; primary_color: string; region: string | null }) => ({
      slug: s.slug, name: s.name, description: s.description, logo: s.logo_url, primaryColor: s.primary_color, region: s.region,
    }));
  }
  const out: StoreSummary[] = [];
  for (const slug of await listLocalSlugs()) {
    const raw = (await readLocal(slug)) as StoreConfigInput | null;
    if (!raw || !raw.isDemo || raw.active === false) continue;
    out.push({
      slug, name: raw.name, description: raw.description ?? null, logo: raw.branding.logo ?? null,
      primaryColor: raw.branding.primaryColor ?? "#6B21A8", region: raw.contact.region ?? null,
    });
  }
  return out;
}

async function listLocalSlugs(): Promise<string[]> {
  try {
    const entries = await fs.readdir(STORES_DIR, { withFileTypes: true });
    return entries.filter((e) => e.isDirectory() && SLUG_RE.test(e.name)).map((e) => e.name).sort();
  } catch {
    return [];
  }
}

export async function listStoreSlugs(): Promise<{ slug: string; updatedAt: Date | null }[]> {
  if (activeSource() === "supabase") {
    const { data, error } = await supabase().rpc("list_store_slugs");
    if (error) return [];
    return (data ?? []).map((r: { slug: string; updated_at: string }) => ({ slug: r.slug, updatedAt: new Date(r.updated_at) }));
  }
  return (await listLocalSlugs()).map((slug) => ({ slug, updatedAt: null }));
}

export const STORES_ROOT = STORES_DIR;
