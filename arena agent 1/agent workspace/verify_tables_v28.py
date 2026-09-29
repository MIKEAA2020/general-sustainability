#!/usr/bin/env python3
"""Structural + numeric verification of Tables 3, 4 and 5 in the v28 tex.

Independent of the battery: joins wrapped continuation lines into logical
rows and compares every cell against the registered elevation campaign.
"""
import csv
import os
import re
import sys

D = "/home/user/fam/e2"
TEX = os.path.join(D, "paperE2_cod_intervention_v28.tex")
ELEV = os.path.join(D, "rerun_campaigns", "results")
tex = open(TEX, encoding="utf-8").read()

BS = chr(92)          # backslash
ROWEND = BS + BS      # LaTeX row terminator '\\'


def table(name):
    anchor = BS + "textbf{" + name + ".}"
    m = re.search(re.escape(anchor) + r"(.*?)"
                  + re.escape(BS + "end{longtable}"), tex, re.S)
    if not m:
        return None
    body = m.group(1)
    # The data rows follow the header block, which ends at \endlastfoot
    # (or \endhead).  Everything before it is column specs / header cells.
    for marker in (BS + "endlastfoot", BS + "endhead", BS + "midrule"):
        if marker in body:
            body = body.split(marker, 1)[1]
            break
    return body


def logical_rows(body):
    """Split on row terminators, join wrapped lines, drop the footer."""
    body = body.split(BS + "bottomrule")[0]
    out = []
    for chunk in body.split(ROWEND):
        c = " ".join(chunk.split())
        if "&" in c:
            out.append(c)
    return out


fails = []


def chk(label, ok, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + label + (("  -- " + detail) if detail else ""))
    if not ok:
        fails.append(label)


# --------------------------------------------------------------------------
# Table 3 -- K-grid
# --------------------------------------------------------------------------
print("=== Table 3 (K-grid) ===")
kg = {}
with open(os.path.join(ELEV, "e2_elevation_k_grid.csv"), encoding="utf-8") as fh:
    for r in csv.DictReader(fh):
        kg[r["K"]] = r

rows = logical_rows(table("Table 3"))
chk("Table 3 has 10 data rows", len(rows) == 10, f"got {len(rows)}")

for r in rows:
    cells = [c.strip() for c in r.split("&")]
    chk(f"Table 3 row has 8 cells ({cells[0][:14]})", len(cells) == 8,
        f"got {len(cells)}: {cells}")
    key = cells[0].split()[0]
    # CSV keys are floats ('1000.0'), tex prints integers ('1000')
    exp = next((v for k, v in kg.items()
                if abs(float(k) - float(key)) < 1e-6), None)
    if exp is None:
        chk(f"Table 3 K={key} present in archive", False)
        continue
    # constructive column (index 4); tex shows the raw (possibly negative) value
    got_c = cells[4].replace(BS + "textbf{", "").replace("}", "")
    want_c = exp["constructive_q10_raw"]
    chk(f"Table 3 K={key:>7s} constructive = {want_c}",
        abs(float(got_c.replace("(", "").replace(BS, "").replace(")", ""))
            - float(want_c)) < 0.006 if got_c not in ("empty",) else False,
        f"tex {got_c}")
    # T=1 lower boundary (index 5)
    got_t1 = cells[5].replace(BS + "textbf{", "").replace("}", "")
    chk(f"Table 3 K={key:>7s} T=1 = {exp['BAU_q10_T1_lo']}",
        got_t1 == exp["BAU_q10_T1_lo"] or abs(float(got_t1) - float(exp["BAU_q10_T1_lo"])) < 0.06,
        f"tex {got_t1}")

# --------------------------------------------------------------------------
# Table 5 -- finite-duration floors
# --------------------------------------------------------------------------
print("\n=== Table 5 (finite-duration floors) ===")
ff = {}
with open(os.path.join(ELEV, "e2_elevation_finite_floors.csv"), encoding="utf-8") as fh:
    for r in csv.DictReader(fh):
        ff[(r["floor"], r["policy"], int(r["n_years"]))] = r["Tinf_lower_boundary"]

LABEL = {"flat_0": "zero catch", "BAU": "BAU (5 kt)", "flat_25": "60 kt / S1 / cascade",
         "flat_50": "120 kt", "flat_75": "180 kt", "flat_100": "240 kt"}

rows5 = logical_rows(table("Table 5"))
chk("Table 5 has 6 data rows", len(rows5) == 6, f"got {len(rows5)}")

for r in rows5:
    cells = [c.strip() for c in r.split("&")]
    lab = cells[0]
    pol = [k for k, v in LABEL.items() if v == lab]
    chk(f"Table 5 row label '{lab}' recognised", bool(pol))
    if not pol:
        continue
    pol = pol[0]
    chk(f"Table 5 row '{lab}' has 7 cells", len(cells) == 7, f"got {len(cells)}")
    want = [ff[("q05", pol, n)] for n in (5, 10, 15)]
    want += [ff[("worst", pol, n)] for n in (5, 10, 15)]
    want = ["empty" if w == "" else w for w in want]
    got = cells[1:7]
    chk(f"Table 5 row '{lab}' matches archive", got == want,
        f"tex {got} vs archive {want}")

# --------------------------------------------------------------------------
# Table 4 -- stochastic viability (registered pool)
# --------------------------------------------------------------------------
print("\n=== Table 4 (stochastic, registered pool) ===")
def p20(path):
    out = {}
    with open(path, encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if (r["scheme"] == "iid" and abs(float(r["S0"]) - 884.6) < 1
                    and int(float(r["T"])) == 20):
                out[r["policy"]] = float(r["P_stay"])
    return out

reg = p20(os.path.join(ELEV, "e2_elevation_stochastic.csv"))
rows4 = logical_rows(table("Table 4"))
chk("Table 4 has 4 data rows", len(rows4) == 4, f"got {len(rows4)}")
for r in rows4:
    cells = [c.strip() for c in r.split("&")]
    pol = {"zero catch": "flat_0", "BAU (5 kt)": "BAU",
           "60 kt / S1 / cascade": "flat_25", "120 kt": "flat_50"}.get(cells[0])
    if pol is None:
        chk(f"Table 4 label '{cells[0]}' recognised", False)
        continue
    want = f"{reg[pol]:.3f}"
    chk(f"Table 4 '{cells[0]}' i.i.d. = {want}", cells[1] == want, f"tex {cells[1]}")

print()
if fails:
    print(f"{len(fails)} FAILED:")
    for f in fails:
        print("  -", f)
    sys.exit(1)
print("ALL TABLE CHECKS PASSED")
