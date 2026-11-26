# Padrão editorial: Cadernos Simplificados para concursos

> "CADERNOS SIMPLIFICADOS: O QUE REALMENTE CAI NA PROVA."
> Este é o padrão permanente para todos os materiais da pasta `CADERNOS/`.

## Papel
Professor de concursos, pesquisador de legislação, especialista em didática e memorização, designer editorial e diagramador de PDFs profissionais. Público: quem estuda para concurso e tem dificuldade com linguagem jurídica.

## Estrutura didática de cada assunto
1. Título → 2. O que é? → 3. Explicação completa → 4. Traduzindo o juridiquês → 5. Na prática (exemplo) →
6. Visualização didática (diagrama, fluxograma, tabela, linha do tempo) → 7. Prioridade de estudo →
8. Palavras-chave → 9. Atenção à pegadinha → 10. Quadro de comparação → 11. Resumo visual →
12. Questões autorais → 13. Gabarito comentado.

## Regras de conteúdo
- Pesquisar antes de produzir (Planalto, DOU, Senado, Câmara, STF, STJ). Não inventar artigos, súmulas, julgados, editais ou estatísticas.
- Citar a lei corretamente e conferir a redação vigente. Incluir "Material pesquisado e atualizado em: [data]". Informar limitações.
- Sem levantamento confiável de incidência, escrever "PRIORIDADE DE ESTUDO", nunca "cai muito".
- Questões criadas para o caderno: marcar como "Questão autoral" e nunca atribuir a uma banca. Questão real só com banca, concurso e ano verificados.
- Mnemônicos só quando forem claros, sempre explicados.
- Se houver edital, ele é a fonte prioritária. Sem edital: perguntar ou usar uma matriz de referência declarada como tal.
- Não prometer aprovação. Não copiar materiais protegidos nem imitar a marca ou o visual de terceiros.

## Estilo de explicação (referência visual enviada pela pessoa usuária)
- Explicação **simplificada e visual**, com um assunto por vez e, em geral, duas páginas por assunto:
  - Página A: título grande; quadro creme com o artigo; **Traduzindo o juridiquês** com personagem professor(a); faixa **Memorize**.
  - Página B: **Entenda na prática** (fluxo de ícones com setas); exemplo curto; **Pegadinha de concurso** (faixa vermelha); palavras-chave.
- Frases curtas, pouco texto corrido e muito esquema. Um bloco por página: o build acusa transbordo (marcadores `§§Pnnn§§`).
- As fotos de referência servem só de estilo: nunca copiar layout, marca ou capa de terceiros.

## Padrão visual
- Capa editorial, sumário numerado, cabeçalho e rodapé com número de página, referências e encerramento.
- Boxes fixos: Letra da lei (creme), O que é? (azul claro), Traduzindo (contorno escuro), Na prática (verde), Memorize (laranja), Pegadinha (vermelho), Prioridade de estudo (escuro), Palavras-chave (chips).
- Ilustrações e diagramas em SVG próprios, sempre com função didática.
- Paleta por disciplina. Penal: grafite, laranja, vermelho. Constitucional: azul. Administrativo: azul e verde. GCM: verde e preto. Direitos Humanos: azul e amarelo. Português: azul ou roxo. Informática: azul-escuro, ciano e cinza.
- Nunca reduzir a fonte para encaixar o conteúdo: aumentar o número de páginas.

## Produção e controle de qualidade
- Fonte HTML/CSS em `fonte/` e PDF final em `pdf/`. Marcadores de sumário: `§§A01§§` (assuntos), `§§U1§§` (unidades), `§§R1§§` (revisão); conferir se o sumário saiu com números. Build com `node fonte/build.js` (Playwright + pypdf), que numera o sumário automaticamente.
- Antes de entregar: renderizar as páginas em imagem e conferir cortes, sobreposições, páginas vazias, legibilidade, português, legislação e referências.
- Organização: `CADERNOS/<DISCIPLINA>/<SUBÁREA>/modulo-NN-<tema>/`. Não sobrescrever edições anteriores sem autorização (nova edição = nova pasta ou sufixo `-ed2`).

## Comandos
`CRIAR CADERNO DE ...` · `CRIAR CADERNO ... PARA <CONCURSO>` · `CRIAR CADERNO BASEADO NESTE EDITAL` · `CRIAR MAPA MENTAL` · `CRIAR FLASHCARDS` · `CRIAR SIMULADO` · `REVISAR ESTE MATERIAL`

## Marca da coleção
- Nome comercial: **MAPA DA APROVAÇÃO — Cadernos Simplificados para Concursos** (20 cadernos). Paleta da marca: branco, preto, grafite, laranja e azul-marinho.
- A marca está aplicada em todos os cadernos: na capa ("MAPA DA APROVAÇÃO" no topo), no cabeçalho das páginas, nos metadados do PDF e na página final. A faixa lateral da capa mantém "Cadernos Simplificados · O que realmente cai na prova".
- Material gratuito de amostra: `MAPA-DA-APROVACAO/mini-ebook-gratuito/`. Não leva link de vendas: os eBooks são entregues aos leads depois da compra.

