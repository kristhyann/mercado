import numpy as np, soundfile as sf, json, sys
d=sys.argv[1]; SR=48000
v,sr=sf.read(d+'/voz.wav',dtype='float32')
idx=np.arange(0,len(v),sr/SR); v=np.interp(idx,np.arange(len(v)),v).astype(np.float32)
T=json.load(open(d+'/tempos.json')); N=int((T['duration']+0.5)*SR); out=np.zeros(N,np.float32); out[:len(v)]+=v/np.abs(v).max()*0.9
rng=np.random.default_rng(1)
def env(n,a=0.005,dec=8):
    t=np.arange(n)/SR; e=np.exp(-t*dec); k=int(a*SR); e[:k]*=np.linspace(0,1,k); return e
def lp(x,k): return np.convolve(x,np.ones(k)/k,'same')
def tone(f0,f1,dur,dec):
    n=int(dur*SR); f=np.linspace(f0,f1,n); ph=2*np.pi*np.cumsum(f)/SR; return np.sin(ph)*env(n,.003,dec)
S={}
S['pop']=tone(380,950,.09,30)
p=np.zeros(int(.6*SR)); t=np.arange(len(p))/SR
for f,a in [(820,1),(1270,.7),(2140,.5),(3400,.3)]: p+=a*np.sin(2*np.pi*f*t)
S['clang']=p*env(len(p),.001,7)
n=int(.4*SR); S['puf']=lp(rng.standard_normal(n),18)*env(n,.01,9)*3
t=np.arange(int(.9*SR))/SR; S['ding']=(np.sin(2*np.pi*1320*t)+.5*np.sin(2*np.pi*2640*t)+.2*np.sin(2*np.pi*3960*t))*env(len(t),.002,5)
t=np.arange(int(.32*SR))/SR; S['buzzx']=np.sign(np.sin(2*np.pi*110*t))*.5*env(len(t),.005,4)
n=int(.12*SR); S['crack']=(rng.standard_normal(n)*env(n,.0005,45)+tone(140,60,.12,25)*1.2)
t=np.arange(int(1.4*SR))/SR; w=np.sin(2*np.pi*(620*t+12*np.sin(2*np.pi*7*t)))+.4*np.sin(2*np.pi*(1240*t)); e=np.minimum(1,t/.3)*np.minimum(1,(1.4-t)/.4); S['mosq']=w*e*.35
n=int(.45*SR); x=rng.standard_normal(n); e=np.sin(np.linspace(0,np.pi,n))**2; S['whoosh']=(x-lp(x,6))*e*.6
seq=[523,659,784,1047]; win=np.zeros(int(.9*SR))
for i,f in enumerate(seq):
    s=tone(f,f,.45,6)+.3*tone(2*f,2*f,.45,8); o=int(i*.09*SR); win[o:o+len(s)]+=s
S['win']=win
t=np.arange(int(.35*SR))/SR; S['gulp']=np.sin(2*np.pi*np.cumsum(np.linspace(300,90,len(t)))/SR)*env(len(t),.005,7)
n=int(.25*SR); z=rng.standard_normal(n)*np.sign(np.sin(2*np.pi*60*np.arange(n)/SR)); S['zap']=z*env(n,.002,14)
S['buzz']=S['buzzx']
for k in S: S[k]=S[k]/np.abs(S[k]).max()
vol={'gulp':.25,'zap':.12,'buzz':.12,'pop':.16,'clang':.2,'puf':.2,'ding':.18,'buzzx':.12,'crack':.25,'mosq':.1,'whoosh':.12,'win':.2}
for e in json.load(open(d+'/eventos.json')):
    s=S[e['type']]*vol[e['type']]; o=int(e['t']*SR); out[o:o+len(s)]+=s[:N-o]
sf.write(d+'/mix_bruta.wav',out,SR)
print('ok',len(out)/SR)
