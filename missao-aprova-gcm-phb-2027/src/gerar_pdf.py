# -*- coding: utf-8 -*-
"""Gera Missao_Aprova_GCM_PHB_2027.pdf.  Uso: python3 gerar_pdf.py"""
import os
import copy
from motor import *
import layout
from layout import (questao, lista_questoes, comentario, grade_gabarito, AnswerSheet)
from qbase import numerar, Texto
import q_port, q_info, q_mat, q_leg, q_local

AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(os.path.dirname(AQUI), 'Missao_Aprova_GCM_PHB_2027.pdf')

L13022 = 'https://www2.camara.leg.br/legin/fed/lei/2014/lei-13022-8-agosto-2014-779152-normaatualizada-pl.html'
CF88 = 'https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html'
PLANALTO_13022 = 'https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l13022.htm'
PLANALTO_13060 = 'https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l13060.htm'
IBGE_HIST = 'https://biblioteca.ibge.gov.br/visualizacao/dtb/piaui/parnaiba.pdf'

# ======================================================================= montagem dos bancos
def textos_de(itens):
    return {t.titulo: t for t in itens if isinstance(t, Texto)}


PORT_ALL = numerar(q_port.ITENS)
PORT = PORT_ALL[:100]
PORT_EX = PORT_ALL[100:] + numerar(q_port.EXTRAS)
TXT_PORT = textos_de(q_port.ITENS)

INFO_ALL = numerar(q_info.ITENS)
INFO, INFO_EX = INFO_ALL[:50], INFO_ALL[50:]

MAT_ALL = numerar(q_mat.ITENS)
MAT, MAT_EX = MAT_ALL[:50], MAT_ALL[50:]

LEG_ALL = numerar(q_leg.ITENS)
_base, _extra_fim = LEG_ALL[:117], LEG_ALL[117:]
_mover = {i for i in range(len(_base)) if i % 7 == 6} | {116}
LEG = [q for i, q in enumerate(_base) if i not in _mover]
LEG_EX = [q for i, q in enumerate(_base) if i in _mover] + _extra_fim

LOCAL = numerar(q_local.ITENS)

# renumera cada disciplina de 1..N
for banco in (PORT, INFO, MAT, LEG, LOCAL):
    for i, q in enumerate(banco, 1):
        q.num = i

assert len(PORT) == 100 and len(INFO) == 50 and len(MAT) == 50 and len(LEG) == 100 and len(LOCAL) == 20, \
    (len(PORT), len(INFO), len(MAT), len(LEG), len(LOCAL))


def dividir(lst, tamanhos):
    out, i = [], 0
    for t in tamanhos:
        out.append(lst[i:i + t])
        i += t
    return out


SP = dividir(PORT_EX, [11, 11, 11])
SI = dividir(INFO_EX, [5, 5, 5])
SM = dividir(MAT_EX, [8, 8, 9])
SL = dividir(LEG_EX, [16, 16, 15])
SIMULADOS = []
for k in range(3):
    qs = [copy.copy(q) for q in SP[k] + SI[k] + SM[k] + SL[k]]
    for i, q in enumerate(qs, 1):
        q.num = i
        q.texto = None
    SIMULADOS.append(qs)
assert all(len(s) == 40 for s in SIMULADOS)

DISC = [
    ('port', 'Língua Portuguesa', PORT, TXT_PORT),
    ('info', 'Noções de Informática', INFO, {}),
    ('mat', 'Matemática e Raciocínio Lógico', MAT, {}),
    ('leg', 'Constituição, Legislação e Conhecimentos Específicos', LEG, {}),
    ('local', 'Conhecimentos Locais de Parnaíba', LOCAL, {}),
]


