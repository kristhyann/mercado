"""Gera miolo.html do Caderno 11: Atos Administrativos. Uso: python3 gerar.py
Base legal conferida no portal do Planalto em 26/11/2026: Lei nº 4.717/1965 (art. 2º), Lei nº 9.784/1999 (arts. 50 e 53 a 55),
LINDB (arts. 20, 21 e 24) e CF/88."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit
from kit import *

DATA = "26 de novembro de 2026"
kit.U = {1:("UNIDADE 1","Noções gerais"),2:("UNIDADE 2","Elementos do ato"),3:("UNIDADE 3","Atributos"),4:("UNIDADE 4","Tipos e classificação"),5:("UNIDADE 5","Extinção dos atos")}

# ================================================================ APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">Como a Administração manifesta sua vontade, o que torna um ato válido e como ele deixa de existir.</p>
<p>Este é o <strong>Caderno 11 da coleção</strong>, o terceiro de <strong>Direito Administrativo</strong>. O ato administrativo é a "peça" básica do trabalho da Administração: uma multa, um alvará, uma nomeação, uma portaria. Saber reconhecer seus <strong>elementos</strong>, seus <strong>atributos</strong> e suas formas de <strong>extinção</strong> é indispensável em qualquer prova de nível médio.</p>
<p>A teoria dos atos administrativos é, em grande parte, <strong>construção doutrinária</strong>. A lei traz pontos-chave (como os vícios do ato na Lei da Ação Popular e a anulação, a revogação e a convalidação na Lei nº 9.784/1999), e o caderno indica quando a informação vem da lei e quando vem da doutrina.</p>
{table(["Recurso","Onde está"],[["Diagrama dos cinco elementos (com a pergunta-chave de cada um)","Unidade 2"],["Elementos vinculados x discricionários","Unidade 2"],["Diagrama dos atributos","Unidade 3"],["Espécies de atos e quadro de classificação","Unidade 4"],["Linha do tempo: perfeição, validade e eficácia","Unidade 4"],["Anulação x revogação x convalidação (cenas e quadro)","Unidade 5"],["Mapa conceitual, erros mais comuns e 24 questões autorais","Revisão e prática"]],["58%",None])}
{lembre(p(f'Lei nº 4.717/1965 (art. 2º), Lei nº 9.784/1999 (arts. 50, 53, 54 e 55) e Lei de Introdução às Normas do Direito Brasileiro (arts. 20, 21 e 24) conferidas no portal do Planalto em <strong>{DATA}</strong>.'), "Fontes e atualização")}''', first=True)

toc_page([("u","UNIDADE 1 · NOÇÕES GERAIS","U1"),("","1. Conceito de ato administrativo","A01"),("","2. Ato administrativo x fato administrativo x atos da Administração","A02"),
 ("u","UNIDADE 2 · ELEMENTOS (REQUISITOS) DO ATO","U2"),("","3. Os cinco elementos (diagrama)","A03"),("","4. Competência","A04"),("","5. Finalidade","A05"),("","6. Forma","A06"),("","7. Motivo e motivação","A07"),("","8. Objeto","A08"),("","9. Elementos vinculados x discricionários","A09"),
 ("u","UNIDADE 3 · ATRIBUTOS","U3"),("","10. Os atributos (diagrama)","A10"),("","11. Presunção de legitimidade e veracidade","A11"),("","12. Imperatividade","A12"),("","13. Autoexecutoriedade (quando aplicável) e tipicidade","A13"),
 ("u","UNIDADE 4 · TIPOS E CLASSIFICAÇÃO","U4"),("","14. Espécies de atos (tipos)","A14"),("","15. Atos negociais: licença, autorização e permissão","A15"),("","16. Classificação dos atos","A16"),("","17. Perfeição, validade e eficácia","A17"),
 ("u","UNIDADE 5 · EXTINÇÃO DOS ATOS","U5"),("","18. Formas de extinção","A18"),("","19. Anulação","A19"),("","20. Revogação","A20"),("","21. Convalidação","A21"),("","22. Anulação x revogação x convalidação","A22"),
 ("u","REVISÃO E PRÁTICA","RV"),("","Mapa conceitual · Erros mais comuns","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),("","Gabarito, respostas dos treinos e referências","R4")])

# ================================================================ UNIDADE 1
opener("01","UNIDADE 1","Noções gerais",["Conceito de ato administrativo","Ato x fato x atos da Administração"],"U1")

add(H(1,'Conceito de <span class="hl">ato administrativo</span>','A manifestação de vontade da Administração com efeitos jurídicos.', "A01") +
 oque(p('<strong>Ato administrativo</strong> é a <strong>declaração unilateral</strong> do Estado, ou de quem o represente, que produz <strong>efeitos jurídicos imediatos</strong>, sob <strong>regime de direito público</strong>, com observância da lei e sujeita a <strong>controle</strong> pelo Poder Judiciário (conceito doutrinário).')) +
 cards([("#1","Declaração do Estado","Ou de quem age em seu nome, como uma concessionária."),("#2","Efeitos jurídicos","Cria, modifica, extingue ou declara direitos e deveres."),("#3","Direito público","Com prerrogativas e sujeições próprias do Estado."),("#4","Sujeito a controle","Pode ser revisto pela Administração e pelo Judiciário.")],4) +
 memo('Ato administrativo = <strong>declaração unilateral</strong> + <strong>efeitos jurídicos</strong> + <strong>regime de direito público</strong> + <strong>controle judicial</strong>.'))
atencao(traduz(p('Pense em atos que você conhece: a <strong>multa</strong> de trânsito, o <strong>alvará</strong> que autoriza uma loja a funcionar, a <strong>nomeação</strong> de um aprovado em concurso, a <strong>portaria</strong> que muda o horário de uma repartição. Todos são manifestações da vontade da Administração que mudam algo na vida das pessoas. Atos administrativos podem ser praticados pelos <strong>três Poderes</strong> quando exercem função administrativa.')) +
 ex(p('Um guarda municipal, no exercício da fiscalização de posturas, lavra um <b>auto de infração</b> contra um ambulante sem licença. Esse auto é um ato administrativo: declaração unilateral da Administração, que produz efeito jurídico (a autuação), sob regime de direito público, e que o ambulante pode contestar na própria Administração ou na Justiça.')) +
 pega('<ul><li>Ato administrativo não é exclusivo do Executivo: o Legislativo e o Judiciário também os praticam.</li><li>Concessionárias de serviço público também podem praticar atos administrativos, quando agem em nome do Estado.</li></ul>'),
 ["declaração unilateral","efeitos jurídicos","regime de direito público","controle judicial"], "O conceito na prática")

add(H(1,'Ato x fato x <span class="hl">atos da Administração</span>','Nem tudo que a Administração faz é ato administrativo.', "A02") +
 table(["Figura","O que é","Exemplo"],[
  ["<b>Ato administrativo</b>","Manifestação de vontade com efeitos jurídicos, sob regime de direito público","Multa, licença, nomeação, portaria"],
  ["<b>Fato administrativo</b>","Atividade material (execução) ou acontecimento que produz efeitos para a Administração, sem ser declaração de vontade","Pavimentar uma rua, demolir um imóvel, a morte de um servidor"],
  ["Ato de direito privado da Administração","A Administração age em pé de igualdade com o particular","Locação de um imóvel para instalar uma repartição"],
  ["Ato político (de governo)","Decisão de alta direção, com fundamento direto na Constituição","Veto a projeto de lei, declaração de guerra"],
  ["Contrato administrativo","Acordo <b>bilateral</b>, e não declaração unilateral","Contrato de obra pública"]],["24%",None,"28%"]) +
 ex(p('A Prefeitura decide, por despacho, que uma obra irregular será <b>demolida</b>: esse despacho é um <b>ato administrativo</b>. Quando as máquinas efetivamente derrubam a construção, há um <b>fato administrativo</b> (a execução material do ato). Se a Prefeitura <b>aluga</b> um prédio para instalar uma escola, pratica ato de direito privado.')) +
 memo('Ato = <strong>declaração de vontade</strong>. Fato = <strong>execução material</strong> ou acontecimento. Contrato = <strong>bilateral</strong>.'))

treino(1, [
 ("O ato administrativo é declaração unilateral que produz efeitos jurídicos, sob regime de direito público.","C","Conceito doutrinário."),
 ("Somente o Poder Executivo pratica atos administrativos.","E","Os três Poderes praticam atos administrativos ao exercer função administrativa."),
 ("A demolição material de uma construção é exemplo de fato administrativo.","C","Execução material."),
 ("O contrato administrativo é espécie de ato administrativo unilateral.","E","Contrato é acordo bilateral."),
 ("O veto a projeto de lei é exemplo de ato político, e não de ato administrativo típico.","C","Ato de governo, com base direta na Constituição."),
 ("Os atos administrativos estão sujeitos a controle pelo Poder Judiciário.","C","Controle de legalidade.")])

# ================================================================ UNIDADE 2
opener("02","UNIDADE 2","Elementos (requisitos) do ato",["Os cinco elementos","Competência","Finalidade","Forma","Motivo e motivação","Objeto","Elementos vinculados x discricionários"],"U2")

def elementos():
    N,G,O=C['navy'],C['blue'],C['golddeep']
    it=[("COMPETÊNCIA","QUEM pode","praticar?","sujeito",N,NV),("FINALIDADE","PARA QUÊ","se pratica?","interesse público",G,C['sky']),("FORMA","COMO se","exterioriza?","em regra, escrita",O,C['goldsoft']),("MOTIVO","POR QUÊ","se pratica?","fato + direito",C['red'],C['redsoft']),("OBJETO","O QUÊ","o ato determina?","conteúdo",C['green'],C['greensoft'])]
    s = f'<figure><svg viewBox="0 0 640 250" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    s += f'<rect x="200" y="4" width="240" height="44" rx="12" fill="{N}"/><text x="320" y="24" text-anchor="middle" font-size="13" font-weight="900" fill="#fff">ATO ADMINISTRATIVO VÁLIDO</text><text x="320" y="40" text-anchor="middle" font-size="10" fill="#cfe0f2">precisa dos cinco elementos sem vício</text>'
    s += '<g stroke="#9db0c8" stroke-width="2.5" fill="none"><path d="M320 48 V64 M66 64 H574 M66 64 V80 M193 64 V80 M320 64 V80 M447 64 V80 M574 64 V80"/></g>'
    for k,(t,a,b,c,fg,bg) in enumerate(it):
        x = 66+k*127
        s += f'<rect x="{x-60}" y="80" width="120" height="132" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x}" y="106" text-anchor="middle" font-size="12" font-weight="900" fill="{fg}">{t}</text>'
        s += f'<text x="{x}" y="136" text-anchor="middle" font-size="12" font-weight="900" fill="{C["ink"]}">{a}</text><text x="{x}" y="154" text-anchor="middle" font-size="11" font-weight="700" fill="{C["ink"]}">{b}</text><text x="{x}" y="190" text-anchor="middle" font-size="9.8" fill="{C["muted"]}">{c}</text>'
    s += f'<text x="320" y="240" text-anchor="middle" font-size="11" font-weight="900" fill="{N}">Memória: COM-FI-FOR-M-OB  ·  “Quem? Para quê? Como? Por quê? O quê?”</text>'
    return s + '</svg><figcaption>Os cinco elementos do ato administrativo e a pergunta que cada um responde.</figcaption></figure>'

add(H(2,'Os <span class="hl">cinco elementos</span>','Competência, finalidade, forma, motivo e objeto.', "A03") +
 elementos() +
 lei("Art. 2º · Lei nº 4.717/1965 (Ação Popular)",'<p>São nulos os atos lesivos ao patrimônio das entidades mencionadas no artigo anterior, nos casos de: a) incompetência; b) vício de forma; c) ilegalidade do objeto; d) inexistência dos motivos; e) desvio de finalidade.</p>') +
 traduz(p('A Lei da Ação Popular não lista os elementos de forma direta, mas, ao indicar os <strong>vícios</strong> que tornam o ato nulo, revela quais são eles. Por isso a doutrina majoritária aponta <strong>cinco elementos</strong> (ou requisitos de validade). Se um deles tem defeito, o ato é <strong>inválido</strong>, embora alguns defeitos possam ser corrigidos (convalidação).'),"profa"))

add(H(2,'<span class="hl">Competência</span>','Quem pode praticar o ato.', "A04") +
 oque(p('É o poder atribuído <strong>por lei</strong> ao agente para praticar o ato. Responde à pergunta: <strong>quem pode?</strong> É sempre elemento <strong>vinculado</strong>.')) +
 table(["Característica","Explicação"],[
  ["Decorre da lei","Só a lei (ou a Constituição) cria competências"],
  ["Irrenunciável","O agente não pode abrir mão (Lei nº 9.784/1999, art. 11)"],
  ["Admite delegação e avocação","Nos limites da lei; não se delegam atos normativos, decisão de recursos e matérias exclusivas (art. 13)"],
  ["Imprescritível e improrrogável","Não se perde por falta de uso; a incompetência não vira competência com o tempo"]],["30%",None]) +
 table(["Vício de competência","O que é","Consequência"],[
  ["Excesso de poder","Agente competente vai além dos limites da sua competência","Nulidade; pode ser convalidado se a competência não for exclusiva"],
  ["Usurpação de função","Pessoa que <b>não é agente público</b> pratica ato como se fosse","Ato considerado inexistente; é também crime (CP, art. 328)"],
  ["Função de fato","Agente com investidura irregular (ex.: posse sem requisito), mas com aparência de legalidade","Atos podem ser mantidos perante terceiros de boa-fé (teoria da aparência)"]],["22%",None,"30%"]) +
 memo('Competência: <strong>quem</strong>. Sempre <strong>vinculada</strong>. Excesso de poder = ir além; usurpação = quem nem é agente; função de fato = investidura irregular, com atos preservados para terceiros de boa-fé.'))

add(H(2,'<span class="hl">Finalidade</span>','Para que o ato é praticado.', "A05") +
 oque(p('É o <strong>resultado</strong> que a Administração quer alcançar com o ato. Responde à pergunta: <strong>para quê?</strong> É elemento <strong>vinculado</strong>: a lei define o fim.')) +
 table(["Sentido","O que significa","Exemplo"],[
  ["Amplo (geral)","Todo ato deve buscar o <b>interesse público</b>","Nenhum ato pode servir a interesse pessoal"],
  ["Estrito (específico)","Cada ato tem um fim próprio, previsto em lei","Remoção serve à necessidade do serviço; não serve para punir"]],["20%",None,"34%"]) +
 lei("Art. 2º, parágrafo único, e · Lei nº 4.717/1965",'<p>e) o desvio de finalidade se verifica quando o agente pratica o ato visando a fim diverso daquele previsto, explícita ou implicitamente, na regra de competência.</p>') +
 ex(p('Uma servidora faz críticas ao secretário e, na semana seguinte, é <b>removida</b> para um posto distante "por necessidade do serviço". Provado que a verdadeira intenção foi <b>punir</b>, há <b>desvio de finalidade</b>: a remoção foi usada para um fim que a lei não prevê. O ato é <b>nulo</b> e não pode ser convalidado.')) +
 memo('Finalidade: <strong>para quê</strong>. Sempre <strong>vinculada</strong>. Vício = <strong>desvio de finalidade</strong> (ato nulo, <strong>não convalidável</strong>).'))

add(H(2,'<span class="hl">Forma</span>','Como o ato se exterioriza.', "A06") +
 oque(p('É o modo de <strong>exteriorização</strong> do ato e as <strong>formalidades</strong> exigidas para a sua prática. Responde à pergunta: <strong>como?</strong> Em regra, é elemento <strong>vinculado</strong>.')) +
 table(["Ponto","Regra"],[
  ["Regra geral","Forma <b>escrita</b>, pois permite controle e registro"],
  ["Exceções","Ordens verbais (instruções urgentes), gestos e sinais (o apito e o gesto do agente de trânsito, o semáforo, placas)"],
  ["Sentido amplo","Inclui o <b>procedimento</b> exigido: motivação, publicação, contraditório e ampla defesa antes de uma sanção"],
  ["Silêncio administrativo","Em regra, a omissão não é ato; só produz efeito (deferimento ou indeferimento) quando a <b>lei</b> assim prevê"],
  ["Vício de forma","Pode ser <b>sanável</b> (forma não essencial) ou insanável (forma essencial à validade, como o processo antes da demissão)"]],["26%",None]) +
 ex(p('O agente de trânsito que, com um gesto, manda o motorista parar pratica um ato administrativo de <b>forma não escrita</b>, válida. Já uma <b>demissão</b> de servidor sem processo administrativo disciplinar tem vício de forma <b>essencial</b> e é <b>nula</b>. Se, porém, um ato foi publicado com erro na data de assinatura, o vício é <b>sanável</b>.')) +
 memo('Forma: <strong>como</strong>. Regra: <strong>escrita</strong>. Vício de forma <strong>não essencial</strong> pode ser <strong>convalidado</strong>.'))

add(H(2,'<span class="hl">Motivo</span> e motivação','Por que o ato é praticado.', "A07") +
 table(["","MOTIVO","MOTIVAÇÃO"],[
  ["O que é","A <b>situação de fato e de direito</b> que autoriza ou exige o ato (o pressuposto)","A <b>exposição escrita</b> dos motivos (a justificativa)"],
  ["Pergunta","<b>Por quê?</b>","Onde estão explicados os porquês?"],
  ["Elemento?","<b>Sim</b>, é elemento do ato","Faz parte da <b>forma</b>"],
  ["Exemplo","Servidor faltou 40 dias seguidos (fato) + a lei prevê demissão por abandono (direito)","O texto da decisão que descreve as faltas e cita a lei"]],["16%",None,None]) +
 table(["Regra","Conteúdo"],[
  ["Quando motivar (Lei nº 9.784/1999, art. 50)","Os atos devem ser motivados, com indicação dos fatos e fundamentos jurídicos, quando, entre outros: neguem, limitem ou afetem direitos; imponham ou agravem deveres ou sanções; decidam processos seletivos; dispensem licitação; decidam recursos; anulem, revoguem, suspendam ou convalidem atos"],
  ["Teoria dos motivos determinantes","O motivo declarado <b>vincula</b> o ato: se for falso ou inexistente, o ato é nulo, mesmo que a motivação não fosse obrigatória"],
  ["Exoneração de cargo em comissão","Dispensa motivação (livre exoneração); mas, se o motivo for declarado, ele vincula"]],["30%",None]) +
 memo('Motivo = <strong>fato + direito</strong> (elemento). Motivação = <strong>exposição</strong> dos motivos (forma). Motivo declarado <strong>vincula</strong>.'))

add(H(2,'<span class="hl">Objeto</span>','O que o ato determina.', "A08") +
 oque(p('É o <strong>conteúdo</strong> do ato: o efeito jurídico imediato que ele produz. Responde à pergunta: <strong>o quê?</strong> Pode ser vinculado ou discricionário.')) +
 table(["Requisito do objeto","Exemplo de vício"],[
  ["Lícito (permitido por lei)","Ato que autoriza construção em área de preservação onde a lei proíbe"],
  ["Possível (de fato e de direito)","Ato que manda demolir um imóvel que já não existe"],
  ["Certo (definido)","Ato que pune “algum servidor do setor”, sem identificá-lo"],
  ["Moral","Ato que, embora formalmente permitido, tem conteúdo desonesto"]],["34%",None]) +
 lei("Art. 2º, parágrafo único, c · Lei nº 4.717/1965",'<p>c) a ilegalidade do objeto ocorre quando o resultado do ato importa em violação de lei, regulamento ou outro ato normativo;</p>') +
 ex(p('No ato de <b>interdição</b> de um restaurante, o objeto é a própria interdição (o fechamento do estabelecimento). No ato de <b>nomeação</b>, o objeto é o provimento do cargo. Se a lei prevê, para certa infração, apenas advertência, aplicar <b>demissão</b> é vício de objeto.')) +
 memo('Objeto: <strong>o quê</strong> (conteúdo). Deve ser <strong>lícito, possível, certo e moral</strong>.'))

ed = scene3([("SEMPRE VINCULADOS",C['navy'],NV,"prof",["Competência,","finalidade e","forma (em regra)."],"a lei define"),
 ("PODEM SER LIVRES",C['blue'],C['sky'],"profa",["Motivo e objeto,","quando a lei dá","margem de escolha."],"MÉRITO"),
 ("MÉRITO",C['golddeep'],C['goldsoft'],"prof",["Conveniência e","oportunidade na","escolha."],"Judiciário não substitui")], "Situação ilustrada: onde fica a liberdade do administrador.")
add(H(2,'Elementos vinculados x <span class="hl">discricionários</span>','Onde fica o mérito administrativo.', "A09") + ed +
 table(["Elemento","Ato vinculado","Ato discricionário"],[
  ["Competência","Vinculado","Vinculado"],["Finalidade","Vinculado","Vinculado"],["Forma","Vinculado","Vinculado (em regra)"],
  ["Motivo","Vinculado","<b>Pode ser discricionário</b>"],["Objeto","Vinculado","<b>Pode ser discricionário</b>"]],["30%",None,None]) +
 memo('<strong>COM-FI-FOR</strong>: sempre vinculados. <strong>M-OB</strong> (motivo e objeto): podem ser discricionários e formam o <strong>mérito</strong>.'))

treino(2, [
 ("São elementos do ato administrativo: competência, finalidade, forma, motivo e objeto.","C","Doutrina majoritária, a partir da Lei nº 4.717/1965."),
 ("A competência pode ser renunciada pelo agente, desde que haja interesse público.","E","É irrenunciável (Lei nº 9.784/1999, art. 11)."),
 ("O desvio de finalidade ocorre quando o agente pratica o ato visando a fim diverso do previsto na regra de competência.","C","Lei nº 4.717/1965, art. 2º, parágrafo único, e."),
 ("Motivo e motivação são expressões sinônimas.","E","Motivo é o pressuposto de fato e de direito; motivação é a sua exposição."),
 ("Pela teoria dos motivos determinantes, o motivo declarado vincula a validade do ato.","C","Motivo falso ou inexistente invalida o ato."),
 ("No ato discricionário, a finalidade é elemento discricionário.","E","A finalidade é sempre vinculada; motivo e objeto podem ser discricionários.")])

# ================================================================ UNIDADE 3
opener("03","UNIDADE 3","Atributos do ato administrativo",["Os atributos","Presunção de legitimidade e veracidade","Imperatividade","Autoexecutoriedade e tipicidade"],"U3")

def atributos():
    N,G,O=C['navy'],C['blue'],C['golddeep']
    it=[("P","PRESUNÇÃO","de legitimidade","e veracidade","todos os atos",N,NV),("A","AUTOEXECUTORIEDADE","executa sem","ordem judicial","só quando a lei prevê ou há urgência",C['red'],C['redsoft']),("T","TIPICIDADE","corresponde a","tipo legal","doutrina (Di Pietro)",O,C['goldsoft']),("I","IMPERATIVIDADE","impõe-se ao","particular","atos que criam obrigações",G,C['sky'])]
    s = f'<figure><svg viewBox="0 0 640 220" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    for k,(l,t1,a,b,c,fg,bg) in enumerate(it):
        x = 6+k*159
        s += f'<rect x="{x}" y="10" width="148" height="170" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><circle cx="{x+74}" cy="42" r="22" fill="{fg}"/><text x="{x+74}" y="50" text-anchor="middle" font-size="22" font-weight="900" fill="#fff">{l}</text>'
        s += f'<text x="{x+74}" y="86" text-anchor="middle" font-size="{11.5 if len(t1)<15 else 9.6}" font-weight="900" fill="{fg}">{t1}</text><text x="{x+74}" y="108" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">{a}</text><text x="{x+74}" y="124" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">{b}</text>'
        for j,w in enumerate(wrap(c, 22)): s += f'<text x="{x+74}" y="{150+j*13}" text-anchor="middle" font-size="9.2" font-weight="700" fill="{C["muted"]}">{w}</text>'
    s += f'<text x="320" y="210" text-anchor="middle" font-size="11" font-weight="900" fill="{N}">Memória: PATI · Presunção, Autoexecutoriedade, Tipicidade, Imperatividade</text>'
    return s + '</svg><figcaption>Os atributos do ato administrativo: só a presunção está presente em todos os atos.</figcaption></figure>'
def wrap(t, n):
    out, cur = [], ""
    for w in t.split():
        if len(cur)+len(w)+1 > n and cur: out.append(cur); cur = w
        else: cur = (cur+" "+w).strip()
    return out + [cur]

add(H(3,'Os <span class="hl">atributos</span>','As qualidades que diferenciam o ato administrativo do ato privado.', "A10") +
 atributos() +
 traduz(p('Atributos são as <strong>prerrogativas</strong> que o ato administrativo tem por ser praticado pelo Estado, em nome do interesse público. Um contrato entre particulares não se impõe a quem não o assinou; já uma ordem de interdição da vigilância sanitária <strong>se impõe</strong> ao dono do restaurante, mesmo que ele não concorde. Atenção: <strong>nem todo ato tem todos os atributos</strong>.')) +
 memo('Atributos: <strong>PATI</strong>. Só a <strong>presunção</strong> existe em todos os atos. Elementos (COM-FI-FOR-M-OB) ≠ atributos (PATI).'))

add(H(3,'Presunção de <span class="hl">legitimidade e veracidade</span>','Até prova em contrário, o ato é válido e verdadeiro.', "A11") +
 table(["Aspecto","Significado"],[
  ["Legitimidade","Presume-se que o ato foi praticado <b>conforme a lei</b>"],
  ["Veracidade","Presume-se que os <b>fatos</b> declarados pela Administração são verdadeiros"],
  ["Natureza","Presunção <b>relativa</b> (admite prova em contrário)"],
  ["Efeito prático","O ato produz efeitos desde logo e cabe a quem o contesta <b>provar</b> o vício (inversão do ônus da prova)"],
  ["Alcance","Está presente em <b>todos</b> os atos administrativos"]],["26%",None]) +
 ex(p('Um agente de trânsito lavra um auto de infração afirmando que o motorista avançou o sinal vermelho. Esse registro é presumido <b>verdadeiro</b> e o ato, <b>legítimo</b>: a multa produz efeitos e é o motorista quem precisa apresentar provas (por exemplo, um vídeo) para derrubá-la. Uma <b>certidão</b> emitida pela Prefeitura também é presumida verdadeira.')) +
 memo('Presunção: <strong>relativa</strong>, em <strong>todos</strong> os atos. Quem alega o vício tem de <strong>provar</strong>.'))

add(H(3,'<span class="hl">Imperatividade</span>','O ato se impõe ao particular, independentemente de concordância.', "A12") +
 oque(p('É o atributo pelo qual o ato administrativo <strong>se impõe a terceiros</strong>, criando obrigações <strong>unilateralmente</strong>, sem depender da concordância deles. A doutrina também o chama de <strong>poder extroverso</strong>.')) +
 table(["Tem imperatividade","Não tem imperatividade"],[
  ["Atos que impõem obrigações: interdição, multa, ordem de demolição, requisição","Atos <b>negociais</b>, que atendem a um pedido do particular: licença, autorização, permissão"],
  ["Ordens de serviço aos subordinados","Atos <b>enunciativos</b>, que só atestam ou opinam: certidão, atestado, parecer"]],["50%",None]) +
 ex(p('A ordem de <b>demolição</b> de uma construção irregular cria uma obrigação para o proprietário, que não precisa concordar: há imperatividade. Já a <b>certidão negativa de débitos</b> apenas atesta uma situação e não impõe nada a ninguém: não há imperatividade.')) +
 memo('Imperatividade = impor obrigação <strong>unilateralmente</strong>. Não existe em atos <strong>negociais</strong> nem <strong>enunciativos</strong>.'))

add(H(3,'Autoexecutoriedade e <span class="hl">tipicidade</span>','Executar sem juiz, quando a lei permite.', "A13") +
 oque(p('<strong>Autoexecutoriedade</strong> é o atributo pelo qual a Administração pode <strong>executar o próprio ato</strong>, inclusive com meios coercitivos, <strong>sem precisar de ordem judicial</strong>. Ela <strong>não existe em todos os atos</strong>: só quando a <strong>lei prevê</strong> ou em situação de <strong>urgência</strong> para proteger o interesse público.')) +
 table(["Há autoexecutoriedade","Não há autoexecutoriedade"],[
  ["Apreensão e destruição de alimentos estragados","Cobrança forçada de multa não paga (exige execução fiscal na Justiça)"],
  ["Interdição de estabelecimento que ameaça a saúde pública","Desapropriação sem acordo (exige ação judicial, salvo acordo)"],
  ["Remoção de veículo estacionado irregularmente","Penhora de bens do particular"],
  ["Dissolução de reunião que se torne violenta","Imposição de sanção sem processo, quando a lei exige processo"]],["50%",None]) +
 lembre(p('A doutrina divide a autoexecutoriedade em <strong>exigibilidade</strong> (meios indiretos de coerção, como a multa, que pressiona o particular a cumprir) e <strong>executoriedade</strong> (meios diretos, como a interdição física, a apreensão e a remoção). A <strong>tipicidade</strong>, apontada por Maria Sylvia Zanella Di Pietro, significa que o ato deve corresponder a uma figura (um tipo) definida em lei para produzir determinado resultado.'), "Desdobramentos (doutrina)") +
 memo('Autoexecutoriedade: só quando a <strong>lei prevê</strong> ou há <strong>urgência</strong>. A <strong>cobrança forçada da multa</strong> exige a via judicial.'))

atencao(
 table(["Atributo","Presente em","Exemplo"],[
  ["Presunção de legitimidade e veracidade","<b>Todos</b> os atos","Auto de infração; certidão"],
  ["Imperatividade","Atos que impõem obrigações","Ordem de demolição"],
  ["Autoexecutoriedade","Quando a lei prevê ou há urgência","Apreensão de mercadoria estragada"],
  ["Tipicidade (doutrina)","Atos unilaterais","Cada ato corresponde a uma figura legal"]],["30%",None,None]) +
 pega('<ul><li>A presunção é <b>relativa</b>, e não absoluta.</li><li>Nem todo ato é <b>imperativo</b>: licença e certidão, por exemplo, não são.</li><li>Nem todo ato é <b>autoexecutório</b>: a cobrança forçada de multa depende de execução judicial.</li><li>Não confunda <b>elementos</b> (requisitos de validade) com <b>atributos</b> (prerrogativas).</li></ul>'),
 ["presunção relativa","imperatividade","poder extroverso","autoexecutoriedade","exigibilidade","executoriedade"])

treino(3, [
 ("A presunção de legitimidade dos atos administrativos é absoluta.","E","É relativa (admite prova em contrário)."),
 ("A presunção de legitimidade está presente em todos os atos administrativos.","C","É o único atributo presente em todos."),
 ("A licença para construir é ato dotado de imperatividade.","E","Atos negociais não impõem obrigação ao particular."),
 ("A cobrança forçada de multa administrativa não paga depende de execução judicial.","C","Não há autoexecutoriedade nesse caso."),
 ("A autoexecutoriedade está presente em todos os atos administrativos.","E","Só quando a lei prevê ou em urgência."),
 ("A imperatividade permite à Administração impor obrigações a terceiros independentemente de sua concordância.","C","Poder extroverso.")])

# ================================================================ UNIDADE 4
opener("04","UNIDADE 4","Tipos e classificação",["Espécies de atos","Atos negociais","Classificação dos atos","Perfeição, validade e eficácia"],"U4")

add(H(4,'Espécies de atos (<span class="hl">tipos</span>)','A classificação de Hely Lopes Meirelles, a mais cobrada.', "A14") +
 table(["Espécie","O que fazem","Exemplos"],[
  ["<b>Normativos</b>","Contêm comandos <b>gerais e abstratos</b> para a correta aplicação da lei","Decretos regulamentares, regulamentos, instruções normativas, regimentos, resoluções, deliberações"],
  ["<b>Ordinatórios</b>","Organizam o <b>funcionamento interno</b> da Administração e a conduta dos agentes","Portarias, ordens de serviço, circulares, avisos, ofícios, despachos"],
  ["<b>Negociais</b>","Atendem a um <b>interesse do particular</b>, que coincide com o interesse público","Licença, autorização, permissão, aprovação, homologação, admissão, visto, dispensa"],
  ["<b>Enunciativos</b>","<b>Atestam</b> um fato ou <b>emitem opinião</b>, sem manifestar vontade de produzir efeitos","Certidões, atestados, pareceres, apostilas"],
  ["<b>Punitivos</b>","Aplicam <b>sanções</b> a servidores ou particulares","Multas, interdição, advertência, suspensão, demissão"]],["18%",None,"34%"]) +
 ex(p('No mesmo dia, uma Prefeitura pode editar um <b>decreto</b> regulamentando a lei de feiras (normativo), uma <b>portaria</b> definindo o horário do setor de fiscalização (ordinatório), conceder um <b>alvará</b> a um feirante (negocial), emitir uma <b>certidão</b> de regularidade (enunciativo) e aplicar <b>multa</b> a um feirante irregular (punitivo).')) +
 memo('Espécies: <strong>NO-OR-NE-EN-PU</strong> (normativos, ordinatórios, negociais, enunciativos e punitivos).'))

add(H(4,'Atos negociais: <span class="hl">licença, autorização e permissão</span>','Os três mais confundidos.', "A15") +
 scene3([("LICENÇA",C['navy'],NV,"prof",["Cumpriu os","requisitos? Tem","direito ao alvará."],"VINCULADA · definitiva"),
  ("AUTORIZAÇÃO",C['blue'],C['sky'],"profa",["Posso autorizar o","uso da praça para","o seu evento.”"],"DISCRICIONÁRIA · precária"),
  ("PERMISSÃO",C['golddeep'],C['goldsoft'],"prof",["Permito o uso","da banca de","jornal na calçada."],"DISCRICIONÁRIA · precária")], "Situação ilustrada: os atos negociais mais cobrados.") +
 table(["","LICENÇA","AUTORIZAÇÃO","PERMISSÃO (de uso)"],[
  ["Natureza","<b>Vinculada</b>","<b>Discricionária</b>","<b>Discricionária</b>"],
  ["Estabilidade","Em regra, <b>definitiva</b>: há direito do particular","<b>Precária</b>: pode ser revogada a qualquer tempo","<b>Precária</b>"],
  ["Interesse predominante","Do particular, com requisitos legais","Do particular","Do particular e da coletividade"],
  ["Exemplos","Licença para construir; licença para dirigir (CNH)","Porte de arma; uso de praça para evento","Banca de jornal ou mesas de bar na calçada"]],["18%",None,None,None]) +
 memo('<strong>Licença</strong>: vinculada e definitiva (requisitos cumpridos = direito). <strong>Autorização</strong> e <strong>permissão</strong>: discricionárias e precárias.'))

add(H(4,'Classificação dos <span class="hl">atos</span>','Os critérios que mais caem.', "A16") +
 table(["Critério","Classificação"],[
  ["Destinatários","<b>Gerais</b> (destinatários indeterminados, como um regulamento) x <b>individuais</b> (destinatários certos, como uma nomeação)"],
  ["Alcance","<b>Internos</b> (efeitos dentro da Administração, como uma portaria de horário) x <b>externos</b> (atingem particulares)"],
  ["Prerrogativas","<b>De império</b> (com supremacia, como a interdição) x <b>de gestão</b> (sem supremacia, como a venda de um bem) x <b>de expediente</b> (rotina, como o protocolo)"],
  ["Liberdade","<b>Vinculados</b> x <b>discricionários</b>"],
  ["Formação da vontade","<b>Simples</b> (um órgão) x <b>complexos</b> (dois ou mais órgãos, cujas vontades se fundem em um único ato) x <b>compostos</b> (um ato principal e outro acessório, que o aprova ou ratifica)"],
  ["Efeitos","<b>Constitutivos</b> (criam ou extinguem situações) x <b>declaratórios</b> (reconhecem situação existente) x <b>enunciativos</b> (atestam ou opinam)"],
  ["Situação","<b>Pendente</b> (sujeito a condição ou termo) x <b>consumado</b> (já produziu todos os efeitos)"]],["22%",None]) +
 table(["","SIMPLES","COMPLEXO","COMPOSTO"],[
  ["Órgãos","Um","Dois ou mais","Dois ou mais"],
  ["Atos","Um ato","<b>Um único ato</b>, com vontades que se fundem","<b>Dois atos</b>: principal + acessório"],
  ["Exemplo didático","Nomeação por um secretário","Decreto assinado pelo Chefe do Executivo e referendado por ministro","Ato que depende de visto ou aprovação de autoridade superior"]],["16%",None,None,None]))

def linha():
    N,G,O=C['navy'],C['blue'],C['golddeep']
    it=[("PERFEITO","concluiu todas as","fases de formação",N,NV),("VÁLIDO","está de acordo","com a lei",G,C['sky']),("EFICAZ","está apto a","produzir efeitos",O,C['goldsoft'])]
    s = f'<figure><svg viewBox="0 0 640 150" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">{arrowdefs("lt")}'
    s += f'<line x1="20" y1="120" x2="620" y2="120" stroke="{C["ink"]}" stroke-width="3" marker-end="url(#lt)"/>'
    for k,(t,a,b,fg,bg) in enumerate(it):
        x=40+k*200
        s += f'<rect x="{x}" y="10" width="170" height="86" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x+85}" y="40" text-anchor="middle" font-size="14" font-weight="900" fill="{fg}">{t}</text><text x="{x+85}" y="62" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">{a}</text><text x="{x+85}" y="78" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">{b}</text><circle cx="{x+85}" cy="120" r="8" fill="{fg}"/>'
    s += f'<text x="320" y="145" text-anchor="middle" font-size="10" fill="{C["muted"]}">perfeição (existência) → validade (conformidade com a lei) → eficácia (aptidão para produzir efeitos)</text>'
    return s + '</svg><figcaption>Linha do tempo do ato: três planos diferentes.</figcaption></figure>'

add(H(4,'Perfeição, validade e <span class="hl">eficácia</span>','Um ato pode existir e ainda não valer, ou valer e ainda não produzir efeitos.', "A17") +
 linha() +
 table(["Combinação","Exemplo"],[
  ["Perfeito, válido e eficaz","Nomeação regular, já publicada"],
  ["Perfeito, válido e ineficaz","Ato regular, mas que só vale a partir de uma data futura (termo) ou depende de condição"],
  ["Perfeito, inválido e eficaz","Ato com vício, mas que produz efeitos enquanto não for anulado, graças à presunção de legitimidade"],
  ["Perfeito, inválido e ineficaz","Ato com vício e que ainda depende de publicação para produzir efeitos"]],["36%",None]) +
 memo('<strong>Perfeito</strong> = concluído. <strong>Válido</strong> = conforme a lei. <strong>Eficaz</strong> = apto a produzir efeitos. Ato inválido pode ser <strong>eficaz</strong> enquanto não anulado.'))

treino(4, [
 ("Certidões e pareceres são exemplos de atos enunciativos.","C","Atestam ou opinam."),
 ("A licença é ato discricionário e precário.","E","Licença é vinculada e, em regra, definitiva; autorização é que é discricionária e precária."),
 ("Portarias e ordens de serviço são exemplos de atos ordinatórios.","C","Organizam o funcionamento interno."),
 ("No ato complexo, há dois atos distintos: um principal e outro acessório.","E","Isso é ato composto; no complexo, as vontades se fundem em um único ato."),
 ("Um ato inválido pode produzir efeitos enquanto não for anulado.","C","Pela presunção de legitimidade."),
 ("Ato perfeito é aquele que está de acordo com a lei.","E","Perfeito é o que completou seu ciclo de formação; o conforme a lei é o válido.")])

# ================================================================ UNIDADE 5
opener("05","UNIDADE 5","Extinção dos atos",["Formas de extinção","Anulação","Revogação","Convalidação","Anulação x revogação x convalidação"],"U5")

add(H(5,'Formas de <span class="hl">extinção</span>','Como um ato deixa de existir (doutrina).', "A18") +
 table(["Forma","O que é","Exemplo"],[
  ["Extinção natural","O ato cumpre seus efeitos ou termina o prazo","Autorização de evento que já ocorreu"],
  ["Extinção subjetiva","Desaparece o sujeito beneficiado","Morte do permissionário de uma banca"],
  ["Extinção objetiva","Desaparece o objeto","Interdição de um prédio que desabou"],
  ["<b>Cassação</b>","O beneficiário <b>descumpre</b> as condições para continuar usufruindo do ato","Cassação de alvará de hotel que passou a funcionar como casa de jogos"],
  ["<b>Caducidade</b>","Uma <b>lei nova</b> torna o ato incompatível","Permissão para circo em área que nova lei transforma em residencial"],
  ["<b>Contraposição</b>","Um novo ato, com efeitos opostos, extingue o anterior","Exoneração extingue os efeitos da nomeação"],
  ["Renúncia","O beneficiário abre mão da vantagem","Servidor que renuncia a um cargo em comissão"],
  ["<b>Anulação</b>","Extinção por <b>ilegalidade</b>","Ver próxima página"],
  ["<b>Revogação</b>","Extinção por <b>conveniência e oportunidade</b>","Ver página seguinte"]],["20%",None,"34%"]) +
 memo('<strong>Cassação</strong> = culpa do beneficiário. <strong>Caducidade</strong> = lei nova. <strong>Contraposição</strong> = ato oposto. <strong>Anulação</strong> = ilegalidade. <strong>Revogação</strong> = conveniência.'))

add(H(5,'<span class="hl">Anulação</span>','A extinção do ato ilegal.', "A19") +
 lei("Arts. 53 e 54 · Lei nº 9.784/1999 (trechos e síntese)",'<p>Art. 53. A Administração deve anular seus próprios atos, quando eivados de vício de legalidade, e pode revogá-los por motivo de conveniência ou oportunidade, respeitados os direitos adquiridos.<br>Art. 54. O direito da Administração de anular os atos administrativos de que decorram efeitos favoráveis para os destinatários decai em cinco anos, contados da data em que foram praticados, salvo comprovada má-fé.</p>') +
 table(["Ponto","Regra"],[
  ["Motivo","<b>Ilegalidade</b> (vício em um dos elementos)"],
  ["Quem anula","A própria <b>Administração</b> (autotutela: de ofício ou provocada) e o <b>Poder Judiciário</b> (quando provocado)"],
  ["Efeitos","<b>Retroativos (ex tunc)</b>: o ato é desfeito desde a origem, ressalvados os direitos de terceiros de boa-fé"],
  ["Prazo","<b>5 anos</b> para anular atos que favorecem o destinatário, salvo má-fé (art. 54)"],
  ["Súmulas do STF","Súmula 346: a Administração pode declarar a nulidade dos seus próprios atos. Súmula 473: pode anulá-los quando ilegais, porque deles não se originam direitos, ou revogá-los por conveniência ou oportunidade, ressalvada a apreciação judicial"],
  ["Consequências (LINDB, art. 21)","A decisão que decretar a invalidação de ato deve indicar de modo expresso suas consequências jurídicas e administrativas"]],["24%",None]) +
 memo('Anulação: <strong>ilegalidade</strong> · Administração <strong>ou</strong> Judiciário · efeitos <strong>ex tunc</strong> · prazo de <strong>5 anos</strong> para atos favoráveis, salvo má-fé. A Administração <strong>deve</strong> anular.'))

add(H(5,'<span class="hl">Revogação</span>','A extinção do ato válido que deixou de ser conveniente.', "A20") +
 table(["Ponto","Regra"],[
  ["Motivo","<b>Conveniência e oportunidade</b> (mérito): o ato é <b>válido</b>, mas deixou de atender ao interesse público"],
  ["Quem revoga","<b>Só a Administração</b> que praticou o ato. O Judiciário só revoga os atos administrativos <b>que ele mesmo</b> pratica"],
  ["Efeitos","<b>Não retroativos (ex nunc)</b>: valem dali em diante, preservando os efeitos já produzidos"],
  ["Direitos adquiridos","Devem ser respeitados (Lei nº 9.784/1999, art. 53; Súmula 473 do STF)"]],["24%",None]) +
 table(["Atos que NÃO podem ser revogados (doutrina)","Por quê"],[
  ["Atos vinculados","Não há conveniência a avaliar"],
  ["Atos consumados (que já esgotaram seus efeitos)","Não há o que revogar"],
  ["Atos que geraram direitos adquiridos","Proteção constitucional do direito adquirido"],
  ["Atos enunciativos (certidões, atestados, pareceres)","Não manifestam vontade; apenas atestam ou opinam"],
  ["Atos de procedimento já superados (preclusão)","A fase seguinte já começou"]],["50%",None]) +
 ex(p('A Prefeitura autorizou um festival na praça para o mês que vem, mas, antes do evento, decide fazer ali uma obra urgente de drenagem. Ela pode <b>revogar</b> a autorização (ato discricionário e precário), por conveniência e oportunidade, com efeitos dali em diante. Já uma licença de construção concedida a quem cumpriu os requisitos não pode ser revogada por mera conveniência: é ato vinculado.')) +
 memo('Revogação: <strong>conveniência e oportunidade</strong> · <strong>só a Administração</strong> · efeitos <strong>ex nunc</strong> · respeita <strong>direitos adquiridos</strong>.'))

add(H(5,'<span class="hl">Convalidação</span>','Corrigir o ato com defeito sanável.', "A21") +
 lei("Art. 55 · Lei nº 9.784/1999",'<p>Art. 55. Em decisão na qual se evidencie não acarretarem lesão ao interesse público nem prejuízo a terceiros, os atos que apresentarem defeitos sanáveis poderão ser convalidados pela própria Administração.</p>') +
 table(["Requisitos (art. 55)","Explicação"],[
  ["Defeito sanável","O vício precisa ser corrigível"],
  ["Sem lesão ao interesse público","A correção não pode prejudicar a coletividade"],
  ["Sem prejuízo a terceiros","Ninguém pode ser prejudicado pela correção"],
  ["Pela própria Administração","Quem convalida é a Administração, com efeitos <b>retroativos (ex tunc)</b>"]],["30%",None]) +
 table(["Elemento viciado","Convalidável?"],[
  ["Competência","<b>Sim</b>, se não for exclusiva (a autoridade competente ratifica o ato)"],
  ["Forma","<b>Sim</b>, se a forma não for essencial à validade"],
  ["Finalidade","<b>Não</b> (desvio de finalidade é insanável)"],
  ["Motivo","<b>Não</b> (motivo falso ou inexistente não se corrige)"],
  ["Objeto","Em regra, <b>não</b>; a doutrina admite a <b>conversão</b> em outro ato quando o objeto é plúrimo"]],["30%",None]) +
 memo('Convalidação: só <strong>competência</strong> (não exclusiva) e <strong>forma</strong> (não essencial) = <strong>"FoCo"</strong>. Efeitos <strong>ex tunc</strong>. Finalidade, motivo e objeto: em regra, <strong>não</strong>.'))

ar = scene3([("ANULAÇÃO",C['red'],C['redsoft'],"prof",["“O alvará foi","dado contra a","lei: anulo.”"],"ILEGALIDADE · ex tunc"),
 ("REVOGAÇÃO",C['blue'],C['sky'],"profa",["“A autorização","não é mais","conveniente.”"],"MÉRITO · ex nunc"),
 ("CONVALIDAÇÃO",C['green'],C['greensoft'],"prof",["“Ratifico o ato","que o assessor","assinou por engano.”"],"VÍCIO SANÁVEL · ex tunc")], "Situação ilustrada: três formas de lidar com um ato.")
add(H(5,'Anulação x revogação x <span class="hl">convalidação</span>','O quadro que resolve as questões.', "A22") + ar +
 table(["","ANULAÇÃO","REVOGAÇÃO","CONVALIDAÇÃO"],[
  ["Motivo","Ilegalidade","Conveniência e oportunidade","Vício sanável"],
  ["Ato","Inválido","Válido","Inválido (com defeito sanável)"],
  ["Quem faz","Administração e Judiciário","Só a Administração (ou o Judiciário quanto aos seus próprios atos administrativos)","A própria Administração"],
  ["Efeitos","Ex tunc (retroativos)","Ex nunc (para o futuro)","Ex tunc (retroativos)"],
  ["Base legal","Lei nº 9.784/1999, art. 53; Súmulas 346 e 473","Lei nº 9.784/1999, art. 53; Súmula 473","Lei nº 9.784/1999, art. 55"]],["14%",None,None,None]))

atencao(
 ex(p('Um assessor, sem competência, assina o alvará de um quiosque que cumpria todos os requisitos. O secretário, que era o competente, <b>ratifica</b> o ato: <b>convalidação</b> por vício de competência não exclusiva. Outro alvará, concedido para um quiosque em área onde a lei proíbe comércio, tem vício de objeto e deve ser <b>anulado</b>. E a autorização de um evento que deixou de ser oportuna é <b>revogada</b>.')) +
 pega('<ul><li>O Judiciário <b>não revoga</b> atos da Administração; ele <b>anula</b> os ilegais.</li><li>Anulação e convalidação retroagem (<b>ex tunc</b>); a revogação vale para o futuro (<b>ex nunc</b>).</li><li>A Administração <b>deve</b> anular o ato ilegal, mas o prazo para anular ato favorável ao destinatário é de <b>5 anos</b>, salvo má-fé.</li><li>Desvio de finalidade e motivo inexistente <b>não</b> se convalidam.</li></ul>'),
 ["anulação · ex tunc","revogação · ex nunc","convalidação","autotutela","Súmula 473","5 anos"])

treino(5, [
 ("A anulação ocorre por ilegalidade e pode ser feita pela Administração ou pelo Poder Judiciário.","C","Lei nº 9.784/1999, art. 53; Súmula 473."),
 ("A revogação produz efeitos retroativos (ex tunc).","E","Produz efeitos ex nunc."),
 ("O Poder Judiciário pode revogar ato discricionário do Poder Executivo por considerá-lo inconveniente.","E","Só a própria Administração revoga; o Judiciário anula atos ilegais."),
 ("Atos com defeitos sanáveis podem ser convalidados pela própria Administração, se não houver lesão ao interesse público nem prejuízo a terceiros.","C","Lei nº 9.784/1999, art. 55."),
 ("O vício de finalidade pode ser convalidado.","E","Desvio de finalidade é insanável."),
 ("A cassação ocorre quando o beneficiário descumpre as condições que deveria manter para continuar usufruindo do ato.","C","Forma de extinção.")])

# ================================================================ REVISÃO
mapa(("ATOS","ADMINIS-","TRATIVOS"), [
  ("CONCEITO",["declaração unilateral","efeitos jurídicos","direito público"],C['navy'],NV),
  ("ELEMENTOS",["COM-FI-FOR-M-OB","quem, para quê, como,","por quê, o quê"],C['golddeep'],C['goldsoft']),
  ("ATRIBUTOS",["PATI","presunção: em todos","autoexec.: quando a lei prevê"],C['blue'],C['sky']),
  ("ESPÉCIES",["normativos, ordinatórios","negociais, enunciativos","punitivos"],C['green'],C['greensoft']),
  ("ANULAÇÃO",["ilegalidade · ex tunc","Adm. e Judiciário","5 anos (favoráveis)"],C['red'],C['redsoft']),
  ("REVOGAÇÃO",["mérito · ex nunc","só a Administração","convalidação: FoCo"],C['navy'],NV)], "Mapa conceitual do Caderno 11.", "O caderno em seis blocos. Explique cada caixa em voz alta.")

erros([
  ["“Motivo e motivação são a mesma coisa.”","Motivo é o fato e o direito; motivação é a exposição escrita dos motivos."],
  ["“A finalidade pode ser discricionária.”","É sempre vinculada; só motivo e objeto podem ser discricionários."],
  ["“A presunção de legitimidade é absoluta.”","É relativa e admite prova em contrário."],
  ["“Todo ato administrativo é autoexecutório.”","Só quando a lei prevê ou há urgência."],
  ["“A licença é discricionária.”","A licença é vinculada; a autorização é discricionária."],
  ["“Certidão tem imperatividade.”","Atos enunciativos não impõem obrigações."],
  ["“No ato complexo há dois atos.”","No complexo há um único ato; no composto, dois (principal e acessório)."]],
 [["“Ato válido é o que completou seu ciclo de formação.”","Isso é ato perfeito; válido é o conforme a lei."],
  ["“O Judiciário pode revogar atos da Administração.”","Só anula os ilegais; revogar é da Administração."],
  ["“A revogação retroage.”","Revogação tem efeitos ex nunc; anulação e convalidação, ex tunc."],
  ["“A Administração pode anular ato favorável a qualquer tempo.”","Prazo de 5 anos, salvo comprovada má-fé (Lei nº 9.784/1999, art. 54)."],
  ["“Qualquer vício pode ser convalidado.”","Só competência (não exclusiva) e forma (não essencial)."],
  ["“Ato vinculado pode ser revogado.”","Atos vinculados não são revogáveis por conveniência."],
  ["“Cassação e caducidade são sinônimos.”","Cassação: descumprimento pelo beneficiário. Caducidade: lei nova incompatível."]])

flashcards([("CONCEITO","O que é ato administrativo?","Declaração unilateral do Estado com efeitos jurídicos, sob regime de direito público, sujeita a controle."),
 ("CONCEITO","Ato x fato administrativo?","Ato: declaração de vontade. Fato: execução material ou acontecimento."),
 ("ELEMENTOS","Quais são os cinco elementos?","Competência, finalidade, forma, motivo e objeto."),
 ("ELEMENTOS","Quais elementos são sempre vinculados?","Competência, finalidade e forma (em regra)."),
 ("ELEMENTOS","Excesso de poder x usurpação de função?","Excesso: agente vai além da competência. Usurpação: quem não é agente pratica o ato."),
 ("ELEMENTOS","Motivo x motivação?","Motivo: fato e direito. Motivação: exposição dos motivos."),
 ("ELEMENTOS","Requisitos do objeto?","Lícito, possível, certo e moral."),
 ("ELEMENTOS","O que é o mérito administrativo?","Escolha de conveniência e oportunidade, no motivo e no objeto."),
 ("ATRIBUTOS","Quais são os atributos (PATI)?","Presunção de legitimidade, autoexecutoriedade, tipicidade e imperatividade."),
 ("ATRIBUTOS","Qual atributo está em todos os atos?","A presunção de legitimidade e veracidade."),
 ("ATRIBUTOS","Exigibilidade x executoriedade?","Exigibilidade: coerção indireta (multa). Executoriedade: coerção direta (apreensão)."),
 ("ATRIBUTOS","A cobrança forçada de multa é autoexecutória?","Não. Exige execução judicial."),
 ("ESPÉCIES","Cinco espécies de atos (Hely)?","Normativos, ordinatórios, negociais, enunciativos e punitivos."),
 ("ESPÉCIES","Licença x autorização?","Licença: vinculada e definitiva. Autorização: discricionária e precária."),
 ("CLASSIFICAÇÃO","Ato complexo x composto?","Complexo: um ato com vontades fundidas. Composto: principal + acessório."),
 ("CLASSIFICAÇÃO","Perfeito, válido e eficaz?","Perfeito: concluído. Válido: conforme a lei. Eficaz: apto a produzir efeitos."),
 ("EXTINÇÃO","Cassação?","Extinção porque o beneficiário descumpriu as condições."),
 ("EXTINÇÃO","Caducidade?","Extinção porque lei nova tornou o ato incompatível."),
 ("EXTINÇÃO","Anulação: motivo, quem e efeitos?","Ilegalidade; Administração e Judiciário; ex tunc."),
 ("EXTINÇÃO","Revogação: motivo, quem e efeitos?","Conveniência e oportunidade; só a Administração; ex nunc."),
 ("EXTINÇÃO","Prazo para anular ato favorável?","5 anos, salvo comprovada má-fé (Lei 9.784, art. 54)."),
 ("EXTINÇÃO","Quais atos não podem ser revogados?","Vinculados, consumados, que geraram direitos adquiridos e enunciativos."),
 ("CONVALIDAÇÃO","Requisitos do art. 55 da Lei 9.784?","Defeito sanável, sem lesão ao interesse público nem prejuízo a terceiros."),
 ("CONVALIDAÇÃO","Que vícios são convalidáveis?","Competência (não exclusiva) e forma (não essencial).")])

Q = [
 ("Conceito","Sobre o ato administrativo, é correto afirmar:",
  ["é sempre bilateral, como os contratos.","é declaração unilateral do Estado ou de quem o represente, com efeitos jurídicos, sob regime de direito público.","só pode ser praticado pelo Poder Executivo.","não está sujeito a controle judicial.","confunde-se com o fato administrativo."],"B",
  "Conceito doutrinário: declaração unilateral, efeitos jurídicos, regime de direito público, controle judicial; praticado pelos três Poderes na função administrativa.","Unilateral + efeitos + direito público."),
 ("Fato administrativo","A execução material da demolição de uma obra irregular, após decisão administrativa, é exemplo de:",
  ["ato normativo.","ato enunciativo.","fato administrativo.","ato complexo.","contrato administrativo."],"C",
  "A decisão é o ato; a execução material (derrubar a obra) é fato administrativo.","Execução material = fato."),
 ("Elementos","São elementos do ato administrativo, segundo a doutrina majoritária:",
  ["competência, finalidade, forma, motivo e objeto.","presunção, imperatividade, autoexecutoriedade e tipicidade.","legalidade, impessoalidade, moralidade, publicidade e eficiência.","perfeição, validade e eficácia.","anulação, revogação e convalidação."],"A",
  "Os cinco elementos derivam dos vícios do art. 2º da Lei nº 4.717/1965. Presunção, imperatividade etc. são atributos.","COM-FI-FOR-M-OB."),
 ("Competência","Pessoa que não é agente público pratica ato fingindo sê-lo. Trata-se de:",
  ["excesso de poder.","desvio de finalidade.","usurpação de função.","função de fato.","vício de forma sanável."],"C",
  "Na usurpação, quem pratica o ato nem é agente público; o ato é considerado inexistente, e a conduta é crime (CP, art. 328).","Nem é agente = usurpação."),
 ("Finalidade","O prefeito remove servidor para local distante apenas para puni-lo por críticas à gestão. O vício está no elemento:",
  ["competência.","forma.","finalidade.","objeto.","motivo, apenas."],"C",
  "Desvio de finalidade: ato praticado para fim diverso do previsto na regra de competência (Lei nº 4.717/1965, art. 2º, parágrafo único, e).","Fim diverso = desvio de finalidade."),
 ("Forma","Sobre a forma do ato administrativo, é correto afirmar:",
  ["admite apenas a forma escrita, sem exceções.","em regra é escrita, mas admite gestos e sinais, como os do agente de trânsito.","o silêncio administrativo sempre equivale a deferimento.","nunca pode ser convalidada.","não se relaciona com a motivação."],"B",
  "A regra é a forma escrita; há exceções (gestos, sinais, ordens verbais). O silêncio só produz efeitos quando a lei prevê; vício de forma não essencial é convalidável.","Forma: escrita em regra; gestos valem."),
 ("Motivo","O pressuposto de fato e de direito que autoriza ou exige a prática do ato denomina-se:",
  ["motivação.","objeto.","motivo.","finalidade.","forma."],"C",
  "Motivo é o pressuposto; motivação é a exposição escrita desse pressuposto.","Motivo = fato + direito."),
 ("Motivos determinantes","Exonerado de cargo em comissão sob a alegação de “corte de gastos”, o servidor prova que, no dia seguinte, outra pessoa foi nomeada para o mesmo cargo. Pela teoria dos motivos determinantes, o ato:",
  ["é válido, porque a exoneração de comissionado é livre.","é nulo, porque o motivo declarado se mostrou falso.","só pode ser revogado.","é válido, pois a motivação era dispensável.","é convalidável pela autoridade."],"B",
  "Embora a exoneração de comissionado dispense motivação, o motivo declarado vincula o ato; motivo falso leva à nulidade.","Motivo declarado vincula."),
 ("Discricionariedade","No ato discricionário, os elementos que podem conter margem de escolha (mérito) são:",
  ["competência e finalidade.","forma e competência.","motivo e objeto.","finalidade e forma.","todos os cinco elementos."],"C",
  "Competência, finalidade e forma são vinculadas; motivo e objeto podem ser discricionários.","M-OB = mérito."),
 ("Atributos","O atributo presente em todos os atos administrativos é a:",
  ["imperatividade.","autoexecutoriedade.","presunção de legitimidade e veracidade.","tipicidade, apenas nos atos normativos.","exigibilidade."],"C",
  "A presunção (relativa) existe em todos os atos; imperatividade e autoexecutoriedade não.","Presunção: em todos."),
 ("Presunção","A presunção de legitimidade dos atos administrativos:",
  ["é absoluta.","é relativa e transfere a quem contesta o ato o ônus de provar o vício.","impede o controle judicial.","só existe nos atos vinculados.","dispensa a publicidade."],"B",
  "Presunção relativa (iuris tantum): admite prova em contrário, a cargo de quem alega o vício.","Presunção relativa."),
 ("Imperatividade","NÃO possui imperatividade:",
  ["a ordem de demolição de obra irregular.","a interdição de estabelecimento.","a multa de trânsito.","a certidão negativa de débitos.","a requisição administrativa."],"D",
  "Atos enunciativos (certidões, atestados) e negociais não impõem obrigações ao particular.","Certidão não impõe nada."),
 ("Autoexecutoriedade","Depende de execução judicial, por não ser autoexecutória:",
  ["a apreensão de alimentos estragados.","a cobrança forçada de multa administrativa não paga.","a interdição de prédio em risco de desabamento.","a remoção de veículo estacionado irregularmente.","a destruição de mercadoria imprópria ao consumo."],"B",
  "A cobrança forçada da multa exige execução fiscal; as demais medidas são autoexecutórias por previsão legal ou urgência.","Cobrar multa à força = Justiça."),
 ("Espécies","Pareceres, certidões e atestados são exemplos de atos:",
  ["normativos.","ordinatórios.","negociais.","enunciativos.","punitivos."],"D",
  "Atos enunciativos atestam um fato ou emitem opinião.","Atesta ou opina = enunciativo."),
 ("Negociais","Sobre licença e autorização, é correto afirmar:",
  ["ambas são vinculadas.","a licença é vinculada e a autorização é discricionária e precária.","a licença é discricionária e precária.","a autorização gera direito adquirido ao particular.","ambas são atos punitivos."],"B",
  "Licença: requisitos cumpridos geram direito (vinculada). Autorização: discricionária e precária, revogável a qualquer tempo.","Licença vincula; autorização é precária."),
 ("Classificação","O ato que resulta da manifestação de dois ou mais órgãos, cujas vontades se fundem para formar um único ato, é classificado como:",
  ["simples.","composto.","complexo.","consumado.","pendente."],"C",
  "Complexo: vontades fundidas em um único ato. Composto: um ato principal e outro acessório.","Fundiu = complexo."),
 ("Eficácia","O ato que concluiu seu ciclo de formação, mas depende de termo futuro para produzir efeitos, é:",
  ["imperfeito.","perfeito e ineficaz.","inválido e eficaz.","consumado.","inexistente."],"B",
  "Perfeito é o ato concluído; eficaz é o apto a produzir efeitos. Sujeito a termo, ainda é ineficaz.","Concluído, mas sem efeito ainda = perfeito e ineficaz."),
 ("Extinção","A extinção do ato porque o beneficiário deixou de cumprir as condições necessárias à sua manutenção denomina-se:",
  ["caducidade.","contraposição.","cassação.","revogação.","renúncia."],"C",
  "Cassação decorre do descumprimento pelo beneficiário; caducidade, de lei nova incompatível.","Descumpriu = cassação."),
 ("Anulação","Sobre a anulação dos atos administrativos, assinale a correta:",
  ["só pode ser feita pelo Poder Judiciário.","decorre de conveniência e oportunidade.","decorre de ilegalidade e produz, em regra, efeitos retroativos.","produz sempre efeitos ex nunc.","não tem prazo em nenhuma hipótese."],"C",
  "Anulação: ilegalidade, pela Administração ou pelo Judiciário, efeitos ex tunc, com prazo de 5 anos para atos favoráveis, salvo má-fé.","Anulação: ilegal, ex tunc."),
 ("Prazo","Segundo a Lei nº 9.784/1999, o direito da Administração de anular atos de que decorram efeitos favoráveis aos destinatários decai em:",
  ["1 ano.","2 anos.","3 anos.","5 anos, salvo comprovada má-fé.","10 anos."],"D",
  "Art. 54 da Lei nº 9.784/1999.","5 anos, salvo má-fé."),
 ("Revogação","A revogação do ato administrativo:",
  ["pode ser feita pelo Judiciário em relação aos atos do Executivo.","decorre de ilegalidade.","decorre de conveniência e oportunidade, produz efeitos ex nunc e respeita direitos adquiridos.","alcança os atos vinculados.","retroage à data do ato revogado."],"C",
  "Lei nº 9.784/1999, art. 53, e Súmula 473 do STF.","Revogação: mérito, ex nunc."),
 ("Revogação","NÃO pode ser revogado:",
  ["a autorização de uso de praça para evento futuro.","a permissão de uso de calçada.","o ato vinculado de licença concedido a quem cumpriu os requisitos.","a autorização de porte concedida de forma precária.","a ordem de serviço interna ainda não executada."],"C",
  "Atos vinculados, consumados, que geraram direitos adquiridos e enunciativos não são revogáveis.","Vinculado não se revoga."),
 ("Convalidação","De acordo com a Lei nº 9.784/1999, podem ser convalidados pela própria Administração os atos:",
  ["com qualquer vício, desde que haja interesse do servidor.","com defeitos sanáveis, quando não houver lesão ao interesse público nem prejuízo a terceiros.","com desvio de finalidade.","com motivo inexistente.","já anulados pelo Judiciário."],"B",
  "Art. 55. Em regra, convalidam-se vícios de competência não exclusiva e de forma não essencial.","Convalidação: sanável, sem lesão e sem prejuízo."),
 ("Comparação","Assinale a alternativa que relaciona corretamente o instituto e seus efeitos:",
  ["anulação · ex nunc; revogação · ex tunc.","anulação · ex tunc; revogação · ex nunc; convalidação · ex tunc.","anulação · ex nunc; convalidação · ex nunc.","revogação · ex tunc; convalidação · ex nunc.","todos produzem efeitos ex nunc."],"B",
  "Anulação e convalidação retroagem (ex tunc); revogação vale para o futuro (ex nunc).","Revogação é a única ex nunc.")]
questoes(Q, "BCAEDBCBDCBDBEBCBCDACBEB")
respostas_treinos()

referencias('''<h3>Legislação consultada (portal do Planalto)</h3><ul>
<li>Lei nº 4.717/1965 (Ação Popular): art. 2º.</li>
<li>Lei nº 9.784/1999: arts. 11, 13, 50, 53, 54 e 55.</li>
<li>Decreto-Lei nº 4.657/1942 (LINDB): arts. 20, 21 e 24.</li>
<li>Citado sem conferência nesta edição: Código Penal, art. 328 (conferido para o Caderno 07).</li></ul>
<h3>Jurisprudência citada</h3><ul><li>STF: Súmulas 346 e 473.</li></ul>''',
 'A base legal foi conferida nos textos do portal do Planalto, que exibem a redação vigente com as notas de alteração. <strong>Limitações:</strong> os textos do Planalto não informam a data da última atualização e não substituem o Diário Oficial. O conceito de ato administrativo, os elementos, os atributos, as espécies (classificação de Hely Lopes Meirelles), os critérios de classificação, as formas de extinção e a lista de atos irrevogáveis são <strong>construções doutrinárias</strong>, apresentadas na forma mais aceita; há divergências entre autores, especialmente nos exemplos de atos complexos e compostos. As Súmulas 346 e 473 do STF não foram reconferidas no portal oficial do tribunal nesta edição. Confira o edital do seu concurso.', DATA)
encerramento("11", "Direito Administrativo", 'Sugestão de continuação: <strong>Caderno 12 · Agentes Públicos</strong>.')
gravar(HERE, "Mapa da Aprovação — Caderno 11 — Atos Administrativos", Q)
