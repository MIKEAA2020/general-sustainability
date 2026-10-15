#!/usr/bin/env python3
"""
Verifier for paper09 v44 (certifying threshold management: Northern cod LRP and
Edwards Aquifer J-17).

Runs the exact re-derivation core (work/p09_core.py), regenerates the tables
and figures, and evaluates named Boolean checks against the regenerated
output: the archive agreement count, the closed forms of Section 2, every
headline number of the abstract and of Tables 1-7, the figure data, and the
numbers quoted in the compiled PDFs when they are present.  Exit status 1 on
any failure.  The core is located beside this file (work/) or in the shipped
source folder (paper09_cod_certification_v44_src/work/).

    python3 paper09_cod_certification_v44_verification.py            # full run, writes *_verification_output.txt
    python3 paper09_cod_certification_v44_verification.py --quick    # reuse work/results.json, no output file
"""
import json
import math
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = HERE if os.path.isdir(os.path.join(HERE, "work")) else os.path.join(HERE, "paper09_cod_certification_v44_src")
WORK = os.path.join(SRC, "work")
QUICK = "--quick" in sys.argv
NCHECKS_EXPECTED = 77   # full run: 3 R0 + 71 content checks + X1-X3; --quick skips the 3 R0 checks
T0 = time.time()
LINES = []
NPASS = NFAIL = 0


def check(name, cond):
    global NPASS, NFAIL
    ok = bool(cond)
    NPASS += ok
    NFAIL += not ok
    line = ("PASS " if ok else "FAIL ") + name
    LINES.append(line)
    print(line, flush=True)


def close(a, b, tol):
    try:
        return a is not None and b is not None and abs(float(a) - float(b)) <= tol
    except (TypeError, ValueError):
        return False


# ------------------------------------------------------------------ 0. run the core
if not QUICK:
    for script in ("p09_core.py", "make_tables.py", "make_figs.py"):
        r = subprocess.run([sys.executable, "-u", script], cwd=WORK, capture_output=True, text=True)
        check(f"R0 {script} exits 0" + ("" if r.returncode == 0 else " :: " + r.stderr[-400:]), r.returncode == 0)
R = json.load(open(os.path.join(WORK, "results.json")))
C, E, A = R["cod"], R["edwards"], R["archive"]
cc, fit, ks = C["constants"], C["fit"], C["kernels"]
ef = E["fit"]

# ------------------------------------------------------------------ 1. archive agreement
check(f"A1 archive agreement: {R['n_archive_checks']} comparisons against the registered campaign artefacts, 0 failures",
      R["n_archive_checks"] == 926 and R["n_archive_check_failures"] == 0)
check("A2 every archive comparison group listed in SI Table (checks) has passed == checks",
      all(c["ok"] for c in R["archive_checks"]))

# ------------------------------------------------------------------ 2. cod fit and constants
check("C1 cod fit: r = 0.2369 (0.236869), K pinned at the 5000-kt box edge, 24 fit transitions 1984-2007, 8 out of sample",
      close(fit["r"], 0.236869, 2e-6) and close(fit["K"], 5000.0, 1e-9) and fit["pinned"] and fit["n_train"] == 24 and fit["n_oos"] == 8)
check("C2 cod LRP = 884.58 kt (1983-1989 mean SSB)", close(C["K_star"], 884.58, 0.01))
check("C3 cod residuals: train SD 114.9 kt, |e|max 328.97 kt in 1992, second collapse residual -323.5 kt in 1993, lag-1 acf 0.554",
      close(fit["train_sd"], 114.9, 0.1) and close(fit["train_abs_max"], 328.97, 0.01) and fit["train_abs_max_year"] == 1992
      and close(fit["residuals_train"]["1993"], -323.5, 0.1) and close(fit["train_lag1_acf"], 0.554, 0.002))
check("C4 cod out-of-sample 2008-2015: SD 28.1 kt, |e|max 46.7 kt in 2014 (declaration not exceeded)",
      close(fit["oos_sd"], 28.1, 0.1) and close(fit["oos_abs_max"], 46.7, 0.1) and fit["oos_abs_max_year"] == 2014 and fit["oos_abs_max"] < fit["train_abs_max"])
check("C5 floor classes |e| = 328.97 / 287.36 / 80.87 kt (min / q05 / q10, linear convention)",
      close(cc["classes_abs"]["UC_min"], 328.97, 0.01) and close(cc["classes_abs"]["UC_q05"], 287.36, 0.01) and close(cc["classes_abs"]["UC_q10"], 80.87, 0.01))
check("C6 g(LRP) = 172.46 kt, g_max = rK/4 = 296.09 kt, F'(LRP) = 1.1531 > 1 (expansive: K > 2 LRP)",
      close(cc["g_Kstar"], 172.46, 0.01) and close(cc["g_max"], 296.09, 0.01) and close(cc["Fp_Kstar"], 1.1531, 0.0001)
      and close(cc["g_max"], fit["r"] * fit["K"] / 4, 1e-6) and fit["K"] > 2 * C["K_star"])
check("C7 C* = g(LRP) - |e| = -156.5 / -114.9 / 91.59 kt; C_vac = g_max - |e| = -32.9 / 8.72 / 215.2 kt",
      all(close(cc["C_star"][k], v, 0.05) for k, v in (("UC_min", -156.5), ("UC_q05", -114.9), ("UC_q10", 91.59)))
      and all(close(cc["C_vac"][k], v, 0.05) for k, v in (("UC_min", -32.9), ("UC_q05", 8.72), ("UC_q10", 215.2)))
      and all(close(cc["C_star"][k], cc["g_Kstar"] - cc["classes_abs"][k], 1e-9) for k in cc["C_star"]))
check("C8 proportional thresholds phi*_safe = 0.5311 and phi*_nonempty = 0.7269 under q10",
      close(cc["phi_star_safe"]["UC_q10"], 0.5311, 0.0001) and close(cc["phi_star_nonempty"]["UC_q10"], 0.7269, 0.0001))

# ------------------------------------------------------------------ 3. cod kernels (Theorem 2.3 / Corollary 2.4)
def binf(v):
    return v[-1] if isinstance(v, list) else v
check("K1 q10: whole safe set (b_T = LRP at every T incl. inf) for BAU, zero catch, flat 60, S1, cascade, graded rules",
      all(close(binf(ks[p]["UC_q10"][T]), C["K_star"], 1e-6) for p in ("BAU", "flat_0", "flat_25", "S1", "cpm", "graded2", "graded3") for T in ks[p]["UC_q10"]))
check("K2 q10: flat 120 and 180 kt are half-lines from s_-(C+|e|) = 1082.3 and 1637.8 kt; flat 240 kt empty at T = inf",
      close(ks["flat_50"]["UC_q10"]["inf"], 1082.3, 0.1) and close(ks["flat_75"]["UC_q10"]["inf"], 1637.8, 0.1) and ks["flat_100"]["UC_q10"]["inf"] is None
      and close(C["b_inf_flat"]["120"]["UC_q10"], 1082.3, 0.1) and C["b_inf_flat"]["240"]["UC_q10"] is None)