# ======================================================================= páginas iniciais
def ficha():
    s = [Spacer(1, 1.0 * cm)]
    s.append(P('<font size="20" color="#0E2238"><b>Missão Aprova GCM PHB</b></font>', 'bodyL'))
    s.append(sp(6))
    s.append(P('Questões, simulados, revisão e estratégia para treinar seu desempenho — preparação para a Guarda Civil Municipal de Parnaíba (PI). Edição 2027.', 'lead'))
    s.append(sp(6))
    s += table(None, [
        ['Conteúdo', '320 questões originais de múltipla escolha (5 alternativas) com gabarito comentado, distribuídas em 5 disciplinas, e 3 simulados inéditos de 40 questões cada, com folha de respostas e gabarito separado.'],
        ['Público', 'Candidatos iniciantes e intermediários que se preparam para a Guarda Civil Municipal de Parnaíba (PI).'],
        ['Fase', 'Pré-edital. As disciplinas são referências de preparação e não correspondem, necessariamente, ao conteúdo programático oficial.'],
        ['Data de referência', 'Novembro de 2026. Textos legais conferidos na versão atualizada disponível nessa data.'],
        ['Formato', 'PDF A4 com sumário clicável, marcadores, folhas de respostas com bolhas clicáveis e páginas preenchíveis.'],
    ], [4.0, 13.0], bold_first=True)
    s += box('atencao', [
        'Este material é <b>independente</b> e <b>não oficial</b>. Não tem vínculo com a Prefeitura Municipal de Parnaíba, com a Guarda Civil Municipal ou com qualquer banca organizadora.',
        'Todas as questões foram <b>elaboradas especialmente para este material</b>. Nenhuma questão é oficial nem foi aplicada por banca, e nenhuma é atribuída a banca alguma. Os simulados <b>não reproduzem</b> a prova de Parnaíba.',
        'Nenhum material garante aprovação. Quando o edital for publicado, ele será a referência definitiva sobre disciplinas, conteúdos e etapas.',
    ], 'AVISO IMPORTANTE')
    s += box('fato', [
        'As questões de legislação foram elaboradas a partir do texto atualizado da Constituição Federal e da Lei nº 13.022/2014 disponível no portal de Legislação Informatizada da Câmara dos Deputados, além das Leis nº 13.060/2014, 8.069/1990, 10.741/2003 e 11.340/2006. As questões sobre Parnaíba usam como fonte principal o histórico do município publicado pelo IBGE e o Censo 2022.',
    ], 'FONTES')
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
    s = chapter('', 'Apresentação', 'Como transformar questões em desempenho')
    s.append(lead('Resolver questões é uma das formas mais eficientes de aprender e de medir o que você já sabe. Mas só funciona se cada erro virar estudo. Este material foi organizado para isso: praticar, corrigir, registrar e revisar.'))
    s.append(H2('O que você vai encontrar'))
    s += table(['Parte', 'Conteúdo', 'Quantidade'], [
        ['Método', 'Técnicas para ler enunciados, eliminar alternativas, evitar pegadinhas e controlar o tempo.', 'Capítulo 1'],
        ['Português', 'Interpretação, ortografia, acentuação, classes, verbos, pronomes, pontuação, concordância, regência, crase, sintaxe, coesão e coerência.', '100 questões'],
        ['Informática', 'Sistemas operacionais, arquivos, internet, navegadores, e-mail, segurança, hardware, software e produtividade.', '50 questões'],
        ['Matemática e RLM', 'Operações, frações, porcentagem, razão, proporção, regra de três, sequências, lógica, problemas, gráficos e tabelas.', '50 questões'],
        ['Legislação', 'Constituição, direitos fundamentais, administração pública, segurança pública, Lei nº 13.022/2014, Lei nº 13.060/2014, direitos humanos e cidadania.', '100 questões'],
        ['Parnaíba', 'História, geografia, cultura, patrimônio, economia e aspectos sociais.', '20 questões'],
        ['Gabaritos comentados', 'Resposta, explicação e erros comuns de cada questão, por disciplina.', '320 comentários'],
        ['Simulados', 'Três simulados inéditos, com instruções, tempo, folha de respostas e gabarito separado.', '3 × 40 questões'],
        ['Controle', 'Caderno de erros e tabelas de desempenho preenchíveis.', 'Capítulos 10 e 11'],
    ], [3.4, 10.6, 3.0], bold_first=True)
    s.append(H2('Como usar o material'))
    s += numbered([
        '<b>Leia o Capítulo 1</b> (método). Ele vale para todas as disciplinas.',
        '<b>Resolva por blocos:</b> 10 a 20 questões de uma disciplina por sessão, com tempo marcado.',
        '<b>Marque as respostas</b> na folha de respostas no fim de cada capítulo (no PDF, toque nas bolhas; no papel, pinte-as).',
        '<b>Corrija</b> no Capítulo 7 (gabaritos comentados). Leia a explicação de todas as questões, inclusive das que acertou.',
        '<b>Registre os erros</b> no caderno de erros (Capítulo 10) e os números no controle de desempenho (Capítulo 11).',
        '<b>Revise</b> os erros em 24 horas, 7 dias e 30 dias.',
        '<b>Faça os simulados</b> depois de completar pelo menos metade das questões de cada disciplina.',
    ])
    s.append(H2('Como resolver as questões'))
    s.append(P('Trate cada questão como na prova: leia o enunciado inteiro, identifique o comando, leia todas as alternativas e só então marque. Se não souber, elimine o que for absurdo e anote que “chutou”. Para estudar, um acerto no chute vale como erro.'))
    s.append(H2('Como registrar erros'))
    s.append(P('Para cada erro relevante, anote no caderno de erros: data, disciplina, assunto, número da questão, o que você marcou, o motivo (falta de conteúdo, interpretação, desatenção, cálculo ou chute), a regra correta e a data da próxima revisão.'))
    s.append(H2('Como revisar'))
    s += table(['Quando', 'O que fazer', 'Tempo'], [
        ['24 horas depois', 'Releia as correções do caderno de erros e refaça as questões erradas sem olhar o gabarito.', '10–15 min'],
        ['7 dias depois', 'Refaça novamente as questões erradas e resolva questões do mesmo assunto.', '15–20 min'],
        ['30 dias depois', 'Revise o caderno de erros completo da disciplina e faça um bloco misto de questões.', '20–30 min'],
    ], [3.5, 10.5, 3.0], bold_first=True)
    s.append(H2('Como acompanhar o desempenho'))
    s.append(P('Calcule o percentual de acertos: <b>acertos ÷ questões × 100</b>. Registre por disciplina e por data no Capítulo 11. Observe a <b>tendência</b> ao longo de várias semanas, não um resultado isolado.'))
    s += box('dica', 'Comece pelas questões da disciplina em que você se sente mais inseguro, mas alterne com uma disciplina que você domina. Acertar também motiva.')
    return s


