# Canal olhaso_3D — regras dos vídeos

- **Marca d'água obrigatória:** todo vídeo (e capa) leva `@olhaso_3D` visível, discreto, sem cobrir o objeto nem a legenda.
- **Exceção — vídeos de QUIZ:** vão para o perfil **Mente Pega**, então a marca d'água (vídeo, capa e CTA) é `@mentepega`, não `@olhaso_3D`. Foto de perfil/mascote em `perfil/mente-pega/`.

## Quiz (perfil Mente Pega) — princípios fixos
Quiz prende porque o espectador participa: pensa na resposta, quer saber se acertou e comenta a pontuação → retenção, replays e comentários. O visual 3D (cenário, cronômetro animado, cartas girando) diferencia dos quizzes de slide.
- **Formato fixo e reconhecível:** mesma estrutura, mesmo cronômetro, mesmas cores de resposta (acerto verde, erro vermelho), mesmo layout (contador "Pergunta X/10", cartão da pergunta, A–D). Base: `videos/quiz-adulto-01/scene.html`.
- **Fundo/cenário DIFERENTE a cada quiz:** trocar a paleta do palco, das luzes neon e do fundo em todo vídeo novo, para nenhum ficar igual ao anterior. Usar cores vibrantes e atraentes (alto contraste, saturadas, degradês), sem usar verde puro nem vermelho puro no fundo para não confundir com acerto/erro. Registrar a paleta usada abaixo e não repetir a do vídeo anterior.
  - Paletas sugeridas: 1) roxo + rosa neon · 2) azul elétrico + ciano · 3) laranja pôr do sol + magenta · 4) turquesa + coral · 5) azul-marinho + dourado · 6) lilás + azul-bebê (pastel vibrante) · 7) índigo + amarelo limão · 8) pink + laranja (candy).
  - Usadas: `quiz-adulto-01` = 1 (roxo + rosa neon) · `quiz-escola-01` = 1 (roxo + rosa neon) · `quiz-parnaiba-01` = 3 (laranja pôr do sol + magenta; página Nostalgia Parnaíba, marca "Nostalgia Parnaíba").
- **Pausa para pensar:** toda pergunta tem **5 s de cronômetro** (contagem 5-4-3-2-1 com tique-taque), sem narração durante a pausa. No roteiro de voz a regra é "Você tem cinco segundos pra cada pergunta".
- **Dificuldade crescente:** começa fácil e termina difícil; a última pode ser pegadinha que gere discussão.
- **Chamada final:** "Quantas você acertou? Comenta aí!" + Segue @mentepega + corte que emenda no começo (loop).
- **Séries:** tema que performar vira Parte 2, Parte 3… (manter numeração no título e na pasta, ex.: `quiz-adulto-02`).
- Conferir todas as respostas antes de produzir e mostrar o roteiro com tempos.
- **CTA obrigatório em TODO vídeo:** pedir para **seguir** (com o @ do perfil) **e comentar** (com uma pergunta que puxe resposta), no mínimo no cartão final.
- A pessoa gera a voz em outra plataforma (ElevenLabs). Entregar só o roteiro em texto (`roteiro_voz.txt`) e esperar o mp3; depois montar o vídeo em cima do áudio dela.
- Formato padrão: vertical 1080x1920, 3D low-poly colorido, legenda palavra por palavra (Poppins), estilo "construa do zero" (skill `construa-do-zero`).
- Kit reutilizável em `videos/_kit/` (render.js, kit.js, pessoas.js, scripts/).
- Estratégia de conteúdo e séries: ver `estrategia/README.md` (pilares, séries de 3 partes, formato de entrega).
- Antes de renderizar o vídeo completo, SEMPRE gerar quadros de teste de todas as cenas e conferir falhas de imagem (objetos cortados, câmera dentro de objetos, textos sobrepostos, peças sumindo, telas escuras). Só renderizar depois de corrigir.
