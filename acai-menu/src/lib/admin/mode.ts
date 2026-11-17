import { activeSource, env } from "../env";

/**
 * supabase → painel real (produção): login pelo Supabase Auth + tabela platform_admins.
 * local    → SOMENTE desenvolvimento: edita os arquivos da pasta /stores com a senha
 *            ADMIN_LOCAL_PASSWORD.
 * preview  → hospedado SEM Supabase (ex.: Vercel só com as lojas de demonstração):
 *            painel apenas para VISUALIZAR, com a senha ADMIN_LOCAL_PASSWORD.
 *            Nenhuma alteração é salva.
 * disabled → painel indisponível (falta configuração).
 */
export type AdminMode = "supabase" | "local" | "preview" | "disabled";

export function adminPassword(): string {
  return process.env.ADMIN_LOCAL_PASSWORD || process.env.ADMIN_DEMO_PASSWORD || "";
}

export function adminMode(): AdminMode {
  if (activeSource() === "supabase") return "supabase";
  if (!adminPassword()) return "disabled";
  return process.env.VERCEL ? "preview" : "local";
}

export const SUPABASE_PUBLIC = { url: env.supabaseUrl, anonKey: env.supabaseAnonKey };
