#!/usr/bin/env python3
"""Apply approved city/country to staged title pages, never reviewed live heads.
Preflight all anchors before writing; rebuild the source-specific diffs.
One-time transform; do not apply twice. Grouping/metadata recorded separately.
"""
from pathlib import Path
from difflib import unified_diff
R=Path('/home/user');B=R/'content_audit/claim_alignment';D=B/'drafts'
files=sorted(D.glob('*.tex'))
assert len(files)==11,[f.name for f in files]
old='Independent Researcher';new='Independent Researcher, Tehran, Iran'
changes=[]
for p in files:
 t=p.read_text();assert new not in t,p
 if p.name=='paper01_obstruction_calculus_v63_supplementary.tex':
  assert t.count(old)==0 and t.count('\\author{Amin Abaee}')==1,p
  updated=t.replace('\\author{Amin Abaee}','\\author{Amin Abaee\\\\[0.2em]{\\small '+new+'}}',1)
 else:
  assert t.count(old)==1,(p,t.count(old))
  updated=t.replace(old,new,1)
 changes.append((p,t,updated))
for p,before,updated in changes:
 p.write_text(updated)
 live=R/'papers'/p.name
 assert live.exists(),p
 (B/'diffs'/(p.stem+'.diff')).write_text(''.join(unified_diff(live.read_text().splitlines(True),updated.splitlines(True),fromfile=str(live),tofile=str(p))))
 if p.name=='paper09_cod_certification_v32.tex':
  (B/'diffs/paper09_cod_certification_v32_host_2026-10-02.diff').write_text(''.join(unified_diff(live.read_text().splitlines(True),updated.splitlines(True),fromfile='papers/'+p.name,tofile='claim_alignment/drafts/'+p.name)))
 if p.name=='paper09b_arv_certification_v2.tex':
  pre=(B/'original_sections/paper09b_arv_v2_prehost.tex').read_text()
  (B/'diffs/paper09b_arv_certification_v2_host_2026-10-02.diff').write_text(''.join(unified_diff(pre.splitlines(True),updated.splitlines(True),fromfile='original_sections/paper09b_arv_v2_prehost.tex',tofile=str(p))))
 print(p.name,'one title-page affiliation updated')
print('PREPARED',len(changes),'sources; original abstracts and reviewed live heads unchanged')
