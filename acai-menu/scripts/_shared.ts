import fs from "node:fs";
import path from "node:path";
import { config as loadEnv } from "dotenv";
import { createClient, type SupabaseClient } from "@supabase/supabase-js";
import { parseStore } from "../src/lib/menu";

export const ROOT = path.resolve(__dirname, "..");
export const STORES = path.join(ROOT, "stores");
loadEnv({ path: path.join(ROOT, ".env.local"), quiet: true });
loadEnv({ path: path.join(ROOT, ".env"), quiet: true });

export const c = {
  ok: (s: string) => console.log(`\x1b[32m✓\x1b[0m ${s}`),
  warn: (s: string) => console.log(`\x1b[33m!\x1b[0m ${s}`),
  err: (s: string) => console.error(`\x1b[31m✗\x1b[0m ${s}`),
  info: (s: string) => console.log(`  ${s}`),
};

export function die(msg: string): never {
  c.err(msg);
  process.exit(1);
}

export function storeFile(slug: string) {
  return path.join(STORES, slug, "store.json");
}

export function listSlugs(): string[] {
  return fs.readdirSync(STORES, { withFileTypes: true })
    .filter((d) => d.isDirectory() && /^[a-z0-9]+(-[a-z0-9]+)*$/.test(d.name) && fs.existsSync(storeFile(d.name)))
    .map((d) => d.name).sort();
}

export function readRaw(slug: string): any {
  const f = storeFile(slug);
  if (!fs.existsSync(f)) die(`Arquivo não encontrado: stores/${slug}/store.json`);
  try {
    return JSON.parse(fs.readFileSync(f, "utf8"));
  } catch (e) {
    die(`JSON inválido em stores/${slug}/store.json: ${(e as Error).message}`);
  }
}

/** Valida e imprime o resultado. Retorna a config ou null. */
export function validate(slug: string, raw = readRaw(slug)) {
  const { config, menu, issues } = parseStore(raw, { strict: true });
  const errors = issues.filter((i) => !i.startsWith("aviso"));
  const warnings = issues.filter((i) => i.startsWith("aviso"));
  if (config && !config.isDemo && /^5500/.test(config.contact.whatsapp)) errors.push("contact.whatsapp ainda é o número de exemplo (550000000000). Informe o WhatsApp real da loja.");
  if (config && raw.slug !== slug) errors.push(`"slug" (${raw.slug}) diferente do nome da pasta (${slug})`);
  warnings.forEach((w) => c.warn(`${slug}: ${w}`));
  if (errors.length || !config || !menu) {
    c.err(`${slug}: ${errors.length} problema(s)`);
    errors.forEach((e) => c.info(`- ${e}`));
    return null;
  }
  const products = menu.categories.reduce((s, cat) => s + cat.products.length, 0);
  c.ok(`${slug}: válido — ${menu.categories.length} categorias, ${products} produtos ativos`);
  return config;
}

export function admin(): SupabaseClient {
  const url = process.env.SUPABASE_URL;
  const key = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!url || !key) die("Defina SUPABASE_URL e SUPABASE_SERVICE_ROLE_KEY no arquivo .env.local (veja .env.example).");
  return createClient(url, key, { auth: { persistSession: false, autoRefreshToken: false } });
}

export function arg(name: string) {
  return process.argv.includes(name);
}
export function positional(): string[] {
  return process.argv.slice(2).filter((a) => !a.startsWith("--"));
}
