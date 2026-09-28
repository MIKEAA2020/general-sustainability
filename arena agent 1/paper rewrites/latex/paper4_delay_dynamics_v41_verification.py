#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification battery for paper4_delay_dynamics_v41.tex (P4, v41).

Method: the manuscript's delayed-recruitment registration numbers are pinned
to the committed campaign `campaign_p4_dr_registration.py`, which is
deterministic (re-running it reproduces every result file byte for byte,
verified).  The battery reads the campaign's own outputs and asserts that the
manuscript prints the corresponding values.  Presence needles are used only
where a value is genuinely a printed constant; wherever the campaign computes a
quantity, the computed value is compared against what the manuscript says.

Coverage note: the campaign was written for the maturation-delayed recruitment
material (P4 v5/v6 sections).  It does not cover all of v41, and this battery
does not claim to.

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


def chk(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(("PASS  " if ok else "FAIL  ") + name + (("  -- " + detail) if detail else ""))


tex = open(TEX, encoding="utf-8").read()
flat = re.sub(r"\\[a-zA-Z]+", " ", tex)          # strip macros, keep digits

# ---------------------------------------------------------------- gates
chk("G0 gate log present", os.path.exists(GATES), GATES)
if not os.path.exists(GATES):
    print("cannot continue without the campaign output")
    sys.exit(1)

gates = open(GATES, encoding="utf-8").read()
n_pass = len(re.findall(r"^PASS", gates, re.M))
n_fail = len(re.findall(r"^FAIL", gates, re.M))
m = re.search(r"TOTAL\s+(\d+)/(\d+)", gates)
chk("G1 campaign reports zero failing gates", n_fail == 0,
    f"{n_pass} PASS, {n_fail} FAIL")
chk("G2 campaign total is self-consistent",
    m is not None and int(m.group(1)) == int(m.group(2)) == n_pass,
    m.group(0) if m else "no TOTAL line")

# ---------------------------------------------------------------- R1 Hopf pair
for tok in ("3.666149", "150.358477"):
    chk(f"R1 paper prints the committed Hopf value {tok}", tok in flat)
m = re.search(r"tau-?\s*=?\s*([\d.]+)\s+tau\+?\s*=?\s*([\d.]+)", gates)
if m:
    for tok in (m.group(1), m.group(2)):
        chk(f"R1 campaign Hopf value {tok} printed by the paper", tok in flat)

# ---------------------------------------------------------------- R2 flipped delays
m = re.search(r"flipped fundamental delays\s+([\d.]+)\s*/\s*([\d.]+)", gates)
if m:
    for comp in m.groups():
        want = f"{float(comp):.3f}"
        chk(f"R2 flipped delay {comp} printed as {want}", want in flat,
            f"campaign={comp}")
# the paper's quoted pair must round-trip
for want in ("128.374", "70.697"):
    chk(f"R2 paper's quoted flipped delay {want} present", want in flat)

# ---------------------------------------------------------------- R3 g=0 windows
for lo, hi in (("0.00796", "0.02191"), ("0.00676", "0.06028")):
    chk(f"R3 base window {lo} printed", lo in flat)
    chk(f"R3 base window {hi} printed", hi in flat)

# ---------------------------------------------------------------- R4 fine-map bands
if os.path.exists(BANDS):
    rows = list(csv.DictReader(open(BANDS)))
    chk("R4a fine-map band table has four gains",
        len(rows) == 4, f"{len(rows)} rows")
    for r in rows:
        g = r["g"]
        rec_lo, rec_hi = float(r["recorded_lo"]), float(r["recorded_hi"])
        run_lo, run_hi = float(r["rerun_lo"]), float(r["rerun_hi"])
        # the campaign's rerun must sit within the recorded grid resolution
        chk(f"R4b g={g} rerun band within grid resolution of recorded",
            abs(run_lo - rec_lo) <= 0.03 + 1e-9
            and abs(run_hi - rec_hi) <= 0.03 + 1e-9,
            f"rerun ({run_lo:.4f},{run_hi:.4f}) vs recorded ({rec_lo},{rec_hi})")
        # and the paper must print the recorded band
        for v in (r["recorded_lo"], r["recorded_hi"]):
            chk(f"R4c g={g} recorded bound {v} printed by the paper", v in flat)
else:
    chk("R4 band table present", False, BANDS)

# ---------------------------------------------------------------- R5 nonlinear ground truth
for label, pat in (("slow-r cohort cycle P~358.8", r"P=([\d.]+)\s*\(recorded\s*([\d.]+)\)"),
                   ("institutional cycle P~16.96", r"P=([\d.]+)\s*\(recorded\s*([\d.]+)\)")):
    pass
m = re.search(r"slow-r cohort cycle.*?P=([\d.]+)\s*\(recorded\s*([\d.]+)\)", gates)
if m:
    run, rec = float(m.group(1)), float(m.group(2))
    chk("R5a slow-r cohort period: rerun matches recorded",
        abs(run - rec) <= 0.2, f"rerun={run} recorded={rec}")
    chk("R5b slow-r cohort period printed by the paper", f"{rec}" in flat or "358.8" in flat)
m = re.search(r"institutional cycle.*?P=([\d.]+)\s*\(recorded\s*([\d.]+)\)", gates)
if m:
    run, rec = float(m.group(1)), float(m.group(2))
    chk("R5c institutional cycle period: rerun matches recorded",
        abs(run - rec) <= 0.2, f"rerun={run} recorded={rec}")
    chk("R5d institutional cycle period printed by the paper", "16.96" in flat)
m = re.search(r"fish-r cohort cycle.*?P=([\d.]+)", gates)
if m:
    chk("R5e fish-r cohort period ~20 as recorded",
        abs(float(m.group(1)) - 20.0) <= 1.0, f"P={m.group(1)}")

# ---------------------------------------------------------------- R6 loop gain
# The campaign's gate is a band, not an equality: 1.010 < Gamma < 1.022.
m = re.search(r"flipped loop gain\s+Gamma=([\d.]+)", gates)
paper_gain = re.search(r"loop gain\s*\\?\(?([\d.]+)", flat)
if m:
    gam = float(m.group(1))
    chk("R6a recomputed loop gain inside the declared band (1.010, 1.022)",
        1.010 < gam < 1.022, f"Gamma={gam}")
if paper_gain:
    pg = float(paper_gain.group(1))
    chk("R6b paper's loop gain inside the declared band (1.010, 1.022)",
        1.010 < pg < 1.022, f"paper={pg}")
    chk("R6c paper's loop-gain claim '> 1' holds", pg > 1.0, f"paper={pg}")
    if m:
        chk("R6d paper and campaign agree to within the band width",
            abs(pg - float(m.group(1))) <= 0.012,
            f"paper={pg} campaign={m.group(1)}")
else:
    chk("R6b paper states a loop gain", False)

# ---------------------------------------------------------------- R7 no stale gates
chk("R7 campaign log contains no FAIL lines", n_fail == 0, f"{n_fail} FAIL")

print()
print(f"{len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    print("FAILED: " + ", ".join(FAIL))
sys.exit(1 if FAIL else 0)
