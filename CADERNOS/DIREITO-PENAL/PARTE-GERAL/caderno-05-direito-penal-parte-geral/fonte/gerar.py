"""Gera miolo.html do Caderno 05: Direito Penal — Parte Geral. Uso: python3 gerar.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from componentes import *

DATA = "25 de novembro de 2026"
P = []
def add(html, first=False): P.append(page(f'<div class="marker">§§P{len(P)+1:03d}§§</div>' + html, first))
U1, U2, U3, U4 = "UNIDADE 1", "UNIDADE 2", "UNIDADE 3", "UNIDADE 4"
T1, T2, T3, T4 = "Fundamentos", "A lei penal", "Teoria do crime", "Penas"
def cp(x): return f"{x} · Código Penal"
def cf(x): return f"{x} · Constituição Federal"
def p(t): return f"<p>{t}</p>"
def colors(*keys):
    m = {"b":(C['blue'],C['sky']),"g":(C['green'],C['greensoft']),"o":(C['golddeep'],C['goldsoft']),"r":(C['red'],C['redsoft']),"n":(C['navy'],'#e6e7ea')}
    return [m[k] for k in keys]
def atencao(html, kws):
    add(pratica_title('Atenção na prova') + html + kw(kws))

# ================================================================ APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">A Parte Geral do Código Penal explicada com situações ilustradas e diagramas.</p>
<p>Este é o <strong>Caderno 05 da coleção</strong>, dedicado ao <strong>Direito Penal: Parte Geral</strong>. A Parte Geral (arts. 1º a 120 do Código Penal) traz as <strong>regras que valem para todos os crimes</strong>: quando a lei penal se aplica, o que é crime, quando alguém pode ser punido e quais penas existem.</p>
<p>É matéria de base para concursos de <strong>Guarda Municipal</strong>, <strong>polícias</strong> e <strong>tribunais</strong>. Conceitos abstratos como dolo eventual, ilicitude e culpabilidade aparecem aqui como <strong>cenas do dia a dia</strong>, com personagens e diagramas. Em geral, cada assunto ocupa <strong>duas páginas</strong>:</p>
{cards([("book","Página 1 · Entenda","Título, texto da lei, <b>Traduzindo o juridiquês</b> e a faixa <b>Memorize</b>.", C['golddeep']),
        ("bulb","Página 2 · Pratique","<b>Entenda na prática</b> com uma situação ilustrada, exemplo e <b>Pegadinha de concurso</b>.", C['blue'])],2)}
<h3>Recursos especiais deste caderno</h3>
{table(["Recurso","Onde está"],[
 ["Diagrama completo da estrutura do crime","Unidade 3"],
 ["Cena ilustrada: dolo eventual x culpa consciente","Unidade 3"],
 ["Fluxograma “Houve crime?”","Unidade 3"],
 ["Árvore das espécies de pena e régua dos regimes","Unidade 4"],
 ["Treinos Certo ou Errado e 24 questões autorais comentadas","Fim de cada unidade e prática final"]],["56%",None])}
{lembre(f'''<p><strong>Material pesquisado e atualizado em: {DATA}.</strong> Os artigos do Código Penal, da Lei de Introdução ao Código Penal, da Lei das Contravenções Penais e da Constituição citados foram conferidos no portal da legislação federal (Planalto). As questões são <strong>autorais</strong>. As limitações da verificação estão nas Referências.</p>''', "Fontes e atualização")}''', first=True)

TOC = [("u","UNIDADE 1 · FUNDAMENTOS","U1"),("","1. Conceito de Direito Penal","A01"),("","2. Finalidade do Direito Penal e da pena","A02"),("","3. Princípios do Direito Penal","A03"),
 ("u","UNIDADE 2 · A LEI PENAL","U2"),("","4. Legalidade e anterioridade","A04"),("","5. Irretroatividade e retroatividade benéfica","A05"),("","6. Aplicação da lei penal no tempo","A06"),("","7. Aplicação da lei penal no espaço (introdução)","A07"),
 ("u","UNIDADE 3 · TEORIA DO CRIME","U3"),("","8. Infração penal: crime e contravenção","A08"),("","9. Conceito de crime e sua estrutura","A09"),("","10. Sujeito ativo e sujeito passivo","A10"),("","11. Dolo e culpa","A11"),("","12. Noções de tipicidade","A12"),("","13. Ilicitude","A13"),("","14. Culpabilidade","A14"),("","15. Houve crime? (fluxograma)","A15"),
 ("u","UNIDADE 4 · PENAS","U4"),("","16. Penas: conceito e limites constitucionais","A16"),("","17. Espécies de penas","A17"),("","18. Penas privativas de liberdade e regimes","A18"),("","19. Restritivas de direitos e multa","A19"),
 ("u","REVISÃO E PRÁTICA","RV"),("","Mapa conceitual · Confusões mais comuns","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),("","Gabarito, respostas dos treinos e referências","R4")]
toc = "".join(f'<li class="u"><span class="t">{t}</span><span class="p" data-pg="{m}"></span></li>' if k=="u" else f'<li><span class="t">{t}</span><span class="p" data-pg="{m}"></span></li>' for k,t,m in TOC)
add(f'''<div class="unit"><span class="u">MAPA DO CADERNO</span></div><h1 class="big">Sumário</h1><ol class="toc" style="border-top:3px solid {C['navy']};margin-top:6pt">{toc}</ol>''')

def opener(num, kicker, title, items, marker):
    lis = "".join(f'<li><span>{i+1:02d}</span>{t}</li>' for i,t in enumerate(items))
    add(f'''<div class="marker">§§{marker}§§</div><div class="opener"><div class="num">{num}</div><div class="k">{kicker}</div><h1>{title}</h1><ul>{lis}</ul></div>''')
TREINOS = []
def treino(n, itens):
    TREINOS.append((n, itens))
    rows = "".join(f'<tr><td style="width:7%;text-align:center;font-weight:900;color:{C["navy"]}">{i+1}</td><td>{a}</td><td style="width:16%;text-align:center">( C ) &nbsp; ( E )</td></tr>' for i,(a,_,_) in enumerate(itens))
    add(f'''<div class="unit"><span class="u">TREINO RÁPIDO</span><span class="t">Unidade {n}</span></div><h1 class="big">Certo ou <span class="hl">errado?</span></h1>
<p class="lead">Marque C ou E sem consultar. As respostas comentadas estão no gabarito, no fim do caderno.</p>
<table><tr><th>#</th><th>Afirmação</th><th style="text-align:center">Sua resposta</th></tr>{rows}</table>''' + memo('Errou? Volte à página do assunto e releia a faixa <strong>Memorize</strong> e a <strong>Pegadinha</strong>.', "Dica:"))

# ================================================================ UNIDADE 1
opener("01","UNIDADE 1","Fundamentos",["Conceito de Direito Penal","Finalidade do Direito Penal e da pena","Princípios do Direito Penal"],"U1")

add(head(U1,T1,'O que é <span class="hl">Direito Penal</span>?','O ramo do Direito que define crimes e penas.', "A01") +
 oque(p('<strong>Direito Penal</strong> é o conjunto de normas que <strong>define as infrações penais</strong> (crimes e contravenções) e estabelece as <strong>sanções</strong> correspondentes (penas e medidas de segurança), com a finalidade de proteger os <strong>bens jurídicos</strong> mais importantes da sociedade.')) +
 cards([("book","Direito Penal OBJETIVO","O <b>conjunto das normas</b> penais em vigor: o Código Penal e as leis penais especiais.",C['navy']),
        ("gavel","Direito Penal SUBJETIVO","O <b>direito de punir</b> do Estado (<i>jus puniendi</i>), que só pode ser exercido nos limites da lei.",C['blue'])],2) +
 traduz(p('O Direito Penal é a “última linha de defesa” da sociedade. Ele só entra em campo quando um <strong>bem muito importante</strong> (vida, liberdade, patrimônio, dignidade sexual) é atacado de forma grave e os outros ramos do Direito, como o civil e o administrativo, não bastam. Por isso se diz que ele é a <strong><i>ultima ratio</i></strong>, o último recurso.')) +
 memo('Direito Penal: define <strong>infrações penais</strong> e suas <strong>sanções</strong> para proteger <strong>bens jurídicos</strong>. É a <strong><i>ultima ratio</i></strong>: só atua quando os outros ramos não bastam.'))

add(pratica_title() +
 flow([("heart",["BEM JURÍDICO","vida, patrimônio,","liberdade..."]),("alert",["ATAQUE GRAVE","a esse bem"]),("book",["LEI PENAL","descreve o crime","e a pena"]),("gavel",["ESTADO","aplica a pena","com processo"])],
      "A lógica do Direito Penal: proteger bens jurídicos por meio de crimes e penas previstos em lei.", colors=colors("g","r","n","b")) +
 ex(p('Paulo deixou de pagar o aluguel. Isso é um problema <b>civil</b> (despejo e cobrança), e não crime: o Direito Penal não intervém. Já Marcos entrou na casa de um vizinho e levou a televisão. Aqui houve ataque grave ao patrimônio, e o Código Penal prevê o crime de furto (art. 155). A diferença mostra o caráter <b>subsidiário</b> do Direito Penal.')) +
 pega('<ul><li>Direito Penal <b>objetivo</b> = normas. Direito Penal <b>subjetivo</b> = direito de punir do Estado. A prova troca!</li><li>O direito de punir é <b>exclusivo do Estado</b>: ninguém pode “fazer justiça com as próprias mãos” (o art. 345 do CP pune o exercício arbitrário das próprias razões).</li><li>A Parte Geral vai do art. 1º ao art. 120 do CP; a Parte Especial, do art. 121 em diante.</li></ul>') +
 kw(["infração penal","sanção penal","bem jurídico","ultima ratio","jus puniendi","objetivo x subjetivo"]))

add(head(U1,T1,'Finalidade do Direito Penal e da <span class="hl">pena</span>','Proteger bens jurídicos, reprovar e prevenir.', "A02") +
 lei(cp("Art. 59, caput (trecho)"),'<p>Art. 59 - O juiz, atendendo à culpabilidade, aos antecedentes, à conduta social, à personalidade do agente, aos motivos, às circunstâncias e conseqüências do crime, bem como ao comportamento da vítima, estabelecerá, conforme seja necessário e suficiente para reprovação e prevenção do crime: (...)</p>') +
 cards([("scales","Retribuição","A pena <b>reprova</b> o mal causado pelo crime.",C['navy']),
        ("people","Prevenção geral","A ameaça da pena <b>desestimula a sociedade</b> a cometer crimes.",C['blue']),
        ("person","Prevenção especial","A pena busca evitar que o <b>próprio condenado</b> volte a delinquir e favorecer sua reintegração.",C['green'])],3) +
 traduz(p('A finalidade do Direito Penal é <strong>proteger bens jurídicos</strong>. Já a pena tem uma função <strong>mista</strong>: ela <strong>reprova</strong> o crime (retribuição) e procura <strong>prevenir</strong> novos crimes, tanto da sociedade em geral (prevenção geral) quanto do próprio condenado (prevenção especial). O art. 59 resume isso em duas palavras: <strong>reprovação e prevenção</strong>.')) +
 memo('Finalidade do Direito Penal: <strong>proteção de bens jurídicos</strong>. Pena (art. 59): <strong>reprovação e prevenção</strong>, ou seja, teoria <strong>mista</strong> (unificadora).'))

PRINC = [("Legalidade (reserva legal)","Só a lei define crime e comina pena.","Art. 5º, XXXIX, CF; art. 1º, CP"),
 ("Anterioridade","A lei penal deve ser anterior ao fato.","Art. 5º, XXXIX, CF; art. 1º, CP"),
 ("Irretroatividade","A lei penal não retroage, salvo para beneficiar o réu.","Art. 5º, XL, CF"),
 ("Intervenção mínima","O Direito Penal só atua quando os outros ramos falham (<i>ultima ratio</i>). Desdobra-se em subsidiariedade e fragmentariedade.","Doutrina"),
 ("Lesividade (ofensividade)","Só há crime se houver lesão ou perigo de lesão a bem jurídico de terceiro.","Doutrina"),
 ("Insignificância","Lesões ínfimas não justificam a intervenção penal: afastam a tipicidade material.","Jurisprudência do STF e do STJ"),
 ("Pessoalidade (intranscendência)","Nenhuma pena passará da pessoa do condenado.","Art. 5º, XLV, CF"),
 ("Individualização da pena","A pena é ajustada a cada caso e a cada condenado.","Art. 5º, XLVI, CF"),
 ("Humanidade","São proibidas penas de morte (salvo guerra declarada), perpétuas, de trabalhos forçados, de banimento e cruéis.","Art. 5º, XLVII, CF"),
 ("Culpabilidade","Não há pena sem culpa (dolo ou culpa): veda-se a responsabilidade penal objetiva.","Doutrina; art. 18, CP")]
add(head(U1,T1,'Princípios do <span class="hl">Direito Penal</span>','Os limites que o Estado deve respeitar para punir.', "A03") +
 table(["Princípio","Ideia central","Fonte"],[[a,b,c] for a,b,c in PRINC],["26%",None,"24%"]) +
 memo('Princípios com <strong>fonte expressa na CF</strong>: legalidade, anterioridade, irretroatividade, pessoalidade, individualização e humanidade. Intervenção mínima, lesividade e insignificância vêm da <strong>doutrina e da jurisprudência</strong>.'))

add(pratica_title("Princípio da insignificância") +
 flow([("coin",["FATO","furto de um","chocolate"]),("search",["4 VETORES","do STF"]),("check",["PRESENTES","fato","materialmente atípico"]),("xmark",["AUSENTES","responde","pelo crime"])],
      "A insignificância exclui a tipicidade material.", colors=colors("o","n","g","r")) +
 cards([("#M","Mínima ofensividade","da conduta"),("#A","Ausência de periculosidade","social da ação"),("#R","Reduzido grau","de reprovabilidade do comportamento"),("#I","Inexpressividade","da lesão jurídica")],2) +
 ex(p('Um jovem sem antecedentes furta, de um grande supermercado, dois pacotes de biscoito. Em casos assim, os tribunais costumam reconhecer a <b>insignificância</b>: o fato é formalmente típico (está descrito no art. 155), mas <b>materialmente atípico</b>, porque não houve lesão relevante ao patrimônio. O STF usa quatro vetores (mnemônico <b>MARI</b>).')) +
 pega('<ul><li>A insignificância afasta a <b>tipicidade material</b>, e não a ilicitude nem a culpabilidade.</li><li>Não é aplicada automaticamente: depende das circunstâncias do caso. Em geral, os tribunais <b>não</b> a admitem em crimes com <b>violência ou grave ameaça</b>, como o roubo.</li></ul>'))

treino(1, [
 ("Direito Penal subjetivo é o conjunto de normas penais em vigor.","E","É o direito de punir do Estado; o conjunto de normas é o Direito Penal objetivo."),
 ("O Direito Penal é considerado a ultima ratio, devendo intervir apenas quando os demais ramos do Direito não forem suficientes.","C","Princípio da intervenção mínima."),
 ("Segundo o art. 59 do CP, a pena deve ser necessária e suficiente para a reprovação e a prevenção do crime.","C","Teoria mista."),
 ("Pelo princípio da pessoalidade, a pena pode passar da pessoa do condenado para seus herdeiros.","E","Nenhuma pena passará da pessoa do condenado (art. 5º, XLV)."),
 ("O princípio da insignificância exclui a ilicitude do fato.","E","Exclui a tipicidade material."),
 ("A Constituição admite pena de morte em caso de guerra declarada.","C","Art. 5º, XLVII, “a”.")])

# ================================================================ UNIDADE 2
opener("02","UNIDADE 2","A lei penal",["Legalidade e anterioridade","Irretroatividade e retroatividade benéfica","Aplicação da lei penal no tempo","Aplicação da lei penal no espaço (introdução)"],"U2")

add(head(U2,T2,'Legalidade e <span class="hl">anterioridade</span>','Não há crime sem lei anterior.', "A04") +
 lei(cp("Art. 1º"),'<p>Art. 1º - Não há crime sem lei anterior que o defina. Não há pena sem prévia cominação legal.</p>') +
 lei(cf("Art. 5º, XXXIX"),'<p>XXXIX - não há crime sem lei anterior que o defina, nem pena sem prévia cominação legal;</p>') +
 traduz(p('Só a <strong>lei</strong> pode dizer o que é crime e qual é a pena (<strong>reserva legal</strong>), e essa lei precisa existir <strong>antes</strong> do fato (<strong>anterioridade</strong>). Medida provisória não pode criar crime (art. 62, § 1º, I, “b”, CF), e a competência para legislar sobre direito penal é privativa da União (art. 22, I, CF).')) +
 flow([("calendar",["LEI","ANTERIOR"]),("doc",["CRIME","DEFINIDO"]),("scales",["PENA","PREVISTA"])],
      "Faltou um elemento? Não há crime a punir.", colors=colors("n","r","o")) +
 memo('<strong>Legalidade</strong> = reserva legal (só lei) + anterioridade (lei antes do fato). A lei penal deve ser <strong>escrita, estrita, prévia e certa</strong>.'))

add(head(U2,T2,'Irretroatividade e retroatividade <span class="hl">benéfica</span>','A lei mais grave não volta no tempo; a mais benéfica volta.', "A05") +
 lei(cf("Art. 5º, XL"),'<p>XL - a lei penal não retroagirá, salvo para beneficiar o réu;</p>') +
 lei(cp("Art. 2º"),'<p>Art. 2º - Ninguém pode ser punido por fato que lei posterior deixa de considerar crime, cessando em virtude dela a execução e os efeitos penais da sentença condenatória.<br>Parágrafo único - A lei posterior, que de qualquer modo favorecer o agente, aplica-se aos fatos anteriores, ainda que decididos por sentença condenatória transitada em julgado.</p>') +
 table(["Lei nova","O que faz","Retroage?"],[
  ["<i>Abolitio criminis</i>","Deixa de considerar o fato crime","<span class='yes'>SIM</span>: cessam a execução e os efeitos penais"],
  ["<i>Novatio legis in mellius</i>","Favorece o agente de qualquer modo","<span class='yes'>SIM</span>: mesmo após o trânsito em julgado"],
  ["<i>Novatio legis in pejus</i>","Agrava a situação","<span class='no'>NÃO</span>: vale a lei antiga"],
  ["<i>Novatio legis</i> incriminadora","Cria um crime novo","<span class='no'>NÃO</span>: só alcança fatos futuros"]],["28%",None,"30%"]) +
 memo('Lei <strong>benéfica retroage sempre</strong>, até depois do trânsito em julgado. Lei <strong>grave nunca retroage</strong>. <i>Abolitio</i> apaga os efeitos <strong>penais</strong>, mas <strong>não os civis</strong> (como o dever de indenizar).'))

linha = f'''<figure><svg viewBox="0 0 640 170" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<defs><marker id="lt" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L10,5 L0,10 z" fill="{C['ink']}"/></marker>
<marker id="lg" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L10,5 L0,10 z" fill="{C['green']}"/></marker></defs>
<line x1="20" y1="110" x2="620" y2="110" stroke="{C['ink']}" stroke-width="4" marker-end="url(#lt)"/>
<circle cx="110" cy="110" r="12" fill="{C['blue']}"/><text x="110" y="140" text-anchor="middle" font-weight="900" font-size="12.5" fill="{C['ink']}">AÇÃO</text><text x="110" y="156" text-anchor="middle" font-size="10.5" fill="{C['muted']}">tempo do crime (art. 4º)</text>
<rect x="290" y="92" width="16" height="36" rx="3" fill="{C['navy']}"/><text x="298" y="140" text-anchor="middle" font-weight="900" font-size="12.5" fill="{C['ink']}">LEI NOVA</text>
<circle cx="490" cy="110" r="12" fill="{C['golddeep']}"/><text x="490" y="140" text-anchor="middle" font-weight="900" font-size="12.5" fill="{C['ink']}">SENTENÇA</text><text x="490" y="156" text-anchor="middle" font-size="10.5" fill="{C['muted']}">ou execução</text>
<path d="M298 86 C 260 30, 150 30, 116 94" fill="none" stroke="{C['green']}" stroke-width="3.5" marker-end="url(#lg)"/>
<rect x="138" y="14" width="200" height="26" rx="13" fill="{C['greensoft']}" stroke="{C['green']}"/><text x="238" y="32" text-anchor="middle" font-size="12" font-weight="900" fill="{C['green']}">mais benéfica → RETROAGE</text>
<rect x="350" y="14" width="250" height="26" rx="13" fill="{C['redsoft']}" stroke="{C['red']}"/><text x="475" y="32" text-anchor="middle" font-size="12" font-weight="900" fill="{C['red']}">mais grave → não retroage</text>
</svg><figcaption>A lei benéfica “volta no tempo”; a mais grave, não.</figcaption></figure>'''
add(head(U2,T2,'Aplicação da lei penal no <span class="hl">tempo</span>','Tempo do crime, leis temporárias e casos especiais.', "A06") +
 lei(cp("Arts. 3º e 4º"),'<p>Art. 3º - A lei excepcional ou temporária, embora decorrido o período de sua duração ou cessadas as circunstâncias que a determinaram, aplica-se ao fato praticado durante sua vigência.<br>Art. 4º - Considera-se praticado o crime no momento da ação ou omissão, ainda que outro seja o momento do resultado.</p>') + linha +
 cards([("clock","Tempo do crime (art. 4º)","Teoria da <b>atividade</b>: vale o momento da conduta.",C['blue']),
        ("calendar","Lei temporária e excepcional (art. 3º)","São <b>ultra-ativas</b>: aplicam-se aos fatos praticados durante sua vigência.",C['golddeep']),
        ("hourglass","Crime permanente e continuado","Aplica-se a lei mais grave se sua vigência for anterior ao fim da permanência ou da continuidade (Súmula 711 do STF).",C['navy'])],3))

add(pratica_title() +
 ex(p('Lucas, com <b>17 anos</b>, atira em Pedro, que morre 20 dias depois, quando Lucas já completou 18 anos. Como o CP adota a teoria da <b>atividade</b>, considera-se o momento do tiro: Lucas era <b>inimputável</b> (menor de 18 anos, art. 27) e responde segundo a legislação especial (ECA), e não pelo Código Penal.')) +
 ex(p('Uma lei com vigência de 90 dias cria um crime relacionado a uma calamidade. Ana pratica a conduta no 60º dia e é julgada quando a lei já não vigora. Ela <b>responde</b> pelo crime: a lei temporária é ultra-ativa (art. 3º).'), "Exemplo prático 2") +
 pega('<ul><li><b>Tempo</b> do crime → teoria da <b>atividade</b> (art. 4º). <b>Lugar</b> do crime → teoria da <b>ubiquidade</b> (art. 6º). Mnemônico <b>LUTA</b>: Lugar-Ubiquidade, Tempo-Atividade.</li><li>Quando a lei mais benéfica surge depois da condenação definitiva, quem a aplica é o <b>juízo das execuções</b> (Súmula 611 do STF).</li><li>O fim da vigência de uma lei temporária <b>não</b> é <i>abolitio criminis</i>.</li></ul>') +
 kw(["teoria da atividade","ultra-atividade","abolitio criminis","novatio legis","Súmula 711","Súmula 611","LUTA"]))

add(head(U2,T2,'Aplicação da lei penal no <span class="hl">espaço</span>','Introdução: território, lugar do crime e extraterritorialidade.', "A07") +
 lei(cp("Arts. 5º, caput, e 6º"),'<p>Art. 5º - Aplica-se a lei brasileira, sem prejuízo de convenções, tratados e regras de direito internacional, ao crime cometido no território nacional.<br>Art. 6º - Considera-se praticado o crime no lugar em que ocorreu a ação ou omissão, no todo ou em parte, bem como onde se produziu ou deveria produzir-se o resultado.</p>') +
 table(["Regra","Resumo"],[
  ["Territorialidade temperada (art. 5º)","A lei brasileira vale para crimes no território nacional, ressalvados tratados e regras de direito internacional (ex.: imunidade diplomática)."],
  ["Território por extensão (art. 5º, § 1º)","Embarcações e aeronaves brasileiras <b>públicas</b> ou a serviço do governo, onde estiverem; e as <b>privadas</b> em alto-mar ou no espaço aéreo correspondente."],
  ["Lugar do crime (art. 6º)","Teoria da <b>ubiquidade</b>: lugar da conduta <b>ou</b> do resultado."],
  ["Extraterritorialidade (art. 7º)","Em casos específicos, a lei brasileira alcança crimes cometidos no estrangeiro, de forma <b>incondicionada</b> (ex.: crime contra a vida do Presidente da República) ou <b>condicionada</b> (ex.: crime praticado por brasileiro)."]],["30%",None]) +
 traduz(p('A regra é simples: crime cometido <strong>no Brasil</strong>, lei brasileira. Se a conduta acontece em um país e o resultado em outro (uma carta-bomba enviada do exterior que explode aqui, por exemplo), o crime também se considera praticado no Brasil, porque basta que <strong>uma parte</strong> dele aconteça aqui.'),"profa") +
 pega('<ul><li>Navio ou avião <b>público</b> brasileiro: território brasileiro <b>onde quer que esteja</b>. <b>Privado</b>: só em <b>alto-mar</b> ou no espaço aéreo correspondente.</li><li>Não confunda o lugar do crime (art. 6º do CP, ubiquidade) com a competência interna para julgar (art. 70 do CPP, lugar da consumação).</li></ul>'))

treino(2, [
 ("Não há crime sem lei anterior que o defina, nem pena sem prévia cominação legal.","C","Art. 5º, XXXIX, CF; art. 1º, CP."),
 ("A lei penal mais benéfica não alcança fatos já decididos por sentença condenatória transitada em julgado.","E","Alcança: art. 2º, parágrafo único."),
 ("A abolitio criminis faz cessar a execução e os efeitos penais da sentença, mas não os efeitos civis.","C","Art. 2º, caput."),
 ("Quanto ao tempo do crime, o CP adotou a teoria do resultado.","E","Teoria da atividade (art. 4º)."),
 ("A lei temporária aplica-se ao fato praticado durante sua vigência, mesmo depois de encerrado o período de sua duração.","C","Art. 3º."),
 ("Quanto ao lugar do crime, o CP adotou a teoria da ubiquidade.","C","Art. 6º.")])

# ================================================================ UNIDADE 3
opener("03","UNIDADE 3","Teoria do crime",["Infração penal: crime e contravenção","Conceito de crime e sua estrutura","Sujeito ativo e sujeito passivo","Dolo e culpa","Noções de tipicidade","Ilicitude","Culpabilidade","Houve crime? (fluxograma)"],"U3")

add(head(U3,T3,'Infração penal: crime e <span class="hl">contravenção</span>','O sistema dicotômico (binário) brasileiro.', "A08") +
 lei("Decreto-Lei nº 3.914/1941 (Lei de Introdução ao Código Penal) · art. 1º",'<p>Art. 1º Considera-se crime a infração penal que a lei comina pena de reclusão ou de detenção, quer isoladamente, quer alternativa ou cumulativamente com a pena de multa; contravenção, a infração penal a que a lei comina, isoladamente, pena de prisão simples ou de multa, ou ambas, alternativa ou cumulativamente.</p>') +
 f'''<figure><svg viewBox="0 0 640 180" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<rect x="230" y="8" width="180" height="44" rx="12" fill="{C['navy']}"/><text x="320" y="36" text-anchor="middle" fill="#fff" font-weight="900" font-size="15">INFRAÇÃO PENAL</text>
<path d="M320 52 V70 M160 70 H480 M160 70 V86 M480 70 V86" stroke="{C['ink']}" stroke-width="2.5" fill="none"/>
<rect x="40" y="86" width="240" height="86" rx="14" fill="{C['sky']}" stroke="{C['blue']}" stroke-width="2.5"/><text x="160" y="112" text-anchor="middle" font-weight="900" font-size="15" fill="{C['blue']}">CRIME (= DELITO)</text>
<text x="160" y="136" text-anchor="middle" font-size="12" fill="{C['ink']}">reclusão ou detenção</text><text x="160" y="154" text-anchor="middle" font-size="11" fill="{C['muted']}">(sozinhas ou com multa)</text>
<rect x="360" y="86" width="240" height="86" rx="14" fill="{C['goldsoft']}" stroke="{C['golddeep']}" stroke-width="2.5"/><text x="480" y="112" text-anchor="middle" font-weight="900" font-size="15" fill="{C['golddeep']}">CONTRAVENÇÃO</text>
<text x="480" y="136" text-anchor="middle" font-size="12" fill="{C['ink']}">prisão simples e/ou multa</text><text x="480" y="154" text-anchor="middle" font-size="11" fill="{C['muted']}">(“crime-anão”)</text>
</svg></figure>''' +
 traduz(p('No Brasil, “infração penal” é o <strong>gênero</strong>, que tem duas espécies: o <strong>crime</strong> (também chamado de delito) e a <strong>contravenção</strong>, que é uma infração menos grave. A diferença está na <strong>pena</strong> prevista em lei: reclusão ou detenção indicam crime; prisão simples ou só multa indicam contravenção.')))

add(pratica_title("Crime x contravenção") +
 table(["","CRIME","CONTRAVENÇÃO"],[
  ["Pena","Reclusão ou detenção (com ou sem multa)","Prisão simples e/ou multa"],
  ["Lei principal","Código Penal e leis especiais","Lei das Contravenções Penais (Decreto-Lei nº 3.688/1941)"],
  ["Tentativa","Punível (art. 14, II, CP)","<b>Não é punível</b> (art. 4º, LCP)"],
  ["Exemplos","Furto (art. 155, CP), homicídio (art. 121, CP)","Vias de fato (art. 21, LCP)"]],["18%",None,None]) +
 ex(p('Durante uma discussão no trânsito, um motorista empurra o outro, sem causar lesão. A conduta pode configurar <b>vias de fato</b>, uma <b>contravenção</b> (art. 21 da LCP). Se o empurrão causasse uma lesão no corpo da vítima, a conduta passaria a ser o <b>crime</b> de lesão corporal (art. 129 do CP).')) +
 pega('<ul><li>Crime e delito são <b>sinônimos</b> no Brasil (sistema dicotômico, ou binário).</li><li>A distinção é feita pela <b>pena cominada</b> na lei, e não pela gravidade “percebida” do fato.</li><li>Na contravenção, a <b>tentativa não é punível</b> (art. 4º da LCP).</li></ul>') +
 kw(["infração penal","crime = delito","contravenção","reclusão ou detenção","prisão simples","sistema dicotômico"]))

estrutura = f'''<figure><svg viewBox="0 0 640 330" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<rect x="230" y="6" width="180" height="48" rx="14" fill="{C['blue']}"/><text x="320" y="37" text-anchor="middle" fill="#fff" font-family="Inter Display" font-weight="900" font-size="20">CRIME</text>
<path d="M320 54 V72 M110 72 H530 M110 72 V88 M320 72 V88 M530 72 V88" stroke="{C['ink']}" stroke-width="2.5" fill="none"/>
''' + "".join(f'<rect x="{x-100}" y="88" width="200" height="50" rx="12" fill="{fg}"/><text x="{x}" y="112" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">{t}</text><text x="{x}" y="129" text-anchor="middle" fill="#fff" font-size="10.5" opacity=".9">{s}</text>' for x,t,s,fg in [(110,"1. FATO TÍPICO","a conduta está na lei",C['navy']),(320,"2. ILICITUDE","contrário ao Direito",C['golddeep']),(530,"3. CULPABILIDADE","juízo de reprovação",C['blue'])]) + \
 "".join(f'<rect x="{x-96}" y="{150+i*40}" width="192" height="32" rx="9" fill="{bg}" stroke="{fg}" stroke-width="1.8"/><text x="{x}" y="{171+i*40}" text-anchor="middle" font-size="10.4" font-weight="700" fill="{C["ink"]}">{t}</text>'
  for x,fg,bg,items in [(110,C['navy'],'#e6e7ea',["Conduta (dolosa ou culposa)","Resultado","Nexo causal","Tipicidade"]),(320,C['golddeep'],C['goldsoft'],["Sem excludentes (art. 23):","estado de necessidade","legítima defesa","estrito cumprimento · ex. regular"]),(530,C['blue'],C['sky'],["Imputabilidade","Potencial consciência","da ilicitude","Conduta diversa exigível"])] for i,t in enumerate(items)) + '''
</svg><figcaption>Estrutura do crime segundo a teoria tripartida (majoritária): fato típico + ilícito + culpável.</figcaption></figure>'''
add(head(U3,T3,'Conceito de crime e sua <span class="hl">estrutura</span>','Formal, material e analítico.', "A09") +
 table(["Conceito","O que diz"],[["Formal","Crime é a conduta descrita na lei penal com ameaça de pena."],["Material","Crime é a conduta que lesa ou expõe a perigo bens jurídicos relevantes."],["Analítico","Crime é o fato <b>típico</b>, <b>ilícito</b> e <b>culpável</b> (teoria tripartida, majoritária). Para a teoria bipartida, crime é o fato típico e ilícito, e a culpabilidade é pressuposto da pena."]],["20%",None]) + estrutura +
 memo('Teoria <strong>tripartida</strong>: crime = <strong>fato típico + ilícito + culpável</strong>. Faltou um dos três? Não há crime (ou, se faltar a culpabilidade, o agente fica isento de pena).'))

furto = f'''<figure><svg viewBox="0 0 640 220" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<rect width="640" height="220" rx="14" fill="#f4f1ee"/><rect y="170" width="640" height="50" fill="#d9d4cf"/>
<g transform="translate(110,40)"><svg viewBox="0 0 100 170" width="80"><use href="#ch-prof"/></svg></g>
<g transform="translate(380,40)"><svg viewBox="0 0 100 170" width="80"><use href="#ch-profa"/></svg></g>
<g transform="translate(300,92)"><rect x="0" y="0" width="22" height="38" rx="4" fill="{C['ink']}"/><rect x="3" y="4" width="16" height="26" rx="2" fill="#9fd3ff"/></g>
<rect x="20" y="16" width="190" height="44" rx="10" fill="{C['navy']}"/><text x="115" y="35" text-anchor="middle" fill="#fff" font-weight="900" font-size="12.5">SUJEITO ATIVO</text><text x="115" y="51" text-anchor="middle" fill="#fff" font-size="10.5">quem pratica: o autor do furto</text>
<rect x="430" y="16" width="190" height="44" rx="10" fill="{C['blue']}"/><text x="525" y="35" text-anchor="middle" fill="#fff" font-weight="900" font-size="12.5">SUJEITO PASSIVO</text><text x="525" y="51" text-anchor="middle" fill="#fff" font-size="10.5">titular do bem: a dona do celular</text>
<rect x="230" y="150" width="180" height="44" rx="10" fill="{C['golddeep']}"/><text x="320" y="169" text-anchor="middle" fill="#fff" font-weight="900" font-size="12">OBJETO MATERIAL</text><text x="320" y="185" text-anchor="middle" fill="#fff" font-size="10.5">a coisa atingida: o celular</text>
<rect x="430" y="150" width="190" height="44" rx="10" fill="{C['green']}"/><text x="525" y="169" text-anchor="middle" fill="#fff" font-weight="900" font-size="12">OBJETO JURÍDICO</text><text x="525" y="185" text-anchor="middle" fill="#fff" font-size="10.5">o bem protegido: o patrimônio</text>
<path d="M311 132 V148" stroke="{C['golddeep']}" stroke-width="2.5"/>
</svg><figcaption>Cena: furto de um celular. Os quatro elementos que a prova costuma pedir.</figcaption></figure>'''
add(head(U3,T3,'Sujeito ativo e <span class="hl">sujeito passivo</span>','Quem pratica e quem sofre o crime.', "A10") + furto +
 table(["Conceito","Significado"],[
  ["Sujeito ativo","Quem pratica a conduta descrita no tipo (autor, coautor ou partícipe). Em regra, pessoa física imputável; a pessoa jurídica pode responder por crimes ambientais (art. 225, § 3º, CF)."],
  ["Sujeito passivo formal (constante)","O <b>Estado</b>, titular do interesse de punir, presente em todo crime."],
  ["Sujeito passivo material (eventual)","O <b>titular do bem jurídico</b> atingido: a vítima (pessoa física, jurídica ou a coletividade)."]],["30%",None]) +
 memo('Sujeito <strong>ativo</strong> = quem pratica. Sujeito <strong>passivo</strong> = quem sofre: o <strong>Estado</strong> (formal) e o <strong>titular do bem</strong> (material).'))

add(pratica_title("Crime comum, próprio e de mão própria") +
 table(["Classificação","Quem pode praticar","Exemplo"],[
  ["Crime comum","Qualquer pessoa","Furto, homicídio"],
  ["Crime próprio","Só quem tem uma qualidade especial exigida pelo tipo, mas admite coautoria e participação","Peculato (exige ser funcionário público)"],
  ["Crime de mão própria","Só o próprio agente pode executar pessoalmente","Falso testemunho"]],["24%",None,"28%"]) +
 ex(p('Um servidor público se apropria de um notebook da repartição que estava sob sua guarda: <b>peculato</b> (art. 312 do CP), crime <b>próprio</b>, porque exige a condição de funcionário público. Se um particular, sabendo dessa condição, ajudar o servidor, poderá responder junto com ele, como coautor ou partícipe.')) +
 pega('<ul><li>O <b>Estado</b> é sujeito passivo de <b>todos</b> os crimes (sujeito passivo formal ou constante).</li><li>Uma pessoa <b>não pode</b> ser, ao mesmo tempo, sujeito ativo e passivo do próprio crime: por isso a <b>autolesão</b>, em regra, não é crime.</li><li>Animais e mortos não são sujeitos passivos: nos crimes que os envolvem, o sujeito passivo é a coletividade ou a família.</li></ul>') +
 kw(["sujeito ativo","sujeito passivo formal (Estado)","sujeito passivo material","objeto material","objeto jurídico","crime próprio"]))

ART18 = '<p>Art. 18 - Diz-se o crime:<br>I - doloso, quando o agente quis o resultado ou assumiu o risco de produzi-lo;<br>II - culposo, quando o agente deu causa ao resultado por imprudência, negligência ou imperícia.<br>Parágrafo único - Salvo os casos expressos em lei, ninguém pode ser punido por fato previsto como crime, senão quando o pratica dolosamente.</p>'
add(head(U3,T3,'Dolo e <span class="hl">culpa</span>','Querer o resultado, assumir o risco ou agir sem cuidado.', "A11") +
 lei(cp("Art. 18"), ART18) +
 cards([("target","Dolo direto","O agente <b>quer</b> o resultado.",C['red']),("alert","Dolo eventual","O agente <b>assume o risco</b>: prevê e aceita o resultado.",C['golddeep']),("car","Culpa","Resultado por <b>falta de cuidado</b>, sem querer nem aceitar.",C['blue'])],3) +
 table(["Modalidade de culpa","Significado","Exemplo"],[["Imprudência","Fazer algo de forma descuidada (agir)","Dirigir em alta velocidade numa rua movimentada"],["Negligência","Deixar de tomar um cuidado (omitir)","Não fazer a manutenção dos freios do carro"],["Imperícia","Falta de aptidão técnica na profissão ou ofício","Motorista profissional que não domina a manobra exigida"]],["22%",None,"38%"]) +
 memo('Dolo: <strong>quis</strong> ou <strong>assumiu o risco</strong>. Culpa: <strong>imprudência, negligência ou imperícia</strong>. Crime culposo só existe se a <strong>lei previr expressamente</strong> (excepcionalidade).'))

cena = f'''<figure><svg viewBox="0 0 640 250" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<rect x="0" y="0" width="312" height="250" rx="14" fill="{C['redsoft']}"/><rect x="328" y="0" width="312" height="250" rx="14" fill="{C['sky']}"/>
<text x="156" y="26" text-anchor="middle" font-weight="900" font-size="14" fill="{C['red']}">DOLO EVENTUAL</text><text x="484" y="26" text-anchor="middle" font-weight="900" font-size="14" fill="{C['blue']}">CULPA CONSCIENTE</text>
<rect x="0" y="170" width="312" height="40" fill="#bdb6b0"/><rect x="328" y="170" width="312" height="40" fill="#bdb6b0"/>
<g transform="translate(60,150)"><rect x="0" y="10" width="90" height="26" rx="8" fill="{C['red']}"/><rect x="18" y="0" width="50" height="16" rx="5" fill="#ffd2c9"/><circle cx="20" cy="38" r="8" fill="{C['ink']}"/><circle cx="72" cy="38" r="8" fill="{C['ink']}"/></g>
<path d="M150 170 h40 M160 178 h30" stroke="{C['red']}" stroke-width="3" stroke-linecap="round"/>
<rect x="20" y="44" width="272" height="88" rx="16" fill="#fff" stroke="{C['red']}" stroke-width="2"/><path d="M90 132 L84 150 L108 132Z" fill="#fff" stroke="{C['red']}" stroke-width="2"/>
<text x="156" y="72" text-anchor="middle" font-size="11.5" font-weight="900" fill="{C['ink']}">“Vou fazer o racha mesmo assim.</text><text x="156" y="92" text-anchor="middle" font-size="11.5" font-weight="900" fill="{C['ink']}">Se atropelar alguém,</text><text x="156" y="112" text-anchor="middle" font-size="11.5" font-weight="900" fill="{C['red']}">azar, tanto faz.”</text>
<text x="156" y="232" text-anchor="middle" font-size="11.5" fill="{C['ink']}">prevê o resultado e <tspan font-weight="900">aceita</tspan></text>
<g transform="translate(400,150)"><rect x="0" y="10" width="90" height="26" rx="8" fill="{C['blue']}"/><rect x="18" y="0" width="50" height="16" rx="5" fill="#ffd2c9"/><circle cx="20" cy="38" r="8" fill="{C['ink']}"/><circle cx="72" cy="38" r="8" fill="{C['ink']}"/></g>
<rect x="348" y="44" width="272" height="88" rx="16" fill="#fff" stroke="{C['blue']}" stroke-width="2"/><path d="M420 132 L414 150 L438 132Z" fill="#fff" stroke="{C['blue']}" stroke-width="2"/>
<text x="484" y="72" text-anchor="middle" font-size="11.5" font-weight="900" fill="{C['ink']}">“Estou rápido e sei que é arriscado,</text><text x="484" y="92" text-anchor="middle" font-size="11.5" font-weight="900" fill="{C['ink']}">mas sou habilidoso: tenho certeza</text><text x="484" y="112" text-anchor="middle" font-size="11.5" font-weight="900" fill="{C['blue']}">de que não vai acontecer.”</text>
<text x="484" y="232" text-anchor="middle" font-size="11.5" fill="{C['ink']}">prevê o resultado, mas <tspan font-weight="900">acredita que o evitará</tspan></text>
</svg><figcaption>Situação ilustrada: o que diferencia os dois motoristas é a atitude diante do resultado previsto.</figcaption></figure>'''
add(pratica_title("Dolo eventual x culpa consciente") + cena +
 table(["","DOLO EVENTUAL","CULPA CONSCIENTE","CULPA INCONSCIENTE"],[
  ["Prevê o resultado?","Sim","Sim","Não (mas era previsível)"],
  ["Atitude","<b>Aceita</b> o resultado (“tanto faz”)","<b>Acredita sinceramente</b> que vai evitá-lo","Não pensa no resultado"],
  ["Responde por","Crime <b>doloso</b>","Crime <b>culposo</b>","Crime <b>culposo</b>"]],["18%",None,None,None]) +
 pega('<ul><li>A diferença entre dolo eventual e culpa consciente <b>não</b> está na previsão (as duas preveem o resultado), mas na <b>aceitação</b>.</li><li>“Salvo os casos expressos em lei”, só se pune o crime <b>doloso</b>: não existe furto culposo, por exemplo.</li><li>Crime <b>preterdoloso</b>: dolo na conduta inicial e culpa no resultado mais grave (ex.: lesão corporal seguida de morte, art. 129, § 3º, do CP).</li></ul>'))

add(head(U3,T3,'Noções de <span class="hl">tipicidade</span>','O fato se encaixa na descrição da lei?', "A12") +
 oque(p('<strong>Tipicidade</strong> é a adequação do fato concreto ao <strong>tipo penal</strong>, que é a descrição da conduta proibida na lei (ex.: “subtrair, para si ou para outrem, coisa alheia móvel”, no furto). É o último elemento do fato típico.')) +
 cards([("puzzle","Tipicidade FORMAL","O fato se <b>encaixa</b> na letra da lei, como uma peça de quebra-cabeça.",C['navy']),
        ("scales","Tipicidade MATERIAL","O fato causa <b>lesão relevante</b> ao bem jurídico. A insignificância a afasta.",C['blue'])],2) +
 lei(cp("Art. 14"),'<p>Art. 14 - Diz-se o crime:<br>I - consumado, quando nele se reúnem todos os elementos de sua definição legal;<br>II - tentado, quando, iniciada a execução, não se consuma por circunstâncias alheias à vontade do agente.<br>Parágrafo único - Salvo disposição em contrário, pune-se a tentativa com a pena correspondente ao crime consumado, diminuída de um a dois terços.</p>') +
 traduz(p('Para haver fato típico, a conduta precisa “caber” no modelo descrito pela lei, como uma chave na fechadura. Se faltar algum elemento do tipo, o fato é <strong>atípico</strong>. Quando a execução começa, mas o crime não se completa por algo alheio à vontade do agente, há <strong>tentativa</strong>, punida com a pena do crime consumado reduzida de 1/3 a 2/3.')))

add(pratica_title() +
 flow([("person",["CONDUTA","dolosa ou","culposa"]),("alert",["RESULTADO","quando o tipo","exigir"]),("link",["NEXO","CAUSAL","art. 13"]),("puzzle",["TIPICIDADE","formal e","material"])],
      "Os quatro elementos do fato típico.", colors=colors("n","r","o","b")) +
 lei(cp("Art. 13, caput"),'<p>Art. 13 - O resultado, de que depende a existência do crime, somente é imputável a quem lhe deu causa. Considera-se causa a ação ou omissão sem a qual o resultado não teria ocorrido.</p>') +
 ex(p('Carlos aponta uma arma para Rui e puxa o gatilho, mas a vítima é salva por atendimento médico rápido. Houve <b>início da execução</b>, e o resultado morte não ocorreu por circunstância alheia à vontade de Carlos: <b>homicídio tentado</b> (art. 14, II), com a pena reduzida de um a dois terços.')) +
 pega('<ul><li><b>Coação física irresistível</b> (alguém força fisicamente a mão do agente) exclui a <b>conduta</b>, logo o fato típico. Já a <b>coação moral irresistível</b> exclui a <b>culpabilidade</b> (art. 22).</li><li>Na tentativa, a redução é de <b>um a dois terços</b>, e não “de metade”.</li><li>A tentativa de <b>contravenção</b> não é punível.</li></ul>'))

ART23 = '<p>Art. 23 - Não há crime quando o agente pratica o fato:<br>I - em estado de necessidade;<br>II - em legítima defesa;<br>III - em estrito cumprimento de dever legal ou no exercício regular de direito.<br>Parágrafo único - O agente, em qualquer das hipóteses deste artigo, responderá pelo excesso doloso ou culposo.</p>'
add(head(U3,T3,'<span class="hl">Ilicitude</span>','Quando um fato típico é permitido pelo Direito.', "A13") +
 lei(cp("Art. 23"), ART23) +
 cards([("umbrella","Estado de necessidade","Salvar direito próprio ou alheio de perigo atual, que não provocou e não podia evitar.",C['green']),
        ("shield","Legítima defesa","Repelir injusta agressão, atual ou iminente, com moderação.",C['blue']),
        ("badge","Estrito cumprimento de dever legal","O agente cumpre um dever imposto pela lei.",C['navy']),
        ("check","Exercício regular de direito","O agente exerce um direito reconhecido pelo ordenamento.",C['golddeep'])],2) +
 traduz(p('<strong>Ilicitude</strong> (ou antijuridicidade) é a contrariedade entre o fato e o Direito. Em regra, todo fato típico é também ilícito. Mas o art. 23 traz situações em que o fato, embora típico, é <strong>permitido</strong>: são as <strong>excludentes de ilicitude</strong>, e nelas “não há crime”. Quem exagera responde pelo <strong>excesso</strong>.')))

add(pratica_title("Legítima defesa x estado de necessidade") +
 lei(cp("Arts. 24 e 25, caput"),'<p>Art. 24 - Considera-se em estado de necessidade quem pratica o fato para salvar de perigo atual, que não provocou por sua vontade, nem podia de outro modo evitar, direito próprio ou alheio, cujo sacrifício, nas circunstâncias, não era razoável exigir-se.<br>Art. 25 - Entende-se em legítima defesa quem, usando moderadamente dos meios necessários, repele injusta agressão, atual ou iminente, a direito seu ou de outrem.</p>') +
 table(["","LEGÍTIMA DEFESA","ESTADO DE NECESSIDADE"],[["Situação","<b>Agressão</b> humana injusta","<b>Perigo</b> (de qualquer origem)"],["Momento","Atual ou <b>iminente</b>","<b>Atual</b>"],["Reação","Contra o <b>agressor</b>","Contra bem de terceiro inocente, se preciso"],["Exemplo","Defender-se de quem ataca com uma faca","Arrombar uma casa para fugir de um incêndio"]],["18%",None,None]) +
 ex(p('Durante uma enchente, Ana arromba a porta de uma casa vazia para se abrigar com os filhos: <b>estado de necessidade</b>. Já Pedro, atacado na rua por alguém armado com uma faca, empurra o agressor e o derruba: <b>legítima defesa</b>. Se, com o agressor já desarmado no chão, Pedro continuar a agredi-lo, responderá pelo <b>excesso</b> (art. 23, parágrafo único).')))

add(head(U3,T3,'<span class="hl">Culpabilidade</span>','O juízo de reprovação sobre o autor do fato.', "A14") +
 table(["Elemento","O que significa","Quando falta (excludente)"],[
  ["Imputabilidade","Capacidade de entender o caráter ilícito do fato e de agir de acordo com esse entendimento","Doença mental ou desenvolvimento mental incompleto ou retardado (art. 26); menores de 18 anos (art. 27)"],
  ["Potencial consciência da ilicitude","Possibilidade de saber que a conduta é proibida","Erro de proibição <b>inevitável</b> (art. 21): isenta de pena"],
  ["Exigibilidade de conduta diversa","Era possível exigir do agente outro comportamento","Coação moral irresistível; obediência hierárquica a ordem não manifestamente ilegal (art. 22)"]],["24%",None,"36%"]) +
 lei(cp("Arts. 26 (caput), 27 e 22"),'<p>Art. 26 - É isento de pena o agente que, por doença mental ou desenvolvimento mental incompleto ou retardado, era, ao tempo da ação ou da omissão, inteiramente incapaz de entender o caráter ilícito do fato ou de determinar-se de acordo com esse entendimento.<br>Art. 27 - Os menores de 18 (dezoito) anos são penalmente inimputáveis, ficando sujeitos às normas estabelecidas na legislação especial.<br>Art. 22 - Se o fato é cometido sob coação irresistível ou em estrita obediência a ordem, não manifestamente ilegal, de superior hierárquico, só é punível o autor da coação ou da ordem.</p>') +
 memo('Culpabilidade: <b>IPE</b> → <strong>I</strong>mputabilidade, <strong>P</strong>otencial consciência da ilicitude, <strong>E</strong>xigibilidade de conduta diversa. Sem culpabilidade, o agente é <strong>isento de pena</strong>.', "Mnemônico:"))

add(pratica_title() +
 ex(p('Um gerente de banco é obrigado a abrir o cofre porque criminosos mantêm sua família refém e ameaçam matá-la. Ele praticou um fato típico e ilícito, mas sob <b>coação moral irresistível</b>: não era exigível conduta diversa. Fica isento de pena, e só o autor da coação responde (art. 22).')) +
 lei(cp("Art. 21, caput"),'<p>Art. 21 - O desconhecimento da lei é inescusável. O erro sobre a ilicitude do fato, se inevitável, isenta de pena; se evitável, poderá diminuí-la de um sexto a um terço.</p>') +
 pega('<ul><li>“O desconhecimento da lei é inescusável”: ninguém se livra alegando que não conhecia a lei. O que pode isentar de pena é o <b>erro sobre a ilicitude</b>, se <b>inevitável</b>.</li><li>Menoridade, doença mental, erro de proibição inevitável e coação moral irresistível excluem a <b>culpabilidade</b>. Legítima defesa e estado de necessidade excluem a <b>ilicitude</b>.</li><li><b>Emoção e paixão não excluem a imputabilidade</b> (art. 28, I, do CP).</li></ul>') +
 kw(["imputabilidade","potencial consciência da ilicitude","exigibilidade de conduta diversa","art. 26","art. 27","coação moral irresistível","isento de pena"]))

fx = f'''<figure><svg viewBox="0 0 640 400" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<defs><marker id="fa" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L10,5 L0,10z" fill="{C['ink']}"/></marker></defs>
''' + "".join(
 f'<rect x="20" y="{y}" width="330" height="64" rx="14" fill="#fff" stroke="{c}" stroke-width="2.8"/><text x="185" y="{y+26}" text-anchor="middle" font-weight="900" font-size="13.5" fill="{c}">{q}</text><text x="185" y="{y+46}" text-anchor="middle" font-size="11" fill="{C["muted"]}">{s}</text>'
 f'<line x1="350" y1="{y+32}" x2="418" y2="{y+32}" stroke="{C["red"]}" stroke-width="3" marker-end="url(#fa)"/><text x="384" y="{y+24}" text-anchor="middle" font-weight="900" font-size="10.5" fill="{C["red"]}">NÃO</text>'
 f'<rect x="424" y="{y+4}" width="196" height="56" rx="12" fill="{C["redsoft"]}" stroke="{C["red"]}" stroke-width="2"/><text x="522" y="{y+28}" text-anchor="middle" font-weight="900" font-size="12.5" fill="{C["red"]}">{r1}</text><text x="522" y="{y+46}" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">{r2}</text>'
 f'<line x1="185" y1="{y+64}" x2="185" y2="{y+94}" stroke="{C["green"]}" stroke-width="3" marker-end="url(#fa)"/><text x="200" y="{y+84}" font-weight="900" font-size="10.5" fill="{C["green"]}">SIM</text>'
 for y,q,s,r1,r2,c in [(10,"1. O fato é típico?","conduta, resultado, nexo, tipicidade","NÃO HÁ CRIME","fato atípico",C['navy']),
  (110,"2. O fato é ilícito?","não há excludente do art. 23?","NÃO HÁ CRIME","há excludente de ilicitude",C['golddeep']),
  (210,"3. O agente é culpável?","imputável, consciente, exigível","ISENTO DE PENA","excludente de culpabilidade",C['blue'])]) + f'''
<rect x="60" y="314" width="250" height="56" rx="14" fill="{C['greensoft']}" stroke="{C['green']}" stroke-width="2.8"/><text x="185" y="348" text-anchor="middle" font-family="Inter Display" font-weight="900" font-size="20" fill="{C['green']}">HÁ CRIME</text>
</svg><figcaption>Siga as perguntas na ordem. Basta um “não” para afastar o crime ou a pena.</figcaption></figure>'''
add(head(U3,T3,'Houve <span class="hl">crime</span>? Siga o fluxo','O raciocínio que resolve casos práticos de prova.', "A15") + fx +
 table(["Caso","Resposta","Por quê"],[
  ["Pessoa furta um pacote de biscoito de valor ínfimo, sem antecedentes","Fato atípico (em regra)","Insignificância afasta a tipicidade material"],
  ["Vítima reage com moderação a um assalto à mão armada","Não há crime","Legítima defesa exclui a ilicitude"],
  ["Adolescente de 16 anos pratica um roubo","Não responde pelo CP","Inimputável (art. 27): legislação especial (ECA)"]],["40%","22%",None]))

treino(3, [
 ("No Brasil, crime e delito são expressões sinônimas.","C","Sistema dicotômico: crime (delito) e contravenção."),
 ("A tentativa de contravenção é punível com a pena da contravenção consumada, reduzida de um a dois terços.","E","Não é punível (art. 4º da LCP)."),
 ("Age com dolo eventual o agente que prevê o resultado, mas acredita sinceramente que poderá evitá-lo.","E","Isso é culpa consciente; no dolo eventual, ele aceita o resultado."),
 ("Salvo os casos expressos em lei, ninguém pode ser punido por fato previsto como crime senão quando o pratica dolosamente.","C","Art. 18, parágrafo único."),
 ("A legítima defesa exclui a culpabilidade.","E","Exclui a ilicitude (art. 23, II)."),
 ("Os menores de 18 anos são penalmente inimputáveis.","C","Art. 27.")])

# ================================================================ UNIDADE 4
opener("04","UNIDADE 4","Penas",["Penas: conceito e limites constitucionais","Espécies de penas","Penas privativas de liberdade e regimes","Restritivas de direitos e multa"],"U4")

add(head(U4,T4,'Penas: conceito e <span class="hl">limites constitucionais</span>','O que a Constituição permite e o que proíbe.', "A16") +
 oque(p('<strong>Pena</strong> é a sanção imposta pelo Estado, por meio do devido processo legal, a quem praticou uma infração penal. Tem finalidade de <strong>reprovação</strong> e <strong>prevenção</strong> (art. 59 do CP).')) +
 lei(cf("Art. 5º, XLV e XLVI"),'<p>XLV - nenhuma pena passará da pessoa do condenado, podendo a obrigação de reparar o dano e a decretação do perdimento de bens ser, nos termos da lei, estendidas aos sucessores e contra eles executadas, até o limite do valor do patrimônio transferido;<br>XLVI - a lei regulará a individualização da pena e adotará, entre outras, as seguintes: a) privação ou restrição da liberdade; b) perda de bens; c) multa; d) prestação social alternativa; e) suspensão ou interdição de direitos;</p>') +
 table(["PERMITIDAS (art. 5º, XLVI, exemplos)","PROIBIDAS (art. 5º, XLVII)"],[["Privação ou restrição da liberdade","De morte, salvo em caso de guerra declarada"],["Perda de bens","De caráter perpétuo"],["Multa","De trabalhos forçados"],["Prestação social alternativa","De banimento"],["Suspensão ou interdição de direitos","Cruéis"]],["50%",None],rh=False) +
 memo('Pessoalidade: a pena <strong>não passa</strong> da pessoa do condenado; a <strong>reparação do dano</strong> e o <strong>perdimento de bens</strong> podem alcançar os sucessores, até o limite do patrimônio transferido.'))

arvore = f'''<figure><svg viewBox="0 0 640 290" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<rect x="220" y="6" width="200" height="46" rx="12" fill="{C['navy']}"/><text x="320" y="28" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">PENAS (art. 32, CP)</text><text x="320" y="44" text-anchor="middle" fill="#fff" font-size="10.5" opacity=".85">as penas são:</text>
<path d="M320 52 V68 M110 68 H530 M110 68 V82 M320 68 V82 M530 68 V82" stroke="{C['ink']}" stroke-width="2.5" fill="none"/>
''' + "".join(f'<rect x="{x-100}" y="82" width="200" height="46" rx="12" fill="{fg}"/><text x="{x}" y="104" text-anchor="middle" fill="#fff" font-weight="900" font-size="13">{t}</text><text x="{x}" y="120" text-anchor="middle" fill="#fff" font-size="10.5">{s}</text>'
 + "".join(f'<rect x="{x-98}" y="{138+i*29}" width="196" height="24" rx="7" fill="{bg}" stroke="{fg}" stroke-width="1.5"/><text x="{x}" y="{154+i*29}" text-anchor="middle" font-size="10" font-weight="700" fill="{C["ink"]}">{l}</text>' for i,l in enumerate(ls))
 for x,t,s,fg,bg,ls in [(110,"I · PRIVATIVAS","DE LIBERDADE",C['red'],C['redsoft'],["Reclusão","Detenção","(prisão simples: contravenções)"]),
   (320,"II · RESTRITIVAS","DE DIREITOS",C['golddeep'],C['goldsoft'],["Prestação pecuniária","Perda de bens e valores","Prestação de serviço à comunidade","Interdição temporária de direitos","Limitação de fim de semana"]),
   (530,"III · MULTA","dias-multa",C['blue'],C['sky'],["10 a 360 dias-multa","paga ao fundo penitenciário"])]) + '</svg><figcaption>Árvore das espécies de pena no Código Penal.</figcaption></figure>'
add(head(U4,T4,'Espécies de <span class="hl">penas</span>','Privativas de liberdade, restritivas de direitos e multa.', "A17") +
 lei(cp("Art. 32"),'<p>Art. 32 - As penas são:<br>I - privativas de liberdade;<br>II - restritivas de direitos;<br>III - de multa.</p>') + arvore +
 traduz(p('O Código Penal tem <strong>três espécies</strong> de pena. As <strong>privativas de liberdade</strong> tiram a liberdade (prisão). As <strong>restritivas de direitos</strong> limitam certos direitos, como prestar serviços à comunidade, e em regra <strong>substituem</strong> a prisão em casos menos graves. A <strong>multa</strong> é o pagamento de um valor, calculado em dias-multa.')) +
 memo('Art. 32: <strong>privativas de liberdade</strong> · <strong>restritivas de direitos</strong> · <strong>multa</strong>. Limite de cumprimento das privativas: <strong>40 anos</strong> (art. 75).'))

regua = f'''<figure><svg viewBox="0 0 640 175" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
''' + "".join(f'<rect x="{x}" y="22" width="190" height="66" rx="10" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x+95}" y="44" text-anchor="middle" font-weight="900" font-size="13" fill="{fg}">{t}</text><text x="{x+95}" y="62" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">{l1}</text><text x="{x+95}" y="78" text-anchor="middle" font-size="10.5" font-weight="800" fill="{C["ink"]}">{l2}</text>' for x,t,l1,l2,fg,bg in [(20,"ATÉ 4 ANOS","não reincidente: pode","começar no ABERTO",C['green'],C['greensoft']),(225,"MAIS DE 4 ATÉ 8","não reincidente: pode","começar no SEMIABERTO",C['golddeep'],C['goldsoft']),(430,"MAIS DE 8 ANOS","começa no","FECHADO",C['red'],C['redsoft'])]) + f'''
<line x1="20" y1="110" x2="620" y2="110" stroke="{C['ink']}" stroke-width="4"/>
{"".join(f'<line x1="{x}" y1="102" x2="{x}" y2="118" stroke="{C["ink"]}" stroke-width="3"/><text x="{x}" y="136" text-anchor="middle" font-weight="900" font-size="12" fill="{C["ink"]}">{t}</text>' for x,t in [(20,"0"),(220,"4 anos"),(425,"8 anos"),(600,"40 anos (limite)")])}
<text x="320" y="160" text-anchor="middle" font-size="11" fill="{C['muted']}">Regime inicial da pena de reclusão (art. 33, § 2º), em esquema simplificado. O juiz também considera os critérios do art. 59.</text>
</svg></figure>'''
add(head(U4,T4,'Penas privativas de liberdade e <span class="hl">regimes</span>','Reclusão, detenção e os três regimes.', "A18") +
 lei(cp("Art. 33, caput"),'<p>Art. 33 - A pena de reclusão deve ser cumprida em regime fechado, semi-aberto ou aberto. A de detenção, em regime semi-aberto, ou aberto, salvo necessidade de transferência a regime fechado.</p>') +
 table(["Regime","Onde se cumpre (art. 33, § 1º)"],[["Fechado","Estabelecimento de segurança máxima ou média"],["Semiaberto","Colônia agrícola, industrial ou estabelecimento similar"],["Aberto","Casa de albergado ou estabelecimento adequado"]],["24%",None]) + regua +
 memo('<strong>Reclusão</strong>: pode começar em qualquer regime (fechado, semiaberto ou aberto). <strong>Detenção</strong>: começa no semiaberto ou no aberto (pode haver regressão ao fechado). <strong>Prisão simples</strong>: para contravenções.'))

add(head(U4,T4,'Restritivas de direitos e <span class="hl">multa</span>','Alternativas à prisão e a pena pecuniária.', "A19") +
 lei(cp("Art. 43"),'<p>Art. 43 - As penas restritivas de direitos são:<br>I - prestação pecuniária;<br>II - perda de bens e valores;<br>III - (VETADO);<br>IV - prestação de serviço à comunidade ou a entidades públicas;<br>V - interdição temporária de direitos;<br>VI - limitação de fim de semana.</p>') +
 table(["Requisitos para substituir a prisão (art. 44, em síntese)",""],[["I · Pena e crime","Pena aplicada <b>não superior a 4 anos</b> e crime <b>sem violência ou grave ameaça</b> à pessoa; ou, qualquer que seja a pena, crime <b>culposo</b>"],["II · Reincidência","Réu <b>não reincidente em crime doloso</b>"],["III · Circunstâncias","Culpabilidade, antecedentes, conduta social, personalidade, motivos e circunstâncias indicarem que a substituição é suficiente"]],["30%",None]) +
 lei(cp("Art. 49, caput"),'<p>Art. 49 - A pena de multa consiste no pagamento ao fundo penitenciário da quantia fixada na sentença e calculada em dias-multa. Será, no mínimo, de 10 (dez) e, no máximo, de 360 (trezentos e sessenta) dias-multa.</p>') +
 memo('Restritivas (art. 43): <strong>5 espécies</strong> (o inciso III foi vetado). Substituição: até <strong>4 anos</strong>, <strong>sem violência ou grave ameaça</strong> (ou crime culposo), <strong>não reincidente em crime doloso</strong>. Multa: <strong>10 a 360 dias-multa</strong>.'))

add(pratica_title() +
 ex(p('Joana foi condenada a 2 anos de reclusão por um furto simples, sem violência. Ela não é reincidente e as circunstâncias são favoráveis. O juiz pode <b>substituir</b> a pena privativa de liberdade por restritivas de direitos, como prestação de serviço à comunidade e prestação pecuniária (art. 44). Já Marcos, condenado a 2 anos por um crime praticado com <b>grave ameaça</b>, <b>não</b> tem direito a essa substituição.')) +
 pega('<ul><li>O art. 43 lista <b>cinco</b> restritivas de direitos em vigor: o <b>inciso III foi vetado</b>.</li><li>No crime <b>culposo</b>, a substituição é possível <b>qualquer que seja a pena</b> aplicada.</li><li>Multa: mínimo de <b>10</b> e máximo de <b>360</b> dias-multa, paga ao <b>fundo penitenciário</b>.</li><li>O limite de cumprimento das penas privativas de liberdade é de <b>40 anos</b> (art. 75, na redação da Lei nº 13.964/2019); antes era de 30 anos.</li></ul>') +
 kw(["prestação pecuniária","perda de bens e valores","prestação de serviço à comunidade","interdição temporária de direitos","limitação de fim de semana","dias-multa","40 anos"]))

treino(4, [
 ("Segundo o art. 32 do CP, as penas são privativas de liberdade, restritivas de direitos e de multa.","C","Art. 32."),
 ("A pena de detenção pode ser cumprida inicialmente em regime fechado.","E","Detenção: semiaberto ou aberto, salvo necessidade de transferência ao fechado."),
 ("O condenado a pena superior a 8 anos deverá começar a cumpri-la em regime fechado.","C","Art. 33, § 2º, “a”."),
 ("A substituição da pena privativa de liberdade por restritiva de direitos é cabível em crime cometido com grave ameaça, desde que a pena não supere 4 anos.","E","Exige crime sem violência ou grave ameaça à pessoa."),
 ("A pena de multa será, no mínimo, de 10 e, no máximo, de 360 dias-multa.","C","Art. 49."),
 ("Nenhuma pena passará da pessoa do condenado, mas a obrigação de reparar o dano pode ser estendida aos sucessores, até o limite do patrimônio transferido.","C","Art. 5º, XLV.")])

# ================================================================ REVISÃO
mapa = f'''<figure><svg viewBox="0 0 640 470" width="580" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<g stroke="#b9b3ad" stroke-width="2.5" fill="none"><path d="M320 235 L150 70"/><path d="M320 235 L490 70"/><path d="M320 235 L120 235"/><path d="M320 235 L520 235"/><path d="M320 235 L150 400"/><path d="M320 235 L490 400"/></g>
<circle cx="320" cy="235" r="74" fill="{C['navy']}"/><text x="320" y="225" text-anchor="middle" fill="{C['gold']}" font-weight="900" font-size="13">PARTE GERAL</text>
<text x="320" y="245" text-anchor="middle" fill="#fff" font-weight="900" font-size="15">DIREITO</text><text x="320" y="263" text-anchor="middle" fill="#fff" font-weight="900" font-size="15">PENAL</text>
''' + "".join(
 f'<rect x="{x-100}" y="{y-40}" width="200" height="80" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x}" y="{y-16}" text-anchor="middle" font-weight="900" font-size="12.5" fill="{fg}">{t}</text>'
 + "".join(f'<text x="{x}" y="{y+4+i*15}" text-anchor="middle" font-size="10.8" fill="{C["ink"]}">{l}</text>' for i,l in enumerate(ls))
 for x,y,t,ls,fg,bg in [
  (150,62,"PRINCÍPIOS",["legalidade · anterioridade","intervenção mínima · MARI","pessoalidade · humanidade"],C['navy'],'#e6e7ea'),
  (490,62,"LEI NO TEMPO",["benéfica retroage; grave não","atividade (art. 4º)","temporária: ultra-ativa"],C['blue'],C['sky']),
  (112,235,"LEI NO ESPAÇO",["territorialidade temperada","ubiquidade (art. 6º)","extraterritorialidade (art. 7º)"],C['golddeep'],C['goldsoft']),
  (528,235,"CRIME",["típico + ilícito + culpável","crime x contravenção (pena)","sujeito ativo x passivo"],C['red'],C['redsoft']),
  (150,408,"DOLO E CULPA",["dolo: quis ou assumiu o risco","culpa: imprudência, negligência,","imperícia · eventual x consciente"],C['green'],C['greensoft']),
  (490,408,"PENAS",["privativas · restritivas · multa","fechado > 8 · 40 anos (art. 75)","multa: 10 a 360 dias-multa"],C['navy'],'#e6e7ea')]) + '</svg><figcaption>Mapa conceitual do Caderno 05.</figcaption></figure>'
add('<div class="marker">§§R1§§</div><div class="unit"><span class="u">REVISÃO</span><span class="t">Véspera da prova</span></div><h1 class="big">Mapa <span class="hl">conceitual</span></h1><p class="lead">A Parte Geral em seis blocos. Explique cada caixa em voz alta.</p>' + mapa)

add('<div class="unit"><span class="u">REVISÃO</span><span class="t">Pontos de confusão</span></div><h1 class="big">As confusões <span class="hl">mais comuns</span></h1><p class="lead">Os pares de conceitos que mais derrubam candidatos neste tema.</p>' +
 table(["Confusão","O certo é"],[
  ["Direito Penal objetivo x subjetivo","Objetivo: normas. Subjetivo: direito de punir do Estado."],
  ["Tempo x lugar do crime","Tempo: <b>atividade</b> (art. 4º). Lugar: <b>ubiquidade</b> (art. 6º). LUTA."],
  ["Lei benéfica x lei grave","Benéfica retroage (até após o trânsito em julgado); grave não retroage."],
  ["Crime x contravenção","Pela pena: reclusão/detenção = crime; prisão simples e/ou multa = contravenção."],
  ["Dolo eventual x culpa consciente","Ambos preveem o resultado; no dolo eventual o agente <b>aceita</b>; na culpa consciente, <b>acredita que evitará</b>."],
  ["Imprudência x negligência x imperícia","Agir com descuido · omitir cuidado · falta de aptidão técnica."],
  ["Excludente de ilicitude x de culpabilidade","Ilicitude: art. 23 (“não há crime”). Culpabilidade: arts. 21, 22, 26 e 27 (“isento de pena”)."],
  ["Coação física x coação moral","Física irresistível: exclui a <b>conduta</b>. Moral irresistível: exclui a <b>culpabilidade</b>."],
  ["Legítima defesa x estado de necessidade","LD: agressão injusta, atual ou iminente. EN: perigo atual."],
  ["Desconhecimento da lei x erro de proibição","Desconhecer a lei é inescusável; o erro sobre a ilicitude inevitável isenta de pena."],
  ["Reclusão x detenção","Reclusão: pode começar no fechado. Detenção: semiaberto ou aberto."],
  ["Restritivas de direitos","Cinco espécies (inciso III do art. 43 vetado); substituição até 4 anos, sem violência ou grave ameaça."]],["34%",None]))

FC = [("CONCEITO","Direito Penal objetivo e subjetivo?","Objetivo: conjunto de normas penais. Subjetivo: direito de punir do Estado."),
 ("FINALIDADE","Finalidade da pena segundo o art. 59?","Reprovação e prevenção do crime (teoria mista)."),
 ("PRINCÍPIOS","O que diz o princípio da pessoalidade?","Nenhuma pena passará da pessoa do condenado (art. 5º, XLV)."),
 ("PRINCÍPIOS","Vetores da insignificância (STF)?","Mínima ofensividade, ausência de periculosidade social, reduzido grau de reprovabilidade, inexpressividade da lesão (MARI)."),
 ("LEGALIDADE","O que diz o art. 1º do CP?","Não há crime sem lei anterior que o defina; não há pena sem prévia cominação legal."),
 ("TEMPO","Lei posterior mais benéfica retroage após o trânsito em julgado?","Sim (art. 2º, parágrafo único)."),
 ("TEMPO","Teoria adotada para o tempo do crime?","Atividade (art. 4º)."),
 ("ESPAÇO","Teoria adotada para o lugar do crime?","Ubiquidade (art. 6º)."),
 ("INFRAÇÃO","Como distinguir crime de contravenção?","Pela pena: reclusão ou detenção (crime); prisão simples e/ou multa (contravenção)."),
 ("INFRAÇÃO","A tentativa de contravenção é punível?","Não (art. 4º da LCP)."),
 ("CRIME","Conceito analítico tripartido?","Fato típico, ilícito e culpável."),
 ("SUJEITOS","Quem é o sujeito passivo formal de todo crime?","O Estado."),
 ("DOLO","Quando o crime é doloso?","Quando o agente quis o resultado ou assumiu o risco de produzi-lo (art. 18, I)."),
 ("CULPA","Modalidades de culpa?","Imprudência, negligência e imperícia (art. 18, II)."),
 ("CULPA","Diferença entre dolo eventual e culpa consciente?","No dolo eventual o agente aceita o resultado; na culpa consciente, acredita que o evitará."),
 ("TIPICIDADE","Elementos do fato típico?","Conduta, resultado, nexo causal e tipicidade."),
 ("TENTATIVA","Redução de pena na tentativa?","De um a dois terços (art. 14, parágrafo único)."),
 ("ILICITUDE","Excludentes de ilicitude do art. 23?","Estado de necessidade, legítima defesa, estrito cumprimento de dever legal e exercício regular de direito."),
 ("ILICITUDE","Requisitos da legítima defesa?","Injusta agressão, atual ou iminente, a direito seu ou de outrem, repelida com moderação e meios necessários."),
 ("CULPABILIDADE","Elementos da culpabilidade?","Imputabilidade, potencial consciência da ilicitude e exigibilidade de conduta diversa (IPE)."),
 ("CULPABILIDADE","Emoção e paixão excluem a imputabilidade?","Não (art. 28, I)."),
 ("PENAS","Espécies de pena do art. 32?","Privativas de liberdade, restritivas de direitos e multa."),
 ("PENAS","Limite de cumprimento das privativas de liberdade?","40 anos (art. 75)."),
 ("PENAS","Limites da pena de multa?","De 10 a 360 dias-multa (art. 49).")]
def fcpage(items, first):
    cs = "".join(f'<div class="c"><div class="f"><small>{a}</small>{q}</div><div class="b">{r}</div></div>' for a,q,r in items)
    h = ('<div class="marker">§§R2§§</div><div class="unit"><span class="u">REVISÃO ATIVA</span></div><h1 class="big">Flash<span class="hl">cards</span></h1><p class="lead">Cubra a resposta, tente lembrar e confira. Revise em 1, 3, 7, 15 e 30 dias.</p>' if first else '')
    return h + f'<div class="fc">{cs}</div>'
add(fcpage(FC[:12], True)); add(fcpage(FC[12:], False))

Q = [
 ("Conceito","O direito de punir do Estado (jus puniendi) corresponde ao:",
  ["Direito Penal objetivo.","Direito Penal subjetivo.","Direito Penal do autor.","Direito Processual Penal.","Direito Penal internacional."],"B",
  "O Direito Penal subjetivo é o direito de punir do Estado; o objetivo é o conjunto de normas penais.","Objetivo = normas; subjetivo = direito de punir."),
 ("Princípios","O princípio segundo o qual o Direito Penal só deve intervir quando os demais ramos do Direito forem insuficientes para proteger o bem jurídico é o da:",
  ["anterioridade.","intervenção mínima.","pessoalidade.","taxatividade.","individualização da pena."],"B",
  "A intervenção mínima (ultima ratio) desdobra-se em subsidiariedade e fragmentariedade.","Ultima ratio = intervenção mínima."),
 ("Princípios","Sobre o princípio da insignificância, assinale a alternativa correta.",
  ["Exclui a culpabilidade do agente.","Exclui a ilicitude do fato.","Afasta a tipicidade material quando a lesão ao bem jurídico é ínfima.","Aplica-se automaticamente a qualquer crime patrimonial.","Está expresso no art. 1º do Código Penal."],"C",
  "A insignificância afasta a tipicidade material. Não é automática e não está expressa no art. 1º do CP; resulta da doutrina e da jurisprudência.","Insignificância → tipicidade material."),
 ("Princípios","Nos termos do art. 5º, XLV, da Constituição:",
  ["a pena pode ser cumprida pelos herdeiros do condenado.","nenhuma pena passará da pessoa do condenado, mas a obrigação de reparar o dano pode ser estendida aos sucessores, até o limite do valor do patrimônio transferido.","a multa sempre se transmite aos herdeiros.","os sucessores respondem integralmente pelas penas do falecido.","a reparação do dano extingue-se com a morte do condenado."],"B",
  "Texto do inciso XLV (pessoalidade ou intranscendência da pena).","A pena não passa; a reparação do dano pode passar, até o limite da herança."),
 ("Lei no tempo","Lei nova, publicada após a condenação definitiva de João, reduziu a pena do crime por ele praticado. Nesse caso:",
  ["a lei nova não se aplica, pois houve trânsito em julgado.","a lei nova aplica-se, pois a lei posterior que de qualquer modo favorecer o agente alcança fatos já decididos por sentença transitada em julgado.","João deve propor nova ação penal.","a lei nova só vale para crimes futuros.","a redução depende de indulto."],"B",
  "Art. 2º, parágrafo único, do CP e art. 5º, XL, da CF. Após o trânsito em julgado, a aplicação cabe ao juízo das execuções (Súmula 611 do STF).","Lei benéfica retroage sempre."),
 ("Lei no tempo","Considera-se praticado o crime no momento da ação ou omissão, ainda que outro seja o momento do resultado. O Código Penal adotou, quanto ao tempo do crime, a teoria:",
  ["do resultado.","da ubiquidade.","da atividade.","mista.","da consumação."],"C",
  "Art. 4º: teoria da atividade. A ubiquidade é a teoria adotada para o lugar do crime (art. 6º).","LUTA: Tempo-Atividade."),
 ("Lei no espaço","Quanto ao lugar do crime, o art. 6º do Código Penal considera praticado o crime:",
  ["apenas no lugar da ação.","apenas no lugar do resultado.","no lugar da ação ou omissão, no todo ou em parte, bem como onde se produziu ou deveria produzir-se o resultado.","no domicílio do autor.","no lugar onde o autor foi preso."],"C",
  "Teoria da ubiquidade (art. 6º).","Lugar: ubiquidade."),
 ("Infração penal","Segundo a Lei de Introdução ao Código Penal, a infração penal para a qual a lei comina, isoladamente, pena de prisão simples é:",
  ["crime doloso.","crime culposo.","contravenção penal.","crime hediondo.","crime de menor potencial, punido com reclusão."],"C",
  "Art. 1º do Decreto-Lei nº 3.914/1941: crime tem reclusão ou detenção; contravenção, prisão simples e/ou multa.","Prisão simples → contravenção."),
 ("Infração penal","Sobre a tentativa nas contravenções penais, é correto afirmar que:",
  ["é punida com a pena da contravenção consumada.","é punida com redução de um a dois terços.","não é punível.","é punida com o dobro da pena.","só é punível nas contravenções dolosas."],"C",
  "Art. 4º da Lei das Contravenções Penais: não é punível a tentativa de contravenção.","Tentativa de contravenção: não punível."),
 ("Crime","Para a teoria tripartida, majoritária, o crime é o fato:",
  ["típico e ilícito, apenas.","típico, ilícito e culpável.","típico, ilícito, culpável e punível.","ilícito e culpável, apenas.","previsto em lei, independentemente de culpa."],"B",
  "Conceito analítico tripartido. Para a teoria bipartida, a culpabilidade é pressuposto da pena; a punibilidade não integra o conceito de crime para a doutrina majoritária.","Típico + ilícito + culpável."),
 ("Sujeitos","Num crime de furto de celular, o Estado figura como sujeito passivo:",
  ["material.","eventual.","formal ou constante.","acidental.","Não há sujeito passivo estatal no furto."],"C",
  "O Estado é sujeito passivo formal (constante) de todo crime; o titular do bem (dono do celular) é o sujeito passivo material (eventual).","Estado = sujeito passivo formal."),
 ("Sujeitos","O peculato, que exige do autor a condição de funcionário público, é exemplo de crime:",
  ["comum.","próprio.","de mão própria que não admite participação.","culposo, apenas.","impossível."],"B",
  "Crime próprio exige qualidade especial do sujeito ativo e admite coautoria e participação de quem conheça essa condição.","Qualidade especial → crime próprio."),
 ("Dolo","Diz-se o crime doloso, nos termos do art. 18, I, do CP, quando o agente:",
  ["deu causa ao resultado por imprudência.","quis o resultado ou assumiu o risco de produzi-lo.","previu o resultado e acreditou que poderia evitá-lo.","não previu o resultado previsível.","agiu por negligência."],"B",
  "Art. 18, I: dolo direto (quis) e dolo eventual (assumiu o risco). C descreve a culpa consciente; A, D e E, formas de culpa.","Dolo: quis ou assumiu o risco."),
 ("Culpa","Motorista que deixa de fazer a manutenção dos freios do veículo e, por isso, causa um acidente com vítima age com:",
  ["dolo direto.","imperícia.","negligência.","dolo eventual.","exercício regular de direito."],"C",
  "Negligência é a omissão de um cuidado devido. Imprudência é agir com descuido; imperícia é falta de aptidão técnica.","Negligência = deixar de tomar cuidado."),
 ("Dolo e culpa","Durante um racha, o motorista pensa: “se atropelar alguém, tanto faz”, e atropela um pedestre. Já outro motorista, em alta velocidade, prevê o risco, mas acredita sinceramente que, por sua habilidade, o acidente não ocorrerá. As condutas caracterizam, respectivamente:",
  ["culpa consciente e dolo eventual.","dolo eventual e culpa consciente.","dolo direto e culpa inconsciente.","culpa inconsciente e dolo direto.","dolo eventual e dolo direto."],"B",
  "No dolo eventual o agente aceita o resultado (“tanto faz”); na culpa consciente, prevê, mas confia que o evitará.","Aceita = dolo eventual; confia = culpa consciente."),
 ("Dolo e culpa","Salvo os casos expressos em lei:",
  ["todo crime admite a forma culposa.","ninguém pode ser punido por fato previsto como crime senão quando o pratica dolosamente.","o crime culposo é punido com a mesma pena do doloso.","a culpa é presumida.","a punição independe de dolo ou culpa."],"B",
  "Art. 18, parágrafo único: excepcionalidade do crime culposo.","Culposo só com previsão expressa."),
 ("Tentativa","Iniciada a execução, o crime não se consuma por circunstâncias alheias à vontade do agente. Salvo disposição em contrário, a pena será:",
  ["a mesma do crime consumado.","a do crime consumado, diminuída de um a dois terços.","a do crime consumado, diminuída de metade.","de multa, apenas.","nenhuma, pois tentativa não é punível."],"B",
  "Art. 14, II, e parágrafo único, do CP.","Tentativa: menos 1/3 a 2/3."),
 ("Ilicitude","NÃO é causa de exclusão da ilicitude prevista no art. 23 do Código Penal:",
  ["estado de necessidade.","legítima defesa.","estrito cumprimento de dever legal.","coação moral irresistível.","exercício regular de direito."],"D",
  "A coação moral irresistível exclui a culpabilidade (art. 22). As demais estão no art. 23.","Art. 23: EN, LD, ECDL, ERD."),
 ("Ilicitude","Nos termos do art. 25 do CP, entende-se em legítima defesa quem, usando moderadamente dos meios necessários, repele injusta agressão:",
  ["passada, a direito seu.","atual ou iminente, a direito seu ou de outrem.","futura e incerta, apenas a direito seu.","atual, apenas a direito de outrem.","qualquer, ainda que justa."],"B",
  "Texto do art. 25, caput.","LD: agressão injusta, atual ou iminente, a direito seu ou de outrem."),
 ("Ilicitude","Na legítima defesa, o agente que, após cessada a agressão, continua a golpear o agressor já rendido:",
  ["permanece amparado pela excludente.","responde pelo excesso doloso ou culposo.","é isento de pena por coação.","comete fato atípico.","está em estado de necessidade."],"B",
  "Art. 23, parágrafo único: o agente responde pelo excesso doloso ou culposo.","Excesso é punível."),
 ("Culpabilidade","São elementos da culpabilidade:",
  ["conduta, resultado e nexo causal.","imputabilidade, potencial consciência da ilicitude e exigibilidade de conduta diversa.","tipicidade e ilicitude.","dolo, culpa e resultado.","legítima defesa e estado de necessidade."],"B",
  "IPE. A alternativa A traz elementos do fato típico; E traz excludentes de ilicitude.","Culpabilidade: IPE."),
 ("Culpabilidade","Sobre a culpabilidade, assinale a alternativa correta.",
  ["A emoção e a paixão excluem a imputabilidade.","O desconhecimento da lei é escusável.","Os menores de 18 anos são penalmente inimputáveis, ficando sujeitos às normas da legislação especial.","A obediência a ordem manifestamente ilegal isenta o subordinado de pena.","O erro de proibição evitável isenta de pena."],"C",
  "Art. 27. Emoção e paixão não excluem a imputabilidade (art. 28, I); o desconhecimento da lei é inescusável (art. 21); a ordem deve ser não manifestamente ilegal (art. 22); o erro evitável apenas pode diminuir a pena.","Menor de 18 → inimputável."),
 ("Penas","Nos termos do art. 33 do CP, a pena de detenção será cumprida:",
  ["obrigatoriamente em regime fechado.","em regime semiaberto ou aberto, salvo necessidade de transferência a regime fechado.","apenas em regime aberto.","em regime fechado, semiaberto ou aberto, à escolha do condenado.","em prisão domiciliar."],"B",
  "Art. 33, caput. A reclusão pode ser cumprida em regime fechado, semiaberto ou aberto.","Detenção: semiaberto ou aberto."),
 ("Penas","Cabe a substituição da pena privativa de liberdade por restritivas de direitos quando, entre outros requisitos:",
  ["a pena aplicada não for superior a 8 anos.","a pena aplicada não for superior a 4 anos e o crime não for cometido com violência ou grave ameaça à pessoa, ou, qualquer que seja a pena, se o crime for culposo.","o réu for reincidente em crime doloso.","o crime for cometido com grave ameaça, desde que a pena seja de até 2 anos.","houver concordância da vítima."],"B",
  "Art. 44, I, combinado com os incisos II (não reincidente em crime doloso) e III (circunstâncias favoráveis).","Até 4 anos, sem violência ou grave ameaça (ou culposo).")]

def qhtml(i, q):
    tema, enun, alts, gab, com, mem = q
    lis = "".join(f'<li data-l="{"ABCDE"[j]}">{a}</li>' for j,a in enumerate(alts))
    return f'<div class="q"><div class="qh"><span class="qn">Questão {i:02d}</span><span class="qa">Questão autoral · {tema}</span></div><p>{enun}</p><ol>{lis}</ol></div>'
qs = [qhtml(i+1,q) for i,q in enumerate(Q)]
add('<div class="marker">§§R3§§</div><div class="unit"><span class="u">PRÁTICA</span><span class="t">24 questões</span></div><h1 class="big">Questões <span class="hl">autorais</span></h1><p class="lead">Elaboradas para este caderno, no estilo de concursos. Nenhuma foi aplicada por banca. Resolva sem consultar.</p>' + "".join(qs[:3]))
for k in range(3, len(qs), 3): add("".join(qs[k:k+3]))
def grid(a, b):
    return "<table><tr>" + "".join(f"<th style='text-align:center'>{i+1:02d}</th>" for i in range(a,b)) + "</tr><tr>" + "".join(f"<td style='text-align:center;font-weight:900;color:{C['navy']}'>{Q[i][3]}</td>" for i in range(a,b)) + "</tr></table>"
gabs = [f'<div class="gab"><div class="gh">Questão {i+1:02d} <span>{q[3]}</span></div><p>{q[4]}</p><span class="mem">Memorize: {q[5]}</span></div>' for i,q in enumerate(Q)]
add('<div class="marker">§§R4§§</div><div class="unit"><span class="u">CORREÇÃO</span></div><h1 class="big">Gabarito <span class="hl">comentado</span></h1><p class="lead">Leia o comentário mesmo quando acertar.</p>' + grid(0,12) + grid(12,24) + "".join(gabs[:4]))
for k in range(4, len(gabs), 6): add("".join(gabs[k:k+6]))
def tr_block(lst):
    out = ""
    for n, itens in lst:
        rows = "".join(f'<tr><td style="width:7%;text-align:center;font-weight:900">{i+1}</td><td style="width:12%;text-align:center" class="{"yes" if r=="C" else "no"}">{"CERTO" if r=="C" else "ERRADO"}</td><td>{c}</td></tr>' for i,(_,r,c) in enumerate(itens))
        out += f'<h3>Treino rápido · Unidade {n}</h3><table><tr><th>#</th><th>Resposta</th><th>Comentário</th></tr>{rows}</table>'
    return out
add('<div class="unit"><span class="u">CORREÇÃO</span><span class="t">Treinos rápidos</span></div><h1 class="big">Respostas dos <span class="hl">treinos</span></h1><p class="lead">Certo ou errado das Unidades 1 a 4.</p>' + tr_block(TREINOS[:2]))
add(tr_block(TREINOS[2:]))

add(f'''<div class="unit"><span class="u">ENCERRAMENTO</span></div><h1 class="big">Referências e <span class="hl">verificação</span></h1><p class="lead">De onde vieram as informações.</p>
<h3>Legislação consultada (portal do Planalto)</h3>
<ul>
<li><strong>Código Penal</strong> (Decreto-Lei nº 2.848/1940): arts. 1º a 7º, 13, 14, 18, 21 a 27, 32, 33, 43, 44, 49, 59 e 75. Citados também os arts. 28, 129, 155, 312 e 345.</li>
<li><strong>Lei de Introdução ao Código Penal</strong> (Decreto-Lei nº 3.914/1941), art. 1º · <strong>Lei das Contravenções Penais</strong> (Decreto-Lei nº 3.688/1941), arts. 4º e 5º.</li>
<li><strong>Constituição Federal</strong>: art. 5º, XXXIX, XL, XLV, XLVI e XLVII; arts. 22, I, 62, § 1º, I, “b”, e 225, § 3º.</li>
<li>Lei nº 13.964/2019 (alterou o art. 75 do CP).</li>
</ul>
<h3>Jurisprudência citada</h3>
<ul><li>STF: Súmulas 611 e 711; vetores do princípio da insignificância (HC 84.412).</li></ul>''' + lembre("{{VERIF}}", "Verificação e limitações"))
add('''<div class="ending"><h2>Fim do Caderno 05</h2><p style="text-align:center">Próximo passo sugerido na coleção: <strong>Direito Penal: Parte Especial (crimes em espécie)</strong>.</p>
<p class="note" style="text-align:center">Caderno Simplificado · Direito Penal · Caderno 05 · 1ª edição · novembro de 2026<br>Material de estudo independente. Não substitui a leitura da lei e do edital do seu concurso.</p></div>''')

VERIF = open(os.path.join(HERE, "verificacao.html")).read() if os.path.exists(os.path.join(HERE, "verificacao.html")) else "<p>(pendente)</p>"
doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Caderno Simplificado — Caderno 05 — Direito Penal: Parte Geral</title>
<link rel="stylesheet" href="estilo.css"></head><body>{symbols()}{"".join(P)}</body></html>'''
open(os.path.join(HERE, "miolo.html"), "w").write(doc.replace("{{VERIF}}", VERIF))
print("páginas planejadas:", len(P))
