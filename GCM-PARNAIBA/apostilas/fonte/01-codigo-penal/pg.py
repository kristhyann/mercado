"""Apostila 01 · Código Penal · Parte Geral (Unidades 1 a 7).
Artigos conferidos no texto compilado do Planalto em 28/11/2026 (ver GCM-PARNAIBA/fontes/notas-de-verificacao.md)."""
from kit import *

def cp(a): return f"Art. {a} · Código Penal"

# ================================================================ UNIDADE 1
opener("01", "UNIDADE 1", "Introdução e princípios", ["O que é Direito Penal", "Crime e contravenção", "Princípios que caem na prova"], "U1")

add(topico('O que é <span class="hl">Direito Penal</span>', 'O ponto de partida para quem nunca estudou Direito.', "A01",
  p("É o ramo do Direito que define quais condutas são <strong>crimes</strong> e quais <strong>penas</strong> podem ser aplicadas a quem as pratica."),
  p("Pense no Direito Penal como a “última linha de defesa” da sociedade. Uma briga sobre uma dívida, por exemplo, se resolve na Justiça cível. Mas quando alguém mata, rouba ou desvia dinheiro público, o Estado entende que o problema é grave demais e usa a sua ferramenta mais forte: a pena."),
  "o principal texto é o <b>Código Penal</b> (Decreto-Lei nº 2.848/1940). A <b>Parte Geral</b> (arts. 1º a 120) traz as regras que valem para todos os crimes; a <b>Parte Especial</b> (art. 121 em diante) descreve cada crime e sua pena.",
  p("O art. 155 do Código Penal descreve o furto: “subtrair, para si ou para outrem, coisa alheia móvel”. Quem pega o celular de alguém em uma praça de Parnaíba e vai embora pratica a conduta descrita nesse artigo."),
  "questões costumam pedir a diferença entre Parte Geral (regras comuns) e Parte Especial (crimes em espécie).",
  "<ul><li><b>Errado:</b> “O Código Penal é uma lei ordinária comum de 1984.”</li><li><b>Certo:</b> é o Decreto-Lei nº 2.848/<b>1940</b>; em 1984 a Lei nº 7.209 reformou a Parte Geral.</li></ul>",
  "Código Penal = <strong>Decreto-Lei 2.848/1940</strong>. Parte Geral: arts. 1º a 120 (regras). Parte Especial: art. 121 em diante (crimes).", 1))

add(H(1, 'Crime e <span class="hl">contravenção</span>', 'As duas espécies de infração penal.', "A02") +
 oque(p("<strong>Infração penal</strong> é o gênero. Ela se divide em <strong>crime</strong> (mais grave) e <strong>contravenção penal</strong> (menos grave, chamada de “crime anão”).")) +
 NAO_CONFUNDA("Crime (ou delito)", "Contravenção penal", [
   ("Gravidade", "Maior", "Menor"),
   ("Pena de prisão", "Reclusão ou detenção", "Prisão simples"),
   ("Onde está", "Código Penal e leis especiais", "Principalmente na Lei das Contravenções Penais (Decreto-Lei nº 3.688/1941)"),
   ("Tentativa", "É punível (regra do art. 14)", "Não é punível (art. 4º da Lei das Contravenções)")]) +
 traduz(p("“Crime” e “delito” são sinônimos no Brasil. A diferença entre crime e contravenção está no <strong>tipo de pena</strong> que a lei prevê, e não no nome que a pessoa dá ao fato.")) +
 ATENCAO(p("A distinção pelo tipo de pena está no art. 1º da Lei de Introdução ao Código Penal (Decreto-Lei nº 3.914/1941). Para esta prova, foque nos <strong>crimes do Código Penal</strong>.")) +
 MEMORIZE("Infração penal = <strong>crime</strong> (reclusão/detenção) + <strong>contravenção</strong> (prisão simples). Crime e delito são sinônimos."))

add(H(1, 'Princípios que <span class="hl">caem na prova</span>', 'As regras de base que limitam o poder de punir.', "A03") +
 table(["Princípio", "O que significa", "Onde está"], [
  ["Legalidade (reserva legal)", "Só a <b>lei</b> pode criar crime e pena. Decreto, portaria ou costume não criam crime", "CF, art. 5º, XXXIX; CP, art. 1º"],
  ["Anterioridade", "A lei que cria o crime tem de existir <b>antes</b> do fato", "CF, art. 5º, XXXIX; CP, art. 1º"],
  ["Irretroatividade da lei mais grave", "A lei penal não retroage, <b>salvo para beneficiar</b> o réu", "CF, art. 5º, XL"],
  ["Intranscendência (pessoalidade)", "Nenhuma pena passa da pessoa do condenado", "CF, art. 5º, XLV"],
  ["Individualização da pena", "A pena é ajustada ao caso e à pessoa", "CF, art. 5º, XLVI"],
  ["Humanidade", "Proíbe penas de morte (salvo guerra declarada), perpétuas, de trabalhos forçados, de banimento e cruéis", "CF, art. 5º, XLVII"],
  ["Intervenção mínima", "O Direito Penal só atua quando os outros ramos não bastam", "Doutrina"],
  ["Insignificância (bagatela)", "Lesões ínfimas ao bem jurídico não são crime (afasta a tipicidade material)", "Jurisprudência do STF"]], ["26%", "50%", None]) +
 lei(cp("1º"), "<p>Não há crime sem lei anterior que o defina. Não há pena sem prévia cominação legal.</p>") +
 PEGADINHA("<ul><li><b>Errado:</b> “Medida provisória pode criar crime.” <b>Certo:</b> a CF proíbe medida provisória sobre direito penal (art. 62, § 1º, I, “b”).</li><li><b>Errado:</b> “A lei penal nunca retroage.” <b>Certo:</b> retroage para <b>beneficiar</b> o réu.</li></ul>"))

atencao(p("<strong>Princípio da insignificância.</strong> O STF exige, em conjunto, quatro vetores para reconhecê-lo: <b>mínima ofensividade</b> da conduta, <b>nenhuma periculosidade social</b> da ação, <b>reduzido grau de reprovabilidade</b> do comportamento e <b>inexpressividade da lesão</b> jurídica.") +
 EXEMPLO(p("Furto de um pacote de biscoitos de baixíssimo valor, sem violência, por pessoa sem histórico criminal: em tese, pode ser reconhecida a insignificância. Já o roubo, por envolver violência ou grave ameaça, não admite o princípio, segundo a jurisprudência dominante.")) +
 MEMORIZE("Insignificância: <strong>MÍNIMA</strong> ofensividade · <strong>NENHUMA</strong> periculosidade · <strong>REDUZIDA</strong> reprovabilidade · <strong>INEXPRESSIVA</strong> lesão."),
 ["Legalidade", "Anterioridade", "Retroatividade benéfica", "Insignificância"], "Princípios (continuação)")

