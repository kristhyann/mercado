# -*- coding: utf-8 -*-
"""Motor de layout do eBook Operação GCM PHB 2027 (ReportLab/Platypus).

Contém: fontes, cores, estilos, componentes (caixas, tabelas, diagramas,
campos preenchíveis) e o template de páginas (capa, cabeçalho, rodapé, sumário).
"""
import math
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, PageBreak, Flowable,
                                KeepTogether, CondPageBreak, NextPageTemplate)
from reportlab.platypus.tableofcontents import TableOfContents

# ------------------------------------------------------------------ fontes
F = '/usr/share/fonts/truetype/'
pdfmetrics.registerFont(TTFont('Body', F + 'crosextra/Carlito-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Body-B', F + 'crosextra/Carlito-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Body-I', F + 'crosextra/Carlito-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Body-BI', F + 'crosextra/Carlito-BoldItalic.ttf'))
pdfmetrics.registerFont(TTFont('Head', F + 'liberation/LiberationSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Sym', F + 'dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('Sym-B', F + 'dejavu/DejaVuSans-Bold.ttf'))
from reportlab.lib.fonts import addMapping
addMapping('Body', 0, 0, 'Body'); addMapping('Body', 1, 0, 'Body-B')
addMapping('Body', 0, 1, 'Body-I'); addMapping('Body', 1, 1, 'Body-BI')

# ------------------------------------------------------------------ cores
NAVY = HexColor('#0E2238')
NAVY2 = HexColor('#1B3A5C')
GOLD = HexColor('#E8A317')
GOLD_L = HexColor('#FDF3DC')
TEAL = HexColor('#0F7C7A')
TEAL_L = HexColor('#E3F4F3')
RED = HexColor('#B23A3A')
RED_L = HexColor('#FBEAEA')
BLUE_L = HexColor('#E8EFF7')
GREY = HexColor('#5B6573')
GREY_L = HexColor('#F2F4F7')
LINE = HexColor('#C9D1DB')
TEXT = HexColor('#1E2630')

PAGE_W, PAGE_H = A4
ML = MR = 2.0 * cm
MT = 2.4 * cm
MB = 2.2 * cm
FW = PAGE_W - ML - MR          # largura útil = 17 cm

# ------------------------------------------------------------------ estilos
def S(name, **kw):
    base = dict(fontName='Body', fontSize=11.2, leading=16, textColor=TEXT,
                spaceAfter=6)
    base.update(kw)
    return ParagraphStyle(name, **base)

ST = {
    'body': S('body', alignment=TA_JUSTIFY),
    'bodyL': S('bodyL'),
    'lead': S('lead', fontSize=12.5, leading=18, textColor=NAVY2, spaceAfter=10),
    'h2': S('h2', fontName='Head', fontSize=15, leading=19, textColor=NAVY,
            spaceBefore=14, spaceAfter=7, keepWithNext=1),
    'h3': S('h3', fontName='Body-B', fontSize=12.5, leading=16, textColor=TEAL,
            spaceBefore=9, spaceAfter=4, keepWithNext=1),
    'bullet': S('bullet', leftIndent=14, bulletIndent=2, spaceAfter=3,
                alignment=TA_LEFT),
    'small': S('small', fontSize=9, leading=12, textColor=GREY),
    'cell': S('cell', fontSize=9.4, leading=12.2, spaceAfter=0),
    'cellB': S('cellB', fontName='Body-B', fontSize=9.4, leading=12.2, spaceAfter=0),
    'cellH': S('cellH', fontName='Body-B', fontSize=9.6, leading=12, spaceAfter=0,
               textColor=colors.white),
    'boxT': S('boxT', fontName='Body-B', fontSize=11.5, leading=14, spaceAfter=3),
    'box': S('box', fontSize=10.6, leading=14.6, spaceAfter=3),
    'toc0': S('toc0', fontName='Body-B', fontSize=12, leading=17, leftIndent=0,
              textColor=NAVY),
    'center': S('center', alignment=TA_CENTER),
    'quote': S('quote', fontName='Body-I', fontSize=12.5, leading=18,
               textColor=NAVY2, alignment=TA_CENTER, spaceBefore=6, spaceAfter=10),
}

# ------------------------------------------------------------------ helpers de texto
def P(txt, st='body'):
    return Paragraph(txt, ST[st] if isinstance(st, str) else st)

def H2(txt):
    return Heading2(txt)

def H3(txt):
    return KeepWithNextPara(txt)

def lead(txt):
    return P(txt, 'lead')

def bullets(items, char='•', color='#E8A317'):
    out = []
    for it in items:
        out.append(Paragraph(it, ST['bullet'],
                             bulletText=None) if False else
                   Paragraph('<font color="%s"><b>%s</b></font>&nbsp;&nbsp;%s' % (color, char, it),
                             ParagraphStyle('bl', parent=ST['bullet'], firstLineIndent=-12,
                                            leftIndent=16)))
    out.append(Spacer(1, 4))
    return out

def numbered(items):
    out = []
    for i, it in enumerate(items, 1):
        out.append(Paragraph('<font color="#0F7C7A"><b>%d.</b></font>&nbsp;&nbsp;%s' % (i, it),
                             ParagraphStyle('nl', parent=ST['bullet'], firstLineIndent=-15,
                                            leftIndent=19)))
    out.append(Spacer(1, 4))
    return out

def sp(h=6):
    return Spacer(1, h)


class KeepWithNextPara(Paragraph):
    def __init__(self, txt):
        Paragraph.__init__(self, txt, ST['h3'])
        self.keepWithNext = 1


class Heading2(Paragraph):
    def __init__(self, txt):
        Paragraph.__init__(self, txt, ST['h2'])
        self.keepWithNext = 1

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFillColor(GOLD)
        c.rect(-9, 2, 3.2, self.height - 4, stroke=0, fill=1)
        c.restoreState()
        Paragraph.draw(self)


# ------------------------------------------------------------------ caixas
BOX_KIND = {
    'dica':    (TEAL_L, TEAL, 'DICA PRÁTICA'),
    'atencao': (RED_L, RED, 'ATENÇÃO'),
    'fato':    (BLUE_L, NAVY2, 'FATO VERIFICÁVEL'),
    'recom':   (GOLD_L, GOLD, 'RECOMENDAÇÃO'),
    'exerc':   (GREY_L, NAVY, 'EXERCÍCIO'),
    'exemplo': (HexColor('#EEF6EA'), HexColor('#3C7A32'), 'EXEMPLO'),
    'erro':    (RED_L, RED, 'ERROS COMUNS'),
}

def box(kind, content, title=None):
    """Caixa de destaque. content: str ou lista de flowables/strings."""
    bg, fg, label = BOX_KIND[kind]
    t = title or label
    inner = [Paragraph('<font color="%s">%s</font>' % (fg.hexval().replace('0x', '#'), t),
                       ST['boxT'])]
    if isinstance(content, str):
        content = [content]
    for c in content:
        inner.append(Paragraph(c, ST['box']) if isinstance(c, str) else c)
    tb = Table([[inner]], colWidths=[FW])
    tb.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg),
        ('LINEBEFORE', (0, 0), (0, -1), 4, fg),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    return [tb, Spacer(1, 8)]


def box_bullets(kind, items, title=None, intro=None):
    st = ParagraphStyle('bb', parent=ST['box'], leftIndent=13, firstLineIndent=-10)
    fg = BOX_KIND[kind][1].hexval().replace('0x', '#')
    lst = []
    if intro:
        lst.append(intro)
    for it in items:
        lst.append(Paragraph('<font color="%s"><b>•</b></font> %s' % (fg, it), st))
    return box(kind, lst, title)


# ------------------------------------------------------------------ tabelas
class NoSplitTable(Table):
    """Tabela curta: não se divide entre páginas (salvo se maior que a página)."""
    def split(self, aW, aH):
        if getattr(self, '_height', 0) and self._height < PAGE_H - MT - MB - 20:
            return []
        return Table.split(self, aW, aH)

def table(header, rows, widths, head_bg=NAVY, zebra=True, fs=None, bold_first=False, split=False):
    """Tabela com quebra de linha automática. widths em cm (somam ≤ 17)."""
    tot = sum(widths)
    assert tot <= 17.01, ('tabela larga demais', tot)
    cs = ST['cell'] if fs is None else ParagraphStyle('c2', parent=ST['cell'], fontSize=fs, leading=fs * 1.3)
    cb = ST['cellB'] if fs is None else ParagraphStyle('c3', parent=ST['cellB'], fontSize=fs, leading=fs * 1.3)
    data = []
    if header:
        data.append([Paragraph(h, ST['cellH']) for h in header])
    for r in rows:
        data.append([c if isinstance(c, Flowable) else
                     Paragraph(str(c), cb if (bold_first and j == 0) else cs)
                     for j, c in enumerate(r)])
    t = Table(data, colWidths=[w * cm for w in widths], repeatRows=1 if header else 0)
    style = [
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, LINE),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]
    if header:
        style += [('BACKGROUND', (0, 0), (-1, 0), head_bg)]
    if zebra:
        start = 1 if header else 0
        for i in range(start, len(data)):
            if (i - start) % 2 == 1:
                style.append(('BACKGROUND', (0, i), (-1, i), GREY_L))
    t.setStyle(TableStyle(style))
    if len(rows) <= 8 and not split:
        t.__class__ = NoSplitTable
    return [t, Spacer(1, 9)]


