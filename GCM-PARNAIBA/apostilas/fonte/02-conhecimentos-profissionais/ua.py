"""Apostila 02 · Conhecimentos Profissionais · Unidades 4, 5 e 6 (Lei 13.022/2014, legislação municipal, atuação preventiva e limites).
Lei 13.022/2014 conferida no Planalto em 26/11/2026; Lei Municipal 1.989/2003 lida no arquivo do projeto (cópia de LeisMunicipais)."""
from kit import *

def lg(a): return f"Art. {a} · Lei nº 13.022/2014 (em síntese)"
def lm(a): return f"Art. {a} · Lei Municipal nº 1.989/2003 (em síntese)"

# ================================================================ UNIDADE 4 · LEI 13.022/2014
opener("04", "UNIDADE 4", "Estatuto Geral das Guardas Municipais", ["Natureza e princípios", "Competências geral e específicas", "Criação, efetivo e requisitos", "Formação, controle e prerrogativas"], "U4")

add(topico('Natureza e <span class="hl">princípios</span>', 'Arts. 1º a 3º da Lei nº 13.022/2014.', "A10",
  p("A Lei nº 13.022/2014 é o <strong>Estatuto Geral das Guardas Municipais</strong>: traz as normas gerais que valem para todas as guardas do país, regulamentando o art. 144, § 8º, da Constituição."),
  p("Pense nela como a “regra nacional” da profissão. Cada cidade cria a sua guarda por lei municipal, mas precisa respeitar o que o Estatuto Geral diz: o que a guarda é, o que pode fazer e como deve ser controlada."),
  (lg("2º e 3º"), "<p><b>Art. 2º:</b> incumbe às guardas municipais, <b>instituições de caráter civil, uniformizadas e armadas</b> conforme previsto em lei, a função de <b>proteção municipal preventiva</b>, ressalvadas as competências da União, dos Estados e do Distrito Federal. <b>Art. 3º (princípios mínimos):</b> I – proteção dos direitos humanos fundamentais, do exercício da cidadania e das liberdades públicas; II – preservação da vida, redução do sofrimento e diminuição das perdas; III – patrulhamento preventivo; IV – compromisso com a evolução social da comunidade; V – uso progressivo da força.</p>"),
  p("Uma equipe faz ronda visível na praça ao entardecer, conversa com comerciantes e orienta frequentadores: aplica o patrulhamento preventivo e o compromisso com a comunidade. Diante de uma discussão, começa pelo diálogo antes de qualquer contenção: uso progressivo da força."),
  "a banca pergunta a natureza (civil, e não militar) ou inclui um falso princípio, como “hierarquia e disciplina militares” ou “patrulhamento repressivo”.",
  "<ul><li><b>Errado:</b> “As guardas municipais são instituições de caráter militar.” <b>Certo:</b> são de caráter <b>civil</b> (art. 2º).</li><li><b>Errado:</b> “A lei exige o uso imediato da força.” <b>Certo:</b> o princípio é o uso <b>progressivo</b> da força.</li></ul>",
  "Guarda = instituição <strong>civil</strong>, <strong>uniformizada</strong>, <strong>armada conforme a lei</strong>, para <strong>proteção municipal preventiva</strong>. Princípios: <strong>direitos humanos · vida · patrulhamento preventivo · comunidade · uso progressivo da força</strong>.", 4))

