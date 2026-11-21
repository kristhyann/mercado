# -*- coding: utf-8 -*-
"""Apresentação e capítulos 1 a 8."""
from motor import *

L13022 = 'https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l13022.htm'
CF88 = 'https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm'


def ficha():
    s = []
    s.append(Spacer(1, 1.2 * cm))
    s.append(P('<font size="20" color="#0E2238"><b>Operação GCM PHB</b></font>', 'bodyL'))
    s.append(sp(6))
    s.append(P('O guia estratégico para começar sua preparação para a Guarda Civil Municipal de Parnaíba (PI) — Edição pré-edital 2027.', 'lead'))
    s.append(sp(10))
    s += table(None, [
        ['Natureza do material', 'Guia educacional independente de organização e métodos de estudo para concursos.'],
        ['Público', 'Pessoas que desejam se preparar para um futuro concurso da Guarda Civil Municipal de Parnaíba (PI), inclusive quem nunca estudou para concursos.'],
        ['Fase', 'Pré-edital: produzido antes da publicação de qualquer edital. Nenhuma informação sobre vagas, salário, disciplinas, banca ou etapas deve ser entendida como oficial.'],
        ['Data de referência', 'Novembro de 2026. Informações sobre leis e sites foram conferidas nessa data.'],
        ['Formato', 'A4, com sumário clicável, marcadores (bookmarks) e campos preenchíveis no planner, nos checklists e no caderno de erros.'],
    ], [4.2, 12.8], zebra=True, bold_first=True)
    s += box('atencao', [
        'Este material <b>não é oficial</b> e não tem vínculo com a Prefeitura Municipal de Parnaíba, com a Guarda Civil Municipal, com a Câmara Municipal ou com qualquer banca organizadora. Não usa brasões, logotipos ou marcas institucionais.',
        'Nenhum material, curso ou método garante aprovação. Resultado depende de estudo consistente, do conteúdo do edital e do desempenho de cada candidato.',
    ], 'AVISO IMPORTANTE')
    s += box('fato', [
        'Ao longo do guia, as caixas <b>FATO VERIFICÁVEL</b> trazem informações com fonte (leis, sites oficiais). As caixas <b>RECOMENDAÇÃO</b> e <b>DICA PRÁTICA</b> trazem orientação pedagógica — sugestões que você pode adaptar à sua realidade.',
    ], 'COMO DIFERENCIAR FATO DE RECOMENDAÇÃO')
    s.append(sp(6))
    s.append(P('<b>Como usar os campos preenchíveis:</b> abra o PDF em um leitor que aceite formulários (Adobe Acrobat Reader, Xodo, leitor do navegador Chrome/Edge ou o app “Arquivos” de muitos celulares). Toque no campo e digite. Lembre-se de <b>salvar uma cópia</b> do arquivo depois de preencher. Se preferir, imprima as páginas e preencha à mão.', 'body'))
    return s


def sumario():
    s = [PageBreak()]
    s.append(P('<font size="22" color="#0E2238"><b>Sumário</b></font>', 'bodyL'))
    s.append(sp(4))
    s.append(P('Toque em um capítulo para ir direto a ele.', 'small'))
    s.append(sp(8))
    s.append(make_toc())
    return s


def apresentacao():
    s = chapter('', 'Apresentação', 'Por que este guia existe e como tirar proveito dele')
    s.append(lead('Você decidiu se preparar para a Guarda Civil Municipal de Parnaíba. Talvez nunca tenha estudado para concurso, talvez trabalhe o dia inteiro, talvez tenha tentado começar antes e parado. Este guia foi feito exatamente para você.'))
    s.append(H2('O que é o projeto Operação GCM PHB'))
    s.append(P('A Operação GCM PHB é um guia de preparação <b>pré-edital</b>: ele ensina como estudar e se organizar <b>antes</b> de o edital ser publicado, para que você chegue a esse momento com base, rotina e método — e não começando do zero quando o prazo já estiver correndo.'))
    s.append(P('O foco não é “dar a matéria”, e sim ensinar o <b>como</b>: como funciona um concurso, como montar uma rotina possível, quais métodos de estudo realmente ajudam a lembrar o conteúdo, como revisar, como resolver questões e como manter a constância por meses.'))
    s.append(H2('Para quem foi criado'))
    s += bullets([
        'Quem <b>nunca estudou</b> para concurso e não sabe por onde começar.',
        'Quem <b>trabalha</b> ou tem pouco tempo e precisa de um plano realista.',
        'Quem já começou, mas sente que estuda <b>sem direção</b> e esquece rápido o que leu.',
        'Quem estuda <b>pelo celular</b> e quer organizar PDFs, anotações e questões.',
    ])
    s.append(H2('Como usar este PDF'))
    s += table(['Etapa', 'O que fazer', 'Capítulos'], [
        ['1. Entender', 'Leia com calma como funciona um concurso e o que é preparação pré-edital.', '1 e 2'],
        ['2. Montar a base', 'Organize materiais, caderno, arquivos e escolha seu modelo de horário.', '3 e 4'],
        ['3. Aprender o método', 'Estude os métodos e o ciclo de estudos. Volte a eles sempre que tiver dúvida.', '5 e 6'],
        ['4. Executar', 'Escolha um plano (30, 60 ou 90 dias) e siga-o usando o planner semanal.', '7, 8, 9 e 14'],
        ['5. Consolidar', 'Aplique revisões, questões e o caderno de erros.', '10, 11 e 12'],
        ['6. Manter', 'Use as estratégias de disciplina e os checklists. Acompanhe o edital.', '13, 15 e 16'],
    ], [3.3, 11.2, 2.5], bold_first=True)
    s += box('dica', 'Não tente ler tudo em um dia. Uma boa forma de começar: leia a Apresentação e os Capítulos 1 a 4 nos dois primeiros dias e já comece o Plano de 30 Dias no terceiro. O próprio plano indica quando voltar aos outros capítulos.')
    s.append(H2('Como usar os outros materiais do kit'))
    s.append(P('Este PDF é <b>autossuficiente</b>: ele contém, em suas páginas, o planner semanal, os checklists e o caderno de erros. Se você recebeu este guia como parte de um kit com outros materiais (por exemplo, planilhas, mapas mentais, flashcards ou listas de questões), use-os assim:'))
    s += table(['Se o kit tiver…', 'Use para…', 'Encaixe no guia'], [
        ['Planilha de controle', 'Registrar horas estudadas e percentual de acertos por disciplina.', 'Capítulo 2 (acompanhar progresso) e Capítulo 11 (análise de desempenho).'],
        ['Mapas mentais / resumos', 'Revisar rapidamente um assunto já estudado — nunca como único estudo.', 'Revisões de 7 e 30 dias (Capítulo 10).'],
        ['Flashcards prontos', 'Treinar recuperação ativa. Edite e crie os seus a partir dos erros.', 'Capítulo 5 (flashcards e revisão espaçada).'],
        ['Listas de questões', 'Praticar logo após a teoria e montar o caderno de erros.', 'Capítulos 11 e 12.'],
        ['Material de conteúdo (teoria)', 'Estudar os assuntos com leitura ativa.', 'Ciclo de estudos (Capítulo 6) e planos (7 a 9).'],
    ], [3.8, 7.0, 6.2], bold_first=True)
    s += box('atencao', '<b>O edital oficial será sempre a referência definitiva.</b> Quando ele for publicado, compare as disciplinas, o conteúdo programático, as etapas e os requisitos com o que você vem estudando, e ajuste seu ciclo. O Capítulo 16 explica como acompanhar a publicação com segurança.')
    return s


