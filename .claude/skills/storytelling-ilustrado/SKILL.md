---
name: storytelling-ilustrado
description: Cria e produz vídeos de storytelling ilustrado no estilo animação 2D / cartoon cinematográfico / graphic novel (personagens expressivos e consistentes, cenários detalhados, câmera em movimento, parallax, partículas, luz e sombra animadas), sempre a partir do áudio de narração que o usuário gera no ElevenLabs. Use quando o usuário pedir um vídeo de storytelling, história ilustrada, história animada, vídeo narrativo em cartoon, "vídeo nesse estilo", um novo episódio de uma série ilustrada, ou enviar o áudio de um roteiro deste formato.
argument-hint: "<tema ou briefing> | <áudio .mp3/.wav> [slug]"
---

# Storytelling Ilustrado

Vídeos narrativos que parecem pequenas animações 2D cinematográficas, não slides. Fale com o usuário em português.

Leia antes de qualquer etapa:
- `references/padrao-visual.md` — identidade visual, consistência, cenários, movimento, textos, qualidade (o padrão do usuário, obrigatório).
- `references/pipeline-tecnico.md` — ferramentas reais do ambiente e como gerar, animar, compor e renderizar.
- `references/modelos.md` — modelos da ficha de personagem, da ficha de cenário e do storyboard por cena.

Pasta do projeto: `video-agent/storytelling/<slug>/` (roteiro, áudio, fichas, storyboard, código Remotion, render). Personagens e cenários de série ficam em `video-agent/storytelling/_biblioteca/` e são reutilizados entre episódios sem alteração.

## Fluxo obrigatório (nunca pule nem inverta)

1. **Roteiro** — entregue só o texto da narração, sem instrução visual misturada. Estrutura: gancho (o 1º segundo desperta curiosidade, sem introdução), contexto, problema, desenvolvimento, conflito ou surpresa, conclusão, CTA quando fizer sentido. Salve em `roteiro.md`. Informe a duração estimada (≈150 palavras/min).
2. **Pare e aguarde o áudio** do ElevenLabs. Não produza storyboard final, imagens finais nem render antes disso. (Pode adiantar, se o usuário pedir, as fichas de personagem.)
3. **Análise do áudio** — duração exata (`ffprobe`), pausas (`silencedetect`), tempos por palavra/frase (transcrição local). Nunca corte, acelere ou edite o áudio: ele é a base da montagem.
4. **Divisão em cenas** pelo tempo real e pela narrativa; pausas viram respiros cinematográficos (plano de reação, câmera que assenta, ambiente).
5. **Storyboard** — fichas de personagem e de cenário primeiro, depois cada cena com número, início/fim, duração, descrição visual, personagem, cenário, ação, câmera, efeitos, transição e trecho da narração. Salve `storyboard.md` e mostre ao usuário. Siga em frente sem esperar aprovação, a menos que ele peça para revisar antes.
6. **Elementos visuais** — personagens como componentes únicos reutilizáveis (mesmo rosto, cabelo, roupa, cores e proporções em todas as cenas) e cenários em camadas para parallax.
7. **Animação** — câmera variada, membros, cabeça, olhos, boca, objetos, partículas, luz. Nada de zoom automático igual em toda cena.
8. **Sincronização** — cada ação no frame da palavra que a motiva (tempos da etapa 3).
9. **Finalização** — música e efeitos sonoros discretos quando apropriados, sempre abaixo da voz; voz intacta.
10. **Render e revisão** — renderize, extraia uma folha de quadros (contact sheet) e confira cada item do checklist em `padrao-visual.md` §Revisão. Corrija e renderize de novo até passar. Entregue o MP4 (e diga o caminho), nunca só código.

Se o usuário não enviou uma imagem de referência de estilo, siga a descrição de `padrao-visual.md`; se enviar, use-a como inspiração de estilo (traço, paleta, luz), nunca para copiar.

## Formato

Padrão vertical 1080x1920 30 fps (Shorts/Reels/TikTok). 16:9 1920x1080 se o usuário pedir. Pergunte só se o pedido não deixar claro e não houver projeto anterior.
