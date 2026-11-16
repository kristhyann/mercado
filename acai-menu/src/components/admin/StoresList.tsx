"use client";
import { useMemo, useState, useTransition } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { ExternalLink, Pencil, Plus, Search, Store } from "lucide-react";
import type { AdminStoreRow } from "@/lib/admin/backend";
import { setStoreActiveAction } from "@/app/admin/actions";
import { previewUrl } from "@/lib/admin/editor";
import { normalizeText } from "@/lib/format";
import { Badge, EmptyState, Toggle, inputCls } from "./ui";

export function StoresList({ stores, siteUrl }: { stores: AdminStoreRow[]; siteUrl: string }) {
  const router = useRouter();
  const [q, setQ] = useState("");
  const [filter, setFilter] = useState<"all" | "active" | "inactive">("all");
  const [pending, start] = useTransition();
  const [error, setError] = useState<string | null>(null);
  const [optimistic, setOptimistic] = useState<Record<string, boolean>>({});

  const list = useMemo(() => {
    const n = normalizeText(q);
    return stores.filter((s) => {
      const active = optimistic[s.slug] ?? s.isActive;
      if (filter === "active" && !active) return false;
      if (filter === "inactive" && active) return false;
      return !n || normalizeText(`${s.name} ${s.slug}`).includes(n);
    });
  }, [stores, q, filter, optimistic]);

  function toggle(slug: string, value: boolean) {
    setOptimistic((o) => ({ ...o, [slug]: value }));
    setError(null);
    start(async () => {
      const res = await setStoreActiveAction(slug, value);
      if (!res.ok) {
        setError(res.error);
        setOptimistic((o) => ({ ...o, [slug]: !value }));
      }
      router.refresh();
    });
  }

  return (
    <div className="space-y-4">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h1 className="text-2xl font-extrabold tracking-tight">Lojas</h1>
          <p className="text-sm text-slate-500">{stores.length} cadastradas</p>
        </div>
        <Link href="/admin/lojas/nova" className="inline-flex h-11 items-center gap-2 rounded-xl bg-violet-700 px-4 text-sm font-bold text-white hover:bg-violet-800">
          <Plus className="size-4" /> Nova loja
        </Link>
      </div>

      <div className="flex flex-col gap-2 sm:flex-row">
        <label className="relative flex-1">
          <Search className="pointer-events-none absolute left-3 top-1/2 size-4 -translate-y-1/2 text-slate-400" />
          <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="Buscar loja…" className={inputCls + " pl-9"} />
        </label>
        <div className="flex rounded-xl bg-white p-1 ring-1 ring-slate-200">
          {(["all", "active", "inactive"] as const).map((f) => (
            <button key={f} onClick={() => setFilter(f)} className={`h-9 flex-1 rounded-lg px-3 text-sm font-semibold sm:flex-none ${filter === f ? "bg-violet-700 text-white" : "text-slate-600"}`}>
              {f === "all" ? "Todas" : f === "active" ? "Ativas" : "Inativas"}
            </button>
          ))}
        </div>
      </div>
      {error && <p className="rounded-xl bg-rose-50 p-3 text-sm font-semibold text-rose-700">{error}</p>}

      {list.length === 0 ? (
        <EmptyState icon={<Store className="size-6" />} title="Nenhuma loja encontrada" />
      ) : (
        <ul className="grid gap-3 md:grid-cols-2">
          {list.map((s) => {
            const active = optimistic[s.slug] ?? s.isActive;
            return (
              <li key={s.slug} className="rounded-2xl bg-white p-4 shadow-sm ring-1 ring-slate-200/70">
                <div className="flex items-start gap-3">
                  <span className="relative size-14 shrink-0 overflow-hidden rounded-xl" style={{ background: s.primaryColor }}>
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    {s.logo && <img src={previewUrl(s.slug, s.logo)!} alt="" className="size-full object-cover" />}
                  </span>
                  <div className="min-w-0 flex-1">
                    <div className="flex flex-wrap items-center gap-1.5">
                      <h2 className="truncate font-extrabold">{s.name}</h2>
                      {s.isDemo && <Badge tone="amber">Demo</Badge>}
                    </div>
                    <p className="truncate text-sm text-slate-500">/{s.slug}</p>
                    <p className="mt-1 text-xs text-slate-500">
                      {s.activeProductCount}/{s.productCount} produtos ativos · {s.categoryCount} categorias · WhatsApp {s.whatsapp}
                    </p>
                  </div>
                </div>
                <div className="mt-3 flex flex-wrap items-center justify-between gap-2 border-t border-slate-100 pt-3">
                  <Toggle checked={active} disabled={pending} onChange={(v) => toggle(s.slug, v)} label={active ? "Ativa" : "Inativa"} />
                  <div className="flex gap-2">
                    {active && (
                      <a href={`${siteUrl}/${s.slug}`} target="_blank" rel="noopener noreferrer" className="inline-flex h-10 items-center gap-1.5 rounded-xl px-3 text-sm font-semibold text-slate-600 ring-1 ring-slate-200 hover:bg-slate-50">
                        <ExternalLink className="size-4" /> Ver
                      </a>
                    )}
                    <Link href={`/admin/lojas/${s.slug}`} className="inline-flex h-10 items-center gap-1.5 rounded-xl bg-violet-700 px-4 text-sm font-bold text-white hover:bg-violet-800">
                      <Pencil className="size-4" /> Editar
                    </Link>
                  </div>
                </div>
              </li>
            );
          })}
        </ul>
      )}
    </div>
  );
}
