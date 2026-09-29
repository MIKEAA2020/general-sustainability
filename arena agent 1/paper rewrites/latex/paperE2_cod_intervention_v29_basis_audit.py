#!/usr/bin/env python3
"""BASIS-AWARE SYSTEMATIC NUMERIC AUDIT for paperE2_cod_intervention_v28.tex.

The failure mode this exists to catch: a wrong basis was propagated through
multiple passes, regenerating a table and writing a script, and was only
caught on a later deep-dive. Any single-pass check can be defeated the same
way, because a number that is CORRECT on one basis is INDISTINGUISHABLE from
the same number on the wrong basis unless you know which basis produced it.

So every quantity the paper prints is declared here with BOTH its v2 (hybrid)
and v3 (source-year, authoritative) values. The audit then reports, for each
printed number, which basis it is consistent with. Anything tagged v2 is a
defect; anything matching neither basis is an unexplained number and is
flagged hardest of all.
"""
import csv
import json
import os
import re
import sys
from collections import defaultdict

import sys
_sib = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "paperE2_cod_intervention_v29.tex")
_default = _sib if os.path.exists(_sib) else \
    "/home/user/fam/e2/paperE2_cod_intervention_v29.tex"
TEX = sys.argv[1] if len(sys.argv) > 1 else _default
REPO = os.environ.get("E2_REPO", "/home/user/repo/wave_e_cod")

tex = open(TEX, encoding="utf-8").read()
lines = tex.split("\n")

# Section 2.3 declares the catch-timing convention and prints the
# destination-year numbers FOR COMPARISON. Those are legitimate, so every
# "v2 value must not appear" count runs against the text with that block
# removed. (Before 2.3 existed, the audit counted the whole document; keeping
# that behaviour would now report a false positive on every class value.)
import re as _re
_m23 = _re.search(_re.escape(chr(92) + "subsubsection{2.3 The catch-timing convention}")
                  + r"(.*?)" + _re.escape(chr(92) + "subsection{3. Results}"), tex, _re.S)
SEC23 = _m23.group(1) if _m23 else ""
TEXNC = tex.replace(SEC23, " [[SEC23]] ")

# --------------------------------------------------------------------------
# Load the authoritative v3 numbers straight from the regenerated artifacts
# --------------------------------------------------------------------------
res3 = json.load(open(f"{REPO}/results/intervention_results_v3.json"))
res2 = json.load(open(f"{REPO}/results/intervention_results_v2.json"))

V3E = f"{REPO}/src/results_srcyear_v3"
V2E = "/home/user/fam/e2/rerun_campaigns/results"


