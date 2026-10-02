#!/usr/bin/env python3
"""Push current workspace creations to source-year branch via Git data API.
One family per correction commit, other recovered records grouped by provenance.
Never upload credentials, generated compile caches, excluded dependencies, or mutate live heads.
CAS-check the ref before every push, and reverse-sweep each updated commit's tree.
Usage: python3 content_audit/claim_alignment/push_and_verify.py [--plan]
"""
import sys,json,base64,urllib.request,urllib.error,hashlib,time
from pathlib import Path
from collections import defaultdict,Counter
R=Path('/home/user');A=R/'content_audit/claim_alignment';BRANCH='e2-v3-source-year'
REPO='https://api.github.com/repos/MIKEAA2020/general-sustainability';ROOT='arena agent 1/agent workspace/'
PAT=(R/'uploads/github_pat.txt').read_text().strip()
H={'Authorization':'Bearer '+PAT,'Accept':'application/vnd.github+json','User-Agent':'paper2-family-deposit','Content-Type':'application/json'}
def api(path,data=None,method=None):
 req=urllib.request.Request(REPO+path,data=(json.dumps(data).encode() if data is not None else None),headers=H,method=method)
 for retry in range(3):
  try:
   with urllib.request.urlopen(req,timeout=120) as f:return json.load(f)
  except (urllib.error.URLError,TimeoutError):
   if retry==2:raise
   time.sleep(1+retry)