add(H(4, 'Competência <span class="hl">geral</span> e competências específicas', 'Arts. 4º e 5º: o que a guarda faz.', "A11") +
 lei(lg("4º"), "<p>É competência geral das guardas municipais a <b>proteção de bens, serviços, logradouros públicos municipais e instalações do Município</b>. Os bens abrangem os de <b>uso comum</b> (praças, ruas), de <b>uso especial</b> (escolas, postos de saúde) e <b>dominiais</b> (patrimônio disponível, como um terreno desocupado).</p>") +
 table(["Grupo", "Competências específicas (art. 5º, em síntese)"], [
  ["Patrimônio e prevenção", "I zelar pelos bens, equipamentos e prédios públicos · II prevenir e inibir, pela presença e vigilância, e coibir infrações penais ou administrativas contra bens, serviços e instalações municipais · III atuar preventiva e permanentemente, protegendo a população que usa os bens e serviços municipais"],
  ["Cooperação", "IV colaborar com os órgãos de segurança pública em ações conjuntas · V colaborar com a pacificação de conflitos que seus integrantes presenciarem · VIII cooperar com a defesa civil · X firmar parcerias, convênios ou consórcios · XI articular-se com órgãos municipais de políticas sociais · XII integrar-se aos órgãos de poder de polícia administrativa (posturas e ordenamento urbano)"],
  ["Trânsito e meio ambiente", "VI exercer as competências de trânsito conferidas nas vias municipais (CTB), ou de forma concorrente, por convênio · VII proteger o patrimônio ecológico, histórico, cultural, arquitetônico e ambiental"],
  ["Comunidade e prevenção", "IX interagir com a sociedade civil · XV contribuir em estudos de impacto na segurança local · XVI ações de prevenção primária à violência · XVIII segurança escolar e cultura de paz"],
  ["Ocorrências e eventos", "XIII garantir o atendimento de ocorrências emergenciais ou prestá-lo direta e imediatamente · XIV encaminhar ao <b>delegado de polícia</b> o autor de infração em <b>flagrante delito</b>, preservando o local do crime quando possível · XVII auxiliar na segurança de grandes eventos e na proteção de autoridades"]], ["22%", None]) +
 p("<strong>Parágrafo único:</strong> nas hipóteses dos incisos XIII e XIV, quando comparecer órgão do art. 144 da CF, a guarda deverá prestar <strong>todo o apoio à continuidade do atendimento</strong>."))

atencao(scene3([("FLAGRANTE", C['red'], C['redsoft'], "prof", ["Detém o autor e", "o apresenta ao", "delegado (XIV)."], "preserva o local"),
  ("CHEGOU A PM", C['blue'], C['sky'], "profa", ["Presta todo apoio", "à continuidade do", "atendimento."], "parágrafo único"),
  ("ESCOLA", C['green'], C['greensoft'], "prof", ["Zela pelo entorno", "e faz ações", "educativas (XVIII)."], "cultura de paz")], "Situação ilustrada: competências específicas em ação.") +
 PEGADINHA("<ul><li><b>Errado:</b> “No flagrante, a guarda lavra o auto de prisão e instaura inquérito.” <b>Certo:</b> encaminha o autor ao <b>delegado de polícia</b> (inciso XIV). A guarda não exerce polícia judiciária.</li><li><b>Errado:</b> “Quando a PM chega, a guarda deve se retirar.” <b>Certo:</b> presta <b>todo o apoio</b> à continuidade do atendimento.</li></ul>") +
 MEMORIZE("Competência geral: <strong>bens, serviços, logradouros e instalações</strong> (uso comum, especial e dominiais). Flagrante: <strong>ao delegado</strong>. Trânsito: <strong>CTB ou convênio</strong>."),
 ["Bens públicos", "Flagrante", "Apoio à continuidade"], "Competências: pontos mais cobrados")

add(H(4, 'Criação, efetivo e <span class="hl">requisitos</span>', 'Arts. 6º a 10.', "A12") +
 table(["Regra", "Conteúdo (em síntese)"], [
  ["Criação (art. 6º)", "O Município <b>pode</b> criar, <b>por lei</b>, sua guarda, subordinada ao <b>chefe do Poder Executivo municipal</b>"],
  ["Efetivo máximo (art. 7º)", "<b>0,4%</b> da população (até 50 mil habitantes) · <b>0,3%</b> (de 50 mil a 500 mil) · <b>0,2%</b> (acima de 500 mil)"],
  ["Consórcio (art. 8º)", "Municípios limítrofes podem, por consórcio público, usar reciprocamente os serviços da guarda"],
  ["Carreira (art. 9º)", "Servidores de <b>carreira única</b> e plano de cargos e remuneração, por lei municipal"]], ["26%", None]) +
 cards([("flag", "Nacionalidade", "brasileira"), ("ballot", "Direitos políticos", "em pleno gozo"), ("check", "Obrigações", "militares e eleitorais quitadas"),
        ("book", "Escolaridade", "nível médio completo"), ("calendar", "Idade", "mínima de 18 anos"), ("heart", "Aptidão", "física, mental e psicológica")]) +
 p("<strong>Art. 10, VII:</strong> idoneidade moral comprovada por investigação social e certidões do Poder Judiciário estadual, federal e distrital. <strong>Parágrafo único:</strong> a lei municipal pode estabelecer outros requisitos.") +
 MEMORIZE("Criação <strong>facultativa e por lei</strong> · comanda o <strong>prefeito</strong> · efetivo <strong>0,4 · 0,3 · 0,2%</strong> · ingresso com <strong>ensino médio e 18 anos</strong>."))