treino(1, [
 ("O Código Penal brasileiro é o Decreto-Lei nº 2.848/1940.", "C", "A Lei nº 7.209/1984 reformou a Parte Geral."),
 ("Uma portaria do Ministério da Justiça pode criar um novo crime.", "E", "Só a lei cria crime (legalidade)."),
 ("A lei penal mais benéfica retroage para alcançar fatos anteriores.", "C", "CF, art. 5º, XL; CP, art. 2º, parágrafo único."),
 ("A pena de multa aplicada ao condenado pode ser cobrada de seus filhos após sua morte.", "E", "Intranscendência: a pena não passa da pessoa do condenado."),
 ("A tentativa de contravenção penal é punível.", "E", "Não é punível (Lei das Contravenções, art. 4º)."),
 ("Crime e delito são expressões sinônimas no Direito Penal brasileiro.", "C", "A outra espécie é a contravenção.")])

# ================================================================ UNIDADE 2
opener("02", "UNIDADE 2", "Aplicação da lei penal", ["Lei penal no tempo", "Tempo do crime", "Lugar do crime e territorialidade"], "U2")

add(topico('Lei penal no <span class="hl">tempo</span>', 'Arts. 2º e 3º: o que acontece quando a lei muda.', "A04",
  p("São as regras que dizem qual lei aplicar quando uma lei penal nova entra em vigor depois do fato."),
  p("Imagine que você fez algo que era crime e, depois, a lei deixou de considerar aquilo crime. A nova lei vale a seu favor. Mas se a lei nova piorar a situação (pena maior), ela não alcança o que você já fez."),
  (cp("2º"), "<p>Ninguém pode ser punido por fato que lei posterior deixa de considerar crime, cessando em virtude dela a execução e os efeitos penais da sentença condenatória. <b>Parágrafo único:</b> a lei posterior que de qualquer modo favorecer o agente aplica-se aos fatos anteriores, ainda que decididos por sentença condenatória transitada em julgado.</p>"),
  p("João foi condenado por um fato que uma lei nova deixou de considerar crime (<i>abolitio criminis</i>). A execução da pena cessa, mesmo que a condenação já fosse definitiva."),
  "a banca troca “lei mais benéfica” por “lei mais grave” ou diz que a retroatividade não alcança a sentença transitada em julgado.",
  "<ul><li><b>Errado:</b> “A lei mais benéfica não alcança condenação definitiva.” <b>Certo:</b> alcança, mesmo após o trânsito em julgado.</li><li><b>Errado:</b> “A lei temporária deixa de ser aplicada aos fatos ocorridos durante sua vigência quando ela termina.” <b>Certo:</b> continua aplicável a esses fatos (art. 3º).</li></ul>",
  "Lei nova <strong>melhor</strong> = retroage (até após o trânsito em julgado). Lei nova <strong>pior</strong> = não retroage. <strong>Abolitio criminis</strong> = o fato deixa de ser crime.", 2))

add(H(2, 'Tempo e lugar do <span class="hl">crime</span>', 'Arts. 4º, 5º e 6º: quando e onde o crime aconteceu.', "A05") +
 oque(p("Regras para saber <strong>em que momento</strong> e <strong>em que lugar</strong> se considera praticado o crime. Isso define, por exemplo, se o agente era menor de idade e se a lei brasileira se aplica.")) +
 lei(cp("4º"), "<p>Considera-se praticado o crime no momento da ação ou omissão, ainda que outro seja o momento do resultado.</p>") +
 lei(cp("6º"), "<p>Considera-se praticado o crime no lugar em que ocorreu a ação ou omissão, no todo ou em parte, bem como onde se produziu ou deveria produzir-se o resultado.</p>") +
 NAO_CONFUNDA("TEMPO do crime (art. 4º)", "LUGAR do crime (art. 6º)", [
   ("Teoria", "Da <b>atividade</b>: momento da conduta", "Da <b>ubiquidade</b>: conduta OU resultado"),
   ("Exemplo", "Tiro dado aos 17 anos; vítima morre quando o autor já tem 18: o agente era menor (inimputável)", "Disparo em Parnaíba e morte em outro Estado ou país: os dois lugares são “lugar do crime”")]) +
 MEMORIZE("<strong>LUTA</strong>: <strong>L</strong>ugar = <strong>U</strong>biquidade · <strong>T</strong>empo = <strong>A</strong>tividade."))

atencao(table(["Regra", "Conteúdo (art. 5º)"], [
  ["Territorialidade (caput)", "Aplica-se a lei brasileira ao crime cometido no território nacional, sem prejuízo de convenções, tratados e regras de direito internacional"],
  ["Território por extensão (§ 1º)", "Embarcações e aeronaves brasileiras <b>públicas ou a serviço do governo</b>, onde quer que estejam; e as <b>mercantes ou de propriedade privada</b>, no espaço aéreo correspondente ou em alto-mar"],
  ["§ 2º", "Também se aplica a lei brasileira aos crimes a bordo de aeronaves ou embarcações estrangeiras privadas em pouso ou voo no espaço aéreo nacional, ou em porto ou mar territorial do Brasil"]], ["28%", None]) +
 PEGADINHA("<ul><li><b>Errado:</b> “Navio privado brasileiro é território brasileiro em qualquer lugar, até em porto estrangeiro.” <b>Certo:</b> o privado só é extensão do território no espaço correspondente ou em <b>alto-mar</b>.</li></ul>") +
 p("O Código ainda prevê casos de <strong>extraterritorialidade</strong> (art. 7º), em que a lei brasileira alcança crimes cometidos fora do país, como os crimes contra a vida ou a liberdade do Presidente da República. Para a prova da GCM, basta saber que essa exceção existe."),
 ["Territorialidade", "Atividade", "Ubiquidade"], "Territorialidade (art. 5º)")

treino(2, [
 ("Considera-se praticado o crime no momento do resultado, ainda que outro seja o momento da ação.", "E", "Momento da ação ou omissão (atividade, art. 4º)."),
 ("Para o lugar do crime, o Código Penal adota a teoria da ubiquidade.", "C", "Art. 6º: conduta ou resultado."),
 ("A lei posterior que favorece o agente aplica-se aos fatos anteriores, ainda que decididos por sentença transitada em julgado.", "C", "Art. 2º, parágrafo único."),
 ("A lei temporária deixa de ser aplicada aos fatos praticados durante sua vigência após o término de seu prazo.", "E", "Art. 3º: continua aplicável a esses fatos."),
 ("Aeronave pública brasileira é considerada extensão do território nacional onde quer que se encontre.", "C", "Art. 5º, § 1º."),
 ("A abolitio criminis faz cessar a execução e os efeitos penais da sentença condenatória.", "C", "Art. 2º, caput.")])

