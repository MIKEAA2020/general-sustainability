# Lean Formalization Layer — `general-sustainability` paper family
### v5 — result-level index

> **This file supersedes `lean_README_v4.md`.** Issued as a new file, not an
> edit, per the project's never-overwrite rule.
>
> **Correction carried in v5.** `lean_audit_v25.md` reported the P3 totals as
> "12 complete · 0 partial · 6 instance · 1 out of reach", which sums to 19
> against a table of 18 rows. The correct figure is **11 complete**; the
> error came from counting `prop:deficit` (i)(ii)(iii) as three results in a
> table where it is one row. v5 states 11. Flagged rather than quietly fixed,
> because a miscount in a coverage index is exactly the class of error this
> index exists to catch.
>
> **Why v3.** v2 corrected the `P3_ProbSufficiency` over-claim and added
> per-result resolution for P3. `lean_audit_v14.md` then audited the seven
> non-P3 modules against their papers and found four distinct failure modes;
> `lean_audit_v15.md` closed two of them with new modules and re-audited
> `P1_AssessmentSeparation`; `lean_audit_v16.md` re-audited the last
> unchecked slot, `EBC_ExactBelief` (1 of 8 results), and relabelled
> `Comp_Certification`'s scaffolding as input-taking procedures. v4 folds
> all of that in, and — with `EBC_ExactBelief_v2` and
> `P1_AssessmentSeparation_v5` — reports a **zero-warning** build.

---

## How to read the index

Every entry carries one of four statuses. They are not interchangeable.

| Status | Meaning |
|---|---|
| **result** | A numbered result of the paper is stated and proved. |
| **machinery** | Supporting lemmas, true and reusable, but **not** any numbered result. |
| **instance** | Numerical / grid-level checks. These live in the **Python verifier layer**, not here. |
| **partial** | Some sub-claims proved, others not; the index says which. |

Two standing facts, stated once so no reader has to infer them:

1. **No paper in this family claims formal verification.** Coverage is a
   property of *this* layer, not a claim made by the papers, and nothing here
   licenses a statement in a paper about what is or is not verified. The
   coverage statement belongs in this index and in the audit reports — never
   in a paper's body.
2. **Coverage is partial and is stated per result, below.** "Ten modules,
   395 theorems, green" is a fact about the code, not about the papers. That
   count also includes ~325 KB of **unimported legacy** (see
   `P1_AssessmentSeparation` below).

Citations `vN` refer to `lean_audit_vN.md`, which records the statement, the
proof strategy, the axiom footprint, and — where a result was *not* closed —
precisely why.

## Build state

`lake build` → **rc = 0, 32 jobs**. Zero `sorry`. **Zero warnings.**

The 7 warnings reported in v3 are cleared, without editing any existing file:
`EBC_ExactBelief_v2` drops the four dead simp arguments from `coord_bound`
(fourteen carried, four unreachable in every branch), and
`P1_AssessmentSeparation_v5` underscores the three unreferenced binders
(`hq` ×2, `hnn`). Both are drop-in replacements and are now the imported
versions. Behaviour is unchanged.

## Architecture

1. **Lean layer (this project): statement-level soundness.** Definitions and
   theorems of the frameworks. Every theorem is fully proved; no `sorry`s, no
   extra axioms.
2. **Python verifier layer (in `latex/`): instance-level checks.** The
   certificate batteries certify concrete numerical instances. The Lean layer
   proves the theorems that make those checks *load-bearing*; the batteries
   supply the certificates.

## Fidelity policy

* **Interface-level over `OrdField K`** (`Formalizations/Prelude.lean`):
  every statement is proved from the ordered-field interface alone, hence
  holds in any model; the papers' statements are the instance `K = ℝ`.
* Each theorem carries a header comment citing the paper's numbered result.
* Deep classical existence results invoked from the literature (e.g. the
  separation theorem behind the *hard* direction of Farkas) are not re-proved;
  the direction the certificates use — soundness — is proved.
* Results requiring analysis beyond `OrdField` (`exp`/`ln`, concentration
  inequalities, real exponents, IVT, weak-\* compactness) are **out of reach
  of this layer by construction**. That is a statement about the layer, never
  about the truth of the result. Where a paper step is replaced by a
  constructive witness, the index says so.

## Build

```
cd lean
lake build          # needs only the pinned toolchain, no network, no Mathlib
```

`lean-toolchain` is pinned to `leanprover/lean4:v4.34.1`. `.lake/` is
gitignored; only sources are versioned.

