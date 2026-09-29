#!/usr/bin/env python3
"""v29 coherence pass 2: the eight surviving v2-basis constants.

The v29 migration changed the CLASS values (-460.0/-318.8/-114.9 ->
-329.0/-287.4/-80.9) and the constructive bound (57.6 -> 91.59), but it did
not reach every worked line that is built out of them. A worked line such
as "172.46 - 318.76 = -146.3" is not a class value; it is arithmetic on
one, and a token-level sweep for the class values alone walks straight
past it. Eight such lines survived into v29. Each is recomputed here on
the source-year classes and replaced.

  1. Section 3.3  172.46 - 318.76 = -146.3   (q05)  -> 172.46 - 287.36 = -114.9
  2. Section 3.3  perpetual-worst (-287.6)          -> (-156.5)
  3. Section 3.3  phi < 1 - 114.85/296.09 = 0.612   -> 1 - 80.87/296.09 = 0.727
  4. Section 3.3  criterion 107.2 / 33.2 / -40.8    -> 141.2 / 67.2 / -6.8
  5. Section 3.7  constructive -62.9 at K=1000      -> -28.87
  6. Section 3.10 F'(K*) median 1.134, [1.001,1.177]-> 1.142, [1.010, 1.179]
  7. Abstract     bootstrap interval [0, 84.8]      -> [0, 121.1]
  8. Abstract +   survival 0.87 -> 0.58 (0.95->0.74)-> 0.91 -> 0.65 (0.95 -> 0.77)
     Conclusions
  9. Conclusions  60-kt rules "outside the robust set", 900.3 kt
                  -> onto the reference point, 884.6 kt (900.3 under v2)

Two further prose defects fixed in the same pass:

 10. Section 3.8  0.8455 reported as 0.84 (truncation where the rest of the
     section rounds); 0.85.
 11. Section 3.6  "The 120-kt rule's kernel is empty" is unqualified and
     false under the Fox form: its 10th-percentile T=1 boundary is 922.7 kt.
     Qualified, and the declared-strength row's "brackets ... from the milder
     side" (a claim the cells do not support: it is lower at two cells and
     higher at one) is replaced by the actual maximum divergence.
"""
from pathlib import Path

P = Path("/home/user/fam/e2/paperE2_cod_intervention_v29.tex")
t = P.read_text(encoding="utf-8")


def rep(old, new, n=1):
    global t
    assert t.count(old) == n, (t.count(old), old[:80])
    t = t.replace(old, new)


# 1 + 2 ---------------------------------------------------------- Section 3.3
rep("independent of the family scaling and rests only on the identified \\(r\\)\n"
    "and the corrected 10th-percentile floor. Under the 5th-percentile floor\n"
    "the corresponding quantity is \\(172.46 - 318.76 = -146.3\\) kt, so no\n"
    "constant catch is robust there; under the perpetual-worst floor the same\n"
    "holds (\\(-287.6\\) kt). \\ensuremath{\\square}\n",
    "independent of the family scaling and rests only on the identified \\(r\\)\n"
    "and the corrected 10th-percentile floor. Under the 5th-percentile floor\n"
    "the corresponding quantity is \\(172.46 - 287.36 = -114.9\\) kt, so no\n"
    "constant catch is robust there; under the perpetual-worst floor the same\n"
    "holds (\\(172.46 - 328.97 = -156.5\\) kt). \\ensuremath{\\square}\n")

# 3 + 4 ------------------------------------------------ Result 3.4 (reactive)
rep("\\((1-\\phi)\\,g_{\\max} > |e_{q10}|\\),\n"
    "i.e.~\\(\\phi < 1 - 114.85/296.09 = 0.612\\). At \\(\\phi = 0.25\\) (\\(0.5\\))\n"
    "the criterion is \\(107.2\\) (\\(33.2\\)) kt \\(> 0\\), so the kernel is the\n"
    "whole safe set; at \\(\\phi = 0.75\\) it is \\(-40.8\\) kt, so the criterion\n"
    "fails and the \\(T=\\infty\\) kernel is empty (\\(920.2\\) kt at \\(T=1\\)).\n",
    "\\((1-\\phi)\\,g_{\\max} > |e_{q10}|\\),\n"
    "i.e.~\\(\\phi < 1 - 80.87/296.09 = 0.727\\). At \\(\\phi = 0.25\\) (\\(0.5\\))\n"
    "the criterion is \\(141.2\\) (\\(67.2\\)) kt \\(> 0\\), so the kernel is the\n"
    "whole safe set; at \\(\\phi = 0.75\\) it is \\(-6.8\\) kt, so the criterion\n"
    "fails and the \\(T=\\infty\\) kernel is empty (\\(920.2\\) kt at \\(T=1\\)).\n")

# 5 ------------------------------------------------------------- Section 3.7
rep("  the box (\\(-62.9\\) kt at \\(K = 1000\\) kt to \\(91.59\\) kt at\n",
    "  the box (\\(-28.87\\) kt at \\(K = 1000\\) kt to \\(91.59\\) kt at\n")

