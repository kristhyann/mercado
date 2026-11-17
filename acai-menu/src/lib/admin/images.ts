import "server-only";
import sharp from "sharp";

export type ImageKind = "logo" | "cover" | "banner" | "product" | "seo";

const PRESETS: Record<ImageKind, { width: number; height: number; fit: "cover" | "inside" }> = {
  logo: { width: 512, height: 512, fit: "cover" },
  cover: { width: 1800, height: 900, fit: "inside" },
  banner: { width: 1400, height: 700, fit: "inside" },
  product: { width: 1200, height: 1200, fit: "inside" },
  seo: { width: 1200, height: 630, fit: "cover" },
};

const ACCEPTED = new Set(["image/jpeg", "image/png", "image/webp", "image/avif", "image/gif", "image/heic", "image/heif"]);
export const MAX_UPLOAD_BYTES = 8 * 1024 * 1024;

/** Valida e otimiza a imagem (redimensiona, corrige rotação, remove metadados, converte para WebP). */
export async function optimizeImage(file: File, kind: ImageKind): Promise<Buffer> {
  if (!PRESETS[kind]) throw new Error("Tipo de imagem inválido.");
  if (!ACCEPTED.has(file.type)) throw new Error("Formato não suportado. Envie JPG, PNG, WebP ou AVIF.");
  if (file.size > MAX_UPLOAD_BYTES) throw new Error("Imagem muito grande (máximo 8 MB).");
  const input = Buffer.from(await file.arrayBuffer());
  const p = PRESETS[kind];
  try {
    return await sharp(input, { limitInputPixels: 50_000_000, animated: false })
      .rotate()
      .resize({ width: p.width, height: p.height, fit: p.fit, withoutEnlargement: p.fit === "inside", position: "attention" })
      .webp({ quality: 80, effort: 4 })
      .toBuffer();
  } catch {
    throw new Error("Não foi possível ler esta imagem. Tente outro arquivo (JPG ou PNG).");
  }
}
