#!/usr/bin/env python3
"""Move pre-title material in two reviewed composites to make page 1 show
approved author identity, abstract and keywords. No theorem/abstract text edit.
"""
from pathlib import Path
from difflib import unified_diff
R=Path('/home/user');B=R/'content_audit/claim_alignment';D=B/'drafts'
p5=D/'paper05_exact_belief_computation_v16.tex';a=p5.read_text()
part='\\part*{Part I --- Exact belief-state computation at scale}\n\\label{part:scale}\n\\addcontentsline{toc}{part}{Part I --- Computation at scale}\n\n'
assert a.count(part)==1
assert a.index(part)<a.index('\\author{Amin Abaee')
a2=a.replace(part,'',1)
anchor='design; antichain compression\n\n'
assert a2.count(anchor)==1
a2=a2.replace(anchor,anchor+part,1)
p11=D/'paper11_forecasting_baselines_v64.tex';b=p11.read_text()
author='\\author{Amin Abaee\\\\[0.35em]\n{\\small Independent Researcher, Tehran, Iran}\\\\[0.55em]\n{\\small\\href{https://orcid.org/0000-0002-0019-1842}{ORCID: 0000-0002-0019-1842}}\\\\[0.3em]\n{\\small\\href{mailto:amin\\_abaee@ut.ac.ir}{amin\\_abaee@ut.ac.ir}}}\n\\maketitle\n'
assert b.count(author)==1
assert b.index('\\begin{abstract}')<b.index(author)
b2=b.replace(author,'',1)
anchor11='\\title{Forecasting under a locked retention rule: process models, naive benchmarks, and two systems}\n'
assert b2.count(anchor11)==1
b2=b2.replace(anchor11,anchor11+author,1)
for p,old,new in ((p5,a,a2),(p11,b,b2)):
 assert new!=old and new.count('Amin Abaee')==old.count('Amin Abaee')
 p.write_text(new);live=R/'papers'/p.name
 (B/'diffs'/(p.stem+'.diff')).write_text(''.join(unified_diff(live.read_text().splitlines(True),new.splitlines(True),fromfile=str(live),tofile=str(p))))
 print('STAGED_FIRST_PAGE',p.name,'only block ordering changed')
