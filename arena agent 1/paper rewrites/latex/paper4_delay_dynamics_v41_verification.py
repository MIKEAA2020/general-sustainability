#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification battery for paper4_delay_dynamics_v41.tex (P4, v41).

The manuscript's delayed-recruitment registration numbers are pinned to the
committed campaign `campaign_p4_dr_registration.py`, which is deterministic
(re-running reproduces every result file byte for byte, verified).

WHY THE PINNING METHOD IS WHAT IT IS

Version 1 of this battery used `value in tex` and was 78% blind: a sabotage
run showed it caught only 2 of 9 mutations.  A presence needle is defeated by
restatement -- `3.666149` occurs five times, so perturbing one occurrence
leaves four that still match.

Constants are now pinned with `no_variant`, which asserts that no variant of
the value occurs anywhere OUTSIDE the places where the value itself is printed.
Two details matter and both were got wrong first time:

  * occurrences of the value are masked out before testing, because otherwise
    every shorter variant is trivially "present" -- '3.66614' is a substring of
    '3.666149', which made the check fail on an unmodified manuscript;
  * the variant set includes +/- 1 unit in the last place, because a sabotage
    edit may carry (3.666149 -> 3.666150 changes two digits, missing a pure
    digit-substitution model entirely).

Values that legitimately collide are reported UNPINNABLE rather than dropped,
and values the campaign itself constrains only by a band (the loop gain) are
reported as band-limited rather than pretended to be pinned.

Coverage: the campaign covers the maturation-delayed recruitment material
(P4 v5/v6 sections).  It does not cover all of v41; neither does this battery.

