"use client";
import { useEffect, useId, useState } from "react";
import { ChevronDown, ChevronUp, Loader2, X } from "lucide-react";
import { moneyText, parseMoney } from "@/lib/admin/editor";

export function cx(...c: (string | false | null | undefined)[]) {
  return c.filter(Boolean).join(" ");
}

const btnBase = "inline-flex items-center justify-center gap-2 rounded-xl font-bold transition active:scale-[0.98] disabled:pointer-events-none disabled:opacity-50";
const btnVariant = {
  primary: "bg-violet-700 text-white hover:bg-violet-800 shadow-sm",
  secondary: "bg-white text-slate-800 ring-1 ring-slate-200 hover:bg-slate-50",
  ghost: "text-slate-600 hover:bg-slate-100",
  danger: "bg-rose-600 text-white hover:bg-rose-700",
  dangerGhost: "text-rose-600 hover:bg-rose-50",
};

export function Button({
  variant = "secondary", size = "md", loading, className, children, ...rest
}: React.ButtonHTMLAttributes<HTMLButtonElement> & { variant?: keyof typeof btnVariant; size?: "sm" | "md" | "lg"; loading?: boolean }) {
  const s = size === "sm" ? "h-9 px-3 text-sm" : size === "lg" ? "h-12 px-5 text-[15px]" : "h-11 px-4 text-sm";
  return (
    <button type="button" {...rest} disabled={rest.disabled || loading} className={cx(btnBase, btnVariant[variant], s, className)}>
      {loading && <Loader2 className="size-4 animate-spin" />}
      {children}
    </button>
  );
}

export function IconButton({ label, className, children, ...rest }: React.ButtonHTMLAttributes<HTMLButtonElement> & { label: string }) {
  return (
    <button type="button" aria-label={label} title={label} {...rest} className={cx("inline-flex size-9 shrink-0 items-center justify-center rounded-lg text-slate-500 transition hover:bg-slate-100 hover:text-slate-900 disabled:opacity-30", className)}>
      {children}
    </button>
  );
}

export function MoveButtons({ onUp, onDown, first, last }: { onUp: () => void; onDown: () => void; first: boolean; last: boolean }) {
  return (
    <span className="flex flex-col">
      <IconButton label="Mover para cima" onClick={onUp} disabled={first} className="size-7">
        <ChevronUp className="size-4" />
      </IconButton>
      <IconButton label="Mover para baixo" onClick={onDown} disabled={last} className="size-7">
        <ChevronDown className="size-4" />
      </IconButton>
    </span>
  );
}

export function Card({ title, description, actions, children, className }: { title?: React.ReactNode; description?: React.ReactNode; actions?: React.ReactNode; children: React.ReactNode; className?: string }) {
  return (
    <section className={cx("rounded-2xl bg-white p-4 shadow-sm ring-1 ring-slate-200/70 sm:p-5", className)}>
      {(title || actions) && (
        <div className="mb-4 flex flex-wrap items-start justify-between gap-2">
          <div>
            {title && <h2 className="text-base font-extrabold text-slate-900">{title}</h2>}
            {description && <p className="mt-0.5 text-sm text-slate-500">{description}</p>}
          </div>
          {actions && <div className="flex flex-wrap gap-2">{actions}</div>}
        </div>
      )}
      {children}
    </section>
  );
}

export function Field({ label, hint, error, children, className }: { label: string; hint?: React.ReactNode; error?: string; children: React.ReactNode; className?: string }) {
  return (
    <label className={cx("block", className)}>
      <span className="mb-1 block text-sm font-semibold text-slate-700">{label}</span>
      {children}
      {hint && !error && <span className="mt-1 block text-xs text-slate-500">{hint}</span>}
      {error && <span className="mt-1 block text-xs font-semibold text-rose-600">{error}</span>}
    </label>
  );
}

export const inputCls =
  "h-11 w-full rounded-xl border border-slate-200 bg-white px-3 text-[16px] text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-violet-500 focus:ring-4 focus:ring-violet-500/15 disabled:bg-slate-50 sm:text-sm";

