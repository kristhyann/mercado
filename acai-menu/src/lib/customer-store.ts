"use client";
/** Lembra os dados do cliente (nome, telefone, endereço) para o próximo pedido, só neste aparelho. */
import type { CustomerInfo } from "./order";

const KEY = "acai-menu:customer";
type Saved = Pick<CustomerInfo, "name" | "phone" | "type" | "address" | "payment">;

export function loadCustomer(): Partial<Saved> {
  try {
    return JSON.parse(localStorage.getItem(KEY) || "{}");
  } catch {
    return {};
  }
}
export function saveCustomer(c: CustomerInfo) {
  try {
    const data: Saved = { name: c.name, phone: c.phone, type: c.type, address: c.address, payment: c.payment };
    localStorage.setItem(KEY, JSON.stringify(data));
  } catch {
    /* navegação privada: ignora */
  }
}
