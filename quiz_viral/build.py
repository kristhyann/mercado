#!/usr/bin/env python3
"""Gera 100_Temas_Quiz_Viral.pdf a partir dos arquivos em conteudo/*.txt.

Formato dos arquivos:
  ## Nome da seção | descrição
  @ Título do quiz | Nicho
  Pergunta | alternativa correta | errada | errada | errada | explicação (opcional)

A alternativa correta é sempre escrita em primeiro lugar; o script embaralha as
alternativas de forma determinística e equilibrada entre A, B, C e D.
"""
import html
import json
import random
import re
import subprocess
import sys
import unicodedata
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "conteudo"
OUT_DIR = ROOT / "saida"
OUT_DIR.mkdir(exist_ok=True)
HTML_PATH = OUT_DIR / "quiz.html"
PDF_PATH = ROOT.parent / "100_Temas_Quiz_Viral.pdf"
LETTERS = "ABCD"


# ---------------------------------------------------------------- parsing
def parse():
    sections, quizzes = [], []
    for f in sorted(CONTENT.glob("*.txt")):
        for ln, raw in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            line = raw.strip()
            if not line:
                continue
            where = f"{f.name}:{ln}"
            if line.startswith("## "):
                name, desc = [p.strip() for p in line[3:].split("|", 1)]
                sections.append({"name": name, "desc": desc, "quizzes": []})
            elif line.startswith("@ "):
                title, niche = [p.strip() for p in line[2:].split("|")]
                q = {"title": title, "niche": niche, "questions": [], "where": where}
                sections[-1]["quizzes"].append(q)
                quizzes.append(q)
            else:
                parts = [p.strip() for p in line.split("|")]
                if len(parts) not in (5, 6):
                    sys.exit(f"{where}: esperado 5 ou 6 campos, encontrado {len(parts)}")
                quizzes[-1]["questions"].append({
                    "q": parts[0],
                    "correct": parts[1],
                    "wrong": parts[2:5],
                    "expl": parts[5] if len(parts) == 6 else "",
                    "where": where,
                })
    for i, q in enumerate(quizzes, 1):
        q["num"] = i
    return sections, quizzes


# ---------------------------------------------------------------- validation
def norm(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9 ]+", "", s).strip()


def validate(sections, quizzes):
    errors = []
    if len(quizzes) != 100:
        errors.append(f"Total de quizzes = {len(quizzes)} (esperado 100)")
    niches = Counter(q["niche"] for q in quizzes)
    for n, c in niches.items():
        if c > 1:
            errors.append(f"Nicho repetido: {n} ({c}x)")
    titles = Counter(norm(q["title"]) for q in quizzes)
    for t, c in titles.items():
        if c > 1:
            errors.append(f"Título repetido: {t}")
    allq = []
    for qz in quizzes:
        if len(qz["questions"]) != 10:
            errors.append(f"{qz['where']} '{qz['title']}' tem {len(qz['questions'])} perguntas")
        for item in qz["questions"]:
            opts = [item["correct"], *item["wrong"]]
            if len({o.strip().lower() for o in opts}) != 4:
                errors.append(f"{item['where']}: alternativas repetidas {opts}")
            if any(not o for o in opts):
                errors.append(f"{item['where']}: alternativa vazia")
            allq.append((norm(item["q"]), item))
    # perguntas idênticas ou quase idênticas
    for i in range(len(allq)):
        a, ia = allq[i]
        for j in range(i + 1, len(allq)):
            b, ib = allq[j]
            if a == b:
                errors.append(f"Pergunta duplicada: {ia['where']} e {ib['where']}")
                continue
            sm = SequenceMatcher(None, a, b)
            if sm.real_quick_ratio() > 0.85 and sm.quick_ratio() > 0.85 and sm.ratio() > 0.85:
                # perguntas de formato fixo (ex.: "Qual é a forma correta?") são permitidas
                # quando as respostas são diferentes
                if norm(ia["correct"]) == norm(ib["correct"]):
                    errors.append(f"Perguntas muito parecidas: {ia['where']} / {ib['where']}")
    return errors


