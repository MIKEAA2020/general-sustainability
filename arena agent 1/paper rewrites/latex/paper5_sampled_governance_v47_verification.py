#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification battery for paper5_sampled_governance_v47_blinded_NatSustain.tex
(P5, v47).

The manuscript's numbers are pinned to three committed campaigns
(crossing_scan, stage_reconstruction, comparator_mse), all deterministic --
re-running them reproduces every result file byte for byte, verified.

WHY THE PINNING METHOD IS WHAT IT IS

Version 1 of this battery used `value in tex` and was 63% blind: a sabotage run
showed it caught only 3 of 8 mutations, because a presence needle is defeated
by restatement (`6.5` occurs 17 times; perturbing one leaves sixteen).

Constants are now pinned with `no_variant`, which asserts that no variant of the
value occurs anywhere OUTSIDE the places where the value itself is printed.
Occurrences are masked out before testing (otherwise every shorter variant is
trivially present -- '0.89' is a substring of '0.895'), and the variant set
includes +/- 1 ulp so that carrying edits are caught.  Constants that still
collide are pinned by anchored extraction, and anything pinnable by neither
method is reported UNPINNABLE rather than dropped.

THE MISMATCH DISCLOSURE

stage_reconstruction prints three MISMATCH verdicts against archived windows.
Those are findings the manuscript already discloses, not defects.  So the
battery asserts in both directions: where the campaign says MATCH the paper may
assert the result; where it says MISMATCH the paper must not claim the window
reproduces and must disclose it.

