"""Gold-labelled eval set, re-keyed to revision v21 (formal-article wording).

This is the v21 refresh of `eval_gold_v20.py`. The master's §12 review points
are unchanged; what changed is the revision's wording, so each anchor is now a
distinctive substring that actually occurs in the v21 material and resolves to
the paragraph that genuinely addresses the claim (and is matcher-ranked top-3).

Anchors are DISTINCTIVE SUBSTRINGS (not line numbers). The eval resolves each
phrase to the revision paragraph(s) containing it, so the gold set is robust to
paragraph re-numbering / document edits (line-number anchors broke the first time
the revision was edited). Each phrase should be:
  * uniquely identifying of the target paragraph, and
  * stable in wording.

Two sets:
  * GOLD_PHRASES      : claim id -> phrases that GENUINELY address the claim (positives).
  * HARD_NEG_PHRASES  : claim id -> phrases that look plausible but are NOT the answer.

Both are used to measure precision/recall of the matcher.

Provenance: v2026-09-06 — re-keyed against
`data/revisions/IMPLEMENTED_revision_ECOMOD_v21.md` after the formal-journal
rewrite superseded the v20 master-facing wording. Old set preserved as
`scan/eval_gold_v20.py`; the callers import via `scan/gold.py`.
"""

GOLD_PHRASES = {
    "12A.1": ["The reduced masking model",
              "quantified, converged, and conditional"],
    "12A.2": ["well posed at the boundary"],
    "12A.3": ["method-dependent (5.26 / 6.74 / 18.70"],
    "12A.4": ["Baseline sits at a knife-edge"],
    "12B.5": ["co-evolving per-capita requirement"],
    "12B.6": ["γ = 1/b_G = 1/V"],
    "12B.7": ["system is genuinely 3-D"],
    "12C.8": ["use a non-multiple step"],
    "12C.9": ["normalise \"barely positive\""],
    "12C.10": ["Complete the scenario/parameter table"],
    "12D.11": ["the delayed-logistic *stability* result is Hutchinson"],
    "12D.12": ["Brander & Taylor (1998) is a distinct Ricardo"],
    "12D.13": ["documented in Wackernagel & Rees (1996)"],
    "12D.14": ["Symbols and units are given for"],
    "12E.1": ["Method sensitivity and numerical checks"],
    "12G.1": ["Which lag destabilises"],
    "12G.2": ["falls from 0.506 (no delays)"],
    "12G.3": ["the complete non-dimensionalization"],
    "12G.4": ["inverse of the orchard framing"],
    "12G.5": ["Scenario-D threshold is near-critical"],
    "12G.6": ["Stability and complexity in model ecosystems"],
    "12G.7": ["Delay asymmetry"],
}

# Semantically close but NOT the right answer. A too-loose threshold would wrongly
# flag these; they sharpen the precision estimate.
HARD_NEG_PHRASES = {
    "12A.1": ["compensatory-aggregation gap"],
    "12A.2": ["Parameters are representative"],
    "12A.3": ["the collapse result holds for"],
    "12A.4": ["the collapse result holds for"],
    "12B.5": ["carrying capacity is not an imposed ceiling"],
    "12B.6": ["Temporal-lead nuance"],
    "12B.7": ["Cap the human-available flow"],
    "12C.8": ["the collapse result holds for"],
    "12C.9": ["The vicious cycle is real and quantitative"],
    "12C.10": ["This is a conceptual / stylised model"],
    "12D.11": ["delay-ratio Hopf"],
    "12D.12": ["carrying capacity is not an imposed ceiling"],
    "12D.13": ["National Footprint Accounts (NFA) data limitation"],
    "12D.14": ["the six-group set"],
    "12E.1": ["The sustainable point is a boundary equilibrium"],
    "12G.1": ["Information-layer limit"],
    "12G.2": ["The coarse grid overstates"],
    "12G.3": ["The vicious cycle is real and quantitative"],
    "12G.4": ["compensatory-aggregation gap"],
    "12G.5": ["The coarse grid overstates"],
    "12G.6": ["The sustainable point is a boundary equilibrium"],
    "12G.7": ["Method-of-steps with RK4"],
}
