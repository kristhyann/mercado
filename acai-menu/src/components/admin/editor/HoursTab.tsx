"use client";
import { Plus, Trash2 } from "lucide-react";
import { useEditor } from "./context";
import { Button, Card, Field, IconButton, Select, TextInput, Toggle, inputCls } from "../ui";
import { WEEKDAYS, type Weekday } from "@/lib/schema";
import { WEEKDAY_LABELS } from "@/lib/hours";

const ORDER: Weekday[] = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];

function Intervals({ list, onChange }: { list: { open: string; close: string }[]; onChange: (l: { open: string; close: string }[]) => void }) {
  return (
    <div className="space-y-2">
      {list.length === 0 && <p className="text-sm text-slate-400">Fechado</p>}
      {list.map((it, i) => (
        <div key={i} className="flex items-center gap-2">
          <input type="time" value={it.open} onChange={(e) => onChange(list.map((x, j) => (j === i ? { ...x, open: e.target.value } : x)))} className={inputCls + " w-32"} aria-label="Abre" />
          <span className="text-sm text-slate-400">às</span>
          <input type="time" value={it.close} onChange={(e) => onChange(list.map((x, j) => (j === i ? { ...x, close: e.target.value } : x)))} className={inputCls + " w-32"} aria-label="Fecha" />
          <IconButton label="Remover horário" onClick={() => onChange(list.filter((_, j) => j !== i))}>
            <Trash2 className="size-4" />
          </IconButton>
        </div>
      ))}
    </div>
  );
}

export function HoursTab() {
  const { cfg, update } = useEditor();
  const h = cfg.hours;
  return (
    <div className="grid gap-4 lg:grid-cols-2">
      <Card title="Status da loja" description="Use para fechar ou pausar rapidamente sem mexer na grade.">
        <div className="space-y-4">
          <Field label="Funcionamento">
            <Select value={h.mode} onChange={(v) => update((d) => { d.hours.mode = v as typeof h.mode; })}>
              <option value="auto">Automático (segue os horários abaixo)</option>
              <option value="open">Sempre aberta (forçar aberto)</option>
              <option value="closed">Fechada (forçar fechado)</option>
            </Select>
          </Field>
          <Field label="Quando estiver fechada">
            <Select value={h.whenClosed} onChange={(v) => update((d) => { d.hours.whenClosed = v as typeof h.whenClosed; })}>
              <option value="block">Não aceitar pedidos</option>
              <option value="schedule">Aceitar pedidos agendados</option>
            </Select>
          </Field>
          <Toggle checked={h.ordersPaused} onChange={(v) => update((d) => { d.hours.ordersPaused = v; })} label="Pausar pedidos agora" description="Ex.: muito movimento. O cardápio continua visível." />
          {h.ordersPaused && (
            <Field label="Mensagem da pausa">
              <TextInput value={h.pausedMessage} onChange={(v) => update((d) => { d.hours.pausedMessage = v || null; })} placeholder="Estamos com muitos pedidos. Voltamos em 30 minutos!" />
            </Field>
          )}
          <Field label="Fuso horário">
            <Select value={h.timezone} onChange={(v) => update((d) => { d.hours.timezone = v; })}>
              {["America/Sao_Paulo", "America/Manaus", "America/Belem", "America/Fortaleza", "America/Recife", "America/Cuiaba", "America/Porto_Velho", "America/Rio_Branco", "America/Noronha"].map((z) => (
                <option key={z} value={z}>{z.replace("America/", "").replace("_", " ")}</option>
              ))}
            </Select>
          </Field>
        </div>
      </Card>

      <Card title="Horário semanal" description="Vários horários por dia são permitidos. Fechar depois da meia-noite: ex. 18:00 às 02:00.">
        <ul className="divide-y divide-slate-100">
          {ORDER.map((day) => (
            <li key={day} className="flex flex-wrap items-start gap-3 py-3">
              <span className="w-20 pt-2.5 text-sm font-bold">{WEEKDAY_LABELS[day]}</span>
              <div className="min-w-0 flex-1">
                <Intervals list={h.weekly[day]} onChange={(l) => update((d) => { d.hours.weekly[day] = l; })} />
              </div>
              <Button size="sm" variant="ghost" onClick={() => update((d) => { d.hours.weekly[day].push({ open: "14:00", close: "22:00" }); })}>
                <Plus className="size-4" /> Horário
              </Button>
            </li>
          ))}
        </ul>
        <Button size="sm" className="mt-2" onClick={() => update((d) => { const mon = d.hours.weekly.mon; for (const w of WEEKDAYS) d.hours.weekly[w] = structuredClone(mon); })}>
          Copiar horário de segunda para todos os dias
        </Button>
      </Card>

      <Card title="Datas especiais" description="Feriados e horários diferentes em datas específicas." className="lg:col-span-2"
        actions={<Button size="sm" onClick={() => update((d) => { d.hours.special.push({ date: new Date().toISOString().slice(0, 10), label: null, closed: true, intervals: [] }); })}><Plus className="size-4" /> Adicionar data</Button>}>
        {h.special.length === 0 ? (
          <p className="text-sm text-slate-500">Nenhuma data especial.</p>
        ) : (
          <ul className="space-y-3">
            {h.special.map((s, i) => (
              <li key={i} className="flex flex-wrap items-start gap-3 rounded-xl bg-slate-50 p-3">
                <input type="date" value={s.date} onChange={(e) => update((d) => { d.hours.special[i].date = e.target.value; })} className={inputCls + " w-44"} aria-label="Data" />
                <TextInput value={s.label} onChange={(v) => update((d) => { d.hours.special[i].label = v || null; })} placeholder="Ex.: Natal" className="w-40" />
                <div className="pt-2">
                  <Toggle checked={s.closed} onChange={(v) => update((d) => { d.hours.special[i].closed = v; if (!v && !d.hours.special[i].intervals.length) d.hours.special[i].intervals = [{ open: "14:00", close: "18:00" }]; })} label="Fechado" />
                </div>
                {!s.closed && <Intervals list={s.intervals} onChange={(l) => update((d) => { d.hours.special[i].intervals = l; })} />}
                <IconButton label="Remover data" className="ml-auto" onClick={() => update((d) => { d.hours.special.splice(i, 1); })}>
                  <Trash2 className="size-4" />
                </IconButton>
              </li>
            ))}
          </ul>
        )}
      </Card>
    </div>
  );
}
