#!/usr/bin/env python3
"""v29g -- prose-coherence pass (the end-to-end read).

Eight edits.  Each one is a plain string replacement asserted to hit exactly
once, and every end marker is searched FROM THE START POSITION (an earlier
end-marker bug duplicated 1,112 lines of this file).

Nothing here touches a table cell.  What changes is prose that had stopped
being true:

  E1  Section 2.3 claimed "the whole analysis" was computed under delta = 1.
      Only the primary runner and its outputs are archived that way.
  E2  Result 3.6 asserted the constructive bound is "unaffected" by the Allee
      refit without saying what it becomes.  It rises: 196.06 - 80.87 = 115.2.
  E3  Section 3.6 quoted Fox cells that Table 2 does not carry, without saying
      so.  They are real (the campaign computes them); now labelled.
  E4  The grid-vs-interval note said "every other cell agrees to about 0.03
      kt".  Measured: 72 finite-horizon cells differ by <= 0.055 kt, five of
      the nine T=inf cells agree exactly, four differ by 0.14/0.30/0.58/0.90.
  E5  Section 3.8 -- the real one.  "The P >= 0.9 bar is not attained by any
      tested constant catch" is FALSE on the v3 pool (zero catch is 0.906;
      the i.i.d. crossing is 13.5 kt).  It was true on the v2 pool (0.868) and
      survived the migration with only the numbers swapped.  The "capping"
      clause also mixed two seeds and named a mechanism that does not follow
      from 1/24 alone, and the same 0.84/0.85 quantity was printed twice with
      two different values.  The whole passage is rewritten, with the
      mechanism measured rather than asserted.
  E6  Conclusions item 1 echoed the 0.85 of the duplicated sentence (0.84).
  E7  Code availability still named the v24 verification script.
  E8  Abstract said the class-vacuity reading "reverses"; the rest of the
      paper says it "narrows".
"""
import io
import os
import sys

TEX = "/home/user/fam/e2/paperE2_cod_intervention_v29.tex"
BAK = "/tmp/v29f_before_prose.tex"

tex = io.open(TEX, encoding="utf-8").read()
orig = tex

EDITS = []

# ---------------------------------------------------------------- E1
EDITS.append((
    "The sensitivity is not suppressed: the whole analysis was also computed\n"
    "under \\(\\delta = 1\\), and those artifacts are archived with the superseded\n"
    "runner rather than overwritten, so every affected number can be read off\n"
    "the archive instead of taken on trust. ",
    "The sensitivity is not suppressed: the primary kernels and their boundary\n"
    "tables were also computed under \\(\\delta = 1\\), and those artifacts are\n"
    "archived with the superseded runner rather than overwritten, so every\n"
    "affected number can be recomputed from the archive instead of taken on\n"
    "trust. "))

# ---------------------------------------------------------------- E2
EDITS.append((
    "The constructive boundary of Section 3.3 and the\n"
    "dominance verdict of Section 3.2 are therefore unaffected. ",
    "The constructive boundary of Section 3.3 and the\n"
    "dominance verdict of Section 3.2 are therefore unaffected --- indeed the\n"
    "constructive bound rises, since at the declared 10th-percentile floor the\n"
    "Allee form gives \\(g(K^*) - |e_{q10}| = 196.06 - 80.87 = 115.2\\) kt\n"
    "(\\(123.3\\) kt on the declared-strength row), so the \\(91.59\\) kt\n"
    "certificate holds a fortiori. The clause-(H1) block itself changes shape\n"
    "without changing the verdict: under the Allee form the 60-kt rules are no\n"
    "longer empty at the 5th-percentile \\(T=\\infty\\) reading (their boundary\n"
    # NB: E10 later retargets this clause; this entry carries the FINAL wording
    # so the script's idempotence test still recognises it.
    "is \\(1131.1\\) kt against BAU's \\(1020.9\\) kt), so the block operates through "
    "a margin rather than\nthrough emptiness at that reading. "))

