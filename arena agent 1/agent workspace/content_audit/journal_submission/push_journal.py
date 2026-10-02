#!/usr/bin/env python3
"""CAS-push final current manuscript artifacts and their scoped review; preserve old remote heads."""
from pathlib import Path
import sys,base64,json
sys.path.insert(0,'/home/user/content_audit/claim_alignment')
import push_and_verify as G
R=Path('/home/user');ROOT=G.ROOT;BR=G.BRANCH
ROOT_DOCS=['LATEST_FAMILY_FILES.md','REVISED_MANUSCRIPTS_2026-10-02.md','JOURNAL_SUBMISSION_REVIEW_2026-10-02.md','SIX_MANUSCRIPT_AUDIT_ADJUDICATION_2026-10-02.md','SIX_AUDITS_REMAINING_POINTS_ADDENDUM_2026-10-02.md','SIX_MANUSCRIPT_REVISION_STATUS_2026-10-02.md','PAIR_CERTIFICATES_AND_COD_FEEDBACK_COMPLETION_2026-10-02.md']
remote=G.api('/git/ref/heads/'+BR)['object']['sha'];expected=(R/'content_audit/push_tip.txt').read_text().strip()
assert remote==expected,(remote,expected)
tree=G.api('/git/trees/'+remote+'?recursive=1');assert not tree['truncated']
old={e['path']:e['sha'] for e in tree['tree'] if e['type']=='blob'}
files=[(rel,p) for rel,p in G.files() if str(rel)!='content_audit/journal_submission/PUSH_SESSION.log']+[(Path(s),R/s) for s in ROOT_DOCS]
changed=[]
for rel,p in files:
 data=p.read_bytes();sha=G.digest(data);target=ROOT+str(rel)
 if old.get(target)!=sha:changed.append((rel,p,sha,len(data)))
print('PLAN',len(changed),'files',sum(x[3] for x in changed),'bytes',flush=True)
print('\n'.join(str(x[0]) for x in changed),flush=True)
if '--plan' in sys.argv:sys.exit(0)
if not changed:
 print('NOTHING_UNPUSHED',remote,flush=True)
 sys.exit(0)
seen=set(old.values())
entries=[]
for i,(rel,p,sha,size) in enumerate(changed,1):
 assert G.api('/git/ref/heads/'+BR)['object']['sha']==remote if i==1 else True
 if sha not in seen:
  blob=G.api('/git/blobs',{'content':base64.b64encode(p.read_bytes()).decode(),'encoding':'base64'})['sha'];assert blob==sha,(str(rel),blob,sha)
  seen.add(sha)
 entries.append({'path':ROOT+str(rel),'mode':'100644','type':'blob','sha':sha})
 if i%20==0:print('UPLOADED',i,'/',len(changed),flush=True)
assert G.api('/git/ref/heads/'+BR)['object']['sha']==remote,'remote moved before commit'
base=G.api('/git/commits/'+remote)['tree']['sha']
newtree=G.api('/git/trees',{'base_tree':base,'tree':entries})['sha']
commit=G.api('/git/commits',{'message':'Prove pair delay thresholds and rerun cod/Edwards feedback analyses\n\nVersion 20 proves exact pair all-control duals; version 36 reconstructs 78 cod table cells, uncertainty, alignment and direct trigger-aware bounded-error kernels. Prior heads preserved; no portal submission or DOI creation.','tree':newtree,'parents':[remote]})['sha']
assert G.api('/git/ref/heads/'+BR)['object']['sha']==remote,'remote moved before ref update'
G.api('/git/refs/heads/'+BR,{'sha':commit},method='PATCH')
verified=G.api('/git/trees/'+commit+'?recursive=1');assert not verified['truncated']
now={e['path']:e['sha'] for e in verified['tree'] if e['type']=='blob'}
for rel,p,sha,size in changed:assert now[ROOT+str(rel)]==sha,(str(rel),sha)
(R/'content_audit/push_tip.txt').write_text(commit+'\n')
print('REMOTE_VERIFIED',commit,'changed',len(changed),flush=True)
