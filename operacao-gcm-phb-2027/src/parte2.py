# -*- coding: utf-8 -*-
"""Capítulos 7, 8 e 9 — planos de 30, 60 e 90 dias."""
from motor import *

# (dia, disciplina/atividade, tempo, objetivo, tarefa, revisão, exercícios)
D30 = [
    # Semana 1 — adaptação e base
    (1, 'Organização', '60 min', 'Preparar o terreno.', 'Ler Apresentação e Caps. 1–2. Criar pastas, caderno e mapa de disciplinas. Escolher horário fixo.', '—', 'Exercício do Cap. 1 (leitura de edital de outra cidade).'),
    (2, 'Organização', '60 min', 'Definir rotina e ciclo.', 'Ler Caps. 3–4 e 6. Escolher modelo (1, 2 ou 3 h) e montar o ciclo na grade do Cap. 6.', 'Reler anotações do dia 1 (10 min).', 'Exercício do Cap. 4 (desenhar a semana real).'),
    (3, 'Português', '60–120 min', 'Entender a base da interpretação de texto.', 'Leitura ativa: tema central, ideia principal e secundária, inferência. Anotações em duas colunas.', 'Dia 2 (10 min).', '10–15 questões de interpretação.'),
    (4, 'Matemática', '60–120 min', 'Revisar operações básicas.', 'Quatro operações, frações e números decimais. Resolver exemplos à mão.', 'Interpretação: folha em branco (10 min).', '15 questões de frações/decimais.'),
    (5, 'Legislação GCM', '60–120 min', 'Conhecer a Lei 13.022/2014.', 'Leitura ativa da lei no site do Planalto: arts. 1º a 5º (princípios e competências). Anotar palavras-chave.', 'Matemática do dia 4 (10 min).', '10 questões sobre arts. 1º–5º.'),
    (6, 'Revisão semanal', '60–120 min', 'Consolidar a semana.', 'Revisão de tudo que foi estudado (folha em branco + anotações). Criar 10 a 15 flashcards.', 'Todos os assuntos da semana.', 'Mini-simulado de 20 questões misturadas.'),
    (7, 'Descanso / planejamento', 'até 30 min', 'Recuperar energia.', 'Preencher o planner da próxima semana. Ler Cap. 5 (métodos) se desejar.', 'Flashcards (opcional).', '—'),
    # Semana 2
    (8, 'Português', '60–120 min', 'Classes de palavras.', 'Substantivo, adjetivo, verbo, advérbio, pronome, preposição, conjunção — função de cada um, com exemplos.', 'Lei 13.022, arts. 1º–5º (revisão de 3 dias).', '15 questões de classes de palavras.'),
    (9, 'Matemática', '60–120 min', 'Razão, proporção e regra de três simples.', 'Teoria com exemplos; diferenciar grandezas diretas e inversas.', 'Classes de palavras (24 h).', '15 questões de regra de três.'),
    (10, 'Informática', '60–120 min', 'Conceitos básicos.', 'Hardware x software, sistema operacional, arquivos e pastas, atalhos comuns.', 'Regra de três (24 h).', '15 questões de conceitos básicos.'),
    (11, 'Legislação GCM', '60–120 min', 'Lei 13.022: competências específicas.', 'Arts. 5º a 9º: competências específicas e criação da guarda. Montar tabela com os incisos mais importantes.', 'Informática (24 h).', '10–15 questões.'),
    (12, 'Const./Direitos Humanos', '60–120 min', 'Direitos e garantias fundamentais.', 'CF, art. 5º: leitura dos incisos mais cobrados (igualdade, legalidade, liberdade, inviolabilidade do domicílio). Anotar.', 'Lei 13.022 arts. 5º–9º (24 h).', '10–15 questões.'),
    (13, 'Revisão semanal', '60–120 min', 'Revisão de 7 dias.', 'Revisar semana 1 (7 dias) e semana 2 (24 h a 5 dias). Atualizar caderno de erros.', 'Semanas 1 e 2.', 'Mini-simulado de 25 questões.'),
    (14, 'Descanso / planejamento', 'até 30 min', 'Avaliar a quinzena.', 'Registrar horas e acertos no planner. Ajustar o ciclo se necessário.', 'Flashcards (opcional).', '—'),
    # Semana 3
    (15, 'Português', '60–120 min', 'Concordância verbal e nominal.', 'Regras gerais e principais casos especiais. Criar exemplos próprios.', 'Art. 5º da CF (24 h).', '15–20 questões de concordância.'),
    (16, 'Matemática / RLM', '60–120 min', 'Porcentagem.', 'Cálculo de porcentagem, aumentos e descontos, aumentos sucessivos.', 'Concordância (24 h).', '20 questões de porcentagem.'),
    (17, 'Legislação GCM', '60–120 min', 'Lei 13.022: requisitos e capacitação.', 'Arts. 10 a 12 (requisitos de investidura e capacitação). Criar flashcards dos requisitos.', 'Porcentagem (24 h).', '10–15 questões.'),
    (18, 'Informática', '60–120 min', 'Editores de texto e planilhas.', 'Funções básicas de editor de texto e planilha (fórmulas simples como SOMA e MÉDIA).', 'Requisitos da Lei 13.022 (24 h).', '15 questões.'),
    (19, 'Português', '60–120 min', 'Pontuação.', 'Uso da vírgula (principais regras e proibições), ponto e vírgula, dois-pontos.', 'Informática (24 h) + revisão 7 dias de classes de palavras.', '15–20 questões.'),
    (20, 'Revisão semanal', '60–120 min', 'Revisão de 7 dias e caderno de erros.', 'Revisar assuntos da semana 2 (7 dias). Refazer questões erradas do caderno.', 'Semana 2 e 3.', 'Simulado de 30 questões (1 h 15).'),
    (21, 'Descanso / planejamento', 'até 30 min', 'Recarregar.', 'Planejar a semana 4. Ler Cap. 13 (disciplina e consistência).', '—', '—'),
    # Semana 4
    (22, 'Matemática / RLM', '60–120 min', 'Raciocínio lógico: proposições.', 'Proposições simples e compostas, conectivos (e, ou, se…então), tabela-verdade básica.', 'Pontuação (24 h).', '15 questões.'),
    (23, 'Const./Direitos Humanos', '60–120 min', 'Segurança pública na CF.', 'CF, art. 144 (órgãos de segurança pública e § 8º sobre guardas municipais).', 'Proposições (24 h).', '10–15 questões.'),
    (24, 'Português', '60–120 min', 'Crase.', 'Casos obrigatórios, proibidos e facultativos.', 'Art. 144 (24 h).', '15–20 questões.'),
    (25, 'Legislação GCM', '60–120 min', 'Lei 13.022: demais artigos.', 'Arts. 13 em diante (controle, prerrogativas, vedações e disposições finais). Revisar a lei completa.', 'Crase (24 h).', '15 questões da lei inteira.'),
    (26, 'Informática', '60–120 min', 'Internet e segurança.', 'Navegadores, e-mail, nuvem, golpes (phishing), vírus e boas práticas.', 'Lei 13.022 (24 h).', '15 questões.'),
    (27, 'Conhecimentos locais', '60 min', 'Conhecer Parnaíba.', 'Ler fontes confiáveis (IBGE Cidades, site da prefeitura) sobre dados gerais, história e geografia do município. Anotar fatos principais.', 'Informática (24 h).', '—'),
    (28, 'Simulado', '2–3 h', 'Medir o primeiro mês.', 'Simulado de 40–60 questões com tempo cronometrado, de todas as disciplinas estudadas.', '—', 'Simulado completo.'),
    (29, 'Análise e erros', '60–120 min', 'Transformar o simulado em plano.', 'Corrigir, calcular % por disciplina, classificar os erros e registrar no caderno.', 'Revisão de 30 dias dos assuntos da semana 1.', 'Refazer questões erradas.'),
    (30, 'Planejamento', '60 min', 'Fechar o ciclo de 30 dias.', 'Preencher a avaliação do mês (Cap. 15). Ajustar o ciclo e escolher o próximo plano (60 ou 90 dias).', 'Flashcards.', '—'),
]