# ---------------------------------------------------------------- E3
EDITS.append((
    "The 60-kt rule's infinite-horizon lower boundary\n"
    "is empty under the 5th-percentile floor. The 120-kt rule is empty under\n"
    "the 5th-percentile and perpetual-worst floors and, under the\n"
    "informative floor, at \\(T=\\infty\\) (its \\(T=1\\) boundary there is\n"
    "\\(922.7\\) kt). ",
    "Three further Fox cells are computed by the campaign but not carried in\n"
    "Table 2: the 60-kt rule's infinite-horizon lower boundary is empty under\n"
    "the 5th-percentile floor, and the 120-kt rule is empty under the\n"
    "5th-percentile and perpetual-worst floors and, under the informative\n"
    "floor, at \\(T=\\infty\\) (its \\(T=1\\) boundary there is \\(922.7\\) kt). "))

# ---------------------------------------------------------------- E4
EDITS.append((
    "Second, the Allee and Fox rows are computed\n"
    "on a \\(0.05\\) kt state grid, while the registered row comes from the\n"
    "committed interval-arithmetic engine. Adjacent to the repelling boundary,\n"
    "where \\(F' > 1\\), the grid's rounding compounds along the orbit and a grid\n"
    "boundary can sit up to \\(1\\) kt below the interval-arithmetic one:\n"
    "\\(2218.75\\) against \\(2219.649\\) kt for the BAU q05 \\(T=\\infty\\)\n"
    "boundary, and \\(2070.30\\) against \\(2070.884\\) kt for zero catch. The two\n"
    "engines are therefore not to be compared at \\(0.1\\) kt resolution; the\n"
    "tolerance the campaign declares is \\(1.0\\) kt, and every other cell the\n"
    "campaign checks agrees to about \\(0.03\\) kt.\n",
    "Second, the Allee and Fox rows are computed\n"
    "on a \\(0.05\\) kt state grid, while the registered row comes from the\n"
    "committed interval-arithmetic engine; the campaign reproduces the\n"
    "registered row on that same grid, so the two engines can be read against\n"
    "each other. At finite horizons they agree to within about one grid step\n"
    "--- of the \\(81\\) cells the campaign checks, the \\(72\\) finite-horizon\n"
    "ones differ by at most \\(0.06\\) kt --- but adjacent to the repelling\n"
    "boundary, where \\(F' > 1\\), the grid's rounding compounds along the orbit:\n"
    "at \\(T = \\infty\\) five of the nine cells agree exactly and the other\n"
    "four differ by \\(0.1\\), \\(0.3\\), \\(0.6\\) and \\(0.9\\) kt, the largest\n"
    "being the BAU q05 boundary, \\(2218.75\\) against \\(2219.649\\) kt (and\n"
    "\\(2070.30\\) against \\(2070.884\\) kt for zero catch). The two engines are\n"
    "therefore not to be compared at \\(0.1\\) kt resolution, and the tolerance\n"
    "the campaign declares is \\(1.0\\) kt.\n"))

