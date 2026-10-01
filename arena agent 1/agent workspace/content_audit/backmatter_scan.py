#!/usr/bin/env python3
"""Compare declarations and supplement pointers, separately from manuscript body and References."""
import sys,re,json,pathlib
sys.path.insert(0,'/home/user/content_audit');import scan_content as a

def tail(s):
 s=a.clean(s)
 m=re.search(r'\\(?:sub)*section\*?\{Declarations\}',s)
 if not m:return ''
 return re.sub(r'\\end\{document\}', '',s[m.start():])

def compare(src,head):
 s=tail(src.read_text(errors='replace'));h=tail(head.read_text(errors='replace'))
 if not s:return None
 sw=[w for w,p in a.words(s)];hw=[w for w,p in a.words(h)]
 gs={tuple(hw[i:i+7]) for i in range(max(0,len(hw)-6))}
 good=[tuple(sw[i:i+7]) in gs for i in range(max(0,len(sw)-6))]
 # contiguous missing word spans >=12; source lines by word offsets
 runs=[];i=0
 while i<len(good):
  if good[i]:i+=1;continue
  j=i+1
  while j<len(good) and not good[j]:j+=1
  if j-i>=12:
   ws=a.words(s);start=ws[i][1];end=ws[min(j+6,len(ws)-1)][1]
   runs.append(dict(words=j-i+6,excerpt=re.sub(r'\s+',' ',s[start:end+20]).strip()[:370]))
  i=j
 return dict(source=src.name,head=head.name,source_words=len(sw),head_words=len(hw),coverage=(sum(good)/len(good) if good else 1),runs=runs,missing_head=(not bool(h)))
res=[]
for key,h in sorted(a.HEAD.items()):
 for typ,s in [('seed',a.SEED[key])]+[('predecessor',a.D/q) for q in a.SRC[key]]:
  x=compare(s,h)
  if x:
   x['key']=key;x['kind']=typ;res.append(x)
   print(f"{key:8} {typ:11} srcW={x['source_words']:4} headW={x['head_words']:4} coverage={x['coverage']:6.1%} runs={len(x['runs']):2} absent={x['missing_head']}")
pathlib.Path('/home/user/content_audit/backmatter_comparisons.json').write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
