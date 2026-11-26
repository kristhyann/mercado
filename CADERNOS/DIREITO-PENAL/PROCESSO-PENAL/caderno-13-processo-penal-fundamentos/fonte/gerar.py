"""Gera miolo.html do Caderno 13: Direito Processual Penal — Fundamentos e Principais Institutos. Uso: python3 gerar.py
Base legal conferida no portal do Planalto em 26/11/2026: Código de Processo Penal (Decreto-Lei nº 3.689/1941) e CF/88."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit
from kit import *

DATA = "26 de novembro de 2026"
kit.U = {1:("UNIDADE 1","Noções gerais"),2:("UNIDADE 2","Investigação e inquérito"),3:("UNIDADE 3","Ação penal"),4:("UNIDADE 4","Provas"),5:("UNIDADE 5","Sujeitos e procedimentos")}
def cpp(x): return f"{x} · Código de Processo Penal"
def cf(x): return f"{x} · Constituição Federal"

# ================================================================ APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">O caminho que vai do crime à sentença: quem investiga, quem acusa, como se prova e como o processo anda.</p>
<p>Este é o <strong>Caderno 13 da coleção</strong>, dedicado ao <strong>Direito Processual Penal</strong>. Se o Direito Penal (Cadernos 05 a 08) diz <strong>o que é crime</strong> e qual é a pena, o Processo Penal diz <strong>como o Estado apura o crime</strong> e aplica a pena, respeitando as garantias de quem é investigado ou acusado.</p>
<p>Para quem estuda para <strong>Guarda Municipal e polícias</strong>, os pontos mais importantes são o <strong>inquérito policial</strong>, a <strong>prisão em flagrante</strong>, a <strong>preservação do local do crime</strong> e a <strong>cadeia de custódia</strong> dos vestígios, porque fazem parte do trabalho de quem chega primeiro a uma ocorrência.</p>
{table(["Recurso","Onde está"],[["Linha do tempo da persecução penal","Unidade 1"],["Sistemas processuais (comparação)","Unidade 1"],["Características do inquérito e prazos","Unidade 2"],["Diagrama das espécies de ação penal","Unidade 3"],["As 10 etapas da cadeia de custódia","Unidade 4"],["Flagrante, audiência de custódia e fluxo do procedimento comum","Unidade 5"],["Mapa conceitual, erros mais comuns e 24 questões autorais","Revisão e prática"]],["58%",None])}
{lembre(p(f'O Código de Processo Penal e a Constituição foram conferidos no portal do Planalto em <strong>{DATA}</strong>. O CPP mudou bastante desde 2019 (Lei nº 13.964/2019, o “Pacote Anticrime”) e teve alterações em <strong>2025 e 2026</strong> (Leis nº 15.272/2025, 15.358/2026 e 15.438/2026, entre outras), que estão incorporadas aqui.'), "Fontes e atualização")}''', first=True)

toc_page([("u","UNIDADE 1 · NOÇÕES GERAIS","U1"),("","1. Conceito e finalidade do processo penal","A01"),("","2. Princípios","A02"),("","3. Sistemas processuais","A03"),
 ("u","UNIDADE 2 · INVESTIGAÇÃO E INQUÉRITO POLICIAL","U2"),("","4. Investigação criminal e polícia judiciária","A04"),("","5. Inquérito policial: conceito e instauração","A05"),("","6. Características do inquérito","A06"),("","7. Prazos, conclusão e arquivamento","A07"),
 ("u","UNIDADE 3 · AÇÃO PENAL","U3"),("","8. Espécies de ação penal (diagrama)","A08"),("","9. Ação penal pública","A09"),("","10. Ação penal privada","A10"),("","11. Pública x privada: princípios e prazos","A11"),
 ("u","UNIDADE 4 · PROVAS","U4"),("","12. Noções gerais de prova","A12"),("","13. Provas ilícitas","A13"),("","14. Principais meios de prova","A14"),("","15. Cadeia de custódia","A15"),
 ("u","UNIDADE 5 · SUJEITOS E PROCEDIMENTOS","U5"),("","16. Sujeitos do processo","A16"),("","17. Prisão em flagrante e audiência de custódia","A17"),("","18. Procedimentos: noções introdutórias","A18"),
 ("u","REVISÃO E PRÁTICA","RV"),("","Mapa conceitual · Erros mais comuns","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),("","Gabarito, respostas dos treinos e referências","R4")])

# ================================================================ UNIDADE 1
opener("01","UNIDADE 1","Noções gerais",["Conceito e finalidade","Princípios","Sistemas processuais"],"U1")

def persecucao():
    N,O,R=C['navy'],C['golddeep'],C['red']
    it=[("CRIME","fato","",N,NV),("INVESTIGAÇÃO","inquérito","(polícia)",O,C['goldsoft']),("AÇÃO PENAL","denúncia ou","queixa",C['blue'],C['sky']),("INSTRUÇÃO","provas em","contraditório",N,NV),("SENTENÇA","condena ou","absolve",R,C['redsoft'])]
    s = f'<figure><svg viewBox="0 0 640 170" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">{arrowdefs("pp")}'
    s += f'<rect x="120" y="4" width="120" height="22" rx="6" fill="{C["goldsoft"]}"/><text x="180" y="19" text-anchor="middle" font-size="10" font-weight="900" fill="{O}">FASE PRÉ-PROCESSUAL</text>'
    s += f'<rect x="250" y="4" width="380" height="22" rx="6" fill="{C["sky"]}"/><text x="440" y="19" text-anchor="middle" font-size="10" font-weight="900" fill="{C["blue"]}">FASE PROCESSUAL (processo penal propriamente dito)</text>'
    for k,(t,a,b,fg,bg) in enumerate(it):
        x=4+k*127
        s += f'<rect x="{x}" y="36" width="112" height="84" rx="12" fill="{bg}" stroke="{fg}" stroke-width="2.4"/><text x="{x+56}" y="66" text-anchor="middle" font-size="11.5" font-weight="900" fill="{fg}">{t}</text><text x="{x+56}" y="86" text-anchor="middle" font-size="9.8" fill="{C["ink"]}">{a}</text><text x="{x+56}" y="101" text-anchor="middle" font-size="9.8" fill="{C["ink"]}">{b}</text>'
        if k<4: s += f'<line x1="{x+114}" y1="78" x2="{x+125}" y2="78" stroke="{C["ink"]}" stroke-width="2.4" marker-end="url(#pp)"/>'
    s += f'<text x="320" y="146" text-anchor="middle" font-size="10.5" font-weight="800" fill="{N}">Persecução penal = investigação + ação penal. O inquérito informa; as provas são produzidas em juízo.</text>'
    return s + '</svg><figcaption>Linha do tempo da persecução penal.</figcaption></figure>'

add(H(1,'Conceito e <span class="hl">finalidade</span>','O instrumento para apurar crimes com garantias.', "A01") +
 oque(p('<strong>Direito Processual Penal</strong> é o conjunto de normas e princípios que regulam a <strong>persecução penal</strong>: a investigação dos crimes, a ação penal, a produção das provas, o julgamento e os recursos. Sua finalidade é permitir a aplicação da lei penal, <strong>protegendo as garantias</strong> do investigado e do acusado.')) +
 persecucao() +
 traduz(p('O Estado não pode simplesmente prender e punir quem ele acha que cometeu um crime. Existe um <strong>caminho obrigatório</strong>: investigar, acusar formalmente, dar ao acusado a chance de se defender, produzir provas perante um juiz e só então decidir. Esse caminho é o processo penal, e ele serve a <strong>dois objetivos</strong> ao mesmo tempo: punir quem cometeu crime e <strong>proteger o inocente</strong> de uma punição injusta.')) +
 memo('Persecução penal = <strong>investigação</strong> (pré-processual) + <strong>ação penal</strong> e <strong>processo</strong>. Finalidade dupla: <strong>aplicar a lei penal</strong> e <strong>garantir direitos</strong>.'))

add(H(1,'<span class="hl">Princípios</span>','As garantias que orientam todo o processo.', "A02") +
 table(["Princípio","O que garante","Base"],[
  ["Devido processo legal","Ninguém será privado da liberdade ou de seus bens sem o devido processo legal","CF, art. 5º, LIV"],
  ["Contraditório e ampla defesa","Ser informado das acusações, reagir a elas e usar todos os meios de defesa","CF, art. 5º, LV"],
  ["Presunção de inocência (não culpabilidade)","Ninguém será considerado culpado até o trânsito em julgado da sentença penal condenatória","CF, art. 5º, LVII"],
  ["Juiz natural","Julgamento por juiz previamente competente; proibidos tribunais de exceção","CF, art. 5º, XXXVII e LIII"],
  ["Inadmissibilidade das provas ilícitas","Provas obtidas por meios ilícitos não podem ser usadas","CF, art. 5º, LVI; CPP, art. 157"],
  ["Não autoincriminação (<i>nemo tenetur se detegere</i>)","Direito de permanecer calado e de não produzir prova contra si","CF, art. 5º, LXIII; Pacto de São José, art. 8.2, g"],
  ["Publicidade","Atos públicos, salvo quando a defesa da intimidade ou o interesse social exigirem sigilo","CF, art. 5º, LX, e art. 93, IX"],
  ["Duração razoável do processo","Processo sem demoras injustificadas","CF, art. 5º, LXXVIII"],
  ["<i>In dubio pro reo</i>","Na dúvida, decide-se a favor do réu","Doutrina e jurisprudência"]],["26%",None,"22%"]) +
 memo('<strong>Presunção de inocência</strong>: culpado só após o <strong>trânsito em julgado</strong>. <strong>Silêncio</strong> não pode ser usado contra o acusado. Na <strong>dúvida</strong>, absolve-se.'))

add(H(1,'Sistemas <span class="hl">processuais</span>','Quem acusa, quem defende e quem julga.', "A03") +
 scene3([("INQUISITIVO",C['red'],C['redsoft'],"prof",["O mesmo juiz","investiga, acusa","e julga."],"funções concentradas"),
  ("ACUSATÓRIO",C['green'],C['greensoft'],"profa",["MP acusa, defesa","defende, juiz","julga, imparcial."],"funções separadas"),
  ("MISTO",C['golddeep'],C['goldsoft'],"prof",["Fase inquisitiva +","fase acusatória","em juízo."],"modelo francês")], "Situação ilustrada: os três sistemas processuais.") +
 lei(cpp("Art. 3º-A (Lei nº 13.964/2019)"),'<p>O processo penal terá "estrutura acusatória, vedadas a iniciativa do juiz na fase de investigação" e a substituição da atuação probatória do órgão de acusação.</p>') +
 table(["","INQUISITIVO","ACUSATÓRIO"],[
  ["Funções","Concentradas em uma só pessoa","Separadas: acusar, defender e julgar"],
  ["Acusado","Objeto da investigação","Sujeito de direitos"],
  ["Processo","Sigiloso, escrito, sem contraditório","Público, oral, com contraditório"],
  ["No Brasil","—","<b>Adotado</b> pela Constituição (o MP é titular da ação penal pública, art. 129, I) e expressamente pelo CPP (art. 3º-A)"]],["16%",None,None]) +
 lembre(p('A Lei nº 13.964/2019 criou o <strong>juiz das garantias</strong> (arts. 3º-B a 3º-F do CPP), responsável pelo controle da legalidade da investigação, com atuação até o recebimento da denúncia, exceto nas infrações de menor potencial ofensivo. Esses artigos foram questionados no STF (ADIs 6.298, 6.299, 6.300 e 6.305), que, em 2023, validou o instituto com ajustes e interpretações. O inquérito policial, por sua vez, tem natureza <strong>inquisitiva</strong>.'), "Juiz das garantias"))

treino(1, [
 ("A persecução penal compreende a investigação e a ação penal.","C","Fase pré-processual e fase processual."),
 ("Pelo princípio da presunção de inocência, ninguém será considerado culpado até o trânsito em julgado de sentença penal condenatória.","C","CF, art. 5º, LVII."),
 ("O silêncio do acusado pode ser interpretado em prejuízo da defesa.","E","Direito de permanecer calado (CF, art. 5º, LXIII)."),
 ("O CPP prevê expressamente que o processo penal terá estrutura acusatória.","C","Art. 3º-A."),
 ("No sistema inquisitivo, as funções de acusar, defender e julgar ficam separadas.","E","Isso é o acusatório; no inquisitivo, elas se concentram."),
 ("As provas obtidas por meios ilícitos são admissíveis no processo, se relevantes.","E","São inadmissíveis (CF, art. 5º, LVI; CPP, art. 157).")])

# ================================================================ UNIDADE 2
opener("02","UNIDADE 2","Investigação e inquérito policial",["Investigação criminal","Inquérito: conceito e instauração","Características","Prazos, conclusão e arquivamento"],"U2")

add(H(2,'Investigação criminal e <span class="hl">polícia judiciária</span>','Quem apura a infração e a autoria.', "A04") +
 lei(cpp("Art. 4º, caput (trecho)"),'<p>A polícia judiciária será exercida pelas autoridades policiais no território de suas respectivas circunscrições "e terá por fim a apuração das infrações penais e da sua autoria".</p>') +
 table(["Quem investiga","Fundamento"],[
  ["Polícia Federal (crimes contra bens, serviços e interesses da União, entre outros)","CF, art. 144, § 1º"],
  ["Polícias Civis (funções de polícia judiciária e apuração de infrações penais, exceto as militares)","CF, art. 144, § 4º"],
  ["Ministério Público (investigação própria)","Reconhecida pelo STF (RE 593.727, Tema 184, 2015), com respeito aos direitos do investigado"],
  ["Outras autoridades administrativas com a mesma função, por lei","CPP, art. 4º, parágrafo único (ex.: CPIs, investigações administrativas)"]],["60%",None]) +
 traduz(p('A <strong>polícia judiciária</strong> (Polícia Civil e Polícia Federal) investiga crimes já ocorridos para que o Ministério Público possa acusar. Isso é diferente da <strong>polícia ostensiva e preventiva</strong> (Polícia Militar) e da atuação das <strong>guardas municipais</strong>, que, segundo o STF (Tema 656, 2025), podem fazer policiamento urbano ostensivo e comunitário, mas <strong>não</strong> exercem polícia judiciária. Qualquer pessoa, porém, pode prender quem esteja em flagrante (CPP, art. 301).'),"profa") +
 memo('Polícia judiciária = <strong>Polícia Civil</strong> e <strong>Polícia Federal</strong>: apura <strong>infração e autoria</strong>. O MP também pode investigar (STF). Guardas municipais <strong>não</strong> fazem polícia judiciária.'))

add(H(2,'Inquérito policial: <span class="hl">conceito e instauração</span>','Procedimento administrativo para reunir elementos sobre o crime.', "A05") +
 oque(p('O <strong>inquérito policial</strong> é um <strong>procedimento administrativo</strong>, presidido pelo <strong>delegado de polícia</strong>, que reúne <strong>elementos informativos</strong> sobre a <strong>materialidade</strong> (existência do crime) e a <strong>autoria</strong>, para formar a convicção do titular da ação penal (o MP ou o ofendido).')) +
 table(["Crime de ação penal...","Como o inquérito começa (CPP, art. 5º)"],[
  ["Pública <b>incondicionada</b>","<b>De ofício</b> pela autoridade policial (portaria ou auto de prisão em flagrante); por <b>requisição</b> do juiz ou do Ministério Público; ou por <b>requerimento</b> do ofendido"],
  ["Pública <b>condicionada</b>","Só com a <b>representação</b> do ofendido (ou requisição do Ministro da Justiça, quando a lei exigir): sem ela, o inquérito <b>não pode ser iniciado</b> (§ 4º)"],
  ["<b>Privada</b>","Só a <b>requerimento</b> de quem tenha qualidade para propor a ação (§ 5º)"]],["30%",None]) +
 table(["Providências da autoridade policial (art. 6º, exemplos)",""],[
  ["Dirigir-se ao local e providenciar que não se alterem o estado e a conservação das coisas até a chegada dos peritos","Apreender os objetos que tiverem relação com o fato, após liberados pelos peritos"],
  ["Ouvir o ofendido e o indiciado","Proceder a reconhecimento de pessoas e coisas e a acareações"],
  ["Determinar o exame de corpo de delito e outras perícias","Ordenar a identificação do indiciado e juntar a folha de antecedentes"]],["50%",None]) +
 memo('Inquérito: <strong>procedimento administrativo</strong>, presidido pelo <strong>delegado</strong>, sobre <strong>materialidade e autoria</strong>. Qualquer pessoa do povo pode comunicar um crime à polícia (art. 5º, § 3º).'))

add(H(2,'Características do <span class="hl">inquérito</span>','As palavras que a prova cobra.', "A06") +
 table(["Característica","Explicação","Base"],[
  ["Escrito","Todas as peças são reduzidas a escrito em um só processado","CPP, art. 9º"],
  ["Sigiloso","A autoridade assegura o sigilo necessário à elucidação do fato ou exigido pelo interesse da sociedade; o defensor, porém, tem acesso aos elementos já documentados (Súmula Vinculante 14)","CPP, art. 20"],
  ["Inquisitivo","Não há contraditório e ampla defesa plenos: é uma investigação, e não um processo","Doutrina"],
  ["Dispensável","Se o MP já tiver elementos suficientes, pode oferecer denúncia sem inquérito","CPP, arts. 12 e 39, § 5º"],
  ["Indisponível","A autoridade policial <b>não pode mandar arquivar</b> o inquérito","CPP, art. 17"],
  ["Oficial e oficioso","Conduzido por órgão oficial e, nos crimes de ação pública incondicionada, instaurado de ofício","CPP, arts. 4º e 5º"],
  ["Discricionário (na condução)","O delegado escolhe as diligências mais adequadas ao caso","Doutrina"]],["18%",None,"20%"]) +
 lei(cpp("Art. 17"),'<p>Art. 17. A autoridade policial não poderá mandar arquivar autos de inquérito.</p>') +
 memo('Inquérito: <strong>escrito, sigiloso, inquisitivo, dispensável, indisponível</strong> e <strong>oficial</strong>. Memória: <strong>“ESIDIO”</strong>. Delegado <strong>não</strong> arquiva.'))

add(H(2,'Prazos, conclusão e <span class="hl">arquivamento</span>','Quanto tempo dura e como termina.', "A07") +
 table(["Situação","Prazo para concluir o inquérito (CPP, art. 10)"],[
  ["Indiciado <b>preso</b> em flagrante ou preventivamente","<b>10 dias</b>"],
  ["Indiciado <b>solto</b>, com ou sem fiança","<b>30 dias</b> (o juiz pode prorrogar quando o fato for de difícil elucidação)"]],["50%",None]) +
 table(["Etapa","Regra"],[
  ["Relatório","Concluídas as investigações, o delegado faz o relatório e remete os autos"],
  ["Devolução para diligências (art. 16)","O MP só pode requerer a devolução para novas diligências imprescindíveis ao oferecimento da denúncia"],
  ["Arquivamento (art. 28, redação da Lei nº 13.964/2019)","Quem ordena o arquivamento é o <b>Ministério Público</b>, que comunica a vítima, o investigado e a autoridade policial e envia os autos à instância de revisão do próprio MP; a vítima pode recorrer em 30 dias (dispositivo com interpretação do STF nas ADIs 6.298, 6.300 e 6.305)"],
  ["Desarquivamento (art. 18)","Arquivado o inquérito por falta de base, a polícia pode fazer novas pesquisas se tiver notícia de outras provas"],
  ["Acordo de não persecução penal (art. 28-A)","Se não for caso de arquivamento e o investigado confessar formal e circunstanciadamente infração <b>sem violência ou grave ameaça</b>, com pena mínima <b>inferior a 4 anos</b>, o MP pode propor acordo, com condições como reparar o dano e prestar serviços"]],["30%",None]) +
 memo('Prazos: <strong>10 dias preso</strong>, <strong>30 dias solto</strong>. Delegado <strong>não</strong> arquiva; quem arquiva é o <strong>MP</strong>. ANPP: confissão + sem violência + pena mínima <strong>menor que 4 anos</strong>.'))

treino(2, [
 ("A polícia judiciária tem por fim a apuração das infrações penais e da sua autoria.","C","CPP, art. 4º."),
 ("Nos crimes de ação penal pública condicionada, o inquérito pode ser instaurado sem a representação do ofendido.","E","Não pode ser iniciado sem ela (art. 5º, § 4º)."),
 ("A autoridade policial pode mandar arquivar autos de inquérito quando não houver indícios de autoria.","E","Art. 17: a autoridade policial não poderá mandar arquivar."),
 ("O inquérito policial é dispensável quando o titular da ação já dispõe de elementos suficientes.","C","Arts. 12 e 39, § 5º."),
 ("O inquérito deve terminar em 10 dias se o indiciado estiver preso, e em 30 dias se estiver solto.","C","Art. 10."),
 ("O acordo de não persecução penal é cabível em crimes cometidos com violência ou grave ameaça.","E","Exige infração sem violência ou grave ameaça (art. 28-A).")])

# ================================================================ UNIDADE 3
opener("03","UNIDADE 3","Ação penal",["Espécies de ação penal","Ação penal pública","Ação penal privada","Pública x privada"],"U3")

def especies():
    N,G,O,R=C['navy'],C['blue'],C['golddeep'],C['red']
    s = f'<figure><svg viewBox="0 0 640 260" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    s += '<g stroke="#b9b3ad" stroke-width="2.5" fill="none"><path d="M320 46 V62 M160 62 H480 M160 62 V78 M480 62 V78 M160 132 V146 M80 146 H240 M80 146 V160 M240 146 V160 M480 132 V146 M380 146 H580 M380 146 V160 M480 146 V160 M580 146 V160"/></g>'
    s += f'<rect x="220" y="4" width="200" height="42" rx="12" fill="{N}"/><text x="320" y="31" text-anchor="middle" font-size="13" font-weight="900" fill="#fff">AÇÃO PENAL</text>'
    s += f'<rect x="60" y="78" width="200" height="54" rx="12" fill="{C["sky"]}" stroke="{G}" stroke-width="2.4"/><text x="160" y="100" text-anchor="middle" font-size="12.5" font-weight="900" fill="{G}">PÚBLICA</text><text x="160" y="118" text-anchor="middle" font-size="10" fill="{C["ink"]}">titular: Ministério Público (denúncia)</text>'
    s += f'<rect x="380" y="78" width="200" height="54" rx="12" fill="{C["goldsoft"]}" stroke="{O}" stroke-width="2.4"/><text x="480" y="100" text-anchor="middle" font-size="12.5" font-weight="900" fill="{O}">PRIVADA</text><text x="480" y="118" text-anchor="middle" font-size="10" fill="{C["ink"]}">titular: ofendido (queixa-crime)</text>'
    for x,a,b in [(80,"INCONDICIONADA","regra geral"),(240,"CONDICIONADA","representação ou requisição")]:
        s += f'<rect x="{x-74}" y="160" width="148" height="56" rx="10" fill="#fff" stroke="{G}" stroke-width="2"/><text x="{x}" y="184" text-anchor="middle" font-size="10.5" font-weight="900" fill="{C["ink"]}">{a}</text><text x="{x}" y="202" text-anchor="middle" font-size="8.8" fill="{C["muted"]}">{b}</text>'
    for x,a,b in [(380,"EXCLUSIVA","ofendido ou sucessores"),(480,"PERSONALÍSSIMA","só o ofendido"),(580,"SUBSIDIÁRIA","inércia do MP")]:
        s += f'<rect x="{x-48}" y="160" width="96" height="56" rx="10" fill="#fff" stroke="{O}" stroke-width="2"/><text x="{x}" y="184" text-anchor="middle" font-size="9.2" font-weight="900" fill="{C["ink"]}">{a}</text><text x="{x}" y="202" text-anchor="middle" font-size="8.2" fill="{C["muted"]}">{b}</text>'
    s += f'<text x="320" y="244" text-anchor="middle" font-size="10.5" font-weight="800" fill="{N}">Regra: a ação penal é pública incondicionada, salvo quando a lei disser o contrário.</text>'
    return s + '</svg><figcaption>Espécies de ação penal.</figcaption></figure>'

add(H(3,'Espécies de <span class="hl">ação penal</span>','Quem pode acusar e de que forma.', "A08") +
 oque(p('<strong>Ação penal</strong> é o direito de pedir ao Poder Judiciário a aplicação da lei penal ao caso concreto. É exercida por meio da <strong>denúncia</strong> (na ação pública, pelo Ministério Público) ou da <strong>queixa-crime</strong> (na ação privada, pelo ofendido).')) +
 especies() +
 memo('Pública = <strong>MP</strong>, por <strong>denúncia</strong>. Privada = <strong>ofendido</strong>, por <strong>queixa</strong>. A regra é a <strong>pública incondicionada</strong>.'))

add(H(3,'Ação penal <span class="hl">pública</span>','O Ministério Público acusa em nome do Estado.', "A09") +
 table(["","INCONDICIONADA","CONDICIONADA"],[
  ["Depende de autorização?","<b>Não</b>","<b>Sim</b>: representação do ofendido ou requisição do Ministro da Justiça (CPP, art. 24)"],
  ["Exemplos","Homicídio, roubo, tráfico, a maioria dos crimes","Ameaça (em regra), lesão corporal leve e culposa (Lei nº 9.099/1995), alguns crimes contra a honra de funcionário público"],
  ["Crimes contra o patrimônio público","Sempre ação pública, qualquer que seja o crime (art. 24, § 2º)","—"]],["24%",None,None]) +
 table(["Regra","Conteúdo"],[
  ["Representação irretratável (art. 25)","A representação será <b>irretratável depois de oferecida a denúncia</b>; antes disso, a vítima pode se retratar"],
  ["Prazo de decadência (art. 38)","A representação deve ser feita em <b>6 meses</b>, contados do dia em que a vítima soube quem é o autor; nos crimes com violência doméstica e familiar contra a mulher, o prazo é de <b>12 meses</b> (§ 2º, Lei nº 15.438/2026)"],
  ["Prazo da denúncia (art. 46)","<b>5 dias</b> se o réu estiver preso; <b>15 dias</b> se estiver solto ou afiançado, contados do recebimento dos autos pelo MP"],
  ["Requisitos da denúncia (art. 41)","Exposição do fato criminoso com todas as circunstâncias, qualificação do acusado, classificação do crime e rol de testemunhas, quando necessário"],
  ["Princípios","Oficialidade (órgão oficial); obrigatoriedade (havendo justa causa, o MP deve denunciar, com mitigações como o ANPP e a transação penal); indisponibilidade (o MP não pode desistir da ação já proposta)"]],["28%",None]))

add(H(3,'Ação penal <span class="hl">privada</span>','A vítima decide se e como acusa.', "A10") +
 table(["Espécie","O que é","Exemplo"],[
  ["Exclusiva","Proposta pelo ofendido ou, se ele morrer ou for declarado ausente, pelo cônjuge, ascendente, descendente ou irmão","Calúnia, difamação e injúria (em regra)"],
  ["Personalíssima","Só o próprio ofendido pode propor; não passa aos sucessores","Exemplo clássico da doutrina: induzimento a erro essencial no casamento (CP, art. 236)"],
  ["Subsidiária da pública","Se o MP não oferecer a denúncia no prazo legal, a vítima pode propor a queixa (CF, art. 5º, LIX; CPP, art. 29); o MP pode retomar a ação a qualquer tempo","Crime de ação pública em que o MP ficou inerte"]],["20%",None,"30%"]) +
 table(["Instituto","O que é","Base"],[
  ["Decadência","Perda do direito por não propor a queixa em <b>6 meses</b> (12 meses na violência doméstica e familiar contra a mulher)","CPP, art. 38"],
  ["Renúncia","A vítima abre mão do direito <b>antes</b> de propor a queixa; a renúncia em relação a um dos autores se estende a todos","CPP, art. 49"],
  ["Perdão","A vítima desiste <b>depois</b> de proposta a queixa; concedido a um, aproveita a todos, mas só produz efeito para quem o aceitar","CPP, art. 51"],
  ["Perempção","Desídia do querelante: por exemplo, deixar o processo parado por 30 dias seguidos","CPP, art. 60"],
  ["Indivisibilidade","A queixa contra um dos autores obriga ao processo de todos","CPP, art. 48"]],["18%",None,"16%"]) +
 memo('Privada: <strong>oportunidade</strong>, <strong>disponibilidade</strong> e <strong>indivisibilidade</strong>. <strong>Renúncia</strong> = antes da queixa. <strong>Perdão</strong> = depois, e depende de <strong>aceitação</strong>.'))

atencao(
 table(["","AÇÃO PÚBLICA","AÇÃO PRIVADA"],[
  ["Titular","Ministério Público","Ofendido ou representante legal"],
  ["Peça inicial","Denúncia","Queixa-crime"],
  ["Princípio quanto a propor","Obrigatoriedade (mitigada)","Oportunidade (a vítima decide)"],
  ["Princípio quanto a desistir","Indisponibilidade","Disponibilidade (renúncia, perdão, perempção)"],
  ["Prazo","5 dias (preso) e 15 dias (solto) para a denúncia","6 meses de decadência para a queixa (12 na violência doméstica contra a mulher)"]],["22%",None,None]) +
 ex(p('Joana sofre uma ameaça do vizinho. A ameaça é, em regra, crime de ação pública <b>condicionada à representação</b>: se ela não representar em 6 meses contados de quando soube quem a ameaçou, ocorre a <b>decadência</b>. Se a ameaça for contra a mulher por razões da condição do sexo feminino, a ação é <b>incondicionada</b> (CP, art. 147, § 2º). Já se o vizinho a <b>injuriar</b>, ela precisa de um advogado para oferecer <b>queixa-crime</b> (ação privada).')) +
 pega('<ul><li>A representação é <b>retratável até o oferecimento</b> da denúncia, e <b>irretratável depois</b>.</li><li>Renúncia é <b>unilateral</b>; perdão é <b>bilateral</b> (depende de aceitação).</li><li>A ação privada subsidiária só cabe quando o MP fica <b>inerte</b>; se ele pediu o arquivamento, não cabe.</li></ul>'),
 ["denúncia","queixa-crime","representação","decadência","renúncia","perdão","perempção"])

treino(3, [
 ("A representação será irretratável depois de oferecida a denúncia.","C","CPP, art. 25."),
 ("O prazo decadencial para a representação ou a queixa é, em regra, de seis meses, contado do dia em que o ofendido vem a saber quem é o autor do crime.","C","CPP, art. 38."),
 ("O prazo para o oferecimento da denúncia, estando o réu preso, é de 15 dias.","E","5 dias (preso) e 15 dias (solto) (art. 46)."),
 ("O perdão do ofendido produz efeitos independentemente de aceitação do querelado.","E","Não produz efeito para quem o recusar (art. 51)."),
 ("A renúncia ao direito de queixa em relação a um dos autores do crime se estende a todos.","C","Art. 49."),
 ("Na ação penal privada subsidiária da pública, a vítima pode oferecer queixa se o MP não oferecer a denúncia no prazo legal.","C","CF, art. 5º, LIX; CPP, art. 29.")])

# ================================================================ UNIDADE 4
opener("04","UNIDADE 4","Provas",["Noções gerais","Provas ilícitas","Principais meios de prova","Cadeia de custódia"],"U4")

add(H(4,'Noções gerais de <span class="hl">prova</span>','Elemento informativo x prova.', "A12") +
 lei(cpp("Art. 155, caput (trecho e síntese)"),'<p>O juiz formará sua convicção pela livre apreciação da prova produzida em contraditório judicial, "não podendo fundamentar sua decisão exclusivamente nos elementos informativos colhidos na investigação", ressalvadas as provas cautelares, não repetíveis e antecipadas.</p>') +
 table(["","ELEMENTO INFORMATIVO","PROVA"],[
  ["Onde é produzido","Na <b>investigação</b> (inquérito)","Em <b>juízo</b>"],
  ["Contraditório","Não há (ou é limitado)","Há contraditório e ampla defesa"],
  ["Pode condenar sozinho?","<b>Não</b>","Sim"],
  ["Exceções","Provas <b>cautelares</b> (ex.: interceptação), <b>não repetíveis</b> (ex.: exame de corpo de delito em lesão que desaparece) e <b>antecipadas</b>","—"]],["22%",None,None]) +
 table(["Regra","Conteúdo"],[
  ["Sistema de valoração","Livre convencimento motivado (persuasão racional): o juiz aprecia livremente, mas deve fundamentar"],
  ["Ônus da prova (art. 156)","A prova da alegação incumbe a quem a fizer; o juiz pode, de ofício, determinar provas urgentes e relevantes"],
  ["Confissão (art. 197)","Tem valor <b>relativo</b>: é confrontada com as demais provas"]],["26%",None]) +
 memo('Condenação <strong>não</strong> pode se basear <strong>só</strong> no inquérito, salvo provas <strong>cautelares, não repetíveis e antecipadas</strong>. Sistema: <strong>livre convencimento motivado</strong>.'))

add(H(4,'Provas <span class="hl">ilícitas</span>','O que não pode entrar no processo.', "A13") +
 lei(cpp("Art. 157, caput (trecho)"),'<p>"São inadmissíveis, devendo ser desentranhadas do processo, as provas ilícitas", assim entendidas as obtidas em violação a normas constitucionais ou legais.</p>') +
 table(["Regra","Conteúdo"],[
  ["Prova ilícita","Obtida com violação de normas constitucionais ou legais (ex.: confissão sob tortura; entrada em casa sem mandado fora das hipóteses legais)"],
  ["Prova ilícita por derivação (§ 1º)","Também são inadmissíveis as provas <b>derivadas</b> das ilícitas: a teoria dos “frutos da árvore envenenada”"],
  ["Exceções (§§ 1º e 2º)","Não há contaminação quando não houver nexo de causalidade entre a ilícita e a derivada, ou quando a derivada puder ser obtida por <b>fonte independente</b>"],
  ["Destino (§ 3º)","A prova declarada inadmissível é desentranhada e inutilizada por decisão judicial"],
  ["Juiz contaminado (§ 5º)","O juiz que conheceu o conteúdo da prova inadmissível não poderá proferir a sentença (dispositivo da Lei nº 13.964/2019, com análise do STF nas ADIs 6.298 e outras)"]],["28%",None]) +
 flow([("bolt",["CONFISSÃO","obtida sob","tortura"]),("search",["LOCAL DA","ARMA indicado","na confissão"]),("xmark",["ARMA","também","contaminada"]),("check",["EXCEÇÃO","fonte","independente"])],
      "Frutos da árvore envenenada: a prova derivada da ilícita também é ilícita, salvo exceções.", colors=colors("r","o","r","g")) +
 memo('Prova ilícita: <strong>inadmissível</strong> e <strong>desentranhada</strong>. Derivadas também, salvo <strong>ausência de nexo</strong> ou <strong>fonte independente</strong>.'))

add(H(4,'Principais <span class="hl">meios de prova</span>','Os mais cobrados em provas policiais.', "A14") +
 table(["Meio de prova","Regra principal"],[
  ["Exame de corpo de delito (art. 158)","Quando a infração deixar vestígios, será indispensável o exame de corpo de delito, direto ou indireto, <b>não podendo supri-lo a confissão</b> do acusado; se os vestígios desaparecerem, a prova testemunhal pode suprir a falta (art. 167)"],
  ["Confissão (art. 197)","Valor relativo, confrontado com as demais provas"],
  ["Testemunhas (arts. 202, 206 e 207)","Toda pessoa poderá ser testemunha; ascendentes, descendentes, cônjuge e irmão do acusado podem recusar-se a depor (salvo quando não for possível obter a prova de outro modo); quem deve guardar sigilo profissional é proibido de depor, salvo se desobrigado"],
  ["Reconhecimento de pessoas (art. 226)","Procedimento: a pessoa descreve o suspeito; o suspeito é colocado ao lado de outras pessoas parecidas; lavra-se auto. O STJ passou a exigir a observância desse procedimento para a validade do reconhecimento"],
  ["Perícias","Feitas, em regra, por perito oficial; o laudo é base técnica para a decisão"]],["28%",None]) +
 ex(p('Em uma briga, a vítima sofre lesões. Mesmo que o agressor <b>confesse</b>, o exame de corpo de delito continua sendo <b>indispensável</b>, porque a lesão deixa vestígios. Se os vestígios desaparecerem antes do exame (a vítima não foi examinada e se curou), testemunhas podem suprir a falta.')) +
 memo('Crime que deixa vestígio = <strong>exame de corpo de delito indispensável</strong>. A <strong>confissão não supre</strong> o exame.'))

def custodia():
    it=["RECONHE-|CIMENTO","ISOLA-|MENTO","FIXAÇÃO","COLETA","ACONDICIO-|NAMENTO","TRANS-|PORTE","RECEBI-|MENTO","PROCES-|SAMENTO","ARMAZENA-|MENTO","DESCARTE"]
    cols=[C['navy'],C['red'],C['golddeep'],C['blue'],C['navy'],C['red'],C['golddeep'],C['blue'],C['navy'],C['red']]
    s = f'<figure><svg viewBox="0 0 640 230" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">{arrowdefs("cc")}'
    for k,t in enumerate(it):
        row=k//5; col=k%5; x=8+col*127; y=10+row*104
        fg=cols[k]
        s += f'<rect x="{x}" y="{y}" width="110" height="78" rx="12" fill="#fff" stroke="{fg}" stroke-width="2.4"/><circle cx="{x+18}" cy="{y+18}" r="12" fill="{fg}"/><text x="{x+18}" y="{y+23}" text-anchor="middle" font-size="12" font-weight="900" fill="#fff">{k+1}</text>'
        parts=t.split("|")
        for j,pt in enumerate(parts): s += f'<text x="{x+58}" y="{y+44+j*15-(7 if len(parts)>1 else 0)}" text-anchor="middle" font-size="11" font-weight="900" fill="{C["ink"]}">{pt}</text>'
        if col<4: s += f'<line x1="{x+112}" y1="{y+39}" x2="{x+125}" y2="{y+39}" stroke="{C["ink"]}" stroke-width="2.2" marker-end="url(#cc)"/>'
    s += f'<text x="320" y="222" text-anchor="middle" font-size="10" fill="{C["muted"]}">As fases 1 a 3 acontecem no local do crime; é aqui que a atuação do primeiro agente a chegar é decisiva.</text>'
    return s + '</svg><figcaption>As 10 etapas da cadeia de custódia (CPP, art. 158-B).</figcaption></figure>'

add(H(4,'Cadeia de <span class="hl">custódia</span>','A história documentada de cada vestígio.', "A15") +
 lei(cpp("Art. 158-A, caput (trecho, Lei nº 13.964/2019)"),'<p>Considera-se cadeia de custódia o "conjunto de todos os procedimentos utilizados para manter e documentar a história cronológica do vestígio" coletado em locais ou em vítimas de crimes, para rastrear sua posse e manuseio a partir de seu reconhecimento até o descarte.</p>') +
 custodia() +
 traduz(p('A cadeia de custódia garante que o vestígio apresentado ao juiz é <strong>o mesmo</strong> que foi encontrado no local, sem troca, contaminação ou adulteração. Por isso cada passo é <strong>registrado</strong>: quem encontrou, quem isolou, quem coletou, como embalou, quem transportou. A coleta deve ser feita <strong>preferencialmente por perito oficial</strong>, e é proibida a entrada em locais isolados ou a remoção de vestígios antes da liberação pelo perito (art. 158-C).'),"profa"))

atencao(
 table(["Etapa","O que é (em síntese)"],[
  ["1. Reconhecimento","Distinguir um elemento como de potencial interesse para a perícia"],
  ["2. Isolamento","Evitar que se altere o estado das coisas: isolar e preservar o local"],
  ["3. Fixação","Descrever detalhadamente o vestígio como encontrado (fotos, croquis)"],
  ["4. Coleta","Recolher o vestígio para análise pericial"],
  ["5. Acondicionamento","Embalar individualmente cada vestígio, com lacre"],
  ["6 a 10","Transporte, recebimento, processamento (exame pericial), armazenamento e descarte"]],["24%",None]) +
 ex(p('Guardas municipais são os primeiros a chegar a uma ocorrência com vítima de disparo. O correto é <b>socorrer a vítima</b>, <b>isolar</b> a área (fita, controle de curiosos) e <b>não tocar</b> nos objetos, aguardando a perícia e a polícia judiciária. Se alguém recolhe a cápsula do chão "para ajudar", sem registro, compromete a cadeia de custódia e pode prejudicar o valor da prova.')) +
 pega('<ul><li>São <b>10 etapas</b>, começando pelo <b>reconhecimento</b> e terminando no <b>descarte</b>.</li><li>Isolamento e fixação vêm <b>antes</b> da coleta.</li><li>A coleta é feita <b>preferencialmente por perito oficial</b>.</li></ul>'),
 ["vestígio","reconhecimento","isolamento","fixação","coleta","perito oficial"])

treino(4, [
 ("O juiz pode fundamentar a condenação exclusivamente nos elementos informativos do inquérito.","E","Art. 155: não exclusivamente, ressalvadas as provas cautelares, não repetíveis e antecipadas."),
 ("São inadmissíveis as provas derivadas das ilícitas, salvo quando não evidenciado o nexo de causalidade ou quando puderem ser obtidas por fonte independente.","C","Art. 157, § 1º."),
 ("Quando a infração deixar vestígios, a confissão do acusado pode suprir o exame de corpo de delito.","E","Art. 158: a confissão não supre."),
 ("A cadeia de custódia tem dez etapas, da coleta ao armazenamento.","E","Dez etapas, do reconhecimento ao descarte."),
 ("O isolamento do local é uma das etapas da cadeia de custódia.","C","Art. 158-B, II."),
 ("A confissão tem valor relativo e deve ser confrontada com as demais provas.","C","Art. 197.")])

# ================================================================ UNIDADE 5
opener("05","UNIDADE 5","Sujeitos e procedimentos",["Sujeitos do processo","Prisão em flagrante e audiência de custódia","Procedimentos: noções introdutórias"],"U5")

add(H(5,'Sujeitos do <span class="hl">processo</span>','Quem participa da relação processual.', "A16") +
 scene3([("JUIZ",C['navy'],NV,"prof",["Imparcial:","conduz o processo","e julga."],"sujeito principal"),
  ("ACUSAÇÃO",C['red'],C['redsoft'],"profa",["MP (ação pública)","ou querelante","(ação privada)."],"parte que acusa"),
  ("DEFESA",C['blue'],C['sky'],"prof",["Acusado + defensor:","ninguém é julgado","sem defensor."],"parte que se defende")], "Situação ilustrada: os sujeitos principais do processo penal.") +
 table(["Sujeito","Papel (base no CPP)"],[
  ["Juiz","Imparcial; conduz o processo e julga; na fase de investigação, atua o juiz das garantias (arts. 3º-B a 3º-F)"],
  ["Ministério Público","Promove, <b>privativamente</b>, a ação penal pública e fiscaliza a execução da lei (art. 257)"],
  ["Acusado e defensor","“Nenhum acusado, ainda que ausente ou foragido, será processado ou julgado sem defensor” (art. 261)"],
  ["Assistente de acusação","O ofendido (ou seu representante, ou sucessores) pode intervir na ação pública como assistente do MP (art. 268)"],
  ["Auxiliares","Peritos, intérpretes, oficiais de justiça, escrivães (sujeitos secundários)"]],["24%",None]))

add(H(5,'Prisão em flagrante e <span class="hl">audiência de custódia</span>','O momento mais comum da atuação policial.', "A17") +
 lei(cpp("Art. 302"),'<p>Considera-se em flagrante delito quem: I - está cometendo a infração penal; II - acaba de cometê-la; III - é perseguido, logo após, pela autoridade, pelo ofendido ou por qualquer pessoa, em situação que faça presumir ser autor da infração; IV - é encontrado, logo depois, com instrumentos, armas, objetos ou papéis que façam presumir ser ele autor da infração.</p>') +
 table(["Espécie (doutrina)","Inciso","Exemplo"],[
  ["Próprio (real)","I e II","Guarda municipal vê o suspeito arrombando um carro"],
  ["Impróprio (quase flagrante)","III","Perseguição logo após o crime, sem interrupção"],
  ["Presumido (ficto)","IV","Suspeito encontrado logo depois com a bolsa da vítima e a faca usada"]],["26%","12%",None]) +
 table(["Regra","Conteúdo"],[
  ["Quem pode prender (art. 301)","Qualquer do povo <b>pode</b> e as autoridades policiais e seus agentes <b>devem</b> prender quem esteja em flagrante"],
  ["Auto de prisão (art. 304)","Ouvidos o condutor, as testemunhas e o preso, lavra-se o auto de prisão em flagrante"],
  ["Audiência de custódia (art. 310)","O juiz deve realizar audiência de custódia em até <b>24 horas</b> da prisão e decidir: <b>relaxar</b> a prisão ilegal, <b>converter</b> em preventiva (se presentes os requisitos) ou conceder <b>liberdade provisória</b>"],
  ["Prisão preventiva (arts. 311 a 313)","Decretada pelo juiz, a requerimento do MP, do querelante ou do assistente, ou por representação da autoridade policial, para garantia da ordem pública, da ordem econômica, por conveniência da instrução ou para assegurar a aplicação da lei penal, com indícios de autoria e prova da existência do crime; não pode ser fundada na gravidade abstrata do crime (art. 312, § 4º, Lei nº 15.272/2025)"]],["24%",None]) +
 memo('Flagrante: <strong>próprio</strong> (cometendo ou acabou de cometer), <strong>impróprio</strong> (perseguido logo após), <strong>presumido</strong> (encontrado logo depois). Custódia em <strong>24 horas</strong>. Qualquer do povo <strong>pode</strong>; policiais <strong>devem</strong> prender.'))

def fluxo():
    N,G,O,R=C['navy'],C['blue'],C['golddeep'],C['red']
    it=[("DENÚNCIA","ou queixa"),("RECEBIMENTO","e citação"),("RESPOSTA","10 dias (art. 396)"),("ABSOLVIÇÃO","SUMÁRIA? (art. 397)"),("AUDIÊNCIA","até 60 dias (art. 400)"),("SENTENÇA","")]
    s = f'<figure><svg viewBox="0 0 640 150" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">{arrowdefs("fx")}'
    cols=[R,N,G,O,N,R]
    for k,(a,b) in enumerate(it):
        x=4+k*106; fg=cols[k]
        s += f'<rect x="{x}" y="14" width="94" height="70" rx="12" fill="#fff" stroke="{fg}" stroke-width="2.4"/><text x="{x+47}" y="44" text-anchor="middle" font-size="10" font-weight="900" fill="{fg}">{a}</text><text x="{x+47}" y="62" text-anchor="middle" font-size="8.6" fill="{C["ink"]}">{b}</text>'
        if k<5: s += f'<line x1="{x+96}" y1="49" x2="{x+104}" y2="49" stroke="{C["ink"]}" stroke-width="2.2" marker-end="url(#fx)"/>'
    s += f'<text x="320" y="110" text-anchor="middle" font-size="10" font-weight="800" fill="{N}">Ordem na audiência (art. 400): ofendido → testemunhas de acusação → testemunhas de defesa →</text>'
    s += f'<text x="320" y="128" text-anchor="middle" font-size="10" font-weight="800" fill="{N}">peritos, acareações e reconhecimento → interrogatório do acusado (por último)</text>'
    return s + '</svg><figcaption>Fluxo simplificado do procedimento comum ordinário.</figcaption></figure>'

add(H(5,'Procedimentos: <span class="hl">noções introdutórias</span>','Comum ou especial; ordinário, sumário ou sumaríssimo.', "A18") +
 table(["Procedimento comum (art. 394, § 1º)","Quando se aplica"],[
  ["Ordinário","Crime com pena máxima <b>igual ou superior a 4 anos</b>"],
  ["Sumário","Crime com pena máxima <b>inferior a 4 anos</b>"],
  ["Sumaríssimo","<b>Infrações de menor potencial ofensivo</b> (contravenções e crimes com pena máxima de até 2 anos), nos Juizados Especiais Criminais (Lei nº 9.099/1995)"]],["40%",None]) +
 fluxo() +
 table(["Ponto","Regra"],[
  ["Procedimentos especiais","Têm ritos próprios: Tribunal do Júri (crimes dolosos contra a vida), crimes de responsabilidade de funcionários públicos, Lei de Drogas, entre outros"],
  ["Termo circunstanciado","Nas infrações de menor potencial ofensivo, em vez do inquérito e do auto de prisão, lavra-se termo circunstanciado (Lei nº 9.099/1995)"],
  ["Prioridade (art. 394-A, Lei nº 14.994/2024)","Processos de crimes hediondos e de violência contra a mulher têm prioridade de tramitação"]],["26%",None]) +
 memo('Pena máxima <strong>4 anos ou mais</strong>: ordinário. <strong>Menos de 4</strong>: sumário. <strong>Menor potencial ofensivo</strong>: sumaríssimo. Interrogatório: <strong>por último</strong>.'))

treino(5, [
 ("Nenhum acusado, ainda que ausente ou foragido, será processado ou julgado sem defensor.","C","CPP, art. 261."),
 ("Considera-se em flagrante quem é encontrado, logo depois, com instrumentos ou objetos que façam presumir ser ele o autor da infração.","C","Art. 302, IV (flagrante presumido)."),
 ("Qualquer do povo deve prender quem esteja em flagrante delito, sob pena de crime.","E","Qualquer do povo pode; as autoridades e seus agentes devem (art. 301)."),
 ("A audiência de custódia deve ser realizada em até 24 horas da prisão.","C","Art. 310."),
 ("O procedimento comum ordinário aplica-se aos crimes com pena máxima inferior a 4 anos.","E","Ordinário: pena máxima igual ou superior a 4 anos (art. 394, § 1º)."),
 ("Na audiência de instrução, o interrogatório do acusado é o último ato da instrução oral.","C","Art. 400.")])

# ================================================================ REVISÃO
mapa(("PROCESSO","PENAL",""), [
  ("PRINCÍPIOS",["inocência até o trânsito","contraditório e defesa","provas ilícitas: não"],C['navy'],NV),
  ("INQUÉRITO",["escrito, sigiloso, inquisitivo","dispensável, indisponível","10 dias preso · 30 solto"],C['golddeep'],C['goldsoft']),
  ("AÇÃO PÚBLICA",["MP · denúncia","5 dias preso · 15 solto","representação: 6 meses"],C['blue'],C['sky']),
  ("AÇÃO PRIVADA",["ofendido · queixa","renúncia antes · perdão depois","perempção: 30 dias parado"],C['golddeep'],C['goldsoft']),
  ("PROVAS",["não só o inquérito","corpo de delito indispensável","custódia: 10 etapas"],C['red'],C['redsoft']),
  ("FLAGRANTE",["próprio · impróprio · presumido","custódia em 24 horas","ordinário: pena máx. ≥ 4"],C['navy'],NV)], "Mapa conceitual do Caderno 13.", "O caderno em seis blocos. Explique cada caixa em voz alta.", center_color=C['gold'])

erros([
  ["“O delegado pode arquivar o inquérito se não achar o autor.”","A autoridade policial não pode mandar arquivar (art. 17); o MP é que arquiva."],
  ["“Sem inquérito não há denúncia.”","O inquérito é dispensável (arts. 12 e 39, § 5º)."],
  ["“O inquérito tem contraditório e ampla defesa plenos.”","É inquisitivo; o defensor tem acesso aos elementos documentados (SV 14)."],
  ["“O inquérito de réu preso tem 30 dias.”","10 dias preso; 30 dias solto (art. 10)."],
  ["“Na ação condicionada, o inquérito começa sem representação.”","Não pode ser iniciado sem ela (art. 5º, § 4º)."],
  ["“A representação pode ser retirada a qualquer tempo.”","É irretratável depois de oferecida a denúncia (art. 25)."],
  ["“A denúncia de réu preso tem 15 dias.”","5 dias preso; 15 dias solto (art. 46)."]],
 [["“O perdão vale mesmo se o querelado recusar.”","Não produz efeito para quem o recusar (art. 51)."],
  ["“O juiz pode condenar só com base no inquérito.”","Não, salvo provas cautelares, não repetíveis e antecipadas (art. 155)."],
  ["“A confissão supre o exame de corpo de delito.”","Não supre (art. 158)."],
  ["“A cadeia de custódia começa na coleta.”","Começa no reconhecimento; são 10 etapas, até o descarte."],
  ["“Qualquer do povo deve prender em flagrante.”","Pode; os policiais é que devem (art. 301)."],
  ["“Guarda municipal faz polícia judiciária.”","Não; o STF admite policiamento ostensivo e comunitário, excluída a polícia judiciária."],
  ["“O interrogatório é o primeiro ato da audiência.”","É o último (art. 400)."]])

flashcards([("NOÇÕES","O que é persecução penal?","Investigação + ação penal."),
 ("PRINCÍPIOS","Presunção de inocência?","Ninguém é culpado até o trânsito em julgado (CF, art. 5º, LVII)."),
 ("SISTEMAS","Qual sistema o CPP adota expressamente?","O acusatório (art. 3º-A)."),
 ("INQUÉRITO","Quem preside o inquérito?","O delegado de polícia (autoridade policial)."),
 ("INQUÉRITO","Como começa o inquérito na ação condicionada?","Com a representação do ofendido (ou requisição do Ministro da Justiça)."),
 ("INQUÉRITO","Características do inquérito?","Escrito, sigiloso, inquisitivo, dispensável, indisponível e oficial."),
 ("INQUÉRITO","Prazos do inquérito?","10 dias preso; 30 dias solto (art. 10)."),
 ("INQUÉRITO","Quem arquiva o inquérito?","O Ministério Público (art. 28); o delegado não pode (art. 17)."),
 ("INQUÉRITO","Requisitos do ANPP?","Confissão formal e circunstanciada, sem violência ou grave ameaça, pena mínima inferior a 4 anos."),
 ("AÇÃO","Titular da ação pública e peça?","Ministério Público, por denúncia."),
 ("AÇÃO","Titular da ação privada e peça?","Ofendido, por queixa-crime."),
 ("AÇÃO","Quando a representação fica irretratável?","Depois de oferecida a denúncia (art. 25)."),
 ("AÇÃO","Prazo de decadência?","6 meses do conhecimento da autoria; 12 meses na violência doméstica contra a mulher."),
 ("AÇÃO","Prazos da denúncia?","5 dias preso; 15 dias solto (art. 46)."),
 ("AÇÃO","Renúncia x perdão?","Renúncia: antes da queixa, unilateral. Perdão: depois, depende de aceitação."),
 ("AÇÃO","Perempção?","Desídia do querelante, como deixar o processo parado por 30 dias seguidos."),
 ("PROVAS","Elemento informativo pode condenar sozinho?","Não, salvo provas cautelares, não repetíveis e antecipadas."),
 ("PROVAS","Prova derivada da ilícita?","Também inadmissível, salvo sem nexo ou por fonte independente."),
 ("PROVAS","Confissão supre corpo de delito?","Não (art. 158)."),
 ("CUSTÓDIA","Primeira e última etapas da cadeia de custódia?","Reconhecimento e descarte."),
 ("FLAGRANTE","Três espécies de flagrante?","Próprio, impróprio e presumido (art. 302)."),
 ("FLAGRANTE","Prazo da audiência de custódia?","Até 24 horas da prisão (art. 310)."),
 ("PROCEDIMENTO","Ordinário x sumário?","Ordinário: pena máxima ≥ 4 anos. Sumário: &lt; 4 anos."),
 ("PROCEDIMENTO","Último ato da instrução oral?","O interrogatório do acusado (art. 400).")])

Q = [
 ("Princípios","Segundo a Constituição, ninguém será considerado culpado:",
  ["após o recebimento da denúncia.","após a sentença de primeiro grau.","até o trânsito em julgado de sentença penal condenatória.","após o indiciamento no inquérito.","após a prisão em flagrante."],"C",
  "CF, art. 5º, LVII: princípio da presunção de inocência (não culpabilidade).","Culpado só após o trânsito em julgado."),
 ("Sistemas","O Código de Processo Penal, após a Lei nº 13.964/2019, estabelece expressamente que o processo penal terá estrutura:",
  ["inquisitiva.","mista.","acusatória.","inquisitória mitigada.","administrativa."],"C",
  "Art. 3º-A: estrutura acusatória, vedadas a iniciativa do juiz na fase de investigação e a substituição da atuação probatória da acusação.","CPP: acusatório (art. 3º-A)."),
 ("Investigação","A polícia judiciária, nos termos do art. 4º do CPP, tem por fim:",
  ["julgar as infrações penais.","a apuração das infrações penais e da sua autoria.","executar as penas.","fazer exclusivamente o policiamento ostensivo.","oferecer a denúncia."],"B",
  "Art. 4º do CPP. Polícia judiciária: Polícias Civil e Federal.","Polícia judiciária: infração + autoria."),
 ("Inquérito","Em crime de ação penal pública condicionada à representação, o inquérito policial:",
  ["pode ser instaurado de ofício.","não poderá ser iniciado sem a representação.","depende de requisição do juiz.","é sempre dispensado.","só pode ser instaurado pelo MP."],"B",
  "Art. 5º, § 4º.","Condicionada: sem representação, sem inquérito."),
 ("Inquérito","NÃO é característica do inquérito policial:",
  ["ser escrito.","ser sigiloso.","ser inquisitivo.","ser indispensável ao oferecimento da denúncia.","ser indisponível para a autoridade policial."],"D",
  "O inquérito é dispensável: se o MP tiver elementos suficientes, pode denunciar sem ele (arts. 12 e 39, § 5º).","Inquérito é dispensável."),
 ("Inquérito","Concluídas as investigações sem identificar o autor, a autoridade policial:",
  ["pode mandar arquivar o inquérito.","não pode mandar arquivar o inquérito.","deve oferecer denúncia contra desconhecido.","deve extinguir a punibilidade.","deve devolver o inquérito à vítima."],"B",
  "Art. 17: a autoridade policial não poderá mandar arquivar autos de inquérito; o arquivamento é ordenado pelo MP (art. 28).","Delegado não arquiva."),
 ("Prazos","O inquérito policial deve terminar, estando o indiciado preso em flagrante, no prazo de:",
  ["5 dias.","10 dias.","15 dias.","30 dias.","60 dias."],"B",
  "Art. 10: 10 dias (preso) e 30 dias (solto).","Inquérito: 10 preso, 30 solto."),
 ("ANPP","Um dos requisitos do acordo de não persecução penal (art. 28-A do CPP) é:",
  ["crime cometido com violência ou grave ameaça.","pena mínima inferior a 4 anos e confissão formal e circunstanciada.","pena máxima superior a 8 anos.","reincidência do investigado.","crime hediondo."],"B",
  "Exige infração sem violência ou grave ameaça, pena mínima inferior a 4 anos e confissão formal e circunstanciada, entre outros requisitos.","ANPP: confissão + sem violência + pena mínima &lt; 4."),
 ("Ação penal","Na ação penal pública, a peça inicial e o titular são, respectivamente:",
  ["queixa e ofendido.","denúncia e Ministério Público.","representação e delegado.","denúncia e ofendido.","queixa e Ministério Público."],"B",
  "Ação pública: MP, por denúncia (CF, art. 129, I; CPP, art. 257). Ação privada: ofendido, por queixa.","Pública = MP + denúncia."),
 ("Representação","Segundo o CPP, a representação do ofendido:",
  ["pode ser retratada a qualquer tempo.","será irretratável depois de oferecida a denúncia.","é irretratável desde o início.","dispensa forma escrita ou oral.","só pode ser feita ao juiz."],"B",
  "Art. 25.","Irretratável após a denúncia."),
 ("Decadência","Em regra, o ofendido decai do direito de queixa ou de representação se não o exercer no prazo de:",
  ["30 dias.","3 meses.","6 meses, contados do dia em que soube quem é o autor do crime.","1 ano, contado do fato.","2 anos."],"C",
  "Art. 38. Nos crimes com violência doméstica e familiar contra a mulher, o prazo é de 12 meses (§ 2º, Lei nº 15.438/2026).","Decadência: 6 meses (regra)."),
 ("Denúncia","O prazo para o oferecimento da denúncia, estando o réu solto, é de:",
  ["5 dias.","10 dias.","15 dias.","30 dias.","6 meses."],"C",
  "Art. 46: 5 dias (preso) e 15 dias (solto ou afiançado).","Denúncia: 5 preso, 15 solto."),
 ("Ação privada","Sobre o perdão do ofendido na ação penal privada, é correto afirmar:",
  ["é concedido antes da queixa.","concedido a um dos querelados, aproveita a todos, mas não produz efeito em relação ao que o recusar.","não depende de aceitação.","só cabe na ação pública.","é sinônimo de renúncia."],"B",
  "Art. 51. A renúncia é anterior à queixa e unilateral; o perdão é posterior e depende de aceitação.","Perdão: depois e com aceitação."),
 ("Ação privada","Deixar o querelante de promover o andamento do processo durante 30 dias seguidos caracteriza:",
  ["decadência.","renúncia.","perempção.","perdão.","prescrição."],"C",
  "Art. 60, I.","30 dias parado = perempção."),
 ("Ação subsidiária","A ação penal privada subsidiária da pública é cabível quando:",
  ["o MP pede o arquivamento do inquérito.","o MP não oferece a denúncia no prazo legal.","a vítima discorda da classificação do crime.","o juiz rejeita a denúncia.","o réu está preso."],"B",
  "CF, art. 5º, LIX; CPP, art. 29. Exige inércia do MP; o pedido de arquivamento não é inércia.","Subsidiária = inércia do MP."),
 ("Provas","De acordo com o art. 155 do CPP, o juiz:",
  ["pode condenar com base exclusivamente no inquérito.","forma sua convicção pela livre apreciação da prova produzida em contraditório judicial, não podendo fundamentar a decisão exclusivamente nos elementos informativos da investigação, ressalvadas as provas cautelares, não repetíveis e antecipadas.","está vinculado a provas tarifadas.","não precisa fundamentar suas decisões.","só pode considerar a confissão."],"B",
  "Livre convencimento motivado com limite quanto aos elementos informativos.","Inquérito sozinho não condena."),
 ("Provas ilícitas","Sobre as provas ilícitas, é correto afirmar:",
  ["são admitidas se forem decisivas.","as derivadas das ilícitas são sempre válidas.","são inadmissíveis, assim como as derivadas, salvo ausência de nexo ou fonte independente.","podem ser usadas pela acusação, mas não pela defesa.","dependem de confirmação do réu."],"C",
  "CPP, art. 157, caput e §§ 1º e 2º; CF, art. 5º, LVI.","Ilícita e derivada: fora, salvo exceções."),
 ("Corpo de delito","Quando a infração deixar vestígios, o exame de corpo de delito:",
  ["pode ser suprido pela confissão.","é indispensável, não podendo supri-lo a confissão do acusado.","é dispensável.","só é feito a pedido da defesa.","só pode ser indireto."],"B",
  "Art. 158. Se os vestígios desaparecerem, a prova testemunhal pode suprir a falta (art. 167).","Confissão não supre corpo de delito."),
 ("Cadeia de custódia","A primeira etapa da cadeia de custódia, segundo o art. 158-B do CPP, é o(a):",
  ["coleta.","isolamento.","reconhecimento.","transporte.","processamento."],"C",
  "As etapas são: reconhecimento, isolamento, fixação, coleta, acondicionamento, transporte, recebimento, processamento, armazenamento e descarte.","Começa no reconhecimento."),
 ("Cadeia de custódia","Ao chegar primeiro a um local de crime, o agente de segurança deve, para preservar a cadeia de custódia:",
  ["recolher os objetos para entregá-los à delegacia.","isolar e preservar o local, sem alterar o estado das coisas, aguardando a perícia (após socorrer eventual vítima).","limpar o local para evitar acidentes.","liberar a entrada de curiosos para identificar testemunhas.","fotografar e descartar os vestígios menores."],"B",
  "Isolamento e preservação estão entre as primeiras etapas; a coleta é feita preferencialmente por perito oficial (art. 158-C).","Isolar e não tocar."),
 ("Sujeitos","Segundo o CPP, o Ministério Público:",
  ["promove privativamente a ação penal pública e fiscaliza a execução da lei.","julga os crimes de menor potencial ofensivo.","preside o inquérito policial.","promove a ação penal privada.","atua apenas como assistente da vítima."],"A",
  "Art. 257. Quem preside o inquérito é o delegado.","MP: titular privativo da ação pública."),
 ("Flagrante","Suspeito encontrado, logo depois do crime, com a bolsa da vítima e a faca utilizada encontra-se em flagrante:",
  ["próprio.","impróprio.","presumido (ficto).","preparado.","esperado."],"C",
  "Art. 302, IV: encontrado logo depois com instrumentos ou objetos que façam presumir ser o autor.","Encontrado com objetos = presumido."),
 ("Custódia","Após a prisão em flagrante, a audiência de custódia deve ser realizada em até:",
  ["12 horas.","24 horas.","48 horas.","72 horas.","5 dias."],"B",
  "Art. 310: o juiz decide relaxar a prisão ilegal, convertê-la em preventiva ou conceder liberdade provisória.","Custódia: 24 horas."),
 ("Procedimento","O procedimento comum ordinário aplica-se quando o crime tiver sanção máxima cominada:",
  ["inferior a 2 anos.","inferior a 4 anos.","igual ou superior a 4 anos.","de até 1 ano.","apenas de multa."],"C",
  "Art. 394, § 1º: ordinário (≥ 4 anos), sumário (&lt; 4 anos), sumaríssimo (menor potencial ofensivo).","Ordinário: 4 anos ou mais.")]
questoes(Q, "CDBAEBCBDAECBDABCEACBDAE")
respostas_treinos()

referencias('''<h3>Legislação consultada (portal do Planalto)</h3><ul>
<li>Código de Processo Penal (Decreto-Lei nº 3.689/1941), texto compilado: arts. 3º-A a 3º-F, 4º a 6º, 9º, 10, 12, 14-A, 16 a 18, 20, 24, 25, 28, 28-A, 29, 30, 38, 39, 41, 46, 48, 49, 51, 60, 155 a 158-C, 167, 197, 202, 206, 207, 226, 257, 261, 268, 301, 302, 304, 310 a 313, 394, 394-A, 396 e 400.</li>
<li>Alterações recentes identificadas nas notas: Leis nº 13.964/2019, 14.245/2021, 14.752/2023, 14.994/2024, 15.272/2025, 15.280/2025, 15.358/2026, 15.438/2026 e 15.487/2026.</li>
<li>Constituição Federal: art. 5º (XXXVII, LIII a LVII, LIX, LX, LXIII, LXXVIII), art. 93, IX, art. 129, I, e art. 144.</li>
<li>Citados sem conferência nesta edição: CPP, arts. 42, 301 e 397; Lei nº 9.099/1995; CP, arts. 147 e 236.</li></ul>
<h3>Jurisprudência citada (identificada em pesquisa)</h3><ul><li>STF: Súmula Vinculante 14; RE 593.727 (Tema 184, investigação pelo MP); ADIs 6.298, 6.299, 6.300 e 6.305 (juiz das garantias e Pacote Anticrime, 2023); RE 608.588 (Tema 656, guardas municipais). STJ: exigência do procedimento do art. 226 do CPP no reconhecimento de pessoas.</li></ul>''',
 'O Código de Processo Penal foi conferido no texto compilado do portal do Planalto, que exibe a redação vigente com as notas de alteração e de “Vide ADI”. <strong>Limitações:</strong> o texto compilado não informa a data da última atualização e não substitui o Diário Oficial; as notas “Vide ADI” não indicam o resultado dos julgamentos, e o alcance das decisões do STF sobre o Pacote Anticrime (juiz das garantias, arquivamento e art. 157, § 5º) está resumido, sem reprodução das teses. A classificação das espécies de flagrante, as características do inquérito e os princípios da ação penal são, em parte, <strong>construções doutrinárias</strong>. A jurisprudência citada foi identificada em pesquisa e não foi reconferida nos portais oficiais. Confira o edital do seu concurso.', DATA)
encerramento("13", "Direito Processual Penal", 'Sugestão de continuação: <strong>Caderno 14 · Direitos Humanos</strong>.')
gravar(HERE, "Mapa da Aprovação — Caderno 13 — Direito Processual Penal", Q)