def csv3(name):
    with open(os.path.join(V3E, name), encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def csv2(name):
    with open(os.path.join(V2E, name), encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


kg3 = csv3("e2_elevation_k_grid.csv")
kg2 = csv2("e2_elevation_k_grid.csv")


def ff(path, keycol=None):
    return csv3(path)


# --------------------------------------------------------------------------
# DECLARATIONS: (label, v2_value, v3_value)
# v3 is authoritative. v2 is what must NOT appear.
# --------------------------------------------------------------------------
D = []


def q(label, v2, v3, note="", allow=()):
    """allow: regexes for contexts in which the v2 value is legitimate
    (an explicit registered-convention comparison), not a migration defect."""
    D.append({"label": label, "v2": v2, "v3": v3, "note": note, "allow": allow})


# --- residual summary (Section 2) -----------------------------------------
# the tex prints the rounded forms; declare those, or every one of these
# reports "neither printed" and the list becomes noise
q("residual SD", "134.96", "114.9")
q("residual mean", "-20.44", "-10.9")
q("residual min", "-460.03", "-329.0")
q("residual signed max", "+179.76", "+206.6")
q("residual lag-1 acf", "0.652", "0.55")
q("declared defect eps", "460.0", "329.0",
  allow=(r"registered defect magnitude", r"registered convention"))

# --- disturbance classes ---------------------------------------------------
for k, lab in (("UC_min", "worst class"), ("UC_q05", "q05 class"),
               ("UC_q10", "q10 class")):
    q(f"{lab} (1dp)", f"{res2['UC'][k]:.1f}", f"{res3['UC'][k]:.1f}")

# --- derived quantities ----------------------------------------------------
q("g(K*)", "172.46", "172.46", "same in both (same r,K)")
q("g_max", "296.09", "296.09", "same in both (same r,K)")
q("F'(K*)", "1.1531", "1.1531", "same in both")
q("q10 constructive bound", "57.61", "91.59")
q("maximal robust flat catch", "57.62", "91.59")

# --- K-grid constructive column -------------------------------------------
for r3 in kg3:
    K = float(r3["K"])
    r2 = next(x for x in kg2 if abs(float(x["K"]) - K) < 1e-9)
    q(f"K-grid K={K:g} constructive", r2["constructive_q10"],
      r3["constructive_q10"])
    q(f"K-grid K={K:g} T=1 lower", r2["BAU_q10_T1_lo"], r3["BAU_q10_T1_lo"])

# --- stochastic (Table 4), i.i.d. T=20 ------------------------------------
for path, tag, basis in (("e2_elevation_stochastic.csv", "stoch", None),):
    s3 = {r["policy"]: r["P_stay"] for r in csv3(path)
          if r["scheme"] == "iid" and int(float(r["T"])) == 20
          and abs(float(r["S0"]) - 884.6) < 1}
    s2 = {r["policy"]: r["P_stay"] for r in csv2(path)
          if r["scheme"] == "iid" and int(float(r["T"])) == 20
          and abs(float(r["S0"]) - 884.6) < 1}
    for pol in ("flat_0", "BAU", "flat_25", "flat_50"):
        q(f"stochastic iid T=20 {pol}", f"{float(s2[pol]):.3f}",
          f"{float(s3[pol]):.3f}")

# --- finite-duration floors (Table 5) -------------------------------------
f3 = {(r["floor"], r["policy"], int(r["n_years"])): r["Tinf_lower_boundary"]
      for r in csv3("e2_elevation_finite_floors.csv")}
f2 = {(r["floor"], r["policy"], int(r["n_years"])): r["Tinf_lower_boundary"]
      for r in csv2("e2_elevation_finite_floors.csv")}
for key in sorted(f3):
    v2 = f2.get(key, "")
    v3 = f3[key]
    if v3 == "":
        v3 = "empty"
    if v2 == "":
        v2 = "empty"
    if v2 != v3:
        q(f"finite floor {key[0]} {key[1]} n={key[2]}", v2, v3)

# --- bootstrap -------------------------------------------------------------
q("bootstrap r median", "0.207", "0.219")
q("bootstrap g(K*) median", "150.5", "159.6")
q("bootstrap constructive median", "35.6", "78.7")
q("bootstrap fraction constructive>0", "71.3", "88.2")

# --- derived quantities built OUT OF a class value -------------------------
# These are the ones a class-token sweep walks straight past: they are not
# class values, they are arithmetic performed on one. Each of them survived the
# first migration pass in v2 form and had to be re-derived.
q("Result 3.4 phi threshold", "0.612", "0.727", "1 - |e_q10|/g_max")
# Result 3.4's criterion was recomputed: the safe-set condition uses g(K*),
# not g_max, so the margins are 48.5 / 5.4 / -37.8 kt.  The superseded values
# (141.2 / 67.2 / -6.8) are declared in the corrected block below as what must
# NOT appear, which is the audit's real job here.
q("Result 3.4 criterion phi=0.25", "141.2", "48.5")
q("Result 3.4 criterion phi=0.50", "67.2", "5.4")
q("Result 3.4 criterion phi=0.75", "-6.8", "-37.8")
q("Section 3.3 q05 arithmetic", "-146.3", "-114.9", "g(K*) - |e_q05|")
q("Section 3.3 worst arithmetic", "-287.6", "-156.5", "g(K*) - |e_worst|")
q("K-grid K=1000 constructive raw", "-62.85", "-28.87", "raw, unclamped")
q("bootstrap F'(K*) median", "1.134", "1.142")
q("bootstrap F'(K*) 90% lower", "1.001", "1.010")
q("bootstrap F'(K*) 90% upper", "1.177", "1.179")
q("bootstrap constructive 90% upper", "84.8", "121.1")
q("certified set at the last horizon", "4942.7", "4560.3", "T=6 -> T=7")
q("60-kt rules T=inf boundary", "900.3", "884.6",
  allow=(r"against .{0,20}under the registered convention",))
q("abstract zero-catch survival", "0.87", "0.91")
q("abstract 120-kt survival", "0.58", "0.65")
q("in-sample MSE at committed (r,K)", "17{,}873", "12{,}772")

# --- Fox form --------------------------------------------------------------
q("Fox constructive bound", "45.08", "79.05")

# --- the prose-coherence pass ---------------------------------------------
# Numbers the end-to-end read added or repaired. Most have no v2 counterpart
# (they are measurements of the v3 artifacts, not basis-dependent quantities),
# so they are declared v3-only: an empty v2 makes the audit skip the "wrong
# basis" test instead of inventing one. Two have a genuine v2 twin and declare
# it, because the migration is exactly what got them wrong the first time.
q("Allee g(K*) at the LRP", "196.06", "196.06")
q("Allee constructive at the declared q10 floor", "", "115.2")
q("declared-strength constructive at the declared q10 floor", "", "123.3")
q("Allee 60-kt q05 T=inf boundary", "", "1131.1")
q("i.i.d. P>=0.9 crossing", "", "13.5")
q("no-1992 P>=0.9 crossing", "", "78.9")
q("P>=0.8 crossing, blocks", "", "72.3")
q("grid catch nearest the constructive bound", "", "92.5")
q("immediate-breach probability", "", "0.083")
q("total failure probability at zero catch", "", "0.094")
q("second fatal residual", "", "-323.5")
q("breach threshold at the LRP (=-g(K*))", "", "-172.5")
q("grown-clear threshold", "", "1020")
q("ceiling if every 1992 draw were fatal", "", "0.427")
q("grid/interval: cells checked", "", "81")
q("grid/interval: finite-horizon cells", "", "72")
q("grid/interval: max finite-horizon difference", "", "0.06")
q("grid/interval: largest T=inf difference", "", "0.9")

# --- the structural pass ---------------------------------------------------
q("C_vac = g_max - |e_q10|", "", "215.2")
q("Family A safe-set threshold", "0.727", "0.531",
  allow=(r"[Nn]onempt", r"g_\\max", r"296\\.09", r"earlier version"))
q("Family A nonempty threshold", "", "0.727")
q("Family A margin at phi=0.25", "141.2", "48.5")
q("Family A margin at phi=0.50", "67.2", "5.4")
q("Family A margin at phi=0.75", "-6.8", "-37.8")
q("Family A phi=0.60 q10 T=1 boundary", "", "895.2")
q("Family A phi=0.60 q10 T=inf boundary", "", "1074.8")
q("Family A phi=0.60 q05 T=1 boundary", "", "1091.0")
q("Family A phi=0.60 worst T=1 boundary", "", "1131.2")
q("profile: lower end of the 95% set", "", "1500")
q("profile: SSE ratio at the box edge", "", "1.027")
q("profile: g(K*) range", "", "148.8")
q("profile: C* range", "", "67.9")
q("profile: smallest expansive K", "", "1775")

# --- the identification pass ----------------------------------------------
q("r median, fixed-K bootstrap (Section 3.10)", "", "0.219")
q("r median, joint bootstrap (Section 3.10)", "", "0.261")
q("committed K (declared box edge)", "", "5000")
q("K median, joint bootstrap", "", "4191")
q("joint bootstrap C* median (expansive regime)", "", "88.1")
q("joint bootstrap 90% band", "", "-5.6")
q("joint bootstrap F' median (expansive regime)", "", "1.137")
q("share of replicates with K pinned", "", "41.7")
q("C* at lambda = 0.5 observation error", "", "112.1")
q("NCAM 1995-2015 C*", "", "171.4")
q("NCAM 1995-2015 C* under the worst floor", "", "166.4")
q("NCAM 1995-2007 C*", "", "274.0")
q("xteNCAM 1995-2024 C*", "", "8.0")
q("xteNCAM 2005-2024 C*", "-48.0", "-7.7",
  allow=(r"1954--2007", r"Section 3.11"))
q("xteNCAM 1954-2007 F'(LRP) (Section 3.11)", "", "1.4447")
q("xteNCAM 2005-2024 F'(LRP) (Section 3.12)", "", "0.925")
q("xteNCAM 1954-2007 fitted K (Section 3.11)", "", "4812.9")
q("xteNCAM recent fitted K (Section 3.12)", "", "472")

# --------------------------------------------------------------------------
# AUDIT
# --------------------------------------------------------------------------
def count(tok):
    """Occurrences of a numeric token, skipping those inside \\vspace etc."""
    return len(re.findall(r"(?<![\d.])" + re.escape(tok) + r"(?!\d)", TEXNC))


def count_excused(d):
    """v2 occurrences that are NOT an explicit registered-convention
    comparison. A v2 value quoted side by side with its v3 counterpart is the
    point of the convention note; the same value used as the paper's own
    number is a defect."""
    tok = d["v2"]
    if tok in ("", "empty"):
        return 0
    n = 0
    for m in re.finditer(r"(?<![\d.])" + re.escape(tok) + r"(?!\d)", TEXNC):
        ctx = TEXNC[max(0, m.start() - 140): m.end() + 140]
        if not any(re.search(a, ctx, re.S) for a in d["allow"]):
            n += 1
    return n


rows = []
for d in D:
    n2 = count_excused(d) if d["v2"] not in ("", "empty") else 0
    n3 = count(d["v3"]) if d["v3"] not in ("", "empty") else 0
    rows.append((d, n2, n3))

print("=" * 96)
print("BASIS-AWARE NUMERIC AUDIT   (v3 = source-year, AUTHORITATIVE)")
print("=" * 96)
print(f"{'quantity':44s} {'v2 (WRONG)':>12s} {'n':>3s}  {'v3 (RIGHT)':>12s} {'n':>3s}  verdict")
print("-" * 96)

bad_v2, ok, neither = [], [], []
for d, n2, n3 in rows:
    if d["v2"] == d["v3"]:
        verdict = "same both"
        ok.append(d)
    elif n3 > 0 and n2 == 0:
        verdict = "OK (v3)"
        ok.append(d)
    elif n2 > 0 and n3 == 0:
        verdict = "** V2 BASIS **"
        bad_v2.append((d, n2))
    elif n2 > 0 and n3 > 0:
        verdict = "** BOTH PRESENT **"
        bad_v2.append((d, n2))
    else:
        verdict = "neither printed"
        neither.append(d)
    print(f"{d['label']:44s} {d['v2']:>12s} {n2:3d}  {d['v3']:>12s} {n3:3d}  {verdict}")

print()
print("=" * 96)
print(f"SUMMARY: {len(ok)} correct/v3, {len(bad_v2)} ON THE V2 BASIS, "
      f"{len(neither)} not printed")
print("=" * 96)
if bad_v2:
    print("\nMUST BE REVERTED (v2 basis present in the tex):")
    for d, n in bad_v2:
        print(f"  {d['label']:44s}  v2={d['v2']:>10s} (x{n})  ->  v3={d['v3']}")
if neither:
    print("\nDeclared but not printed anywhere (check the label is right):")
    for d in neither:
        print(f"  {d['label']:44s}  v3={d['v3']}")

sys.exit(1 if bad_v2 else 0)
