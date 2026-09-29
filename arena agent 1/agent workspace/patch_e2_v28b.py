#!/usr/bin/env python3
"""E2 v28 pass 2: correct the no-dominance mechanism and the remaining
superseded constants.

Empirical basis (all from the deposited registered-basis outputs):
  * at UC_q05 / T=inf EVERY policy's kernel is empty, BAU included
    (|q05| = 318.76 > g_max = 296.09, so the class is vacuous);
  * BAU is at least as protective as every positive-catch rule at all
    27 (class, horizon) readings and strictly more protective at 25;
  * zero catch is more protective still (better at 16, worse at 0);
  * at UC_q10 / T=inf: BAU 884.6, flat_25/S1/cpm/graded2 900.3,
    graded3 884.6, Family A phi=0.25 884.6, phi=0.50 1314.8;
  * BAU UC_q05: T=5 -> 1412.5;  flat_0 UC_q05: T=5 -> 1394.2.
"""
import re

SRC = "/home/user/fam/e2/paperE2_cod_intervention_v28.tex"
tex = open(SRC, encoding="utf-8").read()

EDITS = []

# ---- Table 2 (form comparison): registered Schaefer row uses registered classes
EDITS.append(("T2 Schaefer row", r"""Registered Schaefer & 989.0 & 2219.6 & \textbf{884.6} & empty &
\textbf{884.6} \\""", r"""Registered Schaefer & 1016.5 & empty & \textbf{884.6} & empty &
900.3 \\"""))

# ---- Family A phi=0.75 q10 T=1: 920.2 -> 954.7 (two occurrences)
EDITS.append(("A0.75 T1 (a)", r"""its \(T=\infty\) kernel empty (\(920.2\) kt at \(T=1\) against""",
              r"""its \(T=\infty\) kernel empty (\(954.7\) kt at \(T=1\) against"""))
EDITS.append(("A0.75 T1 (b)", r"""fails and the \(T=\infty\) kernel is empty (\(920.2\) kt at \(T=1\)).""",
              r"""fails and the \(T=\infty\) kernel is empty (\(954.7\) kt at \(T=1\))."""))

# ---- Site 1: why the filter vocabulary is not used
EDITS.append(("site1", r"""comparison that could go either way: under the 5th-percentile class at
\(T=\infty\) every declared positive-catch rule has an empty kernel
while BAU's is nonempty (\(2219.6\) kt), so within the declared family
no positive-catch rule can satisfy (H1) at all --- the rule's outcome is
fixed by the declared classes and BAU's marginal nonemptiness there.""",
              r"""comparison that could go either way: at the registered classes BAU is
at least as protective as every declared positive-catch rule at all 27
(class, horizon) readings and strictly more protective at 25 of them,
while zero catch is more protective still. So within the declared
family no positive-catch rule can satisfy (H1) at all --- the outcome
is fixed by the declared classes, not by any one marginal comparison."""))

# ---- Site 2: infinite-horizon kernels under the 5th-percentile class
EDITS.append(("site2", r"""Under the 5th-percentile class the infinite-horizon kernel is
nonempty for the moratorium (\(2219.6\) kt) and zero catch (\(2070.9\)
kt) but empty for every positive-cap rule.""",
              r"""Under the 5th-percentile class the infinite-horizon kernel is empty
for every policy, the moratorium and zero catch included, because the
\(318.8\) kt floor also exceeds \(g_{\max}\) and the class is vacuous;
at finite horizon it remains nonempty (\(1412.5\) kt for the moratorium
and \(1394.2\) kt for zero catch at \(T = 5\))."""))

