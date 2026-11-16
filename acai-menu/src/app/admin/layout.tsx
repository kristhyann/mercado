import type { Metadata } from "next";

export const metadata: Metadata = {
  title: { default: "Painel — Açaí Menu", template: "%s · Painel Açaí Menu" },
  robots: { index: false, follow: false, nocache: true },
};
export const dynamic = "force-dynamic";

export default function AdminRoot({ children }: { children: React.ReactNode }) {
  return <div className="min-h-dvh bg-slate-100 text-slate-900">{children}</div>;
}
