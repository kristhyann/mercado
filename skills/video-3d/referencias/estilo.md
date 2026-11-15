# Estilo visual e lições aprendidas

## Padrão
- **Formato:** vertical 1080x1920, 30 fps, 3D low-poly colorido (`flatShading`), sol com sombra e céu em degradê.
- **Fonte:** Poppins 900 com contorno preto grosso.
- **Posição dos textos na tela (em pixels):**
  - marca d'água no canto de cima, à esquerda (y≈70, discreta, sempre visível);
  - gancho (y≈200);
  - etiqueta da peça (y≈180);
  - tags e balões (y≈560–620);
  - **legenda palavra por palavra (y≈1300)**;
  - cartão final (y≈1330).
- **Objeto:** sempre na faixa do meio (de 25% a 60% da altura). Nunca embaixo da legenda nem atrás de texto.
- **Cortes:** troque de plano (corte seco) a cada frase, mais ou menos a cada 3 s. Dentro do plano, a câmera anda devagar.
- **Sincronia:** cada peça ou momento entra **na palavra exata** em que a voz fala dela, usando `WD(frase, /palavra/)`.
- **"Mas…":** mostre o problema na tela, com X vermelho ou tag vermelha.
- **Etiqueta da peça:** nome em CAIXA ALTA no topo, até a próxima peça. Comece só depois do gancho, nunca junto com ele.
- **Tags:** no máximo uns 24 caracteres com 60 px, senão cortam. Uma por vez.
- **Sons** (`sfx.py`): pop quando a peça entra, whoosh nos cortes, ding na etiqueta, buzz no "Mas…", win no "Parabéns". Nada de ruído contínuo.

## Lições (erros que já aconteceram)
1. **Vídeo vertical precisa de câmera longe.** Use `ZK` de 1,4 a 1,8 e confira nos testes. "Muito perto" foi o erro mais comum.
2. **Confira cada imagem de teste procurando:**
   - peça escondida (atrás de tronco, de tela solta na frente da câmera, do mascote);
   - algo fora do quadro;
   - texto cobrindo texto;
   - personagem sumido.
3. **`mesh(geo, mat, x, y, z, parent)` só entra na cena se tiver `parent`.** Use `box(...)` ou passe `scene`.
4. **Emoji em texto HTML pode não aparecer.** Para coração e outros ícones, use SVG ou geometria 3D.
5. **mp4 não toca direto no render.** Extraia quadros com ffmpeg (`fps=30,scale=432:768`) para `clips/<nome>/f_%04d.jpg` e use como textura. O `draw` pode ser `async` e esperar a imagem carregar.
6. **Texto desenhado em canvas** (telas, chips, cartazes): carregue a fonte antes (`await document.fonts.load('900 60px P')`).
7. **Close de rosto:** pegue a posição real da cabeça com `getWorldPosition` depois de posar o personagem.
8. **Tempo de render:** cerca de 0,4 s por quadro por processo. 60 s levam uns 10–15 min com 2 processos. O render continua de onde parou: para refazer um trecho, apague só esses quadros e rode de novo.
9. **Duração:** a duração do `tempos.json` precisa ser ≥ a do `voz.wav`. Para deixar a frase final na tela, aumente `duration` em 2–3 s.
10. **Conteúdo adulto:** só sugerido (moita balançando, corações), nunca mostrado.

## Peças prontas do kit
- **`kit.js`:**
  - materiais e malhas: `M(cor)` (material low-poly), `mesh`;
  - animação: `pop(t,dur)` (entrada com salto), `ease`, `easeOut`, `clamp`, `lerp`, `rnd`, `rr`;
  - personagem: `buildMonkey()` com `POSES` e `applyPose` (macaco);
  - cenário: `buildWorld(scene)` (céu, chão e árvores).
- **`pessoas.js`:**
  - criar: `buildPerson({skin, shirt, pants, hair, hairStyle:'short'|'bun'|'bald'})`;
  - poses: `PP` (stand, sit, sitSlump, think, cheer, point, lie…), aplicadas com `poseP(p, P, walk, t)` e misturadas com `mixP`;
  - rosto: `face(p, 'happy'|'sad'|'shock'|'talk'|'angry'|'calm', t)`.
- **Animais e objetos:** monte com esferas, cilindros e caixas low-poly. Olhos grandes brancos com pupila preta deixam o personagem fofo e expressivo.
