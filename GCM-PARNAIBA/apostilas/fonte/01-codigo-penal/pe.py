"""Apostila 01 · Código Penal · Parte Especial (Unidades 8 a 10).
Penas e redações conferidas no texto compilado do Planalto em 28/11/2026, inclusive alterações das Leis 14.994/2024 e 15.397/2026."""
from kit import *

def cp(a): return f"Art. {a} · Código Penal"

# ================================================================ UNIDADE 8
opener("08", "UNIDADE 8", "Crimes contra a pessoa", ["Homicídio e feminicídio", "Lesão corporal", "Crimes contra a honra", "Ameaça, sequestro e violação de domicílio"], "U8")

add(topico('Homi<span class="hl">cídio</span>', 'Art. 121: matar alguém.', "A22",
  p("Homicídio é <strong>matar alguém</strong>. É o crime contra a vida mais conhecido e pode ser doloso (simples, privilegiado ou qualificado) ou culposo."),
  p("O <strong>privilegiado</strong> tem pena menor porque o motivo é mais compreensível (por exemplo, agir sob violenta emoção logo após uma provocação injusta). O <strong>qualificado</strong> tem pena maior porque o motivo ou o meio é mais reprovável (motivo fútil, veneno, emboscada)."),
  (cp("121"), "<p><b>Simples:</b> matar alguém, reclusão de 6 a 20 anos. <b>§ 1º (privilegiado):</b> relevante valor social ou moral, ou domínio de violenta emoção logo em seguida a injusta provocação da vítima: o juiz pode reduzir a pena de um sexto a um terço. <b>§ 2º (qualificado):</b> reclusão de 12 a 30 anos. <b>§ 3º (culposo):</b> detenção de 1 a 3 anos.</p>"),
  p("Briga de trânsito: o motorista mata o outro por causa de uma fechada (motivo fútil): homicídio qualificado. Motorista que, distraído ao celular, atropela e mata um pedestre: homicídio culposo de trânsito, que tem regra própria no Código de Trânsito (art. 302)."),
  "a banca pede as qualificadoras ou cobra se o feminicídio continua no art. 121.",
  "<ul><li><b>Errado:</b> “O feminicídio é qualificadora do art. 121, § 2º, VI.” <b>Certo:</b> desde a Lei nº 14.994/2024, é crime autônomo no <b>art. 121-A</b>, com reclusão de 20 a 40 anos.</li></ul>",
  "Simples <strong>6 a 20</strong> · qualificado <strong>12 a 30</strong> · culposo <strong>detenção 1 a 3</strong> · privilegiado reduz <strong>1/6 a 1/3</strong> · feminicídio <strong>art. 121-A, 20 a 40</strong>.", 8))

atencao(table(["Qualificadora do § 2º", "Em síntese"], [
  ["I", "Mediante paga ou promessa de recompensa, ou outro motivo torpe (repugnante)"],
  ["II", "Motivo fútil (desproporcional, banal)"],
  ["III", "Veneno, fogo, explosivo, asfixia, tortura ou outro meio insidioso ou cruel, ou de que possa resultar perigo comum"],
  ["IV", "Traição, emboscada, dissimulação ou recurso que dificulte ou impossibilite a defesa da vítima"],
  ["V", "Para assegurar a execução, a ocultação, a impunidade ou a vantagem de outro crime"],
  ["VI", "Revogado (o feminicídio foi para o art. 121-A)"],
  ["VII", "Contra integrantes das Forças Armadas e dos órgãos de segurança pública (arts. 142 e 144 da CF), do sistema prisional, da Força Nacional, do Judiciário, do MP, da Defensoria, da Advocacia Pública ou oficial de justiça, em razão da função, ou contra seus familiares"],
  ["VIII", "Com emprego de arma de fogo de uso restrito ou proibido"],
  ["IX", "Contra menor de 14 anos"],
  ["X", "Nas dependências de instituição de ensino"]], ["16%", None]) +
 ATENCAO(p("O inciso VII protege, entre outros, os integrantes dos órgãos do art. 144 da Constituição, em razão da função. As guardas municipais estão no § 8º desse artigo. Se a sua prova cobrar esse ponto, confira o texto literal do inciso.")) +
 lei(cp("121-A"), "<p><b>Feminicídio:</b> matar a mulher por razões da condição do sexo feminino. Pena: reclusão de 20 a 40 anos. Há razões da condição do sexo feminino quando o crime envolve violência doméstica e familiar ou menosprezo ou discriminação à condição de mulher (§ 1º).</p>"),
 ["Motivo torpe e fútil", "Meio cruel", "Feminicídio: art. 121-A"], "Qualificadoras do homicídio")

