#!/usr/bin/env python3
"""Build paperE2_cod_intervention_v29.tex from v27 on the v3 (source-year) basis.

Base choice: v27, not v28. v28's 372 changed lines are overwhelmingly
basis-forced. v27 already carries the source-year kernels (2219.6, 2070.9),
all 36 cells of Table 5, Table 4's i.i.d. column, the source-year residual
SD/mean/max/acf, and the correct vacuity claim ("reduces the vacuous family
from two classes to one"). v28 replaced those with hybrid values.

Fixed here — what v27 still had on the wrong basis:
  * disturbance class LABELS (-460.0/-318.8/-114.9 -> -329.0/-287.4/-80.9);
  * declared defect eps (460.0 -> 329.0);
  * Table 3 K-grid constructive column;
  * Table 4 block/no-1992/1500-kt columns;
  * constructive bound and maximal robust catch (57.6 -> 91.59);
  * the stochastic-constructive readings at C and the P>=0.9 / P>=0.8 crossings;
  * the parametric bootstrap;
  * the certified horizon / certified set (eps changes -> T=7, [4560.3, 10^4]).

All replacement values are read from the regenerated v3 artifacts.
"""
import ast
import csv
import json
import os
import re
from pathlib import Path

V27 = "/home/user/fam/e2/paperE2_cod_intervention_v27.tex"
OUT = "/home/user/fam/e2/paperE2_cod_intervention_v29.tex"
REPO = "/home/user/repo/wave_e_cod"
V3E = f"{REPO}/src/results_srcyear_v3"

res3 = json.load(open(f"{REPO}/results/intervention_results_v3.json"))


