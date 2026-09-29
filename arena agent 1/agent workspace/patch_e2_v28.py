#!/usr/bin/env python3
"""E2 v27 -> v28: propagate the registered (v2) disturbance classes through
the numeric layer and the vacuity structure.

Replacements are applied with str.replace (replace-all, no hardcoded counts),
then a residual sweep reports any expected token that survived.
"""
import os
import re
import shutil

SRC = "/home/user/fam/e2/paperE2_cod_intervention_v27.tex"
DST = "/home/user/fam/e2/paperE2_cod_intervention_v28.tex"

tex = open(SRC, encoding="utf-8").read()
orig = tex

# (label, old, new)
EDITS = []

# ---------------------------------------------------------------- Table 1
EDITS.append(("T1 BAU", r"""BAU (5 kt) & 1025.5 & empty & 989.0 & 2219.6 & \textbf{884.6} &
\textbf{884.6} \\""", r"""BAU (5 kt) & 1141.0 & empty & 1016.5 & empty & \textbf{884.6} &
\textbf{884.6} \\"""))

EDITS.append(("T1 flat240", r"""flat 240 kt & 1233.5 & empty & 1196.4 & empty & 1014.0 & empty \\""",
              r"""flat 240 kt & 1351.1 & empty & 1224.4 & empty & 1043.8 & empty \\"""))

EDITS.append(("T1 flat180", r"""flat 180 kt & 1180.0 & empty & 1143.1 & empty & 961.5 & 1637.8 \\""",
              r"""flat 180 kt & 1297.1 & empty & 1171.0 & empty & 991.2 & 2338.3 \\"""))

EDITS.append(("T1 flat120", r"""flat 120 kt & 1126.8 & empty & 1090.1 & empty & 909.3 & 1082.3 \\""",
              r"""flat 120 kt & 1243.4 & empty & 1117.8 & empty & 938.8 & 1363.0 \\"""))

EDITS.append(("T1 flat60", r"""flat 60 kt & 1073.8 & empty & 1037.2 & empty & \textbf{884.6} &
\textbf{884.6} \\""", r"""flat 60 kt & 1189.9 & empty & 1064.9 & empty & 886.7 &
900.3 \\"""))

EDITS.append(("T1 S1", r"""S1 / cascade & 1073.8 & empty & 1037.2 & empty & \textbf{884.6} &
\textbf{884.6} \\""", r"""S1 / cascade & 1189.9 & empty & 1064.9 & empty & 886.7 &
900.3 \\"""))

EDITS.append(("T1 flat0", r"""flat 0 kt & 1021.1 & empty & 984.7 & 2070.9 & \textbf{884.6} &
\textbf{884.6} \\""", r"""flat 0 kt & 1136.6 & empty & 1012.1 & empty & \textbf{884.6} &
\textbf{884.6} \\"""))

EDITS.append(("T1 A0.25", r"""Family A, \(\phi\)=0.25 & 1064.7 & empty & 1027.3 & empty &
\textbf{884.6} & \textbf{884.6} \\""", r"""Family A, \(\phi\)=0.25 & 1184.2 & empty & 1055.7 & empty &
\textbf{884.6} & \textbf{884.6} \\"""))

EDITS.append(("T1 A0.50", r"""Family A, \(\phi\)=0.50 & 1111.3 & empty & 1071.7 & empty &
\textbf{884.6} & \textbf{884.6} \\""", r"""Family A, \(\phi\)=0.50 & 1234.7 & empty & 1100.9 & empty &
911.3 & 1314.8 \\"""))

EDITS.append(("T1 A0.75", r"""Family A, \(\phi\)=0.75 & 1161.0 & empty & 1119.9 & empty & 920.2 &
empty \\""", r"""Family A, \(\phi\)=0.75 & 1288.0 & empty & 1149.8 & empty & 954.7 &
empty \\"""))

EDITS.append(("T1 Bgraded2", r"""Family B, graded2 & 1073.8 & empty & 1037.2 & empty & \textbf{884.6} &
\textbf{884.6} \\""", r"""Family B, graded2 & 1216.6 & empty & 1064.9 & empty & 886.7 &
900.3 \\"""))

EDITS.append(("T1 Bgraded3", r"""Family B, graded3 & 1073.8 & empty & 1010.9 & empty & \textbf{884.6} &
\textbf{884.6} \\""", r"""Family B, graded3 & 1189.9 & empty & 1064.9 & empty & \textbf{884.6} &
\textbf{884.6} \\"""))

