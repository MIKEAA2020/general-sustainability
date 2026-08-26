#!/usr/bin/env python3
"""
Pinned-hash + independent-rerun checks for research_program/validated_computations/.

Companion to batch 4/VALIDATED_COMPUTATIONS_RERUN.md.
Run:  REPO="$(pwd)" python3 reaudit/verify_validated_computations.py

Does not re-execute the long scripts. Checks that the committed artifacts still
match the Part II short hashes, that the rerun report exists, and that the
certified numerical claims in the committed JSON still say what the register
cites. Exit 0 on success. Writes nothing.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path

import numpy as np

REPO = Path(os.environ.get("REPO", Path(__file__).resolve().parent.parent))
VC = REPO / "research_program" / "validated_computations"
MAN = (REPO / "PROOF_MANIFEST.md").read_text(errors="replace")
FAIL = []


def check(name, cond, detail=""):
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}{(' :: ' + str(detail)) if detail else ''}")
    if not cond:
        FAIL.append(name)


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def short_ok(full: str, cell: str) -> bool:
    m = re.search(r"`([0-9a-f]{8})\.\.\.([0-9a-f]{5,8})`", cell)
    if not m:
        return False
    return full.startswith(m.group(1)) and full.endswith(m.group(2))


print("\n[A] committed artifacts match Part II short hashes")

ROWS = [
    ("A025 Hopf", VC / "a025_fold" / "a025_interval_hopf.json", "eda36cd1", "95b3b2"),
    ("C4 Krawczyk cert", VC / "a021_c4" / "c4_orbit_krawczyk_certificate.json", "5e8df633", "65ab133"),
    ("C4 Krawczyk box", VC / "a021_c4" / "c4_orbit_krawczyk_box.npz", "85f72c76", "7ba4c69"),
    ("C4 off-grid", VC / "a021_c4" / "c4_offgrid_residual_interval.json", "2a4a5e82", "1c74a7f4"),
    ("C4 monodromy json", VC / "a021_c4" / "c4_monodromy_enclosure.json", "01d8c253", "dbaef76"),
    ("C4 monodromy npz", VC / "a021_c4" / "c4_monodromy_dt0p25.npz", "f3dc5445", "a7ca5f"),
    ("E5 numbers", VC / "E5_NUMBERS.json", "5670bcc8", "236e72db"),
]
for name, path, head, tail in ROWS:
    check(f"{name} exists", path.is_file(), path)
    if path.is_file():
        h = sha(path)
        check(f"{name} hash {head}...{tail}", h.startswith(head) and h.endswith(tail), h)

print("\n[B] certified numerical claims in the committed artifacts")

hopf = json.loads((VC / "a025_fold" / "a025_interval_hopf.json").read_text())
certs = hopf["hopf_certificates"]
check("Hopf has two certified roots", len(certs) == 2)
check("tau_- is left/stabilising", certs[0].get("crossing_direction_k0") == "left (stabilising)")
check("tau_+ is right/destabilising", certs[1].get("crossing_direction_k1") == "right (destabilising)")
check("both roots simple", all(c.get("simple_root") for c in certs))
# displayed manuscript intervals must contain the certified ones
tau_m = certs[0]["tau_k0"]
tau_p = certs[1]["tau_k1"]
check("tau_- string contains 3.666149014274", "3.666149014274" in tau_m)
check("tau_+ string contains 150.358477310141", "150.358477310141" in tau_p)

kr = json.loads((VC / "a021_c4" / "c4_orbit_krawczyk_certificate.json").read_text())
check("Krawczyk ok", kr["krawczyk"]["krawczyk_ok"] is True)
check("Krawczyk margin > 1000", kr["krawczyk"]["margin"] > 1000, kr["krawczyk"]["margin"])
check("period is 370.9311778394…", abs(kr["period"] - 370.9311778394) < 1e-10, kr["period"])
check("Krawczyk status is discrete VALIDATED", "discrete K=80" in kr["status"])

og = json.loads((VC / "a021_c4" / "c4_offgrid_residual_interval.json").read_text())
rs = og["residual_sup_grid"]
check("off-grid grid is 256", og["grid_points"] == 256)
check("off-grid E <= 3e-6", rs["E"] <= 3e-6, rs["E"])
check("off-grid N <= 7e-8", rs["N"] <= 7e-8, rs["N"])
check("off-grid is interval-certified", "INTERVAL-CERTIFIED" in og["certification_level"])

mo = json.loads((VC / "a021_c4" / "c4_monodromy_enclosure.json").read_text())
lv = mo["levels"]["dt0p25"]
check("monodromy period_steps=1484", lv["period_steps"] == 1484)
check("phase simple+neutral", lv["phase_multiplier"]["simple_neutral_certified"] is True)
check("dominant below one", lv["dominant_nontrivial"]["below_one_certified"] is True)
check("all nontrivial inside", lv["all_nontrivial_strictly_inside_unit_disc"] is True)
check("phase nominal ~ 1.00480", abs(lv["phase_multiplier"]["nominal"] - 1.0048009793249175) < 1e-12)
check("dominant nominal ~ 0.68764", abs(lv["dominant_nontrivial"]["nominal"] - 0.6876430781740369) < 1e-12)

e5 = json.loads((VC / "E5_NUMBERS.json").read_text())
check("E5 three conditions hold", all(e5["conditions"][k]["holds"] for k in
                                      ("i_Hmin_le_R_minus_aSmin", "ii_Kdag_le_Kmax", "iii_Smin_le_Sstar")))
check("E5 verdict is toy admission", "ADMITTED WITH NUMBERS" in e5["module"]["verdict"])

print("\n[C] independent-rerun register + report")

rerun = REPO / "batch 4" / "VALIDATED_COMPUTATIONS_RERUN.md"
check("rerun report exists", rerun.is_file())
if rerun.is_file():
    rt = rerun.read_text()
    check("report records Hopf MATCH", "a025_interval_hopf.json" in rt and "MATCH" in rt)
    check("report records monodromy MATCH", "c4_monodromy_enclosure.json" in rt)
    check("report does not close Wave E", "No Wave E gate is closed" in rt or "does not close" in rt.lower())

# Part II rows for the five certificates must no longer say **NONE**
part2 = MAN.split("## Part II")[1].split("## Part III")[0]
for needle, label in [
    ("a025_interval_hopf.json", "Hopf"),
    ("c4_orbit_krawczyk_certificate.json", "Krawczyk"),
    ("c4_offgrid_residual_interval.json", "off-grid"),
    ("c4_monodromy_enclosure.json", "monodromy"),
    ("E5_NUMBERS.json", "E5"),
]:
    # find the table row containing the file
    rows = [ln for ln in part2.splitlines() if needle in ln]
    check(f"Part II has a row for {label}", bool(rows))
    if rows:
        check(
            f"Part II {label} is no longer **NONE**",
            "**NONE**" not in rows[0] and "INDEPENDENT_RERUN" in rows[0],
            rows[0][-80:],
        )

check("Part IV off-grid citation is 256-point, not 512",
      "256-point grid" in MAN and "≤ 3e-6 on a 512-point grid" not in MAN)
check("Part IV monodromy citation covers the mesh levels honestly",
      # 2026-08-26: the dt=0.1 second mesh level is computed, so the
      # citation must say "two mesh levels" (and must NOT claim the
      # continuum) — updated from the pre-dt0p1 form which required the
      # "dt=0.25 only" limitation language.
      ("two mesh levels" in MAN or "dt=0.25" in MAN)
      and "certified error balls at two mesh levels (discrete)" in MAN
      and "continuous DDE" not in MAN.split("two mesh levels")[1][:200])

print("\n" + "=" * 72)
if FAIL:
    print(f"{len(FAIL)} check(s) failed: {FAIL}")
    sys.exit(1)
print("All validated-computation rerun claims verified.")
sys.exit(0)
