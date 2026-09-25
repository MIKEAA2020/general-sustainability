# Paper 2 — Obstruction Calculus: Follow-up Roadmap (v29)

**Subject:** *An Obstruction Calculus for Viability under Incomplete Observation*
(current: `paper2_obstruction_calculus_v49_Automatica_routes.tex` + supplementary v46).

**v29 changes:** **P3 hardened** — an external 13-finding audit of
`paper2_probabilistic_sufficiency_v1` was adjudicated finding-by-finding
(all 13 verified, zero rebuttals; addendum
`paper2_probabilistic_sufficiency_v2_addendum.md`) and shipped as
**edition 2**: class superscripts throughout (declared hold vs unrestricted
sequential; the closed form restated as a standalone hold-class
proposition), class-difference region corrected to
2 ≤ z₀ < 1 + min(k, T_obs) (timing cells on the grid; counterexample in the
statement; verified off-grid to z₀ = 4.0), horizon-qualified deficit
profile, the learning-deadline identity relabeled as the pinned-probe
family with two new exact benchmarks (free-probe 21/10 flat; probe-free
exogenous revelation 1 + T_learn/10, kernels 16–12), the 384-vector census
reattributed with its deduplicated 348-vector form, the asymmetric audit's
lost-branch step corrected to step 1 with branch identities, deterministic
observation maps added to the support identity, the σ\* direction fixed to
P1 v49's convention (the misquote existed only in the P3 lineage), and a
notation paragraph (𝒲/𝒲^{bel}, Γ^Π/Γˢ, no unsuperscripted values).
Verify 18/18 (chained 16+21/15/6); 7 pp, overfull 0; v1 and the seeds
byte-frozen. Provenance recorded: the class-attribution defects were latent
in `paper2_belief_state_v2`'s own presentation; check S7 was already
horizon-qualified in code.

## Flagship board (unchanged from v17; status updated)

| # | Flagship | Latest | Status |
|---|----------|--------|--------|
| P1 | Obstruction calculus | v49 + supp v46 | shipped, frozen; owner-side venue decision |
| P2 | Computational certification + library | comp v9 + S1 v6 + `viacert` | current (`65e3ef9`) |
| P3 | Probabilistic sufficiency | **v2 (audit-hardened)** | built, verified, pushed |
| P4 | Worked-systems supplement | ws v10 | current, scan-clean (`592a1ba`) |
| P5 | Applied calibration | — | pending owner data (R12) |

Build-order status: steps 1–3 done; step 4 (P5) pending owner data; step 5
(supersession banners + final roadmap) outstanding, programme-wide. All
other v27 items unchanged and still open where marked there.

*Every claim above is a pointer into the cited sources; nothing here
creates theorem status.*
