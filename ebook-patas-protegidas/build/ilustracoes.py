"""Gera todas as ilustrações vetoriais (SVG) do e-book Patas Protegidas.

Executar:  python3 build/ilustracoes.py
Saída:     imagens/ilustracoes/*.svg

Todas as ilustrações são originais, desenhadas em código, e podem ser
editadas em qualquer editor vetorial (Inkscape, Illustrator, Figma).
"""
from pathlib import Path
import math
import random

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "imagens" / "ilustracoes"

VE = "#1d4a39"   # verde-escuro
V = "#2f6b52"    # verde
VM = "#5b9677"   # verde-médio
VC = "#a9cbb0"   # verde-claro
VP = "#e4efe5"   # verde-pastel
B = "#f5eee2"    # bege
BM = "#ece0cc"   # bege-médio
BE = "#d8c6a8"   # bege-escuro
L = "#e48a45"    # laranja
LE = "#bf6526"   # laranja-escuro
LC = "#fbe6d4"   # laranja-claro
R = "#c0392b"    # vermelho
T = "#22302a"    # texto
CARAMELO = "#d9a066"
CARAMELO_E = "#a8703c"
MADEIRA = "#d9b48a"
MADEIRA_E = "#a97c50"
INOX = "#c9d2d6"
INOX_E = "#8e9ba1"
AGUA = "#8fc6e0"

FONTE = "font-family='Nunito Sans, sans-serif'"

# ------------------------------------------------------------------
# Ícones (traço 24×24) — usados em caixas, aberturas e fichas
# ------------------------------------------------------------------
ICONES = {
    "casa": "M3 11.5 12 4l9 7.5M5.5 9.5V20h13V9.5M10 20v-5.5h4V20",
    "escudo": "M12 3 4.5 6v5.5c0 4.6 3.2 8.2 7.5 9.5 4.3-1.3 7.5-4.9 7.5-9.5V6L12 3Z",
    "tigela": "M3 11h18c0 4.4-3.6 8-8 8h-2c-4.4 0-8-3.6-8-8ZM7 8c1.5-1 3-1 4.5 0M12.5 7c1.5-1 3-1 4.5 0",
    "gota": "M12 3.5c3.2 4.2 6 7.6 6 10.8a6 6 0 0 1-12 0c0-3.2 2.8-6.6 6-10.8Z",
    "estetoscopio": "M6 3v6a4 4 0 0 0 8 0V3M10 13v2a5 5 0 0 0 10 0v-2M20 13a1.6 1.6 0 1 0 0-3.2 1.6 1.6 0 0 0 0 3.2Z",
    "seringa": "m18 3 3 3M16.5 4.5l3 3M19 6l-9.5 9.5-3-3L16 3M7.8 13.8 3 21M11 10l1.5 1.5M9 12l1.5 1.5",
    "cruz": "M9 3h6v6h6v6h-6v6H9v-6H3V9h6V3Z",
    "pilula": "M10.5 20.5a5 5 0 0 1-7-7l6-6a5 5 0 0 1 7 7l-6 6ZM7 10l7 7",
    "banho": "M4 12h16v2a6 6 0 0 1-6 6h-4a6 6 0 0 1-6-6v-2ZM6 12V6a2.5 2.5 0 0 1 5 0M7 20l-1 2M17 20l1 2",
    "bola": "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18ZM5 6.5c3 2 3 9 0 11M19 6.5c-3 2-3 9 0 11",
    "pata": "M12 20c-3 0-5.5-1.6-5.5-4 0-2.6 2.6-5 5.5-5s5.5 2.4 5.5 5c0 2.4-2.5 4-5.5 4ZM6 10.5a1.8 2.3 0 1 0 0-.1M18 10.5a1.8 2.3 0 1 0 0-.1M9.3 7a1.8 2.3 0 1 0 0-.1M14.7 7a1.8 2.3 0 1 0 0-.1",
    "coracao": "M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.3 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10Z",
    "ferramenta": "M14.5 6.5a4 4 0 0 0 5 5l-9 9a2.1 2.1 0 0 1-3-3l9-9a4 4 0 0 0-2-2ZM16 3l-1.5 3.5L17.5 9.5 21 8",
    "carro": "M4 15.5V12l2-5h12l2 5v3.5M4 15.5h16v2.5h-3v-2.5M4 15.5v2.5h3v-2.5M7.5 12.5h.01M16.5 12.5h.01M5 12h14",
    "telefone": "M5 4h3.5l1.5 4-2 1.5a10 10 0 0 0 6.5 6.5L16 14l4 1.5V19a1.5 1.5 0 0 1-1.6 1.5C10.6 20 4 13.4 3.5 5.6A1.5 1.5 0 0 1 5 4Z",
    "checklist": "M9 6h11M9 12h11M9 18h11M4 6l1 1 2-2M4 12l1 1 2-2M4 18l1 1 2-2",
    "alerta": "M12 4 2.8 20h18.4L12 4ZM12 10v4.5M12 17.2v.01",
    "relogio": "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18ZM12 7v5l3 2",
    "termometro": "M10 14.5V5a2 2 0 0 1 4 0v9.5a4 4 0 1 1-4 0ZM12 9v7",
    "lupa": "M10.5 17a6.5 6.5 0 1 0 0-13 6.5 6.5 0 0 0 0 13ZM15.5 15.5 21 21",
    "info": "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18ZM12 11v6M12 7.5v.01",
    "proibido": "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18ZM5.6 5.6l12.8 12.8",
    "lampada": "M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2V16h5v-.1c0-.8.4-1.5 1-2A6 6 0 0 0 12 3Z",
    "osso": "M7 9.5a2.5 2.5 0 1 1 1.8-4.3 2.5 2.5 0 1 1 4.3 1.8l4 4a2.5 2.5 0 1 1 1.8 4.3 2.5 2.5 0 1 1-4.3 1.8l-4-4A2.5 2.5 0 0 1 7 9.5Z",
    "idoso": "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18ZM8.5 10h.01M15.5 10h.01M8.5 15c2 1.5 5 1.5 7 0",
    "mapa": "M9 4 3 6v14l6-2 6 2 6-2V4l-6 2-6-2ZM9 4v14M15 6v14",
    "mala": "M4 8h16v11H4V8ZM9 8V5h6v3M4 13h16",
}


def icone(nome, cor=VE, traco=1.8, preenchido=False, tamanho=24):
    d = ICONES[nome]
    fill = cor if preenchido else "none"
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' width='{tamanho}' height='{tamanho}' "
            f"fill='{fill}' stroke='{cor}' stroke-width='{traco}' stroke-linecap='round' stroke-linejoin='round'>"
            f"<path d='{d}'/></svg>")


# ------------------------------------------------------------------
# Utilidades de desenho
# ------------------------------------------------------------------
def svg(w, h, corpo, fundo=None):
    bg = f"<rect width='{w}' height='{h}' fill='{fundo}'/>" if fundo else ""
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}' width='{w}' height='{h}' "
            f"{FONTE}>{bg}{corpo}</svg>")


def txt(x, y, s, tam=11, cor=T, peso=700, ancora="middle", estilo=""):
    return (f"<text x='{x}' y='{y}' font-size='{tam}' fill='{cor}' font-weight='{peso}' "
            f"text-anchor='{ancora}' {estilo}>{s}</text>")


def multitxt(x, y, linhas, tam=10, cor=T, peso=600, ancora="middle", entre=None):
    entre = entre or tam * 1.25
    return "".join(txt(x, y + i * entre, l, tam, cor, peso, ancora) for i, l in enumerate(linhas))


def bloco(x, y, texto, chars=28, tam=9.6, cor=VE, peso=800):
    """Texto com quebra automática de linha (âncora à esquerda)."""
    linhas, atual = [], ""
    for palavra in texto.split():
        if len(atual) + len(palavra) + 1 > chars and atual:
            linhas.append(atual)
            atual = palavra
        else:
            atual = (atual + " " + palavra).strip()
    linhas.append(atual)
    return multitxt(x, y, linhas, tam, cor, peso, "start", tam * 1.22)


