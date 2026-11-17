import { backend } from "@/lib/admin/backend";
import { NewStoreForm } from "@/components/admin/NewStoreForm";

export const metadata = { title: "Nova loja" };

export default async function NewStorePage() {
  const stores = await backend().listStores();
  return <NewStoreForm stores={stores.map((s) => ({ slug: s.slug, name: s.name }))} />;
}
