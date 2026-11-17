import Link from "next/link";

export default function NotFound() {
  return (
    <main className="flex min-h-dvh flex-col items-center justify-center px-6 text-center">
      <p className="text-6xl">🍇</p>
      <h1 className="mt-4 text-2xl font-extrabold">Cardápio não encontrado</h1>
      <p className="mt-2 max-w-sm text-muted">Confira se o endereço está correto. Este cardápio pode ter mudado de endereço ou estar temporariamente indisponível.</p>
      <Link href="/" className="mt-6 inline-flex h-12 items-center rounded-2xl bg-[#6b21a8] px-6 font-bold text-white">
        Ir para o início
      </Link>
    </main>
  );
}