add(topico('Lesão <span class="hl">corporal</span>', 'Art. 129: ofender a integridade corporal ou a saúde.', "A23",
  p("É ofender a integridade corporal ou a saúde de outra pessoa. A pena cresce conforme a gravidade do resultado."),
  p("Um empurrão que causa um arranhão é lesão leve. Se a vítima perde a visão de um olho, a lesão é gravíssima. Se morre, sem que o agente quisesse a morte, é lesão seguida de morte."),
  (cp("129"), "<p><b>Leve (caput):</b> detenção de 3 meses a 1 ano. <b>Grave (§ 1º):</b> reclusão de 1 a 5 anos. <b>Gravíssima (§ 2º):</b> reclusão de 2 a 8 anos. <b>Seguida de morte (§ 3º):</b> reclusão de 4 a 12 anos. <b>Culposa (§ 6º):</b> detenção de 2 meses a 1 ano. <b>Violência doméstica (§ 9º):</b> reclusão de 2 a 5 anos.</p>"),
  p("Durante uma briga na feira, um homem soca outro, que fica afastado do trabalho por 40 dias: lesão grave (incapacidade para as ocupações habituais por mais de 30 dias)."),
  "a banca troca hipóteses de lesão grave e gravíssima (por exemplo, “debilidade permanente” x “perda” de membro).",
  "<ul><li><b>Debilidade</b> permanente de membro, sentido ou função = <b>grave</b>. <b>Perda ou inutilização</b> = <b>gravíssima</b>.</li><li>Aceleração de parto = grave; <b>aborto</b> = gravíssima.</li></ul>",
  "Grave: <strong>mais de 30 dias</strong>, perigo de vida, <strong>debilidade</strong>, aceleração de parto. Gravíssima: incapacidade permanente, enfermidade incurável, <strong>perda</strong>, deformidade, <strong>aborto</strong>.", 8))

atencao(NAO_CONFUNDA("Lesão grave (§ 1º) · 1 a 5 anos", "Lesão gravíssima (§ 2º) · 2 a 8 anos", [
   ("Incapacidade", "Para as ocupações habituais por <b>mais de 30 dias</b>", "<b>Permanente</b> para o trabalho"),
   ("Membro, sentido ou função", "<b>Debilidade</b> permanente", "<b>Perda ou inutilização</b>"),
   ("Gestante", "<b>Aceleração</b> de parto", "<b>Aborto</b>"),
   ("Outras", "Perigo de vida", "Enfermidade incurável; deformidade permanente")]) +
 lei(cp("122"), "<p>Induzir ou instigar alguém a suicidar-se ou a praticar automutilação, ou prestar-lhe auxílio material para que o faça: reclusão de 6 meses a 2 anos. Se o suicídio se consuma ou da automutilação resulta morte: reclusão de 2 a 6 anos (§ 2º). A pena aumenta até o dobro se a conduta é realizada por rede de computadores, rede social ou transmitida em tempo real (§ 4º).</p>"),
 ["Debilidade x perda", "30 dias", "Art. 122"], "Lesão corporal (continuação)")

