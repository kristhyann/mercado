"""Gera miolo.html da Apostila 01 · Código Penal · GCM Parnaíba. Uso: node build.js (ou python3 gerar.py para só checar).
Skill professor-gcm-parnaiba. Artigos conferidos no Planalto em 28/11/2026 (GCM-PARNAIBA/fontes/notas-de-verificacao.md)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit
from kit import *

DATA = "28 de novembro de 2026"
kit.U = {1: ("UNIDADE 1", "Introdução e princípios"), 2: ("UNIDADE 2", "Aplicação da lei penal"), 3: ("UNIDADE 3", "Teoria do crime"),
         4: ("UNIDADE 4", "Consumação e tentativa"), 5: ("UNIDADE 5", "Excludentes de ilicitude"), 6: ("UNIDADE 6", "Culpabilidade"),
         7: ("UNIDADE 7", "Concurso de pessoas"), 8: ("UNIDADE 8", "Crimes contra a pessoa"), 9: ("UNIDADE 9", "Crimes contra o patrimônio"),
         10: ("UNIDADE 10", "Crimes contra a Administração Pública")}

# ================================================================ APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar esta <span class="hl">apostila</span></h1>
<p class="lead">Código Penal do zero, para quem nunca estudou Direito e quer acertar questões na prova objetiva da GCM de Parnaíba.</p>
{ATENCAO(p("<strong>Edital ainda não confirmado.</strong> O Edital nº 001/2026 da GCM de Parnaíba (banca IGEDUC) foi divulgado em 27/11/2026 e retirado em seguida, para republicação no Diário Oficial do Município. Até a confirmação, os temas desta apostila são <strong>CONTEÚDO ESTIMADO</strong>, escolhidos pelo perfil do cargo e pelos assuntos mais recorrentes de Código Penal em provas de guarda municipal. Quando o edital for republicado, compare o conteúdo programático oficial com o sumário."))}
{table(["Disciplina (distribuição provisória)","Questões","Pontos"],[["<b>Código Penal</b>","<b>15</b>","<b>37,5</b>"],["Conhecimentos Profissionais","15","37,5"],["Língua Portuguesa","10","15"],["Conhecimentos Regionais de Parnaíba","4","4"],["Informática","3","3"],["Raciocínio Lógico","3","3"]],["60%","20%",None])}
<p style="font-size:9.5pt;color:{C["muted"]}">Distribuição provisória, pendente de confirmação no edital oficial. Se confirmada, o Código Penal será uma das duas disciplinas de maior peso.</p>''', first=True)

add(pratica_title("Como estudar com esta apostila") +
 table(["Etapa", "O que fazer"], [
  ["1. Leia uma unidade por sessão", "Cada assunto segue 7 passos: O que é? · Em linguagem simples · Conceito jurídico · Exemplo · Como cai na prova · Pegadinha · Memorize"],
  ["2. Faça o treino rápido", "No fim de cada unidade há um Certo ou Errado. As respostas estão no fim da apostila"],
  ["3. Resolva as 30 questões", "Sem consultar. Depois confira o gabarito comentado, que fica em seção separada"],
  ["4. Anote seus erros", "Use o caderno de erros no fim da apostila"],
  ["5. Revise em D+1, D+7 e D+30", "Use os flashcards, as perguntas rápidas e o mapa mental"]], ["30%", None]) +
 table(["Prioridade de estudo (estimada)", "Unidades"], [
  ["<b>Alta</b>", "Teoria do crime (3) · Tentativa e arrependimentos (4) · Excludentes (5) · Crimes contra o patrimônio (9) · Crimes contra a Administração Pública (10)"],
  ["<b>Média</b>", "Princípios (1) · Culpabilidade e imputabilidade (6) · Concurso de pessoas (7) · Crimes contra a pessoa (8)"],
  ["<b>Base</b>", "Aplicação da lei penal (2): cai menos, mas explica o restante"]], ["30%", None]) +
 cards([("alert", "Atenção", "exceção ou detalhe que muda a resposta"), ("split", "Não confunda", "comparação entre institutos parecidos"), ("bulb", "Memorize", "o que precisa estar na ponta da língua")]) +
 PEGADINHA(p("Os quadros vermelhos mostram como a banca tenta enganar: leia o “Errado” e o “Certo” com atenção.")))

toc_page([
 ("u", "UNIDADE 1 · INTRODUÇÃO E PRINCÍPIOS", "U1"), ("", "1. O que é Direito Penal · 2. Crime e contravenção · 3. Princípios", "A01"),
 ("u", "UNIDADE 2 · APLICAÇÃO DA LEI PENAL", "U2"), ("", "4. Lei penal no tempo · 5. Tempo e lugar do crime", "A04"),
 ("u", "UNIDADE 3 · TEORIA DO CRIME", "U3"), ("", "6. Conceito de crime · 7. Fato típico · 8. Omissão · 9. Dolo e culpa · 10. Erro de tipo", "A06"),
 ("u", "UNIDADE 4 · CONSUMAÇÃO, TENTATIVA E ARREPENDIMENTOS", "U4"), ("", "11. Tentativa · 12. Desistência e arrependimento eficaz · 13. Arrependimento posterior · 14. Crime impossível", "A11"),
 ("u", "UNIDADE 5 · EXCLUDENTES DE ILICITUDE", "U5"), ("", "15. As quatro excludentes · 16. Estado de necessidade · 17. Legítima defesa", "A15"),
 ("u", "UNIDADE 6 · CULPABILIDADE E IMPUTABILIDADE", "U6"), ("", "18. Elementos · 19. Imputabilidade · 20. Emoção, paixão e embriaguez", "A18"),
 ("u", "UNIDADE 7 · CONCURSO DE PESSOAS", "U7"), ("", "21. Autoria, participação e arts. 29 a 31", "A21"),
 ("u", "UNIDADE 8 · CRIMES CONTRA A PESSOA", "U8"), ("", "22. Homicídio e feminicídio · 23. Lesão corporal · 24. Honra · 25. Liberdade", "A22"),
 ("u", "UNIDADE 9 · CRIMES CONTRA O PATRIMÔNIO", "U9"), ("", "26. Furto · 27. Roubo · 28. Extorsão · 29. Apropriação, estelionato e receptação · 30. Imunidades", "A26"),
 ("u", "UNIDADE 10 · CRIMES CONTRA A ADMINISTRAÇÃO PÚBLICA", "U10"), ("", "31. Funcionário público · 32. Crimes de funcionário · 33. Concussão x corrupção · 34. Crimes de particular", "A31"),
 ("u", "PRÁTICA E REVISÃO", "RV"), ("", "30 questões autorais", "R3"), ("", "Gabarito comentado e respostas dos treinos", "R4"), ("", "Resumo estratégico, mapa mental, flashcards, perguntas rápidas e checklist", "R1")])

import pg, pe  # Unidades 1 a 10

# ================================================================ QUESTÕES
Q = [
 ("Princípios", "Sobre o princípio da legalidade em matéria penal, é correto afirmar:",
  ["somente a lei pode definir crimes e cominar penas.", "decreto do Prefeito pode criar crime de alcance municipal.", "medida provisória pode criar crimes em caso de urgência.", "o costume local pode criar crimes, desde que antigo.", "portaria do Ministério da Justiça pode fixar penas."], "A",
  "CF, art. 5º, XXXIX, e CP, art. 1º: não há crime sem lei anterior que o defina, nem pena sem prévia cominação legal. Decreto, portaria e costume não criam crimes; a CF proíbe medida provisória sobre direito penal.", "Crime e pena: só por LEI."),
 ("Lei penal no tempo", "Uma lei nova deixa de considerar crime determinada conduta. Quanto a quem já foi condenado definitivamente por essa conduta:",
  ["cessam a execução e os efeitos penais da sentença condenatória.", "a condenação continua valendo, pois transitou em julgado.", "a pena é apenas reduzida pela metade.", "a lei nova só vale para fatos futuros.", "depende de autorização do Ministério Público."], "A",
  "Art. 2º do CP (abolitio criminis): ninguém pode ser punido por fato que lei posterior deixa de considerar crime, cessando a execução e os efeitos penais da sentença.", "Abolitio criminis alcança até a condenação definitiva."),
 ("Tempo do crime", "Um rapaz de 17 anos efetua disparos contra a vítima, que morre dois meses depois, quando o autor já completou 18 anos. Pelo Código Penal:",
  ["considera-se praticado o crime no momento da conduta, quando o autor era menor de idade.", "considera-se praticado o crime no momento da morte, quando o autor era maior.", "o autor responde pelo Código Penal com pena reduzida.", "aplica-se a teoria da ubiquidade ao tempo do crime.", "o crime só existe se a vítima morrer no mesmo dia."], "A",
  "Art. 4º: teoria da atividade. O tempo do crime é o momento da ação ou omissão, ainda que o resultado ocorra depois. Como era menor de 18 anos, é inimputável (art. 27) e responde pelo ECA. Ubiquidade é a regra do LUGAR do crime.", "LUTA: Lugar-Ubiquidade, Tempo-Atividade."),
 ("Lugar do crime", "Para definir o lugar do crime, o Código Penal adota a teoria:",
  ["da ubiquidade: considera-se o lugar da ação ou omissão e também o do resultado.", "da atividade: apenas o lugar da conduta.", "do resultado: apenas o lugar onde o resultado ocorreu.", "do domicílio do autor.", "do domicílio da vítima."], "A",
  "Art. 6º: considera-se praticado o crime no lugar da ação ou omissão, no todo ou em parte, bem como onde se produziu ou deveria produzir-se o resultado.", "Lugar = Ubiquidade."),
 ("Conceito de crime", "Pelo conceito analítico tripartite, crime é:",
  ["fato típico, ilícito e culpável.", "fato típico e punível.", "qualquer conduta imoral.", "fato ilícito e culpável, apenas.", "conduta prevista em contravenção penal."], "A",
  "A teoria tripartite define crime como fato típico, ilícito (antijurídico) e culpável.", "Três degraus: típico, ilícito, culpável."),
 ("Omissão relevante", "Segundo o art. 13, § 2º, do Código Penal, NÃO tem o dever jurídico de agir para evitar o resultado:",
  ["o pedestre que apenas passa pelo local e não tem nenhum vínculo com a vítima.", "quem tem por lei obrigação de cuidado, proteção ou vigilância.", "quem, de outra forma, assumiu a responsabilidade de impedir o resultado.", "quem, com seu comportamento anterior, criou o risco do resultado.", "a mãe em relação ao filho bebê."], "A",
  "O dever de agir existe nas três hipóteses do art. 13, § 2º: dever legal (como a mãe), quem assumiu a responsabilidade e quem criou o risco. O pedestre sem vínculo não responde pelo resultado, embora possa responder por omissão de socorro (art. 135).", "Dever de agir: LEI, ASSUMIU, CRIOU O RISCO."),
 ("Dolo e culpa", "Sobre dolo e culpa, assinale a alternativa correta:",
  ["salvo os casos expressos em lei, ninguém pode ser punido por fato previsto como crime senão quando o pratica dolosamente.", "todo crime admite a modalidade culposa.", "a imperícia é a falta de cuidado por omissão.", "age com dolo eventual quem não prevê o resultado.", "o crime culposo exige a intenção de produzir o resultado."], "A",
  "Art. 18, parágrafo único: o crime culposo é excepcional e precisa de previsão expressa. Imperícia é falta de aptidão técnica (a omissão é a negligência); no dolo eventual o agente prevê e assume o risco.", "Culposo só se a lei disser."),
 ("Dolo eventual", "Um motorista, em alta velocidade perto de uma escola, percebe que pode atropelar alguém e pensa “se acontecer, tanto faz”. Atropela e mata uma criança. Em tese, houve:",
  ["dolo eventual.", "culpa consciente.", "culpa inconsciente.", "caso fortuito.", "crime impossível."], "A",
  "No dolo eventual o agente prevê o resultado e o aceita (“tanto faz”). Na culpa consciente ele prevê, mas acredita sinceramente que não vai acontecer.", "Aceitou o risco = dolo eventual."),
 ("Erro de tipo", "Ao sair de uma academia, Pedro leva a mochila de outra pessoa, idêntica à sua, acreditando ser a própria. Nesse caso:",
  ["há erro de tipo, que exclui o dolo; como não existe furto culposo, não há crime.", "Pedro responde por furto doloso.", "Pedro responde por furto culposo.", "há erro de proibição, que reduz a pena de um sexto a um terço.", "há legítima defesa putativa."], "A",
  "Art. 20: o erro sobre elemento do tipo (“coisa alheia”) exclui o dolo, permitindo a punição por culpa se prevista em lei. Não existe furto culposo, logo o fato é atípico.", "Erro de TIPO = erro sobre o FATO."),
 ("Tentativa", "Salvo disposição em contrário, a tentativa é punida com a pena do crime consumado:",
  ["diminuída de um a dois terços.", "diminuída de um sexto a um terço.", "reduzida pela metade, sempre.", "aumentada de um terço.", "sem qualquer redução."], "A",
  "Art. 14, parágrafo único. A fração de 1/6 a 1/3 aparece, por exemplo, na participação de menor importância e no erro de proibição evitável.", "Tentativa: 1/3 a 2/3."),
 ("Tentativa x desistência", "Durante a ronda, a GCM surpreende um homem que forçava a porta de uma loja. Ao ver a viatura, ele foge sem levar nada. Em tese, ocorreu:",
  ["tentativa, pois a consumação foi impedida por circunstância alheia à vontade do agente.", "desistência voluntária.", "arrependimento eficaz.", "arrependimento posterior.", "crime impossível."], "A",
  "A execução começou e foi interrompida pela chegada da guarda (fator externo): tentativa (art. 14, II). Na desistência voluntária, o agente para porque quer.", "Quero, mas não posso = tentativa."),
 ("Arrependimento eficaz", "Após ministrar veneno à vítima, o agente se arrepende, leva-a ao hospital e ela sobrevive, com lesões. Pelo art. 15 do Código Penal, ele:",
  ["responde apenas pelos atos já praticados (lesão corporal).", "responde por tentativa de homicídio com pena reduzida.", "fica isento de qualquer pena.", "responde por homicídio consumado.", "tem a pena reduzida de um a dois terços."], "A",
  "Arrependimento eficaz: o agente encerrou a execução, mas impediu o resultado. Responde só pelos atos já praticados.", "Impediu o resultado = só os atos praticados."),
 ("Arrependimento posterior", "São requisitos do arrependimento posterior (art. 16), EXCETO:",
  ["ser o crime cometido com grave ameaça à pessoa.", "reparação do dano ou restituição da coisa.", "ato voluntário do agente.", "ocorrer até o recebimento da denúncia ou da queixa.", "crime cometido sem violência à pessoa."], "A",
  "O arrependimento posterior só cabe em crimes SEM violência ou grave ameaça à pessoa, com reparação ou restituição voluntária, até o recebimento da denúncia ou queixa. A pena é reduzida de 1/3 a 2/3.", "Posterior: sem violência, reparou, voluntário, até a denúncia."),
 ("Crime impossível", "Não se pune a tentativa quando é impossível consumar o crime por:",
  ["ineficácia absoluta do meio ou absoluta impropriedade do objeto.", "ineficácia relativa do meio.", "falha eventual da arma utilizada.", "desistência do agente.", "intervenção da polícia."], "A",
  "Art. 17. Se a ineficácia é apenas relativa (a arma às vezes funciona), há tentativa punível.", "Crime impossível: ABSOLUTA ineficácia ou impropriedade."),
 ("Excludentes", "NÃO é causa de exclusão da ilicitude prevista no art. 23 do Código Penal:",
  ["a coação moral irresistível.", "o estado de necessidade.", "a legítima defesa.", "o estrito cumprimento de dever legal.", "o exercício regular de direito."], "A",
  "A coação moral irresistível (art. 22) afasta a culpabilidade (inexigibilidade de conduta diversa), não a ilicitude.", "Ilicitude: NE-LE-ES-EX."),
 ("Legítima defesa", "Um homem ataca uma senhora com uma faca na praça. Um guarda municipal intervém e o imobiliza com a força necessária. A conduta do guarda caracteriza:",
  ["legítima defesa de terceiro.", "estado de necessidade.", "exercício arbitrário das próprias razões.", "crime de lesão corporal, sem excludente.", "obediência hierárquica."], "A",
  "Art. 25: repelir, com moderação e os meios necessários, injusta agressão atual a direito de outrem. Havia agressão humana injusta, não um simples perigo (estado de necessidade).", "Agressão injusta = legítima defesa."),
 ("Excesso", "Sobre as excludentes de ilicitude, é correto afirmar:",
  ["o agente responde pelo excesso doloso ou culposo em qualquer delas.", "quem age em legítima defesa nunca responde pelo excesso.", "o excesso só é punido se for doloso.", "o excesso só é punido no estado de necessidade.", "o excesso transforma automaticamente o fato em homicídio qualificado."], "A",
  "Art. 23, parágrafo único: em qualquer das hipóteses, o agente responde pelo excesso doloso ou culposo.", "Excesso: responde."),
 ("Estado de necessidade", "Durante um incêndio, um bombeiro militar alega estado de necessidade para não entrar no prédio. Pelo Código Penal:",
  ["não pode alegar estado de necessidade quem tinha o dever legal de enfrentar o perigo.", "o bombeiro pode alegar estado de necessidade normalmente.", "o estado de necessidade exige agressão humana injusta.", "basta que o perigo seja futuro e incerto.", "o estado de necessidade só protege direito próprio."], "A",
  "Art. 24, § 1º. O estado de necessidade exige perigo atual (não agressão) e protege direito próprio ou alheio.", "Dever legal de enfrentar o perigo: não alega."),
 ("Imputabilidade", "Sobre a imputabilidade penal, assinale a alternativa correta:",
  ["os menores de 18 anos são penalmente inimputáveis, sujeitos à legislação especial.", "a embriaguez voluntária exclui a imputabilidade.", "a emoção e a paixão excluem a imputabilidade.", "o semi-imputável é isento de pena.", "o menor de 18 anos responde pelo Código Penal com pena reduzida."], "A",
  "Art. 27. A embriaguez voluntária ou culposa e a emoção ou paixão não excluem a imputabilidade (art. 28); o semi-imputável tem a pena reduzida de 1/3 a 2/3 (art. 26, parágrafo único).", "Menor de 18: inimputável (ECA)."),
 ("Embriaguez", "É isento de pena o agente que, ao tempo do fato, era inteiramente incapaz de entender o caráter ilícito em razão de embriaguez:",
  ["completa, proveniente de caso fortuito ou força maior.", "voluntária e completa.", "culposa e completa.", "preordenada (bebeu para ter coragem).", "incompleta, de qualquer origem."], "A",
  "Art. 28, § 1º. A embriaguez voluntária ou culposa não exclui a imputabilidade; a incompleta por caso fortuito apenas reduz a pena (§ 2º).", "Isenta: COMPLETA + caso fortuito ou força maior."),
 ("Obediência hierárquica", "Um subordinado cumpre ordem MANIFESTAMENTE ilegal de seu superior e agride uma pessoa rendida. Nesse caso:",
  ["o subordinado também responde pelo crime, pois a ordem era manifestamente ilegal.", "só o superior responde, sempre.", "ninguém responde, por haver hierarquia.", "o subordinado fica isento de pena por obediência hierárquica.", "há legítima defesa."], "A",
  "Art. 22: só é punível o autor da ordem quando a ordem NÃO é manifestamente ilegal. Sendo manifestamente ilegal, o subordinado também responde.", "Ordem manifestamente ilegal não se cumpre."),
 ("Concurso de pessoas", "Se a participação no crime for de menor importância, a pena pode ser diminuída de:",
  ["um sexto a um terço.", "um a dois terços.", "metade.", "dois terços, sempre.", "um quarto."], "A",
  "Art. 29, § 1º. Na cooperação dolosamente distinta (§ 2º), aplica-se a pena do crime menos grave, aumentada até metade se o resultado mais grave era previsível.", "Menor importância: 1/6 a 1/3."),
 ("Comunicabilidade", "Um servidor público e um amigo particular, que conhece a condição do servidor, desviam juntos dinheiro da prefeitura. O particular:",
  ["também responde por peculato, pois a condição de funcionário público é elementar do crime e se comunica.", "responde apenas por furto simples.", "não responde por nada, pois não é servidor.", "responde por receptação.", "responde por apropriação indébita."], "A",
  "Art. 30: as condições de caráter pessoal não se comunicam, salvo quando elementares do crime. “Funcionário público” é elementar do peculato.", "Elementar se comunica."),
 ("Homicídio", "Pela redação vigente do Código Penal, o feminicídio:",
  ["é crime autônomo, previsto no art. 121-A, com pena de reclusão de 20 a 40 anos.", "é qualificadora do homicídio, prevista no art. 121, § 2º, VI.", "é contravenção penal.", "tem pena de reclusão de 6 a 20 anos.", "não está previsto no Código Penal."], "A",
  "A Lei nº 14.994/2024 revogou o inciso VI do § 2º do art. 121 e criou o art. 121-A (matar a mulher por razões da condição do sexo feminino), com reclusão de 20 a 40 anos.", "Feminicídio: art. 121-A, 20 a 40."),
 ("Lesão corporal", "Constitui lesão corporal GRAVÍSSIMA (art. 129, § 2º):",
  ["a perda ou inutilização de membro, sentido ou função.", "a incapacidade para as ocupações habituais por mais de 30 dias.", "a debilidade permanente de membro, sentido ou função.", "a aceleração de parto.", "o perigo de vida."], "A",
  "As demais hipóteses são de lesão grave (§ 1º). Debilidade é grave; perda ou inutilização é gravíssima.", "Debilidade = grave; perda = gravíssima."),
 ("Crimes contra a honra", "Maria espalha no bairro, sabendo ser mentira, que o vizinho “furtou a bicicleta da escola municipal na semana passada”. Em tese, Maria cometeu:",
  ["calúnia.", "difamação.", "injúria.", "ameaça.", "denunciação caluniosa."], "A",
  "Calúnia (art. 138): imputar falsamente a alguém fato definido como crime (o furto). Difamação é fato ofensivo não criminoso; injúria é ofensa sem imputação de fato.", "Crime falso = calúnia."),
 ("Furto x roubo", "Dois homens, usando uma faca, abordam uma pessoa na orla e levam seu celular. A conduta configura, em tese:",
  ["roubo com causa de aumento de pena.", "furto qualificado pelo concurso de pessoas.", "furto simples.", "extorsão mediante sequestro.", "estelionato."], "A",
  "Há subtração mediante grave ameaça: roubo (art. 157). O concurso de duas ou mais pessoas e o uso de arma branca são causas de aumento de 1/3 até a metade (§ 2º, II e VII).", "Violência ou grave ameaça = roubo."),
 ("Extorsão", "O criminoso obriga a vítima, sob ameaça, a fazer uma transferência bancária para a conta dele, mantendo-a no carro até concluir a operação. Esse fato se amolda ao crime de:",
  ["extorsão mediante restrição da liberdade da vítima (art. 158, § 3º).", "furto mediante fraude.", "estelionato.", "apropriação indébita.", "receptação."], "A",
  "Na extorsão a colaboração da vítima é indispensável (ela faz a transferência). A restrição da liberdade como condição para obter a vantagem é o art. 158, § 3º (o chamado “sequestro relâmpago”).", "Vítima obrigada a colaborar = extorsão."),
 ("Crimes funcionais", "Um fiscal municipal diz ao comerciante: “ou você me paga R$ 500, ou eu interdito sua loja”. Em tese, o fiscal cometeu:",
  ["concussão.", "corrupção passiva.", "corrupção ativa.", "prevaricação.", "advocacia administrativa."], "A",
  "O verbo EXIGIR caracteriza a concussão (art. 316). Solicitar ou receber seria corrupção passiva (art. 317); oferecer, por particular, corrupção ativa (art. 333).", "EXIGIR = concussão."),
 ("Crimes de particular", "Durante a fiscalização de comércio ambulante, o vendedor empurra o guarda municipal e o ameaça para impedir o recolhimento legal da mercadoria, que acaba não sendo recolhida. Em tese, o vendedor cometeu:",
  ["resistência, na forma qualificada, pois o ato não se executou.", "desobediência.", "desacato.", "corrupção ativa.", "prevaricação."], "A",
  "Art. 329: opor-se a ato legal mediante violência ou ameaça. Se o ato não se executa, a pena é de reclusão de 1 a 3 anos (§ 1º), sem prejuízo da pena da violência. Desobediência não envolve violência; desacato é ofender ou humilhar.", "Violência contra ato legal = resistência."),
]
questoes(Q)
respostas_treinos()

# ================================================================ REVISÃO
add('<div class="marker">§§R1§§</div><div class="unit"><span class="u">REVISÃO</span><span class="t">Véspera da prova</span></div><h1 class="big">Resumo <span class="hl">estratégico</span></h1><p class="lead">O mínimo indispensável de cada unidade, em uma página.</p>' +
 table(["Tema", "O que mais cai"], [
  ["Princípios", "Legalidade e anterioridade (só a lei cria crime); lei mais benéfica retroage; intranscendência; insignificância (4 vetores do STF)"],
  ["Lei penal", "Abolitio criminis cessa execução e efeitos penais; tempo = atividade (art. 4º); lugar = ubiquidade (art. 6º)"],
  ["Teoria do crime", "Crime = típico + ilícito + culpável; omissão relevante (lei, assumiu, criou o risco); culposo só se previsto em lei; erro de tipo exclui o dolo"],
  ["Iter criminis", "Tentativa reduz 1/3 a 2/3; desistência e arrependimento eficaz: só os atos praticados; arrependimento posterior: sem violência, até a denúncia, reduz 1/3 a 2/3; crime impossível: ineficácia absoluta"],
  ["Excludentes", "Necessidade, legítima defesa, dever legal, exercício de direito; excesso punível; dever legal de enfrentar o perigo impede a alegação de necessidade"],
  ["Culpabilidade", "Imputabilidade, consciência da ilicitude, exigibilidade; menor de 18 inimputável; embriaguez voluntária não exclui; semi-imputável reduz 1/3 a 2/3"],
  ["Concurso", "Na medida da culpabilidade; menor importância 1/6 a 1/3; elementar se comunica"],
  ["Contra a pessoa", "Homicídio 6 a 20 (qualificado 12 a 30); feminicídio no art. 121-A (20 a 40); grave x gravíssima; calúnia x difamação x injúria"],
  ["Patrimônio", "Furto 1 a 6 (sem violência); roubo 6 a 10 (com violência); latrocínio 24 a 30; extorsão: vítima colabora; imunidades e exceções do art. 183"],
  ["Administração", "Funcionário público penal (art. 327); peculato; exigir = concussão; solicitar/receber = corrupção passiva; oferecer = corrupção ativa; resistência x desobediência x desacato"]], ["20%", None]))

add(pratica_title("Mapa mental textual") + mapa_textual("CÓDIGO PENAL · GCM PARNAÍBA", [
  ("Fundamentos", ["Legalidade e anterioridade (art. 1º)", "Retroatividade benéfica (art. 2º)", "LUTA: lugar-ubiquidade, tempo-atividade"]),
  ("Crime (tripartite)", ["Fato típico: conduta, resultado, nexo, tipicidade", "Ilicitude: afastada pelas excludentes do art. 23", "Culpabilidade: imputabilidade, consciência, exigibilidade"]),
  ("Caminho do crime", ["Cogitação, preparação, execução, consumação", "Tentativa (fator externo) x desistência (vontade)", "Arrependimento eficaz, posterior e crime impossível"]),
  ("Pessoas e participação", ["Autor x partícipe", "Menor importância 1/6 a 1/3", "Elementar se comunica (art. 30)"]),
  ("Crimes em espécie", ["Pessoa: homicídio, feminicídio, lesão, honra, ameaça", "Patrimônio: furto, roubo, extorsão, estelionato, receptação", "Administração: peculato, concussão, corrupção, resistência, desobediência, desacato"])]))

flashcards([
 ("PRINCÍPIOS", "Quem pode criar crime?", "Somente a lei (CF, art. 5º, XXXIX; CP, art. 1º)."),
 ("PRINCÍPIOS", "A lei penal retroage?", "Só para beneficiar o réu."),
 ("LEI PENAL", "Tempo do crime?", "Momento da ação ou omissão (atividade, art. 4º)."),
 ("LEI PENAL", "Lugar do crime?", "Lugar da conduta ou do resultado (ubiquidade, art. 6º)."),
 ("CRIME", "Conceito analítico?", "Fato típico, ilícito e culpável."),
 ("CRIME", "Quem tem o dever de agir (art. 13, § 2º)?", "Quem tem dever legal; quem assumiu a responsabilidade; quem criou o risco."),
 ("DOLO E CULPA", "Dolo eventual?", "Prever o resultado e assumir o risco de produzi-lo."),
 ("DOLO E CULPA", "Modalidades de culpa?", "Imprudência, negligência e imperícia."),
 ("ERRO", "Erro de tipo?", "Erro sobre o fato: exclui o dolo (art. 20)."),
 ("TENTATIVA", "Redução da tentativa?", "De um a dois terços (art. 14, parágrafo único)."),
 ("TENTATIVA", "Desistência voluntária?", "O agente para por vontade própria; responde só pelos atos praticados."),
 ("TENTATIVA", "Arrependimento posterior?", "Sem violência, reparou ou restituiu, voluntário, até a denúncia: reduz 1/3 a 2/3."),
 ("EXCLUDENTES", "Quais são?", "Estado de necessidade, legítima defesa, estrito cumprimento de dever legal e exercício regular de direito."),
 ("EXCLUDENTES", "Requisitos da legítima defesa?", "Injusta agressão, atual ou iminente, a direito próprio ou alheio, com moderação e os meios necessários."),
 ("CULPABILIDADE", "Menor de 18 anos?", "Inimputável, sujeito à legislação especial (ECA)."),
 ("CULPABILIDADE", "Embriaguez voluntária?", "Não exclui a imputabilidade (art. 28, II)."),
 ("CONCURSO", "Participação de menor importância?", "Reduz de um sexto a um terço (art. 29, § 1º)."),
 ("PESSOA", "Onde está o feminicídio?", "Art. 121-A (Lei 14.994/2024), reclusão de 20 a 40 anos."),
 ("PESSOA", "Calúnia x difamação x injúria?", "Crime falso · fato desonroso · ofensa sem fato."),
 ("PATRIMÔNIO", "Furto x roubo?", "Roubo tem violência ou grave ameaça à pessoa."),
 ("PATRIMÔNIO", "Pena do latrocínio?", "Reclusão de 24 a 30 anos, e multa (art. 157, § 3º, II)."),
 ("ADMINISTRAÇÃO", "Exigir vantagem indevida?", "Concussão (art. 316)."),
 ("ADMINISTRAÇÃO", "Solicitar ou receber vantagem?", "Corrupção passiva (art. 317)."),
 ("ADMINISTRAÇÃO", "Resistência x desobediência?", "Resistência tem violência ou ameaça; desobediência, não.")])

perguntas_rapidas([
 ("Qual é o número do Decreto-Lei que instituiu o Código Penal?", "Decreto-Lei nº 2.848/1940."),
 ("Lei nova mais grave alcança fatos anteriores?", "Não. Só a lei mais benéfica retroage."),
 ("Qual teoria define o tempo do crime?", "Teoria da atividade (art. 4º)."),
 ("Qual teoria define o lugar do crime?", "Teoria da ubiquidade (art. 6º)."),
 ("Quais são os três elementos do conceito analítico de crime?", "Fato típico, ilicitude e culpabilidade."),
 ("Existe furto culposo no Código Penal?", "Não."),
 ("Qual a fração de redução da tentativa?", "De um a dois terços."),
 ("Na desistência voluntária, por que o agente responde?", "Somente pelos atos já praticados."),
 ("Até quando cabe o arrependimento posterior?", "Até o recebimento da denúncia ou da queixa."),
 ("Cabe arrependimento posterior no roubo?", "Não, porque há violência ou grave ameaça."),
 ("Cite as quatro excludentes de ilicitude.", "Estado de necessidade, legítima defesa, estrito cumprimento de dever legal e exercício regular de direito."),
 ("Cabe legítima defesa contra agressão já encerrada?", "Não. A agressão deve ser atual ou iminente."),
 ("Emoção e paixão excluem a imputabilidade?", "Não (art. 28, I)."),
 ("O que acontece com o semi-imputável?", "A pena pode ser reduzida de um a dois terços."),
 ("As condições pessoais se comunicam no concurso de pessoas?", "Não, salvo quando elementares do crime."),
 ("Qual a pena do homicídio simples?", "Reclusão de 6 a 20 anos."),
 ("Debilidade permanente de membro é lesão grave ou gravíssima?", "Grave."),
 ("Qual a diferença entre roubo e extorsão?", "Na extorsão, a colaboração da vítima é indispensável."),
 ("O que caracteriza a concussão?", "Exigir vantagem indevida em razão da função."),
 ("Funcionário público para fins penais precisa ser remunerado?", "Não. Basta exercer cargo, emprego ou função pública, ainda que transitoriamente ou sem remuneração.")])

add(pratica_title("O que você precisa memorizar") + table(["Item", "Memorize"], [
  ["Frações de redução", "Tentativa, arrependimento posterior, semi-imputabilidade e embriaguez incompleta fortuita: 1/3 a 2/3 · Erro de proibição evitável e participação de menor importância: 1/6 a 1/3 · Homicídio privilegiado: 1/6 a 1/3"],
  ["Aumentos", "Furto noturno: + metade · Roubo (§ 2º): 1/3 a 1/2 · Arma de fogo: + 2/3 · Cargo em comissão nos crimes funcionais: + 1/3"],
  ["Penas-chave", "Homicídio 6 a 20 · qualificado 12 a 30 · feminicídio 20 a 40 · furto 1 a 6 · roubo 6 a 10 · latrocínio 24 a 30 · peculato, concussão, corrupção passiva e ativa 2 a 12"],
  ["Teorias", "Tempo: atividade · Lugar: ubiquidade · Crime: tripartite"],
  ["Verbos", "Exigir (concussão) · solicitar, receber, aceitar promessa (corrupção passiva) · oferecer, prometer (corrupção ativa) · apropriar-se, desviar (peculato)"],
  ["Diferenças", "Tentativa x desistência · legítima defesa x estado de necessidade · grave x gravíssima · calúnia x difamação x injúria · furto x roubo x extorsão · resistência x desobediência x desacato"]], ["22%", None]))

add(checklist([
  "Sei explicar legalidade, anterioridade e retroatividade benéfica",
  "Diferencio tempo (atividade) e lugar (ubiquidade) do crime",
  "Sei os três elementos do crime e o que acontece se faltar cada um",
  "Sei as três hipóteses do dever de agir (art. 13, § 2º)",
  "Diferencio dolo eventual e culpa consciente",
  "Diferencio tentativa, desistência, arrependimento eficaz e posterior",
  "Sei as quatro excludentes e os requisitos da legítima defesa",
  "Sei o que exclui e o que não exclui a imputabilidade",
  "Sei as frações do concurso de pessoas e a regra das elementares",
  "Diferencio homicídio simples, privilegiado, qualificado e feminicídio",
  "Diferencio lesão grave e gravíssima",
  "Diferencio calúnia, difamação e injúria",
  "Diferencio furto, roubo, extorsão e estelionato",
  "Sei o conceito penal de funcionário público",
  "Diferencio concussão, corrupção passiva e corrupção ativa",
  "Diferencio resistência, desobediência e desacato"]) +
 pratica_title("Revisões espaçadas") + revisoes_espacadas("Código Penal"))

add(pratica_title("Caderno de erros") + p("Anote cada questão que errar, o motivo do erro e a regra correta. Revise esta página antes de cada simulado.") + caderno_erros(12))

referencias(f'''<h3>Edital</h3><ul>
<li>Aviso de publicação do Edital nº 001/2026 da GCM de Parnaíba (Diário Oficial do Município nº 4344, de 26/11/2026): banca IGEDUC. O edital foi retirado do site da banca para republicação no Diário Oficial; até {DATA}, não foi localizado o edital republicado. <b>Os temas desta apostila são CONTEÚDO ESTIMADO.</b></li>
<li>Tentativa de consulta a edital anterior de guarda municipal do Piauí (GCM de Teresina, NUCEPE): o arquivo não estava disponível (link quebrado).</li></ul>
<h3>Legislação conferida (portal do Planalto, texto compilado)</h3><ul>
<li>Código Penal (Decreto-Lei nº 2.848/1940): arts. 1º a 31 (Parte Geral, redação da Lei nº 7.209/1984; art. 25, parágrafo único, incluído pela Lei nº 13.964/2019) e arts. 121, 121-A, 122, 129, 138 a 140, 145, 147, 148, 150, 155, 157, 158, 159, 168, 171, 180 a 183, 312, 313, 316, 317, 319 a 321, 327, 329 a 333, inclusive as alterações das Leis nº 14.994/2024 (feminicídio no art. 121-A) e nº 15.397/2026 (novas penas de furto, roubo, latrocínio, estelionato e receptação).</li>
<li>Constituição Federal, art. 5º, XXXIX a XLVII, e art. 62, § 1º, I, “b”.</li></ul>
<h3>Questões</h3><ul><li>As 30 questões e os treinos são autorais, elaborados para esta apostila. Nenhuma foi aplicada por banca.</li></ul>''',
 '<strong>Limitações:</strong> o edital oficial não estava disponível (retirado para republicação), por isso os conteúdos são estimados; os sites da banca e de imprensa bloquearam o acesso automatizado; o texto compilado do Planalto foi lido por trechos e pode não refletir alterações publicadas depois desta data; a Lei nº 15.397/2026 revogou a regra de ação penal do estelionato (art. 171, § 5º), e esta apostila não afirma qual regra a substituiu; a referência ao princípio da insignificância resume a jurisprudência do STF, sem conferência do inteiro teor dos acórdãos. Penas e redações mudam com frequência: confira o texto oficial antes da prova.', DATA)
encerramento("01", "Código Penal", "Próxima sugestão: <strong>Apostila 02 · Conhecimentos Profissionais</strong> (Lei nº 13.022/2014 e legislação da GCM de Parnaíba).", "novembro de 2026")
gravar(HERE, "Apostila 01 — Código Penal — GCM Parnaíba", Q)
