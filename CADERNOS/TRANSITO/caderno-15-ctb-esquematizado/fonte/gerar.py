"""Gera miolo.html do Caderno 15: Código de Trânsito Brasileiro Esquematizado. Uso: python3 gerar.py
Base legal conferida no portal do Planalto em 26/11/2026: Lei nº 9.503/1997 (CTB), texto compilado, inclusive Anexos I e II."""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit
from kit import *

DATA = "26 de novembro de 2026"
kit.U = {1:("UNIDADE 1","Conceitos fundamentais"),2:("UNIDADE 2","Sistema Nacional de Trânsito"),3:("UNIDADE 3","Circulação e condutores"),4:("UNIDADE 4","Pedestres e ciclistas"),5:("UNIDADE 5","Sinalização"),6:("UNIDADE 6","Habilitação e infrações")}
def ctb(x): return f"{x} · Código de Trânsito Brasileiro"
RED, YEL, GRN, BLU, BRN = "#d6332a", "#f5c518", "#2c8a5a", "#1565c0", "#7a4a1e"

# ---------- placas (desenhos didáticos) ----------
def pare(cx, cy, r=34):
    pts=" ".join(f"{cx+r*math.cos(math.radians(22.5+45*k)):.1f},{cy+r*math.sin(math.radians(22.5+45*k)):.1f}" for k in range(8))
    return f'<polygon points="{pts}" fill="{RED}" stroke="#fff" stroke-width="3"/><polygon points="{pts}" fill="none" stroke="{RED}" stroke-width="1.5" transform="translate(0,0)"/><text x="{cx}" y="{cy+6}" text-anchor="middle" font-size="{r*0.46:.0f}" font-weight="900" fill="#fff">PARE</text>'
def preferencia(cx, cy, s=36):
    return f'<polygon points="{cx-s},{cy-s*0.6} {cx+s},{cy-s*0.6} {cx},{cy+s*0.9}" fill="#fff" stroke="{RED}" stroke-width="6"/>'
def regulamentacao(cx, cy, txt, r=32, risco=False):
    s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{RED}" stroke-width="7"/><text x="{cx}" y="{cy+8}" text-anchor="middle" font-size="{r*0.62 if len(txt)<4 else r*0.42:.0f}" font-weight="900" fill="#22262b">{txt}</text>'
    if risco: s += f'<line x1="{cx-r*0.7:.0f}" y1="{cy-r*0.7:.0f}" x2="{cx+r*0.7:.0f}" y2="{cy+r*0.7:.0f}" stroke="{RED}" stroke-width="6"/>'
    return s
def advertencia(cx, cy, txt, s=30):
    return f'<polygon points="{cx},{cy-s*1.3} {cx+s*1.3},{cy} {cx},{cy+s*1.3} {cx-s*1.3},{cy}" fill="{YEL}" stroke="#22262b" stroke-width="3"/><text x="{cx}" y="{cy+8}" text-anchor="middle" font-size="22" font-weight="900" fill="#22262b">{txt}</text>'
def indicacao(cx, cy, txt, cor, w=96, h=50):
    return f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" rx="6" fill="{cor}" stroke="#fff" stroke-width="2"/><text x="{cx}" y="{cy+5}" text-anchor="middle" font-size="11" font-weight="900" fill="#fff">{txt}</text>'


def corte_via():
    N=C['navy']
    s = f'<figure><svg viewBox="0 0 640 210" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    # calçada esq, acostamento, pista (2 faixas), canteiro, ciclovia, calçada dir
    parts=[(0,70,"#d9d4c7","CALÇADA",22),(70,50,"#b9bcc0","ACOSTA-","MENTO"),(120,220,"#4a4f55","PISTA",0),(340,40,"#5fae6e","CANTEIRO",1),(380,60,C['red'],"CICLOVIA",2),(440,130,"#4a4f55","PISTA",0),(570,70,"#d9d4c7","CALÇADA",22)]
    for x,w,c,t,k in parts:
        y=60 if c in ("#d9d4c7","#5fae6e") else 70
        s += f'<rect x="{x}" y="{y}" width="{w}" height="{150-y}" fill="{c}"/>'
    s += '<g stroke="#fff" stroke-width="3"><line x1="120" y1="72" x2="120" y2="150"/></g>'
    s += f'<g stroke="{YEL}" stroke-width="4" stroke-dasharray="14 10"><line x1="230" y1="74" x2="230" y2="150"/></g>'
    s += f'<rect x="20" y="40" width="10" height="20" fill="#22262b"/><circle cx="25" cy="32" r="8" fill="#22262b"/>'
    s += f'<rect x="250" y="94" width="40" height="22" rx="5" fill="{BLU}"/><rect x="160" y="110" width="40" height="22" rx="5" fill="#e8e8e8"/>'
    s += f'<circle cx="410" cy="110" r="10" fill="none" stroke="#fff" stroke-width="3"/>'
    labels=[(35,"CALÇADA","pedestres"),(95,"ACOSTA-","MENTO"),(230,"PISTA","veículos (2 faixas)"),(410,"CICLOVIA","separada"),(505,"PISTA",""),(605,"CALÇADA","")]
    for x,a,b in labels:
        s += f'<text x="{x}" y="172" text-anchor="middle" font-size="10" font-weight="900" fill="{N}">{a}</text><text x="{x}" y="186" text-anchor="middle" font-size="9" fill="{C["muted"]}">{b}</text>'
    s += f'<text x="360" y="52" text-anchor="middle" font-size="10" font-weight="900" fill="{N}">CANTEIRO CENTRAL</text><line x1="360" y1="55" x2="360" y2="62" stroke="{N}" stroke-width="1.5"/>'
    s += f'<path d="M0 22 H640" stroke="{N}" stroke-width="2"/><text x="320" y="16" text-anchor="middle" font-size="11" font-weight="900" fill="{N}">VIA = pista + calçada + acostamento + ilha + canteiro central</text>'
    return s + '</svg><figcaption>Corte transversal didático de uma via (fora de escala).</figcaption></figure>'

def glossario():
    return corte_via() + table(["Termo (Anexo I)","Definição (em síntese)"],[
  ["Via","Superfície por onde transitam veículos, pessoas e animais; compreende a pista, a calçada, o acostamento, a ilha e o canteiro central"],
  ["Pista","Parte da via normalmente utilizada para a circulação de veículos"],
  ["Acostamento","Parte da via diferenciada da pista, para parada ou estacionamento de veículos em emergência e circulação de pedestres e bicicletas, quando não houver local apropriado"],
  ["Calçada x passeio","Calçada: parte da via, normalmente segregada e em nível diferente, reservada ao trânsito de pedestres (e mobiliário, sinalização, vegetação). Passeio: parte da calçada (ou da pista, separada por pintura ou elemento físico) livre de interferências, para pedestres e, excepcionalmente, ciclistas"],
  ["Ciclovia x ciclofaixa","Ciclovia: pista própria para ciclos, <b>separada fisicamente</b> do tráfego comum. Ciclofaixa: <b>parte da pista</b> de rolamento para ciclos, delimitada por sinalização específica"],
  ["Cruzamento x interseção","Cruzamento: interseção de duas vias em nível. Interseção: todo cruzamento em nível, entroncamento ou bifurcação"],
  ["Parada x estacionamento","Parada: imobilização pelo tempo <b>estritamente necessário</b> para embarque ou desembarque de passageiros. Estacionamento: imobilização por tempo <b>superior</b> a esse"],
  ["Ultrapassagem","Movimento de passar à frente de outro veículo que se desloca no mesmo sentido, em menor velocidade e na mesma faixa, saindo e retornando à faixa de origem"]],["24%",None])

def vias_box():
    return table(["Via urbana (Anexo I)","Característica"],[
  ["Trânsito rápido","Acessos especiais, trânsito livre, sem interseções em nível, sem acessibilidade direta aos lotes lindeiros e sem travessia de pedestres em nível"],
  ["Arterial","Interseções em nível, geralmente com semáforo, acesso aos lotes lindeiros e às vias secundárias e locais; liga regiões da cidade"],
  ["Coletora","Coleta e distribui o trânsito que precisa entrar ou sair das vias de trânsito rápido ou arteriais"],
  ["Local","Interseções em nível não semaforizadas; destinada apenas ao acesso local ou a áreas restritas"]],["24%",None])