add(H(8, 'Crimes contra a <span class="hl">honra</span>', 'Arts. 138 a 140: calúnia, difamação e injúria.', "A24") +
 oque(p("São crimes que ofendem a <strong>honra</strong>: a reputação da pessoa perante os outros (honra objetiva) ou o sentimento de dignidade dela (honra subjetiva).")) +
 table(["Crime", "Conduta", "Exemplo", "Pena"], [
  ["Calúnia (art. 138)", "Imputar falsamente a alguém <b>fato definido como crime</b>", "“Fulano furtou o celular da escola ontem” (sabendo que é mentira)", "Detenção de 6 meses a 2 anos, e multa"],
  ["Difamação (art. 139)", "Imputar a alguém <b>fato ofensivo à reputação</b> (não criminoso)", "“Fulano chega bêbado ao trabalho todo dia”", "Detenção de 3 meses a 1 ano, e multa"],
  ["Injúria (art. 140)", "Ofender a <b>dignidade ou o decoro</b>, sem imputar fato", "Xingar alguém de “ladrão” ou “incompetente”", "Detenção de 1 a 6 meses, ou multa"]], ["18%", "28%", "30%", None]) +
 traduz(p("Truque: <strong>calúnia</strong> = conta um <strong>crime</strong> falso; <strong>difamação</strong> = conta um <strong>fato</strong> que mancha a reputação; <strong>injúria</strong> = <strong>xingamento</strong>, sem contar fato nenhum.")) +
 PEGADINHA("<ul><li><b>Errado:</b> “Chamar alguém de ladrão é calúnia.” <b>Certo:</b> é <b>injúria</b> (qualidade negativa, sem fato determinado). Seria calúnia dizer, falsamente, que a pessoa furtou algo em tal dia.</li><li>Na difamação, a prova da verdade só é admitida se o ofendido é <b>funcionário público</b> e a ofensa é relativa às suas funções (art. 139, parágrafo único).</li></ul>") +
 MEMORIZE("<strong>Calúnia</strong> = crime falso · <strong>Difamação</strong> = fato desonroso · <strong>Injúria</strong> = ofensa/xingamento. Em regra, ação penal <strong>privada</strong> (queixa, art. 145)."))

add(H(8, 'Ameaça, sequestro e <span class="hl">violação de domicílio</span>', 'Crimes contra a liberdade individual.', "A25") +
 table(["Crime", "Conduta (em síntese)", "Pena", "Detalhe de prova"], [
  ["Ameaça (art. 147)", "Ameaçar alguém, por palavra, escrito, gesto ou outro meio simbólico, de causar-lhe mal injusto e grave", "Detenção de 1 a 6 meses, ou multa", "Depende de <b>representação</b>, salvo se contra a mulher por razões da condição do sexo feminino (pena em dobro)"],
  ["Sequestro e cárcere privado (art. 148)", "Privar alguém de sua liberdade, mediante sequestro ou cárcere privado", "Reclusão de 1 a 3 anos", "Qualifica (2 a 5 anos) se a vítima é ascendente, descendente, cônjuge, companheiro ou maior de 60, menor de 18, se dura mais de 15 dias, entre outros"],
  ["Violação de domicílio (art. 150)", "Entrar ou permanecer, clandestina ou astuciosamente, ou contra a vontade de quem de direito, em casa alheia ou em suas dependências", "Detenção de 1 a 3 meses, ou multa", "Não é crime entrar durante o dia, com as formalidades legais, para prisão ou diligência, nem a qualquer hora quando algum crime está sendo praticado ou na iminência de o ser (§ 3º)"]], ["20%", "32%", "18%", None]) +
 EXEMPLO(p("Um morador avisa a equipe da GCM que um homem pulou o muro da casa vizinha à noite. Entrar escondido em casa alheia, à noite, é violação de domicílio na forma qualificada (§ 1º: detenção de 6 meses a 2 anos). Se ele entrou para furtar, responderá pelo furto ou pela tentativa.")) +
 PEGADINHA("<ul><li>Para o art. 150, “casa” inclui o compartimento não aberto ao público onde alguém exerce profissão (o escritório nos fundos da loja, por exemplo). <b>Não</b> inclui a hospedaria aberta nem o bar (§§ 4º e 5º).</li></ul>"))

treino(8, [
 ("O homicídio simples tem pena de reclusão de 6 a 20 anos.", "C", "Art. 121, caput."),
 ("O feminicídio continua previsto como qualificadora no art. 121, § 2º, VI, do Código Penal.", "E", "Desde a Lei 14.994/2024, é o art. 121-A (20 a 40 anos)."),
 ("A perda de um membro caracteriza lesão corporal grave.", "E", "Perda ou inutilização é gravíssima; debilidade é grave."),
 ("Imputar falsamente a alguém um fato definido como crime caracteriza calúnia.", "C", "Art. 138."),
 ("Xingar alguém de “desonesto” caracteriza difamação.", "E", "É injúria: ofensa sem imputação de fato."),
 ("A ameaça é crime que, em regra, depende de representação da vítima.", "C", "Art. 147, § 2º (salvo o § 1º).")])

# ================================================================ UNIDADE 9
opener("09", "UNIDADE 9", "Crimes contra o patrimônio", ["Furto", "Roubo e latrocínio", "Extorsão e extorsão mediante sequestro", "Apropriação indébita, estelionato e receptação", "Imunidades"], "U9")

