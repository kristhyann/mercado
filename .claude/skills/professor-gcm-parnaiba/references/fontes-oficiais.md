# Fontes oficiais e confiáveis

Ordem de prioridade: 1) edital oficial · 2) texto legal oficial · 3) órgãos oficiais (STF, STJ, IBGE, Prefeitura) · 4) doutrina e materiais reconhecidos, só para explicar, nunca para criar regra.

| O quê | Onde verificar |
|---|---|
| Edital e atos do concurso | Diário Oficial do Município: https://www.parnaiba.pi.gov.br ; página da banca: https://igeduc.selecao.net.br/informacoes/190/ |
| Constituição Federal | https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm |
| Código Penal (DL 2.848/1940) | https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm |
| Código de Processo Penal | https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689compilado.htm |
| Lei 13.022/2014 (Estatuto Geral das Guardas) | https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l13022.htm |
| CTB (Lei 9.503/1997) | https://www.planalto.gov.br/ccivil_03/leis/l9503compilado.htm |
| Lei 13.060/2014 (uso de instrumentos de menor potencial ofensivo) | https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l13060.htm |
| Lei 13.869/2019 (abuso de autoridade) | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/lei/l13869.htm |
| Jurisprudência | portal.stf.jus.br e www.stj.jus.br (temas, súmulas, notícias oficiais) |
| Dados de Parnaíba | IBGE Cidades (cidades.ibge.gov.br), site da Prefeitura e Câmara Municipal |

## Como verificar neste ambiente
- Use o agente `web-fetch` com a URL oficial e peça o texto **literal** dos artigos. Em páginas grandes do Planalto, peça trechos por posição (offset). Desconfie de resumos: confira o texto do artigo.
- Alguns sites (banca, imprensa) bloqueiam acesso automatizado (403). Nesse caso, registre a limitação e peça o arquivo ao usuário.
- PDFs escaneados: renderize as páginas como imagem (pdftoppm) e leia visualmente.
- Registre cada verificação em `GCM-PARNAIBA/fontes/notas-de-verificacao.md`.
