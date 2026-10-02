#!/usr/bin/env python3
"""Reframe fragility as a conditional result; preserve all previous versioned sources."""
from pathlib import Path
src=Path('/home/user/papers/paper09_cod_certification_v37.tex');dst=src.with_name('paper09_cod_certification_v38.tex');s=src.read_text()
def change(old,new):
 global s
 assert s.count(old)==1,(old[:100],s.count(old))
 s=s.replace(old,new)
change('''Two systems, different
hydrologies, different institutions, a conditional, model-and-domain-dependent comparison. A certified verdict is therefore
not a stronger version of a simulated one; it is a different kind of object, whose validity is
\\emph{local in time} and whose locality can be quantified.''','''Two systems, different
hydrologies, different institutions, a conditional, model-and-domain-dependent comparison.
The sensitivity itself is a result: 387 of 2,000 joint parameter refits
lose the positive cod LRP budget under the registered fixed floor, three of
four standard q05 conventions reverse the nonvacuity verdict, catch-year
alignment changes the q10 budget by 43.3\\%, and the Edwards training-error
maximum fails out of sample. These certifications are decision aids conditional
on stated fits, conventions and error models, not unconditional empirical
protection guarantees. Their qualified validity is \\emph{local in time}
and its limits can be quantified.''')
change('''fixed-$K$ refit instead gives $C^*=51.95$ kt. A second constant''','''fixed-$K$ refit instead gives $C^*=51.95$ kt. Under the fixed
registered q10 floor, 387/2,000 joint $(r,K)$ refits have a nonpositive
LRP budget, including 83/1,457 with $K\\ge 2K^*$. These are finite
ensemble sensitivity counts, not calibrated confidence-set coverage or
physical policy probabilities. A second constant''')
change('''\\subsection{4. Discussion}\\label{budget-discussion}

The horizon has a management consequence''','''\\subsection{4. Discussion}\\label{budget-discussion}

\\noindent\\textbf{Certification as a conditional decision aid.}
The $91.59$-kt constructive boundary is a point calculation under the
registered source-year map, q10 estimator and declared floor, not a
universally admissible catch. The raw bootstrap crosses zero, three
standard alternative q05 estimators reverse the perpetual-kernel
classification, and a consistently refitted destination-year alignment
reduces $C^*$ by 43.3\\%. Under the fixed registered floor, the set of
joint parameter refits includes models with a nonpositive LRP budget,
even within the expansive regime. Thus the falsifiable output is a
model-and-class-specific certificate together with its failure
boundaries. These sensitivities inform management comparisons without
proving that any intervention protects the physical stock for every
future productivity sequence.

The horizon has a management consequence''')
assert not dst.exists() or dst.read_text()==s, f'Existing {dst} differs; refusing overwrite'
if not dst.exists():dst.write_text(s)
print('VERIFIED',dst,len(s))
