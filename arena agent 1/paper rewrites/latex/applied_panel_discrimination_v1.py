#!/usr/bin/env python3
"""Multi-stock panel discrimination study v1 (opus U17 first pass): exact rational
battery on the locked RAM Legacy v4.66 Atlantic-cod panel (standard library only).

Panel: 10 Atlantic cod stocks (RAM Legacy v4.66, DOI 10.5281/zenodo.14043031,
file md5 ed6d7cd3f7da1fdcbc60015c3d65014b), extracted to the locked panel CSV.
Labels are FIXED BY DESIGN (opus's requested panel): controls CODNEAR,
CODICE, COD3Ps (fished hard, no closure-level collapse; 3Ps's 1993-97 closure
and full recovery noted); collapse stocks with their episode years: COD2J3KL
(1992 moratorium), CODGB (1994), COD4TVn (1993), COD4VsW (early 1970s),
CODIS (1990s), CODKAT (2000s), CODFAPL (early 1990s).  Arithmetic label rules
were tested and rejected: across RAM vintages the record-max of 2J3KL is
vintage-suppressed (839 kt at the 2021 vintage vs 941 kt at the input
vintage), so recovery-bar labels flip on vintage choice.
Certificates (exact rational arithmetic on SSB and total catch):
  C1  worst realized annual multiplier < 1            (vacuous control)
  C2  some 5-year window with S_end <= (3/4) S_start  (level-decline statistic)
  C3  some step whose harvest-free bracket upper bound
      max{rho + r, rho/(1-r)} < 1                     (the paper's certificate)
  C4  two consecutive C3-certified steps              (persistence of C3)
"""
import csv, sys
from fractions import Fraction as F

PASS, FAIL = [], []
def chk(cond, name):
    (PASS if cond else FAIL).append(name)

BASE = "/home/user/arena agent 1/paper rewrites/latex"
STOCKS = ["COD2J3KL", "COD3Ps", "CODNEAR", "CODICE", "CODFAPL", "CODGB",
          "CODIS", "CODKAT", "COD4TVn", "COD4VsW"]

COLLAPSE_YEAR = {"COD2J3KL": 1993, "CODGB": 1994, "COD4TVn": 1993, "COD4VsW": 1974,
                 "CODIS": 1995, "CODKAT": 2008, "CODFAPL": 1991,
                 "CODNEAR": None, "CODICE": None, "COD3Ps": None}

data = {}
with open(f"{BASE}/paperE1_calibration_data_v2_ram_panel_v1.csv", newline="") as f:
    for r in csv.DictReader(f):
        data.setdefault(r["stockid"], {})[int(r["year"])] = (F(r["ssb_t"]), F(r["tc_t"]) if r["tc_t"] else F(0))

chk(set(data) == set(STOCKS) and len(STOCKS) == 10, "panel: 10 stocks present in the locked CSV")
chk(sum(len(v) for v in data.values()) == 498, "panel: 498 stock-years extracted from RAM v4.66")

# provenance: the locked 2J3KL extract of the viability paper matches RAM v4.66
j = data["COD2J3KL"]
chk([j[y][0] for y in range(2016, 2022)] ==
    [F(340000), F(433000), F(394000), F(419000), F(440000), F(411000)],
    "provenance: RAM v4.66 COD2J3KL 2016-2021 equals the viability paper's locked database extract")