def metodo():
    s = chapter(1, 'Método para resolver questões', 'Leitura, comando, eliminação, pegadinhas e tempo')
    s.append(lead('Muitos pontos se perdem não por falta de conhecimento, mas por leitura apressada, desatenção ou má gestão do tempo. Um método simples, repetido em todas as questões, reduz esses erros.'))
    s.append(FlowSteps([('Ler', 'enunciado completo'), ('Comando', 'o que se pede?'), ('Prever', 'resposta antes das opções'),
                        ('Eliminar', 'descartar erradas'), ('Conferir', 'releia o comando')], per_row=5, box_h=1.5 * cm))
    s.append(sp(10))
    s.append(H2('1. Leitura do enunciado'))
    s += bullets([
        'Leia o enunciado <b>inteiro</b> antes de olhar as alternativas.',
        'Em questões com texto, leia primeiro as perguntas sobre ele e depois o texto. Assim, você lê sabendo o que procurar.',
        'Sublinhe dados numéricos, nomes, prazos e palavras-chave.',
        'Em Matemática, anote os dados em uma lista: o que foi dado e o que se pede.',
    ])
    s.append(H2('2. Identificação do comando'))
    s += table(['Comando', 'O que exige', 'Armadilha'], [
        ['Assinale a correta', 'Uma alternativa verdadeira.', 'As erradas costumam ter um único detalhe trocado.'],
        ['Assinale a INCORRETA / EXCETO / NÃO', 'A alternativa falsa.', 'Marcar a primeira verdadeira por hábito.'],
        ['De acordo com o texto', 'O que o texto diz.', 'Usar opinião ou conhecimento externo.'],
        ['Infere-se / conclui-se', 'Conclusão lógica autorizada pelo texto.', 'Extrapolar além do texto.'],
        ['Segundo a Lei / a CF', 'O texto legal.', 'Trocas de “poderá” por “deverá”, números e prazos.'],
    ], [4.4, 5.2, 7.4], bold_first=True)
    s.append(H2('3. Eliminação de alternativas'))
    s.append(P('Raramente é preciso ter certeza absoluta da resposta. Basta eliminar as alternativas erradas. Procure:'))
    s += bullets([
        '<b>Absolutos:</b> “sempre”, “nunca”, “exclusivamente”, “em nenhuma hipótese”. Muitas vezes tornam a afirmação falsa, mas confira com o que você sabe.',
        '<b>Informação de outro assunto:</b> conceito correto, mas que não responde à pergunta.',
        '<b>Troca de termos:</b> fundamento por objetivo, corregedoria por ouvidoria, 0,3% por 0,4%.',
        '<b>Alternativas opostas:</b> quando duas dizem o contrário uma da outra, uma delas costuma ser a correta.',
    ])
    s.append(H2('4. Identificação de pegadinhas'))
    s += table(['Pegadinha', 'Exemplo', 'Defesa'], [
        ['Troca de uma palavra', '“Ordem judicial permite entrar na casa à noite.” (A CF diz “durante o dia”.)', 'Memorize as palavras-chave do texto legal.'],
        ['Número alterado', '“Idade mínima de 21 anos.” (A Lei nº 13.022/2014 fixa 18.)', 'Faça flashcards com números e prazos.'],
        ['Dupla negação', '“Não deixou de prestar socorro.” (= prestou)', 'Reescreva a frase de forma afirmativa.'],
        ['Parte certa, parte errada', 'Primeira metade correta, final errado.', 'Leia cada alternativa até o fim.'],
        ['Concordância “bonita”, mas errada', '“Houveram muitos casos.”', 'Revise as regras dos verbos impessoais.'],
    ], [3.8, 7.4, 5.8], bold_first=True)
    s.append(H2('5. Controle de tempo'))
    s += table(['Estratégia', 'Como aplicar'], [
        ['Tempo médio por questão', 'Divida o tempo total pelo número de questões e reserve 15 a 20 minutos para a folha de respostas. Ex.: 40 questões em 2 h → cerca de 2,5 min por questão.'],
        ['Duas passadas', 'Na 1ª passada, resolva as fáceis e marque as difíceis. Na 2ª, volte às marcadas.'],
        ['Limite por questão', 'Se passar de 4 minutos sem avançar, siga em frente e volte depois.'],
        ['Ordem de resolução', 'Comece pela disciplina que você domina para ganhar confiança e tempo.'],
        ['Folha de respostas', 'Transcreva em blocos (a cada 10 questões), conferindo o número.'],
    ], [4.6, 12.4], bold_first=True)
    s.append(H2('6. Como evitar erros por desatenção'))
    s += bullets([
        'Circule as palavras <b>NÃO, EXCETO, INCORRETA</b> assim que as ler.',
        'Em cálculos, confira a <b>unidade</b> pedida e se a pergunta é sobre o total, a diferença ou a parte.',
        'Antes de marcar, <b>releia o comando</b>: “estou respondendo exatamente o que foi pedido?”.',
        'Não mude a resposta sem um motivo concreto. A primeira impressão costuma estar baseada no que você estudou.',
        'Faça pausas de 30 segundos a cada bloco de questões para recuperar a atenção.',
    ])
    s.append(H2('7. Como interpretar questões difíceis'))
    s += numbered([
        '<b>Divida o enunciado</b> em partes e explique cada uma com suas palavras.',
        '<b>Identifique o assunto:</b> qual conteúdo a questão está testando?',
        '<b>Teste as alternativas:</b> em Matemática, substitua os valores das opções no problema; em Português, troque a palavra e veja se o sentido se mantém.',
        '<b>Use exemplos simples:</b> em lógica, invente uma situação concreta (“Se chover, levo guarda-chuva”).',
        '<b>Elimine e decida:</b> se restarem duas, escolha a mais fiel ao texto, à lei ou ao cálculo.',
    ])
    s += box('exerc', 'Aplique o método nas 10 primeiras questões de Português. Antes de olhar o gabarito, anote para cada uma: o comando, as palavras-chave e as alternativas eliminadas. Depois compare com os comentários.')
    return s


