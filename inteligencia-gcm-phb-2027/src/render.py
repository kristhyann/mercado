# -*- coding: utf-8 -*-
"""Renderização dos tópicos, exercícios e gabaritos + capa do Inteligência GCM PHB."""
import motor
from motor import *
from qbase import LETRAS

PURPLE = HexColor('#5B3E8E')

# ------------------------------------------------------------------ estrutura de tópico
class Topico:
    def __init__(self, titulo, definicao, explicacao, exemplos=(), erros=(), resumo=(), exercicios=()):
        self.titulo = titulo
        self.definicao = definicao
        self.explicacao = explicacao
        self.exemplos = list(exemplos)
        self.erros = list(erros)
        self.resumo = list(resumo)
        self.exercicios = list(exercicios)


def tab(header, rows, widths, fs=None):
    return ('tab', header, rows, widths, fs)


def bl(items):
    return ('bl', items)


def h3(t):
    return ('h3', t)


def caixa(kind, conteudo, titulo=None):
    return ('box', kind, conteudo, titulo)


def fluxo(passos, per_row=4):
    return ('flow', passos, per_row)


def num(items):
    return ('num', items)


def render_bloco(b):
    if isinstance(b, str):
        return [P(b)]
    k = b[0]
    if k == 'tab':
        _, hdr, rows, w, fs = b
        return table(hdr, rows, w, bold_first=True, fs=fs)
    if k == 'bl':
        return bullets(b[1])
    if k == 'num':
        return numbered(b[1])
    if k == 'h3':
        return [H3(b[1])]
    if k == 'box':
        _, kind, cont, tit = b
        if isinstance(cont, list) and kind in ('erro',):
            return box_bullets(kind, cont, tit)
        return box(kind, cont, tit)
    if k == 'flow':
        return [FlowSteps(b[1], per_row=b[2], box_h=1.5 * cm), Spacer(1, 10)]
    if isinstance(b, Flowable):
        return [b]
    raise ValueError(b)


# ------------------------------------------------------------------ questões
QS = {
    'num': ParagraphStyle('qnum', fontName='Head', fontSize=9.6, leading=12, textColor=colors.white, alignment=TA_CENTER),
    'tag': ParagraphStyle('qtag', fontName='Body', fontSize=8.4, leading=10, textColor=GREY),
    'enun': ParagraphStyle('qenun', fontName='Body', fontSize=10.8, leading=14.8, textColor=TEXT, spaceAfter=3),
    'alt': ParagraphStyle('qalt', fontName='Body', fontSize=10.4, leading=13.8, textColor=TEXT, leftIndent=22, firstLineIndent=-22, spaceAfter=2),
    'gtit': ParagraphStyle('gtit', fontName='Body-B', fontSize=10.6, leading=13.6, textColor=NAVY, spaceAfter=2),
    'gtxt': ParagraphStyle('gtxt', fontName='Body', fontSize=9.9, leading=13.4, textColor=TEXT, spaceAfter=2),
    'gerro': ParagraphStyle('gerro', fontName='Body', fontSize=9.5, leading=12.8, textColor=HexColor('#7A2E2E')),
}


def _nst(parts):
    t = NoSplitTable([[parts]], colWidths=[FW])
    t.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                           ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
    return t


def questao(q, rotulo):
    badge = Table([[Paragraph(rotulo, QS['num'])]], colWidths=[1.5 * cm], rowHeights=[0.58 * cm])
    badge.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), PURPLE), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                               ('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                               ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 1)]))
    head = Table([[badge, Paragraph(q.assunto, QS['tag'])]], colWidths=[1.7 * cm, FW - 1.7 * cm])
    head.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, -1), 0),
                              ('RIGHTPADDING', (0, 0), (-1, -1), 0), ('TOPPADDING', (0, 0), (-1, -1), 0),
                              ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
    parts = [head, Spacer(1, 3), Paragraph(q.enunciado, QS['enun'])]
    if q.tabela:
        hdr, rows = q.tabela
        parts += table(hdr, rows, [min(6.0, 12.0 / len(hdr))] * len(hdr), fs=9.4)
    for L, a in zip(LETRAS, q.alts):
        parts.append(Paragraph('<font color="#5B3E8E"><b>(%s)</b></font>&nbsp;&nbsp;%s' % (L, a), QS['alt']))
    return [_nst(parts), Spacer(1, 9)]