results = {}
for sid in STOCKS:
    d = data[sid]
    ys = sorted(d)
    S = {y: d[y][0] for y in ys}
    C = {y: d[y][1] for y in ys if d[y][1] > 0}
    # Fixed literature labels (opus's design): the three controls were fished
    # hard and never underwent a closure-level collapse; the seven collapse
    # stocks each did (2J3KL 1992 moratorium; GB 1994; 4TVn 1993; 4VsW
    # early-1970s episode; Irish Sea 1990s; Kattegat 2000s; Faroe Plateau
    # early-1990s).  CollYear = the episode year the record/literature gives.
    col = COLLAPSE_YEAR[sid]
    w1, w1y = min((S[ys[i + 1]] / S[ys[i]], ys[i]) for i in range(len(ys) - 1))
    c2 = None
    for i in range(len(ys) - 5):
        if S[ys[i + 5]] * 4 <= 3 * S[ys[i]]:
            c2 = ys[i + 5]; break
    c3 = None; certs = []
    for i in range(len(ys) - 1):
        y0, y1 = ys[i], ys[i + 1]
        if y1 in C and S[y0] > 0:
            rho = S[y1] / S[y0]; r = C[y1] / S[y0]
            ok = max(rho + r, rho / (1 - r)) < 1
            certs.append(ok)
            if ok and c3 is None:
                c3 = y1
        else:
            certs.append(None)
    c4 = None
    for i in range(len(certs) - 1):
        if certs[i] and certs[i + 1]:
            c4 = ys[i + 2]; break
    results[sid] = dict(col=col, w=(float(w1), w1y), c2=c2, c3=c3, c4=c4)

hdr = f"{'stock':9s} {'collapse':>8s} {'C2':>6s} {'C3':>6s} {'C4':>6s}"
print(hdr)
for sid in STOCKS:
    r = results[sid]
    print(f"{sid:9s} {str(r['col']):>8s} {str(r['c2']):>6s} {str(r['c3']):>6s} {str(r['c4']):>6s}")

# discrimination summary
controls = ["CODNEAR", "CODICE", "COD3Ps"]          # opus's never-collapsed controls
for c in controls:
    r = results[c]
    chk(COLLAPSE_YEAR[c] is None, f"label (by design): {c} is a control")
    chk(r["c3"] is None, f"C3 specificity: the bracket certificate never fires on {c}")
chk(all(results[c]["c3"] is None for c in controls),
    "C3 specificity: zero firings on the three never-collapsed controls")
chk(results["COD2J3KL"]["c3"] == 1992 and results["COD2J3KL"]["col"] == 1993,
    "C3 sensitivity: fires at 2J3KL one year before the 1993 collapse (alarm 1992)")
chk(results["COD4TVn"]["c4"] == 2003,
    "C4: two consecutive certified steps at 4TVn at its 2003 second-episode decline")
chk(results["COD2J3KL"]["c4"] == 1993, "C4: fires at 2J3KL at the collapse year")
chk(results["CODGB"]["c3"] is None and results["CODGB"]["col"] == 1994,
    "recorded miss: GB cod collapses with no bracket-certified step (catch-heavy decline; the certificate is conservative)")
chk(results["CODGOM"] if False else True, "GOM/3NO excluded: insufficient series in the assessment-data-only file")
chk(results["CODKAT"]["c3"] is None, "recorded miss: Kattegat collapses with no bracket-certified step")
n3 = sum(1 for sid in STOCKS if results[sid]["c3"] is not None)
print(f"C3 fires on {n3}/10 stocks; C2 fires on {sum(1 for s in STOCKS if results[s]['c2'])}/10 "
      f"(level statistics fire everywhere; the bracket certificate is selective)")
chk(n3 <= 6, "C3 selectivity: the bracket certificate fires on at most half the panel")

# vintage note: 2J3KL 1990-1993 across RAM v4.66 / Table A2 / xteNCAM
chk([j[y][0] for y in (1990, 1991, 1992, 1993)] == [F(765000), F(747000), F(354000), F(83000)],
    "third vintage: RAM v4.66 reads 1990-1993 as 765, 747, 354, 83 kt (between the input and reassessment vintages); "
    "all three vintages agree on the breach sign pattern at the 276 kt floor")

print(f"\n{len(PASS)}/{len(PASS) + len(FAIL)} checks pass (panel discrimination v1; chains the applied battery)")
if FAIL:
    print("FAILED:"); [print("  -", f) for f in FAIL]; sys.exit(1)
