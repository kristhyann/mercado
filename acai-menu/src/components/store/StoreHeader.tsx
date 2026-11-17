"use client";
import { useState } from "react";
import { Bike, Clock, MapPin, Share2, ShoppingBag, Store, X } from "lucide-react";
import { useStore } from "./StoreProvider";
import { Img } from "@/components/ui/Img";
import { InstagramIcon, WhatsAppIcon } from "@/components/ui/icons";
import { weeklySummary } from "@/lib/hours";
import { formatBRL } from "@/lib/format";
import { whatsappUrl } from "@/lib/order";
import { useBackToClose, useLockBody } from "@/lib/hooks";

export function StatusPill({ compact = false }: { compact?: boolean }) {
  const { status } = useStore();
  const tone = status.paused ? "bg-amber-100 text-amber-800" : status.isOpen ? "bg-emerald-100 text-emerald-800" : "bg-rose-100 text-rose-700";
  const dot = status.paused ? "bg-amber-500" : status.isOpen ? "bg-emerald-500" : "bg-rose-500";
  return (
    <span className={`inline-flex items-center gap-1.5 rounded-full px-2.5 py-1 text-xs font-bold ${tone}`}>
      <span className={`relative flex size-2`}>
        {status.isOpen && !status.paused && <span className={`absolute inline-flex size-full animate-ping rounded-full ${dot} opacity-60`} />}
        <span className={`relative inline-flex size-2 rounded-full ${dot}`} />
      </span>
      {status.isOpen && !status.paused ? "ABERTO" : status.paused ? "PAUSADO" : "FECHADO"}
      {!compact && status.detail && !status.paused && <span className="font-medium opacity-80">· {status.detail}</span>}
    </span>
  );
}

export function StoreHeader() {
  const { menu, status } = useStore();
  const [hoursOpen, setHoursOpen] = useState(false);
  const [copied, setCopied] = useState(false);
  const wa = menu.contact.whatsapp;

  async function share() {
    const url = window.location.href.split("#")[0].split("?")[0];
    const data = { title: menu.name, text: `Confira o cardápio da ${menu.name}!`, url };
    try {
      if (navigator.share) {
        await navigator.share(data);
        return;
      }
    } catch (e) {
      if ((e as DOMException).name === "AbortError") return;
    }
    try {
      await navigator.clipboard.writeText(url);
    } catch {
      const ta = document.createElement("textarea");
      ta.value = url;
      document.body.appendChild(ta);
      ta.select();
      document.execCommand("copy");
      ta.remove();
    }
    setCopied(true);
    setTimeout(() => setCopied(false), 2200);
  }

  return (
    <header className="relative">
      <div className="relative h-44 w-full overflow-hidden bg-brand sm:h-64">
        {menu.branding.cover && (
          <Img src={menu.branding.cover} alt="" fill priority sizes="100vw" className="object-cover" />
        )}
        <div className="absolute inset-0 bg-gradient-to-t from-black/45 via-black/5 to-black/10" />
        <div className="absolute right-3 top-3 flex gap-2" style={{ paddingTop: "env(safe-area-inset-top)" }}>
          <button onClick={share} className="flex h-10 items-center gap-2 rounded-full bg-white/90 px-4 text-sm font-semibold text-ink shadow-card backdrop-blur transition active:scale-95" aria-label="Compartilhar cardápio">
            <Share2 className="size-4" /> {copied ? "Link copiado!" : "Compartilhar"}
          </button>
        </div>
      </div>

      <div className="mx-auto max-w-5xl px-4">
        <div className="relative -mt-14 rounded-3xl bg-white p-4 shadow-card sm:-mt-20 sm:p-6">
          <div className="flex items-start gap-4">
            <div className="relative -mt-12 size-24 shrink-0 overflow-hidden rounded-3xl border-4 border-white bg-brand-soft shadow-card sm:-mt-16 sm:size-32">
              {menu.branding.logo ? (
                <Img src={menu.branding.logo} alt={`Logo ${menu.name}`} fill sizes="128px" className="object-cover" priority />
              ) : (
                <div className="flex size-full items-center justify-center text-3xl font-extrabold text-brand">{menu.name[0]}</div>
              )}
            </div>
            <div className="min-w-0 flex-1">
              <h1 className="text-2xl font-extrabold leading-tight tracking-tight text-ink sm:text-3xl">{menu.name}</h1>
              <div className="mt-1.5">
                <StatusPill />
              </div>
            </div>
          </div>

          {menu.description && <p className="mt-3 text-[15px] leading-relaxed text-muted">{menu.description}</p>}

          <ul className="mt-4 grid gap-2 text-sm text-ink/80 sm:grid-cols-2">
            {(menu.contact.region || menu.contact.address) && (
              <li className="flex items-start gap-2">
                <MapPin className="mt-0.5 size-4 shrink-0 text-brand" />
                <span>
                  {menu.contact.region ?? menu.contact.address}
                  {menu.contact.mapsUrl && (
                    <a href={menu.contact.mapsUrl} target="_blank" rel="noopener noreferrer" className="ml-1 font-semibold text-brand underline-offset-2 hover:underline">
                      Ver no mapa
                    </a>
                  )}
                </span>
              </li>
            )}
            <li>
              <button onClick={() => setHoursOpen(true)} className="flex items-center gap-2 text-left font-medium hover:text-brand">
                <Clock className="size-4 shrink-0 text-brand" />
                <span>
                  Horário de funcionamento <span className="font-semibold text-brand underline underline-offset-2">ver</span>
                </span>
              </button>
            </li>
            {menu.ordering.delivery && (
              <li className="flex items-center gap-2">
                <Bike className="size-4 shrink-0 text-brand" />
                <span>
                  Entrega{menu.ordering.deliveryTime ? ` · ${menu.ordering.deliveryTime}` : ""}
                  {menu.delivery.mode === "free" && <b className="ml-1 text-success">· Grátis</b>}
                  {menu.delivery.mode === "fixed" && <span> · {menu.delivery.fixedFee ? formatBRL(menu.delivery.fixedFee) : "Grátis"}</span>}
                  {menu.delivery.mode === "zones" && <span> · taxa por bairro</span>}
                  {menu.delivery.freeAbove !== null && menu.delivery.mode !== "free" && <span className="text-success"> · grátis acima de {formatBRL(menu.delivery.freeAbove)}</span>}
                </span>
              </li>
            )}
            {menu.ordering.pickup && (
              <li className="flex items-center gap-2">
                <Store className="size-4 shrink-0 text-brand" />
                <span>Retirada no local{menu.ordering.pickupTime ? ` · ${menu.ordering.pickupTime}` : ""}</span>
              </li>
            )}
            {menu.ordering.minOrder > 0 && (
              <li className="flex items-center gap-2">
                <ShoppingBag className="size-4 shrink-0 text-brand" />
                <span>Pedido mínimo {formatBRL(menu.ordering.minOrder)}</span>
              </li>
            )}
          </ul>

          <div className="mt-4 flex flex-wrap gap-2">
            {wa ? (
              <a
                href={whatsappUrl(wa, `Olá, ${menu.name}! Vim pelo cardápio digital.`)}
                target="_blank"
                rel="noopener noreferrer"
                className="flex h-12 flex-1 items-center justify-center gap-2 rounded-2xl bg-[#25D366] px-5 text-[15px] font-bold text-white shadow-card transition hover:brightness-95 active:scale-[0.98] sm:flex-none"
              >
                <WhatsAppIcon /> Falar no WhatsApp
              </a>
            ) : null}
            {menu.contact.instagram && (
              <a
                href={`https://instagram.com/${menu.contact.instagram.replace(/^@/, "")}`}
                target="_blank"
                rel="noopener noreferrer"
                className="flex h-12 items-center justify-center gap-2 rounded-2xl border border-line bg-white px-5 text-[15px] font-bold text-ink transition hover:bg-brand-softer active:scale-[0.98]"
              >
                <InstagramIcon /> Instagram
              </a>
            )}
          </div>

          {!status.isOpen && !status.paused && (
            <div className="mt-4 rounded-2xl bg-rose-50 p-4 text-sm text-rose-800">
              <p className="font-bold">Estamos fechados no momento. Confira nosso horário de funcionamento.</p>
              {status.detail && <p className="mt-0.5">{status.detail}.</p>}
              {status.mustSchedule && <p className="mt-1 font-semibold">Você já pode fazer seu pedido e agendar o horário. 🗓️</p>}
            </div>
          )}
          {status.paused && (
            <div className="mt-4 rounded-2xl bg-amber-50 p-4 text-sm font-semibold text-amber-900">{status.detail}</div>
          )}
        </div>
      </div>

      <HoursDialog open={hoursOpen} onClose={() => setHoursOpen(false)} />
    </header>
  );
}

