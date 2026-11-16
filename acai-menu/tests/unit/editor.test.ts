import { describe, expect, it } from "vitest";
import { duplicateProduct, imageRefs, move, parseMoney, removeGroupEverywhere, sizeNames, slugify, uniqueKey } from "@/lib/admin/editor";
import { storeConfigSchema } from "@/lib/schema";
import { parseStore } from "@/lib/menu";
import fs from "node:fs";
import path from "node:path";

const cfg = storeConfigSchema.parse(JSON.parse(fs.readFileSync(path.resolve(__dirname, "../../stores/acai-da-maria/store.json"), "utf8")));

describe("utilitários do painel", () => {
  it("gera chaves únicas a partir do nome", () => {
    expect(slugify("Açaí com Paçoca!")).toBe("acai-com-pacoca");
    expect(uniqueKey("Açaí", ["acai", "acai-2"])).toBe("acai-3");
  });
  it("move itens na lista", () => {
    expect(move([1, 2, 3], 0, 1)).toEqual([2, 1, 3]);
    expect(move([1, 2, 3], 0, -1)).toEqual([1, 2, 3]);
  });
  it("duplica produto logo abaixo, com chave nova, e a loja continua válida", () => {
    const out = duplicateProduct(cfg.products, "acai-tradicional");
    const i = out.findIndex((p) => p.key === "acai-tradicional");
    expect(out[i + 1].key).toBe("acai-tradicional-copia");
    expect(out[i + 1].name).toBe("Açaí tradicional (cópia)");
    expect(parseStore({ ...cfg, products: out }, { strict: true }).issues.filter((x) => !x.startsWith("aviso"))).toEqual([]);
  });
  it("excluir grupo remove dos produtos e das regras por tamanho", () => {
    const out = removeGroupEverywhere(cfg.products, "acompanhamentos");
    const monte = out.find((p) => p.key === "monte-seu-acai")!;
    expect(JSON.stringify({ g: monte.addonGroups, v: monte.variants })).not.toContain("acompanhamentos");
    expect(parseStore({ ...cfg, addonGroups: cfg.addonGroups.filter((g) => g.key !== "acompanhamentos"), products: out }).issues).toEqual([]);
  });
  it("lista tamanhos e imagens usadas; converte dinheiro", () => {
    expect(sizeNames(cfg.products).slice(0, 5)).toEqual(["300 ml", "400 ml", "500 ml", "700 ml", "1 litro"]);
    expect(imageRefs(cfg)).toContain("images/logo.svg");
    expect(parseMoney("19,90")).toBe(19.9);
    expect(parseMoney("1.234,5")).toBe(1234.5);
    expect(parseMoney("abc")).toBeNull();
  });
});