# ------------------------------------------------------------------ campos preenchíveis
_FIELD = [0]

def _fname(prefix):
    _FIELD[0] += 1
    return '%s_%04d' % (prefix, _FIELD[0])


class FormGrid(Flowable):
    """Grade com cabeçalho e linhas de campos de texto preenchíveis (AcroForm).
    Funciona impressa (linhas visíveis) e no leitor de PDF (digitação)."""

    def __init__(self, headers, widths_cm, nrows, row_h=0.9 * cm, prefix='campo',
                 first_col=None, head_bg=NAVY, multiline_cols=()):
        Flowable.__init__(self)
        self.headers = headers
        self.ws = [w * cm for w in widths_cm]
        assert sum(widths_cm) <= 17.01
        self.nrows = nrows
        self.row_h = row_h
        self.prefix = prefix
        self.first_col = first_col     # rótulos fixos na 1ª coluna (lista) ou None
        self.head_bg = head_bg
        self.multiline_cols = multiline_cols
        self.head_h = 0.85 * cm
        # altura de cabeçalho dinâmica para textos longos
        for h, w in zip(headers, self.ws):
            p = Paragraph(h, ST['cellH'])
            _, hh = p.wrap(w - 6, 100)
            self.head_h = max(self.head_h, hh + 10)
        self.width = sum(self.ws)
        self.height = self.head_h + nrows * row_h

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        H = self.height
        # cabeçalho
        c.setFillColor(self.head_bg)
        c.rect(0, H - self.head_h, self.width, self.head_h, stroke=0, fill=1)
        x = 0
        for h, w in zip(self.headers, self.ws):
            p = Paragraph(h, ST['cellH'])
            pw, ph = p.wrap(w - 6, 100)
            p.drawOn(c, x + 3, H - self.head_h + (self.head_h - ph) / 2)
            x += w
        # linhas
        for r in range(self.nrows):
            y = H - self.head_h - (r + 1) * self.row_h
            if r % 2 == 1:
                c.setFillColor(GREY_L)
                c.rect(0, y, self.width, self.row_h, stroke=0, fill=1)
            x = 0
            for j, w in enumerate(self.ws):
                if j == 0 and self.first_col is not None:
                    lab = self.first_col[r] if r < len(self.first_col) else ''
                    p = Paragraph(lab, ST['cellB'])
                    pw, ph = p.wrap(w - 8, self.row_h)
                    p.drawOn(c, x + 4, y + (self.row_h - ph) / 2)
                else:
                    flags = 'multiline' if j in self.multiline_cols else ''
                    c.acroForm.textfield(
                        name=_fname(self.prefix), x=x + 1.5, y=y + 1.5,
                        width=w - 3, height=self.row_h - 3, relative=True,
                        borderWidth=0, borderColor=None,
                        fillColor=None, textColor=TEXT, fontName='Helvetica',
                        fontSize=8 if flags else 9, fieldFlags=flags, maxlen=400,
                        tooltip=self.headers[j])
                x += w
        # grade
        c.setStrokeColor(LINE)
        c.setLineWidth(0.6)
        c.rect(0, 0, self.width, H, stroke=1, fill=0)
        for r in range(self.nrows + 1):
            y = H - self.head_h - r * self.row_h
            c.line(0, y, self.width, y)
        x = 0
        for w in self.ws[:-1]:
            x += w
            c.line(x, 0, x, H)


