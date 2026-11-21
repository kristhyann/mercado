# -*- coding: utf-8 -*-
"""Conteúdo do Operação TAF GCM PHB 2027."""
from motor import *
import visuais as V
from visuais import Figura, linha_figuras, EscalaEsforco, SemanaTipo, Escada, GraficoProgressao, ORANGE

OMS = 'https://www.who.int/publications/i/item/9789240015128'
OMS_FS = 'https://www.who.int/news-room/fact-sheets/detail/physical-activity'
GUIA_MS = 'http://bvsms.saude.gov.br/bvs/publicacoes/guia_atividade_fisica_populacao_brasileira.pdf'
OPAS = 'https://www.paho.org/pt/noticias/30-6-2021-ministerio-da-saude-do-brasil-lanca-guia-atividade-fisica-para-populacao'
PARQ = 'https://eparmedx.com/'


# ======================================================================= páginas iniciais
def ficha():
    s = [Spacer(1, 1.0 * cm)]
    s.append(P('<font size="20" color="#0E2238"><b>Operação TAF GCM PHB</b></font>', 'bodyL'))
    s.append(sp(6))
    s.append(P('Preparação física progressiva para candidatos à Guarda Municipal — edição 2027.', 'lead'))
    s.append(sp(6))
    s += table(None, [
        ['Natureza', 'Guia de preparação física geral para iniciantes, com avaliação inicial, fundamentos, corrida, fortalecimento, planos de 8 e 12 semanas e diário de treino.'],
        ['Público', 'Candidatos que desejam melhorar o condicionamento antes de um possível teste de aptidão física (TAF), principalmente quem está começando.'],
        ['O que NÃO é', 'Não é programa oficial, não reproduz testes ou índices de nenhum edital e não substitui avaliação médica ou acompanhamento de profissional de educação física.'],
        ['Data de referência', 'Novembro de 2026.'],
        ['Formato', 'PDF A4, sumário clicável, tabelas, ilustrações esquemáticas e páginas preenchíveis no leitor de PDF.'],
    ], [3.8, 13.2], bold_first=True)
    s += box('atencao', [
        '<b>Nenhum exercício, número de repetições, tempo ou distância deste guia é critério oficial da Guarda Civil Municipal de Parnaíba.</b> Os testes, os índices mínimos e as regras de execução só serão conhecidos com a publicação do edital.',
        'Antes de iniciar qualquer programa de exercícios, especialmente se você é sedentário, tem mais de 40 anos, possui alguma doença ou usa medicamentos contínuos, procure <b>avaliação médica</b>. Sempre que possível, treine com orientação de um <b>profissional de educação física</b>.',
        'Não há promessa de resultado: a resposta ao treino varia de pessoa para pessoa.',
    ], 'AVISO DE RESPONSABILIDADE')
    s += box('fato', [
        'As orientações gerais de volume e intensidade seguem as Diretrizes da Organização Mundial da Saúde sobre Atividade Física e Comportamento Sedentário (2020) e o Guia de Atividade Física para a População Brasileira (Ministério da Saúde, 2021). Para adultos, ambos recomendam ao menos 150 minutos semanais de atividade moderada (ou 75 minutos de vigorosa) e fortalecimento muscular em 2 ou mais dias por semana.',
    ], 'BASE DAS RECOMENDAÇÕES')
    return s


def sumario():
    s = [PageBreak()]
    s.append(P('<font size="22" color="#0E2238"><b>Sumário</b></font>', 'bodyL'))
    s.append(sp(4))
    s.append(P('Toque em um capítulo para ir direto a ele.', 'small'))
    s.append(sp(8))
    s.append(make_toc())
    return s


def apresentacao():
    s = chapter('', 'Apresentação', 'Começar cedo, evoluir aos poucos, chegar inteiro')
    s.append(lead('Concursos de guarda municipal frequentemente incluem um teste de aptidão física. Quem deixa para treinar só depois do edital costuma ter poucas semanas — e o corpo não se adapta com pressa. Este guia propõe o caminho inverso: começar agora, devagar e com segurança.'))
    s.append(H2('Para quem é este guia'))
    s += bullets([
        'Para quem está <b>sedentário</b> ou treina de forma irregular e quer começar do zero.',
        'Para quem <b>nunca correu</b> e precisa de um caminho seguro da caminhada até a corrida contínua.',
        'Para quem não consegue fazer flexões ou pranchas e precisa de <b>adaptações</b>.',
        'Para quem quer <b>organizar</b> o treino com planos semanais, registros e metas realistas.',
    ])
    s += box('atencao', 'Se você já treina regularmente, este guia pode servir como base de organização, mas provavelmente precisará de um plano mais avançado, de preferência elaborado por um profissional.')
    s.append(H2('Como usar o guia'))
    s += table(['Passo', 'O que fazer', 'Onde'], [
        ['1', 'Leia os cuidados e faça a triagem de segurança.', 'Apresentação e Cap. 2'],
        ['2', 'Registre sua avaliação inicial (sem testes máximos).', 'Cap. 2'],
        ['3', 'Entenda os fundamentos: esforço, progressão, recuperação, aquecimento.', 'Cap. 3'],
        ['4', 'Aprenda a técnica da corrida e dos exercícios.', 'Caps. 4 e 5'],
        ['5', 'Escolha o plano: 8 semanas (já caminha 30 min com conforto) ou 12 semanas (evolução mais gradual).', 'Caps. 6 e 7'],
        ['6', 'Registre cada treino e reavalie a cada 4 semanas.', 'Caps. 8, 11 e 12'],
    ], [1.4, 11.4, 4.2], bold_first=True)
    s.append(H2('Por que começar antecipadamente'))
    s += bullets([
        'Ossos, tendões e articulações se adaptam <b>mais devagar</b> que o fôlego. Aumentar a carga rápido demais é uma causa comum de dores e lesões.',
        'Com tempo, você pode evoluir com <b>pequenos aumentos semanais</b> e incluir semanas mais leves para assimilação.',
        'Quando o edital sair, você poderá focar nos <b>testes específicos</b> exigidos, em vez de começar do zero.',
        'Interrupções (doença, trabalho, viagem) acontecem; quem começa cedo tem margem para retomar sem pressa.',
    ])
    s.append(H2('Como acompanhar a evolução'))
    s.append(P('Você vai acompanhar três tipos de indicadores: <b>volume</b> (minutos, distância, repetições), <b>esforço percebido</b> (escala de 0 a 10) e <b>sensação geral</b> (sono, dores, disposição). A cada 4 semanas, repita a avaliação inicial nas mesmas condições e compare.'))
    s.append(H2('Cuidados essenciais'))
    s += box_bullets('atencao', [
        '<b>Pare imediatamente</b> e procure atendimento se sentir dor ou aperto no peito, falta de ar desproporcional ao esforço, tontura, desmaio, palpitações irregulares, náusea intensa ou confusão. Em emergência, ligue <b>192 (SAMU)</b>.',
        '<b>Não treine com dor importante</b> (dor que piora durante o exercício, faz mancar, altera o movimento ou persiste no dia seguinte). Procure um profissional de saúde.',
        '<b>Não faça testes máximos sozinho.</b> Testes até a exaustão devem ser feitos apenas com avaliação prévia e supervisão.',
        '<b>Calor:</b> em cidades quentes, como Parnaíba, prefira treinar no início da manhã ou no fim da tarde, use roupas leves, protetor solar e beba água antes, durante (em treinos longos) e depois.',
        '<b>Doença aguda:</b> com febre, gripe forte ou infecção, não treine. Retome de forma leve após a recuperação.',
    ], 'SEGURANÇA EM PRIMEIRO LUGAR')
    return s