add(H(4, 'Formação, controle e <span class="hl">prerrogativas</span>', 'Arts. 11 a 22.', "A13") +
 table(["Tema", "Regra (em síntese)"], [
  ["Capacitação (arts. 11 e 12)", "Exige capacitação específica; pode ser adaptada a matriz curricular nacional da Senasp; o órgão de formação <b>não pode ser o mesmo</b> das forças militares (art. 12, § 3º)"],
  ["Corregedoria (art. 13, I)", "Controle <b>interno</b>; obrigatória nas guardas com <b>mais de 50</b> servidores e em <b>todas as que usam arma de fogo</b>"],
  ["Ouvidoria (art. 13, II)", "Controle <b>externo</b>, independente da direção da guarda, <b>qualquer que seja o efetivo</b>"],
  ["Mandato (art. 13, § 2º)", "Corregedor e ouvidor têm mandato; a perda depende de decisão por <b>maioria absoluta da Câmara Municipal</b>"],
  ["Disciplina (art. 14)", "Código de conduta próprio, por lei municipal; <b>vedado</b> regulamento disciplinar de natureza militar"],
  ["Carreira (art. 15)", "Cargos em comissão providos por membros da carreira (nos primeiros 4 anos pode haver dirigente de fora); percentual mínimo para mulheres; progressão funcional"],
  ["Porte (art. 16)", "Pode ser autorizado o porte de arma de fogo, conforme a lei; suspenso por restrição médica, decisão judicial ou justificativa do dirigente"],
  ["Prerrogativas (arts. 17 a 21)", "Telefone <b>153</b> e faixa exclusiva de rádio · cela separada se preso antes da condenação definitiva · vedadas denominações hierárquicas idênticas às militares · uniformes preferencialmente <b>azul-marinho</b>"],
  ["Denominações (art. 22, parágrafo único)", "Guarda civil, guarda civil municipal, guarda metropolitana e guarda civil metropolitana"]], ["28%", None]) +
 PEGADINHA("<ul><li>Ouvidoria: obrigatória <b>sempre</b>. Corregedoria: acima de 50 servidores <b>ou</b> se a guarda é armada.</li><li>Uniforme azul-marinho é <b>preferencial</b>, não obrigatório.</li></ul>"))

treino(4, [
 ("As guardas municipais são instituições de caráter civil, uniformizadas e armadas conforme previsto em lei.", "C", "Art. 2º da Lei 13.022/2014."),
 ("O patrulhamento repressivo é princípio expresso das guardas municipais.", "E", "O princípio é o patrulhamento preventivo (art. 3º, III)."),
 ("Diante de flagrante delito, a guarda deve encaminhar o autor ao delegado de polícia.", "C", "Art. 5º, XIV."),
 ("A ouvidoria só é obrigatória nas guardas com mais de 50 servidores.", "E", "A ouvidoria é exigida independentemente do efetivo."),
 ("Em município com até 50 mil habitantes, o efetivo da guarda não pode exceder 0,4% da população.", "C", "Art. 7º, I."),
 ("As guardas podem adotar regulamento disciplinar de natureza militar.", "E", "Vedado (art. 14, parágrafo único).")])

# ================================================================ UNIDADE 5 · LEGISLAÇÃO MUNICIPAL
opener("05", "UNIDADE 5", "Legislação municipal de Parnaíba", ["Lei nº 1.989/2003: criação, competências e hierarquia", "Organização, regime de trabalho e disciplina", "Lei nº 1.872/2002 e Lei nº 3.480/2019"], "U5")