class CheckList(Flowable):
    """Lista com caixas de seleção clicáveis (AcroForm) + texto."""

    def __init__(self, items, prefix='check', width=FW):
        Flowable.__init__(self)
        self.items = items
        self.prefix = prefix
        self.width = width
        self.paras = [Paragraph(t, ParagraphStyle('ck', parent=ST['bodyL'], fontSize=10.8,
                                                  leading=14.5, spaceAfter=0))
                      for t in items]
        self.gap = 5.5
        self._calc()

    def _calc(self):
        self.hs = []
        for p in self.paras:
            _, h = p.wrap(self.width - 26, 1000)
            self.hs.append(max(h, 14))
        self.height = sum(self.hs) + self.gap * len(self.hs)

    def wrap(self, aw, ah):
        return self.width, self.height

    def split(self, aw, ah):
        # permite quebrar listas longas entre páginas
        acc, n = 0, 0
        for h in self.hs:
            if acc + h + self.gap > ah:
                break
            acc += h + self.gap
            n += 1
        if n == 0 or n == len(self.items):
            return []
        return [CheckList(self.items[:n], self.prefix, self.width),
                CheckList(self.items[n:], self.prefix, self.width)]

    def draw(self):
        c = self.canv
        y = self.height
        for p, h in zip(self.paras, self.hs):
            y -= h
            top = y + h
            c.setStrokeColor(NAVY2)
            c.setLineWidth(0.9)
            c.roundRect(1, top - 13, 12, 12, 2, stroke=1, fill=0)
            c.acroForm.checkbox(name=_fname(self.prefix), x=2, y=top - 12, size=10,
                                relative=True, buttonStyle='check', borderWidth=0,
                                borderColor=None, fillColor=None, textColor=TEAL,
                                tooltip='Marcar como concluído')
            p.drawOn(c, 22, y)
            y -= self.gap


