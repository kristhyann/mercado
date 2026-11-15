# Gera ebook.html (páginas A4 fixas) a partir dos dados. Depois: node pdf.js
import base64, html, os
from dados_a import CURIOSIDADES, PSICOLOGIA
from dados_b import CORPO, ANIMAIS, HUMOR
from dados_c import MISTERIOS, CIENCIA, ALERTAS, HISTORIAS

MARCA = '@olhaso_3D'
FONT = os.path.abspath('../videos/_kit/node_modules/@fontsource/poppins/files')
E = lambda s: html.escape(s, quote=False)
img64 = lambda f: 'data:image/jpeg;base64,' + base64.b64encode(open(f, 'rb').read()).decode()

ICON = {
 'luz': '<circle cx="12" cy="10" r="6"/><path d="M9 16h6v3H9z"/><path d="M10 21h4"/>',
 'mente': '<path d="M9 4a4 4 0 0 0-4 4 4 4 0 0 0-1 7 4 4 0 0 0 5 4h1V4z"/><path d="M15 4a4 4 0 0 1 4 4 4 4 0 0 1 1 7 4 4 0 0 1-5 4h-1V4z"/>',
 'corpo': '<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/><path d="M5 12h3l2-3 2 5 2-2h5"/>',
 'pata': '<circle cx="7" cy="8" r="2"/><circle cx="12" cy="6" r="2"/><circle cx="17" cy="8" r="2"/><path d="M8 17c0-3 2-5 4-5s4 2 4 5-2 3-4 3-4 0-4-3z"/>',
 'riso': '<circle cx="12" cy="12" r="9"/><path d="M8 14a5 5 0 0 0 8 0"/><circle cx="9" cy="9.5" r="1"/><circle cx="15" cy="9.5" r="1"/>',
 'misterio': '<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.8.4-1 1-1 1.7"/><circle cx="12" cy="17" r=".8"/>',
 'atomo': '<ellipse cx="12" cy="12" rx="10" ry="4"/><ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(120 12 12)"/><circle cx="12" cy="12" r="1.5"/>',
 'alerta': '<path d="M12 3l10 18H2z"/><path d="M12 10v5"/><circle cx="12" cy="18" r=".8"/>',
 'coracao': '<path d="M12 20s-8-5-8-11a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 9c0 6-8 11-8 11z"/>',
 'play': '<circle cx="12" cy="12" r="9"/><path d="M10 8l6 4-6 4z"/>',
}
def icon(k, size=28, col='currentColor'):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{col}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICON[k]}</svg>'

CATS = [
 ('Curiosidades surpreendentes', 'luz', '#FFC83D', CURIOSIDADES, 'Fatos do dia a dia que quase ninguém sabe explicar e que fazem o espectador dizer "nunca tinha pensado nisso".'),
 ('Psicologia e comportamento humano', 'mente', '#A78BFA', PSICOLOGIA, 'Por que a gente pensa, sente e age do jeito que age: temas de altíssima identificação.'),
 ('Corpo humano e saúde', 'corpo', '#FF6B8B', CORPO, 'O que acontece dentro de você, explicado de forma simples e responsável.'),
 ('Animais e natureza', 'pata', '#34D399', ANIMAIS, 'Bichos e fenômenos naturais incríveis, perfeitos para personagens 3D carismáticos.'),
 ('Humor e identificação', 'riso', '#FB923C', HUMOR, 'Situações engraçadas que todo mundo já viveu, com uma explicação curiosa por trás.'),
 ('Mistérios e fenômenos inexplicáveis', 'misterio', '#60A5FA', MISTERIOS, 'Enigmas famosos e o que a ciência já descobriu (ou ainda investiga) sobre eles.'),
 ('Ciência e tecnologia', 'atomo', '#22D3EE', CIENCIA, 'Como funcionam as tecnologias que você usa todos os dias.'),
 ('Alertas e perigos do cotidiano', 'alerta', '#F87171', ALERTAS, 'Informação útil que protege, sem sensacionalismo: o tipo de vídeo que as pessoas compartilham.'),
 ('Histórias emocionantes e reflexões', 'coracao', '#F472B6', HISTORIAS, 'Histórias reais e reflexões que tocam o coração e geram comentários.'),
]
TEMPOS = [('0–3 s', 'GANCHO', 'g'), ('3–8 s', 'IDENTIFICAÇÃO', 'i'), ('8–18 s', 'O PROBLEMA', 'p'), ('18–35 s', 'DESENVOLVIMENTO', 'd'), ('35–45 s', 'DESCOBERTA', 'c'), ('45–49 s', 'CTA', 'a')]

pages = []  # (html, numerada?)
def page(body, cls='', num=True, wm=True):
    pages.append((body, cls, num, wm))

