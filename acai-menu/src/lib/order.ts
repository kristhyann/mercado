/**
 * Carrinho → totais → mensagem do WhatsApp.
 * Tudo aqui é puro (sem React) para ser testado automaticamente.
 */
import { findProduct, type Product, type StoreMenu, type Variant } from "./menu";
import { formatBRL, normalizeText, onlyDigits } from "./format";
import { priceItem, validateItem, type PriceBreakdown, type Selections } from "./pricing";
import type { PaymentMethod } from "./schema";

export interface CartItem {
  id: string;
  productKey: string;
  variantKey: string;
  selections: Selections;
  quantity: number;
  notes: string;
  addedAt: number;
}

export interface PricedLine {
  item: CartItem;
  product: Product;
  variant: Variant;
  price: PriceBreakdown;
  total: number;
}

export interface CartEvaluation {
  lines: PricedLine[];
  /** Itens que não existem mais ou ficaram inválidos (produto removido, esgotado…). */
  invalid: { item: CartItem; reason: string }[];
  subtotal: number;
  count: number;
}

export function evaluateCart(menu: StoreMenu, items: CartItem[]): CartEvaluation {
  const lines: PricedLine[] = [];
  const invalid: CartEvaluation["invalid"] = [];
  for (const item of items) {
    const product = findProduct(menu, item.productKey);
    if (!product) {
      invalid.push({ item, reason: "Produto não está mais no cardápio." });
      continue;
    }
    const issues = validateItem(product, item.variantKey, item.selections);
    const variant = product.variants.find((v) => v.key === item.variantKey);
    if (issues.length || !variant) {
      invalid.push({ item, reason: issues[0]?.message ?? "Tamanho indisponível." });
      continue;
    }
    const price = priceItem(product, item.variantKey, item.selections);
    lines.push({ item, product, variant, price, total: price.unitPrice * item.quantity });
  }
  return {
    lines,
    invalid,
    subtotal: lines.reduce((s, l) => s + l.total, 0),
    count: lines.reduce((s, l) => s + l.item.quantity, 0),
  };
}

export type OrderType = "delivery" | "pickup";

export interface DeliveryQuote {
  /** Valor em centavos, ou null quando a taxa será combinada com a loja. */
  fee: number | null;
  allowed: boolean;
  message: string | null;
  zone: string | null;
}

export const UNLISTED_NEIGHBORHOOD = "__outro__";

export function quoteDelivery(menu: StoreMenu, type: OrderType, neighborhood: string, subtotal: number): DeliveryQuote {
  if (type === "pickup") return { fee: 0, allowed: true, message: null, zone: null };
  if (!menu.ordering.delivery) return { fee: null, allowed: false, message: "Esta loja não faz entregas.", zone: null };
  const d = menu.delivery;
  const freeByValue = d.freeAbove !== null && subtotal >= d.freeAbove;

  if (d.mode === "free") return { fee: 0, allowed: true, message: null, zone: null };
  if (d.mode === "fixed") return { fee: freeByValue ? 0 : d.fixedFee, allowed: true, message: null, zone: null };

  if (!neighborhood) return { fee: null, allowed: false, message: "Selecione o bairro para calcular a entrega.", zone: null };
  if (neighborhood === UNLISTED_NEIGHBORHOOD) {
    return d.allowUnlistedNeighborhoods
      ? { fee: null, allowed: true, message: "Taxa de entrega a combinar com a loja pelo WhatsApp.", zone: null }
      : { fee: null, allowed: false, message: "Ainda não entregamos neste bairro. Você pode escolher retirada.", zone: null };
  }
  const zone = d.zones.find((z) => normalizeText(z.neighborhood) === normalizeText(neighborhood));
  if (!zone) return { fee: null, allowed: false, message: "Ainda não entregamos neste bairro.", zone: null };
  return { fee: freeByValue ? 0 : zone.fee, allowed: true, message: null, zone: zone.neighborhood };
}

export const PAYMENT_LABELS: Record<PaymentMethod, string> = {
  pix: "Pix",
  cash: "Dinheiro",
  credit: "Cartão de crédito",
  debit: "Cartão de débito",
};

