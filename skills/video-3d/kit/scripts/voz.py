# voz grátis e offline com Kokoro. uso: python3 voz.py <pasta-do-video> [velocidade] [voz]
# precisa: pip install kokoro-onnx soundfile ; arquivos kokoro-v1.0.onnx e voices-v1.0.bin na pasta videos/_kit/kokoro/
import sys, os, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
d = sys.argv[1]; speed = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0; voice = sys.argv[3] if len(sys.argv) > 3 else 'pm_alex'
K = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'kokoro')
k = Kokoro(os.path.join(K, 'kokoro-v1.0.onnx'), os.path.join(K, 'voices-v1.0.bin'))
lines = [l for l in open(os.path.join(d, 'roteiro_voz.txt'), encoding='utf-8').read().split('\n') if l.strip()]
out = [np.zeros(int(24000 * .15), np.float32)]; sr = 24000
for l in lines:
    a, sr = k.create(l, voice=voice, speed=speed, lang='pt-br')
    thr = .01 * np.abs(a).max(); nz = np.where(np.abs(a) > thr)[0]; a = a[max(0, nz[0] - 240):nz[-1] + 480]
    out += [a.astype(np.float32), np.zeros(int(sr * .25), np.float32)]
out.append(np.zeros(int(sr * .6), np.float32)); y = np.concatenate(out)
sf.write(os.path.join(d, 'voz.wav'), y, sr); print('voz.wav pronta,', round(len(y) / sr, 1), 's')
