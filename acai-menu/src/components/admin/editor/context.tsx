"use client";
import { createContext, useContext } from "react";
import type { StoreConfig } from "@/lib/schema";

export interface EditorCtx {
  cfg: StoreConfig;
  update: (fn: (draft: StoreConfig) => void) => void;
  slug: string;
  issues: string[];
}
export const EditorContext = createContext<EditorCtx | null>(null);
export function useEditor() {
  const c = useContext(EditorContext);
  if (!c) throw new Error("useEditor fora do editor");
  return c;
}
