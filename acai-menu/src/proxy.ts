/**
 * Proxy (antigo middleware) — apenas para /admin:
 *  - renova a sessão do Supabase (tokens expiram a cada hora);
 *  - redireciona para /admin/login quem não tem sessão.
 * A autorização de verdade (é administrador?) é feita no servidor em cada
 * página e em cada ação do painel.
 */
import { NextResponse, type NextRequest } from "next/server";
import { createServerClient } from "@supabase/ssr";

export async function proxy(request: NextRequest) {
  const { pathname } = request.nextUrl;
  const isLogin = pathname === "/admin/login";
  let response = NextResponse.next({ request });
  response.headers.set("X-Robots-Tag", "noindex, nofollow");
  response.headers.set("Cache-Control", "private, no-store");

  const url = process.env.SUPABASE_URL;
  const key = process.env.SUPABASE_ANON_KEY;
  let hasSession = Boolean(request.cookies.get("acai_admin_local")?.value);

  if (url && key && process.env.DATA_SOURCE !== "local") {
    const secure = process.env.NODE_ENV === "production" && request.nextUrl.protocol === "https:";
    const supabase = createServerClient(url, key, {
      cookies: {
        getAll: () => request.cookies.getAll(),
        setAll: (list) => {
          list.forEach(({ name, value }) => request.cookies.set(name, value));
          response = NextResponse.next({ request });
          response.headers.set("X-Robots-Tag", "noindex, nofollow");
          response.headers.set("Cache-Control", "private, no-store");
          list.forEach(({ name, value, options }) => response.cookies.set(name, value, { ...options, httpOnly: true, sameSite: "lax", secure, path: "/" }));
        },
      },
    });
    const { data } = await supabase.auth.getUser();
    hasSession = Boolean(data.user);
  }

  if (!hasSession && !isLogin) {
    const to = request.nextUrl.clone();
    to.pathname = "/admin/login";
    to.search = "";
    return NextResponse.redirect(to);
  }
  return response;
}

export const config = { matcher: ["/admin", "/admin/:path*"] };
