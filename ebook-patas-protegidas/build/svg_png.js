// Exporta todas as ilustrações SVG para PNG (2x), com as fontes do e-book.
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
const RAIZ = path.resolve(__dirname, '..');
const DIR = path.join(RAIZ, 'imagens', 'ilustracoes');
const OUT = path.join(DIR, 'png');
fs.mkdirSync(OUT, { recursive: true });
const fonte = (w) => `@font-face{font-family:'Nunito Sans';font-weight:${w};src:url(data:font/woff2;base64,${fs.readFileSync(path.join(RAIZ, 'estilo/fontes/nunito-sans-latin-' + w + '-normal.woff2')).toString('base64')})}`;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ deviceScaleFactor: 2 });
  for (const f of fs.readdirSync(DIR).filter(f => f.endsWith('.svg'))) {
    const svg = fs.readFileSync(path.join(DIR, f), 'utf8');
    const m = svg.match(/viewBox='0 0 (\d+) (\d+)'/); const w = +m[1], h = +m[2];
    await p.setViewportSize({ width: w, height: h });
    await p.setContent(`<html><head><style>${fonte(600)}${fonte(700)}${fonte(800)}body{margin:0}svg{display:block;width:${w}px;height:${h}px}</style></head><body>${svg}</body></html>`);
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(OUT, f.replace('.svg', '.png')), omitBackground: true });
  }
  await b.close(); console.log('PNGs gerados em', OUT);
})();
