const { chromium } = require('playwright'); const http = require('http'); const fs = require('fs'); const path = require('path');
const ROOT = '/home/user/mercado/videos';
const srv = http.createServer((q, s) => { const p = path.join(ROOT, decodeURIComponent(q.url.split('?')[0])); fs.readFile(p, (e, d) => { if (e) { s.writeHead(404); s.end(); return; } s.writeHead(200, { 'Content-Type': p.endsWith('.js') ? 'text/javascript' : p.endsWith('.html') ? 'text/html' : 'application/octet-stream' }); s.end(d); }); }).listen(8797, async () => {
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const pg = await b.newPage({ viewport: { width: 1080, height: 1920 } }); await pg.goto('http://localhost:8797/macaco-prego/scene.html'); await pg.waitForFunction('window.ready');
  for (const t of process.argv.slice(2)) { await pg.evaluate(t => { draw(+t); document.querySelectorAll('.o').forEach(e => e.style.opacity = 0); }, t); await pg.screenshot({ path: `/tmp/claude-0/capa_${t}.png` }); }
  await b.close(); srv.close();
});