def cap7():
    s = chapter(7, 'Plano de 30 dias', 'Um mês para criar o hábito e construir a base')
    s.append(lead('Este plano foi pensado para quem está começando. Ele cria a rotina, apresenta as disciplinas de base e já inclui revisões, questões e um primeiro simulado.'))
    s.append(H2('Como usar o plano'))
    s += bullets([
        '<b>Tempo:</b> “60–120 min” significa que o dia funciona tanto no modelo de 1 hora quanto no de 2 horas. Com 1 hora, faça a tarefa de forma mais enxuta e menos questões; com 3 horas, aprofunde a teoria e faça mais questões.',
        '<b>Dias da semana:</b> o dia 1 pode começar em qualquer dia. Os dias 7, 14 e 21 são de descanso; troque-os de lugar se precisar.',
        '<b>Atrasou?</b> Não pule dias: continue de onde parou. O plano é uma sequência, não um calendário rígido.',
        '<b>Disciplinas:</b> são exemplos de base pré-edital. Quando o edital sair, ajuste.',
        '<b>Questões:</b> use questões de concursos de nível médio, de preferência de guardas municipais e de bancas que atuam na região.',
    ])
    s += box('dica', 'Marque cada dia concluído na coluna “Dia” com um ✓ no seu caderno ou use o checklist de 30 dias logo após o cronograma.')
    weeks = [('Semana 1 — Adaptação e diagnóstico', 0, 7), ('Semana 2 — Base das disciplinas', 7, 14),
             ('Semana 3 — Aprofundamento e primeiras revisões de 7 dias', 14, 21),
             ('Semana 4 — Ampliação, simulado e ajuste', 21, 30)]
    for title, a, b in weeks:
        s.append(H2(title))
        rows = []
        for d in D30[a:b]:
            dia, disc, tempo, obj, tarefa, rev, ex = d
            rows.append(['<b><font size="11" color="#0E2238">Dia %d</font></b><br/><font color="#0F7C7A"><b>%s</b></font><br/><font size="8" color="#5B6573">%s</font>' % (dia, disc, tempo),
                         obj, tarefa, rev, ex])
        s += table(['Dia / disciplina / tempo', 'Objetivo', 'Tarefa', 'Revisão', 'Exercícios'], rows,
                   [3.0, 3.0, 5.4, 2.9, 2.7], fs=8.8, split=True)
    s.append(H2('Checklist dos 30 dias'))
    items = ['Dia %d — %s: %s' % (d[0], d[1], d[3]) for d in D30]
    s.append(CheckList(items, prefix='p30'))
    s += box('recom', 'Ao fim dos 30 dias, se você cumpriu pelo menos 20 dias, considere o plano um sucesso: o hábito foi criado. Siga para o Plano de 60 ou 90 dias. Se cumpriu menos, repita a estrutura do mês com metas menores (Cap. 13).')
    return s


