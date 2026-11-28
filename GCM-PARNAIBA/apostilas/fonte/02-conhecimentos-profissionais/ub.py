"""Apostila 02 · Conhecimentos Profissionais · Unidades 2, 3, 7, 8 e 9.
CF, ECA, Lei 13.869/2019 e Decreto 12.341/2024 conferidos no Planalto em 28/11/2026; Lei 13.060/2014, CTB e DUDH conferidos em 26/11/2026."""
from kit import *

def cf(a): return f"Art. {a} · Constituição Federal"

# ================================================================ UNIDADE 2 · CONSTITUIÇÃO
def unidade2():
    opener("02", "UNIDADE 2", "Constituição Federal e direitos fundamentais", ["Fundamentos da República", "Direitos e garantias na abordagem", "Direitos da pessoa presa"], "U2")

    add(topico('Fundamentos da <span class="hl">República</span>', 'Art. 1º da Constituição.', "A04",
      p("A Constituição Federal de 1988 é a lei mais importante do país. Todas as outras leis, inclusive as da guarda, precisam respeitá-la."),
      p("O art. 1º diz quais são os “alicerces” do Brasil. O mais cobrado em provas de segurança é a <strong>dignidade da pessoa humana</strong>: toda pessoa, inclusive quem cometeu um crime, deve ser tratada como ser humano."),
      (cf("1º"), "<p>A República Federativa do Brasil, formada pela união indissolúvel dos Estados e Municípios e do Distrito Federal, constitui-se em Estado Democrático de Direito e tem como fundamentos: I – a soberania; II – a cidadania; III – a dignidade da pessoa humana; IV – os valores sociais do trabalho e da livre iniciativa; V – o pluralismo político.</p>"),
      p("Ao conduzir um suspeito detido, o guarda não o expõe a fotos e humilhações em público. Isso respeita a dignidade da pessoa humana e evita crime de abuso de autoridade (Lei 13.869/2019, art. 13)."),
      "a banca troca um fundamento (art. 1º) por um objetivo (art. 3º) ou por um princípio das relações internacionais (art. 4º).",
      "<ul><li><b>Errado:</b> “A independência nacional é fundamento da República.” <b>Certo:</b> é princípio das relações internacionais (art. 4º).</li></ul>",
      "Fundamentos: <strong>SO-CI-DI-VA-PLU</strong> (soberania, cidadania, dignidade, valores sociais do trabalho e da livre iniciativa, pluralismo político).", 2))

    add(H(2, 'Direitos e garantias <span class="hl">na abordagem</span>', 'Art. 5º: os incisos que o guarda aplica no dia a dia.', "A05") +
     table(["Inciso", "O que garante (em síntese)", "Na atuação do guarda"], [
      ["III", "Ninguém será submetido a tortura nem a tratamento desumano ou degradante", "Nunca humilhar, agredir ou expor quem foi detido"],
      ["IV", "Livre manifestação do pensamento, vedado o anonimato", "Crítica à guarda não é crime; ofensa pode ser desacato ou injúria"],
      ["X", "Intimidade, vida privada, honra e imagem são invioláveis", "Não divulgar imagens de pessoas abordadas"],
      ["XI", "A casa é asilo inviolável: sem consentimento do morador, só em flagrante delito, desastre ou para prestar socorro, ou, durante o dia, por determinação judicial", "Entrar em casa sem essas hipóteses é ilegal e pode ser crime (Lei 13.869/2019, art. 22)"],
      ["XV", "Livre locomoção no território nacional em tempo de paz", "Restrições só nos casos previstos em lei"],
      ["XVI", "Reunião pacífica, sem armas, em locais abertos, sem autorização, exigido prévio aviso à autoridade", "Proteger manifestações pacíficas; não exigir “autorização”"]], ["10%", "48%", None]) +
     NAO_CONFUNDA("De dia", "À noite", [
      ("Com ordem judicial", "Pode entrar", "<b>Não</b> pode (só de dia)"),
      ("Flagrante, desastre ou socorro", "Pode entrar", "Pode entrar")]) +
     MEMORIZE("Casa: <strong>flagrante, desastre e socorro</strong> = qualquer hora · <strong>ordem judicial</strong> = só de dia. Reunião: <strong>aviso</strong>, não autorização."))

    add(H(2, 'Direitos da pessoa <span class="hl">presa</span>', 'Art. 5º, XLIX e LVII a LXVIII.', "A06") +
     table(["Inciso", "Garantia (em síntese)"], [
      ["XLIX", "É assegurado aos presos o respeito à integridade física e moral"],
      ["LVII", "Ninguém será considerado culpado até o trânsito em julgado de sentença penal condenatória"],
      ["LXI", "Ninguém será preso senão em flagrante delito ou por ordem escrita e fundamentada de autoridade judiciária competente (salvo transgressão ou crime propriamente militar)"],
      ["LXII", "A prisão e o local onde se encontre o preso serão comunicados imediatamente ao juiz competente e à família do preso ou à pessoa por ele indicada"],
      ["LXIII", "O preso será informado de seus direitos, entre os quais o de permanecer calado, sendo-lhe assegurada a assistência da família e de advogado"],
      ["LXIV", "O preso tem direito à identificação dos responsáveis por sua prisão ou por seu interrogatório policial"],
      ["LXV", "A prisão ilegal será imediatamente relaxada pela autoridade judiciária"],
      ["LXVIII", "Habeas corpus: sempre que alguém sofrer ou se achar ameaçado de sofrer violência ou coação em sua liberdade de locomoção, por ilegalidade ou abuso de poder"]], ["12%", None]) +
     EXEMPLO(p("A equipe prende em flagrante um homem que furtou a bicicleta de uma escola municipal. Os guardas se identificam, informam que ele tem direito de ficar calado, não o expõem a fotos, preservam a integridade dele e o apresentam ao delegado (Lei 13.022/2014, art. 5º, XIV).")) +
     PEGADINHA("<ul><li><b>Errado:</b> “O guarda pode deixar de se identificar ao preso por segurança.” <b>Certo:</b> o preso tem direito à identificação dos responsáveis pela prisão (LXIV); deixar de se identificar pode ser crime (Lei 13.869/2019, art. 16).</li></ul>"))

    treino(2, [
     ("A dignidade da pessoa humana é fundamento da República Federativa do Brasil.", "C", "CF, art. 1º, III."),
     ("Com ordem judicial, a casa pode ser invadida a qualquer hora da noite.", "E", "A ordem judicial só autoriza o ingresso durante o dia (art. 5º, XI)."),
     ("Para socorrer uma pessoa, é possível entrar na casa sem consentimento, mesmo à noite.", "C", "Art. 5º, XI."),
     ("O direito de reunião depende de autorização prévia da autoridade policial.", "E", "Exige apenas prévio aviso (art. 5º, XVI)."),
     ("O preso tem direito à identificação dos responsáveis por sua prisão.", "C", "Art. 5º, LXIV."),
     ("Ninguém será considerado culpado até o trânsito em julgado de sentença penal condenatória.", "C", "Art. 5º, LVII.")])