def placas_txt():
    return table(["Família","Forma e cores (Anexo II)","Função"],[
  ["Regulamentação","Circular; fundo branco, orla e tarja vermelhas, símbolo preto. Exceções: <b>R-1</b> “Parada obrigatória” (octógono vermelho, letras brancas) e <b>R-2</b> “Dê a preferência” (triângulo com fundo branco e orla vermelha)","Informa condições, proibições, obrigações ou restrições; mensagens <b>imperativas</b>, cujo desrespeito constitui infração"],
  ["Advertência","Quadrada, com uma diagonal na vertical (losango); fundo amarelo, símbolo preto. Exceções de forma: A-26a (sentido único), A-26b (sentido duplo) e A-41 (cruz de Santo André)","Alerta para condições potencialmente perigosas, indicando sua natureza; caráter de <b>recomendação</b>"],
  ["Indicação","Em geral retangular. Orientação de destino: fundo <b>verde</b>. Serviços auxiliares e atrativos turísticos: fundo <b>azul</b>. Educativas: fundo branco","Identifica vias, destinos, distâncias, serviços e locais de interesse; caráter informativo ou educativo"]],["18%","46%",None]) + \
 pega('<ul><li>Placa de <b>obra</b> é placa de advertência com o fundo amarelo trocado por <b>laranja</b> (Anexo II, item 5.4).</li><li>A placa “Dê a preferência” é um triângulo com o vértice <b>para baixo</b>.</li><li>Regulamentação <b>obriga</b> (multa se descumprida); advertência <b>alerta</b>.</li></ul>')

def horizontal_txt():
    return table(["Cor da marca viária (Anexo II)","Uso"],[
  ["Amarela","Separa fluxos de <b>sentidos opostos</b>; delimita espaços proibidos para estacionamento ou parada; marca obstáculos"],
  ["Branca","Separa fluxos de <b>mesmo sentido</b>; delimita estacionamento regulamentado; faixas de travessia de pedestres; símbolos e legendas"],
  ["Vermelha","Espaço para bicicletas (ciclovias); símbolos de hospitais e farmácias (cruz)"],
  ["Azul","Símbolos em áreas especiais de estacionamento ou de parada para embarque e desembarque"],
  ["Preta","Contraste entre o pavimento e a pintura"]],["28%",None]) + \
 p('Quanto ao traçado, a linha <b>contínua</b> não tem interrupção e, separando fluxos, indica que não se deve transpô-la (por exemplo, proibindo a ultrapassagem); a linha <b>tracejada ou seccionada</b> permite a transposição com segurança.') + \
 table(["Semáforo (Anexo II)","Significado"],[
  ["Vermelho (veículos)","Obrigatoriedade de <b>parar</b>"],
  ["Amarelo (veículos)","“Atenção”: o condutor deve parar, salvo se isso resultar em situação de perigo para os veículos que vêm atrás"],
  ["Verde (veículos)","Permissão de prosseguir na marcha, efetuando a operação indicada"],
  ["Vermelho intermitente (pedestres)","A fase de travessia está terminando: não comece a atravessar; quem já começou deve concluir"]],["30%",None])
def gestos_txt():
    return table(["Gesto ou apito do agente (Anexo II)","Significado"],[
  ["Braço levantado verticalmente","Ordem de <b>parada obrigatória para todos</b> os veículos; em interseções, os que já estão nela não são obrigados a parar"],
  ["Braço(s) estendido(s) horizontalmente","Parada para os veículos que venham de direções que cortem ortogonalmente a direção indicada pelo braço"],
  ["Um silvo breve · dois silvos breves","“Atenção, siga” · “Pare!”"],
  ["Um silvo longo · um longo e um breve","“Diminua a marcha” · trânsito impedido em todas as direções"]],["34%",None])

