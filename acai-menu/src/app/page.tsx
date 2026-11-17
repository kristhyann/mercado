import Link from "next/link";
import { ArrowRight, Bike, Palette, ShoppingCart, Smartphone, Sparkles, Store } from "lucide-react";
import { listShowcaseStores } from "@/lib/data";
import { env } from "@/lib/env";
import { whatsappUrl } from "@/lib/order";
import { Img } from "@/components/ui/Img";
import { WhatsAppIcon } from "@/components/ui/icons";

export const revalidate = 300;

const FEATURES = [
  { icon: Sparkles, title: "Monte seu açaí", text: "Tamanhos, base, acompanhamentos grátis e pagos, cremes e coberturas, com preço atualizado em tempo real." },
  { icon: ShoppingCart, title: "Carrinho completo", text: "Editar, duplicar quantidades, observações por item e carrinho salvo mesmo se a página for atualizada." },
  { icon: WhatsAppIcon, title: "Pedido no WhatsApp", text: "Mensagem organizada com itens, endereço, pagamento e troco, pronta para a loja confirmar." },
  { icon: Bike, title: "Entrega e retirada", text: "Taxa fixa, por bairro ou grátis, pedido mínimo e entrega grátis a partir de um valor." },
  { icon: Palette, title: "Identidade própria", text: "Logo, capa, cores, banner e link exclusivo. Cada loja parece ter o próprio aplicativo." },
  { icon: Store, title: "Horários inteligentes", text: "Aberto/fechado automático, feriados, pausa de pedidos e agendamento quando a loja está fechada." },
];

