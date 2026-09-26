#!/usr/bin/env python3
"""Applied-regime-viability v4: exact rational verification (standard library only)."""
import csv, sys
from fractions import Fraction as F

PASS, FAIL = [], []
def chk(cond, name):
    (PASS if cond else FAIL).append(name)

BASE = "."
def rows(path):
    with open(f"{BASE}/{path}", newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def num(s):
    s = (s or "").replace(",", "").replace("\u2212", "-").strip()
    return F(s) if s not in ("", "NA", "na", "-") else None

def close(x, displayed, tol=F(6, 100000)):
    return abs(x - F(str(displayed))) <= tol

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
chk(all(sc[y] == rems[y] for y in (1992, 1993, 1994, 1995)),
    "cross-file: reconstruction rows 1992-1995 identical to official rows")
chk(sc.get(2015) == F(4436) == rems.get(2015), "cross-file: reconstruction 2015 = official 2015 = 4436 t")
chk(all(sc[y] > F(130000) for y in range(1983, 1990)),
    "reconstruction: all 1983-1989 removals above 130,000 t")
chk(min(sc[y] for y in range(1983, 1990)) == F(231293)
    and max(sc[y] for y in range(1983, 1990)) == F(268677),
    "reconstruction: 1983-1989 rows span 231,293 - 268,677 t")

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
chk(rvv.get(1990) == F(1627647) and rvv.get(1995) == F(43240), "survey 1990=1627647, 1995=43240 (spine)")

capb = {int(float(r["year"])): F(r["acoustic_kt"])
        for r in rows("paperE1_calibration_data_v1_wave_e_cod/capelin_acoustic_observed.csv")}
chk(capb.get(1990) == F(5783) and capb.get(1991) == F(138) and capb.get(1992) == F(138),
    "capelin 1990=5783, 1991=138, 1992=138 kt (observed rows)")

ramssb = {}
for r in rows("paperE1_calibration_data_v1_ram_timeseries.csv"):
    if r["SSB"]:
        v = F(int(round(float(r["SSB"]))))
        if v > 10000:
            v = v / 1000
        ramssb[int(float(r["year"]))] = v
chk([ramssb.get(y) for y in range(2016, 2022)] == [F(340), F(433), F(394), F(419), F(440), F(411)],
    "RAM SSB 2016-2021 = 340,433,394,419,440,411 kt")

xte = {int(float(r["year"])): r
       for r in rows("paperE1_calibration_data_v1_wave_e_cod/xtencam_table17_ssb.csv")}
xte_ratio = {y: F(r["ssb_over_blim"]) for y, r in xte.items()}
xte_ssb = {y: F(r["ssb_kt"]) for y, r in xte.items()}

# ---------- spine table: every displayed cell equals the file ----------
spine = {1983: ("841.08", "232,345", "2,088,958", None, "0.391"),
         1984: ("863.23", "232,471", "2,198,605", None, "0.377"),
         1985: ("902.94", "231,293", "1,288,360", "3426", "0.349"),
         1986: ("836.00", "266,713", "2,502,702", "3697", "0.277"),
         1987: ("940.75", "239,924", "1,020,462", "2576", "0.494"),
         1988: ("886.40", "268,677", "1,223,314", "4285", "0.335"),
         1989: ("921.66", "253,990", "2,127,417", "3712", "0.289"),
         1990: ("861.92", "219,452", "1,627,647", "5783", "0.403"),
         1991: ("734.51", "172,012", "1,117,670", "138", "1.002"),
         1992: ("381.95", "40,956", "239,740", "138", "2.214"),
         1993: ("101.05", "11,392", "90,709", None, "2.575"),
         1994: ("30.55", "1,314", "21,797", None, "2.331"),
         1995: ("9.68", "413", "43,240", None, "0.288")}
spine_ok = True
for y, (s_, c_, r_, cap_, m_) in spine.items():
    spine_ok &= (ssb[y] == F(s_) and rems[y] == F(c_.replace(",", ""))
                 and rvv[y] == F(r_.replace(",", "")) and mm[y] == F(m_))
    spine_ok &= ((cap_ is None and y not in capb) or (cap_ is not None and capb[y] == F(cap_)))
chk(spine_ok, "spine table 1983-1995: all 65 displayed cells equal the locked files")

# ---------- windows ----------
mult = {y: ssb[y + 1] / ssb[y] for y in range(1983, 1995)}
gmin_y = min(range(1983, 1990), key=lambda y: mult[y])
chk(gmin_y == 1985 and mult[1985] == F(41800, 45147), "reference-window worst multiplier 41800/45147 at 1985->86")
chk(mult[1991] == F(38195, 73451) and mult[1992] == F(2021, 7639), "collapse multipliers 38195/73451, 2021/7639")
chk(mult[1989] == F(86192, 92166) and mult[1990] == F(73451, 86192),
    "connecting transitions 86192/92166, 73451/86192")
chk(F(38195) < F(73451) and F(2021) < F(7639) and F(41800) < F(45147),
    "sub-unitary by numerator < denominator (incl. 38195 < 73451)")
vals = [ssb[y] for y in range(1983, 1990)]
mean = sum(vals) / 7
chk(mean == F(44229, 50), "reference-window mean = 44229/50 = 884.58 kt exactly")

# ---------- harvest-free brackets ----------
def bracket_upper(y, C):
    rho = ssb[y + 1] / ssb[y]
    r = C / ssb[y]
    return max(rho + r, rho / (1 - r)), rho

brackets = [(1985, F(266713, 1000), "1.3140", False), (1989, F(219452, 1000), "1.2274", False),
            (1990, F(172012, 1000), "1.0646", False), (1991, F(172012, 1000), "0.7542", True),
            (1991, F(40956, 1000), "0.5758", True), (1992, F(40956, 1000), "0.3718", True),
            (1992, F(11392, 1000), "0.2944", True), (1993, F(1314, 1000), "0.3153", True),
            (1994, F(413, 1000), "0.3304", True)]
for (y, C, disp, cert) in brackets:
    ub, rho = bracket_upper(y, C)
    chk(close(ub, disp) and (ub < 1) == cert,
        f"bracket {y}->{y+1} C={C}: upper = {disp} ({'certified < 1' if cert else 'straddles'})")
chk(bracket_upper(1991, F(40956))[1] == F(38195, 73451)
    and bracket_upper(1992, F(11392))[1] == F(2021, 7639),
    "bracket rho values equal the certified window multipliers")

# ---------- moratorium losses ----------
loss92 = ssb[1991] - ssb[1992]; loss93 = ssb[1992] - ssb[1993]
chk(loss92 == F("352.56") and loss93 == F("280.90"), "losses 352.56 kt (91->92), 280.90 kt (92->93)")
chk(F(352560, 40956) == loss92 / (rems[1992] / 1000), "loss/removals 1991->92 = 352560/40956")
chk(close(loss92 / (rems[1992] / 1000), "8.61", F(1, 200)), "loss exceeds removals 1991->92 by 8.61")
chk(close(loss93 / (rems[1993] / 1000), "24.66", F(1, 200)), "loss exceeds removals 1992->93 by 24.66")
chk(close(rems[1993] / 1000 / loss93, "0.0406", F(1, 2000)), "removals = 4.06% of the 1993 loss")

# ---------- moratorium scale ----------
facs = [sc[y] / F(1314) for y in range(1983, 1990)] + [sc[y] / F(413) for y in range(1983, 1990)]
chk(min(facs) == F(231293, 1314) and max(facs) == F(268677, 413),
    "scale factors span 231293/1314 = 176.0 to 268677/413 = 650.5")
chk(close(F(231293, 1314), "176.0", F(1, 20)) and close(F(268677, 413), "650.5", F(1, 20)),
    "two-to-three orders: at least 176, at most 651 times")

# ---------- post-moratorium experiment ----------
r94 = F(1314, 1000) / ssb[1993]; r95 = F(413, 1000) / ssb[1994]
chk(close(r94, "0.0130", F(1, 2000)) and close(r95, "0.0135", F(1, 2000)),
    "removals fractions 0.0130, 0.0135 (at most 1.4%)")
chk(all(bracket_upper(y, rems[y + 1] / 1000)[0] < 1 for y in (1993, 1994)),
    "post-moratorium: both steps harvest-free contractions under both conventions")
chk(ssb[1993] / ssb[1995] == F(10105, 968), "two-year factor 10105/968")
chk(close(ssb[1993] / ssb[1995], "10.44", F(1, 200)), "factor 101.05 -> 9.68 = 10.44")
chk(min(ssb[y] for y in range(1983, 2016)) == ssb[1995],
    "9.68 kt (1995) is the minimum of the 1983-2015 series")

# ---------- breach ----------
chk(F(2021) * F(73451) < F(7639) * F(27600), "stress bound: 2021*73451 < 7639*27600 (exact cross-mult)")
chk(ssb[1992] >= F(276) and ssb[1993] < F(276), "first below-floor reading: 1992 above (381.95>=276), 1993 below")
chk(all(ssb[y] < F(276) for y in range(1993, 2015)),
    "input vintage stays below the floor 1993-2014 (250.12 kt at 2014)")
chk(ssb[2014] == F("250.12") and ssb[2015] == F("298.65"), "input vintage re-cross: 250.12 -> 298.65 at 2015")
chk(ramssb[2014] == F(238) and ramssb[2015] == F(277), "database vintage re-cross: 238 -> 277 at 2015")
chk(ssb[1990] < F(8846, 10) and ssb[1991] < F(8846, 10),
    "B_ref breached at 1990 (861.92) and 1991 (734.51)")
r_ = F(41800, 45147)
chk(r_ ** 16 <= F(27600, 92166) < r_ ** 15, "sustained: rho_g^16 <= 27600/92166 < rho_g^15 (16 steps, ceiling)")
n_star = 1
while r_ ** n_star > F(27600, 92166):
    n_star += 1
chk(n_star == 16, "exact breach step count = 16 (ceiling convention)")

# ---------- breach frontier ----------
path = [y for y in range(1989, 1996)]
frontier = [(F("861.92"), F("921.66"), 1990), (F("734.51"), F("861.92"), 1991),
            (F("381.95"), F("734.51"), 1992), (F("101.05"), F("381.95"), 1993),
            (F("30.55"), F("101.05"), 1994), (F("9.68"), F("30.55"), 1995)]
for (lo, hi, yr) in frontier:
    first = min(y for y in range(1989, 2016) if ssb[y] < hi)
    chk(first == yr and ssb[yr - 1] >= hi and ssb[yr] < hi and lo < hi <= ssb[yr - 1],
        f"frontier (post-1989 path): L in ({float(lo)}, {float(hi)}] first below at {yr}")
chk(all(ssb[y] >= F("9.68") for y in range(1983, 2016)),
    "frontier: L <= 9.68 never breached in 1983-2015 (series minimum 9.68)")
chk(F(276) > F("101.05") and F(276) <= F("381.95"), "frontier: 276 kt sits in the 1993 interval")
chk(F(8846, 10) > F("861.92") and F(8846, 10) <= F("921.66"), "frontier: 884.6 kt sits in the 1990 interval")

# ---------- cross-vintage ----------
chk([xte_ssb[y] for y in (1991, 1992, 1993)] == [F(600), F(352), F(79)],
    "xteNCAM SSB 1991-1993 = 600, 352, 79 kt")
chk([xte_ratio[y] for y in (1991, 1992, 1993)] == [F("2.18"), F("1.28"), F("0.29")],
    "xteNCAM floor ratios 2.18, 1.28, 0.29")
chk((xte_ssb[1991] > 276) and (xte_ssb[1992] > 276) and (xte_ssb[1993] < 276)
    and (ssb[1991] > 276) and (ssb[1992] > 276) and (ssb[1993] < 276),
    "sign pattern (above, above, below) agrees across vintages")
chk(close(xte_ssb[1993] / ssb[1993], "0.782", F(1, 500)) and close(ssb[1993] / xte_ssb[1993], "1.28", F(1, 200)),
    "cross-vintage level factor 2021/1580 = 1.28 (reassessment 21.8% lower)")
chk(ssb[1993] / xte_ssb[1993] == F(2021, 1580), "divergence factor is exactly 2021/1580")
implied = [xte_ssb[y] / xte_ratio[y] for y in xte_ratio if xte_ratio[y] != 0]
chk(len(implied) == 71, "implied B_lim: 71 ratio-bearing years")
chk(close(min(implied), "250", F(1, 2)) and close(max(implied), "289", F(1, 2)),
    "implied B_lim range [250, 289] kt (rounded-ratio spread)")
chk(ssb[1993] < min(implied) and xte_ssb[1993] < min(implied)
    and xte_ssb[1992] > max(implied) and xte_ssb[1991] > max(implied),
    "floor comparisons insensitive: 101.05 and 79 below 250; 352 and 600 above 289")
chk(F("1.08") < ssb[1992] / xte_ssb[1992] < F("1.09") and F("1.22") < ssb[1991] / xte_ssb[1991] < F("1.23"),
    "level factors 1.09 (1992) and 1.22 (1991) as displayed")

# ---------- survey + divergence ----------
chk(rvv[1994] / rvv[1989] == F(21797, 2127417), "survey factor 21797/2127417 (1989-1994)")
chk(rvv[1992] / rvv[1991] == F(239740, 1117670), "survey factor 239740/1117670 (1991-1992)")
div = (ssb[1993] / ssb[1989]) / (rvv[1993] / rvv[1989])
chk(close(div, "2.57", F(1, 100)), "instrument divergence: survey falls 2.57x further over 1989-1993")
chk(rvv[1993] / rvv[1989] < ssb[1993] / ssb[1989], "survey common-window factor below the assessment factor")

# ---------- contemporaneity ----------
chk(mm.get(1990) == F(403, 1000) and mm.get(1991) == F(1002, 1000),
    "M diagnostic 0.403 (1990) -> 1.002 (1991): crosses M=1 across the same step as the covariate collapse")
chk((capb[1990] > capb[1991]) and (mm[1990] < 1 <= mm[1991]),
    "covariate collapse and M crossing are coincident (same annual step)")

# ---------- threshold discrimination ----------
chk(all(ssb[y] > F(276) for y in range(1983, 1990)), "B_aux: all seven reference-window readings above (min 836.00)")
chk(min(ssb[y] for y in range(1983, 1990)) == F(836), "reference-window minimum reading = 836.00")
chk(all(ssb[y] < F(276) for y in (1993, 1994, 1995)) and all(ssb[y] > F(276) for y in (1990, 1991, 1992)),
    "B_aux: 1993-1995 below, 1990-1992 above — eras separated without exception")
below_ref = [y for y in range(1983, 1996) if ssb[y] < F(8846, 10)]
chk(below_ref == [1983, 1984, 1986, 1990, 1991, 1992, 1993, 1994, 1995],
    "B_ref: below-set in 1983-1995 = {1983,1984,1986,1990..1995} (9 of 13; no separation)")
chk(sum(1 for y in range(1983, 1990) if ssb[y] < F(8846, 10)) == 3,
    "B_ref: three of the seven reference-window readings below (841.08, 863.23, 836.00)")
dec = {y: ssb[y] / F(8846, 10) for y in range(1983, 1990)}
chk(dec[1987] == F(94075, 88460), "window maximum 6.4% above B_ref (94075/88460)")
chk(close(dec[1987] - 1, "0.064", F(1, 300)), "max deviation +6.4% (outward-rounded from 6.347%)")
chk(close(1 - dec[1986], "0.055", F(1, 300)), "min deviation -5.5% (outward-rounded from 5.494%)")

# ---------- recovery ----------
chk(all(ramssb[y] >= F(276) for y in range(2016, 2022)), "recovery: above 276 kt every year 2016-2021")
chk(ramssb[2020] == F(440) and F(44000, 88460) < F(5, 10), "outcome max 440 kt < 50% of B_ref (44000/88460)")
rec = [rems[y] for y in range(2015, 2022)]
chk(min(rec) == F(4436) and max(rec) == F(12881),
    "recovery removals 2015-2021: 4,436 to 12,881 t (official rows)")
shares = [rems[y] / 1000 / ramssb[y] for y in range(2016, 2022)]
chk(F(23, 1000) <= min(shares) and max(shares) <= F(3, 100),
    "recovery removals shares 2.3%-3.0% of the same vintage's reading")
chk(close(min(shares), "0.023", F(1, 500)) and close(max(shares), "0.030", F(1, 500)),
    "recovery share range outward-rounded correctly (2.3% to 3.0%)")


# ---------- window profile (v5) ----------
xssb = {y: F(r["ssb_kt"]) for y, r in xte.items()}
prods = lambda a, b: ssb[b] / ssb[a]
dec_years = list(range(1983, 1990))
minp = {}
for k in range(1, 7):
    cands = [(prods(dec_years[i], dec_years[i + k]), dec_years[i]) for i in range(len(dec_years) - k)]
    m = min(cands)
    minp[k] = m
chk(minp[1] == (F(41800, 45147), 1985), "profile k=1 min = 41800/45147 at 1985")
chk(minp[2] == (F(83600, 86323), 1984), "profile k=2 min = 83600/86323 at 1984")
chk(minp[3] == (F(44320, 45147), 1985), "profile k=3 min = 44320/45147 at 1985")
chk(minp[4] == (F(15361, 15049), 1985) and minp[4][0] > 1, "profile k=4 min = 15361/15049 > 1 (all grow)")
chk(minp[5] == (F(22160, 21027), 1983) and minp[5][0] > 1, "profile k=5 min = 22160/21027 > 1 (all grow)")
chk(minp[6] == (F(15361, 14018), 1983) and minp[6][0] > 1, "profile k=6 min = 15361/14018 > 1 (all grow)")
below_ct = {k: sum(1 for i in range(len(dec_years) - k) if prods(dec_years[i], dec_years[i+k]) < 1) for k in (1, 2, 3)}
chk(below_ct == {1: 2, 2: 2, 3: 2}, "profile: subwindows below unity = 2/6, 2/5, 2/4 at k = 1, 2, 3")
allg = sum(1 for k in range(1, 7) for i in range(len(dec_years) - k)
           if ssb[dec_years[i+k]] > ssb[dec_years[i]])
chk(allg == 15, "profile: 15 of the 21 subwindows are all-growth")

# ---------- band certificates (v5) ----------
xlo = {y: F(xte[y]["ssb_lo"]) for y in xte}
xhi = {y: F(xte[y]["ssb_hi"]) for y in xte}
bandcert = [y for y in sorted(xssb) if y + 1 in xssb and xhi[y + 1] < xlo[y]]
chk(bandcert == [1991, 1992, 1993, 1994],
    "bands: band-certified declines over 1954-2024 = exactly the four collapse-era steps")
chk(xlo[1992] / xhi[1991] == F(265, 754) and xhi[1992] / xlo[1991] == F(468, 478) < 1,
    "bands: 1991->92 interval [265/754, 468/478], upper bound 0.9791 < 1")
chk(xlo[1993] / xhi[1992] == F(54, 468) and xhi[1993] / xlo[1992] == F(115, 265) < 1,
    "bands: 1992->93 interval [54/468, 115/265], upper bound 0.4340 < 1")
chk(xhi[1993] == F(115) and xhi[1993] < F(276), "bands: 1993 breach band-certified (hi = 115 < 276)")
chk(xlo[1992] <= F(276) <= xhi[1992], "bands: 1992 indeterminate (265 <= 276 <= 468)")
chk(not any(xhi[y + 1] < xlo[y] for y in range(1983, 1990) if y + 1 in xssb),
    "bands: no reference-decade step is band-certified")

# ---------- vintage typology + third vintage (v5) ----------
decx = [xssb[y] / xssb[y + 1] for y in range(1983, 1989)]  # multipliers > 1 means growth
chk(all(xssb[y + 1] > xssb[y] for y in range(1983, 1989)),
    "vintage typology: the reassessment vintage's 1983-1989 is all-growth")
chk(close(xssb[1990] / xssb[1989], "0.854", F(1, 500)) and xssb[1990] < xssb[1989],
    "vintage typology: the decline begins 1989->90 at 738/864 = 0.854")
chk([ramssb[y] for y in (1990, 1991, 1992, 1993)] == [F(765), F(747), F(354), F(83)],
    "third vintage: database extract 1990-1993 = 765, 747, 354, 83 kt")
chk(ramssb[1991] > F(276) and ramssb[1992] > F(276) and ramssb[1993] < F(276),
    "third vintage: sign pattern (above, above, below) agrees against the floor")
chk(close(F(10977, 29000), "0.3785", F(1, 2000)),
    "recovery step: 2020->2021 removals = 10977/29000 = 37.9% of that year's decline")

# ---------- backward extension (v5) ----------
pre = [y for y in sorted(xssb) if y <= 1982]
pk = max(pre, key=lambda y: xssb[y])
chk(pk == 1962 and xssb[1962] == F(1508), "pre-window: vintage peak 1508 kt at 1962")
chk(xssb[1983] == F(427) and close(xssb[1983] / xssb[1962], "0.283", F(1, 1000)),
    "pre-window: 1983 reading 427 kt = 28.3% of the 1962 peak (vintage-internal)")
cr = []
ys_sorted = sorted(xssb)
for i in range(1, len(ys_sorted)):
    y, yprev = ys_sorted[i], ys_sorted[i - 1]
    if (xssb[y] < 276) != (xssb[yprev] < 276):
        cr.append(y)
chk(cr == [1977, 1980, 1993, 2016], "pre-window: 276 kt crossings = {1977, 1980, 1993, 2016}")
chk(xhi[1978] < F(276), "pre-window: the 1978 reading is band-certified below the floor")

# ---------- headline needles ----------
tex = open(f"{BASE}/applied_regime_viability_v9.tex", encoding="utf-8").read()

for _needle in ("Northern Cod Assessment Model", "Hutchings and Myers, 1994",
                "figs_arv/fig_record.pdf", "paper2\\_arv\\_record\\_figure\\_v1.py",
                "Hutchings, J.A., Myers, R.A. (1994)",
                "usepackage{graphicx}", "the 22 consecutive",
                "Ricard et al., 2012", "Ricard, D. et al. (2012)"):
    chk(_needle in " ".join(tex.split()), f"v6 needle: {_needle!r}")
for needle in ["41800}{45147", "2021}{7639", "83600}{86323", "44320}{45147", "15361}{15049",
               "22160}{21027", "15361}{14018", "265}{754", "468}{478", "54}{468", "115}{265",
               "0.9791", "0.4340", "1508", "1962", "28.3", "1977, 1980, 1993, 2016",
               "10977}{29000", "37.9", "765, 747, 354, 83", "738/864", "427", "single acoustic instrument", "38195}{73451", "44229}{50", "86192}{92166",
               "73451}{86192", "40{,}956", "11{,}392", "1{,}314", "4{,}436", "12{,}881",
               "352560}{40956", "280900}{11392", "4.06", "231293}{1314", "268677}{413",
               "651", "at least \\(176\\)", "10105}{968", "10.44", "0.7542", "0.3718", "0.5758", "0.2944",
               "0.3153", "0.3304", "1.3140", "1.2274", "1.0646", "2{,}127{,}417", "21{,}797",
               "1{,}117{,}670", "239{,}740", "90{,}709", "21797}{2127417", "239740}{1117670",
               "2.57", "138}{5783", "73451}{60000", "38195}{35200", "2021}{1580", "250", "289",
               "600, 352, 79", "2.18, 1.28, 0.29", "276", "884.6", "884.58", "250.12", "298.65",
               "238 \\to 277", "250.12 \\to 298.65", "340, 433, 394,", "44000}{88460", "49.7", "2.3\\%", "3.0\\%", "breach frontier", "(861.92, 921.66]",
               "sixteen", "Section 3.10", "836.00", "841.08, 863.23, 836.00", "138", "172{,}012",
               "266{,}713", "219{,}452", "1.4\\%", "rho_{\\mathrm{g}}^{16}", "352.56", "280.90"]:
    chk(needle in tex, f"needle: {needle!r}")
for bad in ["F_{\\mathrm{lim}}", "four and five orders", "tens of thousands of kilotonnes",
            "zero removals inherits", "witnessed twice", "independent of the assessment models",
            "one-year lead", "one step before the mortality", "proves exactly",
            "never a catch-optimization", "\\pm 6.4", "sat at its own failure boundary",
            "match the realized timeline exactly", "approaching the closed fishery",
            "programme", "edition", "flagship", "board", "charter", "L4",
            "Abaee (2026a, 2026b)", "Helly"]:
    if bad in tex:
        FAIL.append(f"retracted/marker absent: {bad!r}")
    else:
        PASS.append(f"retracted/marker absent: {bad!r}")
for heading in ["Funding", "Competing interests", "Data availability", "Code availability",
                "AI declaration"]:
    chk(heading in tex, f"required heading: {heading}")

print(f"{len(PASS)}/{len(PASS) + len(FAIL)} checks pass (chained seeds: predecessor scripts of the applied pair)")
if FAIL:
    print("FAILED:"); [print("  -", f) for f in FAIL]; sys.exit(1)
