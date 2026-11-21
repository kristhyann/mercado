# -*- coding: utf-8 -*-
"""Direitos Humanos e Cidadania + Administração Pública."""
from render import Topico, tab, bl, h3, caixa, fluxo, num
from qbase import Q

DH_TOPICOS = [
    Topico('Conceito e características dos direitos humanos',
        'Direitos humanos são os <b>direitos inerentes a toda pessoa</b>, pelo simples fato de ser humana, independentemente de nacionalidade, sexo, cor, religião, condição social ou qualquer outra característica.',
        [
            'Eles protegem bens essenciais como a vida, a liberdade, a igualdade, a integridade física e a dignidade. Quando reconhecidos na Constituição de um país, costumam ser chamados de <b>direitos fundamentais</b>.',
            tab(['Característica', 'Significado'], [
                ['Universalidade', 'Valem para todas as pessoas.'],
                ['Inalienabilidade', 'Não podem ser vendidos ou transferidos.'],
                ['Indivisibilidade e interdependência', 'Formam um conjunto: direitos civis, políticos, sociais e culturais se complementam.'],
                ['Imprescritibilidade', 'Não se perdem com o passar do tempo.'],
                ['Historicidade', 'Foram conquistados e ampliados ao longo da história.'],
                ['Relatividade (não são absolutos)', 'Podem ser limitados para harmonizar com outros direitos, nos casos previstos.'],
            ], [5.0, 12.0], 9.2),
            h3('“Gerações” (ou dimensões) de direitos — classificação didática'),
            tab(['Dimensão', 'Ideia central', 'Exemplos'], [
                ['1ª', 'Liberdade: limitar o poder do Estado.', 'Vida, liberdade de expressão, direito de voto.'],
                ['2ª', 'Igualdade: prestações do Estado.', 'Educação, saúde, trabalho, previdência.'],
                ['3ª', 'Fraternidade/solidariedade: direitos coletivos e difusos.', 'Meio ambiente equilibrado, paz, desenvolvimento.'],
            ], [2.4, 6.6, 8.0], 9.2),
        ],
        exemplos=['Uma pessoa presa continua tendo direito à integridade física e moral (CF, art. 5º, XLIX).'],
        erros=['Achar que direitos humanos protegem só “alguns grupos”.', 'Achar que quem comete crime perde todos os direitos.'],
        resumo=['Direitos humanos: universais, inalienáveis, indivisíveis, imprescritíveis.', 'Dimensões: liberdade, igualdade, solidariedade.'],
        exercicios=[
            Q('Direitos Humanos', 'A característica segundo a qual os direitos humanos valem para todas as pessoas é a',
              'universalidade.', ['temporariedade.', 'exclusividade.', 'transferibilidade.', 'territorialidade restrita.'], 'Universalidade: titularidade de todos os seres humanos.', ''),
            Q('Direitos Humanos', 'O direito a um meio ambiente equilibrado é usualmente classificado como de',
              'terceira dimensão (solidariedade).', ['primeira dimensão (liberdade).', 'segunda dimensão (igualdade).', 'quinta dimensão exclusivamente.', 'nenhuma dimensão.'], 'Direitos difusos e coletivos, como meio ambiente e paz, são associados à 3ª dimensão.', ''),
        ]),

    Topico('Declaração Universal dos Direitos Humanos',
        'A Declaração Universal dos Direitos Humanos (DUDH) foi <b>adotada e proclamada pela Assembleia Geral das Nações Unidas em 10 de dezembro de 1948</b>, como ideal comum a ser atingido por todos os povos.',
        [
            'Elaborada após a Segunda Guerra Mundial, a DUDH reúne 30 artigos que tratam de direitos civis, políticos, econômicos, sociais e culturais. Por isso, 10 de dezembro é o Dia Internacional dos Direitos Humanos.',
            tab(['Artigo da DUDH', 'Ideia central (síntese)'], [
                ['1º', 'Todos os seres humanos nascem livres e iguais em dignidade e em direitos.'],
                ['3º', 'Direito à vida, à liberdade e à segurança pessoal.'],
                ['5º', 'Ninguém será submetido a tortura nem a tratamento ou castigo cruel, desumano ou degradante.'],
                ['7º', 'Todos são iguais perante a lei e têm direito a igual proteção, sem discriminação.'],
                ['9º', 'Ninguém será arbitrariamente preso, detido ou exilado.'],
                ['11', 'Presunção de inocência até prova de culpa em julgamento público com garantias de defesa.'],
                ['19', 'Liberdade de opinião e de expressão.'],
                ['20', 'Liberdade de reunião e associação pacíficas.'],
            ], [3.0, 14.0], 9.2),
            caixa('dica', 'Vários desses direitos aparecem também no art. 5º da CF/88: proibição da tortura (III), presunção de inocência (LVII), liberdade de expressão (IV), reunião (XVI).'),
        ],
        exemplos=['A proibição da tortura está no art. 5º da DUDH e no art. 5º, III, da CF.'],
        erros=['Confundir 1948 (DUDH) com 1945 (criação da ONU) ou 1988 (CF).'],
        resumo=['DUDH: ONU, 10/12/1948, 30 artigos.', 'Liberdade, igualdade, dignidade, proibição da tortura, presunção de inocência.'],
        exercicios=[
            Q('Direitos Humanos', 'A Declaração Universal dos Direitos Humanos foi adotada pela Assembleia Geral da ONU em',
              '1948.', ['1945.', '1964.', '1988.', '2001.'], 'Adotada em 10 de dezembro de 1948.', '1945 é a criação da ONU.'),
            Q('Direitos Humanos', 'Segundo o artigo 1º da DUDH,',
              'todos os seres humanos nascem livres e iguais em dignidade e em direitos.', ['os direitos dependem da nacionalidade.', 'apenas cidadãos eleitores têm direitos.', 'a dignidade é concedida pelo Estado.', 'os direitos valem só em tempo de paz.'], 'Texto do art. 1º da DUDH.', ''),
        ]),

    Topico('Dignidade humana e igualdade',
        'A <b>dignidade da pessoa humana</b> é o valor de toda pessoa como fim em si mesma, que deve ser respeitada e protegida. A <b>igualdade</b> é o tratamento igual perante a lei e a proibição de discriminações injustas.',
        [
            'Na CF/88, a dignidade da pessoa humana é <b>fundamento da República</b> (art. 1º, III). A igualdade aparece no caput do art. 5º (“todos são iguais perante a lei”) e no inciso I (homens e mulheres são iguais em direitos e obrigações).',
            tab(['Igualdade formal', 'Igualdade material'], [
                ['Todos são iguais perante a lei: a lei se aplica igualmente a todos.', 'Tratar desigualmente os desiguais, na medida de sua desigualdade, para reduzir desigualdades reais (ex.: reserva de vagas para pessoas com deficiência — CF, art. 37, VIII).'],
            ], [8.5, 8.5], 9.2),
            'O art. 3º, IV, da CF estabelece como objetivo promover o bem de todos, <b>sem preconceitos</b> de origem, raça, sexo, cor, idade e quaisquer outras formas de discriminação. O art. 5º, XLI, determina que a lei punirá qualquer discriminação atentatória dos direitos e liberdades fundamentais, e o inciso XLII torna o racismo crime inafiançável e imprescritível.',
        ],
        exemplos=['Atender todas as pessoas com o mesmo respeito, independentemente de aparência, origem ou condição social, é aplicação da dignidade e da igualdade.'],
        erros=['Confundir igualdade material com privilégio.'],
        resumo=['Dignidade: fundamento da República (art. 1º, III).', 'Igualdade formal e material.', 'Racismo: inafiançável e imprescritível.'],
        exercicios=[
            Q('Direitos Humanos', 'Na CF/88, a dignidade da pessoa humana é',
              'fundamento da República Federativa do Brasil.', ['objetivo das relações internacionais.', 'princípio da administração pública.', 'direito social do art. 6º.', 'competência dos Municípios.'], 'Art. 1º, III.', ''),
            Q('Direitos Humanos', 'A reserva de vagas em concursos para pessoas com deficiência é exemplo de',
              'igualdade material.', ['igualdade apenas formal.', 'violação da igualdade.', 'privilégio inconstitucional.', 'princípio da publicidade.'], 'Tratar desigualmente os desiguais para promover igualdade real.', ''),
        ]),

    Topico('Cidadania',
        'Cidadania é a <b>condição de quem participa da vida em sociedade com direitos e deveres</b>, incluindo a participação política e o acesso a direitos civis e sociais.',
        [
            'A cidadania é fundamento da República (CF, art. 1º, II). Em sentido estrito, cidadão é quem está no gozo dos direitos políticos (pode votar). Em sentido amplo, cidadania envolve exercer direitos e cumprir deveres: votar, fiscalizar o poder público, respeitar as leis, conviver com as diferenças, cuidar dos espaços públicos.',
            tab(['Instrumento de cidadania', 'Exemplo'], [
                ['Voto', 'Eleições periódicas (art. 14).'], ['Plebiscito, referendo, iniciativa popular', 'Participação direta (art. 14).'],
                ['Ação popular', 'Qualquer cidadão pode propor contra ato lesivo ao patrimônio público (art. 5º, LXXIII).'],
                ['Direito de petição', 'Pedir providências aos poderes públicos, sem pagar taxas (art. 5º, XXXIV).'],
                ['Acesso à informação', 'Receber informações de órgãos públicos (art. 5º, XXXIII; Lei nº 12.527/2011).'],
                ['Ouvidorias e conselhos', 'Reclamações e controle social (ex.: ouvidoria da guarda — Lei nº 13.022/2014, art. 13).'],
            ], [5.6, 11.4], 9.2),
        ],
        exemplos=['Um morador que registra reclamação na ouvidoria sobre a iluminação de uma praça está exercendo a cidadania.'],
        erros=['Reduzir cidadania apenas ao voto.'],
        resumo=['Cidadania: direitos + deveres + participação.', 'Instrumentos: voto, plebiscito, referendo, iniciativa popular, ação popular, petição, acesso à informação.'],
        exercicios=[
            Q('Cidadania', 'São gratuitos para todos, independentemente do pagamento de taxas, segundo o art. 5º, XXXIV, da CF:',
              'o direito de petição aos poderes públicos e a obtenção de certidões para defesa de direitos.', ['todas as ações judiciais.', 'os serviços cartorários de qualquer natureza.', 'as custas de mandado de segurança.', 'os honorários advocatícios.'], 'Art. 5º, XXXIV.', ''),
            Q('Cidadania', 'A cidadania, na CF/88, é',
              'fundamento da República (art. 1º, II).', ['objetivo do art. 3º.', 'princípio das relações internacionais.', 'princípio exclusivo da administração pública.', 'direito social do art. 7º.'], 'Art. 1º, II.', ''),
        ]),

    Topico('Direitos humanos na atuação pública e grupos vulneráveis',
        'Agentes públicos, especialmente os da segurança, devem atuar como <b>garantidores dos direitos humanos</b>: proteger a vida, respeitar a dignidade e usar a força somente quando necessária e de forma proporcional.',
        [
            tab(['Princípio de atuação', 'Base normativa'], [
                ['Proteção dos direitos humanos fundamentais, da cidadania e das liberdades públicas', 'Lei nº 13.022/2014, art. 3º, I'],
                ['Preservação da vida, redução do sofrimento e diminuição das perdas', 'Lei nº 13.022/2014, art. 3º, II'],
                ['Uso progressivo da força', 'Lei nº 13.022/2014, art. 3º, V'],
                ['Legalidade, necessidade, razoabilidade e proporcionalidade; prioridade a instrumentos de menor potencial ofensivo', 'Lei nº 13.060/2014, art. 2º'],
                ['Socorro imediato a feridos e comunicação à família', 'Lei nº 13.060/2014, art. 6º'],
                ['Proibição de tortura e de tratamento desumano ou degradante', 'CF, art. 5º, III'],
            ], [11.0, 6.0], 9.0),
            h3('Grupos que recebem proteção especial'),
            tab(['Grupo', 'Norma', 'Ponto-chave'], [
                ['Crianças e adolescentes', 'CF, art. 227; ECA (Lei nº 8.069/1990)', 'Prioridade absoluta. Criança: até 12 anos incompletos; adolescente: de 12 a 18 anos. Conduta descrita como crime praticada por eles é ato infracional.'],
                ['Pessoas idosas', 'Estatuto da Pessoa Idosa (Lei nº 10.741/2003)', 'Pessoas com 60 anos ou mais.'],
                ['Mulheres em situação de violência', 'Lei Maria da Penha (Lei nº 11.340/2006)', 'Formas de violência doméstica: física, psicológica, sexual, patrimonial e moral.'],
                ['Pessoas com deficiência', 'CF, art. 37, VIII; Estatuto da Pessoa com Deficiência (Lei nº 13.146/2015)', 'Acessibilidade, inclusão e reserva de vagas.'],
            ], [3.8, 5.6, 7.6], 8.9),
        ],
        exemplos=['Ao encontrar uma criança perdida em evento público, a prioridade é sua proteção e a localização segura dos responsáveis ou o acionamento do Conselho Tutelar, quando for o caso.'],
        erros=['Ver direitos humanos como obstáculo ao trabalho: eles também protegem os próprios agentes.'],
        resumo=['O agente público é garantidor de direitos.', 'Proteção especial: crianças e adolescentes, idosos, mulheres, pessoas com deficiência.'],
        exercicios=[
            Q('Direitos Humanos — atuação pública', 'Segundo o ECA, considera-se criança a pessoa',
              'até doze anos de idade incompletos.', ['até quatorze anos.', 'até dezoito anos.', 'até dez anos completos.', 'até dezesseis anos.'], 'ECA, art. 2º.', ''),
            Q('Direitos Humanos — atuação pública', 'A Lei Maria da Penha prevê como formas de violência doméstica e familiar contra a mulher:',
              'física, psicológica, sexual, patrimonial e moral.', ['apenas física.', 'física e sexual, apenas.', 'apenas psicológica.', 'patrimonial e financeira, apenas.'], 'Lei nº 11.340/2006, art. 7º.', ''),
        ]),
]

