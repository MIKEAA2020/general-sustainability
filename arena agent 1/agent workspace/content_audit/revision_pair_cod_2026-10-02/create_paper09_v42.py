#!/usr/bin/env python3
"""Versioned neutralization of historical editorial phrasing in the preprint source."""
from pathlib import Path
src=Path('/home/user/papers/paper09_cod_certification_v41.tex');dst=src.with_name('paper09_cod_certification_v42.tex');s=src.read_text()
def change(a,b):
 global s
 assert s.count(a)==1,(a[:110],s.count(a))
 s=s.replace(a,b)
change('''independent of the family scaling and rests only on the identified \\(r\\)
and the corrected 10th-percentile floor.''','''independent of the family scaling and conditional on the fitted \\(r\\)
and the registered source-year 10th-percentile floor.''')
change('''The
corrected bound is read as order \\(70\\)--\\(90\\) kt, not the
\\(40\\)--\\(60\\) kt of the frozen convention.''','''The fixed-$K$ raw bootstrap interval for this bound is
$[-69.29,121.07]$ kt at the 5th and 95th percentiles;
it supplies no positive lower sampling endpoint.''')
change('''On that
object the LRP is protected by good years, but the margin good years
must supply is smaller than the frozen convention implied, and reactive
rule design can protect the LRP but not out-supply a flat 60-kt cap.''','''On that
object the LRP's self-viability is sensitive to the productivity class,
while, under the declared 10th-percentile class, reactive rules can
protect the LRP without out-supplying a comparably protective flat
60-kt cap.''')
change('''Figures 1--9 are produced by
\\texttt{wave\\_e\\_cod/src/make\\_figs\\_v18.py}, which adds the two
structural panels to the seven of
\\texttt{wave\\_e\\_cod/src/make\\_figs\\_v17.py} without changing them;
\\texttt{v17} superseded \\texttt{make\\_figs\\_v16.py} only in
provenance --- it imports the v3 runner and reads the v3 elevation
outputs --- and its output is
identical.''','''Figures 1--9 are produced by
\\texttt{wave\\_e\\_cod/src/make\\_figs\\_v18.py}; its source
reads the declared source-year runner and result files and produces
the seven fitted-map panels and two structural panels.''')
change('''The structural
constants of Section 2.4 and the corrected reactive
criterion of Section 3.4''','''The structural
constants of Section 2.4 and the reactive-rule
criterion of Section 3.4''')
change('''The archived diagnostic
\\texttt{e2\\_breakpoint\\_1992.py} instead uses destination-year catch
for its residuals; it is historical and supplies no source-year result
claimed here. The original \\texttt{campaign\\_e2\\_xteNCAM\\_row.py}
also paired a source-year fit with destination-year floor classes. The
source-year correction and a stable analytic solution of the same
interior least-squares fit, archived with its original and two
recomputed CSV outputs, supplies Section 3.11 instead. All other listed
v3 campaigns use the declared source-year convention of Section 2.3. The
registered-convention counterparts are retained rather than overwritten
(\\texttt{run\\_intervention\\_v2.py} and its outputs, and
\\texttt{wave\\_e\\_cod/src/superseded\\_v2/}), so the convention sensitivity
listed in Section 2.3 can be recomputed from the archive rather than
taken on trust.''','''The Section 3.11 sensitivity pairs source-year fitting with
source-year residual floors using an analytic solution of the
interior least-squares fit. The destination-year sensitivity is
refitted separately before computing its floors. Scripts and paired
outputs for both conventions are archived with the analysis; all
reported primary results use the source-year convention of Section 2.3.''')
assert not dst.exists() or dst.read_text()==s, f'Existing {dst} differs; refusing overwrite'
if not dst.exists():dst.write_text(s)
print('VERIFIED',dst,len(s))