add(topico('A GCM de Parnaíba na <span class="hl">lei municipal</span>', 'Lei Municipal nº 1.989/2003, arts. 1º a 4º.', "A14",
  p("A Lei Municipal nº 1.989/2003 é a lei que <strong>cria e organiza</strong> a Guarda Civil Municipal de Parnaíba, com base no art. 144, § 8º, da Constituição."),
  p("A Lei 13.022/2014 é a regra nacional; a Lei 1.989/2003 é a regra da sua cidade: diz a quem a guarda responde, como ingressar, quais são os postos e como funciona a escala de trabalho."),
  (lm("1º a 4º"), "<p><b>Art. 1º:</b> órgão da Administração Direta, com a finalidade de proteger os bens, serviços e instalações municipais e zelar pela fiscalização do cumprimento do Código de Trânsito Brasileiro no Município. <b>Art. 2º:</b> instituição permanente do Poder Executivo, estruturada em postos e graduações e diretamente subordinada ao Chefe do Poder Executivo Municipal. <b>Art. 3º:</b> ingresso por concurso público e posterior aprovação em curso de formação profissional. <b>Art. 4º:</b> sete competências, detalhadas na página seguinte.</p>"),
  p("Durante uma enchente, a GCM apoia a Defesa Civil no isolamento de ruas: competência do art. 4º, V. Na Avenida São Sebastião, um agente da GOTRAN orienta o trânsito: fiscalização do art. 4º, III."),
  "pede-se a quem a GCM é subordinada (ao Prefeito), como se ingressa (concurso + curso de formação) ou qual das competências do art. 4º está correta.",
  "<ul><li><b>Errado:</b> “A GCM de Parnaíba é subordinada ao Comandante da Polícia Militar.” <b>Certo:</b> é subordinada ao <b>Chefe do Poder Executivo Municipal</b>.</li><li><b>Errado:</b> “O ingresso se dá apenas pelo concurso.” <b>Certo:</b> concurso <b>e</b> aprovação em curso de formação.</li></ul>",
  "GCM de Parnaíba: <strong>Administração Direta</strong> · subordinada ao <strong>Prefeito</strong> · ingresso por <strong>concurso + curso de formação</strong> · 7 competências do <strong>art. 4º</strong>.", 5))

add(H(5, 'Competências, organização e <span class="hl">disciplina</span>', 'Lei Municipal nº 1.989/2003, arts. 4º a 37.', "A15") +
 table(["Tema", "Regra (em síntese)"], [
  ["Competências (art. 4º)", "I defender os bens públicos municipais · II vigilância nos logradouros públicos · III fiscalizar a ordenação de trânsito e tráfego urbano · IV segurança pessoal do Prefeito · V auxiliar a defesa civil em calamidade ou emergência · VI campanhas conjuntas com outros órgãos · VII auxiliar na educação, prevenção e defesa do meio ambiente"],
  ["Postos (art. 6º, I)", "Comandante · Subcomandante · Supervisor · Inspetor-Chefe · Inspetor"],
  ["Graduações (art. 6º, II)", "Subinspetor de 1ª, 2ª e 3ª Classe · Guarda de 1ª, 2ª e 3ª Classe · Guarda"],
  ["Estrutura (art. 7º)", "Comandante, Subcomandante, Divisão Administrativa (Pessoal, Almoxarifado, Técnica de Ensino) e Divisão Operacional: <b>GOTRAN</b> (Guarda Ostensiva de Trânsito, cujos integrantes são chamados de “Agentes”) e Guarda da Cidadania, do Patrimônio e das Instalações Públicas Municipais"],
  ["Comandante (arts. 2º, § 1º, e 8º)", "Cargo em comissão nomeado pelo Prefeito, com o mesmo nível hierárquico dos secretários municipais; substituído pelo Subcomandante nas ausências"],
  ["Regime de trabalho (arts. 29 a 33)", "Turnos de 6 horas (0–6, 6–12, 12–18, 18–24) ou escala de 24 horas de trabalho por 48 de folga, a critério do Comandante; o desconhecimento da escala não justifica falta"],
  ["Disciplina (arts. 34 a 37)", "Aplicam-se os deveres e as sanções do Estatuto do Servidor Municipal (Lei nº 1.366/1992); sanções podem chegar à expulsão; é vedado o rebaixamento de posto ou graduação"],
  ["Gratificação de risco (art. 28, parágrafo único)", "40% do vencimento básico no exercício do policiamento auxiliar ostensivo"]], ["28%", None]) +
 ATENCAO(p("A Lei 1.989/2003 usa “postos e graduações” e fala em “função auxiliar policial” (art. 9º). A Lei federal 13.022/2014, posterior, afirma o caráter <b>civil</b> das guardas e veda denominações idênticas às das forças militares (art. 19). Esta apostila apresenta as duas leis como estão; não há, nas fontes consultadas, informação sobre adaptação formal da lei municipal. Na prova, responda conforme a lei indicada na questão.")))

