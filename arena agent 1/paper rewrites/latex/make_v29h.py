#!/usr/bin/env python3
"""v29h -- the structural pass.

The end-to-end read found a *reasoning* error in Result 3.4 (§3.8's reactive
criterion was the criterion for nonemptiness, used to justify a claim about the
whole safe set).  Chasing it produced something better than a fix: on the
increasing branch of the surplus curve the entire kernel table reduces to three
constants, and the no-dominance verdict follows from an identity rather than
from a tabulation.  That is the novelty a top journal asks for, and it is cheap
to state because it is exact.

This script:

  H1  inserts Section 2.4 -- four propositions with one-line proofs, each
      verified against the committed artifacts by campaign_e2_structure_v3.py
      (23/23 checks).
  H2  adds the phi = 0.60 row to Table 1, so the table exhibits all three
      regimes of Proposition 2.3 (run_families_v3.py was re-run to produce it).
  H3  explains Table 1's last column by the two constants (Proposition 2.2).
  H4  states the protection-supply budget identity in Section 3.3.
  H5  rewrites Result 3.4's Reason: two thresholds, three regimes, correct
      margins (48.5 / 5.4 / -37.8 kt), and the correction recorded openly.
  H6  states the certified horizon as an exact crossing (Proposition 2.4).

Nothing here changes a cell of Tables 2-6.
"""
import io
import sys

TEX = "/home/user/fam/e2/paperE2_cod_intervention_v29.tex"
BAK = "/tmp/v29g_before_structural.tex"
B = chr(92)

tex = io.open(TEX, encoding="utf-8").read()
orig = tex
EDITS = []