DH_REVISAO = [
    Q('Revisão — Direitos Humanos', 'O Dia Internacional dos Direitos Humanos é celebrado em',
      '10 de dezembro.', ['5 de outubro.', '7 de setembro.', '1º de maio.', '15 de novembro.'], 'Data da adoção da DUDH (1948).', '5 de outubro é a data da CF/88.'),
    Q('Revisão — Direitos Humanos', 'Pessoa idosa, segundo o Estatuto da Pessoa Idosa, é aquela com idade',
      'igual ou superior a 60 anos.', ['igual ou superior a 65 anos.', 'superior a 70 anos.', 'igual ou superior a 55 anos.', 'igual ou superior a 75 anos.'], 'Lei nº 10.741/2003, art. 1º.', ''),
    Q('Revisão — Direitos Humanos', 'A característica dos direitos humanos que impede sua venda ou transferência é a',
      'inalienabilidade.', ['universalidade.', 'historicidade.', 'relatividade.', 'temporariedade.'], 'Inalienáveis: não podem ser negociados.', ''),
    Q('Revisão — Direitos Humanos', 'É princípio mínimo de atuação das guardas municipais ligado aos direitos humanos:',
      'a preservação da vida, a redução do sofrimento e a diminuição das perdas.', ['a apuração de crimes.', 'o julgamento de infratores.', 'o uso máximo da força.', 'a dispensa de socorro a feridos.'], 'Lei nº 13.022/2014, art. 3º, II.', ''),
    Q('Revisão — Direitos Humanos', 'Tratar desigualmente os desiguais, na medida de sua desigualdade, corresponde à ideia de',
      'igualdade material.', ['igualdade formal apenas.', 'discriminação proibida.', 'princípio da publicidade.', 'soberania.'], 'A igualdade material busca reduzir desigualdades reais.', ''),
]

