# -*- coding: utf-8 -*-
"""Capítulos 10 a 17 e conclusão."""
from motor import *

L13022 = 'https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l13022.htm'
CF88 = 'https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm'


def cap10():
    s = chapter(10, 'Como fazer revisões', 'Revisão de 24 horas, 7 dias e 30 dias')
    s.append(lead('Sem revisão, boa parte do que você estuda hoje tende a ser esquecida em poucos dias. A revisão não é “estudar de novo”: é recuperar o que já foi aprendido, em menos tempo e com mais eficiência.'))
    s.append(Timeline([('D0', 'Estudo', 'Teoria + questões + anotações'),
                       ('24h', 'Revisão 1', '10–15 min · recuperar de memória'),
                       ('7d', 'Revisão 2', '15–20 min · flashcards e questões'),
                       ('30d', 'Revisão 3', '20–30 min · resumo + questões mistas')], height=3.4 * cm))
    s.append(H2('Revisão de 24 horas'))
    s += table(None, [
        ['Quando', 'No dia seguinte ao estudo (de preferência no início da sessão).'],
        ['Duração', '10 a 15 minutos por assunto.'],
        ['Como', '1) Sem olhar o material, escreva ou fale tudo o que lembra (folha em branco). 2) Confira com suas anotações e complete com outra cor. 3) Revise os flashcards criados ontem.'],
        ['Objetivo', 'Fixar o conteúdo enquanto ele ainda está “fresco” e descobrir o que não ficou claro.'],
    ], [3.0, 14.0], zebra=False, bold_first=True)
    s.append(H2('Revisão de 7 dias'))
    s += table(None, [
        ['Quando', 'Uma semana após o estudo. Uma boa prática é concentrar no dia de revisão semanal (ex.: sábado).'],
        ['Duração', '15 a 20 minutos por assunto.'],
        ['Como', '1) Recupere de memória os pontos principais. 2) Faça 5 a 10 questões do assunto. 3) Revise os erros do caderno de erros desse assunto. 4) Atualize o resumo, se houver.'],
        ['Objetivo', 'Consolidar e verificar se o assunto já pode ir para um intervalo maior.'],
    ], [3.0, 14.0], zebra=False, bold_first=True)
    s.append(H2('Revisão de 30 dias'))
    s += table(None, [
        ['Quando', 'Cerca de um mês após o estudo.'],
        ['Duração', '20 a 30 minutos por assunto ou por bloco de assuntos relacionados.'],
        ['Como', '1) Leia o resumo de 1 página. 2) Faça questões misturando assuntos da disciplina. 3) Revise todo o caderno de erros do bloco. 4) Defina: precisa de nova revisão em 30 dias ou pode ir para 60 dias?'],
        ['Objetivo', 'Manter o conteúdo de longo prazo e integrar assuntos.'],
    ], [3.0, 14.0], zebra=False, bold_first=True)
    s.append(H2('Agenda de revisões: exemplo prático'))
    s += table(['Assunto estudado em', 'Revisão 24 h', 'Revisão 7 dias', 'Revisão 30 dias'], [
        ['Seg 05/04 — Crase', 'Ter 06/04', 'Sáb 10/04 (dia de revisão semanal)', 'Qua 05/05'],
        ['Ter 06/04 — Porcentagem', 'Qua 07/04', 'Sáb 10/04 (adiantada 3 dias)', 'Qui 06/05'],
        ['Qua 07/04 — Lei 13.022, arts. 1º–5º', 'Qui 08/04', 'Sáb 17/04 (atrasada 3 dias)', 'Sex 07/05'],
    ], [5.4, 3.2, 4.8, 3.6])
    s.append(P('Note que as revisões de 7 dias foram <b>agrupadas no sábado</b>. Pequenas antecipações ou atrasos (2 a 3 dias) não prejudicam o método e simplificam a rotina.', 'small'))
    s.append(H2('Como adaptar as revisões'))
    s += table(['Situação', 'Adaptação'], [
        ['Você esqueceu quase tudo na revisão', 'Reestude rapidamente e encurte o próximo intervalo (ex.: revise de novo em 3 dias).'],
        ['Você lembrou tudo com facilidade', 'Alongue o próximo intervalo (ex.: de 30 para 45–60 dias).'],
        ['Tem só 1 hora por dia', 'Limite a revisão a 10–15 min diários e concentre as de 7 e 30 dias em um único dia da semana.'],
        ['As revisões acumularam', 'Priorize: 1º caderno de erros, 2º revisões de 7 dias, 3º revisões de 30 dias. Suspenda conteúdo novo por alguns dias.'],
        ['Disciplina de memorização (lei)', 'Use mais flashcards e leitura da lei seca nas revisões.'],
        ['Disciplina de prática (Matemática)', 'Revise fazendo questões, não relendo teoria.'],
    ], [5.5, 11.5], bold_first=True)
    s += box('recom', 'Registre as revisões no planner semanal (Cap. 14). Uma coluna simples com o assunto e as três datas já resolve. No celular, aplicativos de flashcards com repetição espaçada calculam os intervalos automaticamente.')
    return s