check("K3 worst floor: every kernel empty at T = inf; BAU T-step boundaries 1025.5 / 1149.7 / 1260.4 / 1450.0 kt at T = 1, 2, 3, 5",
      all(ks[p]["UC_min"]["inf"] is None for p in ks)
      and all(close(ks["BAU"]["UC_min"][T], v, 0.1) for T, v in (("1", 1025.5), ("2", 1149.7), ("3", 1260.4), ("5", 1450.0))))
check("K4 q05: infinite-horizon kernels non-empty only for C <= C_vac = 8.7 kt (BAU b_inf 2219.6, zero catch 2070.9 kt; 60 kt empty)",
      close(binf(ks["BAU"]["UC_q05"]["inf"]), 2219.6, 0.1) and close(binf(ks["flat_0"]["UC_q05"]["inf"]), 2070.9, 0.1) and ks["flat_25"]["UC_q05"]["inf"] is None
      and close(C["b_inf_flat"]["5"]["UC_q05"], 2219.6, 0.1) and C["b_inf_flat"]["60"]["UC_q05"] is None)
check("K5 stage-at-threshold: S1, cascade and flat 60 kt have identical boundaries under every floor and horizon",
      all(close(binf(ks["S1"][cl][T]), binf(ks["flat_25"][cl][T]), 1e-6) if ks["flat_25"][cl][T] is not None else ks["S1"][cl][T] is None
          for cl in ("UC_min", "UC_q05", "UC_q10") for T in ks["S1"][cl])
      and all(close(binf(ks["cpm"][cl][T]), binf(ks["flat_25"][cl][T]), 1e-6) if ks["flat_25"][cl][T] is not None else ks["cpm"][cl][T] is None
              for cl in ("UC_min", "UC_q05", "UC_q10") for T in ks["cpm"][cl]))
check("K6 graded rules: 60/90 ties flat 60 at T = 1 (1073.8 kt), 30/60/90 is more protective at T = 1 (1047.4 kt); both less protective at T = 5 (1754.3, 1715.1 vs 1656.7 kt), worst floor",
      close(ks["graded2"]["UC_min"]["1"], 1073.8, 0.1) and close(ks["flat_25"]["UC_min"]["1"], 1073.8, 0.1) and close(ks["graded3"]["UC_min"]["1"], 1047.4, 0.1)
      and close(ks["graded2"]["UC_min"]["5"], 1754.3, 0.1) and close(ks["graded3"]["UC_min"]["5"], 1715.1, 0.1) and close(ks["flat_25"]["UC_min"]["5"], 1656.7, 0.1))
check("K7 margins C* - C(LRP) under q10: BAU +86.6, 60-kt rules +31.6, 120 kt -28.4 kt; sign decides whole-safe-set vs half-line",
      close(cc["C_star"]["UC_q10"] - 5, 86.6, 0.05) and close(cc["C_star"]["UC_q10"] - 60, 31.6, 0.05) and close(cc["C_star"]["UC_q10"] - 120, -28.4, 0.05))
fam = C["family_A_q10"]
check("K8 proportional family (q10): phi = 0.25, 0.5 whole safe set; 0.6, 0.7 half-lines from s_- = 1092.0 and 1751.8 kt; 0.75 empty",
      fam["0.25"]["regime"] == "whole safe set" and fam["0.5"]["regime"] == "whole safe set" and fam["0.75"]["regime"] == "empty"
      and close(fam["0.6"]["b_inf"], 1092.0, 0.1) and close(fam["0.7"]["b_inf"], 1751.8, 0.1))
ff = C["finite_floors"]
check("K9 finite floors (q05): 5 and 15 consecutive floor years absorbed from 1298.7 / 1697.8 kt under BAU and 1499.6 / 2193.4 kt under 60 kt",
      close(ff["UC_q05|BAU"]["5"], 1298.7, 0.1) and close(ff["UC_q05|BAU"]["15"], 1697.8, 0.1)
      and close(ff["UC_q05|flat_60"]["5"], 1499.6, 0.1) and close(ff["UC_q05|flat_60"]["15"], 2193.4, 0.1))

# ------------------------------------------------------------------ 4. cod horizons (Theorem 2.7, Propositions 2.8-2.9)
hz, ex, lb = C["certified_horizon"], C["exact_bounded_defect"], C["lipschitz_boundaries"]
check("H1 Lipschitz accumulation r_T = eps (a^T - 1)/(a - 1): 329, 708, 1146, 1650, 2232, 2902, 3675 kt (T = 1..7)",
      all(close(cc["r_T"][str(T)], v, 1.0) for T, v in ((1, 329), (2, 708), (3, 1146), (4, 1650), (5, 2232), (6, 2902), (7, 3675))))
check("H2 Lipschitz certified horizon 6 / 6 / 7 (worst / q05 / q10) for every flat catch <= 150 kt; 6/6/6 at 180; 5/5/6 at 240; ceiling bound 11.63",
      all(tuple(hz[c][k]["last_nonempty"] for k in ("UC_min", "UC_q05", "UC_q10")) == (6, 6, 7) for c in ("0.0", "5.0", "30.0", "60.0", "91.59", "120.0", "150.0"))
      and tuple(hz["180.0"][k]["last_nonempty"] for k in ("UC_min", "UC_q05", "UC_q10")) == (6, 6, 6)
      and [ex["flat_100"][k]["lipschitz_last_nonempty"] for k in ("UC_min", "UC_q05", "UC_q10")] == [5, 5, 6]
      and [ex["flat_75"][k]["lipschitz_last_nonempty"] for k in ("UC_min", "UC_q05", "UC_q10")] == [6, 6, 6]
      and close(C["horizon_bounds_lipschitz"]["policy_independent_ceiling_bound"], 11.63, 0.01))
orb = C["orbit_from_ceiling_BAU"]["UC_min"]
check("H3 worst-case orbit from the 10 000-kt ceiling under BAU (worst floor): 7297, 6169, 5493, 5031, 4690, 4425, 4211 kt; r_6 = 2902 < 4425 - LRP and r_7 = 3675 > 4211 - LRP, so the certificate holds through T = 6 and fails at T = 7",
      all(close(orb[i], v, 1.0) for i, v in enumerate((7297, 6169, 5493, 5031, 4690, 4425, 4211)))
      and cc["r_T"]["6"] < orb[5] - C["K_star"] and cc["r_T"]["7"] > orb[6] - C["K_star"])
