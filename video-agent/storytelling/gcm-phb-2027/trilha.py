"""Trilha original e efeitos sonoros sintetizados (numpy), sincronizados com a narração.
Gera audio/trilha.wav (música + sfx, estéreo 44.1 kHz). A narração NÃO é processada aqui."""
import numpy as np, subprocess, sys, os

SR = 44100
DUR = 57.0
N = int(SR * DUR)
rng = np.random.default_rng(7)
here = os.path.dirname(os.path.abspath(__file__))
L = np.zeros(N); R = np.zeros(N)

def add(sig, t, pan=0.0, gain=1.0):
    i = int(t * SR); n = min(len(sig), N - i)
    if n <= 0: return
    gl, gr = np.cos((pan + 1) * np.pi / 4) * 1.414, np.sin((pan + 1) * np.pi / 4) * 1.414
    L[i:i + n] += sig[:n] * gain * gl; R[i:i + n] += sig[:n] * gain * gr

def hz(note):  # midi -> Hz
    return 440 * 2 ** ((note - 69) / 12)

def env_adsr(n, a, d, s, r):
    e = np.ones(n) * s
    na, nd, nr = int(a * SR), int(d * SR), int(r * SR)
    na = min(na, n); e[:na] = np.linspace(0, 1, na)
    nd = min(nd, n - na); e[na:na + nd] = np.linspace(1, s, nd)
    if nr < n: e[-nr:] *= np.linspace(1, 0, nr)
    return e

def lowpass(x, fc):
    a = np.exp(-2 * np.pi * fc / SR); y = np.zeros_like(x); acc = 0.0
    for i in range(len(x)):
        acc = (1 - a) * x[i] + a * acc; y[i] = acc
    return y

def lp_fast(x, fc, order=2):
    # one-pole IIR via scipy-less vectorised trick: use FFT filter
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR)
    H = 1 / (1 + (f / fc) ** (2 * order)) ** 0.5
    return np.fft.irfft(X * H, len(x))

def bp_fast(x, lo, hi):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR)
    H = (1 / (1 + (f / hi) ** 4) ** 0.5) * (1 - 1 / (1 + (f / lo) ** 4) ** 0.5)
    return np.fft.irfft(X * H, len(x))

def piano(note, dur, vel=1.0):
    n = int((dur + 1.5) * SR); t = np.arange(n) / SR; f = hz(note)
    s = sum(a * np.sin(2 * np.pi * f * k * t * (1 + 0.0004 * k * k)) * np.exp(-t * (1.2 + k * 0.9)) for k, a in [(1, 1), (2, 0.45), (3, 0.22), (4, 0.1), (5, 0.05)])
    s *= np.minimum(1, t / 0.004)
    rel = np.ones(n); cut = int(dur * SR)
    if cut < n: rel[cut:] = np.exp(-(t[cut:] - dur) * 6)
    return s * rel * vel * 0.22

def pad(notes, dur, bright=0.3):
    n = int(dur * SR); t = np.arange(n) / SR; s = np.zeros(n)
    for nt in notes:
        for det in (-0.12, 0.0, 0.12):
            f = hz(nt) * 2 ** (det / 12)
            ph = rng.random() * 6.28
            s += np.sin(2 * np.pi * f * t + ph) + bright * 0.5 * np.sin(4 * np.pi * f * t + ph) + bright * 0.25 * np.sin(6 * np.pi * f * t)
    s *= env_adsr(n, min(1.2, dur / 3), 0.5, 0.85, min(1.4, dur / 3))
    return s / (len(notes) * 3) * 0.5

def noise(dur):
    return rng.standard_normal(int(dur * SR))

# ------------------------------------------------------------------ chords (midi)
Am, F, C, G, Em, Dm = [57, 60, 64], [53, 57, 60], [48, 52, 55, 60], [55, 59, 62], [52, 55, 59], [50, 53, 57]
# section 1: 0 - 25.4  (melancholy, sparse piano + dark pad)
prog1 = [(0.0, Am), (3.2, F), (6.4, C), (9.6, G), (12.8, Am), (16.0, F), (19.2, C), (22.4, G)]
for t0, ch in prog1:
    add(pad([n - 12 for n in ch], 3.4, 0.15), t0, 0, 0.55)
    arp = ch + [ch[1] + 12]
    for i, nt in enumerate(arp):
        add(piano(nt + 12, 0.9, 0.55 if i else 0.75), t0 + 0.2 + i * 0.75, pan=(i - 1.5) * 0.3)
    add(piano(ch[0] - 12, 2.8, 0.6), t0, 0)

