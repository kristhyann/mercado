import json,sys
d=sys.argv[1]
lines=[l for l in open(d+'/roteiro.txt').read().split('\n') if l.strip()]
segs=json.load(open(d+'/segs.json')); W=json.load(open(d+'/whisper.json'))
S=[];match=0
for l,(a,b) in zip(lines,segs):
    rw=l.split(); ww=[w for w in W if w[1]>=a-.15 and w[1]<b+.05]
    if len(ww)==len(rw):
        words=[{'w':r,'start':round(max(x[1],a),3),'end':round(min(x[2],b),3)} for r,x in zip(rw,ww)];match+=1
    else:
        tot=sum(len(r)+2 for r in rw); t=a; words=[]
        for r in rw: dd=(b-a)*(len(r)+2)/tot; words.append({'w':r,'start':round(t,3),'end':round(t+dd,3)}); t+=dd
    S.append({'text':l,'start':round(a,3),'end':round(b,3),'words':words})
import soundfile as sf
info=sf.info(d+'/voz.wav')
json.dump({'duration':round(info.duration+0.4,3),'sentences':S},open(d+'/tempos.json','w'),ensure_ascii=False,indent=1)
print('match',match,'/',len(lines),'dur',info.duration)
