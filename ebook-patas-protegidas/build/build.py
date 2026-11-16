"""Monta o HTML do e-book Patas Protegidas a partir dos arquivos de conteúdo.

Uso:
    python3 build/build.py            # gera build/ebook.html e build/fichas.html

Sintaxe especial usada nos arquivos .md de conteudo/:
    :::tipo Título          caixa (dica, info, alerta, vet, proibido, emergencia, mito, citacao)
    :::doenca Nome | etiqueta      cartão de doença
    :::socorro Nome | etiqueta     cartão de primeiros socorros
    :::projeto Nome | etiqueta     cartão de projeto caseiro
    :::checklist Título            checklist com caixinhas  (itens: "- [ ] texto")
    :::passos                      lista numerada em etapas
    :::grade / :::grade3 / :::grade-verde   cartões em grade (separar células com "+++")
    :::                            fecha o bloco
    @foto(nome, classes, "legenda")     fotografia de imagens/fotos/nome.jpg
    @svg(nome, classes, "legenda")      ilustração de imagens/ilustracoes/nome.svg
    @tabela(classe)                     aplica classe à próxima tabela
    @quebra                             quebra de página
"""
from pathlib import Path
import re
import sys
import html
import json

import markdown

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ilustracoes as ilu  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
CONTEUDO = RAIZ / "conteudo"
BUILD = RAIZ / "build"

ICONE_CAIXA = {
    "dica": ("lampada", "#2f6b52"), "info": ("info", "#7a5a2b"), "alerta": ("alerta", "#bf6526"),
    "vet": ("estetoscopio", "#2b5f77"), "proibido": ("proibido", "#c0392b"),
    "emergencia": ("cruz", "#c0392b"), "mito": ("lupa", "#5b4485"),
}
ROTULO_CAIXA = {
    "dica": "Dica prática", "info": "Saiba mais", "alerta": "Atenção", "vet": "Fale com o veterinário",
    "proibido": "Nunca faça", "emergencia": "Emergência", "mito": "Mito ou verdade?",
}
ICONE_CARD = {"doenca": "estetoscopio", "socorro": "cruz", "projeto": "ferramenta"}


def frontmatter(texto):
    meta = {}
    if texto.startswith("---"):
        _, fm, corpo = texto.split("---", 2)
        for linha in fm.strip().splitlines():
            if ":" in linha:
                k, v = linha.split(":", 1)
                meta[k.strip()] = v.strip()
        return meta, corpo
    return meta, texto


def svg_inline(nome):
    caminho = RAIZ / "imagens" / "ilustracoes" / f"{nome}.svg"
    conteudo = caminho.read_text(encoding="utf-8")
    # torna o SVG responsivo: remove largura/altura fixas do elemento raiz
    return re.sub(r"(<svg[^>]*?) width='\d+' height='\d+'", r"\1", conteudo, count=1)


def figura(tipo, args):
    partes = [a.strip() for a in re.findall(r'"[^"]*"|[^,]+', args)]
    nome = partes[0]
    classes = partes[1].strip('"') if len(partes) > 1 else ""
    legenda = partes[2].strip('"') if len(partes) > 2 else ""
    cap = f"<figcaption>{legenda}</figcaption>" if legenda else ""
    if tipo == "foto":
        return (f'<figure class="photo {classes}"><img src="../imagens/fotos/{nome}.jpg" alt="{html.escape(legenda)}">{cap}</figure>')
    return f'<figure class="ilustra {classes}" data-nome="{nome}">{svg_inline(nome)}{cap}</figure>'