def csv3(name):
    with open(os.path.join(V3E, name), encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


tex = Path(V27).read_text(encoding="utf-8")
n0 = len(tex)
EDITS = []


def E(label, old, new, expect=1):
    EDITS.append((label, old, new, expect))


# ===========================================================================
# 1. DISTURBANCE CLASSES  (hybrid -> source-year)
#    Guard with lookarounds so 1657.6 / 2193.4 etc. are never touched.
# ===========================================================================
for old, new, cnt in (("-460.0", "-329.0", 9), ("-318.8", "-287.4", 6),
                      ("-114.9", "-80.9", 4)):
    E(f"class {old}", rf"(?<![\d.]){re.escape(old)}(?!\d)", new, cnt)
E("defect eps", r"\varepsilon = 460.0", r"\varepsilon = 329.0", 3)

# ===========================================================================
# 2. CONSTRUCTIVE BOUND / MAXIMAL ROBUST CATCH   57.6 -> 91.59
#    (the literal '\(57.6\)' form; '1657.6' is not matched)
# ===========================================================================
E("constructive \(57.6\)", r"\(57.6\)", r"\(91.59\)", 11)
E("constructive bold 57.6 kt", r"\textbf{57.6 kt}", r"\textbf{91.59 kt}", 1)
E("constructive arithmetic",
  r"\(g(K^*) - |e_{q10}| = 172.46 - 114.85 = 57.61\)",
  r"\(g(K^*) - |e_{q10}| = 172.46 - 80.87 = 91.59\)", 1)
E("summary bound at 57.6 kt", r"bound at 57.6 kt", r"bound at 91.59 kt", 1)

# ===========================================================================
# 3. TABLE 3 -- K-grid constructive column (source-year floor -80.87)
# ===========================================================================
T3 = [
    ("1000 & 0.5094 & 127.4 & 0.608 & \\(-32.2\\) & 943.2",
     "1000 & 0.5094 & 127.4 & 0.608 & \\(-28.87\\) & 943.2"),
    ("1200 & 0.5248 & 157.4 & 0.751 & 36.0 & 884.6",
     "1200 & 0.5248 & 157.4 & 0.751 & 41.14 & 884.6"),
    ("1500 & 0.4099 & 153.7 & 0.926 & 62.9 & 884.6",
     "1500 & 0.4099 & 153.7 & 0.926 & 67.9 & 884.6"),
    ("1769.2 (\\(=2K^*\\)) & 0.3559 & 157.4 & 1.000 & 72.7 & 884.6",
     "1769.2 (\\(=2K^*\\)) & 0.3559 & 157.4 & 1.000 & 76.55 & 884.6"),
    ("2000 & 0.3273 & 163.6 & 1.038 & 77.6 & 884.6",
     "2000 & 0.3273 & 163.6 & 1.038 & 80.6 & 884.6"),
    ("2500 & 0.2908 & 181.7 & 1.085 & 83.4 & 884.6",
     "2500 & 0.2908 & 181.7 & 1.085 & 85.33 & 884.6"),
    ("3000 & 0.2704 & 202.8 & 1.111 & 86.6 & 884.6",
     "3000 & 0.2704 & 202.8 & 1.111 & 87.79 & 884.6"),
    ("4000 & 0.2485 & 248.5 & 1.139 & 89.9 & 884.6",
     "4000 & 0.2485 & 248.5 & 1.139 & 90.31 & 884.6"),
    ("7000 (out of box) & 0.2248 & 393.5 & 1.168 & 93.3 & 884.6",
     "7000 (out of box) & 0.2248 & 393.5 & 1.168 & 92.89 & 884.6"),
]
for i, (o, n) in enumerate(T3):
    E(f"T3 row {i+1}", o, n, 1)
# Result 3.7(i) endpoint of the constructive column
E("T3 endpoint 57.6", r"to \(91.59\) kt at", r"to \(91.59\) kt at", 1)

# ===========================================================================
# 4. TABLE 4 -- stochastic viability, regenerated
# ===========================================================================
st = csv3("e2_elevation_stochastic.csv")
for pol, lab in (("flat_0", "zero catch"), ("BAU", "BAU (5 kt)"),
                 ("flat_25", "60 kt / S1 / cascade"), ("flat_50", "120 kt")):
    cells = []
    for scheme, S0 in (("iid", 884.6), ("block4", 884.6),
                       ("iid_no1992", 884.6), ("iid", 1500.0)):
        m = [r for r in st if r["policy"] == pol and r["scheme"] == scheme
             and abs(float(r["S0"]) - S0) < 1 and int(float(r["T"])) == 20]
        cells.append(f"{float(m[0]['P_stay']):.3f}")
    new = f"{lab} & " + " & ".join(cells) + r" \\"
    m = re.search(r"^" + re.escape(lab) + r" & .*?\\\\$", tex, re.M)
    if m:
        E(f"T4 row {lab}", re.escape(m.group(0)), new.replace("\\", "\\\\"), 1)

# ===========================================================================
# 5. STOCHASTIC-CONSTRUCTIVE READINGS (Section 3.8)
# ===========================================================================
E("stoch at C", r"""At \(C = 91.59\) kt the 20-year survival probability from the LRP is
\(0.77\) under i.i.d. draws, \(0.79\) under blocks, and \(0.88\) when
the 1992 residual is removed.""",
  r"""At \(C = 91.59\) kt the 20-year survival probability from the LRP is
\(0.74\) under i.i.d. draws, \(0.73\) under blocks, and \(0.84\) when
the 1992 residual is removed.""", 1)
E("stoch caps", r"capping i.i.d. survival\nat \(0.868\) and block survival at \(0.808\)",
  r"capping i.i.d. survival\nat \(0.906\) and block survival at \(0.849\)", 1)
E("stoch P>=0.9 crossing", r"where the crossing is \(48.6\) kt",
  r"where the crossing is \(78.9\) kt", 1)
E("stoch P>=0.8 crossings",
  r"crossings are \(48.4\) kt (i.i.d.),\n\(38.9\) kt (blocks), and \(95.1\) kt (no-1992).",
  r"crossings are \(81.2\) kt (i.i.d.),\n\(72.3\) kt (blocks), and \(105.2\) kt (no-1992).", 1)
E("stoch at bound again",
  r"falls to \(0.77\) under i.i.d. draws (\(0.79\) under\nblocks, \(0.88\) without the 1992 draw)",
  r"falls to \(0.74\) under i.i.d. draws (\(0.73\) under\nblocks, \(0.84\) without the 1992 draw)", 1)
E("stoch range", r"removals to \(0.58\) at \(120\) kt\)",
  r"removals to \(0.65\) at \(120\) kt\)", 1)
E("stoch range start", r"(\(0.87\) at zero-to-moratorium removals to \(0.65\)",
  r"(\(0.91\) at zero-to-moratorium removals to \(0.65\)", 1)

# ===========================================================================
# 6. PARAMETRIC BOOTSTRAP
# ===========================================================================
E("boot r median", r"\(0.207\)", r"\(0.219\)", 1)
E("boot r interval", r"\([0.001, 0.274]\)", r"\([0.016, 0.277]\)", 1)
E("boot gK median", r"\(150.5\)", r"\(159.6\)", 1)
E("boot gK interval", r"\([0.7, 199.6]\)", r"\([11.6, 201.9]\)", 1)
E("boot cons median", r"\(35.6\)", r"\(78.7\)", 1)
E("boot cons interval", r"\([0.0, 84.8]\)", r"\([0.0, 121.1]\)", 1)
E("boot fraction", r"\(71.3\%\)", r"\(88.2\%\)", 1)

# ===========================================================================
# 7. CERTIFIED LAYER -- recomputed with eps = 328.97 (v3 declared defect)
#    a_max = 1.1531, K* = 884.6, K = 5000
#      K*+r_T: T=6 -> 3787.0   T=7 -> 4560.3   T=8 -> 5452.0 (> K)
#    => certified horizon T = 7, empty from T = 8
# ===========================================================================
E("certified set T=6", r"\([4942.7, 10^4]\)", r"\([3787.0, 10^4]\)", 2)
E("certified horizon 6->7", r"certified horizon is therefore \(T = 6\)",
  r"certified horizon is therefore \(T = 7\)", 1)
E("certified T=7 threshold", r"at \(T = 7\) the shifted threshold is \(6023.9\)",
  r"at \(T = 7\) the shifted threshold is \(4560.3\)", 1)
E("certified horizon summary", r"lengthens the certified horizon (to \(T=6\))",
  r"lengthens the certified horizon (to \(T=7\))", 1)

# ===========================================================================
ast.parse(open(__file__, encoding="utf-8").read())

applied, missing, ambig = [], [], []
for label, old, new, expect in EDITS:
    n = len(re.findall(old, tex)) if old.startswith("(?") else tex.count(old)
    if n == 0:
        missing.append(label)
        continue
    if n != expect:
        ambig.append(f"{label} (found {n}, expected {expect})")
        continue
    tex = re.sub(old, new.replace("\\\\", "\\"), tex) if old.startswith("(?") \
        else tex.replace(old, new)
    applied.append(label)

Path(OUT).write_text(tex, encoding="utf-8")
print(f"wrote {OUT}   ({n0} -> {len(tex)} chars)")
print(f"  applied {len(applied)}   missing {len(missing)}   ambiguous {len(ambig)}")
if missing:
    print("\n  MISSING:")
    for m in missing:
        print("   -", m)
if ambig:
    print("\n  AMBIGUOUS (unchanged):")
    for a in ambig:
        print("   -", a)
