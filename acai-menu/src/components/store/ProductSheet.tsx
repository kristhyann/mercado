"use client";
import { useEffect, useMemo, useRef, useState } from "react";
import { Check, Minus, Plus, X } from "lucide-react";
import { useStore } from "./StoreProvider";
import { Badges } from "./MenuBody";
import { Img } from "@/components/ui/Img";
import { findProduct, type Product, type ProductGroup } from "@/lib/menu";
import { chargeFor, clampSelections, countSelected, priceItem, rulesFor, validateItem, type Selections } from "@/lib/pricing";
import { formatBRL } from "@/lib/format";
import { useBackToClose, useLockBody } from "@/lib/hooks";

export function ProductSheet() {
  const { menu, sheet, closeProduct } = useStore();
  const product = sheet ? findProduct(menu, sheet.productKey) : undefined;
  useBackToClose(Boolean(product), closeProduct);
  useLockBody(Boolean(product));
  if (!product || !sheet) return null;
  return <SheetContent key={`${sheet.productKey}:${sheet.editItemId ?? "new"}`} product={product} editItemId={sheet.editItemId} />;
}

function ruleText(min: number, max: number | null, free: number, extra: number | null) {
  const parts: string[] = [];
  if (max === 1) parts.push(min >= 1 ? "Escolha 1 opção" : "Escolha até 1 opção");
  else if (min > 0 && max !== null && min === max) parts.push(`Escolha ${min} opções`);
  else if (min > 0 && max !== null) parts.push(`Escolha de ${min} a ${max}`);
  else if (min > 0) parts.push(`Escolha pelo menos ${min}`);
  else if (max !== null) parts.push(`Escolha até ${max}`);
  else parts.push("Escolha quantas quiser");
  if (free > 0 && max !== 1) parts.push(`${free} grátis${extra ? `, depois +${formatBRL(extra)} cada` : ""}`);
  return parts.join(" · ");
}

