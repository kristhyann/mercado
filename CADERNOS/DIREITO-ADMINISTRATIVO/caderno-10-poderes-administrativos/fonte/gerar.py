"""Gera miolo.html do Caderno 10: Poderes Administrativos. Uso: python3 gerar.py
Base legal conferida no portal do Planalto em 26/11/2026: CF/88 (arts. 5º, 49 e 84), CTN (arts. 77 e 78),
Lei nº 4.717/1965 (art. 2º), Lei nº 9.784/1999, Lei nº 8.112/1990 e Lei nº 9.873/1999."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from componentes import *

DATA = "26 de novembro de 2026"
P = []
def add(html, first=False): P.append(page(f'<div class="marker">§§P{len(P)+1:03d}§§</div>' + html, first))
U = {1:("UNIDADE 1","Noções gerais"),2:("UNIDADE 2","Vinculado e discricionário"),3:("UNIDADE 3","Hierárquico e disciplinar"),4:("UNIDADE 4","Poder regulamentar"),5:("UNIDADE 5","Poder de polícia"),6:("UNIDADE 6","Limites e abuso de poder")}
def H(u, title, lead, marker=None): return head(U[u][0], U[u][1], title, lead, marker)
def p(t): return f"<p>{t}</p>"
def colors(*keys):
    m = {"b":(C['blue'],C['sky']),"g":(C['green'],C['greensoft']),"o":(C['golddeep'],C['goldsoft']),"r":(C['red'],C['redsoft']),"n":(C['navy'],'#e3eaf3')}
    return [m[k] for k in keys]
def atencao(html, kws=None, t='Atenção na prova'):
    add(pratica_title(t) + html + (kw(kws) if kws else ''))
NV = '#e3eaf3'
def scene3(items, cap):
    s = f'<figure><svg viewBox="0 0 640 260" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    for i,(t,fg,bg,who,lines,leg) in enumerate(items):
        x = i*214
        s += f'<rect x="{x+2}" y="2" width="206" height="256" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x+105}" y="26" text-anchor="middle" font-weight="900" font-size="14" fill="{fg}">{t}</text>'
        s += f'<rect x="{x+14}" y="38" width="182" height="{20+len(lines)*17}" rx="12" fill="#fff" stroke="{fg}" stroke-width="1.8"/>'
        s += "".join(f'<text x="{x+105}" y="{58+j*17}" text-anchor="middle" font-size="11.2" font-weight="800" fill="{C["ink"]}">{l}</text>' for j,l in enumerate(lines))
        s += f'<g transform="translate({x+70},{70+len(lines)*17})"><svg viewBox="0 0 100 170" width="62" height="105"><use href="#ch-{who}"/></svg></g>'
        s += f'<text x="{x+105}" y="244" text-anchor="middle" font-size="11" font-weight="900" fill="{fg}">{leg}</text>'
    return s + f'</svg><figcaption>{cap}</figcaption></figure>'
def cf(x): return f"{x} · Constituição Federal"
def arrowdefs(i="ar"):
    return f'<defs><marker id="{i}" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L10,5 L0,10 z" fill="{C["ink"]}"/></marker></defs>'

# ================================================================ APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">Os instrumentos que a Administração usa para cumprir a lei, e o que acontece quando ela passa dos limites.</p>
<p>Este é o <strong>Caderno 10 da coleção</strong>, o segundo de <strong>Direito Administrativo</strong>. Ele trata dos <strong>poderes administrativos</strong>: vinculado, discricionário, hierárquico, disciplinar, regulamentar e de polícia, além dos <strong>limites</strong> desses poderes e do <strong>abuso de poder</strong>, nas formas de <strong>excesso de poder</strong> e <strong>desvio de finalidade</strong>.</p>
<p>É um assunto essencial para <strong>Guardas Municipais e polícias</strong>: o poder de polícia, a hierarquia e a disciplina fazem parte do dia a dia desses cargos. Por isso, cada poder vem com <strong>situações hipotéticas</strong> do cotidiano da Administração e com <strong>comparações visuais</strong> entre os poderes que mais se confundem.</p>
{table(["Recurso","Onde está"],[["Diagrama de classificação dos poderes","Unidade 1"],["Cenas: vinculado x discricionário; hierárquico x disciplinar","Unidades 2 e 3"],["Delegação x avocação e regulamento executivo x autônomo","Unidades 3 e 4"],["Ciclo de polícia e polícia administrativa x judiciária","Unidade 5"],["Cenas: excesso de poder x desvio de finalidade x omissão","Unidade 6"],["Quadro dos seis poderes, dicas de memorização e 24 questões autorais","Revisão e prática"]],["58%",None])}
{lembre(p(f'A base legal (Constituição, CTN, Lei da Ação Popular, Lei nº 9.784/1999, Lei nº 8.112/1990 e Lei nº 9.873/1999) foi conferida no portal do Planalto em <strong>{DATA}</strong>. Grande parte da teoria dos poderes é <strong>construção doutrinária</strong>; o caderno indica quando é o caso.'), "Fontes e atualização")}''', first=True)

TOC = [("u","UNIDADE 1 · NOÇÕES GERAIS","U1"),("","1. Conceito: o poder-dever","A01"),("","2. Classificação dos poderes (diagrama)","A02"),
 ("u","UNIDADE 2 · PODER VINCULADO E PODER DISCRICIONÁRIO","U2"),("","3. Poder vinculado","A03"),("","4. Poder discricionário e mérito administrativo","A04"),("","5. Vinculado x discricionário","A05"),
 ("u","UNIDADE 3 · PODER HIERÁRQUICO E PODER DISCIPLINAR","U3"),("","6. Poder hierárquico","A06"),("","7. Delegação x avocação","A07"),("","8. Poder disciplinar","A08"),("","9. Hierárquico x disciplinar","A09"),
 ("u","UNIDADE 4 · PODER REGULAMENTAR","U4"),("","10. Poder regulamentar e seus limites","A10"),("","11. Decreto regulamentar x decreto autônomo","A11"),
 ("u","UNIDADE 5 · PODER DE POLÍCIA","U5"),("","12. Conceito de poder de polícia","A12"),("","13. Polícia administrativa x polícia judiciária","A13"),("","14. Ciclo de polícia e delegação","A14"),("","15. Atributos e limites do poder de polícia","A15"),
 ("u","UNIDADE 6 · LIMITES E ABUSO DE PODER","U6"),("","16. Limites dos poderes administrativos","A16"),("","17. Abuso de poder: excesso e desvio","A17"),("","18. Consequências e controle do abuso","A18"),
 ("u","REVISÃO E PRÁTICA","RV"),("","Mapa conceitual · Quadro dos poderes · Erros mais comuns","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),("","Gabarito, respostas dos treinos e referências","R4")]
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
opener("01","UNIDADE 1","Noções gerais",["Conceito: o poder-dever","Classificação dos poderes"],"U1")

add(H(1,'Conceito: o <span class="hl">poder-dever</span>','Poderes são ferramentas para cumprir o interesse público.', "A01") +
 oque(p('<strong>Poderes administrativos</strong> são as <strong>prerrogativas</strong> que a lei confere à Administração e a seus agentes para que possam alcançar o <strong>interesse público</strong>. São <strong>instrumentais</strong>: existem como meio, e não como privilégio pessoal do agente.')) +
 traduz(p('Na Administração, o poder vem sempre acompanhado de um <strong>dever</strong>. O fiscal que encontra um restaurante com comida estragada <strong>não pode escolher</strong> se vai agir ou não: ele tem o <strong>dever de agir</strong>. Por isso a doutrina fala em <strong>poder-dever</strong> (ou, em uma leitura que destaca o dever, <strong>dever-poder</strong>). A competência é <strong>irrenunciável</strong> (Lei nº 9.784/1999, art. 11).')) +
 table(["Característica","O que significa"],[
  ["Instrumentais","Servem para atingir o interesse público, e não o interesse do agente"],
  ["Irrenunciáveis","O agente não pode abrir mão deles; a competência é irrenunciável, salvo delegação e avocação previstas em lei"],
  ["Limitados pela lei","Só existem nos limites da lei; fora disso, há abuso de poder"],
  ["Exercício obrigatório","Diante da situação prevista em lei, o agente deve agir; a omissão pode gerar responsabilidade"]],["26%",None]) +
 memo('Poder administrativo = <strong>poder-dever</strong>: <strong>instrumental</strong>, <strong>irrenunciável</strong> e <strong>limitado pela lei</strong>. Não agir quando devia também é ilegal.'))

def classif():
    N,G,O=C['navy'],C['blue'],C['golddeep']
    s = f'<figure><svg viewBox="0 0 640 300" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    s += f'<g stroke="#9db0c8" stroke-width="2.5" fill="none"><path d="M320 50 V70 M140 70 H500 M140 70 V88 M500 70 V88 M140 144 V160 M75 160 H205 M75 160 V176 M205 160 V176 M500 144 V160 M352 160 H592 M352 160 V176 M432 160 V176 M512 160 V176 M592 160 V176"/></g>'
    s += f'<rect x="190" y="6" width="260" height="44" rx="12" fill="{N}"/><text x="320" y="26" text-anchor="middle" font-size="13" font-weight="900" fill="#fff">PODERES ADMINISTRATIVOS</text><text x="320" y="42" text-anchor="middle" font-size="10" fill="#cfe0f2">classificação usada nas provas</text>'
    s += f'<rect x="20" y="88" width="240" height="56" rx="12" fill="{C["goldsoft"]}" stroke="{O}" stroke-width="2.4"/><text x="140" y="111" text-anchor="middle" font-size="12.5" font-weight="900" fill="{O}">QUANTO À LIBERDADE</text><text x="140" y="130" text-anchor="middle" font-size="10" fill="{C["ink"]}">existe margem de escolha?</text>'
    s += f'<rect x="380" y="88" width="240" height="56" rx="12" fill="{C["sky"]}" stroke="{G}" stroke-width="2.4"/><text x="500" y="111" text-anchor="middle" font-size="12.5" font-weight="900" fill="{G}">QUANTO À FINALIDADE</text><text x="500" y="130" text-anchor="middle" font-size="10" fill="{C["ink"]}">para que serve o poder?</text>'
    for x,a,b in [(75,"VINCULADO","sem escolha"),(205,"DISCRICIONÁRIO","escolha legal")]:
        s += f'<rect x="{x-58}" y="176" width="116" height="56" rx="10" fill="#fff" stroke="{O}" stroke-width="2"/><text x="{x}" y="200" text-anchor="middle" font-size="10.5" font-weight="900" fill="{C["ink"]}">{a}</text><text x="{x}" y="218" text-anchor="middle" font-size="9.5" fill="{C["muted"]}">{b}</text>'
    for x,a,b in [(352,"HIERÁRQUICO","organizar"),(432,"DISCIPLINAR","punir"),(512,"REGULAMENTAR","regulamentar"),(592,"DE POLÍCIA","limitar")]:
        s += f'<rect x="{x-38}" y="176" width="76" height="56" rx="10" fill="#fff" stroke="{G}" stroke-width="2"/><text x="{x}" y="200" text-anchor="middle" font-size="8.2" font-weight="900" fill="{C["ink"]}">{a}</text><text x="{x}" y="218" text-anchor="middle" font-size="9" fill="{C["muted"]}">{b}</text>'
    s += f'<text x="140" y="260" text-anchor="middle" font-size="10.5" font-weight="800" fill="{O}">dizem COMO o poder é exercido</text>'
    s += f'<text x="500" y="260" text-anchor="middle" font-size="10.5" font-weight="800" fill="{G}">dizem PARA QUE o poder serve</text>'
    s += f'<text x="320" y="290" text-anchor="middle" font-size="10" fill="{C["muted"]}">Ex.: o poder de polícia pode ser exercido de forma vinculada ou discricionária, conforme a lei.</text>'
    return s + '</svg><figcaption>Diagrama de classificação dos poderes administrativos.</figcaption></figure>'

add(H(1,'Classificação dos <span class="hl">poderes</span>','Dois grupos que se combinam.', "A02") +
 classif() +
 traduz(p('Repare que os grupos <strong>se combinam</strong>. "Vinculado" e "discricionário" dizem <strong>quanta liberdade</strong> a lei dá ao agente. Os outros quatro dizem <strong>para que</strong> o poder serve. Assim, aplicar uma multa de trânsito é exercício do <strong>poder de polícia</strong> e, ao mesmo tempo, um ato <strong>vinculado</strong>. Por isso parte da doutrina afirma que vinculação e discricionariedade não são "poderes" autônomos, e sim <strong>formas de exercício</strong> dos demais.'),"profa") +
 memo('Dica de memória: <strong>"Vi Di Hi Di Re Po"</strong>: <strong>Vi</strong>nculado, <strong>Di</strong>scricionário, <strong>Hi</strong>erárquico, <strong>Di</strong>sciplinar, <strong>Re</strong>gulamentar e de <strong>Po</strong>lícia. Os dois primeiros = <strong>como</strong>; os quatro últimos = <strong>para quê</strong>.'))

treino(1, [
 ("Os poderes administrativos são prerrogativas instrumentais, conferidas para a realização do interesse público.","C","São meios, não privilégios do agente."),
 ("O agente público pode renunciar a uma competência que a lei lhe atribuiu, desde que o faça por escrito.","E","A competência é irrenunciável (Lei nº 9.784/1999, art. 11), salvo delegação e avocação legais."),
 ("A omissão do agente que tinha o dever de agir pode configurar ilegalidade.","C","O poder é também um dever."),
 ("Uma mesma conduta pode ser, ao mesmo tempo, exercício do poder de polícia e ato vinculado.","C","Os grupos de classificação se combinam."),
 ("O poder hierárquico e o poder discricionário pertencem ao mesmo critério de classificação.","E","Discricionário é quanto à liberdade; hierárquico, quanto à finalidade."),
 ("A expressão poder-dever indica que o administrador tem a obrigação de exercer o poder quando a lei assim exigir.","C","Conceito central da unidade.")])

# ================================================================ UNIDADE 2
opener("02","UNIDADE 2","Poder vinculado e poder discricionário",["Poder vinculado","Poder discricionário e mérito","Vinculado x discricionário"],"U2")

add(H(2,'Poder <span class="hl">vinculado</span>','A lei já decidiu tudo: o agente só aplica.', "A03") +
 oque(p('É aquele em que a <strong>lei estabelece todos os elementos</strong> do ato, sem deixar margem de escolha ao agente. Presentes os requisitos legais, o agente <strong>deve</strong> praticar o ato, e do modo previsto.')) +
 flow([("doc",["PEDIDO","de licença","para construir"]),("check",["REQUISITOS","todos","cumpridos"]),("gavel",["DEVE","conceder","a licença"])],
      "No ato vinculado, cumpridos os requisitos, não há escolha: o ato deve ser praticado.", colors=colors("n","b","o")) +
 table(["Exemplo","Por que é vinculado"],[
  ["Concessão de aposentadoria compulsória ao atingir a idade-limite","A lei fixa a idade e a consequência"],
  ["Licença para construir quando o projeto cumpre todas as normas","Cumpridos os requisitos, há direito do particular"],
  ["Multa de trânsito com valor fixado em lei","O agente não escolhe o valor"],
  ["Nomeação do aprovado dentro do número de vagas, no prazo do concurso","O STF reconhece direito subjetivo à nomeação nesses casos"]],["50%",None]) +
 memo('Vinculado: a lei diz <strong>quem, quando, como e o quê</strong>. Requisitos cumpridos = o agente <strong>deve</strong> praticar o ato. Controle judicial: <strong>total</strong> (de legalidade).'))

add(H(2,'Poder <span class="hl">discricionário</span>','Escolha dentro da lei: conveniência e oportunidade.', "A04") +
 oque(p('É aquele em que a lei deixa ao agente uma <strong>margem de liberdade</strong> para escolher, entre as opções que ela mesma admite, a que melhor atende ao interesse público, segundo critérios de <strong>conveniência e oportunidade</strong>. Esse núcleo de escolha é o <strong>mérito administrativo</strong>.')) +
 traduz(p('Discricionariedade <strong>não é arbitrariedade</strong>. Arbitrário é agir <strong>fora</strong> da lei; discricionário é escolher <strong>dentro</strong> dela. A lei pode deixar margem de escolha de forma <strong>expressa</strong> ("poderá") ou usando <strong>conceitos jurídicos indeterminados</strong> ("boa conduta", "interesse público relevante"), que exigem uma avaliação do agente diante do caso.')) +
 table(["Ponto","Regra"],[
  ["Onde fica a liberdade","Em regra, no <b>motivo</b> e no <b>objeto</b> do ato; competência, finalidade e forma são, em regra, vinculadas (doutrina majoritária)"],
  ["Controle pelo Judiciário","Controla a <b>legalidade</b> (competência, forma, finalidade, razoabilidade, proporcionalidade, motivos), mas não substitui o administrador no <b>mérito</b>"],
  ["Teoria dos motivos determinantes","Se o agente declara um motivo, o ato fica vinculado a ele: motivo falso ou inexistente torna o ato inválido, ainda que a motivação não fosse obrigatória"],
  ["Revogação","Só o ato discricionário pode ser revogado por conveniência e oportunidade, e só pela própria Administração"]],["30%",None]) +
 memo('Discricionário = escolha <strong>dentro da lei</strong> (conveniência e oportunidade = <strong>mérito</strong>). O Judiciário controla a <strong>legalidade</strong>, não o mérito. Motivo declarado <strong>vincula</strong> o ato.'))

vd = scene3([("VINCULADO",C['navy'],NV,"prof",["“Cumpriu os requisitos?","Então a licença","tem de ser concedida.”"],"SEM ESCOLHA"),
 ("DISCRICIONÁRIO",C['blue'],C['sky'],"profa",["“Autorizo a feira","no sábado ou no","domingo, o que for melhor.”"],"ESCOLHA DENTRO DA LEI"),
 ("ARBITRÁRIO",C['red'],C['redsoft'],"prof",["“Não autorizo","porque não gosto","do organizador.”"],"FORA DA LEI = ILEGAL")], "Situação ilustrada: vinculação, discricionariedade e arbitrariedade.")
add(H(2,'Vinculado x <span class="hl">discricionário</span>','A comparação visual que mais cai.', "A05") + vd +
 table(["","PODER VINCULADO","PODER DISCRICIONÁRIO"],[
  ["Liberdade do agente","Nenhuma: a lei define tudo","Margem de escolha dentro da lei"],
  ["Critério","Aplicação da lei ao caso","Conveniência e oportunidade (mérito)"],
  ["Revogação","Não cabe revogação","Pode ser revogado pela Administração"],
  ["Controle judicial","Amplo, de legalidade","De legalidade, sem invadir o mérito"],
  ["Exemplos","Licença para construir; aposentadoria compulsória","Autorização de uso de bem público; escolha do momento de uma obra"]],["20%",None,None]))

atencao(
 ex(p('Uma associação pede à Prefeitura autorização para fazer uma feira cultural na praça. A lei municipal diz que a Prefeitura "poderá autorizar" o uso temporário de praças. A secretária autoriza a feira no domingo, e não no sábado, porque no sábado já há outro evento: escolha <b>discricionária</b> e válida. Se ela negasse a autorização declarando que "a praça estará em reforma", e a reforma não existisse, o ato seria <b>nulo</b> pela <b>teoria dos motivos determinantes</b>.')) +
 pega('<ul><li>Discricionariedade <b>não é</b> arbitrariedade: a escolha precisa respeitar a lei, a finalidade, a razoabilidade e a proporcionalidade.</li><li>O Judiciário <b>pode</b> anular um ato discricionário ilegal ou desproporcional; o que ele não pode é <b>revogar</b> o ato por achar outra opção mais conveniente.</li><li>Atos vinculados <b>não</b> são revogáveis por conveniência.</li></ul>'),
 ["conveniência e oportunidade","mérito administrativo","conceito jurídico indeterminado","motivos determinantes","controle de legalidade","arbitrariedade"])

treino(2, [
 ("No poder vinculado, preenchidos os requisitos legais, o agente é obrigado a praticar o ato.","C","Não há margem de escolha."),
 ("Discricionariedade e arbitrariedade são expressões sinônimas.","E","Discricionário é escolher dentro da lei; arbitrário é agir fora dela."),
 ("O Poder Judiciário pode revogar ato discricionário por considerá-lo inconveniente.","E","O Judiciário anula atos ilegais; a revogação é da própria Administração."),
 ("Pela teoria dos motivos determinantes, o motivo declarado vincula a validade do ato.","C","Motivo falso ou inexistente invalida o ato."),
 ("Os atos vinculados podem ser revogados por razões de conveniência e oportunidade.","E","Revogação é própria dos atos discricionários."),
 ("O mérito administrativo corresponde à avaliação de conveniência e oportunidade feita pelo administrador.","C","Núcleo do poder discricionário.")])

# ================================================================ UNIDADE 3
opener("03","UNIDADE 3","Poder hierárquico e poder disciplinar",["Poder hierárquico","Delegação x avocação","Poder disciplinar","Hierárquico x disciplinar"],"U3")

add(H(3,'Poder <span class="hl">hierárquico</span>','Organizar, distribuir e escalonar funções.', "A06") +
 oque(p('É o poder de que dispõe a Administração para <strong>organizar, distribuir e escalonar</strong> as funções de seus órgãos e para <strong>ordenar e rever</strong> a atuação de seus agentes, estabelecendo uma relação de <strong>subordinação</strong>. Existe dentro de uma <strong>mesma pessoa jurídica</strong>.')) +
 cards([("megaphone","Dar ordens","O superior expede ordens e instruções; o subordinado deve cumpri-las, salvo se manifestamente ilegais (Lei nº 8.112/1990, art. 116, IV).",C['navy']),("eye","Fiscalizar","Acompanhar a atuação dos subordinados.",C['blue']),("doc","Rever atos","Anular atos ilegais e revogar inconvenientes dos subordinados.",C['golddeep']),("split","Delegar e avocar","Transferir ou chamar para si competências, nos limites da lei.",C['green'])],4))
atencao(ex(p('O comandante da Guarda Municipal expede uma ordem de serviço definindo que, no feriado, a equipe reforçará a ronda nas praças: exercício do <b>poder hierárquico</b> (dar ordens). Ao perceber que um inspetor negou, por engano, um pedido de folga previsto em lei, o comandante <b>revê</b> e corrige a decisão do subordinado.')) +
 table(["Onde NÃO há hierarquia","Por quê"],[
  ["Entre a Administração direta e as entidades da indireta","Há vinculação e <b>controle finalístico</b> (tutela), não subordinação"],
  ["Na função típica do Judiciário e do Legislativo","Juízes e parlamentares decidem com independência ao julgar e legislar"],
  ["Entre órgãos consultivos e o órgão que decide, quanto ao conteúdo do parecer","O parecerista tem autonomia técnica"]],["40%",None]) +
 memo('Hierarquia = <strong>subordinação</strong> dentro da <strong>mesma pessoa jurídica</strong>: ordenar, fiscalizar, rever, delegar e avocar. Ordem <strong>manifestamente ilegal</strong> não se cumpre.') +
 pega('<ul><li>O poder hierárquico é <b>interno</b>: não alcança particulares nem outras pessoas jurídicas.</li><li>Rever atos do subordinado inclui <b>anular</b> (ilegais) e <b>revogar</b> (inconvenientes), respeitados os direitos adquiridos.</li><li>Obedecer não é absoluto: ordem <b>manifestamente ilegal</b> não deve ser cumprida.</li></ul>'),
 ["subordinação","mesma pessoa jurídica","ordem manifestamente ilegal","rever atos","controle finalístico"])

def delav():
    N,G,O=C['navy'],C['blue'],C['golddeep']
    s = f'<figure><svg viewBox="0 0 640 210" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">{arrowdefs("da")}'
    for x,t,c,bg in [(20,"DELEGAÇÃO",G,C['sky']),(330,"AVOCAÇÃO",O,C['goldsoft'])]:
        s += f'<rect x="{x}" y="4" width="290" height="200" rx="16" fill="{bg}" stroke="{c}" stroke-width="2.5"/><text x="{x+145}" y="30" text-anchor="middle" font-size="15" font-weight="900" fill="{c}">{t}</text>'
        s += f'<rect x="{x+90}" y="46" width="110" height="38" rx="9" fill="{N}"/><text x="{x+145}" y="70" text-anchor="middle" font-size="11" font-weight="900" fill="#fff">SUPERIOR</text>'
        s += f'<rect x="{x+90}" y="130" width="110" height="38" rx="9" fill="#fff" stroke="{N}" stroke-width="2"/><text x="{x+145}" y="154" text-anchor="middle" font-size="11" font-weight="900" fill="{N}">SUBORDINADO</text>'
    s += f'<line x1="165" y1="86" x2="165" y2="126" stroke="{C["ink"]}" stroke-width="3" marker-end="url(#da)"/><text x="182" y="110" font-size="10" font-weight="800" fill="{G}">transfere</text>'
    s += f'<line x1="475" y1="128" x2="475" y2="88" stroke="{C["ink"]}" stroke-width="3" marker-end="url(#da)"/><text x="492" y="110" font-size="10" font-weight="800" fill="{O}">chama para si</text>'
    s += f'<text x="165" y="190" text-anchor="middle" font-size="10" fill="{C["ink"]}">também a órgão não subordinado (art. 12)</text>'
    s += f'<text x="475" y="190" text-anchor="middle" font-size="10" fill="{C["ink"]}">temporária e excepcional (art. 15)</text>'
    return s + '</svg><figcaption>Delegação desce (ou vai para o lado); avocação sobe.</figcaption></figure>'

add(H(3,'Delegação x <span class="hl">avocação</span>','Lei nº 9.784/1999, arts. 11 a 15.', "A07") +
 delav() +
 table(["","DELEGAÇÃO (arts. 12 a 14)","AVOCAÇÃO (art. 15)"],[
  ["O que é","Transferir <b>parte</b> da competência a outro órgão ou agente","O superior chama para si competência de órgão <b>hierarquicamente inferior</b>"],
  ["Exige hierarquia?","<b>Não necessariamente</b>: pode ser a órgão não subordinado, quando conveniente","<b>Sim</b>: só de órgão inferior"],
  ["Características","Ato publicado; revogável a qualquer tempo; a decisão é considerada do <b>delegado</b>","Temporária, excepcional e por motivos relevantes, devidamente justificados"]],["18%",None,None]) +
 lei("Art. 13 · Lei nº 9.784/1999",'<p>Art. 13. Não podem ser objeto de delegação:<br>I - a edição de atos de caráter normativo;<br>II - a decisão de recursos administrativos;<br>III - as matérias de competência exclusiva do órgão ou autoridade.</p>') +
 memo('Indelegáveis: <strong>"NoRE"</strong> = <strong>No</strong>rmativos, <strong>R</strong>ecursos e <strong>E</strong>xclusivos. Ato praticado por delegação = considerado do <strong>delegado</strong> (é contra ele que cabe mandado de segurança).'))

add(H(3,'Poder <span class="hl">disciplinar</span>','Apurar e punir infrações de quem tem vínculo com a Administração.', "A08") +
 oque(p('É o poder de <strong>apurar infrações e aplicar penalidades</strong> aos <strong>servidores públicos</strong> e às demais pessoas sujeitas à <strong>disciplina administrativa</strong>, como os particulares que têm <strong>vínculo especial</strong> com a Administração (por exemplo, empresas contratadas).')) +
 table(["Ponto","Regra"],[
  ["Quem se sujeita","Servidores e particulares com vínculo específico (contratados, alunos de escola pública, delegatários); <b>não</b> alcança o cidadão comum, que se sujeita ao poder de polícia"],
  ["Dever de apurar (Lei nº 8.112/1990, art. 143)","A autoridade que tiver ciência de irregularidade é <b>obrigada</b> a promover sua apuração imediata, por sindicância ou processo administrativo disciplinar, assegurada a ampla defesa"],
  ["Penalidades (Lei nº 8.112/1990, art. 127)","Advertência; suspensão; demissão; cassação de aposentadoria ou disponibilidade; destituição de cargo em comissão; destituição de função comissionada"],
  ["Dosimetria (art. 128)","Natureza e gravidade da infração, danos, agravantes e atenuantes e antecedentes funcionais; o ato menciona sempre o fundamento legal e a causa da sanção"],
  ["Garantias","Contraditório e ampla defesa (CF, art. 5º, LV) e motivação"]],["28%",None]) +
 traduz(p('O poder disciplinar tem uma face <strong>vinculada</strong> e outra <strong>discricionária</strong>. É vinculado o <strong>dever de apurar</strong> e de punir quando comprovada a infração. Há certa discricionariedade na <strong>escolha e graduação</strong> da pena, dentro dos limites da lei, mas para infrações em que a lei fixa a pena (como as que geram demissão), não há escolha.'),"profa") +
 memo('Disciplinar = punir <strong>quem tem vínculo</strong> com a Administração. Apurar é <strong>obrigatório</strong>. Sempre com <strong>contraditório, ampla defesa e motivação</strong>.'))

hd = scene3([("HIERÁRQUICO",C['navy'],NV,"prof",["“A partir de hoje,","a equipe fará","ronda na praça.”"],"ORDENAR / ORGANIZAR"),
 ("DISCIPLINAR",C['blue'],C['sky'],"profa",["“Após o processo,","aplico suspensão","de 10 dias.”"],"PUNIR QUEM TEM VÍNCULO"),
 ("DE POLÍCIA",C['golddeep'],C['goldsoft'],"prof",["“Seu bar está","sem alvará: fica","interditado.”"],"LIMITAR O PARTICULAR")], "Situação ilustrada: quem é atingido define o poder.")
add(H(3,'Hierárquico x <span class="hl">disciplinar</span>','E a diferença para o poder de polícia.', "A09") + hd +
 table(["","HIERÁRQUICO","DISCIPLINAR","DE POLÍCIA"],[
  ["Atinge","Subordinados","Servidores e particulares com vínculo especial","Qualquer particular (vínculo geral)"],
  ["Finalidade","Organizar, ordenar, rever","Apurar e punir infrações funcionais ou contratuais","Limitar direitos em favor do interesse coletivo"],
  ["Exemplo","Ordem de serviço; delegação","Suspensão de servidor; multa contratual a empresa contratada","Interdição de estabelecimento; multa de trânsito"]],["14%",None,None,None]))

atencao(
 ex(p('Uma empresa contratada pela Prefeitura para a limpeza das escolas descumpre o contrato e recebe <b>multa contratual</b>: exercício do <b>poder disciplinar</b>, porque há um vínculo especial (o contrato). Um restaurante qualquer, sem nenhum contrato com a Prefeitura, que é multado pela vigilância sanitária sofre o <b>poder de polícia</b>. E o chefe que muda a escala dos guardas municipais exerce o <b>poder hierárquico</b>.')) +
 pega('<ul><li>O poder disciplinar <b>decorre</b> do hierárquico quando se trata de servidores, mas <b>não se confunde</b> com ele: também alcança particulares contratados, que não são subordinados.</li><li>Punir o <b>cidadão comum</b> é poder de <b>polícia</b>, não disciplinar.</li><li>A sanção disciplinar não depende de processo penal: as instâncias penal, civil e administrativa são, em regra, <b>independentes</b>.</li></ul>'),
 ["subordinação","vínculo especial","sindicância","PAD","ampla defesa","independência das instâncias"])

treino(3, [
 ("O poder hierárquico existe entre a União e suas autarquias.","E","Entre direta e indireta há controle finalístico, não hierarquia."),
 ("A edição de atos de caráter normativo não pode ser objeto de delegação.","C","Lei nº 9.784/1999, art. 13, I."),
 ("A delegação de competência só é admitida para órgãos hierarquicamente subordinados.","E","Pode ser feita a órgãos não subordinados (art. 12)."),
 ("A avocação é temporária, excepcional e depende de motivos relevantes devidamente justificados.","C","Art. 15 da Lei nº 9.784/1999."),
 ("A multa aplicada a uma empresa contratada que descumpre o contrato decorre do poder disciplinar.","C","Há vínculo especial com a Administração."),
 ("A autoridade que toma ciência de irregularidade no serviço público pode escolher não apurá-la.","E","É obrigada a promover a apuração imediata (Lei nº 8.112/1990, art. 143).")])

# ================================================================ UNIDADE 4
opener("04","UNIDADE 4","Poder regulamentar",["Poder regulamentar e seus limites","Decreto regulamentar x decreto autônomo"],"U4")

add(H(4,'Poder <span class="hl">regulamentar</span> e seus limites','Detalhar a lei para a sua fiel execução.', "A10") +
 lei(cf("Art. 84, IV"),'<p>Art. 84. Compete privativamente ao Presidente da República: [...] IV - sancionar, promulgar e fazer publicar as leis, bem como expedir decretos e regulamentos para sua fiel execução;</p>') +
 traduz(p('O poder regulamentar (ou normativo) permite ao <strong>Chefe do Executivo</strong> editar <strong>decretos e regulamentos</strong> que <strong>detalham</strong> a lei para que ela possa ser aplicada no dia a dia. O regulamento <strong>não pode inovar</strong>: não cria direitos nem obrigações que a lei não previu. Pelo princípio da simetria, governadores e prefeitos têm o mesmo poder em relação às leis estaduais e municipais.')) +
 table(["Limite","Explicação"],[
  ["Não inovar na ordem jurídica","O regulamento não pode criar obrigações, proibições ou penalidades sem base na lei (CF, art. 5º, II)"],
  ["Não contrariar a lei","O regulamento que vai além da lei é ilegal"],
  ["Controle pelo Congresso (CF, art. 49, V)","O Congresso Nacional pode <b>sustar</b> os atos normativos do Executivo que <b>exorbitem do poder regulamentar</b>"],
  ["Controle judicial","O Judiciário pode afastar o regulamento ilegal"],
  ["Indelegabilidade","A edição de atos normativos não pode ser delegada por meio de delegação de competência comum (Lei nº 9.784/1999, art. 13, I)"]],["30%",None]) +
 memo('Regulamento = <strong>fiel execução</strong> da lei. <strong>Não inova</strong>. Se exorbitar, o Congresso pode <strong>sustar</strong> (CF, art. 49, V).'))

add(H(4,'Decreto regulamentar x <span class="hl">decreto autônomo</span>','Art. 84, IV e VI, da Constituição.', "A11") +
 lei(cf("Art. 84, VI (redação da EC nº 32/2001)"),'<p>VI - dispor, mediante decreto, sobre: a) organização e funcionamento da administração federal, quando não implicar aumento de despesa nem criação ou extinção de órgãos públicos; b) extinção de funções ou cargos públicos, quando vagos;</p>') +
 table(["","DECRETO REGULAMENTAR (executivo)","DECRETO AUTÔNOMO"],[
  ["Base","CF, art. 84, IV","CF, art. 84, VI (EC nº 32/2001)"],
  ["Relação com a lei","Depende de uma lei, que ele detalha","Retira fundamento <b>diretamente da Constituição</b>, sem lei a regulamentar"],
  ["Conteúdo","Qualquer lei que precise de detalhamento","Só duas matérias: organização da administração (sem aumentar despesa nem criar ou extinguir órgãos) e extinção de cargos ou funções <b>vagos</b>"],
  ["Pode inovar?","Não","Sim, nos limites estreitos das duas hipóteses"],
  ["Delegação","Indelegável","Pode ser delegado a Ministros, ao PGR e ao AGU (CF, art. 84, parágrafo único)"]],["18%",None,None]) +
 ex(p('Uma lei cria um benefício para servidores e diz que "o regulamento disporá sobre a forma de requerimento". O decreto que define documentos e prazos para o pedido é <b>regulamentar</b>. Já o decreto do Presidente que extingue cem cargos <b>vagos</b> de um ministério é <b>autônomo</b> (art. 84, VI, b). Se os cargos estivessem <b>ocupados</b>, a extinção exigiria lei.')) +
 pega('<ul><li>Decreto autônomo só existe nas <b>duas hipóteses</b> do art. 84, VI. Criar ou extinguir <b>órgãos</b> exige <b>lei</b>.</li><li>Extinguir cargos <b>vagos</b> pode ser por decreto; cargos <b>ocupados</b>, não.</li><li>As agências reguladoras editam normas técnicas, mas sempre <b>subordinadas à lei</b>.</li></ul>'))

treino(4, [
 ("O decreto regulamentar pode criar obrigações não previstas em lei, desde que de interesse público.","E","O regulamento não inova; obrigações dependem de lei (CF, art. 5º, II)."),
 ("Compete ao Congresso Nacional sustar os atos normativos do Poder Executivo que exorbitem do poder regulamentar.","C","CF, art. 49, V."),
 ("O Presidente da República pode, por decreto, extinguir cargos públicos vagos.","C","CF, art. 84, VI, b."),
 ("O decreto autônomo pode criar órgãos públicos, desde que não aumente a despesa.","E","Não pode criar nem extinguir órgãos (CF, art. 84, VI, a)."),
 ("A competência do art. 84, VI, pode ser delegada aos Ministros de Estado.","C","CF, art. 84, parágrafo único."),
 ("O poder regulamentar é exercido pelo Chefe do Poder Executivo para a fiel execução das leis.","C","CF, art. 84, IV.")])

# ================================================================ UNIDADE 5
opener("05","UNIDADE 5","Poder de polícia",["Conceito","Polícia administrativa x polícia judiciária","Ciclo de polícia e delegação","Atributos e limites"],"U5")

add(H(5,'Conceito de <span class="hl">poder de polícia</span>','O único poder com definição em lei: o art. 78 do CTN.', "A12") +
 lei("Art. 78, caput · Código Tributário Nacional (Lei nº 5.172/1966)",'<p>Considera-se poder de polícia atividade da administração pública que, limitando ou disciplinando direito, interesse ou liberdade, regula a prática de ato ou abstenção de fato, em razão de interesse público concernente à segurança, à higiene, à ordem, aos costumes, à disciplina da produção e do mercado, ao exercício de atividades econômicas dependentes de concessão ou autorização do Poder Público, à tranquilidade pública ou ao respeito à propriedade e aos direitos individuais ou coletivos.</p>') +
 traduz(p('Poder de polícia é a atividade de <strong>limitar e condicionar</strong> o exercício de direitos individuais (liberdade e propriedade) em benefício da <strong>coletividade</strong>. Você tem direito de abrir um restaurante, mas precisa de alvará e de higiene; tem direito de dirigir, mas precisa de habilitação e de respeitar os limites de velocidade. O CTN define o poder de polícia porque o seu exercício regular justifica a cobrança de <strong>taxas</strong> (art. 77).'),"profa") +
 table(["Sentido","Abrangência"],[
  ["Amplo","Toda atividade estatal que limita direitos, incluindo as <b>leis</b> que o fazem"],
  ["Estrito (o do Direito Administrativo)","A atividade da <b>Administração</b> de executar essas limitações: fiscalizar, licenciar, sancionar"]],["30%",None]) +
 memo('Poder de polícia = <strong>limitar ou condicionar</strong> liberdade e propriedade em favor do <strong>interesse coletivo</strong>. Conceito legal: <strong>art. 78 do CTN</strong>. Seu exercício regular permite cobrar <strong>taxa</strong>.'))

add(H(5,'Polícia administrativa x <span class="hl">polícia judiciária</span>','A diferença mais cobrada em provas de segurança pública.', "A13") +
 table(["","POLÍCIA ADMINISTRATIVA","POLÍCIA JUDICIÁRIA"],[
  ["Incide sobre","<b>Bens, direitos e atividades</b>","<b>Pessoas</b> (autoria de crimes)"],
  ["Ilícito","<b>Administrativo</b>","<b>Penal</b>"],
  ["Caráter","Predominantemente <b>preventivo</b> (mas também fiscaliza e reprime infrações administrativas)","Predominantemente <b>repressivo</b>: investiga crimes já ocorridos"],
  ["Regras","Direito Administrativo","Direito Processual Penal"],
  ["Quem exerce","Diversos órgãos: vigilância sanitária, fiscais, Detran, guardas municipais (posturas, trânsito)","Polícias Civis e Polícia Federal"]],["18%",None,None]) +
 lembre(p('O STF reconheceu ser constitucional atribuir às <strong>guardas municipais</strong> o exercício do <strong>poder de polícia de trânsito</strong>, inclusive a imposição de sanções administrativas previstas em lei (RE 658.570, Tema 472, 2015). Em 2025, no Tema 656, o STF também admitiu a atuação das guardas em <strong>segurança urbana</strong>, com policiamento ostensivo e comunitário, excluída a polícia judiciária.'), "Guardas municipais e poder de polícia") +
 ex(p('A Polícia Militar que faz policiamento ostensivo na rua atua de forma <b>preventiva</b>; ao prender alguém em flagrante e levá-lo à delegacia, colabora com a persecução penal, que segue com a <b>polícia judiciária</b> (Polícia Civil). Já o guarda municipal que multa um carro estacionado em local proibido exerce <b>polícia administrativa</b> de trânsito.')))

def ciclo():
    N,G,O,R=C['navy'],C['blue'],C['golddeep'],C['red']
    it=[("ORDEM","a lei ou o ato normativo","fixa a regra",N,NV),("CONSENTIMENTO","licença ou autorização","(alvará)",G,C['sky']),("FISCALIZAÇÃO","verifica o","cumprimento",O,C['goldsoft']),("SANÇÃO","multa, interdição,","apreensão",R,C['redsoft'])]
    s = f'<figure><svg viewBox="0 0 640 204" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">{arrowdefs("ci")}'
    for k,(t,a,b,fg,bg) in enumerate(it):
        x=6+k*160
        s += f'<rect x="{x}" y="30" width="136" height="100" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><circle cx="{x+20}" cy="30" r="15" fill="{fg}"/><text x="{x+20}" y="35" text-anchor="middle" font-size="13" font-weight="900" fill="#fff">{k+1}</text>'
        s += f'<text x="{x+68}" y="66" text-anchor="middle" font-size="12.5" font-weight="900" fill="{fg}">{t}</text><text x="{x+68}" y="88" text-anchor="middle" font-size="10" fill="{C["ink"]}">{a}</text><text x="{x+68}" y="104" text-anchor="middle" font-size="10" fill="{C["ink"]}">{b}</text>'
        if k<3: s += f'<line x1="{x+138}" y1="80" x2="{x+156}" y2="80" stroke="{C["ink"]}" stroke-width="2.5" marker-end="url(#ci)"/>'
    s += f'<text x="80" y="160" text-anchor="middle" font-size="10" font-weight="800" fill="{N}">indelegável</text><text x="240" y="160" text-anchor="middle" font-size="10" font-weight="800" fill="{G}">delegável*</text><text x="400" y="160" text-anchor="middle" font-size="10" font-weight="800" fill="{O}">delegável*</text><text x="560" y="160" text-anchor="middle" font-size="10" font-weight="800" fill="{R}">delegável* (STF, Tema 532)</text>'
    s += f'<text x="320" y="182" text-anchor="middle" font-size="9.5" fill="{C["muted"]}">* por lei, a pessoa jurídica de direito privado da Administração indireta, de capital majoritariamente</text><text x="320" y="196" text-anchor="middle" font-size="9.5" fill="{C["muted"]}">público, que preste serviço público próprio do Estado em regime não concorrencial</text>'
    return s + '</svg><figcaption>Ciclo de polícia: as quatro fases e o que pode ser delegado, segundo o STF (Tema 532, 2020).</figcaption></figure>'

add(H(5,'Ciclo de polícia e <span class="hl">delegação</span>','As quatro fases do poder de polícia.', "A14") +
 ciclo() +
 table(["Fase","Exemplo no trânsito"],[
  ["1. Ordem de polícia","O Código de Trânsito proíbe dirigir acima do limite de velocidade"],
  ["2. Consentimento","O Detran expede a carteira de habilitação (licença)"],
  ["3. Fiscalização","O radar e o agente de trânsito verificam a velocidade"],
  ["4. Sanção","Lavratura do auto de infração e aplicação da multa"]],["30%",None]) +
 lembre(p('No <strong>RE 633.782 (Tema 532, 2020)</strong>, o STF decidiu que é constitucional a <strong>delegação do poder de polícia, por meio de lei</strong>, a <strong>pessoas jurídicas de direito privado integrantes da Administração indireta</strong>, de capital social <strong>majoritariamente público</strong>, que prestem exclusivamente serviço público de atuação própria do Estado e em regime não concorrencial, <strong>inclusive para aplicar multas</strong>. A fase de <strong>ordem de polícia</strong>, que depende de lei, permanece indelegável. A delegação a particulares comuns continua não admitida; a eles podem ser atribuídos apenas atos materiais de apoio (como operar radares).'), "O que diz o STF sobre a delegação"))

add(H(5,'Atributos e limites do <span class="hl">poder de polícia</span>','Discricionariedade, autoexecutoriedade e coercibilidade.', "A15") +
 cards([("#D","Discricionariedade","Em regra, há margem de escolha sobre o momento e os meios; mas há atos vinculados, como a licença.") ,("#A","Autoexecutoriedade","A Administração executa a decisão sem precisar de ordem judicial (ex.: interditar obra irregular, apreender mercadoria estragada).") ,("#C","Coercibilidade","A decisão é imposta ao particular, inclusive com uso moderado da força, se necessário.")],3) +
 table(["Limite","Regra"],[
  ["Legalidade e competência","Só o órgão competente, nos limites da lei, com observância do processo legal (CTN, art. 78, parágrafo único)"],
  ["Proporcionalidade","A medida deve ser adequada, necessária e proporcional; vedados os excessos (ex.: destruir mercadoria que poderia ser apenas apreendida)"],
  ["Direitos fundamentais","Não pode eliminar o direito, só condicioná-lo"],
  ["Devido processo","Para as sanções, contraditório e ampla defesa; a autoexecutoriedade não dispensa o processo quando a lei o exige"],
  ["Prescrição (Lei nº 9.873/1999, art. 1º)","Prescreve em <b>5 anos</b> a ação punitiva da Administração federal no exercício do poder de polícia"]],["30%",None]) +
 memo('Atributos: <strong>"DAC"</strong> = <strong>D</strong>iscricionariedade, <strong>A</strong>utoexecutoriedade e <strong>C</strong>oercibilidade. Multa é coercitiva, mas sua <strong>cobrança forçada</strong> depende de execução judicial.'))

atencao(
 ex(p('Durante uma fiscalização de posturas, a equipe da Prefeitura, acompanhada da Guarda Municipal, encontra um food truck vendendo alimentos estragados. A apreensão e o descarte imediato da comida são exercício <b>autoexecutório</b> do poder de polícia, para proteger a saúde pública. A <b>multa</b>, porém, segue o processo administrativo com direito de defesa, e, se não for paga, a cobrança forçada depende de <b>execução fiscal</b> na Justiça.')) +
 pega('<ul><li>A <b>autoexecutoriedade</b> não existe em todos os atos: a cobrança forçada da multa exige a via judicial.</li><li>O poder de polícia <b>não</b> é sempre discricionário: a licença (ex.: alvará de construção) é ato <b>vinculado</b>.</li><li>Licença = ato vinculado e definitivo, em regra; autorização = ato discricionário e precário.</li><li>Particulares comuns <b>não</b> recebem delegação para multar; só entidades da Administração indireta que preencham os requisitos do Tema 532.</li></ul>'),
 ["art. 78 do CTN","ciclo de polícia","autoexecutoriedade","coercibilidade","proporcionalidade","prescrição de 5 anos"])

treino(5, [
 ("O conceito legal de poder de polícia está no art. 78 do Código Tributário Nacional.","C","Conceito legal expresso."),
 ("A polícia administrativa incide sobre pessoas, e a polícia judiciária, sobre bens e atividades.","E","É o contrário: a administrativa incide sobre bens, direitos e atividades; a judiciária, sobre pessoas."),
 ("Segundo o STF, a fase de ordem de polícia pode ser delegada a empresa privada concessionária.","E","A ordem de polícia é indelegável; a delegação admitida no Tema 532 alcança outras fases e só entidades da indireta que cumpram os requisitos."),
 ("A autoexecutoriedade permite à Administração executar suas decisões sem prévia ordem judicial, nos casos previstos em lei ou de urgência.","C","Atributo do poder de polícia."),
 ("O STF considerou constitucional atribuir às guardas municipais o poder de polícia de trânsito, inclusive para aplicar multas.","C","RE 658.570 (Tema 472)."),
 ("Prescreve em cinco anos a ação punitiva da Administração Pública Federal no exercício do poder de polícia.","C","Lei nº 9.873/1999, art. 1º.")])

# ================================================================ UNIDADE 6
opener("06","UNIDADE 6","Limites e abuso de poder",["Limites dos poderes administrativos","Abuso de poder: excesso e desvio","Consequências e controle do abuso"],"U6")

add(H(6,'Limites dos <span class="hl">poderes administrativos</span>','Todo poder tem fronteiras.', "A16") +
 flow([("scales",["LEGALIDADE","só nos limites","da lei"]),("target",["FINALIDADE","interesse","público"]),("idcard",["COMPETÊNCIA","agente certo"]),("puzzle",["PROPORCIO-","NALIDADE","meio adequado"]),("shield",["DIREITOS","fundamentais"])],
      "Os limites que acompanham qualquer poder administrativo.", colors=colors("n","b","o","g","r")) +
 table(["Limite","O que acontece se for ultrapassado"],[
  ["Competência","Ato praticado por quem não tem atribuição: <b>excesso de poder</b> (vício de competência)"],
  ["Finalidade","Ato com fim diverso do interesse público ou do previsto em lei: <b>desvio de finalidade</b>"],
  ["Motivos","Motivo falso ou inexistente: ato nulo (teoria dos motivos determinantes)"],
  ["Proporcionalidade e razoabilidade","Medida exagerada ou inadequada: ato ilegal, controlável pelo Judiciário"],
  ["Forma e processo","Sanção sem contraditório e ampla defesa: ato nulo"],
  ["Dever de agir","Omissão diante do dever legal: ilegalidade (omissão abusiva)"]],["30%",None]) +
 memo('Os limites dos poderes são os mesmos <strong>elementos do ato</strong>: competência, finalidade, forma, motivo e objeto, somados à <strong>proporcionalidade</strong>.'))

ab = scene3([("EXCESSO DE PODER",C['red'],C['redsoft'],"prof",["Guarda municipal","aplica pena de","demissão a colega."],"SEM COMPETÊNCIA"),
 ("DESVIO DE FINALIDADE",C['golddeep'],C['goldsoft'],"profa",["Remove servidor","para cidade distante","só por vingança."],"FIM DIVERSO"),
 ("OMISSÃO",C['navy'],NV,"prof",["Deixa de fiscalizar","obra perigosa","de um aliado."],"NÃO AGIR QUANDO DEVIA")], "Situação ilustrada: as formas de abuso de poder.")
add(H(6,'Abuso de poder: <span class="hl">excesso e desvio</span>','Gênero e espécies.', "A17") + ab +
 table(["","EXCESSO DE PODER","DESVIO DE FINALIDADE (ou de poder)"],[
  ["O que é","O agente atua <b>além da sua competência</b>","O agente atua dentro da competência, mas para <b>fim diverso</b> do previsto"],
  ["Elemento viciado","<b>Competência</b>","<b>Finalidade</b>"],
  ["Exemplo","Subordinado aplica pena que só o chefe máximo pode aplicar","Desapropriação feita para perseguir um adversário político"],
  ["Lei nº 4.717/1965","Incompetência (art. 2º, a)","Desvio de finalidade (art. 2º, e): o agente pratica o ato visando a fim diverso daquele previsto, explícita ou implicitamente, na regra de competência"]],["18%",None,None]))

atencao(
 flow([("alert",["ABUSO","DE PODER","(gênero)"]),("split",["DUAS","ESPÉCIES"]),("idcard",["EXCESSO","competência"]),("target",["DESVIO","finalidade"])],
      "Abuso de poder é o gênero; excesso de poder e desvio de finalidade são as espécies.", colors=colors("r","n","o","b")) +
 ex(p('Um prefeito <b>remove</b> um servidor para um distrito distante. Remoção por necessidade do serviço é permitida; mas, provado que o real motivo foi <b>punir</b> o servidor por ter feito uma denúncia, há <b>desvio de finalidade</b>: a remoção foi usada como castigo, fim diverso do previsto. Já um diretor de departamento que, sem competência, decide sozinho um recurso administrativo que cabia ao secretário pratica <b>excesso de poder</b>.')) +
 pega('<ul><li><b>Abuso</b> de poder é o <b>gênero</b>; <b>excesso</b> e <b>desvio</b> são espécies.</li><li>Excesso = <b>competência</b> (fora dos limites). Desvio = <b>finalidade</b> (dentro da competência, mas com outro fim).</li><li>O ato com desvio de finalidade pode parecer perfeitamente legal na forma: o vício está na <b>intenção</b>.</li><li>A <b>omissão</b> também pode configurar abuso, quando o agente deixa de agir tendo o dever de fazê-lo.</li></ul>'),
 ["abuso de poder","excesso de poder","desvio de finalidade","competência","finalidade","omissão"], "Abuso de poder: o gênero e as espécies")

add(H(6,'Consequências e <span class="hl">controle</span> do abuso','O que o cidadão e o Estado podem fazer.', "A18") +
 table(["Consequência ou instrumento","Como funciona"],[
  ["Nulidade do ato","O ato com abuso é ilegal e deve ser <b>anulado</b> pela própria Administração (autotutela) ou pelo Judiciário"],
  ["Mandado de segurança (CF, art. 5º, LXIX)","Protege direito líquido e certo contra <b>ilegalidade ou abuso de poder</b> de autoridade pública"],
  ["Direito de petição (CF, art. 5º, XXXIV, a)","Qualquer pessoa pode peticionar aos Poderes Públicos em defesa de direitos ou contra <b>ilegalidade ou abuso de poder</b>, sem pagar taxas"],
  ["Habeas corpus (CF, art. 5º, LXVIII)","Contra violência ou coação à liberdade de locomoção por ilegalidade ou abuso de poder"],
  ["Ação popular (Lei nº 4.717/1965)","O cidadão pode pedir a anulação de ato lesivo com desvio de finalidade ou incompetência, entre outros vícios"],
  ["Responsabilidade do agente","Disciplinar (Lei nº 8.112/1990), civil (ressarcimento) e penal: a Lei nº 13.869/2019 tipifica crimes de abuso de autoridade, que exigem finalidade específica de prejudicar ou beneficiar, ou mero capricho"],
  ["Responsabilidade do Estado","O Estado responde de forma objetiva pelo dano (CF, art. 37, § 6º), com direito de regresso contra o agente em caso de dolo ou culpa"]],["30%",None]) +
 lembre(p('Na Lei nº 8.112/1990, o servidor deve <strong>cumprir as ordens superiores, exceto quando manifestamente ilegais</strong> (art. 116, IV), e tem o dever de <strong>representar contra ilegalidade, omissão ou abuso de poder</strong> (art. 116, XII).'), "O servidor diante do abuso") +
 memo('Abuso de poder: ato <strong>nulo</strong> + responsabilidade <strong>disciplinar, civil e penal</strong> do agente. Remédios: <strong>mandado de segurança</strong>, <strong>direito de petição</strong>, <strong>habeas corpus</strong> e <strong>ação popular</strong>.'))

treino(6, [
 ("O abuso de poder é gênero, do qual são espécies o excesso de poder e o desvio de finalidade.","C","Classificação clássica."),
 ("No excesso de poder, o agente atua dentro de sua competência, mas visando a fim diverso do previsto em lei.","E","Essa é a definição de desvio de finalidade; o excesso é atuar além da competência."),
 ("A Lei nº 4.717/1965 define o desvio de finalidade como a prática do ato visando a fim diverso daquele previsto na regra de competência.","C","Art. 2º, parágrafo único, e."),
 ("A omissão do agente que tinha o dever de agir pode caracterizar abuso de poder.","C","Omissão abusiva, segundo a doutrina."),
 ("O servidor público deve cumprir qualquer ordem superior, ainda que manifestamente ilegal.","E","Exceto as manifestamente ilegais (Lei nº 8.112/1990, art. 116, IV)."),
 ("O mandado de segurança pode ser impetrado contra ilegalidade ou abuso de poder de autoridade pública.","C","CF, art. 5º, LXIX.")])

# ================================================================ REVISÃO
mapa = f'''<figure><svg viewBox="0 0 640 470" width="580" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<g stroke="#b3c2d4" stroke-width="2.5" fill="none"><path d="M320 235 L150 70"/><path d="M320 235 L490 70"/><path d="M320 235 L120 235"/><path d="M320 235 L520 235"/><path d="M320 235 L150 400"/><path d="M320 235 L490 400"/></g>
<circle cx="320" cy="235" r="74" fill="{C['navy']}"/><text x="320" y="225" text-anchor="middle" fill="#5fd39e" font-weight="900" font-size="13">PODERES</text>
<text x="320" y="245" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">ADMINIS-</text><text x="320" y="263" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">TRATIVOS</text>
''' + "".join(
 f'<rect x="{x-100}" y="{y-40}" width="200" height="80" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x}" y="{y-16}" text-anchor="middle" font-weight="900" font-size="12.5" fill="{fg}">{t}</text>'
 + "".join(f'<text x="{x}" y="{y+4+i*15}" text-anchor="middle" font-size="10.8" fill="{C["ink"]}">{l}</text>' for i,l in enumerate(ls))
 for x,y,t,ls,fg,bg in [
  (150,62,"VINC. x DISCRIC.",["vinculado: sem escolha","discricionário: mérito","Judiciário: só legalidade"],C['navy'],NV),
  (490,62,"HIERÁRQUICO",["ordenar, rever, delegar","indelegáveis: NoRE","sem hierarquia com indireta"],C['golddeep'],C['goldsoft']),
  (112,235,"DISCIPLINAR",["servidor e contratado","apurar é obrigatório","defesa e motivação"],C['blue'],C['sky']),
  (528,235,"REGULAMENTAR",["fiel execução (84, IV)","autônomo: 84, VI","Congresso susta (49, V)"],C['green'],C['greensoft']),
  (150,408,"DE POLÍCIA",["CTN, art. 78 · DAC","ordem, consentimento,","fiscalização, sanção"],C['golddeep'],C['goldsoft']),
  (490,408,"ABUSO DE PODER",["excesso: competência","desvio: finalidade","omissão também"],C['red'],C['redsoft'])]) + '</svg><figcaption>Mapa conceitual do Caderno 10.</figcaption></figure>'
add('<div class="marker">§§R1§§</div><div class="unit"><span class="u">REVISÃO</span><span class="t">Véspera da prova</span></div><h1 class="big">Mapa <span class="hl">conceitual</span></h1><p class="lead">Os poderes em seis blocos. Explique cada caixa em voz alta.</p>' + mapa)

add('<div class="unit"><span class="u">REVISÃO</span><span class="t">Comparação visual</span></div><h1 class="big">Quadro dos <span class="hl">seis poderes</span></h1><p class="lead">Uma linha por poder: o que é, quem atinge e um exemplo.</p>' +
 table(["Poder","Palavra-chave","Quem atinge","Exemplo"],[
  ["Vinculado","Sem escolha","Depende do ato","Concessão de licença com requisitos cumpridos"],
  ["Discricionário","Conveniência e oportunidade","Depende do ato","Autorização de uso de praça para evento"],
  ["Hierárquico","Subordinação","Agentes e órgãos subordinados","Ordem de serviço; delegação; avocação"],
  ["Disciplinar","Punir quem tem vínculo","Servidores e contratados","Suspensão de servidor após PAD"],
  ["Regulamentar","Fiel execução da lei","Todos (norma geral)","Decreto que regulamenta uma lei"],
  ["De polícia","Limitar direitos","Qualquer particular","Interdição de estabelecimento; multa de trânsito"]],["16%","22%",None,None]) +
 memo('Para não confundir: <strong>hierárquico</strong> = <strong>ordenar</strong>; <strong>disciplinar</strong> = <strong>punir quem tem vínculo</strong>; <strong>de polícia</strong> = <strong>limitar o cidadão comum</strong>; <strong>regulamentar</strong> = <strong>detalhar a lei</strong>.') +
 table(["Dica de memorização","Para lembrar"],[
  ["“Vi Di Hi Di Re Po”","Os seis poderes"],["“NoRE”","Indelegáveis: atos Normativos, Recursos e matérias Exclusivas"],
  ["“DAC”","Atributos do poder de polícia: Discricionariedade, Autoexecutoriedade, Coercibilidade"],
  ["“OCFS”","Ciclo de polícia: Ordem, Consentimento, Fiscalização, Sanção"],
  ["“Excesso = Extrapola a competência; Desvio = Destino errado”","Espécies de abuso de poder"]],["44%",None]))

add('<div class="unit"><span class="u">REVISÃO</span><span class="t">Erros mais comuns</span></div><h1 class="big">Os erros <span class="hl">mais comuns</span> nas provas</h1><p class="lead">Afirmações erradas que costumam aparecer em questões. Ao lado, o que está certo.</p>' +
 table(["Afirmação errada","O certo é"],[
  ["“Discricionariedade é sinônimo de arbitrariedade.”","Discricionário é escolher dentro da lei; arbitrário é agir fora dela."],
  ["“O Judiciário pode revogar ato discricionário.”","Pode <b>anular</b> o ilegal; revogar é da Administração."],
  ["“Há hierarquia entre a União e suas autarquias.”","Há controle finalístico, não hierarquia."],
  ["“Delegação só para subordinados.”","Pode ser feita a órgão não subordinado (Lei nº 9.784/1999, art. 12)."],
  ["“Recursos administrativos podem ser decididos por delegação.”","A decisão de recursos é indelegável (art. 13, II)."],
  ["“Multar o cidadão comum é poder disciplinar.”","É poder de polícia; o disciplinar exige vínculo especial."],
  ["“Decreto pode criar obrigação nova.”","Regulamento não inova; obrigação depende de lei."],
  ["“Decreto autônomo pode extinguir cargos ocupados.”","Só cargos ou funções <b>vagos</b> (CF, art. 84, VI, b)."]],["46%",None]))

add(pratica_title("Erros mais comuns (continuação)") +
 table(["Afirmação errada","O certo é"],[
  ["“Polícia administrativa atua sobre pessoas.”","Atua sobre bens, direitos e atividades; a judiciária, sobre pessoas."],
  ["“O poder de polícia é sempre discricionário.”","Em regra, sim, mas há atos vinculados, como a licença."],
  ["“A multa de polícia pode ser cobrada à força pela Administração.”","A cobrança forçada depende de execução judicial."],
  ["“Empresa privada contratada pode aplicar multas de trânsito.”","Só entidade da Administração indireta que preencha os requisitos do Tema 532."],
  ["“Guarda municipal não pode multar no trânsito.”","O STF admitiu o poder de polícia de trânsito das guardas (Tema 472)."],
  ["“Excesso de poder é agir com fim diverso do previsto.”","Isso é desvio de finalidade; excesso é ir além da competência."],
  ["“Abuso de poder só ocorre por ação.”","A omissão também pode configurar abuso."],
  ["“O servidor deve cumprir qualquer ordem superior.”","Exceto as manifestamente ilegais (Lei nº 8.112/1990, art. 116, IV)."]],["46%",None]))

FC = [("NOÇÕES","Por que se fala em poder-dever?","Porque o administrador tem o dever de exercer o poder quando a lei exige; a competência é irrenunciável."),
 ("NOÇÕES","Quais são os seis poderes cobrados?","Vinculado, discricionário, hierárquico, disciplinar, regulamentar e de polícia."),
 ("VINCULADO","O que caracteriza o poder vinculado?","A lei define todos os elementos; cumpridos os requisitos, o ato é obrigatório."),
 ("DISCRICIONÁRIO","O que é mérito administrativo?","A avaliação de conveniência e oportunidade dentro da lei."),
 ("DISCRICIONÁRIO","O Judiciário controla o mérito?","Não. Controla a legalidade, inclusive razoabilidade e proporcionalidade."),
 ("DISCRICIONÁRIO","Teoria dos motivos determinantes?","O motivo declarado vincula o ato; motivo falso o torna nulo."),
 ("HIERÁRQUICO","O que o poder hierárquico permite?","Ordenar, fiscalizar, rever, delegar e avocar."),
 ("HIERÁRQUICO","O que não pode ser delegado?","Atos normativos, decisão de recursos e matérias exclusivas (art. 13 da Lei 9.784)."),
 ("HIERÁRQUICO","Requisitos da avocação?","Temporária, excepcional, motivos relevantes justificados, de órgão inferior."),
 ("DISCIPLINAR","A quem se aplica o poder disciplinar?","Servidores e particulares com vínculo especial (ex.: contratados)."),
 ("DISCIPLINAR","Penalidades da Lei 8.112?","Advertência, suspensão, demissão, cassação, destituição de cargo em comissão e de função comissionada."),
 ("DISCIPLINAR","Apurar irregularidade é obrigatório?","Sim (Lei 8.112, art. 143), por sindicância ou PAD, com ampla defesa."),
 ("REGULAMENTAR","Base do decreto regulamentar?","CF, art. 84, IV: fiel execução das leis."),
 ("REGULAMENTAR","Hipóteses do decreto autônomo?","Organização da administração sem despesa nem criação/extinção de órgãos; extinção de cargos vagos."),
 ("REGULAMENTAR","Quem susta o regulamento que exorbita?","O Congresso Nacional (CF, art. 49, V)."),
 ("POLÍCIA","Onde está o conceito legal de poder de polícia?","No art. 78 do CTN."),
 ("POLÍCIA","Polícia administrativa x judiciária?","Administrativa: bens e atividades, ilícito administrativo. Judiciária: pessoas, ilícito penal."),
 ("POLÍCIA","Fases do ciclo de polícia?","Ordem, consentimento, fiscalização e sanção."),
 ("POLÍCIA","Atributos do poder de polícia?","Discricionariedade, autoexecutoriedade e coercibilidade."),
 ("POLÍCIA","Prazo da ação punitiva federal no poder de polícia?","5 anos (Lei 9.873/1999)."),
 ("ABUSO","Espécies de abuso de poder?","Excesso de poder e desvio de finalidade."),
 ("ABUSO","Excesso de poder?","Agir além da competência."),
 ("ABUSO","Desvio de finalidade?","Agir dentro da competência, mas com fim diverso do previsto (Lei 4.717, art. 2º)."),
 ("ABUSO","Remédio contra abuso de autoridade pública que fere direito líquido e certo?","Mandado de segurança (CF, art. 5º, LXIX).")]
def fcpage(items, first):
    cs = "".join(f'<div class="c"><div class="f"><small>{a}</small>{q}</div><div class="b">{r}</div></div>' for a,q,r in items)
    h = ('<div class="marker">§§R2§§</div><div class="unit"><span class="u">REVISÃO ATIVA</span></div><h1 class="big">Flash<span class="hl">cards</span></h1><p class="lead">Cubra a resposta, tente lembrar e confira. Revise em 1, 3, 7, 15 e 30 dias.</p>' if first else '')
    return h + f'<div class="fc">{cs}</div>'
add(fcpage(FC[:12], True)); add(fcpage(FC[12:], False))

Q = [
 ("Conceito","Sobre os poderes administrativos, é correto afirmar:",
  ["são privilégios pessoais do agente público.","são prerrogativas instrumentais, de exercício obrigatório quando a lei exige, e irrenunciáveis.","podem ser renunciados livremente pelo agente.","só existem no Poder Executivo federal.","dispensam observância da lei quando o interesse público é relevante."],"B",
  "Os poderes são instrumentos para o interesse público (poder-dever), irrenunciáveis (Lei nº 9.784/1999, art. 11) e sempre limitados pela lei.","Poder-dever, instrumental, irrenunciável."),
 ("Vinculado","Servidor apresenta pedido de licença cumprindo todos os requisitos legais, e a lei não deixa margem de escolha à Administração. Trata-se de exercício de poder:",
  ["discricionário, pois a Administração pode negar por conveniência.","vinculado: cumpridos os requisitos, o ato deve ser praticado.","hierárquico.","regulamentar.","de polícia judiciária."],"B",
  "No poder vinculado, a lei define todos os elementos do ato, e o agente não tem escolha.","Requisitos cumpridos = ato obrigatório."),
 ("Discricionário","O núcleo do poder discricionário, formado pela avaliação de conveniência e oportunidade, denomina-se:",
  ["motivação.","mérito administrativo.","autoexecutoriedade.","coercibilidade.","presunção de legitimidade."],"B",
  "Mérito administrativo é a escolha, dentro da lei, segundo conveniência e oportunidade, que o Judiciário não substitui.","Mérito = conveniência + oportunidade."),
 ("Discricionário","Quanto ao controle judicial dos atos discricionários, é correto afirmar que o Poder Judiciário:",
  ["não pode examiná-los em nenhum aspecto.","pode revogá-los quando inconvenientes.","pode anulá-los se ilegais, desproporcionais ou baseados em motivo inexistente, sem substituir o mérito.","pode substituir a escolha do administrador pela que considerar melhor.","só os examina se houver autorização do Chefe do Executivo."],"C",
  "O controle é de legalidade (inclusive razoabilidade, proporcionalidade e motivos); revogação e escolha de mérito cabem à Administração.","Judiciário anula; não revoga."),
 ("Motivos determinantes","A autoridade nega autorização de uso de uma praça alegando que ela estará em reforma, mas não há reforma prevista. O ato:",
  ["é válido, porque a autorização é discricionária.","é nulo, pela teoria dos motivos determinantes.","é válido, porque a motivação não era obrigatória.","só pode ser revogado pela própria autoridade.","é inexistente."],"B",
  "O motivo declarado vincula o ato: se é falso ou inexistente, o ato é nulo, ainda que a motivação fosse facultativa.","Motivo falso = ato nulo."),
 ("Hierárquico","NÃO decorre do poder hierárquico:",
  ["dar ordens aos subordinados.","fiscalizar a atuação dos subordinados.","rever atos dos subordinados.","avocar competências de órgão inferior.","controlar autarquia vinculada como se fosse subordinada."],"E",
  "Entre a Administração direta e a indireta não há hierarquia, mas controle finalístico (tutela).","Direta x indireta: tutela, não hierarquia."),
 ("Delegação","Segundo a Lei nº 9.784/1999, não pode ser objeto de delegação:",
  ["a assinatura de ofícios.","a decisão de recursos administrativos.","a análise de pedidos de férias.","a fiscalização de contratos.","a emissão de certidões."],"B",
  "Art. 13: são indelegáveis a edição de atos normativos, a decisão de recursos administrativos e as matérias de competência exclusiva.","NoRE: Normativos, Recursos, Exclusivos."),
 ("Avocação","A avocação de competência, segundo a Lei nº 9.784/1999:",
  ["é permanente e dispensa justificativa.","pode ser feita em relação a órgão de mesma hierarquia.","é temporária, excepcional e exige motivos relevantes devidamente justificados.","é proibida em qualquer hipótese.","só pode ser feita por decisão judicial."],"C",
  "Art. 15: avocação temporária de competência de órgão hierarquicamente inferior, em caráter excepcional e por motivos relevantes justificados.","Avocação: temporária e justificada."),
 ("Disciplinar","Empresa contratada pela Prefeitura descumpre cláusula do contrato e recebe multa contratual. A sanção decorre do poder:",
  ["de polícia.","disciplinar.","regulamentar.","hierárquico.","vinculado apenas."],"B",
  "O poder disciplinar alcança servidores e particulares com vínculo especial com a Administração, como os contratados.","Vínculo especial = disciplinar."),
 ("Disciplinar","Sobre o poder disciplinar, é INCORRETO afirmar:",
  ["a autoridade que toma ciência de irregularidade é obrigada a apurá-la.","a aplicação de penalidade exige contraditório e ampla defesa.","o ato de punição deve indicar o fundamento legal e a causa da sanção.","a advertência e a suspensão estão entre as penalidades da Lei nº 8.112/1990.","a autoridade pode deixar de apurar irregularidade por conveniência."],"E",
  "A apuração é obrigatória (Lei nº 8.112/1990, art. 143).","Apurar é dever."),
 ("Disciplinar x polícia","Vigilância sanitária multa restaurante sem qualquer vínculo contratual com a Administração. Trata-se de poder:",
  ["disciplinar.","hierárquico.","de polícia.","regulamentar.","normativo autônomo."],"C",
  "Limitar a atividade de particular sem vínculo especial é poder de polícia; o disciplinar exige vínculo especial.","Cidadão comum = polícia."),
 ("Regulamentar","O poder regulamentar:",
  ["permite ao Executivo criar obrigações não previstas em lei.","destina-se à fiel execução das leis e não pode inovar na ordem jurídica.","é exercido exclusivamente pelo Poder Legislativo.","não está sujeito a controle.","pode ser livremente delegado a qualquer servidor."],"B",
  "CF, art. 84, IV. Se exorbitar, o Congresso pode sustar o ato (art. 49, V).","Regulamento: fiel execução, sem inovar."),
 ("Regulamentar","Compete ao Congresso Nacional, em relação aos atos normativos do Executivo que exorbitem do poder regulamentar:",
  ["revogá-los.","anulá-los com efeitos retroativos, sempre.","sustá-los.","ratificá-los.","convertê-los em lei."],"C",
  "CF, art. 49, V: sustar os atos normativos do Poder Executivo que exorbitem do poder regulamentar ou dos limites de delegação legislativa.","Congresso susta."),
 ("Decreto autônomo","O Presidente da República pode, mediante decreto autônomo:",
  ["criar órgãos públicos.","extinguir cargos públicos ocupados.","dispor sobre organização da administração federal, sem aumento de despesa nem criação ou extinção de órgãos.","criar tributos.","definir crimes."],"C",
  "CF, art. 84, VI, a e b: organização sem aumento de despesa nem criação/extinção de órgãos, e extinção de cargos ou funções vagos.","Autônomo: só duas hipóteses."),
 ("Polícia","O conceito legal de poder de polícia encontra-se:",
  ["na Lei nº 8.112/1990.","no art. 78 do Código Tributário Nacional.","na Lei nº 9.784/1999.","no Código de Processo Penal.","na Lei nº 13.869/2019."],"B",
  "O art. 78 do CTN define o poder de polícia; seu exercício regular fundamenta a cobrança de taxas (art. 77).","Poder de polícia: CTN, art. 78."),
 ("Polícia","Sobre polícia administrativa e polícia judiciária, assinale a correta:",
  ["a polícia administrativa incide sobre pessoas, e a judiciária sobre bens.","a polícia administrativa atua sobre bens, direitos e atividades, em regra de forma preventiva; a judiciária, sobre pessoas, apurando ilícitos penais.","ambas regem-se pelo Código de Processo Penal.","a polícia judiciária é exercida pela vigilância sanitária.","as guardas municipais exercem polícia judiciária."],"B",
  "Administrativa: bens, direitos e atividades, ilícito administrativo. Judiciária: pessoas, ilícito penal, exercida por Polícias Civis e Federal.","Administrativa: atividades; judiciária: pessoas."),
 ("Ciclo de polícia","A emissão de alvará de funcionamento corresponde, no ciclo de polícia, à fase de:",
  ["ordem.","consentimento.","fiscalização.","sanção.","regulamentação."],"B",
  "O consentimento é a anuência estatal ao exercício da atividade (licença ou autorização).","Alvará = consentimento."),
 ("Delegação de polícia","Segundo o STF (Tema 532), a delegação do poder de polícia, inclusive para aplicar multas:",
  ["é proibida em qualquer hipótese.","pode ser feita por decreto a qualquer empresa privada.","é constitucional, por lei, a pessoas jurídicas de direito privado da Administração indireta, de capital majoritariamente público, que prestem serviço público próprio do Estado em regime não concorrencial.","alcança a fase de ordem de polícia.","depende apenas de contrato administrativo."],"C",
  "RE 633.782 (2020). A ordem de polícia, que depende de lei, não é delegada.","Tema 532: estatal com os requisitos, por lei."),
 ("Atributos","A Administração apreende e descarta imediatamente alimentos estragados à venda, sem ordem judicial. Manifesta-se o atributo da:",
  ["presunção de veracidade.","autoexecutoriedade.","tipicidade.","imperatividade normativa.","especialidade."],"B",
  "Autoexecutoriedade: executar a decisão sem prévia ordem judicial, quando a lei autoriza ou em urgência.","Sem juiz = autoexecutoriedade."),
 ("Guardas municipais","De acordo com o STF, a atribuição às guardas municipais do poder de polícia de trânsito, inclusive para impor sanções administrativas:",
  ["é inconstitucional.","é constitucional (Tema 472).","depende de autorização do Detran estadual em cada autuação.","só vale em capitais.","é exclusiva das polícias militares."],"B",
  "RE 658.570 (2015): é constitucional a atribuição às guardas municipais do exercício do poder de polícia de trânsito, inclusive para imposição de sanções administrativas legalmente previstas.","Guarda pode multar no trânsito."),
 ("Abuso","Agente público que pratica ato fora dos limites de sua competência incorre em:",
  ["desvio de finalidade.","excesso de poder.","omissão abusiva.","mérito administrativo.","discricionariedade."],"B",
  "Excesso de poder é vício de competência; desvio de finalidade é vício de finalidade.","Excesso = competência."),
 ("Desvio de finalidade","O prefeito remove um servidor para local distante exclusivamente para puni-lo por críticas feitas à gestão. Configura-se:",
  ["excesso de poder.","desvio de finalidade.","ato vinculado válido.","exercício regular do poder hierárquico.","poder de polícia."],"B",
  "A remoção foi usada com fim diverso do previsto (punir), o que é desvio de finalidade (Lei nº 4.717/1965, art. 2º, parágrafo único, e).","Fim diverso = desvio."),
 ("Abuso","Sobre o abuso de poder, é correto afirmar:",
  ["só ocorre por ação, nunca por omissão.","é gênero, do qual são espécies o excesso de poder e o desvio de finalidade.","não gera responsabilidade do agente.","não pode ser combatido por mandado de segurança.","torna o ato apenas inconveniente, cabendo revogação."],"B",
  "O ato com abuso é nulo; a omissão também pode configurar abuso; cabe mandado de segurança (CF, art. 5º, LXIX).","Abuso: gênero com duas espécies."),
 ("Ordens ilegais","Diante de uma ordem superior manifestamente ilegal, o servidor regido pela Lei nº 8.112/1990:",
  ["deve cumpri-la, sob pena de insubordinação.","não está obrigado a cumpri-la e deve representar contra a ilegalidade.","deve cumpri-la e só depois reclamar.","pode cumpri-la parcialmente.","deve pedir exoneração."],"B",
  "Art. 116, IV: cumprir as ordens superiores, exceto quando manifestamente ilegais; inciso XII: representar contra ilegalidade, omissão ou abuso de poder.","Ordem manifestamente ilegal não se cumpre.")]

ALVO = "BCADBEACBEDBCEADBCAEBDCA"
for i,(tema,enun,alts,gab,com,mem) in enumerate(Q):
    a, b = "ABCDE".index(gab), "ABCDE".index(ALVO[i]); alts = list(alts); alts[a], alts[b] = alts[b], alts[a]
    Q[i] = (tema, enun, alts, ALVO[i], com, mem)
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
add('<div class="unit"><span class="u">CORREÇÃO</span><span class="t">Treinos rápidos</span></div><h1 class="big">Respostas dos <span class="hl">treinos</span></h1><p class="lead">Certo ou errado das Unidades 1 a 6.</p>' + tr_block(TREINOS[:2]))
add(tr_block(TREINOS[2:4])); add(tr_block(TREINOS[4:]))

add(f'''<div class="unit"><span class="u">ENCERRAMENTO</span></div><h1 class="big">Referências e <span class="hl">verificação</span></h1><p class="lead">De onde vieram as informações.</p>
<h3>Legislação consultada (portal do Planalto)</h3>
<ul>
<li>Constituição Federal: art. 5º (II, XXXIV, XXXV, LV, LXVIII e LXIX), art. 49, V, e art. 84 (IV, VI e parágrafo único).</li>
<li>Código Tributário Nacional (Lei nº 5.172/1966): arts. 77 e 78.</li>
<li>Lei nº 4.717/1965 (Ação Popular): art. 2º.</li>
<li>Lei nº 9.784/1999: arts. 11 a 17, 50 e 56.</li>
<li>Lei nº 8.112/1990: arts. 116, 127, 128, 130, 143 e 145.</li>
<li>Lei nº 9.873/1999: art. 1º.</li>
<li>Citadas sem conferência nesta edição: CF, art. 37, § 6º; Lei nº 13.869/2019 (conferida para o Caderno 08).</li>
</ul>
<h3>Jurisprudência citada (identificada em pesquisa)</h3><ul><li>STF: RE 633.782 (Tema 532, delegação do poder de polícia, 2020); RE 658.570 (Tema 472, guardas municipais e trânsito, 2015); RE 608.588 (Tema 656, guardas municipais, 2025).</li></ul>''' + lembre(p(f'<strong>Material pesquisado e atualizado em: {DATA}.</strong> A base legal foi conferida nos textos do portal do Planalto, que exibem a redação vigente com as notas de alteração. <strong>Limitações:</strong> os textos do Planalto não informam a data da última atualização e não substituem o Diário Oficial. A classificação dos poderes, a ideia de poder-dever, o ciclo de polícia, os atributos do poder de polícia, a teoria dos motivos determinantes e a omissão abusiva são <strong>construções doutrinárias</strong>, apresentadas na forma mais aceita. A jurisprudência foi identificada em publicações e não foi reconferida nos portais oficiais dos tribunais; a redação exata da tese do Tema 532 varia entre as fontes consultadas. Confira o edital do seu concurso.'), "Verificação e limitações"))
add('''<div class="ending"><h2>Fim do Caderno 10</h2><p style="text-align:center">Sugestão de continuação em Direito Administrativo: <strong>atos administrativos</strong> (requisitos, atributos, classificação e extinção).</p>
<p class="note" style="text-align:center">Mapa da Aprovação · Caderno Simplificado · Direito Administrativo · Caderno 10 · 1ª edição · novembro de 2026<br>Material de estudo independente. Não substitui a leitura da lei e do edital do seu concurso.</p></div>''')

doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Mapa da Aprovação — Caderno 10 — Poderes Administrativos</title>
<link rel="stylesheet" href="estilo.css"></head><body>{symbols()}{"".join(P)}</body></html>'''
open(os.path.join(HERE, "miolo.html"), "w").write(doc)
print("páginas planejadas:", len(P))
