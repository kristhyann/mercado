# mixagem para vídeo longo: voz + efeitos discretos + trilha suave bem baixa
import numpy as np, soundfile as sf, json, sys
d=sys.argv[1]; SR=48000
v,sr=sf.read(d+'/voz.wav',dtype='float32'); assert sr==SR
T=json.load(open(d+'/tempos.json')); N=int((T['duration']+1)*SR); out=np.zeros(N,np.float32); out[:len(v)]+=v/np.abs(v).max()*.9
rng=np.random.default_rng(3)
def env(n,a=.005,dec=8):
    t=np.arange(n)/SR; e=np.exp(-t*dec); k=max(1,int(a*SR)); e[:k]*=np.linspace(0,1,k); return e
def tone(f0,f1,dur,dec):
    n=int(dur*SR); f=np.linspace(f0,f1,n); return np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.003,dec)
def lp(x,k): return np.convolve(x,np.ones(k)/k,'same')
S={}
S['pop']=tone(420,820,.08,35)
t=np.arange(int(.7*SR))/SR; S['cash']=np.concatenate([np.zeros(int(.02*SR))]); S['cash']=(np.sin(2*np.pi*1568*t)*env(len(t),.002,6)+.6*np.sin(2*np.pi*2093*t)*env(len(t),.002,5))
x=np.zeros(int(.7*SR)); x[int(.12*SR):]+=S['cash'][:len(x)-int(.12*SR)]; x[:int(.05*SR)]+=rng.standard_normal(int(.05*SR))*env(int(.05*SR),.001,60)*.6; S['cash']=x
t=np.arange(int(.5*SR))/SR; S['buzz']=(np.sign(np.sin(2*np.pi*98*t))*.5+np.sin(2*np.pi*196*t)*.5)*env(len(t),.01,4)
n=int(.6*SR); xx=rng.standard_normal(n); S['whoosh']=(xx-lp(xx,8))*np.sin(np.linspace(0,np.pi,n))**2
for k in S: S[k]=S[k]/np.abs(S[k]).max()
vol={'pop':.06,'cash':.14,'buzz':.10,'whoosh':.09}
for e in json.load(open(d+'/eventos.json')):
    s=S[e['type']]*vol[e['type']]; o=int(e['t']*SR); out[o:o+len(s)]+=s[:max(0,N-o)]
# trilha: acordes suaves (Am F C G), troca a cada 4 s, envelope lento
chords=[[220,261.6,329.6],[174.6,220,261.6],[261.6,329.6,392],[196,246.9,293.7]]
seg=int(4*SR); pad=np.zeros(N,np.float32); tt=np.arange(seg)/SR
win=np.minimum(1,tt/1.2)*np.minimum(1,(4-tt)/1.2)
for i in range(N//seg+1):
    c=chords[i%4]; s=sum(np.sin(2*np.pi*f*tt)+.3*np.sin(2*np.pi*f*2*tt+.5) for f in c)*win
    o=i*seg; L=min(seg,N-o); 
    if L<=0: break
    pad[o:o+L]+=s[:L].astype(np.float32)
pad=lp(pad,30); pad=pad/np.abs(pad).max()*.035
fade=np.minimum(1,np.arange(N)/SR/3)*np.minimum(1,(N/SR-np.arange(N)/SR)/4)
out+=pad*fade
sf.write(d+'/mix_bruta.wav',out,SR); print('ok',N/SR)
