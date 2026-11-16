import { notFound } from "next/navigation";
import { getStore } from "@/lib/data";
import { brandStyle } from "@/lib/theme";
import { StoreProvider } from "@/components/store/StoreProvider";
import { DemoRibbon } from "@/components/store/DemoRibbon";

// Cardápios são gerados sob demanda e mantidos em cache por 60 s (ISR).
// O script de cadastro também pede revalidação imediata após cada alteração.
export const revalidate = 60;
export const dynamicParams = true;
export async function generateStaticParams() {
  return [];
}

export default async function StoreLayout({ children, params }: { children: React.ReactNode; params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const menu = await getStore(slug);
  if (!menu) notFound();
  return (
    <div style={brandStyle(menu.branding.primaryColor, menu.branding.secondaryColor)} className="min-h-dvh">
      <StoreProvider menu={menu} serverNow={Date.now()}>
        {menu.isDemo && <DemoRibbon hasWhatsapp={Boolean(menu.contact.whatsapp)} />}
        {children}
      </StoreProvider>
    </div>
  );
}