add(topico('<span class="hl">Furto</span>', 'Art. 155: subtrair sem violência.', "A26",
  p("Furto é <strong>subtrair</strong>, para si ou para outra pessoa, <strong>coisa alheia móvel</strong>, sem violência nem grave ameaça à pessoa."),
  p("É o “pegar escondido” ou sem que a vítima consiga reagir: o batedor de carteira, quem leva a bicicleta deixada na calçada."),
  (cp("155"), "<p>Subtrair, para si ou para outrem, coisa alheia móvel: reclusão de 1 a 6 anos, e multa (redação da Lei nº 15.397/2026). <b>§ 1º</b> A pena aumenta de metade se o crime é praticado durante o repouso noturno. <b>§ 2º</b> Se o criminoso é primário e a coisa furtada é de pequeno valor, o juiz pode substituir a reclusão por detenção, diminuí-la de um a dois terços ou aplicar somente a multa. <b>§ 4º (qualificado):</b> reclusão de 2 a 8 anos, e multa.</p>"),
  p("Na madrugada, um homem quebra o cadeado de uma bicicleta estacionada na orla e foge com ela: furto qualificado por rompimento de obstáculo (§ 4º, I), praticado durante o repouso noturno."),
  "a banca cobra as qualificadoras (rompimento de obstáculo, fraude, escalada, destreza, chave falsa, concurso de pessoas) e o furto privilegiado.",
  "<ul><li><b>Errado:</b> “Furto de energia elétrica não é crime, porque energia não é coisa.” <b>Certo:</b> equipara-se à coisa móvel a energia elétrica ou qualquer outra com valor econômico (§ 3º).</li><li>Penas antigas aparecem em materiais desatualizados: a Lei nº 15.397/2026 elevou a pena do furto simples para <b>1 a 6 anos</b>.</li></ul>",
  "Furto = subtrair coisa alheia móvel <strong>sem violência</strong>. Simples <strong>1 a 6</strong> · noturno <strong>+ metade</strong> · qualificado <strong>2 a 8</strong> · privilegiado: primário + pequeno valor.", 9))

add(topico('Roubo e <span class="hl">latrocínio</span>', 'Art. 157: subtrair com violência ou grave ameaça.', "A27",
  p("Roubo é subtrair coisa alheia móvel <strong>mediante grave ameaça ou violência à pessoa</strong>, ou depois de reduzi-la à impossibilidade de resistência."),
  p("A diferença para o furto é a <strong>violência ou grave ameaça</strong>. O “assalto” do dia a dia é roubo. Se da violência resulta morte, o crime é o <strong>latrocínio</strong> (roubo seguido de morte)."),
  (cp("157"), "<p>Subtrair coisa móvel alheia, para si ou para outrem, mediante grave ameaça ou violência a pessoa, ou depois de havê-la, por qualquer meio, reduzido à impossibilidade de resistência: reclusão de 6 a 10 anos, e multa (Lei nº 15.397/2026). <b>§ 2º</b> aumento de 1/3 até a metade (ex.: concurso de duas ou mais pessoas; arma branca; restrição da liberdade da vítima). <b>§ 2º-A</b> aumento de 2/3 se a violência ou ameaça é exercida com arma de fogo. <b>§ 3º</b> se resulta lesão corporal grave, reclusão de 7 a 18 anos; se resulta morte, reclusão de 24 a 30 anos, e multa.</p>"),
  p("Dois homens abordam uma pessoa na praça com uma faca e levam o celular: roubo com aumento de pena (concurso de pessoas e arma branca). Se um deles dispara e mata a vítima: latrocínio."),
  "a banca troca furto por roubo, ou cobra o roubo impróprio (violência empregada logo depois da subtração, para garantir a impunidade ou a coisa).",
  "<ul><li><b>Errado:</b> “Se o ladrão usa a violência só depois de pegar a coisa, para fugir, há furto.” <b>Certo:</b> é <b>roubo impróprio</b> (§ 1º), com a mesma pena.</li><li>O latrocínio é crime contra o <b>patrimônio</b>, e não contra a vida.</li></ul>",
  "Roubo = subtração <strong>+ violência ou grave ameaça</strong>. Simples <strong>6 a 10</strong> · arma de fogo <strong>+ 2/3</strong> · lesão grave <strong>7 a 18</strong> · latrocínio <strong>24 a 30</strong>.", 9))

