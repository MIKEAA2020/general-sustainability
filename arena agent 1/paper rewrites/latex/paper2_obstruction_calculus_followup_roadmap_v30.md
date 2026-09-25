# Paper 2 — Obstruction Calculus: Follow-up Roadmap (v30)

**Subject:** *An Obstruction Calculus for Viability under Incomplete Observation*
(current: `paper2_obstruction_calculus_v49_Automatica_routes.tex` + supplementary v46).

**v30 changes:** **P3 upgraded to a theory paper** — the round-11 upgrade
menu was adjudicated (addendum
`paper2_probabilistic_sufficiency_v3_addendum.md`) and shipped as
**edition 3** of `paper2_probabilistic_sufficiency`: the class lattice with
realized gaps (value of flexibility / value of observation), parametric
closed forms for all z₀/w/ℓ (the grid tables become one-line corollaries),
the survivable-set antichain formula explaining the witness census,
stabilization on the finite survivable lattice (audited tables are
full-horizon values; rising-continuation mechanism pinned to horizon 40),
and a genuinely stochastic layer — weighted-path deficit identity, the
sensor counterexample breaking min-mass universality (1/20 < 1/2), the
noisy-probe closed form with three value levels, and the repetition
trade-off (7/250 at ε = 1/10, 1/10 floor margin per probe step). Prior
work engaged with verified references (Chatterjee–Doyen–Henzinger 2009;
Papadimitriou–Tsitsiklis 1987; Alshiekh et al. 2018; Nakao–Jiang–Shen
2021); programme meta-talk removed from the paper. Verify 23/23 (chained
16+21/15/6); 9 pp, overfull 0. Round-10 residuals: none. **New programme
items (roadmap):** distributionally robust interpolation over ambiguity
sets; exact point-based value iteration with rational solvers and
survivable-set (ZDD) compression on medium multi-parameter instances;
probe-count asymptotics for the repetition trade-off; the general
learning-deadline law for additively entering hidden parameters;
proof-assistant formalization of the closed forms. Build-order status:
steps 1–3 done (P4 ws v10; P2 comp v9 + S1 v6 + `viacert`; P3 v3); step 4
(P5) pending owner data (R12); step 5 (supersession banners + final
roadmap) outstanding.

## Flagship board (v17 architecture; status updated)

| # | Flagship | Latest | Status |
|---|----------|--------|--------|
| P1 | Obstruction calculus | v49 + supp v46 | shipped, frozen; owner-side venue decision |
| P2 | Computational certification + library | comp v9 + S1 v6 + `viacert` | current (`65e3ef9`) |
| P3 | Probabilistic sufficiency | **v3 (theory upgrade)** | current |
| P4 | Worked-systems supplement | ws v10 | current, scan-clean (`592a1ba`) |
| P5 | Applied calibration | — | pending owner data (R12) |

All other v27 items unchanged and still open where marked there.

*Every claim above is a pointer into the cited sources; nothing here
creates theorem status.*
