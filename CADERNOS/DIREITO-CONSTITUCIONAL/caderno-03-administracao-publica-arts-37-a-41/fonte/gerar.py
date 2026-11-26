"""Gera miolo.html do Caderno 03 de Direito Constitucional (arts. 37 a 41). Uso: python3 gerar.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from componentes import *

DATA = "25 de novembro de 2026"
P = []
def add(html, first=False): P.append(page(f'<div class="marker">§§P{len(P)+1:03d}§§</div>' + html, first))
U1, U2, U3, U4 = "UNIDADE 1", "UNIDADE 2", "UNIDADE 3", "UNIDADE 4"
T1, T2, T3, T4 = "Administração Pública", "Princípios (LIMPE)", "Acesso, cargos e acumulação", "Servidores e responsabilidade"
def cf(x): return f"{x} · Constituição Federal"
def p(t): return f"<p>{t}</p>"
def colors(*keys):
    m = {"b":(C['blue'],C['sky']),"g":(C['green'],C['greensoft']),"o":(C['golddeep'],C['goldsoft']),"r":(C['red'],C['redsoft']),"n":(C['navy'],'#e3e9f3')}
    return [m[k] for k in keys]

# =========================================================== APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">A Administração Pública explicada com situações de repartição, concurso e serviço público.</p>
<p>Este é o <strong>Caderno 03 da coleção de Direito Constitucional</strong>. Ele trata do Capítulo VII do Título III da Constituição, “Da Administração Pública”, nos <strong>arts. 37 a 41</strong>: princípios, concurso, cargos, acumulação, servidores, estabilidade e responsabilidade.</p>
<p>Esse tema aparece tanto em <strong>Direito Constitucional</strong> quanto em <strong>Direito Administrativo</strong>, e é a base para quem vai <strong>ser servidor público</strong>: guardas municipais, policiais, técnicos e analistas. Em geral, cada assunto ocupa <strong>duas páginas</strong>:</p>
{cards([("book","Página 1 · Entenda","Título, texto da lei, <b>Traduzindo o juridiquês</b> e a faixa <b>Memorize</b>.", C['golddeep']),
        ("bulb","Página 2 · Pratique","<b>Entenda na prática</b> com uma situação administrativa, exemplo e <b>Pegadinha de concurso</b>.", C['blue'])],2)}
<h3>Recursos especiais deste caderno</h3>
{table(["Recurso","Onde está"],[
 ["“Qual princípio foi violado?”: 8 situações para treinar","Unidade 2"],
 ["Fluxo “posso acumular estes cargos?”","Unidade 3"],
 ["Linha do tempo da validade do concurso","Unidade 3"],
 ["Esquema da reintegração, recondução e disponibilidade","Unidade 4"],
 ["Treino rápido Certo ou Errado em cada unidade","Fim de cada unidade, com respostas no gabarito"],
 ["24 questões autorais comentadas","Prática final"]],["56%",None])}
{lembre(f'''<p><strong>Material pesquisado e atualizado em: {DATA}.</strong> Os dispositivos dos arts. 37 a 41 citados foram conferidos no texto compilado da Constituição no Planalto, <strong>incluindo a EC nº 138/2025</strong>, que mudou as regras de acumulação de cargos, assim como a Lei nº 9.784/1999 (art. 2º), o Decreto-Lei nº 200/1967 (art. 4º) e a LC nº 152/2015. As questões são <strong>autorais</strong>. As limitações da verificação estão nas Referências.</p>''', "Fontes e atualização")}''', first=True)

TOC = [("u","UNIDADE 1 · ADMINISTRAÇÃO PÚBLICA","U1"),
 ("","1. Conceito de Administração Pública","A01"),("","2. Administração direta e indireta","A02"),
 ("u","UNIDADE 2 · PRINCÍPIOS DA ADMINISTRAÇÃO (LIMPE)","U2"),
 ("","3. Visão geral: LIMPE","A03"),("","4. Legalidade","A04"),("","5. Impessoalidade","A05"),("","6. Moralidade","A06"),
 ("","7. Publicidade","A07"),("","8. Eficiência","A08"),("","9. Princípios implícitos","A09"),("","10. Qual princípio foi violado?","A10"),
 ("u","UNIDADE 3 · ACESSO, CARGOS E ACUMULAÇÃO","U3"),
 ("","11. Acesso aos cargos e concurso público","A11"),("","12. Validade do concurso e direito à nomeação","A12"),("","13. Exceções ao concurso","A13"),
 ("","14. Cargos, empregos e funções","A14"),("","15. Cargo em comissão x função de confiança","A15"),("","16. Acumulação de cargos","A16"),
 ("u","UNIDADE 4 · SERVIDORES E RESPONSABILIDADE","U4"),
 ("","17. Sindicalização, greve, PcD e temporários","A17"),("","18. Remuneração e teto","A18"),("","19. Servidor com mandato eletivo (art. 38)","A19"),
 ("","20. Arts. 39 e 40: direitos e aposentadoria (noções)","A20"),("","21. Estabilidade (art. 41)","A21"),("","22. Perda do cargo e reintegração","A22"),
 ("","23. Responsabilidade do Estado e dos agentes","A23"),
 ("u","REVISÃO E PRÁTICA","RV"),
 ("","Mapa conceitual · Confusões mais comuns","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),("","Gabarito, respostas dos treinos e referências","R4")]
toc = "".join(f'<li class="u"><span class="t">{t}</span><span class="p" data-pg="{m}"></span></li>' if k=="u"
              else f'<li><span class="t">{t}</span><span class="p" data-pg="{m}"></span></li>' for k,t,m in TOC)
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
<table><tr><th>#</th><th>Afirmação</th><th style="text-align:center">Sua resposta</th></tr>{rows}</table>''' +
    memo('Errou? Volte à página do assunto e releia a faixa <strong>Memorize</strong> e a <strong>Pegadinha</strong>.', "Dica:"))

# =========================================================== UNIDADE 1
opener("01","UNIDADE 1","Administração Pública",["Conceito de Administração Pública","Administração direta e indireta"],"U1")

add(head(U1,T1,'O que é Administração <span class="hl">Pública</span>?','Quem administra e o que é administrar.', "A01") +
 oque(p('<strong>Administração Pública</strong> é o conjunto de <strong>entidades, órgãos e agentes</strong> que executam as atividades do Estado voltadas ao <strong>interesse público</strong>, e também a própria <strong>atividade</strong> de administrar: prestar serviços, fiscalizar, fomentar e intervir.')) +
 cards([("sitemap","Sentido SUBJETIVO (orgânico ou formal)","<b>Quem</b> administra: entidades, órgãos e agentes públicos. Costuma ser escrito com iniciais maiúsculas: <b>Administração Pública</b>.",C['blue']),
        ("briefcase","Sentido OBJETIVO (material ou funcional)","<b>O que</b> se faz: a atividade administrativa. Costuma ser escrito com minúsculas: <b>administração pública</b>.",C['golddeep'])],2) +
 traduz(p('Imagine a prefeitura da sua cidade. As <strong>pessoas e repartições</strong> que trabalham lá (secretarias, servidores, guardas) são a Administração no sentido <strong>subjetivo</strong>. O <strong>trabalho</strong> que elas fazem (recolher o lixo, fiscalizar o comércio, manter a creche) é a administração no sentido <strong>objetivo</strong>.')) +
 memo('Subjetivo = <strong>QUEM</strong> (entidades, órgãos, agentes). Objetivo = <strong>O QUÊ</strong> (atividade: serviço público, polícia administrativa, fomento, intervenção).'))

add(pratica_title("As 4 atividades administrativas") +
 flow([("bulb",["SERVIÇO","PÚBLICO","coleta de lixo,","transporte"]),("shield",["POLÍCIA","ADMINISTRATIVA","fiscalizar e","limitar atividades"]),("coin",["FOMENTO","incentivar","o particular"]),("gavel",["INTERVENÇÃO","na propriedade","e na economia"])],
      "O sentido objetivo da Administração: o que ela faz no dia a dia.", colors=colors("b","r","g","o")) +
 ex(p('A fiscal da vigilância sanitária interdita um restaurante com a cozinha em condições irregulares: <b>polícia administrativa</b>. A prefeitura concede bolsas para atletas locais: <b>fomento</b>. O ônibus municipal circulando: <b>serviço público</b>. O tombamento de um casarão histórico: <b>intervenção na propriedade</b>.')) +
 pega('<ul><li>“Administração Pública” (maiúsculas) costuma indicar o sentido <b>subjetivo</b>; “administração pública” (minúsculas), o sentido <b>objetivo</b>. É uma convenção da doutrina, cobrada em provas mais detalhistas.</li><li>Polícia <b>administrativa</b> (fiscaliza atividades e bens, como a vigilância sanitária) ≠ polícia <b>judiciária</b> (apura crimes, como a Polícia Civil).</li><li>O art. 37 vale para a Administração <b>direta e indireta</b> de <b>todos os Poderes</b> e de <b>todos os entes</b>.</li></ul>') +
 kw(["sentido subjetivo","sentido objetivo","serviço público","polícia administrativa","fomento","intervenção"]))

estrutura = f'''<figure><svg viewBox="0 0 640 250" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<rect x="230" y="8" width="180" height="44" rx="12" fill="{C['navy']}"/><text x="320" y="35" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">ENTE FEDERATIVO</text>
<path d="M320 52 V70 M160 70 H480 M160 70 V86 M480 70 V86" stroke="{C['ink']}" stroke-width="2.5" fill="none"/>
<rect x="20" y="86" width="280" height="156" rx="14" fill="{C['sky']}" stroke="{C['blue']}" stroke-width="2.5"/>
<text x="160" y="112" text-anchor="middle" font-weight="900" font-size="15" fill="{C['blue']}">ADMINISTRAÇÃO DIRETA</text>
<text x="160" y="132" text-anchor="middle" font-size="11.5" fill="{C['ink']}">o próprio ente, por seus ÓRGÃOS</text>
<text x="160" y="148" text-anchor="middle" font-size="11.5" fill="{C['ink']}">(sem personalidade jurídica própria)</text>
''' + "".join(f'<rect x="{x}" y="164" width="120" height="30" rx="8" fill="#fff" stroke="{C["blue"]}"/><text x="{x+60}" y="184" text-anchor="middle" font-size="11" font-weight="700" fill="{C["ink"]}">{t}</text>' for x,t in [(36,"Ministérios"),(164,"Secretarias"),(36,"")][:2]) + f'''
<rect x="100" y="200" width="120" height="30" rx="8" fill="#fff" stroke="{C['blue']}"/><text x="160" y="220" text-anchor="middle" font-size="11" font-weight="700" fill="{C['ink']}">Guarda Municipal*</text>
<rect x="340" y="86" width="280" height="156" rx="14" fill="{C['greensoft']}" stroke="{C['green']}" stroke-width="2.5"/>
<text x="480" y="112" text-anchor="middle" font-weight="900" font-size="15" fill="{C['green']}">ADMINISTRAÇÃO INDIRETA</text>
<text x="480" y="132" text-anchor="middle" font-size="11.5" fill="{C['ink']}">ENTIDADES com personalidade</text>
<text x="480" y="148" text-anchor="middle" font-size="11.5" fill="{C['ink']}">jurídica própria</text>
''' + "".join(f'<rect x="{x}" y="{y}" width="124" height="30" rx="8" fill="#fff" stroke="{C["green"]}"/><text x="{x+62}" y="{y+20}" text-anchor="middle" font-size="11" font-weight="700" fill="{C["ink"]}">{t}</text>' for x,y,t in [(352,164,"Autarquias"),(484,164,"Fundações públicas"),(352,200,"Empresas públicas"),(484,200,"Soc. economia mista")]) + f'''
</svg><figcaption>* Quando organizada como órgão da prefeitura, o que é o caso mais comum. Mnemônico da indireta: <b>FAES</b> (Fundações, Autarquias, Empresas públicas, Sociedades de economia mista).</figcaption></figure>'''
add(head(U1,T1,'Administração direta e <span class="hl">indireta</span>','Nível introdutório: quem compõe cada uma.', "A02") + estrutura +
 traduz(p('A <strong>direta</strong> é o próprio ente (União, Estado, DF ou Município) atuando por meio dos seus <strong>órgãos</strong>, que são “departamentos” sem personalidade jurídica. A <strong>indireta</strong> é formada por <strong>entidades criadas pelo ente</strong>, com personalidade jurídica própria, para cuidar de uma tarefa específica. Exemplos: o INSS (autarquia), a Caixa (empresa pública) e o Banco do Brasil (sociedade de economia mista).')) +
 lei(cf("Art. 37, XIX"),'<p>XIX - somente por lei específica poderá ser criada autarquia e autorizada a instituição de empresa pública, de sociedade de economia mista e de fundação, cabendo à lei complementar, neste último caso, definir as áreas de sua atuação;</p>') +
 memo('Autarquia: <strong>criada</strong> por lei específica. Empresa pública, sociedade de economia mista e fundação: lei específica <strong>autoriza</strong> a criação.'))

add(pratica_title("Desconcentração x descentralização") +
 table(["","DESCONCENTRAÇÃO","DESCENTRALIZAÇÃO"],[
  ["O que é","Distribuição de tarefas <b>dentro</b> da mesma pessoa jurídica","Transferência de tarefas para <b>outra</b> pessoa jurídica"],
  ["Cria","<b>Órgãos</b> (sem personalidade)","<b>Entidades</b> (com personalidade) ou delegação a particulares"],
  ["Hierarquia","Sim","Não: há <b>controle</b> (tutela ou supervisão)"],
  ["Exemplo","Prefeitura cria a Secretaria de Segurança","Estado cria uma autarquia de trânsito"]],["18%",None,None]) +
 flow([("capitol",["ENTE","FEDERATIVO"]),("sitemap",["DESCONCENTRA","cria órgãos","internos"]),("link",["DESCENTRALIZA","cria entidades","(FAES)"])],
      "Dois caminhos para dividir o trabalho administrativo.", colors=colors("n","b","g")) +
 pega('<ul><li><b>Órgão não tem personalidade jurídica</b> (ex.: Ministério, Secretaria). <b>Entidade tem</b> (ex.: autarquia).</li><li>Autarquia é <b>criada</b> por lei; empresas públicas e sociedades de economia mista têm a criação <b>autorizada</b> por lei. A prova troca os verbos!</li><li>Entre o ente e a entidade da indireta <b>não há hierarquia</b>, mas sim controle finalístico (supervisão ministerial).</li></ul>') +
 kw(["órgão","entidade","FAES","criada x autorizada","desconcentração","descentralização"]))

treino(1, [
 ("No sentido objetivo, Administração Pública designa o conjunto de entidades, órgãos e agentes públicos.","E","Esse é o sentido subjetivo; o objetivo é a atividade administrativa."),
 ("A administração indireta é composta por autarquias, fundações públicas, empresas públicas e sociedades de economia mista.","C","Mnemônico FAES."),
 ("Os órgãos públicos possuem personalidade jurídica própria.","E","Órgãos não têm personalidade jurídica; entidades têm."),
 ("Somente por lei específica poderá ser criada autarquia.","C","Art. 37, XIX."),
 ("A criação de um órgão dentro da mesma pessoa jurídica é exemplo de descentralização.","E","É desconcentração."),
 ("Os princípios do art. 37 aplicam-se apenas ao Poder Executivo.","E","Aplicam-se à administração direta e indireta de qualquer dos Poderes.")])

# =========================================================== UNIDADE 2
opener("02","UNIDADE 2","Princípios da Administração (LIMPE)",["Visão geral: LIMPE","Legalidade","Impessoalidade","Moralidade","Publicidade","Eficiência","Princípios implícitos","Qual princípio foi violado?"],"U2")

ART37 = '<p>Art. 37. A administração pública direta e indireta de qualquer dos Poderes da União, dos Estados, do Distrito Federal e dos Municípios obedecerá aos princípios de legalidade, impessoalidade, moralidade, publicidade e eficiência e, também, ao seguinte:</p>'
add(head(U2,T2,'Os princípios <span class="hl">LIMPE</span>','Os cinco princípios expressos no caput do art. 37.', "A03") +
 lei(cf("Art. 37, caput"), ART37, "Redação dada pela EC nº 19/1998, que incluiu a eficiência.") +
 cards([("#L","Legalidade","Só faz o que a lei permite."),("#I","Impessoalidade","Interesse público, sem favorecer ou perseguir."),("#M","Moralidade","Ética, honestidade e boa-fé."),
        ("#P","Publicidade","Transparência dos atos."),("#E","Eficiência","Bons resultados, com rapidez e economia.")],5) +
 traduz(p('Os princípios são as <strong>regras de ouro</strong> de quem trabalha no serviço público. Valem para todos: do Presidente da República ao servidor do balcão, da Câmara Municipal à empresa pública. O mnemônico <strong>LIMPE</strong> lembra que a Administração deve ser… “limpa”.')) +
 memo('<b>LIMPE</b> → <strong>L</strong>egalidade, <strong>I</strong>mpessoalidade, <strong>M</strong>oralidade, <strong>P</strong>ublicidade, <strong>E</strong>ficiência. A <strong>eficiência</strong> foi a última a entrar, com a <strong>EC nº 19/1998</strong>.', "Mnemônico:"))

add(pratica_title() +
 flow([("book",["LEGALIDADE","dentro da lei"]),("people",["IMPESSOALIDADE","para todos,","sem favoritismo"]),("heart",["MORALIDADE","com ética"]),("eye",["PUBLICIDADE","às claras"]),("chart",["EFICIÊNCIA","com bons","resultados"])],
      "Um ícone para cada princípio: associe a imagem à palavra.", colors=colors("n","b","r","o","g")) +
 ex(p('Uma prefeitura precisa comprar merenda escolar. A compra deve estar prevista em lei e seguir a licitação (<b>legalidade</b>), sem direcionar para a empresa do amigo do prefeito (<b>impessoalidade</b>), com honestidade nos preços (<b>moralidade</b>), com o contrato publicado no portal da transparência (<b>publicidade</b>) e entregando merenda de qualidade, no prazo e pelo melhor preço (<b>eficiência</b>).')) +
 pega('<ul><li>Os princípios <b>expressos</b> no caput do art. 37 são só os cinco do LIMPE. Razoabilidade, proporcionalidade, supremacia do interesse público, motivação e autotutela são princípios <b>implícitos</b> (ou estão em leis, como a Lei nº 9.784/1999).</li><li>Os princípios valem para a administração <b>direta e indireta</b>, inclusive empresas públicas e sociedades de economia mista.</li><li>A eficiência <b>não</b> estava no texto original de 1988.</li></ul>') +
 kw(["LIMPE","princípios expressos","princípios implícitos","EC nº 19/1998","direta e indireta","qualquer dos Poderes"]))

add(head(U2,T2,'Princípio da <span class="hl">legalidade</span>','O servidor só pode fazer o que a lei autoriza.', "A04") +
 oque(p('Na Administração Pública, <strong>legalidade</strong> significa que o agente público só pode agir quando e como a <strong>lei autoriza</strong>. Não basta a lei não proibir: é preciso que ela <strong>permita</strong>.')) +
 table(["","PARTICULAR","ADMINISTRAÇÃO PÚBLICA"],[["Regra","Pode tudo o que a lei <b>não proíbe</b> (art. 5º, II)","Só pode o que a lei <b>permite</b> (art. 37)"],["Base","Autonomia da vontade","Subordinação à lei"],["Exemplo","Abrir a loja às 6h, se a lei local não proibir","Conceder um auxílio apenas se houver lei prevendo"]],["18%",None,None]) +
 traduz(p('Para você, cidadão, a lei funciona como uma <strong>cerca</strong>: dentro dela, tudo é permitido. Para o servidor, a lei funciona como um <strong>trilho</strong>: ele só pode andar por onde o trilho passa. Se não há trilho, não há caminho.')) +
 memo('Particular: <strong>tudo o que a lei não proíbe</strong>. Administração: <strong>somente o que a lei permite</strong>.'))

add(pratica_title() +
 flow([("person",["DIRETORA","DE ESCOLA","pública"]),("coin",["COBRA TAXA","de matrícula","sem lei"]),("xmark",["VIOLA A","LEGALIDADE"])],
      "Sem lei autorizando, o agente público não pode agir.", colors=colors("b","o","r")) +
 ex(p('A diretora de uma escola municipal decide cobrar R$ 50 de “taxa de matrícula” para comprar material. Mesmo com boa intenção, ela <b>não pode</b>: não há lei autorizando, e a Constituição garante a gratuidade do ensino público em estabelecimentos oficiais (art. 206, IV). Outro exemplo: um servidor não pode tirar 40 dias de férias por conta própria se a lei do seu cargo prevê 30.')) +
 pega('<ul><li>Legalidade administrativa ≠ legalidade do particular. É a confusão mais cobrada no tema.</li><li>A Administração pode agir com <b>discricionariedade</b> (escolher entre opções), mas sempre <b>dentro dos limites da lei</b>.</li><li>Decretos e portarias <b>regulamentam</b> a lei: não podem criar obrigações que a lei não previu.</li></ul>') +
 kw(["só o que a lei permite","subordinação à lei","discricionariedade nos limites da lei","decreto regulamentar"]))

add(head(U2,T2,'Princípio da <span class="hl">impessoalidade</span>','A Administração age para todos, sem favorecer nem perseguir ninguém.', "A05") +
 cards([("target","Finalidade pública","Todo ato deve buscar o <b>interesse público</b>, e não interesses pessoais.",C['blue']),
        ("people","Igualdade de tratamento","Ninguém pode ser favorecido ou perseguido. Ex.: concurso e licitação.",C['green']),
        ("capitol","Vedação de promoção pessoal","O ato é do <b>órgão</b>, não do agente: obra não é “do prefeito”.",C['red'])],3) +
 lei(cf("Art. 37, § 1º"),'<p>§ 1º A publicidade dos atos, programas, obras, serviços e campanhas dos órgãos públicos deverá ter caráter educativo, informativo ou de orientação social, dela não podendo constar nomes, símbolos ou imagens que caracterizem promoção pessoal de autoridades ou servidores públicos.</p>') +
 traduz(p('O servidor atua <strong>em nome do órgão</strong>, e não em nome próprio. Por isso uma obra é “da Prefeitura”, e não “do prefeito Fulano”. E por isso existem concursos e licitações: para que <strong>qualquer pessoa</strong> tenha a mesma chance, sem apadrinhamento.')) +
 memo('Impessoalidade = <strong>finalidade pública</strong> + <strong>tratamento igual</strong> + <strong>proibição de promoção pessoal</strong> (art. 37, § 1º).'))

add(pratica_title() +
 flow([("city",["OBRA","PÚBLICA","nova praça"]),("flag",["PLACA","“Obra do prefeito”","+ foto e slogan"]),("xmark",["PROMOÇÃO","PESSOAL","proibida (§ 1º)"]),("check",["CORRETO","“Prefeitura de...”","caráter informativo"])],
      "A publicidade oficial informa; não faz propaganda do governante.", colors=colors("b","o","r","g")) +
 ex(p('Um prefeito manda pintar todos os prédios públicos com a cor do seu partido e coloca o slogan da campanha nas placas das obras. Isso viola a <b>impessoalidade</b> (art. 37, § 1º). Outro exemplo: um fiscal que só multa os comerciantes adversários políticos do prefeito usa o cargo para <b>perseguir</b>, desviando-se da finalidade pública.')) +
 pega('<ul><li>O § 1º proíbe <b>nomes, símbolos ou imagens</b> que caracterizem <b>promoção pessoal</b>. A publicidade deve ter caráter <b>educativo, informativo ou de orientação social</b>.</li><li>O § 1º está ligado tanto à <b>publicidade</b> quanto à <b>impessoalidade</b>. Se a questão falar em promoção pessoal, pense em impessoalidade.</li><li>A ordem cronológica de pagamento de precatórios e a ordem de classificação no concurso são aplicações da impessoalidade.</li></ul>') +
 kw(["finalidade pública","isonomia","vedação de promoção pessoal","§ 1º","educativo, informativo ou de orientação social"]))

add(head(U2,T2,'Princípio da <span class="hl">moralidade</span>','Não basta ser legal: tem de ser honesto.', "A06") +
 oque(p('<strong>Moralidade administrativa</strong> exige que o agente público atue com <strong>ética, honestidade, lealdade e boa-fé</strong>. Um ato pode até ter aparência legal e, ainda assim, ser <strong>imoral</strong> e, por isso, inválido.')) +
 traduz(p('Imagine um servidor que marca a viagem a serviço sempre para a cidade onde mora a namorada, com diárias pagas pelo órgão, mesmo quando a reunião poderia ser on-line. Talvez não exista uma regra proibindo exatamente isso, mas a conduta <strong>fere a moralidade</strong>: usa o cargo em benefício próprio.')) +
 '<h3>Nepotismo: o exemplo clássico</h3>' +
 p('O STF, com base nos princípios da moralidade e da impessoalidade, editou a <strong>Súmula Vinculante 13</strong>, que proíbe nomear <strong>cônjuge, companheiro ou parente até o 3º grau</strong> (em linha reta, colateral ou por afinidade) da autoridade nomeante, ou de servidor da mesma pessoa jurídica com cargo de direção, chefia ou assessoramento, para <strong>cargo em comissão, função de confiança ou função gratificada</strong>. Inclui o <strong>nepotismo cruzado</strong> (designações recíprocas).') +
 memo('Nepotismo: parentes <strong>até o 3º grau</strong>, inclusive. Tios e sobrinhos (3º grau) <strong>entram</strong>. Primos (4º grau) <strong>não estão</strong> na SV 13.'))

graus = f'''<figure><svg viewBox="0 0 640 175" width="590" xmlns="http://www.w3.org/2000/svg" font-family="Inter">''' + "".join(
 f'<rect x="{x}" y="10" width="148" height="120" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x+74}" y="38" text-anchor="middle" font-weight="900" font-size="15" fill="{fg}">{t}</text>'
 + "".join(f'<text x="{x+74}" y="{62+i*17}" text-anchor="middle" font-size="11.5" fill="{C["ink"]}">{l}</text>' for i,l in enumerate(ls))
 for x,t,ls,fg,bg in [(8,"1º GRAU",["pais e filhos","sogro, sogra,","genro, nora"],C['red'],C['redsoft']),(166,"2º GRAU",["avós e netos","irmãos","cunhados"],C['red'],C['redsoft']),
   (324,"3º GRAU",["tios e sobrinhos","bisavós e","bisnetos"],C['red'],C['redsoft']),(482,"4º GRAU",["primos","fora da SV 13"],C['green'],C['greensoft'])]) + f'''
<text x="245" y="160" text-anchor="middle" font-size="12" font-weight="900" fill="{C['red']}">ALCANÇADOS PELA SÚMULA VINCULANTE 13 (+ cônjuge e companheiro)</text>
</svg><figcaption>Graus de parentesco e nepotismo (esquema simplificado).</figcaption></figure>'''
add(pratica_title() + graus +
 ex(p('O prefeito de um município nomeia o <b>sobrinho</b> (3º grau) como assessor em cargo em comissão: <b>nepotismo</b>, vedado pela SV 13. O secretário de saúde nomeia a filha do secretário de educação, e este nomeia a filha daquele: <b>nepotismo cruzado</b>, também vedado. A nomeação de um <b>primo</b> (4º grau) não é alcançada pela SV 13, mas ainda pode ser anulada se, no caso concreto, ficar demonstrada ofensa à moralidade.')) +
 pega('<ul><li>Para <b>cargos políticos</b> (como secretário municipal ou ministro), o STF tem afastado a aplicação automática da SV 13, salvo fraude ou falta evidente de qualificação. O tema tem nuances: leia com atenção o que a questão pede.</li><li>A moralidade pode ser defendida por qualquer cidadão por meio da <b>ação popular</b> (art. 5º, LXXIII), mesmo sem prejuízo financeiro.</li><li>Ato <b>legal</b> pode ser <b>imoral</b> e, portanto, inválido.</li></ul>') +
 kw(["ética e boa-fé","probidade","nepotismo","SV 13","até o 3º grau","nepotismo cruzado","ação popular"]))

add(head(U2,T2,'Princípio da <span class="hl">publicidade</span>','O que é público deve ser transparente.', "A07") +
 oque(p('<strong>Publicidade</strong> é o dever de dar <strong>transparência</strong> aos atos da Administração, para que a sociedade possa conhecer e controlar o que é feito com o poder e o dinheiro públicos. Em regra, os atos só produzem efeitos externos depois de publicados.')) +
 cards([("eye","Transparência","Divulgação de atos, contratos, gastos e salários. Ex.: portal da transparência.",C['blue']),
        ("doc","Eficácia dos atos","Publicação no Diário Oficial dá conhecimento geral e marca o início dos efeitos.",C['golddeep']),
        ("lock","Exceções: sigilo","Segurança da sociedade e do Estado (art. 5º, XXXIII) e intimidade (art. 5º, X).",C['red'])],3) +
 traduz(p('A regra é: <strong>o que é público tem de ser mostrado</strong>. Você tem o direito de saber quanto a prefeitura gastou na reforma da praça, quem ganhou a licitação e quanto ganha cada servidor. O sigilo é <strong>exceção</strong> e precisa de justificativa, como investigações em andamento ou dados íntimos de alguém.')) +
 memo('Regra: <strong>publicidade e transparência</strong>. Exceção: <strong>sigilo</strong> por segurança da sociedade e do Estado ou proteção da intimidade. Publicidade ≠ propaganda pessoal (§ 1º).'))

add(pratica_title() +
 flow([("doc",["ATO","assinado"]),("eye",["PUBLICAÇÃO","Diário Oficial,","portal"]),("people",["SOCIEDADE","conhece e","controla"]),("check",["ATO","produz","efeitos"])],
      "Publicar dá conhecimento à sociedade e permite o controle.", colors=colors("n","o","b","g")) +
 ex(p('Um cidadão consulta o portal da transparência e encontra o nome, o cargo e a remuneração de cada servidor da prefeitura. Isso é <b>legítimo</b>: o STF decidiu que a divulgação nominal da remuneração dos servidores em sítio eletrônico oficial não viola a intimidade (ARE 652.777). Já os dados médicos de um servidor afastado por doença são protegidos pela <b>intimidade</b> e não podem ser divulgados.')) +
 pega('<ul><li>Publicidade <b>não</b> é princípio absoluto: admite sigilo nos casos previstos.</li><li>Publicidade oficial com nome ou foto do governante → viola o <b>§ 1º</b> (impessoalidade). Publicidade é para informar, não para promover pessoas.</li><li>A Lei de Acesso à Informação (Lei nº 12.527/2011) regulamenta o direito de acesso previsto no art. 5º, XXXIII.</li></ul>') +
 kw(["transparência","condição de eficácia","sigilo excepcional","segurança da sociedade e do Estado","Lei nº 12.527/2011","remuneração nominal"]))

add(head(U2,T2,'Princípio da <span class="hl">eficiência</span>','Fazer bem, rápido e gastando pouco.', "A08") +
 oque(p('<strong>Eficiência</strong> exige que a Administração alcance <strong>os melhores resultados</strong> com <strong>qualidade, rapidez e economia</strong> de recursos. Foi incluída no art. 37 pela <strong>EC nº 19/1998</strong> (a chamada Reforma Administrativa), inspirada no modelo de administração <strong>gerencial</strong>.')) +
 cards([("chart","Resultados","Foco no que a população recebe, e não só no cumprimento de formalidades.",C['green']),
        ("hourglass","Rapidez","Prestar o serviço em tempo razoável.",C['blue']),
        ("coin","Economia","Gastar bem o dinheiro público, sem desperdício.",C['golddeep'])],3) +
 traduz(p('Não basta a repartição estar “dentro da lei”: ela precisa <strong>funcionar bem</strong>. Uma fila de seis meses para marcar uma consulta simples pode até seguir todas as regras, mas não é eficiente. A eficiência cobra do servidor e do órgão <strong>desempenho</strong>.')) +
 memo('Eficiência: <strong>EC nº 19/1998</strong>. Instrumentos: <strong>avaliação especial de desempenho</strong> para a estabilidade, <strong>avaliação periódica</strong> (que pode levar à perda do cargo) e contratos de gestão.'))

add(pratica_title() +
 flow([("clock",["ANTES","fila de madrugada","no posto de saúde"]),("bulb",["MUDANÇA","agendamento","on-line"]),("check",["DEPOIS","atendimento com","hora marcada"])],
      "Eficiência na prática: melhores resultados para o cidadão.", colors=colors("r","o","g")) +
 ex(p('A Constituição liga a eficiência à vida funcional do servidor: para adquirir a estabilidade, ele passa por <b>avaliação especial de desempenho</b> (art. 41, § 4º), e mesmo depois de estável pode perder o cargo por <b>avaliação periódica de desempenho</b>, na forma de lei complementar, assegurada ampla defesa (art. 41, § 1º, III).')) +
 pega('<ul><li>Eficiência <b>não</b> autoriza descumprir a lei: “fazer mais rápido” não justifica dispensar licitação fora das hipóteses legais. A eficiência convive com a legalidade.</li><li>Não estava no texto original: entrou com a <b>EC nº 19/1998</b>.</li><li>Eficiência (meios, uso dos recursos) é diferente de <b>eficácia</b> (alcançar a meta) e de <b>efetividade</b> (impacto real na sociedade), distinção cobrada em Administração Pública.</li></ul>') +
 kw(["EC nº 19/1998","administração gerencial","qualidade, rapidez e economia","avaliação de desempenho","eficiência x eficácia x efetividade"]))

add(head(U2,T2,'Princípios <span class="hl">implícitos</span>','Não estão no caput do art. 37, mas também obrigam a Administração.', "A09") +
 table(["Princípio","O que significa","Exemplo"],[
  ["Supremacia do interesse público","Em conflito, o interesse coletivo prevalece sobre o particular, dentro da lei.","Desapropriação de um imóvel para construir um hospital."],
  ["Indisponibilidade do interesse público","O agente não é dono do interesse público: não pode abrir mão dele à vontade.","O servidor não pode perdoar uma multa por amizade."],
  ["Autotutela","A Administração pode anular seus atos ilegais e revogar os inconvenientes ou inoportunos, ressalvada a apreciação judicial (Súmula 473 do STF).","Prefeitura anula uma nomeação feita sem concurso."],
  ["Razoabilidade e proporcionalidade","A medida deve ser adequada, necessária e na medida certa.","Não se demite um servidor por um atraso de cinco minutos."],
  ["Motivação","O ato deve indicar os fatos e os fundamentos que o justificam.","A decisão que nega um pedido explica o motivo."],
  ["Continuidade do serviço público","Os serviços essenciais não podem parar.","Limites à greve em serviços essenciais."],
  ["Segurança jurídica","Estabilidade das relações e proteção da confiança.","Não se aplica retroativamente uma nova interpretação."]],["24%",None,"32%"]) +
 lei("Lei nº 9.784/1999 · art. 2º, caput",'<p>Art. 2º A Administração Pública obedecerá, dentre outros, aos princípios da legalidade, finalidade, motivação, razoabilidade, proporcionalidade, moralidade, ampla defesa, contraditório, segurança jurídica, interesse público e eficiência.</p>','Lei do processo administrativo federal.') +
 memo('Supremacia e indisponibilidade do interesse público são as <strong>“pedras de toque”</strong> do regime jurídico administrativo. Autotutela: <strong>anula</strong> o ilegal, <strong>revoga</strong> o inconveniente.'))

SIT = [("Um guarda municipal usa a viatura oficial para levar a família à praia no fim de semana.","Moralidade (e legalidade)","Uso de bem público para fins particulares."),
 ("O prefeito coloca sua foto e seu slogan de campanha nas placas das obras.","Impessoalidade","Promoção pessoal vedada pelo art. 37, § 1º."),
 ("Um servidor concede uma licença que a lei do seu cargo não prevê.","Legalidade","A Administração só faz o que a lei permite."),
 ("A prefeitura se recusa a divulgar os contratos de uma obra, sem justificativa.","Publicidade","O sigilo é exceção e precisa de fundamento."),
 ("O secretário nomeia a esposa para um cargo em comissão na própria secretaria.","Moralidade e impessoalidade","Nepotismo (SV 13)."),
 ("Uma repartição leva dois anos para responder a um pedido simples de certidão.","Eficiência","Demora desarrazoada na prestação do serviço."),
 ("A comissão de licitação favorece a empresa de um amigo do prefeito.","Impessoalidade e moralidade","Tratamento desigual e falta de honestidade."),
 ("Um fiscal aplica a multa máxima a um ambulante por uma infração mínima, sem motivo.","Razoabilidade e proporcionalidade (implícitos)","Medida desproporcional à infração.")]
rows = "".join(f'<tr><td style="width:6%;text-align:center;font-weight:900">{i+1}</td><td>{s}</td><td style="width:26%">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</td></tr>' for i,(s,_,_) in enumerate(SIT))
ans = "".join(f'<tr><td style="width:6%;text-align:center;font-weight:900">{i+1}</td><td style="width:32%"><b>{a}</b></td><td>{c}</td></tr>' for i,(_,a,c) in enumerate(SIT))
add(head(U2,T2,'Qual princípio foi <span class="hl">violado</span>?','Exercício com oito situações administrativas. Escreva o princípio ao lado.', "A10") +
 f'<table><tr><th>#</th><th>Situação</th><th>Princípio violado</th></tr>{rows}</table>' +
 memo('Em situações de prova, procure a <strong>palavra-gatilho</strong>: “sem lei” → legalidade; “promoção pessoal”, “favorecer” → impessoalidade; “parente”, “vantagem pessoal” → moralidade; “sigilo sem motivo” → publicidade; “demora”, “desperdício” → eficiência.', "Dica:"))
add(pratica_title("Respostas do exercício") + f'<table><tr><th>#</th><th>Princípio</th><th>Por quê</th></tr>{ans}</table>' +
 pega('<p>Uma mesma conduta pode violar <b>mais de um princípio</b>. O nepotismo, por exemplo, ofende a moralidade e a impessoalidade. Na prova, escolha a alternativa que indica o princípio <b>mais diretamente</b> atingido, ou a que aceita mais de um, se houver.</p>'))

treino(2, [
 ("Os princípios expressos no caput do art. 37 são legalidade, impessoalidade, moralidade, publicidade e eficiência.","C","LIMPE."),
 ("A eficiência consta do texto original da Constituição de 1988.","E","Foi incluída pela EC nº 19/1998."),
 ("A publicidade dos atos de órgãos públicos pode conter o nome do governante, desde que tenha caráter informativo.","E","O § 1º veda nomes, símbolos ou imagens que caracterizem promoção pessoal."),
 ("A nomeação de sobrinho da autoridade nomeante para cargo em comissão viola a Súmula Vinculante 13.","C","Sobrinho é parente de 3º grau."),
 ("Pela legalidade, o servidor público pode fazer tudo o que a lei não proíbe.","E","Só pode fazer o que a lei permite."),
 ("A razoabilidade é princípio expresso no caput do art. 37.","E","É implícito na CF (expresso na Lei nº 9.784/1999).")])

# =========================================================== UNIDADE 3
opener("03","UNIDADE 3","Acesso, cargos e acumulação",["Acesso aos cargos e concurso público","Validade do concurso e direito à nomeação","Exceções ao concurso","Cargos, empregos e funções","Cargo em comissão x função de confiança","Acumulação de cargos"],"U3")

add(head(U3,T3,'Acesso aos cargos e <span class="hl">concurso público</span>','A porta de entrada, igual para todos.', "A11") +
 lei(cf("Art. 37, I e II"),'<p>I - os cargos, empregos e funções públicas são acessíveis aos brasileiros que preencham os requisitos estabelecidos em lei, assim como aos estrangeiros, na forma da lei;<br>II - a investidura em cargo ou emprego público depende de aprovação prévia em concurso público de provas ou de provas e títulos, de acordo com a natureza e a complexidade do cargo ou emprego, na forma prevista em lei, ressalvadas as nomeações para cargo em comissão declarado em lei de livre nomeação e exoneração;</p>') +
 traduz(p('Qualquer brasileiro que cumpra os <strong>requisitos da lei</strong> pode ocupar um cargo público; estrangeiros também, <strong>na forma da lei</strong>. Para entrar num cargo efetivo ou num emprego público, é preciso passar em <strong>concurso</strong> de <strong>provas</strong> ou de <strong>provas e títulos</strong>. A exceção do inciso II são os <strong>cargos em comissão</strong>, de livre nomeação e exoneração.')) +
 memo('Concurso: <strong>provas</strong> ou <strong>provas e títulos</strong>. Nunca só títulos. Requisitos de acesso: <strong>previstos em lei</strong>. Descumprir o concurso gera <strong>nulidade do ato e punição da autoridade</strong> (§ 2º).'))

add(pratica_title("Regras sobre requisitos de concurso") +
 table(["Requisito","Regra"],[
  ["Exame psicotécnico","Só se previsto em <b>lei</b> (Súmula Vinculante 44), com critérios objetivos."],
  ["Limite de idade","Só se justificado pela <b>natureza das atribuições do cargo</b> (Súmula 683 do STF)."],
  ["Pessoas com deficiência","A lei reserva percentual de vagas (art. 37, VIII)."],
  ["Provimento derivado","É inconstitucional investir o servidor, sem concurso, em cargo de <b>outra carreira</b> (Súmula Vinculante 43)."],
  ["Estrangeiros","Acesso “<b>na forma da lei</b>”: a norma não é autoaplicável."]],["28%",None]) +
 ex(p('Um município faz concurso para Guarda Municipal com provas objetivas, teste físico e exame psicotécnico. O psicotécnico só é válido se a <b>lei municipal</b> do cargo o prevê, e não apenas o edital. Já um servidor de nível médio não pode ser “promovido”, sem novo concurso, a um cargo de nível superior de outra carreira (SV 43).')) +
 pega('<ul><li>Concurso de “<b>títulos</b>” apenas → <b>não existe</b> na CF: é de provas ou de provas e títulos.</li><li>Empresas públicas e sociedades de economia mista também fazem <b>concurso</b> para <b>emprego</b> público (inciso II fala em “cargo ou emprego”).</li><li>A inobservância dos incisos II e III gera <b>nulidade do ato</b> e <b>punição da autoridade responsável</b> (§ 2º).</li></ul>') +
 kw(["requisitos estabelecidos em lei","provas ou provas e títulos","natureza e complexidade","SV 44","Súmula 683","SV 43","§ 2º: nulidade"]))

validade = f'''<figure><svg viewBox="0 0 640 175" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<defs><marker id="va" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L10,5 L0,10 z" fill="{C['ink']}"/></marker></defs>
<line x1="20" y1="80" x2="625" y2="80" stroke="{C['ink']}" stroke-width="4" marker-end="url(#va)"/>
<circle cx="40" cy="80" r="10" fill="{C['navy']}"/><text x="40" y="112" text-anchor="middle" font-weight="900" font-size="12" fill="{C['navy']}">HOMOLOGAÇÃO</text>
<rect x="55" y="54" width="270" height="22" rx="8" fill="{C['blue']}"/><text x="190" y="70" text-anchor="middle" fill="#fff" font-weight="800" font-size="12">VALIDADE: ATÉ 2 ANOS (fixada no edital)</text>
<rect x="330" y="54" width="270" height="22" rx="8" fill="{C['gold']}"/><text x="465" y="70" text-anchor="middle" fill="#2a1d00" font-weight="800" font-size="12">PRORROGAÇÃO: 1 VEZ, POR IGUAL PERÍODO</text>
<line x1="327" y1="40" x2="327" y2="120" stroke="{C['muted']}" stroke-width="2" stroke-dasharray="5 4"/>
<text x="190" y="112" text-anchor="middle" font-size="11.5" fill="{C['ink']}">ex.: edital fixa 2 anos</text>
<text x="465" y="112" text-anchor="middle" font-size="11.5" fill="{C['ink']}">+ 2 anos (se a Administração prorrogar)</text>
<text x="320" y="150" text-anchor="middle" font-size="12.5" font-weight="900" fill="{C['navy']}">Validade máxima possível: 2 + 2 = 4 anos · Se o edital fixar 1 ano: 1 + 1 = 2 anos</text>
</svg><figcaption>Art. 37, III: até dois anos, prorrogável uma vez, por igual período.</figcaption></figure>'''
add(head(U3,T3,'Validade do concurso e <span class="hl">direito à nomeação</span>','Até quando o concurso vale e quem tem direito de ser nomeado.', "A12") +
 lei(cf("Art. 37, III e IV"),'<p>III - o prazo de validade do concurso público será de até dois anos, prorrogável uma vez, por igual período;<br>IV - durante o prazo improrrogável previsto no edital de convocação, aquele aprovado em concurso público de provas ou de provas e títulos será convocado com prioridade sobre novos concursados para assumir cargo ou emprego, na carreira;</p>') + validade +
 traduz(p('O concurso “vale” por <strong>até 2 anos</strong>, e esse prazo pode ser <strong>prorrogado uma única vez</strong>, pelo <strong>mesmo período</strong>. Enquanto o concurso estiver válido, quem foi aprovado tem <strong>prioridade</strong> sobre os aprovados em um concurso novo.')) +
 memo('Validade: <strong>até 2 anos</strong> + prorrogação <strong>uma vez</strong>, <strong>por igual período</strong>. A prorrogação é <strong>discricionária</strong>. Aprovado anterior tem <strong>prioridade</strong> sobre novos concursados.'))

add(pratica_title("Quem tem direito à nomeação?") +
 flow([("trophy",["DENTRO DAS","VAGAS","do edital"]),("check",["DIREITO","SUBJETIVO","à nomeação"]),("doc",["CADASTRO","RESERVA","fora das vagas"]),("hourglass",["EXPECTATIVA","de direito","(salvo preterição)"])],
      "Aprovado dentro das vagas tem direito; fora delas, em regra, só expectativa.", colors=colors("g","b","o","r")) +
 ex(p('Um edital oferece 10 vagas para Guarda Municipal, e Ana é aprovada em 8º lugar. Pelo entendimento do STF (RE 598.099), ela tem <b>direito subjetivo</b> à nomeação dentro do prazo de validade, salvo situações excepcionais, supervenientes e devidamente motivadas. Já Bruno, aprovado em 15º lugar, em cadastro de reserva, tem <b>expectativa de direito</b>, que vira direito se houver <b>preterição arbitrária</b> (por exemplo, se contratarem temporários para as mesmas vagas).')) +
 pega('<ul><li>“Prorrogável <b>duas vezes</b>” ou “por <b>até</b> dois anos” → <b>errado</b>: <b>uma vez, por igual período</b>.</li><li>A validade é “<b>de até</b> dois anos”: pode ser menor, por exemplo, de 6 meses ou 1 ano.</li><li>A prioridade do inciso IV vale “<b>durante o prazo improrrogável previsto no edital</b>”. A CF não proíbe abrir um novo concurso enquanto o anterior está válido, mas os aprovados no anterior têm prioridade.</li></ul>') +
 kw(["até dois anos","prorrogável uma vez","por igual período","prioridade sobre novos concursados","direito subjetivo à nomeação","cadastro de reserva","preterição"]))

add(head(U3,T3,'Exceções ao <span class="hl">concurso</span>','Quando se entra no serviço público sem concurso.', "A13") +
 cards([("badge","Cargos em comissão","Livre nomeação e exoneração (art. 37, II e V). Só para direção, chefia e assessoramento.",C['blue']),
        ("hourglass","Contratação temporária","Necessidade temporária de excepcional interesse público, nos casos da lei (art. 37, IX).",C['golddeep']),
        ("ballot","Mandatos eletivos","Prefeito, vereador, deputado: o acesso é pela eleição.",C['green']),
        ("gavel","Nomeações previstas na CF","Ministros do STF e dos tribunais superiores e vagas do quinto constitucional.",C['navy']),
        ("people","Agentes comunitários de saúde e de combate às endemias","Admitidos por processo seletivo público (art. 198, § 4º).",C['red']),
        ("star","Ex-combatentes","Aproveitamento previsto no ADCT (art. 53).",C['muted'])],3) +
 lei(cf("Art. 37, IX"),'<p>IX - a lei estabelecerá os casos de contratação por tempo determinado para atender a necessidade temporária de excepcional interesse público;</p>') +
 traduz(p('A regra é o concurso. As exceções existem por motivos específicos: confiança pessoal (comissionados), urgência temporária (temporários), escolha popular (eleitos) ou escolha prevista na própria Constituição (ministros de tribunais). Fora dessas hipóteses, nomear sem concurso é <strong>nulo</strong>.')))
add(pratica_title('Atenção na prova') +
 pega('<ul><li>A contratação temporária exige: <b>casos previstos em lei</b>, <b>tempo determinado</b>, necessidade <b>temporária</b> e interesse público <b>excepcional</b>. Não pode servir para atividades permanentes e rotineiras.</li><li>Temporários exercem <b>função</b> pública, sem cargo efetivo, e não adquirem estabilidade.</li><li>Agentes comunitários de saúde: <b>processo seletivo público</b>, e não concurso público nos moldes do inciso II.</li></ul>') + kw(['cargo em comissão', 'contratação temporária', 'excepcional interesse público', 'mandato eletivo', 'processo seletivo público', 'art. 37, IX']))

add(head(U3,T3,'Cargos, empregos e <span class="hl">funções</span>','Três formas de ocupar um posto no serviço público.', "A14") +
 table(["","CARGO","EMPREGO","FUNÇÃO"],[
  ["O que é","Posto criado por lei, com atribuições e denominação próprias","Posto de quem é contratado pelo regime da CLT","Conjunto de atribuições <b>sem</b> cargo ou emprego correspondente"],
  ["Regime","Estatutário (estatuto do servidor)","Celetista (CLT)","Depende: função de confiança ou temporária"],
  ["Onde é típico","Administração direta, autarquias e fundações públicas","Empresas públicas e sociedades de economia mista","Em toda a Administração"],
  ["Ocupante","Servidor público (efetivo ou comissionado)","Empregado público","Servidor efetivo (confiança) ou contratado temporário"],
  ["Estabilidade (art. 41)","Sim, para o efetivo após 3 anos","<span class='no'>Não</span>","<span class='no'>Não</span>"]],["16%",None,None,None]) +
 traduz(p('O <strong>cargo</strong> é o “lugar” criado por lei para o servidor estatutário, como o de Guarda Municipal ou Analista Judiciário. O <strong>emprego</strong> é o posto do empregado público regido pela CLT, como um atendente da Caixa. A <strong>função</strong> é um conjunto de tarefas que alguém exerce <strong>sem ter um cargo próprio para isso</strong>: por exemplo, o servidor efetivo designado para chefiar um setor.')) +
 memo('Cargo = <strong>estatutário</strong>. Emprego = <strong>CLT</strong>. Função = <strong>atribuições sem cargo</strong> (de confiança ou temporária). Estabilidade do art. 41: só para <strong>cargo efetivo</strong>.') +
 ex(p('Paula é Guarda Municipal concursada: ocupa um <b>cargo efetivo</b>. Pedro trabalha no Banco do Brasil, sociedade de economia mista, após concurso: ocupa um <b>emprego público</b>. Joana, servidora efetiva, foi designada para chefiar o protocolo: exerce uma <b>função de confiança</b>, além do seu cargo.')))

add(head(U3,T3,'Cargo em comissão x <span class="hl">função de confiança</span>','O par de conceitos mais cobrado do inciso V.', "A15") +
 lei(cf("Art. 37, V"),'<p>V - as funções de confiança, exercidas exclusivamente por servidores ocupantes de cargo efetivo, e os cargos em comissão, a serem preenchidos por servidores de carreira nos casos, condições e percentuais mínimos previstos em lei, destinam-se apenas às atribuições de direção, chefia e assessoramento;</p>') +
 table(["","CARGO EM COMISSÃO","FUNÇÃO DE CONFIANÇA"],[
  ["Quem pode ocupar","<b>Qualquer pessoa</b>, com percentual mínimo reservado a servidores de carreira, conforme a lei","<b>Exclusivamente</b> servidores ocupantes de cargo efetivo"],
  ["Atribuições","Direção, chefia e assessoramento","Direção, chefia e assessoramento"],
  ["Nomeação e saída","Livre nomeação e exoneração (<i>ad nutum</i>)","Livre designação e dispensa"],
  ["Concurso","Não exige","O ocupante já é concursado"],
  ["Estabilidade","<span class='no'>Nunca</span>","Na função, não; no cargo efetivo, sim"]],["22%",None,None]) +
 traduz(p('O <strong>cargo em comissão</strong> é um cargo de verdade, criado por lei, que pode ser ocupado por alguém “de fora”: por exemplo, um assessor jurídico sem vínculo anterior com a prefeitura. A <strong>função de confiança</strong> é uma atribuição extra dada a quem <strong>já é servidor efetivo</strong>, como chefe de seção.')) +
 memo('Função de confiança: <strong>só efetivos</strong>. Cargo em comissão: <strong>qualquer pessoa</strong>, respeitado o <strong>percentual mínimo</strong> legal de servidores de carreira. Ambos: <strong>direção, chefia e assessoramento</strong>.'))
add(pratica_title('Atenção na prova') +
 pega('<ul><li>Cargo em comissão para atividades <b>técnicas ou burocráticas</b> (como motorista ou digitador) é <b>inconstitucional</b>: só serve para direção, chefia e assessoramento.</li><li>“Função de confiança pode ser exercida por pessoa sem vínculo” → <b>errado</b>: é <b>exclusiva</b> de servidores efetivos.</li></ul>') + kw(['função de confiança', 'exclusivamente efetivos', 'cargo em comissão', 'percentual mínimo', 'direção, chefia e assessoramento', 'ad nutum']))

acum = f'''<figure><svg viewBox="0 0 640 300" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<defs><marker id="aa" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L10,5 L0,10 z" fill="{C['ink']}"/></marker></defs>
<rect x="20" y="10" width="300" height="50" rx="12" fill="#fff" stroke="{C['navy']}" stroke-width="2.5"/><text x="170" y="31" text-anchor="middle" font-weight="900" font-size="13" fill="{C['navy']}">1. A combinação está nas exceções?</text><text x="170" y="49" text-anchor="middle" font-size="11" fill="{C['ink']}">(2 professores · professor + outro cargo · 2 saúde)</text>
<line x1="320" y1="35" x2="420" y2="35" stroke="{C['red']}" stroke-width="3" marker-end="url(#aa)"/><text x="370" y="28" text-anchor="middle" font-weight="900" font-size="11" fill="{C['red']}">NÃO</text>
<rect x="426" y="12" width="200" height="46" rx="12" fill="{C['redsoft']}" stroke="{C['red']}" stroke-width="2.5"/><text x="526" y="40" text-anchor="middle" font-weight="900" font-size="13" fill="{C['red']}">ACUMULAÇÃO VEDADA</text>
<line x1="170" y1="60" x2="170" y2="92" stroke="{C['green']}" stroke-width="3" marker-end="url(#aa)"/><text x="186" y="81" font-weight="900" font-size="11" fill="{C['green']}">SIM</text>
<rect x="20" y="98" width="300" height="50" rx="12" fill="#fff" stroke="{C['navy']}" stroke-width="2.5"/><text x="170" y="119" text-anchor="middle" font-weight="900" font-size="13" fill="{C['navy']}">2. Há compatibilidade de horários?</text><text x="170" y="137" text-anchor="middle" font-size="11" fill="{C['ink']}">(um horário não pode se sobrepor ao outro)</text>
<line x1="320" y1="123" x2="420" y2="123" stroke="{C['red']}" stroke-width="3" marker-end="url(#aa)"/><text x="370" y="116" text-anchor="middle" font-weight="900" font-size="11" fill="{C['red']}">NÃO</text>
<rect x="426" y="100" width="200" height="46" rx="12" fill="{C['redsoft']}" stroke="{C['red']}" stroke-width="2.5"/><text x="526" y="128" text-anchor="middle" font-weight="900" font-size="13" fill="{C['red']}">ACUMULAÇÃO VEDADA</text>
<line x1="170" y1="148" x2="170" y2="180" stroke="{C['green']}" stroke-width="3" marker-end="url(#aa)"/><text x="186" y="169" font-weight="900" font-size="11" fill="{C['green']}">SIM</text>
<rect x="20" y="186" width="300" height="50" rx="12" fill="#fff" stroke="{C['navy']}" stroke-width="2.5"/><text x="170" y="207" text-anchor="middle" font-weight="900" font-size="13" fill="{C['navy']}">3. Respeita o teto remuneratório?</text><text x="170" y="225" text-anchor="middle" font-size="11" fill="{C['ink']}">(art. 37, XI: “observado em qualquer caso”)</text>
<line x1="170" y1="236" x2="170" y2="262" stroke="{C['green']}" stroke-width="3" marker-end="url(#aa)"/><text x="186" y="253" font-weight="900" font-size="11" fill="{C['green']}">SIM</text>
<rect x="60" y="266" width="220" height="30" rx="10" fill="{C['greensoft']}" stroke="{C['green']}" stroke-width="2.5"/><text x="170" y="286" text-anchor="middle" font-weight="900" font-size="13" fill="{C['green']}">ACUMULAÇÃO PERMITIDA</text>
<text x="470" y="215" text-anchor="middle" font-size="11" fill="{C['muted']}">Obs.: o STF entende que o teto</text><text x="470" y="231" text-anchor="middle" font-size="11" fill="{C['muted']}">incide sobre cada vínculo</text><text x="470" y="247" text-anchor="middle" font-size="11" fill="{C['muted']}">isoladamente (Temas 377 e 384).</text>
</svg><figcaption>Fluxo de decisão: posso acumular estes cargos?</figcaption></figure>'''
add(head(U3,T3,'Acumulação de <span class="hl">cargos</span>','Regra: proibido. Exceções: três combinações, com horários compatíveis.', "A16") +
 lei(cf("Art. 37, XVI e XVII"),'<p>XVI - é vedada a acumulação remunerada de cargos públicos, exceto, quando houver compatibilidade de horários, observado em qualquer caso o disposto no inciso XI: a) a de dois cargos de professor; b) a de um cargo de professor com outro de qualquer natureza; c) a de dois cargos ou empregos privativos de profissionais de saúde, com profissões regulamentadas;<br>XVII - a proibição de acumular estende-se a empregos e funções e abrange autarquias, fundações, empresas públicas, sociedades de economia mista, suas subsidiárias, e sociedades controladas, direta ou indiretamente, pelo poder público;</p>', 'Alínea “b” com redação dada pela EC nº 138/2025; alínea “c” pela EC nº 34/2001.') + acum)

add(pratica_title() +
 cards([("teacher","2 professores","Professor da rede estadual de manhã e da municipal à tarde.",C['green']),
        ("exam","Professor + cargo de qualquer natureza","Guarda municipal à noite e professor da rede estadual de dia (EC nº 138/2025).",C['blue']),
        ("cross","2 da saúde regulamentada","Enfermeira em dois hospitais públicos, com escalas compatíveis.",C['red'])],3) +
 lembre(p('<strong>Atenção, mudança recente:</strong> até 2025, a alínea “b” permitia acumular um cargo de professor com outro “<strong>técnico ou científico</strong>”, e havia muita discussão sobre o que contava como cargo técnico. A <strong>EC nº 138/2025</strong> mudou o texto para “um cargo de professor com outro <strong>de qualquer natureza</strong>”. Hoje, por exemplo, um <strong>agente administrativo</strong> ou um <strong>guarda municipal</strong> pode acumular com um cargo de professor, desde que haja <strong>compatibilidade de horários</strong> e respeito ao <strong>teto</strong>. Cuidado com apostilas e questões anteriores à emenda.'), "Atualização constitucional 2025") +
 lei(cf("Art. 37, § 10"),'<p>§ 10. É vedada a percepção simultânea de proventos de aposentadoria decorrentes do art. 40 ou dos arts. 42 e 142 com a remuneração de cargo, emprego ou função pública, ressalvados os cargos acumuláveis na forma desta Constituição, os cargos eletivos e os cargos em comissão declarados em lei de livre nomeação e exoneração.</p>') +
 pega('<ul><li>A proibição alcança <b>cargos, empregos e funções</b>, na administração <b>direta e indireta</b>, inclusive subsidiárias e sociedades controladas pelo poder público (XVII).</li><li>Questões antigas que exigem cargo “técnico ou científico” para acumular com o de professor seguem a redação <b>anterior</b> à EC nº 138/2025.</li><li>A CF prevê outras hipóteses fora do art. 37: juiz e membro do MP podem exercer <b>uma</b> função de magistério; o vereador acumula o mandato com o cargo se houver compatibilidade de horários (art. 38, III).</li><li>Aposentado pode receber proventos junto com a remuneração de cargo <b>acumulável</b>, <b>eletivo</b> ou <b>em comissão</b> (§ 10).</li></ul>'))

treino(3, [
 ("O concurso público pode ser apenas de títulos, conforme a natureza do cargo.","E","É de provas ou de provas e títulos."),
 ("O prazo de validade do concurso é de até dois anos, prorrogável uma vez, por igual período.","C","Art. 37, III."),
 ("As funções de confiança podem ser exercidas por pessoas sem vínculo com a Administração.","E","São exclusivas de servidores ocupantes de cargo efetivo."),
 ("Cargos em comissão destinam-se apenas às atribuições de direção, chefia e assessoramento.","C","Art. 37, V."),
 ("É permitida a acumulação de dois cargos de professor, desde que haja compatibilidade de horários.","C","Art. 37, XVI, “a”."),
 ("A proibição de acumular não alcança as sociedades de economia mista.","E","Alcança (art. 37, XVII).")])

# =========================================================== UNIDADE 4
opener("04","UNIDADE 4","Servidores e responsabilidade",["Sindicalização, greve, PcD e temporários","Remuneração e teto","Servidor com mandato eletivo (art. 38)","Arts. 39 e 40: direitos e aposentadoria","Estabilidade (art. 41)","Perda do cargo e reintegração","Responsabilidade do Estado e dos agentes"],"U4")

add(head(U4,T4,'Sindicalização, greve, PcD e <span class="hl">temporários</span>','Direitos coletivos e regras de ingresso especiais.', "A17") +
 lei(cf("Art. 37, VI a IX"),'<p>VI - é garantido ao servidor público civil o direito à livre associação sindical;<br>VII - o direito de greve será exercido nos termos e nos limites definidos em lei específica;<br>VIII - a lei reservará percentual dos cargos e empregos públicos para as pessoas portadoras de deficiência e definirá os critérios de sua admissão;<br>IX - a lei estabelecerá os casos de contratação por tempo determinado para atender a necessidade temporária de excepcional interesse público;</p>') +
 cards([("handshake","Sindicalização (VI)","Garantida ao servidor <b>civil</b>. Ao militar, é <b>proibida</b> (art. 142, § 3º, IV).",C['blue']),
        ("megaphone","Greve (VII)","Nos termos de <b>lei específica</b>, que ainda não foi editada. O STF manda aplicar, no que couber, a lei de greve do setor privado.",C['golddeep']),
        ("people","PcD (VIII)","A lei reserva percentual de cargos e empregos e define os critérios de admissão.",C['green'])],3) +
 traduz(p('O servidor civil pode se <strong>sindicalizar</strong> e fazer <strong>greve</strong>, mas a greve depende de uma <strong>lei específica</strong> que o Congresso ainda não fez. Por isso o STF, em mandados de injunção, determinou a aplicação da lei de greve da iniciativa privada (Lei nº 7.783/1989), no que couber. <strong>Militares</strong> não podem fazer greve nem se sindicalizar.')))
add(pratica_title('Atenção na prova') +
 pega('<ul><li><b>Militares</b>: proibidas a sindicalização e a greve (art. 142, § 3º, IV).</li><li>O STF fixou que é <b>vedado o exercício do direito de greve</b> aos policiais civis e a todos os servidores públicos que atuem <b>diretamente na área de segurança pública</b> (ARE 654.432, Tema 541).</li><li>Os dias de greve, em regra, podem ser <b>descontados</b>, admitida a compensação por acordo (RE 693.456, Tema 531).</li><li>Greve: “lei <b>específica</b>”, e não lei complementar.</li></ul>') + kw(['sindicalização', 'greve: lei específica', 'Tema 541', 'Tema 531', 'reserva para PcD', 'temporários']))

teto = f'''<figure><svg viewBox="0 0 640 230" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<rect x="160" y="8" width="320" height="50" rx="12" fill="{C['navy']}"/><text x="320" y="30" text-anchor="middle" fill="{C['gold']}" font-weight="900" font-size="13">TETO GERAL</text><text x="320" y="48" text-anchor="middle" fill="#fff" font-weight="800" font-size="13">subsídio de Ministro do STF</text>
<path d="M320 58 V76 M110 76 H530 M110 76 V92 M530 76 V92" stroke="{C['ink']}" stroke-width="2.5" fill="none"/>
<rect x="10" y="92" width="200" height="66" rx="12" fill="{C['redsoft']}" stroke="{C['red']}" stroke-width="2.5"/><text x="110" y="116" text-anchor="middle" font-weight="900" font-size="13" fill="{C['red']}">MUNICÍPIOS</text><text x="110" y="138" text-anchor="middle" font-size="12" fill="{C['ink']}">subsídio do <tspan font-weight="900">Prefeito</tspan></text>
<rect x="230" y="92" width="400" height="130" rx="12" fill="{C['sky']}" stroke="{C['blue']}" stroke-width="2.5"/><text x="430" y="116" text-anchor="middle" font-weight="900" font-size="13" fill="{C['blue']}">ESTADOS E DISTRITO FEDERAL</text>
<text x="248" y="142" font-size="12" fill="{C['ink']}"><tspan font-weight="900">Executivo:</tspan> subsídio do Governador</text>
<text x="248" y="164" font-size="12" fill="{C['ink']}"><tspan font-weight="900">Legislativo:</tspan> subsídio dos Deputados Estaduais e Distritais</text>
<text x="248" y="186" font-size="12" fill="{C['ink']}"><tspan font-weight="900">Judiciário:</tspan> Desembargadores do TJ (até 90,25% do Ministro</text>
<text x="248" y="204" font-size="12" fill="{C['ink']}">do STF), aplicado também a MP, Procuradores e Defensores</text>
</svg><figcaption>Teto e subtetos remuneratórios (art. 37, XI), em esquema simplificado.</figcaption></figure>'''
add(head(U4,T4,'Remuneração e <span class="hl">teto</span>','Quem fixa, como reajusta e até quanto se pode ganhar.', "A18") + teto +
 table(["Regra","Resumo"],[
  ["Fixação (X)","Remuneração e subsídio só podem ser fixados ou alterados por <b>lei específica</b>, assegurada <b>revisão geral anual</b>, sempre na mesma data e sem distinção de índices."],
  ["Teto (XI)","Ninguém recebe acima do subsídio de Ministro do STF; nos Estados, DF e Municípios valem os subtetos."],
  ["Vinculação (XIII)","É vedado vincular ou equiparar remunerações (ex.: “o salário do cargo A será sempre igual ao do cargo B”)."],
  ["Irredutibilidade (XV)","O subsídio e os vencimentos são irredutíveis, ressalvadas as hipóteses da CF (como a adequação ao teto)."]],["24%",None]) +
 memo('Teto geral: <strong>Ministro do STF</strong>. Municípios: <strong>Prefeito</strong>. Estados/DF: <strong>Governador</strong> (Executivo), <strong>Deputados</strong> (Legislativo), <strong>Desembargadores</strong> (Judiciário, até 90,25%).') +
 pega('<ul><li>No Município, o subteto é o subsídio do <b>Prefeito</b>, e não o do vereador.</li><li>A irredutibilidade é <b>nominal</b>: não garante reajuste pela inflação; o que existe é o direito à revisão geral anual na forma da lei.</li><li>Remuneração só por <b>lei específica</b>: decreto ou portaria não podem aumentar salário.</li></ul>'))

add(head(U4,T4,'Servidor com <span class="hl">mandato eletivo</span>','Art. 38: o que acontece com o cargo quando o servidor é eleito.', "A19") +
 table(["Mandato","O que acontece com o cargo","Remuneração"],[
  ["Federal, estadual ou distrital (deputado, senador, governador)","<b>Afastado</b> do cargo","Recebe a do <b>mandato</b>"],
  ["Prefeito","<b>Afastado</b> do cargo","Pode <b>optar</b> pela remuneração do cargo ou do mandato"],
  ["Vereador, <b>com</b> compatibilidade de horários","<b>Não</b> se afasta: exerce os dois","Recebe as <b>duas</b>"],
  ["Vereador, <b>sem</b> compatibilidade","Afastado (como o Prefeito)","Pode <b>optar</b>"]],["30%",None,"30%"]) +
 traduz(p('Um servidor eleito <strong>deputado</strong> se afasta do cargo e vive do salário de deputado. Eleito <strong>prefeito</strong>, também se afasta, mas pode escolher qual remuneração prefere. Eleito <strong>vereador</strong>, se os horários forem compatíveis, continua no cargo e acumula as duas remunerações. Em todos os casos de afastamento, o tempo conta para todos os efeitos, <strong>exceto promoção por merecimento</strong>.')) +
 flow([("ballot",["ELEITO","DEPUTADO","afasta-se"]),("capitol",["ELEITO","PREFEITO","afasta-se e opta"]),("clock",["ELEITO","VEREADOR","horário compatível?"]),("check",["SIM","acumula","cargo e mandato"])],
      "Art. 38 em quatro passos.", colors=colors("n","b","o","g")))
add(pratica_title('Atenção na prova') +
 pega('<ul><li>Só o <b>vereador</b> pode acumular cargo e mandato, e só com <b>compatibilidade de horários</b>.</li><li>O direito de <b>optar</b> pela remuneração é do <b>Prefeito</b> (e do vereador sem compatibilidade), e não do deputado.</li><li>O tempo de afastamento <b>não</b> conta para promoção por <b>merecimento</b>.</li></ul>') + kw(['afastamento', 'opção pela remuneração', 'vereador: compatibilidade', 'promoção por merecimento', 'art. 38']))

add(head(U4,T4,'Arts. 39 e 40: direitos e <span class="hl">aposentadoria</span>','Noções sobre os direitos sociais do servidor e o regime próprio de previdência.', "A20") +
 '<h3>Direitos sociais do art. 7º que se aplicam ao servidor (art. 39, § 3º)</h3>' +
 cards([("coin","Remuneração","Salário mínimo; 13º salário; adicional noturno; salário-família.",C['golddeep']),
        ("clock","Jornada","Duração máxima do trabalho; repouso semanal remunerado; hora extra com acréscimo de pelo menos 50%.",C['blue']),
        ("calendar","Férias e licenças","Férias com pelo menos 1/3 a mais; licença à gestante; licença-paternidade.",C['green'])],3) +
 p('A lista inclui também a proteção do mercado de trabalho da mulher, a redução dos riscos do trabalho e a proibição de diferença de salários por sexo, idade, cor ou estado civil. A lei pode estabelecer requisitos diferenciados de admissão quando a natureza do cargo o exigir. <strong>FGTS</strong>, por exemplo, <strong>não</strong> está na lista: é direito do empregado celetista.') +
 '<h3>Aposentadoria do servidor efetivo (art. 40, noções)</h3>' +
 table(["Modalidade","Resumo"],[
  ["Por incapacidade permanente","Quando o servidor não puder ser readaptado, com avaliações periódicas."],
  ["Compulsória","Aos <b>70 anos</b>, ou aos <b>75 anos</b> na forma de lei complementar (a LC nº 152/2015 fixou 75 anos), com proventos proporcionais ao tempo de contribuição."],
  ["Voluntária","Na <b>União</b>: 62 anos (mulher) e 65 anos (homem), mais os requisitos da lei. Nos Estados, DF e Municípios: idade definida em suas Constituições e Leis Orgânicas."]],["26%",None]) +
 memo('Regime próprio (RPPS): só para <strong>titulares de cargo efetivo</strong>, com caráter <strong>contributivo e solidário</strong>. Comissionado “puro”, temporário e empregado público: <strong>Regime Geral</strong> (INSS).'))
add(pratica_title('Atenção na prova') +
 pega('<ul><li>Compulsória: a CF fala em 70 anos <b>ou</b> 75 anos “na forma de lei complementar”, e a <b>LC nº 152/2015</b> fixou <b>75 anos</b>.</li><li>As regras do art. 40 foram profundamente alteradas pela <b>EC nº 103/2019</b> (Reforma da Previdência). Para prova de nível médio, foque nas modalidades e no público do RPPS.</li><li>A <b>EC nº 140/2026</b> incluiu no art. 40 regra própria de aposentadoria para <b>agentes comunitários de saúde e de combate às endemias</b> (57 anos, se mulher, e 60, se homem, com 25 anos de contribuição e de efetivo exercício na atividade).</li></ul>') + kw(['art. 39, § 3º', 'subsídio em parcela única', 'RPPS', 'compulsória: 75 anos', 'EC nº 103/2019', 'EC nº 140/2026']))

ART41 = '<p>Art. 41. São estáveis após três anos de efetivo exercício os servidores nomeados para cargo de provimento efetivo em virtude de concurso público.<br>§ 4º Como condição para a aquisição da estabilidade, é obrigatória a avaliação especial de desempenho por comissão instituída para essa finalidade.</p>'
add(head(U4,T4,'<span class="hl">Estabilidade</span>','A garantia de permanência do servidor efetivo.', "A21") +
 lei(cf("Art. 41, caput e § 4º"), ART41, "Redação dada pela EC nº 19/1998.") +
 flow([("exam",["CONCURSO","PÚBLICO"]),("badge",["NOMEAÇÃO","cargo de","provimento efetivo"]),("calendar",["3 ANOS","de efetivo","exercício"]),("check",["AVALIAÇÃO","ESPECIAL","de desempenho"]),("shield",["ESTÁVEL"])],
      "Os quatro requisitos para adquirir a estabilidade.", colors=colors("n","b","o","g","g")) +
 traduz(p('Estabilidade é a garantia de que o servidor <strong>não será mandado embora</strong> por motivos políticos ou pela vontade do chefe. Ela protege o <strong>serviço público</strong>: o servidor pode cumprir a lei sem medo de retaliação. Para ter estabilidade, é preciso <strong>concurso</strong>, <strong>cargo efetivo</strong>, <strong>3 anos de exercício</strong> e <strong>aprovação na avaliação especial de desempenho</strong>.')) +
 memo('Estabilidade: <strong>concurso + cargo efetivo + 3 anos + avaliação especial</strong>. Não têm estabilidade: comissionado puro, temporário e empregado público.'))

add(pratica_title("Estabilidade x vitaliciedade x efetividade") +
 table(["","ESTABILIDADE","VITALICIEDADE","EFETIVIDADE"],[
  ["Quem","Servidor efetivo concursado","Juízes, membros do MP e dos Tribunais de Contas","Característica do cargo"],
  ["Quando","Após 3 anos + avaliação","Juízes de 1º grau e membros do MP: após 2 anos de exercício","Desde a posse"],
  ["Perde o cargo por","Sentença transitada, PAD, avaliação periódica ou excesso de despesa","Somente sentença judicial transitada em julgado","—"],
  ["Ideia","Garantia no <b>serviço público</b>","Garantia no <b>cargo</b>","Forma de provimento"]],["16%",None,None,None]) +
 ex(p('Marta é Guarda Municipal há 2 anos. Ela já é servidora <b>efetiva</b> (desde a posse), mas ainda <b>não é estável</b>: está em estágio probatório. Se for reprovada na avaliação, poderá ser exonerada, com direito a processo com ampla defesa. Depois de 3 anos e aprovada na avaliação especial, torna-se estável.')) +
 pega('<ul><li><b>Efetividade</b> (característica do cargo, desde a posse) ≠ <b>estabilidade</b> (garantia adquirida após 3 anos e avaliação).</li><li>A estabilidade é no <b>serviço público</b>, e não no cargo: extinto o cargo, o servidor estável fica em <b>disponibilidade</b>, e não é demitido.</li><li>O prazo é de <b>3 anos</b> desde a EC nº 19/1998 (antes eram 2), e a avaliação especial é <b>obrigatória</b>. A jurisprudência alinhou o estágio probatório a esse mesmo prazo de 3 anos.</li><li>Empregados de empresas públicas e sociedades de economia mista <b>não</b> têm a estabilidade do art. 41.</li></ul>'))

ART41b = '<p>§ 1º O servidor público estável só perderá o cargo: I - em virtude de sentença judicial transitada em julgado; II - mediante processo administrativo em que lhe seja assegurada ampla defesa; III - mediante procedimento de avaliação periódica de desempenho, na forma de lei complementar, assegurada ampla defesa.<br>§ 2º Invalidada por sentença judicial a demissão do servidor estável, será ele reintegrado, e o eventual ocupante da vaga, se estável, reconduzido ao cargo de origem, sem direito a indenização, aproveitado em outro cargo ou posto em disponibilidade com remuneração proporcional ao tempo de serviço.<br>§ 3º Extinto o cargo ou declarada a sua desnecessidade, o servidor estável ficará em disponibilidade, com remuneração proporcional ao tempo de serviço, até seu adequado aproveitamento em outro cargo.</p>'
add(head(U4,T4,'Perda do cargo e <span class="hl">reintegração</span>','Quando o estável perde o cargo e o que acontece se a demissão for anulada.', "A22") +
 lei(cf("Art. 41, §§ 1º a 3º"), ART41b) +
 cards([("gavel","1. Sentença judicial","Transitada em julgado (art. 41, § 1º, I).",C['red']),
        ("doc","2. Processo administrativo","Com ampla defesa (art. 41, § 1º, II).",C['golddeep']),
        ("chart","3. Avaliação periódica","Na forma de lei complementar, com ampla defesa (art. 41, § 1º, III).",C['blue']),
        ("coin","4. Excesso de despesa","Com pessoal acima do limite legal, por ato normativo motivado (art. 169, § 4º).",C['navy'])],2) +
 memo('Estável perde o cargo em <strong>4 hipóteses</strong>: <strong>sentença</strong> transitada · <strong>PAD</strong> · <strong>avaliação periódica</strong> (LC) · <strong>excesso de despesa</strong> (art. 169, § 4º).'))

reint = f'''<figure><svg viewBox="0 0 640 230" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<defs><marker id="ra" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L10,5 L0,10 z" fill="{C['ink']}"/></marker></defs>
<rect x="10" y="10" width="190" height="64" rx="12" fill="{C['redsoft']}" stroke="{C['red']}" stroke-width="2.5"/><text x="105" y="36" text-anchor="middle" font-weight="900" font-size="13" fill="{C['red']}">JOÃO É DEMITIDO</text><text x="105" y="56" text-anchor="middle" font-size="11" fill="{C['ink']}">e Maria assume a vaga</text>
<line x1="200" y1="42" x2="238" y2="42" stroke="{C['ink']}" stroke-width="3" marker-end="url(#ra)"/>
<rect x="244" y="10" width="170" height="64" rx="12" fill="{C['goldsoft']}" stroke="{C['golddeep']}" stroke-width="2.5"/><text x="329" y="36" text-anchor="middle" font-weight="900" font-size="13" fill="{C['golddeep']}">JUIZ ANULA</text><text x="329" y="56" text-anchor="middle" font-size="11" fill="{C['ink']}">a demissão de João</text>
<line x1="414" y1="42" x2="452" y2="42" stroke="{C['ink']}" stroke-width="3" marker-end="url(#ra)"/>
<rect x="458" y="10" width="172" height="64" rx="12" fill="{C['greensoft']}" stroke="{C['green']}" stroke-width="2.5"/><text x="544" y="36" text-anchor="middle" font-weight="900" font-size="13" fill="{C['green']}">REINTEGRAÇÃO</text><text x="544" y="56" text-anchor="middle" font-size="11" fill="{C['ink']}">João volta ao cargo</text>
<line x1="544" y1="74" x2="544" y2="100" stroke="{C['ink']}" stroke-width="3" marker-end="url(#ra)"/>
<text x="320" y="122" text-anchor="middle" font-weight="900" font-size="13" fill="{C['navy']}">E Maria, que ocupava a vaga (se for estável)?</text>
''' + "".join(f'<rect x="{x}" y="136" width="196" height="84" rx="12" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x+98}" y="162" text-anchor="middle" font-weight="900" font-size="13" fill="{fg}">{t}</text>' + "".join(f'<text x="{x+98}" y="{182+i*15}" text-anchor="middle" font-size="11" fill="{C["ink"]}">{l}</text>' for i,l in enumerate(ls))
 for x,t,ls,fg,bg in [(10,"RECONDUÇÃO",["volta ao cargo de origem,","sem indenização"],C['blue'],C['sky']),(222,"APROVEITAMENTO",["vai para outro cargo"],C['golddeep'],C['goldsoft']),(434,"DISPONIBILIDADE",["fica em casa, com","remuneração proporcional","ao tempo de serviço"],C['navy'],'#e3e9f3')]) + '</svg><figcaption>Art. 41, § 2º: o que acontece com cada um quando a demissão é anulada.</figcaption></figure>'
add(pratica_title("Reintegração, recondução e disponibilidade") + reint +
 table(["Instituto","Significado"],[
  ["Reintegração","Retorno do servidor estável ao cargo após a <b>anulação da demissão</b>."],
  ["Recondução","Retorno do servidor estável ao <b>cargo de origem</b>, por exemplo quando o antigo ocupante é reintegrado."],
  ["Disponibilidade","Servidor estável fica sem exercer o cargo, recebendo <b>remuneração proporcional ao tempo de serviço</b>."],
  ["Aproveitamento","Retorno do servidor em disponibilidade a um cargo compatível."]],["26%",None]) +
 pega('<ul><li>Na disponibilidade, a remuneração é <b>proporcional ao tempo de serviço</b>, e não integral.</li><li>A recondução do ocupante da vaga ocorre <b>sem direito a indenização</b>.</li><li>Extinto o cargo ou declarada a sua desnecessidade, o estável fica em <b>disponibilidade</b> até ser aproveitado (§ 3º). Ele não é demitido.</li></ul>'))

add(head(U4,T4,'Responsabilidade do Estado e dos <span class="hl">agentes</span>','Quem paga pelos danos causados por servidores e prestadores de serviço público.', "A23") +
 lei(cf("Art. 37, § 6º"),'<p>§ 6º As pessoas jurídicas de direito público e as de direito privado prestadoras de serviços públicos responderão pelos danos que seus agentes, nessa qualidade, causarem a terceiros, assegurado o direito de regresso contra o responsável nos casos de dolo ou culpa.</p>') +
 flow([("car",["VIATURA","da Guarda","colide"]),("person",["VÍTIMA","processa o","MUNICÍPIO"]),("scales",["RESPONSABILIDADE","OBJETIVA","dano + nexo"]),("gavel",["REGRESSO","contra o guarda,","se dolo ou culpa"])],
      "Responsabilidade objetiva do Estado e subjetiva do agente (em regresso).", colors=colors("r","b","o","n")) +
 traduz(p('Se um servidor, <strong>agindo como servidor</strong>, causa dano a alguém, quem responde perante a vítima é o <strong>Estado</strong> (ou a empresa privada que presta o serviço público), e a vítima <strong>não precisa provar culpa</strong>: basta o <strong>dano</strong> e a <strong>ligação</strong> entre ele e a atuação do agente. Depois, o Estado pode cobrar do servidor, em <strong>ação de regresso</strong>, se ele agiu com <strong>dolo ou culpa</strong>.')) +
 memo('Estado: responsabilidade <strong>objetiva</strong> (sem provar culpa), teoria do <strong>risco administrativo</strong>. Agente: responsabilidade <strong>subjetiva</strong>, em <strong>regresso</strong>, se houver <strong>dolo ou culpa</strong>.'))

add(pratica_title("Responsabilidade e improbidade") +
 ex(p('Um ônibus de uma concessionária privada do transporte municipal atropela um pedestre. A concessionária responde <b>objetivamente</b>, mesmo a vítima não sendo passageira: o STF entende que a responsabilidade objetiva da prestadora alcança também os terceiros não usuários do serviço (RE 591.874). E a vítima deve processar o <b>Estado ou a prestadora</b>, e não diretamente o agente (STF, Tema 940, “teoria da dupla garantia”).')) +
 lei(cf("Art. 37, §§ 4º e 5º"),'<p>§ 4º Os atos de improbidade administrativa importarão a suspensão dos direitos políticos, a perda da função pública, a indisponibilidade dos bens e o ressarcimento ao erário, na forma e gradação previstas em lei, sem prejuízo da ação penal cabível.<br>§ 5º A lei estabelecerá os prazos de prescrição para ilícitos praticados por qualquer agente, servidor ou não, que causem prejuízos ao erário, ressalvadas as respectivas ações de ressarcimento.</p>') +
 memo('Improbidade (§ 4º): <b>SUPERIN</b> → <strong>SU</strong>spensão dos direitos políticos, <strong>PER</strong>da da função, <strong>IN</strong>disponibilidade dos bens + ressarcimento ao erário. Sem prejuízo da <strong>ação penal</strong>.', "Mnemônico:") +
 pega('<ul><li>A improbidade <b>não</b> gera “cassação” nem “perda” dos direitos políticos: gera <b>suspensão</b>.</li><li>A responsabilidade objetiva vale para pessoas jurídicas de direito público <b>e</b> para as de direito privado <b>prestadoras de serviços públicos</b>. Empresa estatal que explora atividade econômica segue as regras do direito privado.</li><li>O agente só responde em regresso se agiu com <b>dolo ou culpa</b>. As responsabilidades civil, penal e administrativa do servidor são, em regra, <b>independentes</b>.</li><li>Pelo STF, são imprescritíveis as ações de ressarcimento ao erário fundadas em ato <b>doloso</b> de improbidade (Tema 897).</li></ul>'))

treino(4, [
 ("O direito de greve do servidor público será exercido nos termos e limites definidos em lei específica.","C","Art. 37, VII."),
 ("Os militares podem se sindicalizar, mas não podem fazer greve.","E","Ambos são proibidos (art. 142, § 3º, IV)."),
 ("O servidor eleito vereador, havendo compatibilidade de horários, acumula as vantagens do cargo com a remuneração do mandato.","C","Art. 38, III."),
 ("São estáveis após dois anos de efetivo exercício os servidores nomeados em virtude de concurso público.","E","São três anos (art. 41)."),
 ("Extinto o cargo, o servidor estável ficará em disponibilidade com remuneração integral.","E","A remuneração é proporcional ao tempo de serviço."),
 ("A responsabilidade civil das pessoas jurídicas de direito público pelos danos causados por seus agentes é objetiva.","C","Art. 37, § 6º.")])

# =========================================================== REVISÃO
mapa = f'''<figure><svg viewBox="0 0 640 470" width="580" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<g stroke="#9fb1cc" stroke-width="2.5" fill="none"><path d="M320 235 L150 70"/><path d="M320 235 L490 70"/><path d="M320 235 L120 235"/><path d="M320 235 L520 235"/><path d="M320 235 L150 400"/><path d="M320 235 L490 400"/></g>
<circle cx="320" cy="235" r="74" fill="{C['navy']}"/><text x="320" y="225" text-anchor="middle" fill="{C['gold']}" font-weight="900" font-size="13">ARTS. 37 A 41</text>
<text x="320" y="245" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">ADMINISTRAÇÃO</text><text x="320" y="262" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">PÚBLICA</text>
''' + "".join(
 f'<rect x="{x-100}" y="{y-40}" width="200" height="80" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x}" y="{y-16}" text-anchor="middle" font-weight="900" font-size="12.5" fill="{fg}">{t}</text>'
 + "".join(f'<text x="{x}" y="{y+4+i*15}" text-anchor="middle" font-size="10.8" fill="{C["ink"]}">{l}</text>' for i,l in enumerate(ls))
 for x,y,t,ls,fg,bg in [
  (150,62,"ESTRUTURA",["direta (órgãos) · indireta (FAES)","autarquia criada por lei;","demais: criação autorizada"],C['navy'],'#e3e9f3'),
  (490,62,"PRINCÍPIOS",["LIMPE (eficiência: EC 19/98)","nepotismo: SV 13","promoção pessoal: § 1º"],C['blue'],C['sky']),
  (112,235,"CONCURSO",["provas ou provas e títulos","até 2 anos + 1 vez igual","dentro das vagas: direito"],C['golddeep'],C['goldsoft']),
  (528,235,"CARGOS",["comissão: qualquer pessoa","confiança: só efetivos","direção, chefia, assessoramento"],C['green'],C['greensoft']),
  (150,408,"ACUMULAÇÃO",["2 professores · prof. + qualquer","2 saúde regulamentada","horários + teto (EC 138/25)"],C['red'],C['redsoft']),
  (490,408,"SERVIDOR",["estável: 3 anos + avaliação","perde: sentença, PAD, aval., despesa","§ 6º: objetiva + regresso"],C['navy'],'#e3e9f3')]) + '</svg><figcaption>Mapa conceitual do Caderno 03.</figcaption></figure>'
add('<div class="marker">§§R1§§</div><div class="unit"><span class="u">REVISÃO</span><span class="t">Véspera da prova</span></div><h1 class="big">Mapa <span class="hl">conceitual</span></h1><p class="lead">Os arts. 37 a 41 em seis blocos. Explique cada caixa em voz alta.</p>' + mapa)

add('<div class="unit"><span class="u">REVISÃO</span><span class="t">Pontos de confusão</span></div><h1 class="big">As confusões <span class="hl">mais comuns</span></h1><p class="lead">Os pares de conceitos que mais derrubam candidatos neste tema.</p>' +
 table(["Confusão","O certo é"],[
  ["Legalidade: particular x Administração","Particular: tudo o que a lei não proíbe. Administração: só o que a lei permite."],
  ["Autarquia x demais entidades","Autarquia é <b>criada</b> por lei; empresa pública, sociedade de economia mista e fundação têm a criação <b>autorizada</b>."],
  ["Órgão x entidade","Órgão não tem personalidade jurídica; entidade tem."],
  ["Validade do concurso","Até 2 anos, prorrogável <b>uma vez</b>, por <b>igual período</b>."],
  ["Cargo em comissão x função de confiança","Comissão: qualquer pessoa (com percentual mínimo de servidores). Confiança: só efetivos."],
  ["Nepotismo: até que grau?","Até o <b>3º grau</b> (tios e sobrinhos entram; primos, não)."],
  ["Acumulação","Só nas 3 combinações (2 professores; professor + <b>qualquer</b> outro cargo, desde a EC nº 138/2025; 2 de saúde), com horários compatíveis e teto."],
  ["Subteto municipal","Subsídio do <b>Prefeito</b>."],
  ["Mandato eletivo","Só o vereador acumula (com horário compatível); o Prefeito pode optar pela remuneração."],
  ["Estabilidade","<b>3 anos</b> + avaliação especial obrigatória."],
  ["Disponibilidade","Remuneração <b>proporcional</b> ao tempo de serviço."],
  ["Improbidade","<b>Suspensão</b> (não perda) dos direitos políticos."],
  ["Responsabilidade","Estado: objetiva. Agente: subjetiva, em regresso (dolo ou culpa)."]],["36%",None]))

FC = [("CONCEITO","Sentidos de Administração Pública?","Subjetivo (quem: entidades, órgãos e agentes) e objetivo (o quê: a atividade)."),
 ("ESTRUTURA","Quem compõe a administração indireta?","Autarquias, fundações públicas, empresas públicas e sociedades de economia mista (FAES)."),
 ("ESTRUTURA","Autarquia é criada ou autorizada por lei?","Criada por lei específica (art. 37, XIX)."),
 ("PRINCÍPIOS","Quais são os princípios do caput do art. 37?","Legalidade, impessoalidade, moralidade, publicidade e eficiência (LIMPE)."),
 ("PRINCÍPIOS","Qual emenda incluiu a eficiência?","EC nº 19/1998."),
 ("IMPESSOALIDADE","O que o § 1º do art. 37 proíbe?","Nomes, símbolos ou imagens que caracterizem promoção pessoal de autoridades ou servidores."),
 ("MORALIDADE","Até que grau vai o nepotismo da SV 13?","Até o 3º grau, inclusive, além de cônjuge e companheiro."),
 ("AUTOTUTELA","O que diz a Súmula 473 do STF?","A Administração anula atos ilegais e revoga os inconvenientes, ressalvada a apreciação judicial."),
 ("CONCURSO","Tipos de concurso previstos?","De provas ou de provas e títulos."),
 ("CONCURSO","Validade do concurso?","Até 2 anos, prorrogável uma vez, por igual período."),
 ("CONCURSO","Psicotécnico pode ser exigido só no edital?","Não. Só por lei (Súmula Vinculante 44)."),
 ("CARGOS","Quem exerce função de confiança?","Exclusivamente servidores ocupantes de cargo efetivo."),
 ("ACUMULAÇÃO","Quais acumulações são permitidas?","2 de professor; professor + outro de qualquer natureza (EC nº 138/2025); 2 de saúde com profissão regulamentada."),
 ("ACUMULAÇÃO","Requisitos da acumulação?","Compatibilidade de horários e respeito ao teto (art. 37, XI)."),
 ("GREVE","Como é exercido o direito de greve do servidor?","Nos termos e limites de lei específica (art. 37, VII)."),
 ("TETO","Qual o teto remuneratório geral?","O subsídio mensal de Ministro do STF."),
 ("ART. 38","Servidor eleito prefeito: o que acontece?","É afastado do cargo e pode optar pela remuneração."),
 ("ART. 40","Idade da aposentadoria compulsória?","75 anos, na forma da LC nº 152/2015."),
 ("ESTABILIDADE","Requisitos da estabilidade?","Concurso, cargo efetivo, 3 anos de exercício e avaliação especial de desempenho."),
 ("ESTABILIDADE","Hipóteses de perda do cargo pelo estável?","Sentença transitada, PAD, avaliação periódica (LC) e excesso de despesa (art. 169, § 4º)."),
 ("ART. 41","O que é reintegração?","Retorno do estável ao cargo após a anulação judicial da demissão."),
 ("ART. 41","Remuneração na disponibilidade?","Proporcional ao tempo de serviço."),
 ("RESPONSABILIDADE","Responsabilidade do Estado (§ 6º)?","Objetiva, com direito de regresso contra o agente nos casos de dolo ou culpa."),
 ("IMPROBIDADE","Consequências da improbidade?","Suspensão dos direitos políticos, perda da função, indisponibilidade dos bens e ressarcimento ao erário.")]
def fcpage(items, first):
    cs = "".join(f'<div class="c"><div class="f"><small>{a}</small>{q}</div><div class="b">{r}</div></div>' for a,q,r in items)
    h = ('<div class="marker">§§R2§§</div><div class="unit"><span class="u">REVISÃO ATIVA</span></div><h1 class="big">Flash<span class="hl">cards</span></h1><p class="lead">Cubra a resposta, tente lembrar e confira. Revise em 1, 3, 7, 15 e 30 dias.</p>' if first else '')
    return h + f'<div class="fc">{cs}</div>'
add(fcpage(FC[:12], True)); add(fcpage(FC[12:], False))

Q = [
 ("Conceito","Em seu sentido objetivo, a expressão administração pública designa:",
  ["o conjunto de órgãos e entidades que compõem o Estado.","a atividade administrativa exercida pelo Estado, como a prestação de serviços públicos e o poder de polícia.","apenas o Poder Executivo federal.","os agentes políticos eleitos.","exclusivamente as empresas estatais."],"B",
  "O sentido objetivo (material ou funcional) refere-se à atividade. A descreve o sentido subjetivo; C, D e E restringem indevidamente o conceito.","Subjetivo = quem; objetivo = o quê."),
 ("Estrutura","Nos termos do art. 37, XIX, da Constituição, é correto afirmar que:",
  ["a empresa pública é criada diretamente por lei específica.","somente por lei específica poderá ser criada autarquia.","a sociedade de economia mista dispensa autorização legal.","a autarquia tem sua criação apenas autorizada por lei.","fundações dispensam lei complementar para definir sua área de atuação."],"B",
  "Autarquia é criada por lei específica; empresa pública, sociedade de economia mista e fundação têm a criação autorizada. Cabe à lei complementar definir as áreas de atuação das fundações.","Autarquia: criada. Demais: autorizadas."),
 ("Estrutura","A criação, pela prefeitura, de uma nova Secretaria Municipal de Segurança, sem personalidade jurídica própria, é exemplo de:",
  ["descentralização por outorga.","desconcentração.","criação de entidade da administração indireta.","delegação a particular.","autarquia municipal."],"B",
  "A distribuição de competências dentro da mesma pessoa jurídica, com a criação de órgão, é desconcentração. A descentralização transfere a outra pessoa jurídica.","Órgão = desconcentração; entidade = descentralização."),
 ("LIMPE","São princípios expressos no caput do art. 37 da Constituição:",
  ["legalidade, razoabilidade, moralidade, publicidade e eficiência.","legalidade, impessoalidade, moralidade, publicidade e eficiência.","legalidade, impessoalidade, motivação, publicidade e eficiência.","supremacia do interesse público, impessoalidade, moralidade, publicidade e eficiência.","legalidade, impessoalidade, moralidade, proporcionalidade e eficiência."],"B",
  "LIMPE. Razoabilidade, motivação, supremacia do interesse público e proporcionalidade são princípios implícitos na CF.","LIMPE."),
 ("Legalidade","Um servidor municipal concedeu a um colega uma licença remunerada de 60 dias não prevista em nenhuma lei, alegando que “a lei não proíbe”. A conduta:",
  ["é válida, pois ao servidor é permitido fazer tudo o que a lei não proíbe.","é válida, se houver concordância do chefe imediato.","viola o princípio da legalidade, pois a Administração só pode fazer o que a lei permite.","viola apenas o princípio da publicidade.","é válida por força do princípio da eficiência."],"C",
  "Na Administração, a legalidade significa agir apenas quando a lei autoriza. A regra “tudo o que a lei não proíbe” vale para o particular.","Administração: só o que a lei permite."),
 ("Impessoalidade","O prefeito determinou que todas as placas de obras do município exibissem sua fotografia e o slogan “Gestão Fulano: trabalho que transforma”. A medida viola, de modo mais direto, o princípio da:",
  ["legalidade.","impessoalidade.","eficiência.","publicidade, apenas porque a placa não informa o custo da obra.","continuidade do serviço público."],"B",
  "O art. 37, § 1º, proíbe nomes, símbolos ou imagens que caracterizem promoção pessoal na publicidade oficial, expressão da impessoalidade.","Promoção pessoal → impessoalidade (§ 1º)."),
 ("Moralidade","A autoridade nomeante de um órgão estadual nomeou, para cargo em comissão de assessor, o próprio sobrinho. À luz da Súmula Vinculante 13, a nomeação:",
  ["é válida, pois o sobrinho é parente de 4º grau.","é válida, pois cargos em comissão são de livre nomeação.","viola a Constituição, pois o sobrinho é parente de 3º grau.","só seria inválida se o sobrinho não tivesse formação superior.","é válida se aprovada pela Assembleia Legislativa."],"C",
  "A SV 13 alcança parentes até o 3º grau, inclusive; o sobrinho é parente colateral de 3º grau. A livre nomeação não afasta a moralidade e a impessoalidade.","Nepotismo: até o 3º grau."),
 ("Publicidade","Sobre o princípio da publicidade, assinale a alternativa correta.",
  ["É absoluto e não admite sigilo.","A divulgação nominal da remuneração dos servidores em sítio oficial viola a intimidade, segundo o STF.","Admite exceções, como o sigilo imprescindível à segurança da sociedade e do Estado.","Autoriza a inclusão do nome do governante na publicidade oficial.","Aplica-se apenas à administração direta."],"C",
  "O sigilo é admitido excepcionalmente (art. 5º, XXXIII). O STF considera legítima a divulgação nominal da remuneração (ARE 652.777). O § 1º proíbe a promoção pessoal. O princípio alcança a direta e a indireta.","Regra: transparência. Exceção: sigilo justificado."),
 ("Eficiência","O princípio da eficiência:",
  ["consta do texto original da Constituição de 1988.","foi incluído no art. 37 pela Emenda Constitucional nº 19/1998.","autoriza o administrador a afastar a lei para alcançar melhores resultados.","aplica-se somente às empresas estatais.","substituiu o princípio da legalidade."],"B",
  "A eficiência foi acrescentada pela EC nº 19/1998 e convive com os demais princípios, sem autorizar o descumprimento da lei.","Eficiência: EC nº 19/1998."),
 ("Autotutela","Constatando que uma nomeação foi feita sem concurso público, a própria Administração a anulou. Essa atuação decorre do princípio da:",
  ["autotutela.","publicidade.","continuidade.","especialidade.","tutela jurisdicional."],"A",
  "Pela autotutela (Súmula 473 do STF), a Administração anula seus atos ilegais e revoga os inconvenientes, ressalvada a apreciação judicial.","Autotutela: anula o ilegal, revoga o inconveniente."),
 ("Concurso","A respeito do concurso público, é correto afirmar que:",
  ["pode ser realizado apenas com prova de títulos.","a investidura em cargo em comissão declarado em lei de livre nomeação e exoneração depende de concurso.","a investidura em cargo ou emprego público depende de aprovação prévia em concurso de provas ou de provas e títulos.","empresas públicas estão dispensadas de concurso.","o exame psicotécnico pode ser exigido apenas com base no edital."],"C",
  "Art. 37, II. Não existe concurso só de títulos; cargos em comissão são a exceção; empresas públicas fazem concurso para emprego; o psicotécnico exige lei (SV 44).","Provas ou provas e títulos."),
 ("Validade","O edital de um concurso fixou a validade em um ano. Nos termos da Constituição, essa validade:",
  ["não pode ser prorrogada.","pode ser prorrogada uma vez, por mais um ano.","pode ser prorrogada uma vez, por mais dois anos.","pode ser prorrogada duas vezes, por mais seis meses cada.","é automaticamente de dois anos."],"B",
  "A validade é de até dois anos, prorrogável uma vez, por igual período: 1 ano + 1 ano.","Prorrogação: uma vez, por igual período."),
 ("Nomeação","Segundo o entendimento do STF, o candidato aprovado dentro do número de vagas previsto no edital:",
  ["tem mera expectativa de direito à nomeação.","tem direito subjetivo à nomeação durante o prazo de validade, salvo situações excepcionais devidamente motivadas.","só tem direito se houver nova lei criando o cargo.","perde o direito se a Administração abrir novo concurso.","tem direito à nomeação imediata após a homologação."],"B",
  "O STF (RE 598.099) reconhece direito subjetivo à nomeação do aprovado dentro das vagas, durante a validade, ressalvadas situações excepcionais, supervenientes e motivadas.","Dentro das vagas: direito subjetivo."),
 ("Cargos","As funções de confiança:",
  ["podem ser ocupadas por qualquer pessoa, sem vínculo com a Administração.","são exercidas exclusivamente por servidores ocupantes de cargo efetivo e destinam-se a direção, chefia e assessoramento.","destinam-se a atividades técnicas e operacionais.","dependem de concurso específico.","conferem estabilidade após três anos."],"B",
  "Art. 37, V. Quem pode ocupar cargo em comissão é qualquer pessoa, respeitado o percentual mínimo legal de servidores de carreira.","Função de confiança: só efetivos."),
 ("Cargos","Lei municipal criou 40 cargos em comissão de “motorista” e “digitador”, de livre nomeação e exoneração. Essa lei é:",
  ["válida, pois o Município tem autonomia para criar cargos.","inconstitucional, pois cargos em comissão destinam-se apenas a direção, chefia e assessoramento.","válida, desde que os ocupantes tenham ensino médio.","válida, se houver previsão orçamentária.","inconstitucional apenas quanto aos digitadores."],"B",
  "Atribuições técnicas ou burocráticas devem ser exercidas por cargos efetivos, providos por concurso. Cargo em comissão é só para direção, chefia e assessoramento.","Comissão: direção, chefia, assessoramento."),
 ("Acumulação","É permitida a acumulação remunerada, havendo compatibilidade de horários e observado o teto:",
  ["de dois cargos técnicos.","de um cargo de professor com outro de qualquer natureza.","de dois cargos administrativos de nível médio.","de um cargo de policial com outro de guarda municipal.","de três cargos de professor."],"B",
  "Art. 37, XVI, “b”, com a redação da EC nº 138/2025 (antes: “outro técnico ou científico”). As demais combinações não estão entre as exceções; e as exceções permitem acumular dois cargos, não três.","2 professores · professor + qualquer outro cargo · 2 saúde."),
 ("Acumulação","A proibição constitucional de acumular cargos públicos:",
  ["alcança apenas a administração direta.","estende-se a empregos e funções e abrange autarquias, fundações, empresas públicas, sociedades de economia mista, suas subsidiárias e sociedades controladas pelo poder público.","não se aplica às empresas públicas.","só se aplica a cargos do mesmo ente federativo.","admite qualquer acumulação, desde que haja compatibilidade de horários."],"B",
  "Art. 37, XVII. A compatibilidade de horários só permite a acumulação nas hipóteses do inciso XVI.","A vedação alcança direta e indireta."),
 ("Greve","Sobre os direitos coletivos dos servidores, assinale a alternativa correta.",
  ["O direito de greve será exercido nos termos de lei complementar.","Ao servidor público civil é garantido o direito à livre associação sindical.","Os militares podem fazer greve, desde que mantenham 30% do efetivo.","O servidor público não tem direito de greve.","A greve dos servidores dispensa qualquer regulamentação."],"B",
  "Art. 37, VI. A greve depende de lei específica (VII), não complementar; militares não podem fazer greve nem se sindicalizar.","Sindicalização: servidor civil. Greve: lei específica."),
 ("Teto","No âmbito dos Municípios, o limite remuneratório (subteto) aplicável aos servidores é o subsídio:",
  ["do Governador do Estado.","do Prefeito.","dos Vereadores.","do Presidente da Câmara Municipal.","de Ministro do STF."],"B",
  "Art. 37, XI: nos Municípios, o subteto é o subsídio do Prefeito. O teto geral é o subsídio de Ministro do STF.","Município: Prefeito."),
 ("Art. 38","Servidor público estadual foi eleito vereador e há compatibilidade de horários. Nos termos do art. 38, ele:",
  ["deve ser afastado do cargo, sem remuneração.","deve optar entre a remuneração do cargo e a do mandato.","perceberá as vantagens do cargo, sem prejuízo da remuneração do cargo eletivo.","perderá o cargo efetivo.","só poderá exercer o mandato após a aposentadoria."],"C",
  "Art. 38, III. A opção pela remuneração é a regra do Prefeito (e do vereador sem compatibilidade de horários).","Vereador com horário compatível: acumula."),
 ("Estabilidade","São requisitos para a aquisição da estabilidade pelo servidor público:",
  ["nomeação para cargo em comissão e dois anos de exercício.","aprovação em concurso, nomeação para cargo efetivo, três anos de efetivo exercício e aprovação em avaliação especial de desempenho.","contratação temporária por mais de três anos.","emprego público em sociedade de economia mista por três anos.","três anos de exercício, dispensada a avaliação de desempenho."],"B",
  "Art. 41, caput e § 4º. Comissionados, temporários e empregados públicos não adquirem a estabilidade do art. 41; a avaliação especial é obrigatória.","Concurso + efetivo + 3 anos + avaliação."),
 ("Perda do cargo","O servidor público estável NÃO perderá o cargo:",
  ["em virtude de sentença judicial transitada em julgado.","mediante processo administrativo com ampla defesa.","mediante avaliação periódica de desempenho, na forma de lei complementar.","por decisão discricionária do chefe do Poder Executivo, sem processo.","para adequação ao limite de despesa com pessoal, nos termos do art. 169, § 4º."],"D",
  "As hipóteses de perda são as do art. 41, § 1º, e a do art. 169, § 4º. A dispensa discricionária, sem processo, é incompatível com a estabilidade.","Estável: sentença, PAD, avaliação, despesa."),
 ("Reintegração","Invalidada por sentença judicial a demissão de servidor estável, ele será reintegrado. O eventual ocupante da vaga, se estável, será:",
  ["demitido.","reconduzido ao cargo de origem, sem direito a indenização, aproveitado em outro cargo ou posto em disponibilidade.","indenizado e exonerado.","mantido no cargo, criando-se nova vaga para o reintegrado.","aposentado compulsoriamente."],"B",
  "Art. 41, § 2º. A recondução ocorre sem direito a indenização, e a disponibilidade é com remuneração proporcional ao tempo de serviço.","Reintegra o demitido; reconduz o ocupante."),
 ("Responsabilidade","Viatura da Guarda Municipal, em serviço, colidiu com o carro de um particular. Segundo a Constituição e o entendimento do STF:",
  ["o particular deve processar diretamente o guarda, provando sua culpa.","o Município responde objetivamente, com direito de regresso contra o guarda em caso de dolo ou culpa.","o Município só responde se ficar provada a culpa do guarda.","não há responsabilidade, pois o guarda estava em serviço.","o guarda responde objetivamente e o Município subsidiariamente."],"B",
  "Art. 37, § 6º: responsabilidade objetiva do ente, com regresso contra o agente nos casos de dolo ou culpa. Pelo STF (Tema 940), a ação deve ser proposta contra o ente, e não diretamente contra o agente.","Estado: objetiva. Agente: regresso com dolo ou culpa.")]

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
add('<div class="unit"><span class="u">CORREÇÃO</span><span class="t">Treinos rápidos</span></div><h1 class="big">Respostas dos <span class="hl">treinos</span></h1><p class="lead">Certo ou errado das Unidades 1 a 4.</p>' + tr_block(TREINOS[:2]))
add(tr_block(TREINOS[2:]))

add(f'''<div class="unit"><span class="u">ENCERRAMENTO</span></div><h1 class="big">Referências e <span class="hl">verificação</span></h1><p class="lead">De onde vieram as informações.</p>
<h3>Legislação consultada (portal do Planalto)</h3>
<ul>
<li>BRASIL. <strong>Constituição Federal de 1988</strong>: arts. 37 (caput; I a XI; XV; XVI, com a redação da EC nº 138/2025; XVII; XIX; §§ 1º, 2º, 4º, 5º, 6º e 10), 38, 39 (§§ 3º e 4º), 40 (caput e § 1º) e 41, conferidos no texto compilado. Citados também os arts. 5º, 7º, 142, 169, 198 e 206 e o ADCT (art. 53).</li>
<li><strong>Lei nº 9.784/1999</strong>, art. 2º · <strong>Decreto-Lei nº 200/1967</strong>, art. 4º · <strong>Lei Complementar nº 152/2015</strong> (aposentadoria compulsória aos 75 anos).</li>
<li>Citadas sem nova conferência: Lei nº 7.783/1989 (greve), Lei nº 8.429/1992 (improbidade, alterada pela Lei nº 14.230/2021) e Lei nº 12.527/2011 (acesso à informação).</li>
</ul>
<h3>Jurisprudência citada</h3>
<ul>
<li>STF: Súmula 473 e Súmula 683; Súmulas Vinculantes 13, 43 e 44.</li>
<li>STF: RE 598.099 (direito à nomeação); ARE 652.777 (divulgação da remuneração); RE 591.874 (responsabilidade perante não usuário); Tema 940 (dupla garantia); Tema 897 (ressarcimento por improbidade dolosa); Tema 541 (greve na segurança pública); Tema 531 (desconto dos dias de greve); Temas 377 e 384 (teto e acumulação); MI 670, 708 e 712 (greve dos servidores).</li>
</ul>''' + lembre(f"""<p><strong>Material pesquisado e atualizado em: {DATA}.</strong> Os dispositivos constitucionais listados acima foram conferidos no Planalto. Emendas recentes identificadas nos arts. 37 a 41: <strong>EC nº 135/2024</strong> (art. 37, § 11), <strong>EC nº 138/2025</strong> (art. 37, XVI, “b”: professor com outro cargo de qualquer natureza) e <strong>EC nº 140/2026</strong> (art. 40, §§ 4º e 5º-A). O art. 169, § 4º, não foi conferido palavra por palavra. <strong>Limitação:</strong> os portais de jurisprudência do STF não puderam ser lidos pela ferramenta de pesquisa (o conteúdo é carregado por script). Por isso as súmulas, temas e precedentes citados reproduzem entendimentos consolidados, mas <strong>não foram reconferidos nas fontes oficiais nesta edição</strong>. Confira antes da prova e consulte o edital do seu concurso.</p>""", "Verificação e limitações"))
add('''<div class="ending"><h2>Fim do Caderno 03</h2><p style="text-align:center">Próximo caderno da coleção: <strong>Organização dos Poderes (arts. 44 a 135)</strong>.</p>
<p class="note" style="text-align:center">Mapa da Aprovação · Caderno Simplificado · Direito Constitucional · Caderno 03 · 1ª edição · novembro de 2026<br>Material de estudo independente. Não substitui a leitura da Constituição e do edital do seu concurso.</p></div>''')

doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Caderno Simplificado — Direito Constitucional — Caderno 03</title>
<link rel="stylesheet" href="estilo.css"></head><body>{symbols()}{"".join(P)}</body></html>'''
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "miolo.html"), "w").write(doc)
print("páginas planejadas:", len(P))