def comentario(q, rotulo):
    corpo = [Paragraph('%s &nbsp;·&nbsp; <font color="#0F7C7A">Gabarito: %s</font> &nbsp;·&nbsp; <font color="#5B6573" size="9">%s</font>'
                       % (rotulo, q.resp, q.assunto), QS['gtit']),
             Paragraph('<b>Resposta:</b> (%s) %s' % (q.resp, q.alts[LETRAS.index(q.resp)]), QS['gtxt']),
             Paragraph('<b>Explicação:</b> ' + q.expl, QS['gtxt'])]
    if q.erro:
        corpo.append(Paragraph('<b>Atenção:</b> ' + q.erro, QS['gerro']))
    t = Table([[corpo]], colWidths=[FW])
    t.setStyle(TableStyle([('LINEBEFORE', (0, 0), (0, -1), 3, GOLD), ('LEFTPADDING', (0, 0), (-1, -1), 10),
                           ('RIGHTPADDING', (0, 0), (-1, -1), 4), ('TOPPADDING', (0, 0), (-1, -1), 3),
                           ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]))
    return [t, Spacer(1, 7)]


# ------------------------------------------------------------------ render de tópico
class Marca(Flowable):
    """Marcador invisível: cria entrada de 2º nível nos marcadores (bookmarks) do PDF."""
    def __init__(self, titulo, chave):
        Flowable.__init__(self)
        self.titulo, self.chave = titulo, chave

    def wrap(self, aw, ah):
        return 0, 0

    def draw(self):
        self.canv.bookmarkPage(self.chave)
        self.canv.addOutlineEntry(self.titulo, self.chave, level=1)


def render_topico(t, sigla, idx, contador):
    """Retorna (flowables, lista de (rotulo, questão))."""
    tit = '%s.%d %s' % (sigla, idx, t.titulo)
    s = [CondPageBreak(7 * cm), Marca(tit, 'top_%s_%d' % (sigla, idx)), H2(tit)]
    s += box('fato', t.definicao, 'DEFINIÇÃO')
    for b in t.explicacao:
        s += render_bloco(b)
    if t.exemplos:
        s += box_bullets('exemplo', t.exemplos, 'EXEMPLOS')
    if t.erros:
        s += box_bullets('erro', t.erros, 'ERROS COMUNS')
    if t.resumo:
        s += box_bullets('recom', t.resumo, 'RESUMO')
    qs = []
    if t.exercicios:
        s.append(H3('Exercícios — %s' % t.titulo))
        for q in t.exercicios:
            contador[0] += 1
            rot = '%s-%02d' % (sigla, contador[0])
            s += questao(q, rot)
            qs.append((rot, q))
    return s, qs