class WriteLines(Flowable):
    """Bloco de linhas para escrever, com campo preenchível multilinha."""

    def __init__(self, n=4, label=None, prefix='notas', h=0.75 * cm):
        Flowable.__init__(self)
        self.n, self.label, self.prefix, self.lh = n, label, prefix, h
        self.lab_h = 16 if label else 0
        self.width = FW
        self.height = self.lab_h + n * h + 4

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        if self.label:
            c.setFont('Body-B', 10.5)
            c.setFillColor(NAVY)
            c.drawString(0, self.height - 12, self.label)
        c.setStrokeColor(LINE)
        c.setLineWidth(0.6)
        for i in range(1, self.n + 1):
            y = self.height - self.lab_h - i * self.lh
            c.line(0, y, self.width, y)
        c.acroForm.textfield(name=_fname(self.prefix), x=0, y=self.height - self.lab_h - self.n * self.lh,
                             width=self.width, height=self.n * self.lh, relative=True,
                             borderWidth=0, borderColor=None, fillColor=None,
                             textColor=TEXT, fontName='Helvetica', fontSize=10,
                             fieldFlags='multiline', maxlen=2000, tooltip=self.label or 'Anotações')


# ------------------------------------------------------------------ diagramas
class FlowSteps(Flowable):
    """Fluxo horizontal de etapas em caixas com setas (quebra em linhas)."""

    def __init__(self, steps, per_row=4, box_h=1.55 * cm, color=NAVY2, accent=GOLD, numbered=True):
        Flowable.__init__(self)
        self.steps = steps
        self.per_row = per_row
        self.box_h = box_h
        self.color = color
        self.accent = accent
        self.numbered = numbered
        self.rows = math.ceil(len(steps) / per_row)
        self.vgap = 0.7 * cm
        self.width = FW
        self.height = self.rows * self.box_h + (self.rows - 1) * self.vgap + 6

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        gap = 0.75 * cm
        bw = (self.width - gap * (self.per_row - 1)) / self.per_row
        st = ParagraphStyle('fs', fontName='Body-B', fontSize=9.6, leading=11.5,
                            textColor=colors.white, alignment=TA_CENTER)
        sub = ParagraphStyle('fs2', fontName='Body', fontSize=8.2, leading=10,
                             textColor=HexColor('#DCE6F0'), alignment=TA_CENTER)
        for i, s in enumerate(self.steps):
            r, k = divmod(i, self.per_row)
            x = k * (bw + gap)
            y = self.height - (r + 1) * self.box_h - r * self.vgap
            c.setFillColor(self.color)
            c.roundRect(x, y, bw, self.box_h, 6, stroke=0, fill=1)
            c.setFillColor(self.accent)
            c.rect(x, y + self.box_h - 4, bw, 4, stroke=0, fill=1)
            title, desc = s if isinstance(s, tuple) else (s, '')
            if self.numbered:
                title = '%d. %s' % (i + 1, title)
            p1 = Paragraph(title, st)
            w1, h1 = p1.wrap(bw - 8, self.box_h)
            p2 = Paragraph(desc, sub) if desc else None
            h2 = p2.wrap(bw - 8, self.box_h)[1] if p2 else 0
            tot = h1 + h2 + (2 if p2 else 0)
            yy = y + (self.box_h - 4 - tot) / 2 + h2 + (2 if p2 else 0)
            p1.drawOn(c, x + 4, yy)
            if p2:
                p2.drawOn(c, x + 4, yy - h2 - 2)
            # seta
            if i < len(self.steps) - 1:
                c.setStrokeColor(self.accent)
                c.setFillColor(self.accent)
                c.setLineWidth(2)
                if k < self.per_row - 1:
                    ax = x + bw + 4
                    ay = y + self.box_h / 2
                    c.line(ax, ay, ax + gap - 12, ay)
                    pth = c.beginPath()
                    pth.moveTo(ax + gap - 8, ay)
                    pth.lineTo(ax + gap - 14, ay + 4)
                    pth.lineTo(ax + gap - 14, ay - 4)
                    pth.close()
                    c.drawPath(pth, stroke=0, fill=1)
                else:
                    # seta descendo para próxima linha (volta ao início)
                    ax = x + bw / 2
                    c.line(ax, y - 2, ax, y - self.vgap / 2)
                    c.line(ax, y - self.vgap / 2, bw / 2, y - self.vgap / 2)
                    c.line(bw / 2, y - self.vgap / 2, bw / 2, y - self.vgap + 6)
                    pth = c.beginPath()
                    pth.moveTo(bw / 2, y - self.vgap + 1)
                    pth.lineTo(bw / 2 - 4, y - self.vgap + 7)
                    pth.lineTo(bw / 2 + 4, y - self.vgap + 7)
                    pth.close()
                    c.drawPath(pth, stroke=0, fill=1)