function SheetContent({ product, editItemId }: { product: Product; editItemId?: string }) {
  const { cart, closeProduct, toast, status, menu } = useStore();
  const editing = editItemId ? cart.items.find((i) => i.id === editItemId) : undefined;

  const defaultVariant = product.hasVariantChoice ? null : product.variants[0].key;
  const [variantKey, setVariantKey] = useState<string | null>(editing?.variantKey ?? defaultVariant);
  const [selections, setSelections] = useState<Selections>(() => {
    if (editing) return editing.selections;
    // Pré-seleciona a única opção de grupos obrigatórios com uma só escolha possível.
    const init: Selections = {};
    for (const pg of product.groups) {
      const avail = pg.group.addons.filter((a) => a.available);
      if (pg.rules.min >= 1 && avail.length === 1) init[pg.group.key] = { [avail[0].key]: 1 };
    }
    return init;
  });
  const [quantity, setQuantity] = useState(editing?.quantity ?? 1);
  const [notes, setNotes] = useState(editing?.notes ?? "");
  const [showErrors, setShowErrors] = useState(false);
  const [pulse, setPulse] = useState(0);
  const scrollRef = useRef<HTMLDivElement>(null);

  const variant = variantKey ? product.variants.find((v) => v.key === variantKey) : undefined;
  const price = useMemo(() => priceItem(product, variantKey ?? product.variants[0].key, selections), [product, variantKey, selections]);
  const issues = useMemo(() => validateItem(product, variantKey, selections), [product, variantKey, selections]);
  const total = (variant ? price.unitPrice : price.addons + product.fromPrice) * quantity;

  useEffect(() => setPulse((p) => p + 1), [total]);

  function chooseVariant(key: string) {
    setVariantKey(key);
    setSelections((s) => clampSelections(product, key, s));
  }

  function setQty(pg: ProductGroup, addonKey: string, next: number) {
    const rules = rulesFor(pg, variant);
    setSelections((prev) => {
      const cur = { ...(prev[pg.group.key] ?? {}) };
      if (rules.max === 1 && pg.group.maxPerOption === 1 && next > 0) {
        // Comportamento de "radio": troca a opção.
        return { ...prev, [pg.group.key]: { [addonKey]: 1 } };
      }
      const others = countSelected(cur) - (cur[addonKey] ?? 0);
      let q = Math.max(0, Math.min(next, pg.group.maxPerOption));
      if (rules.max !== null) q = Math.min(q, rules.max - others);
      if (q <= 0) delete cur[addonKey];
      else cur[addonKey] = q;
      return { ...prev, [pg.group.key]: cur };
    });
  }

  function submit() {
    if (issues.length) {
      setShowErrors(true);
      const first = issues[0];
      const el = scrollRef.current?.querySelector(first.groupKey ? `[data-group="${first.groupKey}"]` : "[data-group='__variant']");
      el?.scrollIntoView({ behavior: "smooth", block: "center" });
      return;
    }
    const payload = { productKey: product.key, variantKey: variantKey!, selections: clampSelections(product, variantKey!, selections), quantity, notes: notes.trim() };
    if (editing) {
      cart.update(editing.id, payload);
      toast("Item atualizado");
    } else {
      cart.add(payload);
      toast(`${quantity}x ${product.name} adicionado ao pedido`);
    }
    closeProduct();
  }

  const issueFor = (key: string | null) => (showErrors ? issues.find((i) => i.groupKey === key) : undefined);

  return (
    <div className="fixed inset-0 z-50 flex items-end justify-center sm:items-center sm:p-6" role="dialog" aria-modal="true" aria-label={product.name}>
      <button className="animate-fade-in absolute inset-0 bg-black/55" onClick={closeProduct} aria-label="Fechar" tabIndex={-1} />
      <div className="animate-sheet-up relative flex max-h-[94dvh] w-full max-w-xl flex-col overflow-hidden rounded-t-[28px] bg-white shadow-float sm:max-h-[90dvh] sm:rounded-[28px]">
        <button onClick={closeProduct} className="absolute right-3 top-3 z-10 flex size-11 items-center justify-center rounded-full bg-white/95 text-ink shadow-card backdrop-blur" aria-label="Fechar">
          <X className="size-5" />
        </button>

        <div ref={scrollRef} className="flex-1 overflow-y-auto overscroll-contain">
          <div className="relative aspect-[4/3] w-full bg-brand-softer sm:aspect-[16/10]">
            {product.image && <Img src={product.image} alt={product.name} fill sizes="(max-width: 640px) 100vw, 576px" className="object-cover" priority />}
          </div>
          <div className="p-5">
            <div className="flex flex-wrap gap-1">
              <Badges product={product} max={3} />
            </div>
            <h2 className="mt-1 text-2xl font-extrabold leading-tight">{product.name}</h2>
            {product.description && <p className="mt-1.5 text-[15px] leading-relaxed text-muted">{product.description}</p>}
            {!product.hasVariantChoice && (
              <p className="mt-2 flex items-baseline gap-2">
                <span className="text-xl font-extrabold text-brand">{formatBRL(product.variants[0].price)}</span>
                {product.variants[0].compareAtPrice && <span className="text-muted line-through">{formatBRL(product.variants[0].compareAtPrice)}</span>}
              </p>
            )}
          </div>

          {product.hasVariantChoice && (
            <section data-group="__variant" className={`border-t-8 border-canvas ${issueFor(null) && !variantKey ? "bg-rose-50/60" : ""}`}>
              <GroupHeader title={product.variantLabel} subtitle="Escolha 1 opção" required done={Boolean(variantKey)} error={!variantKey ? issueFor(null)?.message : undefined} />
              <ul className="px-3 pb-3">
                {product.variants.map((v) => {
                  const sel = variantKey === v.key;
                  return (
                    <li key={v.key}>
                      <button
                        type="button"
                        disabled={!v.available}
                        onClick={() => chooseVariant(v.key)}
                        className={`flex min-h-14 w-full items-center gap-3 rounded-2xl px-3 py-2 text-left transition ${sel ? "bg-brand-softer ring-2 ring-brand" : "hover:bg-canvas"} disabled:opacity-50`}
                        aria-pressed={sel}
                      >
                        <span className={`flex size-6 shrink-0 items-center justify-center rounded-full border-2 ${sel ? "border-brand bg-brand" : "border-line"}`}>
                          {sel && <span className="size-2.5 rounded-full bg-white" />}
                        </span>
                        <span className="flex-1">
                          <span className="block text-[15px] font-bold">{v.name}</span>
                          {v.description && <span className="block text-xs text-muted">{v.description}</span>}
                          {!v.available && <span className="block text-xs font-bold text-rose-600">Esgotado</span>}
                        </span>
                        <span className="text-right">
                          <span className="block text-[15px] font-extrabold text-ink">{formatBRL(v.price)}</span>
                          {v.compareAtPrice && <span className="block text-xs text-muted line-through">{formatBRL(v.compareAtPrice)}</span>}
                        </span>
                      </button>
                    </li>
                  );
                })}
              </ul>
            </section>
          )}

          {product.groups.map((pg) => {
            const rules = rulesFor(pg, variant);
            const sel = selections[pg.group.key] ?? {};
            const count = countSelected(sel);
            const breakdown = chargeFor(pg.group, rules, sel);
            const full = rules.max !== null && count >= rules.max;
            const radio = rules.max === 1 && pg.group.maxPerOption === 1;
            const err = issueFor(pg.group.key);
            return (
              <section key={pg.group.key} data-group={pg.group.key} className={`border-t-8 border-canvas ${err ? "bg-rose-50/60" : ""}`}>
                <GroupHeader
                  title={pg.group.name}
                  subtitle={ruleText(rules.min, rules.max, rules.free, pg.group.extraPrice || null)}
                  description={pg.group.description}
                  required={rules.min > 0}
                  done={count >= rules.min && rules.min > 0}
                  counter={rules.max !== 1 ? `${count}${rules.max !== null ? `/${rules.max}` : ""}` : undefined}
                  freeLeft={rules.free > 0 && rules.max !== 1 ? Math.max(0, rules.free - pg.group.addons.reduce((s, a) => s + (a.alwaysPaid ? 0 : sel[a.key] ?? 0), 0)) : undefined}
                  error={err?.message}
                />
                <ul className="px-3 pb-3">
                  {pg.group.addons.map((a) => {
                    const q = sel[a.key] ?? 0;
                    const line = breakdown.lines.find((l) => l.key === a.key);
                    const unitPrice = a.price > 0 ? a.price : pg.group.extraPrice;
                    const disabled = !a.available || (!q && full && !radio);
                    let priceLabel: string | null = null;
                    if (line && line.charged > 0) priceLabel = `+${formatBRL(line.charged)}`;
                    else if (line && line.charged === 0 && unitPrice > 0) priceLabel = "Grátis";
                    else if (!line && unitPrice > 0 && (a.alwaysPaid || rules.free === 0)) priceLabel = `+${formatBRL(unitPrice)}`;
                    else if (!line && unitPrice > 0 && rules.free > 0 && count >= rules.free) priceLabel = `+${formatBRL(unitPrice)}`;
                    return (
                      <li key={a.key}>
                        <div className={`flex min-h-14 items-center gap-3 rounded-2xl px-3 py-1.5 transition ${q ? "bg-brand-softer" : ""} ${disabled ? "opacity-45" : ""}`}>
                          {pg.group.maxPerOption > 1 ? (
                            <>
                              <span className="flex-1">
                                <span className="block text-[15px] font-semibold">{a.name}</span>
                                {!a.available && <span className="text-xs font-bold text-rose-600">Esgotado</span>}
                                {a.description && <span className="block text-xs text-muted">{a.description}</span>}
                              </span>
                              {priceLabel && <span className={`text-sm font-bold ${priceLabel === "Grátis" ? "text-success" : "text-ink"}`}>{priceLabel}</span>}
                              <Stepper value={q} onChange={(n) => setQty(pg, a.key, n)} max={pg.group.maxPerOption} disableInc={disabled || full || q >= pg.group.maxPerOption} label={a.name} />
                            </>
                          ) : (
                            <button type="button" disabled={disabled} onClick={() => setQty(pg, a.key, q ? 0 : 1)} className="flex w-full items-center gap-3 py-1.5 text-left" aria-pressed={q > 0}>
                              <span className={`flex size-6 shrink-0 items-center justify-center border-2 transition ${radio ? "rounded-full" : "rounded-lg"} ${q ? "border-brand bg-brand text-on-brand" : "border-line bg-white"}`}>
                                {q > 0 && (radio ? <span className="size-2.5 rounded-full bg-white" /> : <Check className="size-4" strokeWidth={3} />)}
                              </span>
                              <span className="flex-1">
                                <span className="block text-[15px] font-semibold">{a.name}</span>
                                {!a.available && <span className="text-xs font-bold text-rose-600">Esgotado</span>}
                                {a.description && <span className="block text-xs text-muted">{a.description}</span>}
                              </span>
                              {priceLabel && <span className={`text-sm font-bold ${priceLabel === "Grátis" ? "text-success" : "text-ink"}`}>{priceLabel}</span>}
                            </button>
                          )}
                        </div>
                      </li>
                    );
                  })}
                </ul>
              </section>
            );
          })}

          <section className="border-t-8 border-canvas p-5">
            <label htmlFor="item-notes" className="text-[15px] font-bold">
              Alguma observação?
            </label>
            <textarea
              id="item-notes"
              value={notes}
              onChange={(e) => setNotes(e.target.value.slice(0, 200))}
              rows={2}
              placeholder="Ex.: pouco leite condensado, sem granola…"
              className="mt-2 w-full resize-none rounded-2xl border border-line bg-canvas p-3 outline-none focus:border-brand focus:ring-4 focus:ring-brand/15"
            />
            <p className="mt-1 text-right text-xs text-muted">{notes.length}/200</p>
            {!status.canOrder && (
              <p className="mt-2 rounded-xl bg-amber-50 p-3 text-sm text-amber-900">
                {status.paused
                  ? status.detail
                  : `${menu.name} está fechada agora${status.detail ? ` (${status.detail.toLowerCase()})` : ""}. ${status.mustSchedule ? "Você pode agendar o horário na finalização." : "Monte seu pedido e envie quando abrirmos."}`}
              </p>
            )}
          </section>
        </div>

        <footer className="pb-safe flex items-center gap-3 border-t border-line bg-white px-4 pt-3">
          <Stepper value={quantity} onChange={(n) => setQuantity(Math.max(1, Math.min(99, n)))} min={1} max={99} label="quantidade" large />
          <button
            type="button"
            onClick={submit}
            disabled={!product.available}
            className={`flex h-14 flex-1 items-center justify-between gap-2 rounded-2xl px-5 text-[15px] font-extrabold shadow-float transition active:scale-[0.98] ${
              issues.length ? "bg-brand/60 text-on-brand" : "bg-brand text-on-brand hover:bg-brand-strong"
            }`}
          >
            <span>{editing ? "Salvar" : "Adicionar"}</span>
            <span key={pulse} className="animate-pop">
              {formatBRL(total)}
            </span>
          </button>
        </footer>
      </div>
    </div>
  );
}