# ======================================================================= capítulos de questões
INTRO = {
    'port': ('Português é base para todas as disciplinas: a interpretação aparece também nas questões de legislação e de matemática. '
             'As questões 1 a 17 usam os Textos I, II e III; leia cada texto com atenção antes de responder.'),
    'info': 'Questões sobre o uso prático do computador e da internet com segurança. Quando a questão citar um programa específico (por exemplo, Word em português), considere a versão indicada.',
    'mat': 'Tenha papel e lápis à mão. Resolva sem calculadora, como na prova, e compare depois a sua resolução com o passo a passo do gabarito.',
    'leg': 'As questões foram elaboradas com base no texto atualizado das normas. Leia cada alternativa com atenção às palavras-chave: números, prazos, “poderá”, “deverá”, “exceto”.',
    'local': 'Conhecimentos sobre o município de Parnaíba. Fatos históricos e administrativos foram conferidos no histórico do município publicado pelo IBGE e no Censo 2022.',
}


def cap_disciplina(num, chave, titulo, qs, textos):
    s = chapter(num, titulo, '%d questões originais de múltipla escolha' % len(qs))
    s.append(P(INTRO[chave]))
    assuntos = {}
    for q in qs:
        assuntos.setdefault(q.assunto, []).append(q.num)
    linhas = []
    for a, ns in assuntos.items():
        faixa = ', '.join(str(n) for n in ns) if len(ns) <= 6 else '%d questões' % len(ns)
        linhas.append([a, faixa])
    s += table(['Assunto', 'Questões'], linhas, [6.0, 11.0], bold_first=True, fs=9.2)
    if chave == 'leg':
        s += box('atencao', [
            '<b>Atualização constitucional:</b> em novembro de 2026, o Congresso Nacional aprovou a chamada PEC da Segurança Pública, que pode alterar o art. 144 da Constituição. Na data de referência deste material, a promulgação ainda não havia sido confirmada, e o texto atualizado do art. 144 consultado era o vigente antes dessa emenda. <b>Confira o texto do art. 144 no momento da prova e as regras do edital.</b>',
        ], 'ATENÇÃO À LEGISLAÇÃO')
    if chave == 'local':
        s += box('dica', 'Dados como população e indicadores mudam com o tempo. Em provas, observe sempre o ano de referência citado no enunciado.')
    if textos:
        s.append(PageBreak())
    s.append(H2('Questões'))
    s += lista_questoes(qs, textos)
    s.append(CondPageBreak(10 * cm))
    s.append(H2('Folha de respostas — %s' % titulo))
    s.append(P('Toque nas bolhas para marcar no PDF (ou imprima e pinte). Depois, corrija no Capítulo 7.', 'small'))
    s.append(AnswerSheet([str(q.num) for q in qs], 'resp_%s' % chave, cols=4))
    return s


