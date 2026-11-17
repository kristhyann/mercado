"use client";
import { useState } from "react";
import { ChevronDown, Plus, Trash2 } from "lucide-react";
import { useEditor } from "./context";
import { ImageField } from "../ImageField";
import { Button, Field, IconButton, Modal, MoneyInput, MoveButtons, NumberInput, Select, TextArea, TextInput, Toggle, cx } from "../ui";
import { groupKeyOf, move, uniqueKey, type Product, type Variant } from "@/lib/admin/editor";
import { BADGES, type RuleOverride } from "@/lib/schema";

const BADGE_LABEL: Record<(typeof BADGES)[number], string> = {
  "mais-vendido": "🔥 Mais vendido", promocao: "Promoção", novo: "Novo", vegano: "Vegano", "zero-acucar": "Zero açúcar", destaque: "⭐ Destaque",
};
const SIZE_PRESETS = ["300 ml", "400 ml", "500 ml", "700 ml", "1 litro"];

type Link = NonNullable<Product["addonGroups"]>[number];
function linkOverrides(l: Link): RuleOverride {
  if (typeof l === "string") return {};
  const { group: _g, ...o } = l;
  return o;
}
function makeLink(group: string, o: RuleOverride): Link {
  const clean: RuleOverride = {};
  if (o.min !== undefined) clean.min = o.min;
  if (o.max !== undefined) clean.max = o.max;
  if (o.free !== undefined) clean.free = o.free;
  return Object.keys(clean).length ? { group, ...clean } : group;
}

