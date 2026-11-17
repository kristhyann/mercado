/** Lista as lojas cadastradas no Supabase.  npm run store:list */
import { admin, c, die } from "./_shared";

(async () => {
  const { data, error } = await admin().from("stores").select("slug, name, is_active, is_demo, whatsapp, updated_at").order("slug");
  if (error) die(error.message);
  if (!data?.length) return c.warn("Nenhuma loja cadastrada no Supabase.");
  const site = (process.env.NEXT_PUBLIC_SITE_URL || "").replace(/\/$/, "");
  for (const s of data) {
    console.log(`${s.is_active ? "🟢" : "⚪"} ${s.slug.padEnd(28)} ${s.name.padEnd(28)} wa:${s.whatsapp}${s.is_demo ? "  [demo]" : ""}  ${site}/${s.slug}`);
  }
})();
