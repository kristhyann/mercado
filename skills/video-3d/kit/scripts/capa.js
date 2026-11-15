// uso: node capa.js <pasta-do-video> <segundo> <saida.png>   (tira um quadro limpo, sem textos, para a capa)
const { chromium } = require('playwright'); const http = require('http'); const fs = require('fs'); const path = require('path');
const ROOT = path.resolve(__dirname, '..', '..'); const dir = path.resolve(process.argv[2]); const name = path.basename(dir); const t = +process.argv[3]; const outp = path.resolve(process.argv[4]);
const types = { '.js': 'text/javascript', '.html': 'text/html', '.json': 'application/json', '.woff2': 'font/woff2' };
const srv = http.createServer((q, s) => { const p = path.join(ROOT, decodeURIComponent(q.url.split('?')[0])); fs.readFile(p, (e, d) => { if (e) { s.writeHead(404); s.end(); return; } s.writeHead(200, { 'Content-Type': types[path.extname(p)] || 'application/octet-stream' }); s.end(d); }); });
srv.listen(0, async () => {
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const pg = await b.newPage({ viewport: { width: 1080, height: 1920 } }); await pg.goto(`http://localhost:${srv.address().port}/${name}/scene.html`); await pg.waitForFunction('window.ready', null, { timeout: 120000 });
  await pg.evaluate(async t => { await draw(t); document.querySelectorAll('.o').forEach(e => e.style.opacity = 0); }, t);
  await pg.screenshot({ path: outp }); await b.close(); srv.close(); console.log('capa', outp);
});
