import { describe, expect, it } from "vitest";
import { getStoreStatus, scheduleSlots } from "@/lib/hours";
import { hoursSchema } from "@/lib/schema";

// 2026-11-16 é uma segunda-feira. São Paulo = UTC-3 (sem horário de verão).
const at = (local: string) => new Date(`${local}:00-03:00`);
const hours = (h: object) => hoursSchema.parse(h);

describe("horário de funcionamento", () => {
  const h = hours({ weekly: { mon: [{ open: "14:00", close: "22:00" }], tue: [{ open: "18:00", close: "02:00" }] } });

  it("aberto dentro do horário, fechado fora", () => {
    expect(getStoreStatus(h, at("2026-11-16T15:00")).isOpen).toBe(true);
    expect(getStoreStatus(h, at("2026-11-16T22:00")).isOpen).toBe(false);
    expect(getStoreStatus(h, at("2026-11-16T10:00")).detail).toBe("Abrimos hoje às 14:00");
  });

  it("intervalo que passa da meia-noite", () => {
    expect(getStoreStatus(h, at("2026-11-17T23:30")).isOpen).toBe(true);
    expect(getStoreStatus(h, at("2026-11-18T01:30")).isOpen).toBe(true);
    expect(getStoreStatus(h, at("2026-11-18T02:30")).isOpen).toBe(false);
  });

  it("fechado bloqueia pedidos; com agendamento permite", () => {
    const closed = getStoreStatus(h, at("2026-11-16T10:00"));
    expect(closed.canOrder).toBe(false);
    const sched = getStoreStatus({ ...h, whenClosed: "schedule" }, at("2026-11-16T10:00"));
    expect(sched).toMatchObject({ canOrder: true, mustSchedule: true });
    const slots = scheduleSlots({ ...h, whenClosed: "schedule" }, at("2026-11-16T10:00"));
    expect(slots[0].value).toBe("2026-11-16 14:00");
  });

  it("datas especiais e status manual", () => {
    const x = hours({ weekly: { mon: [{ open: "14:00", close: "22:00" }] }, special: [{ date: "2026-11-16", closed: true }] });
    expect(getStoreStatus(x, at("2026-11-16T15:00")).isOpen).toBe(false);
    expect(getStoreStatus({ ...x, mode: "open" }, at("2026-11-16T03:00")).isOpen).toBe(true);
    expect(getStoreStatus({ ...h, mode: "closed" }, at("2026-11-16T15:00")).isOpen).toBe(false);
  });

  it("pausa temporária desabilita pedidos com mensagem", () => {
    const s = getStoreStatus({ ...h, ordersPaused: true, pausedMessage: "Voltamos às 19h" }, at("2026-11-16T15:00"));
    expect(s).toMatchObject({ canOrder: false, paused: true, detail: "Voltamos às 19h" });
  });
});