def cap11():
    s = chapter(11, 'Como resolver questões', 'Interpretar, evitar desatenção, identificar pegadinhas e estudar pelos erros')
    s.append(H2('Como interpretar enunciados'))
    s.append(P('Muitos erros não vêm da falta de conhecimento, e sim da leitura apressada do enunciado. Use este roteiro em todas as questões:'))
    s.append(FlowSteps([('Comando', 'O que a questão pede?'), ('Palavras-chave', 'circule termos decisivos'),
                        ('Alternativas', 'leia todas'), ('Eliminação', 'descarte as erradas'), ('Confirmação', 'releia o comando')], per_row=5, box_h=1.5 * cm))
    s.append(sp(8))
    s += table(['Tipo de comando', 'O que significa', 'Cuidado'], [
        ['“Assinale a correta”', 'Uma alternativa é verdadeira.', 'As outras podem ter um único detalhe errado.'],
        ['“Assinale a incorreta / EXCETO”', 'Procura-se a falsa.', 'É o comando que mais gera erro por desatenção.'],
        ['“De acordo com o texto”', 'A resposta deve estar no texto, não na sua opinião.', 'Não use conhecimento externo que contrarie o texto.'],
        ['“Infere-se do texto”', 'Conclusão lógica a partir do texto.', 'Não é extrapolar: precisa haver base.'],
        ['“Segundo a Lei…”', 'Vale o texto legal.', 'Atenção a prazos, números e palavras como “poderá” e “deverá”.'],
    ], [4.4, 5.6, 7.0], bold_first=True)
    s.append(H2('Como evitar erros por desatenção'))
    s += bullets([
        '<b>Circule</b> as palavras de comando: não, exceto, incorreta, sempre, somente, apenas.',
        'Leia <b>todas</b> as alternativas, mesmo que a primeira pareça certa.',
        'Em cálculos, <b>confira a unidade</b> pedida (reais, metros, porcentagem) e se a pergunta é sobre o total ou a diferença.',
        'Transcreva para o gabarito em blocos (ex.: a cada 10 questões), com atenção ao número da questão.',
        'Quando estiver cansado, faça uma pausa de 1 minuto: respire, beba água, volte.',
    ])
    s.append(H2('Como identificar pegadinhas'))
    s += table(['Pegadinha comum', 'Exemplo', 'Como se proteger'], [
        ['Troca de uma palavra', '“O prazo é de até 2 anos, <b>improrrogável</b>.” (o correto é prorrogável uma vez)', 'Compare cada palavra com o que você sabe; desconfie de termos absolutos.'],
        ['Generalização', '“Todos”, “nunca”, “sempre”, “exclusivamente”.', 'Termos absolutos costumam tornar a afirmação falsa, mas nem sempre — verifique.'],
        ['Inversão de conceito', 'Atribuir a um órgão a competência de outro.', 'Use tabelas comparativas nas suas anotações.'],
        ['Número alterado', 'Idade, prazo ou percentual trocado.', 'Faça flashcards de números e prazos.'],
        ['Alternativa “quase certa”', 'Correta na primeira parte e errada no final.', 'Leia até o fim, especialmente alternativas longas.'],
        ['Extrapolação de texto', 'Conclusão plausível, mas que o texto não autoriza.', 'Pergunte: “onde isso está escrito?”.'],
    ], [3.8, 6.8, 6.4], bold_first=True)
    s.append(H2('Como estudar por erros'))
    s.append(P('Toda questão errada deve ser classificada por <b>tipo de erro</b>. Cada tipo pede uma ação diferente:'))
    s += table(['Tipo de erro', 'Sinal', 'Ação'], [
        ['Falta de conteúdo', 'Você não sabia o assunto.', 'Voltar à teoria; criar resumo/flashcard.'],
        ['Conteúdo incompleto', 'Sabia a regra, mas não a exceção.', 'Anotar a exceção no caderno de erros e em flashcard.'],
        ['Interpretação', 'Entendeu errado o enunciado ou o texto.', 'Treinar o roteiro de leitura; fazer mais questões de interpretação.'],
        ['Desatenção', 'Sabia, mas leu errado ou marcou errado.', 'Circular palavras de comando; reduzir a pressa.'],
        ['Cálculo', 'Errou uma conta.', 'Conferir operações; treinar contas básicas.'],
        ['Chute errado', 'Não sabia e arriscou.', 'Estudar o assunto; registrar como falta de conteúdo.'],
    ], [3.8, 5.6, 7.6], bold_first=True)
    s += box('dica', 'Também analise questões que você <b>acertou no chute</b> ou com dúvida. Para efeitos de estudo, trate-as como erro.')
    s.append(CondPageBreak(10 * cm))
    s.append(H2('Como analisar o desempenho'))
    s.append(P('Uma vez por semana, preencha a tabela abaixo (ou a do planner). Calcule o percentual: <b>acertos ÷ questões × 100</b>.'))
    s.append(FormGrid(['Disciplina', 'Questões', 'Acertos', '% acertos', 'Principal tipo de erro', 'Ação para a próxima semana'],
                      [3.6, 1.8, 1.8, 1.8, 3.6, 4.4], 7, row_h=0.85 * cm, prefix='desemp',
                      first_col=['Português', 'Matemática/RLM', 'Informática', 'Legislação GCM', 'Const./DH', 'Conh. gerais', 'Outra']))
    s.append(sp(8))
    s += table(['% de acertos', 'Leitura', 'Estratégia sugerida'], [
        ['Abaixo de 50%', 'Base ainda frágil.', 'Mais teoria básica e questões fáceis.'],
        ['50% a 69%', 'Em construção.', 'Equilibrar teoria e questões; reforçar erros mais frequentes.'],
        ['70% a 84%', 'Bom domínio.', 'Mais questões, revisões e simulados.'],
        ['85% ou mais', 'Domínio elevado.', 'Manutenção com questões e revisões espaçadas.'],
    ], [3.5, 4.5, 9.0], bold_first=True)
    s.append(P('Essas faixas são referências pedagógicas para orientar o estudo, não notas de corte. A nota necessária no concurso dependerá do edital e da concorrência.', 'small'))
    s += box('exerc', 'Resolva 20 questões de uma disciplina. Em seguida, classifique cada erro pelo tipo (tabela acima) e registre ao menos 3 no caderno de erros do Capítulo 12.')
    return s


