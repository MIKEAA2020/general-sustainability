"""Verification for paper11_forecasting_baselines v68 (two-system edition).

Reads the archived data/results and the manuscript sources and asserts:
  (a) the carried-forward cod outcome-year, vintage and threshold checks;
  (b) printed Edwards tables against the archived rolling results;
  (c) baseline horizon profiles and full-sample autocorrelations;
  (d) the exact rolling-origin J-17 increment identity, unclipped and clipped
      MSE gaps, and agreement with archived forecasts;
  (e) the deterministic cod power archive, including hashes, seed/row coverage,
      the two-horizon retention rule and raw-to-summary agreement;
  (f) textual invariants, including separate score-gate and class claims.
Standard library only. Run: python3 paper11_forecasting_baselines_v68_verification.py
Layout: the script looks for work/ next to itself or in
paper11_forecasting_baselines_v68_src/ (the repository layout).
"""
import csv, hashlib, json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  ok  {name} {detail}")
    else:
        FAIL += 1
        print(f"FAIL  {name} {detail}")


def locate(rel):
    for base in (HERE, os.path.join(HERE, "paper11_forecasting_baselines_v68_src")):
        p = os.path.join(base, rel)
        if os.path.exists(p):
            return p
    raise FileNotFoundError(rel)


def rows(rel):
    with open(locate(rel), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def ac(x, k):
    n = len(x); m = sum(x) / n
    num = sum((x[i + k] - m) * (x[i] - m) for i in range(n - k))
    den = sum((v - m) ** 2 for v in x)
    return num / den


def pearson(a, b):
    n = len(a); ma = sum(a) / n; mb = sum(b) / n
    sa = math.sqrt(sum((v - ma) ** 2 for v in a)); sb = math.sqrt(sum((v - mb) ** 2 for v in b))
    return sum((a[i] - ma) * (b[i] - mb) for i in range(n)) / (sa * sb)


def profile(S, first, hmax=5):
    out = {}
    for h in range(1, hmax + 1):
        ep, em = [], []
        for i in range(first, len(S) - h):
            ep.append(S[i + h] - S[i]); em.append(S[i + h] - sum(S[: i + 1]) / (i + 1))
        out[h] = (len(ep), math.sqrt(sum(e * e for e in ep) / len(ep)), math.sqrt(sum(e * e for e in em) / len(em)))
    return out


# ---------- sources ----------
tex_main = open(os.path.join(HERE, "paper11_forecasting_baselines_v68.tex"), encoding="utf-8").read()
tex_si = open(os.path.join(HERE, "paper11_forecasting_baselines_v68_supplementary.tex"), encoding="utf-8").read()
tex = tex_main + "\n" + tex_si
flat = " ".join(tex.split())

# ---------- cod data ----------
COD = "work/cod/rerun/data/"
a2 = {int(r["year"]): float(r["ssb_kt"]) for r in rows(COD + "ncam_2016_table_a2.csv")}
ram = {int(r["year"]): float(r["SSB"]) / 1000.0 for r in rows(COD + "paperE1_calibration_data_v1_ram_timeseries.csv") if r["SSB"]}
xt = {int(r["year"]): (float(r["ssb_kt"]), float(r["ssb_over_blim"])) for r in rows(COD + "xtencam_table17_ssb.csv")}
cap = {int(r["year"]): float(r["acoustic_kt"]) for r in rows(COD + "capelin_acoustic_observed.csv")}

print("--- (a) cod: outcome years, vintages, thresholds (SI S10-S12) ---")
lrp = sum(a2[y] for y in range(1983, 1990)) / 7
check("A2 33 years 1983-2015", sorted(a2) == list(range(1983, 2016)))
check("LRP 1983-89 mean = 884.58", abs(lrp - 884.58) < 0.005, f"({lrp:.2f})")
check("2015 SSB 298.65 = 33.8% LRP", abs(a2[2015] - 298.65) < 1e-9 and abs(a2[2015] / lrp - 0.3376) < 5e-4)
out = {y: ram[y] for y in range(2016, 2022)}
check("RAM outcome values", out == {2016: 340.0, 2017: 433.0, 2018: 394.0, 2019: 419.0, 2020: 440.0, 2021: 411.0})
check("RAM 2015 origin = 277", ram[2015] == 277.0)
errs = [abs(out[y] - ram[2015]) for y in out]
check("persistence MAE = 129.2", abs(sum(errs) / 6 - 129.17) < 0.005, f"({sum(errs)/6:.2f})")
check("persistence RMSE = 133.3", abs(math.sqrt(sum(e * e for e in errs) / 6) - 133.34) < 0.005,
      f"({math.sqrt(sum(e*e for e in errs)/6):.2f})")
errs_a2 = [abs(out[y] - a2[2015]) for y in out]
check("A2-origin MAE = 107.5", abs(sum(errs_a2) / 6 - 107.52) < 0.005, f"({sum(errs_a2)/6:.2f})")
check("increase regime (all years above origin)", all(ram[y] > ram[2015] for y in range(2016, 2022)))
conc = [abs(ram[y] - xt[y][0]) for y in range(2016, 2022)]
check("vintage concordance: max 26, mean 16.8", max(conc) == 26.0 and abs(sum(conc) / 6 - 16.83) < 0.005,
      f"(max {max(conc)}, mean {sum(conc)/6:.2f})")
d = {y: a2[y] - ram[y] for y in range(1983, 2016)}
mad = sum(abs(v) for v in d.values()) / 33
check("A2-RAM mean signed +24.7", abs(sum(d.values()) / 33 - 24.7) < 0.05, f"({sum(d.values())/33:.1f})")
check("A2-RAM mean abs 26.8", abs(mad - 26.8) < 0.05, f"({mad:.1f})")
ymax = max(d, key=lambda y: abs(d[y]))
check("A2-RAM max abs 131.2 @1984", ymax == 1984 and abs(abs(d[ymax]) - 131.2) < 0.05, f"({abs(d[ymax]):.1f})")
lrp_ram = sum(ram[y] for y in range(1983, 1990)) / 7
check("RAM-vintage LRP = 790.00", abs(lrp_ram - 790.0) < 0.005, f"({lrp_ram:.2f})")
check("LRP shift = 94.6 kt", abs((lrp - lrp_ram) - 94.58) < 0.01, f"({lrp - lrp_ram:.2f})")
check("Table 17 covers 1954-2024 (71 rows)", sorted(xt) == list(range(1954, 2025)))
below = [y for y in sorted(xt) if xt[y][1] < 1.0]
check("below Blim: 26 years (1977-79, 1993-2015)", below == list(range(1977, 1980)) + list(range(1993, 2016)))
above884 = [y for y in sorted(xt) if xt[y][0] >= 884.6]
check("above 884.6: 16 years (1954-1969)", above884 == list(range(1954, 1970)))
dis = [y for y in sorted(xt) if (xt[y][1] >= 1.0) != (xt[y][0] >= 884.6)]
check("disagreement years = 29", len(dis) == 29, f"({len(dis)})")
check("outcome window 6/6 above Blim, 0/6 above LRP",
      all(xt[y][1] >= 1.0 for y in range(2016, 2022)) and not any(xt[y][0] >= 884.6 for y in range(2016, 2022)))
check("2022-24 also above Blim, below LRP", all(xt[y][1] >= 1.0 and xt[y][0] < 884.6 for y in (2022, 2023, 2024)))
blims = [xt[y][0] / xt[y][1] for y in sorted(xt) if xt[y][1] > 0]
check("implied Blim range 250-289, mean 275.5", abs(min(blims) - 250.0) < 0.5 and abs(max(blims) - 288.9) < 0.5
      and abs(sum(blims) / len(blims) - 275.5) < 0.5, f"({min(blims):.1f}-{max(blims):.1f}, mean {sum(blims)/len(blims):.1f})")
check("checkpoints 2005/2017/2024 = 26/451/342", (xt[2005][0], xt[2017][0], xt[2024][0]) == (26.0, 451.0, 342.0))
check("late-70s ratios 0.69-0.95", abs(min(xt[y][1] for y in (1977, 1978, 1979)) - 0.69) < 0.005
      and abs(max(xt[y][1] for y in (1977, 1978, 1979)) - 0.95) < 0.005)
check("xte outcome values", [xt[y][0] for y in range(2016, 2022)] == [339.0, 451.0, 369.0, 400.0, 414.0, 423.0])
missing = [y for y in range(1982, 2024) if y not in cap]
check("capelin missing years as declared", missing == [1983, 1984, 1993, 1994, 1995, 1997, 1998, 2006, 2016, 2020, 2021, 2022])
check("capelin 2023 = 331.3", cap.get(2023) == 331.3)
for needle in ["12{,}999", "18{,}000", "38{,}000", "1.2 \\(B_{\\mathrm{lim}}\\)", "95\\% CI 0.7--2.1", "540 kt",
               "condemned", "February 2023"]:
    check(f"text contains {needle!r}", needle in tex)
for needle in ["790.0", "884.6", "129.2", "133.3", "107.5", "16.8", "29 disagreement years", "45 years", "16 years",
               "55 consecutive years", "26 years", "94.6"]:
    check(f"text contains {needle!r}", needle in tex)

# ---------- (b) Edwards: archived result files against the printed tables ----------
print("--- (b) Edwards: Tables 7-9 and SI S17, S19, S20 against archived files ---")
EDW = "work/edw/results/"
roll = {(r["model"], int(r["horizon"])): r for r in rows(EDW + "rolling_summary.csv")}


def cell(model, h, key="rmse"):
    return float(roll[(model, h)][key])


table7 = {  # model: (h1 rmse, h1 mae, h5 rmse)
    "naive_persist": (13.23, 10.73, 21.11), "naive_mean": (16.17, 13.17, 16.80), "M1": (12.84, 10.72, 21.25),
    "M2": (14.70, 11.45, 33.49), "M2m": (12.28, 10.22, 17.44), "M3": (14.46, 11.12, 33.46), "M4": (14.30, 11.17, 33.39),
    "M2_oracle": (7.55, 5.79, 10.86)}
for m, (r1, a1, r5) in table7.items():
    check(f"Table 7 {m}: {r1}/{a1}/{r5}", abs(cell(m, 1) - r1) < 0.005 and abs(cell(m, 1, 'mae') - a1) < 0.005
          and abs(cell(m, 5) - r5) < 0.005, f"({cell(m,1):.2f}/{cell(m,1,'mae'):.2f}/{cell(m,5):.2f})")
check("Table 7 n = 75 / 71", int(roll[("M1", 1)]["n"]) == 75 and int(roll[("M1", 5)]["n"]) == 71)
check("Table 7 margins: M1-persist -0.39, M2m-persist -0.95, M2m-M1 -0.56, M2-persist +1.47, mean-persist +2.94",
      abs(cell("M1", 1) - cell("naive_persist", 1) + 0.39) < 0.006 and abs(cell("M2m", 1) - cell("naive_persist", 1) + 0.95) < 0.006
      and abs(cell("M2m", 1) - cell("M1", 1) + 0.56) < 0.006 and abs(cell("M2", 1) - cell("naive_persist", 1) - 1.47) < 0.006
      and abs(cell("naive_mean", 1) - cell("naive_persist", 1) - 2.94) < 0.006)
check("(E1)/(E2) at h=1: M1 < persist; M2m < persist and < M1; M2, M3, M4 > persist",
      cell("M1", 1) < cell("naive_persist", 1) and cell("M2m", 1) < min(cell("naive_persist", 1), cell("M1", 1))
      and all(cell(m, 1) > cell("naive_persist", 1) for m in ("M2", "M3", "M4")))
check("h=5: training mean beats persistence by 4.30; M1 does not beat persistence",
      abs(cell("naive_persist", 5) - cell("naive_mean", 5) - 4.31) < 0.02 and cell("M1", 5) > cell("naive_persist", 5))
h2 = {(r["model"], int(r["horizon"])): float(r["rmse"]) for r in rows(EDW + "pass2_H_summary.csv")}
r2 = {(r["model"], int(r["horizon"])): float(r["rmse"]) for r in rows(EDW + "pass2_R_summary.csv")}
table8 = {"M2_Rar": (13.25, 25.38, 561), "M2_enso": (12.82, 24.42, 528), "M2_precip": (12.80, 25.38, 545),
          "M2_combo": (12.71, 26.88, 538)}  # archived model ids; printed as M2_Renso / M2_Rprecip
for m, (x1, x5, rr) in table8.items():
    check(f"Table 9 {m}: head {x1}/{x5}, recharge {rr}", abs(h2[(m, 1)] - x1) < 0.006 and abs(h2[(m, 5)] - x5) < 0.006
          and abs(r2[(m, 1)] - rr) < 0.6, f"({h2[(m,1)]:.2f}/{h2[(m,5)]:.2f}, {r2[(m,1)]:.0f})")
check("Table 9 recharge baselines: climatology 556, persist 702, precipitation oracle 354",
      abs(r2[("R_mean", 1)] - 556) < 0.6 and abs(r2[("R_persist", 1)] - 702) < 0.6
      and abs(r2[("M2_precip_oracle", 1)] - 354) < 0.6)
check("precipitation oracle head RMSE 10.56", abs(h2[("M2_precip_oracle", 1)] - 10.56) < 0.006, f"({h2[('M2_precip_oracle',1)]:.2f})")
check("three climate modules beat M1 by 0.02-0.13 ft and lose to M2m; AR(1)-on-R rung loses to M1",
      all(0.015 < cell("M1", 1) - h2[(m, 1)] < 0.135 for m in ("M2_enso", "M2_precip", "M2_combo"))
      and all(h2[(m, 1)] > cell("M2m", 1) for m in table8) and h2[("M2_Rar", 1)] > cell("M1", 1))
unc = json.load(open(locate(EDW + "e3_audit_uncertainty.json")))
dm = {t["comparison"]: t for t in unc["dm_tests"]}
want = {"M1 vs naive_persist (h=1, n=75)": (-0.391, -0.852, 0.3967, -1.51, 0.71),
        "M2m vs naive_persist (h=1, n=75)": (-0.947, -3.07, 0.003, -1.45, -0.68),
        "M2m vs M1 (h=1, n=75)": (-0.556, -1.61, 0.11, -1.53, 0.13),
        "M2 vs naive_persist (h=1, n=75)": (1.468, 1.27, 0.21, -0.02, 3.40),
        "naive_mean vs naive_persist (h=5, n=71)": (-4.30, -1.65, 0.10, -9.72, -2.09),
        "M1 vs naive_persist (h=5, n=71)": (0.15, 0.06, 0.95, -5.57, 4.94)}
for k, (mg, z, p, lo, hi) in want.items():
    t = dm.get(k) or next((v for kk, v in dm.items() if kk.startswith(k.split(" (")[0])), None)
    ok = t is not None and abs(float(t["margin_rmse"]) - mg) < 0.006 and abs(float(t["dm_stat"]) - z) < 0.006 \
        and abs(float(t["dm_p_two_sided"]) - p) < 0.006 and abs(float(t["blockboot_margin_95ci"][0]) - lo) < 0.006 \
        and abs(float(t["blockboot_margin_95ci"][1]) - hi) < 0.006
    check(f"Table 8 (uncertainty) {k}", ok, "" if t is None else f"({t['margin_rmse']}, {t['dm_stat']}, {t['dm_p_two_sided']}, {t['blockboot_margin_95ci']})")
check("uncertainty layer: block 8, 10000 replicates, seed 20260905", unc["block"] == 8 and unc["nboot"] == 10000 and unc["seed"] == 20260905)
rec = unc["recovery_M2_trajectory"]
check("recovery M2 clip binds from 1959; RMSE 55.32; drawdown gamma +0.021",
      rec["clip_binds"] and rec["first_binding_year"] == 1959 and abs(rec["rmse_vs_observed"] - 55.32) < 0.006
      and abs(rec["drawdown_crosscheck"]["gamma"] - 0.021) < 0.0006)
fw = {(r["window"], r["model"]): float(r["rmse"]) for r in rows(EDW + "fixed_window_scores.csv")}
s17 = {"dor_drawdown": (23.75, 35.19, 30.94, 18.11, 27.44, 18.12, 18.23, 19.69),
       "dor_recovery": (43.62, 14.07, 56.24, 55.32, 37.74, 55.28, 55.12, 12.26),
       "prepermit_wet": (30.13, 18.24, 20.02, 16.67, 23.47, 16.41, 15.26, 7.18),
       "cpm_era": (27.41, 14.77, 15.62, 23.37, 14.79, 22.84, 22.17, 8.70)}
models = ("naive_persist", "naive_mean", "M1", "M2", "M2m", "M3", "M4", "M2_oracle")
for w, vals in s17.items():
    check(f"SI S17 {w}", all(abs(fw[(w, m)] - v) < 0.006 for m, v in zip(models, vals)),
          "(" + ", ".join(f"{fw[(w,m)]:.2f}" for m in models) + ")")
mod = {(r["model"], int(r["horizon"])): r for r in rows(EDW + "rolling_modern_2007.csv")}
check("SI S19 post-2007 Brier 0.31/0.25/0.25/0.19 (persist/M1/M2m/oracle), n=16",
      abs(float(mod[("naive_persist", 1)]["brier_660"]) - 0.3125) < 1e-6 and abs(float(mod[("M1", 1)]["brier_660"]) - 0.25) < 1e-6
      and abs(float(mod[("M2m", 1)]["brier_660"]) - 0.25) < 1e-6 and abs(float(mod[("M2_oracle", 1)]["brier_660"]) - 0.1875) < 1e-6
      and int(mod[("M1", 1)]["n"]) == 16)
check("SI S19 post-2007 h=1 RMSE 13.09/12.16/12.18/13.31/8.03; h=5 M1 17.16 < persist 25.10; mean 16.41",
      abs(float(mod[("naive_persist", 1)]["rmse"]) - 13.09) < 0.006 and abs(float(mod[("M1", 1)]["rmse"]) - 12.16) < 0.006
      and abs(float(mod[("M2m", 1)]["rmse"]) - 12.18) < 0.006 and abs(float(mod[("M2", 1)]["rmse"]) - 13.31) < 0.006
      and abs(float(mod[("M2_oracle", 1)]["rmse"]) - 8.03) < 0.006 and abs(float(mod[("M1", 5)]["rmse"]) - 17.16) < 0.006
      and abs(float(mod[("naive_persist", 5)]["rmse"]) - 25.10) < 0.006 and abs(float(mod[("naive_mean", 5)]["rmse"]) - 16.41) < 0.006)
com = {r["model"]: float(r["rmse"]) for r in rows(EDW + "fibre_comal_summary.csv")}
check("SI S20 Comal h=1 RMSE persist 71.9, M1 69.0, M2m 68.7, M2 74.8, M3 73.8, M4 73.4, mean 89.7, oracle 45.3",
      all(abs(com[m] - v) < 0.06 for m, v in {"naive_persist": 71.9, "M1": 69.0, "M2m": 68.7, "M2": 74.8, "M3": 73.8, "M4": 73.4,
                                                 "naive_mean": 89.7, "M2_oracle": 45.3}.items()))

# ---------- (c) horizon profile and autocorrelations (SI S23, Section 5) ----------
print("--- (c) horizon profiles and autocorrelations ---")
panel = [r for r in rows("work/edw/data/annual_panel.csv") if r["H_mean"] and 1934 <= int(r["year"]) <= 2023]
H = [float(r["H_mean"]) for r in panel]; R = [float(r["R_total"]) for r in panel]; P = [float(r["P_wells"]) for r in panel]
check("panel 1934-2023, 90 years", len(H) == 90 and int(panel[0]["year"]) == 1934)
yA = sorted(a2); SA = [a2[y] for y in yA]
SB_rows = sorted(xt); SB = [xt[y][0] for y in SB_rows]
pJ = profile(H, 14); pA = profile(SA, yA.index(1990)); pB = profile(SB, SB_rows.index(1965))
check("J-17 baselines h=1/h=5 reproduce Table 7: 13.23/21.11, 16.17/16.80",
      abs(pJ[1][1] - 13.23) < 0.006 and abs(pJ[5][1] - 21.11) < 0.006 and abs(pJ[1][2] - 16.17) < 0.006 and abs(pJ[5][2] - 16.80) < 0.006
      and pJ[1][0] == 75 and pJ[5][0] == 71, f"({pJ[1][1]:.2f}/{pJ[5][1]:.2f}, {pJ[1][2]:.2f}/{pJ[5][2]:.2f})")
check("cod A baselines h=1/h=5 reproduce Table 3: 98.0/264.7, 423.6/507.4 (n=25/21)",
      abs(pA[1][1] - 98.05) < 0.006 and abs(pA[5][1] - 264.72) < 0.006 and abs(pA[1][2] - 423.6) < 0.06 and abs(pA[5][2] - 507.4) < 0.06
      and pA[1][0] == 25 and pA[5][0] == 21, f"({pA[1][1]:.2f}/{pA[5][1]:.2f}, {pA[1][2]:.1f}/{pA[5][2]:.1f})")
check("cod B baselines h=1/h=5: 84.4/300.0, 458.1/521.6 (n=59/55)",
      abs(pB[1][1] - 84.43) < 0.006 and abs(pB[5][1] - 299.98) < 0.006 and abs(pB[1][2] - 458.1) < 0.06 and abs(pB[5][2] - 521.6) < 0.06
      and pB[1][0] == 59 and pB[5][0] == 55, f"({pB[1][1]:.2f}/{pB[5][1]:.2f}, {pB[1][2]:.1f}/{pB[5][2]:.1f})")
ratioJ = [pJ[h][1] / pJ[h][2] for h in range(1, 6)]
predJ = [math.sqrt(2 * (1 - ac(H, h))) for h in range(1, 6)]
check("J-17 ratio 0.82/1.07/1.22/1.27/1.26 vs stationary prediction 0.86/1.14/1.31/1.37/1.36",
      all(abs(a - b) < 0.006 for a, b in zip(ratioJ, (0.818, 1.067, 1.220, 1.270, 1.256)))
      and all(abs(a - b) < 0.006 for a, b in zip(predJ, (0.861, 1.142, 1.314, 1.371, 1.361))))
check("J-17 crossover at h=2 (ratio<1 at h=1, >1 from h=2); prediction within 0.11 at every horizon",
      ratioJ[0] < 1 < ratioJ[1] and all(abs(a - b) < 0.11 for a, b in zip(ratioJ, predJ)),
      "(" + ", ".join(f"{abs(a-b):.3f}" for a, b in zip(ratioJ, predJ)) + ")")
ratioA = [pA[h][1] / pA[h][2] for h in range(1, 6)]; ratioB = [pB[h][1] / pB[h][2] for h in range(1, 6)]
check("cod ratios stay in 0.18-0.58 at every horizon (no crossover)", 0.18 <= min(ratioA + ratioB) and max(ratioA + ratioB) <= 0.58,
      f"({min(ratioA+ratioB):.2f}-{max(ratioA+ratioB):.2f})")
check("AC_h(SSB) Spec. A 0.933/0.825/0.687/0.553/0.406",
      all(abs(ac(SA, h) - v) < 0.0006 for h, v in zip(range(1, 6), (0.933, 0.825, 0.687, 0.553, 0.406))))
check("H AC1 0.629, AC2 0.348, AC3 0.137, AC5 0.073", abs(ac(H, 1) - 0.629) < 0.0006 and abs(ac(H, 2) - 0.348) < 0.0006
      and abs(ac(H, 3) - 0.137) < 0.0006 and abs(ac(H, 5) - 0.073) < 0.0006)
check("R AC1 0.170; P AC1 0.870; r(R_t,R_{t-1}) 0.17; r(H_t,H_{t-1}) 0.64",
      abs(ac(R, 1) - 0.170) < 0.0006 and abs(ac(P, 1) - 0.870) < 0.0006 and abs(pearson(R[1:], R[:-1]) - 0.172) < 0.0006
      and abs(pearson(H[1:], H[:-1]) - 0.644) < 0.0006)
dH = [H[i + 1] - H[i] for i in range(len(H) - 1)]
check("r(dH_t,R_t)=0.742, r(dH_t,R_{t-1})=0.056", abs(pearson(dH, R[1:]) - 0.742) < 0.0006 and abs(pearson(dH, R[:-1]) - 0.056) < 0.0006)
# full-sample one-pool fit by normal equations (4 x 4)
X = [[1.0, R[i + 1], P[i + 1], H[i]] for i in range(len(dH))]
XtX = [[sum(X[k][i] * X[k][j] for k in range(len(X))) for j in range(4)] for i in range(4)]
Xty = [sum(X[k][i] * dH[k] for k in range(len(X))) for i in range(4)]
M = [row[:] + [Xty[i]] for i, row in enumerate(XtX)]
for c in range(4):
    piv = max(range(c, 4), key=lambda r_: abs(M[r_][c])); M[c], M[piv] = M[piv], M[c]
    for r_ in range(4):
        if r_ != c:
            f = M[r_][c] / M[c][c]; M[r_] = [M[r_][j] - f * M[c][j] for j in range(5)]
coef = [M[i][4] / M[i][i] for i in range(4)]
check("full-sample fit (alpha,beta,gamma,delta) = (177.6, 0.0173, -0.0260, -0.273)",
      abs(coef[0] - 177.6) < 0.06 and abs(coef[1] - 0.0173) < 0.00006 and abs(coef[2] + 0.0260) < 0.00006 and abs(coef[3] + 0.273) < 0.0006,
      f"({coef[0]:.1f}, {coef[1]:.4f}, {coef[2]:.4f}, {coef[3]:.3f})")
mech = [coef[1] * R[i] + coef[2] * P[i] for i in range(len(R))]
mu = sum(mech) / len(mech); var = sum((v - mu) ** 2 for v in mech) / len(mech); rho = ac(mech, 1)
check("flux mechanism: sd 9.20, AC1 0.078, mean 3.52", abs(math.sqrt(var) - 9.20) < 0.006 and abs(rho - 0.078) < 0.0006 and abs(mu - 3.52) < 0.006)
# apparent net production autocorrelations (cod)
def coarse(y):
    return 240.0 if y <= 1991 else (120.0 if y == 1992 else 5.0)
landA = {int(r["year"]): float(r["catch_kt"]) for r in rows(COD + "catch_schijns_2021.csv")}
landB = {int(r["year"]): float(r["catch_kt"]) for r in rows(COD + "dfo_2025_table1_landings.csv")}
PA = [SA[i + 1] - SA[i] + coarse(yA[i]) for i in range(len(SA) - 1)]
PA2 = [SA[i + 1] - SA[i] + landA[yA[i]] for i in range(len(SA) - 1)]
PB = [SB[i + 1] - SB[i] + landB.get(SB_rows[i], landB[max(landB)]) for i in range(len(SB) - 1)]
check("apparent net production AC1: 0.753 (A coarse), 0.714 (A annual), 0.908 (B)",
      abs(ac(PA, 1) - 0.753) < 0.0006 and abs(ac(PA2, 1) - 0.714) < 0.0006 and abs(ac(PB, 1) - 0.908) < 0.0006,
      f"({ac(PA,1):.3f}, {ac(PA2,1):.3f}, {ac(PB,1):.3f})")
check("none of the cod production series is weakly autocorrelated (all AC1 > 0.7)", min(ac(PA, 1), ac(PA2, 1), ac(PB, 1)) > 0.7)

# ---------- (d) exact rolling-origin increment identity on J-17 ----------
print("--- (d) exact rolling-origin J-17 increment identity ---")
inc = rows("work/edw/results/increment_identity_rolling.csv")
inc_summary = json.load(open(locate("work/edw/results/increment_identity_rolling.json"), encoding="utf-8"))
inc_origins = [int(r["origin"]) for r in inc]
sub_terms = [float(r["substitution_term_ft2"]) for r in inc]
cross_terms = [float(r["residual_cross_term_ft2"]) for r in inc]
raw_terms = [float(r["raw_mse_gap_contribution_ft2"]) for r in inc]
identity_errors = [float(r["identity_abs_error_ft2"]) for r in inc]
# Independently reconstruct both sides from CSV components (serialized to 12 significant digits).
lhs = []
for r in inc:
    delta = float(r["delta_head_ft"])
    m = float(r["mechanism_realized_flux_ft"])
    mhat = float(r["mechanism_persisted_flux_ft"])
    u = float(r["mechanism_residual_ft"])
    d = m - mhat
    lhs.append((delta - mhat) ** 2 - delta ** 2)
    check(f"identity origin {r['origin']}", abs(lhs[-1] - ((d * d - m * m) - 2 * u * mhat)) < 1e-7)
check("75 contiguous origins 1948-2022, targets origin+1",
      len(inc) == 75 and inc_origins == list(range(1948, 2023))
      and all(int(r["target"]) == int(r["origin"]) + 1 for r in inc))
check("per-origin identity residual below 1e-9 ft^2",
      max(identity_errors) < 1e-9 and max(abs(x - y) for x, y in zip(lhs, raw_terms)) < 1e-7,
      f"(max archived {max(identity_errors):.3g}; reconstructed {max(abs(x-y) for x,y in zip(lhs,raw_terms)):.3g})")
sub_mean = sum(sub_terms) / len(sub_terms)
cross_mean = sum(cross_terms) / len(cross_terms)
raw_mean = sum(raw_terms) / len(raw_terms)
check("rolling substitution term = +76.028642 ft^2", abs(sub_mean - 76.02864216915157) < 1e-8,
      f"({sub_mean:.6f})")
check("rolling residual cross-term = -27.490666 ft^2", abs(cross_mean + 27.49066627629379) < 1e-8,
      f"({cross_mean:.6f})")
check("raw MSE gap = +48.537976 ft^2 and equals sum of both terms",
      abs(raw_mean - 48.53797589285777) < 1e-8 and abs(raw_mean - sub_mean - cross_mean) < 1e-9
      and abs(sum(lhs) / len(lhs) - raw_mean) < 1e-9,
      f"({raw_mean:.6f})")
check("summary JSON records all four forecast/identity checks true",
      inc_summary["checks"] == {"clipped_m2_matches_archived_forecasts": True,
                                 "identity_holds_at_every_origin": True,
                                 "origin_count_is_75": True,
                                 "persistence_matches_archived_forecasts": True})
# Check the emitted (clipped) forecasts directly against the archived forecast file.
archived_h1 = {(int(r["origin"]), r["model"]): float(r["pred"])
               for r in rows(EDW + "rolling_forecasts.csv") if int(r["horizon"]) == 1}
check("all 75 clipped M2 and persistence forecasts match archived outputs within 1e-9",
      all(abs(float(r["clipped_prediction_ft"]) - archived_h1[(int(r["origin"]), "M2")]) < 1e-9
          and abs(float(r["persistence_prediction_ft"]) - archived_h1[(int(r["origin"]), "naive_persist")]) < 1e-9 for r in inc))
upper = [r for r in inc if abs(float(r["raw_prediction_ft"]) - float(r["clipped_prediction_ft"])) > 1e-9
         and float(r["raw_prediction_ft"]) > float(r["clipped_prediction_ft"])]
check("only upper clip is origin 1992: raw 719.1027 ft to 710 ft; no lower clip",
      [int(r["origin"]) for r in upper] == [1992] and not inc_summary["lower_clip_origins"]
      and inc_summary["upper_clip_origins"] == [1992]
      and abs(float(upper[0]["raw_prediction_ft"]) - 719.1027) < 0.0001
      and abs(float(upper[0]["clipped_prediction_ft"]) - 710.0) < 1e-9)
clipped_gap = sum(float(r["sqerr"]) for r in rows(EDW + "rolling_forecasts.csv")
                  if int(r["horizon"]) == 1 and r["model"] == "M2") / 75 \
              - sum(float(r["sqerr"]) for r in rows(EDW + "rolling_forecasts.csv")
                    if int(r["horizon"]) == 1 and r["model"] == "naive_persist") / 75
check("archived clipped MSE gap = +40.988957 ft^2 (RMSE 14.70 vs 13.23)",
      abs(clipped_gap - 40.988957391127094) < 1e-8
      and abs(math.sqrt(inc_summary["clipped_m2_mse_ft2"]) - 14.697759248814572) < 1e-9
      and abs(math.sqrt(inc_summary["persistence_mse_ft2"]) - 13.230085772397212) < 1e-9,
      f"({clipped_gap:.6f})")

# ---------- (e) deterministic cod operating-characteristic archive ----------
print("--- (e) deterministic cod simulation: manifest, hashes, seeds and coverage ---")
POWER = "work/cod/"
power_manifest_path = locate(POWER + "power_simulation_repro_manifest.json")
power_root = os.path.dirname(power_manifest_path)
power_manifest = json.load(open(power_manifest_path, encoding="utf-8"))

def file_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

cells = ["D1_M1_collapse", "D2_M1_recovery", "D3_M2_stockflow", "D4_M1b_depens",
         "D5_persist_null", "D6_timevarying_r", "D7_obs_error"]
sigmas = (11.8, 33.8)
modules = ["M1_autonomous_Schaefer", "M1b_autonomous_Allee", "M2_stockflow_regimeC",
           "M3_AR_residual", "M4_delayed_info"]
check("full v68 run covers exactly replicate IDs 0--199 with no failed cells",
      power_manifest.get("edition") == "Paper11 v68" and power_manifest.get("rep_start") == 0
      and power_manifest.get("rep_end_exclusive") == 200 and power_manifest.get("reps_per_cell") == 200
      and power_manifest.get("cells") == 14 and power_manifest.get("rows") == 14000
      and power_manifest.get("failed_replicates") == 0)
batch_records = power_manifest.get("batches", [])
batch_intervals = sorted((int(b.get("rep_start", -1)), int(b.get("rep_end_exclusive", -1))) for b in batch_records)
check("combined manifest records four contiguous batches",
      batch_intervals == [(0, 50), (50, 100), (100, 150), (150, 200)])
batch_archive_ok = len(batch_records) == 4
required_batch_outputs = {"power_simulation_repro.csv", "power_simulation_repro_summary.csv",
                          "power_simulation_repro_decomposition.csv", "power_simulation_repro_chance.csv"}
for record in batch_records:
    batch_dir = os.path.join(power_root, "power_batches", record.get("directory", ""))
    batch_manifest_path = os.path.join(batch_dir, "power_simulation_repro_manifest.json")
    batch_csv_path = os.path.join(batch_dir, "power_simulation_repro.csv")
    if not os.path.isfile(batch_manifest_path) or not os.path.isfile(batch_csv_path):
        batch_archive_ok = False
        continue
    batch_manifest = json.load(open(batch_manifest_path, encoding="utf-8"))
    start, end = int(record.get("rep_start", -1)), int(record.get("rep_end_exclusive", -1))
    batch_archive_ok &= file_sha256(batch_manifest_path) == record.get("manifest_sha256")
    batch_archive_ok &= file_sha256(batch_csv_path) == record.get("raw_sha256")
    batch_archive_ok &= record.get("rows") == 14 * (end - start) * 5
    batch_archive_ok &= batch_manifest.get("rep_start") == start and batch_manifest.get("rep_end_exclusive") == end
    batch_archive_ok &= batch_manifest.get("rows") == record.get("rows") and batch_manifest.get("failed_replicates") == 0
    batch_outputs = batch_manifest.get("outputs", {})
    batch_archive_ok &= set(batch_outputs) == required_batch_outputs
    for name, digest in batch_outputs.items():
        path = os.path.join(batch_dir, name)
        batch_archive_ok &= os.path.isfile(path) and file_sha256(path) == digest
check("all four archived batch manifests, ranges, counts and output hashes match the combined manifest", batch_archive_ok)
for rel, expected_hash in power_manifest.get("outputs", {}).items():
    out_path = os.path.join(power_root, rel)
    check(f"simulation output hash: {rel}", os.path.isfile(out_path) and file_sha256(out_path) == expected_hash)
sim_path = locate(POWER + "sim_retention_power_repro.py")
runner_path = locate(POWER + "rerun/src/run_ladder.py")
aggregator_path = locate(POWER + "aggregate_power_simulation_repro.py")
check("manifest pins simulator, registered scorer and aggregator sources",
      power_manifest.get("simulator_sha256") == file_sha256(sim_path)
      and power_manifest.get("run_ladder_sha256") == file_sha256(runner_path)
      and power_manifest.get("aggregation_script_sha256") == file_sha256(aggregator_path))
raw_power = rows(POWER + "power_simulation_repro.csv")
expected_power_keys = {(c, float(s), r, m) for c in cells for s in sigmas for r in range(200) for m in modules}
actual_power_keys = [(r["cell"], float(r["sigma"]), int(r["rep"]), r["module"]) for r in raw_power]
check("raw simulation has 14,000 unique cell/noise/replicate/module rows",
      len(raw_power) == 14000 and len(set(actual_power_keys)) == 14000 and set(actual_power_keys) == expected_power_keys)
truth_by_cell = {"D1_M1_collapse": "M1_autonomous_Schaefer", "D2_M1_recovery": "M1_autonomous_Schaefer",
                 "D3_M2_stockflow": "M2_stockflow_regimeC", "D4_M1b_depens": "M1b_autonomous_Allee",
                 "D5_persist_null": "", "D6_timevarying_r": "", "D7_obs_error": ""}
seed_namespace = power_manifest.get("seed_namespace", "")
seed_ok = True
by_cell_rep = {}
for row in raw_power:
    cell, sigma, rep = row["cell"], float(row["sigma"]), int(row["rep"])
    expected_seed = int.from_bytes(hashlib.sha256(f"{seed_namespace}|{cell}|{sigma:.1f}|{rep}".encode("utf-8")).digest()[:8], "big")
    if int(row["seed"]) != expected_seed or not all(math.isfinite(float(row[k])) for k in ("rmse_h1", "rmse_h5", "persist_h1", "persist_h5")):
        seed_ok = False
    by_cell_rep.setdefault((cell, sigma, rep), {})[row["module"]] = row
check("every raw row has its stable SHA-256 seed and finite scores", seed_ok)
comparators = {"M1_autonomous_Schaefer": None, "M1b_autonomous_Allee": "M1_autonomous_Schaefer",
               "M2_stockflow_regimeC": "M1_autonomous_Schaefer", "M3_AR_residual": "M2_stockflow_regimeC",
               "M4_delayed_info": "M3_AR_residual"}
rule_ok = True
for repscores in by_cell_rep.values():
    for module in modules:
        row = repscores.get(module)
        if row is None:
            rule_ok = False
            continue
        expected_retained = all(float(row[f"rmse_h{h}"]) < float(row[f"persist_h{h}"]) * 0.95 for h in (1, 5))
        comp = comparators[module]
        if comp is not None:
            comparator_row = repscores.get(comp)
            expected_retained = expected_retained and comparator_row is not None and all(
                float(row[f"rmse_h{h}"]) < float(comparator_row[f"rmse_h{h}"]) * 0.95 for h in (1, 5))
        expected_actual = row["retained"].strip().lower() in ("true", "1")
        if expected_retained != expected_actual:
            rule_ok = False
check("all 14,000 retention flags implement the two-horizon 5% rule and declared comparators", rule_ok)
summary_rows = rows(POWER + "power_simulation_repro_summary.csv")
summary_map = {(r["cell"], float(r["sigma"])): r for r in summary_rows}
summary_ok = len(summary_map) == 14
for cell in cells:
    for sigma in sigmas:
        group = [by_cell_rep.get((cell, sigma, rep), {}) for rep in range(200)]
        if any(set(g) != set(modules) for g in group):
            summary_ok = False
            continue
        any_rate = sum(any(g[m]["retained"].strip().lower() in ("true", "1") for m in modules) for g in group) / 200
        sr = summary_map.get((cell, sigma))
        if sr is None or int(sr["n_reps"]) != 200:
            summary_ok = False
            continue
        if abs(float(sr["any_module_retention_rate"]) - any_rate) > 1e-8:
            summary_ok = False
        truth = truth_by_cell[cell]
        if truth:
            true_rate = sum(g[truth]["retained"].strip().lower() in ("true", "1") for g in group) / 200
            if abs(float(sr["true_module_rate"]) - true_rate) > 1e-8:
                summary_ok = False
check("14 summary cells match raw replicate-level retention rates (n=200 each)", summary_ok)

# Printed SI cell rates, Monte Carlo intervals, decomposition and chance table.
si_rate_table_ok = True
for cell in cells:
    for sigma in sigmas:
        sr = summary_map[(cell, sigma)]
        if cell in cells[:4]:
            count = int(sr["true_module_retained_n"])
            rate = float(sr["true_module_rate"])
            low, high = float(sr["true_module_wilson95_low"]), float(sr["true_module_wilson95_high"])
        else:
            count = int(sr["any_module_retained_n"])
            rate = float(sr["any_module_retention_rate"])
            low, high = float(sr["any_module_wilson95_low"]), float(sr["any_module_wilson95_high"])
        needle = f"{count}/200; {rate:.3f} [{low:.3f}, {high:.3f}]"
        if needle not in tex_si:
            si_rate_table_ok = False
check("SI cell table reproduces all 14 rates and Wilson intervals from the final summary", si_rate_table_ok)
check("SI reports Wilson intervals for D3/D4 any-module retention as well as true-module power",
      "105/200 and 122/200 series (95\\% Wilson intervals [0.456, 0.593] and [0.541, 0.675])" in tex_si
      and "61/200 and 11/200 ([0.245, 0.372] and [0.031, 0.096])" in tex_si)

decomp_rows = rows(POWER + "power_simulation_repro_decomposition.csv")
decomp_ok = True
truth_label = {"D1_M1_collapse": "M1", "D2_M1_recovery": "M1",
               "D3_M2_stockflow": "M2", "D4_M1b_depens": "M1b"}
for cell in cells[:4]:
    subset = [r for r in decomp_rows if r["cell"] == cell]
    n = sum(int(r["n_reps"]) for r in subset)
    h2_n = sum(int(r["h2_alone_n"]) for r in subset)
    full_n = sum(int(r["full_rule_n"]) for r in subset)
    removed_n = h2_n - full_n
    h2_rate, full_rate, removed_rate = h2_n / n, full_n / n, removed_n / n
    conditional = 100 * removed_n / h2_n if h2_n else 0.0
    needle = (f"{cell[:2]} & {truth_label[cell]} & {h2_rate:.4f} & {full_rate:.4f} & "
              f"{removed_rate:.4f} & {conditional:.0f}\\%")
    if needle not in tex_si:
        decomp_ok = False
check("SI persistence/comparator decomposition table matches the four-batch archive", decomp_ok)

chance_rows = rows(POWER + "power_simulation_repro_chance.csv")
chance_status = {"D1_M1_collapse": "far above 0.20", "D2_M1_recovery": "far above 0.20",
                 "D3_M2_stockflow": "below 0.20", "D4_M1b_depens": "slightly above 0.20"}
chance_labels = {"D1_M1_collapse": "D1 (M1 true)", "D2_M1_recovery": "D2 (M1 true)",
                 "D3_M2_stockflow": "D3 (M2 true)", "D4_M1b_depens": "D4 (M1b true)"}
chance_ok = True
for cell in cells[:4]:
    subset = [r for r in chance_rows if r["cell"] == cell]
    n = sum(int(r["n_reps"]) for r in subset)
    ranks = sum(int(r["truth_lowest_h1_n"]) for r in subset)
    needle = f"{chance_labels[cell]} & {ranks/n:.3f} & {chance_status[cell]}"
    if needle not in tex_si:
        chance_ok = False
check("SI chance table matches pooled replicate-level rank counts", chance_ok)

full_protocol_power = sum(int(r["full_rule_n"]) for r in decomp_rows) / sum(int(r["n_reps"]) for r in decomp_rows)
d5_rows = [r for r in summary_rows if r["cell"] == "D5_persist_null"]
d5_n = sum(int(r["n_reps"]) for r in d5_rows)
d5_false_n = sum(int(r["any_module_retained_n"]) for r in d5_rows)
protocol_baseline = (f"Protocol C as adopted (C1--C3, 5\\% band) & {full_protocol_power:.3f} & "
                     f"{1-d5_false_n/d5_n:.3f}")
check("SI rule-comparison table refreshes the Protocol C baseline from v68 and marks alternatives historical",
      protocol_baseline in tex_si and "other rules are carried forward" in tex_si)

# ---------- (f) textual invariants ----------
print("--- (f) textual invariants ---")
fig6_source = open(locate(POWER + "plot_operating_characteristics.py"), encoding="utf-8").read()
figures_source = open(locate(POWER + "make_figures.py"), encoding="utf-8").read()
check("Fig. 6 reads the aggregate summary and uses separate power/false-retention metrics",
      "power_simulation_repro_summary.csv" in figures_source and "true_module_rate" in fig6_source
      and "any_module_retention_rate" in fig6_source and "expected_reps=200" in figures_source
      and "vals = np.array([[0.965" not in figures_source)
check("separate main/SI PDFs use explicit cross-document table and proposition references",
      "SI Table~S16" in tex_main and "\\ref{tab:si_power}" not in tex_main
      and "main-text Proposition~2" in tex_si and "\\ref{prop:increment}" not in tex_si)
check("no claim of prospective registration",  
      flat.replace("the phrase ``pre-registered'' is avoided", "").count("pre-registered") == 0 and "preregistered" not in flat
      and "registered report" not in flat.lower())
check("dated computational protocol, not prospective registration", "dated computational protocol" in flat and "not a prospective registration" in flat)
check("simulation design and amendment identifiers retained", "d5d9758" in flat and "bd0008f" in flat)
check("score-rule labels retained in the protocol record", "(H1)" in flat and "(H2)" in flat and "(E1)" in flat and "(E2)" in flat)
check("M2m H1/H2 point pass stated separately from function-class exclusion",
      "M2m passes Pass~1 H1/H2" in flat and "additional function classes" in flat and "class-demoted" in flat)
check("Pass 2 point-gate passes separated from empty structure-class set",
      "three point-gate passes" in flat and "retained\\_as\\_structure" in flat and "score-gate failure" in flat)
check("rolling J-17 substitution and residual cross-terms both reported",
      "+76.03" in flat and "-27.49" in flat and "+48.54" in flat and "+40.99" in flat)
check("withdrawn 'weakly autocorrelated' reading accompanied by computed values 0.71-0.75 and 0.91",
      "weakly autocorrelated" in flat and "withdrawn" in flat and "0.71" in flat and "0.91" in flat)
check("Abaee self-citations use lettered authoryear forms consistently",
      "Abaee(2026a)" in flat.replace(" ", "") and "Abaee(2026b)" in flat.replace(" ", ""))
for needle in ["13.23", "12.84", "12.28", "14.70", "16.80", "0.39", "0.95", "7.55", "0.74", "0.17", "0.87",
               "17.1", "2.96"]:
    check(f"main text contains {needle!r}", needle in tex_main)
operating_rates = ["97.5\\%", "95.0\\%", "66.0\\%", "11.0\\%", "10.5\\%", "13.0\\%",
                   "52.5\\%", "61.0\\%", "30.5\\%", "5.5\\%", "2.5\\%", "7.5\\%",
                   "72.0\\%", "77.0\\%", "97.0\\%"]
check("main operating-characteristic narrative reports the full-run rates", all(x in tex_main for x in operating_rates))
check("stale primary v67 power ranges removed from main text",
      not any(x in tex_main for x in ("96.5\\%", "98.5\\%", "9--11\\%", "1.5--3.0\\%", "97--99\\%")))
_abs = tex_main[tex_main.index("\\begin{abstract}"):tex_main.index("\\end{abstract}")]
_body = tex_main[tex_main.index("\\end{abstract}"):]
for _c in sorted(set(re.findall(r"(?<![\d.])\d+(?:\.\d+)?(?![\d.])", _abs)), key=float):
    if _c in ("1983", "2015", "1954", "2024", "1934", "2023", "1991", "1995", "1948", "1965", "1990", "17"):
        continue
    check(f"abstract constant {_c} restated in body", _c in _body)

print(f"\nverification: {PASS}/{PASS + FAIL} checks pass")
sys.exit(1 if FAIL else 0)
