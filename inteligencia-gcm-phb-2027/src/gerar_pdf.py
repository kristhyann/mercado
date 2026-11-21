# -*- coding: utf-8 -*-
"""Gera Inteligencia_GCM_PHB_2027.pdf.  Uso: python3 gerar_pdf.py"""
import os
from motor import *
import render
from render import render_disciplina
import d_port1, d_port2, d_cf, d_lei, d_dh_adm, d_info, d_mat, d_local

AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(os.path.dirname(AQUI), 'Inteligencia_GCM_PHB_2027.pdf')

CF88 = 'https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html'
L13022 = 'https://www2.camara.leg.br/legin/fed/lei/2014/lei-13022-8-agosto-2014-779152-normaatualizada-pl.html'
PL13022 = 'https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l13022.htm'
PL13060 = 'https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l13060.htm'
IBGE_HIST = 'https://biblioteca.ibge.gov.br/visualizacao/dtb/piaui/parnaiba.pdf'
APA = 'https://www.planalto.gov.br/ccivil_03/dnn/anterior_a_2000/1996/dnn4368.htm'
STF656 = 'https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=656'

PORT = d_port1.TOPICOS + d_port2.TOPICOS

DISC = [
    # (num, titulo, subtitulo, sigla, intro, topicos, revisao, resumo, aviso)
    (1, 'Língua Portuguesa', 'Interpretação, gramática e construção do texto', 'LP',
     ['Português é, em geral, uma das disciplinas de maior peso em concursos de nível médio e sustenta todas as outras: interpretar bem um enunciado de legislação ou de matemática também é Português. Este capítulo segue a ordem natural de aprendizagem: texto → palavra → frase → texto novamente.'],
     PORT, d_port2.REVISAO, d_port2.RESUMO_CAP, None),
    (2, 'Constituição Federal', 'Organização, direitos fundamentais, administração e segurança pública', 'CF',
     ['A Constituição Federal de 1988 é a base de toda a legislação estudada neste guia. As explicações foram elaboradas a partir do texto atualizado disponível no portal de Legislação Informatizada da Câmara dos Deputados (consultado em novembro de 2026). Sempre que possível, leia também os artigos citados no texto oficial.'],
     d_cf.TOPICOS, d_cf.REVISAO, d_cf.RESUMO_CAP, None),
    (3, 'Lei nº 13.022/2014', 'Estatuto Geral das Guardas Municipais', 'LG',
     ['Este é o principal conteúdo específico do cargo. A lei tem 23 artigos e deve ser lida na íntegra, várias vezes. As explicações seguem o texto atualizado da norma e indicam sempre o artigo correspondente, para que você possa conferir.'],
     d_lei.TOPICOS, d_lei.REVISAO, d_lei.RESUMO_CAP, None),
    (4, 'Direitos Humanos e Cidadania', 'Conceitos, dignidade, igualdade, cidadania e atuação pública', 'DH',
     ['Direitos humanos e cidadania são temas frequentes em concursos da área de segurança e estão diretamente ligados aos princípios de atuação das guardas municipais (Lei nº 13.022/2014, art. 3º).'],
     d_dh_adm.DH_TOPICOS, d_dh_adm.DH_REVISAO, d_dh_adm.DH_RESUMO, None),
    (5, 'Administração Pública', 'Conceito, princípios e noções de serviço público', 'AP',
     ['O guarda municipal é servidor público: conhecer os princípios da administração pública é conhecer as regras do próprio trabalho. A base está no art. 37 da Constituição.'],
     d_dh_adm.ADM_TOPICOS, d_dh_adm.ADM_REVISAO, d_dh_adm.ADM_RESUMO, None),
    (6, 'Informática', 'Do básico ao uso seguro de computadores, internet e ferramentas de escritório', 'IN',
     ['Este capítulo parte do zero. Se possível, pratique em um computador enquanto estuda: abra o explorador de arquivos, crie pastas, teste os atalhos e monte uma pequena planilha.'],
     d_info.TOPICOS, d_info.REVISAO, d_info.RESUMO_CAP, None),
    (7, 'Matemática e Raciocínio Lógico', 'Passo a passo, sem fórmulas soltas', 'MT',
     ['Cada técnica é explicada com o raciocínio por trás dela e com exemplos resolvidos. Tenha papel e lápis à mão e refaça os exemplos antes de olhar a solução.'],
     d_mat.TOPICOS, d_mat.REVISAO, d_mat.RESUMO_CAP, None),
    (8, 'Conhecimentos Locais de Parnaíba', 'História, geografia, cultura, patrimônio, economia e turismo', 'PH',
     ['As informações deste capítulo foram conferidas em fontes públicas e institucionais, com destaque para o histórico do município publicado pelo IBGE, o Censo Demográfico 2022, decretos federais e registros do IPHAN. Datas e dados sem confirmação em fonte confiável foram deixados de fora.'],
     d_local.TOPICOS, d_local.REVISAO, d_local.RESUMO_CAP, None),
]