function HoursDialog({ open, onClose }: { open: boolean; onClose: () => void }) {
  const { menu, now } = useStore();
  useBackToClose(open, onClose);
  useLockBody(open);
  if (!open) return null;
  const today = new Intl.DateTimeFormat("en-US", { timeZone: menu.hours.timezone, weekday: "short" }).format(now);
  const todayIdx = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].indexOf(today);
  const upcoming = menu.hours.special.filter((s) => s.date >= now.toISOString().slice(0, 10)).slice(0, 4);
  return (
    <div className="fixed inset-0 z-[60] flex items-end justify-center sm:items-center" role="dialog" aria-modal="true" aria-label="Horário de funcionamento">
      <button className="animate-fade-in absolute inset-0 bg-black/50" onClick={onClose} aria-label="Fechar" />
      <div className="animate-sheet-up pb-safe relative w-full max-w-md rounded-t-3xl bg-white p-6 sm:rounded-3xl">
        <div className="flex items-center justify-between">
          <h2 className="text-lg font-extrabold">Horário de funcionamento</h2>
          <button onClick={onClose} className="flex size-10 items-center justify-center rounded-full bg-canvas" aria-label="Fechar">
            <X className="size-5" />
          </button>
        </div>
        <ul className="mt-4 divide-y divide-line">
          {weeklySummary(menu.hours).map((d) => (
            <li key={d.day} className={`flex justify-between py-2.5 text-[15px] ${d.weekday === todayIdx ? "font-bold text-brand" : ""}`}>
              <span>{d.day}{d.weekday === todayIdx ? " (hoje)" : ""}</span>
              <span className={d.text === "Fechado" ? "text-muted" : ""}>{d.text}</span>
            </li>
          ))}
        </ul>
        {upcoming.length > 0 && (
          <div className="mt-4 rounded-2xl bg-brand-softer p-3 text-sm">
            <p className="font-bold text-brand">Horários especiais</p>
            {upcoming.map((s) => (
              <p key={s.date} className="mt-1">
                {s.date.split("-").reverse().join("/")} {s.label ? `(${s.label})` : ""}: {s.closed ? "fechado" : s.intervals.map((i) => `${i.open} às ${i.close}`).join(" · ")}
              </p>
            ))}
          </div>
        )}
        {menu.contact.address && <p className="mt-4 text-sm text-muted">📍 {menu.contact.address}</p>}
      </div>
    </div>
  );
}
