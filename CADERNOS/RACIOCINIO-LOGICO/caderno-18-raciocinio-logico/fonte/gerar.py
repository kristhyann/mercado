"""Gera miolo.html do Caderno 18: Raciocínio Lógico — Fundamentos e Questões. Uso: python3 gerar.py
Todos os cálculos e tabelas-verdade foram conferidos (ver verificar() ao final)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit
from kit import *

DATA = "26 de novembro de 2026"
kit.U = {1:("UNIDADE 1","Proposições"),2:("UNIDADE 2","Conectivos e tabelas-verdade"),3:("UNIDADE 3","Equivalências e negações"),4:("UNIDADE 4","Argumentação"),5:("UNIDADE 5","Sequências"),6:("UNIDADE 6","Matemática básica e problemas")}

def v(x): return f'<span style="display:inline-block;min-width:20px;font-weight:900;color:{C["green"] if x=="V" else C["red"]}">{x}</span>'
def tv(head, rows, dest=None, cap=""):
    """Tabela-verdade visual. dest = índice da coluna destacada."""
    th = "".join(f'<th style="text-align:center">{h}</th>' for h in head)
    trs = ""
    for r in rows:
        tds = ""
        for i,x in enumerate(r):
            bg = (C['goldsoft'] if i==dest else "#fff")
            tds += f'<td style="text-align:center;background:{bg}">{v(x)}</td>'
        trs += f"<tr>{tds}</tr>"
    c = f'<p style="text-align:center;font-size:9pt;color:{C["muted"]};margin-top:-4pt"><i>{cap}</i></p>' if cap else ""
    return f'<table style="width:auto;margin:0 auto 8pt;min-width:60%"><tr>{th}</tr>{trs}</table>{c}'

B4 = [("V","V"),("V","F"),("F","V"),("F","F")]
def col(f): return [f(p=="V", q=="V") for p,q in B4]
def VF(b): return "V" if b else "F"

# ---------------- diagramas ----------------
def venn(tipo):
    s = f'<svg viewBox="0 0 200 134" width="190" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    A, Bc = C['blue'], C['golddeep']
    if tipo=="todo":
        s += f'<circle cx="100" cy="58" r="50" fill="{C["goldsoft"]}" stroke="{Bc}" stroke-width="2.5"/><circle cx="94" cy="64" r="25" fill="{C["sky"]}" stroke="{A}" stroke-width="2.5"/><text x="94" y="69" text-anchor="middle" font-size="13" font-weight="900" fill="{A}">A</text><text x="128" y="36" font-size="13" font-weight="900" fill="{Bc}">B</text>'
        t = "Todo A é B"
    elif tipo=="nenhum":
        s += f'<circle cx="55" cy="62" r="40" fill="{C["sky"]}" stroke="{A}" stroke-width="2.5"/><circle cx="148" cy="62" r="40" fill="{C["goldsoft"]}" stroke="{Bc}" stroke-width="2.5"/><text x="55" y="67" text-anchor="middle" font-size="13" font-weight="900" fill="{A}">A</text><text x="148" y="67" text-anchor="middle" font-size="13" font-weight="900" fill="{Bc}">B</text>'
        t = "Nenhum A é B"
    else:
        s += f'<circle cx="75" cy="62" r="45" fill="{C["sky"]}" fill-opacity=".8" stroke="{A}" stroke-width="2.5"/><circle cx="128" cy="62" r="45" fill="{C["goldsoft"]}" fill-opacity=".7" stroke="{Bc}" stroke-width="2.5"/><text x="55" y="67" text-anchor="middle" font-size="13" font-weight="900" fill="{A}">A</text><text x="150" y="67" text-anchor="middle" font-size="13" font-weight="900" fill="{Bc}">B</text><text x="101" y="67" text-anchor="middle" font-size="16" font-weight="900" fill="{C["red"]}">x</text>'
        t = "Algum A é B"
    return s + f'<text x="100" y="128" text-anchor="middle" font-size="12" font-weight="900" fill="{C["ink"]}">{t}</text></svg>'

def venn3():
    return f'<figure style="display:flex;justify-content:space-around">{venn("todo")}{venn("algum")}{venn("nenhum")}</figure><figcaption>Diagramas de Venn dos quantificadores. Em “algum A é B”, o x marca pelo menos um elemento comum.</figcaption>'

def seq_visual():
    s = f'<figure><svg viewBox="0 0 640 170" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    for r,(t,nums,op,fg,bg) in enumerate([("PROGRESSÃO ARITMÉTICA",["3","7","11","15","19"],"+4",C['blue'],C['sky']),("PROGRESSÃO GEOMÉTRICA",["2","6","18","54","162"],"×3",C['golddeep'],C['goldsoft'])]):
        y=18+r*78
        s += f'<text x="14" y="{y+30}" font-size="11.5" font-weight="900" fill="{fg}">{t}</text>'
        for i,n in enumerate(nums):
            x=210+i*86
            s += f'<rect x="{x}" y="{y+8}" width="56" height="38" rx="9" fill="{bg}" stroke="{fg}" stroke-width="2.4"/><text x="{x+28}" y="{y+33}" text-anchor="middle" font-size="16" font-weight="900" fill="{C["ink"]}">{n}</text>'
            if i<4: s += f'<path d="M{x+58} {y+10} q14 -16 28 0" fill="none" stroke="{fg}" stroke-width="2"/><text x="{x+72}" y="{y+2}" text-anchor="middle" font-size="11" font-weight="900" fill="{fg}">{op}</text>'
    return s + '</svg><figcaption>Na PA soma-se sempre o mesmo número (razão); na PG multiplica-se sempre pelo mesmo número.</figcaption></figure>'

def fatores():
    s = f'<figure><svg viewBox="0 0 640 150" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">{arrowdefs("fz")}'
    for x,t,a,fg,bg in [(80,"R$ 100","preço inicial",C['navy'],NV),(320,"R$ 120","+20% (× 1,20)",C['green'],C['greensoft']),(560,"R$ 96","−20% (× 0,80)",C['red'],C['redsoft'])]:
        s += f'<rect x="{x-70}" y="20" width="140" height="64" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x}" y="52" text-anchor="middle" font-size="19" font-weight="900" fill="{fg}">{t}</text><text x="{x}" y="72" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">{a}</text>'
    s += f'<g stroke="{C["ink"]}" stroke-width="3" marker-end="url(#fz)"><line x1="152" y1="52" x2="246" y2="52"/><line x1="392" y1="52" x2="486" y2="52"/></g>'
    s += f'<text x="320" y="118" text-anchor="middle" font-size="12.5" font-weight="900" fill="{C["navy"]}">1,20 × 0,80 = 0,96 → o preço final é 4% menor que o inicial.</text><text x="320" y="138" text-anchor="middle" font-size="10.5" fill="{C["muted"]}">Aumento e desconto de mesmo percentual NÃO se anulam: os percentuais incidem sobre bases diferentes.</text>'
    return s + '</svg><figcaption>Percentuais sucessivos: multiplique os fatores.</figcaption></figure>'

def grade_logica():
    ck, xx = f'<b style="color:{C["green"]}">✔</b>', f'<span style="color:{C["red"]}">✗</span>'
    return table(["","Praça","Escola","Mercado"],[["Ana",ck,xx,xx],["Bruno",xx,xx,ck],["Carla",xx,ck,xx]],["22%","26%","26%",None])

# ================================================================ APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">Raciocínio lógico se aprende resolvendo: cada assunto vem com o passo a passo, não só com a fórmula.</p>
<p>Este é o <strong>Caderno 18 da coleção</strong>, dedicado ao <strong>Raciocínio Lógico</strong>. A disciplina assusta muita gente, mas segue regras fixas: uma condicional só é falsa em <strong>um</strong> caso; uma negação de “e” vira “ou”; um aumento de 20% seguido de desconto de 20% <strong>não</strong> volta ao preço inicial. Entendendo o porquê, você não precisa decorar tabelas inteiras.</p>
<p>Use lápis e papel. Antes de ler a resolução de cada exemplo, tente fazer sozinho. Os <strong>desafios</strong> espalhados pelo caderno trazem a resposta logo abaixo, para você conferir.</p>
{table(["Recurso","Onde está"],[["O que é e o que não é proposição","Unidade 1"],["Tabelas-verdade coloridas dos cinco conectivos","Unidade 2"],["Quadro de negações e equivalências com exemplos","Unidade 3"],["Diagramas de Venn e argumentos válidos","Unidade 4"],["Sequências numéricas e de figuras","Unidade 5"],["Porcentagem, regra de três e problemas de lógica resolvidos","Unidade 6"],["Mapa conceitual, erros comuns, flashcards e 24 questões autorais","Revisão e prática"]],["58%",None])}''', first=True)

toc_page([("u","UNIDADE 1 · PROPOSIÇÕES","U1"),("","1. O que é proposição","A01"),("","2. Simples e compostas","A02"),
 ("u","UNIDADE 2 · CONECTIVOS E TABELAS-VERDADE","U2"),("","3. Negação, conjunção e disjunção","A03"),("","4. Condicional e bicondicional","A04"),("","5. Montando tabelas-verdade","A05"),
 ("u","UNIDADE 3 · EQUIVALÊNCIAS E NEGAÇÕES","U3"),("","6. Equivalências lógicas","A06"),("","7. Negação de proposições compostas","A07"),("","8. Quantificadores","A08"),
 ("u","UNIDADE 4 · ARGUMENTAÇÃO","U4"),("","9. Argumento válido","A09"),("","10. Diagramas e silogismos","A10"),
 ("u","UNIDADE 5 · SEQUÊNCIAS","U5"),("","11. Sequências numéricas","A11"),("","12. Sequências de letras e figuras","A12"),
 ("u","UNIDADE 6 · MATEMÁTICA BÁSICA E PROBLEMAS","U6"),("","13. Porcentagem","A13"),("","14. Razão, proporção e regra de três","A14"),("","15. Problemas de lógica","A15"),
 ("u","REVISÃO E PRÁTICA","RV"),("","Mapa conceitual · Erros mais comuns","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),("","Gabarito, respostas dos treinos e referências","R4")])

# ================================================================ UNIDADE 1
opener("01","UNIDADE 1","Proposições",["O que é proposição","Simples e compostas"],"U1")

add(H(1,'O que é <span class="hl">proposição</span>','A matéria-prima da lógica.', "A01") +
 oque(p('<strong>Proposição</strong> é uma oração <strong>declarativa</strong> que pode ser classificada como <strong>verdadeira (V)</strong> ou <strong>falsa (F)</strong>, mas não as duas coisas ao mesmo tempo.')) +
 table(["Frase","É proposição?","Por quê"],[
  ["Brasília é a capital do Brasil.","<b>Sim</b>","Declarativa, valor V"],
  ["O Sol gira em torno da Terra.","<b>Sim</b>","Declarativa, valor F (ser falsa não impede de ser proposição)"],
  ["Que horas são?","Não","Pergunta"],
  ["Feche a porta.","Não","Ordem"],
  ["Que dia lindo!","Não","Exclamação"],
  ["x + 3 = 7","Não","Sentença aberta: o valor depende de x"],
  ["Ele é guarda municipal.","Não","Sentença aberta: “ele” não está definido"],
  ["Esta frase é falsa.","Não","Paradoxo: se for V, é F; se for F, é V"]],["40%","18%",None]) +
 table(["Princípio","O que diz"],[
  ["Identidade","Uma proposição verdadeira é verdadeira; uma falsa é falsa"],
  ["Não contradição","Nenhuma proposição é V e F ao mesmo tempo"],
  ["Terceiro excluído","Toda proposição é V ou F; não existe terceira opção"]],["30%",None]) +
 pega('<ul><li>Frase <b>falsa</b> também é proposição: o que importa é poder receber um valor.</li><li>Sentenças com variável (x, ele, alguém indefinido) <b>não</b> são proposições até que a variável seja definida.</li></ul>'))

add(H(1,'Simples e <span class="hl">compostas</span>','Juntando proposições com conectivos.', "A02") +
 table(["Tipo","Definição","Exemplo"],[
  ["Simples","Uma única ideia, sem conectivo","p: “Ana é guarda.”"],
  ["Composta","Duas ou mais proposições ligadas por conectivos","“Ana é guarda <b>e</b> Bruno é agente.”"]],["18%","40%",None]) +
 table(["Conectivo","Símbolo","Leitura","Exemplo"],[
  ["Negação","~ (ou ¬)","não p","Ana <b>não</b> é guarda."],
  ["Conjunção","∧","p e q","Ana é guarda <b>e</b> Bruno é agente."],
  ["Disjunção inclusiva","∨","p ou q","Ana é guarda <b>ou</b> Bruno é agente."],
  ["Disjunção exclusiva","⊻","ou p ou q","<b>Ou</b> Ana é guarda <b>ou</b> é agente."],
  ["Condicional","→","se p, então q","<b>Se</b> chover, <b>então</b> a ronda é suspensa."],
  ["Bicondicional","↔","p se e somente se q","A porta abre <b>se e somente se</b> o crachá é aceito."]],["22%","12%","22%",None]) +
 traduz(p('Antes de qualquer cálculo, <strong>dê nome às partes</strong>. Em “Se o agente está de plantão, então está fardado”, chame p = “o agente está de plantão” e q = “está fardado”. A frase vira p → q. Essa tradução para símbolos é metade da resolução.')) +
 memo('Cinco conectivos: <strong>não (~), e (∧), ou (∨), ou…ou (⊻), se…então (→), se e somente se (↔)</strong>.'))

treino(1, [
 ("“O Brasil fica na Europa” é uma proposição, pois pode ser julgada como falsa.","C","Ser falsa não impede de ser proposição."),
 ("“Estude para a prova!” é uma proposição.","E","Ordem não é proposição."),
 ("“x − 2 = 10” é uma proposição simples.","E","Sentença aberta: depende de x."),
 ("Pelo princípio da não contradição, uma proposição não pode ser verdadeira e falsa ao mesmo tempo.","C","Princípio básico."),
 ("“Ana estuda e Bruno trabalha” é uma proposição composta por conjunção.","C","Conectivo “e”."),
 ("O símbolo → representa a bicondicional.","E","→ é condicional; ↔ é bicondicional.")])

# ================================================================ UNIDADE 2
opener("02","UNIDADE 2","Conectivos e tabelas-verdade",["Negação, conjunção e disjunção","Condicional e bicondicional","Montando tabelas-verdade"],"U2")

add(H(2,'Negação, conjunção e <span class="hl">disjunção</span>','Quando cada uma é verdadeira.', "A03") +
 '<div style="display:flex;gap:10pt">' +
 '<div style="flex:1">' + tv(["p","~p"],[["V","F"],["F","V"]],1,"Negação: inverte o valor.") + '</div>' +
 '<div style="flex:1.4">' + tv(["p","q","p ∧ q"],[[a,b,c] for (a,b),c in zip(B4,[VF(x) for x in col(lambda p,q: p and q)])],2,"Conjunção: V só se ambas forem V.") + '</div></div>' +
 '<div style="display:flex;gap:10pt">' +
 '<div style="flex:1">' + tv(["p","q","p ∨ q"],[[a,b,c] for (a,b),c in zip(B4,[VF(x) for x in col(lambda p,q: p or q)])],2,"Disjunção inclusiva: F só se ambas forem F.") + '</div>' +
 '<div style="flex:1">' + tv(["p","q","p ⊻ q"],[[a,b,c] for (a,b),c in zip(B4,[VF(x) for x in col(lambda p,q: p != q)])],2,"Disjunção exclusiva: V se os valores forem diferentes.") + '</div></div>' +
 traduz(p('Pense em promessas. “Vou estudar <strong>e</strong> treinar”: só cumpri se fiz as duas coisas. “Vou estudar <strong>ou</strong> treinar”: cumpri se fiz pelo menos uma. “<strong>Ou</strong> estudo <strong>ou</strong> treino”: cumpri se fiz exatamente uma.'),"profa"))

add(H(2,'Condicional e <span class="hl">bicondicional</span>','Os dois conectivos mais cobrados.', "A04") +
 '<div style="display:flex;gap:10pt">' +
 '<div style="flex:1">' + tv(["p","q","p → q"],[[a,b,c] for (a,b),c in zip(B4,[VF(x) for x in col(lambda p,q: (not p) or q)])],2,"Condicional: F só em V → F.") + '</div>' +
 '<div style="flex:1">' + tv(["p","q","p ↔ q"],[[a,b,c] for (a,b),c in zip(B4,[VF(x) for x in col(lambda p,q: p == q)])],2,"Bicondicional: V se os valores forem iguais.") + '</div></div>' +
 ex(p('Promessa: “<b>Se</b> você passar no concurso, <b>então</b> eu pago o jantar”. Quando a promessa foi quebrada? Só se você passou (p = V) e eu não paguei (q = F). Se você não passou, eu posso pagar ou não: a promessa não foi quebrada. Por isso a condicional é <b>falsa em um único caso</b>: V → F.'), "Entenda com uma promessa") +
 table(["Na condicional p → q","Nome","Dica"],[
  ["p","Antecedente (condição suficiente)","Se p acontece, q tem que acontecer"],
  ["q","Consequente (condição necessária)","Sem q, não há p"]],["24%","34%",None]) +
 memo('Condicional: só é falsa quando <strong>V → F</strong> (antecedente verdadeiro, consequente falso). Bicondicional: V quando os dois valores são <strong>iguais</strong>.'))

add(H(2,'Montando <span class="hl">tabelas-verdade</span>','Linhas, colunas e classificação.', "A05") +
 p('O número de linhas de uma tabela-verdade é <strong>2<sup>n</sup></strong>, em que n é o número de proposições simples diferentes: 2 proposições = 4 linhas; 3 = 8 linhas; 4 = 16 linhas.') +
 tv(["p","q","~p","~p ∨ q","p → q"],[[a,b,VF(not(a=="V")),VF((a!="V") or (b=="V")),VF((a!="V") or (b=="V"))] for a,b in B4],None,"Passo a passo: as colunas de ~p ∨ q e de p → q são idênticas. Logo, são equivalentes.") +
 table(["Classificação","Última coluna","Exemplo"],[
  ["Tautologia","Só V","p ∨ ~p (“chove ou não chove”)"],
  ["Contradição","Só F","p ∧ ~p (“chove e não chove”)"],
  ["Contingência","V e F misturados","p → q"]],["24%","24%",None]) +
 lembre(p('<strong>Desafio:</strong> quantas linhas tem a tabela de (p ∧ q) → (r ∨ s)? <br><strong>Resposta:</strong> há 4 proposições simples (p, q, r, s), então 2<sup>4</sup> = <strong>16 linhas</strong>.'), "Desafio"))

treino(2, [
 ("A conjunção p ∧ q é verdadeira apenas quando p e q são verdadeiras.","C","Uma F torna tudo F."),
 ("A disjunção inclusiva p ∨ q é falsa quando apenas uma das proposições é falsa.","E","Só é F quando ambas são F."),
 ("Se p é falsa e q é verdadeira, a condicional p → q é verdadeira.","C","Só é F em V → F."),
 ("A bicondicional p ↔ q é verdadeira quando p e q têm o mesmo valor lógico.","C","V ↔ V ou F ↔ F."),
 ("Uma tabela-verdade com três proposições simples tem 6 linhas.","E","2³ = 8 linhas."),
 ("A proposição p ∨ ~p é uma tautologia.","C","Sempre verdadeira.")])

# ================================================================ UNIDADE 3
opener("03","UNIDADE 3","Equivalências e negações",["Equivalências lógicas","Negação de compostas","Quantificadores"],"U3")

add(H(3,'Equivalências <span class="hl">lógicas</span>','Frases diferentes, mesmo valor em todos os casos.', "A06") +
 p('Duas proposições são <strong>equivalentes</strong> quando têm a <strong>mesma tabela-verdade</strong>. Na prova, isso aparece como “é equivalente a” ou “tem o mesmo sentido lógico que”.') +
 table(["Proposição","Equivalente","Exemplo"],[
  ["p → q","~q → ~p (contrapositiva)","Se está de plantão, está fardado ≡ Se não está fardado, não está de plantão."],
  ["p → q","~p ∨ q","Se está de plantão, está fardado ≡ Não está de plantão ou está fardado."],
  ["p ↔ q","(p → q) ∧ (q → p)","Abre se e somente se o crachá é aceito ≡ se é aceito, abre, e se abre, é aceito."],
  ["p ∧ q · p ∨ q","q ∧ p · q ∨ p","A ordem não importa no “e” e no “ou”."]],["18%","30%",None]) +
 pega('<ul><li>A <b>recíproca</b> (q → p) <b>não</b> é equivalente a p → q. “Se está de plantão, está fardado” não garante que “se está fardado, está de plantão”.</li><li>A <b>inversa</b> (~p → ~q) também <b>não</b> é equivalente.</li><li>Equivalente de verdade: <b>inverte e nega</b> os dois lados (contrapositiva).</li></ul>'))

add(H(3,'Negação de proposições <span class="hl">compostas</span>','Leis de De Morgan e a negação da condicional.', "A07") +
 table(["Proposição","Negação","Exemplo"],[
  ["p ∧ q","~p ∨ ~q","“Estuda e trabalha” → “Não estuda <b>ou</b> não trabalha.”"],
  ["p ∨ q","~p ∧ ~q","“Estuda ou trabalha” → “Não estuda <b>e</b> não trabalha.”"],
  ["p → q","p ∧ ~q","“Se chover, a ronda é suspensa” → “Chove <b>e</b> a ronda <b>não</b> é suspensa.”"],
  ["p ↔ q","p ⊻ q","“Abre se e somente se é aceito” → “Ou abre ou é aceito.”"]],["16%","18%",None]) +
 traduz(p('Para negar “e” e “ou” (De Morgan): <strong>negue cada parte e troque o conectivo</strong>. Para negar a condicional, lembre quando ela é falsa: <strong>antecedente acontece e consequente não</strong>. Por isso a negação de p → q é “<strong>mantém o primeiro E nega o segundo</strong>”. Nunca é outra condicional.')) +
 memo('~(p ∧ q) = ~p <strong>∨</strong> ~q · ~(p ∨ q) = ~p <strong>∧</strong> ~q · ~(p → q) = <strong>p ∧ ~q</strong> (“MA NE”: mantém e nega).'))

add(H(3,'<span class="hl">Quantificadores</span>','Todo, algum, nenhum.', "A08") +
 venn3() +
 table(["Proposição","Negação","Exemplo"],[
  ["Todo A é B","Algum A não é B","“Todos os candidatos passaram” → “Algum candidato não passou.”"],
  ["Algum A é B","Nenhum A é B","“Algum guarda faltou” → “Nenhum guarda faltou.”"],
  ["Nenhum A é B","Algum A é B","“Nenhum guarda faltou” → “Algum guarda faltou.”"],
  ["Algum A não é B","Todo A é B","“Algum candidato não passou” → “Todos os candidatos passaram.”"]],["22%","22%",None]) +
 pega('<ul><li>A negação de “Todos passaram” <b>não</b> é “Ninguém passou”: basta <b>um</b> que não tenha passado.</li><li>Em lógica, “algum” significa “pelo menos um” (podendo ser todos).</li></ul>'))

treino(3, [
 ("“Se está de plantão, então está fardado” equivale a “Se não está fardado, então não está de plantão”.","C","Contrapositiva."),
 ("“Se está de plantão, então está fardado” equivale a “Se está fardado, então está de plantão”.","E","Essa é a recíproca, que não é equivalente."),
 ("A negação de “Ana estuda e Bruno trabalha” é “Ana não estuda ou Bruno não trabalha”.","C","De Morgan."),
 ("A negação de “Se chover, a ronda é suspensa” é “Se não chover, a ronda não é suspensa”.","E","Negação: “Chove e a ronda não é suspensa”."),
 ("A negação de “Todos os guardas estão de folga” é “Nenhum guarda está de folga”.","E","É “Algum guarda não está de folga”."),
 ("A negação de “Nenhum candidato faltou” é “Algum candidato faltou”.","C","Basta um.")])

# ================================================================ UNIDADE 4
opener("04","UNIDADE 4","Argumentação",["Argumento válido","Diagramas e silogismos"],"U4")

add(H(4,'Argumento <span class="hl">válido</span>','Premissas, conclusão e as formas que não falham.', "A09") +
 p('<strong>Argumento</strong> é um conjunto de <strong>premissas</strong> que leva a uma <strong>conclusão</strong>. Ele é <strong>válido</strong> quando, sendo as premissas verdadeiras, a conclusão é <strong>obrigatoriamente</strong> verdadeira. Validade é questão de <strong>forma</strong>, não de conteúdo.') +
 table(["Forma","Estrutura","Exemplo","Válido?"],[
  ["Modus ponens","p → q; p; logo q","Se chove, a rua molha. Choveu. Logo, a rua molhou.","<b>Sim</b>"],
  ["Modus tollens","p → q; ~q; logo ~p","Se chove, a rua molha. A rua não molhou. Logo, não choveu.","<b>Sim</b>"],
  ["Silogismo hipotético","p → q; q → r; logo p → r","Se estudo, passo. Se passo, tomo posse. Logo, se estudo, tomo posse.","<b>Sim</b>"],
  ["Silogismo disjuntivo","p ∨ q; ~p; logo q","Ana está na praça ou na escola. Não está na praça. Logo, está na escola.","<b>Sim</b>"],
  ["Afirmar o consequente","p → q; q; logo p","Se chove, a rua molha. A rua molhou. Logo, choveu.",f'<b style="color:{C["red"]}">Não</b> (pode ter sido um caminhão-pipa)'],
  ["Negar o antecedente","p → q; ~p; logo ~q","Se chove, a rua molha. Não choveu. Logo, a rua não molhou.",f'<b style="color:{C["red"]}">Não</b>']],["20%","20%","38%",None]) +
 memo('Válidas: <strong>afirmar o antecedente</strong> (ponens) e <strong>negar o consequente</strong> (tollens). Falácias: <strong>afirmar o consequente</strong> e <strong>negar o antecedente</strong>.'))

add(H(4,'Diagramas e <span class="hl">silogismos</span>','Quando o argumento usa todo, algum e nenhum.', "A10") +
 venn3() +
 traduz(p('<strong>Passo 1:</strong> desenhe a premissa com “todo” ou “nenhum” primeiro (são as mais rígidas). <strong>Passo 2:</strong> encaixe a premissa com “algum”. <strong>Passo 3:</strong> a conclusão só é válida se aparecer em <strong>todos</strong> os desenhos possíveis.')) +
 ex(p('<b>Premissas:</b> Todos os guardas são servidores. Todos os servidores são concursados.<br><b>Desenho:</b> o círculo dos guardas fica dentro do dos servidores, que fica dentro do dos concursados.<br><b>Conclusão válida:</b> todos os guardas são concursados.<br><b>Conclusão inválida:</b> todos os concursados são guardas (o círculo maior não cabe no menor).'), "Resolvendo um silogismo") +
 lembre(p('<strong>Desafio:</strong> “Alguns atletas são guardas. Todos os guardas são servidores.” É obrigatório que algum atleta seja servidor? <br><strong>Resposta:</strong> sim. Os atletas que são guardas estão dentro do círculo dos guardas, que está dentro do dos servidores. Logo, <strong>algum atleta é servidor</strong>.'), "Desafio"))

treino(4, [
 ("Um argumento é válido quando a conclusão decorre obrigatoriamente das premissas.","C","Validade é forma."),
 ("“Se estudo, passo. Passei. Logo, estudei” é um argumento válido.","E","Falácia da afirmação do consequente."),
 ("“Se estudo, passo. Não passei. Logo, não estudei” é um argumento válido (modus tollens).","C","Nega o consequente."),
 ("“Se chove, a rua molha. Não choveu. Logo, a rua não molhou” é um argumento válido.","E","Falácia da negação do antecedente."),
 ("De “Todo A é B” e “Todo B é C” conclui-se validamente que “Todo A é C”.","C","Círculos encaixados."),
 ("De “Todo A é B” conclui-se validamente que “Todo B é A”.","E","B pode ser maior que A.")])

# ================================================================ UNIDADE 5
opener("05","UNIDADE 5","Sequências",["Sequências numéricas","Letras e figuras"],"U5")

add(H(5,'Sequências <span class="hl">numéricas</span>','Descubra a regra antes de calcular.', "A11") +
 seq_visual() +
 table(["Tipo","Regra","Fórmula do termo geral"],[
  ["Progressão aritmética (PA)","Soma-se sempre a mesma razão r","a<sub>n</sub> = a<sub>1</sub> + (n − 1) · r"],
  ["Progressão geométrica (PG)","Multiplica-se sempre pela mesma razão q","a<sub>n</sub> = a<sub>1</sub> · q<sup>n − 1</sup>"]],["30%","36%",None]) +
 traduz(p('Roteiro para qualquer sequência: <strong>1)</strong> calcule a diferença entre termos vizinhos; <strong>2)</strong> se não for constante, teste a divisão; <strong>3)</strong> se nada funcionar, procure quadrados (1, 4, 9, 16…), alternância de duas regras ou diferenças que crescem (1, 2, 4, 7, 11: as diferenças são 1, 2, 3, 4).')) +
 ex(p('<b>PA:</b> a<sub>1</sub> = 5 e r = 4. O 10º termo é a<sub>10</sub> = 5 + 9 · 4 = <b>41</b>.<br><b>PG:</b> a<sub>1</sub> = 3 e q = 2. O 5º termo é a<sub>5</sub> = 3 · 2<sup>4</sup> = 3 · 16 = <b>48</b>.'), "Calculando termos"))

add(H(5,'Sequências de letras e <span class="hl">figuras</span>','Posição no alfabeto e ciclos.', "A12") +
 p('Com letras, converta cada letra na sua <strong>posição no alfabeto</strong> (A = 1, B = 2, C = 3…, considerando as 26 letras, com K, W e Y) e procure a regra numérica. Confira no enunciado se a banca considera o alfabeto de 26 letras.') +
 table(["Sequência","Posições","Regra","Próximo"],[
  ["A, C, E, G, …","1, 3, 5, 7","+2","I (9)"],
  ["B, E, H, K, …","2, 5, 8, 11","+3","N (14)"],
  ["Z, X, V, T, …","26, 24, 22, 20","−2","R (18)"]],["28%","26%","16%",None]) +
 p('Com figuras ou dias que se repetem, o truque é o <strong>ciclo</strong>: descubra de quantos em quantos elementos o padrão se repete e use o <strong>resto da divisão</strong>.') +
 ex(p('Uma escala de plantão segue o ciclo <b>manhã, tarde, noite, folga</b> (4 posições). Qual é o turno do 30º dia, se o 1º dia é “manhã”? 30 ÷ 4 = 7, resto <b>2</b>. O resto 2 corresponde à 2ª posição do ciclo: <b>tarde</b>. (Resto 0 corresponderia à última posição, “folga”.)'), "Ciclos com resto da divisão") +
 lembre(p('<strong>Desafio:</strong> qual é o próximo termo de 1, 4, 9, 16, 25, …? <br><strong>Resposta:</strong> são os quadrados perfeitos (1², 2², 3², 4², 5²). O próximo é 6² = <strong>36</strong>.'), "Desafio"))

treino(5, [
 ("Na sequência 2, 5, 8, 11, …, o próximo termo é 14.","C","PA de razão 3."),
 ("Na sequência 3, 6, 12, 24, …, o próximo termo é 36.","E","PG de razão 2: o próximo é 48."),
 ("Em uma PA com a₁ = 5 e r = 4, o 10º termo é 41.","C","5 + 9 · 4 = 41."),
 ("Na sequência A, C, E, G, …, a próxima letra é H.","E","Salta uma letra: I."),
 ("Em um ciclo de 4 turnos começando em “manhã”, o 30º dia é “tarde”.","C","Resto 2."),
 ("A sequência 1, 4, 9, 16, … é formada por quadrados perfeitos.","C","1², 2², 3², 4².")])

# ================================================================ UNIDADE 6
opener("06","UNIDADE 6","Matemática básica e problemas",["Porcentagem","Razão, proporção e regra de três","Problemas de lógica"],"U6")

add(H(6,'<span class="hl">Porcentagem</span>','Porcentagem é uma fração de denominador 100.', "A13") +
 table(["Situação","Como calcular","Exemplo"],[
  ["x% de um valor","Multiplique por x/100","15% de 240 = 0,15 × 240 = 36"],
  ["Aumento de x%","Multiplique por (1 + x/100)","R$ 80 com aumento de 25% = 80 × 1,25 = R$ 100"],
  ["Desconto de x%","Multiplique por (1 − x/100)","R$ 80 com desconto de 25% = 80 × 0,75 = R$ 60"],
  ["Que percentual é?","Parte ÷ todo × 100","12 de 48 = 12 ÷ 48 = 0,25 = 25%"]],["24%","32%",None]) +
 fatores() +
 ex(p('Dois aumentos sucessivos de 10%: 1,10 × 1,10 = 1,21. O aumento total é de <b>21%</b>, e não de 20%.'), "Mais um exemplo"))

add(H(6,'Razão, proporção e <span class="hl">regra de três</span>','Comparar, igualar e prever.', "A14") +
 table(["Conceito","O que é","Exemplo"],[
  ["Razão","Comparação por divisão: a/b","12 homens e 18 mulheres: razão homens/mulheres = 12/18 = 2/3"],
  ["Proporção","Igualdade entre razões: a/b = c/d, em que a · d = b · c","2/3 = 8/12, pois 2 · 12 = 3 · 8"],
  ["Divisão proporcional","Repartir na razão dada","R$ 900 na razão 2:1 → 3 partes de R$ 300 → R$ 600 e R$ 300"]],["22%","36%",None]) +
 table(["Regra de três","Quando","Exemplo resolvido"],[
  ["Direta","Uma grandeza aumenta e a outra também","3 kg custam R$ 18. Quanto custam 7 kg? 3/7 = 18/x → x = 7 · 18 ÷ 3 = <b>R$ 42</b>"],
  ["Inversa","Uma grandeza aumenta e a outra diminui","6 guardas fazem a ronda em 8 h. Quanto tempo levam 12 guardas? O dobro de guardas leva a metade do tempo: 6 · 8 = 12 · x → x = <b>4 h</b>"]],["16%","30%",None]) +
 traduz(p('Antes de montar a conta, pergunte: “se eu <strong>dobrar</strong> uma grandeza, a outra dobra ou cai pela metade?” Se dobra, é <strong>direta</strong> (multiplica em cruz). Se cai pela metade, é <strong>inversa</strong> (multiplica em linha).')))

add(H(6,'Problemas de <span class="hl">lógica</span>','Tabelas de associação e verdades e mentiras.', "A15") +
 p('<strong>Associação.</strong> Três guardas (Ana, Bruno e Carla) ficam em três postos (praça, escola e mercado), um em cada. Pistas: (1) Ana não fica na escola nem no mercado. (2) Bruno não fica na escola.') +
 grade_logica() +
 p('<strong>Resolução:</strong> pela pista 1, sobra a <b>praça</b> para Ana. Pela pista 2, Bruno não está na escola; como a praça já é de Ana, Bruno fica no <b>mercado</b>. Sobra a <b>escola</b> para Carla.') +
 p('<strong>Verdades e mentiras.</strong> Três suspeitos; só um é culpado e só um fala a verdade. A diz: “B é culpado”. B diz: “Eu não sou culpado”. C diz: “Eu não sou culpado”.') +
 table(["Hipótese","A (“B é culpado”)","B (“não sou”)","C (“não sou”)","Verdades"],[
  ["A culpado","F","V","V","2 ✗"],["B culpado","V","F","V","2 ✗"],["C culpado","F","V","F",f'<b style="color:{C["green"]}">1 ✔</b>']],["20%","22%","18%","18%",None]) +
 memo('Em problemas de verdade e mentira, <strong>teste cada hipótese</strong> e conte as verdades. Só fica a hipótese que respeita a condição do enunciado: aqui, <strong>C é culpado e B fala a verdade</strong>.'))

treino(6, [
 ("15% de 240 é igual a 36.","C","0,15 × 240 = 36."),
 ("Um aumento de 20% seguido de um desconto de 20% faz o preço voltar ao valor inicial.","E","1,2 × 0,8 = 0,96: cai 4%."),
 ("Dois aumentos sucessivos de 10% equivalem a um aumento de 21%.","C","1,1 × 1,1 = 1,21."),
 ("Se 6 guardas fazem uma tarefa em 8 h, 12 guardas, no mesmo ritmo, fazem em 16 h.","E","Grandezas inversas: 4 h."),
 ("Se 3 kg custam R$ 18, 7 kg custam R$ 42.","C","Regra de três direta."),
 ("A razão entre 12 e 18 é igual a 2/3.","C","12/18 simplificado.")])

# ================================================================ REVISÃO
mapa(("RACIOCÍNIO","LÓGICO",""), [
  ("PROPOSIÇÕES",["declarativa, V ou F","pergunta e ordem: não","sentença aberta: não"],C['navy'],NV),
  ("CONECTIVOS",["e: V só se V e V","ou: F só se F e F","se…então: F só V → F"],C['blue'],C['sky']),
  ("EQUIVALÊNCIA E NEGAÇÃO",["p → q ≡ ~q → ~p","~(p ∧ q) = ~p ∨ ~q","~(p → q) = p ∧ ~q"],C['green'],C['greensoft']),
  ("ARGUMENTOS",["ponens e tollens: válidos","afirmar consequente: não","Venn para todo/algum"],C['golddeep'],C['goldsoft']),
  ("SEQUÊNCIAS",["PA: soma · PG: multiplica","ciclos: resto da divisão","letras: posição"],C['red'],C['redsoft']),
  ("MATEMÁTICA",["percentuais: multiplique","+20% −20% = −4%","direta x inversa"],C['navy'],NV)], "Mapa conceitual do Caderno 18.", "O raciocínio lógico em seis blocos. Explique cada caixa em voz alta.", center_color="#ff9f43")

erros([
  ["“Frase falsa não é proposição.”","É proposição: pode ser julgada (como F)."],
  ["“x + 3 = 7 é proposição.”","É sentença aberta: depende de x."],
  ["“p ∨ q é falsa se uma for falsa.”","Só é falsa se ambas forem falsas."],
  ["“Condicional com antecedente falso é falsa.”","F → qualquer coisa é V; só V → F é F."],
  ["“3 proposições = 6 linhas.”","2³ = 8 linhas."],
  ["“p → q equivale a q → p.”","Equivale a ~q → ~p (contrapositiva) e a ~p ∨ q."],
  ["“Negação de p → q é ~p → ~q.”","É p ∧ ~q."]],
 [["“Negação de p ∧ q é ~p ∧ ~q.”","É ~p ∨ ~q (troca o conectivo)."],
  ["“Negação de ‘todos passaram’ é ‘ninguém passou’.”","É “algum não passou”."],
  ["“Se chove, molha; molhou; logo choveu: válido.”","Falácia: afirmação do consequente."],
  ["“Todo A é B, logo todo B é A.”","Não decorre: B pode ser maior."],
  ["“+20% e −20% se anulam.”","1,2 × 0,8 = 0,96 (−4%)."],
  ["“Dois aumentos de 10% = 20%.”","1,1 × 1,1 = 1,21 (21%)."],
  ["“Mais guardas, mais tempo: regra direta.”","Mais trabalhadores, menos tempo: inversa."]])

flashcards([("PROPOSIÇÃO","O que é proposição?","Oração declarativa que pode ser julgada V ou F."),
 ("PROPOSIÇÃO","Pergunta, ordem e exclamação são proposições?","Não."),
 ("PROPOSIÇÃO","Sentença aberta (x + 1 = 3)?","Não é proposição."),
 ("CONECTIVOS","Quando p ∧ q é V?","Só quando p e q são V."),
 ("CONECTIVOS","Quando p ∨ q é F?","Só quando p e q são F."),
 ("CONECTIVOS","Quando p ⊻ q é V?","Quando têm valores diferentes."),
 ("CONECTIVOS","Quando p → q é F?","Só quando p é V e q é F."),
 ("CONECTIVOS","Quando p ↔ q é V?","Quando têm valores iguais."),
 ("TABELA","Número de linhas?","2ⁿ (n = proposições simples)."),
 ("TABELA","Tautologia?","Última coluna só com V."),
 ("EQUIVALÊNCIA","Equivalentes de p → q?","~q → ~p e ~p ∨ q."),
 ("NEGAÇÃO","~(p ∧ q)?","~p ∨ ~q."),
 ("NEGAÇÃO","~(p ∨ q)?","~p ∧ ~q."),
 ("NEGAÇÃO","~(p → q)?","p ∧ ~q."),
 ("NEGAÇÃO","~(p ↔ q)?","p ⊻ q."),
 ("QUANTIFICADOR","Negação de “todo A é B”?","Algum A não é B."),
 ("QUANTIFICADOR","Negação de “nenhum A é B”?","Algum A é B."),
 ("ARGUMENTO","Modus tollens?","p → q; ~q; logo ~p (válido)."),
 ("ARGUMENTO","Afirmação do consequente?","p → q; q; logo p (inválido)."),
 ("SEQUÊNCIA","Termo geral da PA?","aₙ = a₁ + (n − 1) · r."),
 ("SEQUÊNCIA","Termo geral da PG?","aₙ = a₁ · qⁿ⁻¹."),
 ("PORCENTAGEM","+20% seguido de −20%?","× 0,96: queda de 4%."),
 ("PROPORÇÃO","Propriedade fundamental?","a/b = c/d ⇒ a · d = b · c."),
 ("REGRA DE TRÊS","Mais guardas, menos horas?","Inversa.")])

Q = [
 ("Proposições","Assinale a alternativa que contém uma proposição:",
  ["Que horas começa o plantão?","Feche o portão.","Brasília é a capital do Brasil.","x + 3 = 7","Que noite tranquila!"],"C",
  "Só a frase declarativa que pode ser julgada V ou F é proposição. Pergunta, ordem, sentença aberta e exclamação não são.","Proposição = declarativa com valor."),
 ("Conectivos","Sabendo que p é verdadeira e q é falsa, é verdadeira a proposição:",
  ["p ∧ q","p → q","q → p","p ↔ q","~p"],"C",
  "q → p é F → V, que é verdadeira. p ∧ q = F; p → q = V → F = F; p ↔ q = F (valores diferentes); ~p = F.","Condicional só é F em V → F."),
 ("Tabela-verdade","O número de linhas da tabela-verdade da proposição (p ∧ q) → (r ∨ s) é:",
  ["4","8","12","16","32"],"D",
  "Há 4 proposições simples: 2⁴ = 16 linhas.","2ⁿ."),
 ("Condicional","A proposição “Se o guarda está de plantão, então ele está fardado” é falsa quando o guarda:",
  ["não está de plantão e está fardado.","não está de plantão e não está fardado.","está de plantão e está fardado.","está de plantão e não está fardado.","está fardado, em qualquer caso."],"D",
  "A condicional só é falsa quando o antecedente é V (está de plantão) e o consequente é F (não está fardado).","V → F = F."),
 ("Disjunção exclusiva","A proposição “Ou Ana está na praça ou Ana está na escola” é verdadeira quando:",
  ["Ana está nos dois lugares.","Ana não está em nenhum dos dois.","Ana está em exatamente um dos dois lugares.","Ana está na praça, obrigatoriamente.","sempre, independentemente da localização."],"C",
  "A disjunção exclusiva é V quando as proposições têm valores diferentes, isto é, exatamente uma é verdadeira.","Ou…ou = exatamente um."),
 ("Classificação","É uma tautologia:",
  ["p ∧ ~p","p ∨ ~p","p → q","p ∧ q","p ↔ q"],"B",
  "p ∨ ~p é sempre verdadeira. p ∧ ~p é contradição; as demais são contingências.","Tautologia = sempre V."),
 ("Equivalência","Uma proposição logicamente equivalente a “Se o agente está de plantão, então está fardado” é:",
  ["Se o agente está fardado, então está de plantão.","Se o agente não está de plantão, então não está fardado.","Se o agente não está fardado, então não está de plantão.","O agente está de plantão e não está fardado.","O agente está de plantão e está fardado."],"C",
  "A contrapositiva ~q → ~p é equivalente. A recíproca (q → p) e a inversa (~p → ~q) não são; “está de plantão e não está fardado” é a negação.","Inverte e nega."),
 ("Negação","A negação de “João estuda e trabalha” é:",
  ["João não estuda e não trabalha.","João não estuda ou não trabalha.","João estuda ou trabalha.","Se João estuda, então não trabalha.","João não estuda nem trabalha."],"B",
  "Lei de De Morgan: ~(p ∧ q) = ~p ∨ ~q.","Nega as partes e troca e por ou."),
 ("Negação","A negação de “Se chover, então a ronda será suspensa” é:",
  ["Se não chover, a ronda não será suspensa.","Chove e a ronda não é suspensa.","Não chove e a ronda é suspensa.","Se a ronda não for suspensa, não choverá.","Não chove ou a ronda é suspensa."],"B",
  "~(p → q) = p ∧ ~q: mantém o antecedente e nega o consequente.","Mantém e nega."),
 ("Quantificadores","A negação de “Todos os candidatos foram aprovados” é:",
  ["Nenhum candidato foi aprovado.","Algum candidato não foi aprovado.","Todos os candidatos foram reprovados.","Algum candidato foi aprovado.","Somente um candidato foi aprovado."],"B",
  "Para negar “todos”, basta um caso contrário: algum candidato não foi aprovado.","Negação de todo: algum… não."),
 ("Quantificadores","A negação de “Nenhum guarda faltou ao plantão” é:",
  ["Todos os guardas faltaram ao plantão.","Algum guarda faltou ao plantão.","Nenhum guarda compareceu ao plantão.","Algum guarda não faltou ao plantão.","Todos os guardas compareceram."],"B",
  "Negação de “nenhum A é B” é “algum A é B”.","Nenhum ↔ algum."),
 ("Argumentação","Considere as premissas: “Se Ana passou, ela comemorou” e “Ana não comemorou”. Conclui-se corretamente que:",
  ["Ana passou.","Ana não passou.","Ana comemorou.","Ana passou e não comemorou.","nada se pode concluir."],"B",
  "Modus tollens: p → q; ~q; logo ~p.","Nega o consequente, nega o antecedente."),
 ("Argumentação","O argumento “Se chove, a rua fica molhada. A rua está molhada. Logo, choveu” é:",
  ["válido, por modus ponens.","válido, por modus tollens.","inválido, pois afirma o consequente.","válido, pois as premissas são verdadeiras.","inválido, pois nega o antecedente."],"C",
  "Afirmar o consequente é falácia: a rua pode estar molhada por outro motivo.","Afirmar o consequente: inválido."),
 ("Silogismo","Se “Todos os guardas são servidores” e “Todos os servidores são concursados”, então, necessariamente:",
  ["Todos os concursados são guardas.","Todos os guardas são concursados.","Algum concursado não é servidor.","Nenhum guarda é concursado.","Todos os servidores são guardas."],"B",
  "Círculos encaixados: guardas dentro de servidores, servidores dentro de concursados.","Todo A é B, todo B é C ⇒ todo A é C."),
 ("Lógica","Três suspeitos; só um é culpado e só um diz a verdade. A: “B é culpado”. B: “Eu não sou culpado”. C: “Eu não sou culpado”. O culpado é:",
  ["A.","B.","C.","A ou B.","impossível determinar."],"C",
  "Testando: A culpado gera 2 verdades (B e C); B culpado gera 2 (A e C); C culpado gera 1 (só B). Logo, C é culpado.","Teste as hipóteses."),
 ("Sequências","O próximo termo da sequência 2, 5, 8, 11, … é:",
  ["12","13","14","15","16"],"C",
  "PA de razão 3: 11 + 3 = 14.","Diferença constante = PA."),
 ("Sequências","O próximo termo da sequência 3, 6, 12, 24, … é:",
  ["30","36","42","48","54"],"D",
  "PG de razão 2: 24 × 2 = 48.","Quociente constante = PG."),
 ("PA","Em uma progressão aritmética com primeiro termo 5 e razão 4, o 10º termo é:",
  ["36","41","45","40","49"],"B",
  "a₁₀ = 5 + (10 − 1) · 4 = 5 + 36 = 41.","aₙ = a₁ + (n − 1) · r."),
 ("Sequências","O próximo termo da sequência 1, 4, 9, 16, 25, … é:",
  ["30","34","36","49","32"],"C",
  "Quadrados perfeitos: 6² = 36.","Procure quadrados."),
 ("Porcentagem","15% de 240 correspondem a:",
  ["24","30","36","40","48"],"C",
  "0,15 × 240 = 36.","x% = x/100."),
 ("Porcentagem","Um produto de R$ 200,00 sofre aumento de 10% e, em seguida, desconto de 10%. O preço final é:",
  ["R$ 200,00","R$ 198,00","R$ 202,00","R$ 180,00","R$ 220,00"],"B",
  "200 × 1,10 × 0,90 = 200 × 0,99 = 198.","Multiplique os fatores."),
 ("Razão","Em uma turma com 12 homens e 18 mulheres, a razão entre o número de homens e o de mulheres é:",
  ["3/2","2/3","1/2","3/5","2/5"],"B",
  "12/18 = 2/3 (dividindo por 6). Atenção à ordem: homens sobre mulheres.","Razão = a/b, na ordem pedida."),
 ("Regra de três","Seis guardas fazem a ronda de um bairro em 8 horas. Mantido o ritmo, doze guardas farão a mesma ronda em:",
  ["16 horas.","12 horas.","6 horas.","4 horas.","2 horas."],"D",
  "Grandezas inversamente proporcionais: 6 · 8 = 12 · x → x = 4.","Mais gente, menos tempo: inversa."),
 ("Regra de três","Se 3 kg de um produto custam R$ 18,00, então 7 kg custam:",
  ["R$ 36,00","R$ 40,00","R$ 42,00","R$ 45,00","R$ 49,00"],"C",
  "Direta: 3/7 = 18/x → x = 42. (Ou: 1 kg = R$ 6; 7 kg = R$ 42.)","Mais quilos, mais reais: direta.")]

def verificar():
    """Confere os cálculos usados nas questões e treinos."""
    assert 2**4 == 16 and 2**3 == 8
    assert abs(0.15*240-36) < 1e-9 and abs(200*1.1*0.9-198) < 1e-9 and abs(1.2*0.8-0.96) < 1e-9 and abs(1.1*1.1-1.21) < 1e-9
    assert 5+9*4 == 41 and 3*2**4 == 48 and 6*8/12 == 4 and 7*18/3 == 42 and 30 % 4 == 2
    from fractions import Fraction; assert Fraction(12,18) == Fraction(2,3)
    imp = lambda p,q: (not p) or q
    # contrapositiva e ~p ∨ q equivalentes a p → q; negações
    for p in (True,False):
        for q in (True,False):
            assert imp(p,q) == imp(not q, not p) == ((not p) or q)
            assert (not (p and q)) == ((not p) or (not q)) and (not (p or q)) == ((not p) and (not q))
            assert (not imp(p,q)) == (p and not q) and (not (p == q)) == (p != q)
    # problema de verdades e mentiras
    sol = []
    for c in "ABC":
        ditos = [c=="B", c!="B", c!="C"]
        if sum(ditos) == 1: sol.append(c)
    assert sol == ["C"]
    print("verificação matemática: ok")
verificar()

questoes(Q, "BACDEBCAEDBCADEBACDEBCEA")
respostas_treinos()

referencias('''<h3>Base do conteúdo</h3><ul>
<li>Fundamentos de lógica proposicional (proposições, conectivos, tabelas-verdade, equivalências e negações), lógica de argumentação e quantificadores, na forma usual em provas de concursos.</li>
<li>Matemática básica: progressões, porcentagem, razão, proporção e regra de três.</li></ul>
<h3>Textos, exemplos e questões</h3><ul><li>Todos os exemplos, desafios e questões foram criados para este caderno. Os cálculos e tabelas-verdade foram conferidos por rotina automática durante a produção.</li></ul>''',
 'Raciocínio lógico não depende de legislação. <strong>Limitações:</strong> as bancas usam símbolos e nomenclaturas um pouco diferentes (por exemplo, ¬ ou ~ para negação, “disjunção exclusiva” ou “ou exclusivo”) e algumas consideram o alfabeto com ou sem K, W e Y em sequências de letras: leia o enunciado com atenção. Confira o edital do seu concurso.', DATA)
encerramento("18", "Raciocínio Lógico", 'Sugestão de continuação: <strong>Caderno 19 · Legislação das Guardas Municipais</strong>.')
gravar(HERE, "Mapa da Aprovação — Caderno 18 — Raciocínio Lógico", Q)