# ================================================================ UNIDADE 3 · SEGURANÇA PÚBLICA
def unidade3():
    opener("03", "UNIDADE 3", "Segurança pública", ["O art. 144 da Constituição", "O lugar da guarda municipal", "O que o STF decidiu"], "U3")

    add(topico('Segurança pública na <span class="hl">Constituição</span>', 'Art. 144: quem faz o quê.', "A07",
      p("Segurança pública é a atividade do Estado para preservar a ordem pública e a incolumidade das pessoas e do patrimônio."),
      p("A Constituição divide as tarefas entre vários órgãos. Cada um tem sua função: a PM faz o policiamento ostensivo, a Polícia Civil investiga, a PRF patrulha as rodovias federais. A guarda municipal aparece em um parágrafo próprio, o § 8º."),
      (cf("144"), "<p>A segurança pública, dever do Estado, direito e responsabilidade de todos, é exercida para a preservação da ordem pública e da incolumidade das pessoas e do patrimônio, através dos seguintes órgãos: I – polícia federal; II – polícia rodoviária federal; III – polícia ferroviária federal; IV – polícias civis; V – polícias militares e corpos de bombeiros militares; VI – polícias penais federal, estaduais e distrital. <b>§ 8º</b> Os Municípios poderão constituir guardas municipais destinadas à proteção de seus bens, serviços e instalações, conforme dispuser a lei.</p>"),
      p("Um assalto acaba de acontecer na praça. A guarda, que estava próxima, prende o autor em flagrante e o leva ao delegado (Polícia Civil, que investigará). A PM, responsável pelo policiamento ostensivo do Estado, pode apoiar a ocorrência."),
      "pergunta-se quais órgãos estão nos incisos do caput (a guarda não está) ou a função de cada órgão.",
      "<ul><li><b>Errado:</b> “As guardas municipais constam do rol de incisos do caput do art. 144.” <b>Certo:</b> estão no <b>§ 8º</b>. Mesmo assim, o STF reconheceu que integram o Sistema de Segurança Pública (ADPF 995).</li><li>Segurança pública é dever do Estado e “direito e <b>responsabilidade de todos</b>”.</li></ul>",
      "Art. 144: PF · PRF · PFF · polícias civis · PM e bombeiros · polícias penais. Guarda municipal: <strong>§ 8º</strong>, proteção de <strong>bens, serviços e instalações</strong>.", 3))

    add(H(3, 'Funções dos órgãos e <span class="hl">segurança viária</span>', 'Art. 144, §§ 5º, 7º, 8º e 10.', "A08") +
     table(["Órgão", "Função principal"], [
      ["Polícia Federal", "Polícia judiciária da União, entre outras atribuições"],
      ["Polícias civis", "Polícia judiciária e apuração de infrações penais, exceto militares"],
      ["Polícias militares (§ 5º)", "Polícia ostensiva e preservação da ordem pública"],
      ["Corpos de bombeiros militares (§ 5º)", "Atribuições legais e atividades de defesa civil"],
      ["Polícias penais (§ 5º-A)", "Segurança dos estabelecimentos penais"],
      ["Guardas municipais (§ 8º)", "Proteção de bens, serviços e instalações do Município, conforme a lei (Lei 13.022/2014)"]], ["30%", None]) +
     lei(cf("144, § 10"), "<p>A segurança viária, exercida para a preservação da ordem pública e da incolumidade das pessoas e do seu patrimônio nas vias públicas: I – compreende a educação, engenharia e fiscalização de trânsito, além de outras atividades previstas em lei, que assegurem ao cidadão o direito à mobilidade urbana eficiente; II – compete, no âmbito dos Estados, do Distrito Federal e dos Municípios, aos respectivos órgãos ou entidades executivos e seus agentes de trânsito, estruturados em carreira, na forma da lei.</p>") +
     MEMORIZE("PM = <strong>ostensiva + ordem pública</strong> · Civil = <strong>judiciária + investigação</strong> · Guarda = <strong>bens, serviços e instalações</strong> · Segurança viária = <strong>educação, engenharia, fiscalização</strong>."))

    add(H(3, 'O que o <span class="hl">STF</span> decidiu', 'Decisões que mudaram a leitura do papel da guarda.', "A09") +
     table(["Decisão", "O que ficou decidido (em síntese)"], [
      ["ADPF 995 (agosto de 2023)", "As guardas municipais <b>integram o Sistema de Segurança Pública</b>; foram afastadas as interpretações que as excluíam"],
      ["RE 608.588 · Tema 656 (20/02/2025)", "É constitucional o exercício, pelas guardas, de <b>ações de segurança urbana</b>, inclusive <b>policiamento ostensivo e comunitário</b>, respeitadas as atribuições dos demais órgãos e <b>excluída a atividade de polícia judiciária</b>"],
      ["RE 658.570 · Tema 472 (2015)", "É constitucional atribuir às guardas o <b>poder de polícia de trânsito</b>, inclusive a imposição de sanções administrativas previstas em lei"]], ["30%", None]) +
     ATENCAO(p("Os resumos vêm de notícias oficiais do STF e de fontes jurídicas, sem conferência do inteiro teor dos acórdãos. Confira a redação das teses no portal do STF antes da prova.")) +
     PEGADINHA("<ul><li><b>Errado:</b> “Após o Tema 656, a guarda pode instaurar inquérito.” <b>Certo:</b> a polícia judiciária foi <b>expressamente excluída</b>.</li></ul>"))

    treino(3, [
     ("Segurança pública é dever do Estado, direito e responsabilidade de todos.", "C", "CF, art. 144, caput."),
     ("As guardas municipais estão previstas no inciso VI do art. 144 da Constituição.", "E", "Estão no § 8º; o inciso VI trata das polícias penais."),
     ("Às polícias militares cabem a polícia ostensiva e a preservação da ordem pública.", "C", "Art. 144, § 5º."),
     ("Segundo o STF (ADPF 995), as guardas municipais integram o Sistema de Segurança Pública.", "C", "Decisão de 2023."),
     ("No Tema 656, o STF autorizou as guardas a exercer polícia judiciária.", "E", "A polícia judiciária foi excluída."),
     ("A segurança viária compreende educação, engenharia e fiscalização de trânsito.", "C", "Art. 144, § 10, I.")])