# 6 ------------------------------------------------------------ Section 3.10
rep("classification survives the resampling: \\(F'(K^*)\\) has median \\(1.134\\)\n"
    "and \\(90\\%\\) interval \\([1.001, 1.177]\\). The constructive boundary is",
    "classification survives the resampling: \\(F'(K^*)\\) has median \\(1.142\\)\n"
    "and \\(90\\%\\) interval \\([1.010, 1.179]\\). The constructive boundary is")

# 7 + 8 ------------------------------------------------------------- abstract
rep("(\\(0.95\\) to \\(0.74\\) without the 1992 draw); its \\(90\\%\\) bootstrap interval\n"
    "is \\([0, 84.8]\\) kt. (5)",
    "(\\(0.95\\) to \\(0.77\\) without the 1992 draw); its \\(90\\%\\) bootstrap interval\n"
    "is \\([0, 121.1]\\) kt. (5)")
rep("for every admissible \\(K \\ge 2K^* = 1769.2\\) kt (not an artifact of the\n"
    "pinned \\(K\\)), so the certified layer has a finite horizon --- six\n",
    "for every admissible \\(K \\ge 2K^* = 1769.2\\) kt (not an artifact of the\n"
    "pinned \\(K\\)), so the certified layer has a finite horizon --- six\n")
rep("Stochastic viability gives 20-year survival from the LRP of \\(0.87\\)\n"
    "(zero catch) to \\(0.58\\) (\\(120\\) kt) under i.i.d. resampling\n",
    "Stochastic viability gives 20-year survival from the LRP of \\(0.91\\)\n"
    "(zero catch) to \\(0.65\\) (\\(120\\) kt) under i.i.d. resampling\n")

# 9 ------------------------------------------------------------- conclusions
rep("  bound at 91.59 kt, leaves the 60-kt rules outside the robust set\n"
    "  (their \\(T=\\infty\\) boundary is 900.3 kt, above the 884.6 kt reference\n"
    "  point), lengthens the certified horizon (to \\(T=6\\) under the two\n",
    "  bound at 91.59 kt, brings the 60-kt rules onto the reference point\n"
    "  itself (their \\(T=\\infty\\) boundary is \\(884.6\\) kt, against 900.3 kt\n"
    "  under the registered convention), lengthens the certified horizon (to \\(T=6\\) under the two\n")

# 7 + 8 (conclusions item 1) ------------------------------------------------
rep("  \\([0, 84.8]\\) kt and whose 20-year survival probability from the LRP\n"
    "  is \\(0.77\\) under i.i.d. resampling (against \\(0.84\\) at an\n"
    "  intermediate \\(91.59\\) kt), so the operational reading is order\n",
    "  \\([0, 121.1]\\) kt and whose 20-year survival probability from the LRP\n"
    "  is \\(0.74\\) under i.i.d. resampling (\\(0.73\\) under block\n"
    "  resampling, \\(0.85\\) with the 1992 draw removed), so the operational\n"
    "  reading is order\n")

# 10 ------------------------------------------------------------ Section 3.8
rep("from the LRP falls to \\(0.74\\) under i.i.d. draws (\\(0.73\\) under\n"
    "blocks, \\(0.84\\) without the 1992 draw), so the stochastic reading of\n",
    "from the LRP falls to \\(0.74\\) under i.i.d. draws (\\(0.73\\) under\n"
    "blocks, \\(0.85\\) without the 1992 draw), so the stochastic reading of\n")

# 11 ------------------------------------------------------------ Section 3.6
rep("source-year 10th-percentile floor (\\(-80.87\\) kt); the Fox form's own\n"
    "refit-boundary floor is not used so that only the form varies across\n"
    "Table 2. The BAU and zero-catch certificates under the informative class\n"
    "are exactly unchanged (lower boundary \\(884.6\\) kt at every horizon,\n"
    "\\(T=\\infty\\) included). The 60-kt rule's infinite-horizon lower boundary\n"
    "is empty under the 5th-percentile floor. The 120-kt rule's kernel is\n"
    "empty. Table 2 carries the Fox row.\n",
    "source-year 10th-percentile floor (\\(-80.87\\) kt); the Fox form's own\n"
    "refit-boundary floor is not used so that only the form varies across\n"
    "Table 2. The BAU and zero-catch certificates under the informative class\n"
    "are exactly unchanged (lower boundary \\(884.6\\) kt at every horizon,\n"
    "\\(T=\\infty\\) included). The 60-kt rule's infinite-horizon lower boundary\n"
    "is empty under the 5th-percentile floor. The 120-kt rule is empty under\n"
    "the 5th-percentile and perpetual-worst floors and, under the\n"
    "informative floor, at \\(T=\\infty\\) (its \\(T=1\\) boundary there is\n"
    "\\(922.7\\) kt). Table 2 carries the Fox row.\n")

rep("source-year classes its kernels are not empty and it brackets the\n"
    "identified row from the milder side.\n",
    "source-year classes its kernels are nonempty at every reported cell and\n"
    "lie within \\(12\\) kt (about \\(1\\%\\)) of the identified row's at all of\n"
    "them, so the depensation row does not hinge on the identification of\n"
    "\\(s_0\\).\n")

P.write_text(t, encoding="utf-8")
print("v29d: eight v2-basis constants and three prose defects corrected")
