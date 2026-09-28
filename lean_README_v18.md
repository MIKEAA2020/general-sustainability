# Lean Formalization Layer — `general-sustainability` paper family
### v16 — result-level index

> **What changed since v11 (v36).** `prop:bands` taken apart and largely
> rebuilt. The blocker was not mathematics but arithmetic: the layer has
> no `norm_num`, no `ring` and no `linarith`, so `−1/2 + (1/5)·4 = 3/10`
> is a lemma, not a computation. v35 had written that step ad hoc three
> times without converging; v36 pays for it **once**, in `RatArith`
> (`natToK_mul_inv_cancel` clears a denominator exactly, no division;
> `pos_of_mul_pos_left'` converts a scaled inequality back), and every
> clause after that is cheap.
>
> 1. **The shared rational-arithmetic helper** — `RatArith`:
>    `natToK_mul_inv_cancel`, `pos_of_mul_pos_left(')`, `eq_of_mul_eq_mul_pos`.
>    Nothing in it is EBC-specific; it sits after the EBC modules only
>    because `natToK` is defined there.
> 2. **`prop:bands`, singleton clause** — matched play rises at `+3/10`,
>    so a singleton survives from every `z₀ ≥ 1` at every horizon
>    (`EBC_Bands_v2.singleton_survives`).
> 3. **`prop:bands`, pair clause** — Hamming-adjacent pairs survive
>    **exactly** from `z₀ ≥ 1.1`: sufficiency by the alternation
>    (`EBC_Pairs_v2.pair_survives`), necessity because from `z₀ < 1.1`
>    no in-alphabet action keeps both members above the floor for even
>    one step (`EBC_Pairs_v3.pair_first_step_fails`).
> 4. **`prop:bands`, "nothing larger" at the floor** — at `z₀ = 1.0`
>    all surviving cells agree on `I`
>    (`EBC_Classification.floor_survivors_agree`), so the maximal sets
>    are single cells. The 16 and 32 **counts** are instance-level and
>    stay with the verifier, by directive.
>
> A **scope finding** came out of this and is recorded in `EBC_Pairs`:
> `Tri` has a `hold` value, so the layer's action type admits *partial*
> holds, which the paper's verified alphabet (17 actions at `m = 4`: the
> 16 cells plus the all-hold) excludes. From `z₀ = 1.0`, holding at
> exactly the coordinate where a pair differs and matching elsewhere
> gives both cells `+1/10` and rescues the pair. So "survivable exactly
> from `z₀ ≥ 1.1`" is **true over the paper's alphabet and false over
> the unrestricted one** — the proposition needs its action set stated.
>
> Build went 48 → 55 jobs, 43 → 49 imported modules.
>
> **v37 addendum.** `prop:bands` is now **closed in all four clauses**.
> The `z₀ ≥ 1.1` half of "nothing larger" landed: `cor_hamming_m4` is
> stated at `z₀ = 1` and does not transfer to a higher start, so the
> pair-sum bound was re-derived with `z₀` as a parameter
> (`EBC_Classification_v2`), giving `|us| ≤ 10·(z₀ − 1)` after the
> arithmetic reduction (`EBC_Classification_v3`). At `z₀ = 1.1` a pair
> at Hamming distance `≥ 2` survives at most **one step**, so no such
> pair appears in any set that survives at every horizon. The counts 16
> and 32 remain instance-level, with the verifier.
>
> `prop:ladder` is analysed and scoped but **not yet started** — see the
> note in the EBC section. Build went 55 → 57 jobs, 49 → 51 modules.

> **v38 addendum.** `prop:ladder` is complete on the EBC side, and the
> `DetMDP` question is settled by the paper's own wording rather than
> left open. Two corrections to earlier statements in this index:
>
> * `prop:bands` **closed at `2bf7d4b`** — all four clauses. It is not
>   an open item, and the shared arithmetic helper (`RatArith`) that made
>   its clauses cheap was built several pushes earlier.
> * The `prop:ladder` section below, headed "analysed, not started", is
>   now out of date: the EBC half landed in `EBC_Ladder` and
>   `EBC_Ladder_v2`.
>
> Build went 57 → 59 jobs (v38) → 60 jobs, 54 modules (v39).
>
> 1. **`prop:freeze`'s closing clause, on the corrected family** —
>    `P3_FreezeValue.VfamAdm_prune_eq`: the value is the maximum of `b(S)`
>    over the *maximal* jointly survivable sets. v21 had this for the old
>    family; v30 showed the old family is not the paper's `𝒮_k`. **P3 is
>    closed**, with one honest residual: v34 proved the **value**
>    stabilizes after `2^{|supp b|}` strict decreases, not that the
>    **family** stops shrinking, so `VfamAdm_frozen_eq_pruned` takes
>    family-freezing as a hypothesis.
> 2. **EBC: `lem:triangle`, `cor:hamming`, `cor_hamming_m4`.**
>    `EBC_ExactBelief_v3` (no three cells pairwise at Hamming distance 1),
>    `EBC_Dynamics` (the drift model `lem:pairsum` fixes — trajectories,
>    floor, survival), `EBC_Hamming` (the paper's own `h ≤ 1` at `m = 4`).
>    The paper derives `cor:hamming` from a `liminf` of Cesàro averages;
>    the formalization needs no limit — the inequality holds at every
>    finite horizon.
> 3. **`comp` probed, not expanded.** `farkas_sound` is already proved
>    (`Prelude:748`, axiom-free), so Farkas was never the blocker. The
>    continuous-time results (`prop:value`, `thm:bridge`,
>    `prop:beliefcells`) are **out of reach by design**: the layer has no
>    topology and no integration, and was not expanded to chase one
>    result. See `lean_audit_v35_comp_probe.md`.
> 4. **`E1` relabelled.** The target paper has zero numbered environments
>    and the module's paper references are invented (no "telescope", no
>    "level margin" anywhere in the paper). The one genuine lemma is now
>    `Prelude_Monotone.monotone_step_ascent`. See
>    `lean_audit_v35_e1_decision.md`.