> **`Formalizations.lean` is part of the deliverable.** Until v21 the pushed
> branch carried every module but an **out-of-date aggregate import list**, so
> `lake build` on a fresh clone compiled 13 jobs / 9 warnings while the index
> advertised 27 / 0: every module added from v7 on was present but orphaned.
> Fixed in `e555b04`. Standing rule: any push that adds a module must also
> push the import list, and the build must be re-verified from a **fresh
> clone**, never from the working tree.

---

## Slot → module

| Slot | Paper (edition, source of record) | Modules |
|---|---|---|
| P1 | Obstruction calculus (`paper2_obstruction_calculus_v55_Automatica_routes.tex`) | `P1_Obstruction`; `P1_TimingCertificate`, `P1_BeliefSafety`, `P1_BeliefSafety_Value`, `P1_BeliefSafety_Policy` |
| comp | Computational certification (`paper2_computational_certification_v18.tex`) | `Comp_Certification`, `Comp_Certification_v2` |
| ws | Worked systems (`paper2_worked_systems_v17.tex`) | `WS_WorkedSystems`, `WS_WorkedSystems_v2` |
| minimax | Minimax dual certificates (`minimax_dual_certificates_v11.tex`) | `Minimax_Dual` |
| ebc | Exact belief computation (`paper2_exact_belief_computation_v10.tex`) | `EBC_ExactBelief_v2` |
| P3 | Probabilistic sufficiency (`paper2_probabilistic_sufficiency_v11.tex`) | `P3_ProbSufficiency` (machinery); `P3_ClassLattice`, `P3_Sufficiency`, `P3_Deterministic`, `P3_Freeze_Noisy`, `P3_Freeze_Noisy_v2`, `P3_Convexity`, `P3_Antichain`, `P3_Antichain_v2`, `P3_Antichain_v3`, `P3_PiecewiseLinear`, `P3_RobustPL`, `P3_Support` |
| ARV | Applied regime viability (`applied_regime_viability_v9.tex`) | `ARV_RegimeViability`, `ARV_RegimeViability_v2` |
| E1 | Applied forecast ladder (`paperE1_cod_forecast_ladder_v59.tex`) | `E1_ForecastLadder` |
| P1-AS | Assessment separation (`paper1_assessment_separation_v62.tex`) | `P1_AssessmentSeparation_v5` |
| — | interface | `Prelude` |

## Theorem index

### `Prelude` — machinery
Ordered-field interface; `lsum`/`sumRange` (incl. telescoping);
`dotp`/`linComb` + `farkas_sound`; `IsMax`; `FinMass`/`E`/`Prb`. 102
theorems. `OrdField` supplies `le_total` but **no `max`**; modules needing a
maximum define it locally (see `ARV_RegimeViability_v2.omax`).

### `P1_Obstruction` — result
§3.1 framework + `Wk` recursion; `thm:finite-horizon` (soundness +
policy-tree completeness, obstruction-tree duality `blocked_iff`);
`prop:ladder`; `thm:onestep`; `def:kernel`/`prop:selector` (coinductive
`EpiK`); `thm:common-action` discrete core; `prop:monotone`;
`rem:robust-farkas`; `def:certifier`/`prop:fibre`/`cor:certainly-safe`;
`ex:hidden-mode`.

### `P1_TimingCertificate` — result
`thm:lp-instant`: the Farkas-certificate direction
(`blind_window_farkas_certifies`, `farkas_certifies_affine_system`),
monotonicity of infeasibility in the horizon (`infeasible_mono_horizon`,
hence `σ*` by bisection), and the soundness half of the relaxation.
**Not formalized by choice:** the LP complexity count; the relaxation's
incompleteness half. See v6, v8.

### `P1_BeliefSafety` — result
`thm:pomdp`: `V_0(b) = b(𝒱)` (`V_zero`); `V_nonneg`; and `V_{k+1} ≤ V_k` —
more steps cannot raise the survival probability (`V_mono_succ`). v7.

### `P1_BeliefSafety_Value` — result
The homogeneity bridge (`V_homogeneous`, `bayes_bridge` — including the
`ℙ(y|b,a) = 0` case the paper drops) and **`prop:chance`** (`chance_bound`).

### `P1_BeliefSafety_Policy` — result
`Pol`, `J`, `PolIn`; **`V_is_max_over_policies`** — `V` dominates every
in-universe policy and is attained by one. Smallwood–Sondik proved rather
than cited; without it the recursion identity was `rfl`.

