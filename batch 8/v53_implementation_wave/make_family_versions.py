#!/usr/bin/env python3
"""make_family_versions.py — the companion-version fixes of the Task-107 wave.

Builds, as NEW version files (never overwrite), the family cross-reference
corrections discovered/approved this round:

  * P2 v44 (main + supplementary)   — stale P1 reference entry (old md-lineage
    title) updated to the current P1 title, in P2's sentence-case style.
  * ECOMOD v36                      — stale P1 (2026b) and stale P4 (2026a)
    reference titles updated to the current titles; the dangling
    "aggregation theorem (Prop 1)" forward reference made explicit.
  * P3 v50 (md + tex)               — stale P4 (2026a) and stale P1 (2026c)
    reference titles updated to the current titles.

All DOIs unchanged (they are the family's recorded deposit pointers; the
deposit-side title refresh is owner-side knowledge, recorded in the round
record). Fail-loud: exact anchors asserted once; inverse-reconstruction
gate per file; destinations must not exist.
"""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

P1_TITLE_CURRENT = "Aggregate Indices and Transition Safety: A Quantifier-Order Separation Between Scalarized and Coordinate-Wise Feasibility"
P1_TITLE_SENTENCE = "Aggregate indices and transition safety: a quantifier-order separation between scalarized and coordinate-wise feasibility"
P4_TITLE_CURRENT = "Governance delay and the stability of harvested stocks: mobilising and protective feedback rules, and the review interval as a design parameter"

def die(msg: str):
    print(f"FAIL: {msg}")
    sys.exit(1)

def build(src: Path, dst: Path, edits: list, name: str):
    """edits: list of (label, anchor, replacement). Inverse-gated."""
    if not src.exists():
        die(f"[{name}] source missing: {src}")
    if dst.exists():
        die(f"[{name}] destination already exists (never overwrite): {dst}")
    text = src.read_text(encoding="utf-8")
    orig = text
    pairs = []
    for label, anchor, repl in edits:
        n = text.count(anchor)
        if n != 1:
            die(f"[{name}] anchor [{label}] found {n}x:\n---\n{anchor[:200]}\n---")
        pos = text.index(anchor)
        text = text[:pos] + repl + text[pos + len(anchor):]
        pairs.append((label, pos, anchor, repl))
        print(f"  ok  [{name}] {label}")
    # inverse-reconstruction gate
    t = text
    for label, pos, anchor, repl in reversed(pairs):
        if t[pos:pos + len(repl)] != repl:
            die(f"[{name}] inverse gate: replacement not at recorded position [{label}]")
        t = t[:pos] + anchor + t[pos + len(repl):]
    if t != orig:
        die(f"[{name}] inverse-reconstruction mismatch — diff beyond the enumerated edits")
    # sanity: no stale titles remain
    for stale in ["he limits of compensatory aggregation", "elay-Induced Regime Change", "elay-induced regime change"]:
        if stale in text:
            die(f"[{name}] stale title remains: {stale}")
    dst.write_text(text, encoding="utf-8")
    print(f"  WROTE {dst} ({len(orig.splitlines())} -> {len(text.splitlines())} lines)")

LATEX = REPO / "arena agent 1" / "paper rewrites" / "latex"
ECOMOD = REPO / "agent 2 productivity illusion"
P3 = REPO / "paper3" / "latest-2026-09-19" / "manuscript"

print("== P2 v44 (main + supplementary): the stale P1 entry ==")
P2_OLD = ("Abaee, A.: The limits of compensatory aggregation: a formal separation of "
          "weak and strong sustainability assessment. Zenodo. "
          "https://doi.org/10.5281/zenodo.22545740 (2026).")
P2_NEW = (f"Abaee, A.: {P1_TITLE_SENTENCE}. Zenodo. "
          "https://doi.org/10.5281/zenodo.22545740 (2026).")
build(LATEX / "paper2_obstruction_calculus_v43_Automatica_routes.tex",
      LATEX / "paper2_obstruction_calculus_v44_Automatica_routes.tex",
      [("P1 entry title -> current", P2_OLD, P2_NEW)],
      "P2 v44 main")
build(LATEX / "paper2_obstruction_calculus_v43_Automatica_routes_supplementary.tex",
      LATEX / "paper2_obstruction_calculus_v44_Automatica_routes_supplementary.tex",
      [("P1 entry title -> current", P2_OLD, P2_NEW)],
      "P2 v44 supplementary")

print("== ECOMOD v36: stale P1 + P4 entries; the Prop-1 dangling reference ==")
build(ECOMOD / "manuscript_ECOMOD_v35.tex",
      ECOMOD / "manuscript_ECOMOD_v36.tex",
      [("2026a P4 entry title -> current",
        "\\item Abaee, A. (2026a). \\emph{Delay-Induced Regime Change in Harvested Stocks: The Mobilising and Protective Channels of Institutional Feedback, and the Review Interval as Control.} Zenodo. \\url{https://doi.org/10.5281/zenodo.22554217}.",
        f"\\item Abaee, A. (2026a). \\emph{{{P4_TITLE_CURRENT}.}} Zenodo. \\url{{https://doi.org/10.5281/zenodo.22554217}}."),
       ("2026b P1 entry title -> current",
        "\\item Abaee, A. (2026b). \\emph{The Limits of Compensatory Aggregation: A Formal Separation of Weak and Strong Sustainability Assessment.} Zenodo. \\url{https://doi.org/10.5281/zenodo.22545740}.",
        f"\\item Abaee, A. (2026b). \\emph{{{P1_TITLE_CURRENT}.}} Zenodo. \\url{{https://doi.org/10.5281/zenodo.22545740}}."),
       ("Prop-1 dangling reference made explicit",
        "The aggregation theorem (Prop 1) is from the companion work on compensatory aggregation (Abaee, 2026b);",
        "The aggregation theorem (Proposition 1 of the deposited version of that work; Theorem 5 of its current version) is from the companion work on compensatory aggregation (Abaee, 2026b);")],
      "ECOMOD v36")

print("== P3 v50 (md + tex): the stale P4 and P1 entries ==")
for src, dst, ext in [
    (P3 / "paper3_material_ledgers_v49.md", P3 / "paper3_material_ledgers_v50.md", "md"),
    (P3 / "paper3_material_ledgers_v49.tex", P3 / "paper3_material_ledgers_v50.tex", "tex"),
]:
    s = src.read_text(encoding="utf-8")
    # locate the two entries verbatim (they may carry trailing annotations)
    import re
    m4 = re.search(r"Abaee, A\., 2026a\. Delay-induced regime change in harvested stocks: the mobilising and protective channels of institutional feedback, and the review interval as control\. Zenodo\. [^\n]*", s)
    m1 = re.search(r"Abaee, A\., 2026c\. The limits of compensatory aggregation: a formal separation of weak and strong sustainability assessment\. Zenodo\. [^\n]*", s)
    if not m4 or not m1:
        die(f"[P3 v50 {ext}] entry anchors not found")
    e4 = m4.group(0)
    e1 = m1.group(0)
    e4_new = e4.replace("Delay-induced regime change in harvested stocks: the mobilising and protective channels of institutional feedback, and the review interval as control", P4_TITLE_CURRENT)
    e1_new = e1.replace("The limits of compensatory aggregation: a formal separation of weak and strong sustainability assessment", P1_TITLE_SENTENCE)
    build(src, dst,
          [("2026a P4 entry title -> current", e4, e4_new),
           ("2026c P1 entry title -> current", e1, e1_new)],
          f"P3 v50 {ext}")

print("\nAll family versions built.")