def suave(pontos, fechado=True):
    """Curva Catmull-Rom → Bézier passando pelos pontos."""
    n = len(pontos)
    pts = pontos + pontos[:3] if fechado else [pontos[0]] + pontos + [pontos[-1]]
    d = f"M{pts[1][0]:.1f},{pts[1][1]:.1f}" if fechado else f"M{pontos[0][0]:.1f},{pontos[0][1]:.1f}"
    rng = range(n) if fechado else range(n - 1)
    for i in rng:
        p0, p1, p2, p3 = pts[i], pts[i + 1], pts[i + 2], pts[i + 3]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    return d + (" Z" if fechado else "")


def numero(x, y, n, cor=L, r=11):
    return (f"<circle cx='{x}' cy='{y}' r='{r}' fill='{cor}' stroke='#fff' stroke-width='2'/>"
            + txt(x, y + r * 0.38, n, r * 1.05, "#fff", 800))


def cao(x, y, s=1.0, cor=CARAMELO, sombra=CARAMELO_E, olhar=1, deitado=False):
    """Cachorro estilizado de perfil (≈100×68 em escala 1)."""
    g = f"<g transform='translate({x},{y}) scale({s * olhar},{s})'>"
    if deitado:
        g += (f"<path d='M14 50 q-14 -4 -12 -16' stroke='{sombra}' stroke-width='6' fill='none' stroke-linecap='round'/>"
              f"<rect x='12' y='38' width='66' height='22' rx='11' fill='{cor}'/>"
              f"<rect x='56' y='54' width='34' height='8' rx='4' fill='{sombra}'/>"
              f"<circle cx='84' cy='40' r='13' fill='{cor}'/>"
              f"<ellipse cx='95' cy='45' rx='8' ry='6' fill='{cor}'/>"
              f"<circle cx='102' cy='43' r='2.6' fill='{T}'/>"
              f"<path d='M76 30 q-7 2 -6 16 q7 -2 10 -12z' fill='{sombra}'/>"
              f"<path d='M84 38 q3 2 6 0' stroke='{T}' stroke-width='1.6' fill='none' stroke-linecap='round'/>")
    else:
        g += (f"<path d='M22 30 q-12 -6 -14 -20' stroke='{sombra}' stroke-width='6' fill='none' stroke-linecap='round'/>"
              f"<rect x='25' y='40' width='7' height='24' rx='3.5' fill='{sombra}'/>"
              f"<rect x='62' y='40' width='7' height='24' rx='3.5' fill='{sombra}'/>"
              f"<rect x='18' y='24' width='60' height='24' rx='12' fill='{cor}'/>"
              f"<rect x='33' y='40' width='7' height='24' rx='3.5' fill='{cor}'/>"
              f"<rect x='70' y='40' width='7' height='24' rx='3.5' fill='{cor}'/>"
              f"<path d='M66 30 q4 -14 14 -16' stroke='{cor}' stroke-width='14' fill='none' stroke-linecap='round'/>"
              f"<circle cx='82' cy='16' r='13' fill='{cor}'/>"
              f"<ellipse cx='94' cy='21' rx='9' ry='6.5' fill='{cor}'/>"
              f"<circle cx='101' cy='18.5' r='2.8' fill='{T}'/>"
              f"<circle cx='85' cy='12' r='1.9' fill='{T}'/>"
              f"<path d='M74 5 q-8 2 -6 18 q7 -2 11 -14z' fill='{sombra}'/>"
              f"<path d='M93 26 q3 2 6 0' stroke='{T}' stroke-width='1.2' fill='none' stroke-linecap='round'/>")
    return g + "</g>"


def pegada(x, y, s=1.0, cor="#fff", op=0.08, rot=0):
    return (f"<g transform='translate({x},{y}) rotate({rot}) scale({s})' fill='{cor}' opacity='{op}'>"
            "<ellipse cx='0' cy='6' rx='7' ry='6'/><ellipse cx='-8' cy='-4' rx='2.8' ry='3.6'/>"
            "<ellipse cx='-3' cy='-9' rx='2.8' ry='3.6'/><ellipse cx='3' cy='-9' rx='2.8' ry='3.6'/>"
            "<ellipse cx='8' cy='-4' rx='2.8' ry='3.6'/></g>")


def tigela(cx, base, larg=60, alt=18, cor=INOX, cor_e=INOX_E, agua=False, racao=False):
    a = larg / 2
    d = f"M{cx - a},{base - alt} L{cx + a},{base - alt} L{cx + a * .78},{base} L{cx - a * .78},{base} Z"
    s = f"<path d='{d}' fill='{cor}' stroke='{cor_e}' stroke-width='1.5' stroke-linejoin='round'/>"
    s += f"<ellipse cx='{cx}' cy='{base - alt}' rx='{a}' ry='{alt * .28}' fill='{cor_e}' opacity='.55'/>"
    if agua:
        s += f"<ellipse cx='{cx}' cy='{base - alt + 1}' rx='{a * .9}' ry='{alt * .22}' fill='{AGUA}'/>"
    if racao:
        for i in range(9):
            s += f"<circle cx='{cx - a * .7 + i * a * .175}' cy='{base - alt - 1 - (i % 2) * 2}' r='{alt * .16}' fill='{CARAMELO_E}'/>"
    return s


def seta(x1, y1, x2, y2, cor=T, larg=1.6):
    ang = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 7 * math.cos(ang - .45), y2 - 7 * math.sin(ang - .45))
    p2 = (x2 - 7 * math.cos(ang + .45), y2 - 7 * math.sin(ang + .45))
    return (f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{cor}' stroke-width='{larg}'/>"
            f"<path d='M{x2},{y2} L{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} Z' fill='{cor}'/>")


def cota(x1, y1, x2, y2, rotulo, cor=LE, desloc=0, tam=9.5):
    """Linha de medida com setas nas duas pontas."""
    s = seta((x1 + x2) / 2, (y1 + y2) / 2, x1, y1, cor, 1.2) + seta((x1 + x2) / 2, (y1 + y2) / 2, x2, y2, cor, 1.2)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    if abs(x2 - x1) < abs(y2 - y1):  # vertical
        s += (f"<g transform='translate({mx + 4 + desloc},{my}) rotate(-90)'>"
              f"<rect x='{-len(rotulo) * tam * .29 - 3}' y='-9' width='{len(rotulo) * tam * .58 + 6}' height='13' fill='#fff' rx='3'/>"
              + txt(0, 0, rotulo, tam, cor, 800) + "</g>")
    else:
        s += (f"<rect x='{mx - len(rotulo) * tam * .29 - 3}' y='{my - 9 + desloc}' width='{len(rotulo) * tam * .58 + 6}' height='13' fill='#fff' rx='3'/>"
              + txt(mx, my + 1 + desloc, rotulo, tam, cor, 800))
    return s


def painel(x, y, w, h, n, titulo, corpo):
    """Quadro de etapa numerada para os projetos caseiros."""
    s = f"<g transform='translate({x},{y})'>"
    s += f"<rect width='{w}' height='{h}' rx='10' fill='#fff' stroke='{BE}' stroke-width='1.2'/>"
    s += numero(18, 18, str(n), L, 11)
    s += txt(36, 22, titulo, 10.5, VE, 800, "start")
    s += corpo + "</g>"
    return s


def x_vermelho(x, y, r=10):
    return (f"<circle cx='{x}' cy='{y}' r='{r}' fill='{R}'/>"
            f"<path d='M{x - r * .4},{y - r * .4} L{x + r * .4},{y + r * .4} M{x + r * .4},{y - r * .4} L{x - r * .4},{y + r * .4}' stroke='#fff' stroke-width='2.4' stroke-linecap='round'/>")