### `Minimax_Dual` — result
`thm:dual` certificate-soundness direction (`dual_certificate_sound`);
`prop:gap` (`parity_common_safe_empty`, `parity_no_measure_certifies`);
`prop:recover` (ii) (`singleton_uniform`, `singleton_every_measure`,
`singleton_worst_witnesses`); `thm:benchmark` (`benchmark_obstruction`).
**Audited in v14 — no defects found.** The healthiest of the seven.

### `Comp_Certification` (+ `_v2`) — **1 result + 1 restatement + 4 input-taking procedures**
Corrected in v3 (v14, mode D); **relabelled in v4** (v16).

The four are **verdict procedures**, not results: they take the sandwich and
the characterization as **inputs** and read off the verdict. `Comp_Certification_v2`
re-states them under names that say so — `sandwich_verdict_lower`,
`sandwich_verdict_upper`, `sandwich_verdict`, `characterization_verdict` — each a
one-line delegation to its v1 counterpart, so **no proof is duplicated**. Two
headers say outright what v1 did not: `sandwich_verdict` does not establish
that the computed `ρ` and `ē` bracket `J`; `characterization_verdict`'s
`hchar` is the "consequently" clause of `prop:value`, whose real content —
existence of the minimum, from weak-\* compactness of `L^\infty(I_r; U)` —
lies beyond `OrdField`. Both new theorems are **axiom-free**.

| Theorem | Status |
|---|---|
| `robust_row_sound` | **result** — `prop:rows`, soundness direction |
| `dual_feasible_certificate` | restatement of `Prelude.farkas_sound` |
| `positive_bound_obstruction`, `inflated_upper_bound_negative` | one-line consequences |
| `certified_sandwich` | **assumes** `hlo : ρ ≤ J`, `hhi : J ≤ ρ + ē`; does not establish the sandwich |
| `margin_obstruction_verdict` | **assumes** `hchar : ((∃ π, ∀ a, F a π ≤ 0) ↔ J ≤ 0)` |

`prop:value`'s real content is the existence of a minimum, which the paper
grounds in **weak-\* compactness of `L^∞(I_r;U)`** and weak-\* continuity of
`F_a` — beyond `OrdField`, and a legitimate reason not to formalize it. What
the module proves is a three-line consequence under a hypothesis that *is*
the paper's "consequently" clause. The four scaffolding theorems are
nevertheless what the Python certificate layer consumes; they should be read
as **verdict procedures taking the sandwich and the characterization as
inputs**, which is how v3 now labels them.

### `EBC_ExactBelief_v2` — **result, 1 of 8** (audited in v16)
`lem:pairsum` **(i)** — the pair-sum bound (`pair_sum_bound`) and the hold
action (`hold_action_zero`) — an **exact** match to the paper:
`agreeMass` counts agreeing coordinates, which is precisely the paper's
`m − h`. `lem:pairsum` **(ii)** is out of reach (it asserts a `liminf`
bound). `ladder_doubling` is the abstract exact-halving step behind
**`prop:ladder`**, not that proposition, which is instance-level (sixteen
cells, four probes, two `z₀` regimes). The paper has **8 named results**;
this module formalizes one. v2 additionally clears the 4 warnings v1
carried.

### `ARV_RegimeViability` (+ `_v2`) — **result**
`lem:bracket` (harvest-free multiplier bracket), now complete.

* v1: both accounting forms (`bracket_form1`, `bracket_form2`), the lower
  bracket in both forms, the forward sub-unitary certificate, the contraction
  readings. Faithful — the paper genuinely *supposes* the accounting form, so
  `hform` is a transcribed hypothesis, not a smuggled conclusion.
* **v2 closes the two gaps v14 found:** the `max` upper bound
  (`bracket_upper_form1/2`, `bracket_sandwich_form1/2`) and the **iff**
  (`bracket_upper_lt_one_iff`), plus sharper per-form statements
  (`bracket_subunitary_form1/2`). Defines `omax` locally since `OrdField`
  has no `max`.
* v1's header cites v6 of the paper; the current edition is v9. Content
  unchanged; v2 cites v9.

### `WS_WorkedSystems` (+ `_v2`) — result
`prop:master`. Two distinct lemmas, not three:

* `Wk_mono_obs` — **(ii) observations**. Genuinely distinct: changes the
  observation *type* via `refineObs`.
* `master_monotone` (`WS_WorkedSystems_v2`) — the **single** canonical proof
  serving **(i) policies** and **(iii) memory** and `prop:monotone`'s action
  constituent. Axiom-free.

`Wk_mono_adm` / `master_action_axis` / `master_memory_axis` are verbatim the
same theorem (v14, mode B) and are now aliases of `master_monotone`. The
paper itself notes all three share one induction, so what was misleading was
the **count**, not the content.

