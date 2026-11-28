# Metodologia de criação e revisão de PDFs

## Identidade visual
- Paleta: **azul-marinho** `#0f1f3d` (estrutura e títulos), **branco** (fundo), **dourado/amarelo** `#e8b923` (destaques e faixa MEMORIZE), **cinza** `#5f6673` (texto secundário), azul de apoio `#1f4e8c`.
- Fonte Inter / Inter Display (já instaladas). A4, margens de 16 mm, corpo de texto com 11 pt.
- Capa-modelo em `assets/kit/capa.html`, sem brasão, logotipo nem símbolos oficiais da Prefeitura, da GCM ou da banca.
- Cabeçalho "GCM PARNAÍBA · disciplina" e rodapé com a data e o número da página.

## Kit (`assets/kit/`)
| Arquivo | Função |
|---|---|
| `componentes.py` | Ícones, personagens e caixas (lei, traduz, memo, pega, ex, oque, lembre, table, cards, flow) |
| `kit.py` | Páginas, sumário, aberturas de unidade, treinos C/E, questões, gabarito, mapa, flashcards, quadros da Skill (`ATENCAO`, `NAO_CONFUNDA`, `EXEMPLO`, `MEMORIZE`, `PEGADINHA`, `topico`), revisão (`perguntas_rapidas`, `checklist`, `caderno_erros`, `revisoes_espacadas`, `mapa_textual`), checagem automática |
| `estilo.css` | Estilo das páginas |
| `capa.html` | Capa com marcadores preenchidos a partir do config.json |
| `build.js` | Gera o PDF (duas passadas para numerar o sumário, QC de transbordamento, metadados e verificação de integridade) |
| `config.exemplo.json` | Modelo de configuração |

## Passo a passo
```bash
cp -r .claude/skills/professor-gcm-parnaiba/assets/kit GCM-PARNAIBA/apostilas/fonte/01-codigo-penal
cd GCM-PARNAIBA/apostilas/fonte/01-codigo-penal
cp config.exemplo.json config.json        # preencher arquivo, cabeçalho, capa, meta e data
# escrever gerar.py (ver exemplos/exemplo-minimo/gerar.py)
node build.js                              # PDF sai em GCM-PARNAIBA/apostilas/ ("saida": "../..")
```
Regras do `gerar.py`:
- Cada `add(...)` é **uma página**. Se o QC acusar páginas em `sem_marcador`, o conteúdo transbordou: divida em duas páginas (`atencao(...)` cria página de continuação).
- Marcadores de sumário: `§§U1§§` (unidade), `§§A01§§` (tópico), `§§R1§§` (revisão). Use os mesmos códigos em `toc_page`.
- Escreva `&lt;` para o sinal de menor em textos. Use aspas tipográficas “ ” dentro das strings.
- Termine com `gravar(HERE, titulo, Q)`, que grava o miolo e roda a checagem automática.

## Checklist de revisão antes de entregar (todos obrigatórios)
1. **Checagem automática:** `python3 gerar.py` deve mostrar `CHECAGEM: 0 alerta(s)` (palavras repetidas, pontuação, parênteses, alternativas duplicadas).
2. **QC de páginas:** `sem_marcador: []`.
3. **Revisão visual:** renderize todas as páginas (`pdftoppm -r 40`) em folhas de contato e olhe uma a uma. Amplie diagramas e tabelas (`-r 80`). Corrija textos sobrepostos, cortados ou pequenos demais.
4. **Conteúdo:** releia cada artigo citado contra a fonte oficial; confira prazos, penas e números.
5. **Gabarito:** uma correta por questão; comentários coerentes com a letra final; letras equilibradas.
6. **Ortografia:** revise acentuação, concordância e crase dos títulos e quadros.
7. **Integridade:** o build já confere se o PDF abre, o número de páginas e os metadados. Confirme também o tamanho do arquivo e a abertura com `pdfinfo`.
8. **Legibilidade no celular:** corpo de texto com no mínimo 10 pt; tabelas sem colunas espremidas.
9. **Registrar** a apostila no catálogo `GCM-PARNAIBA/README.md` e fazer commit e push.