class Timeline(Flowable):
    """Linha do tempo horizontal (ex.: revisões 24h, 7d, 30d)."""

    def __init__(self, points, height=3.3 * cm):
        Flowable.__init__(self)
        self.points = points      # [(rotulo, titulo, descricao)]
        self.width = FW
        self.height = height

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        n = len(self.points)
        y = self.height - 1.0 * cm
        c.setStrokeColor(LINE)
        c.setLineWidth(3)
        x0, x1 = 0.9 * cm, self.width - 0.9 * cm
        c.line(x0, y, x1, y)
        st = ParagraphStyle('tl', fontName='Body-B', fontSize=10, leading=12,
                            textColor=NAVY, alignment=TA_CENTER)
        sd = ParagraphStyle('tl2', fontName='Body', fontSize=8.6, leading=10.5,
                            textColor=GREY, alignment=TA_CENTER)
        seg = (x1 - x0) / (n - 1)
        cols = [NAVY2, TEAL, GOLD, RED, NAVY]
        for i, (lab, tit, desc) in enumerate(self.points):
            x = x0 + i * seg
            c.setFillColor(cols[i % len(cols)])
            c.circle(x, y, 0.42 * cm, stroke=0, fill=1)
            c.setFillColor(colors.white)
            c.setFont('Body-B', 9.5 if len(lab) < 4 else 8)
            c.drawCentredString(x, y - 3.3, lab)
            w = min(seg - 6, 4.2 * cm)
            p = Paragraph(tit, st)
            pw, ph = p.wrap(w, 40)
            p.drawOn(c, x - w / 2, y - 0.55 * cm - ph)
            q = Paragraph(desc, sd)
            qw, qh = q.wrap(w, 60)
            q.drawOn(c, x - w / 2, y - 0.6 * cm - ph - qh)


class CycleWheel(Flowable):
    """Roda do ciclo de estudos (setores proporcionais) com legenda."""

    def __init__(self, parts, title='', size=6.2 * cm):
        Flowable.__init__(self)
        self.parts = parts       # [(nome, horas)]
        self.size = size
        self.title = title
        self.width = FW
        self.height = size + 0.6 * cm

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        pal = [NAVY2, TEAL, GOLD, HexColor('#7A4FA0'), RED, HexColor('#3C7A32'),
               HexColor('#2F6FB0'), HexColor('#A0662F'), GREY]
        tot = sum(h for _, h in self.parts)
        cx, cy, r = self.size / 2 + 0.3 * cm, self.height / 2, self.size / 2
        ang = 90
        for i, (n, h) in enumerate(self.parts):
            ext = -360 * h / tot
            c.setFillColor(pal[i % len(pal)])
            c.setStrokeColor(colors.white)
            c.setLineWidth(2)
            p = c.beginPath()
            p.moveTo(cx, cy)
            p.arcTo(cx - r, cy - r, cx + r, cy + r, ang, ext)
            p.close()
            c.drawPath(p, stroke=1, fill=1)
            ang += ext
        c.setFillColor(colors.white)
        c.circle(cx, cy, r * 0.45, stroke=0, fill=1)
        c.setFillColor(NAVY)
        c.setFont('Body-B', 10)
        c.drawCentredString(cx, cy + 2, self.title)
        c.setFont('Body', 8.5)
        c.drawCentredString(cx, cy - 10, '%g h por volta' % tot)
        # legenda
        lx = self.size + 1.3 * cm
        ly = self.height - 0.6 * cm
        c.setFont('Body', 10)
        for i, (n, h) in enumerate(self.parts):
            c.setFillColor(pal[i % len(pal)])
            c.rect(lx, ly - 2, 10, 10, stroke=0, fill=1)
            c.setFillColor(TEXT)
            c.drawString(lx + 16, ly, '%s — %g h' % (n, h))
            ly -= 0.62 * cm