function GroupHeader(props: { title: string; subtitle: string; description?: string | null; required?: boolean; done?: boolean; counter?: string; freeLeft?: number; error?: string }) {
  return (
    <div className="sticky top-0 z-[2] flex items-start justify-between gap-3 bg-white/95 px-5 pb-2 pt-4 backdrop-blur">
      <div className="min-w-0">
        <h3 className="text-[16px] font-extrabold">{props.title}</h3>
        <p className="text-[13px] text-muted">{props.subtitle}</p>
        {props.freeLeft !== undefined && (
          <p className={`text-[13px] font-semibold ${props.freeLeft > 0 ? "text-success" : "text-amber-700"}`}>
            {props.freeLeft > 0 ? `Você ainda tem ${props.freeLeft} grátis` : "Escolhas grátis usadas"}
          </p>
        )}
        {props.error && <p className="mt-1 text-[13px] font-bold text-danger">{props.error}</p>}
      </div>
      <div className="flex shrink-0 flex-col items-end gap-1">
        {props.required && (
          <span className={`rounded-md px-2 py-0.5 text-[11px] font-extrabold uppercase ${props.done ? "bg-emerald-100 text-emerald-800" : "bg-ink text-white"}`}>
            {props.done ? "✓ OK" : "Obrigatório"}
          </span>
        )}
        {props.counter && <span className="text-xs font-bold text-muted">{props.counter}</span>}
      </div>
    </div>
  );
}

