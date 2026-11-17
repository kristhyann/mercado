"use client";
import { useEditor } from "./context";
import { ImageField } from "../ImageField";
import { Card, Field, TextArea, TextInput, Toggle, inputCls } from "../ui";
import { maskPhone } from "@/lib/format";

function ColorField({ label, value, onChange }: { label: string; value: string; onChange: (v: string) => void }) {
  return (
    <Field label={label}>
      <div className="flex gap-2">
        <input type="color" value={value} onChange={(e) => onChange(e.target.value.toUpperCase())} className="h-11 w-14 shrink-0 cursor-pointer rounded-xl border border-slate-200 bg-white p-1" aria-label={label} />
        <input value={value} onChange={(e) => onChange(e.target.value.trim())} className={inputCls + " font-mono uppercase"} maxLength={7} />
      </div>
    </Field>
  );
}

/** "5511987654321" ⇄ "(11) 98765-4321" (o 55 é adicionado automaticamente). */
function WhatsAppField() {
  const { cfg, update } = useEditor();
  const local = cfg.contact.whatsapp.startsWith("55") ? cfg.contact.whatsapp.slice(2) : cfg.contact.whatsapp;
  const placeholder = /^5500/.test(cfg.contact.whatsapp);
  return (
    <Field label="WhatsApp que recebe os pedidos" hint="Com DDD. O código do Brasil (55) é adicionado automaticamente." error={placeholder && !cfg.isDemo ? "Informe o número real da loja." : undefined}>
      <TextInput
        value={placeholder ? "" : maskPhone(local)}
        onChange={(v) => update((d) => { d.contact.whatsapp = `55${v.replace(/\D/g, "").slice(0, 11)}`; })}
        inputMode="tel"
        placeholder="(11) 98765-4321"
      />
    </Field>
  );
}

export function GeneralTab() {
  const { cfg, update, slug } = useEditor();
  return (
    <div className="grid gap-4 lg:grid-cols-2">
      <Card title="Informações da loja" className="lg:col-span-2">
        <div className="grid gap-4 sm:grid-cols-2">
          <Field label="Nome">
            <TextInput value={cfg.name} onChange={(v) => update((d) => { d.name = v; })} maxLength={120} />
          </Field>
          <div className="flex items-end pb-2">
            <Toggle checked={cfg.active} onChange={(v) => update((d) => { d.active = v; })} label={cfg.active ? "Loja ativa (visível para os clientes)" : "Loja inativa (oculta)"} description="Desative para tirar o cardápio do ar." />
          </div>
          <Field label="Descrição" className="sm:col-span-2" hint="Aparece abaixo do nome no cardápio.">
            <TextArea value={cfg.description} onChange={(v) => update((d) => { d.description = v || null; })} maxLength={400} />
          </Field>
        </div>
      </Card>

      <Card title="Contato e endereço">
        <div className="space-y-4">
          <WhatsAppField />
          <Field label="Instagram" hint="Somente o usuário, sem @.">
            <TextInput value={cfg.contact.instagram} onChange={(v) => update((d) => { d.contact.instagram = v.replace(/^@/, "").trim() || null; })} placeholder="acaidojoao" />
          </Field>
          <Field label="Endereço" hint="Mostrado para retirada.">
            <TextInput value={cfg.contact.address} onChange={(v) => update((d) => { d.contact.address = v || null; })} placeholder="Rua, número — Bairro, Cidade" />
          </Field>
          <Field label="Região atendida">
            <TextInput value={cfg.contact.region} onChange={(v) => update((d) => { d.contact.region = v || null; })} placeholder="Entregamos no Centro e região" />
          </Field>
          <Field label="Link do Google Maps (opcional)">
            <TextInput value={cfg.contact.mapsUrl} onChange={(v) => update((d) => { d.contact.mapsUrl = v.trim() || null; })} placeholder="https://maps.app.goo.gl/…" />
          </Field>
        </div>
      </Card>

      <Card title="Identidade visual">
        <div className="space-y-5">
          <div className="grid grid-cols-2 gap-3">
            <ColorField label="Cor principal" value={cfg.branding.primaryColor} onChange={(v) => update((d) => { d.branding.primaryColor = v; })} />
            <ColorField label="Cor secundária" value={cfg.branding.secondaryColor} onChange={(v) => update((d) => { d.branding.secondaryColor = v; })} />
          </div>
          <div className="flex items-center gap-3 rounded-xl p-3 text-sm font-bold" style={{ background: cfg.branding.primaryColor, color: "#fff" }}>
            Pré-visualização
            <span className="ml-auto rounded-full px-3 py-1" style={{ background: cfg.branding.secondaryColor, color: "#1c1022" }}>Mais vendido</span>
          </div>
          <ImageField slug={slug} kind="logo" label="Logotipo" value={cfg.branding.logo} onChange={(u) => update((d) => { d.branding.logo = u; })} />
          <ImageField slug={slug} kind="cover" label="Foto de capa" value={cfg.branding.cover} onChange={(u) => update((d) => { d.branding.cover = u; })} />
        </div>
      </Card>

      <Card title="Banner promocional" className="lg:col-span-2" actions={<Toggle checked={cfg.banner.enabled} onChange={(v) => update((d) => { d.banner.enabled = v; })} label="Exibir" />}>
        <div className="grid gap-4 sm:grid-cols-2">
          <div className="space-y-4">
            <Field label="Título">
              <TextInput value={cfg.banner.title} onChange={(v) => update((d) => { d.banner.title = v || null; })} placeholder="Monte seu açaí do seu jeito!" />
            </Field>
            <Field label="Subtítulo">
              <TextInput value={cfg.banner.subtitle} onChange={(v) => update((d) => { d.banner.subtitle = v || null; })} placeholder="Peça agora e receba em casa." />
            </Field>
          </div>
          <ImageField slug={slug} kind="banner" label="Imagem do banner (opcional)" value={cfg.banner.image} onChange={(u) => update((d) => { d.banner.image = u; })} />
        </div>
      </Card>
    </div>
  );
}