def cap1():
    s = chapter(1, 'Como funciona um concurso público', 'Do edital à nomeação, explicado desde o básico')
    s.append(lead('Antes de estudar qualquer matéria, entenda o “jogo”. Quem conhece as regras perde menos tempo, comete menos erros na inscrição e sabe exatamente o que precisa fazer.'))
    s.append(H2('O que é concurso público'))
    s.append(P('Concurso público é o processo de seleção que a administração pública (União, estados, municípios, autarquias etc.) usa para escolher, de forma impessoal, quem vai ocupar cargos efetivos. Todos concorrem sob as mesmas regras, e quem obtém melhor desempenho, dentro dos critérios do edital, tem prioridade na nomeação.'))
    s += box('fato', [
        'A Constituição Federal (art. 37, II) determina que a investidura em cargo ou emprego público depende de aprovação prévia em concurso público de provas ou de provas e títulos, ressalvadas as nomeações para cargo em comissão. O art. 37, III, estabelece que o prazo de validade do concurso é de <b>até dois anos, prorrogável uma vez por igual período</b>.',
        'Fonte: ' + link(CF88, 'Constituição Federal de 1988 — Planalto'),
    ])
    s.append(H2('Glossário essencial'))
    s += table(['Termo', 'O que significa', 'Por que importa para você'], [
        ['Edital', 'Documento oficial que traz todas as regras do concurso: cargos, vagas, requisitos, remuneração, conteúdo, etapas, datas, critérios de aprovação e de desempate.', 'É a “lei do concurso”. Tudo o que vale está nele e em suas retificações.'],
        ['Retificação', 'Publicação que corrige ou altera partes do edital.', 'Pode mudar datas, conteúdo ou regras. Acompanhe sempre.'],
        ['Banca examinadora (organizadora)', 'Instituição contratada para elaborar e aplicar as provas, receber inscrições, julgar recursos e divulgar resultados.', 'Cada banca tem um estilo de questões. Conhecê-lo ajuda a treinar.'],
        ['Inscrição', 'Ato pelo qual o candidato se registra no concurso, geralmente pelo site da banca, com pagamento de taxa (salvo isenção prevista no edital).', 'Só está inscrito quem conclui o cadastro e paga dentro do prazo.'],
        ['Isenção de taxa', 'Dispensa de pagamento para quem se enquadra nos critérios previstos no edital e na legislação aplicável.', 'Tem prazo próprio, normalmente no início das inscrições.'],
        ['Conteúdo programático', 'Lista dos assuntos de cada disciplina que podem ser cobrados.', 'Define exatamente o que estudar.'],
        ['Gabarito preliminar e definitivo', 'Respostas oficiais divulgadas após a prova; o definitivo sai depois dos recursos.', 'Permite conferir sua nota e recorrer.'],
        ['Recurso', 'Pedido formal para revisar questão, gabarito ou resultado, nos prazos do edital.', 'Pode anular ou alterar questões.'],
        ['Nota de corte', 'Pontuação mínima que separou os classificados dentro de um limite em uma etapa.', 'Não é fixa: depende do desempenho geral.'],
        ['Classificação', 'Ordem dos candidatos aprovados conforme a nota e os critérios de desempate.', 'Define a ordem de convocação.'],
        ['Cadastro de reserva', 'Aprovados além do número de vagas imediatas, que podem ser chamados durante a validade.', 'Pode gerar convocação futura.'],
        ['Homologação', 'Ato que confirma oficialmente o resultado final do concurso.', 'Marca o início da contagem da validade (conforme o edital).'],
        ['Convocação', 'Chamado oficial para uma etapa ou para apresentar documentos.', 'Perder o prazo pode eliminar o candidato.'],
        ['Nomeação', 'Ato oficial que designa o aprovado para o cargo, publicado em meio oficial.', 'É o passo que antecede a posse.'],
        ['Posse e exercício', 'Posse: aceitação formal do cargo. Exercício: início efetivo das atividades.', 'Têm prazos legais/editalícios.'],
    ], [3.1, 7.6, 6.3], bold_first=True)
    s.append(H2('Do edital à posse: o caminho típico'))
    s.append(P('A ordem e a existência de cada etapa variam de concurso para concurso. O fluxo abaixo mostra um caminho <b>comum</b>; o de Parnaíba será definido no edital.'))
    s.append(FlowSteps([('Autorização', 'lei / decisão do município'), ('Banca contratada', 'organizadora definida'),
                        ('Edital publicado', 'regras e datas'), ('Inscrições', 'cadastro e taxa'),
                        ('Prova objetiva', '1ª etapa usual'), ('Outras etapas', 'se previstas'),
                        ('Resultado final', 'classificação'), ('Homologação', 'confirmação oficial'),
                        ('Convocação', 'documentos / curso'), ('Nomeação e posse', 'publicação oficial')], per_row=5, box_h=1.5 * cm))
    s.append(sp(10))
    s.append(H2('Etapas que podem existir em concursos de Guardas Municipais'))
    s.append(P('Concursos de guardas municipais costumam ter mais de uma etapa, porque a função exige preparo físico, equilíbrio emocional e conduta compatível. <b>Não é possível afirmar quais etapas serão exigidas em Parnaíba antes do edital.</b> A tabela mostra etapas que <b>aparecem com frequência</b> em concursos de guardas pelo país:'))
    s += table(['Etapa', 'Como costuma funcionar', 'Caráter mais comum'], [
        ['Prova objetiva', 'Questões de múltipla escolha ou “certo/errado” sobre as disciplinas do edital.', 'Eliminatório e classificatório.'],
        ['Prova discursiva / redação', 'Texto sobre um tema proposto. Menos frequente para nível médio, mas possível.', 'Varia.'],
        ['Teste de aptidão física (TAF)', 'Provas como corrida, flexões, abdominais, barra, natação, com índices mínimos por sexo e idade.', 'Geralmente eliminatório.'],
        ['Avaliação psicológica', 'Testes e/ou entrevista para verificar características compatíveis com o cargo.', 'Eliminatório (apto/inapto).'],
        ['Exame médico / toxicológico', 'Avaliação de saúde, exames laboratoriais e, às vezes, toxicológico.', 'Eliminatório.'],
        ['Investigação social', 'Análise de antecedentes e conduta (certidões, declarações, referências).', 'Eliminatório.'],
        ['Curso de formação', 'Formação teórica e prática obrigatória para o exercício do cargo, com frequência e avaliações.', 'Eliminatório e, às vezes, classificatório.'],
    ], [4.0, 9.0, 4.0], bold_first=True)
    s += box('fato', [
        'A Lei nº 13.022/2014 (Estatuto Geral das Guardas Municipais) lista, no art. 10, requisitos básicos para a investidura no cargo de guarda municipal, entre eles: nacionalidade brasileira; gozo dos direitos políticos; quitação com as obrigações militares e eleitorais; <b>nível médio completo</b> de escolaridade; <b>idade mínima de 18 anos</b>; aptidão física, mental e psicológica; e idoneidade moral comprovada por investigação social e certidões. O art. 11 prevê capacitação específica para o exercício das atribuições.',
        'O município pode prever requisitos adicionais. Confirme todos no edital. Fonte: ' + link(L13022, 'Lei nº 13.022/2014 — Planalto'),
    ])
    s += box('dica', 'Mesmo antes do edital, comece a cuidar do condicionamento físico (com orientação profissional) e organize seus documentos pessoais. Se houver TAF e investigação social, você não terá de correr atrás disso em poucas semanas.')
    s.append(H2('A prova objetiva'))
    s.append(P('Na maioria dos concursos de nível médio, a prova objetiva é a etapa que mais elimina candidatos. Os formatos mais comuns são:'))
    s += table(['Formato', 'Como é', 'Cuidado principal'], [
        ['Múltipla escolha (A–D ou A–E)', 'Uma alternativa correta entre 4 ou 5.', 'Ler todas as alternativas antes de marcar; eliminar as absurdas.'],
        ['Certo ou Errado', 'Cada item é julgado. Em alguns editais, um item errado anula um certo.', 'Verificar se há penalidade; deixar em branco pode ser estratégico.'],
    ], [4.2, 6.4, 6.4], bold_first=True)
    s.append(P('O edital informa o número de questões por disciplina, o peso de cada uma, a nota mínima geral e, às vezes, a nota mínima por disciplina. Essas informações mudam completamente a estratégia — por isso o ciclo de estudos (Capítulo 6) deve ser reajustado quando o edital sair.'))
    s.append(H2('Como ler e interpretar um edital'))
    s.append(P('Edital assusta pelo tamanho, mas tem estrutura previsível. Leia em três passadas:'))
    s += table(['Passada', 'Objetivo', 'O que marcar'], [
        ['1ª — Visão geral (30 min)', 'Entender o concurso como um todo.', 'Cargo, vagas, remuneração, requisitos, banca, cronograma.'],
        ['2ª — Regras (1 h)', 'Entender como você será avaliado.', 'Etapas, caráter de cada uma, número de questões, pesos, notas mínimas, desempate, regras do TAF e dos exames.'],
        ['3ª — Conteúdo (1 h)', 'Transformar o conteúdo em plano.', 'Cada disciplina e cada assunto. Compare com o que você já estudou.'],
    ], [4.2, 5.0, 7.8], bold_first=True)
    s += box_bullets('recom', [
        'Salve o edital em PDF e anote a data de publicação. Guarde também cada retificação.',
        'Monte uma tabela com <b>todas as datas</b> (isenção, inscrição, pagamento, prova, recursos) e coloque lembretes no celular.',
        'Grife em cores diferentes: requisitos (vermelho), datas (amarelo), conteúdo (verde).',
        'Procure palavras como “eliminatório”, “classificatório”, “mínimo”, “vedado”, “sob pena de”.',
        'Releia o edital inteiro antes de cada etapa. Detalhes mudam com retificações.',
    ], 'CHECK RÁPIDO DE LEITURA DE EDITAL')
    s += box('exerc', [
        'Pegue qualquer edital recente de guarda municipal (de outra cidade), publicado no site de uma banca. Em 40 minutos, encontre: (1) requisitos do cargo; (2) número de questões por disciplina; (3) nota mínima; (4) etapas eliminatórias; (5) critérios de desempate. Esse treino deixa você pronto para ler o edital de Parnaíba com rapidez quando ele sair.',
    ])
    return s