def cap_gabaritos():
    s = chapter(7, 'Gabaritos comentados', 'Respostas explicadas por disciplina, com os erros mais comuns')
    s.append(P('Para cada questão você encontra: a alternativa correta, o motivo e os erros que costumam levar candidatos a marcar outra opção. Primeiro confira sua folha de respostas com a grade-resumo; depois leia os comentários.'))
    s += box('dica', 'Leia também o comentário das questões que você acertou. Muitas vezes, o acerto veio por eliminação ou por intuição — e o comentário mostra a regra que garante o acerto na próxima vez.')
    for chave, titulo, qs, _ in DISC:
        s.append(PageBreak())
        s.append(SectionMark('Gabarito — ' + titulo, 'gab_' + chave))
        s.append(H2('Gabarito comentado — %s' % titulo))
        s.append(P('<b>Grade-resumo</b>', 'bodyL'))
        s += grade_gabarito(qs)
        for q in qs:
            s += comentario(q)
    return s


class SectionMark(Flowable):
    """Marcador invisível que cria entrada de 2º nível no índice do PDF (bookmark)."""
    def __init__(self, titulo, chave):
        Flowable.__init__(self)
        self.titulo, self.chave = titulo, chave
        self.width = self.height = 0

    def wrap(self, aw, ah):
        return 0, 0

    def draw(self):
        c = self.canv
        c.bookmarkPage(self.chave)
        c.addOutlineEntry(self.titulo, self.chave, level=1)


# ======================================================================= simulados
def cap_simulados():
    s = chapter(8, 'Simulados', 'Três simulados inéditos para treinar como na prova')
    s.append(P('Os simulados reúnem questões inéditas, que não aparecem nos capítulos de disciplina. Cada simulado tem 40 questões: 11 de Língua Portuguesa, 5 de Informática, 8 ou 9 de Matemática e Raciocínio Lógico e 15 ou 16 de Legislação e Conhecimentos Específicos.'))
    s += box('atencao', 'Os simulados são <b>treinos elaborados para este material</b>. Não são oficiais, não reproduzem a prova de Parnaíba e não indicam a quantidade de questões, os pesos ou as disciplinas do edital.')
    s.append(H2('Instruções gerais'))
    s += numbered([
        '<b>Tempo sugerido:</b> 2 horas por simulado (cerca de 3 minutos por questão, incluindo a transcrição).',
        'Escolha um horário sem interrupções e, se possível, o mesmo turno em que a prova costuma ser aplicada.',
        'Não consulte materiais, anotações ou internet. Deixe o celular longe.',
        'Use relógio ou cronômetro. Reserve os 15 minutos finais para preencher a folha de respostas.',
        'Marque as respostas na folha de respostas do simulado. Só depois consulte o gabarito, que está em seção separada.',
        'Registre o resultado no Capítulo 11 e os erros no caderno de erros.',
    ])
    s += table(['Simulado', 'Quando fazer', 'Meta sugerida'], [
        ['Simulado 1', 'Após resolver ao menos metade das questões de cada disciplina.', 'Conhecer o seu ponto de partida.'],
        ['Simulado 2', 'Cerca de 2 a 3 semanas após o Simulado 1, depois de revisar os erros.', 'Superar o resultado anterior.'],
        ['Simulado 3', 'Na reta final, com todas as revisões em dia.', 'Consolidar a estratégia de tempo.'],
    ], [3.0, 8.5, 5.5], bold_first=True)
    blocos = ['Língua Portuguesa', 'Noções de Informática', 'Matemática e Raciocínio Lógico', 'Legislação e Conhecimentos Específicos']
    for k, qs in enumerate(SIMULADOS, 1):
        s.append(PageBreak())
        s.append(SectionMark('Simulado %d' % k, 'sim%d' % k))
        s.append(SimHeader(k, len(qs)))
        s.append(sp(8))
        tam = [len(SP[k - 1]), len(SI[k - 1]), len(SM[k - 1]), len(SL[k - 1])]
        ini = 0
        for nome, t in zip(blocos, tam):
            s.append(H2('%s (questões %d a %d)' % (nome, ini + 1, ini + t)))
            s += lista_questoes(qs[ini:ini + t], {})
            ini += t
        s.append(PageBreak())
        s.append(H2('Folha de respostas — Simulado %d' % k))
        s.append(FormGrid(['Nome', 'Data', 'Início', 'Término'], [7.0, 3.4, 3.3, 3.3], 1, row_h=0.9 * cm, prefix='sim%dcab' % k))
        s.append(sp(8))
        s.append(AnswerSheet(['%02d' % q.num for q in qs], 'sim%d' % k, cols=4))
        s.append(sp(10))
        s.append(FormGrid(['Disciplina', 'Questões', 'Acertos', '% de acertos'], [7.4, 3.2, 3.2, 3.2], 5, row_h=0.8 * cm, prefix='sim%dres' % k,
                          first_col=['Língua Portuguesa', 'Informática', 'Matemática e RLM', 'Legislação', 'TOTAL']))
    return s