def cap12():
    s = chapter(12, 'Caderno de erros', 'Modelos preenchíveis para transformar erros em pontos')
    s.append(lead('O caderno de erros é o seu material mais personalizado: ele mostra exatamente o que <b>você</b> precisa revisar. Use os modelos abaixo digitando no PDF ou imprimindo.'))
    s.append(H2('Como preencher cada campo'))
    s += table(['Campo', 'O que escrever', 'Exemplo'], [
        ['Data', 'Dia em que errou.', '12/04'],
        ['Disciplina', 'Nome da disciplina.', 'Português'],
        ['Assunto', 'Tópico específico.', 'Crase antes de horas'],
        ['Questão', 'Referência curta (fonte/ano/nº) ou resumo do enunciado.', 'Banca X, 2024, q. 7'],
        ['Erro cometido', 'O que você marcou e por quê.', 'Marquei “sem crase” em “às 8h”.'],
        ['Motivo', 'Conteúdo, exceção, interpretação, desatenção, cálculo ou chute.', 'Conteúdo incompleto'],
        ['Correção', 'A regra correta, com suas palavras.', 'Antes de horas determinadas usa-se crase: “às 8h”.'],
        ['Próxima revisão', 'Data para revisar (24 h, 7 d ou 30 d).', '19/04'],
    ], [3.0, 7.4, 6.6], bold_first=True)
    s += box('dica', 'No celular, os campos “Erro cometido” e “Correção” aceitam várias linhas. Para registros longos, use também o espaço de anotações ao final de cada página.')
    hdr = ['Data', 'Disciplina', 'Assunto', 'Questão', 'Erro cometido', 'Motivo', 'Correção', 'Próx. revisão']
    w = [1.5, 2.0, 2.2, 1.9, 2.9, 1.8, 3.0, 1.7]
    for i in range(1, 4):
        s.append(PageBreak())
        s.append(H2('Caderno de erros — folha %d' % i))
        s.append(FormGrid(hdr, w, 12, row_h=1.45 * cm, prefix='erros%d' % i, multiline_cols=(2, 3, 4, 6)))
        s.append(sp(10))
        s.append(WriteLines(3, 'Padrões que percebi nesta folha (erros que se repetem):', prefix='erros_padroes'))
    s.append(PageBreak())
    s.append(H2('Ficha detalhada de erro (para erros importantes)'))
    s.append(P('Use esta ficha quando um erro for recorrente ou envolver um conceito central.'))
    for k in range(2):
        s.append(FormGrid(['Campo', 'Registro'], [4.0, 13.0], 8, row_h=1.15 * cm, prefix='ficha%d' % k,
                          first_col=['Data', 'Disciplina / assunto', 'Questão (fonte)', 'Erro cometido', 'Motivo', 'Correção (regra certa)', 'Como evitar de novo', 'Próximas revisões'],
                          multiline_cols=(1,)))
        s.append(sp(14))
    return s


