"use client";
import { useEffect, useMemo, useRef, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { ArrowLeft, Banknote, Bike, CalendarClock, Check, ClipboardCopy, CreditCard, Loader2, MapPin, QrCode, Store, User } from "lucide-react";
import { useStore } from "./StoreProvider";
import { LineDetails, lineTitle } from "./CartSheet";
import { WhatsAppIcon } from "@/components/ui/icons";
import { formatBRL, maskCEP, maskPhone, normalizeText, onlyDigits, parseBRL } from "@/lib/format";
import {
  buildOrderMessage, computeTotals, generateOrderCode, quoteDelivery, validateCustomer, whatsappUrl,
  PAYMENT_LABELS, UNLISTED_NEIGHBORHOOD, type CustomerInfo, type OrderType,
} from "@/lib/order";
import { scheduleSlots } from "@/lib/hours";
import { loadCustomer, saveCustomer } from "@/lib/customer-store";
import type { PaymentMethod } from "@/lib/schema";

const PAY_ICON: Record<PaymentMethod, React.ReactNode> = {
  pix: <QrCode className="size-5" />,
  cash: <Banknote className="size-5" />,
  credit: <CreditCard className="size-5" />,
  debit: <CreditCard className="size-5" />,
};

const emptyAddress = { cep: "", street: "", number: "", neighborhood: "", complement: "", reference: "" };

export function Checkout() {
  const { menu, evaluation, hydrated, status, now, cart } = useStore();
  const router = useRouter();
  const defaultType: OrderType = menu.ordering.delivery ? "delivery" : "pickup";
  const [c, setC] = useState<CustomerInfo>({
    name: "", phone: "", type: defaultType, address: emptyAddress, payment: menu.ordering.paymentMethods[0],
    needsChange: false, changeFor: null, notes: "", scheduledFor: null,
  });
  const [zoneChoice, setZoneChoice] = useState("");
  const [changeText, setChangeText] = useState("");
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [step, setStep] = useState<"form" | "review" | "sent">("form");
  const [orderCode, setOrderCode] = useState("");
  const [cepState, setCepState] = useState<"idle" | "loading" | "error" | "ok">("idle");
  const [copied, setCopied] = useState(false);
  const formRef = useRef<HTMLFormElement>(null);

  // Restaura dados salvos do cliente (neste aparelho).
  useEffect(() => {
    const saved = loadCustomer();
    setC((prev) => ({
      ...prev,
      name: saved.name ?? "",
      phone: saved.phone ?? "",
      type: saved.type && (saved.type === "delivery" ? menu.ordering.delivery : menu.ordering.pickup) ? saved.type : prev.type,
      address: { ...emptyAddress, ...(saved.address ?? {}) },
      payment: saved.payment && menu.ordering.paymentMethods.includes(saved.payment) ? saved.payment : prev.payment,
    }));
    if (menu.delivery.mode === "zones" && saved.address?.neighborhood) {
      const z = menu.delivery.zones.find((z) => normalizeText(z.neighborhood) === normalizeText(saved.address!.neighborhood));
      if (z) setZoneChoice(z.neighborhood);
    }
  }, [menu]);

  const zonesMode = menu.delivery.mode === "zones";
  const neighborhoodForQuote = zonesMode ? zoneChoice : c.address.neighborhood;
  const quote = quoteDelivery(menu, c.type, neighborhoodForQuote, evaluation.subtotal);
  const totals = computeTotals(evaluation.subtotal, quote);
  const slots = useMemo(() => (status.mustSchedule ? scheduleSlots(menu.hours, now) : []), [status.mustSchedule, menu.hours, now]);
  const belowMin = menu.ordering.minOrder > 0 && evaluation.subtotal < menu.ordering.minOrder;
  const message = useMemo(
    () => (orderCode ? buildOrderMessage({ menu, lines: evaluation.lines, customer: c, totals, orderCode }) : ""),
    [orderCode, menu, evaluation.lines, c, totals],
  );
  const waLink = menu.contact.whatsapp && message ? whatsappUrl(menu.contact.whatsapp, message) : null;

  const set = <K extends keyof CustomerInfo>(k: K, v: CustomerInfo[K]) => setC((p) => ({ ...p, [k]: v }));
  const setAddr = (k: keyof CustomerInfo["address"], v: string) => setC((p) => ({ ...p, address: { ...p.address, [k]: v } }));

  async function lookupCep(cep: string) {
    const d = onlyDigits(cep);
    if (d.length !== 8) return;
    setCepState("loading");
    try {
      const ctrl = new AbortController();
      const t = setTimeout(() => ctrl.abort(), 6000);
      const res = await fetch(`https://viacep.com.br/ws/${d}/json/`, { signal: ctrl.signal });
      clearTimeout(t);
      const data = await res.json();
      if (data.erro) throw new Error("CEP não encontrado");
      setC((p) => ({
        ...p,
        address: {
          ...p.address,
          street: data.logradouro || p.address.street,
          neighborhood: data.bairro || p.address.neighborhood,
        },
      }));
      if (zonesMode && data.bairro) {
        const z = menu.delivery.zones.find((z) => normalizeText(z.neighborhood) === normalizeText(data.bairro));
        setZoneChoice(z ? z.neighborhood : menu.delivery.allowUnlistedNeighborhoods ? UNLISTED_NEIGHBORHOOD : "");
        if (!z) setErrors((e) => ({ ...e, neighborhood: menu.delivery.allowUnlistedNeighborhoods ? "" : `Ainda não entregamos em ${data.bairro}. Escolha um bairro da lista ou retirada.` }));
      }
      setCepState("ok");
    } catch {
      setCepState("error");
    }
  }

  function review(e: React.FormEvent) {
    e.preventDefault();
    const customer: CustomerInfo = {
      ...c,
      address: zonesMode && zoneChoice && zoneChoice !== UNLISTED_NEIGHBORHOOD ? { ...c.address, neighborhood: zoneChoice } : c.address,
      changeFor: c.payment === "cash" && c.needsChange ? parseBRL(changeText) : null,
      scheduledFor: status.mustSchedule ? c.scheduledFor : null,
    };
    const errs = validateCustomer(menu, customer, quote, totals.total, status.mustSchedule);
    if (zonesMode && c.type === "delivery" && !zoneChoice) errs.neighborhood = "Selecione o bairro.";
    setErrors(errs);
    if (Object.keys(errs).length) {
      const first = Object.keys(errs)[0];
      requestAnimationFrame(() => formRef.current?.querySelector<HTMLElement>(`[data-field="${first}"]`)?.scrollIntoView({ behavior: "smooth", block: "center" }));
      return;
    }
    setC(customer);
    saveCustomer(customer);
    setOrderCode(generateOrderCode());
    setStep("review");
    window.scrollTo({ top: 0 });
  }

  async function copyMessage() {
    try {
      await navigator.clipboard.writeText(message);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      /* sem permissão: o texto fica visível para copiar manualmente */
    }
  }

  if (!hydrated) {
    return (
      <div className="flex min-h-dvh items-center justify-center">
        <Loader2 className="size-8 animate-spin text-brand" />
      </div>
    );
  }

  if (evaluation.lines.length === 0 && step !== "sent") {
    return (
      <Shell title="Finalizar pedido">
        <div className="py-20 text-center">
          <p className="text-5xl">🛒</p>
          <p className="mt-3 text-lg font-bold">Seu carrinho está vazio</p>
          <Link href={`/${menu.slug}`} className="mt-5 inline-flex h-12 items-center rounded-2xl bg-brand px-6 font-bold text-on-brand">
            Ver cardápio
          </Link>
        </div>
      </Shell>
    );
  }

  if (step === "sent") {
    return (
      <Shell title="Pedido no WhatsApp">
        <div className="mt-6 rounded-3xl bg-white p-6 text-center shadow-card">
          <div className="mx-auto flex size-16 items-center justify-center rounded-full bg-[#25D366]/15 text-[#128C7E]">
            <WhatsAppIcon className="size-9" />
          </div>
          <h2 className="mt-4 text-2xl font-extrabold">Quase lá!</h2>
          <p className="mt-2 text-[15px] leading-relaxed text-muted">
            Abrimos o WhatsApp da <b className="text-ink">{menu.name}</b> com o seu pedido nº <b className="text-ink">{orderCode}</b> já escrito.
          </p>
          <p className="mt-3 rounded-2xl bg-amber-50 p-3 text-[15px] font-semibold text-amber-900">
            Toque em <b>ENVIAR</b> no WhatsApp para concluir. O pedido só é confirmado quando a loja responder.
          </p>
          <div className="mt-5 grid gap-2">
            {waLink && (
              <a href={waLink} target="_blank" rel="noopener noreferrer" className="flex h-14 items-center justify-center gap-2 rounded-2xl bg-[#25D366] font-extrabold text-white">
                <WhatsAppIcon /> Abrir o WhatsApp novamente
              </a>
            )}
            <button
              onClick={() => {
                cart.clear();
                router.push(`/${menu.slug}`);
              }}
              className="h-14 rounded-2xl bg-brand font-extrabold text-on-brand"
            >
              Já enviei · Fazer novo pedido
            </button>
            <button onClick={() => setStep("review")} className="h-12 font-bold text-brand">
              Voltar e conferir o pedido
            </button>
          </div>
        </div>
      </Shell>
    );
  }

  if (step === "review") {
    return (
      <Shell title="Confira seu pedido" onBack={() => setStep("form")}>
        <p className="mt-4 text-[15px] text-muted">Esta é a mensagem que será enviada para a loja pelo WhatsApp:</p>
        <div className="mt-3 rounded-3xl bg-[#e7ddd4] p-3 shadow-inner">
          <div className="ml-auto max-w-[95%] whitespace-pre-wrap break-words rounded-2xl rounded-tr-sm bg-[#d9fdd3] p-4 font-[system-ui] text-[14px] leading-relaxed text-[#111b21] shadow-sm">
            {message.replace(/\*/g, "")}
          </div>
        </div>
        <button onClick={copyMessage} className="mt-2 flex h-11 items-center gap-2 px-1 text-sm font-bold text-brand">
          <ClipboardCopy className="size-4" /> {copied ? "Mensagem copiada!" : "Copiar mensagem"}
        </button>

        <div className="pb-safe sticky bottom-0 -mx-4 mt-4 border-t border-line bg-canvas/95 px-4 pt-3 backdrop-blur">
          {waLink ? (
            <a
              href={waLink}
              target="_blank"
              rel="noopener noreferrer"
              onClick={() => setTimeout(() => setStep("sent"), 400)}
              className="flex h-16 w-full items-center justify-center gap-3 rounded-2xl bg-[#25D366] text-[17px] font-extrabold text-white shadow-float transition active:scale-[0.98]"
            >
              <WhatsAppIcon className="size-6" /> ENVIAR PEDIDO PELO WHATSAPP
            </a>
          ) : (
            <div className="rounded-2xl bg-amber-50 p-4 text-sm text-amber-900">
              <b>Loja de demonstração:</b> o envio pelo WhatsApp está desativado porque nenhum número foi configurado para demonstrações
              (variável <code>NEXT_PUBLIC_PLATFORM_WHATSAPP</code>). A mensagem acima é exatamente a que seria enviada.
            </div>
          )}
          <button onClick={() => setStep("form")} className="mt-1 h-12 w-full font-bold text-brand">
            Alterar dados
          </button>
        </div>
      </Shell>
    );
  }

  const field = "h-13 w-full rounded-2xl border border-line bg-white px-4 text-[16px] outline-none transition placeholder:text-muted/60 focus:border-brand focus:ring-4 focus:ring-brand/15";
  const err = (k: string) => (errors[k] ? <p className="mt-1 text-sm font-semibold text-danger">{errors[k]}</p> : null);
  const ring = (k: string) => (errors[k] ? " border-danger ring-4 ring-danger/10" : "");

  return (
    <Shell title="Finalizar pedido">
      <form ref={formRef} onSubmit={review} noValidate className="space-y-4 pt-4">
        <Card icon={<User className="size-5" />} title="Seus dados">
          <div className="grid gap-3 sm:grid-cols-2">
            <label data-field="name" className="block">
              <span className="mb-1 block text-sm font-bold">Nome *</span>
              <input className={field + ring("name")} value={c.name} onChange={(e) => set("name", e.target.value)} autoComplete="name" placeholder="Como podemos te chamar?" maxLength={80} />
              {err("name")}
            </label>
            <label data-field="phone" className="block">
              <span className="mb-1 block text-sm font-bold">Telefone / WhatsApp *</span>
              <input className={field + ring("phone")} value={c.phone} onChange={(e) => set("phone", maskPhone(e.target.value))} inputMode="tel" autoComplete="tel-national" placeholder="(11) 98765-4321" />
              {err("phone")}
            </label>
          </div>
        </Card>

        <Card icon={<Bike className="size-5" />} title="Como você quer receber?">
          <div data-field="type" className="grid grid-cols-2 gap-2">
            {menu.ordering.delivery && (
              <Choice selected={c.type === "delivery"} onClick={() => set("type", "delivery")} icon={<Bike className="size-6" />} title="Entrega" subtitle={menu.ordering.deliveryTime ?? undefined} />
            )}
            {menu.ordering.pickup && (
              <Choice selected={c.type === "pickup"} onClick={() => set("type", "pickup")} icon={<Store className="size-6" />} title="Retirada" subtitle={menu.ordering.pickupTime ? `${menu.ordering.pickupTime} · sem taxa` : "sem taxa"} />
            )}
          </div>
          {err("type")}
          {c.type === "pickup" && menu.contact.address && (
            <p className="mt-3 flex gap-2 rounded-2xl bg-brand-softer p-3 text-sm">
              <MapPin className="size-4 shrink-0 text-brand" /> Retire em: {menu.contact.address}
            </p>
          )}
        </Card>

        {c.type === "delivery" && (
          <Card icon={<MapPin className="size-5" />} title="Endereço de entrega">
            <div className="grid grid-cols-6 gap-3">
              <label className="col-span-3 block sm:col-span-2">
                <span className="mb-1 block text-sm font-bold">CEP <span className="font-normal text-muted">(opcional)</span></span>
                <div className="relative">
                  <input
                    className={field}
                    value={c.address.cep}
                    inputMode="numeric"
                    autoComplete="postal-code"
                    placeholder="00000-000"
                    onChange={(e) => {
                      const v = maskCEP(e.target.value);
                      setAddr("cep", v);
                      if (onlyDigits(v).length === 8) lookupCep(v);
                      else setCepState("idle");
                    }}
                  />
                  {cepState === "loading" && <Loader2 className="absolute right-3 top-1/2 size-5 -translate-y-1/2 animate-spin text-muted" />}
                  {cepState === "ok" && <Check className="absolute right-3 top-1/2 size-5 -translate-y-1/2 text-success" />}
                </div>
                {cepState === "error" && <p className="mt-1 text-xs text-muted">CEP não encontrado. Preencha manualmente.</p>}
              </label>

              <label data-field="neighborhood" className="col-span-6 block sm:col-span-4">
                <span className="mb-1 block text-sm font-bold">Bairro *</span>
                {zonesMode ? (
                  <select
                    className={field + ring("neighborhood") + " appearance-none bg-[url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22%236b6475%22 stroke-width=%222%22><path d=%22m6 9 6 6 6-6%22/></svg>')] bg-[length:20px] bg-[right_12px_center] bg-no-repeat pr-10"}
                    value={zoneChoice}
                    onChange={(e) => {
                      setZoneChoice(e.target.value);
                      setErrors((x) => ({ ...x, neighborhood: "" }));
                      if (e.target.value !== UNLISTED_NEIGHBORHOOD) setAddr("neighborhood", e.target.value);
                      else setAddr("neighborhood", "");
                    }}
                  >
                    <option value="">Selecione seu bairro</option>
                    {menu.delivery.zones.map((z) => (
                      <option key={z.neighborhood} value={z.neighborhood}>
                        {z.neighborhood} — {menu.delivery.freeAbove !== null && evaluation.subtotal >= menu.delivery.freeAbove ? "grátis" : z.fee ? formatBRL(z.fee) : "grátis"}
                      </option>
                    ))}
                    <option value={UNLISTED_NEIGHBORHOOD}>Meu bairro não está na lista</option>
                  </select>
                ) : (
                  <input className={field + ring("neighborhood")} value={c.address.neighborhood} onChange={(e) => setAddr("neighborhood", e.target.value)} placeholder="Seu bairro" autoComplete="address-level3" />
                )}
                {err("neighborhood")}
                {zonesMode && zoneChoice === UNLISTED_NEIGHBORHOOD && (
                  <>
                    {!menu.delivery.allowUnlistedNeighborhoods ? (
                      <p className="mt-2 rounded-xl bg-amber-50 p-3 text-sm text-amber-900">
                        Ainda não entregamos em outros bairros. {menu.ordering.pickup && (
                          <button type="button" className="font-bold underline" onClick={() => set("type", "pickup")}>
                            Escolher retirada
                          </button>
                        )}
                      </p>
                    ) : (
                      <>
                        <input className={field + " mt-2"} value={c.address.neighborhood} onChange={(e) => setAddr("neighborhood", e.target.value)} placeholder="Digite o nome do bairro" />
                        <p className="mt-1 text-sm text-muted">A taxa de entrega será combinada com a loja pelo WhatsApp.</p>
                      </>
                    )}
                  </>
                )}
              </label>

              <label data-field="street" className="col-span-6 block sm:col-span-4">
                <span className="mb-1 block text-sm font-bold">Rua *</span>
                <input className={field + ring("street")} value={c.address.street} onChange={(e) => setAddr("street", e.target.value)} autoComplete="address-line1" placeholder="Rua, avenida…" />
                {err("street")}
              </label>
              <label data-field="number" className="col-span-2 block">
                <span className="mb-1 block text-sm font-bold">Número *</span>
                <input className={field + ring("number")} value={c.address.number} onChange={(e) => setAddr("number", e.target.value)} placeholder="123" />
                {err("number")}
              </label>
              <label className="col-span-4 block sm:col-span-3">
                <span className="mb-1 block text-sm font-bold">Complemento</span>
                <input className={field} value={c.address.complement} onChange={(e) => setAddr("complement", e.target.value)} placeholder="Apto, bloco…" autoComplete="address-line2" />
              </label>
              <label className="col-span-6 block sm:col-span-3">
                <span className="mb-1 block text-sm font-bold">Ponto de referência</span>
                <input className={field} value={c.address.reference} onChange={(e) => setAddr("reference", e.target.value)} placeholder="Próximo à padaria…" />
              </label>
            </div>
          </Card>
        )}

        {status.mustSchedule && (
          <Card icon={<CalendarClock className="size-5" />} title="Agendar pedido">
            <p className="mb-2 text-sm text-muted">Estamos fechados agora. Escolha o melhor horário para receber ou retirar:</p>
            <label data-field="scheduledFor" className="block">
              <select className={field + ring("scheduledFor")} value={c.scheduledFor ?? ""} onChange={(e) => set("scheduledFor", e.target.value || null)}>
                <option value="">Selecione o horário</option>
                {slots.map((s) => (
                  <option key={s.value} value={s.value}>
                    {s.label}
                  </option>
                ))}
              </select>
              {err("scheduledFor")}
            </label>
          </Card>
        )}

        <Card icon={<CreditCard className="size-5" />} title="Pagamento">
          <p className="-mt-1 mb-3 text-sm text-muted">O pagamento é feito diretamente com a loja.</p>
          <div data-field="payment" className="grid grid-cols-2 gap-2">
            {menu.ordering.paymentMethods.map((m) => (
              <Choice key={m} selected={c.payment === m} onClick={() => set("payment", m)} icon={PAY_ICON[m]} title={PAYMENT_LABELS[m]} compact />
            ))}
          </div>
          {err("payment")}
          {c.payment === "cash" && (
            <div className="mt-4 rounded-2xl bg-canvas p-4">
              <p className="font-bold">Precisa de troco?</p>
              <div className="mt-2 grid grid-cols-2 gap-2">
                <Choice selected={!c.needsChange} onClick={() => set("needsChange", false)} title="Não" compact />
                <Choice selected={c.needsChange} onClick={() => set("needsChange", true)} title="Sim" compact />
              </div>
              {c.needsChange && (
                <label data-field="changeFor" className="mt-3 block">
                  <span className="mb-1 block text-sm font-bold">Troco para quanto?</span>
                  <div className="relative">
                    <span className="absolute left-4 top-1/2 -translate-y-1/2 font-bold text-muted">R$</span>
                    <input className={field + ring("changeFor") + " pl-12"} value={changeText} onChange={(e) => setChangeText(e.target.value.replace(/[^\d,.]/g, ""))} inputMode="decimal" placeholder={String(Math.ceil(totals.total / 1000) * 10 || 50)} />
                  </div>
                  {err("changeFor")}
                </label>
              )}
            </div>
          )}
        </Card>

        <Card title="Observações do pedido">
          <textarea
            value={c.notes}
            onChange={(e) => set("notes", e.target.value.slice(0, 300))}
            rows={3}
            className="w-full resize-none rounded-2xl border border-line bg-white p-4 outline-none focus:border-brand focus:ring-4 focus:ring-brand/15"
            placeholder="Ex.: entregar na portaria, tocar o interfone 12…"
          />
        </Card>

        <Card title="Resumo do pedido" action={<Link href={`/${menu.slug}`} className="text-sm font-bold text-brand">Editar itens</Link>}>
          <ul className="divide-y divide-line">
            {evaluation.lines.map((l) => (
              <li key={l.item.id} className="flex gap-3 py-3">
                <span className="flex h-7 min-w-7 items-center justify-center rounded-lg bg-brand-soft text-sm font-extrabold text-brand">{l.item.quantity}x</span>
                <div className="min-w-0 flex-1">
                  <p className="font-bold leading-snug">{lineTitle(l)}</p>
                  <LineDetails line={l} />
                </div>
                <span className="font-bold">{formatBRL(l.total)}</span>
              </li>
            ))}
          </ul>
          <dl className="mt-2 space-y-1.5 border-t border-line pt-3 text-[15px]">
            <div className="flex justify-between">
              <dt className="text-muted">Subtotal</dt>
              <dd className="font-semibold">{formatBRL(totals.subtotal)}</dd>
            </div>
            {c.type === "delivery" && (
              <div className="flex justify-between">
                <dt className="text-muted">Taxa de entrega</dt>
                <dd className="font-semibold">
                  {quote.fee === null ? (quote.allowed ? "a combinar" : zonesMode ? "selecione o bairro" : "—") : quote.fee === 0 ? <span className="text-success">Grátis</span> : formatBRL(quote.fee)}
                </dd>
              </div>
            )}
            <div className="flex justify-between pt-1 text-lg">
              <dt className="font-extrabold">Total</dt>
              <dd className="font-extrabold text-brand">
                {formatBRL(totals.total)}
                {quote.fee === null && c.type === "delivery" && quote.allowed && <span className="text-sm font-semibold text-muted"> + entrega</span>}
              </dd>
            </div>
          </dl>
        </Card>

        <div className="pb-safe sticky bottom-0 -mx-4 border-t border-line bg-canvas/95 px-4 pt-3 backdrop-blur">
          {belowMin && <p className="mb-2 text-center text-sm font-semibold text-amber-800">Pedido mínimo: {formatBRL(menu.ordering.minOrder)}</p>}
          {!status.canOrder && <p className="mb-2 text-center text-sm font-semibold text-rose-700">{status.paused ? status.detail : `Estamos fechados no momento. ${status.detail ?? ""}`}</p>}
          <button
            type="submit"
            disabled={belowMin || !status.canOrder}
            className="flex h-16 w-full items-center justify-between rounded-2xl bg-brand px-6 text-[17px] font-extrabold text-on-brand shadow-float transition hover:bg-brand-strong active:scale-[0.98] disabled:bg-line disabled:text-muted disabled:shadow-none"
          >
            <span>REVISAR PEDIDO</span>
            <span>{formatBRL(totals.total)}</span>
          </button>
        </div>
      </form>
    </Shell>
  );
}

function Shell({ title, children, onBack }: { title: string; children: React.ReactNode; onBack?: () => void }) {
  const { menu } = useStore();
  return (
    <div className="min-h-dvh">
      <header className="sticky top-0 z-30 border-b border-line bg-white/95 backdrop-blur">
        <div className="mx-auto flex h-16 max-w-2xl items-center gap-2 px-2">
          {onBack ? (
            <button onClick={onBack} className="flex size-12 items-center justify-center rounded-full hover:bg-canvas" aria-label="Voltar">
              <ArrowLeft className="size-5" />
            </button>
          ) : (
            <Link href={`/${menu.slug}`} className="flex size-12 items-center justify-center rounded-full hover:bg-canvas" aria-label="Voltar ao cardápio">
              <ArrowLeft className="size-5" />
            </Link>
          )}
          <div className="min-w-0">
            <h1 className="truncate text-lg font-extrabold leading-tight">{title}</h1>
            <p className="truncate text-xs text-muted">{menu.name}</p>
          </div>
        </div>
      </header>
      <main className="mx-auto max-w-2xl px-4 pb-6">{children}</main>
    </div>
  );
}

function Card({ title, icon, children, action }: { title: string; icon?: React.ReactNode; children: React.ReactNode; action?: React.ReactNode }) {
  return (
    <section className="rounded-3xl bg-white p-4 shadow-card sm:p-5">
      <div className="mb-3 flex items-center justify-between">
        <h2 className="flex items-center gap-2 text-[17px] font-extrabold">
          {icon && <span className="text-brand">{icon}</span>}
          {title}
        </h2>
        {action}
      </div>
      {children}
    </section>
  );
}

function Choice({ selected, onClick, icon, title, subtitle, compact }: { selected: boolean; onClick: () => void; icon?: React.ReactNode; title: string; subtitle?: string; compact?: boolean }) {
  return (
    <button
      type="button"
      onClick={onClick}
      aria-pressed={selected}
      className={`flex items-center gap-3 rounded-2xl border-2 text-left transition active:scale-[0.98] ${compact ? "min-h-13 px-3 py-2" : "min-h-20 px-4 py-3"} ${
        selected ? "border-brand bg-brand-softer text-brand" : "border-line bg-white text-ink hover:border-brand/40"
      }`}
    >
      {icon && <span className={selected ? "text-brand" : "text-muted"}>{icon}</span>}
      <span className="min-w-0 flex-1">
        <span className="block font-extrabold">{title}</span>
        {subtitle && <span className="block text-xs font-medium text-muted">{subtitle}</span>}
      </span>
      <span className={`flex size-5 shrink-0 items-center justify-center rounded-full border-2 ${selected ? "border-brand bg-brand" : "border-line"}`}>
        {selected && <span className="size-2 rounded-full bg-white" />}
      </span>
    </button>
  );
}
