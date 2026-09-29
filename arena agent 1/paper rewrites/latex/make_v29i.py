#!/usr/bin/env python3
"""v29i -- identification, recency, and presentation.

Merits.  The paper's declared defect is that K is pinned at its optimisation
bound, and every headline result is a function of (r, K).  I1 answers the
objection without pretending to resolve it: profile K, and show that K is not
identified from above while the two functionals the results depend on are.
I2 widens the published bootstrap (which conditions the pin away by refitting r
alone) to a joint refit, and makes the paper's own "the residual conflates
process noise and observation error" declaration quantitative.

Impact.  I3 asks the question the paper otherwise leaves open: is the reference
point self-viable under *current* productivity?  The fit window spans the 1992
collapse, so the identified r averages two regimes.  The honest answer is
regime-dependent, and that is itself the finding.

Presentation.  I4 and I5 re-cut the title and abstract around the structural
result rather than around the list of computations; I6 adds the two new
findings to the conclusions; I7 names the new campaigns in Data availability.
"""
import io
import sys

TEX = "/home/user/fam/e2/paperE2_cod_intervention_v29.tex"
BAK = "/tmp/v29h_before_ident.tex"
B = chr(92)

tex = io.open(TEX, encoding="utf-8").read()
orig = tex
EDITS = []

# ---------------------------------------------------------------- I1
I1 = """
How much of that is carried by the pin? The question can be answered without
resolving it. Profiling \\(K\\) --- refitting \\(r\\) in closed form at each
fixed \\(K\\) on the same window, with the grid extended to \\(50{,}000\\)
kt precisely because the committed value sits on the box --- gives a
profile-likelihood \\(95\\%\\) set running from \\(1500\\) kt to the top of the
grid: the series never approaches carrying capacity, so \\(K\\) is not
identified from above at all. The pin itself buys little: the sum of squares at
\\(K = 5000\\) kt is \\(1.027\\) times the profiled minimum. What is identified
is everything the results depend on. Across the profile set \\(g(K^*)\\) lies
in \\([148.8, 176.1]\\) kt and \\(C^*\\) in \\([67.9, 95.2]\\) kt, so the
constructive bound is pinned to within \\(15\\%\\) by data that do not determine
\\(K\\) at all; and \\(F'(K^*) > 1\\) for every profile-set \\(K\\) at or above
\\(2K^* = 1769.2\\) kt --- the smallest expansive value on the grid is
\\(1775\\) kt --- which is exactly the condition reading (i) declares. The
expansion obstruction is conditional on \\(K \\ge 2K^*\\); it is not conditional
on the pinned value.
"""
EDITS.append((
    "\\begin{figure}[htbp]\n"
    "\\centering\n"
    "\\includegraphics[width=\\linewidth]{figs_e2_v3/fig6_k_sensitivity.png}\n"
    "\\caption{The two panels of the carrying-capacity sensitivity of Section 3.7.}\n"
    "\\end{figure}\n",
    "\\begin{figure}[htbp]\n"
    "\\centering\n"
    "\\includegraphics[width=\\linewidth]{figs_e2_v3/fig6_k_sensitivity.png}\n"
    "\\caption{The two panels of the carrying-capacity sensitivity of Section 3.7.}\n"
    "\\end{figure}\n" + I1))

# ---------------------------------------------------------------- I2
I2 = """
Refitting \\(r\\) alone at \\(K = 5000\\) kt is the narrower of the two
available bands, because it conditions the pin away rather than propagating
it. Refitting both parameters on every replicate gives \\(r\\) a median of
\\(0.261\\) (\\(90\\%\\) interval \\([0.092, 0.500]\\)), \\(K\\) a median of
\\(4191\\) kt with the pin active in \\(41.7\\%\\) of replicates, and the
constructive bound a median of \\(73.7\\) kt with \\(90\\%\\) interval
\\([-89.4, 125.7]\\) kt. The interval's negative tail is made of replicates in
which the refit places \\(K\\) below the reference point --- admissible under
the declared box, and excluded by construction when \\(K\\) is held fixed.
Restricted to the expansive regime \\(K \\ge 2K^*\\) on which the results are
conditional, the bound has median \\(88.1\\) kt (\\(90\\%\\) interval
\\([-5.6, 130.6]\\) kt) and \\(F'(K^*)\\) has median \\(1.137\\) with
\\(90\\%\\) interval \\([1.030, 1.178]\\): expansion holds throughout.

One further declared sensitivity is made quantitative here. The residual of
Section 2.1 conflates process noise and observation error, and only the process
part can act as a persistent floor. If a fraction \\(\\lambda\\) of the residual
variance is observation error, rescaling the empirical pool about its mean by
\\(\\sqrt{1-\\lambda}\\) --- its shape preserved, only its scale changed ---
moves the constructive bound from \\(91.6\\) kt at \\(\\lambda = 0\\) to
\\(112.1\\) kt at \\(\\lambda = 0.5\\), and the vacuous class disappears from
\\(\\lambda \\ge 0.2\\) onward. The reported bound is the conservative end of
that range.
"""
EDITS.append((
    "therefore best read as order \\(70\\)--\\(90\\) kt under the declared\n"
    "10th-percentile class, not as a quota figure.\n",
    "therefore best read as order \\(70\\)--\\(90\\) kt under the declared\n"
    "10th-percentile class, not as a quota figure.\n" + I2))

