"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { AlertTriangle, Trash2 } from "lucide-react";
import { useEditor } from "./context";
import { ImageField } from "../ImageField";
import { Button, Card, Field, Modal, TextArea, TextInput, Toggle } from "../ui";
import { deleteStoreAction, renameStoreAction } from "@/app/admin/actions";

export function AdvancedTab() {
  const { cfg, update, slug } = useEditor();
  const router = useRouter();
  const [newSlug, setNewSlug] = useState(slug);
  const [msg, setMsg] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const [delOpen, setDelOpen] = useState(false);
  const [confirm, setConfirm] = useState("");

  async function rename() {
    if (!window.confirm(`Mudar o endereço de /${slug} para /${newSlug}? O link antigo deixará de funcionar. Salve as alterações pendentes antes.`)) return;
    setBusy(true);
    const res = await renameStoreAction(slug, newSlug);
    setBusy(false);
    if (!res.ok) return setMsg(res.error);
    window.location.href = `/admin/lojas/${res.slug}`;
  }

  async function remove() {
    setBusy(true);
    const res = await deleteStoreAction(slug, confirm);
    setBusy(false);
    if (!res.ok) return setMsg(res.error);
    router.push("/admin/lojas");
    router.refresh();
  }

  return (
    <div className="grid gap-4 lg:grid-cols-2">
      <Card title="Mensagem do WhatsApp" description="Personalize o início e o fim da mensagem do pedido.">
        <div className="space-y-4">
          <Field label="Cabeçalho" hint={`Padrão: 🍇 *NOVO PEDIDO - ${cfg.name.toUpperCase()}*. Use *texto* para negrito.`}>
            <TextInput value={cfg.whatsappMessage.header} onChange={(v) => update((d) => { d.whatsappMessage.header = v || null; })} />
          </Field>
          <Field label="Rodapé" hint="Padrão: PEDIDO ENVIADO PELO CARDÁPIO DIGITAL.">
            <TextArea value={cfg.whatsappMessage.footer} onChange={(v) => update((d) => { d.whatsappMessage.footer = v || null; })} rows={2} />
          </Field>
        </div>
      </Card>

      <Card title="Compartilhamento (SEO)" description="Como o link aparece no Google, WhatsApp, Instagram e Facebook.">
        <div className="space-y-4">
          <Field label="Título"><TextInput value={cfg.seo.title} onChange={(v) => update((d) => { d.seo.title = v || null; })} placeholder={`${cfg.name} — Cardápio digital`} maxLength={90} /></Field>
          <Field label="Descrição"><TextArea value={cfg.seo.description} onChange={(v) => update((d) => { d.seo.description = v || null; })} rows={2} maxLength={200} /></Field>
          <ImageField slug={slug} kind="seo" label="Imagem de compartilhamento (opcional)" value={cfg.seo.image} onChange={(u) => update((d) => { d.seo.image = u; })} />
          <p className="text-xs text-slate-500">Sem imagem, uma prévia com logo, nome e cores da loja é gerada automaticamente.</p>
        </div>
      </Card>

      <Card title="Endereço do cardápio">
        <div className="space-y-3">
          <Field label="Endereço (slug)" hint="Somente letras minúsculas, números e hífens. O link antigo deixa de funcionar.">
            <TextInput value={newSlug} onChange={(v) => setNewSlug(v.toLowerCase().replace(/[^a-z0-9-]/g, ""))} />
          </Field>
          <Button onClick={rename} disabled={busy || newSlug === slug || !newSlug} loading={busy}>Alterar endereço</Button>
        </div>
      </Card>

      <Card title="Outras opções">
        <Toggle checked={cfg.isDemo} onChange={(v) => update((d) => { d.isDemo = v; })} label="Loja de demonstração" description="Mostra a faixa “DEMONSTRAÇÃO” e envia os pedidos para o WhatsApp da plataforma." />
      </Card>

      <Card title="Zona de perigo" className="ring-rose-200 lg:col-span-2">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <p className="text-sm text-slate-600">Excluir a loja apaga definitivamente o cardápio, produtos e imagens. Para tirar do ar temporariamente, apenas desative a loja.</p>
          <Button variant="danger" onClick={() => setDelOpen(true)}><Trash2 className="size-4" /> Excluir loja</Button>
        </div>
      </Card>

      {msg && <p className="rounded-xl bg-rose-50 p-3 text-sm font-semibold text-rose-700 lg:col-span-2">{msg}</p>}

      <Modal open={delOpen} onClose={() => setDelOpen(false)} title="Excluir loja definitivamente"
        footer={<div className="flex justify-end gap-2"><Button onClick={() => setDelOpen(false)}>Cancelar</Button><Button variant="danger" onClick={remove} loading={busy} disabled={confirm !== slug}>Excluir para sempre</Button></div>}>
        <div className="space-y-3">
          <p className="flex gap-2 rounded-xl bg-rose-50 p-3 text-sm text-rose-800"><AlertTriangle className="size-5 shrink-0" /> Esta ação não pode ser desfeita.</p>
          <Field label={`Digite ${slug} para confirmar`}>
            <TextInput value={confirm} onChange={setConfirm} autoComplete="off" />
          </Field>
        </div>
      </Modal>
    </div>
  );
}