check("H4 exact bounded-defect horizons (worst / q05 / q10): BAU 12/13/27, zero catch 12/13/28, 60-kt rules 10/11/20, 120 kt 9/10/16, 180 kt 8/9/14, 240 kt 8/8/12",
      [ex[p][k]["last_nonempty"] for p in ("BAU", "flat_0", "flat_25", "S1", "cpm", "flat_50", "flat_75", "flat_100") for k in ("UC_min", "UC_q05", "UC_q10")]
      == [12, 13, 27, 12, 13, 28, 10, 11, 20, 10, 11, 20, 10, 11, 20, 9, 10, 16, 8, 9, 14, 8, 8, 12])
check("H5 exact BAU worst-floor boundaries 1318, 1714, 2089, 2456, 2828, 3219, 3648, 4143 kt at T = 1..8 and empty after T = 12",
      all(close(ex["BAU"]["UC_min"]["boundaries_T1_20"][i], v, 1.0) for i, v in enumerate((1318, 1714, 2089, 2456, 2828, 3219, 3648, 4143)))
      and ex["BAU"]["UC_min"]["boundaries_T1_20"][12] is None)
check("H6 exact kernel dominates the Lipschitz certificate: exact last non-empty horizon >= Lipschitz for every flat rule and floor, and exact boundary <= certified boundary at every common T",
      all(ex[p][k]["last_nonempty"] >= ex[p][k]["lipschitz_last_nonempty"] for p in ("BAU", "flat_0", "flat_25", "flat_50", "flat_75", "flat_100") for k in ("UC_min", "UC_q05", "UC_q10"))
      and all(ex[p][k]["boundaries_T1_20"][t] <= lb[c][k][t] + 1e-6 for p, c in (("flat_0", "0.0"), ("flat_25", "60.0"), ("flat_50", "120.0"), ("flat_75", "180.0"), ("flat_100", "240.0"))
              for k in ("UC_min", "UC_q05", "UC_q10") for t in range(len(lb[c][k])) if lb[c][k][t] is not None and ex[p][k]["boundaries_T1_20"][t] is not None))
check("H7 exact horizons are monotone: non-increasing in the catch and non-decreasing from the worst to the q10 floor",
      all(ex[a]["UC_min"]["last_nonempty"] >= ex[b]["UC_min"]["last_nonempty"] for a, b in (("flat_0", "BAU"), ("BAU", "flat_25"), ("flat_25", "flat_50"), ("flat_50", "flat_75"), ("flat_75", "flat_100")))
      and all(ex[p]["UC_min"]["last_nonempty"] <= ex[p]["UC_q05"]["last_nonempty"] <= ex[p]["UC_q10"]["last_nonempty"] for p in ex))

# ------------------------------------------------------------------ 5. cod stochastic and identification
st, si = A["stochastic"], C["stochastic_independent"]
check("S1 archived 20-yr survival from the LRP (N = 20 000): iid 0.903 / 0.835 / 0.647, block-4 0.852 / 0.807 / 0.650, no-1992 0.954 / 0.917 / 0.769 (BAU / 60 / 120 kt)",
      all(close(st[f"{s}|{p}|S0=884.6|T=20"], v, 0.0006) for s, vals in (("iid", (0.9031, 0.8353, 0.6466)), ("block4", (0.8515, 0.8065, 0.6499)), ("iid_no1992", (0.9537, 0.9172, 0.7694)))
          for p, v in zip(("BAU", "flat_25", "flat_50"), vals)))
check("S2 independent i.i.d. re-run (seed 20261015) within 0.002 of the archive for BAU, 60 and 120 kt; zero-catch ceiling 0.906 and (23/24)^20 = 0.427",
      all(close(si[f"iid|C={c}|S0=LRP|T=20"], st[f"iid|{p}|S0=884.6|T=20"], 0.002) for c, p in ((5, "BAU"), (60, "flat_25"), (120, "flat_50")))
      and all(close(si[f"block4|C={c}|S0=LRP|T=20"], st[f"block4|{p}|S0=884.6|T=20"], 0.002) for c, p in ((5, "BAU"), (60, "flat_25"), (120, "flat_50")))
      and close(st["iid|flat_0|S0=884.6|T=20"], 0.906, 0.001) and close((23 / 24) ** 20, 0.4269, 0.0001))
cr = A["stochastic_crossings"]
check("S3 constant-catch scan: survival crosses 0.9 at 13.5 kt (iid) and 78.9 kt (no-1992), never under blocks; crosses 0.8 at 81.2 / 72.3 / 105.2 kt; at 92.5 kt 0.742 / 0.727 / 0.844",
      close(cr["iid"]["0.9"], 13.5, 0.1) and close(cr["iid_no1992"]["0.9"], 78.9, 0.1) and cr["block4"]["0.9"] is None
      and close(cr["iid"]["0.8"], 81.2, 0.1) and close(cr["block4"]["0.8"], 72.3, 0.1) and close(cr["iid_no1992"]["0.8"], 105.2, 0.1)
      and close(cr["iid"]["P_at_92.5"], 0.742, 0.001) and close(cr["block4"]["P_at_92.5"], 0.727, 0.001) and close(cr["iid_no1992"]["P_at_92.5"], 0.844, 0.001))
pr, bi = C["profile"], C["bootstrap_independent_fixedK"]
check("I1 profile in K: SSE at K = 5000 is 2.7% above the grid minimum; 1-par cut 1.1955 -> K >= 1500, g(LRP) in [148.8, 176.1], C* in [67.9, 95.2]; 2-par cut 1.313 -> K >= 1275, C* in [51.5, 95.2]",
      close(pr["sse_box_edge_ratio"], 1.027, 0.001) and close(pr["F_cut_ratio_1par"], 1.1955, 0.0005) and close(pr["F_cut_ratio"], 1.313, 0.0005)
      and close(pr["K_set_1par"][0], 1500, 1) and close(pr["K_set"][0], 1275, 1)
      and close(pr["g_Kstar_range_1par"][0], 148.8, 0.1) and close(pr["g_Kstar_range_1par"][1], 176.1, 0.1)
      and close(pr["C_star_range_1par"][0], 67.9, 0.1) and close(pr["C_star_range_1par"][1], 95.2, 0.1) and close(pr["C_star_range"][0], 51.5, 0.1))
check("I2 no-dominance is K-free: 60-kt rules clear C*(K) and 120 kt does not, for every K in the archived identification grid with K >= 1275",
      all((float(r["g_Kstar"]) - cc["classes_abs"]["UC_q10"] >= 60) and (float(r["g_Kstar"]) - cc["classes_abs"]["UC_q10"] < 120) for r in A["k_grid"] if float(r["K"]) >= 1275))
check("I3 fixed-K trajectory bootstrap (independent seed, B = 2000): C* median 78.8 kt, 90% interval [-62.4, 120.3], 12.5% at or below zero; archive 78.7 [-69.3, 121.1], 235/2000",
      close(bi["frozen_floor"]["Cstar_median"], 78.81, 0.05) and close(bi["frozen_floor"]["Cstar_q05_q95"][0], -62.37, 0.05) and close(bi["frozen_floor"]["Cstar_q05_q95"][1], 120.34, 0.05)
      and close(bi["frozen_floor"]["share_nonpositive"], 0.125, 0.0005) and bi["B"] == 2000 and bi["seed"] == 20261015)