def processar_diretivas(texto):
    texto = re.sub(r"@(foto|svg)\(([^)]*)\)", lambda m: "\n" + figura(m.group(1), m.group(2)) + "\n", texto)
    texto = texto.replace("@quebra", '\n<div class="quebra"></div>\n')

    saida, pilha = [], []  # pilha guarda (tipo, número de </div> a fechar)
    for linha in texto.split("\n"):
        m = re.match(r"^:::([\w-]+)?\s*(.*)$", linha)
        if not m:
            if pilha and pilha[-1][0].startswith("grade") and linha.strip() == "+++":
                saida.append('\n</div>\n<div markdown="1">\n')
            else:
                saida.append(linha)
            continue
        tipo, resto = m.group(1), m.group(2).strip()
        if tipo is None:
            _, n = pilha.pop()
            saida.append("\n" + "</div>" * n + "\n")
            continue
        if tipo in ("doenca", "socorro", "projeto"):
            titulo, _, tag = resto.partition("|")
            ic = ilu.icone(ICONE_CARD[tipo], "#ffffff", 2)
            tag_html = f'<span class="tag">{tag.strip()}</span>' if tag.strip() else ""
            h3 = f'<h3>{titulo.strip()}</h3>' if titulo.strip() else '<span class="so-tag"></span>'
            saida.append(f'\n<div class="card {tipo}" markdown="1">\n<div class="card-topo">{ic}{h3}{tag_html}</div>\n'
                         f'<div class="card-corpo" markdown="1">\n')
            pilha.append((tipo, 2))
        elif tipo in ("checklist", "checklist-laranja"):
            cls = "checklist laranja" if tipo == "checklist-laranja" else "checklist"
            ic = ilu.icone("checklist", "#ffffff", 2)
            saida.append(f'\n<div class="{cls}" markdown="1">\n<div class="box-titulo">{ic}{resto}</div>\n')
            pilha.append((tipo, 1))
        elif tipo == "passos":
            saida.append('\n<div class="passos" markdown="1">\n')
            pilha.append((tipo, 1))
        elif tipo.startswith("grade"):
            cls = {"grade": "grid-cards", "grade3": "grid-cards tres", "grade-verde": "grid-cards verde",
                   "grade3-verde": "grid-cards tres verde"}[tipo]
            saida.append(f'\n<div class="{cls}" markdown="1">\n<div markdown="1">\n')
            pilha.append((tipo, 2))
        elif tipo == "citacao":
            saida.append('\n<div class="box citacao" markdown="1">\n')
            pilha.append((tipo, 1))
        else:
            nome_ic, cor = ICONE_CAIXA.get(tipo, ("info", "#1d4a39"))
            titulo = resto or ROTULO_CAIXA.get(tipo, "")
            saida.append(f'\n<div class="box {tipo}" markdown="1">\n<div class="box-titulo">{ilu.icone(nome_ic, cor, 2.2)}{titulo}</div>\n')
            pilha.append((tipo, 1))
    if pilha:
        raise ValueError(f"Bloco ::: não fechado: {pilha}")
    return "\n".join(saida)


MD = markdown.Markdown(extensions=["tables", "md_in_html", "attr_list", "sane_lists"])


def md_para_html(texto):
    texto = processar_diretivas(texto)
    MD.reset()
    out = MD.convert(texto)
    out = re.sub(r"<p>@tabela\(([\w -]+)\)</p>\s*<table>", r'<table class="\1">', out)
    out = re.sub(r"<li>\[ \]\s*", '<li class="ck">', out)
    out = re.sub(r"<li>\s*<p>\[ \]\s*", '<li class="ck"><p>', out)
    out = out.replace("<td>NÃO</td>", '<td class="nao">NÃO</td>').replace("<td>SIM</td>", '<td class="sim">SIM</td>')
    out = out.replace("<h4>", '<div class="h4">')
    out = out.replace("</h4>", "</div>")
    # títulos dos cartões de socorro
    out = re.sub(r'<div class="h4">(O que fazer[^<]*)</div>', r'<div class="h4 fazer">\1</div>', out)
    out = re.sub(r'<div class="h4">(O que (?:NÃO|não) fazer[^<]*)</div>', r'<div class="h4 nao">\1</div>', out)
    return out


def numerar_secoes(corpo_html, num_cap):
    secoes = []
    contador = [0]

    def sub(m):
        contador[0] += 1
        titulo = m.group(1)
        sid = f"cap{num_cap}-s{contador[0]}"
        secoes.append((sid, re.sub("<[^>]+>", "", titulo)))
        return f'<h2 id="{sid}"><span class="num">{num_cap}.{contador[0]}</span>{titulo}</h2>'

    corpo_html = re.sub(r"<h2>(.*?)</h2>", sub, corpo_html)
    return corpo_html, secoes


