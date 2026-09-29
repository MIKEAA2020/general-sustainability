#!/usr/bin/env python3
"""v28e -- migrate Tables 3 and 5 to the REGISTERED basis and fix the
pervasive "source-year" mislabelling.

Diagnosis
---------
Two elevation campaigns exist and both were archived:

  * fam/e2/rerun_campaigns/results/      <- REGISTERED  (campaign_e2_elevation.py)
  * fam/e2/src/results_srcyear/          <- SOURCE-YEAR (campaign_srcyear.py)

Their residual summaries differ:
  registered : mean -20.44  sd 134.96  min -460.03  q05 -318.76  q10 -114.85
               max +179.76  lag1 0.652
  source-year: mean -10.88  sd 114.91  min -328.97  q05 -287.36  q10  -80.87
               max +206.55  lag1 0.554

The v28 correction campaign migrated most NUMBERS to the registered basis but
left the prose LABELS reading "source-year".  Two tables were missed
entirely:

  * Table 5 (finite-duration floors): every one of the 36 cells is the
    source-year value.  Verified exactly against
    src/results_srcyear/e2_elevation_finite_floors.csv.
  * Table 3 (K-grid) Constructive column: 9 of 10 rows match NEITHER campaign
    (the archived constructive is identical in BOTH campaigns, because
    campaign_srcyear.py freezes the floor at the committed -114.85).  The
    K=1000 T=1 entry 943.2 is the source-year value; registered is 1009.2.

Two prose claims were rebuilt on the corrected numbers.

VERIFIED AND LEFT ALONE (these really are source-year, and are correct):
  * Section 3.5 stress replay -- 953.9 / 948.9 / 923.9 / 893.9 reproduce the
    source-year runner exactly (953.96 / 948.96 / 923.96 / 893.96).
  * "under the corrected source-year 10th-percentile class the critical-zone
    rule, the cascade, and the graded rules all hold the LRP" -- recomputed:
    at e = -80.87 the flat_25/S1/cpm/flat_0 lower boundary is 884.6 at
    T = 1, 5 and inf, i.e. exactly BAU.
  * The provenance note about the superseded source-year runner.
"""
import ast
import sys

TEX = "/home/user/fam/e2/paperE2_cod_intervention_v28.tex"

EDITS = []


def E(label, old, new):
    EDITS.append((label, old, new))


# ===========================================================================
# 1. TABLE 5 -- finite-duration floors: source-year -> registered
#    registered values from
#    fam/e2/rerun_campaigns/results/e2_elevation_finite_floors.csv
# ===========================================================================
E("T5 row zero catch",
  r"zero catch & 1280.8 & 1510.5 & 1657.6 & 1431.6 & 1770.9 & 2015.3 \\",
  r"zero catch & 1394.2 & 1705.0 & 1922.2 & 1936.2 & 2769.7 & 3777.4 \\")

E("T5 row BAU",
  r"BAU (5 kt) & 1298.7 & 1540.7 & 1697.8 & 1450.0 & 1803.7 & 2062.3 \\",
  r"BAU (5 kt) & 1412.5 & 1737.1 & 1967.3 & 1956.4 & 2815.1 & 3881.7 \\")

E("T5 row 60 kt",
  r"60 kt / S1 / cascade & 1499.6 & 1893.2 & 2193.4 & 1656.7 & 2188.8 &"
  "\n" r"2657.5 \\",
  r"60 kt / S1 / cascade & 1617.7 & 2113.6 & 2534.4 & 2184.2 & 3364.1 &"
  "\n" r"5505.7 \\")

E("T5 row 120 kt",
  r"120 kt & 1727.7 & 2329.0 & 2898.1 & 1891.7 & 2671.8 & 3562.3 \\",
  r"120 kt & 1851.0 & 2584.1 & 3380.3 & 2444.6 & 4103.8 & empty \\")

E("T5 row 180 kt",
  r"180 kt & 1999.0 & 2869.7 & 3986.2 & 2172.3 & 3285.8 & 5180.7 \\",
  r"180 kt & 2129.2 & 3178.3 & 4827.8 & 2759.4 & 5173.4 & empty \\")