# ---------------------------------------------------------------- I3
I3 = """
\\subsubsection{3.12 Is the reference point self-viable under current
productivity?}\\label{is-the-reference-point-self-viable-under-current-productivity}

The fit window 1983--2007 spans the 1992 collapse, so the identified \\(r\\)
averages two productivity regimes and the floor classes average them with it.
Refitting the same object on post-moratorium windows --- same source-year
convention, same declared box, same construction throughout --- asks whether
the reference point is self-viable under recent productivity (Table 7). The
rows are labelled sensitivities in the sense of Section 3.11: no verdict
transfers between the two series, and none of these windows replaces the frozen
protocol.

\\textbf{Table 7.} The same construction on post-moratorium windows. \\(K\\)
is reported with its bound status; \\(C^*\\) is the constructive bound at each
window's own 10th-percentile floor, and the last column is the same quantity
at each window's perpetual-worst floor.

\\begin{longtable}[]{@{}
  >{\\raggedright\\arraybackslash}p{(\\columnwidth - 18\\tabcolsep) * \\real{0.0833}}
  >{\\raggedleft\\arraybackslash}p{(\\columnwidth - 18\\tabcolsep) * \\real{0.0833}}
  >{\\raggedleft\\arraybackslash}p{(\\columnwidth - 18\\tabcolsep) * \\real{0.0833}}
  >{\\raggedleft\\arraybackslash}p{(\\columnwidth - 18\\tabcolsep) * \\real{0.0833}}
  >{\\raggedleft\\arraybackslash}p{(\\columnwidth - 18\\tabcolsep) * \\real{0.0833}}
  >{\\raggedleft\\arraybackslash}p{(\\columnwidth - 18\\tabcolsep) * \\real{0.0833}}
  >{\\raggedleft\\arraybackslash}p{(\\columnwidth - 18\\tabcolsep) * \\real{0.0833}}
  >{\\raggedleft\\arraybackslash}p{(\\columnwidth - 18\\tabcolsep) * \\real{0.0833}}
  >{\\raggedleft\\arraybackslash}p{(\\columnwidth - 18\\tabcolsep) * \\real{0.0833}}
  >{\\raggedleft\\arraybackslash}p{(\\columnwidth - 18\\tabcolsep) * \\real{0.0833}}@{}}
\\toprule\\noalign{}
\\begin{minipage}[b]{\\linewidth}\\raggedright
Window
\\end{minipage} & \\begin{minipage}[b]{\\linewidth}\\raggedleft
\\(n\\)
\\end{minipage} & \\begin{minipage}[b]{\\linewidth}\\raggedleft
\\(r\\)
\\end{minipage} & \\begin{minipage}[b]{\\linewidth}\\raggedleft
\\(K\\) (kt)
\\end{minipage} & \\begin{minipage}[b]{\\linewidth}\\raggedleft
\\(g(\\mathrm{LRP})\\)
\\end{minipage} & \\begin{minipage}[b]{\\linewidth}\\raggedleft
resid.\\SD
\\end{minipage} & \\begin{minipage}[b]{\\linewidth}\\raggedleft
\\(|e_{q10}|\\)
\\end{minipage} & \\begin{minipage}[b]{\\linewidth}\\raggedleft
\\(C^*\\)
\\end{minipage} & \\begin{minipage}[b]{\\linewidth}\\raggedleft
worst-floor
\\end{minipage} & \\begin{minipage}[b]{\\linewidth}\\raggedleft
\\(F'(\\mathrm{LRP})\\)
\\end{minipage} \\\\
\\midrule\\noalign{}
\\endhead
\\bottomrule\\noalign{}
\\endlastfoot
1983--2007 (frozen) & 24 & 0.2369 & 5000 (upper) & 172.5 & 114.9 & 80.9 &
91.6 & \\(-156.5\\) & 1.153 \\\\
NCAM 1995--2015 & 20 & 0.2731 & 5000 (upper) & 198.9 & 18.9 & 27.4 & 171.4 &
166.4 & 1.176 \\\\
NCAM 1995--2007 & 12 & 0.3901 & 5000 (upper) & 284.0 & 10.6 & 10.0 & 274.0 &
271.2 & 1.252 \\\\
xteNCAM 1995--2024 & 29 & 0.4310 & 472 (lower) & 49.4 & 32.6 & 41.4 & 8.0 &
\\(-38.8\\) & 0.927 \\\\
xteNCAM 2005--2024 & 19 & 0.4439 & 472 (lower) & 50.9 & 40.4 & 58.5 & -7.7 &
\\(-37.9\\) & 0.925 \\\\
\\end{longtable}

On the assessment series the answer is yes, and more comfortably than on the
collapse window. On 1995--2015 the fit gives \\(r = 0.273\\),
\\(g(\\mathrm{LRP}) = 198.9\\) kt and a 10th-percentile floor of only
\\(27.4\\) kt --- the post-moratorium decline was smooth and therefore largely
predictable one step ahead, the residual SD falling from \\(114.9\\) kt to
\\(18.9\\) kt --- so the constructive bound rises to \\(171.4\\) kt and stays
positive under that window's perpetual-worst floor (\\(166.4\\) kt), with the
expansion at the LRP intact (\\(F' = 1.176\\)). On the shorter 1995--2007
window the bound is larger again (\\(274.0\\) kt).

On the second specification the answer is no. On xteNCAM 2005--2024 the fit
places \\(K\\) at its lower bound, \\(472\\) kt, barely above the largest
observed stock, so the fitted surplus at that specification's reference point
is \\(50.9\\) kt against a 10th-percentile floor of \\(58.5\\) kt: the
constructive bound is \\(-7.7\\) kt, and on 1995--2024 it is \\(+8.0\\) kt.
Under either window's perpetual-worst floor it is negative (\\(-37.9\\) and
\\(-38.8\\) kt). The classification reverses with it ---
\\(F'(\\mathrm{LRP}) = 0.925 < 1\\) --- so on the modern series in its recent
state the closed loop contracts at the reference point and the contraction form
of the certified-layer conversion, inapplicable on the frozen object, is the
applicable one.

Two caveats are inseparable from these rows and are stated rather than buried.
The windows are short (12--29 transitions), and in three of the four the
carrying capacity is at a bound, so these are regime readings rather than
estimates of productivity. What they establish does not depend on reading them
as estimates: the reference point's self-viability is regime-dependent ---
comfortable on the assessment series after the moratorium, and at best marginal
on the modern series, at roughly \\(0 \\pm 8\\) kt and negative under that
series' worst observed floor --- and the expansion classification moves with
it. That is consistent with Section 3.11, where the same specification's
1954--2007 fit also failed to make its reference point self-viable.

"""
EDITS.append((B + "subsection{4. Discussion}", I3 + B + "subsection{4. Discussion}"))