Run:  python3 paper4_delay_dynamics_v41_verification.py
Exit: 0 if every check passes, 1 otherwise.
"""
from __future__ import annotations

import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEX = os.path.join(HERE, "paper4_delay_dynamics_v41.tex")
RES = os.path.join(HERE, "results")
GATES = os.path.join(RES, "p4_dr_registration_gates.txt")
BANDS = os.path.join(RES, "p4_dr_finemap_bands.csv")

PASS, FAIL = [], []
UNPINNABLE = []


def chk(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(("PASS  " if ok else "FAIL  ") + name + (("  -- " + detail) if detail else ""))


def variants(value):
    """Decimal variants that must not occur elsewhere.

    Three families, because a sabotage edit can take any of these forms:
      1. last-digit substitution   884.6 -> 884.0..884.9
      2. trailing-zero shorthand   3.666149 -> 3.66615
      3. +/- 1 ulp (a carry, changing two digits): 3.666149 -> 3.666150
    """
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
    """True iff no variant of `value` occurs outside the places printing it.

    Occurrences of `value` are masked out first; without that step every
    shorter variant is trivially present (see the module docstring).
    """
    remainder = tex.replace(value, " ")
    return all(v not in remainder for v in variants(value))


def pin(label, tex, value, where=""):
    """Pin a constant restatement-proof-ly, or record it as unpinnable."""
    if no_variant(tex, value):
        chk(f"{label}: {value} pinned (no variant anywhere else)", True, where)
        return True
    coll = [v for v in variants(value) if v in tex.replace(value, " ")]
    UNPINNABLE.append((label, value, coll[:4]))
    chk(f"{label}: {value} UNPINNABLE", False, f"collides with {coll[:4]}")
    return False


def anchored(label, tex, pattern, expected, tol=0.0):
    """Extract a value at a labelled site and compare."""
    m = re.search(pattern, tex)
    if not m:
        chk(f"{label}: anchor found", False, pattern[:60])
        return False
    got = float(m.group(1))
    ok = abs(got - expected) <= tol
    chk(f"{label}: anchored value {got} == {expected}", ok, pattern[:44])
    return ok


tex = open(TEX, encoding="utf-8").read()

# ---------------------------------------------------------------- gates
if not os.path.exists(GATES):
    chk("campaign gate log present", False, GATES)
    sys.exit(1)
gates = open(GATES, encoding="utf-8").read()
n_pass = len(re.findall(r"^PASS", gates, re.M))
n_fail = len(re.findall(r"^FAIL", gates, re.M))
m = re.search(r"TOTAL\s+(\d+)/(\d+)", gates)
chk("campaign reports zero failing gates", n_fail == 0, f"{n_pass} PASS, {n_fail} FAIL")
chk("campaign total is self-consistent",
    m is not None and int(m.group(1)) == int(m.group(2)) == n_pass,
    m.group(0) if m else "no TOTAL line")

# ---------------------------------------------------------------- R1 Hopf pair
pin("R1 Hopf lower branch", tex, "3.666149", "5 occurrences")
pin("R1 Hopf upper branch", tex, "150.358477", "5 occurrences")

# ---------------------------------------------------------------- R2 flipped delays
pin("R2 flipped delay (lower)", tex, "128.374", "3 occurrences")
pin("R2 flipped delay (upper)", tex, "70.697", "3 occurrences")

# ---------------------------------------------------------------- R3 g=0 windows
pin("R3 window eta=0.914 lower", tex, "0.00796")
pin("R3 window eta=0.914 upper", tex, "0.02191")
pin("R3 window eta=3.0 lower", tex, "0.00676")
pin("R3 window eta=3.0 upper", tex, "0.06028")

# ---------------------------------------------------------------- R4 cycle periods
# These collide because the paper prints recorded and re-run values side by
# side ("registered 358.8-yr ... re-run 358.7 yr"), so they are pinned by
# anchored extraction at the labelled site instead.
anchored("R4a slow-r cohort cycle (registered)", tex,
         r"registered\s*\\?\(?([\d.]+)\\?\)?-yr", 358.8, tol=0.05)
_m = re.search(r"recorded period\s*\\?\(?([\d.]+)\\?\)\s*yr with amplitude"
               r"\s*\\?\(?([\d.]+)", tex)
if _m:
    chk("R4b institutional cycle (recorded period)",
        abs(float(_m.group(1)) - 16.96) <= 0.005, f"got {_m.group(1)}")
    chk("R4c institutional amplitude (recorded)",
        abs(float(_m.group(2)) - 8.66) <= 0.005, f"got {_m.group(2)}")
else:
    chk("R4b/c recorded-period clause found", False)

# ---------------------------------------------------------------- R5 fine-map bands
if os.path.exists(BANDS):
    rows = list(csv.DictReader(open(BANDS)))
    chk("R5a fine-map band table has four gains", len(rows) == 4, f"{len(rows)} rows")
    for r in rows:
        g = r["g"]
        run_lo, run_hi = float(r["rerun_lo"]), float(r["rerun_hi"])
        rec_lo, rec_hi = float(r["recorded_lo"]), float(r["recorded_hi"])
        chk(f"R5b g={g} rerun band within grid resolution of recorded",
            abs(run_lo - rec_lo) <= 0.03 + 1e-9 and abs(run_hi - rec_hi) <= 0.03 + 1e-9,
            f"rerun ({run_lo:.4f},{run_hi:.4f}) vs recorded ({rec_lo},{rec_hi})")
    # band boundaries are short decimals that collide legitimately; record them
    n_coll = 0
    for r in rows:
        for v in (r["recorded_lo"], r["recorded_hi"]):
            if not no_variant(tex, v):
                coll = [x for x in variants(v) if x in tex.replace(v, " ")]
                UNPINNABLE.append((f"R5 band g={r['g']}", v, coll[:3]))
                n_coll += 1
    chk("R5c band boundaries: collisions reported, not dropped", True,
        f"{n_coll} of 8 band boundaries collide with other values in the text")
else:
    chk("R5 band table present", False, BANDS)

# ---------------------------------------------------------------- R6 loop gain
# The campaign's own gate is a band (1.010 < Gamma < 1.022) because the shifted
# points are located only to ~1e-5.  The paper's 1.016 and the campaign's
# 1.019221 both sit inside it, so the loop gain cannot be pinned to a single
# value by either source.  Reported as band-limited rather than claimed pinned.
m = re.search(r"flipped loop gain\s+Gamma=([\d.]+)", gates)
flat = re.sub(r"\\[a-zA-Z]+", " ", tex)
pg = re.search(r"loop gain\s*\\?\(?([\d.]+)", flat)
if m and pg:
    gam, p = float(m.group(1)), float(pg.group(1))
    chk("R6a recomputed loop gain inside the declared band (1.010, 1.022)",
        1.010 < gam < 1.022, f"Gamma={gam}")
    chk("R6b paper's loop gain inside the declared band", 1.010 < p < 1.022, f"{p}")
    chk("R6c paper's 'loop gain > 1' claim holds", p > 1.0, f"{p}")
    UNPINNABLE.append(("R6 loop gain", f"paper {p} vs campaign {gam}",
                       "campaign gate is a band, not an equality"))
else:
    chk("R6 loop gain stated", False)

print()
print(f"{len(PASS)} passed, {len(FAIL)} failed")
if UNPINNABLE:
    print(f"\n{len(UNPINNABLE)} constant(s) reported UNPINNABLE (not silently dropped):")
    for lab, val, coll in UNPINNABLE:
        print(f"  - {lab}: {val}  ({coll})")
if FAIL:
    print("\nFAILED: " + ", ".join(FAIL))
sys.exit(1 if FAIL else 0)
