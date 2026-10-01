#!/usr/bin/env python3
"""Report-only search for short losses across ALL local intermediate versions.

Unlike the former 8-gram / >=20-unmatched-run scan, compare the body of every
saved version to the current head at 5-gram / >=9-unmatched-run granularity.
Source-to-head matches are only leads; rewritten passages must be read by hand.
"""
import json, pathlib, re, collections
import sys
sys.path.insert(0,'/home/user/content_audit')
import scan_content as old
D=pathlib.Path('/home/user/papers')
allfiles={}
for p in D.glob('paper*.tex'):
 m=re.match(r'(paper\d+[a-z]*)_.*_v(\d+)\.tex$',p.name)
 if m:allfiles.setdefault(m.group(1),[]).append((int(m.group(2)),p))
results=[]
for key, versions in sorted(allfiles.items()):
 versions.sort(); head=versions[-1][1]
 b=[w for w,_ in old.words(old.scope(head.read_text(errors='replace'),'.tex'))]
 n=5; present={tuple(b[i:i+n]) for i in range(len(b)-n+1)}
 for v,source in versions[:-1]:
  text=old.scope(source.read_text(errors='replace'),'.tex');words=old.words(text); a=[w for w,_ in words]
  mask=[tuple(a[i:i+n]) in present for i in range(len(a)-n+1)]
  i=0
  while i<len(mask):
   if mask[i]:i+=1;continue
   j=i+1
   while j<len(mask) and not mask[j]:j+=1
   if j-i>=9:
    start=words[i][1];end=words[min(j+n-2,len(words)-1)][1]
    excerpt=re.sub(r'\s+',' ',text[start:end+1]).strip()
    results.append(dict(key=key,source=source.name,target=head.name,line=text.count('\n',0,start)+1,words=j-i+n-1,excerpt=excerpt[:680]))
   i=j
out=pathlib.Path('/home/user/content_audit/unvisited/short_loss_candidates.json');out.write_text(json.dumps(results,indent=2,ensure_ascii=False))
print('pairs',sum(len(x)-1 for x in allfiles.values()),'candidates',len(results),'by lineage',dict(collections.Counter(x['key'] for x in results)))
for x in results:
 print(x['key'],x['source'].split('_v')[-1],x['line'],x['words'],x['excerpt'][:200])
