import json, sys, re, difflib
from faster_whisper import WhisperModel
d=sys.argv[1]
m=WhisperModel('small',device='cpu',compute_type='int8')
import soundfile as sf, numpy as np
a,sr=sf.read(d+'/voz.wav',dtype='float32')
idx=np.arange(0,len(a),sr/16000); a16=np.interp(idx,np.arange(len(a)),a).astype(np.float32)
segs,_=m.transcribe(a16,language='pt',word_timestamps=True,beam_size=5)
W=[]
for s in segs:
    for w in s.words: W.append((w.word.strip(),w.start,w.end))
print(' '.join(w[0] for w in W))
json.dump(W,open(d+'/whisper.json','w'),ensure_ascii=False)
