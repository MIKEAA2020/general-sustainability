# Supersession Map — Programme-Wide Banner Pass (v1)

**Date:** September 26, 2026. **Purpose:** one authoritative pointer table
for the whole programme, recording which edition of every paper is
current and which are superseded. Frozen files are **never edited**; this
map is the banner. Any file not listed here is not part of the programme.

## P1 — Obstruction calculus (flagship)

| Artifact | Status |
|----------|--------|
| `paper2_obstruction_calculus_v49_Automatica_routes.tex` | **current** (σ\* correct at lines 882, 1686, 1703); owner-side venue decision |
| earlier v1–v48 editions | superseded by v49 |

## P2 — Computational certification + library (flagship)

| Artifact | Status |
|----------|--------|
| `paper2_computational_certification_v9.tex` | **current** |
| `paper2_supplement_sensitivity_v6.tex` | **current** (companion) |
| `viacert` library | **current** |
| `paper2_exact_belief_computation_v1.tex` (+ PDF + verify, round 12) | **current** — medium-instance exact point-based evaluation and survivable-set compression; computational companion to the P3 theory |
| earlier computational editions (v1–v8, S1–S5) | superseded |

## P3 — Probabilistic sufficiency (flagship)

| Artifact | Status |
|----------|--------|
| `paper2_probabilistic_sufficiency_v4.tex` (+ PDF + verify 26/26) | **current** — adds DR interpolation, probe-count asymptotics, additive deadline law to v3's class lattice / closed forms / antichain / stochastic layer |
| `paper2_probabilistic_sufficiency_v3.tex` (+ PDF + verify 23/23) | superseded by v4 (frozen at `c630363`) |
| `paper2_probabilistic_sufficiency_v2.tex` (verify 18/18) | superseded by v3 (frozen at `36ed76b`) |
| `paper2_probabilistic_sufficiency_v1.tex` (verify 15/15) | superseded by v2 (frozen at `bd04641`) |
| seeds `paper2_stochastic_selector_v2*`, `paper2_belief_state_v2*` (+ `figs_bs2/`, figures script) | byte-frozen origins of the lineage; corrections land in the P3 flagship only |

## P4 — Worked-systems supplement (flagship)

| Artifact | Status |
|----------|--------|
| `paper2_worked_systems_v10.tex` | **current**, scan-clean (`592a1ba`) |
| earlier ws editions | superseded by v10 |

## P5 — Applied paper

| Artifact | Status |
|----------|--------|
| — | **pending owner data** (parked since round 10); owner's decision gates the build |

## Other

| Artifact | Status |
|----------|--------|
| `hidden_parameter_learning_v1*` (tex + verify) | byte-frozen seed; superseded conceptually by the P3 flagship's stochastic layer |
| roadmaps v16–v30 | superseded by **v31** (`paper2_obstruction_calculus_followup_roadmap_v31.md`) |
| `uploads/github_pat.txt` | **never push** — credential, not programme content |

**Rule reaffirmed:** new versions never overwrite; superseded editions
remain in place, byte-frozen, each with its own verification script and
PDF; this map is updated (as a new `supersession_map_vN.md`) whenever a
flagship advances.
