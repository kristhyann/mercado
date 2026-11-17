import "server-only";
import { cookies } from "next/headers";
import { createServerClient } from "@supabase/ssr";
import { env } from "../env";

/** Cookies de sessão inacessíveis ao JavaScript da página (httpOnly) e só via HTTPS em produção. */
export const SESSION_COOKIE_OPTIONS = {
  httpOnly: true,
  secure: process.env.NODE_ENV === "production" && !env.siteUrl.startsWith("http://localhost"),
  sameSite: "lax" as const,
  path: "/",
};

/** Cliente Supabase com a sessão do administrador (chave anon + JWT do usuário). */
export async function supabaseSession() {
  const store = await cookies();
  return createServerClient(env.supabaseUrl, env.supabaseAnonKey, {
    cookieOptions: SESSION_COOKIE_OPTIONS,
    cookies: {
      getAll: () => store.getAll(),
      setAll: (list) => {
        try {
          list.forEach(({ name, value, options }) => store.set(name, value, { ...options, ...SESSION_COOKIE_OPTIONS }));
        } catch {
          // Em Server Components não é possível gravar cookies; o proxy renova a sessão.
        }
      },
    },
  });
}
