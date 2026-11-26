#!/usr/bin/env python3
"""Gera 100_Quizzes_Virais_Concursos.pdf.

Fontes de conteúdo:
  - ../quiz_concursos/conteudo/*.txt  (quizzes reaproveitados, buscados pelo título)
  - novos/*.txt                         (quizzes inéditos deste material)
  - meta1.txt, meta2.txt, meta3.txt     (tema, gancho, título do vídeo, questão 11,
                                         hashtags e cenário de cada quiz, na ordem final)

Formato das questões: Enunciado | correta | errada | errada | errada | explicação
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
OLD = ROOT.parent / "quiz_concursos" / "conteudo"
NEW = ROOT / "novos"
OUT = ROOT / "saida"
OUT.mkdir(exist_ok=True)
HTML_PATH = OUT / "virais.html"
PDF_PATH = ROOT.parent / "100_Quizzes_Virais_Concursos.pdf"
FONT_DIR = ROOT / "fonts"
LETTERS = "ABCD"
LEVELS = ("Fácil", "Médio", "Difícil")

DISCIPLINES = [
    ("Direito Constitucional", "Fundamentos da República, competências, processo legislativo, direitos individuais e remédios constitucionais."),
    ("Direito Administrativo", "Princípios, organização administrativa, poder de polícia, atos administrativos e regime disciplinar."),
    ("Direito Penal — Parte Geral", "Fato típico, dolo e culpa, excludentes de ilicitude, culpabilidade, concurso de pessoas e penas."),
    ("Direito Penal — Parte Especial", "Crimes contra a vida, a honra e o patrimônio, e crimes contra a Administração Pública."),
    ("Direito Processual Penal", "Inquérito policial, ação penal, prisões cautelares, liberdade provisória e provas."),
    ("Direitos Humanos", "Características e dimensões, sistemas global e interamericano e uso da força pelos agentes de segurança."),
    ("Legislação de Guardas Municipais — Lei nº 13.022/2014", "O Estatuto Geral das Guardas Municipais artigo por artigo."),
    ("Legislação Municipal", "Regras gerais que valem para todos os Municípios. Leis orgânicas, estatutos e códigos variam de cidade para cidade: as questões indicam quando o tema depende da legislação local."),
    ("Código de Trânsito Brasileiro (CTB)", "Circulação, sinalização, habilitação, infrações, penalidades e crimes de trânsito."),
    ("Língua Portuguesa", "Ortografia, concordância, regência, crase, pontuação e semântica."),
    ("Informática", "Hardware, sistemas operacionais, internet, segurança da informação e pacotes de escritório."),
    ("Matemática", "Operações, equações, geometria, estatística, probabilidade e porcentagem."),
    ("Raciocínio Lógico", "Proposições, negações, sequências, argumentação e problemas de lógica."),
    ("Administração Pública", "Arts. 37 a 41 da Constituição: concurso, cargos, remuneração, acumulação, responsabilidade e estabilidade."),
    ("Ética no Serviço Público", "Código de Ética do servidor, comissões de ética, improbidade, transparência e anticorrupção."),
    ("Atualidades", "Fatos verificáveis de 2023 a 2026. Cada questão indica a referência temporal."),
    ("Conhecimentos Gerais", "Símbolos nacionais, ciência, organismos internacionais, cultura e instituições brasileiras."),
    ("Geografia e História do Brasil", "Colônia, Império, República, geografia física e população."),
    ("Noções de Segurança Pública", "Art. 144 da Constituição, órgãos de segurança, jurisprudência sobre guardas municipais e SUSP."),
    ("Criminologia", "Conceito e objeto, escolas criminológicas, teorias sociológicas, vitimologia e prevenção."),
]


# ------------------------------------------------------------------ leitura
def read_quiz_blocks(folder):
    """Devolve {título: {'level':..., 'questions':[...]}} de todos os .txt da pasta."""
    blocks, cur = {}, None
    for f in sorted(folder.glob("*.txt")):
        for ln, raw in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith("## "):
                continue
            if line.startswith("@ "):
                title, _disc, level = [p.strip() for p in line[2:].split("|")]
                cur = blocks[title] = {"level": level, "questions": [], "src": f"{f.name}:{ln}"}
                continue
            parts = [p.strip() for p in line.split("|")]
            if len(parts) != 6:
                sys.exit(f"{f.name}:{ln}: esperado 6 campos, encontrado {len(parts)}")
            cur["questions"].append({"q": parts[0], "correct": parts[1], "wrong": parts[2:5],
                                     "expl": parts[5], "where": f"{f.name}:{ln}"})
    return blocks


def read_meta():
    metas, cur = [], None
    for name in ("meta1.txt", "meta2.txt", "meta3.txt"):
        for raw in (ROOT / name).read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line:
                continue
            if line.startswith("= "):
                cur = {"title": line[2:].strip()}
                metas.append(cur)
            else:
                k, v = line.split(":", 1)
                cur[k.strip()] = v.strip()
    return metas


def load():
    old, new = read_quiz_blocks(OLD), read_quiz_blocks(NEW)
    metas = read_meta()
    quizzes = []
    for i, m in enumerate(metas):
        t = m["title"]
        if t in new:
            src, origin = new[t], "inédito"
        elif t in old:
            src, origin = old[t], "revisado"
        else:
            sys.exit(f"Quiz não encontrado: {t}")
        disc = DISCIPLINES[i // 5][0]
        quizzes.append({"num": i + 1, "title": t, "disc": disc, "level": src["level"],
                        "questions": [dict(q) for q in src["questions"]], "origin": origin, **m})
    unused_new = set(new) - {q["title"] for q in quizzes}
    if unused_new:
        sys.exit(f"Quizzes novos sem metadados: {unused_new}")
    return quizzes


# ------------------------------------------------------------------ validação
def norm(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9 ]+", "", s).strip()


def validate(quizzes):
    err = []
    if len(quizzes) != 100:
        err.append(f"Quizzes = {len(quizzes)}")
    per = Counter(q["disc"] for q in quizzes)
    if len(per) != 20 or set(per.values()) != {5}:
        err.append(f"Distribuição por disciplina incorreta: {per}")
    for key in ("title", "gancho", "video", "q11"):
        vals = [norm(q[key]) for q in quizzes]
        if len(set(vals)) != len(vals):
            err.append(f"Há {key} repetido")
    allq = []
    for qz in quizzes:
        for key in ("tema", "gancho", "video", "q11", "tags", "cena"):
            if len(qz.get(key, "")) < 8:
                err.append(f"Quiz {qz['num']}: campo '{key}' ausente")
        tags = qz.get("tags", "").split()
        if len(tags) != 4 or not all(t.startswith("#") for t in tags):
            err.append(f"Quiz {qz['num']}: são exigidas exatamente 4 hashtags")
        if not qz["q11"].rstrip().endswith(("?", "!")):
            err.append(f"Quiz {qz['num']}: questão 11 deve terminar com ? ou !")
        if re.search(r"\b(resposta|gabarito)\s*:", qz["q11"], re.I):
            err.append(f"Quiz {qz['num']}: questão 11 parece conter resposta")
        if qz["level"] not in LEVELS:
            err.append(f"Quiz {qz['num']}: nível inválido")
        if len(qz["questions"]) != 10:
            err.append(f"Quiz {qz['num']} tem {len(qz['questions'])} questões com alternativas")
        for it in qz["questions"]:
            opts = [it["correct"], *it["wrong"]]
            if len({o.lower() for o in opts}) != 4 or not all(opts):
                err.append(f"{it['where']}: alternativas repetidas ou vazias")
            if len(it["expl"]) < 15:
                err.append(f"{it['where']}: explicação curta")
            allq.append((norm(it["q"]), it))
    for i in range(len(allq)):
        a, ia = allq[i]
        for j in range(i + 1, len(allq)):
            b, ib = allq[j]
            if a == b:
                err.append(f"Enunciado duplicado: {ia['where']} / {ib['where']}")
                continue
            sm = SequenceMatcher(None, a, b)
            if sm.real_quick_ratio() > .8 and sm.quick_ratio() > .8 and sm.ratio() > .8 \
                    and norm(ia["correct"]) == norm(ib["correct"]):
                err.append(f"Questões muito parecidas: {ia['where']} / {ib['where']}")
    return err


# ------------------------------------------------------------------ embaralhamento
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


def arrange(quizzes, seed=1100):
    """Embaralha as alternativas: cada quiz sem três letras iguais seguidas e no máximo 4 por letra;
    entre as disposições válidas, escolhe a que mais equilibra o total geral de A, B, C e D."""
    rng = random.Random(seed)
    total = Counter()

    def candidate(qz):
        targets = list("ABCDABCD") + rng.sample("ABCD", 2)
        rng.shuffle(targets)
        layout = []
        for it, tgt in zip(qz["questions"], targets):
            opts = [it["correct"], *it["wrong"]]
            keys = numeric_key(opts)
            if keys is not None:
                ordered = [opts[k] for k in sorted(range(4), key=lambda k: keys[k])]
                pos = ordered.index(it["correct"])
                if abs((3 - pos) - LETTERS.index(tgt)) < abs(pos - LETTERS.index(tgt)):
                    ordered.reverse()
            else:
                wrong = it["wrong"][:]
                rng.shuffle(wrong)
                pos = LETTERS.index(tgt)
                ordered = wrong[:pos] + [it["correct"]] + wrong[pos:]
            layout.append((ordered, LETTERS[ordered.index(it["correct"])]))
        return layout

    for qz in quizzes:
        best, best_score = None, None
        for _ in range(400):
            lay = candidate(qz)
            ans = "".join(a for _, a in lay)
            c = Counter(ans)
            if re.search(r"(.)\1\1", ans) or len(c) < 4 or max(c.values()) > 4:
                continue
            t = total + c
            mean = sum(t.values()) / 4
            score = sum((t[L] - mean) ** 2 for L in LETTERS)
            if best_score is None or score < best_score:
                best, best_score = lay, score
        if best is None:
            sys.exit(f"Não foi possível distribuir o gabarito do quiz {qz['num']}")
        total += Counter(a for _, a in best)
        for it, (ordered, a) in zip(qz["questions"], best):
            it["options"], it["answer"] = ordered, a


# ------------------------------------------------------------------ textos derivados
def description(q):
    return (f"{q['tema']}. Teste seus conhecimentos de {q['disc']} com 10 questões no estilo de concurso público "
            f"e encare o desafio final. Quantas você acertou? Comente sua nota e responda a questão 11 nos comentários!")


def video_prompt(q):
    L = []
    a = L.append
    a("Crie um vídeo vertical de quiz educativo para concursos públicos, em animação 3D estilo cartoon, "
      "pronto para TikTok, Instagram Reels e YouTube Shorts.")
    a("")
    a("DADOS DO VÍDEO")
    a(f"- Disciplina: {q['disc']}")
    a(f"- Tema: {q['tema']}")
    a(f"- Nível: {q['level']}")
    a(f"- Título do vídeo: {q['video']}")
    a(f"- Formato: vertical 9:16 (1080 x 1920 px), 30 fps, duração aproximada de 90 a 110 segundos.")
    a("")
    a("ESTILO VISUAL")
    a("- Animação 3D cartoon, cores vivas, iluminação suave e personagens expressivos.")
    a(f"- Cenário principal: {q['cena']}.")
    a("- Apresentador: um(a) mascote concurseiro(a) em 3D cartoon, com fone de ouvido e caderno, que reage "
      "com surpresa e comemoração a cada revelação.")
    a("- Objetos, animações e efeitos relacionados ao tema aparecem a cada pergunta (zoom, brilho, "
      "partículas e transições rápidas), sem poluir a tela.")
    a("- Texto grande e legível no celular: fonte sem serifa em negrito, mínimo de 60 px, alto contraste e "
      "contorno escuro; manter o texto dentro da área segura (sem ocupar os 10% superiores e os 15% inferiores).")
    a("- Ritmo dinâmico: cortes a cada 2 ou 3 segundos, cronômetro regressivo visível, som de tique-taque "
      "durante a pergunta e efeito sonoro de acerto na revelação.")
    a("- Narração em português do Brasil, voz animada e clara, com legendas embutidas sincronizadas.")
    a("")
    a("ROTEIRO")
    a(f"1. Abertura (0 a 4 s): mostre o gancho em texto grande, com narração: \"{q['gancho']}\"")
    a("2. Questões 1 a 10: para cada questão, mostre o número, o enunciado e as quatro alternativas "
      "(A, B, C e D) por 5 segundos, com cronômetro regressivo. Ao zerar, destaque a alternativa correta "
      "em verde por 2 a 3 segundos e mostre uma frase curta da explicação.")
    a("3. Questão 11 (desafio final): mostre a pergunta em destaque, SEM alternativas e SEM resposta, "
      "com o texto na tela \"Qual é a sua resposta? Comente abaixo!\" e o mascote pensativo.")
    a("4. Encerramento (últimos 5 s): CTA para comentar e seguir o perfil.")
    a("")
    a("REGRAS DE REVELAÇÃO (OBRIGATÓRIAS)")
    a("- Nunca destaque, pisque, narre ou insinue a alternativa correta antes de o cronômetro daquela questão zerar.")
    a("- Não coloque nenhuma resposta na abertura, na thumbnail, nas legendas antecipadas, no título ou na descrição.")
    a("- As respostas abaixo são apenas para orientar o momento da revelação de cada questão.")
    a("- A questão 11 não tem resposta: não revele, não sugira e não mostre alternativas em nenhum momento.")
    a("")
    a("CONTEÚDO DO QUIZ")
    for i, it in enumerate(q["questions"], 1):
        a("")
        a(f"QUESTÃO {i}: {it['q']}")
        for Lt, o in zip(LETTERS, it["options"]):
            a(f"{Lt}) {o}")
        a(f"[Revelar somente após o cronômetro] Resposta: {it['answer']} — {it['correct'].rstrip('.')}. {it['expl']}")
    a("")
    a("QUESTÃO 11 — DESAFIO FINAL (sem alternativas e sem resposta):")
    a(q["q11"])
    a("")
    a("CTA FINAL")
    a("Narração e texto na tela: \"Quantas você acertou? Comente sua nota e a sua resposta para o desafio "
      "final! Siga o perfil para mais quizzes de concurso.\"")
    a("")
    a("PUBLICAÇÃO")
    a(f"- Título: {q['video']}")
    a(f"- Descrição: {description(q)}")
    a(f"- Hashtags: {q['tags']}")
    a("")
    a("ENTREGA")
    a("- Arquivo MP4 vertical 1080 x 1920, 30 fps, com narração, trilha sonora leve livre de direitos "
      "autorais, efeitos sonoros e legendas embutidas.")
    return "\n".join(L)


# ------------------------------------------------------------------ HTML
def e(s):
    return html.escape(s, quote=True)


FACES = "\n".join(
    f"@font-face {{ font-family: '{fam}'; font-weight: {w}; src: url('file://{FONT_DIR}/{f}.ttf') format('truetype'); }}"
    for fam, w, f in [
        ("VC", 400, "Inter-Regular"), ("VC", 500, "Inter-Medium"), ("VC", 600, "Inter-SemiBold"),
        ("VC", 700, "Inter-Bold"), ("VC", 800, "Inter-ExtraBold"), ("VC", 900, "Inter-Black"),
        ("VCD", 800, "InterDisplay-ExtraBold"), ("VCD", 900, "InterDisplay-Black"),
        ("VCM", 400, "DejaVuSansMono"), ("VCM", 700, "DejaVuSansMono-Bold"),
    ]
)

CSS = r"""
__FACES__
@page { size: 148mm 210mm; margin: 17mm 12.5mm 16mm 12.5mm;
  @top-left { content: "100 QUIZZES PARA CONCURSEIROS"; font: 700 6.3pt 'VC'; letter-spacing: .14em; color: #8a94a6; vertical-align: bottom; padding-bottom: 3mm; }
  @bottom-left { content: "1.100 questões · quizzes e prompts para vídeos"; font: 500 6.1pt 'VC'; color: #a3aab8; vertical-align: top; padding-top: 4mm; }
  @bottom-right { content: counter(page); font: 800 7.6pt 'VC'; color: #0b3b5c; vertical-align: top; padding-top: 4mm; }
}
@page cover { margin: 0; @top-left { content: none } @top-right { content: none } @bottom-left { content: none } @bottom-right { content: none } }
@page prompts { @top-right { content: "PROMPTS DE VÍDEO"; font: 700 6.3pt 'VC'; letter-spacing: .1em; color: #c2410c; vertical-align: bottom; padding-bottom: 3mm; } }
__SECTION_PAGES__
:root { --ink: #172030; --muted: #5b6678; --line: #dfe4ec; --soft: #f2f6fa; --navy: #0b3b5c; --navy2: #155e8a;
  --green: #0f9d58; --green-soft: #e6f5ec; --orange: #ea580c; --orange-soft: #fff1e6; --gold: #f2b705; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin: 0; font-family: 'VC', sans-serif; color: var(--ink); font-size: 9.3pt; line-height: 1.42; }
h1, h2, h3 { font-family: 'VCD', 'VC', sans-serif; margin: 0; }
.marker { position: absolute; font-size: 2pt; color: #fff; line-height: 1; }

.cover { page: cover; width: 148mm; height: 210mm; position: relative; overflow: hidden; color: #fff;
  background: linear-gradient(160deg, #0b3b5c 0%, #0a2c45 55%, #071d2e 100%); padding: 17mm 14mm 13mm; display: flex; flex-direction: column; }
.cover .band { position: absolute; right: -22mm; top: 28mm; width: 90mm; height: 90mm; border-radius: 50%; border: 9mm solid rgba(242,183,5,.16); }
.cover .band2 { position: absolute; left: -30mm; bottom: -30mm; width: 80mm; height: 80mm; border-radius: 50%; background: rgba(234,88,12,.14); }
.cover .tag { position: relative; align-self: flex-start; background: var(--gold); color: #0a2c45; font-size: 6.8pt; font-weight: 900; letter-spacing: .16em; padding: 1.4mm 3mm; border-radius: 1.2mm; }
.cover .big { position: relative; margin-top: 15mm; font-family: 'VCD'; font-weight: 900; font-size: 86pt; line-height: .82; letter-spacing: -.04em; }
.cover h1 { position: relative; font-weight: 900; font-size: 25pt; line-height: 1.02; margin-top: 3mm; }
.cover h1 span { color: var(--gold); }
.cover .sub { position: relative; margin-top: 6mm; font-size: 12pt; font-weight: 800; color: #fff; }
.cover .sub b { color: var(--gold); }
.cover .txt { position: relative; margin-top: 3mm; font-size: 8.6pt; color: #cfdbe8; max-width: 112mm; line-height: 1.45; }
.cover .stats { position: relative; margin-top: auto; display: grid; grid-template-columns: repeat(4, 1fr); gap: 2mm; }
.cover .stats div { border: 1px solid rgba(255,255,255,.25); border-radius: 2mm; padding: 2.4mm 1.6mm; text-align: center; font-size: 6.4pt; font-weight: 600; color: #cfdbe8; }
.cover .stats b { display: block; font-family: 'VCD'; font-size: 14pt; color: #fff; }
.cover .foot { position: relative; margin-top: 4mm; font-size: 6.6pt; color: rgba(255,255,255,.6); letter-spacing: .05em; }

.front { break-before: page; }
.kicker { font-size: 6.8pt; font-weight: 800; letter-spacing: .18em; color: var(--orange); text-transform: uppercase; }
.front h2 { font-size: 19pt; font-weight: 900; color: var(--navy); margin: 1.4mm 0 3.6mm; }
.front p { margin: 0 0 2.5mm; }
.boxes { display: grid; gap: 2mm; margin: 3mm 0; }
.boxes div { background: var(--soft); border-left: 2.6px solid var(--navy2); border-radius: 0 2mm 2mm 0; padding: 2.3mm 3mm; font-size: 8.7pt; }
.boxes b { color: var(--navy); }
.lv { display: inline-block; font-size: 6.4pt; font-weight: 800; letter-spacing: .05em; padding: .6mm 2mm; border-radius: 99px; text-transform: uppercase; vertical-align: 1px; }
.lv.f { background: #e3f4ea; color: #157a43; } .lv.m { background: #fdf0d5; color: #946200; } .lv.d { background: #fde4e4; color: #b42318; }
.small { font-size: 7.9pt; color: var(--muted); }
.toc-sec { break-inside: avoid; margin-top: 3mm; }
.toc-sec h3 { font-size: 7.4pt; font-weight: 800; text-transform: uppercase; letter-spacing: .05em; color: #fff; background: var(--navy); padding: 1.2mm 2.4mm; border-radius: 1.4mm; }
.toc-row { display: flex; align-items: baseline; gap: 1.4mm; font-size: 7.7pt; padding: .7mm .5mm; color: var(--ink); text-decoration: none; border-bottom: 1px dotted #d3d9e3; }
.toc-row .n { font-weight: 800; color: var(--navy2); width: 6.5mm; flex: none; }
.toc-row .t { flex: 1; }
.toc-row .p { flex: none; width: 9mm; text-align: right; font-weight: 800; color: var(--navy); }
.toc-row .pp { flex: none; width: 9mm; text-align: right; font-weight: 800; color: var(--orange); }
.toc-head { display: flex; gap: 1.4mm; font-size: 6.4pt; font-weight: 800; color: var(--muted); justify-content: flex-end; margin-top: 2mm; }
.toc-head span { width: 9mm; text-align: right; }

.part { break-before: page; min-height: 176mm; display: flex; flex-direction: column; justify-content: center; text-align: center; position: relative; }
.part .pn { font-size: 8pt; font-weight: 800; letter-spacing: .3em; color: var(--orange); }
.part h2 { font-size: 26pt; font-weight: 900; color: var(--navy); margin-top: 3mm; line-height: 1.05; }
.part p { color: var(--muted); max-width: 100mm; margin: 4mm auto 0; }

.sec { break-before: page; position: relative; }
.sec .band { background: var(--navy); color: #fff; border-radius: 3mm; padding: 6mm 5mm; position: relative; overflow: hidden; }
.sec .band::after { content: ""; position: absolute; right: 0; top: 0; bottom: 0; width: 3mm; background: var(--gold); }
.sec .dn { font-size: 7pt; font-weight: 800; letter-spacing: .2em; color: var(--gold); }
.sec h2 { font-size: 18pt; font-weight: 900; line-height: 1.08; margin-top: 2mm; }
.sec p.d { margin: 4mm 0 0; font-size: 9.2pt; color: var(--muted); }
.sec ul { list-style: none; padding: 0; margin: 6mm 0 0; border-top: 1.4px solid var(--navy); }
.sec li { padding: 2.2mm 0; border-bottom: 1px solid var(--line); display: flex; gap: 3mm; align-items: baseline; font-size: 8.7pt; }
.sec li b { color: var(--navy2); width: 14mm; flex: none; }
.sec li .t { flex: 1; }

.quiz { break-before: page; position: relative; }
.qhead { border-radius: 3mm; overflow: hidden; border: 1.4px solid var(--navy); margin-bottom: 2.6mm; }
.qhead .top { background: var(--navy); color: #fff; display: flex; justify-content: space-between; align-items: center; padding: 1.7mm 3.4mm; }
.qhead .qn { font-size: 7.6pt; font-weight: 800; letter-spacing: .15em; }
.qhead .qn span { color: var(--gold); }
.qhead .body { padding: 2.4mm 3.4mm 2.6mm; }
.qhead .disc { font-size: 6.8pt; font-weight: 800; letter-spacing: .1em; color: var(--navy2); text-transform: uppercase; }
.qhead h2 { font-size: 13pt; font-weight: 900; color: var(--navy); line-height: 1.15; margin: .8mm 0 1mm; }
.qhead .tema { font-size: 7.8pt; color: var(--muted); }
.hook { background: var(--orange-soft); border: 1.4px solid var(--orange); border-radius: 2.4mm; padding: 2.2mm 3mm; margin-bottom: 2mm; }
.hook .k { font-size: 6.6pt; font-weight: 900; letter-spacing: .16em; color: var(--orange); }
.hook .g { font-size: 10pt; font-weight: 800; line-height: 1.3; margin-top: .6mm; }
.vtitle { font-size: 7.9pt; margin-bottom: 2.8mm; padding: 0 .5mm; }
.vtitle b { color: var(--navy2); }
.question { break-inside: avoid; border: 1px solid var(--line); border-left: 2.4px solid var(--navy2); border-radius: 2mm; padding: 2.4mm 3mm 2.6mm; margin-bottom: 2.3mm; }
.question .qh { font-size: 6.6pt; font-weight: 800; letter-spacing: .12em; color: var(--navy2); text-transform: uppercase; margin-bottom: .8mm; }
.question .stem { font-weight: 600; font-size: 9.2pt; line-height: 1.35; margin-bottom: 1.8mm; }
.opts { display: grid; grid-template-columns: 1fr; gap: 1mm; }
.opts.two { grid-template-columns: 1fr 1fr; }
.opt { display: flex; gap: 2mm; align-items: flex-start; font-size: 8.7pt; line-height: 1.3; padding: .9mm 1.6mm; background: var(--soft); border-radius: 1.4mm; }
.opt .l { flex: none; width: 4.6mm; height: 4.6mm; border-radius: 50%; border: 1.2px solid var(--navy2); color: var(--navy2); background: #fff;
  font-weight: 800; font-size: 6.8pt; display: flex; align-items: center; justify-content: center; margin-top: -.1mm; }
.q11 { break-inside: avoid; border: 2px dashed var(--gold); background: #fffbea; border-radius: 2.6mm; padding: 2.8mm 3.2mm; margin-top: 3mm; }
.q11 .k { font-size: 7pt; font-weight: 900; letter-spacing: .14em; color: #a16207; }
.q11 .t { font-size: 9.6pt; font-weight: 700; margin: 1mm 0 1.2mm; line-height: 1.35; }
.q11 .c { font-size: 7.8pt; font-weight: 800; color: var(--orange); }
.quiz.c1 .question { padding: 1.9mm 2.7mm 2mm; margin-bottom: 1.8mm; }
.quiz.c1 .question .stem { font-size: 8.9pt; margin-bottom: 1.3mm; }
.quiz.c1 .opts { gap: .7mm; }
.quiz.c1 .opt { font-size: 8.4pt; padding: .6mm 1.4mm; }
.quiz.c2 .qhead h2 { font-size: 12pt; }
.quiz.c2 .question { padding: 1.5mm 2.4mm 1.6mm; margin-bottom: 1.4mm; }
.quiz.c2 .question .qh { margin-bottom: .4mm; }
.quiz.c2 .question .stem { font-size: 8.5pt; line-height: 1.27; margin-bottom: 1mm; }
.quiz.c2 .opt { font-size: 8pt; line-height: 1.22; padding: .4mm 1.2mm; }
.quiz.c2 .q11 { padding: 2mm 2.8mm; margin-top: 2mm; }

.key { break-before: page; position: relative; }
.key .khead { display: flex; align-items: center; gap: 2.6mm; margin-bottom: 2.8mm; }
.key .badge { background: var(--green); color: #fff; font-weight: 800; font-size: 7pt; letter-spacing: .14em; padding: 1.2mm 3mm; border-radius: 1.4mm; }
.key .khead h3 { font-size: 9.6pt; font-weight: 800; color: var(--navy); line-height: 1.2; }
.grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 1.4mm; margin-bottom: 2.4mm; }
.grid div { border: 1.2px solid var(--green); border-radius: 1.6mm; display: flex; justify-content: space-between; align-items: center; padding: 1.1mm 2.2mm; font-size: 8.4pt; }
.grid div span { color: var(--muted); font-weight: 700; } .grid div b { color: var(--green); font-size: 10pt; font-weight: 900; }
.g11 { font-size: 7.6pt; color: #a16207; background: #fffbea; border-radius: 1.6mm; padding: 1.4mm 2.4mm; margin-bottom: 3mm; font-weight: 600; }
.exh { font-size: 6.8pt; font-weight: 800; letter-spacing: .16em; color: var(--navy); margin-bottom: 1.4mm; text-transform: uppercase; }
.ex { break-inside: avoid; display: flex; gap: 2.4mm; padding: 1.8mm 0; border-bottom: 1px solid var(--line); font-size: 8.2pt; line-height: 1.37; }
.ex:last-child { border-bottom: none; }
.ex .k { flex: none; width: 9.5mm; font-weight: 900; color: var(--green); }
.ex .t span { color: #3a4556; }
.key.kc .ex { padding: 1.2mm 0; font-size: 7.8pt; line-height: 1.3; }
.key.kc .grid { margin-bottom: 2mm; }
.key.kc .g11 { margin-bottom: 2mm; }

.prompt { break-before: page; page: prompts; position: relative; }
.prompt .ph { display: flex; justify-content: space-between; align-items: center; background: var(--orange); color: #fff; border-radius: 2mm 2mm 0 0; padding: 1.8mm 3.2mm; }
.prompt .ph b { font-size: 8pt; letter-spacing: .12em; font-weight: 900; }
.prompt .ph span { font-size: 6.8pt; font-weight: 700; }
.prompt .meta { border: 1.4px solid var(--orange); border-top: none; border-radius: 0 0 2mm 2mm; padding: 2mm 3.2mm; margin-bottom: 2.6mm; font-size: 7.8pt; }
.prompt .meta b { color: var(--navy); }
.prompt .copy { font-size: 6.4pt; font-weight: 800; letter-spacing: .12em; color: var(--orange); margin-bottom: 1mm; }
.code { font-family: 'VCM', monospace; font-size: 6.75pt; line-height: 1.45; white-space: pre-wrap; overflow-wrap: anywhere; background: #f7f8fa;
  border: 1px solid #d6dbe3; border-left: 2.6px solid var(--orange); border-radius: 1.6mm; padding: 2.6mm 3mm; color: #1d2633; }

.prompt.pc .code { font-size: 6.35pt; line-height: 1.36; padding: 2.2mm 2.6mm; }
.prompt.pc .meta { padding: 1.6mm 3mm; margin-bottom: 2mm; }
.end { break-before: page; text-align: center; padding-top: 30mm; position: relative; }
.end .big { font-family: 'VCD'; font-weight: 900; font-size: 48pt; color: var(--navy); line-height: 1; }
.end h2 { font-size: 16pt; font-weight: 900; color: var(--navy); margin: 3mm 0 5mm; }
.end p { color: var(--muted); max-width: 104mm; margin: 0 auto 3mm; }
.end .note { margin-top: 9mm; font-size: 7.4pt; border-top: 1px solid var(--line); padding-top: 4mm; }
"""

LV = {"Fácil": "f", "Médio": "m", "Difícil": "d"}


def build_html(quizzes, pages=None, c1=(), c2=(), kc=(), pc=()):
    pages = pages or {}
    secs = [(name, desc, [q for q in quizzes if q["disc"] == name]) for name, desc in DISCIPLINES]
    sec_css = "\n".join(
        f'@page s{i} {{ @top-right {{ content: "{name.upper()}"; font: 700 6.1pt \'VC\'; letter-spacing: .06em; '
        f'color: #0b3b5c; vertical-align: bottom; padding-bottom: 3mm; }} }}'
        for i, (name, _, _) in enumerate(secs, 1))
    css = CSS.replace("__FACES__", FACES).replace("__SECTION_PAGES__", sec_css)
    o = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">',
         "<title>100 Quizzes para Concurseiros</title>", f"<style>{css}</style></head><body>"]
    o.append("""
<section class="cover"><div class="band"></div><div class="band2"></div>
  <div class="tag">MATERIAL PREMIUM PARA CONCURSEIROS</div>
  <div class="big">100</div>
  <h1>QUIZZES PARA<br><span>CONCURSEIROS</span></h1>
  <div class="sub"><b>1.100 questões</b> para testar seu conhecimento</div>
  <div class="txt">Guarda Municipal, Polícia Militar, Polícia Civil, agentes públicos e concursos de nível médio. Cada quiz traz gancho, título de vídeo, 10 questões com gabarito comentado, um desafio final para engajamento e um prompt completo para gerar o vídeo.</div>
  <div class="stats"><div><b>20</b>disciplinas</div><div><b>100</b>quizzes</div><div><b>1.100</b>questões</div><div><b>100</b>prompts</div></div>
  <div class="foot">Questões revisadas com base na legislação vigente até 2025 · Atualidades com referência temporal</div>
</section>""")
    lvc = Counter(q["level"] for q in quizzes)
    o.append(f"""
<section class="front">
  <div class="kicker">Apresentação</div>
  <h2>Sobre este material</h2>
  <p>Este material reúne <b>100 quizzes</b> distribuídos igualmente entre <b>20 disciplinas</b> cobradas em concursos de Guarda Municipal, Polícia Militar, Polícia Civil e demais carreiras de nível médio: são 5 quizzes por disciplina.</p>
  <p>Cada quiz tem <b>11 perguntas</b>: 10 questões de múltipla escolha, com quatro alternativas, gabarito e explicação, e uma <b>questão 11</b>, o desafio final, propositalmente sem alternativas e sem resposta, criada para gerar comentários nas redes sociais.</p>
  <p>Na segunda parte, você encontra <b>100 prompts completos</b>, um para cada quiz, prontos para copiar e colar no Claude Code e transformar o quiz em vídeo vertical para TikTok, Instagram Reels e YouTube Shorts.</p>
  <div class="boxes">
    <div><b>Níveis:</b> <span class="lv f">Fácil</span> {lvc['Fácil']} quizzes · <span class="lv m">Médio</span> {lvc['Médio']} · <span class="lv d">Difícil</span> {lvc['Difícil']}. Dentro de cada quiz, as questões também variam de dificuldade.</div>
    <div><b>Fundamentação:</b> as explicações citam o artigo, a lei, a súmula ou o conceito que sustenta a resposta.</div>
    <div><b>Atualidades:</b> as questões indicam a data dos fatos. Em Legislação Municipal, o material traz regras gerais e avisa quando o tema depende da lei de cada cidade.</div>
  </div>
  <p class="small">As questões consideram a legislação e a jurisprudência vigentes até 2025. Leis mudam: antes da prova ou da publicação de um vídeo, confira o texto atualizado exigido no edital.</p>
</section>
<section class="front">
  <div class="kicker">Orientações</div>
  <h2>Como usar os quizzes</h2>
  <div class="boxes">
    <div><b>Para estudar:</b> resolva as 10 questões sem consultar nada, confira o gabarito na página seguinte e leia todas as explicações, inclusive das que acertou.</div>
    <div><b>Para revisar:</b> anote o número das questões erradas e volte à lei seca indicada na explicação. Refaça o quiz alguns dias depois.</div>
    <div><b>Para criar vídeos:</b> use o gancho nos 3 primeiros segundos, o título sugerido na publicação e o prompt da Parte 2 para gerar o vídeo.</div>
    <div><b>Questão 11:</b> é o desafio final. Ela não tem gabarito neste material de propósito: publique-a no fim do vídeo e convide o público a responder nos comentários.</div>
    <div><b>Engajamento:</b> responda aos comentários com a fundamentação legal; isso aumenta o alcance e a autoridade do seu perfil.</div>
  </div>
  <p class="small">No índice, a primeira coluna de páginas leva ao quiz e a segunda, ao prompt do vídeo correspondente.</p>
</section>""")
    o.append('<section class="front"><div class="kicker">Sumário</div><h2>Índice por disciplina</h2>'
             '<div class="toc-head"><span>Quiz</span><span>Prompt</span></div>')
    for si, (name, _, qs) in enumerate(secs, 1):
        o.append(f'<div class="toc-sec"><h3>{si:02d} · {e(name)}</h3>')
        for q in qs:
            n = q["num"]
            o.append(f'<a class="toc-row" href="#quiz{n:03d}"><span class="n">{n:02d}</span><span class="t">{e(q["title"])}</span>'
                     f'<span class="p">{pages.get(f"Q{n:03d}", "000")}</span><span class="pp">{pages.get(f"P{n:03d}", "000")}</span></a>')
        o.append("</div>")
    o.append("</section>")

    o.append('<section class="part"><span class="marker">@@S00@@</span><div class="pn">PARTE 1</div><h2>Os 100 quizzes</h2>'
             '<p>Organizados em 20 disciplinas, com gancho, título do vídeo, 10 questões, desafio final e gabarito comentado.</p></section>')
    for si, (name, desc, qs) in enumerate(secs, 1):
        pg = f"s{si}"
        o.append(f'<section class="sec" style="page:{pg}"><span class="marker">@@S{si:02d}@@</span>'
                 f'<div class="band"><div class="dn">DISCIPLINA {si:02d}</div><h2>{e(name)}</h2></div><p class="d">{e(desc)}</p><ul>')
        for q in qs:
            o.append(f'<li><b>Quiz {q["num"]:02d}</b><span class="t">{e(q["title"])}</span><span class="lv {LV[q["level"]]}">{q["level"]}</span></li>')
        o.append("</ul></section>")
        for q in qs:
            n = q["num"]
            cls = "quiz" + (" c1" if n in c1 else "") + (" c1 c2" if n in c2 else "")
            o.append(f'<section class="{cls}" style="page:{pg}" id="quiz{n:03d}"><span class="marker">@@Q{n:03d}@@</span>'
                     f'<div class="qhead"><div class="top"><span class="qn">QUIZ <span>{n:02d}</span></span><span class="lv {LV[q["level"]]}">{q["level"]}</span></div>'
                     f'<div class="body"><div class="disc">{e(q["disc"])}</div><h2>{e(q["title"])}</h2><div class="tema">Tema: {e(q["tema"])}</div></div></div>'
                     f'<div class="hook"><div class="k">GANCHO DO VÍDEO</div><div class="g">{e(q["gancho"])}</div></div>'
                     f'<div class="vtitle"><b>Título sugerido:</b> {e(q["video"])}</div>')
            for i, it in enumerate(q["questions"], 1):
                two = all(len(x) <= 22 for x in it["options"])
                opts = "".join(f'<div class="opt"><span class="l">{Lt}</span><span>{e(x)}</span></div>' for Lt, x in zip(LETTERS, it["options"]))
                o.append(f'<div class="question"><div class="qh">Questão {i}</div><div class="stem">{e(it["q"])}</div>'
                         f'<div class="opts{" two" if two else ""}">{opts}</div></div>')
            o.append(f'<div class="q11"><div class="k">QUESTÃO 11 — DESAFIO FINAL</div><div class="t">{e(q["q11"])}</div>'
                     f'<div class="c">Qual é a sua resposta? Comente abaixo!</div></div></section>')
            grid = "".join(f"<div><span>{i}.</span><b>{it['answer']}</b></div>" for i, it in enumerate(q["questions"], 1))
            o.append(f'<section class="key{" kc" if n in kc else ""}" style="page:{pg}"><span class="marker">@@K{n:03d}@@</span>'
                     f'<div class="khead"><span class="badge">GABARITO</span><h3>Quiz {n:02d} · {e(q["title"])}</h3></div>'
                     f'<div class="grid">{grid}</div><div class="g11">Questão 11: desafio de engajamento, sem gabarito.</div><div class="exh">Explicações</div>')
            for i, it in enumerate(q["questions"], 1):
                o.append(f'<div class="ex"><span class="k">{i}. {it["answer"]}</span><span class="t"><b>{e(it["correct"].rstrip("."))}.</b> '
                         f'<span>{e(it["expl"])}</span></span></div>')
            o.append("</section>")

    o.append('<section class="part" style="page:prompts"><span class="marker">@@P000@@</span><div class="pn">PARTE 2</div><h2>Os 100 prompts<br>para criação dos vídeos</h2>'
             '<p>Cada prompt é independente e completo: copie o bloco inteiro e cole no Claude Code para gerar o vídeo do quiz correspondente.</p></section>')
    for q in quizzes:
        n = q["num"]
        o.append(f'<section class="prompt{" pc" if n in pc else ""}" id="prompt{n:03d}"><span class="marker">@@P{n:03d}@@</span>'
                 f'<div class="ph"><b>PROMPT DO VÍDEO · QUIZ {n:02d}</b><span>{e(q["disc"])}</span></div>'
                 f'<div class="meta"><b>Título:</b> {e(q["video"])}<br><b>Hashtags:</b> {e(q["tags"])}</div>'
                 f'<div class="copy">COPIE A PARTIR DAQUI ▼</div><div class="code">{e(video_prompt(q))}</div></section>')
    o.append("""
<section class="end"><span class="marker">@@END@@</span><div class="big">1.100</div><h2>questões depois, você está mais perto da aprovação.</h2>
<p>Cada quiz resolvido é um passo a mais. Revise os erros, volte à lei seca e repita os quizzes até acertar todos.</p>
<p>E, ao transformar os quizzes em vídeos, você ensina, engaja e aprende de novo. A vaga é de quem não desiste.</p>
<p><b>Bons estudos e boa prova!</b></p>
<p class="note">Material de estudo com questões elaboradas para preparação. Não substitui a leitura da legislação atualizada nem do edital do concurso.</p></section>""")
    o.append("</body></html>")
    return "\n".join(o)


# ------------------------------------------------------------------ PDF
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


MARK = re.compile(r"@@(?:[QSKP]\d+|END)@@")
QRE = re.compile(r"Q\s*U\s*E\s*S\s*T\s*Ã\s*O\s+\d")


def pdf_pages():
    t = subprocess.run(["pdftotext", "-layout", str(PDF_PATH), "-"], check=True, capture_output=True, text=True).stdout
    return t.split("\f")


def find_pages():
    pages = {}
    for i, p in enumerate(pdf_pages(), 1):
        for m in re.findall(r"@@([QSKP]\d+)@@", p):
            pages.setdefault(m, i)
    return pages


def overflow():
    """Quizzes cuja continuação tem pouco conteúdo: questão isolada (ou só a questão 11)
    na página de questões, ou até duas explicações sobrando no gabarito."""
    widow, key, cur, mode = set(), set(), None, None
    for p in pdf_pages():
        m = re.search(r"@@([QK])(\d+)@@", p)
        if m:
            mode, cur = m.group(1), int(m.group(2))
            continue
        if MARK.search(p) or cur is None:
            mode = None
            continue
        if mode == "Q":
            nq = len(QRE.findall(p))
            if nq <= 1:
                widow.add(cur)
        elif mode == "K":
            if len(re.findall(r"^\s*\d+\.\s+[ABCD]\s", p, re.M)) <= 2:
                key.add(cur)
    return widow, key


def prompt_tails():
    """Prompts cuja última página tem poucas linhas."""
    out, cur = set(), None
    for p in pdf_pages():
        m = re.search(r"@@P(\d+)@@", p)
        if m:
            cur = int(m.group(1))
            continue
        if MARK.search(p):
            cur = None
            continue
        if cur and len([l for l in p.splitlines() if l.strip()]) < 14:
            out.add(cur)
    return out


def main():
    quizzes = load()
    err = validate(quizzes)
    if err:
        print("\n".join(err[:60]))
        sys.exit(1)
    arrange(quizzes)
    print("Distribuição do gabarito:", dict(sorted(Counter(i["answer"] for q in quizzes for i in q["questions"]).items())))
    render(build_html(quizzes))
    w, kc = overflow()
    print("Compactar quizzes:", sorted(w), "| gabaritos:", sorted(kc))
    c1, c2 = set(w), set()
    render(build_html(quizzes, c1=c1, kc=kc))
    w2, k2 = overflow()
    if w2:
        c2 = set(w2)
        print("Compactação máxima:", sorted(c2))
        render(build_html(quizzes, c1=c1, c2=c2, kc=kc | k2))
        w3, k3 = overflow()
        if w3 or k3:
            print("ATENÇÃO: ainda com sobra:", sorted(w3), sorted(k3))
    kc = kc | k2
    pc = prompt_tails()
    print("Prompts compactados:", sorted(pc))
    if pc:
        render(build_html(quizzes, c1=c1, c2=c2, kc=kc, pc=pc))
        left = prompt_tails()
        if left:
            print("ATENÇÃO: prompts ainda com sobra:", sorted(left))
    pages = find_pages()
    render(build_html(quizzes, pages, c1, c2, kc, pc))
    assert find_pages() == pages, "paginação mudou entre as passagens"
    (OUT / "prompts").mkdir(exist_ok=True)
    for q in quizzes:
        (OUT / "prompts" / f"quiz_{q['num']:03d}.txt").write_text(video_prompt(q), encoding="utf-8")
    (OUT / "resumo.json").write_text(json.dumps(
        [{"quiz": q["num"], "disciplina": q["disc"], "titulo": q["title"], "nivel": q["level"], "origem": q["origin"],
          "gabarito": "".join(i["answer"] for i in q["questions"])} for q in quizzes], ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"OK: {len(quizzes)} quizzes, {sum(len(q['questions']) + 1 for q in quizzes)} questões, "
          f"{len(quizzes)} prompts -> {PDF_PATH}")


if __name__ == "__main__":
    main()
