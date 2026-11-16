"use client";
import { useRef, useState } from "react";
import { ImagePlus, Loader2, RefreshCw, Trash2 } from "lucide-react";
import { uploadImageAction } from "@/app/admin/actions";
import { previewUrl } from "@/lib/admin/editor";
import type { ImageKind } from "@/lib/admin/images";
import { cx } from "./ui";

/** Reduz a foto no próprio aparelho antes de enviar (envio rápido mesmo no 4G). */
async function shrink(file: File, maxSide = 2000): Promise<Blob> {
  try {
    const bmp = await createImageBitmap(file);
    const scale = Math.min(1, maxSide / Math.max(bmp.width, bmp.height));
    const w = Math.round(bmp.width * scale), h = Math.round(bmp.height * scale);
    const canvas = document.createElement("canvas");
    canvas.width = w;
    canvas.height = h;
    canvas.getContext("2d")!.drawImage(bmp, 0, 0, w, h);
    const blob = await new Promise<Blob | null>((r) => canvas.toBlob(r, "image/webp", 0.88));
    if (blob && blob.size > 0 && blob.type === "image/webp") return blob;
    const jpg = await new Promise<Blob | null>((r) => canvas.toBlob(r, "image/jpeg", 0.88));
    return jpg ?? file;
  } catch {
    return file; // formato que o navegador não abre (ex.: HEIC): o servidor tenta converter
  }
}

const RATIO: Record<ImageKind, string> = { logo: "aspect-square", cover: "aspect-[5/2]", banner: "aspect-[5/2]", product: "aspect-[4/3]", seo: "aspect-[1200/630]" };
const HINT: Record<ImageKind, string> = {
  logo: "Quadrada, mínimo 512×512 px",
  cover: "Horizontal, ideal 1600×640 px",
  banner: "Horizontal, ideal 1200×480 px",
  product: "Foto do produto, ideal 1200×900 px",
  seo: "1200×630 px (prévia no WhatsApp/Instagram)",
};

export function ImageField({ slug, kind, value, onChange, label }: { slug: string; kind: ImageKind; value: string | null | undefined; onChange: (url: string | null) => void; label: string }) {
  const input = useRef<HTMLInputElement>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const src = previewUrl(slug, value);

  async function pick(file: File) {
    setError(null);
    setBusy(true);
    try {
      const blob = await shrink(file);
      if (blob.size > 4 * 1024 * 1024) throw new Error("Imagem muito grande mesmo após reduzir. Tente outra foto.");
      const fd = new FormData();
      fd.set("slug", slug);
      fd.set("kind", kind);
      fd.set("file", new File([blob], file.name.replace(/\.\w+$/, "") + (blob.type === "image/webp" ? ".webp" : ".jpg"), { type: blob.type || file.type }));
      const res = await uploadImageAction(fd);
      if (!res.ok) throw new Error(res.error);
      onChange(res.url);
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setBusy(false);
      if (input.current) input.current.value = "";
    }
  }

  return (
    <div>
      <span className="mb-1 block text-sm font-semibold text-slate-700">{label}</span>
      <div className={cx("relative overflow-hidden rounded-xl border-2 border-dashed border-slate-200 bg-slate-50", RATIO[kind], kind === "logo" ? "w-32" : "w-full max-w-md")}>
        {src ? (
          // eslint-disable-next-line @next/next/no-img-element
          <img src={src} alt="" className="absolute inset-0 size-full object-cover" />
        ) : (
          <button type="button" onClick={() => input.current?.click()} className="absolute inset-0 flex flex-col items-center justify-center gap-1 text-slate-400 hover:text-violet-600">
            <ImagePlus className="size-7" />
            <span className="text-xs font-semibold">Enviar imagem</span>
          </button>
        )}
        {busy && (
          <div className="absolute inset-0 flex items-center justify-center bg-white/70">
            <Loader2 className="size-6 animate-spin text-violet-600" />
          </div>
        )}
      </div>
      <div className="mt-2 flex flex-wrap gap-2">
        <button type="button" onClick={() => input.current?.click()} disabled={busy} className="inline-flex h-9 items-center gap-1.5 rounded-lg bg-white px-3 text-sm font-semibold text-slate-700 ring-1 ring-slate-200 hover:bg-slate-50">
          {src ? <RefreshCw className="size-4" /> : <ImagePlus className="size-4" />} {src ? "Substituir" : "Enviar"}
        </button>
        {src && (
          <button type="button" onClick={() => onChange(null)} disabled={busy} className="inline-flex h-9 items-center gap-1.5 rounded-lg px-3 text-sm font-semibold text-rose-600 hover:bg-rose-50">
            <Trash2 className="size-4" /> Remover
          </button>
        )}
      </div>
      <p className="mt-1 text-xs text-slate-500">{HINT[kind]} · JPG, PNG ou WebP. Otimizada automaticamente.</p>
      {error && <p className="mt-1 text-xs font-semibold text-rose-600">{error}</p>}
      <input ref={input} type="file" accept="image/jpeg,image/png,image/webp,image/avif,image/heic,image/heif" className="hidden" onChange={(e) => e.target.files?.[0] && pick(e.target.files[0])} />
    </div>
  );
}