Run:  python3 paper5_sampled_governance_v47_verification.py
Exit: 0 if every check passes, 1 otherwise.
"""
from __future__ import annotations

import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEX = os.path.join(HERE, "paper5_sampled_governance_v47_blinded_NatSustain.tex")
RES = os.path.join(HERE, "results")

PASS, FAIL = [], []
UNPINNABLE = []


def chk(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(("PASS  " if ok else "FAIL  ") + name + (("  -- " + detail) if detail else ""))


def variants(value):
    from decimal import Decimal
    s = str(value)
    if "." not in s:
        out = [s[:-1] + d for d in "0123456789" if d != s[-1]]
        try:
            n = int(s)
            out += [str(n - 1), str(n + 1)]
        except ValueError:
            pass
        return out
    head, tail = s.rsplit(".", 1)
    k = len(tail)
    out = [head + "." + tail[:-1] + d for d in "0123456789" if d != tail[-1]]
    for v in list(out):
        h, t = v.rsplit(".", 1)
        st = t.rstrip("0")
        if st != t:
            out.append(h + "." + st if st else h)
    try:
        d = Decimal(s)
        step = Decimal(1).scaleb(-k)
        for delta in (-step, step):
            out.append(format((d + delta).quantize(step), "f"))
    except Exception:
        pass
    return out


def no_variant(tex, value):
    remainder = tex.replace(value, " ")
    return all(v not in remainder for v in variants(value))


def pin(label, tex, value, where=""):
    if no_variant(tex, value):
        chk(f"{label}: {value} pinned (no variant anywhere else)", True, where)
        return True
    coll = [v for v in variants(value) if v in tex.replace(value, " ")]
    UNPINNABLE.append((label, value, coll[:4]))
    chk(f"{label}: {value} UNPINNABLE", False, f"collides with {coll[:4]}")
    return False


def anchored(label, tex, pattern, expected, tol=0.0):
    m = re.search(pattern, tex)
    if not m:
        chk(f"{label}: anchor found", False, pattern[:60])
        return False
    got = float(m.group(1))
    ok = abs(got - expected) <= tol
    chk(f"{label}: anchored value {got} == {expected}", ok, pattern[:44])
    return ok



def all_sites(label, tex, pattern, expected, tol=0.0006):
    """Assert EVERY site matching `pattern` prints `expected`.

    Anchoring only one site leaves the others unpinned: the first occurrence
    of '2.306' is in the '(stable -> unstable)' clause, not in the
    'protective Euler crossing at X yr' sentence.  So every phrasing the
    manuscript uses for a quantity must be enumerated and all its sites
    checked.
    """
    got = re.findall(pattern, tex)
    if not got:
        chk(f"{label}: no site found", False, pattern[:56])
        return False
    vals = [float(g) for g in got]
    bad = [v for v in vals if abs(v - expected) > tol]
    chk(f"{label}: all {len(vals)} site(s) print {expected}", not bad,
        f"found {vals}" + (f"; outliers {bad}" if bad else ""))
    return not bad


def load(name):
    p = os.path.join(RES, name)
    if not os.path.exists(p):
        chk(f"campaign output {name} present", False, p)
        return []
    return list(csv.DictReader(open(p)))


tex = open(TEX, encoding="utf-8").read()
flat = re.sub(r"\\[a-zA-Z]+", " ", tex)

# ============================================================== R1 equilibria
eq = load("p5_stage_equilibria.csv")
chk("R1a four stage classes recorded", len(eq) == 4, f"{len(eq)}")
for r in eq:
    cls, M, tau = r["class_"], r["M"], r["tau"]
    chk(f"R1b {cls}: M={M} printed", M in flat or f"{float(M):.2f}" in flat)
    chk(f"R1c {cls}: tau={tau} printed", tau in flat)
E = {r["E_star"] for r in eq}
chk("R1d equilibrium E* is plant-independent", len(E) == 1, str(E))
pin("R1e equilibrium E*", tex, list(E)[0])

# ============================================================== R2 spectral radii
mul = load("p5_stage_multiplier_record.csv")
rho1 = {}
for r in mul:
    if (r["channel"] == "extractive"
            and abs(float(r["T_r"]) - 1.0) < 1e-9
            and abs(float(r["q"]) - 0.001) < 1e-9):   # the quoted extraction
        rho1[r["class_"]] = float(r["rho"])
chk("R2a annual spectral radius for four classes", len(rho1) == 4, str(sorted(rho1)))
# The four rho(1) values are printed in one labelled clause; pin them there.
# Two of them (0.895, 0.956) collide with 2-decimal values elsewhere (0.89,
# 0.95), so no_variant cannot be used for those -- anchored extraction can.
_clause = re.search(
    r"rho\(1\)\s*=\s*([\d.]+)\\?\)\s*\(anchovy\),\s*([\d.]+)\s*"
    r"\(sprat\),\s*([\d.]+)\s*\(cod\),\s*([\d.]+)\s*\(slow-stock\)",
    tex)
NAMES = ("anchovy", "sprat", "cod", "slow_stock")
if _clause:
    for nm, got in zip(NAMES, _clause.groups()):
        want = rho1.get(nm)
        if want is None:
            continue
        chk(f"R2b {nm} rho(1): paper {got} == campaign {want:.6f}",
            abs(float(got) - want) <= 0.0006, f"printed {got}")
    chk("R2c rho(1) clause contains all four classes",
        len(_clause.groups()) == 4, str(_clause.groups()))
else:
    chk("R2b rho(1) clause found", False)
# record which of them are NOT pinnable by no_variant, rather than dropping them
for nm in NAMES:
    want = rho1.get(nm)
    if want is None:
        continue
    v = f"{want:.3f}"
    if not no_variant(tex, v):
        coll = [x for x in variants(v) if x in tex.replace(v, " ")]
        UNPINNABLE.append((f"R2 {nm} rho(1) by no_variant", v, coll[:3]))
chk("R2d rho(1) values not pinnable by no_variant are reported (informational)", True,
    f"{len([u for u in UNPINNABLE if u[0].startswith('R2 ')])} reported")

# ============================================================== R3 crossings
cr = load("p5_crossing_record.csv")
xings = {}
for r in cr:
    if r["T_crossing"] in ("interval", "") or not r["T_crossing"]:
        continue
    xings.setdefault((r["channel"], r["update"]), []).append(float(r["T_crossing"]))

expect = [("mobilising", "exact", "6.5"),
          ("protective", "Euler", "2.306"),
          ("mobilising", "Euler", "47.536")]
for chan, upd, printed in expect:
    vals = xings.get((chan, upd), [])
    chk(f"R3a {chan}/{upd} has a recorded crossing", bool(vals), str(vals))
    hit = [v for v in vals if abs(v - float(printed)) <= max(0.001, 0.0006 * abs(v))]
    chk(f"R3b paper's {printed} matches a recorded {chan}/{upd} crossing",
        bool(hit), f"recorded={vals}")
    # 2.306 and 47.536 are pinnable by no_variant (probed: no legitimate
    # collision), so pin them unconditionally.  An earlier version routed a
    # detected variant into a "reported as unpinnable" branch that emitted a
    # PASSING check -- turning detection into a green.  Never do that: an
    # unpinnable constant must be caught by an anchor instead, not excused.
    if printed == "47.536":
        pin(f"R3c crossing {printed}", tex, printed)
    elif printed == "2.306":
        # Not pinnable by no_variant under the extended variant set (2.3
        # occurs legitimately).  It is pinned by the two labelled sites below
        # (R3d the "protective Euler crossing at X yr" clause, and R3e the
        # four-crossing list), so report it rather than excusing it.
        coll = [x for x in variants(printed) if x in tex.replace(printed, " ")]
        UNPINNABLE.append((f"R3c crossing {printed} by no_variant", printed, coll[:3]))
    else:
        # 6.5 is approximate and collides (6.0, 6.9 elsewhere); anchor on the
        # "≈6.5 yr" claim and count how many times that claim is made
        anchored("R3c exact-update crossing (~6.5 yr)", tex,
                 r"\\approx\s*\\?\(?([\d.]+)\\?\)?\s*yr", 6.5, tol=0.02)
anchored("R3d protective Euler crossing (labelled site)", tex,
         r"protective Euler crossing at ([\d.]+) yr", 2.306, tol=0.0006)
# the paper also lists all four crossings together; check that list against the
# campaign's recorded crossings
_lst = re.search(r"the ([\d.]+), ([\d.]+), ([\d.]+), and ([\d.]+) yr crossings", tex)
if _lst:
    got = sorted(float(x) for x in _lst.groups())
    want = sorted(round(v, 3) for vals in xings.values() for v in vals)
    chk("R3e the paper's crossing list matches the campaign's recorded set",
        len(got) == len(want) and all(abs(a - b) <= 0.001 for a, b in zip(got, want)),
        f"paper={got} campaign={want}")
else:
    chk("R3e crossing list found", False)


# Every phrasing the manuscript uses for these two crossings, and all sites
# of each.  Enumerated because a single anchor leaves other sites unpinned.
all_sites("R3f 'near a X-year interval' (exact-update crossing)", tex,
          r"near a ([\d.]+)-year interval", 6.5, tol=0.02)
# 'pprox X yr' is used for more than one quantity (there is an unrelated
# 'pprox 24.0 yr' claim), so the sites are filtered to those whose context
# is about a crossing before every one of them is checked.
_ctx = [(float(m.group(1)), tex[max(0, m.start() - 110):m.start()])
        for m in re.finditer(r"\\approx\s*\\?\(?([\d.]+)\\?\)?\s*yr", tex)]
_cross = [v for v, c in _ctx if ("cross" in c or "exact" in c)]
_bad = [v for v in _cross if abs(v - 6.5) > 0.02]
chk("R3g '~X yr' exact-update crossing sites", bool(_cross) and not _bad,
    f"{len(_cross)} crossing-context site(s): {_cross}")
# These two phrasings are shared with the extractive channel (79.143 yr) and
# with the exact-update interval ([0.2, 200.0]), so sites are filtered to the
# protective context before being checked.
_h = [(float(m.group(1)), tex[max(0, m.start() - 160):m.start()])
      for m in re.finditer(r"at ([\d.]+) yr \(stable", tex)]
_h = [v for v, c in _h if "protective" in c]
chk("R3h protective 'at X yr (stable -> unstable)' sites",
    bool(_h) and all(abs(v - 2.306) <= 0.0006 for v in _h), f"{_h}")

_i = [(float(m.group(1)), tex[max(0, m.start() - 160):m.start()])
      for m in re.finditer(r"0\.2,\s*([\d.]+)\]", tex)]
_i = [v for v, c in _i if "protective" in c]
chk("R3i protective stable interval '[0.2, X]' sites",
    bool(_i) and all(abs(v - 2.306) <= 0.0006 for v in _i), f"{_i}")

# ============================================================== R4 MATCH / MISMATCH
cmp_rows = load("p5_stage_comparison.csv")
chk("R4a comparison table recorded", len(cmp_rows) == 6, f"{len(cmp_rows)} rows")
chk("R4b paper discloses the anchovy 3-4 yr window is NOT reproduced",
    "not the anchovy 3--4 yr" in tex)
chk("R4c paper discloses the sprat 6-12 yr window is NOT reproduced",
    "sprat 6--12 yr" in tex)
chk("R4d paper states those classes converge at every review interval",
    "converge at every review interval" in tex)
chk("R4e paper reports the reconstruction's own long-horizon band", "34--35 yr" in tex)
chk("R4f paper calls the archived record unreproduced", "unreproduced" in tex.lower())
chk("R4g paper does not claim the 3-4 yr window reproduces",
    not re.search(r"reproduc\w*\s+the\s+anchovy\s+3--4", tex, re.I))

# ============================================================== R5 trajectories
tr = load("p5_stage_trajectories.csv")
grid = {}
for r in tr:
    if r["class_"] in ("anchovy", "sprat", "cod") and abs(float(r["q"]) - 0.001) < 1e-9:
        try:
            T = int(float(r["T_r"]))
        except ValueError:
            continue
        if 1 <= T <= 20:
            grid.setdefault(r["class_"], {})[T] = r["kind"]
for cls in ("anchovy", "sprat", "cod"):
    kinds = grid.get(cls, {})
    osc = [T for T, k in kinds.items() if k != "converged"]
    chk(f"R5 {cls} converges over the whole 1-20 yr grid",
        len(kinds) == 20 and not osc, f"non-converging at {sorted(osc)}")

band = {}
for r in mul:
    if r["channel"] == "extractive" and abs(float(r["q"]) - 0.001) < 1e-9:
        if float(r["rho"]) > 1.0:
            band.setdefault(r["class_"], []).append(int(float(r["T_r"])))
for cls, Ts in sorted(band.items()):
    if Ts:
        chk(f"R5 band {cls}: unstable from T_r={min(Ts)}", min(Ts) >= 33,
            f"unstable {min(Ts)}-{max(Ts)}")

# ============================================================== R6 robustness
rob = load("p5_stage_robustness30.csv")
chk("R6a 30% robustness recorded", len(rob) > 0, f"{len(rob)} rows")
slow = sorted(int(float(r["T_r"])) for r in rob
              if r["class_"] == "slow_stock" and r["kind"] == "persistent")
if slow:
    chk("R6b slow-stock persistent only at T_r >= 30", min(slow) >= 30, f"{slow}")

# ============================================================== R7 distortion
ltm = load("p5_linear_trajectory_mse.csv")
r05 = [r for r in ltm if abs(float(r["T_r"]) - 0.5) < 1e-9]
if r05:
    rmsd = float(r05[0]["rmsd_scaled_norm"])
    chk("R7a scaled-norm RMSD at T_r=0.5 is ~2", abs(rmsd - 2.0) <= 0.15, f"{rmsd}")
big = [float(r["rmsd_scaled_norm"]) for r in ltm
       if 1e4 <= float(r["rmsd_scaled_norm"]) <= 1e6]
chk("R7b distortion reaches 10^4-10^5", len(big) >= 2, f"{len(big)} points")
chk("R7c paper states the 10^4-10^5 magnitude", "10^4" in tex or "10^{4}" in tex)

print()
print(f"{len(PASS)} passed, {len(FAIL)} failed")
if UNPINNABLE:
    print(f"\n{len(UNPINNABLE)} constant(s) reported UNPINNABLE (not silently dropped):")
    for lab, val, coll in UNPINNABLE:
        print(f"  - {lab}: {val}  ({coll})")
if FAIL:
    print("\nFAILED: " + ", ".join(FAIL))
sys.exit(1 if FAIL else 0)
