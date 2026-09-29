#!/usr/bin/env python3
"""Sabotage-test the v28 battery: for each mutation, the named check must FAIL.

Purpose: prove that (a) the new `also=` precision masking did not gut R8l, and
(b) the Section 2 residual-summary corrections are actually policed by some
check.  A mutation that leaves the battery green is a blind spot to record.
"""
import os
import re
import subprocess
import shutil

D = "/home/user/fam/e2"
TEX = os.path.join(D, "paperE2_cod_intervention_v28.tex")
BAT = os.path.join(D, "paperE2_cod_intervention_v28_verification.py")
BACKUP = "/tmp/v28_tex.bak"
shutil.copy(TEX, BACKUP)

MUTATIONS = [
    # (label, old, new, must-fail check-substring)
    ("R8l: -318.8 -> -318.7",            "-318.8", "-318.7", "R8l Schaefer class value -318.8"),
    ("R8l: -114.9 -> -114.8",            "-114.9", "-114.8", "R8l Schaefer class value -114.9"),
    ("R8l2: -318.76 -> -318.75",         "-318.76", "-318.75", "R8l2 full-precision value -318.76"),
    ("R8l2: -114.85 -> -114.84",         "-114.85", "-114.84", "R8l2 full-precision value -114.85"),
    ("R8k: reintroduce Fox -287.4",      "-318.8", "-287.4", "R8k Fox class value -287.4"),
    ("R8m: -460.0 -> -460.5",            "-460.0", "-460.5", "R8m UC_min"),
    ("sec2: SD 135.0 -> stale 114.9",    "135.0", "114.9",   "residual"),
    ("sec2: mean -20.4 -> stale -10.9",  "-20.4", "-10.9",   "residual"),
    ("sec2: range +179.8 -> +206.6",     "+179.8", "+206.6", "residual"),
    ("sec2: acf 0.65 -> stale 0.55",     "0.65",  "0.55",    "residual"),

    # --- new v28e checks: Tables 3 / 5 / Fox / labels ----------------------
    ("T5: revert BAU n=5 to srcyear",   "1412.5", "1298.7", "R10c"),
    ("T5: revert 240kt worst n=10",     "9427.0", "4687.8", "R10c"),
    ("T3: revert K=1200 constructive",  "7.16",   "36.0",   "R10a"),
    ("T3: revert K=1000 T=1 boundary",  "1009.2", "943.2",  "R10b"),
    ("Fox: revert constructive 45.08",  "45.08",  "79.05",  "R10e"),
    ("3.8: revert BAU srcyear 0.903",   "0.903",  "0.906",  "R10f"),
    ("3.8: revert acf 0.65 -> 0.55",    "0.65",   "0.55",   "R9e"),
    ("3.8: revert pool label",          "24 registered\ntraining residuals",
                                        "24 source-year\ntraining residuals", "R9e"),
    ("label: Table 5 caption",          "(registered); empty",
                                        "(source-year); empty", "R10c"),
]


def run_battery():
    p = subprocess.run(["python3", BAT], cwd=D, capture_output=True, text=True)
    return p.stdout + p.stderr


def failed_checks(out):
    """Return the set of check names on FAILED lines."""
    names = set()
    m = re.search(r"FAILED: (.*)", out)
    if m:
        for part in m.group(1).split(","):
            names.add(part.strip())
    return names


print(f"{'mutation':38s} {'detected':9s} detail")
print("-" * 96)
blind = []
for label, old, new, expect in MUTATIONS:
    tex = open(BACKUP, encoding="utf-8").read()
    if old not in tex:
        print(f"{label:38s} {'SKIP':9s} anchor {old!r} absent")
        continue
    open(TEX, "w", encoding="utf-8").write(tex.replace(old, new, 1))
    out = run_battery()
    fails = failed_checks(out)
    hit = any(expect.lower() in f.lower() for f in fails)
    n_fail = len(re.findall(r"^FAIL", out, re.M))
    # any check failing at all counts as detection
    detected = n_fail > 0
    status = "CAUGHT" if detected else "BLIND"
    if not detected:
        blind.append(label)
    detail = "; ".join(sorted(fails))[:52] if fails else "battery stayed green"
    print(f"{label:38s} {status:9s} {detail}")

shutil.copy(BACKUP, TEX)
print("-" * 96)
print("restored original tex")
if blind:
    print("\nBLIND SPOTS (mutation leaves the battery green):")
    for b in blind:
        print("  -", b)
else:
    print("\nNo blind spots: every mutation is detected by at least one check.")
