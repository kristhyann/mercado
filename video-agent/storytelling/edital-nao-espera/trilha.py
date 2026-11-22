"""Trilha motivacional original + efeitos (numpy) para o Reels 'O edital não vai esperar'.
Gera audio/trilha.wav (estéreo 44.1 kHz) com ducking sob a narração. A narração não é processada aqui."""
import numpy as np, subprocess, os, wave

SR = 44100
DUR = 29.4
N = int(SR * DUR)
rng = np.random.default_rng(11)
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

B = 0.5  # beat (120 bpm)
Am, F, C, G = [57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]
PROG = [Am, F, C, G]

# 0 - 3.75 hook: impact, drone, ticking hats, riser
add(boom(0.8), 0.0)
add(pad([45, 52, 57], 3.9, 0.2), 0.0, 0, 0.7)
for k in range(int(3.7 / (B / 2))): add(hat(0.7 + 0.3 * (k % 2 == 0)), k * B / 2, 0.3)
add(riser(1.6, 0.22), 2.15)

# 3.75 - 12.85 drive
t0 = 3.75
bar = 0
while t0 + bar * 2 * B * 2 < 12.85:
    tb = t0 + bar * 4 * B; ch = PROG[bar % 4]
    add(pad([n - 12 for n in ch] + ch, 4 * B + 0.1, 0.35), tb, 0, 0.55)
    for b in range(4):
        tk = tb + b * B
        if tk >= 12.85: break
        add(kick(), tk)
        if b % 2 == 1: add(snare(0.7), tk, 0.1)
        for e in range(2):
            add(bass(ch[0] - 24, B / 2 - 0.02), tk + e * B / 2)
            add(hat(), tk + e * B / 2 + B / 4, 0.35)
        for s16 in range(4):
            add(pluck((ch + [ch[0] + 12])[(b * 4 + s16) % 4] + 12, 0.15, 0.6), tk + s16 * B / 4, 0.4 * np.sin(b + s16))
    bar += 1
add(riser(0.8, 0.2), 12.05)

# 12.85 - 16.75 breakdown: pad, clock ticks accelerating
add(pad([45, 57, 60, 64], 4.0, 0.15), 12.85, 0, 0.7)
add(piano(69, 1.5, 0.6), 12.95); add(piano(72, 1.5, 0.5), 13.9)
tick_t = 14.45
while tick_t < 16.7:
    p = (tick_t - 14.45) / 2.3
    add(filt(noise(0.03), lo=2000, hi=9000) * np.exp(-tt(0.03) * 120) * 0.6, tick_t, 0.2 if int(tick_t * 10) % 2 else -0.2)
    tick_t += 0.4 - 0.25 * p
add(riser(1.3, 0.3), 15.45)
add(whoosh(0.4, 0.35), 16.6)

# 16.75 - 22.2 build back
t0 = 16.75
for bar in range(3):
    tb = t0 + bar * 4 * B; ch = [F, G, Am][bar]
    if tb >= 22.2: break
    add(pad([n - 12 for n in ch] + ch + [ch[2] + 12], 4 * B + 0.1, 0.5), tb, 0, 0.6)
    for b in range(4):
        tk = tb + b * B
        if tk >= 22.25: break
        add(kick(), tk)
        if b % 2 == 1: add(snare(0.8), tk)
        for e in range(2): add(bass(ch[0] - 24, B / 2 - 0.02), tk + e * B / 2); add(hat(1.1), tk + e * B / 2 + B / 4, 0.3)
        for s16 in range(4): add(pluck((ch + [ch[0] + 12])[(b * 4 + s16) % 4] + 12, 0.15, 0.7), tk + s16 * B / 4, 0.4 * np.cos(b + s16))
# snare roll into the drop
rt = 21.25
while rt < 22.3:
    add(snare(0.25 + 0.6 * (rt - 21.25)), rt); rt += 0.25 if rt < 21.75 else 0.125
add(riser(1.2, 0.3), 21.1)

# 22.3 - 29.4 drop / end card
add(boom(1.0), 22.34)
add(pad([36, 48, 52, 55, 60, 64], 1.6, 0.7), 22.34, 0, 0.85)
add(pad([43, 55, 59, 62, 67], 1.6, 0.7), 23.92, 0, 0.85)
add(boom(0.7), 23.92)
add(pad([45, 57, 60, 64, 69], 1.75, 0.7), 25.55, 0, 0.8)
add(pad([41, 53, 57, 60, 65, 72], 4.0, 0.8), 27.3, 0, 0.9)
for i, m in enumerate([60, 64, 67, 72]): add(piano(m, 2.5, 0.6), 22.34 + i * 0.08, (i - 1.5) * 0.3)
for i, m in enumerate([65, 69, 72, 77]): add(piano(m, 2.0, 0.6), 27.3 + i * 0.08, (i - 1.5) * 0.3)
for tk in np.arange(22.34, 27.2, B):
    add(kick(0.9), tk)
    if int(round((tk - 22.34) / B)) % 2 == 1: add(snare(0.7), tk)
    add(hat(), tk + B / 2, 0.3)
add(filt(noise(3.0), lo=5000) * np.exp(-tt(3.0) * 1.3) * 0.1, 27.3)

# ------------------------------------------------------------------ SFX
t = tt(1.0); add((np.sin(2 * np.pi * 1318.5 * t) + 0.5 * np.sin(2 * np.pi * 1975.5 * t)) * np.exp(-t * 5) * 0.2, 0.18, 0.2)
t = tt(0.55); add(np.sin(2 * np.pi * 165 * t) * (np.sin(2 * np.pi * 7 * t) > -0.2) * 0.2, 0.15)
for c in (3.73, 8.45, 12.82, 16.72): add(whoosh(0.4, 0.3), c - 0.15, 0.2)
for hb in np.arange(3.85, 6.3, 0.62):  # heartbeat
    t = tt(0.3); s = np.sin(2 * np.pi * 55 * t) * np.exp(-t * 18) * 0.6
    add(s, hb); add(s * 0.7, hb + 0.17)
add(filt(noise(0.3), lo=900, hi=6000) * np.sin(np.linspace(0, np.pi, int(0.3 * SR))) * 0.25, 6.38, -0.2)  # page
t = tt(0.25); add(np.sin(2 * np.pi * np.cumsum(900 - 600 * t) / SR) * np.exp(-t * 20) * 0.2, 7.65)  # drop plop
add(filt(noise(0.22), lo=800, hi=5000) * np.sin(np.linspace(0, np.pi, int(0.22 * SR))) * 0.22, 9.46)
add(filt(noise(0.4), lo=3000, hi=10000) * 0.07, 9.82, 0.1)
for p in (0.12, 0.34, 0.56, 0.78): add(filt(noise(0.1), lo=2500, hi=9000) * np.exp(-tt(0.1) * 30) * 0.3, 10.24 + p, 0.2)
for st in np.arange(11.45, 12.85, np.pi / 9.2): add(filt(noise(0.1), hi=900) * np.exp(-tt(0.1) * 35) * 0.4, st)
for i in range(6): add(whoosh(0.35, 0.18), 16.9 + i * 0.42, (i % 2 - 0.5))
add(filt(noise(1.0), lo=5000, hi=15000) * np.exp(-tt(1.0) * 3) * 0.12, 19.5)
add(filt(noise(1.0), lo=5000, hi=15000) * np.exp(-tt(1.0) * 3) * 0.12, 22.15)

# ------------------------------------------------------------------ ducking + normalise
voice = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', os.path.join(here, 'audio/narracao.mp3'), '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout, dtype=np.float32).astype(np.float64)
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