class StackBar(Flowable):
    """Barra empilhada de distribuição de tempo (min)."""

    def __init__(self, label, parts, total_label=None):
        Flowable.__init__(self)
        self.label = label
        self.parts = parts      # [(nome, minutos, cor)]
        self.width = FW
        self.height = 1.45 * cm

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        lw = 2.4 * cm
        c.setFont('Body-B', 10.5)
        c.setFillColor(NAVY)
        c.drawString(0, 0.62 * cm, self.label)
        tot = sum(m for _, m, _ in self.parts)
        x = lw
        bw = self.width - lw
        for n, m, col in self.parts:
            w = bw * m / tot
            c.setFillColor(col)
            c.rect(x, 0.35 * cm, w, 0.75 * cm, stroke=0, fill=1)
            c.setFillColor(colors.white)
            c.setFont('Body-B', 8.4)
            txt = '%s %d\'' % (n, m)
            if c.stringWidth(txt, 'Body-B', 8.4) > w - 4:
                txt = '%d\'' % m
            c.drawCentredString(x + w / 2, 0.62 * cm, txt)
            x += w


# ------------------------------------------------------------------ abertura de capítulo
class ChapterOpener(Flowable):
    TST = ParagraphStyle('ct', fontName='Head', fontSize=21, leading=25, textColor=colors.white)
    SST = ParagraphStyle('cst', fontName='Body-I', fontSize=11, leading=14, textColor=HexColor('#C9D6E4'))

    def __init__(self, num, title, subtitle=''):
        Flowable.__init__(self)
        self.num, self.title, self.subtitle = num, title, subtitle
        self.width = FW
        self.tw = self.width - 4.5 * cm
        self.pt = Paragraph(title, self.TST)
        self.th = self.pt.wrap(self.tw, 10 * cm)[1]
        self.ps = Paragraph(subtitle, self.SST) if subtitle else None
        self.sh = self.ps.wrap(self.tw, 5 * cm)[1] if self.ps else 0
        top = 1.45 * cm if num else 0.9 * cm
        self.height = 0.4 * cm + top + self.th + (0.25 * cm + self.sh if self.ps else 0) + 0.75 * cm

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        key = 'cap_%s' % (self.num or self.title.lower()[:6])
        c.bookmarkPage(key)
        label = ('%s. %s' % (self.num, self.title)) if self.num else self.title
        c.addOutlineEntry(label, key, level=0)
        dt = c._doctemplate
        dt.chapter = label
        dt.notify('TOCEntry', (0, label, c.getPageNumber(), key))
        h = self.height
        c.setFillColor(NAVY)
        c.roundRect(0, 0.4 * cm, self.width, h - 0.4 * cm, 8, stroke=0, fill=1)
        c.saveState()
        p = c.beginPath()
        p.roundRect(0, 0.4 * cm, self.width, h - 0.4 * cm, 8)
        c.clipPath(p, stroke=0, fill=0)
        c.setStrokeColor(HexColor('#18324F'))
        c.setLineWidth(10)
        for i in range(0, 30):
            xx = self.width - 7 * cm + i * 0.6 * cm
            c.line(xx, 0, xx + 3 * cm, h)
        c.setFillColor(GOLD)
        c.rect(0, 0, 0.35 * cm, h, stroke=0, fill=1)
        c.restoreState()
        y = h - 0.75 * cm
        if self.num:
            c.setFillColor(GOLD)
            c.setFont('Head', 11)
            c.drawString(1.0 * cm, y - 0.15 * cm, 'CAPÍTULO %s' % self.num)
            y -= 0.7 * cm
        else:
            y -= 0.15 * cm
        self.pt.drawOn(c, 1.0 * cm, y - self.th)
        y -= self.th + 0.25 * cm
        if self.ps:
            self.ps.drawOn(c, 1.0 * cm, y - self.sh)


def chapter(num, title, subtitle=''):
    return [PageBreak(), ChapterOpener(num, title, subtitle), Spacer(1, 10)]


# ------------------------------------------------------------------ links
def link(url, text=None):
    return '<link href="%s" color="#0F5FA8"><u>%s</u></link>' % (url, text or url)