def ok_verde(x, y, r=10):
    return (f"<circle cx='{x}' cy='{y}' r='{r}' fill='{V}'/>"
            f"<path d='M{x - r * .45},{y} L{x - r * .1},{y + r * .38} L{x + r * .48},{y - r * .35}' stroke='#fff' stroke-width='2.4' fill='none' stroke-linecap='round' stroke-linejoin='round'/>")


# ------------------------------------------------------------------
# Ilustrações
# ------------------------------------------------------------------
def logo(cor_escudo=VE, cor_pata=L, contorno="#fff"):
    pata = ("<g fill='{c}'><ellipse cx='50' cy='62' rx='15' ry='12.5'/>"
            "<ellipse cx='31' cy='45' rx='6' ry='7.6'/><ellipse cx='42.5' cy='34' rx='6' ry='7.6'/>"
            "<ellipse cx='57.5' cy='34' rx='6' ry='7.6'/><ellipse cx='69' cy='45' rx='6' ry='7.6'/></g>").format(c=cor_pata)
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100' width='100' height='100'>"
            f"<path d='M50 4 12 18v26c0 24 16 42 38 52 22-10 38-28 38-52V18L50 4Z' fill='{cor_escudo}' stroke='{contorno}' stroke-width='4'/>"
            f"{pata}</svg>")


def abertura_padrao(nome_icone, semente=1, fundo1=VE, fundo2=V):
    """Arte de abertura para capítulos sem fotografia."""
    rnd = random.Random(semente)
    w, h = 420, 318
    s = (f"<defs><linearGradient id='g{semente}' x1='0' y1='0' x2='1' y2='1'>"
         f"<stop offset='0' stop-color='{fundo2}'/><stop offset='1' stop-color='{fundo1}'/></linearGradient></defs>"
         f"<rect width='{w}' height='{h}' fill='url(#g{semente})'/>")
    s += f"<circle cx='{w * .78}' cy='{h * .38}' r='118' fill='#fff' opacity='.06'/>"
    s += f"<circle cx='{w * .78}' cy='{h * .38}' r='84' fill='#fff' opacity='.07'/>"
    s += f"<circle cx='{w * .1}' cy='{h * .1}' r='60' fill='{L}' opacity='.13'/>"
    for i in range(16):
        x, y = rnd.uniform(10, w - 10), rnd.uniform(10, h - 30)
        s += pegada(x, y, rnd.uniform(.8, 1.5), "#fff", rnd.uniform(.05, .11), rnd.uniform(-40, 40))
    d = ICONES[nome_icone]
    s += (f"<g transform='translate({w * .78 - 72},{h * .38 - 72}) scale(6)' fill='none' stroke='#fff' "
          f"stroke-width='1.1' stroke-linecap='round' stroke-linejoin='round' opacity='.9'><path d='{d}'/></g>")
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}' preserveAspectRatio='xMidYMid slice'>{s}</svg>")


def casa_segura():
    w, h = 520, 330
    s = f"<rect width='{w}' height='{h}' fill='{B}'/>"
    s += f"<rect x='0' y='272' width='{w}' height='58' fill='{VC}'/>"
    # casa
    s += f"<path d='M30 120 L170 40 L310 120 Z' fill='{VE}'/>"
    s += f"<rect x='45' y='118' width='250' height='154' fill='#fff' stroke='{VE}' stroke-width='3'/>"
    s += f"<line x1='170' y1='118' x2='170' y2='272' stroke='{VE}' stroke-width='3'/>"
    s += f"<line x1='45' y1='195' x2='295' y2='195' stroke='{VE}' stroke-width='3'/>"
    # janela/sacada
    s += f"<rect x='200' y='132' width='60' height='44' fill='{AGUA}' opacity='.5' stroke='{VE}' stroke-width='2'/>"
    s += f"<g stroke='{VE}' stroke-width='1.2'>" + "".join(f"<line x1='{200 + i * 6}' y1='132' x2='{200 + i * 6}' y2='176'/>" for i in range(1, 10)) + "</g>"
    # tomada e fio
    s += f"<rect x='62' y='240' width='16' height='20' rx='3' fill='#fff' stroke='{T}' stroke-width='1.5'/><circle cx='67' cy='249' r='1.6' fill='{T}'/><circle cx='73' cy='249' r='1.6' fill='{T}'/>"
    s += f"<path d='M78 252 q20 18 50 6 t40 10' stroke='{T}' stroke-width='2' fill='none'/>"
    # produtos de limpeza
    s += f"<rect x='190' y='232' width='14' height='38' rx='3' fill='{L}'/><rect x='194' y='224' width='6' height='9' fill='{LE}'/>"
    s += f"<rect x='208' y='240' width='16' height='30' rx='3' fill='#7fb2d6'/>"
    # planta
    s += f"<path d='M130 168 q-12 -18 -2 -30 q4 16 4 30 M134 168 q2 -22 14 -28 q-2 18 -10 28 M132 168 q-18 -6 -22 -18 q14 2 22 18' fill='{V}' stroke='{V}'/>"
    s += f"<path d='M120 168 h28 l-4 20 h-20 z' fill='{LE}'/>"
    # sacola
    s += f"<path d='M245 240 h30 l-3 30 h-24 z' fill='#fff' stroke='{T}' stroke-width='1.4'/><path d='M252 240 q8 -14 16 0' stroke='{T}' stroke-width='1.4' fill='none'/>"
    # objetos pequenos
    for i, c in enumerate([R, L, "#7fb2d6", V]):
        s += f"<circle cx='{105 + i * 9}' cy='{185 - (i % 2) * 3}' r='3.4' fill='{c}'/>"
    # piscina
    s += f"<rect x='330' y='250' width='120' height='30' rx='6' fill='{AGUA}' stroke='#5a9fc0' stroke-width='2'/>"
    s += f"<path d='M338 262 q8 -5 16 0 t16 0 t16 0 t16 0 t16 0 t16 0' stroke='#fff' stroke-width='2' fill='none'/>"
    # portão
    s += f"<g stroke='{VE}' stroke-width='3'><line x1='470' y1='180' x2='470' y2='275'/><line x1='512' y1='180' x2='512' y2='275'/><line x1='470' y1='190' x2='512' y2='190'/><line x1='470' y1='265' x2='512' y2='265'/></g>"
    s += f"<g stroke='{VE}' stroke-width='1.6'>" + "".join(f"<line x1='{474 + i * 6}' y1='190' x2='{474 + i * 6}' y2='265'/>" for i in range(7)) + "</g>"
    # sol e calor
    s += f"<circle cx='440' cy='60' r='24' fill='#f6c453'/>" + "".join(
        f"<line x1='{440 + 30 * math.cos(a)}' y1='{60 + 30 * math.sin(a)}' x2='{440 + 40 * math.cos(a)}' y2='{60 + 40 * math.sin(a)}' stroke='#f6c453' stroke-width='3' stroke-linecap='round'/>"
        for a in [i * math.pi / 4 for i in range(8)])
    # cama segura
    s += f"<ellipse cx='105' cy='265' rx='0' ry='0'/>"
    s += cao(345, 196, .55, CARAMELO, CARAMELO_E)
    marcadores = [(70, 232, "1"), (128, 252, "2"), (207, 216, "3"), (134, 130, "4"), (118, 176, "5"),
                  (260, 230, "6"), (390, 240, "7"), (491, 172, "8"), (230, 124, "9"), (440, 98, "10")]
    for x, y, n in marcadores:
        s += numero(x, y, n, L, 10)
    return svg(w, h, s)