def render_disciplina(num_cap, titulo, subtitulo, sigla, intro, topicos, revisao, resumo_cap, aviso=None, abertura=None):
    s = chapter(num_cap, titulo, subtitulo)
    for b in intro:
        s += render_bloco(b)
    if aviso:
        s += aviso
    s.append(H3('Tópicos deste capítulo'))
    s += table(['Nº', 'Tópico'], [['%s.%d' % (sigla, i), t.titulo] for i, t in enumerate(topicos, 1)], [2.0, 15.0], fs=9.4)
    if abertura:
        s += abertura
    contador = [0]
    todas = []
    for i, t in enumerate(topicos, 1):
        f, qs = render_topico(t, sigla, i, contador)
        s += f
        todas += [('Tópico %s.%d — %s' % (sigla, i, t.titulo), qs)]
    # resumo do capítulo
    s.append(PageBreak())
    s.append(H2('Resumo do capítulo — %s' % titulo))
    s += table(['Tema', 'Pontos-chave'], resumo_cap, [4.6, 12.4], fs=9.4)
    # revisão
    rev = []
    if revisao:
        s.append(CondPageBreak(8 * cm))
        s.append(H2('Exercícios de revisão — %s' % titulo))
        s.append(P('Questões que misturam os tópicos do capítulo. Resolva sem consultar e depois confira o gabarito comentado.', 'small'))
        for j, q in enumerate(revisao, 1):
            rot = '%s-R%02d' % (sigla, j)
            s += questao(q, rot)
            rev.append((rot, q))
    # gabarito
    s.append(PageBreak())
    s.append(H2('Gabarito comentado — %s' % titulo))
    grade = [(r, q.resp) for _, qs in todas for r, q in qs] + [(r, q.resp) for r, q in rev]
    s += grade_resumo(grade)
    for nome, qs in todas:
        if not qs:
            continue
        s.append(H3(nome))
        for r, q in qs:
            s += comentario(q, r)
    if rev:
        s.append(H3('Exercícios de revisão'))
        for r, q in rev:
            s += comentario(q, r)
    n = sum(len(qs) for _, qs in todas) + len(rev)
    return s, n


def grade_resumo(pares, por_linha=8):
    rows = []
    for i in range(0, len(pares), por_linha):
        b = pares[i:i + por_linha]
        rows.append(['<b>%s</b>' % r for r, _ in b] + [''] * (por_linha - len(b)))
        rows.append(['<font color="#0F7C7A"><b>%s</b></font>' % l for _, l in b] + [''] * (por_linha - len(b)))
    st = ParagraphStyle('gg', parent=ST['cell'], alignment=TA_CENTER, fontSize=8.6, leading=10.5)
    data = [[Paragraph(c, st) for c in r] for r in rows]
    t = Table(data, colWidths=[FW / por_linha] * por_linha)
    sty = [('GRID', (0, 0), (-1, -1), 0.5, LINE), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
           ('TOPPADDING', (0, 0), (-1, -1), 2), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]
    for r in range(0, len(data), 2):
        sty.append(('BACKGROUND', (0, r), (-1, r), BLUE_L))
    t.setStyle(TableStyle(sty))
    return [t, Spacer(1, 10)]


