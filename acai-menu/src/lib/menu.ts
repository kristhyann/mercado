/**
 * Converte a configuração (StoreConfig, em reais) no cardápio usado pelo site
 * (StoreMenu, em centavos, com produtos herdados e grupos já resolvidos).
 */
import { storeConfigSchema, type Hours, type PaymentMethod, type ProductInput, type RuleOverride, type StoreConfig } from "./schema";

export const toCents = (reais: number) => Math.round(reais * 100);

export interface Addon {
  key: string;
  name: string;
  description: string | null;
  price: number;
  alwaysPaid: boolean;
  available: boolean;
}

export interface GroupRules {
  min: number;
  max: number | null;
  free: number;
}

export interface AddonGroup extends GroupRules {
  key: string;
  name: string;
  description: string | null;
  extraPrice: number;
  maxPerOption: number;
  addons: Addon[];
}

export interface Variant {
  key: string;
  name: string;
  description: string | null;
  price: number;
  compareAtPrice: number | null;
  available: boolean;
  rules: Record<string, RuleOverride>;
}

export interface ProductGroup {
  group: AddonGroup;
  /** Regras do vínculo produto↔grupo (já com sobrescritas do produto). */
  rules: GroupRules;
}

export interface Product {
  key: string;
  categoryKey: string;
  name: string;
  description: string | null;
  image: string | null;
  variantLabel: string;
  /** Sempre ao menos 1. Produtos de preço único recebem uma variação "padrao". */
  variants: Variant[];
  hasVariantChoice: boolean;
  groups: ProductGroup[];
  badges: string[];
  featured: boolean;
  available: boolean;
  /** Sem tamanhos nem opções: pode ser adicionado direto ao carrinho. */
  isSimple: boolean;
  fromPrice: number;
  fromCompareAtPrice: number | null;
}

export interface Category {
  key: string;
  name: string;
  description: string | null;
  icon: string | null;
  products: Product[];
}

export interface DeliveryZone {
  neighborhood: string;
  fee: number;
}

export interface StoreMenu {
  slug: string;
  name: string;
  isDemo: boolean;
  description: string | null;
  seo: { title: string | null; description: string | null; image: string | null };
  branding: { logo: string | null; cover: string | null; primaryColor: string; secondaryColor: string };
  banner: { enabled: boolean; image: string | null; title: string | null; subtitle: string | null };
  contact: { whatsapp: string; instagram: string | null; address: string | null; region: string | null; mapsUrl: string | null };
  hours: Hours;
  ordering: {
    delivery: boolean;
    pickup: boolean;
    minOrder: number;
    deliveryTime: string | null;
    pickupTime: string | null;
    paymentMethods: PaymentMethod[];
    pixKey: string | null;
  };
  delivery: {
    mode: "fixed" | "zones" | "free";
    fixedFee: number;
    freeAbove: number | null;
    allowUnlistedNeighborhoods: boolean;
    zones: DeliveryZone[];
  };
  whatsappMessage: { header: string | null; footer: string | null };
  categories: Category[];
}

export class StoreConfigError extends Error {
  constructor(public issues: string[]) {
    super(`Configuração de loja inválida:\n- ${issues.join("\n- ")}`);
  }
}

/** Resolve "extends" (herança/duplicação de produtos). */
export function resolveExtends(products: ProductInput[], issues: string[]): ProductInput[] {
  const byKey = new Map(products.map((p) => [p.key, p]));
  const cache = new Map<string, ProductInput>();
  const resolve = (p: ProductInput, chain: string[]): ProductInput => {
    if (cache.has(p.key)) return cache.get(p.key)!;
    if (!p.extends) return p;
    if (chain.includes(p.extends)) {
      issues.push(`produto "${p.key}": herança circular (${[...chain, p.extends].join(" → ")})`);
      return p;
    }
    const parent = byKey.get(p.extends);
    if (!parent) {
      issues.push(`produto "${p.key}": extends "${p.extends}" não existe`);
      return p;
    }
    const base = resolve(parent, [...chain, p.key]);
    const merged: ProductInput = { ...base };
    for (const [k, v] of Object.entries(p)) if (v !== undefined) (merged as Record<string, unknown>)[k] = v;
    merged.key = p.key;
    delete merged.extends;
    cache.set(p.key, merged);
    return merged;
  };
  return products.map((p) => resolve(p, [p.key]));
}

