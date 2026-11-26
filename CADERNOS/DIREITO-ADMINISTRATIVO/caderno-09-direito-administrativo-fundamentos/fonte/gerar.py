"""Gera miolo.html do Caderno 09: Direito Administrativo — Fundamentos. Uso: python3 gerar.py
Base legal conferida no portal do Planalto em 26/11/2026: CF/88 (arts. 37, 173 e 175), Decreto-Lei nº 200/1967,
Lei nº 13.303/2016 e Lei nº 9.784/1999."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from componentes import *

DATA = "26 de novembro de 2026"
P = []
def add(html, first=False): P.append(page(f'<div class="marker">§§P{len(P)+1:03d}§§</div>' + html, first))
U = {1:("UNIDADE 1","Noções gerais"),2:("UNIDADE 2","Organização administrativa"),3:("UNIDADE 3","Administração indireta"),4:("UNIDADE 4","Princípios administrativos")}
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

# ================================================================ APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">A base do Direito Administrativo: quem é a Administração Pública, como ela se organiza e quais princípios a guiam.</p>
<p>Este é o <strong>Caderno 09 da coleção</strong>, o primeiro de <strong>Direito Administrativo</strong>. Ele reúne os fundamentos que aparecem em praticamente todo edital de nível médio, de Guarda Municipal aos tribunais: <strong>conceito e objeto</strong> da disciplina, <strong>Administração direta e indireta</strong>, as quatro entidades da indireta (<strong>autarquias, fundações públicas, empresas públicas e sociedades de economia mista</strong>) e os <strong>princípios administrativos</strong>.</p>
<p>O Direito Administrativo brasileiro <strong>não tem um código</strong>: suas regras estão na Constituição, em várias leis e, em boa parte, na <strong>doutrina</strong> e na <strong>jurisprudência</strong>. Por isso, este caderno separa com clareza o que está <strong>na lei</strong> e o que é <strong>construção doutrinária</strong>, porque as bancas cobram as duas coisas.</p>
{table(["Recurso","Onde está"],[["Árvore da Administração Pública","Unidade 2"],["Desconcentração x descentralização (diagrama)","Unidade 2"],["Quadro comparativo das quatro entidades da indireta","Unidade 3"],["Empresa pública x sociedade de economia mista","Unidade 3"],["Princípios com casos ilustrados e a balança da supremacia","Unidade 4"],["Erros mais comuns, flashcards e 24 questões autorais comentadas","Revisão e prática"]],["58%",None])}
{lembre(p(f'A base legal (Constituição, arts. 37, 173 e 175; Decreto-Lei nº 200/1967; Lei nº 13.303/2016; Lei nº 9.784/1999) foi conferida no portal do Planalto em <strong>{DATA}</strong>. Quando um ponto vem da doutrina ou de tribunais, o caderno avisa.'), "Fontes e atualização")}''', first=True)

TOC = [("u","UNIDADE 1 · NOÇÕES GERAIS","U1"),("","1. Conceito e fontes do Direito Administrativo","A01"),("","2. Objeto: a função administrativa","A02"),("","3. Administração Pública: sentidos e Governo x Administração","A03"),
 ("u","UNIDADE 2 · ORGANIZAÇÃO ADMINISTRATIVA","U2"),("","4. Centralização, descentralização e desconcentração","A04"),("","5. Órgãos públicos","A05"),("","6. Administração direta","A06"),("","7. Administração indireta: regras comuns","A07"),
 ("u","UNIDADE 3 · AS ENTIDADES DA ADMINISTRAÇÃO INDIRETA","U3"),("","8. Autarquias","A08"),("","9. Autarquias especiais: agências e outras figuras","A09"),("","10. Fundações públicas","A10"),("","11. Empresas públicas e sociedades de economia mista","A11"),("","12. Empresa pública x sociedade de economia mista","A12"),("","13. Quadro geral das quatro entidades","A13"),
 ("u","UNIDADE 4 · PRINCÍPIOS ADMINISTRATIVOS","U4"),("","14. Visão geral dos princípios","A14"),("","15. Legalidade","A15"),("","16. Impessoalidade","A16"),("","17. Moralidade","A17"),("","18. Publicidade","A18"),("","19. Eficiência","A19"),("","20. Supremacia do interesse público e seus limites","A20"),("","21. Indisponibilidade do interesse público","A21"),("","22. Outros princípios cobrados","A22"),
 ("u","REVISÃO E PRÁTICA","RV"),("","Mapa conceitual · Erros mais comuns","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),("","Gabarito, respostas dos treinos e referências","R4")]
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
opener("01","UNIDADE 1","Noções gerais",["Conceito e fontes do Direito Administrativo","Objeto: a função administrativa","Administração Pública: sentidos e Governo x Administração"],"U1")

add(H(1,'Conceito e fontes do <span class="hl">Direito Administrativo</span>','O ramo que organiza o Estado quando ele administra.', "A01") +
 oque(p('<strong>Direito Administrativo</strong> é o ramo do <strong>direito público</strong> que reúne os princípios e as normas que regem a <strong>função administrativa</strong>, os <strong>órgãos, agentes e entidades</strong> que a exercem e as relações entre a Administração e as pessoas.')) +
 table(["Fonte","O que é","Exemplo"],[
  ["Lei (em sentido amplo)","Fonte <b>principal</b>: Constituição, leis, medidas provisórias e decretos regulamentares","CF, art. 37; Lei nº 9.784/1999"],
  ["Jurisprudência","Decisões reiteradas dos tribunais; algumas vinculam (súmulas vinculantes, repercussão geral)","Súmula Vinculante 13 (nepotismo)"],
  ["Doutrina","Estudo dos especialistas, que cria conceitos e classificações","Classificação dos órgãos públicos"],
  ["Costumes","Práticas reiteradas da Administração; fonte secundária, nunca contra a lei","Praxe administrativa"]],["22%",None,"28%"]) +
 traduz(p('Não existe um "Código Administrativo" no Brasil. As regras estão <strong>espalhadas</strong>: Constituição, Decreto-Lei nº 200/1967, Lei de Processo Administrativo, Lei de Licitações, estatutos de servidores e muitas outras. É por isso que a <strong>doutrina</strong> tem tanto peso nesta matéria: ela organiza esse material espalhado em conceitos que as provas cobram.')) +
 memo('Direito Administrativo: ramo do <strong>direito público</strong>, <strong>não codificado</strong>. Fonte principal: a <strong>lei</strong>. Costume: fonte <strong>secundária</strong>, nunca contra a lei.'))

add(H(1,'Objeto: a <span class="hl">função administrativa</span>','O que o Direito Administrativo estuda.', "A02") +
 table(["Função do Estado","Em que consiste","Quem exerce tipicamente"],[
  ["Legislativa","Criar normas gerais e abstratas que inovam a ordem jurídica","Poder Legislativo"],
  ["Jurisdicional","Resolver conflitos com força de coisa julgada","Poder Judiciário"],
  ["<b>Administrativa</b>","Executar a lei de forma concreta e contínua, para atender ao interesse público","Poder Executivo (mas também, de forma atípica, os outros Poderes)"]],["22%",None,"30%"]) +
 table(["Critério doutrinário","Ideia central"],[
  ["Serviço público","O Direito Administrativo estudaria os serviços públicos (Escola de Bordeaux)"],
  ["Poder Executivo","Estudaria a atividade do Poder Executivo (insuficiente: os outros Poderes também administram)"],
  ["Relações jurídicas","Estudaria as relações entre o Estado e os administrados"],
  ["Teleológico","Estudaria a atividade do Estado voltada a fins concretos"],
  ["Administração Pública (adotado pela doutrina majoritária)","Estuda os órgãos, agentes e entidades que exercem a função administrativa e a própria atividade administrativa"]],["32%",None]) +
 ex(p('Quando o <b>Tribunal de Justiça</b> faz uma licitação para comprar computadores ou nomeia um servidor aprovado em concurso, ele está exercendo <b>função administrativa</b> (função atípica do Judiciário), e essas atividades seguem as regras do Direito Administrativo.')) +
 memo('Objeto do Direito Administrativo: a <strong>função administrativa</strong>, exercida <strong>tipicamente</strong> pelo Executivo e <strong>atipicamente</strong> pelo Legislativo e pelo Judiciário.'))

add(H(1,'Administração Pública: <span class="hl">os dois sentidos</span>','Quem administra e o que se administra.', "A03") +
 table(["","SENTIDO SUBJETIVO (orgânico ou formal)","SENTIDO OBJETIVO (material ou funcional)"],[
  ["Pergunta","<b>Quem</b> administra?","<b>O que</b> é administrar?"],
  ["Significado","O conjunto de <b>órgãos, agentes e entidades</b> que exercem a função administrativa","A própria <b>atividade</b> administrativa"],
  ["Grafia usada pela doutrina","Administração Pública (com iniciais <b>maiúsculas</b>)","administração pública (com iniciais <b>minúsculas</b>)"],
  ["Exemplos","Ministérios, secretarias, autarquias, empresas estatais","Serviço público, polícia administrativa, fomento e intervenção"]],["20%",None,None]) +
 table(["","GOVERNO","ADMINISTRAÇÃO"],[
  ["Função","Política: fixar diretrizes, planos e prioridades","Técnica: executar as decisões"],
  ["Atuação","Com ampla discricionariedade política","Subordinada à lei, com responsabilidade técnica e legal"],
  ["Exemplo","Decidir construir hospitais em vez de estádios","Licitar e construir o hospital"]],["16%",None,None]) +
 memo('Sentido <strong>subjetivo</strong> = <strong>quem</strong> (órgãos, agentes, entidades). Sentido <strong>objetivo</strong> = <strong>o quê</strong> (atividade). Governo <strong>decide</strong>; Administração <strong>executa</strong>.'))

atencao(
 cards([("shield","Polícia administrativa","Limita direitos individuais em favor do interesse coletivo: fiscalização sanitária, de trânsito, de posturas.",C['blue']),("cross","Serviço público","Oferece utilidades à população: transporte, saúde, educação, coleta de lixo.",C['navy']),("coin","Fomento","Incentiva a iniciativa privada de interesse público: subvenções, incentivos.",C['golddeep']),("gavel","Intervenção","Atua no domínio econômico e na propriedade: desapropriação, regulação.",C['red'])],4) +
 ex(p('Uma questão afirma: "Em sentido objetivo, a Administração Pública é o conjunto de órgãos e entidades que exercem a função administrativa." <b>Errado</b>: essa é a definição em sentido <b>subjetivo</b>. Em sentido objetivo, a Administração é a <b>atividade</b> (serviço público, polícia administrativa, fomento, intervenção).')) +
 pega('<ul><li>Não confunda os sentidos: <b>subjetivo/orgânico/formal</b> olha para <b>quem</b>; <b>objetivo/material/funcional</b> olha para a <b>atividade</b>.</li><li>A <b>guarda municipal</b> fiscalizando uma feira exerce atividade de <b>polícia administrativa</b>, que é diferente da polícia judiciária (investigação de crimes).</li></ul>'),
 None, "Atividades da Administração")

treino(1, [
 ("O Direito Administrativo brasileiro está reunido em um código próprio.","E","Não é codificado; suas normas estão espalhadas em várias leis."),
 ("O costume pode ser fonte do Direito Administrativo, desde que não contrarie a lei.","C","Fonte secundária."),
 ("Em sentido objetivo, Administração Pública é o conjunto de órgãos, agentes e entidades que exercem a função administrativa.","E","Essa é a definição em sentido subjetivo."),
 ("O Poder Judiciário pode exercer função administrativa de forma atípica.","C","Ex.: licitações e nomeação de servidores."),
 ("Governo e Administração são expressões sinônimas para a doutrina.","E","Governo fixa diretrizes políticas; a Administração executa."),
 ("A polícia administrativa é uma das atividades da Administração Pública em sentido objetivo.","C","Junto com o serviço público, o fomento e a intervenção.")])

# ================================================================ UNIDADE 2
opener("02","UNIDADE 2","Organização administrativa",["Centralização, descentralização e desconcentração","Órgãos públicos","Administração direta","Administração indireta: regras comuns"],"U2")

def descon():
    N,G=C['navy'],C['blue']
    s = f'<figure><svg viewBox="0 0 640 250" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter"><defs><marker id="ar2" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L10,5 L0,10 z" fill="{C["ink"]}"/></marker></defs>'
    # left: desconcentração
    s += f'<rect x="4" y="4" width="306" height="242" rx="16" fill="{NV}" stroke="{N}" stroke-width="2.5"/><text x="157" y="28" text-anchor="middle" font-size="15" font-weight="900" fill="{N}">DESCONCENTRAÇÃO</text><text x="157" y="46" text-anchor="middle" font-size="10.5" fill="{C["muted"]}">dentro da MESMA pessoa jurídica</text>'
    s += f'<rect x="40" y="58" width="234" height="176" rx="14" fill="#fff" stroke="{N}" stroke-width="2" stroke-dasharray="6 4"/><text x="157" y="76" text-anchor="middle" font-size="10.5" font-weight="800" fill="{N}">MUNICÍPIO (uma só pessoa jurídica)</text>'
    s += f'<rect x="107" y="86" width="100" height="36" rx="8" fill="{N}"/><text x="157" y="109" text-anchor="middle" font-size="11" font-weight="900" fill="#fff">PREFEITURA</text>'
    for k,t in enumerate(["Saúde","Educação","Segurança"]):
        x = 50+k*73
        s += f'<line x1="157" y1="122" x2="{x+33}" y2="158" stroke="{C["ink"]}" stroke-width="1.8" marker-end="url(#ar2)"/><rect x="{x}" y="156" width="68" height="40" rx="7" fill="{NV}" stroke="{N}" stroke-width="1.6"/><text x="{x+34}" y="172" text-anchor="middle" font-size="8.5" font-weight="700" fill="{C["muted"]}">Secretaria</text><text x="{x+34}" y="187" text-anchor="middle" font-size="9.5" font-weight="900" fill="{N}">{t}</text>'
    s += f'<text x="157" y="220" text-anchor="middle" font-size="10.5" font-weight="900" fill="{N}">cria ÓRGÃOS · há HIERARQUIA</text>'
    # right: descentralização
    s += f'<rect x="330" y="4" width="306" height="242" rx="16" fill="{C["sky"]}" stroke="{G}" stroke-width="2.5"/><text x="483" y="28" text-anchor="middle" font-size="15" font-weight="900" fill="{G}">DESCENTRALIZAÇÃO</text><text x="483" y="46" text-anchor="middle" font-size="10.5" fill="{C["muted"]}">para OUTRA pessoa jurídica</text>'
    s += f'<rect x="350" y="70" width="110" height="60" rx="10" fill="#fff" stroke="{N}" stroke-width="2" stroke-dasharray="6 4"/><text x="405" y="96" text-anchor="middle" font-size="11" font-weight="900" fill="{N}">MUNICÍPIO</text><text x="405" y="113" text-anchor="middle" font-size="9.5" fill="{C["muted"]}">pessoa jurídica 1</text>'
    s += f'<rect x="506" y="70" width="114" height="60" rx="10" fill="#fff" stroke="{G}" stroke-width="2" stroke-dasharray="6 4"/><text x="563" y="96" text-anchor="middle" font-size="11" font-weight="900" fill="{G}">AUTARQUIA</text><text x="563" y="113" text-anchor="middle" font-size="9.5" fill="{C["muted"]}">pessoa jurídica 2</text>'
    s += f'<line x1="462" y1="100" x2="502" y2="100" stroke="{C["ink"]}" stroke-width="2.4" marker-end="url(#ar2)"/><text x="482" y="150" text-anchor="middle" font-size="10" fill="{C["ink"]}">transfere o serviço (por lei)</text>'
    s += f'<text x="483" y="186" text-anchor="middle" font-size="10.5" font-weight="900" fill="{G}">cria ou usa ENTIDADES</text><text x="483" y="204" text-anchor="middle" font-size="10.5" font-weight="900" fill="{G}">SEM hierarquia: há controle</text><text x="483" y="222" text-anchor="middle" font-size="10.5" font-weight="900" fill="{G}">(tutela / supervisão)</text>'
    return s + '</svg><figcaption>Desconcentração distribui tarefas por órgãos; descentralização transfere a outra pessoa.</figcaption></figure>'

add(H(2,'Centralização, descentralização e <span class="hl">desconcentração</span>','Como o Estado distribui suas tarefas.', "A04") +
 descon() +
 table(["","DESCONCENTRAÇÃO","DESCENTRALIZAÇÃO"],[
  ["Pessoas jurídicas","<b>Uma só</b>: a tarefa é distribuída entre órgãos internos","<b>Duas</b>: a tarefa passa para outra pessoa"],
  ["Resultado","Cria <b>órgãos</b> (sem personalidade jurídica)","Cria ou usa <b>entidades</b> (com personalidade jurídica) ou particulares"],
  ["Relação","<b>Hierarquia</b> (subordinação)","<b>Vinculação</b>: controle ou tutela, sem hierarquia"],
  ["Exemplo","Prefeitura cria a Secretaria de Segurança","Município cria uma autarquia de trânsito"]],["18%",None,None]))

atencao(
 table(["Tipo de descentralização (doutrina)","Como ocorre","Exemplo"],[
  ["Por <b>outorga</b> (por serviços, funcional ou técnica)","Por <b>lei</b>: transfere a <b>titularidade e a execução</b> do serviço a uma entidade da Administração indireta","Lei cria autarquia previdenciária"],
  ["Por <b>delegação</b> (por colaboração)","Por <b>contrato</b> ou <b>ato</b>: transfere só a <b>execução</b> a um particular, por prazo determinado","Concessão de transporte coletivo a empresa privada (CF, art. 175)"],
  ["<b>Territorial</b> (geográfica)","Entidade com competência genérica sobre uma área","Territórios federais"]],["30%",None,"28%"]) +
 ex(p('A Prefeitura divide seus serviços entre as Secretarias de Saúde, Educação e Segurança: <b>desconcentração</b>. A mesma Prefeitura cria, por lei, uma autarquia para cuidar da água e do esgoto: <b>descentralização por outorga</b>. Depois, concede o transporte de ônibus a uma empresa privada, por licitação: <b>descentralização por delegação</b>.')) +
 pega('<ul><li><b>Desconcentração</b> = <b>órgãos</b> + <b>hierarquia</b>. <b>Descentralização</b> = <b>outra pessoa</b> + <b>controle</b> (sem hierarquia).</li><li>As duas podem acontecer juntas: uma autarquia (descentralização) pode se dividir internamente em departamentos (desconcentração).</li><li>Centralização é o Estado executar a tarefa diretamente, pelos órgãos da Administração direta.</li></ul>'),
 ["desconcentração","descentralização","órgão","entidade","hierarquia","tutela / supervisão","outorga","delegação"])

add(H(2,'<span class="hl">Órgãos</span> públicos','Centros de competência sem personalidade jurídica.', "A05") +
 lei("Art. 1º, § 2º, I e II · Lei nº 9.784/1999 (em síntese)",'<p><b>Órgão</b>: a unidade de atuação integrante da estrutura da Administração direta e da estrutura da Administração indireta. <b>Entidade</b>: a unidade de atuação dotada de personalidade jurídica.</p>') +
 traduz(p('Pela <strong>teoria do órgão</strong> (ou da imputação, de Otto Gierke), quando o agente atua, quem age é a <strong>pessoa jurídica</strong>: a vontade do agente é <strong>imputada</strong> ao Estado. Por isso o órgão não responde sozinho; quem responde é a pessoa jurídica a que ele pertence. O órgão <strong>não tem personalidade jurídica</strong>, mas alguns, como as Casas Legislativas, têm <strong>capacidade processual</strong> para defender suas prerrogativas.'),"profa") +
 table(["Classificação (doutrina)","Tipos"],[
  ["Quanto à posição","<b>Independentes</b> (topo dos Poderes: Presidência, Congresso, tribunais); <b>autônomos</b> (ministérios, secretarias); <b>superiores</b> (gabinetes, departamentos); <b>subalternos</b> (execução)"],
  ["Quanto à estrutura","<b>Simples</b> (sem órgãos internos) ou <b>compostos</b> (com outros órgãos dentro)"],
  ["Quanto à atuação","<b>Singulares</b> (decisão de uma pessoa) ou <b>colegiados</b> (decisão de um grupo, como conselhos)"]],["26%",None]) +
 memo('Órgão: <strong>sem personalidade jurídica</strong>, existe na direta <strong>e</strong> na indireta. Entidade: <strong>com personalidade jurídica</strong>. Teoria adotada: <strong>teoria do órgão (imputação)</strong>.'))

def arvore():
    N,G,O=C['navy'],C['blue'],C['golddeep']
    s = f'<figure><svg viewBox="0 0 640 300" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    s += f'<g stroke="#9db0c8" stroke-width="2.5" fill="none"><path d="M320 52 V74 M150 74 H490 M150 74 V92 M490 74 V92 M150 152 V172 M60 172 H240 M60 172 V188 M150 172 V188 M240 172 V188 M490 152 V172 M380 172 H600 M380 172 V188 M453 172 V188 M527 172 V188 M600 172 V188"/></g>'
    s += f'<rect x="180" y="6" width="280" height="46" rx="12" fill="{N}"/><text x="320" y="26" text-anchor="middle" font-size="13" font-weight="900" fill="#fff">ADMINISTRAÇÃO PÚBLICA</text><text x="320" y="43" text-anchor="middle" font-size="10" fill="#cfe0f2">sentido subjetivo (DL nº 200/1967, art. 4º)</text>'
    s += f'<rect x="40" y="92" width="220" height="60" rx="12" fill="{C["goldsoft"]}" stroke="{O}" stroke-width="2.4"/><text x="150" y="116" text-anchor="middle" font-size="14" font-weight="900" fill="{O}">DIRETA</text><text x="150" y="136" text-anchor="middle" font-size="10" fill="{C["ink"]}">entes políticos e seus órgãos</text>'
    s += f'<rect x="380" y="92" width="220" height="60" rx="12" fill="{C["sky"]}" stroke="{G}" stroke-width="2.4"/><text x="490" y="116" text-anchor="middle" font-size="14" font-weight="900" fill="{G}">INDIRETA</text><text x="490" y="136" text-anchor="middle" font-size="10" fill="{C["ink"]}">entidades com personalidade própria</text>'
    for x,t in [(60,"União"),(150,"Estados e DF"),(240,"Municípios")]:
        s += f'<rect x="{x-42}" y="188" width="84" height="40" rx="9" fill="#fff" stroke="{O}" stroke-width="1.8"/><text x="{x}" y="213" text-anchor="middle" font-size="10" font-weight="800" fill="{C["ink"]}">{t}</text>'
    for x,a,b in [(380,"Autarquia","direito público"),(453,"Fundação","púb. ou priv."),(527,"Empresa","pública · privado"),(600,"Soc. Econ.","Mista · privado")]:
        s += f'<rect x="{x-35}" y="188" width="70" height="56" rx="9" fill="#fff" stroke="{G}" stroke-width="1.8"/><text x="{x}" y="210" text-anchor="middle" font-size="9.6" font-weight="900" fill="{C["ink"]}">{a}</text><text x="{x}" y="228" text-anchor="middle" font-size="8" fill="{C["muted"]}">{b}</text>'
    s += f'<text x="150" y="258" text-anchor="middle" font-size="10.5" font-weight="800" fill="{O}">ministérios, secretarias = órgãos</text><text x="150" y="276" text-anchor="middle" font-size="10" fill="{C["muted"]}">(desconcentração)</text>'
    s += f'<text x="490" y="268" text-anchor="middle" font-size="10.5" font-weight="800" fill="{G}">criadas ou autorizadas por lei específica</text><text x="490" y="286" text-anchor="middle" font-size="10" fill="{C["muted"]}">(descentralização · CF, art. 37, XIX)</text>'
    return s + '</svg><figcaption>A árvore da Administração Pública.</figcaption></figure>'

add(H(2,'Administração <span class="hl">direta</span>','Os entes políticos e seus órgãos.', "A06") +
 lei("Art. 4º, I · Decreto-Lei nº 200/1967",'<p>A Administração Federal compreende: I - A Administração Direta, que se constitui dos serviços integrados na estrutura administrativa da Presidência da República e dos Ministérios; [...]</p>') +
 arvore() +
 traduz(p('A Administração direta é formada pelas <strong>pessoas políticas</strong> (União, Estados, Distrito Federal e Municípios), que têm <strong>autonomia política</strong> e criam leis, e pelos seus <strong>órgãos</strong>. Embora o Decreto-Lei nº 200/1967 trate da esfera federal, a doutrina aplica a mesma estrutura aos Estados, ao DF e aos Municípios.')) +
 memo('Direta = <strong>entes políticos</strong> (pessoas jurídicas de <strong>direito público</strong>) + seus <strong>órgãos</strong>. A <strong>guarda municipal</strong> é órgão da Administração direta do Município.'))

add(H(2,'Administração indireta: <span class="hl">regras comuns</span>','O que as quatro entidades têm em comum.', "A07") +
 lei(cf("Art. 37, XIX"),'<p>XIX - somente por lei específica poderá ser criada autarquia e autorizada a instituição de empresa pública, de sociedade de economia mista e de fundação, cabendo à lei complementar, neste último caso, definir as áreas de sua atuação;</p>') +
 table(["Característica comum","Explicação"],[
  ["Personalidade jurídica própria","Cada entidade é uma pessoa distinta do ente que a criou: tem patrimônio, receitas e responsabilidade próprios"],
  ["Criação por lei específica","Autarquia: <b>criada</b> pela lei. Empresa pública, sociedade de economia mista e fundação: lei <b>autoriza</b> a criação, que se completa com o registro"],
  ["Princípio da especialidade","Só pode atuar na finalidade prevista na lei que a criou ou autorizou"],
  ["Controle finalístico","O ente político exerce <b>tutela</b> ou <b>supervisão ministerial</b> (DL nº 200/1967, arts. 19 e 26), mas <b>não há hierarquia</b>"],
  ["Vinculação a um ministério ou secretaria","A entidade fica vinculada ao órgão da área de sua atividade principal (DL nº 200/1967, art. 4º, parágrafo único)"],
  ["Subsidiárias (CF, art. 37, XX)","Depende de autorização legislativa, em cada caso, a criação de subsidiárias e a participação em empresa privada"]],["30%",None]) +
 pega('<ul><li><b>Autarquia é criada pela lei</b>; as demais têm a criação <b>autorizada</b> por lei. Essa diferença de verbo cai muito.</li><li>Entre a entidade e o ente político <b>não há hierarquia</b>: há <b>controle finalístico</b>, também chamado de tutela ou supervisão.</li><li>A lei complementar define as <b>áreas de atuação</b> das <b>fundações</b>, e não as das empresas estatais.</li></ul>'))

treino(2, [
 ("A desconcentração pressupõe a existência de duas pessoas jurídicas.","E","Ocorre dentro da mesma pessoa jurídica; quem envolve outra pessoa é a descentralização."),
 ("Entre a entidade da Administração indireta e o ente que a criou há relação de hierarquia.","E","Há controle finalístico (tutela/supervisão), sem hierarquia."),
 ("Órgãos públicos não têm personalidade jurídica.","C","Lei nº 9.784/1999, art. 1º, § 2º."),
 ("A autarquia é criada por lei específica, enquanto a lei apenas autoriza a instituição de empresa pública e de sociedade de economia mista.","C","CF, art. 37, XIX."),
 ("Na descentralização por delegação, transfere-se a titularidade do serviço ao particular.","E","Transfere-se apenas a execução; a titularidade fica com o Estado."),
 ("Os órgãos públicos existem apenas na Administração direta.","E","Existem também na estrutura da Administração indireta.")])

# ================================================================ UNIDADE 3
opener("03","UNIDADE 3","As entidades da Administração indireta",["Autarquias","Autarquias especiais","Fundações públicas","Empresas públicas e sociedades de economia mista","Empresa pública x sociedade de economia mista","Quadro geral das quatro entidades"],"U3")

add(H(3,'<span class="hl">Autarquias</span>','O "braço" do Estado com regime de direito público.', "A08") +
 lei("Art. 5º, I · Decreto-Lei nº 200/1967",'<p>Autarquia - o serviço autônomo, criado por lei, com personalidade jurídica, patrimônio e receita próprios, para executar atividades típicas da Administração Pública, que requeiram, para seu melhor funcionamento, gestão administrativa e financeira descentralizada.</p>') +
 table(["Regime jurídico","Como funciona"],[
  ["Natureza","Pessoa jurídica de <b>direito público</b>, criada por <b>lei específica</b>"],
  ["Atividades","<b>Típicas de Estado</b>, que exigem prerrogativas públicas (fiscalizar, regular, prestar serviço público)"],
  ["Bens","<b>Bens públicos</b>: impenhoráveis, imprescritíveis (não sofrem usucapião) e com alienação condicionada à lei"],
  ["Tributos","<b>Imunidade tributária recíproca</b> sobre patrimônio, renda e serviços ligados às suas finalidades (CF, art. 150, § 2º)"],
  ["Processo","Prerrogativas processuais da Fazenda Pública, como prazos diferenciados; dívidas pagas por precatório"],
  ["Responsabilidade","<b>Objetiva</b> (CF, art. 37, § 6º)"],
  ["Pessoal e contratos","Concurso público e licitação; regime de pessoal em regra estatutário (ver nota abaixo)"]],["24%",None]) +
 lembre(p('Em <strong>2024</strong>, no julgamento da <strong>ADI 2.135</strong>, o STF validou a mudança feita pela EC nº 19/1998 no art. 39 da Constituição, que tinha retirado a obrigatoriedade do <strong>regime jurídico único</strong>. Segundo as publicações sobre o julgamento, passou a ser possível contratar novos servidores também pelo regime da CLT, sem efeito retroativo para quem já está no regime estatutário. O alcance prático da decisão ainda é debatido.'), "Regime de pessoal: decisão do STF"))

atencao(
 flow([("capitol",["LEI","específica","cria"]),("idcard",["AUTARQUIA","direito público"]),("shield",["ATIVIDADE","típica de","Estado"]),("scales",["REGIME","de direito","público"])],
      "Autarquia: criada por lei para fazer o que é típico do Estado, com as mesmas prerrogativas dele.", colors=colors("n","b","o","r")) +
 ex(p('O <b>INSS</b> (previdência), o <b>Ibama</b> (fiscalização ambiental) e o <b>Banco Central</b> são autarquias federais. No Município, uma autarquia de água e esgoto ou um departamento autônomo de trânsito criado por lei também são autarquias. Se a autarquia de trânsito causa um dano a um motorista, ela responde de forma <b>objetiva</b>, e seus bens <b>não podem ser penhorados</b>: o pagamento segue o regime de precatórios.')) +
 pega('<ul><li>Autarquia <b>não</b> explora atividade econômica: exerce atividade <b>típica de Estado</b>.</li><li>Autarquia é <b>criada</b> pela lei, sem necessidade de registro em cartório.</li><li>A imunidade tributária recíproca vale para patrimônio, renda e serviços <b>ligados às finalidades essenciais</b> da autarquia.</li></ul>'),
 ["direito público","criada por lei","atividade típica","bens públicos","imunidade recíproca","responsabilidade objetiva"])

add(H(3,'Autarquias <span class="hl">especiais</span>','Agências reguladoras, agências executivas e outras figuras.', "A09") +
 table(["Figura","O que é (em síntese)","Exemplo"],[
  ["Autarquia de regime especial","Autarquia com mais autonomia que a comum, definida na lei que a cria","Universidades federais, Banco Central"],
  ["Agência reguladora","Autarquia de regime especial que <b>regula e fiscaliza</b> um setor; dirigentes com <b>mandato fixo</b> e autonomia técnica (Lei nº 13.848/2019)","Anatel, Aneel, ANS, Anvisa"],
  ["Agência executiva","<b>Qualificação</b> (título) dada a uma autarquia ou fundação que celebra <b>contrato de gestão</b> com o ministério para ampliar sua autonomia (CF, art. 37, § 8º)","Não é uma nova entidade: é um título"],
  ["Associação pública","Consórcio público com personalidade de <b>direito público</b> (Lei nº 11.107/2005); integra a Administração indireta dos entes consorciados","Consórcio intermunicipal de saúde"],
  ["Conselhos profissionais","Reconhecidos pelo STF como de natureza autárquica; a <b>OAB</b> é exceção, por ter regime próprio (ADI 3.026)","CREA, CRM, CRC"]],["24%",None,"24%"]) +
 ex(p('Uma autarquia federal de fiscalização assina com seu ministério um contrato de gestão, comprometendo-se com metas de desempenho, e recebe por decreto o título de <b>agência executiva</b>. Ela continua sendo a <b>mesma autarquia</b>: só ganhou uma qualificação. Já a <b>Anatel</b> nasceu como agência reguladora por lei, com dirigentes de mandato fixo.')) +
 memo('Agência <strong>reguladora</strong>: autarquia especial que <strong>regula</strong> um setor. Agência <strong>executiva</strong>: <strong>título</strong> dado por contrato de gestão. Associação pública: consórcio de <strong>direito público</strong>.'))

add(H(3,'Fundações <span class="hl">públicas</span>','Um patrimônio personalizado a serviço de um fim social.', "A10") +
 lei("Art. 5º, IV · Decreto-Lei nº 200/1967 (em síntese)",'<p>Fundação Pública: entidade dotada de personalidade jurídica de direito privado, sem fins lucrativos, criada em virtude de autorização legislativa, para desenvolver atividades que não exijam execução por órgãos ou entidades de direito público, com autonomia administrativa, patrimônio próprio e funcionamento custeado por recursos da União e de outras fontes. (Incluído pela Lei nº 7.596/1987)</p>') +
 table(["","FUNDAÇÃO DE DIREITO PÚBLICO (fundação autárquica)","FUNDAÇÃO DE DIREITO PRIVADO"],[
  ["Criação","<b>Criada</b> diretamente pela lei, como uma autarquia","Lei <b>autoriza</b>; a personalidade surge com a inscrição da escritura no Registro Civil de Pessoas Jurídicas (DL nº 200/1967, art. 5º, § 3º)"],
  ["Regime","De direito público: prerrogativas semelhantes às das autarquias","Híbrido: direito privado, com regras de direito público (concurso, licitação, controle)"],
  ["Fonte","Construção da doutrina e do STF, que admitem as duas espécies","Definição do DL nº 200/1967"]],["16%",None,None]) +
 traduz(p('A ideia de fundação é a de um <strong>patrimônio</strong> que ganha personalidade para cumprir um <strong>fim social</strong>: educação, cultura, pesquisa, saúde. Ela <strong>não tem fins lucrativos</strong>. O DL nº 200/1967 define a fundação pública como de direito privado, mas o STF e a doutrina reconhecem também a fundação pública de <strong>direito público</strong>, que, na prática, é uma espécie de autarquia.'),"profa") +
 memo('Fundação pública: <strong>patrimônio + fim social + sem lucro</strong>. Pode ser de <strong>direito público</strong> (criada por lei) ou de <strong>direito privado</strong> (autorizada por lei + registro). A <strong>lei complementar</strong> define suas áreas de atuação (CF, art. 37, XIX).'))

add(H(3,'Empresas públicas e <span class="hl">sociedades de economia mista</span>','As empresas estatais (Lei nº 13.303/2016).', "A11") +
 lei("Arts. 3º e 4º · Lei nº 13.303/2016 (trechos e síntese)",'<p>Art. 3º "Empresa pública é a entidade dotada de personalidade jurídica de direito privado, com criação autorizada por lei e com patrimônio próprio", cujo capital social é integralmente detido pela União, pelos Estados, pelo Distrito Federal ou pelos Municípios.<br>Art. 4º Sociedade de economia mista é a entidade dotada de personalidade jurídica de direito privado, com criação autorizada por lei, sob a forma de sociedade anônima, cujas ações com direito a voto pertençam em sua maioria à União, aos Estados, ao Distrito Federal, aos Municípios ou a entidade da administração indireta.</p>') +
 table(["Ponto","Regra"],[
  ["Por que existem","Exploração de atividade econômica pelo Estado, quando necessária aos imperativos da segurança nacional ou a <b>relevante interesse coletivo</b> (CF, art. 173; Lei nº 13.303/2016, art. 2º, § 1º); também prestam serviços públicos"],
  ["Regime","<b>Híbrido</b>: direito privado (como as empresas), com regras de direito público (concurso, licitação, controle pelos tribunais de contas)"],
  ["Privilégios fiscais (CF, art. 173, § 2º)","As que exploram atividade econômica <b>não podem gozar de privilégios fiscais</b> não extensivos às do setor privado"],
  ["Função social (Lei nº 13.303/2016, art. 27)","Realizar o interesse coletivo ou o imperativo de segurança nacional expresso na lei que autorizou sua criação"],
  ["Novidade (Lei nº 15.177/2025)","No mínimo <b>30% de mulheres</b> entre os membros titulares dos conselhos de administração (art. 19-A)"]],["28%",None]))

ep = scene3([("EMPRESA PÚBLICA",C['blue'],C['sky'],"prof",["Capital 100%","público. Qualquer","forma societária."],"ex.: Caixa, Correios"),
 ("SOC. ECONOMIA MISTA",C['golddeep'],C['goldsoft'],"profa",["Maioria das ações","com voto é pública.","Sempre S.A."],"ex.: Banco do Brasil, Petrobras"),
 ("ATIVIDADE",C['navy'],NV,"prof",["Exploram atividade","econômica ou prestam","serviço público."],"regime híbrido")], "Situação ilustrada: o capital e a forma separam as duas estatais.")
add(H(3,'Empresa pública x <span class="hl">sociedade de economia mista</span>','Capital, forma e foro.', "A12") + ep +
 table(["","EMPRESA PÚBLICA","SOCIEDADE DE ECONOMIA MISTA"],[
  ["Capital","<b>Integralmente</b> público (pode haver participação de outras pessoas públicas, desde que o ente controlador mantenha a maioria do capital votante)","Público e privado: a <b>maioria das ações com direito a voto</b> é pública"],
  ["Forma societária","<b>Qualquer</b> forma admitida em direito","Somente <b>sociedade anônima</b>"],
  ["Foro (federais)","<b>Justiça Federal</b> (CF, art. 109, I)","<b>Justiça Estadual</b> (Súmula 556 do STF)"],
  ["Em comum","Direito privado · criação autorizada por lei · concurso público · licitação · não se sujeitam à falência (Lei nº 11.101/2005, art. 2º)","Direito privado · criação autorizada por lei · concurso público · licitação · não se sujeitam à falência"]],["16%",None,None]))

atencao(
 table(["Situação","Consequência"],[
  ["Estatal que <b>explora atividade econômica</b> em concorrência","Regime mais próximo do privado; sem privilégios fiscais (CF, art. 173, § 2º)"],
  ["Estatal que <b>presta serviço público</b> (ex.: Correios)","O STF reconhece prerrogativas próprias da Fazenda, como imunidade tributária recíproca e impenhorabilidade de bens ligados ao serviço"],
  ["Empregados","Regidos pela <b>CLT</b>, mas admitidos por <b>concurso público</b> (CF, art. 37, II)"],
  ["Responsabilidade","Objetiva quando prestam serviço público (CF, art. 37, § 6º); quando exploram atividade econômica, seguem as regras do direito privado"]],["36%",None]) +
 ex(p('A <b>Caixa Econômica Federal</b> é empresa pública: capital integralmente da União, e as ações contra ela correm na <b>Justiça Federal</b>. O <b>Banco do Brasil</b> é sociedade de economia mista: tem acionistas privados, é sociedade anônima, e as ações contra ele correm na <b>Justiça Estadual</b>.')) +
 pega('<ul><li>Sociedade de economia mista é <b>sempre S.A.</b>; empresa pública pode ter <b>qualquer forma</b>.</li><li>Nas duas, a criação é <b>autorizada</b> por lei, e não feita diretamente pela lei.</li><li>Os empregados das estatais são celetistas, mas <b>fazem concurso público</b>.</li><li>Empresa pública e sociedade de economia mista <b>não estão sujeitas à falência</b>.</li></ul>'),
 ["capital integralmente público","maioria das ações com voto","sociedade anônima","Justiça Federal","Súmula 556 do STF","regime híbrido"])

add(H(3,'Quadro geral das <span class="hl">quatro entidades</span>','Para revisar de uma vez.', "A13") +
 table(["","AUTARQUIA","FUNDAÇÃO PÚBLICA","EMPRESA PÚBLICA","SOC. ECONOMIA MISTA"],[
  ["Personalidade","Direito público","Público ou privado","Direito privado","Direito privado"],
  ["Criação","<b>Criada</b> por lei","Lei cria (pública) ou autoriza (privada)","Lei <b>autoriza</b>","Lei <b>autoriza</b>"],
  ["Atividade","Típica de Estado","Social, sem lucro","Econômica ou serviço público","Econômica ou serviço público"],
  ["Capital","—","Patrimônio afetado","100% público","Maioria votante pública"],
  ["Forma","—","—","Qualquer","S.A."],
  ["Pessoal","Em regra estatutário","Conforme o regime","CLT + concurso","CLT + concurso"],
  ["Bens","Públicos","Públicos (se de direito público)","Privados (com ressalvas no serviço público)","Privados (com ressalvas no serviço público)"]],["14%",None,None,None,None]) +
 memo('<strong>Direito público</strong>: autarquia (e fundação de direito público). <strong>Direito privado</strong>: empresa pública, sociedade de economia mista (e fundação de direito privado). <strong>Criada</strong> por lei: só a autarquia (e a fundação de direito público).'))

treino(3, [
 ("A autarquia é pessoa jurídica de direito público criada por lei específica.","C","CF, art. 37, XIX; DL nº 200/1967, art. 5º, I."),
 ("As autarquias podem ser criadas para explorar atividade econômica com finalidade lucrativa.","E","Exercem atividades típicas de Estado."),
 ("A agência executiva é uma nova espécie de entidade da Administração indireta.","E","É uma qualificação dada a autarquia ou fundação que celebra contrato de gestão."),
 ("A sociedade de economia mista pode adotar qualquer forma societária.","E","Só a forma de sociedade anônima (Lei nº 13.303/2016, art. 4º)."),
 ("O capital da empresa pública é integralmente detido por entes públicos.","C","Lei nº 13.303/2016, art. 3º."),
 ("As causas envolvendo sociedade de economia mista federal são, em regra, de competência da Justiça Federal.","E","Justiça Estadual (Súmula 556 do STF).")])

# ================================================================ UNIDADE 4
opener("04","UNIDADE 4","Princípios administrativos",["Visão geral","Legalidade","Impessoalidade","Moralidade","Publicidade","Eficiência","Supremacia do interesse público e seus limites","Indisponibilidade do interesse público","Outros princípios cobrados"],"U4")

add(H(4,'Princípios: <span class="hl">visão geral</span>','Expressos na Constituição, na lei e implícitos.', "A14") +
 lei(cf("Art. 37, caput (redação da EC nº 19/1998)"),'<p>Art. 37. A administração pública direta e indireta de qualquer dos Poderes da União, dos Estados, do Distrito Federal e dos Municípios obedecerá aos princípios de legalidade, impessoalidade, moralidade, publicidade e eficiência e, também, ao seguinte: [...]</p>') +
 cards([("#L","Legalidade","Só fazer o que a lei permite."),("#I","Impessoalidade","Agir para todos, sem favorecer nem perseguir."),("#M","Moralidade","Agir com ética, probidade e boa-fé."),("#P","Publicidade","Dar transparência aos atos."),("#E","Eficiência","Fazer bem, com rapidez e economia.")],5) +
 table(["Onde estão","Princípios"],[
  ["CF, art. 37, caput (expressos, “LIMPE”)","Legalidade, impessoalidade, moralidade, publicidade e eficiência"],
  ["Lei nº 9.784/1999, art. 2º","Legalidade, finalidade, motivação, razoabilidade, proporcionalidade, moralidade, ampla defesa, contraditório, segurança jurídica, interesse público e eficiência"],
  ["Doutrina (supraprincípios)","<b>Supremacia</b> do interesse público e <b>indisponibilidade</b> do interesse público, que formam o chamado <b>regime jurídico-administrativo</b>"]],["30%",None]) +
 memo('<strong>LIMPE</strong> vale para a Administração <strong>direta e indireta</strong>, de <strong>todos os Poderes</strong> e de <strong>todos os entes</strong>. Eficiência entrou com a <strong>EC nº 19/1998</strong>.'))

add(H(4,'<span class="hl">Legalidade</span>','O administrador só faz o que a lei autoriza.', "A15") +
 scene3([("PARTICULAR",C['green'],C['greensoft'],"prof",["Pode fazer tudo","o que a lei","não proíbe."],"autonomia da vontade"),
  ("ADMINISTRADOR",C['blue'],C['sky'],"profa",["Só pode fazer","o que a lei","permite ou manda."],"legalidade estrita"),
  ("RESULTADO",C['navy'],NV,"prof",["Ato sem base","legal é ilegal","e deve ser anulado."],"controle")], "Situação ilustrada: a mesma lei, duas leituras.") +
 traduz(p('Para o particular, vale a regra do art. 5º, II, da Constituição: ninguém é obrigado a fazer ou deixar de fazer algo senão em virtude de lei. Para a Administração, a lógica é inversa: ela só age quando a <strong>lei autoriza</strong>. A Lei nº 9.784/1999 fala em atuação conforme <strong>"a lei e o Direito"</strong>, o que inclui os princípios, e não só o texto da lei (a chamada <strong>juridicidade</strong>).')) +
 memo('Particular: tudo o que a lei <strong>não proíbe</strong>. Administração: só o que a lei <strong>permite</strong>. Ato ilegal: deve ser <strong>anulado</strong>.'))

add(H(4,'<span class="hl">Impessoalidade</span>','Agir para todos, e em nome da instituição.', "A16") +
 table(["Sentido","O que significa","Exemplo"],[
  ["Finalidade","Todo ato deve buscar o <b>interesse público</b>, sem favorecer nem perseguir ninguém","Fila única por ordem de chegada; concurso público; licitação"],
  ["Vedação à promoção pessoal (CF, art. 37, § 1º)","A publicidade de atos, programas, obras e campanhas deve ter caráter educativo, informativo ou de orientação social, sem nomes, símbolos ou imagens que caracterizem promoção pessoal","Placa de obra sem o nome ou a foto do prefeito"],
  ["Imputação ao órgão","Os atos são do <b>órgão</b>, e não do agente que os pratica","Atos do “funcionário de fato” podem ser mantidos perante terceiros de boa-fé"],
  ["Isonomia","Tratar igualmente quem está na mesma situação","Critérios objetivos em seleções"]],["24%",None,"28%"]) +
 lembre(p('A <strong>Súmula Vinculante 13</strong> do STF proíbe o <strong>nepotismo</strong>: a nomeação de cônjuge, companheiro ou parente em linha reta, colateral ou por afinidade, <strong>até o terceiro grau</strong>, da autoridade nomeante ou de servidor da mesma pessoa jurídica com cargo de direção, chefia ou assessoramento, para cargo em comissão, função de confiança ou função gratificada, inclusive o <strong>nepotismo cruzado</strong> (troca de nomeações). A jurisprudência do STF admite, salvo fraude, a nomeação de parentes para <strong>cargos políticos</strong> (como secretário municipal), tema discutido no Tema 1.000.'), "Nepotismo: Súmula Vinculante 13") +
 memo('Impessoalidade = <strong>finalidade pública</strong> + <strong>sem promoção pessoal</strong> + atos imputados ao <strong>órgão</strong>. Nepotismo: proibido até o <strong>3º grau</strong> (SV 13).'))

add(H(4,'<span class="hl">Moralidade</span>','Não basta ser legal: tem de ser honesto.', "A17") +
 traduz(p('A moralidade administrativa exige que o agente atue com <strong>ética, probidade, decoro e boa-fé</strong> (Lei nº 9.784/1999, art. 2º, parágrafo único, IV). Um ato pode até estar formalmente de acordo com a lei e, mesmo assim, ser imoral, quando usa a lei para fins desonestos. A moralidade é <strong>jurídica</strong>: sua violação gera a <strong>invalidade</strong> do ato, e não só reprovação ética.'),"profa") +
 table(["Instrumento de proteção","O que faz"],[
  ["Ação popular (CF, art. 5º, LXXIII)","Qualquer <b>cidadão</b> pode pedir a anulação de ato lesivo à <b>moralidade administrativa</b>, entre outros bens"],
  ["Improbidade administrativa (CF, art. 37, § 4º; Lei nº 8.429/1992)","Sanções como suspensão dos direitos políticos, perda da função, indisponibilidade de bens e ressarcimento ao erário"],
  ["Nepotismo (SV 13)","Proibido também com base na moralidade e na impessoalidade"]],["36%",None]) +
 ex(p('Um prefeito, no último mês do mandato, concede por decreto um aumento a um grupo de servidores aliados, em ato formalmente amparado numa lei genérica, mas com o objetivo de beneficiar apoiadores políticos. Mesmo que o ato pareça legal, ele pode ser anulado por ofender a <b>moralidade</b> e a <b>impessoalidade</b>.')) +
 memo('Moralidade = <strong>ética + probidade + boa-fé</strong>. É princípio <strong>jurídico</strong>: ato imoral é <strong>inválido</strong>. Defesa pelo cidadão: <strong>ação popular</strong>.'))

add(H(4,'<span class="hl">Publicidade</span>','Transparência é a regra; o sigilo, a exceção.', "A18") +
 table(["Ponto","Regra"],[
  ["Dupla função","Dar <b>eficácia</b> aos atos (muitos só produzem efeitos após publicados) e permitir o <b>controle</b> pela sociedade"],
  ["Divulgação oficial (Lei nº 9.784/1999, art. 2º, parágrafo único, V)","Divulgação oficial dos atos administrativos, ressalvadas as hipóteses de sigilo previstas na Constituição"],
  ["Exceções","Sigilo imprescindível à segurança da sociedade e do Estado (CF, art. 5º, XXXIII) e proteção da intimidade"],
  ["Lei de Acesso à Informação (Lei nº 12.527/2011)","Qualquer pessoa pode pedir informações sem precisar justificar o motivo; a transparência ativa obriga a divulgar dados na internet"],
  ["Limite (CF, art. 37, § 1º)","Publicidade não pode virar <b>promoção pessoal</b> da autoridade"]],["32%",None]) +
 ex(p('Um município divulga no seu portal os salários dos servidores, com nome e cargo. O STF considerou legítima a divulgação da remuneração de servidores, em nome da <b>transparência</b>. Já a divulgação de dados médicos de um servidor ofenderia a <b>intimidade</b> e não estaria coberta pela publicidade.')) +
 memo('Publicidade: <strong>regra</strong> é a transparência; <strong>exceção</strong> é o sigilo previsto na Constituição. Publicar não é fazer <strong>propaganda pessoal</strong>.'))

add(H(4,'<span class="hl">Eficiência</span>','O princípio da reforma administrativa de 1998.', "A19") +
 traduz(p('A eficiência foi incluída no art. 37 pela <strong>EC nº 19/1998</strong>, a "reforma administrativa", que buscou um modelo de Administração <strong>gerencial</strong>, voltado a <strong>resultados</strong>. Exige que o serviço seja prestado com <strong>qualidade, rapidez, economia e rendimento</strong>. A eficiência <strong>não</strong> autoriza descumprir a lei: ela soma-se à legalidade, não a substitui.')) +
 table(["Onde a eficiência aparece","Como"],[
  ["Servidores (CF, art. 41)","Estabilidade após 3 anos; avaliação especial de desempenho; perda do cargo por insuficiência de desempenho, mediante avaliação periódica, na forma de lei complementar"],
  ["Contrato de desempenho (CF, art. 37, § 8º)","Ampliação da autonomia de órgãos e entidades em troca de metas de desempenho"],
  ["Agências executivas","Qualificação ligada a plano de metas e contrato de gestão"],
  ["Lei nº 9.784/1999","Eficiência entre os princípios do processo administrativo"]],["30%",None]) +
 memo('Eficiência: <strong>EC nº 19/1998</strong>, Administração <strong>gerencial</strong>, foco em <strong>resultados</strong>. Não justifica agir <strong>contra a lei</strong>.'))

def balanca():
    N,G,R=C['navy'],C['blue'],C['red']
    s = f'<figure><svg viewBox="0 0 640 230" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    s += f'<rect x="305" y="40" width="30" height="160" rx="6" fill="{N}"/><rect x="240" y="196" width="160" height="22" rx="8" fill="{N}"/><circle cx="320" cy="36" r="14" fill="{C["gold"]}"/>'
    s += f'<line x1="110" y1="60" x2="530" y2="40" stroke="{N}" stroke-width="7" stroke-linecap="round"/>'
    s += f'<path d="M110 60 L60 140 M110 60 L160 140" stroke="{N}" stroke-width="2"/><path d="M530 40 L480 120 M530 40 L580 120" stroke="{N}" stroke-width="2"/>'
    s += f'<rect x="20" y="140" width="180" height="58" rx="12" fill="{C["sky"]}" stroke="{G}" stroke-width="2.4"/><text x="110" y="164" text-anchor="middle" font-size="12" font-weight="900" fill="{G}">INTERESSE PÚBLICO</text><text x="110" y="182" text-anchor="middle" font-size="10" fill="{C["ink"]}">prerrogativas do Estado</text>'
    s += f'<rect x="440" y="120" width="180" height="58" rx="12" fill="{C["redsoft"]}" stroke="{R}" stroke-width="2.4"/><text x="530" y="144" text-anchor="middle" font-size="12" font-weight="900" fill="{R}">DIREITOS</text><text x="530" y="162" text-anchor="middle" font-size="10" fill="{C["ink"]}">fundamentais do indivíduo</text>'
    s += f'<text x="320" y="16" text-anchor="middle" font-size="11" font-weight="900" fill="{N}">LIMITES: lei · direitos fundamentais · proporcionalidade · devido processo</text>'
    return s + '</svg><figcaption>A supremacia do interesse público pesa, mas não esmaga os direitos fundamentais: a balança é controlada pela lei e pela proporcionalidade.</figcaption></figure>'

add(H(4,'Supremacia do interesse público e <span class="hl">seus limites</span>','Prerrogativas para o Estado, mas dentro da lei.', "A20") +
 oque(p('Princípio <strong>implícito</strong> (construído pela doutrina) segundo o qual, em caso de conflito, o <strong>interesse público</strong> prevalece sobre o interesse particular. Ele justifica as <strong>prerrogativas</strong> da Administração, que a colocam em posição de superioridade nas relações com os particulares (verticalidade).')) +
 table(["Prerrogativa (exemplos)","Como aparece"],[
  ["Desapropriação","Tomar um imóvel para uma obra pública, mediante indenização"],
  ["Poder de polícia","Interditar estabelecimento que descumpre regras sanitárias"],
  ["Cláusulas exorbitantes","Alterar ou rescindir unilateralmente contratos administrativos, nos limites da lei"],
  ["Atributos do ato","Presunção de legitimidade, imperatividade e autoexecutoriedade"]],["30%",None]) +
 balanca())

atencao(
 table(["Limite","Por quê"],[
  ["Legalidade","A prerrogativa só existe se a <b>lei</b> a prevê"],
  ["Direitos fundamentais","A supremacia não autoriza violar a dignidade, o contraditório, a ampla defesa ou o direito de propriedade sem indenização"],
  ["Proporcionalidade","A medida deve ser adequada, necessária e proporcional ao fim"],
  ["Interesse público primário x secundário","O <b>primário</b> é o interesse da coletividade; o <b>secundário</b>, o interesse patrimonial do próprio Estado. Só o primário justifica a supremacia (distinção doutrinária de Renato Alessi)"],
  ["Crítica doutrinária","Parte da doutrina critica a ideia de uma supremacia abstrata e defende a <b>ponderação</b> caso a caso entre os interesses envolvidos"]],["30%",None]) +
 ex(p('A Prefeitura precisa alargar uma avenida e desapropria parte de um terreno: a supremacia do interesse público justifica a medida, mas exige <b>lei</b>, <b>processo</b> e <b>indenização</b>. Se o Município, para economizar (interesse <b>secundário</b>), simplesmente deixasse de pagar a indenização, não haveria supremacia que o justificasse.')) +
 pega('<ul><li>A supremacia é princípio <b>implícito</b>: não está escrita no art. 37.</li><li>A supremacia <b>não é absoluta</b>: encontra limites na lei e nos direitos fundamentais.</li><li>Interesse do Estado de <b>arrecadar ou economizar</b> é interesse público <b>secundário</b>, que não se sobrepõe aos direitos do cidadão.</li></ul>'),
 ["princípio implícito","prerrogativas","verticalidade","interesse primário","interesse secundário","proporcionalidade"])

add(H(4,'Indisponibilidade do <span class="hl">interesse público</span>','O administrador cuida do que não é dele.', "A21") +
 traduz(p('O administrador é um <strong>gestor de bens alheios</strong>: o interesse público pertence à <strong>coletividade</strong>, e não ao agente. Por isso ele <strong>não pode dispor</strong> desses interesses como quiser: não pode renunciar a direitos, perdoar dívidas ou abrir mão de poderes sem <strong>autorização em lei</strong>. Se a supremacia dá <strong>prerrogativas</strong>, a indisponibilidade impõe <strong>sujeições</strong> (limites).'),"profa") +
 table(["Sujeição (exemplos)","Fundamento"],[
  ["Concurso público para contratar pessoal","CF, art. 37, II"],
  ["Licitação para contratar obras, serviços e compras","CF, art. 37, XXI"],
  ["Vedação à renúncia de poderes ou competências, salvo autorização em lei","Lei nº 9.784/1999, art. 2º, parágrafo único, II"],
  ["Bens públicos inalienáveis enquanto afetados","Regime dos bens públicos"],
  ["Prestação de contas e controle","Tribunais de contas, controle interno e Judiciário"]],["50%",None]) +
 table(["","SUPREMACIA","INDISPONIBILIDADE"],[["Gera","<b>Prerrogativas</b> (poderes)","<b>Sujeições</b> (limites, deveres)"],["Ideia","O interesse público prevalece","O interesse público não pertence ao administrador"],["Juntas","Formam o <b>regime jurídico-administrativo</b>","Formam o <b>regime jurídico-administrativo</b>"]],["16%",None,None]) +
 memo('Supremacia → <strong>prerrogativas</strong>. Indisponibilidade → <strong>sujeições</strong>. Juntas: o <strong>regime jurídico-administrativo</strong>.'))

add(H(4,'Outros princípios <span class="hl">cobrados</span>','Implícitos e da Lei nº 9.784/1999.', "A22") +
 table(["Princípio","Ideia central"],[
  ["Razoabilidade e proporcionalidade","A medida deve ser adequada, necessária e proporcional; vedadas obrigações, restrições e sanções além do necessário (Lei nº 9.784/1999)"],
  ["Motivação","Indicar os <b>fundamentos de fato e de direito</b> das decisões"],
  ["Autotutela","A Administração pode <b>anular</b> seus atos ilegais e <b>revogar</b> os inconvenientes ou inoportunos, respeitados os direitos adquiridos (Súmula 473 do STF; Lei nº 9.784/1999, art. 53)"],
  ["Segurança jurídica","Proteção da confiança; vedada a aplicação retroativa de nova interpretação; prazo de <b>5 anos</b> para anular atos favoráveis ao destinatário, salvo má-fé (Lei nº 9.784/1999, art. 54)"],
  ["Continuidade do serviço público","O serviço não pode parar sem justificativa, pois atende a necessidades da coletividade"],
  ["Tutela (ou controle)","O ente político controla as entidades da Administração indireta quanto ao cumprimento de suas finalidades"],
  ["Especialidade","Entidades da indireta só atuam na finalidade definida em lei"],
  ["Hierarquia","Organização em escalões, com subordinação entre órgãos"]],["28%",None]) +
 ex(p('A Prefeitura percebe que concedeu, por engano, um alvará contrário à lei de zoneamento e o <b>anula</b> (autotutela, por ilegalidade). Em outro caso, decide <b>revogar</b> a autorização de uso de uma praça para um evento, por conveniência, porque a praça será reformada. Anular = ilegalidade; revogar = conveniência e oportunidade.')) +
 memo('<strong>Anular</strong>: ato <strong>ilegal</strong> (Administração ou Judiciário). <strong>Revogar</strong>: ato legal, mas <strong>inconveniente ou inoportuno</strong> (só a Administração). Prazo para anular ato favorável: <strong>5 anos</strong>, salvo má-fé.'))

treino(4, [
 ("O princípio da eficiência foi incluído expressamente no art. 37 da Constituição pela EC nº 19/1998.","C","Reforma administrativa."),
 ("Pelo princípio da legalidade, a Administração pode fazer tudo o que a lei não proíbe.","E","Essa é a regra do particular; a Administração só faz o que a lei permite."),
 ("A publicidade de obras e programas públicos pode conter o nome do governante, desde que de forma discreta.","E","CF, art. 37, § 1º, veda nomes, símbolos ou imagens que caracterizem promoção pessoal."),
 ("A supremacia do interesse público é absoluta e autoriza a Administração a desconsiderar direitos fundamentais.","E","Encontra limites na lei, nos direitos fundamentais e na proporcionalidade."),
 ("A indisponibilidade do interesse público impede o administrador de renunciar a poderes ou competências sem autorização legal.","C","Lei nº 9.784/1999, art. 2º, parágrafo único, II."),
 ("A Administração pode revogar seus atos por motivo de conveniência ou oportunidade, respeitados os direitos adquiridos.","C","Súmula 473 do STF; Lei nº 9.784/1999, art. 53.")])

# ================================================================ REVISÃO
mapa = f'''<figure><svg viewBox="0 0 640 470" width="580" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<g stroke="#b3c2d4" stroke-width="2.5" fill="none"><path d="M320 235 L150 70"/><path d="M320 235 L490 70"/><path d="M320 235 L120 235"/><path d="M320 235 L520 235"/><path d="M320 235 L150 400"/><path d="M320 235 L490 400"/></g>
<circle cx="320" cy="235" r="74" fill="{C['navy']}"/><text x="320" y="225" text-anchor="middle" fill="#5fd39e" font-weight="900" font-size="13">DIREITO</text>
<text x="320" y="245" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">ADMINIS-</text><text x="320" y="263" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">TRATIVO</text>
''' + "".join(
 f'<rect x="{x-100}" y="{y-40}" width="200" height="80" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x}" y="{y-16}" text-anchor="middle" font-weight="900" font-size="12.5" fill="{fg}">{t}</text>'
 + "".join(f'<text x="{x}" y="{y+4+i*15}" text-anchor="middle" font-size="10.8" fill="{C["ink"]}">{l}</text>' for i,l in enumerate(ls))
 for x,y,t,ls,fg,bg in [
  (150,62,"NOÇÕES",["direito público, não codificado","objeto: função administrativa","subjetivo (quem) x objetivo"],C['navy'],NV),
  (490,62,"ORGANIZAÇÃO",["desconcentração: órgãos","descentralização: entidades","sem hierarquia: tutela"],C['golddeep'],C['goldsoft']),
  (112,235,"DIRETA",["União, Estados, DF,","Municípios e seus órgãos","órgão: sem personalidade"],C['golddeep'],C['goldsoft']),
  (528,235,"INDIRETA",["autarquia: criada, público","EP: 100% público, qualquer forma","SEM: maioria votante, S.A."],C['blue'],C['sky']),
  (150,408,"LIMPE",["legalidade · impessoalidade","moralidade · publicidade","eficiência (EC 19/1998)"],C['blue'],C['sky']),
  (490,408,"SUPRAPRINCÍPIOS",["supremacia: prerrogativas","indisponibilidade: sujeições","limites: lei e direitos"],C['navy'],NV)]) + '</svg><figcaption>Mapa conceitual do Caderno 09.</figcaption></figure>'
add('<div class="marker">§§R1§§</div><div class="unit"><span class="u">REVISÃO</span><span class="t">Véspera da prova</span></div><h1 class="big">Mapa <span class="hl">conceitual</span></h1><p class="lead">Os fundamentos em seis blocos. Explique cada caixa em voz alta.</p>' + mapa)

add('<div class="unit"><span class="u">REVISÃO</span><span class="t">Erros mais comuns</span></div><h1 class="big">Os erros <span class="hl">mais comuns</span> nas provas</h1><p class="lead">Afirmações erradas que costumam aparecer em questões. Ao lado, o que está certo.</p>' +
 table(["Afirmação errada","O certo é"],[
  ["“Desconcentração cria nova pessoa jurídica.”","Cria <b>órgãos</b>, dentro da mesma pessoa. Quem envolve outra pessoa é a descentralização."],
  ["“Há hierarquia entre o Município e sua autarquia.”","Há <b>controle finalístico</b> (tutela), sem hierarquia."],
  ["“Órgão público tem personalidade jurídica.”","Não tem; quem tem é a entidade."],
  ["“Empresa pública é criada por lei.”","A lei <b>autoriza</b> a criação; só a autarquia é criada diretamente por lei."],
  ["“Sociedade de economia mista pode ser limitada (Ltda.).”","É sempre <b>sociedade anônima</b>."],
  ["“Empresa pública é pessoa de direito público.”","É pessoa jurídica de <b>direito privado</b>."],
  ["“Agência executiva é nova entidade.”","É <b>qualificação</b> de autarquia ou fundação com contrato de gestão."],
  ["“Estatais podem contratar sem concurso, porque são privadas.”","Empregados são celetistas, mas há <b>concurso público</b> (CF, art. 37, II)."]],["46%",None]))

add(pratica_title("Erros mais comuns (continuação)") +
 table(["Afirmação errada","O certo é"],[
  ["“Os princípios do art. 37 valem só para o Executivo.”","Valem para a Administração direta e indireta de <b>todos os Poderes</b> e entes."],
  ["“Legalidade administrativa: pode tudo o que a lei não proíbe.”","Só pode o que a lei <b>permite</b>."],
  ["“Eficiência está no texto original da CF/88.”","Foi incluída pela <b>EC nº 19/1998</b>."],
  ["“A supremacia do interesse público é expressa no art. 37.”","É princípio <b>implícito</b>."],
  ["“A supremacia autoriza qualquer medida contra o particular.”","Tem limites: lei, direitos fundamentais e proporcionalidade."],
  ["“Revogação ocorre por ilegalidade.”","Por ilegalidade, é <b>anulação</b>; a revogação é por conveniência e oportunidade."],
  ["“Moralidade administrativa é só uma questão ética, sem efeito jurídico.”","Ato imoral é <b>inválido</b> e pode ser anulado (inclusive por ação popular)."],
  ["“A placa da obra pode trazer a foto do prefeito.”","Vedada a promoção pessoal (CF, art. 37, § 1º)."]],["46%",None]))

FC = [("NOÇÕES","Direito Administrativo é ramo do direito público ou privado?","Público, e não é codificado no Brasil."),
 ("NOÇÕES","Qual é o objeto do Direito Administrativo?","A função administrativa e quem a exerce (órgãos, agentes, entidades)."),
 ("NOÇÕES","Sentido subjetivo x objetivo?","Subjetivo: quem administra. Objetivo: a atividade administrativa."),
 ("NOÇÕES","Quatro atividades da Administração (sentido objetivo)?","Serviço público, polícia administrativa, fomento e intervenção."),
 ("ORGANIZAÇÃO","Desconcentração?","Distribuição de tarefas entre órgãos da mesma pessoa jurídica, com hierarquia."),
 ("ORGANIZAÇÃO","Descentralização?","Transferência a outra pessoa (entidade ou particular), sem hierarquia, com controle."),
 ("ORGANIZAÇÃO","Outorga x delegação?","Outorga: por lei, titularidade e execução. Delegação: contrato ou ato, só a execução."),
 ("ORGANIZAÇÃO","Órgão tem personalidade jurídica?","Não. É centro de competência; a vontade é imputada à pessoa jurídica."),
 ("ORGANIZAÇÃO","Quais entidades compõem a Administração indireta (DL 200)?","Autarquias, empresas públicas, sociedades de economia mista e fundações públicas."),
 ("ORGANIZAÇÃO","Criação das entidades (CF, art. 37, XIX)?","Autarquia: criada por lei específica. Demais: lei específica autoriza."),
 ("INDIRETA","Natureza da autarquia?","Pessoa jurídica de direito público, para atividades típicas de Estado."),
 ("INDIRETA","Agência reguladora x executiva?","Reguladora: autarquia especial que regula setor. Executiva: título por contrato de gestão."),
 ("INDIRETA","Fundação pública pode ser de direito público?","Sim (fundação autárquica), além da de direito privado do DL 200."),
 ("INDIRETA","Capital da empresa pública?","Integralmente público."),
 ("INDIRETA","Capital e forma da sociedade de economia mista?","Maioria das ações com voto pública; sempre sociedade anônima."),
 ("INDIRETA","Foro da SEM federal?","Justiça Estadual (Súmula 556 do STF); EP federal: Justiça Federal."),
 ("PRINCÍPIOS","Quais são os princípios do art. 37, caput?","Legalidade, impessoalidade, moralidade, publicidade e eficiência (LIMPE)."),
 ("PRINCÍPIOS","Quando entrou a eficiência?","EC nº 19/1998."),
 ("PRINCÍPIOS","O que proíbe a Súmula Vinculante 13?","Nepotismo, até o terceiro grau, inclusive o cruzado."),
 ("PRINCÍPIOS","Instrumento do cidadão contra ato imoral?","Ação popular (CF, art. 5º, LXXIII)."),
 ("PRINCÍPIOS","Supremacia gera o quê? E a indisponibilidade?","Supremacia: prerrogativas. Indisponibilidade: sujeições."),
 ("PRINCÍPIOS","Interesse público primário x secundário?","Primário: da coletividade. Secundário: patrimonial do Estado."),
 ("PRINCÍPIOS","Anular x revogar?","Anular: ilegalidade. Revogar: conveniência e oportunidade."),
 ("PRINCÍPIOS","Prazo para anular ato favorável ao destinatário?","5 anos, salvo comprovada má-fé (Lei nº 9.784/1999, art. 54).")]
def fcpage(items, first):
    cs = "".join(f'<div class="c"><div class="f"><small>{a}</small>{q}</div><div class="b">{r}</div></div>' for a,q,r in items)
    h = ('<div class="marker">§§R2§§</div><div class="unit"><span class="u">REVISÃO ATIVA</span></div><h1 class="big">Flash<span class="hl">cards</span></h1><p class="lead">Cubra a resposta, tente lembrar e confira. Revise em 1, 3, 7, 15 e 30 dias.</p>' if first else '')
    return h + f'<div class="fc">{cs}</div>'
add(fcpage(FC[:12], True)); add(fcpage(FC[12:], False))

Q = [
 ("Conceito","Sobre o Direito Administrativo brasileiro, é correto afirmar que:",
  ["é ramo do direito privado, voltado às relações entre particulares.","está integralmente reunido em um código próprio.","é ramo do direito público que rege a função administrativa, os órgãos, agentes e entidades que a exercem.","tem como fonte única a jurisprudência.","aplica-se apenas ao Poder Executivo federal."],"C",
  "É ramo do direito público, não codificado, com fontes na lei (principal), na jurisprudência, na doutrina e nos costumes, aplicável à função administrativa exercida em todos os Poderes e entes.","Público, não codificado, função administrativa."),
 ("Objeto","Quando um Tribunal de Justiça realiza licitação para comprar equipamentos, exerce:",
  ["função jurisdicional típica.","função legislativa atípica.","função administrativa atípica.","função política.","atividade privada."],"C",
  "O Judiciário exerce tipicamente a função jurisdicional e, atipicamente, a administrativa, como em licitações e na gestão de pessoal.","Judiciário licitando = função administrativa atípica."),
 ("Administração Pública","A Administração Pública em sentido subjetivo corresponde:",
  ["às atividades de serviço público e de polícia administrativa.","ao conjunto de órgãos, agentes e entidades que exercem a função administrativa.","ao exercício da função legislativa.","às decisões políticas de governo.","apenas às empresas estatais."],"B",
  "Sentido subjetivo, orgânico ou formal: quem administra. O sentido objetivo é a atividade (serviço público, polícia, fomento, intervenção).","Subjetivo = quem."),
 ("Organização","O Município que cria, dentro da Prefeitura, a Secretaria de Segurança Urbana pratica:",
  ["descentralização por outorga.","descentralização por delegação.","desconcentração.","privatização.","concessão de serviço público."],"C",
  "Distribuir competências entre órgãos da mesma pessoa jurídica é desconcentração, com hierarquia entre os órgãos.","Órgão novo, mesma pessoa = desconcentração."),
 ("Organização","Na descentralização por delegação (ou por colaboração):",
  ["transfere-se por lei a titularidade do serviço a uma autarquia.","transfere-se apenas a execução do serviço, por contrato ou ato, normalmente a particular.","criam-se órgãos sem personalidade jurídica.","há hierarquia entre o Estado e o delegatário.","extingue-se a titularidade estatal do serviço."],"B",
  "Na delegação, o Estado mantém a titularidade e transfere só a execução, por contrato (concessão) ou ato (permissão, autorização). A outorga é por lei e transfere titularidade e execução.","Delegação: só a execução."),
 ("Órgãos","Segundo a Lei nº 9.784/1999 e a doutrina, os órgãos públicos:",
  ["têm personalidade jurídica própria.","existem somente na Administração direta.","são unidades de atuação sem personalidade jurídica, presentes na Administração direta e na indireta.","respondem civilmente em nome próprio pelos danos causados.","são sempre colegiados."],"C",
  "Art. 1º, § 2º, I, da Lei nº 9.784/1999. Pela teoria do órgão, a atuação é imputada à pessoa jurídica, que responde pelos danos.","Órgão: sem personalidade, na direta e na indireta."),
 ("Indireta","De acordo com o art. 37, XIX, da Constituição:",
  ["a empresa pública é criada diretamente por lei específica.","a autarquia tem sua criação apenas autorizada por lei.","somente por lei específica pode ser criada autarquia e autorizada a instituição de empresa pública, sociedade de economia mista e fundação.","a lei ordinária define as áreas de atuação das empresas públicas.","a sociedade de economia mista dispensa autorização legal."],"C",
  "Texto do art. 37, XIX. A lei complementar define as áreas de atuação das fundações.","Autarquia: criada. Demais: autorizadas."),
 ("Indireta","Entre a autarquia e o ente político que a criou existe:",
  ["hierarquia, com subordinação total.","controle finalístico (tutela ou supervisão), sem hierarquia.","nenhuma forma de controle.","subordinação apenas no aspecto financeiro.","relação de concessão de serviço público."],"B",
  "As entidades da indireta são vinculadas ao ente que as criou, que exerce controle finalístico (DL nº 200/1967, arts. 19 e 26), sem hierarquia.","Vinculação, não subordinação."),
 ("Autarquias","São características das autarquias, EXCETO:",
  ["personalidade jurídica de direito público.","criação por lei específica.","execução de atividades típicas da Administração.","bens públicos, impenhoráveis.","finalidade lucrativa na exploração de atividade econômica."],"E",
  "Autarquias executam atividades típicas de Estado, sem finalidade lucrativa. A exploração de atividade econômica cabe às empresas estatais.","Autarquia não explora atividade econômica."),
 ("Autarquias especiais","A qualificação de agência executiva:",
  ["cria uma nova pessoa jurídica de direito público.","é dada a autarquia ou fundação que celebra contrato de gestão para ampliar sua autonomia, mediante metas.","é exclusiva das sociedades de economia mista.","transforma a entidade em agência reguladora.","dispensa a entidade de controle."],"B",
  "Agência executiva é um título, não uma nova entidade; liga-se ao contrato de gestão e às metas de desempenho (CF, art. 37, § 8º).","Agência executiva = título."),
 ("Fundações","Sobre as fundações públicas, é correto afirmar:",
  ["visam ao lucro.","o DL nº 200/1967 as define como de direito privado, mas a doutrina e o STF admitem também fundações públicas de direito público.","dispensam qualquer autorização legislativa.","têm suas áreas de atuação definidas por decreto.","são sempre sociedades anônimas."],"B",
  "O DL nº 200/1967 (art. 5º, IV) fala em direito privado, sem fins lucrativos; a fundação de direito público (autárquica) é reconhecida pela doutrina e pelo STF. A lei complementar define as áreas de atuação.","Fundação: privada ou pública; sem lucro."),
 ("Estatais","A empresa pública é:",
  ["pessoa jurídica de direito público, com capital misto.","pessoa jurídica de direito privado, com criação autorizada por lei e capital integralmente público.","pessoa jurídica de direito privado, obrigatoriamente sociedade anônima com acionistas privados.","órgão da Administração direta.","entidade sem personalidade jurídica."],"B",
  "Lei nº 13.303/2016, art. 3º. Pode adotar qualquer forma societária admitida em direito.","EP: privado, 100% público, qualquer forma."),
 ("Estatais","A sociedade de economia mista:",
  ["pode adotar qualquer forma societária.","é sempre sociedade anônima, com a maioria das ações com direito a voto pertencentes ao poder público.","tem capital integralmente público.","é pessoa jurídica de direito público.","é criada diretamente pela lei, sem registro."],"B",
  "Lei nº 13.303/2016, art. 4º. Criação autorizada por lei, direito privado.","SEM: S.A. + maioria votante pública."),
 ("Estatais","Ação de indenização movida contra sociedade de economia mista federal deve tramitar, em regra, na:",
  ["Justiça Federal.","Justiça Estadual.","Justiça do Trabalho, sempre.","Justiça Eleitoral.","Justiça Militar."],"B",
  "Súmula 556 do STF: é competente a Justiça comum (estadual) para julgar as causas em que é parte sociedade de economia mista. Empresa pública federal: Justiça Federal (CF, art. 109, I).","SEM: estadual; EP federal: federal."),
 ("Estatais","As empresas públicas e sociedades de economia mista que exploram atividade econômica:",
  ["gozam de todos os privilégios fiscais da Administração direta.","não podem gozar de privilégios fiscais não extensivos às empresas do setor privado.","contratam empregados sem concurso público.","estão sujeitas à falência como qualquer empresa.","são pessoas jurídicas de direito público."],"B",
  "CF, art. 173, § 2º. Os empregados são admitidos por concurso, e a Lei nº 11.101/2005 exclui as estatais do regime falimentar.","Sem privilégios fiscais."),
 ("LIMPE","Os princípios previstos no art. 37, caput, da Constituição aplicam-se:",
  ["apenas ao Poder Executivo federal.","somente à Administração direta.","à Administração direta e indireta de qualquer dos Poderes da União, dos Estados, do DF e dos Municípios.","apenas às autarquias.","só aos servidores efetivos."],"C",
  "Texto do caput do art. 37.","LIMPE: todos os Poderes, direta e indireta."),
 ("Legalidade","Pelo princípio da legalidade, a Administração Pública:",
  ["pode fazer tudo o que a lei não proíbe.","só pode fazer o que a lei permite ou determina.","pode agir contra a lei para alcançar eficiência.","está dispensada de observar princípios não escritos.","atua conforme a vontade do administrador."],"B",
  "Para o particular, vale a autonomia da vontade; para a Administração, a legalidade estrita, atuando conforme a lei e o Direito.","Administração: só o que a lei permite."),
 ("Impessoalidade","O prefeito que instala placas em obras públicas com sua foto e seu nome ofende principalmente o princípio da:",
  ["eficiência.","impessoalidade.","continuidade.","especialidade.","hierarquia."],"B",
  "CF, art. 37, § 1º: vedados nomes, símbolos ou imagens que caracterizem promoção pessoal, regra ligada à impessoalidade (e à moralidade).","Promoção pessoal fere impessoalidade."),
 ("Impessoalidade","Segundo a Súmula Vinculante 13, é vedada a nomeação para cargo em comissão de parente da autoridade nomeante:",
  ["até o segundo grau, apenas em linha reta.","até o terceiro grau, em linha reta, colateral ou por afinidade, inclusive mediante designações recíprocas.","até o quarto grau, apenas por afinidade.","de qualquer grau, inclusive amigos.","apenas no Poder Judiciário."],"B",
  "A SV 13 alcança cônjuge, companheiro ou parente até o terceiro grau e o nepotismo cruzado, nos três Poderes.","Nepotismo: até o 3º grau, inclusive cruzado."),
 ("Moralidade","Sobre o princípio da moralidade administrativa, assinale a correta:",
  ["É mera recomendação ética, sem efeitos jurídicos.","Ato formalmente legal pode ser invalidado por ofensa à moralidade.","Não pode ser defendido por ação popular.","Aplica-se apenas aos agentes políticos.","Foi revogado pela EC nº 19/1998."],"B",
  "A moralidade é princípio jurídico: o ato imoral é inválido, e o cidadão pode propor ação popular contra ato lesivo à moralidade (CF, art. 5º, LXXIII).","Ato imoral = inválido."),
 ("Eficiência","O princípio da eficiência:",
  ["consta do texto original da Constituição de 1988.","foi incluído no art. 37 pela EC nº 19/1998 e se relaciona ao modelo de Administração gerencial.","autoriza o administrador a descumprir a lei para obter resultados.","aplica-se só às empresas estatais.","substitui o princípio da legalidade."],"B",
  "A eficiência veio com a reforma administrativa de 1998 e soma-se à legalidade, sem substituí-la.","Eficiência: EC 19/1998."),
 ("Supremacia","Sobre a supremacia do interesse público, é correto afirmar:",
  ["está expressa no caput do art. 37.","é absoluta e afasta os direitos fundamentais.","fundamenta as prerrogativas da Administração, mas encontra limites na lei, nos direitos fundamentais e na proporcionalidade.","justifica a prevalência de qualquer interesse patrimonial do Estado.","não tem relação com o poder de polícia."],"C",
  "É princípio implícito. Só o interesse público primário (da coletividade) justifica prerrogativas; o secundário (patrimonial do Estado) não se sobrepõe aos direitos.","Supremacia: prerrogativas com limites."),
 ("Indisponibilidade","A exigência de concurso público e de licitação decorre mais diretamente do princípio da:",
  ["supremacia do interesse público.","indisponibilidade do interesse público.","autoexecutoriedade.","especialidade.","hierarquia."],"B",
  "A indisponibilidade impõe sujeições ao administrador, que gere interesses da coletividade: concurso, licitação, vedação de renúncia de poderes sem lei.","Indisponibilidade → sujeições."),
 ("Autotutela","Segundo a Súmula 473 do STF, a Administração pode:",
  ["revogar atos ilegais, em qualquer caso.","anular seus atos ilegais e revogar os inconvenientes ou inoportunos, respeitados os direitos adquiridos e ressalvada a apreciação judicial.","anular atos apenas mediante decisão judicial.","revogar atos já declarados nulos pelo Judiciário.","manter atos ilegais por conveniência."],"B",
  "Anulação: ilegalidade. Revogação: conveniência e oportunidade, respeitados os direitos adquiridos. A Lei nº 9.784/1999, art. 53, repete a regra.","Anula ilegal; revoga inconveniente.")]

ALVO = "CDBCEABDEBCBDAEBCADBECBA"
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
<li>Constituição Federal: art. 37 (caput, incisos XIX e XX, §§ 1º, 6º e 8º), art. 173 (caput e §§ 1º e 2º) e art. 175.</li>
<li>Decreto-Lei nº 200/1967: arts. 4º, 5º, 6º, 10, 19 e 26 (com as alterações do Decreto-Lei nº 900/1969 e da Lei nº 7.596/1987).</li>
<li>Lei nº 13.303/2016 (Estatuto das Empresas Estatais): arts. 1º a 4º e 27, com a alteração da Lei nº 15.177/2025.</li>
<li>Lei nº 9.784/1999 (Processo Administrativo Federal): arts. 1º, 2º, 53 e 54.</li>
<li>Citadas sem conferência nesta edição: CF, arts. 5º, 39, 41, 109 e 150; Leis nº 8.429/1992, 11.101/2005, 11.107/2005, 12.527/2011 e 13.848/2019; CPC.</li>
</ul>
<h3>Jurisprudência citada (identificada em pesquisa)</h3><ul><li>STF: Súmula Vinculante 13 (nepotismo) e Tema 1.000; Súmulas 473 e 556; ADI 2.135 (regime jurídico único, 2024); ADI 3.026 (OAB).</li></ul>''' + lembre(p(f'<strong>Material pesquisado e atualizado em: {DATA}.</strong> A base legal foi conferida nos textos do portal do Planalto, que exibem a redação vigente com as notas de alteração. <strong>Limitações:</strong> os textos do Planalto não informam a data da última atualização e não substituem o Diário Oficial; algumas páginas mostram versões antigas e novas do mesmo dispositivo, e a versão atual foi identificada pelas notas. Conceitos como sentidos da Administração, classificação dos órgãos, supraprincípios e interesse público primário e secundário são <strong>construções doutrinárias</strong>, apresentadas na forma mais aceita. A jurisprudência foi identificada em publicações e notícias e não foi reconferida nos portais oficiais dos tribunais; o alcance da ADI 2.135 e do Tema 1.000 ainda é debatido. Confira o edital do seu concurso.'), "Verificação e limitações"))
add('''<div class="ending"><h2>Fim do Caderno 09</h2><p style="text-align:center">Sugestão de continuação em Direito Administrativo: <strong>atos administrativos, poderes administrativos e agentes públicos</strong>.</p>
<p class="note" style="text-align:center">Mapa da Aprovação · Caderno Simplificado · Direito Administrativo · Caderno 09 · 1ª edição · novembro de 2026<br>Material de estudo independente. Não substitui a leitura da lei e do edital do seu concurso.</p></div>''')

doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Mapa da Aprovação — Caderno 09 — Direito Administrativo: Fundamentos</title>
<link rel="stylesheet" href="estilo.css"></head><body>{symbols()}{"".join(P)}</body></html>'''
open(os.path.join(HERE, "miolo.html"), "w").write(doc)
print("páginas planejadas:", len(P))
