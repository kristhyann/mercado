/**
 * Regras de preço da personalização (centavos).
 *
 * - Cada grupo tem "free" escolhas grátis; as excedentes são cobradas.
 * - O valor cobrado de uma escolha é o preço da opção ou, se ela não tem preço,
 *   o "extraPrice" do grupo.
 * - Opções "alwaysPaid" são sempre cobradas e não consomem as escolhas grátis.
 * - As escolhas grátis abatem primeiro as opções mais caras (sempre a favor do
 *   cliente e independente da ordem em que ele clicou).
 */
import type { AddonGroup, GroupRules, Product, ProductGroup, Variant } from "./menu";

/** { [chaveDoGrupo]: { [chaveDaOpcao]: quantidade } } */
export type Selections = Record<string, Record<string, number>>;

export interface AddonLine {
  key: string;
  name: string;
  quantity: number;
  /** Total cobrado por esta opção (0 se grátis). */
  charged: number;
}

export interface GroupBreakdown {
  key: string;
  name: string;
  count: number;
  charge: number;
  lines: AddonLine[];
}

export interface PriceBreakdown {
  base: number;
  addons: number;
  unitPrice: number;
  groups: GroupBreakdown[];
}

export function rulesFor(pg: ProductGroup, variant: Variant | undefined): GroupRules {
  const o = variant?.rules[pg.group.key] ?? {};
  return {
    min: o.min ?? pg.rules.min,
    max: o.max !== undefined ? o.max : pg.rules.max,
    free: o.free ?? pg.rules.free,
  };
}

export function countSelected(sel: Record<string, number> | undefined): number {
  if (!sel) return 0;
  return Object.values(sel).reduce((s, q) => s + (q > 0 ? q : 0), 0);
}

export function chargeFor(group: AddonGroup, rules: GroupRules, sel: Record<string, number> | undefined): GroupBreakdown {
  type Unit = { key: string; price: number; alwaysPaid: boolean; order: number };
  const units: Unit[] = [];
  const lines: AddonLine[] = [];
  group.addons.forEach((addon, order) => {
    const qty = Math.max(0, Math.floor(sel?.[addon.key] ?? 0));
    if (!qty) return;
    lines.push({ key: addon.key, name: addon.name, quantity: qty, charged: 0 });
    const price = addon.price > 0 ? addon.price : group.extraPrice;
    for (let i = 0; i < qty; i++) units.push({ key: addon.key, price, alwaysPaid: addon.alwaysPaid, order });
  });

  const lineOf = (k: string) => lines.find((l) => l.key === k)!;
  let charge = 0;
  for (const u of units.filter((u) => u.alwaysPaid)) {
    charge += u.price;
    lineOf(u.key).charged += u.price;
  }
  const regular = units.filter((u) => !u.alwaysPaid).sort((a, b) => b.price - a.price || a.order - b.order);
  regular.slice(rules.free).forEach((u) => {
    charge += u.price;
    lineOf(u.key).charged += u.price;
  });

  return { key: group.key, name: group.name, count: units.length, charge, lines };
}

export function priceItem(product: Product, variantKey: string, selections: Selections): PriceBreakdown {
  const variant = product.variants.find((v) => v.key === variantKey) ?? product.variants[0];
  const groups = product.groups.map((pg) => chargeFor(pg.group, rulesFor(pg, variant), selections[pg.group.key]));
  const addons = groups.reduce((s, g) => s + g.charge, 0);
  return { base: variant.price, addons, unitPrice: variant.price + addons, groups };
}

export interface SelectionIssue {
  groupKey: string | null;
  message: string;
}

export function validateItem(product: Product, variantKey: string | null, selections: Selections): SelectionIssue[] {
  const issues: SelectionIssue[] = [];
  if (!product.available) issues.push({ groupKey: null, message: `${product.name} está indisponível no momento.` });
  const variant = variantKey ? product.variants.find((v) => v.key === variantKey) : undefined;
  if (!variant) issues.push({ groupKey: null, message: `${product.variantLabel}.` });
  else if (!variant.available) issues.push({ groupKey: null, message: `O tamanho ${variant.name} está indisponível.` });

  const known = new Set(product.groups.map((g) => g.group.key));
  for (const gk of Object.keys(selections)) {
    if (!known.has(gk) && countSelected(selections[gk]) > 0) issues.push({ groupKey: gk, message: "Opção não disponível para este produto." });
  }

  for (const pg of product.groups) {
    const rules = rulesFor(pg, variant);
    const sel = selections[pg.group.key] ?? {};
    for (const [ak, q] of Object.entries(sel)) {
      if (q <= 0) continue;
      const addon = pg.group.addons.find((a) => a.key === ak);
      if (!addon) issues.push({ groupKey: pg.group.key, message: `Opção removida do cardápio em "${pg.group.name}".` });
      else if (!addon.available) issues.push({ groupKey: pg.group.key, message: `${addon.name} está esgotado.` });
      else if (q > pg.group.maxPerOption) issues.push({ groupKey: pg.group.key, message: `Máximo de ${pg.group.maxPerOption}x ${addon.name}.` });
    }
    const n = countSelected(sel);
    if (n < rules.min)
      issues.push({
        groupKey: pg.group.key,
        message: rules.min === 1 ? `Escolha uma opção em "${pg.group.name}".` : `Escolha pelo menos ${rules.min} em "${pg.group.name}".`,
      });
    if (rules.max !== null && n > rules.max)
      issues.push({ groupKey: pg.group.key, message: `Escolha no máximo ${rules.max} em "${pg.group.name}".` });
  }
  return issues;
}

/** Remove escolhas que deixaram de existir (útil ao trocar de tamanho). */
export function clampSelections(product: Product, variantKey: string, selections: Selections): Selections {
  const variant = product.variants.find((v) => v.key === variantKey);
  const out: Selections = {};
  for (const pg of product.groups) {
    const rules = rulesFor(pg, variant);
    const src = selections[pg.group.key] ?? {};
    const dst: Record<string, number> = {};
    let total = 0;
    for (const addon of pg.group.addons) {
      let q = Math.min(src[addon.key] ?? 0, pg.group.maxPerOption);
      if (!addon.available) q = 0;
      if (rules.max !== null) q = Math.min(q, rules.max - total);
      if (q > 0) {
        dst[addon.key] = q;
        total += q;
      }
    }
    if (Object.keys(dst).length) out[pg.group.key] = dst;
  }
  return out;
}