class SimHeader(Flowable):
    def __init__(self, k, n):
        Flowable.__init__(self)
        self.k, self.n = k, n
        self.width = FW
        self.height = 3.0 * cm

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(TEAL)
        c.roundRect(0, 0, self.width, self.height, 8, stroke=0, fill=1)
        c.setFillColor(colors.white)
        c.setFont('Head', 22)
        c.drawString(0.8 * cm, self.height - 1.2 * cm, 'SIMULADO %d' % self.k)
        c.setFont('Body', 11)
        c.drawString(0.8 * cm, self.height - 1.9 * cm, '%d questões  ·  Tempo sugerido: 2 horas  ·  Sem consulta' % self.n)
        c.setFont('Body-I', 9.5)
        c.drawString(0.8 * cm, 0.45 * cm, 'Treino elaborado para este material. Não é prova oficial.')
        c.setFillColor(GOLD)
        c.circle(self.width - 1.6 * cm, self.height / 2, 0.95 * cm, stroke=0, fill=1)
        c.setFillColor(NAVY)
        c.setFont('Head', 26)
        c.drawCentredString(self.width - 1.6 * cm, self.height / 2 - 9, str(self.k))


def cap_gab_simulados():
    s = chapter(9, 'Gabaritos dos simulados', 'Confira somente depois de terminar cada simulado')
    s.append(P('Use a grade-resumo para corrigir rapidamente e depois leia os comentários das questões que errou ou acertou com dúvida.'))
    for k, qs in enumerate(SIMULADOS, 1):
        s.append(PageBreak())
        s.append(SectionMark('Gabarito do Simulado %d' % k, 'gsim%d' % k))
        s.append(H2('Gabarito comentado — Simulado %d' % k))
        s += grade_gabarito(qs, rotulo_fn=lambda q: '%02d' % q.num)
        for q in qs:
            s += comentario(q, '%02d' % q.num)
    return s


# ======================================================================= caderno de erros e desempenho
def cap_caderno():
    s = chapter(10, 'Caderno de erros', 'Páginas preenchíveis para transformar erros em acertos')
    s.append(P('Registre aqui os erros relevantes. Os campos podem ser preenchidos no leitor de PDF (toque e digite) ou à mão, após a impressão. Salve uma cópia do arquivo depois de preencher.'))
    s += table(['Motivo do erro', 'Código sugerido', 'Ação recomendada'], [
        ['Falta de conteúdo', 'CONT', 'Estudar a teoria e criar resumo/flashcard.'],
        ['Conteúdo incompleto (exceção)', 'EXC', 'Anotar a exceção em destaque.'],
        ['Interpretação do enunciado/texto', 'INT', 'Aplicar o método do Capítulo 1.'],
        ['Desatenção', 'DES', 'Circular palavras de comando; reduzir a pressa.'],
        ['Erro de cálculo', 'CALC', 'Refazer a conta e treinar operações básicas.'],
        ['Chute', 'CHU', 'Tratar como falta de conteúdo.'],
    ], [5.4, 3.0, 8.6], bold_first=True)
    hdr = ['Data', 'Disciplina', 'Assunto', 'Questão', 'Erro', 'Motivo', 'Correção', 'Revisão']
    w = [1.5, 2.0, 2.3, 1.6, 2.9, 1.6, 3.4, 1.7]
    for i in range(1, 6):
        s.append(PageBreak())
        s.append(H2('Caderno de erros — folha %d' % i))
        s.append(FormGrid(hdr, w, 13, row_h=1.4 * cm, prefix='erros%d' % i, multiline_cols=(2, 4, 6)))
        s.append(sp(8))
        s.append(WriteLines(2, 'Padrões que percebi nesta folha:', prefix='err_pad%d' % i, h=0.7 * cm))
    return s


