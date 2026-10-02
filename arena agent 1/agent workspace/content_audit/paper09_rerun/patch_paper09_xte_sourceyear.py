#!/usr/bin/env python3
"""Narrow source-year correction to the xteNCAM sensitivity in paper09 main.
Requires the separately archived pre-repair candidate; leaves all other
numerical sections and all original abstracts untouched.
"""
from pathlib import Path
from difflib import unified_diff
import re,csv,hashlib
R=Path('/home/user');A=R/'content_audit/claim_alignment';B=R/'content_audit/paper09_rerun'
original=(B/'pre_xte_sourceyear_paper09_main_candidate.tex').read_text()
p=A/'drafts/paper09_cod_certification_v32.tex'
assert p.read_text()==original,'do not apply over a later draft'
s=original
def change(old,new,label):
 global s
 assert s.count(old)==1,(label,s.count(old))
 s=s.replace(old,new,1)
# Check against the independent one-line repaired runner's actual machine outputs.
summary=list(csv.DictReader((B/'review_candidates/e2_xteNCAM_summary.csv').open()))[0]
rows=list(csv.DictReader((B/'review_candidates/e2_xteNCAM_row.csv').open()))
assert summary['r']=='0.5023' and summary['K']=='4812.88' and summary['e_q10']=='-123.2' and summary['constructive_own_q10']=='7.48'
assert len(rows)==12
by={(r['class_'],r['policy']):r for r in rows}
assert all(float(by[('own_q10',pid)][k])==276.0 for pid in ('flat_0','BAU') for k in ('T1','T5','Tinf'))
assert round(float(by[('own_min','flat_0')]['T1']),1)==462.1
change('''The informative certificate does not survive. Under the fit's own
10th-percentile class the constructive bound is negative
(\\(g(\\mathrm{LRP}) = 130.7\\) kt against \\(|e_{q10}| = 178.7\\) kt). The
zero-catch kernel does not hold the LRP from the LRP itself (\\(T=1\\)
lower boundary \\(309.4\\) kt against the \\(276\\)-kt reference point;
business-as-usual at \\(5\\) kt needs \\(312.9\\) kt). The infinite-horizon
zero-catch boundary under that class is \\(386.9\\) kt --- the reference
point is not robustly viable from itself on the second specification,
and every positive constant catch raises the \\(T=1\\) boundary further
(\\(351.2\\) kt at \\(60\\) kt, \\(393.4\\) kt at \\(120\\) kt). The harsh
classes are not vacuous there (\\(g_{\\max} = 604.4\\) kt \\(> 470.8\\) kt),
and their \\(T=1\\) boundaries run \\(515.7\\) kt (zero catch) to \\(602.3\\)
kt (\\(120\\) kt).

The row is a labelled sensitivity with opposite structure at its own
reference point (Table 7). The two specifications agree on the expansion
classification and on the kernel ordering across the declared catches
(zero catch \\ensuremath{\\leq} business-as-usual \\ensuremath{\\leq} 60 kt \\ensuremath{\\leq} 120 kt at \\(T=1\\) on both).
They disagree on the reference point's self-viability. The 2024 xteNCAM
stock (\\(342\\) kt) sits between the second specification's \\(T=1\\)
(\\(309\\) kt) and \\(T=5\\) (\\(368\\) kt) 10th-percentile zero-catch
boundaries.''','''The informative certificate survives under the source-year convention, but
its margin is much smaller than on the registered NCAM series. For the fit's
own 10th-percentile class, \\(g(\\mathrm{LRP}) = 130.7\\) kt and
\\(|e_{q10}| = 123.2\\) kt give a positive constructive bound of
\\(7.48\\) kt. Zero catch and business-as-usual at \\(5\\) kt hold the
\\(276\\)-kt LRP from itself at \\(T=1,5,\\infty\\); their lower
boundaries are \\(276\\) kt at all three horizons. Catch of \\(60\\) kt
instead requires \\(312.45\\) kt at \\(T=1\\) and \\(397.60\\) kt at
\\(T=\\infty\\); \\(120\\) kt requires \\(354.35\\) kt and \\(546.20\\)
kt respectively. The harsh classes are nonvacuous
(\\(g_{\\max} = 604.4\\) kt \\(> 395.9\\) kt); under the worst class,
the \\(T=1\\) lower boundary runs from \\(462.10\\) kt (zero catch)
to \\(548.05\\) kt (\\(120\\) kt).

This labelled sensitivity therefore agrees with the registered NCAM
series on expansion, catch-ordering, and self-viability at the reference
point under each fit's own 10th-percentile class. It differs sharply in
margin (\\(7.48\\) kt versus \\(91.59\\) kt) and in the stronger floor
classes; no numeric verdict transfers between the distinct records.
The 2024 xteNCAM stock (\\(342\\) kt) is above that specification's
10th-percentile zero-catch and \\(5\\)-kt lower boundaries
(\\(276\\) kt at \\(T=1,5,\\infty\\)), but below its 5th-percentile
zero-catch one-step boundary (\\(345.00\\) kt).''','xte prose')
change('xteNCAM (this row) & 0.5023 & 4812.9 & 1.4447 & \\ensuremath{-}48.0 & 309.4 & 386.9 \\\\', 'xteNCAM (this row) & 0.5023 & 4812.9 & 1.4447 & 7.48 & 276.0 & 276.0 \\\\', 'Table 7 row')
change('''Across assessment specifications the findings are
specification-conditional: on the second, unpooled xteNCAM specification
(LRP \\(276\\) kt) the expansion classification and the kernel ordering
survive while the reference point's self-viability does not --- the
current stock sits between that specification's one- and five-year
zero-catch boundaries (Section 3.11).''','''Across assessment specifications the findings are
specification-conditional: on the second, unpooled xteNCAM specification
(LRP \\(276\\) kt) the expansion classification and kernel ordering
survive, and self-viability under its own 10th-percentile source-year
class holds for zero or \\(5\\)-kt catch --- but its constructive margin
is only \\(7.48\\) kt, not the registered series' \\(91.59\\) kt
(Section 3.11). The current stock does not meet the second
specification's 5th-percentile zero-catch one-step boundary.''','cod conclusion')
change('''and the Section 3.8 one-off treatment of the 1992 draw by
\\texttt{e2\\_breakpoint\\_1992.py} in the same directory. Every script
named above implements the source-year convention of Section 2.3.''','''and the Section 3.8 one-off removal of the 1992 draw by
\\texttt{campaign\\_e2\\_elevation\\_v3.py}. The archived diagnostic
\\texttt{e2\\_breakpoint\\_1992.py} instead uses destination-year catch
for its residuals; it is historical and supplies no source-year result
claimed here. The original \\texttt{campaign\\_e2\\_xteNCAM\\_row.py}
also paired a source-year fit with destination-year floor classes. The
source-year one-line correction, archived with its original and two
recomputed CSV outputs, supplies Section 3.11 instead. All other listed
v3 campaigns use the declared source-year convention of Section 2.3.''','provenance caveat')
change('''On the second specification the answer is no. On xteNCAM 2005--2024 the fit''','''On the second specification the answer depends on the window: the 1995--2024
10th-percentile bound is positive (\\(8.0\\) kt), but on xteNCAM 2005--2024 the fit''','modern window scope')
assert len(re.findall(r'\\begin\{abstract\}.*?\\end\{abstract\}',s,re.S))==3
assert all(x in s for x in ('source-year one-line correction','7.48 & 276.0 & 276.0','Tehran, Iran'))
p.write_text(s)
(B/'PAPER09_XTE_SOURCEYEAR_MANUSCRIPT.diff').write_text(''.join(unified_diff(original.splitlines(True),s.splitlines(True),fromfile='pre_xte_sourceyear_paper09_main_candidate.tex',tofile=str(p))))
live=R/'papers/paper09_cod_certification_v32.tex'
(A/'diffs/paper09_cod_certification_v32.diff').write_text(''.join(unified_diff(live.read_text().splitlines(True),s.splitlines(True),fromfile=str(live),tofile=str(p))))
(A/'diffs/paper09_cod_certification_v32_host_2026-10-02.diff').write_text(''.join(unified_diff(live.read_text().splitlines(True),s.splitlines(True),fromfile='papers/paper09_cod_certification_v32.tex',tofile='claim_alignment/drafts/paper09_cod_certification_v32.tex')))
print('STAGED_NARROW_XTE_REPAIR',len(original),'->',len(s),'source-year bounds regenerated; original abstract blocks preserved')
