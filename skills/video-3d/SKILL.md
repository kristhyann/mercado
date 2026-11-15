---
name: video-3d
description: "Cria do começo ao fim um vídeo vertical 3D low-poly para Reels, TikTok e Shorts (gancho forte, cenas 3D sincronizadas com a voz, legenda palavra por palavra, efeitos, capa e títulos com hashtags). Use quando a pessoa pedir para fazer, gerar ou criar um vídeo 3D, um vídeo do canal, ou disser \"quero fazer um vídeo\", ou mandar um áudio pedindo um vídeo."
---

# Vídeo 3D: do tema ao final.mp4

Você entrega um vídeo pronto para postar (**final.mp4 + capa.jpg + titulos.txt**) para uma pessoa que **não sabe programar**.
- Fale em português simples e resolva sozinho tudo que for técnico.
- Só pare nos pontos marcados com **⏸ PARADA**.
- A pasta desta skill (onde está este SKILL.md) tem:
  - `kit/`: programas prontos;
  - `modelos/scene_modelo.html`: modelo de cena;
  - `referencias/roteiro.md` e `referencias/estilo.md`: **leia as duas antes de escrever o roteiro e a cena**.

---

## 1. ⏸ PARADA 1: perguntas (uma única mensagem, curta)

Antes de perguntar, veja se existe `videos/_config.json`: ele guarda a marca d'água e as preferências do último vídeo, pra você sugerir.

Pergunte tudo de uma vez, com sugestões entre parênteses. Aceite "pode escolher" em qualquer item.

1. **Tema:** qual tema? Sugira 3 temas com cara de viral, de formatos diferentes (ex.: "Como funciona a descarga?", "Você é uma barata", "O elefante nunca esquece quem cuidou dele").
2. **Duração:** quantos minutos? (30 s · 1 min · 1min30 · 2 min. Recomendo de 1 min a 1min30.)
3. **Voz:** como vai ser?
   - **a)** gero aqui no Claude, grátis (voz sintética, menos natural);
   - **b)** te mando o roteiro e você gera a voz em outro lugar (ElevenLabs, OpenArt…) e me manda o mp3;
   - **c)** você já tem um áudio pronto (aí eu não escrevo roteiro, só monto em cima dele).
4. **Marca d'água:** qual @ vai aparecer no vídeo e na capa? (sugira a última usada, se houver)
5. **Formato:** construa do zero / como funciona · curiosidade em 2ª pessoa ("você é um…") · história emocionante · fé / reflexão · humor com personagens · historinha que vende um produto. Se a pessoa não escolher, decida pelo tema.
6. **Final:** "Segue a página…" (padrão) ou "Comenta <PALAVRA>" (se tiver produto ou link, qual palavra?).

Depois da resposta:
- crie `videos/<tema-sem-acento-com-hifen>/` e trabalhe sempre nela;
- salve as respostas em `videos/_config.json` (`marca`, `voz`, `final`);
- se existir `CLAUDE.md` no projeto, garanta que ele diga que a marca d'água é obrigatória.

## 2. Preparar o computador (sem perguntar, só avise em uma linha)

Faça isso **enquanto espera** as respostas ou a voz.

- Se `videos/_kit/` não existir: copie `kit/` desta skill para `videos/_kit/`, e dentro dele rode `npm install`.
- Se o Chromium do Playwright não estiver instalado: `npx playwright install chromium`. Se o ambiente já tiver o Playwright, use o que existe.
- Instale o necessário em Python: `pip install faster-whisper soundfile numpy pillow fonttools`.
- O `ffmpeg` também precisa estar instalado:
  - Windows: `winget install ffmpeg`;
  - Mac: `brew install ffmpeg`;
  - Linux: `apt-get install -y ffmpeg`.
- **Voz grátis (opção a):**
  - instale com `pip install kokoro-onnx`;
  - baixe `kokoro-v1.0.onnx` e `voices-v1.0.bin` das *releases* do repositório `thewh1teagle/kokoro-onnx` no GitHub para `videos/_kit/kokoro/`.

## 3. Roteiro (pule se for a opção c)

Siga `referencias/roteiro.md`.
- **Tamanho:** cerca de 2,5 palavras por segundo para a duração escolhida.
- **Gancho:** escreva 3 opções e escolha a mais forte.
- **Arquivos:** salve `roteiro.txt` (grafia correta, uma frase por linha) e `roteiro_voz.txt` (números e siglas como se fala).
- **Revisão:** revise como especialista e como espectador impaciente antes de mostrar.

Mostre o roteiro final num bloco de código, as 3 opções de gancho (marcando a escolhida) e a duração estimada. Depois:

- **Opção a:** gere a voz e siga direto:
  ```
  python3 videos/_kit/scripts/voz.py videos/<tema> [velocidade 1.0] [voz pm_alex]
  ```
  - Se ficar muito curto ou longo, ajuste o roteiro, nunca estique o áudio.
  - Vozes em português: `pm_alex` (masculina) e `pf_dora` (feminina).
