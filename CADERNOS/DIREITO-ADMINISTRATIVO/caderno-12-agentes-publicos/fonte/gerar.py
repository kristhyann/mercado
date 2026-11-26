"""Gera miolo.html do Caderno 12: Agentes Públicos. Uso: python3 gerar.py
Base legal conferida no portal do Planalto em 26/11/2026: CF/88 (arts. 37 a 41), Lei nº 8.112/1990, Lei nº 8.429/1992
e Lei nº 13.869/2019 (art. 2º)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit
from kit import *

DATA = "26 de novembro de 2026"
kit.U = {1:("UNIDADE 1","Conceito e categorias"),2:("UNIDADE 2","Cargo, emprego, função e concurso"),3:("UNIDADE 3","Direitos e deveres"),4:("UNIDADE 4","Responsabilidades"),5:("UNIDADE 5","Regime disciplinar")}
def cf(x): return f"{x} · Constituição Federal"
def L8112(x): return f"{x} · Lei nº 8.112/1990"

# ================================================================ APRESENTAÇÃO
add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar este <span class="hl">caderno</span></h1>
<p class="lead">Quem são as pessoas que atuam em nome do Estado, como entram, o que podem e devem fazer e como respondem pelos seus atos.</p>
<p>Este é o <strong>Caderno 12 da coleção</strong>, o quarto de <strong>Direito Administrativo</strong>. Ele trata dos <strong>agentes públicos</strong>: as categorias (agentes políticos, servidores, particulares em colaboração), a diferença entre <strong>cargo, emprego e função</strong>, o <strong>concurso público</strong>, os <strong>direitos e deveres</strong>, as <strong>responsabilidades</strong> civil, penal e administrativa e as noções de <strong>regime disciplinar</strong>.</p>
<p>As regras gerais estão na <strong>Constituição</strong> (arts. 37 a 41). O detalhamento usado como referência é a <strong>Lei nº 8.112/1990</strong>, o estatuto dos servidores federais. <strong>Atenção:</strong> cada Estado e cada Município tem o seu próprio estatuto. Se o edital do seu concurso cobrar o estatuto local (por exemplo, o estatuto dos servidores do seu Município), leia-o: os prazos e as penalidades podem ser diferentes.</p>
{table(["Recurso","Onde está"],[["Diagrama das categorias de agentes públicos","Unidade 1"],["Cargo x emprego x função (cenas e quadro)","Unidade 2"],["Linha do tempo do concurso à estabilidade","Unidades 2 e 3"],["Diagrama da tripla responsabilidade","Unidade 4"],["Fluxo do processo disciplinar e quadro de penalidades","Unidade 5"],["Mapa conceitual, erros mais comuns e 24 questões autorais","Revisão e prática"]],["58%",None])}
{lembre(p(f'Constituição (arts. 37 a 41), Lei nº 8.112/1990, Lei nº 8.429/1992 (improbidade, com a redação da Lei nº 14.230/2021) e Lei nº 13.869/2019 (art. 2º) conferidas no portal do Planalto em <strong>{DATA}</strong>.'), "Fontes e atualização")}''', first=True)

toc_page([("u","UNIDADE 1 · CONCEITO E CATEGORIAS","U1"),("","1. Conceito de agente público","A01"),("","2. Categorias (diagrama)","A02"),("","3. Agentes políticos","A03"),("","4. Servidores públicos","A04"),("","5. Particulares em colaboração","A05"),
 ("u","UNIDADE 2 · CARGO, EMPREGO, FUNÇÃO E CONCURSO","U2"),("","6. Cargo x emprego x função","A06"),("","7. Cargo em comissão x função de confiança","A07"),("","8. Concurso público","A08"),("","9. Provimento","A09"),
 ("u","UNIDADE 3 · DIREITOS E DEVERES","U3"),("","10. Estágio probatório e estabilidade","A10"),("","11. Principais direitos","A11"),("","12. Deveres e proibições","A12"),
 ("u","UNIDADE 4 · RESPONSABILIDADES","U4"),("","13. A tripla responsabilidade","A13"),("","14. Responsabilidade civil","A14"),("","15. Responsabilidade penal e administrativa","A15"),("","16. Noções de improbidade administrativa","A16"),
 ("u","UNIDADE 5 · NOÇÕES DE REGIME DISCIPLINAR","U5"),("","17. Penalidades disciplinares","A17"),("","18. Sindicância e processo disciplinar","A18"),("","19. Competência e prescrição","A19"),
 ("u","REVISÃO E PRÁTICA","RV"),("","Mapa conceitual · Erros mais comuns","R1"),("","Flashcards","R2"),("","Questões autorais","R3"),("","Gabarito, respostas dos treinos e referências","R4")])

# ================================================================ UNIDADE 1
opener("01","UNIDADE 1","Conceito e categorias",["Conceito de agente público","Categorias","Agentes políticos","Servidores públicos","Particulares em colaboração"],"U1")

add(H(1,'Conceito de <span class="hl">agente público</span>','A expressão mais ampla: todos os que atuam pelo Estado.', "A01") +
 oque(p('<strong>Agente público</strong> é toda pessoa física que exerce, ainda que de forma <strong>transitória</strong> ou <strong>sem remuneração</strong>, uma função pública, por <strong>qualquer forma de vínculo</strong>: eleição, nomeação, designação, contratação ou outra forma de investidura.')) +
 lei("Art. 2º, parágrafo único · Lei nº 13.869/2019 (em síntese)",'<p>Reputa-se agente público todo aquele que exerce, ainda que transitoriamente ou sem remuneração, por eleição, nomeação, designação, contratação ou qualquer outra forma de investidura ou vínculo, mandato, cargo, emprego ou função em órgão ou entidade da Administração Pública.</p>') +
 traduz(p('"Agente público" é o <strong>gênero</strong>: abrange do Presidente da República ao mesário da eleição. "Servidor público" é uma <strong>espécie</strong> dentro desse gênero. A Lei de Improbidade (Lei nº 8.429/1992) e a Lei de Abuso de Autoridade usam conceitos amplos parecidos com esse, para alcançar todos os que atuam em nome do Estado.')) +
 memo('Agente público = <strong>gênero</strong> (todos os que exercem função pública, mesmo transitória ou sem remuneração). Servidor público = <strong>espécie</strong>.'))

def categorias():
    N,G,O=C['navy'],C['blue'],C['golddeep']
    s = f'<figure><svg viewBox="0 0 640 290" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    s += '<g stroke="#9db0c8" stroke-width="2.5" fill="none"><path d="M320 50 V66 M110 66 H530 M110 66 V82 M320 66 V82 M530 66 V82 M320 142 V156 M216 156 H424 M216 156 V170 M320 156 V170 M424 156 V170"/></g>'
    s += f'<rect x="200" y="6" width="240" height="44" rx="12" fill="{N}"/><text x="320" y="26" text-anchor="middle" font-size="13" font-weight="900" fill="#fff">AGENTES PÚBLICOS</text><text x="320" y="42" text-anchor="middle" font-size="10" fill="#cfe0f2">gênero</text>'
    for x,t,a,b,fg,bg in [(110,"AGENTES POLÍTICOS","cúpula do Estado:","mandato ou cargo político",O,C['goldsoft']),(320,"SERVIDORES PÚBLICOS","vínculo profissional","com a Administração",G,C['sky']),(530,"PARTICULARES EM COLABORAÇÃO","sem perder a condição","de particular",C['red'],C['redsoft'])]:
        s += f'<rect x="{x-98}" y="82" width="196" height="60" rx="12" fill="{bg}" stroke="{fg}" stroke-width="2.4"/><text x="{x}" y="104" text-anchor="middle" font-size="{11.5 if len(t)<22 else 10.2}" font-weight="900" fill="{fg}">{t}</text><text x="{x}" y="120" text-anchor="middle" font-size="9.8" fill="{C["ink"]}">{a}</text><text x="{x}" y="134" text-anchor="middle" font-size="9.8" fill="{C["ink"]}">{b}</text>'
    for x,t,a,b in [(216,"ESTATUTÁRIOS","cargo público","regime legal (estatuto)"),(320,"EMPREGADOS","emprego público","regime da CLT"),(424,"TEMPORÁRIOS","função temporária","CF, art. 37, IX")]:
        s += f'<rect x="{x-48}" y="170" width="96" height="62" rx="10" fill="#fff" stroke="{G}" stroke-width="2"/><text x="{x}" y="192" text-anchor="middle" font-size="9.4" font-weight="900" fill="{C["ink"]}">{t}</text><text x="{x}" y="208" text-anchor="middle" font-size="8.2" fill="{C["muted"]}">{a}</text><text x="{x}" y="222" text-anchor="middle" font-size="8.2" fill="{C["muted"]}">{b}</text>'
    s += f'<text x="110" y="168" text-anchor="middle" font-size="9.6" fill="{O}">Presidente, governadores,</text><text x="110" y="182" text-anchor="middle" font-size="9.6" fill="{O}">prefeitos, parlamentares,</text><text x="110" y="196" text-anchor="middle" font-size="9.6" fill="{O}">ministros e secretários</text>'
    s += f'<text x="482" y="168" font-size="9.6" fill="{C["red"]}">requisitados: mesários, jurados</text><text x="482" y="182" font-size="9.6" fill="{C["red"]}">delegados: concessionários,</text><text x="482" y="196" font-size="9.6" fill="{C["red"]}">notários e registradores</text><text x="482" y="210" font-size="9.6" fill="{C["red"]}">voluntários (gestores</text><text x="482" y="224" font-size="9.6" fill="{C["red"]}">de negócio)</text>'
    s += f'<text x="320" y="268" text-anchor="middle" font-size="10" fill="{C["muted"]}">Parte da doutrina inclui uma quarta categoria: os militares (CF, arts. 42 e 142), com regime próprio.</text>'
    return s + '</svg><figcaption>Categorias de agentes públicos (classificação doutrinária mais cobrada).</figcaption></figure>'

add(H(1,'Categorias de <span class="hl">agentes públicos</span>','Três grandes grupos (classificação doutrinária).', "A02") +
 categorias() +
 memo('Três categorias: <strong>políticos</strong> (cúpula), <strong>servidores</strong> (vínculo profissional: estatutários, empregados e temporários) e <strong>particulares em colaboração</strong> (requisitados, delegados e voluntários).'))

add(H(1,'Agentes <span class="hl">políticos</span>','A cúpula do Estado.', "A03") +
 oque(p('São os agentes que ocupam os <strong>cargos estruturais</strong> do Estado e formam a vontade superior do poder público. Exercem <strong>funções políticas</strong>, com atribuições previstas diretamente na <strong>Constituição</strong>, e, em regra, chegam ao cargo por <strong>eleição</strong> ou por <strong>nomeação política</strong>.')) +
 table(["Agentes políticos (exemplos)","Como chegam ao cargo"],[
  ["Presidente, governadores e prefeitos (e vices)","Eleição"],
  ["Senadores, deputados e vereadores","Eleição"],
  ["Ministros de Estado e secretários estaduais e municipais","Nomeação política (livre escolha do Chefe do Executivo)"],
  ["Magistrados e membros do Ministério Público","Parte da doutrina e o STF os incluem entre os agentes políticos; outra parte os considera servidores com regime especial"]],["50%",None]) +
 ex(p('O prefeito e os vereadores de uma cidade são agentes políticos eleitos. Quando o prefeito nomeia o secretário de Segurança, essa nomeação também cria um agente político, de livre escolha. Já o guarda municipal aprovado em concurso é <b>servidor público</b> estatutário, e não agente político.')) +
 memo('Agentes políticos: <strong>cúpula</strong> do Estado, atribuições na <strong>Constituição</strong>, em regra por <strong>eleição</strong> ou <strong>nomeação política</strong>.'))

add(H(1,'Servidores <span class="hl">públicos</span>','Os profissionais da Administração.', "A04") +
 table(["","ESTATUTÁRIOS","EMPREGADOS PÚBLICOS","TEMPORÁRIOS"],[
  ["Ocupam","<b>Cargo</b> público","<b>Emprego</b> público","<b>Função</b> pública temporária"],
  ["Regime","<b>Estatuto</b> (lei), como a Lei nº 8.112/1990","<b>CLT</b> (contrato de trabalho)","Regime especial da lei de cada ente"],
  ["Ingresso","Concurso público (cargo efetivo) ou livre nomeação (cargo em comissão)","Concurso público","Processo seletivo simplificado, para necessidade temporária de excepcional interesse público (CF, art. 37, IX)"],
  ["Onde estão","Administração direta, autarquias e fundações de direito público","Em regra, empresas públicas e sociedades de economia mista","Qualquer ente, por prazo determinado"],
  ["Estabilidade","Sim, após 3 anos, para o efetivo (CF, art. 41)","Não têm a estabilidade do art. 41","Não"]],["16%",None,None,None]) +
 lembre(p('O regime jurídico único obrigatório foi afastado: em <strong>2024</strong>, no julgamento da <strong>ADI 2.135</strong>, o STF validou a mudança da EC nº 19/1998, e os entes passaram a poder contratar novos servidores também pelo regime da CLT, sem efeito retroativo para quem já é estatutário. O alcance prático ainda é debatido.'), "Regime de pessoal: decisão do STF") +
 memo('Estatutário = <strong>cargo</strong> + <strong>estatuto</strong>. Empregado = <strong>emprego</strong> + <strong>CLT</strong>. Temporário = <strong>função</strong> + <strong>art. 37, IX</strong>.'))

add(H(1,'Particulares em <span class="hl">colaboração</span>','Pessoas que colaboram com o Estado sem deixar de ser particulares.', "A05") +
 table(["Modalidade","Quem são","Exemplos"],[
  ["Requisitados (ou honoríficos)","Convocados para prestar um serviço público relevante, em regra sem remuneração","Mesários eleitorais, jurados do Tribunal do Júri, convocados para o serviço militar"],
  ["Delegados","Recebem, por delegação, a execução de um serviço público, por sua conta e risco","Concessionários e permissionários de serviço público; notários e registradores (CF, art. 236)"],
  ["Voluntários (gestores de negócios)","Assumem espontaneamente uma tarefa pública em situação de emergência","Pessoa que ajuda no resgate de vítimas durante uma enchente"],
  ["Credenciados","Recebem a incumbência de representar a Administração em determinado ato","Particular credenciado para representar o país em um evento"]],["24%",None,"34%"]) +
 ex(p('Maria é professora em escola particular e é convocada para trabalhar como <b>mesária</b> nas eleições. Naquele dia, ela é <b>agente pública</b> (particular em colaboração, requisitada) e, se cometer um crime no exercício dessa função, pode responder como funcionária pública para fins penais (CP, art. 327).')) +
 memo('Particulares em colaboração: <strong>requisitados</strong> (mesário, jurado), <strong>delegados</strong> (concessionários, cartórios), <strong>voluntários</strong> e <strong>credenciados</strong>.'))

treino(1, [
 ("Agente público é expressão mais ampla que servidor público.","C","Agente é o gênero; servidor, a espécie."),
 ("Quem exerce função pública sem remuneração não é considerado agente público.","E","O conceito alcança quem atua transitoriamente ou sem remuneração."),
 ("Ministros de Estado e secretários municipais são exemplos de agentes políticos.","C","Nomeação política."),
 ("O empregado público ocupa cargo público e é regido pelo estatuto.","E","Ocupa emprego público, regido pela CLT."),
 ("O mesário eleitoral é exemplo de particular em colaboração com o Poder Público.","C","Requisitado."),
 ("Os servidores temporários são contratados para atender a necessidade temporária de excepcional interesse público.","C","CF, art. 37, IX.")])

# ================================================================ UNIDADE 2
opener("02","UNIDADE 2","Cargo, emprego, função e concurso",["Cargo x emprego x função","Cargo em comissão x função de confiança","Concurso público","Provimento"],"U2")

cef = scene3([("CARGO",C['navy'],NV,"prof",["Lugar criado por lei,","com atribuições e","vencimento próprios."],"ESTATUTÁRIO"),
 ("EMPREGO",C['blue'],C['sky'],"profa",["Vínculo de trabalho","regido pela CLT,","com concurso."],"CELETISTA"),
 ("FUNÇÃO",C['golddeep'],C['goldsoft'],"prof",["Atribuição sem cargo","próprio: confiança","ou temporária."],"SEM CARGO")], "Situação ilustrada: três formas de ocupar um posto público.")
add(H(2,'Cargo x emprego x <span class="hl">função</span>','Três palavras que a prova adora trocar.', "A06") + cef +
 lei(L8112("Art. 3º"),'<p>Art. 3º Cargo público é o conjunto de atribuições e responsabilidades previstas na estrutura organizacional que devem ser cometidas a um servidor.<br>Parágrafo único. Os cargos públicos, acessíveis a todos os brasileiros, são criados por lei, com denominação própria e vencimento pago pelos cofres públicos, para provimento em caráter efetivo ou em comissão.</p>') +
 table(["","CARGO","EMPREGO","FUNÇÃO"],[
  ["Vínculo","Estatutário","Contratual (CLT)","Sem cargo nem emprego próprio"],
  ["Criação","Por lei","Por lei","Atribuições de confiança ou temporárias"],
  ["Exemplos","Guarda municipal, técnico judiciário, policial civil","Empregado da Caixa ou dos Correios","Função de confiança de chefe de seção; contratado temporário"]],["14%",None,None,None]))

add(H(2,'Cargo em comissão x <span class="hl">função de confiança</span>','Direção, chefia e assessoramento.', "A07") +
 lei(cf("Art. 37, V"),'<p>V - as funções de confiança, exercidas exclusivamente por servidores ocupantes de cargo efetivo, e os cargos em comissão, a serem preenchidos por servidores de carreira nos casos, condições e percentuais mínimos previstos em lei, destinam-se apenas às atribuições de direção, chefia e assessoramento;</p>') +
 table(["","CARGO EM COMISSÃO","FUNÇÃO DE CONFIANÇA"],[
  ["Quem pode ocupar","Qualquer pessoa (inclusive de fora do serviço público), respeitado o percentual mínimo reservado a servidores de carreira","<b>Somente</b> servidor ocupante de <b>cargo efetivo</b>"],
  ["Ingresso","Livre nomeação e exoneração (sem concurso)","Designação de quem já é servidor efetivo"],
  ["Finalidade","Direção, chefia e assessoramento","Direção, chefia e assessoramento"],
  ["Estabilidade","Não há (exoneração <i>ad nutum</i>)","O servidor perde a função, mas mantém o cargo efetivo"]],["20%",None,None]) +
 ex(p('O prefeito nomeia um advogado de fora da Prefeitura como assessor jurídico do gabinete: <b>cargo em comissão</b>. Já o guarda municipal concursado que é designado para chefiar uma equipe e recebe uma gratificação exerce <b>função de confiança</b>. Se deixar a chefia, continua guarda municipal.')) +
 memo('<strong>Função de confiança</strong>: só para quem já é <strong>efetivo</strong>. <strong>Cargo em comissão</strong>: qualquer pessoa, com percentual mínimo para servidores de carreira. Ambos: <strong>direção, chefia e assessoramento</strong>.'))

def linha_concurso():
    N,G,O=C['navy'],C['blue'],C['golddeep']
    it=[("EDITAL","regras do","concurso",N,NV),("PROVAS","provas ou provas","e títulos",G,C['sky']),("HOMOLOGAÇÃO","resultado e início","da validade",O,C['goldsoft']),("NOMEAÇÃO","dentro da","validade",C['red'],C['redsoft']),("POSSE E","EXERCÍCIO","",C['green'],C['greensoft'])]
    s = f'<figure><svg viewBox="0 0 640 140" width="610" xmlns="http://www.w3.org/2000/svg" font-family="Inter">{arrowdefs("lc")}'
    for k,(t,a,b,fg,bg) in enumerate(it):
        x=4+k*127
        s += f'<rect x="{x}" y="10" width="112" height="78" rx="12" fill="{bg}" stroke="{fg}" stroke-width="2.4"/><text x="{x+56}" y="38" text-anchor="middle" font-size="11.5" font-weight="900" fill="{fg}">{t}</text><text x="{x+56}" y="58" text-anchor="middle" font-size="9.8" fill="{C["ink"]}">{a}</text><text x="{x+56}" y="74" text-anchor="middle" font-size="9.8" fill="{C["ink"]}">{b}</text>'
        if k<4: s += f'<line x1="{x+114}" y1="49" x2="{x+125}" y2="49" stroke="{C["ink"]}" stroke-width="2.4" marker-end="url(#lc)"/>'
    s += f'<text x="320" y="112" text-anchor="middle" font-size="10.5" font-weight="800" fill="{N}">Validade do concurso: até 2 anos, prorrogável uma vez por igual período (CF, art. 37, III)</text>'
    s += f'<text x="320" y="130" text-anchor="middle" font-size="10" fill="{C["muted"]}">Aprovado dentro do número de vagas do edital: direito à nomeação dentro da validade (STF)</text>'
    return s + '</svg><figcaption>Linha do tempo do concurso público.</figcaption></figure>'

add(H(2,'Concurso <span class="hl">público</span>','A regra para entrar em cargo efetivo ou emprego público.', "A08") +
 lei(cf("Art. 37, I a IV"),'<p>I - os cargos, empregos e funções públicas são acessíveis aos brasileiros que preencham os requisitos estabelecidos em lei, assim como aos estrangeiros, na forma da lei;<br>II - a investidura em cargo ou emprego público depende de aprovação prévia em concurso público de provas ou de provas e títulos, de acordo com a natureza e a complexidade do cargo ou emprego, na forma prevista em lei, ressalvadas as nomeações para cargo em comissão declarado em lei de livre nomeação e exoneração;<br>III - o prazo de validade do concurso público será de até dois anos, prorrogável uma vez, por igual período;<br>IV - durante o prazo improrrogável previsto no edital de convocação, aquele aprovado em concurso público de provas ou de provas e títulos será convocado com prioridade sobre novos concursados para assumir cargo ou emprego, na carreira;</p>') +
 linha_concurso() +
 table(["Ponto importante","Regra"],[
  ["Exceções ao concurso","Cargos em comissão, temporários (art. 37, IX), agentes políticos eleitos e cargos com forma própria de escolha na Constituição (ex.: ministros de tribunais)"],
  ["Exame psicotécnico","Só pode ser exigido se previsto em <b>lei</b> (Súmula Vinculante 44)"],
  ["Provimento derivado","É inconstitucional investir o servidor, sem concurso, em cargo de outra carreira (Súmula Vinculante 43)"],
  ["Reserva para pessoas com deficiência","A lei reservará percentual de cargos e empregos (CF, art. 37, VIII)"]],["28%",None]))

add(H(2,'<span class="hl">Provimento</span>','Como alguém passa a ocupar um cargo.', "A09") +
 table(["Forma de provimento (Lei nº 8.112/1990, art. 8º)","Em que consiste (em síntese)"],[
  ["Nomeação","Única forma de provimento <b>originário</b>: o primeiro ingresso no cargo"],
  ["Promoção","Elevação a classe ou padrão superior dentro da carreira"],
  ["Readaptação","Investidura em cargo compatível com a limitação de capacidade física ou mental verificada em inspeção médica"],
  ["Reversão","Retorno à atividade do servidor aposentado"],
  ["Aproveitamento","Retorno do servidor em disponibilidade a cargo de atribuições compatíveis"],
  ["Reintegração","Retorno do servidor estável cuja demissão foi invalidada"],
  ["Recondução","Retorno do servidor estável ao cargo anteriormente ocupado (ex.: inabilitação em estágio probatório de outro cargo)"]],["30%",None]) +
 lembre(p('A Lei nº 8.112/1990 também listava a <strong>ascensão</strong> e a <strong>transferência</strong>, que foram <strong>revogadas</strong> pela Lei nº 9.527/1997. Essas formas permitiam mudar de carreira sem concurso, o que o STF considera inconstitucional (Súmula Vinculante 43).'), "Formas revogadas") +
 memo('Nomeação = provimento <strong>originário</strong>. As demais são <strong>derivadas</strong>. Ascensão e transferência foram <strong>revogadas</strong>. Após a nomeação vêm a <strong>posse</strong> e o <strong>exercício</strong>.'))

treino(2, [
 ("A função de confiança pode ser exercida por qualquer pessoa, inclusive sem vínculo com a Administração.","E","Somente por servidores ocupantes de cargo efetivo (CF, art. 37, V)."),
 ("O cargo em comissão destina-se apenas às atribuições de direção, chefia e assessoramento.","C","CF, art. 37, V."),
 ("O prazo de validade do concurso público é de até dois anos, prorrogável uma vez, por igual período.","C","CF, art. 37, III."),
 ("A investidura em cargo em comissão depende de aprovação prévia em concurso público.","E","Cargos em comissão são de livre nomeação e exoneração."),
 ("A nomeação é a forma de provimento originário.","C","As demais são derivadas."),
 ("O exame psicotécnico pode ser exigido em concurso mesmo sem previsão em lei, se previsto no edital.","E","Só por lei (Súmula Vinculante 44).")])

# ================================================================ UNIDADE 3
opener("03","UNIDADE 3","Direitos e deveres",["Estágio probatório e estabilidade","Principais direitos","Deveres e proibições"],"U3")

add(H(3,'Estágio probatório e <span class="hl">estabilidade</span>','Da posse à segurança no cargo.', "A10") +
 lei(cf("Art. 41, caput, §§ 1º e 4º"),'<p>Art. 41. São estáveis após três anos de efetivo exercício os servidores nomeados para cargo de provimento efetivo em virtude de concurso público.<br>§ 1º O servidor público estável só perderá o cargo: I - em virtude de sentença judicial transitada em julgado; II - mediante processo administrativo em que lhe seja assegurada ampla defesa; III - mediante procedimento de avaliação periódica de desempenho, na forma de lei complementar, assegurada ampla defesa.<br>§ 4º Como condição para a aquisição da estabilidade, é obrigatória a avaliação especial de desempenho por comissão instituída para essa finalidade.</p>') +
 table(["","ESTÁGIO PROBATÓRIO","ESTABILIDADE"],[
  ["O que é","Período de avaliação da aptidão do servidor para o cargo","Garantia de permanência no serviço público"],
  ["Prazo","A Lei nº 8.112/1990 (art. 20) fala em 24 meses; a jurisprudência do STF e do STJ entende que o estágio acompanha os <b>3 anos</b> da estabilidade","Após <b>3 anos</b> de efetivo exercício + avaliação especial de desempenho"],
  ["Fatores avaliados (art. 20)","Assiduidade, disciplina, capacidade de iniciativa, produtividade e responsabilidade","—"],
  ["Quem tem","Servidor nomeado para cargo efetivo","Servidor <b>efetivo</b>, aprovado em <b>concurso</b> (não alcança comissionados e empregados públicos)"]],["18%",None,None]) +
 memo('Estabilidade: <strong>3 anos</strong> + <strong>avaliação especial</strong> + cargo <strong>efetivo</strong> por <strong>concurso</strong>. O estável só perde o cargo por <strong>sentença transitada em julgado</strong>, <strong>processo administrativo</strong> ou <strong>avaliação periódica</strong> (e também por excesso de despesa com pessoal, CF, art. 169).'))

add(H(3,'Principais <span class="hl">direitos</span>','O que a Constituição e o estatuto garantem.', "A11") +
 table(["Direito","Regra (em síntese)"],[
  ["Associação sindical (CF, art. 37, VI)","Garantida ao servidor público civil"],
  ["Greve (CF, art. 37, VII)","Exercida nos termos e limites de <b>lei específica</b>; enquanto ela não existe, o STF manda aplicar, no que couber, a lei de greve do setor privado"],
  ["Remuneração","Vencimento e vantagens fixados em lei, com teto constitucional (CF, art. 37, XI) e irredutibilidade (art. 37, XV)"],
  ["Férias, licenças e afastamentos","Previstos no estatuto de cada ente (na Lei nº 8.112/1990: férias de 30 dias, licenças por motivo de doença em pessoa da família, para capacitação, entre outras)"],
  ["Acumulação de cargos (CF, art. 37, XVI)","Em regra, <b>vedada</b>; permitida, com compatibilidade de horários e teto, para: dois cargos de professor; um de professor com outro de qualquer natureza (redação da EC nº 138/2025); dois cargos ou empregos privativos de profissionais de saúde com profissões regulamentadas"],
  ["Aposentadoria","Regras do art. 40 da Constituição (regime próprio). A compulsória ocorre aos 70 anos ou, na forma de lei complementar, aos 75 anos (a Lei Complementar nº 152/2015 fixou os 75 anos)"]],["30%",None]) +
 lembre(p('A <strong>EC nº 138/2025</strong> ampliou a hipótese de acumulação: hoje é permitido acumular <strong>um cargo de professor com outro de qualquer natureza</strong> (antes, exigia-se que o outro fosse técnico ou científico), sempre com compatibilidade de horários e respeitado o teto.'), "Atualização constitucional"))

add(H(3,'Deveres e <span class="hl">proibições</span>','O que o servidor deve fazer e o que não pode fazer.', "A12") +
 table(["Deveres (Lei nº 8.112/1990, art. 116, exemplos)","Proibições (art. 117, exemplos)"],[
  ["Exercer com zelo e dedicação as atribuições do cargo","Ausentar-se do serviço durante o expediente sem prévia autorização do chefe"],
  ["Ser leal às instituições a que servir","Valer-se do cargo para lograr proveito pessoal ou de outrem"],
  ["Cumprir as ordens superiores, exceto quando manifestamente ilegais","Receber propina, comissão, presente ou vantagem de qualquer espécie em razão de suas atribuições"],
  ["Levar as irregularidades ao conhecimento da autoridade superior","Manter sob sua chefia imediata, em cargo ou função de confiança, cônjuge, companheiro ou parente até o segundo grau civil"],
  ["Guardar sigilo sobre assuntos da repartição","Proceder de forma desidiosa"],
  ["Ser assíduo e pontual; tratar as pessoas com urbanidade","Utilizar pessoal ou recursos materiais da repartição em serviços ou atividades particulares"],
  ["Representar contra ilegalidade, omissão ou abuso de poder","Participar de gerência ou administração de sociedade privada, ressalvadas as exceções legais"]],["50%",None]) +
 lembre(p('Nenhum servidor pode ser responsabilizado civil, penal ou administrativamente por dar ciência à autoridade superior (ou a outra autoridade competente) de informação sobre crimes ou improbidade de que tenha conhecimento (Lei nº 8.112/1990, art. 126-A, incluído pela Lei nº 12.527/2011).'), "Proteção de quem denuncia") +
 memo('Ordem <strong>manifestamente ilegal</strong> não se cumpre. Descumprir certas proibições do art. 117 (como valer-se do cargo para proveito pessoal ou receber propina) leva à <strong>demissão</strong> (art. 132, XIII).'))

treino(3, [
 ("São estáveis após três anos de efetivo exercício os servidores nomeados para cargo efetivo em virtude de concurso público.","C","CF, art. 41."),
 ("A avaliação especial de desempenho é condição para a aquisição da estabilidade.","C","CF, art. 41, § 4º."),
 ("O servidor ocupante exclusivamente de cargo em comissão adquire estabilidade após três anos.","E","Estabilidade é de servidor efetivo aprovado em concurso."),
 ("O direito de greve do servidor público será exercido nos termos e limites definidos em lei específica.","C","CF, art. 37, VII."),
 ("Após a EC nº 138/2025, é permitida a acumulação de um cargo de professor com outro de qualquer natureza, havendo compatibilidade de horários.","C","CF, art. 37, XVI, b."),
 ("O servidor deve cumprir as ordens superiores, ainda que manifestamente ilegais.","E","Exceto as manifestamente ilegais (art. 116, IV).")])

# ================================================================ UNIDADE 4
opener("04","UNIDADE 4","Responsabilidades",["A tripla responsabilidade","Responsabilidade civil","Responsabilidade penal e administrativa","Noções de improbidade"],"U4")

def tripla():
    N,G,O,R=C['navy'],C['blue'],C['golddeep'],C['red']
    s = f'<figure><svg viewBox="0 0 640 230" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">'
    s += f'<rect x="220" y="6" width="200" height="54" rx="12" fill="{N}"/><text x="320" y="28" text-anchor="middle" font-size="12.5" font-weight="900" fill="#fff">UM MESMO FATO</text><text x="320" y="46" text-anchor="middle" font-size="10" fill="#cfe0f2">praticado pelo servidor</text>'
    s += '<g stroke="#9db0c8" stroke-width="2.5" fill="none"><path d="M320 60 V78 M110 78 H530 M110 78 V94 M320 78 V94 M530 78 V94"/></g>'
    for x,t,a,b,c,fg,bg in [(110,"CIVIL","reparar o dano","ao erário ou a terceiros","art. 122",G,C['sky']),(320,"PENAL","crimes e","contravenções","art. 123",R,C['redsoft']),(530,"ADMINISTRATIVA","infração funcional:","sanção disciplinar","art. 124",O,C['goldsoft'])]:
        s += f'<rect x="{x-95}" y="94" width="190" height="84" rx="12" fill="{bg}" stroke="{fg}" stroke-width="2.4"/><text x="{x}" y="118" text-anchor="middle" font-size="13" font-weight="900" fill="{fg}">{t}</text><text x="{x}" y="138" text-anchor="middle" font-size="10" fill="{C["ink"]}">{a}</text><text x="{x}" y="153" text-anchor="middle" font-size="10" fill="{C["ink"]}">{b}</text><text x="{x}" y="170" text-anchor="middle" font-size="9.5" font-weight="800" fill="{C["muted"]}">Lei nº 8.112/1990, {c}</text>'
    s += f'<text x="320" y="204" text-anchor="middle" font-size="11" font-weight="900" fill="{N}">Art. 125: as sanções podem cumular-se e são independentes entre si.</text>'
    s += f'<text x="320" y="222" text-anchor="middle" font-size="10" fill="{C["muted"]}">Exceção (art. 126): absolvição criminal que negue a existência do fato ou a autoria afasta a responsabilidade administrativa.</text>'
    return s + '</svg><figcaption>A tripla responsabilidade do servidor.</figcaption></figure>'

add(H(4,'A tripla <span class="hl">responsabilidade</span>','Um fato, três esferas.', "A13") +
 lei(L8112("Arts. 121 e 125"),'<p>Art. 121. O servidor responde civil, penal e administrativamente pelo exercício irregular de suas atribuições.<br>Art. 125. As sanções civis, penais e administrativas poderão cumular-se, sendo independentes entre si.</p>') +
 tripla() +
 memo('Três esferas <strong>independentes</strong> que podem se <strong>cumular</strong>. Só a absolvição penal por <strong>inexistência do fato</strong> ou <strong>negativa de autoria</strong> afasta a responsabilidade administrativa.'))

add(H(4,'Responsabilidade <span class="hl">civil</span>','Reparar o dano.', "A14") +
 lei(cf("Art. 37, § 6º"),'<p>§ 6º As pessoas jurídicas de direito público e as de direito privado prestadoras de serviços públicos responderão pelos danos que seus agentes, nessa qualidade, causarem a terceiros, assegurado o direito de regresso contra o responsável nos casos de dolo ou culpa.</p>') +
 flow([("car",["VIATURA","da Guarda","colide"]),("person",["VÍTIMA","processa o","MUNICÍPIO"]),("scales",["ESTADO","responde de forma","OBJETIVA"]),("gavel",["REGRESSO","contra o guarda","se houver dolo ou culpa"])],
      "Dano a terceiro: o Estado responde objetivamente e cobra do agente se houver dolo ou culpa.", colors=colors("n","b","o","r")) +
 table(["Ponto","Regra"],[
  ["Dano ao erário (Lei nº 8.112/1990, art. 122)","O servidor responde por ato omissivo ou comissivo, <b>doloso ou culposo</b>, que cause prejuízo ao erário"],
  ["Dano a terceiros","O <b>Estado</b> responde de forma <b>objetiva</b> (sem precisar provar culpa); depois cobra do servidor, em <b>ação regressiva</b>, se houver dolo ou culpa (art. 122, § 2º)"],
  ["Contra quem a vítima entra com a ação","Segundo o STF (Tema 940), a ação deve ser proposta contra o <b>Estado</b> (ou a prestadora de serviço público), e não diretamente contra o agente: a chamada <b>dupla garantia</b>"]],["30%",None]))

add(H(4,'Responsabilidade <span class="hl">penal e administrativa</span>','Crime e infração funcional.', "A15") +
 table(["","RESPONSABILIDADE PENAL","RESPONSABILIDADE ADMINISTRATIVA"],[
  ["Base (Lei nº 8.112/1990)","Art. 123: crimes e contravenções imputados ao servidor nessa qualidade","Art. 124: ato omissivo ou comissivo praticado no desempenho do cargo ou função"],
  ["Quem apura","Polícia, Ministério Público e Poder Judiciário","A própria Administração (sindicância ou processo disciplinar)"],
  ["Exemplos","Peculato, corrupção passiva, concussão (CP, arts. 312 a 317)","Faltas ao serviço, desídia, descumprimento de dever"],
  ["Conceito de funcionário","Amplo (CP, art. 327): inclui quem exerce função pública transitória ou sem remuneração","Definido pelo estatuto de cada ente"]],["18%",None,None]) +
 lei(L8112("Art. 126"),'<p>Art. 126. A responsabilidade administrativa do servidor será afastada no caso de absolvição criminal que negue a existência do fato ou sua autoria.</p>') +
 table(["Resultado no processo penal","Efeito no processo administrativo"],[
  ["Absolvição por <b>inexistência do fato</b>","<b>Afasta</b> a responsabilidade administrativa"],
  ["Absolvição por <b>negativa de autoria</b>","<b>Afasta</b> a responsabilidade administrativa"],
  ["Absolvição por <b>falta de provas</b>","<b>Não</b> afasta: a Administração pode punir com base nas suas próprias provas (falta residual)"],
  ["Condenação penal","Pode levar à perda do cargo como efeito da condenação, nos casos do CP, art. 92"]],["46%",None]))

add(H(4,'Noções de <span class="hl">improbidade</span> administrativa','Lei nº 8.429/1992, com a redação da Lei nº 14.230/2021.', "A16") +
 lei("Art. 1º, §§ 1º e 2º · Lei nº 8.429/1992 (em síntese e trechos)",'<p>§ 1º Consideram-se atos de improbidade administrativa as condutas dolosas tipificadas nos arts. 9º, 10 e 11 desta Lei. § 2º Considera-se dolo a vontade livre e consciente de alcançar o resultado ilícito tipificado nos arts. 9º, 10 e 11 desta Lei, não bastando a voluntariedade do agente.</p>') +
 table(["Espécie","Exemplo","Sanções principais (art. 12)"],[
  ["Enriquecimento ilícito (art. 9º)","Receber vantagem econômica para facilitar um contrato","Perda dos bens acrescidos, perda da função, suspensão dos direitos políticos até 14 anos, multa"],
  ["Prejuízo ao erário (art. 10)","Permitir, com dolo, a compra de bens por preço superior ao de mercado","Ressarcimento, perda da função, suspensão dos direitos políticos até 12 anos, multa"],
  ["Violação aos princípios (art. 11)","Revelar fato sigiloso para beneficiar alguém; nepotismo","Multa de até 24 vezes a remuneração e proibição de contratar com o poder público por até 4 anos (sem suspensão de direitos políticos)"]],["24%",None,"38%"]) +
 lembre(p('Após a Lei nº 14.230/2021, <strong>só existe improbidade dolosa</strong>: não há mais improbidade culposa. As sanções só podem ser executadas após o <strong>trânsito em julgado</strong> da condenação (art. 12, § 9º). A improbidade é apurada em <strong>ação judicial</strong> (cível), independente das esferas penal e administrativa.'), "Mudanças da reforma de 2021") +
 memo('Improbidade: <strong>só dolosa</strong> desde 2021. Três espécies: <strong>enriquecimento ilícito</strong>, <strong>prejuízo ao erário</strong> e <strong>violação aos princípios</strong>.'))

treino(4, [
 ("As sanções civis, penais e administrativas podem cumular-se, sendo independentes entre si.","C","Lei nº 8.112/1990, art. 125."),
 ("A absolvição criminal por falta de provas afasta automaticamente a responsabilidade administrativa.","E","Só a absolvição por inexistência do fato ou negativa de autoria afasta (art. 126)."),
 ("O Estado responde objetivamente pelos danos que seus agentes, nessa qualidade, causarem a terceiros.","C","CF, art. 37, § 6º."),
 ("O direito de regresso contra o agente depende da comprovação de dolo ou culpa.","C","CF, art. 37, § 6º."),
 ("Após a Lei nº 14.230/2021, admite-se improbidade administrativa na modalidade culposa.","E","Só condutas dolosas."),
 ("Segundo o STF, a vítima deve propor a ação de indenização contra o Estado, e não diretamente contra o agente.","C","Tema 940 (dupla garantia).")])

# ================================================================ UNIDADE 5
opener("05","UNIDADE 5","Noções de regime disciplinar",["Penalidades disciplinares","Sindicância e processo disciplinar","Competência e prescrição"],"U5")

add(H(5,'Penalidades <span class="hl">disciplinares</span>','Lei nº 8.112/1990, arts. 127 a 132.', "A17") +
 table(["Penalidade (art. 127)","Quando se aplica (em síntese)"],[
  ["I - Advertência","Infrações mais leves, como algumas proibições do art. 117 e descumprimento de dever, quando não justificar penalidade mais grave"],
  ["II - Suspensão","Reincidência em faltas punidas com advertência e violação das demais proibições que não levem à demissão; máximo de <b>90 dias</b> (art. 130)"],
  ["III - Demissão","Hipóteses graves do art. 132: crime contra a administração pública, abandono de cargo, inassiduidade habitual, improbidade, insubordinação grave, ofensa física em serviço, corrupção, acumulação ilegal, entre outras"],
  ["IV - Cassação de aposentadoria ou disponibilidade","Falta punível com demissão praticada quando o servidor ainda estava na ativa"],
  ["V - Destituição de cargo em comissão","Falta punível com suspensão ou demissão praticada por quem não ocupa cargo efetivo"],
  ["VI - Destituição de função comissionada","Prevista no mesmo art. 127"]],["30%",None]) +
 lei(L8112("Art. 128 (em síntese e parágrafo único)"),'<p>Na aplicação das penalidades serão consideradas a natureza e a gravidade da infração cometida, os danos que dela provierem para o serviço público, as circunstâncias agravantes ou atenuantes e os antecedentes funcionais. Parágrafo único. O ato de imposição da penalidade mencionará sempre o fundamento legal e a causa da sanção disciplinar.</p>') +
 memo('Seis penalidades: <strong>advertência, suspensão (até 90 dias), demissão, cassação, destituição de cargo em comissão e de função comissionada</strong>. Toda penalidade exige <strong>fundamento legal</strong> e <strong>causa</strong> no ato.'))

def pad():
    N,G,O,R=C['navy'],C['blue'],C['golddeep'],C['red']
    it=[("INSTAURAÇÃO","portaria e","comissão",N,NV),("INQUÉRITO","instrução, defesa","e relatório",G,C['sky']),("JULGAMENTO","decisão da","autoridade",O,C['goldsoft'])]
    s = f'<figure><svg viewBox="0 0 640 160" width="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter">{arrowdefs("pd")}'
    for k,(t,a,b,fg,bg) in enumerate(it):
        x=20+k*210
        s += f'<rect x="{x}" y="10" width="180" height="84" rx="14" fill="{bg}" stroke="{fg}" stroke-width="2.5"/><text x="{x+90}" y="40" text-anchor="middle" font-size="13.5" font-weight="900" fill="{fg}">{t}</text><text x="{x+90}" y="62" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">{a}</text><text x="{x+90}" y="78" text-anchor="middle" font-size="10.5" fill="{C["ink"]}">{b}</text>'
        if k<2: s += f'<line x1="{x+182}" y1="52" x2="{x+206}" y2="52" stroke="{C["ink"]}" stroke-width="2.5" marker-end="url(#pd)"/>'
    s += f'<text x="320" y="122" text-anchor="middle" font-size="10.5" font-weight="800" fill="{N}">Prazo do processo disciplinar: até 60 dias, prorrogável por igual prazo (art. 152)</text>'
    s += f'<text x="320" y="142" text-anchor="middle" font-size="10" fill="{C["muted"]}">Sindicância: até 30 dias, prorrogável por igual período (art. 145, parágrafo único)</text>'
    return s + '</svg><figcaption>As fases do processo administrativo disciplinar (PAD).</figcaption></figure>'

add(H(5,'Sindicância e <span class="hl">processo disciplinar</span>','Como a infração é apurada.', "A18") +
 lei(L8112("Art. 143, caput (em síntese e trecho)"),'<p>A autoridade que tiver ciência de irregularidade no serviço público "é obrigada a promover a sua apuração imediata, mediante sindicância ou processo administrativo disciplinar", assegurada ao acusado ampla defesa.</p>') +
 table(["","SINDICÂNCIA","PROCESSO ADMINISTRATIVO DISCIPLINAR (PAD)"],[
  ["Resultados possíveis (art. 145)","Arquivamento; aplicação de advertência ou suspensão de até 30 dias; ou instauração de PAD","Qualquer penalidade, inclusive demissão"],
  ["Obrigatório quando","—","A infração puder levar a suspensão de mais de 30 dias, demissão, cassação ou destituição"],
  ["Prazo","30 dias, prorrogável por igual período","60 dias, prorrogável por igual prazo"]],["22%",None,None]) +
 pad() +
 lembre(p('Segundo a <strong>Súmula Vinculante 5</strong> do STF, a falta de defesa técnica por advogado no processo administrativo disciplinar <strong>não ofende</strong> a Constituição. O contraditório e a ampla defesa continuam obrigatórios: o servidor deve ser ouvido, pode produzir provas e apresentar defesa.'), "Advogado no PAD"))

add(H(5,'Competência e <span class="hl">prescrição</span>','Quem pune e até quando.', "A19") +
 table(["Competência para aplicar (art. 141, em síntese)","Penalidade"],[
  ["Presidente da República, presidentes das Casas do Legislativo e dos tribunais federais e Procurador-Geral da República","Demissão e cassação de aposentadoria ou disponibilidade"],
  ["Autoridades imediatamente inferiores às do inciso anterior","Suspensão superior a 30 dias"],
  ["Chefe da repartição e outras autoridades, na forma dos regimentos","Advertência ou suspensão de até 30 dias"],
  ["Autoridade que fez a nomeação","Destituição de cargo em comissão"]],["56%",None]) +
 lei(L8112("Art. 142, incisos I a III"),'<p>I - em 5 (cinco) anos, quanto às infrações puníveis com demissão, cassação de aposentadoria ou disponibilidade e destituição de cargo em comissão; II - em 2 (dois) anos, quanto à suspensão; III - em 180 (cento e oitenta) dias, quanto à advertência.</p>') +
 memo('Prescrição da ação disciplinar (Lei nº 8.112/1990): <strong>5 anos</strong> (demissão, cassação, destituição), <strong>2 anos</strong> (suspensão), <strong>180 dias</strong> (advertência), contados de quando o fato se tornou <strong>conhecido</strong>.') +
 pega('<ul><li>Esses prazos são da Lei nº 8.112/1990 (servidores federais). Estatutos estaduais e municipais podem prever prazos diferentes.</li><li>A sindicância pode resultar em advertência ou suspensão de <b>até 30 dias</b>; penas maiores exigem PAD.</li><li>A suspensão máxima é de <b>90 dias</b>.</li></ul>'))

treino(5, [
 ("A suspensão disciplinar, na Lei nº 8.112/1990, não pode exceder 90 dias.","C","Art. 130."),
 ("Da sindicância pode resultar a aplicação de suspensão de até 60 dias.","E","Até 30 dias (art. 145, II)."),
 ("A autoridade que tiver ciência de irregularidade no serviço público é obrigada a promover sua apuração imediata.","C","Art. 143."),
 ("A ação disciplinar prescreve em 5 anos quanto às infrações puníveis com demissão.","C","Art. 142, I."),
 ("Segundo a Súmula Vinculante 5, a falta de defesa técnica por advogado no PAD ofende a Constituição.","E","Não ofende."),
 ("O prazo para conclusão do processo disciplinar não excede 60 dias, prorrogável por igual prazo.","C","Art. 152.")])

# ================================================================ REVISÃO
mapa(("AGENTES","PÚBLI-","COS"), [
  ("CATEGORIAS",["políticos · servidores","particulares em","colaboração"],C['navy'],NV),
  ("CARGO x EMPREGO",["cargo: estatuto","emprego: CLT","função: sem cargo próprio"],C['golddeep'],C['goldsoft']),
  ("CONCURSO",["2 anos + 2 (uma vez)","comissão: livre","psicotécnico só por lei"],C['blue'],C['sky']),
  ("ESTABILIDADE",["3 anos + avaliação","só cargo efetivo","perda: 3 hipóteses"],C['green'],C['greensoft']),
  ("RESPONSABILIDADES",["civil, penal, administrativa","independentes, cumuláveis","regresso: dolo ou culpa"],C['red'],C['redsoft']),
  ("DISCIPLINAR",["6 penalidades","sindicância: até 30 dias","prescrição: 5 · 2 · 180 dias"],C['navy'],NV)], "Mapa conceitual do Caderno 12.", "O caderno em seis blocos. Explique cada caixa em voz alta.")

erros([
  ["“Agente público e servidor público são sinônimos.”","Agente é o gênero; servidor é uma espécie."],
  ["“Quem trabalha sem remuneração não é agente público.”","É, se exerce função pública (ex.: mesário)."],
  ["“Empregado público ocupa cargo e é estatutário.”","Ocupa emprego e é regido pela CLT."],
  ["“Função de confiança pode ser ocupada por pessoa de fora.”","Só por servidor efetivo; quem é de fora pode ocupar cargo em comissão."],
  ["“O concurso vale 2 anos, prorrogáveis várias vezes.”","Prorrogável uma única vez, por igual período."],
  ["“Psicotécnico pode ser exigido só pelo edital.”","Só por lei (Súmula Vinculante 44)."],
  ["“Comissionado adquire estabilidade em 3 anos.”","Estabilidade é só para efetivos aprovados em concurso."]],
 [["“Estável só perde o cargo por sentença judicial.”","Também por processo administrativo e por avaliação periódica de desempenho."],
  ["“Absolvição penal sempre afasta a punição administrativa.”","Só se negar a existência do fato ou a autoria."],
  ["“A vítima pode processar diretamente o servidor.”","Pelo STF (Tema 940), a ação é contra o Estado, que depois cobra em regresso."],
  ["“Ainda existe improbidade culposa.”","Desde a Lei nº 14.230/2021, só dolosa."],
  ["“Sindicância pode aplicar suspensão de 60 dias.”","Até 30 dias; acima disso, exige PAD."],
  ["“Sem advogado, o PAD é nulo.”","Não, segundo a Súmula Vinculante 5."],
  ["“A advertência prescreve em 2 anos.”","Em 180 dias; a suspensão é que prescreve em 2 anos (Lei nº 8.112/1990)."]])

flashcards([("CONCEITO","Agente x servidor público?","Agente: gênero. Servidor: espécie."),
 ("CATEGORIAS","Quais são as três categorias de agentes?","Políticos, servidores públicos e particulares em colaboração."),
 ("CATEGORIAS","Exemplos de agentes políticos?","Presidente, governadores, prefeitos, parlamentares, ministros e secretários."),
 ("CATEGORIAS","Espécies de servidores públicos?","Estatutários, empregados públicos e temporários."),
 ("CATEGORIAS","Exemplos de particulares em colaboração?","Mesários, jurados, concessionários, notários e registradores."),
 ("CARGO","O que é cargo público (Lei 8.112)?","Conjunto de atribuições e responsabilidades da estrutura organizacional cometidas a um servidor; criado por lei."),
 ("CARGO","Função de confiança x cargo em comissão?","Função: só efetivos. Cargo em comissão: qualquer pessoa, com percentual para carreira."),
 ("CONCURSO","Validade do concurso?","Até 2 anos, prorrogável uma vez por igual período."),
 ("CONCURSO","Exame psicotécnico?","Só se previsto em lei (SV 44)."),
 ("PROVIMENTO","Única forma de provimento originário?","Nomeação."),
 ("PROVIMENTO","Reintegração x recondução?","Reintegração: demissão invalidada. Recondução: volta ao cargo anterior."),
 ("ESTABILIDADE","Requisitos da estabilidade?","3 anos de efetivo exercício, cargo efetivo por concurso e avaliação especial."),
 ("ESTABILIDADE","Hipóteses de perda do cargo pelo estável (art. 41)?","Sentença transitada em julgado, processo administrativo e avaliação periódica."),
 ("DIREITOS","Acumulação após a EC 138/2025?","Professor + professor; professor + qualquer outro; dois de saúde, com compatibilidade de horários."),
 ("DEVERES","Ordem manifestamente ilegal?","Não deve ser cumprida (art. 116, IV)."),
 ("RESPONSABILIDADE","As três esferas são dependentes?","Não. São independentes e cumuláveis (art. 125)."),
 ("RESPONSABILIDADE","Quando a absolvição penal afasta a administrativa?","Quando nega a existência do fato ou a autoria (art. 126)."),
 ("RESPONSABILIDADE","Responsabilidade do Estado por dano a terceiro?","Objetiva, com regresso contra o agente se houver dolo ou culpa."),
 ("IMPROBIDADE","Existe improbidade culposa?","Não, desde a Lei 14.230/2021."),
 ("DISCIPLINAR","Seis penalidades da Lei 8.112?","Advertência, suspensão, demissão, cassação, destituição de cargo em comissão e de função comissionada."),
 ("DISCIPLINAR","Suspensão máxima?","90 dias."),
 ("DISCIPLINAR","O que a sindicância pode resultar?","Arquivamento, advertência ou suspensão até 30 dias, ou instauração de PAD."),
 ("DISCIPLINAR","Prazos de prescrição (Lei 8.112)?","5 anos (demissão), 2 anos (suspensão), 180 dias (advertência)."),
 ("DISCIPLINAR","Advogado é obrigatório no PAD?","Não (Súmula Vinculante 5).")])

Q = [
 ("Conceito","Sobre o conceito de agente público, é correto afirmar:",
  ["abrange apenas os servidores concursados.","é expressão ampla, que inclui quem exerce função pública ainda que transitoriamente ou sem remuneração.","exclui os agentes políticos.","exclui os particulares em colaboração.","é sinônimo de empregado público."],"B",
  "Agente público é o gênero e alcança agentes políticos, servidores e particulares em colaboração, mesmo sem remuneração ou de forma transitória.","Agente = gênero amplo."),
 ("Categorias","Mesários convocados pela Justiça Eleitoral e jurados do Tribunal do Júri são classificados como:",
  ["agentes políticos.","empregados públicos.","particulares em colaboração (requisitados).","servidores estatutários.","temporários do art. 37, IX."],"C",
  "Prestam serviço público relevante por convocação, sem perder a condição de particulares.","Mesário e jurado = requisitados."),
 ("Agentes políticos","São exemplos de agentes políticos:",
  ["guarda municipal e técnico judiciário.","prefeito, vereador e secretário municipal.","mesário e jurado.","empregado da Caixa e dos Correios.","concessionário de transporte coletivo."],"B",
  "Agentes políticos ocupam a cúpula do Estado, por eleição ou nomeação política.","Cúpula = políticos."),
 ("Servidores","O empregado público:",
  ["ocupa cargo público e é regido pelo estatuto.","ocupa emprego público e é regido pela CLT, admitido por concurso.","é contratado sem concurso.","adquire a estabilidade do art. 41 da CF.","é agente político."],"B",
  "Empregados públicos ocupam emprego, sob a CLT, mas ingressam por concurso (CF, art. 37, II).","Emprego = CLT + concurso."),
 ("Temporários","A contratação por tempo determinado, prevista no art. 37, IX, da Constituição, destina-se a:",
  ["preencher cargos de direção, chefia e assessoramento.","atender a necessidade temporária de excepcional interesse público.","substituir o concurso público em qualquer caso.","admitir servidores com estabilidade.","nomear agentes políticos."],"B",
  "Texto do art. 37, IX.","Temporário = necessidade temporária excepcional."),
 ("Cargo","De acordo com a Lei nº 8.112/1990, cargo público é:",
  ["o vínculo contratual regido pela CLT.","o conjunto de atribuições e responsabilidades previstas na estrutura organizacional que devem ser cometidas a um servidor.","qualquer função exercida por particular.","a função exercida por agente político eleito.","o contrato temporário."],"B",
  "Art. 3º da Lei nº 8.112/1990; os cargos são criados por lei, com denominação própria e vencimento pago pelos cofres públicos.","Cargo = atribuições + responsabilidades, por lei."),
 ("Confiança","As funções de confiança, segundo a Constituição:",
  ["podem ser exercidas por qualquer pessoa.","são exercidas exclusivamente por servidores ocupantes de cargo efetivo.","dispensam vínculo com a Administração.","destinam-se a atividades operacionais.","exigem concurso específico."],"B",
  "CF, art. 37, V. Os cargos em comissão podem ser ocupados por pessoas de fora, respeitado o percentual mínimo de servidores de carreira.","Função de confiança = só efetivo."),
 ("Concurso","O prazo de validade do concurso público é de:",
  ["até 1 ano, improrrogável.","até 2 anos, prorrogável uma vez, por igual período.","até 2 anos, prorrogável indefinidamente.","até 4 anos, improrrogável.","até 5 anos."],"B",
  "CF, art. 37, III.","2 + 2 (uma vez)."),
 ("Concurso","Sobre o exame psicotécnico em concursos públicos, é correto afirmar:",
  ["pode ser exigido apenas com previsão no edital.","só pode ser exigido se previsto em lei.","é proibido em qualquer caso.","é obrigatório em todos os concursos.","pode ser sigiloso e sem critérios objetivos."],"B",
  "Súmula Vinculante 44: só por lei se pode sujeitar a exame psicotécnico a habilitação de candidato.","Psicotécnico = lei."),
 ("Provimento","É a única forma de provimento originário:",
  ["promoção.","readaptação.","nomeação.","reintegração.","recondução."],"C",
  "As demais formas são derivadas, pois pressupõem vínculo anterior.","Originário = nomeação."),
 ("Provimento","O retorno do servidor estável ao cargo, após a invalidação judicial de sua demissão, denomina-se:",
  ["reversão.","aproveitamento.","reintegração.","recondução.","readaptação."],"C",
  "Reintegração: retorno do estável cuja demissão foi invalidada (CF, art. 41, § 2º).","Demissão anulada = reintegração."),
 ("Estabilidade","São requisitos para a aquisição da estabilidade:",
  ["2 anos de exercício em cargo em comissão.","3 anos de efetivo exercício em cargo efetivo provido por concurso e avaliação especial de desempenho.","5 anos de serviço em qualquer cargo.","apenas a aprovação em concurso.","3 anos em emprego público."],"B",
  "CF, art. 41, caput e § 4º.","3 anos + efetivo + avaliação."),
 ("Estabilidade","O servidor estável pode perder o cargo, segundo o art. 41, § 1º, da CF:",
  ["apenas por sentença judicial transitada em julgado.","por sentença transitada em julgado, processo administrativo com ampla defesa e avaliação periódica de desempenho.","por simples decisão do chefe imediato.","apenas por processo administrativo.","em nenhuma hipótese."],"B",
  "As três hipóteses do art. 41, § 1º (além do excesso de despesa com pessoal, art. 169).","Três hipóteses de perda."),
 ("Direitos","Após a EC nº 138/2025, é permitida, havendo compatibilidade de horários e respeitado o teto, a acumulação de:",
  ["dois cargos administrativos de qualquer natureza.","um cargo de professor com outro de qualquer natureza.","três cargos de professor.","um cargo de juiz com outro de professor e outro de médico.","qualquer cargo com qualquer emprego."],"B",
  "CF, art. 37, XVI, b, com a redação da EC nº 138/2025.","Professor + qualquer outro."),
 ("Deveres","Diante de ordem superior manifestamente ilegal, o servidor regido pela Lei nº 8.112/1990 deve:",
  ["cumpri-la integralmente.","deixar de cumpri-la e representar contra a ilegalidade.","cumpri-la e só depois reclamar.","pedir exoneração.","consultar o sindicato antes de agir."],"B",
  "Art. 116, IV (cumprir ordens, exceto manifestamente ilegais) e XII (representar contra ilegalidade, omissão ou abuso de poder).","Manifestamente ilegal não se cumpre."),
 ("Responsabilidade","Sobre a responsabilidade do servidor, é correto afirmar:",
  ["a responsabilidade civil depende de condenação penal.","as sanções civis, penais e administrativas podem cumular-se e são independentes entre si.","a absolvição criminal por falta de provas afasta a punição administrativa.","o servidor só responde administrativamente.","as três esferas se excluem."],"B",
  "Lei nº 8.112/1990, art. 125; a absolvição só afasta a esfera administrativa se negar o fato ou a autoria (art. 126).","Independentes e cumuláveis."),
 ("Responsabilidade","A responsabilidade administrativa do servidor será afastada no caso de absolvição criminal que:",
  ["reconheça a falta de provas.","negue a existência do fato ou sua autoria.","reconheça a prescrição.","aplique o perdão judicial.","decorra de transação penal."],"B",
  "Art. 126 da Lei nº 8.112/1990.","Fato inexistente ou autoria negada."),
 ("Responsabilidade civil","Viatura da Guarda Municipal, dirigida por guarda em serviço, colide com o carro de um cidadão. Quanto à responsabilidade, é correto afirmar:",
  ["o cidadão deve provar a culpa do Município.","o Município responde objetivamente e pode cobrar do guarda, em regresso, se houver dolo ou culpa.","o guarda responde sozinho, sem participação do Município.","não há responsabilidade se o guarda estava em serviço.","o regresso independe de dolo ou culpa."],"B",
  "CF, art. 37, § 6º; pelo STF (Tema 940), a ação é proposta contra o ente público.","Estado objetivo; agente em regresso."),
 ("Improbidade","Após a Lei nº 14.230/2021, os atos de improbidade administrativa:",
  ["podem ser culposos ou dolosos.","exigem conduta dolosa, entendida como vontade livre e consciente de alcançar o resultado ilícito.","dispensam qualquer elemento subjetivo.","só podem ser praticados por agentes políticos.","são punidos apenas na esfera penal."],"B",
  "Art. 1º, §§ 1º e 2º, da Lei nº 8.429/1992.","Improbidade só dolosa."),
 ("Penalidades","NÃO é penalidade disciplinar prevista no art. 127 da Lei nº 8.112/1990:",
  ["advertência.","suspensão.","demissão.","multa penal.","destituição de cargo em comissão."],"D",
  "As seis penalidades são advertência, suspensão, demissão, cassação, destituição de cargo em comissão e destituição de função comissionada. Multa penal é sanção criminal.","Seis penalidades administrativas."),
 ("Suspensão","Na Lei nº 8.112/1990, a penalidade de suspensão não pode exceder:",
  ["30 dias.","60 dias.","90 dias.","120 dias.","180 dias."],"C",
  "Art. 130.","Suspensão: até 90 dias."),
 ("Sindicância","Da sindicância poderá resultar, segundo a Lei nº 8.112/1990:",
  ["demissão do servidor.","arquivamento, advertência ou suspensão de até 30 dias, ou instauração de processo disciplinar.","cassação de aposentadoria.","suspensão de até 90 dias.","prisão administrativa."],"B",
  "Art. 145. Penalidades mais graves exigem processo administrativo disciplinar.","Sindicância: até 30 dias de suspensão."),
 ("PAD","Segundo a Súmula Vinculante 5 do STF, a falta de defesa técnica por advogado no processo administrativo disciplinar:",
  ["torna o processo nulo.","não ofende a Constituição.","só é admitida para advertência.","depende de autorização judicial.","impede a aplicação de qualquer penalidade."],"B",
  "SV 5. Contraditório e ampla defesa continuam obrigatórios.","Sem advogado no PAD: válido."),
 ("Prescrição","Na Lei nº 8.112/1990, a ação disciplinar quanto às infrações puníveis com advertência prescreve em:",
  ["30 dias.","90 dias.","180 dias.","2 anos.","5 anos."],"C",
  "Art. 142, III; suspensão: 2 anos; demissão: 5 anos.","Advertência: 180 dias.")]
questoes(Q, "BCDBEABDCEBACDEBACBDCEAC")
respostas_treinos()

referencias('''<h3>Legislação consultada (portal do Planalto)</h3><ul>
<li>Constituição Federal: art. 37 (I a IX, XVI, XVII e § 6º), art. 38, art. 39, § 3º, art. 40, § 1º, art. 41 (com a EC nº 19/1998) e alteração da EC nº 138/2025 no art. 37, XVI (conferidos para o Caderno 03 e nesta edição).</li>
<li>Lei nº 8.112/1990: arts. 2º, 3º, 8º, 20, 116, 117, 121 a 128, 130, 132, 141 a 143, 145 e 152.</li>
<li>Lei nº 8.429/1992 (com a redação da Lei nº 14.230/2021): arts. 1º, 9º a 12.</li>
<li>Lei nº 13.869/2019: art. 2º, parágrafo único.</li>
<li>Citados sem conferência nesta edição: CF, arts. 42, 142, 169 e 236; Lei Complementar nº 152/2015; CP, arts. 92 e 327 (este conferido para o Caderno 07).</li></ul>
<h3>Jurisprudência citada (identificada em pesquisa)</h3><ul><li>STF: Súmulas Vinculantes 5, 43 e 44; Tema 940 (dupla garantia); ADI 2.135 (regime jurídico único, 2024); entendimento sobre nomeação dos aprovados dentro do número de vagas e sobre o direito de greve dos servidores.</li><li>STF e STJ: prazo do estágio probatório vinculado aos 3 anos da estabilidade.</li></ul>''',
 'A base legal foi conferida nos textos do portal do Planalto, que exibem a redação vigente com as notas de alteração. <strong>Limitações:</strong> os textos do Planalto não informam a data da última atualização e não substituem o Diário Oficial. A Lei nº 8.112/1990 rege os servidores <strong>federais</strong>: estatutos estaduais e municipais podem ter regras e prazos diferentes, e o edital do seu concurso indica qual cobrar. A classificação dos agentes públicos é <strong>doutrinária</strong>. As súmulas e decisões citadas foram identificadas em pesquisa e não foram reconferidas nos portais oficiais dos tribunais nesta edição.', DATA)
encerramento("12", "Direito Administrativo", 'Sugestão de continuação: <strong>Caderno 13 · Direito Processual Penal</strong>.')
gravar(HERE, "Mapa da Aprovação — Caderno 12 — Agentes Públicos", Q)