# ================================================================ UNIDADE 3
opener("03", "UNIDADE 3", "Teoria do crime", ["Conceito analítico de crime", "Fato típico e nexo causal", "Omissão relevante", "Dolo e culpa", "Erro de tipo"], "U3")

def escada():
    s = f'<figure><svg viewBox="0 0 640 205" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    itens = [("1. FATO TÍPICO", "conduta · resultado", "nexo · tipicidade", C['blue'], C['sky']), ("2. ILICITUDE", "contrário ao direito,", "sem excludente", C['golddeep'], C['goldsoft']), ("3. CULPABILIDADE", "imputabilidade · consciência", "da ilicitude · exigibilidade", C['red'], C['redsoft'])]
    for i, (t, a, b, fg, bg) in enumerate(itens):
        x = 20 + i * 205; hh = 72 + i * 34; y = 172 - hh
        s += f'<rect x="{x}" y="{y}" width="190" height="{hh}" rx="12" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x+95}" y="{y+26}" text-anchor="middle" font-size="13" font-weight="900" fill="{fg}">{t}</text><text x="{x+95}" y="{y+46}" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">{a}</text><text x="{x+95}" y="{y+61}" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">{b}</text>'
    s += f'<text x="320" y="196" text-anchor="middle" font-size="11.5" font-weight="800" fill="{C["navy"]}">Faltou um degrau? Não há crime (ou o agente fica isento de pena).</text>'
    return s + '</svg><figcaption>Conceito analítico (tripartite) de crime: os três degraus.</figcaption></figure>'

add(H(3, 'Conceito analítico de <span class="hl">crime</span>', 'Os três “degraus” que todo crime precisa subir.', "A06") +
 oque(p("Pelo conceito analítico adotado pela maioria da doutrina (teoria <strong>tripartite</strong>), crime é o <strong>fato típico</strong>, <strong>ilícito</strong> (antijurídico) e <strong>culpável</strong>.")) +
 escada() +
 traduz(p("Para condenar alguém, o juiz verifica em ordem: 1) o fato está descrito em lei como crime? 2) ele é contrário ao direito, ou havia uma justificativa, como a legítima defesa? 3) a pessoa podia ser censurada (era maior de idade, sabia que era errado)?")) +
 table(["Se faltar…", "Consequência", "Exemplos"], [
  ["Fato típico", "Não há crime", "Fato não previsto em lei; ausência de dolo e culpa; insignificância"],
  ["Ilicitude", "Não há crime (excludentes do art. 23)", "Legítima defesa, estado de necessidade"],
  ["Culpabilidade", "O agente fica <b>isento de pena</b>", "Menor de 18 anos; doença mental; coação moral irresistível"]], ["22%", "34%", None]) +
 MEMORIZE("Crime = fato <strong>TÍPICO</strong> + <strong>ILÍCITO</strong> + <strong>CULPÁVEL</strong>."))

add(topico('Fato típico e <span class="hl">nexo causal</span>', 'Art. 13: conduta, resultado, nexo e tipicidade.', "A07",
  p("Fato típico é o comportamento humano que se encaixa na descrição de um crime prevista em lei."),
  p("Seus elementos são: <strong>conduta</strong> (ação ou omissão humana, com dolo ou culpa), <strong>resultado</strong> (nos crimes que exigem resultado), <strong>nexo causal</strong> (a ligação entre a conduta e o resultado) e <strong>tipicidade</strong> (o encaixe do fato na lei)."),
  (cp("13, caput"), "<p>O resultado, de que depende a existência do crime, somente é imputável a quem lhe deu causa. Considera-se causa a ação ou omissão sem a qual o resultado não teria ocorrido.</p>"),
  p("A atira em B, que é levado de ambulância. No caminho, a ambulância sofre um acidente e B morre por causa do acidente. Pelo § 1º do art. 13 (causa superveniente relativamente independente que, por si só, produziu o resultado), A responde pela tentativa, e não pelo homicídio consumado."),
  "a banca pede o conceito de causa (conduta sem a qual o resultado não teria ocorrido) ou um caso como o da ambulância.",
  "<ul><li><b>Errado:</b> “Na causa superveniente relativamente independente que por si só produziu o resultado, o agente responde pelo resultado final.” <b>Certo:</b> a imputação é excluída; os fatos anteriores são imputados a quem os praticou.</li></ul>",
  "Fato típico: <strong>conduta · resultado · nexo causal · tipicidade</strong>. Causa = aquilo sem o qual o resultado não teria ocorrido.", 3))

add(topico('Omissão <span class="hl">relevante</span>', 'Art. 13, § 2º: quando “não fazer” é crime.', "A08",
  p("É a situação em que a pessoa responde pelo resultado porque <strong>devia e podia agir</strong> para evitá-lo, e não agiu."),
  p("Em regra, ninguém é obrigado a ser herói. Mas algumas pessoas têm um dever especial de proteger. Se elas cruzam os braços, respondem como se tivessem causado o resultado."),
  (cp("13, § 2º"), "<p>A omissão é penalmente relevante quando o omitente devia e podia agir para evitar o resultado. O dever de agir incumbe a quem: <b>a)</b> tenha por lei obrigação de cuidado, proteção ou vigilância; <b>b)</b> de outra forma, assumiu a responsabilidade de impedir o resultado; <b>c)</b> com seu comportamento anterior, criou o risco da ocorrência do resultado.</p>"),
  p("A mãe que deixa, de propósito, de alimentar o filho bebê responde pelo resultado (dever legal de cuidado). O salva-vidas contratado que vê alguém se afogando e nada faz também responde (assumiu a responsabilidade)."),
  "a banca lista as três hipóteses de dever de agir e troca uma delas por “qualquer pessoa que presencie o fato”.",
  "<ul><li><b>Errado:</b> “Qualquer pessoa que presencie um acidente e não ajude responde pelo resultado morte.” <b>Certo:</b> sem o dever especial, ela pode responder por omissão de socorro (art. 135), não pelo resultado.</li></ul>",
  "Dever de agir: <strong>LEI</strong> (cuidado, proteção, vigilância) · <strong>ASSUMIU</strong> a responsabilidade · <strong>CRIOU O RISCO</strong>. É preciso <strong>dever + poder</strong> agir.", 3))