# ------------------------------------------------- K-grid q05-vacuous cell
EDITS.append(("Kgrid q05 cell", r"""5000 (registered) & 0.2369 & 296.1 & 1.153 & \textbf{57.6} & 884.6 &
884.6 & \textbf{no} \\""", r"""5000 (registered) & 0.2369 & 296.1 & 1.153 & \textbf{57.6} & 884.6 &
884.6 & \textbf{yes} \\"""))

# ---------------------------------------------------------------- Table 3
EDITS.append(("T3 zero", r"""zero catch & 0.906 & 0.862 & 0.958 & 1.000 \\""",
              r"""zero catch & 0.870 & 0.807 & 0.949 & 1.000 \\"""))
EDITS.append(("T3 BAU", r"""BAU (5 kt) & 0.903 & 0.857 & 0.955 & 1.000 \\""",
              r"""BAU (5 kt) & 0.859 & 0.807 & 0.941 & 1.000 \\"""))
EDITS.append(("T3 60kt", r"""60 kt / S1 / cascade & 0.835 & 0.816 & 0.899 & 1.000 \\""",
              r"""60 kt / S1 / cascade & 0.766 & 0.784 & 0.873 & 0.999 \\"""))
EDITS.append(("T3 120kt", r"""120 kt & 0.647 & 0.650 & 0.766 & 0.996 \\""",
              r"""120 kt & 0.580 & 0.585 & 0.732 & 0.990 \\"""))

# ------------------------------------------------------------- G: abstract
EDITS.append(("abstract", r"""identity; the 5th- and 10th-percentile classes are informative.""",
              r"""identity; so does the 5th-percentile class (\(-318.8\) kt), which leaves the
10th-percentile class the only informative class."""))

# ------------------------------------------------------------- A: section 3.2
EDITS.append(("S3.2 critical floor", r"""\(\bar e = g_{\max} = 296.1\) kt yr\(^{-1}\) separates vacuous from
informative classes. Only the perpetual-worst floor (\(-460.0\) kt) sits
beyond it and is vacuous. The 5th-percentile (\(-318.8\) kt) and
10th-percentile (\(-114.9\) kt) floors both lie on the informative side,
which is why the constructive boundary of Section 3.3 exists for the
10th-percentile class and the 5th-percentile class now carries
informative, non-vacuous content.""",
              r"""\(\bar e = g_{\max} = 296.1\) kt yr\(^{-1}\) separates vacuous from
informative classes, and two of the three floors sit beyond it: the
perpetual-worst floor (\(-460.0\) kt) and the 5th-percentile floor
(\(-318.8\) kt). Both are vacuous. Only the 10th-percentile floor
(\(-114.9\) kt) lies on the informative side, which is why the
constructive boundary of Section 3.3 exists for the 10th-percentile
class alone. The 5th-percentile class is vacuous only at the infinite
horizon and by the same identity; its finite-horizon kernels are
nonempty and remain substantive (Table 1)."""))

# -------------------------------------------------------- fig1 caption
EDITS.append(("fig1 caption", r"""\caption{Surplus production of the registered fit with the three persistent floors; only the perpetual-worst floor sits beyond \(g_{\max} = 296.1\) kt yr\(^{-1}\), so only that floor's emptiness is vacuous.}""",
              r"""\caption{Surplus production of the registered fit with the three persistent floors. The perpetual-worst (\(-460.0\) kt) and 5th-percentile (\(-318.8\) kt) floors both sit beyond \(g_{\max} = 296.1\) kt yr\(^{-1}\) and are vacuous at the infinite horizon; only the 10th-percentile floor (\(-114.9\) kt) is informative.}"""))

# -------------------------------------------------------- B: note 3.2 (part 1)
EDITS.append(("note3.2 p1", r"""boundary or the stochastic layer. Under the 5th-percentile and
10th-percentile classes the statement is not vacuous: those floors lie
below the map's maximum surplus and the classes carry informative
content.""",
              r"""boundary or the stochastic layer. Under the 10th-percentile class the
statement is not vacuous: that floor lies below the map's maximum
surplus and the class carries informative content. Under the
5th-percentile class the statement is vacuous at the infinite horizon
and by the same identity, although that class's finite-horizon kernels
are nonempty and carry substantive content."""))

