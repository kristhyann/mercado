# -*- coding: utf-8 -*-
"""Noções de Informática."""
from render import Topico, tab, bl, h3, caixa, fluxo, num
from qbase import Q

TOPICOS = [
    Topico('Hardware',
        'Hardware é a <b>parte física</b> do computador: tudo o que se pode tocar (placas, processador, memória, teclado, monitor).',
        [
            tab(['Componente', 'Função'], [
                ['Processador (CPU)', 'Executa as instruções dos programas; é o “cérebro” do computador.'],
                ['Memória RAM', 'Memória de trabalho, rápida e <b>volátil</b> (perde os dados sem energia).'],
                ['Memória ROM', 'Guarda instruções permanentes de inicialização (firmware); não é volátil.'],
                ['Armazenamento (HD, SSD, pendrive)', 'Guarda arquivos de forma permanente. O SSD é mais rápido que o HD por não ter partes móveis.'],
                ['Placa-mãe', 'Conecta todos os componentes.'],
            ], [5.0, 12.0], 9.2),
            tab(['Periféricos de entrada', 'De saída', 'De entrada e saída'], [
                ['Teclado, mouse, scanner, microfone, webcam', 'Monitor, impressora, caixas de som', 'Tela sensível ao toque, impressora multifuncional, pendrive (armazenamento)'],
            ], [6.0, 5.0, 6.0], 9.2),
            tab(['Unidade', 'Equivale a'], [
                ['1 bit', 'Menor unidade (0 ou 1)'], ['1 byte', '8 bits'], ['1 KB', '1.024 bytes'], ['1 MB', '1.024 KB'], ['1 GB', '1.024 MB'], ['1 TB', '1.024 GB'],
            ], [5.0, 12.0], 9.2),
        ],
        exemplos=['Ao digitar um texto e o computador desligar sem salvar, o texto se perde porque estava apenas na RAM.'],
        erros=['Confundir memória RAM com armazenamento.', 'Achar que monitor é dispositivo de entrada.'],
        resumo=['CPU processa; RAM é temporária; HD/SSD armazena.', 'Entrada, saída e entrada/saída.', 'Byte = 8 bits; cada unidade ≈ 1.024 vezes a anterior.'],
        exercicios=[
            Q('Informática — Hardware', 'A memória que perde seus dados quando o computador é desligado é a',
              'memória RAM.', ['memória ROM.', 'SSD.', 'HD.', 'pendrive.'], 'A RAM é volátil.', ''),
            Q('Informática — Hardware', 'É dispositivo de entrada:',
              'scanner.', ['monitor.', 'impressora.', 'caixa de som.', 'projetor.'], 'O scanner envia dados (imagens) para o computador.', ''),
        ]),

    Topico('Software',
        'Software é a <b>parte lógica</b>: os programas e instruções que fazem o hardware funcionar.',
        [
            tab(['Tipo', 'Exemplos'], [
                ['Software básico (sistema operacional)', 'Windows, Linux, macOS, Android, iOS'],
                ['Aplicativos', 'Editores de texto, planilhas, navegadores, aplicativos de mensagens'],
                ['Utilitários', 'Antivírus, compactadores, desfragmentadores'],
                ['Drivers', 'Programas que permitem ao sistema usar um equipamento (impressora, placa de vídeo)'],
            ], [6.0, 11.0], 9.2),
            tab(['Licença', 'Significado'], [
                ['Software livre', 'Permite usar, estudar, modificar e redistribuir (código-fonte acessível). Ex.: Linux, LibreOffice.'],
                ['Freeware', 'Gratuito, mas não necessariamente com código aberto.'],
                ['Proprietário', 'Uso conforme licença do fabricante, geralmente pago, sem acesso ao código.'],
                ['Shareware / demo', 'Uso gratuito por tempo ou recursos limitados.'],
            ], [4.0, 13.0], 9.2),
        ],
        exemplos=['O LibreOffice é software livre e gratuito; um programa gratuito de código fechado é freeware.'],
        erros=['Achar que todo software gratuito é livre.'],
        resumo=['Software = programas.', 'Básico, aplicativo, utilitário, driver.', 'Livre ≠ gratuito.'],
        exercicios=[
            Q('Informática — Software', 'O programa que permite ao sistema operacional se comunicar com uma impressora é o',
              'driver.', ['firewall.', 'navegador.', 'compactador.', 'editor de texto.'], 'Drivers fazem a ponte entre o sistema e o hardware.', ''),
            Q('Informática — Software', 'Software livre é aquele que',
              'permite executar, estudar, modificar e redistribuir o programa.', ['é sempre pago.', 'não pode ser modificado.', 'só funciona sem internet.', 'é gratuito, mas sem acesso ao código.'], 'As liberdades exigem acesso ao código-fonte.', 'A última opção descreve o freeware.'),
        ]),

    Topico('Sistemas operacionais',
        'Sistema operacional é o <b>software que gerencia o hardware e serve de base</b> para os demais programas, oferecendo a interface com o usuário.',
        [
            'Funções: gerenciar processador, memória e dispositivos; organizar arquivos; controlar usuários e permissões; executar programas.',
            tab(['Atalho (Windows)', 'Função'], [
                ['Ctrl + C / Ctrl + X / Ctrl + V', 'Copiar / recortar / colar'], ['Ctrl + Z / Ctrl + Y', 'Desfazer / refazer'],
                ['Alt + Tab', 'Alternar entre janelas'], ['Alt + F4', 'Fechar a janela ativa'], ['Windows + E', 'Abrir o Explorador de Arquivos'],
                ['Windows + L', 'Bloquear a sessão'], ['Windows + D', 'Mostrar a área de trabalho'], ['Ctrl + Shift + Esc', 'Abrir o Gerenciador de Tarefas'],
                ['Delete / Shift + Delete', 'Enviar para a Lixeira / excluir permanentemente'],
            ], [6.0, 11.0], 9.2),
            'No Linux, o superusuário (administrador) chama-se <b>root</b>. Sistemas móveis mais comuns: Android e iOS.',
        ],
        exemplos=['Ao sair da mesa de trabalho, use Windows + L para bloquear o computador e proteger informações.'],
        erros=['Trocar Ctrl + C (copiar) por Ctrl + V (colar).', 'Achar que Shift + Delete envia para a Lixeira.'],
        resumo=['Sistema operacional gerencia recursos.', 'Atalhos essenciais: Ctrl+C/X/V/Z, Alt+Tab, Win+L, Win+E.'],
        exercicios=[
            Q('Informática — Sistemas operacionais', 'No Windows, o atalho que bloqueia a sessão do usuário é',
              'tecla Windows + L.', ['tecla Windows + D.', 'Alt + Tab.', 'Ctrl + Z.', 'Alt + F4.'], 'Win + L bloqueia; Win + D mostra a área de trabalho.', ''),
            Q('Informática — Sistemas operacionais', 'São exemplos de sistemas operacionais:',
              'Windows, Linux e Android.', ['Word, Excel e PowerPoint.', 'Chrome, Edge e Firefox.', 'Gmail e Outlook.', 'Antivírus e firewall.'], '', ''),
        ]),

    Topico('Arquivos e pastas',
        '<b>Arquivo</b> é um conjunto de dados gravado com um nome (documento, imagem, música, programa). <b>Pasta</b> (diretório) é um local para organizar arquivos e outras pastas.',
        [
            'O nome do arquivo costuma ter uma <b>extensão</b>, que indica o tipo e o programa que o abre.',
            tab(['Extensão', 'Tipo'], [
                ['.docx / .odt', 'Documento de texto (Word / LibreOffice Writer)'], ['.xlsx / .ods', 'Planilha (Excel / LibreOffice Calc)'], ['.pptx / .odp', 'Apresentação'],
                ['.pdf', 'Documento portátil (preserva a formatação)'], ['.jpg, .png, .gif', 'Imagens'], ['.mp3 / .mp4', 'Áudio / vídeo'], ['.zip, .rar', 'Arquivos compactados'], ['.exe', 'Programa executável (cuidado com anexos!)'],
            ], [4.0, 13.0], 9.2),
            tab(['Ação no Windows', 'Resultado'], [
                ['Arrastar para pasta na mesma unidade', 'Move o arquivo.'], ['Arrastar para outra unidade (ex.: pendrive)', 'Copia o arquivo.'],
                ['Ctrl + arrastar', 'Força a cópia.'], ['Atalho na área de trabalho', 'Ícone que aponta para o item original; apagá-lo não apaga o original.'],
            ], [6.6, 10.4], 9.2),
        ],
        exemplos=['Estrutura organizada: Documentos > Estudos > Português > Crase.pdf'],
        erros=['Abrir anexos .exe recebidos de desconhecidos.', 'Achar que apagar o atalho apaga o arquivo.'],
        resumo=['Extensão indica o tipo de arquivo.', 'Mesma unidade: move; outra unidade: copia.'],
        exercicios=[
            Q('Informática — Arquivos', 'A extensão normalmente associada a uma planilha do Excel é',
              '.xlsx', ['.docx', '.mp3', '.jpg', '.pptx'], '.xlsx = planilha do Excel.', ''),
            Q('Informática — Arquivos', 'Ao arrastar um arquivo para outra pasta na MESMA unidade de disco, no Windows, ele é, por padrão,',
              'movido.', ['copiado.', 'excluído.', 'compactado.', 'enviado por e-mail.'], 'Na mesma unidade, arrastar move.', ''),
        ]),

    Topico('Internet',
        'Internet é a <b>rede mundial de computadores</b> interligados que trocam informações por meio de protocolos padronizados.',
        [
            tab(['Termo', 'Significado'], [
                ['Protocolo', 'Conjunto de regras de comunicação (ex.: HTTP, HTTPS, SMTP).'],
                ['HTTP / HTTPS', 'Transferência de páginas web; o HTTPS usa criptografia (conexão segura).'],
                ['URL', 'Endereço de um recurso: https://www.exemplo.gov.br/pagina'],
                ['Domínio', 'Nome do site; “.gov.br” indica órgão governamental brasileiro.'],
                ['DNS', 'Traduz nomes de domínio em endereços IP.'],
                ['IP', 'Endereço numérico de um dispositivo na rede.'],
                ['Intranet', 'Rede privada de uma organização com tecnologias da internet.'],
                ['Nuvem (cloud)', 'Armazenamento e serviços em servidores remotos acessados pela internet (ex.: Google Drive, OneDrive).'],
                ['Download / upload', 'Baixar da internet / enviar para a internet.'],
            ], [3.6, 13.4], 9.2),
        ],
        exemplos=['Em “https://www.ibge.gov.br”, “https” é o protocolo seguro e “ibge.gov.br” é o domínio de um órgão público.'],
        erros=['Achar que o cadeado (HTTPS) garante, sozinho, que o site é honesto: ele indica apenas conexão criptografada.'],
        resumo=['Protocolos: HTTP/HTTPS (web), SMTP (envio de e-mail).', 'DNS traduz nomes em IPs.', 'Intranet: rede privada.'],
        exercicios=[
            Q('Informática — Internet', 'O serviço que converte nomes de domínio em endereços IP é o',
              'DNS.', ['HTML.', 'USB.', 'VPN.', 'PDF.'], '', ''),
            Q('Informática — Internet', 'O protocolo que indica conexão criptografada entre navegador e site é o',
              'HTTPS.', ['HTTP.', 'FTP.', 'SMTP.', 'HTML.'], '', 'HTML é linguagem de marcação, não protocolo.'),
        ]),

    Topico('Navegadores',
        'Navegador (browser) é o <b>programa usado para acessar páginas da web</b>. Exemplos: Google Chrome, Microsoft Edge, Mozilla Firefox, Safari.',
        [
            tab(['Recurso / atalho', 'Função'], [
                ['Ctrl + T', 'Nova aba'], ['Ctrl + W', 'Fechar aba'], ['Ctrl + Shift + T', 'Reabrir a última aba fechada'], ['Ctrl + H', 'Histórico'],
                ['Ctrl + D', 'Adicionar aos favoritos'], ['F5', 'Atualizar a página'], ['Ctrl + Shift + N (Chrome/Edge)', 'Janela anônima/privada'],
            ], [6.0, 11.0], 9.2),
            tab(['Conceito', 'Explicação'], [
                ['Histórico', 'Lista de páginas visitadas.'], ['Cookies', 'Pequenos arquivos gravados pelos sites para lembrar preferências e sessões.'],
                ['Cache', 'Cópia temporária de páginas para carregar mais rápido.'], ['Navegação anônima', 'Não salva histórico, cookies e dados de formulário no dispositivo após fechar a janela, mas NÃO torna o usuário invisível para sites, provedor ou rede.'],
            ], [4.0, 13.0], 9.2),
        ],
        exemplos=['Em um computador público, usar a navegação anônima evita que seu histórico fique salvo naquele aparelho.'],
        erros=['Achar que a navegação anônima protege contra vírus ou garante anonimato total.'],
        resumo=['Ctrl+T nova aba; Ctrl+H histórico; F5 atualiza.', 'Modo anônimo: não grava dados localmente.'],
        exercicios=[
            Q('Informática — Navegadores', 'A navegação anônima nos navegadores',
              'não salva histórico e cookies no dispositivo após fechar a janela.', ['torna o usuário invisível para o provedor.', 'impede qualquer vírus.', 'acelera a conexão.', 'bloqueia todos os anúncios.'], '', ''),
            Q('Informática — Navegadores', 'Na maioria dos navegadores, o atalho Ctrl + H abre',
              'o histórico.', ['uma nova aba.', 'os favoritos.', 'a impressão.', 'a página inicial.'], '', ''),
        ]),

    Topico('Correio eletrônico (e-mail)',
        'E-mail é o <b>serviço de envio e recebimento de mensagens eletrônicas</b>, que podem conter anexos.',
        [
            tab(['Campo', 'Função'], [
                ['Para', 'Destinatário principal.'], ['Cc (cópia)', 'Destinatários em cópia; todos veem os endereços.'],
                ['Cco (cópia oculta)', 'Destinatários ocultos; os demais não veem esses endereços.'], ['Assunto', 'Resumo do conteúdo.'], ['Anexo', 'Arquivo enviado junto.'],
            ], [4.0, 13.0], 9.2),
            tab(['Ação', 'Efeito'], [
                ['Responder', 'Responde apenas ao remetente.'], ['Responder a todos', 'Responde ao remetente e aos destinatários visíveis (Para e Cc), não aos de Cco.'], ['Encaminhar', 'Envia a mensagem a outras pessoas.'],
            ], [4.0, 13.0], 9.2),
            'Protocolos: <b>SMTP</b> (envio), <b>POP3</b> e <b>IMAP</b> (recebimento; o IMAP mantém as mensagens sincronizadas no servidor).',
        ],
        exemplos=['Para enviar um comunicado a muitos moradores sem expor os e-mails de todos, coloque-os em Cco.'],
        erros=['Usar “Responder a todos” sem necessidade, expondo informações.', 'Abrir anexos suspeitos.'],
        resumo=['Cc: cópia visível; Cco: cópia oculta.', 'SMTP envia; POP3/IMAP recebem.'],
        exercicios=[
            Q('Informática — E-mail', 'O campo usado para enviar uma mensagem a destinatários sem que os demais vejam seus endereços é o',
              'Cco.', ['Cc.', 'Para.', 'Assunto.', 'Anexo.'], '', ''),
            Q('Informática — E-mail', 'O protocolo usado para o ENVIO de e-mails é o',
              'SMTP.', ['POP3.', 'IMAP.', 'DNS.', 'HTTP.'], '', ''),
        ]),

    Topico('Segurança da informação',
        'Segurança da informação é o conjunto de práticas para proteger dados e sistemas, garantindo <b>confidencialidade, integridade e disponibilidade</b>.',
        [
            tab(['Pilar', 'Significado', 'Exemplo de ameaça'], [
                ['Confidencialidade', 'Acesso apenas por pessoas autorizadas.', 'Vazamento de senhas.'],
                ['Integridade', 'A informação não é alterada indevidamente.', 'Alteração de um relatório por invasor.'],
                ['Disponibilidade', 'A informação está acessível quando necessária.', 'Sistema fora do ar por ataque.'],
            ], [4.0, 6.6, 6.4], 9.2),
            tab(['Ameaça', 'Como funciona', 'Proteção'], [
                ['Phishing', 'Mensagens falsas que imitam bancos ou órgãos para roubar dados.', 'Desconfiar de urgência, conferir o remetente e o endereço do site.'],
                ['Engenharia social', 'Manipulação psicológica para obter informações (ex.: falso suporte técnico).', 'Verificar por canais oficiais; nunca informar senhas.'],
            ], [3.6, 7.2, 6.2], 9.2),
            'Ferramentas de proteção: <b>antivírus</b> (detecta e remove códigos maliciosos), <b>firewall</b> (controla o tráfego de rede), <b>atualizações</b> do sistema (corrigem falhas), <b>autenticação em dois fatores</b>.',
        ],
        exemplos=['Um SMS dizendo “Sua conta será bloqueada, clique aqui” é típico de phishing.'],
        erros=['Achar que firewall remove vírus (essa é a função do antivírus).'],
        resumo=['Pilares: confidencialidade, integridade, disponibilidade.', 'Phishing e engenharia social exploram a confiança.'],
        exercicios=[
            Q('Informática — Segurança', 'O princípio que garante que a informação não seja alterada indevidamente é a',
              'integridade.', ['confidencialidade.', 'disponibilidade.', 'portabilidade.', 'velocidade.'], '', ''),
            Q('Informática — Segurança', 'O firewall tem como função principal',
              'controlar o tráfego de rede, permitindo ou bloqueando conexões.', ['remover vírus de arquivos.', 'fazer backup.', 'acelerar o processador.', 'criar senhas.'], '', ''),
        ]),

    Topico('Vírus e outros códigos maliciosos (malware)',
        'Malware é <b>qualquer software criado para causar danos</b>, roubar dados ou obter controle indevido de um sistema.',
        [
            tab(['Tipo', 'Característica'], [
                ['Vírus', 'Infecta arquivos e se propaga quando o arquivo infectado é executado.'],
                ['Worm (verme)', 'Propaga-se sozinho pela rede, sem precisar de arquivo hospedeiro.'],
                ['Cavalo de Troia (trojan)', 'Disfarça-se de programa legítimo e abre brechas no sistema.'],
                ['Ransomware', 'Criptografa os arquivos e exige pagamento (resgate).'],
                ['Spyware', 'Espiona as atividades do usuário.'],
                ['Keylogger', 'Registra as teclas digitadas (pode capturar senhas).'],
                ['Adware', 'Exibe propagandas indesejadas.'],
            ], [4.6, 12.4], 9.2),
            caixa('dica', 'Proteção: mantenha sistema e antivírus atualizados, não abra anexos suspeitos, baixe programas apenas de fontes oficiais e faça backups regulares (principal defesa contra ransomware).'),
        ],
        exemplos=['Um “boleto_atrasado.exe” recebido por e-mail é provavelmente um malware.'],
        erros=['Confundir worm (propagação automática) com vírus (precisa de execução).'],
        resumo=['Vírus, worm, trojan, ransomware, spyware, keylogger, adware.', 'Backup protege contra ransomware.'],
        exercicios=[
            Q('Informática — Malware', 'O malware que criptografa arquivos e exige pagamento para liberá-los é o',
              'ransomware.', ['adware.', 'spyware.', 'worm.', 'keylogger.'], '', ''),
            Q('Informática — Malware', 'O malware que se disfarça de programa legítimo para enganar o usuário é o',
              'cavalo de Troia.', ['firewall.', 'backup.', 'adware.', 'worm.'], '', ''),
        ]),

    Topico('Senhas e autenticação',
        'Senha é a <b>chave de acesso</b> a contas e sistemas. Autenticação é o processo de confirmar a identidade do usuário.',
        [
            tab(['Boa prática', 'Por quê'], [
                ['Senhas longas, com letras maiúsculas e minúsculas, números e símbolos', 'Mais difíceis de adivinhar ou quebrar.'],
                ['Não usar dados pessoais (nome, data de nascimento)', 'São facilmente descobertos.'],
                ['Senhas diferentes para cada serviço', 'Se uma vazar, as outras continuam protegidas.'],
                ['Gerenciador de senhas', 'Ajuda a guardar senhas fortes com segurança.'],
                ['Autenticação em dois fatores (2FA)', 'Mesmo que a senha vaze, o invasor precisa do segundo fator (código, aplicativo, biometria).'],
                ['Nunca compartilhar senhas', 'A senha é pessoal e intransferível.'],
            ], [7.6, 9.4], 9.2),
            'Fatores de autenticação: algo que você <b>sabe</b> (senha), algo que você <b>tem</b> (celular, token) e algo que você <b>é</b> (biometria).',
        ],
        exemplos=['Senha fraca: 123456. Senha forte: uma frase longa com símbolos, como “Cafe#Delta-2027!praia”.'],
        erros=['Usar a mesma senha em todos os sites.', 'Anotar a senha em papel colado no monitor.'],
        resumo=['Senhas longas, únicas e sem dados pessoais.', '2FA: segundo fator de verificação.'],
        exercicios=[
            Q('Informática — Senhas', 'A autenticação em dois fatores aumenta a segurança porque',
              'exige, além da senha, uma segunda forma de verificação.', ['dispensa senhas.', 'remove vírus.', 'aumenta a velocidade da internet.', 'faz backup automático.'], '', ''),
            Q('Informática — Senhas', 'Qual senha é a mais segura?',
              'T@refa-Longa#2027!', ['123456', 'senha', 'maria1990', 'qwerty'], 'Longa e com tipos variados de caracteres.', ''),
        ]),

    Topico('Backup',
        'Backup é a <b>cópia de segurança dos dados</b>, guardada em outro local, para recuperação em caso de perda, falha, exclusão acidental ou ataque.',
        [
            tab(['Tipo de backup', 'Como funciona'], [
                ['Completo', 'Copia todos os dados selecionados.'],
                ['Incremental', 'Copia apenas o que mudou desde o último backup (de qualquer tipo).'],
                ['Diferencial', 'Copia o que mudou desde o último backup completo.'],
            ], [4.0, 13.0], 9.2),
            caixa('dica', 'Regra prática conhecida como “3-2-1”: tenha 3 cópias dos dados, em 2 mídias diferentes, sendo 1 fora do local (por exemplo, na nuvem). Teste a restauração periodicamente.'),
        ],
        exemplos=['Guardar as fotos do celular no computador e também na nuvem.'],
        erros=['Guardar o backup no mesmo disco dos dados originais.', 'Nunca testar se o backup funciona.'],
        resumo=['Backup = cópia de segurança em outro local.', 'Completo, incremental, diferencial.'],
        exercicios=[
            Q('Informática — Backup', 'O tipo de backup que copia apenas o que mudou desde o último backup completo é o',
              'diferencial.', ['incremental.', 'completo.', 'espelhado em RAM.', 'compactado.'], '', 'O incremental copia o que mudou desde o último backup de qualquer tipo.'),
            Q('Informática — Backup', 'A principal defesa contra a perda de dados por ransomware é',
              'manter backups atualizados e guardados em outro local.', ['desligar o monitor.', 'usar navegação anônima.', 'aumentar a memória RAM.', 'apagar os cookies.'], '', ''),
        ]),

    Topico('Ferramentas de produtividade',
        'Ferramentas de produtividade são os <b>aplicativos de escritório</b>: editores de texto, planilhas e apresentações.',
        [
            tab(['Função', 'Microsoft Office', 'LibreOffice (livre)', 'Google (online)'], [
                ['Texto', 'Word', 'Writer', 'Documentos'], ['Planilha', 'Excel', 'Calc', 'Planilhas'], ['Apresentação', 'PowerPoint', 'Impress', 'Apresentações'],
            ], [3.6, 4.4, 4.4, 4.6], 9.2),
            'O formato <b>PDF</b> preserva a aparência do documento em qualquer dispositivo e é indicado para envio e impressão. Para editar, use o formato original (.docx, .odt).',
        ],
        exemplos=['Um relatório é escrito no Word ou Writer e enviado em PDF para garantir a formatação.'],
        erros=['Confundir planilha (cálculos) com apresentação (slides).'],
        resumo=['Texto: Word/Writer; planilha: Excel/Calc; apresentação: PowerPoint/Impress.'],
        exercicios=[
            Q('Informática — Produtividade', 'No LibreOffice, o programa equivalente ao Excel é o',
              'Calc.', ['Writer.', 'Impress.', 'Draw.', 'Base.'], '', ''),
            Q('Informática — Produtividade', 'Para apresentar slides em uma reunião, utiliza-se',
              'PowerPoint ou Impress.', ['Excel ou Calc.', 'Paint.', 'Bloco de Notas.', 'Explorador de Arquivos.'], '', ''),
        ]),

    Topico('Edição de texto',
        'Editores de texto permitem <b>criar, formatar e revisar documentos</b>: fonte, tamanho, negrito, alinhamento, listas, tabelas, cabeçalhos e numeração de páginas.',
        [
            tab(['Recurso', 'Uso'], [
                ['Formatação de caractere', 'Fonte, tamanho, negrito, itálico, sublinhado, cor.'],
                ['Formatação de parágrafo', 'Alinhamento (esquerda, centro, direita, justificado), espaçamento, recuo.'],
                ['Listas', 'Marcadores ou numeração.'],
                ['Cabeçalho e rodapé', 'Textos repetidos em todas as páginas (ex.: número da página).'],
                ['Localizar e substituir', 'Encontrar e trocar palavras em todo o documento.'],
                ['Revisão ortográfica', 'Indica possíveis erros de escrita.'],
            ], [5.0, 12.0], 9.2),
            tab(['Atalho', 'Word (português)', 'LibreOffice Writer'], [
                ['Negrito', 'Ctrl + N', 'Ctrl + B'], ['Itálico', 'Ctrl + I', 'Ctrl + I'], ['Sublinhado', 'Ctrl + S', 'Ctrl + U'], ['Salvar', 'Ctrl + B', 'Ctrl + S'],
            ], [4.0, 6.5, 6.5], 9.2),
            caixa('atencao', 'Os atalhos mudam conforme o programa e o idioma. Em provas, observe a versão indicada no enunciado.'),
        ],
        exemplos=['Para que todas as páginas tenham o número no rodapé, use o recurso de cabeçalho/rodapé com numeração automática.'],
        erros=['Digitar o número da página manualmente em cada página.'],
        resumo=['Formatação de caractere e de parágrafo.', 'Atalhos variam entre Word (PT) e Writer.'],
        exercicios=[
            Q('Informática — Edição de texto', 'No Microsoft Word em português, o atalho Ctrl + N aplica',
              'negrito.', ['novo documento.', 'itálico.', 'numeração.', 'nota de rodapé.'], '', 'No Writer, negrito é Ctrl + B.'),
            Q('Informática — Edição de texto', 'O alinhamento que distribui o texto uniformemente entre as margens esquerda e direita é o',
              'justificado.', ['centralizado.', 'à esquerda.', 'à direita.', 'recuado.'], '', ''),
        ]),

    Topico('Planilhas eletrônicas',
        'Planilhas organizam dados em <b>linhas (números) e colunas (letras)</b>; o cruzamento forma a <b>célula</b> (ex.: B3). Permitem cálculos com fórmulas e funções.',
        [
            'Toda fórmula começa com <b>=</b>. Operadores: + (soma), − (subtração), * (multiplicação), / (divisão), ^ (potência).',
            tab(['Função', 'O que faz', 'Exemplo'], [
                ['=SOMA(A1:A5)', 'Soma o intervalo de A1 a A5.', 'A1:A5 = A1, A2, A3, A4, A5'],
                ['=MÉDIA(B1:B3)', 'Média aritmética.', '(4 + 6 + 8) ÷ 3 = 6'],
                ['=MÁXIMO / =MÍNIMO', 'Maior / menor valor.', '=MÁXIMO(C1:C10)'],
                ['=SE(teste; verdadeiro; falso)', 'Retorna um valor se o teste for verdadeiro e outro se falso.', '=SE(A1>=7;"Aprovado";"Reprovado")'],
                ['=CONT.NÚM', 'Conta células com números.', '=CONT.NÚM(A1:A20)'],
            ], [5.0, 6.0, 6.0], 9.0),
            tab(['Referência', 'Comportamento ao copiar a fórmula'], [
                ['A1 (relativa)', 'Coluna e linha mudam.'], ['$A$1 (absoluta)', 'Não muda.'], ['$A1 / A$1 (mista)', 'Fixa só a coluna / só a linha.'],
            ], [5.0, 12.0], 9.2),
            caixa('atencao', 'Nas versões em português, os argumentos das funções são separados por ponto e vírgula (;). O dois-pontos (:) indica intervalo.'),
        ],
        exemplos=['Se B1 = 4, B2 = 6 e B3 = 8: =SOMA(B1:B3) = 18; =MÉDIA(B1:B3) = 6.'],
        erros=['Esquecer o sinal de igual.', 'Confundir =SOMA(A1;A5) (só duas células) com =SOMA(A1:A5) (intervalo).'],
        resumo=['Célula = coluna + linha.', 'Fórmulas começam com =.', '$ fixa linha e/ou coluna.'],
        exercicios=[
            Q('Informática — Planilhas', 'As células A1, A2 e A3 contêm 10, 20 e 30. O resultado de =MÉDIA(A1:A3) é',
              '20', ['10', '30', '60', '3'], '(10 + 20 + 30) ÷ 3 = 60 ÷ 3 = 20.', '60 seria a soma.'),
            Q('Informática — Planilhas', 'Na fórmula =A1*$B$1, ao copiá-la para a linha de baixo, a referência $B$1',
              'permanece $B$1.', ['passa a ser $B$2.', 'passa a ser B2.', 'é apagada.', 'vira A2.'], 'O cifrão fixa coluna e linha (referência absoluta).', ''),
        ]),
]