def condicao_corporal():
    w, h = 520, 250
    s = ""
    perfis = [
        ("Muito magro", 16, 7, 12, R, "1–2 de 9"),
        ("Magro", 17, 10, 14, L, "3 de 9"),
        ("Ideal", 18, 13.5, 16, V, "4–5 de 9"),
        ("Sobrepeso", 20, 19, 19, L, "6–7 de 9"),
        ("Obeso", 23, 26, 23, R, "8–9 de 9"),
    ]
    for i, (nome, c, cin, q, cor, escala) in enumerate(perfis):
        cx = 52 + i * 104
        top = 22
        s += f"<rect x='{cx - 47}' y='8' width='94' height='232' rx='10' fill='{B}'/>"
        # orelhas e cabeça
        s += f"<ellipse cx='{cx - 11}' cy='{top + 14}' rx='5' ry='9' fill='{CARAMELO_E}' transform='rotate(25 {cx - 11} {top + 14})'/>"
        s += f"<ellipse cx='{cx + 11}' cy='{top + 14}' rx='5' ry='9' fill='{CARAMELO_E}' transform='rotate(-25 {cx + 11} {top + 14})'/>"
        pts = [(cx, top + 22), (cx + 8, top + 26), (cx + c, top + 50), (cx + cin, top + 92), (cx + q, top + 118),
               (cx + 7, top + 140), (cx, top + 144), (cx - 7, top + 140), (cx - q, top + 118), (cx - cin, top + 92),
               (cx - c, top + 50), (cx - 8, top + 26)]
        s += f"<path d='{suave(pts)}' fill='{CARAMELO}' stroke='{CARAMELO_E}' stroke-width='1.4'/>"
        s += f"<ellipse cx='{cx}' cy='{top + 12}' rx='11' ry='13' fill='{CARAMELO}' stroke='{CARAMELO_E}' stroke-width='1.4'/>"
        s += f"<ellipse cx='{cx}' cy='{top + 1}' rx='4' ry='3' fill='{T}'/>"
        s += f"<path d='M{cx} {top + 144} q-3 14 4 24' stroke='{CARAMELO_E}' stroke-width='4' fill='none' stroke-linecap='round'/>"
        if i == 0:
            for k in range(4):
                yy = top + 56 + k * 9
                s += f"<path d='M{cx - 12} {yy} q12 4 24 0' stroke='{CARAMELO_E}' stroke-width='1.3' fill='none'/>"
        if i == 2:
            s += f"<path d='M{cx - cin - 7} {top + 92} h-4 M{cx + cin + 7} {top + 92} h4' stroke='{V}' stroke-width='2'/>"
        s += f"<rect x='{cx - 40}' y='{top + 174}' width='80' height='18' rx='9' fill='{cor}'/>"
        s += txt(cx, top + 187, nome, 10, "#fff", 800)
        s += txt(cx, top + 208, escala, 9, T, 700)
    return svg(w, h, s)


def transicao():
    w, h = 520, 200
    fases = [("Dias 1–2", 25), ("Dias 3–4", 50), ("Dias 5–6", 75), ("Dia 7 em diante", 100)]
    s = ""
    for i, (rot, nova) in enumerate(fases):
        x = 30 + i * 122
        alt = 110
        s += f"<rect x='{x}' y='20' width='90' height='{alt}' rx='8' fill='{BM}'/>"
        hn = alt * nova / 100
        s += f"<rect x='{x}' y='{20 + alt - hn}' width='90' height='{hn}' rx='8' fill='{V}'/>"
        if nova < 100:
            s += txt(x + 45, 20 + (alt - hn) / 2 + 5, f"{100 - nova}% antiga", 10, VE, 800)
        s += txt(x + 45, 20 + alt - hn / 2 + 5, f"{nova}% nova", 10, "#fff", 800)
        s += txt(x + 45, 152, rot, 10.5, VE, 800)
        if i < 3:
            s += seta(x + 95, 75, x + 117, 75, L, 2)
    s += txt(w / 2, 184, "Exemplo de transição em cerca de 7 dias — o veterinário pode indicar um ritmo diferente.", 9.5, "#55645c", 600)
    return svg(w, h, s)


def vacinas_linha():
    w, h = 520, 210
    s = f"<line x1='30' y1='90' x2='500' y2='90' stroke='{VC}' stroke-width='6' stroke-linecap='round'/>"
    marcos = [
        (45, "6–8 sem.", ["1ª dose", "da série"], V),
        (140, "a cada 2–4 sem.", ["Doses", "repetidas"], V),
        (240, "16 sem. ou +", ["Última dose", "da série inicial"], L),
        (345, "26 sem. ou +", ["Revacinação", "(reforço)"], L),
        (455, "Depois", ["Reforços nos", "intervalos do vet"], VE),
    ]
    for x, topo, linhas, cor in marcos:
        s += f"<circle cx='{x}' cy='90' r='13' fill='{cor}' stroke='#fff' stroke-width='3'/>"
        s += f"<rect x='{x - 46}' y='34' width='92' height='22' rx='11' fill='{cor}'/>"
        s += txt(x, 49, topo, 9.5, "#fff", 800)
        s += multitxt(x, 124, linhas, 10, T, 700)
    s += txt(w / 2, 178, "Referência: diretrizes de vacinação da WSAVA (2024). O calendário do seu cão", 9.2, "#55645c", 600)
    s += txt(w / 2, 192, "deve ser definido pelo médico-veterinário, conforme região, risco e vacina utilizada.", 9.2, "#55645c", 600)
    return svg(w, h, s)


def desidratacao():
    w, h = 520, 260
    s = f"<rect width='{w}' height='{h}' rx='12' fill='{B}'/>"
    s += cao(90, 70, 2.0, CARAMELO, CARAMELO_E)
    rotulos = [
        (264, 94, 470, 40, "Olhos fundos ou opacos"),
        (292, 107, 470, 78, "Nariz seco, saliva espessa"),
        (278, 122, 470, 116, "Gengivas secas ou pegajosas"),
        (200, 118, 470, 154, "Pele demora a voltar"),
        (160, 194, 470, 192, "Apatia, fraqueza, pouca urina"),
    ]
    for x1, y1, x2, y2, t in rotulos:
        s += f"<circle cx='{x1}' cy='{y1}' r='4' fill='{L}'/>"
        s += f"<polyline points='{x1},{y1} {x2 - 120},{y2} {x2 - 112},{y2}' stroke='{L}' stroke-width='1.5' fill='none'/>"
        s += txt(x2 - 108, y2 + 4, t, 10.5, VE, 800, "start")
    s += txt(30, 240, "Sinais possíveis — só o médico-veterinário confirma desidratação e define o tratamento.", 9.6, "#55645c", 600, "start")
    return svg(w, h, s)


def asfalto():
    w, h = 520, 200
    s = f"<rect width='{w}' height='{h}' rx='12' fill='{B}'/>"
    s += f"<rect x='20' y='130' width='300' height='50' rx='6' fill='#4a4a4a'/>"
    for i in range(10):
        s += f"<rect x='{35 + i * 28}' y='152' width='14' height='4' fill='#f6c453'/>"
    # ondas de calor
    for i in range(4):
        x = 60 + i * 70
        s += f"<path d='M{x} 120 q-8 -12 0 -24 t0 -24' stroke='{L}' stroke-width='3' fill='none' stroke-linecap='round'/>"
    # mão
    s += (f"<g transform='translate(150,92)'><path d='M0 38 h70 q10 0 10 -8 v-6 q0 -6 -8 -6 h-8 v-14 q0 -6 -6 -6 q-6 0 -6 6 v-4 q0 -6 -6 -6 q-6 0 -6 6 v2 q0 -6 -6 -6 q-6 0 -6 6 v4 q0 -6 -6 -6 q-6 0 -6 6 v26 z' "
          f"fill='#f3c9a0' stroke='{LE}' stroke-width='1.6'/></g>")
    # relógio
    s += f"<circle cx='410' cy='92' r='52' fill='#fff' stroke='{L}' stroke-width='5'/>"
    s += f"<path d='M410 92 L410 52 A40 40 0 0 1 448 80 Z' fill='{LC}'/>"
    s += txt(410, 104, "7s", 34, LE, 800)
    s += txt(410, 172, "Mão encostada por 7 segundos.", 11, VE, 800)
    s += txt(410, 188, "Se incomodar, é quente para as patas.", 10, VE, 700)
    return svg(w, h, s)


