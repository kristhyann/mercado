"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { createStoreAction } from "@/app/admin/actions";
import { slugify } from "@/lib/admin/editor";
import { maskPhone } from "@/lib/format";
import { Button, Card, Field, Select, TextInput } from "./ui";

export function NewStoreForm({ stores }: { stores: { slug: string; name: string }[] }) {
  const router = useRouter();
  const [name, setName] = useState("");
  const [slug, setSlug] = useState("");
  const [slugTouched, setSlugTouched] = useState(false);
  const [phone, setPhone] = useState("");
  const [base, setBase] = useState("_modelo");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [issues, setIssues] = useState<string[]>([]);

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    setBusy(true);
    setError(null);
    const digits = phone.replace(/\D/g, "");
    const res = await createStoreAction({ name, slug, whatsapp: digits.length === 10 || digits.length === 11 ? `55${digits}` : digits, base });
    setBusy(false);
    if (!res.ok) {
      setError(res.error);
      setIssues(res.issues ?? []);
      return;
    }
    router.push(`/admin/lojas/${res.slug}?nova=1`);
  }

  return (
    <form onSubmit={submit} className="mx-auto max-w-xl space-y-4">
      <div>
        <h1 className="text-2xl font-extrabold tracking-tight">Nova loja</h1>
        <p className="text-sm text-slate-500">A loja é criada <b>inativa</b>. Configure produtos e aparência e ative quando estiver pronta.</p>
      </div>
      <Card>
        <div className="space-y-4">
          <Field label="Nome da loja">
            <TextInput value={name} onChange={(v) => { setName(v); if (!slugTouched) setSlug(slugify(v)); }} placeholder="Açaí do João" required maxLength={120} />
          </Field>
          <Field label="Endereço do cardápio" hint={`O link será: seudominio.com/${slug || "endereco-da-loja"}`}>
            <TextInput value={slug} onChange={(v) => { setSlugTouched(true); setSlug(v.toLowerCase().replace(/[^a-z0-9-]/g, "")); }} placeholder="acai-do-joao" required maxLength={60} />
          </Field>
          <Field label="WhatsApp que recebe os pedidos" hint="Com DDD. Ex.: (11) 98765-4321">
            <TextInput value={phone} onChange={(v) => setPhone(maskPhone(v))} inputMode="tel" placeholder="(11) 98765-4321" required />
          </Field>
          <Field label="Começar a partir de">
            <Select value={base} onChange={setBase}>
              <option value="_modelo">Modelo básico (Monte seu açaí + bebidas)</option>
              {stores.map((s) => (
                <option key={s.slug} value={s.slug}>Copiar cardápio de: {s.name}</option>
              ))}
            </Select>
          </Field>
        </div>
      </Card>
      {error && (
        <div className="rounded-xl bg-rose-50 p-3 text-sm text-rose-700">
          <p className="font-semibold">{error}</p>
          {issues.map((i) => <p key={i}>• {i}</p>)}
        </div>
      )}
      <Button type="submit" variant="primary" size="lg" loading={busy} className="w-full">Criar loja</Button>
    </form>
  );
}