def cap_taf():
    s = chapter(1, 'Entendendo o TAF', 'O que é, por que existe e como se preparar')
    s.append(H2('O que é o TAF'))
    s.append(P('O Teste de Aptidão Física (TAF) é uma etapa que alguns concursos utilizam para verificar se o candidato tem condicionamento compatível com as atividades do cargo. Em geral, ele tem caráter <b>eliminatório</b> e é composto por provas com índices mínimos definidos no edital, que podem variar por sexo e faixa etária.'))
    s.append(H2('Por que concursos podem exigir aptidão física'))
    s.append(P('Cargos de segurança envolvem patrulhamento a pé, permanência prolongada em pé, deslocamentos rápidos, uso de equipamentos e situações de esforço físico. A Lei nº 13.022/2014 (Estatuto Geral das Guardas Municipais) inclui a <b>aptidão física, mental e psicológica</b> entre os requisitos básicos para investidura no cargo de guarda municipal (art. 10, VI). A forma de avaliar essa aptidão é definida em cada concurso.'))
    s.append(H2('Provas que costumam aparecer em TAFs (exemplos, não oficiais)'))
    s.append(P('A tabela abaixo mostra provas <b>frequentemente</b> encontradas em editais de guardas municipais e outras carreiras de segurança. <b>Não significa que serão exigidas em Parnaíba</b>, nem nos formatos descritos.'))
    s += table(['Prova (exemplo)', 'O que costuma avaliar', 'Como este guia ajuda'], [
        ['Corrida de tempo fixo (ex.: 12 minutos) ou de distância fixa', 'Resistência cardiorrespiratória', 'Progressão caminhada → trote → corrida contínua (Caps. 4, 6 e 7).'],
        ['Flexão de braço', 'Resistência muscular de membros superiores e tronco', 'Progressão parede → bancada → joelhos → tradicional (Cap. 5).'],
        ['Abdominal (diversas modalidades)', 'Resistência do core', 'Prancha, abdominal parcial, dead bug (Cap. 5).'],
        ['Barra fixa (dinâmica ou isométrica)', 'Força de membros superiores', 'Base geral com remada; a barra exige orientação específica.'],
        ['Corrida de velocidade / agilidade', 'Velocidade e mudança de direção', 'Base de condicionamento; treino específico deve vir após o edital.'],
        ['Salto horizontal ou vertical', 'Potência de membros inferiores', 'Base com agachamento e afundo; saltos só após adaptação.'],
        ['Natação', 'Habilidade aquática e resistência', 'Não abordada; exige local seguro e orientação.'],
    ], [4.6, 4.6, 7.8], bold_first=True)
    s.append(H2('Como acompanhar os critérios oficiais'))
    s += numbered([
        'Quando o edital for publicado, leia com atenção a seção do TAF: provas, ordem, tempos, índices mínimos, número de tentativas, vestimenta e regras de execução.',
        'Observe se o TAF é eliminatório, classificatório ou ambos, e se há exigência de atestado médico.',
        'Verifique detalhes técnicos: posição inicial da flexão, contagem do abdominal, tipo de pista, horário provável.',
        'Ajuste seu treino para as provas exigidas, mantendo a progressão gradual.',
        'Desconfie de “índices” divulgados antes do edital: eles não têm valor oficial.',
    ])
    s.append(H2('Como se preparar desde já'))
    s.append(SemanaTipo([('BASE', 'Condicionamento cardiovascular', V.TEAL), ('FORÇA', 'Resistência muscular', ORANGE),
                         ('MOBILIDADE', 'Amplitude e controle', V.GREEN), ('RECUPERAÇÃO', 'Sono, descanso, alimentação', GREY)]))
    s.append(sp(8))
    s.append(P('Antes do edital, o objetivo é construir uma <b>base física geral</b>: fôlego para correr de forma contínua, força para executar flexões, agachamentos e exercícios de tronco com boa técnica, e mobilidade para se movimentar sem limitações. Depois do edital, essa base será direcionada para as provas específicas.'))
    s += box('recom', 'Considere, quando possível, uma avaliação física com profissional de educação física e uma consulta médica (inclusive com avaliação cardiológica, se indicada). Muitos editais exigem atestado médico para o TAF.')
    return s


def cap_avaliacao():
    s = chapter(2, 'Avaliação inicial', 'Registrar o ponto de partida — sem testes máximos')
    s.append(lead('A avaliação inicial serve para saber de onde você parte e para medir a evolução. Ela é feita em ritmo confortável e com limites de segurança. Não é um teste para “ver até onde aguenta”.'))
    s.append(H2('Passo 1 — Triagem de segurança'))
    s.append(P('Responda com sinceridade. As perguntas abaixo são inspiradas em questionários de prontidão para atividade física (como o PAR-Q+). <b>Se responder “sim” a qualquer uma, procure avaliação médica antes de iniciar o programa.</b>'))
    s.append(CheckList([
        'Algum médico já disse que você tem problema no coração ou pressão alta?',
        'Você sente dor no peito em repouso, nas atividades do dia a dia ou ao fazer esforço?',
        'Você já perdeu o equilíbrio por tontura ou perdeu a consciência nos últimos 12 meses?',
        'Você tem alguma doença crônica (diabetes, doença respiratória, renal, entre outras) diagnosticada?',
        'Você usa medicamentos contínuos para alguma condição de saúde?',
        'Você tem problema em ossos, articulações ou coluna que possa piorar com exercícios?',
        'Você passou por cirurgia ou lesão importante recentemente, ou está gestante?',
        'Algum profissional de saúde já recomendou que você só faça exercícios com supervisão?',
    ], prefix='triagem'))
    s.append(sp(4))
    s += box('fato', 'O PAR-Q+ é um questionário internacional de prontidão para atividade física. A versão oficial está disponível em ' + link(PARQ, 'eparmedx.com') + '. As perguntas acima são uma adaptação simplificada e não substituem o questionário oficial nem a avaliação médica.')
    s.append(H2('Passo 2 — Como fazer os registros'))
    s += table(['Registro', 'Como fazer (com segurança)', 'Limite de segurança'], [
        ['Frequência cardíaca de repouso', 'Ao acordar, sentado, conte os batimentos no pulso ou pescoço por 30 segundos e multiplique por 2.', 'Apenas observar; valores muito altos ou irregulares: consulte um médico.'],
        ['Caminhada de 12 minutos', 'Em local plano e seguro, caminhe 12 minutos em ritmo <b>confortável e firme</b>. Anote a distância (ou voltas) e o esforço (0 a 10).', 'Esforço até 5. Não é corrida nem teste máximo.'],
        ['Trote contínuo confortável', 'Somente se a caminhada foi tranquila e a triagem não teve “sim”. Trote leve e anote quanto tempo consegue manter <b>conversando</b>.', 'Pare aos 10 minutos ou se o esforço passar de 6.'],
        ['Agachamento', 'Conte quantas repetições faz com boa técnica, em ritmo controlado.', 'Pare em 20 ou quando a técnica piorar.'],
        ['Flexão de braço', 'Escolha o nível em que consegue executar bem (parede, bancada, joelhos ou tradicional) e conte as repetições.', 'Pare 2 repetições antes de não conseguir mais.'],
        ['Prancha', 'Prancha nos antebraços (joelhos ou pés). Anote o tempo mantendo o corpo alinhado.', 'Pare em 60 s ou quando o quadril cair ou subir.'],
        ['Ponte de glúteo', 'Conte repetições com subida e descida controladas.', 'Pare em 20.'],
    ], [3.6, 8.6, 4.8], bold_first=True)
    s += box('dica', 'Faça os registros num dia descansado, após aquecimento de 5 a 10 minutos (Cap. 3). Repita nas semanas 4, 8 e 12 no mesmo local, horário e condições, para que a comparação seja justa.')
    s.append(H2('Passo 3 — Mobilidade (observação simples)'))
    s += table(['Teste simples', 'Como observar', 'Classificação'], [
        ['Agachamento profundo', 'Pés na largura dos ombros, desça o máximo confortável com calcanhares no chão.', 'Completo / parcial / com dificuldade'],
        ['Alcance sentado', 'Sentado com pernas estendidas, leve as mãos em direção aos pés sem forçar.', 'Passa dos pés / encosta / não alcança'],
        ['Mãos nas costas', 'Uma mão por cima do ombro e outra por baixo, tentando aproximá-las nas costas.', 'Encostam / até 10 cm / mais de 10 cm'],
        ['Tornozelo na parede', 'De frente para a parede, pé à frente, leve o joelho até a parede sem tirar o calcanhar do chão. Meça a distância do dedão à parede.', 'Distância em cm (cada lado)'],
    ], [3.6, 8.8, 4.6], bold_first=True)
    s.append(CondPageBreak(12 * cm))
    s.append(H2('Ficha de avaliação (preencha nas semanas 0, 4, 8 e 12)'))
    s.append(FormGrid(['Registro', 'Semana 0', 'Semana 4', 'Semana 8', 'Semana 12'], [5.4, 2.9, 2.9, 2.9, 2.9], 13, row_h=0.82 * cm, prefix='aval',
                      first_col=['Data', 'FC de repouso (bpm)', 'Caminhada 12 min (m/voltas)', 'Esforço da caminhada (0–10)', 'Trote confortável (min)',
                                 'Agachamentos (reps)', 'Flexão: nível e reps', 'Prancha: tipo e tempo (s)', 'Ponte de glúteo (reps)',
                                 'Agachamento profundo', 'Alcance sentado', 'Mãos nas costas (D/E)', 'Tornozelo na parede (D/E, cm)']))
    return s


