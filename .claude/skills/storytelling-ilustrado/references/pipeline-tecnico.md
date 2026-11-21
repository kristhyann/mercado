# Pipeline técnico

Verifique o ambiente antes de cada projeto (`node -v`, `ffmpeg -version`, `codex --version`, chaves no ambiente). Não invente APIs. O Remotion sozinho não desenha ilustração: ele anima e compõe o que for desenhado/gerado.

## Ferramentas verificadas (nuvem Linux, 2026-11)
- Node 22, ffmpeg/ffprobe, Python 3 com numpy e Pillow.
- Remotion 4.0.545 via npm (`remotion`, `@remotion/cli`, `react@18.3.1`). Render testado em 1080x1920 30 fps.
- Navegador para o Remotion: passar `--browser-executable=/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell` (o download automático do Remotion falha aqui). Em outra máquina, confirme o caminho com `ls /opt/pw-browsers` ou deixe o Remotion baixar.
- Sem gerador de imagem por padrão: o Codex (`codex-images`) só funciona se o usuário instalar e fizer `codex login` com o plano ChatGPT. Nenhuma chave de API de imagem/vídeo no ambiente.

## Fontes da arte (escolher por projeto e registrar no storyboard)
1. **Vetorial desenhada em código (padrão, sempre disponível)** — personagens e cenários em SVG/React com contorno, cel shading, rim light, retícula e grão por filtros SVG. Personagem = rig de recorte (cabeça, olhos, pálpebras, sobrancelhas, boca com visemas, tronco, braço/antebraço/mão, pernas) com pivôs nas articulações → animação real de membros, cabeça, olhos e piscar, e consistência garantida (um componente só).
2. **Ilustração gerada (opcional)** — com `codex-images`, gerar placas de cenário em camadas separadas (fundo, meio, frente) no mesmo prompt-base de estilo; personagens gerados só com folha de referência e checagem de consistência quadro a quadro. Reprovar e regenerar imagens deformadas.
3. **Arte do usuário** — imagens enviadas, separadas em camadas (máscaras) para parallax.
Pode-se misturar: cenário gerado + personagem vetorial rigado, desde que traço, luz e paleta combinem.

## Estrutura do projeto
```
video-agent/storytelling/<slug>/
  roteiro.md  audio/narracao.mp3  analise.json  storyboard.md
  personagens/*.md  cenarios/*.md
  remotion/  (package.json, src/: Root, cenas/, rigs/, cenarios/, fx/, timing.json)
  render/<slug>.mp4  render/contact-sheet.png
video-agent/storytelling/_biblioteca/   (rigs e fichas reutilizados entre episódios)
```
`video-agent/storytelling/*/remotion/node_modules` não é versionado.

## Análise do áudio (etapa 3)
```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 audio/narracao.mp3
ffmpeg -i audio/narracao.mp3 -af silencedetect=noise=-35dB:d=0.35 -f null - 2>&1 | grep silence_
```
Tempos por palavra: whisper.cpp (instalado pelo `short-editing/engine/setup.mjs` em macOS/Windows; no Linux compilar ou usar o binário em `WHISPER_CLI`) ou a API do ElevenLabs se o usuário tiver chave. Sem transcrição disponível: alinhar frases pelo roteiro + silêncios detectados e conferir ouvindo trechos. Salvar em `analise.json` (duração, pausas, frases com início/fim).

## Animação no Remotion
- Uma `<Sequence>` por cena, frames vindos de `timing.json` (gerado da análise), nunca digitados à mão.
- `<Audio src={staticFile('narracao.mp3')} />` uma vez, sem cortes; duração da composição = duração do áudio (arredondada para cima).
- Câmera: componente que aplica scale/translate/rotate com `interpolate` + `Easing` ao grupo da cena; camadas com fator de profundidade para parallax.
- Personagem: props de pose/expressão por keyframes; `idle` (respiração, piscar com `random()` determinístico) sempre ligado.
- FX: chuva, poeira, fumaça, partículas e luz em componentes próprios, determinísticos (`random(seed)`), nunca `Math.random()`.
- Transições: `@remotion/transitions` (mesma versão do Remotion) ou máscaras/objetos passando na frente.

## Som (etapa 9)
Música/sfx só com fonte livre de direitos (biblioteca do usuário, `short-editing/assets/music` se existir, ou síntese). Mixagem final com ffmpeg: voz intacta, música com sidechain/ducking, `loudnorm=I=-14:TP=-1.5`.

## Render e revisão (etapa 10)
```bash
npx remotion render src/index.jsx <Comp> ../render/<slug>.mp4 --browser-executable=<caminho> --codec=h264
ffprobe ... (duração = áudio, 1080x1920, 30 fps, h264/aac)
ffmpeg -i render/<slug>.mp4 -vf "fps=1/2,scale=270:-1,tile=6x5" -frames:v 1 render/contact-sheet.png
```
Olhar a folha de quadros e quadros-chave de cada cena (Read na imagem) e passar o checklist de `padrao-visual.md`.
