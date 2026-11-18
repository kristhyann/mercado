"""Gera o PDF '500 temas para TikTok' a partir de temas.txt."""
import html, re
from pathlib import Path
aqui = Path(__file__).parent
cats = []
for linha in (aqui / "temas.txt").read_text(encoding="utf-8").splitlines():
    if linha.startswith("# "):
        nome, _, desc = linha[2:].partition(" | ")
        cats.append({"nome": nome, "desc": desc, "temas": []})
    elif linha.strip():
        t, _, d = linha.partition(" | ")
        cats[-1]["temas"].append((t, d))
assert sum(len(c["temas"]) for c in cats) == 500

E = html.escape
cores = ["#c0392b", "#e07b34", "#2f6b52", "#7b62a3", "#3f7d99", "#8a6d3b", "#1d4a39", "#bf6526", "#5b9677", "#55645c"]
partes = []
n = 0
for i, c in enumerate(cats):
    cor = cores[i % len(cores)]
    itens = []
    for t, d in c["temas"]:
        n += 1
        itens.append(f'<li><span class="n" style="background:{cor}">{n}</span><div class="t"><b>{E(t)}</b><p>{E(d)}</p></div><span class="ck"></span></li>')
    partes.append(f'''<section class="cat" id="cat{i+1}">
<div class="cab" style="background:{cor}"><div class="k">Categoria {i+1} · temas {n-len(c["temas"])+1} a {n}</div><h2>{E(c["nome"])}</h2><p>{E(c["desc"])}</p></div>
<ol class="lista">{"".join(itens)}</ol></section>''')

indice = "".join(f'<li><a href="#cat{i+1}"><span class="dot" style="background:{cores[i%10]}"></span><span class="nm">{E(c["nome"])}</span><span class="qt">{len(c["temas"])} temas</span></a></li>' for i, c in enumerate(cats))

doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>500 temas para TikTok – Patas Protegidas</title>
<style>
@font-face{{font-family:Fraunces;src:url(../estilo/fontes/fraunces-latin-800-normal.woff2);font-weight:800}}
@font-face{{font-family:Fraunces;src:url(../estilo/fontes/fraunces-latin-400-italic.woff2);font-style:italic}}
@font-face{{font-family:Nunito;src:url(../estilo/fontes/nunito-sans-latin-400-normal.woff2);font-weight:400}}
@font-face{{font-family:Nunito;src:url(../estilo/fontes/nunito-sans-latin-700-normal.woff2);font-weight:700}}
@font-face{{font-family:Nunito;src:url(../estilo/fontes/nunito-sans-latin-800-normal.woff2);font-weight:800}}
@page{{size:148mm 210mm;margin:14mm 12mm 15mm;
 @bottom-center{{content:counter(page);font:700 8pt Nunito;color:#1d4a39}}
 @top-right{{content:"500 TEMAS · PATAS PROTEGIDAS";font:800 6.4pt Nunito;letter-spacing:.14em;color:#e07b34;vertical-align:bottom;padding-bottom:3mm}}}}
@page capa{{margin:0;@bottom-center{{content:none}}@top-right{{content:none}}}}
html{{font-size:9pt}} body{{margin:0;font-family:Nunito,sans-serif;color:#22302a;line-height:1.45}}
h1,h2{{font-family:Fraunces,serif;line-height:1.1;margin:0}}
.capa{{page:capa;height:210mm;width:148mm;position:relative;overflow:hidden;background:#1d4a39;color:#fff;break-after:page}}
.capa img{{width:100%;height:96mm;object-fit:cover;display:block}}
.capa .tx{{padding:9mm 11mm}}
.capa .big{{font-family:Fraunces;font-weight:800;font-size:58pt;line-height:.9;color:#f5a46a}}
.capa h1{{font-size:21pt;margin:2mm 0 4mm;color:#fff}}
.capa p{{color:#b9d3c1;font-size:9.5pt;max-width:110mm}}
.capa .rod{{position:absolute;left:11mm;right:11mm;bottom:9mm;display:flex;justify-content:space-between;font-weight:800;font-size:7.5pt;letter-spacing:.14em;color:#fbe4d1}}
.pg{{break-after:page}}
.pg h2{{font-size:17pt;color:#1d4a39;margin-bottom:3mm}}
.pg h3{{font:800 8pt Nunito;letter-spacing:.12em;text-transform:uppercase;color:#bf6526;margin:5mm 0 1.5mm}}
.pg p,.pg li{{font-size:8.8pt}} .pg ul{{padding-left:4.5mm;margin:0}} .pg li{{margin-bottom:1.2mm}}
.aviso{{background:#fbe4d1;border-left:2mm solid #e07b34;border-radius:2.5mm;padding:2.5mm 3.5mm;margin-top:4mm}}
.indice ol{{list-style:none;padding:0;margin:4mm 0 0}}
.indice a{{display:flex;align-items:center;gap:3mm;padding:2.6mm 0;border-bottom:.6pt solid #e4d8c3;text-decoration:none;color:#22302a;font-weight:700;font-size:9.5pt}}
.indice .dot{{width:3.2mm;height:3.2mm;border-radius:50%;flex:none}} .indice .nm{{flex:1}}
.indice .qt{{font-size:7.6pt;color:#56655d}}
.indice a::after{{content:target-counter(attr(href),page);font-family:Fraunces;font-weight:800;color:#bf6526;min-width:6mm;text-align:right}}
.cat{{break-before:page}}
.cab{{color:#fff;border-radius:3.5mm;padding:4mm 4.5mm;margin-bottom:3mm}}
.cab .k{{font:800 6.8pt Nunito;letter-spacing:.14em;text-transform:uppercase;opacity:.85}}
.cab h2{{font-size:16pt;margin:1mm 0 1.5mm}} .cab p{{margin:0;font-size:8.2pt;opacity:.92}}
.lista{{list-style:none;margin:0;padding:0}}
.lista li{{display:grid;grid-template-columns:8mm 1fr 4mm;gap:2.4mm;align-items:start;padding:2.1mm 0;border-bottom:.6pt solid #ece0cc;break-inside:avoid}}
.lista .n{{color:#fff;font:800 7.2pt Nunito;border-radius:2mm;text-align:center;padding:.8mm 0;margin-top:.3mm}}
.lista b{{font-size:9.3pt;color:#1d4a39}} .lista p{{margin:.4mm 0 0;font-size:8.1pt;color:#4b5a52;line-height:1.38}}
.lista .ck{{width:3.6mm;height:3.6mm;border:1.1pt solid #a9cbb0;border-radius:1mm;margin-top:.6mm}}
.fim{{break-before:page;text-align:center;padding-top:50mm}}
.fim .f{{font-family:Fraunces;font-weight:800;font-size:17pt;color:#1d4a39;line-height:1.25}} .fim .f span{{color:#e07b34}}
</style></head><body>
<section class="capa"><img src="../pagina-vendas/arquivos/capa-video.jpg" alt="">
<div class="tx"><div class="big">500</div><h1>temas para TikTok sobre animais que tocam o coração</h1>
<p>Ideias de vídeos em 3D sobre cães, gatos e outros animais domésticos: abandono, adoção, lealdade, velhice, cuidados e campanhas.</p></div>
<div class="rod"><span>PATAS PROTEGIDAS</span><span>IDEIAS PARA VÍDEOS EM 3D</span></div></section>

<section class="pg"><h2>Como usar este guia</h2>
<p>São 500 temas divididos em 10 categorias. Cada tema traz um título, que pode virar o gancho do vídeo, e uma ideia de cena para animar em 3D. Marque a caixinha ao lado de cada tema depois de postar.</p>
<h3>Estrutura que funciona no TikTok</h3>
<ul><li><b>0 a 3 segundos:</b> comece pela imagem mais forte (o olhar do animal, a caixa na chuva, o portão) e um texto curto na tela.</li>
<li><b>Meio:</b> conte a virada em poucas cenas. Um único momento emocionante vale mais que muitos cortes.</li>
<li><b>Final:</b> termine com esperança e uma chamada: adote, castre, identifique, compartilhe.</li>
<li><b>Duração:</b> de 15 a 45 segundos costuma funcionar bem para histórias emocionais.</li></ul>
<h3>Dicas para os vídeos em 3D</h3>
<ul><li>Mantenha os mesmos personagens em vários vídeos (o caramelo, o gatinho preto, os dachshunds) para criar uma série que o público acompanha.</li>
<li>Use luz quente e cores suaves nas cenas tristes; reserve cores vivas para a virada feliz.</li>
<li>Escreva o texto principal na tela: muita gente assiste sem som.</li>
<li>Músicas calmas de piano ou violão combinam com despedidas e resgates.</li>
<li>Repita uma assinatura no final, como a frase "Informação que protege, cuidado que salva vidas!".</li></ul>
<h3>Ideias de série</h3>
<ul><li><b>Segunda do resgate:</b> uma história da categoria 1 ou 2 toda segunda-feira.</li>
<li><b>Quarta do cuidado:</b> um tema da categoria 7.</li>
<li><b>Sexta do POV:</b> um vídeo narrado pelo animal (categoria 5).</li></ul>
<div class="aviso"><b>Cuidado com o conteúdo sensível.</b> Mostre abandono e dor com delicadeza, sem violência, sangue ou ferimentos. Isso respeita o público e evita que o TikTok limite o vídeo. Nos temas de saúde, termine sempre com "procure o veterinário" e não indique remédios nem doses.</div>
</section>

<section class="pg indice"><h2>Categorias</h2><p>Toque em uma categoria para ir direto a ela.</p><ol>{indice}</ol></section>
{"".join(partes)}
<section class="fim"><div class="f">Compartilhe conhecimento.<br><span>Proteja vidas.</span><br>Combata o abandono.</div>
<p style="margin-top:6mm;font-weight:800;letter-spacing:.2em;font-size:7.5pt;color:#5b9677">PROJETO PATAS PROTEGIDAS</p>
<p style="font-size:8pt;color:#56655d">E-book grátis: patas-protegidas-pagina.vercel.app</p></section>
</body></html>'''
(aqui / "temas.html").write_text(doc, encoding="utf-8")
print("ok")
