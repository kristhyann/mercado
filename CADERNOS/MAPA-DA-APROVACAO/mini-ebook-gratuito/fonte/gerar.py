"""MAPA DA APROVAÇÃO · Mini Guia Gratuito. Gera ebook.html (páginas A4 de layout fixo). Uso: python3 gerar.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from componentes import symbols, char

NAVY, NAVY2, OR, OR2, ORS, GR, GR2, GRAY, GRAY2, BLK, CREAM, RED, REDS, GRN, GRNS = (
 "#0f1f3d","#1c3366","#f07c1b","#ffb066","#fff1e3","#2b2f36","#4a505b","#eef0f3","#d9dde3","#111317","#fbf6ee","#d6332a","#fdecea","#2c8a5a","#e4f4ec")
DATA = "25/11/2026"
PAGES = []
def page(body, run_l="", run_r="", demo="", dark=False, bg="", full=False):
    n = len(PAGES) + 1
    style = f' style="background:{bg}"' if bg else ''
    run = f'<div class="run"><span><b>MAPA DA APROVAÇÃO</b> · {run_l}</span><span>{run_r}</span></div>' if run_l else ''
    foot = (f'<div class="foot"><span>Mini Guia Gratuito · Cadernos Simplificados para Concursos</span><span class="n">{n}</span></div>' if not full else '')
    dm = f'<div class="demo">Amostra do estilo dos cadernos · {demo}</div>' if demo else ''
    inner = body if full else f'<div class="body">{body}</div>'
    PAGES.append(f'<section class="page{" dark" if dark else ""}"{style}>{run}{dm}{inner}{foot}</section>')

def ic(name, color, size=22, x=0, y=0):
    return f'<g style="color:{color}"><use href="#i-{name}" x="{x}" y="{y}" width="{size}" height="{size}"/></g>'
def law(t, txt): return f'<div class="law"><div class="t">{t}</div><p>{txt}</p></div>'
def trad(txt, who="prof"):
    return f'<div class="trad"><div style="flex:none;width:52pt">{char(who,52)}</div><div><div class="tag">Traduzindo o juridiquês</div><p>{txt}</p></div></div>'
def memo(txt, k="Memorize:"):
    return f'<div class="memo"><svg width="26" height="26" style="color:#2a1400;flex:none"><use href="#i-bulb"/></svg><p><b>{k.upper()}</b> {txt}</p></div>'
def trap(items, t="Pegadinha de concurso"):
    return f'<div class="trap"><div class="bar">⚠ {t}</div><div class="bd"><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul></div></div>'
def chips(ws, o=False): return '<div class="chips">' + "".join(f'<span class="chip{" o" if o else ""}">{w}</span>' for w in ws) + '</div>'
def title(kicker, t, lead=""):
    return f'<div class="kicker">{kicker}</div><h1>{t}</h1>' + (f'<p class="lead">{lead}</p>' if lead else '')

# ================================================================ 1. CAPA
stops = [(110,520,"1","CONSTITUCIONAL"),(250,430,"2","ART. 5º"),(130,330,"3","ADMINISTRATIVO"),(300,250,"4","PENAL"),(170,160,"5","PORTUGUÊS")]
route = f'''<svg viewBox="0 0 420 600" width="330" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<path d="M40 590 C 60 560, 90 540, 110 520 S 220 470, 250 430 S 120 370, 130 330 S 280 290, 300 250 S 190 200, 170 160 S 250 90, 320 60" fill="none" stroke="#fff" stroke-opacity=".25" stroke-width="22" stroke-linecap="round"/>
<path d="M40 590 C 60 560, 90 540, 110 520 S 220 470, 250 430 S 120 370, 130 330 S 280 290, 300 250 S 190 200, 170 160 S 250 90, 320 60" fill="none" stroke="{OR}" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
''' + "".join(f'<g transform="translate({x},{y})"><path d="M0 -40 C -18 -40 -26 -26 -26 -16 C -26 2 0 22 0 22 C 0 22 26 2 26 -16 C 26 -26 18 -40 0 -40Z" fill="{OR if i%2==0 else "#fff"}"/><text y="-12" text-anchor="middle" font-weight="900" font-size="20" fill="{NAVY}">{n}</text><text x="{34 if x<200 else -34}" y="-10" text-anchor="{"start" if x<200 else "end"}" font-weight="800" font-size="13" fill="#fff" letter-spacing="1.5">{l}</text></g>' for i,(x,y,n,l) in enumerate(stops)) + f'''
<g transform="translate(320,60)"><rect x="-3" y="-46" width="6" height="56" fill="#fff"/><path d="M3 -46 L50 -34 L3 -20Z" fill="{OR}"/><circle r="9" fill="{OR}"/></g>
<text x="300" y="104" text-anchor="middle" font-weight="900" font-size="12" fill="{OR2}" letter-spacing="2">SEU OBJETIVO</text>
</svg>'''
page(f'''<div style="position:absolute;inset:0;background:{NAVY}"></div>
<div style="position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.06) 1.2px,transparent 1.3px);background-size:7mm 7mm"></div>
<div style="position:absolute;left:0;top:0;bottom:0;width:9mm;background:{OR}"></div>
<div style="position:absolute;left:20mm;top:18mm;right:16mm;display:flex;justify-content:space-between;align-items:center;color:#fff">
 <div style="font-weight:900;letter-spacing:3pt;font-size:10pt">CADERNOS <span style="color:{OR}">SIMPLIFICADOS</span></div>
 <div style="border:1.5px solid rgba(255,255,255,.5);border-radius:20pt;padding:3pt 10pt;font-size:8pt;letter-spacing:1.5pt">MATERIAL GRATUITO</div></div>
<div style="position:absolute;left:20mm;top:34mm;width:175mm;color:#fff">
 <div style="display:inline-block;background:{OR};color:{NAVY};font-weight:900;font-size:10pt;letter-spacing:2.5pt;padding:4pt 10pt;border-radius:3pt">MINI GUIA GRATUITO</div>
 <div style="font-family:'Inter Display';font-weight:900;font-size:62pt;line-height:.9;margin-top:12pt;letter-spacing:-1.2pt;hyphens:none">MAPA DA<br><span style="color:{OR}">APROVAÇÃO</span></div>
 <div style="margin-top:16pt;font-size:15pt;font-weight:800;line-height:1.25;border-left:5px solid {OR};padding-left:11pt;width:85mm">5 assuntos de concurso<br>explicados de forma<br>simplificada</div>
 <div style="margin-top:14pt;font-size:10.5pt;line-height:1.5;color:#c9d3e6;width:80mm">Princípios fundamentais · Art. 5º · Princípios da Administração · Conceito de crime · Interpretação de texto</div>
</div>
<div style="position:absolute;right:8mm;top:98mm">{route}</div>
<div style="position:absolute;left:20mm;right:16mm;bottom:16mm;display:flex;justify-content:space-between;align-items:flex-end;color:#c9d3e6;font-size:8.5pt">
 <div><b style="color:#fff">Para quem está começando:</b> Guardas Municipais, carreiras policiais e concursos administrativos.<br>Explicações curtas · esquemas · mapa mental · pegadinhas · questões comentadas</div>
 <div style="text-align:right">Conteúdo conferido em {DATA}</div></div>''', full=True)

# ================================================================ 2. APRESENTAÇÃO
path = f'''<svg viewBox="0 0 300 520" width="270" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<path d="M60 20 V500" stroke="{GRAY2}" stroke-width="10" stroke-linecap="round"/>
<path d="M60 20 V500" stroke="{OR}" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>''' + "".join(
 f'<circle cx="60" cy="{40+i*105}" r="26" fill="{NAVY if i%2==0 else OR}"/><text x="60" y="{48+i*105}" text-anchor="middle" font-weight="900" font-size="22" fill="#fff">{i+1}</text>'
 f'<text x="100" y="{34+i*105}" font-weight="900" font-size="15" fill="{NAVY}">{t}</text><text x="100" y="{54+i*105}" font-size="12" fill="{GR2}">{s}</text><text x="100" y="{72+i*105}" font-size="11.5" font-weight="800" fill="{OR}">páginas {pg}</text>'
 for i,(t,s,pg) in enumerate([("Princípios fundamentais","Direito Constitucional · arts. 1º a 4º","4 e 5"),("Direitos e garantias","Noções do art. 5º","6 e 7"),("Princípios da Administração","Direito Administrativo · art. 37","8 e 9"),("Conceito de crime","Direito Penal · noções básicas","10 e 11"),("Interpretação de texto","Língua Portuguesa · método prático","12 e 13")])) + '</svg>'
page(f'''{title("Apresentação","Bem-vindo ao <span class='hl'>Mapa</span>","Cinco paradas importantes no caminho de quem estuda para concursos.")}
<div style="display:grid;grid-template-columns:1.05fr .95fr;gap:12mm">
<div>
<p>Este mini guia foi feito para quem está <b>começando</b> e sente que os conteúdos de concurso parecem difíceis demais: leis longas, palavras técnicas, muitas regras para decorar.</p>
<p>Aqui você vai estudar <b>cinco assuntos</b> que aparecem com frequência nos editais de <b>Guardas Municipais</b>, de <b>carreiras policiais</b> e de <b>concursos administrativos</b>. Cada um foi explicado do jeito que os nossos cadernos explicam: <b>linguagem simples</b>, <b>esquemas visuais</b>, exemplos do dia a dia e os <b>alertas de prova</b> que mais derrubam candidatos.</p>
<p>No fim, você testa o que aprendeu com <b>11 questões</b> autorais e confere o <b>gabarito comentado</b>.</p>
<div style="background:{NAVY};color:#fff;border-radius:12pt;padding:11pt 14pt;margin:12pt 0">
 <div style="font-weight:900;color:{OR};letter-spacing:1.5pt;font-size:8.5pt;margin-bottom:4pt">O QUE VOCÊ VAI ENCONTRAR</div>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:3pt 10pt;font-size:9.8pt">
 <span>✓ Explicação direta</span><span>✓ Esquemas e diagramas</span><span>✓ Mapa mental</span><span>✓ Exemplos práticos</span><span>✓ Pegadinhas de prova</span><span>✓ Questões comentadas</span></div></div>
<p class="note">Os trechos de lei foram conferidos no portal oficial da legislação federal (Planalto) em {DATA}. Este material é introdutório: confira sempre o edital do seu concurso.</p>
</div>
<div>{path}</div></div>''', "Apresentação", "Mini Guia Gratuito")

# ================================================================ 3. COMO USAR
steps = [("book",NAVY,"1. Leia o essencial","Comece pelo texto curto e pelo quadro da lei. Não tente decorar ainda."),
 ("megaphone",OR,"2. Traduza","Leia o “Traduzindo o juridiquês” e explique a ideia com suas palavras."),
 ("grid",NAVY2,"3. Visualize","Estude o esquema da página: ele resume a lógica do assunto."),
 ("exam",RED,"4. Pratique","Resolva as questões sem consultar e só depois veja o gabarito.")]
legend = [("Quadro da lei",CREAM,OR,"Trecho oficial. A prova costuma copiar estas palavras."),("Traduzindo o juridiquês","#fff",BLK,"A mesma ideia em linguagem de conversa."),
 ("Memorize",OR,OR,"A frase que precisa estar na sua cabeça no dia da prova."),("Pegadinha de concurso",REDS,RED,"Trocas de palavras e confusões comuns."),
 ("Selo laranja no topo","#fff",OR,"Indica uma página que reproduz o estilo dos cadernos completos.")]
page(f'''{title("Antes de começar","Como usar este <span class='hl'>guia</span>","Um método em quatro passos para aproveitar cada assunto.")}
<svg viewBox="0 0 640 170" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<defs><marker id="m1" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L10,5 L0,10z" fill="{GR}"/></marker></defs>''' +
 "".join(f'<rect x="{6+i*160}" y="8" width="146" height="154" rx="14" fill="#fff" stroke="{c}" stroke-width="2.5"/><circle cx="{79+i*160}" cy="46" r="26" fill="{c}"/>{ic(n,"#fff",28,65+i*160,32)}'
 f'<text x="{79+i*160}" y="96" text-anchor="middle" font-weight="900" font-size="13" fill="{NAVY}">{t}</text>' +
 "".join(f'<text x="{79+i*160}" y="{116+j*15}" text-anchor="middle" font-size="10.5" fill="{GR2}">{w}</text>' for j,w in enumerate(__import__("textwrap").wrap(d,24)))
 + (f'<line x1="{153+i*160}" y1="46" x2="{165+i*160}" y2="46" stroke="{GR}" stroke-width="2.5" marker-end="url(#m1)"/>' if i<3 else '')
 for i,(n,c,t,d) in enumerate(steps)) + '''</svg>
<h3 style="margin-top:12pt">Os elementos que você vai encontrar</h3>''' +
 "".join(f'<div style="display:flex;gap:10pt;align-items:center;padding:7pt 0;border-bottom:1px solid {GRAY2}"><div style="flex:none;width:52mm;background:{bg};border:2px solid {bd};border-radius:9pt;padding:4pt 9pt;font-weight:900;font-size:9.3pt;color:{"#2a1400" if bg==OR else BLK}">{t}</div><div style="font-size:10pt">{d}</div></div>' for t,bg,bd,d in legend) +
 f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:10pt;margin-top:14pt">
<div style="background:{GRAY};border-radius:12pt;padding:11pt 13pt"><div class="kicker" style="font-size:8pt">Ritmo sugerido</div><p style="margin:4pt 0 0">Um assunto por dia, em cerca de <b>30 minutos</b>. No sexto dia, faça todas as questões de uma vez.</p></div>
<div style="background:{ORS};border-radius:12pt;padding:11pt 13pt"><div class="kicker" style="font-size:8pt">Revisão</div><p style="margin:4pt 0 0">Releia só os <b>esquemas</b> e os quadros <b>Memorize</b> 1, 7 e 30 dias depois. É revisão rápida, e funciona.</p></div></div>''', "Como usar", "Mini Guia Gratuito")

# ================================================================ 4. CONSTITUCIONAL · conteúdo
pillars = ["SO","CI","DI","VA","PLU"]
pnames = [["Soberania"],["Cidadania"],["Dignidade da","pessoa humana"],["Valores sociais do","trabalho e da","livre iniciativa"],["Pluralismo","político"]]
temple = f'''<svg viewBox="0 0 640 300" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<path d="M40 70 L320 10 L600 70 Z" fill="{NAVY}"/><text x="320" y="58" text-anchor="middle" font-weight="900" font-size="15" fill="#fff" letter-spacing="2">REPÚBLICA FEDERATIVA DO BRASIL</text>
<rect x="40" y="70" width="560" height="16" fill="{NAVY2}"/>''' + "".join(
 f'<rect x="{62+i*112}" y="94" width="68" height="150" rx="6" fill="{OR if i%2==0 else "#ffd2a8"}"/><text x="{96+i*112}" y="180" text-anchor="middle" font-weight="900" font-size="{20 if len(pillars[i])<3 else 17}" fill="{NAVY}">{pillars[i]}</text>'
 + "".join(f'<text x="{96+i*112}" y="{264+j*13}" text-anchor="middle" font-size="10.3" font-weight="700" fill="{GR}">{l}</text>' for j,l in enumerate(pnames[i]))
 for i in range(5)) + f'<rect x="30" y="244" width="580" height="10" fill="{GRAY2}"/></svg>'
page(f'''{title("Assunto 1 · Direito Constitucional","Princípios <span class='hl'>fundamentais</span>","Os quatro primeiros artigos da Constituição dizem quem o Brasil é, aonde quer chegar e como se comporta no mundo.")}
{law("Art. 1º · Constituição Federal","Art. 1º A República Federativa do Brasil, formada pela união indissolúvel dos Estados e Municípios e do Distrito Federal, constitui-se em Estado Democrático de Direito e tem como fundamentos: I - a soberania; II - a cidadania; III - a dignidade da pessoa humana; IV - os valores sociais do trabalho e da livre iniciativa; V - o pluralismo político.<br>Parágrafo único. Todo o poder emana do povo, que o exerce por meio de representantes eleitos ou diretamente, nos termos desta Constituição.")}
<div style="text-align:center;font-weight:900;color:{NAVY};font-size:10pt;letter-spacing:1.5pt;margin:2pt 0 2pt">OS 5 PILARES QUE SUSTENTAM A REPÚBLICA (FUNDAMENTOS)</div>
{temple}
{trad("Pense no Brasil como um prédio. Os <b>fundamentos</b> são os pilares: sem eles, o prédio cai. Por isso são <b>substantivos</b> (coisas que já existem). “União indissolúvel” quer dizer que nenhum Estado ou Município pode se separar do país.")}
{memo("<b>SO-CI-DI-VA-PLU</b>: SOberania, CIdadania, DIgnidade da pessoa humana, VAlores sociais do trabalho e da livre iniciativa, PLUralismo político.","Mnemônico:")}''',
 "Direito Constitucional", "Princípios fundamentais", demo="Conteúdo simplificado")

# ================================================================ 5. CONSTITUCIONAL · esquema
cols = [("ART. 1º","FUNDAMENTOS","O que o Brasil É",NAVY,"#e6ebf4","star",["Soberania","Cidadania","Dignidade da pessoa humana","Valores sociais do trabalho e da livre iniciativa","Pluralismo político"],"são substantivos"),
 ("ART. 3º","OBJETIVOS","Aonde o Brasil QUER chegar",OR,ORS,"target",["Construir uma sociedade livre, justa e solidária","Garantir o desenvolvimento nacional","Erradicar a pobreza e a marginalização e reduzir as desigualdades sociais e regionais","Promover o bem de todos, sem preconceitos"],"começam com verbos"),
 ("ART. 4º","RELAÇÕES INTERNACIONAIS","Como o Brasil AGE no mundo",NAVY2,"#e8edf8","globe",["Soberania e respeito: independência nacional, autodeterminação dos povos, não-intervenção, igualdade entre os Estados","Paz: defesa da paz, solução pacífica dos conflitos, repúdio ao terrorismo e ao racismo","Humanidade: prevalência dos direitos humanos, cooperação entre os povos, concessão de asilo político"],"10 princípios em 3 grupos")]
colhtml = "".join(f'''<div style="border:2.5px solid {c};border-radius:14pt;overflow:hidden;background:{bg};display:flex;flex-direction:column">
<div style="background:{c};color:#fff;padding:8pt 10pt"><div style="font-size:8pt;font-weight:900;letter-spacing:1.5pt;opacity:.85">{a}</div><div style="font-family:'Inter Display';font-weight:900;font-size:13.5pt;line-height:1.05">{t}</div></div>
<div style="padding:9pt 10pt;flex:1"><div style="display:flex;align-items:center;gap:6pt;margin-bottom:6pt"><svg width="22" height="22" style="color:{c}"><use href="#i-{i}"/></svg><b style="color:{c};font-size:10pt">{s}</b></div>
{"".join(f'<div style="font-size:9.3pt;line-height:1.35;padding:4pt 0;border-top:1px dashed {GRAY2}">{x}</div>' for x in items)}</div>
<div style="background:#fff;border-top:2px solid {c};padding:5pt 10pt;font-size:8.8pt;font-weight:900;color:{c};text-transform:uppercase;letter-spacing:.6pt">→ {tip}</div></div>''' for a,t,s,c,bg,i,items,tip in cols)
page(f'''{title("Assunto 1 · Esquema visual","É · Quer · <span class='hl'>Age</span>","Os arts. 1º, 3º e 4º lado a lado: o esquema que resolve a maioria das questões.")}
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:7pt;margin-bottom:11pt">{colhtml}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:9pt">
{memo("Tem <b>verbo</b>? Art. 3º. Fala de <b>outros países ou povos</b>? Art. 4º. É um <b>valor-base</b> do país? Art. 1º.","Truque de prova:")}
<div style="border:2px solid {NAVY};border-radius:12pt;padding:8pt 12pt"><b style="color:{NAVY}">Parágrafo único do art. 4º:</b> o Brasil buscará a integração dos povos da <b>América Latina</b>, visando a uma comunidade latino-americana de nações.</div></div>
{trap(["<b>Soberania</b> é fundamento (art. 1º); <b>independência nacional</b> é princípio das relações internacionais (art. 4º).","A pobreza e a marginalização devem ser <b>erradicadas</b>; as desigualdades devem ser <b>reduzidas</b>. “Erradicar as desigualdades” está errado.","<b>Dignidade da pessoa humana</b> é fundamento, e não objetivo."])}''',
 "Direito Constitucional", "Esquema visual", demo="Esquema visual")

# ================================================================ 6. ART. 5º
wheel_items = [("VIDA","pulse",RED),("LIBERDADE","dove",NAVY2),("IGUALDADE","scales",OR),("SEGURANÇA","shield",GRN),("PROPRIEDADE","house",NAVY)]
import math
wheel = f'<svg viewBox="0 0 300 300" width="250" xmlns="http://www.w3.org/2000/svg" font-family="Inter"><circle cx="150" cy="150" r="140" fill="{GRAY}"/>'
for i,(t,ico,c) in enumerate(wheel_items):
    a = -math.pi/2 + i*2*math.pi/5
    x, y = 150+98*math.cos(a), 150+98*math.sin(a)
    wheel += f'<line x1="150" y1="150" x2="{x:.0f}" y2="{y:.0f}" stroke="{GRAY2}" stroke-width="3"/><circle cx="{x:.0f}" cy="{y:.0f}" r="36" fill="#fff" stroke="{c}" stroke-width="3"/>{ic(ico,c,26,x-13,y-24)}<text x="{x:.0f}" y="{y+20:.0f}" text-anchor="middle" font-weight="900" font-size="8.6" fill="{c}">{t}</text>'
wheel += f'<circle cx="150" cy="150" r="46" fill="{NAVY}"/><text x="150" y="146" text-anchor="middle" font-weight="900" font-size="15" fill="{OR}">ART. 5º</text><text x="150" y="164" text-anchor="middle" font-weight="800" font-size="10" fill="#fff">caput</text></svg>'
page(f'''{title("Assunto 2 · Direitos e garantias fundamentais","Noções do <span class='hl'>art. 5º</span>","O artigo mais cobrado da Constituição começa protegendo cinco direitos.")}
<div style="display:grid;grid-template-columns:250px 1fr;gap:10pt;align-items:center">
<div>{wheel}</div>
<div>{law("Art. 5º, caput · Constituição Federal","Art. 5º Todos são iguais perante a lei, sem distinção de qualquer natureza, garantindo-se aos brasileiros e aos estrangeiros residentes no País a inviolabilidade do direito à vida, à liberdade, à igualdade, à segurança e à propriedade, nos termos seguintes:")}
<p style="font-size:10pt">Os <b>79 incisos</b> do art. 5º detalham esses cinco direitos.</p></div></div>
<h2 style="margin-top:6pt">Direito x garantia: a casa e o cadeado</h2>
<div style="display:grid;grid-template-columns:1fr 70px 1fr;gap:6pt;align-items:center;margin-bottom:10pt">
<div style="background:#e6ebf4;border-radius:12pt;padding:10pt 12pt;display:flex;gap:9pt;align-items:center"><svg width="42" height="42" style="color:{NAVY};flex:none"><use href="#i-house"/></svg><div><b style="color:{NAVY}">DIREITO</b> declara o bem protegido.<br><span class="note">Ex.: “é livre a locomoção” (inciso XV).</span></div></div>
<div style="text-align:center;font-weight:900;font-size:20pt;color:{OR}">+</div>
<div style="background:{ORS};border-radius:12pt;padding:10pt 12pt;display:flex;gap:9pt;align-items:center"><svg width="42" height="42" style="color:#b35a0c;flex:none"><use href="#i-lock"/></svg><div><b style="color:#b35a0c">GARANTIA</b> é a ferramenta que protege o direito.<br><span class="note">Ex.: <i>habeas corpus</i> (inciso LXVIII).</span></div></div></div>
{trad("O <b>direito</b> é a sua casa; a <b>garantia</b> é o cadeado. Se alguém prende você ilegalmente (viola o direito de ir e vir), o <i>habeas corpus</i> é a chave que abre a cela.","profa")}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:9pt">
<div><h3>Características que caem em prova</h3>{chips(["universais","inalienáveis","imprescritíveis","irrenunciáveis","relativos (não absolutos)","aplicação imediata"])}</div>
{trap(["Pelo STF, a proteção alcança também o estrangeiro <b>não residente</b>, como o turista.","O rol do art. 5º é <b>exemplificativo</b> (§ 2º): há direitos fundamentais fora dele."])}</div>''',
 "Direitos e garantias", "Noções do art. 5º")

# ================================================================ 7. ART. 5º · cidade ilustrada + resumo visual
city = f'''<svg viewBox="0 0 640 250" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<rect x="0" y="0" width="640" height="250" rx="14" fill="#eaf2fb"/>
<rect x="0" y="190" width="640" height="60" fill="#c9ced6"/><rect x="0" y="214" width="640" height="6" fill="#fff" opacity=".7"/>
<!-- prédios -->
<rect x="20" y="70" width="90" height="120" fill="{NAVY2}"/><rect x="118" y="100" width="70" height="90" fill="{NAVY}"/>
<g fill="#ffd2a8">{"".join(f'<rect x="{32+c*24}" y="{84+r*26}" width="12" height="14"/>' for c in range(3) for r in range(4))}</g>
<!-- casa -->
<path d="M430 120 L480 82 L530 120 V190 H430Z" fill="#fff"/><path d="M422 124 L480 76 L538 124" fill="none" stroke="{OR}" stroke-width="8" stroke-linejoin="round"/><rect x="468" y="146" width="24" height="44" fill="{NAVY}"/>
<!-- praça e pessoas -->
<rect x="220" y="176" width="170" height="14" rx="4" fill="{GRN}"/>
{"".join(f'<circle cx="{240+k*28}" cy="148" r="9" fill="{OR if k%2 else NAVY}"/><path d="M{228+k*28} 176 C {230+k*28} 158, {250+k*28} 158, {252+k*28} 176Z" fill="{OR if k%2 else NAVY}"/>' for k in range(5))}
<rect x="288" y="104" width="64" height="28" rx="6" fill="#fff" stroke="{GR}" stroke-width="2"/><text x="320" y="123" text-anchor="middle" font-weight="900" font-size="11" fill="{GR}">PROTESTO</text><line x1="320" y1="132" x2="320" y2="150" stroke="{GR}" stroke-width="2"/>
<!-- celular / balão -->
<rect x="560" y="120" width="44" height="72" rx="8" fill="{GR}"/><rect x="565" y="128" width="34" height="52" rx="3" fill="#fff"/><path d="M570 138h24M570 148h24M570 158h16" stroke="{OR}" stroke-width="3"/>
<!-- viatura -->
<rect x="140" y="196" width="76" height="22" rx="6" fill="#fff" stroke="{NAVY}" stroke-width="2"/><rect x="150" y="186" width="44" height="14" rx="4" fill="#fff" stroke="{NAVY}" stroke-width="2"/><circle cx="156" cy="220" r="6" fill="{GR}"/><circle cx="200" cy="220" r="6" fill="{GR}"/><rect x="166" y="181" width="12" height="5" fill="{RED}"/>
''' + "".join(f'<g transform="translate({x},{y})"><circle r="15" fill="{OR}" stroke="#fff" stroke-width="3"/><text y="5" text-anchor="middle" font-weight="900" font-size="14" fill="#fff">{n}</text></g>' for x,y,n in [(320,80,"1"),(480,60,"2"),(582,104,"3"),(178,166,"4")]) + '</svg>'
sit = [("1","Protesto na praça","Todos podem se reunir pacificamente, sem armas, em local aberto ao público, <b>sem autorização</b>: basta o <b>prévio aviso</b> à autoridade.","XVI"),
 ("2","A casa da Dona Rosa","A casa é asilo inviolável. Sem consentimento, só se entra em <b>flagrante, desastre ou socorro</b> (a qualquer hora) ou por <b>ordem judicial, durante o dia</b>.","XI"),
 ("3","Crítica nas redes","É livre a manifestação do pensamento, <b>vedado o anonimato</b>. Quem for ofendido tem direito de resposta e indenização.","IV e V"),
 ("4","Prisão ilegal","Quem sofre ou está ameaçado de sofrer coação ilegal na liberdade de locomoção pode usar o <b><i>habeas corpus</i></b>, gratuito e sem advogado.","LXVIII")]
tiles = [("Pena de morte","Proibida, salvo guerra declarada (XLVII)"),("Tortura","Ninguém será submetido a ela (III)"),("Legalidade","Ninguém é obrigado a fazer algo senão em virtude de lei (II)"),
 ("Sigilo telefônico","Só por ordem judicial, para fins penais (XII)"),("Associação","Dissolução só por decisão judicial transitada em julgado (XIX)"),("Petição","Assegurada a todos, sem pagamento de taxas (XXXIV)")]
page(f'''{title("Assunto 2 · Exemplo prático","Um dia na <span class='hl'>cidade</span>","Quatro situações comuns e o inciso do art. 5º que resolve cada uma.")}
{city}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:7pt;margin:9pt 0 10pt">''' + "".join(f'<div style="display:flex;gap:8pt;border-bottom:1.5px solid {GRAY2};padding-bottom:6pt"><div style="flex:none;width:24pt;height:24pt;border-radius:50%;background:{OR};color:#fff;font-weight:900;display:flex;align-items:center;justify-content:center">{n}</div><div><b style="color:{NAVY}">{t}</b> <span class="chip o" style="font-size:7.5pt">inciso {inc}</span><div style="font-size:9.4pt;line-height:1.38;margin-top:2pt">{d}</div></div></div>' for n,t,d,inc in sit) + f'''</div>
<div style="background:{NAVY};border-radius:14pt;padding:10pt 12pt">
<div style="display:flex;justify-content:space-between;color:#fff;margin-bottom:7pt"><b style="letter-spacing:1.5pt;font-size:9.5pt;color:#fff">RESUMO VISUAL · MAIS 6 PONTOS DO ART. 5º</b><span style="color:{OR};font-weight:800;font-size:8.5pt">revise em 1 minuto</span></div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6pt">''' + "".join(f'<div style="background:#fff;border-radius:9pt;padding:6pt 9pt"><b style="color:{OR};font-size:9pt;text-transform:uppercase">{a}</b><div style="font-size:8.9pt;line-height:1.32">{b}</div></div>' for a,b in tiles) + '</div></div>',
 "Direitos e garantias", "Exemplo prático", demo="Resumo visual")

# ================================================================ 8. ADMINISTRATIVO
limpe = [("L","Legalidade","O servidor só faz o que a lei <b>permite</b>.","A diretora de escola não pode criar uma “taxa de matrícula” sem lei.","só o que a lei permite"),
 ("I","Impessoalidade","Atuar para todos, sem favorecer nem perseguir.","Placa de obra com foto e slogan do prefeito é proibida (art. 37, § 1º).","promoção pessoal"),
 ("M","Moralidade","Agir com ética, honestidade e boa-fé.","Nomear o sobrinho para cargo em comissão: nepotismo (Súmula Vinculante 13).","nepotismo"),
 ("P","Publicidade","Transparência dos atos públicos.","Contratos e salários no portal da transparência.","sigilo é exceção"),
 ("E","Eficiência","Bons resultados, com rapidez e economia.","Agendamento on-line no posto de saúde em vez de fila de madrugada.","EC nº 19/1998")]
rows = "".join(f'''<div style="display:grid;grid-template-columns:46pt 1fr 1.25fr;gap:9pt;align-items:center;padding:7pt 0;border-bottom:1.5px solid {GRAY2}">
<div style="width:42pt;height:42pt;border-radius:11pt;background:{OR if i%2==0 else NAVY};color:#fff;font-family:'Inter Display';font-weight:900;font-size:24pt;display:flex;align-items:center;justify-content:center">{l}</div>
<div><b style="color:{NAVY};font-size:11pt;text-transform:uppercase">{n}</b><div style="font-size:9.6pt;line-height:1.35">{d}</div></div>
<div style="font-size:9.4pt;line-height:1.35"><span style="font-weight:900;color:{OR};font-size:7.8pt;letter-spacing:1pt">NA PRÁTICA ·</span> {e}<br><span class="chip" style="font-size:7.5pt;margin-top:2pt;display:inline-block">{k}</span></div></div>''' for i,(l,n,d,e,k) in enumerate(limpe))
page(f'''{title("Assunto 3 · Direito Administrativo","Os princípios <span class='hl'>LIMPE</span>","As cinco regras de ouro de quem trabalha no serviço público, no caput do art. 37.")}
{law("Art. 37, caput · Constituição Federal","Art. 37. A administração pública direta e indireta de qualquer dos Poderes da União, dos Estados, do Distrito Federal e dos Municípios obedecerá aos princípios de legalidade, impessoalidade, moralidade, publicidade e eficiência e, também, ao seguinte:")}
{rows}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:9pt;margin-top:10pt">
<div style="border:2px solid {NAVY};border-radius:12pt;padding:8pt 11pt"><b style="color:{NAVY}">CIDADÃO</b> (art. 5º, II): pode fazer <b>tudo o que a lei não proíbe</b>.<br><span class="note">A lei é uma cerca: dentro dela, tudo é permitido.</span></div>
<div style="border:2px solid {OR};border-radius:12pt;padding:8pt 11pt"><b style="color:#b35a0c">ADMINISTRAÇÃO</b> (art. 37): só pode fazer <b>o que a lei permite</b>.<br><span class="note">A lei é um trilho: só se anda por onde ele passa.</span></div></div>
<div style="margin-top:10pt">{memo("<b>LIMPE</b>: Legalidade, Impessoalidade, Moralidade, Publicidade e Eficiência. Valem para a administração <b>direta e indireta</b> de <b>todos os Poderes</b>, na União, nos Estados, no DF e nos Municípios.","Mnemônico:")}</div>''',
 "Direito Administrativo", "Princípios da Administração")

# ================================================================ 9. MAPA MENTAL
mm_nodes = [(320,60,"LEGALIDADE",["só o que a lei permite","decreto não cria obrigação","≠ legalidade do cidadão"],NAVY,"#e6ebf4"),
 (560,175,"IMPESSOALIDADE",["finalidade pública","sem promoção pessoal","concurso e licitação"],OR,ORS),
 (480,395,"MORALIDADE",["ética e boa-fé","nepotismo: SV 13","até o 3º grau"],RED,REDS),
 (160,395,"PUBLICIDADE",["transparência","sigilo é exceção","≠ propaganda pessoal"],NAVY2,"#e8edf8"),
 (80,175,"EFICIÊNCIA",["resultados e economia","entrou com a EC 19/1998","avaliação de desempenho"],GRN,GRNS)]
mm = f'<svg viewBox="0 0 640 480" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
for x,y,t,ls,c,bg in mm_nodes:
    mm += f'<path d="M320 235 Q {(320+x)/2+ (30 if x>320 else -30)} {(235+y)/2} {x} {y}" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round" opacity=".55"/>'
mm += f'<circle cx="320" cy="235" r="78" fill="{NAVY}"/><circle cx="320" cy="235" r="66" fill="none" stroke="{OR}" stroke-width="2" stroke-dasharray="4 5"/><text x="320" y="228" text-anchor="middle" font-family="Inter Display" font-weight="900" font-size="34" fill="#fff">LIMPE</text><text x="320" y="252" text-anchor="middle" font-weight="800" font-size="11" fill="{OR}">ART. 37, CAPUT</text>'
for x,y,t,ls,c,bg in mm_nodes:
    mm += f'<rect x="{x-82}" y="{y-44}" width="164" height="94" rx="14" fill="{bg}" stroke="{c}" stroke-width="2.5"/><rect x="{x-82}" y="{y-44}" width="164" height="24" rx="12" fill="{c}"/><rect x="{x-82}" y="{y-32}" width="164" height="12" fill="{c}"/><text x="{x}" y="{y-27}" text-anchor="middle" font-weight="900" font-size="12" fill="#fff">{t}</text>'
    mm += "".join(f'<text x="{x-72}" y="{y-2+i*17}" font-size="11" fill="{GR}">• {l}</text>' for i,l in enumerate(ls))
mm += '</svg>'
page(f'''{title("Assunto 3 · Mapa mental","LIMPE em <span class='hl'>um olhar</span>","Use este mapa para revisar. Tente explicar cada galho em voz alta, sem olhar.")}
{mm}
<div style="display:grid;grid-template-columns:1.1fr .9fr;gap:9pt;margin-top:4pt">
{trap(["Os princípios <b>expressos</b> no caput são só os cinco do LIMPE. Razoabilidade e proporcionalidade são <b>implícitos</b> na Constituição.","Os princípios valem para a administração <b>direta e indireta</b>, de <b>todos os Poderes</b> e de <b>todos os entes</b>."])}
{memo("A <b>eficiência</b> foi a última a entrar no art. 37, com a <b>Emenda Constitucional nº 19/1998</b>.")}</div>''',
 "Direito Administrativo", "Mapa mental", demo="Mapa mental")

# ================================================================ 10. PENAL · conceito
stairs = f'''<svg viewBox="0 0 640 230" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<rect x="20" y="150" width="190" height="70" rx="8" fill="{NAVY}"/><rect x="220" y="95" width="190" height="125" rx="8" fill="{NAVY2}"/><rect x="420" y="40" width="200" height="180" rx="8" fill="{OR}"/>
<text x="115" y="180" text-anchor="middle" font-weight="900" font-size="16" fill="#fff">1. FATO TÍPICO</text><text x="115" y="200" text-anchor="middle" font-size="11" fill="#cdd6e8">a conduta está descrita na lei</text>
<text x="315" y="125" text-anchor="middle" font-weight="900" font-size="16" fill="#fff">2. ILÍCITO</text><text x="315" y="145" text-anchor="middle" font-size="11" fill="#cdd6e8">contrário ao Direito</text><text x="315" y="161" text-anchor="middle" font-size="11" fill="#cdd6e8">(sem excludente)</text>
<text x="520" y="70" text-anchor="middle" font-weight="900" font-size="16" fill="{NAVY}">3. CULPÁVEL</text><text x="520" y="90" text-anchor="middle" font-size="11" fill="{NAVY}">o agente merece</text><text x="520" y="106" text-anchor="middle" font-size="11" fill="{NAVY}">reprovação</text>

<text x="520" y="190" text-anchor="middle" font-family="Inter Display" font-weight="900" font-size="24" fill="#fff">= CRIME</text>
</svg>'''
page(f'''{title("Assunto 4 · Direito Penal","O que é <span class='hl'>crime</span>?","Dois jeitos de responder: o que a lei diz e como a doutrina analisa um crime.")}
<h2>1. Crime x contravenção: o critério da lei</h2>
{law("Decreto-Lei nº 3.914/1941 (Lei de Introdução ao Código Penal) · art. 1º","Art. 1º Considera-se crime a infração penal que a lei comina pena de reclusão ou de detenção, quer isoladamente, quer alternativa ou cumulativamente com a pena de multa; contravenção, a infração penal a que a lei comina, isoladamente, pena de prisão simples ou de multa, ou ambas, alternativa ou cumulativamente.")}
<div style="display:grid;grid-template-columns:1fr 46pt 1fr;align-items:stretch;margin-bottom:10pt">
<div style="background:{NAVY};color:#fff;border-radius:12pt;padding:9pt 12pt"><div style="font-weight:900;color:{OR};letter-spacing:1pt">CRIME (OU DELITO)</div><div style="font-size:10pt;margin-top:3pt"><b style="color:#fff">Reclusão</b> ou <b style="color:#fff">detenção</b>, sozinhas ou com multa.<br><span style="color:#c9d3e6">Ex.: furto (art. 155 do CP).</span></div></div>
<div style="display:flex;align-items:center;justify-content:center;font-weight:900;color:{GR2};font-size:9pt;text-align:center">INFRAÇÃO<br>PENAL</div>
<div style="background:{GRAY};border-radius:12pt;padding:9pt 12pt"><div style="font-weight:900;color:{NAVY};letter-spacing:1pt">CONTRAVENÇÃO</div><div style="font-size:10pt;margin-top:3pt"><b>Prisão simples</b> e/ou <b>multa</b>.<br><span class="note">É o “crime-anão”: infração de menor gravidade.</span></div></div></div>
<h2>2. O conceito analítico: a escada do crime</h2>
<p>Para a doutrina majoritária (teoria <b>tripartida</b>), crime é um fato <b>típico</b>, <b>ilícito</b> e <b>culpável</b>. Só existe crime se os três degraus forem vencidos.</p>
{stairs}
{trad("Pense numa escada de três degraus. Primeiro: a conduta está descrita na lei como crime? Segundo: ela foi contra o Direito, ou havia uma justificativa, como a legítima defesa? Terceiro: dá para reprovar o autor, ou ele era, por exemplo, menor de 18 anos? Só quem chega ao topo comete crime.")}''',
 "Direito Penal", "Conceito de crime", demo="Conteúdo simplificado")

# ================================================================ 11. PENAL · fluxograma
fx = f'''<svg viewBox="0 0 640 400" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<defs><marker id="fa" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L10,5 L0,10z" fill="{GR}"/></marker></defs>
''' + "".join(
 f'<rect x="20" y="{y}" width="330" height="64" rx="14" fill="#fff" stroke="{c}" stroke-width="2.8"/><text x="185" y="{y+26}" text-anchor="middle" font-weight="900" font-size="13.5" fill="{c}">{q}</text><text x="185" y="{y+46}" text-anchor="middle" font-size="11" fill="{GR2}">{s}</text>'
 f'<line x1="350" y1="{y+32}" x2="418" y2="{y+32}" stroke="{RED}" stroke-width="3" marker-end="url(#fa)"/><text x="384" y="{y+24}" text-anchor="middle" font-weight="900" font-size="10.5" fill="{RED}">{no}</text>'
 f'<rect x="424" y="{y+4}" width="196" height="56" rx="12" fill="{REDS}" stroke="{RED}" stroke-width="2"/><text x="522" y="{y+28}" text-anchor="middle" font-weight="900" font-size="12.5" fill="{RED}">{r1}</text><text x="522" y="{y+46}" text-anchor="middle" font-size="10.5" fill="{GR}">{r2}</text>'
 + (f'<line x1="185" y1="{y+64}" x2="185" y2="{y+94}" stroke="{GRN}" stroke-width="3" marker-end="url(#fa)"/><text x="200" y="{y+84}" font-weight="900" font-size="10.5" fill="{GRN}">SIM</text>' if last else '')
 for y,q,s,no,r1,r2,c,last in [
  (10,"1. O fato é típico?","conduta + resultado + nexo causal + tipicidade","NÃO","NÃO HÁ CRIME","fato atípico",NAVY,True),
  (110,"2. O fato é ilícito?","não há excludente do art. 23 do CP?","NÃO","NÃO HÁ CRIME","há excludente (ex.: legítima defesa)",NAVY2,True),
  (210,"3. O agente é culpável?","imputável · consciência da ilicitude · exigibilidade","NÃO","ISENTO DE PENA","ex.: inimputável (arts. 26 e 27)",OR,True)]) + f'''
<rect x="60" y="314" width="250" height="56" rx="14" fill="{GRNS}" stroke="{GRN}" stroke-width="2.8"/><text x="185" y="348" text-anchor="middle" font-family="Inter Display" font-weight="900" font-size="20" fill="{GRN}">HÁ CRIME</text>
</svg>'''
page(f'''{title("Assunto 4 · Diagrama explicativo","Houve <span class='hl'>crime</span>? Siga o fluxo","Responda às perguntas na ordem. Basta um “não” para não haver crime.")}
{fx}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:9pt">
{law("Art. 23 · Código Penal","Art. 23. Não há crime quando o agente pratica o fato: I - em estado de necessidade; II - em legítima defesa; III - em estrito cumprimento de dever legal ou no exercício regular de direito.")}
<div style="background:{GRAY};border-radius:12pt;padding:9pt 12pt"><div class="kicker" style="font-size:8pt">Caso prático</div><p style="font-size:9.6pt;margin:3pt 0 0">Pedro é atacado com uma faca na rua e se defende com um empurrão que machuca o agressor. A lesão é um fato <b>típico</b>, mas Pedro agiu em <b>legítima defesa</b>: repeliu, com moderação, uma injusta agressão atual (art. 25). O fato <b>não é ilícito</b>, logo <b>não há crime</b>.</p></div></div>
{trap(["Legítima defesa e estado de necessidade afastam a <b>ilicitude</b> (degrau 2). A menoridade afasta a <b>culpabilidade</b> (degrau 3): os menores de 18 anos são penalmente inimputáveis (art. 27).","Salvo os casos expressos em lei, só se pune o crime <b>doloso</b>; o culposo depende de previsão legal (art. 18, parágrafo único)."])}''',
 "Direito Penal", "Diagrama explicativo", demo="Esquema visual")

# ================================================================ 12. PORTUGUÊS
errs = [("EXTRAPOLAÇÃO","vai além do texto",RED,"O texto fala em reduzir a sensação de insegurança; a alternativa diz que a criminalidade acabou."),
 ("REDUÇÃO","fica aquém do texto",OR,"O texto cita três benefícios; a alternativa trata um deles como a única ideia."),
 ("CONTRADIÇÃO","diz o oposto do texto",NAVY,"O texto defende manutenção contínua; a alternativa diz que a obra encerra o problema.")]
target = lambda c, kind: (f'<svg viewBox="0 0 120 120" width="76"><circle cx="60" cy="60" r="44" fill="none" stroke="{GRAY2}" stroke-width="10"/><circle cx="60" cy="60" r="22" fill="{GRNS}" stroke="{GRN}" stroke-width="3"/>' +
  ({"EXTRAPOLAÇÃO":f'<circle cx="100" cy="22" r="10" fill="{c}"/>',"REDUÇÃO":f'<circle cx="60" cy="60" r="8" fill="{c}"/><path d="M60 60 m-16 0 a16 16 0 0 1 16-16" stroke="{c}" stroke-width="4" fill="none"/>',"CONTRADIÇÃO":f'<path d="M30 30 L90 90 M90 30 L30 90" stroke="{c}" stroke-width="8" stroke-linecap="round"/>'}[kind]) + '</svg>')
page(f'''{title("Assunto 5 · Língua Portuguesa","Interpretação de <span class='hl'>texto</span>","A disciplina que aparece em praticamente todos os concursos, e que se aprende com método.")}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:9pt;margin-bottom:10pt">
<div style="border-top:5px solid {NAVY};background:#f6f7f9;border-radius:0 0 12pt 12pt;padding:9pt 12pt"><div style="font-weight:900;color:{NAVY};font-size:11.5pt">COMPREENDER</div><p style="font-size:9.8pt;margin:3pt 0 0">É entender o que está <b>escrito</b>. Responde à pergunta: <i>“o que o texto diz?”</i>. Pistas na questão: “segundo o texto”, “de acordo com o autor”.</p></div>
<div style="border-top:5px solid {OR};background:#f6f7f9;border-radius:0 0 12pt 12pt;padding:9pt 12pt"><div style="font-weight:900;color:#b35a0c;font-size:11.5pt">INTERPRETAR</div><p style="font-size:9.8pt;margin:3pt 0 0">É tirar <b>conclusões</b> que o texto permite, sem inventar. Responde: <i>“o que se pode concluir?”</i>. Pistas: “infere-se”, “depreende-se”, “conclui-se”.</p></div></div>
<h2>Os 3 erros que as alternativas erradas cometem</h2>
''' + "".join(f'<div style="display:grid;grid-template-columns:84px 1fr;gap:9pt;align-items:center;padding:6pt 0;border-bottom:1.5px solid {GRAY2}"><div>{target(c,t)}</div><div><b style="color:{c};font-size:11.5pt">{t}</b> <span style="font-weight:800;color:{GR2}">· {s}</span><div style="font-size:9.6pt;margin-top:2pt">{d}</div></div></div>' for t,s,c,d in errs) +
 f'''<h2 style="margin-top:11pt">Conectivos que mudam o sentido</h2>
{"<table><tr><th style='width:25%'>Sentido</th><th>Exemplos</th><th style='width:38%'>O que indica</th></tr>" + "".join(f"<tr><td class='rh'>{a}</td><td>{b}</td><td>{c}</td></tr>" for a,b,c in [("Oposição","mas, porém, no entanto, contudo, todavia","vem aí a ideia mais importante"),("Conclusão","portanto, logo, por isso, assim","o resultado do raciocínio"),("Causa","porque, pois, já que, visto que","o motivo de algo"),("Concessão","embora, ainda que, mesmo que","admite algo, mas mantém a ideia principal")]) + "</table>"}
{memo("depois de <b>mas, porém, no entanto</b>, quase sempre vem a ideia que o autor quer defender.","Dica de ouro:")}''',
 "Língua Portuguesa", "Interpretação de texto")

# ================================================================ 13. PORTUGUÊS · método
TEXTO = ('<span class="mk1">Durante muito tempo, as praças foram vistas apenas como lugares de passagem.</span> <span class="mk2">Hoje, no entanto,</span> muitas cidades perceberam que um espaço público bem cuidado muda a rotina de um bairro inteiro: atrai famílias, movimenta o comércio local e reduz a sensação de insegurança. <span class="mk2">Não basta, porém,</span> instalar bancos e luminárias. Sem manutenção constante e sem a participação dos moradores, a praça reformada volta a ser abandonada em poucos meses. <span class="mk2">Por isso,</span> <span class="mk3">especialistas defendem que a revitalização seja pensada como um processo contínuo, e não como uma obra que termina no dia da inauguração.</span>')
metodo = [("1","Leia o título e as perguntas antes","Você passa a ler o texto já sabendo o que procurar."),
 ("2","Faça uma leitura corrida","Sem marcar nada: só para entender o assunto geral."),
 ("3","Marque o esqueleto do texto","Ideia principal, conectivos e conclusão (veja ao lado)."),
 ("4","Volte ao texto para cada alternativa","Nunca responda “de memória”: confira a linha."),
 ("5","Elimine pelos 3 erros","Extrapolação, redução e contradição.")]
page(f'''{title("Assunto 5 · Método prático","Como ler e <span class='hl'>marcar</span> um texto","Um método em cinco passos, aplicado a um texto curto escrito para este guia.")}
<style>.mk1{{background:#e6ebf4;border-bottom:2px solid {NAVY};}} .mk2{{background:{OR2};font-weight:800;padding:0 2px;border-radius:3px}} .mk3{{background:#cdeedd;border-bottom:2px solid {GRN};}}</style>
<div style="display:grid;grid-template-columns:.85fr 1.15fr;gap:11pt">
<div>''' + "".join(f'<div style="display:flex;gap:8pt;margin-bottom:9pt"><div style="flex:none;width:28pt;height:28pt;border-radius:8pt;background:{NAVY if int(n)%2 else OR};color:#fff;font-weight:900;font-size:14pt;display:flex;align-items:center;justify-content:center">{n}</div><div><b style="color:{NAVY};font-size:10.3pt">{t}</b><div style="font-size:9.3pt;color:{GR2};line-height:1.35">{d}</div></div></div>' for n,t,d in metodo) + f'''</div>
<div><div style="border:2px solid {GR};border-radius:12pt;padding:11pt 13pt;background:#fff;position:relative">
<div class="kicker" style="font-size:8pt;margin-bottom:5pt">Texto de apoio · autoral</div>
<p style="font-family:'DejaVu Serif',Georgia,serif;font-size:10.2pt;line-height:1.7;margin:0">{TEXTO}</p></div>
<div style="display:flex;flex-direction:column;gap:4pt;margin-top:8pt;font-size:9.2pt">
<div><span class="mk1" style="padding:0 6px">azul</span> situação antiga (ponto de partida)</div>
<div><span class="mk2">laranja</span> conectivos: virada de ideia e conclusão</div>
<div><span class="mk3" style="padding:0 6px">verde</span> ideia principal / tese do autor</div></div></div></div>
<div style="background:{NAVY};color:#fff;border-radius:14pt;padding:10pt 14pt;margin-top:12pt;display:grid;grid-template-columns:auto 1fr;gap:12pt;align-items:center">
<svg width="44" height="44" style="color:{OR}"><use href="#i-target"/></svg>
<div><b style="color:{OR};letter-spacing:1pt">O ESQUELETO DO TEXTO</b><div style="font-size:10pt;margin-top:3pt;color:#e1e7f2">Antes, praças eram só passagem → <b style="color:#fff">no entanto</b>, praças cuidadas trazem benefícios → <b style="color:#fff">porém</b>, a obra sozinha não basta → <b style="color:#fff">por isso</b>, a revitalização deve ser um <b style="color:{OR}">processo contínuo</b>.</div></div></div>
<p class="note" style="margin-top:9pt">As questões 9, 10 e 11 usam este texto. Tente resolvê-las aplicando o método.</p>''',
 "Língua Portuguesa", "Método prático")

# ================================================================ 14-15. QUESTÕES
Q = [
 ("Constitucional","Constitui fundamento da República Federativa do Brasil, nos termos do art. 1º da Constituição:",
  ["a independência nacional.","a erradicação da pobreza.","o pluralismo político.","a prevalência dos direitos humanos.","a garantia do desenvolvimento nacional."],"C",
  "O pluralismo político é fundamento (art. 1º, V). A independência nacional e a prevalência dos direitos humanos são princípios do art. 4º; erradicar a pobreza e garantir o desenvolvimento nacional são objetivos do art. 3º."),
 ("Constitucional","Sobre os objetivos fundamentais da República (art. 3º), assinale a alternativa correta.",
  ["Erradicar as desigualdades sociais e regionais.","Reduzir a pobreza e a marginalização.","Erradicar a pobreza e a marginalização e reduzir as desigualdades sociais e regionais.","Garantir a soberania nacional.","Assegurar a dignidade da pessoa humana como objetivo."],"C",
  "É o texto do art. 3º, III. As alternativas A e B invertem os verbos: a pobreza é erradicada e as desigualdades são reduzidas. Soberania e dignidade são fundamentos (art. 1º)."),
 ("Art. 5º","Moradores de um bairro pretendem fazer um protesto pacífico, sem armas, numa praça pública. Segundo a Constituição, eles devem:",
  ["obter autorização prévia do prefeito.","obter autorização judicial.","apenas avisar previamente a autoridade competente, sem frustrar reunião anteriormente convocada para o mesmo local.","pagar uma taxa de uso do espaço público.","realizar o protesto apenas em local fechado."],"C",
  "Art. 5º, XVI: a reunião independe de autorização; exige-se apenas o prévio aviso à autoridade competente, sem frustrar outra reunião anteriormente convocada para o mesmo local."),
 ("Art. 5º","Com mandado judicial de busca, policiais querem entrar numa casa às 23h, sem consentimento do morador e sem flagrante. Nesse caso:",
  ["podem entrar, pois têm ordem judicial.","não podem entrar, pois a determinação judicial só autoriza o ingresso durante o dia.","podem entrar se estiverem acompanhados de duas testemunhas.","podem entrar com autorização do delegado.","só podem entrar se o morador for estrangeiro."],"B",
  "Art. 5º, XI: sem consentimento, a entrada só é permitida em flagrante, desastre ou para prestar socorro (a qualquer hora), ou durante o dia, por determinação judicial."),
 ("Administrativo","São princípios expressos no caput do art. 37 da Constituição:",
  ["legalidade, razoabilidade, moralidade, publicidade e eficiência.","legalidade, impessoalidade, moralidade, publicidade e eficiência.","legalidade, impessoalidade, motivação, publicidade e eficiência.","supremacia do interesse público, impessoalidade, moralidade, publicidade e eficiência.","legalidade, impessoalidade, moralidade, proporcionalidade e eficiência."],"B",
  "LIMPE. Razoabilidade, motivação, supremacia do interesse público e proporcionalidade são princípios implícitos na Constituição."),
 ("Administrativo","O prefeito mandou colocar sua foto e o slogan “Gestão Fulano” nas placas de todas as obras municipais. A medida viola, de modo mais direto, o princípio da:",
  ["eficiência.","impessoalidade.","legalidade tributária.","continuidade do serviço público.","autotutela."],"B",
  "O art. 37, § 1º, proíbe nomes, símbolos ou imagens que caracterizem promoção pessoal de autoridades na publicidade oficial, expressão do princípio da impessoalidade."),
 ("Penal","Segundo a Lei de Introdução ao Código Penal, a infração penal para a qual a lei comina, isoladamente, pena de prisão simples é:",
  ["crime doloso.","crime culposo.","contravenção penal.","crime hediondo.","delito de menor potencial, sempre punido com reclusão."],"C",
  "Pelo art. 1º do Decreto-Lei nº 3.914/1941, crime é punido com reclusão ou detenção; contravenção, com prisão simples e/ou multa."),
 ("Penal","Ana, atacada por um agressor armado com uma faca, defendeu-se moderadamente com os meios de que dispunha e feriu o agressor. Segundo o Código Penal:",
  ["Ana cometeu crime, pois feriu outra pessoa.","não há crime, pois Ana agiu em legítima defesa, causa que exclui a ilicitude.","Ana é isenta de pena por ser inimputável.","há crime culposo, pois Ana não quis ferir.","o fato é atípico, pois lesão corporal não é crime."],"B",
  "Legítima defesa (art. 25) é excludente de ilicitude: “não há crime” (art. 23, II). O fato é típico, mas não é ilícito."),
 ("Português","Leia o texto da página 13. A ideia principal defendida no texto é a de que:",
  ["as praças devem ser apenas lugares de passagem.","bancos e luminárias bastam para revitalizar uma praça.","a revitalização das praças deve ser um processo contínuo, com manutenção e participação dos moradores.","as cidades devem deixar de investir em praças.","o comércio local é o único beneficiado pelas praças."],"C",
  "A tese aparece depois do conectivo conclusivo “Por isso”. A é a visão antiga que o texto supera; B contradiz o texto (“Não basta”); D contradiz; E é redução (o comércio é um dos benefícios)."),
 ("Português","No trecho “Hoje, no entanto, muitas cidades perceberam...”, a expressão “no entanto” estabelece relação de:",
  ["causa.","conclusão.","oposição.","finalidade.","tempo."],"C",
  "“No entanto” é conectivo de oposição (adversativo): contrapõe a visão antiga (praças como passagem) à percepção atual."),
 ("Português","De acordo com o texto da página 13, é correto inferir que:",
  ["as praças reformadas acabam com a criminalidade do bairro.","sem manutenção, o investimento em uma praça pode ser perdido em pouco tempo.","os moradores atrapalham a conservação das praças.","a inauguração é a etapa mais importante da revitalização.","as praças não influenciam a rotina dos bairros."],"B",
  "O texto afirma que, sem manutenção, a praça “volta a ser abandonada em poucos meses”. A é extrapolação (o texto fala em reduzir a sensação de insegurança); C, D e E contradizem o texto.")]
def qhtml(i,q):
    t,e,alts,_,_ = q
    return f'<div class="q"><div class="qh"><span class="qn">Questão {i:02d}</span><span class="qt">Questão autoral · {t}</span></div><p>{e}</p><ol>{"".join(f"<li data-l=\"{"ABCDE"[j]}\">{a}</li>" for j,a in enumerate(alts))}</ol></div>'
page(title("Prática","Questões de <span class='hl'>fixação</span>","Questões autorais, no estilo de concursos. Resolva sem consultar e confira o gabarito na página 17.") + "".join(qhtml(i+1,Q[i]) for i in range(4)), "Prática", "Questões de fixação")
page("".join(qhtml(i+1,Q[i]) for i in range(4,8)), "Prática", "Questões de fixação")
page("".join(qhtml(i+1,Q[i]) for i in range(8,11)) + memo("terminou? Confira o gabarito comentado na próxima página e anote os assuntos em que errou para revisar.","Próximo passo:"), "Prática", "Questões de fixação")

# ================================================================ 16. GABARITO
grid = "<table style='margin-bottom:9pt'><tr>" + "".join(f"<th style='text-align:center'>{i+1:02d}</th>" for i in range(11)) + "</tr><tr>" + "".join(f"<td style='text-align:center;font-weight:900;color:{NAVY}'>{q[3]}</td>" for q in Q) + "</tr></table>"
page(title("Correção","Gabarito <span class='hl'>comentado</span>") + grid + "".join(f'<div class="g"><div class="gh">Questão {i+1:02d}<span>{q[3]}</span></div><p>{q[4]}</p></div>' for i,q in enumerate(Q)),
 "Correção", "Gabarito comentado", demo="Questão comentada")

# ================================================================ 17. COLEÇÃO
disc = [("book","Direito Constitucional"),("shield","Direitos e Garantias Fundamentais"),("gavel","Direito Penal"),("capitol","Direito Administrativo"),("heart","Direitos Humanos"),
 ("car","CTB · Código de Trânsito"),("grid","Informática"),("pen","Língua Portuguesa"),("puzzle","Raciocínio Lógico"),("badge","Legislação das Guardas Municipais")]
thumbs = [("img/c02a-14.png","Página de conteúdo"),("img/c02b-42.png","Árvore de decisão"),("img/c03a-38.png","Página “Entenda na prática”")]
page(f'''<div class="kicker">A coleção completa</div><h1 style="font-size:27pt">Mapa da Aprovação<br><span class="hl">20 Cadernos Simplificados</span></h1>
<p class="lead" style="margin-bottom:8pt">Uma coleção de 20 cadernos digitais desenvolvidos para ajudar concurseiros a organizar seus estudos, compreender conteúdos importantes, revisar matérias e estudar com mais clareza.</p>
<div class="rule o"></div>
<h3>Disciplinas presentes na coleção (exemplos)</h3>
<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:6pt;margin-bottom:10pt">''' + "".join(f'<div style="border:1.8px solid {GRAY2};border-radius:10pt;padding:7pt 5pt;text-align:center"><svg width="26" height="26" style="color:{OR if i%2==0 else NAVY};margin:0 auto 3pt"><use href="#i-{n}"/></svg><div style="font-size:8.6pt;font-weight:800;color:{NAVY};line-height:1.2">{t}</div></div>' for i,(n,t) in enumerate(disc)) +
 f'''</div><p class="note" style="margin-top:-4pt">E outras disciplinas.</p>
<div style="display:grid;grid-template-columns:1fr 1.2fr;gap:12pt;align-items:start">
<div><h3>O que tem em cada caderno</h3>''' + "".join(f'<div style="display:flex;gap:7pt;align-items:flex-start;padding:3.5pt 0;font-size:9.8pt"><span style="color:{OR};font-weight:900">✓</span><span>{t}</span></div>' for t in ["Explicações em linguagem simples, assunto por assunto","Texto da lei com o “Traduzindo o juridiquês”","Esquemas, fluxogramas e mapas mentais","Exemplos práticos e situações do dia a dia","Pegadinhas de concurso destacadas","Treinos de Certo ou Errado e flashcards","Questões autorais com gabarito comentado","Legislação conferida em fontes oficiais, com data"]) + f'''</div>
<div><h3>Páginas reais dos cadernos de Direito Constitucional</h3>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6pt">''' + "".join(f'<figure style="margin:0"><img src="{src}" style="width:100%;border:1.5px solid {GRAY2};border-radius:4pt;box-shadow:0 3pt 8pt rgba(0,0,0,.18)"><figcaption style="font-size:7.6pt;color:{GR2};text-align:center;margin-top:3pt">{cap}</figcaption></figure>' for src,cap in thumbs) +
 '</div></div></div>', "A coleção", "20 cadernos")

# ================================================================ 18. CTA
page(f'''<div style="position:absolute;inset:0;background:{NAVY}"></div>
<div style="position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.06) 1.2px,transparent 1.3px);background-size:7mm 7mm"></div>
<div style="position:absolute;left:0;top:0;bottom:0;width:9mm;background:{OR}"></div>
<div style="position:absolute;left:24mm;right:20mm;top:30mm;color:#fff">
<div style="font-weight:900;letter-spacing:3pt;font-size:10pt;color:{OR}">MAPA DA APROVAÇÃO</div>
<div style="font-family:'Inter Display';font-weight:900;font-size:36pt;line-height:1;margin:10pt 0 16pt">Este foi só<br>o começo do <span style="color:{OR}">mapa</span>.</div>
<p style="font-size:13.5pt;line-height:1.5;color:#e1e7f2;max-width:150mm">Este mini guia é apenas uma pequena demonstração do que você encontrará na coleção completa <b style="color:#fff">MAPA DA APROVAÇÃO</b>.</p>
<p style="font-size:13.5pt;line-height:1.5;color:#e1e7f2;max-width:150mm">Conheça os <b style="color:#fff">20 cadernos completos</b> e descubra uma maneira mais organizada de estudar para concursos.</p>
<div style="display:flex;gap:14pt;margin:20pt 0">
''' + "".join(f'<div style="flex:1;border:1.5px solid rgba(255,255,255,.3);border-radius:12pt;padding:10pt 12pt"><div style="font-family:Inter Display;font-weight:900;font-size:22pt;color:{OR}">{a}</div><div style="font-size:10pt;color:#e1e7f2">{b}</div></div>' for a,b in [("20","cadernos digitais"),("5","assuntos de amostra neste guia"),("3","etapas por assunto: entender, visualizar e praticar")]) + f'''
</div>
<div style="background:#fff;border-radius:16pt;padding:16pt 18pt;color:{NAVY};text-align:center">
<div style="font-weight:900;letter-spacing:1.5pt;font-size:10pt;color:#b35a0c">CONHEÇA A COLEÇÃO COMPLETA</div>
<div style="margin:8pt auto 2pt;font-weight:800;font-size:12.5pt;line-height:1.4;color:{NAVY}">20 cadernos simplificados para concursos, com leis conferidas, cenas ilustradas e questões autorais comentadas.</div></div>
</div>
<div style="position:absolute;left:24mm;right:20mm;bottom:16mm;font-size:8pt;color:#9fb0cc;line-height:1.5">
Material gratuito e autoral, de caráter introdutório. Os trechos de lei foram conferidos no portal da legislação federal (Planalto) em {DATA}; confira sempre se houve alterações posteriores e consulte o edital do seu concurso. As questões são autorais e não foram aplicadas por banca. Este material não garante aprovação: ele foi feito para ajudar você a estudar com mais clareza.</div>''', full=True)

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Mapa da Aprovação — Mini Guia Gratuito</title>
<link rel="stylesheet" href="ebook.css"></head><body>{symbols()}{"".join(PAGES)}</body></html>'''
open(os.path.join(HERE, "ebook.html"), "w").write(html)
print("páginas:", len(PAGES))