DH_RESUMO = [
    ['Conceito', 'Direitos inerentes a toda pessoa; na Constituição, chamados direitos fundamentais.'],
    ['Características', 'Universais, inalienáveis, indivisíveis, imprescritíveis, históricos, relativos.'],
    ['DUDH', 'ONU, 10/12/1948; igualdade, liberdade, proibição da tortura, presunção de inocência.'],
    ['Dignidade e igualdade', 'Dignidade: fundamento (art. 1º, III). Igualdade formal e material; combate à discriminação.'],
    ['Cidadania', 'Fundamento (art. 1º, II); voto, plebiscito, referendo, iniciativa popular, ação popular, petição.'],
    ['Atuação pública', 'Garantir direitos; uso progressivo da força; proteção especial a vulneráveis (ECA, Pessoa Idosa, Maria da Penha).'],
]

# ======================================================================= ADMINISTRAÇÃO PÚBLICA
ADM_TOPICOS = [
    Topico('Conceito de administração pública',
        'Administração pública é o <b>conjunto de órgãos, entidades e agentes</b> que exercem a função administrativa do Estado, prestando serviços e gerindo os interesses da coletividade.',
        [
            tab(['Sentido', 'Significado'], [
                ['Subjetivo (orgânico)', 'Quem exerce a função: órgãos, entidades e agentes públicos.'],
                ['Objetivo (material)', 'A atividade exercida: serviços públicos, poder de polícia, fomento, intervenção.'],
            ], [4.6, 12.4], 9.2),
            tab(['Administração direta', 'Administração indireta'], [
                ['União, Estados, DF e Municípios, por meio de seus órgãos (ministérios, secretarias). A guarda municipal integra a administração direta do Município, subordinada ao prefeito.', 'Entidades com personalidade jurídica própria, criadas ou autorizadas por lei: autarquias, fundações públicas, empresas públicas e sociedades de economia mista (CF, art. 37, XIX).'],
            ], [8.5, 8.5], 9.0),
            h3('Agentes públicos'),
            'Agente público é toda pessoa que exerce função pública, ainda que temporariamente ou sem remuneração. Servidor público ocupa cargo público, geralmente efetivo (por concurso) ou em comissão (livre nomeação para direção, chefia e assessoramento).',
        ],
        exemplos=['A Secretaria Municipal de Educação é órgão da administração direta; uma autarquia municipal de trânsito, se existir, integra a administração indireta.'],
        erros=['Confundir órgão (sem personalidade jurídica própria) com entidade (com personalidade jurídica).'],
        resumo=['Administração direta: entes e seus órgãos.', 'Indireta: autarquias, fundações, empresas públicas, sociedades de economia mista.'],
        exercicios=[
            Q('Administração Pública', 'São entidades da administração indireta:',
              'autarquias, fundações públicas, empresas públicas e sociedades de economia mista.', ['ministérios e secretarias.', 'Câmara Municipal e Assembleia Legislativa.', 'partidos políticos.', 'sindicatos e associações.'], 'CF, art. 37, XIX.', ''),
            Q('Administração Pública', 'A guarda municipal, subordinada ao prefeito, integra',
              'a administração direta do Município.', ['a administração indireta federal.', 'o Poder Judiciário.', 'o Poder Legislativo municipal.', 'a iniciativa privada.'], 'É órgão do Executivo municipal (Lei nº 13.022/2014, art. 6º).', ''),
        ]),

    Topico('Princípios expressos: LIMPE',
        'O caput do art. 37 da CF determina que a administração pública direta e indireta de qualquer dos Poderes, de todos os entes, obedecerá aos princípios de <b>legalidade, impessoalidade, moralidade, publicidade e eficiência</b>.',
        [
            tab(['Princípio', 'Significado', 'Exemplo prático', 'Violação típica'], [
                ['Legalidade', 'A administração só pode agir quando e como a lei autoriza.', 'Aplicar multa prevista em lei, no valor legal.', 'Exigir documento que nenhuma norma prevê.'],
                ['Impessoalidade', 'Atuar pelo interesse público, sem favorecer ou perseguir pessoas; vedação de promoção pessoal.', 'Atendimento por ordem de chegada.', 'Placa de obra com nome e foto do prefeito (art. 37, § 1º).'],
                ['Moralidade', 'Agir com ética, honestidade, lealdade e boa-fé.', 'Recusar presentes de quem tem interesse no serviço.', 'Usar o cargo para obter vantagens.'],
                ['Publicidade', 'Divulgar os atos oficiais e garantir transparência, salvo sigilo legal.', 'Publicar o edital do concurso.', 'Esconder contratos sem justificativa legal.'],
                ['Eficiência', 'Buscar resultados com qualidade, rapidez e economia (incluído pela EC 19/1998).', 'Organizar escalas para cobrir horários de maior movimento.', 'Desperdício de recursos e demoras injustificadas.'],
            ], [2.6, 4.8, 4.8, 4.8], 8.8),
            caixa('dica', 'Legalidade para o particular (CF, art. 5º, II): pode fazer tudo o que a lei não proíbe. Legalidade para a administração (art. 37): só pode fazer o que a lei permite.'),
            h3('Princípios implícitos (reconhecidos pela doutrina e jurisprudência)'),
            bl(['<b>Supremacia do interesse público</b> sobre o privado e <b>indisponibilidade do interesse público</b>.', '<b>Razoabilidade e proporcionalidade:</b> medidas adequadas, necessárias e equilibradas.',
                '<b>Autotutela:</b> a administração pode anular seus atos ilegais e revogar os inconvenientes.', '<b>Continuidade do serviço público.</b>', '<b>Motivação:</b> indicar os fundamentos dos atos.']),
        ],
        exemplos=['Um servidor que dá prioridade ao atendimento de amigos viola a impessoalidade e a moralidade.'],
        erros=['Incluir razoabilidade no LIMPE (é princípio implícito).', 'Confundir publicidade (transparência) com propaganda pessoal.'],
        resumo=['LIMPE: Legalidade, Impessoalidade, Moralidade, Publicidade, Eficiência.', 'Eficiência foi incluída pela EC 19/1998.'],
        exercicios=[
            Q('Administração Pública', 'A placa de uma obra pública que traz o nome e a foto do prefeito, como promoção pessoal, viola principalmente o princípio da',
              'impessoalidade.', ['eficiência.', 'legalidade tributária.', 'continuidade.', 'autotutela.'], 'Art. 37, § 1º: a publicidade não pode caracterizar promoção pessoal de autoridades.', ''),
            Q('Administração Pública', 'O princípio da eficiência foi incluído no caput do art. 37 pela',
              'Emenda Constitucional nº 19/1998.', ['Constituição original de 1988.', 'Emenda Constitucional nº 104/2019.', 'Lei nº 13.022/2014.', 'Emenda Constitucional nº 90/2015.'], 'A EC 19/1998 (Reforma Administrativa) incluiu a eficiência.', ''),
        ]),

    Topico('Legalidade e impessoalidade em detalhe',
        'Esses dois princípios orientam o <b>dia a dia do servidor</b>: agir conforme a lei e tratar todos de forma igual, buscando o interesse público.',
        [
            h3('Legalidade'),
            'O servidor não age por vontade própria: ele executa o que a lei determina ou autoriza. Mesmo quando há margem de escolha (discricionariedade), essa margem existe porque a lei a concede e deve ser usada dentro dos limites legais, com razoabilidade.',
            tab(['Ato vinculado', 'Ato discricionário'], [
                ['A lei define todos os elementos; não há escolha (ex.: conceder aposentadoria a quem cumpre os requisitos).', 'A lei dá margem de conveniência e oportunidade, dentro de limites (ex.: definir o melhor horário de uma ronda preventiva).'],
            ], [8.5, 8.5], 9.0),
            h3('Impessoalidade'),
            bl(['Finalidade pública: o ato deve atender ao interesse coletivo, e não a interesses pessoais.', 'Igualdade de tratamento: concurso público, licitação, ordem de atendimento.',
                'Os atos são atribuídos ao órgão, e não à pessoa do agente.', 'Vedação de promoção pessoal na publicidade oficial (art. 37, § 1º).']),
        ],
        exemplos=['Um guarda que deixa de registrar uma infração cometida por um conhecido viola a impessoalidade (e a legalidade).'],
        erros=['Achar que discricionariedade é liberdade total.'],
        resumo=['Legalidade: agir conforme a lei.', 'Impessoalidade: interesse público, igualdade e vedação de promoção pessoal.'],
        exercicios=[
            Q('Administração Pública', 'Para a administração pública, o princípio da legalidade significa que ela',
              'só pode fazer o que a lei permite ou determina.', ['pode fazer tudo o que a lei não proíbe.', 'pode agir conforme a vontade do chefe.', 'não precisa seguir leis municipais.', 'só segue a lei em tempo de paz.'], 'Diferença em relação ao particular (art. 5º, II).', ''),
            Q('Administração Pública', 'O concurso público é uma forma de concretizar principalmente o princípio da',
              'impessoalidade.', ['autotutela.', 'continuidade.', 'hierarquia.', 'especialidade.'], 'Garante igualdade de oportunidades e escolha pelo mérito.', ''),
        ]),

    Topico('Moralidade, publicidade e eficiência em detalhe',
        'Esses princípios garantem que a administração seja <b>ética, transparente e eficiente</b>.',
        [
            h3('Moralidade'),
            'Não basta o ato ser legal: ele deve ser honesto e ético. A violação grave pode configurar <b>improbidade administrativa</b>, que, segundo o art. 37, § 4º, da CF, importa a suspensão dos direitos políticos, a perda da função pública, a indisponibilidade dos bens e o ressarcimento ao erário, sem prejuízo da ação penal. A ação popular também protege a moralidade administrativa (art. 5º, LXXIII).',
            h3('Publicidade'),
            'Os atos devem ser divulgados para conhecimento e controle da sociedade. A publicidade oficial deve ter caráter educativo, informativo ou de orientação social (art. 37, § 1º). A Lei de Acesso à Informação (Lei nº 12.527/2011) regulamenta o direito de receber informações dos órgãos públicos (art. 5º, XXXIII), ressalvadas as hipóteses de sigilo.',
            h3('Eficiência'),
            'Exige bons resultados com uso racional dos recursos: qualidade, rapidez, economia e foco no cidadão. A avaliação periódica de desempenho dos servidores e o planejamento das ações são expressões desse princípio.',
        ],
        exemplos=['Publicar o resultado do concurso no diário oficial (publicidade).', 'Planejar rondas conforme dados de ocorrências (eficiência).', 'Recusar vantagem oferecida por particular (moralidade).'],
        erros=['Achar que um ato legal é sempre moral.', 'Usar a publicidade oficial para propaganda pessoal.'],
        resumo=['Moralidade: ética e boa-fé; improbidade tem sanções do art. 37, § 4º.', 'Publicidade: transparência; Lei de Acesso à Informação.', 'Eficiência: resultados com qualidade e economia.'],
        exercicios=[
            Q('Administração Pública', 'Segundo o art. 37, § 4º, da CF, os atos de improbidade administrativa importarão, entre outras consequências,',
              'a suspensão dos direitos políticos.', ['a cassação definitiva da nacionalidade.', 'a pena de morte.', 'a prisão perpétua.', 'o banimento.'], 'Suspensão dos direitos políticos, perda da função, indisponibilidade dos bens e ressarcimento ao erário.', ''),
            Q('Administração Pública', 'A divulgação do edital de um concurso no diário oficial é exemplo de aplicação do princípio da',
              'publicidade.', ['eficiência exclusivamente.', 'pessoalidade.', 'autotutela.', 'continuidade.'], 'Publicidade garante conhecimento e controle.', ''),
        ]),

    Topico('Noções de serviço público e poder de polícia',
        '<b>Serviço público</b> é a atividade prestada pela administração (diretamente ou por delegação) para satisfazer necessidades da coletividade. <b>Poder de polícia</b> é a atividade que limita ou condiciona direitos individuais em favor do interesse público.',
        [
            tab(['Princípio do serviço público', 'Significado'], [
                ['Continuidade', 'O serviço não deve ser interrompido sem justificativa.'], ['Generalidade (universalidade)', 'Deve atender a todos, sem discriminação.'],
                ['Eficiência', 'Prestado com qualidade.'], ['Modicidade', 'Tarifas razoáveis, quando cobradas.'], ['Cortesia', 'Atendimento respeitoso ao usuário.'], ['Atualidade', 'Uso de técnicas e equipamentos modernos.'],
            ], [5.6, 11.4], 9.2),
            'Segundo o art. 30, V, da CF, compete ao Município organizar e prestar, diretamente ou sob regime de concessão ou permissão, os serviços públicos de interesse local, incluído o de transporte coletivo, que tem caráter essencial. O art. 37, § 3º, prevê a participação do usuário (reclamações, acesso a informações, representação contra abusos).',
            h3('Poder de polícia administrativa'),
            'Exemplos: fiscalização de posturas municipais, licenças de funcionamento, ordenamento urbano. A Lei nº 13.022/2014 (art. 5º, XII) prevê que a guarda se integre aos demais órgãos de poder de polícia administrativa, contribuindo para a normatização e a fiscalização das posturas e do ordenamento urbano.',
            caixa('atencao', 'Não confunda <b>polícia administrativa</b> (limita atividades e condiciona direitos, de forma preventiva) com <b>polícia judiciária</b> (investigação de crimes, exercida pelas polícias civil e federal).'),
        ],
        exemplos=['Interromper o transporte coletivo sem motivo viola a continuidade.', 'A fiscalização do uso irregular de calçadas por comércio é exercício de poder de polícia administrativa.'],
        erros=['Confundir polícia administrativa com polícia judiciária.'],
        resumo=['Serviço público: continuidade, generalidade, eficiência, modicidade, cortesia, atualidade.', 'Poder de polícia: limita direitos em prol do interesse público.'],
        exercicios=[
            Q('Administração Pública', 'O princípio do serviço público segundo o qual ele não deve ser interrompido sem justificativa é o da',
              'continuidade.', ['modicidade.', 'cortesia.', 'atualidade.', 'pessoalidade.'], 'Continuidade do serviço público.', ''),
            Q('Administração Pública', 'A fiscalização de posturas municipais e do ordenamento urbano é exemplo de',
              'poder de polícia administrativa.', ['polícia judiciária.', 'função legislativa.', 'função jurisdicional.', 'atividade privada.'], 'Limitação e condicionamento de atividades em favor do interesse público.', ''),
        ]),

    Topico('Servidores públicos e responsabilidade',
        'Servidores públicos estão sujeitos a <b>deveres, proibições e responsabilidades</b> nas esferas administrativa, civil e penal.',
        [
            tab(['Tema', 'Regra constitucional'], [
                ['Ingresso', 'Concurso público para cargo efetivo (art. 37, II); validade de até 2 anos, prorrogável uma vez por igual período (art. 37, III).'],
                ['Funções de confiança e cargos em comissão', 'Atribuições de direção, chefia e assessoramento; funções de confiança só para efetivos (art. 37, V).'],
                ['Acumulação', 'Vedada, salvo exceções e com compatibilidade de horários (art. 37, XVI).'],
                ['Responsabilidade do Estado', 'Objetiva: responde pelos danos que seus agentes causarem a terceiros, com direito de regresso contra o agente com dolo ou culpa (art. 37, § 6º).'],
                ['Regime jurídico', 'Cada ente institui regime jurídico e planos de carreira (art. 39). Em Parnaíba, o estatuto dos servidores é definido por lei municipal.'],
            ], [4.6, 12.4], 9.0),
            tab(['Esfera de responsabilidade', 'Exemplo'], [
                ['Administrativa', 'Processo disciplinar por descumprimento de dever funcional (advertência, suspensão, demissão, conforme o estatuto).'],
                ['Civil', 'Ressarcir prejuízo causado ao erário ou a terceiros (via regresso).'],
                ['Penal', 'Responder por crime praticado no exercício da função.'],
            ], [4.6, 12.4], 9.0),
            'As três esferas são, em regra, independentes: o mesmo fato pode gerar consequências nas três.',
        ],
        exemplos=['Um servidor que danifica um veículo oficial por negligência pode responder administrativamente e ser cobrado pelo prejuízo (civil).'],
        erros=['Achar que a absolvição em um processo administrativo impede sempre a ação penal (as esferas são, em regra, independentes).'],
        resumo=['Concurso, funções de confiança, acumulação, responsabilidade objetiva.', 'Responsabilidades administrativa, civil e penal, em regra independentes.'],
        exercicios=[
            Q('Administração Pública', 'A responsabilidade do Estado pelos danos causados por seus agentes a terceiros, segundo o art. 37, § 6º, é',
              'objetiva, com direito de regresso contra o agente em caso de dolo ou culpa.', ['subjetiva, exigindo prova de culpa do Estado.', 'inexistente.', 'exclusiva do agente.', 'limitada aos danos morais.'], 'Art. 37, § 6º.', ''),
            Q('Administração Pública', 'As responsabilidades administrativa, civil e penal do servidor são, em regra,',
              'independentes entre si.', ['excludentes: só uma pode ser aplicada.', 'aplicadas apenas pelo Poder Legislativo.', 'inexistentes para servidores efetivos.', 'sempre dependentes da esfera penal.'], 'O mesmo fato pode gerar consequências nas três esferas.', ''),
        ]),
]

