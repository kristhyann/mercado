#!/usr/bin/env python3
"""Gera 100_Quizzes_Concursos_Publicos.pdf a partir de conteudo/*.txt.

Formato dos arquivos:
  ## Nome da disciplina | descrição
  @ Título do quiz | Disciplina | Nível
  Enunciado | alternativa correta | errada | errada | errada | explicação

A alternativa correta é sempre escrita primeiro; o script embaralha as
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
HTML_PATH = OUT_DIR / "concursos.html"
PDF_PATH = ROOT.parent / "100_Quizzes_Concursos_Publicos.pdf"
FONT_DIR = ROOT / "fonts"
LETTERS = "ABCD"
LEVELS = ("Fácil", "Médio", "Difícil")


# ------------------------------------------------------------------ parsing
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
                parts = [p.strip() for p in line[2:].split("|")]
                if len(parts) != 3:
                    sys.exit(f"{where}: cabeçalho de quiz inválido")
                title, disc, level = parts
                q = {"title": title, "disc": disc, "level": level, "questions": [], "where": where}
                sections[-1]["quizzes"].append(q)
                quizzes.append(q)
            else:
                parts = [p.strip() for p in line.split("|")]
                if len(parts) != 6:
                    sys.exit(f"{where}: esperado 6 campos, encontrado {len(parts)}")
                quizzes[-1]["questions"].append({
                    "q": parts[0], "correct": parts[1], "wrong": parts[2:5],
                    "expl": parts[5], "where": where,
                })
    for i, q in enumerate(quizzes, 1):
        q["num"] = i
    return sections, quizzes


# ------------------------------------------------------------------ validation
def norm(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9 ]+", "", s).strip()


def validate(sections, quizzes):
    errors = []
    if len(sections) != 19:
        errors.append(f"Disciplinas = {len(sections)} (esperado 19)")
    if len(quizzes) != 100:
        errors.append(f"Quizzes = {len(quizzes)} (esperado 100)")
    for s in sections:
        for q in s["quizzes"]:
            if q["disc"] != s["name"]:
                errors.append(f"{q['where']}: disciplina '{q['disc']}' fora da seção '{s['name']}'")
    if len({norm(q["title"]) for q in quizzes}) != len(quizzes):
        errors.append("Há títulos de quiz repetidos")
    allq = []
    for qz in quizzes:
        if qz["level"] not in LEVELS:
            errors.append(f"{qz['where']}: nível inválido '{qz['level']}'")
        if len(qz["questions"]) != 10:
            errors.append(f"{qz['where']} '{qz['title']}' tem {len(qz['questions'])} questões")
        for it in qz["questions"]:
            opts = [it["correct"], *it["wrong"]]
            if len({o.strip().lower() for o in opts}) != 4 or any(not o for o in opts):
                errors.append(f"{it['where']}: alternativas repetidas ou vazias")
            if len(it["expl"]) < 15:
                errors.append(f"{it['where']}: explicação ausente ou curta demais")
            allq.append((norm(it["q"]), it))
    for i in range(len(allq)):
        a, ia = allq[i]
        for j in range(i + 1, len(allq)):
            b, ib = allq[j]
            if a == b:
                errors.append(f"Enunciado duplicado: {ia['where']} e {ib['where']}")
                continue
            sm = SequenceMatcher(None, a, b)
            if sm.real_quick_ratio() > 0.8 and sm.quick_ratio() > 0.8 and sm.ratio() > 0.8:
                if norm(ia["correct"]) == norm(ib["correct"]):
                    errors.append(f"Questões muito parecidas: {ia['where']} / {ib['where']}")
    return errors


# ------------------------------------------------------------------ arrangement
NUM_RE = re.compile(r"^(\D*?)(-?\d[\d.]*(?:,\d+)?)(\D*)$")


def numeric_key(opts):
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


def arrange(quizzes, seed=144):
    rng = random.Random(seed)
    for qz in quizzes:
        for _ in range(1000):
            targets = list("ABCDABCD") + rng.sample("ABCD", 2)
            rng.shuffle(targets)
            layout = []
            for it, tgt in zip(qz["questions"], targets):
                opts = [it["correct"], *it["wrong"]]
                keys = numeric_key(opts)
                if keys is not None:
                    ordered = [opts[k] for k in sorted(range(4), key=lambda k: keys[k])]
                else:
                    wrong = it["wrong"][:]
                    rng.shuffle(wrong)
                    pos = LETTERS.index(tgt)
                    ordered = wrong[:pos] + [it["correct"]] + wrong[pos:]
                layout.append((ordered, LETTERS[ordered.index(it["correct"])]))
            answers = "".join(a for _, a in layout)
            c = Counter(answers)
            if not re.search(r"(.)\1\1", answers) and len(c) == 4 and max(c.values()) <= 4:
                break
        for it, (ordered, ans) in zip(qz["questions"], layout):
            it["options"], it["answer"] = ordered, ans


# ------------------------------------------------------------------ html
def e(s):
    return html.escape(s, quote=True)


FACES = "\n".join(
    f"@font-face {{ font-family: '{fam}'; font-weight: {w}; src: url('file://{FONT_DIR}/{f}.ttf') format('truetype'); }}"
    for fam, w, f in [
        ("QC", 400, "Inter-Regular"), ("QC", 500, "Inter-Medium"), ("QC", 600, "Inter-SemiBold"),
        ("QC", 700, "Inter-Bold"), ("QC", 800, "Inter-ExtraBold"), ("QC", 900, "Inter-Black"),
        ("QCD", 800, "InterDisplay-ExtraBold"), ("QCD", 900, "InterDisplay-Black"),
    ]
)

CSS = r"""
__FACES__
@page { size: 148mm 210mm; margin: 17mm 13mm 16mm 13mm;
  @top-left { content: "100 QUIZZES PARA CONCURSOS"; font: 700 6.4pt 'QC'; letter-spacing: .14em; color: #8a93a6; vertical-align: bottom; padding-bottom: 3mm; }
  @bottom-left { content: "Material de estudo · questões inéditas"; font: 500 6.2pt 'QC'; color: #a2a9b8; vertical-align: top; padding-top: 4mm; }
  @bottom-right { content: counter(page); font: 700 7.6pt 'QC'; color: #1f3a5f; vertical-align: top; padding-top: 4mm; }
}
@page cover { margin: 0; @top-left { content: none } @top-right { content: none } @bottom-left { content: none } @bottom-right { content: none } }
__SECTION_PAGES__
:root { --ink: #1b2433; --muted: #5f6b7e; --line: #dfe4ec; --soft: #f3f6fa; --navy: #1f3a5f; --navy-2: #2c5282;
  --gold: #c9a227; --teal: #0f766e; --teal-soft: #e7f5f3; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin: 0; font-family: 'QC', sans-serif; color: var(--ink); font-size: 9.4pt; line-height: 1.42; }
h1, h2, h3 { font-family: 'QCD', 'QC', sans-serif; margin: 0; }
.marker { position: absolute; font-size: 2pt; color: #fff; line-height: 1; }

/* capa */
.cover { page: cover; width: 148mm; height: 210mm; position: relative; overflow: hidden; color: #fff;
  background: linear-gradient(165deg, #1f3a5f 0%, #172c48 55%, #0f1f35 100%); padding: 18mm 14mm 14mm; display: flex; flex-direction: column; }
.cover .stripe { position: absolute; left: 0; top: 0; bottom: 0; width: 5mm; background: var(--gold); }
.cover .lines { position: absolute; inset: 0; opacity: .07;
  background-image: repeating-linear-gradient(0deg, #fff 0 1px, transparent 1px 7mm); }
.cover .tag { position: relative; align-self: flex-start; font-size: 6.8pt; font-weight: 800; letter-spacing: .18em; color: var(--gold);
  border-bottom: 1.2px solid var(--gold); padding-bottom: 1.4mm; }
.cover .big { position: relative; margin-top: 16mm; font-family: 'QCD'; font-weight: 900; font-size: 88pt; line-height: .82; letter-spacing: -.04em; }
.cover h1 { position: relative; font-weight: 900; font-size: 25pt; line-height: 1; letter-spacing: -.01em; margin-top: 3mm; }
.cover h1 span { color: var(--gold); }
.cover .sub { position: relative; margin-top: 7mm; font-size: 11pt; line-height: 1.4; font-weight: 500; max-width: 110mm; color: #e8edf5; }
.cover .comp { position: relative; margin-top: 6mm; display: inline-flex; align-self: flex-start; gap: 0; border: 1px solid rgba(255,255,255,.3); border-radius: 2mm; overflow: hidden; }
.cover .comp div { padding: 2.4mm 3.4mm; font-size: 7.6pt; font-weight: 700; letter-spacing: .04em; border-right: 1px solid rgba(255,255,255,.3); }
.cover .comp div:last-child { border-right: none; }
.cover .comp b { color: var(--gold); font-size: 10pt; margin-right: 1mm; }
.cover .disc { position: relative; margin-top: auto; display: flex; flex-wrap: wrap; gap: 1.4mm; }
.cover .disc span { font-size: 6pt; font-weight: 600; border: 1px solid rgba(255,255,255,.25); border-radius: 99px; padding: .8mm 2.2mm; color: #d6deea; }
.cover .foot { position: relative; margin-top: 5mm; font-size: 6.6pt; color: rgba(255,255,255,.6); letter-spacing: .06em; }

/* páginas iniciais */
.front { break-before: page; }
.kicker { font-size: 6.8pt; font-weight: 800; letter-spacing: .18em; color: var(--gold); text-transform: uppercase; }
.front h2 { font-size: 20pt; font-weight: 900; color: var(--navy); margin: 1.4mm 0 4mm; }
.front p { margin: 0 0 2.6mm; }
.steps { display: grid; gap: 2.2mm; margin: 3mm 0 4mm; }
.steps div { border-left: 2.4px solid var(--navy); background: var(--soft); padding: 2.4mm 3.2mm; border-radius: 0 2mm 2mm 0; font-size: 8.8pt; }
.steps b { color: var(--navy); }
.lv { display: inline-block; font-size: 6.6pt; font-weight: 800; letter-spacing: .06em; padding: .6mm 2mm; border-radius: 99px; text-transform: uppercase; vertical-align: 1px; }
.lv.f { background: #e3f4ea; color: #1b7a43; } .lv.m { background: #fdf1d8; color: #9a6a00; } .lv.d { background: #fde4e4; color: #b42318; }
.dist { width: 100%; border-collapse: collapse; font-size: 7.9pt; margin-top: 2mm; }
.dist td { padding: 1mm 1.2mm; border-bottom: 1px solid var(--line); }
.dist td.n { text-align: right; font-weight: 800; color: var(--navy); width: 10mm; }
.toc-sec { break-inside: avoid; margin-top: 3.2mm; }
.toc-sec h3 { font-size: 7.8pt; font-weight: 800; text-transform: uppercase; letter-spacing: .06em; color: #fff; background: var(--navy);
  padding: 1.2mm 2.4mm; border-radius: 1.4mm; display: flex; justify-content: space-between; }
.toc-row { display: flex; align-items: baseline; gap: 1.6mm; font-size: 7.9pt; padding: .7mm .6mm; color: var(--ink); text-decoration: none; border-bottom: 1px dotted #d3d9e3; }
.toc-row .n { font-weight: 800; color: var(--navy-2); width: 7mm; flex: none; }
.toc-row .t { flex: 1; }
.toc-row .lvs { flex: none; font-size: 6pt; font-weight: 700; color: var(--muted); width: 11mm; text-align: right; }
.toc-row .p { font-weight: 800; flex: none; width: 7mm; text-align: right; color: var(--navy); }

/* abertura de disciplina */
.sec { break-before: page; position: relative; min-height: 176mm; }
.sec .band { background: var(--navy); color: #fff; border-radius: 3mm; padding: 6mm 5mm 5.5mm; position: relative; overflow: hidden; }
.sec .band::after { content: ""; position: absolute; right: 0; top: 0; bottom: 0; width: 3mm; background: var(--gold); }
.sec .dn { font-size: 7pt; font-weight: 800; letter-spacing: .2em; color: var(--gold); }
.sec h2 { font-size: 21pt; font-weight: 900; line-height: 1.05; margin-top: 2mm; }
.sec p.d { margin: 4mm 0 0; font-size: 9.6pt; color: var(--muted); }
.sec .lbl { margin-top: 7mm; font-size: 7pt; font-weight: 800; letter-spacing: .16em; color: var(--navy); text-transform: uppercase; }
.sec ul { list-style: none; padding: 0; margin: 2mm 0 0; border-top: 1.4px solid var(--navy); }
.sec li { padding: 2.4mm 0; border-bottom: 1px solid var(--line); display: flex; gap: 3mm; align-items: baseline; font-size: 8.8pt; }
.sec li b { color: var(--navy-2); width: 14mm; flex: none; }
.sec li .t { flex: 1; }

/* quiz */
.quiz { break-before: page; position: relative; }
.qhead { border: 1.4px solid var(--navy); border-radius: 3mm; overflow: hidden; margin-bottom: 3.6mm; }
.qhead .top { background: var(--navy); color: #fff; display: flex; justify-content: space-between; align-items: center; padding: 1.8mm 3.6mm; }
.qhead .qn { font-size: 7.6pt; font-weight: 800; letter-spacing: .16em; }
.qhead .qn span { color: var(--gold); }
.qhead h2 { font-size: 13.6pt; font-weight: 900; line-height: 1.15; color: var(--navy); padding: 2.8mm 3.6mm 1.4mm; }
.qhead .meta { display: flex; gap: 2mm; align-items: center; padding: 0 3.6mm 2.8mm; font-size: 7.4pt; color: var(--muted); }
.qhead .meta b { color: var(--ink); }
.question { break-inside: avoid; border: 1px solid var(--line); border-left: 2.4px solid var(--navy-2); border-radius: 2mm; padding: 2.6mm 3.2mm 2.8mm; margin-bottom: 2.5mm; }
.question .qh { font-size: 6.8pt; font-weight: 800; letter-spacing: .12em; color: var(--navy-2); text-transform: uppercase; margin-bottom: 1mm; }
.question .stem { font-weight: 600; font-size: 9.4pt; line-height: 1.36; margin-bottom: 2mm; }
.opts { display: grid; grid-template-columns: 1fr; gap: 1.1mm; }
.opts.two { grid-template-columns: 1fr 1fr; }
.opt { display: flex; gap: 2mm; align-items: flex-start; font-size: 8.8pt; line-height: 1.3; padding: 1mm 1.6mm; background: var(--soft); border-radius: 1.4mm; }
.opt .l { flex: none; width: 4.6mm; height: 4.6mm; border-radius: 50%; border: 1.2px solid var(--navy-2); color: var(--navy-2);
  font-weight: 800; font-size: 6.8pt; display: flex; align-items: center; justify-content: center; margin-top: -.1mm; background: #fff; }
.quiz.compact .question { padding: 2.1mm 2.8mm 2.2mm; margin-bottom: 2mm; }
.quiz.compact .question .stem { margin-bottom: 1.5mm; font-size: 9.1pt; }
.quiz.compact .opts { gap: .8mm; }
.quiz.compact .opt { font-size: 8.5pt; padding: .7mm 1.4mm; }
.quiz.compact .qhead { margin-bottom: 2.8mm; }
.quiz.tight .question { padding: 1.8mm 2.6mm 1.9mm; margin-bottom: 1.6mm; }
.quiz.tight .question .qh { margin-bottom: .5mm; }
.quiz.tight .question .stem { font-size: 8.8pt; line-height: 1.28; margin-bottom: 1.2mm; }
.quiz.tight .opt { font-size: 8.2pt; line-height: 1.22; padding: .5mm 1.3mm; }

.quiz.xt .qhead h2 { font-size: 12pt; padding-top: 2mm; }
.quiz.xt .question { padding: 1.5mm 2.4mm 1.6mm; margin-bottom: 1.3mm; }
.quiz.xt .question .stem { font-size: 8.5pt; }
.quiz.xt .opt { font-size: 7.9pt; padding: .4mm 1.2mm; }
.quiz.xt .opts { gap: .5mm; }
/* gabarito */
.key { break-before: page; position: relative; }
.key .khead { display: flex; align-items: center; gap: 2.6mm; margin-bottom: 3mm; }
.key .badge { background: var(--teal); color: #fff; font-weight: 800; font-size: 7pt; letter-spacing: .14em; padding: 1.2mm 3mm; border-radius: 1.4mm; }
.key .khead h3 { font-size: 10pt; font-weight: 800; color: var(--navy); line-height: 1.2; }
.grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 1.4mm; margin-bottom: 4mm; }
.grid div { border: 1.2px solid var(--teal); border-radius: 1.6mm; display: flex; justify-content: space-between; align-items: center; padding: 1.2mm 2.2mm; font-size: 8.6pt; }
.grid div span { color: var(--muted); font-weight: 700; }
.grid div b { color: var(--teal); font-size: 10pt; font-weight: 900; }
.exh { font-size: 7pt; font-weight: 800; letter-spacing: .16em; color: var(--navy); margin: 0 0 1.6mm; text-transform: uppercase; }
.ex { break-inside: avoid; display: flex; gap: 2.4mm; padding: 1.9mm 0; border-bottom: 1px solid var(--line); font-size: 8.3pt; line-height: 1.38; }
.ex:last-child { border-bottom: none; }
.ex .k { flex: none; width: 9.5mm; font-weight: 900; color: var(--teal); }
.ex .t b { color: var(--ink); }
.ex .t span { color: #3c4757; }

.key.kc .ex { padding: 1.3mm 0; font-size: 7.9pt; line-height: 1.3; }
.key.kc .grid { margin-bottom: 3mm; }
.key.kc .khead { margin-bottom: 2.2mm; }
/* final */
.end { break-before: page; text-align: center; padding-top: 34mm; }
.end .big { font-family: 'QCD'; font-weight: 900; font-size: 50pt; color: var(--navy); line-height: 1; }
.end h2 { font-size: 16pt; font-weight: 900; color: var(--navy); margin: 3mm 0 5mm; }
.end p { color: var(--muted); max-width: 104mm; margin: 0 auto 3mm; }
.end .note { margin-top: 10mm; font-size: 7.6pt; border-top: 1px solid var(--line); padding-top: 4mm; }
"""

LV_CLASS = {"Fácil": "f", "Médio": "m", "Difícil": "d"}


def build_html(sections, quizzes, pages=None, compact=(), tight=(), kc=(), xt=()):
    pages = pages or {}
    sec_css = []
    for si, s in enumerate(sections, 1):
        label = s["name"].upper().replace('"', "")
        sec_css.append(f'@page s{si} {{ @top-right {{ content: "{label}"; font: 700 6.4pt \'QC\'; letter-spacing: .08em; '
                       f'color: #1f3a5f; vertical-align: bottom; padding-bottom: 3mm; }} }}')
    css = CSS.replace("__FACES__", FACES).replace("__SECTION_PAGES__", "\n".join(sec_css))
    out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">',
           "<title>100 Quizzes para Concursos Públicos</title>", f"<style>{css}</style></head><body>"]

    chips = "".join(f"<span>{e(s['name'])}</span>" for s in sections)
    out.append(f"""
<section class="cover"><div class="stripe"></div><div class="lines"></div>
  <div class="tag">MATERIAL PREPARATÓRIO · GUARDA MUNICIPAL E SEGURANÇA PÚBLICA</div>
  <div class="big">100</div>
  <h1>QUIZZES PARA<br><span>CONCURSOS</span></h1>
  <div class="sub">1.000 questões para testar seus conhecimentos e se preparar para concursos públicos.</div>
  <div class="comp"><div><b>19</b>disciplinas</div><div><b>100</b>desafios</div><div><b>1.000</b>questões</div></div>
  <div class="disc">{chips}</div>
  <div class="foot">Questões inéditas com gabarito comentado · Legislação revisada até 2025</div>
</section>""")

    lv_count = Counter(q["level"] for q in quizzes)
    rows = "".join(
        f'<tr><td>{si:02d} · {e(s["name"])}</td><td class="n">{len(s["quizzes"])}</td></tr>'
        for si, s in enumerate(sections, 1)
    )
    out.append(f"""
<section class="front">
  <div class="kicker">Antes de começar</div>
  <h2>Como usar este material</h2>
  <p>São <b>100 quizzes</b> com <b>10 questões</b> cada, todas com quatro alternativas e apenas uma correta. Ao final de cada quiz há um <b>gabarito</b> em página separada, seguido das <b>explicações</b> com o fundamento legal ou conceitual.</p>
  <div class="steps">
    <div><b>1. Resolva sem consultar.</b> Marque suas respostas antes de virar a página do gabarito.</div>
    <div><b>2. Confira e leia as explicações</b>, inclusive das questões que acertou: elas trazem artigos e súmulas.</div>
    <div><b>3. Revise os erros</b> voltando à lei seca indicada na explicação.</div>
  </div>
  <p>Cada quiz indica a disciplina e o nível: <span class="lv f">Fácil</span> <span class="lv m">Médio</span> <span class="lv d">Difícil</span>. São {lv_count['Fácil']} quizzes fáceis, {lv_count['Médio']} médios e {lv_count['Difícil']} difíceis. Dentro de cada quiz, as questões também variam de dificuldade.</p>
  <p style="font-size:8pt;color:var(--muted)">As questões são inéditas, inspiradas no estilo das bancas, e consideram a legislação e a jurisprudência vigentes até 2025. Leis mudam: antes da prova, confira o texto atualizado exigido no seu edital.</p>
</section>
<section class="front">
  <div class="kicker">Distribuição</div>
  <h2>Quizzes por disciplina</h2>
  <p>As disciplinas mais cobradas nos concursos de Guarda Municipal e da área de segurança pública receberam mais quizzes.</p>
  <table class="dist">{rows}<tr><td><b>Total</b></td><td class="n">{len(quizzes)}</td></tr></table>
</section>""")

    out.append('<section class="front"><div class="kicker">Sumário</div><h2>Índice</h2>')
    for si, s in enumerate(sections, 1):
        sp = pages.get(f"S{si:02d}", "000")
        out.append(f'<div class="toc-sec"><h3><span>{si:02d} · {e(s["name"])}</span><span>{sp}</span></h3>')
        for q in s["quizzes"]:
            p = pages.get(f"Q{q['num']:03d}", "000")
            out.append(f'<a class="toc-row" href="#quiz{q["num"]:03d}"><span class="n">{q["num"]:02d}</span>'
                       f'<span class="t">{e(q["title"])}</span><span class="lvs">{q["level"]}</span><span class="p">{p}</span></a>')
        out.append("</div>")
    out.append("</section>")

    for si, s in enumerate(sections, 1):
        pg = f"s{si}"
        out.append(f'<section class="sec" style="page:{pg}"><span class="marker">@@S{si:02d}@@</span>'
                   f'<div class="band"><div class="dn">DISCIPLINA {si:02d}</div><h2>{e(s["name"])}</h2></div>'
                   f'<p class="d">{e(s["desc"])}</p><div class="lbl">Quizzes desta disciplina</div><ul>')
        for q in s["quizzes"]:
            out.append(f'<li><b>Quiz {q["num"]:02d}</b><span class="t">{e(q["title"])}</span>'
                       f'<span class="lv {LV_CLASS[q["level"]]}">{q["level"]}</span></li>')
        out.append("</ul></section>")
        for q in s["quizzes"]:
            n = q["num"]
            cls = "quiz" + (" compact" if n in compact else "") + (" tight" if n in tight else "") + (" xt" if n in xt else "")
            out.append(f'<section class="{cls}" style="page:{pg}" id="quiz{n:03d}"><span class="marker">@@Q{n:03d}@@</span>'
                       f'<div class="qhead"><div class="top"><span class="qn">QUIZ <span>{n:02d}</span></span>'
                       f'<span class="lv {LV_CLASS[q["level"]]}">{q["level"]}</span></div>'
                       f'<h2>{e(q["title"])}</h2><div class="meta">Disciplina: <b>{e(q["disc"])}</b></div></div>')
            for i, it in enumerate(q["questions"], 1):
                two = all(len(o) <= 22 for o in it["options"])
                opts = "".join(f'<div class="opt"><span class="l">{L}</span><span>{e(o)}</span></div>'
                               for L, o in zip(LETTERS, it["options"]))
                out.append(f'<div class="question"><div class="qh">Questão {i}</div><div class="stem">{e(it["q"])}</div>'
                           f'<div class="opts{" two" if two else ""}">{opts}</div></div>')
            out.append("</section>")
            grid = "".join(f"<div><span>{i}.</span><b>{it['answer']}</b></div>" for i, it in enumerate(q["questions"], 1))
            out.append(f'<section class="key{" kc" if n in kc else ""}" style="page:{pg}"><span class="marker">@@K{n:03d}@@</span>'
                       f'<div class="khead"><span class="badge">GABARITO</span><h3>Quiz {n:02d} · {e(q["title"])}</h3></div>'
                       f'<div class="grid">{grid}</div><div class="exh">Explicações</div>')
            for i, it in enumerate(q["questions"], 1):
                out.append(f'<div class="ex"><span class="k">{i}. {it["answer"]}</span><span class="t">'
                           f'<b>{e(it["correct"].rstrip("."))}.</b> <span>{e(it["expl"])}</span></span></div>')
            out.append("</section>")

    out.append("""
<section class="end" style="position:relative"><span class="marker">@@END@@</span><div class="big">1.000</div><h2>questões resolvidas. Parabéns!</h2>
<p>Volte aos quizzes em que errou mais, releia a lei seca indicada nas explicações e refaça as questões depois de alguns dias.</p>
<p>Constância vence talento. Bons estudos e boa prova!</p>
<p class="note">Material de estudo com questões inéditas. Não substitui a leitura da legislação atualizada nem do edital do concurso.</p></section>""")
    out.append("</body></html>")
    return "\n".join(out)


# ------------------------------------------------------------------ pdf
def render(text):
    HTML_PATH.write_text(text, encoding="utf-8")
    js = f"""
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://{HTML_PATH}', {{ waitUntil: 'load' }});
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({{ path: {json.dumps(str(PDF_PATH))}, preferCSSPageSize: true, printBackground: true, outline: true, tagged: true }});
  await b.close();
}})();"""
    subprocess.run(["node", "-e", js], check=True)


def pdf_pages():
    txt = subprocess.run(["pdftotext", "-layout", str(PDF_PATH), "-"], check=True, capture_output=True, text=True).stdout
    return txt.split("\f")


def find_pages():
    pages = {}
    for i, page in enumerate(pdf_pages(), 1):
        for m in re.findall(r"@@([QSK]\d+)@@", page):
            pages.setdefault(m, i)
    return pages


def widowed():
    """Quizzes cuja última página de questões traz só uma questão."""
    out, current = set(), None
    for page in pdf_pages():
        m = re.search(r"@@Q(\d+)@@", page)
        if m:
            current = int(m.group(1))
        if current is None or re.search(r"@@(?:[QSK]\d+|END)@@", page):
            continue
        if len(QRE.findall(page)) == 1:
            out.add(current)
    return out


QRE = re.compile(r"Q\s*U\s*E\s*S\s*T\s*Ã\s*O\s+\d")


def key_overflow():
    """Quizzes cujo gabarito transborda para outra página com até duas explicações."""
    out, current = set(), None
    for page in pdf_pages():
        m = re.search(r"@@K(\d+)@@", page)
        if m:
            current = int(m.group(1))
            continue
        if re.search(r"@@(?:[QSK]\d+|END)@@", page):
            current = None
            continue
        if current and len(re.findall(r"^\s*\d+\.\s+[ABCD]\s", page, re.M)) <= 2:
            out.add(current)
    return out


def main():
    sections, quizzes = parse()
    errors = validate(sections, quizzes)
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    arrange(quizzes)
    dist = Counter(it["answer"] for q in quizzes for it in q["questions"])
    print("Distribuição do gabarito:", dict(sorted(dist.items())))
    render(build_html(sections, quizzes))
    kc = key_overflow()
    print("Gabaritos compactados:", sorted(kc))
    compact = widowed()
    print("Compactados:", sorted(compact))
    tight, xt = set(), set()
    if compact:
        render(build_html(sections, quizzes, compact=compact, kc=kc))
        tight = widowed()
        if tight:
            print("Extra-compactados:", sorted(tight))
            render(build_html(sections, quizzes, compact=compact, tight=tight, kc=kc))
            xt = widowed()
            if xt:
                print("Compactação máxima:", sorted(xt))
                render(build_html(sections, quizzes, compact=compact, tight=tight | xt, kc=kc, xt=xt))
                left = widowed()
                if left:
                    print("ATENÇÃO: questão isolada em:", sorted(left))
    left_k = key_overflow()
    if left_k:
        print("ATENÇÃO: gabarito ainda transbordando:", sorted(left_k))
    pages = find_pages()
    render(build_html(sections, quizzes, pages, compact, tight | xt, kc, xt))
    assert find_pages() == pages, "paginação mudou entre as passagens"
    (OUT_DIR / "gabarito.json").write_text(json.dumps(
        [{"quiz": q["num"], "disciplina": q["disc"], "nivel": q["level"],
          "respostas": "".join(it["answer"] for it in q["questions"])} for q in quizzes],
        ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"OK: {len(sections)} disciplinas, {len(quizzes)} quizzes, "
          f"{sum(len(q['questions']) for q in quizzes)} questões -> {PDF_PATH}")


if __name__ == "__main__":
    main()