add(H(9, 'Extorsão e extorsão mediante <span class="hl">sequestro</span>', 'Arts. 158 e 159: obrigar a vítima a colaborar.', "A28") +
 table(["Crime", "Conduta (em síntese)", "Pena"], [
  ["Extorsão (art. 158)", "Constranger alguém, mediante violência ou grave ameaça, com o intuito de obter indevida vantagem econômica, a fazer, tolerar que se faça ou deixar de fazer alguma coisa", "Reclusão de 4 a 10 anos, e multa"],
  ["Extorsão com restrição da liberdade (art. 158, § 3º)", "Cometida mediante a restrição da liberdade da vítima, condição necessária para obter a vantagem (o chamado “sequestro relâmpago”)", "Reclusão de 6 a 12 anos, além da multa"],
  ["Extorsão mediante sequestro (art. 159)", "Sequestrar pessoa com o fim de obter qualquer vantagem como condição ou preço do resgate", "Reclusão de 8 a 15 anos (mais de 24h, vítima menor de 18 ou maior de 60, ou cometido por bando ou quadrilha: 12 a 20)"]], ["26%", "50%", None]) +
 NAO_CONFUNDA("Roubo", "Extorsão", [
   ("Quem entrega a coisa?", "O agente <b>tira</b> a coisa (a colaboração da vítima é dispensável)", "A vítima <b>faz</b> algo; sua colaboração é <b>indispensável</b>"),
   ("Exemplo", "Arrancar a bolsa sob ameaça", "Obrigar a vítima a fazer um PIX ou a dizer a senha do cartão")]) +
 MEMORIZE("Extorsão: a vítima é <strong>obrigada a colaborar</strong>. “Sequestro relâmpago” = extorsão com restrição da liberdade (<strong>art. 158, § 3º</strong>). Resgate = <strong>art. 159</strong>."))

add(H(9, 'Apropriação, estelionato e <span class="hl">receptação</span>', 'Arts. 168, 171 e 180.', "A29") +
 table(["Crime", "Conduta (em síntese)", "Pena", "Exemplo"], [
  ["Apropriação indébita (art. 168)", "Apropriar-se de coisa alheia móvel de que tem a posse ou a detenção", "Reclusão de 1 a 4 anos, e multa", "Pegar emprestado o notebook do colega e vendê-lo"],
  ["Estelionato (art. 171)", "Obter vantagem ilícita, em prejuízo alheio, induzindo ou mantendo alguém em erro, mediante artifício, ardil ou outro meio fraudulento", "Reclusão de 1 a 5 anos, e multa (Lei nº 15.397/2026)", "Vender um carro que não existe pela internet"],
  ["Receptação (art. 180)", "Adquirir, receber, transportar, conduzir ou ocultar coisa que sabe ser produto de crime, ou influir para que terceiro de boa-fé a adquira", "Reclusão de 2 a 6 anos, e multa (Lei nº 15.397/2026)", "Comprar um celular sabendo que foi roubado"]], ["20%", "34%", "20%", None]) +
 NAO_CONFUNDA("Furto mediante fraude", "Estelionato", [
   ("Papel da fraude", "Distrai a vítima para o agente <b>subtrair</b> a coisa", "Engana a vítima, que <b>entrega</b> a coisa voluntariamente"),
   ("Exemplo", "Fingir ser cliente para distrair o vendedor e pegar a mercadoria", "Pagar com comprovante de PIX falso e receber a mercadoria")]) +
 ATENCAO(p("A receptação é punível ainda que o autor do crime anterior seja desconhecido ou isento de pena (art. 180, § 4º). Existe também a <b>receptação culposa</b> (§ 3º), quando a pessoa deveria presumir a origem criminosa, por exemplo pelo preço muito abaixo do mercado.")))