# ------------------------------------------------------------------ capa
def draw_cover(c, doc):
    W, H = PAGE_W, PAGE_H
    c.saveState()
    c.setFillColor(NAVY)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    # rede de conexões (inteligência)
    import random
    rnd = random.Random(7)
    pts = [(rnd.uniform(10.5 * cm, W - 0.6 * cm), rnd.uniform(5.2 * cm, 15 * cm)) for _ in range(24)]
    c.setLineWidth(0.7)
    for i, (x1, y1) in enumerate(pts):
        for (x2, y2) in pts[i + 1:]:
            d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            if d < 3.6 * cm:
                c.setStrokeColor(HexColor('#27507A'))
                c.line(x1, y1, x2, y2)
    for i, (x, y) in enumerate(pts):
        c.setFillColor(GOLD if i % 5 == 0 else HexColor('#4C7DB0'))
        c.circle(x, y, 3.2 if i % 5 == 0 else 2.2, stroke=0, fill=1)
    # livro estilizado
    bx, by = W - 6.2 * cm, 9.0 * cm
    c.setFillColor(HexColor('#0A1A2B'))
    c.roundRect(bx - 2.9 * cm, by - 2.3 * cm, 5.8 * cm, 4.4 * cm, 8, stroke=0, fill=1)
    for sgn, col in ((-1, colors.white), (1, HexColor('#E9EEF5'))):
        c.setFillColor(col)
        pth = c.beginPath()
        pth.moveTo(bx, by - 1.6 * cm)
        pth.curveTo(bx + sgn * 1.0 * cm, by - 1.2 * cm, bx + sgn * 2.0 * cm, by - 1.35 * cm, bx + sgn * 2.5 * cm, by - 1.2 * cm)
        pth.lineTo(bx + sgn * 2.5 * cm, by + 1.6 * cm)
        pth.curveTo(bx + sgn * 2.0 * cm, by + 1.75 * cm, bx + sgn * 1.0 * cm, by + 1.6 * cm, bx, by + 1.25 * cm)
        pth.close()
        c.drawPath(pth, stroke=0, fill=1)
    c.setStrokeColor(LINE)
    c.setLineWidth(1)
    for k in range(6):
        yy = by + 0.9 * cm - k * 0.38 * cm
        c.line(bx - 2.15 * cm, yy, bx - 0.35 * cm, yy - 0.06 * cm)
        c.line(bx + 0.35 * cm, yy - 0.06 * cm, bx + 2.15 * cm, yy)
    c.setFillColor(GOLD)
    c.circle(bx + 2.3 * cm, by + 1.6 * cm, 0.55 * cm, stroke=0, fill=1)
    c.setFillColor(NAVY)
    c.setFont('Head', 13)
    c.drawCentredString(bx + 2.3 * cm, by + 1.43 * cm, '§')
    # títulos
    c.setFillColor(GOLD)
    c.rect(0, H - 9.6 * cm, 0.9 * cm, 6.9 * cm, stroke=0, fill=1)
    c.setFont('Head', 11)
    c.drawString(2.0 * cm, H - 3.2 * cm, 'PREPARAÇÃO PRÉ-EDITAL  ·  GUIA DE DISCIPLINAS')
    c.setFillColor(colors.white)
    c.setFont('Head', 50)
    c.drawString(1.85 * cm, H - 5.5 * cm, 'INTELIGÊNCIA')
    c.setFillColor(GOLD)
    c.setFont('Head', 66)
    c.drawString(1.8 * cm, H - 8.1 * cm, 'GCM PHB')
    st = ParagraphStyle('cs', fontName='Body', fontSize=15, leading=20, textColor=HexColor('#DCE6F0'))
    p = Paragraph('Guia de disciplinas, legislação e conhecimentos locais para a preparação pré-edital.', st)
    pw, ph = p.wrap(12.0 * cm, 4 * cm)
    p.drawOn(c, 2.0 * cm, H - 9.1 * cm - ph)
    c.setFillColor(colors.white)
    c.setFont('Head', 62)
    c.drawString(2.0 * cm, 6.1 * cm, '2027')
    c.setFillColor(GOLD)
    c.rect(2.0 * cm, 5.6 * cm, 4.4 * cm, 0.18 * cm, stroke=0, fill=1)
    c.setFont('Body-B', 11.2)
    tops = ['Português, Constituição e Lei nº 13.022/2014', 'Direitos Humanos, Administração Pública e Informática',
            'Matemática, Raciocínio Lógico e Parnaíba', 'Explicações, exemplos, exercícios e gabaritos']
    yy = 4.6 * cm
    for t in tops:
        c.setFillColor(GOLD)
        c.circle(2.15 * cm, yy + 3.5, 2.6, stroke=0, fill=1)
        c.setFillColor(HexColor('#DCE6F0'))
        c.drawString(2.5 * cm, yy, t)
        yy -= 0.62 * cm
    c.setFillColor(HexColor('#0A1A2B'))
    c.rect(0, 0, W, 1.3 * cm, stroke=0, fill=1)
    c.setFont('Body', 8.4)
    c.setFillColor(HexColor('#AFC0D2'))
    c.drawString(2.0 * cm, 0.52 * cm, 'Material didático independente. Não é publicação oficial da Prefeitura de Parnaíba, da Guarda Civil Municipal ou de banca organizadora.')
    c.restoreState()


motor.draw_cover = draw_cover
