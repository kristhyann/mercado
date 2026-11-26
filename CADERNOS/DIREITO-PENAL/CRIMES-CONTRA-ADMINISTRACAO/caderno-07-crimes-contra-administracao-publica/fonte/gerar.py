"""Gera miolo.html do Caderno 07: Crimes contra a Administração Pública. Uso: python3 gerar.py
Tipos penais e penas conferidos no texto compilado do Código Penal (Planalto) em 26/11/2026 (arts. 312 a 359)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from componentes import *

DATA = "26 de novembro de 2026"
P = []
def add(html, first=False): P.append(page(f'<div class="marker">§§P{len(P)+1:03d}§§</div>' + html, first))
U = {1:("UNIDADE 1","Noções gerais"),2:("UNIDADE 2","Crimes do funcionário público"),3:("UNIDADE 3","Crimes do particular"),4:("UNIDADE 4","Administração da Justiça")}
def H(u, title, lead, marker=None): return head(U[u][0], U[u][1], title, lead, marker)
def cp(x): return f"{x} · Código Penal"
def p(t): return f"<p>{t}</p>"
def colors(*keys):
    m = {"b":(C['blue'],C['sky']),"g":(C['green'],C['greensoft']),"o":(C['golddeep'],C['goldsoft']),"r":(C['red'],C['redsoft']),"n":(C['navy'],'#e6e7ea')}
    return [m[k] for k in keys]
def atencao(html, kws=None, t='Atenção na prova'):
    add(pratica_title(t) + html + (kw(kws) if kws else ''))
def scene3(items, cap):
    """Três quadros ilustrados lado a lado: (título, cor, cor-fundo, personagem, balão[linhas], legenda)."""
    s = f'<figure><svg viewBox="0 0 640 260" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    for i,(t,fg,bg,who,lines,leg) in enumerate(items):
        x = i*214
        s += f'<rect x="{x+2}" y="2" width="206" height="256" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x+105}" y="26" text-anchor="middle" font-weight="900" font-size="14" fill="{fg}">{t}</text>'
        s += f'<rect x="{x+14}" y="38" width="182" height="{20+len(lines)*17}" rx="12" fill="#fff" stroke="{fg}" stroke-width="1.8"/>'
        s += "".join(f'<text x="{x+105}" y="{58+j*17}" text-anchor="middle" font-size="11.2" font-weight="800" fill="{C["ink"]}">{l}</text>' for j,l in enumerate(lines))
        s += f'<g transform="translate({x+70},{70+len(lines)*17})"><svg viewBox="0 0 100 170" width="62" height="105"><use href="#ch-{who}"/></svg></g>'
        s += f'<text x="{x+105}" y="244" text-anchor="middle" font-size="11" font-weight="900" fill="{fg}">{leg}</text>'
    return s + f'</svg><figcaption>{cap}</figcaption></figure>'
NV = '#e6e7ea'

# ================================================================ APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">Os crimes contra a Administração Pública explicados pelas diferenças entre eles, com o foco das provas policiais e de nível médio.</p>
<p>Este é o <strong>Caderno 07 da coleção</strong>, dedicado aos <strong>crimes contra a Administração Pública</strong> (Título XI da Parte Especial do Código Penal, arts. 312 a 359-H). É um assunto obrigatório nos editais de <strong>Guarda Municipal</strong>, das <strong>polícias</strong> e de muitos cargos administrativos, porque trata do que o próprio servidor não pode fazer e do que o cidadão não pode fazer contra o servidor.</p>
<p>A dificuldade das provas não está em decorar penas, e sim em <strong>separar crimes parecidos</strong>: peculato e furto; concussão e corrupção passiva; corrupção passiva e prevaricação; resistência, desobediência e desacato; contrabando e descaminho; denunciação caluniosa e comunicação falsa de crime. Por isso o caderno tem <strong>cenas ilustradas</strong>, <strong>tabelas de diferenciação</strong>, um <strong>roteiro de decisão</strong> e uma seção só com os <strong>erros mais comuns</strong>.</p>
{lembre(p(f'<strong>Todos os tipos penais e todas as penas deste caderno foram conferidos no texto compilado do Código Penal, no portal do Planalto, em {DATA}</strong> (arts. 312 a 359). Destaques recentes: o <strong>art. 338-A</strong> (descumprimento de medidas protetivas de urgência), incluído pela Lei nº 15.280/2025, e a decisão do STF na <strong>ADPF 496</strong> sobre o desacato. As limitações da pesquisa estão na página de referências.'), "Fontes e atualização")}
{table(["Recurso","Onde está"],[["Cenas: exigir x solicitar x oferecer","Unidade 2"],["Roteiro de decisão: qual é o crime?","Unidade 2"],["Cenas: resistência x desobediência x desacato","Unidade 3"],["Cenas: denunciação caluniosa x comunicação falsa x autoacusação","Unidade 4"],["Erros mais comuns nas provas e tabela-mestra de penas","Revisão"],["24 questões autorais comentadas e treinos Certo ou Errado","Prática final e fim das unidades"]],["56%",None])}''', first=True)

TOC = [("u","UNIDADE 1 · NOÇÕES GERAIS","U1"),("","1. Conceito e organização do Título XI","A01"),("","2. Funcionário público para fins penais (art. 327)","A02"),("","3. Crimes funcionais próprios e impróprios","A03"),
 ("u","UNIDADE 2 · CRIMES PRATICADOS POR FUNCIONÁRIO PÚBLICO","U2"),("","4. Peculato doloso (art. 312)","A04"),("","5. Peculato culposo e peculato mediante erro de outrem","A05"),("","6. Inserção de dados falsos e modificação de sistema","A06"),("","7. Concussão e excesso de exação (art. 316)","A07"),("","8. Corrupção passiva (art. 317)","A08"),("","9. Exigir x solicitar x oferecer: qual é o crime?","A09"),("","10. Prevaricação (arts. 319 e 319-A)","A10"),("","11. Condescendência, advocacia administrativa e sigilo funcional","A11"),("","12. Outros crimes funcionais","A12"),
 ("u","UNIDADE 3 · CRIMES PRATICADOS POR PARTICULAR","U3"),("","13. Usurpação de função pública","A13"),("","14. Resistência (art. 329)","A14"),("","15. Desobediência (art. 330)","A15"),("","16. Desacato e a controvérsia da ADPF 496","A16"),("","17. Resistência x desobediência x desacato","A17"),("","18. Tráfico de influência e corrupção ativa","A18"),("","19. Contrabando x descaminho","A19"),
 ("u","UNIDADE 4 · ADMINISTRAÇÃO DA JUSTIÇA E OUTROS CRIMES","U4"),("","20. Denunciação caluniosa x comunicação falsa x autoacusação falsa","A20"),("","21. Falso testemunho e coação no curso do processo","A21"),("","22. Exercício arbitrário e favorecimentos","A22"),("","23. Medidas protetivas, celular em presídio e fuga de preso","A23"),("","24. Noções de crimes em licitações","A24"),
 ("u","REVISÃO E PRÁTICA","RV"),("","Mapa conceitual · Erros mais comuns · Tabela de penas","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),("","Gabarito, respostas dos treinos e referências","R4")]
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
opener("01","UNIDADE 1","Noções gerais",["Conceito e organização do Título XI","Funcionário público para fins penais","Crimes funcionais próprios e impróprios"],"U1")

def tit_xi():
    caps = [("CAP. I","Funcionário público","contra a Administração","em geral · arts. 312 a 327",C['red'],C['redsoft']),
            ("CAP. II","Particular","contra a Administração","em geral · arts. 328 a 337-A",C['golddeep'],C['goldsoft']),
            ("CAP. II-A","Particular contra a","Administração Pública","estrangeira · 337-B a 337-D",C['navy'],NV),
            ("CAP. II-B","Licitações e","contratos administrativos","arts. 337-E a 337-P",C['navy'],NV),
            ("CAP. III","Administração","da Justiça","arts. 338 a 359",C['golddeep'],C['goldsoft']),
            ("CAP. IV","Finanças","públicas","arts. 359-A a 359-H",C['navy'],NV)]
    s = f'<figure><svg viewBox="0 0 640 300" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    s += f'<rect x="170" y="4" width="300" height="50" rx="12" fill="{C["navy"]}"/><text x="320" y="25" text-anchor="middle" font-size="13" font-weight="900" fill="{C["gold"]}">TÍTULO XI DO CÓDIGO PENAL</text><text x="320" y="44" text-anchor="middle" font-size="12" font-weight="800" fill="#fff">Crimes contra a Administração Pública</text>'
    s += '<g stroke="#b9b3ad" stroke-width="2.2" fill="none"><path d="M320 54 V78 M110 78 H530 M110 78 V96 M320 78 V96 M530 78 V96 M110 186 V200 M320 186 V200 M530 186 V200"/></g>'
    for i,(k,a,b,c,fg,bg) in enumerate(caps):
        x = 20 + (i%3)*210; y = 96 + (i//3)*110
        s += f'<rect x="{x}" y="{y}" width="180" height="90" rx="12" fill="{bg}" stroke="{fg}" stroke-width="2.4"/><text x="{x+90}" y="{y+20}" text-anchor="middle" font-size="11.5" font-weight="900" fill="{fg}">{k}</text>'
        s += f'<text x="{x+90}" y="{y+40}" text-anchor="middle" font-size="12" font-weight="800" fill="{C["ink"]}">{a}</text><text x="{x+90}" y="{y+56}" text-anchor="middle" font-size="12" font-weight="800" fill="{C["ink"]}">{b}</text><text x="{x+90}" y="{y+76}" text-anchor="middle" font-size="10.5" fill="{C["muted"]}">{c}</text>'
    return s + '</svg><figcaption>Como o Código Penal organiza os crimes contra a Administração Pública. Em vermelho e laranja, o foco deste caderno.</figcaption></figure>'

add(H(1,'O que são crimes contra a <span class="hl">Administração Pública</span>','O bem protegido é o bom funcionamento do Estado.', "A01") +
 oque(p('São condutas que atingem o <strong>funcionamento regular, a moralidade e o patrimônio</strong> da Administração Pública. Podem ser praticadas pelo <strong>próprio servidor</strong> (o "inimigo interno") ou por um <strong>particular</strong> que atrapalha, engana ou corrompe o Estado.')) +
 tit_xi() +
 traduz(p('Pense no Estado como uma grande empresa de todos. O Código Penal protege essa empresa de dois lados: de quem <strong>trabalha dentro dela</strong> e abusa do cargo (Capítulo I) e de quem está <strong>do lado de fora</strong> e tenta corrompê-la, enganá-la ou impedir seu trabalho (Capítulo II). A Justiça, que também é parte do Estado, ganhou um capítulo próprio (Capítulo III).')) +
 memo('Capítulo I: crimes do <strong>funcionário</strong> (312 a 327). Capítulo II: crimes do <strong>particular</strong> (328 a 337-A). Capítulo III: crimes contra a <strong>Administração da Justiça</strong> (338 a 359).'))

add(H(1,'Funcionário público <span class="hl">para fins penais</span>','Art. 327: um conceito bem mais amplo que o do Direito Administrativo.', "A02") +
 lei(cp("Art. 327, caput"),'<p>Art. 327 - Considera-se funcionário público, para os efeitos penais, quem, embora transitoriamente ou sem remuneração, exerce cargo, emprego ou função pública.</p>') +
 table(["Regra","Conteúdo (em síntese)"],[
  ["Conceito (caput)","Exercer <b>cargo, emprego ou função pública</b>, ainda que de forma <b>transitória</b> ou <b>sem remuneração</b>"],
  ["Equiparação (§ 1º, Lei nº 9.983/2000)","Quem exerce cargo, emprego ou função em <b>entidade paraestatal</b>, e quem trabalha para <b>empresa prestadora de serviço contratada ou conveniada</b> para executar atividade típica da Administração"],
  ["Aumento de pena (§ 2º, Lei nº 6.799/1980)","Pena aumentada da <b>terça parte</b> quando o autor ocupa <b>cargo em comissão</b> ou <b>função de direção ou assessoramento</b> em órgão da administração direta, sociedade de economia mista, empresa pública ou fundação instituída pelo poder público"]],["30%",None]) +
 traduz(p('Para o Direito Penal, não importa se a pessoa é concursada, se recebe salário ou se ficará só um dia na função. Importa se ela <strong>exerce uma função pública</strong>. Por isso o <strong>mesário</strong> da eleição e o <strong>jurado</strong> do Tribunal do Júri são funcionários públicos para fins penais enquanto exercem a função.'),"profa") +
 memo('<strong>Transitoriamente</strong> ou <strong>sem remuneração</strong>: continua sendo funcionário público para o CP. Comissão, direção ou assessoramento: pena <strong>+1/3</strong>.'))

atencao(
 flow([("idcard",["CONCURSADO","cargo efetivo"]),("ballot",["MESÁRIO","função transitória,","sem salário"]),("briefcase",["TERCEIRIZADO","empresa contratada","p/ atividade típica"]),("gavel",["TODOS SÃO","funcionários","públicos (art. 327)"])],
      "Para o Código Penal, o que conta é o exercício da função pública.", colors=colors("n","o","b","r")) +
 ex(p('Um vigilante de empresa <b>terceirizada</b>, contratada pela prefeitura para fazer a segurança de uma escola, subtrai notebooks da sala de informática aproveitando a facilidade do posto. Pela equiparação do § 1º do art. 327, ele pode responder como funcionário público, e o fato pode configurar <b>peculato-furto</b> (art. 312, § 1º), e não furto comum.')) +
 pega('<ul><li>O conceito penal é <b>mais amplo</b> que o administrativo: quem exerce função pública <b>sem remuneração</b> também é alcançado.</li><li>O aumento do § 2º é de <b>um terço</b> ("terça parte"), e não de metade.</li><li>O particular que participa do crime junto com o funcionário, <b>sabendo dessa condição</b>, responde pelo mesmo crime funcional, porque a condição de funcionário é <b>elementar</b> do tipo e se comunica (art. 30 do CP).</li></ul>'),
 ["cargo, emprego ou função","transitoriamente","sem remuneração","paraestatal","empresa contratada ou conveniada","terça parte"])

add(H(1,'Crimes funcionais <span class="hl">próprios e impróprios</span>','Uma classificação doutrinária que ajuda a entender as diferenças.', "A03") +
 table(["","FUNCIONAL PRÓPRIO","FUNCIONAL IMPRÓPRIO"],[
  ["Ideia","Sem a condição de funcionário, o fato <b>não é crime</b> (é atípico)","Sem a condição de funcionário, o fato <b>vira outro crime</b>"],
  ["Exemplos","Prevaricação, concussão, condescendência criminosa","Peculato (sem a condição de funcionário, seria furto ou apropriação indébita)"],
  ["Como identificar","Retire o funcionário da cena: sobra algum crime?","Retire o funcionário da cena: sobra um crime comum"]],["18%",None,None]) +
 lembre(p('<strong>Súmula 599 do STJ:</strong> "O princípio da insignificância é inaplicável aos crimes contra a administração pública." A jurisprudência abre exceção para o <strong>descaminho</strong>, crime tributário em que se usa um parâmetro de valor. O STF não adota a súmula de forma automática e já analisou casos concretos de forma diferente.'), "Insignificância e crimes contra a Administração") +
 memo('Funcional <strong>próprio</strong>: tirou o funcionário, <strong>não sobra crime</strong>. Funcional <strong>impróprio</strong>: tirou o funcionário, <strong>sobra crime comum</strong>. Insignificância: em regra, <strong>não se aplica</strong> (Súmula 599 do STJ), salvo no descaminho.') +
 pega('<ul><li>A classificação em próprio e impróprio é <b>doutrinária</b>: a lei não usa esses nomes.</li><li>Não generalize a Súmula 599 para o <b>descaminho</b>: nele, a jurisprudência admite a insignificância.</li></ul>'))

treino(1, [
 ("Para os efeitos penais, quem exerce função pública sem remuneração não é considerado funcionário público.","E","É funcionário público, ainda que transitoriamente ou sem remuneração (art. 327)."),
 ("Equipara-se a funcionário público quem trabalha para empresa prestadora de serviço contratada para a execução de atividade típica da Administração Pública.","C","Art. 327, § 1º."),
 ("A pena é aumentada da metade quando o autor ocupa cargo em comissão em órgão da administração direta.","E","O aumento é da terça parte (art. 327, § 2º)."),
 ("Os crimes praticados por particular contra a Administração em geral estão no Capítulo II do Título XI.","C","Arts. 328 a 337-A."),
 ("Segundo a Súmula 599 do STJ, o princípio da insignificância é inaplicável aos crimes contra a Administração Pública.","C","Com a exceção jurisprudencial do descaminho."),
 ("O mesário de eleição, enquanto exerce a função, pode ser considerado funcionário público para fins penais.","C","Exerce função pública, ainda que transitoriamente e sem remuneração.")])

# ================================================================ UNIDADE 2
opener("02","UNIDADE 2","Crimes praticados por funcionário público",["Peculato doloso","Peculato culposo e mediante erro de outrem","Inserção de dados falsos e modificação de sistema","Concussão e excesso de exação","Corrupção passiva","Exigir x solicitar x oferecer","Prevaricação","Condescendência, advocacia administrativa e sigilo","Outros crimes funcionais"],"U2")

add(H(2,'<span class="hl">Peculato</span> doloso (art. 312)','Apropriar-se, desviar ou subtrair valendo-se do cargo.', "A04") +
 lei(cp("Art. 312, caput"),'<p>Art. 312 - Apropriar-se o funcionário público de dinheiro, valor ou qualquer outro bem móvel, público ou particular, de que tem a posse em razão do cargo, ou desviá-lo, em proveito próprio ou alheio:<br>Pena - reclusão, de dois a doze anos, e multa.</p>') +
 table(["Modalidade","O que o funcionário faz","Ele tinha a posse?"],[
  ["Peculato-apropriação (caput, 1ª parte)","Fica com o bem como se fosse dono","<b>Sim</b>, em razão do cargo"],
  ["Peculato-desvio (caput, 2ª parte)","Dá ao bem destino diferente do devido, em proveito próprio ou alheio","<b>Sim</b>, em razão do cargo"],
  ["Peculato-furto (§ 1º)","Subtrai, ou concorre para que outro subtraia, valendo-se da <b>facilidade</b> que o cargo proporciona","<b>Não</b>"]],["30%",None,"22%"]) +
 traduz(p('Peculato é o "furto ou a apropriação do servidor". O bem pode ser <strong>público ou particular</strong>: basta que esteja sob a guarda da Administração. Se o servidor já tinha o bem nas mãos por causa do cargo, é apropriação ou desvio; se não tinha, mas usou a facilidade do cargo para pegá-lo, é peculato-furto.')) +
 memo('Peculato: <strong>reclusão de 2 a 12 anos</strong>, e multa. Bem <strong>público ou particular</strong>. Com posse: apropriação ou desvio. Sem posse, com facilidade do cargo: <strong>peculato-furto</strong>.'))

atencao(
 flow([("wallet",["TESOUREIRO","guarda o dinheiro","da prefeitura"]),("coin",["FICA COM","R$ 8 mil","para si"]),("gavel",["PECULATO-","-APROPRIAÇÃO","art. 312, caput"])],
      "O funcionário tinha a posse em razão do cargo e passou a agir como dono.", colors=colors("n","o","r")) +
 ex(p('<b>Desvio:</b> o secretário municipal usa verba da merenda para pagar a festa de aniversário da filha. <b>Peculato-furto:</b> o servidor da recepção, que não guarda o almoxarifado, aproveita que conhece a senha do cadeado e leva caixas de material. <b>Bem particular:</b> o agente que fica com o celular apreendido de um preso também comete peculato, pois o bem estava sob a guarda da Administração.')) +
 pega('<ul><li>O bem do peculato pode ser <b>particular</b>, desde que esteja na posse do funcionário em razão do cargo.</li><li>No peculato-furto, o funcionário <b>não tem a posse</b>: ele se vale da <b>facilidade</b> do cargo.</li><li><b>Uso momentâneo</b> de bem infungível, com devolução (o chamado "peculato de uso"), segundo o entendimento majoritário não é crime do CP para o servidor comum, mas pode ser improbidade. Para prefeitos, há tipo próprio em lei especial (Decreto-Lei nº 201/1967).</li></ul>'),
 ["posse em razão do cargo","apropriar-se","desviar","facilidade do cargo","bem público ou particular","2 a 12 anos"])

add(H(2,'Peculato culposo e peculato <span class="hl">mediante erro de outrem</span>','Art. 312, §§ 2º e 3º, e art. 313.', "A05") +
 table(["Crime","Conduta (em síntese)","Pena"],[
  ["Peculato culposo (art. 312, § 2º)","O funcionário <b>concorre culposamente</b> (por descuido) para o crime de outrem","Detenção, 3 meses a 1 ano"],
  ["Peculato mediante erro de outrem (art. 313)","Apropriar-se de dinheiro ou qualquer utilidade que, no exercício do cargo, <b>recebeu por erro de outrem</b>","Reclusão, 1 a 4 anos, e multa"]],["30%",None,"24%"]) +
 lei(cp("Art. 312, § 3º (em síntese)"),'<p>No peculato culposo, a reparação do dano, se precede à sentença irrecorrível, extingue a punibilidade; se lhe é posterior, reduz de metade a pena imposta.</p>') +
 flow([("lock",["GUARDA ESQUECE","o cofre aberto","(culpa)"]),("mask2",["TERCEIRO","aproveita e","furta o dinheiro"]),("gavel",["GUARDA:","peculato culposo","(§ 2º)"])],
      "No peculato culposo, o descuido do funcionário facilita o crime de outra pessoa.", colors=colors("o","r","n")) +
 memo('Reparação do dano no peculato <strong>culposo</strong>: <strong>antes</strong> da sentença irrecorrível, <strong>extingue a punibilidade</strong>; <strong>depois</strong>, <strong>reduz a pena pela metade</strong>. Erro de outrem: o funcionário <strong>recebe por engano</strong> e fica com o valor (o chamado "peculato-estelionato").') +
 pega('<ul><li>O § 3º vale só para o peculato <b>culposo</b>. No doloso, a reparação não extingue a punibilidade.</li><li>No art. 313, o erro é <b>espontâneo</b> da vítima. Se o funcionário <b>provoca</b> o erro com fraude, não é esse crime.</li></ul>'))

add(H(2,'Dados falsos e <span class="hl">modificação de sistema</span>','Arts. 313-A e 313-B: o peculato da era digital.', "A06") +
 table(["","INSERÇÃO DE DADOS FALSOS (313-A)","MODIFICAÇÃO NÃO AUTORIZADA (313-B)"],[
  ["Quem pratica","<b>Funcionário autorizado</b> a operar o sistema","<b>Qualquer funcionário</b>"],
  ["Conduta","Inserir ou facilitar a inserção de dados falsos, ou alterar ou excluir indevidamente dados corretos","Modificar ou alterar sistema de informações ou programa de informática sem autorização ou solicitação de autoridade competente"],
  ["Finalidade","Obter vantagem indevida ou causar dano","Não exige finalidade especial"],
  ["Pena","Reclusão, 2 a 12 anos, e multa","Detenção, 3 meses a 2 anos, e multa (aumento de 1/3 até a metade se houver dano à Administração ou ao administrado)"]],["18%",None,None]) +
 ex(p('Uma servidora do órgão previdenciário, com senha de acesso ao sistema, cadastra um benefício em nome de pessoa que nunca contribuiu e divide os valores com ela: <b>inserção de dados falsos</b> (art. 313-A). Um servidor de outro setor que, sem autorização, altera o código do programa de protocolo para "pular" a fila: <b>modificação não autorizada de sistema</b> (art. 313-B).')) +
 memo('<strong>313-A</strong>: mexe nos <strong>dados</strong>, é funcionário <strong>autorizado</strong>, pena de <strong>2 a 12 anos</strong> (igual à do peculato). <strong>313-B</strong>: mexe no <strong>sistema ou programa</strong>, pena de <strong>detenção de 3 meses a 2 anos</strong>.') +
 pega('<ul><li>Dados x sistema: no 313-A o sistema continua igual e os <b>dados</b> são falsos; no 313-B o próprio <b>programa</b> é alterado.</li><li>Os dois artigos foram incluídos pela <b>Lei nº 9.983/2000</b>.</li></ul>'))

add(H(2,'<span class="hl">Concussão</span> e excesso de exação','Art. 316: o funcionário EXIGE.', "A07") +
 lei(cp("Art. 316, caput (redação da Lei nº 13.964/2019)"),'<p>Art. 316 - Exigir, para si ou para outrem, direta ou indiretamente, ainda que fora da função ou antes de assumi-la, mas em razão dela, vantagem indevida:<br>Pena - reclusão, de 2 (dois) a 12 (doze) anos, e multa.</p>') +
 table(["Forma","Conduta (em síntese)","Pena"],[
  ["Concussão (caput)","<b>Exigir</b> vantagem indevida em razão da função, mesmo fora dela ou antes de assumi-la","Reclusão, 2 a 12 anos, e multa"],
  ["Excesso de exação (§ 1º)","Exigir tributo ou contribuição social que sabe ou deveria saber <b>indevido</b>, ou empregar na cobrança meio <b>vexatório ou gravoso</b> que a lei não autoriza","Reclusão, 3 a 8 anos, e multa"],
  ["Excesso de exação qualificado (§ 2º)","<b>Desviar</b>, em proveito próprio ou de outrem, o que recebeu indevidamente para recolher aos cofres públicos","Reclusão, 2 a 12 anos, e multa"]],["24%",None,"22%"]) +
 traduz(p('Na concussão, o servidor <strong>impõe</strong>: usa o medo que o cargo provoca ("ou paga, ou eu prejudico você"). A vítima cede porque teme represálias. Por isso a vítima da concussão <strong>não comete crime</strong> ao pagar. O crime se consuma com a <strong>exigência</strong>, mesmo que o dinheiro nunca seja entregue.'),"profa") +
 memo('Concussão = <strong>EXIGIR</strong>. É crime <strong>formal</strong>: consuma-se com a exigência. Excesso de exação: cobrança de <strong>tributo indevido</strong> ou por <strong>meio vexatório</strong> (3 a 8 anos).'))

add(H(2,'Corrupção <span class="hl">passiva</span> (art. 317)','O funcionário SOLICITA, RECEBE ou ACEITA PROMESSA.', "A08") +
 lei(cp("Art. 317, caput"),'<p>Art. 317 - Solicitar ou receber, para si ou para outrem, direta ou indiretamente, ainda que fora da função ou antes de assumi-la, mas em razão dela, vantagem indevida, ou aceitar promessa de tal vantagem:<br>Pena - reclusão, de 2 (dois) a 12 (doze) anos, e multa.</p>') +
 table(["Forma","Conteúdo (em síntese)","Pena"],[
  ["Simples (caput)","Solicitar, receber ou aceitar promessa de vantagem indevida em razão da função","Reclusão, 2 a 12 anos, e multa"],
  ["Majorada (§ 1º)","Em consequência da vantagem ou promessa, o funcionário <b>retarda ou deixa de praticar</b> ato de ofício, ou o pratica <b>infringindo dever funcional</b>","Aumento de <b>1/3</b>"],
  ["Privilegiada (§ 2º)","Pratica, deixa de praticar ou retarda ato de ofício, com infração de dever funcional, <b>cedendo a pedido ou influência de outrem</b> (sem vantagem)","Detenção, 3 meses a 1 ano, ou multa"]],["22%",None,"22%"]) +
 ex(p('O fiscal de obras diz ao dono da construção: "Com um agrado de R$ 2 mil, eu não vejo as irregularidades" (<b>solicitar</b>). Outro fiscal, sem pedir nada, aceita o envelope que o construtor oferece (<b>receber</b>): corrupção passiva para o fiscal e corrupção ativa para o construtor. Se, por causa do dinheiro, o fiscal deixa de lavrar o auto de infração, incide o aumento de 1/3 do § 1º.')) +
 memo('Corrupção passiva = <strong>SOLICITAR, RECEBER ou ACEITAR PROMESSA</strong>. Ato de ofício efetivamente violado: <strong>+1/3</strong> (§ 1º). Cedeu a <strong>pedido de alguém</strong>, sem vantagem: forma <strong>privilegiada</strong> (§ 2º).'))

adm = scene3([("CONCUSSÃO",C['red'],C['redsoft'],"prof",["“Ou me paga","R$ 500, ou eu","interdito a loja.”"],"funcionário EXIGE"),
 ("CORRUPÇÃO PASSIVA",C['golddeep'],C['goldsoft'],"profa",["“Com um","cafezinho de R$ 200","isso se resolve...”"],"funcionário SOLICITA"),
 ("CORRUPÇÃO ATIVA",C['navy'],NV,"prof",["“Tome R$ 300","para esquecer","essa multa.”"],"particular OFERECE")], "Situação ilustrada: o verbo diz qual é o crime.")
add(H(2,'Exigir x solicitar x <span class="hl">oferecer</span>','A diferença que mais aparece nas provas.', "A09") + adm +
 table(["","CONCUSSÃO (316)","CORRUPÇÃO PASSIVA (317)","CORRUPÇÃO ATIVA (333)"],[
  ["Quem pratica","Funcionário público","Funcionário público","<b>Particular</b> (ou funcionário agindo como particular)"],
  ["Verbo","<b>Exigir</b>","<b>Solicitar, receber, aceitar promessa</b>","<b>Oferecer, prometer</b>"],
  ["Clima","Imposição: a vítima tem medo","Negociação: pedido ou acerto","Iniciativa do particular"],
  ["Quem paga comete crime?","<b>Não</b>: é vítima","Se ofereceu ou prometeu antes, sim (corrupção ativa)","—"],
  ["Pena","Reclusão, 2 a 12, e multa","Reclusão, 2 a 12, e multa","Reclusão, 2 a 12, e multa"]],["16%",None,None,None]))

def arvore():
    s = f'<figure><svg viewBox="0 0 640 332" width="620" xmlns="http://www.w3.org/2000/svg" font-family="Inter"><defs><marker id="ar" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L10,5 L0,10 z" fill="{C["ink"]}"/></marker></defs>'
    def box(x,y,w,h,fg,bg,lines,bold=0):
        r = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="11" fill="{bg}" stroke="{fg}" stroke-width="2.3"/>'
        for j,l in enumerate(lines):
            r += f'<text x="{x+w/2}" y="{y+20+j*16}" text-anchor="middle" font-size="{12 if j==0 else 10.8}" font-weight="{900 if j==0 else 600}" fill="{fg if j==0 else C["ink"]}">{l}</text>'
        return r
    def ln(x1,y1,x2,y2,t=""):
        r = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{C["ink"]}" stroke-width="2" marker-end="url(#ar)"/>'
        if t: r += f'<text x="{(x1+x2)/2+6}" y="{(y1+y2)/2}" font-size="10.5" font-weight="800" fill="{C["muted"]}">{t}</text>'
        return r
    s += box(220,4,200,44,C['navy'],NV,["QUEM TOMOU A INICIATIVA?","de pedir ou de oferecer"])
    s += box(40,90,230,44,C['golddeep'],C['goldsoft'],["O FUNCIONÁRIO","qual foi o verbo?"])
    s += box(370,90,230,44,C['navy'],NV,["O PARTICULAR","ofereceu ou prometeu"])
    s += ln(280,48,170,88) + ln(360,48,480,88)
    s += box(4,190,140,60,C['red'],C['redsoft'],["EXIGIU","com ameaça implícita","→ CONCUSSÃO (316)"])
    s += box(160,190,140,60,C['golddeep'],C['goldsoft'],["SOLICITOU","ou recebeu","→ CORRUPÇÃO PASSIVA"])
    s += box(370,190,230,60,C['navy'],NV,["CORRUPÇÃO ATIVA (333)","e o funcionário que recebe ou","aceita: CORRUPÇÃO PASSIVA (317)"])
    s += ln(120,134,74,188) + ln(190,134,230,188) + ln(485,134,485,188)
    s += box(40,266,560,60,C['green'],C['greensoft'],["NÃO HOUVE VANTAGEM?","Agiu por interesse ou sentimento pessoal → PREVARICAÇÃO (319)","Cedeu a pedido ou influência de alguém → CORRUPÇÃO PASSIVA PRIVILEGIADA (317, § 2º)"])
    return s + '</svg><figcaption>Roteiro de decisão: três perguntas resolvem a maior parte das questões.</figcaption></figure>'

atencao(arvore() +
 pega('<ul><li>Na concussão, a vítima que paga <b>não</b> comete corrupção ativa: ela cedeu a uma <b>exigência</b>.</li><li>A corrupção passiva e a ativa são <b>independentes</b>: pode haver uma sem a outra. Se o funcionário <b>solicita</b> e o particular <b>apenas paga</b>, sem ter oferecido nada, só há corrupção passiva.</li><li>Os três crimes são <b>formais</b>: consumam-se com a exigência, a solicitação ou o oferecimento, ainda que a vantagem não seja entregue.</li></ul>'),
 ["exigir = concussão","solicitar/receber = corrupção passiva","oferecer/prometer = corrupção ativa","crime formal","crimes independentes"], "Roteiro de decisão: qual é o crime?")

add(H(2,'<span class="hl">Prevaricação</span> (arts. 319 e 319-A)','O funcionário age ou se omite por interesse ou sentimento pessoal.', "A10") +
 lei(cp("Art. 319"),'<p>Art. 319 - Retardar ou deixar de praticar, indevidamente, ato de ofício, ou praticá-lo contra disposição expressa de lei, para satisfazer interesse ou sentimento pessoal:<br>Pena - detenção, de três meses a um ano, e multa.</p>') +
 lei(cp("Art. 319-A (Lei nº 11.466/2007)"),'<p>Art. 319-A. Deixar o Diretor de Penitenciária e/ou agente público, de cumprir seu dever de vedar ao preso o acesso a aparelho telefônico, de rádio ou similar, que permita a comunicação com outros presos ou com o ambiente externo:<br>Pena: detenção, de 3 (três) meses a 1 (um) ano.</p>') +
 traduz(p('Na prevaricação não há dinheiro envolvido: o servidor <strong>retarda, deixa de fazer ou faz contra a lei</strong> o seu trabalho para satisfazer um <strong>interesse ou sentimento pessoal</strong>: amizade, vingança, preguiça proposital, simpatia política. Se houver vantagem indevida, o crime passa a ser corrupção passiva.')) +
 memo('Prevaricação: <strong>interesse ou sentimento pessoal</strong>, sem vantagem. Detenção de <strong>3 meses a 1 ano</strong>, e multa. 319-A: agente que <strong>não impede</strong> o acesso do preso a <strong>celular</strong>.'))

atencao(
 flow([("idcard",["AGENTE","DE TRÂNSITO"]),("people",["INFRATOR É","seu amigo de","infância"]),("xmark",["NÃO AUTUA","por amizade","(sem vantagem)"]),("gavel",["PREVARICAÇÃO","art. 319"])],
      "Sem vantagem indevida e por sentimento pessoal: prevaricação.", colors=colors("n","o","r","b")) +
 table(["","PREVARICAÇÃO (319)","CORRUPÇÃO PASSIVA (317)","CORRUPÇÃO PRIVILEGIADA (317, § 2º)"],[
  ["Motivo","Interesse ou sentimento <b>próprio</b>","<b>Vantagem indevida</b>","<b>Pedido ou influência de outrem</b>"],
  ["Exemplo","Não autua o amigo","Não autua por R$ 200","Não autua porque o vereador pediu"]],["16%",None,None,None]) +
 pega('<ul><li>Celular no presídio tem <b>dois</b> crimes diferentes: o <b>agente</b> que deixa de impedir o acesso (art. 319-A, Capítulo I) e <b>quem faz o aparelho entrar</b> no estabelecimento (art. 349-A, Capítulo III).</li><li>Na prevaricação, o interesse é <b>do próprio funcionário</b>. Se ele apenas atende ao <b>pedido de outra pessoa</b>, a hipótese se aproxima da corrupção passiva privilegiada.</li></ul>'),
 ["interesse ou sentimento pessoal","retardar","deixar de praticar","ato de ofício","319-A · celular"])

add(H(2,'Condescendência, advocacia administrativa e <span class="hl">sigilo</span>','Arts. 320, 321 e 325.', "A11") +
 table(["Crime","Conduta (em síntese)","Pena"],[
  ["Condescendência criminosa (art. 320)","Deixar, <b>por indulgência</b>, de responsabilizar subordinado que cometeu infração no exercício do cargo, ou, sem competência para isso, não levar o fato ao conhecimento da autoridade competente","Detenção, 15 dias a 1 mês, ou multa"],
  ["Advocacia administrativa (art. 321)","<b>Patrocinar</b>, direta ou indiretamente, interesse privado perante a Administração, valendo-se da qualidade de funcionário","Detenção, 1 a 3 meses, ou multa; se o interesse é <b>ilegítimo</b>: detenção, 3 meses a 1 ano, além da multa"],
  ["Violação de sigilo funcional (art. 325)","<b>Revelar</b> fato de que tem ciência em razão do cargo e que deva permanecer em segredo, ou facilitar a revelação; § 1º: permitir ou facilitar acesso indevido a sistemas, inclusive com senha, ou usar indevidamente o acesso restrito","Detenção, 6 meses a 2 anos, ou multa, se o fato não constitui crime mais grave; se resulta dano (§ 2º): reclusão, 2 a 6 anos, e multa"]],["24%",None,"26%"]) +
 ex(p('<b>Condescendência:</b> a chefe descobre que um subordinado falsificou a folha de ponto, mas, por pena, decide "deixar pra lá". <b>Advocacia administrativa:</b> o servidor da prefeitura usa sua influência no setor de alvarás para acelerar o processo da empresa do cunhado. <b>Sigilo funcional:</b> o servidor que corrige a prova do concurso conta o gabarito a um candidato antes da divulgação.')) +
 memo('Condescendência: <strong>indulgência</strong> com o subordinado. Advocacia administrativa: <strong>patrocinar interesse privado</strong> usando o cargo. Sigilo funcional: <strong>revelar segredo</strong> conhecido em razão do cargo.'))

add(H(2,'Outros crimes <span class="hl">funcionais</span>','Tipos menos cobrados, mas presentes nos editais completos.', "A12") +
 table(["Crime","Conduta (em síntese)","Pena"],[
  ["Extravio, sonegação ou inutilização de livro ou documento (art. 314)","Extraviar, sonegar ou inutilizar livro oficial ou documento de que tem a guarda em razão do cargo","Reclusão, 1 a 4 anos, se o fato não constitui crime mais grave"],
  ["Emprego irregular de verbas ou rendas públicas (art. 315)","Dar às verbas ou rendas públicas <b>aplicação diversa</b> da estabelecida em lei (sem proveito próprio)","Detenção, 1 a 3 meses, ou multa"],
  ["Facilitação de contrabando ou descaminho (art. 318)","Facilitar, com infração de dever funcional, a prática de contrabando ou descaminho","Reclusão, 3 a 8 anos, e multa"],
  ["Violência arbitrária (art. 322)","Praticar violência no exercício da função ou a pretexto de exercê-la","Detenção, 6 meses a 3 anos, além da pena da violência"],
  ["Abandono de função (art. 323)","Abandonar cargo público, fora dos casos permitidos em lei","Detenção, 15 dias a 1 mês, ou multa; com prejuízo público: 3 meses a 1 ano, e multa; em faixa de fronteira: 1 a 3 anos, e multa"],
  ["Exercício funcional ilegalmente antecipado ou prolongado (art. 324)","Entrar no exercício antes de satisfeitas as exigências legais, ou continuar depois de saber oficialmente da exoneração, remoção, substituição ou suspensão","Detenção, 15 dias a 1 mês, ou multa"]],["30%",None,"26%"]) +
 lembre(p('O texto compilado do Planalto ainda traz o <strong>art. 322</strong> (violência arbitrária) sem nota de revogação. Há discussão doutrinária sobre sua revogação por leis de abuso de autoridade; este caderno apresenta o texto como consta da compilação oficial. Já o <strong>art. 350</strong> foi expressamente revogado pela Lei nº 13.869/2019 (nova Lei de Abuso de Autoridade).'), "Situação dos arts. 322 e 350") +
 '')
atencao(ex(p('O prefeito usa verba que a lei vinculava à saúde para asfaltar uma rua, sem nenhum proveito pessoal: em tese, <b>emprego irregular de verbas públicas</b> (art. 315). Se ele usasse o mesmo dinheiro para reformar a própria casa, haveria desvio em proveito próprio. Já o servidor que, após ser exonerado e oficialmente comunicado, continua despachando processos comete o <b>art. 324</b>.')) +
 pega('<ul><li><b>Desviar</b> verba em proveito próprio ou alheio é <b>peculato-desvio</b> (art. 312); dar à verba <b>outra finalidade pública</b> não prevista em lei é <b>emprego irregular</b> (art. 315), com pena muito menor.</li><li>O servidor da alfândega que facilita o contrabando responde pelo <b>art. 318</b>, e não como partícipe do art. 334-A.</li></ul>'), ["aplicação diversa da lei","facilitação de contrabando","abandono de cargo","faixa de fronteira","exercício prolongado"])

treino(2, [
 ("No peculato, o bem apropriado pelo funcionário deve ser obrigatoriamente público.","E","Pode ser público ou particular, desde que esteja em sua posse em razão do cargo."),
 ("No peculato culposo, a reparação do dano antes da sentença irrecorrível extingue a punibilidade.","C","Art. 312, § 3º."),
 ("A concussão consuma-se com a simples exigência da vantagem indevida.","C","É crime formal."),
 ("O funcionário que deixa de praticar ato de ofício para satisfazer sentimento pessoal, sem receber vantagem, comete corrupção passiva.","E","Comete prevaricação (art. 319)."),
 ("A inserção de dados falsos em sistema de informações (art. 313-A) só pode ser praticada por funcionário autorizado.","C","O tipo exige o funcionário autorizado."),
 ("Exigir tributo que sabe indevido configura excesso de exação, com pena de reclusão de 3 a 8 anos, e multa.","C","Art. 316, § 1º.")])

# ================================================================ UNIDADE 3
opener("03","UNIDADE 3","Crimes praticados por particular",["Usurpação de função pública","Resistência","Desobediência","Desacato e a ADPF 496","Resistência x desobediência x desacato","Tráfico de influência e corrupção ativa","Contrabando x descaminho"],"U3")

add(H(3,'Usurpação de <span class="hl">função pública</span>','Art. 328: fingir ser funcionário e agir como tal.', "A13") +
 lei(cp("Art. 328"),'<p>Art. 328 - Usurpar o exercício de função pública:<br>Pena - detenção, de três meses a dois anos, e multa.<br>Parágrafo único - Se do fato o agente aufere vantagem:<br>Pena - reclusão, de dois a cinco anos, e multa.</p>') +
 traduz(p('Usurpar é <strong>tomar para si</strong> algo que não é seu. O crime exige que a pessoa <strong>pratique atos</strong> da função, como se fosse o servidor: fiscalizar, multar, apreender. Apenas <strong>dizer</strong> que é policial, sem praticar ato nenhum, não é usurpação; pode ser a contravenção de simulação da qualidade de funcionário (art. 45 da Lei das Contravenções Penais).'),"profa") +
 flow([("badge",["FALSO FISCAL","colete e","crachá falso"]),("doc",["\"AUTUA\"","ambulantes","na praça"]),("coin",["COBRA R$ 100","para","\"liberar\""]),("gavel",["USURPAÇÃO","com vantagem","(p. único)"])],
      "Quem pratica atos da função sem ser funcionário usurpa a função pública.", colors=colors("o","n","r","b")) +
 memo('Usurpação: <strong>praticar atos</strong> da função. Com <strong>vantagem</strong>: reclusão de <strong>2 a 5 anos</strong>, e multa. Só se dizer funcionário, sem praticar atos: não é o art. 328.'))

add(H(3,'<span class="hl">Resistência</span> (art. 329)','Opor-se a ato legal com violência ou ameaça.', "A14") +
 lei(cp("Art. 329, caput"),'<p>Art. 329 - Opor-se à execução de ato legal, mediante violência ou ameaça a funcionário competente para executá-lo ou a quem lhe esteja prestando auxílio:<br>Pena - detenção, de dois meses a dois anos.</p>') +
 table(["Requisito ou regra","Explicação"],[
  ["Ato <b>legal</b>","Se a ordem é ilegal (prisão sem flagrante nem mandado, por exemplo), não há resistência"],
  ["<b>Violência ou ameaça</b>","Contra o funcionário competente <b>ou contra quem o auxilia</b> (inclusive um particular)"],
  ["Ato não executado (§ 1º)","Se, em razão da resistência, o ato não se executa: <b>reclusão, de 1 a 3 anos</b>"],
  ["Concurso com a violência (§ 2º)","As penas são aplicadas <b>sem prejuízo</b> das correspondentes à violência (ex.: lesão corporal)"]],["28%",None]) +
 ex(p('Guardas municipais cumprem, com um oficial de justiça, ordem judicial de desocupação. O morador ameaça com uma barra de ferro o chaveiro contratado que ajudava a equipe e impede a entrada. Há <b>resistência</b>, com a pena do § 1º se o ato não for executado: a ameaça atingiu <b>quem prestava auxílio</b> ao funcionário.')) +
 memo('Resistência = <strong>ato legal + violência ou ameaça</strong>. Ato não executado: <strong>reclusão de 1 a 3 anos</strong>. Pena da violência: <strong>soma-se</strong>.') +
 pega('<ul><li><b>Resistência passiva</b> (deitar no chão, agarrar-se ao poste, recusar-se a andar) não tem violência nem ameaça contra a pessoa: não configura o art. 329.</li><li>A ameaça do art. 329 <b>não precisa ser grave</b>: o tipo fala apenas em "ameaça".</li></ul>'))

add(H(3,'<span class="hl">Desobediência</span> (art. 330)','Descumprir a ordem legal, sem violência.', "A15") +
 lei(cp("Art. 330"),'<p>Art. 330 - Desobedecer a ordem legal de funcionário público:<br>Pena - detenção, de quinze dias a seis meses, e multa.</p>') +
 traduz(p('A desobediência é o <strong>"não" puro e simples</strong> a uma ordem legal dirigida diretamente à pessoa: não parar, não sair, não entregar. Não há agressão nem ameaça. A ordem precisa ser <strong>legal</strong>, vir de <strong>funcionário competente</strong> e ser dirigida a quem tem o <strong>dever de cumpri-la</strong>.')) +
 flow([("badge",["ORDEM LEGAL","\"Desligue o som","e saia da via.\""]),("person",["PARTICULAR","ignora e","continua"]),("gavel",["DESOBEDIÊNCIA","art. 330"])],
      "Desobediência: descumprir, sem violência, uma ordem legal de funcionário público.", colors=colors("n","o","r")) +
 memo('Desobediência: <strong>ordem legal</strong> + <strong>descumprimento sem violência</strong>. Pena: detenção de <strong>15 dias a 6 meses</strong>, e multa.') +
 pega('<ul><li>Com violência ou ameaça para impedir o ato, o crime passa a ser <b>resistência</b>.</li><li>A <b>ordem ilegal</b> não gera o dever de obedecer.</li><li>Ninguém é obrigado a produzir prova contra si mesmo: a recusa a se autoincriminar não é desobediência.</li></ul>'))

add(H(3,'<span class="hl">Desacato</span> e a controvérsia','Art. 331 e a decisão do STF na ADPF 496.', "A16") +
 lei(cp("Art. 331"),'<p>Art. 331 - Desacatar funcionário público no exercício da função ou em razão dela:<br>Pena - detenção, de seis meses a dois anos, ou multa.</p>') +
 traduz(p('Desacatar é <strong>humilhar, menosprezar ou ofender</strong> o funcionário, atingindo o prestígio da função: xingar, cuspir, rasgar o auto de infração na cara do agente. A ofensa precisa acontecer <strong>no exercício da função</strong> (o agente está trabalhando) ou <strong>em razão dela</strong> (o agente está de folga, mas é ofendido por causa do trabalho).'),"profa") +
 lembre(p('Por muitos anos se discutiu se o crime de desacato seria compatível com a <strong>liberdade de expressão</strong> e com a <strong>Convenção Americana sobre Direitos Humanos</strong> (Pacto de São José da Costa Rica). Houve decisões divergentes no STJ em 2016 e 2017. Em <strong>2020</strong>, o <strong>STF</strong>, na <strong>ADPF 496</strong>, decidiu por maioria que o art. 331 <strong>foi recepcionado</strong> pela Constituição de 1988 e é <strong>compatível</strong> com a Convenção. Entendimento atual: <strong>desacato é crime</strong>. O STF ressaltou que a crítica, ainda que dura, não se confunde com o desacato, que exige a intenção de humilhar ou desprestigiar a função.'), "A controvérsia e o entendimento do STF") +
 memo('Desacato <strong>continua sendo crime</strong> (STF, ADPF 496, 2020). Exige ofensa <strong>no exercício da função ou em razão dela</strong>. Crítica respeitosa, ainda que dura, não é desacato.'))

atencao(
 table(["Situação","Há desacato?"],[
  ["Motorista xinga o agente durante a abordagem","<b>Sim</b>: no exercício da função"],
  ["Ex-autuado encontra o agente de folga no mercado e o humilha por causa da multa","<b>Sim</b>: em razão da função"],
  ["Cidadão escreve em rede social uma crítica dura, mas respeitosa, à atuação da Guarda","<b>Não</b>: é crítica, não intenção de humilhar"],
  ["Vizinho xinga o policial de folga por uma briga de garagem, sem relação com o trabalho","<b>Não</b> é desacato: pode ser <b>injúria</b> (art. 140)"],
  ["Ofensa feita por telefone ou carta, sem a presença do funcionário","A doutrina majoritária exige a presença do funcionário; sem ela, tende a ser crime contra a honra"]],["62%",None]) +
 pega('<ul><li>Questões antigas afirmam que o desacato "deixou de ser crime" por incompatibilidade com o Pacto de São José. O entendimento atual do STF (ADPF 496) é o <b>oposto</b>.</li><li>A pena do desacato (6 meses a 2 anos) é <b>maior</b> que a da desobediência (15 dias a 6 meses) e tem a alternativa de <b>multa</b>.</li><li>Funcionário que ofende outro funcionário, no exercício da função, também pode cometer desacato, segundo a doutrina majoritária.</li></ul>'),
 ["no exercício da função","em razão dela","ADPF 496","recepcionado","Pacto de São José","intenção de humilhar"])

cena = scene3([("RESISTÊNCIA",C['red'],C['redsoft'],"prof",["Empurra o agente","para impedir","a apreensão."],"VIOLÊNCIA ou AMEAÇA"),
 ("DESOBEDIÊNCIA",C['golddeep'],C['goldsoft'],"profa",["Ignora a ordem","de parar e segue","dirigindo."],"só DESCUMPRE a ordem"),
 ("DESACATO",C['navy'],NV,"prof",["“Seu verme,","você não manda","em nada!”"],"OFENDE / HUMILHA")], "Situação ilustrada: a mesma abordagem, três crimes diferentes.")
add(H(3,'Resistência x desobediência x <span class="hl">desacato</span>','Como separar os três crimes de uma abordagem.', "A17") + cena +
 table(["","RESISTÊNCIA (329)","DESOBEDIÊNCIA (330)","DESACATO (331)"],[
  ["Núcleo","<b>Opor-se</b> a ato legal","<b>Desobedecer</b> ordem legal","<b>Desacatar</b> (ofender)"],
  ["Violência ou ameaça","<b>Sim</b>, é essencial","Não","Não é essencial"],
  ["Objetivo do agente","Impedir a execução do ato","Não cumprir a ordem","Humilhar o funcionário e a função"],
  ["Pena","Detenção, 2 meses a 2 anos (reclusão, 1 a 3, se o ato não se executa)","Detenção, 15 dias a 6 meses, e multa","Detenção, 6 meses a 2 anos, ou multa"]],["17%",None,None,None]))

add(H(3,'Tráfico de influência e <span class="hl">corrupção ativa</span>','Arts. 332 e 333.', "A18") +
 lei(cp("Art. 333 (redação da Lei nº 10.763/2003)"),'<p>Art. 333 - Oferecer ou prometer vantagem indevida a funcionário público, para determiná-lo a praticar, omitir ou retardar ato de ofício:<br>Pena - reclusão, de 2 (dois) a 12 (doze) anos, e multa.</p>') +
 table(["Crime","Conduta (em síntese)","Pena"],[
  ["Corrupção ativa majorada (art. 333, parágrafo único)","Em razão da vantagem ou promessa, o funcionário <b>retarda ou omite</b> ato de ofício, ou o pratica infringindo dever funcional","Aumento de <b>1/3</b>"],
  ["Tráfico de influência (art. 332)","Solicitar, exigir, cobrar ou obter vantagem a pretexto de <b>influir</b> em ato praticado por funcionário público no exercício da função","Reclusão, 2 a 5 anos, e multa; aumento de <b>metade</b> se o agente alega ou insinua que a vantagem também se destina ao funcionário"]],["30%",None,"26%"]) +
 ex(p('Um homem procura o dono de um bar e diz: "Sou amigo do chefe da fiscalização. Por R$ 3 mil eu faço ele arquivar o seu processo." Ele não é funcionário e não precisa ter influência real: é <b>tráfico de influência</b> (art. 332), com aumento de metade porque insinuou que parte do dinheiro iria para o fiscal. Se o dono do bar procurasse diretamente o fiscal e lhe oferecesse o dinheiro, seria <b>corrupção ativa</b>.')) +
 '')
atencao(memo('Corrupção ativa: o particular <strong>oferece ou promete</strong>. Consuma-se com a oferta, mesmo que o funcionário recuse. Tráfico de influência: <strong>vende prestígio</strong>, real ou inventado, junto ao funcionário.') +
 pega('<ul><li>Na corrupção ativa, a oferta deve ser <b>antes</b> do ato, para <b>determinar</b> o funcionário. Dar um presente <b>depois</b>, sem acordo prévio, não se encaixa nos verbos "oferecer ou prometer" para determinar o ato.</li><li>Se o funcionário <b>exigiu</b> e o particular pagou, não há corrupção ativa: há <b>concussão</b>, e o particular é vítima.</li></ul>'), ["oferecer ou prometer","determinar o ato de ofício","crime formal","a pretexto de influir","aumento de metade"])

add(H(3,'Contrabando x <span class="hl">descaminho</span>','Arts. 334 e 334-A (Lei nº 13.008/2014).', "A19") +
 table(["","DESCAMINHO (334)","CONTRABANDO (334-A)"],[
  ["Texto","Iludir, no todo ou em parte, o pagamento de direito ou imposto devido pela entrada, pela saída ou pelo consumo de mercadoria","Importar ou exportar mercadoria <b>proibida</b>"],
  ["A mercadoria é","<b>Permitida</b>, mas o imposto não é pago","<b>Proibida</b> (ou sujeita a autorização que não existe)"],
  ["Bem protegido","Principalmente a arrecadação tributária","Saúde, segurança, moralidade pública, indústria nacional"],
  ["Pena","Reclusão, <b>1 a 4 anos</b>","Reclusão, <b>2 a 5 anos</b>"],
  ["Transporte aéreo, marítimo ou fluvial (§ 3º)","Pena em <b>dobro</b>","Pena em <b>dobro</b>"],
  ["Insignificância","Admitida pela jurisprudência, com parâmetro de valor do tributo","Em regra, não admitida"]],["20%",None,None]) +
 memo('<strong>Descaminho</strong> = mercadoria <strong>lícita</strong> + <strong>imposto iludido</strong> (1 a 4). <strong>Contrabando</strong> = mercadoria <strong>proibida</strong> (2 a 5). Por avião ou barco: pena em <strong>dobro</strong> nos dois.'))
atencao(flow([("briefcase",["ELETRÔNICOS","lícitos, sem","pagar imposto"]),("alert",["DESCAMINHO","1 a 4 anos"]),("xmark",["CIGARRO","de venda proibida","no Brasil"]),("alert",["CONTRABANDO","2 a 5 anos"])],
      "Mercadoria permitida sem imposto: descaminho. Mercadoria proibida: contrabando.", colors=colors("b","o","r","n")) +
 pega('<ul><li>Vender, expor, manter em depósito ou usar, em atividade comercial, mercadoria estrangeira introduzida clandestinamente também é crime (§ 1º dos dois artigos), e o comércio irregular feito <b>em residência</b> equipara-se a atividade comercial (§ 2º).</li><li>O aumento do § 3º é de <b>dobro</b>, e não de 1/3.</li></ul>'), ["mercadoria proibida","iludir imposto","pena em dobro","transporte aéreo, marítimo ou fluvial","Lei nº 13.008/2014"])

treino(3, [
 ("Para configurar a resistência, é indispensável que o agente empregue violência ou ameaça contra o funcionário competente ou contra quem lhe preste auxílio.","C","Art. 329."),
 ("A pessoa que apenas se recusa a cumprir uma ordem legal, sem violência ou ameaça, comete resistência.","E","Comete desobediência (art. 330)."),
 ("Segundo o STF (ADPF 496), o crime de desacato não foi recepcionado pela Constituição de 1988.","E","O STF decidiu que o art. 331 foi recepcionado e é compatível com a Convenção Americana."),
 ("A corrupção ativa consuma-se com o oferecimento da vantagem indevida, ainda que o funcionário a recuse.","C","Crime formal."),
 ("Importar mercadoria permitida sem pagar o imposto devido configura contrabando.","E","É descaminho (art. 334); contrabando envolve mercadoria proibida."),
 ("Na usurpação de função pública, se o agente aufere vantagem, a pena é de reclusão de 2 a 5 anos, e multa.","C","Art. 328, parágrafo único.")])

# ================================================================ UNIDADE 4
opener("04","UNIDADE 4","Administração da Justiça e outros crimes",["Denunciação caluniosa x comunicação falsa x autoacusação","Falso testemunho e coação no curso do processo","Exercício arbitrário e favorecimentos","Medidas protetivas, celular em presídio e fuga","Noções de crimes em licitações"],"U4")

just = scene3([("DENUNCIAÇÃO",C['red'],C['redsoft'],"prof",["“Foi o Pedro","quem roubou!”","(sabe que não foi)"],"ACUSA pessoa inocente"),
 ("COMUNICAÇÃO FALSA",C['golddeep'],C['goldsoft'],"profa",["“Fui roubada!”","(o roubo","nunca existiu)"],"crime INEXISTENTE, sem acusar"),
 ("AUTOACUSAÇÃO",C['navy'],NV,"prof",["“Fui eu quem","furtou a loja.”","(não foi)"],"acusa A SI MESMO")], "Situação ilustrada: três mentiras à autoridade, três crimes.")
add(H(4,'Denunciação caluniosa, comunicação falsa e <span class="hl">autoacusação</span>','Arts. 339, 340 e 341.', "A20") + just +
 table(["","DENUNCIAÇÃO CALUNIOSA (339)","COMUNICAÇÃO FALSA (340)","AUTOACUSAÇÃO FALSA (341)"],[
  ["Conduta","<b>Dar causa</b> à instauração de inquérito, processo judicial, PAD, inquérito civil ou ação de improbidade contra alguém, imputando-lhe crime, infração ético-disciplinar ou ato ímprobo de que <b>o sabe inocente</b>","Provocar a ação de autoridade comunicando crime ou contravenção que sabe <b>não ter ocorrido</b>","Acusar-se, perante a autoridade, de crime <b>inexistente</b> ou <b>praticado por outrem</b>"],
  ["Pessoa determinada?","<b>Sim</b>, aponta um inocente","Não aponta ninguém (ou aponta pessoa inexistente)","Aponta a si mesmo"],
  ["Pena","Reclusão, 2 a 8 anos, e multa","Detenção, 1 a 6 meses, ou multa","Detenção, 3 meses a 2 anos, ou multa"]],["17%",None,None,None]))

atencao(
 table(["Regra da denunciação caluniosa","Conteúdo"],[["Anonimato ou nome suposto (§ 1º)","Pena aumentada de <b>sexta parte</b>"],["Imputação de contravenção (§ 2º)","Pena <b>diminuída de metade</b>"]],["40%",None]) +
 table(["","CALÚNIA (138)","DENUNCIAÇÃO CALUNIOSA (339)"],[["Bem protegido","Honra da vítima","Administração da Justiça"],["O que o agente faz","Atribui falsamente um crime a alguém (fala, escreve, divulga)","<b>Provoca a instauração</b> de investigação ou processo contra o inocente"],["Pena","Detenção, 6 meses a 2 anos, e multa","Reclusão, 2 a 8 anos, e multa"]],["18%",None,None]) +
 pega('<ul><li>Sem pessoa determinada, não há denunciação caluniosa: pode haver <b>comunicação falsa de crime</b>.</li><li>Inventar um roubo para receber o seguro do celular é <b>comunicação falsa</b> (e pode haver fraude contra a seguradora).</li><li>A denunciação caluniosa não se limita a inquérito policial: inclui <b>PAD</b>, <b>inquérito civil</b> e <b>ação de improbidade</b> (redação da Lei nº 14.110/2020).</li></ul>'),
 ["dar causa à instauração","sabe inocente","pessoa determinada","crime que não ocorreu","autoacusação","Lei nº 14.110/2020"])

add(H(4,'Falso testemunho e <span class="hl">coação no curso do processo</span>','Arts. 342, 343 e 344.', "A21") +
 lei(cp("Art. 342, caput"),'<p>Art. 342. Fazer afirmação falsa, ou negar ou calar a verdade como testemunha, perito, contador, tradutor ou intérprete em processo judicial, ou administrativo, inquérito policial, ou em juízo arbitral:<br>Pena - reclusão, de 2 (dois) a 4 (quatro) anos, e multa.</p>') +
 table(["Regra","Conteúdo (em síntese)"],[
  ["Aumento de 1/6 a 1/3 (art. 342, § 1º)","Crime praticado mediante suborno, ou com o fim de obter prova destinada a produzir efeito em processo penal, ou em processo civil em que for parte entidade da administração pública"],
  ["Retratação (art. 342, § 2º)","O fato <b>deixa de ser punível</b> se, <b>antes da sentença</b> no processo em que ocorreu o ilícito, o agente se retrata ou declara a verdade"],
  ["Corrupção de testemunha ou perito (art. 343)","Dar, oferecer ou prometer dinheiro ou vantagem para a testemunha ou o perito mentir ou calar a verdade: reclusão, 3 a 4 anos, e multa"],
  ["Coação no curso do processo (art. 344)","Usar <b>violência ou grave ameaça</b> contra autoridade, parte ou qualquer pessoa que funcione em processo judicial, policial, administrativo ou arbitral, para favorecer interesse próprio ou alheio: reclusão, 1 a 4 anos, e multa, além da pena da violência; aumento de 1/3 até a metade se o processo envolver crime contra a dignidade sexual (Lei nº 14.245/2021)"]],["30%",None]) +
 memo('Falso testemunho: <strong>testemunha, perito, contador, tradutor ou intérprete</strong>. Retratação <strong>antes da sentença</strong>: fato deixa de ser punível. Ameaçar testemunha: <strong>coação no curso do processo</strong>.') +
 pega('<ul><li>A <b>vítima</b> e o <b>réu</b> não estão na lista do art. 342: não cometem falso testemunho.</li><li>Quem paga a testemunha para mentir responde pelo <b>art. 343</b>, com pena maior que a da própria testemunha.</li></ul>'))

add(H(4,'Exercício arbitrário e <span class="hl">favorecimentos</span>','Arts. 345, 348 e 349.', "A22") +
 table(["Crime","Conduta (em síntese)","Pena"],[
  ["Exercício arbitrário das próprias razões (art. 345)","<b>Fazer justiça pelas próprias mãos</b>, para satisfazer pretensão, embora legítima, salvo quando a lei o permite","Detenção, 15 dias a 1 mês, ou multa, além da pena da violência; sem violência, ação mediante <b>queixa</b>"],
  ["Favorecimento pessoal (art. 348)","Auxiliar a <b>subtrair-se à ação de autoridade</b> o autor de crime punido com reclusão","Detenção, 1 a 6 meses, e multa (15 dias a 3 meses, e multa, se o crime não é punido com reclusão)"],
  ["Favorecimento real (art. 349)","Prestar a criminoso, fora dos casos de coautoria ou receptação, auxílio destinado a <b>tornar seguro o proveito do crime</b>","Detenção, 1 a 6 meses, e multa"]],["28%",None,"28%"]) +
 table(["","FAVORECIMENTO PESSOAL","FAVORECIMENTO REAL"],[["Ajuda quem?","A <b>pessoa</b> do criminoso a fugir ou se esconder","A guardar o <b>proveito</b> do crime"],["Exemplo","Esconder o autor do roubo em casa","Guardar o dinheiro roubado para o autor"],["Parentes","<b>Isentos de pena</b>: ascendente, descendente, cônjuge ou irmão (art. 348, § 2º)","Não há essa isenção"]],["18%",None,None]) +
 memo('Pessoal = esconde a <strong>pessoa</strong>. Real = protege a <strong>coisa</strong> (o proveito). Parentes próximos: isentos só no favorecimento <strong>pessoal</strong>.') +
 pega('<ul><li>O auxílio prometido <b>antes</b> do crime torna a pessoa <b>partícipe</b>, e não autora de favorecimento.</li><li>No favorecimento real, se o agente age em proveito próprio, adquirindo ou ocultando a coisa, o crime tende a ser <b>receptação</b>.</li></ul>'))

add(H(4,'Medidas protetivas, celular em presídio e <span class="hl">fuga</span>','Arts. 338-A, 349-A, 351 e 352.', "A23") +
 lembre(p('<strong>Art. 338-A (Lei nº 15.280/2025):</strong> pune quem <strong>descumpre decisão judicial que defere medidas protetivas de urgência</strong>. Pena: <strong>reclusão, de 2 a 5 anos, e multa</strong>. O crime existe independentemente da competência civil ou criminal do juiz que deferiu as medidas; na prisão em flagrante, <strong>só o juiz</strong> pode conceder fiança; e outras sanções cabíveis continuam aplicáveis.'), "Novidade: descumprimento de medidas protetivas no Código Penal") +
 table(["Crime","Conduta (em síntese)","Pena"],[
  ["Celular em estabelecimento prisional (art. 349-A)","Ingressar, promover, intermediar, auxiliar ou facilitar a entrada de aparelho de comunicação móvel, rádio ou similar, sem autorização legal","Detenção, 3 meses a 1 ano"],
  ["Fuga de pessoa presa (art. 351)","Promover ou facilitar a fuga de pessoa legalmente presa ou submetida a medida de segurança detentiva","Detenção, 6 meses a 2 anos; à mão armada, por mais de uma pessoa ou com arrombamento: reclusão, 2 a 6 anos; por quem tem a custódia: reclusão, 1 a 4 anos"],
  ["Fuga culposa (art. 351, § 4º)","Funcionário incumbido da custódia ou guarda que, por <b>culpa</b>, permite a fuga","Detenção, 3 meses a 1 ano, ou multa"],
  ["Evasão mediante violência (art. 352)","O <b>próprio preso</b> evade-se ou tenta evadir-se usando violência contra a pessoa","Detenção, 3 meses a 1 ano, além da pena da violência"]],["26%",None,"30%"]) +
 '')
atencao(memo('O preso que foge <strong>sem violência</strong> não comete o crime do art. 352 (pode haver falta disciplinar). Com violência contra a pessoa: <strong>art. 352</strong>. Quem <strong>ajuda</strong> na fuga: <strong>art. 351</strong>.') +
 pega('<ul><li>O art. 338-A <b>não</b> substitui as medidas da Lei Maria da Penha: ele tipifica o <b>descumprimento</b> da decisão judicial no próprio CP.</li><li>A <b>tentativa</b> de fuga com violência já consuma o art. 352 ("evadir-se <b>ou tentar evadir-se</b>").</li></ul>'), ["medidas protetivas de urgência","fiança só pelo juiz","349-A · celular","promover ou facilitar a fuga","fuga culposa","evasão com violência"])

add(H(4,'Noções de crimes em <span class="hl">licitações</span>','Arts. 337-E a 337-P (Lei nº 14.133/2021).', "A24") +
 traduz(p('Desde a Lei nº 14.133/2021 (nova Lei de Licitações), os crimes em licitações e contratos administrativos estão <strong>dentro do Código Penal</strong>, no Capítulo II-B do Título XI. Para provas de nível médio e policiais, basta reconhecer os nomes e as ideias centrais.')) +
 table(["Crime","Pena"],[
  ["Contratação direta ilegal (337-E)","Reclusão, 4 a 8 anos, e multa"],["Frustração do caráter competitivo de licitação (337-F)","Reclusão, 4 a 8 anos, e multa"],
  ["Patrocínio de contratação indevida (337-G)","Reclusão, 6 meses a 3 anos, e multa"],["Modificação ou pagamento irregular em contrato administrativo (337-H)","Reclusão, 4 a 8 anos, e multa"],
  ["Perturbação de processo licitatório (337-I)","Detenção, 6 meses a 3 anos, e multa"],["Violação de sigilo em licitação (337-J)","Detenção, 2 a 3 anos, e multa"],
  ["Afastamento de licitante (337-K)","Reclusão, 3 a 5 anos, e multa, além da pena da violência"],["Fraude em licitação ou contrato (337-L)","Reclusão, 4 a 8 anos, e multa"],
  ["Contratação inidônea (337-M)","Reclusão, 1 a 3 anos, e multa (3 a 6 anos, e multa, para quem celebra o contrato com o inidôneo)"],["Impedimento indevido (337-N)","Reclusão, 6 meses a 2 anos, e multa"],
  ["Omissão grave de dado ou de informação por projetista (337-O)","Reclusão, 6 meses a 3 anos, e multa"]],["58%",None]) +
 memo('Multa nos crimes em licitações (art. 337-P): <strong>não pode ser inferior a 2%</strong> do valor do contrato.'))

treino(4, [
 ("Comete denunciação caluniosa quem dá causa à instauração de inquérito policial contra alguém, imputando-lhe crime de que o sabe inocente.","C","Art. 339."),
 ("Quem comunica à autoridade um roubo que nunca ocorreu, sem apontar autor, comete denunciação caluniosa.","E","Comete comunicação falsa de crime (art. 340)."),
 ("No falso testemunho, o fato deixa de ser punível se, antes da sentença no processo em que ocorreu o ilícito, o agente se retrata ou declara a verdade.","C","Art. 342, § 2º."),
 ("O irmão que esconde em casa o autor de um roubo para que ele não seja preso fica isento de pena.","C","Favorecimento pessoal, art. 348, § 2º."),
 ("Descumprir decisão judicial que defere medidas protetivas de urgência é crime previsto no art. 338-A do CP, com pena de reclusão de 2 a 5 anos, e multa.","C","Lei nº 15.280/2025."),
 ("O preso que foge sem empregar violência contra a pessoa comete o crime do art. 352 do CP.","E","O art. 352 exige violência contra a pessoa.")])

# ================================================================ REVISÃO
mapa = f'''<figure><svg viewBox="0 0 640 470" width="580" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<g stroke="#b9b3ad" stroke-width="2.5" fill="none"><path d="M320 235 L150 70"/><path d="M320 235 L490 70"/><path d="M320 235 L120 235"/><path d="M320 235 L520 235"/><path d="M320 235 L150 400"/><path d="M320 235 L490 400"/></g>
<circle cx="320" cy="235" r="74" fill="{C['navy']}"/><text x="320" y="222" text-anchor="middle" fill="{C['gold']}" font-weight="900" font-size="12.5">CRIMES CONTRA A</text>
<text x="320" y="242" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">ADMINISTRAÇÃO</text><text x="320" y="260" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">PÚBLICA</text>
''' + "".join(
 f'<rect x="{x-100}" y="{y-40}" width="200" height="80" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x}" y="{y-16}" text-anchor="middle" font-weight="900" font-size="12.5" fill="{fg}">{t}</text>'
 + "".join(f'<text x="{x}" y="{y+4+i*15}" text-anchor="middle" font-size="10.8" fill="{C["ink"]}">{l}</text>' for i,l in enumerate(ls))
 for x,y,t,ls,fg,bg in [
  (150,62,"FUNCIONÁRIO (327)",["transitório ou sem salário","terceirizado: equiparado","comissão/direção: +1/3"],C['navy'],NV),
  (490,62,"PECULATO (312)",["apropriar · desviar: 2-12","sem posse: peculato-furto","culposo: reparação extingue"],C['red'],C['redsoft']),
  (112,235,"O VERBO DECIDE",["exigir = concussão","solicitar = corrupção passiva","oferecer = corrupção ativa"],C['golddeep'],C['goldsoft']),
  (528,235,"ABORDAGEM",["violência = resistência","só descumpre = desobediência","ofende = desacato (crime)"],C['green'],C['greensoft']),
  (150,408,"SEM VANTAGEM",["sentimento pessoal:","prevaricação (319)","pedido de outrem: 317, § 2º"],C['blue'],C['sky']),
  (490,408,"JUSTIÇA",["acusa inocente: 339","crime inventado: 340","esconde pessoa: 348"],C['navy'],NV)]) + '</svg><figcaption>Mapa conceitual do Caderno 07.</figcaption></figure>'
add('<div class="marker">§§R1§§</div><div class="unit"><span class="u">REVISÃO</span><span class="t">Véspera da prova</span></div><h1 class="big">Mapa <span class="hl">conceitual</span></h1><p class="lead">O caderno em seis blocos. Explique cada caixa em voz alta.</p>' + mapa)

add('<div class="unit"><span class="u">REVISÃO</span><span class="t">Erros mais comuns</span></div><h1 class="big">Os erros <span class="hl">mais comuns</span> nas provas</h1><p class="lead">Afirmações erradas que aparecem com frequência em questões. Ao lado, o que está certo.</p>' +
 table(["Afirmação errada","O certo é"],[
  ["“Quem trabalha sem salário não é funcionário público.”","É, se exerce função pública, ainda que transitoriamente ou sem remuneração (art. 327)."],
  ["“O peculato só recai sobre bem público.”","Recai sobre bem <b>público ou particular</b> em posse do funcionário em razão do cargo."],
  ["“A reparação do dano extingue a punibilidade do peculato.”","Só no peculato <b>culposo</b>, e se feita antes da sentença irrecorrível."],
  ["“Concussão e corrupção passiva são a mesma coisa.”","Concussão: <b>exigir</b>. Corrupção passiva: <b>solicitar, receber, aceitar promessa</b>."],
  ["“Quem paga ao funcionário que exigiu comete corrupção ativa.”","Não: é <b>vítima</b> de concussão."],
  ["“A corrupção ativa só se consuma se o funcionário aceitar.”","Consuma-se com a <b>oferta ou promessa</b> (crime formal)."],
  ["“Não autuar o amigo é corrupção passiva.”","Sem vantagem e por sentimento pessoal: <b>prevaricação</b>."]],["46%",None]))

add(pratica_title("Erros mais comuns (continuação)") +
 table(["Afirmação errada","O certo é"],[
  ["“Recusar-se a cumprir a ordem é resistência.”","Sem violência ou ameaça é <b>desobediência</b>."],
  ["“Deitar no chão para não ser levado é resistência.”","Resistência passiva, sem violência ou ameaça contra a pessoa, não configura o art. 329."],
  ["“O desacato deixou de ser crime por causa do Pacto de São José.”","O STF (ADPF 496, 2020) decidiu que o art. 331 foi <b>recepcionado</b> e é compatível com a Convenção."],
  ["“Xingar o policial de folga por briga pessoal é desacato.”","Sem relação com a função, é crime contra a honra (injúria)."],
  ["“Contrabando é trazer mercadoria sem pagar imposto.”","Isso é <b>descaminho</b>. Contrabando envolve mercadoria <b>proibida</b>."],
  ["“Inventar um crime sem apontar o autor é denunciação caluniosa.”","É <b>comunicação falsa de crime</b> (art. 340). A denunciação exige pessoa determinada."],
  ["“O pai que esconde o filho foragido comete favorecimento pessoal punível.”","Ascendente, descendente, cônjuge ou irmão ficam <b>isentos de pena</b> (art. 348, § 2º)."],
  ["“A insignificância se aplica a qualquer crime contra a Administração.”","Em regra, <b>não</b> (Súmula 599 do STJ), salvo a exceção do descaminho."]],["46%",None]))

add(pratica_title("Tabela-mestra de penas") +
 table(["Crime","Pena"],[
  ["Peculato (312) · inserção de dados falsos (313-A) · concussão (316) · corrupção passiva (317) · corrupção ativa (333)","Reclusão, 2 a 12 anos, e multa"],
  ["Excesso de exação (316, § 1º) · facilitação de contrabando ou descaminho (318)","Reclusão, 3 a 8 anos, e multa"],
  ["Tráfico de influência (332) · descumprimento de medidas protetivas (338-A)","Reclusão, 2 a 5 anos, e multa"],
  ["Contrabando (334-A)","Reclusão, 2 a 5 anos"],["Descaminho (334)","Reclusão, 1 a 4 anos"],
  ["Denunciação caluniosa (339)","Reclusão, 2 a 8 anos, e multa"],["Falso testemunho (342)","Reclusão, 2 a 4 anos, e multa"],
  ["Peculato mediante erro de outrem (313)","Reclusão, 1 a 4 anos, e multa"],
  ["Peculato culposo (312, § 2º) · prevaricação (319: e multa) · 319-A · 349-A","Detenção, 3 meses a 1 ano"],
  ["Resistência (329)","Detenção, 2 meses a 2 anos (reclusão, 1 a 3, se o ato não se executa)"],
  ["Desacato (331)","Detenção, 6 meses a 2 anos, ou multa"],["Desobediência (330)","Detenção, 15 dias a 6 meses, e multa"],
  ["Usurpação de função (328)","Detenção, 3 meses a 2 anos, e multa (reclusão, 2 a 5, e multa, com vantagem)"]],["60%",None]) +
 memo('Os <strong>"cinco grandes"</strong> (peculato, dados falsos, concussão, corrupção passiva e ativa) têm a mesma pena: <strong>reclusão de 2 a 12 anos</strong>, e multa.'))

FC = [("FUNCIONÁRIO","Conceito penal de funcionário público?","Quem exerce cargo, emprego ou função pública, ainda que transitoriamente ou sem remuneração (art. 327)."),
 ("FUNCIONÁRIO","Quem é equiparado a funcionário público?","Quem atua em entidade paraestatal e quem trabalha em empresa contratada ou conveniada para atividade típica da Administração (§ 1º)."),
 ("FUNCIONÁRIO","Aumento do art. 327, § 2º?","Terça parte, para ocupantes de cargo em comissão ou função de direção ou assessoramento."),
 ("PECULATO","Peculato-furto?","O funcionário não tem a posse, mas subtrai valendo-se da facilidade do cargo (art. 312, § 1º)."),
 ("PECULATO","Reparação do dano no peculato culposo?","Antes da sentença irrecorrível: extingue a punibilidade. Depois: reduz a pena pela metade."),
 ("PECULATO","Peculato mediante erro de outrem?","Apropriar-se de valor recebido, no exercício do cargo, por erro de outrem (art. 313): reclusão, 1 a 4 anos."),
 ("CORRUPÇÃO","Verbo da concussão?","Exigir (art. 316)."),
 ("CORRUPÇÃO","Verbos da corrupção passiva?","Solicitar, receber ou aceitar promessa de vantagem indevida (art. 317)."),
 ("CORRUPÇÃO","Corrupção passiva privilegiada?","Ceder a pedido ou influência de outrem, sem vantagem: detenção, 3 meses a 1 ano, ou multa (§ 2º)."),
 ("CORRUPÇÃO","Excesso de exação?","Exigir tributo indevido ou cobrar por meio vexatório ou gravoso: reclusão, 3 a 8 anos, e multa."),
 ("FUNCIONAIS","Prevaricação?","Retardar, deixar de praticar ou praticar contra a lei ato de ofício, por interesse ou sentimento pessoal."),
 ("FUNCIONAIS","Condescendência criminosa?","Deixar, por indulgência, de responsabilizar subordinado infrator (art. 320)."),
 ("PARTICULAR","Usurpação de função pública?","Praticar atos da função sem ser funcionário; com vantagem: reclusão, 2 a 5 anos, e multa."),
 ("PARTICULAR","Requisito central da resistência?","Violência ou ameaça para se opor a ato legal (art. 329)."),
 ("PARTICULAR","Resistência quando o ato não se executa?","Reclusão, de 1 a 3 anos (§ 1º)."),
 ("PARTICULAR","Desacato ainda é crime?","Sim. STF, ADPF 496 (2020): recepcionado e compatível com a Convenção Americana."),
 ("PARTICULAR","Tráfico de influência?","Obter ou pedir vantagem a pretexto de influir em ato de funcionário; aumento de metade se insinua que o dinheiro também é para ele."),
 ("PARTICULAR","Contrabando x descaminho?","Contrabando: mercadoria proibida (2 a 5). Descaminho: imposto iludido (1 a 4)."),
 ("JUSTIÇA","Denunciação caluniosa x comunicação falsa?","Denunciação: acusa pessoa determinada que sabe inocente. Comunicação falsa: crime que não ocorreu."),
 ("JUSTIÇA","Retratação no falso testemunho?","Antes da sentença no processo em que ocorreu o ilícito: o fato deixa de ser punível."),
 ("JUSTIÇA","Favorecimento pessoal x real?","Pessoal: ajuda a pessoa a fugir. Real: protege o proveito do crime."),
 ("JUSTIÇA","Quem é isento no favorecimento pessoal?","Ascendente, descendente, cônjuge ou irmão do criminoso."),
 ("JUSTIÇA","O que diz o art. 338-A?","Descumprir decisão que defere medidas protetivas de urgência: reclusão, 2 a 5 anos, e multa."),
 ("JUSTIÇA","Preso que foge sem violência?","Não comete o crime do art. 352, que exige violência contra a pessoa.")]
def fcpage(items, first):
    cs = "".join(f'<div class="c"><div class="f"><small>{a}</small>{q}</div><div class="b">{r}</div></div>' for a,q,r in items)
    h = ('<div class="marker">§§R2§§</div><div class="unit"><span class="u">REVISÃO ATIVA</span></div><h1 class="big">Flash<span class="hl">cards</span></h1><p class="lead">Cubra a resposta, tente lembrar e confira. Revise em 1, 3, 7, 15 e 30 dias.</p>' if first else '')
    return h + f'<div class="fc">{cs}</div>'
add(fcpage(FC[:12], True)); add(fcpage(FC[12:], False))

Q = [
 ("Funcionário público","Mário, mesário convocado pela Justiça Eleitoral, sem remuneração, apropria-se de bem que estava sob sua guarda durante a votação. Para fins penais, Mário:",
  ["não é funcionário público, por não receber remuneração.","não é funcionário público, por exercer função transitória.","é funcionário público, pois exerce função pública, ainda que transitoriamente e sem remuneração.","só seria funcionário público se fosse concursado.","é equiparado a funcionário apenas para fins civis."],"C",
  "O art. 327 considera funcionário público quem, embora transitoriamente ou sem remuneração, exerce cargo, emprego ou função pública.","Transitório e sem salário: continua funcionário."),
 ("Funcionário público","Sobre o aumento de pena previsto no art. 327, § 2º, do Código Penal, é correto afirmar que:",
  ["é de metade e se aplica a qualquer servidor efetivo.","é da terça parte e se aplica a ocupantes de cargo em comissão ou função de direção ou assessoramento.","é de dois terços e se aplica a empregados terceirizados.","é do dobro para crimes de corrupção.","foi revogado pela Lei nº 9.983/2000."],"B",
  "O § 2º prevê aumento da terça parte para ocupantes de cargos em comissão ou de função de direção ou assessoramento em órgãos e entidades da Administração.","Comissão ou direção: +1/3."),
 ("Peculato","O tesoureiro de uma autarquia, que guarda os valores arrecadados em razão do cargo, passa a usar parte deles para pagar dívidas pessoais. Ele comete:",
  ["furto qualificado.","apropriação indébita.","peculato.","concussão.","prevaricação."],"C",
  "Apropriar-se de dinheiro de que tem a posse em razão do cargo é peculato (art. 312, caput). Sem a condição de funcionário, seria apropriação indébita.","Posse em razão do cargo + apropriação = peculato."),
 ("Peculato","O servidor que não tem a posse de equipamentos do almoxarifado, mas os subtrai aproveitando-se da facilidade que o cargo lhe proporciona, comete:",
  ["peculato-apropriação.","peculato-desvio.","peculato-furto.","peculato culposo.","furto simples."],"C",
  "Art. 312, § 1º: sem ter a posse, o funcionário subtrai ou concorre para a subtração, valendo-se da facilidade do cargo.","Sem posse + facilidade do cargo = peculato-furto."),
 ("Peculato","No peculato culposo, a reparação do dano feita após a sentença irrecorrível:",
  ["extingue a punibilidade.","reduz de metade a pena imposta.","não produz nenhum efeito.","transforma o crime em doloso.","só produz efeito se houver perdão do ofendido."],"B",
  "Art. 312, § 3º: antes da sentença irrecorrível, extingue a punibilidade; depois, reduz de metade a pena imposta.","Antes: extingue. Depois: metade."),
 ("Dados falsos","A servidora autorizada a operar o sistema de benefícios insere dados falsos para conceder benefício indevido a terceiro. A conduta configura:",
  ["modificação não autorizada de sistema (art. 313-B).","inserção de dados falsos em sistema de informações (art. 313-A).","peculato culposo.","prevaricação.","violação de sigilo funcional."],"B",
  "O art. 313-A pune o funcionário autorizado que insere dados falsos para obter vantagem indevida ou causar dano. O 313-B trata da alteração do próprio sistema ou programa.","Dados falsos = 313-A; sistema alterado = 313-B."),
 ("Concussão","O fiscal municipal diz ao comerciante: “Ou você me paga R$ 1.000, ou eu interdito sua loja amanhã.” O comerciante não paga. O fiscal cometeu:",
  ["tentativa de concussão, pois não recebeu o dinheiro.","concussão consumada.","corrupção passiva.","corrupção ativa.","fato atípico."],"B",
  "A concussão (art. 316) é crime formal: consuma-se com a exigência, independentemente do recebimento.","Exigiu = consumou."),
 ("Corrupção","O policial que, durante uma abordagem, sugere ao motorista que “um cafezinho de R$ 200 resolve a situação” comete:",
  ["concussão.","corrupção passiva.","corrupção ativa.","prevaricação.","advocacia administrativa."],"B",
  "Solicitar vantagem indevida em razão da função é corrupção passiva (art. 317). Se houvesse exigência com ameaça implícita, seria concussão.","Solicitar = corrupção passiva."),
 ("Corrupção","O motorista que, sem qualquer pedido, oferece dinheiro ao agente de trânsito para não ser autuado, tendo a oferta recusada, comete:",
  ["fato atípico, pois o agente recusou.","tentativa de corrupção ativa.","corrupção ativa consumada.","corrupção passiva.","desacato."],"C",
  "Oferecer ou prometer vantagem indevida a funcionário público para determiná-lo a omitir ato de ofício configura corrupção ativa (art. 333), que se consuma com a oferta.","Ofereceu = consumou."),
 ("Corrupção","Sobre os crimes de corrupção, assinale a alternativa correta.",
  ["A corrupção passiva depende sempre da corrupção ativa.","Quem paga ao funcionário que exigiu a vantagem comete corrupção ativa.","A corrupção passiva e a corrupção ativa são crimes independentes.","A corrupção ativa só pode ser praticada por funcionário público.","A corrupção passiva exige que o funcionário pratique o ato de ofício."],"C",
  "Pode haver corrupção passiva sem ativa (o funcionário solicita e o particular apenas paga) e ativa sem passiva (o funcionário recusa a oferta). Quem paga diante de exigência é vítima de concussão.","Passiva e ativa: crimes independentes."),
 ("Prevaricação","O agente de fiscalização deixa de lavrar auto de infração contra um amigo de infância, sem receber qualquer vantagem, apenas por consideração pessoal. Ele comete:",
  ["corrupção passiva.","prevaricação.","condescendência criminosa.","concussão.","fato atípico."],"B",
  "Deixar de praticar ato de ofício para satisfazer interesse ou sentimento pessoal é prevaricação (art. 319). Com vantagem indevida, seria corrupção passiva.","Sentimento pessoal, sem vantagem = prevaricação."),
 ("Funcionais","A chefe de setor que, por indulgência, deixa de responsabilizar subordinado que cometeu infração no exercício do cargo comete:",
  ["prevaricação.","condescendência criminosa.","advocacia administrativa.","corrupção passiva privilegiada.","abandono de função."],"B",
  "Art. 320: deixar o funcionário, por indulgência, de responsabilizar subordinado que cometeu infração no exercício do cargo.","Indulgência com subordinado = condescendência."),
 ("Usurpação","Um homem veste colete com a inscrição “FISCALIZAÇÃO”, aborda ambulantes, simula autuações e cobra R$ 100 de cada um para “liberar” a venda. Ele comete:",
  ["desacato.","usurpação de função pública, na forma qualificada pela vantagem.","corrupção passiva.","concussão.","tráfico de influência."],"B",
  "Praticar atos da função sem ser funcionário é usurpação (art. 328); se aufere vantagem, a pena é de reclusão de 2 a 5 anos, e multa (parágrafo único).","Pratica atos da função + vantagem = usurpação qualificada."),
 ("Resistência","Durante o cumprimento de mandado de prisão, o procurado empurra o policial e consegue fugir, impedindo a prisão. Ele responde por resistência:",
  ["simples, com detenção de 2 meses a 2 anos.","qualificada, com reclusão de 1 a 3 anos, pois o ato não se executou.","apenas se causar lesão grave no policial.","absorvida pela desobediência.","somente se usar arma de fogo."],"B",
  "Art. 329, § 1º: se, em razão da resistência, o ato não se executa, a pena é de reclusão de 1 a 3 anos.","Ato não executado = reclusão de 1 a 3."),
 ("Resistência","A pessoa que, durante a condução, se deita no chão e se recusa a andar, sem agredir nem ameaçar ninguém:",
  ["comete resistência.","comete desacato.","não comete resistência, pois não há violência ou ameaça contra a pessoa.","comete roubo impróprio.","comete coação no curso do processo."],"C",
  "A resistência exige violência ou ameaça contra o funcionário ou quem o auxilia. A chamada resistência passiva não configura o art. 329.","Sem violência ou ameaça, não há resistência."),
 ("Desobediência","O condutor que, sem qualquer violência, ignora a ordem legal de parada dada por agente público e segue viagem pratica, em tese:",
  ["resistência.","desobediência.","desacato.","usurpação de função.","favorecimento pessoal."],"B",
  "Desobedecer a ordem legal de funcionário público, sem violência ou ameaça, é desobediência (art. 330). (Atenção: em situações de trânsito podem incidir também normas do Código de Trânsito Brasileiro.)","Só descumpre = desobediência."),
 ("Desacato","Sobre o crime de desacato, de acordo com o entendimento do STF na ADPF 496, é correto afirmar que:",
  ["foi revogado pela Convenção Americana sobre Direitos Humanos.","não foi recepcionado pela Constituição de 1988.","foi recepcionado pela Constituição e é compatível com a Convenção Americana.","só existe se houver violência física.","passou a ser contravenção penal."],"C",
  "Em 2020, o STF decidiu que o art. 331 do CP foi recepcionado pela Constituição de 1988 e é compatível com a Convenção Americana sobre Direitos Humanos.","Desacato: crime vigente (ADPF 496)."),
 ("Desacato","Um homem encontra, num supermercado, o policial de folga que o havia prendido semanas antes e o humilha em voz alta por causa da prisão. Em tese, há:",
  ["desacato, pois a ofensa ocorreu em razão da função.","apenas injúria, pois o policial estava de folga.","desobediência.","resistência.","fato atípico."],"A",
  "O art. 331 alcança a ofensa no exercício da função ou em razão dela. Mesmo de folga, o policial foi ofendido por causa do trabalho.","Em razão da função também é desacato."),
 ("Tráfico de influência","Pessoa que não é servidora cobra R$ 5 mil de um empresário, dizendo que é amiga do fiscal e que parte do valor será repassada a ele para arquivar um processo. A conduta configura:",
  ["corrupção ativa.","corrupção passiva.","tráfico de influência, com aumento de metade da pena.","concussão.","exploração de prestígio sem pena."],"C",
  "Art. 332: obter vantagem a pretexto de influir em ato de funcionário; o parágrafo único aumenta a pena da metade se o agente alega ou insinua que a vantagem também se destina ao funcionário.","Vende influência + insinua repasse = +metade."),
 ("Contrabando","Importar, sem pagar os tributos devidos, mercadorias de comercialização permitida no Brasil configura:",
  ["contrabando.","descaminho.","receptação.","facilitação de contrabando.","estelionato."],"B",
  "Descaminho (art. 334): iludir o pagamento de imposto devido pela entrada de mercadoria. Contrabando (art. 334-A) é importar ou exportar mercadoria proibida.","Mercadoria permitida sem imposto = descaminho."),
 ("Denunciação","Carla, sabendo que Pedro é inocente, procura a delegacia e o acusa de um furto, dando causa à instauração de inquérito policial contra ele. Carla comete:",
  ["calúnia.","comunicação falsa de crime.","denunciação caluniosa.","autoacusação falsa.","falso testemunho."],"C",
  "Dar causa à instauração de inquérito contra alguém, imputando-lhe crime de que o sabe inocente, é denunciação caluniosa (art. 339), com reclusão de 2 a 8 anos, e multa.","Acusa inocente + instaura investigação = 339."),
 ("Comunicação falsa","Para receber o seguro, João registra ocorrência de roubo de seu celular, que nunca aconteceu, sem apontar qualquer suspeito. Quanto ao crime contra a Administração da Justiça, João comete:",
  ["denunciação caluniosa.","comunicação falsa de crime.","autoacusação falsa.","favorecimento real.","coação no curso do processo."],"B",
  "Provocar a ação da autoridade comunicando crime que sabe não ter ocorrido, sem imputá-lo a pessoa determinada, é comunicação falsa de crime (art. 340).","Crime inventado, sem acusado = 340."),
 ("Favorecimento","A mãe que esconde em casa o filho, autor de roubo, para que ele não seja preso:",
  ["comete favorecimento real.","comete favorecimento pessoal, mas é isenta de pena.","comete receptação.","comete coautoria no roubo.","comete fraude processual."],"B",
  "Auxiliar autor de crime a subtrair-se à ação da autoridade é favorecimento pessoal (art. 348); o § 2º isenta de pena ascendente, descendente, cônjuge ou irmão.","Parente próximo: isento no favorecimento pessoal."),
 ("Medidas protetivas","De acordo com o art. 338-A do Código Penal, incluído pela Lei nº 15.280/2025, descumprir decisão judicial que defere medidas protetivas de urgência:",
  ["é mera infração administrativa.","é crime punido com reclusão, de 2 a 5 anos, e multa.","é crime punido com detenção, de 15 dias a 6 meses.","só é crime se a decisão for de juiz criminal.","admite fiança concedida pelo delegado em qualquer caso."],"B",
  "O art. 338-A prevê reclusão de 2 a 5 anos, e multa; o crime independe da competência civil ou criminal do juiz, e, na prisão em flagrante, apenas a autoridade judicial pode conceder fiança.","338-A: 2 a 5 anos; fiança só pelo juiz.")]

# distribui as respostas corretas entre A e E (troca de posição; as alternativas não dependem da ordem)
ALVO = "CBDCBEBADCEBDACBEACBDEAD"
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
add('<div class="unit"><span class="u">CORREÇÃO</span><span class="t">Treinos rápidos</span></div><h1 class="big">Respostas dos <span class="hl">treinos</span></h1><p class="lead">Certo ou errado das Unidades 1 a 4.</p>' + tr_block(TREINOS[:2]))
add(tr_block(TREINOS[2:]))

add(f'''<div class="unit"><span class="u">ENCERRAMENTO</span></div><h1 class="big">Referências e <span class="hl">verificação</span></h1><p class="lead">De onde vieram as informações.</p>
<h3>Legislação consultada (portal do Planalto)</h3>
<ul>
<li><strong>Código Penal</strong> (Decreto-Lei nº 2.848/1940), texto compilado: arts. 30, 312 a 337-A, 337-E a 337-P, 338-A a 352 e 359.</li>
<li>Leis identificadas nas notas de alteração desses artigos: nº 4.729/1965, 6.799/1980, 8.137/1990, 9.127/1995, 9.983/2000, 10.268/2001, 10.763/2003, 11.466/2007, 12.012/2009, 12.850/2013, 13.008/2014, 13.869/2019, 13.964/2019, 14.110/2020, 14.133/2021, 14.245/2021 e 15.280/2025.</li>
<li>Citados sem conferência nesta edição: Decreto-Lei nº 201/1967 (crimes de prefeitos) e art. 45 da Lei das Contravenções Penais.</li>
</ul>
<h3>Jurisprudência citada</h3><ul><li>STF: ADPF 496 (desacato, 2020).</li><li>STJ: Súmula 599 (insignificância nos crimes contra a Administração Pública) e a exceção jurisprudencial do descaminho.</li></ul>''' + lembre(p(f'<strong>Material pesquisado e atualizado em: {DATA}.</strong> Os tipos penais e as penas foram conferidos no texto compilado do Código Penal no portal do Planalto, que exibe a redação vigente com as notas de alteração. <strong>Limitações:</strong> o texto compilado não informa a data da última atualização e não substitui a publicação oficial; a Lei nº 15.280/2025 não foi lida no Diário Oficial; regras extensas aparecem resumidas. A ADPF 496, a Súmula 599 do STJ e os precedentes do STJ de 2016 e 2017 sobre o desacato foram identificados em pesquisa, mas não reconferidos nos portais oficiais dos tribunais. A situação do art. 322 e o "peculato de uso" envolvem debate doutrinário. Expressões como "doutrina majoritária" indicam posição corrente, e não lei. Confira se houve alteração posterior antes da prova e consulte o edital do seu concurso.'), "Verificação e limitações"))
add('''<div class="ending"><h2>Fim do Caderno 07</h2><p style="text-align:center">Sugestão de próximo caderno na coleção: <strong>Legislação Penal Especial</strong> (Lei de Abuso de Autoridade, Lei de Drogas, Estatuto do Desarmamento, Lei Maria da Penha).</p>
<p class="note" style="text-align:center">Mapa da Aprovação · Caderno Simplificado · Direito Penal · Caderno 07 · 1ª edição · novembro de 2026<br>Material de estudo independente. Não substitui a leitura da lei e do edital do seu concurso.</p></div>''')

doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Caderno Simplificado — Caderno 07 — Crimes contra a Administração Pública</title>
<link rel="stylesheet" href="estilo.css"></head><body>{symbols()}{"".join(P)}</body></html>'''
open(os.path.join(HERE, "miolo.html"), "w").write(doc)
print("páginas planejadas:", len(P))
