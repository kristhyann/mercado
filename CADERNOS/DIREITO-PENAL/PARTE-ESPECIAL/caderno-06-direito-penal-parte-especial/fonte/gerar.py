"""Gera miolo.html do Caderno 06: Direito Penal — Parte Especial. Uso: python3 gerar.py
Todos os textos legais e penas foram conferidos no texto compilado do Código Penal (Planalto) em 26/11/2026."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from componentes import *

DATA = "26 de novembro de 2026"
P = []
def add(html, first=False): P.append(page(f'<div class="marker">§§P{len(P)+1:03d}§§</div>' + html, first))
U = {1:("UNIDADE 1","Crimes contra a vida"),2:("UNIDADE 2","Lesões corporais"),3:("UNIDADE 3","Crimes contra a honra"),4:("UNIDADE 4","Liberdade individual"),5:("UNIDADE 5","Crimes contra o patrimônio"),6:("UNIDADE 6","Administração Pública")}
def H(u, title, lead, marker=None): return head(U[u][0], U[u][1], title, lead, marker)
def cp(x): return f"{x} · Código Penal"
def p(t): return f"<p>{t}</p>"
def colors(*keys):
    m = {"b":(C['blue'],C['sky']),"g":(C['green'],C['greensoft']),"o":(C['golddeep'],C['goldsoft']),"r":(C['red'],C['redsoft']),"n":(C['navy'],'#e6e7ea')}
    return [m[k] for k in keys]
def atencao(html, kws=None, t='Atenção na prova'):
    add(pratica_title(t) + html + (kw(kws) if kws else ''))
def novo(txt, t="Atualização legislativa"):
    return lembre(p(txt), t)
def scene3(items, cap):
    """Três quadros ilustrados lado a lado: (título, cor, cor-fundo, personagem, balão[linhas], legenda)."""
    s = f'<figure><svg viewBox="0 0 640 260" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    for i,(t,fg,bg,who,lines,leg) in enumerate(items):
        x = i*214
        s += f'<rect x="{x+2}" y="2" width="206" height="256" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x+105}" y="26" text-anchor="middle" font-weight="900" font-size="14" fill="{fg}">{t}</text>'
        s += f'<rect x="{x+14}" y="38" width="182" height="{20+len(lines)*17}" rx="12" fill="#fff" stroke="{fg}" stroke-width="1.8"/>'
        s += "".join(f'<text x="{x+105}" y="{58+j*17}" text-anchor="middle" font-size="11.2" font-weight="800" fill="{C["ink"]}">{l}</text>' for j,l in enumerate(lines))
        s += f'<g transform="translate({x+70},{70+len(lines)*17})"><svg viewBox="0 0 100 170" width="62" height="105"><use href="#ch-{who}"/></svg></g>'
        s += f'<text x="{x+105}" y="244" text-anchor="middle" font-size="11" font-weight="900" fill="{fg}">{leg}</text>'
    return s + f'</svg><figcaption>{cap}</figcaption></figure>'

# ================================================================ APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">Os crimes mais cobrados em concursos de nível médio e policiais, com as diferenças entre crimes parecidos.</p>
<p>Este é o <strong>Caderno 06 da coleção</strong>, dedicado ao <strong>Direito Penal: Parte Especial</strong>, a parte do Código Penal que descreve <strong>cada crime</strong> e sua pena. O foco são os crimes que mais aparecem em provas de <strong>Guarda Municipal</strong>, <strong>polícias</strong> e concursos de nível médio: crimes contra a <strong>vida</strong>, <strong>lesões corporais</strong>, crimes contra a <strong>honra</strong>, a <strong>liberdade individual</strong> e o <strong>patrimônio</strong>, e as noções de crimes contra a <strong>Administração Pública</strong>.</p>
<p>Em prova, o mais difícil é <strong>não confundir crimes parecidos</strong>: furto, roubo e extorsão; calúnia, difamação e injúria; concussão e corrupção. Por isso este caderno tem muitos <strong>quadros comparativos</strong> e <strong>cenas ilustradas</strong>.</p>
{lembre(p(f'<strong>Atenção: a Parte Especial mudou muito entre 2024 e 2026.</strong> Entre outras, as Leis nº 14.994/2024 (feminicídio como crime autônomo), 14.811/2024 (intimidação sistemática), 15.134/2025, 15.159/2025, 15.181/2025, 15.358/2026 (marco legal do crime organizado), 15.384/2026 (vicaricídio), <strong>15.397/2026</strong> (reforma dos crimes patrimoniais, com aumento das penas de furto, roubo e receptação) e 15.517/2026 (furto e roubo de combustíveis). <strong>Todas as penas deste caderno foram conferidas no texto compilado do Código Penal no Planalto em {DATA}.</strong> Apostilas anteriores podem trazer penas desatualizadas.'), "Fontes e atualização")}
{table(["Recurso","Onde está"],[["Cenas: calúnia x difamação x injúria","Unidade 3"],["Cenas: furto x roubo x extorsão","Unidade 5"],["Cenas: concussão x corrupção passiva x corrupção ativa","Unidade 6"],["Quadros comparativos de penas e elementos","Em todas as unidades"],["24 questões autorais comentadas e treinos Certo ou Errado","Prática final e fim das unidades"]],["56%",None])}''', first=True)

TOC = [("u","UNIDADE 1 · CRIMES CONTRA A VIDA","U1"),("","1. Homicídio","A01"),("","2. Feminicídio e vicaricídio","A02"),("","3. Induzimento ao suicídio, infanticídio e aborto","A03"),
 ("u","UNIDADE 2 · LESÕES CORPORAIS","U2"),("","4. Lesão corporal: leve, grave, gravíssima e seguida de morte","A04"),("","5. Lesão em violência doméstica e contra a mulher","A05"),
 ("u","UNIDADE 3 · CRIMES CONTRA A HONRA","U3"),("","6. Calúnia, difamação e injúria","A06"),("","7. Aumentos de pena, exclusão, retratação e ação penal","A07"),
 ("u","UNIDADE 4 · CRIMES CONTRA A LIBERDADE INDIVIDUAL","U4"),("","8. Constrangimento ilegal e ameaça","A08"),("","9. Intimidação sistemática, perseguição e violência psicológica","A09"),("","10. Sequestro, cárcere privado e redução à condição análoga à de escravo","A10"),("","11. Violação de domicílio","A11"),
 ("u","UNIDADE 5 · CRIMES CONTRA O PATRIMÔNIO","U5"),("","12. Furto","A12"),("","13. Roubo","A13"),("","14. Extorsão e extorsão mediante sequestro","A14"),("","15. Furto x roubo x extorsão","A15"),("","16. Dano e apropriação indébita","A16"),("","17. Estelionato","A17"),("","18. Receptação e imunidades","A18"),
 ("u","UNIDADE 6 · CRIMES CONTRA A ADMINISTRAÇÃO PÚBLICA","U6"),("","19. Funcionário público e peculato","A19"),("","20. Concussão x corrupção passiva x corrupção ativa","A20"),("","21. Prevaricação, resistência, desobediência e desacato","A21"),
 ("u","REVISÃO E PRÁTICA","RV"),("","Mapa conceitual · Confusões mais comuns","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),("","Gabarito, respostas dos treinos e referências","R4")]
toc = "".join(f'<li class="u"><span class="t">{t}</span><span class="p" data-pg="{m}"></span></li>' if k=="u" else f'<li><span class="t">{t}</span><span class="p" data-pg="{m}"></span></li>' for k,t,m in TOC)
add(f'''<div class="unit"><span class="u">MAPA DO CADERNO</span></div><h1 class="big">Sumário</h1><ol class="toc" style="border-top:3px solid {C['navy']};margin-top:6pt">{toc}</ol>''')

def opener(num, kicker, title, items, marker):
    lis = "".join(f'<li><span>{i+1:02d}</span>{t}</li>' for i,t in enumerate(items))
    add(f'''<div class="marker">§§{marker}§§</div><div class="opener"><div class="num">{num}</div><div class="k">{kicker}</div><h1>{title}</h1><ul>{lis}</ul></div>''')
TREINOS = []
def treino(n, itens):
    TREINOS.append((n, itens))
    rows = "".join(f'<tr><td style="width:7%;text-align:center;font-weight:900;color:{C["navy"]}">{i+1}</td><td>{a}</td><td style="width:16%;text-align:center">( C ) &nbsp; ( E )</td></tr>' for i,(a,_,_) in enumerate(itens))
    add(f'''<div class="unit"><span class="u">TREINO RÁPIDO</span><span class="t">Unidade {n}</span></div><h1 class="big">Certo ou <span class="hl">errado?</span></h1>
<p class="lead">Marque C ou E sem consultar. As respostas comentadas estão no gabarito, no fim do caderno.</p>
<table><tr><th>#</th><th>Afirmação</th><th style="text-align:center">Sua resposta</th></tr>{rows}</table>''' + memo('Errou? Volte à página do assunto e releia a faixa <strong>Memorize</strong> e a <strong>Pegadinha</strong>.', "Dica:"))

# ================================================================ UNIDADE 1
opener("01","UNIDADE 1","Crimes contra a vida",["Homicídio","Feminicídio e vicaricídio","Induzimento ao suicídio, infanticídio e aborto"],"U1")

add(H(1,'<span class="hl">Homicídio</span> (art. 121)','Matar alguém: simples, privilegiado, qualificado e culposo.', "A01") +
 lei(cp("Art. 121, caput"),'<p>Art. 121. Matar alguém:<br>Pena - reclusão, de seis a vinte anos.</p>') +
 table(["Forma","O que é","Pena"],[
  ["Simples (caput)","Matar alguém, sem as circunstâncias especiais","Reclusão, 6 a 20 anos"],
  ["Privilegiado (§ 1º)","Motivo de relevante valor social ou moral, ou domínio de violenta emoção logo após injusta provocação da vítima","Redução de 1/6 a 1/3"],
  ["Qualificado (§ 2º)","Motivos ou meios mais graves (lista abaixo)","Reclusão, 12 a 30 anos"],
  ["Culposo (§ 3º)","Morte causada por imprudência, negligência ou imperícia","Detenção, 1 a 3 anos"],
  ["Organização criminosa ultraviolenta ou milícia (§ 2º-D)","Homicídio doloso praticado por integrante, no contexto do marco legal do crime organizado","Reclusão, 20 a 40 anos"]],["24%",None,"22%"]) +
 traduz(p('O homicídio protege o bem mais importante: a <strong>vida humana</strong> depois do nascimento. A lei separa as formas conforme a <strong>intenção</strong> (doloso ou culposo) e as <strong>circunstâncias</strong>: um motivo nobre diminui a pena (privilegiado); um motivo torpe ou um meio cruel aumentam (qualificado).')) +
 memo('Simples: <strong>6 a 20</strong>. Qualificado: <strong>12 a 30</strong>. Culposo: <strong>detenção de 1 a 3</strong>. No culposo, o juiz pode deixar de aplicar a pena (<strong>perdão judicial</strong>, § 5º) se as consequências atingirem o próprio agente de forma tão grave que a pena se torne desnecessária.'))

add(pratica_title("As qualificadoras do § 2º (texto vigente)") +
 table(["Inciso","Qualificadora (em síntese)","Tipo"],[
  ["I","Mediante paga ou promessa de recompensa, ou outro motivo torpe","Motivo"],["II","Motivo fútil","Motivo"],
  ["III","Veneno, fogo, explosivo, asfixia, tortura ou outro meio insidioso ou cruel, ou de que possa resultar perigo comum","Meio"],
  ["IV","Traição, emboscada, dissimulação ou outro recurso que dificulte ou torne impossível a defesa","Modo"],
  ["V","Para assegurar a execução, a ocultação, a impunidade ou vantagem de outro crime","Conexão"],
  ["VI","<b>Revogado</b> (Lei nº 14.994/2024): o feminicídio virou crime autônomo (art. 121-A)","—"],
  ["VII","Contra agentes de segurança pública e do sistema prisional, ou contra membros do Judiciário, MP, Defensoria, Advocacia Pública e oficiais de justiça, ou seus familiares, em razão da função (Lei nº 15.134/2025)","Vítima"],
  ["VIII","Com emprego de arma de fogo de uso restrito ou proibido","Meio"],["IX","Contra menor de 14 anos","Vítima"],
  ["X","Nas dependências de instituição de ensino (Lei nº 15.159/2025)","Local"]],["10%",None,"14%"]) +
 ex(p('Durante uma discussão sobre futebol, Caio mata o colega por ter perdido a aposta de R$ 10: motivo <b>fútil</b> (§ 2º, II). Já Rafael mata o vizinho porque ele estuprou sua filha, logo após saber do fato, dominado por violenta emoção: pode haver <b>homicídio privilegiado</b> (§ 1º), com redução de pena.')) +
 pega('<ul><li><b>Motivo fútil</b> (desproporcional, banal) ≠ <b>motivo torpe</b> (repugnante, como matar por herança ou por dinheiro).</li><li>O feminicídio <b>não é mais</b> qualificadora do homicídio desde a Lei nº 14.994/2024: é o crime do <b>art. 121-A</b>.</li><li>O homicídio culposo tem pena de <b>detenção</b>; o doloso, de <b>reclusão</b>.</li></ul>'))

add(H(1,'Feminicídio e <span class="hl">vicaricídio</span>','Crimes autônomos criados em 2024 e 2026.', "A02") +
 lei(cp("Art. 121-A, caput (Lei nº 14.994/2024)"),'<p>Feminicídio<br>Art. 121-A. Matar mulher por razões da condição do sexo feminino:<br>Pena - reclusão, de 20 (vinte) a 40 (quarenta) anos.</p>') +
 table(["Ponto","Regra (art. 121-A)"],[
  ["Razões da condição do sexo feminino (§ 1º)","Quando o crime envolve <b>violência doméstica e familiar</b> ou <b>menosprezo ou discriminação à condição de mulher</b>"],
  ["Aumento de 1/3 até a metade (§ 2º)","Durante a gestação ou nos 3 meses após o parto (ou se a vítima for mãe ou responsável por criança, adolescente ou pessoa com deficiência); vítima menor de 14, maior de 60, com deficiência ou doença degenerativa; na presença de descendente ou ascendente; em descumprimento de medida protetiva; com as circunstâncias do art. 121, § 2º, III, IV ou VIII"],
  ["Coautores (§ 3º)","As circunstâncias pessoais do § 1º se comunicam aos coautores e partícipes"]],["30%",None]) +
 lei(cp("Art. 121-B (Lei nº 15.384/2026), em síntese"),'<p>Vicaricídio: matar descendente, ascendente, dependente, enteado ou pessoa sob guarda ou responsabilidade da mulher, com o fim de lhe causar sofrimento, punição ou controle, em contexto de violência doméstica e familiar. Pena: reclusão, de 20 a 40 anos.</p>') +
 memo('Feminicídio: <strong>art. 121-A</strong>, crime <strong>autônomo</strong>, pena de <strong>20 a 40 anos</strong>. Vicaricídio: <strong>art. 121-B</strong>, mesma pena, para quem mata pessoa próxima da mulher para atingi-la.'))

add(pratica_title() +
 flow([("person",["MULHER","vítima"]),("home2",["VIOLÊNCIA DOMÉSTICA","ou menosprezo à","condição de mulher"]),("gavel",["ART. 121-A","feminicídio","20 a 40 anos"])],
      "Feminicídio: a morte da mulher por razões da condição do sexo feminino.", colors=colors("b","r","n")) +
 ex(p('Marcos mata a ex-companheira, contra quem havia medida protetiva de urgência, na frente do filho do casal. Ele responde por <b>feminicídio</b> (art. 121-A), com aumento de 1/3 até a metade por duas razões: crime na presença de descendente e em descumprimento de medida protetiva. Se uma mulher é morta num assalto, sem relação com a condição de mulher, o crime <b>não</b> é feminicídio.')) +
 pega('<ul><li>Não basta a vítima ser mulher: é preciso a morte <b>por razões da condição do sexo feminino</b> (violência doméstica e familiar ou menosprezo e discriminação).</li><li>Questões antigas tratam o feminicídio como <b>qualificadora</b> do art. 121, § 2º, VI. Esse inciso foi <b>revogado</b> em 2024.</li><li>A pena do feminicídio (20 a 40 anos) é <b>maior</b> que a do homicídio qualificado (12 a 30 anos).</li></ul>') +
 kw(["art. 121-A","razões da condição do sexo feminino","violência doméstica e familiar","20 a 40 anos","art. 121-B · vicaricídio","Lei nº 14.994/2024"]))

add(H(1,'Suicídio, infanticídio e <span class="hl">aborto</span>','Arts. 122 a 128.', "A03") +
 table(["Crime","Conduta (em síntese)","Pena"],[
  ["Induzimento, instigação ou auxílio a suicídio ou automutilação (art. 122)","Induzir ou instigar alguém a suicidar-se ou a praticar automutilação, ou prestar-lhe auxílio material","Reclusão, 6 meses a 2 anos; 1 a 3 anos se resulta lesão grave ou gravíssima; 2 a 6 anos se resulta morte"],
  ["Infanticídio (art. 123)","Matar, sob a influência do estado puerperal, o próprio filho, durante o parto ou logo após","Detenção, 2 a 6 anos"],
  ["Aborto pela gestante ou com seu consentimento (art. 124)","Provocar aborto em si mesma ou consentir que outrem o provoque","Detenção, 1 a 3 anos"],
  ["Aborto por terceiro sem consentimento (art. 125)","Provocar aborto sem o consentimento da gestante","Reclusão, 3 a 10 anos"],
  ["Aborto por terceiro com consentimento (art. 126)","Provocar aborto com o consentimento da gestante","Reclusão, 1 a 4 anos"]],["30%",None,"28%"]) +
 lei(cp("Art. 128"),'<p>Art. 128 - Não se pune o aborto praticado por médico:<br>I - se não há outro meio de salvar a vida da gestante;<br>II - se a gravidez resulta de estupro e o aborto é precedido de consentimento da gestante ou, quando incapaz, de seu representante legal.</p>') +
 memo('Infanticídio: <strong>a própria mãe</strong>, sob <strong>estado puerperal</strong>, <strong>durante ou logo após o parto</strong>. Aborto legal (art. 128): <strong>por médico</strong>, para salvar a vida da gestante ou em gravidez resultante de estupro, com consentimento.'))

add(pratica_title("Homicídio x infanticídio x aborto") +
 table(["","ABORTO","INFANTICÍDIO","HOMICÍDIO"],[["Vítima","Feto (vida intrauterina)","O próprio filho, durante ou logo após o parto","Pessoa já nascida"],["Autor","Gestante ou terceiro","Só a mãe, sob estado puerperal","Qualquer pessoa"],["Ponto-chave","Interrupção da gravidez","Influência do estado puerperal","Matar alguém"]],["16%",None,None,None]) +
 ex(p('Logo após o parto, ainda sob forte abalo físico e psíquico causado pelo estado puerperal, Joana mata o recém-nascido: <b>infanticídio</b>. Se a mesma conduta fosse praticada pelo pai da criança, sem participação da mãe, o crime seria <b>homicídio</b>. O STF também decidiu que a interrupção da gravidez de feto anencéfalo não é crime (ADPF 54).')) +
 pega('<ul><li>Infanticídio exige o <b>estado puerperal</b>; sem ele, a mãe responde por <b>homicídio</b>.</li><li>O aborto do art. 128 deve ser praticado por <b>médico</b>. No caso de estupro, exige-se o <b>consentimento</b> da gestante (ou do representante legal, se incapaz).</li><li>No art. 122, se a vítima é menor de 14 anos ou não tem discernimento, a lei manda o agente responder por <b>lesão gravíssima</b> ou <b>homicídio</b>, conforme o resultado (§§ 6º e 7º).</li></ul>'))

treino(1, [
 ("A pena do homicídio simples é de reclusão, de seis a vinte anos.","C","Art. 121, caput."),
 ("O feminicídio continua sendo uma qualificadora do homicídio (art. 121, § 2º, VI).","E","O inciso VI foi revogado; o feminicídio é crime autônomo (art. 121-A)."),
 ("A pena do feminicídio é de reclusão, de 20 a 40 anos.","C","Art. 121-A (Lei nº 14.994/2024)."),
 ("No homicídio culposo, o juiz pode deixar de aplicar a pena se as consequências da infração atingirem o agente de forma tão grave que a pena se torne desnecessária.","C","Perdão judicial (art. 121, § 5º)."),
 ("O infanticídio pode ser praticado pelo pai da criança, sob a influência do estado puerperal.","E","Só a mãe, sob a influência do estado puerperal."),
 ("Não se pune o aborto praticado por médico se a gravidez resulta de estupro e há consentimento da gestante.","C","Art. 128, II.")])

# ================================================================ UNIDADE 2
opener("02","UNIDADE 2","Lesões corporais",["Lesão corporal: leve, grave, gravíssima e seguida de morte","Lesão em violência doméstica e contra a mulher"],"U2")

add(H(2,'Lesão <span class="hl">corporal</span> (art. 129)','A gravidade é definida pelo resultado.', "A04") +
 lei(cp("Art. 129, caput"),'<p>Art. 129. Ofender a integridade corporal ou a saúde de outrem:<br>Pena - detenção, de três meses a um ano.</p>') +
 table(["Espécie","Resultados (em síntese)","Pena"],[
  ["Leve (caput)","Ofensa à integridade corporal ou à saúde, sem os resultados abaixo","Detenção, 3 meses a 1 ano"],
  ["Grave (§ 1º)","Incapacidade para as ocupações habituais por <b>mais de 30 dias</b>; perigo de vida; debilidade permanente de membro, sentido ou função; aceleração de parto","Reclusão, 1 a 5 anos"],
  ["Gravíssima (§ 2º)","Incapacidade <b>permanente</b> para o trabalho; enfermidade incurável; <b>perda</b> ou inutilização de membro, sentido ou função; deformidade permanente; <b>aborto</b>","Reclusão, 2 a 8 anos"],
  ["Seguida de morte (§ 3º)","Resulta morte, e o agente não quis nem assumiu o risco de produzi-la (crime preterdoloso)","Reclusão, 4 a 12 anos"],
  ["Culposa (§ 6º)","Lesão causada por imprudência, negligência ou imperícia","Detenção, 2 meses a 1 ano"]],["20%",None,"22%"]) +
 memo('<strong>Debilidade</strong> permanente → grave. <strong>Perda</strong> ou inutilização → gravíssima. Aceleração de parto → grave. <strong>Aborto</strong> → gravíssima. Mais de <strong>30 dias</strong> de incapacidade → grave.'))

add(pratica_title() +
 flow([("person",["SOCO","no rosto"]),("search",["PERÍCIA","avalia o","resultado"]),("alert",["35 DIAS","sem trabalhar","→ grave (§ 1º)"]),("xmark",["PERDEU","A VISÃO de um olho","→ gravíssima (§ 2º)"])],
      "A mesma conduta pode gerar lesões de gravidades diferentes conforme o resultado.", colors=colors("n","b","o","r")) +
 ex(p('Numa briga, Pedro dá um soco em Lucas, que cai, bate a cabeça e morre. Pedro queria apenas machucar, não matar, nem assumiu o risco da morte: <b>lesão corporal seguida de morte</b> (§ 3º), um crime <b>preterdoloso</b> (dolo na lesão, culpa na morte). Se Pedro quisesse matar, seria homicídio.')) +
 pega('<ul><li><b>Debilidade</b> (enfraquecimento) permanente de membro é lesão <b>grave</b>; <b>perda</b> ou inutilização é <b>gravíssima</b>.</li><li>O aborto como resultado da lesão é lesão <b>gravíssima</b>; a aceleração do parto é lesão <b>grave</b>.</li><li>A lesão culposa tem pena de <b>detenção</b>, e o § 8º permite o <b>perdão judicial</b>, como no homicídio culposo.</li><li>A Lei nº 15.358/2026 incluiu os §§ 3º-A e 8º-A, com penas maiores quando a lesão é praticada por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia.</li></ul>'))

add(H(2,'Lesão em violência doméstica e <span class="hl">contra a mulher</span>','Os §§ 9º, 12 e 13 do art. 129.', "A05") +
 table(["Hipótese","Regra (texto vigente)","Pena / aumento"],[
  ["Violência doméstica (§ 9º)","Lesão contra ascendente, descendente, irmão, cônjuge ou companheiro, ou com quem conviva ou tenha convivido, ou prevalecendo-se de relações domésticas, de coabitação ou de hospitalidade (a redação atual do caput, dada pela Lei nº 15.455/2026, também alcança as relações com trabalhadores domésticos)","Reclusão, 2 a 5 anos"],
  ["Contra a mulher (§ 13)","Lesão contra a mulher, por razões da condição do sexo feminino, nos termos do § 1º do art. 121-A","Reclusão, 2 a 5 anos"],
  ["Agentes de segurança e do sistema de justiça; escola (§ 12)","Lesão dolosa contra esses agentes ou seus familiares, em razão da função, ou nas dependências de instituição de ensino (Lei nº 15.159/2025)","Aumento de 1/3 a 2/3 (e de 2/3 ao dobro em situações específicas na escola)"],
  ["Pessoa com deficiência (§ 11)","Lesão do § 9º contra pessoa com deficiência","Aumento de 1/3"]],["24%",None,"24%"]) +
 traduz(p('A lei pune com mais rigor a lesão praticada <strong>dentro de casa</strong>, contra familiares ou pessoas com quem se convive, e a lesão contra a <strong>mulher por razões da condição de mulher</strong>. Nesses casos, mesmo a lesão leve deixa de ter pena de detenção de 3 meses a 1 ano e passa a ter <strong>reclusão de 2 a 5 anos</strong> (redação da Lei nº 14.994/2024).'),"profa") +
 memo('§ 9º (violência doméstica) e § 13 (contra a mulher): <strong>reclusão de 2 a 5 anos</strong>. Agentes de segurança em razão da função: <strong>aumento de 1/3 a 2/3</strong> (§ 12).'))

treino(2, [
 ("A lesão corporal que resulta incapacidade para as ocupações habituais por mais de trinta dias é gravíssima.","E","É grave (§ 1º, I)."),
 ("A lesão que resulta perda ou inutilização de membro, sentido ou função é gravíssima.","C","§ 2º, III."),
 ("A lesão corporal seguida de morte é exemplo de crime preterdoloso.","C","Dolo na lesão e culpa na morte (§ 3º)."),
 ("A aceleração do parto é resultado que qualifica a lesão como gravíssima.","E","É lesão grave (§ 1º, IV); o aborto é que torna a lesão gravíssima."),
 ("A lesão praticada contra a mulher por razões da condição do sexo feminino tem pena de reclusão, de 2 a 5 anos.","C","§ 13 (Lei nº 14.994/2024)."),
 ("A lesão corporal leve tem pena de reclusão, de um a cinco anos.","E","Detenção, de 3 meses a 1 ano.")])

# ================================================================ UNIDADE 3
opener("03","UNIDADE 3","Crimes contra a honra",["Calúnia, difamação e injúria","Aumentos de pena, exclusão, retratação e ação penal"],"U3")

honra = scene3([("CALÚNIA",C['red'],C['redsoft'],"prof",["“O João furtou","o caixa da loja.”","(e é mentira)"],"fato CRIMINOSO falso"),
 ("DIFAMAÇÃO",C['golddeep'],C['goldsoft'],"profa",["“A Ana chega","bêbada ao trabalho","toda segunda.”"],"fato OFENSIVO à reputação"),
 ("INJÚRIA",C['navy'],'#e6e7ea',"prof",["“Você é um","incompetente","e um idiota!”"],"QUALIDADE negativa")], "Situação ilustrada: três frases, três crimes diferentes.")
add(H(3,'Calúnia, difamação e <span class="hl">injúria</span>','A diferença está no que se atribui à vítima.', "A06") + honra +
 table(["","CALÚNIA (art. 138)","DIFAMAÇÃO (art. 139)","INJÚRIA (art. 140)"],[
  ["Texto","Caluniar alguém, imputando-lhe <b>falsamente fato definido como crime</b>","Difamar alguém, imputando-lhe <b>fato ofensivo à sua reputação</b>","Injuriar alguém, ofendendo-lhe a <b>dignidade ou o decoro</b>"],
  ["O que se atribui","Um <b>fato</b> que é <b>crime</b>, e falso","Um <b>fato</b> desonroso (verdadeiro ou falso)","Uma <b>qualidade</b> negativa (xingamento)"],
  ["Honra atingida","Objetiva (reputação)","Objetiva (reputação)","Subjetiva (autoestima)"],
  ["Exceção da verdade","Em regra, admitida","Só se o ofendido é funcionário público e a ofensa se refere às suas funções","Não admitida"],
  ["Pena","Detenção, 6 meses a 2 anos, e multa","Detenção, 3 meses a 1 ano, e multa","Detenção, 1 a 6 meses, ou multa"]],["16%",None,None,None]))

add(pratica_title("Injúria qualificada e outros pontos") +
 lei(cp("Art. 140, § 3º (redação da Lei nº 14.532/2023)"),'<p>§ 3º Se a injúria consiste na utilização de elementos referentes a religião ou à condição de pessoa idosa ou com deficiência:<br>Pena - reclusão, de 1 (um) a 3 (três) anos, e multa.</p>') +
 novo('Desde a Lei nº 14.532/2023, o § 3º do art. 140 <strong>não menciona mais raça, cor ou etnia</strong>. A injúria por esses motivos passou a ser tratada na <strong>Lei do Racismo (Lei nº 7.716/1989)</strong>, com pena mais grave. Em provas recentes, “injúria racial” é crime da Lei nº 7.716/1989, e não do art. 140, § 3º, do CP.', "Atualização: injúria racial") +
 ex(p('Num grupo de mensagens, Paulo escreve que o vizinho “desviou dinheiro do condomínio”, sabendo que é mentira: <b>calúnia</b> (apropriação indébita é crime). Se escrevesse que o vizinho “não paga as contas e vive de favores”: <b>difamação</b>. Se chamasse o vizinho de “vagabundo”: <b>injúria</b>.')) +
 pega('<ul><li>Calúnia e difamação atribuem <b>fatos</b>; a injúria atribui <b>qualidades</b>.</li><li>Na calúnia, o fato precisa ser <b>crime</b> e <b>falso</b>. Atribuir falsamente uma <b>contravenção</b> não é calúnia (pode ser difamação).</li><li>É punível a calúnia contra os <b>mortos</b> (art. 138, § 2º).</li><li>Quem, sabendo falsa a imputação, a <b>propala ou divulga</b> também responde por calúnia (art. 138, § 1º).</li></ul>'))

add(H(3,'Aumentos, exclusão, retratação e <span class="hl">ação penal</span>','Arts. 141 a 145.', "A07") +
 table(["Regra","Conteúdo (em síntese)"],[
  ["Aumento de 1/3 (art. 141)","Contra o Presidente da República ou chefe de governo estrangeiro; contra funcionário público em razão das funções, ou contra os Presidentes do Senado, da Câmara ou do STF; na presença de várias pessoas ou por meio que facilite a divulgação; contra criança, adolescente, pessoa maior de 60 anos ou com deficiência (exceto no art. 140, § 3º)"],
  ["Pena em dobro (§ 1º)","Crime cometido mediante paga ou promessa de recompensa"],
  ["Pena em triplo (§ 2º)","Crime cometido ou divulgado em redes sociais da internet"],
  ["Pena em dobro (§ 3º, Lei nº 14.994/2024)","Crime contra a mulher por razões da condição do sexo feminino"],
  ["Exclusão do crime (art. 142)","Não há injúria ou difamação punível na ofensa irrogada em juízo pela parte ou procurador; na crítica literária, artística ou científica (salvo intenção de ofender); no conceito desfavorável emitido por funcionário público no cumprimento do dever"],
  ["Retratação (art. 143)","O querelado que, antes da sentença, se retrata cabalmente da <b>calúnia ou da difamação</b> fica isento de pena"],
  ["Ação penal (art. 145)","Em regra, mediante <b>queixa</b> (ação privada). Exceções: lesão corporal resultante da injúria real; requisição do Ministro da Justiça (art. 141, I); representação do ofendido (art. 141, II, e art. 140, § 3º)"]],["28%",None]) +
 memo('Redes sociais: pena em <strong>triplo</strong>. Paga ou promessa: em <strong>dobro</strong>. Contra a mulher por razões da condição do sexo feminino: em <strong>dobro</strong>. Retratação: só na <strong>calúnia e difamação</strong>. Ação penal: em regra, <strong>queixa</strong>.') +
 pega('<ul><li>A retratação <b>não</b> se aplica à <b>injúria</b>.</li><li>A ofensa contra funcionário público em razão das funções tem ação penal mediante <b>representação</b>, e não queixa.</li></ul>'))

treino(3, [
 ("Imputar falsamente a alguém fato definido como crime configura difamação.","E","É calúnia (art. 138)."),
 ("Na injúria, o agente atribui à vítima uma qualidade negativa, ofendendo sua dignidade ou decoro.","C","Art. 140."),
 ("É punível a calúnia contra os mortos.","C","Art. 138, § 2º."),
 ("A retratação antes da sentença isenta de pena o autor de calúnia, difamação ou injúria.","E","Só calúnia e difamação (art. 143)."),
 ("Se o crime contra a honra é cometido ou divulgado em redes sociais da internet, a pena é aplicada em triplo.","C","Art. 141, § 2º."),
 ("O art. 140, § 3º, do CP continua prevendo a injúria em razão de raça, cor ou etnia.","E","Após a Lei nº 14.532/2023, o § 3º trata de religião e da condição de pessoa idosa ou com deficiência.")])

# ================================================================ UNIDADE 4
opener("04","UNIDADE 4","Crimes contra a liberdade individual",["Constrangimento ilegal e ameaça","Intimidação sistemática, perseguição e violência psicológica","Sequestro, cárcere privado e redução à condição análoga à de escravo","Violação de domicílio"],"U4")

add(H(4,'Constrangimento ilegal e <span class="hl">ameaça</span>','Arts. 146 e 147.', "A08") +
 lei(cp("Art. 146, caput, e art. 147, caput"),'<p>Art. 146 - Constranger alguém, mediante violência ou grave ameaça, ou depois de lhe haver reduzido, por qualquer outro meio, a capacidade de resistência, a não fazer o que a lei permite, ou a fazer o que ela não manda:<br>Pena - detenção, de três meses a um ano, ou multa.<br>Art. 147 - Ameaçar alguém, por palavra, escrito ou gesto, ou qualquer outro meio simbólico, de causar-lhe mal injusto e grave:<br>Pena - detenção, de um a seis meses, ou multa.</p>') +
 table(["","CONSTRANGIMENTO ILEGAL","AMEAÇA"],[["Objetivo do agente","Obrigar a vítima a <b>fazer ou deixar de fazer</b> algo","Apenas <b>intimidar</b>, prometendo mal injusto e grave"],["Exemplo","“Saia desta praça agora ou apanha.”","“Um dia eu te pego.”"],["Pena","Detenção, 3 meses a 1 ano, ou multa","Detenção, 1 a 6 meses, ou multa"]],["22%",None,None]) +
 lei(cp("Art. 147, §§ 1º e 2º (Lei nº 14.994/2024), em síntese"),'<p>§ 1º: se a ameaça é contra a mulher por razões da condição do sexo feminino, aplica-se a pena em dobro. § 2º: somente se procede mediante representação, exceto na hipótese do § 1º.</p>') +
 memo('Ameaça: em regra, ação penal mediante <strong>representação</strong>. Contra a mulher por razões da condição do sexo feminino: pena em <strong>dobro</strong> e ação <strong>sem</strong> necessidade de representação.'))
atencao(ex(p('Ao ser cobrado por uma dívida, Mário diz ao credor: “Se você vier aqui de novo, eu quebro seu carro e você vai se arrepender.” Há <b>ameaça</b> (promessa de mal injusto e grave). Se Mário, com uma barra de ferro na mão, obrigasse o credor a assinar um recibo de quitação, haveria <b>constrangimento ilegal</b>, ou até <b>extorsão</b>, se o objetivo fosse vantagem econômica.')) +
 pega('<ul><li>No constrangimento ilegal, há <b>imposição de conduta</b>; na ameaça, basta a <b>promessa de mal</b>.</li><li>Não há constrangimento ilegal na intervenção médica sem consentimento em caso de iminente perigo de vida, nem na coação para impedir suicídio (art. 146, § 3º).</li><li>A Lei nº 15.358/2026 criou o art. 147-C, que pune a ameaça praticada no contexto da atuação de organizações criminosas.</li></ul>'), ["mal injusto e grave","impor conduta","representação","pena em dobro (mulher)","art. 147-C"])

add(H(4,'Bullying, perseguição e <span class="hl">violência psicológica</span>','Crimes incluídos a partir de 2021.', "A09") +
 table(["Crime","Conduta (em síntese)","Pena"],[
  ["Intimidação sistemática (bullying) · art. 146-A (Lei nº 14.811/2024)","Intimidar sistematicamente, de modo intencional e repetitivo, uma ou mais pessoas, por violência física ou psicológica, humilhação, discriminação ou ações verbais, morais, sociais ou outras, sem motivação evidente","Multa, se não constituir crime mais grave"],
  ["Intimidação sistemática virtual (cyberbullying) · art. 146-A, parágrafo único","A mesma conduta realizada por rede de computadores, redes sociais, aplicativos, jogos on-line ou outros meios digitais, ou transmitida em tempo real","Reclusão, 2 a 4 anos, e multa, se não constituir crime mais grave"],
  ["Perseguição (stalking) · art. 147-A (Lei nº 14.132/2021)","Perseguir alguém, reiteradamente e por qualquer meio, ameaçando-lhe a integridade física ou psicológica, restringindo sua capacidade de locomoção ou perturbando sua esfera de liberdade ou privacidade","Reclusão, 6 meses a 2 anos, e multa (aumento de metade em situações do § 1º; ação mediante representação)"],
  ["Violência psicológica contra a mulher · art. 147-B (Lei nº 14.188/2021)","Causar dano emocional à mulher que a prejudique ou que vise controlar suas ações, comportamentos, crenças e decisões, por ameaça, humilhação, manipulação, isolamento, chantagem etc.","Reclusão, 6 meses a 2 anos, e multa, se não constituir crime mais grave; aumento de metade se usada inteligência artificial ou tecnologia que altere imagem ou som da vítima (Lei nº 15.123/2025)"]],["28%",None,"30%"]) +
 memo('Bullying presencial: <strong>multa</strong>. Cyberbullying: <strong>reclusão de 2 a 4 anos</strong>. Perseguição: <strong>reiteração</strong> + ação mediante <strong>representação</strong>. Violência psicológica: vítima <strong>mulher</strong>.'))

atencao(ex(p('Um ex-namorado passa semanas seguindo a vítima, aparecendo na porta do trabalho e mandando dezenas de mensagens por perfis falsos, deixando-a com medo de sair de casa: <b>perseguição</b> (art. 147-A). Um grupo de alunos humilha repetidamente um colega num jogo on-line, sem motivo aparente: <b>intimidação sistemática virtual</b> (art. 146-A, parágrafo único).')) +
 pega('<ul><li>Perseguição exige <b>reiteração</b> (“reiteradamente”): um único episódio não configura o crime.</li><li>O bullying presencial tem pena apenas de <b>multa</b>; o virtual, de <b>reclusão</b>. A diferença de pena é grande e costuma ser cobrada.</li><li>Na violência psicológica do art. 147-B, a vítima é <b>mulher</b>; nos arts. 146-A e 147-A, qualquer pessoa.</li></ul>'),
 ["intimidação sistemática","cyberbullying","reiteradamente","representação","dano emocional à mulher","inteligência artificial"])

add(H(4,'Sequestro, cárcere privado e <span class="hl">trabalho escravo</span>','Arts. 148 e 149.', "A10") +
 lei(cp("Art. 148, caput"),'<p>Art. 148 - Privar alguém de sua liberdade, mediante sequestro ou cárcere privado:<br>Pena - reclusão, de um a três anos.</p>') +
 table(["Forma","Hipóteses (em síntese)","Pena"],[
  ["Qualificada (§ 1º)","Vítima ascendente, descendente, cônjuge ou companheiro do agente, ou maior de 60 anos; internação fraudulenta em casa de saúde ou hospital; privação por mais de 15 dias; vítima menor de 18 anos; fins libidinosos","Reclusão, 2 a 5 anos"],
  ["Grave sofrimento (§ 2º)","Se resulta à vítima, em razão de maus-tratos ou da natureza da detenção, grave sofrimento físico ou moral","Reclusão, 2 a 8 anos"],
  ["Crime organizado (§ 3º, Lei nº 15.358/2026)","Praticado por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada","Reclusão, 12 a 20 anos"]],["22%",None,"20%"]) +
 lei(cp("Art. 149, em síntese"),'<p>Redução a condição análoga à de escravo: submeter alguém a trabalhos forçados ou a jornada exaustiva, a condições degradantes de trabalho, ou restringir sua locomoção em razão de dívida com o empregador ou preposto. Pena: reclusão, de dois a oito anos, e multa, além da pena correspondente à violência.</p>') +
 memo('Sequestro: <strong>privar a liberdade</strong> (reclusão de 1 a 3 anos). Mais de <strong>15 dias</strong>, vítima <strong>menor de 18</strong> ou <strong>maior de 60</strong>: qualificado (2 a 5 anos).') +
 pega('<ul><li>Sequestro (art. 148) ≠ <b>extorsão mediante sequestro</b> (art. 159): nesta, o agente quer obter uma <b>vantagem</b> como condição ou preço do resgate.</li><li>O trabalho escravo não exige correntes: <b>jornada exaustiva</b> ou <b>condições degradantes</b> já configuram o crime.</li></ul>'))

add(H(4,'Violação de <span class="hl">domicílio</span>','Art. 150: a proteção penal da casa.', "A11") +
 lei(cp("Art. 150, caput"),'<p>Art. 150 - Entrar ou permanecer, clandestina ou astuciosamente, ou contra a vontade expressa ou tácita de quem de direito, em casa alheia ou em suas dependências:<br>Pena - detenção, de um a três meses, ou multa.</p>') +
 table(["Regra","Conteúdo (em síntese)"],[
  ["Qualificada (§ 1º)","Durante a noite, em lugar ermo, com violência ou arma, ou por duas ou mais pessoas: detenção, 6 meses a 2 anos, além da pena da violência"],
  ["Não é crime (§ 3º)","Entrar durante o dia, com as formalidades legais, para efetuar prisão ou outra diligência; entrar a qualquer hora quando algum crime está sendo praticado ou na iminência de o ser"],
  ["É “casa” (§ 4º)","Qualquer compartimento habitado; aposento ocupado de habitação coletiva; compartimento não aberto ao público onde alguém exerce profissão ou atividade"],
  ["Não é “casa” (§ 5º)","Hospedaria, estalagem ou habitação coletiva enquanto aberta (salvo o aposento ocupado); taverna, casa de jogo e similares"]],["24%",None]) +
 ex(p('Um ex-inquilino usa uma chave antiga para entrar no apartamento enquanto o novo morador viaja: <b>violação de domicílio</b>, praticada de forma clandestina. Um escritório de advocacia, na parte fechada ao público, também é “casa” para o Código Penal (§ 4º, III); a recepção aberta ao público, não.')) +
 memo('“Casa” é conceito <strong>amplo</strong>: inclui quarto de hotel ocupado e escritório fechado ao público. Combina com a inviolabilidade do art. 5º, XI, da CF.'))

treino(4, [
 ("Na ameaça, o agente promete à vítima mal injusto e grave por palavra, escrito, gesto ou qualquer outro meio simbólico.","C","Art. 147."),
 ("A ameaça contra a mulher por razões da condição do sexo feminino tem a pena aplicada em dobro.","C","Art. 147, § 1º (Lei nº 14.994/2024)."),
 ("A intimidação sistemática presencial (bullying) é punida com reclusão de 2 a 4 anos.","E","O bullying presencial é punido com multa; a pena de reclusão de 2 a 4 anos é da forma virtual."),
 ("O crime de perseguição exige que a conduta seja praticada reiteradamente.","C","Art. 147-A."),
 ("O sequestro é qualificado se a privação da liberdade dura mais de quinze dias.","C","Art. 148, § 1º, III."),
 ("O quarto de hotel ocupado pelo hóspede não é considerado casa para fins do art. 150.","E","Aposento ocupado de habitação coletiva é casa (§ 4º, II).")])

# ================================================================ UNIDADE 5
opener("05","UNIDADE 5","Crimes contra o patrimônio",["Furto","Roubo","Extorsão e extorsão mediante sequestro","Furto x roubo x extorsão","Dano e apropriação indébita","Estelionato","Receptação e imunidades"],"U5")

add(H(5,'<span class="hl">Furto</span> (art. 155)','Subtrair coisa alheia móvel, sem violência ou grave ameaça.', "A12") +
 lei(cp("Art. 155, caput (redação da Lei nº 15.397/2026)"),'<p>Art. 155 - Subtrair, para si ou para outrem, coisa alheia móvel:<br>Pena - reclusão, de 1 (um) a 6 (seis) anos, e multa.</p>') +
 novo('A <strong>Lei nº 15.397/2026</strong> elevou a pena do furto simples para <strong>reclusão de 1 a 6 anos</strong> e multa (antes era de 1 a 4 anos) e reorganizou várias formas qualificadas. Desconfie de materiais que ainda trazem a pena antiga.', "Atualização 2026") +
 table(["Forma","Hipóteses (em síntese)","Pena"],[
  ["Repouso noturno (§ 1º)","Furto praticado durante o repouso noturno","Aumento de metade"],
  ["Privilegiado (§ 2º)","Criminoso primário e coisa de pequeno valor","Juiz pode substituir reclusão por detenção, reduzir de 1/3 a 2/3 ou aplicar só multa"],
  ["Qualificado (§ 4º)","Destruição ou rompimento de obstáculo; abuso de confiança, fraude, escalada ou destreza; chave falsa; concurso de duas ou mais pessoas; contra bens que comprometam órgãos públicos ou serviços essenciais","Reclusão, 2 a 8 anos, e multa"],
  ["Explosivo (§ 4º-A)","Emprego de explosivo ou artefato análogo que cause perigo comum","Reclusão, 4 a 10 anos, e multa"],
  ["Fraude eletrônica (§ 4º-B)","Furto mediante fraude por dispositivo eletrônico ou informático","Reclusão, 4 a 10 anos, e multa"],
  ["Veículo (§ 5º)","Veículo automotor levado para outro Estado ou para o exterior","Reclusão, 4 a 10 anos, e multa"],
  ["Animais e eletrônicos (§ 6º)","Semovente doméstico de produção ou animal doméstico; <b>celular</b>, computador, tablet ou similar","Reclusão, 4 a 10 anos, e multa"],
  ["Explosivos e arma (§ 7º)","Subtração de substâncias explosivas ou acessórios; <b>arma de fogo</b>","Reclusão, 4 a 10 anos, e multa"]],["20%",None,"22%"]))

add(pratica_title() +
 flow([("phonecrack",["CELULAR","sobre a mesa","do bar"]),("person",["PEGA E SAI","sem violência","nem ameaça"]),("gavel",["FURTO","de celular","§ 6º: 4 a 10 anos"])],
      "Furto: a subtração acontece sem violência ou grave ameaça à pessoa.", colors=colors("b","n","r")) +
 ex(p('Enquanto a vítima conversa no bar, Pedro pega o celular dela da mesa e vai embora sem ser notado. Não houve violência nem grave ameaça: é <b>furto</b>, e, por se tratar de celular, incide o <b>§ 6º, II</b> (reclusão de 4 a 10 anos), incluído pela Lei nº 15.397/2026. Se Pedro tivesse pulado o muro de uma casa para furtar, haveria <b>escalada</b> (§ 4º, II).')) +
 pega('<ul><li>Energia elétrica e qualquer outra coisa com valor econômico equiparam-se a coisa móvel (§ 3º).</li><li>Furto privilegiado: criminoso <b>primário</b> + coisa de <b>pequeno valor</b>.</li><li>Furto não tem <b>violência ou grave ameaça à pessoa</b>; se tiver, é <b>roubo</b>. Violência contra a <b>coisa</b> (arrombar a porta) não transforma o furto em roubo: qualifica o furto (rompimento de obstáculo).</li><li>A Lei nº 15.517/2026 criou formas próprias para o furto de combustíveis (§§ 10 a 12).</li></ul>'))

add(H(5,'<span class="hl">Roubo</span> (art. 157)','Subtração com violência ou grave ameaça à pessoa.', "A13") +
 lei(cp("Art. 157, caput (redação da Lei nº 15.397/2026)"),'<p>Art. 157 - Subtrair coisa móvel alheia, para si ou para outrem, mediante grave ameaça ou violência a pessoa, ou depois de havê-la, por qualquer meio, reduzido à impossibilidade de resistência:<br>Pena - reclusão, de 6 (seis) a 10 (dez) anos, e multa.</p>') +
 table(["Forma","Hipóteses (em síntese)","Pena"],[
  ["Roubo impróprio (§ 1º)","Logo depois de subtraída a coisa, emprega violência ou grave ameaça para assegurar a impunidade do crime ou a detenção da coisa","A mesma do caput"],
  ["Aumento de 1/3 até metade (§ 2º)","Concurso de duas ou mais pessoas; vítima em serviço de transporte de valores; veículo levado a outro Estado ou ao exterior; restrição da liberdade da vítima; explosivos; <b>arma branca</b>; cabos e equipamentos de energia, telefonia ou dados; <b>celular</b> ou similar; <b>arma de fogo</b> (inciso X); combustíveis","+1/3 até a metade"],
  ["Aumento de 2/3 (§ 2º-A)","Violência ou ameaça exercida com emprego de <b>arma de fogo</b>; destruição de obstáculo com explosivo; resultados graves no roubo de combustíveis","+2/3"],
  ["Arma de uso restrito ou proibido (§ 2º-B)","Violência ou grave ameaça com arma de fogo de uso restrito ou proibido","Pena do caput em dobro"],
  ["Lesão grave (§ 3º, I)","Se da violência resulta lesão corporal grave","Reclusão, 7 a 18 anos, e multa"],
  ["Morte (§ 3º, II), o “latrocínio”","Se da violência resulta morte","Reclusão, 24 a 30 anos, e multa"]],["20%",None,"18%"]) +
 memo('Roubo: <strong>6 a 10 anos</strong> (Lei nº 15.397/2026). Roubo com resultado morte: <strong>24 a 30 anos</strong>. Arma <strong>branca</strong>: +1/3 até metade. Arma de <strong>fogo</strong>: +2/3. Arma de uso <strong>restrito ou proibido</strong>: dobro.'))

add(pratica_title("Roubo próprio x roubo impróprio") +
 flow([("mask2",["ROUBO PRÓPRIO","violência ou ameaça","ANTES ou DURANTE","a subtração"]),("phonecrack",["SUBTRAÇÃO"]),("mask2",["ROUBO IMPRÓPRIO","violência ou ameaça","LOGO DEPOIS, para","garantir a fuga ou a coisa"])],
      "O momento da violência define a espécie de roubo.", colors=colors("r","n","o")) +
 ex(p('Lucas pega escondido uma bolsa numa loja (até aqui, furto), mas, ao ser abordado pelo segurança na saída, dá um soco nele para fugir com a bolsa: <b>roubo impróprio</b> (§ 1º). Em outro caso, Rafael aponta uma faca para a vítima e exige o celular: <b>roubo próprio</b>, com o aumento da <b>arma branca</b> (§ 2º, VII) e o do <b>celular</b> (§ 2º, IX).')) +
 pega('<ul><li>“Latrocínio” é o nome doutrinário do roubo com resultado <b>morte</b> (§ 3º, II); a lei não usa esse termo. Pelo STF, há latrocínio quando o homicídio se consuma, ainda que o agente não realize a subtração (Súmula 610).</li><li>Violência contra a <b>coisa</b> não é roubo; o roubo exige violência ou grave ameaça à <b>pessoa</b>.</li><li>A Lei nº 15.358/2026 incluiu os §§ 4º e 5º: pena em triplo quando o roubo é praticado por integrante de organização criminosa ultraviolenta, e reclusão de 20 a 40 anos se resultar morte nesse contexto.</li></ul>'))

add(H(5,'Extorsão e extorsão mediante <span class="hl">sequestro</span>','Arts. 158 e 159.', "A14") +
 lei(cp("Art. 158, caput"),'<p>Art. 158 - Constranger alguém, mediante violência ou grave ameaça, e com o intuito de obter para si ou para outrem indevida vantagem econômica, a fazer, tolerar que se faça ou deixar de fazer alguma coisa:<br>Pena - reclusão, de quatro a dez anos, e multa.</p>') +
 table(["Forma","Hipóteses (em síntese)","Pena"],[
  ["Majorada (§ 1º)","Cometida por duas ou mais pessoas, ou com emprego de arma","+1/3 até metade"],
  ["Com restrição da liberdade (§ 3º), o “sequestro relâmpago”","Restrição da liberdade da vítima, condição necessária para obter a vantagem econômica","Reclusão, 6 a 12 anos, e multa (lesão grave ou morte: penas do art. 159, §§ 2º e 3º)"],
  ["Organização criminosa (§ 4º, Lei nº 15.358/2026)","Praticada por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia","Pena em triplo"],
  ["Extorsão mediante sequestro (art. 159)","Sequestrar pessoa com o fim de obter qualquer vantagem como condição ou preço do resgate","Reclusão, 8 a 15 anos (12 a 20 se dura mais de 24 h, vítima menor de 18 ou maior de 60, ou bando; 16 a 24 se lesão grave; 24 a 30 se morte)"]],["24%",None,"28%"]) +
 traduz(p('Na extorsão, o criminoso <strong>obriga a vítima a agir</strong>: fazer um PIX, assinar um documento, entregar uma senha. A <strong>colaboração da vítima</strong> é indispensável para o criminoso obter a vantagem. No “sequestro relâmpago”, a vítima tem a liberdade restringida, por exemplo levada a caixas eletrônicos, até fazer os saques.'),"profa") +
'')
atencao(ex(p('Dois criminosos abordam Júlia no estacionamento, colocam-na no carro e a levam a três caixas eletrônicos para sacar dinheiro, soltando-a em seguida: <b>extorsão com restrição da liberdade</b> (“sequestro relâmpago”, art. 158, § 3º). Se, em vez disso, mantivessem Júlia em cativeiro e exigissem da família um resgate, o crime seria <b>extorsão mediante sequestro</b> (art. 159).')) +
 memo('Extorsão: vítima <strong>faz, tolera ou deixa de fazer</strong> algo, com fim de <strong>vantagem econômica</strong>. Delação no art. 159: o concorrente que denuncia e facilita a libertação tem a pena reduzida de <strong>1 a 2/3</strong> (§ 4º).'), ["fazer, tolerar ou deixar de fazer","vantagem econômica","sequestro relâmpago (§ 3º)","extorsão mediante sequestro","delação premiada (§ 4º)"])

fre = scene3([("FURTO",C['blue'],C['sky'],"prof",["(pega o celular","da mesa, escondido)"],"sem violência ou ameaça"),
 ("ROUBO",C['red'],C['redsoft'],"profa",["“Passa o celular","agora!” (com faca)"],"o agente TOMA a coisa"),
 ("EXTORSÃO",C['golddeep'],C['goldsoft'],"prof",["“Faz um PIX de","R$ 2 mil ou eu","solto as fotos.”"],"a VÍTIMA faz o ato")], "Situação ilustrada: três condutas patrimoniais que a prova costuma misturar.")
add(H(5,'Furto x roubo x <span class="hl">extorsão</span>','A comparação mais cobrada dos crimes patrimoniais.', "A15") + fre +
 table(["","FURTO (155)","ROUBO (157)","EXTORSÃO (158)"],[
  ["Violência ou grave ameaça à pessoa","Não","Sim","Sim"],
  ["Quem realiza o ato final","O agente subtrai","O agente subtrai (toma a coisa)","A <b>vítima</b> faz, tolera ou deixa de fazer algo"],
  ["Colaboração da vítima","Não há","Dispensável","<b>Indispensável</b>"],
  ["Pena base","Reclusão, 1 a 6 anos, e multa","Reclusão, 6 a 10 anos, e multa","Reclusão, 4 a 10 anos, e multa"]],["24%",None,None,None]) +
 pega('<ul><li>Se o criminoso <b>poderia</b> tomar a coisa sozinho (ex.: arranca a bolsa sob ameaça), é <b>roubo</b>. Se ele <b>depende</b> da ação da vítima (ex.: senha bancária, transferência), é <b>extorsão</b>.</li><li>Extorsão mediante sequestro (art. 159) ≠ sequestro relâmpago (art. 158, § 3º): no primeiro, a vítima é privada da liberdade como condição ou preço do resgate; no segundo, a restrição da liberdade é o meio para obter a vantagem da própria vítima.</li></ul>'))

add(H(5,'Dano e <span class="hl">apropriação indébita</span>','Arts. 163 e 168.', "A16") +
 lei(cp("Art. 163, caput, e art. 168, caput"),'<p>Art. 163 - Destruir, inutilizar ou deteriorar coisa alheia:<br>Pena - detenção, de um a seis meses, ou multa.<br>Art. 168 - Apropriar-se de coisa alheia móvel, de que tem a posse ou a detenção:<br>Pena - reclusão, de um a quatro anos, e multa.</p>') +
 table(["Dano qualificado (art. 163, parágrafo único)","Pena"],[["Com violência à pessoa ou grave ameaça; com substância inflamável ou explosiva (se não for crime mais grave); contra o patrimônio da União, Estado, DF, Município, autarquia, fundação pública, empresa pública, sociedade de economia mista ou concessionária de serviços públicos; por motivo egoísta ou com prejuízo considerável para a vítima","Detenção, 6 meses a 3 anos, e multa, além da pena da violência"]],[None,"28%"],rh=False) +
 ex(p('Um torcedor quebra os vidros de um ônibus da empresa concessionária do transporte municipal: <b>dano qualificado</b> (patrimônio de concessionária de serviço público). Já Carla recebe da empresa um notebook para trabalhar em casa e, ao ser demitida, decide ficar com ele: <b>apropriação indébita</b>, com aumento de 1/3 por ter recebido a coisa em razão de emprego (art. 168, § 1º).')) +
 pega('<ul><li>No dano não há intenção de <b>ficar</b> com a coisa: o objetivo é <b>destruir, inutilizar ou deteriorar</b>.</li><li>Na apropriação indébita, o agente já tem a <b>posse ou detenção lícita</b> e só depois decide se apropriar (dolo posterior). No estelionato, a fraude vem <b>antes</b> e é ela que faz a vítima entregar a coisa.</li><li>No dano por motivo egoísta ou com prejuízo considerável, a ação penal é mediante <b>queixa</b> (art. 167).</li></ul>'))

add(H(5,'<span class="hl">Estelionato</span> (art. 171)','Obter vantagem ilícita por meio de fraude.', "A17") +
 lei(cp("Art. 171, caput (redação da Lei nº 15.397/2026)"),'<p>Art. 171 - Obter, para si ou para outrem, vantagem ilícita, em prejuízo alheio, induzindo ou mantendo alguém em erro, mediante artifício, ardil, ou qualquer outro meio fraudulento:<br>Pena - reclusão, de 1 (um) a 5 (cinco) anos, e multa.</p>') +
 table(["Regra","Conteúdo (em síntese)"],[
  ["Fraude eletrônica (§ 2º-A)","Fraude com informações fornecidas pela vítima ou por terceiro induzido a erro por redes sociais, contatos telefônicos, e-mail fraudulento ou meio semelhante: reclusão, 4 a 8 anos, e multa"],
  ["Servidor no exterior (§ 2º-B)","Aumento de 1/3 a 2/3"],
  ["Contra idoso ou vulnerável (§ 4º)","Aumento de 1/3 ao dobro"],
  ["“Conta laranja” (§ 2º, VII, Lei nº 15.397/2026)","Nas mesmas penas incorre quem cede conta para a prática de fraudes"],
  ["Representação (antigo § 5º)","<b>Revogado</b> pela Lei nº 15.397/2026: deixou de existir a regra especial que exigia, em regra, representação da vítima"]],["28%",None]) +
 traduz(p('O estelionatário não usa força: usa a <strong>enganação</strong>. Ele cria uma mentira (o “artifício” ou “ardil”) que faz a vítima <strong>entregar voluntariamente</strong> a vantagem, como o falso funcionário do banco que pede uma transferência ou o falso anúncio de aluguel por temporada.')) +
 memo('Estelionato: <strong>fraude</strong> → vítima em <strong>erro</strong> → <strong>entrega</strong> a vantagem. Fraude eletrônica: <strong>4 a 8 anos</strong>. O § 5º (representação) foi <strong>revogado</strong> em 2026.'))

atencao(table(["","FURTO MEDIANTE FRAUDE (155, § 4º, II)","ESTELIONATO (171)"],[["Papel da fraude","Distrai a vítima para o agente <b>subtrair</b>","Engana a vítima para que ela <b>entregue</b>"],["Vontade da vítima","Não entrega nada","Entrega voluntariamente, porque está em erro"],["Exemplo","Falso técnico distrai o morador e leva o celular","Golpe do falso leilão: a vítima paga por um carro que não existe"]],["22%",None,None]) +
 ex(p('Um golpista se passa pela filha da vítima num aplicativo de mensagens, diz que trocou de número e pede um PIX urgente: <b>fraude eletrônica</b> (art. 171, § 2º-A), com aumento se a vítima for idosa (§ 4º). Quem empresta a própria conta bancária para receber esse dinheiro incorre nas mesmas penas (§ 2º, VII).')) +
 pega('<ul><li>Na dúvida entre furto mediante fraude e estelionato, pergunte: a vítima <b>entregou</b> a coisa (estelionato) ou o agente a <b>tirou</b> (furto)?</li><li>Questões anteriores a 2026 afirmam que o estelionato exige representação da vítima, em regra (antigo § 5º). Esse parágrafo foi <b>revogado</b> pela Lei nº 15.397/2026.</li></ul>'),
 ["artifício, ardil ou meio fraudulento","vítima em erro","fraude eletrônica","conta laranja","§ 5º revogado"])

add(H(5,'Receptação e <span class="hl">imunidades</span>','Art. 180 e arts. 181 a 183.', "A18") +
 lei(cp("Art. 180, caput (redação da Lei nº 15.397/2026)"),'<p>Art. 180 - Adquirir, receber, transportar, conduzir ou ocultar, em proveito próprio ou alheio, coisa que sabe ser produto de crime, ou influir para que terceiro, de boa-fé, a adquira, receba ou oculte:<br>Pena - reclusão, de 2 (dois) a 6 (seis) anos, e multa.</p>') +
 table(["Forma","Conteúdo (em síntese)","Pena"],[["Qualificada (§ 1º)","No exercício de atividade comercial ou industrial, coisa que <b>deve saber</b> ser produto de crime","Reclusão, 3 a 8 anos, e multa"],["“Culposa” (§ 3º)","Coisa que, pela natureza, desproporção entre valor e preço ou condição de quem oferece, <b>deve presumir-se</b> obtida por meio criminoso","Detenção, 1 mês a 1 ano, ou multa, ou ambas"],["Bens públicos (§ 6º) e cabos (§ 7º)","Bens do patrimônio público; cabos e equipamentos de energia, telefonia, dados ou ferroviários","Pena em dobro"]],["22%",None,"24%"]) +
 table(["Imunidades nos crimes patrimoniais",""],[["Isenção de pena (art. 181)","Crime contra cônjuge, na constância da sociedade conjugal, ou contra ascendente ou descendente"],["Representação (art. 182)","Contra cônjuge separado judicialmente, irmão, ou tio ou sobrinho com quem o agente coabita"],["Não se aplicam (art. 183)","Roubo, extorsão e crimes com grave ameaça ou violência à pessoa; ao estranho que participa do crime; vítima com 60 anos ou mais"]],["30%",None]) +
 memo('Receptação: <strong>sabe</strong> (caput, 2 a 6) · <strong>deve saber</strong> no comércio (§ 1º, 3 a 8) · <strong>deve presumir</strong> (§ 3º, culposa). Imunidade do art. 181 <strong>não vale</strong> para roubo, extorsão, violência ou vítima idosa.'))

treino(5, [
 ("A pena do furto simples é de reclusão, de 1 a 4 anos, e multa.","E","Desde a Lei nº 15.397/2026, é de 1 a 6 anos."),
 ("O furto de celular passou a ter pena de reclusão de 4 a 10 anos, e multa.","C","Art. 155, § 6º, II (Lei nº 15.397/2026)."),
 ("No roubo impróprio, a violência ou grave ameaça é empregada logo depois da subtração, para assegurar a impunidade ou a detenção da coisa.","C","Art. 157, § 1º."),
 ("Se da violência do roubo resulta morte, a pena é de reclusão de 24 a 30 anos, e multa.","C","Art. 157, § 3º, II (Lei nº 15.397/2026)."),
 ("Na extorsão, a colaboração da vítima é dispensável para a obtenção da vantagem.","E","É indispensável: a vítima faz, tolera ou deixa de fazer algo."),
 ("O estelionato continua dependendo, em regra, de representação da vítima, nos termos do art. 171, § 5º.","E","O § 5º foi revogado pela Lei nº 15.397/2026.")])

# ================================================================ UNIDADE 6
opener("06","UNIDADE 6","Crimes contra a Administração Pública",["Funcionário público e peculato","Concussão x corrupção passiva x corrupção ativa","Prevaricação, resistência, desobediência e desacato"],"U6")

add(H(6,'Funcionário público e <span class="hl">peculato</span>','Arts. 327 e 312.', "A19") +
 lei(cp("Art. 312, caput"),'<p>Art. 312 - Apropriar-se o funcionário público de dinheiro, valor ou qualquer outro bem móvel, público ou particular, de que tem a posse em razão do cargo, ou desviá-lo, em proveito próprio ou alheio:<br>Pena - reclusão, de dois a doze anos, e multa.</p>') +
 table(["Ponto","Regra (em síntese)"],[
  ["Funcionário público para fins penais (art. 327)","Quem, embora transitoriamente ou sem remuneração, exerce cargo, emprego ou função pública; equipara-se quem trabalha em entidade paraestatal ou em empresa contratada ou conveniada para atividade típica da Administração"],
  ["Peculato-apropriação e peculato-desvio (caput)","Apropriar-se do bem que tem a posse em razão do cargo, ou desviá-lo"],
  ["Peculato-furto (§ 1º)","Sem ter a posse, subtrai ou concorre para que seja subtraído, valendo-se da facilidade que o cargo proporciona"],
  ["Peculato culposo (§ 2º)","Concorre culposamente para o crime de outrem: detenção, 3 meses a 1 ano"],
  ["Reparação do dano (§ 3º)","No peculato culposo: antes da sentença irrecorrível, extingue a punibilidade; depois, reduz a pena pela metade"]],["30%",None]) +
 memo('Peculato: <strong>reclusão de 2 a 12 anos</strong>. A reparação do dano <strong>extingue a punibilidade</strong> só no peculato <strong>culposo</strong>, se feita antes da sentença irrecorrível.') +
 pega('<ul><li>Funcionário público, para o CP, é conceito <b>amplo</b>: inclui quem exerce função pública <b>temporariamente</b> e <b>sem remuneração</b> (ex.: mesário e jurado).</li><li>O benefício do § 3º vale para o peculato <b>culposo</b>, e não para o doloso.</li></ul>'))

adm = scene3([("CONCUSSÃO",C['red'],C['redsoft'],"prof",["“Ou me paga","R$ 500, ou eu","multo o senhor.”"],"funcionário EXIGE"),
 ("CORRUPÇÃO PASSIVA",C['golddeep'],C['goldsoft'],"profa",["“Com um","cafezinho de R$ 200","isso se resolve...”"],"funcionário SOLICITA/RECEBE"),
 ("CORRUPÇÃO ATIVA",C['navy'],'#e6e7ea',"prof",["“Tome R$ 300","para esquecer","essa multa.”"],"particular OFERECE/PROMETE")], "Situação ilustrada: o verbo diz qual é o crime.")
add(H(6,'Concussão x corrupção passiva x <span class="hl">corrupção ativa</span>','O verbo de cada tipo resolve a questão.', "A20") + adm +
 table(["","CONCUSSÃO (316)","CORRUPÇÃO PASSIVA (317)","CORRUPÇÃO ATIVA (333)"],[
  ["Quem pratica","Funcionário público","Funcionário público","<b>Particular</b>"],
  ["Verbo","<b>Exigir</b> vantagem indevida","<b>Solicitar ou receber</b> vantagem indevida, ou <b>aceitar promessa</b>","<b>Oferecer ou prometer</b> vantagem indevida"],
  ["Ideia","Imposição (a vítima teme)","Negociação (pedido ou aceitação)","Iniciativa do particular para determinar o ato de ofício"],
  ["Pena","Reclusão, 2 a 12 anos, e multa","Reclusão, 2 a 12 anos, e multa","Reclusão, 2 a 12 anos, e multa"]],["16%",None,None,None]) +
 memo('<strong>Exigir</strong> = concussão. <strong>Solicitar, receber, aceitar promessa</strong> = corrupção passiva. <strong>Oferecer, prometer</strong> = corrupção ativa. As três: <strong>reclusão de 2 a 12 anos</strong>, e multa.'))

add(H(6,'Prevaricação, resistência, desobediência e <span class="hl">desacato</span>','Arts. 319, 329, 330 e 331.', "A21") +
 table(["Crime","Conduta (texto legal)","Pena"],[
  ["Prevaricação (319)","Retardar ou deixar de praticar, indevidamente, ato de ofício, ou praticá-lo contra disposição expressa de lei, para satisfazer interesse ou sentimento pessoal","Detenção, 3 meses a 1 ano, e multa"],
  ["Resistência (329)","Opor-se à execução de ato legal, mediante violência ou ameaça a funcionário competente para executá-lo ou a quem lhe esteja prestando auxílio","Detenção, 2 meses a 2 anos (reclusão, 1 a 3 anos, se o ato não se executa)"],
  ["Desobediência (330)","Desobedecer a ordem legal de funcionário público","Detenção, 15 dias a 6 meses, e multa"],
  ["Desacato (331)","Desacatar funcionário público no exercício da função ou em razão dela","Detenção, 6 meses a 2 anos, ou multa"]],["18%",None,"24%"]) +
 lei(cp("Art. 333, caput"),'<p>Art. 333 - Oferecer ou prometer vantagem indevida a funcionário público, para determiná-lo a praticar, omitir ou retardar ato de ofício:<br>Pena - reclusão, de 2 (dois) a 12 (doze) anos, e multa.</p>') +
 ex(p('Durante uma abordagem, o motorista se recusa a parar após a ordem legal do agente: <b>desobediência</b>. Se ele empurra o agente para impedir a apreensão do veículo: <b>resistência</b> (violência contra o funcionário). Se ele xinga e humilha o agente na frente de todos, em razão da função: <b>desacato</b>.')) +
 pega('<ul><li><b>Resistência</b> exige <b>violência ou ameaça</b>; a <b>desobediência</b> é o simples descumprimento da ordem legal.</li><li>O desacato exige que a ofensa ocorra <b>no exercício da função ou em razão dela</b>.</li><li>Na prevaricação, o motivo é <b>interesse ou sentimento pessoal</b>; se o funcionário age por vantagem indevida, é corrupção passiva.</li></ul>'))

treino(6, [
 ("Para os efeitos penais, considera-se funcionário público quem, embora transitoriamente ou sem remuneração, exerce cargo, emprego ou função pública.","C","Art. 327."),
 ("No peculato doloso, a reparação do dano antes da sentença irrecorrível extingue a punibilidade.","E","Isso vale para o peculato culposo (§ 3º)."),
 ("O funcionário que exige vantagem indevida em razão da função comete concussão.","C","Art. 316."),
 ("O particular que oferece vantagem indevida a funcionário para que ele deixe de praticar ato de ofício comete corrupção passiva.","E","Comete corrupção ativa (art. 333)."),
 ("A resistência exige violência ou ameaça contra o funcionário competente.","C","Art. 329."),
 ("A pena da concussão é de reclusão, de 2 a 12 anos, e multa.","C","Art. 316 (redação da Lei nº 13.964/2019).")])

# ================================================================ REVISÃO
mapa = f'''<figure><svg viewBox="0 0 640 470" width="580" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<g stroke="#b9b3ad" stroke-width="2.5" fill="none"><path d="M320 235 L150 70"/><path d="M320 235 L490 70"/><path d="M320 235 L120 235"/><path d="M320 235 L520 235"/><path d="M320 235 L150 400"/><path d="M320 235 L490 400"/></g>
<circle cx="320" cy="235" r="74" fill="{C['navy']}"/><text x="320" y="225" text-anchor="middle" fill="{C['gold']}" font-weight="900" font-size="13">PARTE ESPECIAL</text>
<text x="320" y="245" text-anchor="middle" fill="#fff" font-weight="900" font-size="15">DIREITO</text><text x="320" y="263" text-anchor="middle" fill="#fff" font-weight="900" font-size="15">PENAL</text>
''' + "".join(
 f'<rect x="{x-100}" y="{y-40}" width="200" height="80" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x}" y="{y-16}" text-anchor="middle" font-weight="900" font-size="12.5" fill="{fg}">{t}</text>'
 + "".join(f'<text x="{x}" y="{y+4+i*15}" text-anchor="middle" font-size="10.8" fill="{C["ink"]}">{l}</text>' for i,l in enumerate(ls))
 for x,y,t,ls,fg,bg in [
  (150,62,"VIDA",["homicídio 6-20 · qualif. 12-30","feminicídio (121-A) 20-40","infanticídio: estado puerperal"],C['navy'],'#e6e7ea'),
  (490,62,"LESÃO",["grave: >30 dias, debilidade","gravíssima: perda, aborto","doméstica/mulher: 2-5 anos"],C['blue'],C['sky']),
  (112,235,"HONRA",["calúnia: crime falso","difamação: fato ofensivo","injúria: qualidade negativa"],C['golddeep'],C['goldsoft']),
  (528,235,"LIBERDADE",["ameaça · perseguição (reiterada)","bullying: multa · virtual 2-4","sequestro: >15 dias qualifica"],C['green'],C['greensoft']),
  (150,408,"PATRIMÔNIO",["furto 1-6 · roubo 6-10","morte no roubo 24-30","extorsão: vítima colabora"],C['red'],C['redsoft']),
  (490,408,"ADMINISTRAÇÃO",["exigir = concussão","solicitar = corrupção passiva","oferecer = corrupção ativa"],C['navy'],'#e6e7ea')]) + '</svg><figcaption>Mapa conceitual do Caderno 06.</figcaption></figure>'
add('<div class="marker">§§R1§§</div><div class="unit"><span class="u">REVISÃO</span><span class="t">Véspera da prova</span></div><h1 class="big">Mapa <span class="hl">conceitual</span></h1><p class="lead">A Parte Especial em seis blocos. Explique cada caixa em voz alta.</p>' + mapa)

add('<div class="unit"><span class="u">REVISÃO</span><span class="t">Pontos de confusão</span></div><h1 class="big">As confusões <span class="hl">mais comuns</span></h1><p class="lead">Os pares de crimes que mais derrubam candidatos.</p>' +
 table(["Confusão","O certo é"],[
  ["Feminicídio: qualificadora ou crime?","Crime <b>autônomo</b> (art. 121-A), pena de 20 a 40 anos, desde a Lei nº 14.994/2024."],
  ["Motivo fútil x torpe","Fútil: banal, desproporcional. Torpe: repugnante, vil."],
  ["Infanticídio x homicídio","Infanticídio: mãe, sob estado puerperal, durante ou logo após o parto."],
  ["Lesão grave x gravíssima","Debilidade e mais de 30 dias: grave. Perda, incapacidade permanente, deformidade, aborto: gravíssima."],
  ["Calúnia x difamação x injúria","Fato criminoso falso · fato ofensivo · qualidade negativa."],
  ["Constrangimento ilegal x ameaça","Impor conduta · prometer mal injusto e grave."],
  ["Bullying x cyberbullying","Presencial: multa. Virtual: reclusão de 2 a 4 anos."],
  ["Furto x roubo","Roubo exige violência ou grave ameaça à <b>pessoa</b>."],
  ["Roubo x extorsão","Roubo: o agente toma. Extorsão: a vítima faz o ato (colaboração indispensável)."],
  ["Apropriação indébita x estelionato","Apropriação: posse lícita antes, dolo depois. Estelionato: fraude antes da entrega."],
  ["Concussão x corrupção passiva x ativa","Exigir · solicitar/receber/aceitar · oferecer/prometer."],
  ["Resistência x desobediência","Resistência: com violência ou ameaça. Desobediência: só descumprir a ordem legal."]],["34%",None]))

FC = [("VIDA","Pena do homicídio simples e do qualificado?","Simples: reclusão de 6 a 20 anos. Qualificado: 12 a 30 anos."),
 ("VIDA","Onde está hoje o feminicídio e qual a pena?","Art. 121-A, crime autônomo; reclusão de 20 a 40 anos."),
 ("VIDA","O que é perdão judicial no homicídio culposo?","O juiz deixa de aplicar a pena se as consequências atingirem o agente de forma tão grave que a pena se torne desnecessária."),
 ("VIDA","Elementos do infanticídio?","A mãe mata o próprio filho, sob estado puerperal, durante o parto ou logo após."),
 ("VIDA","Quando o aborto não é punido (art. 128)?","Feito por médico: para salvar a vida da gestante ou em gravidez resultante de estupro, com consentimento."),
 ("LESÃO","Lesão com mais de 30 dias de incapacidade?","Lesão grave (art. 129, § 1º, I)."),
 ("LESÃO","Lesão que resulta aborto?","Lesão gravíssima (art. 129, § 2º, V)."),
 ("HONRA","Diferença entre calúnia e difamação?","Calúnia: fato definido como crime, falso. Difamação: fato ofensivo à reputação."),
 ("HONRA","Pena se o crime contra a honra for divulgado em redes sociais?","Pena em triplo (art. 141, § 2º)."),
 ("HONRA","A retratação vale para quais crimes?","Calúnia e difamação (art. 143)."),
 ("LIBERDADE","Pena do bullying presencial e do virtual?","Presencial: multa. Virtual: reclusão de 2 a 4 anos, e multa."),
 ("LIBERDADE","Requisito central da perseguição?","Reiteração da conduta (art. 147-A)."),
 ("LIBERDADE","Ameaça contra a mulher por razões da condição do sexo feminino?","Pena em dobro e ação sem necessidade de representação (art. 147, §§ 1º e 2º)."),
 ("PATRIMÔNIO","Pena atual do furto simples?","Reclusão de 1 a 6 anos, e multa (Lei nº 15.397/2026)."),
 ("PATRIMÔNIO","Furto privilegiado?","Criminoso primário e coisa de pequeno valor (art. 155, § 2º)."),
 ("PATRIMÔNIO","Pena atual do roubo simples?","Reclusão de 6 a 10 anos, e multa (Lei nº 15.397/2026)."),
 ("PATRIMÔNIO","Roubo impróprio?","Violência ou grave ameaça logo depois da subtração, para garantir a impunidade ou a coisa."),
 ("PATRIMÔNIO","Roubo com arma de fogo?","Aumento de 2/3 (art. 157, § 2º-A, I)."),
 ("PATRIMÔNIO","Diferença entre roubo e extorsão?","Na extorsão, a colaboração da vítima é indispensável."),
 ("PATRIMÔNIO","Pena da fraude eletrônica?","Reclusão de 4 a 8 anos, e multa (art. 171, § 2º-A)."),
 ("PATRIMÔNIO","Receptação: sabe x deve saber x deve presumir?","Caput (sabe) · qualificada no comércio (deve saber) · culposa (deve presumir)."),
 ("ADMINISTRAÇÃO","Conceito penal de funcionário público?","Quem exerce cargo, emprego ou função pública, ainda que transitoriamente ou sem remuneração."),
 ("ADMINISTRAÇÃO","Exigir vantagem indevida é qual crime?","Concussão (art. 316)."),
 ("ADMINISTRAÇÃO","Desobediência x desacato?","Desobedecer a ordem legal · ofender o funcionário no exercício ou em razão da função.")]
def fcpage(items, first):
    cs = "".join(f'<div class="c"><div class="f"><small>{a}</small>{q}</div><div class="b">{r}</div></div>' for a,q,r in items)
    h = ('<div class="marker">§§R2§§</div><div class="unit"><span class="u">REVISÃO ATIVA</span></div><h1 class="big">Flash<span class="hl">cards</span></h1><p class="lead">Cubra a resposta, tente lembrar e confira. Revise em 1, 3, 7, 15 e 30 dias.</p>' if first else '')
    return h + f'<div class="fc">{cs}</div>'
add(fcpage(FC[:12], True)); add(fcpage(FC[12:], False))

Q = [
 ("Homicídio","Após perder uma aposta de pequeno valor, Caio mata o colega com um tiro. O homicídio é qualificado pelo:",
  ["motivo torpe.","motivo fútil.","emprego de veneno.","feminicídio.","relevante valor moral."],"B",
  "Motivo fútil é o banal, desproporcional à reação (art. 121, § 2º, II). Torpe é o motivo repugnante; relevante valor moral é causa de diminuição (§ 1º).","Fútil = banal; torpe = repugnante."),
 ("Feminicídio","Sobre o feminicídio, na legislação vigente, assinale a alternativa correta.",
  ["É qualificadora do homicídio prevista no art. 121, § 2º, VI.","É crime autônomo, previsto no art. 121-A, com pena de reclusão de 20 a 40 anos.","Configura-se sempre que a vítima for mulher, independentemente da motivação.","Tem a mesma pena do homicídio simples.","Foi revogado pela Lei nº 14.994/2024."],"B",
  "A Lei nº 14.994/2024 revogou o inciso VI do § 2º e criou o art. 121-A, crime autônomo, exigindo razões da condição do sexo feminino.","Feminicídio: art. 121-A, 20 a 40 anos."),
 ("Infanticídio","Logo após o parto, sob a influência do estado puerperal, a mãe mata o próprio filho. Ela responde por:",
  ["homicídio qualificado.","aborto.","infanticídio.","lesão corporal seguida de morte.","homicídio culposo."],"C",
  "Art. 123: matar, sob a influência do estado puerperal, o próprio filho, durante o parto ou logo após.","Estado puerperal + mãe = infanticídio."),
 ("Lesão","A lesão corporal que resulta incapacidade para as ocupações habituais por mais de trinta dias é classificada como:",
  ["leve.","grave.","gravíssima.","seguida de morte.","culposa."],"B",
  "Art. 129, § 1º, I. A incapacidade permanente para o trabalho é que torna a lesão gravíssima.","Mais de 30 dias = grave."),
 ("Lesão","Numa briga, José dá um soco em Paulo, que cai, bate a cabeça e morre. José não quis nem assumiu o risco da morte. José responde por:",
  ["homicídio doloso.","homicídio culposo apenas.","lesão corporal seguida de morte.","lesão corporal leve.","latrocínio."],"C",
  "Art. 129, § 3º: crime preterdoloso, com dolo na lesão e culpa no resultado morte.","Dolo na lesão + culpa na morte = preterdolo."),
 ("Honra","Ricardo afirma, em um grupo de mensagens, sabendo ser mentira, que o colega “desviou dinheiro do caixa da empresa”. Ricardo comete:",
  ["injúria.","difamação.","calúnia.","denunciação caluniosa.","ameaça."],"C",
  "Imputar falsamente fato definido como crime é calúnia (art. 138). A difamação atribui fato ofensivo que não precisa ser crime; a injúria atribui qualidade negativa.","Fato criminoso falso = calúnia."),
 ("Honra","Chamar alguém de “incompetente e idiota” configura, em tese:",
  ["calúnia.","difamação.","injúria.","constrangimento ilegal.","ameaça."],"C",
  "A injúria ofende a dignidade ou o decoro, atribuindo qualidade negativa (art. 140).","Qualidade negativa = injúria."),
 ("Honra","Se o crime contra a honra é cometido ou divulgado em redes sociais da internet, a pena:",
  ["é aumentada de um terço.","é aplicada em dobro.","é aplicada em triplo.","não sofre alteração.","é substituída por multa."],"C",
  "Art. 141, § 2º. A pena em dobro vale para paga ou promessa de recompensa (§ 1º) e para crimes contra a mulher por razões da condição do sexo feminino (§ 3º).","Redes sociais = triplo."),
 ("Liberdade","Sobre a intimidação sistemática (bullying), prevista no art. 146-A do CP, é correto afirmar que:",
  ["a forma presencial é punida com reclusão de 2 a 4 anos.","a forma virtual é punida com reclusão de 2 a 4 anos, e multa, se a conduta não constituir crime mais grave.","não é crime, mas infração administrativa.","exige vítima mulher.","foi criada pela Lei Maria da Penha."],"B",
  "Art. 146-A (Lei nº 14.811/2024): a forma presencial é punida com multa; a virtual (parágrafo único), com reclusão de 2 a 4 anos e multa.","Bullying: multa; cyberbullying: 2 a 4 anos."),
 ("Liberdade","O ex-companheiro que, durante semanas, persegue a vítima, aparece repetidamente em seu trabalho e envia dezenas de mensagens ameaçadoras comete:",
  ["ameaça simples, apenas.","perseguição (art. 147-A).","constrangimento ilegal.","sequestro.","injúria."],"B",
  "A perseguição exige reiteração e ameaça à integridade física ou psicológica, restrição da locomoção ou perturbação da liberdade ou privacidade.","Reiteração = perseguição."),
 ("Liberdade","É considerado “casa”, para os fins do crime de violação de domicílio:",
  ["a taverna aberta ao público.","a hospedaria enquanto aberta, quanto às áreas comuns.","o aposento ocupado de habitação coletiva.","a casa de jogo.","a recepção aberta ao público de um escritório."],"C",
  "Art. 150, § 4º, II. As demais hipóteses estão no § 5º (não compreendidas na expressão casa) ou são áreas abertas ao público.","Quarto ocupado de hotel = casa."),
 ("Furto","De acordo com a redação vigente do art. 155 do CP, a pena do furto simples é de:",
  ["detenção, de 6 meses a 2 anos.","reclusão, de 1 a 4 anos, e multa.","reclusão, de 1 a 6 anos, e multa.","reclusão, de 4 a 10 anos, e multa.","reclusão, de 2 a 8 anos, e multa."],"C",
  "A Lei nº 15.397/2026 alterou a pena do furto simples para reclusão de 1 a 6 anos e multa. A de 1 a 4 anos era a pena anterior; 2 a 8 é a do furto qualificado do § 4º.","Furto simples: 1 a 6 anos."),
 ("Furto","Ana pega, sem ser notada, o celular que a vítima deixou sobre a mesa de uma lanchonete. Pela redação vigente do CP, trata-se de:",
  ["roubo.","furto, com a pena do § 6º (reclusão, de 4 a 10 anos, e multa).","estelionato.","apropriação indébita.","dano."],"B",
  "Subtração sem violência ou grave ameaça é furto. A Lei nº 15.397/2026 incluiu o celular no § 6º do art. 155.","Celular furtado: § 6º."),
 ("Furto","Configura furto privilegiado, autorizando os benefícios do art. 155, § 2º:",
  ["furto praticado durante o repouso noturno.","criminoso primário e coisa furtada de pequeno valor.","furto com destruição de obstáculo.","furto de veículo levado a outro Estado.","furto praticado por duas pessoas."],"B",
  "O § 2º exige primariedade e pequeno valor. O repouso noturno aumenta a pena; as demais são qualificadoras.","Privilégio: primário + pequeno valor."),
 ("Roubo","Lucas subtrai uma bolsa numa loja e, ao ser abordado pelo segurança na saída, agride-o para fugir com o objeto. Lucas comete:",
  ["furto qualificado.","roubo próprio.","roubo impróprio.","extorsão.","lesão corporal, apenas."],"C",
  "Art. 157, § 1º: violência empregada logo depois da subtração para assegurar a impunidade ou a detenção da coisa.","Violência depois da subtração = roubo impróprio."),
 ("Roubo","No roubo, a violência ou grave ameaça exercida com emprego de arma de fogo:",
  ["aumenta a pena de 1/3 até a metade.","aumenta a pena de 2/3.","duplica a pena, em qualquer caso.","não altera a pena.","transforma o crime em extorsão."],"B",
  "Art. 157, § 2º-A, I. A arma branca gera aumento de 1/3 até a metade (§ 2º, VII), e a arma de uso restrito ou proibido, pena em dobro (§ 2º-B).","Arma de fogo: +2/3."),
 ("Roubo","Na redação vigente, se da violência empregada no roubo resulta morte, a pena é de:",
  ["reclusão, de 20 a 30 anos.","reclusão, de 24 a 30 anos, e multa.","reclusão, de 12 a 30 anos.","reclusão, de 7 a 18 anos.","detenção, de 4 a 12 anos."],"B",
  "Art. 157, § 3º, II, com a redação da Lei nº 15.397/2026. A pena de 7 a 18 anos é a do resultado lesão grave.","Roubo com morte: 24 a 30 anos."),
 ("Extorsão","Mediante grave ameaça, o agente obriga a vítima a fazer uma transferência bancária para sua conta. Trata-se de:",
  ["furto mediante fraude.","roubo.","extorsão.","estelionato.","apropriação indébita."],"C",
  "Na extorsão (art. 158), a vítima é constrangida a fazer algo, e sua colaboração é indispensável para a obtenção da vantagem.","Vítima faz o ato sob ameaça = extorsão."),
 ("Estelionato","Golpista se passa por filho da vítima em aplicativo de mensagens e a convence a fazer um PIX. A conduta configura:",
  ["furto simples.","estelionato na forma de fraude eletrônica (art. 171, § 2º-A).","roubo.","extorsão.","receptação."],"B",
  "A vítima, induzida em erro por meio de aplicativo, entrega voluntariamente a vantagem. A fraude eletrônica tem pena de reclusão de 4 a 8 anos e multa.","Fraude que faz a vítima entregar = estelionato."),
 ("Estelionato","Sobre a ação penal no estelionato, após a Lei nº 15.397/2026, é correto afirmar que:",
  ["continua exigindo representação da vítima, em regra, nos termos do § 5º.","o § 5º do art. 171, que tratava da representação, foi revogado.","passou a ser crime de ação penal privada.","depende de requisição do Ministro da Justiça.","só se procede mediante queixa."],"B",
  "O § 5º, incluído pela Lei nº 13.964/2019, foi revogado pela Lei nº 15.397/2026, deixando de existir a regra especial de representação.","§ 5º do art. 171: revogado."),
 ("Receptação","Comerciante adquire, no exercício de sua atividade, celulares que deve saber serem produto de crime. Ele responde por:",
  ["receptação culposa.","receptação qualificada (art. 180, § 1º).","furto.","estelionato.","favorecimento real."],"B",
  "O § 1º pune a receptação no exercício de atividade comercial ou industrial, com coisa que o agente deve saber ser produto de crime: reclusão de 3 a 8 anos e multa.","Comércio + deve saber = qualificada."),
 ("Administração","O fiscal que diz ao comerciante “ou me paga R$ 500, ou eu interdito o seu estabelecimento” comete:",
  ["corrupção passiva.","corrupção ativa.","concussão.","prevaricação.","peculato."],"C",
  "Exigir vantagem indevida em razão da função é concussão (art. 316). Solicitar ou receber é corrupção passiva.","Exigir = concussão."),
 ("Administração","O motorista que oferece dinheiro ao agente de trânsito para que ele não lavre a autuação comete:",
  ["corrupção passiva.","corrupção ativa.","concussão.","desacato.","prevaricação."],"B",
  "Oferecer ou prometer vantagem indevida a funcionário para determiná-lo a omitir ato de ofício é corrupção ativa (art. 333).","Particular oferece = corrupção ativa."),
 ("Administração","Durante abordagem, o condutor empurra o agente público para impedir a apreensão legal do veículo. Ele comete:",
  ["desobediência.","desacato.","resistência.","prevaricação.","corrupção ativa."],"C",
  "A resistência (art. 329) exige oposição à execução de ato legal mediante violência ou ameaça ao funcionário. A desobediência é o simples descumprimento da ordem legal.","Violência ou ameaça para impedir ato legal = resistência.")]

def qhtml(i, q):
    tema, enun, alts, gab, com, mem = q
    lis = "".join(f'<li data-l="{"ABCDE"[j]}">{a}</li>' for j,a in enumerate(alts))
    return f'<div class="q"><div class="qh"><span class="qn">Questão {i:02d}</span><span class="qa">Questão autoral · {tema}</span></div><p>{enun}</p><ol>{lis}</ol></div>'
qs = [qhtml(i+1,q) for i,q in enumerate(Q)]
add('<div class="marker">§§R3§§</div><div class="unit"><span class="u">PRÁTICA</span><span class="t">24 questões</span></div><h1 class="big">Questões <span class="hl">autorais</span></h1><p class="lead">Elaboradas para este caderno, no estilo de concursos. Nenhuma foi aplicada por banca. Resolva sem consultar.</p>' + "".join(qs[:3]))
for k in range(3, len(qs), 3): add("".join(qs[k:k+3]))
def grid(a, b):
    return "<table><tr>" + "".join(f"<th style='text-align:center'>{i+1:02d}</th>" for i in range(a,b)) + "</tr><tr>" + "".join(f"<td style='text-align:center;font-weight:900;color:{C['navy']}'>{Q[i][3]}</td>" for i in range(a,b)) + "</tr></table>"
gabs = [f'<div class="gab"><div class="gh">Questão {i+1:02d} <span>{q[3]}</span></div><p>{q[4]}</p><span class="mem">Memorize: {q[5]}</span></div>' for i,q in enumerate(Q)]
add('<div class="marker">§§R4§§</div><div class="unit"><span class="u">CORREÇÃO</span></div><h1 class="big">Gabarito <span class="hl">comentado</span></h1><p class="lead">Leia o comentário mesmo quando acertar.</p>' + grid(0,12) + grid(12,24) + "".join(gabs[:4]))
for k in range(4, len(gabs), 6): add("".join(gabs[k:k+6]))
def tr_block(lst):
    out = ""
    for n, itens in lst:
        rows = "".join(f'<tr><td style="width:7%;text-align:center;font-weight:900">{i+1}</td><td style="width:12%;text-align:center" class="{"yes" if r=="C" else "no"}">{"CERTO" if r=="C" else "ERRADO"}</td><td>{c}</td></tr>' for i,(_,r,c) in enumerate(itens))
        out += f'<h3>Treino rápido · Unidade {n}</h3><table><tr><th>#</th><th>Resposta</th><th>Comentário</th></tr>{rows}</table>'
    return out
add('<div class="unit"><span class="u">CORREÇÃO</span><span class="t">Treinos rápidos</span></div><h1 class="big">Respostas dos <span class="hl">treinos</span></h1><p class="lead">Certo ou errado das Unidades 1 a 6.</p>' + tr_block(TREINOS[:2]))
add(tr_block(TREINOS[2:4])); add(tr_block(TREINOS[4:]))

add(f'''<div class="unit"><span class="u">ENCERRAMENTO</span></div><h1 class="big">Referências e <span class="hl">verificação</span></h1><p class="lead">De onde vieram as informações.</p>
<h3>Legislação consultada (portal do Planalto)</h3>
<ul>
<li><strong>Código Penal</strong> (Decreto-Lei nº 2.848/1940), texto compilado: arts. 121, 121-A, 121-B, 122 a 129, 138 a 150, 155 a 159, 163, 167, 168, 171, 180 a 183, 312, 316, 317, 319, 327, 329, 330, 331 e 333.</li>
<li>Leis que alteraram esses artigos e foram identificadas nas notas do texto compilado: nº 13.964/2019, 14.132/2021, 14.155/2021, 14.188/2021, 14.344/2022, 14.532/2023, 14.811/2024, 14.967/2024, 14.994/2024, 15.123/2025, 15.134/2025, 15.159/2025, 15.181/2025, 15.358/2026, 15.384/2026, 15.397/2026, 15.455/2026 e 15.517/2026.</li>
<li>Citada sem conferência: Lei nº 7.716/1989 (Lei do Racismo), quanto à injúria racial.</li>
</ul>
<h3>Jurisprudência citada</h3><ul><li>STF: ADPF 54 (feto anencéfalo); Súmula 610 (latrocínio).</li></ul>''' + lembre(p(f'<strong>Material pesquisado e atualizado em: {DATA}.</strong> Todos os tipos penais e todas as penas deste caderno foram conferidos no texto compilado do Código Penal no portal do Planalto, que exibe a redação vigente com as notas de alteração. <strong>Limitações:</strong> o texto compilado não indica a data da última atualização, e as leis de 2026 (como a nº 15.397/2026) não foram lidas no Diário Oficial; algumas regras extensas aparecem resumidas, e não transcritas. A Lei nº 7.716/1989 e as súmulas e precedentes do STF citados não foram reconferidos nesta edição. Confira se houve alteração posterior antes da prova e consulte o edital do seu concurso.'), "Verificação e limitações"))
add('''<div class="ending"><h2>Fim do Caderno 06</h2><p style="text-align:center">Sugestão de próximo caderno na coleção: <strong>Legislação Penal Especial</strong> (Lei de Drogas, Estatuto do Desarmamento, Lei Maria da Penha, crimes de trânsito).</p>
<p class="note" style="text-align:center">Mapa da Aprovação · Caderno Simplificado · Direito Penal · Caderno 06 · 1ª edição · novembro de 2026<br>Material de estudo independente. Não substitui a leitura da lei e do edital do seu concurso.</p></div>''')

doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Caderno Simplificado — Caderno 06 — Direito Penal: Parte Especial</title>
<link rel="stylesheet" href="estilo.css"></head><body>{symbols()}{"".join(P)}</body></html>'''
open(os.path.join(HERE, "miolo.html"), "w").write(doc)
print("páginas planejadas:", len(P))