# ---------------------------------------------------------------- shuffling
NUM_RE = re.compile(r"^(\D*?)(-?\d[\d.]*(?:,\d+)?)(\D*)$")


def numeric_key(opts):
    """Se todas as alternativas forem números com o mesmo prefixo/sufixo, devolve chaves."""
    keys, affix = [], None
    for o in opts:
        m = NUM_RE.match(o)
        if not m:
            return None
        pre, num, suf = m.groups()
        if affix is None:
            affix = (pre, suf)
        elif affix != (pre, suf):
            return None
        keys.append(float(num.replace(".", "").replace(",", ".")))
    return keys


def arrange(quizzes, seed=2026):
    rng = random.Random(seed)
    for qz in quizzes:
        for attempt in range(500):
            targets = list("ABCDABCD") + rng.sample("ABCD", 2)
            rng.shuffle(targets)
            layout = []
            for item, tgt in zip(qz["questions"], targets):
                opts = [item["correct"], *item["wrong"]]
                keys = numeric_key(opts)
                if keys is not None:
                    order = sorted(range(4), key=lambda k: keys[k])
                    ordered = [opts[k] for k in order]
                    if abs(3 - ordered.index(item["correct"]) - LETTERS.index(tgt)) < abs(ordered.index(item["correct"]) - LETTERS.index(tgt)):
                        ordered.reverse()
                else:
                    wrong = item["wrong"][:]
                    rng.shuffle(wrong)
                    pos = LETTERS.index(tgt)
                    ordered = wrong[:pos] + [item["correct"]] + wrong[pos:]
                layout.append((ordered, LETTERS[ordered.index(item["correct"])]))
            answers = "".join(a for _, a in layout)
            counts = Counter(answers)
            no_runs = not re.search(r"(.)\1\1", answers)
            balanced = max(counts.values()) <= 4 and len(counts) == 4
            if no_runs and balanced:
                break
        for item, (ordered, ans) in zip(qz["questions"], layout):
            item["options"] = ordered
            item["answer"] = ans


# ---------------------------------------------------------------- html
def e(s):
    return html.escape(s, quote=True)


FONT_DIR = ROOT / "fonts"
FACES = "\n".join(
    f"@font-face {{ font-family: '{fam}'; font-weight: {w}; src: url('file://{FONT_DIR}/{f}.ttf') format('truetype'); }}"
    for fam, w, f in [
        ("QV", 400, "Inter-Regular"), ("QV", 500, "Inter-Medium"), ("QV", 600, "Inter-SemiBold"),
        ("QV", 700, "Inter-Bold"), ("QV", 800, "Inter-ExtraBold"), ("QV", 900, "Inter-Black"),
        ("QVD", 800, "InterDisplay-ExtraBold"), ("QVD", 900, "InterDisplay-Black"),
    ]
)

