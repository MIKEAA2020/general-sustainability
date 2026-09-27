# Lean Formalization Layer — `general-sustainability` paper family
### v2 — result-level index

> **This file supersedes `lean_README.md`.** It is issued as a new file
> rather than an edit, per the project's never-overwrite rule.
>
> **Why v2 exists.** The v1 theorem index resolved *papers* to *modules*,
> and labelled rows "done". That made a slot like
>
> > `P3_ProbSufficiency` | `thm:recursion` … ; `thm:agree`'s
> > pointwise-ceiling core | **done**
>
> read as an affirmative claim that those numbered results are formalized.
> It is not so: `P3_ProbSufficiency`'s four theorems are generic laws about
> an abstract kernel `Φ`, attached to no numbered result. v2 separates
> **result** from **machinery** from **instance** so that "done" can no
> longer be misread, and adds per-result resolution for every P3 result.
>
> See `lean_audit_v10.md` §5 and `lean_audit_v13.md` for the reasoning.

---

## How to read the index

Every entry carries one of four statuses. They are not interchangeable.

| Status | Meaning |
|---|---|
| **result** | A numbered result of the paper is stated and proved. |
| **machinery** | Supporting lemmas that are true and reusable but are **not** any numbered result. |
| **instance** | Numerical / grid-level checks. These live in the **Python verifier layer**, not here. |
| **partial** | Some sub-claims proved, others not; the index says which. |

Two standing facts, stated once so no reader has to infer them:

1. **No paper in this family claims formal verification.** Searching all ten
   `.tex` files for `lean|mechaniz|proof assistant|formally verified` returns
   zero hits in nine of them. Coverage is a property of *this* layer, not a
   claim made by the papers, and nothing here licenses a statement in a paper
   about what is or is not verified.
2. **Coverage is partial and is stated per result, below.** "Ten modules,
   395 theorems, green" is a fact about the code, not about the papers.

Citations of the form `vN` refer to `lean_audit_vN.md`, which records the
statement, the proof strategy, the axiom footprint, and — where a result was
*not* closed — precisely why.

## Architecture (unchanged from v1)

1. **Lean layer (this project): statement-level soundness.** Definitions and
   theorems of the frameworks. Every theorem is fully proved; there are **no
   `sorry`s and no extra axioms**.
2. **Python verifier layer (in `latex/`): instance-level checks.** The
   certificate batteries certify concrete numerical instances. The Lean layer
   proves the theorems that make those certificate checks *load-bearing* (a
   checked certificate implies the claimed property); the batteries supply
   the certificates.

## Fidelity policy (unchanged, one addition)

* Formalizations are **interface-level over `OrdField K`**
  (`Formalizations/Prelude.lean`): every statement is proved from the
  ordered-field interface alone, hence holds in any model; the papers'
  statements are the instance `K = ℝ`.
* Each theorem carries a header comment citing the paper's numbered result
  and quoting its statement gist.