def ciclo_carrapato():
    w, h = 520, 300
    s = f"<rect width='{w}' height='{h}' rx='12' fill='{B}'/>"
    cx, cy, r = 260, 142, 86
    s += f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='none' stroke='{VC}' stroke-width='4' stroke-dasharray='8 6'/>"
    s += cao(cx - 46, cy - 26, .9, CARAMELO, CARAMELO_E)
    fases = [("Ovos", "no ambiente", -90), ("Larva", "alimenta-se no cão", 0), ("Ninfa", "alimenta-se no cão", 90), ("Adulto", "suga sangue e se reproduz", 180)]
    for nome, desc, ang in fases:
        a = math.radians(ang)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        s += f"<circle cx='{x:.0f}' cy='{y:.0f}' r='20' fill='{VE}'/>"
        if nome == "Ovos":
            for k in range(5):
                s += f"<circle cx='{x - 8 + k * 4:.0f}' cy='{y + (k % 2) * 4 - 2:.0f}' r='2.4' fill='{LC}'/>"
        else:
            tam = {"Larva": 4, "Ninfa": 6, "Adulto": 8}[nome]
            s += f"<ellipse cx='{x:.0f}' cy='{y:.0f}' rx='{tam}' ry='{tam * 1.3}' fill='{L}'/>"
            for k in range(-1, 2):
                s += f"<path d='M{x - tam:.0f} {y + k * tam * .5:.0f} h-{tam * .8} M{x + tam:.0f} {y + k * tam * .5:.0f} h{tam * .8}' stroke='{L}' stroke-width='1.5'/>"
        ax = x + (34 if ang in (0,) else -34 if ang == 180 else 0)
        ay = y + (36 if ang == 90 else -38 if ang == -90 else 4)
        anc = "start" if ang == 0 else "end" if ang == 180 else "middle"
        if ang == 0:
            ax = x + 26
        if ang == 180:
            ax = x - 26
        s += txt(ax, ay, nome, 11.5, VE, 800, anc) + txt(ax, ay + 13, desc, 9, "#55645c", 600, anc)
    s += txt(w / 2, 290, "A maior parte do ciclo acontece no ambiente: tratar só o cão não basta.", 9.6, LE, 800)
    return svg(w, h, s)


def maca():
    w, h = 520, 200
    s = f"<rect width='{w}' height='{h}' rx='12' fill='{B}'/>"
    # opção tábua
    s += f"<rect x='30' y='110' width='200' height='16' rx='4' fill='{MADEIRA}' stroke='{MADEIRA_E}' stroke-width='1.5'/>"
    s += cao(60, 70, 1.4, CARAMELO, CARAMELO_E, deitado=True)
    s += f"<rect x='40' y='86' width='180' height='26' rx='6' fill='{VC}' opacity='.55'/>"
    for x in (90, 160):
        s += f"<rect x='{x}' y='84' width='10' height='44' fill='{L}' opacity='.9'/>"
    s += txt(130, 150, "Superfície firme (tábua, porta,", 10, VE, 800)
    s += txt(130, 163, "papelão grosso) + faixas largas", 10, VE, 800)
    # opção cobertor
    s += f"<path d='M290 120 q100 30 200 0 l-10 -30 q-90 20 -180 0 z' fill='{VC}' stroke='{V}' stroke-width='1.6'/>"
    s += cao(330, 58, 1.2, CARAMELO, CARAMELO_E, deitado=True)
    for x in (292, 488):
        s += f"<circle cx='{x}' cy='105' r='7' fill='#f3c9a0' stroke='{LE}'/>"
    s += txt(390, 150, "Cobertor esticado por duas", 10, VE, 800)
    s += txt(390, 163, "pessoas, mantendo o corpo alinhado", 10, VE, 800)
    s += txt(w / 2, 188, "Mova o animal o mínimo possível e mantenha coluna e pescoço apoiados.", 9.6, "#55645c", 600)
    return svg(w, h, s)


def carro_seguranca():
    w, h = 520, 230
    s = ""
    def carro(x, y):
        return (f"<g transform='translate({x},{y})'><path d='M5 60 v-18 l18 -26 h66 l26 26 h10 q8 0 8 8 v10 z' fill='#fff' stroke='{VE}' stroke-width='2.4'/>"
                f"<path d='M30 20 h22 v22 h-38 z M58 20 h28 l20 22 h-48 z' fill='{AGUA}' opacity='.45'/>"
                f"<circle cx='30' cy='62' r='11' fill='{T}'/><circle cx='100' cy='62' r='11' fill='{T}'/></g>")
    opcoes = [
        ("Caixa de transporte", "presa ao banco ou no assoalho", True, "caixa"),
        ("Peitoral + cinto pet", "no banco traseiro", True, "cinto"),
        ("Solto no colo", "ou com a cabeça para fora", False, "colo"),
    ]
    for i, (t1, t2, ok, tipo) in enumerate(opcoes):
        x = 12 + i * 170
        s += f"<rect x='{x}' y='6' width='158' height='218' rx='12' fill='{VP if ok else '#f9e1dd'}'/>"
        s += carro(x + 12, 40)
        if tipo == "caixa":
            s += f"<rect x='{x + 62}' y='64' width='36' height='26' rx='4' fill='{L}' stroke='{LE}' stroke-width='1.5'/>"
            s += f"<g stroke='{LE}'>" + "".join(f"<line x1='{x + 88 + k * 3}' y1='68' x2='{x + 88 + k * 3}' y2='86'/>" for k in range(3)) + "</g>"
        if tipo == "cinto":
            s += cao(x + 60, 58, .38, CARAMELO, CARAMELO_E)
            s += f"<line x1='{x + 80}' y1='72' x2='{x + 78}' y2='94' stroke='{R}' stroke-width='2.4'/>"
        if tipo == "colo":
            s += cao(x + 22, 52, .4, CARAMELO, CARAMELO_E)
        s += (ok_verde if ok else x_vermelho)(x + 140, 26, 11)
        s += txt(x + 79, 150, t1, 11, VE if ok else R, 800)
        s += txt(x + 79, 166, t2, 9.6, T, 600)
    s += txt(w / 2, 208, "", 9, T)
    return svg(w, h, s)


def unha():
    w, h = 520, 190
    s = f"<rect width='{w}' height='{h}' rx='12' fill='{B}'/>"
    # unha clara
    def garra(x, y, escura=False):
        cor = "#3a3a3a" if escura else "#f2ece4"
        g = f"<g transform='translate({x},{y})'>"
        g += f"<path d='M0 40 q0 -40 40 -40 q70 0 110 50 q-20 -6 -40 -6 h-110 z' fill='{cor}' stroke='{BE if not escura else T}' stroke-width='2'/>"
        if not escura:
            g += f"<path d='M4 38 q2 -28 34 -30 q30 0 46 22 q-14 8 -40 10 z' fill='#f2a7a7'/>"
        g += f"<rect x='-40' y='0' width='44' height='46' rx='10' fill='{CARAMELO}'/>"
        g += f"<line x1='{108 if not escura else 112}' y1='-6' x2='{100 if not escura else 104}' y2='56' stroke='{R}' stroke-width='2.4' stroke-dasharray='5 4'/>"
        return g + "</g>"
    s += garra(60, 40)
    s += garra(320, 40, True)
    s += txt(140, 130, "Unha clara: o sabugo (rosado)", 10.5, VE, 800)
    s += txt(140, 145, "é visível. Corte só a ponta.", 10.5, VE, 800)
    s += txt(395, 130, "Unha escura: o sabugo não aparece.", 10.5, VE, 800)
    s += txt(395, 145, "Corte pouquinho por vez.", 10.5, VE, 800)
    s += txt(w / 2, 176, "A linha tracejada vermelha mostra a região segura de corte, longe do sabugo.", 9.6, "#55645c", 600)
    return svg(w, h, s)