def cap_fundamentos():
    s = chapter(3, 'Fundamentos do treinamento', 'Os princípios que tornam o treino seguro e eficiente')
    s.append(H2('Condicionamento cardiovascular'))
    s.append(P('É a capacidade do coração, dos pulmões e dos músculos de sustentar esforços contínuos, como caminhar rápido, correr ou pedalar. Melhora com atividades aeróbias repetidas ao longo das semanas, principalmente em intensidade leve a moderada, com aumentos graduais.'))
    s.append(H2('Resistência muscular e fortalecimento'))
    s.append(P('<b>Resistência muscular</b> é a capacidade de repetir um movimento muitas vezes (como flexões e abdominais). <b>Fortalecimento</b> é o aumento da força dos músculos. Para iniciantes, exercícios com o peso do corpo, em 2 ou 3 séries de 8 a 15 repetições, com técnica controlada, desenvolvem ambas as capacidades.'))
    s.append(H2('Mobilidade'))
    s.append(P('É a capacidade de mover as articulações com amplitude e controle. Boa mobilidade de tornozelos, quadris, coluna torácica e ombros ajuda a executar agachamentos, flexões e a correr com mais eficiência.'))
    s.append(H2('Intensidade: como controlar o esforço'))
    s.append(EscalaEsforco())
    s.append(sp(6))
    s += table(['Tipo de treino', 'Esforço-alvo (0 a 10)', 'Teste da fala'], [
        ['Caminhada / aquecimento', '2 a 4', 'Conversa normal, sem esforço.'],
        ['Trote e corrida leve (maior parte do treino)', '4 a 6', 'Consegue falar frases curtas.'],
        ['Fortalecimento', '5 a 7', 'Termina a série sentindo que ainda faria 2 ou 3 repetições.'],
        ['Esforço forte (raramente, e só após semanas de base)', '7 a 8', 'Fala poucas palavras.'],
    ], [6.2, 4.0, 6.8], bold_first=True)
    s += box('fato', 'O “teste da fala” e a escala de esforço de 0 a 10 são formas simples de monitorar a intensidade recomendadas pelo Guia de Atividade Física para a População Brasileira: em atividades moderadas é possível conversar, mas não cantar; em vigorosas, a fala fica difícil.')
    s.append(H2('Progressão'))
    s.append(P('Progredir é aumentar a exigência <b>aos poucos</b>, dando tempo para o corpo se adaptar. Aumente uma variável de cada vez:'))
    s += table(['Variável', 'Exemplo de progressão'], [
        ['Duração', 'De 1 minuto para 1 minuto e 30 segundos de trote em cada bloco.'],
        ['Repetições', 'De 2 × 8 para 2 × 10 agachamentos.'],
        ['Séries', 'De 2 para 3 séries.'],
        ['Dificuldade do exercício', 'Da flexão na parede para a flexão na bancada.'],
        ['Frequência', 'De 2 para 3 sessões de corrida por semana.'],
    ], [4.2, 12.8], bold_first=True)
    s += box('recom', 'Uma referência prática usada por treinadores é não aumentar o volume semanal total muito mais que cerca de 10% de uma semana para outra e incluir, a cada 3 ou 4 semanas, uma semana mais leve (“assimilação”). Trata-se de uma orientação de bom senso, não de uma regra científica rígida: se o corpo der sinais de cansaço excessivo, mantenha ou reduza.')
    s.append(H2('Recuperação e descanso'))
    s.append(P('O condicionamento melhora <b>durante a recuperação</b>, e não apenas durante o treino. Sem descanso, o cansaço se acumula e o risco de lesão aumenta.'))
    s += bullets([
        '<b>Sono:</b> para adultos, geralmente se recomendam de 7 a 9 horas por noite.',
        '<b>Dias de descanso:</b> pelo menos 1 a 2 dias por semana sem treino intenso.',
        '<b>Intervalo entre treinos de força:</b> cerca de 48 horas para o mesmo grupo muscular.',
        '<b>Alimentação e hidratação:</b> refeições equilibradas e água ao longo do dia. Para orientação individual, procure um nutricionista.',
        '<b>Sinais de recuperação insuficiente:</b> cansaço persistente, sono ruim, dores que não passam, desânimo, queda de desempenho.',
    ])
    s.append(H2('Aquecimento'))
    s.append(P('Prepara músculos, articulações e o sistema cardiovascular. Leva de 5 a 10 minutos e deve ser feito antes de todos os treinos.'))
    s += table(['Etapa', 'O que fazer', 'Tempo'], [
        ['1. Ativação geral', 'Caminhada progressiva (de lenta a firme).', '3–5 min'],
        ['2. Mobilidade dinâmica', 'Círculos de braços, rotação de quadril, flexão e extensão de tornozelos, elevação de joelhos caminhando.', '2–3 min'],
        ['3. Específico', 'Antes de correr: 2 ou 3 trechos curtos de trote bem leve. Antes da força: 1 série fácil de cada exercício.', '1–2 min'],
    ], [3.8, 10.4, 2.8], bold_first=True)
    s.append(H2('Volta à calma'))
    s.append(P('Ao terminar, caminhe de 3 a 5 minutos até a respiração se normalizar. Alongamentos leves e estáticos podem ser feitos nesse momento, sem dor.'))
    return s


def cap_corrida():
    s = chapter(4, 'Corrida para iniciantes', 'Da caminhada à corrida contínua, sem pressa')
    s.append(H2('Como começar'))
    s += bullets([
        '<b>Calçado:</b> tênis confortável, com amortecimento e bem ajustado. Não precisa ser caro.',
        '<b>Local:</b> prefira terrenos planos e regulares (pistas, calçadões, parques). Evite trânsito intenso e horários de calor forte.',
        '<b>Frequência:</b> 3 sessões por semana, em dias alternados, são suficientes no início.',
        '<b>Objetivo inicial:</b> conseguir caminhar 30 minutos com conforto; depois, alternar caminhada e trote.',
    ])
    s.append(H2('Como caminhar'))
    s += numbered([
        'Postura ereta, olhar à frente, ombros relaxados.',
        'Braços dobrados em cerca de 90°, balançando ao lado do corpo, em oposição às pernas.',
        'Passadas naturais: o calcanhar toca o solo e o pé “rola” até a ponta.',
        'Ritmo firme, em que você consegue conversar (esforço 3 a 4).',
    ])
    s.append(H2('Como alternar caminhada e corrida'))
    s.append(P('O método de <b>intervalos</b> intercala trechos curtos de trote leve com caminhada para recuperação. Com o tempo, os trechos de trote aumentam e os de caminhada diminuem, até a corrida contínua.'))
    s.append(FlowSteps([('Caminhada', '20–30 min confortáveis'), ('Intervalos curtos', '30 s a 1 min de trote'),
                        ('Intervalos médios', '2 a 4 min de trote'), ('Intervalos longos', '5 a 10 min de trote'),
                        ('Contínuo', '15 a 20 min leves')], per_row=5, box_h=1.55 * cm))
    s.append(sp(8))
    s.append(H2('Técnica básica da corrida'))
    s += table(['Ponto', 'Orientação'], [
        ['Passada', 'Passos curtos e leves. Evite “esticar” a perna à frente do corpo.'],
        ['Contato com o solo', 'Pise abaixo do corpo, de forma suave. Não force pisar com a ponta ou com o calcanhar: a pisada natural se ajusta com a prática.'],
        ['Tronco', 'Levemente inclinado à frente, a partir dos tornozelos, sem curvar as costas.'],
        ['Braços', 'Relaxados, cotovelos dobrados, movimento para frente e para trás (não cruzando o corpo).'],
        ['Respiração', 'Pelo nariz e pela boca, de forma natural. Se não conseguir falar frases curtas, diminua o ritmo.'],
    ], [3.6, 13.4], bold_first=True)
    s.append(H2('Como evoluir'))
    s += bullets([
        'Só avance para a etapa seguinte quando a atual estiver <b>confortável</b> (esforço até 6) por pelo menos 2 sessões.',
        'Se uma semana foi difícil, <b>repita a semana</b>. Repetir não é fracasso: é respeitar a adaptação.',
        'Aumente primeiro a <b>duração</b> do trote; a velocidade virá naturalmente com o tempo.',
        'Inclua uma semana mais leve a cada 3 ou 4 semanas.',
    ])
    s.append(H2('Como controlar o esforço'))
    s.append(P('Use a escala de 0 a 10 e o teste da fala (Cap. 3). Na maior parte do tempo, o trote deve ser <b>leve a moderado (4 a 6)</b>: você consegue falar frases curtas. Se precisar parar para respirar, o ritmo estava forte demais — caminhe e reduza a velocidade no próximo trecho.'))
    s.append(H2('Sinais de alerta'))
    s += table(['Sinal', 'O que fazer'], [
        ['Dor ou aperto no peito, falta de ar desproporcional, tontura, desmaio, palpitações irregulares', '<b>Pare imediatamente</b> e procure atendimento médico. Em emergência, ligue 192.'],
        ['Dor localizada que piora durante a corrida, faz mancar ou altera a passada', 'Pare o treino. Se persistir no dia seguinte, procure um profissional de saúde.'],
        ['Dor na canela, no joelho ou no pé que aparece sempre no início dos treinos', 'Reduza o volume e procure avaliação; pode ser sobrecarga.'],
        ['Cãibras, sede intensa, dor de cabeça, náusea no calor', 'Pare, vá para a sombra, hidrate-se. Se não melhorar, procure atendimento.'],
        ['Cansaço que não passa, sono ruim, desânimo por vários dias', 'Faça uma semana mais leve ou descanse alguns dias.'],
    ], [7.4, 9.6], bold_first=True)
    s += box('dica', 'Leve água em treinos acima de 30–40 minutos ou em dias quentes, e use roupas claras e leves.')
    return s