export default async function Home() {
  const demos = await listShowcaseStores();
  const wa = env.platformWhatsapp;
  return (
    <div className="min-h-dvh bg-white">
      <header className="mx-auto flex max-w-6xl items-center justify-between px-4 py-5">
        <Link href="/" className="flex items-center gap-2.5">
          <span className="flex size-10 items-center justify-center rounded-2xl bg-[#6b21a8] text-xl shadow-card">🍇</span>
          <span className="text-xl font-extrabold tracking-tight text-[#3b0764]">
            AÇAÍ <span className="text-[#a855f7]">MENU</span>
          </span>
        </Link>
        {wa && (
          <a href={whatsappUrl(wa, "Olá! Quero um cardápio digital Açaí Menu para minha açaiteria.")} target="_blank" rel="noopener noreferrer" className="hidden h-11 items-center gap-2 rounded-full bg-[#3b0764] px-5 text-sm font-bold text-white sm:flex">
            <WhatsAppIcon className="size-4" /> Quero para minha loja
          </a>
        )}
      </header>

      <section className="relative overflow-hidden">
        <div className="absolute inset-0 -z-10 bg-[radial-gradient(circle_at_80%_20%,#f3e8ff,transparent_45%),radial-gradient(circle_at_10%_80%,#fef3c7,transparent_40%)]" />
        <div className="mx-auto grid max-w-6xl items-center gap-10 px-4 pb-16 pt-8 md:grid-cols-2 md:pt-16">
          <div>
            <span className="inline-flex items-center gap-2 rounded-full bg-[#f3e8ff] px-3 py-1 text-sm font-bold text-[#6b21a8]">
              <Smartphone className="size-4" /> Cardápio digital para açaiterias
            </span>
            <h1 className="mt-4 text-4xl font-extrabold leading-[1.05] tracking-tight text-[#1c1022] sm:text-6xl">
              Seu açaí favorito <span className="text-[#7e22ce]">a poucos cliques.</span>
            </h1>
            <p className="mt-5 max-w-lg text-lg leading-relaxed text-muted">
              Cardápio com link exclusivo, montagem de açaí, carrinho e pedidos organizados direto no WhatsApp da sua loja. Sem app, sem complicação.
            </p>
            <div className="mt-8 flex flex-wrap gap-3">
              {demos[0] && (
                <Link href={`/${demos[0].slug}`} className="flex h-14 items-center gap-2 rounded-2xl bg-[#6b21a8] px-6 text-[16px] font-extrabold text-white shadow-float transition hover:bg-[#581c87]">
                  Ver cardápio de exemplo <ArrowRight className="size-5" />
                </Link>
              )}
              {wa && (
                <a href={whatsappUrl(wa, "Olá! Quero um cardápio digital Açaí Menu para minha açaiteria.")} target="_blank" rel="noopener noreferrer" className="flex h-14 items-center gap-2 rounded-2xl bg-[#25D366] px-6 text-[16px] font-extrabold text-white">
                  <WhatsAppIcon /> Falar com a gente
                </a>
              )}
            </div>
          </div>
          <div className="relative mx-auto w-full max-w-sm">
            <div className="rounded-[44px] border-[10px] border-[#1c1022] bg-[#faf8fc] p-3 shadow-float">
              <div className="rounded-3xl bg-gradient-to-br from-[#6b21a8] to-[#3b0764] p-5 text-white">
                <p className="text-sm font-semibold opacity-80">MONTE SEU AÇAÍ!</p>
                <p className="mt-1 text-2xl font-extrabold">500 ml · R$ 18,00</p>
              </div>
              {["Açaí tradicional", "Banana", "Leite em pó", "Granola"].map((t, i) => (
                <div key={t} className="mt-2 flex items-center justify-between rounded-2xl bg-white px-4 py-3 text-sm font-semibold shadow-card">
                  <span>{t}</span>
                  <span className="text-xs font-bold text-emerald-600">{i === 0 ? "Base" : "Grátis"}</span>
                </div>
              ))}
              <div className="mt-2 flex items-center justify-between rounded-2xl bg-white px-4 py-3 text-sm font-semibold shadow-card">
                <span>Nutella extra</span>
                <span className="text-xs font-bold">+R$ 3,00</span>
              </div>
              <div className="mt-3 flex h-14 items-center justify-between rounded-2xl bg-[#25D366] px-5 font-extrabold text-white">
                <span>Enviar pedido</span>
                <span>R$ 21,00</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="bg-[#faf8fc] py-16">
        <div className="mx-auto max-w-6xl px-4">
          <h2 className="text-center text-3xl font-extrabold tracking-tight">Tudo que uma açaiteria precisa para vender online</h2>
          <div className="mt-10 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {FEATURES.map((f) => (
              <div key={f.title} className="rounded-3xl bg-white p-6 shadow-card">
                <span className="flex size-12 items-center justify-center rounded-2xl bg-[#f3e8ff] text-[#6b21a8]">
                  <f.icon className="size-6" />
                </span>
                <h3 className="mt-4 text-lg font-extrabold">{f.title}</h3>
                <p className="mt-1.5 leading-relaxed text-muted">{f.text}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {demos.length > 0 && (
        <section className="py-16">
          <div className="mx-auto max-w-6xl px-4">
            <h2 className="text-3xl font-extrabold tracking-tight">Cardápios de demonstração</h2>
            <p className="mt-2 text-muted">Lojas fictícias para você testar o fluxo completo de pedido.</p>
            <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {demos.map((s) => (
                <Link key={s.slug} href={`/${s.slug}`} className="group flex items-center gap-4 rounded-3xl bg-white p-4 shadow-card ring-1 ring-line transition hover:-translate-y-0.5">
                  <span className="relative size-16 shrink-0 overflow-hidden rounded-2xl" style={{ background: s.primaryColor }}>
                    {s.logo && <Img src={s.logo} alt="" fill sizes="64px" className="object-cover" />}
                  </span>
                  <span className="min-w-0 flex-1">
                    <span className="block truncate text-lg font-extrabold">{s.name}</span>
                    <span className="block truncate text-sm text-muted">/{s.slug}</span>
                  </span>
                  <ArrowRight className="size-5 text-muted transition group-hover:translate-x-1" />
                </Link>
              ))}
            </div>
          </div>
        </section>
      )}

      <footer className="border-t border-line py-8 text-center text-sm text-muted">
        <p>
          <b className="text-[#3b0764]">AÇAÍ MENU</b> · Seu açaí favorito a poucos cliques.
        </p>
      </footer>
    </div>
  );
}
