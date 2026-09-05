"""Authoritative (human/machine-verified) status overrides, keyed by master ID.

The automatic matcher is a first-pass detector; this curated table holds the
verified verdicts (established by the independent numerical audit + manual
re-review). The CLI applies these as the authoritative `status`, keeps the
auto score + method as evidence, and flags any ITEM where the automatic status
disagrees with the curated verdict (a signal the matcher needs tuning or the
item needs another look).

Status values: covered | partial | superseded | missing | ambiguous.
"""
# Claims whose underlying number/results are properties of the COPY of the ORIGINAL
# gross-depletion model (they are the ones the numeric verifiers recompute on `sim.py`).
ORIGINAL_MODEL_IDS = {"12A.3", "12G.2", "12G.4", "12G.5"}

# Claims whose content describes the CORRECTED (1‴) unified model's structure/analytics
# (the remediation itself); these are corrected-model claims.
CORRECTED_MODEL_IDS = {"12A.1", "12A.2", "12B.5", "12B.6", "12B.7", "12C.8",
                       "12C.9", "12C.10", "12G.3", "12G.6", "12G.7"}

OVERRIDES = {
    "12A.1":   ("superseded",
                "Head-line masking numbers were computed on the ORIGINAL model; under the "
                "corrected model the mask is narrow/deficit-limited (~5.4 yr, vanishing >0.075)."),
    "12A.2":   ("covered", "K->0 blow-up fixed via A_ext extinction floor + clamps."),
    "12A.3":   ("covered", "D_E method-dependent (5.26/6.74/18.70); verified 5.26."),
    "12A.4":   ("covered", "Knife-edge chi=1 <=> rho=3q flagged as non-generic."),
    "12B.5":   ("covered", "per-capita footprint constant; endogenising e, r_opt offered."),
    "12B.6":   ("covered", "gross gamma E retained as named supplement variant."),
    "12B.7":   ("covered", "K is algebraic, not a state; system is 3-D."),
    "12C.8":   ("covered", "state no interpolation / use non-multiple step."),
    "12C.9":   ("covered", "state grid range; normalise Re lambda by r."),
    "12C.10":  ("covered", "complete scenario/parameter table."),
    "12D.11":  ("covered", "cite Hutchinson 1948; soften Haberl & Aubauer novelty."),
    "12D.12":  ("covered", "correct Brander-Taylor characterisation."),
    "12D.13":  ("covered", "GFN reference list adopted."),
    "12D.14":  ("covered", "E5 cleanliness: antibiotic, elevator, per-year, units, tense."),
    "12E.1":   ("covered", "verified-correct list preserved ('do not fix')."),
    "12G.1":   ("covered", "four falsifiable predictions stated."),
    "12G.2":   ("covered",
                "basin-shrinkage 0.506->0.042; ORIGINAL-model S0. Corrected S0 is a one-sided "
                "boundary -> recompute separately (risk R1)."),
    "12G.3":   ("covered", "full dimensionless group set s,g,f,theta,tau."),
    "12G.4":   ("covered", "B/C = environment recovers, humans collapse (opposite framing)."),
    "12G.5":   ("covered", "(20,20) recovers / (30,25) collapses; min-M grid-sensitive."),
    "12G.6":   ("covered", "submission hygiene: May orphan, Modeling/Modelling, keywords, .py/.pdf."),
    "12G.7":   ("covered",
                "Jevons rebound, tau_D asymmetry, omega=0, trivial equilibrium, Omega footnote, "
                "dde23 covered; the SECOND masking set's numbers are superseded (original model)."),
}

# --- Human judgment calls captured so future scans are consistent ------------
# These are the cases where the AUTO detector and the CURATED verdict diverge,
# plus the reasoning. Recorded so the next run resolves them the same way and
# a reviewer can see the decision was made, not arbitrar ily.
CURATED_DECISIONS = {
    "12B.6": ("covered",
              "AUTO flagged a supersession marker in the matched paragraph; curated says COVERED "
              "because the B7 point ('general gamma advertised but only gamma=1 used') is "
              "addressed by reconciling gamma as `1/b_G` in the unified model and retaining gross "
              "gamma-E as a named supplement variant (§2.2, §7). The marker is contextual prose, "
              "not a withdrawal of this item."),
    "12G.7": ("covered",
              "AUTO flagged 'superseded-style' phrasing in §8; curated says COVERED because the "
              "12G.7 fine points (Jevons rebound, tau_D/asymmetry, omega=0, trivial equilibrium, "
              "dde23, Omega footnote) ARE implemented in §3/§5/§8. The superseded phrasing refers "
              "only to the SECOND masking set's original-model numbers, which is a separate item "
              "(12A.1)."),
}

# IDs where an explicit marker in the matched revision paragraph is CONTEXTUAL
# (the revision discusses supersession in general) and must NOT flip the item to
# superseded. The curated verdict is authoritative; the auto detection is evidence.
NOT_SUPERSEDED = {"12B.6", "12G.7"}
