# Paper 2 — Obstruction Calculus: Follow-up Roadmap (v32)

**Subject:** *An Obstruction Calculus for Viability under Incomplete Observation*
(current: `paper2_obstruction_calculus_v49_Automatica_routes.tex` + supplementary v46).

**v32 changes:** **Round 13 shipped — audit-adjudication round.** (1) **P3 edition 5**
(`paper2_probabilistic_sufficiency_v5.tex`): the round-12 audit bundle — companion
back-pointer to the P2 scaling record (closing the citation asymmetry), the
noiseless-limit remark (the exact split of `prop:learn` is the ε → 0 degeneration
of the probe-count law: sep → 1/2, p_wrong(1) = ε → 0), and the calculus
Section-10 cross-note (the sensor counterexample delimits the deterministic-limit
min-mass bound; the delayed-hidden-regime instance is the deadline law at
d₀ = 1, e_p = 0). Verify **28/28**; 9 pp, overfull 0. (2) **Exact belief
computation edition 2** (`paper2_exact_belief_computation_v2.tex`): the
four-parameter cube (16 cells × 16 levels = 256 augmented cells, 17 actions,
exact rational arithmetic) — the pair-sum lemma forcing all blind survivable
sets into Hamming-adjacent pairs (nothing ≥ 3 survives any blind policy, any
period), bands 16 singletons / 32 Hamming-1 pairs, the doubling observation
ladder (each probe doubles conditional kernel mass; three probes exhaust
observation above the edge), exact PBVI at k = 4 (83,521 sequences → ≤ 545
vectors; 84 exact pairings), the antichain census (1,048,576 raw → 496 stored),
and a third deadline-law instance (z₀ ≥ 1 + T/2). Verify **16/16** (chains
edition 1); 3 pp, overfull 0. **Catches before ship:** census arithmetic 736 →
496 (verifier), deadline test construction, one overfull display. (3) **P5
re-adjudicated (root-cause status correction):** the applied data gate is
**cleared** — `paperE1_calibration_data_v1` (RAM v4.66 extract; DFO 2016
Table A2 cross-checked 33/33; xteNCAM Table 17 with Blim 276 checkpoints; the
capelin hidden-regime covariate; wave-e-cod canonicalized with locked
provenance) landed 2026-09-24 and already feeds the applied forecast-ladder
flagship at v50 (47/47). The residual ledger's "pending owner data" (R12) is
stale as a data statement; what remains owner-side is the **decision**: (a)
designate the E1 forecast-ladder lineage as P5, or (b) build the
obstruction-programme applied paper on the same locked data (hidden-regime
viability with the capelin covariate against Blim/LRP thresholds). (4)
**Cross-tool feasibility datum recorded:** z3 5.1.0 agrees with the exact
arithmetic on two bounded cube questions (unsat for the full cube at T = 4;
sat for the Hamming-1 pair at T = 12) — the first verified datum for the
recorded cross-tool comparison construction; no SMT/conic solver enters any
shipped verify chain. (5) **Supersession map v2** (this round's advances).

## Cross-effect map (round-13 audit result)

| Edge | Effect | Recorded where |
|---|---|---|
| P3 v4 → P1 §10 | subsumption: P1's delayed-hidden-regime instance = deadline law at d₀ = 1, e_p = 0 | P3 v5 cross-note |
| P3 v4 ← P1 §10 | delimitation: min-mass deficit bound is deterministic-limit-scoped (sensor instance: 1/20 < 1/2) | P3 v5 cross-note |
| P3 ↔ P2 (ebc) | back-pointer now symmetric: ebc cites P3's `prop:pl` machinery; P3 v5 names the scaling record | both editions |
| P3 v4/v5 ↔ P4 ws v10 | none: ws v10's "2026b, Theorem 1" is P1's; v4/v5 purely additive over v3 (no stale sibling paraphrases) | round-13 audit |
| seeds ↔ flagships | regression-safe: seed verifies run inside the P3 chain every audit; seeds byte-frozen | v31 map, unchanged |
| P2 (ebc) → P4-style applied (E1) | none yet; option (b) for P5 would create this edge (capelin covariate × hidden-regime machinery) | this roadmap, §P5 |

## Flagship board (v17 architecture; status updated)

| # | Flagship | Latest | Status |
|---|----------|--------|--------|
| P1 | Obstruction calculus | v49 + supp v46 | shipped, frozen; owner-side venue decision |
| P2 | Computational certification + library | comp v9 + S1 v6 + `viacert`; **exact belief computation v2** | current |
| P3 | Probabilistic sufficiency | **v5 (companion pointers + bridge remark + Section-10 note)** | current; v1–v4 frozen |
| P4 | Worked-systems supplement | ws v10 | current, scan-clean (`592a1ba`), unaffected |
| P5 | Applied paper | **data gate cleared; pending owner decision between (a) E1 v50 designation and (b) the obstruction-applied build** | re-adjudicated R13 |

Seeds (byte-frozen): `paper2_stochastic_selector_v2*`, `paper2_belief_state_v2*`,
`hidden_parameter_learning_v1*` (tex + verify each) + `figs_bs2/` five PDFs +
`paper2_belief_state_figures.py`. Editions frozen in place: P3 v1 (`bd04641`), v2
(`36ed76b`), v3 (`c630363`), v4 (`2ac7adc`); ebc v1 (chained seed of v2).

## Build-order status

1. P4 ws v10 — done.
2. P2 comp v9 + S1 v6 + `viacert` — done; ebc v2 added (round 13).
3. P3 v5 — done (round 13; v1–v4 frozen).
4. P5 — **owner decision** (data in hand; two options above).
5. Supersession banners — map v2 current; final roadmap rolls forward.
6. Recorded constructions of their own (unchanged dispositions, one new datum):
   cross-tool comparison study (now with the z3 5.1.0 agreement datum; certificate
   file as exchange format remains the prerequisite); conic/stochastic P2 edition
   citing P3's `prop:dr` as its formal home; Epistemic-HJBI Open Problem 1
   (conjectures with named gaps); Lean formalization of the closed forms
   (deferred by decision).
