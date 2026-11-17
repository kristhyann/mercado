"use client";
import { useEffect, useRef, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { AlertTriangle, ArrowUp, ChevronRight, Pencil, ShoppingBag, Trash2, X } from "lucide-react";
import { useStore } from "./StoreProvider";
import { Stepper } from "./ProductSheet";
import { Img } from "@/components/ui/Img";
import { formatBRL } from "@/lib/format";
import type { PricedLine } from "@/lib/order";
import { useBackToClose, useLockBody } from "@/lib/hooks";

export function lineTitle(l: PricedLine) {
  return l.product.hasVariantChoice ? `${l.product.name} · ${l.variant.name}` : l.product.name;
}

export function LineDetails({ line }: { line: PricedLine }) {
  const groups = line.price.groups.filter((g) => g.lines.length);
  if (!groups.length && !line.item.notes) return null;
  return (
    <div className="mt-1 space-y-0.5 text-[13px] leading-snug text-muted">
      {groups.map((g) => (
        <p key={g.key}>
          <span className="font-semibold text-ink/70">{g.name}:</span>{" "}
          {g.lines.map((l, i) => (
            <span key={l.key}>
              {i > 0 && ", "}
              {l.quantity > 1 ? `${l.quantity}x ` : ""}
              {l.name}
              {l.charged > 0 && <span className="font-semibold text-ink/70"> (+{formatBRL(l.charged)})</span>}
            </span>
          ))}
        </p>
      ))}
      {line.item.notes && <p className="italic">Obs.: {line.item.notes}</p>}
    </div>
  );
}

export function CartButton() {
  const { evaluation, hydrated, setCartOpen, cartOpen, sheet } = useStore();
  const [bump, setBump] = useState(0);
  const prev = useRef(evaluation.count);
  useEffect(() => {
    if (evaluation.count > prev.current) setBump((b) => b + 1);
    prev.current = evaluation.count;
  }, [evaluation.count]);
  if (!hydrated || evaluation.count === 0 || cartOpen || sheet) return null;
  return (
    <div className="pb-safe pointer-events-none fixed inset-x-0 bottom-0 z-40 px-4">
      <button
        onClick={() => setCartOpen(true)}
        key={bump}
        className="animate-pop pointer-events-auto mx-auto flex h-16 w-full max-w-xl items-center gap-3 rounded-2xl bg-brand px-4 text-on-brand shadow-float transition hover:bg-brand-strong active:scale-[0.98]"
        aria-label={`Meu pedido, ${evaluation.count} itens, ${formatBRL(evaluation.subtotal)}`}
      >
        <span className="relative flex size-10 items-center justify-center rounded-xl bg-white/15">
          <ShoppingBag className="size-5" />
          <span className="absolute -right-1.5 -top-1.5 flex size-6 items-center justify-center rounded-full bg-accent text-xs font-extrabold text-on-accent ring-2 ring-brand">{evaluation.count}</span>
        </span>
        <span className="flex-1 text-left text-[16px] font-extrabold">🛒 MEU PEDIDO ({evaluation.count})</span>
        <span className="text-[16px] font-extrabold">{formatBRL(evaluation.subtotal)}</span>
        <ChevronRight className="size-5" />
      </button>
    </div>
  );
}

export function BackToTop() {
  const [show, setShow] = useState(false);
  const { evaluation, hydrated } = useStore();
  useEffect(() => {
    const on = () => setShow(window.scrollY > 900);
    on();
    window.addEventListener("scroll", on, { passive: true });
    return () => window.removeEventListener("scroll", on);
  }, []);
  if (!show) return null;
  return (
    <button
      onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
      className={`animate-fade-in fixed right-4 z-30 flex size-12 items-center justify-center rounded-full bg-white text-brand shadow-float ring-1 ring-line transition active:scale-90 ${hydrated && evaluation.count > 0 ? "bottom-24" : "bottom-6"}`}
      aria-label="Voltar ao topo"
    >
      <ArrowUp className="size-5" strokeWidth={2.5} />
    </button>
  );
}

export function CartSheet() {
  const { menu, cart, evaluation, cartOpen, setCartOpen, openProduct, sheet, status } = useStore();
  const router = useRouter();
  const close = () => setCartOpen(false);
  useBackToClose(cartOpen, close);
  useLockBody(cartOpen);
  const [confirmClear, setConfirmClear] = useState(false);

  useEffect(() => {
    if (cartOpen) router.prefetch(`/${menu.slug}/checkout`);
  }, [cartOpen, menu.slug, router]);

  if (!cartOpen) return null;
  const { lines, invalid, subtotal } = evaluation;
  const belowMin = menu.ordering.minOrder > 0 && subtotal < menu.ordering.minOrder;
  const empty = lines.length === 0;

  return (
    <div className={`fixed inset-0 z-50 flex items-end justify-center sm:items-stretch sm:justify-end ${sheet ? "invisible" : ""}`} role="dialog" aria-modal="true" aria-label="Meu pedido">
      <button className="animate-fade-in absolute inset-0 bg-black/55" onClick={close} aria-label="Fechar" tabIndex={-1} />
      <div className="animate-sheet-up relative flex max-h-[94dvh] w-full max-w-xl flex-col overflow-hidden rounded-t-[28px] bg-canvas sm:max-h-none sm:max-w-md sm:rounded-none sm:rounded-l-[28px]">
        <header className="flex items-center justify-between border-b border-line bg-white px-5 py-4">
          <div>
            <h2 className="text-xl font-extrabold">Meu pedido</h2>
            <p className="text-sm text-muted">{menu.name}</p>
          </div>
          <button onClick={close} className="flex size-11 items-center justify-center rounded-full bg-canvas" aria-label="Fechar">
            <X className="size-5" />
          </button>
        </header>

        <div className="flex-1 overflow-y-auto overscroll-contain px-4 py-4">
          {invalid.length > 0 && (
            <div className="mb-3 rounded-2xl bg-amber-50 p-3 text-sm text-amber-900">
              <p className="flex items-center gap-2 font-bold">
                <AlertTriangle className="size-4" /> {invalid.length === 1 ? "1 item precisa de atenção" : `${invalid.length} itens precisam de atenção`}
              </p>
              <p className="mt-0.5">O cardápio foi atualizado. Esses itens não serão enviados:</p>
              <ul className="mt-2 space-y-1">
                {invalid.map(({ item, reason }) => (
                  <li key={item.id} className="flex items-center justify-between gap-2">
                    <span>• {reason}</span>
                    <button onClick={() => cart.remove(item.id)} className="shrink-0 font-bold underline">
                      Remover
                    </button>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {empty ? (
            <div className="py-16 text-center">
              <p className="text-5xl">🍇</p>
              <p className="mt-3 text-lg font-bold">Seu pedido está vazio</p>
              <p className="text-muted">Que tal montar um açaí agora?</p>
              <button onClick={close} className="mt-5 h-12 rounded-2xl bg-brand px-6 font-bold text-on-brand">
                Ver cardápio
              </button>
            </div>
          ) : (
            <ul className="space-y-3">
              {lines.map((l) => (
                <li key={l.item.id} className="rounded-3xl bg-white p-3 shadow-card">
                  <div className="flex gap-3">
                    <div className="relative size-16 shrink-0 overflow-hidden rounded-2xl bg-brand-softer">
                      {l.product.image && <Img src={l.product.image} alt="" fill sizes="64px" className="object-cover" />}
                    </div>
                    <div className="min-w-0 flex-1">
                      <div className="flex items-start justify-between gap-2">
                        <h3 className="text-[15px] font-bold leading-snug">{lineTitle(l)}</h3>
                        <span className="shrink-0 text-[15px] font-extrabold">{formatBRL(l.total)}</span>
                      </div>
                      <LineDetails line={l} />
                      {l.item.quantity > 1 && <p className="mt-0.5 text-xs text-muted">{formatBRL(l.price.unitPrice)} cada</p>}
                    </div>
                  </div>
                  <div className="mt-2 flex items-center justify-between gap-2 border-t border-line pt-2">
                    <div className="flex gap-1">
                      {!l.product.isSimple && (
                        <button onClick={() => openProduct(l.product.key, l.item.id)} className="flex h-10 items-center gap-1.5 rounded-xl px-3 text-sm font-bold text-brand hover:bg-brand-softer">
                          <Pencil className="size-4" /> Editar
                        </button>
                      )}
                      <button onClick={() => cart.remove(l.item.id)} className="flex h-10 items-center gap-1.5 rounded-xl px-3 text-sm font-bold text-danger hover:bg-rose-50">
                        <Trash2 className="size-4" /> Remover
                      </button>
                    </div>
                    <Stepper value={l.item.quantity} onChange={(n) => cart.setQuantity(l.item.id, n)} min={0} max={99} label={l.product.name} />
                  </div>
                </li>
              ))}
            </ul>
          )}

          {!empty && (
            <div className="mt-4 flex items-center justify-between px-1">
              <button onClick={close} className="h-11 font-bold text-brand">
                + Adicionar mais itens
              </button>
              {confirmClear ? (
                <span className="flex items-center gap-2 text-sm">
                  Limpar tudo?
                  <button onClick={() => { cart.clear(); setConfirmClear(false); }} className="h-9 rounded-lg bg-danger px-3 font-bold text-white">
                    Sim
                  </button>
                  <button onClick={() => setConfirmClear(false)} className="h-9 rounded-lg bg-white px-3 font-bold ring-1 ring-line">
                    Não
                  </button>
                </span>
              ) : (
                <button onClick={() => setConfirmClear(true)} className="h-11 text-sm font-semibold text-muted underline">
                  Limpar pedido
                </button>
              )}
            </div>
          )}
        </div>

        {!empty && (
          <footer className="pb-safe border-t border-line bg-white px-5 pt-4">
            <dl className="space-y-1 text-[15px]">
              <div className="flex justify-between">
                <dt className="text-muted">Subtotal</dt>
                <dd className="font-bold">{formatBRL(subtotal)}</dd>
              </div>
              <div className="flex justify-between">
                <dt className="text-muted">Entrega</dt>
                <dd className="font-semibold">
                  {menu.delivery.mode === "free" || !menu.ordering.delivery
                    ? menu.ordering.delivery ? "Grátis" : "Somente retirada"
                    : menu.delivery.mode === "fixed"
                      ? menu.delivery.freeAbove !== null && subtotal >= menu.delivery.freeAbove ? "Grátis" : formatBRL(menu.delivery.fixedFee)
                      : "calculada pelo bairro"}
                </dd>
              </div>
            </dl>
            {belowMin && (
              <p className="mt-2 rounded-xl bg-amber-50 p-2.5 text-sm font-semibold text-amber-900">
                Pedido mínimo de {formatBRL(menu.ordering.minOrder)}. Faltam {formatBRL(menu.ordering.minOrder - subtotal)}.
              </p>
            )}
            {!status.canOrder && (
              <p className="mt-2 rounded-xl bg-rose-50 p-2.5 text-sm font-semibold text-rose-800">
                {status.paused ? status.detail : `Estamos fechados no momento.${status.detail ? ` ${status.detail}.` : ""}`}
              </p>
            )}
            <Link
              href={`/${menu.slug}/checkout`}
              aria-disabled={belowMin || !status.canOrder}
              onClick={(e) => {
                if (belowMin || !status.canOrder) e.preventDefault();
              }}
              className={`mt-3 flex h-14 w-full items-center justify-between rounded-2xl px-5 text-[16px] font-extrabold shadow-float transition active:scale-[0.98] ${
                belowMin || !status.canOrder ? "pointer-events-none bg-line text-muted shadow-none" : "bg-brand text-on-brand hover:bg-brand-strong"
              }`}
            >
              <span>FINALIZAR PEDIDO</span>
              <span className="flex items-center gap-1">
                {formatBRL(subtotal)} <ChevronRight className="size-5" />
              </span>
            </Link>
          </footer>
        )}
      </div>
    </div>
  );
}