def cap13():
    s = chapter(13, 'Disciplina e consistência', 'Procrastinação, hábitos, desmotivação e metas realistas')
    s.append(lead('Motivação ajuda a começar; hábito é o que faz continuar. A preparação para concurso é uma maratona, e a vitória está mais na constância do que na intensidade.'))
    s.append(H2('Como evitar a procrastinação'))
    s.append(P('Procrastinar não é preguiça: muitas vezes é fuga de uma tarefa que parece grande, chata ou difícil demais. A solução é tornar a tarefa <b>menor, clara e fácil de começar</b>.'))
    s += table(['Estratégia', 'Como aplicar'], [
        ['Regra dos 2 minutos', 'Comprometa-se apenas a abrir o material e estudar 2 minutos. Começar costuma ser a parte mais difícil.'],
        ['Tarefa específica', 'Troque “estudar Português” por “ler as págs. 12–18 sobre crase e fazer 10 questões”.'],
        ['Blocos de foco', 'Trabalhe em blocos curtos (ex.: 25 min de foco + 5 min de pausa). Depois de 4 blocos, uma pausa maior.'],
        ['Ambiente sem distrações', 'Celular em outro cômodo ou em modo foco; abas fechadas; avise a família do seu horário.'],
        ['Intenção de implementação', 'Planeje no formato “Quando ___, eu vou ___”. Ex.: “Quando chegar do trabalho e jantar, vou estudar 1 hora na mesa da sala”.'],
    ], [4.5, 12.5], bold_first=True)
    s.append(H2('Como manter a constância'))
    s += bullets([
        '<b>Não quebre a corrente:</b> marque no calendário cada dia estudado. Visualizar a sequência motiva a continuar.',
        '<b>Estudo mínimo:</b> nos dias difíceis, faça 15 minutos. O objetivo é manter o hábito vivo.',
        '<b>Planeje a semana no domingo</b> e o dia na véspera.',
        '<b>Celebre marcos:</b> 30 dias, 100 horas, primeiro simulado. Recompensas simples reforçam o comportamento.',
        '<b>Estude acompanhado:</b> um colega de estudo ou grupo com metas semanais aumenta o compromisso.',
    ])
    s.append(H2('Como retomar depois de parar'))
    s.append(P('Todo candidato para em algum momento: doença, trabalho, problemas pessoais. O erro é transformar uma pausa em desistência.'))
    s += numbered([
        '<b>Sem culpa:</b> aceite a pausa. Culpa consome energia que poderia ir para o estudo.',
        '<b>Recomece pequeno:</b> na primeira semana, metade do tempo que você estudava.',
        '<b>Revise antes de avançar:</b> dedique os primeiros dias a revisões e ao caderno de erros.',
        '<b>Retome o ciclo de onde parou</b>, sem tentar recuperar tudo de uma vez.',
        '<b>Investigue a causa:</b> se a rotina era pesada demais, ajuste-a para não parar de novo.',
    ])
    s.append(H2('Como enfrentar a desmotivação'))
    s += table(['Pensamento', 'Resposta mais útil'], [
        ['“Não tenho edital, para que estudar?”', 'Quem estuda antes chega ao edital com vantagem. Cada hora agora alivia a pressão depois.'],
        ['“Estou errando muito.”', 'Errar no treino é o que permite acertar na prova. Seus erros viram seu caderno de revisão.'],
        ['“Os outros estudam mais.”', 'Compare você com você do mês passado. Acompanhe seus próprios números.'],
        ['“Não tenho tempo.”', '30 minutos diários somam cerca de 15 horas por mês.'],
        ['“Não sou bom em Matemática.”', 'Habilidade se desenvolve com prática progressiva: comece pelo básico e avance.'],
    ], [6.0, 11.0], bold_first=True)
    s += box('recom', 'Escreva em uma folha os seus motivos para querer o cargo (estabilidade, servir à comunidade, carreira) e deixe-a visível no local de estudo. Releia nos dias difíceis.')
    s.append(H2('Como criar hábitos'))
    s.append(P('Um hábito se forma com <b>gatilho → rotina → recompensa</b>, repetidos até se tornarem automáticos.'))
    s.append(FlowSteps([('Gatilho', 'ex.: terminar o jantar'), ('Rotina', 'ex.: 1 h de estudo na mesa'), ('Recompensa', 'ex.: marcar o dia, 1 episódio de série')], per_row=3, box_h=1.5 * cm, numbered=False))
    s.append(sp(8))
    s += bullets([
        'Associe o estudo a algo que você já faz todos os dias (ex.: depois do café da manhã).',
        'Facilite: deixe o material pronto na véspera.',
        'Dificulte as distrações: deslogue de redes sociais no computador de estudo.',
        'Tenha paciência: hábitos podem levar semanas ou meses para se consolidar, e isso varia de pessoa para pessoa.',
    ])
    s.append(H2('Como estabelecer metas realistas'))
    s += table(['Pergunta', 'Por que fazer'], [
        ['Quantas horas reais tenho por semana?', 'Evita planos impossíveis que geram frustração.'],
        ['O que é o mínimo aceitável por dia?', 'Garante a continuidade em dias ruins.'],
        ['Qual meta mensal de processo posso cumprir com folga?', 'Metas cumpridas aumentam a confiança.'],
        ['Como vou medir?', 'Sem medida, não há como ajustar.'],
    ], [7.0, 10.0], bold_first=True)
    s.append(CondPageBreak(8.5 * cm))
    s.append(H2('Meu compromisso'))
    s.append(FormGrid(['Item', 'Minha resposta'], [5.5, 11.5], 6, row_h=1.0 * cm, prefix='compromisso',
                      first_col=['Meu motivo principal', 'Horário fixo de estudo', 'Local de estudo', 'Horas por semana (meta)', 'Estudo mínimo diário', 'Recompensa semanal']))
    return s


