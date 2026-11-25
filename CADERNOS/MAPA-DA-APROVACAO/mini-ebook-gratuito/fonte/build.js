// Gera o PDF do Mini Guia Gratuito e verifica transbordo de conteúdo em cada página.
// Uso: node build.js
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const path = require('path');
const DIR = __dirname;
const OUT = path.join(DIR, '..', 'pdf', 'Mapa-da-Aprovacao_Mini-Guia-Gratuito_5-Assuntos-Simplificados.pdf');
(async () => {
  execFileSync('python3', [path.join(DIR, 'gerar.py')], { stdio: 'inherit' });
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.join(DIR, 'ebook.html'), { waitUntil: 'networkidle' });
  await page.emulateMedia({ media: 'print' });
  const qc = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll('.page').forEach((pg, i) => {
      const b = pg.querySelector('.body');
      if (b && b.scrollHeight > b.clientHeight + 1) out.push({ pagina: i + 1, excesso_px: b.scrollHeight - b.clientHeight });
      if (b) b.querySelectorAll('*').forEach(el => { if (el.scrollWidth > el.clientWidth + 2 && getComputedStyle(el).overflow === 'hidden' && el.tagName !== 'TABLE') out.push({ pagina: i + 1, largura: el.className || el.tagName }); });
    });
    return { paginas: document.querySelectorAll('.page').length, problemas: out };
  });
  console.log('QC:', JSON.stringify(qc));
  await page.pdf({ path: OUT, printBackground: true, preferCSSPageSize: true });
  await browser.close();
  execFileSync('python3', ['-I', '-c', `
import sys
from pypdf import PdfReader, PdfWriter
r=PdfReader(sys.argv[1]); w=PdfWriter()
for p in r.pages: w.add_page(p)
w.add_metadata({'/Title':'Mapa da Aprovação — Mini Guia Gratuito: 5 assuntos de concurso explicados de forma simplificada','/Author':'Mapa da Aprovação — Cadernos Simplificados para Concursos','/Subject':'Princípios fundamentais, art. 5º, princípios da Administração, conceito de crime e interpretação de texto'})
w.write(sys.argv[1]); print('páginas no PDF:', len(r.pages))`, OUT], { stdio: 'inherit' });
  console.log('OK ->', OUT);
})();
