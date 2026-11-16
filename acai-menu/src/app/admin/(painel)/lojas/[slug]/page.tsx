import { notFound } from "next/navigation";
import { backend } from "@/lib/admin/backend";
import { storeConfigSchema } from "@/lib/schema";
import { env } from "@/lib/env";
import { StoreEditor } from "@/components/admin/editor/StoreEditor";

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  return { title: `Editar ${(await params).slug}` };
}

export default async function EditStorePage({ params, searchParams }: { params: Promise<{ slug: string }>; searchParams: Promise<{ nova?: string }> }) {
  const { slug } = await params;
  const { nova } = await searchParams;
  const doc = await backend().getStore(slug);
  if (!doc) notFound();
  const parsed = storeConfigSchema.safeParse(doc.config);
  if (!parsed.success) {
    return (
      <div className="rounded-2xl bg-white p-6 ring-1 ring-rose-200">
        <h1 className="text-lg font-extrabold text-rose-700">Não foi possível abrir esta loja</h1>
        <p className="mt-1 text-sm text-slate-600">Os dados salvos estão em um formato inválido:</p>
        <ul className="mt-3 list-disc pl-5 text-sm text-slate-700">
          {parsed.error.issues.slice(0, 20).map((i, n) => <li key={n}>{i.path.join(".")}: {i.message}</li>)}
        </ul>
      </div>
    );
  }
  return <StoreEditor initial={parsed.data} updatedAt={doc.updatedAt} siteUrl={env.siteUrl} isNew={nova === "1"} />;
}
