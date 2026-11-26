"""Kit comum dos Cadernos Simplificados (estrutura de páginas, treinos, revisão, questões e encerramento).
Uso em gerar.py:  import kit; from kit import *  e depois kit.U = {...}; kit.CAD = "11"; etc."""
import os, re
from componentes import *

P = []
U = {}
CAD = "00"
NV = '#e6e7ea'
TREINOS = []

def add(html, first=False): P.append(page(f'<div class="marker">§§P{len(P)+1:03d}§§</div>' + html, first))
def H(u, title, lead, marker=None): return head(U[u][0], U[u][1], title, lead, marker)
def p(t): return f"<p>{t}</p>"
def colors(*keys):
    m = {"b":(C['blue'],C['sky']),"g":(C['green'],C['greensoft']),"o":(C['golddeep'],C['goldsoft']),"r":(C['red'],C['redsoft']),"n":(C['navy'],NV)}
    return [m[k] for k in keys]
def atencao(html, kws=None, t='Atenção na prova'):
    add(pratica_title(t) + html + (kw(kws) if kws else ''))
def arrowdefs(i="ar"):
    return f'<defs><marker id="{i}" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L10,5 L0,10 z" fill="{C["ink"]}"/></marker></defs>'
def scene3(items, cap):
    s = f'<figure><svg viewBox="0 0 640 260" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    for i,(t,fg,bg,who,lines,leg) in enumerate(items):
        x = i*214
        s += f'<rect x="{x+2}" y="2" width="206" height="256" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x+105}" y="26" text-anchor="middle" font-weight="900" font-size="{14 if len(t)<=18 else 12.5}" fill="{fg}">{t}</text>'
        s += f'<rect x="{x+14}" y="38" width="182" height="{20+len(lines)*17}" rx="12" fill="#fff" stroke="{fg}" stroke-width="1.8"/>'
        s += "".join(f'<text x="{x+105}" y="{58+j*17}" text-anchor="middle" font-size="11.2" font-weight="800" fill="{C["ink"]}">{l}</text>' for j,l in enumerate(lines))
        s += f'<g transform="translate({x+70},{70+len(lines)*17})"><svg viewBox="0 0 100 170" width="62" height="105"><use href="#ch-{who}"/></svg></g>'
        s += f'<text x="{x+105}" y="244" text-anchor="middle" font-size="11" font-weight="900" fill="{fg}">{leg}</text>'
    return s + f'</svg><figcaption>{cap}</figcaption></figure>'

def toc_page(TOC):
    toc = "".join(f'<li class="u"><span class="t">{t}</span><span class="p" data-pg="{m}"></span></li>' if k=="u" else f'<li><span class="t">{t}</span><span class="p" data-pg="{m}"></span></li>' for k,t,m in TOC)
    add(f'''<div class="unit"><span class="u">MAPA DO CADERNO</span></div><h1 class="big">Sumário</h1><ol class="toc" style="border-top:3px solid {C['navy']};margin-top:6pt">{toc}</ol>''')

def opener(num, kicker, title, items, marker):
    lis = "".join(f'<li><span>{i+1:02d}</span>{t}</li>' for i,t in enumerate(items))
    add(f'''<div class="marker">§§{marker}§§</div><div class="opener"><div class="num">{num}</div><div class="k">{kicker}</div><h1>{title}</h1><ul>{lis}</ul></div>''')

def treino(n, itens):
    TREINOS.append((n, itens))
    rows = "".join(f'<tr><td style="width:7%;text-align:center;font-weight:900;color:{C["navy"]}">{i+1}</td><td>{a}</td><td style="width:16%;text-align:center">( C ) &nbsp; ( E )</td></tr>' for i,(a,_,_) in enumerate(itens))
    add(f'''<div class="unit"><span class="u">TREINO RÁPIDO</span><span class="t">Unidade {n}</span></div><h1 class="big">Certo ou <span class="hl">errado?</span></h1>
<p class="lead">Marque C ou E sem consultar. As respostas comentadas estão no gabarito, no fim do caderno.</p>
<table><tr><th>#</th><th>Afirmação</th><th style="text-align:center">Sua resposta</th></tr>{rows}</table>''' + memo('Errou? Volte à página do assunto e releia a faixa <strong>Memorize</strong> e a <strong>Pegadinha</strong>.', "Dica:"))