# ================================================================ APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">O Código de Trânsito em esquemas: quem manda no trânsito, como se circula, como se sinaliza e o que dá multa e pontos.</p>
<p>Este é o <strong>Caderno 15 da coleção</strong>, dedicado ao <strong>Código de Trânsito Brasileiro</strong> (Lei nº 9.503/1997). Ele é cobrado em concursos de <strong>Guarda Municipal</strong>, <strong>agente de trânsito</strong>, <strong>PRF</strong>, <strong>polícias militares</strong> e <strong>Detrans</strong>. O CTB tem mais de 300 artigos; aqui estão, de forma esquematizada, os pontos mais presentes nos editais e na atuação prática.</p>
<p><strong>Atenção às mudanças:</strong> o CTB foi alterado muitas vezes desde 2020 (Leis nº 14.071/2020, 14.440/2022, 14.599/2023, 15.153/2025, 15.428/2026 e 15.503/2026, entre outras). Valores, pontos e prazos aqui conferem com o texto compilado do Planalto em <strong>{DATA}</strong>. Apostilas antigas podem trazer regras superadas, como a antiga pontuação única de 20 pontos para suspensão.</p>
{table(["Recurso","Onde está"],[["Glossário visual (via, pista, calçada, ciclovia, parada x estacionamento)","Unidade 1"],["Organograma do Sistema Nacional de Trânsito","Unidade 2"],["Cenas de preferência e ultrapassagem","Unidade 3"],["Placas de regulamentação, advertência e indicação","Unidade 5"],["Pirâmide da prevalência dos sinais","Unidade 5"],["Tabela de multas e pontos","Unidade 6"],["Mapa conceitual, erros mais comuns e 24 questões autorais","Revisão e prática"]],["58%",None])}''', first=True)

toc_page([("u","UNIDADE 1 · CONCEITOS FUNDAMENTAIS","U1"),("","1. O que é trânsito (art. 1º)","A01"),("","2. Glossário visual do CTB","A02"),("","3. Classificação das vias e velocidades","A03"),
 ("u","UNIDADE 2 · SISTEMA NACIONAL DE TRÂNSITO","U2"),("","4. Composição do SNT","A04"),("","5. Órgãos e competências","A05"),
 ("u","UNIDADE 3 · CIRCULAÇÃO E DEVERES DOS CONDUTORES","U3"),("","6. Deveres gerais dos condutores","A06"),("","7. Regras de circulação e preferência","A07"),("","8. Ultrapassagem, emergência e luzes","A08"),
 ("u","UNIDADE 4 · PEDESTRES E CICLISTAS","U4"),("","9. Pedestres","A09"),("","10. Ciclistas","A10"),
 ("u","UNIDADE 5 · SINALIZAÇÃO","U5"),("","11. Tipos de sinais e prevalência","A11"),("","12. Placas (sinalização vertical)","A12"),("","13. Marcas viárias, semáforo e gestos","A13"),
 ("u","UNIDADE 6 · SEGURANÇA VIÁRIA, HABILITAÇÃO E INFRAÇÕES","U6"),("","14. Noções de habilitação","A14"),("","15. Infrações, multas e pontos","A15"),("","16. Regras frequentemente cobradas","A16"),
 ("u","REVISÃO E PRÁTICA","RV"),("","Mapa conceitual · Erros mais comuns","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),("","Gabarito, respostas dos treinos e referências","R4")])

# ================================================================ UNIDADE 1
opener("01","UNIDADE 1","Conceitos fundamentais",["O que é trânsito","Glossário visual","Classificação das vias e velocidades"],"U1")

add(H(1,'O que é <span class="hl">trânsito</span>','Art. 1º do CTB.', "A01") +
 lei(ctb("Art. 1º, caput"),'<p>Art. 1º O trânsito de qualquer natureza nas vias terrestres do território nacional, abertas à circulação, rege-se por este Código.</p>') +
 table(["Parágrafo","Regra (em síntese)"],[
  ["§ 1º · Conceito de trânsito","Utilização das vias por <b>pessoas, veículos e animais</b>, isolados ou em grupos, conduzidos ou não, para fins de <b>circulação, parada, estacionamento e operação de carga ou descarga</b>"],
  ["§ 2º · Direito de todos","O trânsito em condições seguras é <b>direito de todos</b> e dever dos órgãos e entidades do Sistema Nacional de Trânsito"],
  ["§ 3º · Responsabilidade","Os órgãos do SNT respondem <b>objetivamente</b> por danos causados aos cidadãos em virtude de ação, omissão ou erro na execução e manutenção de programas, projetos e serviços que garantam o trânsito seguro"]],["26%",None]) +
 traduz(p('“Trânsito” não é só carro andando: inclui o <strong>pedestre</strong> na calçada, o <strong>ciclista</strong>, o <strong>cavaleiro</strong>, o carro <strong>parado</strong> ou <strong>estacionado</strong> e o caminhão <strong>descarregando</strong>. E trânsito seguro é um <strong>direito</strong>: se um buraco não sinalizado causa um acidente, o órgão responsável pode responder pelo dano, sem que a vítima precise provar culpa.')) +
 memo('Trânsito = <strong>pessoas, veículos e animais</strong> · <strong>circulação, parada, estacionamento e carga/descarga</strong>. Trânsito seguro = <strong>direito de todos</strong>. Órgãos respondem de forma <strong>objetiva</strong>.'))

add(H(1,'Glossário <span class="hl">visual</span> do CTB','Conceitos do Anexo I.', "A02") +
 glossario())

add(H(1,'Classificação das vias e <span class="hl">velocidades</span>','Art. 61: quando não há placa.', "A03") +
 lei(ctb("Art. 61, caput"),'<p>Art. 61. A velocidade máxima permitida para a via será indicada por meio de sinalização, obedecidas suas características técnicas e as condições de trânsito.</p>') +
 table(["Tipo de via (sem sinalização)","Velocidade máxima (art. 61, § 1º)"],[
  ["<b>Urbana</b> · via de trânsito rápido","80 km/h"],["<b>Urbana</b> · via arterial","60 km/h"],["<b>Urbana</b> · via coletora","40 km/h"],["<b>Urbana</b> · via local","30 km/h"],
  ["<b>Rural</b> · rodovia de pista dupla","110 km/h para automóveis, camionetas, caminhonetes e motocicletas; 90 km/h para os demais veículos"],
  ["<b>Rural</b> · rodovia de pista simples","100 km/h para automóveis, camionetas, caminhonetes e motocicletas; 90 km/h para os demais veículos"],
  ["<b>Rural</b> · estrada (não pavimentada)","60 km/h"]],["44%",None]) +
 memo('Urbanas: <strong>80 · 60 · 40 · 30</strong> (trânsito rápido, arterial, coletora, local). Rurais: <strong>110</strong> (pista dupla), <strong>100</strong> (pista simples) para autos e motos; <strong>60</strong> em estradas. A placa sempre <strong>prevalece</strong> sobre esses limites.'))

add(H(1,'Os quatro tipos de <span class="hl">via urbana</span>','Classificação do Anexo I.') + vias_box() + pega('<ul><li>Esses limites valem <b>só quando não houver sinalização</b>; havendo placa, vale a placa.</li><li>Rodovia é via rural <b>pavimentada</b>; estrada é via rural <b>não pavimentada</b>.</li><li>Os valores de 110 e 100 km/h foram fixados pela Lei nº 14.440/2022.</li></ul>'))

treino(1, [
 ("Para o CTB, o trânsito inclui a utilização das vias por pessoas, veículos e animais para circulação, parada, estacionamento e operação de carga ou descarga.","C","Art. 1º, § 1º."),
 ("O trânsito em condições seguras é direito de todos e dever dos órgãos do Sistema Nacional de Trânsito.","C","Art. 1º, § 2º."),
 ("Os órgãos do SNT só respondem por danos se ficar provada a culpa do servidor.","E","A responsabilidade é objetiva (art. 1º, § 3º)."),
 ("Em via urbana local sem sinalização, a velocidade máxima é de 30 km/h.","C","Art. 61, § 1º."),
 ("Em rodovia de pista dupla sem sinalização, a velocidade máxima para automóveis é de 100 km/h.","E","É de 110 km/h; 100 km/h é na pista simples."),
 ("Em estradas (vias rurais não pavimentadas) sem sinalização, a velocidade máxima é de 60 km/h.","C","Art. 61, § 1º.")])

# ================================================================ UNIDADE 2
opener("02","UNIDADE 2","Sistema Nacional de Trânsito",["Composição do SNT","Órgãos e competências"],"U2")

def snt():
    N,B,O,R,G=C['navy'],C['blue'],C['golddeep'],C['red'],C['green']
    s = f'<figure><svg viewBox="0 0 640 270" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    s += f'<rect x="200" y="6" width="240" height="44" rx="12" fill="{N}"/><text x="320" y="26" text-anchor="middle" font-size="13" font-weight="900" fill="#fff">SISTEMA NACIONAL DE TRÂNSITO</text><text x="320" y="42" text-anchor="middle" font-size="10" fill="#cfd6df">CTB, art. 7º</text>'
    s += '<g stroke="#9aa3ad" stroke-width="2.4" fill="none"><path d="M320 50 V64 M80 64 H560 M80 64 V78 M240 64 V78 M400 64 V78 M560 64 V78 M160 150 V164 M60 164 H260 M60 164 V176 M160 164 V176 M260 164 V176"/></g>'
    for x,t,a,b,fg,bg in [(80,"I · CONTRAN","normativo e","coordenador",N,NV),(240,"II · CETRAN","e CONTRANDIFE","(Estados e DF)",B,C['sky']),(400,"III · EXECUTIVOS","de trânsito: União,","Estados, DF, Municípios",O,C['goldsoft']),(560,"IV · RODOVIÁRIOS","órgãos executivos","rodoviários",G,C['greensoft'])]:
        s += f'<rect x="{x-74}" y="78" width="148" height="72" rx="12" fill="{bg}" stroke="{fg}" stroke-width="2.3"/><text x="{x}" y="102" text-anchor="middle" font-size="11" font-weight="900" fill="{fg}">{t}</text><text x="{x}" y="120" text-anchor="middle" font-size="9.6" fill="{C["ink"]}">{a}</text><text x="{x}" y="135" text-anchor="middle" font-size="9.6" fill="{C["ink"]}">{b}</text>'
    for x,t,a in [(60,"V · PRF","rodovias federais"),(160,"VI · POLÍCIAS","MILITARES"),(260,"VII · JARI","julgam recursos")]:
        s += f'<rect x="{x-48}" y="176" width="96" height="58" rx="10" fill="#fff" stroke="{R}" stroke-width="2"/><text x="{x}" y="200" text-anchor="middle" font-size="9.8" font-weight="900" fill="{C["ink"]}">{t}</text><text x="{x}" y="218" text-anchor="middle" font-size="9" fill="{C["muted"]}">{a}</text>'
    s += f'<rect x="330" y="176" width="300" height="58" rx="10" fill="{C["redsoft"]}" stroke="{R}" stroke-width="2"/><text x="480" y="198" text-anchor="middle" font-size="10.5" font-weight="900" fill="{R}">GUARDAS MUNICIPAIS NÃO ESTÃO NA LISTA</text><text x="480" y="216" text-anchor="middle" font-size="9.4" fill="{C["ink"]}">mas podem exercer o poder de polícia de trânsito,</text><text x="480" y="228" text-anchor="middle" font-size="9.4" fill="{C["ink"]}">quando a lei municipal atribui (STF, Tema 472)</text>'
    s += f'<text x="320" y="258" text-anchor="middle" font-size="10" fill="{C["muted"]}">JARI = Juntas Administrativas de Recursos de Infrações; CETRAN = Conselho Estadual; CONTRANDIFE = Conselho de Trânsito do DF.</text>'
    return s + '</svg><figcaption>Composição do Sistema Nacional de Trânsito (art. 7º).</figcaption></figure>'

add(H(2,'Composição do <span class="hl">SNT</span>','Quem integra o Sistema Nacional de Trânsito.', "A04") +
 snt() +
 traduz(p('O SNT é o conjunto de órgãos da União, dos Estados, do DF e dos Municípios que cuidam do trânsito: planejam, regulamentam, registram e licenciam veículos, formam e habilitam condutores, fiscalizam, julgam infrações e recursos e aplicam penalidades (art. 5º). O <strong>CONTRAN</strong> é o órgão máximo <strong>normativo e coordenador</strong>; os <strong>Detrans</strong> são os executivos estaduais; os <strong>Municípios</strong> integram o sistema por meio de órgão executivo de trânsito ou diretamente pela prefeitura (art. 24, § 2º).'),"profa") +
 memo('SNT (art. 7º): <strong>CONTRAN · CETRAN/CONTRANDIFE · executivos de trânsito · executivos rodoviários · PRF · PMs · JARI</strong>.'))

add(H(2,'Órgãos e <span class="hl">competências</span>','Quem faz o quê.', "A05") +
 table(["Órgão","Principais competências (em síntese)"],[
  ["CONTRAN (art. 12)","Estabelecer as normas regulamentares do Código e as diretrizes da Política Nacional de Trânsito; coordenar os órgãos do SNT; zelar pela uniformidade e cumprimento das normas"],
  ["PRF (art. 20)","Nas rodovias e estradas federais: cumprir e fazer cumprir a legislação, patrulhar, fiscalizar, autuar e aplicar penalidades"],
  ["Órgãos rodoviários (art. 21)","Planejar, projetar, regulamentar e operar o trânsito nas rodovias de sua circunscrição; sinalizar; fiscalizar, autuar e aplicar multas"],
  ["Detrans (art. 22)","Habilitação (expedir e cassar permissão, CNH e licença de aprendizagem), registro e licenciamento de veículos, fiscalização e autuação"],
  ["Polícias Militares (art. 23)","Fiscalização de trânsito quando e conforme <b>convênio</b> firmado, como agentes do órgão executivo de trânsito ou rodoviário"],
  ["Órgãos municipais (art. 24)","Fiscalizar, autuar e aplicar penalidades na sua competência; sinalizar; estacionamento rotativo pago; registro de veículos de propulsão humana e de tração animal; competência <b>exclusiva</b> sobre certas infrações, como estacionamento e parada irregulares (§ 4º, Lei nº 14.599/2023)"]],["24%",None]) +
 lembre(p('Pode lavrar o auto de infração o <strong>agente da autoridade de trânsito</strong>: servidor civil, estatutário ou celetista, ou policial militar designado pela autoridade de trânsito (art. 280, § 4º). O STF considerou constitucional atribuir às <strong>guardas municipais</strong> o poder de polícia de trânsito, inclusive para aplicar sanções previstas em lei (RE 658.570, Tema 472).'), "Agente da autoridade de trânsito"))

treino(2, [
 ("O CONTRAN é o órgão máximo normativo e coordenador do Sistema Nacional de Trânsito.","C","Art. 12 e art. 7º, I."),
 ("As guardas municipais estão expressamente listadas entre os integrantes do SNT no art. 7º do CTB.","E","Não estão na lista; o STF admite o exercício do poder de polícia de trânsito por elas."),
 ("A habilitação de condutores é atribuição dos órgãos executivos de trânsito dos Estados e do DF (Detrans).","C","Art. 22."),
 ("As Polícias Militares fiscalizam o trânsito quando e conforme convênio firmado.","C","Art. 23, III."),
 ("Compete à PRF fiscalizar o trânsito nas vias urbanas municipais.","E","Atua nas rodovias e estradas federais (art. 20)."),
 ("A JARI julga os recursos contra penalidades de trânsito.","C","Juntas Administrativas de Recursos de Infrações.")])

# ================================================================ UNIDADE 3
opener("03","UNIDADE 3","Circulação e deveres dos condutores",["Deveres gerais","Regras de circulação e preferência","Ultrapassagem, emergência e luzes"],"U3")

add(H(3,'Deveres gerais dos <span class="hl">condutores</span>','Arts. 26 a 28.', "A06") +
 table(["Artigo","Dever (em síntese)"],[
  ["Art. 26","Os usuários das vias devem <b>abster-se de todo ato que possa constituir perigo ou obstáculo</b> para o trânsito, ou causar danos a propriedades; e não obstruir o trânsito nem torná-lo perigoso, atirando, depositando ou abandonando objetos na via"],
  ["Art. 27","Antes de colocar o veículo em circulação, o condutor deve verificar a existência e as boas condições de funcionamento dos equipamentos de uso obrigatório e a existência de combustível suficiente"],
  ["Art. 28","O condutor deverá, a todo momento, <b>ter domínio de seu veículo</b>, dirigindo-o com atenção e cuidados indispensáveis à segurança do trânsito"]],["16%",None]) +
 flow([("car",["VERIFICA","equipamentos e","combustível (27)"]),("eye",["ATENÇÃO","e domínio do","veículo (28)"]),("shield",["NÃO CRIA","perigo nem","obstáculo (26)"])],
      "Os três deveres básicos de quem dirige.", colors=colors("b","o","g")) +
 memo('Três deveres básicos: <strong>não criar perigo</strong> (26), <strong>verificar o veículo</strong> (27) e <strong>ter domínio do veículo</strong> com atenção (28).'))

def cruzamento():
    s = f'<figure><svg viewBox="0 0 640 230" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    for k,(t,a,b) in enumerate([("1º","RODOVIA","quem já está na rodovia"),("2º","ROTATÓRIA","quem já circula nela"),("3º","DEMAIS CASOS","quem vem pela DIREITA")]):
        x=10+k*212
        s += f'<rect x="{x}" y="10" width="196" height="180" rx="16" fill="{[C["sky"],C["goldsoft"],C["greensoft"]][k]}" stroke="{[C["blue"],C["golddeep"],C["green"]][k]}" stroke-width="2.5"/>'
        s += f'<text x="{x+98}" y="44" text-anchor="middle" font-size="26" font-weight="900" fill="{[C["blue"],C["golddeep"],C["green"]][k]}">{t}</text><text x="{x+98}" y="76" text-anchor="middle" font-size="14" font-weight="900" fill="{C["ink"]}">{a}</text><text x="{x+98}" y="98" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">tem preferência</text><text x="{x+98}" y="116" text-anchor="middle" font-size="10.5" font-weight="800" fill="{C["ink"]}">{b}</text>'
    # mini cruzamento no 3º
    x0=10+2*212+98
    s += f'<rect x="{x0-48}" y="128" width="96" height="16" fill="#9aa0a6"/><rect x="{x0-8}" y="124" width="16" height="62" fill="#9aa0a6"/>'
    s += f'<rect x="{x0+16}" y="130" width="22" height="12" rx="3" fill="{C["red"]}"/><rect x="{x0-5}" y="160" width="10" height="18" rx="3" fill="{C["blue"]}"/>'
    s += f'<text x="320" y="215" text-anchor="middle" font-size="10.5" font-weight="800" fill="{C["navy"]}">Cruzamento sem sinalização (art. 29, III): rodovia → rotatória → quem vem pela direita do condutor.</text>'
    return s + '</svg><figcaption>A ordem de preferência em cruzamentos não sinalizados.</figcaption></figure>'

add(H(3,'Regras de circulação e <span class="hl">preferência</span>','Art. 29.', "A07") +
 table(["Regra","Conteúdo (art. 29, em síntese)"],[
  ["Lado de circulação (I)","A circulação far-se-á pelo <b>lado direito</b> da via, admitindo-se as exceções devidamente sinalizadas"],
  ["Distância de segurança (II)","O condutor deve guardar distância de segurança lateral e frontal entre o seu e os demais veículos, e em relação ao bordo da pista"],
  ["Preferência sem sinalização (III)","a) veículo que transita por rodovia; b) veículo que circula em rotatória; c) nos demais casos, o que vier pela <b>direita</b> do condutor"],
  ["Responsabilidade (§ 2º)","Os veículos de <b>maior porte</b> são sempre responsáveis pela segurança dos <b>menores</b>, os motorizados pelos não motorizados e, juntos, pela incolumidade dos <b>pedestres</b>"]],["26%",None]) +
 cruzamento())

add(H(3,'Ultrapassagem, emergência e <span class="hl">luzes</span>','Art. 29, VII e X, e art. 40.', "A08") +
 table(["Tema","Regra (em síntese)"],[
  ["Ultrapassagem (art. 29, X e XI)","Em regra, deve ser feita <b>pela esquerda</b>, com sinal prévio, espaço suficiente e sem perigo; quem vai ser ultrapassado não deve acelerar e deve manter-se à direita"],
  ["Veículos de emergência (art. 29, VII)","Ambulâncias, bombeiros, polícia, fiscalização e operação de trânsito, com dispositivos de <b>alarme sonoro e iluminação vermelha intermitente</b> ligados, têm prioridade de trânsito e livre circulação, estacionamento e parada, quando em serviço de urgência; os demais condutores devem deixar livre a passagem"],
  ["Farol baixo (art. 40, I)","Aceso durante a <b>noite</b> e, mesmo de dia, em <b>túneis</b> e sob <b>chuva, neblina ou cerração</b>"],
  ["Rodovias de pista simples (art. 40, § 2º, Lei nº 14.071/2020)","Veículos <b>sem luz de rodagem diurna (DRL)</b> devem manter os faróis acesos, mesmo de dia, em rodovias de <b>pista simples</b> situadas <b>fora dos perímetros urbanos</b>"]],["30%",None]) +
 ex(p('Uma viatura da Guarda Municipal com sirene e luz vermelha intermitente ligadas, atendendo uma ocorrência urgente, se aproxima por trás de um carro. O motorista deve <b>deixar a passagem livre</b>, desviando para a direita quando possível. Fora de urgência (sem os dispositivos ligados), a viatura segue as regras comuns.')) +
 memo('Ultrapassar pela <strong>esquerda</strong>. Emergência: <strong>sirene + luz vermelha intermitente</strong> e <strong>urgência</strong>. Farol baixo de dia: <strong>túnel, chuva, neblina</strong> e rodovia de <strong>pista simples</strong> fora da cidade (sem DRL).'))

treino(3, [
 ("O condutor deve ter, a todo momento, domínio de seu veículo, dirigindo com atenção e cuidados indispensáveis à segurança.","C","Art. 28."),
 ("Em cruzamento não sinalizado entre duas vias urbanas comuns, tem preferência o veículo que vier pela esquerda do condutor.","E","Pela direita (art. 29, III, c)."),
 ("Em cruzamento não sinalizado, o veículo que circula em rotatória tem preferência.","C","Art. 29, III, b."),
 ("Os veículos de maior porte são responsáveis pela segurança dos menores, e todos pela incolumidade dos pedestres.","C","Art. 29, § 2º."),
 ("Veículos de emergência têm prioridade apenas se estiverem com os dispositivos de alarme sonoro e iluminação intermitente ligados, em serviço de urgência.","C","Art. 29, VII."),
 ("Pela regra atual, todo veículo deve circular com farol baixo aceso durante o dia em qualquer via urbana.","E","De dia, a regra vale para túneis, chuva/neblina e rodovias de pista simples fora do perímetro urbano (veículos sem DRL).")])

# ================================================================ UNIDADE 4
opener("04","UNIDADE 4","Pedestres e ciclistas",["Pedestres","Ciclistas"],"U4")

add(H(4,'<span class="hl">Pedestres</span>','Arts. 68 a 71.', "A09") +
 table(["Regra","Conteúdo (em síntese)"],[
  ["Onde andar (art. 68)","É assegurada ao pedestre a utilização dos <b>passeios</b> ou passagens apropriadas das vias urbanas e dos acostamentos das vias rurais"],
  ["Ciclista desmontado (art. 68, § 1º)","O ciclista desmontado empurrando a bicicleta <b>equipara-se ao pedestre</b> em direitos e deveres"],
  ["Onde atravessar (art. 69)","Na <b>faixa</b> ou passagem a ele destinada, sempre que existir numa distância de até <b>50 metros</b> dele"],
  ["Prioridade (art. 70)","Os pedestres que estiverem atravessando a via sobre as faixas delimitadas para esse fim têm <b>prioridade</b> de passagem, exceto nos locais com sinalização semafórica, onde devem ser respeitadas as indicações do semáforo"],
  ["Manutenção (art. 71)","O órgão ou entidade com circunscrição sobre a via manterá, obrigatoriamente, as faixas e passagens de pedestres em boas condições de visibilidade, higiene, segurança e sinalização"]],["26%",None]) +
 scene3([("NA FAIXA",C['green'],C['greensoft'],"prof",["Pedestre na faixa","sem semáforo:","prioridade dele."],"o carro para"),
  ("COM SEMÁFORO",C['golddeep'],C['goldsoft'],"profa",["Vale a luz","do semáforo","de pedestres."],"respeita o sinal"),
  ("FAIXA A 40 m",C['red'],C['redsoft'],"prof",["Faixa a menos de","50 m: deve usá-la","para atravessar."],"art. 69")], "Situação ilustrada: o pedestre e a faixa."))

add(H(4,'<span class="hl">Ciclistas</span>','Arts. 58, 59 e 68, § 1º.', "A10") +
 table(["Regra","Conteúdo (em síntese)"],[
  ["Onde circular (art. 58)","Nas vias urbanas e rurais de pista dupla, a bicicleta circula, quando não houver ciclovia, ciclofaixa ou acostamento (ou quando não for possível usá-los), pelos <b>bordos da pista</b>, no <b>mesmo sentido</b> de circulação regulamentado para a via, com <b>preferência sobre os veículos automotores</b>"],
  ["Calçadas (art. 59)","A circulação de bicicletas nos passeios só é permitida quando <b>autorizada e devidamente sinalizada</b> pelo órgão com circunscrição sobre a via"],
  ["Desmontado (art. 68, § 1º)","Empurrando a bicicleta, o ciclista é equiparado ao pedestre"],
  ["Proteção (art. 29, § 2º)","Os veículos motorizados são responsáveis pela segurança dos não motorizados"]],["26%",None]) +
 ex(p('Uma ciclista pedala no bordo direito de uma avenida sem ciclofaixa, no mesmo sentido dos carros: conduta correta, e ela tem <b>preferência</b> sobre os automotores. Se ela subir na calçada pedalando, sem autorização e sinalização, comete irregularidade; se descer e empurrar a bicicleta, passa a ser tratada como <b>pedestre</b>.')) +
 memo('Bicicleta: <strong>bordo da pista</strong>, <strong>mesmo sentido</strong>, <strong>preferência</strong> sobre automotores. Calçada: só se <strong>autorizado e sinalizado</strong>. Empurrando: <strong>pedestre</strong>.'))

treino(4, [
 ("O pedestre deve atravessar na faixa sempre que ela existir a até 50 metros dele.","C","Art. 69."),
 ("Os pedestres na faixa têm prioridade de passagem, inclusive nos locais com semáforo, independentemente da cor do sinal.","E","Nos locais com semáforo, prevalecem as indicações dele (art. 70)."),
 ("O ciclista desmontado empurrando a bicicleta equipara-se ao pedestre em direitos e deveres.","C","Art. 68, § 1º."),
 ("Sem ciclovia ou ciclofaixa, a bicicleta circula pelos bordos da pista, no sentido contrário ao dos veículos.","E","No mesmo sentido (art. 58)."),
 ("A circulação de bicicletas nas calçadas é sempre permitida.","E","Só quando autorizada e sinalizada (art. 59)."),
 ("A bicicleta tem preferência sobre os veículos automotores, nas condições do art. 58.","C","Art. 58.")])

# ================================================================ UNIDADE 5
opener("05","UNIDADE 5","Sinalização",["Tipos de sinais e prevalência","Placas","Marcas viárias, semáforo e gestos"],"U5")

def piramide():
    s = f'<figure><svg viewBox="0 0 640 240" width="560" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    niveis=[("1º · ORDENS DO AGENTE DE TRÂNSITO",C['red'],"#fff"),("2º · SEMÁFORO",C['golddeep'],"#fff"),("3º · DEMAIS SINAIS (placas, marcas)",C['blue'],"#fff"),("4º · NORMAS GERAIS DE CIRCULAÇÃO",C['navy'],"#fff")]
    for k,(t,c,tc) in enumerate(niveis):
        w=300+k*100; x=320-w/2; y=10+k*54
        s += f'<rect x="{x}" y="{y}" width="{w}" height="46" rx="8" fill="{c}"/><text x="320" y="{y+29}" text-anchor="middle" font-size="12.5" font-weight="900" fill="{tc}">{t}</text>'
    return s + '</svg><figcaption>Prevalência (art. 89): o agente prevalece sobre o semáforo, que prevalece sobre os demais sinais, que prevalecem sobre as normas gerais.</figcaption></figure>'

add(H(5,'Tipos de sinais e <span class="hl">prevalência</span>','Arts. 87 e 89.', "A11") +
 table(["Classificação dos sinais de trânsito (art. 87)",""],[
  ["I - verticais (placas)","II - horizontais (marcas no pavimento)"],
  ["III - dispositivos de sinalização auxiliar (cones, tachas, defensas)","IV - luminosos (semáforos)"],
  ["V - sonoros (apito do agente)","VI - gestos do agente de trânsito e do condutor"]],["50%",None]) +
 lei(ctb("Art. 89"),'<p>Art. 89. A sinalização terá a seguinte ordem de prevalência: I - as ordens do agente de trânsito sobre as normas de circulação e outros sinais; II - as indicações do semáforo sobre os demais sinais; III - as indicações dos sinais sobre as demais normas de trânsito.</p>') +
 piramide() +
 memo('Prevalência: <strong>AGENTE &gt; SEMÁFORO &gt; PLACAS e MARCAS &gt; NORMAS GERAIS</strong>. Se o agente manda seguir com o semáforo vermelho, obedece-se ao agente.'))

def placas():
    s = f'<figure><svg viewBox="0 0 640 210" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    s += pare(60, 70) + preferencia(160, 66) + regulamentacao(260, 70, "60") + regulamentacao(350, 70, "E", risco=True)
    s += advertencia(460, 70, "!") + indicacao(570, 50, "CENTRO →", GRN) + indicacao(570, 104, "HOSPITAL", BLU)
    for x,t in [(60,"R-1 · Parada"),(160,"R-2 · Dê a"),(260,"Velocidade"),(350,"Proibido"),(460,"Advertência"),(570,"Indicação")]:
        s += f'<text x="{x}" y="150" text-anchor="middle" font-size="10" font-weight="900" fill="{C["ink"]}">{t}</text>'
    for x,t in [(60,"obrigatória"),(160,"preferência"),(260,"máxima"),(350,"estacionar"),(460,"(perigo)"),(570,"(destino/serviço)")]:
        s += f'<text x="{x}" y="164" text-anchor="middle" font-size="9.5" fill="{C["muted"]}">{t}</text>'
    s += f'<rect x="10" y="178" width="400" height="24" rx="6" fill="{C["redsoft"]}"/><text x="210" y="194" text-anchor="middle" font-size="10" font-weight="900" fill="{C["red"]}">REGULAMENTAÇÃO: obrigações, proibições e limites</text>'
    s += f'<rect x="420" y="178" width="80" height="24" rx="6" fill="#fff6cc"/><text x="460" y="194" text-anchor="middle" font-size="9" font-weight="900" fill="#8a6200">ALERTA</text>'
    s += f'<rect x="510" y="178" width="120" height="24" rx="6" fill="{C["greensoft"]}"/><text x="570" y="194" text-anchor="middle" font-size="9" font-weight="900" fill="{C["green"]}">ORIENTA</text>'
    return s + '</svg><figcaption>As três famílias de placas (desenhos didáticos, fora de escala).</figcaption></figure>'

add(H(5,'<span class="hl">Placas</span> (sinalização vertical)','Regulamentação, advertência e indicação.', "A12") +
 placas() +
 placas_txt())

add(H(5,'Marcas viárias, semáforo e <span class="hl">gestos</span>','Sinalização horizontal, luminosa e gestual.', "A13") +
 horizontal_txt())

add(H(5,'Gestos e apitos do <span class="hl">agente</span>','O agente prevalece sobre todos os sinais.') + gestos_txt() +
 ex(p('Num cruzamento com semáforo verde para você, o agente de trânsito levanta o braço verticalmente. Você deve <b>parar</b>: a ordem do agente prevalece sobre o semáforo (art. 89, I). Se você já estava dentro do cruzamento, não é obrigado a parar.')) +
 memo('Braço <strong>para cima</strong>: todos param. Braço <strong>na horizontal</strong>: param os que vêm de direções que cortam a direção do braço. Dois silvos breves: <strong>pare</strong>.'))

treino(5, [
 ("As ordens do agente de trânsito prevalecem sobre as indicações do semáforo.","C","Art. 89, I."),
 ("As indicações dos sinais prevalecem sobre as ordens do agente de trânsito.","E","O agente prevalece sobre todos (art. 89)."),
 ("Os gestos do agente de trânsito e do condutor são sinais de trânsito previstos no art. 87 do CTB.","C","Art. 87, VI."),
 ("A placa de parada obrigatória (R-1) tem forma octogonal, na cor vermelha.","C","Anexo II."),
 ("As placas de advertência têm, em regra, forma circular com orla vermelha.","E","São amarelas, em forma de quadrado com diagonal vertical (losango); a circular com orla vermelha é de regulamentação."),
 ("As marcas viárias amarelas separam movimentos veiculares de fluxos opostos.","C","Anexo II.")])

# ================================================================ UNIDADE 6
opener("06","UNIDADE 6","Segurança viária, habilitação e infrações",["Noções de habilitação","Infrações, multas e pontos","Regras frequentemente cobradas"],"U6")

add(H(6,'Noções de <span class="hl">habilitação</span>','Arts. 140 a 159.', "A14") +
 table(["Tema","Regra (em síntese)"],[
  ["Requisitos (art. 140)","Ser penalmente imputável, saber ler e escrever e possuir documento de identidade (ou equivalente)"],
  ["Permissão para Dirigir (art. 148, §§ 2º e 3º)","Validade de <b>um ano</b>; ao fim, o condutor recebe a CNH se não tiver cometido infração de natureza <b>grave ou gravíssima</b> nem for reincidente em infração <b>média</b>"],
  ["Exames de aptidão física e mental (art. 147, § 2º)","Renovação a cada <b>10 anos</b> para menores de 50 anos; a cada <b>5 anos</b> dos 50 aos 70; a cada <b>3 anos</b> a partir dos 70"],
  ["Toxicológico (art. 148-A)","Exigido nas categorias C, D e E para obter e renovar a habilitação; a Lei nº 15.153/2025 estendeu a exigência às categorias A e B na primeira habilitação, na forma e vigência que estabelece"],
  ["CNH (art. 159, Lei nº 15.428/2026)","Pode ser física ou digital e vale como documento de identidade; sua validade acompanha a do exame de aptidão física e mental"]],["30%",None]) +
 table(["Categoria (art. 143)","Pode conduzir (em síntese)"],[
  ["A","Veículo motorizado de duas ou três rodas (moto, motoneta, triciclo)"],
  ["B","Veículo não abrangido pela A, com peso bruto total até 3.500 kg e lotação até 8 lugares, excluído o motorista; pela Lei nº 15.503/2026, também veículos elétricos ou híbridos até 4.250 kg, conforme critérios do Contran"],
  ["C","Veículo de carga com peso bruto total acima de 3.500 kg"],
  ["D","Veículo de passageiros com lotação acima de 8 lugares, excluído o motorista"],
  ["E","Combinação de veículos em que a unidade acoplada tenha 6.000 kg ou mais, ou lotação acima de 8 lugares"]],["20%",None]))

add(H(6,'Infrações, multas e <span class="hl">pontos</span>','Arts. 258, 259 e 261.', "A15") +
 table(["Natureza da infração","Multa (art. 258)","Pontos (art. 259)"],[
  ["<b>Gravíssima</b>","R$ 293,47","7"],["<b>Grave</b>","R$ 195,23","5"],["<b>Média</b>","R$ 130,16","4"],["<b>Leve</b>","R$ 88,38","3"]],["40%","30%",None]) +
 table(["Suspensão do direito de dirigir por pontos (art. 261, I, Lei nº 14.071/2020)","Limite em 12 meses"],[
  ["Se houver <b>duas ou mais</b> infrações gravíssimas na pontuação","<b>20 pontos</b>"],
  ["Se houver <b>uma</b> infração gravíssima","<b>30 pontos</b>"],
  ["Se <b>não houver</b> infração gravíssima","<b>40 pontos</b>"]],["66%",None]) +
 lembre(p('Os valores das multas são os do art. 258 do CTB, com a redação da Lei nº 13.281/2016. O art. 319-A permite ao Contran atualizá-los pelo IPCA; confira se houve atualização posterior por resolução. Algumas infrações têm a multa <strong>multiplicada</strong> (por exemplo, por três ou por dez), como as de dirigir sem habilitação e sob efeito de álcool.'), "Atenção aos valores") +
 memo('Pontos: <strong>7 · 5 · 4 · 3</strong> (gravíssima, grave, média, leve). Suspensão: <strong>20 · 30 · 40</strong> pontos, conforme o número de gravíssimas.'))

add(H(6,'Regras <span class="hl">frequentemente cobradas</span>','Infrações e crimes que mais aparecem.', "A16") +
 table(["Conduta","Consequência (em síntese)"],[
  ["Dirigir sem possuir CNH ou Permissão (art. 162, I)","Gravíssima; multa multiplicada por <b>três</b>; retenção do veículo até a apresentação de condutor habilitado"],
  ["Dirigir sob influência de álcool ou de substância psicoativa (art. 165)","Gravíssima; multa multiplicada por <b>dez</b>; suspensão do direito de dirigir por <b>12 meses</b>"],
  ["Recusar-se ao teste do bafômetro ou exame (art. 165-A)","As <b>mesmas</b> penalidades do art. 165"],
  ["Dirigir segurando ou manuseando celular (art. 252, parágrafo único)","Infração <b>gravíssima</b> (usar fones ou telefone celular, sem segurar ou manusear, é média, art. 252, VI)"],
  ["Homicídio culposo na direção (art. 302)","Detenção de 2 a 4 anos, e suspensão ou proibição de dirigir; sob influência de álcool: reclusão de 5 a 8 anos (§ 3º)"],
  ["Lesão corporal culposa na direção (art. 303)","Detenção de 6 meses a 2 anos, e suspensão ou proibição de dirigir"],
  ["Embriaguez ao volante (art. 306)","Detenção de 6 meses a 3 anos, multa e suspensão ou proibição; configura-se, entre outros meios, com 6 decigramas de álcool por litro de sangue ou 0,3 miligrama por litro de ar alveolar"]],["32%",None]) +
 memo('Álcool: infração <strong>gravíssima x10</strong> + <strong>12 meses</strong> de suspensão; recusa = <strong>mesma</strong> pena. Crime de embriaguez: <strong>0,3 mg/L</strong> de ar ou <strong>6 dg/L</strong> de sangue. Celular <strong>na mão</strong>: gravíssima.'))

treino(6, [
 ("A Permissão para Dirigir tem validade de um ano.","C","Art. 148, § 2º."),
 ("O condutor com menos de 50 anos renova os exames de aptidão física e mental a cada 5 anos.","E","A cada 10 anos (art. 147, § 2º)."),
 ("A infração gravíssima corresponde a 7 pontos.","C","Art. 259."),
 ("Se não houver infração gravíssima na pontuação, a suspensão ocorre ao atingir 40 pontos em 12 meses.","C","Art. 261, I."),
 ("A recusa ao teste do bafômetro não gera penalidade, por proteção contra a autoincriminação.","E","Gera as mesmas penalidades do art. 165 (art. 165-A)."),
 ("Dirigir segurando ou manuseando telefone celular é infração gravíssima.","C","Art. 252, parágrafo único.")])

# ================================================================ REVISÃO
mapa(("CTB","ESQUEMA-","TIZADO"), [
  ("CONCEITOS",["pessoas, veículos e animais","trânsito seguro: direito","urbanas: 80·60·40·30"],C['navy'],NV),
  ("SNT",["CONTRAN normatiza","Detran habilita","municípios fiscalizam"],C['blue'],C['sky']),
  ("CIRCULAÇÃO",["lado direito","rodovia, rotatória, direita","maior protege o menor"],C['green'],C['greensoft']),
  ("PEDESTRES E BICICLETAS",["faixa a até 50 m","bordo, mesmo sentido","desmontado = pedestre"],C['golddeep'],C['goldsoft']),
  ("SINALIZAÇÃO",["agente > semáforo","> sinais > normas","amarelo: fluxos opostos"],C['red'],C['redsoft']),
  ("HABILITAÇÃO E PONTOS",["permissão: 1 ano","7·5·4·3 pontos","suspensão: 20·30·40"],C['navy'],NV)], "Mapa conceitual do Caderno 15.", "O CTB em seis blocos. Explique cada caixa em voz alta.", center_color=C['gold'])

erros([
  ["“Trânsito é só a circulação de veículos.”","Inclui pessoas e animais, e também parada, estacionamento e carga/descarga."],
  ["“Em rodovia de pista dupla, o limite é 100 km/h.”","110 km/h para autos, camionetas, caminhonetes e motos; 100 é na pista simples."],
  ["“Guarda municipal integra o SNT pelo art. 7º.”","Não está na lista, mas pode exercer poder de polícia de trânsito (STF)."],
  ["“No cruzamento sem sinal, passa quem vem pela esquerda.”","Pela direita (depois de rodovia e rotatória)."],
  ["“Ultrapassagem pode ser pela direita.”","Em regra, pela esquerda."],
  ["“Viatura tem preferência sempre.”","Só em serviço de urgência, com sirene e luz vermelha intermitente."],
  ["“Pedestre na faixa sempre tem prioridade, mesmo com semáforo fechado para ele.”","Onde há semáforo, valem as indicações dele."]],
 [["“O semáforo prevalece sobre o agente.”","O agente prevalece sobre o semáforo (art. 89)."],
  ["“Placa de advertência é redonda com borda vermelha.”","É amarela em losango; redonda com orla vermelha é de regulamentação."],
  ["“Faixa amarela separa fluxos de mesmo sentido.”","Amarela separa sentidos opostos; branca, o mesmo sentido."],
  ["“Exame médico a cada 5 anos para todos.”","10 anos (menos de 50), 5 anos (50 a 70), 3 anos (70 ou mais)."],
  ["“Suspensão sempre com 20 pontos.”","20, 30 ou 40 pontos, conforme o número de gravíssimas."],
  ["“Recusar o bafômetro não tem consequência.”","Mesmas penalidades do art. 165 (art. 165-A)."],
  ["“Usar fone de ouvido é gravíssima.”","Segurar ou manusear o celular é gravíssima; fones/celular sem manusear é média."]])

flashcards([("CONCEITOS","Conceito de trânsito (art. 1º, § 1º)?","Uso das vias por pessoas, veículos e animais para circulação, parada, estacionamento e carga/descarga."),
 ("CONCEITOS","Responsabilidade dos órgãos do SNT?","Objetiva (art. 1º, § 3º)."),
 ("VIAS","Limites urbanos sem placa?","80 (trânsito rápido), 60 (arterial), 40 (coletora), 30 (local)."),
 ("VIAS","Limites rurais sem placa (autos e motos)?","110 (pista dupla), 100 (pista simples), 60 (estrada)."),
 ("SNT","Órgão máximo normativo do SNT?","CONTRAN."),
 ("SNT","Quem habilita condutores?","Os Detrans (órgãos executivos estaduais e do DF)."),
 ("SNT","Quem pode lavrar auto de infração (art. 280, § 4º)?","Servidor civil (estatutário ou celetista) ou policial militar designado."),
 ("CIRCULAÇÃO","Lado de circulação?","Direito, salvo exceções sinalizadas."),
 ("CIRCULAÇÃO","Preferência sem sinalização?","Rodovia; rotatória; nos demais casos, quem vem pela direita."),
 ("CIRCULAÇÃO","Responsabilidade do art. 29, § 2º?","Maior pelo menor; motorizado pelo não motorizado; todos pelos pedestres."),
 ("CIRCULAÇÃO","Quando veículo de emergência tem prioridade?","Em urgência, com alarme sonoro e luz vermelha intermitente ligados."),
 ("LUZES","Farol aceso de dia em rodovia?","Pista simples fora do perímetro urbano, para veículos sem DRL."),
 ("PEDESTRES","Distância para usar a faixa?","Até 50 metros (art. 69)."),
 ("PEDESTRES","Ciclista desmontado?","Equipara-se ao pedestre (art. 68, § 1º)."),
 ("CICLISTAS","Como circula a bicicleta sem ciclovia?","Bordo da pista, mesmo sentido, com preferência sobre automotores."),
 ("SINALIZAÇÃO","Ordem de prevalência?","Agente > semáforo > sinais > normas gerais (art. 89)."),
 ("SINALIZAÇÃO","Seis tipos de sinais (art. 87)?","Verticais, horizontais, auxiliares, luminosos, sonoros e gestos."),
 ("SINALIZAÇÃO","Cores das placas?","Regulamentação: orla vermelha. Advertência: amarela. Indicação: verde (destino) e azul (serviços)."),
 ("SINALIZAÇÃO","Marca amarela x branca?","Amarela: fluxos opostos. Branca: mesmo sentido e áreas de circulação."),
 ("HABILITAÇÃO","Validade da Permissão para Dirigir?","1 ano."),
 ("HABILITAÇÃO","Renovação do exame médico?","10 anos (&lt;50), 5 anos (50 a 70), 3 anos (≥70)."),
 ("INFRAÇÕES","Pontos por natureza?","7, 5, 4 e 3 (gravíssima, grave, média, leve)."),
 ("INFRAÇÕES","Limites de suspensão por pontos?","20 (2+ gravíssimas), 30 (1), 40 (nenhuma)."),
 ("INFRAÇÕES","Álcool ao volante (infração)?","Gravíssima, multa x10, suspensão de 12 meses; recusa: mesma penalidade.")])

Q = [
 ("Conceitos","De acordo com o CTB, considera-se trânsito:",
  ["apenas a circulação de veículos automotores.","a utilização das vias por pessoas, veículos e animais, isolados ou em grupos, conduzidos ou não, para circulação, parada, estacionamento e operação de carga ou descarga.","somente o deslocamento em rodovias.","a circulação de pedestres nas calçadas, apenas.","o conjunto de placas e semáforos."],"B",
  "Art. 1º, § 1º.","Pessoas, veículos e animais."),
 ("Conceitos","Segundo o art. 1º, § 3º, do CTB, os órgãos do SNT respondem pelos danos causados aos cidadãos em virtude de falhas nos serviços de trânsito de forma:",
  ["subjetiva, dependendo de prova de culpa.","objetiva.","solidária com o motorista, sempre.","nenhuma, por se tratar de serviço gratuito.","subsidiária ao seguro obrigatório."],"B",
  "Responsabilidade objetiva por ação, omissão ou erro.","Órgão do SNT: responsabilidade objetiva."),
 ("Velocidade","Em via urbana arterial sem sinalização, a velocidade máxima permitida é de:",
  ["30 km/h.","40 km/h.","60 km/h.","80 km/h.","100 km/h."],"C",
  "Art. 61, § 1º: 80 (trânsito rápido), 60 (arterial), 40 (coletora), 30 (local).","Arterial = 60."),
 ("Velocidade","Em rodovia de pista simples, sem sinalização, a velocidade máxima para automóveis é de:",
  ["80 km/h.","90 km/h.","100 km/h.","110 km/h.","120 km/h."],"C",
  "Art. 61, § 1º (redação da Lei nº 14.440/2022): 110 km/h na pista dupla e 100 km/h na pista simples.","Pista simples = 100."),
 ("SNT","O órgão máximo normativo e coordenador do Sistema Nacional de Trânsito é o:",
  ["DENATRAN.","CONTRAN.","CETRAN.","Detran.","JARI."],"B",
  "Art. 7º, I, e art. 12.","CONTRAN normatiza."),
 ("SNT","Compete aos órgãos executivos de trânsito dos Estados e do DF (Detrans), entre outras atribuições:",
  ["julgar recursos contra multas, em última instância.","expedir a Permissão para Dirigir, a CNH e realizar o registro e licenciamento de veículos.","patrulhar rodovias federais.","editar as normas regulamentares do CTB.","legislar sobre trânsito."],"B",
  "Art. 22. O CONTRAN edita normas; a PRF patrulha rodovias federais; a JARI julga recursos.","Detran: habilitação e registro."),
 ("Agente","Pode ser agente da autoridade de trânsito, para lavrar autos de infração, segundo o art. 280, § 4º:",
  ["qualquer cidadão.","servidor civil, estatutário ou celetista, ou policial militar designado pela autoridade de trânsito.","somente policial federal.","apenas o prefeito.","empresa privada contratada."],"B",
  "Art. 280, § 4º. Para guardas municipais, o STF admitiu o poder de polícia de trânsito quando a lei municipal atribui (Tema 472).","Agente: servidor ou PM designado."),
 ("Preferência","Em cruzamento não sinalizado entre duas vias urbanas comuns, sem rotatória, tem preferência de passagem o veículo:",
  ["de maior porte.","que vier pela esquerda do condutor.","que vier pela direita do condutor.","que buzinar primeiro.","mais rápido."],"C",
  "Art. 29, III, c. Antes, prevalecem o veículo em rodovia (a) e o que circula em rotatória (b).","Sem sinal: direita."),
 ("Circulação","Sobre a responsabilidade prevista no art. 29, § 2º, do CTB, é correto afirmar:",
  ["os pedestres são responsáveis pela segurança dos veículos.","os veículos de maior porte são responsáveis pela segurança dos menores, os motorizados pelos não motorizados e, juntos, pela incolumidade dos pedestres.","os veículos menores respondem pelos maiores.","só os ônibus têm responsabilidade.","a regra vale apenas em rodovias."],"B",
  "Texto do art. 29, § 2º.","Maior protege o menor."),
 ("Emergência","Veículos de emergência gozam de prioridade e livre circulação quando:",
  ["estiverem identificados, mesmo sem urgência.","estiverem em serviço de urgência, com alarme sonoro e iluminação vermelha intermitente ligados.","transitarem apenas em rodovias.","tiverem autorização do Detran para cada deslocamento.","forem conduzidos por servidor público."],"B",
  "Art. 29, VII.","Urgência + sirene + luz vermelha."),
 ("Luzes","Pela regra vigente do art. 40 do CTB, veículos sem luz de rodagem diurna devem manter os faróis acesos durante o dia:",
  ["em todas as vias urbanas.","em rodovias de pista simples situadas fora dos perímetros urbanos.","somente em vias locais.","apenas em dias de sol.","em nenhuma hipótese."],"B",
  "Art. 40, § 2º (Lei nº 14.071/2020). Também de dia em túneis e sob chuva, neblina ou cerração (art. 40, I).","Pista simples fora da cidade."),
 ("Pedestres","O pedestre deve cruzar a via na faixa ou passagem a ele destinada sempre que esta existir numa distância de até:",
  ["10 metros.","30 metros.","50 metros.","100 metros.","200 metros."],"C",
  "Art. 69.","Faixa a até 50 m."),
 ("Pedestres","Sobre a prioridade do pedestre na faixa, é correto afirmar:",
  ["é absoluta, inclusive contra o semáforo.","os pedestres que estiverem atravessando sobre a faixa têm prioridade, exceto nos locais com semáforo, onde devem ser respeitadas as indicações dele.","só existe em vias rurais.","depende de autorização do agente.","não existe no CTB."],"B",
  "Art. 70.","Faixa: prioridade, salvo semáforo."),
 ("Ciclistas","Não havendo ciclovia, ciclofaixa ou acostamento, a bicicleta deve circular:",
  ["na calçada, sempre.","pelos bordos da pista, no mesmo sentido de circulação regulamentado para a via, com preferência sobre os veículos automotores.","no centro da pista.","no sentido contrário ao dos veículos.","apenas em vias locais."],"B",
  "Art. 58. Na calçada, só quando autorizada e sinalizada (art. 59).","Bordo, mesmo sentido, preferência."),
 ("Ciclistas","O ciclista desmontado, empurrando a bicicleta:",
  ["equipara-se a veículo automotor.","equipara-se ao pedestre em direitos e deveres.","não pode circular na calçada.","deve usar capacete obrigatoriamente.","comete infração."],"B",
  "Art. 68, § 1º.","Desmontado = pedestre."),
 ("Sinalização","Segundo o art. 89 do CTB, a ordem de prevalência da sinalização é:",
  ["semáforo, agente, placas, normas.","ordens do agente, semáforo, demais sinais, normas de circulação.","placas, semáforo, agente, normas.","normas, placas, semáforo, agente.","agente, placas, semáforo, normas."],"B",
  "Art. 89, I a III.","Agente > semáforo > sinais > normas."),
 ("Sinalização","NÃO é sinal de trânsito classificado no art. 87 do CTB:",
  ["sinal vertical.","sinal horizontal.","sinal luminoso.","gesto do agente de trânsito.","anúncio publicitário à margem da via."],"E",
  "Art. 87: verticais, horizontais, dispositivos auxiliares, luminosos, sonoros e gestos do agente e do condutor.","Propaganda não é sinal."),
 ("Placas","A placa de regulamentação, como regra, apresenta:",
  ["forma de losango e fundo amarelo.","forma circular, fundo branco e orla vermelha, com exceções como a R-1 (octogonal) e a R-2 (triangular).","forma retangular e fundo verde.","forma retangular e fundo azul.","forma triangular e fundo marrom."],"B",
  "Anexo II do CTB. Advertência: amarela; indicação: verde (destino) ou azul (serviços).","Regulamentação: círculo com orla vermelha."),
 ("Marcas","As marcas viárias na cor amarela são utilizadas para:",
  ["separar movimentos veiculares de mesmo sentido.","separar movimentos veiculares de fluxos opostos, entre outras funções.","indicar ciclovias.","indicar vagas de pessoas com deficiência.","enfeitar a via."],"B",
  "Anexo II: amarela separa fluxos opostos; branca separa fluxos de mesmo sentido.","Amarela = sentidos opostos."),
 ("Habilitação","A Permissão para Dirigir tem validade de:",
  ["6 meses.","1 ano.","2 anos.","5 anos.","10 anos."],"B",
  "Art. 148, § 2º; a CNH é concedida se não houver infração grave ou gravíssima nem reincidência em média.","Permissão: 1 ano."),
 ("Habilitação","Para condutor com idade inferior a 50 anos, os exames de aptidão física e mental são renovados a cada:",
  ["3 anos.","5 anos.","10 anos.","12 anos.","15 anos."],"C",
  "Art. 147, § 2º (Lei nº 14.071/2020): 10, 5 e 3 anos conforme a faixa etária.","Menos de 50: 10 anos."),
 ("Pontos","Pelo art. 259 do CTB, a infração grave computa:",
  ["3 pontos.","4 pontos.","5 pontos.","7 pontos.","10 pontos."],"C",
  "Gravíssima 7, grave 5, média 4, leve 3.","Grave = 5."),
 ("Suspensão","O condutor que, em 12 meses, somar pontos sem nenhuma infração gravíssima terá o direito de dirigir suspenso ao atingir:",
  ["20 pontos.","30 pontos.","40 pontos.","50 pontos.","60 pontos."],"C",
  "Art. 261, I (Lei nº 14.071/2020): 20 (duas ou mais gravíssimas), 30 (uma) e 40 (nenhuma).","Nenhuma gravíssima = 40."),
 ("Álcool","O condutor que se recusa a se submeter ao teste do etilômetro:",
  ["não sofre nenhuma penalidade.","está sujeito às mesmas penalidades e medidas do art. 165 (gravíssima, multa multiplicada por dez e suspensão por 12 meses).","comete apenas infração leve.","só pode ser punido se houver acidente.","é preso em flagrante automaticamente."],"B",
  "Art. 165-A.","Recusa = mesma pena do álcool.")]
questoes(Q, "BACDEBCAEDBCABDEBCAEDCBA")
respostas_treinos()

referencias('''<h3>Legislação consultada (portal do Planalto)</h3><ul>
<li>Código de Trânsito Brasileiro (Lei nº 9.503/1997), texto compilado: arts. 1º, 5º, 7º, 12, 20 a 24, 26 a 29, 40, 58, 59, 61, 68 a 71, 87, 89, 140, 143, 147, 148, 148-A, 159, 162, 165, 165-A, 252, 258, 259, 261, 280, 302, 303 e 306, e Anexos I e II.</li>
<li>Alterações recentes identificadas nas notas: Leis nº 13.281/2016, 14.071/2020, 14.440/2022, 14.599/2023, 15.153/2025, 15.428/2026 e 15.503/2026.</li></ul>
<h3>Jurisprudência citada</h3><ul><li>STF: RE 658.570 (Tema 472, guardas municipais e poder de polícia de trânsito, 2015).</li></ul>''',
 'O CTB foi conferido no texto compilado do portal do Planalto, que exibe a redação vigente com as notas de alteração. <strong>Limitações:</strong> o texto compilado não informa a data da última atualização e não substitui o Diário Oficial; os valores de multa são os do art. 258, que podem ser atualizados pelo Contran (art. 319-A), e as resoluções do Contran não foram consultadas; o Anexo II (sinalização) foi lido no PDF oficial disponibilizado pelo Planalto, que é uma digitalização em imagem, e as placas deste caderno são <strong>desenhos didáticos</strong>, fora de escala, e não substituem os manuais oficiais de sinalização. A vigência de algumas alterações de 2025 e 2026 depende de regras próprias de cada lei. Confira o edital do seu concurso.', DATA)
encerramento("15", "Legislação de Trânsito", 'Sugestão de continuação: <strong>Caderno 16 · Informática para Concursos</strong>.')
gravar(HERE, "Mapa da Aprovação — Caderno 15 — CTB Esquematizado", Q)
