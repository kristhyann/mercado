"use client";
import { useEffect, useMemo, useRef, useState } from "react";
import { Ban, Plus, Search, Sparkles, X } from "lucide-react";
import { useStore } from "./StoreProvider";
import { Img } from "@/components/ui/Img";
import type { Category, Product } from "@/lib/menu";
import { formatBRL, normalizeText } from "@/lib/format";

const BADGE: Record<string, { label: string; cls: string }> = {
  "mais-vendido": { label: "🔥 Mais vendido", cls: "bg-accent text-on-accent" },
  promocao: { label: "Promoção", cls: "bg-rose-600 text-white" },
  novo: { label: "Novo", cls: "bg-emerald-600 text-white" },
  vegano: { label: "Vegano", cls: "bg-lime-600 text-white" },
  "zero-acucar": { label: "Zero açúcar", cls: "bg-sky-600 text-white" },
  destaque: { label: "⭐ Destaque", cls: "bg-brand text-on-brand" },
};

export function Badges({ product, max = 2 }: { product: Product; max?: number }) {
  const list = [...product.badges];
  if (product.fromCompareAtPrice && product.fromCompareAtPrice > product.fromPrice && !list.includes("promocao")) list.unshift("promocao");
  return (
    <>
      {list.slice(0, max).map((b) => (
        <span key={b} className={`inline-flex items-center rounded-full px-2 py-0.5 text-[11px] font-bold uppercase tracking-wide ${BADGE[b]?.cls ?? "bg-brand text-on-brand"}`}>
          {BADGE[b]?.label ?? b}
        </span>
      ))}
    </>
  );
}

function Price({ product }: { product: Product }) {
  const multi = product.variants.filter((v) => v.available).length > 1;
  return (
    <div className="flex items-baseline gap-2">
      {multi && <span className="text-xs font-medium text-muted">a partir de</span>}
      <span className="text-[17px] font-extrabold text-brand">{formatBRL(product.fromPrice)}</span>
      {product.fromCompareAtPrice && product.fromCompareAtPrice > product.fromPrice && (
        <span className="text-sm text-muted line-through">{formatBRL(product.fromCompareAtPrice)}</span>
      )}
    </div>
  );
}

function useAdd() {
  const { openProduct, cart, toast, status, menu } = useStore();
  return (product: Product) => {
    if (!product.available) return;
    if (product.isSimple) {
      cart.add({ productKey: product.key, variantKey: product.variants[0].key, selections: {}, quantity: 1, notes: "" });
      toast(`${product.name} adicionado ao pedido`);
      if (!status.canOrder) setTimeout(() => toast(status.paused ? "Pedidos pausados no momento" : `${menu.name} está fechada agora`), 1400);
      return;
    }
    openProduct(product.key);
  };
}

function ProductCard({ product }: { product: Product }) {
  const add = useAdd();
  const unavailable = !product.available;
  return (
    <article
      className={`group relative flex gap-3 rounded-3xl bg-white p-3 shadow-card ring-1 ring-line/60 transition sm:p-4 ${unavailable ? "opacity-60" : "hover:-translate-y-0.5 hover:shadow-lg"}`}
    >
      <button
        type="button"
        onClick={() => add(product)}
        disabled={unavailable}
        className="absolute inset-0 z-0 rounded-3xl"
        aria-label={unavailable ? `${product.name} indisponível` : `Ver ${product.name}`}
      />
      <div className="pointer-events-none relative z-[1] flex min-w-0 flex-1 flex-col">
        <div className="flex flex-wrap gap-1">
          <Badges product={product} />
        </div>
        <h3 className="mt-1 text-[16px] font-bold leading-snug text-ink">{product.name}</h3>
        {product.description && <p className="mt-1 line-clamp-2 text-[13.5px] leading-snug text-muted">{product.description}</p>}
        <div className="mt-auto pt-2">
          {unavailable ? (
            <span className="inline-flex items-center gap-1 text-sm font-bold text-muted">
              <Ban className="size-4" /> Indisponível
            </span>
          ) : (
            <Price product={product} />
          )}
        </div>
      </div>
      <div className="pointer-events-none relative z-[1] flex shrink-0 flex-col items-end">
        <div className="relative size-28 overflow-hidden rounded-2xl bg-brand-softer sm:size-32">
          {product.image ? (
            <Img src={product.image} alt={product.name} fill sizes="128px" className={`object-cover transition duration-300 ${unavailable ? "grayscale" : "group-hover:scale-105"}`} />
          ) : (
            <div className="flex size-full items-center justify-center text-4xl">🍇</div>
          )}
        </div>
        {!unavailable && (
          <span className="relative z-[2] -mt-5 mr-2 flex h-10 items-center gap-1 rounded-full bg-brand px-4 text-sm font-extrabold text-on-brand shadow-float">
            <Plus className="size-4" strokeWidth={3} /> ADICIONAR
          </span>
        )}
      </div>
    </article>
  );
}