export function TextInput({ value, onChange, className, ...rest }: Omit<React.InputHTMLAttributes<HTMLInputElement>, "value" | "onChange"> & { value: string | null | undefined; onChange: (v: string) => void }) {
  return <input {...rest} value={value ?? ""} onChange={(e) => onChange(e.target.value)} className={cx(inputCls, className)} />;
}

export function TextArea({ value, onChange, rows = 3, ...rest }: Omit<React.TextareaHTMLAttributes<HTMLTextAreaElement>, "value" | "onChange"> & { value: string | null | undefined; onChange: (v: string) => void }) {
  return <textarea {...rest} rows={rows} value={value ?? ""} onChange={(e) => onChange(e.target.value)} className={cx(inputCls, "h-auto py-2.5")} />;
}

export function Select({ value, onChange, children, className }: { value: string; onChange: (v: string) => void; children: React.ReactNode; className?: string }) {
  return (
    <select value={value} onChange={(e) => onChange(e.target.value)} className={cx(inputCls, "pr-8", className)}>
      {children}
    </select>
  );
}

/** Campo de dinheiro em reais. Aceita "12,50" ou "12.5". */
export function MoneyInput({ value, onChange, allowEmpty, placeholder = "0,00", className }: { value: number | null | undefined; onChange: (v: number | null) => void; allowEmpty?: boolean; placeholder?: string; className?: string }) {
  const [text, setText] = useState(moneyText(value));
  const [focused, setFocused] = useState(false);
  useEffect(() => {
    if (!focused) setText(moneyText(value));
  }, [value, focused]);
  return (
    <div className={cx("relative", className)}>
      <span className="pointer-events-none absolute left-3 top-1/2 -translate-y-1/2 text-sm font-semibold text-slate-400">R$</span>
      <input
        inputMode="decimal"
        value={text}
        placeholder={placeholder}
        onFocus={() => setFocused(true)}
        onBlur={() => {
          setFocused(false);
          setText(moneyText(value));
        }}
        onChange={(e) => {
          const t = e.target.value.replace(/[^\d,.]/g, "");
          setText(t);
          const n = parseMoney(t);
          if (n !== null) onChange(n);
          else if (!t && allowEmpty) onChange(null);
          else if (!t) onChange(0);
        }}
        className={cx(inputCls, "pl-9 tabular-nums")}
      />
    </div>
  );
}

export function NumberInput({ value, onChange, min = 0, max, allowEmpty, placeholder, className }: { value: number | null | undefined; onChange: (v: number | null) => void; min?: number; max?: number; allowEmpty?: boolean; placeholder?: string; className?: string }) {
  return (
    <input
      type="number"
      inputMode="numeric"
      min={min}
      max={max}
      placeholder={placeholder}
      value={value ?? ""}
      onChange={(e) => {
        if (e.target.value === "") return onChange(allowEmpty ? null : min);
        let n = Math.floor(Number(e.target.value));
        if (!Number.isFinite(n)) return;
        if (n < min) n = min;
        if (max !== undefined && n > max) n = max;
        onChange(n);
      }}
      className={cx(inputCls, "tabular-nums", className)}
    />
  );
}

export function Toggle({ checked, onChange, label, description, disabled }: { checked: boolean; onChange: (v: boolean) => void; label?: React.ReactNode; description?: React.ReactNode; disabled?: boolean }) {
  const id = useId();
  return (
    <div className="flex items-start gap-3">
      <button
        id={id}
        type="button"
        role="switch"
        aria-checked={checked}
        disabled={disabled}
        onClick={() => onChange(!checked)}
        className={cx("relative mt-0.5 inline-flex h-6 w-11 shrink-0 items-center rounded-full transition disabled:opacity-50", checked ? "bg-violet-600" : "bg-slate-300")}
      >
        <span className={cx("inline-block size-5 rounded-full bg-white shadow transition", checked ? "translate-x-5.5" : "translate-x-0.5")} />
      </button>
      {(label || description) && (
        <label htmlFor={id} className="cursor-pointer select-none">
          {label && <span className="block text-sm font-semibold text-slate-800">{label}</span>}
          {description && <span className="block text-xs text-slate-500">{description}</span>}
        </label>
      )}
    </div>
  );
}

