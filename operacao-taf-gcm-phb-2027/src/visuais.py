# -*- coding: utf-8 -*-
"""Capa, ilustrações de exercícios (figuras esquemáticas) e diagramas do Operação TAF."""
import motor
from motor import *

ORANGE = HexColor('#E5672A')
GREEN = HexColor('#3C8D3F')

# ------------------------------------------------------------------ figuras esquemáticas
# Coordenadas num espaço de 120 x 70 unidades. Cada pose: linhas (polilinhas) e cabeça (x, y).
POSES = {
    'agachamento': {'linhas': [[(50, 4), (63, 25), (38, 31)], [(38, 31), (47, 55)], [(47, 55), (74, 50)], [(42, 4), (58, 4)]],
                    'cabeca': (51, 63)},
    'agachamento_cadeira': {'linhas': [[(52, 4), (62, 24), (40, 28)], [(40, 28), (48, 53)], [(48, 53), (72, 47)],
                                       [(26, 24), (44, 24)], [(28, 24), (28, 4)], [(26, 24), (26, 46)]],
                            'cabeca': (52, 61)},
    'flexao': {'linhas': [[(30, 4), (30, 25)], [(30, 25), (68, 16), (106, 6)]], 'cabeca': (22, 29)},
    'flexao_joelhos': {'linhas': [[(30, 4), (30, 24)], [(30, 24), (62, 14), (84, 4)], [(84, 4), (100, 14)]], 'cabeca': (22, 28)},
    'flexao_parede': {'linhas': [[(20, 4), (20, 68)], [(22, 46), (40, 46)], [(40, 46), (70, 26), (88, 4)]], 'cabeca': (35, 54)},
    'prancha': {'linhas': [[(30, 4), (44, 4)], [(30, 4), (30, 19)], [(30, 19), (68, 14), (106, 5)]], 'cabeca': (22, 22)},
    'prancha_joelhos': {'linhas': [[(30, 4), (44, 4)], [(30, 4), (30, 19)], [(30, 19), (62, 12), (84, 4)], [(84, 4), (100, 12)]], 'cabeca': (22, 22)},
    'ponte': {'linhas': [[(22, 5), (60, 27)], [(60, 27), (82, 31), (88, 4)], [(22, 5), (56, 4)]], 'cabeca': (12, 8)},
    'perdigueiro': {'linhas': [[(38, 4), (38, 30)], [(38, 30), (76, 30)], [(76, 30), (76, 4)], [(76, 30), (112, 34)], [(38, 30), (6, 36)]],
                    'cabeca': (30, 38)},
    'prancha_lateral': {'linhas': [[(28, 4), (28, 18)], [(28, 4), (40, 4)], [(28, 18), (64, 12), (100, 4)], [(28, 18), (40, 40)]], 'cabeca': (21, 24)},
    'dead_bug': {'linhas': [[(30, 6), (70, 6)], [(30, 6), (34, 42)], [(30, 6), (4, 24)], [(70, 6), (82, 30), (102, 32)], [(70, 6), (106, 10)]],
                 'cabeca': (20, 12)},
    'afundo': {'linhas': [[(32, 4), (36, 26), (60, 30)], [(60, 30), (80, 8), (100, 8)], [(60, 30), (60, 56)], [(60, 52), (48, 40), (58, 32)]],
               'cabeca': (60, 64)},
    'abdominal_parcial': {'linhas': [[(25, 16), (55, 5)], [(55, 5), (75, 28), (92, 4)], [(25, 16), (46, 24)]], 'cabeca': (17, 22)},
    'remada': {'linhas': [[(44, 4), (52, 24), (40, 36)], [(40, 36), (80, 50)], [(74, 48), (72, 30)], [(64, 20), (80, 20), (80, 30), (64, 30), (64, 20)]],
               'cabeca': (90, 55)},
}