# ---------- capa ----------
grid = ''.join(f'<div class="ci" style="background-image:url({img64(f"img/{x}.jpg")})"></div>' for x in 'abcd')
page(f'''
<div class="cover">
  <div class="cgrid">{grid}</div>
  <div class="cfade"></div>
  <div class="ctext">
    <div class="ckick">E-BOOK · BÔNUS EXCLUSIVO</div>
    <h1><span class="n100">100</span> IDEIAS DE<br>VÍDEOS VIRAIS</h1>
    <div class="csub">100 temas, ganchos poderosos e roteiros prontos para transformar curiosidade em conteúdo.</div>
    <div class="ctags"><span>Reels</span><span>TikTok</span><span>Shorts</span><span>IA + vídeos 3D</span></div>
    <div class="csign">{icon('play', 26, '#FFC83D')} Guia de Criação de Conteúdo com Inteligência Artificial</div>
  </div>
</div>''', 'pcover', num=False)

# ---------- como usar ----------
page(f'''
<div class="hd"><div class="kick">ANTES DE COMEÇAR</div><h2>Como usar este e-book</h2></div>
<p class="lead">Aqui estão <b>100 temas diferentes</b>, cada um pronto para virar um vídeo curto de cerca de <b>49 segundos</b> para Instagram Reels, TikTok e YouTube Shorts. Você pode gravar com a sua voz ou gerar a narração com inteligência artificial.</p>
<div class="howgrid">
  <div class="how"><b>1 · Título</b><span>O tema do vídeo, escrito para despertar curiosidade.</span></div>
  <div class="how"><b>2 · Gancho</b><span>A frase dos primeiros 3 segundos. Também vai escrita grande na tela.</span></div>
  <div class="how"><b>3 · Identificação</b><span>Faz o espectador pensar "isso acontece comigo".</span></div>
  <div class="how"><b>4 · Curiosidade ou problema</b><span>O que o vídeo vai explicar, em uma frase.</span></div>
  <div class="how"><b>5 · Roteiro de 49 s</b><span>Narração completa dividida em 6 blocos de tempo. É só copiar.</span></div>
  <div class="how"><b>6 · Ideia visual 3D</b><span>O que mostrar em cada bloco do roteiro.</span></div>
  <div class="how"><b>7 · CTA</b><span>A chamada final para comentar, compartilhar ou seguir.</span></div>
  <div class="how"><b>8 · Potencial</b><span>Por que o tema tende a gerar interesse.</span></div>
</div>
<div class="tipbox"><div class="tiph">A estrutura dos 49 segundos</div>
<div class="tl">{''.join(f'<div class="tlc"><b>{a}</b><span>{b}</span></div>' for a, b, _ in TEMPOS)}</div></div>
<div class="tips">
  <div><b>Ritmo da voz.</b> Os roteiros têm entre 110 e 160 palavras. Numa narração animada (cerca de 2,7 palavras por segundo), ficam perto de 49 s. Se passar, corte uma frase do desenvolvimento.</div>
  <div><b>Números por extenso.</b> Na hora de gerar a voz com IA, escreva os números por extenso para a pronúncia sair certa.</div>
  <div><b>Fatos com responsabilidade.</b> Os textos foram escritos com base em informações amplamente aceitas. Nos temas de saúde, eles não substituem a orientação de um profissional.</div>
  <div><b>Adapte ao seu estilo.</b> Troque palavras, use expressões da sua região e personalize o CTA com o nome da sua página.</div>
</div>''')

# ---------- numeração ----------
# capa(1) + como usar(2) + sumário(3,4) ; cada categoria: divisória + temas ; final + encerramento
start = 5; cat_pages = []; tema_pages = []; p = start
for c in CATS:
    cat_pages.append(p); p += 1
    tema_pages.append(list(range(p, p + len(c[3])))); p += len(c[3])
final_page = p

# ---------- sumário (2 páginas) ----------
n = 0; blocks = []
for ci, c in enumerate(CATS):
    items = ''
    for ti, d in enumerate(c[3]):
        n += 1
        items += f'<div class="si"><span class="sn" style="color:{c[2]}">{n:03d}</span><span class="st">{E(d["t"])}</span><span class="sp">{tema_pages[ci][ti]}</span></div>'
    blocks.append(f'<div class="sblock"><div class="sh" style="color:{c[2]}">{icon(c[1], 18, c[2])} {E(c[0])}<span>{len(c[3])} temas · p. {cat_pages[ci]}</span></div>{items}</div>')
half1 = blocks[:4]; half2 = blocks[4:]
page(f'<div class="hd"><div class="kick">SUMÁRIO</div><h2>Os 100 temas</h2></div><div class="sum">{"".join(half1)}</div>')
page(f'<div class="sum">{"".join(half2)}<div class="sblock"><div class="sh" style="color:#FFC83D">{icon("play", 18, "#FFC83D")} Como transformar qualquer tema em um vídeo 3D<span>p. {final_page}</span></div></div></div>')