function FeaturedCard({ product }: { product: Product }) {
  const add = useAdd();
  return (
    <button
      type="button"
      onClick={() => add(product)}
      className="group relative w-[78%] shrink-0 snap-start overflow-hidden rounded-3xl bg-white text-left shadow-card ring-1 ring-line/60 sm:w-[340px]"
    >
      <div className="relative aspect-[4/3] w-full overflow-hidden bg-brand-softer">
        {product.image && <Img src={product.image} alt={product.name} fill sizes="(max-width: 640px) 80vw, 340px" className="object-cover transition duration-500 group-hover:scale-105" />}
        <div className="absolute left-3 top-3 flex gap-1">
          <Badges product={product} />
        </div>
      </div>
      <div className="flex items-end justify-between gap-3 p-4">
        <div className="min-w-0">
          <h3 className="truncate text-[17px] font-extrabold">{product.name}</h3>
          <Price product={product} />
        </div>
        <span className="flex size-11 shrink-0 items-center justify-center rounded-full bg-brand text-on-brand shadow-float transition group-active:scale-90">
          <Plus className="size-5" strokeWidth={3} />
        </span>
      </div>
    </button>
  );
}

export function Banner() {
  const { menu } = useStore();
  const b = menu.banner;
  if (!b.enabled || (!b.image && !b.title)) return null;
  return (
    <section className="mx-auto mt-5 max-w-5xl px-4" aria-label="Promoção">
      <div className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-brand to-brand-strong shadow-card">
        {b.image && <Img src={b.image} alt="" fill sizes="(max-width: 1024px) 100vw, 1024px" className="object-cover" />}
        <div className="relative flex min-h-36 flex-col justify-center bg-gradient-to-r from-black/55 via-black/25 to-transparent p-5 sm:min-h-48 sm:p-8">
          {b.title && <p className="max-w-[70%] text-xl font-extrabold leading-tight text-white drop-shadow sm:text-3xl">{b.title}</p>}
          {b.subtitle && <p className="mt-1.5 max-w-[65%] text-sm font-medium text-white/90 sm:text-base">{b.subtitle}</p>}
        </div>
      </div>
    </section>
  );
}