def cap2():
    s = chapter(2, 'Conhecendo a preparação para GCM', 'Preparação pré-edital: começar antes, com direção')
    s.append(H2('O que significa preparação pré-edital'))
    s.append(P('É o estudo feito <b>antes</b> da publicação do edital, com base nas disciplinas que costumam aparecer em concursos do mesmo tipo de cargo e no conhecimento básico que qualquer prova de nível médio exige (português, matemática, informática, legislação). Quando o edital sair, você não começa: você <b>ajusta</b>.'))
    s.append(H2('Por que começar antes'))
    s += table(['Quem começa antes do edital', 'Quem começa só depois do edital'], [
        ['Tem meses para aprender a base com calma.', 'Tem poucas semanas (às vezes 45–90 dias) até a prova.'],
        ['Já tem rotina, método e revisões funcionando.', 'Precisa criar hábito e estudar conteúdo ao mesmo tempo.'],
        ['Usa o período pós-edital para revisar e fazer questões.', 'Usa o período pós-edital para ver a teoria pela primeira vez.'],
        ['Pode cuidar do condicionamento físico e dos documentos com antecedência.', 'Corre para fazer tudo junto.'],
    ], [8.5, 8.5], zebra=True)
    s += box('atencao', 'Pré-edital não é adivinhar. Estude o que é <b>provável e útil</b> (base comum), sem se apegar a boatos sobre data, vagas ou conteúdo. O risco do pré-edital é estudar algo que não cairá — por isso priorize as matérias que aparecem em praticamente todos os concursos de nível médio.')
    s.append(H2('Disciplinas que costumam aparecer em concursos de guarda municipal'))
    s.append(P('A lista abaixo é um <b>exemplo baseado no padrão de concursos de guardas municipais em geral</b>. <b>Não é a lista oficial de Parnaíba</b>, que só será conhecida no edital. Use-a para montar sua base.'))
    s += table(['Grupo', 'Exemplos de disciplinas', 'Prioridade pré-edital sugerida'], [
        ['Base comum', 'Língua Portuguesa (interpretação, gramática); Matemática e/ou Raciocínio Lógico; Noções de Informática.', '<b>Alta</b> — aparecem em quase todo concurso de nível médio.'],
        ['Legislação da área', 'Lei nº 13.022/2014 (Estatuto Geral das Guardas Municipais); noções de Direito Constitucional (direitos e garantias fundamentais, art. 144 — segurança pública); Direitos Humanos.', '<b>Alta</b> — ligadas diretamente ao cargo.'],
        ['Legislação local', 'Lei Orgânica do Município; Estatuto dos Servidores Municipais; lei de criação/organização da guarda local.', '<b>Média</b> — confirme se e quais leis existem e estão vigentes.'],
        ['Complementares', 'Noções de Direito Administrativo e Penal; legislação de trânsito; Estatuto da Criança e do Adolescente; Estatuto do Desarmamento.', '<b>Média/baixa</b> — dependem muito do edital.'],
        ['Conhecimentos gerais', 'Atualidades; história e geografia do Piauí e de Parnaíba.', '<b>Baixa a média</b> — estude aos poucos.'],
    ], [3.2, 8.8, 5.0], bold_first=True)
    s.append(H2('Como se organizar e evitar estudar sem direção'))
    s.append(P('Estudar sem direção é abrir o material “no que der vontade”, trocar de assunto toda hora e não saber o que já foi visto. Os sintomas são claros: sensação de que estuda muito e não sai do lugar, esquecimento rápido, ansiedade. O remédio tem três partes:'))
    s += numbered([
        '<b>Um mapa:</b> a lista de disciplinas e assuntos (a tabela acima, depois o edital).',
        '<b>Uma rota:</b> um ciclo de estudos e um plano (Capítulos 6 a 9) que dizem o que estudar em cada sessão.',
        '<b>Um painel:</b> registro de horas, assuntos concluídos, revisões e acertos (planner e caderno de erros).',
    ])
    s.append(H2('Como definir metas'))
    s.append(P('Metas boas são <b>específicas, mensuráveis e possíveis</b>. Separe três níveis:'))
    s += table(['Nível', 'Exemplo ruim', 'Exemplo bom'], [
        ['Meta de processo (diária)', '“Estudar bastante hoje.”', '“Estudar 50 min de Português (crase) + 15 questões + revisar o assunto de ontem.”'],
        ['Meta semanal', '“Avançar em Matemática.”', '“Concluir porcentagem e regra de três; 60 questões; 1 revisão de 7 dias.”'],
        ['Meta de resultado (mensal)', '“Ficar bom em tudo.”', '“Chegar a 70% de acertos em Português nas questões do mês.”'],
    ], [4.0, 4.6, 8.4], bold_first=True)
    s += box('recom', 'Foque nas metas de <b>processo</b>. Você controla se estudou 1 hora; não controla totalmente se acertou 80%. Quando o processo é cumprido com constância, o resultado tende a melhorar.')
    s.append(H2('Como acompanhar o progresso'))
    s.append(P('O que não é medido vira impressão. Acompanhe semanalmente quatro indicadores simples:'))
    s += table(['Indicador', 'Como medir', 'Sinal de alerta'], [
        ['Horas líquidas', 'Some só o tempo realmente estudando (sem celular, sem pausas).', 'Queda por 2 semanas seguidas.'],
        ['Assuntos concluídos', 'Marque no mapa de disciplinas cada assunto visto + com questões.', 'Muitos assuntos “começados” e poucos concluídos.'],
        ['Revisões feitas', 'Quantas revisões programadas foram cumpridas.', 'Menos de 70% das revisões cumpridas.'],
        ['% de acertos', 'Acertos ÷ questões feitas × 100, por disciplina.', 'Disciplina abaixo de 60% por várias semanas.'],
    ], [3.4, 8.4, 5.2], bold_first=True)
    s.append(P('O planner semanal (Capítulo 14) já traz espaço para registrar esses números.'))
    return s


