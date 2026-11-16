/** Leitura centralizada das variáveis de ambiente (somente no servidor). */
export const env = {
  siteUrl: (process.env.NEXT_PUBLIC_SITE_URL || (process.env.VERCEL_PROJECT_PRODUCTION_URL ? `https://${process.env.VERCEL_PROJECT_PRODUCTION_URL}` : "http://localhost:3000")).replace(/\/$/, ""),
  supabaseUrl: process.env.SUPABASE_URL || "",
  supabaseAnonKey: process.env.SUPABASE_ANON_KEY || "",
  dataSource: (process.env.DATA_SOURCE || "auto") as "auto" | "supabase" | "local",
  platformWhatsapp: (process.env.NEXT_PUBLIC_PLATFORM_WHATSAPP || "").replace(/\D/g, ""),
  revalidateSecret: process.env.REVALIDATE_SECRET || "",
};

export function activeSource(): "supabase" | "local" {
  if (env.dataSource === "local") return "local";
  if (env.dataSource === "supabase") return "supabase";
  return env.supabaseUrl && env.supabaseAnonKey ? "supabase" : "local";
}
