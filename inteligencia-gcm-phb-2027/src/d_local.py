# -*- coding: utf-8 -*-
"""Conhecimentos locais de Parnaíba (PI).

Fontes: IBGE (Biblioteca — histórico e formação administrativa; Censo 2022); decreto federal de 28/08/1996 (APA Delta do Parnaíba);
decreto federal de 16/11/2000 (Resex Marinha do Delta do Parnaíba); Lei nº 13.651/2018 (UFDPar); IPHAN (cajuína, 2014);
estudos acadêmicos sobre o tombamento do conjunto histórico (aprovação pelo Conselho Consultivo do IPHAN em 2008);
INMET (normais climatológicas, via verbete da Wikipédia em português, usado apenas para cruzar dados geográficos).
"""
from render import Topico, tab, bl, h3, caixa, fluxo, num
from qbase import Q, QF

TOPICOS = [
    Topico('Localização e características gerais',
        'Parnaíba é um <b>município do litoral norte do Piauí</b>, o segundo mais populoso do estado, e a principal porta de entrada para o Delta do Parnaíba.',
        [
            tab(['Aspecto', 'Informação', 'Fonte'], [
                ['Estado / região', 'Piauí — Região Nordeste.', 'IBGE'],
                ['População', '162.159 habitantes (Censo 2022), a 2ª maior do Piauí, atrás de Teresina.', 'IBGE, Censo 2022'],
                ['Área territorial', 'Cerca de 437 km².', 'IBGE'],
                ['Gentílico', 'Parnaibano.', 'IBGE'],
                ['Municípios limítrofes', 'Luís Correia, Ilha Grande, Buriti dos Lopes, Bom Princípio do Piauí e, pelo rio, Araioses (MA).', 'Divisão territorial'],
                ['Hidrografia', 'Banhada pelo rio Igaraçu, braço do rio Parnaíba; próxima ao Delta do Parnaíba.', '—'],
                ['Região metropolitana', 'É a principal cidade da Região Metropolitana de Parnaíba.', 'Legislação estadual'],
            ], [3.6, 10.0, 3.4], 9.0),
            caixa('fato', 'O Piauí tem o <b>menor litoral</b> entre os estados brasileiros costeiros e apenas quatro municípios litorâneos: <b>Parnaíba, Luís Correia, Ilha Grande e Cajueiro da Praia</b>.'),
            h3('Clima'),
            'O clima é tropical, quente o ano todo. Segundo as normais climatológicas do INMET, as chuvas se concentram no primeiro semestre (especialmente de fevereiro a maio), enquanto o segundo semestre, sobretudo de agosto a novembro, é muito seco.',
        ],
        exemplos=['Em provas, uma pergunta comum é: “Qual é o segundo município mais populoso do Piauí?” — Parnaíba.'],
        erros=['Confundir Parnaíba (PI) com Santana de Parnaíba (SP).', 'Dizer que Parnaíba é a capital do Piauí (a capital é Teresina).'],
        resumo=['Litoral norte do Piauí; 2º município mais populoso (162.159 hab. — Censo 2022).', 'Gentílico: parnaibano.', 'Rio Igaraçu; porta de entrada do Delta.'],
        exercicios=[
            Q('Parnaíba — Geografia', 'Segundo o Censo 2022 do IBGE, Parnaíba é, em população, o',
              'segundo município mais populoso do Piauí.', ['município mais populoso do Piauí.', 'menor município do litoral piauiense.', 'terceiro município mais populoso do Nordeste.', 'município menos populoso do estado.'],
              'Parnaíba (162.159 hab.) fica atrás apenas de Teresina.', ''),
            Q('Parnaíba — Geografia', 'São municípios do litoral piauiense:',
              'Parnaíba, Luís Correia, Ilha Grande e Cajueiro da Praia.', ['Teresina, Picos, Floriano e Oeiras.', 'Parnaíba, Teresina, Piripiri e Campo Maior.', 'Luís Correia, Picos, Oeiras e Ilha Grande.', 'Cajueiro da Praia, Floriano, Parnaíba e Teresina.'],
              'O litoral do Piauí tem apenas esses quatro municípios.', ''),
        ]),

    Topico('Formação histórica',
        'A ocupação da região e a formação do município estão ligadas à <b>pecuária, às charqueadas e ao comércio pelo rio</b>, com destaque para o Porto das Barcas.',
        [
            'As informações a seguir seguem o histórico do município publicado pelo IBGE.',
            tab(['Ano', 'Acontecimento'], [
                ['1699', 'A região entre o rio Igaraçu e a Serra da Ibiapaba é desbravada por Leonardo de Sá e companheiros, que obtêm uma sesmaria às margens do rio.'],
                ['Depois de 1761', 'Inicia-se o desenvolvimento. Funcionava no local uma charqueada do português Domingos Dias da Silva, fundador do Porto das Barcas e pioneiro nos setores comercial e agrícola.'],
                ['1761–1762', 'Provisão régia de 19/06/1761 eleva a localidade a município; instalado em 18/08/1762 pelo governador João Pereira Caldas, com o nome de São João da Parnaíba e sede no lugarejo de Testa Branca.'],
                ['1770', 'A população, insatisfeita com a sede em Testa Branca, passa a residir em Porto das Barcas; no governo de Gonçalo Lourenço Botelho de Castro, a mudança é atendida.'],
                ['1801', 'Resolução régia cria o distrito com a denominação de Parnaíba.'],
                ['1844', 'Elevação à condição de cidade, pela resolução provincial nº 166.'],
                ['1931–1938', 'Parnaíba incorpora o extinto município de Amarração (1931); o distrito passa a chamar-se Luiz Correia (1935) e é desmembrado, tornando-se município (1938).'],
            ], [2.6, 14.4], 9.0),
            h3('Origem do nome'),
            'O IBGE registra duas hipóteses: homenagem ao então distrito paulista de Parnaíba, por parte dos primeiros exploradores, ou origem na palavra tupi que significaria “grande rio não navegável”.',
        ],
        exemplos=['O Porto das Barcas é o núcleo histórico da cidade: foi para lá que a população se mudou, deixando Testa Branca.'],
        erros=['Dizer que a cidade foi fundada em 1844 (1844 é a elevação à categoria de cidade).', 'Confundir Domingos Dias da Silva com Simplício Dias da Silva.'],
        resumo=['1699: Leonardo de Sá.', 'Domingos Dias da Silva: charqueada e Porto das Barcas.', '1762: instalação como São João da Parnaíba (Testa Branca).', '1844: elevação a cidade.'],
        exercicios=[
            Q('Parnaíba — História', 'Segundo o IBGE, o município instalado em 1762 recebeu o nome de',
              'São João da Parnaíba, com sede em Testa Branca.', ['Vila do Delta, com sede no Porto das Barcas.', 'Amarração, com sede em Luís Correia.', 'Nossa Senhora da Graça, com sede em Ilha Grande.', 'Igaraçu, com sede na Pedra do Sal.'], '', ''),
            QF('Parnaíba — História', 'Parnaíba foi elevada à condição de cidade, por resolução provincial, em',
               ['1699', '1762', '1801', '1844', '1938'], 'D', 'IBGE: resolução provincial nº 166, de 1844.', '1762 é a instalação do município.'),
        ]),

    Topico('Parnaíba e a Independência do Brasil',
        'Em <b>19 de outubro de 1822</b>, a vila de Parnaíba proclamou sua adesão à Independência do Brasil, em movimento que teve entre seus líderes <b>Simplício Dias da Silva</b>.',
        [
            'A adesão desencadeou a reação das tropas portuguesas comandadas pelo major João José da Cunha Fidié, que marchou em direção a Parnaíba. Os líderes do movimento se deslocaram para o Ceará. Os confrontos que se seguiram no Piauí incluíram a <b>Batalha do Jenipapo</b>, travada em <b>13 de março de 1823</b>, em Campo Maior.',
            caixa('dica', 'A data de 19 de outubro é celebrada no Piauí como marco da adesão à Independência. Não confunda: Parnaíba <b>aderiu</b> à Independência do Brasil (em relação a Portugal); ela não se separou do Brasil.'),
        ],
        exemplos=['Em questões de história regional, a sequência costuma ser: adesão de Parnaíba (out/1822) → reação de Fidié → Batalha do Jenipapo (mar/1823).'],
        erros=['Atribuir a Batalha do Jenipapo a Parnaíba (ocorreu em Campo Maior).'],
        resumo=['19/10/1822: adesão de Parnaíba à Independência.', 'Simplício Dias da Silva entre os líderes.', 'Batalha do Jenipapo: 13/03/1823, Campo Maior.'],
        exercicios=[
            Q('Parnaíba — História', 'Em outubro de 1822, a vila de Parnaíba',
              'proclamou sua adesão à Independência do Brasil.', ['declarou-se independente do Brasil.', 'tornou-se capital do Império.', 'recebeu a família real portuguesa.', 'foi anexada ao Maranhão.'], '', ''),
            Q('Parnaíba — História', 'A Batalha do Jenipapo, ligada às lutas pela Independência no Piauí, ocorreu em',
              'Campo Maior, em 1823.', ['Parnaíba, em 1844.', 'Teresina, em 1822.', 'Luís Correia, em 1938.', 'Oeiras, em 1762.'], '', ''),
        ]),

    Topico('Geografia e meio ambiente: o Delta do Parnaíba',
        'O <b>Delta do Parnaíba</b>, formado pelo rio Parnaíba em sua foz no Oceano Atlântico, na divisa entre Piauí e Maranhão, é considerado o <b>único delta em mar aberto das Américas</b>.',
        [
            'Um delta se forma quando um rio se divide em vários braços ao chegar ao mar, criando ilhas, canais, mangues e dunas. Por ser a principal porta de entrada para o Delta, Parnaíba é conhecida como <b>“Capital do Delta”</b>.',
            tab(['Unidade de conservação', 'Criação', 'Categoria'], [
                ['Área de Proteção Ambiental (APA) Delta do Parnaíba', 'Decreto federal de 28 de agosto de 1996; abrange áreas do Piauí, do Maranhão e do Ceará.', 'Uso sustentável'],
                ['Reserva Extrativista Marinha do Delta do Parnaíba', 'Decreto federal de 16 de novembro de 2000.', 'Uso sustentável'],
            ], [5.6, 8.0, 3.4], 9.0),
            'Essas unidades são hoje geridas pelo órgão ambiental federal (ICMBio). Outros atrativos naturais da região são a <b>Lagoa do Portinho</b> e a praia da <b>Pedra do Sal</b>, famosa pelo pôr do sol.',
            caixa('fato', 'A Lei nº 13.022/2014 prevê como competência das guardas proteger o patrimônio ecológico e ambiental do Município, inclusive com medidas educativas e preventivas (art. 5º, VII) — tema especialmente relevante em Parnaíba.'),
        ],
        exemplos=['Uma questão pode perguntar por que Parnaíba é chamada de “Capital do Delta”.'],
        erros=['Dizer que o Delta do Parnaíba é o maior delta do mundo (a característica destacada é ser o único em mar aberto das Américas).'],
        resumo=['Único delta em mar aberto das Américas.', 'APA Delta do Parnaíba (1996) e Resex Marinha (2000).', 'Lagoa do Portinho e Pedra do Sal.'],
        exercicios=[
            Q('Parnaíba — Meio ambiente', 'Parnaíba é conhecida como “Capital do Delta” porque',
              'é a principal porta de entrada para o Delta do Parnaíba, único delta em mar aberto das Américas.', ['é a capital do Piauí.', 'fica no interior do Maranhão.', 'é banhada pelo rio São Francisco.', 'abriga o maior delta da Europa.'], '', ''),
            Q('Parnaíba — Meio ambiente', 'A Área de Proteção Ambiental Delta do Parnaíba foi criada por decreto federal em',
              '1996.', ['1762.', '1844.', '1988.', '2018.'], 'Decreto de 28 de agosto de 1996.', 'A Resex Marinha do Delta é de 2000.'),
        ]),

    Topico('Cultura e patrimônio',
        'Parnaíba reúne <b>patrimônio histórico, religioso e cultural</b> ligado à sua formação como entreposto comercial e cidade portuária.',
        [
            tab(['Patrimônio', 'Descrição'], [
                ['Porto das Barcas', 'Núcleo histórico às margens do rio Igaraçu, com casarões e antigos armazéns ligados ao período comercial; hoje é espaço cultural e turístico.'],
                ['Conjunto histórico e paisagístico', 'O centro histórico de Parnaíba é protegido pelo IPHAN; estudos acadêmicos registram a aprovação do tombamento pelo Conselho Consultivo do órgão em 2008.'],
                ['Catedral de Nossa Senhora Mãe da Divina Graça', 'Sede da Diocese de Parnaíba, um dos principais templos católicos da cidade.'],
                ['Cajuína', 'A produção tradicional e as práticas socioculturais associadas à cajuína no Piauí foram registradas como Patrimônio Cultural do Brasil pelo IPHAN em 2014.'],
            ], [5.0, 12.0], 9.0),
            caixa('atencao', 'Algumas datas de tombamento aparecem de forma diferente em fontes distintas (por exemplo, 2008 e 2011), possivelmente pela diferença entre aprovação e inscrição formal. Em provas, siga o que o enunciado indicar e prefira fontes oficiais (IPHAN).'),
            'A Constituição atribui ao Município a promoção da proteção do patrimônio histórico-cultural local (art. 30, IX), e a Lei nº 13.022/2014 atribui às guardas a proteção desse patrimônio (art. 5º, VII).',
        ],
        exemplos=['A proteção do casario do Porto das Barcas envolve o Município, o IPHAN e, na vigilância preventiva, a guarda municipal.'],
        erros=['Dizer que a cajuína é patrimônio exclusivo de Parnaíba: o registro refere-se às práticas tradicionais no Piauí.'],
        resumo=['Porto das Barcas: núcleo histórico.', 'Conjunto histórico protegido pelo IPHAN.', 'Cajuína: Patrimônio Cultural do Brasil (2014).'],
        exercicios=[
            Q('Parnaíba — Patrimônio', 'O Porto das Barcas, em Parnaíba, destaca-se por ser',
              'um núcleo histórico às margens do rio Igaraçu, ligado à origem comercial da cidade.', ['um porto moderno de contêineres.', 'uma reserva indígena fechada.', 'um aeroporto desativado.', 'um bairro industrial construído em 2010.'], '', ''),
            Q('Parnaíba — Patrimônio', 'As práticas tradicionais associadas à produção da cajuína no Piauí foram registradas como Patrimônio Cultural do Brasil pelo IPHAN em',
              '2014.', ['1822.', '1948.', '1988.', '2022.'], '', ''),
        ]),

    Topico('Economia',
        'A economia de Parnaíba combina <b>comércio e serviços</b>, turismo, agropecuária e iniciativas industriais, com raízes históricas no comércio portuário.',
        [
            tab(['Período', 'Atividades em destaque'], [
                ['Colonial e imperial', 'Pecuária, charqueadas (carne-seca) e comércio de couro; escoamento pelo porto (IBGE).'],
                ['Séculos XIX e XX', 'Comércio de produtos regionais, entre eles produtos extrativistas como a cera de carnaúba.'],
                ['Atualidade', 'Comércio e serviços (polo regional), turismo, agricultura irrigada nos tabuleiros litorâneos, Zona de Processamento de Exportação (ZPE) e serviços aeroportuários.'],
            ], [4.0, 13.0], 9.2),
            'O <b>Aeroporto Internacional de Parnaíba</b> (Prefeito Dr. João Silva Filho) atende a região turística conhecida como <b>Rota das Emoções</b>.',
        ],
        exemplos=['Uma ZPE é uma área com regime especial para empresas voltadas à exportação.'],
        erros=['Atribuir a Parnaíba atividades de mineração de ouro ou petróleo em alto-mar.'],
        resumo=['Raízes: charqueadas, couro e comércio portuário.', 'Hoje: comércio, serviços, turismo, agricultura irrigada, ZPE.'],
        exercicios=[
            Q('Parnaíba — Economia', 'Segundo o histórico do IBGE, a economia inicial da região esteve ligada a',
              'charqueadas e comércio, com escoamento pelo porto.', ['mineração de ouro.', 'indústria automobilística.', 'extração de petróleo em alto-mar.', 'cultivo de café em larga escala.'], '', ''),
            Q('Parnaíba — Economia', 'Uma iniciativa voltada a empresas exportadoras em Parnaíba é a',
              'Zona de Processamento de Exportação (ZPE).', ['Zona Franca de Manaus.', 'Usina de Itaipu.', 'Refinaria de Paulínia.', 'Polo de Camaçari.'], '', ''),
        ]),

    Topico('Aspectos sociais e educação',
        'Parnaíba é <b>polo regional de serviços, saúde e educação</b> no norte do Piauí.',
        [
            tab(['Indicador / instituição', 'Informação'], [
                ['População (Censo 2022)', '162.159 habitantes, com predominância urbana: cerca de 154,7 mil na área urbana e 7,5 mil na rural.'],
                ['Universidade Federal do Delta do Parnaíba (UFDPar)', 'Criada pela Lei nº 13.651, de 11 de abril de 2018, por desmembramento da Universidade Federal do Piauí (UFPI).'],
                ['Outras instituições públicas de ensino superior e técnico', 'Campus da Universidade Estadual do Piauí (UESPI) e do Instituto Federal do Piauí (IFPI).'],
                ['Religião', 'Sede da Diocese de Parnaíba.'],
            ], [5.6, 11.4], 9.0),
            caixa('dica', 'Indicadores sociais (população, IDH, renda) mudam com o tempo. Em provas, observe o ano citado e prefira dados do IBGE.'),
        ],
        exemplos=['A UFDPar surgiu do antigo campus da UFPI em Parnaíba.'],
        erros=['Dizer que a UFDPar foi criada pela Lei nº 13.022/2014 (essa é o Estatuto das Guardas).'],
        resumo=['Polo regional de serviços e educação.', 'UFDPar: Lei nº 13.651/2018.'],
        exercicios=[
            Q('Parnaíba — Aspectos sociais', 'A Universidade Federal do Delta do Parnaíba (UFDPar) foi criada',
              'pela Lei nº 13.651/2018, por desmembramento da UFPI.', ['pela Lei nº 13.022/2014.', 'por decreto municipal em 1844.', 'como instituição privada em 1990.', 'pela Constituição de 1988.'], '', ''),
            Q('Parnaíba — Aspectos sociais', 'Segundo o Censo 2022, a população de Parnaíba vive majoritariamente',
              'na área urbana.', ['na área rural.', 'em ilhas do Delta.', 'em outro estado.', 'em proporções iguais entre área urbana e rural.'], 'Cerca de 154,7 mil na área urbana e 7,5 mil na rural.', ''),
        ]),

    Topico('Turismo',
        'O turismo é uma das atividades de maior destaque, impulsionado pelo <b>Delta do Parnaíba</b>, pelo patrimônio histórico e pela integração à <b>Rota das Emoções</b>.',
        [
            tab(['Atrativo', 'Destaque'], [
                ['Delta do Parnaíba', 'Passeios de barco pelos canais, ilhas, mangues e dunas.'],
                ['Porto das Barcas', 'Centro histórico, cultura, gastronomia e artesanato.'],
                ['Pedra do Sal', 'Praia conhecida pelo pôr do sol.'],
                ['Lagoa do Portinho', 'Lagoa cercada por dunas.'],
                ['Rota das Emoções', 'Roteiro que conecta Jericoacoara (CE), o Delta do Parnaíba (PI/MA) e os Lençóis Maranhenses (MA).'],
            ], [4.4, 12.6], 9.2),
            caixa('fato', 'Turismo e preservação caminham juntos: as unidades de conservação do Delta são de uso sustentável, ou seja, admitem visitação e atividades econômicas compatíveis com a proteção ambiental.'),
        ],
        exemplos=['Um turista que chega pelo Aeroporto de Parnaíba pode visitar o Delta, a Pedra do Sal e seguir pela Rota das Emoções.'],
        erros=['Incluir na Rota das Emoções destinos de outras regiões, como Fernando de Noronha.'],
        resumo=['Delta, Porto das Barcas, Pedra do Sal, Lagoa do Portinho.', 'Rota das Emoções: Jericoacoara, Delta, Lençóis Maranhenses.'],
        exercicios=[
            Q('Parnaíba — Turismo', 'A Rota das Emoções conecta',
              'Jericoacoara (CE), o Delta do Parnaíba (PI/MA) e os Lençóis Maranhenses (MA).', ['Salvador, Recife e Natal.', 'Foz do Iguaçu e Pantanal.', 'Teresina, Brasília e Goiânia.', 'Fernando de Noronha e Abrolhos.'], '', ''),
            Q('Parnaíba — Turismo', 'A praia de Parnaíba conhecida pelo pôr do sol é a',
              'Pedra do Sal.', ['Copacabana.', 'Praia do Futuro.', 'Ponta Negra.', 'Porto de Galinhas.'], '', ''),
        ]),

    Topico('Características regionais e organização municipal',
        'Como todo município brasileiro, Parnaíba é um <b>ente federativo autônomo</b> (CF, art. 18), com Poder Executivo (prefeito) e Poder Legislativo (Câmara Municipal), regido por sua Lei Orgânica.',
        [
            tab(['Elemento', 'Explicação'], [
                ['Lei Orgânica do Município', 'Funciona como a “constituição” do município; organiza os Poderes locais e as competências municipais.'],
                ['Prefeito', 'Chefe do Poder Executivo municipal; a guarda municipal é subordinada a ele (Lei nº 13.022/2014, art. 6º, parágrafo único).'],
                ['Câmara Municipal', 'Elabora as leis municipais e fiscaliza o Executivo; decide sobre a perda de mandato de corregedores e ouvidores da guarda (Lei nº 13.022/2014, art. 13, § 2º).'],
                ['Leis municipais relevantes para o concurso', 'Lei de criação e organização da guarda, estatuto dos servidores municipais e plano de cargos. Consulte a versão vigente no site da prefeitura ou da Câmara.'],
            ], [5.0, 12.0], 9.0),
            caixa('atencao', 'O edital poderá cobrar legislação municipal específica de Parnaíba (Lei Orgânica, estatuto dos servidores, lei da guarda). Este guia não reproduz essas leis porque elas devem ser lidas na versão oficial e atualizada, publicada pelo Município.'),
        ],
        exemplos=['Uma lei municipal pode criar requisitos adicionais para o cargo de guarda (Lei nº 13.022/2014, art. 10, parágrafo único).'],
        erros=['Achar que a guarda é subordinada à Câmara Municipal.'],
        resumo=['Município autônomo: prefeito + Câmara + Lei Orgânica.', 'Leia a legislação municipal na fonte oficial.'],
        exercicios=[
            Q('Parnaíba — Organização municipal', 'A norma que funciona como a “constituição” do Município é a',
              'Lei Orgânica do Município.', ['Constituição Estadual.', 'Lei nº 13.022/2014.', 'Declaração Universal dos Direitos Humanos.', 'Lei de Acesso à Informação.'], '', ''),
            Q('Parnaíba — Organização municipal', 'A guarda municipal de qualquer Município é subordinada',
              'ao prefeito, chefe do Poder Executivo municipal.', ['à Câmara Municipal.', 'ao governador.', 'ao IPHAN.', 'ao ICMBio.'], 'Lei nº 13.022/2014, art. 6º, parágrafo único.', ''),
        ]),
]

