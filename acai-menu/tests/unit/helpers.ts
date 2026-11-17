import fs from "node:fs";
import path from "node:path";
import { parseStoreOrThrow, findProduct } from "@/lib/menu";

export function loadMenu(slug: string) {
  const raw = JSON.parse(fs.readFileSync(path.resolve(__dirname, "../../stores", slug, "store.json"), "utf8"));
  return parseStoreOrThrow(raw);
}
export function product(slug: string, key: string) {
  const p = findProduct(loadMenu(slug), key);
  if (!p) throw new Error(`produto ${key} não encontrado`);
  return p;
}
