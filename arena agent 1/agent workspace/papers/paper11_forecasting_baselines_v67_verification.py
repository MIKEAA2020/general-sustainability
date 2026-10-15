"""Verification for paper11_forecasting_baselines v67 (two-system edition).

Reads the registered data files and the archived result files of both
systems together with the manuscript sources (main text + Supplementary
Information, read together) and asserts, in order:
  (a) the cod outcome-year, vintage and threshold cross-checks carried over
      from the single-system edition (SI S10-S12), including the presence
      of the pinned values in the sources;
  (b) every cell of main-text Tables 7-9 and of SI S17, S19, S20 against the
      archived Edwards result files;
  (c) the baseline horizon profile of SI S23 recomputed from the registered
      series, its agreement with the archived h=1 and h=5 summaries of both
      systems, and the autocorrelations quoted in Section 5;
  (d) the arithmetic of Proposition 2 on the J-17 numbers;
  (e) textual invariants.
Standard library only.  Run: python3 paper11_forecasting_baselines_v67_verification.py
Layout: the script looks for  work/  next to itself or inside
paper11_forecasting_baselines_v67_src/ (the repository layout).
"""
import csv, json, math, os, re, sys

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
    for base in (HERE, os.path.join(HERE, "paper11_forecasting_baselines_v67_src")):
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
tex_main = open(os.path.join(HERE, "paper11_forecasting_baselines_v67.tex"), encoding="utf-8").read()
tex_si = open(os.path.join(HERE, "paper11_forecasting_baselines_v67_supplementary.tex"), encoding="utf-8").read()
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

# ---------- (d) Proposition 2 arithmetic on J-17 ----------
print("--- (d) Proposition 2 arithmetic ---")
term = var * (1 - 2 * rho) - mu ** 2
check("sigma^2(1-2rho) - mu^2 > 0 (persisted near-white driver predicted to lose)", term > 0, f"({term:.1f} ft^2)")
check("mu^2/(2 sigma^2) < rho threshold: rho=0.078 < 0.5 - mu^2/(2 sigma^2)", rho < 0.5 - mu ** 2 / (2 * var))
pred_M2 = math.sqrt(cell("naive_persist", 1) ** 2 + var * (1 - 2 * rho))
check("stylised M2 RMSE 15.70 ft (archived 14.70): over-predicts the loss, same sign",
      abs(pred_M2 - 15.70) < 0.006 and pred_M2 > cell("naive_persist", 1) and cell("M2", 1) > cell("naive_persist", 1), f"({pred_M2:.2f})")
gap_obs = cell("M2", 1) ** 2 - cell("M2m", 1) ** 2
check("predicted M2m-over-M2 advantage 71.4 ft^2 within 10% of archived 65.1 ft^2", abs(var * (1 - 2 * rho) - gap_obs) / gap_obs < 0.10,
      f"({var*(1-2*rho):.1f} vs {gap_obs:.1f})")
check("ordering M2m <= persist < M2 at h=1", cell("M2m", 1) <= cell("naive_persist", 1) < cell("M2", 1))

# ---------- (e) textual invariants ----------
print("--- (e) textual invariants ---")
check("no claim of prospective registration",
      flat.replace("the phrase ``pre-registered'' is avoided", "").count("pre-registered") == 0 and "preregistered" not in flat
      and "registered report" not in flat.lower())
check("protocol described as fixed computational protocol", "fixed computational protocol" in flat)
check("simulation pre-specification hashes present", "d5d9758" in flat and "bd0008f" in flat)
check("both protocols named with their hurdles", "(H1)" in flat and "(H2)" in flat and "(E1)" in flat and "(E2)" in flat)
check("M2m class clause disclosed as a deviation", "class clause" in flat and "deviation" in flat)
check("withdrawn 'weakly autocorrelated' reading accompanied by computed values 0.71-0.75 and 0.91",
      "weakly autocorrelated" in flat and "withdrawn" in flat and "0.71" in flat and "0.91" in flat)
check("Abaee self-citations use lettered authoryear forms consistently",
      "Abaee(2026a)" in flat.replace(" ", "") and "Abaee(2026b)" in flat.replace(" ", ""))
for needle in ["13.23", "12.84", "12.28", "14.70", "16.80", "0.39", "0.95", "7.55", "0.74", "0.17", "0.87", "97", "9--11",
               "17.1", "2.96"]:
    check(f"main text contains {needle!r}", needle in tex_main)
_abs = tex_main[tex_main.index("\\begin{abstract}"):tex_main.index("\\end{abstract}")]
_body = tex_main[tex_main.index("\\end{abstract}"):]
for _c in sorted(set(re.findall(r"(?<![\d.])\d+(?:\.\d+)?(?![\d.])", _abs)), key=float):
    if _c in ("1983", "2015", "1954", "2024", "1934", "2023", "1991", "1995", "1948", "1965", "1990", "17"):
        continue
    check(f"abstract constant {_c} restated in body", _c in _body)

print(f"\nverification: {PASS}/{PASS + FAIL} checks pass")
sys.exit(1 if FAIL else 0)
