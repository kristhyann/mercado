/**
 * Gera as ilustrações (SVG) das LOJAS DE DEMONSTRAÇÃO.
 * Lojas reais devem usar fotografias próprias (JPG/WebP) — veja o README.
 *
 *   npm run demo:images
 */
import fs from "node:fs";
import path from "node:path";

type Topping =
  | "strawberry" | "banana" | "granola" | "kiwi" | "nutella" | "condensed" | "ninho" | "pacoca"
  | "chocolate" | "mango" | "pineapple" | "coconut" | "blueberry" | "pistachio" | "kitkat" | "cream" | "honey" | "grape";
type Kind = "cup" | "bowl" | "barca" | "can" | "bottle" | "coconut" | "combo" | "duo" | "family" | "jar" | "scoop" | "mousse" | "glass" | "promo";

interface Recipe { kind: Kind; toppings?: Topping[]; tint?: string; label?: string; base?: string }

const RECIPES: Record<string, Recipe> = {
  "monte-seu-acai": { kind: "cup", toppings: ["strawberry", "banana", "granola", "condensed"] },
  "promo": { kind: "promo", toppings: ["strawberry", "kiwi", "granola", "condensed"] },
  "combo-bebida": { kind: "combo", toppings: ["banana", "granola", "condensed"], tint: "#dc2626" },
  "combo-dupla": { kind: "duo", toppings: ["strawberry", "ninho", "nutella"] },
  "combo-familia": { kind: "family", toppings: ["strawberry", "banana", "kiwi", "granola", "condensed"] },
  "acai-tradicional": { kind: "cup", toppings: ["granola", "banana"] },
  "acai-morango": { kind: "cup", toppings: ["strawberry", "condensed"] },
  "acai-nutella": { kind: "cup", toppings: ["nutella", "strawberry"] },
  "acai-ninho": { kind: "cup", toppings: ["ninho", "cream"] },
  "acai-banana": { kind: "cup", toppings: ["banana", "granola", "honey"] },
  "acai-pacoca": { kind: "cup", toppings: ["pacoca", "condensed"] },
  "acai-premium": { kind: "bowl", toppings: ["strawberry", "kitkat", "nutella", "ninho", "pistachio"] },
  "acai-especial": { kind: "bowl", toppings: ["banana", "strawberry", "granola", "honey", "cream"] },
  "acai-fit": { kind: "bowl", toppings: ["banana", "strawberry", "granola", "blueberry"] },
  "acai-havaiano": { kind: "bowl", toppings: ["pineapple", "mango", "coconut", "honey"] },
  "copo-ninho": { kind: "glass", toppings: ["ninho"], base: "#f8fafc" },
  "copo-nutella": { kind: "glass", toppings: ["nutella", "strawberry"], base: "#5b3a29" },
  "copo-morango": { kind: "glass", toppings: ["strawberry"], base: "#fbcfe8" },
  "copo-chocolate": { kind: "glass", toppings: ["chocolate", "kitkat"], base: "#78350f" },
  "tigela": { kind: "bowl", toppings: ["banana", "granola", "strawberry", "condensed"] },
  "barca": { kind: "barca", toppings: ["strawberry", "banana", "kiwi", "granola", "condensed", "grape"] },
  "cupuacu": { kind: "cup", toppings: ["condensed"], base: "#fde68a" },
  "sorvete": { kind: "scoop" },
  "mousse": { kind: "mousse" },
  "nutella": { kind: "jar", tint: "#5b3a29", label: "50g" },
  "leite-po": { kind: "jar", tint: "#f8fafc", label: "50g" },
  "refri": { kind: "can", tint: "#dc2626" },
  "guarana": { kind: "can", tint: "#16a34a" },
  "agua": { kind: "bottle", tint: "#38bdf8" },
  "suco": { kind: "glass", base: "#fb923c", toppings: [] },
  "agua-coco": { kind: "coconut" },
};

const STORE_IMAGES: Record<string, string[]> = {
  "acai-da-maria": Object.keys(RECIPES).filter((k) => !["acai-fit", "acai-havaiano", "agua-coco"].includes(k)),
  "acai-tropical": ["monte-seu-acai", "acai-fit", "acai-havaiano", "barca", "agua-coco", "suco"],
  "acai-premium": ["acai-premium", "acai-nutella", "monte-seu-acai", "mousse", "sorvete"],
};