add(H(9, '<span class="hl">Imunidades</span> nos crimes patrimoniais', 'Arts. 181 a 183: quando a família isenta de pena.', "A30") +
 table(["Regra", "Conteúdo"], [
  ["Imunidade absoluta (art. 181)", "É <b>isento de pena</b> quem comete crime patrimonial em prejuízo: do cônjuge, na constância da sociedade conjugal; de ascendente ou descendente"],
  ["Imunidade relativa (art. 182)", "Só se procede mediante <b>representação</b> se o crime é cometido em prejuízo: do cônjuge desquitado ou judicialmente separado; de irmão; de tio ou sobrinho com quem o agente coabita"],
  ["Exceções (art. 183)", "As imunidades <b>não se aplicam</b>: se o crime é de roubo ou extorsão ou envolve grave ameaça ou violência à pessoa; ao estranho que participa do crime; se a vítima tem 60 anos ou mais"]], ["28%", None]) +
 EXEMPLO(p("O filho que furta dinheiro da carteira do pai, de 50 anos, é isento de pena (art. 181, II). Se o pai tivesse 65 anos, ou se o filho usasse violência, a imunidade não valeria (art. 183).")) +
 MEMORIZE("Imunidade: <strong>cônjuge, pais e filhos</strong> = isento · <strong>irmão, tio ou sobrinho que coabita</strong> = depende de representação · <strong>NÃO vale</strong>: violência ou grave ameaça, roubo, extorsão, estranho, vítima de <strong>60+</strong>."))

treino(9, [
 ("Furto é subtrair, para si ou para outrem, coisa alheia móvel.", "C", "Art. 155."),
 ("A pena do furto simples é de reclusão de 1 a 4 anos, segundo a redação vigente do Código Penal.", "E", "Desde a Lei 15.397/2026, é de 1 a 6 anos."),
 ("O ladrão que, logo após a subtração, emprega violência para garantir a fuga com a coisa comete roubo impróprio.", "C", "Art. 157, § 1º."),
 ("O latrocínio é crime contra a vida.", "E", "É crime contra o patrimônio (art. 157, § 3º, II)."),
 ("Na extorsão, a colaboração da vítima é indispensável para a obtenção da vantagem.", "C", "Diferença em relação ao roubo."),
 ("O filho que furta o pai de 70 anos é isento de pena pela imunidade do art. 181.", "E", "A imunidade não se aplica se a vítima tem 60 anos ou mais (art. 183, III).")])

# ================================================================ UNIDADE 10
opener("10", "UNIDADE 10", "Crimes contra a Administração Pública", ["Quem é funcionário público para o Direito Penal", "Crimes praticados por funcionário público", "Crimes praticados por particular contra a Administração"], "U10")

add(topico('Funcionário público <span class="hl">para o Direito Penal</span>', 'Art. 327: um conceito bem mais amplo que o do Direito Administrativo.', "A31",
  p("É quem exerce cargo, emprego ou função pública, ainda que de forma <strong>transitória</strong> ou <strong>sem remuneração</strong>."),
  p("Para o Direito Penal, não importa se a pessoa é concursada, comissionada, temporária ou voluntária: se exerce função pública, pode cometer crimes “de funcionário público”. Isso inclui você, quando for guarda municipal."),
  (cp("327"), "<p>Considera-se funcionário público, para os efeitos penais, quem, embora transitoriamente ou sem remuneração, exerce cargo, emprego ou função pública. <b>§ 1º</b> Equipara-se a funcionário público quem exerce cargo, emprego ou função em entidade paraestatal, e quem trabalha para empresa prestadora de serviço contratada ou conveniada para a execução de atividade típica da Administração Pública. <b>§ 2º</b> A pena é aumentada da terça parte quando os autores forem ocupantes de cargos em comissão ou de função de direção ou assessoramento.</p>"),
  p("O mesário convocado para a eleição e o jurado são funcionários públicos para fins penais enquanto exercem a função, mesmo sem remuneração."),
  "a banca diz que só o servidor efetivo e remunerado pode cometer peculato ou corrupção passiva.",
  "<ul><li><b>Errado:</b> “O conceito penal de funcionário público exige vínculo efetivo e remuneração.” <b>Certo:</b> basta exercer cargo, emprego ou função pública, ainda que transitoriamente ou sem remuneração.</li></ul>",
  "Funcionário público penal: exerce <strong>cargo, emprego ou função pública</strong>, mesmo <strong>transitoriamente</strong> ou <strong>sem remuneração</strong>. Comissionado ou cargo de direção: <strong>+ 1/3</strong>.", 10))