REVISAO = [
    Q('Revisão — Parnaíba', 'Segundo o IBGE, o fundador do Porto das Barcas foi',
      'Domingos Dias da Silva.', ['Leonardo de Sá.', 'Simplício Dias da Silva.', 'João Pereira Caldas.', 'Gonçalo Lourenço Botelho de Castro.'], '', 'Leonardo de Sá desbravou a região em 1699; João Pereira Caldas instalou o município.'),
    Q('Revisão — Parnaíba', 'O gentílico de quem nasce em Parnaíba é',
      'parnaibano.', ['parnaibense.', 'piauiense do litoral.', 'parnaíbo.', 'deltense.'], 'IBGE.', ''),
    Q('Revisão — Parnaíba', 'O rio que banha a cidade de Parnaíba, braço do rio Parnaíba, é o',
      'Igaraçu.', ['Poti.', 'São Francisco.', 'Gurgueia.', 'Tocantins.'], '', 'O Poti banha Teresina.'),
    Q('Revisão — Parnaíba', 'O distrito de Amarração, que pertenceu a Parnaíba, passou a se chamar Luiz Correia e foi desmembrado, tornando-se município, em',
      '1938.', ['1762.', '1801.', '1844.', '1996.'], 'IBGE: decreto estadual nº 147, de 1938.', ''),
    Q('Revisão — Parnaíba', 'A Reserva Extrativista Marinha do Delta do Parnaíba foi criada em',
      '2000.', ['1762.', '1822.', '1988.', '2018.'], 'Decreto federal de 16/11/2000.', ''),
    Q('Revisão — Parnaíba', 'Em relação ao Delta do Parnaíba, é correto afirmar que',
      'é considerado o único delta em mar aberto das Américas.', ['é o maior delta do mundo.', 'fica inteiramente no Ceará.', 'é formado pelo rio São Francisco.', 'não possui unidades de conservação.'], '', ''),
]

RESUMO_CAP = [
    ['Localização', 'Litoral norte do Piauí; 2º município mais populoso (162.159 hab. — Censo 2022); gentílico parnaibano; rio Igaraçu.'],
    ['Formação histórica', '1699 Leonardo de Sá; Domingos Dias da Silva (charqueada, Porto das Barcas); 1762 São João da Parnaíba (Testa Branca); 1770 mudança para Porto das Barcas; 1844 cidade.'],
    ['Independência', '19/10/1822 adesão; Simplício Dias da Silva; Batalha do Jenipapo (13/03/1823, Campo Maior).'],
    ['Delta', 'Único delta em mar aberto das Américas; APA (1996) e Resex Marinha (2000).'],
    ['Patrimônio e cultura', 'Porto das Barcas; conjunto histórico protegido pelo IPHAN; Catedral; cajuína (Patrimônio Cultural do Brasil, 2014).'],
    ['Economia e turismo', 'Comércio e serviços, turismo (Rota das Emoções), agricultura irrigada, ZPE, aeroporto internacional.'],
    ['Sociedade e organização', 'Polo regional; UFDPar (Lei nº 13.651/2018); município autônomo com Lei Orgânica, prefeito e Câmara.'],
]