# ---------------------------------------------------------------- I4 (title)
EDITS.append((
    "\\title{Robust viability of the 2J3KL limit reference point under a surplus-production map: policy scoring, expansion, and when catch cannot help}",
    "\\title{A harvest--protection budget at the limit reference point: robust viability of Northern cod (NAFO 2J3KL) under persistent productivity shocks}"))

# ---------------------------------------------------------------- I5 (abstract)
OLD_ABS = tex[tex.index("\\begin{abstract}") + len("\\begin{abstract}"):tex.index("\\end{abstract}")]
NEW_ABS = """

Reference points are usually defended by simulation. Here the defence is a
characterisation: on the increasing branch of the surplus curve, the robustness
of a single-threshold reference point to persistent productivity shocks reduces
to three constants, and the kernel computation collapses to algebra. Applied to
Northern cod (NAFO 2J3KL; Schaefer fit 1983--2007; LRP \\(884.6\\) kt) under a
protocol frozen before any score was computed: (1) The largest catch holding
the reference point from itself is \\(C^* = g(\\mathrm{LRP}) - |e| = 91.59\\)
kt, and --- the identity behind every comparison here --- any rule's protection
margin is exactly \\(C^*\\) minus its catch at the reference point: at that
point harvest and protection are one budget. A second constant,
\\(g_{\\max} - |e| = 215.2\\) kt, separates viable-but-raised kernels from
empty ones, and together they reproduce the kernel table in closed form.
(2) Because of that identity the no-dominance verdict is structural, not
empirical: a reactive rule cannot out-supply a flat cap it matches in
protection. (3) The map is expansive at the reference point for every
admissible \\(K \\ge 2K^*\\), so the certified layer has a finite horizon ---
six years under the two harsher floors, seven under the informative one --- and
that horizon is the crossing at which a geometrically growing erosion margin
overtakes the worst-case trajectory. (4) Carrying capacity is not identified
from above (the profile-likelihood set runs past \\(50{,}000\\) kt), but the
functionals the results depend on are: across it, \\(C^* \\in [67.9, 95.2]\\)
kt and \\(F' > 1\\) throughout the expansive range; under joint resampling the
constructive bound is \\(88.1\\) kt \\([-5.6, 130.6]\\). (5) Self-viability is
regime-dependent: on the post-moratorium window the bound rises to
\\(171\\) kt, while on the modern series (2005--2024, LRP \\(276\\) kt) it is
\\(0 \\pm 8\\) kt and negative under that window's worst floor. On this map the
reference point is protected by good years, and reactive design cannot buy
protection with supply.

"""
EDITS.append((OLD_ABS, NEW_ABS))

