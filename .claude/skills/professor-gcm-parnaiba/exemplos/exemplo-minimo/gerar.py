"""Exemplo mínimo de apostila com o kit da Skill professor-gcm-parnaiba. Uso: copie assets/kit/ para esta pasta e rode node build.js.
Conteúdo conferido no arquivo da Lei Municipal nº 1.989/2003 (GCM-PARNAIBA/fontes/legislacao-municipal/)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit
from kit import *

DATA = "28 de novembro de 2026"
kit.U = {1: ("UNIDADE 1", "A GCM de Parnaíba")}

add(f'''<div class="unit"><span class="u">ANTES DE COMEÇAR</span></div>
<h1 class="big">Como usar esta <span class="hl">apostila</span></h1>
<p class="lead">Exemplo curto que mostra todos os blocos que uma apostila completa deve ter.</p>
{ATENCAO(p("<strong>Edital ainda não confirmado.</strong> A distribuição de questões usada nas apostilas (Código Penal 15, Conhecimentos Profissionais 15, Português 10, Regionais 4, Informática 3, Raciocínio Lógico 3) é <strong>provisória</strong> e deve ser conferida no edital oficial."))}
{table(["Etapa","O que fazer"],[["1","Leia o tópico nos 7 passos"],["2","Resolva as questões sem consultar"],["3","Confira o gabarito comentado"],["4","Agende as revisões D+1, D+7 e D+30"]],["14%",None])}''', first=True)

toc_page([("u", "UNIDADE 1 · A GCM DE PARNAÍBA", "U1"), ("", "1. Competências da GCM (Lei nº 1.989/2003)", "A01"),
          ("u", "PRÁTICA E REVISÃO", "RV"), ("", "Questões autorais", "R3"), ("", "Gabarito comentado", "R4")])
opener("01", "UNIDADE 1", "A GCM de Parnaíba", ["Competências da GCM"], "U1")

add(topico('Competências da <span class="hl">GCM</span>', 'Art. 4º da Lei Municipal nº 1.989/2003.', "A01",
  p("É a lista do que a Guarda Civil Municipal de Parnaíba pode e deve fazer, segundo a lei municipal que a criou."),
  p("Pense na lei como a “descrição do cargo” da Guarda: ela diz em quais tarefas a corporação trabalha, como proteger o patrimônio, vigiar praças e auxiliar no trânsito."),
  ("Art. 4º (em síntese) · Lei nº 1.989/2003", "<p>Compete à GCM: I defender os bens públicos municipais; II executar vigilância nos logradouros públicos; III fiscalizar a ordenação de trânsito e tráfego urbano; IV manter a segurança pessoal do Prefeito; V auxiliar a defesa civil em calamidade ou emergência; VI desenvolver campanhas conjuntas com outros órgãos; VII auxiliar na educação, prevenção e defesa do meio ambiente.</p>"),
  p("Durante uma enchente em um bairro, a GCM apoia a Defesa Civil no isolamento de áreas de risco: é a competência do inciso V."),
  "a banca pode trocar uma competência municipal por uma atribuição de outro órgão, como investigar crimes, que é função da polícia civil.",
  "<ul><li><b>Errado:</b> “A GCM de Parnaíba tem competência para investigar crimes e instaurar inquérito.”</li><li><b>Certo:</b> a lei não prevê isso; investigar é função de polícia judiciária.</li></ul>",
  "Sete competências: <strong>bens públicos · logradouros · trânsito · segurança do Prefeito · defesa civil · campanhas · meio ambiente</strong>.", 1))
atencao(NAO_CONFUNDA("Lei federal 13.022/2014", "Lei municipal 1.989/2003", [("Alcance", "Normas gerais para todas as guardas do país", "Cria e organiza a GCM de Parnaíba"), ("Natureza", "Instituição de caráter civil", "Fala em postos, graduações e função auxiliar policial")]), t="Não confunda")

Q = [
 ("Competências", "Segundo o art. 4º da Lei Municipal nº 1.989/2003, compete à Guarda Civil Municipal de Parnaíba:",
  ["auxiliar os órgãos de defesa civil em estados de calamidade pública ou de emergência.", "instaurar inquérito policial.", "julgar infrações de trânsito em última instância.", "lavrar o auto de prisão em flagrante.", "fiscalizar rodovias federais."], "A",
  "Art. 4º, V. As demais são atribuições de outros órgãos (polícia judiciária, órgãos recursais de trânsito, PRF).", "Defesa civil = inciso V."),
 ("Hierarquia", "Pela Lei nº 1.989/2003, a Guarda Civil Municipal de Parnaíba é diretamente subordinada:",
  ["ao Secretário de Segurança do Estado.", "ao Chefe do Poder Executivo Municipal.", "à Câmara Municipal.", "ao Comandante da Polícia Militar.", "ao Juiz da Comarca."], "B",
  "Art. 2º: instituição permanente do Poder Executivo Municipal, diretamente subordinada ao Prefeito.", "GCM responde ao Prefeito."),
 ("Ingresso", "O ingresso no quadro efetivo da GCM de Parnaíba, segundo o art. 3º da Lei nº 1.989/2003, ocorre por:",
  ["indicação do Comandante.", "concurso público e posterior aprovação em curso de formação profissional.", "contratação temporária.", "eleição entre os guardas.", "transferência da Polícia Militar."], "B",
  "Art. 3º: concurso público e aprovação em curso de formação, desenvolvido pelo Comando ou por guarda de outro Município, mediante convênio.", "Concurso + curso de formação."),
]
questoes(Q)
add(pratica_title("Revisão") + MEMORIZE("A GCM de Parnaíba é subordinada ao <strong>Prefeito</strong>; ingresso por <strong>concurso + curso de formação</strong>.") +
    checklist(["Sei listar as 7 competências do art. 4º", "Sei a quem a GCM é subordinada", "Sei como se dá o ingresso"]) + revisoes_espacadas("Lei 1.989/2003"))
referencias("<h3>Fontes</h3><ul><li>Lei Municipal nº 1.989/2003 de Parnaíba (cópia de LeisMunicipais, em GCM-PARNAIBA/fontes/legislacao-municipal/).</li></ul>",
            "Exemplo de demonstração. O texto oficial é o publicado no Diário Oficial do Município; o edital ainda não foi confirmado.", DATA)
encerramento("00", "Exemplo mínimo", "Agora peça sua primeira apostila completa.", "novembro de 2026")
gravar(HERE, "Exemplo mínimo — GCM Parnaíba", Q)