# ---- Site 3: the Reason paragraph (Result 3.2)
EDITS.append(("site3", r"""an empty kernel, while BAU's kernel is nonempty there (\(2219.6\) kt).
Because empty is worst, none of them is at least as protective as BAU at
that reading, so clause (H1) fails for every positive-catch rule. The
informative 10th-percentile class is not where the verdict is decided:
under that class the flat 60-kt cap, the critical-zone rule, the
cascade, and both graded rules hold the LRP from itself at every horizon
(\(884.6\) kt at \(T=1\) and \(T=\infty\)), exactly matching BAU, and
the surplus-proportional family at \(\phi \le 0.50\) holds it too while
harvesting more than the moratorium --- so the informative class is
where the reactive family \emph{almost} passes, not where it fails.""",
              r"""an empty kernel --- and so does BAU's, that reading being vacuous ---
so the 5th-percentile class at \(T = \infty\) ties every rule at worst
and does not by itself decide the verdict. What decides it is that BAU
is at least as protective as every positive-catch rule at all 27
(class, horizon) readings and strictly more protective at 25 of them,
so clause (H1) fails for every positive-catch rule. The informative
10th-percentile class discriminates in the same direction: under it BAU
holds the LRP from itself at every horizon (\(884.6\) kt at \(T = 1\)
and \(T = \infty\)), while the flat 60-kt cap, the critical-zone rule,
the cascade and graded2 sit at \(900.3\) kt at \(T = \infty\) and
graded3 at \(884.6\) kt, so only the surplus-proportional family at
\(\phi \le 0.25\) still matches BAU there while harvesting more than the
moratorium --- the informative class is where the reactive family
\emph{almost} passes, not where it fails."""))

EDITS.append(("site3 H3", r"""mechanism: the equal-protective flat-60 cap (mean allowed catch \(60\)""",
              r"""mechanism: the near-equal flat-60 cap (mean allowed catch \(60\)"""))

EDITS.append(("site3 tail", r"""and the mechanism is the empty-at-the-5th-percentile-class reading of
clause (H1), with the supply comparison as a second failure.""",
              r"""and the mechanism is clause (H1) read at every reading, on which BAU is
never worse and is strictly better at 25 of the 27, with the supply
comparison as a second failure."""))

# ---- Site 4: T=5 classification paragraph
EDITS.append(("site4", r"""5th-percentile class the moratorium's kernel is nonempty (its
\(T=\infty\) boundary is \(2219.6\) kt, above the observed range), so
the classification there follows the informative geometry rather than
universal emptiness.""",
              r"""5th-percentile class every kernel is empty at \(T = \infty\), the
moratorium's included, that class being vacuous; at finite horizon the
moratorium's kernel is nonempty (\(1412.5\) kt at \(T = 5\)), above the
observed range, so at those horizons the classification follows the
informative geometry rather than universal emptiness."""))

# ---- Site 5: discussion
EDITS.append(("site5", r"""because every such rule is empty there while BAU's kernel is nonempty
(\(2219.6\) kt). The supply comparison is a second failure, not the""",
              r"""because BAU is at least as protective as every such rule at every
reading and strictly more protective at 25 of the 27. The supply
comparison is a second failure, not the"""))

# ---- Site 6: limitations
EDITS.append(("site6", r"""the 5th-percentile class at \(T=\infty\) every positive-catch rule is
empty while BAU's kernel is nonempty (\(2219.6\) kt). Because clause""",
              r"""the registered classes every positive-catch rule is worse than BAU at
25 of the 27 (class, horizon) readings and better at none, the
5th-percentile \(T=\infty\) reading tying them all at empty. Because
clause"""))

# ---- Site 7: summary bullet
EDITS.append(("site7", r"""geometry or, alone, supply: every positive-catch rule is empty there
while BAU's kernel is nonempty (\(2219.6\) kt). Under the informative""",
              r"""geometry or, alone, supply: BAU is at least as protective as every
positive-catch rule at every one of the 27 (class, horizon) readings
and strictly more protective at 25. Under the informative"""))

applied, failed = [], []
for label, old, new in EDITS:
    if old in tex:
        n = tex.count(old)
        tex = tex.replace(old, new)
        applied.append((label, n))
    else:
        failed.append(label)

open(SRC, "w", encoding="utf-8").write(tex)

print(f"applied {len(applied)}/{len(EDITS)} edits -> {SRC}")
for label, n in applied:
    print(f"  OK   {label} ({n})")
for label in failed:
    print(f"  MISS {label}")

print("\nresidual sweep:")
for tok in ["2219.6", "2070.9", "920.2", "989.0", "1025.5", "1064.7",
            "1111.3", "1161.0", "0.906", "0.862", "0.958", "0.647"]:
    hits = len(re.findall(r"(?<![\d.])" + re.escape(tok) + r"(?!\d)", tex))
    print(f"  {tok:10s} x{hits}" + ("   <-- STILL PRESENT" if hits else ""))