# ------------------------------------------------------------------ documento
class Doc(BaseDocTemplate):
    def __init__(self, fn, **kw):
        BaseDocTemplate.__init__(self, fn, pagesize=A4, leftMargin=ML, rightMargin=MR,
                                 topMargin=MT, bottomMargin=MB, **kw)
        self.chapter = ''
        fr = Frame(ML, MB, FW, PAGE_H - MT - MB, id='f', leftPadding=0, rightPadding=0,
                   topPadding=0, bottomPadding=0)
        frc = Frame(0, 0, PAGE_W, PAGE_H, id='fc', leftPadding=0, rightPadding=0,
                    topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate('capa', [frc], onPage=draw_cover),
            PageTemplate('normal', [fr], onPageEnd=draw_page),
        ])

    def beforeDocument(self):
        self.chapter = ''


def draw_page(c, doc):
    n = c.getPageNumber()
    c.saveState()
    # cabeçalho
    c.setFillColor(NAVY)
    c.rect(0, PAGE_H - 0.42 * cm, PAGE_W, 0.42 * cm, stroke=0, fill=1)
    c.setFillColor(GOLD)
    c.rect(0, PAGE_H - 0.52 * cm, PAGE_W * 0.28, 0.1 * cm, stroke=0, fill=1)
    c.setFont('Head', 8.2)
    c.setFillColor(NAVY)
    c.drawString(ML, PAGE_H - 1.35 * cm, 'INTELIGÊNCIA GCM PHB  ·  GUIA DE DISCIPLINAS 2027')
    c.setFont('Body', 8.8)
    c.setFillColor(GREY)
    ch = doc.chapter or ''
    if len(ch) > 58:
        ch = ch[:56] + '…'
    c.drawRightString(PAGE_W - MR, PAGE_H - 1.35 * cm, ch)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.line(ML, PAGE_H - 1.6 * cm, PAGE_W - MR, PAGE_H - 1.6 * cm)
    # rodapé
    c.line(ML, 1.45 * cm, PAGE_W - MR, 1.45 * cm)
    c.setFont('Body', 8.2)
    c.setFillColor(GREY)
    c.drawString(ML, 0.95 * cm, 'Material independente de preparação pré-edital — não oficial. O edital publicado é a referência definitiva.')
    c.setFillColor(NAVY)
    c.roundRect(PAGE_W - MR - 1.2 * cm, 0.72 * cm, 1.2 * cm, 0.55 * cm, 3, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont('Body-B', 9.5)
    c.drawCentredString(PAGE_W - MR - 0.6 * cm, 0.9 * cm, str(n))
    c.restoreState()


def draw_cover(c, doc):
    W, H = PAGE_W, PAGE_H
    c.saveState()
    c.setFillColor(NAVY)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    # faixas diagonais
    c.setStrokeColor(HexColor('#142C47'))
    c.setLineWidth(18)
    for i in range(-10, 30):
        x = i * 1.4 * cm
        c.line(x, 0, x + 12 * cm, H)
    # grade técnica sutil
    c.setStrokeColor(HexColor('#1D3B5E'))
    c.setLineWidth(0.4)
    for i in range(0, 40):
        c.line(0, i * 1 * cm, W, i * 1 * cm)
    # bloco dourado lateral
    c.setFillColor(GOLD)
    c.rect(0, H - 9.2 * cm, 0.9 * cm, 6.5 * cm, stroke=0, fill=1)
    # selo superior
    c.setFillColor(GOLD)
    c.setFont('Head', 11)
    c.drawString(2.0 * cm, H - 3.2 * cm, 'PREPARAÇÃO PRÉ-EDITAL  ·  EBOOK GUIA')
    c.setFillColor(colors.white)
    c.setFont('Head', 58)
    c.drawString(1.85 * cm, H - 5.6 * cm, 'OPERAÇÃO')
    c.setFillColor(GOLD)
    c.setFont('Head', 74)
    c.drawString(1.8 * cm, H - 8.4 * cm, 'GCM PHB')
    # subtítulo
    st = ParagraphStyle('cs', fontName='Body', fontSize=16, leading=21,
                        textColor=HexColor('#DCE6F0'))
    p = Paragraph('O guia estratégico para começar sua preparação para a '
                  '<b><font color="#FFFFFF">Guarda Civil Municipal de Parnaíba</font></b>.', st)
    pw, ph = p.wrap(12.5 * cm, 5 * cm)
    p.drawOn(c, 2.0 * cm, H - 9.4 * cm - ph)

    # ilustração: escudo genérico + livro + check (sem brasões/marcas)
    cx, cy = W - 6.3 * cm, 9.2 * cm
    s = 1.0
    # círculos alvo
    for rr, col in ((5.2, HexColor('#15304E')), (4.2, HexColor('#1B3A5C')), (3.2, HexColor('#21466E'))):
        c.setFillColor(col)
        c.circle(cx, cy, rr * cm, stroke=0, fill=1)
    # escudo
    def shield(x, y, w, h):
        pth = c.beginPath()
        pth.moveTo(x - w / 2, y + h / 2)
        pth.lineTo(x + w / 2, y + h / 2)
        pth.lineTo(x + w / 2, y)
        pth.curveTo(x + w / 2, y - h * 0.32, x + w * 0.2, y - h * 0.45, x, y - h / 2)
        pth.curveTo(x - w * 0.2, y - h * 0.45, x - w / 2, y - h * 0.32, x - w / 2, y)
        pth.close()
        return pth
    c.setFillColor(GOLD)
    c.drawPath(shield(cx, cy + 0.2 * cm, 4.4 * cm, 5.2 * cm), stroke=0, fill=1)
    c.setFillColor(NAVY)
    c.drawPath(shield(cx, cy + 0.2 * cm, 3.7 * cm, 4.5 * cm), stroke=0, fill=1)
    # livro aberto dentro do escudo
    c.setFillColor(colors.white)
    bx, by = cx, cy + 0.55 * cm
    for sgn in (-1, 1):
        pth = c.beginPath()
        pth.moveTo(bx, by - 0.75 * cm)
        pth.curveTo(bx + sgn * 0.6 * cm, by - 0.45 * cm, bx + sgn * 1.1 * cm, by - 0.55 * cm, bx + sgn * 1.45 * cm, by - 0.45 * cm)
        pth.lineTo(bx + sgn * 1.45 * cm, by + 0.85 * cm)
        pth.curveTo(bx + sgn * 1.1 * cm, by + 0.95 * cm, bx + sgn * 0.6 * cm, by + 0.85 * cm, bx, by + 0.6 * cm)
        pth.close()
        c.drawPath(pth, stroke=0, fill=1)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.8)
    for k in range(4):
        yy = by + 0.45 * cm - k * 0.28 * cm
        c.line(bx - 1.2 * cm, yy, bx - 0.25 * cm, yy - 0.05 * cm)
        c.line(bx + 0.25 * cm, yy - 0.05 * cm, bx + 1.2 * cm, yy)
    # check
    c.setStrokeColor(GOLD)
    c.setLineWidth(5)
    c.setLineCap(1)
    c.setLineJoin(1)
    pth = c.beginPath()
    pth.moveTo(cx - 0.75 * cm, cy - 1.0 * cm)
    pth.lineTo(cx - 0.15 * cm, cy - 1.6 * cm)
    pth.lineTo(cx + 0.95 * cm, cy - 0.45 * cm)
    c.drawPath(pth, stroke=1, fill=0)
    # estrelas pequenas de progresso
    c.setFillColor(GOLD)
    c.setFont('Sym', 13)
    for i in range(3):
        c.drawCentredString(cx - 0.9 * cm + i * 0.9 * cm, cy + 2.15 * cm, '★')

    # ano grande
    c.setFillColor(colors.white)
    c.setFont('Head', 64)
    c.drawString(2.0 * cm, 6.2 * cm, '2027')
    c.setFillColor(GOLD)
    c.rect(2.0 * cm, 5.7 * cm, 4.5 * cm, 0.18 * cm, stroke=0, fill=1)
    # tópicos
    c.setFont('Body-B', 11.5)
    c.setFillColor(HexColor('#DCE6F0'))
    topics = ['Do zero à rotina de estudos', 'Planos de 30, 60 e 90 dias',
              'Métodos, revisões e questões', 'Planner, checklists e caderno de erros']
    yy = 4.6 * cm
    for t in topics:
        c.setFillColor(GOLD)
        c.circle(2.15 * cm, yy + 3.5, 2.6, stroke=0, fill=1)
        c.setFillColor(HexColor('#DCE6F0'))
        c.drawString(2.5 * cm, yy, t)
        yy -= 0.62 * cm
    # rodapé capa
    c.setFillColor(HexColor('#0A1A2B'))
    c.rect(0, 0, W, 1.3 * cm, stroke=0, fill=1)
    c.setFont('Body', 8.6)
    c.setFillColor(HexColor('#AFC0D2'))
    c.drawString(2.0 * cm, 0.52 * cm, 'Material educacional independente. Não é publicação oficial da Prefeitura de Parnaíba nem da Guarda Civil Municipal.')
    c.restoreState()


def make_toc():
    toc = TableOfContents()
    toc.levelStyles = [ParagraphStyle('t0', fontName='Body-B', fontSize=11.5, leading=15,
                                      textColor=NAVY, leftIndent=0, spaceBefore=3.5,
                                      spaceAfter=3.5)]
    toc.dotsMinLevel = 0
    return toc