def cap14():
    s = chapter(14, 'Planner semanal', 'Páginas preenchíveis para planejar e acompanhar cada semana')
    s.append(P('Use uma página por semana. Preencha no domingo (plano) e ao longo da semana (realizado). Os campos podem ser preenchidos no leitor de PDF ou à mão, após a impressão. Para mais semanas, imprima ou duplique o arquivo.'))
    s += box('dica', 'Sugestão: salve uma cópia do PDF com o nome da semana (ex.: “Planner_semana_05.pdf”) antes de preencher, para manter o histórico.')
    dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    for k in range(1, 5):
        s.append(PageBreak())
        s.append(H2('Planner semanal — semana %d' % k))
        s.append(FormGrid(['Semana de', 'Meta de horas', 'Meta de questões', 'Foco da semana'], [3.6, 3.0, 3.0, 7.4], 1, row_h=0.9 * cm, prefix='pw%dh' % k))
        s.append(sp(8))
        s.append(FormGrid(['Dia', 'Disciplina / assunto', 'Revisões do dia', 'Questões (feitas/acertos)', 'Horas', 'Feito?'],
                          [2.2, 5.4, 3.8, 2.6, 1.4, 1.6], 7, row_h=1.25 * cm, prefix='pw%d' % k,
                          first_col=dias, multiline_cols=(1, 2)))
        s.append(sp(8))
        s.append(FormGrid(['Revisões agendadas (assunto)', '24 h', '7 dias', '30 dias'], [7.4, 3.2, 3.2, 3.2], 4, row_h=0.75 * cm, prefix='pw%dr' % k))
        s.append(sp(8))
        s.append(FormGrid(['Balanço', 'Horas totais', 'Questões', '% acertos', 'Simulado'], [3.4, 3.4, 3.4, 3.4, 3.4], 1, row_h=0.85 * cm, prefix='pw%db' % k,
                          first_col=['Resultado']))
        s.append(sp(6))
        s.append(WriteLines(2, 'O que funcionou / o que vou ajustar na próxima semana:', prefix='pw%dn' % k, h=0.7 * cm))
    return s


def cap15():
    s = chapter(15, 'Checklist do candidato', 'Listas práticas para não esquecer nada')
    s.append(P('Toque nas caixas para marcar (no leitor de PDF) ou imprima e marque à mão.'))
    s.append(H2('Checklist de início da preparação'))
    s.append(CheckList([
        'Li a Apresentação e os Capítulos 1 a 4.',
        'Defini meu horário fixo e meu local de estudo.',
        'Escolhi o modelo de horário (1, 2 ou 3 horas por dia).',
        'Montei meu ciclo de estudos (Capítulo 6).',
        'Criei a estrutura de pastas e o caderno (mapa de disciplinas + caderno de erros).',
        'Separei uma fonte de teoria e uma de questões para cada disciplina.',
        'Salvei o texto oficial da Lei nº 13.022/2014 e da Constituição Federal.',
        'Ativei modo foco/não perturbe para o horário de estudo.',
        'Escolhi meu plano (30, 60 ou 90 dias) e preenchi o primeiro planner semanal.',
    ], prefix='ck_inicio'))
    s.append(H2('Checklist diário'))
    s.append(CheckList([
        'Fiz a revisão de 24 horas do assunto de ontem.',
        'Estudei a teoria prevista com leitura ativa.',
        'Fiz questões do assunto do dia.',
        'Registrei os erros relevantes no caderno de erros.',
        'Revisei os flashcards do dia.',
        'Anotei horas e questões no planner.',
        'Defini o que vou estudar amanhã.',
    ], prefix='ck_diario'))
    s.append(H2('Checklist semanal'))
    s.append(CheckList([
        'Fiz as revisões de 7 dias programadas.',
        'Revisei o caderno de erros da semana.',
        'Calculei o percentual de acertos por disciplina.',
        'Comparei horas planejadas e horas realizadas.',
        'Tirei pelo menos meio dia de descanso.',
        'Planejei a próxima semana no planner.',
        'Verifiquei as fontes oficiais sobre o concurso (Capítulo 16).',
    ], prefix='ck_semanal'))
    s.append(H2('Checklist mensal'))
    s.append(CheckList([
        'Fiz um simulado e analisei os resultados.',
        'Fiz as revisões de 30 dias.',
        'Reajustei o ciclo de estudos com base nos dados.',
        'Atualizei os resumos de 1 página das disciplinas.',
        'Fiz backup dos meus arquivos e anotações.',
    ], prefix='ck_mensal'))
    s.append(H2('Checklist de documentos e preparação geral'))
    s.append(P('Itens que costumam ser exigidos em algum momento de concursos públicos. Confira a lista exata no edital.', 'small'))
    s.append(CheckList([
        'Documento oficial de identidade com foto válido e CPF regular.',
        'Título de eleitor e comprovante de quitação eleitoral.',
        'Certificado de reservista ou documento de quitação militar (quando aplicável).',
        'Comprovante de escolaridade (certificado/histórico do ensino médio).',
        'Comprovante de residência atualizado.',
        'Certidões de antecedentes (sei onde emitir cada uma).',
        'E-mail que eu acesso com frequência, para cadastro na banca.',
        'Rotina de atividade física iniciada com orientação adequada (para possível TAF).',
        'Exames de saúde de rotina em dia (para possíveis exames médicos).',
    ], prefix='ck_docs'))
    s.append(H2('Checklist quando o edital for publicado'))
    s.append(CheckList([
        'Baixei o edital da fonte oficial (prefeitura e/ou banca) e salvei na pasta 00.',
        'Li o edital em três passadas (Capítulo 1).',
        'Anotei todas as datas no calendário com lembretes.',
        'Conferi se cumpro todos os requisitos do cargo.',
        'Verifiquei regras e prazos de isenção da taxa.',
        'Fiz a inscrição e guardei o comprovante.',
        'Paguei o boleto dentro do prazo e guardei o comprovante.',
        'Refiz o ciclo com disciplinas, número de questões e pesos oficiais.',
        'Comecei a acompanhar retificações e comunicados.',
    ], prefix='ck_edital'))
    s.append(H2('Checklist da véspera e do dia da prova'))
    s.append(CheckList([
        'Conferi local, horário de abertura e fechamento dos portões no cartão de confirmação.',
        'Fiz o trajeto antes ou calculei o tempo com folga.',
        'Separei documento com foto e caneta do tipo exigido no edital (geralmente esferográfica de tinta preta, em material transparente).',
        'Verifiquei os itens proibidos no local de prova.',
        'Dormi bem e fiz uma refeição leve.',
        'Levei água e lanche, se permitido.',
        'Defini minha ordem de resolução e o tempo para transcrever o gabarito.',
    ], prefix='ck_prova'))
    s.append(CondPageBreak(8.5 * cm))
    s.append(H2('Avaliação dos primeiros 30 dias'))
    s.append(FormGrid(['Pergunta', 'Resposta'], [7.0, 10.0], 6, row_h=1.0 * cm, prefix='aval30',
                      first_col=['Quantos dias estudei de 30?', 'Total de horas líquidas', 'Total de questões / % de acertos', 'Disciplina mais forte', 'Disciplina mais fraca', 'O que vou mudar no próximo mês']))
    return s


