/**
 * Revalidação imediata do cache de uma loja, chamada pelo script `npm run store:sync`.
 * POST /api/revalidate  { "slug": "acai-da-maria" }  com header  Authorization: Bearer <REVALIDATE_SECRET>
 */
import { revalidatePath } from "next/cache";
import { timingSafeEqual } from "node:crypto";
import { env } from "@/lib/env";

function authorized(req: Request) {
  const header = req.headers.get("authorization") ?? "";
  const token = header.replace(/^Bearer\s+/i, "");
  if (!env.revalidateSecret || !token) return false;
  const a = Buffer.from(token);
  const b = Buffer.from(env.revalidateSecret);
  return a.length === b.length && timingSafeEqual(a, b);
}

export async function POST(req: Request) {
  if (!authorized(req)) return Response.json({ ok: false, error: "não autorizado" }, { status: 401 });
  let slug = "";
  try {
    slug = String((await req.json()).slug ?? "");
  } catch {
    /* corpo inválido */
  }
  if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(slug)) return Response.json({ ok: false, error: "slug inválido" }, { status: 400 });
  revalidatePath(`/${slug}`);
  revalidatePath(`/${slug}/checkout`);
  revalidatePath(`/${slug}`, "layout");
  revalidatePath("/");
  revalidatePath("/sitemap.xml");
  return Response.json({ ok: true, slug, revalidatedAt: new Date().toISOString() });
}