add(topico('Dolo e <span class="hl">culpa</span>', 'Art. 18: querer o resultado ou ser descuidado.', "A09",
  p("<strong>Dolo</strong> é querer o resultado ou assumir o risco de produzi-lo. <strong>Culpa</strong> é causar o resultado por descuido: imprudência, negligência ou imperícia."),
  p("Dolo é “eu quis” ou “eu não liguei se acontecesse”. Culpa é “eu não quis, mas fui descuidado”. Importante: em regra, só existe crime doloso; o crime culposo só existe quando a lei prevê expressamente."),
  (cp("18"), "<p>Diz-se o crime: I – doloso, quando o agente quis o resultado ou assumiu o risco de produzi-lo; II – culposo, quando o agente deu causa ao resultado por imprudência, negligência ou imperícia. <b>Parágrafo único:</b> salvo os casos expressos em lei, ninguém pode ser punido por fato previsto como crime, senão quando o pratica dolosamente.</p>"),
  p("Não existe “dano culposo” no Código Penal: quem quebra sem querer a vidraça da escola municipal não comete crime de dano, embora possa ter de indenizar."),
  "a banca troca dolo eventual (assumiu o risco) por culpa consciente (acreditou que não aconteceria) ou cobra o caráter excepcional do crime culposo.",
  "<ul><li><b>Errado:</b> “Todo crime admite a forma culposa.” <b>Certo:</b> só quando a lei prevê expressamente (art. 18, parágrafo único).</li></ul>",
  "Dolo: <strong>quis</strong> (direto) ou <strong>assumiu o risco</strong> (eventual). Culpa: <strong>imprudência</strong> (fez o que não devia), <strong>negligência</strong> (deixou de fazer), <strong>imperícia</strong> (falta de técnica). Culposo só se a lei disser.", 3))

atencao(NAO_CONFUNDA("Dolo eventual", "Culpa consciente", [
   ("O agente prevê o resultado?", "Sim", "Sim"),
   ("Atitude diante do resultado", "Aceita: “se acontecer, tanto faz”", "Confia que não vai acontecer"),
   ("Responde por", "Crime doloso", "Crime culposo (se previsto em lei)")]) +
 table(["Modalidade de culpa", "O que é", "Exemplo"], [
  ["Imprudência", "Agir de forma precipitada, sem cautela (ação)", "Dirigir em alta velocidade perto de escola"],
  ["Negligência", "Deixar de tomar o cuidado devido (omissão)", "Deixar arma carregada ao alcance de criança"],
  ["Imperícia", "Falta de aptidão técnica em arte, ofício ou profissão", "Profissional que executa procedimento sem saber a técnica"]], ["22%", "40%", None]) +
 p("<strong>Crime preterdoloso:</strong> dolo na conduta inicial e culpa no resultado mais grave. O art. 19 diz que, pelo resultado que agrava especialmente a pena, só responde o agente que o houver causado ao menos culposamente. Exemplo: lesão corporal seguida de morte (art. 129, § 3º)."),
 ["Dolo direto e eventual", "Culpa consciente", "Preterdolo"], "Dolo e culpa (continuação)")

add(topico('Erro de <span class="hl">tipo</span>', 'Art. 20: errar sobre o que está fazendo.', "A10",
  p("É o engano sobre um elemento do próprio crime: a pessoa não sabe que está praticando a conduta descrita na lei."),
  p("Quem leva da academia a mochila de outra pessoa, achando que era a sua (idêntica), não “quer subtrair coisa alheia”: falta o dolo de furtar."),
  (cp("20, caput"), "<p>O erro sobre elemento constitutivo do tipo legal de crime exclui o dolo, mas permite a punição por crime culposo, se previsto em lei.</p>"),
  p("No exemplo da mochila, como não existe furto culposo, o fato não é crime. Já o caçador que atira em um arbusto achando que era um animal e atinge uma pessoa pode responder por homicídio <b>culposo</b>, se o erro era evitável."),
  "a banca confunde erro de tipo (sobre o fato) com erro de proibição (sobre a lei, art. 21).",
  "<ul><li><b>Errado:</b> “O erro de tipo sempre isenta de pena.” <b>Certo:</b> exclui o dolo; pode restar crime culposo, se houver previsão legal.</li><li>No erro sobre a pessoa (§ 3º), consideram-se as qualidades da vítima <b>visada</b>, não as da atingida.</li></ul>",
  "Erro de <strong>TIPO</strong> = erro sobre o <strong>FATO</strong> → exclui o dolo. Erro de <strong>PROIBIÇÃO</strong> = erro sobre a <strong>ILICITUDE</strong> → atinge a culpabilidade.", 3))

treino(3, [
 ("Pela teoria tripartite, crime é fato típico, ilícito e culpável.", "C", "Conceito analítico."),
 ("Considera-se causa a ação ou omissão sem a qual o resultado não teria ocorrido.", "C", "Art. 13, caput."),
 ("Qualquer pessoa que presencie um crime tem o dever jurídico de impedir o resultado, sob pena de responder por ele.", "E", "O dever de agir é restrito às hipóteses do art. 13, § 2º."),
 ("Age com dolo eventual quem assume o risco de produzir o resultado.", "C", "Art. 18, I."),
 ("Todo crime admite a forma culposa.", "E", "Só nos casos expressos em lei."),
 ("O erro de tipo exclui o dolo, mas permite a punição a título de culpa, se previsto em lei.", "C", "Art. 20, caput.")])

# ================================================================ UNIDADE 4
opener("04", "UNIDADE 4", "Consumação, tentativa e arrependimentos", ["Iter criminis", "Consumação e tentativa", "Desistência voluntária e arrependimento eficaz", "Arrependimento posterior", "Crime impossível"], "U4")

def iter_crim():
    s = f'<figure><svg viewBox="0 0 640 150" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">{arrowdefs("it")}'
    fases = [("COGITAÇÃO", "pensar", "não punível", C['muted']), ("PREPARAÇÃO", "comprar a arma", "em regra, não punível", C['muted']), ("EXECUÇÃO", "começa o ataque", "tentativa já punível", C['golddeep']), ("CONSUMAÇÃO", "todos os elementos", "crime consumado", C['red'])]
    for i, (t, a, b, c) in enumerate(fases):
        x = 10 + i * 158
        s += f'<rect x="{x}" y="20" width="140" height="80" rx="12" fill="#fff" stroke="{c}" stroke-width="2.6"/><text x="{x+70}" y="46" text-anchor="middle" font-size="12" font-weight="900" fill="{c}">{t}</text><text x="{x+70}" y="66" text-anchor="middle" font-size="10" fill="{C["ink"]}">{a}</text><text x="{x+70}" y="84" text-anchor="middle" font-size="10" font-weight="800" fill="{C["ink"]}">{b}</text>'
        if i < 3: s += f'<line x1="{x+142}" y1="60" x2="{x+156}" y2="60" stroke="{C["ink"]}" stroke-width="2.5" marker-end="url(#it)"/>'
    s += f'<text x="320" y="132" text-anchor="middle" font-size="11" font-weight="800" fill="{C["navy"]}">Iter criminis: o “caminho do crime”. A punição começa, em regra, quando se inicia a execução.</text>'
    return s + '</svg><figcaption>As fases do crime.</figcaption></figure>'