## Catálogo
| Disciplina | Módulo | Conteúdo | Atualizado em | PDF |
|---|---|---|---|---|
| Direito Administrativo | Caderno 12 | Agentes públicos: categorias, cargo/emprego/função, concurso, direitos, deveres, responsabilidades e regime disciplinar (Lei 8.112) | 26/11/2026 | `DIREITO-ADMINISTRATIVO/caderno-12-agentes-publicos/pdf/` |
| Direito Administrativo | Caderno 11 | Atos administrativos: conceito, elementos, atributos, espécies, classificação, anulação, revogação e convalidação | 26/11/2026 | `DIREITO-ADMINISTRATIVO/caderno-11-atos-administrativos/pdf/` |
| Direito Administrativo | Caderno 10 | Poderes administrativos: vinculado, discricionário, hierárquico, disciplinar, regulamentar, de polícia, limites e abuso de poder | 26/11/2026 | `DIREITO-ADMINISTRATIVO/caderno-10-poderes-administrativos/pdf/` |
| Direito Administrativo | Caderno 09 | Fundamentos: conceito, objeto, Administração direta e indireta, autarquias, fundações, estatais, princípios (LIMPE, supremacia e indisponibilidade) e organização administrativa | 26/11/2026 | `DIREITO-ADMINISTRATIVO/caderno-09-direito-administrativo-fundamentos/pdf/` |
| Direito Constitucional | 04 | Segurança Pública (art. 144), com quadro sobre a PEC 18/2025 (não promulgada) | 25/11/2026 | `DIREITO-CONSTITUCIONAL/caderno-04-seguranca-publica-art-144/pdf/` |
| Direito Constitucional | 03 | Administração Pública na Constituição (arts. 37 a 41), com a EC nº 138/2025 | 25/11/2026 | `DIREITO-CONSTITUCIONAL/caderno-03-administracao-publica-arts-37-a-41/pdf/` |
| Direito Constitucional | 02 | Direitos e garantias fundamentais (art. 5º) | 25/11/2026 | `DIREITO-CONSTITUCIONAL/caderno-02-direitos-e-garantias-fundamentais-art-5/pdf/` |
| Direito Constitucional | 01 | Fundamentos, princípios (arts. 1º a 4º) e organização do Estado | 25/11/2026 | `DIREITO-CONSTITUCIONAL/caderno-01-fundamentos-principios-organizacao-do-estado/pdf/` |
| Direito Processual Penal | Caderno 13 | Fundamentos: princípios, sistemas, inquérito, ação penal, provas, cadeia de custódia, sujeitos, flagrante e procedimentos | 26/11/2026 | `DIREITO-PENAL/PROCESSO-PENAL/caderno-13-processo-penal-fundamentos/pdf/` |
| Direito Penal: Legislação Penal Especial | Caderno 08 | Drogas, Desarmamento, Hediondos, Tortura, Maria da Penha, Abuso de Autoridade e Organizações Criminosas (com alterações de 2025-2026) | 26/11/2026 | `DIREITO-PENAL/LEGISLACAO-PENAL-ESPECIAL/caderno-08-legislacao-penal-especial/pdf/` |
| Direito Penal: Crimes contra a Administração Pública | Caderno 07 | Título XI do CP: funcionário público, crimes funcionais, crimes de particular (desacato e ADPF 496), Administração da Justiça (com o art. 338-A, Lei 15.280/2025) e noções de licitações | 26/11/2026 | `DIREITO-PENAL/CRIMES-CONTRA-ADMINISTRACAO/caderno-07-crimes-contra-administracao-publica/pdf/` |
| Direito Penal: Parte Especial | Caderno 06 | Crimes contra a vida, honra, liberdade, patrimônio e Administração Pública (com Leis 14.994/2024 e 15.397/2026) | 26/11/2026 | `DIREITO-PENAL/PARTE-ESPECIAL/caderno-06-direito-penal-parte-especial/pdf/` |
| Direito Penal: Parte Geral | Caderno 05 | Parte Geral completa: princípios, lei penal, teoria do crime e penas | 25/11/2026 | `DIREITO-PENAL/PARTE-GERAL/caderno-05-direito-penal-parte-geral/pdf/` |
| Direito Penal: Parte Geral | 01 | Aplicação da Lei Penal (arts. 1º a 12 do CP). Mantido: aprofunda arts. 8º a 12 e extraterritorialidade, não detalhados no Caderno 05 | 24/11/2026 | `DIREITO-PENAL/PARTE-GERAL/modulo-01-aplicacao-da-lei-penal/pdf/` |
| Mapa da Aprovação (amostra gratuita) | — | Mini Guia Gratuito: 5 assuntos simplificados | 25/11/2026 | `MAPA-DA-APROVACAO/mini-ebook-gratuito/pdf/` |
