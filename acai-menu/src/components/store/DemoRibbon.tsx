export function DemoRibbon({ hasWhatsapp }: { hasWhatsapp: boolean }) {
  return (
    <div className="bg-ink px-4 py-2 text-center text-xs font-semibold text-white">
      🧪 Loja de DEMONSTRAÇÃO — produtos, preços e endereço fictícios.
      {hasWhatsapp ? " Pedidos vão para o WhatsApp da plataforma Açaí Menu." : " Envio pelo WhatsApp desativado nesta demonstração."}
    </div>
  );
}