export function ProductForm({ productKey, onClose, onRename }: { productKey: string; onClose: () => void; onRename: (k: string) => void }) {
  const { cfg, update, slug } = useEditor();
  const index = cfg.products.findIndex((p) => p.key === productKey);
  const p = cfg.products[index];
  const [rulesOpen, setRulesOpen] = useState<string | null>(null);
  if (!p) return null;

  const set = (fn: (d: Product) => void) => update((d) => fn(d.products[index]));
  const links = p.addonGroups ?? [];
  const linked = links.map(groupKeyOf);
  const hasVariants = Boolean(p.variants?.length);

  function rename(name: string) {
    const auto = /^novo-produto(-\d+)?$/.test(p.key);
    let newKey = p.key;
    if (auto && name.trim()) newKey = uniqueKey(name, cfg.products.filter((x) => x.key !== p.key).map((x) => x.key));
    set((d) => { d.name = name; d.key = newKey; });
    if (newKey !== p.key) onRename(newKey);
  }

  function addVariant(name: string) {
    set((d) => {
      const list = d.variants ?? [];
      list.push({ key: uniqueKey(name, list.map((v) => v.key)), name, description: null, price: list.at(-1)?.price ?? d.price ?? 10, compareAtPrice: null, available: true, rules: {} });
      d.variants = list;
    });
  }

  function setMode(variants: boolean) {
    set((d) => {
      if (variants && !d.variants?.length) {
        d.variants = [{ key: "unico", name: "Único", description: null, price: d.price ?? 10, compareAtPrice: d.compareAtPrice ?? null, available: true, rules: {} }];
        d.price = null;
        d.compareAtPrice = null;
      } else if (!variants && d.variants?.length) {
        d.price = d.variants[0].price;
        d.compareAtPrice = d.variants[0].compareAtPrice;
        d.variants = [];
      }
    });
  }

  const setVariant = (i: number, fn: (v: Variant) => void) => set((d) => fn(d.variants![i]));

  return (
    <Modal open onClose={onClose} title={p.name || "Produto"} wide footer={<div className="flex justify-end"><Button variant="primary" onClick={onClose}>Concluir</Button></div>}>
      <div className="space-y-5">
        <p className="rounded-xl bg-violet-50 p-3 text-xs text-violet-800">As alterações ficam pendentes até você clicar em <b>Salvar</b> na barra inferior do editor.</p>

        <section className="grid gap-4 sm:grid-cols-2">
          <div className="space-y-4">
            <Field label="Nome do produto">
              <TextInput value={p.name} onChange={rename} maxLength={120} />
            </Field>
            <Field label="Categoria">
              <Select value={p.category ?? ""} onChange={(v) => set((d) => { d.category = v; })}>
                {cfg.categories.map((c) => <option key={c.key} value={c.key}>{c.name}</option>)}
              </Select>
            </Field>
            <Field label="Descrição">
              <TextArea value={p.description} onChange={(v) => set((d) => { d.description = v || null; })} maxLength={400} />
            </Field>
          </div>
          <ImageField slug={slug} kind="product" label="Foto do produto" value={p.image} onChange={(u) => set((d) => { d.image = u; })} />
        </section>

        <section className="grid gap-3 rounded-xl bg-white p-4 ring-1 ring-slate-200 sm:grid-cols-3">
          <Toggle checked={p.active !== false} onChange={(v) => set((d) => { d.active = v; })} label="Ativo" description="Desligado: oculto do cardápio" />
          <Toggle checked={p.available !== false} onChange={(v) => set((d) => { d.available = v; })} label="Disponível" description="Desligado: aparece como “Indisponível”" />
          <Toggle checked={Boolean(p.featured)} onChange={(v) => set((d) => { d.featured = v; })} label="Destaque" description="Aparece no carrossel do topo" />
        </section>

        <section className="rounded-xl bg-white p-4 ring-1 ring-slate-200">
          <div className="mb-3 flex flex-wrap items-center justify-between gap-2">
            <h3 className="font-extrabold">Preço</h3>
            <div className="flex rounded-xl bg-slate-100 p-1">
              <button type="button" onClick={() => setMode(false)} className={cx("h-9 rounded-lg px-3 text-sm font-semibold", !hasVariants ? "bg-white shadow-sm" : "text-slate-500")}>Preço único</button>
              <button type="button" onClick={() => setMode(true)} className={cx("h-9 rounded-lg px-3 text-sm font-semibold", hasVariants ? "bg-white shadow-sm" : "text-slate-500")}>Vários tamanhos</button>
            </div>
          </div>

          {!hasVariants ? (
            <div className="grid grid-cols-2 gap-3">
              <Field label="Preço">
                <MoneyInput value={p.price} onChange={(v) => set((d) => { d.price = v ?? 0; })} />
              </Field>
              <Field label="Preço “de” (promoção)" hint="Opcional, aparece riscado">
                <MoneyInput allowEmpty placeholder="—" value={p.compareAtPrice} onChange={(v) => set((d) => { d.compareAtPrice = v; })} />
              </Field>
            </div>
          ) : (
            <div className="space-y-3">
              <Field label="Título da escolha" hint="Ex.: Escolha o tamanho">
                <TextInput value={p.variantLabel} onChange={(v) => set((d) => { d.variantLabel = v || null; })} placeholder="Escolha o tamanho" />
              </Field>
              <ul className="space-y-2">
                {p.variants!.map((v, i) => (
                  <li key={i} className="rounded-xl bg-slate-50 p-2">
                    <div className="flex flex-wrap items-center gap-2">
                      <MoveButtons first={i === 0} last={i === p.variants!.length - 1} onUp={() => set((d) => { d.variants = move(d.variants!, i, -1); })} onDown={() => set((d) => { d.variants = move(d.variants!, i, 1); })} />
                      <TextInput value={v.name} onChange={(x) => setVariant(i, (vv) => { vv.name = x; })} className="min-w-28 flex-1" aria-label="Nome do tamanho" />
                      <MoneyInput value={v.price} onChange={(x) => setVariant(i, (vv) => { vv.price = x ?? 0; })} className="w-28" />
                      <MoneyInput allowEmpty placeholder="de —" value={v.compareAtPrice} onChange={(x) => setVariant(i, (vv) => { vv.compareAtPrice = x; })} className="w-28" />
                      <Toggle checked={v.available} onChange={(x) => setVariant(i, (vv) => { vv.available = x; })} />
                      <IconButton label="Remover tamanho" disabled={p.variants!.length === 1} onClick={() => set((d) => { d.variants!.splice(i, 1); })}>
                        <Trash2 className="size-4" />
                      </IconButton>
                    </div>
                    {linked.length > 0 && (
                      <>
                        <button type="button" onClick={() => setRulesOpen(rulesOpen === v.key ? null : v.key)} className="mt-1 flex items-center gap-1 px-1 text-xs font-semibold text-violet-700">
                          <ChevronDown className={cx("size-3 transition", rulesOpen === v.key && "rotate-180")} /> Regras deste tamanho {Object.keys(v.rules).length ? `(${Object.keys(v.rules).length})` : ""}
                        </button>
                        {rulesOpen === v.key && (
                          <div className="mt-2 space-y-2 rounded-lg bg-white p-2">
                            <p className="text-xs text-slate-500">Deixe em branco para usar a regra do produto/grupo.</p>
                            {linked.map((gk) => {
                              const g = cfg.addonGroups.find((x) => x.key === gk);
                              if (!g) return null;
                              const r = v.rules[gk] ?? {};
                              const setRule = (field: "free" | "max", val: number | null) =>
                                setVariant(i, (vv) => {
                                  const next = { ...(vv.rules[gk] ?? {}) };
                                  if (val === null) delete next[field];
                                  else next[field] = val;
                                  if (Object.keys(next).length) vv.rules[gk] = next;
                                  else delete vv.rules[gk];
                                });
                              return (
                                <div key={gk} className="flex flex-wrap items-center gap-2 text-sm">
                                  <span className="min-w-32 flex-1 font-semibold">{g.name}</span>
                                  <label className="flex items-center gap-1">grátis <NumberInput allowEmpty value={r.free ?? null} onChange={(n) => setRule("free", n)} className="w-20" placeholder={String(g.free)} /></label>
                                  <label className="flex items-center gap-1">máx. <NumberInput allowEmpty min={1} value={r.max ?? null} onChange={(n) => setRule("max", n)} className="w-20" placeholder={g.max === null ? "∞" : String(g.max)} /></label>
                                </div>
                              );
                            })}
                          </div>
                        )}
                      </>
                    )}
                  </li>
                ))}
              </ul>
              <div className="flex flex-wrap gap-2">
                {SIZE_PRESETS.filter((s) => !p.variants!.some((v) => v.name === s)).map((s) => (
                  <Button key={s} size="sm" onClick={() => addVariant(s)}><Plus className="size-3" /> {s}</Button>
                ))}
                <Button size="sm" onClick={() => addVariant("Novo tamanho")}><Plus className="size-3" /> Outro</Button>
              </div>
            </div>
          )}
        </section>

        <section className="rounded-xl bg-white p-4 ring-1 ring-slate-200">
          <h3 className="font-extrabold">Opções de personalização</h3>
          <p className="mb-3 text-sm text-slate-500">Escolha quais grupos (base, acompanhamentos, adicionais…) o cliente pode personalizar neste produto. Cadastre os grupos na aba Acompanhamentos.</p>
          {cfg.addonGroups.length === 0 && <p className="text-sm text-slate-400">Nenhum grupo cadastrado.</p>}
          <ul className="space-y-2">
            {links.map((l, i) => {
              const gk = groupKeyOf(l);
              const g = cfg.addonGroups.find((x) => x.key === gk);
              const o = linkOverrides(l);
              const setO = (field: keyof RuleOverride, val: number | null) =>
                set((d) => {
                  const cur = linkOverrides(d.addonGroups![i]);
                  if (val === null) delete cur[field];
                  else cur[field] = val;
                  d.addonGroups![i] = makeLink(gk, cur);
                });
              return (
                <li key={gk} className="rounded-xl bg-slate-50 p-2">
                  <div className="flex items-center gap-2">
                    <MoveButtons first={i === 0} last={i === links.length - 1} onUp={() => set((d) => { d.addonGroups = move(d.addonGroups!, i, -1); })} onDown={() => set((d) => { d.addonGroups = move(d.addonGroups!, i, 1); })} />
                    <span className="flex-1 font-semibold">{g?.name ?? gk}</span>
                    <IconButton label="Remover grupo do produto" onClick={() => set((d) => { d.addonGroups!.splice(i, 1); })}><Trash2 className="size-4" /></IconButton>
                  </div>
                  {g && (
                    <div className="mt-1 flex flex-wrap items-center gap-2 pl-9 text-sm">
                      <span className="text-xs text-slate-500">Só neste produto:</span>
                      <label className="flex items-center gap-1">mín. <NumberInput allowEmpty value={o.min ?? null} onChange={(n) => setO("min", n)} className="w-18" placeholder={String(g.min)} /></label>
                      <label className="flex items-center gap-1">máx. <NumberInput allowEmpty min={1} value={o.max ?? null} onChange={(n) => setO("max", n)} className="w-18" placeholder={g.max === null ? "∞" : String(g.max)} /></label>
                      <label className="flex items-center gap-1">grátis <NumberInput allowEmpty value={o.free ?? null} onChange={(n) => setO("free", n)} className="w-18" placeholder={String(g.free)} /></label>
                    </div>
                  )}
                </li>
              );
            })}
          </ul>
          {cfg.addonGroups.some((g) => !linked.includes(g.key)) && (
            <div className="mt-3 flex flex-wrap gap-2">
              {cfg.addonGroups.filter((g) => !linked.includes(g.key)).map((g) => (
                <Button key={g.key} size="sm" onClick={() => set((d) => { d.addonGroups = [...(d.addonGroups ?? []), g.key]; })}>
                  <Plus className="size-3" /> {g.name}
                </Button>
              ))}
            </div>
          )}
        </section>

        <section className="rounded-xl bg-white p-4 ring-1 ring-slate-200">
          <h3 className="mb-3 font-extrabold">Selos</h3>
          <div className="flex flex-wrap gap-2">
            {BADGES.map((b) => {
              const on = (p.badges ?? []).includes(b);
              return (
                <button key={b} type="button" onClick={() => set((d) => { d.badges = on ? (d.badges ?? []).filter((x) => x !== b) : [...(d.badges ?? []), b]; })}
                  className={cx("h-9 rounded-full px-3 text-sm font-semibold ring-1", on ? "bg-violet-700 text-white ring-violet-700" : "bg-white text-slate-600 ring-slate-200")} aria-pressed={on}>
                  {BADGE_LABEL[b]}
                </button>
              );
            })}
          </div>
        </section>
        <p className="text-xs text-slate-400">Código interno: {p.key}</p>
      </div>
    </Modal>
  );
}