### `E1_ForecastLadder` — **machinery**
Corrected in v3 (v14, modes A and C — the weakest entry).

`paperE1_cod_forecast_ladder_v59.tex` contains **zero** `theorem`,
`proposition`, `lemma` or `corollary` environments; its only labels are
sections, figures and tables. **There is no ladder result in the paper to
formalize.** The module's five theorems are generic `sumRange` arithmetic on
`Nat → K`: `ladder_telescope` is literally `sumRange_telescope f N`, a
one-line alias of `Prelude:559`; `ladder_bound_upper`/`_lower` are
`sumRange` monotonicity, already covered by `sumRange_le_sumRange'`;
`ladder_bracket` is their conjunction; `ladder_ascent` is induction on `Nat`.
Nothing mentions a ladder, a level, a forecast or a margin.

### `P3_ProbSufficiency` — **machinery**
Four generic laws for an abstract expectation kernel `Φ`: `Φ_mono`,
`Φ_const`, `Φ_le_const`, `iterΦ_mono`. True and reusable, but **NOT**
`thm:recursion` and **NOT** `thm:agree`'s core. v1's index labelled this row
as those results with status "done"; corrected in v2, retained here.

### P3 — result-level index

All 18 numbered results of `paper2_probabilistic_sufficiency_v11.tex`.

| # | Result | Status | Module / where |
|---|---|---|---|
| 1 | `thm:recursion` | **result** | `P3_Sufficiency.VAdm`, `recursion_normalized` (v11) |
| 2 | `thm:support` | **result** | support identity `supp(b⁺) = Post(supp b, a, y)` — `P3_Support.support_identity` (v25). Stated on `SafeMDP`, not `DetMDP`: the theorem is about the *degeneration* of stochastic kernels, so it needs genuine `T` and `g` to degenerate. Consequences 1–3 not proved (see v25) |
| 3 | `prop:antichain` | **result** | (i) v13; (ii) alpha-vectors = indicators of maximal elements, `P3_Antichain_v2.Vfam_prune_eq` (v21); (iii) antichain (v20); (iv) deficit = min `b(S^c)`, `P3_Antichain_v3.deficit_eq_min_compl` (v22). **Sperner count in (iii) not claimed** — a separate theorem |
| 4 | `cor:closed` | **instance** | Python layer |
| 5 | `thm:parametric` | **instance** | Python layer |
| 6 | `prop:pl` | **result** | convexity (`P3_Convexity.VAdm_convex`, v19); witness set `Γ_k` and growth law `\|Γ_{k+1}\| ≤ \|A\|·\|Γ_k\|^{Y}` (`P3_PiecewiseLinear`, v23); segment form `V_k = max_{α∈Γ_k} αᵀb` (`P3_RobustPL.VR_eq_max_alpha`, v24). **Rationality clause not formalized** (needs `K := ℚ`); the general stochastic masked backup is out of scope by design — it is the *other* operator (v24) |
| 7 | `prop:degen` | **result** | `P3_Deterministic.VR_eq_total_of_jointly_surviving` (v12) |
| 8 | `prop:freeze` | **result** | nesting, antitonicity, `2^{\|supp b\|}` magnitude, range (v13); drop **count** `P3_Freeze_Noisy_v2.prop_freeze_drop_count` (v18) |
| 9 | `prop:deficit` | **result** | (i)(ii)(iii) — all three parts (v11, v12) |
| 10 | `thm:agree` | **instance** | 48-cell grid; Python layer |
| 11 | `thm:lattice` (i) | **result** | `P3_ClassLattice.class_monotone` (axiom-free) (v9) |
| 12 | `thm:class` | **instance** | needs delayed-instance dynamics |
| 13 | `prop:learn` | **instance** | Python layer |
| 14 | `prop:pathdeficit` | **result** | `P3_Sufficiency.path_deficit` (choice-free) (v11) |
| 15 | `prop:noisyprobe` | **result** | `P3_Freeze_Noisy.three_levels` (v13); instance thresholds not formalized |
| 16 | `prop:dr` (i) | **result** | `P3_ClassLattice.contam_lower`, `contam_sharp` (v9) |
| 17 | `prop:probecount` | **out of reach of this layer** | `exp`/`ln` + Stirling. **Verified as mathematics**: 118 checks, 0 failures — `verify_probecount.py`, v10 §3 |
| 18 | `prop:additivelaw` | **instance** | needs additive-drift dynamics |

