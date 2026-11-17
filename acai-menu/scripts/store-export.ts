/**
 * Baixa do Supabase a configuração atual de uma loja para stores/<slug>/store.json
 * (útil se alguém editou direto no painel do Supabase). Faz backup do arquivo anterior.
 *   npm run store:export -- acai-do-joao
 */
import fs from "node:fs";
import path from "node:path";
import { STORES, admin, c, die, positional, storeFile } from "./_shared";

(async () => {
  const [slug] = positional();
  if (!slug) die("Uso: npm run store:export -- <slug>");
  const { data, error } = await admin().rpc("get_store_menu", { p_slug: slug });
  if (error) die(error.message);
  if (!data) die(`Loja "${slug}" não existe no Supabase.`);
  fs.mkdirSync(path.join(STORES, slug), { recursive: true });
  if (fs.existsSync(storeFile(slug))) {
    const bak = storeFile(slug).replace(/\.json$/, `.backup-${Date.now()}.json`);
    fs.copyFileSync(storeFile(slug), bak);
    c.info(`Backup: ${path.relative(process.cwd(), bak)}`);
  }
  fs.writeFileSync(storeFile(slug), JSON.stringify({ $schema: "../store.schema.json", ...data }, null, 2) + "\n");
  c.ok(`Exportado para stores/${slug}/store.json`);
})();
