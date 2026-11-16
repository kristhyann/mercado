/**
 * Cria uma nova loja a partir do modelo:
 *   npm run store:new -- acai-do-joao "Açaí do João" 5511987654321
 */
import fs from "node:fs";
import path from "node:path";
import { STORES, c, die, positional, storeFile } from "./_shared";
import { RESERVED_SLUGS } from "../src/lib/schema";

const [slug, name, whatsapp] = positional();
if (!slug || !name) die('Uso: npm run store:new -- <slug> "<Nome da loja>" [whatsapp com DDI+DDD]');
if (!/^[a-z0-9]+(-[a-z0-9]+)*$/.test(slug) || RESERVED_SLUGS.has(slug)) die(`Slug inválido: "${slug}". Use letras minúsculas, números e hífens (ex.: acai-do-joao).`);
if (fs.existsSync(storeFile(slug))) die(`A loja "${slug}" já existe em stores/${slug}.`);
if (whatsapp && !/^\d{12,15}$/.test(whatsapp)) die("WhatsApp deve ter só dígitos com DDI 55 + DDD + número (ex.: 5511987654321).");

const template = JSON.parse(fs.readFileSync(path.join(STORES, "_modelo", "store.json"), "utf8"));
template.slug = slug;
template.name = name;
template.isDemo = false;
template.seo.title = `${name} — Cardápio e pedidos pelo WhatsApp`;
if (whatsapp) template.contact.whatsapp = whatsapp;
fs.mkdirSync(path.join(STORES, slug, "images"), { recursive: true });
fs.writeFileSync(storeFile(slug), JSON.stringify(template, null, 2) + "\n");
c.ok(`Loja criada: stores/${slug}/store.json`);
c.info("Próximos passos:");
c.info(`1. Coloque logo, capa e fotos em stores/${slug}/images/`);
c.info(`2. Edite stores/${slug}/store.json (produtos, preços, horários, entrega)`);
c.info(`3. npm run store:validate -- ${slug}`);
c.info(`4. npm run store:sync -- ${slug}`);
if (!whatsapp) c.warn("Lembre-se de preencher contact.whatsapp.");
