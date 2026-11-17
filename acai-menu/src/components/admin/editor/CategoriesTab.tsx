"use client";
import { useState } from "react";
import { FolderPlus, Trash2 } from "lucide-react";
import { useEditor } from "./context";
import { Button, Card, EmptyState, Field, IconButton, Modal, MoveButtons, Select, TextInput, Toggle } from "../ui";
import { move, uniqueKey } from "@/lib/admin/editor";

export function CategoriesTab() {
  const { cfg, update } = useEditor();
  const [newName, setNewName] = useState("");
  const [deleting, setDeleting] = useState<string | null>(null);
  const [moveTo, setMoveTo] = useState("");
  const count = (key: string) => cfg.products.filter((p) => p.category === key).length;

  function add() {
    const name = newName.trim();
    if (!name) return;
    update((d) => { d.categories.push({ key: uniqueKey(name, d.categories.map((c) => c.key)), name, description: null, icon: null, active: true }); });
    setNewName("");
  }

  function confirmDelete() {
    const key = deleting!;
    update((d) => {
      d.products = d.products.map((p) => (p.category === key ? { ...p, category: moveTo } : p));
      if (!moveTo) d.products = d.products.filter((p) => p.category !== key);
      d.categories = d.categories.filter((c) => c.key !== key);
    });
    setDeleting(null);
  }

  const del = cfg.categories.find((c) => c.key === deleting);
  const others = cfg.categories.filter((c) => c.key !== deleting);

  return (
    <div className="space-y-4">
      <Card title="Nova categoria">
        <form onSubmit={(e) => { e.preventDefault(); add(); }} className="flex gap-2">
          <TextInput value={newName} onChange={setNewName} placeholder="Ex.: Barcas, Combos, Bebidas…" maxLength={60} className="flex-1" />
          <Button type="submit" variant="primary" disabled={!newName.trim()}><FolderPlus className="size-4" /> Adicionar</Button>
        </form>
      </Card>

      {cfg.categories.length === 0 ? (
        <EmptyState icon={<FolderPlus className="size-6" />} title="Nenhuma categoria" />
      ) : (
        <Card title="Categorias" description="A ordem aqui é a ordem no cardápio. Categorias sem produtos ativos não aparecem para o cliente.">
          <ul className="space-y-2">
            {cfg.categories.map((c, i) => (
              <li key={c.key} className="flex items-center gap-2 rounded-xl bg-slate-50 p-2">
                <MoveButtons first={i === 0} last={i === cfg.categories.length - 1} onUp={() => update((d) => { d.categories = move(d.categories, i, -1); })} onDown={() => update((d) => { d.categories = move(d.categories, i, 1); })} />
                <div className="min-w-0 flex-1">
                  <TextInput value={c.name} onChange={(v) => update((d) => { d.categories[i].name = v; })} maxLength={60} aria-label="Nome da categoria" />
                  <p className="mt-1 px-1 text-xs text-slate-500">{count(c.key)} produto(s)</p>
                </div>
                <Toggle checked={c.active} onChange={(v) => update((d) => { d.categories[i].active = v; })} />
                <IconButton label="Excluir categoria" onClick={() => { setDeleting(c.key); setMoveTo(others[0]?.key ?? ""); }}>
                  <Trash2 className="size-4 text-rose-500" />
                </IconButton>
              </li>
            ))}
          </ul>
        </Card>
      )}

      <Modal open={Boolean(del)} onClose={() => setDeleting(null)} title={`Excluir “${del?.name ?? ""}”`}
        footer={<div className="flex justify-end gap-2"><Button onClick={() => setDeleting(null)}>Cancelar</Button><Button variant="danger" onClick={confirmDelete}>Excluir categoria</Button></div>}>
        {del && count(del.key) > 0 ? (
          <Field label={`Esta categoria tem ${count(del.key)} produto(s). Mover para:`}>
            <Select value={moveTo} onChange={setMoveTo}>
              {others.map((o) => <option key={o.key} value={o.key}>{o.name}</option>)}
              <option value="">Excluir os produtos também</option>
            </Select>
          </Field>
        ) : (
          <p className="text-slate-700">A categoria está vazia e será removida.</p>
        )}
      </Modal>
    </div>
  );
}
