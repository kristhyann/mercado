import sys, numpy as np, soundfile as sf, json
from kokoro_onnx import Kokoro
d=sys.argv[1]; speed=float(sys.argv[2]) if len(sys.argv)>2 else 1.0
k=Kokoro('/tmp/kokoro/kokoro.onnx','/tmp/kokoro/voices.bin')
lines=[l for l in open(d+'/roteiro_voz.txt').read().split('\n') if l.strip()]
out=[];sr=24000;segs=[];t=0.15
out.append(np.zeros(int(sr*.15),dtype=np.float32))
for l in lines:
    a,sr=k.create(l,voice='pm_alex',speed=speed,lang='pt-br')
    # aparar silêncio das bordas
    thr=0.01*np.abs(a).max(); nz=np.where(np.abs(a)>thr)[0]; a=a[max(0,nz[0]-240):nz[-1]+480]
    segs.append((t,t+len(a)/sr)); out.append(a.astype(np.float32)); t+=len(a)/sr
    gap=0.22; out.append(np.zeros(int(sr*gap),dtype=np.float32)); t+=gap
out.append(np.zeros(int(sr*.6),dtype=np.float32))
y=np.concatenate(out); sf.write(d+'/voz.wav',y,sr)
json.dump(segs,open(d+'/segs.json','w'))
words=sum(len(l.split()) for l in lines); print('dur',len(y)/sr,'wps',words/sum(b-a for a,b in segs))
