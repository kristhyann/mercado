/**
 * Serve imagens da pasta stores/<slug>/images no MODO LOCAL (lojas de demonstração
 * e desenvolvimento). Em produção com Supabase, as imagens vêm do Supabase Storage.
 */
import fs from "node:fs/promises";
import path from "node:path";
import { STORES_ROOT } from "@/lib/data";

const TYPES: Record<string, string> = {
  ".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
  ".webp": "image/webp", ".avif": "image/avif", ".gif": "image/gif",
};

export async function GET(_req: Request, { params }: { params: Promise<{ slug: string; path: string[] }> }) {
  const { slug, path: parts } = await params;
  if (!/^[a-z0-9-]+$/.test(slug) || parts.some((p) => p === ".." || p.includes("\\") || p.startsWith("."))) {
    return new Response("Not found", { status: 404 });
  }
  const base = path.join(STORES_ROOT, slug);
  const file = path.normalize(path.join(base, ...parts));
  const type = TYPES[path.extname(file).toLowerCase()];
  if (!file.startsWith(base + path.sep) || !type) return new Response("Not found", { status: 404 });
  try {
    const data = await fs.readFile(file);
    return new Response(new Uint8Array(data), {
      headers: {
        "Content-Type": type,
        "Cache-Control": "public, max-age=3600, stale-while-revalidate=86400",
        ...(type === "image/svg+xml" ? { "Content-Security-Policy": "default-src 'none'; style-src 'unsafe-inline'; sandbox" } : {}),
      },
    });
  } catch {
    return new Response("Not found", { status: 404 });
  }
}
