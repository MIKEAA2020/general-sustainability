#!/usr/bin/env python3
"""v29 closing pass: the two declared sensitivities, and a typographic fix.

Open items 3 and 4 of the remediation plan are both *declared* rather than
resolved, and both belong in the paper rather than only in the campaign
scripts:

  3. Table 2's s0 = 642.3 kt is a rounding of the fitted 642.3296 kt. One
     printed cell moves by one grid step.
  4. The Allee and Fox rows are computed on a 0.05 kt state GRID while the
     registered row comes from the committed INTERVAL-ARITHMETIC engine. Next
     to the repelling boundary the grid's rounding compounds along the orbit,
     so a grid boundary can sit up to 1 kt below the committed one. The two
     engines are not comparable at 0.1 kt.

Plus: the first real LaTeX compile (tectonic 0.17) reported two overfull
hboxes in the Data-availability paragraph, the worse at 45 pt, caused by one
unbreakable 84-character path inside \texttt{}. An \allowbreak at the last
directory separator fixes it without changing the rendered text.
"""
from pathlib import Path

P = Path("/home/user/fam/e2/paperE2_cod_intervention_v29.tex")
t = P.read_text(encoding="utf-8")


def rep(old, new, n=1):
    global t
    assert t.count(old) == n, (t.count(old), old[:80])
    t = t.replace(old, new)


# ------------------------------------------------- Section 3.6 reproducibility
rep("""source-year classes its kernels are nonempty at every reported cell and
lie within \\(12\\) kt (about \\(1\\%\\)) of the identified row's at all of
them, so the depensation row does not hinge on the identification of
\\(s_0\\).
""",
    """source-year classes its kernels are nonempty at every reported cell and
lie within \\(12\\) kt (about \\(1\\%\\)) of the identified row's at all of
them, so the depensation row does not hinge on the identification of
\\(s_0\\).

\\emph{Reproducibility note (two declared sensitivities).} First, the
manuscript's \\(s_0 = 642.3\\) kt is a rounding of the fitted
\\(642.3296\\) kt, and one printed cell moves by a single grid step between
them: the BAU worst-class \\(T=\\infty\\) boundary is \\(1098.75\\) kt at the
rounded \\(s_0\\) and \\(1098.8\\) kt at the fitted one (the q05
\\(T=\\infty\\) boundary moves \\(1020.9 \\to 1020.95\\) kt, which prints
identically). Every other cell is unchanged, and the published cells are
those of the rounded \\(s_0\\). Second, the Allee and Fox rows are computed
on a \\(0.05\\) kt state grid, while the registered row comes from the
committed interval-arithmetic engine. Adjacent to the repelling boundary,
where \\(F' > 1\\), the grid's rounding compounds along the orbit and a grid
boundary can sit up to \\(1\\) kt below the interval-arithmetic one:
\\(2218.75\\) against \\(2219.649\\) kt for the BAU q05 \\(T=\\infty\\)
boundary, and \\(2070.30\\) against \\(2070.884\\) kt for zero catch. The two
engines are therefore not to be compared at \\(0.1\\) kt resolution; the
tolerance the campaign declares is \\(1.0\\) kt, and every other cell the
campaign checks agrees to about \\(0.03\\) kt.
""")

# ------------------------------------------------- overfull hbox in Data avail
rep("\\texttt{arena agent 1/other documents/rerun\\_campaigns/campaign\\_e2\\_xteNCAM\\_row.py};",
    "\\texttt{arena agent 1/other documents/rerun\\_campaigns/\\allowbreak\n"
    "campaign\\_e2\\_xteNCAM\\_row.py};")

P.write_text(t, encoding="utf-8")
print("v29f: declared sensitivities added; overfull path made breakable")