* Deep classical existence results invoked from the literature (e.g. the
  separation theorem behind the *hard* direction of Farkas' lemma) are not
  re-proved; the direction the certificates use — soundness — is proved.
* **Addition.** Results requiring analysis beyond `OrdField` (notably
  `exp`/`ln` and concentration inequalities) are **out of reach of this
  layer by construction**. That is a statement about the layer, never about
  the truth of the result. `prop:probecount` is the standing example: it is
  not formalized here, and it has been independently verified as
  mathematics — see `lean_audit_v10.md` §3 and `verify_probecount.py`.

## Build

```
cd lean
lake build          # needs only the pinned toolchain, no network, no Mathlib
```

`lean-toolchain` is pinned to `leanprover/lean4:v4.34.1`. `.lake/` is
gitignored; only sources are versioned.

---

## Slot → module

| Slot | Paper (edition, source of record) | Modules |
|---|---|---|
| P1 | Obstruction calculus — theory main line (`paper2_obstruction_calculus_v55_Automatica_routes.tex`) | `P1_Obstruction`; **new:** `P1_TimingCertificate`, `P1_BeliefSafety`, `P1_BeliefSafety_Value`, `P1_BeliefSafety_Policy` |
| comp | Computational certification (`paper2_computational_certification_v18.tex`) | `Comp_Certification` |
| ws | Worked systems (`paper2_worked_systems_v17.tex`) | `WS_WorkedSystems` |
| minimax | Minimax dual certificates (`minimax_dual_certificates_v11.tex`) | `Minimax_Dual` |
| ebc | Exact belief computation (`paper2_exact_belief_computation_v10.tex`) | `EBC_ExactBelief` |
| P3 | Probabilistic sufficiency (`paper2_probabilistic_sufficiency_v11.tex`) | `P3_ProbSufficiency` (machinery); **new:** `P3_ClassLattice`, `P3_Sufficiency`, `P3_Deterministic`, `P3_Freeze_Noisy` |
| ARV | Applied regime viability (`applied_regime_viability_v9.tex`) | `ARV_RegimeViability` |
| E1 | Applied forecast ladder (`paperE1_cod_forecast_ladder_v59.tex`) | `E1_ForecastLadder` |
| P1-AS | Assessment separation — the head paper (`paper1_assessment_separation_v62.tex`) | `P1_AssessmentSeparation` |
| — | interface | `Prelude` |

## Theorem index

### `Prelude`
**machinery.** Ordered-field interface; `lsum`/`sumRange` (incl. telescoping);
`dotp`/`linComb` + `farkas_sound`; `IsMax`; `FinMass`/`E`/`Prb`.
Done — 102 theorems.

### `P1_Obstruction`
**result + machinery** (as v1, unchanged in v2): §3.1 framework + `Wk`
recursion; `thm:finite-horizon` (soundness + policy-tree completeness,
obstruction-tree duality `blocked_iff`); `prop:ladder`; `thm:onestep`;
`def:kernel`/`prop:selector` (coinductive `EpiK`); `thm:common-action`
discrete core; `prop:monotone`; `rem:robust-farkas`; `def:certifier`/
`prop:fibre`/`cor:certainly-safe`; `ex:hidden-mode`.

### `P1_TimingCertificate` — new (v8)
**result.** `thm:lp-instant`: the Farkas-certificate direction
(`blind_window_farkas_certifies`, `farkas_certifies_affine_system` — the
latter declaration-independent), monotonicity of infeasibility in the horizon
(`infeasible_mono_horizon`, hence `σ*` by bisection), and the soundness half
of the relaxation (`relaxation_sound`).
**Not formalized by choice:** the LP complexity count (needs a machine
model); the relaxation's incompleteness half (instance-level). See v6, v8.

### `P1_BeliefSafety` — new (v7)
**result.** `thm:pomdp`: `V_0(b) = b(𝒱)` (`V_zero`); the safety value is
nonnegative (`V_nonneg`); and — the load-bearing fact `prop:chance` invokes —
`V_{k+1} ≤ V_k`, *more steps cannot raise the survival probability*
(`V_mono_succ`), with `one_step_le_total` its choice-free base case.
**Modelling:** unnormalized sub-probability masses, positive-homogeneous
recursion; exit carried by `Σ_{x'} T ≤ 1` so the deficit is the paper's
`p(x,a)`; absorbing state `⊥` untracked. See v7.

### `P1_BeliefSafety_Value` — new (v8)
**result.** Closes the two gaps v7 flagged in itself:
*the homogeneity bridge* (`V_homogeneous`, `bayes_bridge` — including the
`ℙ(y|b,a) = 0` case the paper drops silently, proved zero rather than absent
by fiat); and **`prop:chance`** (`chance_bound`), via the equality form
`one_step_eq`, horizon antitonicity `V_antitone`, and `exit_add_survival`.

### `P1_BeliefSafety_Policy` — new (v8)
**result.** Gives `thm:pomdp`'s recursion real content. `Pol`, `J`, `PolIn`;
**`V_is_max_over_policies`** — `V` dominates every in-universe policy
(`J_dominated`) and is attained by one (`V_attained`). This is
Smallwood–Sondik's recursion proved rather than cited; without it the
recursion identity was `rfl`, i.e. content-free (v7 §3.1).

### `Minimax_Dual`, `Comp_Certification`, `EBC_ExactBelief`, `ARV_RegimeViability`, `WS_WorkedSystems`, `E1_ForecastLadder`
**result** (as v1, unchanged in v2): `thm:dual` soundness direction;
`prop:gap`; `prop:recover`; `thm:benchmark`; `prop:rows`, the certified
sandwich, `prop:value`; `lem:pairsum`; `lem:bracket`; `prop:master`; ladder
bookkeeping.

### `P3_ProbSufficiency` — **corrected in v2**
**machinery.** Four generic laws for an abstract expectation kernel `Φ`:
`Φ_mono`, `Φ_const`, `Φ_le_const`, `iterΦ_mono`.
**These are true and reusable, but they are NOT `thm:recursion` and NOT
`thm:agree`'s core.** v1's index labelled this row as those results with
status "done"; that was an over-claim and is corrected here. No P3 numbered
result was formalized by this module. See v9 §1, v13 §3.

### P3 — result-level index (v2)

All 18 numbered results of `paper2_probabilistic_sufficiency_v11.tex`.

| # | Result | Status | Module / where |
|---|---|---|---|
| 1 | `thm:recursion` | **result** | `P3_Sufficiency.VAdm`, `recursion_normalized`, `VAdm_mono_adm` (v11) |
| 2 | `thm:support` | **partial** | min-mass consequence in `P3_Deterministic.min_mass_bound` (v12); the support identity `supp(b⁺)=Post(supp b,a,y)` is **not** proved — needs a disturbance weighting + `lsum` strict-positivity |
| 3 | `prop:antichain` | **partial** | (i) `Vfam`/`bS` in `P3_Freeze_Noisy` (v13); (ii) alpha-vector characterisation not proved |
| 4 | `cor:closed` | **instance** | Python layer |
| 5 | `thm:parametric` | **instance** | Python layer |
| 6 | `prop:pl` | **partial** | max-of-linear-functionals feasible; convexity over `OrdField` not closed |
| 7 | `prop:degen` | **result** | `P3_Deterministic.VR`, `VR_eq_total_of_jointly_surviving` (v12) |
| 8 | `prop:freeze` | **partial** | nesting `Sfam_nesting`, antitonicity `Vfam_antitone`, `2^{\|supp b\|}` magnitude `Sfam0_card_le`/`subsetsOf_length`, range `Vfam_finite_range` (v13); the literal **count** of strict decreases is not proved |
| 9 | `prop:deficit` | **result** | (i) `deficit_chance`, (ii) `min_mass_bound`, (iii) `deficit_mono` — all three parts (v11, v12) |
| 10 | `thm:agree` | **instance** | 48-cell grid; Python layer |
| 11 | `thm:lattice` (i) | **result** | `P3_ClassLattice.class_monotone` (axiom-free), `class_le_unrestricted` (v9) |
| 12 | `thm:class` | **instance** | needs delayed-instance dynamics |
| 13 | `prop:learn` | **instance** | Python layer |
| 14 | `prop:pathdeficit` | **result** | `P3_Sufficiency.path_deficit` (choice-free) (v11) |
| 15 | `prop:noisyprobe` | **result** | `P3_Freeze_Noisy.three_levels`, `mixture_nonneg` (v13); instance thresholds not formalized |
| 16 | `prop:dr` (i) | **result** | `P3_ClassLattice.contam_lower`, `contam_sharp` (v9) |
| 17 | `prop:probecount` | **out of reach of this layer** | `exp`/`ln` in the statement, Stirling in the proof. **Independently verified as mathematics** — 118 checks, 0 failures — see `verify_probecount.py`, v10 §3 |
| 18 | `prop:additivelaw` | **instance** | needs additive-drift dynamics |

**P3 totals:** 7 results formalized · 4 partial · 6 instance-level ·
1 out of reach. The formalizable backlog is empty.

### `P1_AssessmentSeparation`
**result** (as v1, unchanged in v2): the witness datum (§4.5); Theorem 5
(1)–(7); Remark 2 + Proposition 3; Theorem 9 (i)(iii) + Proposition 10;
Lemma A; Lemma B; the master-equation reductions; Theorem S2 with its
false-certification witnesses.
