# alinha roteiro.txt com whisper.json de uma voz externa (mp3) -> tempos.json
import json, sys, re, unicodedata, difflib, soundfile as sf
d=sys.argv[1]
def norm(w):
    w=unicodedata.normalize('NFD',w.lower()); w=''.join(c for c in w if unicodedata.category(c)!='Mn'); return re.sub(r'[^a-z0-9]','',w)
lines=[l for l in open(d+'/roteiro.txt').read().split('\n') if l.strip()]
R=[(i,w) for i,l in enumerate(lines) for w in l.split()]
W=json.load(open(d+'/whisper.json'))
a=[norm(w) for _,w in R]; b=[norm(w[0]) for w in W]
T=[None]*len(R)
for blk in difflib.SequenceMatcher(None,a,b,autojunk=False).get_matching_blocks():
    for k in range(blk.size): T[blk.a+k]=(W[blk.b+k][1],W[blk.b+k][2])
# preencher buracos por interpolação
for k in range(len(R)):
    if T[k] is None:
        p=max([j for j in range(k) if T[j]],default=None); n=min([j for j in range(k+1,len(R)) if T[j]],default=None)
        t0=T[p][1] if p is not None else 0; t1=T[n][0] if n is not None else t0+.4
        cnt=(n if n is not None else k+1)-(p if p is not None else -1)-1; pos=k-(p if p is not None else -1)
        s=t0+(t1-t0)*(pos-1)/cnt; T[k]=(s,t0+(t1-t0)*pos/cnt)
print('casadas',sum(1 for x in a if x),'faltando',sum(1 for k in range(len(R)) if not any(True for _ in [0])))
S=[]
for i,l in enumerate(lines):
    ks=[k for k in range(len(R)) if R[k][0]==i]
    words=[{'w':R[k][1],'start':round(T[k][0],3),'end':round(T[k][1],3)} for k in ks]
    S.append({'text':l,'start':words[0]['start'],'end':words[-1]['end'],'words':words})
dur=sf.info(d+'/voz.wav').duration
json.dump({'duration':round(max(dur,S[-1]['end'])+1.2,3),'sentences':S},open(d+'/tempos.json','w'),ensure_ascii=False,indent=1)
print('dur',dur); print(' '.join(f"{i}:{s['start']:.1f}" for i,s in enumerate(S)))
