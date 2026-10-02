#!/usr/bin/env python3
"""Make versioned claim-alignment revision; do not modify earlier manuscript heads."""
from pathlib import Path
src=Path('/home/user/papers/paper09_cod_certification_v36.tex')
dst=src.with_name('paper09_cod_certification_v37.tex')
s=src.read_text()
def change(old,new,n=1):
 global s
 assert s.count(old)==n,(old[:90],s.count(old),n)
 s=s.replace(old,new)
# Main composite abstract: place limitations adjacent to headline numeric result.
change('''protection are one budget. A second constant, $g_{\\max} - |e| = 215.2$ kt, separates viable-but-raised
kernels''','''protection are one budget. This 91.59-kt point result is conditional on the
registered source-year fit and 10th-percentile residual floor: among 2,000
fixed-$K$ bootstrap refits, the raw signed 90\\% percentile interval for its
constructive margin is $[-69.29,121.07]$ kt, with 235 nonpositive margins.
The linear-interpolated 5th-percentile floor makes the q05 perpetual kernel
nonempty, but inverted-CDF, Hazen and Weibull quantiles make it empty; a
consistent destination-year refit changes the q10 constructive bound to
51.95 kt. A second constant, $g_{\\max} - |e| = 215.2$ kt, separates viable-but-raised
kernels''')
# Authored System I lead-in abstract, retained as an abstract: qualify its local headline too.
change('''is exactly \\(C^*\\) minus its catch there --- at that point harvest and
protection are one budget; a second constant''','''is exactly \\(C^*\\) minus its catch there --- at that point harvest and
protection are one budget. Under the declared fixed-$K$ resampling scheme,
the raw signed 90\\% percentile interval for this bound is
$[-69.29,121.07]$ kt (235/2,000 nonpositive), so a positive point bound
is not a positive lower sampling endpoint. The q05 infinite-horizon
nonvacuity result is specific to the archived linear-interpolated quantile;
three other standard conventions make q05 vacuous. A destination-year
fixed-$K$ refit instead gives $C^*=51.95$ kt. A second constant''')
change('''values below use the declared linear-interpolation convention.
With the finite source-year residual pool, other standard 5th-percentile
conventions can move the estimated floor past the maximum surplus; the
5th-percentile nonvacuity verdict is therefore estimator-sensitive.''','''values below use NumPy's default \\texttt{percentile} method \\texttt{linear}
(the source campaign's \\texttt{np.percentile(res\\_tr,5)}), preserved for
like-for-like reproducibility of the registered run, not because it is
uniquely identified by 24 observations. Its q05 floor is $-287.36$ kt;
inverted-CDF, Hazen and Weibull conventions give $-323.51$, $-325.15$
and $-327.61$ kt. The fitted maximum surplus is $296.09$ kt: hence the
linear convention gives a nonempty q05 perpetual kernel for BAU, whereas
all three alternatives exceed that maximum in absolute magnitude and make
even the zero-catch q05 kernel empty. This is a convention-dependent
classification, not a robust physical distinction.''')
change('''constructive boundary is \\(51.95\\) kt, compared with \\(91.59\\) kt
under source-year alignment; BAU retains''','''constructive boundary is \\(51.95\\) kt, compared with \\(91.59\\) kt
under source-year alignment (a 43.3\\% reduction relative to the latter);
BAU retains''')
change('''The 5th-percentile class (\\(-287.4\\)
kt yr\\textsuperscript{-1}) and the 10th-percentile class''','''Only under the declared linear quantile is the 5th-percentile
($-287.4$ kt yr\\textsuperscript{-1}) below $g_{\\max}$; inverted-CDF,
Hazen and Weibull quantiles each make that class vacuous. Under the
declared convention the 5th-percentile ($-287.4$ kt) and the 10th-percentile class''')
change('''content (Table 1, Result 3.3), and the 5th-percentile moratorium kernel
is nonempty (\\(2219.6\\) kt). The correction of the residual convention
therefore reduces the vacuous family from two classes to one.''','''content (Table 1, Result 3.3), and the 5th-percentile moratorium kernel
is nonempty (\\(2219.6\\) kt). Thus exactly one of these three classes
is vacuous only under the registered linear-quantile convention.''')
change('''$-325.15$ kt (Hazen) and $-327.61$ kt (Weibull); only the first lies
above $-g_{\\max}\\simeq-296.09$ kt. Consequently q05
infinite-horizon nonvacuity is a quantile-convention-sensitive conclusion.''','''$-325.15$ kt (Hazen) and $-327.61$ kt (Weibull); only the first lies
above $-g_{\\max}\\simeq-296.09$ kt. The linear method reproduces the
archived \\texttt{np.percentile} campaign, but this provenance does not
privilege it as an estimator of a persistent physical floor. Consequently
q05 infinite-horizon nonvacuity is a quantile-convention-sensitive
conclusion; three of four listed conventions reverse it.''')
# A finite bootstrap ensemble is not a confidence set, and uniform positivity fails even there.
change('''These are conditional parametric-bootstrap
summaries of the declared Schaefer fit and resampling scheme, not
frequentist coverage guarantees across model forms. Under four common''','''These are conditional parametric-bootstrap
summaries of the declared Schaefer fit and resampling scheme, not
frequentist coverage guarantees across model forms. Moreover, keeping the
registered q10 floor fixed, the finite set of all 2,000 joint parameter
refits has 387 members with $C^*\\le0$; even among the 1,457 refits
with $K\\ge2K^*$, 83 have $C^*\\le0$. Thus a uniform positive LRP
self-viability budget is false even over these sampled fitted maps.
These counts concern a finite ensemble, not a validated confidence
region or a probability that a physical policy works. Under four common''')
change('https://www.edwardsaquifer.org/wp-content/uploads/2025/05/2023-Groundwater-Discharge-and-Usage.pdf', '\\url{https://www.edwardsaquifer.org/wp-content/uploads/2025/05/2023-Groundwater-Discharge-and-Usage.pdf}')
change('https://www.edwardsaquifer.org/groundwater-users/critical-period-drought-management/', '\\url{https://www.edwardsaquifer.org/groundwater-users/critical-period-drought-management/}')
change('Washington, DC. https://doi.org/10.17226/21699', 'Washington, DC. \\url{https://doi.org/10.17226/21699}')
change('\\textbf{Limitation, stated because a referee will ask.}', '\\textbf{Catch-timing and fit limitation.}')
change('''On this map the reference point is protected by good years rather than
by demand management --- but under the corrected class the margin that
good years must supply is smaller than the frozen reading implied.''','''Under the registered source-year floors, the LRP's self-viability depends
on the stated productivity class, while catch reduces the remaining local
protection budget.''')
change('held frozen across forms as the corrected source-year classes', 'held fixed across forms at the registered source-year class endpoints')
change('''The source-year floors are milder than the frozen
  ones, so the boundaries sit below the earlier reading at every
  duration.''','''These boundaries are conditional on the declared source-year
  disturbance floors; the table does not mix catch-alignment conventions.''')
change('''reading under the frozen convention is not an identified finding but a
consequence of that convention's harsh floor classes: under the
corrected source-year 10th-percentile class''','''reading under a more severe floor class is not an identified finding but
a consequence of its class choice: under the registered source-year
10th-percentile class''')
change('''horizon, so the geometry-based verdict of the frozen reading no longer
applies.''','''horizon, so a geometry-based verdict depends on the stated
floor class.''')
if dst.exists() and dst.read_text()!=s:
 import hashlib
 assert hashlib.sha256(dst.read_bytes()).hexdigest()=='fab82d1473e02c6ecf6b8dab4afc0f256a97b8de2116cf4fb6eda39b42781ccb', f'Existing {dst} differs from known pre-final draft; refusing overwrite'
 dst.write_text(s)
if not dst.exists(): dst.write_text(s)
assert dst.read_text()==s
print('VERIFIED',dst,len(s))
