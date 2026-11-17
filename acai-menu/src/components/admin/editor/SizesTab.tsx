"use client";
import { useState } from "react";
import { Plus, Ruler, Trash2 } from "lucide-react";
import { useEditor } from "./context";
import { Button, Card, ConfirmButton, EmptyState, Field, IconButton, MoneyInput, TextInput } from "../ui";
import { sizeNames, uniqueKey } from "@/lib/admin/editor";

export function SizesTab() {
  const { cfg, update } = useEditor();
  const sizes = sizeNames(cfg.products);
  const rows = cfg.products.map((p, index) => ({ p, index })).filter(({ p }) => p.variants?.length);
  const [newSize, setNewSize] = useState("");
  const [newPrice, setNewPrice] = useState<number | null>(null);
  const [targets, setTargets] = useState<string[]>([]);

  function renameSize(from: string, to: string) {
    update((d) => { for (const p of d.products) for (const v of p.variants ?? []) if (v.name === from) v.name = to; });
  }
  function removeSize(name: string) {
    update((d) => { for (const p of d.products) if (p.variants && p.variants.length > 1) p.variants = p.variants.filter((v) => v.name !== name); });
  }
  function addTo(index: number, name: string, price: number) {
    update((d) => {
      const p = d.products[index];
      if (!p.variants) p.variants = [];
      if (p.variants.some((v) => v.name === name)) return;
      p.variants.push({ key: uniqueKey(name, p.variants.map((v) => v.key)), name, description: null, price, compareAtPrice: null, available: true, rules: {} });
    });
  }
  function addToMany() {
    const name = newSize.trim();
    if (!name || newPrice == null) return;
    for (const key of targets) {
      const i = cfg.products.findIndex((p) => p.key === key);
      if (i >= 0) addTo(i, name, newPrice);
    }
    setNewSize("");
    setTargets([]);
  }

  return (
    <div className="space-y-4">
      <Card title="Tabela de preços por tamanho" description="Cada produto tem seus próprios preços por tamanho. Edite direto na tabela. Para mudar o nome de um tamanho em todos os produtos, edite o cabeçalho.">
        {rows.length === 0 ? (
          <EmptyState icon={<Ruler className="size-6" />} title="Nenhum produto com tamanhos">No produto, escolha “Vários tamanhos” na seção Preço.</EmptyState>
        ) : (
          <div className="-mx-4 overflow-x-auto px-4 sm:-mx-5 sm:px-5">
            <table className="w-full min-w-max border-separate border-spacing-y-1 text-sm">
              <thead>
                <tr>
                  <th className="sticky left-0 z-10 bg-white pr-3 text-left font-bold text-slate-500">Produto</th>
                  {sizes.map((s) => (
                    <th key={s} className="px-1 text-left">
                      <div className="flex items-center gap-1">
                        <input defaultValue={s} onBlur={(e) => e.target.value.trim() && e.target.value !== s && renameSize(s, e.target.value.trim())} className="h-9 w-28 rounded-lg border border-transparent bg-slate-50 px-2 font-bold hover:border-slate-200 focus:border-violet-500 focus:outline-none" aria-label={`Nome do tamanho ${s}`} />
                        <ConfirmButton message={`Remover o tamanho "${s}" de todos os produtos? (produtos que só têm esse tamanho ficam como estão)`} onConfirm={() => removeSize(s)} label="Remover">
                          <IconButton label={`Remover ${s}`} className="size-7"><Trash2 className="size-3.5" /></IconButton>
                        </ConfirmButton>
                      </div>
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {rows.map(({ p, index }) => (
                  <tr key={p.key}>
                    <td className="sticky left-0 z-10 max-w-48 truncate bg-white pr-3 font-semibold">{p.name}</td>
                    {sizes.map((s) => {
                      const vi = p.variants!.findIndex((v) => v.name === s);
                      return (
                        <td key={s} className="px-1">
                          {vi >= 0 ? (
                            <MoneyInput value={p.variants![vi].price} onChange={(x) => update((d) => { d.products[index].variants![vi].price = x ?? 0; })} className="w-32" />
                          ) : (
                            <button onClick={() => addTo(index, s, p.variants!.at(-1)?.price ?? 0)} className="flex h-11 w-32 items-center justify-center gap-1 rounded-xl border border-dashed border-slate-200 text-xs font-semibold text-slate-400 hover:border-violet-400 hover:text-violet-600">
                              <Plus className="size-3" /> adicionar
                            </button>
                          )}
                        </td>
                      );
                    })}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </Card>

      <Card title="Adicionar um tamanho a vários produtos">
        <div className="grid gap-3 sm:grid-cols-3">
          <Field label="Tamanho"><TextInput value={newSize} onChange={setNewSize} placeholder="Ex.: 1 litro" /></Field>
          <Field label="Preço inicial"><MoneyInput value={newPrice} onChange={setNewPrice} allowEmpty /></Field>
          <div className="flex items-end"><Button variant="primary" className="w-full" onClick={addToMany} disabled={!newSize.trim() || newPrice == null || !targets.length}><Plus className="size-4" /> Adicionar a {targets.length} produto(s)</Button></div>
        </div>
        <div className="mt-3 flex flex-wrap gap-2">
          {cfg.products.filter((p) => p.variants?.length).map((p) => {
            const on = targets.includes(p.key);
            return (
              <button key={p.key} type="button" onClick={() => setTargets(on ? targets.filter((k) => k !== p.key) : [...targets, p.key])} className={`h-9 rounded-full px-3 text-sm font-semibold ring-1 ${on ? "bg-violet-700 text-white ring-violet-700" : "bg-white text-slate-600 ring-slate-200"}`} aria-pressed={on}>
                {p.name}
              </button>
            );
          })}
        </div>
      </Card>
    </div>
  );
}