# ================================================================ UNIDADE 7 · DIREITOS HUMANOS E USO DA FORÇA
def unidade7():
    opener("07", "UNIDADE 7", "Direitos humanos e uso proporcional da força", ["Direitos humanos para o profissional de segurança", "Uso da força: Lei 13.060/2014 e Decreto 12.341/2024", "Abuso de autoridade"], "U7")

    add(topico('Direitos humanos para o <span class="hl">guarda</span>', 'Por que o tema é central na atuação de segurança.', "A19",
      p("Direitos humanos são os direitos básicos de toda pessoa, pelo simples fato de ser humana: vida, liberdade, integridade, dignidade, igualdade."),
      p("Para o guarda, direitos humanos não são “direitos de bandido”: são as regras que protegem todos, inclusive o próprio agente. Atuar respeitando esses direitos dá legitimidade e segurança jurídica à ocorrência."),
      "são reconhecidos na Constituição (art. 1º, III, e art. 5º) e em tratados internacionais, como a <b>Declaração Universal dos Direitos Humanos</b> (ONU, 10/12/1948). A Lei 13.022/2014 põe a proteção dos direitos humanos fundamentais como <b>primeiro princípio</b> de atuação das guardas (art. 3º, I).",
      p("Em uma ocorrência de briga, o guarda contém o agressor, mas garante que ele receba atendimento médico se estiver ferido e não seja agredido por populares. Protege os direitos de todos os envolvidos."),
      "a banca apresenta afirmações como “direitos humanos só protegem vítimas” ou pergunta qual é o primeiro princípio do art. 3º da Lei 13.022/2014.",
      "<ul><li><b>Errado:</b> “Direitos humanos não se aplicam a quem cometeu crime.” <b>Certo:</b> são <b>universais</b>; o preso conserva o direito à integridade física e moral (CF, art. 5º, XLIX).</li></ul>",
      "Direitos humanos: <strong>universais</strong>, de todos. Primeiro princípio da guarda: <strong>proteção dos direitos humanos fundamentais</strong> (Lei 13.022/2014, art. 3º, I). DUDH: <strong>ONU, 1948</strong>.", 7))

    add(topico('Uso <span class="hl">proporcional</span> da força', 'Lei 13.060/2014 e Decreto 12.341/2024.', "A20",
      p("É usar a força somente quando necessário, na medida certa e de forma progressiva, dando prioridade aos instrumentos de menor potencial ofensivo."),
      p("Imagine uma escada: presença, diálogo, comandos verbais, contenção com as mãos, instrumentos de menor potencial ofensivo e, só em último caso, arma de fogo. Sobe-se um degrau apenas se o anterior não resolver, e desce-se assim que a ameaça diminui."),
      "a <b>Lei 13.060/2014</b> determina que os órgãos de segurança pública priorizem instrumentos de menor potencial ofensivo, observados os princípios de legalidade, necessidade, razoabilidade e proporcionalidade, e veda o uso de arma de fogo contra pessoa em fuga desarmada ou que não represente risco imediato, e contra veículo que desrespeite bloqueio policial, salvo se houver risco. O <b>Decreto 12.341/2024</b>, que a regulamenta, lista os princípios de legalidade, precaução, necessidade, proporcionalidade, razoabilidade, responsabilização e não discriminação, e diz que a arma de fogo é <b>medida de último recurso</b>.",
      p("Um homem desarmado foge de uma abordagem correndo pela praça, sem ameaçar ninguém. Atirar nele é ilegítimo. O correto é acompanhar, pedir apoio e, se possível, conter sem disparos."),
      "a banca troca “progressivo” por “máximo” ou afirma que é legítimo atirar em quem foge.",
      "<ul><li><b>Errado:</b> “É legítimo o disparo contra veículo que fura bloqueio, em qualquer caso.” <b>Certo:</b> só se o ato representar risco de morte ou lesão aos agentes ou a terceiros.</li><li>Pela Lei 13.060/2014, quem é atingido deve receber socorro, e a família deve ser comunicada.</li></ul>",
      "Força: <strong>legalidade, necessidade, razoabilidade, proporcionalidade</strong> · prioridade ao <strong>menor potencial ofensivo</strong> · arma de fogo = <strong>último recurso</strong> · nunca contra <strong>fuga desarmada sem risco</strong>.", 7))

    atencao(table(["Decreto 12.341/2024", "Regra (em síntese)"], [
      ["Princípios (art. 2º)", "Legalidade, precaução, necessidade, proporcionalidade, razoabilidade, responsabilização e não discriminação"],
      ["Antes da força (art. 3º, § 1º)", "Priorizar comunicação, negociação e técnicas que impeçam a escalada da violência"],
      ["Arma de fogo (art. 3º, § 2º)", "Medida de último recurso"],
      ["Vedações (art. 3º, § 3º)", "Contra pessoa em fuga desarmada ou que não represente risco imediato; contra veículo que desrespeite bloqueio, salvo risco"],
      ["Depois (art. 3º, § 5º)", "Relatório circunstanciado sempre que o uso da força resultar em lesão ou morte"],
      ["Capacitação (art. 4º)", "Obrigatória e anual, durante o horário de serviço"],
      ["Equipamentos (art. 6º, III)", "Pelo menos dois instrumentos de menor potencial ofensivo por profissional em serviço"]], ["30%", None]) +
     ATENCAO(p("O decreto se dirige aos “profissionais de segurança pública” e aos órgãos de segurança pública dos Estados, do DF e dos Municípios. O texto lido não cita as guardas municipais pelo nome; o STF reconheceu que as guardas integram o Sistema de Segurança Pública (ADPF 995). Na prova, siga o enunciado.")) +
     MEMORIZE("Decreto 12.341/2024: <strong>arma de fogo = último recurso</strong> · <strong>relatório</strong> se houver lesão ou morte · <strong>capacitação anual</strong>."),
     ["Último recurso", "Relatório circunstanciado", "Menor potencial ofensivo"], "Decreto 12.341/2024")

    add(H(7, 'Abuso de <span class="hl">autoridade</span>', 'Lei 13.869/2019: os crimes mais ligados à atuação de rua.', "A21") +
     oque(p("É o crime praticado por <strong>agente público</strong> que, no exercício da função ou a pretexto de exercê-la, abusa do poder que lhe foi atribuído. Só há crime se houver a <strong>finalidade específica</strong> de prejudicar alguém, beneficiar a si ou a terceiro, ou por mero capricho ou satisfação pessoal (art. 1º, § 1º). A divergência na interpretação da lei ou na avaliação de fatos e provas <strong>não</strong> configura abuso (§ 2º).")) +
     table(["Artigo", "Conduta (em síntese)", "Pena"], [
      ["Art. 13", "Constranger o preso, com violência, grave ameaça ou redução da capacidade de resistência, a exibir-se à curiosidade pública, a situação vexatória ou a produzir prova contra si", "Detenção de 1 a 4 anos, e multa"],
      ["Art. 16", "Deixar de identificar-se ou identificar-se falsamente ao preso por ocasião de sua captura", "Detenção de 6 meses a 2 anos, e multa"],
      ["Art. 22", "Invadir ou permanecer em imóvel alheio, sem determinação judicial ou fora das condições legais. Não há crime para prestar socorro ou quando houver fundados indícios de flagrante delito ou desastre (§ 2º)", "Detenção de 1 a 4 anos, e multa"],
      ["Art. 33", "Exigir informação ou cumprimento de obrigação sem expresso amparo legal", "Detenção de 6 meses a 2 anos, e multa"]], ["12%", "60%", None]) +
     p("A ação penal desses crimes é <strong>pública incondicionada</strong> (art. 3º). O conceito de agente público é amplo: inclui quem exerce função pública ainda que transitoriamente ou sem remuneração (art. 2º, parágrafo único).") +
     PEGADINHA("<ul><li><b>Errado:</b> “Qualquer erro de interpretação da lei pelo agente configura abuso de autoridade.” <b>Certo:</b> a divergência de interpretação <b>não</b> configura (art. 1º, § 2º); exige-se finalidade específica.</li></ul>"))

    treino(7, [
     ("A Lei 13.060/2014 determina a prioridade de instrumentos de menor potencial ofensivo.", "C", "Base do uso progressivo da força."),
     ("É legítimo atirar contra pessoa em fuga, desarmada e sem representar risco.", "E", "Vedado pela Lei 13.060/2014 e pelo Decreto 12.341/2024."),
     ("Pelo Decreto 12.341/2024, a arma de fogo é medida de último recurso.", "C", "Art. 3º, § 2º."),
     ("Uso da força que resulte em lesão ou morte exige relatório circunstanciado.", "C", "Decreto 12.341/2024, art. 3º, § 5º."),
     ("A simples divergência na interpretação da lei configura crime de abuso de autoridade.", "E", "Não configura (Lei 13.869/2019, art. 1º, § 2º)."),
     ("Expor o preso à curiosidade pública, mediante constrangimento, pode configurar abuso de autoridade.", "C", "Lei 13.869/2019, art. 13.")])