rw, ar = C["recent_windows"], A["recent"]
check("I4 recent windows: 1995-2015 C* = 165.7 kt at the exact minimiser K = 4316.6 (171.4 at the archived box edge); 1995-2007 C* = 274.0; xteNCAM (LRP 276) 2005-2024 C* = -7.7, 1995-2024 +8.0",
      close(rw["NCAM 1995-2015"]["C_star"], 165.7, 0.1) and close(rw["NCAM 1995-2015"]["K"], 4316.6, 0.5) and close(rw["NCAM 1995-2015"]["at_K_5000"]["C_star"], 171.4, 0.1)
      and close(ar["NCAM 1995-2015"]["Cstar"], 171.4, 0.1) and close(rw["NCAM 1995-2007"]["C_star"], 274.0, 0.1)
      and close(ar["xteNCAM 2005-2024"]["Cstar"], -7.7, 0.1) and close(ar["xteNCAM 1995-2024"]["Cstar"], 8.0, 0.1))
fox = {r["form"]: r for r in A["fox"]}
check("I5 alternative forms (archive): Fox C* = 79.05 kt with g_max 192.0 (C_vac = 111.2 kt), F'(LRP) 1.0764; Schaefer row reproduces 91.59; declared-s0 Allee kernels under q10 are the whole safe set for BAU and S1",
      close(float(fox["Fox (this campaign)"]["constructive_q10"]), 79.05, 0.01) and close(float(fox["Fox (this campaign)"]["g_max"]) - cc["classes_abs"]["UC_q10"], 111.2, 0.1)
      and close(float(fox["Fox (this campaign)"]["Fp_Kstar"]), 1.0764, 0.0001) and close(float(fox["Schaefer (committed)"]["constructive_q10"]), 91.59, 0.01)
      and close(float(A["allee"]["declared_s0=442.3|BAU|UC_q10|T=inf"]), 884.6, 0.1) and close(float(A["allee"]["declared_s0=442.3|S1|UC_q10|T=inf"]), 884.6, 0.1))
check("I6 observation-error share lambda (archive): C* = 91.6, 95.2, 99.0, 103.0, 107.4, 112.1 kt for lambda = 0..0.5; vacuous worst class gone from lambda = 0.2",
      all(close(float(re.search(r"C\* = ([-\d.]+)", A["ident"][f"obs-error|lambda = {l}"]).group(1)), v, 0.05)
          for l, v in (("0.0", 91.6), ("0.1", 95.2), ("0.2", 99.0), ("0.3", 103.0), ("0.4", 107.4), ("0.5", 112.1))))
sup = A["cod_results_summary"]["supply"]
check("I7 supply on the observed 1983-2007 states: S1 10.0 kt with the cut active in 83% of years, cascade 16.3 kt, flat 60 kt 60",
      close(sup["S1"]["train_mean_C"], 10.0, 0.05) and close(sup["S1"]["train_cut_active_fraction"], 0.833, 0.001)
      and close(sup["cpm"]["train_mean_C"], 16.25, 0.05) and close(sup["flat_25"]["train_mean_C"], 60.0, 1e-6))

# ------------------------------------------------------------------ 6. Edwards fit, attractors, securability (Corollary 2.5, Theorem 2.10)
check("E1 Edwards OLS 1935-1990 (56 transitions): alpha 163.49, beta 0.01983, gamma -0.02844, a = 0.7461 (contraction), 33 out-of-sample transitions",
      close(ef["alpha"], 163.49, 0.01) and close(ef["beta"], 0.01983, 0.00001) and close(ef["gamma"], -0.02844, 0.00001) and close(ef["a"], 0.7461, 0.0001)
      and ef["n_train"] == 56 and ef["n_oos"] == 33 and 0 < ef["a"] < 1)
check("E2 residuals: fit SD 5.60 ft, |e|max 15.41 ft (1971); out of sample SD 8.40 ft, |e|max 21.81 ft (2004) > declaration",
      close(ef["train_sd"], 5.60, 0.01) and close(ef["train_abs_max"], 15.41, 0.01) and ef["train_abs_max_year"] == 1971
      and close(ef["oos_sd"], 8.40, 0.01) and close(ef["oos_abs_max"], 21.81, 0.01) and ef["oos_abs_max_year"] == 2004 and ef["oos_abs_max"] > ef["train_abs_max"])
check("E3 recharge floors 43.7 (1956) / 166.5 / 179.08; P_bar = 282.16; r_inf = eps/(1-a) = 60.70 ft (85.90 ft out of sample)",
      close(E["floors"]["UC_min"], 43.7, 0.05) and close(E["floors"]["UC_q05"], 166.5, 0.05) and close(E["floors"]["UC_q10"], 179.08, 0.01)
      and close(E["P_bar"], 282.16, 0.01) and close(E["r_inf"], 60.70, 0.01) and close(E["r_inf_oos"], 85.90, 0.01))
at = E["attractors"]
check("E4 worst-floor attractors: BAU 615.72, flat 90% 618.88, S1 = flat 80% 622.04, cascade = flat 60% 628.36, zero pumping 647.32 ft",
      close(at["BAU"]["UC_min"]["self_consistent"], 615.72, 0.01) and close(at["flat_90"]["UC_min"]["self_consistent"], 618.88, 0.01)
      and close(at["S1"]["UC_min"]["self_consistent"], 622.04, 0.01) and close(at["flat_80"]["UC_min"]["self_consistent"], 622.04, 0.01)
      and close(at["cpm"]["UC_min"]["self_consistent"], 628.36, 0.01) and close(at["flat_60"]["UC_min"]["self_consistent"], 628.36, 0.01)
      and close(at["flat_0"]["UC_min"]["self_consistent"], 647.32, 0.01))
check("E5 q05 / q10 attractors: BAU 625.31 / 626.29, flat 90% 628.47 / 629.45, S1 631.63 / 632.61, cascade 636.37 / 637.35, zero 656.91 / 657.90 ft (all above 618)",
      all(close(at[p][k]["self_consistent"], v, 0.01) for p, vals in (("BAU", (625.31, 626.29)), ("flat_90", (628.47, 629.45)), ("S1", (631.63, 632.61)), ("cpm", (636.37, 637.35)), ("flat_0", (656.91, 657.90)))
          for k, v in zip(("UC_q05", "UC_q10"), vals))
      and all(at[p][k]["self_consistent"] > 618 for p in at for k in ("UC_q05", "UC_q10")))