E("T5 row 240 kt",
  r"240 kt & 2623.1 & 4013.4 & 8790.9 & 2825.0 & 4687.8 & empty \\",
  r"240 kt & 2774.7 & 4507.6 & empty & 3521.3 & 9427.0 & empty \\")

# --- Result 3.8(i): the two quoted boundaries, and the stale comparison ----
E("Result 3.8(i) boundaries",
  r"""  Duration is informative. A five-year 5th-percentile episode already
  lifts the BAU boundary from the LRP to \(1298.7\) kt, and a
  fifteen-year episode lifts it to \(1697.8\) kt. The safe set contracts
  as the episode lengthens, without the arithmetic vacuity of the
  perpetual classes. The source-year floors are milder than the frozen
  ones, so the boundaries sit below the earlier reading at every
  duration.""",
  r"""  Duration is informative. A five-year 5th-percentile episode already
  lifts the BAU boundary from the LRP to \(1412.5\) kt, and a
  fifteen-year episode lifts it to \(1967.3\) kt. The safe set contracts
  as the episode lengthens, without the arithmetic vacuity of the
  perpetual classes: the perpetual 5th-percentile floor empties the
  kernel at \(T = \infty\), whereas every finite duration is informative
  at both floors.""")

# ===========================================================================
# 2. TABLE 3 -- K-grid Constructive column + K=1000 T=1 boundary
#    constructive = g(K*) - 114.85, identical in both archived campaigns
# ===========================================================================
E("T3 K=1000",
  r"1000 & 0.5094 & 127.4 & 0.608 & \(-32.2\) & 943.2 & empty & yes \\",
  r"1000 & 0.5094 & 127.4 & 0.608 & \(-62.85\) & 1009.2 & empty & yes \\")

E("T3 K=1200",
  r"1200 & 0.5248 & 157.4 & 0.751 & 36.0 & 884.6 & 884.6 & yes \\",
  r"1200 & 0.5248 & 157.4 & 0.751 & 7.16 & 884.6 & 884.6 & yes \\")

E("T3 K=1500",
  r"1500 & 0.4099 & 153.7 & 0.926 & 62.9 & 884.6 & 884.6 & yes \\",
  r"1500 & 0.4099 & 153.7 & 0.926 & 33.92 & 884.6 & 884.6 & yes \\")

E("T3 K=1769.2",
  r"1769.2 (\(=2K^*\)) & 0.3559 & 157.4 & 1.000 & 72.7 & 884.6 & 884.6 &"
  "\n" r"yes \\",
  r"1769.2 (\(=2K^*\)) & 0.3559 & 157.4 & 1.000 & 42.57 & 884.6 & 884.6 &"
  "\n" r"yes \\")

E("T3 K=2000",
  r"2000 & 0.3273 & 163.6 & 1.038 & 77.6 & 884.6 & 884.6 & yes \\",
  r"2000 & 0.3273 & 163.6 & 1.038 & 46.62 & 884.6 & 884.6 & yes \\")

E("T3 K=2500",
  r"2500 & 0.2908 & 181.7 & 1.085 & 83.4 & 884.6 & 884.6 & yes \\",
  r"2500 & 0.2908 & 181.7 & 1.085 & 51.35 & 884.6 & 884.6 & yes \\")

E("T3 K=3000",
  r"3000 & 0.2704 & 202.8 & 1.111 & 86.6 & 884.6 & 884.6 & yes \\",
  r"3000 & 0.2704 & 202.8 & 1.111 & 53.81 & 884.6 & 884.6 & yes \\")

E("T3 K=4000",
  r"4000 & 0.2485 & 248.5 & 1.139 & 89.9 & 884.6 & 884.6 & yes \\",
  r"4000 & 0.2485 & 248.5 & 1.139 & 56.33 & 884.6 & 884.6 & yes \\")

E("T3 K=5000",
  r"5000 (registered) & 0.2369 & 296.1 & 1.153 & \textbf{57.6} & 884.6 &"
  "\n" r"884.6 & \textbf{yes} \\",
  r"5000 (registered) & 0.2369 & 296.1 & 1.153 & \textbf{57.61} & 884.6 &"
  "\n" r"884.6 & \textbf{yes} \\")