add(topico('Consumação e <span class="hl">tentativa</span>', 'Art. 14: quando o crime se completa e quando para no meio.', "A11",
  p("O crime está <strong>consumado</strong> quando reúne todos os elementos da sua definição legal. É <strong>tentado</strong> quando, iniciada a execução, não se consuma por circunstâncias <strong>alheias à vontade</strong> do agente."),
  p("Na tentativa, a pessoa quer chegar ao fim, mas algo externo a impede: a vítima foge, a polícia chega, a arma falha."),
  (cp("14"), "<p>Diz-se o crime: I – consumado, quando nele se reúnem todos os elementos de sua definição legal; II – tentado, quando, iniciada a execução, não se consuma por circunstâncias alheias à vontade do agente. <b>Parágrafo único:</b> salvo disposição em contrário, pune-se a tentativa com a pena correspondente ao crime consumado, diminuída de um a dois terços.</p>"),
  p("Durante a ronda, a equipe da GCM flagra um homem tentando arrombar a porta de uma loja na feira. Ele foge sem levar nada: houve tentativa de furto, porque a execução começou e foi interrompida pela chegada da guarda."),
  "pergunta-se a fração de redução (1/3 a 2/3) ou se apresenta um caso para identificar tentativa, desistência ou arrependimento.",
  "<ul><li><b>Errado:</b> “A tentativa é punida com a pena do crime consumado reduzida de um sexto a um terço.” <b>Certo:</b> de <b>um a dois terços</b>.</li><li>Planejar e comprar a ferramenta (preparação), em regra, não é punível.</li></ul>",
  "Tentativa: <strong>começou + não terminou por fator EXTERNO</strong>. Redução de <strong>1/3 a 2/3</strong>.", 4))

add(topico('Desistência voluntária e <span class="hl">arrependimento eficaz</span>', 'Art. 15: a “ponte de ouro”.', "A12",
  p("São situações em que o próprio agente, <strong>por vontade própria</strong>, impede a consumação do crime. Ele só responde pelo que já fez."),
  p("Na <strong>desistência voluntária</strong>, a pessoa para no meio da execução (“posso continuar, mas não quero”). No <strong>arrependimento eficaz</strong>, ela termina a execução, mas depois age para evitar o resultado e consegue."),
  (cp("15"), "<p>O agente que, voluntariamente, desiste de prosseguir na execução ou impede que o resultado se produza, só responde pelos atos já praticados.</p>"),
  p("<b>Desistência:</b> o ladrão entra na casa, vê fotos de crianças e vai embora sem levar nada: responde só pela violação de domicílio. <b>Arrependimento eficaz:</b> alguém dá veneno à vítima e, arrependido, leva-a ao hospital, onde ela é salva: responde pela lesão corporal, não por tentativa de homicídio."),
  "a banca compara com a tentativa: a diferença está em QUEM impediu a consumação (o próprio agente ou um fator externo).",
  "<ul><li><b>Errado:</b> “No arrependimento eficaz, o agente responde por tentativa com pena reduzida.” <b>Certo:</b> responde só pelos atos já praticados.</li><li>Se o resultado acontece mesmo assim, o arrependimento <b>não</b> foi eficaz.</li></ul>",
  "Desistência = <strong>para a execução</strong>. Arrependimento eficaz = <strong>terminou, mas impediu o resultado</strong>. Nos dois: responde <strong>só pelos atos já praticados</strong>.", 4))

atencao(iter_crim() + NAO_CONFUNDA("Tentativa (art. 14, II)", "Desistência e arrependimento eficaz (art. 15)", [
   ("Por que não consumou?", "Circunstância <b>alheia</b> à vontade do agente", "<b>Vontade</b> do próprio agente"),
   ("Responde por", "Tentativa (pena reduzida de 1/3 a 2/3)", "Só pelos atos já praticados"),
   ("Frase-teste", "“Quero, mas não posso”", "“Posso, mas não quero”")]) +
 MEMORIZE("Teste de Frank: <strong>“quero, mas não posso”</strong> = tentativa · <strong>“posso, mas não quero”</strong> = desistência."),
 ["Fator externo", "Vontade própria"], "Não confunda: tentativa x desistência")

add(topico('Arrependimento <span class="hl">posterior</span>', 'Art. 16: reparar o dano depois do crime.', "A13",
  p("É a redução de pena para quem, depois de consumado o crime sem violência ou grave ameaça, repara o dano ou devolve a coisa voluntariamente, até o recebimento da denúncia ou queixa."),
  p("O crime já aconteceu (por isso “posterior”). A lei premia quem devolve o que levou antes de o processo começar."),
  (cp("16"), "<p>Nos crimes cometidos sem violência ou grave ameaça à pessoa, reparado o dano ou restituída a coisa, até o recebimento da denúncia ou da queixa, por ato voluntário do agente, a pena será reduzida de um a dois terços.</p>"),
  p("Uma pessoa furta uma bicicleta e, arrependida, devolve-a ao dono antes de o juiz receber a denúncia: terá a pena reduzida. No roubo isso não se aplica, porque há violência ou grave ameaça."),
  "a banca muda o prazo (“até a sentença”) ou aplica a regra ao roubo.",
  "<ul><li><b>Errado:</b> “Cabe arrependimento posterior até a sentença.” <b>Certo:</b> até o <b>recebimento</b> da denúncia ou queixa.</li><li><b>Errado:</b> “O arrependimento posterior extingue o crime.” <b>Certo:</b> apenas <b>reduz</b> a pena.</li></ul>",
  "Arrependimento posterior: <strong>sem violência ou grave ameaça</strong> + <strong>reparou ou restituiu</strong> + <strong>voluntário</strong> + <strong>até o recebimento da denúncia</strong> → reduz de <strong>1/3 a 2/3</strong>.", 4))

add(topico('Crime <span class="hl">impossível</span>', 'Art. 17: quando consumar era impossível desde o início.', "A14",
  p("É a tentativa que não é punida porque, pelo meio usado ou pelo objeto escolhido, era <strong>absolutamente impossível</strong> consumar o crime."),
  p("Atirar com uma arma de brinquedo para matar alguém, ou “matar” uma pessoa que já estava morta: o crime nunca poderia acontecer."),
  (cp("17"), "<p>Não se pune a tentativa quando, por ineficácia absoluta do meio ou por absoluta impropriedade do objeto, é impossível consumar-se o crime.</p>"),
  p("<b>Meio absolutamente ineficaz:</b> tentar envenenar alguém com açúcar. <b>Objeto absolutamente impróprio:</b> tentar abortar quando a mulher não está grávida."),
  "a banca troca “absoluta” por “relativa”: se a ineficácia é apenas relativa (a arma às vezes funciona), há tentativa punível.",
  "<ul><li><b>Errado:</b> “Arma que falhou por defeito eventual caracteriza crime impossível.” <b>Certo:</b> ineficácia <b>relativa</b> gera tentativa punível.</li></ul>",
  "Crime impossível: ineficácia <strong>ABSOLUTA</strong> do meio ou impropriedade <strong>ABSOLUTA</strong> do objeto → tentativa <strong>não punível</strong>.", 4))

