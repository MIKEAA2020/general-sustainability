"""Gold-labelled eval set for the master->revision matcher.

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
"""

GOLD_PHRASES = {
    "12A.1": ["quantified, converged, and *conditional*",
              "The reduced masking model (`dA/dt = G(A) − ramp(E−bA)/b_G"],
    "12A.2": ["non-Lipschitz singularity fix",
              "method-of-steps with RK4"],
    "12A.3": ["method-dependent (5.26 / 6.74 / 18.70"],
    "12A.4": ["Baseline sits at `χ = 1` **because `ρ` was set to `3q`**"],
    "12B.5": ["Per-capita footprint is constant",
              "Endogenising `e` and `r_opt` is an offered extension"],
    "12B.6": ["retained only as the \"land-conversion",
              "B6/B7 (co-evolution, general γ)"],
    "12B.7": ["**algebraic**, not a state", "`K` is algebraic, not a state"],
    "12C.8": ["no interpolation occurs"],
    "12C.9": ["State the grid range", "normalise \"barely positive\" Re λ by `r`"],
    "12C.10": ["Complete the scenario/parameter table"],
    "12D.11": ["cite Hutchinson (1948)"],
    "12D.12": ["correct the Brander–Taylor (1998) characterisation"],
    "12D.13": ["add the GFN account + limitations references", "Wackernagel & Rees;"],
    "12D.14": ["antibiotic resistance"],
    "12E.1": ["Verified correctness (do not \"fix\")"],
    "12G.1": ["oscillation period near onset ≈ 4× the dominant lag",
              "Which lag destabilises"],
    "12G.2": ["measured basin-shrinkage result", "0.506 (no delays)"],
    "12G.3": ["complete non-dimensionalization", "the six-group set"],
    "12G.4": ["*inverse* of the orchard framing"],
    "12G.5": ["Scenario-D threshold is an accident"],
    "12G.6": ["Submission hygiene:", "orphan May (1973)"],
    "12G.7": ["Delay asymmetry explicitly", "Jevons-type rebound", "max Ω not reported\" footnote"],
}

# Semantically close but NOT the right answer. A too-loose threshold would wrongly
# flag these; they sharpen the precision estimate.
HARD_NEG_PHRASES = {
    "12A.1": ["sustainable equilibrium is interior", "genuine overshoot→collapse run",
              "vicious cycle is real and quantitative"],
    "12A.2": ["conceptual / stylised model with representative calibration"],
    "12A.3": ["ρ is still large in the original scale"],
    "12A.4": ["max-sustainable-yield", "the two-delay stability boundary is controlled"],
    "12B.5": ["Scenario B/C is the *inverse* of the orchard framing"],
    "12B.6": ["State the delay asymmetry explicitly"],
    "12B.7": ["Linearising `(1‴)+(4′)`"],
    "12C.8": ["smooth   ramp", "clamping"],
    "12C.9": ["flow-only limit", "fixed liability above the maximum sustainable yield"],
    "12C.10": ["verbal walk-through"],
    "12D.11": ["carrying capacity is not an imposed ceiling"],
    "12D.12": ["Original claim | Corrected (defensible) claim"],
    "12D.13": ["the two masks (weak/strong sustainability)"],
    "12D.14": ["We present a minimal coupled human–environment model"],
    "12E.1": ["characteristic equation and Appendix A linearisation"],
    "12G.1": ["two masks (weak/strong sustainability), made observable"],
    "12G.2": ["fixed liability above the maximum sustainable yield"],
    "12G.3": ["Regeneration: G(A) = ρ A", "`K = B/e` is emergent"],
    "12G.4": ["which e, which lags, and whether T(t) is active"],
    "12G.5": ["a₁₁ gains the `+b/b_G`"],
    "12G.6": ["provided as Word documents"],
    "12G.7": ["representative overshoot run", "deferred to future work"],
}
