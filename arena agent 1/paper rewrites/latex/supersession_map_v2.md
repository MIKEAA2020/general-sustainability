# Supersession Map — Programme-Wide Banner Pass (v2)

**Date:** September 26, 2026. **Supersedes `supersession_map_v1.md`.** Same rule
as v1: frozen files are never edited; this map is the banner; any file not
listed here is not part of the programme.

## P1 — Obstruction calculus (flagship)

| Artifact | Status |
|----------|--------|
| `paper2_obstruction_calculus_v49_Automatica_routes.tex` | **current** (σ\* correct at lines 882, 1686, 1703); owner-side venue decision |
| `paper2_obstruction_calculus_v46_Automatica_routes_supplementary.*` | **current** (companion supplementary) |
| earlier v1–v48 editions | superseded by v49 |

## P2 — Computational certification + library (flagship)

| Artifact | Status |
|----------|--------|
| `paper2_computational_certification_v9.tex` (+ PDF + verify 37/37) | **current** |
| `paper2_computational_certification_supplementary_v6.tex` | **current** (companion) |
| `viacert` library | **current** |
| `paper2_exact_belief_computation_v2.tex` (+ PDF + verify 16/16) | **current** — the four-parameter cube: pair-sum/Hamming classification, doubling ladder, PBVI at k = 4, census 1,048,576 → 496 |
| `paper2_exact_belief_computation_v1.tex` (+ PDF + verify 11/11) | superseded by v2; retained as its **chained seed** (runs inside v2's chain) |
| earlier computational editions (v1–v8, S1–S5) | superseded |

## P3 — Probabilistic sufficiency (flagship)

| Artifact | Status |
|----------|--------|
| `paper2_probabilistic_sufficiency_v5.tex` (+ PDF + verify 28/28) | **current** — v4 plus the companion back-pointer, the noiseless-limit remark (ε → 0 bridge), and the calculus Section-10 cross-note |
| `paper2_probabilistic_sufficiency_v4.tex` (verify 26/26) | superseded by v5 (frozen at `2ac7adc`) |
| `paper2_probabilistic_sufficiency_v3.tex` (verify 23/23) | superseded (frozen at `c630363`) |
| `paper2_probabilistic_sufficiency_v2.tex` (verify 18/18) | superseded (frozen at `36ed76b`) |
| `paper2_probabilistic_sufficiency_v1.tex` (verify 15/15) | superseded (frozen at `bd04641`) |
| seeds `paper2_stochastic_selector_v2*`, `paper2_belief_state_v2*` (+ `figs_bs2/`, figures script) | byte-frozen origins; corrections land in the P3 flagship only |

## P4 — Worked-systems supplement (flagship)

| Artifact | Status |
|----------|--------|
| `paper2_worked_systems_v10.tex` | **current**, scan-clean (`592a1ba`) |
| earlier ws editions | superseded by v10 |

## P5 — Applied paper

| Artifact | Status |
|----------|--------|
| `paperE1_cod_forecast_ladder_v50.tex` (+ verify 47/47) + `paperE1_calibration_data_v1*` | **applied lineage, current, data-fed**; P5 designation pending owner decision between (a) adopting this lineage and (b) the obstruction-applied build on the same locked data |
| — | prior "pending owner data" status retired (data landed 2026-09-24) |

## Other

| Artifact | Status |
|----------|--------|
| `hidden_parameter_learning_v1*` (tex + verify) | byte-frozen seed; absorbed at proposition level into P3 v4+ |
| roadmaps v16–v31 | superseded by **v32** (`paper2_obstruction_calculus_followup_roadmap_v32.md`) |
| `supersession_map_v1.md` | superseded by this map |
| `uploads/github_pat.txt` | **never push** — credential, not programme content |
| release-asset `.github_pat` (in `edwards-framework-e1` assets) | **owner action: revoke/rotate** (flagged in the calibration addendum; reiterated here) |

**Rule reaffirmed:** new versions never overwrite; superseded editions remain
byte-frozen with their own verify scripts and PDFs; this map is updated (as
`supersession_map_v(N+1).md`) whenever a flagship advances.
