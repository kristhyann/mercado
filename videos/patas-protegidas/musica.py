# Trilha emocional original (piano + cordas), gerada por código.
# Começa suave, cresce no meio e termina com sensação de esperança.
import numpy as np, soundfile as sf, json
SR = 48000
T = json.load(open('tempos.json')); DUR = T['duration']; N = int(DUR * SR); out = np.zeros((N, 2))
ALL = [w for s in T['sentences'] for w in s['words']]
def when(word, after=0):
    for w in ALL:
        if w['start'] >= after and w['w'].lower().startswith(word): return w['start']
    return after
T_LIVRO = when('foi'); T_COM = when('com', 29); T_PORQ = when('porque'); T_FIM = when('patas', T_PORQ)
BPM = 70; beat = 60 / BPM; bar = 4 * beat
rng = np.random.default_rng(7)
def addst(sig, t, g=1., pan=0.):
    i = int(t * SR)
    if i >= N or i < 0: return
    s = sig[:N - i]; l = np.sqrt((1 - pan) / 2); r = np.sqrt((1 + pan) / 2)
    out[i:i + len(s), 0] += s * g * l; out[i:i + len(s), 1] += s * g * r
hz = lambda m: 440 * 2 ** ((m - 69) / 12)
def piano(f, dur=2.5):
    n = int(dur * SR); t = np.arange(n) / SR
    s = sum(np.sin(2 * np.pi * f * k * t + k) * (0.6 ** (k - 1)) * np.exp(-t * (1.2 + k * .8)) for k in range(1, 6))
    a = int(.004 * SR); s[:a] *= np.linspace(0, 1, a); return s * .5
def pad(f, dur):
    n = int(dur * SR); t = np.arange(n) / SR
    s = sum(np.sin(2 * np.pi * f * (1 + d) * t + p) for d, p in [(0, 0), (.003, 1), (-.003, 2), (.0015, 3)]) / 4
    s += .3 * np.sin(2 * np.pi * 2 * f * t)
    e = np.minimum(1, t / 1.2) * np.minimum(1, (dur - t) / 1.2); return s * e
# progressão I–V–vi–IV (C G Am F) e variação vi–IV–I–V
PROG = [[48, 55, 60, 64, 67], [43, 50, 59, 62, 67], [45, 52, 57, 60, 64], [41, 48, 57, 60, 65]]
def level(t):  # curva de intensidade 0..1
    if t < T_LIVRO: return .35
    if t < T_COM: return .55
    if t < T_PORQ: return .75
    return 1.0
nb = int(DUR / bar) + 1
for b in range(nb):
    tb = b * bar; ch = PROG[b % 4]; L = level(tb)
    if tb >= DUR: break
    # baixo
    addst(piano(hz(ch[0]), bar * 1.1), tb, .5 * (.6 + .4 * L))
    # arpejo do piano em colcheias
    arp = [ch[1], ch[2], ch[3], ch[4], ch[3], ch[2], ch[3], ch[4]]
    for e, m in enumerate(arp):
        te = tb + e * beat / 2
        if te >= DUR: break
        addst(piano(hz(m + 12), 1.6), te, .22 + .08 * L, pan=(-.3 if e % 2 else .3))
    # cordas entram depois da primeira frase
    if tb >= 7.5:
        for m in ch[1:4]: addst(pad(hz(m), bar + 1.2), tb, .045 * L)
    # melodia simples no clímax
    if tb >= T_PORQ - bar:
        mel = [ch[4] + 12, ch[3] + 12, ch[4] + 12, ch[2] + 24]
        for e, m in enumerate(mel): addst(piano(hz(m), 2.0), tb + e * beat, .16)
    # pulso leve (bumbo suave) na parte do meio
    if T_COM - .2 <= tb < T_FIM:
        n = int(.3 * SR); t = np.arange(n) / SR; k = np.sin(2 * np.pi * np.cumsum(45 + 60 * np.exp(-t * 25)) / SR) * np.exp(-t * 10)
        for q in range(4): addst(k, tb + q * beat, .18 * L)
# acorde final aberto (C com nona) segurando até o fim
for m in [36, 48, 55, 60, 62, 64, 67, 72]: addst(piano(hz(m), DUR - T_FIM + 1), T_FIM, .16)
for m in [48, 55, 64]: addst(pad(hz(m), DUR - T_FIM), T_FIM, .06)
# reverb simples (eco difuso)
rev = np.zeros_like(out)
for d, g in [(.031, .35), (.047, .3), (.071, .25), (.113, .2), (.173, .15), (.257, .1)]:
    i = int(d * SR); rev[i:, 0] += out[:-i, 1] * g; rev[i:, 1] += out[:-i, 0] * g
out = out + rev
fade = int(2.5 * SR); out[-fade:] *= np.linspace(1, 0, fade)[:, None]
out /= np.abs(out).max() + 1e-9; out *= .8
sf.write('musica.wav', out.mean(1), SR)
print('musica.wav', DUR)