def cap3():
    s = chapter(3, 'Como começar do zero', 'Materiais, ferramentas e rotina para quem nunca estudou para concursos')
    s.append(H2('Como iniciar sem experiência'))
    s.append(P('Começar do zero é normal. A maior parte dos candidatos inicia sem saber estudar de forma eficiente. O segredo é <b>começar pequeno e constante</b>, em vez de grande e irregular.'))
    s += numbered([
        '<b>Semana 1 — Adaptação:</b> 30 a 60 minutos por dia. O objetivo é criar o hábito, não esgotar a matéria.',
        '<b>Comece pela base:</b> Português e Matemática/Raciocínio Lógico sustentam todas as outras disciplinas e quase sempre têm peso alto.',
        '<b>Estude e pratique no mesmo dia:</b> depois de cada assunto, faça algumas questões, mesmo que erre muitas.',
        '<b>Registre:</b> anote o que estudou e quanto tempo. Isso cria senso de avanço.',
        '<b>Aumente aos poucos:</b> depois de 2 a 3 semanas estáveis, acrescente 15 a 30 minutos.',
    ])
    s.append(H2('Como escolher materiais'))
    s.append(P('Material demais atrapalha tanto quanto material de menos. Para cada disciplina, tenha <b>uma fonte principal de teoria</b> e <b>uma fonte de questões</b>.'))
    s += table(['Tipo', 'Bom sinal', 'Mau sinal'], [
        ['Teoria (PDF/livro)', 'Linguagem clara, exemplos, exercícios comentados, atualizado com a legislação vigente.', 'Texto copiado, sem data, cheio de erros, desatualizado.'],
        ['Legislação', 'Texto da lei no site oficial (Planalto, Câmara, site do município).', 'Lei “resumida” sem indicar alterações.'],
        ['Questões', 'Questões reais de concursos, com gabarito e, se possível, comentários.', 'Questões sem fonte ou inventadas.'],
        ['Vídeos', 'Complemento pontual de assuntos difíceis.', 'Usar vídeo como única fonte e assistir em velocidade sem praticar.'],
    ], [3.5, 7.0, 6.5], bold_first=True)
    s += box('dica', '<b>Lei se estuda na fonte.</b> O texto de leis federais é gratuito e oficial no site do Planalto (planalto.gov.br). Leis municipais costumam estar no site da prefeitura, da câmara municipal ou no diário oficial. Use resumos só como apoio.')
    s.append(H2('Como estudar no celular'))
    s.append(P('O celular pode ser seu melhor aliado ou seu maior inimigo. Use-o com regras:'))
    s += table(['Faça', 'Evite'], [
        ['Ative o modo “Não perturbe” ou “Foco” durante o estudo.', 'Estudar com notificações de redes sociais ligadas.'],
        ['Use leitor de PDF com marcação (grifar, comentar).', 'Ler PDFs passivamente rolando a tela.'],
        ['Resolva questões em sites/apps nos intervalos (ônibus, fila, almoço).', 'Deixar “estudo no celular” como o único estudo do dia.'],
        ['Use aplicativo de flashcards (ex.: Anki, gratuito na versão Android e web) para revisar.', 'Criar flashcards em excesso, que você não consegue revisar.'],
        ['Use cronômetro ou técnica de blocos (ex.: 25 a 50 minutos de foco).', 'Estudar “até cansar”, sem controle de tempo.'],
        ['Deixe a tela com tamanho de fonte confortável e, à noite, modo escuro.', 'Ler por horas com brilho alto, forçando a vista.'],
    ], [8.5, 8.5])
    s.append(H2('Como estudar usando PDFs'))
    s += numbered([
        '<b>Antes de ler:</b> veja o sumário do capítulo e os títulos. Pergunte-se “o que vou aprender aqui?”.',
        '<b>Durante:</b> grife pouco (no máximo uma frase por parágrafo) e escreva comentários com suas palavras.',
        '<b>Depois:</b> feche o PDF e tente explicar o conteúdo em voz alta ou por escrito (recuperação ativa).',
        '<b>Por fim:</b> faça questões e registre os erros.',
    ])
    s += box('dica', 'Crie um padrão de cores e use sempre o mesmo: <b>amarelo</b> = conceito; <b>verde</b> = exemplo; <b>vermelho</b> = exceção/pegadinha; <b>azul</b> = prazos e números. Isso acelera muito as revisões.')
    s.append(H2('Como organizar o caderno'))
    s.append(P('Você pode usar caderno físico, digital ou os dois. O importante é ter uma estrutura fixa:'))
    s += table(['Parte do caderno', 'Conteúdo'], [
        ['Capa interna', 'Seu objetivo, data de início e sua meta semanal de horas.'],
        ['Mapa de disciplinas', 'Lista de assuntos por disciplina com caixas para marcar: estudado, questões, revisão 24 h, 7 d, 30 d.'],
        ['Seções por disciplina', 'Anotações curtas por assunto, com título, data e página de origem.'],
        ['Caderno de erros', 'Pode ser uma seção separada ou um caderno à parte (modelo no Capítulo 12).'],
        ['Registro semanal', 'Horas, questões, acertos e reflexão (modelo no Capítulo 14).'],
    ], [4.5, 12.5], bold_first=True)
    s.append(H2('Como organizar arquivos'))
    s.append(P('Uma estrutura de pastas simples evita perder tempo procurando materiais. Sugestão (no celular, no computador ou na nuvem):'))
    tree = ('<font name="Sym" size="9.5">'
            'GCM_PHB_2027/<br/>'
            '&nbsp;&nbsp;├── 00_Edital_e_Noticias_Oficiais/<br/>'
            '&nbsp;&nbsp;├── 01_Portugues/ &nbsp;&nbsp;(teoria, questoes, resumos)<br/>'
            '&nbsp;&nbsp;├── 02_Matematica_RLM/<br/>'
            '&nbsp;&nbsp;├── 03_Informatica/<br/>'
            '&nbsp;&nbsp;├── 04_Legislacao/ &nbsp;&nbsp;(Lei_13022, Constituicao, Leis_Municipais)<br/>'
            '&nbsp;&nbsp;├── 05_Conhecimentos_Gerais/<br/>'
            '&nbsp;&nbsp;├── 06_Simulados/<br/>'
            '&nbsp;&nbsp;└── 07_Controle/ &nbsp;&nbsp;(planner, caderno de erros, planilhas)'
            '</font>')
    s += box('exemplo', [tree], 'EXEMPLO DE ESTRUTURA DE PASTAS')
    s += box('recom', 'Nomeie arquivos com <b>data no início</b> (ex.: 2027-01-15_Portugues_Crase.pdf). Faça backup na nuvem (Google Drive, OneDrive ou similar) uma vez por semana.')
    s.append(H2('Como manter uma rotina'))
    s += bullets([
        '<b>Horário fixo:</b> estude, sempre que possível, no mesmo horário. O cérebro se acostuma.',
        '<b>Local fixo:</b> um canto da casa, uma mesa da biblioteca, mesmo que seja simples.',
        '<b>Ritual de início:</b> água, celular no silencioso, material aberto, cronômetro ligado. Em 2 minutos você está estudando.',
        '<b>Plano do dia definido na véspera:</b> você senta e já sabe o que fazer.',
        '<b>Dia de folga planejado:</b> descanso também faz parte da rotina.',
    ])
    s.append(H2('Como estudar trabalhando'))
    s.append(P('A maioria dos candidatos de guarda municipal trabalha. Isso não impede a preparação, mas exige estratégia:'))
    s += table(['Momento', 'Ideia de uso'], [
        ['Antes do trabalho (30–60 min)', 'Teoria nova, quando a mente está descansada.'],
        ['Deslocamento', 'Flashcards, leitura de lei, questões rápidas no celular, áudio de revisão.'],
        ['Intervalo de almoço (15–30 min)', 'Bloco de questões ou revisão de 24 horas.'],
        ['Noite (45–90 min)', 'Questões, caderno de erros, leitura ativa de assunto mais leve.'],
        ['Fim de semana', 'Blocos maiores: teoria de assuntos difíceis, simulado, revisão semanal.'],
    ], [5.0, 12.0], bold_first=True)
    s.append(H2('Como estudar tendo pouco tempo'))
    s += bullets([
        '<b>30 minutos por dia, todos os dias, vencem 4 horas só no sábado.</b> A repetição distribuída fixa melhor o conteúdo.',
        'Use a regra <b>“estudo mínimo”</b>: em dias ruins, faça pelo menos 15 minutos (uma revisão ou 10 questões). Isso preserva o hábito.',
        'Priorize disciplinas de base e de maior peso provável.',
        'Troque teoria longa por <b>questões comentadas</b>: você aprende o conteúdo e o estilo da prova ao mesmo tempo.',
        'Corte desperdícios: veja quanto tempo passa em redes sociais (o próprio celular mostra) e “compre” parte desse tempo para estudo.',
    ])
    return s


