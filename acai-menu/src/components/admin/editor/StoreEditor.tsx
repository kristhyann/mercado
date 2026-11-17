"use client";
import { useCallback, useDeferredValue, useEffect, useMemo, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { AlertTriangle, ArrowLeft, CheckCircle2, ExternalLink, Save, Undo2 } from "lucide-react";
import type { StoreConfig } from "@/lib/schema";
import { parseStore } from "@/lib/menu";
import { saveStoreAction } from "@/app/admin/actions";
import { EditorContext } from "./context";
import { Badge, Button, cx } from "../ui";
import { GeneralTab } from "./GeneralTab";
import { HoursTab } from "./HoursTab";
import { DeliveryTab } from "./DeliveryTab";
import { CategoriesTab } from "./CategoriesTab";
import { ProductsTab } from "./ProductsTab";
import { SizesTab } from "./SizesTab";
import { AddonsTab } from "./AddonsTab";
import { AdvancedTab } from "./AdvancedTab";

const TABS = [
  { id: "loja", label: "Loja", C: GeneralTab },
  { id: "produtos", label: "Produtos", C: ProductsTab },
  { id: "categorias", label: "Categorias", C: CategoriesTab },
  { id: "tamanhos", label: "Tamanhos", C: SizesTab },
  { id: "acompanhamentos", label: "Acompanhamentos", C: AddonsTab },
  { id: "horarios", label: "Horários", C: HoursTab },
  { id: "entrega", label: "Entrega e pagamento", C: DeliveryTab },
  { id: "avancado", label: "Avançado", C: AdvancedTab },
] as const;

export function StoreEditor({ initial, updatedAt, siteUrl, isNew }: { initial: StoreConfig; updatedAt: string; siteUrl: string; isNew: boolean }) {
  const router = useRouter();
  const [cfg, setCfg] = useState<StoreConfig>(initial);
  const [saved, setSaved] = useState(() => JSON.stringify(initial));
  const [version, setVersion] = useState(updatedAt);
  const [tab, setTab] = useState<(typeof TABS)[number]["id"]>("loja");
  const [saving, setSaving] = useState(false);
  const [result, setResult] = useState<{ ok: boolean; message: string; issues?: string[] } | null>(isNew ? { ok: true, message: "Loja criada! Ela está inativa: configure e ative quando estiver pronta." } : null);

  const dirty = JSON.stringify(cfg) !== saved;
  const deferred = useDeferredValue(cfg);
  const issues = useMemo(() => parseStore(deferred, { strict: true }).issues.filter((i) => !i.startsWith("aviso")), [deferred]);

  const update = useCallback((fn: (d: StoreConfig) => void) => {
    setCfg((prev) => {
      const d = structuredClone(prev);
      fn(d);
      return d;
    });
  }, []);

  const save = useCallback(async () => {
    setSaving(true);
    setResult(null);
    const res = await saveStoreAction(cfg.slug, cfg, version);
    setSaving(false);
    if (res.ok) {
      setVersion(res.updatedAt);
      setSaved(JSON.stringify(cfg));
      setResult({ ok: true, message: cfg.active ? "Salvo! O cardápio público já foi atualizado." : "Salvo! (a loja está inativa e não aparece para os clientes)" });
      router.refresh();
    } else {
      setResult({ ok: false, message: res.error, issues: res.issues });
    }
  }, [cfg, version, router]);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "s") {
        e.preventDefault();
        if (dirty && !saving) save();
      }
    };
    const onLeave = (e: BeforeUnloadEvent) => {
      if (dirty) e.preventDefault();
    };
    window.addEventListener("keydown", onKey);
    window.addEventListener("beforeunload", onLeave);
    return () => {
      window.removeEventListener("keydown", onKey);
      window.removeEventListener("beforeunload", onLeave);
    };
  }, [dirty, saving, save]);

  useEffect(() => {
    if (result?.ok) {
      const t = setTimeout(() => setResult(null), 5000);
      return () => clearTimeout(t);
    }
  }, [result]);

  const Active = TABS.find((t) => t.id === tab)!.C;
  return (
    <EditorContext.Provider value={{ cfg, update, slug: cfg.slug, issues }}>
      <div className="space-y-4">
        <div className="flex flex-wrap items-center gap-3">
          <Link href="/admin/lojas" className="flex size-10 items-center justify-center rounded-xl bg-white ring-1 ring-slate-200" aria-label="Voltar para lojas">
            <ArrowLeft className="size-5" />
          </Link>
          <div className="min-w-0 flex-1">
            <div className="flex flex-wrap items-center gap-2">
              <h1 className="truncate text-xl font-extrabold tracking-tight sm:text-2xl">{cfg.name || "Sem nome"}</h1>
              {cfg.active ? <Badge tone="green">Ativa</Badge> : <Badge>Inativa</Badge>}
              {cfg.isDemo && <Badge tone="amber">Demonstração</Badge>}
            </div>
            <p className="truncate text-sm text-slate-500">/{cfg.slug}</p>
          </div>
          {cfg.active && (
            <a href={`${siteUrl}/${cfg.slug}`} target="_blank" rel="noopener noreferrer" className="inline-flex h-10 items-center gap-1.5 rounded-xl bg-white px-3 text-sm font-semibold ring-1 ring-slate-200 hover:bg-slate-50">
              <ExternalLink className="size-4" /> Ver cardápio
            </a>
          )}
        </div>

        <nav className="sticky top-14 z-20 -mx-3 overflow-x-auto border-b border-slate-200 bg-slate-100/95 px-3 backdrop-blur lg:top-0" aria-label="Seções">
          <div className="flex gap-1 py-2">
            {TABS.map((t) => (
              <button
                key={t.id}
                onClick={() => setTab(t.id)}
                className={cx("h-10 shrink-0 rounded-xl px-3.5 text-sm font-bold transition", tab === t.id ? "bg-violet-700 text-white shadow-sm" : "text-slate-600 hover:bg-white")}
              >
                {t.label}
              </button>
            ))}
          </div>
        </nav>

        {result && (
          <div className={cx("rounded-xl p-3 text-sm", result.ok ? "bg-emerald-50 text-emerald-800" : "bg-rose-50 text-rose-800")} role="status">
            <p className="flex items-center gap-2 font-bold">
              {result.ok ? <CheckCircle2 className="size-4" /> : <AlertTriangle className="size-4" />} {result.message}
            </p>
            {result.issues?.map((i) => <p key={i} className="ml-6">• {i}</p>)}
          </div>
        )}

        <Active />

        <div className="h-20" />
        <div className={cx("fixed inset-x-0 z-40 border-t border-slate-200 bg-white/95 px-3 py-3 shadow-[0_-8px_24px_rgba(0,0,0,0.06)] backdrop-blur transition lg:bottom-0 lg:left-60", "bottom-14 lg:bottom-0", dirty ? "translate-y-0" : "pointer-events-none translate-y-[200%]")}>
          <div className="mx-auto flex max-w-6xl items-center gap-2">
            <div className="min-w-0 flex-1 text-sm">
              <p className="font-bold text-slate-800">Alterações não salvas</p>
              {issues.length > 0 ? (
                <p className="truncate text-xs font-semibold text-rose-600" title={issues.join("\n")}>{issues.length} problema(s): {issues[0]}</p>
              ) : (
                <p className="hidden text-xs text-slate-500 sm:block">Ctrl+S para salvar</p>
              )}
            </div>
            <Button onClick={() => { setCfg(JSON.parse(saved)); setResult(null); }} variant="ghost" disabled={saving}>
              <Undo2 className="size-4" /> <span className="hidden sm:inline">Descartar</span>
            </Button>
            <Button onClick={save} variant="primary" loading={saving} size="lg">
              {!saving && <Save className="size-4" />} Salvar
            </Button>
          </div>
        </div>
      </div>
    </EditorContext.Provider>
  );
}