atencao(table(["Lei", "O que interessa para a prova"], [
  ["Lei nº 1.872/2002", "Criou 59 vagas de Guarda Civil Municipal (com base na Lei 1.615/1997, que instituiu a GCM); definiu a lotação de quem atua no trânsito e nas demais áreas. Parte foi revogada pela Lei 1.989/2003"],
  ["Lei nº 3.480/2019", "Obriga questões de conhecimentos regionais de Parnaíba (história, geografia, cultura, ética, política e economia) nas provas de concursos da Prefeitura"]], ["24%", None]) +
 lembre(p("Não estavam disponíveis para esta apostila: a Lei nº 1.615/1997 (que instituiu a GCM), a Lei nº 1.366/1992 (Estatuto do Servidor de Parnaíba) e a Lei Orgânica do Município. Se o edital as cobrar, elas exigirão estudo complementar."), "Lacunas da legislação municipal") +
 MEMORIZE("Postos: <strong>Comandante → Subcomandante → Supervisor → Inspetor-Chefe → Inspetor</strong>. Trânsito: <strong>GOTRAN</strong>. Escala: <strong>6h</strong> ou <strong>24 × 48</strong>."),
 ["Lei 1.872/2002", "Lei 3.480/2019", "Lacunas"], "Outras leis municipais")

treino(5, [
 ("A GCM de Parnaíba é órgão da Administração Direta do Município, subordinado diretamente ao Chefe do Poder Executivo Municipal.", "C", "Lei 1.989/2003, arts. 1º e 2º."),
 ("O ingresso na GCM de Parnaíba se dá por concurso público, dispensado o curso de formação.", "E", "Exige aprovação em curso de formação (art. 3º)."),
 ("Manter a segurança pessoal do Prefeito está entre as competências previstas no art. 4º da Lei Municipal 1.989/2003.", "C", "Art. 4º, IV."),
 ("Os integrantes da GOTRAN são denominados “Agentes”.", "C", "Art. 7º, § 3º."),
 ("Pela Lei 1.989/2003, o desconhecimento da escala justifica a falta ao serviço.", "E", "Não justifica (art. 33)."),
 ("A Lei Municipal 3.480/2019 obriga questões de conhecimentos regionais nos concursos da Prefeitura de Parnaíba.", "C", "Art. 1º.")])

# ================================================================ UNIDADE 6 · ATUAÇÃO PREVENTIVA, ÉTICA E LIMITES
opener("06", "UNIDADE 6", "Atuação preventiva, ética e limites", ["Atuação preventiva e comunitária", "Ética profissional e cidadania", "Limites da atuação da Guarda Municipal"], "U6")

add(topico('Atuação preventiva e <span class="hl">comunitária</span>', 'O jeito de trabalhar que a lei espera da guarda.', "A16",
  p("Atuação preventiva é agir <strong>antes</strong> que o problema aconteça, pela presença, pela vigilância e pela proximidade com a comunidade."),
  p("A melhor ocorrência é a que não acontece. Uma viatura visível na saída da escola, uma ronda que conhece os comerciantes da feira e um guarda que orienta o cidadão evitam crimes e acidentes."),
  "a Lei 13.022/2014 adota o <b>patrulhamento preventivo</b> como princípio (art. 3º, III) e atribui à guarda prevenir e inibir infrações pela presença e vigilância (art. 5º, II), atuar preventiva e permanentemente (art. 5º, III) e desenvolver prevenção primária à violência (art. 5º, XVI).",
  p("Moradores relatam furtos frequentes em uma praça escura. A guarda aumenta a ronda no horário crítico, comunica à Prefeitura a falta de iluminação e participa de reunião com a associação de moradores: prevenção, articulação e interação com a comunidade."),
  "a banca apresenta uma conduta repressiva ou investigativa como se fosse a função típica da guarda.",
  "<ul><li><b>Errado:</b> “A função principal da guarda é investigar crimes ocorridos no município.” <b>Certo:</b> a função é a <b>proteção municipal preventiva</b>; investigar é polícia judiciária.</li></ul>",
  "Prevenção = <strong>presença + vigilância + proximidade</strong>. Bases legais: <strong>art. 3º, III</strong> e <strong>art. 5º, II, III e XVI</strong> da Lei 13.022/2014.", 6))