def cap4():
    s = chapter(4, 'Organização do tempo', 'Modelos de 1, 2 e 3 horas por dia')
    s.append(lead('O melhor horário é o que você consegue cumprir. Escolha o modelo mais próximo da sua realidade e ajuste. Em todos eles, o tempo é dividido em quatro partes: estudo de teoria, questões, revisão e pausas.'))
    s.append(H2('Os quatro componentes de uma sessão'))
    s += table(['Componente', 'Função', 'Proporção sugerida'], [
        ['Estudo (teoria)', 'Aprender conteúdo novo com leitura ativa e anotações.', '40% a 50%'],
        ['Questões', 'Aplicar o conteúdo, conhecer o estilo da banca, encontrar falhas.', '25% a 35%'],
        ['Revisão', 'Recuperar o que foi estudado antes (24 h, 7 d, 30 d) e o caderno de erros.', '15% a 25%'],
        ['Pausas', 'Descansar a atenção. Levante, beba água, alongue, longe de telas.', '5 a 10 min por hora'],
    ], [3.5, 9.5, 4.0], bold_first=True)
    s.append(sp(4))
    s.append(StackBar('1 h/dia', [('Revisão', 10, TEAL), ('Teoria', 25, NAVY2), ('Pausa', 5, GREY), ('Questões', 20, GOLD)]))
    s.append(StackBar('2 h/dia', [('Revisão', 15, TEAL), ('Teoria', 45, NAVY2), ('Pausa', 10, GREY), ('Questões', 35, GOLD), ('Erros', 15, RED)]))
    s.append(StackBar('3 h/dia', [('Revisão', 20, TEAL), ('Teoria', 50, NAVY2), ('Pausa', 10, GREY), ('Questões', 40, GOLD), ('Pausa', 10, GREY), ('Teoria 2', 30, NAVY), ('Erros', 20, RED)]))
    s.append(P('Distribuição sugerida em minutos (as barras são proporcionais).', 'small'))
    s.append(H2('Modelo 1 — 1 hora por dia'))
    s.append(P('Ideal para quem trabalha em tempo integral ou tem filhos pequenos. Estude <b>uma disciplina por dia</b>, seguindo o ciclo.'))
    s += table(['Bloco', 'Tempo', 'O que fazer'], [
        ['Revisão de 24 h', '10 min', 'Recupere de memória o assunto de ontem; depois confira as anotações.'],
        ['Teoria', '25 min', 'Leitura ativa de um tópico pequeno, com anotações curtas.'],
        ['Pausa', '5 min', 'Levante, beba água.'],
        ['Questões', '20 min', '10 a 15 questões do tópico de hoje. Registre erros importantes.'],
    ], [4.0, 2.2, 10.8], bold_first=True)
    s += box('dica', 'No modelo de 1 hora, guarde 1 dia da semana (ex.: sábado) para revisão de 7 dias e caderno de erros, em vez de teoria nova.')
    s.append(H2('Modelo 2 — 2 horas por dia'))
    s.append(P('Permite estudar <b>duas disciplinas por dia</b> ou uma disciplina com mais profundidade.'))
    s += table(['Bloco', 'Tempo', 'O que fazer'], [
        ['Revisão', '15 min', 'Revisão de 24 h + flashcards do dia.'],
        ['Teoria — disciplina A', '45 min', 'Novo tópico com leitura ativa e anotações.'],
        ['Pausa', '10 min', 'Pausa longe de telas.'],
        ['Questões — disciplina A ou B', '35 min', '20 a 30 questões. Se for disciplina B, escolha um assunto já estudado.'],
        ['Caderno de erros', '15 min', 'Registre e corrija erros do dia; agende próxima revisão.'],
    ], [4.6, 2.2, 10.2], bold_first=True)
    s.append(H2('Modelo 3 — 3 horas por dia'))
    s.append(P('Para quem tem mais disponibilidade (meio período livre, desempregado, estudante). Atenção para não trocar quantidade por qualidade.'))
    s += table(['Bloco', 'Tempo', 'O que fazer'], [
        ['Revisão', '20 min', 'Revisão de 24 h e de 7 dias (conforme agenda) + flashcards.'],
        ['Teoria — disciplina A', '50 min', 'Assunto novo, de preferência uma disciplina difícil.'],
        ['Pausa', '10 min', 'Pausa ativa.'],
        ['Questões — disciplina A', '40 min', '25 a 35 questões do assunto estudado.'],
        ['Pausa', '10 min', 'Pausa.'],
        ['Teoria — disciplina B', '30 min', 'Disciplina mais leve ou leitura de lei.'],
        ['Caderno de erros e planejamento', '20 min', 'Registrar erros e definir o plano de amanhã.'],
    ], [4.6, 2.2, 10.2], bold_first=True)
    s.append(H2('Sugestão de semana-tipo'))
    s += table(['Dia', 'Foco principal', 'Observação'], [
        ['Segunda a sexta', 'Seguir o ciclo de estudos (teoria + questões + revisão).', 'Uma ou duas disciplinas por dia.'],
        ['Sábado', 'Revisão de 7 dias, caderno de erros, bloco grande de questões ou simulado.', 'Ótimo dia para medir progresso.'],
        ['Domingo', 'Descanso total ou leve (até 1 h de flashcards) + planejar a semana.', 'Descanso evita esgotamento.'],
    ], [3.5, 9.0, 4.5], bold_first=True)
    s += box('atencao', 'Dormir mal reduz a memória e a atenção. Cortar sono para estudar mais costuma sair caro. Preserve, sempre que possível, um período regular de sono.')
    s += box('exerc', [
        'Desenhe sua semana real: marque em uma folha os horários de trabalho, deslocamento, refeições e compromissos fixos. Os espaços que sobrarem são seus candidatos a horário de estudo. Escolha o modelo (1, 2 ou 3 h) que caiba neles <b>com folga</b>.',
    ])
    return s