# ---------------------------------------------------------------- E5
EDITS.append((
    "The constructive boundary of Section 3.3 carries a stochastic reading.\n"
    "At \\(C = 91.59\\) kt the 20-year survival probability from the LRP is\n"
    "\\(0.74\\) under i.i.d. draws, \\(0.73\\) under blocks, and \\(0.84\\) when\n"
    "the 1992 residual is removed. The \\(P \\ge 0.9\\) bar is not attained by\n"
    "any tested constant catch under i.i.d. or block resampling --- the 1992\n"
    "draw recurs with probability \\(1/24\\) per year, capping i.i.d. survival\n"
    "at \\(0.906\\) and block survival at \\(0.849\\) --- and it is met only when\n"
    "the 1992 draw is removed, where the crossing is \\(78.9\\) kt\n"
    "(interpolated). The \\(P \\ge 0.8\\) crossings are \\(81.2\\) kt (i.i.d.),\n"
    "\\(72.3\\) kt (blocks), and \\(105.2\\) kt (no-1992). The one-off treatment\n"
    "of 1992 is a declared sensitivity, not an identified break. At the\n"
    "constructive bound itself (\\(91.59\\) kt) the 20-year survival probability\n"
    "from the LRP falls to \\(0.74\\) under i.i.d. draws (\\(0.73\\) under\n"
    "blocks, \\(0.85\\) without the 1992 draw), so the stochastic reading of\n"
    "the bound is a survival probability of roughly three-quarters rather\n"
    "than the near-certainty that holds at moratorium-level removals. The\n"
    "constructive bound of \\(91.59\\) kt puts the worst-case reading of the\n"
    "boundary below the 60-kt flat-cap family, while the stochastic layer\n"
    "shows the survival probability falls steadily across that range\n"
    "(\\(0.91\\) at zero-to-moratorium removals to \\(0.65\\) at \\(120\\) kt).",
    "The constructive boundary of Section 3.3 carries a stochastic reading.\n"
    "At the grid catch nearest the bound (\\(92.5\\) kt on the campaign's\n"
    "\\(2.5\\) kt grid) the 20-year survival probability from the LRP is\n"
    "\\(0.74\\) under i.i.d. draws, \\(0.73\\) under block resampling and\n"
    "\\(0.84\\) when the 1992 draw is removed --- roughly three-quarters, not\n"
    "the near-certainty that holds at moratorium-level removals.\n"
    "\n"
    "The \\(P \\ge 0.9\\) bar separates the two resampling schemes. Under i.i.d.\n"
    "resampling it is attained, but only by near-moratorium catches: the\n"
    "interpolated crossing is \\(13.5\\) kt against a ceiling of \\(0.906\\) at\n"
    "zero catch (Table 4), and by \\(60\\) kt survival has already fallen to\n"
    "\\(0.835\\). Under block resampling it is not attained at all, the ceiling\n"
    "there being \\(0.852\\) (Table 4; \\(0.849\\) in the crossing sweep, which\n"
    "carries its own fixed seed --- a Monte-Carlo difference of \\(0.003\\) at\n"
    "\\(N = 20{,}000\\)); blocks of four preserve the residual autocorrelation\n"
    "of Section 2.1, so a poor year tends to be followed by another. Removing\n"
    "the 1992 draw lifts that crossing to \\(78.9\\) kt. The \\(P \\ge 0.8\\)\n"
    "crossings are \\(81.2\\) kt (i.i.d.), \\(72.3\\) kt (blocks) and \\(105.2\\)\n"
    "kt (no-1992). The one-off treatment of 1992 is a declared sensitivity,\n"
    "not an identified break.\n"
    "\n"
    "Two properties of the pool explain the ceiling. First, failures are\n"
    "concentrated at the start of the horizon: the chance of an immediate breach is \\(2/24 = 0.083\\) against a\n"
    "total failure probability of \\(0.094\\), and \\(99\\%\\) of failures occur\n"
    "within the first three years. The reason is that from the reference point\n"
    "the stock is one year's growth from safety --- under zero catch a draw\n"
    "worse than \\(-172.5\\) kt breaches the LRP at once, and two of the\n"
    "twenty-four residuals are worse than that, the 1992 draw (\\(-329.0\\)\n"
    "kt) and one other (\\(-323.5\\) kt). Second, a draw of that magnitude is\n"
    "harmless once\n"
    "the stock has grown past about \\(1020\\) kt, roughly a year later, which\n"
    "is why the ceiling is \\(0.906\\) and not the \\(0.43\\) that the \\(1/24\\)\n"
    "recurrence alone would suggest: the probability of escaping the 1992 draw\n"
    "for twenty years is \\((23/24)^{20} = 0.427\\), and that would be the\n"
    "ceiling only if every 1992 draw were fatal.\n"
    "\n"
    "The constructive bound of \\(91.59\\) kt sits above the 60-kt flat-cap\n"
    "family, so those rules are robust in the worst case, while the stochastic\n"
    "layer shows the survival probability falling steadily across that range\n"
    "(\\(0.91\\) at zero-to-moratorium removals to \\(0.65\\) at \\(120\\) kt)."))

# ---------------------------------------------------------------- E6
EDITS.append((
    "resampling, \\(0.85\\) with the 1992 draw removed), so the operational",
    "resampling, \\(0.84\\) with the 1992 draw removed), so the operational"))