def mapa(center, blocks, cap, lead, center_color="#5fd39e"):
    """center: (linha1, linha2, linha3); blocks: 6 x (titulo, [3 linhas], fg, bg)."""
    pos = [(150,62),(490,62),(112,235),(528,235),(150,408),(490,408)]
    s = f'''<figure><svg viewBox="0 0 640 470" width="580" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<g stroke="#b3c2d4" stroke-width="2.5" fill="none">''' + "".join(f'<path d="M320 235 L{x} {y}"/>' for x,y in pos) + f'''</g>
<circle cx="320" cy="235" r="74" fill="{C['navy']}"/><text x="320" y="225" text-anchor="middle" fill="{center_color}" font-weight="900" font-size="13">{center[0]}</text>
<text x="320" y="245" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">{center[1]}</text><text x="320" y="263" text-anchor="middle" fill="#fff" font-weight="900" font-size="14">{center[2]}</text>'''
    for (x,y),(t,ls,fg,bg) in zip(pos, blocks):
        s += f'<rect x="{x-100}" y="{y-40}" width="200" height="80" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x}" y="{y-16}" text-anchor="middle" font-weight="900" font-size="12.5" fill="{fg}">{t}</text>'
        s += "".join(f'<text x="{x}" y="{y+4+i*15}" text-anchor="middle" font-size="10.8" fill="{C["ink"]}">{l}</text>' for i,l in enumerate(ls))
    s += f'</svg><figcaption>{cap}</figcaption></figure>'
    add('<div class="marker">§§R1§§</div><div class="unit"><span class="u">REVISÃO</span><span class="t">Véspera da prova</span></div><h1 class="big">Mapa <span class="hl">conceitual</span></h1><p class="lead">' + lead + '</p>' + s)

def erros(rows1, rows2=None):
    add('<div class="unit"><span class="u">REVISÃO</span><span class="t">Erros mais comuns</span></div><h1 class="big">Os erros <span class="hl">mais comuns</span> nas provas</h1><p class="lead">Afirmações erradas que costumam aparecer em questões. Ao lado, o que está certo.</p>' + table(["Afirmação errada","O certo é"], rows1, ["46%",None]))
    if rows2: add(pratica_title("Erros mais comuns (continuação)") + table(["Afirmação errada","O certo é"], rows2, ["46%",None]))

def flashcards(FC):
    def fcpage(items, first):
        cs = "".join(f'<div class="c"><div class="f"><small>{a}</small>{q}</div><div class="b">{r}</div></div>' for a,q,r in items)
        h = ('<div class="marker">§§R2§§</div><div class="unit"><span class="u">REVISÃO ATIVA</span></div><h1 class="big">Flash<span class="hl">cards</span></h1><p class="lead">Cubra a resposta, tente lembrar e confira. Revise em 1, 3, 7, 15 e 30 dias.</p>' if first else '')
        return h + f'<div class="fc">{cs}</div>'
    add(fcpage(FC[:12], True))
    for k in range(12, len(FC), 14): add(fcpage(FC[k:k+14], False))

def questoes(Q, ALVO):
    """Q: (tema, enunciado, [5 alternativas], gabarito, comentário, memorize). ALVO redistribui o gabarito."""
    for i,(tema,enun,alts,gab,com,mem) in enumerate(Q):
        assert len(alts) == 5, f"Q{i+1}: precisa de 5 alternativas"
        a, b = "ABCDE".index(gab), "ABCDE".index(ALVO[i]); alts = list(alts); alts[a], alts[b] = alts[b], alts[a]
        Q[i] = (tema, enun, alts, ALVO[i], com, mem)
    def qhtml(i, q):
        tema, enun, alts, gab, com, mem = q
        lis = "".join(f'<li data-l="{"ABCDE"[j]}">{a}</li>' for j,a in enumerate(alts))
        return f'<div class="q"><div class="qh"><span class="qn">Questão {i:02d}</span><span class="qa">Questão autoral · {tema}</span></div><p>{enun}</p><ol>{lis}</ol></div>'
    qs = [qhtml(i+1,q) for i,q in enumerate(Q)]
    add(f'<div class="marker">§§R3§§</div><div class="unit"><span class="u">PRÁTICA</span><span class="t">{len(Q)} questões</span></div><h1 class="big">Questões <span class="hl">autorais</span></h1><p class="lead">Elaboradas para este caderno, no estilo de concursos. Nenhuma foi aplicada por banca. Resolva sem consultar.</p>' + "".join(qs[:3]))
    for k in range(3, len(qs), 3): add("".join(qs[k:k+3]))
    def grid(a, b):
        return "<table><tr>" + "".join(f"<th style='text-align:center'>{i+1:02d}</th>" for i in range(a,b)) + "</tr><tr>" + "".join(f"<td style='text-align:center;font-weight:900;color:{C['navy']}'>{Q[i][3]}</td>" for i in range(a,b)) + "</tr></table>"
    gabs = [f'<div class="gab"><div class="gh">Questão {i+1:02d} <span>{q[3]}</span></div><p>{q[4]}</p><span class="mem">Memorize: {q[5]}</span></div>' for i,q in enumerate(Q)]
    grids = "".join(grid(a, min(a+12, len(Q))) for a in range(0, len(Q), 12))
    add('<div class="marker">§§R4§§</div><div class="unit"><span class="u">CORREÇÃO</span></div><h1 class="big">Gabarito <span class="hl">comentado</span></h1><p class="lead">Leia o comentário mesmo quando acertar.</p>' + grids + "".join(gabs[:4]))
    for k in range(4, len(gabs), 6): add("".join(gabs[k:k+6]))

