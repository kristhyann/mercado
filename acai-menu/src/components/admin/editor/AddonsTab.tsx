"use client";
import { useState } from "react";
import { ChevronDown, Layers, Plus, Trash2 } from "lucide-react";
import { useEditor } from "./context";
import { Badge, Button, Card, ConfirmButton, EmptyState, Field, IconButton, MoneyInput, MoveButtons, NumberInput, Select, TextInput, Toggle, cx } from "../ui";
import { groupKeyOf, move, removeGroupEverywhere, uniqueKey, type AddonGroup } from "@/lib/admin/editor";
import { formatBRL } from "@/lib/format";

const PRESETS: { label: string; desc: string; make: (key: string) => AddonGroup }[] = [
  { label: "Escolha obrigatória (1 opção)", desc: "Ex.: base do açaí, sabor", make: (key) => ({ key, name: "Escolha a base", description: null, min: 1, max: 1, free: 1, extraPrice: 0, maxPerOption: 1, addons: [] }) },
  { label: "Acompanhamentos (grátis + extra)", desc: "Ex.: 3 grátis, até 6, R$ 2,00 cada extra", make: (key) => ({ key, name: "Acompanhamentos", description: null, min: 0, max: 6, free: 3, extraPrice: 2, maxPerOption: 1, addons: [] }) },
  { label: "Adicionais pagos", desc: "Cada opção tem seu preço", make: (key) => ({ key, name: "Adicionais", description: null, min: 0, max: null, free: 0, extraPrice: 0, maxPerOption: 3, addons: [] }) },
];

function summary(g: AddonGroup) {
  const p: string[] = [];
  p.push(g.min > 0 ? `obrigatório (mín. ${g.min})` : "opcional");
  p.push(g.max === null ? "sem limite" : `até ${g.max}`);
  if (g.free > 0) p.push(`${g.free} grátis`);
  if (g.extraPrice > 0) p.push(`extra ${formatBRL(Math.round(g.extraPrice * 100))}`);
  return p.join(" · ");
}