def exercicio(nome, pose_list, execucao, erros, mais_facil, mais_dificil, cuidados, quando=None):
    s = [H2(nome)]
    s += linha_figuras(pose_list)
    if quando:
        s.append(P(quando, 'bodyL'))
    s.append(H3('Execução'))
    s += numbered(execucao)
    data = [
        [Paragraph('<b>Erros comuns</b>', ST['cellB']), Paragraph('<b>Adaptações</b>', ST['cellB']), Paragraph('<b>Cuidados</b>', ST['cellB'])],
        [[Paragraph('• ' + e, ST['cell']) for e in erros],
         [Paragraph('<b>Mais fácil:</b> ' + mais_facil, ST['cell']), Spacer(1, 3), Paragraph('<b>Mais difícil:</b> ' + mais_dificil, ST['cell'])],
         [Paragraph('• ' + c_, ST['cell']) for c_ in cuidados]],
    ]
    t = NoSplitTable(data, colWidths=[5.6 * cm, 5.8 * cm, 5.6 * cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), RED_L), ('BACKGROUND', (1, 0), (1, 0), TEAL_L), ('BACKGROUND', (2, 0), (2, 0), GOLD_L),
        ('GRID', (0, 0), (-1, -1), 0.5, LINE), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    s += [t]
    bloco = NoSplitTable([[s]], colWidths=[FW])
    bloco.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                               ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
    return [bloco, Spacer(1, 14)]