// ─── utilidades ────────────────────────────────────────────────────────────
function hexToRgb(hex: string) {
  const n = parseInt(hex.slice(1), 16);
  return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
}
function mix(a: string, b: string, t: number) {
  const A = hexToRgb(a), B = hexToRgb(b);
  return "#" + A.map((v, i) => Math.round(v + (B[i] - v) * t).toString(16).padStart(2, "0")).join("");
}
let seed = 1;
const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647);
const r = (min: number, max: number) => min + rnd() * (max - min);

const ACAI = "#4a1259";
const ACAI_LIGHT = "#6d1f7f";

function toppingsSvg(list: Topping[], cx: number, cy: number, rx: number, ry: number): string {
  let out = "";
  const spots = (n: number, fn: (x: number, y: number, i: number) => string) => {
    for (let i = 0; i < n; i++) {
      const a = r(0, Math.PI * 2), d = Math.sqrt(rnd());
      out += fn(cx + Math.cos(a) * rx * d * 0.85, cy + Math.sin(a) * ry * d * 0.75, i);
    }
  };
  list.forEach((t, idx) => {
    const sector = (fn: (x: number, y: number, i: number) => string, n: number) => {
      // concentra cada cobertura em uma região, como numa foto real
      const a0 = (idx / Math.max(list.length, 1)) * Math.PI * 2;
      for (let i = 0; i < n; i++) {
        const a = a0 + r(-0.7, 0.7), d = r(0.25, 0.95);
        out += fn(cx + Math.cos(a) * rx * d * 0.82, cy + Math.sin(a) * ry * d * 0.7, i);
      }
    };
    switch (t) {
      case "strawberry":
        sector((x, y) => `<g transform="translate(${x} ${y}) rotate(${r(-40, 40)})"><path d="M0 -16 C14 -16 18 2 0 18 C-18 2 -14 -16 0 -16Z" fill="#e11d48"/><path d="M0 -10 C8 -10 10 2 0 12 C-10 2 -8 -10 0 -10Z" fill="#fb7185" opacity=".7"/><path d="M-7 -15 L0 -22 L7 -15 L0 -12Z" fill="#16a34a"/></g>`, 5);
        break;
      case "banana":
        sector((x, y) => `<g transform="translate(${x} ${y})"><circle r="13" fill="#fde68a"/><circle r="9" fill="#fef3c7"/><circle r="2" fill="#a16207" opacity=".5"/></g>`, 5);
        break;
      case "kiwi":
        sector((x, y) => `<g transform="translate(${x} ${y})"><circle r="14" fill="#65a30d"/><circle r="11" fill="#a3e635"/><circle r="4" fill="#f7fee7"/>${[0, 1, 2, 3, 4, 5].map((k) => `<circle cx="${Math.cos(k) * 7}" cy="${Math.sin(k) * 7}" r="1.2" fill="#1a2e05"/>`).join("")}</g>`, 3);
        break;
      case "granola":
        sector((x, y) => `<rect x="${x}" y="${y}" width="${r(5, 10)}" height="${r(4, 7)}" rx="2" fill="${["#b45309", "#d97706", "#92400e"][Math.floor(r(0, 3))]}" transform="rotate(${r(0, 90)} ${x} ${y})"/>`, 26);
        break;
      case "pacoca":
        sector((x, y) => `<circle cx="${x}" cy="${y}" r="${r(3, 7)}" fill="#d6a565"/>`, 22);
        break;
      case "ninho":
        spots(70, (x, y) => `<circle cx="${x}" cy="${y}" r="${r(1.5, 4)}" fill="#fffdf7" opacity=".95"/>`);
        break;
      case "coconut":
        sector((x, y) => `<rect x="${x}" y="${y}" width="10" height="3" rx="1.5" fill="#fff" transform="rotate(${r(0, 180)} ${x} ${y})"/>`, 28);
        break;
      case "blueberry":
        sector((x, y) => `<circle cx="${x}" cy="${y}" r="7" fill="#312e81"/><circle cx="${x - 2}" cy="${y - 2}" r="2" fill="#818cf8"/>`, 7);
        break;
      case "grape":
        sector((x, y) => `<circle cx="${x}" cy="${y}" r="8" fill="#16a34a"/><circle cx="${x - 2}" cy="${y - 3}" r="2.5" fill="#86efac"/>`, 4);
        break;
      case "pistachio":
        sector((x, y) => `<ellipse cx="${x}" cy="${y}" rx="5" ry="3.5" fill="#84cc16" transform="rotate(${r(0, 180)} ${x} ${y})"/>`, 14);
        break;
      case "mango":
        sector((x, y) => `<rect x="${x}" y="${y}" width="14" height="14" rx="3" fill="#f59e0b" transform="rotate(${r(0, 90)} ${x} ${y})"/><rect x="${x + 2}" y="${y + 2}" width="6" height="6" rx="2" fill="#fcd34d"/>`, 5);
        break;
      case "pineapple":
        sector((x, y) => `<path d="M${x} ${y} l14 0 l-7 -14z" fill="#facc15" stroke="#eab308" stroke-width="1"/>`, 6);
        break;
      case "kitkat":
        sector((x, y) => `<g transform="translate(${x} ${y}) rotate(${r(-60, 60)})"><rect x="-6" y="-22" width="12" height="40" rx="2" fill="#7c2d12"/><rect x="-6" y="-22" width="12" height="40" rx="2" fill="none" stroke="#9a3412"/><line x1="-6" y1="-8" x2="6" y2="-8" stroke="#431407"/><line x1="-6" y1="6" x2="6" y2="6" stroke="#431407"/></g>`, 2);
        break;
      case "chocolate":
        sector((x, y) => `<rect x="${x}" y="${y}" width="4" height="9" rx="2" fill="${["#ef4444", "#facc15", "#22c55e", "#3b82f6", "#f97316"][Math.floor(r(0, 5))]}" transform="rotate(${r(0, 180)} ${x} ${y})"/>`, 26);
        break;
      case "cream":
        out += `<path d="M${cx - rx * 0.35} ${cy - 4} q${rx * 0.12} -22 ${rx * 0.25} -4 q${rx * 0.12} -20 ${rx * 0.25} 2 q-${rx * 0.25} 16 -${rx * 0.5} 2z" fill="#fff7ed" stroke="#fde7cf"/>`;
        break;
      case "nutella":
      case "condensed":
      case "honey": {
        const color = t === "nutella" ? "#5b2c16" : t === "honey" ? "#f59e0b" : "#fffaf0";
        let d = `M${cx - rx * 0.8} ${cy - ry * 0.2}`;
        for (let i = 0; i < 6; i++) d += ` Q${cx - rx * 0.8 + (i + 0.5) * rx * 0.28} ${cy + (i % 2 ? -1 : 1) * ry * 0.6} ${cx - rx * 0.8 + (i + 1) * rx * 0.28} ${cy - ry * 0.2 + r(-8, 8)}`;
        out += `<path d="${d}" fill="none" stroke="${color}" stroke-width="${t === "nutella" ? 7 : 6}" stroke-linecap="round" opacity=".95"/>`;
        break;
      }
    }
  });
  return out;
}

