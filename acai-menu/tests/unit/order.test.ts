import { describe, expect, it } from "vitest";
import {
  buildOrderMessage, computeTotals, evaluateCart, quoteDelivery, validateCustomer, whatsappUrl,
  UNLISTED_NEIGHBORHOOD, type CartItem, type CustomerInfo,
} from "@/lib/order";
import { parseBRL, formatBRL, maskPhone } from "@/lib/format";
import { loadMenu } from "./helpers";

const maria = loadMenu("acai-da-maria");
const tropical = loadMenu("acai-tropical");
const premium = loadMenu("acai-premium");

const item = (over: Partial<CartItem>): CartItem => ({
  id: Math.random().toString(36).slice(2), productKey: "monte-seu-acai", variantKey: "500ml",
  selections: {}, quantity: 1, notes: "", addedAt: 0, ...over,
});

const cart: CartItem[] = [
  item({ selections: { base: { tradicional: 1 }, acompanhamentos: { banana: 1, "leite-em-po": 1, granola: 1 }, adicionais: { "nutella-extra": 1 } } }),
  item({ variantKey: "300ml", selections: { base: { "com-morango": 1 }, acompanhamentos: { pacoca: 1 }, coberturas: { "leite-condensado": 1 } } }),
];

const customer = (over: Partial<CustomerInfo> = {}): CustomerInfo => ({
  name: "João Silva", phone: "(11) 98765-4321", type: "delivery",
  address: { cep: "", street: "Rua das Flores", number: "123", neighborhood: "Centro", complement: "", reference: "" },
  payment: "pix", needsChange: false, changeFor: null, notes: "Entregar na portaria.", scheduledFor: null, ...over,
});

describe("carrinho", () => {
  it("soma subtotal e quantidade", () => {
    const ev = evaluateCart(maria, cart);
    expect(ev.subtotal).toBe(2100 + 1200);
    expect(ev.count).toBe(2);
    const ev2 = evaluateCart(maria, [{ ...cart[0], quantity: 3 }]);
    expect(ev2.subtotal).toBe(6300);
    expect(ev2.count).toBe(3);
  });

  it("descarta itens que saíram do cardápio ou ficaram inválidos", () => {
    const ev = evaluateCart(maria, [item({ productKey: "nao-existe" }), item({ selections: {} })]);
    expect(ev.lines).toHaveLength(0);
    expect(ev.invalid).toHaveLength(2);
  });

  it("um carrinho de uma loja não vale em outra", () => {
    const ev = evaluateCart(premium, cart);
    expect(ev.lines).toHaveLength(0);
  });
});

describe("taxa de entrega", () => {
  it("por bairro (sem inventar taxa para bairro não cadastrado)", () => {
    expect(quoteDelivery(maria, "delivery", "Centro", 3300).fee).toBe(400);
    expect(quoteDelivery(maria, "delivery", "vila nova", 3300).fee).toBe(700);
    const fora = quoteDelivery(maria, "delivery", UNLISTED_NEIGHBORHOOD, 3300);
    expect(fora.allowed).toBe(false);
    expect(fora.fee).toBeNull();
    expect(quoteDelivery(maria, "delivery", "Bairro Inventado", 3300).allowed).toBe(false);
  });
  it("taxa fixa com entrega grátis acima de um valor", () => {
    expect(quoteDelivery(tropical, "delivery", "", 3000).fee).toBe(500);
    expect(quoteDelivery(tropical, "delivery", "", 6000).fee).toBe(0);
  });
  it("entrega grátis e retirada sem taxa", () => {
    expect(quoteDelivery(premium, "delivery", "", 1000).fee).toBe(0);
    expect(quoteDelivery(maria, "pickup", "", 1000)).toMatchObject({ fee: 0, allowed: true });
  });
});

