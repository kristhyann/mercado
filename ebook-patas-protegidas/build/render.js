// Renderiza um HTML paginado (Paged.js) em PDF usando o Chromium do Playwright.
// Uso: node build/render.js build/ebook.html saida/arquivo.pdf
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const http = require('http');

const RAIZ = path.resolve(__dirname, '..');
const TIPOS = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript',
  '.jpg': 'image/jpeg', '.png': 'image/png', '.svg': 'image/svg+xml', '.woff2': 'font/woff2' };

function servidor() {
  return new Promise(res => {
    const srv = http.createServer((req, resp) => {
      const arq = path.join(RAIZ, decodeURIComponent(req.url.split('?')[0]));
      if (!arq.startsWith(RAIZ) || !fs.existsSync(arq)) { resp.writeHead(404); return resp.end(); }
      resp.writeHead(200, { 'Content-Type': TIPOS[path.extname(arq)] || 'application/octet-stream' });
      fs.createReadStream(arq).pipe(resp);
    });
    srv.listen(0, '127.0.0.1', () => res(srv));
  });
}

const PAGED = process.env.PAGED_JS ||
  path.join(__dirname, 'vendor', 'paged.polyfill.js');

(async () => {
  const [entrada, saida] = process.argv.slice(2);
  const srv = await servidor();
  const url = `http://127.0.0.1:${srv.address().port}/` + path.relative(RAIZ, path.resolve(entrada));
  const browser = await chromium.launch();
  const page = await browser.newPage();
  page.on('console', m => { if (m.type() === 'error') console.log('[console]', m.text()); });
  page.on('pageerror', e => console.log('[pageerror]', e.message));
  await page.goto(url, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.evaluate(() => { window.PagedConfig = { auto: false }; });
  await page.addScriptTag({ path: PAGED });
  const n = await page.evaluate(async () => {
    const flow = await window.PagedPolyfill.preview();
    return flow.total;
  });
  console.log('Páginas:', n);
  // checa estouro de conteúdo em cada página
  const estouros = await page.evaluate(() => {
    const r = [];
    document.querySelectorAll('.pagedjs_page').forEach((p, i) => {
      const area = p.querySelector('.pagedjs_page_content');
      if (area && area.scrollHeight > area.clientHeight + 2) r.push(i + 1);
    });
    return r;
  });
  if (estouros.length) console.log('Páginas com possível estouro:', estouros.join(', '));
  await page.pdf({ path: saida, preferCSSPageSize: true, printBackground: true, outline: false, tagged: true });
  await browser.close();
  srv.close();
  console.log('PDF gerado:', saida, (fs.statSync(saida).size / 1e6).toFixed(1) + ' MB');
})();