def cap_fortalecimento():
    s = chapter(5, 'Fortalecimento', 'Exercícios básicos com o peso do corpo, execução e adaptações')
    s.append(P('Todos os exercícios podem ser feitos em casa, sem equipamentos (alguns usam cadeira, mesa firme ou mochila). As ilustrações são <b>esquemáticas</b>: mostram a posição geral do corpo. Leia sempre a descrição da execução.'))
    s += box('atencao', 'Execute em ritmo controlado (cerca de 2 segundos para descer e 1 a 2 segundos para subir), sem prender a respiração: solte o ar na fase de maior esforço. Nenhum exercício deve causar dor articular. Se doer, pare e procure orientação.')
    s += exercicio('Agachamento',
        [('agachamento_cadeira', 'Nível 1: sentar e levantar'), ('agachamento', 'Nível 2: agachamento livre')],
        ['Pés na largura dos ombros, pontas levemente voltadas para fora.', 'Leve o quadril para trás e para baixo, como quem vai sentar.',
         'Mantenha o peito aberto, as costas neutras e os calcanhares no chão.', 'Desça até onde conseguir manter a técnica (coxas paralelas ao chão é uma boa referência).',
         'Empurre o chão com o pé inteiro e suba até ficar em pé.'],
        ['Joelhos caindo para dentro.', 'Calcanhares saindo do chão.', 'Costas arredondadas.', 'Descer rápido demais, “despencando”.'],
        'Sentar e levantar de uma cadeira firme, encostando levemente o quadril no assento.',
        'Pausa de 2 segundos embaixo; mais repetições; depois, afundo estático.',
        ['Joelhos na direção das pontas dos pés.', 'Amplitude sem dor: não force a profundidade.', 'Use cadeira estável, encostada na parede.'])
    s.append(H2('Progressão da flexão de braço'))
    s.append(Escada(['Flexão na parede', 'Flexão na bancada ou mesa firme', 'Flexão com joelhos no chão', 'Flexão tradicional'], cor=V.TEAL))
    s.append(sp(8))
    s += exercicio('Flexão adaptada (parede, bancada e joelhos)',
        [('flexao_parede', 'Parede'), ('flexao_joelhos', 'Joelhos no chão')],
        ['Mãos um pouco mais afastadas que a largura dos ombros, na altura do peito.', 'Corpo alinhado da cabeça aos joelhos (ou aos pés), abdômen firme.',
         'Dobre os cotovelos, levando o peito em direção ao apoio; cotovelos a cerca de 45° do tronco.', 'Empurre o apoio até estender os braços, sem travar os cotovelos com força.'],
        ['Quadril caindo ou empinado.', 'Cabeça projetada à frente.', 'Cotovelos muito abertos (em “T”).', 'Amplitude muito curta.'],
        'Quanto mais alto o apoio das mãos (parede > mesa > banco), mais fácil.',
        'Diminua a altura do apoio até o chão; depois, passe para a flexão tradicional.',
        ['Apoio firme e que não deslize.', 'Use um colchonete sob os joelhos.', 'Punhos doloridos: apoie em halteres ou nos punhos fechados, ou reduza o volume.'],
        quando='Use a flexão adaptada até conseguir fazer pelo menos 3 séries de 12 a 15 repetições com boa técnica no nível atual.')
    s += exercicio('Flexão tradicional (quando adequada)',
        [('flexao', 'Flexão tradicional')],
        ['Mãos no chão, um pouco além da largura dos ombros; pés juntos ou levemente afastados.', 'Corpo em linha reta dos calcanhares à cabeça; abdômen e glúteos contraídos.',
         'Desça de forma controlada até o peito ficar próximo ao chão.', 'Empurre o chão até estender os braços, mantendo o alinhamento.'],
        ['“Minhoca”: o quadril sobe depois do peito.', 'Lombar arqueada.', 'Descer apenas alguns centímetros.', 'Respiração presa.'],
        'Volte para joelhos no chão nas últimas repetições de cada série.',
        'Mais repetições; pausa de 1 segundo embaixo; descida mais lenta (3 segundos).',
        ['Comece somente quando dominar a flexão com joelhos.', 'Qualidade antes de quantidade.', 'Em TAFs, a forma de execução é definida no edital.'])
    s += exercicio('Prancha',
        [('prancha_joelhos', 'Prancha com joelhos'), ('prancha', 'Prancha tradicional')],
        ['Apoie os antebraços no chão, cotovelos abaixo dos ombros.', 'Estenda as pernas (ou mantenha os joelhos apoiados).',
         'Contraia abdômen e glúteos, alinhando cabeça, tronco e quadril.', 'Respire normalmente e mantenha a posição pelo tempo indicado.'],
        ['Quadril caído (lombar afundada).', 'Quadril muito alto.', 'Prender a respiração.', 'Manter a posição com a técnica já perdida.'],
        'Joelhos no chão; tempo menor (10–15 s).',
        'Aumente o tempo aos poucos (até 45–60 s) ou alterne toques de ombro mantendo o quadril parado.',
        ['Pare quando o alinhamento se perder.', 'Dor lombar: volte para a versão com joelhos ou procure orientação.'])
    s += exercicio('Prancha lateral',
        [('prancha_lateral', 'Prancha lateral')],
        ['Deite de lado, antebraço apoiado com o cotovelo abaixo do ombro.', 'Joelhos dobrados (versão adaptada) ou pernas estendidas.',
         'Eleve o quadril até o corpo formar uma linha reta.', 'Mantenha o tempo indicado e troque de lado.'],
        ['Quadril caindo.', 'Ombro “afundando”, sem apoio ativo.', 'Tronco girando para frente ou para trás.'],
        'Joelhos dobrados no chão.', 'Pernas estendidas e, depois, braço livre estendido para o alto.',
        ['Dor no ombro: reduza o tempo ou faça a versão com joelhos.', 'Trabalhe os dois lados igualmente.'])
    s += exercicio('Ponte de glúteo',
        [('ponte', 'Ponte de glúteo')],
        ['Deite de costas, joelhos dobrados, pés apoiados no chão na largura do quadril.', 'Braços ao lado do corpo.',
         'Contraia os glúteos e eleve o quadril até alinhar joelhos, quadril e ombros.', 'Segure 1 a 2 segundos e desça devagar.'],
        ['Arquear a lombar no topo.', 'Empurrar com as pontas dos pés.', 'Joelhos abrindo ou fechando.'],
        'Menor amplitude de subida.', 'Pausa de 3 segundos no topo; depois, ponte com uma perna (apenas após dominar a versão básica).',
        ['O esforço deve ser sentido nos glúteos e posteriores da coxa, não na lombar.'])
    s += exercicio('Exercícios de core: perdigueiro e dead bug',
        [('perdigueiro', 'Perdigueiro'), ('dead_bug', 'Dead bug')],
        ['<b>Perdigueiro:</b> em quatro apoios (mãos abaixo dos ombros, joelhos abaixo do quadril), estenda um braço à frente e a perna oposta para trás, sem girar o quadril. Volte e troque.',
         '<b>Dead bug:</b> deitado de costas, braços para o alto e joelhos dobrados a 90°. Estenda um braço para trás e a perna oposta à frente, mantendo a lombar encostada no chão. Volte e troque.',
         'Movimentos lentos, respiração contínua.'],
        ['Girar o quadril (perdigueiro).', 'Lombar desgrudando do chão (dead bug).', 'Pressa: o objetivo é controle.'],
        'Mova só os braços ou só as pernas.', 'Pausa de 2 a 3 segundos na posição estendida.',
        ['Movimento sem dor.', 'Ótimos para aprender a estabilizar o tronco antes de abdominais mais intensos.'])
    s += exercicio('Abdominal parcial',
        [('abdominal_parcial', 'Abdominal parcial')],
        ['Deite de costas, joelhos dobrados, pés no chão.', 'Mãos nas coxas ou cruzadas no peito.',
         'Contraia o abdômen e eleve a cabeça e as escápulas do chão, deslizando as mãos em direção aos joelhos.', 'Desça de forma controlada.'],
        ['Puxar o pescoço com as mãos.', 'Subir com impulso.', 'Tirar a lombar totalmente do chão no início do aprendizado.'],
        'Menor amplitude; mãos apoiadas nas coxas.', 'Mais repetições; descida mais lenta.',
        ['Desconforto no pescoço: apoie a cabeça nas mãos sem puxá-la.', 'Em TAFs, a modalidade de abdominal é definida no edital.'])
    s += exercicio('Afundo estático',
        [('afundo', 'Afundo estático')],
        ['Dê um passo largo à frente, com os pés afastados na largura do quadril.', 'Desça o joelho de trás em direção ao chão, mantendo o tronco ereto.',
         'O joelho da frente acompanha a direção do pé.', 'Suba empurrando o chão com o pé da frente. Faça todas as repetições e troque de perna.'],
        ['Passo curto demais.', 'Joelho da frente caindo para dentro.', 'Tronco inclinado demais.'],
        'Segure em uma parede ou cadeira para equilíbrio; menor amplitude.', 'Mais repetições; depois, afundo alternado caminhando.',
        ['Joelho de trás não deve bater no chão.', 'Dor no joelho: reduza a amplitude ou volte ao agachamento.'])
    s += exercicio('Remada com mochila',
        [('remada', 'Remada curvada com mochila')],
        ['Coloque alguns livros em uma mochila resistente (comece com pouco peso).', 'Pés na largura do quadril, joelhos levemente dobrados, incline o tronco à frente com as costas retas.',
         'Segure a mochila com os braços estendidos e puxe-a em direção ao abdômen, aproximando as escápulas.', 'Desça de forma controlada.'],
        ['Arredondar as costas.', 'Puxar com impulso do tronco.', 'Peso excessivo.'],
        'Faça com uma mão, apoiando a outra em uma cadeira.', 'Aumente o peso aos poucos ou use elástico de treino.',
        ['Lombar sensível: faça a versão com apoio.', 'Se o edital exigir barra fixa, procure orientação para um treino específico.'])
    s.append(CondPageBreak(9 * cm))
    s.append(H2('Rotina de mobilidade (8 a 10 minutos)'))
    s.append(P('Faça depois dos treinos ou em dias de descanso. Movimentos lentos, sem dor, respirando normalmente.'))
    s += table(['Movimento', 'Como fazer', 'Dose'], [
        ['Tornozelo na parede', 'De frente para a parede, leve o joelho à frente sem tirar o calcanhar do chão.', '10 vezes cada lado'],
        ['Agachamento sustentado', 'Desça no agachamento profundo segurando em algo firme e permaneça respirando.', '3 × 20 s'],
        ['Abertura de quadril', 'Em afundo com joelho de trás no chão, leve o quadril levemente à frente.', '2 × 20 s cada lado'],
        ['Gato e camelo', 'Em quatro apoios, arredonde e estenda a coluna devagar.', '10 vezes'],
        ['Rotação torácica', 'Em quatro apoios, mão na nuca, gire o tronco abrindo o cotovelo para o teto.', '8 vezes cada lado'],
        ['Círculos de ombros e braços', 'Círculos amplos para frente e para trás.', '10 vezes cada sentido'],
        ['Alongamento de posterior', 'Em pé, calcanhar apoiado em um degrau, incline o tronco com as costas retas.', '2 × 20 s cada lado'],
    ], [4.2, 9.8, 3.0], bold_first=True)
    return s


# ======================================================================= planos
SEMANA8 = [('SEG', 'Corrida', V.TEAL), ('TER', 'Força A + mobilidade', ORANGE), ('QUA', 'Corrida', V.TEAL), ('QUI', 'Força B + mobilidade', ORANGE),
           ('SEX', 'Descanso ou caminhada leve', GREY), ('SÁB', 'Sessão longa leve', V.TEAL), ('DOM', 'Descanso', GREY)]

FORCA_A = 'Agachamento · Flexão (seu nível) · Ponte de glúteo · Prancha · Perdigueiro'
FORCA_B = 'Afundo estático (ou agachamento) · Remada com mochila · Prancha lateral · Dead bug · Abdominal parcial'

P8 = [
    # (corrida, min de corrida, sessão longa, séries×reps, prancha, nota)
    ("8 × (1' trote + 2' caminhada)", 8, "Caminhada ativa contínua de 30–35'", '2 × 8', '2 × 15–20 s', 'Adaptação: foco em técnica e regularidade.'),
    ("7 × (1'30\" trote + 2' caminhada)", 10.5, "Caminhada ativa contínua de 35'", '2 × 10', '2 × 20 s', 'Aumento pequeno do trote.'),
    ("6 × (2' trote + 2' caminhada)", 12, "10' caminhada + 4 × (2' trote + 3' caminhada) + 5' caminhada", '2 × 12', '2 × 25 s', 'Se a semana 2 foi difícil, repita-a.'),
    ("5 × (2' trote + 2' caminhada)", 10, "Caminhada ativa de 30' + reavaliação (Cap. 2), sem esforço máximo", '2 × 10', '2 × 20 s', 'ASSIMILAÇÃO: semana mais leve.'),
    ("5 × (3' trote + 2' caminhada)", 15, "6 × (2' trote + 2' caminhada)", '3 × 10', '3 × 25 s', 'Passagem para 3 séries. Se o trote de 3 minutos ficar pesado, faça 6 × (2\'30" trote + 2\' caminhada) nesta semana.'),
    ("4 × (4' trote + 2' caminhada)", 16, "5 × (3' trote + 2' caminhada)", '3 × 12', '3 × 30 s', 'Trote sempre em ritmo de conversa.'),
    ("3 × (6' trote + 2' caminhada)", 18, "3 × (5' trote + 2' caminhada) + 10' caminhada", '3 × 12–15', '3 × 35 s', 'Considere avançar o nível da flexão.'),
    ("2 × (10' trote + 2' caminhada)", 20, "Reavaliação: 15–20' de trote contínuo leve, se confortável; se não, 3 × (6' + 2')", '3 × 10–12 (novo nível, se avançou)', '3 × 30–40 s', 'Fechamento do ciclo e reavaliação.'),
]