# ---------- categorias e temas ----------
n = 0
for ci, (nome, ic, cor, lista, desc) in enumerate(CATS):
    page(f'''
<div class="div" style="--c:{cor}">
  <div class="dicon">{icon(ic, 120, cor)}</div>
  <div class="dnum">NICHO {ci + 1:02d}</div>
  <h2 class="dt">{E(nome)}</h2>
  <div class="dcount">{len(lista)} temas · do {n + 1:03d} ao {n + len(lista):03d}</div>
  <p class="ddesc">{E(desc)}</p>
</div>''', 'pdiv')
    for d in lista:
        n += 1
        rot = ''.join(f'<div class="rr"><div class="rt"><b>{a}</b><span>{b}</span></div><div class="rx">{E(d[k])}</div></div>' for a, b, k in TEMPOS)
        vis = ''.join(f'<li><b>{TEMPOS[j][0]}</b> {E(v)}</li>' for j, v in enumerate(d['v']))
        page(f'''
<div class="th" style="--c:{cor}">
  <div class="chip">{icon(ic, 16, cor)} {E(nome)}</div><div class="tn">TEMA <b>{n:03d}</b>/100</div>
</div>
<h3 class="tt">{E(d["t"])}</h3>
<div class="hook" style="--c:{cor}"><div class="hl">GANCHO · 0–3 s</div><div class="hx">“{E(d["g"])}”</div></div>
<div class="two">
  <div class="bx"><div class="bl" style="color:{cor}">IDENTIFICAÇÃO</div>{E(d["i"])}</div>
  <div class="bx"><div class="bl" style="color:{cor}">CURIOSIDADE OU PROBLEMA</div>{E(d["q"])}</div>
</div>
<div class="rot" style="--c:{cor}"><div class="rh">ROTEIRO COMPLETO · ~49 s <span>pronto para copiar</span></div>{rot}</div>
<div class="vis"><div class="rh2" style="color:{cor}">IDEIA VISUAL PARA VÍDEO 3D</div><ul>{vis}</ul></div>
<div class="two">
  <div class="bx cta" style="--c:{cor}"><div class="bl" style="color:{cor}">CTA</div>{E(d["a"])}</div>
  <div class="bx"><div class="bl" style="color:{cor}">POTENCIAL DE IDENTIFICAÇÃO</div>{E(d["pot"])}</div>
</div>''', 'ptema')

# ---------- final ----------
steps = [('Escolha um tema', 'Pegue um dos 100 temas, de preferência de um nicho em que você quer construir audiência.'),
 ('Copie o roteiro', 'Copie os 6 blocos do roteiro. Ajuste palavras para o seu jeito de falar.'),
 ('Abra o Claude Code', 'No computador, no navegador (claude.ai/code) ou no app do Claude no Android.'),
 ('Use a Skill de vídeos 3D', 'Escreva "quero fazer um vídeo", cole o roteiro e responda às perguntas: duração, voz e marca d\'água.'),
 ('Gere as cenas', 'O Claude monta as cenas 3D sincronizadas com cada frase, confere as imagens e corrige.'),
 ('Crie a narração', 'Gere a voz com IA (ElevenLabs, por exemplo) ou deixe o Claude gerar, e envie o áudio.'),
 ('Finalize e publique', 'Receba o vídeo, a capa e os títulos com hashtags para cada rede. Poste e acompanhe a retenção.')]
page(f'''
<div class="hd"><div class="kick">PASSO A PASSO</div><h2>Como transformar qualquer tema em um vídeo 3D</h2></div>
<div class="steps">{''.join(f'<div class="step"><div class="sn2">{i + 1}</div><div><b>{E(a)}</b><span>{E(b)}</span></div></div>' for i, (a, b) in enumerate(steps))}</div>
<div class="tipbox"><div class="tiph">Dica de ouro</div><div class="tipt">O gancho decide se a pessoa fica. Coloque a frase do gancho escrita grande na tela no primeiro segundo, mostre a coisa mais interessante logo no início e troque de cena a cada 3 segundos.</div></div>''')
page(f'''
<div class="end">
  <div class="eicon">{icon('play', 90, '#FFC83D')}</div>
  <h2>Agora é com você.</h2>
  <p>Escolha o primeiro tema, crie o seu vídeo e publique hoje.<br>Consistência transforma curiosidade em audiência.</p>
  <div class="ebrand">{E(MARCA)}</div>
  <div class="elegal">© Material exclusivo para alunos. É proibida a reprodução, revenda ou distribuição, total ou parcial, sem autorização.</div>
</div>''', 'pend')

# ---------- HTML ----------
css = open('estilo.css').read().replace('FONTDIR', 'file://' + FONT)
out = []
for i, (body, cls, num, wm) in enumerate(pages):
    pn = i + 1
    w = f'<div class="wm">{E(MARCA)}</div><div class="wm wm2">{E(MARCA)}</div>' if wm else ''
    f = f'<div class="ft"><span>100 Ideias de Vídeos Virais · {E(MARCA)} · Material exclusivo, proibida a reprodução</span><b>{pn}</b></div>' if num else ''
    out.append(f'<section class="page {cls}">{w}<div class="in">{body}</div>{f}</section>')
open('ebook.html', 'w').write(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>100 Ideias de Vídeos Virais</title><style>{css}</style></head><body>{"".join(out)}</body></html>')
print('páginas:', len(pages), '| temas:', n, '| página final:', final_page)
