# Curso: Vídeos 3D com IA e Claude Code. Plano de gravação

**Formato das aulas:** tela gravada + sua voz (pode ser a voz da IA) + legenda. Cada aula tem de 3 a 8 minutos e ensina **uma coisa só**.
**Regra de ouro:** o aluno aperta play e repete o que vê. Mostre cada clique e evite pular etapas.

---

## Como gravar (equipamento mínimo)
| Onde você grava | Ferramenta grátis | Dica |
|---|---|---|
| Computador | **OBS Studio** (Windows/Mac) | Grave em 1080p. Aumente o zoom do navegador ou terminal pra 125–150% pra letra ficar legível no celular |
| Android | Gravador de tela nativo (puxe a barra de cima → "Gravar tela") | Ative "mostrar toques" nas Opções do desenvolvedor, pra o aluno ver onde você toca |
| Voz | Microfone de fone com fio já resolve. Grave num lugar sem eco | Ou grave sem voz e narre depois com o ElevenLabs, como nos seus vídeos |
| Edição | CapCut (PC ou celular) | Corte as esperas (render, instalação) e coloque "⏩ acelerado" na tela |

**Estrutura de toda aula (fixa):**
1. **0–10 s:** "Nesta aula você vai…" + o resultado final na tela.
2. **Passo a passo:** gravação de tela.
3. **Fechamento (10 s):** "Pronto, agora você já… Na próxima aula…"

**Abertura do curso:** use o seu anúncio de 49 s como aula 0 ("O que você vai aprender").

---

## MÓDULO 1: Preparando tudo (o aluno sai com o Claude Code funcionando)

### Aula 1.1: O que é o Claude e o Claude Code
- Claude é a IA da Anthropic. O **Claude Code** é o "modo programador": ele cria arquivos, roda programas e monta o vídeo sozinho, a partir do que você pede em português.
- O aluno não precisa saber programar: ele só conversa.
- Mostre um vídeo pronto seu e diga: "isso aqui foi feito conversando".

### Aula 1.2: Criando a conta e escolhendo o plano
- Entrar em **claude.ai** e criar a conta (Google ou e-mail).
- O Claude Code precisa de um **plano pago** (Pro ou superior). Mostre a tela de planos e diga pra o aluno conferir o preço atual na moeda dele. Não fale um valor fixo, porque muda.

### Aula 1.3: Usando pelo celular Android ou pelo navegador (sem instalar nada)
- Abrir o **app do Claude** (ou o navegador em **claude.ai/code**) e ir na parte de **Code**.
- Conectar uma conta do **GitHub** (é onde ficam guardados os projetos e vídeos). Mostre a criação da conta no GitHub e a criação de um repositório vazio, por exemplo `meus-videos`.
- Abrir uma sessão nesse repositório e mandar "oi" pra testar.
- *Atenção:* grave essa aula olhando a tela atual do app, porque os menus mudam de nome com o tempo.

### Aula 1.4: Instalando no computador (opcional, pra quem prefere)
- **Windows:** abrir o PowerShell e colar o comando de instalação da página oficial (**code.claude.com/docs**, seção de instalação).
- **Mac ou Linux:** abrir o Terminal e colar o comando da mesma página.
- Digitar `claude`, fazer login com a conta e testar.
- Mostrar também o **app Claude para desktop**, que tem o Claude Code dentro, pra quem não quer terminal.
- *Grave copiando o comando direto da página oficial no dia da gravação. Não deixe um comando fixo na tela, porque ele pode mudar.*

### Aula 1.5: Instalando a skill de vídeos 3D
- **O que é uma skill:** um arquivo de instruções que ensina o Claude a fazer uma tarefa sempre do mesmo jeito. A sua é a **"construa-do-zero"**.
- **Pelo site ou app:** em claude.ai, Configurações → Capacidades/Skills → **Enviar skill** → escolher o `.zip` que vem no curso. Depois disso, ela aparece sozinha nas sessões do Claude Code.
- **No computador:** colocar a pasta da skill em `~/.claude/skills/construa-do-zero/` (a pasta precisa ter o arquivo `SKILL.md`).
- **Teste:** escrever "quero fazer um vídeo". O Claude deve responder com as perguntas da skill (tema, voz, mascote).
- *Você vai precisar entregar a skill pro aluno como arquivo pra baixar (veja "Próximos passos" no fim).*

---

## MÓDULO 2: Seu primeiro vídeo 3D (do zero até o mp4)

### Aula 2.1: Escolhendo o tema e pedindo o roteiro
- Escrever "quero fazer um vídeo sobre como funciona uma descarga".
- Mostrar o roteiro chegando: gancho, "Mas…", "Então…", nome da peça, final com "Segue a página".
- Ensinar a pedir ajustes, por exemplo: "deixa o gancho mais forte", "quero 1 minuto e 20".

### Aula 2.2: Gerando a voz no ElevenLabs
- Copiar o `roteiro_voz.txt` e colar no ElevenLabs (texto para fala).
- Escolher a voz (mostre as que você usa, como a Will e o Renato). Explique estabilidade e similaridade (você usa 50 e 75).
- Baixar o mp3 e enviar na conversa do Claude.
- Truque: números já vêm escritos por extenso no roteiro, pra a voz não errar.

