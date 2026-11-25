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
- Fonte HTML/CSS em `fonte/` e PDF final em `pdf/`. Build com `node fonte/build.js` (Playwright + pypdf), que numera o sumário automaticamente.
- Antes de entregar: renderizar as páginas em imagem e conferir cortes, sobreposições, páginas vazias, legibilidade, português, legislação e referências.
- Organização: `CADERNOS/<DISCIPLINA>/<SUBÁREA>/modulo-NN-<tema>/`. Não sobrescrever edições anteriores sem autorização (nova edição = nova pasta ou sufixo `-ed2`).

## Comandos
`CRIAR CADERNO DE ...` · `CRIAR CADERNO ... PARA <CONCURSO>` · `CRIAR CADERNO BASEADO NESTE EDITAL` · `CRIAR MAPA MENTAL` · `CRIAR FLASHCARDS` · `CRIAR SIMULADO` · `REVISAR ESTE MATERIAL`

## Catálogo
| Disciplina | Módulo | Conteúdo | Atualizado em | PDF |
|---|---|---|---|---|
| Direito Constitucional | 01 | Fundamentos, princípios (arts. 1º a 4º) e organização do Estado | 25/11/2026 | `DIREITO-CONSTITUCIONAL/caderno-01-fundamentos-principios-organizacao-do-estado/pdf/` |
| Direito Penal: Parte Geral | 01 | Aplicação da Lei Penal (arts. 1º a 12 do CP) | 24/11/2026 | `DIREITO-PENAL/PARTE-GERAL/modulo-01-aplicacao-da-lei-penal/pdf/` |
