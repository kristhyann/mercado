// uso: node render.js <pasta-do-video> test t1,t2,...   |   node render.js <pasta> full <workers>
const { chromium } = require('playwright'); const http = require('http'); const fs = require('fs'); const path = require('path');
const ROOT = path.resolve(__dirname, '..'); const dir = process.argv[2]; const mode = process.argv[3];
const name = path.basename(path.resolve(dir));
const types = { '.js': 'text/javascript', '.html': 'text/html', '.json': 'application/json', '.woff2': 'font/woff2' };
const srv = http.createServer((q, s) => { const p = path.join(ROOT, decodeURIComponent(q.url.split('?')[0])); fs.readFile(p, (e, d) => { if (e) { s.writeHead(404); s.end(); return; } s.writeHead(200, { 'Content-Type': types[path.extname(p)] || 'application/octet-stream' }); s.end(d); }); });
srv.listen(0, async () => {
  const port = srv.address().port; const url = `http://localhost:${port}/${name}/scene.html`;
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const open = async () => { const pg = await b.newPage({ viewport: { width: 1080, height: 1920 } }); pg.on('console', m => { if (m.type() === 'error') console.log('ERR', m.text()); }); pg.on('pageerror', e => console.log('PAGEERR', e.message)); await pg.goto(url); await pg.waitForFunction('window.ready', null, { timeout: 120000 }); return pg; };
  if (mode === 'test') {
    const pg = await open(); const ts = process.argv[4].split(',').map(Number); const out = path.join(dir, 'teste'); fs.mkdirSync(out, { recursive: true });
    for (const t of ts) { await pg.evaluate(t => draw(t), t); await pg.screenshot({ path: path.join(out, `t_${t.toFixed(2).padStart(6, '0')}.jpg`), type: 'jpeg', quality: 80 }); }
    fs.writeFileSync(path.join(dir, 'eventos.json'), JSON.stringify(await pg.evaluate('window.EVENTS')));
  } else {
    const nw = +process.argv[4] || 3; const pg0 = await open(); const dur = await pg0.evaluate('window.DURATION');
    fs.writeFileSync(path.join(dir, 'eventos.json'), JSON.stringify(await pg0.evaluate('window.EVENTS')));
    const N = Math.ceil(dur * 30); const out = path.join(dir, 'quadros'); fs.mkdirSync(out, { recursive: true });
    const pages = [pg0]; for (let i = 1; i < nw; i++) pages.push(await open());
    let done = 0; const t0 = Date.now();
    await Promise.all(pages.map(async (pg, w) => {
      for (let f = w; f < N; f += nw) {
        const fp = path.join(out, `f_${String(f).padStart(5, '0')}.jpg`); if (fs.existsSync(fp)) { done++; continue; }
        await pg.evaluate(t => draw(t), f / 30); await pg.screenshot({ path: fp + '.tmp', type: 'jpeg', quality: 93 }); fs.renameSync(fp + '.tmp', fp);
        if (++done % 150 === 0) console.log(`${done}/${N} quadros  (${((Date.now() - t0) / 1000).toFixed(0)}s)`);
      }
    }));
    console.log('pronto', N);
  }
  await b.close(); srv.close();
});