add(H(10, 'Crimes praticados por <span class="hl">funcionário público</span>', 'Os verbos que diferenciam cada crime.', "A32") +
 table(["Crime", "Verbo-chave e conduta (em síntese)", "Pena"], [
  ["Peculato (art. 312)", "<b>Apropriar-se</b> ou <b>desviar</b> dinheiro, valor ou bem móvel, público ou particular, de que tem a posse em razão do cargo. § 1º (peculato-furto): <b>subtrair</b> valendo-se da facilidade do cargo", "Reclusão de 2 a 12 anos, e multa"],
  ["Peculato culposo (art. 312, § 2º)", "Concorrer <b>culposamente</b> para o crime de outrem", "Detenção de 3 meses a 1 ano"],
  ["Peculato mediante erro de outrem (art. 313)", "Apropriar-se de dinheiro ou utilidade que, no exercício do cargo, <b>recebeu por erro</b> de outrem", "Reclusão de 1 a 4 anos, e multa"],
  ["Concussão (art. 316)", "<b>Exigir</b> vantagem indevida, em razão da função", "Reclusão de 2 a 12 anos, e multa"],
  ["Corrupção passiva (art. 317)", "<b>Solicitar</b> ou <b>receber</b> vantagem indevida, ou <b>aceitar promessa</b> dela, em razão da função", "Reclusão de 2 a 12 anos, e multa"],
  ["Prevaricação (art. 319)", "Retardar ou deixar de praticar ato de ofício, ou praticá-lo contra a lei, para satisfazer <b>interesse ou sentimento pessoal</b>", "Detenção de 3 meses a 1 ano, e multa"],
  ["Condescendência criminosa (art. 320)", "Deixar, por <b>indulgência</b>, de responsabilizar subordinado infrator, ou de levar o fato à autoridade competente", "Detenção de 15 dias a 1 mês, ou multa"],
  ["Advocacia administrativa (art. 321)", "<b>Patrocinar</b> interesse privado perante a Administração, valendo-se da qualidade de funcionário", "Detenção de 1 a 3 meses, ou multa"]], ["24%", "52%", None]) +
 ATENCAO(p("<b>Peculato culposo:</b> a reparação do dano, se anterior à sentença irrecorrível, <b>extingue a punibilidade</b>; se posterior, reduz de metade a pena imposta (art. 312, § 3º).")))

add(topico('Concussão x corrupção <span class="hl">passiva</span>', 'Arts. 316 e 317: a diferença está no verbo.', "A33",
  p("Os dois crimes envolvem funcionário público e vantagem indevida em razão da função. Na <strong>concussão</strong>, ele <strong>exige</strong>; na <strong>corrupção passiva</strong>, ele <strong>solicita, recebe ou aceita promessa</strong>."),
  p("Exigir é impor, com intimidação implícita (“ou você paga, ou…”). Solicitar é pedir; receber é aceitar o que foi oferecido. A pena é a mesma (reclusão de 2 a 12 anos, e multa), mas a banca cobra a diferença."),
  (cp("316 e 317"), "<p><b>Concussão:</b> exigir, para si ou para outrem, direta ou indiretamente, ainda que fora da função ou antes de assumi-la, mas em razão dela, vantagem indevida. <b>Corrupção passiva:</b> solicitar ou receber, para si ou para outrem, direta ou indiretamente, ainda que fora da função ou antes de assumi-la, mas em razão dela, vantagem indevida, ou aceitar promessa de tal vantagem.</p>"),
  p("Um fiscal diz ao comerciante: “ou me paga R$ 500, ou eu interdito sua loja”: concussão. Outro fiscal pede, sem ameaçar, “uma ajudinha” para agilizar o alvará: corrupção passiva. O comerciante que oferece dinheiro ao fiscal comete corrupção ativa (art. 333)."),
  "o caso traz o verbo e você precisa classificar; ou a banca afirma que é preciso receber o dinheiro para consumar o crime.",
  "<ul><li><b>Errado:</b> “A corrupção passiva só se consuma quando o funcionário recebe a vantagem.” <b>Certo:</b> basta <b>solicitar</b> ou <b>aceitar a promessa</b> (crime formal).</li><li>O crime existe “ainda que fora da função ou <b>antes de assumi-la</b>”, desde que em razão dela.</li></ul>",
  "<strong>EXIGIR</strong> = concussão · <strong>SOLICITAR / RECEBER / ACEITAR PROMESSA</strong> = corrupção passiva · particular que <strong>OFERECE ou PROMETE</strong> = corrupção ativa.", 10))

