"""Gera miolo.html da Apostila 02 · Conhecimentos Profissionais · GCM Parnaíba. Uso: node build.js.
Skill professor-gcm-parnaiba. Verificações em GCM-PARNAIBA/fontes/notas-de-verificacao.md."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit
from kit import *

DATA = "28 de novembro de 2026"
kit.U = {1: ("UNIDADE 1", "O que é cobrado"), 2: ("UNIDADE 2", "Constituição Federal"), 3: ("UNIDADE 3", "Segurança pública"),
         4: ("UNIDADE 4", "Lei nº 13.022/2014"), 5: ("UNIDADE 5", "Legislação municipal"), 6: ("UNIDADE 6", "Atuação e limites"),
         7: ("UNIDADE 7", "Direitos humanos e força"), 8: ("UNIDADE 8", "ECA"), 9: ("UNIDADE 9", "Trânsito")}

add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar esta <span class="hl">apostila</span></h1>
<p class="lead">A legislação e as regras de conduta do guarda municipal, explicadas do zero.</p>
{ATENCAO(p("<strong>Edital ainda não confirmado.</strong> O Edital nº 001/2026 da GCM de Parnaíba (banca IGEDUC) foi retirado para republicação no Diário Oficial. As notícias da época citaram a disciplina “Conhecimentos Profissionais”, mas <strong>sem o conteúdo programático</strong>. Por isso, os temas desta apostila são <strong>CONTEÚDO ESTIMADO</strong>: escolhidos pela legislação da carreira e pelo perfil do cargo. Compare com o edital quando ele for republicado."))}
{table(["Disciplina (distribuição provisória)","Questões","Pontos"],[["Código Penal","15","37,5"],["<b>Conhecimentos Profissionais</b>","<b>15</b>","<b>37,5</b>"],["Língua Portuguesa","10","15"],["Conhecimentos Regionais de Parnaíba","4","4"],["Informática","3","3"],["Raciocínio Lógico","3","3"]],["60%","20%",None])}
<p style="font-size:9.5pt;color:{C["muted"]}">Distribuição provisória, pendente de confirmação no edital oficial.</p>
{table(["Etapa","O que fazer"],[["1","Leia o mapa de pertinência (Unidade 1) para saber onde concentrar esforço"],["2","Estude uma unidade por sessão e faça o treino Certo ou Errado"],["3","Resolva as 30 questões sem consultar e confira o gabarito comentado"],["4","Revise com o resumo, os flashcards e o checklist"]],["14%",None])}''', first=True)

toc_page([
 ("u", "UNIDADE 1 · O QUE É COBRADO", "U1"), ("", "1. Mapa de pertinência dos temas", "A01"),
 ("u", "UNIDADE 2 · CONSTITUIÇÃO FEDERAL", "U2"), ("", "4. Fundamentos · 5. Direitos na abordagem · 6. Direitos do preso", "A04"),
 ("u", "UNIDADE 3 · SEGURANÇA PÚBLICA", "U3"), ("", "7. Art. 144 · 8. Funções dos órgãos · 9. Decisões do STF", "A07"),
 ("u", "UNIDADE 4 · ESTATUTO GERAL DAS GUARDAS (LEI 13.022/2014)", "U4"), ("", "10. Princípios · 11. Competências · 12. Criação e requisitos · 13. Controle e prerrogativas", "A10"),
 ("u", "UNIDADE 5 · LEGISLAÇÃO MUNICIPAL DE PARNAÍBA", "U5"), ("", "14. Lei 1.989/2003 · 15. Organização, escala e disciplina", "A14"),
 ("u", "UNIDADE 6 · ATUAÇÃO PREVENTIVA, ÉTICA E LIMITES", "U6"), ("", "16. Atuação preventiva · 17. Ética e cidadania · 18. Limites da atuação", "A16"),
 ("u", "UNIDADE 7 · DIREITOS HUMANOS E USO PROPORCIONAL DA FORÇA", "U7"), ("", "19. Direitos humanos · 20. Uso da força · 21. Abuso de autoridade", "A19"),
 ("u", "UNIDADE 8 · CRIANÇA E ADOLESCENTE (ECA)", "U8"), ("", "22. Proteção · 23. Ato infracional e apreensão", "A22"),
 ("u", "UNIDADE 9 · NOÇÕES DE TRÂNSITO", "U9"), ("", "24. A guarda e o CTB · 25. Regras mais aplicadas", "A24"),
 ("u", "PRÁTICA E REVISÃO", "RV"), ("", "30 questões autorais", "R3"), ("", "Gabarito comentado e respostas dos treinos", "R4"), ("", "Resumo, revisão rápida, flashcards e checklist", "R1")])

# ================================================================ UNIDADE 1
opener("01", "UNIDADE 1", "O que é cobrado", ["Mapa de pertinência dos temas"], "U1")
add(H(1, 'Mapa de <span class="hl">pertinência</span>', 'Nem todo tema da lista cai: veja o que tem respaldo nas fontes.', "A01") +
 p("“Conhecimentos Profissionais” é a parte da prova que cobra o que o guarda precisa saber para trabalhar: a lei da carreira, os limites de atuação e o respeito aos direitos. Como o conteúdo oficial ainda não foi publicado, cada tema foi avaliado pela força do respaldo nas fontes:") +
 table(["Tema", "Relevância estimada", "Justificativa"], [
  ["Lei nº 13.022/2014 (Estatuto Geral)", "<b>ALTA</b>", "Lei nacional da carreira; regulamenta o art. 144, § 8º, da CF"],
  ["Lei Municipal nº 1.989/2003 (GCM de Parnaíba)", "<b>ALTA</b>", "Lei que criou e organiza a guarda do concurso"],
  ["CF: fundamentos, direitos e garantias, art. 144", "<b>ALTA</b>", "Base de toda a atuação; o art. 144 trata da segurança pública e das guardas"],
  ["Direitos humanos e uso proporcional da força", "<b>ALTA</b>", "Princípios do art. 3º da Lei 13.022 (direitos humanos e uso progressivo da força); Lei 13.060/2014"],
  ["Atuação preventiva, ética, cidadania e limites", "<b>ALTA</b>", "Função preventiva (art. 2º da Lei 13.022) e princípios do art. 37 da CF"],
  ["Abuso de autoridade (Lei 13.869/2019)", "MÉDIA", "Limita a conduta de todo agente público, inclusive na abordagem"],
  ["Estatuto da Criança e do Adolescente", "MÉDIA", "Segurança escolar é competência da guarda (Lei 13.022, art. 5º, XVIII)"],
  ["Legislação de trânsito", "MÉDIA", "A lei municipal prevê fiscalização de trânsito e a GOTRAN; a Lei 13.022 permite a atuação no trânsito"],
  ["Primeiros socorros", "BAIXA", "Não há, nas fontes consultadas, previsão específica; a Lei 13.060/2014 prevê socorro a quem é ferido no uso da força. Não desenvolvido nesta apostila"],
  ["Estatuto do Servidor de Parnaíba (Lei 1.366/1992)", "Possível", "Citado pela Lei 1.989/2003 para direitos e disciplina, mas o texto não estava disponível"]], ["32%", "18%", None]) +
 PEGADINHA(p("Não estude por listas da internet que “garantem” o conteúdo. Até a republicação do edital, nada é oficial. Use esta tabela para priorizar e ajuste quando o edital sair.")))

import ub
ub.unidade2(); ub.unidade3()
import ua  # Unidades 4, 5 e 6
ub.unidade7(); ub.unidade8(); ub.unidade9()

# ================================================================ QUESTÕES
Q = [
 ("Lei 13.022/2014", "Segundo a Lei nº 13.022/2014, as guardas municipais são instituições de caráter:",
  ["civil, uniformizadas e armadas conforme previsto em lei, com função de proteção municipal preventiva.", "militar, auxiliares e reserva do Exército.", "militar, subordinadas ao Governador do Estado.", "privado, contratadas pelo Município para vigilância.", "judiciário, vinculadas ao juiz da comarca."], "A",
  "Art. 2º da Lei 13.022/2014: instituições de caráter civil, uniformizadas e armadas conforme a lei, com função de proteção municipal preventiva.", "Guarda = civil e preventiva."),
 ("Princípios", "NÃO constitui princípio mínimo de atuação das guardas municipais, segundo o art. 3º da Lei nº 13.022/2014:",
  ["a hierarquia e a disciplina militares.", "a proteção dos direitos humanos fundamentais.", "o patrulhamento preventivo.", "o uso progressivo da força.", "o compromisso com a evolução social da comunidade."], "A",
  "Os cinco princípios são: direitos humanos e cidadania; preservação da vida e redução do sofrimento e das perdas; patrulhamento preventivo; compromisso com a comunidade; uso progressivo da força. A lei afasta o regime militar.", "Cinco princípios: DH, vida, preventivo, comunidade, força progressiva."),
 ("Competências", "Diante de flagrante delito, a guarda municipal deve, segundo a Lei nº 13.022/2014:",
  ["encaminhar o autor ao delegado de polícia, preservando o local do crime quando possível e sempre que necessário.", "lavrar o auto de prisão em flagrante.", "instaurar inquérito policial.", "liberar o autor após identificá-lo.", "conduzir o autor diretamente ao presídio."], "A",
  "Art. 5º, XIV. A guarda não exerce polícia judiciária: não lavra o auto nem instaura inquérito.", "Flagrante: ao delegado."),
 ("Competências", "A competência geral das guardas municipais, prevista no art. 4º da Lei nº 13.022/2014, é a proteção de:",
  ["bens, serviços, logradouros públicos municipais e instalações do Município.", "fronteiras e portos.", "presídios estaduais.", "bens da União em todo o território nacional.", "estabelecimentos bancários privados."], "A",
  "Art. 4º. Os bens incluem os de uso comum, de uso especial e dominiais.", "Bens, serviços, logradouros e instalações."),
 ("Controle", "Sobre o controle das guardas municipais, é correto afirmar:",
  ["a ouvidoria é exigida independentemente do número de servidores.", "a corregedoria é dispensada nas guardas que utilizam arma de fogo.", "a ouvidoria é subordinada ao comandante da guarda.", "o corregedor pode ser afastado livremente pelo prefeito.", "a guarda deve adotar regulamento disciplinar militar."], "A",
  "Art. 13: corregedoria obrigatória acima de 50 servidores ou se a guarda usa arma de fogo; ouvidoria independente e obrigatória em qualquer guarda; perda do mandato por maioria absoluta da Câmara. Regulamento militar é vedado (art. 14).", "Ouvidoria: sempre."),
 ("Requisitos", "É requisito básico de investidura no cargo de guarda municipal, segundo a Lei nº 13.022/2014:",
  ["nível médio completo de escolaridade.", "nível superior completo.", "idade mínima de 21 anos.", "serviço militar prestado nas Forças Armadas.", "residência no Município há mais de cinco anos."], "A",
  "Art. 10: nacionalidade brasileira, direitos políticos, obrigações militares e eleitorais, nível médio completo, 18 anos, aptidão física, mental e psicológica e idoneidade moral. A lei municipal pode criar outros requisitos.", "Médio completo e 18 anos."),
 ("Efetivo", "Em um Município com 40.000 habitantes, o efetivo máximo da guarda municipal é de:",
  ["160 guardas.", "120 guardas.", "80 guardas.", "200 guardas.", "400 guardas."], "A",
  "Art. 7º, I: até 50 mil habitantes, 0,4% da população. 40.000 × 0,004 = 160.", "0,4 · 0,3 · 0,2%."),
 ("Prerrogativas", "O número telefônico destinado pela Anatel aos Municípios que possuem guarda municipal é o:",
  ["153.", "190.", "192.", "193.", "199."], "A",
  "Art. 17 da Lei 13.022/2014.", "Guarda = 153."),
 ("Legislação municipal", "Pela Lei Municipal nº 1.989/2003, a Guarda Civil Municipal de Parnaíba é diretamente subordinada:",
  ["ao Chefe do Poder Executivo Municipal.", "ao Comandante-Geral da Polícia Militar.", "à Câmara Municipal.", "ao Secretário de Segurança do Estado.", "ao Juiz da Comarca."], "A",
  "Art. 2º da Lei 1.989/2003.", "GCM responde ao Prefeito."),
 ("Legislação municipal", "Segundo a Lei Municipal nº 1.989/2003, o ingresso no quadro efetivo da Guarda Civil Municipal de Parnaíba ocorre por:",
  ["concurso público e posterior aprovação em curso de formação profissional.", "indicação do Comandante.", "contratação temporária renovável.", "transferência de policiais militares.", "eleição entre os servidores municipais."], "A",
  "Art. 3º: concurso público e aprovação em curso de formação, do próprio Comando ou de guarda de outro Município, por convênio.", "Concurso + curso de formação."),
 ("Legislação municipal", "Na estrutura da Guarda Civil Municipal de Parnaíba, a sigla GOTRAN designa:",
  ["a Guarda Ostensiva de Trânsito, cujos integrantes são denominados Agentes.", "o Grupo de Operações Táticas e Resgate.", "a Gerência de Orçamento e Transportes.", "o Gabinete do Comandante.", "a Guarda do Patrimônio Histórico."], "A",
  "Art. 7º, § 2º, I, e § 3º da Lei 1.989/2003.", "GOTRAN = trânsito."),
 ("Legislação municipal", "Pela Lei Municipal nº 1.989/2003, é correto afirmar sobre o regime de trabalho:",
  ["o desconhecimento da escala não justifica falta ao serviço.", "o turno de trabalho é sempre de 12 horas.", "é proibida a escala de 24 horas.", "o comandante não pode alterar a forma da escala.", "a falta é justificada se o guarda não conhecia a escala."], "A",
  "Arts. 29 a 33: turnos de 6 horas ou escala de 24 por 48 horas, a critério do Comandante; o desconhecimento da escala não justifica falta (art. 33).", "Desconhecer a escala não justifica a falta."),
 ("Constituição", "É fundamento da República Federativa do Brasil, nos termos do art. 1º da Constituição:",
  ["a dignidade da pessoa humana.", "a prevalência dos direitos humanos.", "a erradicação da pobreza.", "a independência nacional.", "a defesa da paz."], "A",
  "Art. 1º: soberania, cidadania, dignidade da pessoa humana, valores sociais do trabalho e da livre iniciativa e pluralismo político. As demais são objetivos (art. 3º) ou princípios das relações internacionais (art. 4º).", "SO-CI-DI-VA-PLU."),
 ("Direitos fundamentais", "Sobre a inviolabilidade do domicílio, é correto afirmar:",
  ["sem o consentimento do morador, é possível entrar na casa, a qualquer hora, em flagrante delito, desastre ou para prestar socorro.", "com ordem judicial, é possível entrar na casa a qualquer hora da noite.", "a autoridade policial pode autorizar a entrada durante a noite.", "a simples suspeita de crime autoriza a entrada sem ordem judicial.", "a casa é inviolável em qualquer situação, sem exceções."], "A",
  "CF, art. 5º, XI: flagrante, desastre e socorro autorizam a entrada a qualquer hora; a ordem judicial só autoriza durante o dia.", "Mandado: só de dia."),
 ("Direitos do preso", "NÃO corresponde a um direito do preso previsto na Constituição:",
  ["ser exibido à imprensa para identificação pública.", "ser informado de seus direitos, entre os quais o de permanecer calado.", "ter a prisão comunicada imediatamente ao juiz e à família.", "conhecer a identificação dos responsáveis por sua prisão.", "ter respeitada sua integridade física e moral."], "A",
  "CF, art. 5º, XLIX, LXII, LXIII e LXIV. Exibir o preso à curiosidade pública, mediante constrangimento, pode ser crime de abuso de autoridade (Lei 13.869/2019, art. 13).", "Preso: calado, comunicado, identifica quem prendeu, integridade."),
 ("Direito de reunião", "Sobre o direito de reunião, previsto no art. 5º, XVI, da Constituição:",
  ["independe de autorização, sendo exigido apenas prévio aviso à autoridade competente.", "depende de autorização prévia da guarda municipal.", "pode ser exercido com armas, se registradas.", "prevalece sobre reunião anteriormente convocada para o mesmo local.", "só pode ocorrer em recinto fechado."], "A",
  "A reunião deve ser pacífica, sem armas, em local aberto ao público, sem frustrar outra reunião já convocada, com prévio aviso.", "Aviso, não autorização."),
 ("Segurança pública", "As guardas municipais estão previstas na Constituição Federal:",
  ["no art. 144, § 8º, destinadas à proteção dos bens, serviços e instalações municipais, conforme dispuser a lei.", "no art. 144, inciso VI, como polícia penal municipal.", "no art. 142, como força auxiliar do Exército.", "no art. 5º, como direito fundamental.", "apenas em lei ordinária, sem previsão constitucional."], "A",
  "O inciso VI do art. 144 trata das polícias penais. As guardas estão no § 8º.", "Guarda: art. 144, § 8º."),
 ("STF", "No julgamento do Tema 656 de repercussão geral (2025), o STF entendeu que as guardas municipais:",
  ["podem exercer ações de segurança urbana, inclusive policiamento ostensivo e comunitário, respeitadas as atribuições dos demais órgãos e excluída a polícia judiciária.", "podem instaurar inquéritos policiais.", "substituem as polícias militares.", "não podem realizar nenhum tipo de policiamento.", "só podem proteger prédios da prefeitura."], "A",
  "RE 608.588, Tema 656, julgado em 20/02/2025, conforme notícia oficial do STF.", "Ostensivo e comunitário, sem polícia judiciária."),
 ("Uso da força", "Segundo a Lei nº 13.060/2014, NÃO é legítimo o uso de arma de fogo:",
  ["contra pessoa em fuga que esteja desarmada ou que não represente risco imediato de morte ou lesão.", "em legítima defesa contra agressão armada atual.", "para repelir agressão com risco de morte a terceiro.", "contra quem dispara contra a equipe.", "para defender vítima mantida refém sob ameaça de morte."], "A",
  "Lei 13.060/2014, art. 2º, parágrafo único, I; regra repetida no Decreto 12.341/2024, art. 3º, § 3º.", "Fuga desarmada e sem risco: não atira."),
 ("Uso da força", "Segundo o Decreto nº 12.341/2024, que regulamenta a Lei nº 13.060/2014, o emprego de arma de fogo:",
  ["é medida de último recurso.", "é a primeira opção diante de qualquer desobediência.", "dispensa capacitação específica.", "dispensa relatório, mesmo quando resulta em morte.", "é permitido contra qualquer veículo que fure bloqueio."], "A",
  "Art. 3º, § 2º. O decreto exige relatório circunstanciado se houver lesão ou morte (§ 5º) e só permite o disparo contra veículo que fura bloqueio se houver risco (§ 3º, II).", "Arma de fogo = último recurso."),
 ("Uso da força", "Durante uma discussão na feira, o guarda municipal deve, como regra, adotar:",
  ["a presença e o diálogo antes de qualquer contenção, usando a força de modo progressivo e proporcional.", "o uso imediato de algemas em todos os envolvidos.", "o disparo de advertência para dispersar as pessoas.", "a força máxima disponível, para encerrar logo a ocorrência.", "a retirada do local, por não ser competência da guarda."], "A",
  "Uso progressivo da força (Lei 13.022, art. 3º, V) e prioridade à comunicação e à negociação (Decreto 12.341/2024, art. 3º, § 1º). Colaborar com a pacificação de conflitos presenciados é competência da guarda (Lei 13.022, art. 5º, V).", "Primeiro presença e diálogo."),
 ("Abuso de autoridade", "Sobre a Lei de Abuso de Autoridade (Lei nº 13.869/2019), é correto afirmar:",
  ["a divergência na interpretação da lei ou na avaliação de fatos e provas não configura abuso de autoridade.", "qualquer erro do agente configura abuso de autoridade.", "os crimes dependem de queixa do ofendido.", "a lei só se aplica a juízes e promotores.", "não exige nenhuma finalidade específica do agente."], "A",
  "Art. 1º, §§ 1º e 2º: exige finalidade específica (prejudicar, beneficiar ou mero capricho); divergência de interpretação não configura. A ação penal é pública incondicionada (art. 3º) e a lei alcança todo agente público (art. 2º).", "Abuso exige finalidade específica."),
 ("Abuso de autoridade", "Deixar de identificar-se ao preso por ocasião de sua captura caracteriza, em tese:",
  ["crime de abuso de autoridade previsto na Lei nº 13.869/2019.", "mera falta funcional sem consequência penal.", "crime de desacato.", "contravenção penal.", "conduta permitida, por razões de segurança."], "A",
  "Lei 13.869/2019, art. 16 (detenção de 6 meses a 2 anos). A CF garante ao preso a identificação dos responsáveis por sua prisão (art. 5º, LXIV).", "Identificar-se ao preso é dever."),
 ("Ética", "Um guarda deixa de fiscalizar a barraca irregular de um amigo, mas autua com rigor o concorrente. A conduta viola, principalmente, o princípio da:",
  ["impessoalidade.", "publicidade.", "eficiência.", "continuidade.", "autotutela."], "A",
  "CF, art. 37, caput: a impessoalidade proíbe favorecimentos e perseguições. A conduta pode, ainda, configurar crime como a prevaricação.", "Favoreceu amigo = impessoalidade."),
 ("Atuação preventiva", "Constitui exemplo típico de atuação preventiva da guarda municipal:",
  ["a ronda visível em praça com histórico de furtos, no horário de maior movimento.", "a investigação de um homicídio ocorrido na cidade.", "o interrogatório formal de suspeitos na base da guarda.", "a lavratura de auto de prisão em flagrante.", "o cumprimento de mandado de busca e apreensão sem a polícia."], "A",
  "Prevenir e inibir pela presença e vigilância (Lei 13.022, art. 5º, II) e patrulhamento preventivo (art. 3º, III). As demais são atividades de polícia judiciária.", "Prevenção = presença e vigilância."),
 ("ECA", "Pelo Estatuto da Criança e do Adolescente, considera-se criança a pessoa:",
  ["até 12 anos de idade incompletos.", "até 14 anos de idade.", "até 16 anos de idade.", "até 18 anos de idade incompletos.", "até 10 anos de idade."], "A",
  "ECA, art. 2º: criança até 12 anos incompletos; adolescente de 12 a 18 anos.", "Criança: até 12 incompletos."),
 ("ECA", "Durante a ronda escolar, um guarda municipal identifica sinais de maus-tratos em uma criança. Segundo o ECA, a suspeita deve ser obrigatoriamente comunicada:",
  ["ao Conselho Tutelar da localidade.", "somente aos pais da criança.", "à direção da escola, apenas.", "à imprensa local.", "ao comandante da guarda, que decide se informa alguém."], "A",
  "ECA, art. 13: comunicação obrigatória ao Conselho Tutelar, sem prejuízo de outras providências legais.", "Maus-tratos: Conselho Tutelar."),
 ("ECA", "Sobre o adolescente apreendido em flagrante de ato infracional, é correto afirmar:",
  ["não pode ser conduzido em compartimento fechado de veículo policial em condições atentatórias à dignidade ou que impliquem risco.", "deve ser conduzido no porta-malas da viatura, por segurança.", "pode ficar incomunicável até o dia seguinte.", "é preso e indiciado como um adulto.", "dispensa comunicação à família."], "A",
  "ECA, arts. 107 (comunicação imediata ao juiz e à família), 172 (encaminhamento à autoridade policial) e 178 (vedação do compartimento fechado em condições indignas).", "Sem compartimento fechado; comunicar já."),
 ("Trânsito", "Um agente da GOTRAN, por gestos, manda os veículos seguirem, embora o semáforo esteja vermelho. Pelo Código de Trânsito, o condutor deve:",
  ["seguir, pois as ordens do agente prevalecem sobre o semáforo.", "parar, pois o semáforo prevalece sobre o agente.", "parar, pois as normas gerais prevalecem.", "buzinar e aguardar o sinal verde.", "decidir livremente, por haver conflito."], "A",
  "CTB, art. 89: ordens do agente > semáforo > demais sinais > normas de circulação.", "Agente > semáforo."),
 ("Limites", "Assinale a conduta que está FORA dos limites legais de atuação da guarda municipal:",
  ["entrar à noite em uma residência, sem consentimento, para cumprir ordem judicial de busca.", "prender em flagrante e apresentar o autor ao delegado.", "entrar em uma casa a qualquer hora para socorrer uma vítima.", "fiscalizar o trânsito com base na competência legal.", "colaborar com a pacificação de conflito presenciado."], "A",
  "A ordem judicial só autoriza o ingresso durante o dia (CF, art. 5º, XI). Cumprir mandado de busca domiciliar entre 21h e 5h pode configurar abuso de autoridade (Lei 13.869/2019, art. 22, § 1º, III).", "Mandado de busca: de dia."),
]
questoes(Q)
respostas_treinos()

# ================================================================ REVISÃO
add('<div class="marker">§§R1§§</div><div class="unit"><span class="u">REVISÃO</span><span class="t">Véspera da prova</span></div><h1 class="big">Resumo <span class="hl">estratégico</span></h1><p class="lead">O essencial de cada unidade em uma página.</p>' +
 table(["Unidade", "O que mais cai"], [
  ["Constituição", "Fundamentos (SO-CI-DI-VA-PLU); domicílio (flagrante, desastre, socorro; ordem judicial só de dia); reunião com aviso; direitos do preso (calado, comunicação, identificação, integridade)"],
  ["Segurança pública", "Art. 144: órgãos dos incisos; guarda no § 8º; PM ostensiva; Civil judiciária; segurança viária; STF: ADPF 995, Tema 656, Tema 472"],
  ["Lei 13.022/2014", "Civil, uniformizada, armada conforme a lei, preventiva; 5 princípios; competência geral e 18 específicas; flagrante ao delegado; efetivo 0,4/0,3/0,2%; corregedoria e ouvidoria; 153"],
  ["Lei municipal", "Lei 1.989/2003: subordinação ao Prefeito; concurso + curso de formação; 7 competências; postos e graduações; GOTRAN; escala 6h ou 24×48"],
  ["Atuação e limites", "Prevenção pela presença; LIMPE; ouvidoria; a guarda não investiga nem lavra auto de prisão"],
  ["Direitos humanos e força", "Universalidade; uso progressivo; Lei 13.060/2014; Decreto 12.341/2024 (último recurso, relatório, capacitação); abuso de autoridade exige finalidade específica"],
  ["ECA", "Criança até 12 incompletos; Conselho Tutelar; apreensão comunicada já; sem compartimento fechado; internação máx. 3 anos"],
  ["Trânsito", "Lei 13.022, art. 5º, VI; agente > semáforo; pedestre e faixa a 50 m; álcool e celular gravíssimas"]], ["22%", None]))

add(pratica_title("Revisão rápida: verdadeiro ou falso de memória") + table(["Afirmação", "Resposta"], [
  ["A guarda municipal é instituição de caráter militar.", "Falso: civil"],
  ["Ouvidoria é exigida em qualquer guarda.", "Verdadeiro"],
  ["A guarda pode lavrar auto de prisão em flagrante.", "Falso: encaminha ao delegado"],
  ["Ordem judicial autoriza entrar em casa à noite.", "Falso: só de dia"],
  ["O preso tem direito à identificação de quem o prendeu.", "Verdadeiro"],
  ["As guardas estão no inciso VI do art. 144.", "Falso: § 8º"],
  ["Arma de fogo é medida de último recurso.", "Verdadeiro"],
  ["Divergência de interpretação configura abuso de autoridade.", "Falso"],
  ["Criança é a pessoa até 12 anos incompletos.", "Verdadeiro"],
  ["O semáforo prevalece sobre o agente de trânsito.", "Falso: o agente prevalece"],
  ["A GCM de Parnaíba é subordinada ao Prefeito.", "Verdadeiro"],
  ["Desconhecer a escala justifica a falta.", "Falso"]], ["72%", None]))

flashcards([
 ("LEI 13.022", "Natureza da guarda?", "Civil, uniformizada e armada conforme a lei; proteção municipal preventiva."),
 ("LEI 13.022", "Cinco princípios?", "Direitos humanos; vida; patrulhamento preventivo; comunidade; uso progressivo da força."),
 ("LEI 13.022", "Competência geral?", "Proteger bens, serviços, logradouros e instalações municipais."),
 ("LEI 13.022", "Flagrante?", "Encaminhar o autor ao delegado, preservando o local."),
 ("LEI 13.022", "Corregedoria e ouvidoria?", "Corregedoria: mais de 50 servidores ou guarda armada. Ouvidoria: sempre."),
 ("LEI 13.022", "Efetivo máximo?", "0,4% (até 50 mil), 0,3% (até 500 mil), 0,2% (acima)."),
 ("MUNICIPAL", "A quem a GCM de Parnaíba é subordinada?", "Ao Chefe do Poder Executivo Municipal."),
 ("MUNICIPAL", "Como se ingressa?", "Concurso público e aprovação em curso de formação."),
 ("MUNICIPAL", "O que é a GOTRAN?", "Guarda Ostensiva de Trânsito; seus integrantes são Agentes."),
 ("MUNICIPAL", "Escalas possíveis?", "Turnos de 6 horas ou 24 por 48 horas."),
 ("CF", "Fundamentos da República?", "Soberania, cidadania, dignidade, valores sociais do trabalho e da livre iniciativa, pluralismo político."),
 ("CF", "Quando entrar em casa sem consentimento?", "Flagrante, desastre, socorro (qualquer hora); ordem judicial (de dia)."),
 ("CF", "Direitos do preso?", "Calar, comunicação ao juiz e à família, identificação de quem prendeu, integridade."),
 ("SEG. PÚBLICA", "Onde está a guarda na CF?", "Art. 144, § 8º."),
 ("SEG. PÚBLICA", "Função da PM?", "Polícia ostensiva e preservação da ordem pública."),
 ("STF", "Tema 656?", "Segurança urbana, inclusive policiamento ostensivo e comunitário; sem polícia judiciária."),
 ("FORÇA", "Princípios da Lei 13.060?", "Legalidade, necessidade, razoabilidade e proporcionalidade."),
 ("FORÇA", "Arma de fogo no Decreto 12.341?", "Último recurso; relatório se houver lesão ou morte."),
 ("FORÇA", "Quando não atirar?", "Pessoa em fuga desarmada ou sem risco; veículo em bloqueio, salvo risco."),
 ("ABUSO", "O que a Lei 13.869 exige?", "Finalidade específica: prejudicar, beneficiar ou mero capricho."),
 ("ÉTICA", "Princípios do art. 37 da CF?", "Legalidade, impessoalidade, moralidade, publicidade e eficiência."),
 ("ECA", "Criança x adolescente?", "Até 12 anos incompletos · de 12 a 18 anos."),
 ("ECA", "Maus-tratos?", "Comunicação obrigatória ao Conselho Tutelar."),
 ("TRÂNSITO", "Prevalência da sinalização?", "Agente > semáforo > sinais > normas.")])

add(checklist([
  "Sei a natureza, os princípios e as competências da Lei 13.022/2014",
  "Sei as regras de efetivo, requisitos, corregedoria, ouvidoria e prerrogativas",
  "Conheço a Lei Municipal 1.989/2003: subordinação, ingresso, competências, postos, GOTRAN e escala",
  "Sei os fundamentos da República e os direitos do art. 5º usados na abordagem",
  "Sei as hipóteses de entrada em domicílio",
  "Sei os direitos da pessoa presa",
  "Sei o art. 144 e onde está a guarda municipal",
  "Conheço as decisões do STF (ADPF 995, Temas 656 e 472)",
  "Sei aplicar o uso progressivo e proporcional da força (Lei 13.060 e Decreto 12.341)",
  "Sei o que caracteriza abuso de autoridade e os crimes mais ligados à abordagem",
  "Sei as regras do ECA sobre proteção, ato infracional e apreensão",
  "Sei as noções de trânsito ligadas à atuação da guarda",
  "Sei os limites da atuação da guarda (o que pode e o que não pode)"]) +
 pratica_title("Revisões espaçadas") + revisoes_espacadas("Conhecimentos Profissionais"))

add(pratica_title("Caderno de erros") + p("Anote cada questão que errar, o motivo do erro e a regra correta.") + caderno_erros(12))

referencias(f'''<h3>Edital e editais anteriores</h3><ul>
<li>Aviso do Edital nº 001/2026 da GCM de Parnaíba (Diário Oficial do Município nº 4344, 26/11/2026; banca IGEDUC). O edital foi retirado para republicação; até {DATA} não foi localizado o texto republicado nem o conteúdo programático. <b>Conteúdo desta apostila: ESTIMADO.</b></li>
<li>Concurso de GCM de Cajueiro da Praia-PI (2026, INBRASP): as notícias consultadas não trazem o conteúdo programático. Edital de GCM de Teresina (NUCEPE): link indisponível.</li></ul>
<h3>Legislação conferida (portal do Planalto)</h3><ul>
<li>Constituição Federal: art. 1º; art. 5º (caput, III, IV, X, XI, XV, XVI, XXXIX, XLIII, XLIX, LVII, LXI a LXV, LXVIII); art. 37, caput; art. 144 (caput e §§ 5º, 7º, 8º, 9º e 10).</li>
<li>Lei nº 13.022/2014 (Estatuto Geral das Guardas Municipais), arts. 1º a 23.</li>
<li>Lei nº 13.060/2014 e Decreto nº 12.341/2024 (uso da força).</li>
<li>Lei nº 13.869/2019 (abuso de autoridade): arts. 1º a 3º, 9º, 12, 13, 15, 16, 18, 22, 24, 25, 27, 33 e 38.</li>
<li>Lei nº 8.069/1990 (ECA): arts. 2º, 4º, 5º, 13, 15, 18, 101, 103 a 107, 109, 112, 121, 131, 136, 171 a 174, 178, 232, 234 e 244-B.</li>
<li>Lei nº 9.503/1997 (CTB): arts. 24, 29, 61, 69, 70, 89, 165, 165-A, 252, 259 e 280.</li></ul>
<h3>Legislação municipal (arquivos do projeto)</h3><ul><li>Leis nº 1.989/2003, 1.872/2002 e 3.480/2019 de Parnaíba (cópias de repositórios de legislação; o texto oficial é o do Diário Oficial).</li></ul>
<h3>Jurisprudência</h3><ul><li>STF: ADPF 995 (2023); RE 608.588, Tema 656 (2025); RE 658.570, Tema 472 (2015), conforme notícias oficiais do tribunal.</li></ul>''',
 '<strong>Limitações:</strong> o edital oficial não estava disponível, por isso o conteúdo é estimado; não estavam disponíveis a Lei nº 1.615/1997, a Lei nº 1.366/1992 (Estatuto do Servidor de Parnaíba) e a Lei Orgânica do Município; o Decreto nº 12.341/2024 não cita as guardas municipais pelo nome no texto lido; as decisões do STF foram resumidas a partir de notícias oficiais, sem leitura do inteiro teor; primeiros socorros não foram desenvolvidos por falta de respaldo nas fontes. Confira o texto oficial das normas antes da prova.', DATA)
encerramento("02", "Conhecimentos Profissionais", "Próxima sugestão: <strong>Apostila 03 · Língua Portuguesa</strong>.", "novembro de 2026")
gravar(HERE, "Apostila 02 — Conhecimentos Profissionais — GCM Parnaíba", Q)
