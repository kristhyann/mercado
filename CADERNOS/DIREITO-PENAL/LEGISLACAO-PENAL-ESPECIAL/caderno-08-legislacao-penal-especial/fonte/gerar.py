"""Gera miolo.html do Caderno 08: Legislação Penal Especial. Uso: python3 gerar.py
Leis conferidas nos textos do portal do Planalto em 26/11/2026: 11.343/2006, 10.826/2003, 8.072/1990,
11.340/2006, 13.869/2019, 9.455/1997 e 12.850/2013."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from componentes import *

DATA = "26 de novembro de 2026"
P = []
def add(html, first=False): P.append(page(f'<div class="marker">§§P{len(P)+1:03d}§§</div>' + html, first))
U = {1:("UNIDADE 1","Lei de Drogas"),2:("UNIDADE 2","Estatuto do Desarmamento"),3:("UNIDADE 3","Hediondos e Tortura"),4:("UNIDADE 4","Lei Maria da Penha"),5:("UNIDADE 5","Abuso de Autoridade e Org. Criminosa")}
def H(u, title, lead, marker=None): return head(U[u][0], U[u][1], title, lead, marker)
def L(n, x): return f"{x} · Lei nº {n}"
def p(t): return f"<p>{t}</p>"
def colors(*keys):
    m = {"b":(C['blue'],C['sky']),"g":(C['green'],C['greensoft']),"o":(C['golddeep'],C['goldsoft']),"r":(C['red'],C['redsoft']),"n":(C['navy'],'#e6e7ea')}
    return [m[k] for k in keys]
def atencao(html, kws=None, t='Atenção na prova'):
    add(pratica_title(t) + html + (kw(kws) if kws else ''))
NV = '#e6e7ea'
def scene3(items, cap):
    s = f'<figure><svg viewBox="0 0 640 260" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    for i,(t,fg,bg,who,lines,leg) in enumerate(items):
        x = i*214
        s += f'<rect x="{x+2}" y="2" width="206" height="256" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x+105}" y="26" text-anchor="middle" font-weight="900" font-size="14" fill="{fg}">{t}</text>'
        s += f'<rect x="{x+14}" y="38" width="182" height="{20+len(lines)*17}" rx="12" fill="#fff" stroke="{fg}" stroke-width="1.8"/>'
        s += "".join(f'<text x="{x+105}" y="{58+j*17}" text-anchor="middle" font-size="11.2" font-weight="800" fill="{C["ink"]}">{l}</text>' for j,l in enumerate(lines))
        s += f'<g transform="translate({x+70},{70+len(lines)*17})"><svg viewBox="0 0 100 170" width="62" height="105"><use href="#ch-{who}"/></svg></g>'
        s += f'<text x="{x+105}" y="244" text-anchor="middle" font-size="11" font-weight="900" fill="{fg}">{leg}</text>'
    return s + f'</svg><figcaption>{cap}</figcaption></figure>'
def ficha(items):
    """Infográfico de 'ficha da lei': lista de (rótulo, valor)."""
    rows = "".join(f'<tr><td class="rh" style="width:30%">{a}</td><td>{b}</td></tr>' for a,b in items)
    return f'<table><tr><th colspan="2">Ficha da lei</th></tr>{rows}</table>'

# ================================================================ APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">As leis penais especiais mais presentes em editais de polícias e guardas municipais, explicadas pelo que costuma ser cobrado.</p>
<p>Este é o <strong>Caderno 08 da coleção</strong>, dedicado à <strong>Legislação Penal Especial</strong>: as leis penais que ficam <strong>fora do Código Penal</strong>. Ele <strong>não reproduz as leis inteiras</strong>. Para cada uma, você encontra a <strong>finalidade</strong>, os <strong>conceitos centrais</strong>, as <strong>diferenças</strong> que mais confundem e os <strong>pontos de atenção</strong>.</p>
<p><strong>Por que estas leis?</strong> A seleção considerou três critérios: presença habitual em editais de <strong>Guarda Municipal</strong>, <strong>PM</strong>, <strong>Polícia Civil</strong>, <strong>Polícia Penal</strong> e <strong>PRF</strong>; ligação direta com o trabalho de segurança pública; e alterações recentes. Por isso, além das seis leis indicadas, incluímos noções da <strong>Lei de Organizações Criminosas</strong> (Lei nº 12.850/2013), alterada em 2025 e 2026.</p>
{table(["Lei","Por que importa para o seu concurso","Prioridade de estudo"],[
 ["Drogas (11.343/2006)","Ocorrência comum no patrulhamento; usuário x traficante","<b>Alta</b>"],
 ["Desarmamento (10.826/2003)","Posse x porte; porte das guardas municipais","<b>Alta</b>"],
 ["Maria da Penha (11.340/2006)","Atendimento à vítima e medidas protetivas","<b>Alta</b>"],
 ["Abuso de Autoridade (13.869/2019)","Limites da atuação do próprio agente público","<b>Alta</b>"],
 ["Crimes Hediondos (8.072/1990)","Rol de crimes e consequências mais rigorosas","Média"],
 ["Tortura (9.455/1997)","Espécies de tortura e omissão do agente","Média"],
 ["Organizações Criminosas (12.850/2013)","Conceito e diferenças com outras associações","Média"]],["30%",None,"18%"])}
{lembre(p(f'A "prioridade de estudo" é uma <strong>avaliação didática</strong> baseada na relação da lei com o cargo, e não um levantamento estatístico de provas. <strong>Todas as leis foram conferidas no portal do Planalto em {DATA}.</strong> Se houver edital, ele prevalece.'), "Como ler a prioridade")}''', first=True)

TOC = [("u","UNIDADE 1 · LEI DE DROGAS (LEI Nº 11.343/2006)","U1"),("","1. Finalidade e conceito de droga","A01"),("","2. Porte para consumo pessoal (art. 28) e a decisão do STF","A02"),("","3. Tráfico de drogas (art. 33)","A03"),("","4. Usuário x traficante x uso compartilhado","A04"),("","5. Tráfico privilegiado (art. 33, § 4º)","A05"),("","6. Associação, financiamento, aumentos e restrições","A06"),
 ("u","UNIDADE 2 · ESTATUTO DO DESARMAMENTO (LEI Nº 10.826/2003)","U2"),("","7. Posse x porte","A07"),("","8. Crimes com arma de uso permitido (arts. 12 a 15)","A08"),("","9. Uso restrito, uso proibido, comércio e tráfico","A09"),("","10. Porte de arma das guardas municipais","A10"),
 ("u","UNIDADE 3 · CRIMES HEDIONDOS E TORTURA","U3"),("","11. O que é crime hediondo e o rol do art. 1º","A11"),("","12. Equiparados e consequências","A12"),("","13. Tortura: as espécies do art. 1º","A13"),("","14. Tortura: omissão, aumentos e efeitos","A14"),
 ("u","UNIDADE 4 · LEI MARIA DA PENHA (LEI Nº 11.340/2006)","U4"),("","15. Violência doméstica: conceito e formas","A15"),("","16. Atendimento policial e medidas protetivas","A16"),("","17. Descumprimento e pontos processuais","A17"),
 ("u","UNIDADE 5 · ABUSO DE AUTORIDADE E ORGANIZAÇÕES CRIMINOSAS","U5"),("","18. Abuso de autoridade: regras gerais","A18"),("","19. Crimes de abuso mais cobrados","A19"),("","20. Organização criminosa (Lei nº 12.850/2013)","A20"),("","21. Associação criminosa x associação para o tráfico x organização criminosa","A21"),
 ("u","REVISÃO E PRÁTICA","RV"),("","Mapa conceitual · Erros mais comuns · Números da lei","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),("","Gabarito, respostas dos treinos e referências","R4")]
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

# ================================================================ UNIDADE 1 · DROGAS
opener("01","UNIDADE 1","Lei de Drogas",["Finalidade e conceito de droga","Porte para consumo pessoal e o STF","Tráfico de drogas","Usuário x traficante x uso compartilhado","Tráfico privilegiado","Associação, financiamento, aumentos e restrições"],"U1")

add(H(1,'Lei de Drogas: <span class="hl">finalidade e conceito</span>','Prevenir, tratar e reprimir: a lei tem duas faces.', "A01") +
 ficha([("Lei","nº 11.343/2006 (institui o Sisnad)"),("Duas finalidades","<b>Prevenção, atenção e reinserção</b> de usuários e dependentes; <b>repressão</b> à produção não autorizada e ao tráfico"),("Conceito de droga (art. 1º, parágrafo único)","Substâncias ou produtos capazes de causar dependência, especificados em lei ou relacionados em listas atualizadas periodicamente pelo Poder Executivo federal"),("Lista usada hoje (art. 66)","Portaria SVS/MS nº 344/1998, da Anvisa/Ministério da Saúde"),("Crimes principais","Art. 28 (consumo pessoal), art. 33 (tráfico), art. 35 (associação), art. 36 (financiamento), art. 37 (informante)")]) +
 traduz(p('A lei não traz uma lista de drogas. Ela diz que droga é o que uma <strong>norma do Poder Executivo</strong> disser que é. Por isso a doutrina chama esses crimes de <strong>norma penal em branco</strong>: o tipo penal precisa ser "completado" por outra norma, a lista da Anvisa. Se uma substância sai da lista, o fato deixa de ser crime.')) +
 memo('Droga = substância que causa dependência <strong>e</strong> está na <strong>lista oficial</strong> (Portaria SVS/MS nº 344/1998). Lei de Drogas = <strong>norma penal em branco</strong>.'))

add(H(1,'Porte para <span class="hl">consumo pessoal</span> (art. 28)','Não há pena de prisão para o usuário.', "A02") +
 table(["Ponto","Regra (texto vigente)"],[
  ["Verbos (caput)","<b>Adquirir, guardar, ter em depósito, transportar ou trazer consigo</b>, para consumo pessoal, droga sem autorização"],
  ["Penas (incisos I a III)","I - advertência sobre os efeitos das drogas; II - prestação de serviços à comunidade; III - medida educativa de comparecimento a programa ou curso educativo"],
  ["Cultivo (§ 1º)","Semear, cultivar ou colher plantas para preparar <b>pequena quantidade</b>, para consumo pessoal: mesmas medidas"],
  ["Como o juiz decide (§ 2º)","Natureza e quantidade da substância, local e condições da ação, circunstâncias sociais e pessoais, conduta e antecedentes"],
  ["Prazo das medidas (§§ 3º e 4º)","Incisos II e III: até <b>5 meses</b>; na reincidência, até <b>10 meses</b>"],
  ["Se o usuário não cumprir (§ 6º)","Admoestação verbal e, depois, multa"],
  ["No flagrante (art. 48, § 2º)","<b>Não se impõe prisão em flagrante</b>: o autor vai ao juízo ou assume o compromisso de comparecer, e lavra-se <b>termo circunstanciado</b>"]],["28%",None]) +
 lembre(p('Em <strong>2024</strong>, no <strong>RE 635.659</strong> (Tema 506 da repercussão geral), o STF decidiu que o porte de <strong>maconha</strong> para consumo pessoal <strong>não é crime</strong>: continua proibido, mas como <strong>infração administrativa</strong>, sem efeitos penais, com advertência e medida educativa. Presume-se usuário quem estiver com até <strong>40 gramas</strong> ou <strong>6 plantas fêmeas</strong> de cannabis. A presunção é <strong>relativa</strong>: provas de venda podem indicar tráfico mesmo com menos de 40 g. A decisão vale <strong>só para a maconha</strong>; para as demais drogas, o art. 28 continua sendo crime. O texto do art. 28 no Planalto <strong>não foi alterado</strong>.'), "Decisão do STF sobre a maconha"))

add(H(1,'<span class="hl">Tráfico</span> de drogas (art. 33)','Dezoito verbos e uma pena alta.', "A03") +
 lei(L("11.343/2006","Art. 33, caput (pena)"),'<p>Importar, exportar, remeter, preparar, produzir, fabricar, adquirir, vender, expor à venda, oferecer, ter em depósito, transportar, trazer consigo, guardar, prescrever, ministrar, entregar a consumo ou fornecer drogas, ainda que gratuitamente, sem autorização ou em desacordo com determinação legal ou regulamentar:<br>Pena - reclusão de 5 (cinco) a 15 (quinze) anos e pagamento de 500 (quinhentos) a 1.500 (mil e quinhentos) dias-multa.</p>') +
 table(["Figura","Conduta (em síntese)","Pena"],[
  ["Equiparadas (§ 1º)","I - matéria-prima, insumo ou produto químico destinado à preparação de drogas; II - semear ou cultivar plantas que constituam matéria-prima; III - usar ou consentir que se use local ou bem para o tráfico; IV - vender ou entregar droga a <b>agente policial disfarçado</b>, com indícios de conduta criminosa preexistente (Lei nº 13.964/2019)","Mesma do caput"],
  ["Induzir, instigar ou auxiliar o uso (§ 2º)","Estimular alguém a usar droga","Detenção, 1 a 3 anos, e multa"],
  ["Uso compartilhado (§ 3º)","Oferecer droga <b>eventualmente</b>, <b>sem objetivo de lucro</b>, a pessoa de seu <b>relacionamento</b>, para <b>juntos</b> a consumirem","Detenção, 6 meses a 1 ano, e multa, sem prejuízo das penas do art. 28"]],["24%",None,"24%"]) +
 traduz(p('Repare que vários verbos do tráfico (<strong>adquirir, guardar, ter em depósito, transportar, trazer consigo</strong>) são os <strong>mesmos</strong> do art. 28. O que separa usuário de traficante não é o verbo, e sim a <strong>finalidade</strong>: consumo próprio ou difusão da droga. E "ainda que gratuitamente": <strong>dar</strong> droga também é tráfico.'),"profa"))

usu = scene3([("USUÁRIO (art. 28)",C['green'],C['greensoft'],"prof",["Pequena porção","no bolso, para","usar no fim de semana."],"CONSUMO PRÓPRIO"),
 ("COMPARTILHADO (§ 3º)",C['golddeep'],C['goldsoft'],"profa",["Oferece, uma vez,","um cigarro ao amigo,","para usarem juntos."],"EVENTUAL, SEM LUCRO"),
 ("TRÁFICO (art. 33)",C['red'],C['redsoft'],"prof",["Porções embaladas,","balança, anotações","e dinheiro trocado."],"DIFUSÃO / VENDA")], "Situação ilustrada: as circunstâncias mostram a finalidade.")
add(H(1,'Usuário x uso compartilhado x <span class="hl">traficante</span>','A diferença está na finalidade, revelada pelas circunstâncias.', "A04") + usu +
 table(["","USUÁRIO (28)","USO COMPARTILHADO (33, § 3º)","TRÁFICO (33)"],[
  ["Finalidade","Consumo próprio","Consumir junto com pessoa do seu relacionamento","Difundir a droga (com ou sem lucro)"],
  ["Prisão em flagrante","<b>Não</b>: termo circunstanciado","Infração de menor potencial ofensivo","<b>Sim</b>"],
  ["Pena","Advertência, serviços, medida educativa","Detenção, 6 meses a 1 ano, e multa","Reclusão, 5 a 15 anos, e multa"]],["18%",None,None,None]))

atencao(
 flow([("search",["CIRCUNSTÂNCIAS","quantidade,","local, conduta"]),("doc",["ANTECEDENTES","e situação","pessoal (§ 2º)"]),("scales",["JUIZ DECIDE","consumo ou","tráfico"])],
      "Art. 28, § 2º: não há um número fixo na lei; o juiz avalia o conjunto (para a maconha, o STF fixou a presunção de 40 g).", colors=colors("n","o","r")) +
 ex(p('Um guarda municipal aborda um jovem com dois cigarros de maconha e nenhum outro indício. Pela decisão do STF, presume-se usuário, e a conduta é infração administrativa. Se fosse cocaína, seria o crime do art. 28, com termo circunstanciado e sem prisão em flagrante. Já outro jovem, com 25 porções embaladas, balança de precisão e anotações de vendas, indica <b>tráfico</b>, mesmo que a quantidade total seja pequena.')) +
 pega('<ul><li>A lei <b>não fixa quantidade</b> para diferenciar usuário e traficante; o critério de 40 g veio do STF e vale só para a <b>maconha</b>, como presunção relativa.</li><li>No uso compartilhado, os requisitos são <b>cumulativos</b>: eventualidade, sem lucro, pessoa do relacionamento e consumo conjunto. Faltando um, volta a ser tráfico.</li><li>O usuário <b>não</b> é preso em flagrante, mas pode ser conduzido para a lavratura do termo circunstanciado.</li></ul>'),
 ["finalidade","art. 28, § 2º","termo circunstanciado","40 g · presunção relativa","uso compartilhado","ainda que gratuitamente"])

add(H(1,'Tráfico <span class="hl">privilegiado</span> (art. 33, § 4º)','Redução de 1/6 a 2/3 para o traficante eventual.', "A05") +
 lei(L("11.343/2006","Art. 33, § 4º (requisitos)"),'<p>Nos delitos definidos no caput e no § 1º deste artigo, as penas poderão ser reduzidas de um sexto a dois terços, [...] desde que o agente seja primário, de bons antecedentes, não se dedique às atividades criminosas nem integre organização criminosa.</p>') +
 cards([("#1","Primário","Não é reincidente."),("#2","Bons antecedentes","Sem condenações anteriores que pesem contra ele."),("#3","Não se dedica a crimes","O tráfico não é seu meio de vida."),("#4","Não integra organização criminosa","Não faz parte de facção ou grupo estruturado.")],4) +
 ex(p('Uma jovem primária, sem antecedentes, é presa levando droga de uma cidade a outra a pedido de um conhecido, sem indícios de que se dedique ao tráfico ou integre facção. Ela responde por tráfico (art. 33), mas pode ter a pena reduzida de 1/6 a 2/3 pelo § 4º. Se ficasse provado que ela integra uma facção, a redução não seria possível.')))
atencao(lembre(p('O STF decidiu em 2016 (HC 118.533) que o tráfico privilegiado <strong>não é crime hediondo</strong>. O entendimento foi reafirmado no Tema 1.400 da repercussão geral e consolidado na <strong>Súmula Vinculante 63</strong> (2025). Consequência: não se aplicam as regras mais rigorosas de progressão de regime e de livramento condicional dos hediondos, e é possível indulto. O texto da lei ainda menciona a vedação da conversão em restritivas de direitos, mas há nota no Planalto à <strong>Resolução nº 5/2012</strong> do Senado, que suspendeu essa vedação após decisão do STF.'), "Tráfico privilegiado não é hediondo") +
 memo('Tráfico privilegiado: <strong>quatro requisitos cumulativos</strong> e redução de <strong>1/6 a 2/3</strong>. <strong>Não é hediondo</strong> (Súmula Vinculante 63).') +
 pega('<ul><li>O § 4º é uma <b>causa de diminuição de pena</b>, e não um crime diferente: o crime continua sendo tráfico.</li><li>Os requisitos são <b>cumulativos</b>: faltando um, não há redução.</li><li>Para a lei, o tráfico do caput é equiparado a hediondo; o privilegiado, segundo o STF, <b>não</b>.</li></ul>'),
 ["primário","bons antecedentes","não se dedica a crimes","não integra organização criminosa","1/6 a 2/3","Súmula Vinculante 63"])

add(H(1,'Associação, financiamento, <span class="hl">aumentos</span> e restrições','Arts. 35 a 44.', "A06") +
 table(["Crime","Conduta (em síntese)","Pena"],[
  ["Associação para o tráfico (art. 35)","Associarem-se <b>duas ou mais pessoas</b> para praticar, <b>reiteradamente ou não</b>, os crimes dos arts. 33, caput e § 1º, e 34","Reclusão, 3 a 10 anos, e multa"],
  ["Financiamento (art. 36)","Financiar ou custear a prática do tráfico","Reclusão, 8 a 20 anos, e multa"],
  ["Informante (art. 37)","Colaborar, como informante, com grupo ou associação destinados ao tráfico","Reclusão, 2 a 6 anos, e multa"],
  ["Maquinário (art. 34)","Fabricar, adquirir, possuir etc. maquinário ou instrumento destinado à fabricação de drogas","Reclusão, 3 a 10 anos, e multa"],
  ["Prescrição culposa (art. 38)","Prescrever ou ministrar, culposamente, droga sem necessidade ou em dose excessiva","Detenção, 6 meses a 2 anos, e multa"]],["26%",None,"22%"]) +
 table(["Regra","Conteúdo"],[
  ["Aumento de 1/6 a 2/3 (art. 40)","Transnacionalidade; função pública ou missão de educação, guarda ou vigilância; nas imediações de presídios, escolas, hospitais e locais semelhantes; violência, grave ameaça, arma de fogo ou intimidação; tráfico entre Estados ou com o DF; envolvendo criança ou adolescente; agente que financia o crime"],
  ["Pena em dobro (art. 40-A, Lei nº 15.358/2026)","Crimes dos arts. 33 a 37 praticados por integrante de <b>organização criminosa ultraviolenta, grupo paramilitar ou milícia privada</b>; com arma de fogo, aplica-se o concurso material"],
  ["Restrições (art. 44)","Arts. 33, caput e § 1º, e 34 a 37: inafiançáveis e, pelo texto legal, insuscetíveis de sursis, graça, indulto, anistia e liberdade provisória"]],["28%",None]))

atencao(
 table(["","ASSOCIAÇÃO PARA O TRÁFICO (art. 35)","SIMPLES COAUTORIA NO TRÁFICO"],[["Pessoas","2 ou mais","2 ou mais"],["Vínculo","<b>Estável e permanente</b> (entendimento da jurisprudência)","Ocasional, só para aquele crime"],["Crime","Autônomo: existe mesmo sem tráfico consumado","Só há o tráfico"]],["22%",None,None]) +
 ex(p('Dois amigos se juntam <b>uma única vez</b> para levar uma mala de droga a outra cidade: coautoria em tráfico. Dois irmãos que, há meses, dividem tarefas fixas de vender e guardar a droga do bairro: tráfico <b>e</b> associação para o tráfico (art. 35).')) +
 pega('<ul><li>A associação para o tráfico exige <b>duas</b> pessoas; a associação criminosa do CP exige <b>três</b>; a organização criminosa, <b>quatro</b>.</li><li>Apesar do texto do art. 44, o STF declarou inconstitucional a <b>proibição automática da liberdade provisória</b> no tráfico (HC 104.339, 2012). Em prova que pergunta "segundo a lei", vale o texto; "segundo o STF", vale a jurisprudência.</li><li>Art. 40-A é <b>novidade de 2026</b>: pena em dobro para integrante de organização criminosa ultraviolenta ou milícia.</li></ul>'),
 ["duas ou mais pessoas","reiteradamente ou não","financiar ou custear","informante","art. 40-A · em dobro","art. 44"])

treino(1, [
 ("O usuário surpreendido com droga para consumo pessoal deve ser preso em flagrante.","E","Não se impõe prisão em flagrante; lavra-se termo circunstanciado (art. 48, § 2º)."),
 ("Entregar droga gratuitamente a terceiro pode configurar tráfico.","C","O art. 33 diz “ainda que gratuitamente”."),
 ("A Lei de Drogas fixa a quantidade máxima de droga que caracteriza consumo pessoal.","E","A lei não fixa quantidade; o juiz avalia as circunstâncias (art. 28, § 2º). O critério de 40 g para a maconha veio do STF."),
 ("O tráfico privilegiado exige que o agente seja primário, de bons antecedentes, não se dedique a atividades criminosas nem integre organização criminosa.","C","Art. 33, § 4º."),
 ("Segundo a Súmula Vinculante 63, o tráfico privilegiado é crime hediondo.","E","A súmula afirma o contrário: não é hediondo."),
 ("A associação para o tráfico exige no mínimo quatro pessoas.","E","Exige duas ou mais pessoas (art. 35).")])

# ================================================================ UNIDADE 2 · DESARMAMENTO
opener("02","UNIDADE 2","Estatuto do Desarmamento",["Posse x porte","Crimes com arma de uso permitido","Uso restrito, uso proibido, comércio e tráfico","Porte de arma das guardas municipais"],"U2")

pp = scene3([("POSSE (art. 12)",C['green'],C['greensoft'],"prof",["Arma guardada","em casa ou no","trabalho."],"DENTRO de casa/trabalho"),
 ("PORTE (art. 14)",C['red'],C['redsoft'],"profa",["Arma na cintura,","no carro, na rua,","no ônibus."],"FORA de casa/trabalho"),
 ("DISPARO (art. 15)",C['golddeep'],C['goldsoft'],"prof",["Atira para o alto","na rua, em festa,","em local habitado."],"EM LUGAR HABITADO")], "Situação ilustrada: o lugar onde a arma está decide o crime.")
add(H(2,'Posse x <span class="hl">porte</span>','O registro autoriza a posse; o porte é outra autorização.', "A07") + pp +
 table(["","POSSE","PORTE"],[
  ["Onde","No interior da <b>residência ou domicílio</b>, ou dependência, ou no <b>local de trabalho</b> se o dono for o titular ou responsável legal pelo estabelecimento (art. 5º)","Em qualquer outro lugar: rua, veículo, transporte público"],
  ["Documento","Certificado de <b>registro</b>","Autorização de <b>porte</b>, que é <b>proibido</b> em todo o país, salvo as exceções legais (art. 6º)"],
  ["Imóvel rural (art. 5º, § 5º)","Toda a extensão do imóvel rural é considerada residência (Lei nº 13.870/2019)","—"]],["18%",None,None]))

add(H(2,'Crimes com arma de <span class="hl">uso permitido</span>','Arts. 12 a 15.', "A08") +
 table(["Crime","Conduta (em síntese)","Pena"],[
  ["Posse irregular (art. 12)","Possuir ou manter sob guarda arma, acessório ou munição de uso permitido, em desacordo com a lei, <b>em casa ou no trabalho</b> (se titular ou responsável)","Detenção, 1 a 3 anos, e multa"],
  ["Omissão de cautela (art. 13)","Deixar de tomar as cautelas necessárias para impedir que <b>menor de 18 anos ou pessoa com deficiência mental</b> se apodere da arma","Detenção, 1 a 2 anos, e multa"],
  ["Porte ilegal (art. 14)","Portar, transportar, trazer consigo etc. arma, acessório ou munição de uso permitido, sem autorização","Reclusão, 2 a 4 anos, e multa"],
  ["Disparo (art. 15)","Disparar arma de fogo ou acionar munição em lugar habitado ou em suas adjacências, em via pública ou em direção a ela, desde que a conduta não tenha como finalidade a prática de outro crime","Reclusão, 2 a 4 anos, e multa"]],["22%",None,"22%"]) +
 traduz(p('Note a escala: a <strong>posse</strong> (arma em casa) é punida com <strong>detenção</strong>; o <strong>porte</strong> e o <strong>disparo</strong>, com <strong>reclusão</strong>. A lei pune mais quem leva a arma para a rua, onde o risco para outras pessoas é maior. A omissão de cautela é o único crime <strong>culposo</strong> do Estatuto, segundo a doutrina.')) +
 memo('Posse (12): <strong>detenção 1 a 3</strong>. Omissão de cautela (13): <strong>detenção 1 a 2</strong>. Porte (14) e disparo (15): <strong>reclusão 2 a 4</strong>.') +
 pega('<ul><li>O texto dos arts. 14 e 15 diz que são <b>inafiançáveis</b>, mas o STF, na <b>ADI 3.112</b>, declarou essas vedações inconstitucionais (o Planalto traz a nota "Vide Adin 3.112-1").</li><li>O dono de um <b>comércio</b> que guarda a arma no próprio estabelecimento comete <b>posse</b>; o <b>empregado</b> que a leva ao trabalho comete <b>porte</b>.</li></ul>'))

add(H(2,'Uso restrito, uso proibido, <span class="hl">comércio e tráfico</span>','Arts. 16 a 21-A.', "A09") +
 table(["Crime","Conduta (em síntese)","Pena"],[
  ["Posse ou porte de arma de uso restrito (art. 16, caput)","Possuir, portar, adquirir, transportar etc. arma, acessório ou munição de uso restrito, sem autorização","Reclusão, 3 a 6 anos, e multa"],
  ["Figuras equiparadas (art. 16, § 1º)","Suprimir ou alterar marca ou numeração; modificar a arma; possuir artefato explosivo ou incendiário; portar arma com numeração raspada; vender arma ou munição a <b>criança ou adolescente</b>; produzir ou recarregar munição sem autorização","Mesma do caput"],
  ["Arma de uso proibido (art. 16, § 2º)","Condutas do caput ou do § 1º envolvendo arma de uso proibido","Reclusão, 4 a 12 anos"],
  ["Comércio ilegal (art. 17)","Adquirir, vender, expor à venda etc., no exercício de atividade comercial ou industrial, inclusive clandestina ou em residência","Reclusão, 6 a 12 anos, e multa"],
  ["Tráfico internacional (art. 18)","Importar, exportar ou favorecer a entrada ou saída de arma, acessório ou munição, sem autorização","Reclusão, 8 a 16 anos, e multa"]],["26%",None,"22%"]) +
 table(["Regra","Conteúdo"],[
  ["Aumento de metade (arts. 19 e 20)","Arts. 17 e 18 com arma de uso proibido ou restrito; arts. 14 a 18 praticados por integrante dos órgãos e empresas dos arts. 6º, 7º e 8º, ou por reincidente específico"],
  ["Aumento de 2/3 (art. 21-A, Lei nº 15.358/2026)","Arts. 12, 14 e 16 praticados em conjunto com crime da Lei de Drogas, ou ligados diretamente ao tráfico"],
  ["Hediondos (Lei nº 8.072/1990)","Posse ou porte de arma de <b>uso proibido</b> (art. 16), comércio ilegal (art. 17) e tráfico internacional (art. 18)"]],["30%",None]) +
 memo('Restrito: <strong>3 a 6</strong>. Proibido: <strong>4 a 12</strong> (e hediondo). Comércio: <strong>6 a 12</strong>. Tráfico internacional: <strong>8 a 16</strong>. Numeração raspada é crime do art. 16, § 1º, mesmo se a arma for de uso permitido.'))

add(H(2,'Porte de arma das <span class="hl">guardas municipais</span>','Art. 6º, III e IV, e as decisões do STF.', "A10") +
 table(["Ponto","Situação atual"],[
  ["Texto original do art. 6º","Porte para guardas de capitais e municípios com mais de 500 mil habitantes (inciso III) e, em serviço, para municípios entre 50 mil e 500 mil (inciso IV)"],
  ["Decisão do STF (2021)","Nas <b>ADIs 5.538 e 5.948</b> e na <b>ADC 38</b>, o STF considerou inconstitucional o critério populacional e garantiu o porte aos integrantes das guardas municipais de <b>todos</b> os municípios. O Planalto registra: “Expressões declaradas inconstitucionais pela ADIN 5538” (inciso III) e “Declarado inconstitucional pela ADIN 5538” (inciso IV)"],
  ["Porte fora de serviço","Ainda há divergência sobre o alcance; nova ação (ADI 7.717) tramitava no STF"],
  ["Atuação das guardas (Tema 656, 2025)","O STF considerou constitucional a atuação das guardas em ações de <b>segurança urbana</b>, inclusive <b>policiamento ostensivo e comunitário</b>, excluída a <b>polícia judiciária</b> (investigação)"]],["26%",None]) +
 ex(p('Uma questão afirma: "Guardas municipais de cidades com menos de 50 mil habitantes não podem ter porte de arma de fogo, segundo o Estatuto." É uma pegadinha: o texto original fazia essa distinção, mas o STF a declarou <b>inconstitucional</b>. Hoje, o critério populacional não vale.')) +
 memo('Porte das guardas: <strong>todos os municípios</strong>, sem critério populacional (STF, 2021). Guardas podem fazer <strong>policiamento ostensivo e comunitário</strong>, mas <strong>não investigam</strong> (Tema 656).'))

treino(2, [
 ("Manter arma de uso permitido em casa, sem registro, configura porte ilegal de arma.","E","Configura posse irregular (art. 12)."),
 ("A pena do porte ilegal de arma de fogo de uso permitido é de reclusão, de 2 a 4 anos, e multa.","C","Art. 14."),
 ("Portar arma de uso permitido com numeração raspada configura o crime do art. 16, § 1º, do Estatuto.","C","Art. 16, § 1º, IV."),
 ("A posse ilegal de arma de fogo de uso proibido é crime hediondo.","C","Lei nº 8.072/1990, art. 1º, parágrafo único, II."),
 ("Segundo o STF, apenas guardas municipais de cidades com mais de 50 mil habitantes podem ter porte de arma.","E","O STF declarou o critério populacional inconstitucional (ADIs 5.538 e 5.948)."),
 ("Disparar arma de fogo em via pública, sem a finalidade de praticar outro crime, configura o crime do art. 15 do Estatuto.","C","Disparo de arma de fogo.")])

# ================================================================ UNIDADE 3 · HEDIONDOS E TORTURA
opener("03","UNIDADE 3","Crimes hediondos e tortura",["O que é crime hediondo e o rol do art. 1º","Equiparados e consequências","Tortura: as espécies","Tortura: omissão, aumentos e efeitos"],"U3")

add(H(3,'Crime hediondo e o <span class="hl">rol do art. 1º</span>','Hediondo é o que a lei diz que é.', "A11") +
 traduz(p('O Brasil adota o <strong>critério legal</strong>: só é hediondo o crime que está na <strong>lista</strong> da Lei nº 8.072/1990, consumado ou tentado. O juiz não pode considerar hediondo um crime fora da lista, por mais grave que seja. A lista muda com frequência: foi alterada em <strong>2024, 2025 e 2026</strong>.')) +
 table(["Inciso","Crime hediondo (Código Penal), em síntese"],[
  ["I","Homicídio em atividade típica de grupo de extermínio, ainda que por um só agente, e homicídio qualificado (art. 121, § 2º)"],
  ["I-A","Lesão corporal dolosa gravíssima ou seguida de morte contra agentes de segurança pública, do sistema prisional, da Força Nacional, membros do Judiciário, MP, Defensoria, Advocacia Pública e oficiais de justiça (ou familiares), em razão da função, ou nas dependências de instituição de ensino"],
  ["I-B e I-C","<b>Feminicídio</b> (art. 121-A) e <b>vicaricídio</b> (art. 121-B, Lei nº 15.384/2026)"],
  ["II","Roubo com restrição de liberdade da vítima, com arma de fogo (ou de uso proibido ou restrito) ou com resultado lesão grave ou morte"],
  ["III e IV","Extorsão qualificada pela restrição da liberdade, lesão ou morte; extorsão mediante sequestro (simples e qualificada)"],
  ["V e VI","Estupro e estupro de vulnerável"],
  ["VII e VII-B","Epidemia com resultado morte; falsificação de produto destinado a fins terapêuticos ou medicinais"],
  ["VIII","Favorecimento da prostituição ou exploração sexual de criança, adolescente ou vulnerável"],
  ["IX","Furto qualificado pelo emprego de explosivo"],
  ["X a XII","Induzimento ao suicídio ou automutilação pela internet; sequestro de menor de 18 anos; tráfico de pessoas contra criança ou adolescente (Lei nº 14.811/2024)"]],["14%",None]))

add(pratica_title("Também são hediondos (parágrafo único)") +
 table(["Inciso","Crime de lei especial, em síntese"],[
  ["I","Genocídio (Lei nº 2.889/1956)"],
  ["II a IV","Posse ou porte de arma de <b>uso proibido</b>, comércio ilegal e tráfico internacional de arma (Estatuto do Desarmamento)"],
  ["V","Organização criminosa direcionada à prática de crime hediondo ou equiparado"],
  ["VI","Crimes do Código Penal Militar idênticos aos do art. 1º (Lei nº 14.688/2023)"],
  ["VII","Crimes do ECA ligados a material de abuso sexual infantil e exploração (redação da Lei nº 15.487/2026)"],
  ["VIII","Crimes de domínio social estruturado e de favorecimento ao domínio social estruturado (Lei nº 15.358/2026)"]],["14%",None]) +
 ex(p('Furto simples, homicídio simples (fora de grupo de extermínio) e roubo simples <b>não</b> são hediondos, porque não estão na lista. Já o roubo com emprego de arma de fogo <b>é</b>, desde a Lei nº 13.964/2019. O porte de arma de uso <b>restrito</b> não é hediondo; o de uso <b>proibido</b> é.')) +
 pega('<ul><li>Homicídio <b>simples</b> só é hediondo se praticado em atividade típica de <b>grupo de extermínio</b>.</li><li>O rol vale para crimes <b>consumados ou tentados</b>.</li><li>Arma de uso <b>restrito</b> x <b>proibido</b>: só a de uso proibido entra na lista.</li></ul>'))

add(H(3,'Equiparados e <span class="hl">consequências</span>','Art. 2º: os "TTT" e as restrições.', "A12") +
 flow([("pill",["TRÁFICO","de drogas"]),("bolt",["TORTURA","Lei 9.455"]),("alert",["TERRORISMO","Lei 13.260"]),("gavel",["EQUIPARADOS","a hediondos","(CF, art. 5º, XLIII)"])],
      "Os três “T”: não são hediondos, mas recebem o mesmo tratamento rigoroso.", colors=colors("r","o","n","b")) +
 table(["Consequência (art. 2º)","Regra"],[
  ["Insuscetíveis de","<b>Anistia, graça e indulto</b> (I) e <b>fiança</b> (II)"],
  ["Regime inicial","Inicialmente <b>fechado</b> (§ 1º); o STF, porém, declarou inconstitucional a obrigatoriedade desse regime inicial (HC 111.840, 2012)"],
  ["Progressão","O antigo § 2º (2/5 e 3/5) foi <b>revogado</b> pela Lei nº 13.964/2019; hoje as frações estão no art. 112 da Lei de Execução Penal"],
  ["Apelar em liberdade (§ 3º)","O juiz decide fundamentadamente"],
  ["Prisão temporária (§ 4º)","<b>30 dias</b>, prorrogável por igual período em caso de extrema e comprovada necessidade"],
  ["Associação (art. 8º)","Associação criminosa para hediondos, tortura, tráfico ou terrorismo: reclusão, 3 a 6 anos"]],["30%",None]) +
 memo('Hediondos e equiparados: <strong>sem anistia, graça, indulto e fiança</strong>. Temporária: <strong>30 + 30 dias</strong>. Liberdade provisória <strong>sem fiança</strong> é possível (a vedação saiu da lei em 2007).'))

add(H(3,'<span class="hl">Tortura</span>: as espécies do art. 1º','Lei nº 9.455/1997.', "A13") +
 table(["Espécie","Conduta (em síntese)","Pena"],[
  ["Tortura-prova (I, a)","Constranger alguém com violência ou grave ameaça, causando sofrimento físico ou mental, para obter <b>informação, declaração ou confissão</b> da vítima ou de terceiro","Reclusão, 2 a 8 anos"],
  ["Tortura para crime (I, b)","Para provocar <b>ação ou omissão de natureza criminosa</b>","Reclusão, 2 a 8 anos"],
  ["Tortura discriminatória (I, c)","Em razão de <b>discriminação racial ou religiosa</b>","Reclusão, 2 a 8 anos"],
  ["Tortura-castigo (II)","Submeter alguém, sob sua <b>guarda, poder ou autoridade</b>, a <b>intenso</b> sofrimento físico ou mental, como castigo pessoal ou medida preventiva","Reclusão, 2 a 8 anos"],
  ["Tortura contra a mulher (III, Lei nº 15.410/2026)","Submeter mulher, de forma <b>reiterada</b>, a sofrimento intenso no contexto de <b>violência doméstica e familiar</b>","Reclusão, 2 a 8 anos"],
  ["Tortura do preso (§ 1º)","Submeter pessoa presa ou sujeita a medida de segurança a sofrimento por ato não previsto em lei ou não resultante de medida legal","Reclusão, 2 a 8 anos"]],["24%",None,"16%"]) +
 traduz(p('A tortura <strong>não é crime só de policial</strong>: qualquer pessoa pode praticá-la (crime comum). Ser agente público <strong>aumenta</strong> a pena. A exceção é a tortura-castigo (inciso II), que exige uma relação de <strong>guarda, poder ou autoridade</strong> sobre a vítima, como pais, cuidadores ou agentes prisionais.'),"profa") +
 memo('Tortura: em regra, <strong>crime comum</strong>. Pena básica: <strong>reclusão de 2 a 8 anos</strong>. Novidade: <strong>inciso III</strong> (mulher, violência doméstica, Lei nº 15.410/2026).'))

add(H(3,'Tortura: omissão, <span class="hl">aumentos e efeitos</span>','Art. 1º, §§ 2º a 7º.', "A14") +
 table(["Regra","Conteúdo"],[
  ["Omissão (§ 2º)","Quem se omite quando tinha o <b>dever de evitar ou apurar</b> a tortura: <b>detenção, 1 a 4 anos</b>"],
  ["Resultado (§ 3º)","Lesão grave ou gravíssima: reclusão, 4 a 10 anos; morte: reclusão, 8 a 16 anos"],
  ["Aumento de 1/6 a 1/3 (§ 4º)","I - agente público; II - contra criança, gestante, pessoa com deficiência, adolescente ou maior de 60 anos; III - mediante sequestro"],
  ["Efeitos (§ 5º)","Perda do cargo, função ou emprego público e interdição para seu exercício pelo <b>dobro</b> do prazo da pena aplicada"],
  ["Fiança e clemência (§ 6º)","Inafiançável e insuscetível de graça ou anistia"],
  ["Regime (§ 7º)","Inicia em regime <b>fechado</b>, salvo a hipótese do § 2º (omissão)"],
  ["Extraterritorialidade (art. 2º)","A lei se aplica mesmo fora do território nacional, se a vítima for brasileira ou o agente estiver em local sob jurisdição brasileira"]],["28%",None]) +
 ex(p('Durante uma abordagem, dois policiais afogam repetidamente um suspeito num balde para que ele revele onde escondeu a arma (<b>tortura-prova</b>, com aumento por serem agentes públicos). O delegado que assiste a tudo e nada faz responde pelo <b>§ 2º</b> (omissão). Condenados, os policiais perdem o cargo, e a perda é <b>automática</b>, segundo o entendimento predominante.')) +
 pega('<ul><li>A omissão do § 2º tem pena de <b>detenção</b> e é a única espécie que <b>não</b> começa obrigatoriamente no regime fechado.</li><li>A tortura é insuscetível de <b>graça e anistia</b> pela Lei nº 9.455; a vedação de <b>indulto</b> vem da Lei dos Crimes Hediondos (art. 2º).</li><li>Tortura-castigo exige sofrimento <b>intenso</b>. Um castigo com abuso dos meios de correção, sem sofrimento intenso, pode ser o crime de <b>maus-tratos</b> do CP.</li></ul>'))

treino(3, [
 ("O furto simples é crime hediondo.","E","Só o furto qualificado pelo emprego de explosivo está na lista (art. 1º, IX)."),
 ("O feminicídio é crime hediondo.","C","Art. 1º, I-B (Lei nº 14.994/2024)."),
 ("A prisão temporária nos crimes hediondos tem prazo de 30 dias, prorrogável por igual período.","C","Art. 2º, § 4º."),
 ("A tortura é crime próprio de agente público.","E","Em regra, é crime comum; ser agente público aumenta a pena (§ 4º, I)."),
 ("Quem se omite diante da tortura, tendo o dever de evitá-la, responde com pena de detenção de 1 a 4 anos.","C","Art. 1º, § 2º."),
 ("A condenação por tortura acarreta a perda do cargo e a interdição para seu exercício pelo dobro do prazo da pena aplicada.","C","Art. 1º, § 5º.")])

# ================================================================ UNIDADE 4 · MARIA DA PENHA
opener("04","UNIDADE 4","Lei Maria da Penha",["Violência doméstica: conceito e formas","Atendimento policial e medidas protetivas","Descumprimento e pontos processuais"],"U4")

def wrap(t, n):
    out, cur = [], ""
    for w in t.split():
        if len(cur)+len(w)+1 > n and cur: out.append(cur); cur = w
        else: cur = (cur+" "+w).strip()
    return out + [cur]
def formas():
    it = [("person","FÍSICA","ofende a integridade","ou a saúde corporal",C['red'],C['redsoft']),("brain","PSICOLÓGICA","dano emocional, controle,","humilhação, isolamento",C['golddeep'],C['goldsoft']),
          ("alert","SEXUAL","presenciar, manter ou participar","de relação sexual não desejada",C['navy'],NV),("wallet","PATRIMONIAL","reter, subtrair, destruir","bens, documentos, valores",C['green'],C['greensoft']),
          ("speech","MORAL","calúnia, difamação","ou injúria",C['blue'],C['sky']),("people","VICÁRIA","atinge filhos, parentes ou","rede de apoio para ferir a mulher",C['muted'],'#eef0f3')]
    s = f'<figure><svg viewBox="0 0 640 170" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    for i,(ic,t,a,b,fg,bg) in enumerate(it):
        x = 2+i*106.5
        s += f'<rect x="{x}" y="4" width="100" height="160" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.4"/><g style="color:{fg}"><use href="#i-{ic}" x="{x+32}" y="16" width="36" height="36"/></g>'
        s += f'<text x="{x+50}" y="80" text-anchor="middle" font-size="11.5" font-weight="900" fill="{fg}">{t}</text>'
        s += "".join(f'<text x="{x+50}" y="{102+k*13}" text-anchor="middle" font-size="8.4" fill="{C["ink"]}">{w}</text>' for k,w in enumerate(wrap(a+" "+b, 20)))
    return s + '</svg><figcaption>Art. 7º: as seis formas de violência doméstica e familiar contra a mulher; a vicária foi incluída pela Lei nº 15.384/2026 (rol exemplificativo: "entre outras").</figcaption></figure>'

add(H(4,'Violência doméstica: <span class="hl">conceito e formas</span>','Arts. 5º e 7º da Lei nº 11.340/2006.', "A15") +
 lei(L("11.340/2006","Art. 5º, caput"),'<p>Para os efeitos desta Lei, configura violência doméstica e familiar contra a mulher qualquer ação ou omissão baseada no gênero que lhe cause morte, lesão, sofrimento físico, sexual ou psicológico e dano moral ou patrimonial: [...]</p>') +
 table(["Âmbito (art. 5º)","O que significa"],[
  ["I - Unidade doméstica","Espaço de convívio permanente de pessoas, com ou sem vínculo familiar, inclusive as esporadicamente agregadas"],
  ["II - Família","Indivíduos que são ou se consideram aparentados, por laços naturais, afinidade ou vontade expressa"],
  ["III - Relação íntima de afeto","O agressor convive ou conviveu com a ofendida, <b>independentemente de coabitação</b> (ex.: namoro, ex-namoro)"],
  ["Parágrafo único","As relações independem de <b>orientação sexual</b>"]],["30%",None]) +
 formas())

atencao(
 table(["Pergunta de prova","Resposta"],[
  ["A lei protege qualquer pessoa agredida em casa?","Não: protege a <b>mulher</b>, em violência <b>baseada no gênero</b>"],
  ["O agressor precisa ser homem?","Não: pode ser mulher (ex.: relação entre duas mulheres, mãe e filha)"],
  ["Precisa morar junto?","Não: na relação íntima de afeto, independe de coabitação"],
  ["Mulher trans é protegida?","A jurisprudência do STJ reconhece a aplicação da lei às mulheres trans (REsp 1.977.124, 2022)"]],["46%",None]) +
 ex(p('Um ex-namorado, que nunca morou com a vítima, passa a ameaçá-la e a divulgar mentiras sobre ela nas redes sociais depois do término. Há violência doméstica e familiar no âmbito da <b>relação íntima de afeto</b>, nas formas <b>psicológica</b> e <b>moral</b>, ainda que não tenham morado juntos.')) +
 pega('<ul><li>A Lei Maria da Penha não cria, em regra, crimes novos: ela traz <b>medidas de proteção</b> e regras processuais. Os crimes estão no CP e em outras leis.</li><li>O rol do art. 7º é <b>exemplificativo</b> ("entre outras").</li><li>Violência <b>patrimonial</b> também é violência doméstica: reter documentos da mulher, por exemplo.</li><li>Novidade de 2026: a <b>violência vicária</b> (art. 7º, VI) é a violência contra filhos, parentes ou pessoas próximas da mulher, praticada para atingi-la.</li></ul>'),
 ["baseada no gênero","relação íntima de afeto","independe de coabitação","rol exemplificativo","violência vicária"])

add(H(4,'Atendimento policial e <span class="hl">medidas protetivas</span>','Arts. 10 a 12-C e 18 a 24.', "A16") +
 table(["Regra","Conteúdo (em síntese)"],[
  ["Atendimento (arts. 10 a 12)","A autoridade policial que tomar conhecimento deve adotar providências imediatas: garantir proteção, encaminhar a vítima a atendimento, acompanhá-la para retirar pertences, ouvir a ofendida, colher provas e remeter ao juiz, em <b>48 horas</b>, o pedido de medidas protetivas"],
  ["Afastamento imediato do lar (art. 12-C)","Havendo risco atual ou iminente à vida ou à integridade física, sexual, psicológica, moral ou patrimonial (redação da Lei nº 15.411/2026), o agressor é afastado do lar pela <b>autoridade judicial</b>; pelo <b>delegado</b>, se o município não for sede de comarca; ou pelo <b>policial</b>, se também não houver delegado disponível. O juiz é comunicado em 24 horas"],
  ["Monitoramento eletrônico (art. 12-D e art. 22, VIII, Lei nº 15.383/2026)","Em risco à integridade física ou psicológica, o juiz ou, onde não houver sede de comarca, o delegado determina o monitoramento eletrônico imediato do agressor, com alerta à vítima e à polícia se ele invadir a área proibida"],
  ["Concessão (arts. 18 e 19)","O juiz decide em <b>48 horas</b>; as medidas podem ser concedidas de imediato, sem ouvir as partes, e <b>independem</b> de tipificação penal, de ação penal ou cível, de boletim de ocorrência ou de inquérito; vigoram enquanto persistir o risco (§§ 4º a 6º, Lei nº 14.550/2023)"],
  ["Medidas que obrigam o agressor (art. 22)","Suspensão da posse ou restrição do porte de armas; afastamento do lar; proibição de aproximação e de contato; proibição de frequentar lugares; restrição de visitas aos filhos; alimentos; programas de reeducação; acompanhamento psicossocial; monitoramento eletrônico"],
  ["Medidas à ofendida (arts. 23 e 24)","Encaminhamento a programa de proteção; recondução ao domicílio; afastamento da ofendida sem prejuízo de direitos; proteção patrimonial; matrícula dos dependentes em escola próxima; auxílio-aluguel por até 6 meses"]],["28%",None]) +
 flow([("phone",["CHAMADO","190 / 153"]),("shield",["PROTEÇÃO","imediata"]),("home2",["AFASTAMENTO","do lar","(art. 12-C)"]),("gavel",["JUIZ: 48h","medidas","protetivas"])],
      "Do chamado à medida protetiva: o papel do agente de segurança.", colors=colors("n","b","o","r")))

add(H(4,'Descumprimento e <span class="hl">pontos processuais</span>','O que muda no processo quando há violência doméstica.', "A17") +
 lembre(p('<strong>Art. 24-A (Lei nº 11.340/2006):</strong> "Descumprir decisão judicial que defere medidas protetivas de urgência previstas nesta Lei." Pena atual: <strong>reclusão, de 2 a 5 anos, e multa</strong> (redação da Lei nº 14.994/2024). A pena aumenta de <strong>1/3 até a metade</strong> se o descumprimento envolver as áreas de exclusão do monitoramento ou a retirada, violação ou alteração da tornozeleira sem autorização judicial (§ 4º, Lei nº 15.383/2026). O crime independe da competência civil ou criminal do juiz, e, na prisão em flagrante, <strong>só o juiz pode conceder fiança</strong>. O Código Penal também passou a ter um tipo com conteúdo semelhante, o art. 338-A (Lei nº 15.280/2025), com a mesma pena; o texto da Lei Maria da Penha, conferido no Planalto, mantém o art. 24-A em vigor.'), "Crime de descumprimento de medida protetiva") +
 table(["Regra","Conteúdo"],[
  ["Renúncia à representação (art. 16)","Nos crimes de ação pública condicionada, só é admitida <b>perante o juiz</b>, em audiência designada para esse fim, antes do recebimento da denúncia, ouvido o MP"],
  ["Prazo para representar (art. 16-A, Lei nº 15.438/2026)","A vítima decai do direito de queixa ou de representação se não o exercer em <b>12 meses</b>, contados de quando soube quem é o autor"],
  ["Sigilo (art. 17-A, Lei nº 14.857/2024)","O nome da vítima fica em sigilo nos processos; o sigilo não alcança o nome do autor"],
  ["Penas proibidas (art. 17)","É vedada a aplicação de pena de <b>cesta básica</b> ou outras de prestação pecuniária, e a substituição por pena que implique pagamento isolado de multa"],
  ["Lei nº 9.099/1995 (art. 41)","<b>Não se aplica</b> aos crimes praticados com violência doméstica e familiar contra a mulher, independentemente da pena (sem transação penal ou suspensão condicional do processo)"],
  ["Prisão preventiva (art. 20)","Cabe em qualquer fase do inquérito ou da instrução, decretada pelo juiz"]],["30%",None]) +
 memo('Renúncia: <strong>só perante o juiz</strong>. Proibido: <strong>cesta básica</strong> e multa isolada. Lei nº 9.099: <strong>não se aplica</strong> (art. 41).'))

treino(4, [
 ("A Lei Maria da Penha exige que agressor e vítima morem juntos.","E","Na relação íntima de afeto, independe de coabitação (art. 5º, III)."),
 ("A violência patrimonial é uma das formas de violência doméstica previstas no art. 7º.","C","Art. 7º, IV."),
 ("As medidas protetivas de urgência dependem da instauração de inquérito policial.","E","Independem de tipificação penal, de boletim de ocorrência e de inquérito (art. 19)."),
 ("A renúncia à representação, nos crimes da Lei Maria da Penha, pode ser feita na delegacia.","E","Só perante o juiz, em audiência (art. 16)."),
 ("É vedada a aplicação de pena de cesta básica nos casos de violência doméstica e familiar contra a mulher.","C","Art. 17."),
 ("A Lei nº 9.099/1995 não se aplica aos crimes praticados com violência doméstica e familiar contra a mulher.","C","Art. 41.")])

# ================================================================ UNIDADE 5 · ABUSO E ORCRIM
opener("05","UNIDADE 5","Abuso de autoridade e organizações criminosas",["Abuso de autoridade: regras gerais","Crimes de abuso mais cobrados","Organização criminosa","Associação criminosa x associação para o tráfico x organização criminosa"],"U5")

add(H(5,'Abuso de autoridade: <span class="hl">regras gerais</span>','Lei nº 13.869/2019.', "A18") +
 lei(L("13.869/2019","Art. 1º, §§ 1º e 2º (em síntese e trechos)"),'<p>§ 1º As condutas só constituem crime quando praticadas pelo agente "com a finalidade específica de prejudicar outrem ou beneficiar a si mesmo ou a terceiro, ou, ainda, por mero capricho ou satisfação pessoal".<br>§ 2º "A divergência na interpretação de lei ou na avaliação de fatos e provas não configura abuso de autoridade."</p>') +
 table(["Ponto","Regra (em síntese)"],[
  ["Quem pratica (art. 2º)","Qualquer <b>agente público</b>, servidor ou não, de qualquer Poder e esfera: servidores e militares, membros do Legislativo, do Executivo, do Judiciário, do MP e dos tribunais de contas; quem exerce função, ainda que transitória ou sem remuneração"],
  ["Ação penal (art. 3º)","<b>Pública incondicionada</b>; admite ação privada subsidiária se o MP não agir no prazo (6 meses para propor)"],
  ["Efeitos da condenação (art. 4º)","Indenizar o dano; <b>inabilitação</b> para cargo por 1 a 5 anos; <b>perda</b> do cargo. Inabilitação e perda exigem <b>reincidência</b> em abuso de autoridade e <b>não são automáticas</b>: o juiz deve declará-las motivadamente"],
  ["Penas restritivas (art. 5º)","Prestação de serviços; suspensão do cargo por 1 a 6 meses, com perda dos vencimentos"],
  ["Revogação (art. 44)","Revogou a antiga Lei nº 4.898/1965 e o art. 350 do Código Penal"]],["26%",None]) +
 memo('Sem a <strong>finalidade específica</strong> do § 1º, não há crime de abuso. Divergência de interpretação <strong>não é abuso</strong>. Perda do cargo: só com <strong>reincidência</strong> e <strong>não automática</strong>.'))

add(H(5,'Crimes de abuso <span class="hl">mais cobrados</span>','Uma seleção dos tipos ligados à atuação policial.', "A19") +
 table(["Art.","Conduta (em síntese)","Pena"],[
  ["9","Decretar medida de privação da liberdade em manifesta desconformidade com as hipóteses legais","Detenção, 1 a 4 anos, e multa"],
  ["12","Deixar injustificadamente de comunicar prisão em flagrante à autoridade judiciária no prazo legal","Detenção, 6 meses a 2 anos, e multa"],
  ["13","Constranger o preso, com violência, grave ameaça ou redução de sua capacidade de resistência, a exibir-se à curiosidade pública, a situação vexatória ou a produzir prova contra si ou contra terceiro","Detenção, 1 a 4 anos, e multa, sem prejuízo da pena da violência"],
  ["16","Deixar de identificar-se ou identificar-se falsamente ao preso por ocasião de sua captura","Detenção, 6 meses a 2 anos, e multa"],
  ["18","Submeter o preso a interrogatório policial durante o período de repouso noturno, salvo flagrante ou consentimento com assistência","Detenção, 6 meses a 2 anos, e multa"],
  ["21","Manter presos de ambos os sexos na mesma cela, ou criança ou adolescente com maiores","Detenção, 1 a 4 anos, e multa"],
  ["22","Invadir ou adentrar imóvel alheio sem determinação judicial ou fora das condições legais; § 1º, III: cumprir mandado de busca domiciliar após as <b>21h</b> ou antes das <b>5h</b>","Detenção, 1 a 4 anos, e multa"],
  ["25","Obter prova, em investigação ou fiscalização, por meio manifestamente ilícito","Detenção, 1 a 4 anos, e multa"],
  ["33","Exigir informação ou cumprimento de obrigação sem expresso amparo legal","Detenção, 6 meses a 2 anos, e multa"],
  ["38","Antecipar, o responsável pelas investigações, por meio de comunicação (inclusive redes sociais), atribuição de culpa antes de concluídas as apurações","Detenção, 6 meses a 2 anos, e multa"]],["8%",None,"24%"]))

atencao(
 lembre(p('O art. 22, § 2º, diz que <strong>não há crime</strong> se o ingresso no imóvel for para <strong>prestar socorro</strong>, ou quando houver <strong>fundados indícios</strong> que indiquem a necessidade do ingresso em razão de situação de <strong>flagrante delito</strong> ou de <strong>desastre</strong>.'), "Quando entrar na casa não é abuso") +
 ex(p('Um guarda municipal, sem nenhum indício, exige que um ambulante entregue o celular desbloqueado "para conferir": pode configurar o <b>art. 33</b> (exigir sem amparo legal), se houver a finalidade específica do art. 1º, § 1º. Já o agente que ouve gritos de socorro e entra na casa para salvar a vítima <b>não</b> comete abuso (art. 22, § 2º).')) +
 pega('<ul><li>O mandado de busca domiciliar só pode ser cumprido das <b>5h às 21h</b>: cumpri-lo fora desse horário é crime (art. 22, § 1º, III).</li><li>Os crimes de abuso são <b>dolosos</b> e exigem finalidade específica: não existe abuso de autoridade <b>culposo</b>.</li><li>Alguns artigos foram <b>vetados</b> (11, 14, 17, 26, 34 e 35) e não existem como crime.</li></ul>'),
 ["finalidade específica","mero capricho","ação pública incondicionada","reincidência","5h às 21h","flagrante delito"])

add(H(5,'Organização <span class="hl">criminosa</span>','Lei nº 12.850/2013.', "A20") +
 lei(L("12.850/2013","Art. 1º, § 1º (em síntese)"),'<p>"Considera-se organização criminosa a associação de 4 (quatro) ou mais pessoas" estruturalmente ordenada e caracterizada pela divisão de tarefas, ainda que informalmente, com objetivo de obter vantagem de qualquer natureza, mediante a prática de infrações penais com penas máximas superiores a 4 anos, ou de caráter transnacional.</p>') +
 cards([("#4","4 ou mais pessoas","Número mínimo de integrantes."),("#E","Estrutura e divisão de tarefas","Ainda que informal."),("#V","Vantagem de qualquer natureza","Direta ou indireta."),("#P","Penas máximas acima de 4 anos","Ou infrações transnacionais.")],4) +
 memo('Organização criminosa = <strong>4 ou mais</strong> + <strong>estrutura</strong> + <strong>divisão de tarefas</strong> + infrações com pena máxima <strong>acima de 4 anos</strong> (ou transnacionais).'))
atencao(table(["Ponto","Regra (em síntese)"],[
  ["Crime (art. 2º)","Promover, constituir, financiar ou integrar organização criminosa: <b>reclusão, 3 a 8 anos, e multa</b>, sem prejuízo das penas dos demais crimes"],
  ["Aumentos","Até a metade com emprego de arma de fogo (§ 2º); pena agravada para quem exerce o comando (§ 3º); 1/6 a 2/3 com participação de criança ou adolescente, funcionário público, envio de produto ao exterior, conexão com outras organizações ou transnacionalidade (§ 4º)"],
  ["Meios de prova (art. 3º)","Colaboração premiada; captação ambiental; ação controlada; acesso a registros; interceptação; quebra de sigilos; infiltração de agentes; cooperação entre órgãos"],
  ["Novidades (Lei nº 15.245/2025)","Arts. 21-A (obstrução de ações contra o crime organizado) e 21-B (conspiração): reclusão, 4 a 12 anos, e multa"]],["26%",None]) +
 pega('<ul><li>A divisão de tarefas pode ser <b>informal</b>: não se exige estatuto, hierarquia escrita ou nome.</li><li>Infrações com pena máxima de <b>exatamente 4 anos</b> não bastam: a lei exige pena máxima <b>superior</b> a 4 anos (salvo caráter transnacional).</li><li>A pena da organização criminosa é aplicada <b>sem prejuízo</b> das penas dos crimes praticados pelo grupo.</li></ul>'),
 ["4 ou mais pessoas","divisão de tarefas","pena máxima superior a 4 anos","colaboração premiada","infiltração de agentes","Lei nº 15.245/2025"])

add(H(5,'Associação criminosa x tráfico x <span class="hl">organização criminosa</span>','Conte as pessoas e veja a finalidade.', "A21") +
 table(["","ASSOCIAÇÃO CRIMINOSA (CP, art. 288)","ASSOCIAÇÃO PARA O TRÁFICO (Drogas, art. 35)","ORGANIZAÇÃO CRIMINOSA (Lei 12.850, art. 2º)"],[
  ["Mínimo de pessoas","<b>3</b>","<b>2</b>","<b>4</b>"],
  ["Finalidade","Cometer crimes (quaisquer)","Tráfico (arts. 33, caput e § 1º, e 34)","Infrações com pena máxima acima de 4 anos ou transnacionais"],
  ["Estrutura","Basta o vínculo associativo","Basta o vínculo associativo (estável, segundo a jurisprudência)","Estrutura ordenada e <b>divisão de tarefas</b>"],
  ["Pena","Reclusão, 1 a 3 anos","Reclusão, 3 a 10 anos, e multa","Reclusão, 3 a 8 anos, e multa"]],["16%",None,None,None]) +
 flow([("people",["2 PESSOAS","tráfico","art. 35"]),("people",["3 PESSOAS","crimes em geral","CP, art. 288"]),("sitemap",["4 PESSOAS","estrutura +","tarefas · Lei 12.850"])],
      "Regra de memória: 2 (tráfico) · 3 (CP) · 4 (organização criminosa).", colors=colors("r","o","n")) +
 memo('<strong>2-3-4</strong>: associação para o tráfico (2), associação criminosa (3), organização criminosa (4). Organização criminosa exige <strong>estrutura e divisão de tarefas</strong>.'))

treino(5, [
 ("Para configurar abuso de autoridade, basta que o agente pratique a conduta descrita na lei, independentemente de finalidade especial.","E","Exige finalidade específica de prejudicar, beneficiar ou mero capricho (art. 1º, § 1º)."),
 ("A divergência na interpretação de lei não configura abuso de autoridade.","C","Art. 1º, § 2º."),
 ("A perda do cargo é efeito automático de qualquer condenação por abuso de autoridade.","E","Exige reincidência e declaração motivada na sentença (art. 4º, parágrafo único)."),
 ("Cumprir mandado de busca domiciliar após as 21h ou antes das 5h pode configurar crime de abuso de autoridade.","C","Art. 22, § 1º, III."),
 ("A organização criminosa exige a associação de três ou mais pessoas.","E","Exige quatro ou mais (art. 1º, § 1º)."),
 ("Os crimes de abuso de autoridade são de ação penal pública incondicionada.","C","Art. 3º.")])

# ================================================================ REVISÃO
mapa = f'''<figure><svg viewBox="0 0 640 470" width="580" xmlns="http://www.w3.org/2000/svg" font-family="Inter">
<g stroke="#b9b3ad" stroke-width="2.5" fill="none"><path d="M320 235 L150 70"/><path d="M320 235 L490 70"/><path d="M320 235 L120 235"/><path d="M320 235 L520 235"/><path d="M320 235 L150 400"/><path d="M320 235 L490 400"/></g>
<circle cx="320" cy="235" r="74" fill="{C['navy']}"/><text x="320" y="225" text-anchor="middle" fill="{C['gold']}" font-weight="900" font-size="13">LEGISLAÇÃO</text>
<text x="320" y="245" text-anchor="middle" fill="#fff" font-weight="900" font-size="15">PENAL</text><text x="320" y="263" text-anchor="middle" fill="#fff" font-weight="900" font-size="15">ESPECIAL</text>
''' + "".join(
 f'<rect x="{x-100}" y="{y-40}" width="200" height="80" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x}" y="{y-16}" text-anchor="middle" font-weight="900" font-size="12.5" fill="{fg}">{t}</text>'
 + "".join(f'<text x="{x}" y="{y+4+i*15}" text-anchor="middle" font-size="10.8" fill="{C["ink"]}">{l}</text>' for i,l in enumerate(ls))
 for x,y,t,ls,fg,bg in [
  (150,62,"DROGAS",["usuário: sem prisão, TC","tráfico 5-15 · privilegiado","não hediondo (SV 63)"],C['red'],C['redsoft']),
  (490,62,"ARMAS",["posse (casa) x porte (rua)","restrito 3-6 · proibido 4-12","guardas: porte em todos"],C['golddeep'],C['goldsoft']),
  (112,235,"HEDIONDOS",["só o que está no rol","sem anistia, graça, indulto","temporária 30 + 30"],C['navy'],NV),
  (528,235,"TORTURA",["crime comum · 2 a 8","omissão: detenção 1 a 4","perda do cargo: dobro"],C['blue'],C['sky']),
  (150,408,"MARIA DA PENHA",["gênero · 6 formas","medidas em 48h, sem BO","24-A: reclusão 2 a 5"],C['green'],C['greensoft']),
  (490,408,"ABUSO · ORCRIM",["finalidade específica","busca: 5h às 21h","orcrim: 4 + estrutura"],C['navy'],NV)]) + '</svg><figcaption>Mapa conceitual do Caderno 08.</figcaption></figure>'
add('<div class="marker">§§R1§§</div><div class="unit"><span class="u">REVISÃO</span><span class="t">Véspera da prova</span></div><h1 class="big">Mapa <span class="hl">conceitual</span></h1><p class="lead">As sete leis em seis blocos. Explique cada caixa em voz alta.</p>' + mapa)

add('<div class="unit"><span class="u">REVISÃO</span><span class="t">Erros mais comuns</span></div><h1 class="big">Os erros <span class="hl">mais comuns</span> nas provas</h1><p class="lead">Afirmações erradas que costumam aparecer em questões. Ao lado, o que está certo.</p>' +
 table(["Afirmação errada","O certo é"],[
  ["“O usuário de drogas é preso em flagrante.”","Não se impõe prisão em flagrante: lavra-se termo circunstanciado (art. 48, § 2º)."],
  ["“A Lei de Drogas fixa a quantidade que separa usuário e traficante.”","A lei não fixa; o juiz analisa as circunstâncias. Os 40 g valem só para a maconha, por decisão do STF."],
  ["“Dar droga de graça não é tráfico.”","É: “ainda que gratuitamente” (art. 33). Exceção: uso compartilhado do § 3º."],
  ["“Tráfico privilegiado é hediondo.”","Não é (Súmula Vinculante 63)."],
  ["“Arma em casa sem registro é porte ilegal.”","É <b>posse</b> irregular (art. 12)."],
  ["“Guarda de cidade pequena não tem porte de arma.”","O STF derrubou o critério populacional (ADIs 5.538 e 5.948)."],
  ["“Porte de arma de uso restrito é hediondo.”","Só o de uso <b>proibido</b> está no rol."]],["46%",None]))

add(pratica_title("Erros mais comuns (continuação)") +
 table(["Afirmação errada","O certo é"],[
  ["“Todo homicídio é hediondo.”","Só o qualificado e o praticado em atividade típica de grupo de extermínio."],
  ["“Tráfico, tortura e terrorismo são hediondos.”","São <b>equiparados</b> a hediondos."],
  ["“Tortura só pode ser praticada por policial.”","Em regra, é crime comum; ser agente público aumenta a pena."],
  ["“A Maria da Penha só vale se o casal mora junto.”","Na relação íntima de afeto, independe de coabitação."],
  ["“A vítima pode retirar a representação na delegacia.”","Só perante o juiz, em audiência (art. 16)."],
  ["“Medida protetiva exige boletim de ocorrência e inquérito.”","Independe de ambos (art. 19)."],
  ["“A Maria da Penha prevê cinco formas de violência.”","Desde 2026 são seis: a vicária foi incluída (art. 7º, VI)."],
  ["“Perda do cargo é automática no abuso de autoridade.”","Exige reincidência e declaração motivada (art. 4º)."],
  ["“Organização criminosa: três ou mais pessoas.”","Quatro ou mais, com estrutura e divisão de tarefas."]],["46%",None]))

add(pratica_title("Os números que mais caem") +
 table(["Número","Onde aparece"],[
  ["5 a 15 anos","Pena do tráfico (art. 33)"],["1/6 a 2/3","Redução do tráfico privilegiado (§ 4º) e aumento do art. 40 da Lei de Drogas"],
  ["5 e 10 meses","Prazo máximo das medidas do art. 28 (e na reincidência)"],["40 g / 6 plantas","Presunção de usuário de maconha (STF, RE 635.659)"],
  ["2, 3 e 4 pessoas","Associação para o tráfico · associação criminosa · organização criminosa"],
  ["1 a 3 · 2 a 4","Posse irregular (detenção) · porte ilegal e disparo (reclusão)"],
  ["3 a 6 · 4 a 12","Arma de uso restrito · arma de uso proibido"],["30 + 30 dias","Prisão temporária em crimes hediondos e equiparados"],
  ["2 a 8 anos","Pena básica da tortura"],["Dobro da pena","Interdição para cargo público após condenação por tortura"],
  ["12 meses","Prazo para a vítima representar ou oferecer queixa (Maria da Penha, art. 16-A)"],
  ["48 horas","Envio do pedido de medida protetiva ao juiz e prazo para o juiz decidir"],
  ["5h às 21h","Horário para cumprir mandado de busca domiciliar (art. 22 da Lei de Abuso)"],
  ["1 a 5 anos","Inabilitação para cargo público na Lei de Abuso de Autoridade"]],["28%",None]))

FC = [("DROGAS","O que é droga para a Lei 11.343?","Substância que causa dependência e consta de lista do Executivo federal (Portaria SVS/MS 344/1998)."),
 ("DROGAS","Penas do art. 28?","Advertência, prestação de serviços à comunidade e medida educativa."),
 ("DROGAS","O usuário é preso em flagrante?","Não. Lavra-se termo circunstanciado (art. 48, § 2º)."),
 ("DROGAS","Pena do tráfico?","Reclusão de 5 a 15 anos e 500 a 1.500 dias-multa."),
 ("DROGAS","Requisitos do uso compartilhado?","Eventual, sem lucro, a pessoa do relacionamento, para juntos consumirem."),
 ("DROGAS","Requisitos do tráfico privilegiado?","Primário, bons antecedentes, não se dedica a crimes, não integra organização criminosa."),
 ("DROGAS","Novidade do art. 40-A?","Pena em dobro para integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia."),
 ("ARMAS","Posse x porte?","Posse: em casa ou no trabalho (titular). Porte: fora desses locais."),
 ("ARMAS","Pena da posse irregular e do porte ilegal (uso permitido)?","Posse: detenção 1 a 3. Porte: reclusão 2 a 4."),
 ("ARMAS","Arma com numeração raspada?","Art. 16, § 1º, IV: reclusão de 3 a 6 anos."),
 ("ARMAS","Porte das guardas municipais hoje?","Em todos os municípios, sem critério populacional (STF, 2021)."),
 ("ARMAS","Novidade do art. 21-A?","Aumento de 2/3 para posse ou porte ligados ao tráfico de drogas."),
 ("HEDIONDOS","Qual critério define o crime hediondo?","Critério legal: só o que está no rol da Lei 8.072."),
 ("HEDIONDOS","Quais são os equiparados?","Tráfico de drogas, tortura e terrorismo."),
 ("HEDIONDOS","Do que são insuscetíveis?","Anistia, graça, indulto e fiança."),
 ("TORTURA","Pena da omissão de quem devia evitar a tortura?","Detenção de 1 a 4 anos (§ 2º)."),
 ("TORTURA","Efeito da condenação por tortura?","Perda do cargo e interdição pelo dobro do prazo da pena."),
 ("TORTURA","Novidade de 2026?","Inciso III: sofrimento intenso e reiterado à mulher em violência doméstica (Lei 15.410/2026)."),
 ("MARIA DA PENHA","Três âmbitos do art. 5º?","Unidade doméstica, família e relação íntima de afeto."),
 ("MARIA DA PENHA","Formas de violência do art. 7º?","Física, psicológica, sexual, patrimonial, moral e vicária (incluída em 2026)."),
 ("MARIA DA PENHA","Quem afasta o agressor do lar se não há juiz na comarca?","O delegado; se também não houver delegado disponível, o policial (art. 12-C)."),
 ("ABUSO","Elemento subjetivo exigido?","Finalidade de prejudicar, beneficiar a si ou a terceiro, ou mero capricho ou satisfação pessoal."),
 ("ABUSO","Horário do mandado de busca domiciliar?","Das 5h às 21h; fora disso, art. 22, § 1º, III."),
 ("ORCRIM","Conceito de organização criminosa?","4 ou mais pessoas, estrutura, divisão de tarefas, infrações com pena máxima acima de 4 anos ou transnacionais.")]
def fcpage(items, first):
    cs = "".join(f'<div class="c"><div class="f"><small>{a}</small>{q}</div><div class="b">{r}</div></div>' for a,q,r in items)
    h = ('<div class="marker">§§R2§§</div><div class="unit"><span class="u">REVISÃO ATIVA</span></div><h1 class="big">Flash<span class="hl">cards</span></h1><p class="lead">Cubra a resposta, tente lembrar e confira. Revise em 1, 3, 7, 15 e 30 dias.</p>' if first else '')
    return h + f'<div class="fc">{cs}</div>'
add(fcpage(FC[:12], True)); add(fcpage(FC[12:], False))

Q = [
 ("Drogas","Durante patrulhamento, agentes encontram com um jovem pequena quantidade de cocaína destinada ao seu próprio consumo. Segundo a Lei nº 11.343/2006, deve-se:",
  ["prendê-lo em flagrante por tráfico.","prendê-lo em flagrante pelo art. 28.","lavrar termo circunstanciado, sem impor prisão em flagrante.","liberá-lo sem nenhuma providência, pois o fato é atípico.","encaminhá-lo diretamente ao presídio."],"C",
  "Para o art. 28 não se impõe prisão em flagrante; o autor é encaminhado ao juízo ou assume o compromisso de comparecer, lavrando-se termo circunstanciado (art. 48, § 2º). A decisão do STF sobre a maconha não alcança a cocaína.","Usuário: termo circunstanciado, sem prisão."),
 ("Drogas","Sobre a decisão do STF no RE 635.659, é correto afirmar que:",
  ["descriminalizou o porte de todas as drogas para consumo pessoal.","tornou o porte de maconha para consumo pessoal infração administrativa, com presunção relativa de usuário até 40 g ou 6 plantas fêmeas.","liberou a venda de maconha em até 40 g.","revogou expressamente o art. 28 da Lei de Drogas.","fixou presunção absoluta de usuário até 60 g."],"B",
  "O STF tratou apenas da maconha, manteve a proibição como ilícito não penal e fixou presunção relativa (40 g ou 6 plantas fêmeas). O texto do art. 28 não foi alterado.","Maconha, 40 g, presunção relativa."),
 ("Drogas","A pena prevista para o crime de tráfico de drogas (art. 33, caput) é de:",
  ["detenção, de 1 a 3 anos.","reclusão, de 3 a 10 anos.","reclusão, de 5 a 15 anos, e 500 a 1.500 dias-multa.","reclusão, de 8 a 20 anos.","reclusão, de 2 a 6 anos."],"C",
  "Art. 33, caput. Reclusão de 3 a 10 é a da associação (art. 35); 8 a 20, a do financiamento (art. 36); 2 a 6, a do informante (art. 37).","Tráfico: 5 a 15."),
 ("Drogas","Pedro oferece, em uma única ocasião e sem objetivo de lucro, um cigarro de maconha à namorada, para que fumem juntos. Pela lei, a conduta se enquadra:",
  ["no tráfico do art. 33, caput.","no art. 33, § 3º (uso compartilhado).","no art. 35 (associação).","no art. 37 (informante).","em fato atípico."],"B",
  "Oferecer droga eventualmente, sem lucro, a pessoa do relacionamento, para juntos consumirem: art. 33, § 3º, com detenção de 6 meses a 1 ano e multa.","Eventual + sem lucro + relacionamento + juntos."),
 ("Drogas","NÃO é requisito do tráfico privilegiado (art. 33, § 4º):",
  ["ser primário.","ter bons antecedentes.","não se dedicar às atividades criminosas.","não integrar organização criminosa.","ter confessado espontaneamente o crime."],"E",
  "A lei exige quatro requisitos cumulativos: primário, bons antecedentes, não se dedicar a atividades criminosas e não integrar organização criminosa. Confissão não é requisito.","Quatro requisitos, sem confissão."),
 ("Drogas","A associação para o tráfico (art. 35 da Lei nº 11.343/2006) exige a reunião de, no mínimo:",
  ["duas pessoas.","três pessoas.","quatro pessoas.","cinco pessoas.","dez pessoas."],"A",
  "Art. 35: “associarem-se duas ou mais pessoas”. A associação criminosa do CP exige três; a organização criminosa, quatro.","2 (tráfico) · 3 (CP) · 4 (orcrim)."),
 ("Armas","Carlos guarda em sua casa, sem registro, um revólver de uso permitido. Ele comete:",
  ["porte ilegal de arma de fogo de uso permitido.","posse irregular de arma de fogo de uso permitido.","omissão de cautela.","disparo de arma de fogo.","fato atípico."],"B",
  "Possuir arma de uso permitido em desacordo com a lei, no interior da residência, é posse irregular (art. 12), com detenção de 1 a 3 anos e multa.","Em casa = posse."),
 ("Armas","A conduta de portar arma de fogo de uso permitido com numeração raspada configura:",
  ["porte ilegal de arma de uso permitido (art. 14).","posse irregular (art. 12).","crime do art. 16, § 1º, IV, do Estatuto.","contravenção penal.","comércio ilegal de arma de fogo."],"C",
  "O art. 16, § 1º, IV, pune quem porta arma com numeração, marca ou sinal de identificação raspado, suprimido ou adulterado, com as penas do caput (reclusão de 3 a 6 anos).","Numeração raspada = art. 16, § 1º."),
 ("Armas","Assinale a alternativa que contém crime do Estatuto do Desarmamento considerado hediondo:",
  ["posse irregular de arma de uso permitido.","porte ilegal de arma de uso permitido.","posse ou porte ilegal de arma de fogo de uso proibido.","omissão de cautela.","disparo de arma de fogo."],"C",
  "O parágrafo único do art. 1º da Lei nº 8.072/1990 inclui a posse ou porte de arma de uso proibido (art. 16), o comércio ilegal (art. 17) e o tráfico internacional (art. 18).","Só o uso proibido."),
 ("Armas","Sobre o porte de arma de fogo pelos integrantes das guardas municipais, considerando as decisões do STF, é correto afirmar que:",
  ["é permitido apenas nas capitais.","é permitido apenas em municípios com mais de 500 mil habitantes.","é vedado em municípios com menos de 50 mil habitantes.","o critério populacional do Estatuto foi declarado inconstitucional, garantindo-se o porte nas guardas de todos os municípios.","é proibido em qualquer caso."],"D",
  "Nas ADIs 5.538 e 5.948 e na ADC 38 (2021), o STF afastou o critério populacional dos incisos III e IV do art. 6º.","Guardas: todos os municípios."),
 ("Armas","Disparar arma de fogo em via pública, sem a finalidade de praticar outro crime, configura crime punido com:",
  ["detenção, de 1 a 3 anos.","reclusão, de 2 a 4 anos, e multa.","reclusão, de 3 a 6 anos.","detenção, de 1 a 2 anos.","apenas multa."],"B",
  "Art. 15 do Estatuto: reclusão de 2 a 4 anos e multa.","Disparo: 2 a 4."),
 ("Hediondos","É crime hediondo, segundo a Lei nº 8.072/1990:",
  ["furto simples.","homicídio simples praticado por motivo de ciúme.","roubo simples.","roubo com emprego de arma de fogo.","lesão corporal leve."],"D",
  "O art. 1º, II, b, inclui o roubo com emprego de arma de fogo (Lei nº 13.964/2019). Os demais não estão no rol.","Roubo com arma de fogo é hediondo."),
 ("Hediondos","São equiparados a hediondos:",
  ["tráfico de drogas, tortura e terrorismo.","furto, roubo e extorsão.","estupro, tortura e feminicídio.","tráfico de pessoas, sequestro e homicídio.","corrupção, peculato e concussão."],"A",
  "A Constituição (art. 5º, XLIII) e o art. 2º da Lei nº 8.072/1990 dão a tráfico, tortura e terrorismo o mesmo tratamento dos hediondos.","Os três T."),
 ("Hediondos","Os crimes hediondos e equiparados são, segundo o art. 2º da Lei nº 8.072/1990, insuscetíveis de:",
  ["liberdade provisória sem fiança.","progressão de regime.","anistia, graça, indulto e fiança.","apelação em liberdade.","prisão temporária."],"C",
  "Art. 2º, I e II. A vedação da liberdade provisória saiu da lei em 2007, e a progressão é possível, com as frações do art. 112 da LEP.","Sem anistia, graça, indulto e fiança."),
 ("Tortura","Mãe que, como castigo, submete o filho a intenso sofrimento físico, queimando-lhe as mãos, comete:",
  ["maus-tratos.","lesão corporal leve.","tortura-castigo (art. 1º, II, da Lei nº 9.455/1997).","constrangimento ilegal.","exercício arbitrário das próprias razões."],"C",
  "Submeter pessoa sob sua guarda, poder ou autoridade a intenso sofrimento como castigo pessoal é tortura-castigo; a pena é aumentada por ser a vítima criança (§ 4º, II).","Guarda + sofrimento intenso + castigo = tortura."),
 ("Tortura","O delegado que presencia a tortura praticada por subordinados e nada faz, tendo o dever de evitá-la, responde:",
  ["como coautor, com a mesma pena dos executores.","pelo § 2º do art. 1º, com detenção de 1 a 4 anos.","apenas administrativamente.","por prevaricação.","por condescendência criminosa."],"B",
  "O § 2º pune quem se omite diante das condutas, quando tinha o dever de evitá-las ou apurá-las, com detenção de 1 a 4 anos.","Omissão: detenção 1 a 4."),
 ("Tortura","Sobre a Lei de Tortura, é INCORRETO afirmar:",
  ["a tortura, em regra, pode ser praticada por qualquer pessoa.","a condenação acarreta perda do cargo e interdição pelo dobro do prazo da pena.","o crime é inafiançável e insuscetível de graça ou anistia.","o condenado por tortura por omissão (§ 2º) inicia obrigatoriamente no regime fechado.","a pena aumenta de 1/6 a 1/3 se o crime é cometido por agente público."],"D",
  "O § 7º manda iniciar em regime fechado, salvo a hipótese do § 2º (omissão).","Omissão: fora da regra do regime fechado."),
 ("Maria da Penha","Para a Lei Maria da Penha, configura violência doméstica e familiar contra a mulher a ação ou omissão:",
  ["praticada apenas por homem.","baseada no gênero, no âmbito da unidade doméstica, da família ou de relação íntima de afeto.","que exige coabitação entre agressor e vítima.","limitada à violência física.","praticada apenas por cônjuge ou companheiro."],"B",
  "Art. 5º: ação ou omissão baseada no gênero, nos três âmbitos. A relação íntima de afeto independe de coabitação, e o rol de formas inclui violência psicológica, sexual, patrimonial e moral.","Gênero + três âmbitos."),
 ("Maria da Penha","Reter os documentos pessoais da companheira para impedi-la de sair de casa caracteriza, entre outras, violência:",
  ["moral.","sexual.","patrimonial.","institucional.","física."],"C",
  "Art. 7º, IV: a retenção, subtração ou destruição de documentos pessoais, bens e valores é violência patrimonial.","Documentos retidos = patrimonial."),
 ("Maria da Penha","Em município que não é sede de comarca, verificado risco atual à vida da mulher, o agressor poderá ser afastado do lar:",
  ["somente pelo juiz.","pelo delegado de polícia.","pelo Ministério Público.","pelo Conselho Tutelar.","pela própria vítima, por escrito."],"B",
  "Art. 12-C: pela autoridade judicial; pelo delegado, quando o município não for sede de comarca; ou pelo policial, quando também não houver delegado disponível.","Sem comarca: delegado; sem delegado: policial."),
 ("Maria da Penha","Nos crimes praticados com violência doméstica e familiar contra a mulher:",
  ["aplica-se a transação penal da Lei nº 9.099/1995.","admite-se a pena de cesta básica.","não se aplica a Lei nº 9.099/1995, independentemente da pena prevista.","a renúncia à representação pode ser feita na delegacia.","as medidas protetivas dependem de inquérito instaurado."],"C",
  "Art. 41. O art. 17 veda a cesta básica; o art. 16 exige renúncia perante o juiz; o art. 19 dispensa inquérito para as medidas protetivas.","Lei 9.099: não se aplica."),
 ("Abuso","De acordo com a Lei nº 13.869/2019, as condutas nela descritas constituem crime de abuso de autoridade quando praticadas:",
  ["em qualquer caso, bastando o dolo genérico.","também na forma culposa.","com a finalidade específica de prejudicar outrem ou beneficiar a si mesmo ou a terceiro, ou por mero capricho ou satisfação pessoal.","apenas por membros do Poder Judiciário.","apenas por servidores concursados."],"C",
  "Art. 1º, § 1º. A lei exige essa finalidade específica; não há forma culposa, e o sujeito ativo é qualquer agente público.","Finalidade específica."),
 ("Abuso","O agente que cumpre mandado de busca e apreensão domiciliar às 22 horas, fora das hipóteses legais, pode responder por:",
  ["fato atípico, pois havia mandado.","crime do art. 22, § 1º, III, da Lei de Abuso de Autoridade.","violação de domicílio do CP, apenas.","prevaricação.","desobediência."],"B",
  "O art. 22, § 1º, III, pune quem cumpre mandado de busca domiciliar após as 21h ou antes das 5h.","Busca domiciliar: 5h às 21h."),
 ("Org. criminosa","Segundo a Lei nº 12.850/2013, considera-se organização criminosa a associação de:",
  ["2 ou mais pessoas, para o tráfico.","3 ou mais pessoas, para cometer crimes.","4 ou mais pessoas, estruturalmente ordenada e com divisão de tarefas, para infrações com pena máxima superior a 4 anos ou transnacionais.","5 ou mais pessoas, com hierarquia formal obrigatória.","qualquer número de pessoas armadas."],"C",
  "Art. 1º, § 1º. A divisão de tarefas pode ser informal. 2 pessoas é a associação para o tráfico; 3, a associação criminosa do CP.","Orcrim: 4 + estrutura + tarefas.")]

ALVO = "CBDBEADCBDBAEDCBDBCEACBD"
for i,(tema,enun,alts,gab,com,mem) in enumerate(Q):
    a, b = "ABCDE".index(gab), "ABCDE".index(ALVO[i]); alts = list(alts); alts[a], alts[b] = alts[b], alts[a]
    Q[i] = (tema, enun, alts, ALVO[i], com, mem)
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
add('<div class="unit"><span class="u">CORREÇÃO</span><span class="t">Treinos rápidos</span></div><h1 class="big">Respostas dos <span class="hl">treinos</span></h1><p class="lead">Certo ou errado das Unidades 1 a 5.</p>' + tr_block(TREINOS[:2]))
add(tr_block(TREINOS[2:4])); add(tr_block(TREINOS[4:]))

add(f'''<div class="unit"><span class="u">ENCERRAMENTO</span></div><h1 class="big">Referências e <span class="hl">verificação</span></h1><p class="lead">De onde vieram as informações.</p>
<h3>Legislação consultada (portal do Planalto)</h3>
<ul>
<li>Lei nº 11.343/2006 (Drogas); Lei nº 10.826/2003 (Estatuto do Desarmamento); Lei nº 8.072/1990 (Crimes Hediondos); Lei nº 11.340/2006 (Maria da Penha); Lei nº 13.869/2019 (Abuso de Autoridade); Lei nº 9.455/1997 (Tortura); Lei nº 12.850/2013 (Organizações Criminosas).</li>
<li>Alterações recentes identificadas nas notas dessas leis: nº 13.840/2019, 13.870/2019, 13.964/2019, 14.321/2022, 14.688/2023, 14.811/2024, 14.967/2024, 14.994/2024, 15.159/2025, 15.245/2025, 15.306/2025, 15.358/2026, 15.384/2026, 15.410/2026 e 15.487/2026, além das alterações da Lei Maria da Penha: nº 13.827/2019, 13.880/2019, 13.894/2019, 13.984/2020, 14.550/2023, 14.674/2023, 14.857/2024, 15.380/2026, 15.383/2026, 15.411/2026, 15.412/2026, 15.438/2026 e 15.455/2026; e o art. 338-A do Código Penal (Lei nº 15.280/2025), conferido para o Caderno 07.</li>
<li>Citados sem conferência nesta edição: Código Penal, art. 288 (associação criminosa) e art. 136 (maus-tratos); Lei de Execução Penal, art. 112; Lei nº 13.260/2016 (terrorismo).</li>
</ul>
<h3>Jurisprudência citada (identificada em pesquisa)</h3><ul><li>STF: RE 635.659 (Tema 506, maconha, 2024); HC 118.533, Tema 1.400 e Súmula Vinculante 63 (tráfico privilegiado); HC 104.339 (liberdade provisória no tráfico); HC 111.840 (regime inicial); ADI 3.112; ADIs 5.538 e 5.948 e ADC 38 (porte das guardas, 2021); RE 608.588 (Tema 656, guardas municipais, 2025).</li><li>STJ: REsp 1.977.124 (Lei Maria da Penha e mulheres trans).</li></ul>''' + lembre(p(f'<strong>Material pesquisado e atualizado em: {DATA}.</strong> As leis foram conferidas nos textos do portal do Planalto, que exibem a redação vigente com notas de alteração; algumas páginas mostram versões antigas e novas lado a lado, e a versão atual foi identificada pelas notas. <strong>Limitações:</strong> os textos do Planalto não informam a data da última atualização e não substituem o Diário Oficial; as leis de 2025 e 2026 não foram lidas no DOU, e o conteúdo da Lei nº 15.358/2026 só foi conferido nos dispositivos que ela inseriu nessas leis. A jurisprudência foi identificada em notícias e publicações e não foi reconferida nos portais oficiais dos tribunais. O caderno não reproduz as leis por inteiro. Confira se houve alteração posterior antes da prova e consulte o edital do seu concurso.'), "Verificação e limitações"))
add('''<div class="ending"><h2>Fim do Caderno 08</h2><p style="text-align:center">Continue revisando pelos flashcards e pelos erros mais comuns. Volte às tabelas de diferenciação sempre que errar uma questão.</p>
<p class="note" style="text-align:center">Mapa da Aprovação · Caderno Simplificado · Legislação Penal Especial · Caderno 08 · 1ª edição · novembro de 2026<br>Material de estudo independente. Não substitui a leitura da lei e do edital do seu concurso.</p></div>''')

doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Mapa da Aprovação — Caderno 08 — Legislação Penal Especial</title>
<link rel="stylesheet" href="estilo.css"></head><body>{symbols()}{"".join(P)}</body></html>'''
open(os.path.join(HERE, "miolo.html"), "w").write(doc)
print("páginas planejadas:", len(P))
