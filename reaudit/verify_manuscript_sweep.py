#!/usr/bin/env python3
"""
Manuscript-side consistency sweep over revised_articles/.

Companion to verify_consistency.py (the tree-side grep). PROOF_MANIFEST.md
Part VII: "the manuscript-side sweep is the same check run over
revised_articles/ and is recommended before each paper is finalised."

Run from the repository root:
    REPO="$(pwd)" python3 reaudit/verify_manuscript_sweep.py

Section A: the same discipline checks as verify_consistency.py §A,
           scoped to revised_articles/ only.
Section B: C3-style vocabulary (computations labelled as proofs).
Section C: how the Part II validated-computation artifacts are cited.
Exit 0 => every check holds. Writes nothing.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

REPO = Path(os.environ.get("REPO", Path(__file__).resolve().parent.parent))
ART = REPO / "revised_articles"
FAIL = []


def check(name, cond, detail=""):
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}{(' :: ' + str(detail)) if detail else ''}")
    if not cond:
        FAIL.append(name)


def files():
    return sorted(p for p in ART.iterdir() if p.suffix in (".md", ".tex"))


def grep_all(pattern, flags=re.I):
    rx = re.compile(pattern, flags)
    hits = []
    for p in files():
        for i, ln in enumerate(p.read_text(errors="replace").splitlines()):
            if rx.search(ln):
                hits.append((p.name, i + 1, ln.strip()))
    return hits


NEG = re.compile(
    r"\b(never|not|no |cannot|does not|is not|forbidden|prohibit|withdrawn|"
    r"unavailable|zero |\bNOT\b|do not|does not)",
    re.I,
)

print("\n[A] same discipline checks, scoped to revised_articles/")

FORBIDDEN = [
    "continuum orbit exists",
    "bunching inequality closes",
    r"persistence theorem.{0,40}hypothes.{0,20}verif",
    "decidable against the calibrated",
    "fold is certified for the continuous",
]
for pat in FORBIDDEN:
    hits = grep_all(pat)
    if pat == "bunching inequality closes":
        hits = [h for h in hits if "numerical" not in h[2].lower()]
    asserted = [h for h in hits if not NEG.search(h[2])]
    check(
        f"Part-V forbidden claim never ASSERTED: /{pat}/",
        not asserted,
        asserted[:2] or f"0 assertions ({len(hits)} mentions)",
    )

e5 = grep_all(r"\bE5\b")
bad_e5 = [
    h
    for h in e5
    if re.search(r"E5.{0,60}(transfer|applies to).{0,40}(2J3KL|Edwards|real system)", h[2], re.I)
    and "not" not in h[2].lower()
    and "no transfer" not in h[2].lower()
    and "does not" not in h[2].lower()
]
check("no unqualified E5 -> real-system transfer claim", not bad_e5, bad_e5[:2] or "clean")

tcs = [
    h
    for h in grep_all(r"TCS-1\.1|TCS_1_1")
    if re.search(r"(controlling|conforms? to|valid under|compatible with)[^.;]{0,15}TCS-1\.1", h[2], re.I)
    and not NEG.search(h[2])
]
check("no document asserts TCS-1.1 is controlling", not tcs, tcs[:2] or "0 assertions")

refuted = ["A3.Thm1", "B6.Thm1", "E4.Thm2", "E4.Lem1"]
CORRECTIVE = re.compile(
    r"refut|repair|withdraw|false|incorrect|corrected|superseded|session record|not.*claim",
    re.I,
)
leaks = [
    h
    for t in refuted
    for h in grep_all(re.escape(t))
    if not CORRECTIVE.search(h[2])
]
check("item-1 refutations not cited as proved", not leaks, leaks[:3] or "contained")

print("\n[B] C3-style: computations labelled as proofs")

# Manifest vocabulary reserved for formal proofs, applied to a computation.
c3 = []
for h in grep_all(r"\bPROVEN\b|\bVALIDATED\b|INTERVAL-CERTIFIED"):
    if re.search(r"\b(not|never|no )\b.{0,20}(PROVEN|VALIDATED|INTERVAL-CERTIFIED)", h[2], re.I):
        continue
    # "interval-certified crossings/pair/delays" is the Part IV citation form,
    # not the reserved PROVEN status. Flag only the reserved tokens or a
    # computation labelled PROVEN.
    if re.search(r"\bPROVEN\b", h[2]) or re.search(
        r"Committed and (PROVEN|VALIDATED|INTERVAL-CERTIFIED)", h[2]
    ):
        c3.append(h)
check(
    "no manuscript uses reserved PROVEN/Committed-and-* for a computation",
    not c3,
    c3[:3] or "clean",
)

# Fold must not be called interval-certified / validated.
fold_over = [
    h
    for h in grep_all(r"fold")
    if re.search(r"interval[- ]certified.{0,40}fold|certified fold|validated fold theorem", h[2], re.I)
    and not NEG.search(h[2])
    and "not" not in h[2].lower()
]
check("no manuscript asserts a certified/validated fold", not fold_over, fold_over[:2] or "clean")

print("\n[C] Part II artifact citation (informational + one hard check)")

hopf_hits = grep_all(r"3\.666149")
check(
    "A025/A018/A020 display the certified Candidate-A tau_- enclosure",
    any("A025" in h[0] for h in hopf_hits)
    and any("A018" in h[0] for h in hopf_hits)
    and any("A020" in h[0] for h in hopf_hits),
    f"{len(hopf_hits)} lines across {sorted({h[0] for h in hopf_hits})}",
)

# A025 must not still say the pipeline has not been independently reproduced
# once the rerun report exists. This check is informational if the report is
# absent; hard once batch 4/VALIDATED_COMPUTATIONS_RERUN.md is present.
rerun = REPO / "batch 4" / "VALIDATED_COMPUTATIONS_RERUN.md"
stale = grep_all(r"does not yet contain an independently reproduced")
if rerun.exists():
    check(
        "A025 no longer claims the Hopf pipeline is unreproduced (rerun report exists)",
        not stale,
        stale[:2] or "updated",
    )
else:
    print(
        "  [SKIP] A025 unreproduced-pipeline sentence "
        "(rerun report not yet in tree — expected before the report lands)"
    )

# Continuum-lift honesty in A021: the discrete certificates must not be
# promoted to a continuum orbit / continuum Floquet proof.
a021 = (ART / "A021_liebig_graph_corrected.tex").read_text(errors="replace")
check(
    "A021 still refuses a continuum monodromy enclosure",
    "not an outward-rounded enclosure of the continuum monodromy operator" in a021,
)
check(
    "A021 still keeps Conjecture graph / Prop conditional open",
    "Conjecture" in a021 and "remains open" in a021 and "remains conditional" in a021,
)

print("\n" + "=" * 72)
if FAIL:
    print(f"{len(FAIL)} check(s) failed: {FAIL}")
    sys.exit(1)
print("All manuscript-side sweep checks passed.")
sys.exit(0)