def ficha():
    s = [Spacer(1, 1.0 * cm)]
    s.append(P('<font size="20" color="#0E2238"><b>Inteligência GCM PHB</b></font>', 'bodyL'))
    s.append(sp(6))
    s.append(P('Guia de disciplinas, legislação e conhecimentos locais para a preparação pré-edital — Guarda Civil Municipal de Parnaíba (PI). Edição 2027.', 'lead'))
    s.append(sp(6))
    s += table(None, [
        ['Conteúdo', 'Oito disciplinas explicadas desde o básico, com definições, explicações, exemplos, erros comuns, resumos, exercícios originais e gabaritos comentados.'],
        ['Público', 'Candidatos à Guarda Civil Municipal de Parnaíba (PI), inclusive quem está começando do zero.'],
        ['Fase', 'Pré-edital. As disciplinas e os assuntos são referências de preparação e não correspondem, necessariamente, ao conteúdo programático oficial.'],
        ['Data de referência', 'Novembro de 2026. Textos legais conferidos na versão atualizada disponível nessa data.'],
        ['Formato', 'PDF A4 com sumário clicável, marcadores, quadros, tabelas e páginas preenchíveis (checklist e plano de revisão).'],
    ], [3.8, 13.2], bold_first=True)
    s += box('atencao', [
        'Material <b>independente e não oficial</b>, sem vínculo com a Prefeitura Municipal de Parnaíba, a Guarda Civil Municipal ou qualquer banca organizadora.',
        'A <b>publicação do edital será a referência definitiva</b> sobre disciplinas, conteúdos e etapas. Nenhum material garante aprovação.',
        'Os exercícios foram <b>elaborados especialmente para este guia</b> e não são questões oficiais de nenhuma banca.',
    ], 'AVISO IMPORTANTE')
    s += box('fato', 'Fontes principais: Constituição Federal e Lei nº 13.022/2014 (textos atualizados — Câmara dos Deputados); Lei nº 13.060/2014; ECA; Estatuto da Pessoa Idosa; Lei Maria da Penha; Declaração Universal dos Direitos Humanos; decisões do STF; IBGE; IPHAN; decretos federais sobre o Delta do Parnaíba. A lista completa está no capítulo de recursos e referências.', 'FONTES')
    return s


def sumario():
    s = [PageBreak()]
    s.append(P('<font size="22" color="#0E2238"><b>Sumário</b></font>', 'bodyL'))
    s.append(sp(4))
    s.append(P('Toque em um capítulo para ir direto a ele. Os subtópicos aparecem nos marcadores do leitor de PDF.', 'small'))
    s.append(sp(8))
    s.append(make_toc())
    return s