LATERAL8 = ['2 × 10–15 s', '2 × 15 s', '2 × 20 s', '2 × 15 s', '2 × 20 s', '3 × 20 s', '3 × 25 s', '3 × 25–30 s']


def cap_plano8():
    s = chapter(6, 'Plano de 8 semanas', 'Para quem já caminha 30 minutos com conforto')
    s.append(P('<b>Pré-requisitos:</b> triagem de segurança sem respostas “sim” (ou liberação médica) e capacidade de caminhar 30 minutos sem desconforto. Se ainda não é o seu caso, comece pelo Plano de 12 semanas.'))
    s.append(H2('Estrutura semanal'))
    s.append(SemanaTipo(SEMANA8))
    s.append(sp(8))
    s += table(['Componente', 'Como fazer', 'Intensidade', 'Recuperação'], [
        ['Corrida (seg e qua)', "5' de caminhada de aquecimento + bloco da semana + 5' de caminhada de volta à calma.", 'Trote 4–6; caminhada 3–4', 'Pelo menos 1 dia entre sessões de corrida.'],
        ['Sessão longa leve (sáb)', 'Treino mais longo e tranquilo, indicado em cada semana.', '3–5', 'Domingo de descanso.'],
        ['Força A e B (ter e qui)', "Aquecimento de 5' + 5 exercícios em circuito ou por séries + 8–10' de mobilidade.", '5–7 (2–3 repetições na reserva)', "60–90 s entre séries; 48 h entre sessões."],
        ['Sexta-feira', "Descanso ou caminhada leve de 20–30'.", '2–3', '—'],
    ], [3.4, 6.6, 3.4, 3.6], bold_first=True, fs=9)
    s += table(['Treino', 'Exercícios'], [['Força A', FORCA_A], ['Força B', FORCA_B]], [3.0, 14.0], bold_first=True)
    s.append(GraficoProgressao([w[1] for w in P8], 'Minutos de trote por sessão de corrida (seg/qua) — semana 4 é de assimilação', destaque=(4,)))
    s.append(sp(6))
    for i, (cor, mins, longo, series, prancha, nota) in enumerate(P8, 1):
        s.append(CondPageBreak(9 * cm))
        s.append(H2('Semana %d%s' % (i, ' — assimilação' if i == 4 else '')))
        s += table(['Dia', 'Treino', 'Conteúdo', 'Duração', 'Esforço'], [
            ['Seg', 'Corrida', "5' caminhada + %s + 5' caminhada" % cor, "≈ 30–35'", '4–6'],
            ['Ter', 'Força A', '%s — %s séries/reps; prancha %s' % (FORCA_A, series, prancha), "≈ 35–40'", '5–7'],
            ['Qua', 'Corrida', "5' caminhada + %s + 5' caminhada" % cor, "≈ 30–35'", '4–6'],
            ['Qui', 'Força B', '%s — %s séries/reps; prancha lateral %s cada lado' % (FORCA_B, series, LATERAL8[i - 1]), "≈ 35–40'", '5–7'],
            ['Sex', 'Descanso ativo', "Descanso ou caminhada leve de 20–30'", "0–30'", '2–3'],
            ['Sáb', 'Longo leve', longo, "≈ 30–40'", '3–5'],
            ['Dom', 'Descanso', 'Descanso completo', '—', '—'],
        ], [1.3, 2.4, 9.3, 2.0, 2.0], bold_first=True, fs=8.8)
        s.append(P('<b>Progressão / observação:</b> %s' % nota, 'small'))
    s.append(H2('Critérios para avançar ou repetir'))
    s += table(['Situação', 'Decisão'], [
        ['Completou todos os treinos com esforço dentro do alvo e sem dores', 'Avance para a próxima semana.'],
        ['Precisou parar várias vezes ou o esforço passou de 7', 'Repita a semana.'],
        ['Dor que piora com o treino ou persiste no dia seguinte', 'Interrompa, descanse e procure um profissional de saúde.'],
        ['Faltou a 2 ou mais treinos na semana', 'Repita a semana.'],
        ['Ficou mais de 2 semanas parado', 'Volte 2 semanas no plano (veja o Cap. 10).'],
    ], [9.0, 8.0], bold_first=True)
    return s


P12_CARDIO = [
    ("Caminhada contínua de 20' em ritmo confortável", 0, "Caminhada de 20–25'"),
    ("Caminhada contínua de 25'", 0, "Caminhada de 25–30'"),
    ("Caminhada de 30' com 4 trechos de 2' em ritmo mais firme", 0, "Caminhada de 30'"),
    ("Caminhada de 30' (assimilação)", 0, "Caminhada de 30' + reavaliação (Cap. 2), sem esforço máximo"),
    ("5' caminhada + 6 × (30\" trote + 2'30\" caminhada) + 5' caminhada", 3, "Caminhada de 30–35'"),
    ("5' caminhada + 7 × (1' trote + 2' caminhada) + 5' caminhada", 7, "6 × (1' trote + 2' caminhada)"),
    ("5' caminhada + 7 × (1'30\" trote + 2' caminhada) + 5' caminhada", 10.5, "8 × (1' trote + 2' caminhada)"),
    ("5' caminhada + 6 × (1'30\" trote + 2' caminhada) + 5' caminhada (assimilação)", 9, "Caminhada de 30' + reavaliação, sem esforço máximo"),
    ("5' caminhada + 6 × (2' trote + 2' caminhada) + 5' caminhada", 12, "5 × (2' trote + 2' caminhada)"),
    ("5' caminhada + 5 × (3' trote + 2' caminhada) + 5' caminhada", 15, "6 × (2' trote + 2' caminhada)"),
    ("5' caminhada + 4 × (4' trote + 2' caminhada) + 5' caminhada", 16, "4 × (3' trote + 2' caminhada)"),
    ("5' caminhada + 3 × (5' trote + 2' caminhada) + 5' caminhada", 15, "Reavaliação: 3 × (6' trote + 2' caminhada) ou 12–15' de trote contínuo leve, se confortável"),
]

NIVEIS = {
    1: ('Nível 1', 'Sentar e levantar da cadeira · Flexão na parede · Ponte de glúteo · Prancha com joelhos · Perdigueiro (só braços ou só pernas)'),
    2: ('Nível 2', 'Agachamento livre (amplitude confortável) · Flexão na bancada/mesa firme · Ponte de glúteo · Prancha com joelhos ou tradicional curta · Perdigueiro completo · Dead bug'),
    3: ('Nível 3', 'Agachamento livre · Flexão com joelhos (ou tradicional, se adequada) · Afundo estático · Prancha tradicional · Prancha lateral · Abdominal parcial · Remada com mochila'),
}
SERIES12 = ['2 × 8', '2 × 10', '2 × 12', '2 × 10', '2 × 10', '2 × 12', '3 × 10', '2 × 12', '3 × 10', '3 × 12', '3 × 12–15', '3 × 10–12']
PRANCHA12 = ['2 × 10 s', '2 × 15 s', '2 × 20 s', '2 × 15 s', '2 × 20 s', '2 × 25 s', '3 × 25 s', '2 × 25 s', '3 × 25 s', '3 × 30 s', '3 × 35 s', '3 × 30–40 s']