# -------------------------------------------------------- B: note 3.2 (part 2)
EDITS.append(("note3.2 p2", r"""below \(g_{\max}\) and are not vacuous: their kernels carry substantive
content (Table 1, Result 3.3), and the 5th-percentile moratorium kernel
is nonempty (\(2219.6\) kt). The correction of the residual convention
therefore reduces the vacuous family from two classes to one. The""",
              r"""below \(g_{\max}\) and is not vacuous: its kernels carry substantive
content (Table 1, Result 3.3). The 5th-percentile class (\(-318.8\) kt
yr\(^{-1}\)) also exceeds \(g_{\max}\): at \(T = \infty\) the kernel of
every policy, the moratorium included, is empty (Table 1), while at
finite horizons it is nonempty. The registered disturbance classes
therefore leave two of the three classes vacuous and the
10th-percentile class the only informative one. The"""))

# -------------------------------------------------------- C: K-grid reading
EDITS.append(("Kgrid reading", r"""  The vacuity structure is \(K\)-dependent in the source-year
  convention. The perpetual-worst floor is vacuous at every in-box
  \(K\), but the 5th-percentile class is vacuous only at \(K \le 4000\)
  kt and becomes informative at \(K \ge 5000\) kt (\(g_{\max} = 296.1\)
  kt at the registered \(K\)), which is itself the registered point.""",
              r"""  The vacuity structure is \(K\)-dependent. The perpetual-worst floor
  is vacuous at every in-box \(K\), and so is the 5th-percentile class:
  at the registered \(K = 5000\) kt, \(g_{\max} = 296.1\) kt still falls
  short of the \(318.8\) kt floor, and the grid first reports that class
  informative at \(K = 7000\) kt, outside the declared box."""))

# -------------------------------------------------------- D: discussion
EDITS.append(("discussion", r"""catch included --- holds the LRP. Under the 5th-percentile floor the
statement is no longer vacuous: in the source-year convention that floor
lies below the maximum surplus, and the moratorium's \(T=\infty\) kernel
is nonempty (\(2219.6\) kt). The certified-layer emptiness beyond
\(T = 6\) years (Section 3.4) is a different statement, about the
conversion's expansive form: the governed map's expansion rate
(\(F' = 1.153\) at the LRP) empties every certified kernel beyond seven
years. Neither result paraphrases the other. The vacuous-class""",
              r"""catch included --- holds the LRP. Under the 5th-percentile floor the
statement is vacuous as well and by the same identity: that floor also
exceeds the maximum surplus, and at \(T = \infty\) the moratorium's
kernel is empty (Table 1), so the 5th-percentile reading survives only
at finite horizon. The certified-layer emptiness beyond \(T = 6\) years
(Section 3.4) is a different statement, about the conversion's expansive
form: the governed map's expansion rate (\(F' = 1.153\) at the LRP)
empties every certified kernel beyond six years. Neither result
paraphrases the other. The vacuous-class"""))

EDITS.append(("discussion forms", r"""and its 5th-percentile half is not, that class being informative on both
forms.""",
              r"""and its 5th-percentile half is not exempt: that class is vacuous on the
registered form, where its \(T = \infty\) kernels are empty, but
informative on the depensatory refit, whose moratorium kernel at
\(T = \infty\) is nonempty (\(1067.6\) kt)."""))

# -------------------------------------------------------- E: limitations
EDITS.append(("limitations", r"""perpetual floor, not an independent draw). The 10th-percentile class is
the mildest with non-vacuous content, and only the perpetual-worst floor
sits beyond the map's maximum surplus (Section 3.2), which is what makes
its emptiness vacuous as a productivity statement.""",
              r"""perpetual floor, not an independent draw). The 10th-percentile class is
the only class with non-vacuous content; it is the perpetual-worst and
5th-percentile floors that sit beyond the map's maximum surplus
(Section 3.2), which is what makes their emptiness vacuous as a
productivity statement at the infinite horizon."""))

# -------------------------------------------------------- F: note A
EDITS.append(("note A", r"""\emph{Definitional note A (identity).} Only the perpetual-worst floor is
vacuous, and that vacuity is an arithmetic identity of the declared
class --- the floor exceeds the map's maximum surplus, so every
trajectory declines for every catch, zero included --- not an empirical
finding about Northern cod productivity (Section 3.2's note). The
5th-percentile and 10th-percentile classes are informative, and the
5th-percentile moratorium kernel is nonempty (\(2219.6\) kt).""",
              r"""\emph{Definitional note A (identity).} Two of the three floors are
vacuous --- the perpetual-worst and the 5th-percentile --- and that
vacuity is an arithmetic identity of the declared classes: each exceeds
the map's maximum surplus, so at \(T = \infty\) every trajectory
declines for every catch, zero included. It is not an empirical finding
about Northern cod productivity (Section 3.2's note). Only the
10th-percentile class is informative; the 5th-percentile class carries
substantive content at finite horizons only."""))

