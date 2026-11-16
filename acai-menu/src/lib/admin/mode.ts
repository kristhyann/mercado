import { activeSource, env } from "../env";

/**
 * supabase → painel real (produção): login pelo Supabase Auth + tabela platform_admins.
 * local    → SOMENTE desenvolvimento: edita os arquivos da pasta /stores com a senha
 *            ADMIN_LOCAL_PASSWORD. Nunca é ativado na Vercel.
 * disabled → painel indisponível (falta configuração).
 */
export function adminMode(): "supabase" | "local" | "disabled" {
  if (activeSource() === "supabase") return "supabase";
  if (process.env.ADMIN_LOCAL_PASSWORD && !process.env.VERCEL) return "local";
  return "disabled";
}

export const SUPABASE_PUBLIC = { url: env.supabaseUrl, anonKey: env.supabaseAnonKey };