function acaiTop(cx: number, cy: number, rx: number, ry: number, base = ACAI) {
  return `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="${base}"/>
  <ellipse cx="${cx}" cy="${cy - ry * 0.55}" rx="${rx * 0.94}" ry="${ry * 1.45}" fill="${base}"/>
  <ellipse cx="${cx - rx * 0.2}" cy="${cy - ry * 0.25}" rx="${rx * 0.55}" ry="${ry * 0.45}" fill="${base === ACAI ? ACAI_LIGHT : mix(base, "#ffffff", 0.25)}" opacity=".6"/>`;
}

function cup(cx: number, bottom: number, w: number, h: number, t: Topping[], base = ACAI) {
  const top = bottom - h, tw = w / 2, bw = w * 0.36;
  return `<path d="M${cx - tw} ${top} L${cx - bw} ${bottom} Q${cx} ${bottom + 10} ${cx + bw} ${bottom} L${cx + tw} ${top}Z" fill="${base}"/>
  <path d="M${cx - tw * 0.92} ${top + h * 0.35} L${cx + tw * 0.92} ${top + h * 0.35}" stroke="#ffffff" stroke-opacity=".12" stroke-width="10"/>
  <path d="M${cx - tw + 8} ${top + 6} L${cx - bw + 6} ${bottom - 6}" stroke="#fff" stroke-opacity=".35" stroke-width="8" stroke-linecap="round"/>
  ${acaiTop(cx, top, tw, tw * 0.28, base)}
  <g>${toppingsSvg(t, cx, top - tw * 0.28, tw * 0.95, tw * 0.62)}</g>
  <path d="M${cx - tw - 4} ${top} L${cx - bw - 2} ${bottom + 2} Q${cx} ${bottom + 14} ${cx + bw + 2} ${bottom + 2} L${cx + tw + 4} ${top}" fill="none" stroke="#ffffff" stroke-opacity=".55" stroke-width="4"/>`;
}

