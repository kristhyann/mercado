/** Utilitários do editor do painel (rodam no navegador e no servidor). */
import type { StoreConfig } from "../schema";

export type Product = StoreConfig["products"][number];
export type Category = StoreConfig["categories"][number];
export type AddonGroup = StoreConfig["addonGroups"][number];
export type Addon = AddonGroup["addons"][number];
export type Variant = NonNullable<Product["variants"]>[number];

export function slugify(text: string): string {
  return text
    .normalize("NFD").replace(/[̀-ͯ]/g, "")
    .toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 50) || "item";
}

export function uniqueKey(base: string, taken: Iterable<string>): string {
  const set = new Set(taken);
  const root = slugify(base);
  if (!set.has(root)) return root;
  for (let i = 2; ; i++) if (!set.has(`${root}-${i}`)) return `${root}-${i}`;
}

export function move<T>(list: T[], index: number, delta: number): T[] {
  const to = index + delta;
  if (to < 0 || to >= list.length) return list;
  const copy = [...list];
  const [item] = copy.splice(index, 1);
  copy.splice(to, 0, item);
  return copy;
}

export function clone<T>(v: T): T {
  return JSON.parse(JSON.stringify(v));
}

/** Duplica um produto logo abaixo do original, com nova chave e "(cópia)" no nome. */
export function duplicateProduct(products: Product[], key: string): Product[] {
  const i = products.findIndex((p) => p.key === key);
  if (i < 0) return products;
  const copy = clone(products[i]);
  copy.key = uniqueKey(`${products[i].key}-copia`, products.map((p) => p.key));
  copy.name = `${products[i].name ?? ""} (cópia)`;
  copy.featured = false;
  const out = [...products];
  out.splice(i + 1, 0, copy);
  return out;
}

export function groupKeyOf(link: string | { group: string }) {
  return typeof link === "string" ? link : link.group;
}

/** Todas as imagens referenciadas pela loja (para limpeza de arquivos não usados). */
export function imageRefs(c: Pick<StoreConfig, "branding" | "banner" | "seo" | "products">): string[] {
  return [c.branding.logo, c.branding.cover, c.banner?.image, c.seo?.image, ...c.products.map((p) => p.image)].filter((x): x is string => Boolean(x));
}

/** Pré-visualização: caminhos relativos (modo local) viram URLs do próprio site. */
export function previewUrl(slug: string, ref: string | null | undefined): string | null {
  if (!ref) return null;
  if (/^(https?:)?\/\//.test(ref) || ref.startsWith("/") || ref.startsWith("data:")) return ref;
  return `/assets/${slug}/${ref.replace(/^\.\//, "")}`;
}

/** Remove um grupo de opções de todos os produtos (e das regras por tamanho). */
export function removeGroupEverywhere(products: Product[], groupKey: string): Product[] {
  return products.map((p) => ({
    ...p,
    addonGroups: p.addonGroups?.filter((l) => groupKeyOf(l) !== groupKey),
    variants: p.variants?.map((v) => {
      const rules = { ...v.rules };
      delete rules[groupKey];
      return { ...v, rules };
    }),
  }));
}

/** Nomes de tamanhos usados na loja, na ordem em que aparecem. */
export function sizeNames(products: Product[]): string[] {
  const seen: string[] = [];
  for (const p of products) for (const v of p.variants ?? []) if (!seen.includes(v.name)) seen.push(v.name);
  return seen;
}

export function parseMoney(text: string): number | null {
  const t = text.replace(/[^\d,.-]/g, "").trim();
  if (!t) return null;
  const n = Number(t.includes(",") ? t.replace(/\./g, "").replace(",", ".") : t);
  return Number.isFinite(n) && n >= 0 ? Math.round(n * 100) / 100 : null;
}

export function moneyText(v: number | null | undefined): string {
  return v == null ? "" : v.toFixed(2).replace(".", ",");
}
