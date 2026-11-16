/**
 * Publica uma loja (ou todas) no Supabase:
 *   npm run store:sync -- acai-do-joao
 *   npm run store:sync -- --all
 *   npm run store:sync -- acai-do-joao --dry-run   (só valida e mostra o que faria)
 *
 * 1. Valida o store.json.
 * 2. Envia as imagens locais (caminhos relativos, ex.: images/logo.png) para o Supabase Storage.
 * 3. Grava tudo de forma atômica com admin_sync_store() (tudo ou nada).
 * 4. Pede ao site para atualizar o cache da loja na hora.
 */
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { STORES, admin, arg, c, die, listSlugs, positional, readRaw, validate } from "./_shared";
import { toSyncPayload } from "../src/lib/sync-payload";
import type { StoreConfig } from "../src/lib/schema";

const MIME: Record<string, string> = { ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp", ".avif": "image/avif", ".svg": "image/svg+xml", ".gif": "image/gif" };
const bucket = process.env.SUPABASE_STORAGE_BUCKET || "store-assets";
const dry = arg("--dry-run");

const isLocal = (v: string | null | undefined): v is string => Boolean(v) && !/^(https?:)?\/\//.test(v!) && !v!.startsWith("data:");

async function uploadImages(slug: string, config: StoreConfig) {
  const sb = dry && !process.env.SUPABASE_URL ? null : admin();
  const cache = new Map<string, string>();
  const up = async (ref: string | null | undefined): Promise<string | null> => {
    if (!isLocal(ref)) return ref ?? null;
    if (cache.has(ref)) return cache.get(ref)!;
    const file = path.resolve(STORES, slug, ref.replace(/^\//, ""));
    if (!file.startsWith(path.join(STORES, slug))) die(`Caminho de imagem fora da pasta da loja: ${ref}`);
    if (!fs.existsSync(file)) die(`Imagem não encontrada: stores/${slug}/${ref}`);
    const ext = path.extname(file).toLowerCase();
    if (!MIME[ext]) die(`Formato não suportado: ${ref} (use jpg, png, webp, avif ou svg)`);
    const data = fs.readFileSync(file);
    if (data.length > 5 * 1024 * 1024) die(`Imagem maior que 5 MB: ${ref}. Reduza antes de enviar.`);
    // Nome com hash do conteúdo: trocar a foto gera URL nova (sem cache antigo).
    const hash = crypto.createHash("sha1").update(data).digest("hex").slice(0, 10);
    const key = `${slug}/${path.basename(file, ext).replace(/[^a-z0-9-]/gi, "-").toLowerCase()}-${hash}${ext}`;
    if (!dry && sb) {
      const { error } = await sb.storage.from(bucket).upload(key, data, { contentType: MIME[ext], upsert: true, cacheControl: "31536000" });
      if (error) die(`Falha ao enviar ${ref}: ${error.message}`);
    }
    if (!dry && !sb) die("Supabase não configurado.");
    const url = sb ? sb.storage.from(bucket).getPublicUrl(key).data.publicUrl : `(storage)/${bucket}/${key}`;
    cache.set(ref, url);
    return url;
  };
  config.branding.logo = await up(config.branding.logo);
  config.branding.cover = await up(config.branding.cover);
  config.banner.image = await up(config.banner.image);
  config.seo.image = await up(config.seo.image);
  for (const p of config.products) if (p.image !== undefined) p.image = await up(p.image);
  return cache.size;
}

async function revalidate(slug: string) {
  const site = process.env.NEXT_PUBLIC_SITE_URL;
  const secret = process.env.REVALIDATE_SECRET;
  if (!site || !secret || site.includes("localhost")) {
    c.warn("Cache do site não revalidado (defina NEXT_PUBLIC_SITE_URL e REVALIDATE_SECRET). A loja atualiza sozinha em até 60 s.");
    return;
  }
  try {
    const res = await fetch(`${site.replace(/\/$/, "")}/api/revalidate`, {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${secret}` },
      body: JSON.stringify({ slug }),
    });
    if (res.ok) c.ok(`Site atualizado: ${site}/${slug}`);
    else c.warn(`Revalidação respondeu ${res.status}. A loja atualiza sozinha em até 60 s.`);
  } catch (e) {
    c.warn(`Não foi possível revalidar (${(e as Error).message}). A loja atualiza sozinha em até 60 s.`);
  }
}

async function syncOne(slug: string) {
  const config = validate(slug, readRaw(slug));
  if (!config) return false;
  const n = await uploadImages(slug, config);
  c.ok(`${slug}: ${n} imagem(ns) ${dry ? "seriam enviadas" : "enviadas"} ao Storage`);
  const payload = toSyncPayload(config);
  if (dry) {
    c.info(`(dry-run) ${payload.products.length} produtos seriam gravados.`);
    return true;
  }
  const { data, error } = await admin().rpc("admin_sync_store", { payload });
  if (error) {
    c.err(`${slug}: erro no Supabase: ${error.message}`);
    if (/function .* does not exist/i.test(error.message)) c.info("Execute os arquivos de supabase/migrations no SQL Editor do Supabase.");
    return false;
  }
  c.ok(`${slug}: publicado (${(data as { products: number }).products} produtos)`);
  await revalidate(slug);
  return true;
}

(async () => {
  const slugs = arg("--all") ? listSlugs() : positional();
  if (!slugs.length) die("Uso: npm run store:sync -- <slug> | --all [--dry-run]");
  let fail = 0;
  for (const s of slugs) if (!(await syncOne(s))) fail++;
  process.exit(fail ? 1 : 0);
})();
