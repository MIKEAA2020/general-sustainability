# Lean Formalization Layer — `general-sustainability` paper family
### v7 — result-level index

> **This file supersedes `lean_README_v6.md`.** Issued as a new file, not an
> edit, per the project's never-overwrite rule.
>
> **What changed since v6 (v31).** Two modules: `P3_Rational` and
> `P3_Binomial`; the build went 38 → 40 jobs, 35 → 37 imports.
>
> 1. **`P3_Rational` (item 4).** `prop:pl`'s closing clause — over rational
>    data every `α` is an exact rational vector, every `V^Π_k(b)` at a
>    rational belief is an exact rational, and the attaining witness is
>    part of the computation — is now proved as a **closure theorem** for
>    the segment form, over an abstract `RatSub K` interface rather than
>    by instantiating at `K = ℚ`, where the claim would be vacuous. The
>    module also gives the layer its **first concrete model**
>    (`instance ratOrdField : OrdField Rat`), so every theorem in the
>    layer now has a non-vacuous interpretation.
> 2. **`P3_Binomial` (item 5, partial).** `prop:antichain` (iii)'s Sperner
>    bound needs binomial coefficients, which this dependency-free layer
>    does not have (`Nat.choose` is an unknown identifier). The module
>    defines `choose` and proves its laws. **The Sperner bound itself is
>    NOT claimed** — see the entry below and `lean_audit_v31.md` for
>    exactly what remains and why.
>
> **What changed since v5.** Six modules were added — `P3_Bridge` (v26),
> `P3_Viable` (v27), `P3_Feedback` (v28), `P3_FeedbackValue` (v29),
> `P3_SurvivableAdm` and `P3_BlindValue` (v30) — and the build went 32 → 38
> jobs, 30 → 35 imports. Substantively:
>
> 1. **`thm:support` is now claimed in full, on both readings.** v5 recorded
>    its three consequences as not proved. Consequence 1 is
>    `P3_FeedbackValue.VFb_eq_total_iff_Wmem` (v29) for the unrestricted
>    sequential class — which v28 established from the text is the class
>    `thm:support` names — and `P3_BlindValue.VR_eq_total_iff_Wblind` (v30)
>    for the blind class. Consequences 2 and 3 are `VFb_min_mass_bound` and
>    `VFb_antitone`.
> 2. **The `𝒲_k` ambiguity is resolved by the text, not by fiat.** v27
>    defined two viable-set recursions and refused to choose. v28 read
>    `def:value` (`Π = Π_seq`, "the class of all sequential policies") and
>    proved the two notions differ (`Wmem_not_le_Wblind`, on a
>    deterministic-kernel model). v29/v30 then formalized both.
> 3. **A fidelity defect is recorded in `prop:antichain` (i) and
>    `prop:freeze`.** `Survivable` omits the admissibility constraint the
>    paper's `𝒮_k` carries; `P3_SurvivableAdm` supplies the corrected
>    objects additively. See those rows.
>
> **Correction carried forward from v5.** `lean_audit_v25.md` reported the
> P3 totals as "12 complete · 0 partial · 6 instance · 1 out of reach",
> which sums to 19 against a table of 18 rows. The correct figure is
> **11 complete**. Flagged rather than quietly fixed, because a miscount in
> a coverage index is exactly the class of error this index exists to catch.
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
| **partial** | Some sub-concepts proved, others not; the index says which. |

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

`lake build` → **rc = 0, 40 jobs** (37 imported modules). Zero `sorry`.
**Zero warnings.** Verified from a **fresh clone**, never the working tree.

The 7 warnings reported in v3 are cleared, without editing any existing file:
`EBC_ExactBelief_v2` drops the four dead simp arguments from `coord_bound`,
and `P1_AssessmentSeparation_v5` underscores the three unreferenced binders
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
  inequalities, real exponents, IVT, weak-\\* compactness) are **out of reach
  of this layer by construction**. That is a statement about the layer, never
  about the truth of the result. Where a paper step is replaced by a
  constructive witness, the index says so.