# ---------------------------------------------------------------- H1
SEC24 = """\\subsubsection{2.4 What the kernel problem reduces
to}\\label{what-the-kernel-problem-reduces-to}

The kernels of Section 3 are computed by exact backward recursion on the
declared interval engine, but they are not merely numerical. On the increasing
branch of the surplus curve --- the only branch the safe set occupies here,
since \\(K^* < K/2\\) --- the whole table reduces to three constants. Write
\\(g\\) for the surplus, \\(|e|\\) for the persistent floor, \\(C(S)\\) for the
policy's catch and \\(F(S) = S + g(S) - C(S) - |e|\\) for the worst-case closed
loop. Every statement below is verified cell by cell against the committed
kernels by \\texttt{campaign\\_e2\\_structure\\_v3.py} (23 checks).

\\textbf{Proposition 2.1 (Constructive bound and the protection--supply
budget).} For any policy whose catch at the reference point is \\(C(K^*)\\),
the safe set is held from itself if and only if
\\(C(K^*) \\le C^* := g(K^*) - |e|\\), and the margin by which it is held is
exactly \\(C^* - C(K^*)\\).

\\emph{Proof.} One step from \\(K^*\\) gives
\\(K^* + g(K^*) - C(K^*) - |e|\\), which is at least \\(K^*\\) under exactly the
stated inequality; and because \\(S \\mapsto S + g(S) - C(S)\\) is increasing on
the safe set for every declared policy, invariance at the reference point is
invariance of the whole set. The margin is the difference of the two sides.
\\ensuremath{\\square}

The largest catch that holds the reference point from itself is therefore
\\(C^* = 172.46 - 80.87 = 91.59\\) kt (Section 3.3). The identity is the
substantive part: at the reference point harvest and protection are one
budget, and every kilotonne taken there is a kilotonne of margin surrendered.
Section 3.2 shows that this, and not the tabulation, is why no declared rule
dominates the moratorium.

\\textbf{Proposition 2.2 (Perpetual bound and the infinite-horizon
boundary).} For a constant catch \\(C\\), the \\(T=\\infty\\) kernel is
\\([b_\\infty, \\infty)\\) with \\(b_\\infty = \\max(K^*, s_-(C))\\), where
\\(s_-(C)\\) is the smaller root of \\(g(S) = C + |e|\\); it is empty if and only
if \\(C > C_{\\mathrm{vac}} := g_{\\max} - |e|\\).

\\emph{Proof.} \\(F(S) - S = g(S) - C - |e|\\) is positive exactly between the
two roots of \\(g(S) = C + |e|\\). From any state above the smaller root the
trajectory increases towards the larger and so never falls below the smaller;
from any state below it the trajectory declines. If \\(C + |e| > g_{\\max}\\)
there is no root and the trajectory declines everywhere. \\ensuremath{\\square}

Two constants therefore organise the last column of Table 1: below
\\(C^* = 91.59\\) kt the kernel is the whole safe set; between \\(C^*\\) and
\\(C_{\\mathrm{vac}} = 296.09 - 80.87 = 215.2\\) kt it is a proper half-line
strictly above the reference point; above \\(C_{\\mathrm{vac}}\\) it is empty.
The column is reproduced in closed form to \\(0.1\\) kt for all six flat caps.

\\textbf{Proposition 2.3 (Reactive families).} For \\(C(S) = \\phi\\, g(S)\\)
above the LRP and 0 below, the closed loop is
\\(F(S) = S + (1-\\phi)\\,g(S) - |e|\\) and there are three regimes: the kernel
is the whole safe set iff \\(\\phi \\le 1 - |e|/g(K^*)\\); it is a proper
half-line iff that fails but \\(\\phi < 1 - |e|/g_{\\max}\\); and it is empty iff
\\(\\phi \\ge 1 - |e|/g_{\\max}\\).

\\emph{Proof.} Proposition 2.1 with \\(C(K^*) = \\phi\\, g(K^*)\\), and
Proposition 2.2 with the effective surplus \\((1-\\phi)g\\). \\ensuremath{\\square}

Under the declared 10th-percentile floor the two thresholds are \\(0.531\\) and
\\(0.727\\). The members \\(\\phi = 0.25\\) and \\(0.50\\) hold the entire safe
set --- the second by \\(5.4\\) kt, not by the \\(67.2\\) kt an earlier version
of this paper reported (Section 3.4) --- \\(\\phi = 0.75\\) is empty, and the
band \\(0.531 < \\phi < 0.727\\) is the regime in which the rule is viable but
only from above the reference point. No member of the originally declared
family fell in that band, which is why the erroneous criterion went unnoticed;
the family has been extended by \\(\\phi = 0.60\\) so that Table 1 exhibits it.

\\textbf{Proposition 2.4 (The certified horizon is a crossing).} Let
\\(S_{\\mathrm{hi}}\\) be the domain ceiling and
\\(r_T = \\varepsilon(a_{\\max}^T-1)/(a_{\\max}-1)\\) the erosion margin of
Definition 2.7. The certified kernel at horizon \\(T\\) is nonempty iff
\\(F^T(S_{\\mathrm{hi}}) \\ge K^* + r_T\\), and since \\(F^T(S_{\\mathrm{hi}})\\)
is nonincreasing in \\(T\\) while \\(r_T\\) increases, the certified horizon is
the unique crossing
\\(T^* = \\max\\{T : F^T(S_{\\mathrm{hi}}) \\ge K^* + r_T\\}\\). It is finite
whenever the loop is expansive.

\\emph{Proof.} \\(F\\) is increasing, so the supremum over initial states of
the \\(T\\)-step minimum is attained at the ceiling; the rest is the definition
of the certified kernel. Finiteness follows because \\(r_T\\) grows
geometrically in \\(T\\) while \\(F^T(S_{\\mathrm{hi}})\\) is bounded below (it
converges to the attracting fixed point when one exists, and declines
otherwise). \\ensuremath{\\square}

The crossing reproduces the computed horizons exactly --- \\(T^* = 6\\) under
the perpetual-worst and 5th-percentile floors and \\(T^* = 7\\) under the
informative one, for both BAU and zero catch (Section 3.4). Where the loop has
an attracting fixed point \\(S^\\dagger\\) the crossing is bounded below by
\\(\\lfloor\\log(1 + (S^\\dagger-K^*)(a_{\\max}-1)/\\varepsilon)/\\log
a_{\\max}\\rfloor\\), which is attained once the ceiling trajectory has
converged: it gives 7 against 7 under the informative floor, and 4 against 6
under the 5th-percentile floor, where at six years the ceiling trajectory is
still \\(1{,}500\\) kt above the attractor.

"""