# ---------------------------------------------------------------- E7
EDITS.append((
    "The verification script\n"
    "\\texttt{paperE2\\_cod\\_intervention\\_v24\\_verification.py} recomputes\n"
    "the fit, the surplus at the reference point, the three erosion\n"
    "constants and the constructive bound from the locked input files and\n"
    "compares them against the values this manuscript prints; it is archived\n"
    "alongside this manuscript.",
    "The verification script\n"
    "\\texttt{paperE2\\_cod\\_intervention\\_v29\\_verification.py} recomputes the\n"
    "fit, the floor classes, the kernel tables, the constructive bound, the\n"
    "certified horizon and the form-comparison rows from the archived campaign\n"
    "outputs and compares them against every value this manuscript prints; it\n"
    "is archived alongside this manuscript together with the mutation harness\n"
    "\\texttt{paperE2\\_cod\\_intervention\\_v29\\_sabotage.py} and the\n"
    "numeric-provenance audit\n"
    "\\texttt{paperE2\\_cod\\_intervention\\_v29\\_basis\\_audit.py}."))

# ---------------------------------------------------------------- E8
EDITS.append((
    "certificates intact; only the class-vacuity\nreading reverses.",
    "certificates intact; only the class-vacuity\nreading narrows."))

# ---------------------------------------------------------------- E9
EDITS.append((
    "In the source-year convention the flat-180-kt policy's\n"
    "\\(T=\\infty\\) boundary (Table 1) is empty under the 5th-percentile class,\n"
    "so no converged fixed point is reported for it; the registered\n"
    "finite-horizon values follow the same recursion with the corrected\n"
    "floors (computed by a runner with the iteration cap raised to\n"
    "\\(20{,}000\\) and an explicit convergence assertion). ",
    "In the source-year convention the flat-180-kt policy's\n"
    "\\(T=\\infty\\) boundary (Table 1) is empty under the 5th-percentile class,\n"
    "so no converged fixed point is reported for it; the runner raises the\n"
    "fixpoint iteration cap to \\(20{,}000\\) and refuses to return an\n"
    "unconverged iterate, which an earlier \\(300\\)-iteration cap did silently\n"
    "on exactly this row. "))

# ---------------------------------------------------------------- E10
# "universal emptiness" is already used in Section 3.5 in a different sense;
# reusing it here made the phrase ambiguous to check (a mutation of this
# sentence stayed green because the Section 3.5 occurrence survived).
EDITS.append((
    "so the block operates by\nmargin rather than by universal emptiness.",
    "so the block operates through a margin rather than\nthrough emptiness at that reading."))

# ---------------------------------------------------------------- E11
# Wording only: no number moves. Three antecedents were loose after the
# paragraph was split in two.
EDITS.append((
    "Two properties of the pool set the ceiling, and both were measured\n"
    "rather than assumed. First, failures are concentrated at the start of the\n"
    "horizon:",
    "Two properties of the pool explain the ceiling. First, failures are\n"
    "concentrated at the start of the horizon:"))
EDITS.append((
    "Removing\nthe 1992 draw lifts the crossing to \\(78.9\\) kt.",
    "Removing\nthe 1992 draw lifts that crossing to \\(78.9\\) kt."))
EDITS.append((
    "Second, the same draw is harmless once\nthe stock has grown past about",
    "Second, a draw of that magnitude is harmless once\nthe stock has grown past about"))

def norm(s):
    """Whitespace-collapsed form. Later edits in this list (and a rewrap of one
    paragraph to the source's 72-column style) change the line breaks of an
    earlier edit's result, so the idempotence test has to be line-break blind
    -- otherwise the script aborts on a file that is already correct."""
    return " ".join(s.split())


for i, (old, new) in enumerate(EDITS, 1):
    n = tex.count(old)
    if n == 0 and norm(new) in norm(tex):
        print("E%d already applied -- skipped" % i)
        continue
    if n != 1:
        sys.exit("E%d: anchor matched %d times (expected 1); aborting" % (i, n))
    # every edit is a literal splice: ONE occurrence, replaced in place
    tex = tex.replace(old, new, 1)
    print("E%d applied" % i)

if tex == orig:
    print("nothing to do -- the tex already carries every edit")
    sys.exit(0)
assert tex != orig
io.open(BAK, "w", encoding="utf-8").write(orig)
io.open(TEX, "w", encoding="utf-8").write(tex)
print("backup ->", BAK)
print("lines %d -> %d" % (orig.count("\n") + 1, tex.count("\n") + 1))
