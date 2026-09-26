# Lean Formalization Layer — `general-sustainability` paper family

This directory contains a Lean 4 formalization of the **core theorem layer** of
the paper family in `arena agent 1/paper rewrites/latex/`. One module per slot: (edition citations current as of round 28; the
formalized theorem layer is unchanged across these presentation-pass
editions — round 27/28 touched navigation, keywords, and reference
hygiene only)

| Slot | Paper (edition, source of record) | Module |
|---|---|---|
| P1 | Obstruction calculus — theory main line (2026b, `paper2_obstruction_calculus_v55_Automatica_routes.tex`) | `Formalizations.P1_Obstruction` |
| comp | Computational certification (2026d, `paper2_computational_certification_v17.tex`) | `Formalizations.Comp_Certification` |
| ws | Worked systems (2026c, `paper2_worked_systems_v17.tex`) | `Formalizations.WS_WorkedSystems` |
| minimax | Minimax dual certificates (2026g, `minimax_dual_certificates_v9.tex`) | `Formalizations.Minimax_Dual` |
| ebc | Exact belief computation (2026f, `paper2_exact_belief_computation_v8.tex`) | `Formalizations.EBC_ExactBelief` |
| P3 | Probabilistic sufficiency (2026e, `paper2_probabilistic_sufficiency_v10.tex`) | `Formalizations.P3_ProbSufficiency` |
| ARV | Applied regime viability (2026a, `applied_regime_viability_v8.tex`) | `Formalizations.ARV_RegimeViability` |
| E1 | Applied forecast ladder (E1, `paperE1_cod_forecast_ladder_v58.tex`) | `Formalizations.E1_ForecastLadder` |
| **P1-AS** | **Assessment separation — the head paper** (`paper1_assessment_separation_v62.tex`) | `Formalizations.P1_AssessmentSeparation` |

## Two-tier architecture

The certification architecture of the programme is reflected, not duplicated:

1. **Lean layer (this project): statement-level soundness.** Definitions and
   theorems of the frameworks — obstruction soundness, kernel fixed-point
   structure, certificate-soundness theorems (Farkas, minimax duals), belief
   algebra, sufficiency reductions, viability monotonicity, ladder telescoping.
   Every theorem is fully proved; there are **no `sorry`s and no extra axioms**.
2. **Python verifier layer (unchanged, in `latex/`): instance-level checks.**
   The 48/48, 54/54, 37/37, 25/25, 30/30, 236/236, 49/49 item batteries certify
   concrete numerical instances. The Lean layer proves the theorems that make
   those certificate checks *load-bearing* (a checked certificate implies the
   claimed property); the batteries supply the certificates.

## Fidelity policy

* Formalizations are **interface-level over `OrdField K`** (see
  `Formalizations/Prelude.lean`): every analytic statement is proved from the
  ordered-field interface alone, hence holds in any model; the papers'
  statements are the instance `K = ℝ`.
* Each theorem carries a header comment citing the paper's numbered result and
  quoting its statement gist. Abstractions (e.g. discrete-time or
  relation-based dynamics for the viability framework) are flagged explicitly
  in the module header and in the README index below.
* Deep classical existence results that the papers invoke from the literature
  (e.g. separation theorems behind the *hard* direction of Farkas' lemma) are
  **not** re-proved; the direction the papers' certificates actually use —
  soundness — is proved.
* The frozen slots (ebc, P3) are formalized **as they stand** at their current
  editions; no paper file is edited by this layer.

## Build

```
cd lean
lake build          # needs only the pinned toolchain, no network, no Mathlib
```

`lean-toolchain` is pinned to `leanprover/lean4:v4.34.1`. The project has no
dependencies, so a bare toolchain install suffices. (`.lake/` is gitignored;
only sources are versioned.)

## Theorem index

Complete — ten modules (395 theorems total; `lake build` green, zero
`sorry`, zero new axioms).

| Module | Formalizes (paper items) | Status |
|---|---|---|
| `Prelude` | ordered-field interface; `lsum`/`sumRange` (incl. telescoping); `dotp`/`linComb` + `farkas_sound`; `IsMax`; `FinMass`/`E`/`Prb` (102 theorems total) | done |
| `P1_Obstruction` | §3.1 framework + `Wk` recursion; `thm:finite-horizon` (soundness + policy-tree completeness, obstruction-tree duality `blocked_iff`); `prop:ladder` (descending kernels); `thm:onestep`; `def:kernel`/`prop:selector` (coinductive `EpiK`); `thm:common-action` discrete core; `prop:monotone` (action + disturbance constituents, finite-horizon); `rem:robust-farkas` (perturbation margin); `def:certifier`/`prop:fibre`/`cor:certainly-safe`; `ex:hidden-mode` (complete instance) | done |
| `Minimax_Dual` | `thm:dual` certificate-soundness direction; `prop:gap` (convexity boundary, complete counterexample); `prop:recover` (i) ℓ1-normalized pair + (ii) singleton/Isaacs; `thm:benchmark` obstruction margin algebra | done |
| `Comp_Certification` | `prop:rows` robust-row soundness; the certified sandwich (`ρ ≤ J ≤ ρ + ē`) with positive-lower-bound obstruction and inflated-upper-bound negativity; `prop:value` margin-obstruction verdict; the dual-feasible certificate (`farkas_sound` restated) | done |
| `EBC_ExactBelief` | `lem:pairsum` (i) pair-sum bound with hold action; the observation-ladder doubling (exact-halving conditional mass) | done |
| `P3_ProbSufficiency` | `thm:recursion` expectation-kernel operator laws (monotone, constants, monotone iterates); `thm:agree`'s pointwise-ceiling core | done |
| `ARV_RegimeViability` | `lem:bracket` harvest-free multiplier bracket in full (both accounting forms, lower bracket, sub-unitary certificate, contraction readings) | done |
| `WS_WorkedSystems` | `prop:master` all three axes (policy/action, observation refinement, memory) as horizon-kernel monotonicity via the P1 machinery | done |
| `E1_ForecastLadder` | the ladder bookkeeping: telescoping identity, two-sided level bracket, ascent law | done |
| `P1_AssessmentSeparation` | the witness datum (§4.5) exactly; Theorem 5 (1)–(7) in full; Remark 2 + Proposition 3 (fourfold chain, full-cone identity); Theorem 9 (i)(iii) + Proposition 10; Lemma A (handshake identity + engine equivalence); Lemma B(i) convention + (ii) rational witness (the linear exception through a collapsed coordinate); **the master-equation reductions** — θ > 0 and θ < 0 at the abstract power interface (the averaging argument), θ = 0 (the LPI form) at the `GeoLaws` geometric-mean interface (swap-product identity `F·S = s²-1`, master row `s² ≥ 2`); **Theorem S2** — (i) the θ = 1 rung accepts every gap state; the Leontief identification `V⁰ = V_typ`; (ii) the false-certification witnesses: the harmonic member's Fibonacci pair (8/5 rejects / 13/8 accepts, the whole interval `[13/8, 2)`), the σ = 1/4 rung at 9/5, the `∀m` family (every `σ = 1/(m+1)` false-certifies `[2-2^-(m+1), 2)` via a Bernoulli lower bound), the σ = 2 rung's exact rational floor `5/4` (an iff, the ladder table's row), the σ = 3 rung at the canonical datum 6/5 (rational brackets `(1/3, 5/3)` proved in-layer; the critical-elasticity bracket `σ* ∈ (2, 3]`), the σ = 1 (LPI) witness 3/2 and the `√2` floor's bracket 141/100; the two-sided summary (only Leontief is uniformly safe) | done |
