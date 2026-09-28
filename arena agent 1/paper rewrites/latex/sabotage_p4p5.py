#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Falsifiability harness for the P4 and P5 verification batteries.

A green battery is not evidence.  For each battery this copies the paper
directory to a temp location, perturbs one load-bearing number in the tex
(last-digit flip), runs the COPY of the battery, and checks that the battery
FAILS.  A mutation the battery does not catch is a blind spot, and is reported
as a finding rather than suppressed.

Note: the batteries resolve their tex via __file__, so the COPY inside the
mutation directory must be executed -- running the original path would re-read
the unmutated manuscript and report every mutation as caught.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

WORK = "/home/user"

CASES = {
    "P4": {
        "dir": "fam/p4",
        "tex": "paper4_delay_dynamics_v41.tex",
        "battery": "paper4_delay_dynamics_v41_verification.py",
        # each token must be present in the tex and load-bearing
        "mutations": [
            ("3.666149", "3.666150"),     # committed Hopf pair, lower branch
            ("150.358477", "150.358479"), # committed Hopf pair, upper branch
            ("128.374", "128.379"),       # flipped fundamental delay
            ("70.697", "70.692"),
            ("0.00796", "0.00799"),       # g=0 base window, eta=0.914
            ("0.06028", "0.06025"),       # g=0 base window, eta=3.0
            ("1.016", "1.0169"),          # loop gain (also tests the band logic)
            ("358.8", "358.3"),           # slow-r cohort period
            ("16.96", "16.92"),           # institutional cycle period
        ],
    },
    "P5": {
        "dir": "fam/p5",
        "tex": "paper5_sampled_governance_v47_blinded_NatSustain.tex",
        "battery": "paper5_sampled_governance_v47_verification.py",
        "mutations": [
            ("0.895", "0.897"),   # rho(1) anchovy
            ("0.923", "0.925"),   # rho(1) sprat
            ("0.956", "0.958"),   # rho(1) cod
            ("0.994", "0.996"),   # rho(1) slow-stock
            ("2.0896", "2.0899"), # plant-independent equilibrium E*
            ("6.5", "6.2"),       # exact-update crossing
            ("2.306", "2.309"),   # protective Euler crossing
            ("47.536", "47.539"), # mobilising Euler crossing
        ],
    },
}

results = {}
for paper, cfg in CASES.items():
    src = os.path.join(WORK, cfg["dir"])
    tex = os.path.join(src, cfg["tex"])
    original = open(tex, encoding="utf-8").read()

    print(f"\n===== {paper} =====")
    rows = []
    for old, new in cfg["mutations"]:
        n = original.count(old)
        if n == 0:
            print(f"  SKIP  {old!r} not present in the manuscript")
            rows.append({"mutation": f"{old}->{new}", "status": "SKIP", "n": 0})
            continue

        tmp = tempfile.mkdtemp(prefix=f"{paper}_mut_")
        dst = os.path.join(tmp, os.path.basename(src))
        shutil.copytree(src, dst)
        dtex = os.path.join(dst, cfg["tex"])
        body = open(dtex, encoding="utf-8").read()
        assert body.count(old) == n
        open(dtex, "w", encoding="utf-8").write(body.replace(old, new, 1))

        proc = subprocess.run([sys.executable, cfg["battery"]],
                              cwd=dst, capture_output=True, text=True, timeout=600)
        out = proc.stdout + proc.stderr
        m = re.search(r"(\d+) passed, (\d+) failed", out)
        npass = int(m.group(1)) if m else -1
        nfail = int(m.group(2)) if m else -1
        caught = proc.returncode != 0
        status = "CAUGHT" if caught else "MISSED"
        print(f"  {status}  {old} -> {new}  (exit {proc.returncode}, "
              f"{npass} passed / {nfail} failed, {n} occurrence(s))")
        if not caught and nfail > 0:
            print("        (battery counted failures but still exited 0 -- "
                  "exit-line defect)")
        rows.append({"mutation": f"{old}->{new}", "status": status,
                     "exit": proc.returncode, "n_pass": npass,
                     "n_fail": nfail, "n": n})
        shutil.rmtree(tmp, ignore_errors=True)

    missed = [r for r in rows if r["status"] == "MISSED"]
    skipped = [r for r in rows if r["status"] == "SKIP"]
    caught = [r for r in rows if r["status"] == "CAUGHT"]
    print(f"  -- {len(caught)} caught, {len(missed)} MISSED, {len(skipped)} skipped")
    results[paper] = {"rows": rows, "caught": len(caught),
                      "missed": len(missed), "skipped": len(skipped)}

print()
print("=" * 60)
for paper, r in results.items():
    print(f"{paper}: {r['caught']} caught / {r['missed']} MISSED / {r['skipped']} skipped")
    for row in r["rows"]:
        if row["status"] == "MISSED":
            print(f"   BLIND SPOT: {row['mutation']}")

json.dump(results, open("/home/user/sabotage_p4p5.json", "w"), indent=1)
print("\nwritten: /home/user/sabotage_p4p5.json")
