# Padrão visual e de qualidade

## 1. Identidade visual
- Animação 2D ilustrada, cartoon cinematográfico, aparência de graphic novel.
- Contorno desenhado (traço escuro, espessura levemente variável), sombras ilustradas em blocos (cel shading) com uma segunda sombra suave, luz de recorte (rim light) nos personagens.
- Iluminação dramática com direção de luz coerente por cenário (janela, poste, tela de celular, pôr do sol).
- Paleta definida por história (3 a 5 cores principais + neutros) e por momento emocional (frio/dessaturado no problema, quente no desfecho). Registrar na ficha do projeto.
- Textura discreta: grão de papel/ruído leve e retícula (halftone) sutil nas sombras. Nunca dominante.
- Composição cinematográfica: regra dos terços, primeiro plano/plano médio/fundo, planos variados (geral, médio, close, detalhe, sobre o ombro, plongée/contra-plongée).
- O mesmo estilo em todas as cenas: mesma espessura de traço, mesmo tipo de sombra, mesma textura.

## 2. Consistência de personagens
- Ficha visual antes de qualquer cena (modelo em `modelos.md`): idade, rosto, cabelo, roupas e cores (hex), traços marcantes, proporções (altura em cabeças), expressões, personalidade visual.
- Cada personagem é um único componente/rig reutilizado; cenas só mudam pose, expressão e ângulo, nunca rosto, cabelo, roupa, proporção ou cor.
- Troca de roupa só se o roteiro pedir (ex.: dia seguinte) e registrada na ficha como variante.
- Séries: fichas e componentes ficam em `_biblioteca/` e são importados, não redesenhados.

## 3. Cenários
- Detalhados e com propósito: cada objeto ambienta ou conta a história (relógio marcando a hora citada, celular com notificação, contas na mesa, chuva na janela).
- Construídos em camadas de profundidade (fundo distante, meio, primeiro plano, elementos à frente da câmera) para parallax real.
- Ficha por cenário: hora do dia, fonte de luz, paleta, objetos-chave e o que cada um comunica.
- Mesmo cenário reaparecendo = mesmos objetos nos mesmos lugares (continuidade).

## 4. Movimento
Variar e justificar. Repertório:
- Câmera: dolly-in/out, pan, tilt, travelling lateral, push lento de tensão, câmera na mão sutil em momentos tensos, whip-pan em transições, rack focus (desfoque de camada).
- Parallax por camadas em todo plano com cenário.
- Personagem: respiração (idle), piscar, olhos que seguem a ação, inclinação/giro de cabeça, braços e mãos gesticulando, boca sincronizada com fala de personagem quando houver, troca de expressão no tempo da emoção, squash & stretch leve.
- Objetos: tela que acende, ponteiro do relógio, porta, papel caindo, vapor do café, carros passando.
- Ambiente: chuva, poeira, fumaça, folhas, faíscas, feixes de luz, sombras que deslizam, luz piscando, flare.
- Regras: nunca o mesmo movimento em duas cenas seguidas; easing suave (sem início/fim seco); pausas da narração = câmera assenta ou plano de respiro.

## 5. Narrativa
Gancho no 1º segundo → contexto → problema → desenvolvimento → conflito/surpresa → conclusão → CTA (se fizer sentido). Frases curtas, fáceis de seguir; continuidade de causa e efeito entre as cenas.

## 6. Cenas
Cada cena: número, início/fim e duração (do áudio real), descrição visual, personagem, cenário, ação, câmera, efeitos, transição, trecho da narração. Transições motivadas (match cut, objeto que passa na frente, luz que estoura, wipe por elemento do cenário, dissolve em mudança de tempo). Sem cortes secos sem motivo.

## 7. Narração
Base da montagem. Não alterar, cortar, acelerar nem reordenar o áudio. Cenas se ajustam à duração real.

## 8. Textos na tela
Só quando agregam: horários, datas, valores, nomes, alertas, palavras-chave. Curtos (até ~4 palavras), grandes, legíveis, dentro da área segura (vertical: longe dos 250 px de baixo e da faixa direita de ícones). Preferir texto diegético (no celular, no relógio, num papel). Ortografia conferida (acentos!). Legenda completa da narração só se o usuário pedir.

## 9. Som
Música de fundo de acordo com a emoção, ducking sob a voz (voz sempre clara, música ~ -20 dB abaixo), efeitos sonoros discretos em ações-chave (porta, notificação, chuva, whoosh de transição). Volume final em torno de -14 LUFS.

## Revisão (checklist antes de entregar)
- [ ] Todas as cenas presentes, na ordem, cobrindo 100% do áudio, sem frames vazios.
- [ ] Continuidade: objetos, luz e posições coerentes entre cenas.
- [ ] Personagens idênticos à ficha em todas as cenas.
- [ ] Ações sincronizadas com as palavras (±3 frames).
- [ ] Áudio da narração intacto (mesma duração do arquivo enviado), música abaixo da voz, sem clipping.
- [ ] Ritmo: nenhuma cena parada demais nem corrida; pausas aproveitadas.
- [ ] Movimentos variados; nenhuma repetição consecutiva.
- [ ] Sem deformações, elementos aleatórios, recortes visíveis ou camadas vazando na borda durante o movimento de câmera.
- [ ] Textos legíveis, na área segura, ortografia correta.
- [ ] Exportação: resolução, fps, codec H.264 + AAC, duração = áudio, arquivo abre e toca.