def abertura(meta):
    n = meta["num"]
    foto = meta.get("foto")
    pos = meta.get("foto_pos", "50% 40%")
    if foto:
        arte = f'<div class="foto"><img src="../imagens/fotos/{foto}.jpg" style="object-position:{pos}" alt=""></div>'
    else:
        arte = f'<div class="padrao">{ilu.abertura_padrao(meta.get("icone", "pata"), int(n))}</div>'
    itens = "".join(f"<li>{i.strip()}</li>" for i in meta.get("aprende", "").split("|") if i.strip())
    ic = ilu.icone(meta.get("icone", "pata"), "#ffffff", 1.8)
    curto = meta.get("curto", meta["titulo"])
    return f"""
<section class="abertura" id="cap-{n}">
  {arte}
  <div class="icone-cap">{ic}</div>
  <div class="texto">
    <div class="numero">Capítulo {int(n):02d}</div>
    <h1 data-curto="{html.escape(curto)}">{meta['titulo']}</h1>
    <div class="resumo">{meta.get('resumo', '')}</div>
    <div class="aprende"><div class="kicker">Neste capítulo</div><ul>{itens}</ul></div>
  </div>
</section>"""


def montar_capitulos():
    capitulos = []
    for arq in sorted(CONTEUDO.glob("cap*.md")):
        meta, corpo = frontmatter(arq.read_text(encoding="utf-8"))
        corpo_html = md_para_html(corpo)
        corpo_html, secoes = numerar_secoes(corpo_html, int(meta["num"]))
        capitulos.append((meta, corpo_html, secoes))
    return capitulos


def sumario(capitulos):
    itens = []
    for meta, _, secoes in capitulos:
        n = int(meta["num"])
        subs = "".join(f'<li><a href="#{sid}"><span class="t">{t}</span></a></li>' for sid, t in secoes)
        itens.append(f'<li class="cap"><a href="#cap-{n}"><span class="n">{n:02d}</span><span class="t">{meta["titulo"]}</span></a>'
                     f'<ol class="secoes">{subs}</ol></li>')
    itens.insert(0, '<li class="cap"><a href="#apresentacao"><span class="n">→</span><span class="t">Como usar este guia</span></a></li>')
    itens.append('<li class="cap"><a href="#referencias"><span class="n">+</span><span class="t">Referências e fontes consultadas</span></a></li>')
    return f"""
<section class="preliminar sumario" id="sumario">
  <div class="kicker">Navegue pelo guia</div>
  <h1>Sumário</h1>
  <p class="pequeno">Toque em qualquer título para ir direto à página.</p>
  <ol>{''.join(itens)}</ol>
</section>"""


def pagina_simples(nome):
    meta, corpo = frontmatter((CONTEUDO / nome).read_text(encoding="utf-8"))
    return meta, md_para_html(corpo)


def cabecalho(titulo):
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<title>{titulo}</title>
<meta name="author" content="Projeto Patas Protegidas">
<meta name="description" content="Guia completo de cuidados, saúde, proteção e bem-estar canino.">
<link rel="stylesheet" href="../estilo/ebook.css">
</head><body>
"""


def capa():
    return f"""
<section class="capa">
  <div class="foto"><img src="../imagens/fotos/caramelo-capa.jpg" alt="Cachorro caramelo olhando para cima"></div>
  <div class="veu"></div>
  <div class="topo">
    <div class="marca">{ilu.logo(L_ESC := '#1d4a39', '#e48a45', '#fbe6d4').replace("width='100' height='100'", "")}PATAS PROTEGIDAS</div>
    <h1>Meu cachorro,<br><span>minha responsabilidade</span></h1>
  </div>
  <div class="selo"><b>18</b>CAPÍTULOS<br>+ FICHAS</div>
  <div class="base">
    <div class="sub">O guia completo de cuidados, saúde, proteção e bem-estar canino.</div>
    <div class="frase">“Um cachorro não precisa apenas de um lar. Ele precisa de alguém que saiba cuidar dele.”</div>
  </div>
</section>"""


def rosto():
    return f"""
<section class="preliminar rosto">
  <div class="logo">{ilu.logo().replace("width='100' height='100'", "")}</div>
  <div class="projeto">PATAS PROTEGIDAS</div>
  <h1>Meu cachorro,<br>minha responsabilidade</h1>
  <div class="sub">O guia definitivo para proteger, alimentar, cuidar e proporcionar uma vida saudável e segura ao seu melhor amigo.</div>
  <div class="frase">“Um cachorro não precisa apenas de um lar.<br>Ele precisa de alguém que saiba cuidar dele.”</div>
  <div class="edicao">Projeto Patas Protegidas<br>1ª edição · 2026</div>