def identificacao():
    w, h = 520, 190
    s = f"<rect width='{w}' height='{h}' rx='12' fill='{B}'/>"
    s += f"<path d='M40 60 q110 70 220 0' stroke='{V}' stroke-width='14' fill='none' stroke-linecap='round'/>"
    s += f"<circle cx='150' cy='92' r='6' fill='none' stroke='{INOX_E}' stroke-width='3'/>"
    s += f"<path d='M150 98 l-34 10 v40 q34 22 68 0 v-40 z' fill='{L}' stroke='{LE}' stroke-width='2'/>"
    s += txt(150, 124, "NOME", 10, "#fff", 800) + txt(150, 138, "(00) 00000-0000", 8.6, "#fff", 700)
    s += txt(150, 178, "Coleira com plaquinha de identificação", 10, VE, 800)
    # microchip
    s += f"<rect x='330' y='70' width='120' height='34' rx='17' fill='#e9eef0' stroke='{INOX_E}' stroke-width='2'/>"
    s += f"<rect x='350' y='80' width='60' height='14' rx='3' fill='{VC}'/>"
    s += f"<g stroke='{V}' stroke-width='1.4'>" + "".join(f"<line x1='{356 + k * 8}' y1='80' x2='{356 + k * 8}' y2='94'/>" for k in range(7)) + "</g>"
    s += txt(390, 128, "Microchip: do tamanho aproximado", 10, VE, 800)
    s += txt(390, 142, "de um grão de arroz, aplicado", 10, VE, 800)
    s += txt(390, 156, "sob a pele pelo veterinário", 10, VE, 800)
    s += txt(390, 178, "(ilustração ampliada)", 9, "#55645c", 600)
    return svg(w, h, s)


# ------------------------- Projetos caseiros ------------------------
def projeto_bebedouro():
    w, h = 520, 420
    s = ""
    # 1 materiais
    c = f"<rect x='20' y='50' width='120' height='70' rx='6' fill='{MADEIRA}' stroke='{MADEIRA_E}' stroke-width='1.5'/>"
    c += f"<g stroke='{MADEIRA_E}' opacity='.5'><path d='M24 66 h110 M24 84 h110 M24 102 h110'/></g>"
    c += tigela(195, 112, 66, 22, INOX, INOX_E)
    c += f"<rect x='24' y='140' width='60' height='10' rx='3' fill='#555'/><circle cx='100' cy='145' r='8' fill='#555'/><circle cx='120' cy='145' r='8' fill='#555'/>"
    c += txt(160, 150, "pés de borracha", 9, T, 700, "start")
    c += txt(80, 175, "tábua de polietileno ou madeira maciça", 9, T, 600)
    c += txt(80, 187, "≈ 30 × 30 cm (cão médio), 15–18 mm", 9, LE, 800)
    s += painel(10, 10, 245, 200, 1, "Materiais", c)
    # 2 marcar
    c = f"<rect x='20' y='45' width='205' height='120' rx='8' fill='{MADEIRA}' stroke='{MADEIRA_E}' stroke-width='1.5'/>"
    c += f"<circle cx='122' cy='105' r='44' fill='none' stroke='{T}' stroke-width='1.6' stroke-dasharray='5 4'/>"
    c += f"<circle cx='122' cy='105' r='36' fill='none' stroke='{R}' stroke-width='2'/>"
    c += seta(170, 70, 152, 82, T, 1.2) + txt(176, 66, "aba", 9, T, 700, "start")
    c += txt(122, 186, "Trace o círculo ≈ 1 cm para dentro da aba", 9, VE, 800)
    s += painel(265, 10, 245, 200, 2, "Marque o encaixe", c)
    # 3 cortar e lixar
    c = f"<rect x='20' y='45' width='205' height='120' rx='22' fill='{MADEIRA}' stroke='{MADEIRA_E}' stroke-width='1.5'/>"
    c += f"<circle cx='122' cy='105' r='36' fill='{B}' stroke='{MADEIRA_E}' stroke-width='2'/>"
    c += f"<rect x='150' y='118' width='50' height='24' rx='4' fill='{L}' transform='rotate(-20 175 130)'/>"
    c += txt(122, 182, "Corte, lixe o furo e arredonde os cantos", 9, VE, 800)
    c += txt(122, 195, "(raio ≥ 2 cm). Sem farpas!", 9, LE, 800)
    s += painel(10, 220, 245, 200, 3, "Corte e acabamento", c)
    # 4 montar
    c = f"<path d='M30 140 L70 110 H210 L170 140 Z' fill='{MADEIRA}' stroke='{MADEIRA_E}' stroke-width='1.5'/>"
    c += f"<path d='M30 140 v10 h140 v-10 M170 150 l40 -30 v-10' fill='{MADEIRA_E}' stroke='{MADEIRA_E}'/>"
    c += f"<ellipse cx='120' cy='124' rx='34' ry='10' fill='{INOX_E}'/>"
    c += f"<ellipse cx='120' cy='122' rx='30' ry='8' fill='{AGUA}'/>"
    c += f"<rect x='36' y='150' width='12' height='6' rx='2' fill='#555'/><rect x='152' y='150' width='12' height='6' rx='2' fill='#555'/>"
    c += cao(150, 52, .5, CARAMELO, CARAMELO_E, olhar=-1)
    c += txt(122, 182, "Encaixe a tigela e cole os pés", 9, VE, 800)
    c += txt(122, 195, "antiderrapantes nos cantos", 9, VE, 800)
    s += painel(265, 220, 245, 200, 4, "Montagem final", c)
    return svg(w, h, s)


def projeto_comedouro():
    w, h = 520, 210
    s = ""
    c = f"<rect x='20' y='50' width='150' height='90' rx='12' fill='{INOX}' stroke='{INOX_E}' stroke-width='2'/>"
    for i in range(3):
        for j in range(2):
            c += f"<circle cx='{48 + i * 47}' cy='{75 + j * 42}' r='16' fill='{INOX_E}' opacity='.6'/>"
    c += f"<rect x='180' y='70' width='50' height='70' rx='6' fill='#555' opacity='.85'/>"
    c += txt(205, 160, "tapete", 9, T, 700) + txt(205, 171, "antiderrapante", 9, T, 700)
    c += txt(95, 160, "forma de inox", 9, T, 700) + txt(95, 171, "sem rebarbas", 9, T, 700)
    s += painel(10, 10, 245, 190, 1, "Materiais", c)
    c = f"<rect x='18' y='122' width='200' height='12' rx='4' fill='#555'/>"
    c += f"<rect x='28' y='60' width='180' height='62' rx='10' fill='{INOX}' stroke='{INOX_E}' stroke-width='2'/>"
    for i in range(4):
        cx = 56 + i * 41
        c += f"<ellipse cx='{cx}' cy='88' rx='15' ry='12' fill='{INOX_E}' opacity='.6'/>"
        for k in range(4):
            c += f"<circle cx='{cx - 6 + k * 4}' cy='{86 + (k % 2) * 4}' r='2.6' fill='{CARAMELO_E}'/>"
    c += txt(118, 160, "Distribua a porção da refeição", 9, VE, 800)
    c += txt(118, 173, "entre as cavidades e apoie no tapete", 9, VE, 800)
    s += painel(265, 10, 245, 190, 2, "Monte e sirva", c)
    return svg(w, h, s)


