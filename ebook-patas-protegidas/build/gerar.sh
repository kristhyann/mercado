#!/usr/bin/env bash
# Gera todos os arquivos finais do e-book Patas Protegidas.
# Requisitos: Python 3 (markdown, Pillow), Node.js com Playwright/Chromium, pandoc e poppler-utils.
set -euo pipefail
cd "$(dirname "$0")/.."
export NODE_PATH="${NODE_PATH:-$(npm root -g)}"

python3 build/fotos.py
python3 build/ilustracoes.py
python3 build/build.py
node build/svg_png.js

node build/render.js build/ebook.html  saida/Patas-Protegidas-ebook-completo.pdf
node build/render.js build/fichas.html saida/Patas-Protegidas-fichas-e-checklists.pdf
python3 build/marcadores.py saida/Patas-Protegidas-ebook-completo.pdf

# Capa em imagem (PNG) e em PDF de uma página
pdftoppm -r 220 -png -f 1 -l 1 -singlefile saida/Patas-Protegidas-ebook-completo.pdf saida/capa
python3 -c "from pypdf import PdfReader,PdfWriter;r=PdfReader('saida/Patas-Protegidas-ebook-completo.pdf');w=PdfWriter();w.add_page(r.pages[0]);w.compress_identical_objects(remove_duplicates=True,remove_unreferenced=True);w.write('saida/capa.pdf')"

# Versão editável (Word) a partir do HTML de conteúdo
(cd build && pandoc editavel.html -f html -t docx --resource-path=.:.. -o ../saida/Patas-Protegidas-texto-editavel.docx)
echo "Pronto. Arquivos em saida/"