def cap16():
    s = chapter(16, 'Como acompanhar o edital', 'Fontes oficiais, publicações e como fugir de fake news')
    s.append(lead('Na fase pré-edital circulam muitos boatos: datas, número de vagas, salário, banca. Aprenda a separar informação oficial de especulação.'))
    s += box('fato', [
        'Situação na data de referência deste guia (novembro de 2026): nas buscas realizadas em fontes públicas, <b>não foi localizado edital publicado</b> para a Guarda Civil Municipal de Parnaíba (PI). Notícias recentes sobre concursos da Prefeitura de Parnaíba tratavam de outros cargos (por exemplo, a área da saúde). Isso pode mudar a qualquer momento — confirme sempre nas fontes oficiais.',
    ], 'SITUAÇÃO ATUAL')
    s.append(H2('Onde procurar informações oficiais'))
    s += table(['Fonte', 'O que encontrar', 'Endereço'], [
        ['Prefeitura Municipal de Parnaíba', 'Notícias oficiais, leis municipais, comunicados e acesso ao Diário Oficial do Município.', link('https://parnaiba.pi.gov.br', 'parnaiba.pi.gov.br')],
        ['Diário Oficial do Município de Parnaíba', 'Publicação dos atos oficiais: leis autorizando concursos, contratação de banca, edital, homologação e nomeações.', 'Acesse pelo site da prefeitura (seção “Diário Oficial”).'],
        ['Diário Oficial dos Municípios (APPM)', 'Publicações oficiais de municípios piauienses. Verifique se o ato que você procura foi publicado ali.', link('https://www.diarioficialdosmunicipios.org', 'diarioficialdosmunicipios.org')],
        ['Site da banca organizadora', 'Edital, inscrições, cartão de confirmação, gabaritos, recursos e resultados.', 'Será conhecido quando a banca for contratada e anunciada oficialmente.'],
        ['Planalto (legislação federal)', 'Texto oficial e atualizado da Constituição e da Lei nº 13.022/2014.', link(L13022, 'Lei 13.022/2014') + ' · ' + link(CF88, 'Constituição')],
        ['IBGE Cidades', 'Dados oficiais sobre o município, úteis para conhecimentos locais.', link('https://www.ibge.gov.br/cidades-e-estados/pi/parnaiba.html', 'ibge.gov.br — Parnaíba')],
    ], [4.0, 7.2, 5.8], bold_first=True)
    s.append(P('Endereços conferidos em novembro de 2026. Sites oficiais podem mudar de estrutura; em caso de link quebrado, procure pelo nome do órgão em um buscador e confira se o domínio termina em <b>.gov.br</b> (órgãos públicos) ou se é o domínio oficial da banca.', 'small'))
    s.append(H2('Sinais de que um concurso está se aproximando'))
    s += table(['Sinal', 'Onde aparece', 'O que significa'], [
        ['Lei criando/ampliando cargos ou autorizando concurso', 'Diário Oficial do Município; site da prefeitura/câmara.', 'Base legal para o concurso.'],
        ['Comissão do concurso nomeada', 'Diário Oficial (portaria/decreto).', 'Organização interna começou.'],
        ['Contratação da banca', 'Diário Oficial; portal de licitações/contratações.', 'Sinal forte: edital costuma vir depois.'],
        ['Edital publicado', 'Diário Oficial e site da banca.', 'Início oficial do concurso.'],
    ], [5.4, 6.0, 5.6], bold_first=True)
    s.append(H2('Como evitar fake news'))
    s += box('atencao', [
        '<b>Cuidado com nomes parecidos:</b> existe o município de <b>Santana de Parnaíba</b>, no estado de <b>São Paulo</b>, que também tem Guarda Civil Municipal e já realizou concursos para o cargo. Notícias, editais e vídeos sobre “GCM Parnaíba” podem se referir à cidade paulista. Sempre confira se o texto fala de <b>Parnaíba – PI</b>.',
    ], 'ARMADILHA REAL')
    s += table(['Sinal de alerta', 'Por que desconfiar'], [
        ['“Edital confirmado!” sem link para documento oficial', 'Informação oficial tem número de ato e data de publicação.'],
        ['Data de prova ou salário divulgados antes do edital', 'Esses dados só são oficiais no edital.'],
        ['Pedido de pagamento para “garantir vaga” ou “pré-inscrição”', 'Inscrição só ocorre pelo canal oficial indicado no edital. Isso pode ser golpe.'],
        ['Links encurtados ou sites com domínio estranho', 'Podem ser páginas falsas para roubar dados.'],
        ['Prints de conversas e áudios “de alguém da prefeitura”', 'Não são fontes oficiais.'],
        ['Notícia sem data ou de anos anteriores', 'Pode ser antiga e fora de contexto.'],
    ], [7.0, 10.0], bold_first=True)
    s.append(H2('Como confirmar uma informação em 4 passos'))
    s += numbered([
        '<b>Identifique a fonte:</b> quem publicou? É órgão oficial, banca ou veículo de imprensa identificado?',
        '<b>Procure o documento:</b> há número de lei, decreto, portaria ou edital e a data de publicação?',
        '<b>Confira no meio oficial:</b> busque o ato no Diário Oficial ou no site da prefeitura/banca.',
        '<b>Verifique a cidade e o ano:</b> é Parnaíba (PI)? A informação é atual?',
    ])
    s += box('recom', 'Reserve 10 minutos por semana (por exemplo, no domingo, ao planejar a semana) para verificar as fontes oficiais. Isso evita a ansiedade de checar notícias o tempo todo e mantém você informado.')
    return s


