"""Gera miolo.html do Caderno 16: Informática para Concursos. Uso: python3 gerar.py
Conteúdo introdutório e prático. Atalhos e nomes de funções seguem as versões em português do Windows, do Microsoft Word/Excel e do LibreOffice."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit
from kit import *

DATA = "26 de novembro de 2026"
kit.U = {1:("UNIDADE 1","Conceitos básicos e hardware"),2:("UNIDADE 2","Software e Windows"),3:("UNIDADE 3","Texto e planilhas"),4:("UNIDADE 4","Internet e e-mail"),5:("UNIDADE 5","Segurança da informação"),6:("UNIDADE 6","Redes")}

def kbd(*ks): return " + ".join(f'<span style="display:inline-block;border:1.5px solid {C["navy"]};border-bottom-width:3px;border-radius:4px;padding:0 5px;font-weight:800;font-size:9.5pt;background:#fff">{k}</span>' for k in ks)

# ---------------- diagramas ----------------
def computador():
    N,B=C['navy'],C['blue']
    s = f'<figure><svg viewBox="0 0 640 220" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">{arrowdefs("cp")}'
    box=[(70,"ENTRADA","teclado, mouse,","scanner, microfone",C['green'],C['greensoft']),(320,"PROCESSAMENTO","CPU: unidade de controle,","ULA e registradores",B,C['sky']),(570,"SAÍDA","monitor, impressora,","caixa de som",C['golddeep'],C['goldsoft'])]
    for x,t,a,b,fg,bg in box:
        s += f'<rect x="{x-95}" y="20" width="190" height="96" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x}" y="50" text-anchor="middle" font-size="14" font-weight="900" fill="{fg}">{t}</text><text x="{x}" y="74" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">{a}</text><text x="{x}" y="90" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">{b}</text>'
    s += f'<g stroke="{C["ink"]}" stroke-width="3" marker-end="url(#cp)"><line x1="167" y1="68" x2="220" y2="68"/><line x1="417" y1="68" x2="470" y2="68"/><line x1="300" y1="118" x2="300" y2="150"/></g><line x1="340" y1="152" x2="340" y2="120" stroke="{C["ink"]}" stroke-width="3" marker-end="url(#cp)"/>'
    s += f'<rect x="200" y="152" width="240" height="56" rx="12" fill="{NV}" stroke="{N}" stroke-width="2.5"/><text x="320" y="176" text-anchor="middle" font-size="13" font-weight="900" fill="{N}">MEMÓRIA E ARMAZENAMENTO</text><text x="320" y="194" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">RAM (trabalho) · HD/SSD (guarda)</text>'
    return s + '</svg><figcaption>O ciclo básico: entrada → processamento → saída, com apoio da memória.</figcaption></figure>'

def piramide_mem():
    s = f'<figure><svg viewBox="0 0 640 252" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    niv=[("REGISTRADORES",C['red']),("CACHE",C['golddeep']),("MEMÓRIA RAM",C['blue']),("ARMAZENAMENTO (SSD, HD)",C['navy'])]
    for k,(t,c) in enumerate(niv):
        w=160+k*100; x=260-w/2; y=12+k*56
        s += f'<rect x="{x}" y="{y}" width="{w}" height="48" rx="8" fill="{c}"/><text x="260" y="{y+30}" text-anchor="middle" font-size="12.5" font-weight="900" fill="#fff">{t}</text>'
    s += f'<g stroke="{C["ink"]}" stroke-width="2.5" fill="none"><path d="M560 230 V20"/><path d="M552 30 L560 16 L568 30"/></g>'
    s += f'<text x="580" y="40" font-size="13" font-weight="900" fill="{C["ink"]}" transform="rotate(90 585 70)">mais rápida e mais cara</text>'
    s += f'<text x="530" y="244" text-anchor="end" font-size="12.5" font-weight="800" fill="{C["muted"]}">maior capacidade e menor custo por byte ↓</text>'
    return s + '</svg><figcaption>Hierarquia de memória: quanto mais perto da CPU, mais rápida, menor e mais cara.</figcaption></figure>'

def planilha():
    N,B=C['navy'],C['blue']
    s = f'<figure><svg viewBox="0 0 640 220" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    cols=["","A","B","C"]; xs=[20,60,170,280]; ws=[40,110,110,200]
    for i,c in enumerate(cols):
        s += f'<rect x="{xs[i]}" y="20" width="{ws[i]}" height="26" fill="{NV}" stroke="#9aa6b5"/><text x="{xs[i]+ws[i]/2}" y="38" text-anchor="middle" font-size="12" font-weight="900" fill="{N}">{c}</text>'
    dados=[("1","Produto","Qtd","Total (fórmula)"),("2","Caneta","10","=B2*2"),("3","Lápis","5","=B3*2"),("4","","","=SOMA(C2:C3)")]
    for r,(n,a,b,c) in enumerate(dados):
        y=46+r*26
        for i,v in enumerate([n,a,b,c]):
            fill = NV if i==0 else ("#fff" if r>0 else C['sky'])
            s += f'<rect x="{xs[i]}" y="{y}" width="{ws[i]}" height="26" fill="{fill}" stroke="#9aa6b5"/><text x="{xs[i]+(ws[i]/2 if i==0 else 8)}" y="{y+18}" text-anchor="{"middle" if i==0 else "start"}" font-size="11.5" font-weight="{900 if (i==0 or r==0) else 600}" fill="{B if (i==3 and r>0) else C["ink"]}">{v}</text>'
    s += f'<rect x="280" y="72" width="200" height="26" fill="none" stroke="{C["red"]}" stroke-width="3"/>'
    s += f'<rect x="500" y="40" width="130" height="140" rx="12" fill="{C["goldsoft"]}" stroke="{C["golddeep"]}" stroke-width="2"/><text x="565" y="64" text-anchor="middle" font-size="11" font-weight="900" fill="{C["golddeep"]}">COPIOU C2</text><text x="565" y="80" text-anchor="middle" font-size="11" font-weight="900" fill="{C["golddeep"]}">PARA C3</text>'
    s += f'<text x="565" y="106" text-anchor="middle" font-size="11" fill="{C["ink"]}">=B2*2</text><text x="565" y="124" text-anchor="middle" font-size="14" font-weight="900" fill="{C["ink"]}">↓</text><text x="565" y="142" text-anchor="middle" font-size="11" font-weight="900" fill="{C["ink"]}">=B3*2</text><text x="565" y="166" text-anchor="middle" font-size="9.5" fill="{C["muted"]}">a linha “andou” junto</text>'
    s += f'<text x="20" y="176" font-size="10.5" fill="{C["ink"]}">Resultados: C2 = 20 · C3 = 10 · C4 = 30.</text><text x="20" y="194" font-size="10.5" fill="{C["ink"]}">A2 é o <tspan font-weight="900">endereço</tspan> da célula: coluna A, linha 2.</text>'
    return s + '</svg><figcaption>Planilha didática: fórmula, intervalo e referência relativa.</figcaption></figure>'

def url():
    s = f'<figure><svg viewBox="0 0 640 150" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    partes=[("https://",C['green'],"protocolo","(seguro: HTTPS)"),("www.exemplo.gov.br",C['blue'],"domínio","(nome do site)"),("/editais/",C['golddeep'],"caminho","(pasta no servidor)"),("aviso.pdf",C['red'],"recurso","(arquivo)")]
    x=20
    for t,c,a,b in partes:
        w=len(t)*10.2+16
        s += f'<rect x="{x}" y="20" width="{w}" height="40" rx="8" fill="{c}"/><text x="{x+w/2}" y="46" text-anchor="middle" font-size="15" font-weight="900" fill="#fff" font-family="monospace">{t}</text>'
        s += f'<text x="{x+w/2}" y="84" text-anchor="middle" font-size="12" font-weight="900" fill="{c}">{a}</text><text x="{x+w/2}" y="102" text-anchor="middle" font-size="10" fill="{C["muted"]}">{b}</text>'
        x+=w+6
    s += f'<text x="320" y="135" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">O DNS traduz o domínio no endereço IP do servidor; o navegador então pede a página pelo protocolo.</text>'
    return s + '</svg><figcaption>Anatomia de uma URL (endereço fictício).</figcaption></figure>'

def email_fluxo():
    s = f'<figure><svg viewBox="0 0 640 170" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">{arrowdefs("em")}'
    for x,t,a,fg,bg in [(80,"ANA","escreve e envia",C['green'],C['greensoft']),(320,"SERVIDORES","de e-mail",C['navy'],NV),(560,"BRUNO","lê a mensagem",C['golddeep'],C['goldsoft'])]:
        s += f'<rect x="{x-75}" y="30" width="150" height="70" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x}" y="60" text-anchor="middle" font-size="14" font-weight="900" fill="{fg}">{t}</text><text x="{x}" y="80" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">{a}</text>'
    s += f'<g stroke="{C["ink"]}" stroke-width="3" marker-end="url(#em)"><line x1="158" y1="65" x2="238" y2="65"/><line x1="398" y1="65" x2="478" y2="65"/></g>'
    s += f'<rect x="160" y="112" width="80" height="26" rx="6" fill="{C["green"]}"/><text x="200" y="130" text-anchor="middle" font-size="12" font-weight="900" fill="#fff">SMTP</text><text x="200" y="156" text-anchor="middle" font-size="10" fill="{C["muted"]}">envio</text>'
    s += f'<rect x="400" y="112" width="80" height="26" rx="6" fill="{C["blue"]}"/><text x="440" y="130" text-anchor="middle" font-size="11" font-weight="900" fill="#fff">POP3 · IMAP</text><text x="440" y="156" text-anchor="middle" font-size="10" fill="{C["muted"]}">recebimento</text>'
    return s + '</svg><figcaption>Protocolos de e-mail: SMTP envia; POP3 e IMAP recebem.</figcaption></figure>'

def backup_linha():
    s = f'<figure><svg viewBox="0 0 640 230" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    dias=["DOM","SEG","TER","QUA"]
    for i,d in enumerate(dias):
        s += f'<text x="{170+i*120}" y="22" text-anchor="middle" font-size="12" font-weight="900" fill="{C["navy"]}">{d}</text>'
    linhas=[("INCREMENTAL",["COMPLETO","muda SEG","muda TER","muda QUA"],C['blue'],C['sky']),("DIFERENCIAL",["COMPLETO","desde DOM","desde DOM","desde DOM"],C['golddeep'],C['goldsoft'])]
    for r,(t,cels,fg,bg) in enumerate(linhas):
        y=36+r*80
        s += f'<text x="14" y="{y+36}" font-size="12" font-weight="900" fill="{fg}">{t}</text>'
        for i,c in enumerate(cels):
            w = 100 if i==0 else (40 if r==0 else 40+i*26)
            col = C['navy'] if i==0 else fg
            s += f'<rect x="{120}" y="{y+i*0}" width="0" height="0"/>'
            s += f'<rect x="{120+i*120}" y="{y+14}" width="{min(w,110)}" height="34" rx="6" fill="{col if i==0 else bg}" stroke="{col}" stroke-width="2"/><text x="{120+i*120+min(w,110)/2}" y="{y+36}" text-anchor="middle" font-size="10.5" font-weight="900" fill="{"#fff" if i==0 else fg}">{c if i==0 else ""}</text><text x="{120+i*120+55}" y="{y+64}" text-anchor="middle" font-size="11" font-weight="700" fill="{C["ink"]}">{"" if i==0 else c}</text>'
    s += f'<text x="320" y="206" text-anchor="middle" font-size="10.5" font-weight="800" fill="{C["ink"]}">Restaurar na quarta: incremental = completo + SEG + TER + QUA · diferencial = completo + o de QUA.</text>'
    return s + '</svg><figcaption>Incremental copia o que mudou desde o último backup; diferencial, desde o último completo (os blocos crescem).</figcaption></figure>'

def rede():
    N,B=C['navy'],C['blue']
    s = f'<figure><svg viewBox="0 0 640 220" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    s += '<g stroke="#9aa6b5" stroke-width="3"><line x1="120" y1="60" x2="250" y2="110"/><line x1="120" y1="160" x2="250" y2="110"/><line x1="250" y1="110" x2="380" y2="110"/><line x1="380" y1="110" x2="520" y2="110"/></g>'
    for x,y,t,a in [(80,60,"PC","notebook"),(80,160,"IMPRESSORA","de rede")]:
        s += f'<rect x="{x-50}" y="{y-22}" width="100" height="44" rx="10" fill="{C["sky"]}" stroke="{B}" stroke-width="2"/><text x="{x}" y="{y-2}" text-anchor="middle" font-size="11" font-weight="900" fill="{B}">{t}</text><text x="{x}" y="{y+13}" text-anchor="middle" font-size="9.5" fill="{C["ink"]}">{a}</text>'
    for x,t,a,fg,bg in [(250,"SWITCH","liga aparelhos da LAN",C['green'],C['greensoft']),(380,"ROTEADOR","liga redes diferentes",C['golddeep'],C['goldsoft'])]:
        s += f'<rect x="{x-62}" y="84" width="124" height="52" rx="10" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x}" y="106" text-anchor="middle" font-size="12" font-weight="900" fill="{fg}">{t}</text><text x="{x}" y="124" text-anchor="middle" font-size="9" fill="{C["ink"]}">{a}</text>'
    s += f'<path d="M500 128 a26 26 0 0 1 50 -10 a18 18 0 0 1 22 30 h-62 a16 16 0 0 1 -10 -20z" fill="{NV}" stroke="{N}" stroke-width="2.5"/><text x="540" y="142" text-anchor="middle" font-size="11" font-weight="900" fill="{N}">INTERNET</text>'
    s += f'<rect x="20" y="196" width="400" height="20" rx="5" fill="{C["sky"]}"/><text x="220" y="210" text-anchor="middle" font-size="10" font-weight="900" fill="{B}">REDE LOCAL (LAN)</text><text x="540" y="210" text-anchor="middle" font-size="10" font-weight="900" fill="{N}">REDE MUNDIAL (WAN)</text>'
    return s + '</svg><figcaption>Uma rede doméstica ou de escritório, de forma simplificada.</figcaption></figure>'

# ================================================================ APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">Informática sem complicação: o que é cada coisa, para que serve e como as bancas perguntam.</p>
<p>Este é o <strong>Caderno 16 da coleção</strong>, dedicado à <strong>Informática para Concursos</strong>. A disciplina aparece em editais de Guarda Municipal, polícias e cargos administrativos e costuma cobrar <strong>conceitos práticos</strong>: identificar um periférico, saber o que faz um atalho, ler uma fórmula de planilha, reconhecer um golpe de <em>phishing</em>.</p>
<p>O conteúdo é <strong>introdutório</strong> e segue as versões em português do <strong>Windows</strong>, do <strong>Microsoft Word e Excel</strong> e do <strong>LibreOffice</strong>. Atalhos e menus mudam entre programas, idiomas e versões: quando houver diferença importante, o caderno avisa. Confira sempre a versão indicada no edital.</p>
{table(["Recurso","Onde está"],[["Ciclo entrada · processamento · saída","Unidade 1"],["Pirâmide da memória","Unidade 1"],["Tabelas de atalhos (Windows, Word, Writer, navegador)","Unidades 2 a 4"],["Planilha comentada e exercício de fórmulas","Unidade 3"],["Anatomia de uma URL e fluxo do e-mail","Unidade 4"],["Quadro dos malwares e linha do tempo do backup","Unidade 5"],["Mapa conceitual, erros comuns, flashcards e 24 questões autorais","Revisão e prática"]],["58%",None])}''', first=True)

toc_page([("u","UNIDADE 1 · CONCEITOS BÁSICOS E HARDWARE","U1"),("","1. O computador e a informação digital","A01"),("","2. Componentes e periféricos","A02"),("","3. Memória e armazenamento","A03"),
 ("u","UNIDADE 2 · SOFTWARE, SISTEMAS OPERACIONAIS E WINDOWS","U2"),("","4. Tipos de software e licenças","A04"),("","5. Sistemas operacionais","A05"),("","6. Windows: arquivos e pastas","A06"),("","7. Atalhos do Windows","A07"),
 ("u","UNIDADE 3 · PROCESSADORES DE TEXTO E PLANILHAS","U3"),("","8. Processadores de texto","A08"),("","9. Planilhas: células e fórmulas","A09"),("","10. Funções e mensagens de erro","A10"),
 ("u","UNIDADE 4 · INTERNET, NAVEGADORES E E-MAIL","U4"),("","11. Internet: conceitos","A11"),("","12. Navegadores","A12"),("","13. Correio eletrônico","A13"),
 ("u","UNIDADE 5 · SEGURANÇA DA INFORMAÇÃO","U5"),("","14. Princípios de segurança","A14"),("","15. Malware","A15"),("","16. Golpes, senhas e proteção","A16"),("","17. Backup","A17"),
 ("u","UNIDADE 6 · REDES (INTRODUTÓRIO)","U6"),("","18. Redes e equipamentos","A18"),("","19. Computação em nuvem","A19"),
 ("u","REVISÃO E PRÁTICA","RV"),("","Mapa conceitual · Erros mais comuns","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),("","Gabarito, respostas dos treinos e referências","R4")])

# ================================================================ UNIDADE 1
opener("01","UNIDADE 1","Conceitos básicos e hardware",["O computador e a informação digital","Componentes e periféricos","Memória e armazenamento"],"U1")

add(H(1,'O computador e a <span class="hl">informação digital</span>','Hardware, software e o sistema binário.', "A01") +
 computador() +
 table(["Conceito","O que é"],[
  ["Hardware","A parte <b>física</b> do computador: tudo o que se pode tocar (placa-mãe, processador, teclado, monitor)"],
  ["Software","A parte <b>lógica</b>: programas e sistemas, as instruções que dizem ao hardware o que fazer"],
  ["Bit","Menor unidade de informação: 0 ou 1 (sistema binário)"],
  ["Byte","Conjunto de <b>8 bits</b>; representa, por exemplo, um caractere"]],["22%",None]) +
 traduz(p('Pense numa cozinha: o <strong>hardware</strong> é o fogão, as panelas e os ingredientes; o <strong>software</strong> é a receita. Sem receita, o fogão não sabe o que fazer; sem fogão, a receita não sai do papel. E o computador só entende uma “língua”: <strong>0 e 1</strong>, desligado e ligado.')))

add(H(1,'Unidades de <span class="hl">medida</span>','De bit a terabyte.') +
 table(["Unidade","Equivale a (convenção usual em provas)"],[
  ["1 byte (B)","8 bits"],["1 kilobyte (KB)","1.024 bytes"],["1 megabyte (MB)","1.024 KB"],["1 gigabyte (GB)","1.024 MB"],["1 terabyte (TB)","1.024 GB"]],["34%",None]) +
 lembre(p('Na base binária, cada degrau multiplica por <strong>1.024</strong> (2 elevado a 10). Fabricantes de discos costumam usar o padrão decimal (1 GB = 1 bilhão de bytes), por isso um disco “de 1 TB” aparece com menos espaço no Windows. Em provas, salvo indicação diferente, use <strong>1.024</strong>.'), "Por que 1.024 e não 1.000?") +
 ex(p('Uma conexão de <b>100 Mbps</b> (megabits por segundo) não baixa 100 megabytes por segundo: como 1 byte = 8 bits, o máximo teórico é cerca de <b>12,5 MB/s</b>. Velocidade de rede costuma ser medida em <b>bits</b>; tamanho de arquivo, em <b>bytes</b>.')) +
 memo('<strong>1 byte = 8 bits</strong>. Cada degrau (KB, MB, GB, TB) = <strong>×1.024</strong>. Internet em <strong>bits</strong> (b minúsculo); arquivos em <strong>bytes</strong> (B maiúsculo).'))

add(H(1,'Componentes e <span class="hl">periféricos</span>','O que fica dentro e o que fica em volta.', "A02") +
 table(["Componente","Função"],[
  ["Placa-mãe","Placa principal que interliga todos os componentes"],
  ["Processador (CPU)","O “cérebro”: executa as instruções. Tem a <b>unidade de controle</b> (coordena), a <b>ULA</b> (unidade lógica e aritmética, faz cálculos e comparações) e os <b>registradores</b> (memórias internas ultrarrápidas)"],
  ["Fonte de alimentação","Converte a energia da tomada para os componentes"],
  ["Placa de vídeo","Processa as imagens exibidas no monitor (pode ser integrada ou dedicada)"]],["26%",None]) +
 table(["Periférico de...","Exemplos"],[
  ["<b>Entrada</b> (envia dados ao computador)","Teclado, mouse, scanner, microfone, webcam, leitor de código de barras"],
  ["<b>Saída</b> (recebe dados do computador)","Monitor, impressora, caixa de som, fone de ouvido, projetor"],
  ["<b>Entrada e saída</b> (mistos)","Tela sensível ao toque (touchscreen), impressora multifuncional (imprime e digitaliza), pen drive e HD externo (gravam e leem)"]],["34%",None]) +
 pega('<ul><li><b>Monitor comum</b> é só saída; o <b>touchscreen</b> é entrada e saída.</li><li>A <b>multifuncional</b> é mista porque também digitaliza (scanner = entrada).</li><li>Webcam e microfone são de <b>entrada</b>, mesmo sendo usados em chamadas.</li></ul>'))

add(H(1,'Memória e <span class="hl">armazenamento</span>','Onde o computador trabalha e onde ele guarda.', "A03") +
 piramide_mem() +
 table(["Tipo","Característica principal"],[
  ["RAM","Memória de trabalho, onde ficam os programas em uso. É <b>volátil</b>: apaga ao desligar"],
  ["ROM","Memória de leitura, <b>não volátil</b>; guarda o firmware de inicialização (BIOS/UEFI)"],
  ["Cache","Memória pequena e muito rápida entre a CPU e a RAM, com os dados mais usados"],
  ["Memória virtual","Espaço do disco usado como extensão da RAM quando ela acaba (é mais lento)"],
  ["HD, SSD, pen drive","Armazenamento <b>permanente</b> (não volátil). O HD é magnético, com partes móveis; o SSD e o pen drive usam memória flash, sem partes móveis, e o SSD é bem mais rápido que o HD"]],["24%",None]) +
 memo('RAM = <strong>volátil</strong> (some ao desligar). ROM, HD, SSD = <strong>não voláteis</strong>. Ordem de velocidade: <strong>registradores > cache > RAM > SSD > HD</strong>.'))

treino(1, [
 ("Hardware é a parte física do computador, e software é a parte lógica.","C","Definições básicas."),
 ("Um byte corresponde a 10 bits.","E","1 byte = 8 bits."),
 ("O scanner é um periférico de saída.","E","É de entrada: envia a imagem ao computador."),
 ("A impressora multifuncional, que imprime e digitaliza, é periférico de entrada e saída.","C","Imprimir é saída; digitalizar é entrada."),
 ("A memória RAM é volátil: seu conteúdo é perdido quando o computador é desligado.","C","Por isso é preciso salvar o arquivo no disco."),
 ("O HD é mais rápido que a memória cache.","E","A cache é muito mais rápida; o HD é o mais lento da hierarquia.")])

# ================================================================ UNIDADE 2
opener("02","UNIDADE 2","Software, sistemas operacionais e Windows",["Tipos de software e licenças","Sistemas operacionais","Arquivos e pastas","Atalhos do Windows"],"U2")

add(H(2,'Tipos de software e <span class="hl">licenças</span>','Para que serve cada programa e o que se pode fazer com ele.', "A04") +
 table(["Tipo","Exemplo","Para quê"],[
  ["Software básico (de sistema)","Windows, Linux, macOS, Android","Gerencia o hardware e serve de base para os demais programas"],
  ["Aplicativo","Word, Excel, navegador, WhatsApp","Executa tarefas do usuário"],
  ["Utilitário","Antivírus, compactador (ZIP), desfragmentador","Manutenção, proteção e otimização do sistema"]],["26%","30%",None]) +
 table(["Licença","O que significa"],[
  ["Proprietário","O uso depende de licença do fabricante; em regra, o código-fonte é fechado (ex.: Windows, Microsoft Office)"],
  ["Software livre","Garante as liberdades de <b>executar</b>, <b>estudar</b> (acesso ao código-fonte), <b>redistribuir</b> cópias e <b>modificar e distribuir</b> versões modificadas (ex.: Linux, LibreOffice, Firefox)"],
  ["Freeware","Gratuito, mas não necessariamente com código aberto"],
  ["Shareware / trial","Uso gratuito por tempo ou com recursos limitados; depois exige pagamento"]],["24%",None]) +
 pega('<ul><li><b>Software livre não significa gratuito</b>: “livre” se refere à liberdade, não ao preço. Pode haver cobrança por distribuição ou suporte.</li><li><b>Freeware não é software livre</b>: pode ser grátis e ter código fechado.</li></ul>'))

add(H(2,'Sistemas <span class="hl">operacionais</span>','O “gerente” do computador.', "A05") +
 p('O <strong>sistema operacional (SO)</strong> é o software que gerencia o processador, a memória, os arquivos e os dispositivos, e oferece a interface para o usuário e para os programas. Seu núcleo é chamado de <strong>kernel</strong>.') +
 table(["Sistema","Características para prova"],[
  ["Windows (Microsoft)","Proprietário; o mais usado em computadores pessoais e órgãos públicos"],
  ["Linux","Kernel livre; distribuído em <b>distribuições</b> (Ubuntu, Debian, Fedora, Mint); muito usado em servidores"],
  ["macOS (Apple)","Proprietário; computadores da Apple"],
  ["Android e iOS","Sistemas de dispositivos móveis; o Android tem base no kernel Linux"]],["26%",None]) +
 cards([("cpu","Gerencia o processador","decide qual programa usa a CPU e quando"),("layers","Gerencia a memória","distribui a RAM entre os programas"),("folder","Gerencia arquivos","organiza pastas, nomes e permissões")]) +
 memo('SO = <strong>gerente do hardware</strong> + interface. Kernel = <strong>núcleo</strong>. Linux = <strong>livre</strong>, em <strong>distribuições</strong>.'))

add(H(2,'Windows: arquivos e <span class="hl">pastas</span>','Explorador de Arquivos, extensões e Lixeira.', "A06") +
 table(["Conceito","Explicação"],[
  ["Arquivo","Conjunto de dados com nome, por exemplo <b>relatorio.docx</b>; a parte depois do ponto é a <b>extensão</b>, que indica o tipo"],
  ["Pasta (diretório)","Recipiente que organiza arquivos e outras pastas (subpastas)"],
  ["Caminho","Endereço do arquivo, como C:\\Usuários\\Ana\\Documentos\\relatorio.docx"],
  ["Nomes proibidos","No Windows, o nome não pode conter os caracteres \\ / : * ? \" &lt; &gt; |"],
  ["Lixeira","A tecla Delete envia o arquivo do disco local para a Lixeira (é possível restaurar); <b>Shift + Delete</b> exclui sem passar por ela. Em regra, arquivos apagados de pen drives e pastas de rede não vão para a Lixeira"]],["22%",None]) +
 table(["Extensão","Tipo"],[
  [".docx · .odt","Texto (Word · LibreOffice Writer)"],[".xlsx · .ods","Planilha (Excel · LibreOffice Calc)"],[".pptx · .odp","Apresentação"],[".pdf","Documento portátil"],
  [".txt","Texto simples"],[".jpg · .png","Imagem"],[".mp3 · .mp4","Áudio · vídeo"],[".zip · .rar","Compactado"],[".exe","Executável (programa) do Windows"]],["30%",None]))

atencao(p('<strong>Arrastar e soltar</strong> é uma das pegadinhas preferidas das bancas. No Explorador de Arquivos do Windows:') +
 table(["Ação com o mouse","Resultado"],[
  ["Arrastar para uma pasta da <b>mesma unidade</b> (C: para C:)","<b>Move</b> o arquivo"],
  ["Arrastar para <b>outra unidade</b> (C: para o pen drive)","<b>Copia</b> o arquivo"],
  ["Arrastar segurando <b>Ctrl</b>","Copia"],
  ["Arrastar segurando <b>Shift</b>","Move"],
  ["Arrastar segurando <b>Alt</b>","Cria um atalho"]],["50%",None]) +
 scene3([("MESMA UNIDADE",C['blue'],C['sky'],"prof",["C: para C:","o arquivo","muda de lugar."],"MOVE"),
  ("OUTRA UNIDADE",C['green'],C['greensoft'],"profa",["C: para pen drive:","o original","continua no C:."],"COPIA"),
  ("SHIFT + DELETE",C['red'],C['redsoft'],"prof",["Apaga sem","passar pela","Lixeira."],"PERMANENTE")], "Situação ilustrada: o que acontece com o arquivo."),
 ["Mover", "Copiar", "Atalho", "Lixeira"])

add(H(2,'Atalhos do <span class="hl">Windows</span>','Os mais cobrados.', "A07") +
 table(["Atalho","Função"],[
  [kbd("Ctrl","C")+" · "+kbd("Ctrl","X")+" · "+kbd("Ctrl","V"),"Copiar · recortar · colar"],
  [kbd("Ctrl","Z"),"Desfazer"],
  [kbd("Ctrl","A"),"Selecionar tudo (no Windows em português)"],
  [kbd("Alt","Tab"),"Alternar entre janelas abertas"],
  [kbd("Alt","F4"),"Fechar a janela ou o programa ativo"],
  [kbd("Ctrl","Shift","Esc"),"Abrir o Gerenciador de Tarefas"],
  [kbd("Win","E"),"Abrir o Explorador de Arquivos"],
  [kbd("Win","D"),"Mostrar a área de trabalho"],
  [kbd("Win","L"),"Bloquear o computador"],
  [kbd("Win","R"),"Abrir a caixa Executar"],
  [kbd("Win","V"),"Histórico da área de transferência"],
  [kbd("Win","Shift","S"),"Capturar parte da tela"],
  [kbd("F2"),"Renomear o item selecionado"],
  [kbd("Shift","Delete"),"Excluir sem enviar para a Lixeira"]],["44%",None]) +
 memo('<strong>Win + E</strong> = Explorador · <strong>Win + D</strong> = Desktop · <strong>Win + L</strong> = Lock (bloquear) · <strong>F2</strong> = renomear · <strong>Ctrl + Shift + Esc</strong> = Gerenciador de Tarefas.'))

treino(2, [
 ("O sistema operacional é um software básico, que gerencia os recursos de hardware.","C","É a base para os demais programas."),
 ("Todo software livre é necessariamente gratuito.","E","“Livre” se refere a liberdades; pode haver cobrança."),
 ("No Windows, a extensão .xlsx indica uma planilha do Excel.","C",".ods é a do LibreOffice Calc."),
 ("Arrastar um arquivo de uma pasta do disco C: para outra pasta do disco C:, sem teclas, copia o arquivo.","E","Na mesma unidade, move; para outra unidade, copia."),
 ("O atalho Shift + Delete exclui o arquivo sem enviá-lo para a Lixeira.","C","Exclusão permanente."),
 ("O atalho Win + L abre o Explorador de Arquivos.","E","Win + L bloqueia; Win + E abre o Explorador.")])

# ================================================================ UNIDADE 3
opener("03","UNIDADE 3","Processadores de texto e planilhas",["Processadores de texto","Planilhas: células e fórmulas","Funções e mensagens de erro"],"U3")

add(H(3,'Processadores de <span class="hl">texto</span>','Word (Microsoft) e Writer (LibreOffice).', "A08") +
 p('Processadores de texto criam e formatam documentos: fonte, parágrafos, tabelas, imagens, cabeçalho e rodapé, numeração de páginas, revisão ortográfica. Os atalhos mudam conforme o programa <strong>e o idioma</strong>, e as bancas exploram justamente essa diferença:') +
 table(["Ação","Word em português","LibreOffice Writer"],[
  ["Negrito",kbd("Ctrl","N"),kbd("Ctrl","B")],
  ["Itálico",kbd("Ctrl","I"),kbd("Ctrl","I")],
  ["Sublinhado",kbd("Ctrl","S"),kbd("Ctrl","U")],
  ["Salvar",kbd("Ctrl","B"),kbd("Ctrl","S")],
  ["Selecionar tudo",kbd("Ctrl","T"),kbd("Ctrl","A")],
  ["Abrir",kbd("Ctrl","A"),kbd("Ctrl","O")],
  ["Novo documento",kbd("Ctrl","O"),kbd("Ctrl","N")],
  ["Centralizar · justificar",kbd("Ctrl","E")+" · "+kbd("Ctrl","J"),kbd("Ctrl","E")+" · "+kbd("Ctrl","J")],
  ["Imprimir",kbd("Ctrl","P"),kbd("Ctrl","P")],
  ["Verificar ortografia",kbd("F7"),kbd("F7")]],["30%","35%",None]) +
 pega('<ul><li>No <b>Word em português</b>, Ctrl + S <b>sublinha</b> e Ctrl + B <b>salva</b>. No Writer (e no Word em inglês), Ctrl + B é <b>negrito</b> e Ctrl + S é <b>salvar</b>.</li><li>No Word em português, <b>Ctrl + T</b> seleciona tudo; no navegador, Ctrl + T abre uma nova guia.</li></ul>'))

add(H(3,'Planilhas: células e <span class="hl">fórmulas</span>','Excel (Microsoft) e Calc (LibreOffice).', "A09") +
 planilha() +
 table(["Regra","Explicação"],[
  ["Célula","Encontro de uma coluna (letra) com uma linha (número): <b>B3</b>"],
  ["Fórmula","Começa com <b>=</b> (sinal de igual). Ex.: =B2*2"],
  ["Intervalo (:)","<b>A1:A5</b> = de A1 até A5 (cinco células)"],
  ["União (;)","<b>A1;A5</b> = só A1 e A5 (duas células)"],
  ["Operadores","+ soma · - subtração · * multiplicação · / divisão · ^ potência"],
  ["Ordem","Primeiro parênteses, depois potência, depois multiplicação e divisão, por fim soma e subtração"]],["24%",None]) +
 memo('Fórmula começa com <strong>=</strong>. <strong>Dois-pontos</strong> = “até”; <strong>ponto e vírgula</strong> = “e”. =2+3*4 dá <strong>14</strong>; =(2+3)*4 dá <strong>20</strong>.'))

atencao(p('<strong>Referências relativas, absolutas e mistas.</strong> Ao copiar uma fórmula para outra célula, as referências “andam” junto, a menos que estejam travadas pelo cifrão ($).') +
 table(["Referência","Ao copiar a fórmula","Exemplo: fórmula em C1 copiada para D2"],[
  ["Relativa: <b>A1</b>","Linha e coluna mudam","=A1 vira =B2"],
  ["Absoluta: <b>$A$1</b>","Nada muda","=$A$1 continua =$A$1"],
  ["Mista: <b>$A1</b>","Coluna travada, linha muda","=$A1 vira =$A2"],
  ["Mista: <b>A$1</b>","Linha travada, coluna muda","=A$1 vira =B$1"]],["24%","30%",None]) +
 ex(p('<b>Exercício prático.</b> Em C2 está =B2*$E$1 (E1 guarda a taxa). Copiando C2 para C3, a fórmula fica <b>=B3*$E$1</b>: B2 andou uma linha; $E$1 ficou travado. Copiando C2 para D2 (uma coluna à direita), fica <b>=C2*$E$1</b>.'), "Exercício prático") +
 lembre(p('A tecla <strong>F4</strong>, com o cursor sobre a referência durante a edição da fórmula no Excel, alterna entre A1, $A$1, A$1 e $A1.'), "Dica de produtividade"),
 ["Relativa A1", "Absoluta $A$1", "Mista $A1 e A$1"], "Referências na planilha")

add(H(3,'Funções e mensagens de <span class="hl">erro</span>','As funções mais cobradas.', "A10") +
 table(["Função (português)","O que faz","Exemplo"],[
  ["SOMA","Soma os valores","=SOMA(A1:A5)"],
  ["MÉDIA","Média aritmética","=MÉDIA(A1:A5)"],
  ["MÁXIMO · MÍNIMO","Maior · menor valor","=MÁXIMO(A1:A5)"],
  ["CONT.NÚM","Conta células com números","=CONT.NÚM(A1:A5)"],
  ["CONT.SE","Conta células que atendem a um critério","=CONT.SE(A1:A5;\"&gt;7\")"],
  ["SE","Testa uma condição e devolve um de dois resultados","=SE(B2&gt;=7;\"Aprovado\";\"Reprovado\")"],
  ["PROCV","Procura um valor na primeira coluna de uma tabela e devolve o de outra coluna","=PROCV(A2;E2:F10;2;FALSO)"]],["24%","40%",None]) +
 table(["Erro","Significado provável"],[
  ["#DIV/0!","Divisão por zero"],["#NOME?","Nome de função ou texto não reconhecido (ex.: =SOMMA)"],["#REF!","Referência a célula inválida (por exemplo, apagada)"],
  ["#VALOR!","Tipo de dado errado (ex.: somar texto)"],["#N/D","Valor não disponível (ex.: PROCV não encontrou)"],["#####","Coluna estreita demais para exibir o valor"]],["24%",None]) +
 ex(p('Notas 6, 8 e 10 em A1:A3. =MÉDIA(A1:A3) dá <b>8</b>; =MÁXIMO(A1:A3) dá <b>10</b>; =CONT.SE(A1:A3;"&gt;=8") dá <b>2</b>; =SE(MÉDIA(A1:A3)&gt;=7;"Aprovado";"Reprovado") dá <b>Aprovado</b>.')))

treino(3, [
 ("No Word em português, o atalho Ctrl + N aplica negrito.","C","No Writer, o negrito é Ctrl + B."),
 ("No Word em português, Ctrl + B aplica negrito.","E","No Word em português, Ctrl + B salva."),
 ("Em uma planilha, toda fórmula começa com o sinal de igual.","C","Ex.: =A1+B1."),
 ("A referência A1:A4 abrange apenas as células A1 e A4.","E","Dois-pontos indica intervalo: A1, A2, A3 e A4."),
 ("A fórmula =2+3*4 resulta em 20.","E","Multiplicação primeiro: 2 + 12 = 14."),
 ("Copiando =$A$1*B1 de C1 para C2, a fórmula fica =$A$1*B2.","C","$A$1 é absoluta; B1 é relativa e anda uma linha.")])

# ================================================================ UNIDADE 4
opener("04","UNIDADE 4","Internet, navegadores e e‑mail",["Internet: conceitos","Navegadores","Correio eletrônico"],"U4")

add(H(4,'Internet: <span class="hl">conceitos</span>','Rede mundial, web, URL e protocolos.', "A11") +
 url() +
 table(["Conceito","O que é"],[
  ["Internet","Rede mundial que interliga redes de computadores"],
  ["WWW (web)","Serviço da internet formado por páginas ligadas por hiperlinks; internet e web não são a mesma coisa (e-mail também usa a internet)"],
  ["HTTP · HTTPS","Protocolos de transferência de páginas; o HTTPS acrescenta criptografia (TLS) e exibe o <b>cadeado</b> no navegador"],
  ["DNS","Sistema que traduz nomes de domínio (www.exemplo.gov.br) em endereços IP"],
  ["Endereço IP","Número que identifica um dispositivo na rede (ex.: 192.168.0.1)"],
  ["Intranet · extranet","Intranet: rede <b>privada</b> de uma organização que usa as tecnologias da internet. Extranet: parte da intranet acessível a parceiros externos autorizados"],
  ["Download · upload","Download: baixar da rede para o seu dispositivo. Upload: enviar do seu dispositivo para a rede"]],["22%",None]) +
 pega('<ul><li>O <b>cadeado</b> indica conexão criptografada, mas <b>não garante</b> que o site seja legítimo: sites falsos também podem usar HTTPS.</li><li><b>Intranet</b> usa os mesmos protocolos da internet; o que muda é que o acesso é restrito.</li></ul>'))

add(H(4,'<span class="hl">Navegadores</span>','Chrome, Edge, Firefox, Safari.', "A12") +
 table(["Recurso","Explicação"],[
  ["Guias (abas)","Várias páginas na mesma janela"],
  ["Favoritos","Endereços salvos para acesso rápido"],
  ["Histórico","Lista das páginas visitadas"],
  ["Cookies","Pequenos arquivos que os sites gravam para lembrar preferências e sessões"],
  ["Cache","Cópias de partes das páginas guardadas para carregar mais rápido"],
  ["Navegação anônima (privativa)","Não guarda histórico, cookies e dados de formulário <b>no seu dispositivo</b> depois que a janela é fechada; <b>não</b> esconde a navegação do provedor, da rede do trabalho ou dos sites"]],["30%",None]) +
 table(["Atalho (Chrome, Edge e Firefox)","Função"],[
  [kbd("Ctrl","T")+" · "+kbd("Ctrl","W"),"Nova guia · fechar guia"],
  [kbd("Ctrl","Shift","T"),"Reabrir a última guia fechada"],
  [kbd("Ctrl","Shift","N"),"Janela anônima no Chrome (InPrivate no Edge); no Firefox, é "+kbd("Ctrl","Shift","P")],
  [kbd("Ctrl","H")+" · "+kbd("Ctrl","J"),"Histórico · downloads"],
  [kbd("Ctrl","D"),"Adicionar aos favoritos"],
  [kbd("F5"),"Recarregar a página"],
  [kbd("Ctrl","F"),"Localizar na página"]],["44%",None]) +
 memo('Modo anônimo = <strong>não grava no seu computador</strong>, mas <strong>não deixa você invisível</strong>. Ctrl + Shift + T = <strong>reabre</strong> a guia fechada sem querer.'))

add(H(4,'Correio <span class="hl">eletrônico</span>','Campos, protocolos e boas práticas.', "A13") +
 email_fluxo() +
 table(["Item","Explicação"],[
  ["Endereço","usuario@dominio, por exemplo ana@exemplo.gov.br (o @ separa o usuário do domínio)"],
  ["Para","Destinatários principais"],
  ["Cc (com cópia)","Destinatários em cópia; todos veem quem recebeu"],
  ["Cco (com cópia oculta)","Destinatários ocultos: os demais <b>não</b> veem esses endereços"],
  ["Responder · responder a todos","Responde ao remetente · ao remetente e aos demais destinatários visíveis (Para e Cc)"],
  ["Encaminhar","Envia a mensagem recebida a outra pessoa; em regra, leva os anexos (o “responder” normalmente não leva)"],
  ["POP3 x IMAP","POP3 baixa as mensagens para o dispositivo (podendo removê-las do servidor); IMAP mantém as mensagens no servidor e sincroniza vários dispositivos"],
  ["Webmail","Acesso ao e-mail pelo navegador, sem programa instalado"]],["28%",None]) +
 ex(p('Uma servidora precisa avisar 40 moradores sobre uma reunião sem expor o e-mail de cada um. O correto é colocar os moradores em <b>Cco</b>. Se usar Cc, todos verão o endereço de todos.')))

treino(4, [
 ("Internet e World Wide Web são sinônimos perfeitos.","E","A web é um dos serviços da internet; o e-mail é outro."),
 ("O DNS traduz nomes de domínio em endereços IP.","C","É a “agenda” da internet."),
 ("O cadeado do HTTPS garante que o site é legítimo e confiável.","E","Garante a conexão criptografada; site falso também pode ter HTTPS."),
 ("A navegação anônima impede que o provedor de internet saiba quais sites foram visitados.","E","Só não grava dados no dispositivo local."),
 ("O protocolo SMTP é usado para o envio de e-mails.","C","POP3 e IMAP são de recebimento."),
 ("Destinatários em Cco não são vistos pelos demais destinatários.","C","Cópia oculta.")])

# ================================================================ UNIDADE 5
opener("05","UNIDADE 5","Segurança da informação",["Princípios","Malware","Golpes, senhas e proteção","Backup"],"U5")

add(H(5,'Princípios de <span class="hl">segurança</span>','O que a segurança da informação protege.', "A14") +
 cards([("lock","Confidencialidade","só quem tem autorização acessa a informação",C['blue']),("check","Integridade","a informação não é alterada indevidamente",C['green']),("clock","Disponibilidade","a informação está acessível quando necessária",C['golddeep'])]) +
 table(["Princípio complementar","Significado"],[
  ["Autenticidade","Garante a identidade de quem enviou ou criou a informação"],
  ["Irretratabilidade (não repúdio)","O autor não pode negar a autoria de uma ação ou mensagem"]],["34%",None]) +
 table(["Mecanismo","Para que serve"],[
  ["Criptografia simétrica","Usa a <b>mesma chave</b> para cifrar e decifrar"],
  ["Criptografia assimétrica","Usa um <b>par de chaves</b>: pública e privada"],
  ["Assinatura digital","Garante <b>autenticidade, integridade e não repúdio</b>; sozinha, não garante sigilo"],
  ["Certificado digital","Documento eletrônico que associa uma chave pública a uma pessoa ou instituição, emitido por autoridade certificadora"]],["30%",None]) +
 memo('Tripé <strong>CID</strong>: <strong>C</strong>onfidencialidade, <strong>I</strong>ntegridade, <strong>D</strong>isponibilidade. Assinatura digital: autenticidade + integridade + não repúdio (<strong>não</strong> sigilo).'))

add(H(5,'<span class="hl">Malware</span>','Os programas maliciosos e como se diferenciam.', "A15") +
 table(["Tipo","Como age","Marca registrada"],[
  ["Vírus","Insere cópias de si em outros arquivos ou programas","Depende de <b>execução</b> do arquivo infectado"],
  ["Worm (verme)","Propaga-se sozinho pela rede, explorando falhas","<b>Não precisa</b> de hospedeiro nem de execução pelo usuário"],
  ["Cavalo de troia","Parece um programa útil, mas executa ações maliciosas escondidas","“Presente de grego”"],
  ["Ransomware","Torna os dados inacessíveis, em geral por criptografia, e exige resgate","<b>Sequestro</b> de dados"],
  ["Spyware","Monitora o usuário e envia informações a terceiros","Espionagem"],
  ["Keylogger · screenlogger","Spywares que capturam as teclas digitadas · as imagens da tela","Roubo de senhas"],
  ["Adware","Exibe propaganda indesejada","Anúncios"],
  ["Backdoor","Abre uma “porta dos fundos” para o invasor voltar","Acesso remoto escondido"],
  ["Bot · botnet","Computador controlado remotamente · rede de computadores assim controlados","Usados em ataques em massa"],
  ["Rootkit","Conjunto de técnicas para esconder a presença do invasor ou de outro malware","Camuflagem"]],["20%","48%",None]) +
 pega('<ul><li><b>Vírus</b> precisa de hospedeiro e de execução; <b>worm</b> se espalha sozinho. É a diferença mais cobrada.</li><li><b>Keylogger</b> é um tipo de <b>spyware</b>.</li></ul>'))

add(H(5,'Golpes, senhas e <span class="hl">proteção</span>','Engenharia social e ferramentas de defesa.', "A16") +
 table(["Golpe","Como funciona"],[
  ["Phishing","Mensagem falsa (e-mail, SMS, WhatsApp) que imita banco, órgão público ou loja para levar a vítima a informar dados ou clicar em link malicioso"],
  ["Engenharia social","Manipulação psicológica: urgência, medo, falsa autoridade (“sou do suporte, preciso da sua senha”)"],
  ["Pharming","Redireciona o usuário para um site falso mesmo quando ele digita o endereço correto (por exemplo, alterando o DNS)"]],["22%",None]) +
 table(["Ferramenta","O que faz (e o que não faz)"],[
  ["Antivírus","Detecta e remove malware conhecido; precisa de atualização constante"],
  ["Firewall","Controla o <b>tráfego de rede</b> que entra e sai, segundo regras; <b>não</b> é antivírus e não remove vírus"],
  ["Autenticação em dois fatores (2FA)","Combina dois fatores diferentes: algo que você <b>sabe</b> (senha), <b>tem</b> (celular, token) ou <b>é</b> (biometria)"],
  ["Atualizações","Corrigem falhas de segurança exploradas por worms e invasores"]],["30%",None]) +
 scene3([("SENHA FORTE",C['green'],C['greensoft'],"profa",["Longa, com letras,","números e símbolos;","uma para cada site."],"use gerenciador"),
  ("NÃO COMPARTILHE",C['red'],C['redsoft'],"prof",["Nenhum suporte","legítimo pede","sua senha."],"engenharia social"),
  ("ATIVE O 2FA",C['blue'],C['sky'],"profa",["Senha + código","no celular:","dois fatores."],"camada extra")], "Situação ilustrada: boas práticas com senhas."))

add(H(5,'<span class="hl">Backup</span>','Cópia de segurança.', "A17") +
 backup_linha() +
 table(["Tipo","O que copia","Restauração"],[
  ["Completo (total)","Todos os arquivos selecionados","Só o último completo"],
  ["Incremental","O que mudou desde o <b>último backup de qualquer tipo</b>","Último completo + <b>todos</b> os incrementais seguintes"],
  ["Diferencial","O que mudou desde o <b>último backup completo</b>","Último completo + o <b>último</b> diferencial"]],["22%","42%",None]) +
 lembre(p('Boa prática conhecida como <strong>regra 3-2-1</strong>: manter <strong>3</strong> cópias dos dados, em <strong>2</strong> tipos de mídia diferentes, com <strong>1</strong> cópia fora do local (por exemplo, na nuvem). Backup que nunca foi testado pode falhar na hora de restaurar.'), "Boa prática") +
 memo('Incremental: <strong>desde o último backup</strong> (rápido para copiar, lento para restaurar). Diferencial: <strong>desde o último completo</strong> (cresce a cada dia, restaura com 2 conjuntos).'))

treino(5, [
 ("Os três pilares clássicos da segurança da informação são confidencialidade, integridade e disponibilidade.","C","Tripé CID."),
 ("A assinatura digital, por si só, garante o sigilo do conteúdo da mensagem.","E","Garante autenticidade, integridade e não repúdio; sigilo exige criptografia do conteúdo."),
 ("O worm se propaga automaticamente pela rede, sem precisar ser executado pelo usuário.","C","Diferença em relação ao vírus."),
 ("Ransomware é o malware que exibe propagandas indesejadas.","E","Esse é o adware; ransomware sequestra dados e pede resgate."),
 ("O firewall substitui o antivírus, pois remove arquivos infectados.","E","Firewall filtra tráfego de rede; não remove vírus."),
 ("O backup diferencial copia os arquivos alterados desde o último backup completo.","C","O incremental considera o último backup de qualquer tipo.")])

# ================================================================ UNIDADE 6
opener("06","UNIDADE 6","Redes (introdutório)",["Redes e equipamentos","Computação em nuvem"],"U6")

add(H(6,'Redes e <span class="hl">equipamentos</span>','Como os computadores conversam.', "A18") +
 rede() +
 table(["Tipo de rede","Alcance"],[
  ["PAN","Pessoal, poucos metros (ex.: Bluetooth entre celular e fone)"],
  ["LAN","Local: casa, escritório, prédio"],
  ["MAN","Metropolitana: uma cidade"],
  ["WAN","Longa distância: países e continentes; a internet é a maior delas"]],["22%",None]) +
 table(["Equipamento","Função"],[
  ["Switch","Interliga os dispositivos de uma rede local e encaminha os dados ao destino certo"],
  ["Roteador","Interliga redes diferentes (como a rede da casa e a internet) e escolhe o caminho dos pacotes"],
  ["Modem","Converte o sinal entre o computador e o meio de transmissão da operadora"],
  ["Ponto de acesso (access point)","Cria ou amplia a rede sem fio (Wi-Fi)"]],["30%",None]) +
 memo('Alcance crescente: <strong>PAN · LAN · MAN · WAN</strong>. <strong>Switch</strong> = dentro da rede; <strong>roteador</strong> = entre redes.'))

add(H(6,'Computação em <span class="hl">nuvem</span>','Usar recursos pela internet.', "A19") +
 p('<strong>Computação em nuvem</strong> é o uso de servidores, armazenamento e programas oferecidos pela internet, sob demanda, sem que o usuário precise manter a infraestrutura. Exemplos do dia a dia: guardar fotos em um serviço de armazenamento on-line, usar webmail, editar documentos no navegador.') +
 table(["Modelo de serviço","O que é entregue","Exemplo"],[
  ["SaaS (software como serviço)","O programa pronto, usado pelo navegador ou aplicativo","Webmail, editor de textos on-line"],
  ["PaaS (plataforma como serviço)","Ambiente para desenvolver e hospedar aplicações","Plataformas de desenvolvimento em nuvem"],
  ["IaaS (infraestrutura como serviço)","Servidores, rede e armazenamento virtuais","Máquinas virtuais alugadas"]],["30%","40%",None]) +
 cards([("cloud","Vantagem","acesso de qualquer lugar e de vários dispositivos"),("wifi","Dependência","exige conexão com a internet"),("lock","Cuidado","senha forte e 2FA protegem a conta")]) +
 memo('<strong>SaaS</strong> = software pronto · <strong>PaaS</strong> = plataforma · <strong>IaaS</strong> = infraestrutura.'))

treino(6, [
 ("A internet é considerada a maior rede do tipo WAN.","C","Rede de longa distância."),
 ("Uma rede Bluetooth entre o celular e o fone de ouvido é um exemplo de PAN.","C","Rede pessoal."),
 ("O switch é o equipamento que interliga redes diferentes, como a rede doméstica e a internet.","E","Esse é o roteador; o switch atua dentro da rede local."),
 ("O ponto de acesso (access point) cria ou amplia uma rede sem fio.","C","Wi-Fi."),
 ("No modelo SaaS, o usuário recebe um programa pronto para uso pela internet.","C","Ex.: webmail."),
 ("Arquivos salvos em nuvem podem ser acessados sem nenhuma conexão com a internet, em qualquer situação.","E","Em regra, a nuvem depende de conexão; alguns serviços mantêm cópias locais sincronizadas.")])

# ================================================================ REVISÃO
mapa(("INFORMÁTICA","PARA","CONCURSOS"), [
  ("HARDWARE",["entrada, saída e mistos","CPU: UC, ULA, registradores","RAM volátil"],C['navy'],NV),
  ("SOFTWARE E WINDOWS",["livre ≠ grátis","mesma unidade: move","Shift + Delete: sem Lixeira"],C['blue'],C['sky']),
  ("TEXTO E PLANILHA",["Word: Ctrl+N negrito","fórmula começa com =","$A$1 não anda"],C['green'],C['greensoft']),
  ("INTERNET E E-MAIL",["DNS: nome em IP","anônimo não é invisível","SMTP envia · Cco oculta"],C['golddeep'],C['goldsoft']),
  ("SEGURANÇA",["CID","worm sem hospedeiro","firewall ≠ antivírus"],C['red'],C['redsoft']),
  ("REDES E NUVEM",["PAN · LAN · MAN · WAN","roteador entre redes","SaaS · PaaS · IaaS"],C['navy'],NV)], "Mapa conceitual do Caderno 16.", "A informática da prova em seis blocos. Explique cada caixa em voz alta.", center_color="#29c4e6")

erros([
  ["“Um byte tem 10 bits.”","1 byte = 8 bits."],
  ["“Scanner é periférico de saída.”","É de entrada; a multifuncional é mista."],
  ["“A RAM guarda os arquivos mesmo desligada.”","A RAM é volátil; quem guarda é o HD/SSD."],
  ["“Software livre é sempre gratuito.”","Livre = liberdades; pode ser pago. Freeware = grátis, nem sempre livre."],
  ["“Arrastar na mesma unidade copia.”","Na mesma unidade, move; para outra unidade, copia."],
  ["“No Word em português, Ctrl + B é negrito.”","É salvar; negrito é Ctrl + N (no Writer, negrito é Ctrl + B)."],
  ["“A1:A4 são só duas células.”","Dois-pontos = intervalo (4 células); ponto e vírgula = células isoladas."]],
 [["“=2+3*4 dá 20.”","Dá 14: multiplicação antes da soma."],
  ["“Internet e web são a mesma coisa.”","A web é um serviço da internet."],
  ["“Cadeado = site confiável.”","Cadeado = conexão criptografada; o site pode ser falso."],
  ["“Navegação anônima esconde tudo.”","Só não grava dados no seu dispositivo."],
  ["“Vírus se espalha sozinho pela rede.”","Quem se espalha sozinho é o worm; o vírus depende de execução."],
  ["“Firewall remove vírus.”","Firewall filtra tráfego; quem remove é o antivírus."],
  ["“Incremental copia desde o último completo.”","Esse é o diferencial; o incremental, desde o último backup de qualquer tipo."]])

flashcards([("HARDWARE","1 byte equivale a?","8 bits."),
 ("HARDWARE","1 KB equivale a (convenção de prova)?","1.024 bytes."),
 ("HARDWARE","Partes da CPU?","Unidade de controle, ULA e registradores."),
 ("HARDWARE","Touchscreen é periférico de?","Entrada e saída."),
 ("MEMÓRIA","Memória volátil?","RAM: perde o conteúdo ao desligar."),
 ("MEMÓRIA","Para que serve a cache?","Guardar dados mais usados entre a CPU e a RAM, com alta velocidade."),
 ("SOFTWARE","Quatro liberdades do software livre?","Executar, estudar, redistribuir e modificar/distribuir modificações."),
 ("SOFTWARE","Núcleo do sistema operacional?","Kernel."),
 ("WINDOWS","Arrastar para outra unidade?","Copia (na mesma unidade, move)."),
 ("WINDOWS","Win + E · Win + D · Win + L?","Explorador · área de trabalho · bloquear."),
 ("WINDOWS","Shift + Delete?","Exclui sem passar pela Lixeira."),
 ("WORD","Negrito, sublinhado e salvar no Word em português?","Ctrl + N · Ctrl + S · Ctrl + B."),
 ("PLANILHA","A1:A5 x A1;A5?","Intervalo de 5 células x apenas 2 células."),
 ("PLANILHA","$A$1?","Referência absoluta: não muda ao copiar."),
 ("PLANILHA","#DIV/0!?","Divisão por zero."),
 ("INTERNET","O que faz o DNS?","Traduz nomes de domínio em endereços IP."),
 ("INTERNET","Intranet?","Rede privada que usa tecnologias da internet."),
 ("NAVEGADOR","Ctrl + Shift + T?","Reabre a última guia fechada."),
 ("E-MAIL","SMTP · POP3 · IMAP?","Envio · recebimento (baixa) · recebimento (sincroniza)."),
 ("E-MAIL","Cco?","Cópia oculta: demais destinatários não veem."),
 ("SEGURANÇA","Vírus x worm?","Vírus precisa de hospedeiro e execução; worm se propaga sozinho."),
 ("SEGURANÇA","Ransomware?","Sequestra dados (criptografa) e exige resgate."),
 ("SEGURANÇA","Fatores do 2FA?","Algo que você sabe, tem ou é (dois diferentes)."),
 ("BACKUP","Incremental x diferencial?","Desde o último backup x desde o último completo.")])

Q = [
 ("Hardware","Assinale a alternativa que apresenta apenas periféricos de entrada:",
  ["monitor e impressora.","teclado, mouse e scanner.","caixa de som e projetor.","monitor e caixa de som.","impressora e fone de ouvido."],"B",
  "Teclado, mouse e scanner enviam dados ao computador. Monitor, impressora, caixa de som, projetor e fone são de saída.","Entrada envia; saída recebe."),
 ("Hardware","A impressora multifuncional, que imprime e digitaliza documentos, é classificada como periférico:",
  ["apenas de entrada.","apenas de saída.","de entrada e saída.","de processamento.","de armazenamento interno."],"C",
  "Imprimir é saída; digitalizar (scanner) é entrada.","Multifuncional = mista."),
 ("Medidas","Considerando a convenção binária, 2 KB correspondem a:",
  ["2.000 bytes.","2.024 bytes.","2.048 bytes.","1.024 bits.","16 bits."],"C",
  "1 KB = 1.024 bytes; logo, 2 KB = 2.048 bytes.","KB = 1.024 bytes."),
 ("Memória","Sobre a memória RAM, é correto afirmar:",
  ["é não volátil e armazena o firmware de inicialização.","é volátil e armazena temporariamente os programas e dados em uso.","é mais lenta que o HD.","só existe em servidores.","é o mesmo que memória cache."],"B",
  "A RAM é a memória de trabalho, volátil. O firmware fica na ROM; o HD é mais lento; a cache é outra memória.","RAM: trabalho e volátil."),
 ("Memória","Na hierarquia de memória, a mais rápida entre as opções abaixo é:",
  ["HD.","SSD.","memória RAM.","registradores do processador.","pen drive."],"D",
  "Ordem: registradores, cache, RAM, SSD, HD.","Registradores no topo."),
 ("Software","Sobre software livre, é correto afirmar:",
  ["é sempre gratuito.","garante ao usuário, entre outras, a liberdade de estudar o programa e de modificá-lo.","é o mesmo que freeware.","não pode ser comercializado.","tem código-fonte sempre fechado."],"B",
  "Software livre garante executar, estudar, redistribuir e modificar. Pode ser comercializado; freeware é grátis, mas pode ter código fechado.","Livre = liberdade, não preço."),
 ("Sistemas operacionais","O componente central do sistema operacional, responsável por gerenciar diretamente o hardware, é o:",
  ["navegador.","kernel.","compactador.","antivírus.","editor de texto."],"B",
  "O kernel é o núcleo do SO.","Kernel = núcleo."),
 ("Windows","No Explorador de Arquivos do Windows, ao arrastar um arquivo do disco C: para um pen drive, sem pressionar nenhuma tecla, o arquivo será:",
  ["movido.","copiado.","excluído.","renomeado.","compactado."],"B",
  "Para outra unidade, o padrão é copiar; na mesma unidade, mover. Ctrl força cópia; Shift força movimentação.","Outra unidade = copia."),
 ("Windows","No Windows, o atalho que exclui o arquivo selecionado sem enviá-lo para a Lixeira é:",
  ["Ctrl + Delete.","Shift + Delete.","Alt + F4.","Ctrl + Z.","Win + D."],"B",
  "Shift + Delete exclui permanentemente. Alt + F4 fecha a janela; Ctrl + Z desfaz; Win + D mostra a área de trabalho.","Shift + Delete = sem Lixeira."),
 ("Windows","O atalho do Windows que bloqueia o computador é:",
  ["Win + E.","Win + D.","Win + L.","Win + R.","Alt + Tab."],"C",
  "Win + L bloqueia; Win + E abre o Explorador; Win + D mostra a área de trabalho; Win + R abre Executar; Alt + Tab alterna janelas.","L de lock."),
 ("Word","No Microsoft Word em português, os atalhos para aplicar negrito e para salvar o documento são, respectivamente:",
  ["Ctrl + B e Ctrl + S.","Ctrl + N e Ctrl + B.","Ctrl + G e Ctrl + S.","Ctrl + N e Ctrl + S.","Ctrl + I e Ctrl + B."],"B",
  "No Word em português: Ctrl + N negrito, Ctrl + B salvar, Ctrl + S sublinhado. Ctrl + B e Ctrl + S (negrito e salvar) valem no Writer e no Word em inglês.","Word em português: N = negrito, S = sublinhado, B = salvar."),
 ("Planilha","Em uma planilha, a fórmula =2+3*2^2 resulta em:",
  ["14.","20.","36.","100.","10."],"A",
  "Primeiro a potência (2^2 = 4), depois a multiplicação (3 × 4 = 12), por fim a soma (2 + 12 = 14).","Potência, multiplicação, soma."),
 ("Planilha","A fórmula =B2*$D$1, escrita na célula C2, é copiada para a célula C5. A fórmula em C5 será:",
  ["=B2*$D$1","=B5*$D$1","=B5*$D$4","=E5*$D$1","=B2*$D$4"],"B",
  "B2 é relativa e anda três linhas (B5); $D$1 é absoluta e não muda.","Cifrão trava."),
 ("Planilha","A expressão =SOMA(A1:A3) soma:",
  ["somente A1 e A3.","as células A1, A2 e A3.","as colunas A a C da linha 1.","apenas A2.","A1 multiplicado por A3."],"B",
  "Dois-pontos indica intervalo. Para somar só A1 e A3, usa-se =SOMA(A1;A3).","Dois-pontos = até."),
 ("Planilha","A mensagem de erro #DIV/0! indica:",
  ["nome de função digitado errado.","divisão por zero.","referência a célula excluída.","coluna estreita demais.","valor não encontrado pela procura."],"B",
  "#NOME? = nome inválido; #REF! = referência inválida; ##### = coluna estreita; #N/D = valor não disponível.","DIV/0 = dividir por zero."),
 ("Internet","O serviço responsável por traduzir nomes de domínio, como www.exemplo.gov.br, em endereços IP é o:",
  ["HTTP.","SMTP.","DNS.","FTP.","POP3."],"C",
  "O DNS faz a tradução de nomes em IP. HTTP transfere páginas; SMTP envia e-mail; FTP transfere arquivos; POP3 recebe e-mail.","DNS = agenda de endereços."),
 ("Internet","Sobre o cadeado exibido na barra de endereços em sites com HTTPS, é correto afirmar:",
  ["garante que o site pertence a um órgão público.","indica que a comunicação entre o navegador e o site é criptografada.","impede qualquer tipo de golpe.","significa que o site não usa cookies.","indica navegação anônima."],"B",
  "O cadeado indica conexão criptografada (TLS); não garante a legitimidade do site.","Cadeado = conexão cifrada."),
 ("Navegadores","A navegação anônima (privativa) nos navegadores:",
  ["torna o usuário invisível para o provedor de internet.","não armazena, no dispositivo, histórico e cookies da sessão depois que a janela é fechada.","bloqueia todos os vírus.","impede que os sites saibam o endereço IP do usuário.","apaga o histórico de navegação anterior."],"B",
  "O modo privativo apenas não grava dados localmente; provedor, rede e sites continuam podendo registrar o acesso.","Anônimo não é invisível."),
 ("E-mail","Para enviar um e-mail a vários destinatários sem que um veja o endereço dos outros, deve-se usar o campo:",
  ["Para.","Cc.","Cco.","Assunto.","Responder a todos."],"C",
  "Cco (com cópia oculta) esconde os destinatários entre si.","Cco = oculta."),
 ("E-mail","O protocolo que mantém as mensagens no servidor e sincroniza a caixa de entrada entre vários dispositivos é o:",
  ["SMTP.","IMAP.","HTTP.","DNS.","FTP."],"B",
  "IMAP sincroniza; POP3 baixa as mensagens; SMTP envia.","IMAP sincroniza."),
 ("Segurança","O malware que se propaga automaticamente pelas redes, explorando vulnerabilidades, sem necessidade de ser executado pelo usuário, é o:",
  ["vírus.","worm.","adware.","keylogger.","cavalo de troia."],"B",
  "O worm se autopropaga; o vírus depende de hospedeiro e execução.","Worm anda sozinho."),
 ("Segurança","Um servidor recebe um e-mail que imita o banco, com urgência para “atualizar dados” por um link. Trata-se de:",
  ["backup.","phishing.","firewall.","criptografia.","ransomware."],"B",
  "Phishing é a mensagem falsa que imita instituição para obter dados. Ransomware sequestra arquivos.","Phishing = pescaria de dados."),
 ("Segurança","Sobre o firewall, é correto afirmar:",
  ["remove vírus de arquivos infectados.","controla o tráfego de rede que entra e sai, conforme regras definidas.","substitui o backup.","é um tipo de malware.","só existe em celulares."],"B",
  "Firewall filtra conexões; quem remove vírus é o antivírus.","Firewall = porteiro da rede."),
 ("Backup","O tipo de backup que copia apenas os arquivos alterados desde o último backup completo, acumulando as alterações a cada execução, é o:",
  ["incremental.","diferencial.","completo.","espelhado.","manual."],"B",
  "Diferencial: desde o último completo. Incremental: desde o último backup de qualquer tipo.","Diferencial cresce.")]
questoes(Q, "BACDEBCAEDBCADEBACDEBCEA")
respostas_treinos()

referencias('''<h3>Base do conteúdo</h3><ul>
<li>Conceitos introdutórios de informática (hardware, software, memória, sistemas operacionais, internet, correio eletrônico, segurança, backup e redes), em linguagem didática.</li>
<li>Atalhos de teclado e nomes de funções das versões em português do Windows, do Microsoft Word e Excel e do LibreOffice Writer e Calc, e dos navegadores Chrome, Edge e Firefox.</li></ul>
<h3>Para aprofundar</h3><ul><li>Cartilha de Segurança para Internet, do CERT.br (cartilha.cert.br), material gratuito sobre golpes, malware e proteção.</li><li>Páginas oficiais de ajuda da Microsoft e do LibreOffice para a lista completa de atalhos da sua versão.</li></ul>''',
 'Informática não depende de legislação; o risco está nas <strong>diferenças entre versões</strong>. <strong>Limitações:</strong> atalhos e menus podem mudar entre versões, idiomas e configurações dos programas; o caderno usa as versões em português e indica as diferenças mais cobradas (Word x Writer). As definições de malware e de backup seguem as classificações usuais da área, que podem variar levemente entre autores e bancas. Confira o edital do seu concurso, que pode indicar versões específicas.', DATA)
encerramento("16", "Informática", 'Sugestão de continuação: <strong>Caderno 17 · Língua Portuguesa</strong>.')
gravar(HERE, "Mapa da Aprovação — Caderno 16 — Informática para Concursos", Q)
