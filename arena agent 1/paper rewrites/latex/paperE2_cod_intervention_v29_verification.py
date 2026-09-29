#!/usr/bin/env python3
"""Verification battery for paperE2_cod_intervention_v29.tex -- v3 (source-year).

The 123-check v28 battery is deliberately NOT used: it pins the hybrid basis
and would validate the wrong thing. This one reads the regenerated v3
artifacts and fails on any v2/hybrid value.

  repo/wave_e_cod/results/intervention_results_v3.json
  repo/wave_e_cod/results/intervention_boundaries_v3.csv
  repo/wave_e_cod/results/e2_families_v3.csv
  repo/wave_e_cod/src/results_srcyear_v3/e2_elevation_*.csv
  repo/wave_e_cod/src/results_forms_v3/{e2_allee_rows_v3,e2_fox_*_v3}.csv
  repo/arena agent 1/other documents/rerun_campaigns/results/e2_xteNCAM_*.csv

Design rules this battery is built on (all learned the hard way):

  * A presence check is defeated by repetition across scopes. Values that
    recur (91.59, 884.6, 2219.6) get SCOPED checks plus NEAR-MISS guards
    that assert adjacent values are absent.
  * A context-free token can be legitimately ambiguous. Section 2.3 now
    deliberately prints the destination-year classes for comparison, so all
    "no v2 value survives" checks run against the text with that block
    removed (TEXNC) rather than against the whole document.
  * Row comparisons collapse whitespace and strip \\textbf{} and the row
    terminator, because longtable rows wrap in the source.
  * Where a number is cheap to recompute from the artifacts (the certified
    ladder and its horizons), recompute it; do not just grep for it.
  * Every check here has been sabotage-tested: flipping any single number
    the battery is meant to protect must turn at least one check red.
"""
import csv
import importlib.util
import json
import math
import os
import re
import sys

import numpy as np

# An optional argv[1] overrides the tex under test (the sabotage harness needs
# to point the battery at a mutated copy). With no argument the battery looks
# for the tex NEXT TO ITSELF first -- that is where it will sit once archived
# alongside the paper, as the project's other *_verification.py scripts do --
# and falls back to the workspace path.
TEX = sys.argv[1] if len(sys.argv) > 1 else None
if TEX is None:
    _sib = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "paperE2_cod_intervention_v29.tex")
    TEX = _sib if os.path.exists(_sib) else \
        "/home/user/fam/e2/paperE2_cod_intervention_v29.tex"
REPO = "/home/user/repo/wave_e_cod"
V3E = REPO + "/src/results_srcyear_v3"
V3F = REPO + "/src/results_forms_v3"   # campaigns + outputs, archived with the runner
XTE = "/home/user/repo/arena agent 1/other documents/rerun_campaigns/results"
BS = chr(92)

tex = open(TEX, encoding="utf-8").read()
res3 = json.load(open(REPO + "/results/intervention_results_v3.json"))
res2 = json.load(open(REPO + "/results/intervention_results_v2.json"))

PASS, FAIL = [], []


