"""Gera miolo.html do Caderno 14: Direitos Humanos — Conceitos, Tratados e Direitos Fundamentais. Uso: python3 gerar.py
Textos conferidos em fontes oficiais em 26/11/2026: CF/88 (Planalto), Decretos nº 591, 592 e 678/1992 (Planalto),
Lei nº 13.060/2014 e Decreto nº 12.341/2024 (Planalto) e DUDH (reprodução do UNICEF Brasil)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit
from kit import *

DATA = "26 de novembro de 2026"
kit.U = {1:("UNIDADE 1","Conceito e fundamentos"),2:("UNIDADE 2","Características"),3:("UNIDADE 3","História e dimensões"),4:("UNIDADE 4","DUDH e tratados"),5:("UNIDADE 5","Espécies de direitos"),6:("UNIDADE 6","Segurança pública")}
def cf(x): return f"{x} · Constituição Federal"

# ================================================================ APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">O que são os direitos humanos, de onde vieram, onde estão escritos e o que significam no trabalho de quem atua na segurança pública.</p>
<p>Este é o <strong>Caderno 14 da coleção</strong>, dedicado aos <strong>Direitos Humanos</strong>. A disciplina aparece em praticamente todos os editais de <strong>Guarda Municipal</strong> e das <strong>polícias</strong>, porque o agente de segurança é, ao mesmo tempo, <strong>protetor</strong> desses direitos e alguém que pode <strong>violá-los</strong> se agir fora dos limites.</p>
<p>O caderno combina três tipos de conteúdo: <strong>teoria</strong> (conceito, características e dimensões, em grande parte construções doutrinárias), <strong>normas</strong> (Constituição, Declaração Universal e tratados ratificados pelo Brasil) e <strong>atuação prática</strong> (direitos do preso, uso da força e instrumentos de menor potencial ofensivo).</p>
{table(["Recurso","Onde está"],[["Infográfico: direitos humanos x direitos fundamentais","Unidade 1"],["Características (universalidade, indivisibilidade, interdependência e outras)","Unidade 2"],["Linha do tempo e infográfico das dimensões","Unidade 3"],["DUDH, Pactos de 1966 e Pacto de São José","Unidade 4"],["Quadro das espécies de direitos","Unidade 5"],["Direitos do preso, uso da força e situações práticas","Unidade 6"],["Mapa conceitual, erros mais comuns e 24 questões autorais","Revisão e prática"]],["58%",None])}
{lembre(p(f'Constituição, Decretos nº 591, 592 e 678/1992 (Pactos de 1966 e Pacto de São José), Lei nº 13.060/2014 e Decreto nº 12.341/2024 conferidos no portal do Planalto, e Declaração Universal conferida na reprodução do UNICEF Brasil, em <strong>{DATA}</strong>.'), "Fontes e atualização")}''', first=True)

toc_page([("u","UNIDADE 1 · CONCEITO E FUNDAMENTOS","U1"),("","1. Conceito de direitos humanos","A01"),("","2. Fundamentos","A02"),("","3. Dignidade da pessoa humana","A03"),
 ("u","UNIDADE 2 · CARACTERÍSTICAS","U2"),("","4. Universalidade, indivisibilidade e interdependência","A04"),("","5. Outras características","A05"),
 ("u","UNIDADE 3 · EVOLUÇÃO HISTÓRICA E DIMENSÕES","U3"),("","6. Linha do tempo","A06"),("","7. Dimensões (gerações) de direitos","A07"),
 ("u","UNIDADE 4 · DECLARAÇÃO UNIVERSAL E TRATADOS","U4"),("","8. Declaração Universal dos Direitos Humanos","A08"),("","9. Sistemas de proteção e principais tratados","A09"),("","10. Tratados de direitos humanos na Constituição","A10"),
 ("u","UNIDADE 5 · ESPÉCIES DE DIREITOS","U5"),("","11. Direitos civis e políticos","A11"),("","12. Direitos sociais, econômicos e culturais","A12"),
 ("u","UNIDADE 6 · DIREITOS HUMANOS E SEGURANÇA PÚBLICA","U6"),("","13. Direitos da pessoa presa","A13"),("","14. Uso da força e instrumentos de menor potencial ofensivo","A14"),("","15. Tortura, abuso e algemas","A15"),("","16. Atuação na prática","A16"),
 ("u","REVISÃO E PRÁTICA","RV"),("","Mapa conceitual · Erros mais comuns","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),("","Gabarito, respostas dos treinos e referências","R4")])

# ================================================================ UNIDADE 1
opener("01","UNIDADE 1","Conceito e fundamentos",["Conceito de direitos humanos","Fundamentos","Dignidade da pessoa humana"],"U1")

def dh_df():
    N,G,O=C['navy'],C['blue'],C['golddeep']
    s = f'<figure><svg viewBox="0 0 640 200" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    s += f'<rect x="10" y="20" width="300" height="150" rx="16" fill="{C["sky"]}" stroke="{G}" stroke-width="2.5"/><text x="160" y="50" text-anchor="middle" font-size="15" font-weight="900" fill="{G}">DIREITOS HUMANOS</text>'
    s += f'<text x="160" y="80" text-anchor="middle" font-size="11" fill="{C["ink"]}">previstos em normas</text><text x="160" y="96" text-anchor="middle" font-size="11" font-weight="900" fill="{C["ink"]}">INTERNACIONAIS</text><text x="160" y="124" text-anchor="middle" font-size="10.5" fill="{C["muted"]}">DUDH, Pactos de 1966,</text><text x="160" y="140" text-anchor="middle" font-size="10.5" fill="{C["muted"]}">Pacto de São José</text>'
    s += f'<rect x="330" y="20" width="300" height="150" rx="16" fill="{C["goldsoft"]}" stroke="{O}" stroke-width="2.5"/><text x="480" y="50" text-anchor="middle" font-size="15" font-weight="900" fill="{O}">DIREITOS FUNDAMENTAIS</text>'
    s += f'<text x="480" y="80" text-anchor="middle" font-size="11" fill="{C["ink"]}">positivados na</text><text x="480" y="96" text-anchor="middle" font-size="11" font-weight="900" fill="{C["ink"]}">CONSTITUIÇÃO de um Estado</text><text x="480" y="124" text-anchor="middle" font-size="10.5" fill="{C["muted"]}">no Brasil: Título II da CF/88</text><text x="480" y="140" text-anchor="middle" font-size="10.5" fill="{C["muted"]}">(arts. 5º a 17)</text>'
    s += f'<text x="320" y="192" text-anchor="middle" font-size="10.5" font-weight="800" fill="{N}">Mesma essência (a dignidade humana); a diferença está no PLANO em que são reconhecidos.</text>'
    return s + '</svg><figcaption>Direitos humanos x direitos fundamentais (distinção doutrinária).</figcaption></figure>'

add(H(1,'Conceito de <span class="hl">direitos humanos</span>','Direitos que toda pessoa tem por ser pessoa.', "A01") +
 oque(p('<strong>Direitos humanos</strong> são o conjunto de direitos considerados <strong>essenciais</strong> para que toda pessoa possa viver com <strong>dignidade</strong>, reconhecidos a todos os seres humanos, <strong>sem distinção</strong> de nacionalidade, cor, sexo, religião, opinião ou qualquer outra condição.')) +
 dh_df() +
 traduz(p('Direitos humanos não são “direitos de bandido”, como às vezes se diz: são direitos de <strong>todas as pessoas</strong>, inclusive da vítima, do cidadão comum e do próprio agente de segurança. O guarda municipal tem direito à vida, à integridade física, a condições dignas de trabalho e a um processo justo, assim como qualquer outra pessoa.')) +
 memo('Direitos humanos = plano <strong>internacional</strong>. Direitos fundamentais = plano <strong>constitucional</strong> (no Brasil, arts. 5º a 17). Ambos têm como base a <strong>dignidade</strong>.'))

add(H(1,'<span class="hl">Fundamentos</span>','Por que os direitos humanos existem e obrigam.', "A02") +
 table(["Corrente","Ideia central"],[
  ["Jusnaturalista","Os direitos humanos decorrem da própria natureza humana e existem antes de qualquer lei; o Estado apenas os reconhece"],
  ["Positivista","Os direitos humanos valem porque estão previstos em normas jurídicas (Constituição, tratados)"],
  ["Histórica (ou realista)","Os direitos são conquistas construídas ao longo da história, fruto de lutas sociais; por isso são históricos e se ampliam"],
  ["Moral / dignidade","O fundamento último é a <b>dignidade da pessoa humana</b>, valor que a Constituição coloca entre os fundamentos da República"]],["26%",None]) +
 lei(cf("Art. 1º, III, e art. 4º, II"),'<p>Art. 1º A República Federativa do Brasil [...] tem como fundamentos: [...] III - a dignidade da pessoa humana; [...]<br>Art. 4º A República Federativa do Brasil rege-se nas suas relações internacionais pelos seguintes princípios: [...] II - prevalência dos direitos humanos;</p>') +
 memo('Dignidade da pessoa humana = <strong>fundamento</strong> da República (art. 1º, III). Prevalência dos direitos humanos = <strong>princípio</strong> das relações internacionais (art. 4º, II).'))

add(H(1,'Dignidade da <span class="hl">pessoa humana</span>','O valor-fonte de todos os direitos.', "A03") +
 traduz(p('A ideia mais conhecida, inspirada no filósofo <strong>Immanuel Kant</strong>, é que a pessoa deve ser tratada sempre como um <strong>fim em si mesma</strong>, e nunca apenas como um <strong>meio</strong> para os objetivos de outros. As coisas têm <strong>preço</strong>; as pessoas têm <strong>dignidade</strong>. Por isso a dignidade não depende de mérito, comportamento ou condição: até quem cometeu um crime grave conserva sua dignidade.'),"profa") +
 cards([("heart","Valor intrínseco","Toda pessoa tem dignidade pelo simples fato de ser humana.",C['blue']),("shield","Limite ao Estado","Proíbe tortura, tratamento degradante e penas cruéis.",C['navy']),("people","Igual para todos","Não há pessoas com mais ou menos dignidade.",C['golddeep']),("home2","Mínimo existencial","Exige condições materiais mínimas: saúde, educação, moradia.",C['green'])],4))
atencao(ex(p('Durante uma abordagem, um suspeito já imobilizado e algemado é exibido a curiosos e fotografado de forma humilhante. Mesmo que ele tenha cometido o crime, essa exposição <b>viola a dignidade</b> e pode configurar abuso de autoridade (Lei nº 13.869/2019, art. 13). A dignidade é o limite que separa a força legítima do abuso.')) +
 memo('Dignidade: a pessoa é <strong>fim</strong>, nunca mero <strong>meio</strong>. Ninguém perde a dignidade, nem quem comete crimes.') +
 pega('<ul><li>A dignidade não é um direito que se “ganha” por bom comportamento: é <b>inerente</b> a toda pessoa.</li><li>Dignidade da pessoa humana é <b>fundamento</b> da República (art. 1º, III), e não objetivo nem princípio das relações internacionais.</li></ul>'),
 ["dignidade","fim em si mesma","mínimo existencial","art. 1º, III"], "A dignidade na prática")

treino(1, [
 ("Direitos humanos são direitos reconhecidos a todas as pessoas, sem distinção de qualquer natureza.","C","Conceito básico."),
 ("Segundo a doutrina, direitos fundamentais são os direitos humanos positivados na Constituição de um Estado.","C","Distinção pelo plano de reconhecimento."),
 ("A dignidade da pessoa humana é princípio das relações internacionais previsto no art. 4º da Constituição.","E","É fundamento da República (art. 1º, III); a prevalência dos direitos humanos é que é princípio do art. 4º."),
 ("Para a corrente jusnaturalista, os direitos humanos decorrem da natureza humana e existem antes da lei.","C","Fundamento jusnaturalista."),
 ("Quem comete um crime grave perde sua dignidade.","E","A dignidade é inerente a toda pessoa."),
 ("A prevalência dos direitos humanos é princípio que rege o Brasil nas relações internacionais.","C","CF, art. 4º, II.")])

# ================================================================ UNIDADE 2
opener("02","UNIDADE 2","Características",["Universalidade, indivisibilidade e interdependência","Outras características"],"U2")

add(H(2,'Universalidade, indivisibilidade e <span class="hl">interdependência</span>','As três características mais cobradas.', "A04") +
 lembre(p('A <strong>Declaração e Programa de Ação de Viena</strong> (Conferência Mundial sobre Direitos Humanos, <strong>1993</strong>) afirmou que todos os direitos humanos são <strong>universais, indivisíveis, interdependentes e inter-relacionados</strong>, e que a comunidade internacional deve tratá-los de forma global, justa e equitativa, com a mesma ênfase.'), "Conferência de Viena (1993)") +
 table(["Característica","Significado","Exemplo"],[
  ["<b>Universalidade</b>","Os direitos humanos pertencem a <b>todas as pessoas</b>, em qualquer lugar, independentemente de nacionalidade, cultura ou condição","Um estrangeiro em situação irregular continua tendo direito à vida e a não ser torturado"],
  ["<b>Indivisibilidade</b>","Os direitos formam um <b>conjunto único</b>: não se pode escolher garantir só alguns (civis, por exemplo) e deixar outros (sociais) de lado","Não basta garantir a liberdade de expressão se a pessoa não tem acesso à educação"],
  ["<b>Interdependência</b> (inter-relação)","Os direitos <b>dependem uns dos outros</b>: a realização de um contribui para a de outro, e a violação de um afeta os demais","O direito à saúde depende do direito à moradia e ao saneamento; o direito ao voto depende da educação e da informação"]],["20%",None,"36%"]) +
 memo('<strong>Universal</strong> = para todos. <strong>Indivisível</strong> = um só bloco, sem hierarquia. <strong>Interdependente</strong> = um depende do outro. Fonte de referência: <strong>Viena, 1993</strong>.'))

add(H(2,'Outras <span class="hl">características</span>','A lista completa que aparece nas provas.', "A05") +
 table(["Característica","Significado"],[
  ["Historicidade","São fruto da história e se ampliam ao longo do tempo (por isso falamos em dimensões)"],
  ["Inerência","Pertencem à pessoa pelo simples fato de ser humana"],
  ["Inalienabilidade","Não podem ser vendidos, cedidos ou transferidos"],
  ["Irrenunciabilidade","A pessoa não pode abrir mão deles (pode deixar de exercê-los em certo momento, mas não renunciar ao direito)"],
  ["Imprescritibilidade","Não se perdem pela falta de uso ao longo do tempo"],
  ["Inviolabilidade","Não podem ser desrespeitados por leis ou atos de autoridade"],
  ["Relatividade (limitabilidade)","Não são absolutos: podem ser limitados quando entram em conflito com outros direitos, por ponderação (exceção discutida: a proibição da tortura)"],
  ["Vedação ao retrocesso","Os direitos já conquistados não podem ser simplesmente suprimidos"],
  ["Complementaridade","Devem ser interpretados em conjunto, e não isoladamente"],
  ["Efetividade","O Poder Público deve atuar para garantir que os direitos se realizem na prática"]],["28%",None]) +
 ex(p('A liberdade de reunião (CF, art. 5º, XVI) é um direito humano, mas <b>não é absoluta</b>: a reunião deve ser pacífica, sem armas, e não pode frustrar outra reunião já convocada para o mesmo local. Já a proibição de tortura é tratada pela doutrina como um dos raros direitos que não admitem exceção em nenhuma circunstância.')) +
 memo('Para lembrar sem decorar a lista: os direitos humanos são <strong>históricos</strong>, <strong>não se vendem</strong> (inalienáveis), <strong>não se renunciam</strong> (irrenunciáveis), <strong>não prescrevem</strong> (imprescritíveis) e são, em regra, <strong>relativos</strong>.'))

treino(2, [
 ("Segundo a Declaração de Viena de 1993, os direitos humanos são universais, indivisíveis, interdependentes e inter-relacionados.","C","Conferência Mundial de Viena."),
 ("A indivisibilidade permite ao Estado escolher garantir apenas os direitos civis, deixando os sociais para depois.","E","Os direitos formam um conjunto único."),
 ("A universalidade significa que os direitos humanos pertencem a todas as pessoas, independentemente de nacionalidade.","C","Característica da universalidade."),
 ("Os direitos humanos são, em regra, absolutos e não admitem limitação.","E","São, em regra, relativos (limitáveis)."),
 ("A imprescritibilidade indica que os direitos humanos não se perdem pelo decurso do tempo.","C","Não prescrevem."),
 ("A historicidade explica por que os direitos humanos se ampliaram ao longo do tempo.","C","Fruto de conquistas históricas.")])

# ================================================================ UNIDADE 3
opener("03","UNIDADE 3","Evolução histórica e dimensões",["Linha do tempo","Dimensões (gerações) de direitos"],"U3")

def timeline():
    ev=[("1215","Magna Carta","limites ao rei"),("1689","Bill of Rights","Inglaterra"),("1776","Declaração de","Independência (EUA)"),("1789","Declaração dos Direitos","do Homem e do Cidadão"),("1917/1919","Constituições do","México e de Weimar"),("1945","Carta da ONU","criação da ONU"),("1948","DUDH","Declaração Universal"),("1966","Pactos","PIDCP e PIDESC"),("1969","Pacto de","São José"),("1988","Constituição","Cidadã (Brasil)")]
    s = f'<figure><svg viewBox="0 0 640 250" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    s += f'<line x1="20" y1="125" x2="620" y2="125" stroke="{C["navy"]}" stroke-width="4"/>'
    for k,(y,a,b) in enumerate(ev):
        x=36+k*63; up = k%2==0
        col = C['gold'] if y in ("1948","1988") else C['blue']
        s += f'<circle cx="{x}" cy="125" r="9" fill="{col}" stroke="{C["navy"]}" stroke-width="2"/>'
        yy = 60 if up else 150
        s += f'<line x1="{x}" y1="{116 if up else 134}" x2="{x}" y2="{yy+ (40 if up else 0)}" stroke="#9db0c8" stroke-width="1.5"/>'
        s += f'<text x="{x}" y="{yy+12}" text-anchor="middle" font-size="11" font-weight="900" fill="{C["navy"]}">{y}</text><text x="{x}" y="{yy+26}" text-anchor="middle" font-size="8.4" font-weight="700" fill="{C["ink"]}">{a}</text><text x="{x}" y="{yy+38}" text-anchor="middle" font-size="8" fill="{C["muted"]}">{b}</text>'
    return s + '</svg><figcaption>Marcos históricos dos direitos humanos (em amarelo, os mais cobrados: DUDH e CF/88).</figcaption></figure>'

add(H(3,'Linha do <span class="hl">tempo</span>','Os marcos da construção dos direitos humanos.', "A06") +
 timeline() +
 table(["Marco","Por que importa"],[
  ["Revoluções liberais (EUA, 1776; França, 1789)","Afirmação dos direitos de <b>liberdade</b> contra o poder absoluto do Estado"],
  ["Constituições do México (1917) e de Weimar (1919)","Primeiras a prever <b>direitos sociais</b> (trabalho, educação, previdência)"],
  ["Segunda Guerra Mundial e criação da ONU (1945)","As atrocidades da guerra levaram à <b>internacionalização</b> dos direitos humanos"],
  ["Declaração Universal (1948)","Primeiro documento a proclamar, em escala mundial, um catálogo de direitos para todas as pessoas"],
  ["Constituição de 1988","Marco da redemocratização brasileira, com amplo rol de direitos fundamentais"]],["38%",None]) +
 memo('<strong>1945</strong>: ONU. <strong>1948</strong>: DUDH. <strong>1966</strong>: os dois Pactos. <strong>1969</strong>: Pacto de São José. <strong>1988</strong>: Constituição Cidadã.'))

def dimensoes():
    it=[("1ª","LIBERDADE","civis e políticos","Estado se abstém","vida, liberdade, voto",C['blue'],C['sky']),
        ("2ª","IGUALDADE","sociais, econômicos e culturais","Estado presta","saúde, educação, trabalho",C['golddeep'],C['goldsoft']),
        ("3ª","FRATERNIDADE","difusos e coletivos","toda a humanidade","paz, meio ambiente",C['green'],C['greensoft'])]
    s = f'<figure><svg viewBox="0 0 640 220" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    for k,(n,t,a,b,c,fg,bg) in enumerate(it):
        x=8+k*212
        s += f'<rect x="{x}" y="8" width="200" height="190" rx="16" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x+100}" y="52" text-anchor="middle" font-size="36" font-weight="900" fill="{fg}">{n}</text><text x="{x+100}" y="82" text-anchor="middle" font-size="15" font-weight="900" fill="{fg}">{t}</text>'
        s += f'<text x="{x+100}" y="110" text-anchor="middle" font-size="11" font-weight="800" fill="{C["ink"]}">{a}</text><text x="{x+100}" y="134" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">{b}</text><text x="{x+100}" y="162" text-anchor="middle" font-size="10.5" fill="{C["muted"]}">ex.: {c}</text>'
    s += f'<text x="320" y="214" text-anchor="middle" font-size="10.5" font-weight="800" fill="{C["navy"]}">Lema da Revolução Francesa: liberdade, igualdade, fraternidade (Karel Vasak, 1979).</text>'
    return s + '</svg><figcaption>As três primeiras dimensões de direitos.</figcaption></figure>'

add(H(3,'Dimensões (<span class="hl">gerações</span>) de direitos','Como os direitos foram se somando.', "A07") +
 dimensoes() +
 table(["Dimensão","Conteúdo","Observação"],[
  ["4ª (doutrina)","Para Paulo Bonavides: democracia, informação e pluralismo. Para Norberto Bobbio: direitos ligados à biotecnologia e à manipulação genética","Classificação sem consenso"],
  ["5ª (doutrina)","Para Paulo Bonavides: o direito à paz","Para outros autores, a paz está na 3ª dimensão"]],["18%",None,"26%"]) +
 traduz(p('Hoje a doutrina prefere a palavra <strong>dimensões</strong> em vez de <strong>gerações</strong>, porque “geração” sugere que uma substitui a outra. Na verdade, os direitos se <strong>somam</strong>: os de liberdade continuam existindo ao lado dos sociais e dos difusos. Isso combina com a <strong>indivisibilidade</strong> e a <strong>interdependência</strong>.')) +
 memo('1ª = <strong>liberdade</strong> (o Estado <strong>não</strong> interfere). 2ª = <strong>igualdade</strong> (o Estado <strong>presta</strong>). 3ª = <strong>fraternidade</strong> (direitos de <strong>todos</strong>). Dimensões se <strong>somam</strong>.'))

treino(3, [
 ("As Constituições do México (1917) e de Weimar (1919) são marcos dos direitos sociais.","C","Primeiras a prever direitos sociais."),
 ("A Declaração Universal dos Direitos Humanos foi adotada em 1966.","E","Em 10 de dezembro de 1948; em 1966 vieram os Pactos."),
 ("Os direitos de primeira dimensão exigem, em regra, uma abstenção do Estado.","C","Direitos de liberdade."),
 ("O direito ao meio ambiente equilibrado é classicamente apontado como direito de segunda dimensão.","E","É de terceira dimensão (difusos)."),
 ("A doutrina prefere o termo dimensões porque os direitos se somam, em vez de se substituírem.","C","Crítica ao termo gerações."),
 ("Os direitos sociais, econômicos e culturais são associados à ideia de igualdade.","C","Segunda dimensão.")])

# ================================================================ UNIDADE 4
opener("04","UNIDADE 4","Declaração Universal e tratados",["Declaração Universal dos Direitos Humanos","Sistemas de proteção e tratados","Tratados na Constituição"],"U4")

add(H(4,'Declaração Universal dos <span class="hl">Direitos Humanos</span>','10 de dezembro de 1948.', "A08") +
 lei("Preâmbulo e art. 1º · Declaração Universal dos Direitos Humanos",'<p>Adotada e proclamada pela Assembleia Geral das Nações Unidas (resolução 217 A III) em 10 de dezembro de 1948.<br>Artigo 1: Todos os seres humanos nascem livres e iguais em dignidade e direitos. [...]</p>') +
 table(["Ponto","Informação"],[
  ["Quem adotou","Assembleia Geral da ONU, pela <b>Resolução 217 A (III)</b>"],
  ["Data","<b>10 de dezembro de 1948</b> (hoje, Dia Internacional dos Direitos Humanos)"],
  ["Tamanho","Preâmbulo e <b>30 artigos</b>"],
  ["Natureza jurídica","É uma <b>resolução</b>, e não um tratado: formalmente, não foi assinada e ratificada pelos Estados. A doutrina considera que muitos de seus dispositivos valem como <b>costume internacional</b> e princípios gerais"],
  ["Conteúdo","Reúne direitos civis e políticos (arts. 3º a 21) e direitos econômicos, sociais e culturais (arts. 22 a 27), afirmando a indivisibilidade"]],["24%",None]) +
 table(["Artigo","Conteúdo (em síntese)"],[
  ["3","Direito à vida, à liberdade e à segurança pessoal"],["5","Ninguém será submetido à tortura, nem a tratamento ou castigo cruel, desumano ou degradante"],
  ["9","Ninguém será arbitrariamente preso, detido ou exilado"],["11.1","Presunção de inocência até prova de culpa, em julgamento público com garantias de defesa"],
  ["19","Liberdade de opinião e de expressão"],["21","Participação no governo, acesso ao serviço público e eleições periódicas"],
  ["23","Direito ao trabalho e a remuneração justa"],["25 e 26","Padrão de vida adequado (alimentação, moradia, saúde) e direito à educação"]],["14%",None]))

add(H(4,'Sistemas de proteção e <span class="hl">principais tratados</span>','Global (ONU) e regional (OEA).', "A09") +
 table(["","SISTEMA GLOBAL (ONU)","SISTEMA INTERAMERICANO (OEA)"],[
  ["Documentos principais","DUDH (1948); Pacto Internacional sobre Direitos Civis e Políticos (PIDCP) e Pacto Internacional sobre Direitos Econômicos, Sociais e Culturais (PIDESC), ambos de 1966","Convenção Americana sobre Direitos Humanos (<b>Pacto de São José da Costa Rica</b>), de 22 de novembro de 1969"],
  ["No Brasil","PIDCP promulgado pelo Decreto nº 592/1992; PIDESC pelo Decreto nº 591/1992","Promulgado pelo Decreto nº 678/1992"],
  ["Órgãos","Conselho de Direitos Humanos, comitês dos tratados","Comissão Interamericana e Corte Interamericana de Direitos Humanos"]],["20%",None,None]) +
 lembre(p('A <strong>Carta Internacional dos Direitos Humanos</strong> (“International Bill of Rights”) é o nome dado ao conjunto formado pela <strong>DUDH</strong> e pelos <strong>dois Pactos de 1966</strong>. Ao contrário da Declaração, os Pactos são <strong>tratados</strong>: obrigam juridicamente os Estados que os ratificam.'), "Carta Internacional dos Direitos Humanos") +
 table(["Pacto de São José (Decreto nº 678/1992)","Conteúdo (em síntese)"],[
  ["Art. 4.1","Direito à vida, protegido pela lei e, em geral, desde o momento da concepção"],
  ["Art. 5.2","Ninguém deve ser submetido a torturas nem a penas ou tratos cruéis, desumanos ou degradantes"],
  ["Art. 7.5","A pessoa detida deve ser conduzida, sem demora, à presença de um juiz (base da audiência de custódia)"],
  ["Art. 7.7","Ninguém deve ser detido por dívida, salvo por inadimplemento de obrigação alimentar"],
  ["Art. 8.2, g","Direito de não ser obrigado a depor contra si mesmo nem a declarar-se culpado"]],["30%",None]))

add(H(4,'Tratados de direitos humanos na <span class="hl">Constituição</span>','Hierarquia e mecanismos especiais.', "A10") +
 lei(cf("Art. 5º, §§ 1º a 4º"),'<p>§ 1º As normas definidoras dos direitos e garantias fundamentais têm aplicação imediata.<br>§ 2º Os direitos e garantias expressos nesta Constituição não excluem outros decorrentes do regime e dos princípios por ela adotados, ou dos tratados internacionais em que a República Federativa do Brasil seja parte.<br>§ 3º Os tratados e convenções internacionais sobre direitos humanos que forem aprovados, em cada Casa do Congresso Nacional, em dois turnos, por três quintos dos votos dos respectivos membros, serão equivalentes às emendas constitucionais. (EC nº 45/2004)<br>§ 4º O Brasil se submete à jurisdição de Tribunal Penal Internacional a cuja criação tenha manifestado adesão. (EC nº 45/2004)</p>') +
 table(["Tratado de direitos humanos","Hierarquia no Brasil"],[
  ["Aprovado pelo rito do § 3º (2 turnos, 3/5, nas duas Casas)","<b>Equivalente a emenda constitucional</b> (ex.: Convenção sobre os Direitos das Pessoas com Deficiência)"],
  ["Aprovado pelo rito comum (antes ou depois da EC nº 45/2004)","<b>Supralegal</b>: abaixo da Constituição, acima das leis (entendimento do STF, RE 466.343, 2008)"],
  ["Tratado que não é de direitos humanos","Equivalente a <b>lei ordinária</b>"]],["46%",None]) +
 lembre(p('Por causa do status supralegal do Pacto de São José (art. 7.7), o STF entendeu que não cabe mais a prisão civil do depositário infiel (<strong>Súmula Vinculante 25</strong>). Também por força da EC nº 45/2004, nas hipóteses de grave violação de direitos humanos, o <strong>Procurador-Geral da República</strong> pode pedir ao <strong>STJ</strong> o <strong>incidente de deslocamento de competência</strong> para a Justiça Federal (CF, art. 109, V-A e § 5º).'), "Consequências práticas"))

treino(4, [
 ("A Declaração Universal dos Direitos Humanos foi adotada pela Assembleia Geral da ONU em 10 de dezembro de 1948.","C","Resolução 217 A (III)."),
 ("A DUDH é um tratado internacional ratificado pelos Estados.","E","É uma resolução da Assembleia Geral."),
 ("O Pacto de São José da Costa Rica foi promulgado no Brasil pelo Decreto nº 678/1992.","C","Convenção Americana sobre Direitos Humanos."),
 ("Tratados de direitos humanos aprovados em cada Casa, em dois turnos, por três quintos dos votos, equivalem a emendas constitucionais.","C","CF, art. 5º, § 3º."),
 ("Segundo o STF, tratados de direitos humanos aprovados pelo rito comum têm status de lei ordinária.","E","Têm status supralegal."),
 ("O incidente de deslocamento de competência é suscitado pelo Procurador-Geral da República perante o STJ.","C","CF, art. 109, § 5º.")])

# ================================================================ UNIDADE 5
opener("05","UNIDADE 5","Espécies de direitos",["Direitos civis e políticos","Direitos sociais, econômicos e culturais"],"U5")

add(H(5,'Direitos civis e <span class="hl">políticos</span>','Liberdade e participação.', "A11") +
 table(["","DIREITOS CIVIS","DIREITOS POLÍTICOS"],[
  ["Protegem","A pessoa contra abusos do Estado e de terceiros: vida, liberdade, igualdade, intimidade, propriedade","A participação da pessoa na vida política e nas decisões do Estado"],
  ["Exemplos na CF","Art. 5º: vida, igualdade, liberdade de expressão, de crença, de locomoção, inviolabilidade do domicílio, devido processo legal","Art. 14: sufrágio universal, voto direto e secreto, com valor igual para todos; plebiscito, referendo e iniciativa popular"],
  ["Tratado de referência","PIDCP (Decreto nº 592/1992) e Pacto de São José","PIDCP e Pacto de São José"]],["18%",None,None]) +
 ex(p('Quando um guarda municipal respeita o direito de um grupo se reunir pacificamente numa praça, protege um <b>direito civil</b> (liberdade de reunião). Quando a Guarda apoia a segurança de um local de votação, colabora com o exercício de um <b>direito político</b> (o voto).')) +
 memo('Civis = proteção da <strong>pessoa</strong> (vida, liberdade). Políticos = <strong>participação</strong> (votar, ser votado, plebiscito, referendo, iniciativa popular).'))

add(H(5,'Direitos sociais, <span class="hl">econômicos e culturais</span>','Igualdade material.', "A12") +
 lei(cf("Art. 6º (redação da EC nº 90/2015)"),'<p>Art. 6º São direitos sociais a educação, a saúde, a alimentação, o trabalho, a moradia, o transporte, o lazer, a segurança, a previdência social, a proteção à maternidade e à infância, a assistência aos desamparados, na forma desta Constituição.</p>') +
 table(["Espécie","O que protege","Exemplos"],[
  ["Sociais","Condições de vida digna, por meio de prestações do Estado","Saúde, educação, moradia, alimentação, transporte, assistência"],
  ["Econômicos","Relações de trabalho e meios de subsistência","Trabalho, salário justo, sindicalização, greve, previdência"],
  ["Culturais","Participação na vida cultural e acesso aos bens culturais","Acesso à cultura, proteção do patrimônio cultural, educação"]],["18%",None,"36%"]) +
 lembre(p('O PIDESC (Decreto nº 591/1992) prevê que cada Estado deve adotar medidas, “até o máximo de seus recursos disponíveis”, para alcançar <strong>progressivamente</strong> a plena realização desses direitos (art. 2.1). Daí vêm as ideias de <strong>realização progressiva</strong>, de <strong>mínimo existencial</strong> e de <strong>vedação ao retrocesso</strong>.'), "Realização progressiva") +
 memo('Art. 6º, em blocos: <strong>educação e saúde</strong> · <strong>alimentação, trabalho e moradia</strong> · <strong>transporte e lazer</strong> · <strong>segurança e previdência</strong> · <strong>maternidade e infância</strong> · <strong>desamparados</strong>. Atenção: <strong>segurança</strong> e <strong>transporte</strong> também são direitos sociais.'))

treino(5, [
 ("São direitos sociais previstos no art. 6º da Constituição a alimentação, o transporte e a segurança.","C","Art. 6º, com a EC nº 90/2015."),
 ("O direito de votar e ser votado é exemplo de direito civil, e não político.","E","É direito político."),
 ("O PIDESC prevê a realização progressiva dos direitos econômicos, sociais e culturais.","C","Art. 2.1."),
 ("A segurança é direito social expressamente previsto no art. 6º da Constituição.","C","Art. 6º."),
 ("O plebiscito, o referendo e a iniciativa popular são formas de exercício da soberania popular previstas no art. 14 da Constituição.","C","Direitos políticos."),
 ("O direito ao trabalho é exemplo de direito de primeira dimensão.","E","É direito social/econômico, de segunda dimensão.")])

# ================================================================ UNIDADE 6
opener("06","UNIDADE 6","Direitos humanos e segurança pública",["Direitos da pessoa presa","Uso da força","Tortura, abuso e algemas","Atuação na prática"],"U6")

add(H(6,'Direitos da <span class="hl">pessoa presa</span>','O que a Constituição e os tratados garantem.', "A13") +
 table(["Direito","Base"],[
  ["Ninguém será submetido a tortura nem a tratamento desumano ou degradante","CF, art. 5º, III; DUDH, art. 5º; Pacto de São José, art. 5.2"],
  ["Respeito à integridade física e moral do preso","CF, art. 5º, XLIX"],
  ["Comunicação imediata da prisão e do local ao juiz e à família ou pessoa indicada","CF, art. 5º, LXII"],
  ["Ser informado de seus direitos, entre os quais o de permanecer calado, com assistência da família e de advogado","CF, art. 5º, LXIII"],
  ["Identificação dos responsáveis pela prisão ou pelo interrogatório","CF, art. 5º, LXIV"],
  ["Presunção de inocência até o trânsito em julgado","CF, art. 5º, LVII; DUDH, art. 11.1"],
  ["Ser levado sem demora à presença de um juiz (audiência de custódia)","Pacto de São José, art. 7.5; CPP, art. 310 (até 24 horas)"]],["58%",None]) +
 memo('Preso: <strong>integridade</strong> preservada, prisão <strong>comunicada</strong>, direito ao <strong>silêncio</strong>, direito de saber <strong>quem o prendeu</strong> e de ver um <strong>juiz sem demora</strong>.'))

add(H(6,'Uso da força e instrumentos de <span class="hl">menor potencial ofensivo</span>','Lei nº 13.060/2014 e Decreto nº 12.341/2024.', "A14") +
 lei("Art. 2º · Lei nº 13.060/2014 (em síntese)",'<p>Os órgãos de segurança pública deverão priorizar a utilização dos instrumentos de menor potencial ofensivo, desde que o seu uso não coloque em risco a integridade física ou psíquica dos policiais, e deverão obedecer aos princípios da legalidade, da necessidade e da razoabilidade e proporcionalidade.<br>Parágrafo único. Não é legítimo o uso de arma de fogo: I - contra pessoa em fuga que esteja desarmada ou que não represente risco imediato de morte ou de lesão aos agentes de segurança pública ou a terceiros; e II - contra veículo que desrespeite bloqueio policial em via pública, exceto quando o ato represente risco de morte ou lesão aos agentes de segurança pública ou a terceiros.</p>') +
 table(["Ponto","Regra"],[
  ["Instrumentos de menor potencial ofensivo (art. 4º)","Os projetados para conter, debilitar ou incapacitar temporariamente pessoas, com baixa probabilidade de causar morte ou lesões permanentes (ex.: espargidor de pimenta, arma de incapacitação neuromuscular, munição de impacto controlado)"],
  ["Socorro (art. 6º)","Quem for ferido em razão do uso da força deve receber atendimento médico imediato, e a família deve ser comunicada"],
  ["Formação (art. 3º)","Os cursos de formação e capacitação devem incluir conteúdo sobre o uso desses instrumentos"],
  ["Regulamento","Decreto nº 12.341/2024"]],["30%",None]) +
 lembre(p('O <strong>Decreto nº 12.341/2024</strong> regulamenta a Lei nº 13.060/2014 e fixa como princípios do uso da força: <strong>legalidade, precaução, necessidade, proporcionalidade, razoabilidade, responsabilização e não discriminação</strong> (art. 2º). Os profissionais devem <strong>priorizar a comunicação, a negociação</strong> e técnicas que impeçam a escalada da violência, e o emprego de arma de fogo é <strong>medida de último recurso</strong> (art. 3º, §§ 1º e 2º). Quando o uso da força resultar em ferimento ou morte, deve ser feito <strong>relatório circunstanciado</strong> (art. 3º, § 5º). Os repasses do Fundo Nacional de Segurança Pública para ações de uso da força de Estados, DF e Municípios ficam condicionados ao cumprimento dessas regras (art. 9º).'), "Decreto nº 12.341/2024"))

add(H(6,'Tortura, abuso e <span class="hl">algemas</span>','Quando a força vira crime.', "A15") +
 table(["Tema","Regra"],[
  ["Tortura (Lei nº 9.455/1997)","Crime comum, com pena aumentada se praticado por agente público; quem se omite tendo o dever de evitar responde com detenção de 1 a 4 anos; a condenação gera perda do cargo (ver Caderno 08)"],
  ["Abuso de autoridade (Lei nº 13.869/2019)","Exemplos: constranger o preso a exibir-se à curiosidade pública ou a situação vexatória (art. 13); deixar de se identificar ao preso (art. 16); exige finalidade específica de prejudicar, beneficiar ou mero capricho (ver Caderno 08)"],
  ["Uso de algemas (Súmula Vinculante 11)","Só é lícito em caso de resistência, fundado receio de fuga ou de perigo à integridade física própria ou alheia, por parte do preso ou de terceiros, justificada a excepcionalidade por escrito, sob pena de responsabilidade e de nulidade"],
  ["Documentos da ONU","Código de Conduta para os Funcionários Responsáveis pela Aplicação da Lei (1979) e Princípios Básicos sobre o Uso da Força e de Armas de Fogo (1990): uso da força só quando estritamente necessário e na medida exigida"]],["26%",None]) +
 scene3([("LEGÍTIMO",C['green'],C['greensoft'],"prof",["Suspeito armado","avança: uso","proporcional da força."],"necessário e proporcional"),
  ("EXCESSIVO",C['golddeep'],C['goldsoft'],"profa",["Suspeito já","rendido continua","sendo agredido."],"desproporcional"),
  ("CRIME",C['red'],C['redsoft'],"prof",["Agressões para","obter confissão","do detido."],"tortura (Lei 9.455)")], "Situação ilustrada: a fronteira entre a força legítima e o crime."))

atencao(
 table(["Situação","Conduta conforme os direitos humanos"],[
  ["Suspeito desarmado foge a pé","<b>Não</b> atirar: o uso de arma de fogo contra pessoa em fuga desarmada, sem risco imediato, não é legítimo (Lei nº 13.060/2014)"],
  ["Motorista fura bloqueio sem colocar ninguém em risco","<b>Não</b> atirar no veículo; comunicar e acompanhar"],
  ["Pessoa ferida na ocorrência","Prestar ou acionar socorro imediato e comunicar a família"],
  ["Preso algemado sem resistência","Algema só com justificativa escrita (SV 11); não expor o preso à curiosidade pública"],
  ["Testemunhar colega agredindo detido","Intervir e comunicar: a omissão de quem tinha o dever de evitar a tortura é crime"]],["36%",None]) +
 pega('<ul><li>Priorizar instrumentos de menor potencial ofensivo não significa proibir a arma de fogo: ela continua legítima diante de <b>risco imediato de morte ou lesão</b>.</li><li>Algema não é regra: exige <b>resistência, risco de fuga ou perigo</b>, com justificativa por escrito.</li><li>Direitos humanos protegem também os <b>agentes de segurança</b>: a lei condiciona o uso dos instrumentos à preservação da integridade física e psíquica dos policiais.</li></ul>'),
 ["legalidade","necessidade","proporcionalidade","menor potencial ofensivo","Súmula Vinculante 11","socorro imediato"], "Atuação na prática")

treino(6, [
 ("A Constituição assegura aos presos o respeito à integridade física e moral.","C","CF, art. 5º, XLIX."),
 ("Segundo a Lei nº 13.060/2014, é legítimo o uso de arma de fogo contra pessoa em fuga que esteja desarmada e não represente risco imediato.","E","Não é legítimo (art. 2º, parágrafo único, I)."),
 ("Os princípios da legalidade, da necessidade e da razoabilidade e proporcionalidade orientam o uso de instrumentos de menor potencial ofensivo.","C","Lei nº 13.060/2014, art. 2º."),
 ("O uso de algemas é a regra em qualquer prisão, dispensando justificativa.","E","SV 11: só em caso de resistência, fuga ou perigo, com justificativa escrita."),
 ("O Pacto de São José prevê que a pessoa detida deve ser conduzida, sem demora, à presença de um juiz.","C","Art. 7.5."),
 ("Quem é ferido em razão do uso da força deve receber atendimento médico imediato.","C","Lei nº 13.060/2014, art. 6º.")])

# ================================================================ REVISÃO
mapa(("DIREITOS","HUMA-","NOS"), [
  ("CONCEITO",["direitos de toda pessoa","humanos: internacional","fundamentais: Constituição"],C['navy'],NV),
  ("CARACTERÍSTICAS",["universais · indivisíveis","interdependentes (Viena)","históricos, relativos"],C['golddeep'],C['goldsoft']),
  ("DIMENSÕES",["1ª liberdade · 2ª igualdade","3ª fraternidade","se somam"],C['blue'],C['sky']),
  ("DUDH E TRATADOS",["DUDH 1948: resolução","Pactos 1966 · São José 1969","§ 3º: emenda; outros: supralegal"],C['green'],C['greensoft']),
  ("ESPÉCIES",["civis e políticos","sociais, econômicos,","culturais (art. 6º)"],C['golddeep'],C['goldsoft']),
  ("SEGURANÇA PÚBLICA",["preso: integridade, silêncio","força: necessária, proporcional","algema: SV 11"],C['red'],C['redsoft'])], "Mapa conceitual do Caderno 14.", "O caderno em seis blocos. Explique cada caixa em voz alta.", center_color=C['gold'])

erros([
  ["“Direitos humanos são direitos de quem comete crimes.”","São direitos de todas as pessoas, inclusive vítimas e agentes de segurança."],
  ["“Direitos humanos e fundamentais são exatamente a mesma coisa.”","Humanos: plano internacional; fundamentais: positivados na Constituição."],
  ["“A dignidade é princípio das relações internacionais.”","É fundamento da República (art. 1º, III)."],
  ["“Os direitos humanos são absolutos.”","Em regra, são relativos (limitáveis)."],
  ["“Indivisibilidade permite priorizar só alguns direitos.”","Os direitos formam um conjunto único."],
  ["“A DUDH é de 1966.”","É de 10/12/1948; os Pactos é que são de 1966."],
  ["“Meio ambiente é direito de 2ª dimensão.”","É de 3ª dimensão (difusos)."]],
 [["“A DUDH é um tratado.”","É uma resolução da Assembleia Geral da ONU."],
  ["“Todo tratado de direitos humanos tem força de emenda.”","Só os aprovados pelo rito do art. 5º, § 3º; os demais são supralegais."],
  ["“Segurança não é direito social.”","É, expressamente (CF, art. 6º)."],
  ["“Pode atirar em quem foge desarmado.”","Não é legítimo, sem risco imediato (Lei nº 13.060/2014)."],
  ["“Algemar é sempre permitido.”","Só com resistência, risco de fuga ou perigo, justificado por escrito (SV 11)."],
  ["“Direitos humanos não protegem o policial.”","Protegem todas as pessoas, inclusive o agente."],
  ["“O IDC é pedido pelo Ministro da Justiça ao STF.”","É pedido pelo Procurador-Geral da República ao STJ (CF, art. 109, § 5º)."]])

flashcards([("CONCEITO","Direitos humanos x fundamentais?","Humanos: plano internacional. Fundamentais: positivados na Constituição."),
 ("CONCEITO","Onde está a dignidade da pessoa humana na CF?","Art. 1º, III: fundamento da República."),
 ("CONCEITO","Prevalência dos direitos humanos?","Princípio das relações internacionais (CF, art. 4º, II)."),
 ("CARACTERÍSTICAS","Quais as características afirmadas em Viena (1993)?","Universais, indivisíveis, interdependentes e inter-relacionados."),
 ("CARACTERÍSTICAS","Os direitos humanos são absolutos?","Em regra, não: são relativos e podem ser ponderados."),
 ("CARACTERÍSTICAS","Imprescritibilidade?","Não se perdem com o tempo."),
 ("HISTÓRIA","Primeiras constituições com direitos sociais?","México (1917) e Weimar (1919)."),
 ("HISTÓRIA","Quando a ONU foi criada?","1945."),
 ("DIMENSÕES","1ª dimensão?","Liberdade: direitos civis e políticos; abstenção do Estado."),
 ("DIMENSÕES","2ª dimensão?","Igualdade: direitos sociais, econômicos e culturais; prestações."),
 ("DIMENSÕES","3ª dimensão?","Fraternidade: direitos difusos e coletivos (paz, meio ambiente)."),
 ("DIMENSÕES","Por que dimensões e não gerações?","Porque os direitos se somam, não se substituem."),
 ("DUDH","Data e documento de adoção da DUDH?","10/12/1948, Resolução 217 A (III) da Assembleia Geral da ONU."),
 ("DUDH","Quantos artigos tem a DUDH?","30."),
 ("DUDH","Natureza jurídica da DUDH?","Resolução (não tratado); muitos dispositivos valem como costume."),
 ("TRATADOS","O que forma a Carta Internacional dos Direitos Humanos?","DUDH + PIDCP + PIDESC."),
 ("TRATADOS","Decreto do Pacto de São José?","Decreto nº 678/1992."),
 ("TRATADOS","Hierarquia de tratado de DH aprovado pelo rito comum?","Supralegal (STF)."),
 ("TRATADOS","Hierarquia de tratado de DH pelo rito do § 3º?","Equivalente a emenda constitucional."),
 ("ESPÉCIES","Direitos sociais do art. 6º?","Educação, saúde, alimentação, trabalho, moradia, transporte, lazer, segurança, previdência, maternidade e infância, desamparados."),
 ("PRESO","Direito do preso de ver um juiz sem demora?","Pacto de São José, art. 7.5 (audiência de custódia)."),
 ("FORÇA","Princípios da Lei 13.060/2014?","Legalidade, necessidade, razoabilidade e proporcionalidade."),
 ("FORÇA","Quando não é legítimo usar arma de fogo (Lei 13.060)?","Contra pessoa em fuga desarmada sem risco imediato; contra veículo que fura bloqueio sem risco."),
 ("ALGEMAS","Quando o uso de algemas é lícito (SV 11)?","Resistência, receio de fuga ou perigo à integridade, justificado por escrito.")])

Q = [
 ("Conceito","Sobre a distinção doutrinária entre direitos humanos e direitos fundamentais, é correto afirmar:",
  ["não há nenhuma relação entre eles.","direitos humanos são reconhecidos no plano internacional, e direitos fundamentais são os positivados na Constituição de um Estado.","direitos fundamentais valem apenas para estrangeiros.","direitos humanos dependem de lei ordinária para existir.","direitos fundamentais são sempre absolutos."],"B",
  "A diferença está no plano de reconhecimento; a essência comum é a dignidade da pessoa humana.","Humanos: internacional; fundamentais: Constituição."),
 ("Fundamentos","A dignidade da pessoa humana, na Constituição de 1988, é:",
  ["princípio das relações internacionais (art. 4º).","fundamento da República Federativa do Brasil (art. 1º, III).","objetivo fundamental (art. 3º).","direito social (art. 6º).","norma sem aplicação prática."],"B",
  "Art. 1º, III. A prevalência dos direitos humanos é princípio das relações internacionais (art. 4º, II).","Dignidade = fundamento (art. 1º)."),
 ("Dignidade","Segundo a ideia inspirada em Kant, a dignidade da pessoa humana significa que:",
  ["a pessoa pode ser usada como meio, se houver interesse público.","a pessoa deve ser tratada como fim em si mesma, nunca apenas como meio.","só tem dignidade quem cumpre a lei.","a dignidade pode ser comprada.","a dignidade depende da nacionalidade."],"B",
  "As coisas têm preço; as pessoas têm dignidade.","Pessoa = fim, não meio."),
 ("Características","A característica segundo a qual os direitos humanos formam um conjunto único, sem que se possa garantir apenas parte deles, é a:",
  ["imprescritibilidade.","indivisibilidade.","historicidade.","relatividade.","inalienabilidade."],"B",
  "Indivisibilidade: direitos civis, políticos, sociais, econômicos e culturais formam um bloco único (Viena, 1993).","Um só bloco = indivisível."),
 ("Características","A característica que indica que os direitos humanos pertencem a todas as pessoas, independentemente de nacionalidade, é a:",
  ["universalidade.","complementaridade.","efetividade.","relatividade.","historicidade."],"A",
  "Universalidade: todos, em todo lugar.","Para todos = universal."),
 ("Características","Sobre as características dos direitos humanos, é INCORRETO afirmar:",
  ["são históricos.","são inalienáveis.","são imprescritíveis.","são, em regra, absolutos e ilimitáveis.","são interdependentes."],"D",
  "Em regra, os direitos humanos são relativos e podem ser limitados por ponderação, com exceção discutida da proibição da tortura.","Em regra, relativos."),
 ("História","As primeiras constituições a preverem direitos sociais foram as do:",
  ["Brasil (1824) e dos EUA (1787).","México (1917) e de Weimar, Alemanha (1919).","França (1958) e da Itália (1947).","Portugal (1976) e da Espanha (1978).","Japão (1946) e da Índia (1950)."],"B",
  "Marcos do constitucionalismo social.","Sociais: México 1917, Weimar 1919."),
 ("Dimensões","Os direitos civis e políticos, que exigem em regra abstenção do Estado, correspondem à:",
  ["primeira dimensão, ligada à liberdade.","segunda dimensão, ligada à igualdade.","terceira dimensão, ligada à fraternidade.","quarta dimensão, ligada à genética.","quinta dimensão, ligada à paz."],"A",
  "Associação didática com o lema liberdade, igualdade e fraternidade.","1ª = liberdade."),
 ("Dimensões","O direito ao meio ambiente ecologicamente equilibrado é classicamente apontado como direito de:",
  ["primeira dimensão.","segunda dimensão.","terceira dimensão.","quarta dimensão, segundo Bobbio.","nenhuma dimensão."],"C",
  "Direitos difusos e coletivos, de solidariedade (fraternidade).","Meio ambiente = 3ª."),
 ("DUDH","A Declaração Universal dos Direitos Humanos foi adotada:",
  ["por tratado assinado em 1966.","pela Assembleia Geral da ONU, em 10 de dezembro de 1948.","pela OEA, em 1969.","pelo Conselho de Segurança, em 1945.","pela Constituição brasileira, em 1988."],"B",
  "Resolução 217 A (III), com 30 artigos.","DUDH: 10/12/1948."),
 ("DUDH","Quanto à natureza jurídica da DUDH, é correto afirmar:",
  ["é tratado ratificado por todos os países.","é resolução da Assembleia Geral, e muitos de seus dispositivos são considerados costume internacional.","é lei federal brasileira.","é decisão da Corte Interamericana.","não tem nenhum valor jurídico ou político."],"B",
  "Formalmente, não é tratado; a doutrina reconhece força de costume a vários de seus dispositivos.","DUDH = resolução."),
 ("Tratados","A chamada Carta Internacional dos Direitos Humanos é formada:",
  ["pela DUDH e pelo Pacto de São José.","pela DUDH e pelos dois Pactos de 1966 (PIDCP e PIDESC).","pela Carta da ONU e pela Constituição.","pelos tratados da OEA.","pela Convenção contra a Tortura."],"B",
  "DUDH (1948) + PIDCP e PIDESC (1966).","Carta = DUDH + 2 Pactos."),
 ("Tratados","O Pacto de São José da Costa Rica:",
  ["é tratado do sistema global da ONU de 1966.","é a Convenção Americana sobre Direitos Humanos, de 1969, promulgada no Brasil pelo Decreto nº 678/1992.","foi revogado pela Constituição de 1988.","trata apenas de direitos sociais.","não foi ratificado pelo Brasil."],"B",
  "Sistema interamericano (OEA).","São José = Convenção Americana (1969)."),
 ("Constituição","Tratados de direitos humanos aprovados, em cada Casa do Congresso, em dois turnos, por três quintos dos votos, são:",
  ["equivalentes a leis ordinárias.","equivalentes a emendas constitucionais.","supralegais.","infraconstitucionais sem eficácia.","decretos regulamentares."],"B",
  "CF, art. 5º, § 3º (EC nº 45/2004).","Rito especial = emenda."),
 ("Constituição","Segundo o STF, tratados de direitos humanos aprovados pelo rito comum têm hierarquia:",
  ["constitucional.","supralegal.","de lei ordinária.","de decreto.","de resolução."],"B",
  "RE 466.343 (2008); daí a Súmula Vinculante 25 (proibição da prisão civil do depositário infiel).","Rito comum = supralegal."),
 ("IDC","Nas hipóteses de grave violação de direitos humanos, o incidente de deslocamento de competência para a Justiça Federal é suscitado:",
  ["pelo Ministro da Justiça perante o STF.","pelo Procurador-Geral da República perante o STJ.","pelo governador perante o TJ.","pela vítima perante o juiz estadual.","pelo delegado perante o MPF."],"B",
  "CF, art. 109, V-A e § 5º.","IDC: PGR → STJ."),
 ("Espécies","Assinale a alternativa que contém apenas direitos sociais expressos no art. 6º da Constituição:",
  ["voto, plebiscito e referendo.","alimentação, transporte e segurança.","liberdade de expressão e de crença.","inviolabilidade do domicílio e sigilo.","propriedade e herança."],"B",
  "Art. 6º, com a redação da EC nº 90/2015.","Segurança e transporte são sociais."),
 ("Espécies","O plebiscito, o referendo e a iniciativa popular são exemplos de:",
  ["direitos sociais.","direitos políticos.","direitos culturais.","direitos difusos.","garantias processuais."],"B",
  "CF, art. 14: formas de exercício da soberania popular.","Participação = políticos."),
 ("PIDESC","O PIDESC estabelece que os Estados devem adotar medidas, até o máximo de seus recursos disponíveis, para assegurar os direitos nele previstos de forma:",
  ["imediata e integral.","progressiva.","facultativa.","exclusivamente judicial.","temporária."],"B",
  "Art. 2.1 do PIDESC (Decreto nº 591/1992).","PIDESC = realização progressiva."),
 ("Preso","É direito constitucional da pessoa presa:",
  ["permanecer incomunicável por 10 dias.","ser informada de seus direitos, entre os quais o de permanecer calada.","ser exibida à imprensa.","dispensar a comunicação da prisão ao juiz.","ser interrogada sem advogado e sem informação de direitos."],"B",
  "CF, art. 5º, LXIII; também a comunicação imediata da prisão (LXII) e a identificação dos responsáveis (LXIV).","Preso: direito ao silêncio."),
 ("Uso da força","Segundo a Lei nº 13.060/2014, NÃO é legítimo o uso de arma de fogo:",
  ["em legítima defesa contra agressão armada.","contra pessoa em fuga que esteja desarmada ou que não represente risco imediato de morte ou lesão.","para proteger terceiro de risco imediato de morte.","contra veículo cujo condutor ameace atropelar agentes.","em defesa da própria vida."],"B",
  "Art. 2º, parágrafo único, I. Também não é legítimo contra veículo que fura bloqueio, salvo risco de morte ou lesão.","Fuga desarmada: não atirar."),
 ("Uso da força","São princípios expressos no art. 2º da Lei nº 13.060/2014:",
  ["legalidade, necessidade, razoabilidade e proporcionalidade.","hierarquia e disciplina, apenas.","oportunidade e conveniência.","celeridade e economicidade.","publicidade e eficiência, apenas."],"A",
  "A lei manda priorizar instrumentos de menor potencial ofensivo, sem risco à integridade dos policiais.","Legalidade, necessidade, razoabilidade, proporcionalidade."),
 ("Algemas","Segundo a Súmula Vinculante 11, o uso de algemas é lícito:",
  ["em qualquer prisão, por segurança.","apenas em caso de resistência, fundado receio de fuga ou perigo à integridade física, justificada a excepcionalidade por escrito.","somente com ordem judicial prévia.","apenas para presos condenados.","nunca, por violar a dignidade."],"B",
  "Sob pena de responsabilidade do agente e de nulidade da prisão ou do ato.","Algema: exceção justificada por escrito."),
 ("Prática","Durante uma ocorrência, um guarda municipal vê um colega agredindo um detido já imobilizado para que ele confesse. A conduta correta, à luz dos direitos humanos e da lei, é:",
  ["ignorar, pois o detido é suspeito.","intervir para cessar a agressão e comunicar o fato, pois a omissão de quem tinha o dever de evitar a tortura é crime.","participar, para agilizar a confissão.","apenas registrar a confissão obtida.","fotografar o detido para divulgação."],"B",
  "A agressão para obter confissão é tortura (Lei nº 9.455/1997); quem se omite tendo o dever de evitar responde (art. 1º, § 2º).","Omissão diante da tortura é crime.")]
questoes(Q, "BCDBAECADBEBCDBEACBDBAEB")
respostas_treinos()

referencias('''<h3>Fontes consultadas</h3><ul>
<li>Constituição Federal (portal do Planalto): arts. 1º, III; 4º, II; 5º (III, XVI, XLIX, LVII, LXII, LXIII, LXIV e §§ 1º a 4º); 6º; 14; 109, V-A e § 5º.</li>
<li>Decreto nº 678/1992 (Pacto de São José); Decreto nº 592/1992 (PIDCP); Decreto nº 591/1992 (PIDESC), no portal do Planalto.</li>
<li>Lei nº 13.060/2014 e Decreto nº 12.341/2024 (uso da força), no portal do Planalto.</li>
<li>Declaração Universal dos Direitos Humanos, reprodução em português do UNICEF Brasil (o site oficial do Alto Comissariado da ONU não pôde ser acessado na pesquisa).</li>
<li>Lei nº 9.455/1997 e Lei nº 13.869/2019 (conferidas para o Caderno 08); CPP, art. 310 (conferido para o Caderno 13).</li>
<li>Citados sem conferência nesta edição: Declaração e Programa de Ação de Viena (1993); Código de Conduta da ONU para os Funcionários Responsáveis pela Aplicação da Lei (1979); Princípios Básicos sobre o Uso da Força e de Armas de Fogo (1990).</li></ul>
<h3>Jurisprudência citada</h3><ul><li>STF: RE 466.343 (status supralegal, 2008); Súmulas Vinculantes 11 (algemas) e 25 (depositário infiel).</li></ul>''',
 'As normas foram conferidas em fontes oficiais (Planalto) e a DUDH, em reprodução do UNICEF Brasil. <strong>Limitações:</strong> os textos do Planalto não informam a data da última atualização e não substituem o Diário Oficial; há divergência, entre fontes, sobre o dia exato de adoção do PIDESC em dezembro de 1966, por isso o caderno indica apenas o ano. Conceitos como as dimensões de direitos, os fundamentos e boa parte das características são <strong>construções doutrinárias</strong>, com divergências entre autores (especialmente na 4ª e na 5ª dimensões). As súmulas e decisões citadas não foram reconferidas nos portais oficiais dos tribunais nesta edição. Confira o edital do seu concurso.', DATA)
encerramento("14", "Direitos Humanos", 'Sugestão de continuação: <strong>Caderno 15 · Código de Trânsito Brasileiro</strong>.')
gravar(HERE, "Mapa da Aprovação — Caderno 14 — Direitos Humanos", Q)
