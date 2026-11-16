"use client";
import { useEffect, useRef, useSyncExternalStore } from "react";

/** Relógio que atualiza a cada 30 s; usa o horário do servidor na hidratação (sem divergência). */
const TICK = 30_000;
const listeners = new Set<() => void>();
let timer: ReturnType<typeof setInterval> | null = null;
let current = Math.floor(Date.now() / TICK) * TICK;
function subscribe(cb: () => void) {
  listeners.add(cb);
  if (!timer) {
    current = Date.now();
    timer = setInterval(() => {
      current = Date.now();
      listeners.forEach((l) => l());
    }, TICK);
  }
  return () => {
    listeners.delete(cb);
    if (!listeners.size && timer) {
      clearInterval(timer);
      timer = null;
    }
  };
}
export function useNow(serverNow: number): Date {
  const t = useSyncExternalStore(subscribe, () => current, () => serverNow);
  return new Date(t);
}

/**
 * Fecha um modal com o botão "voltar" do Android/navegador.
 * Ao abrir, adiciona uma entrada no histórico; o "voltar" fecha o modal em vez de sair da página.
 */
export function useBackToClose(open: boolean, onClose: () => void) {
  const closeRef = useRef(onClose);
  closeRef.current = onClose;
  useEffect(() => {
    if (!open) return;
    const id = Math.random();
    const path = window.location.pathname;
    // Mantém o estado interno do Next.js e acrescenta a marca do modal.
    window.history.pushState({ ...(window.history.state ?? {}), acaiModal: id }, "");
    let poppedByBack = false;
    const onPop = (e: PopStateEvent) => {
      // Se o estado atual ainda é o deste modal, quem fechou foi um modal "filho".
      if ((e.state as { acaiModal?: number } | null)?.acaiModal === id) return;
      poppedByBack = true;
      closeRef.current();
    };
    window.addEventListener("popstate", onPop);
    return () => {
      window.removeEventListener("popstate", onPop);
      const stillHere = window.location.pathname === path && (window.history.state as { acaiModal?: number } | null)?.acaiModal === id;
      if (!poppedByBack && stillHere) window.history.back();
    };
  }, [open]);
}

/** Trava a rolagem do fundo enquanto um modal está aberto. */
export function useLockBody(lock: boolean) {
  useEffect(() => {
    if (!lock) return;
    const prev = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => {
      document.body.style.overflow = prev;
    };
  }, [lock]);
}