export function Badge({ tone = "slate", children }: { tone?: "slate" | "green" | "red" | "amber" | "violet"; children: React.ReactNode }) {
  const t = { slate: "bg-slate-100 text-slate-600", green: "bg-emerald-100 text-emerald-700", red: "bg-rose-100 text-rose-700", amber: "bg-amber-100 text-amber-800", violet: "bg-violet-100 text-violet-700" }[tone];
  return <span className={cx("inline-flex items-center rounded-full px-2 py-0.5 text-xs font-bold", t)}>{children}</span>;
}

/** Janela: gaveta inferior no celular, centralizada/lateral no computador. */
export function Modal({ open, onClose, title, children, footer, wide }: { open: boolean; onClose: () => void; title: string; children: React.ReactNode; footer?: React.ReactNode; wide?: boolean }) {
  useEffect(() => {
    if (!open) return;
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && onClose();
    window.addEventListener("keydown", onKey);
    const prev = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    return () => {
      window.removeEventListener("keydown", onKey);
      document.body.style.overflow = prev;
    };
  }, [open, onClose]);
  if (!open) return null;
  return (
    <div className="fixed inset-0 z-50 flex items-end justify-center sm:items-center sm:p-4" role="dialog" aria-modal="true" aria-label={title}>
      <button className="absolute inset-0 bg-slate-900/50" onClick={onClose} aria-label="Fechar" tabIndex={-1} />
      <div className={cx("relative flex max-h-[94dvh] w-full flex-col overflow-hidden rounded-t-2xl bg-slate-50 shadow-2xl sm:rounded-2xl", wide ? "sm:max-w-3xl" : "sm:max-w-lg")}>
        <header className="flex items-center justify-between gap-3 border-b border-slate-200 bg-white px-4 py-3">
          <h2 className="truncate text-lg font-extrabold text-slate-900">{title}</h2>
          <IconButton label="Fechar" onClick={onClose}>
            <X className="size-5" />
          </IconButton>
        </header>
        <div className="flex-1 overflow-y-auto p-4">{children}</div>
        {footer && <footer className="border-t border-slate-200 bg-white px-4 py-3" style={{ paddingBottom: "max(0.75rem, env(safe-area-inset-bottom))" }}>{footer}</footer>}
      </div>
    </div>
  );
}

/** Botão que pede confirmação antes de executar uma ação destrutiva. */
export function ConfirmButton({ onConfirm, children, message, label = "Excluir", size = "sm" }: { onConfirm: () => void; children: React.ReactNode; message: string; label?: string; size?: "sm" | "md" }) {
  const [open, setOpen] = useState(false);
  return (
    <>
      <span onClick={() => setOpen(true)}>{children}</span>
      <Modal
        open={open}
        onClose={() => setOpen(false)}
        title="Confirmar"
        footer={
          <div className="flex justify-end gap-2">
            <Button onClick={() => setOpen(false)} size={size}>Cancelar</Button>
            <Button variant="danger" size={size} onClick={() => { setOpen(false); onConfirm(); }}>{label}</Button>
          </div>
        }
      >
        <p className="text-slate-700">{message}</p>
      </Modal>
    </>
  );
}

export function EmptyState({ icon, title, children }: { icon: React.ReactNode; title: string; children?: React.ReactNode }) {
  return (
    <div className="rounded-2xl border-2 border-dashed border-slate-200 bg-white p-8 text-center">
      <div className="mx-auto flex size-12 items-center justify-center rounded-2xl bg-violet-50 text-violet-600">{icon}</div>
      <p className="mt-3 font-bold text-slate-800">{title}</p>
      {children && <div className="mt-2 text-sm text-slate-500">{children}</div>}
    </div>
  );
}