class Figura(Flowable):
    """Ilustração esquemática (bonequinho) de um exercício."""

    def __init__(self, pose, legenda='', w=5.4 * cm, h=3.5 * cm):
        Flowable.__init__(self)
        self.pose, self.legenda = pose, legenda
        self.width, self.height = w, h

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(HexColor('#F3F6FA'))
        c.setStrokeColor(LINE)
        c.roundRect(0, 0, self.width, self.height, 6, stroke=1, fill=1)
        leg_h = 0.55 * cm if self.legenda else 0
        bx, by = 0.25 * cm, leg_h + 0.15 * cm
        bw, bh = self.width - 0.5 * cm, self.height - leg_h - 0.35 * cm
        s = min(bw / 120.0, bh / 70.0)
        ox = bx + (bw - 120 * s) / 2
        oy = by
        c.setStrokeColor(HexColor('#B8C3D0'))
        c.setLineWidth(1.2)
        c.line(bx, oy + 4 * s - 2, bx + bw, oy + 4 * s - 2)          # chão
        P = POSES[self.pose]
        c.setStrokeColor(NAVY)
        c.setLineWidth(max(2.6, 4.2 * s))
        c.setLineCap(1)
        c.setLineJoin(1)
        for pl in P['linhas']:
            pth = c.beginPath()
            x0, y0 = pl[0]
            pth.moveTo(ox + x0 * s, oy + y0 * s)
            for (x, y) in pl[1:]:
                pth.lineTo(ox + x * s, oy + y * s)
            c.drawPath(pth, stroke=1, fill=0)
        hx, hy = P['cabeca']
        c.setFillColor(ORANGE)
        c.circle(ox + hx * s, oy + hy * s, 6.2 * s, stroke=0, fill=1)
        if self.legenda:
            c.setFillColor(NAVY)
            c.setFont('Body-B', 8.6)
            c.drawCentredString(self.width / 2, 0.2 * cm, self.legenda)


def linha_figuras(itens):
    """Coloca até 3 figuras lado a lado."""
    n = len(itens)
    w = (FW - (n - 1) * 0.3 * cm) / n if n > 1 else 8.4 * cm
    cells = [Figura(p, l, w=w, h=3.6 * cm) for p, l in itens]
    t = Table([cells], colWidths=[w + (0.3 * cm if i < n - 1 else 0) for i in range(n)])
    t.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                           ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
                           ('VALIGN', (0, 0), (-1, -1), 'TOP')]))
    return [t, Spacer(1, 8)]


# ------------------------------------------------------------------ escala de esforço
class EscalaEsforco(Flowable):
    def __init__(self):
        Flowable.__init__(self)
        self.width = FW
        self.height = 3.0 * cm

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        cores = ['#3C8D3F', '#4E9A3F', '#6AA63E', '#8DB33C', '#B5BE38', '#D9C032', '#E8A317', '#E5862A', '#E5672A', '#C9452E', '#A8302E']
        w = self.width / 11
        y = 1.25 * cm
        for i, col in enumerate(cores):
            c.setFillColor(HexColor(col))
            c.rect(i * w, y, w - 2, 0.8 * cm, stroke=0, fill=1)
            c.setFillColor(colors.white)
            c.setFont('Head', 11)
            c.drawCentredString(i * w + w / 2 - 1, y + 0.27 * cm, str(i))
        faixas = [(0, 2, 'Repouso / muito leve'), (3, 4, 'Leve: conversa fácil'), (5, 6, 'Moderado: fala frases curtas'),
                  (7, 8, 'Forte: fala poucas palavras'), (9, 10, 'Máximo: evitar sem supervisão')]
        st = ParagraphStyle('ef', fontName='Body', fontSize=8.2, leading=9.6, textColor=TEXT, alignment=TA_CENTER)
        for a, b, txt in faixas:
            x0, x1 = a * w, (b + 1) * w - 2
            c.setStrokeColor(GREY)
            c.setLineWidth(0.8)
            c.line(x0 + 2, y - 0.12 * cm, x1 - 2, y - 0.12 * cm)
            p = Paragraph(txt, st)
            pw, ph = p.wrap(x1 - x0, 1 * cm)
            p.drawOn(c, x0, y - 0.2 * cm - ph)
        c.setFillColor(NAVY)
        c.setFont('Body-B', 9.5)
        c.drawString(0, self.height - 0.35 * cm, 'Escala de percepção de esforço (PSE) de 0 a 10 e “teste da fala”')