EDITS.append((B + "subsection{3. Results}", SEC24 + B + "subsection{3. Results}"))

# ---------------------------------------------------------------- H2
EDITS.append((
    "Family A, \\(\\phi\\)=0.50 & 1111.3 & empty & 1071.7 & empty &\n"
    "\\textbf{884.6} & \\textbf{884.6} \\\\\n",
    "Family A, \\(\\phi\\)=0.50 & 1111.3 & empty & 1071.7 & empty &\n"
    "\\textbf{884.6} & \\textbf{884.6} \\\\\n"
    "Family A, \\(\\phi\\)=0.60 & 1131.2 & empty & 1091.0 & empty & 895.2 &\n"
    "1074.8 \\\\\n"))

# ---------------------------------------------------------------- H3
EDITS.append((
    "Under the 10th-percentile class the moratorium, zero catch, the flat\n"
    "60-kt cap, the critical-zone rule, the cascade, both graded rules, and\n"
    "the surplus-proportional family at \\(\\phi \\le 0.50\\) all hold the entire\n"
    "safe set \\([884.6, 10^4]\\) kt at every horizon. Every higher nonzero cap\n"
    "lifts the kernel's lower edge above the LRP.",
    "Under the 10th-percentile class the moratorium, zero catch, the flat\n"
    "60-kt cap, the critical-zone rule, the cascade, both graded rules, and\n"
    "the surplus-proportional family at \\(\\phi \\le 0.50\\) all hold the entire\n"
    "safe set \\([884.6, 10^4]\\) kt at every horizon. Every higher nonzero cap\n"
    "lifts the kernel's lower edge above the LRP, and the column is not a\n"
    "list of accidents: by Proposition 2.2 the boundary is\n"
    "\\(\\max(K^*, s_-(C))\\) with \\(s_-(C)\\) the smaller root of\n"
    "\\(g(S) = C + |e_{q10}|\\), so the catches divide at\n"
    "\\(C^* = 91.59\\) kt (whole safe set), \\(C_{\\mathrm{vac}} = 215.2\\) kt\n"
    "(nonempty) and beyond it (empty) --- which is exactly what the last column\n"
    "shows, to \\(0.1\\) kt, for all six flat caps."))

# ---------------------------------------------------------------- H4
EDITS.append((
    "This is certification geometry at one declared shock class, not a\n"
    "harvest rule.",
    "Proposition 2.1 gives the bound a second reading: the margin by which\n"
    "any policy holds the reference point is exactly \\(91.59\\) kt minus its\n"
    "catch there, so the bound is the whole budget and harvest and protection\n"
    "are the same quantity seen from two sides. This is certification\n"
    "geometry at one declared shock class, not a harvest rule."))