def projeto_gravidade():
    w, h = 520, 330
    s = f"<rect width='{w}' height='{h}' rx='12' fill='{B}'/>"
    # base e coluna
    s += f"<rect x='60' y='270' width='220' height='18' rx='4' fill='{MADEIRA}' stroke='{MADEIRA_E}' stroke-width='1.5'/>"
    s += f"<rect x='70' y='60' width='22' height='212' rx='3' fill='{MADEIRA}' stroke='{MADEIRA_E}' stroke-width='1.5'/>"
    # mão-francesa
    s += f"<path d='M92 250 L120 270 H92 Z' fill='{MADEIRA_E}'/>"
    # garrafão invertido
    s += f"<path d='M120 60 h90 q10 0 10 10 v120 q0 12 -12 18 l-22 10 v24 h-42 v-24 l-22 -10 q-12 -6 -12 -18 v-120 q0 -10 10 -10 z' fill='{AGUA}' opacity='.55' stroke='#5a9fc0' stroke-width='2'/>"
    s += f"<rect x='140' y='242' width='50' height='6' fill='#5a9fc0'/>"
    # faixas de fixação
    for y in (95, 165):
        s += f"<rect x='86' y='{y}' width='148' height='12' rx='4' fill='{L}' opacity='.9'/>"
    # tigela
    s += f"<path d='M100 268 L240 268 L226 246 L114 246 Z' fill='{INOX}' stroke='{INOX_E}' stroke-width='1.6'/>"
    s += f"<rect x='117' y='252' width='106' height='10' fill='{AGUA}'/>"
    # cotas
    s += cota(300, 248, 300, 262, "") + txt(306, 260, "1,5–2 cm", 9.5, LE, 800, "start")
    s += f"<line x1='190' y1='248' x2='300' y2='248' stroke='{LE}' stroke-dasharray='3 3'/><line x1='226' y1='262' x2='300' y2='262' stroke='{LE}' stroke-dasharray='3 3'/>"
    # legendas
    leg = [
        (81, 64, "Coluna de madeira parafusada à base"),
        (234, 120, "Recipiente de uso alimentar (PP ou PET), 2–5 L"),
        (234, 170, "Faixas largas de velcro ou abraçadeira com proteção"),
        (240, 256, "Tigela de inox larga e pesada"),
        (280, 280, "Base ≈ 35 × 35 cm, com pés de borracha"),
    ]
    xs = 340
    for i, (x, y, t) in enumerate(leg):
        ty = 40 + i * 50
        s += f"<circle cx='{x}' cy='{y}' r='3.5' fill='{VE}'/><polyline points='{x},{y} {xs - 8},{ty} {xs},{ty}' fill='none' stroke='{VE}' stroke-width='1'/>"
        s += bloco(xs + 4, ty + 4, t, 30, 9.8)
    s += txt(40, 316, "A água desce até cobrir a boca do recipiente e para: o nível se mantém sozinho.", 10, LE, 800, "start")
    return svg(w, h, s)


def projeto_elevado():
    w, h = 520, 300
    s = f"<rect width='{w}' height='{h}' rx='12' fill='{B}'/>"
    # vista frontal
    s += f"<rect x='40' y='90' width='230' height='22' rx='8' fill='{MADEIRA}' stroke='{MADEIRA_E}' stroke-width='1.5'/>"
    s += f"<rect x='52' y='112' width='20' height='120' rx='6' fill='{MADEIRA}' stroke='{MADEIRA_E}' stroke-width='1.5'/>"
    s += f"<rect x='238' y='112' width='20' height='120' rx='6' fill='{MADEIRA}' stroke='{MADEIRA_E}' stroke-width='1.5'/>"
    s += f"<rect x='72' y='200' width='166' height='14' rx='4' fill='{MADEIRA_E}'/>"
    s += f"<rect x='48' y='232' width='28' height='8' rx='3' fill='#555'/><rect x='234' y='232' width='28' height='8' rx='3' fill='#555'/>"
    s += tigela(105, 96, 54, 18, INOX, INOX_E, racao=True)
    s += tigela(205, 96, 54, 18, INOX, INOX_E, agua=True)
    s += f"<line x1='20' y1='240' x2='290' y2='240' stroke='{T}' stroke-width='1.5'/>"
    s += cota(26, 92, 26, 238, "altura ≈ cotovelo", LE, -2)
    s += txt(155, 268, "Vista frontal", 10.5, VE, 800)
    # vista superior
    s += f"<rect x='320' y='70' width='170' height='110' rx='18' fill='{MADEIRA}' stroke='{MADEIRA_E}' stroke-width='1.5'/>"
    s += f"<circle cx='370' cy='125' r='28' fill='{B}' stroke='{MADEIRA_E}' stroke-width='2'/><circle cx='440' cy='125' r='28' fill='{B}' stroke='{MADEIRA_E}' stroke-width='2'/>"
    s += cota(320, 196, 490, 196, "≈ 3 × diâmetro da tigela", LE)
    s += txt(405, 230, "Vista superior: cantos", 10.5, VE, 800) + txt(405, 245, "arredondados, furos lixados", 10.5, VE, 800)
    s += txt(260, 288, "Use apenas se o veterinário recomendar — veja o alerta sobre cães de peito profundo.", 9.6, R, 800)
    return svg(w, h, s)


def projeto_caminha():
    w, h = 520, 230
    s = ""
    c = f"<rect x='20' y='60' width='120' height='40' rx='6' fill='#f3e3a6' stroke='#c9b46a' stroke-width='1.5'/>"
    c += f"<g fill='#c9b46a' opacity='.6'>" + "".join(f"<circle cx='{30 + (k * 13) % 110}' cy='{70 + (k * 7) % 25}' r='1.6'/>" for k in range(22)) + "</g>"
    c += f"<rect x='150' y='56' width='80' height='60' rx='6' fill='{VC}' stroke='{V}' stroke-width='1.5'/>"
    c += f"<line x1='158' y1='110' x2='222' y2='110' stroke='{T}' stroke-width='2' stroke-dasharray='3 2'/>"
    c += txt(80, 125, "espuma ou manta", 9, T, 700) + txt(190, 135, "capa com zíper", 9, T, 700)
    c += txt(118, 165, "Tamanho: comprimento do cão deitado", 9, VE, 800) + txt(118, 178, "e esticado + ≈ 15 cm", 9, LE, 800)
    s += painel(10, 10, 245, 210, 1, "Materiais e medida", c)
    c = f"<ellipse cx='122' cy='118' rx='100' ry='42' fill='{V}'/>"
    c += f"<ellipse cx='122' cy='112' rx='76' ry='28' fill='{VC}'/>"
    c += cao(70, 66, .95, CARAMELO, CARAMELO_E, deitado=True)
    c += txt(122, 182, "Borda de manta enrolada apoia a cabeça;", 9, VE, 800)
    c += txt(122, 195, "a capa sai para lavar", 9, VE, 800)
    s += painel(265, 10, 245, 210, 2, "Montagem", c)
    return svg(w, h, s)


