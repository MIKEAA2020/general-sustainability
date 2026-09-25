#!/usr/bin/env python3
"""Applied-regime-viability v2: exact rational verification (standard library only)."""
import csv, sys
from fractions import Fraction as F

PASS, FAIL = [], []
def chk(cond, name):
    (PASS if cond else FAIL).append(name)

BASE = "/home/user/arena agent 1/paper rewrites/latex"
def rows(path):
    with open(f"{BASE}/{path}", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def num(s):
    s = (s or "").replace(",", "").replace("\u2212", "-").strip()
    return F(s) if s not in ("", "NA", "na", "-") else None

# ---------- inputs ----------
a2 = rows("paperE1_calibration_data_v1_wave_e_cod/ncam_2016_table_a2.csv")
ssb = {int(float(r["year"])): F(r["ssb_kt"]) for r in a2}
mm = {int(float(r["year"])): F(r["M_age5_14"]) for r in a2}
chk(len(a2) == 33 and set(ssb) == set(range(1983, 2016)), "A2: 33 rows, SSB 1983-2015 complete")

rems = {int(float(r["year"])): F(r["catch_t"])
        for r in rows("paperE1_calibration_data_v1_wave_e_cod/dfo_2025_table1_landings.csv")}
chk(rems.get(1992) == F(40956) and rems.get(1993) == F(11392), "removals 1992=40956, 1993=11392 t")
chk(rems.get(2015) == F(4436), "removals 2015=4436 t (official)")

sc = {int(float(r["year"])): F(r["catch_t"])
      for r in rows("paperE1_calibration_data_v1_wave_e_cod/catch_schijns_2021.csv")}
chk(sc.get(1994) == F(1314) and sc.get(1995) == F(413), "reconstruction 1994=1314, 1995=413 t")
chk(sc.get(2015) == F(4436) == rems.get(2015), "cross-file: reconstruction 2015 = official 2015 = 4436 t")
chk(all(sc[y] > F(130000) for y in range(1983, 1990)),
    "reconstruction: all 1983-1989 removals above 130,000 t")

rvv = {}
dup_ok = True
for r in rows("paperE1_calibration_data_v1_wave_e_cod/rv_fall_abundance_schijns_table3.csv"):
    y = int(float(r["year"])); v = F(r["rv_abundance_index"])
    if y in rvv and rvv[y] != v:
        dup_ok = False
    rvv[y] = v
chk(dup_ok, "survey file: duplicate year rows are row-consistent (no contradiction)")
chk(rvv.get(1989) == F(2127417) and rvv.get(1991) == F(1117670), "survey 1989=2127417, 1991=1117670")
chk(rvv.get(1992) == F(239740) and rvv.get(1993) == F(90709) and rvv.get(1994) == F(21797),
    "survey 1992=239740, 1993=90709, 1994=21797")

ramssb = {}
for r in rows("paperE1_calibration_data_v1_ram_timeseries.csv"):
    if r["SSB"]:
        v = F(int(round(float(r["SSB"]))))
        if v > 10000:
            v = v / 1000
        ramssb[int(float(r["year"]))] = v
chk([ramssb.get(y) for y in range(2016, 2022)] == [F(340), F(433), F(394), F(419), F(440), F(411)],
    "RAM SSB 2016-2021 = 340,433,394,419,440,411 kt")

xte_ratio = {int(float(r["year"])): F(r["ssb_over_blim"])
             for r in rows("paperE1_calibration_data_v1_wave_e_cod/xtencam_table17_ssb.csv")}

# ---------- windows ----------
mult = {y: ssb[y + 1] / ssb[y] for y in range(1983, 1990)} | {1991: ssb[1992] / ssb[1991], 1992: ssb[1993] / ssb[1992]}
gmin_y = min(range(1983, 1990), key=lambda y: mult[y])
chk(gmin_y == 1985 and mult[1985] == F(41800, 45147), "good-window worst multiplier 41800/45147 at 1985->86")
chk(mult[1991] == F(38195, 73451) and mult[1992] == F(2021, 7639), "bad-window multipliers 38195/73451, 2021/7639")

# ---------- breach ----------
chk(mult[1992] <= F(27600, 73451), "breach bound 2021/7639 <= 27600/73451 (exact cross-mult)")
chk(ssb.get(1993) is not None and float(ssb[1993]) == 101.05 and ssb[1993] < F(276), "1993 SSB 101.05 < 276")
chk(xte_ratio.get(1993) == F(29, 100), "xteNCAM ratio at 1993 = 0.29")
chk(ssb.get(1991) is not None and float(ssb[1991]) == 734.51 and ssb[1991] < F(8846, 10), "1991 734.51 < 884.6 (LRP already breached)")

# ---------- marginal decade ----------
vals = [ssb[y] for y in range(1983, 1990)]
mean = sum(vals) / 7
chk(abs(float(mean) - 884.58) < 0.005, "decade mean = 884.58 kt (LRP provenance)")
dec = {y: ssb[y] / F(8846, 10) for y in range(1983, 1990)}  # ratios against the LRP 884.6
dmin_y = min(dec, key=lambda y: dec[y]); dmax_y = max(dec, key=lambda y: dec[y])
chk(dec[dmin_y] == F(4180, 4423) and dmin_y == 1986, "decade min ratio 4180/4423 (1986)")
chk(dec[dmax_y] == F(94075, 88460) and dmax_y == 1987, "decade max ratio 94075/88460 (1987)")
r = F(41800, 45147)
chk(r ** 16 <= F(27600, 92166) < r ** 15, "rho_g^16 <= 27600/92166 < rho_g^15 (sixteen years)")

# ---------- survey + covariate ----------
chk(rvv[1994] / rvv[1989] == F(21797, 2127417), "survey factor 21797/2127417 (1989-1994)")
chk(rvv[1992] / rvv[1991] == F(239740, 1117670), "survey factor 239740/1117670 (1992)")
cap = rows("paperE1_calibration_data_v1_wave_e_cod/capelin_acoustic_observed.csv")
capb = {int(float(r_["year"])): F(r_["acoustic_kt"]) for r_ in cap}
chk(capb.get(1990) == F(5783) and capb.get(1991) == F(138), "capelin 1990=5783, 1991=138 kt")
m = mm
chk(m.get(1990) == F(403, 1000) and m.get(1991) == F(1002, 1000), "M diagnostic 0.403 (1990) -> 1.002 (1991)")

# ---------- recovery ----------
chk(all(ramssb[y] >= F(276) for y in range(2016, 2022)), "recovery: above 276 kt every year 2016-2021")
chk(ramssb[2020] == F(440) and F(44000, 88460) < F(5, 10), "outcome max 440 kt < 50% of LRP (44000/88460)")

# ---------- headline needles ----------
tex = open(f"{BASE}/applied_regime_viability_v2.tex", encoding="utf-8").read()
for needle in ["41800/45147", "2021}{7639", "38195}{73451", "40{,}956", "11{,}392", "1{,}314",
               "413", "4{,}436", "2{,}127{,}417", "21{,}797", "1{,}117{,}670", "239{,}740", "90{,}709",
               "138}{5783", "0.945", "1.064", "0.265", "0.520", "884.6", "0.29", "0.403",
               "1.002", "340, 433, 394,", "49.7", "sixteen years", "Section 3.10",
               "independent of the assessment models", "observed rows"]:
    chk(needle in tex, f"needle: {needle!r}")
for bad in ["programme", "edition", "flagship", "board", "charter", "L4", "Abaee (2026a, 2026b)"]:
    if bad in tex:
        FAIL.append(f"meta-marker absent: {bad!r}")
    else:
        PASS.append(f"meta-marker absent: {bad!r}")

print(f"{len(PASS)}/{len(PASS) + len(FAIL)} checks pass (chained seeds: predecessor scripts of the applied pair)")
if FAIL:
    print("FAILED:"); [print("  -", f) for f in FAIL]; sys.exit(1)