CSS = r"""
__FACES__
@page { size: 148mm 210mm; margin: 17mm 13mm 16mm 13mm;
  @top-left { content: "100 TEMAS DE QUIZ VIRAL"; font: 600 6.6pt 'QV'; letter-spacing: .14em; color: #9a97b5; vertical-align: bottom; padding-bottom: 3mm; }
  @bottom-center { content: counter(page); font: 600 7.5pt 'QV'; color: #6b6890; vertical-align: top; padding-top: 4mm; }
}
@page cover { margin: 0; @top-left { content: none } @top-right { content: none } @bottom-center { content: none } }
@page front { @top-right { content: none } }
__SECTION_PAGES__
:root {
  --ink: #1d1a3a; --muted: #6b6890; --line: #e6e3f3; --soft: #f5f3fc;
  --brand: #5b3df5; --brand-2: #8b5cf6; --accent: #ff4d6d; --ok: #0e9f6e; --ok-soft: #e8f7f0;
}
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin: 0; font-family: 'QV', sans-serif; color: var(--ink); font-size: 9.6pt; line-height: 1.42;
 }
h1, h2, h3 { font-family: 'QVD', 'QV', sans-serif; margin: 0; }
.marker { position: absolute; font-size: 2pt; color: #fff; line-height: 1; }

/* ---------- capa ---------- */
.cover { page: cover; width: 148mm; height: 210mm; position: relative; overflow: hidden; color: #fff;
  background: radial-gradient(120% 80% at 100% 0%, #8b5cf6 0%, rgba(139,92,246,0) 55%),
              radial-gradient(90% 70% at 0% 100%, #ff4d6d 0%, rgba(255,77,109,0) 55%),
              linear-gradient(160deg, #2a1b8f 0%, #1a1446 60%, #120e33 100%);
  padding: 20mm 15mm 16mm; display: flex; flex-direction: column; }
.cover .grid { position: absolute; inset: 0; opacity: .10;
  background-image: linear-gradient(#fff 1px, transparent 1px), linear-gradient(90deg, #fff 1px, transparent 1px);
  background-size: 9mm 9mm; }
.cover .tag { position: relative; display: inline-block; align-self: flex-start; border: 1px solid rgba(255,255,255,.45);
  border-radius: 99px; padding: 1.6mm 4mm; font-size: 7pt; font-weight: 700; letter-spacing: .16em; }
.cover .big { position: relative; margin-top: 18mm; font-family: 'QVD'; font-weight: 900; font-size: 92pt;
  line-height: .82; letter-spacing: -.04em; }
.cover .big span { color: #ffd166; }
.cover h1 { position: relative; font-weight: 900; font-size: 30pt; line-height: .98; letter-spacing: -.02em; margin-top: 3mm; }
.cover .sub { position: relative; margin-top: 7mm; font-size: 11.5pt; line-height: 1.38; font-weight: 500; max-width: 108mm; }
.cover .sub b { color: #ffd166; }
.cover .comp { position: relative; margin-top: 4mm; font-size: 8.6pt; color: rgba(255,255,255,.78); max-width: 108mm; }
.cover .bubbles { position: relative; margin-top: auto; display: grid; grid-template-columns: repeat(4, 1fr); gap: 2.4mm; }
.cover .bubbles div { background: rgba(255,255,255,.10); border: 1px solid rgba(255,255,255,.22); border-radius: 3mm;
  padding: 2.6mm 2mm; text-align: center; font-size: 6.8pt; font-weight: 600; }
.cover .bubbles b { display: block; font-size: 15pt; font-weight: 900; font-family: 'QVD'; color: #fff; }
.cover .plats { position: relative; margin-top: 5mm; font-size: 7pt; letter-spacing: .1em; font-weight: 700; color: rgba(255,255,255,.7); text-align: center; }

/* ---------- páginas iniciais ---------- */
.front { page: front; break-before: page; }
.kicker { font-size: 7pt; font-weight: 800; letter-spacing: .18em; color: var(--brand); text-transform: uppercase; }
.front h2 { font-size: 21pt; font-weight: 900; letter-spacing: -.02em; margin: 1.5mm 0 4mm; }
.front p { margin: 0 0 2.6mm; }
.howto { display: grid; gap: 2.6mm; margin-top: 4mm; }
.howto div { background: var(--soft); border-radius: 3mm; padding: 3mm 3.6mm; }
.howto b { color: var(--brand); }
.tips li { margin-bottom: 1.6mm; }
.toc-sec { break-inside: avoid; margin-top: 3.6mm; }
.toc-sec h3 { font-size: 8pt; font-weight: 800; text-transform: uppercase; letter-spacing: .08em; color: var(--brand);
  border-bottom: 1.4px solid var(--brand); padding-bottom: 1mm; margin-bottom: 1mm; display: flex; justify-content: space-between; }
.toc-row { display: flex; align-items: baseline; gap: 1.6mm; font-size: 8.1pt; padding: .55mm 0; color: var(--ink); text-decoration: none; }
.toc-row .n { font-weight: 800; color: var(--muted); width: 7mm; flex: none; }
.toc-row .t { flex: 0 1 auto; }
.toc-row .dots { flex: 1; border-bottom: 1px dotted #c9c5df; transform: translateY(-1mm); min-width: 4mm; }
.toc-row .p { font-weight: 700; flex: none; }

/* ---------- abertura de seção ---------- */
.sec { break-before: page; position: relative; min-height: 176mm; display: flex; flex-direction: column; }
.sec .num { font-family: 'QVD'; font-weight: 900; font-size: 64pt; line-height: 1; color: var(--soft);
  -webkit-text-stroke: 1.2px var(--brand); }
.sec h2 { font-size: 25pt; font-weight: 900; line-height: 1.02; letter-spacing: -.02em; margin-top: 2mm; }
.sec .bar { width: 18mm; height: 2.2mm; border-radius: 2mm; background: linear-gradient(90deg, var(--brand), var(--accent)); margin: 5mm 0 4mm; }
.sec p { font-size: 10.5pt; color: var(--muted); margin: 0; }
.sec ul { list-style: none; padding: 0; margin: 8mm 0 0; border-top: 1px solid var(--line); }
.sec li { padding: 2.2mm 0; border-bottom: 1px solid var(--line); display: flex; gap: 3mm; font-size: 9pt; }
.sec li b { color: var(--brand); width: 15mm; flex: none; }
.sec li span.niche { margin-left: auto; color: var(--muted); font-size: 7.4pt; text-align: right; }

/* ---------- quiz ---------- */
.quiz { break-before: page; position: relative; }
.qhead { border-radius: 4mm; padding: 4.2mm 4.6mm 4mm; color: #fff; margin-bottom: 4mm;
  background: linear-gradient(135deg, var(--brand) 0%, #3b25b8 100%); position: relative; overflow: hidden; }
.qhead::after { content: ""; position: absolute; right: -10mm; top: -12mm; width: 34mm; height: 34mm; border-radius: 50%;
  background: rgba(255,255,255,.08); }
.qhead .row { display: flex; justify-content: space-between; align-items: center; position: relative; }
.qhead .qn { font-size: 7.4pt; font-weight: 800; letter-spacing: .16em; }
.qhead .niche { font-size: 6.8pt; font-weight: 700; background: rgba(255,255,255,.18); padding: .9mm 2.6mm; border-radius: 99px; }
.qhead h2 { font-size: 15.5pt; font-weight: 900; line-height: 1.1; letter-spacing: -.01em; margin-top: 2mm; position: relative; }
.question { break-inside: avoid; border: 1px solid var(--line); border-radius: 3mm; padding: 2.8mm 3.2mm 3mm; margin-bottom: 2.6mm; }
.question .stem { display: flex; gap: 2.4mm; font-weight: 700; font-size: 9.8pt; line-height: 1.32; margin-bottom: 2.2mm; }
.question .stem .qnum { flex: none; width: 6mm; height: 6mm; border-radius: 50%; background: var(--ink); color: #fff;
  font-size: 7.4pt; font-weight: 800; display: flex; align-items: center; justify-content: center; margin-top: -.3mm; }
.opts { display: grid; grid-template-columns: 1fr; gap: 1.3mm; padding-left: 8.4mm; }
.opts.two { grid-template-columns: 1fr 1fr; }
.opt { display: flex; gap: 2mm; align-items: flex-start; font-size: 9pt; line-height: 1.3; }
.quiz.compact .qhead { padding: 3.4mm 4.2mm 3.2mm; margin-bottom: 3mm; }
.quiz.compact .qhead h2 { font-size: 14pt; margin-top: 1.4mm; }
.quiz.compact .question { padding: 2.2mm 3mm 2.3mm; margin-bottom: 2mm; }
.quiz.compact .question .stem { margin-bottom: 1.6mm; font-size: 9.5pt; }
.quiz.compact .opts { gap: .9mm; }
.quiz.compact .opt { font-size: 8.8pt; }
.quiz.tight .question { padding: 1.9mm 2.8mm 2mm; margin-bottom: 1.6mm; }
.quiz.tight .question .stem { font-size: 9.2pt; margin-bottom: 1.3mm; }
.quiz.tight .opt { font-size: 8.5pt; line-height: 1.22; }
.opt .l { flex: none; width: 4.6mm; height: 4.6mm; border-radius: 1.2mm; background: var(--soft); color: var(--brand);
  font-weight: 800; font-size: 7pt; display: flex; align-items: center; justify-content: center; margin-top: -.2mm; }

/* ---------- gabarito ---------- */
.key { break-before: page; }
.key .khead { display: flex; align-items: center; gap: 3mm; margin-bottom: 3.4mm; }
.key .badge { background: var(--ok); color: #fff; font-weight: 800; font-size: 7pt; letter-spacing: .14em; padding: 1.2mm 3mm; border-radius: 99px; }
.key .khead h3 { font-size: 11pt; font-weight: 800; }
.key .box { background: var(--ok-soft); border-radius: 3.4mm; padding: 2mm 3.6mm; }
.krow { display: flex; gap: 2.6mm; padding: 2mm 0; border-bottom: 1px solid rgba(14,159,110,.18); break-inside: avoid; font-size: 8.9pt; line-height: 1.35; }
.krow:last-child { border-bottom: none; }
.krow .kn { flex: none; width: 5mm; font-weight: 800; color: var(--muted); }
.krow .ka { flex: none; width: 5.6mm; height: 5.6mm; border-radius: 1.4mm; background: var(--ok); color: #fff; font-weight: 800;
  font-size: 8pt; display: flex; align-items: center; justify-content: center; margin-top: -.4mm; }
.krow .kt b { font-weight: 700; }
.krow .kt span { color: #3f5b52; }
.cta { margin-top: 4mm; border: 1.4px dashed #c9c5df; border-radius: 3mm; padding: 2.8mm 3.4mm; font-size: 8.2pt; color: var(--muted); break-inside: avoid; }
.cta b { color: var(--accent); }

/* ---------- final ---------- */
.end { break-before: page; page: front; text-align: center; padding-top: 40mm; }
.end .big { font-family: 'QVD'; font-weight: 900; font-size: 54pt; color: var(--brand); line-height: 1; }
.end h2 { font-size: 18pt; font-weight: 900; margin: 4mm 0; }
.end p { color: var(--muted); max-width: 100mm; margin: 0 auto 3mm; }
"""