def cap_plano12():
    s = chapter(7, 'Plano de 12 semanas', 'Evolução mais gradual: começando pela caminhada')
    s.append(P('Indicado para quem está sedentário, retorna após longo período parado, tem sobrepeso ou sente que precisa de mais tempo de adaptação. O plano tem três fases de 4 semanas, cada uma terminando com uma semana mais leve e uma reavaliação.'))
    s.append(FlowSteps([('Fase 1 · S1–S4', 'Caminhada e força nível 1'), ('Fase 2 · S5–S8', 'Primeiros trotes e nível 2'),
                        ('Fase 3 · S9–S12', 'Intervalos maiores e nível 3')], per_row=3, box_h=1.5 * cm, numbered=False))
    s.append(sp(8))
    s.append(H2('Estrutura semanal'))
    s.append(SemanaTipo([('SEG', 'Caminhada / corrida', V.TEAL), ('TER', 'Força + mobilidade', ORANGE), ('QUA', 'Caminhada / corrida', V.TEAL),
                         ('QUI', 'Mobilidade ou descanso', V.GREEN), ('SEX', 'Força + mobilidade', ORANGE), ('SÁB', 'Sessão leve', V.TEAL), ('DOM', 'Descanso', GREY)]))
    s.append(sp(8))
    s += table(['Nível de força', 'Semanas', 'Exercícios'], [[NIVEIS[k][0], ('1–4', '5–8', '9–12')[k - 1], NIVEIS[k][1]] for k in (1, 2, 3)],
               [2.8, 2.0, 12.2], bold_first=True)
    s.append(GraficoProgressao([w[1] if w[1] else 0.0001 for w in P12_CARDIO], 'Minutos de trote por sessão (seg/qua) — semanas 1 a 4 só caminhada; 4 e 8 são de assimilação', destaque=(4, 8)))
    s.append(sp(6))
    for i, (cardio, mins, sab) in enumerate(P12_CARDIO, 1):
        nivel = 1 if i <= 4 else (2 if i <= 8 else 3)
        s.append(CondPageBreak(8.5 * cm))
        s.append(H2('Semana %d%s' % (i, ' — assimilação' if i in (4, 8) else '')))
        s += table(['Dia', 'Treino', 'Conteúdo', 'Duração', 'Esforço'], [
            ['Seg', 'Caminhada/corrida', cardio, "≈ 20–35'", '3–6'],
            ['Ter', 'Força (%s)' % NIVEIS[nivel][0], '%s séries/reps; prancha %s; + mobilidade' % (SERIES12[i - 1], PRANCHA12[i - 1]), "≈ 30–35'", '5–7'],
            ['Qua', 'Caminhada/corrida', cardio, "≈ 20–35'", '3–6'],
            ['Qui', 'Mobilidade', "Rotina de mobilidade (8–10') ou descanso", "0–10'", '2'],
            ['Sex', 'Força (%s)' % NIVEIS[nivel][0], '%s séries/reps; prancha %s; + mobilidade' % (SERIES12[i - 1], PRANCHA12[i - 1]), "≈ 30–35'", '5–7'],
            ['Sáb', 'Sessão leve', sab, "≈ 25–35'", '3–5'],
            ['Dom', 'Descanso', 'Descanso completo', '—', '—'],
        ], [1.3, 2.9, 8.8, 2.0, 2.0], bold_first=True, fs=8.8)
    s += box('recom', 'Ao concluir as 12 semanas, você pode continuar com as semanas 6 a 8 do Plano de 8 semanas, que trazem trotes mais longos, ou manter 2 a 3 sessões de corrida e 2 de força por semana até a publicação do edital.')
    return s


# ======================================================================= acompanhamento e demais capítulos
def cap_acompanhamento():
    s = chapter(8, 'Acompanhamento', 'Registre para enxergar sua evolução')
    s.append(P('Preencha uma linha por treino. No campo “Esforço”, use a escala de 0 a 10. Em “Observações”, anote sono, dores, clima ou qualquer fator importante. Os campos podem ser preenchidos no PDF ou impressos.'))
    s += table(['Coluna', 'Exemplo de preenchimento'], [
        ['Data', '12/03'], ['Treino', "Corrida S3 — 6 × (2' + 2')"], ['Duração', "34'"], ['Distância', '3,2 km (se souber; opcional)'],
        ['Repetições', 'Agachamento 2 × 12; flexão joelhos 2 × 10'], ['Esforço', '5'], ['Observações', 'Calor; leve cansaço nas panturrilhas.'],
    ], [3.4, 13.6], bold_first=True)
    hdr = ['Data', 'Treino', 'Duração', 'Distância', 'Repetições', 'Esforço (0–10)', 'Observações']
    w = [1.6, 3.4, 1.7, 1.8, 3.2, 1.7, 3.6]
    for i in range(1, 5):
        s.append(PageBreak())
        s.append(H2('Tabela de acompanhamento — página %d' % i))
        s.append(FormGrid(hdr, w, 20, row_h=0.95 * cm, prefix='acomp%d' % i))
    s.append(PageBreak())
    s.append(H2('Resumo mensal'))
    s.append(FormGrid(['Mês', 'Treinos feitos', 'Minutos de corrida', 'Melhor marca de flexões', 'Prancha (melhor tempo)', 'Observações'],
                      [1.8, 2.4, 2.8, 3.0, 3.0, 4.0], 4, row_h=1.1 * cm, prefix='mensal', first_col=['Mês 1', 'Mês 2', 'Mês 3', 'Mês 4']))
    return s


def cap_erros():
    s = chapter(9, 'Erros comuns', 'O que mais atrapalha iniciantes — e como evitar')
    erros = [
        ('Excesso de treinamento', 'Treinar todos os dias, com intensidade alta, sem semanas leves.', 'Cansaço constante, sono ruim, dores persistentes, queda de rendimento, irritabilidade.', 'Siga o plano, respeite os dias de descanso e as semanas de assimilação.'),
        ('Ignorar dores', 'Continuar treinando com dor que piora ou persiste.', 'Dor que altera o movimento, faz mancar ou dura mais de 2–3 dias.', 'Interrompa, reduza o volume e procure um profissional de saúde.'),
        ('Falta de descanso', 'Dormir pouco e não ter dias livres.', 'Sensação de “corpo pesado”, desmotivação.', 'Priorize o sono e mantenha 1 a 2 dias de descanso por semana.'),
        ('Começar muito forte', 'Correr rápido demais nos primeiros treinos.', 'Precisar parar logo no início; esforço acima de 7.', 'Comece pela caminhada e use o teste da fala.'),
        ('Não aquecer', 'Iniciar o treino “frio”.', 'Rigidez, desconforto nos primeiros minutos.', 'Faça 5 a 10 minutos de aquecimento sempre.'),
        ('Não respeitar a progressão', 'Pular semanas ou dobrar o volume por ansiedade.', 'Dores nas canelas, joelhos ou pés.', 'Avance só quando a semana atual estiver confortável.'),
        ('Comparar-se com outros', 'Seguir o ritmo de amigos mais treinados.', 'Frustração, lesões.', 'Compare-se apenas com você mesmo, usando seus registros.'),
        ('Treinar só o que gosta', 'Fazer apenas corrida (ou apenas força).', 'Desequilíbrio entre capacidades.', 'Mantenha corrida, força e mobilidade no plano.'),
    ]
    s += table(['Erro', 'Como acontece', 'Sinais', 'Como evitar'], [list(e) for e in erros], [3.2, 4.2, 4.6, 5.0], bold_first=True, fs=9.2)
    s += box('atencao', '“Sem dor, sem ganho” não é uma boa regra para iniciantes. Desconforto muscular leve e passageiro após treinos novos é comum; dor aguda, articular ou que piora com o movimento não é normal e deve ser avaliada.')
    return s


def cap_disciplina():
    s = chapter(10, 'Disciplina', 'Constância, motivação, metas e retomada')
    s.append(H2('Constância'))
    s += bullets([
        'Defina <b>dias e horários fixos</b> para treinar e trate-os como compromissos.',
        'Deixe roupa e tênis prontos na véspera.',
        'Tenha uma <b>versão mínima</b> do treino para dias difíceis (ex.: 20 minutos de caminhada + 1 série de cada exercício).',
        'Treinar acompanhado aumenta o compromisso.',
    ])
    s.append(H2('Motivação'))
    s.append(P('A motivação oscila. O que mantém o treino é o <b>hábito</b>. Marque cada treino concluído no checklist semanal e observe sua evolução nos registros: ver o progresso é uma das maiores fontes de motivação.'))
    s.append(H2('Metas'))
    s += table(['Tipo', 'Exemplo ruim', 'Exemplo bom'], [
        ['Processo (semanal)', '“Treinar bastante.”', '“Fazer os 5 treinos da semana 3.”'],
        ['Desempenho (4 semanas)', '“Ficar em forma.”', "“Trotar 10' sem parar em ritmo de conversa.”"],
        ['Longo prazo (12 semanas)', '“Passar no TAF.”', '“Fazer 3 × 12 flexões com joelhos e trotar 15–20 minutos contínuos.”'],
    ], [4.0, 4.6, 8.4], bold_first=True)
    s.append(H2('Como retomar após interrupções'))
    s += table(['Tempo parado', 'Como retomar'], [
        ['Até 1 semana', 'Repita a última semana concluída.'],
        ['1 a 2 semanas', 'Volte 1 semana no plano.'],
        ['2 a 4 semanas', 'Volte 2 semanas no plano.'],
        ['Mais de 4 semanas', 'Recomece pela semana 1 do plano mais adequado (provavelmente o de 12 semanas) e refaça a avaliação inicial.'],
        ['Após doença ou lesão', 'Retome somente com liberação, de forma leve, e reduza o volume pela metade na primeira semana.'],
    ], [4.0, 13.0], bold_first=True)
    s.append(H2('Meu compromisso'))
    s.append(FormGrid(['Item', 'Minha resposta'], [5.4, 11.6], 6, row_h=1.0 * cm, prefix='comp',
                      first_col=['Plano escolhido', 'Dias e horários de treino', 'Local de treino', 'Meta de 4 semanas', 'Meta de 12 semanas', 'Versão mínima do treino']))
    return s