def chk(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(("PASS  " if ok else "FAIL  ") + name + (("  -- " + detail) if detail else ""))


def has(tok, s=None):
    return len(re.findall(r"(?<![\d.])" + re.escape(tok) + r"(?!\d)",
                          tex if s is None else s))


def csv3(name):
    with open(os.path.join(V3E, name), encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def csvf(name):
    with open(os.path.join(V3F, name), encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def block(num):
    """The longtable body of 'Table <num>.', normalised for row matching."""
    m = re.search(re.escape(BS + "textbf{Table " + str(num) + ".}")
                  + r"(.*?)" + re.escape(BS + "end{longtable}"), tex, re.S)
    if not m:
        return ""
    b = m.group(1)
    # strip \textbf{...} BEFORE collapsing whitespace; a naive replace of the
    # opening token leaves the closing brace behind and breaks row matching
    b = re.sub(r"\\textbf\{([^{}]*)\}", r"\1", b)
    return " ".join(b.split())


# The Section 2.3 convention block legitimately quotes destination-year
# numbers, so every "v2 value absent" check runs against the rest of the paper.
m23 = re.search(re.escape(BS + "subsubsection{2.3 The catch-timing convention}")
                + r"(.*?)" + re.escape(BS + "subsection{3. Results}"), tex, re.S)
SEC23 = m23.group(1) if m23 else ""
SEC23N = " ".join(SEC23.split())          # the source wraps mid-sentence
TEXNC = tex.replace(SEC23, " [[SEC23]] ")

# Prose phrases wrap mid-sentence in the source, so they are matched against a
# whitespace-collapsed copy; a raw substring test silently fails on the newline.
FLAT = " ".join(tex.split())

# run_ladder must be imported once and registered in sys.modules: re-importing
# it under a second name breaks @dataclass, which looks the class's module up
# in sys.modules and finds None.
_spec = importlib.util.spec_from_file_location("run_ladder", REPO + "/src/run_ladder.py")
rl = importlib.util.module_from_spec(_spec)
sys.modules["run_ladder"] = rl
_spec.loader.exec_module(rl)

# ===========================================================================
# R9 -- Section 2: residual summary, and the declared convention
# ===========================================================================
f3, f2 = res3["fit"], res2["fit"]
gmax = f3["r"] * f3["K"] / 4.0

for label, key, want in (("SD", "train_residual_sd", 114.91),
                         ("min", "train_residual_min", -328.97),
                         ("q05", "train_residual_q05", -287.36),
                         ("q10", "train_residual_q10", -80.87),
                         ("signed max", "train_residual_max", 328.97)):
    v = f3[key]
    chk("R9a v3 residual %s = %.2f reproduces" % (label, want),
        abs(abs(v) - abs(want)) < 0.01, "v3=%.4f" % v)

for form in ("114.9", "-10.9", "+206.6", "0.55", "-329.0"):
    chk("R9b Section 2 prints the source-year form %s" % form, has(form) > 0)

# 0.65 is deliberately absent from this list: it is now a legitimate rounding
# of the v3 120-kt survival probability (0.6466). The residual autocorrelation
# is checked by the scoped R9c2/R9c4 checks instead.
for bad in ("134.96", "135.0", "-20.44", "+179.8", "0.652"):
    chk("R9c no v2 residual value %s outside Section 2.3" % bad,
        has(bad, TEXNC) == 0)

# 0.65 is ambiguous: it is the v2 autocorrelation AND a rounding of the 120-kt
# survival (0.6466). Scope to the Section 2 residual sentence.
m_sec2 = re.search(r"The training-window residuals.{0,220}", tex, re.S)
sec2 = m_sec2.group(0) if m_sec2 else ""
chk("R9c2 Section 2 residual sentence does not state 0.65",
    bool(sec2) and "0.65" not in sec2)
m_38 = re.search(r"resample the 24.{0,200}", tex, re.S)
s38 = m_38.group(0) if m_38 else ""
chk("R9c3 Section 3.8 quotes the source-year autocorrelation 0.55",
    bool(s38) and "0.55" in s38)
chk("R9c4 Section 3.8 does not quote the v2 autocorrelation 0.65",
    bool(s38) and "0.65" not in s38)

for near in ("114.8", "114.7", "115.0", "-10.8", "-10.95",
             "-328.9", "-329.1", "206.5", "206.7"):
    chk("R9d no near-miss source-year value %s survives" % near, has(near) == 0)

# --- Section 2.3: the convention is declared, evidenced, and limited --------
chk("R9e Section 2.3 exists", bool(SEC23) and len(SEC23) > 1500,
    "%d chars" % len(SEC23))
for tok in ("source-year", "destination-year", "Convention (adopted)",
            "12{,}772", "17{,}873", "28.5", "0.2084",
            "17{,}713", "15{,}026", "834.9", "783.1"):
    chk("R9f Section 2.3 states %s" % tok, tok in SEC23N)
chk("R9g Section 2.3 admits the provenance gap on ssb_kt",
    "Nothing in the archived source documentation records whether" in SEC23N)
chk("R9h Section 2.3 says the convention is not adopted on provenance",
    "rather than derived from provenance" in SEC23N)
for pair in (("91.59", "57.61"), ("884.6", "900.3")):
    chk("R9i Section 2.3 reports the sensitivity %s vs %s" % pair,
        all(x in SEC23N for x in pair))
chk("R9j Section 2.3 states the vacuous-class sensitivity (one vs two)",
    "one against two" in SEC23N)
# A single-site corruption of the source-year triple inside the comparison
# sentence would otherwise hide behind the block's legitimate v2 values: R10b
# exempts Section 2.3, so the block needs its own check.
# The triples are written as \(-329.0\)/\(-287.4\)/\(-80.9\), so the LaTeX
# delimiters have to go before a substring test can see them. (An earlier
# version of this check kept the markup and failed permanently -- which made
# the sabotage harness report 47/47 on a battery that was never green.)
def numstr(s):
    return re.sub(r"[^0-9./\-]", "", s)


chk("R9j2 Section 2.3 comparison sentence is intact",
    "-329.0/-287.4/-80.9" in numstr(SEC23N)
    and "-460.0/-318.8/-114.9" in numstr(SEC23N),
    "source-year vs destination-year triples")
chk("R9j3 Section 2.3 comparison contains each triple exactly once",
    numstr(SEC23N).count("-329.0/-287.4/-80.9") == 1
    and numstr(SEC23N).count("-460.0/-318.8/-114.9") == 1)

# recompute the two MSEs the subsection quotes
def _mse(dest):
    yr, ssb, c_reg, c_ann, idx, lrp = rl.load()
    m = yr <= 2007
    S, C = ssb[m], c_ann[m]
    dS = np.diff(S)
    Cc = C[1:] if dest else C[:-1]
    pred = np.array([rl.surplus(s, f3["r"], f3["K"]) - c
                     for s, c in zip(S[:-1], Cc)])
    return float(np.mean((dS - pred) ** 2))


chk("R9k in-sample MSE source-year 12,772 recomputes",
    abs(_mse(False) - 12772.17) < 1.0, "%.1f" % _mse(False))
chk("R9l in-sample MSE destination-year 17,873 recomputes",
    abs(_mse(True) - 17873.32) < 1.0, "%.1f" % _mse(True))
chk("R9m the 28.5%% gap recomputes",
    abs(100 * (1 - _mse(False) / _mse(True)) - 28.5) < 0.2,
    "%.2f%%" % (100 * (1 - _mse(False) / _mse(True))))

# ===========================================================================
# R10 -- classes, vacuity, the restored no-dominance mechanism
# ===========================================================================
def dp1_variants(v):
    """Both 1-dp renderings of a class value. -114.85 is '-114.8' to Python and
    '-114.9' to round-half-up, and the paper uses the latter; a guard that
    checks only the Python rendering is blind to half the possible leaks."""
    return sorted({"%.1f" % v,
                   "%.1f" % (math.floor(abs(v) * 10) / 10 * (-1 if v < 0 else 1)),
                   "%.1f" % (math.ceil(abs(v) * 10) / 10 * (-1 if v < 0 else 1))})


def has_except(tok, allow):
    """Occurrences of tok in TEXNC that are NOT in an allowed context."""
    n = 0
    for m in re.finditer(r"(?<![\d.])" + re.escape(tok) + r"(?!\d)", TEXNC):
        ctx = TEXNC[max(0, m.start() - 120): m.end() + 120]
        if not any(re.search(a, ctx, re.S) for a in allow):
            n += 1
    return n


# -114.9 is ambiguous: it is the v2 q10 class (-114.85 rounded half-up) AND the
# v3 Section 3.3 arithmetic result (172.46 - 287.36 = -114.90). Only the
# arithmetic context is allowed; every other occurrence is a v2 leak.
ALLOW_CLASS = {"-114.9": (r"172\.46 - 287\.36",)}
for k, lab in (("UC_min", "worst"), ("UC_q05", "q05"), ("UC_q10", "q10")):
    v3, v2 = res3["UC"][k], res2["UC"][k]
    chk("R10a %s class %.1f printed" % (lab, v3), has("%.1f" % v3) > 0)
    for form in dp1_variants(v2):
        allow = ALLOW_CLASS.get(form, ())
        n = has_except(form, allow) if allow else has(form, TEXNC)
        chk("R10b no v2 %s class %s outside Section 2.3" % (lab, form), n == 0,
            "%d occurrence(s)" % n)

nvac = sum(1 for k in res3["UC"] if abs(res3["UC"][k]) > gmax)
chk("R10c vacuous classes = %d of 3 under v3 (g_max=%.2f)" % (nvac, gmax), nvac == 1)
chk("R10d q05 informative under v3 (287.36 < 296.09)",
    abs(res3["UC"]["UC_q05"]) < gmax)
chk("R10e q05 BAU T=inf kernel 2219.6 restored at 12 sites", has("2219.6") == 12)
chk("R10f q05 zero-catch 2070.9 present", has("2070.9") > 0)
chk("R10g states the vacuous family reduces from two classes to one",
    "reduces the vacuous family from two classes to one" in tex)
chk("R10h no-dominance mechanism still cites BAU's nonempty q05 kernel",
    re.search(r"BAU's kernel is nonempty.{0,40}2219\.6", tex, re.S) is not None)

# ===========================================================================
# R11 -- every table, parsed into rows and compared cell by cell
#
# Longtable rows wrap in the source, carry \textbf{} and end in \\, so string
# matching a whole row is brittle. Each table is parsed into cells and compared
# numerically, with a tolerance of one grid step (0.05 kt) where the number
# comes from the 0.05 kt grid rather than from the interval-arithmetic engine.
# ===========================================================================
def data_rows(num):
    blk = block(num)
    tail = blk.split(BS + "endlastfoot")[-1]
    out = []
    for r in tail.split(BS + BS):
        cells = [c.strip() for c in r.split("&")]
        if len(cells) >= 2:
            out.append(cells)
    return out


def norm(s):
    """Labels carry LaTeX (\(\phi\), \(s_0\), ^{ast}) and trailing notes
    ('5000 (registered)'), so compare on alphanumerics only."""
    return re.sub(r"[^0-9A-Za-z_.=,*]", "", s)


def num(c):
    c = c.replace(BS, "").replace("{", "").replace("}", "")
    c = c.replace("ensuremath", "").replace("(", "").replace(")", "")
    try:
        return float(c)
    except ValueError:
        return None


def cmp_row(got, lab, cells, tol=0.051):
    """tol is a scalar or a per-cell list (see Table 3, where r is printed to
    4 dp and g_max to 1 dp, so one tolerance cannot serve both columns)."""
    """(ok, detail) for one parsed row against its expected cells.

    The label is matched as a PREFIX after normalisation, because table rows
    carry trailing annotations ('1769.2 (\\(=2K^*\\))', '5000 (registered)').
    A None entry in `cells` skips that column (free-text cells)."""
    if not norm(got[0]).startswith(norm(lab)):
        return False, "label mismatch: got '%s' want '%s'" % (got[0], lab)
    if len(got) - 1 != len(cells):
        return False, "%d cells, expected %d" % (len(got) - 1, len(cells))
    for i, want in enumerate(cells):
        if want is None:
            continue
        t_i = tol[i] if isinstance(tol, (list, tuple)) else tol
        g, w = num(got[i + 1]), (None if want in ("empty", None) else float(want))
        if g is None and w is None:
            continue
        if g is None or w is None:
            return False, "cell %d: got %s want %s" % (i, got[i + 1], want)
        if abs(g - w) > t_i:
            return False, "cell %d: got %s want %s" % (i, got[i + 1], want)
    return True, ""


KER = res3["kernels"]
FAM = {(r["policy"], r["class"], r["T"]): r["boundary"]
       for r in csv.DictReader(open(REPO + "/results/e2_families_v3.csv"))}


def kcell(pid, uc, T):
    if pid.startswith(("A_", "B_")):
        v = FAM.get((pid, uc, T), "")
    else:
        kk = KER[pid][uc][T].get("nominal")
        v = "" if not kk else float(kk[0][0])
    return "empty" if v in ("", None) else v


# --- Table 1 ---------------------------------------------------------------
ROW1 = [("BAU (5 kt)", "BAU"), ("flat 240 kt", "flat_100"),
        ("flat 180 kt", "flat_75"), ("flat 120 kt", "flat_50"),
        ("flat 60 kt", "flat_25"), ("S1 / cascade", "S1"), ("flat 0 kt", "flat_0"),
        ("Family A, phi=0.25", "A_phi0.25"), ("Family A, phi=0.50", "A_phi0.5"),
        # phi = 0.60 was added so that Table 1 exhibits the middle regime of
        # Proposition 2.3 (viable, but not from the reference point itself);
        # its cells come from the re-run families campaign.
        ("Family A, phi=0.60", "A_phi0.6"),
        ("Family A, phi=0.75", "A_phi0.75"),
        ("Family B, graded2", "B_graded2"), ("Family B, graded3", "B_graded3")]
rows = data_rows(1)
chk("R11a Table 1 parses to 13 rows", len(rows) == 13, "%d rows" % len(rows))
bad1 = []
for i, (lab, pid) in enumerate(ROW1):
    want = [kcell(pid, uc, T) for uc in ("UC_min", "UC_q05", "UC_q10")
            for T in ("1", "inf")]
    if i >= len(rows):
        bad1.append("%s: row missing" % lab)
        continue
    ok, det = cmp_row(rows[i], lab, want)
    if not ok:
        bad1.append("%s: %s" % (lab, det))
chk("R11b Table 1 reproduces the v3 kernels + families (13 rows)", not bad1,
    "; ".join(bad1) if bad1 else "all 13 rows, 78 cells match")

# --- Table 2 ---------------------------------------------------------------
alr = {r["cell"]: r["computed"] for r in csvf("e2_allee_rows_v3.csv")}
fox = {r["class_"] + "|" + r["policy"]: r for r in csvf("e2_fox_kernels_v3.csv")}


def acell(key):
    v = alr.get(key)
    return "empty" if v in (None, "") else float(v)


def fcell(cls, pol, T):
    v = fox[cls + "|" + pol][T]
    return "empty" if v in (None, "") else float(v)


rows = data_rows(2)
chk("R11c Table 2 parses to 4 rows", len(rows) == 4, "%d rows" % len(rows))
ROW2 = [
    ("Registered Schaefer",
     [kcell("BAU", "UC_q05", "1"), kcell("BAU", "UC_q05", "inf"),
      kcell("BAU", "UC_q10", "inf"), kcell("BAU", "UC_min", "inf"),
      kcell("S1", "UC_q10", "inf")]),
    ("Allee refit (s_0 = 642.3)",
     [acell("allee_s0=642.3|BAU|UC_q05|T=1"), acell("allee_s0=642.3|BAU|UC_q05|T=inf"),
      acell("allee_s0=642.3|BAU|UC_q10|T=inf"), acell("allee_s0=642.3|BAU|UC_min|T=inf"),
      acell("allee_s0=642.3|S1|UC_q10|T=inf")]),
    ("Declared s_0 = 0.5K^{\\ast} (442.3), refit",
     [acell("declared_s0=442.3|BAU|UC_q05|T=1"), acell("declared_s0=442.3|BAU|UC_q05|T=inf"),
      acell("declared_s0=442.3|BAU|UC_q10|T=inf"), acell("declared_s0=442.3|BAU|UC_min|T=inf"),
      acell("declared_s0=442.3|S1|UC_q10|T=inf")]),
    ("Fox refit (r = 0.1044, K pinned)",
     [fcell("UC_q05", "BAU", "T1"), fcell("UC_q05", "BAU", "Tinf"),
      fcell("UC_q10", "BAU", "Tinf"), fcell("UC_min", "BAU", "Tinf"),
      fcell("UC_q10", "S1", "Tinf")]),
]
bad2 = []
for i, (lab, want) in enumerate(ROW2):
    if i >= len(rows):
        bad2.append("%s: row missing" % lab)
        continue
    ok, det = cmp_row(rows[i], lab, want)
    if not ok:
        bad2.append("%s: %s" % (lab, det))
chk("R11d Table 2 reproduces the v3 form campaigns (4 rows)", not bad2,
    "; ".join(bad2) if bad2 else "all 4 rows, 20 cells match")

# --- Table 3 ---------------------------------------------------------------
rows = data_rows(3)
chk("R11e Table 3 parses to 10 rows", len(rows) == 10, "%d rows" % len(rows))
kg = csv3("e2_elevation_k_grid.csv")
bad3 = []
for i, r in enumerate(kg):
    if i >= len(rows):
        bad3.append("K=%s row missing" % r["K"])
        continue
    got = rows[i]
    disp = r["constructive_q10_raw"] if float(r["constructive_q10_raw"]) < 0 \
        else r["constructive_q10"]
    # per-column tolerance: r and F' are printed to 3-4 dp, so a single
    # 0.05 kt tolerance lets a 2% error in r through unnoticed
    ok, det = cmp_row(got, "%g" % float(r["K"]),
                      [float(r["r"]), float(r["g_max"]), float(r["Fp_Kstar"]),
                       float(disp),
                       "empty" if not r["BAU_q10_T1_lo"] else float(r["BAU_q10_T1_lo"]),
                       "empty" if not r["BAU_q10_Tinf_lo"] else float(r["BAU_q10_Tinf_lo"]),
                       None],          # the 'q05 vacuous' yes/no column
                      tol=[0.0006, 0.051, 0.0006, 0.006, 0.051, 0.051, 0.051])
    if ok:
        want_vac = "yes" if r["q05_vacuous"] == "True" else "no"
        if rows[i][-1] != want_vac:
            ok, det = False, "q05 vacuous: got %s want %s" % (rows[i][-1], want_vac)
    if not ok:
        bad3.append("K=%s: %s" % (r["K"], det))
chk("R11f Table 3 reproduces the v3 K-grid", not bad3,
    "; ".join(bad3) if bad3 else "all 10 rows match")
chk("R11g no v2 K-grid T=1 value 1009.2 survives", has("1009.2") == 0)
chk("R11g2 Section 3.7 quotes the v3 K=1000 constructive -28.87",
    has("-28.87") > 0 and has("-62.9") == 0)

# --- Table 4 ---------------------------------------------------------------
st = csv3("e2_elevation_stochastic.csv")
rows = data_rows(4)
chk("R11h Table 4 parses to 4 rows", len(rows) == 4, "%d rows" % len(rows))
bad4 = []
for i, (pol, lab) in enumerate((("flat_0", "zero catch"), ("BAU", "BAU (5 kt)"),
                                ("flat_25", "60 kt / S1 / cascade"),
                                ("flat_50", "120 kt"))):
    want = []
    for scheme, S0 in (("iid", 884.6), ("block4", 884.6),
                       ("iid_no1992", 884.6), ("iid", 1500.0)):
        mm = [x for x in st if x["policy"] == pol and x["scheme"] == scheme
              and abs(float(x["S0"]) - S0) < 1 and int(float(x["T"])) == 20]
        want.append(float(mm[0]["P_stay"]))
    if i >= len(rows):
        bad4.append("%s: row missing" % lab)
        continue
    ok, det = cmp_row(rows[i], lab, want, tol=0.0006)
    if not ok:
        bad4.append("%s: %s" % (lab, det))
chk("R11i Table 4 reproduces the v3 stochastic campaign", not bad4,
    "; ".join(bad4) if bad4 else "all 4 rows match")

# --- Table 5 ---------------------------------------------------------------
ff = {(r["floor"], r["policy"], int(r["n_years"])): r["Tinf_lower_boundary"]
      for r in csv3("e2_elevation_finite_floors.csv")}
rows = data_rows(5)
chk("R11j Table 5 parses to 6 rows", len(rows) == 6, "%d rows" % len(rows))
bad5 = []
for i, (pol, lab) in enumerate((("flat_0", "zero catch"), ("BAU", "BAU (5 kt)"),
                                ("flat_25", "60 kt / S1 / cascade"),
                                ("flat_50", "120 kt"), ("flat_75", "180 kt"),
                                ("flat_100", "240 kt"))):
    want = ["empty" if not ff[(fl, pol, n)] else float(ff[(fl, pol, n)])
            for fl in ("q05", "worst") for n in (5, 10, 15)]
    if i >= len(rows):
        bad5.append("%s: row missing" % lab)
        continue
    ok, det = cmp_row(rows[i], lab, want, tol=0.051)
    if not ok:
        bad5.append("%s: %s" % (lab, det))
chk("R11k Table 5 reproduces the v3 finite-floor campaign", not bad5,
    "; ".join(bad5) if bad5 else "all 6 rows, 36 cells match")

# --- Table 6 ---------------------------------------------------------------
rows = data_rows(6)
chk("R11l Table 6 parses to 2 rows", len(rows) == 2, "%d rows" % len(rows))
xsum = list(csv.DictReader(open(XTE + "/e2_xteNCAM_summary.csv")))[0]
xrow = {(r["class_"], r["policy"]): r
        for r in csv.DictReader(open(XTE + "/e2_xteNCAM_row.csv"))}
ok, det = cmp_row(rows[1], "xteNCAM (this row)",
                  [float(xsum["r"]), float(xsum["K"]), float(xsum["Fp_lrp"]),
                   float(xsum["constructive_own_q10"]),
                   float(xrow[("own_q10", "flat_0")]["T1"]),
                   float(xrow[("own_q10", "flat_0")]["Tinf"])], tol=0.051)
chk("R11m Table 6 reproduces the archived xteNCAM row", ok, det)
ok, det = cmp_row(rows[0], "NCAM (registered)",
                  [float(f3["r"]), None, 1.1531, 91.59, 884.6, 884.6], tol=0.02)
# got[0] is the label, so the K cell is got[2], not got[1]
if ok and "5000" not in rows[0][2]:
    ok, det = False, "K cell: got '%s', expected it to contain 5000" % rows[0][2]
chk("R11n Table 6 NCAM row matches the v3 primary object", ok, det)

# ===========================================================================
# R12 -- the constructive bound and the certified layer, RECOMPUTED
# ===========================================================================
chk("R12a constructive bound 91.59 printed", has("91.59") > 0)
# The v2 bound is printed BOTH as 57.6 and as 57.61/57.62. An earlier guard
# used 57\.6(?!\d), which cannot match "57.61" because the next character is a
# digit -- so a 91.59 -> 57.61 substitution slipped straight through it.
for tok in ("57.6", "57.61", "57.62"):
    chk("R12b no v2 constructive bound %s survives" % tok, has(tok, TEXNC) == 0)
for near in ("91.58", "91.60", "91.57", "91.61"):
    chk("R12c no near-miss constructive value %s survives" % near, has(near) == 0)
chk("R12d Section 3.3 q05 arithmetic 172.46 - 287.36 = -114.9",
    "172.46 - 287.36 = -114.9" in tex)
chk("R12e Section 3.3 worst arithmetic 172.46 - 328.97 = -156.5",
    "172.46 - 328.97 = -156.5" in tex)
chk("R12f no v2 Section 3.3 arithmetic (318.76 / -146.3 / -287.6)",
    all(has(x) == 0 for x in ("318.76", "146.3")) and has("-287.6", TEXNC) == 0)
chk("R12g Result 3.4 phi threshold on the v3 floor (0.727)",
    "1 - 80.87/296.09 = 0.727" in tex)
# The Result 3.4 criterion as printed used g_max, where the claim being made
# (the whole safe set is held) requires g(K*).  The margins are therefore
# 48.5 / 5.4 / -37.8 kt, not 141.2 / 67.2 / -6.8 kt, and the safe-set
# threshold is 0.531, not 0.727 -- which is the NONEMPTINESS threshold and is
# still reported as such.  See campaign_e2_structure_v3.py, section 4.
# 5.4 recurs (Section 2.4 quotes the same margin when naming the correction),
# so the criterion is pinned as a sentence, not as three loose tokens.
chk("R12h Result 3.4 states the three corrected margins as one sentence",
    ("the margin is " + BS + "(48.5" + BS + ") (" + BS + "(5.4" + BS + ")) kt"
     in FLAT))
for v in ("48.5", "-37.8"):
    chk("R12h2 Result 3.4 criterion value %s printed" % v, has(v) > 0)
for tok in ("114.85", "0.612", "107.2", "33.2", "40.8"):
    chk("R12i no v2 Result 3.4 value %s survives" % tok, has(tok, TEXNC) == 0)
chk("R12i2 Result 3.4 states BOTH thresholds (0.531 safe set, 0.727 nonempty)",
    "1 - 80.87/172.46 = 0.531" in tex.replace("\\n", " ")
    and "1 - 80.87/296.09 = 0.727" in tex.replace("\\n", " "))
chk("R12i3 the superseded criterion values are gone",
    all(has(v) == 0 for v in ("141.2", "67.2", "-6.8")))
chk("R12i4 the superseded criterion is named as an error, not silently dropped",
    "missed by quoting" in FLAT
    and "The three tabulated verdicts were unaffected" in FLAT)

# --- certified layer: recompute the ladder and the horizons ----------------
spec = importlib.util.spec_from_file_location("rix", REPO + "/src/run_intervention_v3.py")
ri = importlib.util.module_from_spec(spec)
sys.modules["rix"] = ri
spec.loader.exec_module(ri)
fit = ri.fit_surplus()
pol = ri.make_policies()
eps = float(res3["erosion"]["eps_train_max"])
amax = float(res3["erosion"]["a_max"])
Ks, K = ri.K_STAR, float(fit["K"])
lad = [Ks + eps * (amax ** T - 1) / (amax - 1) for T in range(1, 9)]
chk("R12j certified thresholds recompute (T=7 -> 4560.3, T=8 -> 5452.0)",
    abs(lad[6] - 4560.28) < 0.05 and abs(lad[7] - 5452.0) < 0.05,
    " ".join("%.1f" % v for v in lad))
for T, want in ((1, 1213.6), (4, 2534.7), (6, 3787.0), (7, 4560.3), (8, 5452.0)):
    chk("R12k certified threshold T=%d %.1f printed" % (T, want), has("%.1f" % want) > 0)

hor = {}
for ucid in ("UC_min", "UC_q05", "UC_q10"):
    e = float(fit["train_residual_" + ucid[3:]])
    last, empty_from = None, None
    for T in range(1, 12):
        iv = ri.kernel(pol["BAU"], fit, e, Ks + eps * (amax ** T - 1) / (amax - 1), T)
        if iv:
            last = T
        elif last is not None and empty_from is None:
            empty_from = T
    hor[ucid] = (last, empty_from)
chk("R12l certified horizon recomputes: worst T=6 then empty from T=7",
    hor["UC_min"] == (6, 7), str(hor))
chk("R12m certified horizon recomputes: q05 T=6 then empty from T=7",
    hor["UC_q05"] == (6, 7), str(hor))
chk("R12n certified horizon recomputes: q10 T=7 then empty from T=8",
    hor["UC_q10"] == (7, 8), str(hor))
# The tex writes the horizon as \(T = 7\); a hand-rolled '.' wildcard for the
# backslash silently swallows the wrong characters, so escape the literal.
chk("R12o Result 3.5 states the two harsher floors empty from T=7",
    re.search(r"certified kernel is empty" + r"\s+"
              + re.escape(r"from \(T = 7\) under the perpetual-worst and 5th-percentile floors"),
              tex) is not None)
chk("R12p Result 3.5 states the informative floor empties from T=8",
    re.search(re.escape(r"from \(T = 8\) under the 10th-percentile floor"),
              tex) is not None)
for v in ("5132.9", "4593.2", "4560.3"):
    chk("R12q certified set %s printed" % v, has(v) > 0)
chk("R12r no v2 certified set 4942.7 / 6023.9 survives",
    all(has(x) == 0 for x in ("4942.7", "6023.9")))
chk("R12s the naive K*+r_T < K criterion is no longer asserted",
    "nonempty only while" not in tex)
chk("R12t the convention shift is stated as one year at every class",
    "lengthens the horizon by one year at every class" in tex)
chk("R12u abstract states the finite horizon, not 'beyond six years'",
    "so the certified layer has a finite horizon" in tex
    and "certified kernels are empty beyond six years" not in tex)

# ===========================================================================
# R13 -- Section 3.6 form rows, recomputed
# ===========================================================================
js = json.load(open(V3F + "/e2_allee_rows_v3.json"))
for lab, got in (("Allee r", js["allee"]["r"]), ("Allee K", js["allee"]["K"]),
                 ("Allee s0", js["allee"]["s0"]), ("Allee MSE", js["allee"]["MSE"]),
                 ("Allee g_max", js["allee"]["g_max"]), ("Allee F'", js["allee"]["Fp_Kstar"]),
                 ("declared r", js["declared"]["r"]), ("declared K", js["declared"]["K"]),
                 ("declared MSE", js["declared"]["MSE"]), ("declared g_max", js["declared"]["g_max"])):
    form = "%.1f" % got if abs(got) >= 100 else ("%.4f" % got if abs(got) < 10 else "%.2f" % got)
    chk("R13a Section 3.6 %s = %s printed" % (lab, form),
        (form in tex) or ("%.2f" % got in tex) or ("%.1f" % got in tex),
        "computed %r" % got)
for v in ("2.0", "1671.7", "642.3", "7690.1", "372.4", "1.7818",
          "3223.7", "9330.0", "883.6", "0.1044", "13{,}873.1",
          "159.92", "1.0764", "79.05"):
    chk("R13b Section 3.6 prints %s" % v, has(v) > 0 or (v in tex))
chk("R13c Fox constructive 79.05 = 159.92 - 80.87 stated",
    "159.92 - 80.87 = 79.05" in tex)
chk("R13d no v2 Fox constructive 45.08 survives", has("45.08") == 0)
# Fox r: the value recurs (prose + Table 2 label), so a presence check cannot
# see a single-site corruption. Scope the prose site and pin the total count.
chk("R13d2 Section 3.6 Fox refit sentence states r = 0.1044",
    re.search(re.escape(r"\(r = 0.1044\), \(K = 5000\) kt pinn"), tex) is not None)
for tok, n in (("0.1044", 2), ("372.4", 2), ("1671.7", 1), ("642.3", 3),
               ("7690.1", 2), ("3223.7", 1), ("9330.0", 1), ("1.7818", 1),
               ("883.6", 1), ("79.05", 1), ("159.92", 1), ("1.0764", 1)):
    chk("R13d3 Section 3.6 value %s appears at exactly %d sites" % (tok, n),
        has(tok) == n, "found %d" % has(tok))
chk("R13d4 the two declared sensitivities are stated in Section 3.6",
    "Reproducibility note (two declared sensitivities)" in tex
    and "642.3296" in tex and "1098.75" in tex and "1020.95" in tex
    and "2218.75" in tex and "2219.649" in tex
    and "2070.30" in tex and "2070.884" in tex
    and "not to be compared at" in tex)
chk("R13e the 120-kt Fox emptiness is qualified (922.7 at T=1)",
    has("922.7") > 0 and "The 120-kt rule's kernel is" not in tex)
chk("R13f the declared row's divergence claim is 12 kt", "within " in tex
    and "12" in tex and "hinge on the identification" in tex)
chk("R13g Section 3.6 keeps the frozen classes so only the form varies",
    "so that only the form varies across" in tex)

# ===========================================================================
# R14 -- stochastic / bootstrap / abstract / conclusions echoes
# ===========================================================================
for v in ("0.906", "0.903", "0.835", "0.647", "0.954", "0.769", "0.852", "0.650"):
    chk("R14a Table 4 / Section 3.8 value %s printed" % v, has(v) > 0)
m_abs = re.search(re.escape(BS + "begin{abstract}") + r"(.*?)"
                  + re.escape(BS + "end{abstract}"), tex, re.S)
ABS = m_abs.group(1) if m_abs else ""
chk("R14b abstract survival range is the v3 one (0.91 to 0.65)",
    bool(ABS) and ("falls from " + BS + "(0.91" + BS + ") to " + BS + "(0.65"
                   + BS + ")") in " ".join(ABS.split()))
chk("R14c abstract carries the joint-resampling band (88.1 [-5.6, 130.6])",
    bool(ABS) and "88.1" in ABS and "[-5.6, 130.6]" in ABS)
# 0.74 is NOT in this list: it is the v3 survival at the constructive bound and
# appears at three sites. 0.87 / 0.58 are the v2 abstract values.
chk("R14d no v2 abstract survival values 0.87 / 0.58 survive",
    all(has(x) == 0 for x in ("0.87", "0.58")))
# 0.74 used to be printed three times because Section 3.8's sentence had been
# duplicated by a patch.  The count is the WRONG guard for that (it is satisfied
# by a third copy anywhere in the document); what must hold is one statement in
# Section 3.8 and one in the conclusions.
m38b = re.search(re.escape(BS + "subsubsection{3.8 Stochastic viability}")
                 + r"(.*?)" + re.escape(BS + "subsubsection{3.9"), tex, re.S)
SEC38 = m38b.group(1) if m38b else ""
mCO = re.search(re.escape(BS + "subsection{5. Conclusions}") + r"(.*?)"
                + re.escape(BS + "subsection{References}"), tex, re.S)
CONCL = mCO.group(1) if mCO else ""
chk("R14d2 the survival at the constructive bound (0.74) is stated once in "
    "Section 3.8 and once in the conclusions",
    bool(SEC38) and bool(CONCL)
    and has("0.74", SEC38) == 1 and has("0.74", CONCL) == 1 and has("0.74") == 2,
    "sec3.8=%d concl=%d total=%d" % (has("0.74", SEC38), has("0.74", CONCL),
                                     has("0.74")))
chk("R14e bootstrap constructive median 78.7 and interval [0.0, 121.1]",
    has("78.7") > 0 and has("121.1") >= 2)
chk("R14f no v2 bootstrap interval 84.8 survives", has("84.8") == 0)
chk("R14g Section 3.10 F'(K*) median 1.142, interval [1.010, 1.179]",
    all(x in tex for x in ("1.142", "1.010", "1.179")))
chk("R14h no v2 bootstrap F' values (1.134 / 1.001 / 1.177)",
    all(has(x, TEXNC) == 0 for x in ("1.134", "1.177")) and has("1.001", TEXNC) == 0)
boot = np.genfromtxt(V3E + "/e2_elevation_bootstrap.csv", delimiter=",", names=True)
for col, want in (("r", 0.219), ("g_Kstar", 159.6), ("constructive", 78.7)):
    chk("R14i bootstrap %s median %.4g recomputes" % (col, want),
        abs(np.median(boot[col]) - want) < 0.06, "%.4f" % np.median(boot[col]))
chk("R14j bootstrap 88.2%% positive recomputes",
    abs(float((boot["constructive"] > 0).mean()) * 100 - 88.2) < 0.1)
chk("R14k bootstrap F' median 1.142 and 90%% interval [1.010, 1.179] recompute",
    abs(np.median(boot["Fp"]) - 1.1416) < 0.002
    and abs(np.percentile(boot["Fp"], 5) - 1.0103) < 0.002
    and abs(np.percentile(boot["Fp"], 95) - 1.1792) < 0.002)
chk("R14l conclusions item 5: the 60-kt claim is the v3 one",
    "brings the 60-kt rules onto the reference point" in tex
    and "leaves the 60-kt rules outside the robust set" not in tex)
chk("R14m conclusions item 1 survival 0.74 (not 0.77 with a self-comparison)",
    "is " + BS + "(0.74" + BS + ") under i.i.d. resampling" in tex)
chk("R14n conclusions certified horizon is the two-part statement",
    "six years under the two" in tex and "seven under the informative one" in tex)

# ===========================================================================
# R15 -- provenance, figures, declarations
# ===========================================================================
chk("R15a no reference to the superseded v2 families script",
    "run_families_v2.py" not in tex)
figs = sorted(set(re.findall(r"figs_e2_v3/([a-z0-9_]*\.png)", tex)))
missing = [f for f in figs if not os.path.exists("/home/user/fam/figs_e2_v3/" + f)]
chk("R15b all %d referenced figures exist in figs_e2_v3" % len(figs),
    len(figs) == 9 and not missing, "missing %s" % missing if missing else ", ".join(figs))
chk("R15c no reference to the old figure directory",
    "figs_e2/fig" not in tex)

for name in ("run\\_intervention\\_v3.py", "run\\_families\\_v3.py",
             "campaign\\_e2\\_elevation\\_v3.py", "make\\_figs\\_v17.py",
             "campaign\\_e2\\_depensation\\_v3.py", "campaign\\_e2\\_allee\\_declared\\_v3.py",
             "campaign\\_e2\\_fox\\_form\\_v3.py", "campaign\\_e2\\_xteNCAM\\_row.py",
             "e2\\_breakpoint\\_1992.py", "superseded\\_v2",
             "intervention\\_results\\_v3.json", "intervention\\_boundaries\\_v3.csv",
             "e2\\_families\\_v3.csv", "results\\_srcyear\\_v3", "results\\_forms\\_v3"):
    chk("R15d data availability names %s" % name.replace(BS, ""), name in tex)

chk("R15e data availability no longer credits the hybrid elevation campaign",
    re.search(r"rerun" + BS + "_campaigns/campaign" + BS + "_e2" + BS + "_elevation\.py", tex) is None)
chk("R15f data availability no longer credits the hybrid Fox campaign",
    re.search(r"campaign" + BS + "_e2" + BS + "_fox" + BS + "_form\.py", tex) is None)
chk("R15g no 'no random components' claim survives",
    "no random components" not in tex)
chk("R15h Section 3.11 no longer says 'registered convention'",
    "refitted in the registered convention" not in tex)
chk("R15i Section 3.11 states the same source-year convention",
    "refitted in the same source-year convention" in tex)

# --- R16 -- the source must be clean bytes --------------------------------
# A stray control character (a regex replacement template once turned \a into
# a BELL) makes XeTeX halt with "Text line contains an invalid character".
# Nothing above would notice, so the check has to be explicit.
_ctrl = sorted({c for c in tex if (ord(c) < 32 and c not in "\n\r\t")
                or ord(c) == 127})
chk("R16a no non-printable characters in the source", not _ctrl,
    "".join(hex(ord(c)) for c in _ctrl))
chk("R16b source ends with \\end{document}",
    tex.rstrip().endswith(BS + "end{document}"))
chk("R16c every \\begin has a matching \\end", not _ctrl and
    len(re.findall(r"\\begin\{", tex)) == len(re.findall(r"\\end\{", tex)),
    "%d begin / %d end" % (len(re.findall(r"\\begin\{", tex)),
                           len(re.findall(r"\\end\{", tex))))

# ===========================================================================
# R17 -- the prose-coherence pass: claims the end-to-end read found broken
# ===========================================================================
# An end-to-end read (not a numeric sweep) found prose that had stopped being
# true on the v3 basis: a v2-era sentence whose numbers had been swapped but
# whose direction had not, a duplicated paragraph printing the same quantity
# two ways, an asserted "cap" whose mechanism does not follow, and sentences
# quoting numbers no tabulated cell supports.  Every claim below is recomputed.

chk("R17a no 'not attained by any tested constant catch' claim survives",
    "not attained by any tested constant catch" not in tex)
chk("R17b the 0.84 / 0.85 duplication is gone (one value, stated twice)",
    has("0.84") >= 2 and has("0.85") == 0,
    "0.84 x%d, 0.85 x%d" % (has("0.84"), has("0.85")))

# --- the P >= 0.9 / 0.8 crossings, recomputed from the constructive sweep ---
cst = csv3("e2_elevation_stochastic_constructive.csv")


def _cross(scheme, bar):
    """Interpolated crossing of P_stay = bar in C, or (None, max P)."""
    rows = sorted((r for r in cst if r["scheme"] == scheme),
                  key=lambda r: float(r["C"]))
    above = [r for r in rows if float(r["P_stay"]) >= bar]
    below = [r for r in rows if float(r["P_stay"]) < bar]
    if not above:
        return None, max(float(r["P_stay"]) for r in rows)
    chi = float(above[-1]["C"])
    clo = float(below[0]["C"])
    phi = float(above[-1]["P_stay"])
    plo = float(below[0]["P_stay"])
    return chi + (bar - phi) * (clo - chi) / (plo - phi), None


x90_iid, _ = _cross("iid", 0.9)
x90_blk, max_blk = _cross("block4", 0.9)
x90_no, _ = _cross("iid_no1992", 0.9)
x80_iid, _ = _cross("iid", 0.8)
x80_blk, _ = _cross("block4", 0.8)
x80_no, _ = _cross("iid_no1992", 0.8)
chk("R17c the i.i.d. P>=0.9 crossing 13.5 kt recomputes",
    x90_iid is not None and abs(x90_iid - 13.5) < 0.05,
    "%.3f" % x90_iid if x90_iid else "not attained")
chk("R17d Section 3.8 prints the i.i.d. crossing 13.5 kt", has("13.5") > 0)
chk("R17e the block P>=0.9 bar is genuinely unattained (max %.4f < 0.9)"
    % max_blk, x90_blk is None and max_blk < 0.9)
chk("R17f the no-1992 P>=0.9 crossing 78.9 kt recomputes",
    x90_no is not None and abs(x90_no - 78.9) < 0.05, "%.3f" % x90_no)
chk("R17g the P>=0.8 crossings 81.2 / 72.3 / 105.2 kt recompute",
    all(abs(g - w) < 0.05 for g, w in
        ((x80_iid, 81.2), (x80_blk, 72.3), (x80_no, 105.2))),
    "%.2f / %.2f / %.2f" % (x80_iid, x80_blk, x80_no))
chk("R17h Section 3.8 prints all three P>=0.8 crossings",
    all(t in tex for t in ("81.2", "72.3", "105.2")))
chk("R17i Section 3.8 says the i.i.d. bar IS attained and the block bar is not",
    "it is attained, but only by near-moratorium catches" in tex
    and "Under block resampling it is not attained at all" in tex)

# --- the ceilings, taken from the artifact the sentence cites --------------
stoch = {(r["scheme"], r["policy"], r["S0"], r["T"]): float(r["P_stay"])
         for r in csv3("e2_elevation_stochastic.csv")}
ceil_iid = stoch[("iid", "flat_0", "884.6", "20")]
ceil_blk = stoch[("block4", "flat_0", "884.6", "20")]
chk("R17j the i.i.d. ceiling 0.906 is the Table 4 zero-catch value",
    abs(ceil_iid - 0.906) < 0.0005, "%.4f" % ceil_iid)
chk("R17k the block ceiling 0.852 is the Table 4 zero-catch value",
    abs(ceil_blk - 0.852) < 0.0005, "%.4f" % ceil_blk)
chk("R17l the block crossing-sweep value 0.849 is stated with its seed caveat",
    "0.849" in tex and "carries its own fixed seed" in tex
    and "Monte-Carlo difference of " in tex)
chk("R17m the 60-kt i.i.d. survival 0.835 is the Table 4 value",
    abs(stoch[("iid", "flat_25", "884.6", "20")] - 0.835) < 0.0005)
# 0.906 and 0.852 also sit in Table 4, so an unscoped presence check stays
# green when the PROSE sentence is corrupted. Pin the sentence.
chk("R17m2 Section 3.8 prints the i.i.d. ceiling 0.906 where it cites it",
    ("ceiling of " + BS + "(0.906" + BS + ") at zero catch") in FLAT)
chk("R17m3 Section 3.8 prints the block ceiling 0.852 where it cites it",
    ("there being " + BS + "(0.852" + BS + ") (Table 4") in FLAT)

# --- the bound's stochastic reading: which catch was actually evaluated ----
bound_nearest = min(np.arange(0.0, 125.0, 2.5), key=lambda c: abs(c - 91.59))
chk("R17n 92.5 kt is the nearest 2.5 kt grid catch to the bound",
    abs(bound_nearest - 92.5) < 1e-9, "%.2f" % bound_nearest)
chk("R17o Section 3.8 names the grid catch it evaluates (92.5 on a 2.5 kt grid)",
    "92.5" in tex and "2.5" in tex
    and "At the grid catch nearest the bound" in tex)
p_no92 = [float(r["P_stay"]) for r in cst
          if r["scheme"] == "iid_no1992" and abs(float(r["C"]) - 92.5) < 1e-9][0]
chk("R17p the no-1992 survival at the bound is 0.84 (0.8444), not 0.85",
    abs(p_no92 - 0.84) < 0.005 and abs(p_no92 - 0.8444) < 0.0001,
    "%.4f" % p_no92)

# --- the mechanism: recompute, do not assert -------------------------------
def _res_tr():
    """The source-year training residual pool, as the elevation campaign builds it."""
    yr, ssb_v, c_reg_v, c_ann_v, idx_v, lrp_v = rl.load()
    f = res3["fit"]
    by_year = {int(yr[j + 1]): float(
        ssb_v[j + 1] - (ssb_v[j] + rl.surplus(ssb_v[j], f["r"], f["K"])
                        - c_ann_v[j])) for j in range(len(yr) - 1)}
    return np.array([by_year[y] for y in sorted(by_year) if y <= 2007])


res_pool = _res_tr()
gK = float(rl.surplus(884.6, res3["fit"]["r"], res3["fit"]["K"]))
fatal = sorted(res_pool[res_pool < -gK])
chk("R17q exactly two of the 24 residuals breach the LRP from itself under "
    "zero catch (worse than -%.2f kt)" % gK, len(fatal) == 2,
    "%d: %s" % (len(fatal), fatal))
chk("R17r the two fatal residuals print as -329.0 and -323.5",
    [round(v, 1) for v in fatal] == [-329.0, -323.5],
    str([round(v, 1) for v in fatal]))
chk("R17r2 Section 3.8 prints both fatal residuals (-329.0 and -323.5)",
    has("-323.5") >= 1 and has("-329.0") >= 1 and "-323.5" in SEC38)
chk("R17s the immediate-breach probability 2/24 = 0.083 is printed",
    "2/24 = 0.083" in tex and abs(2 / 24 - 0.083) < 0.0005)
chk("R17t the total failure probability 0.094 is printed and recomputes",
    has("0.094") > 0 and abs((1 - ceil_iid) - 0.094) < 0.0005,
    "%.4f" % (1 - ceil_iid))
# the stock level at which the 1992 draw stops being fatal, zero catch
_lo, _hi = 884.6, 4000.0
for _ in range(200):
    _m = 0.5 * (_lo + _hi)
    if _m + float(rl.surplus(_m, res3["fit"]["r"], res3["fit"]["K"])) \
            + float(res_pool.min()) >= 884.6:
        _hi = _m
    else:
        _lo = _m
chk("R17u the 'grown clear' threshold ~1020 kt recomputes",
    abs(_hi - 1020) < 2.0, "%.1f" % _hi)
chk("R17u2 Section 3.8 prints the grown-clear threshold 1020 kt",
    has("1020", SEC38) == 1, "sec3.8 x%d" % has("1020", SEC38))
chk("R17v the 1/24-only ceiling 0.427 is printed and recomputes",
    "0.427" in tex and abs((23 / 24) ** 20 - 0.427) < 0.0005,
    "%.4f" % (23 / 24) ** 20)
chk("R17w Section 3.8 states the 0.43 that the 1/24 recurrence alone would give",
    has("0.43") > 0)
chk("R17w2 the breach threshold -172.5 is printed and equals g(K*) = %.3f" % gK,
    has("-172.5", SEC38) == 1 and abs(172.5 - gK) < 0.05,
    "sec3.8 x%d, g(K*)=%.3f" % (has("-172.5", SEC38), gK))

# --- Result 3.6: what the Allee refit does to the constructive bound -------
alr2 = {r["cell"]: r["computed"] for r in csvf("e2_allee_rows_v3.csv")}
gA = float(rl.surplus(884.6, 2.0, 1671.6596479199984, 642.3296235050077))
gD = float(rl.surplus(884.6, 2.0, 3223.70, 442.3))
e10 = abs(float(res3["fit"]["train_residual_q10"]))
chk("R17x Allee g(K*) = 196.06 recomputes", abs(gA - 196.06) < 0.02,
    "%.3f" % gA)
chk("R17y Allee constructive 115.2 = 196.06 - 80.87 recomputes and is printed",
    abs(gA - e10 - 115.2) < 0.05 and "196.06 - 80.87 = 115.2" in tex,
    "%.3f" % (gA - e10))
chk("R17z declared-strength constructive 123.3 recomputes and is printed",
    abs(gD - e10 - 123.3) < 0.05 and "123.3" in tex, "%.3f" % (gD - e10))
chk("R17aa the Allee 60-kt q05 T=inf boundary 1131.1 and BAU's 1020.9 are as "
    "printed", abs(float(alr2["allee_s0=642.3|S1|UC_q05|T=inf"]) - 1131.1) < 0.06
    and abs(float(alr2["allee_s0=642.3|BAU|UC_q05|T=inf"]) - 1020.9) < 0.06,
    "%s / %s" % (alr2["allee_s0=642.3|S1|UC_q05|T=inf"],
                 alr2["allee_s0=642.3|BAU|UC_q05|T=inf"]))
chk("R17aa2 Result 3.6 prints the 1131.1 kt Allee boundary it recomputes",
    has("1131.1") == 1, "x%d" % has("1131.1"))
# "universal emptiness" also appears in Section 3.5 in another sense, so the
# check pins this sentence's own wording rather than a shared phrase.
chk("R17ab Result 3.6 says the Allee block works by margin, not by emptiness",
    "the block operates through a margin rather than through emptiness"
    in FLAT)

# --- the grid-vs-interval note, measured -----------------------------------
gd = [r for r in csvf("campaign_e2_depensation_v3.csv")
      if r["variant"] == "grid_schaefer_check" and r["boundary_committed"]]
gfin = [r for r in gd if r["T"] != "inf"]
ginf = [r for r in gd if r["T"] == "inf"]
_d = lambda r: abs(float(r["boundary_committed"]) - float(r["boundary_grid"]))
chk("R17ac the grid/interval cell counts 81 / 72 / 9 recompute",
    (len(gd), len(gfin), len(ginf)) == (81, 72, 9),
    "%d / %d / %d" % (len(gd), len(gfin), len(ginf)))
_mcells = re.search(r"of the " + re.escape(BS + "(") + r"(\d+)"
                    + re.escape(BS + ")") + r" cells the campaign checks, the "
                    + re.escape(BS + "(") + r"(\d+)" + re.escape(BS + ")"), FLAT)
chk("R17ac2 the note prints the cell counts it recomputes (81 / 72)",
    _mcells is not None
    and (int(_mcells.group(1)), int(_mcells.group(2))) == (len(gd), len(gfin)),
    "printed %s" % (str(_mcells.groups()) if _mcells else None))
# A one-sided "measured <= stated" test is satisfied by a stated value that is
# far too loose, so the stated number is parsed back out and pinned to the
# measurement in both directions.
_mfin = re.search(r"at most " + re.escape(BS + "(") + r"([0-9.]+)"
                  + re.escape(BS + ")") + r" kt", FLAT)
_stated = float(_mfin.group(1)) if _mfin else None
_meas = max(_d(r) for r in gfin)
chk("R17ad the stated finite-horizon agreement parses to the measured max",
    _stated is not None and abs(_stated - _meas) <= 0.01,
    "stated %s, measured %.4f" % (_stated, _meas))
# 0.835 also sits in Table 4, so a section-scoped count cannot see the prose
# site on its own; pin the sentence instead.
chk("R17ad2 Section 3.8 prose cites the 60-kt survival 0.835",
    ("by " + BS + "(60" + BS + ") kt survival has already fallen to "
     + BS + "(0.835" + BS + ")") in FLAT)
chk("R17ae five of the nine T=inf cells agree exactly",
    sum(1 for r in ginf if _d(r) < 1e-9) == 5,
    "%d" % sum(1 for r in ginf if _d(r) < 1e-9))
chk("R17af the four T=inf differences print as 0.1 / 0.3 / 0.6 / 0.9",
    sorted(round(_d(r), 1) for r in ginf if _d(r) >= 1e-9) == [0.1, 0.3, 0.6, 0.9],
    str(sorted(round(_d(r), 1) for r in ginf if _d(r) >= 1e-9)))
_minf = re.search(r"the other four differ by (.*?) kt, the largest", FLAT)
# the numbers carry LaTeX delimiters (\(0.1\)), so strip the markup by taking
# the bare numerals out of the captured clause
_pn = sorted(float(x) for x in re.findall(r"[0-9]*\.[0-9]+", _minf.group(1))) \
    if _minf else []
chk("R17af2 the printed T=inf differences are the recomputed ones",
    _pn == sorted(round(_d(r), 1) for r in ginf if _d(r) >= 1e-9), str(_pn))
chk("R17ag the old 'every other cell agrees to about 0.03 kt' claim is gone",
    "agrees to about " not in tex)

# ===========================================================================
# R18 -- provenance and prose of the archived scripts
# ===========================================================================
chk("R18a Section 2.3 no longer claims the whole analysis was recomputed",
    "the whole analysis was also computed" not in FLAT
    and "the primary kernels and their boundary tables were also computed" in FLAT)
chk("R18b the un-tabulated Fox cells are labelled as not carried in Table 2",
    "Three further Fox cells" in tex and "not carried in Table 2" in FLAT)
chk("R18c code availability names the v29 verification script, not v24",
    "paperE2" + BS + "_cod" + BS + "_intervention" + BS + "_v29"
    + BS + "_verification.py" in tex
    and "v24" + BS + "_verification.py" not in tex)
chk("R18d code availability names the sabotage harness and the audit",
    "v29" + BS + "_sabotage.py" in tex and "v29" + BS + "_basis" + BS + "_audit.py"
    in tex)
chk("R18e the abstract says the class-vacuity reading narrows, not reverses",
    "reading narrows" in tex and "reading reverses" not in tex)
chk("R18f the data-availability flat-180 sentence names the convergence guard",
    "refuses to return an unconverged iterate" in FLAT and "20{,}000" in tex
    and "the registered finite-horizon values follow the same recursion"
    not in FLAT)


# ===========================================================================
# R19 -- Section 2.4: the four propositions, and the constants behind Table 1
# ===========================================================================
m24 = re.search(re.escape(BS + "subsubsection{2.4 What the kernel problem reduces")
                + r"(.*?)" + re.escape(BS + "subsection{3. Results}"), tex, re.S)
SEC24 = m24.group(1) if m24 else ""
chk("R19a Section 2.4 exists and is substantial",
    bool(SEC24) and len(SEC24) > 3000, "%d chars" % len(SEC24))
for lab in ("Proposition 2.1 (Constructive bound and the protection--supply",
            "Proposition 2.2 (Perpetual bound and the infinite-horizon",
            "Proposition 2.3 (Reactive families)",
            "Proposition 2.4 (The certified horizon is a crossing)"):
    chk("R19b %s stated" % lab[:16], lab in tex)
chk("R19c every proposition carries a proof", SEC24.count("emph{Proof.}") == 4,
    "%d proofs" % SEC24.count("emph{Proof.}"))

# the structural artifacts, read back and checked against the paper
S_OUT = REPO + "/src/results_struct_v3"
st = {r["quantity"]: r["value"] for r in csv.DictReader(open(S_OUT + "/e2_structure_v3.csv"))}
stj = json.load(open(S_OUT + "/e2_structure_v3.json"))
chk("R19d the structure campaign is green (23 checks, 0 failed)",
    stj["n_failed"] == 0 and stj["n_checks"] == 23,
    "%d/%d" % (stj["n_checks"] - stj["n_failed"], stj["n_checks"]))
# 215.2 appears in Section 2.4 and in the fig8 caption, so a bare presence
# test stays green when either site is corrupted.  Pin the arithmetic.
# 215.2 is printed at four sites (abstract, Section 2.4, the fig8 caption and
# Section 3.1).  A single-site corruption is invisible to a presence test, so
# the arithmetic, the caption phrase AND the site count are all pinned.
chk("R19e C_vac = g_max - |e| = 215.2 recomputes and is printed at all 4 sites",
    abs(stj["C_vac"] - 215.2) < 0.05
    and ("296.09 - 80.87 = 215.2" in FLAT)
    and (BS + "(C_{\mathrm{vac}} = 215.2" + BS + ") kt") in FLAT
    and has("215.2") == 4,
    "%.3f, printed x%d" % (stj["C_vac"], has("215.2")))
chk("R19f the safe-set threshold 0.531 and the nonempty threshold 0.727 both "
    "recompute", abs(stj["phi_safe"] - 0.531) < 0.001
    and abs(stj["phi_nonempty"] - 0.727) < 0.001,
    "%.4f / %.4f" % (stj["phi_safe"], stj["phi_nonempty"]))
chk("R19g the two thresholds are printed in the arithmetic form the paper uses",
    "1 - 80.87/172.46 = 0.531" in FLAT and "1 - 80.87/296.09 = 0.727" in FLAT)
chk("R19h the budget identity is stated as an EQUALITY in Section 3.3",
    ("margin plus its catch equal" in FLAT
     or ("margin is exactly " + BS + "(91.59" + BS + ") minus its catch there"
         in FLAT)))
# the middle regime is only visible if the row is actually in Table 1: a rule
# that is viable but not from the reference point itself has a T=inf boundary
# strictly above 884.6 -- which is what 1074.8 says.
chk("R19i the middle regime is tabulated (phi = 0.60: 895.2 at T=1, 1074.8 at "
    "T=inf)", "895.2" in block(1) and "1074.8" in block(1)
    and "Family A, " + BS + "(" + BS + "phi" + BS + ")=0.60 & 1131.2 & empty & "
    "1091.0 & empty & 895.2 & 1074.8" in " ".join(block(1).split()))
_hex_ok = True
for _p in ("BAU (5 kt)", "zero catch"):
    for _c, _want in (("worst", 6), ("q05", 6), ("q10", 7)):
        _k = "horizon|%s|%s" % (_p, _c)
        _a, _b = st[_k].split(" / ")
        _hex_ok &= (_a == _b == str(_want))
chk("R19j the exact crossing reproduces the computed horizon 6 / 6 / 7 for both "
    "policies and all three classes", _hex_ok,
    "; ".join("horizon|%s|%s = %s" % (_p, _c, st["horizon|%s|%s" % (_p, _c)])
              for _p in ("BAU (5 kt)",) for _c in ("worst", "q05", "q10")))
chk("R19j2 the horizon is stated as a crossing, and the value matches",
    "unique crossing" in FLAT and ("T^* = 6" in FLAT or "T^*=6" in FLAT))
chk("R19k the closed-form b_inf column matches Table 1 for all six flat caps",
    all(st["b_inf(C=%.0f)" % C] == ("empty" if C == 240 else
        ("884.6" if C <= 60 else ("1082.3" if C == 120 else "1637.8")))
        for C in (0, 5, 60, 120, 180, 240)))

# ===========================================================================
# R20 -- identification: profile likelihood, joint bootstrap, observation error
# ===========================================================================
I_OUT = REPO + "/src/results_ident_v3"
idt = {r["quantity"]: r["value"] for r in
       csv.DictReader(open(I_OUT + "/e2_identification_v3.csv"))}
idj = json.load(open(I_OUT + "/e2_identification_v3.json"))
prof = list(csv.DictReader(open(I_OUT + "/e2_profile_K.csv")))
chk("R20a the identification campaign is green", idj["n_failed"] == 0,
    "%d/%d" % (idj["n_checks"] - idj["n_failed"], idj["n_checks"]))
_cut = idj["sse_min"] * (1.0 + 4.3009 / 22.0)      # F_{1,22;0.95}, n = 24
_Kset = [float(p["K"]) for p in prof if float(p["sse"]) <= _cut]
chk("R20b K is not identified from above (the profile 95% set reaches the top "
    "of the grid)", min(_Kset) <= 1600 and max(_Kset) >= 49000,
    "profile set %.0f - %.0f kt" % (min(_Kset), max(_Kset)))
chk("R20b2 the paper says so", "not identified from above" in FLAT)
# "1500" also appears as a K-grid row in Table 3, so the token alone proves
# nothing about the profile set: pin the sentence that states it.
chk("R20c the paper prints the profile 95% set endpoints (1500 to 50{,}000)",
    ("set running from " + BS + "(1500" + BS + ") kt to the top of the" + BS
     + "*" if False else "set running from " + BS + "(1500" + BS
     + ") kt to the top of the grid") in FLAT and "50{,}000" in tex)
_ratio = min(float(p["sse"]) for p in prof if abs(float(p["K"]) - 5000.0) < 1.0) \
    / idj["sse_min"]
chk("R20d the pin buys 2.7% of the criterion, and 1.027 is printed",
    abs(_ratio - 1.027) < 0.001 and "1.027" in tex, "recomputed %.4f" % _ratio)
# Each of these is printed TWICE (abstract and body).  A whole-document
# presence check therefore survives a single-site corruption, so both sites
# are required.
m37 = re.search(re.escape(BS + "subsubsection{3.7 Carrying-capacity")
                + r"(.*?)" + re.escape(BS + "subsubsection{3.8"), tex, re.S)
SEC37 = m37.group(1) if m37 else ""
m310 = re.search(re.escape(BS + "subsubsection{3.10 Uncertainty bands")
                 + r"(.*?)" + re.escape(BS + "subsubsection{3.11"), tex, re.S)
SEC310 = m310.group(1) if m310 else ""
for tok, lab in (("[148.8, 176.1]", "g(K*) profile range"),
                 ("1775", "smallest expansive K")):
    chk("R20e %s printed in Section 3.7" % lab, tok in SEC37,
        "3.7:%s" % (tok in SEC37))
# C*'s range recurs (abstract and Section 3.7), so both sites are required --
# a whole-document presence test survives a single-site corruption.
chk("R20e2 C* profile range printed in Section 3.7 AND the abstract",
    "[67.9, 95.2]" in SEC37 and "[67.9, 95.2]" in ABS,
    "3.7:%s abs:%s" % ("[67.9, 95.2]" in SEC37, "[67.9, 95.2]" in ABS))
chk("R20f the joint bootstrap: 0.261 / 4191 / 88.1 / 1.137 printed",
    all(has(x, SEC310) > 0 for x in ("0.261", "4191", "88.1", "1.137")))
chk("R20f2 the joint bootstrap band is printed in the abstract too",
    "88.1" in ABS and "4191" not in ABS or "88.1" in ABS)
chk("R20g the 41.7% pin share and the 90% band [-5.6, 130.6] printed",
    "41.7" in tex and "[-5.6, 130.6]" in tex)
chk("R20h the observation-error sensitivity 91.6 -> 112.1 printed",
    "91.6" in tex and "112.1" in tex and "lambda" in tex)
chk("R20i the profile figure and the frontier figure are referenced",
    "fig8_frontier.png" in tex and "fig9_identification.png" in tex)

# ===========================================================================
# R21 -- Section 3.12: the regime question
# ===========================================================================
m312 = re.search(re.escape(BS + "subsubsection{3.12 Is the reference point")
                 + r"(.*?)" + re.escape(BS + "subsection{4. Discussion}"), tex, re.S)
SEC312 = m312.group(1) if m312 else ""
chk("R21a Section 3.12 exists", bool(SEC312) and len(SEC312) > 2500,
    "%d chars" % len(SEC312))
rec_rows = {r["label"]: r for r in csv.DictReader(open(I_OUT + "/e2_recent_windows.csv"))}
for lab in ("NCAM 1995-2015", "NCAM 1995-2007", "xteNCAM 1995-2024",
            "xteNCAM 2005-2024"):
    chk("R21b the %s row is archived" % lab, lab in rec_rows)
tbl7 = block(7)
for lab, row in rec_rows.items():
    chk("R21c Table 7 %s: r, C* and F' match the campaign" % lab,
        ("%.4f" % float(row["r"]))[:5] in tbl7
        and ("%.1f" % float(row["Cstar"])) in tbl7
        and ("%.3f" % float(row["Fp"])) in tbl7,
        "r=%s C*=%s F'=%s" % (row["r"], row["Cstar"], row["Fp"]))
chk("R21d the regime finding is stated in Section 3.12 AND the abstract",
    has("0 " + BS + "pm 8", SEC312) == 1 and has("0 " + BS + "pm 8", ABS) == 1,
    "3.12 x%d, abstract x%d" % (has("0 " + BS + "pm 8", SEC312),
                                has("0 " + BS + "pm 8", ABS)))
# No OR-fallback here: both halves sit in one sentence, so an `or` makes the
# check immune to either half being corrupted.
chk("R21e the bound-status caveat is stated (K at a bound, regime readings)",
    "in three of the four the carrying capacity is at a bound, so these are "
    "regime readings" in FLAT)
chk("R21f no verdict is claimed to transfer between the two series",
    "labelled sensitivities" in SEC312 and "no verdict" in SEC312)

print()
print("%d passed, %d failed" % (len(PASS), len(FAIL)))
if FAIL:
    print("FAILED:")
    for f in FAIL:
        print("  - " + f)
sys.exit(1 if FAIL else 0)