export interface CustomerInfo {
  name: string;
  phone: string;
  type: OrderType;
  address: {
    cep: string;
    street: string;
    number: string;
    neighborhood: string;
    complement: string;
    reference: string;
  };
  payment: PaymentMethod;
  needsChange: boolean;
  changeFor: number | null; // centavos
  notes: string;
  scheduledFor: string | null; // "AAAA-MM-DD HH:MM"
}

export interface OrderTotals {
  subtotal: number;
  deliveryFee: number | null;
  total: number;
}

export function computeTotals(subtotal: number, quote: DeliveryQuote): OrderTotals {
  return { subtotal, deliveryFee: quote.fee, total: subtotal + (quote.fee ?? 0) };
}

const SEP = "━━━━━━━━━━━━━━";

function formatSchedule(value: string): string {
  const [date, time] = value.split(" ");
  const [y, m, d] = date.split("-");
  const wd = ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado"][new Date(`${date}T12:00:00Z`).getUTCDay()];
  return `${wd}, ${d}/${m}/${y} às ${time}`;
}

export function describeLine(line: PricedLine): string[] {
  const out: string[] = [];
  const { product, variant, price, item } = line;
  const title = product.hasVariantChoice || (variant.name && product.variants.length === 1 && variant.key !== "padrao")
    ? `${product.name} ${variant.name}`.trim()
    : product.name;
  out.push(`*${item.quantity}x ${title}*`);
  for (const g of price.groups) {
    if (!g.lines.length) continue;
    const paidOnly = g.lines.every((l) => l.charged > 0);
    if (g.lines.length === 1 && !paidOnly && g.lines[0].quantity === 1) {
      out.push(`${g.name}: ${g.lines[0].name}`);
      continue;
    }
    out.push(`${g.name}:`);
    for (const l of g.lines) {
      const qty = l.quantity > 1 ? `${l.quantity}x ` : "";
      out.push(`- ${qty}${l.name}${l.charged > 0 ? `: +${formatBRL(l.charged)}` : ""}`);
    }
  }
  if (item.notes.trim()) out.push(`Obs.: ${item.notes.trim()}`);
  out.push(item.quantity > 1 ? `Valor: ${item.quantity} x ${formatBRL(price.unitPrice)} = ${formatBRL(line.total)}` : `Valor: ${formatBRL(line.total)}`);
  return out;
}

export interface OrderMessageInput {
  menu: StoreMenu;
  lines: PricedLine[];
  customer: CustomerInfo;
  totals: OrderTotals;
  orderCode: string;
}