# ------------------------------------------------------------------ semana-tipo
class SemanaTipo(Flowable):
    def __init__(self, dias):
        Flowable.__init__(self)
        self.dias = dias          # [(dia, atividade, cor)]
        self.width = FW
        self.height = 2.6 * cm

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        n = len(self.dias)
        w = self.width / n
        st = ParagraphStyle('sd', fontName='Body-B', fontSize=8.8, leading=10.4, textColor=colors.white, alignment=TA_CENTER)
        for i, (d, a, col) in enumerate(self.dias):
            x = i * w
            c.setFillColor(NAVY)
            c.roundRect(x + 2, self.height - 0.75 * cm, w - 4, 0.7 * cm, 4, stroke=0, fill=1)
            c.setFillColor(colors.white)
            c.setFont('Head', 9)
            c.drawCentredString(x + w / 2, self.height - 0.52 * cm, d)
            c.setFillColor(col)
            c.roundRect(x + 2, 0, w - 4, self.height - 0.9 * cm, 4, stroke=0, fill=1)
            p = Paragraph(a, st)
            pw, ph = p.wrap(w - 8, 2 * cm)
            p.drawOn(c, x + 4, (self.height - 0.9 * cm - ph) / 2)


# ------------------------------------------------------------------ escada de progressão
class Escada(Flowable):
    def __init__(self, degraus, cor=TEAL):
        Flowable.__init__(self)
        self.degraus = degraus
        self.cor = cor
        self.width = FW
        self.height = 0.7 * cm * len(degraus) + 0.9 * cm

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        n = len(self.degraus)
        step_w = self.width / n
        st = ParagraphStyle('es', fontName='Body-B', fontSize=8.6, leading=10, textColor=colors.white, alignment=TA_CENTER)
        for i, txt in enumerate(self.degraus):
            h = 0.9 * cm + i * 0.7 * cm
            c.setFillColor(self.cor if i < n - 1 else GOLD)
            c.roundRect(i * step_w + 2, 0, step_w - 4, h, 4, stroke=0, fill=1)
            p = Paragraph('%d. %s' % (i + 1, txt), st)
            pw, ph = p.wrap(step_w - 8, h)
            p.drawOn(c, i * step_w + 4, h - ph - 4)


# ------------------------------------------------------------------ gráfico de progressão do volume
class GraficoProgressao(Flowable):
    """Barras: minutos de corrida por sessão em cada semana."""

    def __init__(self, valores, titulo, destaque=()):
        Flowable.__init__(self)
        self.valores = valores
        self.titulo = titulo
        self.destaque = destaque
        self.width = FW
        self.height = 4.6 * cm

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        n = len(self.valores)
        top = max(self.valores)
        base = 0.7 * cm
        hmax = self.height - 1.6 * cm
        bw = (self.width - 1.2 * cm) / n
        c.setFillColor(NAVY)
        c.setFont('Body-B', 9.5)
        c.drawString(0, self.height - 0.35 * cm, self.titulo)
        c.setStrokeColor(LINE)
        c.line(1.0 * cm, base, self.width, base)
        for i, v in enumerate(self.valores):
            h = hmax * v / top
            x = 1.1 * cm + i * bw
            c.setFillColor(GOLD if (i + 1) in self.destaque else TEAL)
            c.rect(x + 3, base, bw - 6, h, stroke=0, fill=1)
            c.setFillColor(TEXT)
            c.setFont('Body-B', 8.4)
            c.drawCentredString(x + bw / 2, base + h + 3, ('%g' % round(v, 1)).replace('.', ','))
            c.setFont('Body', 8)
            c.setFillColor(GREY)
            c.drawCentredString(x + bw / 2, base - 0.38 * cm, 'S%d' % (i + 1))


