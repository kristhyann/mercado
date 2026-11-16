import { describe, expect, it } from "vitest";
import { clampSelections, priceItem, validateItem } from "@/lib/pricing";
import { loadMenu, product } from "./helpers";

const monte = product("acai-da-maria", "monte-seu-acai");

describe("personalização e cálculo de preço", () => {
  it("cada tamanho tem seu preço", () => {
    const prices = Object.fromEntries(monte.variants.map((v) => [v.name, v.price]));
    expect(prices).toEqual({ "300 ml": 1200, "400 ml": 1500, "500 ml": 1800, "700 ml": 2300, "1 litro": 3200 });
  });

  it("exemplo do enunciado: 500 ml + 3 acompanhamentos grátis + Nutella extra = R$ 21,00", () => {
    const sel = {
      base: { tradicional: 1 },
      acompanhamentos: { banana: 1, "leite-em-po": 1, granola: 1 },
      adicionais: { "nutella-extra": 1 },
    };
    expect(validateItem(monte, "500ml", sel)).toEqual([]);
    const p = priceItem(monte, "500ml", sel);
    expect(p.unitPrice).toBe(2100);
    expect(p.groups.find((g) => g.key === "acompanhamentos")!.charge).toBe(0);
  });

  it("acompanhamentos acima do limite grátis são cobrados automaticamente", () => {
    const sel = { base: { tradicional: 1 }, acompanhamentos: { banana: 1, granola: 1, morango: 1, pacoca: 1, confete: 1 } };
    // 500 ml: 3 grátis, extra R$ 2,00 → 2 extras = R$ 4,00
    expect(priceItem(monte, "500ml", sel).unitPrice).toBe(1800 + 400);
    // 1 litro: 5 grátis → nada extra
    expect(priceItem(monte, "1l", sel).unitPrice).toBe(3200);
  });

  it("opção 'sempre paga' não consome as grátis (zero açúcar, Nutella)", () => {
    const sel = { base: { "zero-acucar": 1 }, coberturas: { "cobertura-nutella": 1, "leite-condensado": 1 } };
    // base +2,00 · Nutella +3,00 · leite condensado é a 1ª grátis
    expect(priceItem(monte, "300ml", sel).unitPrice).toBe(1200 + 200 + 300);
  });

  it("adicionais pagos podem repetir até o limite por opção", () => {
    const sel = { base: { tradicional: 1 }, adicionais: { "nutella-extra": 2, "kit-kat": 1 } };
    expect(priceItem(monte, "300ml", sel).unitPrice).toBe(1200 + 600 + 350);
    expect(validateItem(monte, "300ml", { ...sel, adicionais: { "nutella-extra": 4 } })[0].message).toMatch(/Máximo de 3x/);
  });

  it("opção obrigatória e limite máximo são validados", () => {
    expect(validateItem(monte, "500ml", {}).map((i) => i.groupKey)).toContain("base");
    const muitos = { base: { tradicional: 1 }, acompanhamentos: { banana: 1, granola: 1, morango: 1, pacoca: 1, confete: 1, granulado: 1, sucrilhos: 1 } };
    expect(validateItem(monte, "500ml", muitos).some((i) => /no máximo 6/.test(i.message))).toBe(true);
    expect(validateItem(monte, null, { base: { tradicional: 1 } })[0].message).toMatch(/tamanho/i);
  });

  it("opção esgotada não pode ser escolhida", () => {
    const issues = validateItem(monte, "500ml", { base: { tradicional: 1 }, acompanhamentos: { kiwi: 1 } });
    expect(issues[0].message).toMatch(/esgotado/);
  });

  it("trocar para tamanho menor remove o excesso de escolhas", () => {
    const sel = { base: { tradicional: 1 }, acompanhamentos: { banana: 1, granola: 1, morango: 1, pacoca: 1, confete: 1, granulado: 1, sucrilhos: 1, amendoim: 1 } };
    const clamped = clampSelections(monte, "300ml", sel);
    expect(Object.keys(clamped.acompanhamentos)).toHaveLength(5);
  });

  it("produto herdado (extends) recebe as opções do original", () => {
    const morango = product("acai-da-maria", "acai-com-morango");
    expect(morango.groups.map((g) => g.group.key)).toEqual(["coberturas", "adicionais", "talheres"]);
    expect(morango.variants.map((v) => v.price)).toEqual([1100, 1600, 2100]);
    const promo = product("acai-da-maria", "promo-500-do-dia");
    expect(promo.fromPrice).toBe(1590);
    expect(promo.fromCompareAtPrice).toBe(1800);
    expect(promo.groups.length).toBe(6);
  });

  it("produto indisponível aparece mas não pode ser pedido", () => {
    const pacoca = product("acai-da-maria", "acai-com-pacoca");
    expect(pacoca.available).toBe(false);
    expect(validateItem(pacoca, "300ml", {})[0].message).toMatch(/indisponível/);
  });

  it("produtos simples (bebidas) não exigem personalização", () => {
    const coca = product("acai-da-maria", "coca-lata");
    expect(coca.isSimple).toBe(true);
    expect(priceItem(coca, "padrao", {}).unitPrice).toBe(600);
  });

  it("barca: tamanho maior libera mais acompanhamentos grátis", () => {
    const barca = product("acai-da-maria", "barca-acai");
    const sel = { base: { tradicional: 1 }, acompanhamentos: Object.fromEntries(["banana", "granola", "morango", "pacoca", "confete", "granulado", "sucrilhos"].map((k) => [k, 1])) };
    expect(priceItem(barca, "pequena", sel).addons).toBe(600); // 4 grátis, 3 extras (e 7 > máx. 6: validação acusa)
    expect(validateItem(barca, "pequena", sel).length).toBeGreaterThan(0);
    expect(priceItem(barca, "media", sel).addons).toBe(200); // 6 grátis, 1 extra
    expect(priceItem(barca, "grande", sel).addons).toBe(0);
  });

  it("lojas diferentes têm cardápios diferentes", () => {
    const names = (slug: string) => loadMenu(slug).categories.map((c) => c.name);
    expect(names("acai-da-maria")).toContain("Barcas");
    expect(names("acai-premium")).not.toContain("Barcas");
  });
});
