import type { CSSProperties } from "react";

function rgb(hex: string): [number, number, number] {
  const n = parseInt(hex.replace("#", ""), 16);
  return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
}
function toHex([r, g, b]: number[]) {
  return "#" + [r, g, b].map((v) => Math.round(Math.max(0, Math.min(255, v))).toString(16).padStart(2, "0")).join("");
}
export function mix(a: string, b: string, t: number) {
  const A = rgb(a), B = rgb(b);
  return toHex(A.map((v, i) => v + (B[i] - v) * t));
}
function luminance(hex: string) {
  const [r, g, b] = rgb(hex).map((v) => {
    const c = v / 255;
    return c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4;
  });
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}
export function contrastText(hex: string) {
  return luminance(hex) > 0.45 ? "#1c1022" : "#ffffff";
}

/** Variáveis CSS aplicadas no cardápio de cada loja (identidade visual própria). */
export function brandStyle(primary: string, secondary: string): CSSProperties {
  // Garante legibilidade de textos na cor principal sobre fundo claro.
  const brand = luminance(primary) > 0.35 ? mix(primary, "#000000", 0.35) : primary;
  return {
    "--brand": brand,
    "--brand-strong": mix(brand, "#000000", 0.22),
    "--brand-soft": mix(brand, "#ffffff", 0.88),
    "--brand-softer": mix(brand, "#ffffff", 0.95),
    "--on-brand": contrastText(brand),
    "--accent": secondary,
    "--accent-soft": mix(secondary, "#ffffff", 0.85),
    "--on-accent": contrastText(secondary),
  } as CSSProperties;
}
