"""Build paper5 v40 main tex from v39: F-calibration + cross-system evidence
results, results-at-a-glance table, F-scale scope sentence."""
import re

SRC = '/home/user/paper5_v39/paper5_sampled_governance_v39_NatSustain.tex'
DST = '/home/user/paper5_v40/paper5_sampled_governance_v40_NatSustain.tex'
SUPP15 = '/home/user/paper5_v39/paper5_supplementary_v15_NatSustain.md'
s = open(SRC, encoding='utf-8').read()
n0 = len(s)

def rep(old, new, tag):
    global s
    c = s.count(old)
    assert c == 1, f'{tag}: count={c}\n---\n{old[:220]}'
    s = s.replace(old, new, 1)
    print(f'{tag}: OK')

def repw(old_joined, new, tag):
    global s
    pat = re.compile(re.escape(old_joined).replace(r'\ ', r'\s+'))
    ms = pat.findall(s)
    assert len(ms) == 1, f'{tag}: count={len(ms)}\n---\n{old_joined[:220]}'
    s = pat.sub(lambda _: new, s, count=1)
    print(f'{tag}: OK (flex)')

# V version comment
rep('% The decision clock (paper 5, revision v39): remaining-audit-points incorporation and rejected-research execution (sensitivity battery, F-reparameterisation grid, Neimark-Sacker verification, alternative-band screens, computed Figures 3-5, Table-3 completion) with line numbers for review.',
    '% The decision clock (paper 5, revision v40): q-calibration and cross-system evidence (F-placement, ADH verification, F-excess dormancy test, 50-digit precision certificate), results-at-a-glance table, F-scale scope sentence with line numbers for review.',
    'V-version')

# F1 F-scale scope sentence (data-backed) in the F paragraph
repw(r'with the equilibrium infeasible (\(N^*<0\)) once \(F^*>r\) (Supplementary S11).',
     r'with the equilibrium infeasible (\(N^*<0\)) once \(F^*>r\) (Supplementary S11). Assessed fishing mortality across the 42-stock cohort (median mean-\(F\) 0.37) and a 454-stock broader pool (median 0.21) exceeds the illustrative baseline \(F^*\) by two orders of magnitude, sitting beyond the model feasibility boundary; quantitative thresholds are therefore scale-conditional (Supplementary S12).',
     'F1-Fscale')

# F2 Section 3.5: F-excess + ADH sentences
repw(r'Figure~\ref{fig:screen} shows the baseline \(q\)-value distribution and per-stock null excess.',
     r'Figure~\ref{fig:screen} shows the baseline \(q\)-value distribution and per-stock null excess. Exploitation intensity carries no spectral excess once the ENSO confound is removed (Spearman 0.03 with Peru/Chile excluded, against 0.31 before; Supplementary S12). Across a 454-stock broader pool, the archived cohort median buffer-years (1.79) sits at the second percentile of resampled medians, independently re-executed (Supplementary S12).',
     'F2-xsys')

# F3 Table 3 solver row: precision certificate
repw(r'matrix exponential (\texttt{expm}); IEEE-754 double; 2k/20k/200k scans identical &',
     r'matrix exponential (\texttt{expm}); IEEE-754 double; 2k/20k/200k scans identical; 50-digit certificate (S12) &',
     'F3-certsolver')

# F4 Table 5: results at a glance (before Discussion)
assert s.count('Table 5') == 0, 'Table 5 collision'
m36 = re.search(r'\\subsubsection\{3\.6\s+([^}]*)\}', s)
assert m36, '3.6 header not found'
t36 = m36.group(1).strip()
print('3.6 title:', t36)
d = open(SUPP15, encoding='utf-8').read()
m = re.search(r'- \*\*Main text §3\.6:\*\* (.*?)(?=\n- |\n\n|\Z)', d, re.S)
assert m, 'S1 3.6 row not found'
s1row = ' '.join(m.group(1).split())
print('S1 3.6:', s1row[:150])
if 'ower' in t36:
    row36 = r'\(\S\)3.6 Power analysis & independently re-executed computation \\'
    row36 = 'Power analysis (Section 3.6) & independently re-executed computation \\\\'
elif 'anked' in t36:
    row36 = 'Ranked test (Section 3.6) & executed analysis \\\\'
else:
    row36 = f'{t36} (Section 3.6) & see S1: {s1row[:90]} \\\\'
TABLE5 = r'''Table 5 collects the Section 3 results with their evidential status; Supplementary S1 is the complete inventory.

\textbf{Table 5.} Results at a glance: each Section 3 result with its evidential status.

\begin{longtable}[]{@{}
  >{\raggedright\arraybackslash}p{(\columnwidth - 2\tabcolsep) * \real{0.5000}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 2\tabcolsep) * \real{0.5000}}@{}}
\toprule\noalign{}
\endhead
\bottomrule\noalign{}
\endlastfoot
Forward invariance (Section 3.1) & theorem \\
Rapid-review consistency (Section 3.2) & conditional theorem (finite horizons) \\
Response regions (Section 3.3) & archived records (provisional) \\
Crossing record; battery, F-grid, NS records (Section 3.4) & re-execution-verified computation; nominal-tier records (S11) \\
Screen null; alternative bands; F-excess; ADH (Section 3.5) & re-execution-verified zero count; nominal-tier records (S9.1, S11, S12) \\
''' + row36 + '\n' + r'''Case search (Section 3.7) & executed search (evidential gap, not disconfirmation) \\
Cod two-window split (Section 3.8) & descriptive partition; hypotheses, not results \\
\end{longtable}

\subsection{4'''
rep(r'\subsection{4', TABLE5, 'F4-glance')

print('len delta:', len(s) - n0)
import os
os.makedirs('/home/user/paper5_v40', exist_ok=True)
open(DST, 'w', encoding='utf-8').write(s)
print('WROTE', DST)
