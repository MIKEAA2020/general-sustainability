"""Verification for paperE1_cod_forecast_ladder v50, Sections 3.8-3.10.

Regenerates every number in the outcome-year, threshold
definition-dependence, and suspension sections from the archived data
files (in-repo, locked provenance) and asserts the cross-checks.
Standard library only. Run: python3 paperE1_cod_forecast_ladder_v56_verification.py
"""
import csv, math, os, sys

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

def rows(path):
    with open(os.path.join(HERE, path), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

# ---------- data ----------
a2 = {int(r["year"]): float(r["ssb_kt"]) for r in rows("paperE1_calibration_data_v1_wave_e_cod/ncam_2016_table_a2.csv")}
ram = {int(r["year"]): float(r["SSB"]) / 1000.0 for r in rows("paperE1_calibration_data_v1_ram_timeseries.csv") if r["SSB"]}
xt = {int(r["year"]): (float(r["ssb_kt"]), float(r["ssb_over_blim"])) for r in rows("paperE1_calibration_data_v1_wave_e_cod/xtencam_table17_ssb.csv")}
cap = {int(r["year"]): float(r["acoustic_kt"]) for r in rows("paperE1_calibration_data_v1_wave_e_cod/capelin_acoustic_observed.csv")}
tex = open(os.path.join(HERE, "paperE1_cod_forecast_ladder_v57.tex"), encoding="utf-8").read()

for _needle in ("Northern Cod Assessment Model", "limit reference point"):
    check(_needle in " ".join(tex.split()), f"v6 needle: {_needle!r}")

# ---------- E1: Specification A base series integrity ----------
lrp = sum(a2[y] for y in range(1983, 1990)) / 7
check("A2 33 years 1983-2015", sorted(a2) == list(range(1983, 2016)))
check("LRP 1983-89 mean = 884.58", abs(lrp - 884.58) < 0.005, f"({lrp:.2f})")
check("2015 SSB 298.65 = 33.8% LRP", abs(a2[2015] - 298.65) < 1e-9 and abs(a2[2015] / lrp - 0.3376) < 5e-4)

# ---------- E2: outcome years ----------
out = {y: ram[y] for y in range(2016, 2022)}
check("RAM outcome values", out == {2016: 340.0, 2017: 433.0, 2018: 394.0, 2019: 419.0, 2020: 440.0, 2021: 411.0})
errs = [abs(ram[y] - ram[2015]) for y in range(2016, 2022)]
check("RAM 2015 origin = 277", ram[2015] == 277.0)
check("persistence MAE = 129.2", abs(sum(errs) / 6 - 129.17) < 0.005, f"({sum(errs)/6:.2f})")
check("persistence RMSE = 133.3", abs(math.sqrt(sum(e * e for e in errs) / 6) - 133.34) < 0.005,
      f"({math.sqrt(sum(e*e for e in errs)/6):.2f})")
errs_a2 = [abs(ram[y] - a2[2015]) for y in range(2016, 2022)]
check("A2-origin MAE = 107.5", abs(sum(errs_a2) / 6 - 107.52) < 0.005, f"({sum(errs_a2)/6:.2f})")
check("increase regime (all years above origin)", all(ram[y] > ram[2015] for y in range(2016, 2022)))
conc = [abs(ram[y] - xt[y][0]) for y in range(2016, 2022)]
check("vintage concordance: max 26, mean 16.8", max(conc) == 26.0 and abs(sum(conc) / 6 - 16.83) < 0.005,
      f"(max {max(conc):.0f}, mean {sum(conc)/6:.2f})")

# ---------- E3: vintage overlap 1983-2015 ----------
d = {y: a2[y] - ram[y] for y in range(1983, 2016)}
mad = sum(abs(v) for v in d.values()) / 33
check("A2-RAM mean signed +24.7", abs(sum(d.values()) / 33 - 24.7) < 0.05, f"({sum(d.values())/33:.1f})")
check("A2-RAM mean abs 26.8", abs(mad - 26.8) < 0.05, f"({mad:.1f})")
ymax = max(d, key=lambda k: abs(d[k]))
check("A2-RAM max abs 131.2 @1984", ymax == 1984 and abs(abs(d[ymax]) - 131.2) < 0.05, f"({abs(d[ymax]):.1f})")

# ---------- E4: vintage-shifted LRP ----------
lrp_ram = sum(ram[y] for y in range(1983, 1990)) / 7
check("RAM-vintage LRP = 790.00", abs(lrp_ram - 790.0) < 0.005, f"({lrp_ram:.2f})")
check("LRP shift = 94.6 kt", abs((lrp - lrp_ram) - 94.58) < 0.01, f"({lrp - lrp_ram:.2f})")

# ---------- E5: threshold classification on xteNCAM file ----------
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
blims = [xt[y][0] / xt[y][1] for y in sorted(xt)]
check("implied Blim range 250-289, mean 275.5", abs(min(blims) - 250.0) < 0.5 and abs(max(blims) - 288.9) < 0.5
      and abs(sum(blims) / len(blims) - 275.5) < 0.1, f"([{min(blims):.0f},{max(blims):.0f}] {sum(blims)/len(blims):.1f})")
check("checkpoints 2005/2017/2024 = 26/451/342", (xt[2005][0], xt[2017][0], xt[2024][0]) == (26.0, 451.0, 342.0))
check("late-70s ratios 0.69-0.95", abs(min(xt[y][1] for y in (1977, 1978, 1979)) - 0.69) < 0.005
      and abs(max(xt[y][1] for y in (1977, 1978, 1979)) - 0.95) < 0.005)
check("xte outcome values", [xt[y][0] for y in range(2016, 2022)] == [339.0, 451.0, 369.0, 400.0, 414.0, 423.0])

# ---------- E6: capelin observed-years structure ----------
missing = [y for y in range(1982, 2024) if y not in cap]
check("capelin missing years as declared", missing == [1983, 1984, 1993, 1994, 1995, 1997, 1998, 2006, 2016, 2020, 2021, 2022])
check("capelin 2023 = 331.3", cap.get(2023) == 331.3)

# ---------- E7: suspension facts pinned in the text ----------
for needle in ["12{,}999", "18{,}000", "38{,}000", "1.2 \\(B_{\\mathrm{lim}}\\)",
               "95\\% CI 0.7--2.1", "540 kt", "condemned", "February 2023"]:
    check(f"text contains {needle!r}", needle in tex)

# ---------- E8: section numbers present in text ----------
for needle in ["790.0", "884.6", "129.2", "133.3", "107.5", "16.8", "29 disagreement years",
               "45 years", "16 years", "55 consecutive years", "26 years", "94.6"]:
    check(f"text contains {needle!r}", needle in tex)

print(f"\nverification: {PASS}/{PASS + FAIL} checks pass")
sys.exit(1 if FAIL else 0)
