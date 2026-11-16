"use client";
import { useActionState } from "react";
import { Loader2, Lock } from "lucide-react";
import { loginAction } from "@/app/admin/actions";
import { inputCls } from "./ui";

export function LoginForm({ mode }: { mode: "supabase" | "local" }) {
  const [state, action, pending] = useActionState(loginAction, { error: null });
  return (
    <form action={action} className="space-y-4 rounded-2xl bg-white p-5 shadow-sm ring-1 ring-slate-200">
      {mode === "local" && (
        <p className="rounded-xl bg-amber-50 p-3 text-xs text-amber-900">Modo de desenvolvimento local: edita os arquivos da pasta <code>stores/</code>.</p>
      )}
      {mode === "supabase" && (
        <label className="block">
          <span className="mb-1 block text-sm font-semibold">E-mail</span>
          <input name="email" type="email" autoComplete="username" required className={inputCls} />
        </label>
      )}
      <label className="block">
        <span className="mb-1 block text-sm font-semibold">Senha</span>
        <input name="password" type="password" autoComplete="current-password" required className={inputCls} />
      </label>
      {state.error && <p className="rounded-xl bg-rose-50 p-3 text-sm font-semibold text-rose-700" role="alert">{state.error}</p>}
      <button disabled={pending} className="flex h-12 w-full items-center justify-center gap-2 rounded-xl bg-violet-700 font-bold text-white hover:bg-violet-800 disabled:opacity-60">
        {pending ? <Loader2 className="size-4 animate-spin" /> : <Lock className="size-4" />} Entrar
      </button>
    </form>
  );
}
