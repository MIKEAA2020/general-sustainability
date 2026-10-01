#!/usr/bin/env python3
"""Restore the approved byline and contribution on the merged paper09 head.

All three source studies carry an identical author block (also in cod v31).
No date is inferred for the new merged work; \\date{} suppresses TeX's default
current-date insertion. Preserve all four abstracts; remove only a repeated
\\maketitle within the second part. Match exact source and target anchors.
"""
from pathlib import Path
import re

D=Path('/home/user/papers')
p=D/'paper09_cod_certification_v32.tex'
t=p.read_text()
sources=[Path('/home/user/content_audit/seeds/09_paperE2_cod_intervention_v29.tex'),
         D/'paper09_cod_certification_v31.tex',
         D/'paper09b_arv_certification_v2.tex',
         D/'paper10b_edwards_aquifer_v1.tex']
authors=[s.read_text().split('\\author{',1)[1].split('\\date{',1)[0] for s in sources]
assert len(set(authors))==1, 'source bylines disagree'
author='\\author{'+authors[0].strip()
assert 'Amin Abaee' in author and 'orcid.org/0000-0002-0019-1842' in author
assert not re.search(r'^\\author\{',t,re.M)
assert len(re.findall(r'^\\maketitle\s*$',t,re.M))==2
assert len(re.findall(r'^\\title\{',t,re.M))==1
assert len(re.findall(r'^\\begin\{abstract\}',t,re.M))==4
assert len(re.findall(r'^\\end\{abstract\}',t,re.M))==4
anchor='\\title{Certification, not simulation: the viability of harvest rules on two real resource systems, and the horizon of what can be certified}\n\\begin{abstract}'
assert t.count(anchor)==1
t=t.replace(anchor,anchor.replace('\\begin{abstract}',author+'\n\\date{}\n\\maketitle\n\\begin{abstract}'),1)
# Original first title call occurred *after* the combined abstract.
a='\\end{abstract}\n\\maketitle\n\n'
assert t.count(a)==1
t=t.replace(a,'\\end{abstract}\n\n',1)
# The other title call was inside Part II, immediately before its own abstract.
b='\\addcontentsline{toc}{part}{Part II --- Regime viability on Northern cod}\n\n\\maketitle\n\n\\begin{abstract}'
assert t.count(b)==1
t=t.replace(b,b.replace('\\maketitle\n\n',''),1)
start=t.index('\\subsection*{CRediT authorship contribution statement}')
end=t.index('\\subsection*{AI declaration}',start)
old=t[start:end]
assert '[AUTHOR NAME --- full name as it should appear]' in old
assert 'A.A. conceptualized the entire work, wrote, reviewed and edited the manuscript.' not in t
t=t[:start]+'\\subsection*{Author contributions}\nA.A. conceptualized the entire work, wrote, reviewed and edited the manuscript.\n\n'+t[end:]
assert len(re.findall(r'^\\maketitle\s*$',t,re.M))==1
assert len(re.findall(r'^\\author\{',t,re.M))==1
assert len(re.findall(r'^\\begin\{abstract\}',t,re.M))==4
assert len(re.findall(r'^\\end\{abstract\}',t,re.M))==4
p.write_text(t)
print('paper09: source-agreed approved byline restored; approved contribution; one title call, four abstracts')