REVISAO = [
    Q('Revisão — Informática', 'São exemplos de dispositivos de saída:',
      'monitor e impressora.', ['teclado e mouse.', 'scanner e microfone.', 'webcam e teclado.', 'mouse e scanner.'], '', ''),
    Q('Revisão — Informática', 'A combinação de teclas que abre o Explorador de Arquivos no Windows é',
      'Windows + E.', ['Windows + L.', 'Windows + D.', 'Alt + F4.', 'Ctrl + Esc.'], '', ''),
    Q('Revisão — Informática', 'Mensagens falsas que imitam instituições para obter dados pessoais caracterizam',
      'phishing.', ['backup.', 'firewall.', 'cookie.', 'driver.'], '', ''),
    Q('Revisão — Informática', 'Em uma planilha, o resultado de =SOMA(A1:A4), sendo A1=2, A2=4, A3=6 e A4=8, é',
      '20', ['8', '12', '5', '48'], '2 + 4 + 6 + 8 = 20.', ''),
    Q('Revisão — Informática', 'O malware que se propaga sozinho pela rede, sem precisar de arquivo hospedeiro, é o',
      'worm.', ['vírus de macro.', 'adware.', 'cookie.', 'driver.'], '', ''),
    Q('Revisão — Informática', 'O formato de arquivo mais indicado para preservar a formatação de um documento em qualquer dispositivo é o',
      'PDF.', ['TXT.', 'MP3.', 'EXE.', 'ZIP.'], '', ''),
]

RESUMO_CAP = [
    ['Hardware e software', 'Hardware é físico; software é lógico. CPU processa; RAM volátil; HD/SSD armazena. Livre ≠ gratuito.'],
    ['Sistema operacional', 'Gerencia recursos; atalhos Ctrl+C/X/V/Z, Alt+Tab, Win+L, Win+E, Shift+Delete.'],
    ['Arquivos e pastas', 'Extensões (.docx, .xlsx, .pdf, .jpg, .exe); mesma unidade move, outra unidade copia.'],
    ['Internet e navegadores', 'HTTPS, DNS, URL, domínio .gov.br; modo anônimo não grava dados no dispositivo.'],
    ['E-mail', 'Cc visível, Cco oculto; SMTP envia, POP3/IMAP recebem.'],
    ['Segurança', 'Confidencialidade, integridade, disponibilidade; phishing; malware; senhas fortes; 2FA; backup.'],
    ['Produtividade', 'Word/Writer, Excel/Calc, PowerPoint/Impress; PDF preserva formatação.'],
    ['Planilhas', 'Fórmulas com =; SOMA, MÉDIA, MÁXIMO, SE; referência absoluta com $.'],
]