function bowl(cx: number, cy: number, w: number, t: Topping[], color = "#f5f5f4", base = ACAI) {
  const rw = w / 2;
  return `<ellipse cx="${cx}" cy="${cy + rw * 0.62}" rx="${rw * 0.5}" ry="${rw * 0.08}" fill="#000" opacity=".12"/>
  <path d="M${cx - rw} ${cy} Q${cx - rw} ${cy + rw * 0.65} ${cx} ${cy + rw * 0.62} Q${cx + rw} ${cy + rw * 0.65} ${cx + rw} ${cy}Z" fill="${color}"/>
  <path d="M${cx - rw * 0.8} ${cy + rw * 0.18} Q${cx} ${cy + rw * 0.5} ${cx + rw * 0.8} ${cy + rw * 0.18}" stroke="#000" stroke-opacity=".06" stroke-width="10" fill="none"/>
  ${acaiTop(cx, cy, rw, rw * 0.3, base)}
  <g>${toppingsSvg(t, cx, cy - rw * 0.2, rw * 0.95, rw * 0.5)}</g>`;
}

function illustration(recipe: Recipe, primary: string, secondary: string): string {
  const W = 800, H = 600;
  const bg1 = mix(primary, "#ffffff", 0.9), bg2 = mix(secondary, "#ffffff", 0.82);
  let body = "";
  const t = recipe.toppings ?? [];
  switch (recipe.kind) {
    case "cup": body = cup(400, 500, 300, 300, t, recipe.base); break;
    case "promo": body = cup(400, 500, 300, 300, t) + `<g transform="translate(600 140) rotate(12)"><circle r="78" fill="${secondary}"/><circle r="66" fill="none" stroke="#fff" stroke-dasharray="6 6" stroke-width="3"/><text y="14" text-anchor="middle" font-family="Arial, sans-serif" font-weight="900" font-size="44" fill="#fff">%</text></g>`; break;
    case "bowl": body = bowl(400, 330, 440, t, "#fafaf9"); break;
    case "glass": {
      const base = recipe.base ?? ACAI;
      body = `<rect x="300" y="170" width="200" height="320" rx="26" fill="#ffffff" opacity=".55"/>
      <rect x="312" y="300" width="176" height="180" rx="20" fill="${ACAI}"/>
      <rect x="312" y="250" width="176" height="60" fill="${base}"/>
      <rect x="312" y="215" width="176" height="40" fill="${ACAI_LIGHT}"/>
      <g>${toppingsSvg(t, 400, 205, 88, 24)}</g>
      <rect x="300" y="170" width="200" height="320" rx="26" fill="none" stroke="#fff" stroke-width="6" opacity=".8"/>
      <rect x="320" y="185" width="14" height="280" rx="7" fill="#fff" opacity=".45"/>`;
      break;
    }
    case "barca": {
      body = `<ellipse cx="400" cy="480" rx="280" ry="22" fill="#000" opacity=".1"/>
      <path d="M90 300 Q400 330 710 300 L640 450 Q400 490 160 450Z" fill="#a16207"/>
      <path d="M90 300 Q400 330 710 300 L700 322 Q400 352 100 322Z" fill="#ca8a04"/>
      ${[0, 1, 2].map((i) => `<ellipse cx="${250 + i * 150}" cy="300" rx="95" ry="34" fill="${ACAI}"/><ellipse cx="${235 + i * 150}" cy="292" rx="50" ry="14" fill="${ACAI_LIGHT}" opacity=".6"/>`).join("")}
      <g>${toppingsSvg(t, 400, 286, 300, 50)}</g>`;
      break;
    }
    case "combo": body = cup(330, 510, 260, 280, t) + can(580, 510, recipe.tint ?? "#dc2626", 0.8); break;
    case "duo": body = cup(280, 510, 230, 250, t) + cup(530, 520, 230, 250, [...t].reverse()); break;
    case "family": body = bowl(400, 300, 400, t) + cup(170, 520, 150, 160, t.slice(0, 2)) + cup(630, 520, 150, 160, t.slice(1, 3)); break;
    case "can": body = can(400, 500, recipe.tint ?? "#dc2626", 1.2); break;
    case "bottle":
      body = `<rect x="350" y="120" width="100" height="40" rx="10" fill="#0ea5e9"/><path d="M340 170 Q340 150 360 150 L440 150 Q460 150 460 170 L470 230 L470 480 Q470 510 440 510 L360 510 Q330 510 330 480 L330 230Z" fill="#bae6fd" opacity=".85"/><rect x="330" y="300" width="140" height="90" fill="${recipe.tint ?? "#38bdf8"}"/><rect x="350" y="180" width="16" height="300" rx="8" fill="#fff" opacity=".6"/>`;
      break;
    case "coconut":
      body = `<circle cx="400" cy="330" r="170" fill="#65a30d"/><circle cx="400" cy="330" r="150" fill="#84cc16"/><ellipse cx="400" cy="230" rx="90" ry="34" fill="#fefce8"/><rect x="430" y="80" width="14" height="170" rx="7" fill="${secondary}" transform="rotate(16 437 165)"/>`;
      break;
    case "jar":
      body = `<rect x="300" y="170" width="200" height="50" rx="12" fill="${secondary}"/><rect x="290" y="210" width="220" height="280" rx="34" fill="${recipe.tint ?? "#5b3a29"}"/><rect x="310" y="290" width="180" height="110" rx="14" fill="#fff"/><text x="400" y="362" text-anchor="middle" font-family="Arial, sans-serif" font-weight="800" font-size="48" fill="${primary}">${recipe.label ?? ""}</text>`;
      break;
    case "scoop":
      body = `<path d="M300 330 L400 520 L500 330Z" fill="#d97706"/><path d="M300 330 L400 520 L500 330" fill="none" stroke="#92400e" stroke-width="3"/><circle cx="350" cy="290" r="70" fill="#fbcfe8"/><circle cx="450" cy="290" r="70" fill="#fde68a"/><circle cx="400" cy="220" r="70" fill="${ACAI_LIGHT}"/>`;
      break;
    case "mousse":
      body = `<path d="M290 220 L510 220 L480 470 Q400 500 320 470Z" fill="#fff" opacity=".6"/><path d="M300 300 L500 300 L480 465 Q400 495 320 465Z" fill="#fde047"/><path d="M296 260 L504 260 L500 300 L300 300Z" fill="#fef9c3"/><path d="M300 250 q100 -40 200 0" fill="none" stroke="#a16207" stroke-width="10" stroke-linecap="round"/><circle cx="360" cy="245" r="8" fill="#1c1917"/><circle cx="430" cy="240" r="8" fill="#1c1917"/>`;
      break;
  }
  seed = 7;
  const dots = Array.from({ length: 14 }, () => `<circle cx="${r(0, W)}" cy="${r(0, H)}" r="${r(6, 22)}" fill="${primary}" opacity="${r(0.04, 0.09).toFixed(2)}"/>`).join("");
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}">
<defs><radialGradient id="bg" cx="50%" cy="40%" r="75%"><stop offset="0" stop-color="#ffffff"/><stop offset=".55" stop-color="${bg1}"/><stop offset="1" stop-color="${bg2}"/></radialGradient></defs>
<rect width="${W}" height="${H}" fill="url(#bg)"/>${dots}
<ellipse cx="400" cy="560" rx="260" ry="22" fill="${primary}" opacity=".12"/>
<g transform="translate(400 330) scale(${recipe.kind === "barca" || recipe.kind === "family" || recipe.kind === "duo" ? 1.08 : 1.32}) translate(-400 -330)">${body}</g>
</svg>`;
}

function can(cx: number, bottom: number, color: string, s = 1) {
  const w = 120 * s, h = 220 * s, x = cx - w / 2, y = bottom - h;
  return `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${18 * s}" fill="${color}"/><rect x="${x + 6 * s}" y="${y - 10 * s}" width="${w - 12 * s}" height="${20 * s}" rx="${8 * s}" fill="#d4d4d8"/><rect x="${x + 14 * s}" y="${y + 20 * s}" width="${14 * s}" height="${h - 40 * s}" rx="${7 * s}" fill="#fff" opacity=".35"/><circle cx="${cx}" cy="${y + h * 0.5}" r="${30 * s}" fill="#fff" opacity=".9"/>`;
}