* **Where a paper's own text is ambiguous, the ambiguity is not resolved in
  code.** Both readings are defined, the relation between them is proved, and
  the choice is reported for the paper to make (`P3_Viable`, `P3_Feedback`).

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
>
> **Corollary, learned the hard way in v28.** The v28 push script rewrote
> only the first path match per line and silently clobbered
> `P3_Viable.lean` with the contents of `P3_Feedback.lean`; it was caught by
> md5-comparing against the working tree and repaired in `ec5acc6`. Push
> scripts list **source and destination paths explicitly** — never derive one
> from the other by substitution.

---

## Slot → module

| Slot | Paper (edition, source of record) | Modules |
|---|---|---|
| P1 | Obstruction calculus (`paper2_obstruction_calculus_v55_Automatica_routes.tex`) | `P1_Obstruction`; `P1_TimingCertificate`, `P1_BeliefSafety`, `P1_BeliefSafety_Value`, `P1_BeliefSafety_Policy` |
| comp | Computational certification (`paper2_computational_certification_v18.tex`) | `Comp_Certification`, `Comp_Certification_v2` |
| ws | Worked systems (`paper2_worked_systems_v17.tex`) | `WS_WorkedSystems`, `WS_WorkedSystems_v2` |
| minimax | Minimax dual certificates (`minimax_dual_certificates_v11.tex`) | `Minimax_Dual` |
| ebc | Exact belief computation (`paper2_exact_belief_computation_v10.tex`) | `EBC_ExactBelief_v2` |
| P3 | Probabilistic sufficiency (`paper2_probabilistic_sufficiency_v11.tex`) | `P3_ProbSufficiency` (machinery); `P3_ClassLattice`, `P3_Sufficiency`, `P3_Deterministic`, `P3_Freeze_Noisy`, `P3_Freeze_Noisy_v2`, `P3_Convexity`, `P3_Antichain`, `P3_Antichain_v2`, `P3_Antichain_v3`, `P3_PiecewiseLinear`, `P3_RobustPL`, `P3_Support`, `P3_Bridge`, `P3_Viable`, `P3_Feedback`, `P3_FeedbackValue`, `P3_SurvivableAdm`, `P3_BlindValue` |
| ARV | Applied regime viability (`applied_regime_viability_v9.tex`) | `ARV_RegimeViability`, `ARV_RegimeViability_v2` |
| E1 | Applied forecast ladder (`paperE1_cod_forecast_ladder_v59.tex`) | `E1_ForecastLadder` |
| P1-AS | Assessment separation (`paper1_assessment_separation_v62.tex`) | `P1_AssessmentSeparation_v5` |
| — | interface | `Prelude` |

## Theorem index

