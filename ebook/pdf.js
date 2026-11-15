const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage();
  await pg.goto('file://' + path.resolve('ebook.html'), { waitUntil: 'load' }); await pg.evaluate(() => document.fonts.ready);
  const over = await pg.evaluate(() => [...document.querySelectorAll('.page')].map((p, i) => { const inn = p.querySelector('.in'); const r = inn.getBoundingClientRect(); let maxB = 0; inn.querySelectorAll('*').forEach(e => { const b = e.getBoundingClientRect().bottom; if (b > maxB) maxB = b; }); return [i + 1, Math.round(maxB - r.bottom)]; }).filter(x => x[1] > 0));
  console.log('estouros:', JSON.stringify(over));
  await pg.pdf({ path: '100_TEMAS_VIRAIS.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  await b.close();
})();
