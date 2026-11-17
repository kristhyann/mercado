/**
 * Prepara o JSON enviado para admin_sync_store(): configuração validada,
 * com a herança de produtos ("extends") já resolvida.
 */
import { resolveExtends } from "./menu";
import type { StoreConfig } from "./schema";

export function toSyncPayload(config: StoreConfig) {
  const issues: string[] = [];
  const products = resolveExtends(config.products, issues).map((p) => {
    const { extends: _ignored, ...rest } = p;
    return rest;
  });
  if (issues.length) throw new Error(issues.join("\n"));
  const { $schema: _s, ...rest } = config;
  return { ...rest, products };
}
