"""Gera miolo.html do Caderno 01 de Direito Constitucional. Uso: python3 gerar.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from componentes import *

DATA = "25 de novembro de 2026"
P = []  # páginas
def add(html, first=False): P.append(page(f'<div class="marker">§§P{len(P)+1:03d}§§</div>' + html, first))
U1, U2, U3 = "UNIDADE 1", "UNIDADE 2", "UNIDADE 3"
T1, T2, T3 = "A Constituição", "Princípios fundamentais", "Organização do Estado"

# =========================================================== APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">Um assunto por vez, com explicações curtas, desenhos e alertas de prova.</p>
<p>Este é o <strong>Caderno 01 da coleção de Direito Constitucional</strong>. Ele trata dos fundamentos da matéria: o que é uma Constituição, como ela é classificada, a Constituição Federal de 1988, os <strong>princípios fundamentais (arts. 1º a 4º)</strong> e a <strong>organização básica do Estado brasileiro</strong>, com noções de federalismo.</p>
<p>Ele foi feito para quem está <strong>começando</strong>. Cada assunto ocupa, em geral, <strong>duas páginas</strong>:</p>
{cards([("book","Página 1 · Entenda","Título, texto da lei, <b>Traduzindo o juridiquês</b> e a faixa <b>Memorize</b>.", C['golddeep']),
        ("bulb","Página 2 · Pratique","<b>Entenda na prática</b> (esquema visual), exemplo do dia a dia e <b>Pegadinha de concurso</b>.", C['blue'])],2)}
<h3>O que cada quadro significa</h3>
{table(["Quadro","Para que serve"],[
 ["Texto da lei (creme)","Trecho oficial da Constituição. Leia com atenção: a prova copia as palavras."],
 ["Traduzindo o juridiquês","A mesma ideia explicada como numa conversa, sem palavras difíceis."],
 ["Memorize (amarelo)","A frase que precisa estar na sua cabeça no dia da prova."],
 ["Entenda na prática","Esquema visual e exemplo para enxergar a regra funcionando."],
 ["Pegadinha de concurso (vermelho)","Confusões comuns e trocas de palavras que derrubam candidatos."],
 ["Prioridade de estudo","Pontos que merecem revisão. É uma avaliação didática, <b>não</b> uma estatística de banca."]],["34%",None])}
{lembre(f'''<p><strong>Material pesquisado e atualizado em: {DATA}.</strong> Os dispositivos da Constituição citados foram conferidos no texto compilado do Planalto e não tiveram alteração de redação, exceto onde indicado. Todas as questões são <strong>autorais</strong> e nunca foram aplicadas por banca. Confira sempre o <strong>edital</strong> do seu concurso.</p>''', "Fontes e atualização")}''', first=True)

# =========================================================== SUMÁRIO (preenchido no build)
TOC = [("u","UNIDADE 1 · A CONSTITUIÇÃO","U1"),
 ("","1. O que é Constituição","A01"),("","2. Para que serve a Constituição","A02"),("","3. Supremacia constitucional","A03"),
 ("","4. Classificações das Constituições","A04"),("","5. A Constituição Federal de 1988","A05"),
 ("u","UNIDADE 2 · PRINCÍPIOS FUNDAMENTAIS (ARTS. 1º A 4º)","U2"),
 ("","6. Art. 1º: a República Federativa do Brasil","A06"),("","7. Os 5 fundamentos da República","A07"),
 ("","8. Art. 2º: separação dos Poderes (complementar)","A08"),("","9. Art. 3º: objetivos fundamentais","A09"),
 ("","10. Art. 4º: princípios das relações internacionais","A10"),("","11. Fundamentos x objetivos x princípios","A11"),
 ("u","UNIDADE 3 · ORGANIZAÇÃO DO ESTADO","U3"),
 ("","12. Forma de Estado, de governo, sistema e regime","A12"),("","13. Noções de federalismo","A13"),
 ("","14. Art. 18: os entes da Federação","A14"),("","15. União","A15"),("","16. Estados","A16"),
 ("","17. Distrito Federal","A17"),("","18. Municípios","A18"),("","19. Repartição de competências","A19"),
 ("","20. Art. 19: vedações a todos os entes","A20"),
 ("u","REVISÃO E PRÁTICA","RV"),
 ("","Mapa conceitual e resumo visual","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),
 ("","Gabarito comentado","R4"),("","Referências e plano de revisão","R5")]
toc = "".join(f'<li class="u"><span class="t">{t}</span><span class="p" data-pg="{m}"></span></li>' if k=="u"
              else f'<li><span class="t">{t}</span><span class="p" data-pg="{m}"></span></li>' for k,t,m in TOC)
add(f'''<div class="unit"><span class="u">MAPA DO CADERNO</span></div><h1 class="big">Sumário</h1>
<p class="lead">Siga a ordem: cada assunto prepara o seguinte.</p><ol class="toc">{toc}</ol>''')

def opener(num, kicker, title, items, marker):
    lis = "".join(f'<li><span>{i+1:02d}</span>{t}</li>' for i,t in enumerate(items))
    add(f'''<div class="marker">§§{marker}§§</div><div class="opener"><div class="num">{num}</div><div class="k">{kicker}</div><h1>{title}</h1><ul>{lis}</ul></div>''')

# =========================================================== UNIDADE 1
opener("01","UNIDADE 1","A Constituição",["O que é Constituição","Para que serve a Constituição","Supremacia constitucional","Classificações das Constituições","A Constituição Federal de 1988"],"U1")

# ---- 1. Conceito
add(head(U1,T1,'O que é <span class="hl">Constituição</span>?','A lei mais importante de um país: ela cria e organiza o Estado.', "A01") +
 oque('<p>Constituição é a <strong>lei fundamental e suprema</strong> de um Estado. Ela organiza o Estado (quem manda, como manda e até onde pode mandar), define a <strong>forma de governo</strong>, distribui o poder entre os órgãos e garante os <strong>direitos fundamentais</strong> das pessoas.</p>') +
 traduz('<p>Pense num prédio. Antes de qualquer regra do condomínio, existe a <strong>planta</strong>: ela diz onde ficam as paredes, quantos andares há e o que não pode ser derrubado. A Constituição é a <strong>planta do país</strong>. Todas as outras leis são construídas em cima dela e não podem contrariá-la.</p>') +
 memo('Constituição = lei <strong>suprema</strong> que <strong>organiza o Estado</strong>, <strong>limita o poder</strong> e <strong>garante direitos</strong>.') +
 '<h3>Os três sentidos clássicos de Constituição</h3>' +
 table(["Sentido","Autor","Ideia central"],[
  ["Sociológico","Ferdinand Lassalle","A Constituição real é a <b>soma dos fatores reais de poder</b>. Se o texto escrito não corresponder a eles, será só uma “folha de papel”."],
  ["Político","Carl Schmitt","A Constituição é a <b>decisão política fundamental</b> do povo (forma de Estado, de governo, direitos). O resto é “lei constitucional”."],
  ["Jurídico","Hans Kelsen","A Constituição é <b>norma jurídica pura</b>, o fundamento de validade de todo o ordenamento (topo da pirâmide)."]],["18%","20%",None]))

add(pratica_title() +
 flow([("people",["POVO","titular do poder"]),("scroll",["CONSTITUIÇÃO","escrita pelo poder","constituinte"]),("capitol",["ESTADO","organizado e","limitado"]),("shield",["DIREITOS","garantidos às","pessoas"])],
      "A Constituição nasce da vontade do povo, organiza o Estado e protege as pessoas.") +
 ex('<p>Imagine que um prefeito queira proibir, por decreto, que moradores de outra cidade entrem no município. Mesmo sendo uma autoridade eleita, ele <strong>não pode</strong>: a Constituição garante a liberdade de locomoção no território nacional (art. 5º, XV). A Constituição está <strong>acima</strong> de qualquer autoridade.</p>') +
 pega('<ul><li><strong>Lassalle → “folha de papel”</strong> e “fatores reais de poder” (sentido <b>sociológico</b>).</li><li><strong>Schmitt → “decisão política fundamental”</strong> (sentido <b>político</b>).</li><li><strong>Kelsen → norma pura, pirâmide</strong> (sentido <b>jurídico</b>).</li></ul><p>A prova costuma trocar os autores. Associe cada um à sua palavra-chave.</p>') +
 kw(["lei fundamental","organiza o Estado","limita o poder","direitos fundamentais","Lassalle: fatores reais de poder","Schmitt: decisão política","Kelsen: norma pura"]))

# ---- 2. Finalidade
add(head(U1,T1,'Para que serve a <span class="hl">Constituição</span>?','Três missões: organizar, limitar e proteger.', "A02") +
 cards([("capitol","Organizar o Estado","Define a forma de Estado, os entes federativos, os Poderes e suas funções.",C['blue']),
        ("lock","Limitar o poder","Impede abusos: separa os Poderes e diz o que o governo <b>não</b> pode fazer.",C['red']),
        ("shield","Garantir direitos","Protege direitos individuais, sociais, políticos e de nacionalidade.",C['green'])],3) +
 traduz('<p>Quando um povo cria um Estado, entrega a ele muito poder: prender, cobrar impostos, fazer leis. A Constituição é o <strong>contrato</strong> que diz como esse poder será usado e quais <strong>limites</strong> ele nunca poderá ultrapassar. É por isso que se fala em <strong>constitucionalismo</strong>: o movimento histórico de <strong>limitar o poder</strong> por meio de uma Constituição.</p>') +
 memo('A Constituição <strong>organiza</strong> o Estado, <strong>limita</strong> o poder e <strong>garante</strong> direitos. Sem limitação do poder e garantia de direitos, não há Constituição no sentido moderno.') +
 lei("Declaração dos Direitos do Homem e do Cidadão (França, 1789) · art. 16",'<p>“Toda sociedade na qual a garantia dos direitos não está assegurada, nem a separação dos poderes determinada, não tem Constituição.”</p>','Tradução livre. Documento histórico, não é lei brasileira: aparece aqui para mostrar a origem da ideia.'))

add(pratica_title() +
 flow([("crown",["PODER","SEM LIMITES","absolutismo"]),("scroll",["CONSTITUIÇÃO","impõe regras"]),("scales",["PODER","LIMITADO","Estado de Direito"])],
      "O constitucionalismo transforma o poder absoluto em poder limitado pelo Direito.", colors=[(C['red'],C['redsoft']),(C['golddeep'],C['goldsoft']),(C['green'],C['greensoft'])]) +
 ex('<p>Um governador deseja ficar no cargo por 12 anos seguidos. Ele não pode simplesmente decidir isso: a Constituição limita a reeleição para um único período subsequente (art. 14, § 5º). A regra existe exatamente para <strong>limitar o poder</strong> e garantir a alternância no governo.</p>') +
 pega('<p>“A Constituição serve apenas para organizar o Estado.” <strong>Errado.</strong> Organizar é só uma das finalidades. As Constituições modernas também <strong>limitam o poder</strong> e <strong>garantem direitos fundamentais</strong>. Desconfie de alternativas com “apenas” e “somente”.</p>') +
 prio('<p>Associe sempre: <strong>constitucionalismo = limitação do poder</strong>. Essa ideia reaparece em separação dos Poderes, cláusulas pétreas e direitos fundamentais.</p>'))

# ---- 3. Supremacia
pyr = f'''<figure><svg viewBox="0 0 640 300" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<path d="M320 12 L420 102 H220 Z" fill="{C['navy']}"/><text x="320" y="72" text-anchor="middle" fill="#fff" font-weight="900" font-size="15">CF/88</text><text x="320" y="90" text-anchor="middle" fill="#cfe0f8" font-size="10">+ emendas</text>
<path d="M216 106 H424 L478 156 H162 Z" fill="{C['blue']}"/><text x="320" y="136" text-anchor="middle" fill="#fff" font-weight="800" font-size="12.5">Tratados de DH com rito de emenda</text><text x="320" y="150" text-anchor="middle" fill="#e8f1fc" font-size="10.5">(art. 5º, § 3º): força de emenda</text>
<path d="M158 160 H482 L530 204 H110 Z" fill="#5d93e6"/><text x="320" y="186" text-anchor="middle" fill="#fff" font-weight="800" font-size="12.5">Tratados de DH sem esse rito</text><text x="320" y="199" text-anchor="middle" fill="#fff" font-size="10.5">supralegais: abaixo da CF, acima das leis (STF)</text>
<path d="M106 208 H534 L586 252 H54 Z" fill="{C['sky2']}"/><text x="320" y="236" text-anchor="middle" fill="{C['navy']}" font-weight="800" font-size="12.5">Leis (complementares, ordinárias), medidas provisórias...</text>
<path d="M50 256 H590 L630 292 H10 Z" fill="{C['sky']}"/><text x="320" y="279" text-anchor="middle" fill="{C['navy']}" font-weight="700" font-size="12">Decretos, portarias, resoluções (atos infralegais)</text>
</svg><figcaption>Pirâmide normativa simplificada: tudo o que está abaixo deve respeitar o que está acima.</figcaption></figure>'''
add(head(U1,T1,'Supremacia <span class="hl">constitucional</span>','A Constituição está no topo. Nada pode contrariá-la.', "A03") +
 oque('<p><strong>Supremacia constitucional</strong> significa que a Constituição ocupa o <strong>topo do ordenamento jurídico</strong>. Todas as leis e atos do poder público retiram dela sua validade. Uma norma que contrarie a Constituição é <strong>inconstitucional</strong> e pode ser retirada do sistema pelo <strong>controle de constitucionalidade</strong>.</p>') +
 pyr +
 traduz('<p>A Constituição é a “chefe” de todas as normas. Se uma lei manda uma coisa e a Constituição manda outra, <strong>vale a Constituição</strong>, e a lei pode ser declarada inconstitucional pelo Judiciário.</p>') +
 memo('Supremacia → <strong>rigidez</strong> (mudar a CF é mais difícil) → <strong>controle de constitucionalidade</strong> (o que contraria a CF é invalidado).'))

add(pratica_title() +
 flow([("doc",["LEI NOVA","aprovada pelo","Legislativo"]),("scales",["CONFRONTO","com a CF"]),("check",["COMPATÍVEL","continua","válida"]),("xmark",["INCOMPATÍVEL","é declarada","inconstitucional"])],
      "A Constituição é o parâmetro: toda norma é medida por ela.", colors=[(C['blue'],C['sky']),(C['golddeep'],C['goldsoft']),(C['green'],C['greensoft']),(C['red'],C['redsoft'])]) +
 ex('<p>Uma lei estadual cria pena de prisão para quem não pagar o IPVA. Essa lei é inconstitucional por dois motivos: legislar sobre direito penal é competência privativa da União (art. 22, I), e a Constituição proíbe a prisão civil por dívida (art. 5º, LXVII); hoje só se admite a do devedor de pensão alimentícia, já que o STF afastou a do depositário infiel (Súmula Vinculante 25). A supremacia da CF permite ao Judiciário afastar essa lei.</p>') +
 '<h3>Por que a Constituição é difícil de mudar?</h3><p>Porque ela é <strong>rígida</strong>. Uma lei ordinária é aprovada por maioria simples. Já uma <strong>emenda constitucional</strong> precisa ser discutida e votada em cada Casa do Congresso, <strong>em dois turnos</strong>, e aprovada por <strong>três quintos</strong> dos votos dos membros (art. 60, § 2º). Essa dificuldade protege a supremacia.</p>' +
 pega('<p>Tratado internacional de direitos humanos <strong>só</strong> tem força de emenda constitucional se aprovado em cada Casa do Congresso, em <strong>dois turnos</strong>, por <strong>três quintos</strong> dos votos (art. 5º, § 3º, incluído pela EC nº 45/2004). Sem esse rito, o STF o considera <strong>supralegal</strong> (abaixo da CF e acima das leis). Não diga que “todo tratado de direitos humanos é emenda constitucional”.</p>') +
 kw(["topo do ordenamento","fundamento de validade","rigidez","controle de constitucionalidade","3/5 em dois turnos","supralegal"]))

# ---- 4. Classificações (3 páginas)
add(head(U1,T1,'Classificações das <span class="hl">Constituições</span>','As “etiquetas” que a doutrina usa para descrever uma Constituição.', "A04") +
 traduz('<p>Classificar é colocar <strong>etiquetas</strong>. Assim como uma pessoa pode ser descrita pela altura, pela idade e pela cidade onde nasceu, uma Constituição é descrita pela <strong>origem</strong> (quem a fez), pela <strong>forma</strong>, pela <strong>extensão</strong>, pela <strong>estabilidade</strong> etc. A prova pede que você saiba as etiquetas e, principalmente, <strong>quais se aplicam à CF/88</strong>.</p>') +
 '<h3>1. Quanto à origem: quem fez?</h3>' +
 table(["Tipo","Como nasce","Exemplo no Brasil"],[
  ["Promulgada<br>(democrática, popular)","Elaborada por uma <b>Assembleia Constituinte</b> eleita pelo povo.","1891, 1934, 1946 e <b>1988</b>"],
  ["Outorgada<br>(imposta)","Imposta pelo governante, <b>sem participação popular</b>.","1824 e 1937; a doutrina também aponta 1967 e a EC nº 1/1969"],
  ["Cesarista<br>(bonapartista)","Feita pelo governante e depois submetida a <b>plebiscito ou referendo</b> apenas para ratificar.","Não há exemplo consensual no Brasil"],
  ["Pactuada<br>(dualista)","Resulta de um <b>acordo</b> entre duas forças (por exemplo, rei e Parlamento).","Exemplo clássico: Magna Carta inglesa (1215)"]],["22%",None,"30%"]) +
 '<h3>2. Quanto à forma</h3>' +
 table(["Tipo","Característica"],[
  ["Escrita","Reunida em um documento solene, elaborado de uma só vez. Ex.: CF/88."],
  ["Não escrita (costumeira)","Formada por costumes, jurisprudência e textos esparsos. Ex.: Inglaterra."]],["30%",None]) +
 memo('Promulgada = <strong>povo participa</strong> (Assembleia Constituinte). Outorgada = <strong>imposta</strong> pelo governante.'))

add(head(U1,T1,'Classificações <span class="hl">(continuação)</span>','Extensão, elaboração, estabilidade e conteúdo.') +
 '<h3>3. Quanto à extensão</h3>' +
 table(["Tipo","Característica"],[["Sintética (concisa)","Poucos artigos, só o essencial. Ex.: Constituição dos EUA."],["Analítica (prolixa)","Longa e detalhada, trata de muitos assuntos. Ex.: <b>CF/88</b>."]],["30%",None]) +
 '<h3>4. Quanto ao modo de elaboração</h3>' +
 table(["Tipo","Característica"],[["Dogmática","Escrita de uma vez, com os <b>dogmas</b> (ideias) do momento. Ex.: <b>CF/88</b>."],["Histórica","Formada lentamente, ao longo do tempo (costumeira). Ex.: Inglaterra."]],["30%",None]) +
 '<h3>5. Quanto à estabilidade (alterabilidade)</h3>' +
 flow([("lock",["IMUTÁVEL","não pode","ser alterada"]),("shield",["RÍGIDA","processo mais","difícil que lei"]),("layers",["SEMIRRÍGIDA","parte rígida,","parte flexível"]),("pen",["FLEXÍVEL","alterada como","lei comum"])],
      "Da mais difícil para a mais fácil de alterar. A CF/88 é rígida.", colors=[(C['navy'],'#e3e9f3'),(C['blue'],C['sky']),(C['golddeep'],C['goldsoft']),(C['green'],C['greensoft'])]) +
 '<p>A Constituição de <strong>1824</strong> é o exemplo brasileiro de <strong>semirrígida</strong> (art. 178 daquela Constituição). Parte da doutrina (Alexandre de Moraes) chama a CF/88 de <strong>super-rígida</strong>, porque, além de rígida, tem um núcleo que não pode ser abolido: as <strong>cláusulas pétreas</strong> (art. 60, § 4º).</p>' +
 '<h3>6. Quanto ao conteúdo</h3>' +
 table(["Tipo","Característica"],[["Material","O que importa é o <b>assunto</b>: é constitucional a norma que trata de organização do Estado, Poderes e direitos, esteja onde estiver."],["Formal","O que importa é a <b>forma</b>: é constitucional tudo o que está no texto da Constituição, qualquer que seja o assunto. A <b>CF/88</b> é formal."]],["30%",None]))

add(head(U1,T1,'O “RG” da <span class="hl">CF/88</span>','Como a doutrina majoritária classifica a Constituição de 1988.') +
 table(["Critério","CF/88 é...","Por quê"],[
  ["Origem","<b>Promulgada</b>","Feita por Assembleia Nacional Constituinte eleita."],
  ["Forma","<b>Escrita</b>","Está num documento único e solene."],
  ["Extensão","<b>Analítica</b>","É extensa e detalhada."],
  ["Elaboração","<b>Dogmática</b>","Foi escrita de uma vez, com as ideias da época."],
  ["Estabilidade","<b>Rígida</b> (para parte da doutrina, super-rígida)","Emenda exige 3/5 em dois turnos; há cláusulas pétreas."],
  ["Conteúdo","<b>Formal</b>","Tudo o que está no texto tem status constitucional."],
  ["Ideologia","<b>Eclética</b> (pluralista)","Concilia ideias diferentes (livre iniciativa e valor social do trabalho, por exemplo)."],
  ["Finalidade","<b>Dirigente</b>","Traça programas e metas para o Estado (ex.: objetivos do art. 3º)."]],["20%","30%",None]) +
 memo('<b>PEDRA FED</b> → <strong>P</strong>romulgada, <strong>E</strong>scrita, <strong>D</strong>ogmática, <strong>R</strong>ígida, <strong>A</strong>nalítica · <strong>F</strong>ormal, <strong>E</strong>clética, <strong>D</strong>irigente. Imagine a CF/88 como uma <strong>pedra</strong> firme da <strong>Fed</strong>eração.', "Mnemônico:") +
 pega('<ul><li>“A CF/88 é <b>flexível</b>” ou “<b>semirrígida</b>” → <strong>errado</strong>: ela é rígida.</li><li>“A CF/88 é <b>sintética</b>” → <strong>errado</strong>: ela é analítica.</li><li>Quanto à classificação ontológica de Loewenstein (normativa, nominal ou semântica), <strong>há divergência</strong> na doutrina sobre a CF/88. Não marque como “pacífico”.</li></ul>') +
 kw(["promulgada","outorgada","cesarista","escrita","analítica","dogmática","rígida","super-rígida","formal","dirigente"]))

# ---- 5. CF/88
timeline = f'''<figure><svg viewBox="0 0 640 170" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<line x1="20" y1="70" x2="625" y2="70" stroke="{C['ink']}" stroke-width="4"/>
''' + "".join(
 f'<circle cx="{x}" cy="70" r="{15 if y=="1988" else 11}" fill="{col}"/><text x="{x}" y="{40}" text-anchor="middle" font-weight="900" font-size="{15 if y=="1988" else 13}" fill="{C["ink"]}">{y}</text>'
 f'<text x="{x}" y="100" text-anchor="middle" font-size="10.5" font-weight="800" fill="{col}">{t1}</text><text x="{x}" y="115" text-anchor="middle" font-size="10" fill="{C["muted"]}">{t2}</text><text x="{x}" y="129" text-anchor="middle" font-size="10" fill="{C["muted"]}">{t3}</text>'
 for x,y,col,t1,t2,t3 in [(45,"1824",C['red'],"OUTORGADA","Império","semirrígida"),(130,"1891",C['green'],"PROMULGADA","1ª republicana","federação"),
   (215,"1934",C['green'],"PROMULGADA","direitos","sociais"),(300,"1937",C['red'],"OUTORGADA","Estado Novo","“Polaca”"),
   (385,"1946",C['green'],"PROMULGADA","redemocra-","tização"),(470,"1967",C['red'],"OUTORGADA*","regime","militar"),(575,"1988",C['blue'],"PROMULGADA","“Constituição","Cidadã”")]) + f'''
<text x="320" y="160" text-anchor="middle" font-size="10" fill="{C['muted']}">* Há quem classifique 1967 como “semioutorgada”. A EC nº 1/1969 é tratada por parte da doutrina como uma nova Constituição (outorgada).</text>
</svg><figcaption>Linha do tempo das Constituições brasileiras.</figcaption></figure>'''
add(head(U1,T1,'A Constituição Federal de <span class="hl">1988</span>','A “Constituição Cidadã”, que marcou a volta da democracia.', "A05") +
 '<p>A CF/88 foi <strong>promulgada em 5 de outubro de 1988</strong> pela Assembleia Nacional Constituinte, depois de mais de duas décadas de regime militar. O presidente da Constituinte, Ulysses Guimarães, chamou-a de <strong>“Constituição Cidadã”</strong>, pela ênfase nos direitos fundamentais e na participação popular.</p>' + timeline +
 traduz('<p>O Brasil já teve <strong>sete</strong> Constituições. Elas se alternam entre momentos democráticos (promulgadas) e autoritários (outorgadas). A atual, de 1988, é a mais longa e detalhada da nossa história e colocou os <strong>direitos das pessoas</strong> logo no começo do texto, antes da organização do Estado.</p>') +
 memo('CF/88: <strong>promulgada em 5/10/1988</strong>, “Constituição Cidadã”. Constituições <strong>outorgadas</strong> do Brasil: <strong>1824 e 1937</strong> (a doutrina acrescenta 1967/1969).'))

estrutura = table(["Parte","Conteúdo","Artigos"],[
 ["Preâmbulo","Apresenta os valores da Constituição.","—"],
 ["Título I","Princípios Fundamentais","1º a 4º"],["Título II","Direitos e Garantias Fundamentais","5º a 17"],
 ["Título III","Organização do Estado","18 a 43"],["Título IV","Organização dos Poderes","44 a 135"],
 ["Título V","Defesa do Estado e das Instituições","136 a 144"],["Título VI","Tributação e Orçamento","145 a 169"],
 ["Título VII","Ordem Econômica e Financeira","170 a 192"],["Título VIII","Ordem Social","193 a 232"],
 ["Título IX","Disposições Constitucionais Gerais","233 a 250"],["ADCT","Ato das Disposições Constitucionais Transitórias","numeração própria"]],["18%",None,"22%"])
add(pratica_title("Como a CF/88 está organizada") + estrutura +
 pega('<p><strong>O preâmbulo não tem força normativa</strong>, segundo o STF (ADI 2.076): ele não serve de parâmetro para declarar uma lei inconstitucional e não precisa ser copiado nas Constituições estaduais. Ele tem valor de <strong>orientação</strong> para a interpretação. Lembre também: o preâmbulo menciona “sob a proteção de Deus”, mas o Estado brasileiro é <strong>laico</strong> (art. 19, I).</p>') +
 prio('<p>Saiba de cor que os <strong>Princípios Fundamentais</strong> estão nos <strong>arts. 1º a 4º</strong> e a <strong>Organização do Estado</strong> começa no <strong>art. 18</strong>. Questões de “localize o dispositivo” são comuns em provas de nível médio.</p>'))

# =========================================================== UNIDADE 2
opener("02","UNIDADE 2","Princípios fundamentais",["Art. 1º: a República Federativa do Brasil","Os 5 fundamentos (SO-CI-DI-VA-PLU)","Art. 2º: separação dos Poderes","Art. 3º: objetivos fundamentais","Art. 4º: relações internacionais","Quadro comparativo final"],"U2")

ART1 = '''<p>Art. 1º A República Federativa do Brasil, formada pela união indissolúvel dos Estados e Municípios e do Distrito Federal, constitui-se em Estado Democrático de Direito e tem como fundamentos:<br>I - a soberania;<br>II - a cidadania;<br>III - a dignidade da pessoa humana;<br>IV - os valores sociais do trabalho e da livre iniciativa;<br>V - o pluralismo político.<br>Parágrafo único. Todo o poder emana do povo, que o exerce por meio de representantes eleitos ou diretamente, nos termos desta Constituição.</p>'''
add(head(U2,T2,'Art. 1º: a República <span class="hl">Federativa</span> do Brasil','O artigo que apresenta o Brasil: quem somos e no que acreditamos.', "A06") +
 lei("Art. 1º · Constituição Federal", ART1) +
 traduz('<p>O art. 1º é a “carteira de identidade” do Brasil. Ele diz que somos uma <strong>República</strong>, que somos uma <strong>Federação</strong> (União, Estados, DF e Municípios unidos para sempre), que somos um <strong>Estado Democrático de Direito</strong> (o povo escolhe e todos obedecem às leis, inclusive o governo) e quais são os <strong>5 fundamentos</strong>, os alicerces do país.</p>') +
 memo('<strong>União indissolúvel</strong> = nenhum ente pode se separar. O poder vem do <strong>povo</strong>, exercido por <strong>representantes eleitos</strong> (democracia indireta) <strong>ou diretamente</strong>: democracia <strong>semidireta</strong> ou participativa.'))

add(pratica_title() +
 flow([("people",["POVO","titular do","poder"]),("ballot",["ELEIÇÕES","escolhe","representantes"]),("capitol",["REPRESENTANTES","decidem em","nome do povo"]),("pen",["DIRETAMENTE","plebiscito, referendo,","iniciativa popular"])],
      "Parágrafo único do art. 1º: o povo exerce o poder de forma indireta e também direta.") +
 ex('<p>Em 2005, os brasileiros foram às urnas para responder se o comércio de armas de fogo e munição deveria ser proibido. Isso foi um <strong>referendo</strong>: o povo decidindo <strong>diretamente</strong>. Nos dias normais, quem faz as leis são deputados e senadores eleitos, ou seja, o poder exercido <strong>por representantes</strong>. Os instrumentos de participação direta estão no art. 14 (plebiscito, referendo e iniciativa popular).</p>') +
 pega('<ul><li>O art. 1º fala em união indissolúvel “dos <b>Estados e Municípios e do Distrito Federal</b>”. A <b>União</b> não aparece nessa frase, e os <b>Territórios Federais</b> não são entes federativos.</li><li>Quem tem <b>soberania</b> é a <b>República Federativa do Brasil</b>. União, Estados, DF e Municípios têm <b>autonomia</b>.</li><li>A democracia brasileira é <b>semidireta</b> (participativa), e não puramente representativa.</li></ul>') +
 kw(["República","Federação","união indissolúvel","Estado Democrático de Direito","todo o poder emana do povo","democracia semidireta"]))

# ---- 7. Fundamentos
add(head(U2,T2,'Os 5 <span class="hl">fundamentos</span> da República','Os alicerces do Brasil, no art. 1º, incisos I a V.', "A07") +
 cards([("#SO","Soberania","Poder supremo dentro do território e independência perante outros países."),
        ("#CI","Cidadania","Participar da vida política e ter direitos respeitados (votar, ser votado, fiscalizar)."),
        ("#DI","Dignidade da pessoa humana","Todo ser humano tem valor próprio e não pode ser tratado como coisa. É o “valor-fonte” dos direitos."),
        ("#VA","Valores sociais do trabalho e da livre iniciativa","Valoriza quem trabalha e quem empreende, sempre com função social."),
        ("#PLU","Pluralismo político","Convivência de ideias, crenças e opiniões diferentes, não só de partidos.")],5) +
 memo('<b>SO-CI-DI-VA-PLU</b> → <strong>SO</strong>berania, <strong>CI</strong>dadania, <strong>DI</strong>gnidade da pessoa humana, <strong>VA</strong>lores sociais do trabalho e da livre iniciativa, <strong>PLU</strong>ralismo político. Leia em voz alta: “sô-ci-di-va-plu”.', "Mnemônico:") +
 traduz('<p>Os fundamentos são aquilo que o Brasil <strong>já é</strong> e não abre mão: um país <strong>soberano</strong>, de <strong>cidadãos</strong>, que respeita a <strong>dignidade</strong> das pessoas, valoriza o <strong>trabalho</strong> e a <strong>livre iniciativa</strong> e aceita a <strong>diversidade de ideias</strong>. Repare: os fundamentos são <strong>substantivos</strong>, “coisas que existem”, e não verbos.</p>'))

add(pratica_title() +
 flow([("globe",["SOBERANIA","ninguém manda","no Brasil"]),("idcard",["CIDADANIA","direitos","políticos"]),("heart",["DIGNIDADE","valor de","cada pessoa"]),("briefcase",["TRABALHO E","LIVRE INICIATIVA","emprego e negócios"]),("people",["PLURALISMO","diversidade","de ideias"])],
      "Um ícone para cada fundamento: associe a imagem à palavra.", colors=[(C['navy'],'#e3e9f3'),(C['blue'],C['sky']),(C['red'],C['redsoft']),(C['golddeep'],C['goldsoft']),(C['green'],C['greensoft'])]) +
 ex('<p><b>Dignidade:</b> o STF editou a Súmula Vinculante 11, que só admite o uso de algemas em caso de resistência, fundado receio de fuga ou perigo à integridade física, justificado por escrito. A ideia é evitar humilhação desnecessária, uma aplicação concreta da dignidade.<br><b>Pluralismo:</b> a lei não pode proibir a criação de um partido apenas porque suas ideias desagradam ao governo.</p>') +
 pega('<ul><li><b>“Valores sociais do trabalho <u>e</u> da livre iniciativa”</b> é um <b>único</b> fundamento (inciso IV). Alternativa que cite só “livre iniciativa” ou “valorização do trabalho” como fundamento isolado deve ser lida com cuidado.</li><li><b>Pluralismo político</b> ≠ pluripartidarismo: ele é mais amplo, abrange diversidade de ideias, culturas e crenças.</li><li><b>Soberania</b> é fundamento (art. 1º); <b>independência nacional</b> é princípio das relações internacionais (art. 4º). Não troque!</li></ul>') +
 kw(["SO-CI-DI-VA-PLU","soberania","cidadania","dignidade da pessoa humana","valores sociais do trabalho e da livre iniciativa","pluralismo político"]))

# ---- 8. Art 2
add(head(U2,T2,'Art. 2º: separação dos <span class="hl">Poderes</span>','Conteúdo complementar: está nos princípios fundamentais e costuma ser cobrado junto.', "A08") +
 lei("Art. 2º · Constituição Federal",'<p>Art. 2º São Poderes da União, independentes e harmônicos entre si, o Legislativo, o Executivo e o Judiciário.</p>') +
 cards([("capitol","Legislativo","Função típica: <b>legislar</b> e <b>fiscalizar</b>. Congresso Nacional (Câmara + Senado).",C['blue']),
        ("briefcase","Executivo","Função típica: <b>administrar</b> e governar. Presidente da República e ministros.",C['golddeep']),
        ("gavel","Judiciário","Função típica: <b>julgar</b>, resolvendo conflitos com base na lei.",C['red'])],3) +
 traduz('<p>O poder do Estado é <strong>um só</strong>, mas é dividido em <strong>três funções</strong> para que ninguém concentre tudo. Cada Poder fiscaliza os outros. É o sistema de <strong>freios e contrapesos</strong>: por exemplo, o Presidente pode vetar uma lei, o Congresso pode derrubar o veto e o Judiciário pode declarar a lei inconstitucional.</p>') +
 memo('Poderes <strong>independentes e harmônicos</strong> entre si. A separação dos Poderes é <strong>cláusula pétrea</strong> (art. 60, § 4º, III).') +
 pega('<p>Cada Poder também exerce, de forma <b>atípica</b>, funções dos outros: o Senado <b>julga</b> o Presidente por crime de responsabilidade; o Judiciário <b>administra</b> seus servidores; o Presidente edita <b>medidas provisórias</b>, que têm força de lei. “Independentes” não significa “isolados”.</p>'))

# ---- 9. Art 3
ART3 = '<p>Art. 3º Constituem objetivos fundamentais da República Federativa do Brasil:<br>I - construir uma sociedade livre, justa e solidária;<br>II - garantir o desenvolvimento nacional;<br>III - erradicar a pobreza e a marginalização e reduzir as desigualdades sociais e regionais;<br>IV - promover o bem de todos, sem preconceitos de origem, raça, sexo, cor, idade e quaisquer outras formas de discriminação.</p>'
add(head(U2,T2,'Art. 3º: objetivos <span class="hl">fundamentais</span>','Aonde o Brasil quer chegar: as metas da República.', "A09") +
 lei("Art. 3º · Constituição Federal", ART3) +
 traduz('<p>Se os fundamentos (art. 1º) são o que o Brasil <strong>já é</strong>, os objetivos (art. 3º) são o que o Brasil <strong>quer alcançar</strong>. Por isso todos começam com <strong>verbos</strong> de ação: construir, garantir, erradicar, reduzir, promover. São as <strong>metas</strong> que orientam as políticas públicas.</p>') +
 memo('<b>CON-GA-ER-PRO</b> → <strong>CON</strong>struir, <strong>GA</strong>rantir, <strong>ER</strong>radicar (e reduzir), <strong>PRO</strong>mover. <strong>Objetivo começa com verbo.</strong>', "Mnemônico:"))

add(pratica_title() +
 flow([("people",["CONSTRUIR","sociedade livre,","justa e solidária"]),("chart",["GARANTIR","desenvolvimento","nacional"]),("fire",["ERRADICAR","pobreza e","marginalização"]),("scales",["REDUZIR","desigualdades","sociais e regionais"]),("heart",["PROMOVER","o bem de todos,","sem preconceitos"])],
      "As metas do art. 3º: cada uma começa com um verbo.", colors=[(C['blue'],C['sky']),(C['green'],C['greensoft']),(C['red'],C['redsoft']),(C['golddeep'],C['goldsoft']),(C['navy'],'#e3e9f3')]) +
 ex('<p>Programas de transferência de renda para famílias pobres concretizam o objetivo de <b>erradicar a pobreza</b>. Incentivos fiscais para instalar indústrias no Norte e no Nordeste buscam <b>reduzir as desigualdades regionais</b>. Leis que punem a discriminação no trabalho concretizam o objetivo de <b>promover o bem de todos, sem preconceitos</b>.</p>') +
 pega('<ul><li>Atenção aos verbos: a pobreza e a marginalização devem ser <b>erradicadas</b> (eliminadas); as desigualdades devem ser <b>reduzidas</b>. A prova troca: “erradicar as desigualdades regionais” está <b>errado</b>.</li><li>O desenvolvimento é <b>nacional</b>, não “regional” nem “econômico”.</li><li>O inciso IV lista origem, raça, sexo, cor e idade, e termina com “<b>quaisquer outras formas de discriminação</b>”. A lista é <b>exemplificativa</b>.</li><li>“Dignidade da pessoa humana” é <b>fundamento</b>, não objetivo.</li></ul>') +
 kw(["construir","garantir","erradicar","reduzir","promover","sociedade livre, justa e solidária","desenvolvimento nacional","quaisquer outras formas de discriminação"]))

# ---- 10. Art 4
ART4 = '<p>Art. 4º A República Federativa do Brasil rege-se nas suas relações internacionais pelos seguintes princípios:<br>I - independência nacional; II - prevalência dos direitos humanos; III - autodeterminação dos povos; IV - não-intervenção; V - igualdade entre os Estados; VI - defesa da paz; VII - solução pacífica dos conflitos; VIII - repúdio ao terrorismo e ao racismo; IX - cooperação entre os povos para o progresso da humanidade; X - concessão de asilo político.<br>Parágrafo único. A República Federativa do Brasil buscará a integração econômica, política, social e cultural dos povos da América Latina, visando à formação de uma comunidade latino-americana de nações.</p>'
add(head(U2,T2,'Art. 4º: relações <span class="hl">internacionais</span>','Como o Brasil se comporta diante dos outros países.', "A10") +
 lei("Art. 4º · Constituição Federal", ART4) +
 traduz('<p>O art. 4º é o “código de conduta” do Brasil no mundo. São <strong>10 princípios</strong>. Decorar a lista seca é difícil, então agrupe-os em <strong>três ideias</strong>: o Brasil <strong>respeita a soberania</strong> (a sua e a dos outros), <strong>defende a paz</strong> e <strong>protege a humanidade</strong>.</p>') +
 cards([("flag","1. Soberania e respeito","Independência nacional · autodeterminação dos povos · não-intervenção · igualdade entre os Estados",C['navy']),
        ("dove","2. Paz","Defesa da paz · solução pacífica dos conflitos · repúdio ao terrorismo e ao racismo",C['blue']),
        ("heart","3. Humanidade","Prevalência dos direitos humanos · cooperação entre os povos para o progresso da humanidade · concessão de asilo político",C['red'])],3))

add(pratica_title() +
 flow([("flag",["SOBERANIA","4 princípios"]),("dove",["PAZ","3 princípios"]),("heart",["HUMANIDADE","3 princípios"]),("globe",["AMÉRICA LATINA","integração","(parágrafo único)"])],
      "4 + 3 + 3 = 10 princípios, mais a meta de integração latino-americana.", colors=[(C['navy'],'#e3e9f3'),(C['blue'],C['sky']),(C['red'],C['redsoft']),(C['green'],C['greensoft'])]) +
 ex('<p>Um jornalista estrangeiro perseguido no seu país por criticar o governo pede proteção ao Brasil. Ao conceder <b>asilo político</b>, o Brasil aplica o art. 4º, X. Quando o Brasil se recusa a apoiar uma invasão militar a outro país, aplica a <b>não-intervenção</b> e a <b>solução pacífica dos conflitos</b>.</p>') +
 pega('<ul><li>O parágrafo único fala em integração dos povos da <b>América Latina</b>, visando a uma <b>comunidade latino-americana de nações</b>. Não é “América do Sul”, “Mercosul” nem “Américas”.</li><li><b>Repúdio</b> ao terrorismo e ao racismo, não “combate” nem “tolerância zero”.</li><li><b>Independência nacional</b> (art. 4º) ≠ <b>soberania</b> (art. 1º) ≠ <b>desenvolvimento nacional</b> (art. 3º).</li><li>O texto diz “<b>prevalência</b> dos direitos humanos”, não “primazia” nem “supremacia”.</li></ul>') +
 kw(["independência nacional","prevalência dos direitos humanos","autodeterminação","não-intervenção","igualdade entre os Estados","asilo político","América Latina"]))

# ---- 11. Comparativo
add(head(U2,T2,'Fundamentos x objetivos x <span class="hl">princípios</span>','O quadro que resolve a maioria das questões sobre os arts. 1º, 3º e 4º.', "A11") +
 table(["","FUNDAMENTOS · art. 1º","OBJETIVOS · art. 3º","PRINCÍPIOS · art. 4º"],[
  ["Ideia","O que o Brasil <b>é</b> (base)","Aonde o Brasil quer <b>chegar</b> (metas)","Como o Brasil <b>age</b> no mundo"],
  ["Forma","Substantivos","<b>Verbos</b> (construir, garantir...)","Substantivos"],
  ["Quantos","5","4 incisos","10 + parágrafo único"],
  ["Mnemônico","SO-CI-DI-VA-PLU","CON-GA-ER-PRO","Soberania · Paz · Humanidade"],
  ["Exemplo","Dignidade da pessoa humana","Erradicar a pobreza","Concessão de asilo político"]],["16%","28%","28%","28%"]) +
 '<h3>Teste rápido: de qual artigo é?</h3>' +
 table(["Expressão","Resposta"],[
  ["Soberania","Art. 1º (fundamento)"],["Independência nacional","Art. 4º (princípio internacional)"],
  ["Garantir o desenvolvimento nacional","Art. 3º (objetivo)"],["Pluralismo político","Art. 1º (fundamento)"],
  ["Prevalência dos direitos humanos","Art. 4º"],["Reduzir as desigualdades sociais e regionais","Art. 3º"],
  ["Cidadania","Art. 1º"],["Cooperação entre os povos para o progresso da humanidade","Art. 4º"]],["60%",None]) +
 memo('Tem <strong>verbo</strong>? → art. 3º. Fala de <strong>outros países ou povos</strong>? → art. 4º. É uma <strong>base, um valor</strong> do país? → art. 1º.', "Truque de prova:"))

# =========================================================== UNIDADE 3
opener("03","UNIDADE 3","Organização do Estado",["Forma de Estado, de governo, sistema e regime","Noções de federalismo","Art. 18: os entes da Federação","União, Estados, DF e Municípios","Repartição de competências","Art. 19: vedações"],"U3")

# ---- 12. Formas
add(head(U3,T3,'Os 4 pilares do <span class="hl">Estado brasileiro</span>','Forma de Estado, forma de governo, sistema de governo e regime político.', "A12") +
 cards([("map","Forma de Estado","<b>FEDERAÇÃO</b><br>Como o poder se distribui no <b>território</b>.",C['navy']),
        ("flag","Forma de governo","<b>REPÚBLICA</b><br>Como se escolhe e se substitui o chefe de Estado.",C['blue']),
        ("briefcase","Sistema de governo","<b>PRESIDENCIALISMO</b><br>Como se relacionam Executivo e Legislativo.",C['golddeep']),
        ("ballot","Regime político","<b>DEMOCRÁTICO</b><br>Quem é o titular do poder: o povo.",C['green'])],2) +
 table(["Pilar","Brasil","O oposto","Característica"],[
  ["Forma de Estado","Federação","Estado unitário","Vários centros de poder com autonomia (União, Estados, DF, Municípios)."],
  ["Forma de governo","República","Monarquia","Mandato <b>temporário</b>, chefe <b>eleito</b> e que <b>responde</b> por seus atos."],
  ["Sistema de governo","Presidencialismo","Parlamentarismo","Presidente acumula chefia de <b>Estado</b> e de <b>governo</b>."],
  ["Regime político","Democracia","Autocracia","O poder emana do povo."]],["20%","17%","18%",None]))

add(pratica_title() +
 flow([("map",["FEDERAÇÃO","forma de","Estado"]),("flag",["REPÚBLICA","forma de","governo"]),("briefcase",["PRESIDENCIALISMO","sistema de","governo"]),("ballot",["DEMOCRACIA","regime","político"])],
      "Os quatro pilares, na ordem em que costumam ser cobrados.", colors=[(C['navy'],'#e3e9f3'),(C['blue'],C['sky']),(C['golddeep'],C['goldsoft']),(C['green'],C['greensoft'])]) +
 ex('<p>Em <b>21 de abril de 1993</b>, o povo brasileiro votou em um <b>plebiscito</b>, previsto no ADCT da Constituição, para escolher entre república e monarquia e entre presidencialismo e parlamentarismo. Venceram a <b>república</b> e o <b>presidencialismo</b>.</p>') +
 pega('<ul><li><b>A forma federativa de Estado é cláusula pétrea</b> (art. 60, § 4º, I). A <b>forma republicana</b> e o <b>sistema presidencialista</b> <b>não</b> estão expressamente na lista do art. 60, § 4º. A república aparece como princípio sensível (art. 34, VII, “a”), e o tema é debatido na doutrina.</li><li>Não confunda <b>forma de Estado</b> (Federação) com <b>forma de governo</b> (República).</li></ul>') +
 kw(["Federação","República","Presidencialismo","Democracia","plebiscito de 1993","forma federativa = cláusula pétrea"]))

# ---- 13. Federalismo (3 páginas)
fedconf = table(["","FEDERAÇÃO","CONFEDERAÇÃO"],[
 ["Base jurídica","Uma <b>Constituição</b>","Um <b>tratado</b> internacional"],
 ["Soberania","Só do Estado federal (o todo)","Cada Estado mantém a sua"],
 ["Membros têm","<b>Autonomia</b>","<b>Soberania</b>"],
 ["Direito de separação (secessão)","<span class=\"no\">NÃO</span> (vínculo indissolúvel)","<span class=\"yes\">SIM</span>, em regra"],
 ["Exemplo","Brasil, EUA, Alemanha","EUA entre 1781 e 1789 (Artigos da Confederação)"]],["28%",None,None])
add(head(U3,T3,'Noções de <span class="hl">federalismo</span>','Federação: vários governos dentro de um só país.', "A13") +
 oque('<p><strong>Federação</strong> é a forma de Estado em que o poder político é <strong>distribuído no território</strong> entre um governo central e governos regionais (e, no Brasil, também locais), todos com <strong>autonomia</strong>, unidos de forma <strong>indissolúvel</strong> por uma Constituição.</p>') +
 traduz('<p>Num <strong>Estado unitário</strong>, um único governo central manda em tudo (como na França). Na <strong>Federação</strong>, o país é como uma grande família: cada membro tem sua <strong>casa</strong> e suas <strong>regras</strong> (autonomia), mas todos vivem sob o mesmo teto, a Constituição, e <strong>ninguém pode sair da família</strong>.</p>') +
 '<h3>Federação x Confederação</h3>' + fedconf +
 memo('Federação → <strong>Constituição</strong>, <strong>autonomia</strong>, <strong>sem direito de secessão</strong>. Confederação → <strong>tratado</strong>, <strong>soberania</strong>, pode sair.'))

sobaut = f'''<figure><svg viewBox="0 0 640 230" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<rect x="190" y="8" width="260" height="62" rx="14" fill="{C['navy']}"/><text x="320" y="32" text-anchor="middle" fill="#fff" font-weight="900" font-size="15">REPÚBLICA FEDERATIVA DO BRASIL</text>
<text x="320" y="54" text-anchor="middle" fill="{C['gold']}" font-weight="900" font-size="14">SOBERANIA</text>
<path d="M320 70 V92 M85 92 H555 M85 92 V110 M243 92 V110 M398 92 V110 M555 92 V110" stroke="{C['ink']}" stroke-width="2.5" fill="none"/>
''' + "".join(f'<rect x="{x-68}" y="110" width="136" height="58" rx="12" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x}" y="135" text-anchor="middle" font-weight="900" font-size="14" fill="{fg}">{t}</text><text x="{x}" y="155" text-anchor="middle" font-size="11.5" font-weight="700" fill="{C["ink"]}">autonomia</text>'
 for x,t,fg,bg in [(85,"UNIÃO",C['blue'],C['sky']),(243,"ESTADOS",C['green'],C['greensoft']),(398,"DISTRITO FEDERAL",C['golddeep'],C['goldsoft']),(555,"MUNICÍPIOS",C['red'],C['redsoft'])]) + f'''
<rect x="20" y="186" width="600" height="36" rx="10" fill="#f4f6fa" stroke="{C['sky2']}"/>
<text x="320" y="209" text-anchor="middle" font-size="12" fill="{C['ink']}"><tspan font-weight="900">Autonomia</tspan> = auto-organização + autogoverno + autoadministração (+ autolegislação)</text>
</svg><figcaption>Soberania é do todo (a República); os entes federativos têm autonomia.</figcaption></figure>'''
add(head(U3,T3,'Soberania x <span class="hl">autonomia</span>','A diferença mais cobrada em federalismo.') + sobaut +
 table(["Capacidade","Significado","Exemplo"],[
  ["Auto-organização","Elaborar a própria Constituição ou Lei Orgânica.","Constituição do Estado do Piauí; Lei Orgânica de cada município."],
  ["Autogoverno","Eleger os próprios governantes.","Eleição de governador, prefeito, deputados estaduais e vereadores."],
  ["Autoadministração","Prestar os próprios serviços, com competências e recursos próprios.","O município organiza o transporte coletivo local."],
  ["Autolegislação","Fazer as próprias leis, dentro das competências.","Lei municipal sobre horário do comércio local."]],["22%",None,"34%"]) +
 pega('<p>“Os Estados-membros são <b>soberanos</b>.” <strong>Errado!</strong> No Brasil, só a <b>República Federativa do Brasil</b> é soberana. União, Estados, DF e Municípios são <b>autônomos</b> (art. 18). A <b>União</b> também não é soberana: ela apenas <b>representa</b> a República nas relações internacionais.</p>'))

add(head(U3,T3,'Características do federalismo <span class="hl">brasileiro</span>','Como a Federação brasileira nasceu e funciona.') +
 table(["Característica","O que significa no Brasil"],[
  ["Por desagregação (segregação)","Nasceu de um Estado <b>unitário</b> (o Império) que se dividiu em Estados com a República, em 1889 (formalizada na Constituição de 1891). O oposto é o federalismo <b>por agregação</b>, quando Estados soberanos se unem (EUA)."],
  ["Centrífugo","O movimento foi do centro para as partes, descentralizando o poder."],
  ["Cooperativo","Os entes atuam em <b>colaboração</b>, com competências comuns (art. 23) e concorrentes (art. 24)."],
  ["De três níveis (tricotômico)","Além da União e dos Estados, os <b>Municípios</b> também são entes federativos, o que é uma particularidade brasileira."],
  ["Indissolúvel","Não existe direito de secessão. A União pode intervir para <b>manter a integridade nacional</b> (art. 34, I)."],
  ["Cláusula pétrea","“Não será objeto de deliberação a proposta de emenda tendente a abolir: I - a forma federativa de Estado” (art. 60, § 4º, I)."]],["30%",None]) +
 flow([("crown",["IMPÉRIO","Estado unitário","(até 1889)"]),("split",["REPÚBLICA","Estado se divide","(1889/1891)"]),("grid",["FEDERAÇÃO","3 níveis","(CF/88)"])],
      "Federalismo por desagregação: do Estado unitário à Federação.", colors=[(C['red'],C['redsoft']),(C['golddeep'],C['goldsoft']),(C['blue'],C['sky'])]) +
 memo('Federação brasileira: <strong>desagregação</strong>, <strong>cooperativa</strong>, <strong>três níveis</strong> (com Municípios), <strong>indissolúvel</strong> e <strong>cláusula pétrea</strong>.'))

# ---- 14. Art 18
ART18 = '<p>Art. 18. A organização político-administrativa da República Federativa do Brasil compreende a União, os Estados, o Distrito Federal e os Municípios, todos autônomos, nos termos desta Constituição.<br>§ 1º Brasília é a Capital Federal.<br>§ 2º Os Territórios Federais integram a União, e sua criação, transformação em Estado ou reintegração ao Estado de origem serão reguladas em lei complementar.</p>'
entes = f'''<figure><svg viewBox="0 0 640 210" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<rect x="210" y="6" width="220" height="44" rx="12" fill="{C['navy']}"/><text x="320" y="33" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">ORGANIZAÇÃO POLÍTICO-ADMINISTRATIVA</text>
<path d="M320 50 V70 M85 70 H555 M85 70 V86 M243 70 V86 M398 70 V86 M555 70 V86" stroke="{C['ink']}" stroke-width="2.5" fill="none"/>
''' + "".join(f'<rect x="{x-68}" y="86" width="136" height="50" rx="12" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x}" y="116" text-anchor="middle" font-weight="900" font-size="14" fill="{fg}">{t}</text>'
 for x,t,fg,bg in [(85,"UNIÃO",C['blue'],C['sky']),(243,"ESTADOS (26)",C['green'],C['greensoft']),(398,"DISTRITO FEDERAL",C['golddeep'],C['goldsoft']),(555,"MUNICÍPIOS",C['red'],C['redsoft'])]) + f'''
<path d="M85 136 V160" stroke="{C['muted']}" stroke-width="2" stroke-dasharray="5 4"/>
<rect x="17" y="160" width="190" height="42" rx="10" fill="#fff" stroke="{C['muted']}" stroke-width="2" stroke-dasharray="6 4"/>
<text x="112" y="178" text-anchor="middle" font-weight="900" font-size="12" fill="{C['muted']}">TERRITÓRIOS FEDERAIS</text>
<text x="112" y="194" text-anchor="middle" font-size="10.5" fill="{C['muted']}">integram a União · NÃO são entes</text>
<text x="430" y="182" text-anchor="middle" font-size="12" font-weight="800" fill="{C['ink']}">Todos os 4 entes são AUTÔNOMOS</text>
</svg><figcaption>Os quatro entes federativos. Territórios, se criados, são parte da União (hoje não há nenhum).</figcaption></figure>'''
add(head(U3,T3,'Art. 18: os entes da <span class="hl">Federação</span>','Quem forma a Federação brasileira.', "A14") +
 lei("Art. 18, caput e §§ 1º e 2º · Constituição Federal", ART18) + entes +
 traduz('<p>A Federação brasileira tem <strong>quatro tipos de entes</strong>: União, Estados, DF e Municípios. Todos são <strong>autônomos</strong> e não há hierarquia entre eles: cada um manda no que a Constituição lhe atribuiu. <strong>Territórios</strong> não são entes: se forem criados, serão uma espécie de “braço” da União. Atualmente não existe nenhum.</p>'))

add(pratica_title() +
 flow([("capitol",["UNIÃO","interesse","nacional"]),("map",["ESTADOS","interesse","regional"]),("star",["DF","regional","+ local"]),("house",["MUNICÍPIOS","interesse","local"])],
      "Não há hierarquia entre os entes: cada um atua na sua área de interesse.", colors=[(C['blue'],C['sky']),(C['green'],C['greensoft']),(C['golddeep'],C['goldsoft']),(C['red'],C['redsoft'])]) +
 ex('<p>Uma lei federal não “vale mais” que uma lei municipal só por ser federal. Se o assunto é de <b>interesse local</b>, como o horário de funcionamento do comércio, a competência é do <b>Município</b> (Súmula Vinculante 38 do STF), e a União não pode invadi-la.</p>') +
 pega('<ul><li><b>Territórios Federais NÃO são entes federativos</b>: eles integram a União (art. 18, § 2º). Sua criação, transformação em Estado ou reintegração ao Estado de origem dependem de <b>lei complementar</b>.</li><li><b>Brasília é a Capital Federal</b> (art. 18, § 1º). Brasília ≠ Distrito Federal: o DF é o ente; Brasília é a capital, situada no DF.</li><li>“A União é hierarquicamente superior aos Estados” → <b>errado</b>. Os entes são autônomos, sem hierarquia.</li></ul>') +
 kw(["União","Estados","Distrito Federal","Municípios","todos autônomos","Brasília é a Capital Federal","Territórios integram a União","lei complementar"]))

# ---- 15. União
add(head(U3,T3,'<span class="hl">União</span>: o ente central','Uma pessoa jurídica com “duas caras”.', "A15") +
 oque('<p>A <strong>União</strong> é o ente federativo central, uma <strong>pessoa jurídica de direito público interno</strong>, autônoma como os demais. Mas ela tem uma função especial: <strong>representa a República Federativa do Brasil</strong> nas relações internacionais (art. 21, I).</p>') +
 f'''<figure><svg viewBox="0 0 640 170" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<circle cx="320" cy="85" r="58" fill="{C['navy']}"/><text x="320" y="82" text-anchor="middle" fill="#fff" font-weight="900" font-size="18">UNIÃO</text><text x="320" y="102" text-anchor="middle" fill="{C['gold']}" font-size="11" font-weight="800">duas faces</text>
<rect x="20" y="40" width="210" height="90" rx="14" fill="{C['sky']}" stroke="{C['blue']}" stroke-width="2.5"/>
<text x="125" y="66" text-anchor="middle" font-weight="900" font-size="13" fill="{C['blue']}">FACE INTERNA</text>
<text x="125" y="88" text-anchor="middle" font-size="11.5" fill="{C['ink']}">ente federativo autônomo,</text><text x="125" y="104" text-anchor="middle" font-size="11.5" fill="{C['ink']}">igual aos Estados, DF e</text><text x="125" y="120" text-anchor="middle" font-size="11.5" fill="{C['ink']}">Municípios (sem hierarquia)</text>
<rect x="410" y="40" width="210" height="90" rx="14" fill="{C['goldsoft']}" stroke="{C['golddeep']}" stroke-width="2.5"/>
<text x="515" y="66" text-anchor="middle" font-weight="900" font-size="13" fill="{C['golddeep']}">FACE EXTERNA</text>
<text x="515" y="88" text-anchor="middle" font-size="11.5" fill="{C['ink']}">representa a República</text><text x="515" y="104" text-anchor="middle" font-size="11.5" fill="{C['ink']}">Federativa do Brasil, que é</text><text x="515" y="120" text-anchor="middle" font-size="11.5" fill="{C['ink']}">a titular da soberania</text>
<line x1="230" y1="85" x2="262" y2="85" stroke="{C['ink']}" stroke-width="2.5"/><line x1="378" y1="85" x2="410" y2="85" stroke="{C['ink']}" stroke-width="2.5"/>
</svg></figure>''' +
 traduz('<p>Dentro do Brasil, a União é “mais um” ente, ao lado de Estados, DF e Municípios. Fora do Brasil, quando o país assina um tratado ou mantém relações com outro Estado, quem age é a União, mas <strong>em nome da República Federativa do Brasil</strong>. A soberania é da República, não da União.</p>') +
 lei("Art. 21, I · Constituição Federal",'<p>Art. 21. Compete à União:<br>I - manter relações com Estados estrangeiros e participar de organizações internacionais;</p>') +
 memo('União = <strong>pessoa jurídica de direito público interno</strong>, autônoma. Representa a RFB, que é <strong>pessoa jurídica de direito público externo</strong> e <strong>soberana</strong>.'))

add(pratica_title() +
 flow([("globe",["RELAÇÕES","EXTERIORES","art. 21, I"]),("shield",["DEFESA","NACIONAL","Forças Armadas"]),("chart",["MOEDA","emissão pelo","Banco Central"]),("gavel",["LEIS","NACIONAIS","direito penal, civil..."])],
      "Exemplos de assuntos de interesse nacional, a cargo da União.") +
 ex('<p>Quando o Brasil assina um acordo comercial com outro país, quem negocia é a União, por meio do Presidente da República e do Ministério das Relações Exteriores, mas o acordo obriga a <b>República Federativa do Brasil</b> como um todo. Já quando a União firma um convênio com o Estado do Piauí para construir uma estrada, ela age como <b>ente federativo interno</b>, em igualdade com o Estado.</p>') +
 pega('<ul><li>“A União é soberana.” → <b>errado</b>. Ela é <b>autônoma</b>; a soberania é da RFB.</li><li>“A União é pessoa jurídica de direito público externo.” → <b>errado</b>. A União é de direito público <b>interno</b>; quem tem personalidade internacional é a <b>RFB</b>.</li><li>Os bens da União estão no art. 20, e suas competências, nos arts. 21 (administrativas exclusivas) e 22 (legislativas privativas).</li></ul>') +
 kw(["pessoa jurídica de direito público interno","representa a RFB","autonomia","art. 21: competência exclusiva","art. 22: competência privativa"]))

# ---- 16. Estados
ART25 = '<p>Art. 25. Os Estados organizam-se e regem-se pelas Constituições e leis que adotarem, observados os princípios desta Constituição.<br>§ 1º São reservadas aos Estados as competências que não lhes sejam vedadas por esta Constituição.</p>'
ART18_3 = '<p>Art. 18, § 3º Os Estados podem incorporar-se entre si, subdividir-se ou desmembrar-se para se anexarem a outros, ou formarem novos Estados ou Territórios Federais, mediante aprovação da população diretamente interessada, através de plebiscito, e do Congresso Nacional, por lei complementar.</p>'
add(head(U3,T3,'<span class="hl">Estados</span>-membros','Os entes regionais: cada um com sua Constituição.', "A16") +
 lei("Art. 25, caput e § 1º · Constituição Federal", ART25) +
 traduz('<p>Cada Estado tem a sua <strong>própria Constituição</strong> (auto-organização), elege seu <strong>governador</strong> e seus <strong>deputados estaduais</strong> (autogoverno) e cuida dos assuntos de interesse <strong>regional</strong>. E tem a chamada <strong>competência remanescente</strong> (ou residual): pode tratar de tudo o que a Constituição <strong>não proibiu</strong> e não deu a outro ente.</p>') +
 memo('Estados: <strong>Constituição estadual</strong> + <strong>competência remanescente</strong> (art. 25, § 1º): o que não for vedado nem atribuído a outro ente.') +
 lei("Art. 18, § 3º · Constituição Federal · Novos Estados", ART18_3))

add(pratica_title("Como nasce um novo Estado") +
 flow([("ballot",["PLEBISCITO","população","diretamente","interessada"]),("capitol",["CONGRESSO","NACIONAL","aprova"]),("doc",["LEI","COMPLEMENTAR","federal"]),("map",["NOVO","ESTADO"])],
      "Art. 18, § 3º: plebiscito + lei complementar do Congresso Nacional.", colors=[(C['green'],C['greensoft']),(C['blue'],C['sky']),(C['golddeep'],C['goldsoft']),(C['navy'],'#e3e9f3')]) +
 ex('<p>Em 2011, foi realizado no Pará um plebiscito sobre a divisão do Estado para criar os Estados de Carajás e Tapajós. Votou a <b>população de todo o Estado do Pará</b>, e não só a das regiões que seriam separadas, e a divisão foi rejeitada. O STF entende que “população diretamente interessada” abrange a população <b>tanto da área desmembrada quanto da área remanescente</b> (ADI 2.650).</p>') +
 pega('<ul><li>Novo <b>Estado</b> → plebiscito + <b>lei complementar federal</b> (Congresso Nacional).</li><li>Novo <b>Município</b> → plebiscito + <b>lei estadual</b> (art. 18, § 4º). A prova troca as duas regras!</li><li>Os Estados têm competência <b>remanescente</b>; os Municípios, competência para assuntos de <b>interesse local</b>.</li></ul>') +
 kw(["Constituição estadual","competência remanescente","plebiscito","população diretamente interessada","lei complementar federal"]))

# ---- 17. DF
ART32 = '<p>Art. 32. O Distrito Federal, vedada sua divisão em Municípios, reger-se-á por lei orgânica, votada em dois turnos com interstício mínimo de dez dias, e aprovada por dois terços da Câmara Legislativa, que a promulgará, atendidos os princípios estabelecidos nesta Constituição.<br>§ 1º Ao Distrito Federal são atribuídas as competências legislativas reservadas aos Estados e Municípios.</p>'
add(head(U3,T3,'Distrito <span class="hl">Federal</span>','Um ente “híbrido”: metade Estado, metade Município.', "A17") +
 lei("Art. 32, caput e § 1º · Constituição Federal", ART32) +
 traduz('<p>O DF é um ente <strong>especial</strong>. Ele <strong>não pode ser dividido em Municípios</strong> e, por isso, acumula as competências legislativas de <strong>Estado e de Município</strong>. Em vez de Constituição, tem uma <strong>Lei Orgânica</strong>. O governador e os deputados distritais são eleitos pelo povo do DF, e a casa legislativa se chama <strong>Câmara Legislativa</strong>.</p>') +
 table(["","Estado","Distrito Federal","Município"],[
  ["Lei maior","Constituição estadual","Lei Orgânica","Lei Orgânica"],
  ["Chefe do Executivo","Governador","Governador","Prefeito"],
  ["Legislativo","Assembleia Legislativa","Câmara Legislativa","Câmara Municipal"],
  ["Parlamentares","Deputados estaduais","Deputados distritais","Vereadores"],
  ["Pode ter municípios?","Sim","<span class=\"no\">Não</span>","—"]],["22%",None,None,None]) +
 memo('DF = <strong>vedada a divisão em Municípios</strong> · <strong>Lei Orgânica</strong> (2 turnos, interstício de 10 dias, 2/3 da Câmara Legislativa) · competências de <strong>Estado + Município</strong>.'))

add(pratica_title() +
 flow([("map",["COMPETÊNCIAS","DE ESTADO"]),("star",["DISTRITO","FEDERAL","acumula as duas"]),("house",["COMPETÊNCIAS","DE MUNICÍPIO"])],
      "Art. 32, § 1º: o DF soma as competências legislativas estaduais e municipais.", colors=[(C['green'],C['greensoft']),(C['golddeep'],C['goldsoft']),(C['red'],C['redsoft'])]) +
 ex('<p>No DF não há prefeitos. Cidades como Taguatinga e Ceilândia são <b>regiões administrativas</b>, e não Municípios. Assim, a Câmara Legislativa pode tanto fazer uma lei sobre um assunto estadual (por exemplo, o ICMS do DF, dentro das regras constitucionais) quanto sobre um assunto local, como o funcionamento do comércio.</p>') +
 pega('<ul><li>“O DF pode ser dividido em Municípios.” → <b>errado</b>: é vedado (art. 32).</li><li>“O DF tem Constituição distrital.” → <b>errado</b>: tem <b>Lei Orgânica</b>.</li><li>“Brasília é um Município.” → <b>errado</b>: Brasília é a Capital Federal (art. 18, § 1º) e fica no DF.</li><li>O DF é ente federativo <b>autônomo</b>, mas tem autonomia parcialmente tutelada: cabe à União organizar e manter, por exemplo, a Polícia Civil, a Polícia Penal, a Polícia Militar e o Corpo de Bombeiros Militar do DF (art. 21, XIV).</li></ul>') +
 kw(["vedada a divisão em Municípios","Lei Orgânica","Câmara Legislativa","deputados distritais","competências de Estado e Município"]))

# ---- 18. Municípios
ART18_4 = '<p>Art. 18, § 4º A criação, a incorporação, a fusão e o desmembramento de Municípios, far-se-ão por lei estadual, dentro do período determinado por Lei Complementar Federal, e dependerão de consulta prévia, mediante plebiscito, às populações dos Municípios envolvidos, após divulgação dos Estudos de Viabilidade Municipal, apresentados e publicados na forma da lei.</p>'
add(head(U3,T3,'<span class="hl">Municípios</span>','Os entes locais, os mais próximos do cidadão.', "A18") +
 lei("Art. 29, caput (início) · Constituição Federal",'<p>Art. 29. O Município reger-se-á por lei orgânica, votada em dois turnos, com o interstício mínimo de dez dias, e aprovada por dois terços dos membros da Câmara Municipal, que a promulgará, atendidos os princípios estabelecidos nesta Constituição, na Constituição do respectivo Estado e os seguintes preceitos: (...)</p>') +
 lei("Art. 30, I e II · Constituição Federal",'<p>Art. 30. Compete aos Municípios:<br>I - legislar sobre assuntos de interesse local;<br>II - suplementar a legislação federal e a estadual no que couber;</p>') +
 traduz('<p>O Município é onde a vida acontece: a rua, o posto de saúde, a escola infantil, o ônibus. Por isso ele cuida dos assuntos de <strong>interesse local</strong>. Tem <strong>Lei Orgânica</strong> (e não Constituição), elege <strong>prefeito</strong> e <strong>vereadores</strong> e pode <strong>suplementar</strong> leis federais e estaduais para adaptá-las à realidade local.</p>') +
 memo('Município: <strong>Lei Orgânica</strong> (2 turnos, 10 dias, 2/3 da Câmara Municipal) · <strong>interesse local</strong> · competência <strong>suplementar</strong> “no que couber”. <strong>Não tem Poder Judiciário próprio.</strong>'))

add(pratica_title("Criação de Municípios") + lei("Art. 18, § 4º · Constituição Federal (redação da EC nº 15/1996)", ART18_4) +
 flow([("doc",["LEI COMPLEMENTAR","FEDERAL","fixa o período"]),("chart",["ESTUDOS DE","VIABILIDADE","publicados"]),("ballot",["PLEBISCITO","populações dos","Municípios envolvidos"]),("pen",["LEI","ESTADUAL","cria o Município"])],
      "Os requisitos do art. 18, § 4º, na ordem.", colors=[(C['navy'],'#e3e9f3'),(C['golddeep'],C['goldsoft']),(C['green'],C['greensoft']),(C['red'],C['redsoft'])]) +
 lembre('<p><strong>Novidade legislativa:</strong> a <strong>Lei Complementar nº 230, de 15 de abril de 2026</strong>, regulamentou o art. 18, § 4º <strong>apenas</strong> para o <strong>desmembramento de parte de um Município para incorporação a outro, limítrofe</strong>. Ela fixa o período de <strong>15 anos</strong> a partir da publicação, exige Estudo de Viabilidade Municipal e plebiscito único nos Municípios envolvidos, e proíbe expressamente que esse procedimento <strong>crie um novo Município</strong>. Para a <strong>criação de novos Municípios</strong>, a lei complementar federal que fixe o período continua pendente até a data desta verificação.</p>', "Atualização 2026") +
 pega('<ul><li>Novo Município → <b>lei estadual</b>, e não lei federal. Novo Estado → <b>lei complementar federal</b>.</li><li>O plebiscito é feito com as populações dos <b>Municípios envolvidos</b>, <b>depois</b> da divulgação dos Estudos de Viabilidade.</li><li>Município <b>não tem Judiciário</b> próprio nem representação no Senado.</li></ul>'))

# ---- 19. Competências
comp = f'''<figure><svg viewBox="0 0 640 150" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<rect x="10" y="10" width="620" height="38" rx="10" fill="{C['navy']}"/><text x="320" y="35" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">PRINCÍPIO DA PREDOMINÂNCIA DO INTERESSE</text>
''' + "".join(f'<rect x="{x}" y="62" width="145" height="78" rx="12" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x+72}" y="90" text-anchor="middle" font-weight="900" font-size="13" fill="{fg}">{t}</text><text x="{x+72}" y="112" text-anchor="middle" font-size="11.5" fill="{C["ink"]}">{a}</text><text x="{x+72}" y="128" text-anchor="middle" font-size="11.5" fill="{C["ink"]}">{b}</text>'
 for x,t,a,b,fg,bg in [(10,"UNIÃO","interesse","GERAL / NACIONAL",C['blue'],C['sky']),(168,"ESTADOS","interesse","REGIONAL",C['green'],C['greensoft']),(326,"MUNICÍPIOS","interesse","LOCAL",C['red'],C['redsoft']),(485,"DF","interesse","REGIONAL + LOCAL",C['golddeep'],C['goldsoft'])]) + '</svg></figure>'
add(head(U3,T3,'Repartição de <span class="hl">competências</span>','Noções: quem faz o quê na Federação.', "A19") +
 oque('<p><strong>Competência</strong> é a parcela de poder que a Constituição atribui a cada ente. A repartição segue o <strong>princípio da predominância do interesse</strong>: o assunto vai para o ente cujo interesse prevalece.</p>') + comp +
 table(["Artigo","Tipo","Quem","Ideia"],[
  ["Art. 21","Exclusiva (administrativa)","União","Só a União executa; <b>indelegável</b>. Ex.: emitir moeda."],
  ["Art. 22","Privativa (legislativa)","União","Só a União legisla, mas <b>lei complementar</b> pode autorizar os Estados a legislar sobre <b>questões específicas</b>. Ex.: direito penal e civil."],
  ["Art. 23","Comum (administrativa)","Todos os entes","Todos atuam juntos. Ex.: proteger o meio ambiente e cuidar da saúde."],
  ["Art. 24","Concorrente (legislativa)","União, Estados e DF","União faz <b>normas gerais</b>; Estados <b>suplementam</b>. Municípios <b>não</b> estão no caput."],
  ["Art. 25, § 1º","Remanescente","Estados","O que não for vedado nem atribuído a outros."],
  ["Art. 30, I e II","Local e suplementar","Municípios","Interesse local; suplementar leis federais e estaduais no que couber."]],["14%","22%","18%",None]))

add(pratica_title("Competência concorrente (art. 24)") +
 flow([("capitol",["UNIÃO","edita normas","gerais (§ 1º)"]),("map",["ESTADOS","suplementam","(§ 2º)"]),("doc",["SEM LEI FEDERAL","Estado legisla","de forma plena (§ 3º)"]),("stop",["LEI FEDERAL","SUPERVENIENTE","suspende a eficácia","da estadual contrária (§ 4º)"])],
      "Os quatro parágrafos do art. 24 em sequência.", colors=[(C['blue'],C['sky']),(C['green'],C['greensoft']),(C['golddeep'],C['goldsoft']),(C['red'],C['redsoft'])]) +
 ex('<p>Imagine que não exista lei federal com normas gerais sobre determinado assunto da lista do art. 24. O Estado pode legislar de forma <b>plena</b> sobre ele, para atender às suas peculiaridades. Se depois a União editar normas gerais, a lei estadual tem a eficácia <b>suspensa</b> no que for contrária a elas. Ela não é revogada.</p>') +
 pega('<ul><li>Lei federal superveniente <b>suspende a eficácia</b> da lei estadual contrária. Não “revoga”!</li><li>Os <b>Municípios não estão no caput do art. 24</b>, mas podem suplementar a legislação federal e a estadual no que couber (art. 30, II).</li><li>Competência <b>comum</b> (art. 23) é <b>administrativa</b> e inclui os Municípios; competência <b>concorrente</b> (art. 24) é <b>legislativa</b>.</li></ul>') +
 memo('Administrativas: <strong>21 exclusiva</strong> e <strong>23 comum</strong>. Legislativas: <strong>22 privativa</strong> e <strong>24 concorrente</strong>. Truque: “<strong>exclusiva não se delega, privativa se delega</strong>”.') +
 kw(["predominância do interesse","exclusiva","privativa","comum","concorrente","remanescente","normas gerais","suspende a eficácia"]))

# ---- 20. Art 19
ART19 = '<p>Art. 19. É vedado à União, aos Estados, ao Distrito Federal e aos Municípios:<br>I - estabelecer cultos religiosos ou igrejas, subvencioná-los, embaraçar-lhes o funcionamento ou manter com eles ou seus representantes relações de dependência ou aliança, ressalvada, na forma da lei, a colaboração de interesse público;<br>II - recusar fé aos documentos públicos;<br>III - criar distinções entre brasileiros ou preferências entre si.</p>'
add(head(U3,T3,'Art. 19: vedações a <span class="hl">todos os entes</span>','Três proibições que valem para União, Estados, DF e Municípios.', "A20") +
 lei("Art. 19 · Constituição Federal", ART19) +
 cards([("church","Estado laico","Nenhum ente pode criar, financiar, atrapalhar ou se aliar a igrejas, ressalvada a colaboração de interesse público.",C['blue']),
        ("doc","Fé dos documentos","Um documento público emitido por um ente vale perante os demais. Ex.: RG emitido por um Estado.",C['golddeep']),
        ("people","Igualdade federativa","Nenhum ente pode favorecer brasileiros de um lugar ou outro ente.",C['green'])],3) +
 traduz('<p>O art. 19 garante a <strong>convivência</strong> na Federação: o Estado é <strong>laico</strong> (não tem religião oficial, mas respeita todas), um documento público de qualquer ente deve ser <strong>aceito</strong> pelos outros, e ninguém pode criar <strong>privilégios</strong> por local de origem.</p>') +
 pega('<ul><li><b>Laico</b> não é “antirreligioso”: a CF admite a <b>colaboração de interesse público</b>, na forma da lei, e garante a liberdade de crença (art. 5º, VI).</li><li>Uma lei estadual que dê preferência em concurso público a quem nasceu no próprio Estado viola o art. 19, III.</li></ul>'))

# =========================================================== REVISÃO
mapa = f'''<figure><svg viewBox="0 0 640 520" width="560" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<g stroke="#9fb1cc" stroke-width="2.5" fill="none"><path d="M320 260 L150 80"/><path d="M320 260 L490 80"/><path d="M320 260 L110 260"/><path d="M320 260 L530 260"/><path d="M320 260 L150 440"/><path d="M320 260 L490 440"/><path d="M320 260 L320 470"/></g>
<circle cx="320" cy="260" r="78" fill="{C['navy']}"/><text x="320" y="248" text-anchor="middle" fill="{C['gold']}" font-weight="900" font-size="13">CADERNO 01</text>
<text x="320" y="268" text-anchor="middle" fill="#fff" font-weight="900" font-size="15">DIREITO</text><text x="320" y="286" text-anchor="middle" fill="#fff" font-weight="900" font-size="15">CONSTITUCIONAL</text>
''' + "".join(
 f'<rect x="{x-95}" y="{y-38}" width="190" height="76" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x}" y="{y-14}" text-anchor="middle" font-weight="900" font-size="13" fill="{fg}">{t}</text>'
 + "".join(f'<text x="{x}" y="{y+6+i*15}" text-anchor="middle" font-size="11" fill="{C["ink"]}">{l}</text>' for i,l in enumerate(ls))
 for x,y,t,ls,fg,bg in [
  (150,62,"CONSTITUIÇÃO",["lei suprema: organiza,","limita e garante"],C['navy'],'#e3e9f3'),
  (490,62,"CF/88 = PEDRA FED",["promulgada · escrita · dogmática","rígida · analítica..."],C['blue'],C['sky']),
  (102,260,"ART. 1º",["SO-CI-DI-VA-PLU","união indissolúvel"],C['golddeep'],C['goldsoft']),
  (538,260,"ART. 3º",["CON-GA-ER-PRO","objetivos = verbos"],C['green'],C['greensoft']),
  (150,452,"ART. 4º",["soberania · paz ·","humanidade + Am. Latina"],C['red'],C['redsoft']),
  (490,452,"FEDERAÇÃO",["autonomia ≠ soberania","indissolúvel · pétrea"],C['navy'],'#e3e9f3'),
  (320,478,"ART. 18",["União · Estados · DF · Municípios","Territórios não são entes"],C['blue'],C['sky'])]) + '</svg><figcaption>Mapa conceitual do Caderno 01.</figcaption></figure>'
add(f'<div class="marker">§§R1§§</div><div class="unit"><span class="u">REVISÃO</span><span class="t">Véspera da prova</span></div><h1 class="big">Mapa <span class="hl">conceitual</span></h1><p class="lead">Todo o caderno em um esquema. Tente explicar cada caixa em voz alta.</p>' + mapa)

add('<div class="unit"><span class="u">REVISÃO</span><span class="t">Uma linha por assunto</span></div><h1 class="big">Resumo <span class="hl">visual</span></h1><p class="lead">Leia, cubra a coluna da direita e tente lembrar.</p>' +
 table(["Assunto","O essencial"],[
  ["Constituição","Lei suprema que organiza o Estado, limita o poder e garante direitos."],
  ["Sentidos","Lassalle: sociológico (fatores reais de poder). Schmitt: político (decisão fundamental). Kelsen: jurídico (norma pura)."],
  ["Supremacia","CF no topo; rigidez (EC: 3/5, dois turnos, cada Casa); controle de constitucionalidade."],
  ["CF/88","Promulgada em 5/10/1988. PEDRA FED. Preâmbulo sem força normativa (STF)."],
  ["Art. 1º","RFB = união indissolúvel de Estados, Municípios e DF; Estado Democrático de Direito; SO-CI-DI-VA-PLU; poder do povo (direto e por representantes)."],
  ["Art. 2º","Legislativo, Executivo e Judiciário: independentes e harmônicos."],
  ["Art. 3º","Objetivos com verbos: construir, garantir, erradicar/reduzir, promover."],
  ["Art. 4º","10 princípios: soberania (4), paz (3), humanidade (3); integração da América Latina."],
  ["4 pilares","Federação, República, Presidencialismo, Democracia. Forma federativa = cláusula pétrea."],
  ["Federalismo","Desagregação, cooperativo, três níveis, indissolúvel. Soberania da RFB; entes autônomos."],
  ["Art. 18","União, Estados, DF e Municípios, todos autônomos. Brasília = capital. Territórios integram a União (LC)."],
  ["Novos entes","Estado: plebiscito + LC federal. Município: LC federal (período) + EVM + plebiscito + lei estadual."],
  ["DF","Vedada a divisão em Municípios; Lei Orgânica; competências de Estado + Município."],
  ["Competências","21 exclusiva, 22 privativa (delegável por LC), 23 comum, 24 concorrente, 25 § 1º remanescente, 30 local."],
  ["Art. 19","Estado laico; fé dos documentos públicos; sem distinções entre brasileiros."]],["20%",None]))

FC = [("CONCEITO","O que é Constituição?","Lei fundamental e suprema que organiza o Estado, limita o poder e garante direitos."),
 ("SENTIDOS","Quem definiu a Constituição como “soma dos fatores reais de poder”?","Ferdinand Lassalle (sentido sociológico)."),
 ("SENTIDOS","E como “decisão política fundamental”?","Carl Schmitt (sentido político)."),
 ("SUPREMACIA","Qual o quórum para aprovar emenda constitucional?","3/5 dos membros, em dois turnos, em cada Casa do Congresso (art. 60, § 2º)."),
 ("TRATADOS","Quando tratado de direitos humanos equivale a emenda?","Se aprovado em cada Casa, em dois turnos, por 3/5 (art. 5º, § 3º)."),
 ("CLASSIFICAÇÃO","Qual o mnemônico das classificações da CF/88?","PEDRA FED: promulgada, escrita, dogmática, rígida, analítica, formal, eclética, dirigente."),
 ("HISTÓRIA","Quais Constituições brasileiras foram outorgadas?","1824 e 1937; a doutrina também aponta 1967 e a EC nº 1/1969."),
 ("PREÂMBULO","O preâmbulo tem força normativa?","Não, segundo o STF (ADI 2.076). Serve de diretriz interpretativa."),
 ("ART. 1º","Quais são os fundamentos da República?","Soberania, cidadania, dignidade da pessoa humana, valores sociais do trabalho e da livre iniciativa, pluralismo político."),
 ("ART. 1º","Que tipo de democracia o parágrafo único consagra?","Semidireta (participativa): por representantes eleitos ou diretamente."),
 ("ART. 3º","Como reconhecer um objetivo fundamental?","Começa com verbo: construir, garantir, erradicar, reduzir, promover."),
 ("ART. 3º","Pobreza e desigualdades: erradicar ou reduzir?","Erradicar a pobreza e a marginalização; reduzir as desigualdades sociais e regionais."),
 ("ART. 4º","Integração com quais povos (parágrafo único)?","Da América Latina, visando a uma comunidade latino-americana de nações."),
 ("ART. 4º","Asilo político é fundamento, objetivo ou princípio?","Princípio das relações internacionais (art. 4º, X)."),
 ("FEDERAÇÃO","Federação x confederação: qual tem direito de secessão?","A confederação, em regra. A federação é indissolúvel."),
 ("FEDERAÇÃO","Quem é soberano no Brasil?","A República Federativa do Brasil. Os entes são autônomos."),
 ("AUTONOMIA","Quais capacidades formam a autonomia?","Auto-organização, autogoverno, autoadministração (e autolegislação)."),
 ("ART. 18","Territórios Federais são entes federativos?","Não. Integram a União; criação e transformação por lei complementar."),
 ("ESTADOS","Como se cria um novo Estado?","Plebiscito da população diretamente interessada + lei complementar do Congresso."),
 ("MUNICÍPIOS","Como se cria um novo Município?","Lei estadual, no período da LC federal, após EVM e plebiscito (art. 18, § 4º)."),
 ("DF","O DF pode ser dividido em Municípios?","Não (art. 32). Ele acumula competências de Estado e Município."),
 ("COMPETÊNCIA","Diferença entre exclusiva e privativa?","Exclusiva (art. 21) é indelegável; privativa (art. 22) pode ser delegada aos Estados por LC."),
 ("COMPETÊNCIA","Efeito da lei federal superveniente sobre normas gerais?","Suspende a eficácia da lei estadual no que lhe for contrário (art. 24, § 4º)."),
 ("ART. 19","Estado laico proíbe toda relação com igrejas?","Não. Ressalva a colaboração de interesse público, na forma da lei.")]
def fcpage(items, first):
    cs = "".join(f'<div class="c"><div class="f"><small>{a}</small>{q}</div><div class="b">{r}</div></div>' for a,q,r in items)
    h = ('<div class="marker">§§R2§§</div><div class="unit"><span class="u">REVISÃO ATIVA</span></div><h1 class="big">Flash<span class="hl">cards</span></h1><p class="lead">Cubra a resposta, tente lembrar e confira. Revise em 1, 3, 7, 15 e 30 dias.</p>' if first else '')
    return h + f'<div class="fc">{cs}</div>'
add(fcpage(FC[:12], True)); add(fcpage(FC[12:], False))

# =========================================================== QUESTÕES
Q = [
 ("Conceito","Sobre os sentidos de Constituição, assinale a alternativa correta.",
  ["Para Hans Kelsen, a Constituição é a soma dos fatores reais de poder.","Para Ferdinand Lassalle, a Constituição escrita que não corresponde aos fatores reais de poder é uma simples “folha de papel”.","Para Carl Schmitt, a Constituição é norma pura, sem relação com a política.","O sentido sociológico identifica a Constituição como decisão política fundamental.","O sentido jurídico foi formulado por Lassalle."],"B",
  "Lassalle (sentido sociológico) fala em fatores reais de poder e em “folha de papel”. A atribui a Kelsen a ideia de Lassalle; C descreve Kelsen, não Schmitt; D descreve Schmitt (sentido político); E está errada, pois o sentido jurídico é de Kelsen.","Lassalle = fatores reais de poder; Schmitt = decisão política; Kelsen = norma pura."),
 ("Supremacia","Um tratado internacional de direitos humanos foi aprovado pelo Congresso Nacional por maioria simples, em turno único. Segundo a Constituição e o entendimento do STF, esse tratado terá status:",
  ["de emenda constitucional.","de lei complementar.","supralegal, abaixo da Constituição e acima das leis.","de decreto regulamentar.","superior à Constituição."],"C",
  "Só tem equivalência a emenda o tratado de direitos humanos aprovado em cada Casa, em dois turnos, por 3/5 (art. 5º, § 3º). Sem esse rito, o STF o considera supralegal. Nenhum tratado fica acima da Constituição (E).","Tratado de DH: com rito do § 3º = emenda; sem o rito = supralegal."),
 ("Classificação","Segundo a classificação adotada pela doutrina majoritária, a Constituição Federal de 1988 é:",
  ["outorgada, escrita, sintética e flexível.","promulgada, costumeira, analítica e rígida.","promulgada, escrita, analítica e rígida.","cesarista, escrita, dogmática e semirrígida.","pactuada, escrita, sintética e rígida."],"C",
  "A CF/88 é promulgada (Assembleia Constituinte), escrita, analítica (extensa) e rígida (emenda exige processo qualificado). Não é outorgada, costumeira, sintética, flexível, semirrígida, cesarista ou pactuada.","PEDRA FED."),
 ("História","Assinale a alternativa que indica apenas Constituições brasileiras outorgadas.",
  ["1824 e 1891.","1891 e 1934.","1824 e 1937.","1934 e 1946.","1946 e 1988."],"C",
  "1824 (Império) e 1937 (Estado Novo) foram impostas sem participação popular. 1891, 1934, 1946 e 1988 foram promulgadas.","Outorgadas: 1824 e 1937 (e, para a doutrina, 1967 e a EC nº 1/1969)."),
 ("CF/88","A respeito do preâmbulo da Constituição Federal de 1988, segundo o STF, é correto afirmar que ele:",
  ["tem força normativa e serve de parâmetro para controle de constitucionalidade.","é norma de reprodução obrigatória nas Constituições estaduais.","não tem força normativa, mas serve como diretriz de interpretação.","revoga as leis que lhe forem contrárias.","só pode ser alterado por plebiscito."],"C",
  "O STF (ADI 2.076) entende que o preâmbulo não tem força normativa, não é parâmetro de controle e não é de reprodução obrigatória. Serve de orientação interpretativa.","Preâmbulo: sem força normativa."),
 ("Art. 1º","Constitui fundamento da República Federativa do Brasil, nos termos do art. 1º da Constituição:",
  ["a independência nacional.","a erradicação da pobreza.","o pluralismo político.","a prevalência dos direitos humanos.","a garantia do desenvolvimento nacional."],"C",
  "Pluralismo político é fundamento (art. 1º, V). Independência nacional (A) e prevalência dos direitos humanos (D) são princípios do art. 4º; erradicar a pobreza (B) e garantir o desenvolvimento nacional (E) são objetivos do art. 3º.","SO-CI-DI-VA-PLU."),
 ("Art. 1º","De acordo com o parágrafo único do art. 1º da Constituição, todo o poder emana do povo, que o exerce:",
  ["exclusivamente por meio de representantes eleitos.","exclusivamente de forma direta, por plebiscito.","por meio de representantes eleitos ou diretamente, nos termos da Constituição.","por meio dos partidos políticos, que são titulares do poder.","por meio do Presidente da República, chefe de Estado."],"C",
  "O texto prevê o exercício por representantes eleitos ou diretamente, o que caracteriza a democracia semidireta (participativa). As alternativas com “exclusivamente” contrariam o texto.","Democracia semidireta: representantes + participação direta."),
 ("Art. 3º","Constitui objetivo fundamental da República Federativa do Brasil:",
  ["erradicar as desigualdades sociais e regionais.","reduzir a pobreza e a marginalização.","garantir o desenvolvimento nacional.","assegurar a soberania.","promover a dignidade da pessoa humana como fundamento."],"C",
  "Garantir o desenvolvimento nacional é objetivo (art. 3º, II). O texto manda erradicar a pobreza e a marginalização e reduzir as desigualdades. A e B invertem os verbos. Soberania (D) e dignidade (E) são fundamentos.","Erradicar a pobreza; reduzir as desigualdades."),
 ("Art. 3º","O art. 3º, IV, da Constituição estabelece como objetivo promover o bem de todos, sem preconceitos de origem, raça, sexo, cor, idade e quaisquer outras formas de discriminação. Sobre essa lista, é correto afirmar que ela é:",
  ["taxativa, admitindo apenas as formas expressamente citadas.","exemplificativa, pois abrange quaisquer outras formas de discriminação.","aplicável apenas às relações de trabalho.","dirigida exclusivamente à União.","um fundamento da República."],"B",
  "A expressão “quaisquer outras formas de discriminação” torna a lista exemplificativa. O dispositivo vincula toda a República, não só a União, e trata de objetivo, não de fundamento.","Objetivos = metas da República; o inciso IV tem lista aberta."),
 ("Art. 4º","Nas relações internacionais, o Brasil rege-se, entre outros, pelo princípio da:",
  ["cidadania.","concessão de asilo político.","erradicação da marginalização.","soberania popular.","livre iniciativa."],"B",
  "A concessão de asilo político está no art. 4º, X. Cidadania (A) é fundamento; erradicar a marginalização (C) é objetivo; livre iniciativa (E) integra um fundamento; “soberania popular” (D) não está na lista do art. 4º.","Art. 4º: soberania (4), paz (3), humanidade (3)."),
 ("Art. 4º","Conforme o parágrafo único do art. 4º, a República Federativa do Brasil buscará a integração econômica, política, social e cultural dos povos:",
  ["do Mercosul, visando à formação de um mercado comum.","da América do Sul, visando à formação de uma união aduaneira.","da América Latina, visando à formação de uma comunidade latino-americana de nações.","das Américas, visando à formação de uma confederação.","de língua portuguesa, visando à formação de uma comunidade lusófona."],"C",
  "O texto menciona os povos da América Latina e a formação de uma comunidade latino-americana de nações. As demais alternativas trocam a região ou a finalidade.","América LATINA, comunidade latino-americana de nações."),
 ("Formas","Assinale a alternativa que relaciona corretamente os conceitos aplicáveis ao Brasil.",
  ["Forma de Estado: república; forma de governo: federação.","Forma de Estado: federação; forma de governo: república; sistema de governo: presidencialismo.","Forma de Estado: unitária; sistema de governo: parlamentarismo.","Forma de governo: monarquia constitucional; regime: democrático.","Forma de Estado: confederação; forma de governo: república."],"B",
  "O Brasil é uma Federação (forma de Estado), uma República (forma de governo) e adota o presidencialismo (sistema de governo). A inverte os conceitos; C, D e E indicam formas que o Brasil não adota.","Federação · República · Presidencialismo · Democracia."),
 ("Federalismo","Sobre o federalismo brasileiro, é correto afirmar que:",
  ["os Estados-membros são soberanos e podem se separar da Federação.","a União é soberana e hierarquicamente superior aos Estados.","os entes federativos são autônomos, e a soberania pertence à República Federativa do Brasil.","a forma federativa pode ser abolida por emenda constitucional aprovada por 3/5.","os Municípios não integram a Federação."],"C",
  "Os entes são autônomos (art. 18), e a soberania é da RFB. Não há direito de secessão (A); a União não é soberana nem superior (B); a forma federativa é cláusula pétrea (D); os Municípios são entes federativos (E).","Soberania = RFB; autonomia = entes; forma federativa = cláusula pétrea."),
 ("Federalismo","A Federação brasileira surgiu a partir de um Estado unitário, que se descentralizou com a República. Por isso, a doutrina a classifica como federalismo:",
  ["por agregação.","por desagregação.","confederativo.","centrípeto por associação de Estados soberanos.","de dois níveis, sem Municípios."],"B",
  "O Brasil passou de Estado unitário (Império) a Federação: federalismo por desagregação (centrífugo). Por agregação é o caso dos EUA. A federação brasileira tem três níveis, incluindo Municípios.","Brasil = desagregação; EUA = agregação."),
 ("Art. 18","Nos termos do art. 18 da Constituição, os Territórios Federais:",
  ["são entes federativos autônomos.","integram a União, e sua criação é regulada em lei complementar.","integram os Estados de onde forem desmembrados, por lei estadual.","têm a mesma autonomia dos Municípios.","são criados por decreto do Presidente da República."],"B",
  "O art. 18, § 2º, diz que os Territórios integram a União e que sua criação, transformação em Estado ou reintegração ao Estado de origem são reguladas em lei complementar. Eles não são entes federativos.","Territórios: integram a União; lei complementar."),
 ("Estados","A criação de um novo Estado, por desmembramento, depende de:",
  ["lei estadual, após consulta às Câmaras Municipais.","aprovação da população diretamente interessada, por plebiscito, e do Congresso Nacional, por lei complementar.","referendo nacional e decreto do Presidente da República.","emenda constitucional aprovada por 3/5.","lei ordinária federal, dispensada a consulta popular."],"B",
  "É o que diz o art. 18, § 3º. Lei estadual (A) é o instrumento para criar Municípios. Não se exige emenda (D), e a consulta popular é obrigatória (E).","Novo Estado: plebiscito + LC federal. Novo Município: lei estadual."),
 ("Municípios","Sobre a criação de Municípios (art. 18, § 4º), assinale a alternativa correta.",
  ["Faz-se por lei federal ordinária.","Dispensa plebiscito quando houver Estudo de Viabilidade favorável.","Faz-se por lei estadual, dentro do período determinado por lei complementar federal, após Estudos de Viabilidade Municipal e plebiscito com as populações dos Municípios envolvidos.","Depende apenas de aprovação da Câmara Municipal do Município de origem.","Pode ocorrer a qualquer tempo, por decreto do governador."],"C",
  "A alternativa C reproduz os requisitos do art. 18, § 4º (redação da EC nº 15/1996). O plebiscito é obrigatório e posterior à divulgação dos estudos.","LC federal (período) + EVM + plebiscito + lei estadual."),
 ("DF","Sobre o Distrito Federal, é correto afirmar que:",
  ["pode ser dividido em Municípios por lei distrital.","rege-se por Constituição distrital.","acumula as competências legislativas reservadas aos Estados e aos Municípios.","é a Capital Federal.","não possui autonomia."],"C",
  "Art. 32, § 1º: ao DF são atribuídas as competências legislativas dos Estados e dos Municípios. A divisão em Municípios é vedada (A); ele se rege por Lei Orgânica (B); a capital é Brasília (D); o DF é autônomo (E).","DF: sem Municípios, Lei Orgânica, competências estaduais e municipais."),
 ("Competências","No âmbito da competência legislativa concorrente (art. 24), a superveniência de lei federal sobre normas gerais:",
  ["revoga a lei estadual anterior.","suspende a eficácia da lei estadual, no que lhe for contrário.","não produz nenhum efeito sobre a lei estadual.","torna a lei estadual inconstitucional desde sua origem.","exige que o Estado edite nova lei no prazo de 30 dias."],"B",
  "Art. 24, § 4º: a lei federal superveniente suspende a eficácia da lei estadual no que lhe for contrário. Não há revogação nem inconstitucionalidade originária.","Concorrente: suspende a eficácia, não revoga."),
 ("Art. 19","Uma lei estadual concedeu pontuação extra em concurso público aos candidatos nascidos no próprio Estado. Essa lei:",
  ["é válida, por concretizar a autonomia estadual.","é válida, se aprovada por 2/3 da Assembleia Legislativa.","viola a vedação de criar distinções entre brasileiros (art. 19, III).","viola apenas o princípio da laicidade.","é válida, por se tratar de competência remanescente."],"C",
  "O art. 19, III, proíbe a todos os entes criar distinções entre brasileiros ou preferências entre si. A autonomia não autoriza discriminar pela origem. A laicidade (D) é o inciso I e não se aplica ao caso.","Art. 19: laicidade, fé dos documentos públicos, igualdade entre brasileiros.")]

def qhtml(i, q):
    tema, enun, alts, gab, com, mem = q
    lis = "".join(f'<li data-l="{"ABCDE"[j]}">{a}</li>' for j,a in enumerate(alts))
    return f'<div class="q"><div class="qh"><span class="qn">Questão {i:02d}</span><span class="qa">Questão autoral · {tema}</span></div><p>{enun}</p><ol>{lis}</ol></div>'
qs = [qhtml(i+1,q) for i,q in enumerate(Q)]
add('<div class="marker">§§R3§§</div><div class="unit"><span class="u">PRÁTICA</span><span class="t">20 questões</span></div><h1 class="big">Questões <span class="hl">autorais</span></h1><p class="lead">Elaboradas para este caderno, no estilo de concursos. Nenhuma foi aplicada por banca. Resolva sem consultar.</p>' + "".join(qs[:3]))
for k in range(3, 20, 3): add("".join(qs[k:k+3]))

grid = "<tr>" + "".join(f"<th style='text-align:center'>{i+1:02d}</th>" for i in range(10)) + "</tr><tr>" + "".join(f"<td style='text-align:center;font-weight:900;color:#0b2a5b'>{q[3]}</td>" for q in Q[:10]) + "</tr>"
grid2 = "<tr>" + "".join(f"<th style='text-align:center'>{i+11:02d}</th>" for i in range(10)) + "</tr><tr>" + "".join(f"<td style='text-align:center;font-weight:900;color:#0b2a5b'>{q[3]}</td>" for q in Q[10:]) + "</tr>"
gabs = [f'<div class="gab"><div class="gh">Questão {i+1:02d} <span>{q[3]}</span></div><p>{q[4]}</p><span class="mem">Memorize: {q[5]}</span></div>' for i,q in enumerate(Q)]
add('<div class="marker">§§R4§§</div><div class="unit"><span class="u">CORREÇÃO</span></div><h1 class="big">Gabarito <span class="hl">comentado</span></h1><p class="lead">Leia o comentário mesmo quando acertar.</p>' + f'<table>{grid}</table><table>{grid2}</table>' + "".join(gabs[:4]))
for k in range(4, 20, 6): add("".join(gabs[k:k+6]))

# =========================================================== REFERÊNCIAS
add(f'''<div class="marker">§§R5§§</div><div class="unit"><span class="u">ENCERRAMENTO</span></div><h1 class="big">Referências e <span class="hl">plano de revisão</span></h1><p class="lead">De onde vieram as informações e como continuar.</p>
<h3>Legislação consultada (portal do Planalto)</h3>
<ul>
<li>BRASIL. <strong>Constituição da República Federativa do Brasil de 1988</strong>: preâmbulo; arts. 1º, 2º, 3º, 4º, 5º (§ 3º e incisos citados), 14, 18, 19, 21, 22, 23, 24, 25, 29, 30, 32, 34 e 60. Texto compilado: planalto.gov.br/ccivil_03/constituicao/constituicao.htm.</li>
<li>BRASIL. <strong>Emenda Constitucional nº 15, de 1996</strong> (redação do art. 18, § 4º) e <strong>nº 45, de 2004</strong> (art. 5º, § 3º).</li>
<li>BRASIL. <strong>Lei Complementar nº 230, de 15 de abril de 2026</strong>: normas gerais para o desmembramento de parte de um Município para incorporação a outro, limítrofe (art. 18, § 4º, da CF). DOU de 16/4/2026.</li>
</ul>
<h3>Jurisprudência citada</h3>
<ul><li>STF, <strong>ADI 2.076</strong>: preâmbulo sem força normativa.</li><li>STF, <strong>ADI 2.650</strong>: “população diretamente interessada” no desmembramento de Estado.</li>
<li>STF, <strong>Súmula Vinculante 11</strong> (uso de algemas) e <strong>Súmula Vinculante 38</strong> (horário de funcionamento do comércio).</li><li>STF, entendimento sobre a hierarquia supralegal dos tratados de direitos humanos não aprovados pelo rito do art. 5º, § 3º (RE 466.343).</li></ul>
{lembre(f"""<p><strong>Material pesquisado e atualizado em: {DATA}.</strong> O texto dos arts. 1º, 2º, 3º, 4º, 5º (§ 3º), 18, 19, 21 (I), 22 (parágrafo único), 24 (§§ 1º a 4º), 25, 29, 30, 32, 34 (I) e 60 (§§ 2º e 4º) foi conferido palavra por palavra no texto compilado do Planalto. A LC nº 230/2026 foi consultada no Planalto. <strong>Limitação:</strong> o texto do ADCT não pôde ser acessado na verificação; a referência ao plebiscito de 1993 baseia-se em fato histórico amplamente documentado. As súmulas e precedentes citados não foram reconferidos no portal do STF nesta edição. Antes da prova, confira se houve alteração posterior a esta data.</p>""", "Verificação e limitações")}
''')
add(f'''<div class="unit"><span class="u">ENCERRAMENTO</span></div><h3>Plano de revisão sugerido</h3>
{table(["Quando","O que fazer","Tempo"],[["Dia 1","Unidade 1 completa","1h30"],["Dia 2","Unidade 2 + quadro comparativo","1h30"],["Dia 3","Unidade 3","2h"],["Dia 4","Questões sem consulta + gabarito comentado","1h"],["Dias 7, 15 e 30","Mapa conceitual, resumo visual e flashcards","30 min"]],["24%",None,"16%"])}
<div class="ending"><h2>Fim do Caderno 01</h2><p style="text-align:center">Próximo caderno da coleção: <strong>Direitos e Garantias Fundamentais (arts. 5º a 17)</strong>.</p>
<p class="note" style="text-align:center">Caderno Simplificado · Direito Constitucional · Caderno 01 · 1ª edição · novembro de 2026<br>Material de estudo independente. Não substitui a leitura da Constituição e do edital do seu concurso.</p></div>''')

doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Caderno Simplificado — Direito Constitucional — Caderno 01</title>
<link rel="stylesheet" href="estilo.css"></head><body>{symbols()}{"".join(P)}</body></html>'''
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "miolo.html"), "w").write(doc)
print("páginas planejadas:", len(P))
