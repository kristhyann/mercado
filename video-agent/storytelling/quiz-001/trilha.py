"""Trilha motivacional original + efeitos (numpy) para o Reels Quiz 01.
Gera audio/trilha.wav (estéreo 44.1 kHz) com ducking sob a narração. A narração não é processada aqui."""
import numpy as np, subprocess, os, wave

SR = 44100
DUR = 88.0
N = int(SR * DUR)
rng = np.random.default_rng(21)
here = os.path.dirname(os.path.abspath(__file__))
L = np.zeros(N); R = np.zeros(N)

def add(sig, t, pan=0.0, gain=1.0):
    i = int(t * SR); n = min(len(sig), N - i)
    if n <= 0 or i < 0: return
    gl, gr = np.cos((pan + 1) * np.pi / 4) * 1.414, np.sin((pan + 1) * np.pi / 4) * 1.414
    L[i:i + n] += sig[:n] * gain * gl; R[i:i + n] += sig[:n] * gain * gr

hz = lambda m: 440 * 2 ** ((m - 69) / 12)
noise = lambda d: rng.standard_normal(int(d * SR))
def filt(x, lo=None, hi=None):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR); H = np.ones_like(f)
    if hi: H *= 1 / np.sqrt(1 + (f / hi) ** 4)
    if lo: H *= 1 - 1 / np.sqrt(1 + (f / lo) ** 4)
    return np.fft.irfft(X * H, len(x))
def tt(d): return np.arange(int(d * SR)) / SR

def pluck(m, d=0.35, v=1.0):
    t = tt(d + 0.4); f = hz(m)
    s = sum(a * np.sin(2 * np.pi * f * k * t) * np.exp(-t * (6 + 4 * k)) for k, a in [(1, 1), (2, 0.5), (3, 0.25), (4, 0.12)])
    return s * np.minimum(1, t / 0.003) * v * 0.2
def piano(m, d, v=1.0):
    t = tt(d + 1.2); f = hz(m)
    s = sum(a * np.sin(2 * np.pi * f * k * t) * np.exp(-t * (1.0 + k * 0.8)) for k, a in [(1, 1), (2, 0.45), (3, 0.2), (4, 0.08)])
    rel = np.ones(len(t)); c = int(d * SR); rel[c:] = np.exp(-(t[c:] - d) * 5)
    return s * rel * np.minimum(1, t / 0.004) * v * 0.22
def pad(notes, d, bright=0.4):
    t = tt(d); s = np.zeros(len(t))
    for m in notes:
        for det in (-0.1, 0, 0.1):
            f = hz(m) * 2 ** (det / 12); ph = rng.random() * 6.28
            s += np.sin(2 * np.pi * f * t + ph) + bright * 0.5 * np.sin(4 * np.pi * f * t + ph)
    e = np.ones(len(t)); a = min(len(t) // 3, int(0.3 * SR)); e[:a] = np.linspace(0, 1, a); e[-a:] *= np.linspace(1, 0, a)
    return s * e / (len(notes) * 3) * 0.5
def kick(g=1.0):
    t = tt(0.4); return np.sin(2 * np.pi * np.cumsum(50 + 110 * np.exp(-t * 35)) / SR) * np.exp(-t * 8) * 0.8 * g
def hat(g=1.0):
    t = tt(0.08); return filt(noise(0.08), lo=7000) * np.exp(-t * 60) * 0.12 * g
def snare(g=1.0):
    t = tt(0.25); return (filt(noise(0.25), lo=1500, hi=9000) * 0.6 + np.sin(2 * np.pi * 190 * t) * 0.4) * np.exp(-t * 16) * 0.45 * g
def bass(m, d, g=1.0):
    t = tt(d); f = hz(m)
    return (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t)) * np.exp(-t * 3) * np.minimum(1, t / 0.005) * 0.35 * g
def boom(g=1.0):
    t = tt(2.0)
    return (np.sin(2 * np.pi * np.cumsum(38 + 70 * np.exp(-t * 10)) / SR) * np.exp(-t * 2) * 0.9 + filt(noise(2.0), hi=3000) * np.exp(-t * 7) * 0.3) * g
def whoosh(d=0.4, g=0.3):
    return filt(noise(d), lo=400, hi=6000) * np.sin(np.linspace(0, np.pi, int(d * SR))) ** 2 * g
def riser(d, g=0.25):
    return filt(noise(d), lo=900, hi=8000) * np.linspace(0, 1, int(d * SR)) ** 2.5 * g

B = 0.5
Am, F, C, G, Dm, E = [57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62], [50, 53, 57], [52, 56, 59]
PROG = [Am, F, C, G]

def groove(t0, t1, g=1.0, plucks=True):
    bar = 0
    while t0 + bar * 4 * B < t1 - 0.1:
        tb = t0 + bar * 4 * B; ch = PROG[bar % 4]
        add(pad([n - 12 for n in ch] + ch, min(4 * B, t1 - tb) + 0.05, 0.3), tb, 0, 0.45 * g)
        for b in range(4):
            tk = tb + b * B
            if tk >= t1 - 0.05: break
            add(kick(0.7 * g), tk)
            if b % 2 == 1: add(snare(0.45 * g), tk, 0.1)
            add(bass(ch[0] - 24, B - 0.03, 0.8 * g), tk)
            add(hat(0.8 * g), tk + B / 2, 0.35)
            if plucks:
                for s8 in range(2): add(pluck((ch + [ch[0] + 12])[(b * 2 + s8) % 4] + 12, 0.15, 0.45 * g), tk + s8 * B / 2, 0.4 * np.sin(b + s8))
        bar += 1