def apresentacao():
    s = chapter('', 'Apresentação', 'Como estudar com este guia')
    s.append(lead('Este guia reúne, em um só lugar, as disciplinas que costumam fazer parte de concursos de guardas municipais, explicadas desde o início, com linguagem simples, exemplos, exercícios e gabaritos comentados.'))
    s.append(H2('Como utilizar'))
    s += table(['Etapa', 'O que fazer'], [
        ['1. Escolha a disciplina', 'Siga a ordem de prioridade: Português, Constituição, Lei nº 13.022/2014 e Direitos Humanos; depois Administração Pública, Informática, Matemática e Parnaíba.'],
        ['2. Estude um tópico por vez', 'Leia a definição, a explicação e os exemplos. Observe os erros comuns.'],
        ['3. Faça os exercícios do tópico', 'Sem consultar. Depois confira no gabarito comentado, no fim do capítulo.'],
        ['4. Revise com o resumo', 'Use o quadro “Resumo” de cada tópico e o resumo do capítulo.'],
        ['5. Faça a revisão do capítulo', 'Os exercícios de revisão misturam os tópicos.'],
        ['6. Marque no checklist e agende revisões', 'Use o checklist preenchível e o plano de revisão (24 h, 7 dias, 30 dias).'],
    ], [4.6, 12.4], bold_first=True)
    s.append(H2('Estrutura de cada tópico'))
    s.append(FlowSteps([('Definição', 'o conceito'), ('Explicação', 'com tabelas'), ('Exemplos', 'aplicação'), ('Erros comuns', 'o que evitar'),
                        ('Resumo', 'revisão rápida'), ('Exercícios', 'treino'), ('Gabarito', 'no fim do capítulo'), ('Revisão', 'checklist e plano')], per_row=4, box_h=1.45 * cm))
    s.append(sp(10))
    s.append(H2('Como estudar'))
    s += bullets([
        '<b>Leitura ativa:</b> antes de ler, transforme o título em pergunta; depois de ler, explique o conteúdo com suas palavras.',
        '<b>Lei seca:</b> leia o texto oficial dos artigos citados (Constituição e Lei nº 13.022/2014). As explicações daqui ajudam a entendê-lo, mas não o substituem.',
        '<b>Exercícios logo após a teoria:</b> errar no treino é parte do aprendizado.',
        '<b>Sessões curtas e frequentes:</b> 1 a 2 tópicos por sessão rendem mais que muitas horas sem pausa.',
    ])
    s.append(H2('Como revisar'))
    s += table(['Revisão', 'Quando', 'Como'], [
        ['24 horas', 'No dia seguinte ao estudo.', 'Leia o resumo do tópico e tente lembrar dos pontos principais sem olhar; refaça os exercícios errados.'],
        ['7 dias', 'Uma semana depois.', 'Releia os quadros de erros comuns e faça novamente os exercícios do tópico.'],
        ['30 dias', 'Um mês depois.', 'Leia o resumo do capítulo e resolva os exercícios de revisão.'],
    ], [2.6, 4.0, 10.4], bold_first=True)
    s.append(H2('Como utilizar com os outros PDFs do projeto'))
    s += table(['Material', 'Papel', 'Como combinar'], [
        ['Operação GCM PHB', 'Organização dos estudos, métodos, planos de 30/60/90 dias, planner.', 'Use os planos para distribuir os tópicos deste guia ao longo das semanas.'],
        ['Inteligência GCM PHB (este guia)', 'Conteúdo teórico das disciplinas, com exercícios de fixação.', 'Base de estudo: aprenda aqui antes de treinar com questões.'],
        ['Missão Aprova GCM PHB', 'Banco de questões, simulados, caderno de erros e controle de desempenho.', 'Depois de estudar um capítulo aqui, resolva as questões da mesma disciplina lá.'],
        ['Operação TAF GCM PHB', 'Preparação física geral.', 'Mantenha os treinos físicos em paralelo aos estudos.'],
    ], [4.4, 6.0, 6.6], bold_first=True)
    s += box('atencao', 'Quando o edital for publicado, compare o conteúdo programático oficial com este guia, estude os assuntos que estiverem no edital e dê atenção especial à legislação municipal de Parnaíba que for exigida.')
    return s


def cap_resumos(resumos):
    s = chapter(9, 'Resumos gerais', 'Os pontos essenciais de cada disciplina em um só lugar')
    s.append(P('Use estes quadros nas revisões de 30 dias e na reta final. Eles reúnem os resumos de cada capítulo.'))
    for titulo, rows in resumos:
        s.append(CondPageBreak(6 * cm))
        s.append(H2(titulo))
        s += table(['Tema', 'Pontos-chave'], rows, [4.6, 12.4], bold_first=True, fs=9.2)
    return s