# -------------------------------------------------------- Data availability
EDITS.append(("dataavail", r"""Re-executing the source-year intervention runner regenerates both output
files (the results archive and the kernel-boundary table); a
verification re-execution in a fresh environment reproduced every
reported value to nine significant figures; the trailing digits of the
floating-point fields differ by about one part in \(10^{9}\) across BLAS
builds and are not byte-identical. In the source-year convention the flat-180-kt policy's""",
              r"""Re-executing the registered intervention runner
(\texttt{wave\_e\_cod/src/run\_intervention\_v2.py}) regenerates both
output files (the results archive and the kernel-boundary table); a
verification re-execution in a fresh environment reproduced every
reported value to nine significant figures; the trailing digits of the
floating-point fields differ by about one part in \(10^{9}\) across BLAS
builds and are not byte-identical. The reported disturbance classes are
those of the registered fit itself (\(-460.03\), \(-318.76\) and
\(-114.85\) kt yr\(^{-1}\), residual SD \(134.96\)); an earlier
source-year runner carried a different residual convention and its
numbers are superseded and not reported here. Under the registered
classes the flat-180-kt policy's"""))

EDITS.append(("dataavail figs", r"""Sections 3.7--3.10 (carrying-capacity grid, stochastic viability,
finite-duration floors, bootstrap bands, and Figures 1--7) are produced
by the repository script rerun\_campaigns/campaign\_e2\_elevation.py
with fixed seeds, and their outputs are archived alongside it;
re-execution regenerates them exactly.""",
              r"""Sections 3.7--3.10 (carrying-capacity grid, stochastic viability,
finite-duration floors, bootstrap bands) are produced by the repository
script rerun\_campaigns/campaign\_e2\_elevation.py with fixed seeds, and
their outputs are archived alongside it; re-execution regenerates them
exactly. The reactive-family rows of Table 1 are produced by
\texttt{wave\_e\_cod/src/run\_families\_v2.py}, which writes
\texttt{e2\_families\_v2.csv}. Figures 1--7 are rendered from those
archived outputs by \texttt{wave\_e\_cod/src/make\_figs\_v16.py}; that
renderer is the only step not re-executed by the runners named above."""))

# ---------------------------------------------------------------- apply
applied, failed = [], []
for label, old, new in EDITS:
    if old in tex:
        n = tex.count(old)
        tex = tex.replace(old, new)
        applied.append((label, n))
    else:
        failed.append(label)

open(DST, "w", encoding="utf-8").write(tex)

print(f"applied {len(applied)}/{len(EDITS)} edits -> {DST}")
for label, n in applied:
    print(f"  OK   {label}  ({n} occurrence{'s' if n != 1 else ''})")
for label in failed:
    print(f"  MISS {label}")

# ---------------------------------------------------- residual token sweep
print("\nresidual sweep (superseded tokens that should now be gone):")
RESID = ["2219.6", "2070.9", "1025.5", "989.0", "1233.5", "1196.4", "1180.0",
         "1143.1", "1126.8", "1090.1", "909.3", "1082.3", "1073.8", "1037.2",
         "1010.9", "1021.1", "984.7", "1064.7", "1111.3", "1161.0", "1027.3",
         "1071.7", "1119.9", "920.2", "1014.0", "961.5", "1637.8",
         "0.906", "0.862", "0.958", "0.903", "0.857", "0.955",
         "0.835", "0.816", "0.899", "0.647", "0.650", "0.766", "0.996"]
for tok in RESID:
    # boundary-safe: not preceded by digit or dot, not followed by digit
    hits = len(re.findall(r"(?<![\d.])" + re.escape(tok) + r"(?!\d)", tex))
    if hits:
        print(f"  STILL PRESENT  {tok}  x{hits}")

print("\n'seven' occurrences remaining:", len(re.findall(r"\bseven\b", tex)))
for m in re.finditer(r"\bseven\b", tex):
    line = tex[:m.start()].count("\n") + 1
    print(f"  line {line}: ...{tex[max(0,m.start()-70):m.start()+40]}...".replace("\n", " "))
