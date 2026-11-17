/**
 * Duplica uma loja inteira (cardápio, opções, imagens) para um novo cliente:
 *   npm run store:duplicate -- acai-da-maria acai-do-joao "Açaí do João"
 */
import fs from "node:fs";
import path from "node:path";
import { STORES, c, die, positional, readRaw, storeFile } from "./_shared";

const [from, slug, name] = positional();
if (!from || !slug || !name) die('Uso: npm run store:duplicate -- <loja-origem> <novo-slug> "<Novo nome>"');
if (!/^[a-z0-9]+(-[a-z0-9]+)*$/.test(slug)) die(`Slug inválido: "${slug}"`);
if (fs.existsSync(path.join(STORES, slug))) die(`stores/${slug} já existe.`);
const raw = readRaw(from);
fs.cpSync(path.join(STORES, from), path.join(STORES, slug), { recursive: true });
raw.slug = slug;
raw.name = name;
raw.isDemo = false;
raw.contact.whatsapp = "550000000000";
if (raw.seo) raw.seo.title = `${name} — Cardápio e pedidos pelo WhatsApp`;
fs.writeFileSync(storeFile(slug), JSON.stringify(raw, null, 2) + "\n");
c.ok(`stores/${from} → stores/${slug}`);
c.warn(`Ajuste contact.whatsapp, endereço, cores, logo e preços em stores/${slug}/store.json antes de sincronizar.`);