**P3 totals: 11 result · 0 partial · 6 instance · 1 out of reach** (sums to
the 18 rows above). Formalizable backlog: empty.

Every one of the four results that was still partial at v4 is now closed:
`prop:freeze` (v18), `prop:pl` (v19, v23, v24), `prop:antichain` (v20, v21,
v22), `thm:support` (v25). What remains unclaimed in P3 is not a gap in the
work but a scope statement: the Sperner count, `prop:pl`'s rationality
clause, and the three consequences of `thm:support` — each recorded with its
reason in the corresponding audit report.

### `P3_Support` — result (v25)
`thm:support`, the support identity. `DetKernels` makes the paper's
"deterministic kernels and deterministic observation maps" an explicit `0/1`
hypothesis on `SafeMDP`'s `T` and `g`; `obsMass_eq_filter` collapses the
posterior to a filtered sum; `support_identity` is the iff. Builds two `lsum`
facts the layer lacked (`le_lsum_of_mem`, `lsum_pos_exists`).

### `P3_RobustPL` — result (v24)
`prop:pl`, segment form. **`alphaSeg`/`GammaSeg` and
`VR_eq_max_alpha`**: `V_k(b) = max_{α ∈ Γ_k} αᵀ b` with `α^seg` the survival
indicators. `survT_adversarial` makes the adversarial disturbance reading
explicit. v24 also **corrects v23**: the paper (`rem:operators`, `prop:degen`)
prescribes the adversarial reading for the deterministic layer, and
`P3_Deterministic.survT` already implemented it — so no disturbance weighting
was ever missing.

### `P3_PiecewiseLinear` — result (v23)
`prop:pl`, growth law. `selections`/`selections_length` (`|Γ_k|^{|Y|}`),
`dedup` (absent from this stdlib), `step_length` (**exactly** `|A|·|Γ|^{|Y|}`
before dedup), `Gamma_succ_length_le`. The law is independent of what the
backup operator does.

### `P3_Antichain_v3` — result (v22)
`prop:antichain` (iv). `lmax_sub_dual` (this layer has `lmax` but no
max/min duality), `complOf`, `bS_compl` (`b(S) + b(S^c) = 1`, under an
explicit normalization hypothesis), `deficit_eq_min_compl`,
`bS_compl_singleton` (the min-mass case).

### `P3_Antichain_v2` — result (v21)
`prop:antichain` (ii). `mem_erase_iff` (`List.mem_erase` is absent here),
`lsum_eq_of_mem_iff`, `bS_mono_of_subset`, `exists_maximal_above` (by
induction on the family — no termination measure), `Vfam_prune_eq`.

### `P1_AssessmentSeparation_v5` — result
**Audited in v15 — no defects found; the best-documented module in the layer.**
The witness datum (§4.5); Theorem 5 (1)–(7); Remark 2 + Proposition 3;
Theorem 9 (i)(iii) + Proposition 10; Lemma A (handshake identity + engine
equivalence); Lemma B; the master-equation reductions; Theorem S2.

Every specific numeric claim traces to code: the Fibonacci witnesses 8/5
rejects / 13/8 accepts, `σ = 1/4` at 9/5, the `∀m` false-certification
family, the `σ = 2` floor `5/4` as an iff, the `σ = 3` datum 6/5 with
brackets `(1/3, 5/3)`, the LPI witness 3/2, and the `√2` floor's `141/100`.

Two things this module does that others should copy:

* **It separates convention from theorem.** Lemma B(i) is a *convention*,
  "stipulated … not derived from the rung algebra (it cannot be: see
  `collapse_convention_not_implied`)". A theorem that the convention is **not**
  implied is the opposite of promoting a conclusion to a hypothesis.
* **It states what is not formalized, and why.** Theorem S1 (nesting) is
  "genuinely analytic (real exponents)"; the relative-interior topology of
  Theorem 5(4) and the IVT step in S2(ii) are replaced by explicit rational
  interval witnesses, labelled a **constructive strengthening**, not passed
  off as the original.

**Correction carried in v3:** the earlier "Theorem 5 (1)–(7) **in full**" is
over-stated — 5(4)'s topology is *replaced*, not formalized as written.

**Housekeeping:** four versions now exist (`P1_AssessmentSeparation.lean`,
`_v3`, `_v4`, `_v5`; ~490 KB, 246–247 declarations each) but **only `_v5` is
imported**. The rest is unimported legacy that inflates the advertised
395-theorem count; v5 differs from v4 only in three underscored binders. This
is the direct cost of the never-overwrite rule applied to a 165 KB file, and
it is worth pruning.
