# paper1 (Zenodo 22545740) and paper4 (Zenodo 22554217): overlap check vs ECOMOD v33

Follows on from `audits/PAPER3_OVERLAP_CHECK_vs_v33.md`. Downloaded and text-searched both PDFs to
verify the sibling-paper boundaries ECOMOD cites in its Division-of-labour bullet, and to confirm the
two sentences I inserted into the manuscript are accurate.

---

## paper1 — *The Limits of Compensatory Aggregation: A Formal Separation of Weak and Strong Sustainability Assessment* (23 pp)

- **Domain:** static *assessment/separation* theory. A separation result on a typed transition datum under
  exact-tube semantics: for every nonnegative scalarisation weight some action keeps the *aggregate* floor
  nonnegative, while no single action keeps all *typed* floors nonnegative. `FPagg = Vweak \ Vtyp` is the
  impossibility region, nonempty interior; a blend/conv exification theorem and a time-sharing converse.
- **Overlap with ECOMOD:** **none.** Searched terms present/absent: `biocapacity 0`, `global hectare 0`,
  `gha 0`, `National Footprint 0`, `footprint 0`, `conversion 0` (land), `composition illusion 0`,
  `two-book 0`, `land use 0`, `E_ceil 0`. Its single `identifiability` hit is a *calibration/data*
  methodological step, unrelated to gha-identifiability.
- **Productivity-illusion pointer (important):** paper1 *explicitly hands the dynamical sense away* —
  "the productivity illusion of adequate delivery from a quietly reduced base **belongs to the companion
  ledger study** (Author, A., et al., in review)." So paper1 (static aggregation theorem) and paper3
  (ledger/yield-inflation framing) own the concept's two senses; ECOMOD uses the **distinct term**
  *composition illusion* for its dynamical two-book realisation. No duplication.
- **Conclusion:** ECOMOD cites paper1 correctly for Prop 1; no trimming needed. Static assessment theory
  vs. a dynamical model.

## paper4 — *Delay-Induced Regime Change in Harvested Stocks: The Mobilising and Protective Channels of Institutional Feedback, and the Review Interval as Control* (39 pp)

- **Domain:** *institutional* (governance-loop) delay in a **gated three-state** model `(N, Z, E)`:
  stock, deficit memory, deployed effort. Two effort laws (mobilising vs protective quota-tracking);
  characteristic equation → cubic modulus + phase relation; two subcritical Hopf crossings (≈3.7, ≈150 yr)
  bound a stabilising window for the mobilising channel; protective channel = no-Hopf theorem; periodic
  review → Neimark–Sacker crossing ≈6.5 yr; five-regime attractor topology.
- **Overlap with ECOMOD:** **none structurally.** `biocapacity 0`, `global hectare 0`, `gha 0`,
  `footprint 0`, `composition illusion 0`, `two-book 0`, `identifiability 0`. Its 13 `qEN` hits are the
  **same single-resource deficit identity** `qEN − R = −ṅ` that paper3 declares as the shared object —
  **not** ECOMOD's two-book deficit `S=[E−σ_fY_f−σ_cY_c]_+`. Its 2 `composition` hits are stock-law
  birth–mortality decompositions, not land composition.
- **The decisive distinction:** paper4's delay is in the **institutional feedback loop** (deployed-effort
  response and the *review interval*), whereas ECOMOD's delays are **ecological** (regeneration `τ_g`,
  demography `τ_p`). paper4 has no land book, no ecological-regeneration/demography lag, no biocapacity,
  and no two-book structure.
- **Cross-ref:** paper3's interface contract explicitly names this companion: "the companion delay-dynamics
  analysis (**Author, D., et al., in review**)" = paper4. This confirms my inserted sentence that paper3
  "cedes all delay/Hopf dynamics to the companion."

---

## What I inserted into `manuscript_ECOMOD_v33.tex`

1. **New paragraph** at the top of §Discussion Identifiability — "Relation to the general ledger framework
   (paper3)": paper3 owns the *static* accounting layer, cedes all delay/Hopf/periodic dynamics to the
   companion, and registers a two-pool dynamical model as an open gap; ECOMOD supplies exactly that missing
   *dynamical* two-book realisation for global-hectare biocapacity. The term is deliberately *composition*
   illusion (two-book land conversion), which paper3 frames as the yield-inflation sense of "productivity
   illusion."

2. **Division-of-labour bullet** extended to: (a) attribute the static ledger + aggregation obstruction to
   paper3 (which cedes delay/Hopf dynamics and registers the two-pool gap); (b) attribute the *institutional*
   slow-turnover delay regime to paper4/v18; and (c) **state the delay-channel distinction explicitly** —
   ECOMOD's delays are ecological (`τ_g`,`τ_p`), paper4's are institutional (governance response + review
   interval). This closes the one requirement from the earlier positioning audit.

Verified: manuscript parses-balanced (braces 0, `$` even, envs balanced), both new passages present.

*Read-only vs. paper1/paper4 (downloaded to `p1/`, `p4/`); only the ECOMOD manuscript was edited in this step.*