### Aula 2.3: O Claude monta a cena 3D
- Mostrar o Claude criando a cena, gerando as imagens de teste e corrigindo sozinho.
- Ensinar a pedir correções por tempo: "aos 20 segundos a câmera está muito perto", "a etiqueta está cobrindo o objeto".

### Aula 2.4: Render, capa e títulos
- O render demora (⏩ acelere na edição). No fim, o Claude manda **final.mp4**, **capa.jpg** e **titulos.txt**.
- Mostrar a marca d'água e explicar como trocar pelo @ do aluno (pedir: "minha marca d'água é @fulano").

### Aula 2.5: Usando um áudio pronto (sem roteiro)
- Mostrar o caso do macaco: enviar um mp3 qualquer e escrever "faça um vídeo com esse áudio". O Claude transcreve e monta.

---

## MÓDULO 3: Formatos que você pode produzir (um vídeo seu por aula)
Cada aula mostra o vídeo pronto e **a frase exata que você pediu** pro Claude:
1. **Como funciona / construção** (descarga, escada rolante, celular)
2. **Curiosidade animal em 2ª pessoa** ("você é uma barata")
3. **História emocionante** (elefante)
4. **Fé / parábola** (filho pródigo), com marca d'água própria
5. **Piada / humor com personagens** (o Caco)
6. **Historinha com produto ou oferta** (manicure + "comenta AGENDA")

---

## MÓDULO 4: Temas que têm chance de viralizar
*(Não prometa viralização. Ensine o método.)*

### Aula 4.1: De onde tirar ideias
- **Pesquisa nas redes:** na busca do TikTok e do YouTube Shorts, procure "como funciona", "você sabia", "curiosidades". Filtre pelos mais vistos e anote os temas que se repetem.
- **Comentários:** perguntas nos comentários dos seus vídeos e dos concorrentes ("e o vaso sanitário de avião?") viram temas.
- **Coisas do dia a dia que todo mundo usa e ninguém sabe como funcionam:** fone, torradeira, escada rolante, descarga.
- **Google Trends:** veja o que está subindo no Brasil.

### Aula 4.2: Pedindo ideias pro Claude
Prompt pra mostrar na tela:
> "Me dê 15 ideias de vídeos curtos 3D no estilo 'como funciona' sobre objetos do dia a dia. Para cada uma: o gancho dos 3 primeiros segundos, as 4 peças que vou montar e por que a pessoa ficaria até o fim."

### Aula 4.3: O gancho decide tudo
- **Pergunta impossível de ignorar:** "Pra onde vai tudo?"
- **Afirmação estranha:** "Você vive uma semana sem cabeça".
- **Mistério visual:** "Por que os degraus somem?"
- **Texto grande no primeiro segundo:** mostre os seus exemplos.

### Aula 4.4: Medindo o que funcionou
- Na análise de cada rede, olhe a **retenção nos 3 primeiros segundos** e a **porcentagem que assistiu até o fim**.
- Faça mais do formato que segura as pessoas e mude o gancho do que não segurou.

---

## MÓDULO 5: Montando suas redes sociais

### Aula 5.1: Criando os perfis
- **YouTube:** criar o canal com nome, foto, banner e descrição.
- **TikTok e Instagram:** passar o Instagram pra **conta profissional** (Criador).
- **Nome igual em tudo** (como o seu @olhaso_3D) e a mesma foto em todas as redes.
- Bio em uma frase: "Vídeos 3D mostrando como as coisas funcionam por dentro".

### Aula 5.2: Postando do jeito certo
- O mesmo vídeo vertical vai pras 3 redes.
- Use o `titulos.txt`: um título e hashtags pra cada rede. Fixe o comentário.
- Constância: escolha um ritmo que você consiga manter (ex.: 1 vídeo por dia ou 3 por semana).
- Responda os primeiros comentários.

### Aula 5.3: Como funciona a monetização
- **YouTube (Programa de Parcerias)** e **TikTok (programa de recompensas para criadores):** cada plataforma exige um número mínimo de inscritos ou seguidores e de visualizações.
- Mostre a página oficial de requisitos de cada uma **no dia da gravação**, porque os números mudam.
- Outros caminhos: vender um produto (como você faz com a agenda e com este curso), parcerias e serviços de criação de vídeo pra outras pessoas.
- **Seja honesto:** não existe prazo garantido pra monetizar.

### Aula 5.4: Respostas automáticas (ManyChat)
- Usar o guia `videos/anuncio-curso/manychat.md`: comenta a palavra e recebe o link no direct.

---

## Bônus
- **Aula B1:** criando o anúncio do seu próprio produto (mostre o seu anúncio de 49 s sendo feito).
- **Aula B2:** problemas comuns e como resolver:
  - o render parou;
  - a voz ficou longa demais;
  - a legenda errou uma palavra;
  - a câmera ficou longe.
  - Em todos os casos, a solução é pedir em português.

---

## Ordem de gravação sugerida (pra lançar rápido)
1. Aula 0 (anúncio), 1.1, 1.2, 1.3, 1.5, 2.1, 2.2, 2.3, 2.4. Com isso o aluno já faz o primeiro vídeo.
2. Depois: módulos 3, 4 e 5.
3. Por último: 1.4 (computador), 2.5 e os bônus.
