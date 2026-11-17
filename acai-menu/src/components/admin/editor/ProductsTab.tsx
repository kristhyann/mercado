"use client";
import { useMemo, useState } from "react";
import { Copy, EyeOff, Package, Pencil, Plus, Search, Trash2 } from "lucide-react";
import { useEditor } from "./context";
import { Badge, Button, ConfirmButton, EmptyState, IconButton, MoveButtons, Select, Toggle, inputCls } from "../ui";
import { duplicateProduct, previewUrl, uniqueKey, type Product } from "@/lib/admin/editor";
import { formatBRL, normalizeText } from "@/lib/format";
import { ProductForm } from "./ProductForm";

function priceLabel(p: Product) {
  if (p.variants?.length) {
    const prices = p.variants.map((v) => v.price);
    const min = Math.min(...prices), max = Math.max(...prices);
    return min === max ? formatBRL(Math.round(min * 100)) : `${formatBRL(Math.round(min * 100))} – ${formatBRL(Math.round(max * 100))}`;
  }
  return p.price != null ? formatBRL(Math.round(p.price * 100)) : "sem preço";
}

export function ProductsTab() {
  const { cfg, update, slug } = useEditor();
  const [q, setQ] = useState("");
  const [cat, setCat] = useState("");
  const [editing, setEditing] = useState<string | null>(null);

  const visible = useMemo(() => {
    const n = normalizeText(q);
    return cfg.products
      .map((p, index) => ({ p, index }))
      .filter(({ p }) => (!cat || p.category === cat) && (!n || normalizeText(`${p.name} ${p.description ?? ""}`).includes(n)));
  }, [cfg.products, q, cat]);

  /** Move dentro da mesma categoria (a ordem no cardápio é por categoria). */
  function moveWithinCategory(index: number, delta: number) {
    update((d) => {
      const c = d.products[index].category;
      let j = index + delta;
      while (j >= 0 && j < d.products.length && d.products[j].category !== c) j += delta;
      if (j < 0 || j >= d.products.length) return;
      [d.products[index], d.products[j]] = [d.products[j], d.products[index]];
    });
  }

  function addProduct() {
    const category = cat || cfg.categories[0]?.key;
    if (!category) return;
    const key = uniqueKey("novo-produto", cfg.products.map((p) => p.key));
    update((d) => { d.products.push({ key, category, name: "Novo produto", description: null, image: null, price: 10, active: true, available: true, badges: [], featured: false, addonGroups: [] }); });
    setEditing(key);
  }

  const byCategory = cfg.categories.map((c) => ({ c, items: visible.filter(({ p }) => p.category === c.key) })).filter((g) => g.items.length);
  const orphans = visible.filter(({ p }) => !cfg.categories.some((c) => c.key === p.category));

  return (
    <div className="space-y-4">
      <div className="flex flex-col gap-2 sm:flex-row">
        <label className="relative flex-1">
          <Search className="pointer-events-none absolute left-3 top-1/2 size-4 -translate-y-1/2 text-slate-400" />
          <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="Buscar produto…" className={inputCls + " pl-9"} />
        </label>
        <Select value={cat} onChange={setCat} className="sm:w-56">
          <option value="">Todas as categorias</option>
          {cfg.categories.map((c) => <option key={c.key} value={c.key}>{c.name}</option>)}
        </Select>
        <Button variant="primary" onClick={addProduct} disabled={!cfg.categories.length}><Plus className="size-4" /> Novo produto</Button>
      </div>
      {!cfg.categories.length && <p className="rounded-xl bg-amber-50 p-3 text-sm text-amber-900">Crie uma categoria antes de adicionar produtos.</p>}

      {visible.length === 0 && <EmptyState icon={<Package className="size-6" />} title="Nenhum produto encontrado" />}

      {[...byCategory, ...(orphans.length ? [{ c: { key: "__", name: "Sem categoria válida" }, items: orphans }] : [])].map(({ c, items }) => (
        <section key={c.key} className="rounded-2xl bg-white shadow-sm ring-1 ring-slate-200/70">
          <h2 className="border-b border-slate-100 px-4 py-3 font-extrabold">{c.name} <span className="text-sm font-semibold text-slate-400">({items.length})</span></h2>
          <ul className="divide-y divide-slate-100">
            {items.map(({ p, index }, k) => {
              const img = previewUrl(slug, p.image);
              return (
                <li key={p.key} className={`flex items-center gap-2 px-2 py-2 sm:px-3 ${p.active === false ? "opacity-60" : ""}`}>
                  <MoveButtons first={k === 0} last={k === items.length - 1} onUp={() => moveWithinCategory(index, -1)} onDown={() => moveWithinCategory(index, 1)} />
                  <button onClick={() => setEditing(p.key)} className="flex min-w-0 flex-1 items-center gap-3 text-left">
                    <span className="relative size-14 shrink-0 overflow-hidden rounded-xl bg-slate-100">
                      {/* eslint-disable-next-line @next/next/no-img-element */}
                      {img ? <img src={img} alt="" className="size-full object-cover" /> : <Package className="m-auto mt-4 size-6 text-slate-300" />}
                    </span>
                    <span className="min-w-0">
                      <span className="block truncate font-bold">{p.name}</span>
                      <span className="block truncate text-sm text-slate-500">{priceLabel(p)}{p.variants?.length ? ` · ${p.variants.length} tamanhos` : ""}</span>
                      <span className="mt-0.5 flex flex-wrap gap-1">
                        {p.active === false && <Badge><EyeOff className="mr-1 size-3" />Oculto</Badge>}
                        {p.available === false && <Badge tone="red">Indisponível</Badge>}
                        {p.featured && <Badge tone="violet">Destaque</Badge>}
                      </span>
                    </span>
                  </button>
                  <div className="hidden sm:block"><Toggle checked={p.active !== false} onChange={(v) => update((d) => { d.products[index].active = v; })} /></div>
                  <IconButton label="Editar" onClick={() => setEditing(p.key)}><Pencil className="size-4" /></IconButton>
                  <IconButton label="Duplicar" onClick={() => update((d) => { d.products = duplicateProduct(d.products, p.key); })}><Copy className="size-4" /></IconButton>
                  <ConfirmButton message={`Excluir "${p.name}"? Esta ação será aplicada ao salvar.`} onConfirm={() => update((d) => { d.products.splice(index, 1); })}>
                    <IconButton label="Excluir"><Trash2 className="size-4 text-rose-500" /></IconButton>
                  </ConfirmButton>
                </li>
              );
            })}
          </ul>
        </section>
      ))}

      {editing && <ProductForm productKey={editing} onClose={() => setEditing(null)} onRename={setEditing} />}
    </div>
  );
}