add(topico('Ética profissional e <span class="hl">cidadania</span>', 'O comportamento esperado do servidor que usa farda.', "A17",
  p("Ética profissional é o conjunto de valores e deveres que orientam a conduta do servidor. Cidadania é o exercício de direitos e deveres pelas pessoas na vida em sociedade."),
  p("O guarda é um servidor público. Deve tratar todos com respeito, sem favorecer amigos nem perseguir desafetos, agir dentro da lei e prestar contas do que faz. Respeitar a cidadania é garantir que o cidadão exerça seus direitos, inclusive o de reclamar."),
  "a Constituição impõe à Administração Pública de todos os entes os princípios de <b>legalidade, impessoalidade, moralidade, publicidade e eficiência</b> (art. 37, caput). A Lei 13.022/2014 inclui a proteção da cidadania e das liberdades públicas entre os princípios (art. 3º, I), prevê a ouvidoria para receber reclamações e elogios (art. 13, II) e um código de conduta próprio (art. 14).",
  p("Um comerciante amigo pede ao guarda que “faça vista grossa” para a mercadoria irregular dele, mas cobre rigor do concorrente. Atender ao pedido viola a impessoalidade e a moralidade, e pode configurar crime, como prevaricação ou corrupção."),
  "aparecem casos de favorecimento, de tratamento desrespeitoso ou de uso do cargo para benefício pessoal, e a banca pergunta qual princípio foi violado.",
  "<ul><li><b>Errado:</b> “Por ser agente de segurança, o guarda pode deixar de identificar-se ao abordar o cidadão.” <b>Certo:</b> a atuação deve ser transparente e dentro da lei; a Lei de Abuso de Autoridade pune, por exemplo, quem deixa de se identificar ao preso ou se identifica falsamente (art. 16).</li></ul>",
  "Princípios da Administração: <strong>LIMPE</strong> (legalidade, impessoalidade, moralidade, publicidade, eficiência). Cidadania: <strong>respeito, transparência e prestação de contas</strong> (ouvidoria).", 6))

add(H(6, 'Limites da atuação da <span class="hl">Guarda Municipal</span>', 'O que a guarda pode e o que não pode fazer.', "A18") +
 NAO_CONFUNDA("A guarda PODE (com base legal)", "A guarda NÃO PODE", [
  ("Prisão", "Prender em flagrante e encaminhar ao delegado (CPP, art. 301; Lei 13.022, art. 5º, XIV)", "Lavrar auto de prisão, instaurar inquérito ou investigar (polícia judiciária)"),
  ("Policiamento", "Ações de segurança urbana, inclusive policiamento ostensivo e comunitário, respeitadas as atribuições dos demais órgãos (STF, Tema 656)", "Substituir a polícia militar ou a polícia civil em suas atribuições exclusivas"),
  ("Força", "Usar a força de modo progressivo, necessário e proporcional (Lei 13.022, art. 3º, V; Lei 13.060/2014)", "Usar arma de fogo contra pessoa em fuga desarmada que não represente risco (Lei 13.060, art. 2º, parágrafo único, I)"),
  ("Domicílio", "Entrar em casa em flagrante delito, desastre ou para prestar socorro (CF, art. 5º, XI)", "Entrar em casa sem consentimento fora dessas hipóteses ou sem ordem judicial de dia"),
  ("Trânsito", "Fiscalizar e autuar, quando a competência for conferida por lei municipal ou convênio (CTB; STF, Tema 472)", "Atuar fora da sua competência ou circunscrição"),
  ("Disciplina", "Seguir código de conduta próprio", "Submeter-se a regulamento disciplinar militar (Lei 13.022, art. 14)")]) +
 ATENCAO(p("Os resumos das decisões do STF (ADPF 995, Tema 656 e Tema 472) vêm de notícias oficiais do tribunal. A redação exata das teses deve ser conferida no portal do STF.")) +
 MEMORIZE("A guarda <strong>previne, protege, prende em flagrante e encaminha</strong>. Não <strong>investiga</strong>, não <strong>lavra auto de prisão</strong>, não usa força <strong>desproporcional</strong>."))

treino(6, [
 ("A atuação típica da guarda municipal é preventiva, baseada na presença e na vigilância.", "C", "Lei 13.022/2014, arts. 2º, 3º, III, e 5º, II e III."),
 ("Favorecer um comerciante conhecido na fiscalização viola o princípio da impessoalidade.", "C", "CF, art. 37, caput."),
 ("A guarda municipal pode instaurar inquérito policial sobre crimes ocorridos em bens municipais.", "E", "Não exerce polícia judiciária."),
 ("Segundo o STF, as guardas podem exercer policiamento ostensivo e comunitário, respeitadas as atribuições dos demais órgãos.", "C", "Tema 656 (2025), conforme notícia oficial do STF."),
 ("A ouvidoria é um instrumento de participação do cidadão no controle da guarda.", "C", "Art. 13, II, da Lei 13.022/2014."),
 ("É legítimo o uso de arma de fogo contra pessoa em fuga, ainda que desarmada e sem representar risco.", "E", "Lei 13.060/2014, art. 2º, parágrafo único, I.")])
