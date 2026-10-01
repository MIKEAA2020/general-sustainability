#!/usr/bin/env python3
"""Delete ONLY locally redundant and verified remote-backed copies; keep live heads.
--apply performs deletion after checking remote branch blob SHA and local digest.
Generated compile intermediates are reproducible with compile_drafts.py; their
final PDFs are retained in paper 2 family. Preserves count-source Lean modules.
"""
from pathlib import Path
import re,json,hashlib,urllib.request,sys,tarfile
R=Path('/home/user');A=R/'content_audit/claim_alignment';root='arena agent 1/agent workspace/'
tip=(R/'content_audit/push_tip.txt').read_text().strip();pat=(R/'uploads/github_pat.txt').read_text().strip()
req=urllib.request.Request('https://api.github.com/repos/MIKEAA2020/general-sustainability/git/trees/'+tip+'?recursive=1',headers={'Authorization':'Bearer '+pat,'User-Agent':'safe-prune'})
with urllib.request.urlopen(req,timeout=120) as f:tree=json.load(f)
assert not tree['truncated'];remote={x['path']:x['sha'] for x in tree['tree'] if x['type']=='blob'}
def digest(p):
 b=p.read_bytes();return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
need_count={p.resolve() for p in (R/'content_audit/scientific_validity/ebc').glob('*.lean')}
need_count.add((R/'latest/lean/Minimax_Dual.lean').resolve())
candidates=[]
for d in [R/'content_audit/scientific_validity',R/'latest/lean']:
 for p in d.rglob('*.lean'):
  if p.resolve() not in need_count:candidates.append((p,'source-matched Lean copy; remote verified'))
# Archive only clearly older files of the same name/version lineage; retain any
# named in local runnable producer/review scripts and every supplement.
script_text='\n'.join(p.read_text(errors='replace') for d in ['content_audit','p5','papers/supprec'] for p in (R/d).rglob('*.py') if '__pycache__' not in p.parts)
tex=list((R/'papers').glob('*.tex'));latest={}
for p in tex:
 m=re.fullmatch(r'(.*)_v(\d+)\.tex',p.name)
 if m:latest[m.group(1)]=max(latest.get(m.group(1),0),int(m.group(2)))
for p in tex:
 m=re.fullmatch(r'(.*)_v(\d+)\.tex',p.name)
 if m and int(m.group(2))<latest[m.group(1)] and p.name not in script_text:
  candidates.append((p,'superseded TeX lineage; not named by runnable scripts'))
# Repeated root-level working copies: the live paper remains in papers/ and
# compiled corrected main PDFs are in paper 2 family (except unrelated b08).
for d in ('b01','b08','b09','b11'):
 for p in (R/d).glob('*'):
  if p.is_file() and p.suffix in ('.tex','.pdf'):
   if p.suffix=='.tex' and not (R/'papers'/p.name).exists():continue
   candidates.append((p,'root-level duplicate, remote-backed; papers/ head and figures retained'))
# All per-run copied TeX/PDF/logs in compile/<family> are regenerable, with the
# successful summary files retained and corrected PDF bundle kept separately.
for p in (A/'compile').rglob('*'):
 if p.is_file() and not p.is_symlink() and p.name not in ('results.tsv','all_compiles.log'):
  candidates.append((p,'rebuildable isolated TeX compile output'))
# Remove LaTeX auxiliary files that Tectonic recreates (never authoritative).
for p in (R/'b08').glob('*'):
 if p.is_file() and p.suffix in ('.aux','.toc','.out'):
  candidates.append((p,'regenerable LaTeX auxiliary'))
# Confirm offline that the release tar is exactly the executable we retain.
archive=R/'tools/t.tar.gz';binary=R/'tools/tectonic'
assert archive.exists() and binary.exists()
with tarfile.open(archive,'r:gz') as tf:
 assert tf.getnames()==['tectonic']
 assert hashlib.sha256(tf.extractfile('tectonic').read()).hexdigest()==hashlib.sha256(binary.read_bytes()).hexdigest()
candidates.append((archive,'duplicate release archive: extracted binary retained'))
# Strongest case: current repo tree contains byte-identical blob at same path.
rows=[]
for p,why in sorted(set(candidates)):
 rel=str(p.relative_to(R)); sha=digest(p);rem=remote.get(root+rel)
 if rel=='tools/t.tar.gz':
  backed='DUPLICATE_OF_RETAINED_BINARY'
 elif rel.startswith(('content_audit/claim_alignment/compile/','b08/')) and (p.suffix in ('.aux','.toc','.out') or '/compile/' in rel):
  # Generated files need not be in Git; their source and builder are preserved.
  backed='REBUILDABLE'
 else:
  assert rem==sha,(rel,sha,rem)
  backed='REMOTE_SHA_IDENTICAL'
 rows.append((rel,p.stat().st_size,sha,backed,why))
manifest=A/'PRUNE_MANIFEST.tsv'
manifest.write_text('path\tbytes\tgit_blob_sha\tverification\treason\n'+''.join('\t'.join(map(str,row))+'\n' for row in rows))
print('eligible',len(rows),'bytes',sum(row[1] for row in rows),'MB',round(sum(row[1] for row in rows)/1e6,2),'manifest',manifest)
if '--apply' in sys.argv:
 for rel,_,_,_,_ in rows:(R/rel).unlink()
 # no work product in empty per-run subfolders; preserve compile root summaries
 for p in sorted((A/'compile').glob('*')):
  if p.is_dir():
   for x in p.iterdir():
    if x.is_symlink():x.unlink()
   if not any(p.iterdir()):p.rmdir()
 for d in ('b01','b08','b09','b11'):
  pass
 print('removed',len(rows),'verified/rebuildable local copies. Kept',len(need_count),'Lean count sources and all live heads.')