ADM_REVISAO = [
    Q('Revisão — Administração Pública', 'O mnemônico LIMPE refere-se aos princípios',
      'expressos no caput do art. 37 da CF.', ['dos direitos sociais.', 'das relações internacionais.', 'do processo penal.', 'da Lei nº 13.060/2014.'], 'Legalidade, impessoalidade, moralidade, publicidade, eficiência.', ''),
    Q('Revisão — Administração Pública', 'Agir com ética, honestidade e boa-fé corresponde ao princípio da',
      'moralidade.', ['publicidade.', 'eficiência.', 'legalidade estrita.', 'continuidade.'], '', ''),
    Q('Revisão — Administração Pública', 'São princípios implícitos da administração pública:',
      'razoabilidade e proporcionalidade.', ['legalidade e publicidade.', 'impessoalidade e eficiência.', 'moralidade e legalidade.', 'publicidade e moralidade.'], 'Razoabilidade e proporcionalidade não estão no caput do art. 37.', ''),
    Q('Revisão — Administração Pública', 'Compete ao Município, segundo o art. 30, V, da CF, organizar e prestar os serviços públicos de interesse local, incluído o',
      'transporte coletivo, que tem caráter essencial.', ['serviço postal nacional.', 'controle de fronteiras.', 'emissão de moeda.', 'policiamento das rodovias federais.'], 'Art. 30, V.', ''),
    Q('Revisão — Administração Pública', 'Recusar um presente oferecido por alguém interessado em um serviço público é atitude coerente com o princípio da',
      'moralidade.', ['pessoalidade.', 'publicidade comercial.', 'modicidade.', 'atualidade.'], 'A moralidade exige ética e afastamento de vantagens indevidas.', ''),
]

ADM_RESUMO = [
    ['Conceito', 'Órgãos, entidades e agentes que exercem a função administrativa. Direta (entes e órgãos) e indireta (autarquias, fundações, empresas públicas, sociedades de economia mista).'],
    ['LIMPE', 'Legalidade, impessoalidade, moralidade, publicidade, eficiência (art. 37, caput).'],
    ['Princípios implícitos', 'Supremacia e indisponibilidade do interesse público, razoabilidade, proporcionalidade, autotutela, continuidade, motivação.'],
    ['Serviço público', 'Continuidade, generalidade, eficiência, modicidade, cortesia, atualidade; serviços locais pelo Município (art. 30, V).'],
    ['Poder de polícia', 'Limita e condiciona direitos em favor do interesse público; diferente de polícia judiciária.'],
    ['Servidores', 'Concurso, funções de confiança, acumulação, responsabilidade objetiva do Estado, esferas administrativa, civil e penal.'],
]