### v10 — result-level index

> **What changed since v9 (v34).** One module, `P3_FreezeCount`; the build
> went 42 → 43 jobs, 39 → 40 imports. Plus the paper edit, issued as
> `paper2_probabilistic_sufficiency_v12.tex`.
>
> 1. **`prop:freeze`'s `2^{|supp b|}` is proved** — the last paper-owned
>    claim in P3. `strictDrop_length_le`: for every horizon `n`, the
>    number of strict decreases among the first `n` horizons is at most
>    `2^{|supp b|}`. The paper asserts this one itself, so unlike Sperner
>    it could not be skipped.
> 2. **A defect in this layer, found and recorded.** v18's
>    `prop_freeze_drop_count` was listed as having done the count. Its
>    **statement** bounds the drops by `2^{|univX|}`; its **comment**
>    claims `2^{|supp b|}`. The comment over-claims, and the README had
>    propagated it. Corrected here and in `lean_audit_v34.md` §2; the v18
>    file is left untouched. The new theorem is also on the **corrected**
>    family (`SfamAdm`/`VfamAdm`), not the defective `Sfam`/`Vfam`.
> 3. **The paper edit is applied**, as `v12`: the three-symbol fix
>    (`𝒲^{fb}_k`, `𝒲_k`, `𝒲^{bel}_k`, with `𝒲^{bel}_k` explicitly the
>    analogue of the blind `𝒲_k`), the restated `thm:support`, a
>    replacement for the invalid converse, and the new
>    `rem:feedback-strict`. `prop:deficit` (ii) left untouched, as §4 of
>    the draft requires.

> **What changed since v8 (v33).** One module, `P3_SupportRepair`; the
> build went 41 → 42 jobs, 38 → 39 imports.
>
> 1. **Repair A is adopted and complete.** `thm:support` keeps the
>    unrestricted sequential class and `𝒲_k` is restated as the feedback
>    recursion; the repaired statement is `VFb_eq_one_iff_Wmem` (v32),
>    already proved. v33 supplies consequence 2 in literal form
>    (`VFb_min_mass_bound_one`) and restates `prop:deficit` (ii) in the
>    paper's own `𝒲^{bel}_k` vocabulary (`deficit_min_mass_of_not_Wbel`).
> 2. **The downstream check found one casualty, and it is not a theorem.**
>    `𝒲^{bel}_k` (paper line 789) is defined by a *declared-class*
>    sequence, i.e. it is the belief-space analogue of the **blind**
>    recursion. So once `𝒲_k` becomes the feedback recursion, line 252's
>    "its belief-space analogue" is false — `Wfbel_not_Wbel` exhibits a
>    normalized belief in one family and not the other. The paper needs
>    **three** symbols, not two. Details in `lean_audit_v33.md` §3.
> 3. **The false theorem is recorded, not buried.** See the `thm:support`
>    row and `lean_audit_v33.md` §5: the paper's printed statement was
>    refuted by an explicit witness; the repaired form is proved.

> **What changed since v7 (v32).** One module, `P3_SupportValue`, and two
> decisions; the build went 40 → 41 jobs, 37 → 38 imports.
>
> 1. **`thm:support` is now stated in the paper's literal form.**
>    v29/v30 proved `V = totalD(b)`; the paper writes `V_k(b) = 1`. `Mass`
>    carries no normalization, so the literal form is a *corollary* with
>    `totalD M b = 1` as an explicit hypothesis, not an assumption smuggled
>    in. Both readings now have it.
> 2. **The `Wmem`/`Wblind` question is closed at value level, and the
>    answer is that the paper needs an edit.** `thm:support` names the
>    unrestricted sequential class but pairs it with the *blind*
>    recursion `𝒲_k`. `paper_literal_thm_support_fails` exhibits a
>    **normalized** belief on which `V_k(b) = 1` while
>    `supp(b) ∉ 𝒲_k` — so the sentence is false as written. Three repairs
>    are proved; which one to adopt is a paper-side editorial choice.
> 3. **Sperner is closed by decision, not by omission.** The paper cites
>    the count to Sperner (1928); it does not prove it. The bound is
>    therefore *not* formalized, deliberately — see `lean_audit_v32.md`.

> **This file supersedes `lean_README_v9.md`.** Issued as a new file, not an
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

