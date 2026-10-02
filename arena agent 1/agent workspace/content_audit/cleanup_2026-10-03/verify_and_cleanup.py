#!/usr/bin/env python3
"""CAS verify every deletion: exact path on feature branch or pushed archive.
Usage: --plan (write manifest); --apply (assert manifest remote and remove).
Never inspect uploads/ or mutate remote history. Keep v65/v66, current heads,
recovered SI, five-cube artifacts and current preprint upload package.
"""
from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile
import sys,csv,io
sys.path.insert(0,'/home/user/content_audit/claim_alignment')
import push_and_verify as G
R=Path('/home/user');O=R/'content_audit/cleanup_2026-10-03';C=O/'CANONICAL_CLEANUP_MANIFEST.tsv';S=O/'SCRATCH_RECLONE_MANIFEST.tsv';ARCH=O/'UNPUSHED_SCRATCH_ARCHIVE.zip';SNAP=O/'PUSH_SESSION_SNAPSHOT.log'
assert sys.argv[1:] in (['--plan'],['--apply'])
remote=G.api('/git/ref/heads/'+G.BRANCH)['object']['sha'];assert remote==(R/'content_audit/push_tip.txt').read_text().strip()
t=G.api('/git/trees/'+remote+'?recursive=1');assert not t['truncated'];old={e['path']:e['sha'] for e in t['tree'] if e['type']=='blob'}
for p in [ARCH,S,SNAP,O/'archive_workspace_scratch.py']:
 assert old.get(G.ROOT+str(p.relative_to(R)))==G.digest(p.read_bytes()),f'not pushed: {p}'
# Only source/PDF revisions superseded by currently preserved heads; keep
# four previous PDFs used by LATEST_FAMILY_FILES.md for source-only revisions.
cand=[]
def add(pattern):cand.extend(p for p in R.glob(pattern) if p.is_file())
for v in range(18,22):add(f'papers/paper03_computational_certification_v{v}*')
for v in range(34,43):add(f'papers/paper09_cod_certification_v{v}.*')
for s in ['papers/paper02_probabilistic_sufficiency_v14.tex','papers/paper04_minimax_dual_certificates_v18.tex','papers/paper05_exact_belief_computation_v18.tex','papers/paper06_assessment_separation_v69.tex',
 'paper 2 family/02_probabilistic_sufficiency/paper02_probabilistic_sufficiency_v14.tex',
 'paper 2 family/04_minimax_dual_certificates/paper04_minimax_dual_certificates_v18.tex',
 'paper 2 family/05_exact_belief_computation/paper05_exact_belief_computation_v18.tex']:
 p=R/s
 if p.is_file():cand.append(p)
add('paper 2 family/03_computational_certification/paper03_computational_certification_v18*')
add('paper 2 family/09_cod_with_arv/paper09_cod_certification_v34.*')
add('content_audit/scientific_validity/ebc/*.lean')
cand=sorted(set(cand))
# Must not touch publication/review active head material.
for p in cand:
 s=str(p.relative_to(R))
 assert not any(z in s for z in ('v65','v66','v22','v43','ebc_fivecube','paper11_forecasting_baselines_v66_SI')),(s,'protected')
 assert old.get(G.ROOT+s)==G.digest(p.read_bytes()),('not byte-identical on feature branch',s)
rows=[]
for p in cand:
 rel=str(p.relative_to(R));b=p.read_bytes();rows.append((rel,str(len(b)),sha256(b).hexdigest(),old[G.ROOT+rel]))
header='path\tbytes\tsha256\tgit_blob_sha1\n'
expected=header+''.join('\t'.join(row)+'\n' for row in rows)
if sys.argv[1]=='--plan':
 C.write_text(expected)
 print('PLAN_CANONICAL',len(rows),'files',sum(int(r[1]) for r in rows),'bytes','SHA256',sha256(C.read_bytes()).hexdigest())
 print('SCRATCH_ARCHIVE_REMOTE_VERIFIED',old[G.ROOT+str(ARCH.relative_to(R))]);sys.exit(0)
assert C.read_text()==expected,'manifest changed or candidates missing; stop'
assert old.get(G.ROOT+str(C.relative_to(R)))==G.digest(C.read_bytes()),'cleanup manifest not pushed'
# Validate every scratch row against the versioned archive or an actual remote blob.
entries=list(csv.DictReader(io.StringIO(S.read_text()),delimiter='\t'))
with ZipFile(ARCH) as z:
 assert z.testzip() is None
 for row in entries:
  p=R/row['original_path'];assert p.is_file(),p
  data=p.read_bytes();assert len(data)==int(row['bytes']) and sha256(data).hexdigest()==row['sha256']
  if row['storage']=='archived_unique':assert z.read(row['original_path'])==data
  else:
   assert row['storage']=='remote_identical_blob'
   assert old.get(row['locator'])==row['git_blob_sha1'],row
# PUSH_SESSION was changed by earlier operations; the exact current version was pushed as snapshot.
pushlog=R/'content_audit/journal_submission/PUSH_SESSION.log'
assert SNAP.read_bytes()==pushlog.read_bytes()
# Revalidate canonical file contents, then remove only the named paths.
for p in cand:assert old.get(G.ROOT+str(p.relative_to(R)))==G.digest(p.read_bytes())
for p in cand:p.unlink()
for row in entries:(R/row['original_path']).unlink()
pushlog.unlink()
# Prune only now-empty scratch directories, not current ready packages or active sources.
for top in [R/'PREPRINTS_ORG_AUTHOR_REVIEW_2026-10-02',R/'content_audit/revision_pair_cod_2026-10-02',R/'content_audit/journal_submission/preprints_org_ready_2026-10-02']:
 for d in sorted((x for x in top.rglob('*') if x.is_dir()),key=lambda x:len(x.parts),reverse=True):
  if not any(d.iterdir()):d.rmdir()
 if top.name=='PREPRINTS_ORG_AUTHOR_REVIEW_2026-10-02' and not any(top.iterdir()):top.rmdir()
result=f'REMOTE_VERIFIED_TIP {remote}\nDELETED_CANONICAL {len(cand)}\nDELETED_SCRATCH {len(entries)}\nDELETED_SNAPSHOT_OF_MUTABLE_LOG 1\nARCHIVE_SHA256 {sha256(ARCH.read_bytes()).hexdigest()}\nCANONICAL_MANIFEST_SHA256 {sha256(C.read_bytes()).hexdigest()}\n'
(O/'CLEANUP_RESULT.log').write_text(result);print(result)