E("T3 K=7000",
  r"7000 (out of box) & 0.2248 & 393.5 & 1.168 & 93.3 & 884.6 & 884.6 &"
  "\n" r"no \\",
  r"7000 (out of box) & 0.2248 & 393.5 & 1.168 & 58.91 & 884.6 & 884.6 &"
  "\n" r"no \\")

# --- Result 3.7(i) endpoint, and the K=1000 T=1 boundary in Result 3.7(ii)
E("Result 3.7(i) constructive endpoints",
  r"""  constructive bound rises monotonically toward the registered end of
  the box (\(-62.9\) kt at \(K = 1000\) kt to \(57.6\) kt at
  \(K = 5000\) kt), with the fit cost rising as \(K\) falls below""",
  r"""  constructive bound rises monotonically toward the registered end of
  the box (\(-62.85\) kt at \(K = 1000\) kt to \(57.61\) kt at
  \(K = 5000\) kt), with the fit cost rising as \(K\) falls below""")

E("Result 3.7(ii) K=1000 T=1 boundary",
  r"""  bound is negative at \(K = 1000\) kt, and the BAU kernel under the
  10th-percentile class is empty at \(T = \infty\) with the \(T = 1\)
  boundary raised to \(943.2\) kt --- the moratorium itself no longer
  holds the reference point.""",
  r"""  bound is negative at \(K = 1000\) kt, and the BAU kernel under the
  10th-percentile class is empty at \(T = \infty\) with the \(T = 1\)
  boundary raised to \(1009.2\) kt --- the moratorium itself no longer
  holds the reference point.""")

# ===========================================================================
# 3. FOX FORM -- constructive bound was computed with the source-year floor
#    registered: g(K*) = 159.923, |e_q10| = 114.848 -> 45.076 (archived 45.08)
# ===========================================================================
E("Fox constructive bound",
  r"""The constructive 10th-percentile bound is
\(g(K^*) - |e_{q10}| = 159.92 - 80.87 = 79.05\) kt, under the
source-year 10th-percentile floor (\(-80.87\) kt); the Fox form's own
refit-boundary floor is not used so that only the form varies across
Table 2.""",
  r"""The constructive 10th-percentile bound is
\(g(K^*) - |e_{q10}| = 159.923 - 114.848 = 45.08\) kt, under the
registered 10th-percentile floor (\(-114.85\) kt); the Fox form's own
refit-boundary floor is not used so that only the form varies across
Table 2.""")

# ===========================================================================
# 4. LABELS: "source-year" -> "registered" wherever registered numbers are
#    used.  (Section 3.5, the two dominance/sensitivity claims about the
#    source-year class, and the provenance note are correct and untouched.)
# ===========================================================================
E("label: section 3.2 declared classes",
  r"Under the declared source-year classes, every member of both was empty",
  r"Under the declared registered classes, every member of both was empty")

E("label: Table 1 caption",
  r"""disturbance classes, in the
source-year convention. ``empty'' denotes that no state is robustly""",
  r"""disturbance classes, in the
registered convention. ``empty'' denotes that no state is robustly""")

E("label: section 3.6 lead-in",
  r"""on the residual convention, and those are reported here in the
source-year convention. The depensatory form is the better-fitting of""",
  r"""on the residual convention, and those are reported here in the
registered convention. The depensatory form is the better-fitting of""")

E("label: Table 2 frozen classes",
  r"endpoints, held frozen across forms as the corrected source-year classes",
  r"endpoints, held frozen across forms as the registered classes")

E("label: Allee declared-strength alternative",
  r"source-year classes its kernels are not empty and it brackets the",
  r"registered classes its kernels are not empty and it brackets the")

E("label: Table 2 caption",
  r"boundaries (kt) at the declared source-year class endpoints.",
  r"boundaries (kt) at the declared registered class endpoints.")