export function buildOrderMessage({ menu, lines, customer, totals, orderCode }: OrderMessageInput): string {
  const L: string[] = [];
  L.push(menu.whatsappMessage.header?.trim() || `🍇 *NOVO PEDIDO - ${menu.name.toUpperCase()}*`);
  L.push(`Pedido nº ${orderCode}`);
  if (menu.isDemo) L.push("⚠️ PEDIDO DE DEMONSTRAÇÃO (loja fictícia)");
  L.push("");
  L.push(`👤 *CLIENTE:* ${customer.name.trim()}`);
  L.push(`📞 *TELEFONE:* ${customer.phone.trim()}`);
  L.push(`🛵 *TIPO:* ${customer.type === "delivery" ? "Entrega" : "Retirada no estabelecimento"}`);
  if (customer.scheduledFor) L.push(`⏰ *AGENDADO PARA:* ${formatSchedule(customer.scheduledFor)}`);
  L.push("");
  L.push("📦 *PEDIDO:*");
  lines.forEach((line, i) => {
    L.push("");
    L.push(...describeLine(line));
    if (i === lines.length - 1) L.push("");
  });
  L.push(SEP);
  L.push("");
  L.push(`Subtotal: ${formatBRL(totals.subtotal)}`);
  if (customer.type === "delivery") {
    L.push(`Entrega: ${totals.deliveryFee === null ? "a combinar" : totals.deliveryFee === 0 ? "Grátis" : formatBRL(totals.deliveryFee)}`);
  }
  L.push("");
  L.push(`*TOTAL: ${formatBRL(totals.total)}*${totals.deliveryFee === null && customer.type === "delivery" ? " + entrega" : ""}`);
  L.push("");

  if (customer.type === "delivery") {
    const a = customer.address;
    L.push("📍 *ENDEREÇO:*");
    L.push(`${a.street.trim()}, ${a.number.trim()}${a.complement.trim() ? ` - ${a.complement.trim()}` : ""}`);
    L.push(`Bairro: ${a.neighborhood.trim()}`);
    if (a.cep.trim()) L.push(`CEP: ${a.cep.trim()}`);
    if (a.reference.trim()) L.push(`Referência: ${a.reference.trim()}`);
  } else {
    L.push("🏪 *RETIRADA NO ESTABELECIMENTO*");
    if (menu.contact.address) L.push(menu.contact.address);
  }
  L.push("");

  L.push(`💳 *PAGAMENTO:* ${PAYMENT_LABELS[customer.payment]}`);
  if (customer.payment === "cash") {
    if (customer.needsChange && customer.changeFor) {
      L.push(`Troco para: ${formatBRL(customer.changeFor)} (troco de ${formatBRL(Math.max(0, customer.changeFor - totals.total))})`);
    } else L.push("Não precisa de troco.");
  }
  if (customer.payment === "pix" && menu.ordering.pixKey) L.push(`Chave Pix da loja: ${menu.ordering.pixKey}`);

  if (customer.notes.trim()) {
    L.push("");
    L.push(`📝 *Observações:* ${customer.notes.trim()}`);
  }
  L.push("");
  L.push(SEP);
  L.push(menu.whatsappMessage.footer?.trim() || "PEDIDO ENVIADO PELO CARDÁPIO DIGITAL.");
  return L.join("\n");
}

/** Link oficial de conversa do WhatsApp (wa.me) com a mensagem codificada. */
export function whatsappUrl(phone: string, text?: string): string {
  const digits = onlyDigits(phone);
  return text ? `https://wa.me/${digits}?text=${encodeURIComponent(text)}` : `https://wa.me/${digits}`;
}

export function generateOrderCode(now = Date.now()): string {
  const alphabet = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
  let s = "";
  const rnd = typeof crypto !== "undefined" && "getRandomValues" in crypto ? crypto.getRandomValues(new Uint8Array(3)) : [0, 0, 0].map(() => Math.floor(Math.random() * 256));
  for (const b of rnd) s += alphabet[b % alphabet.length];
  return `${s}${String(now).slice(-3)}`;
}

/** Validação dos dados do cliente antes de gerar a mensagem. */
export function validateCustomer(menu: StoreMenu, c: CustomerInfo, quote: DeliveryQuote, total: number, mustSchedule: boolean): Record<string, string> {
  const e: Record<string, string> = {};
  if (c.name.trim().length < 2) e.name = "Informe seu nome.";
  const phone = onlyDigits(c.phone);
  if (phone.length < 10 || phone.length > 11) e.phone = "Informe um telefone com DDD.";
  if (c.type === "delivery" && !menu.ordering.delivery) e.type = "Esta loja não faz entregas.";
  if (c.type === "pickup" && !menu.ordering.pickup) e.type = "Esta loja não faz retirada.";
  if (c.type === "delivery") {
    if (!c.address.street.trim()) e.street = "Informe a rua.";
    if (!c.address.number.trim()) e.number = "Informe o número (ou S/N).";
    if (!c.address.neighborhood.trim()) e.neighborhood = "Informe o bairro.";
    if (!quote.allowed) e.neighborhood = quote.message ?? "Bairro não atendido.";
  }
  if (!menu.ordering.paymentMethods.includes(c.payment)) e.payment = "Escolha a forma de pagamento.";
  if (c.payment === "cash" && c.needsChange) {
    if (!c.changeFor) e.changeFor = "Informe para quanto precisa de troco.";
    else if (c.changeFor < total) e.changeFor = "O valor do troco precisa ser maior que o total do pedido.";
  }
  if (mustSchedule && !c.scheduledFor) e.scheduledFor = "Escolha o horário do pedido.";
  return e;
}
