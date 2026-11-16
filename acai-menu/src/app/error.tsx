"use client";

export default function Error({ reset }: { error: Error; reset: () => void }) {
  return (
    <main className="flex min-h-dvh flex-col items-center justify-center px-6 text-center">
      <p className="text-6xl">😕</p>
      <h1 className="mt-4 text-2xl font-extrabold">Não foi possível carregar o cardápio</h1>
      <p className="mt-2 max-w-sm text-muted">Verifique sua conexão e tente novamente.</p>
      <button onClick={reset} className="mt-6 h-12 rounded-2xl bg-[#6b21a8] px-6 font-bold text-white">
        Tentar novamente
      </button>
    </main>
  );
}