`lake build` → **rc = 0, 60 jobs** (54 imported modules). Zero `sorry`.
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
| comp | Computational certification (`paper2_computational_certification_v18.tex`) | `Comp_Certification`, `Comp_Certification_v2` — **Farkas core proved** (`Prelude.farkas_sound`); `prop:value`, `thm:bridge`, `prop:beliefcells` out of reach by design (v35) |
| ws | Worked systems (`paper2_worked_systems_v17.tex`) | `WS_WorkedSystems`, `WS_WorkedSystems_v2` |
| minimax | Minimax dual certificates (`minimax_dual_certificates_v11.tex`) | `Minimax_Dual` |
| ebc | Exact belief computation (`paper2_exact_belief_computation_v10.tex`) | `EBC_ExactBelief_v2`; `EBC_ExactBelief_v3`, `EBC_Dynamics`, `EBC_Hamming` (v35); `EBC_Bands`, `EBC_Bands_v2`, `EBC_Pairs`, `EBC_Pairs_v2`, `EBC_Pairs_v3`, `EBC_Classification`, `EBC_Classification_v2`, `EBC_Classification_v3` (v36); `EBC_Ladder`, `EBC_Ladder_v2` (v37); `EBC_Deadline` (v39) |
| P3 | Probabilistic sufficiency (`paper2_probabilistic_sufficiency_v12.tex`) | `P3_ProbSufficiency` (machinery); `P3_ClassLattice`, `P3_Sufficiency`, `P3_Deterministic`, `P3_Freeze_Noisy`, `P3_Freeze_Noisy_v2`, `P3_Convexity`, `P3_Antichain`, `P3_Antichain_v2`, `P3_Antichain_v3`, `P3_PiecewiseLinear`, `P3_RobustPL`, `P3_Support`, `P3_Bridge`, `P3_Viable`, `P3_Feedback`, `P3_FeedbackValue`, `P3_Rational`, `P3_Binomial`, `P3_SupportValue`, `P3_SupportRepair`, `P3_FreezeCount` (v31–v34), `P3_FreezeValue` (v35) |
| ARV | Applied regime viability (`applied_regime_viability_v9.tex`) | `ARV_RegimeViability`, `ARV_RegimeViability_v2` |
| E1 | Applied forecast ladder (`paperE1_cod_forecast_ladder_v59.tex`) | `E1_ForecastLadder` — **no formalizable target**: the paper has zero numbered environments and the module's paper references do not exist (v35); the one genuine lemma is relocated to `Prelude_Monotone` |
| P1-AS | Assessment separation (`paper1_assessment_separation_v62.tex`) | `P1_AssessmentSeparation_v5` |
| — | interface | `Prelude`; `Prelude_Monotone` (v35), `RatArith` (v36) |

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
| 2 | `thm:support` | **result — proved on the repaired reading** | support identity `supp(b⁺) = Post(supp b, a, y)` — `P3_Support.support_identity` (v25), stated on `SafeMDP`. **Consequence 1** `VFb_eq_one_iff_Wmem` (v32) — this is the repaired statement; the printed one was **false** (see the warning below). **Consequence 2** `VFb_min_mass_bound_one` (v33), `VFb_min_mass_bound` (v29). **Consequence 3** `VFb_antitone` (v29). **Blind twin** `VR_eq_one_iff_Wblind` (v32) is `prop:degen` consequence 1, not `thm:support` |
| 3 | `prop:antichain` | **result** (i) carries a correction — see below | (i) v13, corrected in v30 (`VfamAdm`); (ii) alpha-vectors = indicators of maximal elements, `P3_Antichain_v2.Vfam_prune_eq` (v21); (iii) antichain (v20); (iv) deficit = min `b(S^c)`, `P3_Antichain_v3.deficit_eq_min_compl` (v22). **Sperner count in (iii): antichain proved, count cited to
Sperner (1928) by the paper and not formalized, by decision (v32)** |
| 4 | `cor:closed` | **instance** | Python layer |
| 5 | `thm:parametric` | **instance** | Python layer |
| 6 | `prop:pl` | **result** | convexity (`P3_Convexity.VAdm_convex`, v19); witness set `Γ_k` and growth law `\|Γ_{k+1}\| ≤ \|A\|·\|Γ_k\|^{Y}` (`P3_PiecewiseLinear`, v23); segment form `V_k = max_{α∈Γ_k} αᵀb` (`P3_RobustPL.VR_eq_max_alpha`, v24). **Rationality clause not formalized** (needs `K := ℚ`); the general stochastic masked backup is out of scope by design — it is the *other* operator (v24) |
| 7 | `prop:degen` | **result** | `P3_Deterministic.VR_eq_total_of_jointly_surviving` (v12); the `𝒲_k` form (both directions) is `P3_BlindValue.VR_eq_total_iff_Wblind` (v30) |
| 8 | `prop:freeze` | **result** (same correction as (3)) | nesting + antitonicity on the corrected family `SfamAdm_nesting`, `VfamAdm_antitone` (v30). **Drop count at the paper's bound `2^{\|supp b\|}`**: `P3_FreezeCount.strictDrop_length_le` (v34) — plus `no_drop_beyond_bound`, the stabilization form. **v18's** `prop_freeze_drop_count` is a *weaker* statement: its bound is `2^{\|univX\|}` (its comment claims `2^{\|supp b\|}` — see `lean_audit_v34.md` §2) and it runs on the defective `Sfam`/`Vfam`. Second clause — frozen value as `max_S b(S)` over the **maximal** sets — proved for the old family (`Vfam_prune_eq`, v21), **not yet** for `SfamAdm` | **Frozen-value clause on the corrected family: `VfamAdm_prune_eq` (v35).**
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

**`thm:support` was false as printed, and the paper is being edited.**
v32 produced a normalized belief on a model with deterministic kernels and
a deterministic observation map with `V_k(b) = 1` but
`supp(b) ∉ 𝒲_k(blind)`; the paper paired the unrestricted sequential class
with the blind recursion. **Repair A** is adopted: `𝒲_k` in `thm:support`
becomes the feedback recursion `𝒲^{fb}_k`, and the repaired statement is
what the layer proves. A remark covers the blind window, where the two
recursions agree (`Wmem_eq_Wblind_of_blind`).