def cap_desempenho():
    s = chapter(11, 'Controle de desempenho', 'Acompanhe sua evolução por data e por disciplina')
    s.append(P('Preencha uma linha a cada bloco de questões resolvido. Percentual = acertos ÷ quantidade × 100. Nas observações, anote o assunto com mais erros ou o tipo de erro predominante.'))
    s += table(['% de acertos', 'Leitura sugerida', 'Próximo passo'], [
        ['Abaixo de 50%', 'Base em construção.', 'Rever a teoria e refazer as questões erradas.'],
        ['50% a 69%', 'Evolução em andamento.', 'Reforçar os assuntos com mais erros.'],
        ['70% a 84%', 'Bom domínio.', 'Manter questões e revisões espaçadas.'],
        ['85% ou mais', 'Domínio elevado.', 'Treinar tempo e fazer simulados.'],
    ], [3.5, 5.0, 8.5], bold_first=True)
    s.append(P('As faixas acima são referências pedagógicas e não notas de corte. A nota exigida dependerá do edital e da concorrência.', 'small'))
    hdr = ['Data', 'Disciplina', 'Quantidade', 'Acertos', 'Erros', 'Percentual', 'Observações']
    w = [1.7, 3.0, 1.9, 1.7, 1.6, 1.9, 5.2]
    for i in range(1, 4):
        s.append(PageBreak() if i > 1 else CondPageBreak(14 * cm))
        s.append(H2('Registro de desempenho — página %d' % i))
        s.append(FormGrid(hdr, w, 18, row_h=0.95 * cm, prefix='desemp%d' % i))
    s.append(PageBreak())
    s.append(H2('Resumo por disciplina'))
    s.append(P('Some os resultados de cada disciplina ao final de cada mês.', 'small'))
    s.append(FormGrid(['Disciplina', 'Mês 1 (%)', 'Mês 2 (%)', 'Mês 3 (%)', 'Mês 4 (%)', 'Tendência'],
                      [5.0, 2.2, 2.2, 2.2, 2.2, 3.2], 6, row_h=1.0 * cm, prefix='resumo',
                      first_col=['Língua Portuguesa', 'Informática', 'Matemática e RLM', 'Legislação', 'Conhecimentos locais', 'Simulados']))
    s.append(sp(12))
    s.append(H2('Resultados dos simulados'))
    s.append(FormGrid(['Simulado', 'Data', 'Acertos (de 40)', '%', 'Tempo usado', 'Principal ajuste'],
                      [2.6, 2.2, 2.6, 1.6, 2.4, 5.6], 3, row_h=1.0 * cm, prefix='ressim',
                      first_col=['Simulado 1', 'Simulado 2', 'Simulado 3']))
    return s


VIDEOS = [
    ('Português — crase', 'Crase - Aula 01 ♫ Concerto da Crase ♫ [Prof Noslen]', 'Professor Noslen', 'yUpRa62vcSI', 'Regras básicas de crase com exemplos.'),
    ('Português — concordância verbal', 'Concordância Verbal - Aula 01 [Prof Noslen]', 'Professor Noslen', '4ZJnTqTk4_Y', 'Regra geral e casos especiais de concordância verbal.'),
    ('Matemática — porcentagem', 'APRENDA PORCENTAGEM EM 8 MINUTOS | Fácil e Rápido', 'Dicasdemat Sandro Curió', 'azedx0uou64', 'Cálculo de porcentagem, aumentos e descontos.'),
    ('Matemática — regra de três', 'Aprenda Agora I Regra de Três I Simples I Composta', 'Dicasdemat Sandro Curió', 'aAef69w8aNk', 'Grandezas diretas e inversas; regra de três composta.'),
    ('Raciocínio lógico — tabela-verdade', 'Aprenda de uma vez por todas a montar a Tabela Verdade - Prof Robson Liers - Mathematicamente', 'Prof. Robson Liers - Mathematicamente', 'LGCQ0HZpTDw', 'Conectivos lógicos e montagem da tabela-verdade.'),
    ('Informática — malwares e segurança', 'Informática: Princípios da Segurança da Informação e Malwares', 'Focus Concursos', 'VgXdkqyZdD8', 'Pilares da segurança e tipos de códigos maliciosos.'),
    ('Constituição — art. 5º', 'Constituição Federal - Artigo 5º - Direitos e Deveres Individuais e Coletivos - Aula 01', 'Gustavo Fregapani', 'XS3QU0mHAv0', 'Leitura comentada dos primeiros incisos do art. 5º.'),
    ('Lei nº 13.022/2014', 'Estatuto Geral das Guardas Municipais Atualizado 2026 | Lei 13.022/2014', 'Monster Concursos', 'uB0oN1Qqv7M', 'Visão geral do Estatuto Geral das Guardas Municipais.'),
]


