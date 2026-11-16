import Link from "next/link";
import { ArrowRight, Package, Plus, Store, ToggleLeft, ToggleRight } from "lucide-react";
import { backend } from "@/lib/admin/backend";
import { previewUrl } from "@/lib/admin/editor";

export const metadata = { title: "Painel" };

export default async function Dashboard() {
  const stores = await backend().listStores();
  const active = stores.filter((s) => s.isActive).length;
  const products = stores.reduce((s, x) => s + x.productCount, 0);
  const stats = [
    { label: "Lojas cadastradas", value: stores.length, icon: Store, tone: "bg-violet-50 text-violet-700" },
    { label: "Lojas ativas", value: active, icon: ToggleRight, tone: "bg-emerald-50 text-emerald-700" },
    { label: "Lojas inativas", value: stores.length - active, icon: ToggleLeft, tone: "bg-slate-100 text-slate-600" },
    { label: "Produtos cadastrados", value: products, icon: Package, tone: "bg-amber-50 text-amber-700" },
  ];
  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h1 className="text-2xl font-extrabold tracking-tight">Painel</h1>
          <p className="text-sm text-slate-500">Visão geral da plataforma</p>
        </div>
        <Link href="/admin/lojas/nova" className="inline-flex h-11 items-center gap-2 rounded-xl bg-violet-700 px-4 text-sm font-bold text-white hover:bg-violet-800">
          <Plus className="size-4" /> Nova loja
        </Link>
      </div>

      <div className="grid grid-cols-2 gap-3 lg:grid-cols-4">
        {stats.map((s) => (
          <div key={s.label} className="rounded-2xl bg-white p-4 shadow-sm ring-1 ring-slate-200/70">
            <span className={`flex size-10 items-center justify-center rounded-xl ${s.tone}`}>
              <s.icon className="size-5" />
            </span>
            <p className="mt-3 text-3xl font-extrabold tabular-nums">{s.value}</p>
            <p className="text-sm text-slate-500">{s.label}</p>
          </div>
        ))}
      </div>

      <section className="rounded-2xl bg-white shadow-sm ring-1 ring-slate-200/70">
        <div className="flex items-center justify-between border-b border-slate-100 px-4 py-3">
          <h2 className="font-extrabold">Últimas lojas adicionadas</h2>
          <Link href="/admin/lojas" className="text-sm font-bold text-violet-700">Ver todas</Link>
        </div>
        {stores.length === 0 ? (
          <p className="p-6 text-center text-sm text-slate-500">Nenhuma loja ainda. <Link href="/admin/lojas/nova" className="font-bold text-violet-700">Cadastre a primeira</Link>.</p>
        ) : (
          <ul className="divide-y divide-slate-100">
            {stores.slice(0, 6).map((s) => (
              <li key={s.slug}>
                <Link href={`/admin/lojas/${s.slug}`} className="flex items-center gap-3 px-4 py-3 hover:bg-slate-50">
                  <span className="relative size-11 shrink-0 overflow-hidden rounded-xl" style={{ background: s.primaryColor }}>
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    {s.logo && <img src={previewUrl(s.slug, s.logo)!} alt="" className="size-full object-cover" />}
                  </span>
                  <span className="min-w-0 flex-1">
                    <span className="block truncate font-bold">{s.name}</span>
                    <span className="block truncate text-xs text-slate-500">/{s.slug} · {s.productCount} produtos · criada em {new Date(s.createdAt).toLocaleDateString("pt-BR")}</span>
                  </span>
                  <span className={`rounded-full px-2 py-0.5 text-xs font-bold ${s.isActive ? "bg-emerald-100 text-emerald-700" : "bg-slate-100 text-slate-500"}`}>{s.isActive ? "Ativa" : "Inativa"}</span>
                  <ArrowRight className="size-4 text-slate-400" />
                </Link>
              </li>
            ))}
          </ul>
        )}
      </section>
    </div>
  );
}
