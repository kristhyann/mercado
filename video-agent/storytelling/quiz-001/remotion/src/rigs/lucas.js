// Ficha visual do Lucas em código: única fonte das cores e proporções (personagens/lucas.md)
export const LUCAS = {
  skin: '#A8714F', skinShade: '#7A4A30', skinLight: '#C98E66', lip: '#7E4734',
  hair: '#1E1714', hairFade: '#3A2B24',
  iris: '#3A2216', eyeWhite: '#F4EDE4',
  polo: '#2F6E73', poloShade: '#1F4D52', poloLight: '#4A8F92', collarTrim: '#CFE3DF',
  tee: '#8C96A3', teeShade: '#646E7C', teeLight: '#AEB7C2',
  jeans: '#33415C', jeansShade: '#232E44', shorts: '#22262E', shortsShade: '#15181E',
  shoe: '#F2F0EA', shoeShade: '#C9C5BC', shoeStripe: '#E8743B',
  bag: '#23304F', bagShade: '#162038',
};

// expressions: brow raise, browIn (+ = inner up / sad, - = frown), lid droop, smile (-1..1), open (0..1)
export const EXPR = {
  neutro: {brow: 0, browIn: 0, lid: 0.12, smile: 0, open: 0},
  cansado: {brow: -0.1, browIn: 0.15, lid: 0.38, smile: -0.15, open: 0},
  abatido: {brow: 0.1, browIn: 0.85, lid: 0.45, smile: -0.7, open: 0},
  desejo: {brow: 0.45, browIn: 0.35, lid: 0.05, smile: 0.05, open: 0.25},
  focado: {brow: -0.25, browIn: -0.25, lid: 0.28, smile: -0.05, open: 0},
  determinado: {brow: -0.45, browIn: -0.75, lid: 0.18, smile: -0.2, open: 0},
  esforco: {brow: -0.3, browIn: -0.6, lid: 0.35, smile: -0.35, open: 0.35},
  esperanca: {brow: 0.4, browIn: 0.15, lid: 0, smile: 0.45, open: 0.1},
  assustado: {brow: 0.95, browIn: 0.7, lid: -0.12, smile: -0.35, open: 0.55},
  perdido: {brow: 0.5, browIn: 0.6, lid: 0.15, smile: -0.25, open: 0.1},
  distraido: {brow: 0.1, browIn: 0.1, lid: 0.3, smile: 0.1, open: 0},
  confiante: {brow: 0.05, browIn: -0.15, lid: 0.12, smile: 0.6, open: 0},
};

export const mixExpr = (a, b, x) => {
  const A = typeof a === 'string' ? EXPR[a] : a, B = typeof b === 'string' ? EXPR[b] : b;
  const o = {};
  for (const k of Object.keys(A)) o[k] = A[k] + (B[k] - A[k]) * x;
  return o;
};

export const DIEGO = {
  skin: '#D9A47E', skinShade: '#A8724F', skinLight: '#EDC09C', lip: '#A0584A',
  hair: '#3B2A20', hairFade: '#3B2A20', stubble: 0,
  polo: '#B5463C', poloShade: '#85302A', poloLight: '#D06A5E', collarTrim: '#F2EDE4',
  tee: '#B5463C', teeShade: '#85302A', teeLight: '#D06A5E',
};

export const PROFESSORA = {
  skin: '#8A5A3C', skinShade: '#64402A', skinLight: '#A8724F', lip: '#7A3A34',
  hair: '#24170F', hairFade: '#24170F', stubble: 0,
  polo: '#6B4C8A', poloShade: '#4D356A', poloLight: '#8A6AAA', collarTrim: '#F2EDE4',
  tee: '#6B4C8A', teeShade: '#4D356A', teeLight: '#8A6AAA',
};
