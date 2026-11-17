"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { LayoutDashboard, LogOut, Plus, Store } from "lucide-react";
import { logoutAction } from "@/app/admin/actions";
import { cx } from "./ui";

const NAV = [
  { href: "/admin", label: "Painel", icon: LayoutDashboard, exact: true },
  { href: "/admin/lojas", label: "Lojas", icon: Store, exact: false },
  { href: "/admin/lojas/nova", label: "Nova loja", icon: Plus, exact: true },
];

export function AdminShell({ email, mode, children }: { email: string; mode: "supabase" | "local" | "preview"; children: React.ReactNode }) {
  const path = usePathname();
  const active = (n: (typeof NAV)[number]) => (n.exact ? path === n.href : path.startsWith(n.href) && path !== "/admin/lojas/nova");
  return (
    <div className="lg:flex">
      <aside className="sticky top-0 hidden h-dvh w-60 shrink-0 flex-col border-r border-slate-200 bg-white p-4 lg:flex">
        <Link href="/admin" className="flex items-center gap-2 px-2 py-1">
          <span className="flex size-9 items-center justify-center rounded-xl bg-violet-700 text-lg">🍇</span>
          <span className="font-extrabold tracking-tight">AÇAÍ <span className="text-violet-600">MENU</span></span>
        </Link>
        <nav className="mt-6 space-y-1">
          {NAV.map((n) => (
            <Link key={n.href} href={n.href} className={cx("flex h-11 items-center gap-3 rounded-xl px-3 text-sm font-semibold", active(n) ? "bg-violet-50 text-violet-700" : "text-slate-600 hover:bg-slate-50")}>
              <n.icon className="size-5" /> {n.label}
            </Link>
          ))}
        </nav>
        <div className="mt-auto border-t border-slate-100 pt-4">
          <p className="truncate px-2 text-xs text-slate-500">{email}</p>
          <form action={logoutAction}>
            <button className="mt-2 flex h-10 w-full items-center gap-2 rounded-xl px-3 text-sm font-semibold text-slate-600 hover:bg-slate-50">
              <LogOut className="size-4" /> Sair
            </button>
          </form>
        </div>
      </aside>

      <header className="sticky top-0 z-30 flex h-14 items-center justify-between border-b border-slate-200 bg-white/95 px-3 backdrop-blur lg:hidden">
        <Link href="/admin" className="flex items-center gap-2">
          <span className="flex size-8 items-center justify-center rounded-lg bg-violet-700">🍇</span>
          <span className="text-sm font-extrabold">AÇAÍ <span className="text-violet-600">MENU</span></span>
        </Link>
        <form action={logoutAction}>
          <button className="flex h-10 items-center gap-1.5 rounded-lg px-3 text-sm font-semibold text-slate-600" aria-label="Sair">
            <LogOut className="size-4" /> Sair
          </button>
        </form>
      </header>

      <div className="min-w-0 flex-1 pb-24 lg:pb-10">
        {mode === "preview" && (
          <div className="bg-sky-100 px-4 py-2 text-center text-xs font-semibold text-sky-900">
            👀 Modo visualização: explore à vontade, mas nenhuma alteração é salva. Para editar de verdade, configure o Supabase.
          </div>
        )}
        {mode === "local" && <div className="bg-amber-100 px-4 py-2 text-center text-xs font-semibold text-amber-900">Modo local (desenvolvimento): as alterações são gravadas nos arquivos da pasta stores/.</div>}
        <div className="mx-auto max-w-6xl px-3 py-5 sm:px-6">{children}</div>
      </div>

      <nav className="fixed inset-x-0 bottom-0 z-30 grid grid-cols-3 border-t border-slate-200 bg-white lg:hidden" style={{ paddingBottom: "env(safe-area-inset-bottom)" }}>
        {NAV.map((n) => (
          <Link key={n.href} href={n.href} className={cx("flex h-14 flex-col items-center justify-center gap-0.5 text-[11px] font-bold", active(n) ? "text-violet-700" : "text-slate-500")}>
            <n.icon className="size-5" /> {n.label}
          </Link>
        ))}
      </nav>
    </div>
  );
}
