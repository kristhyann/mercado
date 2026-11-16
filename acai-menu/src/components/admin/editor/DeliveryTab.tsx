"use client";
import { Plus, Trash2 } from "lucide-react";
import { useEditor } from "./context";
import { Button, Card, Field, IconButton, MoneyInput, Select, TextInput, Toggle } from "../ui";
import { PAYMENT_METHODS } from "@/lib/schema";
import { PAYMENT_LABELS } from "@/lib/order";

export function DeliveryTab() {
  const { cfg, update } = useEditor();
  const o = cfg.ordering, dl = cfg.delivery;
  return (
    <div className="grid gap-4 lg:grid-cols-2">
      <Card title="Formas de receber">
        <div className="space-y-4">
          <Toggle checked={o.delivery} onChange={(v) => update((d) => { d.ordering.delivery = v; })} label="Entrega" />
          <Toggle checked={o.pickup} onChange={(v) => update((d) => { d.ordering.pickup = v; })} label="Retirada no estabelecimento (sem taxa)" />
          <div className="grid grid-cols-2 gap-3">
            <Field label="Tempo de entrega">
              <TextInput value={o.deliveryTime} onChange={(v) => update((d) => { d.ordering.deliveryTime = v || null; })} placeholder="30–50 min" />
            </Field>
            <Field label="Tempo de retirada">
              <TextInput value={o.pickupTime} onChange={(v) => update((d) => { d.ordering.pickupTime = v || null; })} placeholder="15 min" />
            </Field>
          </div>
          <Field label="Pedido mínimo" hint="0 = sem mínimo">
            <MoneyInput value={o.minOrder} onChange={(v) => update((d) => { d.ordering.minOrder = v ?? 0; })} />
          </Field>
        </div>
      </Card>

      <Card title="Pagamento">
        <div className="space-y-3">
          {PAYMENT_METHODS.map((m) => (
            <Toggle
              key={m}
              checked={o.paymentMethods.includes(m)}
              onChange={(v) => update((d) => { d.ordering.paymentMethods = v ? PAYMENT_METHODS.filter((x) => x === m || d.ordering.paymentMethods.includes(x)) : d.ordering.paymentMethods.filter((x) => x !== m); })}
              label={PAYMENT_LABELS[m]}
            />
          ))}
          <Field label="Chave Pix (opcional)" hint="É enviada na mensagem quando o cliente escolhe Pix.">
            <TextInput value={o.pixKey} onChange={(v) => update((d) => { d.ordering.pixKey = v.trim() || null; })} />
          </Field>
        </div>
      </Card>

      {o.delivery && (
        <Card title="Taxa de entrega" className="lg:col-span-2">
          <div className="grid gap-4 sm:grid-cols-3">
            <Field label="Tipo de taxa">
              <Select value={dl.mode} onChange={(v) => update((d) => { d.delivery.mode = v as typeof dl.mode; })}>
                <option value="fixed">Taxa fixa</option>
                <option value="zones">Por bairro</option>
                <option value="free">Entrega grátis</option>
              </Select>
            </Field>
            {dl.mode === "fixed" && (
              <Field label="Valor da taxa">
                <MoneyInput value={dl.fixedFee} onChange={(v) => update((d) => { d.delivery.fixedFee = v ?? 0; })} />
              </Field>
            )}
            {dl.mode !== "free" && (
              <Field label="Grátis a partir de (opcional)" hint="Subtotal mínimo para entrega grátis.">
                <MoneyInput allowEmpty placeholder="—" value={dl.freeAbove} onChange={(v) => update((d) => { d.delivery.freeAbove = v; })} />
              </Field>
            )}
          </div>

          {dl.mode === "zones" && (
            <div className="mt-5">
              <div className="mb-2 flex items-center justify-between">
                <h3 className="text-sm font-extrabold">Bairros atendidos</h3>
                <Button size="sm" onClick={() => update((d) => { d.delivery.zones.push({ neighborhood: "", fee: 0, active: true }); })}>
                  <Plus className="size-4" /> Bairro
                </Button>
              </div>
              {dl.zones.length === 0 && <p className="rounded-xl bg-amber-50 p-3 text-sm text-amber-900">Cadastre pelo menos um bairro.</p>}
              <ul className="space-y-2">
                {dl.zones.map((z, i) => (
                  <li key={i} className="flex items-center gap-2">
                    <TextInput value={z.neighborhood} onChange={(v) => update((d) => { d.delivery.zones[i].neighborhood = v; })} placeholder="Nome do bairro" className="flex-1" />
                    <MoneyInput value={z.fee} onChange={(v) => update((d) => { d.delivery.zones[i].fee = v ?? 0; })} className="w-32" />
                    <Toggle checked={z.active} onChange={(v) => update((d) => { d.delivery.zones[i].active = v; })} />
                    <IconButton label="Remover bairro" onClick={() => update((d) => { d.delivery.zones.splice(i, 1); })}>
                      <Trash2 className="size-4" />
                    </IconButton>
                  </li>
                ))}
              </ul>
              <div className="mt-4">
                <Toggle checked={dl.allowUnlistedNeighborhoods} onChange={(v) => update((d) => { d.delivery.allowUnlistedNeighborhoods = v; })} label="Aceitar bairros fora da lista" description="A taxa fica 'a combinar' com a loja pelo WhatsApp. Desligado: o cliente é avisado de que o bairro não é atendido." />
              </div>
            </div>
          )}
        </Card>
      )}
    </div>
  );
}
