/**
 * Status de funcionamento calculado no fuso horário da loja.
 * Suporta vários intervalos por dia, intervalos que passam da meia-noite
 * (ex.: 18:00–02:00), datas especiais (feriados) e status manual.
 */
import { WEEKDAYS, type Hours, type Interval } from "./schema";

export const WEEKDAY_LABELS: Record<(typeof WEEKDAYS)[number], string> = {
  sun: "Domingo", mon: "Segunda", tue: "Terça", wed: "Quarta", thu: "Quinta", fri: "Sexta", sat: "Sábado",
};
const SHORT = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"];

const toMin = (hhmm: string) => {
  const [h, m] = hhmm.split(":").map(Number);
  return h * 60 + m;
};
const fmt = (min: number) => `${String(Math.floor(min / 60) % 24).padStart(2, "0")}:${String(min % 60).padStart(2, "0")}`;

/** Data/hora "de parede" no fuso da loja. */
export interface LocalTime {
  date: string; // AAAA-MM-DD
  weekday: number; // 0 = domingo
  minutes: number; // minutos desde 00:00
}

export function localTime(now: Date, timeZone: string): LocalTime {
  let parts: Intl.DateTimeFormatPart[];
  try {
    parts = new Intl.DateTimeFormat("en-US", {
      timeZone, year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", hourCycle: "h23", weekday: "short",
    }).formatToParts(now);
  } catch {
    return localTime(now, "America/Sao_Paulo");
  }
  const get = (t: string) => parts.find((p) => p.type === t)?.value ?? "";
  const wd = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].indexOf(get("weekday"));
  return {
    date: `${get("year")}-${get("month")}-${get("day")}`,
    weekday: wd,
    minutes: (Number(get("hour")) % 24) * 60 + Number(get("minute")),
  };
}

function addDays(date: string, n: number): string {
  const d = new Date(`${date}T12:00:00Z`);
  d.setUTCDate(d.getUTCDate() + n);
  return d.toISOString().slice(0, 10);
}
function weekdayOf(date: string): number {
  return new Date(`${date}T12:00:00Z`).getUTCDay();
}

/** Intervalos de um dia específico (considera datas especiais). */
export function intervalsFor(hours: Hours, date: string): Interval[] {
  const special = hours.special.find((s) => s.date === date);
  if (special) return special.closed ? [] : special.intervals;
  return hours.weekly[WEEKDAYS[weekdayOf(date)]];
}

/** Janelas [início, fim) em minutos relativos à meia-noite do dia `date`. */
function windowsFor(hours: Hours, date: string): [number, number][] {
  const out: [number, number][] = [];
  for (const i of intervalsFor(hours, date)) {
    const o = toMin(i.open);
    let c = toMin(i.close);
    if (c <= o) c += 24 * 60; // passa da meia-noite
    out.push([o, c]);
  }
  for (const i of intervalsFor(hours, addDays(date, -1))) {
    const o = toMin(i.open);
    const c = toMin(i.close);
    if (c <= o && c > 0) out.push([0, c]); // continuação de ontem
  }
  return out;
}

export interface StoreStatus {
  isOpen: boolean;
  /** Pedidos permitidos agora (aberta, ou fechada com agendamento). */
  canOrder: boolean;
  mustSchedule: boolean;
  paused: boolean;
  label: string;
  detail: string | null;
  nextOpening: { date: string; minutes: number; label: string } | null;
}

export function nextOpening(hours: Hours, now: Date, maxDays = 8): StoreStatus["nextOpening"] {
  const lt = localTime(now, hours.timezone);
  for (let d = 0; d < maxDays; d++) {
    const date = addDays(lt.date, d);
    const starts = intervalsFor(hours, date)
      .map((i) => toMin(i.open))
      .filter((m) => d > 0 || m > lt.minutes)
      .sort((a, b) => a - b);
    if (starts.length) {
      const m = starts[0];
      const day = d === 0 ? "hoje" : d === 1 ? "amanhã" : SHORT[weekdayOf(date)].toLowerCase();
      return { date, minutes: m, label: `${day} às ${fmt(m)}` };
    }
  }
  return null;
}

export function getStoreStatus(hours: Hours, now: Date = new Date()): StoreStatus {
  const lt = localTime(now, hours.timezone);
  let isOpen: boolean;
  let closesAt: number | null = null;
  if (hours.mode === "open") isOpen = true;
  else if (hours.mode === "closed") isOpen = false;
  else {
    const w = windowsFor(hours, lt.date).find(([o, c]) => lt.minutes >= o && lt.minutes < c);
    isOpen = Boolean(w);
    if (w) closesAt = w[1];
  }

  const next = isOpen ? null : hours.mode === "closed" ? null : nextOpening(hours, now);
  if (hours.ordersPaused) {
    return {
      isOpen, canOrder: false, mustSchedule: false, paused: true,
      label: "Pedidos pausados",
      detail: hours.pausedMessage ?? "Estamos com os pedidos pausados no momento. Volte em instantes!",
      nextOpening: next,
    };
  }
  if (isOpen) {
    return {
      isOpen: true, canOrder: true, mustSchedule: false, paused: false,
      label: "Aberto agora",
      detail: closesAt !== null ? `Fecha às ${fmt(closesAt)}` : null,
      nextOpening: null,
    };
  }
  const schedule = hours.whenClosed === "schedule" && next !== null;
  return {
    isOpen: false, canOrder: schedule, mustSchedule: schedule, paused: false,
    label: "Fechado",
    detail: next ? `Abrimos ${next.label}` : null,
    nextOpening: next,
  };
}

/** Horários disponíveis para agendamento (a cada `step` min) nos próximos dias. */
export function scheduleSlots(hours: Hours, now: Date, days = 3, step = 30, leadMinutes = 30): { value: string; label: string }[] {
  const lt = localTime(now, hours.timezone);
  const slots: { value: string; label: string }[] = [];
  for (let d = 0; d < days; d++) {
    const date = addDays(lt.date, d);
    const wd = weekdayOf(date);
    const [, mm, dd] = date.split("-");
    const dayLabel = d === 0 ? "Hoje" : d === 1 ? "Amanhã" : `${SHORT[wd]} ${dd}/${mm}`;
    for (const i of intervalsFor(hours, date)) {
      const o = toMin(i.open);
      let c = toMin(i.close);
      if (c <= o) c = 24 * 60;
      for (let m = Math.ceil(o / step) * step; m < c; m += step) {
        if (d === 0 && m < lt.minutes + leadMinutes) continue;
        slots.push({ value: `${date} ${fmt(m)}`, label: `${dayLabel}${d > 1 ? "" : ` (${dd}/${mm})`} às ${fmt(m)}` });
      }
    }
  }
  return slots.slice(0, 120);
}

/** Linhas da tabela de horários para exibir ao cliente. */
export function weeklySummary(hours: Hours): { day: string; text: string; weekday: number }[] {
  const order = [1, 2, 3, 4, 5, 6, 0];
  return order.map((wd) => {
    const list = hours.weekly[WEEKDAYS[wd]];
    return {
      weekday: wd,
      day: WEEKDAY_LABELS[WEEKDAYS[wd]],
      text: list.length ? list.map((i) => `${i.open} às ${i.close}`).join(" · ") : "Fechado",
    };
  });
}
