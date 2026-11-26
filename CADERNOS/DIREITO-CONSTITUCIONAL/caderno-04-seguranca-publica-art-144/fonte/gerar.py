"""Gera miolo.html do Caderno 04 de Direito Constitucional (art. 144). Uso: python3 gerar.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from componentes import *

DATA = "25 de novembro de 2026"
P = []
def add(html, first=False): P.append(page(f'<div class="marker">§§P{len(P)+1:03d}§§</div>' + html, first))
U1, U2, U3, U4, U5 = "UNIDADE 1", "UNIDADE 2", "UNIDADE 3", "UNIDADE 4", "UNIDADE 5"
T1, T2, T3, T4, T5 = "Fundamentos", "Órgãos da União", "Órgãos dos Estados e do DF", "Municípios", "Organização e comparações"
def cf(x): return f"{x} · Constituição Federal"
def p(t): return f"<p>{t}</p>"
def colors(*keys):
    m = {"b":(C['blue'],C['sky']),"g":(C['green'],C['greensoft']),"o":(C['golddeep'],C['goldsoft']),"r":(C['red'],C['redsoft']),"n":(C['navy'],'#e3e9f3')}
    return [m[k] for k in keys]
def atencao(pega_html, kws):
    add(pratica_title('Atenção na prova') + pega_html + kw(kws))

# ---------- textos do art. 144 (conferidos no Planalto) ----------
A144_CAPUT = '<p>Art. 144. A segurança pública, dever do Estado, direito e responsabilidade de todos, é exercida para a preservação da ordem pública e da incolumidade das pessoas e do patrimônio, através dos seguintes órgãos:<br>I - polícia federal;<br>II - polícia rodoviária federal;<br>III - polícia ferroviária federal;<br>IV - polícias civis;<br>V - polícias militares e corpos de bombeiros militares;<br>VI - polícias penais federal, estaduais e distrital.</p>'
A144_1 = '<p>§ 1º A polícia federal, instituída por lei como órgão permanente, organizado e mantido pela União e estruturado em carreira, destina-se a:<br>I - apurar infrações penais contra a ordem política e social ou em detrimento de bens, serviços e interesses da União ou de suas entidades autárquicas e empresas públicas, assim como outras infrações cuja prática tenha repercussão interestadual ou internacional e exija repressão uniforme, segundo se dispuser em lei;<br>II - prevenir e reprimir o tráfico ilícito de entorpecentes e drogas afins, o contrabando e o descaminho, sem prejuízo da ação fazendária e de outros órgãos públicos nas respectivas áreas de competência;<br>III - exercer as funções de polícia marítima, aeroportuária e de fronteiras;<br>IV - exercer, com exclusividade, as funções de polícia judiciária da União.</p>'
A144_2 = '<p>§ 2º A polícia rodoviária federal, órgão permanente, organizado e mantido pela União e estruturado em carreira, destina-se, na forma da lei, ao patrulhamento ostensivo das rodovias federais.</p>'
A144_3 = '<p>§ 3º A polícia ferroviária federal, órgão permanente, organizado e mantido pela União e estruturado em carreira, destina-se, na forma da lei, ao patrulhamento ostensivo das ferrovias federais.</p>'
A144_4 = '<p>§ 4º Às polícias civis, dirigidas por delegados de polícia de carreira, incumbem, ressalvada a competência da União, as funções de polícia judiciária e a apuração de infrações penais, exceto as militares.</p>'
A144_5 = '<p>§ 5º Às polícias militares cabem a polícia ostensiva e a preservação da ordem pública; aos corpos de bombeiros militares, além das atribuições definidas em lei, incumbe a execução de atividades de defesa civil.</p>'
A144_5A = '<p>§ 5º-A. Às polícias penais, vinculadas ao órgão administrador do sistema penal da unidade federativa a que pertencem, cabe a segurança dos estabelecimentos penais.</p>'
A144_6 = '<p>§ 6º As polícias militares e os corpos de bombeiros militares, forças auxiliares e reserva do Exército subordinam-se, juntamente com as polícias civis e as polícias penais estaduais e distrital, aos Governadores dos Estados, do Distrito Federal e dos Territórios.</p>'
A144_7 = '<p>§ 7º A lei disciplinará a organização e o funcionamento dos órgãos responsáveis pela segurança pública, de maneira a garantir a eficiência de suas atividades.</p>'
A144_8 = '<p>§ 8º Os Municípios poderão constituir guardas municipais destinadas à proteção de seus bens, serviços e instalações, conforme dispuser a lei.</p>'
A144_9 = '<p>§ 9º A remuneração dos servidores policiais integrantes dos órgãos relacionados neste artigo será fixada na forma do § 4º do art. 39.</p>'
A144_10 = '<p>§ 10. A segurança viária, exercida para a preservação da ordem pública e da incolumidade das pessoas e do seu patrimônio nas vias públicas:<br>I - compreende a educação, engenharia e fiscalização de trânsito, além de outras atividades previstas em lei, que assegurem ao cidadão o direito à mobilidade urbana eficiente; e<br>II - compete, no âmbito dos Estados, do Distrito Federal e dos Municípios, aos respectivos órgãos ou entidades executivos e seus agentes de trânsito, estruturados em Carreira, na forma da lei.</p>'

# ================================================================ APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">O art. 144 explicado com cenários, comparações e as competências de cada órgão.</p>
<p>Este é o <strong>Caderno 04 da coleção de Direito Constitucional</strong>, dedicado à <strong>Segurança Pública (art. 144)</strong>. Para quem vai prestar concurso de <strong>Guarda Municipal</strong>, <strong>Polícia Militar</strong>, <strong>Polícia Civil</strong>, <strong>Polícia Penal</strong>, <strong>PRF</strong> ou <strong>PF</strong>, este é um dos artigos mais importantes da Constituição: ele define <strong>quem é quem</strong> na segurança pública.</p>
<p>O foco aqui é a pergunta que mais aparece em prova: <strong>qual órgão faz o quê?</strong> Por isso o caderno traz muitos <strong>quadros comparativos</strong> e <strong>cenários</strong> do tipo “quem atende esta ocorrência?”. Em geral, cada assunto ocupa <strong>duas páginas</strong>:</p>
{cards([("book","Página 1 · Entenda","Título, texto da lei, <b>Traduzindo o juridiquês</b> e a faixa <b>Memorize</b>.", C['golddeep']),
        ("bulb","Página 2 · Pratique","<b>Entenda na prática</b>, exemplo e <b>Pegadinha de concurso</b>.", C['blue'])],2)}
<h3>Recursos especiais deste caderno</h3>
{table(["Recurso","Onde está"],[
 ["Mapa dos órgãos por ente federativo","Unidade 1"],
 ["Cenário “Uma noite na cidade: quem atende?”","Unidade 5"],
 ["Quadro comparativo completo dos órgãos","Unidade 5"],
 ["Polícia administrativa x polícia judiciária","Unidade 5"],
 ["Quadro de atualização: PEC da Segurança Pública","Unidade 5"],
 ["Treinos Certo ou Errado e 24 questões autorais comentadas","Fim de cada unidade e prática final"]],["56%",None])}
{lembre(f'''<p><strong>Material pesquisado e atualizado em: {DATA}.</strong> O texto do art. 144 foi conferido no texto compilado da Constituição no Planalto. A <strong>PEC da Segurança Pública (PEC 18/2025)</strong> foi aprovada pelo Congresso, mas <strong>ainda não havia sido promulgada</strong> na data desta verificação: este caderno ensina o texto <strong>vigente</strong> e traz um quadro com as mudanças previstas. As questões são <strong>autorais</strong>.</p>''', "Fontes e atualização")}''', first=True)

TOC = [("u","UNIDADE 1 · FUNDAMENTOS","U1"),("","1. Conceito constitucional de segurança pública","A01"),("","2. Dever do Estado, direito e responsabilidade de todos","A02"),("","3. Os órgãos do art. 144: visão geral","A03"),
 ("u","UNIDADE 2 · ÓRGÃOS DA UNIÃO","U2"),("","4. Polícia Federal","A04"),("","5. Polícia Rodoviária Federal","A05"),("","6. Polícia Ferroviária Federal","A06"),
 ("u","UNIDADE 3 · ÓRGÃOS DOS ESTADOS E DO DF","U3"),("","7. Polícias Civis","A07"),("","8. Polícias Militares","A08"),("","9. Corpos de Bombeiros Militares","A09"),("","10. Polícias Penais","A10"),("","11. Subordinação e o caso do Distrito Federal","A11"),
 ("u","UNIDADE 4 · MUNICÍPIOS","U4"),("","12. Guardas Municipais: previsão constitucional","A12"),("","13. Guardas Municipais: lei e entendimento do STF","A13"),("","14. Segurança viária e agentes de trânsito","A14"),
 ("u","UNIDADE 5 · ORGANIZAÇÃO E COMPARAÇÕES","U5"),("","15. Polícia administrativa x polícia judiciária","A15"),("","16. Quadro comparativo dos órgãos","A16"),("","17. Uma noite na cidade: quem atende?","A17"),("","18. Noções de organização: SUSP e outros órgãos","A18"),("","19. Atualização: PEC da Segurança Pública","A19"),
 ("u","REVISÃO E PRÁTICA","RV"),("","Mapa conceitual · Confusões mais comuns","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),("","Gabarito, respostas dos treinos e referências","R4")]
toc = "".join(f'<li class="u"><span class="t">{t}</span><span class="p" data-pg="{m}"></span></li>' if k=="u" else f'<li><span class="t">{t}</span><span class="p" data-pg="{m}"></span></li>' for k,t,m in TOC)
add(f'''<div class="unit"><span class="u">MAPA DO CADERNO</span></div><h1 class="big">Sumário</h1><ol class="toc" style="border-top:3px solid #0b2a5b;margin-top:6pt">{toc}</ol>''')

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
opener("01","UNIDADE 1","Fundamentos",["Conceito constitucional de segurança pública","Dever do Estado, direito e responsabilidade de todos","Os órgãos do art. 144: visão geral"],"U1")

add(head(U1,T1,'O que é <span class="hl">segurança pública</span>?','O conceito que abre o art. 144.', "A01") +
 lei(cf("Art. 144, caput e incisos I a VI"), A144_CAPUT, "Inciso VI incluído pela EC nº 104/2019 (polícias penais).") +
 traduz(p('Segurança pública é a atividade que o Estado exerce para manter a <strong>ordem pública</strong> (a convivência pacífica nas ruas) e proteger a <strong>incolumidade das pessoas e do patrimônio</strong> (“incolumidade” quer dizer estar a salvo, sem sofrer dano). Ela é exercida por <strong>órgãos específicos</strong>, listados nos incisos do art. 144.')) +
 memo('Finalidades: preservação da <strong>ordem pública</strong> e da <strong>incolumidade das pessoas e do patrimônio</strong>. Natureza: <strong>dever</strong> do Estado, <strong>direito e responsabilidade de todos</strong>.'))

add(pratica_title() +
 flow([("capitol",["DEVER","do Estado"]),("people",["DIREITO E","RESPONSABILIDADE","de todos"]),("shield",["ÓRGÃOS","do art. 144"]),("check",["ORDEM PÚBLICA","+ incolumidade das","pessoas e do patrimônio"])],
      "O caput do art. 144 em uma linha.", colors=colors("n","o","b","g")) +
 ex(p('Uma escola organiza, com a Polícia Militar, uma palestra sobre segurança no trânsito, e os moradores de um bairro criam um grupo para comunicar à polícia situações suspeitas. As duas iniciativas mostram a ideia de que a segurança pública é <b>responsabilidade de todos</b>. Mas o <b>dever</b> de exercer a segurança pública, com uso da força quando necessário, é do <b>Estado</b>, por meio dos órgãos do art. 144.')) +
 pega('<ul><li>Atenção à ordem das palavras: “<b>dever do Estado</b>, <b>direito e responsabilidade de todos</b>”. A prova troca: “dever de todos e responsabilidade do Estado” está errado.</li><li>A finalidade é a preservação da ordem pública e da <b>incolumidade</b> das pessoas e do patrimônio.</li><li>A segurança aparece também como direito <b>individual</b> (art. 5º, caput) e como direito <b>social</b> (art. 6º).</li></ul>') +
 kw(["dever do Estado","direito e responsabilidade de todos","ordem pública","incolumidade","pessoas e patrimônio"]))

add(head(U1,T1,'Dever do Estado, direito e <span class="hl">responsabilidade de todos</span>','Quem executa e quem colabora.', "A02") +
 table(["Expressão","Significado","Exemplo"],[
  ["Dever do Estado","O Estado é <b>obrigado</b> a garantir a segurança pública, por meio dos seus órgãos. É uma atividade típica de Estado.","Manter policiamento nas ruas e investigar crimes."],
  ["Direito de todos","Qualquer pessoa pode <b>exigir</b> do Estado a proteção da segurança.","Cobrar iluminação, patrulhamento e atendimento às ocorrências."],
  ["Responsabilidade de todos","A sociedade também deve <b>colaborar</b>, sem substituir o Estado.","Denunciar crimes, colaborar com investigações, respeitar as leis."]],["24%",None,"32%"]) +
 traduz(p('O Estado é o “dono do serviço”: só ele pode exercer a segurança pública com <strong>poder de polícia</strong> e uso legítimo da força. A população tem o direito de exigir esse serviço e a responsabilidade de colaborar, por exemplo denunciando um crime. Colaborar não significa “fazer justiça com as próprias mãos”.')) +
 memo('<strong>DEVER</strong>: Estado. <strong>DIREITO E RESPONSABILIDADE</strong>: todos. A colaboração da sociedade não transfere ao particular as funções dos órgãos policiais.') +
 pega('<ul><li>Particulares e empresas de segurança privada <b>não</b> são órgãos de segurança pública: a segurança privada é atividade regulada por lei e fiscalizada pela Polícia Federal.</li><li>Qualquer pessoa <b>pode</b> prender quem esteja em flagrante delito, e as autoridades policiais e seus agentes <b>devem</b> fazê-lo (Código de Processo Penal, art. 301).</li></ul>'))

orgaos_mapa = f'''<figure><svg viewBox="0 0 640 330" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<rect x="230" y="6" width="180" height="44" rx="12" fill="{C['navy']}"/><text x="320" y="33" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">ART. 144</text>
<path d="M320 50 V66 M110 66 H530 M110 66 V80 M320 66 V80 M530 66 V80" stroke="{C['ink']}" stroke-width="2.5" fill="none"/>
<rect x="10" y="80" width="200" height="200" rx="14" fill="{C['sky']}" stroke="{C['blue']}" stroke-width="2.5"/><text x="110" y="104" text-anchor="middle" font-weight="900" font-size="14" fill="{C['blue']}">UNIÃO</text>
''' + "".join(f'<rect x="24" y="{116+i*38}" width="172" height="30" rx="8" fill="#fff" stroke="{C["blue"]}"/><text x="110" y="{136+i*38}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{C["ink"]}">{t}</text>' for i,t in enumerate(["Polícia Federal","Polícia Rodoviária Federal","Polícia Ferroviária Federal","Polícia Penal federal"])) + f'''
<rect x="220" y="80" width="200" height="200" rx="14" fill="{C['greensoft']}" stroke="{C['green']}" stroke-width="2.5"/><text x="320" y="104" text-anchor="middle" font-weight="900" font-size="14" fill="{C['green']}">ESTADOS E DF</text>
''' + "".join(f'<rect x="234" y="{116+i*38}" width="172" height="30" rx="8" fill="#fff" stroke="{C["green"]}"/><text x="320" y="{136+i*38}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{C["ink"]}">{t}</text>' for i,t in enumerate(["Polícias Civis","Polícias Militares","Corpos de Bombeiros Militares","Polícias Penais estaduais/distrital"])) + f'''
<rect x="430" y="80" width="200" height="200" rx="14" fill="{C['goldsoft']}" stroke="{C['golddeep']}" stroke-width="2.5"/><text x="530" y="104" text-anchor="middle" font-weight="900" font-size="14" fill="{C['golddeep']}">MUNICÍPIOS</text>
<rect x="444" y="116" width="172" height="30" rx="8" fill="#fff" stroke="{C['golddeep']}" stroke-dasharray="5 3"/><text x="530" y="136" text-anchor="middle" font-size="11.5" font-weight="700" fill="{C['ink']}">Guardas Municipais (§ 8º)</text>
<text x="530" y="170" text-anchor="middle" font-size="10.5" fill="{C['ink']}">não estão nos incisos I a VI;</text>
<text x="530" y="186" text-anchor="middle" font-size="10.5" fill="{C['ink']}">previsão no § 8º (“poderão</text>
<text x="530" y="202" text-anchor="middle" font-size="10.5" fill="{C['ink']}">constituir”). O STF as reconhece</text>
<text x="530" y="218" text-anchor="middle" font-size="10.5" fill="{C['ink']}">como integrantes do sistema</text>
<text x="530" y="234" text-anchor="middle" font-size="10.5" fill="{C['ink']}">de segurança pública.</text>
<text x="320" y="310" text-anchor="middle" font-size="12" font-weight="900" fill="{C['navy']}">Incisos I a VI: 6 incisos, órgãos da União e dos Estados/DF</text>
</svg><figcaption>Os órgãos de segurança pública organizados por ente federativo.</figcaption></figure>'''
add(head(U1,T1,'Os órgãos do art. 144: <span class="hl">visão geral</span>','Quem é quem, organizado por ente federativo.', "A03") + orgaos_mapa +
 traduz(p('O art. 144 distribui a segurança pública entre a <strong>União</strong> (PF, PRF, PFF e Polícia Penal federal) e os <strong>Estados e o DF</strong> (Polícias Civis, Polícias Militares, Corpos de Bombeiros Militares e Polícias Penais). Os <strong>Municípios</strong> aparecem no § 8º: <strong>podem</strong> criar guardas municipais.')) +
 memo('Incisos: <b>I</b> PF · <b>II</b> PRF · <b>III</b> PFF · <b>IV</b> Polícias Civis · <b>V</b> PM e CBM · <b>VI</b> Polícias Penais. Guardas Municipais: <strong>§ 8º</strong>.'))

add(pratica_title() +
 flow([("capitol",["UNIÃO","PF · PRF · PFF","Polícia Penal federal"]),("map",["ESTADOS E DF","PC · PM · CBM","Polícias Penais"]),("house",["MUNICÍPIOS","Guardas Municipais","(§ 8º)"])],
      "Três níveis da Federação, três conjuntos de órgãos.", colors=colors("b","g","o")) +
 ex(p('O art. 144 lista os órgãos com funções de segurança pública. Por isso o STF tem entendido que <b>os Estados não podem criar outros órgãos de segurança pública</b> fora desse modelo, por exemplo transformando uma perícia em polícia autônoma. A exceção que gerou mais debate é a das <b>Guardas Municipais</b>, que estão no § 8º e não nos incisos. Em 2023, o STF reconheceu que elas integram o Sistema de Segurança Pública (ADPF 995).')) +
 pega('<ul><li>“Polícias penais <b>municipais</b>” → <b>não existem</b>. O inciso VI fala em polícias penais <b>federal, estaduais e distrital</b>.</li><li>Polícia Militar e Corpo de Bombeiros Militar estão no <b>mesmo inciso</b> (V).</li><li><b>Forças Armadas</b> (art. 142) e <b>Força Nacional</b> não estão no rol do art. 144.</li><li>A <b>Polícia Penal</b> foi incluída pela <b>EC nº 104/2019</b>.</li></ul>') +
 kw(["6 incisos","União","Estados e DF","Municípios: § 8º","EC nº 104/2019","rol do art. 144"]))

treino(1, [
 ("A segurança pública é dever de todos e responsabilidade do Estado.","E","É dever do Estado, direito e responsabilidade de todos."),
 ("A segurança pública é exercida para a preservação da ordem pública e da incolumidade das pessoas e do patrimônio.","C","Art. 144, caput."),
 ("As polícias penais foram incluídas no art. 144 pela EC nº 104/2019.","C","Inciso VI e § 5º-A."),
 ("A Constituição prevê polícias penais federal, estaduais, distrital e municipais.","E","Não há polícia penal municipal."),
 ("Polícias militares e corpos de bombeiros militares estão previstos no mesmo inciso do art. 144.","C","Inciso V."),
 ("As Forças Armadas integram o rol de órgãos de segurança pública do art. 144.","E","Estão no art. 142, fora do rol do art. 144.")])

# ================================================================ UNIDADE 2
opener("02","UNIDADE 2","Órgãos da União",["Polícia Federal","Polícia Rodoviária Federal","Polícia Ferroviária Federal"],"U2")

add(head(U2,T2,'<span class="hl">Polícia Federal</span>','Quatro competências, uma delas exclusiva.', "A04") +
 lei(cf("Art. 144, § 1º"), A144_1, "Redação dada pela EC nº 19/1998.") +
 cards([("search","I · Apurar infrações","Contra a ordem política e social, bens, serviços e interesses da União, autarquias e empresas públicas federais; e infrações com repercussão interestadual ou internacional que exijam repressão uniforme.",C['blue']),
        ("alert","II · Drogas, contrabando e descaminho","Prevenir e reprimir, sem prejuízo da ação fazendária e de outros órgãos.",C['red']),
        ("plane","III · Marítima, aeroportuária e de fronteiras","Controle de portos, aeroportos e fronteiras.",C['golddeep']),
        ("gavel","IV · Polícia judiciária da União","Com <b>exclusividade</b>.",C['navy'])],2))

add(pratica_title() +
 flow([("coin",["CRIME CONTRA","BENS DA UNIÃO","ex.: Correios"]),("globe",["REPERCUSSÃO","INTERESTADUAL OU","INTERNACIONAL"]),("plane",["PORTOS, AEROPORTOS","E FRONTEIRAS"]),("gavel",["POLÍCIA JUDICIÁRIA","DA UNIÃO","exclusiva"])],
      "Quando o caso é da Polícia Federal.", colors=colors("o","b","n","r")) +
 traduz(p('A PF é a “polícia investigativa da União”. Ela apura crimes que atingem <strong>bens, serviços e interesses federais</strong> (como roubo a uma agência dos Correios, que é empresa pública federal), crimes que <strong>ultrapassam as fronteiras de um Estado</strong> e exigem resposta uniforme, além de combater o tráfico de drogas, o contrabando e o descaminho e de controlar portos, aeroportos e fronteiras.'),"profa") +
 ex(p('Roubo a uma agência da <b>Caixa Econômica Federal</b> (empresa pública federal): caso da <b>PF</b>. Roubo a uma agência do <b>Banco do Brasil</b> (sociedade de economia mista): em regra, caso da <b>Polícia Civil</b>, já que o § 1º, I, menciona autarquias e empresas públicas federais, e não sociedades de economia mista.')) +
 pega('<ul><li>A PF exerce <b>com exclusividade</b> a polícia judiciária <b>da União</b>.</li><li>O inciso I fala em entidades <b>autárquicas e empresas públicas</b> federais. <b>Sociedade de economia mista</b> (Banco do Brasil, Petrobras) <b>não</b> está na lista.</li><li>Tráfico de drogas, contrabando e descaminho: a PF previne e reprime “<b>sem prejuízo</b>” da atuação de outros órgãos. A competência <b>não</b> é exclusiva.</li></ul>'))

add(head(U2,T2,'Polícia <span class="hl">Rodoviária Federal</span>','O patrulhamento ostensivo das rodovias federais.', "A05") +
 lei(cf("Art. 144, § 2º"), A144_2, "Redação dada pela EC nº 19/1998.") +
 traduz(p('A PRF é a polícia que você vê nas <strong>BRs</strong>, as rodovias federais. Sua função constitucional é o <strong>patrulhamento ostensivo</strong>: estar visível, fiscalizar, prevenir e reprimir infrações nas rodovias federais, na forma da lei. Ela é organizada e mantida pela <strong>União</strong>.')) +
 flow([("road",["RODOVIA","FEDERAL","(BR)"]),("eye",["PATRULHAMENTO","OSTENSIVO","visível"]),("car",["FISCALIZAÇÃO","trânsito e","crimes em flagrante"])],
      "PRF: presença ostensiva nas rodovias federais.", colors=colors("b","o","g")) +
 memo('PRF: <strong>patrulhamento ostensivo</strong> das <strong>rodovias federais</strong>, <strong>na forma da lei</strong>. Órgão permanente, organizado e mantido pela <strong>União</strong>, estruturado em carreira.'))
atencao(pega('<ul><li>A PRF atua nas rodovias <b>federais</b>. Rodovias estaduais costumam ser fiscalizadas pela polícia militar rodoviária do Estado ou pelo órgão estadual de trânsito.</li><li>Patrulhamento <b>ostensivo</b> ≠ investigação: a PRF não exerce polícia judiciária. Um crime grave descoberto na BR é levado à autoridade com atribuição para investigá-lo (PF ou Polícia Civil, conforme o caso).</li><li>A expressão é “patrulhamento ostensivo” (PRF e PFF), enquanto a PM tem “polícia ostensiva e preservação da ordem pública”.</li></ul>') +
 ex(p('Durante uma fiscalização numa BR, a PRF encontra drogas escondidas num caminhão. Os policiais rodoviários realizam a <b>prisão em flagrante</b> e apresentam o caso à autoridade competente. A investigação posterior, em regra, cabe à <b>Polícia Federal</b> se houver tráfico internacional ou interestadual com repercussão que exija repressão uniforme, ou à <b>Polícia Civil</b> nos demais casos.')),
 ["rodovias federais","patrulhamento ostensivo","na forma da lei","União","estruturado em carreira"])

add(head(U2,T2,'Polícia <span class="hl">Ferroviária Federal</span>','A polícia das ferrovias federais.', "A06") +
 lei(cf("Art. 144, § 3º"), A144_3) +
 traduz(p('A Polícia Ferroviária Federal tem a mesma lógica da PRF, só que nas <strong>ferrovias federais</strong>: patrulhamento ostensivo, na forma da lei. Embora prevista na Constituição desde 1988, ela <strong>nunca foi estruturada</strong> como carreira nos mesmos moldes da PF e da PRF. Mesmo assim, aparece em provas que cobram a literalidade do art. 144.')) +
 table(["","PRF (§ 2º)","PFF (§ 3º)"],[["Onde atua","Rodovias federais","Ferrovias federais"],["Função","Patrulhamento ostensivo","Patrulhamento ostensivo"],["Quem mantém","União","União"],["Natureza","Órgão permanente, estruturado em carreira","Órgão permanente, estruturado em carreira"]],["22%",None,None]) +
 memo('PRF → <strong>RODO</strong>vias federais. PFF → <strong>FERRO</strong>vias federais. As duas: <strong>patrulhamento ostensivo</strong>, “na forma da lei”, mantidas pela <strong>União</strong>.') +
 pega('<ul><li>A PFF <b>está</b> na Constituição (inciso III e § 3º), mesmo sem estrutura efetiva. Alternativa que diga que “a CF não prevê polícia ferroviária” está <b>errada</b>.</li><li>Não confunda “ferroviária <b>federal</b>” com a segurança de metrôs e trens urbanos estaduais ou municipais, feita por outros órgãos e empresas.</li></ul>'))

treino(2, [
 ("A Polícia Federal exerce, com exclusividade, as funções de polícia judiciária da União.","C","Art. 144, § 1º, IV."),
 ("Cabe à Polícia Federal apurar infrações penais em detrimento de sociedades de economia mista federais.","E","O inciso I menciona autarquias e empresas públicas, não sociedades de economia mista."),
 ("A Polícia Federal previne e reprime o tráfico ilícito de entorpecentes com exclusividade.","E","“Sem prejuízo” da ação de outros órgãos."),
 ("A Polícia Rodoviária Federal destina-se, na forma da lei, ao patrulhamento ostensivo das rodovias federais.","C","Art. 144, § 2º."),
 ("A Polícia Ferroviária Federal não tem previsão constitucional.","E","Está no inciso III e no § 3º."),
 ("Compete à Polícia Federal exercer as funções de polícia marítima, aeroportuária e de fronteiras.","C","Art. 144, § 1º, III.")])

# ================================================================ UNIDADE 3
opener("03","UNIDADE 3","Órgãos dos Estados e do DF",["Polícias Civis","Polícias Militares","Corpos de Bombeiros Militares","Polícias Penais","Subordinação e o caso do Distrito Federal"],"U3")

add(head(U3,T3,'<span class="hl">Polícias Civis</span>','A polícia investigativa dos Estados e do DF.', "A07") +
 lei(cf("Art. 144, § 4º"), A144_4) +
 traduz(p('A Polícia Civil é a <strong>polícia judiciária</strong> dos Estados e do DF: ela <strong>investiga</strong> os crimes depois que acontecem, reúne provas e instaura o <strong>inquérito policial</strong>. É dirigida por <strong>delegados de polícia de carreira</strong>. Ela só não investiga os crimes de competência da União (que cabem à PF) e os crimes <strong>militares</strong>.')) +
 cards([("search","Polícia judiciária","Investigar crimes e auxiliar a Justiça criminal.",C['blue']),("badge","Delegado de carreira","Quem dirige a Polícia Civil.",C['golddeep']),("xmark","Exceções","Competência da União (PF) e infrações militares.",C['red'])],3) +
 memo('Polícia Civil: <strong>polícia judiciária</strong> + apuração de infrações penais, <strong>ressalvada a competência da União</strong> e <strong>exceto as militares</strong>. Dirigida por <strong>delegado de carreira</strong>.'))
atencao(pega('<ul><li>“Exceto as <b>militares</b>”: os crimes militares são apurados pela <b>polícia judiciária militar</b> (por meio de inquérito policial militar), e não pela Polícia Civil.</li><li>Polícia Civil <b>investiga</b>; Polícia Militar faz <b>policiamento ostensivo</b>. É a diferença mais cobrada do art. 144.</li><li>Quem dirige a Polícia Civil é o <b>delegado de polícia de carreira</b>, e não um oficial militar nem um membro do Ministério Público.</li></ul>') +
 flow([("alert",["CRIME","acontece"]),("siren",["PM","atende e prende","em flagrante"]),("search",["POLÍCIA CIVIL","investiga","(inquérito)"]),("gavel",["MP E","JUDICIÁRIO","ação penal"])],
      "Ciclo da ocorrência comum: a PM previne e atende; a Civil investiga.", colors=colors("r","b","o","n")),
 ["polícia judiciária","apuração de infrações penais","delegado de carreira","ressalvada a competência da União","exceto as militares"])

add(head(U3,T3,'<span class="hl">Polícias Militares</span>','Polícia ostensiva e preservação da ordem pública.', "A08") +
 lei(cf("Art. 144, § 5º (1ª parte)"),'<p>§ 5º Às polícias militares cabem a polícia ostensiva e a preservação da ordem pública; (...)</p>') +
 traduz(p('A Polícia Militar é a polícia <strong>fardada e visível</strong>: ela patrulha as ruas para <strong>prevenir</strong> crimes, atende ocorrências e restabelece a ordem quando ela é quebrada. Por isso se diz que faz <strong>polícia ostensiva</strong> (que se mostra) e <strong>preservação da ordem pública</strong>. É também <strong>força auxiliar e reserva do Exército</strong>.')) +
 cards([("eye","Polícia ostensiva","Presença visível que previne o crime.",C['blue']),("shield","Ordem pública","Manter e restabelecer a tranquilidade.",C['green']),("flag","Força auxiliar","Reserva do Exército (§ 6º).",C['navy'])],3) +
 memo('PM: <strong>polícia ostensiva</strong> + <strong>preservação da ordem pública</strong>. É <strong>força auxiliar e reserva do Exército</strong>, mas se subordina ao <strong>Governador</strong>.'))
atencao(pega('<ul><li>“A PM é subordinada ao Exército” → <b>errado</b>: ela é <b>força auxiliar e reserva</b> do Exército, mas se <b>subordina aos Governadores</b> (§ 6º).</li><li>A PM <b>não</b> é polícia judiciária comum: a investigação dos crimes comuns cabe à Polícia Civil. A PM exerce polícia judiciária apenas quanto aos <b>crimes militares</b> de seus integrantes.</li><li>“Polícia ostensiva” (PM) é mais amplo que “patrulhamento ostensivo” (PRF e PFF): abrange todas as fases do policiamento, da prevenção à repressão imediata.</li></ul>') +
 ex(p('Um assalto está acontecendo numa padaria. A população liga para o 190, e a <b>Polícia Militar</b> chega, prende o assaltante em flagrante e o leva à delegacia. A partir daí, a <b>Polícia Civil</b> lavra o auto de prisão em flagrante e conduz a investigação.')),
 ["polícia ostensiva","preservação da ordem pública","força auxiliar","reserva do Exército","subordinação ao Governador"])

add(head(U3,T3,'Corpos de <span class="hl">Bombeiros Militares</span>','Defesa civil e atribuições definidas em lei.', "A09") +
 lei(cf("Art. 144, § 5º (2ª parte)"),'<p>§ 5º (...) aos corpos de bombeiros militares, além das atribuições definidas em lei, incumbe a execução de atividades de defesa civil.</p>') +
 traduz(p('Os Bombeiros Militares combatem incêndios, fazem salvamentos e resgates e atuam em desastres. A Constituição destaca a <strong>execução de atividades de defesa civil</strong>, além das atribuições que a lei definir (como prevenção de incêndios e vistorias). Assim como a PM, são <strong>forças auxiliares e reserva do Exército</strong> e se subordinam ao <strong>Governador</strong>.'),"profa") +
 flow([("fire",["INCÊNDIO","combate"]),("umbrella",["DESASTRE","enchente,","deslizamento"]),("people",["SALVAMENTO","e resgate"]),("shield",["DEFESA","CIVIL","(CF, § 5º)"])],
      "Atividades típicas dos Corpos de Bombeiros Militares.", colors=colors("r","b","o","g")) +
 memo('CBM: <strong>defesa civil</strong> + <strong>atribuições definidas em lei</strong>. Estão no inciso <strong>V</strong>, junto com a PM.') +
 pega('<ul><li>Bombeiros Militares <b>são</b> órgãos de segurança pública (inciso V).</li><li>Defesa civil é tarefa <b>expressa</b> dos Bombeiros na CF; a PM tem polícia ostensiva e ordem pública.</li><li>Bombeiros e PM: forças auxiliares e reserva do <b>Exército</b> (não da Marinha nem da Aeronáutica).</li></ul>'))

add(head(U3,T3,'Polícias <span class="hl">Penais</span>','O órgão mais novo do art. 144.', "A10") +
 lei(cf("Art. 144, § 5º-A"), A144_5A, "Incluído pela EC nº 104/2019.") +
 traduz(p('A Polícia Penal cuida da <strong>segurança dos estabelecimentos penais</strong>: presídios, penitenciárias e cadeias públicas. Antes da EC nº 104/2019, essa função era exercida principalmente por agentes penitenciários, sem status de polícia na Constituição. Hoje existem polícias penais <strong>federal, estaduais e distrital</strong>, vinculadas ao órgão que administra o sistema penal de cada ente.')) +
 flow([("jail",["ESTABELECIMENTO","PENAL","presídio"]),("shield",["SEGURANÇA","interna e","externa"]),("sitemap",["VINCULAÇÃO","ao órgão administrador","do sistema penal"])],
      "Polícia Penal: segurança dos estabelecimentos penais.", colors=colors("n","b","o")) +
 memo('Polícia Penal: <strong>segurança dos estabelecimentos penais</strong>. Esferas: <strong>federal, estaduais e distrital</strong>. Criada pela <strong>EC nº 104/2019</strong>.') +
 pega('<ul><li>Não existe Polícia Penal <b>municipal</b>.</li><li>A Polícia Penal é <b>vinculada ao órgão administrador do sistema penal</b> da unidade federativa (ex.: secretaria de administração penitenciária).</li><li>As polícias penais <b>estaduais e distrital</b> se subordinam ao <b>Governador</b> (§ 6º); a federal, à União.</li></ul>'))

add(head(U3,T3,'Subordinação e o caso do <span class="hl">Distrito Federal</span>','A quem cada órgão responde.', "A11") +
 lei(cf("Art. 144, § 6º"), A144_6, "Redação dada pela EC nº 104/2019.") +
 table(["Órgão","Mantido por","Subordinado a"],[
  ["PF, PRF, PFF, Polícia Penal federal","União","União (Poder Executivo federal)"],
  ["PC, PM, CBM e Polícia Penal dos Estados","Estado","<b>Governador</b> do Estado"],
  ["PC, PM, CBM e Polícia Penal do DF","<b>União</b> (art. 21, XIV)","<b>Governador do DF</b>"],
  ["Guarda Municipal","Município","Prefeito (Município)"]],["38%","24%",None]) +
 traduz(p('Regra simples: cada órgão responde ao chefe do Executivo do seu ente. A única peculiaridade é o <strong>Distrito Federal</strong>: suas polícias e seus bombeiros são <strong>organizados e mantidos pela União</strong> (art. 21, XIV), mas continuam <strong>subordinados ao Governador do DF</strong>.')) +
 memo('PM e CBM: <strong>forças auxiliares e reserva do Exército</strong>, subordinados aos <strong>Governadores</strong>. DF: <strong>mantidos pela União</strong>, <strong>subordinados ao Governador do DF</strong>.') +
 pega('<ul><li>“As polícias do DF são subordinadas ao Presidente da República” → <b>errado</b>: são mantidas pela União, mas subordinadas ao Governador do DF.</li><li>O § 6º menciona Governadores dos Estados, do Distrito Federal e <b>dos Territórios</b>.</li></ul>'))

treino(3, [
 ("Às polícias civis, dirigidas por delegados de polícia de carreira, incumbem as funções de polícia judiciária, inclusive quanto às infrações militares.","E","Exceto as militares."),
 ("Às polícias militares cabem a polícia ostensiva e a preservação da ordem pública.","C","Art. 144, § 5º."),
 ("As polícias militares são forças auxiliares e reserva do Exército e, por isso, subordinam-se ao Comandante do Exército.","E","Subordinam-se aos Governadores (§ 6º)."),
 ("Aos corpos de bombeiros militares incumbe a execução de atividades de defesa civil, além das atribuições definidas em lei.","C","Art. 144, § 5º."),
 ("Às polícias penais cabe a segurança dos estabelecimentos penais.","C","Art. 144, § 5º-A."),
 ("As polícias civil e militar do Distrito Federal são organizadas e mantidas pela União, mas subordinam-se ao Governador do DF.","C","Art. 21, XIV, e art. 144, § 6º.")])

# ================================================================ UNIDADE 4
opener("04","UNIDADE 4","Municípios",["Guardas Municipais: previsão constitucional","Guardas Municipais: lei e entendimento do STF","Segurança viária e agentes de trânsito"],"U4")

add(head(U4,T4,'Guardas Municipais: <span class="hl">previsão constitucional</span>','O § 8º do art. 144.', "A12") +
 lei(cf("Art. 144, § 8º"), A144_8) +
 cards([("house","“Os Municípios PODERÃO”","Criar a guarda é uma <b>faculdade</b> do Município, e não uma obrigação.",C['golddeep']),
        ("shield","Proteção","Dos <b>bens, serviços e instalações</b> do Município.",C['blue']),
        ("doc","“Conforme dispuser a lei”","A lei geral é o <b>Estatuto Geral das Guardas Municipais</b> (Lei nº 13.022/2014).",C['green'])],3) +
 traduz(p('A Constituição <strong>permite</strong> que cada Município crie a sua guarda, e o texto do § 8º fala em proteger os <strong>bens, serviços e instalações</strong> municipais: a praça, a escola, o posto de saúde, o serviço de transporte. Com o tempo, a lei e o STF deixaram claro que a atuação das guardas vai além da vigilância de prédios, alcançando a <strong>segurança urbana</strong>, sempre sem investigar crimes.')) +
 memo('§ 8º: Municípios <strong>poderão</strong> constituir guardas municipais destinadas à proteção de seus <strong>bens, serviços e instalações</strong>, <strong>conforme dispuser a lei</strong>.'))

add(pratica_title() +
 flow([("house",["MUNICÍPIO","decide criar","(faculdade)"]),("doc",["LEI","municipal +","Lei nº 13.022/2014"]),("badge",["GUARDA","MUNICIPAL","instituição civil"]),("city",["PROTEÇÃO","bens, serviços,","instalações e pessoas"])],
      "Da previsão constitucional à atuação nas ruas.", colors=colors("o","n","b","g")) +
 ex(p('Um guarda municipal em patrulha numa praça presencia um furto de celular e detém o autor. Ele pode agir: <b>qualquer pessoa pode</b> prender quem esteja em flagrante delito (CPP, art. 301), e a proteção do espaço público e das pessoas que o utilizam está entre as atribuições da guarda. Em seguida, apresenta o preso à <b>Polícia Civil</b>, que conduzirá a investigação.')) +
 pega('<ul><li>As guardas municipais estão no <b>§ 8º</b>, e <b>não</b> nos incisos I a VI do art. 144.</li><li>“Os Municípios <b>deverão</b> constituir guardas” → <b>errado</b>: “<b>poderão</b>”.</li><li>A guarda municipal é instituição de caráter <b>civil</b>, e não militar.</li><li>A guarda <b>não</b> exerce polícia judiciária: não instaura inquérito nem investiga crimes.</li></ul>') +
 kw(["§ 8º","poderão constituir","bens, serviços e instalações","conforme dispuser a lei","caráter civil","sem polícia judiciária"]))

add(head(U4,T4,'Guardas Municipais: <span class="hl">lei e STF</span>','O que o Estatuto Geral e o Supremo dizem sobre a atuação das guardas.', "A13") +
 table(["Fonte","O que estabelece"],[
  ["Lei nº 13.022/2014 (Estatuto Geral das Guardas Municipais)","Define as guardas como instituições de caráter <b>civil</b>, uniformizadas e armadas conforme a lei, com função de <b>proteção municipal preventiva</b>; a competência geral é a proteção de bens, serviços, <b>logradouros públicos</b> e instalações do Município. Lista princípios (como proteção dos direitos humanos, preservação da vida e uso progressivo da força) e competências específicas, como colaborar com os demais órgãos de segurança pública e proteger a população que utiliza os bens, serviços e instalações municipais."],
  ["Lei nº 13.675/2018 (SUSP)","Inclui as guardas municipais entre os <b>integrantes operacionais</b> do Sistema Único de Segurança Pública."],
  ["STF · ADPF 995 (2023)","Reconheceu que as guardas municipais <b>integram o Sistema de Segurança Pública</b>."],
  ["STF · RE 608.588, Tema 656 (2025)","Fixou que é constitucional o exercício de <b>ações de segurança urbana</b> pelas guardas, <b>inclusive policiamento ostensivo comunitário</b>, respeitadas as atribuições dos demais órgãos do art. 144, <b>excluída qualquer atividade de polícia judiciária</b> e com <b>controle externo pelo Ministério Público</b>."]],["30%",None]) +
 memo('Guarda Municipal: <strong>caráter civil</strong> · <strong>integra o sistema de segurança pública</strong> (STF) · pode fazer <strong>policiamento ostensivo comunitário</strong> (Tema 656) · <strong>nunca polícia judiciária</strong> · controle externo do <strong>MP</strong>.'))

add(pratica_title("O que a Guarda Municipal pode e não pode") +
 table(["PODE (segundo a lei e o STF)","NÃO PODE"],[
  ["Proteger bens, serviços e instalações municipais","Instaurar inquérito policial"],
  ["Fazer patrulhamento preventivo e policiamento ostensivo comunitário","Exercer funções de polícia judiciária (investigar crimes)"],
  ["Prender em flagrante e apresentar o preso à autoridade","Invadir atribuições exclusivas dos demais órgãos do art. 144"],
  ["Colaborar com os demais órgãos de segurança pública","Atuar sem o controle externo do Ministério Público"],
  ["Atuar na proteção da população que usa os espaços públicos","Ser organizada como instituição militar"]],["50%",None],rh=False) +
 ex(p('A guarda de um município realiza rondas diárias nas escolas municipais e nas praças, atende a um chamado de briga num terminal de ônibus e conduz os envolvidos à delegacia. Tudo isso está dentro do entendimento do STF. Já a abertura de uma investigação, com depoimentos formais e relatório para o Ministério Público, seria atividade de <b>polícia judiciária</b>, vedada à guarda.')) +
 pega('<ul><li>O Tema 656 permite o policiamento ostensivo <b>comunitário</b>, <b>respeitadas as atribuições dos demais órgãos</b>: a guarda não substitui a Polícia Militar.</li><li>Leia com atenção se a questão pergunta pela <b>literalidade da CF</b> (§ 8º: proteção de bens, serviços e instalações) ou pelo <b>entendimento do STF</b> (segurança urbana e policiamento comunitário).</li></ul>'))

add(head(U4,T4,'Segurança viária e <span class="hl">agentes de trânsito</span>','O § 10 do art. 144.', "A14") +
 lei(cf("Art. 144, § 10"), A144_10, "Incluído pela EC nº 82/2014.") +
 traduz(p('O § 10 trata da <strong>segurança viária</strong>: a segurança no trânsito, nas vias públicas. Ela compreende <strong>educação, engenharia e fiscalização de trânsito</strong> e cabe, nos Estados, no DF e nos Municípios, aos <strong>órgãos executivos de trânsito</strong> e seus <strong>agentes de trânsito</strong>, estruturados em carreira.')) +
 flow([("teacher",["EDUCAÇÃO","campanhas","e escolas"]),("road",["ENGENHARIA","sinalização","e vias"]),("eye",["FISCALIZAÇÃO","agentes de","trânsito"]),("check",["MOBILIDADE","URBANA","eficiente"])],
      "Os três pilares da segurança viária.", colors=colors("b","o","r","g")) +
 memo('Segurança viária: <strong>educação, engenharia e fiscalização</strong> de trânsito. Compete aos <strong>órgãos executivos de trânsito</strong> e seus <strong>agentes</strong>, estruturados em <strong>carreira</strong>. Incluída pela <strong>EC nº 82/2014</strong>.'))
atencao(pega('<ul><li>O § 10 <b>não</b> transformou os agentes de trânsito em “polícia”: eles não estão nos incisos I a VI.</li><li>No âmbito dos <b>Estados, DF e Municípios</b>. A segurança viária nas rodovias federais envolve a PRF (§ 2º).</li></ul>'), ["segurança viária","educação, engenharia e fiscalização","agentes de trânsito","carreira","EC nº 82/2014","mobilidade urbana"])

treino(4, [
 ("Os Municípios deverão constituir guardas municipais destinadas à proteção de seus bens, serviços e instalações.","E","“Poderão” constituir: é uma faculdade."),
 ("As guardas municipais estão previstas nos incisos do art. 144 da Constituição.","E","Estão no § 8º."),
 ("Segundo o STF, as guardas municipais podem exercer funções de polícia judiciária.","E","O Tema 656 exclui qualquer atividade de polícia judiciária."),
 ("Segundo o STF, é constitucional o policiamento ostensivo comunitário pelas guardas municipais, respeitadas as atribuições dos demais órgãos.","C","Tema 656 (RE 608.588)."),
 ("A segurança viária compreende a educação, a engenharia e a fiscalização de trânsito.","C","Art. 144, § 10, I."),
 ("O Estatuto Geral das Guardas Municipais define as guardas como instituições de caráter militar.","E","Caráter civil (Lei nº 13.022/2014).")])

# ================================================================ UNIDADE 5
opener("05","UNIDADE 5","Organização e comparações",["Polícia administrativa x polícia judiciária","Quadro comparativo dos órgãos","Uma noite na cidade: quem atende?","Noções de organização: SUSP e outros órgãos","Atualização: PEC da Segurança Pública"],"U5")

add(head(U5,T5,'Polícia administrativa x <span class="hl">polícia judiciária</span>','A distinção que organiza todo o art. 144.', "A15") +
 table(["","POLÍCIA ADMINISTRATIVA (OSTENSIVA)","POLÍCIA JUDICIÁRIA (INVESTIGATIVA)"],[
  ["Momento","<b>Antes</b> do crime (prevenção) e repressão imediata","<b>Depois</b> do crime"],
  ["Objetivo","Evitar o crime, manter a ordem","Apurar autoria e materialidade"],
  ["Como atua","Patrulhamento visível, fiscalização","Inquérito policial, diligências, provas"],
  ["Órgãos","PM, PRF, PFF, Guardas Municipais (segurança urbana)","Polícia Civil, Polícia Federal"],
  ["Imagem","Viatura na rua","Delegacia e investigação"]],["16%",None,None]) +
 traduz(p('Pense num jogo de futebol. A polícia <strong>administrativa</strong> é o árbitro em campo: está presente, previne faltas e para o jogo na hora. A polícia <strong>judiciária</strong> é o VAR: analisa depois o que aconteceu, reúne as provas e leva o caso para quem vai decidir (o Ministério Público e o juiz).')) +
 memo('<strong>Ostensiva/preventiva</strong>: PM (rua), PRF (BR), PFF (ferrovia), Guarda (cidade). <strong>Judiciária/investigativa</strong>: Polícia Civil (Estados/DF) e Polícia Federal (União).'))

comp = table(["Órgão","Ente","Função constitucional","Tipo","Subordinação"],[
 ["Polícia Federal","União","Apurar infrações federais e interestaduais/internacionais; drogas, contrabando e descaminho; polícia marítima, aeroportuária e de fronteiras; polícia judiciária da União (exclusiva)","Judiciária e administrativa","União"],
 ["Polícia Rodoviária Federal","União","Patrulhamento ostensivo das rodovias federais","Ostensiva","União"],
 ["Polícia Ferroviária Federal","União","Patrulhamento ostensivo das ferrovias federais","Ostensiva","União"],
 ["Polícia Penal federal","União","Segurança dos estabelecimentos penais federais","Segurança penal","União"],
 ["Polícia Civil","Estados e DF","Polícia judiciária e apuração de infrações (exceto militares e as da União)","Judiciária","Governador"],
 ["Polícia Militar","Estados e DF","Polícia ostensiva e preservação da ordem pública","Ostensiva","Governador"],
 ["Corpo de Bombeiros Militar","Estados e DF","Defesa civil e atribuições da lei","Defesa civil","Governador"],
 ["Polícia Penal estadual/distrital","Estados e DF","Segurança dos estabelecimentos penais","Segurança penal","Governador"],
 ["Guarda Municipal","Municípios","Proteção de bens, serviços e instalações (CF); segurança urbana e policiamento comunitário (STF)","Preventiva","Prefeito"]],["17%","11%",None,"14%","12%"])
add(head(U5,T5,'Quadro comparativo dos <span class="hl">órgãos</span>','A página para revisar na véspera da prova.', "A16") + comp +
 memo('Investigar → <strong>Civil</strong> (Estado) ou <strong>Federal</strong> (União). Patrulhar → <strong>PM</strong> (cidade), <strong>PRF</strong> (BR), <strong>PFF</strong> (ferrovia). Presídio → <strong>Polícia Penal</strong>. Incêndio e desastre → <strong>Bombeiros</strong>. Patrimônio e espaço municipal → <strong>Guarda</strong>.', "Resumo:"))

noite = f'''<figure><svg viewBox="0 0 640 260" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<rect width="640" height="260" rx="14" fill="#14254a"/>
{"".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="#fff" opacity=".7"/>' for x,y in [(40,30),(120,20),(210,40),(330,18),(420,35),(520,22),(600,40),(270,60),(560,70)])}
<circle cx="590" cy="48" r="18" fill="#f5e7b5"/>
<rect x="0" y="200" width="640" height="60" fill="#3a4660"/><rect x="0" y="226" width="640" height="5" fill="#f2a516" opacity=".7"/>
<rect x="20" y="110" width="80" height="90" fill="#24375f"/><rect x="108" y="130" width="60" height="70" fill="#1d2e52"/>
{"".join(f'<rect x="{30+c*22}" y="{122+r*22}" width="10" height="12" fill="#ffd98a"/>' for c in range(3) for r in range(3))}
<rect x="190" y="140" width="110" height="60" fill="#4b5875"/><path d="M190 140 h110 v10 h-110z" fill="#6b7896"/><text x="245" y="178" text-anchor="middle" font-size="11" font-weight="900" fill="#fff">PADARIA</text>
<rect x="330" y="120" width="120" height="80" fill="#2b3a5e"/>{"".join(f'<rect x="{338+k*20}" y="128" width="4" height="72" fill="#9aa6bb"/>' for k in range(6))}<text x="390" y="114" text-anchor="middle" font-size="10" font-weight="900" fill="#cfe0f8">PRESÍDIO</text>
<path d="M480 200 L520 120 L560 200Z" fill="#e2552c" opacity=".9"/><path d="M500 200 L520 150 L540 200Z" fill="#f2a516"/>
<rect x="580" y="150" width="50" height="50" fill="#2b3a5e"/><text x="605" y="146" text-anchor="middle" font-size="9" font-weight="900" fill="#cfe0f8">PRAÇA</text>
''' + "".join(f'<g transform="translate({x},{y})"><circle r="14" fill="#f2a516" stroke="#fff" stroke-width="3"/><text y="5" text-anchor="middle" font-weight="900" font-size="13" fill="#0b2a5b">{n}</text></g>' for x,y,n in [(245,126,"1"),(316,150,"2"),(520,100,"3"),(566,166,"4"),(60,96,"5"),(150,240,"6")]) + '</svg><figcaption>Seis ocorrências numa mesma noite. Qual órgão atua em cada uma?</figcaption></figure>'
add(head(U5,T5,'Uma noite na cidade: <span class="hl">quem atende?</span>','Cenário ilustrado: associe cada ocorrência ao órgão com atribuição constitucional.', "A17") + noite +
 table(["#","Ocorrência","Órgão","Por quê"],[
  ["1","Assalto em andamento na padaria","Polícia Militar","Polícia ostensiva e preservação da ordem pública (§ 5º)."],
  ["2","Tentativa de fuga e motim no presídio estadual","Polícia Penal estadual","Segurança dos estabelecimentos penais (§ 5º-A)."],
  ["3","Incêndio num terreno com risco às casas vizinhas","Corpo de Bombeiros Militar","Atribuições da lei e defesa civil (§ 5º)."],
  ["4","Vandalismo contra o parquinho da praça municipal","Guarda Municipal","Proteção de bens e instalações do Município (§ 8º)."],
  ["5","Investigação do assalto à padaria, no dia seguinte","Polícia Civil","Polícia judiciária e apuração de infrações (§ 4º)."],
  ["6","Carro com mercadorias contrabandeadas parado numa BR","PRF (flagrante) e PF (investigação)","Patrulhamento ostensivo das rodovias federais (§ 2º); contrabando (§ 1º, II)."]],["6%","30%","22%",None]))

add(head(U5,T5,'Noções de <span class="hl">organização</span>','Sistema Único de Segurança Pública e outros atores.', "A18") +
 lei(cf("Art. 144, §§ 7º e 9º"), A144_7 + A144_9, "§ 9º incluído pela EC nº 19/1998 (remuneração por subsídio).") +
 table(["Tema","Noção"],[
  ["SUSP","A Lei nº 13.675/2018 instituiu o <b>Sistema Único de Segurança Pública</b>, que integra os órgãos de segurança dos três níveis da Federação para atuação conjunta, coordenada e sistêmica. As guardas municipais estão entre os integrantes operacionais."],
  ["Remuneração (§ 9º)","Os servidores policiais dos órgãos do art. 144 são remunerados por <b>subsídio</b> (parcela única), na forma do art. 39, § 4º."],
  ["Competência legislativa","Compete à União legislar sobre normas gerais de organização, efetivo, material bélico, garantias, convocação, mobilização, inatividades e pensões das polícias militares e dos corpos de bombeiros militares (art. 22, XXI)."],
  ["Forças Armadas","Marinha, Exército e Aeronáutica (art. 142) <b>não</b> são órgãos do art. 144. Podem atuar na garantia da lei e da ordem, nos termos da CF e da lei."],
  ["Força Nacional","Programa de cooperação federativa criado por lei, que reúne profissionais de vários órgãos. Não está no rol do art. 144."]],["24%",None]) +
 memo('§ 7º: <strong>lei</strong> disciplina organização e funcionamento dos órgãos, para garantir a <strong>eficiência</strong>. § 9º: remuneração por <strong>subsídio</strong>. SUSP: <strong>Lei nº 13.675/2018</strong>.'))

PEC_BOX = "{{PEC}}"
add(head(U5,T5,'Atualização: <span class="hl">PEC da Segurança Pública</span>','O que pode mudar no art. 144 depois da promulgação.', "A19") + PEC_BOX)
add(pratica_title('Atenção na prova') + "{{PEC2}}")

treino(5, [
 ("A Polícia Militar exerce polícia ostensiva, e a Polícia Civil exerce polícia judiciária.","C","§§ 4º e 5º."),
 ("A Polícia Rodoviária Federal exerce polícia judiciária nas rodovias federais.","E","Faz patrulhamento ostensivo."),
 ("Os servidores policiais dos órgãos do art. 144 são remunerados na forma do art. 39, § 4º (subsídio).","C","Art. 144, § 9º."),
 ("A Força Nacional de Segurança Pública está prevista no rol de órgãos do art. 144.","E","Não está no rol."),
 ("A segurança dos estabelecimentos penais estaduais cabe à Polícia Militar.","E","Cabe à Polícia Penal (§ 5º-A)."),
 ("A lei disciplinará a organização e o funcionamento dos órgãos de segurança pública, de maneira a garantir a eficiência de suas atividades.","C","Art. 144, § 7º.")])

# ================================================================ REVISÃO
mapa = f'''<figure><svg viewBox="0 0 640 470" width="580" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<g stroke="#9fb1cc" stroke-width="2.5" fill="none"><path d="M320 235 L150 70"/><path d="M320 235 L490 70"/><path d="M320 235 L120 235"/><path d="M320 235 L520 235"/><path d="M320 235 L150 400"/><path d="M320 235 L490 400"/></g>
<circle cx="320" cy="235" r="74" fill="{C['navy']}"/><text x="320" y="225" text-anchor="middle" fill="{C['gold']}" font-weight="900" font-size="13">ART. 144</text>
<text x="320" y="245" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">SEGURANÇA</text><text x="320" y="262" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">PÚBLICA</text>
''' + "".join(
 f'<rect x="{x-100}" y="{y-40}" width="200" height="80" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x}" y="{y-16}" text-anchor="middle" font-weight="900" font-size="12.5" fill="{fg}">{t}</text>'
 + "".join(f'<text x="{x}" y="{y+4+i*15}" text-anchor="middle" font-size="10.8" fill="{C["ink"]}">{l}</text>' for i,l in enumerate(ls))
 for x,y,t,ls,fg,bg in [
  (150,62,"CONCEITO",["dever do Estado; direito e","responsabilidade de todos","ordem pública + incolumidade"],C['navy'],'#e3e9f3'),
  (490,62,"UNIÃO",["PF: judiciária da União (exclusiva)","PRF: rodovias · PFF: ferrovias","Polícia Penal federal"],C['blue'],C['sky']),
  (112,235,"ESTADOS E DF",["Civil: investiga (exceto militares)","PM: ostensiva · CBM: defesa civil","Penal: estabelecimentos penais"],C['green'],C['greensoft']),
  (528,235,"SUBORDINAÇÃO",["Governadores (PC, PM, CBM, PP)","PM/CBM: reserva do Exército","DF: mantidas pela União"],C['golddeep'],C['goldsoft']),
  (150,408,"MUNICÍPIOS",["§ 8º: poderão criar guardas","bens, serviços e instalações","STF: policiamento comunitário"],C['red'],C['redsoft']),
  (490,408,"ORGANIZAÇÃO",["§ 7º lei · § 9º subsídio","§ 10 segurança viária","SUSP: Lei nº 13.675/2018"],C['navy'],'#e3e9f3')]) + '</svg><figcaption>Mapa conceitual do Caderno 04.</figcaption></figure>'
add('<div class="marker">§§R1§§</div><div class="unit"><span class="u">REVISÃO</span><span class="t">Véspera da prova</span></div><h1 class="big">Mapa <span class="hl">conceitual</span></h1><p class="lead">O art. 144 em seis blocos. Explique cada caixa em voz alta.</p>' + mapa)

add('<div class="unit"><span class="u">REVISÃO</span><span class="t">Pontos de confusão</span></div><h1 class="big">As confusões <span class="hl">mais comuns</span></h1><p class="lead">Os pares de conceitos que mais derrubam candidatos neste tema.</p>' +
 table(["Confusão","O certo é"],[
  ["Dever x responsabilidade","<b>Dever</b> do Estado; <b>direito e responsabilidade</b> de todos."],
  ["PM x Polícia Civil","PM: polícia <b>ostensiva</b> e ordem pública. Civil: polícia <b>judiciária</b> e apuração de infrações."],
  ["PF x Polícia Civil","PF: infrações contra a União, autarquias e empresas públicas federais e casos interestaduais/internacionais. Civil: o restante (exceto militares)."],
  ["Empresa pública x sociedade de economia mista","PF apura crimes contra <b>empresas públicas</b> federais (ex.: Caixa, Correios); não menciona sociedades de economia mista (ex.: Banco do Brasil)."],
  ["PRF x PFF","PRF: <b>rodovias</b> federais. PFF: <b>ferrovias</b> federais. Ambas: patrulhamento ostensivo."],
  ["Reserva do Exército x subordinação","PM e CBM são <b>reserva</b> do Exército, mas se <b>subordinam</b> aos Governadores."],
  ["Polícia Penal","Federal, estaduais e distrital. <b>Não há municipal</b>. Incluída pela EC nº 104/2019."],
  ["DF","Polícias e bombeiros <b>mantidos pela União</b>, <b>subordinados ao Governador do DF</b>."],
  ["Guardas: “poderão” x “deverão”","Os Municípios <b>poderão</b> constituir guardas (§ 8º)."],
  ["Guardas: CF x STF","CF: bens, serviços e instalações. STF (Tema 656): segurança urbana e policiamento ostensivo comunitário, <b>sem polícia judiciária</b>."],
  ["Forças Armadas e Força Nacional","<b>Não</b> estão no rol do art. 144."],
  ["PEC da Segurança Pública","Aprovada pelo Congresso, mas <b>não promulgada</b> na data desta edição: vale o texto vigente."]],["34%",None]))

FC = [("CONCEITO","Natureza da segurança pública (caput)?","Dever do Estado, direito e responsabilidade de todos."),
 ("CONCEITO","Finalidades da segurança pública?","Preservação da ordem pública e da incolumidade das pessoas e do patrimônio."),
 ("ROL","Quais são os órgãos dos incisos I a VI?","PF, PRF, PFF, Polícias Civis, PM e CBM, Polícias Penais."),
 ("PF","Qual competência a PF exerce com exclusividade?","As funções de polícia judiciária da União."),
 ("PF","A PF apura crimes contra quais entidades federais?","União, entidades autárquicas e empresas públicas (não sociedades de economia mista)."),
 ("PF","Funções de polícia marítima, aeroportuária e de fronteiras?","Cabem à Polícia Federal (§ 1º, III)."),
 ("PRF","Função da PRF?","Patrulhamento ostensivo das rodovias federais, na forma da lei."),
 ("PFF","Função da PFF?","Patrulhamento ostensivo das ferrovias federais, na forma da lei."),
 ("CIVIL","Quem dirige as polícias civis?","Delegados de polícia de carreira."),
 ("CIVIL","Quais infrações a Polícia Civil não apura?","As de competência da União e as militares."),
 ("PM","Funções da Polícia Militar?","Polícia ostensiva e preservação da ordem pública."),
 ("CBM","O que incumbe aos bombeiros militares, além da lei?","A execução de atividades de defesa civil."),
 ("PENAL","Função das polícias penais?","Segurança dos estabelecimentos penais."),
 ("PENAL","Qual emenda criou as polícias penais?","EC nº 104/2019."),
 ("SUBORDINAÇÃO","A quem se subordinam PM, CBM, PC e polícias penais estaduais?","Aos Governadores dos Estados, do DF e dos Territórios."),
 ("SUBORDINAÇÃO","PM e CBM são o quê em relação ao Exército?","Forças auxiliares e reserva do Exército."),
 ("DF","Quem organiza e mantém as polícias do DF?","A União (art. 21, XIV)."),
 ("GUARDA","Onde estão as guardas municipais no art. 144?","No § 8º."),
 ("GUARDA","Finalidade constitucional das guardas?","Proteção dos bens, serviços e instalações do Município."),
 ("GUARDA","O que o STF decidiu no Tema 656?","Guardas podem exercer segurança urbana e policiamento ostensivo comunitário, sem polícia judiciária."),
 ("GUARDA","Qual é o Estatuto Geral das Guardas Municipais?","Lei nº 13.022/2014."),
 ("VIÁRIA","O que compreende a segurança viária?","Educação, engenharia e fiscalização de trânsito (§ 10)."),
 ("ORGANIZAÇÃO","Como são remunerados os policiais do art. 144?","Por subsídio, na forma do art. 39, § 4º (§ 9º)."),
 ("ORGANIZAÇÃO","Qual lei instituiu o SUSP?","Lei nº 13.675/2018.")]
def fcpage(items, first):
    cs = "".join(f'<div class="c"><div class="f"><small>{a}</small>{q}</div><div class="b">{r}</div></div>' for a,q,r in items)
    h = ('<div class="marker">§§R2§§</div><div class="unit"><span class="u">REVISÃO ATIVA</span></div><h1 class="big">Flash<span class="hl">cards</span></h1><p class="lead">Cubra a resposta, tente lembrar e confira. Revise em 1, 3, 7, 15 e 30 dias.</p>' if first else '')
    return h + f'<div class="fc">{cs}</div>'
add(fcpage(FC[:12], True)); add(fcpage(FC[12:], False))

Q = [
 ("Conceito","Nos termos do art. 144 da Constituição, a segurança pública é:",
  ["dever de todos e responsabilidade exclusiva do Estado.","dever do Estado, direito e responsabilidade de todos.","direito do Estado e dever dos cidadãos.","responsabilidade exclusiva das polícias estaduais.","dever da União e dos Estados, apenas."],"B",
  "Texto literal do caput: dever do Estado, direito e responsabilidade de todos.","Dever: Estado. Direito e responsabilidade: todos."),
 ("Rol","NÃO está entre os órgãos de segurança pública previstos nos incisos do art. 144:",
  ["polícia ferroviária federal.","polícias penais federal, estaduais e distrital.","corpos de bombeiros militares.","guardas municipais.","polícia rodoviária federal."],"D",
  "As guardas municipais estão no § 8º, e não nos incisos I a VI. As demais alternativas estão nos incisos III, VI, V e II.","Guardas: § 8º."),
 ("PF","Compete à Polícia Federal, com exclusividade:",
  ["prevenir e reprimir o tráfico ilícito de entorpecentes.","exercer as funções de polícia judiciária da União.","o patrulhamento ostensivo das rodovias federais.","a preservação da ordem pública nos Estados.","a execução de atividades de defesa civil."],"B",
  "Art. 144, § 1º, IV. O combate ao tráfico é “sem prejuízo” de outros órgãos; o patrulhamento das rodovias é da PRF; a ordem pública, da PM; a defesa civil, dos Bombeiros.","PF: polícia judiciária da União, com exclusividade."),
 ("PF","Um roubo foi praticado contra uma agência de empresa pública federal. Nos termos do art. 144, a apuração da infração cabe, em regra, à:",
  ["Polícia Militar.","Polícia Civil.","Polícia Federal.","Guarda Municipal.","Polícia Rodoviária Federal."],"C",
  "A PF apura infrações em detrimento de bens, serviços e interesses da União, de suas autarquias e empresas públicas (§ 1º, I).","Empresa pública federal → PF."),
 ("PF","Um furto foi praticado contra uma agência de sociedade de economia mista federal. Considerando a literalidade do art. 144, § 1º, I:",
  ["a apuração cabe à Polícia Federal, pois toda entidade federal está abrangida.","as sociedades de economia mista não estão mencionadas no § 1º, I, e a apuração, em regra, cabe à Polícia Civil.","a apuração cabe à Polícia Rodoviária Federal.","a apuração cabe à Guarda Municipal.","o fato não é crime."],"B",
  "O § 1º, I, menciona a União, suas autarquias e empresas públicas, sem citar sociedades de economia mista. Em regra, a apuração cabe à Polícia Civil, ressalvadas outras hipóteses de competência federal.","Sociedade de economia mista: fora do § 1º, I."),
 ("PF","Exercer as funções de polícia marítima, aeroportuária e de fronteiras cabe:",
  ["à Polícia Rodoviária Federal.","às Polícias Militares.","à Polícia Federal.","às Forças Armadas, com exclusividade.","às Polícias Civis."],"C",
  "Art. 144, § 1º, III.","Portos, aeroportos e fronteiras → PF."),
 ("PRF","A Polícia Rodoviária Federal destina-se, na forma da lei:",
  ["à apuração das infrações penais cometidas nas rodovias.","ao patrulhamento ostensivo das rodovias federais.","ao patrulhamento ostensivo das rodovias estaduais e federais.","às funções de polícia judiciária da União.","à segurança dos estabelecimentos penais federais."],"B",
  "Art. 144, § 2º. A PRF não exerce polícia judiciária e atua nas rodovias federais.","PRF: patrulhamento ostensivo de rodovias federais."),
 ("PFF","Sobre a Polícia Ferroviária Federal, é correto afirmar que:",
  ["não tem previsão constitucional.","destina-se, na forma da lei, ao patrulhamento ostensivo das ferrovias federais.","é mantida pelos Estados.","exerce polícia judiciária nas ferrovias.","integra as Forças Armadas."],"B",
  "Art. 144, inciso III e § 3º. É órgão permanente, organizado e mantido pela União.","PFF: ferrovias federais."),
 ("Civil","Às polícias civis incumbem, ressalvada a competência da União:",
  ["a polícia ostensiva e a preservação da ordem pública.","as funções de polícia judiciária e a apuração de infrações penais, exceto as militares.","as funções de polícia judiciária, inclusive quanto aos crimes militares.","o patrulhamento das rodovias estaduais.","a segurança dos estabelecimentos penais."],"B",
  "Art. 144, § 4º. As polícias civis são dirigidas por delegados de polícia de carreira.","Civil: judiciária, exceto militares."),
 ("PM","Às polícias militares cabem:",
  ["a polícia judiciária e a apuração de infrações penais.","a polícia ostensiva e a preservação da ordem pública.","as atividades de defesa civil, com exclusividade.","a segurança dos estabelecimentos penais.","as funções de polícia de fronteiras."],"B",
  "Art. 144, § 5º, primeira parte.","PM: ostensiva + ordem pública."),
 ("Subordinação","As polícias militares e os corpos de bombeiros militares:",
  ["subordinam-se ao Comandante do Exército.","são forças auxiliares e reserva do Exército e subordinam-se aos Governadores.","subordinam-se ao Ministro da Justiça.","são órgãos da União.","subordinam-se aos Prefeitos."],"B",
  "Art. 144, § 6º. Ser reserva do Exército não significa subordinação ao Exército.","Reserva do Exército; subordinação ao Governador."),
 ("CBM","Aos corpos de bombeiros militares, além das atribuições definidas em lei, incumbe:",
  ["a preservação da ordem pública.","a execução de atividades de defesa civil.","a polícia judiciária.","o patrulhamento ostensivo das rodovias.","a proteção dos bens municipais."],"B",
  "Art. 144, § 5º, segunda parte.","CBM: defesa civil."),
 ("Penal","Sobre as polícias penais, é correto afirmar que:",
  ["foram criadas pela Constituição originária de 1988.","existem nas esferas federal, estadual, distrital e municipal.","cabe-lhes a segurança dos estabelecimentos penais, vinculadas ao órgão administrador do sistema penal da unidade federativa a que pertencem.","subordinam-se ao Poder Judiciário.","exercem polícia judiciária."],"C",
  "Art. 144, § 5º-A, incluído pela EC nº 104/2019. Não há polícia penal municipal.","Polícia Penal: estabelecimentos penais; EC nº 104/2019."),
 ("DF","Sobre as polícias civil e militar e o corpo de bombeiros militar do Distrito Federal:",
  ["são organizados e mantidos pelo DF e subordinados ao Presidente da República.","são organizados e mantidos pela União e subordinados ao Governador do DF.","são órgãos municipais.","subordinam-se ao Ministro da Defesa.","não integram a segurança pública."],"B",
  "Art. 21, XIV (organização e manutenção pela União) e art. 144, § 6º (subordinação ao Governador do DF).","DF: mantidos pela União; subordinados ao Governador."),
 ("Guardas","Nos termos do art. 144, § 8º, da Constituição:",
  ["os Municípios deverão constituir guardas municipais.","os Municípios poderão constituir guardas municipais destinadas à proteção de seus bens, serviços e instalações, conforme dispuser a lei.","as guardas municipais exercem polícia judiciária.","as guardas municipais são forças auxiliares do Exército.","as guardas municipais estão subordinadas ao Governador."],"B",
  "Texto literal do § 8º. A criação é facultativa; as guardas não exercem polícia judiciária, não são reserva do Exército e se vinculam ao Município.","§ 8º: “poderão”."),
 ("Guardas","Segundo a tese fixada pelo STF no Tema 656 (RE 608.588), as guardas municipais:",
  ["podem instaurar inquéritos policiais.","podem exercer ações de segurança urbana, inclusive policiamento ostensivo comunitário, respeitadas as atribuições dos demais órgãos e excluída a polícia judiciária.","só podem vigiar prédios públicos.","substituem a Polícia Militar no policiamento ostensivo.","não estão sujeitas a controle externo."],"B",
  "A tese admite segurança urbana e policiamento ostensivo comunitário, com respeito às atribuições dos demais órgãos, sem polícia judiciária e com controle externo pelo Ministério Público.","Tema 656: comunitário, sem polícia judiciária."),
 ("Guardas","O Estatuto Geral das Guardas Municipais (Lei nº 13.022/2014) define as guardas como instituições de caráter:",
  ["militar.","civil.","paramilitar.","judiciário.","privado."],"B",
  "A lei define as guardas como instituições de caráter civil, uniformizadas e armadas conforme a lei.","Guarda Municipal: caráter civil."),
 ("Viária","A segurança viária, nos termos do art. 144, § 10:",
  ["compete exclusivamente à Polícia Rodoviária Federal.","compreende a educação, a engenharia e a fiscalização de trânsito, competindo, nos Estados, DF e Municípios, aos órgãos executivos de trânsito e seus agentes.","foi prevista no texto originário de 1988.","compete às Forças Armadas.","integra as funções da polícia judiciária."],"B",
  "Art. 144, § 10, incluído pela EC nº 82/2014.","Viária: educação, engenharia, fiscalização."),
 ("Cenário","Durante a madrugada, um assalto está em andamento numa farmácia. O órgão com atribuição constitucional para a pronta atuação ostensiva é a:",
  ["Polícia Civil.","Polícia Militar.","Polícia Federal.","Polícia Penal.","Polícia Ferroviária Federal."],"B",
  "A PM exerce polícia ostensiva e preservação da ordem pública. A investigação posterior cabe à Polícia Civil.","Crime em andamento → PM."),
 ("Cenário","Após a prisão em flagrante do assaltante, a investigação de um roubo comum praticado contra um particular cabe, em regra, à:",
  ["Polícia Militar.","Polícia Civil.","Polícia Federal.","Guarda Municipal.","Polícia Rodoviária Federal."],"B",
  "A apuração de infrações comuns, sem interesse da União, cabe à Polícia Civil (§ 4º).","Investigação comum → Polícia Civil."),
 ("Distinção","Assinale a alternativa que associa corretamente o órgão à natureza predominante de sua atividade.",
  ["Polícia Civil: polícia ostensiva.","Polícia Militar: polícia judiciária.","Polícia Rodoviária Federal: patrulhamento ostensivo.","Polícia Federal: apenas polícia ostensiva.","Guarda Municipal: polícia judiciária."],"C",
  "A PRF faz patrulhamento ostensivo (§ 2º). A Civil é judiciária; a PM é ostensiva; a PF exerce polícia judiciária da União e outras funções; a guarda não exerce polícia judiciária.","Ostensiva x judiciária."),
 ("Organização","A remuneração dos servidores policiais integrantes dos órgãos do art. 144 será fixada:",
  ["livremente por decreto do Governador.","na forma do art. 39, § 4º, ou seja, por subsídio.","por convenção coletiva.","em percentual da arrecadação de multas.","pelo Poder Judiciário."],"B",
  "Art. 144, § 9º: remuneração na forma do art. 39, § 4º (subsídio em parcela única).","§ 9º: subsídio."),
 ("Organização","Sobre a organização da segurança pública, é correto afirmar que:",
  ["as Forças Armadas integram o rol do art. 144.","a Força Nacional de Segurança Pública está prevista no art. 144.","a lei disciplinará a organização e o funcionamento dos órgãos responsáveis pela segurança pública, de maneira a garantir a eficiência de suas atividades.","as empresas de segurança privada são órgãos de segurança pública.","os Municípios podem criar polícias penais."],"C",
  "Art. 144, § 7º. Forças Armadas, Força Nacional e segurança privada não estão no rol; não há polícia penal municipal.","§ 7º: lei, eficiência."),
 ("Atualização","Sobre a PEC da Segurança Pública (PEC 18/2025), na data desta edição (25/11/2026), é correto afirmar que:",
  ["já está em vigor como emenda constitucional e revogou o § 8º do art. 144.","foi aprovada pela Câmara e pelo Senado, mas ainda não havia sido promulgada, de modo que continua valendo o texto atual do art. 144.","foi rejeitada pelo Senado.","dispensa promulgação, por ter sido aprovada em dois turnos.","depende de sanção do Presidente da República."],"B",
  "Emendas constitucionais são promulgadas pelas Mesas da Câmara e do Senado (art. 60, § 3º), sem sanção presidencial. Até a promulgação, vale o texto vigente.","PEC aprovada ≠ emenda em vigor.")]

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
def tr_block(lst):
    out = ""
    for n, itens in lst:
        rows = "".join(f'<tr><td style="width:7%;text-align:center;font-weight:900">{i+1}</td><td style="width:12%;text-align:center" class="{"yes" if r=="C" else "no"}">{"CERTO" if r=="C" else "ERRADO"}</td><td>{c}</td></tr>' for i,(_,r,c) in enumerate(itens))
        out += f'<h3>Treino rápido · Unidade {n}</h3><table><tr><th>#</th><th>Resposta</th><th>Comentário</th></tr>{rows}</table>'
    return out
add('<div class="unit"><span class="u">CORREÇÃO</span><span class="t">Treinos rápidos</span></div><h1 class="big">Respostas dos <span class="hl">treinos</span></h1><p class="lead">Certo ou errado das Unidades 1 a 5.</p>' + tr_block(TREINOS[:2]))
add(tr_block(TREINOS[2:4])); add(tr_block(TREINOS[4:]))

add(f'''<div class="unit"><span class="u">ENCERRAMENTO</span></div><h1 class="big">Referências e <span class="hl">verificação</span></h1><p class="lead">De onde vieram as informações.</p>
<h3>Legislação consultada</h3>
<ul>
<li>BRASIL. <strong>Constituição Federal de 1988</strong>: art. 144 (caput, incisos I a VI e §§ 1º a 10), conferido no texto compilado do Planalto; arts. 21, XIV, e 22, XXI. Citados também os arts. 5º, 6º, 39, § 4º, 60, § 3º, e 142.</li>
<li>Emendas Constitucionais nº 19/1998, nº 82/2014 e nº 104/2019.</li>
<li><strong>Lei nº 13.022/2014</strong> (Estatuto Geral das Guardas Municipais) · <strong>Lei nº 13.675/2018</strong> (SUSP) · Código de Processo Penal, art. 301.</li>
<li>PEC nº 18/2025 (PEC da Segurança Pública): tramitação no Senado Federal e na Câmara dos Deputados e notícias oficiais da Agência Senado.</li>
</ul>
<h3>Jurisprudência citada</h3>
<ul><li>STF, ADPF 995 (2023): guardas municipais integram o Sistema de Segurança Pública.</li><li>STF, RE 608.588, Tema 656 (2025): ações de segurança urbana e policiamento ostensivo comunitário pelas guardas municipais.</li></ul>''' + lembre("{{VERIF}}", "Verificação e limitações"))
add('''<div class="ending"><h2>Fim do Caderno 04</h2><p style="text-align:center">Próximo caderno da coleção: <strong>Organização dos Poderes (arts. 44 a 135)</strong>.</p>
<p class="note" style="text-align:center">Mapa da Aprovação · Caderno Simplificado · Direito Constitucional · Caderno 04 · 1ª edição · novembro de 2026<br>Material de estudo independente. Não substitui a leitura da Constituição e do edital do seu concurso.</p></div>''')

PEC_HTML = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "pec.html")).read() if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "pec.html")) else "<p>(pendente)</p>"
VERIF = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "verificacao.html")).read() if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "verificacao.html")) else "<p>(pendente)</p>"
doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Caderno Simplificado — Direito Constitucional — Caderno 04</title>
<link rel="stylesheet" href="estilo.css"></head><body>{symbols()}{"".join(P)}</body></html>'''
doc = doc.replace("{{PEC2}}", PEC_HTML.split("<!--SPLIT-->")[1] if "<!--SPLIT-->" in PEC_HTML else "").replace("{{PEC}}", PEC_HTML.split("<!--SPLIT-->")[0]).replace("{{VERIF}}", VERIF)
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "miolo.html"), "w").write(doc)
print("páginas planejadas:", len(P))