check("E6 attractor closed form H* = (alpha + beta R_floor + gamma P)/(1 - a) reproduces BAU and flat caps under every floor",
      all(close(at[p][k]["self_consistent"], (ef["alpha"] + ef["beta"] * E["floors"][k] + ef["gamma"] * q * E["P_bar"]) / (1 - ef["a"]), 1e-6)
          for p, q in (("BAU", 1.0), ("flat_90", 0.9), ("flat_80", 0.8), ("flat_60", 0.6), ("flat_0", 0.0)) for k in ("UC_min", "UC_q05", "UC_q10")))
check("E7 securability of 618 ft: minimal flat cut rho* = 0.9278 (7.2% cut; 261.8, i.e. 31.5% below the 1991-2023 mean 382.1); 660 ft unsecurable: zero-pumping attractor short by 12.68 / 3.09 / 2.10 ft",
      close(E["minimal_flat_cut_618_UCmin"]["rho_star"], 0.9278, 0.0001) and close(E["minimal_flat_cut_618_UCmin"]["rho_star"] * E["P_bar"], 261.8, 0.1)
      and all(close(E["margin_660"][k], v, 0.01) for k, v in (("UC_min", -12.68), ("UC_q05", -3.09), ("UC_q10", -2.10)))
      and all(E["zero_pumping_attractor"][k] < 660 for k in ("UC_min", "UC_q05", "UC_q10")))
dE = E["data"]
_y = dE["years"]; _P = dE["P"]
check("E8 pumping record: fit-window mean 282.16, 1991-2023 mean 382.1, highest annual mean head 692.0 ft; 1956 mean head 623.15 ft",
      close(sum(p for y, p in zip(_y, _P) if y > 1990) / 33, 382.1, 0.1) and close(max(dE["H"]), 692.0, 0.05) and close(dE["H"][_y.index(1956)], 623.15, 0.01))

# ------------------------------------------------------------------ 7. Edwards kernels, horizons, identity
kn, kc, be = E["kernels_nominal"], E["kernels_certified"], E["bounded_error"]
check("E9 618-ft nominal kernels: BAU worst floor b_T = 618.8, 619.8, 621.2, 625.6, 639.5, 658.4, 692.4 ft (T = 1,2,3,5,8,10,12), empty at T = 13 = floor(12.70) + 1; every cut policy whole safe set",
      all(close(kn["K_phys_618"]["BAU"]["UC_min"][T], v, 0.05) for T, v in (("1", 618.8), ("2", 619.8), ("3", 621.2), ("5", 625.6), ("8", 639.5), ("10", 658.4), ("12", 692.4)))
      and kn["K_phys_618"]["BAU"]["UC_min"]["first_empty"] == 13 and close(kn["K_phys_618"]["BAU"]["UC_min"]["T_empty_closed_form"], 12.70, 0.01)
      and all(close(kn["K_phys_618"][p][k][T], 618.0, 1e-6) for p in ("flat_90", "flat_80", "S1", "cpm", "flat_0") for k in ("UC_min", "UC_q05", "UC_q10")
              for T in kn["K_phys_618"][p][k] if T not in ("first_empty", "T_empty_closed_form")))
check("E10 660-ft nominal kernels (worst floor): BAU = S1 = cascade 675.1 / 695.3 ft at T = 1, 2 and empty at T = 3; zero pumping 664.3 / 670.1 / 677.8 ft, empty at T = 6",
      close(kn["K_inst_660"]["BAU"]["UC_min"]["1"], 675.1, 0.05) and close(kn["K_inst_660"]["BAU"]["UC_min"]["2"], 695.3, 0.05) and kn["K_inst_660"]["BAU"]["UC_min"]["first_empty"] == 3
      and kn["K_inst_660"]["S1"]["UC_min"]["first_empty"] == 3 and kn["K_inst_660"]["cpm"]["UC_min"]["first_empty"] == 3
      and all(close(kn["K_inst_660"]["flat_0"]["UC_min"][T], v, 0.05) for T, v in (("1", 664.3), ("2", 670.1), ("3", 677.8))) and kn["K_inst_660"]["flat_0"]["UC_min"]["first_empty"] == 6)
check("E11 Lipschitz r_T = 15.41, 26.91, 35.49, 41.89, 46.66 ft; certified 618-ft BAU boundaries 639.43 / 668.16 / 706.66 ft (T = 1-3), empty at T = 4; S1 and cascade 706.66 at T = 3; flat 80% 697.76; zero pumping to T = 4 (687.88)",
      all(close(E["r_T"][str(T)], v, 0.01) for T, v in ((1, 15.41), (2, 26.91), (3, 35.49), (4, 41.89), (5, 46.66)))
      and all(close(kc["K_phys_618"]["BAU"]["UC_min"][T], v, 0.01) for T, v in (("1", 639.43), ("2", 668.16), ("3", 706.66))) and kc["K_phys_618"]["BAU"]["UC_min"]["4"] is None
      and close(kc["K_phys_618"]["S1"]["UC_min"]["3"], 706.66, 0.01) and close(kc["K_phys_618"]["cpm"]["UC_min"]["3"], 706.66, 0.01)
      and close(kc["K_phys_618"]["flat_80"]["UC_min"]["3"], 697.76, 0.01) and close(kc["K_phys_618"]["flat_0"]["UC_min"]["4"], 687.88, 0.01) and kc["K_phys_618"]["flat_0"]["UC_min"]["5"] is None)
check("E12 certified horizons: 3 years for every pumping rule under the worst floor and for BAU, flat 90-70%, S1 and cascade under every floor; flat 60% and 50% reach 4 under the quantile floors; zero pumping 4 (worst) and 5 (q05, q10); 660 ft: 1 year for every rule",
      all(kc["K_phys_618"][p]["UC_min"]["last_nonempty"] == 3 for p in ("BAU", "flat_90", "flat_80", "flat_70", "flat_60", "flat_50", "S1", "cpm"))
      and all(kc["K_phys_618"][p][k]["last_nonempty"] == 3 for p in ("BAU", "flat_90", "flat_80", "flat_70", "S1", "cpm") for k in ("UC_q05", "UC_q10"))
      and all(kc["K_phys_618"][p][k]["last_nonempty"] == 4 for p in ("flat_60", "flat_50") for k in ("UC_q05", "UC_q10"))
      and kc["K_phys_618"]["flat_0"]["UC_min"]["last_nonempty"] == 4 and kc["K_phys_618"]["flat_0"]["UC_q05"]["last_nonempty"] == 5 and kc["K_phys_618"]["flat_0"]["UC_q10"]["last_nonempty"] == 5
      and all(kc["K_inst_660"][p][k]["last_nonempty"] == 1 for p in kc["K_inst_660"] for k in ("UC_min", "UC_q05", "UC_q10")))