# ---------------------------------------------------------------- H5
EDITS.append((
    "\\emph{Reason.} For a surplus-proportional rule \\(C = \\phi\\, g(S)\\) the\n"
    "closed loop is \\(F(S) = S + (1-\\phi)\\,g(S) + e\\), a single concave\n"
    "quadratic. Under the 10th-percentile floor the loop holds the LRP from\n"
    "itself when the scaled surplus exceeds the floor:\n"
    "\\((1-\\phi)\\,g_{\\max} > |e_{q10}|\\),\n"
    "i.e.~\\(\\phi < 1 - 80.87/296.09 = 0.727\\). At \\(\\phi = 0.25\\) (\\(0.5\\))\n"
    "the criterion is \\(141.2\\) (\\(67.2\\)) kt \\(> 0\\), so the kernel is the\n"
    "whole safe set; at \\(\\phi = 0.75\\) it is \\(-6.8\\) kt, so the criterion\n"
    "fails and the \\(T=\\infty\\) kernel is empty (\\(920.2\\) kt at \\(T=1\\)).\n"
    "Under the 5th-percentile floor the criterion is \\(\\phi < 0.029\\), so no\n"
    "surplus-proportional rule with positive \\(\\phi\\) holds that class ---\n"
    "which is exactly why the same family is empty there, and why it does not\n"
    "dominate BAU under the frozen rule.",
    "\\emph{Reason.} For a surplus-proportional rule \\(C = \\phi\\, g(S)\\) the\n"
    "closed loop is \\(F(S) = S + (1-\\phi)\\,g(S) + e\\), a single concave\n"
    "quadratic, and Proposition 2.3 gives three regimes rather than two. The\n"
    "safe set is held from itself iff the scaled surplus at the reference\n"
    "point covers the floor, \\((1-\\phi)\\,g(K^*) \\ge |e_{q10}|\\), i.e.\n"
    "\\(\\phi \\le 1 - 80.87/172.46 = 0.531\\); at \\(\\phi = 0.25\\) (\\(0.50\\))\n"
    "the margin is \\(48.5\\) (\\(5.4\\)) kt, so both qualify, the second only\n"
    "just. Nonemptiness is the weaker condition\n"
    "\\((1-\\phi)\\,g_{\\max} > |e_{q10}|\\), i.e.\n"
    "\\(\\phi < 1 - 80.87/296.09 = 0.727\\), and it fails at \\(\\phi = 0.75\\)\n"
    "(margin \\(-37.8\\) kt), so that member's \\(T=\\infty\\) kernel is empty\n"
    "(\\(920.2\\) kt at \\(T=1\\)). Between the two thresholds the rule is\n"
    "viable but only from above the reference point: at the added member\n"
    "\\(\\phi = 0.60\\) the informative kernel is \\([1074.8, 10^4]\\) kt, not\n"
    "the safe set, and it is this regime that an earlier version of this paper\n"
    "missed by quoting \\(0.727\\) as the threshold for holding the safe set.\n"
    "The three tabulated verdicts were unaffected, which is why the error\n"
    "survived every numeric check. Under the 5th-percentile floor the\n"
    "criterion is \\(\\phi < 0.029\\), so no surplus-proportional rule with\n"
    "positive \\(\\phi\\) holds that class --- which is exactly why the same\n"
    "family is empty there, and why it does not dominate BAU under the frozen\n"
    "rule."))

# ---------------------------------------------------------------- H6
EDITS.append((
    "On this object the binding obstruction to certified intervention claims\n"
    "is the expansion rate itself, not the defect magnitude.",
    "Proposition 2.4 names the mechanism precisely: the certified horizon is\n"
    "the crossing at which the geometrically growing margin\n"
    "\\(K^* + r_T\\) overtakes the worst-case trajectory from the domain\n"
    "ceiling, and it reproduces the computed horizons exactly\n"
    "(\\(T^* = 6\\), 6 and 7). On this object the binding obstruction to\n"
    "certified intervention claims is the expansion rate itself, not the\n"
    "defect magnitude."))


def norm(s):
    return " ".join(s.split())


for i, (old, new) in enumerate(EDITS, 1):
    n = tex.count(old)
    if n == 0 and norm(new) in norm(tex):
        print("H%d already applied -- skipped" % i)
        continue
    if n != 1:
        sys.exit("H%d: anchor matched %d times (expected 1); aborting" % (i, n))
    tex = tex.replace(old, new, 1)
    print("H%d applied" % i)

if tex == orig:
    print("nothing to do")
    sys.exit(0)
io.open(BAK, "w", encoding="utf-8").write(orig)
io.open(TEX, "w", encoding="utf-8").write(tex)
print("backup ->", BAK)
print("lines %d -> %d" % (orig.count("\n") + 1, tex.count("\n") + 1))