def cap_checklist(listas):
    s = chapter(10, 'Checklist de revisão', 'Toque nas caixas para marcar no PDF ou imprima')
    s.append(P('Marque cada tópico depois de: (1) estudar a teoria; (2) fazer os exercícios; (3) conferir o gabarito. Ao final, todas as caixas marcadas indicam que você percorreu todo o guia.'))
    for titulo, itens in listas:
        s.append(CondPageBreak(5 * cm))
        s.append(H2(titulo))
        s.append(CheckList(itens, prefix='chk'))
        s.append(sp(6))
    return s


def cap_plano(listas):
    s = chapter(11, 'Plano de revisão', 'Sistema de revisões em 24 horas, 7 dias e 30 dias')
    s.append(P('Anote a data em que estudou cada tópico e agende as três revisões. Os campos podem ser preenchidos no leitor de PDF (salve uma cópia) ou à mão, após a impressão.'))
    s.append(Timeline([('D0', 'Estudo', 'Teoria + exercícios'), ('24h', 'Revisão 1', 'Resumo + exercícios errados'),
                       ('7d', 'Revisão 2', 'Erros comuns + exercícios do tópico'), ('30d', 'Revisão 3', 'Resumo do capítulo + revisão')], height=3.3 * cm))
    s += table(['Situação', 'Ajuste'], [
        ['Esqueceu muito na revisão', 'Reestude e faça nova revisão em 3 dias.'],
        ['Lembrou tudo com facilidade', 'Alongue o próximo intervalo (por exemplo, de 30 para 45 dias).'],
        ['Revisões acumuladas', 'Priorize: 24 h → 7 dias → 30 dias; pause conteúdo novo por alguns dias.'],
    ], [6.0, 11.0], bold_first=True)
    for titulo, itens in listas:
        s.append(PageBreak())
        s.append(H2('Plano de revisão — %s' % titulo))
        s.append(FormGrid(['Tópico', 'Estudo (data)', '24 h', '7 dias', '30 dias', 'OK'], [6.8, 2.2, 2.0, 2.0, 2.0, 2.0], len(itens),
                          row_h=0.78 * cm, prefix='plano', first_col=itens))
    return s


VIDEOS = [
    ('Língua Portuguesa', 'Tipos textuais', 'Tipos Textuais [ Prof Noslen]', 'Professor Noslen', 'ibwf_X3498c'),
    ('Língua Portuguesa', 'Classes de palavras', 'CLASSES DE PALAVRAS + EXERCÍCIOS RESOLVIDOS', 'Professor Noslen', '2tMS1O3xn24'),
    ('Língua Portuguesa', 'Uso da vírgula', 'Uso da Vírgula! Com Prof. Noslen!', 'Professor Noslen', '-uUtlvKifiY'),
    ('Língua Portuguesa', 'Concordância verbal', 'Concordância Verbal - Aula 01 [Prof Noslen]', 'Professor Noslen', '4ZJnTqTk4_Y'),
    ('Língua Portuguesa', 'Regência verbal', 'Regência Verbal - Aula 02 [Prof Noslen]', 'Professor Noslen', 'r4Pew3CliXI'),
    ('Língua Portuguesa', 'Crase', 'Crase - Aula 01 ♫ Concerto da Crase ♫ [Prof Noslen]', 'Professor Noslen', 'yUpRa62vcSI'),
    ('Constituição', 'Art. 5º — direitos individuais', 'Constituição Federal - Artigo 5º - Direitos e Deveres Individuais e Coletivos - Aula 01', 'Gustavo Fregapani', 'XS3QU0mHAv0'),
    ('Constituição', 'Direitos sociais (art. 6º)', 'CF88 - Art. 6º (Direitos Sociais)', 'Prof. Emerson Bruno', 'MoGVEN2o9EI'),
    ('Lei nº 13.022/2014', 'Estatuto Geral das Guardas Municipais', 'Estatuto Geral das Guardas Municipais Atualizado 2026 | Lei 13.022/2014', 'Monster Concursos', 'uB0oN1Qqv7M'),
    ('Direitos Humanos e Cidadania', 'Cidadania', 'O que é cidadania?', 'Escola da Câmara', 'xF0JJ-fosys'),
    ('Administração Pública', 'Princípios (LIMPE)', 'PRINCÍPIOS DA ADMINISTRAÇÃO PÚBLICA - Resumo para Concursos (Art. 37 da Constituição)', 'Me Julga - Cíntia Brunelli', 'Y_m2s4TXPyM'),
    ('Informática', 'Segurança e malwares', 'Informática: Princípios da Segurança da Informação e Malwares', 'Focus Concursos', 'VgXdkqyZdD8'),
    ('Matemática', 'Porcentagem', 'APRENDA PORCENTAGEM EM 8 MINUTOS | Fácil e Rápido', 'Dicasdemat Sandro Curió', 'azedx0uou64'),
    ('Matemática', 'Regra de três', 'Aprenda Agora I Regra de Três I Simples I Composta', 'Dicasdemat Sandro Curió', 'aAef69w8aNk'),
    ('Raciocínio lógico', 'Tabela-verdade', 'Aprenda de uma vez por todas a montar a Tabela Verdade - Prof Robson Liers - Mathematicamente', 'Prof. Robson Liers - Mathematicamente', 'LGCQ0HZpTDw'),
    ('Parnaíba', 'Delta do Parnaíba', 'Programa Expedições - Do Delta do Parnaíba aos Lençóis Maranhenses', 'Instituto Chico Mendes (ICMBio)', '-uZhDA1R0BM'),
]


