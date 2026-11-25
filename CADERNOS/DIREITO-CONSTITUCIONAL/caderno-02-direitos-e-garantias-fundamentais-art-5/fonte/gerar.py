"""Gera miolo.html do Caderno 02 de Direito Constitucional (art. 5º). Uso: python3 gerar.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from componentes import *

DATA = "25 de novembro de 2026"
P = []
def add(html, first=False): P.append(page(f'<div class="marker">§§P{len(P)+1:03d}§§</div>' + html, first))
U1, U2, U3, U4 = "UNIDADE 1", "UNIDADE 2", "UNIDADE 3", "UNIDADE 4"
T1, T2, T3, T4 = "Teoria dos direitos fundamentais", "Os 5 direitos do caput", "Liberdades e proteções", "Remédios e garantias processuais"
CF = "Art. 5º, {} · Constituição Federal"
def cf(x): return CF.format(x)
def p(t): return f"<p>{t}</p>"

def colors(*keys):
    m = {"b":(C['blue'],C['sky']),"g":(C['green'],C['greensoft']),"o":(C['golddeep'],C['goldsoft']),"r":(C['red'],C['redsoft']),"n":(C['navy'],'#e3e9f3')}
    return [m[k] for k in keys]

# =========================================================== APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">O art. 5º em situações do dia a dia, um assunto por vez.</p>
<p>Este é o <strong>Caderno 02 da coleção de Direito Constitucional</strong>, dedicado aos <strong>Direitos e Garantias Fundamentais do art. 5º</strong>. É o artigo mais cobrado da Constituição em provas de nível médio e superior, e também o mais longo: são 79 incisos e 4 parágrafos.</p>
<p>Aqui você não vai decorar a lista seca. Cada direito vira uma <strong>situação ilustrada</strong>: uma pessoa, um problema e a resposta da Constituição. Em geral, cada assunto ocupa <strong>duas páginas</strong>:</p>
{cards([("book","Página 1 · Entenda","Título, texto da lei, <b>Traduzindo o juridiquês</b> e a faixa <b>Memorize</b>.", C['golddeep']),
        ("bulb","Página 2 · Pratique","<b>Entenda na prática</b> (esquema visual), exemplo do dia a dia e <b>Pegadinha de concurso</b>.", C['blue'])],2)}
<h3>Recursos especiais deste caderno</h3>
{table(["Recurso","Onde está"],[
 ["Treino rápido Certo ou Errado","No fim de cada unidade, com respostas no gabarito"],
 ["Árvore de decisão: “qual remédio usar?”","Unidade 4, abertura dos remédios constitucionais"],
 ["Quadro comparativo dos 5 remédios","Unidade 4"],
 ["As 12 confusões mais comuns","Revisão final"],
 ["24 questões autorais comentadas","Prática final"]],["50%",None])}
{lembre(f'''<p><strong>Material pesquisado e atualizado em: {DATA}.</strong> Todos os incisos do art. 5º citados foram conferidos palavra por palavra no texto compilado do Planalto, assim como as Leis nº 9.507/1997, 12.016/2009, 13.300/2016 e 13.869/2019. As questões são <strong>autorais</strong> e nunca foram aplicadas por banca. As limitações da verificação estão nas Referências.</p>''', "Fontes e atualização")}''', first=True)

TOC = [("u","UNIDADE 1 · TEORIA DOS DIREITOS FUNDAMENTAIS","U1"),
 ("","1. O que são direitos fundamentais","A01"),("","2. Direitos x garantias","A02"),("","3. Características dos direitos fundamentais","A03"),
 ("u","UNIDADE 2 · OS 5 DIREITOS DO CAPUT","U2"),
 ("","4. Igualdade","A04"),("","5. Direito à vida","A05"),("","6. Liberdade","A06"),("","7. Segurança","A07"),("","8. Propriedade","A08"),
 ("u","UNIDADE 3 · LIBERDADES E PROTEÇÕES","U3"),
 ("","9. Legalidade","A09"),("","10. Liberdade de expressão","A10"),("","11. Liberdade religiosa","A11"),("","12. Direito de reunião","A12"),
 ("","13. Direito de associação","A13"),("","14. Inviolabilidade domiciliar","A14"),("","15. Sigilo das comunicações","A15"),("","16. Direito de petição","A16"),
 ("u","UNIDADE 4 · REMÉDIOS E GARANTIAS PROCESSUAIS","U4"),
 ("","17. Qual remédio usar? (árvore de decisão)","A17"),("","18. Habeas corpus","A18"),("","19. Habeas data","A19"),("","20. Mandado de segurança","A20"),
 ("","21. Mandado de injunção","A21"),("","22. Ação popular","A22"),("","23. Quadro comparativo dos remédios","A23"),
 ("","24. Devido processo legal","A24"),("","25. Contraditório e ampla defesa","A25"),
 ("u","REVISÃO E PRÁTICA","RV"),
 ("","Mapa conceitual · As 12 confusões mais comuns","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),("","Gabarito, respostas dos treinos e referências","R4")]
toc = "".join(f'<li class="u"><span class="t">{t}</span><span class="p" data-pg="{m}"></span></li>' if k=="u"
              else f'<li><span class="t">{t}</span><span class="p" data-pg="{m}"></span></li>' for k,t,m in TOC)
add(f'''<div class="unit"><span class="u">MAPA DO CADERNO</span></div><h1 class="big">Sumário</h1>
<ol class="toc" style="border-top:3px solid #0b2a5b;margin-top:6pt">{toc}</ol>''')

def opener(num, kicker, title, items, marker):
    lis = "".join(f'<li><span>{i+1:02d}</span>{t}</li>' for i,t in enumerate(items))
    add(f'''<div class="marker">§§{marker}§§</div><div class="opener"><div class="num">{num}</div><div class="k">{kicker}</div><h1>{title}</h1><ul>{lis}</ul></div>''')

TREINOS = []  # (unidade, [(afirmação, C/E, comentário)])
def treino(n, itens):
    TREINOS.append((n, itens))
    rows = "".join(f'<tr><td style="width:7%;text-align:center;font-weight:900;color:{C["navy"]}">{i+1}</td><td>{a}</td><td style="width:16%;text-align:center">( C ) &nbsp; ( E )</td></tr>' for i,(a,_,_) in enumerate(itens))
    add(f'''<div class="unit"><span class="u">TREINO RÁPIDO</span><span class="t">Unidade {n}</span></div><h1 class="big">Certo ou <span class="hl">errado?</span></h1>
<p class="lead">Marque C ou E sem consultar. As respostas comentadas estão no gabarito, no fim do caderno.</p>
<table><tr><th>#</th><th>Afirmação</th><th style="text-align:center">Sua resposta</th></tr>{rows}</table>''' +
    memo('Errou? Volte à página do assunto e releia a faixa <strong>Memorize</strong> e a <strong>Pegadinha</strong>. É ali que está a resposta.', "Dica:"))

# =========================================================== UNIDADE 1
opener("01","UNIDADE 1","Teoria dos direitos fundamentais",["O que são direitos fundamentais","Direitos x garantias","Características dos direitos fundamentais"],"U1")

CAPUT = '<p>Art. 5º Todos são iguais perante a lei, sem distinção de qualquer natureza, garantindo-se aos brasileiros e aos estrangeiros residentes no País a inviolabilidade do direito à vida, à liberdade, à igualdade, à segurança e à propriedade, nos termos seguintes:</p>'
add(head(U1,T1,'O que são direitos <span class="hl">fundamentais</span>?','Os direitos mínimos para uma vida livre e digna, protegidos pela Constituição.', "A01") +
 oque(p('<strong>Direitos fundamentais</strong> são os direitos básicos da pessoa humana <strong>reconhecidos e protegidos pela Constituição</strong> de um país. Eles limitam o poder do Estado e garantem a cada pessoa condições mínimas de liberdade, igualdade e dignidade.')) +
 lei(cf("caput"), CAPUT) +
 traduz(p('Pense nos direitos fundamentais como um <strong>escudo</strong> que a Constituição entrega a cada pessoa. Esse escudo protege contra abusos do Estado (e, em certos casos, de outras pessoas). O art. 5º traz o principal conjunto desses escudos, os <strong>direitos e deveres individuais e coletivos</strong>.')) +
 memo('O caput protege <strong>5 direitos</strong>: <strong>vida, liberdade, igualdade, segurança e propriedade</strong>. Os 79 incisos detalham esses cinco.'))

geracoes = f'''<figure><svg viewBox="0 0 640 170" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">''' + "".join(
 f'<rect x="{x}" y="10" width="196" height="150" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x+98}" y="38" text-anchor="middle" font-weight="900" font-size="15" fill="{fg}">{t}</text><text x="{x+98}" y="60" text-anchor="middle" font-weight="900" font-size="13" fill="{C["ink"]}">{l}</text>'
 + "".join(f'<text x="{x+98}" y="{86+i*17}" text-anchor="middle" font-size="11.5" fill="{C["ink"]}">{ln}</text>' for i,ln in enumerate(ls))
 for x,t,l,ls,fg,bg in [(10,"1ª DIMENSÃO","LIBERDADE",["direitos civis e políticos","Estado deve se ABSTER","(vida, propriedade, voto)","séc. XVIII"],C['blue'],C['sky']),
   (222,"2ª DIMENSÃO","IGUALDADE",["direitos sociais, econômicos","e culturais: Estado deve AGIR","(saúde, educação, trabalho)","início do séc. XX"],C['green'],C['greensoft']),
   (434,"3ª DIMENSÃO","FRATERNIDADE",["direitos difusos, de toda","a coletividade","(meio ambiente, paz,","desenvolvimento)"],C['golddeep'],C['goldsoft'])]) + '</svg><figcaption>As dimensões (gerações) dos direitos seguem o lema da Revolução Francesa: liberdade, igualdade, fraternidade.</figcaption></figure>'
add(pratica_title("Entenda na prática") + geracoes +
 ex(p('<b>Quem é protegido?</b> O caput fala em “brasileiros e estrangeiros residentes no País”. Mas o STF interpreta o texto de forma ampla: um turista estrangeiro preso no aeroporto de Fortaleza também pode impetrar <i>habeas corpus</i>. E pessoas jurídicas têm os direitos compatíveis com a sua natureza (por exemplo, honra objetiva, propriedade e sigilo).')) +
 lei(cf("§§ 1º e 2º"),'<p>§ 1º As normas definidoras dos direitos e garantias fundamentais têm aplicação imediata.<br>§ 2º Os direitos e garantias expressos nesta Constituição não excluem outros decorrentes do regime e dos princípios por ela adotados, ou dos tratados internacionais em que a República Federativa do Brasil seja parte.</p>') +
 pega('<ul><li>“O art. 5º protege apenas brasileiros e estrangeiros residentes.” Na <b>literalidade</b> do caput, sim. Mas, pelo entendimento do STF, a proteção alcança também o estrangeiro <b>não residente</b> (em trânsito). Leia o comando: “segundo a CF” (literal) ou “segundo o STF”.</li><li>O rol do art. 5º é <b>exemplificativo</b> (§ 2º): existem direitos fundamentais fora dele, como o princípio da anterioridade tributária (art. 150, III, “b”), segundo o STF.</li><li>Direitos fundamentais também valem <b>entre particulares</b> (eficácia horizontal): o STF anulou a exclusão de um associado feita sem direito de defesa (RE 201.819).</li></ul>'))

add(head(U1,T1,'Direitos x <span class="hl">garantias</span>','Um declara o bem protegido; a outra é a ferramenta que o protege.', "A02") +
 cards([("heart","DIREITO","Norma <b>declaratória</b>: reconhece um bem da vida. Ex.: “é livre a locomoção” (XV).",C['blue']),
        ("shield","GARANTIA","Norma <b>assecuratória</b>: é o instrumento que protege o direito. Ex.: <i>habeas corpus</i> (LXVIII).",C['golddeep']),
        ("gavel","REMÉDIO CONSTITUCIONAL","Garantia em forma de <b>ação judicial</b>: HC, HD, MS, MI e ação popular.",C['red'])],3) +
 traduz(p('O <strong>direito</strong> é o bem que você tem, como a sua liberdade de ir e vir. A <strong>garantia</strong> é o “cadeado” que protege esse bem. Se alguém prende você ilegalmente, o <i>habeas corpus</i> é a chave que abre a cela. Rui Barbosa resumia assim: direitos são disposições <strong>declaratórias</strong>, e garantias são disposições <strong>assecuratórias</strong>.')) +
 table(["Direito (declara)","Garantia (protege)"],[
  ["Liberdade de locomoção (XV)","<i>Habeas corpus</i> (LXVIII)"],
  ["Acesso a informações pessoais (XXXIII e LXXII)","<i>Habeas data</i> (LXXII)"],
  ["Inviolabilidade da casa (XI)","Exigência de ordem judicial, cumprida durante o dia (XI)"],
  ["Liberdade (LIV)","Devido processo legal (LIV)"],
  ["Direito de defesa (LV)","Contraditório e ampla defesa (LV)"]],["50%",None],rh=False) +
 memo('<strong>Direito</strong> = declara (o bem). <strong>Garantia</strong> = assegura (o cadeado). Às vezes os dois estão <strong>no mesmo inciso</strong>.'))

add(pratica_title() +
 flow([("heart",["DIREITO","liberdade de","locomoção"]),("alert",["VIOLAÇÃO","prisão","ilegal"]),("shield",["GARANTIA","habeas","corpus"]),("unlock",["RESULTADO","liberdade","restabelecida"])],
      "A garantia entra em ação quando o direito é ameaçado ou violado.", colors=colors("b","r","o","g")) +
 ex(p('Marina foi presa sem ordem judicial e sem estar em flagrante. Seu <b>direito</b> violado é a liberdade de locomoção. A <b>garantia</b> que ela usa é o <i>habeas corpus</i>, que pode ser impetrado por qualquer pessoa, até por um amigo, sem advogado.')) +
 pega('<ul><li>“Direitos e garantias são sinônimos.” <b>Errado</b>: direitos declaram, garantias asseguram.</li><li>“Garantias são apenas os remédios constitucionais.” <b>Errado</b>: os remédios são uma <b>espécie</b> de garantia. Há garantias que não são ações, como a exigência de ordem judicial para entrar numa casa durante o dia.</li><li>O Título II da CF chama-se “Dos Direitos e Garantias Fundamentais” e abrange os arts. 5º a 17: direitos individuais e coletivos, sociais, de nacionalidade, políticos e partidos políticos.</li></ul>') +
 kw(["declaratórias","assecuratórias","remédios constitucionais","Rui Barbosa","Título II: arts. 5º a 17"]))

add(head(U1,T1,'Características dos direitos <span class="hl">fundamentais</span>','As “qualidades” que todo direito fundamental tem.', "A03") +
 table(["Característica","Significado","Exemplo"],[
  ["Historicidade","Surgem e evoluem ao longo da história.","A proteção de dados pessoais virou direito fundamental em 2022 (LXXIX)."],
  ["Universalidade","Pertencem a todos os seres humanos.","Um estrangeiro em trânsito também não pode ser torturado."],
  ["Inalienabilidade","Não podem ser vendidos nem transferidos.","Ninguém pode vender sua liberdade."],
  ["Imprescritibilidade","Não se perdem pelo passar do tempo.","Quem passa 30 anos sem votar continua com o direito ao voto."],
  ["Irrenunciabilidade","Não se pode abrir mão deles de forma definitiva (o não exercício temporário é possível).","Participar de um reality show não significa renunciar para sempre à intimidade."],
  ["Relatividade (limitabilidade)","Nenhum direito é absoluto: podem ceder diante de outros.","A liberdade de expressão não protege a calúnia."],
  ["Concorrência","Podem ser exercidos ao mesmo tempo.","Um jornalista exerce informação, opinião e expressão juntas."],
  ["Complementaridade","Devem ser interpretados em conjunto.","Vida digna exige saúde, moradia e liberdade."]],["24%",None,"36%"]) +
 traduz(p('Guarde a ideia central: os direitos fundamentais são de <strong>todos</strong>, <strong>não se vendem</strong>, <strong>não vencem</strong> com o tempo, <strong>não se renunciam</strong> para sempre e <strong>não são absolutos</strong>. Quando dois direitos entram em choque, o juiz faz uma <strong>ponderação</strong> no caso concreto.')))

add(pratica_title("Quando dois direitos se chocam") +
 flow([("megaphone",["LIBERDADE DE","IMPRENSA","publicar notícia"]),("scales",["PONDERAÇÃO","juiz analisa","o caso concreto"]),("eye",["INTIMIDADE","E HONRA","da pessoa"])],
      "Colisão de direitos: nenhum vence sempre; o juiz pondera conforme o caso.", colors=colors("b","o","r")) +
 ex(p('Um site publica a foto de uma celebridade na praia. A liberdade de imprensa (IX) choca-se com a imagem e a intimidade (X). Não existe resposta pronta: o juiz pondera o interesse público da notícia, o local e a forma da publicação. Se houver abuso, cabe <b>indenização</b>, mas <b>não censura prévia</b>.')) +
 pega('<ul><li>“Os direitos fundamentais são absolutos.” <b>Errado</b>: são <b>relativos</b>. Parte da doutrina aponta como exceções a proibição da tortura e a da escravidão, que seriam absolutas.</li><li>“Os direitos fundamentais são renunciáveis.” <b>Errado</b>: são <b>irrenunciáveis</b>. O que se admite é a <b>limitação voluntária</b> e temporária do seu exercício.</li><li>As normas de direitos fundamentais têm <b>aplicação imediata</b> (§ 1º): não dependem, em regra, de lei para valer.</li></ul>') +
 memo('<b>HUIIR</b> → <strong>H</strong>istóricos, <strong>U</strong>niversais, <strong>I</strong>nalienáveis, <strong>I</strong>mprescritíveis, <strong>I</strong>rrenunciáveis e <strong>R</strong>elativos.', "Mnemônico:"))

treino(1, [
 ("O caput do art. 5º protege, literalmente, os brasileiros e os estrangeiros residentes no País.","C","É a literalidade do caput. O STF amplia a proteção ao estrangeiro não residente."),
 ("Direitos e garantias fundamentais são expressões sinônimas.","E","Direitos são declaratórios; garantias são assecuratórias."),
 ("O rol de direitos do art. 5º é taxativo.","E","É exemplificativo (art. 5º, § 2º)."),
 ("As normas definidoras de direitos e garantias fundamentais têm aplicação imediata.","C","É o texto do § 1º."),
 ("Os direitos fundamentais podem ser vendidos, pois integram o patrimônio da pessoa.","E","São inalienáveis."),
 ("A liberdade de expressão é um direito absoluto.","E","Os direitos fundamentais são relativos; não protegem a calúnia, por exemplo.")])

# =========================================================== UNIDADE 2
opener("02","UNIDADE 2","Os 5 direitos do caput",["Igualdade","Direito à vida","Liberdade","Segurança","Propriedade"],"U2")

add(head(U2,T2,'<span class="hl">Igualdade</span>','Tratar igualmente os iguais e desigualmente os desiguais, na medida da desigualdade.', "A04") +
 lei(cf("caput e inciso I"),'<p>Todos são iguais perante a lei, sem distinção de qualquer natureza (...)<br>I - homens e mulheres são iguais em direitos e obrigações, nos termos desta Constituição;</p>') +
 cards([("scales","Igualdade FORMAL","Todos são iguais <b>perante a lei</b>: a mesma regra para todos.",C['blue']),
        ("people","Igualdade MATERIAL","Tratar desigualmente os desiguais para <b>reduzir desigualdades reais</b>.",C['green'])],2) +
 traduz(p('Imagine três pessoas de alturas diferentes tentando ver um jogo por cima do muro. Dar <strong>um banquinho igual</strong> para cada uma é igualdade <strong>formal</strong>. Dar <strong>mais banquinhos a quem é mais baixo</strong>, para que todos enxerguem, é igualdade <strong>material</strong>. A Constituição adota as duas.')) +
 memo('Igualdade <strong>formal</strong> = perante a lei. Igualdade <strong>material</strong> = reduzir desigualdades (ações afirmativas, cotas). Diferenciar é permitido quando há <strong>justificativa razoável</strong>.'))

add(pratica_title() +
 flow([("people",["DIFERENÇA","DE TRATAMENTO"]),("q",["HÁ MOTIVO","RAZOÁVEL?","ligado ao objetivo"]),("check",["SIM","diferenciação","válida"]),("xmark",["NÃO","discriminação","inconstitucional"])],
      "Teste da igualdade: toda diferenciação precisa de uma justificativa razoável.", colors=colors("n","o","g","r")) +
 ex(p('<b>Concurso público:</b> um edital para Guarda Municipal limita a idade máxima dos candidatos. Pela Súmula 683 do STF, o limite de idade só é legítimo quando <b>justificado pela natureza das atribuições do cargo</b>. E a exigência de exame psicotécnico só vale se prevista em <b>lei</b> (Súmula Vinculante 44). <b>Cotas raciais</b> em universidades públicas foram declaradas constitucionais pelo STF (ADPF 186).')) +
 pega('<ul><li>Igualdade <b>não</b> proíbe toda diferenciação: proíbe a diferenciação <b>sem justificativa razoável</b>.</li><li>Homens e mulheres são iguais “<b>nos termos desta Constituição</b>”: a própria CF traz diferenças, como a licença-maternidade maior que a paternidade e regras próprias de aposentadoria.</li><li>Requisitos de concurso (idade, altura, psicotécnico) precisam de <b>previsão legal</b> e de relação com as <b>atribuições do cargo</b>.</li></ul>') +
 kw(["igualdade formal","igualdade material","ações afirmativas","Súmula 683 (idade)","SV 44 (psicotécnico)","nos termos desta Constituição"]))

add(head(U2,T2,'Direito à <span class="hl">vida</span>','O direito que dá sentido a todos os outros.', "A05") +
 lei(cf("III e XLVII"),'<p>III - ninguém será submetido a tortura nem a tratamento desumano ou degradante;<br>XLVII - não haverá penas: a) de morte, salvo em caso de guerra declarada, nos termos do art. 84, XIX; b) de caráter perpétuo; c) de trabalhos forçados; d) de banimento; e) cruéis;</p>') +
 cards([("pulse","Direito de continuar vivo","Ninguém pode ser morto arbitrariamente. Por isso a regra é a proibição da pena de morte.",C['red']),
        ("heart","Direito a uma vida digna","Viver com o mínimo: saúde, alimentação, moradia e integridade física e moral.",C['green'])],2) +
 traduz(p('O direito à vida tem <strong>duas faces</strong>: o direito de <strong>não ser morto</strong> e o direito de <strong>viver com dignidade</strong>. Por isso a CF proíbe a tortura e as penas cruéis, e só admite a pena de morte em <strong>uma</strong> situação: <strong>guerra declarada</strong>.')) +
 memo('Pena de morte: <strong>proibida</strong>, <strong>salvo em caso de guerra declarada</strong> (art. 84, XIX). Penas proibidas: <b>morte, perpétua, trabalhos forçados, banimento e cruéis</b>.'))

add(pratica_title() +
 flow([("pulse",["VIDA","regra:","proteção"]),("xmark",["PENA DE MORTE","proibida"]),("alert",["EXCEÇÃO","guerra","declarada"]),("shield",["TORTURA","proibida sem","exceção"])],
      "A vida é protegida com uma única exceção expressa para a pena de morte.", colors=colors("g","r","o","n")) +
 ex(p('O direito à vida, como todo direito fundamental, não é absoluto. O STF decidiu que <b>não é crime</b> a interrupção da gravidez de feto <b>anencéfalo</b> (ADPF 54) e que as <b>pesquisas com células-tronco embrionárias</b>, nos termos da Lei de Biossegurança, são constitucionais (ADI 3.510). E a legítima defesa (art. 25 do CP) permite reagir a uma agressão injusta, inclusive com risco à vida do agressor.')) +
 pega('<ul><li>Pena de morte: exceção <b>só</b> em <b>guerra declarada</b>. Não é “guerra civil”, “estado de sítio” nem “crimes hediondos”.</li><li>Penas de <b>caráter perpétuo</b> são proibidas, inclusive a prisão perpétua.</li><li>Tortura: o art. 5º, XLIII, a considera crime <b>inafiançável</b> e insuscetível de <b>graça ou anistia</b>.</li></ul>') +
 kw(["duas acepções","guerra declarada","art. 84, XIX","penas proibidas","tortura","ADPF 54","ADI 3.510"]))

add(head(U2,T2,'<span class="hl">Liberdade</span>','Ir, vir, pensar, crer, reunir-se, associar-se e trabalhar.', "A06") +
 lei(cf("XV"),'<p>XV - é livre a locomoção no território nacional em tempo de paz, podendo qualquer pessoa, nos termos da lei, nele entrar, permanecer ou dele sair com seus bens;</p>') +
 traduz(p('“Liberdade” no caput é uma palavra-mãe: dela nascem várias liberdades específicas, que você vai estudar uma a uma na Unidade 3. A mais básica é a <strong>liberdade de locomoção</strong>: entrar, ficar e sair do país, e circular dentro dele, levando seus bens. Quem protege essa liberdade é o <i>habeas corpus</i>.')) +
 cards([("pin","Locomoção","Ir, vir e permanecer (XV)",C['blue']),("megaphone","Pensamento e expressão","IV, V e IX",C['golddeep']),("church","Crença","VI a VIII",C['green']),
        ("people","Reunião","XVI",C['red']),("handshake","Associação","XVII a XXI",C['navy']),("briefcase","Profissão","XIII",C['blue'])],3) +
 memo('Locomoção é livre <strong>em tempo de paz</strong> e <strong>nos termos da lei</strong>. Garantia: <i>habeas corpus</i>.'))

add(pratica_title() +
 flow([("pin",["ENTRAR","no território"]),("house",["PERMANECER","nele"]),("link",["SAIR","dele"]),("briefcase",["COM SEUS","BENS"])],
      "Art. 5º, XV: quatro elementos da liberdade de locomoção.", colors=colors("b","g","o","n")) +
 ex(p('Durante uma epidemia, a lei pode impor restrições temporárias de circulação por razões de saúde pública: a liberdade de locomoção é relativa e vale “<b>nos termos da lei</b>”. Já um prefeito que proíba, por conta própria, a entrada de moradores de outra cidade viola o inciso XV. Em <b>estado de sítio</b>, a própria CF autoriza restrições maiores (art. 139, I).')) +
 pega('<ul><li>A locomoção é livre “<b>em tempo de paz</b>”. Em tempo de guerra admitem-se restrições maiores.</li><li>O livre exercício de profissão (XIII) também é relativo: “atendidas as qualificações profissionais que a lei estabelecer”. Por isso a lei pode exigir o exame da OAB, por exemplo.</li><li>Quem protege a locomoção é o <b>habeas corpus</b>, e não o mandado de segurança.</li></ul>') +
 kw(["em tempo de paz","nos termos da lei","entrar, permanecer ou sair","com seus bens","habeas corpus"]))

add(head(U2,T2,'<span class="hl">Segurança</span>','Segurança pessoal e, sobretudo, segurança jurídica.', "A07") +
 lei(cf("XXXVI"),'<p>XXXVI - a lei não prejudicará o direito adquirido, o ato jurídico perfeito e a coisa julgada;</p>') +
 cards([("star","Direito adquirido","Direito que já entrou no seu patrimônio porque você cumpriu todos os requisitos.",C['blue']),
        ("doc","Ato jurídico perfeito","Ato já concluído segundo a lei da época. Ex.: contrato assinado.",C['golddeep']),
        ("gavel","Coisa julgada","Decisão judicial da qual não cabe mais recurso.",C['red'])],3) +
 traduz(p('A segurança do caput tem dois sentidos. A <strong>segurança pessoal</strong> é estar protegido contra violência. A <strong>segurança jurídica</strong> é poder confiar nas regras: uma lei nova <strong>não pode desfazer</strong> o que já foi conquistado ou decidido de forma definitiva. Ninguém consegue planejar a vida se as regras mudarem para trás.')) +
 memo('A lei nova não prejudica: <strong>direito adquirido</strong>, <strong>ato jurídico perfeito</strong> e <strong>coisa julgada</strong>. Mnemônico: <b>DAC</b> (Direito adquirido, Ato perfeito, Coisa julgada).'))

add(pratica_title() +
 flow([("calendar",["2024","João cumpre todos","os requisitos"]),("doc",["2026","lei nova muda","as regras"]),("shield",["RESULTADO","direito de João","está protegido"])],
      "Direito adquirido: a lei nova não alcança quem já tinha cumprido os requisitos.", colors=colors("g","o","b")) +
 ex(p('João completou em 2024 todos os requisitos para se aposentar, mas não fez o pedido. Em 2026 uma nova regra torna a aposentadoria mais difícil. Como João já tinha <b>direito adquirido</b>, poderá se aposentar pelas regras antigas. Quem ainda não tinha completado os requisitos tinha só uma <b>expectativa de direito</b> e segue a regra nova.')) +
 pega('<ul><li>Não existe direito adquirido contra a <b>Constituição originária</b>, nem direito adquirido a <b>regime jurídico</b>: um servidor não pode exigir que as regras da carreira nunca mudem.</li><li>“Segurança” no caput do art. 5º (direito individual) não se confunde com “segurança pública” (art. 144), que é dever do Estado e responsabilidade de todos.</li><li><b>Expectativa de direito</b> não é protegida como direito adquirido.</li></ul>') +
 kw(["segurança jurídica","direito adquirido","ato jurídico perfeito","coisa julgada","expectativa de direito"]))

add(head(U2,T2,'<span class="hl">Propriedade</span>','Garantida, mas com função social.', "A08") +
 lei(cf("XXII a XXV"),'<p>XXII - é garantido o direito de propriedade;<br>XXIII - a propriedade atenderá a sua função social;<br>XXIV - a lei estabelecerá o procedimento para desapropriação por necessidade ou utilidade pública, ou por interesse social, mediante justa e prévia indenização em dinheiro, ressalvados os casos previstos nesta Constituição;<br>XXV - no caso de iminente perigo público, a autoridade competente poderá usar de propriedade particular, assegurada ao proprietário indenização ulterior, se houver dano;</p>') +
 traduz(p('A sua casa, seu carro e seu terreno são seus: a propriedade é <strong>garantida</strong>. Mas ela não pode ser usada contra a sociedade: deve cumprir uma <strong>função social</strong>. Por isso o Poder Público pode, em certos casos, <strong>tomar</strong> o bem (desapropriação) ou <strong>usá-lo temporariamente</strong> numa emergência (requisição).')) +
 memo('Desapropriação: indenização <strong>justa, prévia e em dinheiro</strong> (regra). Requisição: <strong>iminente perigo público</strong>, indenização <strong>ulterior</strong> (depois) e <strong>só se houver dano</strong>.'))

add(pratica_title("Desapropriação x requisição") +
 table(["","DESAPROPRIAÇÃO (XXIV)","REQUISIÇÃO (XXV)"],[
  ["O que acontece","O Estado <b>toma</b> o bem definitivamente","O Estado <b>usa</b> o bem temporariamente"],
  ["Motivo","Necessidade ou utilidade pública, ou interesse social","<b>Iminente perigo público</b>"],
  ["Indenização","<b>Justa, prévia e em dinheiro</b> (regra)","<b>Ulterior</b> (depois), <b>se houver dano</b>"],
  ["Exemplo","Casa desapropriada para construir uma avenida","Galpão usado como abrigo durante uma enchente"]],["20%",None,None]) +
 ex(p('Durante uma enchente, a Defesa Civil usa o ginásio de um clube particular para abrigar famílias. Isso é <b>requisição</b>: não precisa pagar antes e só indeniza se o ginásio sofrer dano. Já a prefeitura que quer o terreno de Ana para construir uma escola faz uma <b>desapropriação</b>: Ana recebe indenização justa e prévia, em dinheiro.')) +
 pega('<ul><li>“Indenização <b>prévia</b> na requisição” → <b>errado</b>: na requisição ela é <b>ulterior</b> e só existe se houver dano.</li><li>A regra da indenização prévia e em dinheiro tem <b>exceções</b> na própria CF (“ressalvados os casos previstos”): imóvel urbano ou rural que descumpre a função social pode ser pago em <b>títulos</b> (arts. 182 e 184), e há casos de expropriação <b>sem indenização</b>, como terras com cultivo ilegal de plantas psicotrópicas ou exploração de trabalho escravo (art. 243).</li></ul>') +
 kw(["função social","desapropriação","justa e prévia indenização em dinheiro","requisição","iminente perigo público","indenização ulterior"]))

treino(2, [
 ("A Constituição admite a pena de morte em caso de guerra declarada.","C","Art. 5º, XLVII, “a”, nos termos do art. 84, XIX."),
 ("A igualdade proíbe qualquer tratamento diferenciado entre pessoas.","E","Diferenciações com justificativa razoável são permitidas (igualdade material)."),
 ("Na requisição administrativa, a indenização é prévia e em dinheiro.","E","É ulterior e só se houver dano (XXV)."),
 ("A lei nova não prejudicará o direito adquirido, o ato jurídico perfeito e a coisa julgada.","C","Art. 5º, XXXVI."),
 ("A liberdade de locomoção no território nacional é assegurada em tempo de paz.","C","Art. 5º, XV."),
 ("Segundo o STF, o limite de idade em concurso só é legítimo quando justificado pela natureza das atribuições do cargo.","C","Súmula 683 do STF.")])

# =========================================================== UNIDADE 3
opener("03","UNIDADE 3","Liberdades e proteções",["Legalidade","Liberdade de expressão","Liberdade religiosa","Direito de reunião","Direito de associação","Inviolabilidade domiciliar","Sigilo das comunicações","Direito de petição"],"U3")

add(head(U3,T3,'Princípio da <span class="hl">legalidade</span>','Só a lei pode obrigar você a fazer ou deixar de fazer algo.', "A09") +
 lei(cf("II"),'<p>II - ninguém será obrigado a fazer ou deixar de fazer alguma coisa senão em virtude de lei;</p>') +
 traduz(p('Para o <strong>cidadão</strong>, a regra é a liberdade: você pode fazer <strong>tudo o que a lei não proíbe</strong>. Uma portaria, um decreto ou a vontade de uma autoridade não criam obrigações sozinhos. Já a <strong>Administração Pública</strong> funciona ao contrário: só pode fazer <strong>o que a lei permite</strong> (art. 37).')) +
 table(["","PARTICULAR (art. 5º, II)","ADMINISTRAÇÃO PÚBLICA (art. 37)"],[
  ["Regra","Pode fazer tudo o que a lei <b>não proíbe</b>","Só pode fazer o que a lei <b>permite</b>"],
  ["Ideia","Autonomia da vontade","Subordinação à lei"],
  ["Exemplo","Pintar a casa de qualquer cor, se a lei local não proibir","Servidor só concede um benefício previsto em lei"]],["18%",None,None]) +
 memo('Particular: <strong>tudo o que a lei não proíbe</strong>. Administração: <strong>só o que a lei permite</strong>.'))

add(pratica_title() +
 flow([("doc",["PORTARIA","sem base","em lei"]),("person",["CRIA","OBRIGAÇÃO","ao cidadão"]),("xmark",["VIOLA O","ART. 5º, II"])],
      "Só a lei, em sentido amplo, cria obrigações; atos infralegais apenas regulamentam a lei.", colors=colors("o","n","r")) +
 ex(p('Um guarda municipal exige que um comerciante feche a loja às 18h com base apenas em uma “ordem verbal” do secretário, sem nenhuma lei ou ato normativo fundado em lei. O comerciante não está obrigado: “ninguém será obrigado a fazer ou deixar de fazer alguma coisa <b>senão em virtude de lei</b>”.')) +
 pega('<ul><li><b>Legalidade</b> (art. 5º, II) é mais ampla: “lei” abrange atos normativos com força de lei. <b>Reserva legal</b> é mais estrita: certas matérias só podem ser tratadas por <b>lei formal</b> (ex.: crimes e penas, art. 5º, XXXIX).</li><li>Não confunda a legalidade do <b>particular</b> com a da <b>Administração</b>. É uma das confusões mais cobradas.</li></ul>') +
 kw(["senão em virtude de lei","autonomia da vontade","legalidade administrativa","reserva legal"]))

add(head(U3,T3,'Liberdade de <span class="hl">expressão</span>','Pensar, falar e criar sem censura, mas com responsabilidade.', "A10") +
 lei(cf("IV, V e IX"),'<p>IV - é livre a manifestação do pensamento, sendo vedado o anonimato;<br>V - é assegurado o direito de resposta, proporcional ao agravo, além da indenização por dano material, moral ou à imagem;<br>IX - é livre a expressão da atividade intelectual, artística, científica e de comunicação, independentemente de censura ou licença;</p>') +
 traduz(p('Você pode dizer o que pensa, escrever, criar arte e fazer jornalismo <strong>sem pedir licença</strong> e <strong>sem censura</strong>. Mas precisa <strong>se identificar</strong> (o anonimato é vedado) e <strong>responder pelos abusos</strong>: quem é ofendido tem direito de resposta e de indenização. A regra é: <strong>liberdade antes, responsabilidade depois</strong>.')) +
 memo('Livre manifestação <strong>com identificação</strong> (vedado o anonimato). <strong>Sem censura ou licença</strong>. Abuso gera <strong>direito de resposta proporcional + indenização</strong>.'))

add(pratica_title() +
 flow([("megaphone",["FALA","LIVRE","sem censura"]),("mask",["ANONIMATO","vedado"]),("alert",["ABUSO?","ofensa, dano"]),("scales",["RESPOSTA E","INDENIZAÇÃO","depois"])],
      "Controle posterior, e não prévio: responde-se pelo abuso depois que ele ocorre.", colors=colors("b","r","o","g")) +
 ex(p('Um blogueiro publica, assinando o próprio nome, uma crítica dura ao prefeito: liberdade de expressão. Se publicar uma acusação falsa de crime, o prefeito terá direito de <b>resposta proporcional</b> e de <b>indenização</b>, mas ninguém pode impedir a publicação <b>antes</b>. O STF afirmou que biografias <b>não dependem de autorização prévia</b> do biografado (ADI 4.815).')) +
 pega('<ul><li>A liberdade de expressão <b>não protege o discurso de ódio</b>: o STF manteve a condenação por racismo de quem publicava obras antissemitas (HC 82.424, caso Ellwanger).</li><li><b>Denúncia anônima</b>: segundo o STF, sozinha não basta para instaurar inquérito ou decretar medidas invasivas, mas autoriza <b>diligências preliminares</b> para verificar se os fatos são verdadeiros.</li><li>O direito de resposta é <b>proporcional ao agravo</b> e <b>não exclui</b> a indenização (“além da indenização”).</li></ul>') +
 kw(["vedado o anonimato","direito de resposta proporcional","dano material, moral ou à imagem","independentemente de censura ou licença"]))

add(head(U3,T3,'Liberdade <span class="hl">religiosa</span>','Crer, não crer e praticar a sua fé, num Estado laico.', "A11") +
 lei(cf("VI e VIII"),'<p>VI - é inviolável a liberdade de consciência e de crença, sendo assegurado o livre exercício dos cultos religiosos e garantida, na forma da lei, a proteção aos locais de culto e a suas liturgias;<br>VIII - ninguém será privado de direitos por motivo de crença religiosa ou de convicção filosófica ou política, salvo se as invocar para eximir-se de obrigação legal a todos imposta e recusar-se a cumprir prestação alternativa, fixada em lei;</p>') +
 traduz(p('Cada pessoa escolhe sua religião, ou nenhuma. O Estado brasileiro é <strong>laico</strong>: não tem religião oficial, mas protege todas. O inciso VIII cria a <strong>escusa de consciência</strong>: quem tem uma crença que impede cumprir uma obrigação geral, como o serviço militar, pode cumprir uma <strong>prestação alternativa</strong>. Se recusar as duas, pode perder direitos.')) +
 memo('Escusa de consciência: recusar obrigação geral <strong>+ recusar a prestação alternativa</strong> = <strong>privação de direitos</strong> (perda ou suspensão dos direitos políticos, art. 15, IV).'))

add(pratica_title("Escusa de consciência") +
 flow([("church",["CRENÇA","impede cumprir","obrigação geral"]),("doc",["PRESTAÇÃO","ALTERNATIVA","fixada em lei"]),("check",["CUMPRE","nenhum direito","é perdido"]),("xmark",["RECUSA AS DUAS","privação de","direitos"])],
      "Art. 5º, VIII, combinado com o art. 15, IV.", colors=colors("b","o","g","r")) +
 ex(p('Pedro é convocado para o serviço militar obrigatório, mas sua convicção religiosa o impede de pegar em armas. Ele pode cumprir um <b>serviço alternativo</b> (art. 143, § 1º). Se também se recusar ao serviço alternativo, poderá ter os <b>direitos políticos</b> atingidos (art. 15, IV). Em outro exemplo, o inciso VII assegura <b>assistência religiosa</b> em hospitais, presídios e quartéis.')) +
 pega('<ul><li>Laicidade <b>não</b> é hostilidade à religião: o art. 19, I, ressalva a “colaboração de interesse público, na forma da lei”.</li><li>Ninguém perde direitos <b>só</b> por causa da crença. A privação exige <b>duas recusas</b>: a obrigação geral <b>e</b> a prestação alternativa.</li><li>A proteção aos locais de culto é garantida “<b>na forma da lei</b>”.</li></ul>') +
 kw(["liberdade de consciência e de crença","Estado laico","escusa de consciência","prestação alternativa","art. 15, IV"]))

add(head(U3,T3,'Direito de <span class="hl">reunião</span>','Encontrar-se em público, sem pedir permissão.', "A12") +
 lei(cf("XVI"),'<p>XVI - todos podem reunir-se pacificamente, sem armas, em locais abertos ao público, independentemente de autorização, desde que não frustrem outra reunião anteriormente convocada para o mesmo local, sendo apenas exigido prévio aviso à autoridade competente;</p>') +
 '<h3>Checklist da reunião válida</h3>' +
 cards([("dove","Pacífica","Sem violência.",C['green']),("xmark","Sem armas","Nenhum participante armado.",C['red']),("map","Local aberto ao público","Praças, ruas, parques.",C['blue']),
        ("bell" if False else "megaphone","Prévio AVISO","Avisar a autoridade, e não pedir autorização.",C['golddeep']),("calendar","Não frustrar outra","Respeitar a reunião já convocada para o mesmo local.",C['navy']),("check","Sem autorização","Independe de permissão do Poder Público.",C['green'])],3) +
 traduz(p('Para fazer uma manifestação na praça, você <strong>não pede licença</strong>: apenas <strong>avisa</strong> a autoridade com antecedência, para que ela organize o trânsito e a segurança e para que duas manifestações não sejam marcadas no mesmo lugar e hora.')) +
 memo('Reunião: <strong>aviso</strong> sim, <strong>autorização</strong> não. Pacífica, sem armas, local aberto, sem frustrar reunião anterior.'))

add(pratica_title() +
 flow([("calendar",["GRUPO 1","avisa primeiro","para o sábado"]),("people",["GRUPO 2","quer o mesmo","local e horário"]),("alert",["CONFLITO","não pode frustrar","a anterior"]),("map",["SOLUÇÃO","outro local","ou horário"])],
      "Prevalece a reunião anteriormente convocada para o mesmo local.", colors=colors("g","o","r","b")) +
 ex(p('Um sindicato avisa a prefeitura de que fará um ato na praça central no sábado às 10h. Outro grupo quer o mesmo local e horário. O segundo grupo não pode <b>frustrar</b> a reunião anteriormente convocada. O STF garantiu a realização de marchas pela descriminalização das drogas, por entender que defender a mudança de uma lei é exercício das liberdades de reunião e de expressão (ADPF 187).')) +
 pega('<ul><li>“Depende de <b>autorização</b> da autoridade” → <b>errado</b>: exige-se apenas <b>prévio aviso</b>.</li><li>Locais “abertos ao público”, e não “quaisquer locais”: reunião em local fechado e privado é outra situação.</li><li>A garantia da liberdade de reunião é o <b>mandado de segurança</b>, e não o <i>habeas corpus</i>, porque o direito protegido não é a locomoção em si.</li></ul>') +
 kw(["pacificamente","sem armas","locais abertos ao público","independentemente de autorização","prévio aviso","não frustrar outra reunião"]))

add(head(U3,T3,'Direito de <span class="hl">associação</span>','Unir-se de forma estável, com objetivos comuns.', "A13") +
 lei(cf("XVII a XXI"),'<p>XVII - é plena a liberdade de associação para fins lícitos, vedada a de caráter paramilitar;<br>XVIII - a criação de associações e, na forma da lei, a de cooperativas independem de autorização, sendo vedada a interferência estatal em seu funcionamento;<br>XIX - as associações só poderão ser compulsoriamente dissolvidas ou ter suas atividades suspensas por decisão judicial, exigindo-se, no primeiro caso, o trânsito em julgado;<br>XX - ninguém poderá ser compelido a associar-se ou a permanecer associado;<br>XXI - as entidades associativas, quando expressamente autorizadas, têm legitimidade para representar seus filiados judicial ou extrajudicialmente;</p>') +
 table(["","REUNIÃO (XVI)","ASSOCIAÇÃO (XVII)"],[["Duração","<b>Temporária</b> (um encontro)","<b>Permanente</b> (estável)"],["Requisito","Prévio aviso","Fins lícitos; não pode ser paramilitar"],["Exemplo","Passeata no domingo","Associação de moradores do bairro"]],["18%",None,None]) +
 memo('<strong>Suspender</strong> atividades: decisão judicial. <strong>Dissolver</strong>: decisão judicial <strong>transitada em julgado</strong>. Ninguém é obrigado a se associar <strong>nem a permanecer</strong> associado.'))

add(pratica_title() +
 flow([("handshake",["CRIAÇÃO","sem autorização","do Estado"]),("stop",["SUSPENSÃO","só por decisão","judicial"]),("gavel",["DISSOLUÇÃO","decisão judicial","+ trânsito em julgado"])],
      "Quanto mais grave a medida contra a associação, maior a exigência.", colors=colors("g","o","r")) +
 ex(p('O governador quer fechar uma associação de moradores que critica sua gestão. Ele <b>não pode</b>: a dissolução compulsória só ocorre por <b>decisão judicial transitada em julgado</b>, e é vedada a interferência estatal no funcionamento. Se a associação quiser defender seus filiados em juízo, precisa estar <b>expressamente autorizada</b> por eles (XXI).')) +
 pega('<ul><li>Suspensão: basta <b>decisão judicial</b>. Dissolução: decisão judicial <b>com trânsito em julgado</b>. A prova troca!</li><li><b>Representação</b> (XXI) exige autorização expressa dos filiados. Já no <b>mandado de segurança coletivo</b> (LXX, “b”) a entidade age em nome próprio e, pela Súmula 629 do STF, <b>independe da autorização</b> dos associados.</li><li>Vedada a associação de caráter <b>paramilitar</b>.</li></ul>') +
 kw(["fins lícitos","vedada a paramilitar","independem de autorização","dissolução: trânsito em julgado","suspensão: decisão judicial","expressamente autorizadas"]))

casa = f'''<figure><svg viewBox="0 0 640 230" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<rect x="10" y="10" width="300" height="210" rx="16" fill="{C['goldsoft']}" stroke="{C['golddeep']}" stroke-width="2.5"/>
<g transform="translate(26,22)" style="color:{C['golddeep']}"><use href="#i-sun" width="34" height="34"/></g>
<g transform="translate(66,22)" style="color:{C['navy']}"><use href="#i-moon" width="34" height="34"/></g>
<text x="190" y="45" text-anchor="middle" font-weight="900" font-size="14" fill="{C['golddeep']}">A QUALQUER HORA</text>
<text x="190" y="62" text-anchor="middle" font-size="11" fill="{C['ink']}">(dia ou noite)</text>
''' + "".join(f'<rect x="28" y="{80+i*34}" width="264" height="28" rx="8" fill="#fff" stroke="{C["golddeep"]}"/><text x="44" y="{99+i*34}" font-size="12.5" font-weight="700" fill="{C["ink"]}">{t}</text>' for i,t in enumerate(["✓  Consentimento do morador","✓  Flagrante delito","✓  Desastre","✓  Prestar socorro"])) + f'''
<rect x="330" y="10" width="300" height="210" rx="16" fill="{C['sky']}" stroke="{C['blue']}" stroke-width="2.5"/>
<g transform="translate(346,22)" style="color:{C['golddeep']}"><use href="#i-sun" width="34" height="34"/></g>
<text x="500" y="45" text-anchor="middle" font-weight="900" font-size="14" fill="{C['blue']}">SÓ DURANTE O DIA</text>
<text x="500" y="62" text-anchor="middle" font-size="11" fill="{C['ink']}">(nunca à noite)</text>
<rect x="348" y="80" width="264" height="28" rx="8" fill="#fff" stroke="{C['blue']}"/><text x="364" y="99" font-size="12.5" font-weight="700" fill="{C['ink']}">✓  Determinação judicial</text>
<text x="480" y="140" text-anchor="middle" font-size="11.5" fill="{C['ink']}">Lei de Abuso de Autoridade:</text>
<text x="480" y="157" text-anchor="middle" font-size="11.5" fill="{C['ink']}">é crime cumprir mandado de busca</text>
<text x="480" y="174" text-anchor="middle" font-size="11.5" fill="{C['ink']}">domiciliar <tspan font-weight="900">após as 21h ou antes das 5h</tspan></text>
<text x="480" y="191" text-anchor="middle" font-size="10.5" fill="{C['muted']}">(Lei nº 13.869/2019, art. 22, § 1º, III)</text>
</svg><figcaption>Inviolabilidade domiciliar: quatro exceções valem a qualquer hora; a ordem judicial, só de dia.</figcaption></figure>'''
add(head(U3,T3,'Inviolabilidade <span class="hl">domiciliar</span>','A casa é asilo inviolável, com exceções bem definidas.', "A14") +
 lei(cf("XI"),'<p>XI - a casa é asilo inviolável do indivíduo, ninguém nela podendo penetrar sem consentimento do morador, salvo em caso de flagrante delito ou desastre, ou para prestar socorro, ou, durante o dia, por determinação judicial;</p>') + casa +
 traduz(p('Ninguém entra na sua casa sem a sua permissão, nem a polícia. As exceções são poucas: <strong>flagrante</strong>, <strong>desastre</strong> e <strong>socorro</strong> permitem entrar a qualquer hora; a <strong>ordem judicial</strong> só pode ser cumprida <strong>durante o dia</strong>.')) +
 memo('<b>FDS a qualquer hora</b>: <strong>F</strong>lagrante, <strong>D</strong>esastre, <strong>S</strong>ocorro (+ consentimento). <strong>Ordem judicial: só de dia.</strong>', "Mnemônico:"))

add(pratica_title("O que é “casa”?") +
 flow([("house",["RESIDÊNCIA","casa ou","apartamento"]),("city",["QUARTO DE HOTEL","ocupado pelo","hóspede"]),("briefcase",["ESCRITÓRIO","parte não aberta","ao público"]),("map",["TRAILER OU","BARRACO","onde se mora"])],
      "O conceito de casa é amplo: qualquer compartimento habitado ou de uso profissional fechado ao público.", colors=colors("b","g","o","n")) +
 ex(p('Policiais recebem uma denúncia de tráfico e arrombam a porta de uma casa à noite, sem mandado. O STF fixou a tese de que a entrada forçada sem mandado, mesmo à noite, só é lícita quando amparada em <b>fundadas razões</b>, <b>justificadas depois</b> por escrito, que indiquem situação de <b>flagrante delito</b> dentro da casa, sob pena de responsabilização dos agentes e nulidade das provas (RE 603.616, Tema 280). Uma simples denúncia anônima, sem outros elementos, não basta.')) +
 pega('<ul><li>Ordem judicial à <b>noite</b> → <b>não pode</b> ser cumprida, mesmo com mandado.</li><li>Flagrante, desastre e socorro → <b>a qualquer hora</b>, sem mandado.</li><li>Escritório e consultório (na parte fechada ao público) também são “casa” para fins de proteção.</li><li>A CPI <b>não</b> pode determinar busca e apreensão domiciliar: é matéria de <b>reserva de jurisdição</b>.</li></ul>'))

add(head(U3,T3,'Sigilo das <span class="hl">comunicações</span>','Cartas, telegramas, dados e telefonemas são protegidos.', "A15") +
 lei(cf("XII"),'<p>XII - é inviolável o sigilo da correspondência e das comunicações telegráficas, de dados e das comunicações telefônicas, salvo, no último caso, por ordem judicial, nas hipóteses e na forma que a lei estabelecer para fins de investigação criminal ou instrução processual penal;</p>') +
 cards([("envelope","Correspondência","Cartas e encomendas.",C['blue']),("doc","Telegráficas","Telegramas.",C['golddeep']),("database","Dados","Informações armazenadas e transmitidas.",C['green']),("phone","Telefônicas","Exceção expressa: interceptação por ordem judicial.",C['red'])],2) +
 traduz(p('O texto protege quatro tipos de comunicação. A única exceção <strong>escrita</strong> na Constituição é a <strong>telefônica</strong> (“no último caso”): ela pode ser interceptada, mas só com <strong>ordem judicial</strong>, nas hipóteses da lei (Lei nº 9.296/1996) e para fins <strong>criminais</strong> (investigação ou processo penal).')) +
 memo('Interceptação telefônica: <strong>ordem judicial</strong> + <strong>hipóteses da lei</strong> + finalidade <strong>penal</strong> (investigação criminal ou instrução processual penal). Nunca para processo civil.'))

add(pratica_title() +
 flow([("phone",["TELEFONE","comunicação","protegida"]),("gavel",["ORDEM","JUDICIAL"]),("doc",["HIPÓTESES","DA LEI","Lei nº 9.296/96"]),("shield",["FIM","PENAL","investigação ou processo"])],
      "Os três requisitos da interceptação telefônica.", colors=colors("b","r","o","n")) +
 ex(p('Numa ação de divórcio, um dos cônjuges pede ao juiz da vara de família a interceptação do telefone do outro. O pedido deve ser negado: a interceptação só é permitida para fins de <b>investigação criminal ou instrução processual penal</b>. E uma <b>CPI</b> pode quebrar o sigilo <b>bancário, fiscal e de registros telefônicos</b> (a lista de chamadas), mas <b>não pode</b> determinar interceptação telefônica, que exige ordem judicial.')) +
 pega('<ul><li><b>Interceptação</b> (ouvir a conversa em tempo real) ≠ <b>quebra de sigilo telefônico</b> (acesso aos registros: números, datas, duração). A CPI pode a segunda, não a primeira.</li><li>Na literalidade, a exceção expressa é só a <b>telefônica</b>. Mesmo assim, o STF entende que nenhum sigilo é absoluto e já admitiu restrições excepcionais aos demais.</li><li>Finalidade <b>penal</b> sempre: nada de interceptação para processo civil, trabalhista ou administrativo.</li></ul>') +
 kw(["correspondência","telegráficas","dados","telefônicas","no último caso","ordem judicial","investigação criminal","Lei nº 9.296/1996"]))

add(head(U3,T3,'Direito de <span class="hl">petição</span>','Pedir ou reclamar ao Poder Público, sem pagar nada.', "A16") +
 lei(cf("XXXIV"),'<p>XXXIV - são a todos assegurados, independentemente do pagamento de taxas:<br>a) o direito de petição aos Poderes Públicos em defesa de direitos ou contra ilegalidade ou abuso de poder;<br>b) a obtenção de certidões em repartições públicas, para defesa de direitos e esclarecimento de situações de interesse pessoal;</p>') +
 traduz(p('Qualquer pessoa, física ou jurídica, brasileira ou estrangeira, pode <strong>pedir</strong>, <strong>reclamar</strong> ou <strong>denunciar</strong> ao Poder Público, por escrito, <strong>sem pagar taxa</strong> e <strong>sem precisar de advogado</strong>. Também pode obter <strong>certidões</strong> para defender direitos ou esclarecer situações de interesse pessoal.')) +
 table(["","DIREITO DE PETIÇÃO (XXXIV, “a”)","DIREITO DE AÇÃO (XXXV)"],[["A quem se dirige","Aos <b>Poderes Públicos</b> (via administrativa)","Ao <b>Poder Judiciário</b>"],["Advogado","Não precisa","Em regra, precisa"],["Custo","Independe de taxas","Pode haver custas judiciais"]],["22%",None,None]) +
 pega('<ul><li>Certidão <b>negada</b> pela repartição → o remédio é o <b>mandado de segurança</b>, e não o <i>habeas data</i>. O HD serve para informações sobre a <b>própria pessoa</b> em bancos de dados.</li><li>O direito de petição <b>independe do pagamento de taxas</b>: cobrar taxa para protocolar uma reclamação é inconstitucional.</li><li>Petição ≠ ação judicial: a petição não exige advogado, porque não é processo judicial.</li></ul>'))

treino(3, [
 ("A Administração Pública pode fazer tudo o que a lei não proíbe.","E","Essa é a regra do particular; a Administração só faz o que a lei permite."),
 ("É livre a manifestação do pensamento, sendo vedado o anonimato.","C","Art. 5º, IV."),
 ("O direito de reunião depende de prévia autorização da autoridade competente.","E","Exige apenas prévio aviso."),
 ("As associações só podem ser compulsoriamente dissolvidas por decisão judicial transitada em julgado.","C","Art. 5º, XIX."),
 ("Com ordem judicial, a polícia pode entrar na casa durante a noite para cumprir mandado de busca.","E","A ordem judicial só pode ser cumprida durante o dia."),
 ("A interceptação telefônica pode ser autorizada pelo juiz em processo civil de divórcio.","E","Só para investigação criminal ou instrução processual penal.")])

# =========================================================== UNIDADE 4
opener("04","UNIDADE 4","Remédios e garantias processuais",["Qual remédio usar? (árvore de decisão)","Habeas corpus","Habeas data","Mandado de segurança","Mandado de injunção","Ação popular","Quadro comparativo","Devido processo legal","Contraditório e ampla defesa"],"U4")

arvore = f'''<figure><svg viewBox="0 0 640 520" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<defs><marker id="ta" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L10,5 L0,10 z" fill="{C['ink']}"/></marker></defs>
''' + "".join(
 f'<rect x="20" y="{y}" width="360" height="54" rx="12" fill="#fff" stroke="{C["navy"]}" stroke-width="2.5"/><text x="200" y="{y+23}" text-anchor="middle" font-weight="800" font-size="13" fill="{C["navy"]}">{q1}</text><text x="200" y="{y+41}" text-anchor="middle" font-size="12" fill="{C["ink"]}">{q2}</text>'
 f'<line x1="380" y1="{y+27}" x2="438" y2="{y+27}" stroke="{C["green"]}" stroke-width="3" marker-end="url(#ta)"/><text x="408" y="{y+20}" text-anchor="middle" font-weight="900" font-size="11" fill="{C["green"]}">SIM</text>'
 f'<rect x="444" y="{y+2}" width="186" height="50" rx="12" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="537" y="{y+25}" text-anchor="middle" font-weight="900" font-size="{12 if len(r1)>16 else 14}" fill="{fg}">{r1}</text><text x="537" y="{y+42}" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">{r2}</text>'
 + (f'<line x1="200" y1="{y+54}" x2="200" y2="{y+78}" stroke="{C["red"]}" stroke-width="3" marker-end="url(#ta)"/><text x="218" y="{y+70}" font-weight="900" font-size="11" fill="{C["red"]}">NÃO</text>' if last is False else '')
 for y,q1,q2,r1,r2,fg,bg,last in [
  (10,"A liberdade de locomoção (ir e vir)","foi violada ou ameaçada?","HABEAS CORPUS","LXVIII · gratuito",C['red'],C['redsoft'],False),
  (92,"Quero conhecer ou corrigir informações","SOBRE MIM em banco de dados público?","HABEAS DATA","LXXII · gratuito",C['golddeep'],C['goldsoft'],False),
  (174,"Falta uma lei regulamentadora que","impede exercer um direito constitucional?","MANDADO DE INJUNÇÃO","LXXI",C['green'],C['greensoft'],False),
  (256,"Sou cidadão e quero anular ato lesivo ao","patrimônio público, moralidade, meio ambiente...?","AÇÃO POPULAR","LXXIII",C['navy'],'#e3e9f3',False),
  (338,"Tenho direito líquido e certo violado","por autoridade (e nenhum caso acima)?","MANDADO DE SEGURANÇA","LXIX · residual",C['blue'],C['sky'],True)]) + f'''
<rect x="20" y="420" width="610" height="88" rx="14" fill="#f4f6fa" stroke="{C['sky2']}" stroke-width="2"/>
<text x="325" y="446" text-anchor="middle" font-weight="900" font-size="13" fill="{C['navy']}">Por que o mandado de segurança fica por último?</text>
<text x="325" y="468" text-anchor="middle" font-size="12" fill="{C['ink']}">Porque ele é RESIDUAL: protege direito líquido e certo “não amparado</text>
<text x="325" y="486" text-anchor="middle" font-size="12" fill="{C['ink']}">por habeas corpus ou habeas data”. Primeiro elimine HC e HD.</text>
</svg><figcaption>Árvore de decisão: responda às perguntas de cima para baixo.</figcaption></figure>'''
add(head(U4,T4,'Qual <span class="hl">remédio</span> usar?','A árvore de decisão que resolve a maioria das questões sobre remédios.', "A17") + arvore)

add(head(U4,T4,'<span class="hl">Habeas corpus</span>','A garantia da liberdade de ir e vir.', "A18") +
 lei(cf("LXVIII e LXXVII"),'<p>LXVIII - conceder-se-á "habeas-corpus" sempre que alguém sofrer ou se achar ameaçado de sofrer violência ou coação em sua liberdade de locomoção, por ilegalidade ou abuso de poder;<br>LXXVII - são gratuitas as ações de "habeas-corpus" e "habeas-data", e, na forma da lei, os atos necessários ao exercício da cidadania.</p>','Grafia oficial com hífen, como no texto do Planalto.') +
 traduz(p('<i>Habeas corpus</i> significa, em latim, algo como “que tenhas o corpo”. É a ação que protege a <strong>liberdade de locomoção</strong>. Pode ser <strong>preventivo</strong> (quando há ameaça de prisão ilegal: o juiz dá um <strong>salvo-conduto</strong>) ou <strong>repressivo</strong> (quando a prisão já aconteceu: o juiz manda soltar, com um <strong>alvará de soltura</strong>). É <strong>gratuito</strong> e dispensa advogado.')) +
 table(["Quem","Quem é"],[["Impetrante","Quem pede: <b>qualquer pessoa</b>, física ou jurídica, sem advogado, até analfabeta ou estrangeira"],["Paciente","Quem sofre a coação: sempre <b>pessoa física</b>"],["Autoridade coatora","Quem pratica a ilegalidade: autoridade pública ou até um particular (ex.: hospital que retém paciente)"]],["24%",None]) +
 memo('HC: <strong>locomoção</strong> · <strong>gratuito</strong> · <strong>sem advogado</strong> · <strong>qualquer pessoa</strong> impetra · paciente é <strong>pessoa física</strong> · preventivo ou repressivo.'))

add(pratica_title() +
 flow([("alert",["AMEAÇA","de prisão","ilegal"]),("shield",["HC","PREVENTIVO","salvo-conduto"]),("jail",["PRISÃO","ilegal já","ocorreu"]),("unlock",["HC","REPRESSIVO","alvará de soltura"])],
      "As duas modalidades do habeas corpus.", colors=colors("o","g","r","b")) +
 ex(p('Uma clínica particular impede a saída de um paciente que recebeu alta até que a família pague a conta. A irmã do paciente, sem advogado, impetra <i>habeas corpus</i> em favor dele. A coação à liberdade de locomoção pode partir até de um <b>particular</b>.')) +
 pega('<ul><li>Não cabe HC em relação a <b>punições disciplinares militares</b> (art. 142, § 2º). Segundo o STF, é possível discutir apenas a <b>legalidade</b> da punição (competência, cerimonial), e não o mérito.</li><li>Pessoa jurídica pode ser <b>impetrante</b>, mas não <b>paciente</b>.</li><li>Não cabe HC quando o direito em jogo não é a locomoção: por exemplo, contra pena exclusivamente de multa ou para discutir perda de cargo.</li></ul>') +
 kw(["liberdade de locomoção","preventivo / repressivo","salvo-conduto","alvará de soltura","gratuito","sem advogado","paciente = pessoa física"]))

add(head(U4,T4,'<span class="hl">Habeas data</span>','Para conhecer e corrigir informações sobre você mesmo.', "A19") +
 lei(cf("LXXII"),'<p>LXXII - conceder-se-á "habeas-data":<br>a) para assegurar o conhecimento de informações relativas à pessoa do impetrante, constantes de registros ou bancos de dados de entidades governamentais ou de caráter público;<br>b) para a retificação de dados, quando não se prefira fazê-lo por processo sigiloso, judicial ou administrativo;</p>') +
 traduz(p('<i>Habeas data</i> é a ação para <strong>conhecer</strong> e <strong>corrigir</strong> informações <strong>sobre a sua própria pessoa</strong> guardadas em bancos de dados do governo ou de caráter público, como um cadastro de proteção ao crédito. A Lei nº 9.507/1997 acrescentou uma terceira finalidade: <strong>anotar</strong> uma explicação ou contestação nos registros.')) +
 cards([("eye","Conhecer","Saber o que há sobre você.",C['blue']),("pen","Retificar","Corrigir dados errados.",C['golddeep']),("doc","Anotar","Incluir explicação ou contestação (Lei nº 9.507/97).",C['green'])],3) +
 memo('HD: informações <strong>da própria pessoa</strong> · <strong>gratuito</strong> · <strong>exige advogado</strong> · precisa de <strong>recusa administrativa prévia</strong>.'))

add(pratica_title() +
 flow([("doc",["PEDIDO","ADMINISTRATIVO","ao órgão"]),("hourglass",["RECUSA OU","SILÊNCIO","10 dias (acesso)","15 dias (retificar)"]),("gavel",["HABEAS","DATA","com advogado"])],
      "Antes do HD é preciso tentar a via administrativa (Lei nº 9.507/97, art. 8º, parágrafo único).", colors=colors("b","o","g")) +
 ex(p('Carla descobre que seu nome consta como “devedora” num cadastro de caráter público, por um erro. Primeiro ela pede a correção ao órgão. Se ele recusar, ou ficar mais de 15 dias sem decidir, ela pode impetrar <i>habeas data</i>. Sem esse pedido prévio, falta interesse de agir: pela Súmula 2 do STJ, não cabe HD se não houve recusa de informações pela autoridade administrativa.')) +
 pega('<ul><li>HD protege informações <b>da própria pessoa</b>. Para informações de terceiros ou de interesse geral, o caminho é outro (por exemplo, MS ou a Lei de Acesso à Informação).</li><li>Certidão negada → <b>mandado de segurança</b>, e não HD.</li><li>HD é <b>gratuito</b> (LXXVII), mas, diferentemente do HC, <b>exige advogado</b>.</li></ul>') +
 kw(["informações relativas à pessoa do impetrante","entidades governamentais ou de caráter público","retificação","recusa prévia","Súmula 2 do STJ","gratuito"]))

add(head(U4,T4,'Mandado de <span class="hl">segurança</span>','O remédio “coringa”: protege o direito líquido e certo.', "A20") +
 lei(cf("LXIX e LXX"),'<p>LXIX - conceder-se-á mandado de segurança para proteger direito líquido e certo, não amparado por "habeas-corpus" ou "habeas-data", quando o responsável pela ilegalidade ou abuso de poder for autoridade pública ou agente de pessoa jurídica no exercício de atribuições do Poder Público;<br>LXX - o mandado de segurança coletivo pode ser impetrado por: a) partido político com representação no Congresso Nacional; b) organização sindical, entidade de classe ou associação legalmente constituída e em funcionamento há pelo menos um ano, em defesa dos interesses de seus membros ou associados;</p>') +
 traduz(p('<strong>Direito líquido e certo</strong> é aquele que você consegue provar <strong>de imediato, com documentos</strong>, sem precisar de testemunhas ou perícia. O MS é <strong>residual</strong>: só cabe quando o caso não é de HC nem de HD. O prazo é de <strong>120 dias</strong> contados da ciência do ato (Lei nº 12.016/2009, art. 23).')) +
 memo('MS: direito <strong>líquido e certo</strong> (prova documental pré-constituída) · <strong>residual</strong> · prazo de <strong>120 dias</strong> · contra <strong>autoridade pública</strong> ou agente no exercício de atribuições do Poder Público.'))

add(pratica_title() +
 flow([("doc",["PROVA","documental","pronta"]),("alert",["ATO ILEGAL","de autoridade"]),("hourglass",["ATÉ 120 DIAS","da ciência","do ato"]),("shield",["MANDADO DE","SEGURANÇA"])],
      "Os requisitos do mandado de segurança.", colors=colors("g","r","o","b")) +
 ex(p('Lucas foi aprovado em 1º lugar num concurso, mas a Administração nomeou o 3º colocado no lugar dele. Com o edital, o resultado e o ato de nomeação em mãos (<b>prova documental</b>), ele impetra mandado de segurança dentro de 120 dias. Se dependesse de ouvir testemunhas, o MS não seria o caminho.')) +
 pega('<ul><li><b>MS coletivo</b>: partido político <b>com representação no Congresso Nacional</b>; organização sindical, entidade de classe ou associação em funcionamento há <b>pelo menos um ano</b>. Pela Súmula 629 do STF, a impetração <b>independe da autorização</b> dos associados.</li><li>Não cabe MS contra <b>lei em tese</b> (Súmula 266 do STF), e o MS <b>não substitui ação de cobrança</b> (Súmula 269 do STF).</li><li>O prazo de 120 dias é <b>decadencial</b>: perdido o prazo, ainda é possível ir às vias ordinárias, mas não ao MS.</li></ul>') +
 kw(["direito líquido e certo","residual","120 dias","autoridade pública","MS coletivo","partido com representação no CN","1 ano"]))

add(head(U4,T4,'Mandado de <span class="hl">injunção</span>','Quando falta a lei que permitiria exercer o seu direito.', "A21") +
 lei(cf("LXXI"),'<p>LXXI - conceder-se-á mandado de injunção sempre que a falta de norma regulamentadora torne inviável o exercício dos direitos e liberdades constitucionais e das prerrogativas inerentes à nacionalidade, à soberania e à cidadania;</p>') +
 traduz(p('Às vezes a Constituição promete um direito, mas diz que ele será exercido “<strong>na forma da lei</strong>”, e essa lei nunca é feita. O mandado de injunção combate essa <strong>omissão</strong>. Hoje ele é regulado pela <strong>Lei nº 13.300/2016</strong>, que permite ao Judiciário fixar um prazo para o legislador e, se a omissão continuar, <strong>estabelecer as condições</strong> para o exercício do direito.')) +
 memo('MI = <strong>falta de norma regulamentadora</strong> que torna <strong>inviável</strong> exercer direito constitucional. Lei nº 13.300/2016. Posição <strong>concretista</strong>: o Judiciário viabiliza o exercício do direito.'))

add(pratica_title() +
 flow([("doc",["CF PROMETE","direito “na","forma da lei”"]),("puzzlex",["FALTA","A LEI","omissão"]),("gavel",["MANDADO DE","INJUNÇÃO"]),("check",["JUDICIÁRIO","fixa prazo e as","condições de exercício"])],
      "O mandado de injunção combate a omissão legislativa.", colors=colors("b","r","o","g")) +
 ex(p('A CF garante o direito de greve aos servidores públicos “nos termos e nos limites definidos em lei específica” (art. 37, VII), mas essa lei não foi editada por muitos anos. Ao julgar mandados de injunção (MI 670, 708 e 712), o STF determinou a aplicação, no que coubesse, da lei de greve do setor privado aos servidores, até que o Congresso edite a lei própria.')) +
 pega('<ul><li>MI ≠ ADO (ação direta de inconstitucionalidade por omissão): o MI pode ser proposto por <b>qualquer pessoa</b> prejudicada, para o <b>caso concreto</b>; a ADO tem legitimados restritos (art. 103) e controle abstrato.</li><li><b>MI coletivo</b> (Lei nº 13.300/2016, art. 12): Ministério Público, partido político com representação no Congresso, organização sindical, entidade de classe ou associação há pelo menos 1 ano, e Defensoria Pública.</li><li>Só cabe MI se a falta de norma tornar o exercício <b>inviável</b>, e não apenas mais difícil.</li></ul>') +
 kw(["falta de norma regulamentadora","inviável","omissão","Lei nº 13.300/2016","concretista","MI coletivo"]))

add(head(U4,T4,'Ação <span class="hl">popular</span>','O cidadão como fiscal do patrimônio público.', "A22") +
 lei(cf("LXXIII"),'<p>LXXIII - qualquer cidadão é parte legítima para propor ação popular que vise a anular ato lesivo ao patrimônio público ou de entidade de que o Estado participe, à moralidade administrativa, ao meio ambiente e ao patrimônio histórico e cultural, ficando o autor, salvo comprovada má-fé, isento de custas judiciais e do ônus da sucumbência;</p>') +
 traduz(p('A ação popular permite que <strong>qualquer cidadão</strong> (pessoa com <strong>título de eleitor</strong>, em dia com a Justiça Eleitoral) vá à Justiça para <strong>anular atos lesivos</strong> ao que é de todos: dinheiro público, moralidade, meio ambiente e patrimônio histórico e cultural. Para não intimidar o cidadão, ele fica <strong>isento de custas</strong> e de honorários de sucumbência, salvo se agir com <strong>má-fé comprovada</strong>. É regulada pela Lei nº 4.717/1965.')) +
 cards([("coin","Patrimônio público","Inclui entidades de que o Estado participe.",C['golddeep']),("scales","Moralidade administrativa","Mesmo sem prejuízo financeiro.",C['blue']),("tree","Meio ambiente","Bem de toda a coletividade.",C['green']),("capitol","Patrimônio histórico e cultural","Prédios, monumentos, tradições.",C['red'])],2) +
 memo('Ação popular: <strong>cidadão</strong> (eleitor) · anula ato lesivo a <strong>patrimônio público, moralidade, meio ambiente e patrimônio histórico-cultural</strong> · isento de custas <strong>salvo má-fé</strong>.'))

add(pratica_title() +
 flow([("idcard",["CIDADÃO","prova com o","título de eleitor"]),("alert",["ATO LESIVO","ex.: contrato","superfaturado"]),("gavel",["AÇÃO","POPULAR","Lei nº 4.717/65"]),("check",["ANULAÇÃO","+ ressarcimento","dos danos"])],
      "Da cidadania à anulação do ato lesivo.", colors=colors("b","r","o","g")) +
 ex(p('Rita, eleitora de Parnaíba, descobre que a prefeitura contratou, sem licitação e por preço muito acima do mercado, uma empresa do cunhado do prefeito. Ela pode propor <b>ação popular</b> para anular o contrato. Se perder a ação, não pagará custas nem honorários, a menos que se prove que agiu de <b>má-fé</b>.')) +
 pega('<ul><li><b>Pessoa jurídica não pode</b> propor ação popular (Súmula 365 do STF). O <b>Ministério Público</b> também não a propõe: ele pode assumir a ação se o autor desistir, e tem a ação civil pública como instrumento próprio.</li><li>Estrangeiro, mesmo residente, <b>não</b> propõe ação popular, porque não é cidadão (eleitor). Exceção discutida: o português equiparado (art. 12, § 1º).</li><li>A lesão à <b>moralidade</b> basta, mesmo sem prejuízo financeiro.</li></ul>') +
 kw(["qualquer cidadão","título de eleitor","ato lesivo","moralidade administrativa","isento de custas","salvo comprovada má-fé","Súmula 365"]))

add(head(U4,T4,'Quadro comparativo dos <span class="hl">remédios</span>','A página para revisar na véspera da prova.', "A23") +
 table(["","HC","HD","MS","MI","AÇÃO POPULAR"],[
  ["Protege","Liberdade de locomoção","Informações da própria pessoa","Direito líquido e certo (residual)","Direito inviável por falta de norma","Patrimônio público, moralidade, meio ambiente, patrimônio histórico-cultural"],
  ["Quem propõe","Qualquer pessoa","A pessoa titular dos dados","Titular do direito (pessoa física ou jurídica)","Titular do direito inviabilizado","Cidadão (eleitor)"],
  ["Advogado","<span class='no'>Não precisa</span>","Precisa","Precisa","Precisa","Precisa"],
  ["Custo","<span class='yes'>Gratuito</span>","<span class='yes'>Gratuito</span>","Há custas","Há custas","Isento, salvo má-fé"],
  ["Inciso","LXVIII","LXXII","LXIX e LXX","LXXI","LXXIII"],
  ["Lei","CPP","9.507/1997","12.016/2009","13.300/2016","4.717/1965"],
  ["Destaque","Preventivo ou repressivo","Exige recusa prévia","Prazo de 120 dias","Concretista","Lesão à moralidade basta"]],["15%","14%","15%","16%","16%",None]) +
 memo('<b>Gratuitos: só HC e HD</b> (LXXVII). <b>Sem advogado: só HC.</b> <b>Coletivos previstos:</b> MS (na CF) e MI (na Lei nº 13.300/2016).', "Atenção:") +
 pega('<ul><li>“Todos os remédios constitucionais são gratuitos.” → <b>errado</b>: só HC e HD. A ação popular tem isenção de custas para o autor, salvo má-fé, o que é diferente de gratuidade geral.</li><li>“O habeas data dispensa advogado, como o habeas corpus.” → <b>errado</b>.</li><li>Locomoção → HC. Dados pessoais → HD. Certidão negada → MS.</li></ul>'))

add(head(U4,T4,'Devido processo <span class="hl">legal</span>','Ninguém perde liberdade ou bens sem um processo justo.', "A24") +
 lei(cf("LIV, LVI e LXXVIII"),'<p>LIV - ninguém será privado da liberdade ou de seus bens sem o devido processo legal;<br>LVI - são inadmissíveis, no processo, as provas obtidas por meios ilícitos;<br>LXXVIII - a todos, no âmbito judicial e administrativo, são assegurados a razoável duração do processo e os meios que garantam a celeridade de sua tramitação.</p>','LXXVIII incluído pela EC nº 45/2004.') +
 cards([("doc","Sentido FORMAL (processual)","Seguir as regras do processo: juiz competente, citação, prazos, defesa e recurso.",C['blue']),
        ("scales","Sentido MATERIAL (substancial)","A decisão deve ser justa, <b>razoável e proporcional</b>, e não apenas formalmente correta.",C['golddeep'])],2) +
 traduz(p('O devido processo legal é a “regra do jogo limpo”. Antes de tirar a liberdade ou os bens de alguém, o Estado precisa seguir um <strong>caminho previsto em lei</strong>, com juiz imparcial, direito de defesa e decisão fundamentada. Dele derivam várias outras garantias, como o contraditório, a ampla defesa e a proibição de provas ilícitas.')) +
 memo('Devido processo legal = <strong>princípio-mãe</strong> das garantias processuais. Sentidos <strong>formal</strong> e <strong>material</strong> (razoabilidade e proporcionalidade). Provas ilícitas: <strong>inadmissíveis</strong>.'))

add(pratica_title() +
 flow([("doc",["ACUSAÇÃO","formal"]),("person",["CITAÇÃO","ciência do","acusado"]),("megaphone",["DEFESA","e produção","de provas"]),("gavel",["DECISÃO","fundamentada","e recorrível"])],
      "As etapas mínimas de um devido processo.", colors=colors("n","b","o","g")) +
 ex(p('A polícia obtém uma confissão mediante tortura e encontra drogas a partir dessa confissão. A confissão é <b>prova ilícita</b> e inadmissível (LVI). Pela teoria dos <b>frutos da árvore envenenada</b>, também são ilícitas as provas derivadas dela, salvo quando não houver nexo de causalidade ou quando puderem ser obtidas por fonte independente (art. 157, § 1º, do CPP).')) +
 pega('<ul><li>O devido processo legal vale para privar alguém da <b>liberdade</b> ou de seus <b>bens</b>, ou seja, também em processos administrativos e civis, e não só no processo penal.</li><li>A razoável duração do processo (LXXVIII) vale no âmbito <b>judicial e administrativo</b>.</li><li>Provas ilícitas são inadmissíveis <b>no processo</b>; a doutrina e a jurisprudência admitem, excepcionalmente, a prova ilícita usada <b>em favor do réu</b> para provar sua inocência.</li></ul>') +
 kw(["devido processo legal","sentido formal","sentido material","provas ilícitas","frutos da árvore envenenada","razoável duração do processo"]))

add(head(U4,T4,'Contraditório e <span class="hl">ampla defesa</span>','Ser ouvido e poder se defender, inclusive em processos administrativos.', "A25") +
 lei(cf("LV"),'<p>LV - aos litigantes, em processo judicial ou administrativo, e aos acusados em geral são assegurados o contraditório e ampla defesa, com os meios e recursos a ela inerentes;</p>') +
 cards([("megaphone","CONTRADITÓRIO","<b>Ciência + reação</b>: saber o que foi alegado contra você e poder responder.",C['blue']),
        ("shield","AMPLA DEFESA","Usar todos os meios lícitos de defesa: <b>defesa técnica</b> (advogado) e <b>autodefesa</b>, provas e recursos.",C['green'])],2) +
 traduz(p('<strong>Contraditório</strong> é o direito de <strong>saber</strong> e de <strong>responder</strong>: se a outra parte juntou um documento, você deve ser informado e poder se manifestar. <strong>Ampla defesa</strong> é poder se defender com <strong>todos os meios</strong> admitidos: advogado, testemunhas, documentos, perícias e recursos. Valem no processo <strong>judicial</strong> e no <strong>administrativo</strong>.')) +
 memo('Contraditório = <strong>informação + reação</strong>. Ampla defesa = <strong>defesa técnica + autodefesa</strong>. Valem no processo <strong>judicial e administrativo</strong>.'))

add(pratica_title() +
 flow([("doc",["PROCESSO","ADMINISTRATIVO","disciplinar"]),("person",["SERVIDOR","é notificado"]),("megaphone",["APRESENTA","DEFESA","com ou sem advogado"]),("gavel",["DECISÃO","da autoridade"])],
      "Contraditório e ampla defesa também valem no processo administrativo.", colors=colors("n","b","o","g")) +
 ex(p('Um guarda municipal responde a processo administrativo disciplinar por faltas ao serviço. Ele tem direito de ser notificado, apresentar defesa, produzir provas e recorrer. Se não constituir advogado, o processo não é nulo só por isso: pela Súmula Vinculante 5, a falta de defesa técnica por advogado no PAD não ofende a Constituição.')) +
 pega('<ul><li><b>Súmula Vinculante 5</b>: a falta de advogado no processo administrativo disciplinar <b>não</b> ofende a CF. No processo <b>penal</b>, porém, a defesa técnica é obrigatória.</li><li><b>Inquérito policial</b>: para a doutrina majoritária, é procedimento inquisitivo, sem contraditório pleno. Mas a <b>Súmula Vinculante 14</b> garante ao defensor acesso amplo aos elementos de prova <b>já documentados</b> que digam respeito ao direito de defesa.</li><li>LV menciona “litigantes” e “acusados em geral”, em processo <b>judicial ou administrativo</b>.</li></ul>') +
 kw(["contraditório","ampla defesa","processo judicial ou administrativo","defesa técnica","autodefesa","SV 5","SV 14"]))

treino(4, [
 ("O habeas corpus pode ser impetrado por qualquer pessoa, independentemente de advogado.","C","É a regra do HC, que dispensa capacidade postulatória."),
 ("O mandado de segurança é cabível para proteger a liberdade de locomoção.","E","É residual: não cabe quando o caso é de HC ou HD."),
 ("O habeas data é gratuito e dispensa advogado.","E","É gratuito, mas exige advogado."),
 ("Pessoa jurídica tem legitimidade para propor ação popular.","E","Súmula 365 do STF: não tem."),
 ("O mandado de injunção é cabível quando a falta de norma regulamentadora torna inviável o exercício de direitos constitucionais.","C","Art. 5º, LXXI."),
 ("O contraditório e a ampla defesa são assegurados somente no processo judicial.","E","Também no processo administrativo (LV).")])

# =========================================================== REVISÃO
mapa = f'''<figure><svg viewBox="0 0 640 470" width="580" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<g stroke="#9fb1cc" stroke-width="2.5" fill="none"><path d="M320 235 L150 70"/><path d="M320 235 L490 70"/><path d="M320 235 L120 235"/><path d="M320 235 L520 235"/><path d="M320 235 L150 400"/><path d="M320 235 L490 400"/></g>
<circle cx="320" cy="235" r="74" fill="{C['navy']}"/><text x="320" y="225" text-anchor="middle" fill="{C['gold']}" font-weight="900" font-size="13">ART. 5º</text>
<text x="320" y="245" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">DIREITOS E</text><text x="320" y="262" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">GARANTIAS</text>
''' + "".join(
 f'<rect x="{x-100}" y="{y-40}" width="200" height="80" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x}" y="{y-16}" text-anchor="middle" font-weight="900" font-size="12.5" fill="{fg}">{t}</text>'
 + "".join(f'<text x="{x}" y="{y+4+i*15}" text-anchor="middle" font-size="10.8" fill="{C["ink"]}">{l}</text>' for i,l in enumerate(ls))
 for x,y,t,ls,fg,bg in [
  (150,62,"TEORIA",["direito declara, garantia protege","HUIIR · rol exemplificativo","aplicação imediata"],C['navy'],'#e3e9f3'),
  (490,62,"CAPUT",["vida · liberdade · igualdade","segurança · propriedade","DAC · requisição ≠ desapropriação"],C['blue'],C['sky']),
  (112,235,"LIBERDADES",["expressão: sem anonimato","religião: escusa","reunião: aviso, não autorização"],C['golddeep'],C['goldsoft']),
  (528,235,"PROTEÇÕES",["casa: FDS qualquer hora,","ordem judicial só de dia","telefone: juiz + fim penal"],C['red'],C['redsoft']),
  (150,408,"REMÉDIOS",["HC locomoção · HD dados","MS residual 120 dias","MI omissão · AP cidadão"],C['green'],C['greensoft']),
  (490,408,"PROCESSO",["devido processo legal","contraditório + ampla defesa","SV 5 · SV 14 · provas ilícitas"],C['navy'],'#e3e9f3')]) + '</svg><figcaption>Mapa conceitual do Caderno 02.</figcaption></figure>'
add('<div class="marker">§§R1§§</div><div class="unit"><span class="u">REVISÃO</span><span class="t">Véspera da prova</span></div><h1 class="big">Mapa <span class="hl">conceitual</span></h1><p class="lead">O art. 5º em seis blocos. Explique cada caixa em voz alta.</p>' + mapa)

add('<div class="unit"><span class="u">REVISÃO</span><span class="t">Pontos de confusão</span></div><h1 class="big">As 12 confusões <span class="hl">mais comuns</span></h1><p class="lead">Os pares de conceitos que mais derrubam candidatos neste tema.</p>' +
 table(["Confusão","O certo é"],[
  ["Direito x garantia","Direito <b>declara</b>; garantia <b>assegura</b>."],
  ["Reunião: autorização x aviso","Basta <b>prévio aviso</b>; autorização não é exigida."],
  ["Associação: suspensão x dissolução","Suspensão: decisão judicial. Dissolução: decisão judicial <b>transitada em julgado</b>."],
  ["Casa: ordem judicial à noite","<b>Não pode</b>. Flagrante, desastre e socorro: a qualquer hora."],
  ["Interceptação x quebra de sigilo","Interceptação: só juiz, fim penal. Registros telefônicos: a CPI pode."],
  ["Desapropriação x requisição","Desapropriação: prévia e em dinheiro. Requisição: <b>ulterior, se houver dano</b>."],
  ["Legalidade do particular x Administração","Particular: tudo o que a lei não proíbe. Administração: só o que a lei permite."],
  ["Certidão negada: HD ou MS?","<b>MS</b>. O HD é para dados da própria pessoa."],
  ["Remédios gratuitos","Só <b>HC e HD</b>."],
  ["Advogado nos remédios","Só o <b>HC</b> dispensa advogado."],
  ["Ação popular: quem propõe","<b>Cidadão (eleitor)</b>. Não: pessoa jurídica, MP ou estrangeiro."],
  ["PAD sem advogado","<b>Válido</b> (SV 5). No processo penal, a defesa técnica é obrigatória."]],["36%",None]))

FC = [("TEORIA","Diferença entre direito e garantia?","Direito declara o bem; garantia é o instrumento que o assegura."),
 ("TEORIA","O rol do art. 5º é taxativo?","Não. É exemplificativo (§ 2º)."),
 ("CARACTERÍSTICAS","Mnemônico das características?","HUIIR: históricos, universais, inalienáveis, imprescritíveis, irrenunciáveis, relativos."),
 ("IGUALDADE","Formal x material?","Formal: perante a lei. Material: tratar desigualmente os desiguais para reduzir desigualdades."),
 ("VIDA","Quando cabe pena de morte?","Só em caso de guerra declarada (art. 84, XIX)."),
 ("SEGURANÇA","O que a lei nova não pode prejudicar?","Direito adquirido, ato jurídico perfeito e coisa julgada (DAC)."),
 ("PROPRIEDADE","Indenização na requisição?","Ulterior e só se houver dano."),
 ("LEGALIDADE","Regra para o particular?","Pode fazer tudo o que a lei não proíbe."),
 ("EXPRESSÃO","O que é vedado na manifestação do pensamento?","O anonimato."),
 ("RELIGIÃO","Quando há privação de direitos por crença?","Quando a pessoa recusa a obrigação geral e também a prestação alternativa."),
 ("REUNIÃO","O que se exige para a reunião?","Prévio aviso à autoridade; não é preciso autorização."),
 ("ASSOCIAÇÃO","Dissolução compulsória exige?","Decisão judicial transitada em julgado."),
 ("CASA","Quais exceções valem a qualquer hora?","Consentimento, flagrante, desastre e socorro."),
 ("CASA","Ordem judicial pode ser cumprida à noite?","Não. Só durante o dia."),
 ("SIGILO","Requisitos da interceptação telefônica?","Ordem judicial, hipóteses da lei e fim penal (investigação ou instrução)."),
 ("PETIÇÃO","Certidão negada: qual remédio?","Mandado de segurança."),
 ("HC","Quem pode impetrar HC?","Qualquer pessoa, física ou jurídica, sem advogado."),
 ("HD","Requisito prévio do HD?","Recusa ou demora da autoridade administrativa (Súmula 2 do STJ)."),
 ("MS","Prazo do mandado de segurança?","120 dias da ciência do ato (Lei nº 12.016/2009, art. 23)."),
 ("MS","Legitimados do MS coletivo?","Partido com representação no CN; sindicato, entidade de classe ou associação há pelo menos 1 ano."),
 ("MI","Quando cabe mandado de injunção?","Falta de norma regulamentadora que torne inviável exercer direito constitucional."),
 ("AÇÃO POPULAR","Pessoa jurídica pode propor?","Não (Súmula 365 do STF)."),
 ("PROCESSO","Sentidos do devido processo legal?","Formal (procedimento) e material (razoabilidade e proporcionalidade)."),
 ("PROCESSO","Falta de advogado no PAD é nula?","Não (Súmula Vinculante 5).")]
def fcpage(items, first):
    cs = "".join(f'<div class="c"><div class="f"><small>{a}</small>{q}</div><div class="b">{r}</div></div>' for a,q,r in items)
    h = ('<div class="marker">§§R2§§</div><div class="unit"><span class="u">REVISÃO ATIVA</span></div><h1 class="big">Flash<span class="hl">cards</span></h1><p class="lead">Cubra a resposta, tente lembrar e confira. Revise em 1, 3, 7, 15 e 30 dias.</p>' if first else '')
    return h + f'<div class="fc">{cs}</div>'
add(fcpage(FC[:12], True)); add(fcpage(FC[12:], False))

Q = [
 ("Teoria","A respeito da distinção entre direitos e garantias fundamentais, assinale a alternativa correta.",
  ["Direitos e garantias são expressões sinônimas na Constituição.","Os direitos são disposições assecuratórias, e as garantias, disposições declaratórias.","As garantias são instrumentos destinados a assegurar o exercício dos direitos, como o habeas corpus em relação à liberdade de locomoção.","Todas as garantias fundamentais são ações judiciais.","Os remédios constitucionais são direitos, e não garantias."],"C",
  "Garantias asseguram os direitos; o HC protege a locomoção. B inverte os conceitos; nem toda garantia é ação judicial (D); os remédios são espécie de garantia (E).","Direito declara; garantia assegura."),
 ("Teoria","Sobre as características dos direitos fundamentais, é correto afirmar que eles são:",
  ["absolutos, pois nunca podem ser restringidos.","renunciáveis, desde que a renúncia seja por escrito.","imprescritíveis, pois não se perdem pelo decurso do tempo.","alienáveis, quando tiverem conteúdo patrimonial.","taxativamente previstos no art. 5º."],"C",
  "São imprescritíveis. São relativos (A), irrenunciáveis (B), inalienáveis (D) e o rol do art. 5º é exemplificativo (E).","HUIIR."),
 ("Igualdade","Edital de concurso para Guarda Municipal fixou idade máxima de 30 anos, sem previsão em lei e sem relação com as atribuições do cargo. Segundo o entendimento sumulado do STF, essa exigência:",
  ["é válida, por se tratar de critério objetivo.","é válida em qualquer concurso para carreira de segurança.","só se legitima quando justificada pela natureza das atribuições do cargo.","é sempre inconstitucional, pois a CF proíbe qualquer limite de idade.","depende apenas de previsão no edital."],"C",
  "Súmula 683 do STF: o limite de idade só se legitima quando justificado pela natureza das atribuições do cargo. A CF não proíbe todo limite (D), e o edital sozinho não basta (E).","Requisitos de concurso: lei + relação com o cargo."),
 ("Vida","A Constituição Federal admite a pena de morte:",
  ["nos crimes hediondos.","em caso de guerra declarada, nos termos do art. 84, XIX.","durante o estado de sítio.","no crime de terrorismo.","em caso de guerra civil."],"B",
  "Art. 5º, XLVII, “a”: só em caso de guerra declarada. As demais hipóteses não autorizam pena de morte.","Pena de morte: só guerra declarada."),
 ("Propriedade","Durante uma enchente, a Defesa Civil utilizou o galpão de uma empresa para abrigar desabrigados. Sobre essa situação, é correto afirmar que:",
  ["houve desapropriação, com indenização prévia e em dinheiro.","houve requisição, com indenização ulterior, se houver dano.","a medida é inconstitucional, por violar o direito de propriedade.","a indenização é sempre devida, ainda que não haja dano.","depende de autorização judicial prévia."],"B",
  "Iminente perigo público autoriza a requisição (XXV): o bem é usado temporariamente e a indenização é ulterior, só se houver dano.","Requisição: ulterior e se houver dano."),
 ("Segurança","Nos termos do art. 5º, XXXVI, a lei não prejudicará:",
  ["a expectativa de direito, o ato jurídico perfeito e a coisa julgada.","o direito adquirido, o ato jurídico perfeito e a coisa julgada.","o direito adquirido, o regime jurídico e a coisa julgada.","o direito adquirido, o ato administrativo e a sentença de primeiro grau.","apenas a coisa julgada."],"B",
  "Texto literal do inciso XXXVI. Expectativa de direito (A) e regime jurídico (C) não estão protegidos da mesma forma.","DAC."),
 ("Legalidade","Sobre o princípio da legalidade, assinale a alternativa correta.",
  ["O particular só pode fazer o que a lei expressamente autoriza.","A Administração Pública pode fazer tudo o que a lei não proíbe.","Ninguém será obrigado a fazer ou deixar de fazer alguma coisa senão em virtude de lei.","Uma portaria pode criar obrigações ao particular, independentemente de lei.","A legalidade aplica-se somente ao direito penal."],"C",
  "Texto literal do art. 5º, II. A e B invertem as regras do particular e da Administração; D e E estão erradas.","Particular: o que a lei não proíbe. Administração: o que a lei permite."),
 ("Expressão","Sobre a liberdade de manifestação do pensamento, é correto afirmar que:",
  ["é livre, sendo assegurado o anonimato.","depende de licença prévia quando realizada pela imprensa.","é livre, sendo vedado o anonimato e assegurado o direito de resposta proporcional ao agravo, além de indenização.","o direito de resposta exclui o direito à indenização.","admite censura prévia em casos de interesse público."],"C",
  "Incisos IV e V. O anonimato é vedado (A); não há licença (B) nem censura (E); a resposta é “além da indenização” (D).","Sem anonimato, sem censura, com responsabilidade."),
 ("Religião","Pedro recusou-se a prestar o serviço militar obrigatório por convicção religiosa e também se recusou a cumprir a prestação alternativa fixada em lei. Nesse caso:",
  ["Pedro não sofrerá nenhuma consequência, por força da liberdade de crença.","Pedro poderá ser privado de direitos, nos termos do art. 5º, VIII.","Pedro deverá ser preso.","Pedro perderá a nacionalidade brasileira.","a prestação alternativa é inconstitucional."],"B",
  "A privação de direitos ocorre quando a pessoa invoca a crença para se eximir da obrigação geral e recusa a prestação alternativa (art. 5º, VIII; art. 15, IV).","Duas recusas = privação de direitos."),
 ("Reunião","Um grupo pretende realizar manifestação pacífica, sem armas, em praça pública. Nos termos da Constituição, o grupo deve:",
  ["obter autorização prévia do prefeito.","obter autorização judicial.","apenas avisar previamente a autoridade competente, sem frustrar reunião anteriormente convocada para o mesmo local.","pagar taxa de uso do espaço público.","realizar a reunião somente em local fechado."],"C",
  "Art. 5º, XVI: independe de autorização, exigido apenas o prévio aviso, sem frustrar outra reunião anteriormente convocada.","Aviso, não autorização."),
 ("Associação","A respeito do direito de associação, assinale a alternativa correta.",
  ["A criação de associações depende de autorização do Poder Executivo.","As associações podem ser dissolvidas por decisão administrativa.","As associações só podem ser compulsoriamente dissolvidas por decisão judicial transitada em julgado.","É permitida a associação de caráter paramilitar, desde que para fins lícitos.","O associado é obrigado a permanecer associado por no mínimo um ano."],"C",
  "Art. 5º, XIX. A criação independe de autorização (A); a dissolução é judicial (B); é vedada a paramilitar (D); ninguém é obrigado a permanecer associado (E).","Suspensão: judicial. Dissolução: judicial + trânsito em julgado."),
 ("Casa","Policiais, munidos de mandado judicial de busca e apreensão, pretendem ingressar numa residência às 23h, sem consentimento do morador e sem situação de flagrante. Nesse caso:",
  ["podem entrar, pois possuem ordem judicial.","não podem entrar, pois a determinação judicial só pode ser cumprida durante o dia.","podem entrar, desde que acompanhados de duas testemunhas.","podem entrar, desde que o juiz autorize expressamente o horário noturno.","só podem entrar com autorização do delegado."],"B",
  "Art. 5º, XI: a determinação judicial só autoriza o ingresso durante o dia. A Lei nº 13.869/2019 tipifica o cumprimento de mandado de busca domiciliar após as 21h ou antes das 5h.","Ordem judicial: só de dia."),
 ("Casa","É hipótese em que a Constituição autoriza o ingresso na casa, sem consentimento do morador, durante a noite:",
  ["cumprimento de mandado de prisão.","flagrante delito.","determinação de Comissão Parlamentar de Inquérito.","ordem do Ministério Público.","fiscalização tributária."],"B",
  "Flagrante, desastre e socorro autorizam o ingresso a qualquer hora. Ordem judicial só de dia; CPI, MP e Fisco não podem determinar busca domiciliar.","FDS: a qualquer hora."),
 ("Sigilo","Sobre o sigilo das comunicações telefônicas, é correto afirmar que a interceptação:",
  ["pode ser determinada por CPI.","pode ser autorizada por juiz para instruir ação de divórcio.","depende de ordem judicial, nas hipóteses e na forma da lei, para investigação criminal ou instrução processual penal.","pode ser determinada pelo delegado em caso de urgência.","é absolutamente proibida."],"C",
  "Art. 5º, XII. CPI não determina interceptação (reserva de jurisdição); a finalidade deve ser penal.","Juiz + lei + fim penal."),
 ("Petição","Um cidadão requereu certidão a uma repartição pública para defender um direito, e o pedido foi negado sem justificativa. O remédio constitucional adequado é:",
  ["habeas data.","habeas corpus.","mandado de segurança.","mandado de injunção.","ação popular."],"C",
  "A obtenção de certidões é direito líquido e certo (XXXIV, “b”); a recusa ilegal é combatida por mandado de segurança. O HD é para informações da própria pessoa em bancos de dados.","Certidão negada → MS."),
 ("HC","Sobre o habeas corpus, assinale a alternativa correta.",
  ["Só pode ser impetrado por advogado.","Pessoa jurídica pode figurar como paciente.","Pode ser preventivo, quando há ameaça de violência ou coação à liberdade de locomoção.","Cabe para discutir o mérito de punições disciplinares militares.","É uma ação onerosa, sujeita a custas."],"C",
  "O HC pode ser preventivo ou repressivo. Dispensa advogado (A); o paciente é pessoa física (B); não cabe quanto ao mérito das punições disciplinares militares (D); é gratuito (E).","HC: locomoção, gratuito, sem advogado."),
 ("HD","Maria quer conhecer as informações a seu respeito constantes de banco de dados de entidade governamental. Segundo a jurisprudência do STJ, para impetrar habeas data ela deve:",
  ["comprovar a recusa ou a omissão da autoridade administrativa em fornecer as informações.","comprovar que é eleitora.","impetrar a ação sem advogado.","pagar custas iniciais.","aguardar o prazo de 120 dias."],"A",
  "Súmula 2 do STJ e Lei nº 9.507/1997, art. 8º, parágrafo único: é preciso a recusa (ou demora) administrativa. O HD é gratuito e exige advogado; 120 dias é o prazo do MS.","HD: recusa prévia + advogado + gratuito."),
 ("MS","O mandado de segurança:",
  ["protege qualquer direito, ainda que dependa de prova testemunhal.","é cabível contra lei em tese.","protege direito líquido e certo não amparado por habeas corpus ou habeas data, e deve ser impetrado em até 120 dias da ciência do ato.","substitui a ação de cobrança.","pode ser impetrado sem advogado."],"C",
  "Art. 5º, LXIX, e Lei nº 12.016/2009, art. 23. Exige prova pré-constituída (A); não cabe contra lei em tese (B, Súmula 266) nem substitui cobrança (D, Súmula 269); exige advogado (E).","MS: líquido e certo, residual, 120 dias."),
 ("MS coletivo","Pode impetrar mandado de segurança coletivo, nos termos da Constituição:",
  ["qualquer partido político registrado no TSE.","associação legalmente constituída e em funcionamento há pelo menos seis meses.","partido político com representação no Congresso Nacional.","o cidadão, em defesa do patrimônio público.","pessoa física, em defesa de direito alheio."],"C",
  "Art. 5º, LXX: partido com representação no Congresso Nacional; organização sindical, entidade de classe ou associação em funcionamento há pelo menos um ano.","Partido com representação no CN; associação há 1 ano."),
 ("MI","O mandado de injunção é cabível quando:",
  ["houver ilegalidade praticada por autoridade pública.","a falta de norma regulamentadora tornar inviável o exercício de direitos e liberdades constitucionais.","for necessário anular ato lesivo ao patrimônio público.","a pessoa quiser corrigir dados pessoais.","houver prisão ilegal."],"B",
  "Art. 5º, LXXI. A descreve o MS; C, a ação popular; D, o HD; E, o HC.","MI = omissão legislativa."),
 ("Ação popular","Sobre a ação popular, assinale a alternativa correta.",
  ["Pode ser proposta por pessoa jurídica.","O autor fica isento de custas e do ônus da sucumbência, salvo comprovada má-fé.","Só é cabível se houver prejuízo financeiro ao erário.","Pode ser proposta por estrangeiro residente no País.","É proposta exclusivamente pelo Ministério Público."],"B",
  "Art. 5º, LXXIII. Pessoa jurídica não propõe (Súmula 365); a lesão à moralidade basta; estrangeiro não é cidadão; o autor é qualquer cidadão.","AP: cidadão, isento salvo má-fé."),
 ("Remédios","São gratuitas, nos termos do art. 5º, LXXVII, as ações de:",
  ["mandado de segurança e mandado de injunção.","habeas corpus e habeas data.","habeas corpus e mandado de segurança.","ação popular e habeas data.","todos os remédios constitucionais."],"B",
  "Somente HC e HD são gratuitos por força do inciso LXXVII.","Gratuitos: HC e HD."),
 ("Processo","Sobre o devido processo legal e as provas, é correto afirmar que:",
  ["o devido processo legal só se aplica ao processo penal.","são inadmissíveis, no processo, as provas obtidas por meios ilícitos.","a razoável duração do processo aplica-se apenas ao processo judicial.","o devido processo legal tem apenas sentido formal.","provas ilícitas são admitidas se o crime for grave."],"B",
  "Art. 5º, LVI. O devido processo vale para privação da liberdade ou de bens (A); a razoável duração vale no judicial e no administrativo (C); há também o sentido material (D).","Provas ilícitas: inadmissíveis."),
 ("Ampla defesa","Servidor municipal respondeu a processo administrativo disciplinar sem estar assistido por advogado, mas foi notificado, apresentou defesa e pôde produzir provas. Segundo o STF:",
  ["o processo é nulo, pois a defesa técnica é obrigatória em qualquer processo.","a falta de defesa técnica por advogado no PAD não ofende a Constituição.","o contraditório não se aplica a processos administrativos.","o processo é nulo, pois a ampla defesa só se aplica com advogado.","o servidor deveria ter impetrado habeas data."],"B",
  "Súmula Vinculante 5. O contraditório e a ampla defesa valem no processo administrativo (LV), mas a ausência de advogado no PAD, por si só, não gera nulidade.","SV 5: PAD sem advogado é válido.")]

def qhtml(i, q):
    tema, enun, alts, gab, com, mem = q
    lis = "".join(f'<li data-l="{"ABCDE"[j]}">{a}</li>' for j,a in enumerate(alts))
    return f'<div class="q"><div class="qh"><span class="qn">Questão {i:02d}</span><span class="qa">Questão autoral · {tema}</span></div><p>{enun}</p><ol>{lis}</ol></div>'
qs = [qhtml(i+1,q) for i,q in enumerate(Q)]
add('<div class="marker">§§R3§§</div><div class="unit"><span class="u">PRÁTICA</span><span class="t">24 questões</span></div><h1 class="big">Questões <span class="hl">autorais</span></h1><p class="lead">Elaboradas para este caderno, no estilo de concursos. Nenhuma foi aplicada por banca. Resolva sem consultar.</p>' + "".join(qs[:3]))
for k in range(3, len(qs), 3): add("".join(qs[k:k+3]))

def grid(a, b):
    return "<table><tr>" + "".join(f"<th style='text-align:center'>{i+1:02d}</th>" for i in range(a,b)) + "</tr><tr>" + "".join(f"<td style='text-align:center;font-weight:900;color:#0b2a5b'>{Q[i][3]}</td>" for i in range(a,b)) + "</tr></table>"
gabs = [f'<div class="gab"><div class="gh">Questão {i+1:02d} <span>{q[3]}</span></div><p>{q[4]}</p><span class="mem">Memorize: {q[5]}</span></div>' for i,q in enumerate(Q)]
add('<div class="marker">§§R4§§</div><div class="unit"><span class="u">CORREÇÃO</span></div><h1 class="big">Gabarito <span class="hl">comentado</span></h1><p class="lead">Leia o comentário mesmo quando acertar.</p>' + grid(0,12) + grid(12,24) + "".join(gabs[:4]))
for k in range(4, len(gabs), 6): add("".join(gabs[k:k+6]))
# respostas dos treinos
def tr_block(lst):
    out = ""
    for n, itens in lst:
        rows = "".join(f'<tr><td style="width:7%;text-align:center;font-weight:900">{i+1}</td><td style="width:12%;text-align:center" class="{"yes" if r=="C" else "no"}">{"CERTO" if r=="C" else "ERRADO"}</td><td>{c}</td></tr>' for i,(_,r,c) in enumerate(itens))
        out += f'<h3>Treino rápido · Unidade {n}</h3><table><tr><th>#</th><th>Resposta</th><th>Comentário</th></tr>{rows}</table>'
    return out
add('<div class="unit"><span class="u">CORREÇÃO</span><span class="t">Treinos rápidos</span></div><h1 class="big">Respostas dos <span class="hl">treinos</span></h1><p class="lead">Certo ou errado das Unidades 1 a 4.</p>' + tr_block(TREINOS[:2]))
add(tr_block(TREINOS[2:]))
tr_html = ""
for n, itens in []:
    rows = "".join(f'<tr><td style="width:7%;text-align:center;font-weight:900">{i+1}</td><td style="width:10%;text-align:center" class="{"yes" if r=="C" else "no"}">{"CERTO" if r=="C" else "ERRADO"}</td><td>{c}</td></tr>' for i,(_,r,c) in enumerate(itens))
    tr_html += f'<div class="cmp"><h3>Treino rápido · Unidade {n}</h3><table><tr><th>#</th><th>Resposta</th><th>Comentário</th></tr>{rows}</table></div>'

add(f'''<div class="marker">§§R5§§</div><div class="unit"><span class="u">ENCERRAMENTO</span></div><h1 class="big">Referências e <span class="hl">verificação</span></h1><p class="lead">De onde vieram as informações.</p>
<h3>Legislação consultada (portal do Planalto)</h3>
<ul>
<li>BRASIL. <strong>Constituição Federal de 1988</strong>: art. 5º (caput; incisos I a VI, VIII, IX, X a XXV, XXXIV a XXXVI, XLVII, LIV a LVI, LXVIII a LXXIII, LXXVII a LXXIX; §§ 1º e 2º), conferidos palavra por palavra no texto compilado. Citados também os arts. 15, 19, 37, 84, 103, 139, 142, 143, 144, 182, 184 e 243.</li>
<li><strong>Lei nº 9.507/1997</strong> (habeas data), art. 8º, parágrafo único · <strong>Lei nº 12.016/2009</strong> (mandado de segurança), art. 23 · <strong>Lei nº 13.300/2016</strong> (mandado de injunção), arts. 2º, 8º e 12 · <strong>Lei nº 13.869/2019</strong> (abuso de autoridade), art. 22, § 1º, III. Todas conferidas no Planalto.</li>
<li>Citadas sem nova conferência: Lei nº 4.717/1965 (ação popular), Lei nº 9.296/1996 (interceptação telefônica), Código Penal (art. 25) e Código de Processo Penal (art. 157, § 1º).</li>
</ul>
<h3>Jurisprudência citada</h3>
<ul>
<li>STF: Súmulas 266, 269, 365, 629 e 683; Súmulas Vinculantes 5, 14 e 44.</li>
<li>STJ: Súmula 2.</li>
<li>STF: RE 201.819 (eficácia horizontal); ADPF 186 (cotas); ADPF 54 (anencefalia); ADI 3.510 (células-tronco); ADI 4.815 (biografias); HC 82.424 (Ellwanger); ADPF 187 (liberdade de reunião); RE 603.616, Tema 280 (ingresso em domicílio); MI 670, 708 e 712 (greve de servidores).</li>
</ul>
{lembre(f"""<p><strong>Material pesquisado e atualizado em: {DATA}.</strong> O texto do art. 5º foi conferido no Planalto: nenhum inciso novo depois do LXXIX, e a emenda mais recente no artigo é a EC nº 115/2022 (proteção de dados). <strong>Limitação:</strong> os portais de súmulas do STF e do STJ e a página do Tema 280 não puderam ser lidos pela ferramenta de pesquisa (o conteúdo é carregado por script). Por isso as súmulas e os precedentes citados reproduzem entendimentos consolidados, mas <strong>não foram reconferidos nas fontes oficiais nesta edição</strong>. Confira antes da prova e consulte o edital do seu concurso.</p>""", "Verificação e limitações")}
''')
add(f'''<div class="ending"><h2>Fim do Caderno 02</h2><p style="text-align:center">Próximo caderno da coleção: <strong>Direitos Sociais, Nacionalidade e Direitos Políticos (arts. 6º a 17)</strong>.</p>
<p class="note" style="text-align:center">Caderno Simplificado · Direito Constitucional · Caderno 02 · 1ª edição · novembro de 2026<br>Material de estudo independente. Não substitui a leitura da Constituição e do edital do seu concurso.</p></div>''')

doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Caderno Simplificado — Direito Constitucional — Caderno 02</title>
<link rel="stylesheet" href="estilo.css"></head><body>{symbols()}{"".join(P)}</body></html>'''
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "miolo.html"), "w").write(doc)
print("páginas planejadas:", len(P))