treino(4, [
 ("Pune-se a tentativa, salvo disposição em contrário, com a pena do crime consumado diminuída de um a dois terços.", "C", "Art. 14, parágrafo único."),
 ("Na desistência voluntária, o agente responde por tentativa.", "E", "Responde só pelos atos já praticados (art. 15)."),
 ("No arrependimento eficaz, o agente, após encerrar a execução, impede que o resultado se produza.", "C", "Art. 15."),
 ("O arrependimento posterior aplica-se ao crime de roubo, desde que a coisa seja devolvida.", "E", "Só nos crimes sem violência ou grave ameaça."),
 ("O arrependimento posterior pode ocorrer até a sentença de primeiro grau.", "E", "Até o recebimento da denúncia ou queixa."),
 ("Não se pune a tentativa quando, por ineficácia absoluta do meio, é impossível consumar-se o crime.", "C", "Art. 17.")])

# ================================================================ UNIDADE 5
opener("05", "UNIDADE 5", "Excludentes de ilicitude", ["As quatro excludentes", "Estado de necessidade", "Legítima defesa", "Estrito cumprimento e exercício regular"], "U5")

add(H(5, 'As quatro <span class="hl">excludentes</span>', 'Art. 23: quando o fato típico não é crime.', "A15") +
 oque(p("São situações previstas em lei em que a conduta, embora descrita como crime, é <strong>permitida pelo Direito</strong>. Por isso, não há crime.")) +
 lei(cp("23"), "<p>Não há crime quando o agente pratica o fato: I – em estado de necessidade; II – em legítima defesa; III – em estrito cumprimento de dever legal ou no exercício regular de direito. <b>Parágrafo único:</b> o agente, em qualquer das hipóteses deste artigo, responderá pelo excesso doloso ou culposo.</p>") +
 PEGADINHA("<ul><li><b>Errado:</b> “Quem age em legítima defesa nunca responde por nada.” <b>Certo:</b> responde pelo <b>excesso</b> doloso ou culposo.</li></ul>") +
 MEMORIZE("Excludentes: <strong>NE-LE-ES-EX</strong> (necessidade, legítima defesa, estrito cumprimento, exercício regular). Excesso: <strong>responde</strong>."))

add(topico('Estado de <span class="hl">necessidade</span>', 'Art. 24: sacrificar um bem para salvar outro.', "A16",
  p("É sacrificar um bem jurídico para salvar outro de um <strong>perigo atual</strong>, que o agente não provocou por vontade própria e não podia evitar de outro modo."),
  p("Não há um “agressor”: há um <strong>perigo</strong> (incêndio, naufrágio, animal solto). Para se salvar ou salvar alguém, a pessoa causa um dano a outro bem."),
  (cp("24"), "<p>Considera-se em estado de necessidade quem pratica o fato para salvar de perigo atual, que não provocou por sua vontade, nem podia de outro modo evitar, direito próprio ou alheio, cujo sacrifício, nas circunstâncias, não era razoável exigir-se. <b>§ 1º</b> Não pode alegar estado de necessidade quem tinha o dever legal de enfrentar o perigo.</p>"),
  p("Durante um incêndio, uma pessoa arromba a porta da casa do vizinho para salvar uma criança presa lá dentro: o dano à porta está justificado pelo estado de necessidade."),
  "a banca troca “perigo” por “agressão” (o que seria legítima defesa) ou omite a regra do dever legal de enfrentar o perigo.",
  "<ul><li><b>Errado:</b> “O bombeiro pode alegar estado de necessidade para não entrar no prédio em chamas.” <b>Certo:</b> quem tem o <b>dever legal</b> de enfrentar o perigo não pode alegá-lo (§ 1º).</li></ul>",
  "Estado de necessidade = <strong>PERIGO atual</strong>, não provocado, inevitável. Quem tem <strong>dever legal</strong> de enfrentar o perigo não pode alegar.", 5))

add(topico('Legítima <span class="hl">defesa</span>', 'Art. 25: repelir uma agressão injusta.', "A17",
  p("É usar moderadamente os meios necessários para repelir uma <strong>injusta agressão</strong>, atual ou iminente, a direito próprio ou de terceiro."),
  p("Aqui existe um agressor. Você pode se defender (ou defender outra pessoa), mas com moderação: o necessário para fazer a agressão parar."),
  (cp("25"), "<p>Entende-se em legítima defesa quem, usando moderadamente dos meios necessários, repele injusta agressão, atual ou iminente, a direito seu ou de outrem. <b>Parágrafo único</b> (Lei nº 13.964/2019): observados os requisitos do caput, considera-se também em legítima defesa o agente de segurança pública que repele agressão ou risco de agressão a vítima mantida refém durante a prática de crimes.</p>"),
  p("Um homem ataca uma mulher com uma faca na praça. Um guarda municipal intervém e o imobiliza, usando a força necessária para cessar a agressão: legítima defesa de terceiro."),
  "a banca pede os requisitos (injusta agressão, atual ou iminente, meios necessários, moderação) ou testa a agressão passada (vingança não é legítima defesa).",
  "<ul><li><b>Errado:</b> “Cabe legítima defesa contra agressão já encerrada.” <b>Certo:</b> a agressão deve ser <b>atual ou iminente</b>; depois disso é vingança.</li><li><b>Errado:</b> “Só se admite legítima defesa de direito próprio.” <b>Certo:</b> também de direito <b>de outrem</b>.</li></ul>",
  "Legítima defesa: <strong>injusta AGRESSÃO</strong> + <strong>atual ou iminente</strong> + direito próprio ou alheio + <strong>meios necessários</strong> + <strong>moderação</strong>.", 5))

atencao(NAO_CONFUNDA("Legítima defesa", "Estado de necessidade", [
   ("Situação", "<b>Agressão</b> humana injusta", "<b>Perigo</b> atual (natureza, animal, acidente…)"),
   ("Atual ou iminente?", "Agressão <b>atual ou iminente</b>", "Perigo <b>atual</b>"),
   ("Quem é atingido", "O agressor", "Pode ser um terceiro inocente"),
   ("Exemplo", "Defender-se de um assaltante armado", "Arrombar uma porta para fugir de um incêndio")]) +
 table(["Excludente", "O que é", "Exemplo no serviço público"], [
  ["Estrito cumprimento de dever legal", "Agir exatamente como a lei obriga, sem excessos", "Oficial de justiça que cumpre ordem judicial de busca e apreensão; agente que realiza prisão em flagrante dentro da lei"],
  ["Exercício regular de direito", "Exercer um direito previsto no ordenamento, dentro dos limites", "Qualquer pessoa do povo que prende alguém em flagrante (CPP, art. 301); esportes violentos dentro das regras"]], ["28%", "34%", None]) +
 PEGADINHA("<ul><li>O <b>excesso</b> em qualquer excludente é punível (art. 23, parágrafo único). Ex.: continuar agredindo o agressor já desmaiado.</li></ul>"),
 ["Agressão x perigo", "Excesso punível", "Dever legal"], "Não confunda: as excludentes")