def cap_recursos():
    s = chapter(12, 'Recursos complementares e referências', 'Vídeos gratuitos opcionais e fontes oficiais')
    s.append(P('Os vídeos são <b>opcionais</b>: o conteúdo principal está neste guia. Eles podem ajudar quem deseja outra explicação de assuntos específicos. Títulos, canais e links foram conferidos em novembro de 2026; os canais podem alterar ou remover vídeos.'))
    s += box('atencao', 'Os vídeos são de canais independentes, sem vínculo com este guia. Em caso de divergência, prevalecem o texto oficial da lei e o edital.')
    rows = [['<b>%s</b>' % d, a, '%s<br/><font color="#5B6573">Canal: %s</font><br/>%s' % (t, c, link('https://www.youtube.com/watch?v=' + v, 'Abrir vídeo'))] for d, a, t, c, v in VIDEOS]
    s += table(['Disciplina', 'Assunto', 'Título, canal e link'], rows, [3.6, 3.8, 9.6], fs=8.8)
    s.append(H2('Referências'))
    refs = [
        'BRASIL. Constituição da República Federativa do Brasil de 1988 — texto atualizado. Câmara dos Deputados: ' + link(CF88, 'camara.leg.br') + '.',
        'BRASIL. Lei nº 13.022, de 8 de agosto de 2014 — Estatuto Geral das Guardas Municipais: ' + link(L13022, 'camara.leg.br (norma atualizada)') + ' · ' + link(PL13022, 'planalto.gov.br') + '.',
        'BRASIL. Lei nº 13.060, de 22 de dezembro de 2014 — instrumentos de menor potencial ofensivo: ' + link(PL13060, 'planalto.gov.br') + '.',
        'BRASIL. Lei nº 8.069/1990 (ECA); Lei nº 10.741/2003 (Estatuto da Pessoa Idosa); Lei nº 11.340/2006 (Lei Maria da Penha); Lei nº 12.527/2011 (Lei de Acesso à Informação); Lei nº 13.146/2015 (Estatuto da Pessoa com Deficiência); Lei nº 13.651/2018 (cria a UFDPar).',
        'ONU. Declaração Universal dos Direitos Humanos, 1948.',
        'STF. ADPF 995 (2023); RE 608.588 — Tema 656 da repercussão geral (2025): ' + link(STF656, 'portal.stf.jus.br') + '.',
        'IBGE. Biblioteca — Parnaíba (PI): histórico e formação administrativa: ' + link(IBGE_HIST, 'biblioteca.ibge.gov.br') + '. Censo Demográfico 2022.',
        'BRASIL. Decreto de 28 de agosto de 1996 — cria a APA Delta do Parnaíba: ' + link(APA, 'planalto.gov.br') + '. Decreto de 16 de novembro de 2000 — cria a Reserva Extrativista Marinha do Delta do Parnaíba.',
        'IPHAN. Registro da produção tradicional e das práticas socioculturais associadas à cajuína no Piauí como Patrimônio Cultural do Brasil (2014).',
    ]
    for r in refs:
        s.append(P(r, ParagraphStyle('ref', parent=ST['bodyL'], fontSize=9.6, leading=13.2, leftIndent=12, firstLineIndent=-12)))
    return s


