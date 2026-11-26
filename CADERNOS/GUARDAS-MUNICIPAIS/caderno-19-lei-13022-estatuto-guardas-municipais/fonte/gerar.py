"""Gera miolo.html do Caderno 19: Legislação das Guardas Municipais — Lei nº 13.022/2014. Uso: python3 gerar.py
Base legal conferida no portal do Planalto em 26/11/2026 (texto da Lei nº 13.022/2014, arts. 1º a 23; remissões à ADPF 995 e ao Decreto nº 11.841/2023 exibidas na página)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit
from kit import *

DATA = "26 de novembro de 2026"
kit.U = {1:("UNIDADE 1","Fundamentos e princípios"),2:("UNIDADE 2","Competências"),3:("UNIDADE 3","Criação e organização"),4:("UNIDADE 4","Investidura e formação"),5:("UNIDADE 5","Controle e prerrogativas"),6:("UNIDADE 6","Atuação prática e STF")}
def lg(x): return f"{x} · Lei nº 13.022/2014 (em síntese)"

# ---------------- diagramas ----------------
def piramide_base():
    N,B=C['navy'],C['blue']
    s = f'<figure><svg viewBox="0 0 640 210" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">{arrowdefs("pb")}'
    for x,t,a,b,fg,bg in [(110,"CF/88","art. 144, § 8º","autoriza os Municípios",N,NV),(320,"LEI 13.022/2014","normas gerais","(Estatuto Geral)",B,C['sky']),(530,"LEI MUNICIPAL","cria a guarda e","define carreira e regras",C['golddeep'],C['goldsoft'])]:
        s += f'<rect x="{x-92}" y="24" width="184" height="96" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.6"/><text x="{x}" y="56" text-anchor="middle" font-size="15" font-weight="900" fill="{fg}">{t}</text><text x="{x}" y="80" text-anchor="middle" font-size="11" fill="{C["ink"]}">{a}</text><text x="{x}" y="98" text-anchor="middle" font-size="11" fill="{C["ink"]}">{b}</text>'
    s += f'<g stroke="{C["ink"]}" stroke-width="3" marker-end="url(#pb)"><line x1="204" y1="72" x2="224" y2="72"/><line x1="414" y1="72" x2="434" y2="72"/></g>'
    s += f'<rect x="60" y="146" width="520" height="44" rx="10" fill="{C["redsoft"]}" stroke="{C["red"]}" stroke-width="2"/><text x="320" y="166" text-anchor="middle" font-size="11.5" font-weight="900" fill="{C["red"]}">A criação é FACULTATIVA: “o Município PODE criar” a guarda, por lei (art. 6º).</text><text x="320" y="182" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">Subordinação: chefe do Poder Executivo municipal (art. 6º, parágrafo único).</text>'
    return s + '</svg><figcaption>Da Constituição à lei municipal: a cadeia normativa das guardas.</figcaption></figure>'

def principios_roda():
    N=C['navy']
    s = f'<figure><svg viewBox="0 0 640 260" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    itens=[(130,50,"I","Direitos humanos,","cidadania e liberdades"),(510,50,"II","Preservação da vida,","menos sofrimento e perdas"),(110,200,"III","Patrulhamento","preventivo"),(530,200,"IV","Compromisso com a","evolução social da comunidade"),(320,232,"V","Uso progressivo","da força")]
    s += '<g stroke="#b9c2bc" stroke-width="2.4">' + "".join(f'<line x1="320" y1="130" x2="{x}" y2="{y}"/>' for x,y,*_ in itens) + '</g>'
    s += f'<circle cx="320" cy="130" r="58" fill="{N}"/><text x="320" y="124" text-anchor="middle" font-size="12" font-weight="900" fill="#3ddc6f">PRINCÍPIOS</text><text x="320" y="142" text-anchor="middle" font-size="11" font-weight="900" fill="#fff">art. 3º</text>'
    for x,y,n,a,b in itens:
        w=200 if n!="V" else 170
        s += f'<rect x="{x-w/2}" y="{y-26}" width="{w}" height="52" rx="12" fill="{C["sky"]}" stroke="{C["blue"]}" stroke-width="2.2"/><text x="{x-w/2+14}" y="{y+6}" font-size="15" font-weight="900" fill="{C["blue"]}">{n}</text><text x="{x+12}" y="{y-3}" text-anchor="middle" font-size="10.5" font-weight="800" fill="{C["ink"]}">{a}</text><text x="{x+12}" y="{y+13}" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">{b}</text>'
    return s + '</svg><figcaption>Os cinco princípios mínimos de atuação das guardas municipais.</figcaption></figure>'

def controle():
    s = f'<figure><svg viewBox="0 0 640 230" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    s += f'<rect x="190" y="10" width="260" height="44" rx="12" fill="{C["navy"]}"/><text x="320" y="30" text-anchor="middle" font-size="12" font-weight="900" fill="#fff">CONTROLE DA GUARDA</text><text x="320" y="46" text-anchor="middle" font-size="10" fill="#c9d2cc">art. 13 · órgãos permanentes e autônomos</text>'
    s += '<g stroke="#9aa3ad" stroke-width="2.4"><path d="M320 54 V70 M160 70 H480 M160 70 V84 M480 70 V84"/></g>'
    for x,t,a,b,c,fg,bg in [(160,"INTERNO · CORREGEDORIA","apura infrações disciplinares","obrigatória se a guarda tiver","mais de 50 servidores OU usar arma de fogo",C['red'],C['redsoft']),(480,"EXTERNO · OUVIDORIA","recebe reclamações, sugestões,","elogios e denúncias; independente","da direção; obrigatória em QUALQUER guarda",C['green'],C['greensoft'])]:
        s += f'<rect x="{x-150}" y="84" width="300" height="104" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.6"/><text x="{x}" y="110" text-anchor="middle" font-size="13" font-weight="900" fill="{fg}">{t}</text>'
        s += f'<text x="{x}" y="134" text-anchor="middle" font-size="10.8" fill="{C["ink"]}">{a}</text><text x="{x}" y="152" text-anchor="middle" font-size="10.8" fill="{C["ink"]}">{b}</text><text x="{x}" y="170" text-anchor="middle" font-size="10.8" font-weight="800" fill="{C["ink"]}">{c}</text>'
    s += f'<text x="320" y="214" text-anchor="middle" font-size="11" font-weight="800" fill="{C["navy"]}">Corregedor e ouvidor têm mandato; a perda exige maioria absoluta da Câmara Municipal (art. 13, § 2º).</text>'
    return s + '</svg><figcaption>Controle interno e externo das guardas municipais.</figcaption></figure>'

# ================================================================ APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">A lei que todo candidato a Guarda Municipal precisa dominar, artigo por artigo, com situações práticas.</p>
<p>Este é o <strong>Caderno 19 da coleção</strong>, dedicado à <strong>Lei nº 13.022/2014</strong>, o <strong>Estatuto Geral das Guardas Municipais</strong>. É uma lei curta (23 artigos), mas cobrada em detalhes nos concursos de GCM: os cinco princípios, as dezoito competências específicas, os limites de efetivo, os requisitos de investidura, a corregedoria e a ouvidoria.</p>
<p>A lei foi conferida no portal do Planalto em <strong>{DATA}</strong>. Os quadros de “texto legal” trazem a lei <strong>em síntese</strong>, preservando os termos-chave; para a redação literal, leia a lei no Planalto. O caderno também explica duas decisões do STF que mudaram a leitura da lei: a <strong>ADPF 995</strong> (2023) e o <strong>Tema 656</strong> (2025).</p>
{table(["Recurso","Onde está"],[["Cadeia normativa: CF, Estatuto e lei municipal","Unidade 1"],["Roda dos cinco princípios","Unidade 1"],["As 18 competências específicas agrupadas por tema","Unidade 2"],["Tabela de efetivo máximo com exemplos de cálculo","Unidade 3"],["Requisitos de investidura e formação","Unidade 4"],["Organograma do controle (corregedoria e ouvidoria)","Unidade 5"],["Situações hipotéticas ilustradas e decisões do STF","Unidade 6"],["Mapa conceitual, erros comuns, flashcards e 24 questões autorais","Revisão e prática"]],["58%",None])}''', first=True)

toc_page([("u","UNIDADE 1 · FUNDAMENTOS E PRINCÍPIOS","U1"),("","1. Base constitucional e natureza da guarda","A01"),("","2. Princípios mínimos de atuação","A02"),
 ("u","UNIDADE 2 · COMPETÊNCIAS","U2"),("","3. Competência geral: bens, serviços e instalações","A03"),("","4. Competências específicas","A04"),
 ("u","UNIDADE 3 · CRIAÇÃO E ORGANIZAÇÃO","U3"),("","5. Criação, subordinação e consórcio","A05"),("","6. Limite de efetivo","A06"),
 ("u","UNIDADE 4 · INVESTIDURA E FORMAÇÃO","U4"),("","7. Requisitos para o cargo","A07"),("","8. Capacitação","A08"),
 ("u","UNIDADE 5 · CONTROLE, CARREIRA E PRERROGATIVAS","U5"),("","9. Corregedoria e ouvidoria","A09"),("","10. Cargos, carreira e porte de arma","A10"),("","11. Prerrogativas e vedações","A11"),
 ("u","UNIDADE 6 · ATUAÇÃO PRÁTICA, OUTROS ÓRGÃOS E STF","U6"),("","12. Relação com outros órgãos","A12"),("","13. Situações práticas","A13"),("","14. O que o STF decidiu","A14"),
 ("u","REVISÃO E PRÁTICA","RV"),("","Mapa conceitual · Erros mais comuns","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),("","Gabarito, respostas dos treinos e referências","R4")])

# ================================================================ UNIDADE 1
opener("01","UNIDADE 1","Fundamentos e princípios",["Base constitucional e natureza","Princípios mínimos de atuação"],"U1")

add(H(1,'Base constitucional e <span class="hl">natureza</span> da guarda','Art. 144, § 8º, da CF e arts. 1º e 2º da lei.', "A01") +
 lei("Art. 144, § 8º · Constituição Federal",'<p>§ 8º Os Municípios poderão constituir guardas municipais destinadas à proteção de seus bens, serviços e instalações, conforme dispuser a lei.</p>') +
 piramide_base() +
 lei(lg("Arts. 1º e 2º"),'<p>A lei institui normas gerais para as guardas municipais, disciplinando o § 8º do art. 144 da Constituição (art. 1º). Incumbe às guardas municipais, <b>instituições de caráter civil, uniformizadas e armadas</b> conforme previsto em lei, a função de <b>proteção municipal preventiva</b>, ressalvadas as competências da União, dos Estados e do Distrito Federal (art. 2º).</p>') +
 memo('Guarda municipal: instituição <strong>civil</strong>, <strong>uniformizada</strong> e <strong>armada conforme a lei</strong>, com função de <strong>proteção municipal preventiva</strong>.'))

add(H(1,'Princípios mínimos de <span class="hl">atuação</span>','Art. 3º: os valores que orientam todo o trabalho.', "A02") +
 principios_roda() +
 traduz(p('Os princípios são a “bússola” da guarda. O guarda municipal age <strong>antes</strong> do problema (patrulhamento preventivo), com foco em <strong>proteger pessoas</strong> (vida, direitos, liberdades), <strong>próximo da comunidade</strong> e usando a força de forma <strong>progressiva</strong>: começa pela presença e pela palavra e só avança se a situação exigir.')) +
 pega('<ul><li>São princípios <b>mínimos</b>: a lei municipal pode acrescentar outros.</li><li>O princípio é o <b>uso progressivo</b> da força, e não “uso máximo” ou “uso imediato”.</li><li>O <b>patrulhamento preventivo</b> é princípio expresso do art. 3º.</li></ul>') +
 memo('Cinco princípios (art. 3º): <strong>direitos humanos</strong> · <strong>vida</strong> (menos sofrimento e perdas) · <strong>patrulhamento preventivo</strong> · <strong>comunidade</strong> · <strong>uso progressivo da força</strong>.'))

treino(1, [
 ("Segundo a Constituição, os Municípios poderão constituir guardas municipais destinadas à proteção de seus bens, serviços e instalações.","C","Art. 144, § 8º."),
 ("As guardas municipais são instituições de caráter militar.","E","São instituições de caráter civil (art. 2º)."),
 ("A função das guardas é a proteção municipal preventiva, ressalvadas as competências da União, dos Estados e do DF.","C","Art. 2º."),
 ("O uso progressivo da força é um dos princípios mínimos de atuação das guardas municipais.","C","Art. 3º, V."),
 ("O patrulhamento repressivo é princípio expresso do art. 3º.","E","O princípio é o patrulhamento preventivo."),
 ("Os princípios do art. 3º são mínimos, o que não impede a previsão de outros.","C","A lei fala em “princípios mínimos”.")])

# ================================================================ UNIDADE 2
opener("02","UNIDADE 2","Competências",["Competência geral","Competências específicas"],"U2")

add(H(2,'Competência geral: bens, serviços e <span class="hl">instalações</span>','Art. 4º.', "A03") +
 lei(lg("Art. 4º e parágrafo único"),'<p>É competência geral das guardas municipais a <b>proteção de bens, serviços, logradouros públicos municipais e instalações do Município</b>. Os bens mencionados abrangem os de <b>uso comum</b>, os de <b>uso especial</b> e os <b>dominiais</b>.</p>') +
 table(["Bem público","O que é","Exemplo"],[
  ["Uso comum do povo","Usado livremente pela população","Praças, ruas, parques"],
  ["Uso especial","Destinado a um serviço ou estabelecimento público","Escola municipal, posto de saúde, sede da prefeitura"],
  ["Dominial","Patrimônio disponível do Município, sem destinação específica","Terreno municipal desocupado"]],["24%","40%",None]) +
 lembre(p('A página da lei no Planalto traz, junto ao art. 4º, a remissão “Vide ADPF 995”: o STF reconheceu que as guardas municipais <strong>integram o sistema de segurança pública</strong> (ver Unidade 6).'), "Remissão ao STF") +
 memo('Competência geral: proteger <strong>bens, serviços, logradouros e instalações</strong> do Município. Bens de <strong>uso comum, uso especial e dominiais</strong>.'))

add(H(2,'Competências <span class="hl">específicas</span>','Art. 5º: dezoito incisos, respeitadas as competências federais e estaduais.', "A04") +
 table(["Tema","Incisos (em síntese)"],[
  ["Patrimônio e prevenção","I · zelar pelos bens, equipamentos e prédios públicos · II · prevenir e inibir, pela presença e vigilância, e coibir infrações penais ou administrativas contra bens, serviços e instalações municipais · III · atuar preventiva e permanentemente no território do Município, protegendo a população que usa bens, serviços e instalações municipais"],
  ["Cooperação e paz social","IV · colaborar, de forma integrada, com os órgãos de segurança pública em ações conjuntas pela paz social · V · colaborar com a pacificação de conflitos que seus integrantes presenciarem, respeitando os direitos fundamentais · VIII · cooperar com os demais órgãos de defesa civil"],
  ["Trânsito e meio ambiente","VI · exercer as competências de trânsito que lhes forem conferidas nas vias municipais (CTB), ou de forma concorrente, por convênio · VII · proteger o patrimônio ecológico, histórico, cultural, arquitetônico e ambiental, inclusive com medidas educativas e preventivas"],
  ["Comunidade e articulação","IX · interagir com a sociedade civil em soluções e projetos locais de segurança · X · firmar parcerias, convênios ou consórcios com outros entes · XI · articular-se com órgãos municipais de políticas sociais · XII · integrar-se a outros órgãos de poder de polícia administrativa na fiscalização de posturas e ordenamento urbano"],
  ["Ocorrências","XIII · garantir o atendimento de ocorrências emergenciais, ou prestá-lo direta e imediatamente quando deparar com elas · XIV · encaminhar ao <b>delegado de polícia</b>, diante de <b>flagrante delito</b>, o autor da infração, preservando o local do crime, quando possível e sempre que necessário"],
  ["Prevenção e eventos","XV · contribuir em estudos de impacto na segurança local (plano diretor) · XVI · desenvolver ações de prevenção primária à violência · XVII · auxiliar na segurança de grandes eventos e na proteção de autoridades e dignitários · XVIII · atuar na segurança escolar, zelando pelo entorno e participando de ações educativas, para a cultura de paz"]],["22%",None]) +
 p('<strong>Parágrafo único:</strong> no exercício de suas competências, a guarda pode colaborar ou atuar conjuntamente com órgãos de segurança pública da União, dos Estados, do DF ou de Municípios vizinhos; nas hipóteses dos incisos XIII e XIV, diante do comparecimento de órgão do art. 144 da CF, deverá prestar <strong>todo o apoio</strong> à continuidade do atendimento. Os incisos IV, XIII e XIV e o parágrafo único remetem, no Planalto, ao <strong>Decreto nº 11.841/2023</strong>, que os regulamenta.'))

atencao(pega('<ul><li>No <b>flagrante</b>, a guarda <b>encaminha o autor ao delegado de polícia</b> (inciso XIV); ela não lavra o auto de prisão em flagrante nem investiga: não exerce polícia judiciária.</li><li>As competências de <b>trânsito</b> são as conferidas pelo CTB nas vias municipais, ou por <b>convênio</b> (inciso VI).</li><li>Pacificação de conflitos: os que seus integrantes <b>presenciarem</b> (inciso V).</li><li>Segurança escolar: entorno das escolas e ações com alunos e profissionais da <b>rede municipal</b> (inciso XVIII).</li></ul>') +
 scene3([("FLAGRANTE",C['red'],C['redsoft'],"prof",["Detém o autor e","o apresenta ao","delegado (XIV)."],"preserva o local"),
  ("CHEGOU A PM",C['blue'],C['sky'],"profa",["Presta todo apoio","à continuidade do","atendimento."],"parágrafo único"),
  ("ESCOLA",C['green'],C['greensoft'],"prof",["Zela pelo entorno","e faz ações","educativas (XVIII)."],"cultura de paz")], "Situação ilustrada: competências específicas em ação."),
 ["Flagrante: delegado", "Trânsito: CTB ou convênio", "Segurança escolar", "Decreto 11.841/2023"], "Pontos mais cobrados do art. 5º")

treino(2, [
 ("É competência geral das guardas a proteção de bens, serviços, logradouros públicos municipais e instalações do Município.","C","Art. 4º."),
 ("Os bens protegidos pela guarda limitam-se aos de uso especial.","E","Abrangem uso comum, uso especial e dominiais."),
 ("Diante de flagrante delito, a guarda deve encaminhar o autor ao delegado de polícia, preservando o local do crime quando possível.","C","Art. 5º, XIV."),
 ("A guarda pode exercer competências de trânsito nas vias municipais, nos termos do CTB, ou de forma concorrente mediante convênio.","C","Art. 5º, VI."),
 ("Quando um órgão do art. 144 da CF comparece a uma ocorrência atendida pela guarda, esta deve encerrar imediatamente sua participação.","E","Deve prestar todo o apoio à continuidade do atendimento."),
 ("A atuação na segurança escolar, zelando pelo entorno das escolas, está entre as competências específicas.","C","Art. 5º, XVIII.")])

# ================================================================ UNIDADE 3
opener("03","UNIDADE 3","Criação e organização",["Criação, subordinação e consórcio","Limite de efetivo"],"U3")

add(H(3,'Criação, subordinação e <span class="hl">consórcio</span>','Arts. 6º, 8º e 9º.', "A05") +
 table(["Artigo","Regra (em síntese)"],[
  ["Art. 6º","O Município <b>pode</b> criar, <b>por lei</b>, sua guarda municipal; a guarda é subordinada ao <b>chefe do Poder Executivo municipal</b>"],
  ["Art. 8º","Municípios <b>limítrofes</b> podem, mediante <b>consórcio público</b>, utilizar reciprocamente os serviços da guarda municipal"],
  ["Art. 9º","A guarda é formada por servidores públicos integrantes de <b>carreira única</b> e plano de cargos e remuneração, nos termos de lei municipal"]],["16%",None]) +
 traduz(p('Nenhum Município é obrigado a ter guarda: a lei diz que ele “<strong>pode</strong>” criá-la. Se criar, precisa de <strong>lei</strong> (não basta decreto), e quem comanda é o <strong>prefeito</strong>. Cidades vizinhas pequenas podem se juntar num <strong>consórcio público</strong> para usar os serviços da guarda uma da outra.')) +
 memo('Criação: <strong>facultativa e por lei</strong>. Subordinação: <strong>prefeito</strong>. Vizinhos: <strong>consórcio público</strong>. Servidores: <strong>carreira única</strong>.'))

add(H(3,'Limite de <span class="hl">efetivo</span>','Art. 7º: teto proporcional à população.', "A06") +
 table(["População do Município","Efetivo máximo (art. 7º)","Exemplo de cálculo"],[
  ["Até 50.000 habitantes","<b>0,4%</b> da população","40.000 hab. × 0,4% = até 160 guardas"],
  ["Mais de 50.000 e menos de 500.000","<b>0,3%</b> da população, desde que o efetivo não seja inferior ao permitido no inciso I","200.000 hab. × 0,3% = até 600 guardas"],
  ["Mais de 500.000 habitantes","<b>0,2%</b> da população, desde que o efetivo não seja inferior ao permitido no inciso II","1.000.000 hab. × 0,2% = até 2.000 guardas"]],["28%","36%",None]) +
 lembre(p('<strong>Parágrafo único:</strong> se a população diminuir (censo ou estimativa oficial do IBGE), fica garantida a preservação do efetivo existente, que deverá ser ajustado à variação populacional nos termos de lei municipal.'), "Se a população cair") +
 pega('<ul><li>Os percentuais são <b>tetos</b> (“não poderá exceder”), não pisos.</li><li>Quanto <b>maior</b> o Município, <b>menor</b> o percentual: 0,4% · 0,3% · 0,2%.</li></ul>') +
 memo('Efetivo máximo: <strong>0,4%</strong> (até 50 mil) · <strong>0,3%</strong> (50 mil a 500 mil) · <strong>0,2%</strong> (acima de 500 mil).'))

treino(3, [
 ("Todo Município é obrigado a criar sua guarda municipal.","E","A criação é facultativa (“poderá”)."),
 ("A guarda municipal é subordinada ao chefe do Poder Executivo municipal.","C","Art. 6º, parágrafo único."),
 ("Municípios limítrofes podem, mediante consórcio público, utilizar reciprocamente os serviços da guarda.","C","Art. 8º."),
 ("Em Município com até 50.000 habitantes, o efetivo da guarda não pode exceder 0,4% da população.","C","Art. 7º, I."),
 ("Em Município com mais de 500.000 habitantes, o efetivo mínimo obrigatório é de 0,2% da população.","E","0,2% é limite máximo, não mínimo."),
 ("A guarda é formada por servidores de carreira única, com plano de cargos e remuneração.","C","Art. 9º.")])

# ================================================================ UNIDADE 4
opener("04","UNIDADE 4","Investidura e formação",["Requisitos para o cargo","Capacitação"],"U4")

add(H(4,'Requisitos para o <span class="hl">cargo</span>','Art. 10: requisitos básicos de investidura.', "A07") +
 cards([("flag","Nacionalidade","brasileira"),("ballot","Direitos políticos","em pleno gozo"),("check","Obrigações","militares e eleitorais quitadas"),
        ("book","Escolaridade","nível médio completo"),("calendar","Idade","mínima de 18 anos"),("heart","Aptidão","física, mental e psicológica")]) +
 table(["Requisito (art. 10)","Detalhe"],[
  ["VII · Idoneidade moral","Comprovada por <b>investigação social</b> e <b>certidões</b> expedidas perante o Poder Judiciário estadual, federal e distrital"],
  ["Parágrafo único","Outros requisitos podem ser estabelecidos em <b>lei municipal</b>"]],["30%",None]) +
 pega('<ul><li>A escolaridade mínima é o <b>nível médio completo</b> (não superior).</li><li>Idade mínima de <b>18 anos</b>; a lei federal não fixa idade máxima.</li><li>A lei municipal <b>pode acrescentar</b> requisitos (ex.: CNH, altura), respeitada a razoabilidade.</li></ul>') +
 memo('Sete requisitos: <strong>brasileiro · direitos políticos · quite com obrigações militares e eleitorais · ensino médio · 18 anos · aptidão física, mental e psicológica · idoneidade moral</strong>.'))

add(H(4,'<span class="hl">Capacitação</span>','Arts. 11 e 12: formação específica e órgão de formação.', "A08") +
 table(["Artigo","Regra (em síntese)"],[
  ["Art. 11","O exercício das atribuições exige <b>capacitação específica</b>, com matriz curricular compatível com as atividades; pode ser adaptada a matriz curricular nacional elaborada pela Senasp (Ministério da Justiça)"],
  ["Art. 12, caput","É facultada ao Município a criação de <b>órgão de formação, treinamento e aperfeiçoamento</b>, orientado pelos princípios do art. 3º"],
  ["Art. 12, § 1º","Municípios podem firmar <b>convênios ou consórcios</b> para esse fim"],
  ["Art. 12, § 2º","O Estado pode, mediante convênio, manter órgão de formação centralizado, com conselho gestor que assegure a participação dos Municípios"],
  ["Art. 12, § 3º","O órgão de formação <b>não pode ser o mesmo</b> destinado a formação, treinamento ou aperfeiçoamento de <b>forças militares</b>"]],["18%",None]) +
 traduz(p('A lei reforça o caráter <strong>civil</strong> da guarda também na formação: o guarda pode estudar em escola própria do Município, em escola consorciada ou em escola estadual centralizada, mas <strong>não</strong> no mesmo órgão que forma militares.'),"profa"))

treino(4, [
 ("Para investidura no cargo de guarda municipal, exige-se nível superior completo.","E","Nível médio completo (art. 10, IV)."),
 ("A idade mínima para investidura é de 18 anos.","C","Art. 10, V."),
 ("A idoneidade moral é comprovada por investigação social e certidões do Poder Judiciário estadual, federal e distrital.","C","Art. 10, VII."),
 ("A lei municipal não pode estabelecer requisitos além dos previstos na lei federal.","E","Parágrafo único do art. 10 permite outros requisitos."),
 ("O órgão de formação da guarda pode ser o mesmo destinado à formação de forças militares.","E","É vedado (art. 12, § 3º)."),
 ("Pode ser adaptada a matriz curricular nacional de formação em segurança pública elaborada pela Senasp.","C","Art. 11, parágrafo único.")])

# ================================================================ UNIDADE 5
opener("05","UNIDADE 5","Controle, carreira e prerrogativas",["Corregedoria e ouvidoria","Cargos, carreira e porte de arma","Prerrogativas e vedações"],"U5")

add(H(5,'Corregedoria e <span class="hl">ouvidoria</span>','Arts. 13 e 14.', "A09") +
 controle() +
 table(["Regra","Conteúdo (em síntese)"],[
  ["Art. 13, § 1º","O Executivo municipal pode criar <b>órgão colegiado</b> para exercer o controle social das atividades de segurança, analisar a alocação de recursos e acompanhar metas"],
  ["Art. 14","Para efeito do controle interno, a guarda terá <b>código de conduta próprio</b>, conforme lei municipal"],
  ["Art. 14, parágrafo único","As guardas <b>não podem ficar sujeitas a regulamentos disciplinares de natureza militar</b>"]],["24%",None]) +
 pega('<ul><li>Corregedoria: obrigatória para guardas com <b>mais de 50</b> servidores <b>e</b> para <b>todas as que usam arma de fogo</b>.</li><li>Ouvidoria: obrigatória <b>independentemente</b> do número de servidores.</li><li>Regulamento disciplinar <b>militar</b>: vedado.</li></ul>'))

add(H(5,'Cargos, carreira e <span class="hl">porte de arma</span>','Arts. 15 e 16.', "A10") +
 table(["Regra","Conteúdo (em síntese)"],[
  ["Art. 15, caput","Os cargos <b>em comissão</b> das guardas devem ser providos por <b>membros efetivos do quadro de carreira</b> do órgão"],
  ["Art. 15, § 1º","Nos primeiros <b>4 anos</b> de funcionamento, a guarda pode ser dirigida por profissional estranho a seus quadros, preferencialmente com experiência na área de segurança ou defesa social"],
  ["Art. 15, § 2º","Deve haver <b>percentual mínimo para o sexo feminino</b>, definido em lei municipal, em todos os níveis da carreira"],
  ["Art. 15, § 3º","Deve ser garantida a <b>progressão funcional</b> da carreira em todos os níveis"],
  ["Art. 16","Aos guardas pode ser autorizado o <b>porte de arma de fogo</b>, conforme previsto em lei"],
  ["Art. 16, parágrafo único","O porte é <b>suspenso</b> em caso de restrição médica, de decisão judicial ou mediante justificativa do dirigente da guarda"]],["22%",None]) +
 memo('Comissionados: <strong>da carreira</strong> (salvo nos <strong>4 primeiros anos</strong>). Mulheres: <strong>percentual mínimo</strong> em lei municipal. Porte: <strong>conforme a lei</strong>, suspenso por restrição médica, decisão judicial ou justificativa do chefe.'))

add(H(5,'Prerrogativas e <span class="hl">vedações</span>','Arts. 17 a 22.', "A11") +
 table(["Artigo","Regra (em síntese)"],[
  ["Art. 17","A Anatel destinará o número telefônico <b>153</b> e faixa exclusiva de radiofrequência aos Municípios que possuam guarda municipal"],
  ["Art. 18","É assegurado ao guarda o recolhimento à <b>cela, isoladamente dos demais presos</b>, quando sujeito a prisão antes de condenação definitiva"],
  ["Art. 19","A estrutura hierárquica <b>não pode utilizar</b> denominação idêntica à das forças militares quanto a postos e graduações, títulos, uniformes, distintivos e condecorações"],
  ["Art. 20","Reconhece-se a representatividade das guardas no Conselho Nacional de Segurança Pública, no Conselho Nacional das Guardas Municipais e, no interesse dos Municípios, no Conselho Nacional de Secretários e Gestores Municipais de Segurança Pública"],
  ["Art. 21","Uniformes e equipamentos padronizados, <b>preferencialmente na cor azul-marinho</b>"],
  ["Art. 22","As guardas existentes deveriam adaptar-se à lei em <b>2 anos</b>; são permitidas as denominações consagradas pelo uso: <b>guarda civil, guarda civil municipal, guarda metropolitana e guarda civil metropolitana</b>"]],["14%",None]) +
 memo('<strong>153</strong> = telefone da guarda · <strong>cela separada</strong> antes da condenação definitiva · <strong>nada de patentes militares</strong> · <strong>azul-marinho</strong> (preferencialmente).'))

treino(5, [
 ("A corregedoria é obrigatória nas guardas com mais de 50 servidores e em todas as que utilizam arma de fogo.","C","Art. 13, I."),
 ("A ouvidoria só é exigida nas guardas com mais de 50 servidores.","E","É exigida independentemente do número de servidores."),
 ("As guardas municipais podem adotar regulamento disciplinar de natureza militar.","E","Vedado (art. 14, parágrafo único)."),
 ("Nos primeiros quatro anos de funcionamento, a guarda pode ser dirigida por profissional estranho a seus quadros.","C","Art. 15, § 1º."),
 ("O número telefônico 153 é destinado aos Municípios que possuem guarda municipal.","C","Art. 17."),
 ("A lei obriga o uso de uniformes na cor preta.","E","Preferencialmente azul-marinho (art. 21).")])

# ================================================================ UNIDADE 6
opener("06","UNIDADE 6","Atuação prática, outros órgãos e STF",["Relação com outros órgãos","Situações práticas","O que o STF decidiu"],"U6")

add(H(6,'Relação com outros <span class="hl">órgãos</span>','Cooperação, integração e respeito às competências.', "A12") +
 table(["Com quem","Como a lei prevê","Fundamento"],[
  ["Polícias e órgãos do art. 144 da CF","Ações conjuntas e integradas; apoio à continuidade do atendimento quando o órgão comparece","Art. 5º, IV e parágrafo único"],
  ["Polícia Civil (delegado)","Encaminhamento do autor preso em flagrante, preservando o local do crime","Art. 5º, XIV"],
  ["Órgãos de trânsito","Competências do CTB nas vias municipais ou por convênio","Art. 5º, VI"],
  ["Defesa civil","Cooperação","Art. 5º, VIII"],
  ["Políticas sociais do Município","Ações interdisciplinares de segurança","Art. 5º, XI"],
  ["Fiscalização de posturas","Integração com órgãos de poder de polícia administrativa","Art. 5º, XII"],
  ["Outros Municípios","Consórcio público, convênios e atuação conjunta","Arts. 5º, X, e 8º"]],["28%","44%",None]) +
 lembre(p('O STF, na ADPF 995, apontou que a Lei nº 13.675/2018 (que criou o Sistema Único de Segurança Pública, SUSP) coloca as guardas municipais entre os <strong>integrantes operacionais</strong> do sistema. Essa referência foi obtida no noticiário oficial e nos resumos do acórdão; confira o texto da Lei do SUSP se o edital a cobrar.'), "Lei do SUSP"))

add(H(6,'Situações <span class="hl">práticas</span>','Casos hipotéticos para treinar a aplicação da lei.', "A13") +
 table(["Situação hipotética","Conduta compatível com a lei"],[
  ["Durante ronda na praça, a equipe flagra um furto de celular","Deter o autor e <b>encaminhá-lo ao delegado de polícia</b>, preservando o local quando possível e necessário (art. 5º, XIV)"],
  ["A equipe depara com um idoso caído na calçada, ferido","<b>Prestar ou garantir o atendimento</b> da ocorrência emergencial, acionando o socorro (art. 5º, XIII)"],
  ["Discussão acalorada entre vizinhos diante dos guardas","<b>Colaborar com a pacificação do conflito</b>, respeitando os direitos fundamentais (art. 5º, V), com uso progressivo da força se necessário"],
  ["Pichação em prédio histórico tombado pelo Município","Proteger o <b>patrimônio histórico e cultural</b> e coibir a infração (art. 5º, II e VII)"],
  ["Show na orla com 50 mil pessoas","<b>Auxiliar na segurança do grande evento</b>, em integração com os demais órgãos (art. 5º, XVII)"],
  ["Viatura da PM chega a uma ocorrência que a guarda atendia","Prestar <b>todo o apoio à continuidade do atendimento</b> (art. 5º, parágrafo único)"],
  ["Movimentação suspeita na saída de uma escola municipal","Atuar na <b>segurança escolar</b>, zelando pelo entorno (art. 5º, XVIII)"]],["40%",None]) +
 scene3([("PRESENÇA",C['green'],C['greensoft'],"profa",["Ronda visível","previne e inibe","a infração."],"art. 5º, II"),
  ("DIÁLOGO",C['blue'],C['sky'],"prof",["Conversa e","negociação antes","de qualquer força."],"uso progressivo"),
  ("ENCAMINHAMENTO",C['red'],C['redsoft'],"profa",["Flagrante:","apresentar ao","delegado."],"art. 5º, XIV")], "Situação ilustrada: a escada da atuação preventiva."))

add(H(6,'O que o <span class="hl">STF</span> decidiu','Decisões que influenciam a leitura da lei.', "A14") +
 table(["Decisão","O que ficou decidido (em síntese)"],[
  ["ADPF 995 (Plenário, agosto de 2023)","As guardas municipais <b>integram o Sistema de Segurança Pública</b>; foram afastadas as interpretações judiciais que as excluíam desse sistema. A página da lei no Planalto remete a essa ADPF junto ao art. 4º"],
  ["RE 608.588, Tema 656 de repercussão geral (Plenário, 20/02/2025)","É constitucional o exercício, pelas guardas municipais, de <b>ações de segurança urbana</b>, inclusive <b>policiamento ostensivo e comunitário</b>, respeitadas as atribuições dos demais órgãos de segurança pública e <b>excluída a atividade de polícia judiciária</b>"],
  ["RE 658.570, Tema 472 (2015)","É constitucional atribuir às guardas municipais o exercício de <b>poder de polícia de trânsito</b>, inclusive a imposição de sanções administrativas previstas em lei"]],["30%",None]) +
 pega('<ul><li>Mesmo após o Tema 656, a guarda <b>não exerce polícia judiciária</b>: não preside inquérito nem investiga crimes; no flagrante, encaminha ao delegado.</li><li>As decisões convivem com a lei: o Estatuto continua valendo, agora lido à luz do STF.</li></ul>') +
 lembre(p('Os resumos das decisões do STF foram obtidos em notícias oficiais do tribunal e em fontes jurídicas, e não foram reconferidos no inteiro teor dos acórdãos. Para a redação exata das teses, consulte o portal do STF (Tema 656 e ADPF 995).'), "Verificação"))

treino(6, [
 ("Segundo o STF (ADPF 995), as guardas municipais integram o Sistema de Segurança Pública.","C","Decisão de 2023."),
 ("No Tema 656, o STF admitiu que as guardas exerçam atividades de polícia judiciária.","E","A polícia judiciária foi expressamente excluída."),
 ("O STF reconheceu como constitucional o policiamento ostensivo e comunitário pelas guardas, respeitadas as atribuições dos demais órgãos.","C","Tema 656 (2025)."),
 ("É constitucional atribuir às guardas municipais o poder de polícia de trânsito, inclusive para impor sanções previstas em lei.","C","Tema 472."),
 ("Ao prender alguém em flagrante, a guarda municipal deve lavrar o auto de prisão e instaurar o inquérito.","E","Deve encaminhar o autor ao delegado de polícia."),
 ("Diante de ocorrência emergencial com que deparar, a guarda pode prestar o atendimento de forma direta e imediata.","C","Art. 5º, XIII.")])

# ================================================================ REVISÃO
mapa(("LEI","13.022/","2014"), [
  ("NATUREZA",["civil, uniformizada","armada conforme lei","proteção preventiva"],C['navy'],NV),
  ("PRINCÍPIOS",["direitos humanos e vida","patrulhamento preventivo","uso progressivo da força"],C['blue'],C['sky']),
  ("COMPETÊNCIAS",["bens, serviços, instalações","18 incisos no art. 5º","flagrante: ao delegado"],C['green'],C['greensoft']),
  ("ORGANIZAÇÃO",["criação facultativa, por lei","prefeito comanda","0,4 · 0,3 · 0,2%"],C['golddeep'],C['goldsoft']),
  ("CONTROLE",["corregedoria: >50 ou arma","ouvidoria: sempre","sem regulamento militar"],C['red'],C['redsoft']),
  ("STF E PRÁTICA",["ADPF 995: integra o sistema","Tema 656: ostensivo","sem polícia judiciária"],C['navy'],NV)], "Mapa conceitual do Caderno 19.", "O Estatuto Geral em seis blocos. Explique cada caixa em voz alta.", center_color="#3ddc6f")

erros([
  ["“A guarda municipal é instituição militar.”","É instituição de caráter civil (art. 2º)."],
  ["“O Município é obrigado a criar guarda.”","A criação é facultativa, por lei (art. 6º)."],
  ["“A guarda é subordinada ao secretário estadual de segurança.”","É subordinada ao chefe do Executivo municipal."],
  ["“O princípio é o uso imediato da força.”","É o uso progressivo da força (art. 3º, V)."],
  ["“Bens protegidos: só os de uso especial.”","Uso comum, uso especial e dominiais."],
  ["“No flagrante, a guarda lavra o auto.”","Encaminha o autor ao delegado de polícia."],
  ["“0,4% é o efetivo mínimo.”","Os percentuais são limites máximos."]],
 [["“Exige-se nível superior.”","Nível médio completo (art. 10, IV)."],
  ["“A lei municipal não pode criar requisitos.”","Pode estabelecer outros requisitos (art. 10, parágrafo único)."],
  ["“Ouvidoria só para guardas grandes.”","Ouvidoria em qualquer guarda; corregedoria acima de 50 ou se armada."],
  ["“Pode haver regulamento disciplinar militar.”","Vedado (art. 14, parágrafo único)."],
  ["“Comissionados podem ser de fora, sempre.”","Devem ser da carreira, salvo nos 4 primeiros anos de funcionamento."],
  ["“Uniforme obrigatoriamente azul-marinho.”","Preferencialmente azul-marinho (art. 21)."],
  ["“Após o Tema 656, a guarda virou polícia judiciária.”","A polícia judiciária foi excluída."]])

flashcards([("NATUREZA","Base constitucional?","Art. 144, § 8º, da CF."),
 ("NATUREZA","Caráter da instituição?","Civil, uniformizada e armada conforme a lei."),
 ("NATUREZA","Função (art. 2º)?","Proteção municipal preventiva."),
 ("PRINCÍPIOS","Cinco princípios do art. 3º?","Direitos humanos; vida; patrulhamento preventivo; comunidade; uso progressivo da força."),
 ("COMPETÊNCIA","Competência geral (art. 4º)?","Proteger bens, serviços, logradouros e instalações municipais."),
 ("COMPETÊNCIA","Espécies de bens protegidos?","Uso comum, uso especial e dominiais."),
 ("COMPETÊNCIA","Flagrante delito (art. 5º, XIV)?","Encaminhar o autor ao delegado, preservando o local."),
 ("COMPETÊNCIA","Trânsito (art. 5º, VI)?","Competências do CTB nas vias municipais ou por convênio."),
 ("COMPETÊNCIA","Quando o órgão do art. 144 chega?","Prestar todo apoio à continuidade do atendimento."),
 ("ORGANIZAÇÃO","Criação da guarda?","Facultativa, por lei municipal."),
 ("ORGANIZAÇÃO","Subordinação?","Chefe do Poder Executivo municipal."),
 ("ORGANIZAÇÃO","Municípios vizinhos?","Consórcio público para uso recíproco."),
 ("EFETIVO","Limites do art. 7º?","0,4% (até 50 mil) · 0,3% (50 a 500 mil) · 0,2% (acima de 500 mil)."),
 ("INVESTIDURA","Escolaridade e idade?","Nível médio completo · 18 anos."),
 ("INVESTIDURA","Idoneidade moral?","Investigação social e certidões judiciais."),
 ("FORMAÇÃO","Pode usar órgão de formação militar?","Não (art. 12, § 3º)."),
 ("CONTROLE","Corregedoria obrigatória quando?","Mais de 50 servidores ou uso de arma de fogo."),
 ("CONTROLE","Ouvidoria obrigatória quando?","Sempre, qualquer que seja o efetivo."),
 ("CONTROLE","Perda do mandato de corregedor e ouvidor?","Maioria absoluta da Câmara Municipal."),
 ("CARREIRA","Direção nos 4 primeiros anos?","Pode ser de profissional estranho aos quadros."),
 ("PRERROGATIVAS","Telefone da guarda?","153."),
 ("PRERROGATIVAS","Prisão antes da condenação definitiva?","Cela isolada dos demais presos."),
 ("STF","ADPF 995?","Guardas integram o Sistema de Segurança Pública."),
 ("STF","Tema 656?","Segurança urbana, inclusive policiamento ostensivo e comunitário; sem polícia judiciária.")])

Q = [
 ("Natureza","Segundo a Lei nº 13.022/2014, as guardas municipais são instituições de caráter:",
  ["militar, subordinadas ao Exército.","civil, uniformizadas e armadas conforme previsto em lei.","militar, auxiliares das polícias militares.","privado, contratadas pelo Município.","judiciário, vinculadas ao Ministério Público."],"B",
  "Art. 2º: instituições de caráter civil, uniformizadas e armadas conforme previsto em lei, com função de proteção municipal preventiva.","Guarda = civil."),
 ("Natureza","A função atribuída às guardas municipais pelo art. 2º da lei é a de:",
  ["polícia judiciária municipal.","proteção municipal preventiva, ressalvadas as competências da União, dos Estados e do DF.","investigação de crimes contra o patrimônio.","defesa nacional.","julgamento de infrações administrativas."],"B",
  "Art. 2º.","Proteção municipal preventiva."),
 ("Princípios","NÃO é princípio mínimo de atuação das guardas municipais, segundo o art. 3º:",
  ["proteção dos direitos humanos fundamentais.","patrulhamento preventivo.","uso progressivo da força.","compromisso com a evolução social da comunidade.","hierarquia e disciplina militares."],"E",
  "Os princípios são: direitos humanos, cidadania e liberdades; preservação da vida e redução do sofrimento e das perdas; patrulhamento preventivo; compromisso com a comunidade; uso progressivo da força.","Militarismo não é princípio."),
 ("Competência geral","A competência geral das guardas municipais, prevista no art. 4º, é a proteção de:",
  ["fronteiras e portos.","bens, serviços, logradouros públicos municipais e instalações do Município.","bens da União.","presídios estaduais.","instituições financeiras privadas."],"B",
  "Art. 4º, caput.","Bens, serviços, logradouros e instalações."),
 ("Competência geral","Os bens municipais protegidos pela guarda, nos termos do parágrafo único do art. 4º, abrangem os de:",
  ["uso especial, apenas.","uso comum, apenas.","uso comum, uso especial e dominiais.","propriedade privada.","titularidade estadual."],"C",
  "Parágrafo único do art. 4º.","Comum, especial e dominial."),
 ("Flagrante","Ao se deparar com flagrante delito, a guarda municipal deve, segundo o art. 5º, XIV:",
  ["lavrar o auto de prisão em flagrante.","liberar o autor após identificá-lo.","encaminhar o autor ao delegado de polícia, preservando o local do crime quando possível e sempre que necessário.","conduzir o autor diretamente ao juiz.","instaurar inquérito policial."],"C",
  "A guarda não exerce polícia judiciária: encaminha ao delegado.","Flagrante: ao delegado."),
 ("Trânsito","Quanto ao trânsito, as guardas municipais podem:",
  ["atuar apenas em rodovias federais.","exercer as competências de trânsito que lhes forem conferidas, nas vias e logradouros municipais, nos termos do CTB, ou de forma concorrente, mediante convênio.","emitir CNH.","julgar recursos contra multas estaduais.","atuar no trânsito somente com autorização da PRF."],"B",
  "Art. 5º, VI. O STF (Tema 472) admitiu o poder de polícia de trânsito pelas guardas.","Trânsito: CTB ou convênio."),
 ("Cooperação","Em ocorrência atendida pela guarda nos casos dos incisos XIII e XIV do art. 5º, com o comparecimento de órgão do art. 144 da CF, a guarda deverá:",
  ["retirar-se imediatamente.","assumir o comando da ocorrência.","prestar todo o apoio à continuidade do atendimento.","exigir autorização do prefeito para continuar.","transferir a ocorrência à defesa civil."],"C",
  "Parágrafo único do art. 5º.","Chegou a polícia: apoio total."),
 ("Escola","A atuação preventiva na segurança escolar, zelando pelo entorno e participando de ações educativas na rede municipal, está prevista no art. 5º, inciso:",
  ["I.","VI.","XII.","XVIII.","XIV."],"D",
  "Art. 5º, XVIII: segurança escolar e cultura de paz.","Escola = XVIII."),
 ("Criação","Sobre a criação da guarda municipal, é correto afirmar:",
  ["é obrigatória em todos os Municípios.","depende de decreto do governador.","é facultativa, mediante lei, e a guarda subordina-se ao chefe do Executivo municipal.","depende de autorização do Ministério da Justiça.","só é possível em capitais."],"C",
  "Art. 6º e parágrafo único.","Pode criar, por lei; comanda o prefeito."),
 ("Consórcio","Municípios limítrofes podem utilizar reciprocamente os serviços de suas guardas mediante:",
  ["decreto estadual.","consórcio público.","contrato com empresa privada.","convênio com as Forças Armadas.","lei federal específica."],"B",
  "Art. 8º.","Vizinhos: consórcio público."),
 ("Efetivo","Em Município com 40.000 habitantes, o efetivo da guarda não poderá exceder:",
  ["80 guardas.","120 guardas.","160 guardas.","200 guardas.","400 guardas."],"C",
  "Até 50 mil habitantes: 0,4% da população. 40.000 × 0,004 = 160.","Até 50 mil: 0,4%."),
 ("Efetivo","Em Município com mais de 500.000 habitantes, o limite de efetivo da guarda corresponde a:",
  ["0,1% da população.","0,2% da população, desde que não seja inferior ao permitido no inciso II.","0,3% da população, sem restrições.","0,4% da população.","1% da população."],"B",
  "Art. 7º, III.","Acima de 500 mil: 0,2%."),
 ("Investidura","É requisito básico para investidura no cargo de guarda municipal:",
  ["nível superior completo.","idade mínima de 21 anos.","nível médio completo.","ter servido às Forças Armadas.","possuir CNH categoria D."],"C",
  "Art. 10: nacionalidade brasileira, gozo dos direitos políticos, quitação militar e eleitoral, nível médio completo, 18 anos, aptidão física, mental e psicológica e idoneidade moral.","Médio completo, 18 anos."),
 ("Investidura","A idoneidade moral do candidato é comprovada por:",
  ["declaração do próprio candidato.","investigação social e certidões expedidas perante o Poder Judiciário estadual, federal e distrital.","carta de recomendação de autoridade.","entrevista com o prefeito.","atestado médico."],"B",
  "Art. 10, VII.","Investigação social + certidões."),
 ("Formação","Sobre a formação dos guardas municipais, é correto afirmar:",
  ["deve ocorrer obrigatoriamente em academia militar.","o órgão de formação não pode ser o mesmo destinado à formação de forças militares.","é dispensada para quem tem nível superior.","só pode ser feita pela União.","é proibido o convênio entre Municípios."],"B",
  "Art. 12, § 3º. Os Municípios podem firmar convênios ou consórcios (§ 1º).","Formação civil."),
 ("Controle","A corregedoria, órgão de controle interno, é obrigatória:",
  ["em todas as guardas, sem exceção.","nas guardas com mais de 50 servidores e em todas as que utilizam arma de fogo.","apenas nas capitais.","somente nas guardas com mais de 500 servidores.","apenas quando houver denúncia."],"B",
  "Art. 13, I. A ouvidoria, por sua vez, é exigida independentemente do efetivo.","Corregedoria: >50 ou armada."),
 ("Controle","A ouvidoria das guardas municipais:",
  ["é subordinada ao comandante da guarda.","só existe em guardas com mais de 50 servidores.","é órgão de controle externo, independente em relação à direção da guarda, qualquer que seja o número de servidores.","julga infrações disciplinares.","é facultativa."],"C",
  "Art. 13, II.","Ouvidoria: externa, independente, sempre."),
 ("Disciplina","Quanto ao regime disciplinar, a lei estabelece que as guardas municipais:",
  ["seguem o regulamento disciplinar do Exército.","terão código de conduta próprio, conforme lei municipal, e não podem ficar sujeitas a regulamentos disciplinares de natureza militar.","seguem o regulamento da Polícia Militar do respectivo Estado.","não estão sujeitas a nenhum código de conduta.","seguem o Código Penal Militar."],"B",
  "Art. 14 e parágrafo único.","Código próprio; nada militar."),
 ("Carreira","Os cargos em comissão das guardas municipais devem ser providos, em regra, por:",
  ["policiais militares da reserva.","membros efetivos do quadro de carreira do órgão.","qualquer pessoa indicada pelo prefeito.","delegados de polícia.","integrantes das Forças Armadas."],"B",
  "Art. 15, caput. Nos primeiros 4 anos de funcionamento, a guarda pode ser dirigida por profissional estranho aos quadros (§ 1º).","Comissionados da carreira."),
 ("Prerrogativas","O número telefônico destinado pela Anatel aos Municípios que possuam guarda municipal é o:",
  ["190.","192.","193.","153.","199."],"D",
  "Art. 17. (190: PM; 192: SAMU; 193: bombeiros; 199: defesa civil.)","Guarda = 153."),
 ("Prerrogativas","Ao guarda municipal preso antes de condenação definitiva é assegurado:",
  ["prisão domiciliar automática.","recolhimento à cela, isoladamente dos demais presos.","liberdade imediata.","prisão em quartel militar.","suspensão do processo."],"B",
  "Art. 18.","Cela separada."),
 ("Uniforme","Sobre uniformes e denominações, a lei estabelece que:",
  ["os uniformes devem ser idênticos aos da PM.","os uniformes e equipamentos são padronizados, preferencialmente na cor azul-marinho, e são vedadas denominações hierárquicas idênticas às das forças militares.","a guarda deve usar patentes do Exército.","a única denominação permitida é “guarda municipal”.","os uniformes são livres, sem padronização."],"B",
  "Arts. 19 e 21. O art. 22, parágrafo único, admite denominações consagradas: guarda civil, guarda civil municipal, guarda metropolitana e guarda civil metropolitana.","Azul-marinho; sem patentes militares."),
 ("STF","No julgamento do Tema 656 de repercussão geral (2025), o STF decidiu que as guardas municipais:",
  ["não podem realizar qualquer atividade de segurança.","podem exercer ações de segurança urbana, inclusive policiamento ostensivo e comunitário, respeitadas as atribuições dos demais órgãos e excluída a polícia judiciária.","substituem as polícias militares.","podem instaurar inquéritos policiais.","só podem proteger prédios públicos."],"B",
  "RE 608.588, Tema 656, julgado em 20/02/2025.","Ostensivo e comunitário, sem polícia judiciária.")]

def verificar():
    assert round(40000*0.004) == 160 and round(200000*0.003) == 600 and round(1000000*0.002) == 2000
    print("verificação de cálculos: ok")
verificar()

questoes(Q, "BACDEBCAEDBCADEBACDEBCEA")
respostas_treinos()

referencias('''<h3>Legislação consultada (portal do Planalto)</h3><ul>
<li>Lei nº 13.022/2014 (Estatuto Geral das Guardas Municipais), arts. 1º a 23. A página exibe remissão à ADPF 995 (art. 4º) e ao Decreto nº 11.841/2023 (art. 5º, IV, XIII, XIV e parágrafo único); não exibe vetos nem notas de alteração de redação.</li>
<li>Constituição Federal, art. 144, § 8º.</li></ul>
<h3>Jurisprudência citada</h3><ul>
<li>STF, ADPF 995 (Plenário, 2023): guardas municipais integram o Sistema de Segurança Pública.</li>
<li>STF, RE 608.588, Tema 656 (Plenário, 20/02/2025): ações de segurança urbana, inclusive policiamento ostensivo e comunitário, excluída a polícia judiciária.</li>
<li>STF, RE 658.570, Tema 472 (2015): poder de polícia de trânsito.</li></ul>''',
 'A lei foi conferida no texto do portal do Planalto; os quadros trazem o texto <strong>em síntese</strong>, preservando termos-chave, e não substituem a leitura literal. <strong>Limitações:</strong> a página não informa data de atualização e pode não exibir alterações posteriores; o Decreto nº 11.841/2023 e a Lei nº 13.675/2018 (SUSP) não foram lidos na íntegra; os resumos das decisões do STF vêm de notícias oficiais do tribunal e de fontes jurídicas, sem conferência do inteiro teor dos acórdãos. Há propostas de mudança constitucional sobre segurança pública em tramitação no Congresso que podem alterar o tema. Confira o edital e a lei municipal da guarda do seu concurso.', DATA)
encerramento("19", "Legislação das Guardas Municipais", 'Sugestão de continuação: <strong>Caderno 20 · Questões Comentadas</strong>.')
gravar(HERE, "Mapa da Aprovação — Caderno 19 — Lei 13.022/2014", Q)