### `Prelude` — machinery
Ordered-field interface; `lsum`/`sumRange` (incl. telescoping);
`dotp`/`linComb` + `farkas_sound`; `IsMax`; `FinMass`/`E`/`Prb`. 102
theorems. `OrdField` supplies `le_total` but **no `max`**; modules needing a
maximum define `lmax`/`lmin` over lists.

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
| 2 | `thm:support` | **result** | support identity `supp(b⁺) = Post(supp b, a, y)` — `P3_Support.support_identity` (v25), stated on `SafeMDP` (the theorem is about the *degeneration* of stochastic kernels, so it needs genuine `T` and `g`). **Consequence 1** `VFb_eq_total_iff_Wmem` (v29) for `Π_seq`, and `VR_eq_total_iff_Wblind` (v30) for the blind class. **Consequence 2** `VFb_min_mass_bound` (v29), `min_mass_bound` (v12). **Consequence 3** `VFb_antitone` (v29), `Vfam_antitone` (v18) |
| 3 | `prop:antichain` | **result** (i) carries a correction — see below | (i) v13, corrected in v30 (`VfamAdm`); (ii) alpha-vectors = indicators of maximal elements, `P3_Antichain_v2.Vfam_prune_eq` (v21); (iii) antichain (v20); (iv) deficit = min `b(S^c)`, `P3_Antichain_v3.deficit_eq_min_compl` (v22). **Sperner count in (iii) not claimed** — a separate theorem |
| 4 | `cor:closed` | **instance** | Python layer |
| 5 | `thm:parametric` | **instance** | Python layer |
| 6 | `prop:pl` | **result** | convexity (`P3_Convexity.VAdm_convex`, v19); witness set `Γ_k` and growth law `\|Γ_{k+1}\| ≤ \|A\|·\|Γ_k\|^{Y}` (`P3_PiecewiseLinear`, v23); segment form `V_k = max_{α∈Γ_k} αᵀb` (`P3_RobustPL.VR_eq_max_alpha`, v24). **Rationality clause not formalized** (needs `K := ℚ`); the general stochastic masked backup is out of scope by design — it is the *other* operator (v24) |
| 7 | `prop:degen` | **result** | `P3_Deterministic.VR_eq_total_of_jointly_surviving` (v12); the `𝒲_k` form (both directions) is `P3_BlindValue.VR_eq_total_iff_Wblind` (v30) |
| 8 | `prop:freeze` | **result** (same correction as (3)) | nesting, antitonicity, `2^{\|supp b\|}` magnitude, range (v13); drop **count** `P3_Freeze_Noisy_v2.prop_freeze_drop_count` (v18); admissible-family form `VfamAdm_antitone`, `SfamAdm0_card_le`, `VfamAdm_finite_range` (v30) |
| 9 | `prop:deficit` | **result** | (i)(ii)(iii) — all three parts (v11, v12) |
| 10 | `thm:agree` | **instance** | 48-cell grid; Python layer |
| 11 | `thm:lattice` (i) | **result** | `P3_ClassLattice.class_monotone` (axiom-free) (v9). The middle equality's set-level form is `P3_Feedback.Wmem_eq_Wblind_of_blind` (v28) |
| 12 | `thm:class` | **instance** | needs delayed-instance dynamics |
| 13 | `prop:learn` | **instance** | Python layer |
| 14 | `prop:pathdeficit` | **result** | `P3_Sufficiency.path_deficit` (choice-free) (v11) |
| 15 | `prop:noisyprobe` | **result** | `P3_Freeze_Noisy.three_levels` (v13); instance thresholds not formalized |
| 16 | `prop:dr` (i) | **result** | `P3_ClassLattice.contam_lower`, `contam_sharp` (v9) |
| 17 | `prop:probecount` | **out of reach of this layer** | `exp`/`ln` + Stirling. **Verified as mathematics**: 118 checks, 0 failures — `verify_probecount.py`, v10 §3 |
| 18 | `prop:additivelaw` | **instance** | needs additive-drift dynamics |

**P3 totals: 11 result · 0 partial · 6 instance · 1 out of reach** (sums to
the 18 rows above). Formalizable backlog: empty.

**Correction carried in v30 (`prop:antichain` (i), `prop:freeze`).**
`Survivable` (`P3_Freeze_Noisy`) is `∃ u : Nat → A, ∀ x ∈ S → survK M k u x`
with **no constraint that `u` be admissible**, while `prop:antichain`
defines `𝒮_k` as the subsets survivable by one **admissible** class-element
and `DetMDP` carries `univA` for exactly that purpose. So `Sfam` — hence
`Vfam`, hence the v13/v18 formalizations of (i) and `prop:freeze` — range
over a family that can be **larger** than the paper's, and `Vfam` may
overstate the value. `P3_SurvivableAdm` supplies the corrected objects
(`SurvivableAdm`, `SfamAdm`, `VfamAdm`) additively and proves
`VfamAdm_le_Vfam`, so the old value is an upper bound on the corrected one.
The structural theorems (`VfamAdm_antitone`, `SfamAdm0_card_le`,
`VfamAdm_finite_range`) are re-proved for the corrected family; only the
*identification* with the paper's `𝒮_k` was affected.

What remains unclaimed in P3 is not a gap in the work but a scope statement:
the Sperner count in `prop:antichain` (iii), `prop:pl`'s rationality clause,
and the instance-level results — each recorded with its reason in the
corresponding audit report.

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