# ------------------------------------------------------------------ capa
def draw_cover(c, doc):
    W, H = PAGE_W, PAGE_H
    c.saveState()
    c.setFillColor(NAVY)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    # pista de atletismo estilizada (curvas)
    c.setLineWidth(1.4)
    for i in range(6):
        c.setStrokeColor(HexColor('#1E3D60') if i % 2 == 0 else HexColor('#24496F'))
        r = 7.0 * cm + i * 0.75 * cm
        c.circle(W - 4.5 * cm, 8.0 * cm, r, stroke=1, fill=0)
    c.setStrokeColor(HexColor('#132B46'))
    c.setLineWidth(16)
    for i in range(-12, 8):
        x = i * 1.5 * cm
        c.line(x, H, x + 11 * cm, H - 14 * cm)
    c.setFillColor(ORANGE)
    c.rect(0, H - 9.4 * cm, 0.9 * cm, 6.7 * cm, stroke=0, fill=1)
    c.setFont('Head', 11)
    c.drawString(2.0 * cm, H - 3.2 * cm, 'PREPARAÇÃO FÍSICA GERAL  ·  INICIANTES')
    c.setFillColor(colors.white)
    c.setFont('Head', 56)
    c.drawString(1.85 * cm, H - 5.6 * cm, 'OPERAÇÃO')
    c.setFillColor(ORANGE)
    c.setFont('Head', 96)
    c.drawString(1.75 * cm, H - 8.8 * cm, 'TAF')
    c.setFillColor(GOLD)
    c.setFont('Head', 36)
    c.drawString(9.0 * cm, H - 8.6 * cm, 'GCM PHB')
    st = ParagraphStyle('cs', fontName='Body', fontSize=16, leading=21, textColor=HexColor('#DCE6F0'))
    p = Paragraph('Preparação física progressiva para candidatos à Guarda Municipal.', st)
    pw, ph = p.wrap(13.5 * cm, 4 * cm)
    p.drawOn(c, 2.0 * cm, H - 9.7 * cm - ph)
    # figura correndo (esquemática)
    cx, cy, s = W - 5.0 * cm, 11.6 * cm, 0.075 * cm
    c.setStrokeColor(colors.white)
    c.setLineWidth(9)
    c.setLineCap(1)
    c.setLineJoin(1)
    def pl(pts):
        pth = c.beginPath()
        pth.moveTo(cx + pts[0][0] * s, cy + pts[0][1] * s)
        for x, y in pts[1:]:
            pth.lineTo(cx + x * s, cy + y * s)
        c.drawPath(pth, stroke=1, fill=0)
    pl([(0, 0), (8, 40)])                       # tronco
    pl([(0, 0), (22, -18), (12, -44)])          # perna da frente
    pl([(0, 0), (-16, -22), (-40, -30)])        # perna de trás
    pl([(6, 32), (26, 22), (36, 36)])           # braço da frente
    pl([(6, 32), (-12, 18), (-26, 26)])         # braço de trás
    c.setFillColor(ORANGE)
    c.circle(cx + 12 * s, cy + 56 * s, 9 * s, stroke=0, fill=1)
    # linhas de velocidade
    c.setStrokeColor(GOLD)
    c.setLineWidth(3)
    for k, yy in enumerate((20, 6, -8)):
        c.line(cx - (60 + k * 6) * s, cy + yy * s, cx - (95 + k * 10) * s, cy + yy * s)
    # 2027
    c.setFillColor(colors.white)
    c.setFont('Head', 62)
    c.drawString(2.0 * cm, 6.1 * cm, '2027')
    c.setFillColor(ORANGE)
    c.rect(2.0 * cm, 5.6 * cm, 4.4 * cm, 0.18 * cm, stroke=0, fill=1)
    c.setFont('Body-B', 11.5)
    tops = ['Avaliação inicial sem testes máximos', 'Corrida do zero: caminhada → trote → corrida',
            'Fortalecimento com adaptações', 'Planos de 8 e 12 semanas + diário de treino']
    yy = 4.6 * cm
    for t in tops:
        c.setFillColor(ORANGE)
        c.circle(2.15 * cm, yy + 3.5, 2.6, stroke=0, fill=1)
        c.setFillColor(HexColor('#DCE6F0'))
        c.drawString(2.5 * cm, yy, t)
        yy -= 0.62 * cm
    c.setFillColor(HexColor('#0A1A2B'))
    c.rect(0, 0, W, 1.3 * cm, stroke=0, fill=1)
    c.setFont('Body', 8.2)
    c.setFillColor(HexColor('#AFC0D2'))
    c.drawString(2.0 * cm, 0.52 * cm, 'Material independente de preparação física geral. Não apresenta critérios oficiais e não substitui avaliação médica ou de profissional de educação física.')
    c.restoreState()


motor.draw_cover = draw_cover