# section 2: 25.4 - 39.45 (decision -> preparation: pulse + faster arpeggio)
prog2 = [(25.4, Am), (28.6, F), (31.8, C), (35.0, G), (38.2, G)]
beat = 0.4  # 150 bpm eighths
for t0, ch in prog2:
    d = 3.2 if t0 < 38 else 1.25
    add(pad([n - 12 for n in ch] + [ch[0]], d + 0.2, 0.35), t0, 0, 0.6)
    add(piano(ch[0] - 12, d, 0.75), t0, 0)
    k = 0
    while k * beat < d - 0.05:
        nt = (ch + [ch[0] + 12])[k % 4] + 12
        add(piano(nt, 0.35, 0.42 + 0.1 * (k % 2 == 0)), t0 + k * beat, pan=0.35 * np.sin(k))
        k += 1
# soft pulse (kick-like thump) from the decision on
def thump(g=1.0):
    n = int(0.35 * SR); t = np.arange(n) / SR
    f = 55 + 70 * np.exp(-t * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9) * 0.6 * g
tt = 26.82
while tt < 39.3:
    add(thump(0.8 if tt < 29 else 1.0), tt, 0)
    tt += 0.8
# riser into the opportunity
n = int(1.4 * SR); r = bp_fast(noise(1.4), 800, 6000) * np.linspace(0, 1, n) ** 2 * 0.25
add(r, 38.1, 0)

# section 3: 39.45 - 49.65 (uplift: C G Am F, bright pad + melody)
prog3 = [(39.45, C), (42.0, G), (44.55, Am), (47.1, F)]
for t0, ch in prog3:
    add(pad([n - 12 for n in ch] + [n for n in ch], 2.7, 0.6), t0, 0, 0.7)
    add(piano(ch[0] - 12, 2.4, 0.8), t0, 0)
    for k in range(6):
        add(piano((ch + [ch[0] + 12, ch[1] + 12])[k % 5] + 12, 0.4, 0.45), t0 + k * 0.42, pan=0.3 * np.sin(k * 1.3))
mel = [(39.6, 76, 1.1), (40.8, 74, 0.6), (41.4, 72, 0.6), (42.1, 74, 1.6), (44.6, 72, 0.8), (45.4, 76, 1.2), (47.2, 77, 0.8), (48.0, 76, 0.6), (48.6, 74, 1.0)]
for t0, nt, d in mel:
    add(piano(nt, d, 0.6), t0, 0.1)
for tt in np.arange(39.45, 49.5, 0.8):
    add(thump(0.9), tt, 0)
n = int(1.0 * SR); add(bp_fast(noise(1.0), 1500, 9000) * np.linspace(0, 1, n) ** 3 * 0.3, 48.65, 0)

# section 4: 49.65 - 57 (brand: F -> G -> C sustained)
add(pad([41, 53, 57, 60, 65], 1.6, 0.6), 49.65, 0, 0.8)
add(pad([43, 55, 59, 62, 67], 1.0, 0.6), 51.25, 0, 0.8)
add(pad([36, 48, 52, 55, 60, 64], 5.6, 0.7), 52.24, 0, 0.95)
for i, nt in enumerate([60, 64, 67, 72, 76]):
    add(piano(nt, 3.5, 0.6), 52.24 + i * 0.09, pan=(i - 2) * 0.25)
add(piano(36, 4.0, 1.0), 52.24, 0)
# impact on "2027"
n = int(1.8 * SR); t = np.arange(n) / SR
boom = np.sin(2 * np.pi * np.cumsum(40 + 60 * np.exp(-t * 12)) / SR) * np.exp(-t * 2.2) * 0.9
boom += lp_fast(noise(1.8), 2500) * np.exp(-t * 6) * 0.25
add(boom, 52.24, 0)
add(bp_fast(noise(3.0), 4000, 14000) * np.exp(-np.arange(int(3 * SR)) / SR * 1.5) * 0.12, 52.24, 0)

# ------------------------------------------------------------------ SFX
def rain(dur, level):
    x = bp_fast(noise(dur), 900, 9000) * 0.5 + lp_fast(noise(dur), 500) * 0.4
    drops = np.zeros(len(x)); idx = rng.integers(0, len(x), int(dur * 60)); drops[idx] = rng.random(len(idx)) * 1.5
    x += bp_fast(drops, 2000, 7000)
    e = np.ones(len(x)); f = int(0.6 * SR); e[:f] = np.linspace(0, 1, f); e[-f:] = np.linspace(1, 0, f)
    return x * e * level
add(rain(9.2, 0.07), 0.0, -0.2); add(rain(9.2, 0.07), 0.0, 0.2)
add(rain(5.2, 0.035), 13.7, 0)
add(rain(3.3, 0.06), 35.3, 0)
# phone vibration
n = int(0.62 * SR); t = np.arange(n) / SR
add(np.sin(2 * np.pi * 165 * t) * (np.sin(2 * np.pi * 7 * t) > -0.2) * 0.22 * np.minimum(1, t / 0.01), 0.1, 0)
# low thud on "não havia"
n = int(1.2 * SR); t = np.arange(n) / SR
add(np.sin(2 * np.pi * np.cumsum(50 + 30 * np.exp(-t * 20)) / SR) * np.exp(-t * 3.5) * 0.55, 2.86, 0)
# whooshes
def whoosh(d=0.5, g=0.35):
    n = int(d * SR); t = np.linspace(0, 1, n)
    return bp_fast(noise(d), 400, 5000) * np.sin(np.pi * t) ** 2 * g
