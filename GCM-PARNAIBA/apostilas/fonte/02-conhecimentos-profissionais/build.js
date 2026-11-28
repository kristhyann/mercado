// Gera o PDF de uma apostila: capa + miolo (cabeçalho, rodapé, sumário numerado em duas passadas e QC).
// Uso: node build.js   — lê config.json na mesma pasta (ver config.exemplo.json). Requer playwright e python3 com pypdf.
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const DIR = __dirname;
const CFG = JSON.parse(fs.readFileSync(path.join(DIR, 'config.json'), 'utf8'));
const OUT = path.resolve(DIR, process.env.OUT_DIR || CFG.saida || '..');
const FINAL = path.join(OUT, CFG.arquivo);
const TMP = path.join(DIR, '.build'); fs.mkdirSync(TMP, { recursive: true }); fs.mkdirSync(OUT, { recursive: true });
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');

const header = `<div style="width:100%;font-family:Inter,sans-serif;font-size:7.5pt;color:#5f6673;padding:0 16mm;display:flex;justify-content:space-between;letter-spacing:.8pt;">
  <span><b style="color:#0f1f3d">GCM PARNAÍBA</b> · ${esc(CFG.cab_esq)}</span><span>${esc(CFG.cab_dir)}</span></div>`;
const footer = `<div style="width:100%;font-family:Inter,sans-serif;font-size:7.5pt;color:#5f6673;padding:0 16mm;display:flex;justify-content:space-between;align-items:center;">
  <span>${esc(CFG.rodape)}</span>
  <span style="background:#0f1f3d;color:#e8b923;font-weight:800;border-radius:4px;padding:2px 8px;font-size:8pt;"><span class="pageNumber"></span></span></div>`;

async function renderBody(page, toc) {
  await page.goto('file://' + path.join(DIR, 'miolo.html'), { waitUntil: 'networkidle' });
  if (toc) await page.evaluate(t => { document.querySelectorAll('[data-pg]').forEach(e => { e.textContent = t[e.dataset.pg] || ''; }); }, toc);
  const file = path.join(TMP, 'miolo.pdf');
  await page.pdf({ path: file, format: 'A4', printBackground: true, displayHeaderFooter: true, headerTemplate: header, footerTemplate: footer, preferCSSPageSize: true });
  return file;
}

function capaHTML() {
  const c = CFG.capa; let s = fs.readFileSync(path.join(DIR, 'capa.html'), 'utf8');
  const chips = (c.chips || []).map(x => `<span>${esc(x)}</span>`).join('');
  const rep = { NUMERO: c.numero, TITULO1: c.titulo1, TITULO2: c.titulo2, SUB: c.sub, DESCRICAO: c.descricao, CHIPS: chips, DATA: c.data, AVISO: c.aviso || '' };
  for (const [k, v] of Object.entries(rep)) s = s.split(`{{${k}}}`).join(k === 'CHIPS' ? v : esc(v));
  const f = path.join(TMP, 'capa.render.html'); fs.writeFileSync(f, s); return f;
}

(async () => {
  execFileSync('python3', [path.join(DIR, 'gerar.py')], { stdio: 'inherit' });
  const browser = await chromium.launch();
  const page = await browser.newPage();
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
  const qc = JSON.parse(execFileSync('python3', ['-I', '-c', `
import sys,json,re
from pypdf import PdfReader
r=PdfReader(sys.argv[1]); bad=[]
for i,p in enumerate(r.pages):
    if not re.search(r'§§P\\d{3}§§', p.extract_text() or ''): bad.append(i+1)
print(json.dumps({'paginas':len(r.pages),'sem_marcador':bad}))`, body]).toString());
  console.log('QC:', qc, qc.sem_marcador.length ? '<- ATENÇÃO: páginas transbordadas, divida o conteúdo' : '(ok)');
  body = await renderBody(page, toc);
  await page.goto('file://' + capaHTML(), { waitUntil: 'networkidle' });
  const capa = path.join(TMP, 'capa.pdf');
  await page.pdf({ path: capa, width: '210mm', height: '297mm', printBackground: true, pageRanges: '1' });
  await browser.close();
  execFileSync('python3', ['-I', '-c', `
import sys,json
from pypdf import PdfWriter, PdfReader
w=PdfWriter()
for f in sys.argv[3:]: w.append(f)
m=json.loads(sys.argv[2]); w.add_metadata({'/Title':m['title'],'/Subject':m['subject'],'/Keywords':m['keywords'],'/Author':'Professor GCM Parnaíba'})
w.write(sys.argv[1])
r=PdfReader(sys.argv[1]); assert len(r.pages)>1 and r.metadata.title==m['title']
print('Integridade: ok,', len(r.pages), 'páginas')`, FINAL, JSON.stringify(CFG.meta), capa, body], { stdio: 'inherit' });
  console.log('OK ->', FINAL);
})();