def cap8():
    s = chapter(8, 'Plano de 60 dias', 'Progressão em três fases: base, aprofundamento e prática')
    s.append(lead('O plano de 60 dias serve para quem já criou o hábito (ou acabou de concluir o Plano de 30 dias) e quer cobrir as disciplinas de base com mais profundidade, revisões regulares e simulados.'))
    s.append(FlowSteps([('Fase 1 · Dias 1–20', 'Base sólida'), ('Fase 2 · Dias 21–40', 'Aprofundamento'), ('Fase 3 · Dias 41–60', 'Prática e revisão')], per_row=3, box_h=1.5 * cm, numbered=False))
    s.append(sp(8))
    s.append(H2('Visão geral das fases'))
    s += table(['Fase', 'Foco', 'Proporção do tempo', 'Meta da fase'], [
        ['1 — Base (dias 1–20)', 'Teoria das disciplinas de base com questões fáceis e médias.', 'Teoria 50% · Questões 30% · Revisão 20%', 'Ver os assuntos fundamentais de Português, Matemática, Informática e Lei 13.022.'],
        ['2 — Aprofundamento (dias 21–40)', 'Assuntos mais difíceis, Constitucional/Direitos Humanos e legislação complementar.', 'Teoria 40% · Questões 35% · Revisão 25%', 'Atingir 60–65% de acertos nas disciplinas de base.'],
        ['3 — Prática (dias 41–60)', 'Questões, simulados e revisão dos erros.', 'Teoria 25% · Questões 45% · Revisão 30%', 'Atingir 70% de acertos e fazer 3 simulados.'],
    ], [3.6, 5.0, 3.8, 4.6], bold_first=True)
    s.append(H2('Fase 1 — Base (dias 1 a 20)'))
    s += table(['Semana', 'Metas de conteúdo', 'Revisões', 'Exercícios'], [
        ['Dias 1–7', 'Português: interpretação, classes de palavras. Matemática: operações, frações, regra de três. Lei 13.022: arts. 1º–5º.', '24 h diária; revisão semanal no dia 6.', '80–100 questões na semana.'],
        ['Dias 8–14', 'Português: concordância, pontuação. Matemática: porcentagem. Informática: conceitos básicos e sistema operacional. Lei 13.022: arts. 5º–12.', '24 h diária; 7 dias dos assuntos da semana anterior.', '100–120 questões.'],
        ['Dias 15–20', 'Português: crase, regência. RLM: proposições. Informática: editores e planilhas. Lei 13.022: restante.', '24 h, 7 dias; revisão geral no dia 20.', 'Simulado curto (30 questões) no dia 20.'],
    ], [2.4, 7.6, 3.8, 3.2], bold_first=True)
    s.append(H2('Fase 2 — Aprofundamento (dias 21 a 40)'))
    s += table(['Semana', 'Metas de conteúdo', 'Revisões', 'Exercícios'], [
        ['Dias 21–27', 'CF: arts. 1º–5º e art. 144. Português: regência, colocação pronominal. Matemática: juros simples, equações do 1º grau.', '24 h, 7 dias e 30 dias (assuntos dos dias 1–7).', '120 questões.'],
        ['Dias 28–34', 'Direitos Humanos (noções). RLM: sequências e problemas lógicos. Informática: internet, e-mail e segurança. Leis municipais (se disponíveis).', '24 h, 7 dias, 30 dias.', '120–140 questões; simulado de 40 questões no dia 34.'],
        ['Dias 35–40', 'Revisar pontos fracos indicados pelo caderno de erros e pelo simulado. Conhecimentos gerais e locais.', 'Revisão de todo o caderno de erros.', '100 questões focadas nos pontos fracos.'],
    ], [2.4, 7.6, 3.8, 3.2], bold_first=True)
    s.append(H2('Fase 3 — Prática e revisão (dias 41 a 60)'))
    s += table(['Semana', 'Metas', 'Revisões', 'Exercícios'], [
        ['Dias 41–47', 'Questões por disciplina com tempo. Teoria só para lacunas.', '30 dias dos assuntos da fase 1; flashcards diários.', '150 questões; simulado de 50 questões no dia 47.'],
        ['Dias 48–54', 'Leitura da Lei 13.022 completa e dos artigos da CF estudados. Resumos de 1 página por disciplina.', 'Caderno de erros completo.', '150 questões; questões de provas de guardas municipais.'],
        ['Dias 55–60', 'Simulado final e balanço. Planejar os próximos passos.', 'Revisão geral com resumos.', 'Simulado de 60 questões (dia 57); análise (dia 58).'],
    ], [2.4, 7.6, 3.8, 3.2], bold_first=True)
    s.append(H2('Rotina diária típica no plano de 60 dias (2 h)'))
    s += table(['Ordem', 'Atividade', 'Tempo'], [
        ['1', 'Revisão de 24 h + flashcards', '15 min'],
        ['2', 'Teoria da disciplina do ciclo', '40–50 min'],
        ['3', 'Pausa', '10 min'],
        ['4', 'Questões (mesmo assunto ou assunto anterior)', '35–40 min'],
        ['5', 'Caderno de erros + plano de amanhã', '10–15 min'],
    ], [1.6, 12.4, 3.0])
    s.append(CondPageBreak(9.5 * cm))
    s.append(H2('Acompanhamento do plano de 60 dias'))
    s.append(P('Preencha ao final de cada bloco de 10 dias. Compare os números e ajuste o ciclo conforme o Capítulo 6.'))
    s.append(FormGrid(['Período', 'Horas líquidas', 'Questões feitas', '% acertos', 'Revisões cumpridas (%)', 'Disciplina mais fraca', 'Ajuste decidido'],
                      [2.0, 2.0, 2.0, 1.8, 2.4, 3.2, 3.6], 6, row_h=1.0 * cm, prefix='p60',
                      first_col=['Dias 1–10', 'Dias 11–20', 'Dias 21–30', 'Dias 31–40', 'Dias 41–50', 'Dias 51–60']))
    return s


