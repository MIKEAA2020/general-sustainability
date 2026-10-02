#!/usr/bin/env python3
"""Archive noncanonical scratch from vetted paths, recording remote-blob matches.
Never read uploads or credentials. Run before deletion; require CAS Git tip.
"""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import hashlib,sys,re
sys.path.insert(0,'/home/user/content_audit/claim_alignment')
import push_and_verify as G
R=Path('/home/user');O=R/'content_audit/cleanup_2026-10-03';O.mkdir(exist_ok=True)
prefixes=('PREPRINTS_ORG_AUTHOR_REVIEW_2026-10-02/','content_audit/revision_pair_cod_2026-10-02/build','content_audit/journal_submission/preprints_org_ready_2026-10-02/build')
remote=G.api('/git/ref/heads/'+G.BRANCH)['object']['sha'];assert remote==(R/'content_audit/push_tip.txt').read_text().strip()
t=G.api('/git/trees/'+remote+'?recursive=1');assert not t['truncated']
paths={e['path']:e['sha'] for e in t['tree'] if e['type']=='blob'}
blobmap={v:k for k,v in paths.items()}
rows=[];archive=O/'UNPUSHED_SCRATCH_ARCHIVE.zip'
secretpat=re.compile(rb'gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|Bearer [A-Za-z0-9_\-]{20,}|BEGIN (?:RSA|OPENSSH|EC|PRIVATE) KEY|Authorization:\s*Bearer',re.I)
with ZipFile(archive,'w',ZIP_DEFLATED,compresslevel=6) as z:
 for top in [R/'PREPRINTS_ORG_AUTHOR_REVIEW_2026-10-02',R/'content_audit/revision_pair_cod_2026-10-02',R/'content_audit/journal_submission/preprints_org_ready_2026-10-02']:
  for p in sorted(top.rglob('*')):
   if not p.is_file() or p.is_symlink():continue
   rel=p.relative_to(R);s=str(rel)
   if not s.startswith(prefixes):continue
   b=p.read_bytes()
   assert not secretpat.search(b),f'possible credential in {s}; refuse archive'
   blob=G.digest(b);same=paths.get(G.ROOT+s)==blob
   match=blobmap.get(blob)
   # Same-path remote files are canonical and not cleanup candidates.
   if same:continue
   if match:kind='remote_identical_blob';locator=match
   else:kind='archived_unique';locator=archive.relative_to(R).as_posix()+':'+s;z.write(p,arcname=s)
   rows.append((s,len(b),hashlib.sha256(b).hexdigest(),blob,kind,locator))
with ZipFile(archive) as z:
 assert z.testzip() is None
 for s,n,sha,blob,kind,locator in rows:
  if kind=='archived_unique':assert hashlib.sha256(z.read(s)).hexdigest()==sha
(O/'SCRATCH_RECLONE_MANIFEST.tsv').write_text('original_path\tbytes\tsha256\tgit_blob_sha1\tstorage\tlocator\n'+''.join('\t'.join(map(str,row))+'\n' for row in rows))
print('ARCHIVED',sum(r[4]=='archived_unique' for r in rows),'remote-identical',sum(r[4]=='remote_identical_blob' for r in rows),'zip_bytes',archive.stat().st_size,'archive_sha256',hashlib.sha256(archive.read_bytes()).hexdigest())