def projeto_brinquedos():
    w, h = 520, 420
    s = ""
    # corda trançada
    c = ""
    cores = [L, V, BE]
    for k in range(3):
        pts = " ".join(f"{40 + i * 14},{100 + 10 * math.sin(i * .9 + k * 2.1)}" for i in range(12))
        c += f"<polyline points='{pts}' stroke='{cores[k]}' stroke-width='9' fill='none' stroke-linecap='round'/>"
    c += f"<circle cx='34' cy='100' r='13' fill='{LE}'/><circle cx='200' cy='100' r='13' fill='{LE}'/>"
    c += txt(122, 150, "3 tiras largas de tecido de algodão", 9, VE, 800) + txt(122, 163, "trançadas bem apertado, nós nas pontas", 9, VE, 800)
    c += txt(122, 182, "Uso só com supervisão", 9, R, 800)
    s += painel(10, 10, 245, 200, 1, "Corda de cabo de guerra", c)
    # tapete de farejar
    c = f"<rect x='30' y='50' width='185' height='100' rx='8' fill='#555'/>"
    rnd = random.Random(4)
    for i in range(9):
        for j in range(5):
            cor = [L, V, VC, BE][rnd.randint(0, 3)]
            c += f"<path d='M{42 + i * 20} {62 + j * 19} q-5 -9 0 -14 M{42 + i * 20} {62 + j * 19} q5 -9 0 -14' stroke='{cor}' stroke-width='5' fill='none' stroke-linecap='round'/>"
    c += txt(122, 172, "Tiras de fleece amarradas em tapete vazado", 9, VE, 800)
    c += txt(122, 185, "de borracha; esconda petiscos", 9, VE, 800)
    s += painel(265, 10, 245, 200, 2, "Tapete de farejar", c)
    # toalha burrito
    c = f"<rect x='30' y='70' width='90' height='60' rx='4' fill='{VC}' stroke='{V}' stroke-width='1.5'/>"
    for k in range(5):
        c += f"<circle cx='{45 + k * 15}' cy='{100 + (k % 2) * 8}' r='3' fill='{CARAMELO_E}'/>"
    c += seta(126, 100, 146, 100, L, 2)
    c += f"<rect x='152' y='84' width='70' height='32' rx='16' fill='{VC}' stroke='{V}' stroke-width='1.5'/>"
    c += f"<path d='M168 84 v32 M206 84 v32' stroke='{V}' stroke-width='1.5'/>"
    c += txt(122, 160, "Espalhe petiscos numa toalha velha,", 9, VE, 800) + txt(122, 173, "enrole e dê um nó frouxo", 9, VE, 800)
    s += painel(10, 220, 245, 200, 3, "Toalha-surpresa", c)
    # caixa de forrageamento
    c = f"<path d='M50 80 L190 80 L200 140 L40 140 Z' fill='{MADEIRA}' stroke='{MADEIRA_E}' stroke-width='1.5'/>"
    c += f"<path d='M50 80 l-18 -22 M190 80 l18 -22' stroke='{MADEIRA_E}' stroke-width='5' stroke-linecap='round'/>"
    for k in range(7):
        c += f"<path d='M{60 + k * 20} 86 q8 -14 16 0 q-6 10 -16 0' fill='#fff' stroke='{BE}'/>"
    c += txt(122, 162, "Caixa de papelão sem grampos, fitas", 9, VE, 800) + txt(122, 175, "ou tinta, com papel amassado e petiscos", 9, VE, 800)
    s += painel(265, 220, 245, 200, 4, "Caixa de forrageamento", c)
    return svg(w, h, s)


def projeto_abrigo():
    w, h = 520, 360
    s = f"<rect width='{w}' height='{h}' rx='12' fill='{B}'/>"
    # árvore / sombra
    s += f"<rect x='40' y='150' width='14' height='140' fill='{MADEIRA_E}'/>"
    s += f"<circle cx='47' cy='120' r='48' fill='{VM}'/><circle cx='80' cy='140' r='34' fill='{V}'/>"
    s += f"<ellipse cx='190' cy='298' rx='160' ry='12' fill='{VE}' opacity='.18'/>"
    # pedrisco / drenagem
    s += f"<rect x='90' y='286' width='260' height='14' rx='4' fill='{BE}'/>"
    rnd = random.Random(2)
    for k in range(40):
        s += f"<circle cx='{95 + rnd.random() * 250:.0f}' cy='{289 + rnd.random() * 9:.0f}' r='{1.5 + rnd.random() * 1.6:.1f}' fill='{MADEIRA_E}'/>"
    # pés / piso elevado
    for x in (120, 300):
        s += f"<rect x='{x}' y='262' width='16' height='26' fill='{MADEIRA_E}'/>"
    s += f"<rect x='110' y='252' width='206' height='12' fill='{MADEIRA_E}'/>"
    # paredes
    s += f"<rect x='116' y='140' width='194' height='114' fill='{MADEIRA}' stroke='{MADEIRA_E}' stroke-width='2'/>"
    for y in range(152, 254, 14):
        s += f"<line x1='116' y1='{y}' x2='310' y2='{y}' stroke='{MADEIRA_E}' stroke-width='.8' opacity='.6'/>"
    # porta deslocada
    s += f"<path d='M232 254 v-62 q0 -20 22 -20 q22 0 22 20 v62 z' fill='#5b3d22'/>"
    # ventilação
    for k in range(4):
        s += f"<rect x='{136 + k * 16}' y='150' width='10' height='6' rx='2' fill='#5b3d22'/>"
    # telhado
    s += f"<path d='M96 146 L213 84 L330 146' fill='none' stroke='{VE}' stroke-width='14' stroke-linejoin='round' stroke-linecap='round'/>"
    s += f"<path d='M116 140 L213 92 L310 140 Z' fill='{MADEIRA}' stroke='{MADEIRA_E}'/>"
    # chuva e vento
    for k in range(6):
        s += f"<line x1='{140 + k * 30}' y1='30' x2='{132 + k * 30}' y2='52' stroke='#5a9fc0' stroke-width='2' stroke-linecap='round'/>"
    rotulos = [
        (213, 84, 40, "Telhado inclinado com beiral (≥ 10 cm) e manta térmica"),
        (160, 153, 96, "Aberturas de ventilação no alto das paredes"),
        (254, 200, 152, "Porta deslocada para um lado: canto protegido do vento"),
        (213, 258, 208, "Piso elevado 10–15 cm do chão"),
        (330, 293, 256, "Base de pedrisco ou leve inclinação para escoar a água"),
    ]
    for x, y, ty, t in rotulos:
        s += f"<circle cx='{x}' cy='{y}' r='4' fill='{L}'/><polyline points='{x},{y} 356,{ty} 364,{ty}' fill='none' stroke='{L}' stroke-width='1.2'/>"
        s += bloco(368, ty + 4, t, 27, 9.6)
    s += txt(30, 340, "Posicione o abrigo na sombra, com a porta fora da direção da chuva e do vento.", 10, LE, 800, "start")
    s += cao(150, 196, .55, CARAMELO, CARAMELO_E)
    return svg(w, h, s)


def gerar():
    SAIDA.mkdir(parents=True, exist_ok=True)
    arquivos = {
        "logo": logo(),
        "logo-claro": logo(VE, L, "#fff"),
        "casa-segura": casa_segura(),
        "condicao-corporal": condicao_corporal(),
        "transicao-alimentar": transicao(),
        "vacinas-linha": vacinas_linha(),
        "desidratacao": desidratacao(),
        "asfalto-7-segundos": asfalto(),
        "ciclo-carrapato": ciclo_carrapato(),
        "maca-improvisada": maca(),
        "carro-seguranca": carro_seguranca(),
        "unha-corte": unha(),
        "identificacao": identificacao(),
        "projeto1-bebedouro": projeto_bebedouro(),
        "projeto2-comedouro": projeto_comedouro(),
        "projeto3-gravidade": projeto_gravidade(),
        "projeto4-elevado": projeto_elevado(),
        "projeto5-caminha": projeto_caminha(),
        "projeto6-brinquedos": projeto_brinquedos(),
        "projeto7-abrigo": projeto_abrigo(),
    }
    for nome, conteudo in arquivos.items():
        (SAIDA / f"{nome}.svg").write_text(conteudo, encoding="utf-8")
    icones_dir = SAIDA / "icones"
    icones_dir.mkdir(exist_ok=True)
    for nome in ICONES:
        (icones_dir / f"{nome}.svg").write_text(icone(nome), encoding="utf-8")
    print(f"{len(arquivos)} ilustrações e {len(ICONES)} ícones gerados em {SAIDA}")


if __name__ == "__main__":
    gerar()
