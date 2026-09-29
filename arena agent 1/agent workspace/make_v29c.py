#!/usr/bin/env python3
"""v29 coherence pass 1: the certified layer (Section 3.4) and its echoes.

WHAT WAS WRONG. Result 3.5 asserted a single certified horizon for every
class and located it by the criterion K* + r_T < K. Direct evaluation of
the runner's own kernel() at the shifted threshold shows that criterion is
neither necessary nor sufficient:

  v3, eps = 328.97, a_max = 1.1531, K* = 884.6, K = 5000, domain [K*, 10^4]
    UC_min : nonempty through T=6 (6 of 7 policies), empty from T=7
    UC_q05 : nonempty through T=6 (6 of 7 policies), empty from T=7
    UC_q10 : nonempty through T=7 (5 of 7 policies), empty from T=8

  The naive test would say "nonempty through T=7" for all three classes,
  because 4560.3 < 5000. It is wrong for the two harsher floors: under the
  perpetual-worst floor the closed loop has no worst-case fixed point at
  all, so every trajectory declines, and from the domain ceiling the BAU
  path is at 4689.6 kt after five steps and 4424.5 kt after six --- it
  clears L(6) = 3787.0 kt but not L(7) = 4560.3 kt.

  The manuscript's artifact reports certified_horizon_nonempty = 5 for
  every policy and class. That field is a GRID ARTIFACT, not the horizon:
  HORIZONS = [1, 2, 3, 5, 8, 10, 15, 20, inf] skips 6 and 7, so 5 is merely
  the last declared horizon tested. This patch computes 6 and 7 explicitly.

Also corrected: the trailing claim that the convention "lengthens the
certified horizon by two years". With the registered defect magnitude
(460.0 kt) the horizons are T=5 (two harsher floors) and T=6 (informative
floor); with the source-year magnitude (329.0 kt) they are T=6 and T=7.
One year, at every class, not two.
"""
from pathlib import Path

P = Path("/home/user/fam/e2/paperE2_cod_intervention_v29.tex")
t = P.read_text(encoding="utf-8")


def rep(old, new, n=1):
    global t
    assert t.count(old) == n, (t.count(old), old[:70])
    t = t.replace(old, new)


# ---------------------------------------------------------------- abstract
rep("pinned \\(K\\)), so certified kernels are empty beyond six years. (4)",
    "pinned \\(K\\)), so the certified layer has a finite horizon --- six\nyears under the two harsher floors, seven under the informative one. (4)")

# ------------------------------------------------- Section 3.4 lead-in + result
rep(
    "The conversion of Definition 2.7 needs the closed loop's contraction\n"
    "rate. The next result shows that no such contraction is available at the\n"
    "declared safe set, and that the certified kernel is therefore empty\n"
    "beyond six years.\n"
    "\n"
    "\\textbf{Result 3.5 (Expansion obstruction).} On the governed\n"
    "surplus-production map of Definition 2.1, the certified kernel is empty\n"
    "beyond \\(T = 6\\) years for every declared policy, zero catch included.\n"
    "At \\(T = 6\\) the certified set is \\([3787.0, 10^4]\\) kt.\n",

    "The conversion of Definition 2.7 needs the closed loop's contraction\n"
    "rate. The next result shows that no such contraction is available at the\n"
    "declared safe set, and that the certified layer therefore has a finite\n"
    "horizon: six years under the two harsher floors, seven under the\n"
    "informative one.\n"
    "\n"
    "\\textbf{Result 3.5 (Expansion obstruction).} On the governed\n"
    "surplus-production map of Definition 2.1 the certified kernel is empty\n"
    "from \\(T = 7\\) under the perpetual-worst and 5th-percentile floors,\n"
    "and from \\(T = 8\\) under the 10th-percentile floor, for every declared\n"
    "policy, zero catch included. At the last nonempty horizon the certified\n"
    "sets lie far above the observed range of the stock:\n"
    "\\([5132.9, 10^4]\\) kt (perpetual worst, BAU, \\(T = 6\\)),\n"
    "\\([4593.2, 10^4]\\) kt (5th percentile, BAU, \\(T = 6\\)), and\n"
    "\\([4560.3, 10^4]\\) kt (10th percentile, BAU and zero catch,\n"
    "\\(T = 7\\)); under the informative floor the 180- and 240-kt caps are\n"
    "already empty at \\(T = 7\\).\n")

