# Lean Formalization Layer — `general-sustainability` paper family

This directory contains a Lean 4 formalization of the **core theorem layer** of
the paper family in `arena agent 1/paper rewrites/latex/`. One module per slot:

| Slot | Paper (edition, source of record) | Module |
|---|---|---|
| P1 | Obstruction calculus — theory main line (2026b, `paper2_obstruction_calculus_v53_Automatica_routes.tex`) | `Formalizations.P1_Obstruction` |
| comp | Computational certification (2026d, `paper2_computational_certification_v15.tex`) | `Formalizations.Comp_Certification` |
| ws | Worked systems (2026c, `paper2_worked_systems_v15.tex`) | `Formalizations.WS_WorkedSystems` |
| minimax | Minimax dual certificates (2026g, `minimax_dual_certificates_v7.tex`) | `Formalizations.Minimax_Dual` |
| ebc | Exact belief computation (2026f, `paper2_exact_belief_computation_v6.tex`) | `Formalizations.EBC_ExactBelief` |
| P3 | Probabilistic sufficiency (2026e, `paper2_probabilistic_sufficiency_v8.tex`) | `Formalizations.P3_ProbSufficiency` |
| ARV | Applied regime viability (2026a, `applied_regime_viability_v6.tex`) | `Formalizations.ARV_RegimeViability` |
| E1 | Applied forecast ladder (E1, `paperE1_cod_forecast_ladder_v56.tex`) | `Formalizations.E1_ForecastLadder` |

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

(to be completed as modules land)

| Module | Formalizes (paper items) | Status |
|---|---|---|
| `Prelude` | ordered-field interface; `lsum`/`sumRange` (incl. telescoping); `dotp`/`linComb` + `farkas_sound`; `IsMax`; `FinMass`/`E`/`Prb` | done |
| `P1_Obstruction` | §3.1 framework + `Wk` recursion; `thm:finite-horizon` (soundness + policy-tree completeness, obstruction-tree duality `blocked_iff`); `prop:ladder` (descending kernels); `thm:onestep`; `def:kernel`/`prop:selector` (coinductive `EpiK`); `thm:common-action` discrete core; `prop:monotone` (action + disturbance constituents, finite-horizon); `rem:robust-farkas` (perturbation margin); `def:certifier`/`prop:fibre`/`cor:certainly-safe`; `ex:hidden-mode` (complete instance) | done |
| `Minimax_Dual` | `thm:dual` certificate-soundness direction; `prop:gap` (convexity boundary, complete); `prop:recover` (i)+(ii); `thm:benchmark` obstruction algebra | done |