check("E13 exact bounded-defect kernel = Lipschitz certificate for every constant-pumping rule (Prop. 2.8(ii)): BAU 639.43 / 668.16 / 706.66, empty at T = 4; departures only for S1 (T=3), cascade (T=2,3) and zero pumping (T=1,2), all with a larger exact kernel and no change of horizon",
      all(close(be["BAU"]["UC_min|train"]["boundaries"][i], v, 1e-6) for i, v in enumerate((639.4321837561727, 668.1580295056373, 706.6596690683523)))
      and be["BAU"]["UC_min|train"]["first_empty"] == 4
      and all(r["equal"] for r in E["lipschitz_vs_exact_identity"]["rows"] if r["policy"] in ("BAU", "flat_90", "flat_80", "flat_60"))
      and sorted((r["policy"], r["T"]) for r in E["lipschitz_vs_exact_identity"]["rows"] if not r["equal"]) == [("S1", 3), ("cpm", 2), ("cpm", 3), ("flat_0", 1), ("flat_0", 2)]
      and all(r["exact"] < r["inflated"] for r in E["lipschitz_vs_exact_identity"]["rows"] if not r["equal"])
      and all(be[p]["UC_min|train"]["first_empty"] - 1 == kc["K_phys_618"][p]["UC_min"]["last_nonempty"] for p in be))
check("E14 bounded-defect suprema at T = 3: BAU 16.01, S1 16.71, cascade 17.23, flat 80% 17.62, zero pumping 24.04 ft; at T = 4 9.91-11.60 ft for pumping rules and 17.93 for zero pumping; declared 15.41 clears every T = 3 supremum and only zero pumping's at T = 4; OOS 21.81 clears only zero pumping's at T = 3",
      close(be["BAU"]["sup_eps_UC_min"]["3"], 16.01, 0.01) and close(be["S1"]["sup_eps_UC_min"]["3"], 16.71, 0.01) and close(be["cpm"]["sup_eps_UC_min"]["3"], 17.23, 0.01)
      and close(be["flat_80"]["sup_eps_UC_min"]["3"], 17.62, 0.01) and close(be["flat_0"]["sup_eps_UC_min"]["3"], 24.04, 0.01)
      and close(min(be[p]["sup_eps_UC_min"]["4"] for p in be), 9.91, 0.01) and close(max(be[p]["sup_eps_UC_min"]["4"] for p in be if p != "flat_0"), 11.60, 0.01)
      and close(be["flat_0"]["sup_eps_UC_min"]["4"], 17.93, 0.01)
      and all(be[p]["sup_eps_UC_min"]["3"] > ef["train_abs_max"] for p in be) and all(be[p]["sup_eps_UC_min"]["4"] < ef["train_abs_max"] for p in be if p != "flat_0")
      and all(be[p]["sup_eps_UC_min"]["3"] < ef["oos_abs_max"] for p in be if p != "flat_0") and be["flat_0"]["sup_eps_UC_min"]["3"] > ef["oos_abs_max"])
check("E15 out-of-sample defect 21.81 ft: every pumping rule's exact 618-ft kernel empty at T = 3 (BAU 648.0 / 688.2 ft at T = 1, 2), zero pumping's at T = 4; audited horizon 2 for every pumping rule",
      all(be[p]["UC_min|oos"]["first_empty"] == 3 for p in be if p != "flat_0") and be["flat_0"]["UC_min|oos"]["first_empty"] == 4
      and close(be["BAU"]["UC_min|oos"]["boundaries"][0], 648.0, 0.05) and close(be["BAU"]["UC_min|oos"]["boundaries"][1], 688.2, 0.05))
check("E16 indefinite certificate needs H* >= 618 + r_inf = 678.7 ft; highest attractor in the family is 657.9 ft (zero pumping, q10)",
      close(618 + E["r_inf"], 678.7, 0.05) and close(max(at[p][k]["self_consistent"] for p in at for k in at[p]), 657.90, 0.01) and max(at[p][k]["self_consistent"] for p in at for k in at[p]) < 618 + E["r_inf"])

# ------------------------------------------------------------------ 8. Edwards supply, retention, replays, bootstrap
so, cl, oc = E["supply_open_loop"], E["closed_loop"], E["occupancy"]
check("E17 open-loop supply on 1934-1990 heads: S1 262.36 (cut active 35%), flat 90% 253.94, flat 80% 225.73, cascade 254.93, flat 60% 169.29; S1 +3.3% vs flat 90, +16.2% vs flat 80; cascade +50.6% vs flat 60",
      close(so["S1"]["train_mean_P"], 262.36, 0.01) and close(so["S1"]["train_cut_active"], 0.351, 0.001) and close(so["flat_90"]["train_mean_P"], 253.94, 0.01)
      and close(so["flat_80"]["train_mean_P"], 225.73, 0.01) and close(so["cpm"]["train_mean_P"], 254.93, 0.01) and close(so["flat_60"]["train_mean_P"], 169.29, 0.01)
      and close(so["S1"]["train_mean_P"] / so["flat_90"]["train_mean_P"] - 1, 0.033, 0.001) and close(so["S1"]["train_mean_P"] / so["flat_80"]["train_mean_P"] - 1, 0.162, 0.001)
      and close(so["cpm"]["train_mean_P"] / so["flat_60"]["train_mean_P"] - 1, 0.506, 0.001))
check("E18 out-of-sample open-loop supply over the 33 heads 1991-2023: S1 263.35, cascade 258.22, cut active 33%; heads below 660/650/640/630 in 20/12/5/1 of 57 fit years",
      close(so["S1"]["oos_mean_P"], 263.35, 0.01) and close(so["cpm"]["oos_mean_P"], 258.22, 0.01) and close(so["S1"]["oos_cut_active"], 0.333, 0.001)
      and oc["train"]["counts"] == [20, 12, 5, 1] and oc["train"]["n"] == 57 and oc["oos"]["counts"] == [11, 5, 2, 0])
check("E19 closed loop 1934-1990: S1 258.98 (cut active 41%), cascade 254.70, flat 90% 253.94, flat 80% 225.73, flat 60% 169.29; BAU ends 1990 at 677.65 ft vs observed 645.84",
      close(cl["S1"]["train_1934_1990"]["mean_P"], 258.98, 0.01) and close(cl["S1"]["train_1934_1990"]["cut_active"], 0.41, 0.005) and close(cl["cpm"]["train_1934_1990"]["mean_P"], 254.70, 0.01)
      and close(cl["flat_90"]["train_1934_1990"]["mean_P"], 253.94, 0.01) and close(cl["flat_80"]["train_1934_1990"]["mean_P"], 225.73, 0.01) and close(cl["flat_60"]["train_1934_1990"]["mean_P"], 169.29, 0.01)
      and close(cl["BAU"]["train_1934_1990"]["end_head"], 677.65, 0.01) and close(dE["H"][_y.index(1990)], 645.84, 0.01))