# ================================================================ UNIDADE 8 · ECA
def unidade8():
    opener("08", "UNIDADE 8", "Criança e adolescente (ECA)", ["Conceitos e proteção", "Ato infracional e apreensão"], "U8")

    add(topico('Criança, adolescente e <span class="hl">proteção</span>', 'ECA (Lei nº 8.069/1990), arts. 2º, 13, 18 e 101.', "A22",
      p("O Estatuto da Criança e do Adolescente (ECA) é a lei que protege quem tem menos de 18 anos. Criança é a pessoa até 12 anos incompletos; adolescente, entre 12 e 18 anos (art. 2º)."),
      p("Crianças e adolescentes têm todos os direitos de qualquer pessoa e mais uma proteção especial, porque estão em desenvolvimento. O guarda, sobretudo na segurança escolar, convive com esse público e precisa conhecer as regras."),
      "é dever de todos velar pela dignidade da criança e do adolescente, pondo-os a salvo de tratamento desumano, violento, aterrorizante, vexatório ou constrangedor (art. 18). Os casos de suspeita ou confirmação de castigo físico, tratamento cruel ou degradante e maus-tratos serão <b>obrigatoriamente comunicados ao Conselho Tutelar</b> (art. 13). O Conselho Tutelar é órgão permanente e autônomo, não jurisdicional (art. 131).",
      p("Durante a ronda escolar, um guarda percebe marcas de agressão em uma criança, que conta apanhar em casa. A conduta correta é acionar o <b>Conselho Tutelar</b> e, se houver crime em andamento, as autoridades policiais."),
      "pede-se a idade que separa criança de adolescente (12 anos) ou a quem comunicar suspeita de maus-tratos (Conselho Tutelar).",
      "<ul><li><b>Errado:</b> “Criança é a pessoa até 14 anos.” <b>Certo:</b> até <b>12 anos incompletos</b>.</li><li>Criança que pratica ato infracional recebe <b>medidas de proteção</b> (art. 101), não medida socioeducativa (art. 105).</li></ul>",
      "Criança: <strong>até 12 anos incompletos</strong> · adolescente: <strong>12 a 18</strong> · maus-tratos: comunicação <strong>obrigatória</strong> ao <strong>Conselho Tutelar</strong>.", 8))

    add(H(8, 'Ato infracional e <span class="hl">apreensão</span>', 'ECA, arts. 103 a 112 e 171 a 178.', "A23") +
     table(["Regra", "Conteúdo (em síntese)"], [
      ["Ato infracional (art. 103)", "Conduta descrita como crime ou contravenção penal, praticada por criança ou adolescente"],
      ["Inimputabilidade (art. 104)", "Menores de 18 anos são penalmente inimputáveis; considera-se a idade <b>na data do fato</b>"],
      ["Privação de liberdade (art. 106)", "Só em <b>flagrante</b> de ato infracional ou por ordem escrita e fundamentada do juiz; o adolescente tem direito de saber quem o apreendeu e de ser informado de seus direitos"],
      ["Comunicação (art. 107)", "A apreensão e o local onde está o adolescente devem ser comunicados <b>incontinenti</b> (imediatamente) ao juiz e à família ou pessoa indicada"],
      ["Encaminhamento (art. 172)", "O adolescente apreendido em flagrante será, desde logo, encaminhado à autoridade policial competente"],
      ["Transporte (art. 178)", "Não pode ser conduzido em <b>compartimento fechado</b> de veículo policial em condições atentatórias à dignidade ou que impliquem risco"],
      ["Medidas socioeducativas (art. 112)", "Advertência · obrigação de reparar o dano · prestação de serviços à comunidade · liberdade assistida · semiliberdade · internação"],
      ["Internação (art. 121)", "Prazo máximo de <b>3 anos</b>; liberação compulsória aos <b>21 anos</b>"]], ["28%", None]) +
     PEGADINHA("<ul><li><b>Errado:</b> “O adolescente que comete ato infracional é preso e indiciado como um adulto.” <b>Certo:</b> é <b>apreendido</b> e encaminhado à autoridade policial; responde pelo ECA.</li><li>Submeter criança ou adolescente sob sua guarda ou vigilância a vexame ou constrangimento é crime (art. 232: detenção de 6 meses a 2 anos).</li></ul>") +
     MEMORIZE("Adolescente: <strong>apreensão</strong> (não prisão) · comunicar <strong>imediatamente</strong> juiz e família · nada de <strong>porta-malas/compartimento fechado</strong> · internação máx. <strong>3 anos</strong>, libera aos <strong>21</strong>."))

    treino(8, [
     ("Pelo ECA, criança é a pessoa até 12 anos de idade incompletos.", "C", "Art. 2º."),
     ("A suspeita de maus-tratos contra criança deve ser obrigatoriamente comunicada ao Conselho Tutelar.", "C", "Art. 13."),
     ("O adolescente pode ser conduzido em compartimento fechado da viatura, em qualquer condição.", "E", "Vedado em condições atentatórias à dignidade ou com risco (art. 178)."),
     ("Para o ECA, considera-se a idade do adolescente na data do fato.", "C", "Art. 104, parágrafo único."),
     ("A internação de adolescente pode durar até 5 anos.", "E", "Máximo de 3 anos (art. 121, § 3º)."),
     ("A criança que pratica ato infracional recebe medida socioeducativa de internação.", "E", "Recebe medidas de proteção (art. 105).")])