def digest(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def files():
 for d in ['papers','content_audit','latest','p5','family','b01','b08','b09','b11','paper 2 family','lean_repro']:
  for f in (R/d).rglob('*'):
   if not f.is_file() or f.is_symlink():continue
   rel=f.relative_to(R)
   if any(x in rel.parts for x in ['__pycache__','.cache','.local','build','node_modules']):continue
   if str(rel)=='content_audit/push_tip.txt':continue  # mutable local checkpoint, not evidence
   if 'compile' in rel.parts and str(rel) not in ('content_audit/claim_alignment/compile/results.tsv','content_audit/claim_alignment/compile/all_compiles.log','content_audit/claim_alignment/compile/paper09_results.tsv','content_audit/claim_alignment/compile/paper09_compiles.log'):continue
   if f.suffix.lower() in ('.aux','.toc','.out','.pyc','.synctex.gz'):continue
   yield rel,f
def group(rel):
 s=str(rel);parts=rel.parts
 if s.startswith('paper 2 family/'):
  if parts[1] in ('README.md','SHA256SUMS.tsv','GROUPING_DECISION_2026-10-02.md'):return '99_alignment_meta'
  if parts[1] in ('figs_e1','figs_e3'):return '11_forecasting_baselines'
  if parts[1] in ('figs_e2_v3','figs_e4'):return '09_cod_with_arv'
  return parts[1]
 if s.startswith('content_audit/scientific_validity/'):
  return {'ws':'11c_worked_systems','comp':'03_computational_certification','minimax':'04_minimax_dual_certificates','ebc':'05_exact_belief_computation','psuff':'02_probabilistic_sufficiency','arv':'09b_regime_viability','e1':'11_forecasting_baselines','paper01':'01_obstruction'}.get(parts[2],'other-scientific-validity')
 if s.startswith('content_audit/claim_alignment/'):
  for k,v in (('paper11c_','11c_worked_systems'),('paper03_','03_computational_certification'),('paper04_','04_minimax_dual_certificates'),('paper05_','05_exact_belief_computation'),('paper02_','02_probabilistic_sufficiency'),('paper09b_','09_cod_with_arv'),('paper09_cod_','09_cod_with_arv'),('paper11_','11_forecasting_baselines'),('paper01_','01_obstruction')):
   if k in rel.name:return v
  for k,v in [('ws','11c_worked_systems'),('comp','03_computational_certification'),('minimax','04_minimax_dual_certificates'),('ebc','05_exact_belief_computation'),('psuff','02_probabilistic_sufficiency'),('arv','09b_regime_viability'),('e1','11_forecasting_baselines'),('paper01_compat','01_obstruction'),('paper01_supp_compat','01_obstruction')]:
   if rel.name==f'patch_{k}.py':return v
  if parts[2]=='assets_paper01_supp':return '01_obstruction'
  return '99_alignment_meta'
 if s.startswith('papers/'):
  for k,v in [('PAPER01','01_obstruction'),('WS_','11c_worked_systems'),('COMP_','03_computational_certification'),('MINIMAX_','04_minimax_dual_certificates'),('EBC_','05_exact_belief_computation'),('PSUFF_','02_probabilistic_sufficiency'),('ARV_','09b_regime_viability'),('E1_','11_forecasting_baselines')]:
   if rel.name.startswith(k) and ('SCIENTIFIC' in rel.name or 'LEAN_FIDELITY' in rel.name):return v
  return '90_papers_provenance'
 if parts[0]=='content_audit':return '80_audit_'+(parts[1] if len(parts)>2 else 'misc')
 return '85_workspace_'+parts[0]
def main():
 tip=(R/'content_audit/push_tip.txt').read_text().strip();actual=api('/git/ref/heads/'+BRANCH)['object']['sha']
 assert tip==actual,('branch moved',tip,actual)
 t=api('/git/trees/'+actual+'?recursive=1');assert not t['truncated']
 old={x['path']:x['sha'] for x in t['tree'] if x['type']=='blob'};sha_present=set(old.values())
 grouped=defaultdict(list)
 for rel,p in files():
  b=p.read_bytes();d=digest(b);path=ROOT+str(rel)
  if old.get(path)!=d:grouped[group(rel)].append((str(rel),p,d,len(b)))
 for v in grouped.values():v.sort()
 total=sum(map(len,grouped.values()));size=sum(x[3] for v in grouped.values() for x in v)
 print('PLAN',len(grouped),'commits',total,'changed files',size,'bytes',flush=True)
 for key in sorted(grouped):print(key,len(grouped[key]),sum(x[3] for x in grouped[key]),flush=True)
 if '--plan' in sys.argv:return
 # Commits for individual correction families first; all other records separate.
 order=sorted(grouped,key=lambda k:(0 if k[:2].isdigit() and not k.startswith(('80','85','90','99')) else 1,k))
 history=[];cur=actual
 for key in order:
  entries=grouped[key]
  # Always fetch fresh tip; do not race or silently override another writer.
  now=api('/git/ref/heads/'+BRANCH)['object']['sha']
  assert now==cur,('remote branch drift',cur,now)
  bt=api('/git/commits/'+cur)['tree']['sha'];tree=[]
  for path,f,sha,nbytes in entries:
   if sha not in sha_present:
    data=f.read_bytes();assert digest(data)==sha
    got=api('/git/blobs',{'content':base64.b64encode(data).decode(),'encoding':'base64'})['sha']
    assert got==sha,(path,got,sha);sha_present.add(sha)
   tree.append({'path':ROOT+path,'mode':'100644','type':'blob','sha':sha})
  newtree=api('/git/trees',{'base_tree':bt,'tree':tree})['sha']
  msg=('Stage paper 2 family corrected '+key+' with source-specific provenance' if key[:2].isdigit() and not key.startswith(('80','85','90','99')) else 'Preserve recoverable source/audit records: '+key)
  commit=api('/git/commits',{'message':msg+'\n\nNot a Preprints.org submission. Reviewed live heads unchanged; pinned Lean default build passed, strict generated-axiom gate remains.','tree':newtree,'parents':[cur]})['sha']
  api('/git/refs/heads/'+BRANCH,{'sha':commit},method='PATCH')
  chk=api('/git/trees/'+commit+'?recursive=1');assert not chk['truncated']
  look={x['path']:x['sha'] for x in chk['tree'] if x['type']=='blob'}
  for path,_,sha,_ in entries:assert look[ROOT+path]==sha,path
  history.append((key,cur,commit,len(entries)))
  cur=commit
  (R/'content_audit/push_tip.txt').write_text(cur+'\n')
  # Final metadata commit contains the preceding chain; avoid a self-referential
  # history file changing after the very commit that uploads it.
  if key!='99_alignment_meta':
   (A/'PUSH_HISTORY.tsv').write_text('group\tparent\tcommit\tfiles\n'+''.join('\t'.join(map(str,row))+'\n' for row in history))
  print('PUSHED',key,len(entries),commit,'reverse sweep PASS',flush=True)
 print('REMOTE FINAL',cur,'groups',len(history),'files',sum(x[3] for x in history),flush=True)
if __name__=='__main__':main()