treino(5, [
 ("Não há crime quando o agente pratica o fato em estrito cumprimento de dever legal.", "C", "Art. 23, III."),
 ("Quem age em legítima defesa não responde pelo excesso, ainda que doloso.", "E", "Responde pelo excesso doloso ou culposo."),
 ("Pode alegar estado de necessidade quem tinha o dever legal de enfrentar o perigo.", "E", "Art. 24, § 1º."),
 ("A legítima defesa exige injusta agressão, atual ou iminente.", "C", "Art. 25."),
 ("O agente de segurança pública que repele agressão a vítima mantida refém também é considerado em legítima defesa, observados os requisitos legais.", "C", "Art. 25, parágrafo único (Lei 13.964/2019)."),
 ("No estado de necessidade há sempre um agressor humano.", "E", "Há um perigo atual; a agressão é típica da legítima defesa.")])

# ================================================================ UNIDADE 6
opener("06", "UNIDADE 6", "Culpabilidade e imputabilidade", ["Elementos da culpabilidade", "Imputabilidade", "Emoção, paixão e embriaguez", "Erro de proibição, coação e obediência"], "U6")

add(H(6, 'Elementos da <span class="hl">culpabilidade</span>', 'O terceiro degrau: a pessoa pode ser censurada?', "A18") +
 oque(p("Culpabilidade é o <strong>juízo de reprovação</strong> sobre o autor do fato típico e ilícito. Sem ela, o agente fica <strong>isento de pena</strong>.")) +
 table(["Elemento", "Pergunta", "Se faltar (exemplos)"], [
  ["Imputabilidade", "A pessoa tinha capacidade de entender e de se determinar?", "Menor de 18 anos; doença mental (art. 26); embriaguez completa por caso fortuito (art. 28, § 1º)"],
  ["Potencial consciência da ilicitude", "Ela podia saber que aquilo era proibido?", "Erro de proibição inevitável (art. 21)"],
  ["Exigibilidade de conduta diversa", "Dava para exigir que agisse de outro modo?", "Coação moral irresistível; obediência a ordem não manifestamente ilegal (art. 22)"]], ["26%", "34%", None]) +
 traduz(p("Para lembrar: a culpabilidade pergunta se a pessoa <strong>podia entender</strong> (imputabilidade), se <strong>podia saber</strong> que era errado (consciência) e se <strong>podia agir diferente</strong> (exigibilidade).")) +
 MEMORIZE("Culpabilidade: <strong>IMPUTABILIDADE</strong> + <strong>POTENCIAL CONSCIÊNCIA DA ILICITUDE</strong> + <strong>EXIGIBILIDADE DE CONDUTA DIVERSA</strong>."))

add(topico('Imputa<span class="hl">bilidade</span>', 'Arts. 26 e 27: doença mental e menoridade.', "A19",
  p("É a capacidade de entender que o fato é ilícito e de se comportar de acordo com esse entendimento."),
  p("O Código usa o critério <strong>biopsicológico</strong> para a doença mental: não basta ter a doença; é preciso que ela tire do agente, no momento do fato, a capacidade de entender ou de se controlar. Para os menores de 18 anos, o critério é só a idade."),
  (cp("26 e 27"), "<p><b>Art. 26.</b> É isento de pena o agente que, por doença mental ou desenvolvimento mental incompleto ou retardado, era, ao tempo da ação ou da omissão, inteiramente incapaz de entender o caráter ilícito do fato ou de determinar-se de acordo com esse entendimento. <b>Parágrafo único:</b> a pena pode ser reduzida de um a dois terços se o agente não era inteiramente capaz. <b>Art. 27.</b> Os menores de 18 anos são penalmente inimputáveis, ficando sujeitos às normas estabelecidas na legislação especial.</p>"),
  p("Um adolescente de 16 anos que pratica um roubo não comete crime no sentido penal: comete <b>ato infracional</b> e responde pelo Estatuto da Criança e do Adolescente (Lei nº 8.069/1990)."),
  "a banca troca a fração do semi-imputável ou afirma que o menor de 18 anos “responde pelo Código Penal com pena reduzida”.",
  "<ul><li><b>Errado:</b> “O semi-imputável é isento de pena.” <b>Certo:</b> tem a pena <b>reduzida</b> de 1/3 a 2/3.</li><li>A idade é verificada no <b>momento da conduta</b> (art. 4º), não no do resultado.</li></ul>",
  "Inimputável (inteiramente incapaz) = <strong>isento de pena</strong>. Semi-imputável = pena <strong>reduzida de 1/3 a 2/3</strong>. Menor de 18 = inimputável (ECA).", 6))

add(topico('Emoção, paixão e <span class="hl">embriaguez</span>', 'Art. 28: o que não exclui a responsabilidade.', "A20",
  p("O art. 28 diz que emoção, paixão e embriaguez voluntária ou culposa <strong>não excluem</strong> a imputabilidade."),
  p("Quem bebe porque quis (ou bebeu demais sem cuidado) e comete um crime responde normalmente. Só a embriaguez <strong>completa</strong>, vinda de <strong>caso fortuito ou força maior</strong> (sem culpa do agente), isenta de pena."),
  (cp("28"), "<p>Não excluem a imputabilidade penal: I – a emoção ou a paixão; II – a embriaguez, voluntária ou culposa, pelo álcool ou substância de efeitos análogos. <b>§ 1º</b> É isento de pena o agente que, por embriaguez completa, proveniente de caso fortuito ou força maior, era, ao tempo da ação ou da omissão, inteiramente incapaz de entender o caráter ilícito do fato ou de determinar-se de acordo com esse entendimento. <b>§ 2º</b> A pena pode ser reduzida de um a dois terços se, por embriaguez proveniente de caso fortuito ou força maior, o agente não possuía a plena capacidade.</p>"),
  p("Alguém coloca, escondido, uma droga na bebida de outra pessoa, que fica completamente fora de si e agride um terceiro: embriaguez completa por caso fortuito, que pode isentar de pena."),
  "a banca afirma que a embriaguez voluntária exclui a imputabilidade ou que crime “por ciúme” (paixão) é isento de pena.",
  "<ul><li><b>Errado:</b> “O crime cometido sob forte emoção é isento de pena.” <b>Certo:</b> emoção e paixão <b>não excluem</b> a imputabilidade (podem, em certos casos, diminuir a pena, como no homicídio privilegiado).</li></ul>",
  "Emoção, paixão e embriaguez voluntária ou culposa: <strong>NÃO excluem</strong>. Embriaguez <strong>completa por caso fortuito ou força maior</strong>: <strong>isenta</strong>. Incompleta: <strong>reduz de 1/3 a 2/3</strong>.", 6))

