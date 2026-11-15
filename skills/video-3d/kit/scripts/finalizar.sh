#!/usr/bin/env bash
# uso: bash finalizar.sh <pasta-do-video>   (efeitos + volume padrão -14 LUFS + junta imagem e som em final.mp4)
set -e; cd "$1"; K="$(cd "$(dirname "$0")" && pwd)"
python3 "$K/sfx.py" .
if [ -f musica.wav ]; then
  ffmpeg -loglevel error -y -i mix_bruta.wav -i musica.wav -filter_complex "[1:a]volume=0.3,aresample=48000[m];[m][0:a]sidechaincompress=threshold=0.04:ratio=5:attack=15:release=250[md];[0:a][md]amix=inputs=2:normalize=0:duration=first" mix2.wav && mv mix2.wav mix_bruta.wav
fi
ffmpeg -loglevel error -y -i mix_bruta.wav -af "acompressor=threshold=-18dB:ratio=3:attack=5:release=120,alimiter=limit=0.9,loudnorm=I=-14:TP=-1.5:LRA=11" -ar 48000 audio.wav
ffmpeg -loglevel error -y -framerate 30 -i quadros/f_%05d.jpg -i audio.wav -c:v libx264 -preset medium -crf 19 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart final.mp4
echo "final.mp4: $(ffprobe -v error -show_entries format=duration -of csv=p=0 final.mp4) s"
