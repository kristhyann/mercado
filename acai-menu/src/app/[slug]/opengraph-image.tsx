/**
 * Imagem de compartilhamento gerada automaticamente para cada loja
 * (aparece no WhatsApp, Instagram, Facebook). Se a loja tiver seo.image,
 * aquela imagem é usada no lugar desta.
 */
import { ImageResponse } from "next/og";
import fs from "node:fs/promises";
import path from "node:path";
import { getStore, STORES_ROOT } from "@/lib/data";
import { mix } from "@/lib/theme";

export const alt = "Cardápio digital";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";
export const revalidate = 3600;

async function toDataUri(src: string | null): Promise<string | null> {
  if (!src) return null;
  try {
    if (src.startsWith("/assets/")) {
      const [, , slug, ...rest] = src.split("/");
      const file = path.join(STORES_ROOT, slug, ...rest);
      if (!file.startsWith(STORES_ROOT)) return null;
      const buf = await fs.readFile(file);
      const type = file.endsWith(".svg") ? "image/svg+xml" : file.endsWith(".png") ? "image/png" : "image/jpeg";
      return `data:${type};base64,${buf.toString("base64")}`;
    }
    if (/^https:\/\//.test(src)) {
      const res = await fetch(src);
      if (!res.ok) return null;
      const type = res.headers.get("content-type") ?? "image/png";
      if (type.includes("webp") || type.includes("avif")) return null; // não suportado pelo gerador
      return `data:${type};base64,${Buffer.from(await res.arrayBuffer()).toString("base64")}`;
    }
  } catch {
    return null;
  }
  return null;
}

export default async function OgImage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const menu = await getStore(slug);
  const name = menu?.name ?? "Cardápio digital";
  const primary = menu?.branding.primaryColor ?? "#6B21A8";
  const secondary = menu?.branding.secondaryColor ?? "#F59E0B";
  const logo = await toDataUri(menu?.branding.logo ?? null);
  const tagline = menu?.banner.title ?? "Monte seu açaí e peça pelo WhatsApp";

  return new ImageResponse(
    (
      <div
        style={{
          width: "100%", height: "100%", display: "flex", alignItems: "center", padding: "72px",
          background: `linear-gradient(135deg, ${mix(primary, "#000000", 0.35)} 0%, ${primary} 55%, ${mix(primary, secondary, 0.5)} 100%)`,
          color: "white", fontFamily: "sans-serif",
        }}
      >
        <div style={{ display: "flex", position: "absolute", right: -120, top: -120, width: 520, height: 520, borderRadius: 9999, background: "rgba(255,255,255,0.08)" }} />
        <div style={{ display: "flex", position: "absolute", right: 80, bottom: -160, width: 380, height: 380, borderRadius: 9999, background: "rgba(255,255,255,0.06)" }} />
        {logo ? (
          // eslint-disable-next-line @next/next/no-img-element
          <img src={logo} width={260} height={260} style={{ borderRadius: 56, border: "8px solid rgba(255,255,255,0.9)", objectFit: "cover" }} alt="" />
        ) : (
          <div style={{ display: "flex", width: 260, height: 260, borderRadius: 56, background: "white", color: primary, fontSize: 140, fontWeight: 800, alignItems: "center", justifyContent: "center" }}>
            {name[0]}
          </div>
        )}
        <div style={{ display: "flex", flexDirection: "column", marginLeft: 56, flex: 1 }}>
          <div style={{ fontSize: 30, fontWeight: 600, opacity: 0.85, letterSpacing: 2 }}>CARDÁPIO DIGITAL</div>
          <div style={{ fontSize: name.length > 18 ? 76 : 92, fontWeight: 800, lineHeight: 1.05, marginTop: 8 }}>{name}</div>
          <div style={{ fontSize: 34, marginTop: 20, opacity: 0.92 }}>{tagline}</div>
          <div style={{ display: "flex", marginTop: 36 }}>
            <div style={{ display: "flex", background: secondary, color: "#1c1022", fontSize: 30, fontWeight: 800, padding: "14px 28px", borderRadius: 9999 }}>
              Peça pelo WhatsApp →
            </div>
          </div>
        </div>
      </div>
    ),
    size,
  );
}
