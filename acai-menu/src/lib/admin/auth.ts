import "server-only";
import crypto from "node:crypto";
import { cookies } from "next/headers";
import { redirect } from "next/navigation";
import { adminMode } from "./mode";
import { supabaseSession } from "./supabase-session";

export interface AdminSession {
  mode: "supabase" | "local";
  email: string;
}

const LOCAL_COOKIE = "acai_admin_local";
const LOCAL_TTL = 12 * 60 * 60 * 1000;

function localSecret() {
  return crypto.createHash("sha256").update(`acai-menu:${process.env.ADMIN_LOCAL_PASSWORD ?? ""}:${process.env.ADMIN_SESSION_SECRET ?? ""}`).digest();
}
function sign(payload: string) {
  return crypto.createHmac("sha256", localSecret()).update(payload).digest("base64url");
}
function safeEqual(a: string, b: string) {
  const A = Buffer.from(a), B = Buffer.from(b);
  return A.length === B.length && crypto.timingSafeEqual(A, B);
}

/** Retorna a sessão do administrador ou null. Toda verificação acontece no servidor. */
export async function getAdminSession(): Promise<AdminSession | null> {
  const mode = adminMode();
  if (mode === "supabase") {
    const sb = await supabaseSession();
    // getUser() valida o token no servidor de autenticação (não confia só no cookie).
    const { data, error } = await sb.auth.getUser();
    if (error || !data.user) return null;
    const { data: isAdmin, error: e2 } = await sb.rpc("is_platform_admin");
    if (e2 || isAdmin !== true) return null;
    return { mode, email: data.user.email ?? "" };
  }
  if (mode === "local") {
    const raw = (await cookies()).get(LOCAL_COOKIE)?.value ?? "";
    const [exp, sig] = raw.split(".");
    if (!exp || !sig || Number(exp) < Date.now() || !safeEqual(sig, sign(`admin.${exp}`))) return null;
    return { mode, email: "admin@local" };
  }
  return null;
}

/** Para páginas do painel: redireciona ao login se não for administrador. */
export async function requireAdminPage(): Promise<AdminSession> {
  const s = await getAdminSession();
  if (!s) redirect("/admin/login");
  return s;
}

export class AdminAuthError extends Error {
  constructor() {
    super("Sessão expirada ou acesso negado. Entre novamente.");
  }
}

/** Para ações (gravações): lança erro se não for administrador. */
export async function requireAdminAction(): Promise<AdminSession> {
  const s = await getAdminSession();
  if (!s) throw new AdminAuthError();
  return s;
}

// ─── Login / logout ─────────────────────────────────────────────────────────
const attempts = new Map<string, { n: number; until: number }>();

export async function login(email: string, password: string, ip: string): Promise<string | null> {
  const key = ip || "?";
  const a = attempts.get(key);
  if (a && a.until > Date.now()) return "Muitas tentativas. Aguarde alguns minutos e tente novamente.";
  const fail = async (msg: string) => {
    const cur = attempts.get(key) ?? { n: 0, until: 0 };
    cur.n += 1;
    if (cur.n >= 5) {
      cur.until = Date.now() + 5 * 60 * 1000;
      cur.n = 0;
    }
    attempts.set(key, cur);
    await new Promise((r) => setTimeout(r, 600));
    return msg;
  };

  const mode = adminMode();
  if (mode === "supabase") {
    const sb = await supabaseSession();
    const { error } = await sb.auth.signInWithPassword({ email: email.trim(), password });
    if (error) return fail("E-mail ou senha incorretos.");
    const { data: isAdmin } = await sb.rpc("is_platform_admin");
    if (isAdmin !== true) {
      await sb.auth.signOut();
      return fail("Este usuário não tem acesso ao painel.");
    }
    attempts.delete(key);
    return null;
  }
  if (mode === "local") {
    const expected = process.env.ADMIN_LOCAL_PASSWORD ?? "";
    if (!expected || !safeEqual(crypto.createHash("sha256").update(password).digest("hex"), crypto.createHash("sha256").update(expected).digest("hex"))) {
      return fail("Senha incorreta.");
    }
    const exp = String(Date.now() + LOCAL_TTL);
    (await cookies()).set(LOCAL_COOKIE, `${exp}.${sign(`admin.${exp}`)}`, { httpOnly: true, sameSite: "lax", path: "/", secure: false, maxAge: LOCAL_TTL / 1000 });
    attempts.delete(key);
    return null;
  }
  return "Painel não configurado. Veja a seção Painel administrativo no README.";
}

export async function logout() {
  const mode = adminMode();
  if (mode === "supabase") await (await supabaseSession()).auth.signOut();
  (await cookies()).delete(LOCAL_COOKIE);
}