def metodo(nome, oque, como, exemplo, aplicar, erros):
    s = [H2(nome)]
    s += table(None, [
        ['O que é', oque],
        ['Como funciona', como],
    ], [3.2, 13.8], zebra=False, bold_first=True)
    s += box('exemplo', exemplo)
    s.append(H3('Como aplicar'))
    s += numbered(aplicar)
    s += box_bullets('erro', erros)
    return s


def cap5():
    s = chapter(5, 'Métodos de estudo', 'O que é, como funciona, exemplo, como aplicar e erros comuns')
    s.append(lead('Ler e reler é a forma de estudo mais comum — e uma das menos eficientes. Pesquisas em psicologia cognitiva mostram que técnicas que fazem você <b>recuperar</b> a informação da memória e <b>espaçar</b> o estudo no tempo tendem a gerar retenção mais duradoura.'))
    s += box('fato', 'Revisões da literatura científica sobre técnicas de estudo (por exemplo, Dunlosky e colaboradores, 2013, na revista <i>Psychological Science in the Public Interest</i>) classificam a <b>prática de testes</b> (recuperação ativa) e a <b>prática distribuída</b> (revisão espaçada) entre as técnicas de maior utilidade, enquanto grifar e reler aparecem com utilidade baixa quando usados isoladamente.')
    s += metodo('1. Leitura ativa',
        'Ler com um objetivo, fazendo perguntas ao texto e processando o conteúdo, em vez de apenas passar os olhos.',
        'Antes de ler, você prevê o que vai aprender; durante, identifica ideias principais e relaciona com o que já sabe; depois, testa se entendeu.',
        'Assunto: <b>crase</b>. Antes de ler, você anota: “Quando usar crase? Quando é proibida?”. Ao ler, responde às perguntas na margem. Ao final, sem olhar, escreve 3 casos obrigatórios e 3 proibidos.',
        ['Leia títulos e subtítulos do tópico (1 min).', 'Transforme cada título em pergunta.', 'Leia um bloco (1 ou 2 páginas) e pare.', 'Responda às perguntas com suas palavras.', 'Marque o que não entendeu para revisar.'],
        ['Ler longos trechos sem parar para pensar.', 'Grifar quase tudo — o grifo perde a função.', 'Ler cansado, com o celular ao lado.'])
    s += metodo('2. Anotações',
        'Registro curto, com suas próprias palavras, das ideias essenciais do que foi estudado.',
        'Escrever obriga o cérebro a selecionar e reorganizar a informação. Anotações boas são curtas, organizadas e fáceis de revisar.',
        'Método de duas colunas: à esquerda, perguntas-chave (“Quem pode ser guarda municipal?”); à direita, as respostas resumidas (“Lei 13.022, art. 10: brasileiro, 18 anos, nível médio…”). Na revisão, cubra a coluna da direita e responda.',
        ['Divida a página: coluna estreita (perguntas) e coluna larga (respostas).', 'Anote só depois de ler um bloco — não durante cada frase.', 'Use abreviações e símbolos padronizados.', 'Ao final, escreva um resumo de 2 ou 3 linhas no rodapé.'],
        ['Copiar o material inteiro.', 'Anotar sem nunca revisar.', 'Gastar mais tempo enfeitando do que entendendo.'])
    s += metodo('3. Resumos',
        'Síntese do assunto, mais completa que a anotação, organizada para revisão futura.',
        'O resumo condensa um tópico em uma página ou menos: conceitos, regras, exceções e exemplos. Pode ser em texto, tópicos, tabela ou mapa mental.',
        'Resumo de <b>porcentagem</b>: fórmula (x% de N = x/100 × N), aumento (× 1,xx), desconto (× 0,yy), aumentos sucessivos (multiplicar fatores) e 2 exemplos resolvidos.',
        ['Faça o resumo <b>depois</b> de estudar e fazer questões, não antes.', 'Inclua o que você errou nas questões.', 'Limite: no máximo 1 página por tópico.', 'Use o resumo nas revisões de 7 e 30 dias.'],
        ['Fazer resumo de tudo, inclusive do que já sabe.', 'Resumos longos que viram um segundo livro.', 'Usar resumo pronto de terceiros como única fonte.'])
    s += metodo('4. Flashcards',
        'Cartões com uma pergunta na frente e a resposta no verso, para treinar memória de forma ativa.',
        'Ao ver a pergunta, você tenta lembrar a resposta antes de virar o cartão. Isso é recuperação ativa. Combinados com revisão espaçada, os cartões que você erra aparecem mais vezes.',
        'Frente: “Qual o prazo de validade de um concurso público segundo a CF?”. Verso: “Até 2 anos, prorrogável uma vez por igual período (art. 37, III)”.',
        ['Crie cartões a partir de erros e de pontos que você costuma esquecer.', 'Uma ideia por cartão; perguntas objetivas.', 'Revise diariamente (5 a 15 min).', 'Use papel (caixas por nível) ou aplicativo de repetição espaçada (ex.: Anki).'],
        ['Copiar parágrafos inteiros no verso.', 'Criar centenas de cartões e abandonar a revisão.', 'Ler a resposta sem tentar lembrar antes.'])
    s += metodo('5. Revisão espaçada',
        'Revisar o mesmo conteúdo em intervalos crescentes (por exemplo, 1, 7 e 30 dias).',
        'A cada revisão, o esforço para lembrar fortalece a memória e o esquecimento fica mais lento. Os intervalos aumentam à medida que você domina o conteúdo.',
        'Estudou <b>Lei 13.022 (arts. 1º a 5º)</b> na segunda. Revisa na terça (24 h), na segunda seguinte (7 dias) e cerca de um mês depois (30 dias).',
        ['Registre a data de cada assunto estudado.', 'Agende as revisões no planner (Capítulo 14).', 'Em cada revisão, comece tentando lembrar sem olhar.', 'Se esqueceu muito, encurte o próximo intervalo.'],
        ['Revisar só quando “sobra tempo”.', 'Reler tudo em vez de testar a memória.', 'Acumular revisões atrasadas sem replanejar.'])
    s += metodo('6. Recuperação ativa',
        'Puxar a informação da memória sem olhar o material: responder perguntas, explicar em voz alta, escrever o que lembra.',
        'O ato de lembrar é, em si, um treino de memória. Errar e depois conferir também ajuda a aprender.',
        'Depois de estudar <b>sujeito e predicado</b>, feche o material e escreva em 5 minutos tudo o que lembra. Em seguida, confira e complete com outra cor o que faltou.',
        ['Ao terminar um tópico, feche o material.', 'Escreva ou fale tudo o que lembra (técnica da “folha em branco”).', 'Compare com o material e marque lacunas.', 'Estude de novo só as lacunas.'],
        ['Achar que reconhecer o texto é o mesmo que saber.', 'Desistir porque “não lembra nada” — o esforço é o treino.', 'Fazer apenas no dia da prova.'])
    s += metodo('7. Resolução de questões',
        'Praticar com questões de provas anteriores e de bancas que aplicam concursos semelhantes.',
        'As questões mostram como o conteúdo é cobrado, revelam lacunas e treinam atenção e tempo. Elas são, ao mesmo tempo, estudo e diagnóstico.',
        'Após estudar <b>regra de três</b>, faça 20 questões. Acertou 12. Os 8 erros mostram que você confunde grandezas inversamente proporcionais — esse é seu próximo ponto de estudo.',
        ['Faça questões logo após a teoria (mesmo dia).', 'Comece por questões fáceis e aumente a dificuldade.', 'Leia o comentário/gabarito de todas, inclusive das que acertou.', 'Registre erros relevantes no caderno de erros.'],
        ['Fazer milhares de questões sem analisar os erros.', 'Pular a teoria e “chutar” até acertar.', 'Olhar a resposta antes de tentar resolver.'])
    s += metodo('8. Simulados',
        'Prova completa ou parcial feita em condições parecidas com as reais: tempo limitado, sem consulta, de uma vez.',
        'Treina resistência, administração do tempo, ordem de resolução e controle emocional. Gera dados para ajustar o plano.',
        'Sábado, 8h: 60 questões de várias disciplinas em 3 horas, com gabarito preenchido em folha de respostas. Depois, análise: acertos por disciplina e tipos de erro.',
        ['Comece com simulados curtos (20–30 questões) e aumente.', 'Simule horário, tempo e ausência de consulta.', 'Corrija e analise no mesmo dia ou no seguinte.', 'Registre o resultado no planner e ajuste o ciclo.'],
        ['Fazer simulado e não analisar.', 'Fazer simulados cedo demais, sem base, e se desmotivar.', 'Comparar-se com notas de desconhecidos na internet.'])
    s += metodo('9. Caderno de erros',
        'Registro organizado dos erros cometidos em questões, com a causa e a correção.',
        'Seus erros mostram exatamente o que você precisa estudar. Revisar os próprios erros é uma das revisões mais eficientes, porque é personalizada.',
        'Errou uma questão porque não percebeu a palavra “exceto”. Registro: motivo = desatenção; correção = circular palavras de comando antes de ler as alternativas.',
        ['Registre só erros relevantes (não cada pequeno deslize repetido).', 'Escreva a causa do erro (ver Capítulo 12).', 'Escreva a regra correta com suas palavras.', 'Agende revisão e refaça a questão depois de alguns dias.'],
        ['Copiar a questão inteira e a resposta, sem refletir.', 'Nunca revisar o caderno.', 'Registrar tudo e ficar com um caderno impossível de revisar.'])
    s.append(H2('Resumo: quando usar cada método'))
    s += table(['Momento', 'Métodos mais indicados'], [
        ['Primeiro contato com o assunto', 'Leitura ativa + anotações.'],
        ['Logo após a teoria', 'Recuperação ativa (folha em branco) + questões.'],
        ['Revisão de 24 h', 'Recuperação ativa + flashcards.'],
        ['Revisão de 7 e 30 dias', 'Resumos, flashcards, questões e caderno de erros.'],
        ['Reta final', 'Simulados, caderno de erros, resumos e leitura de lei seca.'],
    ], [6.0, 11.0], bold_first=True)
    return s


