# -*- coding: utf-8 -*-
"""Componentes específicos do Missão Aprova: capa, questões, folha de respostas e gabaritos."""
import motor
from motor import *
from qbase import LETRAS

# ------------------------------------------------------------------ estilos de questão
QS = {
    'num': ParagraphStyle('qnum', fontName='Head', fontSize=10.5, leading=13, textColor=colors.white, alignment=TA_CENTER),
    'tag': ParagraphStyle('qtag', fontName='Body', fontSize=8.6, leading=10, textColor=GREY),
    'enun': ParagraphStyle('qenun', fontName='Body', fontSize=11, leading=15.2, textColor=TEXT, spaceAfter=4),
    'alt': ParagraphStyle('qalt', fontName='Body', fontSize=10.6, leading=14.2, textColor=TEXT,
                          leftIndent=22, firstLineIndent=-22, spaceAfter=2.5),
    'gtit': ParagraphStyle('gtit', fontName='Body-B', fontSize=10.8, leading=14, textColor=NAVY, spaceAfter=2),
    'gtxt': ParagraphStyle('gtxt', fontName='Body', fontSize=10, leading=13.6, textColor=TEXT, spaceAfter=2),
    'gerro': ParagraphStyle('gerro', fontName='Body', fontSize=9.6, leading=13, textColor=HexColor('#7A2E2E'), spaceAfter=0),
    'txt': ParagraphStyle('txtbase', fontName='Body', fontSize=10.8, leading=15.5, textColor=TEXT, alignment=TA_JUSTIFY,
                          firstLineIndent=14, spaceAfter=0),
}


def bloco_texto(texto):
    corpo = [Paragraph('<font color="#0F7C7A"><b>%s</b></font>' % texto.titulo, ST['boxT'])]
    for par in texto.corpo.split('<br/>'):
        corpo.append(Paragraph(par, QS['txt']))
    corpo.append(Spacer(1, 4))
    corpo.append(Paragraph('<i>%s</i>' % texto.fonte, ST['small']))
    t = Table([[corpo]], colWidths=[FW])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor('#F6F8FB')),
        ('BOX', (0, 0), (-1, -1), 0.6, LINE),
        ('LINEBEFORE', (0, 0), (0, -1), 4, TEAL),
        ('LEFTPADDING', (0, 0), (-1, -1), 12), ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 9), ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
    ]))
    return [Spacer(1, 4), t, Spacer(1, 10)]


def tabela_questao(tab):
    head, rows = tab
    n = len(head)
    w = [min(6.0, 12.0 / n)] * n
    return table(head, rows, w, fs=9.6)


def questao(q, rotulo=None):
    """Bloco visual de uma questão (enunciado + alternativas)."""
    num = rotulo or str(q.num)
    badge = Table([[Paragraph(num, QS['num'])]], colWidths=[1.25 * cm], rowHeights=[0.62 * cm])
    badge.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), NAVY), ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, -1), 0),
                               ('RIGHTPADDING', (0, 0), (-1, -1), 0), ('TOPPADDING', (0, 0), (-1, -1), 0),
                               ('BOTTOMPADDING', (0, 0), (-1, -1), 1)]))
    tag = q.assunto + (' · com base no %s' % q.texto.split(' — ')[0] if q.texto else '')
    head = Table([[badge, Paragraph(tag, QS['tag'])]], colWidths=[1.45 * cm, FW - 1.45 * cm])
    head.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('LEFTPADDING', (0, 0), (-1, -1), 0),
                              ('RIGHTPADDING', (0, 0), (-1, -1), 0), ('TOPPADDING', (0, 0), (-1, -1), 0),
                              ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
    parts = [head, Spacer(1, 4), Paragraph(q.enunciado, QS['enun'])]
    if q.tabela:
        parts += tabela_questao(q.tabela)
    for L, a in zip(LETRAS, q.alts):
        parts.append(Paragraph('<font color="#1B3A5C"><b>(%s)</b></font>&nbsp;&nbsp;%s' % (L, a), QS['alt']))
    t = NoSplitTable([[parts]], colWidths=[FW])
    t.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                           ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
    return [t, Spacer(1, 11)]


def lista_questoes(qs, mapa_textos, rotulo_fn=None):
    out = []
    ultimo = None
    for q in qs:
        if q.texto and q.texto != ultimo and q.texto in mapa_textos:
            out.append(CondPageBreak(9 * cm))
            out += bloco_texto(mapa_textos[q.texto])
        ultimo = q.texto
        out += questao(q, rotulo_fn(q) if rotulo_fn else None)
    return out