def cap9():
    s = chapter(9, 'Plano de 90 dias', 'Fase inicial, consolidação, revisão, prática, simulados e ajustes')
    s.append(lead('O plano de 90 dias é o mais completo. Ele é ideal para quem começa com bastante antecedência ou quer uma preparação pré-edital robusta, deixando a base pronta para quando o edital for publicado.'))
    s.append(FlowSteps([('Fase inicial', 'Dias 1–30 · Base'), ('Consolidação', 'Dias 31–60 · Profundidade'),
                        ('Revisão e prática', 'Dias 61–90 · Simulados')], per_row=3, box_h=1.5 * cm, numbered=False))
    s.append(sp(8))
    s.append(H2('Estrutura geral'))
    s += table(['Fase', 'Objetivo', 'O que muda na rotina', 'Indicador de sucesso'], [
        ['Inicial (dias 1–30)', 'Criar o hábito e estudar a base de todas as disciplinas prioritárias.', 'Mais teoria; questões fáceis; revisão de 24 h e semanal.', '≥ 20 dias de estudo; todos os assuntos de base vistos uma vez.'],
        ['Consolidação (31–60)', 'Aprofundar, cobrir disciplinas complementares e fortalecer pontos fracos.', 'Equilíbrio entre teoria e questões; revisões de 7 e 30 dias; caderno de erros ativo.', '≥ 65% de acertos nas disciplinas de base.'],
        ['Revisão e prática (61–90)', 'Treinar como na prova e revisar tudo.', 'Predomínio de questões e simulados; teoria só para lacunas.', '≥ 70% de acertos; 4 simulados feitos e analisados.'],
    ], [3.3, 4.5, 5.0, 4.2], bold_first=True)
    s.append(H2('Fase inicial — dias 1 a 30'))
    s.append(P('Siga o <b>Plano de 30 Dias</b> (Capítulo 7). Ele já está desenhado para essa fase. Se tiver 3 horas por dia, acrescente a cada dia um segundo bloco curto de uma disciplina leve (Informática ou Conhecimentos gerais).'))
    s.append(H2('Fase de consolidação — dias 31 a 60'))
    s += table(['Semana', 'Conteúdo (exemplo)', 'Revisão', 'Prática'], [
        ['5 (31–37)', 'Português: regência e colocação pronominal. Matemática: equações do 1º grau e sistemas simples. CF: art. 5º (continuação).', '7 e 30 dias da semana 1.', '120 questões.'],
        ['6 (38–44)', 'RLM: sequências, lógica de argumentação. Informática: segurança da informação. Direitos Humanos: noções e principais documentos.', '7 e 30 dias da semana 2.', '120 questões; simulado de 40 questões.'],
        ['7 (45–51)', 'Português: semântica (sinônimos, antônimos, sentido figurado) e reescrita de frases. Matemática: juros simples, média e problemas. Legislação local (se disponível).', '7 e 30 dias da semana 3.', '140 questões.'],
        ['8 (52–60)', 'Conteúdos complementares (noções de Direito Administrativo e Penal, ECA, trânsito — conforme tempo). Revisão dirigida pelo caderno de erros.', 'Caderno de erros completo; 30 dias da semana 4.', '140 questões; simulado de 50 questões no dia 60.'],
    ], [2.3, 8.2, 3.5, 3.0], bold_first=True)
    s.append(H2('Fase de revisão e prática — dias 61 a 90'))
    s += table(['Semana', 'Foco', 'Simulado', 'Ajuste'], [
        ['9 (61–67)', 'Questões por disciplina com tempo controlado. Resumos de 1 página por disciplina.', '—', 'Identificar as 3 disciplinas mais fracas.'],
        ['10 (68–74)', 'Bloco extra para as 3 disciplinas mais fracas. Leitura completa da Lei 13.022.', 'Simulado 2 (60 questões).', 'Comparar com o simulado do dia 60.'],
        ['11 (75–81)', 'Revisão geral por resumos e flashcards; questões mistas.', 'Simulado 3 (60 questões).', 'Ajustar ordem de resolução e tempo por questão.'],
        ['12 (82–88)', 'Caderno de erros completo; refazer questões erradas.', 'Simulado 4 (60 questões).', 'Definir o ciclo pós-90 dias.'],
        ['Dias 89–90', 'Balanço final e planejamento da manutenção.', '—', 'Preencher o painel de 90 dias.'],
    ], [2.3, 7.4, 3.3, 4.0], bold_first=True)
    s.append(H2('Calendário de simulados'))
    s.append(Timeline([('D28', 'Simulado 0', 'Diagnóstico do 1º mês (40–60 q.)'),
                       ('D60', 'Simulado 1', '50 questões · fim da consolidação'),
                       ('D74', 'Simulado 2', '60 questões · com tempo real'),
                       ('D81', 'Simulado 3', '60 questões · testar estratégia'),
                       ('D88', 'Simulado 4', '60 questões · balanço final')], height=3.5 * cm))
    s.append(H2('Como fazer ajustes durante os 90 dias'))
    s += table(['Se acontecer…', 'Faça…'], [
        ['Perdi uma semana inteira', 'Retome do ponto onde parou; não tente “compensar” estudando o dobro. Corte teoria nova da semana seguinte e priorize revisões atrasadas.'],
        ['Uma disciplina não evolui', 'Volte à teoria básica, procure outra explicação (outro material ou vídeo complementar) e faça questões mais fáceis antes das difíceis.'],
        ['As revisões estão acumulando', 'Faça uma “semana de revisão” sem conteúdo novo. Depois, reduza a quantidade de assuntos novos por semana.'],
        ['O edital foi publicado durante o plano', 'Pare, leia o edital (Cap. 1) e refaça o ciclo. A partir daí, siga o conteúdo programático oficial e as datas do concurso.'],
        ['Notas de simulado caíram', 'Analise se foi conteúdo, interpretação, tempo ou cansaço. Uma queda isolada é normal; observe a tendência de 2–3 simulados.'],
    ], [5.0, 12.0], bold_first=True)
    s.append(CondPageBreak(13.5 * cm))
    s.append(H2('Painel de acompanhamento de 90 dias'))
    s.append(FormGrid(['Semana', 'Horas', 'Questões', '% acertos', 'Simulado (nota)', 'Ponto forte', 'Ponto a melhorar'],
                      [1.8, 1.6, 1.9, 1.8, 2.3, 3.8, 3.8], 13, row_h=0.78 * cm, prefix='p90',
                      first_col=[str(i) for i in range(1, 14)]))
    return s