for tt in (8.25, 28.95, 32.7, 25.33):
    add(whoosh(0.45 if tt != 25.33 else 0.3, 0.3), tt, 0.3)
# stamp
n = int(0.4 * SR); t = np.arange(n) / SR
add((lp_fast(noise(0.4), 1200) * 0.8 + np.sin(2 * np.pi * 90 * t)) * np.exp(-t * 18) * 0.45, 11.43, 0.1)
# car passing (doppler swell) 15.5 - 17.8
n = int(2.6 * SR); t = np.arange(n) / SR
car = lp_fast(noise(2.6), 700) * 0.8 + np.sin(2 * np.pi * np.cumsum(90 - 25 * np.tanh((t - 1.3) * 3)) / SR) * 0.3
car *= np.exp(-((t - 1.3) / 0.7) ** 2) * 0.35
i0 = int(15.5 * SR); pan = np.tanh((t - 1.3) * 2)
L[i0:i0 + n] += car * (1 - pan) * 0.8; R[i0:i0 + n] += car * (1 + pan) * 0.8
# paper rip
n = int(0.5 * SR); t = np.arange(n) / SR
rip = bp_fast(noise(0.5), 1500, 8000) * (rng.random(n) > 0.6) * np.exp(-t * 5) * 0.5
add(rip, 26.8, -0.3)
# planner pops
for i in range(17):
    n = int(0.06 * SR); t = np.arange(n) / SR
    add(np.sin(2 * np.pi * (600 + i * 25) * t) * np.exp(-t * 60) * 0.12, 29.1 + 0.05 + i * 0.065, (i % 7 - 3) * 0.15)
# pen ticks
for tt in (30.92, 31.14, 31.36, 31.58):
    add(bp_fast(noise(0.12), 2500, 9000) * np.exp(-np.arange(int(0.12 * SR)) / SR * 30) * 0.35, tt, 0.2)
# card flip + highlighter
add(bp_fast(noise(0.25), 800, 5000) * np.sin(np.linspace(0, np.pi, int(0.25 * SR))) * 0.25, 31.9, 0)
add(bp_fast(noise(0.45), 3000, 10000) * 0.08, 32.24, 0.1)
# running footsteps at dawn
for tt in np.arange(32.9, 35.35, np.pi / 9.2):
    n = int(0.12 * SR); add(lp_fast(noise(0.12), 900) * np.exp(-np.arange(n) / SR * 35) * 0.4, tt, 0)
# calendar pages
for i in range(7):
    add(bp_fast(noise(0.3), 1000, 6000) * np.sin(np.linspace(0, np.pi, int(0.3 * SR))) * 0.15, 35.4 + i * 0.38, 0.3)
# notification ding
n = int(1.2 * SR); t = np.arange(n) / SR
add((np.sin(2 * np.pi * 1318.5 * t) + 0.5 * np.sin(2 * np.pi * 1975.5 * t)) * np.exp(-t * 4) * 0.18, 39.6, 0.2)
add((np.sin(2 * np.pi * 1760 * t)) * np.exp(-t * 4) * 0.14, 39.72, 0.2)
# footsteps to the exam, last one marked
for tt in [43.84 - 0.56 * k for k in range(4, 0, -1)] + [43.84]:
    n = int(0.25 * SR); t = np.arange(n) / SR
    g = 0.75 if abs(tt - 43.84) < 0.01 else 0.35
    add((lp_fast(noise(0.25), 700) * 0.7 + np.sin(2 * np.pi * 70 * t)) * np.exp(-t * 22) * g, tt, 0)
# flash shimmer
add(bp_fast(noise(1.2), 5000, 15000) * np.exp(-np.arange(int(1.2 * SR)) / SR * 3) * 0.1, 49.62, 0)

# ------------------------------------------------------------------ ducking under the voice
voice = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', os.path.join(here, 'audio/narracao.mp3'), '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout, dtype=np.float32).astype(np.float64)
v = np.zeros(N); v[:min(N, len(voice))] = np.abs(voice[:N])
win = int(0.12 * SR); env = np.convolve(v, np.ones(win) / win, 'same')
env = env / (env.max() + 1e-9)
active = np.clip(env * 6, 0, 1)
# smooth attack/release
sm = np.convolve(active, np.ones(int(0.25 * SR)) / int(0.25 * SR), 'same')
duck = 1 - 0.45 * sm  # ~ -5 dB under speech
L *= duck; R *= duck

mx = max(np.abs(L).max(), np.abs(R).max())
L /= mx; R /= mx
out = np.stack([L, R], 1).astype(np.float32)
import wave
with wave.open(os.path.join(here, 'audio/trilha.wav'), 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(out, -1, 1) * 32000).astype(np.int16).tobytes())
print('ok', DUR)
