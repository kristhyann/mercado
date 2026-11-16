# Patas Protegidas — *Meu cachorro, minha responsabilidade*

E-book completo de cuidados, saúde, proteção e bem-estar canino, com 18 capítulos, fichas imprimíveis, checklists, infográficos e 7 projetos caseiros ilustrados.

## Arquivos finais (`saida/`)

| Arquivo | O que é |
|---|---|
| `Patas-Protegidas-ebook-completo.pdf` | E-book completo diagramado (A5, 222 páginas), com sumário clicável, páginas numeradas, marcadores de navegação e referências |
| `Patas-Protegidas-fichas-e-checklists.pdf` | Só as fichas (Cap. 16) e checklists (Cap. 17), para imprimir |
| `capa.png` / `capa.pdf` | Capa em imagem de alta resolução e em PDF |
| `Patas-Protegidas-texto-editavel.docx` | Texto completo em Word, para revisão e edição |

> Para imprimir em folha A4, use "ajustar à página" ou "2 páginas por folha".

## Estrutura do projeto

```
ebook-patas-protegidas/
├── conteudo/                 ← TEXTO EDITÁVEL (Markdown) — um arquivo por capítulo
│   ├── 00-creditos.md, 00-apresentacao.md
│   ├── cap01-…md  …  cap18-…md
│   └── 99-referencias.md
├── imagens/
│   ├── fotos-originais/      ← fotografias recebidas, sem alteração
│   ├── fotos/                ← recortes usados no livro (gerados por build/fotos.py)
│   └── ilustracoes/          ← infográficos e projetos em SVG (editáveis) + png/ + icones/
├── estilo/
│   ├── ebook.css             ← identidade visual, tipografia, cores, layout das páginas
│   └── fontes/               ← Fraunces e Nunito Sans (SIL Open Font License)
├── build/
│   ├── gerar.sh              ← gera tudo de uma vez
│   ├── fotos.py              ← recortes das fotos
│   ├── ilustracoes.py        ← desenha todos os SVGs (ícones, infográficos, projetos)
│   ├── svg_png.js            ← exporta as ilustrações em PNG
│   ├── build.py              ← Markdown → HTML diagramado
│   ├── render.js             ← HTML → PDF (Paged.js + Chromium)
│   ├── marcadores.py         ← marcadores (bookmarks) e metadados do PDF
│   └── vendor/               ← Paged.js (licença MIT)
└── saida/                    ← arquivos finais
```

## Como editar o texto

Abra o capítulo em `conteudo/` em qualquer editor de texto. Além do Markdown comum (`##` seção, `###` subseção, `**negrito**`, listas e tabelas), há blocos especiais:

```
:::dica Título            caixa verde de dica       (também: info, alerta, vet, proibido, emergencia, mito)
:::checklist Título       checklist (itens começam com "- [ ]")
:::passos                 lista numerada em etapas
:::grade                  cartões lado a lado (separe com +++)   — grade3, grade-verde
:::doenca | etiqueta      cartão de doença          (também: socorro, projeto)
:::citacao                frase em destaque
:::                       fecha o bloco
@foto(nome, classes, "legenda")   foto de imagens/fotos/nome.jpg   (classes: direita, esquerda, redonda, meia)
@svg(nome, classes, "legenda")    ilustração de imagens/ilustracoes/nome.svg
@tabela(proibidos)                cor da próxima tabela (proibidos, permitidos, grade, semana)
@quebra                           nova página
```

O cabeçalho de cada capítulo (entre `---`) define número, título, foto de abertura e a lista "Neste capítulo".

## Como gerar o PDF novamente

Requisitos: Python 3 com `markdown`, `Pillow` e `pypdf`; Node.js com `playwright` (Chromium); `pandoc` e `poppler-utils`.

```bash
pip install markdown pillow pypdf
./build/gerar.sh
```

## Onde cada fotografia aparece

| Foto original | Uso no livro |
|---|---|
| Cão caramelo olhando para cima | Capa, abertura do Cap. 1, abertura do Cap. 10, mensagem final (Cap. 18) |
| Cão preto e caramelo com pote de água | Abertura do Cap. 4 (Água), Cap. 1 (adoção de adultos), contracapa |
| Dachshund de pelo longo | Abertura do Cap. 3 (Alimentação), Cap. 9 (pelos longos) |
| Filhote de dachshund | Abertura do Cap. 11 (Filhotes) |
| Filhotes dormindo | Abertura do Cap. 13 (Abandono), Cap. 13 (ajudar animais de rua), abertura do Cap. 18 |

## Aviso

Conteúdo educativo. Não substitui consulta, diagnóstico, prescrição ou tratamento por médico-veterinário. Nenhuma dose de medicamento ou dieta caseira é indicada no livro.