atencao(table(["Instituto", "Regra (em síntese)", "Consequência"], [
  ["Erro de proibição (art. 21)", "Engano sobre a <b>ilicitude</b> do fato. O desconhecimento da lei é inescusável", "Inevitável: isenta de pena. Evitável: reduz de <b>1/6 a 1/3</b>"],
  ["Coação moral irresistível (art. 22)", "Alguém é forçado, por ameaça grave, a praticar o crime", "Só é punível o <b>autor da coação</b>"],
  ["Obediência hierárquica (art. 22)", "Cumprimento de ordem de superior hierárquico <b>não manifestamente ilegal</b>", "Só é punível o <b>autor da ordem</b>"]], ["28%", "40%", None]) +
 PEGADINHA("<ul><li><b>Errado:</b> “O subordinado que cumpre ordem manifestamente ilegal fica isento de pena.” <b>Certo:</b> se a ordem é <b>manifestamente</b> ilegal, ele também responde.</li><li><b>Errado:</b> “Alegar desconhecimento da lei isenta de pena.” <b>Certo:</b> o desconhecimento da lei é <b>inescusável</b>; o que pode isentar é o erro inevitável sobre a ilicitude.</li></ul>") +
 EXEMPLO(p("Um guarda municipal recebe do superior a ordem de agredir um morador já rendido. A ordem é <b>manifestamente ilegal</b>: se cumprir, responde junto com quem deu a ordem.")),
 ["Erro de proibição", "Coação irresistível", "Obediência hierárquica"], "Erro de proibição, coação e obediência")

treino(6, [
 ("A culpabilidade é composta por imputabilidade, potencial consciência da ilicitude e exigibilidade de conduta diversa.", "C", "Elementos da culpabilidade."),
 ("O semi-imputável é isento de pena.", "E", "Tem a pena reduzida de um a dois terços (art. 26, parágrafo único)."),
 ("Os menores de 18 anos são penalmente inimputáveis.", "C", "Art. 27."),
 ("A embriaguez voluntária exclui a imputabilidade penal.", "E", "Não exclui (art. 28, II)."),
 ("O erro de proibição evitável pode reduzir a pena de um sexto a um terço.", "C", "Art. 21."),
 ("Na obediência a ordem manifestamente ilegal, só o superior responde.", "E", "Só se a ordem não for manifestamente ilegal (art. 22).")])

# ================================================================ UNIDADE 7
opener("07", "UNIDADE 7", "Concurso de pessoas", ["Autoria e participação", "Regras dos arts. 29 a 31"], "U7")

add(topico('Concurso de <span class="hl">pessoas</span>', 'Arts. 29 a 31: quando várias pessoas praticam o crime.', "A21",
  p("É a colaboração de duas ou mais pessoas para a prática do mesmo crime. Cada uma responde <strong>na medida de sua culpabilidade</strong>."),
  p("O <strong>autor</strong> executa o crime (ou tem o domínio do fato); o <strong>partícipe</strong> ajuda sem executar: induz, instiga ou presta auxílio, como emprestar a arma ou vigiar a rua."),
  (cp("29"), "<p>Quem, de qualquer modo, concorre para o crime incide nas penas a este cominadas, na medida de sua culpabilidade. <b>§ 1º</b> Se a participação for de menor importância, a pena pode ser diminuída de um sexto a um terço. <b>§ 2º</b> Se algum dos concorrentes quis participar de crime menos grave, ser-lhe-á aplicada a pena deste; essa pena será aumentada até metade, na hipótese de ter sido previsível o resultado mais grave.</p>"),
  p("A e B combinam furtar uma loja à noite. B fica na esquina vigiando (partícipe) e A entra e leva os objetos (autor). Os dois respondem por furto. Se A, sem combinar com B, agride o vigia, B, que quis só o furto, responde pelo crime menos grave (art. 29, § 2º)."),
  "a banca pede a fração da participação de menor importância (1/6 a 1/3) ou a regra da cooperação dolosamente distinta.",
  "<ul><li><b>Errado:</b> “Todos os concorrentes recebem exatamente a mesma pena.” <b>Certo:</b> cada um responde <b>na medida de sua culpabilidade</b>.</li><li>O ajuste, a instigação e o auxílio <b>não são puníveis</b> se o crime não chega, pelo menos, a ser tentado (art. 31).</li></ul>",
  "Concurso: <strong>na medida da culpabilidade</strong>. Menor importância: <strong>reduz 1/6 a 1/3</strong>. Quis crime menos grave: pena deste, <strong>aumentada até metade</strong> se o mais grave era previsível.", 7))

atencao(table(["Regra", "Conteúdo"], [
  ["Requisitos (doutrina)", "Pluralidade de agentes e de condutas; relevância causal de cada conduta; liame subjetivo (vontade de colaborar); identidade de infração"],
  ["Art. 30 (circunstâncias incomunicáveis)", "Não se comunicam as circunstâncias e as condições de caráter pessoal, <b>salvo quando elementares do crime</b>"],
  ["Art. 31 (impunibilidade)", "O ajuste, a determinação ou instigação e o auxílio, salvo disposição expressa em contrário, não são puníveis se o crime não chega, pelo menos, a ser tentado"]], ["30%", None]) +
 EXEMPLO(p("<b>Art. 30 na prática:</b> um servidor público e um particular (que sabe da condição do amigo) desviam juntos dinheiro da prefeitura. A condição de funcionário público é <b>elementar</b> do peculato e se comunica: o particular também responde por peculato.")) +
 MEMORIZE("Condição pessoal <strong>não se comunica</strong>, salvo se for <strong>elementar</strong> do crime (ex.: “funcionário público” no peculato)."),
 ["Liame subjetivo", "Elementares", "Art. 31"], "Concurso de pessoas (continuação)")

treino(7, [
 ("Quem, de qualquer modo, concorre para o crime incide nas penas a este cominadas, na medida de sua culpabilidade.", "C", "Art. 29, caput."),
 ("A participação de menor importância pode reduzir a pena de um a dois terços.", "E", "De um sexto a um terço (art. 29, § 1º)."),
 ("As condições de caráter pessoal sempre se comunicam aos demais participantes.", "E", "Só quando elementares do crime (art. 30)."),
 ("O auxílio não é punível, em regra, se o crime não chega a ser tentado.", "C", "Art. 31."),
 ("O particular que, sabendo da condição do comparsa servidor, ajuda-o a desviar verba pública pode responder por peculato.", "C", "A condição de funcionário é elementar e se comunica."),
 ("Se um dos concorrentes quis participar de crime menos grave, aplica-se a ele a pena deste.", "C", "Art. 29, § 2º.")])
