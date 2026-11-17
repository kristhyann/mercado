import type { Metadata, Viewport } from "next";
import { env } from "@/lib/env";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL(env.siteUrl),
  title: { default: "Açaí Menu — Seu açaí favorito a poucos cliques", template: "%s" },
  description: "Cardápio digital para açaiterias com pedidos direto no WhatsApp. Monte seu açaí, escolha os acompanhamentos e peça em poucos cliques.",
  applicationName: "Açaí Menu",
  formatDetection: { telephone: false },
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  viewportFit: "cover",
  themeColor: "#6b21a8",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}