export function MenuBody() {
  const { menu } = useStore();
  const [query, setQuery] = useState("");
  const [active, setActive] = useState(menu.categories[0]?.key ?? "");
  const navRef = useRef<HTMLDivElement>(null);
  const clickLock = useRef(0);

  const q = normalizeText(query);
  const categories: Category[] = useMemo(() => {
    if (!q) return menu.categories;
    return menu.categories
      .map((c) => ({
        ...c,
        products: c.products.filter((p) => normalizeText(`${p.name} ${p.description ?? ""} ${c.name}`).includes(q)),
      }))
      .filter((c) => c.products.length > 0);
  }, [menu.categories, q]);

  const featured = useMemo(() => menu.categories.flatMap((c) => c.products).filter((p) => p.featured && p.available), [menu.categories]);

  // Destaca a categoria visível (scrollspy).
  useEffect(() => {
    const els = categories.map((c) => document.getElementById(`cat-${c.key}`)).filter(Boolean) as HTMLElement[];
    if (!els.length) return;
    const io = new IntersectionObserver(
      (entries) => {
        if (Date.now() < clickLock.current) return;
        const visible = entries.filter((e) => e.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        if (visible[0]) setActive(visible[0].target.id.replace("cat-", ""));
      },
      { rootMargin: "-130px 0px -55% 0px", threshold: 0 },
    );
    els.forEach((el) => io.observe(el));
    return () => io.disconnect();
  }, [categories]);

  // Mantém o botão da categoria ativa visível na barra horizontal.
  useEffect(() => {
    const btn = navRef.current?.querySelector<HTMLElement>(`[data-cat="${active}"]`);
    if (btn && navRef.current) {
      const nav = navRef.current;
      nav.scrollTo({ left: btn.offsetLeft - nav.clientWidth / 2 + btn.clientWidth / 2, behavior: "smooth" });
    }
  }, [active]);

  function goTo(key: string) {
    setActive(key);
    clickLock.current = Date.now() + 900;
    document.getElementById(`cat-${key}`)?.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  return (
    <>
      <div className="sticky top-0 z-30 mt-5 border-b border-line/70 bg-canvas/90 backdrop-blur-md">
        <div className="mx-auto max-w-5xl px-4 pt-3">
          <label className="relative block">
            <span className="sr-only">Buscar no cardápio</span>
            <Search className="pointer-events-none absolute left-4 top-1/2 size-5 -translate-y-1/2 text-muted" />
            <input
              type="search"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Buscar açaí, combos, bebidas…"
              className="h-12 w-full rounded-2xl border border-line bg-white pl-12 pr-12 text-[16px] shadow-sm outline-none transition placeholder:text-muted/70 focus:border-brand focus:ring-4 focus:ring-brand/15"
              enterKeyHint="search"
            />
            {query && (
              <button onClick={() => setQuery("")} className="absolute right-2 top-1/2 flex size-9 -translate-y-1/2 items-center justify-center rounded-full hover:bg-canvas" aria-label="Limpar busca">
                <X className="size-4" />
              </button>
            )}
          </label>
        </div>
        <nav ref={navRef} className="no-scrollbar mx-auto flex max-w-5xl gap-2 overflow-x-auto px-4 py-3" aria-label="Categorias">
          {categories.map((c) => (
            <button
              key={c.key}
              data-cat={c.key}
              onClick={() => goTo(c.key)}
              className={`h-10 shrink-0 rounded-full px-4 text-sm font-bold transition active:scale-95 ${
                active === c.key ? "bg-brand text-on-brand shadow-md" : "bg-white text-ink/80 ring-1 ring-line hover:bg-brand-softer"
              }`}
              aria-current={active === c.key ? "true" : undefined}
            >
              {c.name}
            </button>
          ))}
        </nav>
      </div>

      <main className="mx-auto max-w-5xl px-4 pb-36">
        {!q && featured.length > 0 && (
          <section className="mt-6" aria-labelledby="destaques">
            <h2 id="destaques" className="flex items-center gap-2 text-xl font-extrabold">
              <Sparkles className="size-5 text-accent" /> Destaques
            </h2>
            <div className="no-scrollbar -mx-4 mt-3 flex snap-x snap-mandatory gap-3 overflow-x-auto scroll-px-4 px-4 pb-2">
              {featured.map((p) => (
                <FeaturedCard key={p.key} product={p} />
              ))}
            </div>
          </section>
        )}

        {categories.length === 0 && (
          <div className="mt-16 text-center">
            <p className="text-4xl">🔎</p>
            <p className="mt-2 font-bold">Nada encontrado para “{query}”.</p>
            <button onClick={() => setQuery("")} className="mt-3 font-semibold text-brand underline">
              Ver cardápio completo
            </button>
          </div>
        )}

        {categories.map((c) => (
          <section key={c.key} id={`cat-${c.key}`} className="scroll-mt-header mt-8" aria-labelledby={`h-${c.key}`}>
            <h2 id={`h-${c.key}`} className="text-xl font-extrabold tracking-tight">
              {c.name}
            </h2>
            {c.description && <p className="mt-0.5 text-sm text-muted">{c.description}</p>}
            <div className="mt-3 grid gap-3 md:grid-cols-2">
              {c.products.map((p) => (
                <ProductCard key={p.key} product={p} />
              ))}
            </div>
          </section>
        ))}
      </main>
    </>
  );
}