# ------------------------------------------------------- Result 3.5 reason
rep(
    "\\emph{Reason.} Here \\(F'(S) = 1 + r(1-2S/K)\\) is increasing as \\(S\\)\n"
    "falls. At the LRP, \\(F'(K^*) = 1.153 > 1\\). The governed surplus map is\n"
    "therefore expansive at the declared safe set, contracting only above\n"
    "\\(K/2 = 2500\\) kt --- a stock level the series never approaches. The\n"
    "contraction form of the conversion is therefore inapplicable. The\n"
    "expansive form \\(r_T = \\varepsilon(a_{\\max}^T - 1)/(a_{\\max} - 1)\\)\n"
    "grows without bound; with the committed \\(\\varepsilon = 329.0\\) kt and\n"
    "\\(a_{\\max} = 1.1531\\): \\(r_1 = 329.0\\), \\(r_2 = 708.3\\),\n"
    "\\(r_3 = 1145.7\\), \\(r_5 = 2231.7\\), \\(r_6 = 2902.4\\), \\(r_7 = 3675.7\\)\n"
    "kt. The certified kernel --- the nominal kernel of \\(K^* + r_T\\) --- is\n"
    "nonempty only while \\(K^* + r_T < K\\), i.e.~through \\(T = 7\\)\n"
    "(\\(4560.3\\) kt); at \\(T = 8\\) the shifted threshold is \\(5452.0\\) kt,\n"
    "above the carrying capacity, and the certified kernel is empty. The\n"
    "certified horizon is therefore \\(T = 7\\), not the earlier\n"
    "beyond-\\(T = 5\\) reading. At \\(T=7\\) the certified set is\n"
    "\\([4560.3, 10^4]\\) kt, above the entire observed range of the stock. \\ensuremath{\\square}\n",

    "\\emph{Reason.} Here \\(F'(S) = 1 + r(1-2S/K)\\) is increasing as \\(S\\)\n"
    "falls. At the LRP, \\(F'(K^*) = 1.153 > 1\\). The governed surplus map is\n"
    "therefore expansive at the declared safe set, contracting only above\n"
    "\\(K/2 = 2500\\) kt --- a stock level the series never approaches. The\n"
    "contraction form of the conversion is therefore inapplicable. The\n"
    "expansive form \\(r_T = \\varepsilon(a_{\\max}^T - 1)/(a_{\\max} - 1)\\)\n"
    "grows without bound; with the committed \\(\\varepsilon = 329.0\\) kt and\n"
    "\\(a_{\\max} = 1.1531\\): \\(r_1 = 329.0\\), \\(r_2 = 708.3\\),\n"
    "\\(r_3 = 1145.7\\), \\(r_4 = 1650.1\\), \\(r_5 = 2231.7\\),\n"
    "\\(r_6 = 2902.4\\), \\(r_7 = 3675.7\\), \\(r_8 = 4567.4\\) kt, so the\n"
    "shifted threshold \\(K^* + r_T\\) runs \\(1213.6\\), \\(1592.9\\),\n"
    "\\(2030.3\\), \\(2534.7\\), \\(3116.3\\), \\(3787.0\\), \\(4560.3\\),\n"
    "\\(5452.0\\) kt at \\(T = 1,\\ldots,8\\).\n"
    "\n"
    "Emptiness is not simply the shifted threshold outgrowing the carrying\n"
    "capacity: at \\(T = 7\\) the threshold (\\(4560.3\\) kt) is still below\n"
    "\\(K = 5000\\) kt, and the certified kernel is empty under the two\n"
    "harsher floors nevertheless. What fails is the trajectory, not the\n"
    "arithmetic of the shift. Under the perpetual-worst floor the BAU closed\n"
    "loop has no worst-case fixed point at all, so every trajectory declines;\n"
    "started from the domain ceiling of \\(10^4\\) kt it reaches \\(4689.6\\)\n"
    "kt after five steps and \\(4424.5\\) kt after six, which clears the\n"
    "six-year threshold (\\(3787.0\\) kt) but not the seven-year one\n"
    "(\\(4560.3\\) kt). Under the informative 10th-percentile floor the loop\n"
    "does have an attracting worst-case fixed point (\\(4606.5\\) kt for BAU,\n"
    "above the seven-year threshold and below the eight-year one), which is\n"
    "why the horizon is one year longer there. The certified sets at those\n"
    "horizons lie above the entire observed range of the stock. \\ensuremath{\\square}\n")

# ------------------------------------------------ Section 3.4 trailing para
rep(
    "is defect-bound to \\(T \\le 3\\) years. The corrected convention lengthens\n"
    "the certified horizon by two years (empty from \\(T = 8\\) rather than\n"
    "\\(T = 6\\)).\n",
    "is defect-bound to \\(T \\le 3\\) years. The source-year convention\n"
    "lengthens the horizon by one year at every class (\\(T = 5 \\to 6\\)\n"
    "under the two harsher floors, \\(T = 6 \\to 7\\) under the informative\n"
    "floor), because it replaces the registered defect magnitude\n"
    "(\\(\\varepsilon = 460.0\\) kt) by the source-year one (\\(329.0\\) kt)\n"
    "while leaving \\(a_{\\max}\\) unchanged.\n")

# ------------------------------------------------------------- Section 4 echo
rep(
    "The certified-layer emptiness beyond\n"
    "\\(T = 6\\) years (Section 3.4) is a different statement, about the\n"
    "conversion's expansive form: the governed map's expansion rate\n"
    "(\\(F' = 1.153\\) at the LRP) empties every certified kernel beyond seven\n"
    "years. Neither",
    "The certified-layer emptiness beyond\n"
    "\\(T = 6\\) years under the two harsher floors and beyond \\(T = 7\\) under\n"
    "the informative one (Section 3.4) is a different statement, about the\n"
    "conversion's expansive form: the governed map's expansion rate\n"
    "(\\(F' = 1.153\\) at the LRP) empties every certified kernel at those\n"
    "horizons. Neither")

# ---------------------------------------------------------- Conclusions echo
rep(
    "  The certified layer is empty beyond six years because the map is\n"
    "  expansive at the reference point --- for every admissible\n",
    "  The certified layer has a finite horizon --- six years under the two\n"
    "  harsher floors, seven under the informative one --- because the map\n"
    "  is expansive at the reference point --- for every admissible\n")

rep(
    "  bound at 91.59 kt, leaves the 60-kt rules outside the robust set\n"
    "  (their \\(T=\\infty\\) boundary is 900.3 kt, above the 884.6 kt reference\n"
    "  point), lengthens the certified horizon (to \\(T=7\\)), and reduces\n",
    "  bound at 91.59 kt, leaves the 60-kt rules outside the robust set\n"
    "  (their \\(T=\\infty\\) boundary is 900.3 kt, above the 884.6 kt reference\n"
    "  point), lengthens the certified horizon (to \\(T=6\\) under the two\n"
    "  harsher floors and \\(T=7\\) under the informative one), and reduces\n")

P.write_text(t, encoding="utf-8")
print("v29c: certified-layer coherence patch applied")