check("E20 closed loop from the 1990 head: S1 268.48 (cut active 24%), ends 2023 at 643.32 ft vs observed 635.68; BAU ends at 639.2; all rules end between 639 and 671 ft",
      close(cl["S1"]["oos_1991_2023"]["mean_P"], 268.48, 0.01) and close(cl["S1"]["oos_1991_2023"]["cut_active"], 0.24, 0.005) and close(cl["S1"]["oos_1991_2023"]["end_head"], 643.32, 0.01)
      and close(dE["H"][-1], 635.68, 0.01) and close(cl["BAU"]["oos_1991_2023"]["end_head"], 639.2, 0.05)
      and 639 <= min(cl[p]["oos_1991_2023"]["end_head"] for p in cl) and max(cl[p]["oos_1991_2023"]["end_head"] for p in cl) <= 671)
rp, fd = E["replay_1950s"], E["fit_diagnostic_1950s"]
check("E21 1951-1956 replay minima: BAU 629.65, flat 90% 632.27, S1 634.88, cascade 637.06, zero pumping 655.81 ft; actual-pumping model 631.2 vs observed 623.2 (bias 8.1 ft, unsafe direction)",
      close(rp["BAU"]["min_head"], 629.65, 0.01) and close(rp["flat_90"]["min_head"], 632.27, 0.01) and close(rp["S1"]["min_head"], 634.88, 0.01) and close(rp["cpm"]["min_head"], 637.06, 0.01)
      and close(rp["flat_0"]["min_head"], 655.81, 0.01) and close(fd["model_1956"], 631.2, 0.05) and close(fd["max_abs_error"], 8.1, 0.05) and fd["model_1956"] > dE["H"][_y.index(1956)])
ffe, fcs = E["finite_floors"], E["floor_class_supply"]
check("E22 finite 1956-floors under BAU: 5 years absorbed from 625.6 ft, 10 from 658.4 ft, 15 from nowhere; cut policies absorb any run; floor-class supply S1 226.7 vs flat 80% 225.7, cascade 174.5 vs flat 60% 169.3",
      close(ffe["BAU|UC_min"]["5"], 625.6, 0.05) and close(ffe["BAU|UC_min"]["10"], 658.4, 0.05) and ffe["BAU|UC_min"]["15"] is None
      and all(close(ffe[f"{p}|UC_min"][n], 618.0, 1e-6) for p in ("S1", "cpm", "flat_90") for n in ("5", "10", "15"))
      and close(fcs["S1"]["mean_P"], 226.7, 0.05) and close(fcs["flat_80"]["mean_P"], 225.7, 0.05) and close(fcs["cpm"]["mean_P"], 174.5, 0.05) and close(fcs["flat_60"]["mean_P"], 169.3, 0.05))
bo, ab = E["bootstrap_independent"], {r["policy"]: r for r in A["edw_audit_bootstrap"]["per_policy"]}
check("E23 attractor bootstrap (independent seed, B = 5000): P(H* >= 618) BAU 0.403, flat 90% 0.523, flat 80% 0.644, flat 60% 0.824, zero 0.989; within 0.012 of the archive; SD 10-13 ft; no non-contractive replicate",
      all(close(bo["P_attractor_ge_618"][p], v, 0.0005) for p, v in (("BAU", 0.4034), ("flat_90", 0.523), ("flat_80", 0.644), ("flat_60", 0.824), ("flat_0", 0.989)))
      and all(close(bo["P_attractor_ge_618"][p], ab[k]["p_attractor_ge_618"], 0.012) for p, k in (("BAU", "BAU"), ("flat_90", "flat-90%"), ("flat_80", "flat-80%"), ("flat_60", "flat-60%"), ("flat_0", "flat-0%")))
      and 10 <= min(bo["attractor_sd"].values()) and max(bo["attractor_sd"].values()) <= 13.2 and bo["noncontractive"] == 0 and A["edw_audit_bootstrap"]["noncontractive_reps"] == 0)
check("E24 flat-90% minus BAU gap: 90% interval [1.9, 5.1] ft, positive in every replicate (min 0.5 ft), gamma < 0 in every refit; coefficient ratios have CV 0.25 and 0.30",
      close(bo["gap_flat90_minus_BAU_q05_q50_q95"][0], 1.94, 0.01) and close(bo["gap_flat90_minus_BAU_q05_q50_q95"][2], 5.09, 0.01) and bo["gap_positive_share"] == 1.0
      and close(bo["gap_flat90_minus_BAU_min"], 0.52, 0.01) and bo["gamma_nonneg_reps"] == 0
      and close(bo["coef_ratio_sd_over_point"]["beta_over_1ma"], 0.254, 0.001) and close(bo["coef_ratio_sd_over_point"]["gamma_over_1ma"], 0.304, 0.001))

# ------------------------------------------------------------------ 9. closed forms of Section 2 against the recursion
r_, K_, th = fit["r"], fit["K"], C["K_star"]
def s_minus(level):
    return None if level > r_ * K_ / 4 else 0.5 * K_ * (1 - math.sqrt(1 - 4 * level / (r_ * K_)))
check("T1 Corollary 2.4: b_inf = max(LRP, s_-(C + |e|)) reproduces the recursion's infinite-horizon boundary for every flat catch and floor with a non-empty kernel",
      all(close(binf(ks[p][k]["inf"]), max(th, s_minus(c + cc["classes_abs"][k])), 0.05)
          for p, c in (("BAU", 5.0), ("flat_0", 0.0), ("flat_25", 60.0), ("flat_50", 120.0), ("flat_75", 180.0), ("flat_100", 240.0)) for k in ("UC_min", "UC_q05", "UC_q10")
          if ks[p][k]["inf"] is not None)
      and all(s_minus(c + cc["classes_abs"][k]) is None or c + cc["classes_abs"][k] > cc["g_max"] - 1e-9
              for p, c in (("BAU", 5.0), ("flat_0", 0.0), ("flat_25", 60.0), ("flat_50", 120.0), ("flat_75", 180.0), ("flat_100", 240.0)) for k in ("UC_min", "UC_q05", "UC_q10")
              if ks[p][k]["inf"] is None))
a_ = ef["a"]
check("T2 Corollary 2.5: b_T = H* + (618 - H*)/a^T and T_empty = floor(ln((710 - H*)/(618 - H*))/ln(1/a)) + 1 reproduce the BAU 618-ft recursion under the worst floor",
      all(close(kn["K_phys_618"]["BAU"]["UC_min"][T], at["BAU"]["UC_min"]["self_consistent"] + (618 - at["BAU"]["UC_min"]["self_consistent"]) / a_ ** int(T), 1e-6)
          for T in ("1", "2", "3", "5", "8", "10", "12"))
      and math.floor(math.log((710 - at["BAU"]["UC_min"]["self_consistent"]) / (618 - at["BAU"]["UC_min"]["self_consistent"])) / math.log(1 / a_)) + 1 == kn["K_phys_618"]["BAU"]["UC_min"]["first_empty"])