add(H(10, 'Crimes praticados por <span class="hl">particular</span>', 'Arts. 329 a 333: os mais presentes na rotina de quem está na rua.', "A34") +
 table(["Crime", "Conduta (em síntese)", "Pena"], [
  ["Resistência (art. 329)", "Opor-se à execução de <b>ato legal</b>, mediante <b>violência ou ameaça</b> a funcionário competente ou a quem lhe presta auxílio", "Detenção de 2 meses a 2 anos (se o ato não se executa: reclusão de 1 a 3 anos)"],
  ["Desobediência (art. 330)", "Desobedecer a <b>ordem legal</b> de funcionário público (sem violência)", "Detenção de 15 dias a 6 meses, e multa"],
  ["Desacato (art. 331)", "Desacatar (humilhar, ofender) funcionário público no exercício da função ou em razão dela", "Detenção de 6 meses a 2 anos, ou multa"],
  ["Tráfico de influência (art. 332)", "Solicitar, exigir, cobrar ou obter vantagem a pretexto de influir em ato de funcionário público", "Reclusão de 2 a 5 anos, e multa"],
  ["Corrupção ativa (art. 333)", "<b>Oferecer</b> ou <b>prometer</b> vantagem indevida a funcionário público para determiná-lo a praticar, omitir ou retardar ato de ofício", "Reclusão de 2 a 12 anos, e multa"]], ["22%", "48%", None]) +
 NAO_CONFUNDA("Resistência", "Desobediência", [
   ("Violência ou ameaça?", "<b>Sim</b>, contra o funcionário ou quem o auxilia", "<b>Não</b>: só descumpre a ordem"),
   ("Exemplo", "Empurrar e ameaçar o guarda para impedir a apreensão de mercadoria irregular", "Recusar-se a parar o veículo após ordem legal, sem agredir ninguém")]) +
 MEMORIZE("Particular: <strong>violência</strong> contra ato legal = resistência · descumpriu ordem legal = desobediência · humilhou o servidor = desacato · <strong>ofereceu</strong> vantagem = corrupção ativa."))

atencao(EXEMPLO(p("Durante uma fiscalização de comércio ambulante, o guarda municipal informa ao vendedor que a mercadoria será recolhida, conforme a lei municipal:") +
 table(["Reação do vendedor", "Crime em tese"], [
  ["Xinga o guarda de “vagabundo” e “ladrão de pobre” na frente de todos", "Desacato (art. 331)"],
  ["Recusa-se a entregar a mercadoria, sem agressão nem ameaça", "Desobediência (art. 330)"],
  ["Empurra o guarda e ameaça agredi-lo para impedir o recolhimento", "Resistência (art. 329), sem prejuízo da pena da violência"],
  ["Oferece R$ 100 para o guarda “deixar para lá”", "Corrupção ativa (art. 333)"],
  ["O guarda aceita os R$ 100", "O guarda comete corrupção passiva (art. 317)"],
  ["O guarda exige R$ 100 para não recolher", "O guarda comete concussão (art. 316)"]], ["58%", None]), "Situação prática: fiscalização na feira") +
 PEGADINHA("<ul><li>Resistência exige <b>ato legal</b>: opor-se a uma ordem ilegal não configura o crime.</li><li>Na corrupção ativa, basta <b>oferecer ou prometer</b>, mesmo que o funcionário recuse.</li></ul>"),
 ["Desacato", "Desobediência", "Resistência", "Corrupção ativa e passiva"], "Atuação prática do guarda municipal")

treino(10, [
 ("Para os efeitos penais, é funcionário público quem exerce função pública, ainda que transitoriamente e sem remuneração.", "C", "Art. 327, caput."),
 ("O funcionário que exige vantagem indevida em razão da função comete corrupção passiva.", "E", "Exigir é concussão (art. 316)."),
 ("A corrupção passiva pode ser praticada antes de o agente assumir a função, desde que em razão dela.", "C", "Art. 317."),
 ("No peculato culposo, a reparação do dano anterior à sentença irrecorrível extingue a punibilidade.", "C", "Art. 312, § 3º."),
 ("Quem apenas descumpre ordem legal de funcionário, sem violência ou ameaça, comete resistência.", "E", "Comete desobediência (art. 330)."),
 ("O particular que oferece vantagem indevida a funcionário público comete corrupção ativa, ainda que o funcionário recuse.", "C", "Art. 333: basta oferecer ou prometer.")])
