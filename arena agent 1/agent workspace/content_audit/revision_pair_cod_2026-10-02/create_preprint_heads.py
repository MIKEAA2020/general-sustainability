#!/usr/bin/env python3
"""Versioned preprint-format head with conflict declaration before references."""
from pathlib import Path
p=Path('/home/user/papers')
for old,new in [('paper03_computational_certification_v21','paper03_computational_certification_v22'),('paper09_cod_certification_v40','paper09_cod_certification_v41')]:
 src=p/(old+'.tex');dst=p/(new+'.tex');s=src.read_text()
 anchor='\\subsection*{References}'
 assert s.count(anchor)==1
 if old.startswith('paper03'):
  a='\\subsection*{Competing interests}\nNone.\n\n'
  statement='\\subsection*{Conflicts of Interest}\nThe author declares no conflicts of interest.\n\n'
  assert s.count(a)==1;s=s.replace(a,'')
  a='\\path{paper03_computational_certification_v21_supplementary.tex}'
  b='\\path{paper03_computational_certification_v22_supplementary.tex}'
  assert s.count(a)==1;s=s.replace(a,b)
  si=p/'paper03_computational_certification_v22_supplementary.tex'
  content=(p/'paper03_computational_certification_v21_supplementary.tex').read_bytes()
  assert not si.exists() or si.read_bytes()==content
  if not si.exists():si.write_bytes(content)
 else:
  a='''\\subsection*{Declaration of competing interest}

The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to
influence the work reported in this paper.

'''
  assert s.count(a)==1;s=s.replace(a,'')
  statement='\\subsection*{Conflicts of Interest}\nThe author declares no conflicts of interest.\n\n'
 s=s.replace(anchor,statement+anchor)
 assert not dst.exists() or dst.read_text()==s, f'Existing {dst} differs'
 if not dst.exists():dst.write_text(s)
 print('VERIFIED',dst)