def respostas_treinos():
    def tr_block(lst):
        out = ""
        for n, itens in lst:
            rows = "".join(f'<tr><td style="width:7%;text-align:center;font-weight:900">{i+1}</td><td style="width:12%;text-align:center" class="{"yes" if r=="C" else "no"}">{"CERTO" if r=="C" else "ERRADO"}</td><td>{c}</td></tr>' for i,(_,r,c) in enumerate(itens))
            out += f'<h3>Treino rápido · Unidade {n}</h3><table><tr><th>#</th><th>Resposta</th><th>Comentário</th></tr>{rows}</table>'
        return out
    n = len(TREINOS)
    add(f'<div class="unit"><span class="u">CORREÇÃO</span><span class="t">Treinos rápidos</span></div><h1 class="big">Respostas dos <span class="hl">treinos</span></h1><p class="lead">Certo ou errado das Unidades 1 a {n}.</p>' + tr_block(TREINOS[:2]))
    for k in range(2, n, 2): add(tr_block(TREINOS[k:k+2]))

def referencias(html_listas, limitacoes, data):
    add(f'''<div class="unit"><span class="u">ENCERRAMENTO</span></div><h1 class="big">Referências e <span class="hl">verificação</span></h1><p class="lead">De onde vieram as informações.</p>{html_listas}''' + lembre(p(f'<strong>Material pesquisado e atualizado em: {data}.</strong> ' + limitacoes), "Verificação e limitações"))

def encerramento(num, disciplina, sugestao):
    add(f'''<div class="ending"><h2>Fim do Caderno {num}</h2><p style="text-align:center">{sugestao}</p>
<p class="note" style="text-align:center">Mapa da Aprovação · Caderno Simplificado · {disciplina} · Caderno {num} · 1ª edição · novembro de 2026<br>Material de estudo independente. Não substitui a leitura da lei e do edital do seu concurso.</p></div>''')

def gravar(here, titulo, Q=None):
    doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{titulo}</title>
<link rel="stylesheet" href="estilo.css"></head><body>{symbols()}{"".join(P)}</body></html>'''
    open(os.path.join(here, "miolo.html"), "w").write(doc)
    checar(doc, Q)
    print("páginas planejadas:", len(P))

def checar(doc, Q=None):
    """Checagem automática de erros comuns: palavras repetidas, espaços duplos, pontuação duplicada, gabarito."""
    body = doc.split("</defs></svg>", 1)[-1]
    body = re.sub(r"<svg.*?</svg>", " | ", body, flags=re.S)
    body = re.sub(r"<div class=\"marker\">.*?</div>", " | ", body)
    body = re.sub(r"</?(b|strong|em|i|span)( [^>]*)?>", "", body)
    txt = re.sub(r"<[^>]+>", " | ", body)
    txt = re.sub(r"&nbsp;", " ", txt)
    probs = []
    for m in re.finditer(r"\b(\w{2,})\s+\1\b", txt, flags=re.I):
        w = m.group(1).lower()
        if w not in ("se", "nos", "nós"): probs.append("palavra repetida: " + txt[max(0,m.start()-30):m.end()+30].strip())
    for m in re.finditer(r"[,;:]\s*[,;:.]|\.\.(?!\.)|[^\s|]\s+[,.;:](?![\d.])", txt):
        ctx = txt[max(0,m.start()-30):m.end()+30].strip()
        if "..." not in ctx and "[...]" not in ctx: probs.append("pontuação: " + ctx)
    for m in re.finditer(r"\((?! C )(?! E )\s|(?<!\( C)(?<!\( E)\s\)", txt):
        probs.append("parêntese com espaço: " + txt[max(0,m.start()-25):m.end()+25].strip())
    if Q:
        for i, q in enumerate(Q):
            if len(set(q[2])) != 5: probs.append(f"Q{i+1}: alternativas repetidas")
    if TREINOS:
        for n, itens in TREINOS:
            for a, r, c in itens:
                if r not in ("C", "E"): probs.append(f"treino {n}: resposta inválida")
    print(f"CHECAGEM: {len(probs)} alerta(s)")
    for pr in probs[:40]: print("  -", pr)