function initials(name: string) {
  const words = name.replace(/a[çc]a[íi]/gi, "").split(/\s+/).filter((w) => w.length > 2);
  return (words[0]?.[0] ?? name[0]).toUpperCase();
}

function logo(name: string, primary: string, secondary: string) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="${mix(primary, "#ffffff", 0.15)}"/><stop offset="1" stop-color="${mix(primary, "#000000", 0.25)}"/></linearGradient></defs>
<rect width="256" height="256" rx="64" fill="url(#g)"/>
<circle cx="190" cy="66" r="22" fill="${secondary}"/><path d="M190 44 q10 -16 24 -14" stroke="#22c55e" stroke-width="6" fill="none" stroke-linecap="round"/>
<text x="128" y="170" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif" font-weight="700" font-size="128" fill="#ffffff">${initials(name)}</text>
<text x="128" y="214" text-anchor="middle" font-family="Arial, sans-serif" font-weight="700" font-size="22" letter-spacing="5" fill="#ffffff" opacity=".85">AÇAÍ</text>
</svg>`;
}

function cover(primary: string, secondary: string) {
  seed = 11;
  const W = 1600, H = 640;
  const berries = Array.from({ length: 60 }, () => {
    const x = r(0, W), y = r(0, H), rr = r(10, 34);
    return `<circle cx="${x}" cy="${y}" r="${rr}" fill="${mix(primary, "#000000", r(0.1, 0.5))}" opacity=".5"/><circle cx="${x - rr / 3}" cy="${y - rr / 3}" r="${rr / 4}" fill="#fff" opacity=".18"/>`;
  }).join("");
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" preserveAspectRatio="xMidYMid slice">
<defs><linearGradient id="c" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="${mix(primary, "#000000", 0.35)}"/><stop offset=".6" stop-color="${primary}"/><stop offset="1" stop-color="${mix(primary, secondary, 0.45)}"/></linearGradient></defs>
<rect width="${W}" height="${H}" fill="url(#c)"/>${berries}
${[0, 1, 2, 3, 4].map((i) => `<path d="M${200 + i * 320} ${H} q60 -160 0 -320" stroke="#22c55e" stroke-opacity=".25" stroke-width="10" fill="none"/>`).join("")}
</svg>`;
}

function banner(primary: string, secondary: string) {
  seed = 3;
  const W = 1200, H = 480;
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}">
<defs><linearGradient id="b" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="${mix(primary, "#000000", 0.2)}"/><stop offset="1" stop-color="${mix(primary, secondary, 0.35)}"/></linearGradient></defs>
<rect width="${W}" height="${H}" fill="url(#b)"/>
<circle cx="980" cy="240" r="260" fill="#fff" opacity=".08"/><circle cx="980" cy="240" r="190" fill="#fff" opacity=".08"/>
<g transform="translate(400 -110) scale(1.25)">${bowl(440, 300, 420, ["strawberry", "banana", "kiwi", "granola", "condensed"], "#fafaf9")}</g>
</svg>`;
}

function main() {
  const root = path.resolve(__dirname, "..", "stores");
  for (const [slug, images] of Object.entries(STORE_IMAGES)) {
    const cfgPath = path.join(root, slug, "store.json");
    if (!fs.existsSync(cfgPath)) continue;
    const cfg = JSON.parse(fs.readFileSync(cfgPath, "utf8"));
    if (!cfg.isDemo) {
      console.log(`↷ ${slug}: não é demonstração, ignorado.`);
      continue;
    }
    const { primaryColor: p, secondaryColor: s } = cfg.branding;
    const dir = path.join(root, slug, "images");
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(path.join(dir, "logo.svg"), logo(cfg.name, p, s));
    fs.writeFileSync(path.join(dir, "cover.svg"), cover(p, s));
    fs.writeFileSync(path.join(dir, "banner.svg"), banner(p, s));
    for (const name of images) {
      seed = name.split("").reduce((a, c) => a + c.charCodeAt(0), 0) + 1;
      fs.writeFileSync(path.join(dir, `${name}.svg`), illustration(RECIPES[name], p, s));
    }
    console.log(`✓ ${slug}: ${images.length + 3} imagens`);
  }
}

main();