export function buildMenu(config: StoreConfig): { menu: StoreMenu; issues: string[] } {
  const issues: string[] = [];

  const groups = new Map<string, AddonGroup>();
  for (const g of config.addonGroups) {
    const addons = g.addons
      .filter((a) => a.active)
      .map<Addon>((a) => ({
        key: a.key,
        name: a.name,
        description: a.description,
        price: toCents(a.price),
        alwaysPaid: a.alwaysPaid,
        available: a.available,
      }));
    groups.set(g.key, {
      key: g.key,
      name: g.name,
      description: g.description,
      min: g.min,
      max: g.max,
      free: g.free,
      extraPrice: toCents(g.extraPrice),
      maxPerOption: g.maxPerOption,
      addons,
    });
  }

  const categoryKeys = new Set(config.categories.map((c) => c.key));
  const products: Product[] = [];

  for (const p of resolveExtends(config.products, issues)) {
    const where = `produto "${p.key}"`;
    if (p.active === false) continue;
    if (!p.name) issues.push(`${where}: falta "name"`);
    if (!p.category) issues.push(`${where}: falta "category"`);
    else if (!categoryKeys.has(p.category)) issues.push(`${where}: categoria "${p.category}" não existe`);

    let variants: Variant[];
    let hasVariantChoice = true;
    if (p.variants && p.variants.length > 0) {
      const seen = new Set<string>();
      variants = p.variants.map((v) => {
        if (seen.has(v.key)) issues.push(`${where}: tamanho duplicado "${v.key}"`);
        seen.add(v.key);
        for (const gk of Object.keys(v.rules)) if (!groups.has(gk)) issues.push(`${where}: regra do tamanho "${v.key}" cita grupo inexistente "${gk}"`);
        return {
          key: v.key,
          name: v.name,
          description: v.description,
          price: toCents(v.price),
          compareAtPrice: v.compareAtPrice != null ? toCents(v.compareAtPrice) : null,
          available: v.available,
          rules: v.rules,
        };
      });
      hasVariantChoice = variants.length > 1;
    } else if (p.price != null) {
      hasVariantChoice = false;
      variants = [
        {
          key: "padrao",
          name: "",
          description: null,
          price: toCents(p.price),
          compareAtPrice: p.compareAtPrice != null ? toCents(p.compareAtPrice) : null,
          available: true,
          rules: {},
        },
      ];
    } else {
      issues.push(`${where}: informe "price" ou "variants"`);
      continue;
    }

    const productGroups: ProductGroup[] = [];
    for (const link of p.addonGroups ?? []) {
      const gk = typeof link === "string" ? link : link.group;
      const group = groups.get(gk);
      if (!group) {
        issues.push(`${where}: grupo de opções "${gk}" não existe`);
        continue;
      }
      if (group.addons.length === 0) continue;
      const o: RuleOverride = typeof link === "string" ? {} : link;
      productGroups.push({
        group,
        rules: {
          min: o.min ?? group.min,
          max: o.max !== undefined ? o.max : group.max,
          free: o.free ?? group.free,
        },
      });
    }

    const availableVariants = variants.filter((v) => v.available);
    const cheapest = (availableVariants.length ? availableVariants : variants).reduce((a, b) => (b.price < a.price ? b : a));

    products.push({
      key: p.key,
      categoryKey: p.category ?? "",
      name: p.name ?? p.key,
      description: p.description ?? null,
      image: p.image ?? null,
      variantLabel: p.variantLabel ?? "Escolha o tamanho",
      variants,
      hasVariantChoice,
      groups: productGroups,
      badges: p.badges ?? [],
      featured: p.featured ?? false,
      available: (p.available ?? true) && availableVariants.length > 0,
      isSimple: !hasVariantChoice && productGroups.length === 0,
      fromPrice: cheapest.price,
      fromCompareAtPrice: cheapest.compareAtPrice,
    });
  }

  const categories: Category[] = config.categories
    .filter((c) => c.active)
    .map((c) => ({
      key: c.key,
      name: c.name,
      description: c.description,
      icon: c.icon,
      products: products.filter((p) => p.categoryKey === c.key),
    }))
    .filter((c) => c.products.length > 0);

  const menu: StoreMenu = {
    slug: config.slug,
    name: config.name,
    isDemo: config.isDemo,
    description: config.description,
    seo: config.seo,
    branding: config.branding,
    banner: config.banner,
    contact: config.contact,
    hours: config.hours,
    ordering: { ...config.ordering, minOrder: toCents(config.ordering.minOrder) },
    delivery: {
      mode: config.delivery.mode,
      fixedFee: toCents(config.delivery.fixedFee),
      freeAbove: config.delivery.freeAbove != null ? toCents(config.delivery.freeAbove) : null,
      allowUnlistedNeighborhoods: config.delivery.allowUnlistedNeighborhoods,
      zones: config.delivery.zones.filter((z) => z.active).map((z) => ({ neighborhood: z.neighborhood, fee: toCents(z.fee) })),
    },
    whatsappMessage: config.whatsappMessage,
    categories,
  };
  return { menu, issues };
}