def comentario(q, rotulo=None):
    num = rotulo or str(q.num)
    corpo = [Paragraph('Questão %s &nbsp;·&nbsp; <font color="#0F7C7A">Gabarito: %s</font> &nbsp;·&nbsp; '
                       '<font color="#5B6573" size="9">%s</font>' % (num, q.resp, q.assunto), QS['gtit']),
             Paragraph('<b>Resposta correta:</b> (%s) %s' % (q.resp, q.alts[LETRAS.index(q.resp)]), QS['gtxt']),
             Paragraph('<b>Por quê:</b> ' + q.expl, QS['gtxt'])]
    if q.erro:
        corpo.append(Paragraph('<b>Erros comuns:</b> ' + q.erro, QS['gerro']))
    t = Table([[corpo]], colWidths=[FW])
    t.setStyle(TableStyle([
        ('LINEBEFORE', (0, 0), (0, -1), 3, GOLD),
        ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    return [t, Spacer(1, 8)]


def grade_gabarito(qs, rotulo_fn=None, por_linha=10):
    """Tabela-resumo de gabarito (número/letra)."""
    rows = []
    for i in range(0, len(qs), por_linha):
        bloco = qs[i:i + por_linha]
        nums = [(rotulo_fn(q) if rotulo_fn else str(q.num)) for q in bloco]
        rows.append(['<b>%s</b>' % n for n in nums] + [''] * (por_linha - len(bloco)))
        rows.append(['<font color="#0F7C7A"><b>%s</b></font>' % q.resp for q in bloco] + [''] * (por_linha - len(bloco)))
    data = [[Paragraph(c, ParagraphStyle('gg', parent=ST['cell'], alignment=TA_CENTER, fontSize=9.4)) for c in r] for r in rows]
    w = FW / por_linha
    t = Table(data, colWidths=[w] * por_linha)
    st = [('GRID', (0, 0), (-1, -1), 0.5, LINE), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
          ('TOPPADDING', (0, 0), (-1, -1), 2), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]
    for r in range(0, len(data), 2):
        st.append(('BACKGROUND', (0, r), (-1, r), BLUE_L))
    t.setStyle(TableStyle(st))
    return [t, Spacer(1, 10)]


# ------------------------------------------------------------------ folha de respostas
class AnswerSheet(Flowable):
    """Folha de respostas com bolhas clicáveis (grupos de rádio AcroForm) — imprimível também."""

    def __init__(self, rotulos, prefix, cols=4, row_h=0.62 * cm):
        Flowable.__init__(self)
        self.rotulos = rotulos
        self.prefix = prefix
        self.cols = cols
        self.row_h = row_h
        self.rows = -(-len(rotulos) // cols)
        self.width = FW
        self.head = 0.55 * cm
        self.height = self.head + self.rows * row_h + 4

    def wrap(self, aw, ah):
        return self.width, self.height

    def split(self, aw, ah):
        n_rows = int((ah - self.head - 4) // self.row_h)
        if n_rows <= 0 or n_rows >= self.rows:
            return []
        k = n_rows * self.cols
        # divide por colunas: mantém numeração em sequência vertical dentro de cada parte
        return [AnswerSheet(self.rotulos[:k], self.prefix, self.cols, self.row_h),
                AnswerSheet(self.rotulos[k:], self.prefix, self.cols, self.row_h)]

    def draw(self):
        c = self.canv
        cw = self.width / self.cols
        H = self.height
        for k in range(self.cols):
            x0 = k * cw
            c.setFillColor(NAVY)
            c.roundRect(x0 + 2, H - self.head, cw - 4, self.head - 2, 3, stroke=0, fill=1)
            c.setFillColor(colors.white)
            c.setFont('Body-B', 8.6)
            c.drawString(x0 + 8, H - self.head + 5, 'Nº')
            for j, L in enumerate(LETRAS):
                c.drawCentredString(x0 + 0.95 * cm + j * 0.62 * cm + 5, H - self.head + 5, L)
        for i, rot in enumerate(self.rotulos):
            k, r = divmod(i, self.rows)
            x0 = k * cw
            y = H - self.head - (r + 1) * self.row_h
            if r % 2 == 1:
                c.setFillColor(GREY_L)
                c.rect(x0 + 2, y, cw - 4, self.row_h, stroke=0, fill=1)
            c.setFillColor(NAVY)
            c.setFont('Body-B', 9)
            c.drawString(x0 + 7, y + self.row_h / 2 - 3, rot)
            grupo = '%s_%s' % (self.prefix, rot.replace('.', '_'))
            for j, L in enumerate(LETRAS):
                cx = x0 + 0.95 * cm + j * 0.62 * cm
                c.setStrokeColor(NAVY2)
                c.setLineWidth(0.7)
                c.circle(cx + 5, y + self.row_h / 2, 5.6, stroke=1, fill=0)
                c.setFont('Body', 6.4)
                c.setFillColor(HexColor('#9AA5B4'))
                c.drawCentredString(cx + 5, y + self.row_h / 2 - 2.2, L)
                c.acroForm.radio(name=grupo, value=L, selected=False, x=cx, y=y + self.row_h / 2 - 5,
                                 size=10, relative=True, buttonStyle='circle', shape='circle',
                                 borderWidth=0, borderColor=None, fillColor=None, textColor=TEAL,
                                 forceBorder=False, tooltip='Questão %s — alternativa %s' % (rot, L))
        c.setStrokeColor(LINE)
        c.setLineWidth(0.5)
        for k in range(1, self.cols):
            c.line(k * cw, 0, k * cw, H - self.head)


# ------------------------------------------------------------------ capa
def draw_cover(c, doc):
    W, H = PAGE_W, PAGE_H
    c.saveState()
    c.setFillColor(NAVY)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setStrokeColor(HexColor('#132B46'))
    c.setLineWidth(16)
    for i in range(-12, 30):
        x = i * 1.5 * cm
        c.line(x, H, x + 11 * cm, 0)
    c.setStrokeColor(HexColor('#1D3B5E'))
    c.setLineWidth(0.4)
    for i in range(0, 22):
        c.line(i * 1 * cm, 0, i * 1 * cm, H)
    # faixa dourada lateral
    c.setFillColor(GOLD)
    c.rect(0, H - 9.6 * cm, 0.9 * cm, 6.9 * cm, stroke=0, fill=1)
    c.setFont('Head', 11)
    c.drawString(2.0 * cm, H - 3.2 * cm, 'QUESTÕES  ·  SIMULADOS  ·  REVISÃO')
    c.setFillColor(colors.white)
    c.setFont('Head', 54)
    c.drawString(1.85 * cm, H - 5.5 * cm, 'MISSÃO')
    c.drawString(1.85 * cm, H - 7.4 * cm, 'APROVA')
    c.setFillColor(GOLD)
    c.setFont('Head', 60)
    c.drawString(1.8 * cm, H - 9.6 * cm, 'GCM PHB')
    st = ParagraphStyle('cs', fontName='Body', fontSize=15.5, leading=20.5, textColor=HexColor('#DCE6F0'))
    p = Paragraph('Questões, simulados, revisão e estratégia para treinar seu desempenho.', st)
    pw, ph = p.wrap(12.5 * cm, 4 * cm)
    p.drawOn(c, 2.0 * cm, H - 10.5 * cm - ph)
    # ilustração: alvo + folha de respostas
    cx, cy = W - 6.0 * cm, 8.6 * cm
    for rr, col in ((5.0, HexColor('#15304E')), (4.0, HexColor('#1B3A5C')), (3.0, HexColor('#21466E'))):
        c.setFillColor(col)
        c.circle(cx, cy, rr * cm, stroke=0, fill=1)
    # folha
    fw, fh = 4.6 * cm, 5.8 * cm
    fx, fy = cx - fw / 2 - 0.3 * cm, cy - fh / 2
    c.setFillColor(HexColor('#0A1A2B'))
    c.roundRect(fx + 0.18 * cm, fy - 0.18 * cm, fw, fh, 6, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.roundRect(fx, fy, fw, fh, 6, stroke=0, fill=1)
    c.setFillColor(NAVY)
    c.rect(fx, fy + fh - 0.75 * cm, fw, 0.75 * cm, stroke=0, fill=1)
    c.setFillColor(GOLD)
    c.setFont('Head', 8)
    c.drawString(fx + 0.3 * cm, fy + fh - 0.5 * cm, 'FOLHA DE RESPOSTAS')
    marcadas = [1, 3, 0, 4, 2, 1, 3]
    for r in range(7):
        yy = fy + fh - 1.35 * cm - r * 0.62 * cm
        c.setFillColor(GREY)
        c.setFont('Body-B', 7.5)
        c.drawString(fx + 0.25 * cm, yy - 2.5, '%02d' % (r + 1))
        for j in range(5):
            bx = fx + 1.05 * cm + j * 0.68 * cm
            if j == marcadas[r]:
                c.setFillColor(TEAL)
                c.circle(bx, yy, 0.2 * cm, stroke=0, fill=1)
            else:
                c.setStrokeColor(HexColor('#9AA5B4'))
                c.setLineWidth(0.8)
                c.circle(bx, yy, 0.2 * cm, stroke=1, fill=0)
    # selo de check
    sx, sy = cx + 2.3 * cm, cy - 2.2 * cm
    c.setFillColor(GOLD)
    c.circle(sx, sy, 1.05 * cm, stroke=0, fill=1)
    c.setStrokeColor(NAVY)
    c.setLineWidth(5)
    c.setLineCap(1)
    c.setLineJoin(1)
    pth = c.beginPath()
    pth.moveTo(sx - 0.5 * cm, sy)
    pth.lineTo(sx - 0.1 * cm, sy - 0.4 * cm)
    pth.lineTo(sx + 0.55 * cm, sy + 0.4 * cm)
    c.drawPath(pth, stroke=1, fill=0)
    # ano
    c.setFillColor(colors.white)
    c.setFont('Head', 62)
    c.drawString(2.0 * cm, 6.1 * cm, '2027')
    c.setFillColor(GOLD)
    c.rect(2.0 * cm, 5.6 * cm, 4.4 * cm, 0.18 * cm, stroke=0, fill=1)
    c.setFont('Body-B', 11.5)
    tops = ['320 questões originais comentadas', '3 simulados com folha de respostas',
            'Gabaritos explicados passo a passo', 'Caderno de erros e controle de desempenho']
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
    c.drawString(2.0 * cm, 0.52 * cm, 'Material de treino independente. Não é publicação oficial da Prefeitura de Parnaíba, da Guarda Civil Municipal ou de banca organizadora.')
    c.restoreState()


motor.draw_cover = draw_cover
