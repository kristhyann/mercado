// Gera Mapa_da_Aprovacao_Acesso.pdf a partir de acesso.html. Uso: node build.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage();
  await pg.goto('file://' + path.join(__dirname, 'acesso.html'), { waitUntil: 'networkidle' });
  await pg.pdf({ path: path.join(__dirname, '..', 'Mapa_da_Aprovacao_Acesso.pdf'), preferCSSPageSize: true, printBackground: true });
  await b.close();
})();
