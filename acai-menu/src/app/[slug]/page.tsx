import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { getStore } from "@/lib/data";
import { StoreHeader } from "@/components/store/StoreHeader";
import { Banner, MenuBody } from "@/components/store/MenuBody";
import { ProductSheet } from "@/components/store/ProductSheet";
import { BackToTop, CartButton, CartSheet } from "@/components/store/CartSheet";

export const revalidate = 60;

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const menu = await getStore(slug);
  if (!menu) return { title: "Cardápio não encontrado" };
  const title = menu.seo.title ?? `${menu.name} — Cardápio digital`;
  const description = menu.seo.description ?? menu.description ?? `Peça na ${menu.name} pelo WhatsApp: monte seu açaí do seu jeito.`;
  const images = menu.seo.image ? [{ url: menu.seo.image, width: 1200, height: 630, alt: menu.name }] : undefined; // senão usa opengraph-image.tsx
  return {
    title,
    description,
    alternates: { canonical: `/${menu.slug}` },
    openGraph: { type: "website", locale: "pt_BR", url: `/${menu.slug}`, siteName: menu.name, title, description, ...(images ? { images } : {}) },
    twitter: { card: "summary_large_image", title, description, ...(images ? { images: images.map((i) => i.url) } : {}) },
    icons: menu.branding.logo ? { icon: menu.branding.logo, apple: menu.branding.logo } : undefined,
    robots: menu.isDemo ? { index: false, follow: true } : undefined,
    other: { "theme-color": menu.branding.primaryColor },
  };
}

export default async function StorePage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const menu = await getStore(slug);
  if (!menu) notFound();
  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "Restaurant",
    name: menu.name,
    description: menu.description ?? undefined,
    servesCuisine: "Açaí",
    address: menu.contact.address ?? undefined,
    image: menu.branding.logo ?? undefined,
  };
  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd).replace(/</g, "\\u003c") }} />
      <StoreHeader />
      <Banner />
      <MenuBody />
      <ProductSheet />
      <CartSheet />
      <CartButton />
      <BackToTop />
    </>
  );
}