CTAS = [
    "Peça para o público comentar quantas acertou de 10 — isso multiplica os comentários.",
    "Dê 5 segundos por pergunta com um cronômetro na tela: a contagem segura a retenção.",
    "Pergunte nos comentários qual foi a mais difícil e use a resposta no próximo vídeo.",
    "Revele o gabarito só no final ou numa parte 2 — curiosidade gera visualização completa.",
    "Desafie o público a marcar um amigo que acertaria tudo: é compartilhamento garantido.",
]


def build_html(sections, quizzes, pages=None, compact=(), tight=()):
    pages = pages or {}
    sec_css = []
    for si, s in enumerate(sections, 1):
        label = s["name"].upper().replace('"', "")
        sec_css.append(
            f'@page s{si} {{ @top-right {{ content: "{label}"; font: 600 6.6pt \'QV\'; '
            f"letter-spacing: .1em; color: #5b3df5; vertical-align: bottom; padding-bottom: 3mm; }} }}"
        )
    css = CSS.replace("__SECTION_PAGES__", "\n".join(sec_css)).replace("__FACES__", FACES)

    out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">',
           "<title>100 Temas de Quiz Viral</title>", f"<style>{css}</style></head><body>"]

    # capa
    out.append("""
<section class="cover"><div class="grid"></div>
  <div class="tag">COLEÇÃO PARA CRIADORES DE CONTEÚDO</div>
  <div class="big">100<span>.</span></div>
  <h1>TEMAS DE<br>QUIZ VIRAL</h1>
  <div class="sub"><b>1.000 perguntas</b> para criar vídeos, desafiar seguidores e aumentar o engajamento.</div>
  <div class="comp">Uma coleção de desafios para TikTok, Instagram Reels, YouTube Shorts e outras plataformas.</div>
  <div class="bubbles">
    <div><b>100</b>temas</div><div><b>1.000</b>perguntas</div><div><b>4.000</b>alternativas</div><div><b>100</b>gabaritos</div>
  </div>
  <div class="plats">TIKTOK · INSTAGRAM REELS · YOUTUBE SHORTS · FACEBOOK REELS</div>
</section>""")

    # como usar
    out.append("""
<section class="front">
  <div class="kicker">Antes de começar</div>
  <h2>Como usar este material</h2>
  <p>Cada um dos <b>100 quizzes</b> traz um tema, <b>10 perguntas</b> com <b>4 alternativas</b> e um <b>gabarito</b> com a resposta correta e, quando ajuda, uma explicação rápida para você narrar no vídeo.</p>
  <p>Os quizzes são independentes e misturam perguntas fáceis, médias e difíceis para manter o público tentando até o fim. Fatos sobre recordes e eventos recentes podem mudar: confira antes de publicar.</p>
  <div class="howto">
    <div><b>1. Escolha o tema</b> pelo índice ou pela categoria que combina com o seu público.</div>
    <div><b>2. Grave em blocos:</b> uma pergunta por tela, alternativas visíveis e um cronômetro de 3 a 5 segundos.</div>
    <div><b>3. Revele a resposta</b> logo depois ou deixe o gabarito para o final, aumentando a retenção.</div>
    <div><b>4. Chame para os comentários:</b> “Quantas você acertou?”, “Marca quem erraria a 7”.</div>
  </div>
  <div class="kicker" style="margin-top:6mm">Dicas de engajamento</div>
  <ul class="tips">
    <li>Comece pela pergunta mais curiosa do quiz para prender nos primeiros segundos.</li>
    <li>Transforme um quiz em série: perguntas 1–5 na parte 1 e 6–10 na parte 2.</li>
    <li>Use as explicações do gabarito como “fato curioso” na hora de revelar a resposta.</li>
  </ul>
</section>""")

    # índice
    out.append('<section class="front"><div class="kicker">Sumário</div><h2>Índice</h2>')
    for si, s in enumerate(sections, 1):
        sp = pages.get(f"S{si:02d}", "000")
        out.append(f'<div class="toc-sec"><h3><span>{si:02d} · {e(s["name"])}</span><span>{sp}</span></h3>')
        for q in s["quizzes"]:
            p = pages.get(f"Q{q['num']:03d}", "000")
            out.append(
                f'<a class="toc-row" href="#quiz{q["num"]:03d}"><span class="n">{q["num"]:02d}</span>'
                f'<span class="t">{e(q["title"])}</span><span class="dots"></span><span class="p">{p}</span></a>'
            )
        out.append("</div>")
    out.append("</section>")

    for si, s in enumerate(sections, 1):
        pg = f"s{si}"
        out.append(f'<section class="sec" style="page:{pg}" id="sec{si:02d}"><span class="marker">@@S{si:02d}@@</span>')
        out.append(f'<div class="num">{si:02d}</div><h2>{e(s["name"])}</h2><div class="bar"></div><p>{e(s["desc"])}</p><ul>')
        for q in s["quizzes"]:
            out.append(f'<li><b>Quiz {q["num"]:02d}</b><span>{e(q["title"])}</span><span class="niche">{e(q["niche"])}</span></li>')
        out.append("</ul></section>")
        for q in s["quizzes"]:
            n = q["num"]
            out.append(f'<section class="quiz{" compact" if n in compact else ""}{" tight" if n in tight else ""}" style="page:{pg}" id="quiz{n:03d}"><span class="marker">@@Q{n:03d}@@</span>')
            out.append(
                f'<div class="qhead"><div class="row"><span class="qn">QUIZ {n:02d}</span>'
                f'<span class="niche">Nicho: {e(q["niche"])}</span></div><h2>{e(q["title"])}</h2></div>'
            )
            for i, item in enumerate(q["questions"], 1):
                two = all(len(o) <= 24 for o in item["options"])
                opts = "".join(
                    f'<div class="opt"><span class="l">{L}</span><span>{e(o)}</span></div>'
                    for L, o in zip(LETTERS, item["options"])
                )
                out.append(
                    f'<div class="question"><div class="stem"><span class="qnum">{i}</span><span>{e(item["q"])}</span></div>'
                    f'<div class="opts{" two" if two else ""}">{opts}</div></div>'
                )
            out.append("</section>")
            out.append(f'<section class="key" style="page:{pg}"><div class="khead"><span class="badge">GABARITO</span>'
                       f'<h3>Quiz {n:02d} · {e(q["title"])}</h3></div><div class="box">')
            for i, item in enumerate(q["questions"], 1):
                ans = item["correct"].rstrip(".")
                expl = f' <span>{e(item["expl"])}</span>' if item["expl"] else ""
                out.append(
                    f'<div class="krow"><span class="kn">{i}.</span><span class="ka">{item["answer"]}</span>'
                    f'<span class="kt"><b>{e(ans)}.</b>{expl}</span></div>'
                )
            out.append(f'</div><div class="cta"><b>Dica para o vídeo:</b> {CTAS[(n - 1) % len(CTAS)]}</div></section>')

    out.append("""
<section class="end"><div class="big">1.000</div><h2>perguntas prontas para viralizar</h2>
<p>Agora é com você: escolha um tema, grave e desafie seus seguidores.</p>
<p>Quantas eles vão acertar? A resposta vai estar nos comentários.</p></section>""")
    out.append("</body></html>")
    return "\n".join(out)