export function Stepper({ value, onChange, min = 0, max = 99, disableInc, label, large }: { value: number; onChange: (n: number) => void; min?: number; max?: number; disableInc?: boolean; label: string; large?: boolean }) {
  const size = large ? "size-11" : "size-9";
  if (!large && value === 0) {
    return (
      <button type="button" onClick={() => onChange(1)} disabled={disableInc} className={`${size} flex items-center justify-center rounded-full border-2 border-brand text-brand disabled:border-line disabled:text-muted`} aria-label={`Adicionar ${label}`}>
        <Plus className="size-4" strokeWidth={3} />
      </button>
    );
  }
  return (
    <div className={`flex items-center rounded-full ${large ? "bg-canvas p-1" : "bg-white ring-1 ring-line"}`}>
      <button type="button" onClick={() => onChange(value - 1)} disabled={value <= min} className={`${size} flex items-center justify-center rounded-full text-brand transition active:scale-90 disabled:text-muted/50`} aria-label={`Diminuir ${label}`}>
        <Minus className="size-4" strokeWidth={3} />
      </button>
      <span className={`min-w-7 text-center font-extrabold tabular-nums ${large ? "text-lg" : "text-[15px]"}`} aria-live="polite">
        {value}
      </span>
      <button type="button" onClick={() => onChange(value + 1)} disabled={disableInc || value >= max} className={`${size} flex items-center justify-center rounded-full text-brand transition active:scale-90 disabled:text-muted/50`} aria-label={`Aumentar ${label}`}>
        <Plus className="size-4" strokeWidth={3} />
      </button>
    </div>
  );
}
