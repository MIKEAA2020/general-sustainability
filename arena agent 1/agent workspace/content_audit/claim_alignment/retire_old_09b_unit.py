#!/usr/bin/env python3
"""Retire only superseded, remotely reclonable old paper09b package paths.
Requires the new two-document unit to be remotely present and locally SHA-verified.
No live manuscripts or scientific evidence are deleted.
"""
from pathlib import Path
import sys,json,hashlib
sys.path.insert(0,str(Path(__file__).parent))
from push_and_verify import api,R,ROOT,BRANCH,digest
import csv
oldbase='paper 2 family/09b_regime_viability/'
newbase='paper 2 family/09_cod_with_arv/'
anchor='8f51818a7dfa7886a85ffadd7010e67feb6636dc'
localtip=(R/'content_audit/push_tip.txt').read_text().strip()
actual=api('/git/ref/heads/'+BRANCH)['object']['sha'];assert localtip==actual
before=api('/git/trees/'+anchor+'?recursive=1');current=api('/git/trees/'+actual+'?recursive=1')
assert not before['truncated'] and not current['truncated']
a={e['path']:e['sha'] for e in before['tree'] if e['type']=='blob'}
b={e['path']:e['sha'] for e in current['tree'] if e['type']=='blob'}
old={p:s for p,s in b.items() if p.startswith(ROOT+oldbase)}
assert len(old)==4,old
for p,s in old.items():assert a.get(p)==s,(p,'not byte-identical to remote prior source')
required=('paper09_cod_certification_v32.tex','paper09_cod_certification_v32.pdf','paper09b_arv_certification_v2.tex','paper09b_arv_certification_v2.pdf')
manifest=list(csv.DictReader((R/'paper 2 family/SHA256SUMS.tsv').open(),delimiter='\t'))
for fn in required:
 p=ROOT+newbase+fn
 assert p in b,p
 f=R/newbase/fn
 assert digest(f.read_bytes())==b[p]
 assert any(row['path']==newbase.split('paper 2 family/')[1]+fn and row['sha256']==hashlib.sha256(f.read_bytes()).hexdigest() for row in manifest)
# Only after remote and local new-unit checks does this create a deletion tree.
log=R/'content_audit/claim_alignment/RETIRED_09B_REMOTE_PATHS.tsv'
log.write_text('remote_path\told_blob_sha1\tbaseline_commit\n'+''.join(f'{p}\t{s}\t{anchor}\n' for p,s in sorted(old.items())))
basetree=api('/git/commits/'+actual)['tree']['sha']
newtree=api('/git/trees',{'base_tree':basetree,'tree':[{'path':p,'mode':'100644','type':'blob','sha':None} for p in sorted(old)]})['sha']
commit=api('/git/commits',{'message':'Retire superseded standalone ARV package after verified two-document paper09 unit\n\nFour old blobs remain reclonable at the prior commit. No publication upload.','tree':newtree,'parents':[actual]})['sha']
assert api('/git/ref/heads/'+BRANCH)['object']['sha']==actual
api('/git/refs/heads/'+BRANCH,{'sha':commit},method='PATCH')
after=api('/git/trees/'+commit+'?recursive=1');assert not after['truncated']
c={e['path']:e['sha'] for e in after['tree'] if e['type']=='blob'}
assert not any(p.startswith(ROOT+oldbase) for p in c)
assert all(c[ROOT+newbase+f]==b[ROOT+newbase+f] for f in required)
assert ROOT+'uploads/github_pat.txt' not in c
assert {p:s for p,s in c.items() if p.startswith(ROOT+'uploads/')}=={p:s for p,s in b.items() if p.startswith(ROOT+'uploads/')}  # pre-existing public reference PDF unchanged
(R/'content_audit/push_tip.txt').write_text(commit+'\n')
print('RETIRED_OLD_09B',len(old),'remote old blobs after verified new paper09 main+companion; new tip',commit,'reverse sweep PASS')