def cap_checklist():
    s = chapter(11, 'Checklist semanal', 'Marque a cada semana — toque nas caixas no PDF ou imprima')
    for i in range(1, 5):
        if i > 1:
            s.append(CondPageBreak(12 * cm))
        s.append(H2('Semana nº ____ (folha %d)' % i))
        s.append(CheckList([
            'Fiz aquecimento antes de todos os treinos.',
            'Completei as sessões de corrida/caminhada previstas.',
            'Completei os treinos de força previstos.',
            'Fiz a rotina de mobilidade pelo menos 2 vezes.',
            'Mantive o esforço dentro do alvo (teste da fala).',
            'Respeitei os dias de descanso.',
            'Dormi bem na maior parte das noites.',
            'Bebi água ao longo do dia e nos treinos em dias quentes.',
            'Não treinei com dor importante.',
            'Registrei os treinos na tabela de acompanhamento.',
            'Decidi se vou avançar ou repetir a próxima semana.',
        ], prefix='chk%d' % i))
        s.append(sp(6))
    return s


def cap_diario():
    s = chapter(12, 'Diário de treino', 'Páginas preenchíveis para registrar sensações e aprendizados')
    s.append(P('Use o diário para registrar o que os números não mostram: disposição, sono, dores, clima, humor e aprendizados. Uma página serve para uma semana.'))
    dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    for i in range(1, 7):
        s.append(PageBreak())
        s.append(H2('Diário — semana ____ (página %d)' % i))
        s.append(FormGrid(['Dia', 'Treino realizado', 'Duração', 'Esforço', 'Sono (h)', 'Dores / observações'],
                          [2.2, 5.2, 1.8, 1.7, 1.7, 4.4], 7, row_h=1.35 * cm, prefix='diario%d' % i, first_col=dias, multiline_cols=(1, 5)))
        s.append(sp(8))
        s.append(WriteLines(3, 'O que funcionou bem nesta semana:', prefix='dfunc%d' % i, h=0.7 * cm))
        s.append(sp(4))
        s.append(WriteLines(3, 'O que vou ajustar na próxima semana:', prefix='dajus%d' % i, h=0.7 * cm))
    return s


VIDEOS = [
    ('Corrida para iniciantes', 'Corrida para iniciantes: como começar a correr?', 'Drauzio Varella', '5FJoqhlszTI'),
    ('Aquecimento para corrida', 'AQUECIMENTO EM 3 MINUTOS: evite lesões deixando seu corpo preparado para a corrida!', 'Corrida & Performance', '3PqzgxkgwAs'),
    ('Agachamento', 'COMO FAZER AGACHAMENTO - Passo a passo do agachamento perfeito', 'Tay Training', 'qrZs_1K1CFI'),
    ('Flexão de braço (progressões)', 'O melhor jeito de fazer FLEXÃO DE BRAÇO - Da iniciante a avançada', 'Tay Training', '9ozLIq3Nmkw'),
    ('Prancha', 'Como fazer a prancha abdominal corretamente', 'VOLL TV', 'Yu0wjtD5FkU'),
    ('Mobilidade', 'ALONGAMENTO DINÂMICO | Exercícios de Mobilidade para Prevenir DOR no Corpo | Aurélio Alfieri', 'Aurélio Alfieri', 'F1iejoRbRts'),
]


def cap_recursos():
    s = chapter(13, 'Recursos complementares', 'Vídeos gratuitos opcionais e fontes')
    s.append(P('Os vídeos são <b>opcionais</b>: todo o conteúdo necessário está neste guia. Eles podem ajudar a visualizar a execução de movimentos. Títulos, canais e links foram conferidos em novembro de 2026; os canais podem alterar ou remover vídeos.'))
    s += box('atencao', 'Os vídeos são de canais independentes, sem vínculo com este guia. Se alguma orientação divergir das recomendações de segurança deste material ou do seu médico, siga a opção mais conservadora e procure um profissional.')
    rows = [['<b>%s</b>' % tema, '%s<br/><font color="#5B6573">Canal: %s</font>' % (tit, canal), link('https://www.youtube.com/watch?v=' + vid, 'Abrir vídeo')]
            for tema, tit, canal, vid in VIDEOS]
    s += table(['Assunto', 'Título e canal', 'Link'], rows, [4.0, 10.0, 3.0])
    s.append(H2('Referências'))
    refs = [
        'ORGANIZAÇÃO MUNDIAL DA SAÚDE. <i>Diretrizes da OMS para atividade física e comportamento sedentário</i>. Genebra: OMS, 2020. ' + link(OMS, 'who.int') + ' · Ficha informativa: ' + link(OMS_FS, 'who.int') + '.',
        'BRASIL. Ministério da Saúde. <i>Guia de Atividade Física para a População Brasileira</i>. Brasília, 2021. ' + link(GUIA_MS, 'bvsms.saude.gov.br') + ' · Notícia do lançamento: ' + link(OPAS, 'paho.org') + '.',
        'PAR-Q+ — <i>Physical Activity Readiness Questionnaire for Everyone</i>. ' + link(PARQ, 'eparmedx.com') + '.',
        'BRASIL. Lei nº 13.022, de 8 de agosto de 2014 — Estatuto Geral das Guardas Municipais (art. 10, VI: aptidão física, mental e psicológica).',
    ]
    for r in refs:
        s.append(P(r, ParagraphStyle('ref', parent=ST['bodyL'], fontSize=9.8, leading=13.5, leftIndent=12, firstLineIndent=-12)))
    return s


def conclusao():
    s = chapter('', 'Conclusão', 'Continuidade e adaptação ao edital')
    s.append(lead('Condicionamento físico é construído com semanas e meses de treino regular. Se você seguiu um dos planos, já tem algo valioso: uma base e um método.'))
    s.append(H2('Depois dos planos'))
    s += bullets([
        'Mantenha <b>2 a 3 sessões de corrida</b> e <b>2 de fortalecimento</b> por semana, com mobilidade e descanso.',
        'Continue progredindo devagar: trotes mais longos, flexões em nível mais difícil, pranchas mais longas.',
        'Reavalie a cada 4 semanas e registre tudo.',
    ])
    s.append(H2('Quando o edital for publicado'))
    s += numbered([
        'Leia com atenção as provas do TAF, os índices mínimos, as regras de execução e as exigências de atestado médico.',
        'Compare as exigências com seus registros atuais e identifique as maiores diferenças.',
        'Ajuste o treino para as provas específicas, de preferência com orientação de um profissional de educação física.',
        'Treine a execução exatamente como o edital descreve (posição inicial, amplitude, contagem).',
        'Nas últimas semanas antes do teste, reduza o volume para chegar descansado.',
    ])
    s += box('recom', ['Treine com regularidade, respeite os sinais do corpo, evolua aos poucos e busque orientação profissional sempre que possível. Não há garantia de resultado, mas uma preparação antecipada, gradual e segura é o melhor caminho para chegar ao teste em boas condições.'], 'PARA LEVAR COM VOCÊ')
    s.append(sp(12))
    s.append(P('Bons treinos!', 'quote'))
    s.append(P('<b>Operação TAF GCM PHB</b> · 2027', 'center'))
    s.append(sp(14))
    s.append(P('Material independente de preparação física geral. Não apresenta critérios oficiais da Guarda Civil Municipal de Parnaíba e não substitui avaliação médica ou acompanhamento de profissional de educação física. Informações conferidas em novembro de 2026.', 'small'))
    return s
