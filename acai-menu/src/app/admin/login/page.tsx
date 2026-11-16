import { redirect } from "next/navigation";
import { getAdminSession } from "@/lib/admin/auth";
import { adminMode } from "@/lib/admin/mode";
import { LoginForm } from "@/components/admin/LoginForm";

export const metadata = { title: "Entrar" };

export default async function LoginPage() {
  const mode = adminMode();
  if (mode !== "disabled" && (await getAdminSession())) redirect("/admin");
  return (
    <main className="flex min-h-dvh items-center justify-center px-4 py-10">
      <div className="w-full max-w-sm">
        <div className="mb-6 text-center">
          <span className="mx-auto flex size-14 items-center justify-center rounded-2xl bg-violet-700 text-2xl shadow-lg">🍇</span>
          <h1 className="mt-4 text-2xl font-extrabold tracking-tight">
            AÇAÍ <span className="text-violet-600">MENU</span>
          </h1>
          <p className="text-sm text-slate-500">Painel do administrador da plataforma</p>
        </div>
        {mode === "disabled" ? (
          <div className="rounded-2xl bg-white p-5 text-sm text-slate-600 shadow-sm ring-1 ring-slate-200">
            <p className="font-bold text-slate-900">Painel não configurado</p>
            <p className="mt-2">Configure <code>SUPABASE_URL</code> e <code>SUPABASE_ANON_KEY</code> e rode as migrações do Supabase (veja o README, seção “Painel administrativo”).</p>
          </div>
        ) : (
          <LoginForm mode={mode} />
        )}
      </div>
    </main>
  );
}
