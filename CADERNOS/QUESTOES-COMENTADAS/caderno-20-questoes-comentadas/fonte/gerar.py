"""Gera miolo.html do Caderno 20: Questões Comentadas — Treinamento para Concursos. Uso: python3 gerar.py
Banco de questões autorais baseado nos Cadernos 01 a 19 (questoes_a.py e questoes_b.py)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit
from kit import *
from questoes_a import DISC_A
from questoes_b import DISC_B

DATA = "26 de novembro de 2026"
DISC = DISC_A + DISC_B
L = "ABCDE"
NIVCOR = {"Fácil": (C['green'], C['greensoft']), "Média": (C['golddeep'], C['goldsoft']), "Difícil": (C['red'], C['redsoft'])}

# ---------- monta as questões: posição da correta distribuída de forma equilibrada ----------
QS = []   # (num, disc_idx, assunto, nivel, enun, alts, gab, expl, [(letra, motivo)], dica)
n = 0
for d, (nome, base, lista) in enumerate(DISC):
    for (assunto, nivel, enun, certa, erradas, expl, dica) in lista:
        assert len(erradas) == 4, (nome, assunto)
        pos = (n * 2 + n // 5) % 5
        alts = [e[0] for e in erradas]; alts.insert(pos, certa)
        motivos = []
        k = 0
        for i, a in enumerate(alts):
            if i == pos: continue
            motivos.append((L[i], erradas[k][1])); k += 1
        assert len(set(alts)) == 5, (nome, assunto, "alternativas repetidas")
        n += 1
        QS.append((n, d, assunto, nivel, enun, alts, L[pos], expl, motivos, dica))

def badge(t, fg, bg): return f'<span style="display:inline-block;background:{bg};color:{fg};border:1.5px solid {fg};border-radius:20pt;padding:0 7pt;font-size:7.6pt;font-weight:900;letter-spacing:.5pt;margin-left:4pt">{t}</span>'

def qcard(q):
    num, d, assunto, nivel, enun, alts, gab, *_ = q
    fg, bg = NIVCOR[nivel]
    lis = "".join(f'<li data-l="{L[j]}">{a}</li>' for j, a in enumerate(alts))
    return (f'<div class="q"><div class="qh"><span class="qn">Questão {num:02d}</span><span class="qa">Questão autoral · {assunto}'
            f'{badge(nivel.upper(), fg, bg)}</span></div><p>{enun}</p><ol>{lis}</ol></div>')

def ccard(q):
    num, d, assunto, nivel, enun, alts, gab, expl, motivos, dica = q
    ers = "".join(f'<li><b>{l})</b> {m}</li>' for l, m in motivos)
    return (f'<div class="gab"><div class="gh">Questão {num:02d} <span>{gab}</span>'
            f'<small style="font-weight:700;color:{C["muted"]};margin-left:8pt">Assunto: {assunto} · {nivel}</small></div>'
            f'<p><b>Por que a {gab} está correta:</b> {expl}</p>'
            f'<p style="margin-bottom:2pt"><b>Por que as outras estão erradas:</b></p><ul style="margin-top:0">{ers}</ul>'
            f'<span class="mem">Dica de memorização: {dica}</span></div>')

# ================================================================ APRESENTAÇÃO
nq = len(QS)
cont = {k: sum(1 for q in QS if q[3] == k) for k in NIVCOR}
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">O treino final da coleção: questões autorais de todas as disciplinas, com comentários completos.</p>
<p>Este é o <strong>Caderno 20 da coleção</strong>, um banco de <strong>{nq} questões autorais</strong> de múltipla escolha (A a E), organizadas em <strong>{len(DISC)} disciplinas</strong> e baseadas no conteúdo dos Cadernos 01 a 19. Todas foram elaboradas para este material: <strong>nenhuma foi aplicada por banca</strong> e nenhuma é atribuída a concurso real.</p>
<p>Em cada disciplina, as questões vêm primeiro, sem resposta. Logo depois vem o <strong>gabarito comentado</strong> da disciplina, com: a alternativa correta e por que ela está correta; por que cada alternativa errada está errada; uma <strong>dica de memorização</strong>; e o <strong>assunto</strong> e o <strong>nível</strong> de cada questão.</p>
{table(["Nível","Quantidade","Para que serve"],[[badge("FÁCIL",*NIVCOR["Fácil"]),str(cont["Fácil"]),"Fixar o conceito básico"],[badge("MÉDIA",*NIVCOR["Média"]),str(cont["Média"]),"Aplicar a regra em situações e comparações"],[badge("DIFÍCIL",*NIVCOR["Difícil"]),str(cont["Difícil"]),"Detalhes, exceções e pegadinhas"]],["24%","20%",None])}
{memo("Resolva cada disciplina <strong>sem consultar</strong>, anote suas respostas e só então confira o gabarito. Errou? Volte ao caderno indicado no início da disciplina.", "Método:")}''', first=True)

TOC = []
for d, (nome, base, lista) in enumerate(DISC):
    a = sum(len(x[2]) for x in DISC[:d]) + 1
    TOC.append(("", f"{d+1:02d}. {nome} (questões {a:02d} a {a+len(lista)-1:02d})", f"A{d+1:02d}"))
add('<div class="unit"><span class="u">MAPA DO CADERNO</span></div><h1 class="big">Sumário</h1>' +
    '<ol class="toc" style="border-top:3px solid ' + C['navy'] + ';margin-top:6pt">' +
    '<li class="u"><span class="t">QUESTÕES POR DISCIPLINA</span><span class="p" data-pg="A01"></span></li>' +
    "".join(f'<li><span class="t">{t}</span><span class="p" data-pg="{m}"></span></li>' for _, t, m in TOC) +
    '<li class="u"><span class="t">ENCERRAMENTO</span><span class="p" data-pg="R1"></span></li>' +
    '<li><span class="t">Gabarito geral e desempenho por disciplina</span><span class="p" data-pg="R1"></span></li>' +
    '<li><span class="t">Referências e verificação</span><span class="p" data-pg="R2"></span></li></ol>')

# ================================================================ DISCIPLINAS
for d, (nome, base, lista) in enumerate(DISC):
    qs = [q for q in QS if q[1] == d]
    head_html = (f'<div class="marker">§§A{d+1:02d}§§</div><div class="unit"><span class="u">DISCIPLINA {d+1:02d}</span><span class="t">{base.split(" · ")[0]}</span></div>'
                 f'<h1 class="big">{nome}</h1><p class="lead">{base.split(" · ")[1]} · questões {qs[0][0]:02d} a {qs[-1][0]:02d}. Resolva antes de ver o gabarito.</p>')
    add(head_html + "".join(qcard(q) for q in qs[:3]))
    add("".join(qcard(q) for q in qs[3:]))
    first = True
    for k in range(0, len(qs), 3):
        h = (f'<div class="unit"><span class="u">GABARITO COMENTADO</span><span class="t">{nome}</span></div>' if first else "")
        add(h + "".join(ccard(q) for q in qs[k:k+3])); first = False

# ================================================================ GABARITO GERAL
def grid(a, b):
    return "<table><tr>" + "".join(f"<th style='text-align:center'>{QS[i][0]:02d}</th>" for i in range(a, b)) + "</tr><tr>" + \
           "".join(f"<td style='text-align:center;font-weight:900;color:{C['navy']}'>{QS[i][6]}</td>" for i in range(a, b)) + "</tr></table>"
grids = "".join(grid(a, min(a + 15, nq)) for a in range(0, nq, 15))
desemp = table(["Disciplina", "Questões", "Seus acertos"], [[nome, f"{sum(len(x[2]) for x in DISC[:d])+1:02d} a {sum(len(x[2]) for x in DISC[:d+1]):02d}", "____ de 5"] for d, (nome, b, l) in enumerate(DISC)], ["52%", "22%", None])
add('<div class="marker">§§R1§§</div><div class="unit"><span class="u">CORREÇÃO</span></div><h1 class="big">Gabarito <span class="hl">geral</span></h1><p class="lead">Todas as respostas em um só lugar, para conferência rápida.</p>' + grids)
add(pratica_title("Desempenho por disciplina") + p("Anote seus acertos. Disciplina com 3 acertos ou menos merece revisão no caderno correspondente.") + desemp)

# distribuição das letras (controle de qualidade)
dist = {l: sum(1 for q in QS if q[6] == l) for l in L}
print("distribuição do gabarito:", dist)
assert max(dist.values()) - min(dist.values()) <= 2

add('<div class="marker">§§R2§§</div>' + f'''<div class="unit"><span class="u">ENCERRAMENTO</span></div><h1 class="big">Referências e <span class="hl">verificação</span></h1><p class="lead">De onde vieram as informações.</p>
<h3>Base do conteúdo</h3><ul>
<li>Cadernos 01 a 19 da coleção Mapa da Aprovação, cujas bases legais foram conferidas no portal do Planalto nas datas indicadas em cada caderno.</li>
<li>Constituição Federal; Código Penal; Código de Processo Penal; Leis nº 8.072/1990, 8.112/1990, 9.455/1997, 9.503/1997 (CTB), 9.784/1999, 10.826/2003, 11.340/2006, 11.343/2006, 13.022/2014 e 13.060/2014.</li>
<li>Jurisprudência citada: STF, Súmula 473; RE 635.659 (2024); ADPF 995 (2023); RE 608.588, Tema 656 (2025).</li></ul>
<h3>Questões</h3><ul><li>Todas as {nq} questões são autorais, elaboradas para este caderno. Nenhuma foi aplicada em concurso nem é atribuída a banca examinadora.</li></ul>''' +
    lembre(p(f'<strong>Material pesquisado e atualizado em: {DATA}.</strong> As questões refletem a legislação e a jurisprudência descritas nos Cadernos 01 a 19. <strong>Limitações:</strong> leis e entendimentos dos tribunais mudam; as decisões judiciais citadas foram resumidas a partir de fontes oficiais de notícias e não substituem o inteiro teor; algumas classificações doutrinárias (como atributos do poder de polícia e gerações de direitos) variam entre autores. Confira sempre o edital do seu concurso.'), "Verificação e limitações"))
encerramento("20", "Questões Comentadas", 'Fim da coleção. Revise os cadernos das disciplinas em que você teve menos acertos.')
gravar(HERE, "Mapa da Aprovação — Caderno 20 — Questões Comentadas", None)