def conclusao():
    s = chapter('', 'Conclusão', 'Como continuar estudando e acompanhar o edital')
    s.append(lead('Se você percorreu este guia, construiu uma base sólida nas disciplinas que costumam fazer parte de concursos de guardas municipais. O próximo passo é transformar essa base em desempenho.'))
    s.append(H2('Como continuar'))
    s += numbered([
        'Mantenha o <b>plano de revisão</b> em dia (24 h, 7 dias, 30 dias).',
        'Leia a <b>lei seca</b> da Constituição (arts. 1º a 6º, 37 e 144) e a <b>Lei nº 13.022/2014</b> completa, várias vezes.',
        'Resolva muitas <b>questões</b> (por exemplo, no Missão Aprova GCM PHB) e registre os erros.',
        'Reforce os tópicos em que mais errou, voltando à explicação deste guia.',
        'Mantenha uma rotina constante, mesmo que curta, e cuide também da preparação física.',
    ])
    s.append(H2('Quando o edital for publicado'))
    s += numbered([
        'Baixe o edital do site oficial da prefeitura e/ou da banca e confira o conteúdo programático.',
        'Compare com este guia: marque o que já estudou e identifique assuntos novos.',
        'Procure a <b>legislação municipal</b> exigida (Lei Orgânica, estatuto dos servidores, lei da guarda) no site da prefeitura ou da Câmara Municipal.',
        'Verifique se houve alterações na legislação federal (por exemplo, emendas ao art. 144 da Constituição).',
        'Reorganize o cronograma até a prova, priorizando as disciplinas de maior peso.',
    ])
    s += box('recom', ['Nenhum material garante aprovação, mas estudo constante, revisões bem feitas e muita prática aumentam suas chances. Use este guia como base, confie no processo e acompanhe sempre as informações oficiais.'], 'PARA LEVAR COM VOCÊ')
    s.append(sp(12))
    s.append(P('Bons estudos!', 'quote'))
    s.append(P('<b>Inteligência GCM PHB</b> · 2027', 'center'))
    s.append(sp(14))
    s.append(P('Material didático independente de preparação pré-edital, sem vínculo com a Prefeitura Municipal de Parnaíba, a Guarda Civil Municipal ou bancas organizadoras. Informações conferidas em novembro de 2026.', 'small'))
    return s


def montar():
    story = [NextPageTemplate('normal'), PageBreak()]
    story += ficha()
    story += sumario()
    story += apresentacao()
    total_q = 0
    resumos, listas = [], []
    for num, tit, sub, sigla, intro, tops, rev, res, aviso in DISC:
        f, n = render_disciplina(num, tit, sub, sigla, intro, tops, rev, res, aviso)
        story += f
        total_q += n
        resumos.append((tit, res))
        listas.append((tit, ['%s.%d %s' % (sigla, i, t.titulo) for i, t in enumerate(tops, 1)]))
    story += cap_resumos(resumos)
    story += cap_checklist(listas)
    story += cap_plano(listas)
    story += cap_recursos()
    story += conclusao()
    print('Exercícios no total:', total_q)
    return story


def main():
    doc = Doc(SAIDA, title='Inteligência GCM PHB 2027', author='Projeto Inteligência GCM PHB',
              subject='Guia de disciplinas, legislação e conhecimentos locais para a preparação pré-edital — GCM Parnaíba (PI)',
              keywords='concurso, guarda civil municipal, Parnaíba, Português, Constituição, Lei 13.022, direitos humanos',
              creator='Inteligência GCM PHB', lang='pt-BR')
    doc.multiBuild(montar())
    print('PDF gerado:', SAIDA)


if __name__ == '__main__':
    main()