# ---------------------------------------------------------------- pdf
def render(html_text):
    HTML_PATH.write_text(html_text, encoding="utf-8")
    js = f"""
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://{HTML_PATH}', {{ waitUntil: 'load' }});
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({{ path: {json.dumps(str(PDF_PATH))}, preferCSSPageSize: true, printBackground: true, outline: true, tagged: true }});
  await b.close();
}})();
"""
    subprocess.run(["node", "-e", js], check=True)


def pdf_text_pages():
    text = subprocess.run(["pdftotext", "-layout", str(PDF_PATH), "-"], check=True,
                          capture_output=True, text=True).stdout
    return text.split("\f")


def widowed_quizzes():
    """Quizzes cuja última página de perguntas tem só uma pergunta."""
    out, current = set(), None
    for page in pdf_text_pages():
        m = re.search(r"@@Q(\d+)@@", page)
        if m:
            current = int(m.group(1))
        lines = [l for l in page.splitlines() if l.strip()]
        if current and "GABARITO" not in page and len(lines) < 12 and re.match(r"\s*10\s", lines[1] if len(lines) > 1 else ""):
            out.add(current)
    return out


def find_pages():
    pages = {}
    for i, page in enumerate(pdf_text_pages(), 1):
        for m in re.findall(r"@@([QS]\d+)@@", page):
            pages.setdefault(m, i)
    return pages