def slam(t):
    add(boom(0.6), t); add(whoosh(0.35, 0.35), t - 0.3)

def countdown(t0):
    for k in range(5):
        tt0 = t0 + k
        s = tt(0.12); add((np.sin(2 * np.pi * (880 + k * 60) * s) * np.exp(-s * 40)) * 0.25, tt0, 0)
        add(filt(noise(0.04), lo=2500, hi=9000) * np.exp(-tt(0.04) * 100) * 0.5, tt0 + 0.5, 0.2)
        add(kick(0.5), tt0)
    add(pad([45, 52], 5.0, 0.1), t0, 0, 0.5)
    add(riser(1.2, 0.22), t0 + 3.8)

def correct(t):
    s = tt(1.4)
    for i, m in enumerate([72, 76, 79, 84]):
        add(np.sin(2 * np.pi * hz(m) * s) * np.exp(-s * 3) * 0.16, t + i * 0.06, (i - 1.5) * 0.3)
    add(filt(noise(1.0), lo=6000) * np.exp(-tt(1.0) * 4) * 0.08, t)

# intro
add(boom(0.8), 0.0); add(riser(1.2, 0.2), 2.3)
for k in range(7): add(hat(0.8), k * B / 2 + 0.5, 0.3)
add(pad([45, 52, 57], 3.7, 0.2), 0.0, 0, 0.6)
s = tt(0.4); add(np.sin(2 * np.pi * np.cumsum(300 + 400 * s) / SR) * np.exp(-s * 8) * 0.25, 2.5)  # "você cai?" pop
# question 1
slam(3.7)
groove(5.2, 29.85)
countdown(29.85)
add(boom(0.35), 34.85)
correct(36.52)
groove(37.4, 44.8, 0.8)
# question 2
slam(44.8)
groove(46.2, 64.65)
countdown(64.65)
add(boom(0.35), 69.65)
correct(71.26)
groove(72.2, 80.0, 0.8)
# outro
add(boom(0.7), 80.0)
add(pad([45, 57, 60, 64], 2.4, 0.5), 80.0, 0, 0.7)
add(boom(0.8), 82.46)
add(pad([36, 48, 52, 55, 60, 64], 2.9, 0.7), 82.46, 0, 0.85)
add(boom(0.6), 85.32)
add(pad([41, 53, 57, 60, 65, 72], 2.7, 0.8), 85.32, 0, 0.9)
for i, m in enumerate([65, 69, 72, 77]): add(piano(m, 2.0, 0.6), 85.32 + i * 0.08, (i - 1.5) * 0.3)
for tk in np.arange(82.46, 87.4, B):
    add(kick(0.8), tk); add(hat(), tk + B / 2, 0.3)
# scene sfx
add(filt(noise(0.3), lo=900, hi=6000) * np.sin(np.linspace(0, np.pi, int(0.3 * SR))) * 0.2, 10.3)   # column wobble rustle
s = tt(0.5); add(np.sin(2 * np.pi * 140 * s) * np.exp(-s * 10) * 0.25, 10.3)
add(filt(noise(0.3), lo=800, hi=5000) * np.sin(np.linspace(0, np.pi, int(0.3 * SR))) * 0.22, 48.4)  # envelope
for tA in (17.44, 21.5, 24.68, 26.52, 54.6, 57.2, 59.14, 61.68):  # alternatives pop in
    s = tt(0.08); add(np.sin(2 * np.pi * 620 * s) * np.exp(-s * 50) * 0.12, tA, 0.2)
add(whoosh(0.4, 0.25), 39.1)  # card flies to "objetivos"
add(boom(0.25), 73.4)          # pin drop

# ------------------------------------------------------------------ ducking + normalise
voice = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', os.path.join(here, 'audio/narracao-montada.wav'), '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout, dtype=np.float32).astype(np.float64)
v = np.zeros(N); v[:min(N, len(voice))] = np.abs(voice[:N])
w = int(0.1 * SR); env = np.convolve(v, np.ones(w) / w, 'same'); env /= env.max() + 1e-9
sm = np.convolve(np.clip(env * 6, 0, 1), np.ones(int(0.2 * SR)) / int(0.2 * SR), 'same')
duck = 1 - 0.45 * sm
L *= duck; R *= duck
fo = int(0.8 * SR); L[-fo:] *= np.linspace(1, 0, fo); R[-fo:] *= np.linspace(1, 0, fo)
mx = max(np.abs(L).max(), np.abs(R).max()); L /= mx; R /= mx
with wave.open(os.path.join(here, 'audio/trilha.wav'), 'wb') as f:
    f.setnchannels(2); f.setsampwidth(2); f.setframerate(SR)
    f.writeframes((np.clip(np.stack([L, R], 1), -1, 1) * 32000).astype(np.int16).tobytes())
print('ok')
