// Gera o PDF final: capa + miolo (com cabeçalho, rodapé e sumário numerado em duas passadas).
// Uso: node build.js   (requer playwright e python3 com pypdf)
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const DIR = __dirname;
const OUT = path.join(DIR, '..', 'pdf');
const FINAL = path.join(OUT, 'Caderno-Simplificado_Caderno-06_Direito-Penal-Parte-Especial.pdf');
const TMP = path.join(DIR, '.build'); fs.mkdirSync(TMP, { recursive: true }); fs.mkdirSync(OUT, { recursive: true });

const header = `<div style="width:100%;font-family:Inter,sans-serif;font-size:7.5pt;color:#5b6475;padding:0 16mm;display:flex;justify-content:space-between;letter-spacing:.8pt;">
  <span><b style="color:#1b2333">CADERNO SIMPLIFICADO</b> · DIREITO PENAL</span><span>CADERNO 06 · PARTE ESPECIAL · 1ª EDIÇÃO</span></div>`;
const footer = `<div style="width:100%;font-family:Inter,sans-serif;font-size:7.5pt;color:#5b6475;padding:0 16mm;display:flex;justify-content:space-between;align-items:center;">
  <span>O que realmente cai na prova · Atualizado em 25/11/2026</span>
  <span style="background:#1d2129;color:#fff;font-weight:800;border-radius:4px;padding:2px 8px;font-size:8pt;"><span class="pageNumber"></span></span></div>`;

async function renderBody(page, toc) {
  await page.goto('file://' + path.join(DIR, 'miolo.html'), { waitUntil: 'networkidle' });
  if (toc) await page.evaluate(t => { document.querySelectorAll('[data-pg]').forEach(e => { e.textContent = t[e.dataset.pg] || ''; }); }, toc);
  const file = path.join(TMP, 'miolo.pdf');
  await page.pdf({ path: file, format: 'A4', printBackground: true, displayHeaderFooter: true, headerTemplate: header, footerTemplate: footer, preferCSSPageSize: true });
  return file;
}

(async () => {
  execFileSync('python3', [path.join(DIR, 'gerar.py')], { stdio: 'inherit' });
  const browser = await chromium.launch();
  const page = await browser.newPage();
  // passada 1: descobrir em que página começa cada capítulo
  let body = await renderBody(page, null);
  const toc = JSON.parse(execFileSync('python3', ['-I', '-c', `
import sys,json,re
from pypdf import PdfReader
r=PdfReader(sys.argv[1]); out={}
for i,p in enumerate(r.pages):
    for m in re.findall(r'§§([AUR][A-Z]?\\d+)§§', p.extract_text() or ''):
        out.setdefault(m, str(i+1))
print(json.dumps(out))`, body]).toString());
  console.log('Sumário:', toc);
  // controle de qualidade: cada bloco deve caber em uma página (marcadores P001...)
  const qc = JSON.parse(execFileSync('python3', ['-I', '-c', `
import sys,json,re
from pypdf import PdfReader
r=PdfReader(sys.argv[1]); bad=[]
for i,p in enumerate(r.pages):
    if not re.search(r'§§P\\d{3}§§', p.extract_text() or ''): bad.append(i+1)
print(json.dumps({'paginas':len(r.pages),'sem_marcador':bad}))`, body]).toString());
  console.log('QC:', qc);
  // passada 2: com números de página
  body = await renderBody(page, toc);
  await page.goto('file://' + path.join(DIR, 'capa.html'), { waitUntil: 'networkidle' });
  const capa = path.join(TMP, 'capa.pdf');
  await page.pdf({ path: capa, width: '210mm', height: '297mm', printBackground: true, pageRanges: '1' });
  await browser.close();
  execFileSync('python3', ['-I', '-c', `
import sys
from pypdf import PdfWriter
w=PdfWriter()
for f in sys.argv[2:]: w.append(f)
w.add_metadata({'/Title':'Caderno Simplificado — Caderno 06: Direito Penal — Parte Especial','/Subject':'Direito Penal, Parte Especial: crimes contra a pessoa, o patrimônio e a Administração Pública, para concursos','/Keywords':'direito constitucional, concursos, CF/88, direito penal, parte especial, homicídio, feminicídio, lesão corporal, honra, furto, roubo, extorsão, estelionato, peculato'})
w.write(sys.argv[1])`, FINAL, capa, body]);
  console.log('OK ->', FINAL);
})();
