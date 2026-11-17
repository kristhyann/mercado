"use client";
import { createContext, useCallback, useContext, useEffect, useMemo, useRef, useState } from "react";
import { CheckCircle2 } from "lucide-react";
import type { StoreMenu } from "@/lib/menu";
import { getCartStore, type CartState } from "@/lib/cart-store";
import { evaluateCart, type CartEvaluation } from "@/lib/order";
import { getStoreStatus, type StoreStatus } from "@/lib/hours";
import { useNow } from "@/lib/hooks";

interface SheetState {
  productKey: string;
  editItemId?: string;
}

interface StoreCtx {
  menu: StoreMenu;
  hydrated: boolean;
  cart: CartState;
  evaluation: CartEvaluation;
  status: StoreStatus;
  now: Date;
  sheet: SheetState | null;
  openProduct: (productKey: string, editItemId?: string) => void;
  closeProduct: () => void;
  cartOpen: boolean;
  setCartOpen: (open: boolean) => void;
  toast: (message: string) => void;
}

const Ctx = createContext<StoreCtx | null>(null);

export function useStore() {
  const c = useContext(Ctx);
  if (!c) throw new Error("useStore fora do StoreProvider");
  return c;
}

export function StoreProvider({ menu, serverNow, children }: { menu: StoreMenu; serverNow: number; children: React.ReactNode }) {
  const useCart = getCartStore(menu.slug);
  const cart = useCart();
  const [hydrated, setHydrated] = useState(false);
  const [sheet, setSheet] = useState<SheetState | null>(null);
  const [cartOpen, setCartOpen] = useState(false);
  const [toastMsg, setToastMsg] = useState<{ id: number; text: string } | null>(null);
  const toastTimer = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    const p = useCart.persist.rehydrate();
    Promise.resolve(p).finally(() => setHydrated(true));
  }, [useCart]);

  // Sincroniza o carrinho entre abas abertas da mesma loja.
  useEffect(() => {
    const onStorage = (e: StorageEvent) => {
      if (e.key === `acai-menu:cart:${menu.slug}`) useCart.persist.rehydrate();
    };
    window.addEventListener("storage", onStorage);
    return () => window.removeEventListener("storage", onStorage);
  }, [menu.slug, useCart]);

  const now = useNow(serverNow);
  const minute = Math.floor(now.getTime() / 60000);
  // eslint-disable-next-line react-hooks/exhaustive-deps
  const status = useMemo(() => getStoreStatus(menu.hours, now), [menu.hours, minute]);
  const evaluation = useMemo(() => evaluateCart(menu, hydrated ? cart.items : []), [menu, cart.items, hydrated]);

  const toast = useCallback((text: string) => {
    if (toastTimer.current) clearTimeout(toastTimer.current);
    setToastMsg({ id: Date.now(), text });
    toastTimer.current = setTimeout(() => setToastMsg(null), 2600);
  }, []);

  const value: StoreCtx = {
    menu, hydrated, cart, evaluation, status, now, sheet,
    openProduct: (productKey, editItemId) => setSheet({ productKey, editItemId }),
    closeProduct: () => setSheet(null),
    cartOpen, setCartOpen, toast,
  };

  return (
    <Ctx.Provider value={value}>
      {children}
      {toastMsg && (
        <div
          key={toastMsg.id}
          role="status"
          aria-live="polite"
          className="animate-toast fixed bottom-24 left-1/2 z-[70] flex max-w-[calc(100%-2rem)] -translate-x-1/2 items-center gap-2 rounded-full bg-ink px-5 py-3 text-sm font-semibold text-white shadow-float"
        >
          <CheckCircle2 className="size-5 shrink-0 text-emerald-400" />
          <span className="truncate">{toastMsg.text}</span>
        </div>
      )}
    </Ctx.Provider>
  );
}
