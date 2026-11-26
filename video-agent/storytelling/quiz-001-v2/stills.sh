#!/bin/bash
# usage: stills.sh frame1 frame2 ... -> scratchpad/st_<frame>.png and a montage
cd "$(dirname "$0")/remotion"
OUT=/tmp/claude-0/-home-user-mercado/f08a30ce-bff3-57e9-93b0-38f584516bfc/scratchpad/st4
mkdir -p $OUT
B=/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell
args=""
for f in "$@"; do npx remotion still src/index.jsx Video $OUT/$f.png --frame=$f --browser-executable=$B --scale=0.4 --log=error >/dev/null 2>&1 || echo "fail $f"; args="$args $OUT/$f.png"; done
ffmpeg -v error -y $(for f in "$@"; do echo -n "-i $OUT/$f.png "; done) -filter_complex "$(i=0; for f in "$@"; do echo -n "[$i:v]"; i=$((i+1)); done)hstack=inputs=$#" $OUT/montage.png 2>/dev/null || cp $OUT/$1.png $OUT/montage.png
echo $OUT/montage.png