- **Opção b ⏸ PARADA 2:** "Cola o texto abaixo no gerador de voz, baixa o mp3 e me manda aqui."
  - Mostre o `roteiro_voz.txt` num bloco de código.
  - Quando o mp3 chegar, salve em `videos/<tema>/voz.mp3` e converta:
    ```
    ffmpeg -i voz.mp3 -ar 48000 -ac 1 voz.wav
    ```
  - Se a pessoa mudou alguma frase ao gravar, atualize o `roteiro.txt` com o que ela falou de verdade.
- **Opção c:** salve o áudio como `voz.mp3` e converta para `voz.wav`.
  - Transcreva (passo 4) e escreva `roteiro.txt` a partir da transcrição, com a grafia corrigida e uma frase por linha.

## 4. Tempos da voz (legenda e sincronia)
```
cd videos/<tema>
python3 ../_kit/scripts/tempos.py .        # transcreve -> whisper.json
python3 ../_kit/scripts/align_ext.py .     # alinha com roteiro.txt -> tempos.json (frases e palavras com início/fim)
```
- Confira a lista de frases e os tempos que o script imprime.
- Para deixar a frase final na tela depois da voz, aumente `duration` no `tempos.json` em 2–3 s.
- **Duração exata** (anúncio, por exemplo): encurte as pausas com `silenceremove` e, se ainda faltar, acelere no máximo 5% com `atempo`. Depois refaça este passo.

## 5. Cena 3D
- Copie `modelos/scene_modelo.html` para `videos/<tema>/scene.html` e troque tudo que está marcado com ►: gancho, objeto ou personagens, tempos das palavras, planos, etiquetas, tags, cartão final e **marca d'água**.
- Siga `referencias/estilo.md`. O essencial:
  - um plano por frase, com corte seco;
  - cada peça ou momento entra na palavra exata;
  - "Mas…" mostra o problema;
  - o objeto fica na faixa do meio;
  - a câmera fica longe (`ZK`).
- Reaproveite cenas de vídeos anteriores da pasta `videos/` como base quando o formato for parecido.

## 6. Conferir (você mesmo, antes de mostrar)
```
NODE_PATH=$(npm root -g) node ../_kit/render.js . test 1,4,8,12,...    # uma imagem a cada 3–5 s -> teste/
python3 ../_kit/scripts/grid.py teste grade.jpg 6                     # junta numa grade
```
- Olhe a grade e corrija até ficar bom. Procure:
  - coisa fora do quadro;
  - câmera perto demais;
  - peça escondida;
  - texto em cima de texto;
  - personagem sumido;
  - algo que não dá pra entender o que é.
- Se a pessoa pediu pra ver antes, mostre a grade e pergunte "Posso renderizar?". Se não pediu, siga.

## 7. Render e montagem
```
NODE_PATH=$(npm root -g) node ../_kit/render.js . full 2    # quadros/ (continua de onde parou)
bash ../_kit/scripts/finalizar.sh .                        # efeitos + volume -14 LUFS + final.mp4
```
- **Avise antes:** quanto tempo deve levar (cerca de 0,4 s por quadro por processo) e que pode deixar rodando. Rode em segundo plano.
- **Trilha:** se quiser música, ponha um `musica.wav` na pasta antes de finalizar. Ela fica baixa e abaixa sozinha quando a voz fala.
- **Conferência:** depois, tire uns 10 quadros do `final.mp4` com ffmpeg e confira.

## 8. Capa e títulos
- **Capa:**
  ```
  NODE_PATH=$(npm root -g) node ../_kit/scripts/capa.js . <segundo> /tmp/quadro.png
  python3 ../_kit/scripts/capa.py /tmp/quadro.png capa.jpg "LINHA 1" "LINHA 2" "@MARCA"
  ```
  Escolha um segundo em que o objeto ou personagem esteja inteiro e bonito, e o texto da capa não cubra o principal.
- **`titulos.txt`:**
  - **títulos:** 3 opções e o texto da capa;
  - **por rede** (YouTube Shorts, TikTok, Instagram Reels, Facebook Reels e Kwai): título ou legenda e 4–7 hashtags;
  - **comentário para fixar.**
  - Não prometa visualizações nem ganhos.

## 9. Entregar
- Mande `final.mp4`, `capa.jpg` e `titulos.txt`.
- Explique em poucas linhas o que aparece em cada parte do vídeo.
- Se o projeto for um repositório git, faça commit da pasta do vídeo (o `.gitignore` deve ignorar `quadros/`, `teste/` e `*.wav`).
- Pergunte se quer mudar algo. Pedidos do tipo "aos 20 segundos a câmera está perto" se resolvem refazendo só os quadros daquele trecho.

## Regras que nunca mudam
- **Marca d'água** em todo vídeo e capa, discreta, sem cobrir o objeto nem a legenda.
- **Formato:** vertical 1080x1920, 3D low-poly colorido, legenda palavra por palavra em Poppins.
- **Conteúdo honesto:** nada de fato inventado, depoimento falso ou promessa de resultado. Conteúdo picante fica só sugerido.
- **Sem cópia:** não recrie personagens, marcas ou cenas de obras de terceiros. Crie personagens originais.
