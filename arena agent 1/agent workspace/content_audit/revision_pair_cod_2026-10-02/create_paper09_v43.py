#!/usr/bin/env python3
"""Final neutral manuscript-language pass; no result or data changes."""
from pathlib import Path
src=Path('/home/user/papers/paper09_cod_certification_v42.tex')
dst=src.with_name('paper09_cod_certification_v43.tex')
s=src.read_text()
def change(a,b):
 global s
 assert s.count(a)==1,(a[:110],s.count(a))
 s=s.replace(a,b)
change('''form, and the originals behind that form and behind the alternatives compared below should be
named rather than assumed. The logistic surplus-production model,''','''form. The foundational sources for this form and the alternatives compared below
are cited explicitly. The logistic surplus-production model,''')
change('''The fixed-$K$ raw bootstrap interval for this bound is
$[-69.29,121.07]$ kt at the 5th and 95th percentiles;
it supplies no positive lower sampling endpoint.''','''Its fixed-$K$ bootstrap sensitivity has no positive lower sampling endpoint;
see the linked audit for numerical details.''')
change('''The corrected
source-year pool is marginally less severe than the frozen
destination-year pool, so the survival probabilities are higher across
the board.''','''The source-year residual pool is marginally less severe than the
destination-year sensitivity pool, so its survival probabilities are
higher across the board.''')
change('''are therefore conditional stress-test outputs of the originally
specified conversion, not newly established uniform closed-loop
certificates.''','''are therefore conditional stress-test outputs of the declared
conversion, not uniform closed-loop certificates.''')
change('''so no converged fixed point is reported for it; the runner raises the
fixpoint iteration cap to \\(20{,}000\\) and refuses to return an
unconverged iterate, which an earlier \\(300\\)-iteration cap did silently
on exactly this row.''','''so no converged fixed point is reported for it; the runner uses a
fixpoint iteration cap of \\(20{,}000\\) and refuses to return an
unconverged iterate.''')
assert not dst.exists() or dst.read_text()==s, f'Existing {dst} differs; refusing overwrite'
if not dst.exists():dst.write_text(s)
print('VERIFIED',dst,len(s))