describe("mensagem do WhatsApp", () => {
  const ev = evaluateCart(maria, cart);
  const quote = quoteDelivery(maria, "delivery", "Centro", ev.subtotal);
  const totals = computeTotals(ev.subtotal, quote);
  const msg = buildOrderMessage({ menu: maria, lines: ev.lines, customer: customer(), totals, orderCode: "ABC123" });

  it("contém todos os dados do pedido", () => {
    expect(totals.total).toBe(3700);
    for (const s of [
      "NOVO PEDIDO - AÇAÍ DA MARIA", "CLIENTE:* João Silva", "1x Monte seu açaí 500 ml", "Escolha a base: Açaí tradicional",
      "- Banana", "- Leite em pó", "- Granola", "Nutella extra: +R$ 3,00", "Valor: R$ 21,00", "1x Monte seu açaí 300 ml",
      "Escolha a base: Açaí com morango", "Valor: R$ 12,00", "Subtotal: R$ 33,00", "Entrega: R$ 4,00", "TOTAL: R$ 37,00",
      "Rua das Flores, 123", "Bairro: Centro", "PAGAMENTO:* Pix", "Entregar na portaria.", "PEDIDO ENVIADO PELO CARDÁPIO DIGITAL.",
    ]) expect(msg).toContain(s);
    expect(msg).toContain("PEDIDO DE DEMONSTRAÇÃO");
  });

  it("retirada não pede endereço nem cobra entrega", () => {
    const q = quoteDelivery(maria, "pickup", "", ev.subtotal);
    const m = buildOrderMessage({ menu: maria, lines: ev.lines, customer: customer({ type: "pickup" }), totals: computeTotals(ev.subtotal, q), orderCode: "X" });
    expect(m).toContain("RETIRADA NO ESTABELECIMENTO");
    expect(m).not.toContain("ENDEREÇO");
    expect(m).not.toContain("Entrega:");
    expect(m).toContain("TOTAL: R$ 33,00");
  });

  it("dinheiro com troco", () => {
    const m = buildOrderMessage({ menu: maria, lines: ev.lines, customer: customer({ payment: "cash", needsChange: true, changeFor: 5000 }), totals, orderCode: "X" });
    expect(m).toContain("Troco para: R$ 50,00 (troco de R$ 13,00)");
  });

  it("gera link wa.me com URL encoding correto", () => {
    const url = whatsappUrl("55 (11) 98765-4321", msg);
    expect(url.startsWith("https://wa.me/5511987654321?text=")).toBe(true);
    const decoded = decodeURIComponent(url.split("?text=")[1]);
    expect(decoded).toBe(msg);
    expect(url).not.toMatch(/\s/);
  });

  it("cabeçalho e rodapé personalizados por loja", () => {
    const tev = evaluateCart(tropical, [item({ variantKey: "300ml" })]);
    const m = buildOrderMessage({ menu: tropical, lines: tev.lines, customer: customer({ type: "pickup" }), totals: computeTotals(tev.subtotal, { fee: 0, allowed: true, message: null, zone: null }), orderCode: "X" });
    expect(m.startsWith("🌴 *NOVO PEDIDO - AÇAÍ TROPICAL*")).toBe(true);
    expect(m).toContain("Aguarde a confirmação da loja");
  });
});

describe("validação dos dados do cliente", () => {
  const quote = quoteDelivery(maria, "delivery", "Centro", 3300);
  it("aceita dados completos", () => {
    expect(validateCustomer(maria, customer(), quote, 3700, false)).toEqual({});
  });
  it("exige nome, telefone e endereço na entrega", () => {
    const e = validateCustomer(maria, customer({ name: "", phone: "123", address: { cep: "", street: "", number: "", neighborhood: "", complement: "", reference: "" } }), quoteDelivery(maria, "delivery", "", 0), 3700, false);
    expect(Object.keys(e).sort()).toEqual(["name", "neighborhood", "number", "phone", "street"]);
  });
  it("troco precisa ser maior que o total", () => {
    expect(validateCustomer(maria, customer({ payment: "cash", needsChange: true, changeFor: 2000 }), quote, 3700, false).changeFor).toBeTruthy();
  });
  it("forma de pagamento não aceita pela loja é recusada", () => {
    expect(validateCustomer(premium, customer({ payment: "cash" }), { fee: 0, allowed: true, message: null, zone: null }, 3700, false).payment).toBeTruthy();
  });
  it("exige horário quando a loja está fechada e aceita agendamento", () => {
    expect(validateCustomer(maria, customer(), quote, 3700, true).scheduledFor).toBeTruthy();
  });
});

describe("formatação", () => {
  it("moeda e telefone", () => {
    expect(formatBRL(123456)).toBe("R$ 1.234,56");
    expect(parseBRL("50")).toBe(5000);
    expect(parseBRL("R$ 1.234,50")).toBe(123450);
    expect(parseBRL("12.5")).toBe(1250);
    expect(maskPhone("11987654321")).toBe("(11) 98765-4321");
  });
});
