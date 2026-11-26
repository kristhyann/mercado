"""Gera miolo.html do Caderno 17: Língua Portuguesa — Gramática, Interpretação e Questões. Uso: python3 gerar.py
Norma-padrão do português brasileiro e Acordo Ortográfico de 1990 (vigente no Brasil desde 2016, com o VOLP da ABL)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit
from kit import *

DATA = "26 de novembro de 2026"
kit.U = {1:("UNIDADE 1","Interpretação de textos"),2:("UNIDADE 2","Classes gramaticais"),3:("UNIDADE 3","Sintaxe"),4:("UNIDADE 4","Concordância e regência"),5:("UNIDADE 5","Crase e pontuação"),6:("UNIDADE 6","Ortografia e acentuação")}

def ok(t): return f'<span style="color:{C["green"]};font-weight:800">✔ {t}</span>'
def no(t): return f'<span style="color:{C["red"]};font-weight:800;text-decoration:line-through">{t}</span>'

# ---------------- diagramas ----------------
def frase_arvore():
    N,B=C['navy'],C['blue']
    s = f'<figure><svg viewBox="0 0 640 230" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    s += f'<text x="320" y="30" text-anchor="middle" font-size="19" font-weight="800" fill="{C["ink"]}">Os guardas municipais orientaram os pedestres.</text>'
    s += f'<rect x="58" y="44" width="236" height="6" rx="3" fill="{N}"/><rect x="304" y="44" width="278" height="6" rx="3" fill="{B}"/>'
    s += f'<g stroke="#9aa3ad" stroke-width="2.4"><line x1="176" y1="52" x2="176" y2="80"/><line x1="443" y1="52" x2="443" y2="80"/><line x1="380" y1="124" x2="380" y2="150"/><line x1="510" y1="124" x2="510" y2="150"/><line x1="380" y1="150" x2="510" y2="150"/><line x1="443" y1="124" x2="443" y2="150"/></g>'
    s += f'<rect x="66" y="80" width="220" height="44" rx="10" fill="{NV}" stroke="{N}" stroke-width="2.4"/><text x="176" y="100" text-anchor="middle" font-size="13" font-weight="900" fill="{N}">SUJEITO</text><text x="176" y="116" text-anchor="middle" font-size="10" fill="{C["ink"]}">de quem se fala · núcleo: guardas</text>'
    s += f'<rect x="343" y="80" width="200" height="44" rx="10" fill="{C["sky"]}" stroke="{B}" stroke-width="2.4"/><text x="443" y="100" text-anchor="middle" font-size="13" font-weight="900" fill="{B}">PREDICADO</text><text x="443" y="116" text-anchor="middle" font-size="10" fill="{C["ink"]}">o que se diz do sujeito</text>'
    s += f'<rect x="320" y="156" width="120" height="44" rx="10" fill="#fff" stroke="{B}" stroke-width="2"/><text x="380" y="176" text-anchor="middle" font-size="11.5" font-weight="900" fill="{B}">VERBO (VTD)</text><text x="380" y="192" text-anchor="middle" font-size="10" fill="{C["ink"]}">orientaram</text>'
    s += f'<rect x="450" y="156" width="130" height="44" rx="10" fill="#fff" stroke="{B}" stroke-width="2"/><text x="515" y="176" text-anchor="middle" font-size="11.5" font-weight="900" fill="{B}">OBJETO DIRETO</text><text x="515" y="192" text-anchor="middle" font-size="10" fill="{C["ink"]}">os pedestres</text>'
    s += f'<text x="176" y="160" text-anchor="middle" font-size="10.5" font-weight="800" fill="{C["red"]}">Pergunte ao verbo: QUEM orientou?</text><text x="176" y="176" text-anchor="middle" font-size="10.5" font-weight="800" fill="{C["red"]}">“Os guardas municipais” = sujeito.</text>'
    return s + '</svg><figcaption>Análise de uma oração: sujeito, predicado e complemento.</figcaption></figure>'

def crase_conta():
    s = f'<figure><svg viewBox="0 0 640 200" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    for x,t,a,c in [(90,"a","preposição","(quem exige é o verbo ou nome)"),(270,"a","artigo","(quem aceita é a palavra feminina)"),(470,"à","crase","(fusão das duas)")]:
        col = C['blue'] if x<400 else C['red']
        s += f'<circle cx="{x}" cy="70" r="46" fill="{C["sky"] if x<400 else C["redsoft"]}" stroke="{col}" stroke-width="3"/><text x="{x}" y="88" text-anchor="middle" font-size="52" font-weight="900" fill="{col}">{t}</text>'
        s += f'<text x="{x}" y="138" text-anchor="middle" font-size="13" font-weight="900" fill="{col}">{a}</text><text x="{x}" y="156" text-anchor="middle" font-size="10" fill="{C["muted"]}">{c}</text>'
    s += f'<text x="180" y="86" text-anchor="middle" font-size="40" font-weight="900" fill="{C["ink"]}">+</text><text x="370" y="86" text-anchor="middle" font-size="40" font-weight="900" fill="{C["ink"]}">=</text>'
    s += f'<text x="320" y="188" text-anchor="middle" font-size="12" font-weight="800" fill="{C["navy"]}">Teste: troque a palavra feminina por uma masculina. Se aparecer “ao”, há crase.</text>'
    return s + '</svg><figcaption>A crase é a fusão da preposição “a” com o artigo “a”.</figcaption></figure>'

def virgula_proibida():
    s = f'<figure><svg viewBox="0 0 640 170" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    for y,(a,b,c) in [(20,("O candidato aprovado","comemorou","o resultado.")),(96,("Ontem à noite","o candidato","comemorou."))]:
        pass
    s += f'<rect x="20" y="16" width="600" height="56" rx="12" fill="{C["redsoft"]}" stroke="{C["red"]}" stroke-width="2"/>'
    s += f'<text x="40" y="52" font-size="17" font-weight="800" fill="{C["ink"]}">O candidato aprovado<tspan fill="{C["red"]}" font-size="26">,</tspan> comemorou<tspan fill="{C["red"]}" font-size="26">,</tspan> o resultado.</text>'
    s += f'<text x="600" y="52" text-anchor="end" font-size="12" font-weight="900" fill="{C["red"]}">ERRADO</text>'
    s += f'<rect x="20" y="92" width="600" height="56" rx="12" fill="{C["greensoft"]}" stroke="{C["green"]}" stroke-width="2"/>'
    s += f'<text x="40" y="128" font-size="17" font-weight="800" fill="{C["ink"]}">Ontem à noite<tspan fill="{C["green"]}" font-size="26">,</tspan> o candidato comemorou o resultado.</text><text x="600" y="128" text-anchor="end" font-size="12" font-weight="900" fill="{C["green"]}">CERTO</text>'
    return s + '</svg><figcaption>Não se separa o sujeito do verbo nem o verbo do complemento; o adjunto adverbial deslocado pode ser isolado.</figcaption></figure>'

def acento_fluxo():
    N,B=C['navy'],C['blue']
    s = f'<figure><svg viewBox="0 0 640 250" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    s += f'<rect x="220" y="8" width="200" height="40" rx="10" fill="{N}"/><text x="320" y="33" text-anchor="middle" font-size="13" font-weight="900" fill="#fff">Onde está a sílaba tônica?</text>'
    s += '<g stroke="#9aa3ad" stroke-width="2.4"><path d="M320 48 V62 M110 62 H530 M110 62 V76 M320 62 V76 M530 62 V76"/></g>'
    cols=[(110,"ÚLTIMA","OXÍTONA","acentua se terminar em","a(s), e(s), o(s), em, ens","sofá · café · avô · também",C['green'],C['greensoft']),
          (320,"PENÚLTIMA","PAROXÍTONA","acentua se terminar em","l, n, r, x, i(s), us, um, ã(o), ps, ditongo","fácil · hífen · açúcar · táxi · vírus",B,C['sky']),
          (530,"ANTEPENÚLTIMA","PROPAROXÍTONA","acentua","SEMPRE","lâmpada · público · árvore",C['red'],C['redsoft'])]
    for x,a,b,c,d,e,fg,bg in cols:
        s += f'<rect x="{x-100}" y="76" width="200" height="160" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/>'
        s += f'<text x="{x}" y="100" text-anchor="middle" font-size="11" font-weight="800" fill="{C["muted"]}">{a}</text><text x="{x}" y="122" text-anchor="middle" font-size="15" font-weight="900" fill="{fg}">{b}</text>'
        s += f'<text x="{x}" y="150" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">{c}</text><text x="{x}" y="170" text-anchor="middle" font-size="{11 if len(d)<30 else 9.6}" font-weight="900" fill="{C["ink"]}">{d}</text>'
        s += f'<text x="{x}" y="208" text-anchor="middle" font-size="{11 if len(e)<30 else 9.8}" font-style="italic" fill="{fg}">{e}</text>'
    return s + '</svg><figcaption>As três regras de base da acentuação gráfica.</figcaption></figure>'

# ================================================================ APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">Português de prova não é decoreba: é entender por que a frase funciona do jeito que funciona.</p>
<p>Este é o <strong>Caderno 17 da coleção</strong>, dedicado à <strong>Língua Portuguesa</strong>, disciplina presente em praticamente todos os concursos. Aqui cada regra vem acompanhada do <strong>motivo</strong> e de um <strong>teste prático</strong> para você aplicar na hora da prova, como trocar a palavra feminina por masculina para descobrir a crase ou perguntar “quem?” ao verbo para achar o sujeito.</p>
<p>O caderno segue a <strong>norma-padrão</strong> do português brasileiro, que é a cobrada em provas, e o <strong>Acordo Ortográfico de 1990</strong>, obrigatório no Brasil desde 2016. Quando houver mais de uma forma aceita, o caderno avisa.</p>
{table(["Recurso","Onde está"],[["Texto autoral com questões de interpretação","Unidade 1"],["Classes gramaticais com exemplos em frases","Unidade 2"],["Análise de oração (sujeito e predicado) em esquema","Unidade 3"],["Concordância e regência em situações do dia a dia","Unidade 4"],["A “conta” da crase e o mapa da vírgula","Unidade 5"],["Fluxograma da acentuação e os porquês","Unidade 6"],["Mapa conceitual, erros comuns, flashcards e 24 questões autorais","Revisão e prática"]],["58%",None])}''', first=True)

toc_page([("u","UNIDADE 1 · INTERPRETAÇÃO DE TEXTOS","U1"),("","1. Compreender x interpretar","A01"),("","2. Tipos e gêneros textuais","A02"),("","3. Treino com texto autoral","A03"),
 ("u","UNIDADE 2 · CLASSES GRAMATICAIS","U2"),("","4. Substantivo, adjetivo e advérbio","A04"),("","5. Verbo","A05"),("","6. Pronome","A06"),("","7. Preposição e conjunção","A07"),
 ("u","UNIDADE 3 · SINTAXE","U3"),("","8. Sujeito","A08"),("","9. Predicado e complementos","A09"),("","10. Orações coordenadas e subordinadas","A10"),
 ("u","UNIDADE 4 · CONCORDÂNCIA E REGÊNCIA","U4"),("","11. Concordância verbal","A11"),("","12. Concordância nominal","A12"),("","13. Regência","A13"),
 ("u","UNIDADE 5 · CRASE E PONTUAÇÃO","U5"),("","14. Crase","A14"),("","15. Pontuação","A15"),
 ("u","UNIDADE 6 · ORTOGRAFIA E ACENTUAÇÃO","U6"),("","16. Ortografia: dúvidas frequentes","A16"),("","17. Acentuação gráfica","A17"),
 ("u","REVISÃO E PRÁTICA","RV"),("","Mapa conceitual · Erros mais comuns","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),("","Gabarito, respostas dos treinos e referências","R4")])

# ================================================================ UNIDADE 1
opener("01","UNIDADE 1","Interpretação de textos",["Compreender x interpretar","Tipos e gêneros textuais","Treino com texto autoral"],"U1")

add(H(1,'Compreender x <span class="hl">interpretar</span>','As duas operações que a banca cobra.', "A01") +
 table(["Operação","O que é","Como a questão costuma perguntar"],[
  ["Compreensão","Identificar o que está <b>escrito</b> no texto","“Segundo o texto…”, “De acordo com o autor…”, “O texto informa que…”"],
  ["Interpretação","Concluir o que o texto <b>permite deduzir</b>, sem estar escrito com essas palavras","“Infere-se do texto…”, “Depreende-se…”, “O texto permite concluir…”"]],["18%","38%",None]) +
 traduz(p('Imagine que um colega diz: “Chegou encharcado ao plantão”. <strong>Compreender</strong> é saber que ele chegou molhado. <strong>Interpretar</strong> é concluir que provavelmente estava chovendo ou que ele foi pego por algum imprevisto. Mas cuidado: concluir que ele “não tem guarda-chuva” já é ir além do que a frase autoriza.')) +
 table(["Erro de leitura","O que acontece","Exemplo"],[
  ["Extrapolação","Vai além do que o texto diz","O texto fala em “aumento de furtos” e a alternativa diz que “a cidade é a mais violenta do país”"],
  ["Redução","Toma uma parte pelo todo","O texto cita várias causas e a alternativa diz que há uma só"],
  ["Contradição","Diz o oposto do texto","O texto afirma que o projeto “reduziu” as ocorrências e a alternativa diz que as “aumentou”"]],["18%","30%",None]) +
 memo('Na prova, a alternativa correta precisa ter <strong>apoio no texto</strong>. Desconfie de palavras absolutas como <strong>sempre, nunca, todos, somente, exclusivamente</strong>.'))

add(H(1,'Tipos e <span class="hl">gêneros</span> textuais','Estrutura x formato social.', "A02") +
 p('<strong>Tipo textual</strong> é a estrutura predominante de um trecho, definida pelo modo de organização da linguagem: são poucos e fixos. <strong>Gênero textual</strong> é o formato concreto que circula na sociedade, com função e público definidos: são muitos (notícia, ofício, receita, bula, crônica, edital).') +
 table(["Tipo","O que faz","Marcas","Gêneros em que predomina"],[
  ["Narrativo","Conta fatos em sequência","Personagens, tempo, lugar, verbos de ação no passado","Conto, crônica, notícia, boletim de ocorrência"],
  ["Descritivo","Caracteriza seres, lugares, objetos","Adjetivos, verbos de estado","Retrato falado, anúncio de imóvel"],
  ["Dissertativo-argumentativo","Defende um ponto de vista","Tese, argumentos, conectivos de causa e conclusão","Artigo de opinião, editorial, redação de concurso"],
  ["Expositivo","Explica e informa, sem defender opinião","Definições, dados, linguagem objetiva","Verbete, aula, texto didático"],
  ["Injuntivo (instrucional)","Orienta o leitor a agir","Verbos no imperativo, passos","Manual, receita, edital, placa de orientação"]],["20%","22%","30%",None]) +
 lembre(p('Um mesmo gênero pode misturar tipos. Uma <strong>notícia</strong> narra o fato, descreve o local e pode expor dados; o que importa é identificar o tipo <strong>predominante</strong> no trecho indicado pela questão.'), "Tipos se misturam"))

TEXTO = ('<p style="border-left:5px solid #6b3fa0;padding:6pt 12pt;background:#f2ebfa;border-radius:6pt"><strong>A praça que voltou a ter gente</strong> (texto autoral)<br>'
 '(1) Durante anos, a praça central do bairro foi evitada pelos moradores. A iluminação era precária, os bancos estavam quebrados e, ao entardecer, o espaço ficava vazio. '
 '(2) Há dois anos, a prefeitura reformou o local, instalou novas luminárias e passou a manter uma equipe da Guarda Municipal em ronda fixa. '
 '(3) A mudança, contudo, não veio apenas das obras: comerciantes organizaram uma feira aos sábados, e a escola vizinha começou a usar a praça para atividades ao ar livre. '
 '(4) Hoje, famílias ocupam o espaço até a noite. Segundo os moradores, a sensação de segurança aumentou porque a praça voltou a ser um lugar de convivência, e não só porque passou a ser vigiada.</p>')

add(H(1,'Treino com <span class="hl">texto autoral</span>','Leia e responda antes de conferir.', "A03") + TEXTO +
 table(["Pergunta","Resposta comentada"],[
  ["1. Qual é o tipo textual predominante?","<b>Narrativo</b>, com trechos descritivos: o texto relata uma mudança ao longo do tempo (“durante anos”, “há dois anos”, “hoje”)"],
  ["2. Pode-se afirmar que a reforma foi a única causa da mudança?","<b>Não</b>. O período 3 diz que a mudança “não veio apenas das obras”: houve a feira e as atividades da escola. Afirmar causa única é <b>redução</b>"],
  ["3. O que a conjunção “contudo” (período 3) expressa?","<b>Oposição</b> (adversativa): quebra a expectativa de que só as obras explicariam a mudança. Pode ser trocada por “porém” ou “no entanto”"],
  ["4. Infere-se que a praça era pouco usada à noite antes da reforma?","<b>Sim</b>. O período 1 informa que “ao entardecer, o espaço ficava vazio”"],
  ["5. É correto dizer que o texto critica a atuação da Guarda Municipal?","<b>Não</b>. O texto apenas relativiza: a segurança aumentou “não só” pela vigilância. Ver crítica é <b>extrapolação</b>"]],["40%",None]))

treino(1, [
 ("Quando a questão pergunta “segundo o texto”, ela cobra compreensão, ou seja, o que está escrito.","C","Compreensão é localizar a informação."),
 ("Interpretar um texto permite qualquer conclusão do leitor, desde que coerente com sua experiência.","E","A conclusão precisa ter apoio no texto."),
 ("Afirmar que um texto trata de “todas” as causas de um problema quando ele cita apenas algumas é um caso de redução.","E","É extrapolação (vai além). Redução é tomar uma parte como se fosse o todo."),
 ("O edital de concurso é um gênero em que predomina o tipo injuntivo.","C","Orienta o candidato sobre como proceder."),
 ("No texto autoral, a reforma da praça é apresentada como a única causa da mudança.","E","“Não veio apenas das obras.”"),
 ("Tipos textuais são poucos e fixos; gêneros textuais são muitos e variam conforme a função social.","C","Distinção básica.")])

# ================================================================ UNIDADE 2
opener("02","UNIDADE 2","Classes gramaticais",["Substantivo, adjetivo e advérbio","Verbo","Pronome","Preposição e conjunção"],"U2")

add(H(2,'Substantivo, adjetivo e <span class="hl">advérbio</span>','Quem nomeia, quem caracteriza, quem dá a circunstância.', "A04") +
 p('A língua portuguesa tem <strong>dez classes de palavras</strong>: substantivo, artigo, adjetivo, numeral, pronome, verbo, advérbio, preposição, conjunção e interjeição. A classe depende da <strong>função na frase</strong>, e não da palavra isolada.') +
 table(["Classe","Função","Exemplo na frase"],[
  ["Substantivo","Nomeia seres, objetos, lugares, sentimentos, ações","A <b>guarda</b> garantiu a <b>segurança</b> do <b>evento</b>."],
  ["Adjetivo","Caracteriza o substantivo; concorda com ele","Foi uma ação <b>rápida</b> e <b>eficiente</b>."],
  ["Advérbio","Indica circunstância (tempo, lugar, modo, intensidade, negação); é <b>invariável</b>","Ela chegou <b>cedo</b> e agiu <b>muito</b> <b>bem</b>."]],["18%","40%",None]) +
 ex(p('Veja como a função muda a classe: em “o <b>jantar</b> estava ótimo”, <i>jantar</i> é substantivo (vem com artigo); em “vamos <b>jantar</b>”, é verbo. Em “ela é <b>meio</b> tímida”, <i>meio</i> é advérbio (= um pouco) e não varia; em “comeu <b>meia</b> pizza”, é numeral e concorda.'), "Mesma palavra, classes diferentes") +
 pega('<ul><li>Advérbio <b>não varia</b>: “Elas estavam <b>meio</b> nervosas” (e não “meias nervosas”).</li><li>“Bastante” varia quando é adjetivo (= muitos): “<b>bastantes</b> candidatos”; não varia quando é advérbio: “estudaram <b>bastante</b>”.</li></ul>'))

add(H(2,'<span class="hl">Verbo</span>','Ação, estado ou fenômeno, flexionado no tempo.', "A05") +
 p('O verbo é a classe mais rica em flexões: varia em <strong>pessoa</strong> (eu, tu, ele…), <strong>número</strong> (singular, plural), <strong>tempo</strong> (presente, pretérito, futuro), <strong>modo</strong> e <strong>voz</strong>.') +
 table(["Modo","Indica","Exemplo"],[
  ["Indicativo","Certeza, fato","O candidato <b>estuda</b> todos os dias."],
  ["Subjuntivo","Dúvida, hipótese, desejo","Espero que ele <b>estude</b>. Se ele <b>estudasse</b>, passaria."],
  ["Imperativo","Ordem, pedido, conselho","<b>Estude</b> com método."]],["18%","30%",None]) +
 table(["Voz","Quem pratica a ação","Exemplo"],[
  ["Ativa","O sujeito pratica","A guarda <b>fiscalizou</b> o evento."],
  ["Passiva analítica","O sujeito sofre (ser + particípio)","O evento <b>foi fiscalizado</b> pela guarda."],
  ["Passiva sintética","O sujeito sofre (verbo + se)","<b>Fiscalizaram-se</b> os eventos."],
  ["Reflexiva","O sujeito pratica e sofre","O candidato <b>se preparou</b>."]],["22%","30%",None]) +
 traduz(p('Para testar a voz passiva sintética, transforme em analítica: “Vendem-se casas” vira “Casas <strong>são vendidas</strong>”. Deu certo? Então “casas” é o sujeito e o verbo vai para o plural. Isso será essencial na concordância (Unidade 4).'), "profa"))

add(H(2,'<span class="hl">Pronome</span>','Substitui ou acompanha o substantivo.', "A06") +
 table(["Tipo","Exemplos","Ponto de prova"],[
  ["Pessoal reto · oblíquo","eu, tu, ele · me, te, se, o, a, lhe","Na norma-padrão, o reto é sujeito; o oblíquo, complemento: “Entre <b>mim</b> e você”; “para <b>eu</b> fazer” (eu é sujeito de fazer)"],
  ["Possessivo","meu, teu, seu, nosso","“Seu” pode gerar ambiguidade: “Ana disse a Rita que <b>seu</b> carro foi multado” (de quem?)"],
  ["Demonstrativo","este, esse, aquele (e variações), isto, isso, aquilo","<b>Este</b>: perto de quem fala ou o que ainda vai ser dito. <b>Esse</b>: perto de quem ouve ou o que já foi dito"],
  ["Relativo","que, o qual, quem, cujo, onde","<b>Cujo</b> indica posse e não admite artigo depois: “o servidor <b>cujo</b> processo” (nunca “cujo o”). <b>Onde</b> só para lugar"],
  ["Indefinido","alguém, ninguém, todo, algum, nenhum, cada","“Algum” depois do substantivo vale negação: “motivo <b>algum</b>” = nenhum motivo"],
  ["De tratamento","você, Vossa Senhoria, Vossa Excelência","Pede verbo e possessivo na 3ª pessoa: “Vossa Excelência <b>decidiu</b> sobre <b>seu</b> pedido”"]],["20%","28%",None]))

add(H(2,'Preposição e <span class="hl">conjunção</span>','As palavras que ligam.', "A07") +
 table(["Classe","O que liga","Exemplos"],[
  ["Preposição","Liga <b>palavras</b>, criando relação de dependência entre elas","a, ante, após, até, com, contra, de, desde, em, entre, para, perante, por, sem, sob, sobre, trás"],
  ["Conjunção","Liga <b>orações</b> (ou termos de mesma função), estabelecendo sentido entre elas","e, mas, porém, porque, embora, se, quando, logo, portanto"]],["18%","38%",None]) +
 table(["Sentido da conjunção","Exemplos","Na frase"],[
  ["Adição","e, nem, não só… mas também","Estudou <b>e</b> foi aprovado."],
  ["Oposição (adversativa)","mas, porém, contudo, todavia, entretanto, no entanto","Estudou, <b>mas</b> não foi aprovado."],
  ["Concessão","embora, ainda que, mesmo que, conquanto","<b>Embora</b> tenha estudado, não foi aprovado."],
  ["Causa","porque, como (no início), já que, visto que","<b>Como</b> estudou, foi aprovado."],
  ["Conclusão","logo, portanto, por isso, pois (depois do verbo)","Estudou; foi, <b>portanto</b>, aprovado."],
  ["Condição","se, caso, desde que","<b>Se</b> estudar, será aprovado."],
  ["Finalidade","para que, a fim de que","Estudou <b>para que</b> fosse aprovado."]],["26%","38%",None]) +
 memo('<strong>Mas</strong> e <strong>embora</strong> têm sentido parecido (contraste), mas estrutura diferente: com “mas”, o verbo fica no indicativo; com “embora”, no <strong>subjuntivo</strong>. Questões de reescrita exploram isso.'))

treino(2, [
 ("Em “Ela estava meio cansada”, a palavra “meio” é advérbio e, por isso, não deve variar.","C","Advérbio é invariável."),
 ("Em “Espero que você estude”, o verbo “estude” está no modo indicativo.","E","Está no subjuntivo (desejo)."),
 ("A frase “O servidor cujo o processo foi arquivado” está de acordo com a norma-padrão.","E","“Cujo” não admite artigo depois: “cujo processo”."),
 ("Em “Entre mim e você”, o uso do pronome “mim” está correto.","C","Depois de preposição, usa-se o oblíquo tônico."),
 ("As conjunções “mas” e “contudo” expressam oposição.","C","São adversativas."),
 ("“Embora” é conjunção que exprime conclusão.","E","Exprime concessão.")])

# ================================================================ UNIDADE 3
opener("03","UNIDADE 3","Sintaxe",["Sujeito","Predicado e complementos","Orações coordenadas e subordinadas"],"U3")

add(H(3,'<span class="hl">Sujeito</span>','O termo com o qual o verbo concorda.', "A08") +
 frase_arvore() +
 table(["Tipo de sujeito","Como reconhecer","Exemplo"],[
  ["Simples","Um núcleo","<b>Os moradores</b> aprovaram a reforma."],
  ["Composto","Dois ou mais núcleos","<b>A escola e a feira</b> movimentaram a praça."],
  ["Oculto (desinencial)","Não aparece, mas a terminação do verbo o revela","Chegamos cedo. (nós)"],
  ["Indeterminado","Existe, mas não se sabe ou não se quer dizer quem é: verbo na 3ª pessoa do plural sem referente, ou verbo + se (sem objeto direto)","<b>Roubaram</b> o celular. <b>Precisa-se</b> de vigilantes."],
  ["Oração sem sujeito","Verbos impessoais: haver (= existir), fazer (tempo), fenômenos da natureza","<b>Há</b> vagas. <b>Faz</b> dez anos. <b>Choveu</b> muito."]],["22%","40%",None]) +
 pega('<ul><li>O sujeito pode vir <b>depois</b> do verbo: “Chegaram <b>as provas</b>.” Pergunte ao verbo: o que chegou?</li><li>“Haver” no sentido de existir <b>não tem sujeito</b>: “Havia muitos candidatos” (e não “haviam”).</li></ul>'))

add(H(3,'Predicado e <span class="hl">complementos</span>','O que o verbo precisa para fazer sentido.', "A09") +
 table(["Transitividade","Precisa de…","Exemplo"],[
  ["Intransitivo (VI)","Nada; sentido completo","O candidato <b>chegou</b>."],
  ["Transitivo direto (VTD)","Complemento <b>sem</b> preposição (objeto direto)","Ela <b>leu</b> o edital."],
  ["Transitivo indireto (VTI)","Complemento <b>com</b> preposição (objeto indireto)","Ele <b>obedeceu</b> às normas."],
  ["Transitivo direto e indireto (VTDI)","Os dois complementos","<b>Entregou</b> o relatório ao chefe."],
  ["De ligação (VL)","Um predicativo (característica ou estado do sujeito)","A praça <b>ficou</b> movimentada."]],["30%","34%",None]) +
 table(["Predicado","Núcleo","Exemplo"],[
  ["Verbal","Um verbo de ação (significativo)","Os guardas <b>patrulharam</b> o bairro."],
  ["Nominal","Um predicativo, ligado por verbo de ligação (ser, estar, parecer, ficar, permanecer, continuar)","A equipe <b>estava</b> <b>preparada</b>."],
  ["Verbo-nominal","Um verbo de ação e um predicativo","Os candidatos <b>saíram</b> <b>confiantes</b>."]],["20%","44%",None]) +
 lembre(p('Outros termos frequentes: <strong>adjunto adverbial</strong> (circunstância: “à noite”, “no bairro”), <strong>adjunto adnominal</strong> (acompanha o substantivo: “os”, “novas”), <strong>aposto</strong> (explica um termo, em geral entre vírgulas: “Ana, <b>a coordenadora</b>, falou”) e <strong>vocativo</strong> (chamamento: “<b>Candidatos</b>, atenção!”).'), "Outros termos da oração"))

add(H(3,'Orações coordenadas e <span class="hl">subordinadas</span>','Como as orações se combinam no período.', "A10") +
 p('<strong>Período</strong> é a frase com um ou mais verbos. Cada verbo (ou locução verbal) forma uma <strong>oração</strong>. As orações se combinam de dois jeitos:') +
 table(["Processo","Relação","Exemplo"],[
  ["Coordenação","Orações <b>independentes</b> sintaticamente, lado a lado","Estudei muito, <b>mas</b> não passei."],
  ["Subordinação","Uma oração <b>depende</b> da outra e exerce função nela (sujeito, objeto, adjunto)","Espero <b>que você passe</b>. (objeto de “espero”)"]],["20%","40%",None]) +
 table(["Subordinada adjetiva","Sentido","Exemplo"],[
  ["Restritiva (sem vírgula)","Restringe: só uma parte do grupo","Os candidatos <b>que estudaram</b> foram aprovados. (só os que estudaram)"],
  ["Explicativa (entre vírgulas)","Generaliza: todo o grupo","Os candidatos, <b>que estudaram</b>, foram aprovados. (todos estudaram)"]],["28%","26%",None]) +
 table(["Subordinada adverbial","Conjunções típicas"],[
  ["Causal","porque, como, já que, visto que"],["Concessiva","embora, ainda que, mesmo que"],["Condicional","se, caso, desde que"],["Final","para que, a fim de que"],
  ["Temporal","quando, enquanto, assim que"],["Conformativa","conforme, segundo, como (= conforme)"],["Proporcional","à medida que, à proporção que"]],["30%",None]))

treino(3, [
 ("Em “Chegaram as provas”, o sujeito é “as provas”.","C","Sujeito posposto."),
 ("Em “Havia muitos candidatos”, o sujeito é “muitos candidatos”.","E","Oração sem sujeito; “muitos candidatos” é objeto direto."),
 ("Em “Roubaram o celular”, sem referência anterior, o sujeito é indeterminado.","C","3ª pessoa do plural sem referente."),
 ("Em “A equipe estava preparada”, o predicado é nominal.","C","Verbo de ligação + predicativo."),
 ("A oração adjetiva explicativa vem sem vírgulas e restringe o sentido do termo.","E","A explicativa vem entre vírgulas e generaliza; a restritiva vem sem vírgulas."),
 ("Em “Embora chovesse, a feira aconteceu”, a oração destacada é concessiva.","C","“Embora” introduz concessão.")])

# ================================================================ UNIDADE 4
opener("04","UNIDADE 4","Concordância e regência",["Concordância verbal","Concordância nominal","Regência"],"U4")

add(H(4,'Concordância <span class="hl">verbal</span>','O verbo concorda com o sujeito em número e pessoa.', "A11") +
 p('A regra geral é simples: <strong>ache o sujeito e faça o verbo concordar com ele</strong>. Os erros de prova aparecem quando o sujeito está longe, depois do verbo ou disfarçado.') +
 table(["Situação","Regra","Exemplo"],[
  ["Sujeito depois do verbo","Concorda do mesmo jeito","<b>Faltaram</b> dois candidatos."],
  ["Sujeito composto antes do verbo","Plural","A escola e a feira <b>movimentaram</b> a praça."],
  ["Haver = existir","Impessoal: <b>singular</b>, inclusive o auxiliar","<b>Havia</b> problemas. <b>Deve haver</b> soluções."],
  ["Existir, ocorrer, acontecer","Têm sujeito: concordam","<b>Existiam</b> problemas. <b>Ocorreram</b> falhas."],
  ["Fazer (tempo decorrido)","Impessoal: singular","<b>Faz</b> dois anos que a praça foi reformada."],
  ["Verbo + se apassivador (VTD)","Concorda com o sujeito paciente","<b>Vendem-se</b> casas. (casas são vendidas)"],
  ["Verbo + se indeterminador (VTI ou VI)","Singular","<b>Precisa-se</b> de vigilantes. <b>Trata-se</b> de questões difíceis."],
  ["“A maioria de”, “grande parte de” + plural","Singular ou plural","A maioria dos candidatos <b>chegou</b> (ou <b>chegaram</b>) cedo."]],["30%","26%",None]))

atencao(scene3([("HAVER = EXISTIR",C['red'],C['redsoft'],"prof",["Havia muitas","pessoas na praça.","(não “haviam”)"],"SINGULAR"),
  ("VENDEM-SE",C['green'],C['greensoft'],"profa",["Casas são","vendidas: casas","é o sujeito."],"PLURAL"),
  ("PRECISA-SE DE",C['blue'],C['sky'],"prof",["Com preposição,","não há sujeito","paciente."],"SINGULAR")], "Situação ilustrada: o teste do “se”.") +
 p('<strong>Como decidir entre “vende-se” e “vendem-se”?</strong> Tente a voz passiva com “ser”. Se “casas <strong>são vendidas</strong>” faz sentido, o “se” é apassivador e o verbo concorda com “casas”. Se o verbo pede preposição (“precisar <strong>de</strong>”, “tratar <strong>de</strong>”), não há passiva possível: o verbo fica no singular.'),
 ["Haver impessoal", "Se apassivador", "Se indeterminador"], "O teste do “se”")

add(H(4,'Concordância <span class="hl">nominal</span>','Artigo, adjetivo, numeral e pronome concordam com o substantivo.', "A12") +
 table(["Caso","Regra","Exemplo"],[
  ["Adjetivo depois de vários substantivos","Plural ou concorda com o mais próximo","Prédio e praça <b>reformados</b> (ou <b>reformada</b>)."],
  ["Adjetivo antes de vários substantivos","Concorda com o mais próximo","<b>Nova</b> praça e prédio."],
  ["Anexo, incluso, obrigado, mesmo, próprio, quite","Variam: concordam com o termo","Seguem <b>anexas</b> as cópias. “<b>Obrigada</b>”, disse ela."],
  ["Meio","Advérbio (= um pouco): invariável · numeral (= metade): varia","Ela está <b>meio</b> cansada. Esperou <b>meia</b> hora."],
  ["Menos","Sempre invariável","Havia <b>menos</b> pessoas. (nunca “menas”)"],
  ["É proibido, é necessário, é bom","Sem artigo: invariável · com artigo: concorda","É <b>proibido</b> entrada. É <b>proibida</b> a entrada."]],["30%","30%",None]) +
 memo('Advérbio e “menos” <strong>não variam</strong>. Com artigo, a expressão <strong>concorda</strong>: “é proibid<strong>a</strong> <strong>a</strong> entrada”.'))

add(H(4,'<span class="hl">Regência</span>','Quando o verbo ou o nome pede preposição.', "A13") +
 p('<strong>Regência</strong> é a relação entre um termo e seu complemento: alguns verbos ligam-se direto ao complemento; outros exigem preposição. E o mesmo verbo pode mudar de sentido conforme a regência.') +
 table(["Verbo","Sentido e regência","Exemplo na norma-padrão"],[
  ["Assistir","Ver: VTI (a) · ajudar: VTD","Assisti <b>ao</b> jogo. O médico assistiu o paciente."],
  ["Aspirar","Desejar: VTI (a) · respirar: VTD","Aspira <b>ao</b> cargo. Aspirou o ar da manhã."],
  ["Visar","Pretender: VTI (a) · mirar ou dar visto: VTD","Visa <b>ao</b> cargo (regência tradicional). Visou o documento."],
  ["Obedecer · desobedecer","VTI (a)","Obedeça <b>às</b> normas."],
  ["Preferir","Prefere-se uma coisa <b>a</b> outra","Prefiro estudar <b>a</b> sair. (não “prefiro mais… do que”)"],
  ["Ir · chegar","Pedem a preposição <b>a</b> (destino)","Cheguei <b>ao</b> trabalho. Vou <b>à</b> escola. (na fala, “em” é comum, mas não é padrão)"],
  ["Implicar","Acarretar: VTD","A decisão implica <b>responsabilidade</b>. (não “implica em”, na regência tradicional)"],
  ["Pagar · perdoar","Coisa: VTD · pessoa: VTI (a)","Paguei a conta <b>ao</b> fornecedor."],
  ["Esquecer · lembrar","Sem pronome: VTD · com pronome: VTI (de)","Esqueci o livro. Esqueci-me <b>do</b> livro."]],["18%","34%",None]) +
 pega('<ul><li>Regência + artigo feminino = <b>crase</b>: “obedecer <b>às</b> leis”, “assistir <b>à</b> palestra”. Por isso regência e crase andam juntas.</li><li>Alguns usos (como “visar” transitivo direto no sentido de pretender e “implicar em”) já são aceitos por gramáticos e dicionários modernos; em prova, siga a regência tradicional, a menos que a questão indique o contrário.</li></ul>'))

treino(4, [
 ("A frase “Haviam muitos candidatos na sala” está correta na norma-padrão.","E","“Haver” (existir) é impessoal: “Havia”."),
 ("Em “Vendem-se apartamentos”, o verbo está corretamente no plural.","C","Apartamentos são vendidos: sujeito paciente."),
 ("A frase “Precisam-se de vigilantes” está correta.","E","Com preposição, o “se” indetermina o sujeito: “Precisa-se de vigilantes”."),
 ("Em “Seguem anexas as cópias”, a palavra “anexas” concorda corretamente.","C","“Anexo” varia."),
 ("Na norma-padrão, “assistir” no sentido de ver é transitivo indireto: “assistir ao filme”.","C","Pede a preposição “a”."),
 ("A construção “Prefiro mais estudar do que sair” segue a norma-padrão.","E","O correto é “Prefiro estudar a sair”.")])

# ================================================================ UNIDADE 5
opener("05","UNIDADE 5","Crase e pontuação",["Crase","Pontuação"],"U5")

add(H(5,'<span class="hl">Crase</span>','Não é um acento “que se coloca”: é uma fusão que acontece.', "A14") +
 crase_conta() +
 traduz(p('Para haver crase, precisam aparecer <strong>duas coisas</strong>: um termo que <strong>exige</strong> a preposição “a” (vou <strong>a</strong>, obedecer <strong>a</strong>, referir-se <strong>a</strong>) e uma palavra feminina que <strong>aceita</strong> o artigo “a”. Se faltar uma delas, não há crase. Por isso não existe crase antes de palavra masculina, de verbo ou de pronome que não aceita artigo: falta o artigo.')) +
 table(["Teste","Como fazer","Exemplo"],[
  ["Troca pelo masculino","Se o “a” vira “ao”, há crase","Fui <b>à</b> feira → fui <b>ao</b> mercado."],
  ["Ida e volta (lugares)","“Vou a, volto da” = crase; “vou a, volto de” = sem crase","Vou <b>à</b> Bahia (volto <b>da</b> Bahia). Vou <b>a</b> Roma (volto <b>de</b> Roma)."]],["24%","36%",None]))

atencao(table(["Crase obrigatória","Exemplos"],[
  ["Locuções femininas (adverbiais, prepositivas, conjuntivas)","às vezes, à noite, às pressas, à custa de, à medida que"],
  ["Indicação de horas","Chegou <b>às</b> 10h. O plantão vai das 7h <b>às</b> 19h."],
  ["“À moda de”, mesmo com a palavra moda oculta","Bife <b>à</b> milanesa. Gol <b>à</b> Pelé."],
  ["a + aquele, aquela, aquilo · a + a qual","Refiro-me <b>àquele</b> caso. A norma <b>à qual</b> obedeço."]],["44%",None]) +
 table(["Crase proibida","Exemplos"],[
  ["Antes de palavra masculina","Andar <b>a</b> pé. Pagamento <b>a</b> prazo."],
  ["Antes de verbo","Começou <b>a</b> estudar. <b>A</b> partir de hoje."],
  ["Antes de pronomes que não aceitam artigo","Entreguei <b>a</b> ela. Dirijo-me <b>a</b> Vossa Excelência."],
  ["Com “a” no singular antes de palavra no plural","Fez referência <b>a</b> pessoas."],
  ["Entre palavras repetidas","Cara <b>a</b> cara. Gota <b>a</b> gota."]],["44%",None]) +
 table(["Crase facultativa","Exemplos"],[
  ["Antes de pronome possessivo feminino no singular","Fui <b>à</b> (ou <b>a</b>) minha casa de praia."],
  ["Antes de nome próprio feminino de pessoa","Entreguei o livro <b>à</b> (ou <b>a</b>) Maria."],
  ["Depois de “até”","Foi até <b>à</b> (ou <b>a</b>) praça."]],["44%",None]),
 ["Locuções femininas", "Horas", "Masculino e verbo: nunca"], "Quando há (e quando não há) crase")

add(H(5,'<span class="hl">Pontuação</span>','A vírgula organiza a frase e pode mudar o sentido.', "A15") +
 virgula_proibida() +
 table(["Use a vírgula para…","Exemplo"],[
  ["Separar itens de uma enumeração","Trouxe caneta, lápis, borracha e documento."],
  ["Isolar o aposto explicativo","Ana, <b>a coordenadora</b>, abriu a reunião."],
  ["Isolar o vocativo","<b>Candidatos</b>, mantenham silêncio."],
  ["Isolar o adjunto adverbial deslocado (obrigatória se for longo; facultativa se for curto)","<b>Durante a madrugada</b>, a equipe permaneceu na praça."],
  ["Antes de conjunções adversativas (mas, porém)","Estudou muito, <b>mas</b> não passou."],
  ["Isolar orações adjetivas explicativas","Os moradores, <b>que participaram da feira</b>, aprovaram a reforma."],
  ["Isolar conjunções deslocadas","A reforma, <b>contudo</b>, não resolveu tudo."]],["50%",None]) +
 lembre(p('<strong>Ponto e vírgula</strong>: separa orações longas ou itens que já têm vírgula. <strong>Dois-pontos</strong>: anuncia enumeração, explicação ou citação. <strong>Travessão</strong>: marca a fala de personagem ou destaca uma expressão, como se fosse uma vírgula mais forte.'), "Outros sinais"))

treino(5, [
 ("Em “Vou à feira”, há crase porque “ir” exige a preposição “a” e “feira” aceita o artigo “a”.","C","Teste: vou ao mercado."),
 ("Usa-se crase em “Começou à estudar”.","E","Antes de verbo não há crase."),
 ("Na indicação de horas, como em “às 10h”, a crase é obrigatória.","C","Locução adverbial de tempo."),
 ("A crase antes de nome próprio feminino de pessoa é facultativa.","C","“à Maria” ou “a Maria”."),
 ("Na frase “O candidato aprovado, comemorou o resultado”, a vírgula está correta.","E","Não se separa o sujeito do verbo."),
 ("O vocativo deve ser isolado por vírgula.","C","“Candidatos, atenção!”")])

# ================================================================ UNIDADE 6
opener("06","UNIDADE 6","Ortografia e acentuação",["Ortografia: dúvidas frequentes","Acentuação gráfica"],"U6")

add(H(6,'Ortografia: dúvidas <span class="hl">frequentes</span>','Palavras parecidas, sentidos diferentes.', "A16") +
 table(["Forma","Quando usar","Exemplo"],[
  ["por que","Pergunta, ou quando equivale a “pelo qual” ou “por qual motivo”","<b>Por que</b> você faltou? Não sei <b>por que</b> faltou."],
  ["por quê","No fim da frase (antes de pontuação)","Você faltou <b>por quê</b>?"],
  ["porque","Resposta, explicação ou causa","Faltei <b>porque</b> estava doente."],
  ["porquê","Substantivo (vem com artigo): “o motivo”","Explique o <b>porquê</b> da falta."],
  ["mal · mau","Mal: oposto de bem · mau: oposto de bom","Dormiu <b>mal</b>. É um <b>mau</b> exemplo."],
  ["há · a","Há: tempo passado (= faz) · a: tempo futuro ou distância","Mudou-se <b>há</b> dois anos. Daqui <b>a</b> dois dias. Fica <b>a</b> 3 km."],
  ["onde · aonde","Onde: lugar em que se está · aonde: lugar a que se vai (verbos de movimento)","<b>Onde</b> você mora? <b>Aonde</b> você vai?"],
  ["senão · se não","Senão: caso contrário, mas sim · se não: caso não","Estude, <b>senão</b> não passará. <b>Se não</b> estudar, não passará."],
  ["a fim de · afim","A fim de: finalidade · afim: semelhante, com afinidade","Estudou <b>a fim de</b> passar. Áreas <b>afins</b>."],
  ["mas · mais","Mas: oposição · mais: quantidade","Quis ir, <b>mas</b> choveu. Quero <b>mais</b> tempo."]],["16%","42%",None]) +
 memo('Teste rápido: <strong>mal</strong> ↔ bem; <strong>mau</strong> ↔ bom. <strong>Há</strong> dois anos = <strong>faz</strong> dois anos. No fim da frase, <strong>por quê</strong> leva acento.'))

add(H(6,'Acentuação <span class="hl">gráfica</span>','Três regras de base e as novidades do Acordo.', "A17") +
 acento_fluxo() +
 table(["Regra complementar","Exemplos"],[
  ["Monossílabos tônicos terminados em a(s), e(s), o(s)","pá, pé, pó, mês, nós"],
  ["Hiato com i ou u tônicos, sozinhos na sílaba ou com s","saída, baú, país, juízes"],
  ["Acento diferencial que continua","pôr (verbo) x por (preposição); pôde (passado) x pode (presente); têm e vêm (plural) x tem e vem (singular)"]],["44%",None]) +
 table(["O que mudou com o Acordo Ortográfico","Antes","Agora"],[
  ["Ditongos abertos éi e ói em paroxítonas perderam o acento","idéia, assembléia, heróico","ideia, assembleia, heroico (mas herói e papéis, oxítonas, mantêm)"],
  ["Hiatos “ee” e “oo” perderam o acento","crêem, lêem, vêem, vôo","creem, leem, veem, voo"],
  ["Trema foi abolido (exceto em nomes estrangeiros)","freqüente, lingüiça","frequente, linguiça"],
  ["Alguns acentos diferenciais caíram","pára (verbo), pêlo","para, pelo"]],["40%","24%",None]))

treino(6, [
 ("Em “Não sei por que ele faltou”, a grafia “por que” está correta.","C","Equivale a “por qual motivo”."),
 ("Na frase “Ele é um mal exemplo”, a grafia está correta.","E","Oposto de bom: “mau exemplo”."),
 ("Em “Mudou-se a dois anos”, o correto seria “há dois anos”.","C","Tempo passado = há (faz)."),
 ("Todas as palavras proparoxítonas são acentuadas.","C","Lâmpada, público, árvore."),
 ("Após o Acordo Ortográfico, a palavra “ideia” continua com acento agudo.","E","Paroxítona com ditongo aberto “ei” perdeu o acento."),
 ("A forma verbal “pôr” mantém o acento diferencial em relação à preposição “por”.","C","Acento diferencial mantido.")])

# ================================================================ REVISÃO
mapa(("LÍNGUA","PORTU-","GUESA"), [
  ("INTERPRETAÇÃO",["compreender x interpretar","apoio no texto","cuidado com absolutos"],C['navy'],NV),
  ("CLASSES",["advérbio não varia","cujo sem artigo","mas x embora"],C['blue'],C['sky']),
  ("SINTAXE",["pergunte ao verbo","haver = sem sujeito","restritiva x explicativa"],C['green'],C['greensoft']),
  ("CONCORDÂNCIA E REGÊNCIA",["vendem-se casas","precisa-se de","assistir ao jogo"],C['golddeep'],C['goldsoft']),
  ("CRASE E VÍRGULA",["a + a = à","troque pelo masculino","sujeito, verbo: sem vírgula"],C['red'],C['redsoft']),
  ("ORTOGRAFIA",["porquês","mal x mau · há x a","ideia sem acento"],C['navy'],NV)], "Mapa conceitual do Caderno 17.", "O português da prova em seis blocos. Explique cada caixa em voz alta.", center_color="#c9a6ff")

erros([
  ["“Interpretar é concluir o que eu acho.”","A conclusão precisa de apoio no texto."],
  ["“Elas estavam meias cansadas.”","Meio (advérbio) não varia: meio cansadas."],
  ["“O servidor cujo o processo…”","Cujo não admite artigo: cujo processo."],
  ["“Haviam muitos candidatos.”","Havia: haver (existir) é impessoal."],
  ["“Precisam-se de vigilantes.”","Precisa-se de: com preposição, singular."],
  ["“Prefiro mais isso do que aquilo.”","Prefiro isso a aquilo."],
  ["“Assisti o jogo.” (ver)","Assisti ao jogo, na norma-padrão."]],
 [["“Começou à estudar.”","Antes de verbo, não há crase."],
  ["“Andar à pé.”","Antes de masculino, não há crase."],
  ["“O candidato aprovado, comemorou.”","Não se separa sujeito e verbo com vírgula."],
  ["“Ele é um mal exemplo.”","Mau (oposto de bom)."],
  ["“Mudou-se a dois anos.”","Há dois anos (tempo passado)."],
  ["“Você faltou por que?”","No fim da frase: por quê."],
  ["“Idéia, assembléia, vôo.”","Ideia, assembleia, voo (Acordo Ortográfico)."]])

flashcards([("INTERPRETAÇÃO","Compreensão x interpretação?","O que está escrito x o que se pode concluir com apoio no texto."),
 ("INTERPRETAÇÃO","Extrapolação?","Ir além do que o texto autoriza."),
 ("TIPOS","Tipo predominante em manuais e editais?","Injuntivo (instrucional)."),
 ("CLASSES","Advérbio varia?","Não: “meio cansada”, “estudaram bastante”."),
 ("CLASSES","Este x esse?","Este: perto de quem fala ou o que vem. Esse: perto de quem ouve ou o que já foi dito."),
 ("CLASSES","Cujo admite artigo depois?","Não: “cujo processo”."),
 ("CLASSES","Mas x embora?","Ambos contrastam; “embora” pede subjuntivo."),
 ("SINTAXE","Como achar o sujeito?","Pergunte ao verbo “quem?” ou “o quê?”."),
 ("SINTAXE","Orações sem sujeito?","Haver (existir), fazer (tempo), fenômenos da natureza."),
 ("SINTAXE","Predicado nominal?","Verbo de ligação + predicativo."),
 ("SINTAXE","Adjetiva restritiva x explicativa?","Sem vírgula, restringe x entre vírgulas, generaliza."),
 ("CONCORDÂNCIA","Haver (existir) no plural?","Não: “havia problemas”, “deve haver soluções”."),
 ("CONCORDÂNCIA","Vende-se ou vendem-se casas?","Vendem-se (casas são vendidas)."),
 ("CONCORDÂNCIA","Precisa-se ou precisam-se de?","Precisa-se de (singular)."),
 ("CONCORDÂNCIA","É proibido entrada x a entrada?","Sem artigo: proibido. Com artigo: proibida a entrada."),
 ("REGÊNCIA","Assistir (ver)?","VTI: assistir ao jogo."),
 ("REGÊNCIA","Preferir?","Preferir uma coisa a outra."),
 ("CRASE","Fórmula da crase?","Preposição a + artigo a = à."),
 ("CRASE","Teste da crase?","Trocar por masculino: se aparece “ao”, há crase."),
 ("CRASE","Crase antes de verbo ou masculino?","Nunca (salvo “à moda de”)."),
 ("VÍRGULA","Separa sujeito e verbo?","Nunca."),
 ("ORTOGRAFIA","Por quê com acento?","No fim da frase."),
 ("ORTOGRAFIA","Há x a (tempo)?","Há: passado. A: futuro ou distância."),
 ("ACENTUAÇÃO","Proparoxítonas?","Todas acentuadas.")])

Q = [
 ("Interpretação","No texto autoral “A praça que voltou a ter gente”, a expressão “não veio apenas das obras” indica que:",
  ["as obras não tiveram nenhuma influência na mudança.","a mudança teve outras causas além das obras.","a feira foi a única causa da mudança.","os moradores rejeitaram a reforma.","a Guarda Municipal deixou de atuar na praça."],"B",
  "“Não… apenas” admite as obras como causa, mas acrescenta outras (feira, escola). Dizer que não tiveram influência contradiz o texto; dizer que a feira foi a única é redução.","Não apenas = também outras."),
 ("Interpretação","Em uma questão de interpretação, a alternativa que afirma algo que vai além do que o texto permite concluir apresenta um erro de:",
  ["redução.","extrapolação.","coesão.","concordância.","regência."],"B",
  "Extrapolação é ir além; redução é tomar a parte pelo todo; contradição é dizer o oposto.","Extrapolar = passar do limite."),
 ("Tipos textuais","O texto que orienta o leitor a agir, com verbos no imperativo e etapas, como um manual, é predominantemente:",
  ["narrativo.","descritivo.","injuntivo.","dissertativo-argumentativo.","expositivo."],"C",
  "O tipo injuntivo (instrucional) orienta comportamentos: manuais, receitas, editais.","Injuntivo = instrução."),
 ("Classes","Na frase “Ela ficou meio preocupada com a prova”, a palavra “meio” é:",
  ["numeral e deve concordar com “preocupada”.","advérbio e, portanto, invariável.","adjetivo e deve ir para o feminino.","substantivo.","preposição."],"B",
  "“Meio” significa “um pouco”, modifica o adjetivo e é advérbio, logo invariável. Como numeral (metade), varia: meia hora.","Advérbio não varia."),
 ("Pronomes","Assinale a frase de acordo com a norma-padrão:",
  ["O candidato cujo o recurso foi aceito comemorou.","O candidato cujo recurso foi aceito comemorou.","O candidato que o recurso foi aceito comemorou.","O candidato onde o recurso foi aceito comemorou.","O candidato cujo do recurso foi aceito comemorou."],"B",
  "“Cujo” indica posse e não admite artigo depois. “Onde” só se usa para lugar.","Cujo + substantivo, sem artigo."),
 ("Conjunções","Na frase “O treinamento foi longo; os guardas, porém, mantiveram a concentração”, a conjunção “porém” pode ser substituída, sem alteração de sentido, por:",
  ["portanto.","contudo.","porque.","logo.","conforme."],"B",
  "“Porém” e “contudo” são adversativas (oposição). Portanto e logo são conclusivas; porque é causal; conforme é conformativa.","Porém = contudo = todavia."),
 ("Sujeito","Em qual das frases o sujeito é indeterminado?",
  ["Os guardas chegaram cedo.","Choveu durante a madrugada.","Precisa-se de agentes de trânsito.","Há vagas no estacionamento.","Chegamos ao posto."],"C",
  "Verbo transitivo indireto + se: sujeito indeterminado. “Choveu” e “há” formam orações sem sujeito; “chegamos” tem sujeito oculto.","VTI + se = indeterminado."),
 ("Sujeito","Na frase “Faltaram dois candidatos à prova”, o sujeito é:",
  ["oculto.","inexistente.","“dois candidatos”.","“à prova”.","indeterminado."],"C",
  "O sujeito está depois do verbo: o que faltou? Dois candidatos. Por isso o verbo está no plural.","Sujeito pode vir depois do verbo."),
 ("Predicado","Em “A equipe permaneceu atenta durante o evento”, o predicado é:",
  ["verbal.","nominal.","verbo-nominal.","inexistente.","indeterminado."],"B",
  "“Permanecer” é verbo de ligação e “atenta” é predicativo do sujeito: predicado nominal.","Verbo de ligação + predicativo = nominal."),
 ("Orações","Compare: (I) “Os candidatos que estudaram foram aprovados.” (II) “Os candidatos, que estudaram, foram aprovados.” É correto afirmar:",
  ["as duas frases têm o mesmo sentido.","em I, todos os candidatos estudaram; em II, só alguns.","em I, apenas os que estudaram foram aprovados; em II, todos estudaram e foram aprovados.","a frase II está errada.","a frase I está errada."],"C",
  "Sem vírgulas, a oração adjetiva é restritiva (só uma parte); entre vírgulas, é explicativa (todo o grupo).","Vírgula muda o sentido."),
 ("Concordância verbal","Assinale a frase correta quanto à concordância verbal:",
  ["Haviam muitas pessoas na praça.","Devem haver soluções para o problema.","Havia muitas pessoas na praça.","Fazem dez anos que a praça foi reformada.","Existia muitos problemas no bairro."],"C",
  "Haver (existir) e fazer (tempo) são impessoais: singular, inclusive o auxiliar (“deve haver”). “Existir” é pessoal: “existiam muitos problemas”.","Haver = existir: singular."),
 ("Concordância verbal","Assinale a frase correta:",
  ["Aluga-se salas comerciais.","Precisam-se de vigilantes.","Alugam-se salas comerciais.","Trata-se de questões difíceis e precisam-se de calma.","Vende-se apartamentos."],"C",
  "“Salas são alugadas”: sujeito paciente no plural, verbo no plural. Com preposição (precisar de, tratar de), o verbo fica no singular.","Se + VTD: concorda; se + VTI: singular."),
 ("Concordância nominal","Assinale a frase correta quanto à concordância nominal:",
  ["Seguem anexo as fotografias.","É proibida entrada de pessoas estranhas.","Havia menas pessoas na fila.","Ela mesma redigiu o relatório.","Elas estavam meias nervosas."],"D",
  "“Mesmo” concorda: ela mesma. Corrigindo as demais: anexas as fotografias; é proibido entrada (sem artigo); menos pessoas; meio nervosas.","Mesmo, anexo, obrigado variam."),
 ("Regência","Assinale a frase de acordo com a regência da norma-padrão:",
  ["Assistimos o filme ontem.","Ele aspira o cargo de inspetor.","Os condutores devem obedecer às normas de trânsito.","Prefiro mais caminhar do que correr.","Cheguei no posto às 7h."],"C",
  "Obedecer é VTI (a) + artigo = às. Corrigindo: assistimos ao filme; aspira ao cargo; prefiro caminhar a correr; cheguei ao posto.","Obedecer a."),
 ("Regência","No sentido de “ajudar, prestar assistência”, o verbo “assistir” é:",
  ["intransitivo.","transitivo direto: “O enfermeiro assistiu o ferido”.","transitivo indireto obrigatório: “assistiu ao ferido”.","de ligação.","sempre pronominal."],"B",
  "Assistir = ajudar: VTD. Assistir = ver: VTI (a).","Assistir: ver ao jogo, ajudar o ferido."),
 ("Crase","Assinale a alternativa em que o acento indicativo de crase está correto:",
  ["Começou à chover forte.","Fomos à pé até o posto.","Entreguei o relatório à ela.","O plantão começa às 19h.","Ficamos frente à frente."],"D",
  "Horas pedem crase. Não há crase antes de verbo (a chover), masculino (a pé), pronome pessoal (a ela) nem entre palavras repetidas (frente a frente).","Horas: às."),
 ("Crase","Em “Refiro-me ___ norma que entrou em vigor e não ___ que foi revogada”, as lacunas são preenchidas por:",
  ["a · aquela.","à · àquela.","a · àquela.","à · aquela.","há · àquela."],"B",
  "“Referir-se a” + artigo “a” (norma) = à. “Referir-se a” + “aquela” = àquela.","a + aquela = àquela."),
 ("Crase","A crase é facultativa em:",
  ["Vou à escola.","Refiro-me à minha irmã.","Chegou às 8h.","Saiu às pressas.","Obedeça à lei."],"B",
  "Antes de pronome possessivo feminino no singular, a crase é facultativa. Nas demais, é obrigatória.","Possessivo feminino: facultativa."),
 ("Pontuação","Assinale a frase pontuada corretamente:",
  ["Os moradores do bairro, aprovaram a reforma.","A prefeitura reformou, a praça.","Durante a madrugada, a equipe permaneceu no local.","O guarda, entregou o documento ao motorista.","Os candidatos que, estudaram foram aprovados."],"C",
  "O adjunto adverbial deslocado pode ser isolado por vírgula. Nas demais, a vírgula separa sujeito e verbo, verbo e complemento ou corta a oração indevidamente.","Sujeito, verbo: nunca."),
 ("Pontuação","Em “Senhores candidatos, a prova começará em instantes”, a vírgula isola:",
  ["o aposto.","o vocativo.","o sujeito.","o objeto direto.","o adjunto adnominal."],"B",
  "“Senhores candidatos” é um chamamento: vocativo, sempre isolado por vírgula.","Chamamento = vocativo."),
 ("Ortografia","Assinale a frase correta quanto ao uso dos porquês:",
  ["Não sei porque ele faltou.","Ele faltou por quê estava doente.","Por que você não veio?","Explique o por que da decisão.","Você não veio porquê?"],"C",
  "Pergunta no início: por que. Correções: não sei por que; faltou porque estava doente; o porquê da decisão; não veio por quê?","Pergunta: por que · fim: por quê."),
 ("Ortografia","Assinale a frase correta:",
  ["Ele é um mal motorista.","A viatura chegou a dez minutos.","Daqui há dois dias será a prova.","O agente agiu mal ao não sinalizar.","Aonde você está agora?"],"D",
  "Mal é oposto de bem (agiu mal). Correções: mau motorista; chegou há dez minutos; daqui a dois dias; onde você está (sem movimento).","Mal x bem; mau x bom."),
 ("Acentuação","Assinale a alternativa em que todas as palavras estão grafadas de acordo com o Acordo Ortográfico vigente:",
  ["idéia, vôo, freqüente.","ideia, voo, frequente.","idéia, voo, frequente.","ideia, vôo, freqüente.","ideía, voô, frequênte."],"B",
  "O Acordo retirou o acento dos ditongos abertos ei/oi em paroxítonas (ideia), dos hiatos oo/ee (voo, leem) e aboliu o trema (frequente).","Ideia, voo, frequente."),
 ("Acentuação","São acentuadas pela mesma regra as palavras:",
  ["café e lâmpada.","fácil e açúcar.","sofá e táxi.","pé e público.","herói e hífen."],"B",
  "Fácil (termina em l) e açúcar (termina em r) são paroxítonas acentuadas pela terminação. Café e sofá são oxítonas; lâmpada e público, proparoxítonas.","Paroxítona em l, n, r, x…")]
questoes(Q, "BACDEBCAEDBCADEBACDEBCEA")
respostas_treinos()

referencias('''<h3>Base normativa</h3><ul>
<li>Norma-padrão do português brasileiro, conforme as gramáticas normativas de referência.</li>
<li>Acordo Ortográfico da Língua Portuguesa de 1990, promulgado no Brasil pelo Decreto nº 6.583/2008, com uso obrigatório desde 1º de janeiro de 2016 (Decreto nº 7.875/2012).</li>
<li>Vocabulário Ortográfico da Língua Portuguesa (VOLP), da Academia Brasileira de Letras, para consulta de grafias.</li></ul>
<h3>Textos e questões</h3><ul><li>O texto “A praça que voltou a ter gente” e todas as frases de exemplo foram escritos para este caderno.</li></ul>''',
 '<strong>Limitações:</strong> a gramática normativa admite, em alguns pontos, mais de uma forma (concordância com sujeito composto posposto, crase facultativa, regências que dicionários modernos já aceitam, como “visar” transitivo direto no sentido de pretender e “implicar em”); o caderno indica a forma tradicional, mais segura em provas, e avisa quando há variação. Bancas podem adotar posições de autores específicos. Confira o edital do seu concurso.', DATA)
encerramento("17", "Língua Portuguesa", 'Sugestão de continuação: <strong>Caderno 18 · Raciocínio Lógico</strong>.')
gravar(HERE, "Mapa da Aprovação — Caderno 17 — Língua Portuguesa", Q)