### `P3_Bridge` — machinery (v26)
Two survival notions, and why they agree. `P3_Freeze_Noisy` computes with
infinite schedules (`survK`, `Prop`-valued) and `P3_Deterministic` with
finite tuples (`survT`, `Bool`-valued); nothing connected them, so the layer
proved the same theorem twice in incompatible vocabularies.
`survK_congr_prefix` (`survK M k u x` sees only `u 0 … u (k-1)`) and
`survT_iff_survK` are the bridge. **Correction carried here:** v25 proposed a
`SafeMDP`/`DetMDP` bridge for `thm:support`'s min-mass consequence; that was
wrong — `min_mass_bound` already proves it, and a bridge between the robust
and stochastic operators is not a theorem (`rem:operators` says they differ).

### `P3_Viable` — the `𝒲_k` recursion (v27)
Defines the viable-set recursion the paper writes as
`𝒲_k = {B : some admissible a maps every x ∈ B into 𝒲_{k-1}-supported
posteriors}`, which no module had. Both readings are given:
`Wblind` (one continuation for all successors — open loop) and `Wmem` (a
continuation per observation — feedback, the literal `∀y` text).
`Wblind_iff_survK` identifies the blind recursion with `survK`-viability;
`Wblind_le_Wmem` is the unconditional direction.

Two editorial decisions are stated rather than hidden. **Safety is re-checked
at every level**, because `DetMDP` has `safe : X → Bool` but no absorbing-`⊥`
axiom, and without it `𝒲_{k+1} ⊆ 𝒲_k` fails at the base. **The choice
between `Wmem` and `Wblind` is left to the paper** — resolved in v28, not
here.

### `P3_Feedback` — the resolution (v28)
Settles the v27 question with a proof rather than a decision.

* `Wmem_iff_feedback`: `Wmem` is exactly survival under an admissible
  observation-history policy `π : List Y → A` (`survPol`). Axioms:
  `[propext, Classical.choice]` — choice is load-bearing, since `Y` has no
  finiteness hypothesis.
* `Wmem_not_le_Wblind`: a model with **deterministic kernels** and a
  deterministic observation map — i.e. inside `thm:support`'s own hypothesis
  class — on which `Wmem M 2 B ∧ ¬ Wblind M 2 B`. The two readings are
  genuinely different families; `Wmem_le_Wblind` is not a theorem.
* `Wmem_eq_Wblind_of_blind`: on a constant observation map they coincide.
  This is `thm:lattice`'s middle equality at set level, and it is why the
  blind formalization was right for `prop:degen` (a blind window) and not for
  consequence 1.

### `P3_FeedbackValue` — `thm:support` consequence 1 (v29)
The value side. `VR` maximizes over action *tuples*; consequence 1 needs a
maximum over *policies*, and `List Y → A` is infinite. `VFb` instead
maximizes over the jointly policy-survivable subsets — which is
`prop:antichain` (i) read for the feedback class, hence finite, hence the
paper's own route from sets to values. Results:
`VFb_eq_total_iff_Wmem` (consequence 1), `VFb_min_mass_bound` (consequence
2), `VFb_antitone` (consequence 3), plus `Wmem_empty`/`Wmem_downward`/
`Wmem_succ`, the subset split lemma `lsum_subset_add_le`, and the missing
arithmetic (`lt_add_of_pos_right`, `lmax_lt`).

Scope: `VFb` is the **robust** value. Under `thm:support`'s deterministic
kernels the robust and expectation readings coincide, so the theorem is the
paper's; off that class they differ, as `rem:operators` says they should.

### `P3_SurvivableAdm` — the admissible blind family (v30)
The fidelity fix for `prop:antichain`'s `𝒮_k` (see the correction note
above), supplied additively because `P3_Freeze_Noisy` must not be edited.
`SurvivableAdm_iff_Wblind` identifies the corrected family with `𝒲_k`
-viability, so the three blind notions are one; `SfamAdm_subset_Sfam` and
`VfamAdm_le_Vfam` quantify the defect; `VfamAdm_le_VFb` is **the value of
observation at operator level** (a schedule is the policy that ignores its
history), strict in general by v28's counterexample.

