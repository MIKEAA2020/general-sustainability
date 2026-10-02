#!/usr/bin/env python3
"""Submission-format composite abstract and first-page keywords; preserve authored part abstracts."""
from pathlib import Path
src=Path('/home/user/papers/paper09_cod_certification_v39.tex');dst=src.with_name('paper09_cod_certification_v40.tex')
s=src.read_text();start=s.index('\\begin{abstract}');end=s.index('\\end{abstract}',start)+len('\\end{abstract}')
abstract=r'''\begin{abstract}
A viability certificate is conditional on its fitted dynamics, disturbance
class, initial-state domain and horizon; it cannot by itself guarantee
protection of a physical resource. We characterize both the certificate
and its failure boundary on Northern cod and the Edwards Aquifer. In a
source-year Schaefer fit to cod (1983--2007), the local 10th-percentile
harvest budget at the limit reference point (LRP, 884.6 kt) is
$C^*=91.59$ kt. Under the registered fixed residual floor, LRP
self-viability for catch $C$ holds precisely when
$r\ge(C+80.87)/[884.6(1-884.6/K)]$; 387 of 2,000 joint parameter
bootstrap refits have a nonpositive budget. The raw fixed-$K$ bootstrap
90\% interval for that budget is $[-69.29,121.07]$ kt. Three of four
common 5th-percentile conventions make the perpetual q05 class vacuous,
and a consistent destination-year refit reduces the q10 budget by
43.3\%. For Edwards, a jump-aware bounded-error set recursion makes
the three-year 618-ft kernel empty above an \emph{assumed uniform}
additive defect of approximately 16.01 ft for business-as-usual pumping
or 17.23 ft for the staged cascade, under UC-min recharge and the
710-ft ceiling. The observed out-of-sample residual maximum (21.81 ft)
exceeds both limits; no future uniform defect bound is established.
These fitted-model certifications are decision aids with quantified
fragility, not unconditional empirical protection guarantees. A separate
exact-rational Northern cod companion addresses historical-event
certification under different assumptions.
\end{abstract}

\noindent\textbf{Keywords:} viability certification; Northern cod;
Edwards Aquifer; harvest rules; feedback; uncertainty sensitivity
'''
s=s[:start]+abstract+s[end:]
assert s.count('\\begin{abstract}')==3 and s.count('\\end{abstract}')==3
assert not dst.exists() or dst.read_text()==s, f'Existing {dst} differs; refusing overwrite'
if not dst.exists():dst.write_text(s)
print('VERIFIED',dst,len(s))
