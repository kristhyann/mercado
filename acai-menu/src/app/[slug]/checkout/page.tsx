import type { Metadata } from "next";
import { Checkout } from "@/components/store/Checkout";
import { getStore } from "@/lib/data";

export const revalidate = 60;

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const menu = await getStore(slug);
  return { title: menu ? `Finalizar pedido — ${menu.name}` : "Finalizar pedido", robots: { index: false, follow: false } };
}

export default function CheckoutPage() {
  return <Checkout />;
}