### `P3_BlindValue` — the blind composition (v30)
Chains `Wblind_iff_survK` (v27) + `survT_iff_survK` (v26) +
`VR_eq_total_of_jointly_surviving` (v12) into
`VR_eq_total_iff_Wblind`: `VR_k(b) = totalD(b) ⟺ supp(b) ∈ 𝒲_k`, in both
directions, the forward one proved **strictly** (`VR_lt_total_of_not_Wblind`)
rather than by a deficit bound. Plumbing: `mem_tuples` (`t ∈ tuples M k ↔
|t| = k ∧` every entry admissible), `getD_mem_of_lt`,
`exists_tuple_of_sched`, and `smass_eq_bS_survSet` (a tuple's survived mass
is the mass of its surviving set — the value-level bridge between the two
vocabularies).

### `P3_Rational` — `prop:pl` rationality (v31)

Two things, and the first is the larger.

**A model.** `instance ratOrdField : OrdField Rat`. Until now every theorem
in this layer was proved over an abstract `OrdField K` with **no instance
anywhere** — consistent, but with nothing ruling out vacuity. `Rat`
satisfies the interface, so the layer is now known to be inhabited. Three
fields needed work: `zero_ne_one` and `zero_le_one` by `decide`, and
`add_le_add` assembled from `Rat.add_le_add_left` in four `calc` steps
(`OrdField` is not a `Preorder`, so `le_trans` must be applied by hand).

**The closure theorem.** Rationality is *not* proved by instantiating at
`K = ℚ`: there every element is rational and the claim says nothing. The
content of the paper's clause is that the **construction preserves**
rationality, so it is introduced as an interface — `RatSub K` with
`isRat : K → Prop` closed under `0, 1, +, −, ·, ⁻¹` — and what is proved
is closure: `rat_lsum` (finite sums), `rat_lmax` (via `lmax_isMax`, so the
max is *attained*, not merely approached), `rat_ind`, then `alphaSeg_rat`,
`smass_rat`, `VR_rat`, `VFb_rat`, `VfamAdm_rat`. The witness clause is
discharged by `VfamAdm_rat_witness`, using `VfamAdm_finite_range`.
`instance ratSubRat : RatSub Rat` shows the interface is satisfiable.

**Scope, stated plainly.** Rationality is proved for the **segment form**
only. `alphaSeg_rat` holds because `α^seg` is the survival indicator
`ind (survT M t)`, i.e. `0` or `1` — rational with **no hypothesis on the
data at all**. The general masked backup would need rational `T` and `g`
on `SafeMDP`'s stochastic kernels, which is the *other* operator and out
of scope by design since v24 (`rem:operators`).

### `P3_Binomial` — machinery for Sperner (v31, INCOMPLETE)

**This module contains no result.** It exists because `prop:antichain`
(iii)'s bound `|A| ≤ C(n, ⌊n/2⌋)` cannot even be *stated* without binomial
coefficients, and the layer has none: `Nat.choose`, `Nat.factorial`, and
`List.permutations` are all unknown identifiers (probed, v31). So `choose`
is defined by Pascal's recursion and its basic laws are proved:
`choose_succ_succ` (by `rfl`), `choose_zero_right`, `choose_zero_succ`,
`choose_eq_zero_of_lt`, `choose_self`, `choose_pos`, `choose_succ_self`,
plus `choose_six_three` as a `native_decide` check that the recursion
computes what it should.

**What remains, and why it is not done.** Three steps: (1) unimodality,
`C(n,k) ≤ C(n, n/2)`; (2) LYM, by maximal-chain counting; (3) the
cardinality bound. Step 1 was attempted and **failed**, informatively:
the two-step recursion needs the case `2(k+2) = n+1`, which is binomial
*symmetry* — so symmetry must precede unimodality, and symmetry is itself
a separate induction. Step 2 needs factorials, a permutation enumerator,
and `C(n,k)·k!·(n-k)! = n!`, none of which exists here.

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
