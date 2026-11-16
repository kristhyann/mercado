"use client";
/**
 * Carrinho por loja, salvo no localStorage (sobrevive a atualização da página).
 * Chave: acai-menu:cart:<slug> — o carrinho de uma loja nunca aparece em outra.
 */
import { create, type StoreApi, type UseBoundStore } from "zustand";
import { createJSONStorage, persist } from "zustand/middleware";
import type { CartItem } from "./order";
import type { Selections } from "./pricing";

export interface CartState {
  items: CartItem[];
  add: (item: Omit<CartItem, "id" | "addedAt">) => CartItem;
  update: (id: string, patch: Partial<Omit<CartItem, "id">>) => void;
  setQuantity: (id: string, quantity: number) => void;
  remove: (id: string) => void;
  clear: () => void;
}

const sameSelections = (a: Selections, b: Selections) => JSON.stringify(sortDeep(a)) === JSON.stringify(sortDeep(b));
function sortDeep(s: Selections) {
  return Object.keys(s).sort().map((g) => [g, Object.keys(s[g]).sort().filter((k) => s[g][k] > 0).map((k) => [k, s[g][k]])]).filter(([, v]) => (v as unknown[]).length);
}
const uid = () => (typeof crypto !== "undefined" && "randomUUID" in crypto ? crypto.randomUUID() : `${Date.now()}-${Math.random().toString(36).slice(2)}`);

const safeStorage = createJSONStorage(() => {
  try {
    const k = "__acai_test__";
    localStorage.setItem(k, "1");
    localStorage.removeItem(k);
    return localStorage;
  } catch {
    const mem = new Map<string, string>();
    return { getItem: (k) => mem.get(k) ?? null, setItem: (k, v) => void mem.set(k, v), removeItem: (k) => void mem.delete(k) };
  }
});

type CartStore = UseBoundStore<StoreApi<CartState>> & { persist: { rehydrate: () => Promise<void> | void } };
const stores = new Map<string, CartStore>();

export function getCartStore(slug: string): CartStore {
  let s: unknown = stores.get(slug);
  if (!s) {
    s = create<CartState>()(
      persist(
        (set, get) => ({
          items: [],
          add: (input) => {
            // Mesmo produto com a mesma personalização → soma quantidade.
            const existing = get().items.find(
              (i) => i.productKey === input.productKey && i.variantKey === input.variantKey && i.notes.trim() === input.notes.trim() && sameSelections(i.selections, input.selections),
            );
            if (existing) {
              const merged = { ...existing, quantity: Math.min(99, existing.quantity + input.quantity) };
              set({ items: get().items.map((i) => (i.id === existing.id ? merged : i)) });
              return merged;
            }
            const item: CartItem = { ...input, id: uid(), addedAt: Date.now() };
            set({ items: [...get().items, item] });
            return item;
          },
          update: (id, patch) => set({ items: get().items.map((i) => (i.id === id ? { ...i, ...patch } : i)) }),
          setQuantity: (id, quantity) =>
            set({ items: quantity <= 0 ? get().items.filter((i) => i.id !== id) : get().items.map((i) => (i.id === id ? { ...i, quantity: Math.min(99, quantity) } : i)) }),
          remove: (id) => set({ items: get().items.filter((i) => i.id !== id) }),
          clear: () => set({ items: [] }),
        }),
        { name: `acai-menu:cart:${slug}`, version: 1, storage: safeStorage, skipHydration: true, partialize: (s) => ({ items: s.items }) },
      ),
    );
    stores.set(slug, s as unknown as CartStore);
  }
  return s as CartStore;
}