export function AddonsTab() {
  const { cfg, update } = useEditor();
  const [open, setOpen] = useState<string | null>(cfg.addonGroups[0]?.key ?? null);
  const used = (k: string) => cfg.products.filter((p) => (p.addonGroups ?? []).some((l) => groupKeyOf(l) === k)).length;

  function addGroup(i: number) {
    const key = uniqueKey(PRESETS[i].make("x").name, cfg.addonGroups.map((g) => g.key));
    update((d) => { d.addonGroups.push(PRESETS[i].make(key)); });
    setOpen(key);
  }

  return (
    <div className="space-y-4">
      <Card title="Novo grupo de opções" description="Grupos são reaproveitados por vários produtos (ex.: o mesmo grupo de acompanhamentos para copos, tigelas e barcas).">
        <div className="grid gap-2 sm:grid-cols-3">
          {PRESETS.map((p, i) => (
            <button key={p.label} type="button" onClick={() => addGroup(i)} className="rounded-xl border-2 border-dashed border-slate-200 p-3 text-left hover:border-violet-400 hover:bg-violet-50">
              <span className="flex items-center gap-1 font-bold text-slate-800"><Plus className="size-4" /> {p.label}</span>
              <span className="text-xs text-slate-500">{p.desc}</span>
            </button>
          ))}
        </div>
      </Card>

      {cfg.addonGroups.length === 0 && <EmptyState icon={<Layers className="size-6" />} title="Nenhum grupo de opções" />}

      {cfg.addonGroups.map((g, gi) => {
        const isOpen = open === g.key;
        const setG = (fn: (d: AddonGroup) => void) => update((d) => fn(d.addonGroups[gi]));
        return (
          <section key={g.key} className="rounded-2xl bg-white shadow-sm ring-1 ring-slate-200/70">
            <div className="flex items-center gap-2 p-3">
              <MoveButtons first={gi === 0} last={gi === cfg.addonGroups.length - 1} onUp={() => update((d) => { d.addonGroups = move(d.addonGroups, gi, -1); })} onDown={() => update((d) => { d.addonGroups = move(d.addonGroups, gi, 1); })} />
              <button onClick={() => setOpen(isOpen ? null : g.key)} className="min-w-0 flex-1 text-left">
                <span className="flex flex-wrap items-center gap-2">
                  <span className="font-extrabold">{g.name}</span>
                  <Badge>{g.addons.length} opções</Badge>
                  <Badge tone={used(g.key) ? "violet" : "amber"}>{used(g.key) ? `em ${used(g.key)} produto(s)` : "não usado"}</Badge>
                </span>
                <span className="block text-xs text-slate-500">{summary(g)}</span>
              </button>
              <ConfirmButton message={`Excluir o grupo "${g.name}"? Ele será removido de ${used(g.key)} produto(s).`} onConfirm={() => update((d) => { d.addonGroups.splice(gi, 1); d.products = removeGroupEverywhere(d.products, g.key); })}>
                <IconButton label="Excluir grupo"><Trash2 className="size-4 text-rose-500" /></IconButton>
              </ConfirmButton>
              <IconButton label={isOpen ? "Recolher" : "Expandir"} onClick={() => setOpen(isOpen ? null : g.key)}><ChevronDown className={cx("size-5 transition", isOpen && "rotate-180")} /></IconButton>
            </div>

            {isOpen && (
              <div className="space-y-4 border-t border-slate-100 p-4">
                <div className="grid gap-3 sm:grid-cols-2">
                  <Field label="Nome do grupo (aparece para o cliente)"><TextInput value={g.name} onChange={(v) => setG((d) => { d.name = v; })} maxLength={120} /></Field>
                  <Field label="Descrição (opcional)"><TextInput value={g.description} onChange={(v) => setG((d) => { d.description = v || null; })} placeholder="Ex.: Os 3 primeiros são grátis" /></Field>
                </div>
                <div className="grid grid-cols-2 gap-3 sm:grid-cols-5">
                  <div className="col-span-2 flex items-end pb-2 sm:col-span-1">
                    <Toggle checked={g.min > 0} onChange={(v) => setG((d) => { d.min = v ? Math.max(1, d.min) : 0; })} label="Obrigatório" />
                  </div>
                  <Field label="Mínimo"><NumberInput value={g.min} onChange={(n) => setG((d) => { d.min = n ?? 0; })} /></Field>
                  <Field label="Máximo" hint="vazio = sem limite"><NumberInput allowEmpty min={1} value={g.max} onChange={(n) => setG((d) => { d.max = n; })} placeholder="∞" /></Field>
                  <Field label="Quantos grátis"><NumberInput value={g.free} onChange={(n) => setG((d) => { d.free = n ?? 0; })} /></Field>
                  <Field label="Valor do extra" hint="por escolha além das grátis"><MoneyInput value={g.extraPrice} onChange={(v) => setG((d) => { d.extraPrice = v ?? 0; })} /></Field>
                </div>
                <Field label="Repetir a mesma opção" className="max-w-xs">
                  <Select value={String(g.maxPerOption)} onChange={(v) => setG((d) => { d.maxPerOption = Number(v); })}>
                    <option value="1">Não (marcar/desmarcar)</option>
                    {[2, 3, 4, 5].map((n) => <option key={n} value={n}>Até {n}x a mesma opção</option>)}
                  </Select>
                </Field>

                <div>
                  <h3 className="mb-2 text-sm font-extrabold">Opções</h3>
                  <ul className="space-y-2">
                    {g.addons.map((a, ai) => (
                      <li key={ai} className={cx("rounded-xl bg-slate-50 p-2", !a.active && "opacity-60")}>
                        <div className="flex flex-wrap items-center gap-2">
                          <MoveButtons first={ai === 0} last={ai === g.addons.length - 1} onUp={() => setG((d) => { d.addons = move(d.addons, ai, -1); })} onDown={() => setG((d) => { d.addons = move(d.addons, ai, 1); })} />
                          <TextInput value={a.name} onChange={(v) => setG((d) => { d.addons[ai].name = v; })} className="min-w-36 flex-1" aria-label="Nome da opção" />
                          <Select value={a.alwaysPaid ? "paid" : a.price > 0 ? "priced" : "free"} className="w-48"
                            onChange={(v) => setG((d) => {
                              const x = d.addons[ai];
                              if (v === "free") { x.alwaysPaid = false; x.price = 0; }
                              if (v === "priced") { x.alwaysPaid = false; if (!x.price) x.price = 2; }
                              if (v === "paid") { x.alwaysPaid = true; if (!x.price) x.price = 2; }
                            })}>
                            <option value="free">Incluído / gratuito{g.extraPrice > 0 ? " (extra cobra o valor do grupo)" : ""}</option>
                            <option value="priced">Com preço próprio</option>
                            <option value="paid">Adicional sempre pago</option>
                          </Select>
                          {(a.price > 0 || a.alwaysPaid) && <MoneyInput value={a.price} onChange={(v) => setG((d) => { d.addons[ai].price = v ?? 0; })} className="w-28" />}
                          <label className="flex items-center gap-1 text-xs font-semibold text-slate-600"><Toggle checked={a.available} onChange={(v) => setG((d) => { d.addons[ai].available = v; })} /> Disponível</label>
                          <label className="flex items-center gap-1 text-xs font-semibold text-slate-600"><Toggle checked={a.active} onChange={(v) => setG((d) => { d.addons[ai].active = v; })} /> Ativo</label>
                          <IconButton label="Remover opção" onClick={() => setG((d) => { d.addons.splice(ai, 1); })}><Trash2 className="size-4" /></IconButton>
                        </div>
                      </li>
                    ))}
                  </ul>
                  <Button size="sm" className="mt-2" onClick={() => setG((d) => { d.addons.push({ key: uniqueKey("nova-opcao", d.addons.map((x) => x.key)), name: "Nova opção", description: null, price: 0, alwaysPaid: false, available: true, active: true }); })}>
                    <Plus className="size-4" /> Adicionar opção
                  </Button>
                </div>
                <p className="rounded-xl bg-slate-50 p-3 text-xs text-slate-600">
                  <b>Como o preço é calculado:</b> as primeiras <b>{g.free}</b> escolhas são grátis; cada escolha além disso custa o preço próprio da opção ou, se ela não tiver preço, {formatBRL(Math.round(g.extraPrice * 100))}. “Adicional sempre pago” é cobrado sempre e não usa as grátis. Os tamanhos podem mudar estes números (aba Produtos → regras do tamanho).
                </p>
              </div>
            )}
          </section>
        );
      })}
    </div>
  );
}