def cap6():
    s = chapter(6, 'Como organizar disciplinas', 'Ciclo de estudos, prioridades e reorganização da rotina')
    s.append(H2('O que é um ciclo de estudos'))
    s.append(P('Em vez de amarrar disciplinas a dias da semana (segunda = Português, terça = Matemática…), o ciclo é uma <b>sequência de disciplinas com horas definidas</b>, que você percorre na ordem, independentemente do dia. Quando termina a sequência, começa de novo.'))
    s += table(['Vantagem do ciclo', 'Por que importa'], [
        ['Nenhuma disciplina fica esquecida', 'Se você perde um dia, simplesmente continua de onde parou.'],
        ['Mais tempo para o que é difícil ou pesa mais', 'Você define as horas de cada disciplina.'],
        ['Alternância de assuntos', 'Estudar matérias diferentes em sequência reduz o cansaço e ajuda a memória.'],
        ['Flexível para quem trabalha', 'Funciona com 1, 2 ou 3 horas por dia.'],
    ], [6.0, 11.0], bold_first=True)
    s += box('atencao', 'As disciplinas e horas dos exemplos abaixo são <b>modelos de pré-edital</b>. <b>Não representam disciplinas, pesos ou distribuição oficiais</b> do concurso de Parnaíba. Quando o edital sair, refaça o ciclo com base no número de questões e nos pesos publicados.')
    s.append(H2('Como montar seu ciclo em 5 passos'))
    s += numbered([
        '<b>Liste as disciplinas</b> (use a tabela do Capítulo 2; depois, o edital).',
        '<b>Dê nota de importância (1 a 3):</b> quanto a disciplina tende a pesar na prova.',
        '<b>Dê nota de dificuldade (1 a 3):</b> quanto você domina (3 = domina pouco).',
        '<b>Some as notas</b> e distribua as horas da semana proporcionalmente à soma.',
        '<b>Defina a ordem</b>, alternando disciplinas pesadas e leves e evitando duas exatas seguidas.',
    ])
    s += table(['Disciplina (exemplo)', 'Importância', 'Dificuldade', 'Soma', 'Horas no ciclo (10 h)'], [
        ['Língua Portuguesa', '3', '2', '5', '2,5 h'],
        ['Matemática / RLM', '2', '3', '5', '2,5 h'],
        ['Lei 13.022/2014 e legislação da GCM', '3', '1', '4', '2,0 h'],
        ['Direito Constitucional / Direitos Humanos', '2', '2', '4', '1,5 h'],
        ['Noções de Informática', '2', '1', '3', '1,0 h'],
        ['Conhecimentos gerais / locais', '1', '1', '2', '0,5 h'],
    ], [6.2, 2.4, 2.4, 1.8, 4.2], bold_first=True)
    s.append(P('Cálculo: soma total = 23. Português recebe 5/23 de 10 h ≈ 2,2 h, arredondado para 2,5 h. Arredonde para blocos de 30 minutos e confira se a soma fecha o total.', 'small'))
    s.append(H2('Exemplos de ciclos adaptáveis'))
    s.append(CycleWheel([('Português', 2.5), ('Matemática/RLM', 2.5), ('Legislação GCM', 2), ('Constitucional/DH', 1.5), ('Informática', 1), ('Conh. gerais', 0.5)], 'Ciclo 10 h'))
    s.append(sp(6))
    s += table(['Ciclo', 'Para quem', 'Sequência sugerida (blocos)'], [
        ['Ciclo A — 7 h por volta (1 h/dia)', 'Quem tem 1 hora por dia.', 'Português 1 h → Matemática 1 h → Legislação GCM 1 h → Português 1 h → Informática 1 h → Matemática 1 h → Constitucional/DH 1 h.'],
        ['Ciclo B — 10 h por volta (≈2 h/dia)', 'Quem tem 2 horas por dia, 5 dias.', 'Português 1 h → Legislação 1 h → Matemática 1 h → Informática 1 h → Português 1,5 h → Constitucional/DH 1,5 h → Matemática 1,5 h → Legislação 1 h → Conh. gerais 0,5 h.'],
        ['Ciclo C — 15 h por volta (3 h/dia)', 'Quem tem 3 horas por dia.', 'Português 1,5 h → Matemática 1,5 h → Legislação 1,5 h → Informática 1 h → Constitucional/DH 1,5 h → Português 1,5 h → Matemática 1,5 h → Leis municipais 1 h → Direitos Humanos 1 h → Legislação 1,5 h → Conh. gerais 1 h.'],
    ], [4.0, 3.5, 9.5], bold_first=True)
    s.append(H2('Como alternar assuntos'))
    s += bullets([
        'Alterne <b>exatas e humanas</b>: depois de Matemática, uma disciplina de leitura (Português, Legislação).',
        'Dentro de uma disciplina, após 2 ou 3 sessões em um assunto, faça questões misturando assuntos já vistos (prática intercalada).',
        'Evite estudar o mesmo assunto por muitos dias seguidos sem praticar outros.',
    ])
    s.append(H2('Como priorizar dificuldades'))
    s.append(P('Disciplina difícil precisa de <b>mais tempo e mais cedo no dia</b>, quando você está mais descansado. Mas cuidado: não abandone o que você já domina, porque também cai na prova e é onde você garante pontos.'))
    s += table(['Situação', 'Ajuste no ciclo'], [
        ['Acertos abaixo de 60% em uma disciplina por 2–3 semanas', 'Aumente 30 a 60 min dessa disciplina por volta e volte à teoria básica.'],
        ['Acertos acima de 80% de forma estável', 'Reduza a teoria e mantenha questões e revisões.'],
        ['Um assunto específico com muitos erros', 'Crie um bloco extra só para ele por uma semana.'],
        ['Edital publicado', 'Refaça todo o ciclo com o número de questões e os pesos oficiais.'],
    ], [7.0, 10.0], bold_first=True)
    s.append(H2('Como reorganizar a rotina'))
    s.append(P('A vida muda: horário de trabalho, doença, filhos, viagens. Reorganizar não é fracassar, é ajustar.'))
    s += numbered([
        'Reavalie quantas horas reais você tem por semana agora.',
        'Mantenha a <b>ordem</b> do ciclo e reduza o tamanho dos blocos (ex.: de 1 h para 40 min).',
        'Se precisar cortar, corte primeiro teoria nova; mantenha revisões e questões.',
        'Faça a revisão do ciclo a cada 4 semanas, usando os dados do planner.',
    ])
    s.append(CondPageBreak(11 * cm))
    s += box('exerc', 'Monte agora o seu ciclo: liste as disciplinas, dê as notas de importância e dificuldade, calcule as horas para o seu total semanal e escreva a sequência. Use o espaço abaixo.')
    s.append(FormGrid(['Ordem', 'Disciplina', 'Importância (1–3)', 'Dificuldade (1–3)', 'Horas no ciclo', 'Voltas concluídas'],
                      [1.5, 5.5, 2.4, 2.4, 2.4, 2.8], 9, row_h=0.8 * cm, prefix='ciclo',
                      first_col=[str(i) for i in range(1, 10)]))
    return s