def cap_recursos():
    s = chapter(12, 'Recursos complementares', 'Vídeos gratuitos opcionais e fontes oficiais')
    s.append(P('Os vídeos abaixo são <b>opcionais</b> e servem apenas para quem quiser outra explicação de um assunto mais difícil. Todo o conteúdo necessário está neste PDF. Títulos, canais e links foram conferidos em novembro de 2026; os canais podem alterar ou remover vídeos a qualquer momento.'))
    s += box('atencao', 'Os vídeos são de canais independentes, sem vínculo com este material. Em caso de divergência, prevalecem o texto oficial da lei e o edital.')
    rows = []
    for tema, tit, canal, vid, desc in VIDEOS:
        rows.append(['<b>%s</b>' % tema, '%s<br/><font color="#5B6573">Canal: %s</font><br/>%s' % (tit, canal, link('https://www.youtube.com/watch?v=' + vid, 'Abrir vídeo')), desc])
    s += table(['Assunto', 'Título, canal e link', 'O que complementa'], rows, [4.0, 8.0, 5.0])
    s.append(H2('Fontes oficiais e referências'))
    refs = [
        'BRASIL. Constituição da República Federativa do Brasil de 1988 — texto atualizado. Câmara dos Deputados, Legislação Informatizada: ' + link(CF88, 'camara.leg.br') + '.',
        'BRASIL. Lei nº 13.022, de 8 de agosto de 2014 (Estatuto Geral das Guardas Municipais) — norma atualizada: ' + link(L13022, 'camara.leg.br') + ' · ' + link(PLANALTO_13022, 'planalto.gov.br') + '.',
        'BRASIL. Lei nº 13.060, de 22 de dezembro de 2014 (instrumentos de menor potencial ofensivo): ' + link(PLANALTO_13060, 'planalto.gov.br') + '.',
        'BRASIL. Lei nº 8.069/1990 (Estatuto da Criança e do Adolescente); Lei nº 10.741/2003 (Estatuto da Pessoa Idosa); Lei nº 11.340/2006 (Lei Maria da Penha); Lei nº 13.651/2018 (cria a UFDPar).',
        'ONU. Declaração Universal dos Direitos Humanos, 1948.',
        'STF. ADPF 995 (2023) e RE 608.588 — Tema 656 da repercussão geral (2025), sobre a atuação das guardas municipais.',
        'IBGE. Biblioteca — Parnaíba (PI): histórico e formação administrativa: ' + link(IBGE_HIST, 'biblioteca.ibge.gov.br') + '. Censo Demográfico 2022.',
    ]
    for r in refs:
        s.append(P(r, ParagraphStyle('ref', parent=ST['bodyL'], fontSize=9.8, leading=13.5, leftIndent=12, firstLineIndent=-12)))
    return s


def conclusao():
    s = chapter('', 'Conclusão', 'Missão em andamento')
    s.append(lead('Resolver 320 questões e três simulados não é pouco. Se você chegou até aqui corrigindo, registrando e revisando, construiu algo mais valioso que uma nota: um método.'))
    s.append(P('O desempenho em provas melhora com repetição inteligente: questões, análise dos erros, revisão espaçada e simulados periódicos. Volte ao caderno de erros sempre que possível, refaça as questões que errou e acompanhe a sua evolução no controle de desempenho.'))
    s.append(P('Quando o edital for publicado, compare as disciplinas e os conteúdos com o que você treinou aqui, ajuste o plano de estudos e mantenha a rotina. Nenhum material garante aprovação — mas a prática constante e bem orientada aumenta, e muito, as suas chances.'))
    s += box('recom', ['Próximos passos: (1) refaça as questões que você errou; (2) revise o caderno de erros a cada semana; (3) repita os simulados depois de 30 dias e compare os resultados; (4) acompanhe as publicações oficiais sobre o concurso.'], 'PARA CONTINUAR')
    s.append(sp(12))
    s.append(P('Bons estudos e boa prova.', 'quote'))
    s.append(P('<b>Missão Aprova GCM PHB</b> · 2027', 'center'))
    s.append(sp(16))
    s.append(P('Material de treino independente, com questões originais. Sem vínculo com a Prefeitura Municipal de Parnaíba, com a Guarda Civil Municipal ou com bancas organizadoras. Informações conferidas em novembro de 2026.', 'small'))
    return s


# ======================================================================= build
def montar():
    story = [NextPageTemplate('normal'), PageBreak()]
    story += ficha()
    story += sumario()
    story += apresentacao()
    story += metodo()
    for i, (chave, titulo, qs, textos) in enumerate(DISC, 2):
        story += cap_disciplina(i, chave, titulo, qs, textos)
    story += cap_gabaritos()
    story += cap_simulados()
    story += cap_gab_simulados()
    story += cap_caderno()
    story += cap_desempenho()
    story += cap_recursos()
    story += conclusao()
    return story


def main():
    doc = Doc(SAIDA, title='Missão Aprova GCM PHB 2027',
              author='Projeto Missão Aprova GCM PHB',
              subject='Questões, simulados, revisão e estratégia para a Guarda Civil Municipal de Parnaíba (PI)',
              keywords='concurso, guarda civil municipal, Parnaíba, questões, simulados',
              creator='Missão Aprova GCM PHB', lang='pt-BR')
    doc.multiBuild(montar())
    print('PDF gerado:', SAIDA)


if __name__ == '__main__':
    main()