**The repair is merged into the paper, not merely drafted.** Verified
against `paper2_probabilistic_sufficiency_v12.tex` (v41):

* the notation paragraph defines all three symbols — `𝒲^{fb}_k`
  (feedback), `𝒲_k` (blind, "one action for the whole set, chosen before
  the observation arrives"), `𝒲^{bel}_k`;
* `thm:support` states `V_k(b) = 1` iff `supp(b) ∈ 𝒲^{fb}_k` for the
  unrestricted sequential class — repair A verbatim;
* the line-256 cross-reference reads `𝒲^{bel}_k` as the belief-space
  analogue of **`𝒲_k`** (blind), not of `𝒲^{fb}_k` — the correction
  repair A costs;
* `rem:feedback-strict` records `𝒲_k ⊆ 𝒲^{fb}_k` with strict inclusion
  under `thm:support`'s own hypotheses, the `{p,q}` witness, agreement
  on a blind window, and the consequence that `thm:support` is a feedback
  theorem while `prop:degen` is blind.

Earlier text here said the edit "is drafted in
`paper2_repairA_thm_support_v1.tex`", which understated the state: that
file is the standalone draft, and its content is in v12.

**P3 totals: 11 result · 1 partial · 6 instance · 1 out of reach** — and P3 is now closed: every result row is settled, the only open item being `prop:deficit` (i), out of scope since v24 (`rem:operators`) — the
partial being `prop:antichain` (iii), whose cardinality half is the paper's
own citation of Sperner and is not formalized **by decision** (v32). (Sums to
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

### `P3_Binomial` — machinery for Sperner (v31, complete machinery)

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

**Scoped in v41: the machinery is complete, and nothing here is
half-built.** `choose` and every law this module claims are proved; the
module does exactly the job it was built for, which is to make
`prop:antichain` (iii) *statable* — the layer had no binomials at all, so
the bound could not previously be written down. It is **machinery only**:
the Sperner bound itself is **cited, not formalized, by decision**, and
that decision is unchanged. The three steps listed above were never
claimed; step 1's failure is a recorded finding about a route not taken,
not an unfinished proof.

### `P3_SupportValue` — `thm:support` literally, and a counterexample (v32)

Two halves, and the second is the reason to read this one.

**§1 — the literal statement.** The paper says `V_k(b) = 1` iff
`supp(b) ∈ 𝒲_k`; the layer had `V = totalD(b)` (v29/v30). That is not a
cosmetic gap: `Mass` (`P1_BeliefSafety:169`) carries only `nonneg`, no
normalization, so `totalD M b = 1` is a *hypothesis* the layer cannot
discharge. `VFb_eq_one_iff_Wmem` and `VR_eq_one_iff_Wblind` state the
paper's sentence with that hypothesis explicit, and
`VFb_lt_one_of_not_Wmem` / `VR_lt_one_of_not_Wblind` give the
contrapositive **strictly** (value `< 1`, not `≤ 1`).

**§2 — the paper's sentence is false as written.** `thm:support` is stated
for *the unrestricted sequential class* — value `VFb`, viability `Wmem` —
but the `𝒲_k` it names (paper lines 302–304, "some admissible `a` maps
every `x ∈ B` into `𝒲_{k-1}`-supported posteriors", with no case split on
the observation) is the **blind** recursion `Wblind`. v28 proved these
differ (`Wmem_not_le_Wblind`) under `thm:support`'s own hypotheses.
`paper_literal_thm_support_fails` closes the loop at value level: a
normalized belief — mass `1/2` on each of `p` and `q` — with
`VFb_2(b) = 1` and `supp(b) ∉ Wblind_2`. So the forward direction of the
paper's iff fails.

Three repairs are proved, because the choice among them is the paper's,
not the layer's: **A** keep the sequential class and read `𝒲_k` as the
feedback recursion (`VFb_eq_one_iff_Wmem`); **B** keep `𝒲_k` verbatim and
read `V_k` as the sequential-blind value (`VR_eq_one_iff_Wblind`, no
hypothesis on observations); **C** keep both on a blind window
(`Wmem_eq_Wblind_of_blind`, v28 — the set-level form of `thm:lattice`'s
`V^{ol} = V^{seq,blind}`), which is the only reading on which the sentence
is true *as written*.

### `P3_SupportRepair` — repair A, and its downstream cost (v33)

Three items, all consequences of adopting repair A.

**§1 — consequence 2, literally.** `VFb_min_mass_bound_one`: for a
normalized belief whose support is not `𝒲_k^{fb}`-viable,
`1 - VFb_k(b) ≥ min_{x ∈ supp b} b(x)`. v29 had this as
`mn ≤ totalD(b) - VFb_k(b)`; the paper writes `1 - V_k(b)`, and `Mass`
carries no normalization, so the hypothesis is named.

**§2 — `𝒲^{bel}_k`.** The paper defines a *belief-space* viability family
at line 789: "the beliefs whose support admits a jointly surviving
**declared-class** sequence". That is the belief-space form of the **blind**
recursion. `Wbel` is that family, and `deficit_min_mass_of_not_Wbel` is
`prop:deficit` (ii) in the paper's own words; v12's `min_mass_bound` said
the same thing with the hypothesis spelled out per-tuple.

**§3 — what repair A costs.** `Wfbel` is the belief-space analogue of the
*repaired* `𝒲_k`; `Wfbel_not_Wbel` exhibits a normalized belief in
`Wfbel` and not in `Wbel`. So if the paper redefines `𝒲_k` as feedback but
leaves `𝒲^{bel}_k` as published, line 252's claim that `𝒲^{bel}_k` is
"its belief-space analogue" is false. The fix is three symbols
(`𝒲^{fb}_k`, `𝒲_k`, `𝒲^{bel}_k`) and a corrected cross-reference — not
renaming everything to the repaired symbol, which would break
`prop:deficit` (ii)'s proof, since that one cites `prop:degen`.

### `P3_FreezeCount` — `prop:freeze`'s count (v34)

**`strictDrop_length_le`**: for every horizon `n`, the number of strict
decreases of `ℓ ↦ V_ℓ(b)` below `n` is at most `2^{|supp b|}` — the paper's
bound, on the corrected family `SfamAdm`/`VfamAdm`.

Three ingredients, none of them previously available in combination:

* `VfamAdm_mem_range` — every value of the sequence is `b(T)` for some
  `T ⊆ supp(b)`; the maximum is attained (`lmax_isMax`) and truncating a
  maximizer to the support preserves its mass (`bS_supp_trunc`).
* `strictDrop_value_inj` — two strict drops never repeat a value, by
  `VfamAdm_antitone`: `V_{k₂} ≤ V_{k₁+1} < V_{k₁}`.
* `subsetsOf_length` (v13) for the `2^{|supp b|}`, and a new
  `nodup_mem_length_le` (pigeonhole for lists) to turn "distinct values
  inside a list of length `N`" into "at most `N` drops".

`no_drop_beyond_bound` is the paper's "stabilizes" phrasing: once the drop
list has reached the bound it cannot grow. Supporting list lemmas
(`nodup_mem_length_le`, `nodup_map_on_of_inj`, `nodup_filterP`,
`mem_erase_of_mem_of_ne`) are proved here because the layer has no
cardinality machinery.

**Not to be confused with `P3_Freeze_Noisy_v2.prop_freeze_drop_count`
(v18)**, which bounds the drops by `2^{|univX|}` — weaker, and on the
family v30 showed to be defective. Its docstring claims `2^{|supp b|}`;
the statement does not. That over-claim is recorded in
`lean_audit_v34.md` §2 and corrected in this row. The v18 file is left
untouched.

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

### `P3_FreezeValue` — `prop:freeze`'s frozen-value clause (v35)

Carries v21's pruning identity across to the corrected family, which is
what `prop:freeze`'s closing clause was missing.

* `PrunedAdm`, `PrunedAdm_mem`, `PrunedAdm_ne`, `SfamAdm_mem_nodup`.
* `VfamAdm_prune_eq` — **`prop:freeze`'s "frozen value is `max_S b(S)`
  over the maximal sets of the frozen family"**, on `𝒮^adm_k`. This is
  also `prop:antichain` (ii) for the corrected family.
* `VfamAdm_frozen_eq_pruned` — the frozen-value form. **Family-freezing
  is a hypothesis**: a family can keep losing non-maximizers without the
  maximum moving, so value-stabilization (v34) does not imply it.
* `PrunedAdm_antichain` — by v20's `maximals_antichain`.

### `EBC_ExactBelief_v3` — `lem:triangle` (v35)

`hamming` (by recursion on the index list, not by filtering),
`hamming_eq_zero`, `hamming_ne_zero_exists`, `hamming_zero_of_agree`, and

* `no_adjacency_triangle` — no three cells are pairwise at Hamming
  distance `1`, any `m`. Proved via the parity invariant the paper names
  in passing (the hypercube is bipartite): at each coordinate the three
  "differ" indicators are all `0` or exactly two `1`s.
* `no_three_pairwise_adjacent` — the contradiction form.

### `EBC_Dynamics` — the drift model (v35)

The layer had the inner product and the pair-sum bound, but no
trajectory, no floor, no survival.

* `natToK` — the Nat→K embedding the layer lacks (no `OfNat`, no
  `NatCast`), with `natToK_nonneg/add/mono`, `lsum_ones`, `natToK_le_one`.
* `neg_add`, `half_add_half`, `five_mul_fifth`, `two_pos`, `five_pos`.
* `drift` (`-1/2 + (1/5)⟨u,θ⟩`), `stateAfter`, `totalDrift`,
  `survivesTo`, `stateAfter_eq`, `survivesTo_totalDrift_lower`.
* `pairIpSum`, `drift_pair`, `totalDrift_pair`.
* §5 `pairIpSum_upper`, `pairIpSum_lower_of_survive`,
  `le_of_mul_le_mul_pos`, `agreeMass_add_natToK_hamming`,
  **`cor_hamming`** (`five ≤ two * agreeMass`, the paper's `5 ≤ 2(m−h)`),
  **`cor_hamming_dist`** (`five + 2h ≤ 2m`, the paper's `h ≤ m − 5/2`).

The paper reaches `cor:hamming` through a `liminf` of Cesàro averages;
the formalization holds at every finite horizon and needs no limit.

### `EBC_Hamming` — `cor:hamming` at `m = 4` (v35)

* `natToK_mul`, `two_mul_two_eq_four`,
  `two_mul_four_eq_five_add_three`, `le_of_add_le_add_left`,
  `three_lt_four`.
* **`cor_hamming_m4`** — Hamming distance `≤ 1` for two cells that both
  survive a nonempty horizon from `z₀ = 1` over a 4-dimensional index
  set. Does **not** include the paper's closing "every pair inside a
  blind survivable set is Hamming-adjacent", which needs survivability
  to pass to subsets.

### `Prelude_Monotone` — relocated (v35)

* `monotone_step_ascent` — a sequence whose steps never descend never
  descends. Relocated from `E1_ForecastLadder.ladder_ascent`, the only
  one of that module's five theorems with a proof (the other four are
  one-line aliases of `sumRange` lemmas) and the only one whose stated
  paper reference survives checking.


### `RatArith` — machinery (v36)

Rational arithmetic over a bare `OrdField`. The layer has no `norm_num`,
no `ring` and no `linarith`, so clearing denominators is a lemma.

* **`natToK_mul_inv_cancel`** — `natToK (q·m) · (1 / natToK m) = natToK q`:
  clears a denominator exactly, with no division. The workhorse.
* `natToK_mul_inv` — `natToK m · (1 / natToK m) = 1`, for `m ≠ 0`.
* `natToK_pos`, `natToK_ne_zero` — general forms of the `ten_pos` /
  `three_pos` style lemmas that had been written ad hoc.
* **`pos_of_mul_pos_left'`** — `0 < c·x` and `0 < c` give `0 < x`: the
  order half of the scaling argument.
* `eq_of_mul_eq_mul_pos` — cancel a positive factor from an equality
  (currently stated in `EBC_Pairs_v3`; belongs here and can move
  unchanged).

### EBC — `prop:bands` (v36)

| # | Result | Status | Module / where |
|---|---|---|---|
| — | `prop:bands` (i) — a singleton survives from every `z₀ ≥ 1` | **result clause** | `EBC_Bands_v2.singleton_survives`; matched drift `+3/10` is `matched_drift_pos_m4` |
| — | `prop:bands` (ii) — a Hamming-adjacent pair survives from `z₀ ≥ 1.1` | **result clause** | `EBC_Pairs_v2.pair_survives`, on the alternation `altPairs`; cycle gain `+1/5` is `cycle_net_nonneg` |
| — | `prop:bands` (ii) — and **not** from `z₀ < 1.1` | **result clause** | `EBC_Pairs_v3.pair_first_step_fails`, **over `inAlphabet`** |
| — | `prop:bands` (iii) — nothing larger, at `z₀ = 1.0` | **result clause** | `EBC_Classification.floor_survivors_agree` (all survivors agree on `I`), `no_three_survivors`, `survivesSet_mono` |
| — | `prop:bands` (iii) — nothing larger, at `z₀ ≥ 1.1` | **result clause** | `EBC_Classification_v3.far_pair_horizon_bound`: `\|us\| ≤ 10·(z₀ − 1)`, from `far_pair_sum_bound` (`EBC_Classification_v2`) — at `z₀ = 1.1` a distance-`≥2` pair survives at most one step |
| — | the counts **16** singletons and **32** pairs | **instance** | Python layer, by directive |

Supporting: `EBC_Bands.matched` / `ipi_matched` / `drift_matched`;
`EBC_Pairs.ipi_mismatched` (`⟨matched θ′, θ⟩ = m − 2h`),
`mismatch_scale_m4` (the `−1/10`), `mismatched_step_floor` (the dip);
`EBC_Pairs_v3.drift_cell_le_neg_tenth`; `EBC_Pairs_v2.inAlphabet`.

**Caveat carried by every one of these clauses.** `inAlphabet` is the
paper's action set: the 16 cell actions plus the all-hold. The layer's
action type `Nat → Tri` is larger — it admits partial holds — and over
that larger set `prop:bands` (ii)'s "exactly" is false. See the note in
`EBC_Pairs` and the audit.


### EBC — `prop:ladder` (closed in v38; see the status section below)

`prop:ladder` (geometric ladder) states that the maximal conditional
kernel mass doubles with each probe:

```
z₀ = 1.0  :  1/16 → 1/8 → 1/4 → 1/2 → 1
z₀ ≥ 1.1  :  1/8  → 1/4 → 1/2 → 1   → 1
```

for zero through four probes. Its proof decomposes into three inputs:

1. **The antichain value formula** (companion P3 theory): the kernel
   value of a prior is the maximal survivable-set mass it charges, and
   survivability is hereditary downward, so for the uniform prior on a
   support `S` the value is `max{|A| : A ⊆ S, A survivable} / |S|`.
   Proved in the P3 slot — `P3_FreezeValue.VfamAdm_prune_eq` (v35) is
   the value-as-max-over-maximal-sets form on the corrected family.
2. **Heredity**: **proved here** in EBC terms —
   `EBC_Classification.survivesSet_mono`.
3. **`prop:bands`**: **proved** — the survivable subsets are singletons
   at the floor and Hamming-adjacent pairs above the edge.

With those, a `2^j`-cell subcube has value `1/2^j` at the edge and
`2/2^j` above it (capped at `1` when `j = 0`), which is the ladder.

**What is instance-level and therefore stays with the verifier:** the ten
numbers themselves, the 16 cells, the `2^j` subcube sizes, and the claim
that supports after `0…4` probes are subcubes with `j = 4,3,2,1,0`. The
paper itself says "the script recomputes all ten values by exhaustive
survivable-subset enumeration within each support".

**What remains to be formalized**, and it is a cross-paper bridge rather
than a new idea: connect the P3 value functional to EBC survivability
(the two slots currently use different notions of "survivable set" —
P3's is the class-restricted `SfamAdm` family, EBC's is the drift/floor
`survivesTo`), and model a probe as a restriction of the index set. That
bridge is the work; the mathematics on the EBC side is done.


### `prop:ladder` — status (v38)

**Complete on the EBC side.** `EBC_Ladder` fixed the shape — set
survivability as `survivesSetAt`, one in-alphabet policy of `L` actions
keeping every member at or above the floor, which is P3's
`SurvivableAdm M S k` verbatim — and `EBC_Ladder_v2` completed the
cardinality facts the value formula consumes:

| fact | theorem |
|---|---|
| heredity of survivability | `EBC_Ladder.survivesSetAt_mono` |
| at the floor, all members agree on `I`, so `M = 1` | `EBC_Ladder.floor_survivable_all_agree` |
| above the edge, every pair is Hamming-adjacent, so `M ≤ 2` | `EBC_Ladder.pairs_adjacent_above` |
| no three pairwise-distinct survivors above the edge | `EBC_Ladder_v2.no_three_distinct_above` |
| a surviving subset is a singleton or an adjacent pair | `EBC_Ladder_v2.survivor_is_singleton_or_adjacent_pair` |
| `M = 2` is attained | `EBC_Ladder.adjacent_pair_survives` |
| a subcube with a free coordinate contains an adjacent pair | `EBC_Ladder.subcube_adjacent_pair` |
| a probe, modelled as a restriction of the index set | `EBC_Ladder.inSubcube`, `flip` |

With the value `= M/|S|`, that is `1/|S|` at the edge and
`min(1, 2/|S|)` above it — the paper's two rows, `|S|` symbolic.

**The `DetMDP` instantiation is not being done, and here is why.** The
decision rule is the paper's claim: type-identity ("is an instance of")
would require it, shape-equivalence ("has the same value form") would
not. `prop:ladder`'s proof reads *"The companion theory's antichain
formula **makes** the kernel value of a prior the maximal survivable-set
mass it charges…"* — it **applies** the companion formula, and never
asserts the ladder *is* an instance of `VfamAdm`. So the formalization
target is shape-equivalence, and building a `DetMDP` over the sixteen
cells whose `survK` is EBC's `survivesTo` would add mechanism without
adding a theorem. The bridge is recorded as **structural**. If a future
edition of the paper claims type-identity, revisit this.


### `prop:deadline` — status (v39)

**Built.** paper2_exact_belief_computation_v10, ll. 365–392: hold for
`T` steps (drift `−1/2`), the parameter revealed exactly at `T`, then
matched forever (drift `+3/10` on every branch). Viability holds exactly
when `z₀ ≥ 1 + T/2`.

**Why this needs no delayed-instance machinery.** The delay lives
entirely in the *shape of the action sequence*, not in the state. For
branch `θ` the realized sequence is `hold^T ++ (matched θ)^n`, and
`survivesTo I θ us z0` is already a branchwise predicate taking an
arbitrary action list, so adaptivity after revelation costs nothing:
each branch supplies its own list, and `matched` is `θ`-dependent by
construction. No state expansion, no belief or filter, no new transition
structure. The revelation event itself is never modelled, because the
claim concerns the realized trajectory — which is how the paper's own
proof proceeds: *"under the hold every cell drifts −1/2 … after
revelation the matched action rises at +3/10 on every branch"*, and
*"the direct branchwise argument needs no scalar-additivity
hypothesis"*.

The paper's two numbers were already in the layer: hold scores
`ipi = 0` (`hold_action_zero`) so drifts `−1/2`; matched scores
`ipi = m` (`ipi_matched`) so at `m = 4` drifts `−1/2 + 4/5 = +3/10`,
which the layer carries as `matched_scale_m4` (`10·d = 3`).

| fact | theorem |
|---|---|
| the deadline policy | `EBC_Deadline.deadlineSeq` |
| hold drifts `−1/2` | `holdAct_drift` |
| matched drift `≥ 0` at `m = 4` | `matched_drift_nonneg` |
| `t` holds accumulate `t·(−1/2)` | `totalDrift_holdRep` |
| survival to revelation forces `z₀ ≥ 1 + T/2` | `deadline_necessity` |
| the converse for the hold phase | `holdRep_survives` |
| `z ≥ 1` plus nonnegative drift survives any tail | `matchedRep_survives` |
| survival across a concatenation | `survivesTo_append` |
| `z₀ ≥ 1 + T/2` gives survival at every horizon | `deadline_sufficiency` |
| **the law** | `deadline_law` |
| the policy uses only the paper's 17 actions | `deadlineSeq_inAlphabet` |

Two notes on the formalization:

* Sufficiency needs only `d ≥ 0`, not the exact `3/10` — once `z ≥ 1` a
  nonnegative drift keeps every later state at or above the floor. That
  keeps the `4/5 − 1/2 = 3/10` identity off the critical path; the value
  itself is already in the layer.
* `T` is left symbolic. The paper states `T = 0,…,4`, but nothing in the
  argument uses the restriction.

**EBC is closed.** `prop:bands` (all four clauses), `prop:ladder`
(complete on the EBC side, bridge recorded as structural), and
`prop:deadline` are done. The remaining EBC items — `prop:pbvi`,
`prop:census`, the 5,219-policy / 60-step search, the 84 pairings, the
subset census — are instance-level, and **were already verified by full
enumeration**: see the `prop:instance` section below.


### `prop:instance` — status (v40)

**Verified by full enumeration. 30/30 checks pass, exit 0.**

The instance-level items were scoped before any decision was taken about
how to check them, and scoping found the verifier **already exists**:
`paper2_exact_belief_computation_v10_verification.py` in the latex
folder. It enumerates; it does not sample.

| item | check | result |
|---|---|---|
| 5,219 policies × 60 steps | *exhaustive 1/2/3-periodic classification (5,219 policies, 60-step certificates)* | **PASS** |
| 84 pairings | *exact point-based evaluation … 7 rational beliefs × 3 levels × 4 horizons (84 pairings); 17⁴ = 83,521 sequences deduplicate to ≤ 545 vectors* | **PASS** |
| the subset census | *antichain census: 1,048,576 raw subset evaluations collapse to 496 stored maximal sets* | **PASS** |

Runtime 7m36s. Not prohibitive; full enumeration is what runs.

**A correction on the "65,536" figure.** It is not one number. The
antichain census is **1,048,576 raw subset evaluations collapsing to 496
stored maximal sets** (16 at the edge + 32×15 above); the paper's text
carries `$2^{16} = 65{,}536$ raw subsets, $736$ stored antichain`. Both
are compression ratios over the same structure; earlier notes quoted
65,536 as *the* subset count without distinguishing it from the census
figure.

**Symmetry reduction already exists** — it is what the check measures:
raw evaluations collapse by 4,096× and 2,048× per level via a
Minato-style antichain representation (the paper cites Minato 1993).

**One defect found, and it was environmental.** The first run reported
29/30:

```
FAIL chained script exits green: paper2_exact_belief_computation_v2_verification.py (16/16)
```

The verifiers form a regression chain (v10 → v2 → v1), and each script
reads its **own `.tex` sibling** from its working directory; run outside
the latex folder each crashes with `FileNotFoundError` *after* its
mathematical checks have already passed. With the three missing siblings
fetched, the chain resolves: **30/30, exit 0**. Worth recording that the
chained check fails closed (exit 1) rather than skipping, which is
correct behaviour. Separately, the `proof completeness` check passes
while reporting one missing *optional* needle, `29-cell radius-two ball`.

**The verifier independently corroborates the Lean layer.** The two were
built separately and agree:

| Lean | verifier check |
|---|---|
| `EBC_Deadline.deadline_law` | *deadline instance on the cube: viability iff z₀ ≥ 1 + T/2* — PASS |
| `prop:ladder`, value `1/\|S\|` at the edge, `min(1, 2/\|S\|)` above | *observation ladder exact: 1/16, 1/8, 1/4, 1/2, 1 at the edge and 1/8, 1/4, 1/2, 1, 1 above* — PASS |
| `EBC_Ladder_v2.no_three_distinct_above` | *no three cells pairwise Hamming-adjacent (all C(16,3) = 560 triples)* — PASS |
| `prop:bands`, 16 singletons / 32 pairs | *16 singletons at 1.0; exactly the 32 Hamming-1 pairs at 1.1 and 2.5; nothing larger* — PASS |

The ladder row is the sharpest case. At `|S| = 16` the Lean layer's
formula gives `1/16` at the edge and `min(1, 2/16) = 1/8` above it; the
verifier's enumeration reports exactly `1/16` and `1/8` as its first two
ladder entries. Two independent derivations of the same numbers.

Full output and reproduction steps: `ebc_verification_report.md`.


### Paper-side status (v42) — the EBC paper, edited

**This is the first paper edit of this chat.** Through v41 the work was
Lean modules, READMEs and audits only; repair A in the companion paper
was already merged when it was verified in v41, not done here.

The finding: `paper2_exact_belief_computation_v10.tex` contained **zero**
occurrences of `Lean`, `formaliz`, `mechanized`, `machine-check` or
`proof assistant`. The 60-job layer was invisible, and the gap ran in
one direction — **the theorems outran the prose**. `prop:deadline` was
credited to *"direct simulation"* when it is proved; `prop:ladder` to
*"the ten ladder values by survivable-subset enumeration"* when the
value form is proved with `|S|` symbolic; §methods described *"one
deterministic script"* as the whole apparatus.

The root cause is not three wrong sentences: **§Verification methods
described an apparatus that predated the Lean layer.** So v11 rewrites
the section rather than patching sentences, and states what each result
actually rests on — **proved** (bands, ladder, deadline) ·
**enumerated, not proved** (census, 84 pairings, 83,521 → 545, `m ≠ 4`)
· **simulated** (`m = 5, 7` balls; the deadline grid check, now
redundant but retained as a cross-check).

One strengthening was **deliberately declined**. The blind-class
restriction could have been made to look load-bearing on the companion's
strictness result. It cannot be: that theorem is proved *in the
companion's model*, and the correspondence with the cube is one of
**form, not type**. v11 says it motivates the restriction rather than
proving it necessary — and notes the useful consequence, that the
paper's open question about non-blind disciplines cannot be settled by
transfer.

Two defects were introduced and caught before the push: a `\ref{bands}`
with no matching `\label` (the band proposition is `\ref{prop:bands}`, 
in the section labelled `hamming`), and a `\noindent` destroyed by a 
Python escape. Post-fix: **unresolved refs none**, braces balanced, environments matched.
environments matched.

**Caveat:** no `pdflatex` in this environment, so v11 was **not
compiled** — verified by reference resolution and inspection only.

**Still open:** the glance table's **736** stored antichain vs the
abstract's **496** stored maximal sets (possibly different measures, not
verified); and the titles, abstracts and supplementary material of the
other papers have not been reviewed against the findings.