VIDEOS = [
    ('Como ler um edital (Capítulo 1)', 'COMO LER EDITAL DE CONCURSO PÚBLICO? Evandro Guedes - AlfaCon', 'AlfaCon', 'JNwyFx3IEQM',
     'Complementa a leitura em três passadas do edital e o glossário de termos.'),
    ('Ciclo de estudos e revisões (Capítulos 6 e 10)', 'Ciclo de estudo e revisões: Qual a MELHOR forma de organizar os estudos', 'Prof Diogo Moreira', 'f28JZBxOAL4',
     'Outra explicação sobre como organizar ciclo e revisões, útil para comparar com o método do guia.'),
    ('Memória, recuperação ativa e revisão espaçada (Capítulo 5)', 'Como se lembrar de TUDO QUE VOCÊ ESTUDA | Seja Um ESTUDANTE Melhor', 'SejaUmaPessoaMelhor', 'zY_Y3VK5jK0',
     'Aprofunda os métodos de recuperação ativa, repetição espaçada e flashcards.'),
    ('Caderno de erros (Capítulo 12)', 'Como fazer um CADERNO DE ERROS para CONCURSOS PÚBLICOS', 'Felipe Graton - Brabo Concursos', 'U_SrJrnw2JE',
     'Mostra outra forma de montar e revisar o caderno de erros.'),
    ('Interpretação de questões (Capítulo 11)', 'Interpretação de Textos para Concursos: 7 Dicas p/ nunca mais errar questões (comprovado)', 'Mateus Andrade - O Brabo dos Concursos', '-bTMKe6B-sc',
     'Reforça o roteiro de leitura de enunciados e textos.'),
    ('Procrastinação (Capítulo 13)', 'Como parar de PROCRASTINAR?', 'Ciência Todo Dia', 'WIS3PzNJEdU',
     'Explica, em linguagem de divulgação científica, por que procrastinamos e como agir.'),
    ('Lei nº 13.022/2014 (Capítulo 2 e planos)', 'Estatuto Geral das Guardas Municipais Atualizado 2026 | Lei 13.022/2014', 'Monster Concursos', 'uB0oN1Qqv7M',
     'Apoio à leitura da lei. Estude sempre também o texto oficial no site do Planalto.'),
]