# ================================================================ UNIDADE 9 · TRÂNSITO
def unidade9():
    opener("09", "UNIDADE 9", "Noções de trânsito para a guarda", ["A guarda e o Código de Trânsito", "Regras que o guarda mais aplica"], "U9")

    add(topico('A guarda e o <span class="hl">Código de Trânsito</span>', 'Lei 13.022/2014, art. 5º, VI; CTB, arts. 24 e 280.', "A24",
      p("O Código de Trânsito Brasileiro (CTB, Lei 9.503/1997) organiza o trânsito no país. A guarda pode atuar no trânsito quando a competência lhe é conferida."),
      p("Em Parnaíba, a própria lei municipal da guarda prevê a fiscalização do trânsito e cria a GOTRAN (Guarda Ostensiva de Trânsito). Por isso o tema tende a aparecer na parte profissional da prova (conteúdo estimado)."),
      "a Lei 13.022/2014 permite à guarda exercer as competências de trânsito que lhe forem conferidas nas vias municipais, nos termos do CTB, ou de forma concorrente, mediante convênio (art. 5º, VI). O CTB atribui aos órgãos municipais fiscalizar, autuar e aplicar penalidades no âmbito de sua competência (art. 24), e o auto de infração é lavrado por servidor civil, estatutário ou celetista, ou policial militar designado pela autoridade de trânsito (art. 280, § 4º). O STF admitiu o poder de polícia de trânsito pelas guardas (Tema 472).",
      p("Um agente da GOTRAN orienta o fluxo em um cruzamento com o semáforo apagado. Seus gestos prevalecem sobre as demais regras de circulação (CTB, art. 89)."),
      "a banca cobra a ordem de prevalência da sinalização ou se a guarda pode autuar.",
      "<ul><li><b>Errado:</b> “O semáforo prevalece sobre as ordens do agente de trânsito.” <b>Certo:</b> o agente prevalece (art. 89).</li></ul>",
      "Prevalência: <strong>agente > semáforo > sinais > normas</strong>. Guarda no trânsito: <strong>CTB ou convênio</strong> (Lei 13.022, art. 5º, VI). Parnaíba: <strong>GOTRAN</strong>.", 9))

    add(H(9, 'Regras que o guarda <span class="hl">mais aplica</span>', 'CTB: pedestres, prioridade e infrações frequentes.', "A25") +
     table(["Tema", "Regra (em síntese)"], [
      ["Responsabilidade (art. 29, § 2º)", "Os veículos maiores são responsáveis pelos menores, os motorizados pelos não motorizados, e todos pela segurança dos pedestres"],
      ["Emergência (art. 29, VII)", "Veículos de socorro, polícia e fiscalização de trânsito têm prioridade quando em serviço de urgência, com alarme sonoro e luz vermelha intermitente ligados"],
      ["Pedestres (arts. 69 e 70)", "Devem usar a faixa existente a até 50 metros; na faixa, têm prioridade, salvo onde houver semáforo"],
      ["Velocidade urbana (art. 61)", "Sem placa: 80 km/h (trânsito rápido), 60 (arterial), 40 (coletora), 30 (local)"],
      ["Álcool (arts. 165 e 165-A)", "Infração gravíssima, multa multiplicada por 10 e suspensão por 12 meses; a recusa ao teste tem as mesmas penalidades"],
      ["Celular (art. 252, parágrafo único)", "Dirigir segurando ou manuseando o celular é infração gravíssima"],
      ["Pontuação (art. 259)", "Gravíssima 7, grave 5, média 4, leve 3 pontos"]], ["30%", None]) +
     ATENCAO(p("Esta unidade é uma noção para a parte profissional. Se o edital trouxer Legislação de Trânsito como disciplina própria, estude o CTB em material específico.")))

    treino(9, [
     ("A guarda municipal pode exercer competências de trânsito nas vias municipais, nos termos do CTB, ou por convênio.", "C", "Lei 13.022/2014, art. 5º, VI."),
     ("As ordens do agente de trânsito prevalecem sobre o semáforo.", "C", "CTB, art. 89."),
     ("Pela Lei Municipal 1.989/2003, a GOTRAN é a Guarda Ostensiva de Trânsito.", "C", "Art. 7º, § 2º, I."),
     ("O pedestre deve usar a faixa sempre que ela existir a até 100 metros.", "E", "Até 50 metros (CTB, art. 69)."),
     ("A recusa ao teste do etilômetro não gera penalidade administrativa.", "E", "Mesmas penalidades do art. 165 (art. 165-A)."),
     ("A infração gravíssima computa 7 pontos.", "C", "CTB, art. 259.")])