def main():
    sections, quizzes = parse()
    errors = validate(sections, quizzes)
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    arrange(quizzes)
    dist = Counter(item["answer"] for q in quizzes for item in q["questions"])
    print("Distribuição de respostas:", dict(sorted(dist.items())))
    render(build_html(sections, quizzes))
    compact = widowed_quizzes()
    print("Quizzes compactados:", sorted(compact))
    render(build_html(sections, quizzes, compact=compact))
    tight = widowed_quizzes()
    if tight:
        print("Quizzes extra-compactados:", sorted(tight))
        render(build_html(sections, quizzes, compact=compact, tight=tight))
        left = widowed_quizzes()
        if left:
            print("ATENÇÃO: ainda com pergunta isolada:", sorted(left))
    pages = find_pages()
    render(build_html(sections, quizzes, pages, compact, tight))
    pages2 = find_pages()
    assert pages == pages2, "paginação mudou entre as passagens"
    (OUT_DIR / "gabarito.json").write_text(json.dumps(
        [{"quiz": q["num"], "titulo": q["title"], "respostas": "".join(i["answer"] for i in q["questions"])} for q in quizzes],
        ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"OK: {len(quizzes)} quizzes, {sum(len(q['questions']) for q in quizzes)} perguntas -> {PDF_PATH}")


if __name__ == "__main__":
    main()