</section>"""


def final():
    return f"""
<section class="final">
  <div class="foto"><img src="../imagens/fotos/pretocaramelo-inteiro.jpg" alt="Cachorro preto e caramelo sentado olhando para a câmera"></div>
  <div class="texto">
    <div class="grande">Compartilhe conhecimento.<span>Proteja vidas.</span>Combata o abandono.</div>
    <div class="logo">{ilu.logo(L_ESC := '#2f6b52', '#e48a45', '#fbe6d4').replace("width='100' height='100'", "")}</div>
    <div class="assinatura">PROJETO PATAS PROTEGIDAS</div>
  </div>
</section>"""


def gerar():
    capitulos = montar_capitulos()
    estrutura = [{"num": int(m["num"]), "titulo": m["titulo"], "secoes": sec} for m, _, sec in capitulos]
    (BUILD / "estrutura.json").write_text(json.dumps(estrutura, ensure_ascii=False, indent=1), encoding="utf-8")
    _, creditos = pagina_simples("00-creditos.md")
    _, apresentacao = pagina_simples("00-apresentacao.md")
    _, referencias = pagina_simples("99-referencias.md")

    partes = [cabecalho("Patas Protegidas — Meu cachorro, minha responsabilidade"), capa(), rosto(),
              f'<section class="preliminar creditos">{creditos}</section>',
              sumario(capitulos),
              f'<section class="preliminar apresentacao" id="apresentacao">{apresentacao}</section>']
    for meta, corpo, _ in capitulos:
        partes.append(abertura(meta))
        partes.append(f'<section class="corpo-capitulo">{corpo}</section>')
    partes.append(f'<section class="capitulo referencias" id="referencias">{referencias}</section>')
    partes.append(final())
    partes.append("</body></html>")
    (BUILD / "ebook.html").write_text("\n".join(partes), encoding="utf-8")

    # Arquivo separado só com fichas e checklists (capítulos 16 e 17), para impressão
    fichas = [cabecalho("Patas Protegidas — Fichas e checklists imprimíveis"),
              f'''<section class="preliminar rosto"><div class="logo">{ilu.logo().replace("width='100' height='100'", "")}</div>
<div class="projeto">PATAS PROTEGIDAS</div><h1>Fichas e checklists<br>imprimíveis</h1>
<div class="sub">Material complementar do guia “Meu cachorro, minha responsabilidade”. Imprima, preencha e deixe à mão.</div>
<div class="frase">Dica: em folha A4, use “ajustar à página” ou “2 páginas por folha”.</div></section>''']
    for meta, corpo, _ in capitulos:
        if int(meta["num"]) in (16, 17):
            fichas.append(f'<section class="capitulo corpo-capitulo">{corpo}</section>')
    fichas.append("</body></html>")
    (BUILD / "fichas.html").write_text("\n".join(fichas), encoding="utf-8")

    # Versão editável: HTML limpo (sem paginação) para conversão em DOCX
    editavel = [cabecalho("Patas Protegidas — versão editável")]
    for meta, corpo, _ in capitulos:
        editavel.append(f"<h1>Capítulo {int(meta['num'])} — {meta['titulo']}</h1><p><em>{meta.get('resumo', '')}</em></p>{corpo}")
    editavel.append(f"<h1>Referências</h1>{referencias}</body></html>")
    texto = "\n".join(editavel)
    # troca ilustrações vetoriais por PNG e remove ícones decorativos
    texto = re.sub(r'(<figure class="ilustra[^"]*" data-nome="([^"]+)">)<svg.*?</svg>',
                   r'\1<img src="../imagens/ilustracoes/png/\2.png" style="max-width:100%">', texto, flags=re.S)
    texto = re.sub(r"<svg.*?</svg>", "", texto, flags=re.S)
    (BUILD / "editavel.html").write_text(texto, encoding="utf-8")
    print(f"{len(capitulos)} capítulos montados.")


if __name__ == "__main__":
    gerar()