# ---------------------------------------------------------------- I6 (conclusions)
EDITS.append((
    "\\item\n  The results are convention-dependent in the residual convention only",
    "\\item\n  The comparison is governed by an identity rather than by a tabulation:\n"
    "  at the reference point a rule's protection margin plus its catch equal\n"
    "  \\(91.59\\) kt exactly (Proposition 2.1), so no reactive rule can\n"
    "  out-supply a flat cap it matches in protection and the no-dominance\n"
    "  verdict of finding (2) is structural. The certified horizon is likewise\n"
    "  a crossing, not a search: six or seven years is where the geometrically\n"
    "  growing erosion margin overtakes the worst-case trajectory.\n"
    "\\item\n  The results are convention-dependent in the residual convention only"))

EDITS.append((
    "Across assessment specifications the findings are\nspecification-conditional: on the second, unpooled xteNCAM specification\n(LRP \\(276\\) kt) the expansion classification and the kernel ordering\nsurvive while the reference point's self-viability does not --- the\ncurrent stock sits between that specification's one- and five-year\nzero-catch boundaries (Section 3.11).",
    "Across assessment specifications the findings are\nspecification-conditional: on the second, unpooled xteNCAM specification\n(LRP \\(276\\) kt) the expansion classification and the kernel ordering\nsurvive while the reference point's self-viability does not --- the\ncurrent stock sits between that specification's one- and five-year\nzero-catch boundaries (Section 3.11). Across productivity regimes they are\nregime-conditional in the same way: the constructive bound is\n\\(171\\) kt on the post-moratorium assessment window and \\(0 \\pm 8\\)\nkt on the modern series (Section 3.12), so the reference point's\nself-viability is a property of the regime as much as of the rule."))

# ---------------------------------------------------------------- I7 (data availability)
EDITS.append((
    "Figures 1--7 are produced by\n\\texttt{wave\\_e\\_cod/src/make\\_figs\\_v17.py};",
    "Figures 1--7 are produced by\n\\texttt{wave\\_e\\_cod/src/make\\_figs\\_v17.py};\n"
    "the structural constants of Section 2.4 and the corrected reactive\n"
    "criterion of Section 3.4 are verified cell by cell by\n"
    "\\texttt{wave\\_e\\_cod/src/campaign\\_e2\\_structure\\_v3.py} (23 checks,\n"
    "outputs in \\texttt{src/results\\_struct\\_v3/}), and the profile\n"
    "likelihood, joint bootstrap, observation-error sensitivity and\n"
    "post-moratorium windows of Sections 3.7, 3.10 and 3.12 by\n"
    "\\texttt{wave\\_e\\_cod/src/campaign\\_e2\\_identification\\_v3.py}\n"
    "(outputs in \\texttt{src/results\\_ident\\_v3/});"))


def norm(s):
    return " ".join(s.split())


for i, (old, new) in enumerate(EDITS, 1):
    n = tex.count(old)
    if n == 0 and norm(new) in norm(tex):
        print("I%d already applied -- skipped" % i)
        continue
    if n != 1:
        sys.exit("I%d: anchor matched %d times (expected 1); aborting" % (i, n))
    tex = tex.replace(old, new, 1)
    print("I%d applied" % i)

if tex == orig:
    print("nothing to do")
    sys.exit(0)
io.open(BAK, "w", encoding="utf-8").write(orig)
io.open(TEX, "w", encoding="utf-8").write(tex)
print("backup ->", BAK)
print("lines %d -> %d" % (orig.count("\n") + 1, tex.count("\n") + 1))