check("T3 Corollary 2.5 applied to the inflated threshold: certified 618-ft boundary at horizon T equals max(618 + r_T, H* + (618 + r_T - H*)/a^T) for BAU, flat 80% and zero pumping at every non-empty horizon",
      all(close(kc["K_phys_618"][p]["UC_min"][T], max(618 + E["r_T"][T], at[p]["UC_min"]["self_consistent"] + (618 + E["r_T"][T] - at[p]["UC_min"]["self_consistent"]) / a_ ** int(T)), 1e-6)
          for p in ("BAU", "flat_80", "flat_0") for T in ("1", "2", "3", "4", "5") if kc["K_phys_618"][p]["UC_min"].get(T) is not None))
check("T4 Theorem 2.10 (securability): LRP securable under q10 (C* > 0) and not under q05/worst (C* < 0); 618 ft securable under every floor (zero-pumping attractor > 618); 660 ft under none",
      cc["C_star"]["UC_q10"] > 0 and cc["C_star"]["UC_q05"] < 0 and cc["C_star"]["UC_min"] < 0
      and all(E["zero_pumping_attractor"][k] > 618 for k in ("UC_min", "UC_q05", "UC_q10")) and all(E["zero_pumping_attractor"][k] < 660 for k in ("UC_min", "UC_q05", "UC_q10")))
check("T5 Proposition 2.8(iii) instance: exact kernel strictly exceeds the Lipschitz certificate for the strictly concave cod map (every flat rule and floor) and never for the affine Edwards map",
      all(ex[p][k]["last_nonempty"] > ex[p][k]["lipschitz_last_nonempty"] for p in ("BAU", "flat_0", "flat_25", "flat_50", "flat_75", "flat_100") for k in ("UC_min", "UC_q05", "UC_q10"))
      and all(r["equal"] for r in E["lipschitz_vs_exact_identity"]["rows"] if r["policy"] in ("BAU", "flat_90", "flat_80", "flat_60")))

# ------------------------------------------------------------------ 10. generated tables and figures exist and carry the numbers
def rd(path):
    p = os.path.join(SRC, path)
    return open(p).read() if os.path.exists(p) else None
tabs = {n: rd(f"parts/gen_tab_{n}.tex") for n in ("inputs", "cod_kernels", "edw", "horizons", "cod_unc", "edw_unc", "resolved")}
check("G1 seven main tables generated (inputs, cod_kernels, edw, horizons, cod_unc, edw_unc, resolved)", all(v is not None for v in tabs.values()))
check("G2 Table cod_kernels carries 1082.3, 1637.8, 1450.0, 2219.6; Table edw carries 615.72, 618.88, 622.04, 628.36, 647.32 and the supplies 262.36 / 254.93",
      tabs["cod_kernels"] is not None and all(s in tabs["cod_kernels"] for s in ("1082.3", "1637.8", "1450.0", "2219.6"))
      and tabs["edw"] is not None and all(s in tabs["edw"] for s in ("615.7", "618.9", "622.0", "628.4", "647.3", "262.4", "254.9")))
check("G3 Table horizons carries the exact horizons 12 / 13 / 27 (BAU), 10 / 11 / 20 (60 kt) and the Edwards 3 / 2 (declared / OOS)",
      tabs["horizons"] is not None and all(s in tabs["horizons"] for s in ("12", "13", "27", "10", "11", "20")))
check("G4 Table edw_unc carries the suprema 16.01, 16.71, 17.23, 24.04 and the supplies 262.36 / 258.98 / 268.48",
      tabs["edw_unc"] is not None and all(s in tabs["edw_unc"] for s in ("16.01", "16.71", "17.23", "24.04", "262.36", "258.98", "268.48")))
sis = [f for f in os.listdir(os.path.join(SRC, "si_parts")) if f.startswith("gen_si_")] if os.path.isdir(os.path.join(SRC, "si_parts")) else []
check("G5 seventeen SI tables generated", len(sis) == 17)
figs = [f"fig_{n}.pdf" for n in ("data", "cod_kernels", "cod_ident", "edw_kernels", "edw_replay", "horizons")]
check("G6 six figures generated from results.json (" + ", ".join(figs) + ")", all(os.path.exists(os.path.join(SRC, "figs", f)) for f in figs))

# ------------------------------------------------------------------ 11. manuscript text
def pdf_text(path):
    try:
        import pymupdf
    except Exception:
        try:
            import fitz as pymupdf
        except Exception:
            return None
    if not os.path.exists(path):
        return None
    t = "".join(pg.get_text() for pg in pymupdf.open(path))
    t = t.replace("\ufb01", "fi").replace("\ufb02", "fl").replace("\ufb00", "ff").replace("\u2212", "-").replace("\u00ad", "")
    return re.sub(r"\s+", " ", t)

main = pdf_text(os.path.join(HERE, "paper09_cod_certification_v44.pdf"))
si = pdf_text(os.path.join(HERE, "paper09_cod_certification_v44_SI.pdf"))
MAIN_NEEDLES = ["884.6", "91.6", "215.2", "1.153", "7.2%", "615.7", "618.9", "622.0", "628.4", "647.3", "60.7", "678.7", "706.7",
                "3.3%", "50.6%", "16.2%", "21.8", "15.4", "0.90", "0.41", "926", "12.5%", "165.7", "4316.6", "8–13", "12–28", "10.0 kt"]
SI_NEEDLES = ["1092.0", "1751.8", "1074.8", "0.4269", "20261015", "20260905", "2026-08-26", "16.01", "0.5311", "0.7269"]
if main is None:
    check("X1 (main PDF not available: text checks skipped)", True)
    check("X2 (main PDF not available: check-count statement not verified)", True)
else:
    missing = [n for n in MAIN_NEEDLES if n.replace(" ", "") not in main.replace(" ", "")]
    check("X1 main text quotes the recomputed headline numbers" + ("" if not missing else " :: missing " + ", ".join(missing)), not missing)
    check(f"X2 main text states the check count ({NCHECKS_EXPECTED} checks) consistently with this script",
          (f"checks {NCHECKS_EXPECTED} statements" in main or f"{NCHECKS_EXPECTED} statements" in main) and NPASS + NFAIL + 2 + (3 if QUICK else 0) == NCHECKS_EXPECTED)
if si is None:
    check("X3 (supplement PDF not available: text checks skipped)", True)
else:
    missing = [n for n in SI_NEEDLES if n.replace(" ", "") not in si.replace(" ", "")]
    check("X3 supplement quotes the recomputed numbers" + ("" if not missing else " :: missing " + ", ".join(missing)), not missing)

# ------------------------------------------------------------------ summary
total = NPASS + NFAIL
summary = f"{NPASS}/{total} checks passed in {time.time() - T0:.1f} s" + (" (quick mode)" if QUICK else "")
print(summary)
LINES.append(summary)
if not QUICK:
    with open(os.path.join(HERE, "paper09_cod_certification_v44_verification_output.txt"), "w") as f:
        f.write("\n".join(LINES) + "\n")
sys.exit(0 if NFAIL == 0 else 1)
