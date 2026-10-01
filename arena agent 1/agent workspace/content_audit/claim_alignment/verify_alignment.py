#!/usr/bin/env python3
"""Non-destructive report-only validation of transitional alignment drafts.
No TeX/Lean build or whole-paper scientific-validity verdict is implied.
"""
from collections import Counter
from difflib import unified_diff
from pathlib import Path
import re, sys
root=Path('/home/user');b=root/'content_audit/claim_alignment'
sys.path.insert(0,str(root/'p5'))
import phase0_scan as p0
import scan_continuations as det
names=['paper11c_worked_systems_audit_v2','paper03_computational_certification_v16','paper04_minimax_dual_certificates_v16','paper05_exact_belief_computation_v16','paper02_probabilistic_sufficiency_v12','paper09b_arv_certification_v2','paper11_forecasting_baselines_v64']
files=[n+'.tex' for n in names]+['paper03_computational_certification_v16_supplementary.tex','paper01_obstruction_calculus_v63.tex','paper01_obstruction_calculus_v63_supplementary.tex']
for fn in files:
 src=root/'papers'/fn;dst=b/'drafts'/fn;diff=b/'diffs'/(Path(fn).stem+'.diff')
 a=src.read_text();z=dst.read_text();assert a!=z
 assert diff.read_text()==''.join(unified_diff(a.splitlines(True),z.splitlines(True),fromfile=str(src),tofile=str(dst)))
 original=re.findall(r'\\begin\{abstract\}.*?\\end\{abstract\}',a,re.S)
 if len(original)==1:
  assert (b/'original_abstracts'/(Path(fn).stem+'.txt')).read_text()==original[0]
 elif len(original)>1:
  for i,x in enumerate(original,1):
   assert (b/'original_abstracts'/(Path(fn).stem+f'_abstract_{i}.txt')).read_text()==x
 assert len(original)==len(re.findall(r'\\begin\{abstract\}.*?\\end\{abstract\}',z,re.S))
 for protected in ('Amin Abaee','A.A. conceptualized the entire work, wrote, reviewed and edited the manuscript.'):
  if fn=='paper01_obstruction_calculus_v63_supplementary.tex' and protected=='Amin Abaee':
   assert a.count(protected)==0 and z.count(protected)==1,(fn,protected)
  else:assert a.count(protected)==z.count(protected),(fn,protected)
 # Count only executable TeX: legacy composite terminators were in comments.
 def mismatch(t):
  t='\n'.join(re.sub(r'(?<!\\)%.*$', '', line) for line in t.splitlines())
  return Counter(re.findall(r'\\begin\{([^}]+)\}',t))-Counter(re.findall(r'\\end\{([^}]+)\}',t)),Counter(re.findall(r'\\end\{([^}]+)\}',t))-Counter(re.findall(r'\\begin\{([^}]+)\}',t))
 assert mismatch(a)==mismatch(z)==(Counter(),Counter()),fn
 es=p0.ref_entries(p0.strip_comments(z))
 hits=[(ln,e[:60],det.signals(e,es[i-1][1] if i else '')) for i,(ln,e) in enumerate(es) if det.signals(e,es[i-1][1] if i else '')]
 print(fn,'diff reproducible; abstract archive exact; protected text checked; executable environments balanced; report-only detached-tail candidates',len(hits))
 if hits: print('  ',hits[:5])
 assert not hits,(fn,hits)
print('Report-only draft checks passed; they do not replace the manuscript/witness review or a compile.')
