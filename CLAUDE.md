# Canal olhaso_3D — regras dos vídeos

- **Marca d'água obrigatória:** todo vídeo (e capa) leva `@olhaso_3D` visível, discreto, sem cobrir o objeto nem a legenda.
- **Exceção — vídeos de QUIZ:** vão para o perfil **Mente Pega**, então a marca d'água (vídeo, capa e CTA) é `@mentepega`, não `@olhaso_3D`. Foto de perfil/mascote em `perfil/mente-pega/`.

## Quiz (perfil Mente Pega) — princípios fixos
Quiz prende porque o espectador participa: pensa na resposta, quer saber se acertou e comenta a pontuação → retenção, replays e comentários. O visual 3D (cenário, cronômetro animado, cartas girando) diferencia dos quizzes de slide.
- **Formato fixo e reconhecível:** mesma vinheta, mesmo cronômetro, mesmas cores (acerto verde, erro vermelho). Base: `videos/quiz-adulto-01/scene.html` (palco neon roxo, cubo "?", cronômetro 3D, contador "Pergunta X/10").
- **Pausa para pensar:** toda pergunta tem 3 s de cronômetro (5 s nos desafios visuais), sem narração durante a pausa.
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