def cap17():
    s = chapter(17, 'Recursos complementares', 'Vídeos gratuitos opcionais para aprofundar temas')
    s.append(P('Os vídeos abaixo são <b>opcionais</b>. Todo o conteúdo necessário para usar este guia está nas páginas anteriores. Eles servem apenas para quem quiser ver outra explicação de um tema. Os links foram conferidos em novembro de 2026; vídeos podem ser removidos ou alterados pelos canais a qualquer momento.'))
    s += box('atencao', 'Os vídeos são de canais independentes, sem vínculo com este guia. Opiniões e métodos apresentados neles são de responsabilidade dos autores. Se algo contradisser o edital ou a lei oficial, prevalecem o edital e a lei.')
    rows = []
    for tema, titulo, canal, vid, desc in VIDEOS:
        url = 'https://www.youtube.com/watch?v=%s' % vid
        rows.append(['<b>%s</b>' % tema, '%s<br/><font color="#5B6573">Canal: %s</font><br/>%s' % (titulo, canal, link(url, 'Abrir vídeo')), desc])
    s += table(['Tema complementado', 'Vídeo (título, canal e link)', 'Como ajuda'], rows, [4.0, 7.5, 5.5])
    s.append(H2('Outras fontes gratuitas e confiáveis'))
    s += table(['Recurso', 'Para quê', 'Link'], [
        ['Planalto — Legislação', 'Texto oficial de leis federais e da Constituição.', link('https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm', 'planalto.gov.br')],
        ['IBGE Cidades — Parnaíba', 'Dados oficiais do município.', link('https://www.ibge.gov.br/cidades-e-estados/pi/parnaiba.html', 'ibge.gov.br')],
        ['Anki (aplicativo de flashcards)', 'Revisão espaçada automática; gratuito no computador, na web e no Android.', link('https://apps.ankiweb.net', 'apps.ankiweb.net')],
    ], [4.5, 7.5, 5.0], bold_first=True)
    s.append(H2('Referências utilizadas'))
    refs = [
        'BRASIL. Constituição da República Federativa do Brasil de 1988 (arts. 37 e 144). Disponível em: ' + link(CF88, 'planalto.gov.br') + '.',
        'BRASIL. Lei nº 13.022, de 8 de agosto de 2014. Dispõe sobre o Estatuto Geral das Guardas Municipais. Disponível em: ' + link(L13022, 'planalto.gov.br') + '.',
        'DUNLOSKY, J. et al. Improving Students’ Learning With Effective Learning Techniques. <i>Psychological Science in the Public Interest</i>, v. 14, n. 1, p. 4–58, 2013.',
        'ROEDIGER, H. L.; KARPICKE, J. D. Test-Enhanced Learning: Taking Memory Tests Improves Long-Term Retention. <i>Psychological Science</i>, v. 17, n. 3, p. 249–255, 2006.',
        'CEPEDA, N. J. et al. Distributed practice in verbal recall tasks: A review and quantitative synthesis. <i>Psychological Bulletin</i>, v. 132, n. 3, p. 354–380, 2006.',
        'GOLLWITZER, P. M. Implementation intentions: Strong effects of simple plans. <i>American Psychologist</i>, v. 54, n. 7, p. 493–503, 1999.',
    ]
    for r in refs:
        s.append(P(r, ParagraphStyle('ref', parent=ST['bodyL'], fontSize=9.8, leading=13.5, leftIndent=12, firstLineIndent=-12)))
    return s


def conclusao():
    s = chapter('', 'Conclusão', 'O próximo passo é seu')
    s.append(lead('Você chegou ao fim do guia — mas este é, na verdade, o começo da sua preparação.'))
    s.append(P('Ao longo destas páginas, você aprendeu como funciona um concurso, o que é preparação pré-edital, como organizar o tempo, quais métodos de estudo funcionam, como montar um ciclo, como revisar, como resolver questões e como transformar erros em aprendizado. Você também recebeu planos de 30, 60 e 90 dias, um planner semanal, checklists e um caderno de erros.'))
    s.append(P('Nada disso substitui a parte mais importante: <b>sentar e estudar, hoje e amanhã de novo</b>. Não existe atalho, e ninguém pode garantir aprovação. O que existe é um caminho que aumenta suas chances: estudar com método, de forma constante, revisando e praticando, e ajustando a rota quando o edital for publicado.'))
    s.append(H2('Seus próximos 7 dias'))
    s.append(CheckList([
        'Hoje: definir horário e local de estudo e preencher “Meu compromisso” (Capítulo 13).',
        'Amanhã: montar o ciclo de estudos (Capítulo 6) e a estrutura de pastas.',
        'Dia 3: começar o Plano de 30 Dias (Capítulo 7).',
        'Dia 4 a 6: seguir o plano, com revisão de 24 horas e questões.',
        'Dia 7: preencher o planner da próxima semana e comemorar a primeira semana concluída.',
    ], prefix='prox7'))
    s.append(sp(8))
    s += box('recom', [
        'Haverá dias bons e dias ruins. Nos ruins, faça o mínimo. Nos bons, siga o plano. Quando cair, recomece sem culpa. Quando o edital sair, leia com atenção, ajuste o ciclo e siga em frente.',
        'Constância vence intensidade. Um passo por dia, todos os dias.',
    ], 'PARA LEVAR COM VOCÊ')
    s.append(sp(14))
    s.append(P('Bons estudos e boa preparação.', 'quote'))
    s.append(P('<b>Operação GCM PHB</b> · Preparação pré-edital 2027', 'center'))
    s.append(sp(18))
    s.append(P('Material educacional independente, sem vínculo com a Prefeitura Municipal de Parnaíba, com a Guarda Civil Municipal ou com bancas organizadoras. As informações sobre legislação e fontes foram conferidas em novembro de 2026. O edital oficial, quando publicado, prevalece sobre qualquer orientação deste guia.', 'small'))
    return s