/** Verificações extras usadas no cadastro (scripts), mais rígidas que a exibição. */
export function strictIssues(config: StoreConfig): string[] {
  const out: string[] = [];
  if (config.categories.length === 0) out.push("cadastre pelo menos uma categoria");
  if (config.products.length === 0) out.push("cadastre pelo menos um produto");
  config.addonGroups.forEach((g) => {
    if (g.addons.length === 0) out.push(`grupo "${g.key}": cadastre pelo menos uma opção`);
    if (g.max !== null && g.free > g.max) out.push(`grupo "${g.key}": "free" (${g.free}) maior que "max" (${g.max})`);
  });
  const usedGroups = new Set(config.products.flatMap((p) => (p.addonGroups ?? []).map((l) => (typeof l === "string" ? l : l.group))));
  config.addonGroups.forEach((g) => {
    if (!usedGroups.has(g.key)) out.push(`aviso: grupo "${g.key}" não é usado por nenhum produto`);
  });
  return out;
}

/** Valida e monta o cardápio. Retorna todos os problemas encontrados (não para no primeiro). */
export function parseStore(raw: unknown, opts: { strict?: boolean } = {}): { config: StoreConfig | null; menu: StoreMenu | null; issues: string[] } {
  const parsed = storeConfigSchema.safeParse(raw);
  if (!parsed.success) {
    return {
      config: null,
      menu: null,
      issues: parsed.error.issues.map((i) => `${i.path.join(".") || "(raiz)"}: ${i.message}`),
    };
  }
  const { menu, issues } = buildMenu(parsed.data);
  if (opts.strict) issues.push(...strictIssues(parsed.data));
  return { config: parsed.data, menu, issues };
}

export function parseStoreOrThrow(raw: unknown): StoreMenu {
  const { menu, issues } = parseStore(raw);
  if (!menu || issues.length) throw new StoreConfigError(issues);
  return menu;
}

/** Busca um produto/variação/grupo pelas chaves (usado pelo carrinho). */
export function findProduct(menu: StoreMenu, productKey: string): Product | undefined {
  for (const c of menu.categories) {
    const p = c.products.find((x) => x.key === productKey);
    if (p) return p;
  }
  return undefined;
}