E("label: section 3.7 lead-in",
  r"""by one-step least squares at each \(K\) on the same window, in the
source-year convention, with the kernel scored against each refit's own
source-year 10th-percentile floor.""",
  r"""by one-step least squares at each \(K\) on the same window, in the
registered convention, with the kernel scored against the frozen
registered 10th-percentile floor of \(-114.85\) kt.""")

E("label: Table 3 caption",
  r"""\textbf{Table 3.} Carrying-capacity sensitivity in the source-year
convention: \(r\) refit at fixed \(K\), kernel scored against that
refit's own corrected 10th-percentile floor.""",
  r"""\textbf{Table 3.} Carrying-capacity sensitivity in the registered
convention: \(r\) refit at fixed \(K\), kernel scored against that
refit's own surplus \(g(K^*)\) less the frozen registered
10th-percentile floor of \(-114.85\) kt.""")

# --- Section 3.8 stochastic: Table 4 is on the REGISTERED pool ------------
E("label+value: section 3.8 residual pool and autocorrelation",
  r"""initial stock, \(20{,}000\) trajectories resample the 24 source-year
training residuals (i.i.d., and in moving blocks of four, respecting the
residual autocorrelation of \(0.55\)). Viability is scored as the""",
  r"""initial stock, \(20{,}000\) trajectories resample the 24 registered
training residuals (i.i.d., and in moving blocks of four, respecting the
residual autocorrelation of \(0.65\)). Viability is scored as the""")

E("label: Table 4 caption",
  r"policies), source-year pool.",
  r"policies), registered pool.")

E("rewrite: section 3.8 severity comparison",
  r"""under every scheme --- the peaks sit far above the LRP. The corrected
source-year pool is marginally less severe than the frozen
destination-year pool, so the survival probabilities are higher across
the board.""",
  r"""under every scheme --- the peaks sit far above the LRP. The residual
convention matters here, and in the direction the fit implies: on the
source-year pool, whose residual SD is \(114.9\) kt against the
registered \(135.0\) kt, the same four probabilities are \(0.906\),
\(0.906\), \(0.835\) and \(0.647\), so the milder convention raises every
survival probability by three to seven points. Table 4 reports the
registered pool throughout.""")

E("label: section 3.9 convention",
  r"""recursion on the monotone map, in the source-year convention (the
\(n=5\) worst-floor BAU boundary reproduces the registered \(T=5\)
boundary of the archived kernel table as a built-in check).""",
  r"""recursion on the monotone map, in the registered convention (the
\(n=5\) worst-floor BAU boundary reproduces the registered \(T=5\)
boundary of \(1956.4\) kt from the archived kernel table as a built-in
check).""")

E("label: Table 5 caption",
  r"""floor of \(n\) years followed by zero residual (source-year); empty = no""",
  r"""floor of \(n\) years followed by zero residual (registered); empty = no""")

E("label: section 3.10 bootstrap residuals",
  r"with resampled source-year training residuals and refits \(r\) at",
  r"with resampled registered training residuals and refits \(r\) at")

E("label+value: section 3.12 convention-dependent summary",
  r"""  in the sense that the source-year convention sets the constructive
  bound at 57.6 kt, leaves the 60-kt rules outside the robust set""",
  r"""  in the sense that the registered convention sets the constructive
  bound at \(57.61\) kt, leaves the 60-kt rules outside the robust set""")


src = open(__file__, encoding="utf-8").read()
ast.parse(src)

tex = open(TEX, encoding="utf-8").read()
print(f"loaded {TEX}  ({len(tex)} chars)\n")

applied = ambiguous = missing = 0
for label, old, new in EDITS:
    n = tex.count(old)
    if n == 0:
        print(f"  MISS       {label}")
        missing += 1
    elif n > 1:
        print(f"  AMBIGUOUS  {label}  ({n} matches) -- left unchanged")
        ambiguous += 1
    else:
        tex = tex.replace(old, new, 1)
        applied += 1
        print(f"  ok         {label}")

open(TEX, "w", encoding="utf-8").write(tex)
print(f"\napplied {applied}  missing {missing}  ambiguous {ambiguous}")
sys.exit(0 if (missing == 0 and ambiguous == 0) else 1)
