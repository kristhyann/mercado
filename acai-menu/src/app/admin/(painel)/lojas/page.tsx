import { backend } from "@/lib/admin/backend";
import { StoresList } from "@/components/admin/StoresList";
import { env } from "@/lib/env";

export const metadata = { title: "Lojas" };

export default async function StoresPage() {
  const stores = await backend().listStores();
  return <StoresList stores={stores} siteUrl={env.siteUrl} />;
}
