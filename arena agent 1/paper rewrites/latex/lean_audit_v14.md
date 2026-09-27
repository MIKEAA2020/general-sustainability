# Lean audit v14 — result-level re-audit of the seven non-P3 modules

**Branch:** `lean-audit-v4` (additive). **Toolchain:** `v4.34.1`.
**This batch contains no new Lean module.** It is a statement-level audit:
every declaration of the seven modules outside the P3 work was extracted and
its **hypotheses and conclusion compared against the corresponding numbered
environment in the paper**.

**Method.** Declarations were machine-extracted (signature only, proof
bodies stripped) and each paper result was located by its `\label` and the
environment printed in full. Claims below are checked against the paper text,
not against the README.

---

## Headline

v13 found that `P3_ProbSufficiency`'s four generic kernel laws were indexed
as if they were `thm:recursion` and `thm:agree`. That pattern **does recur**,
but not uniformly, and it takes four distinguishable forms. Separately — and
this is a correction to my own working hypothesis — two modules I expected to
be weak turned out to be substantially sound.

| Failure mode | Meaning | Where found |
|---|---|---|
| **A. Alias** | The theorem's proof is a one-line call to an existing `Prelude` lemma; zero new content. | `E1_ForecastLadder` |
| **B. Triplication** | One theorem appears verbatim in three places and is indexed as three distinct results. | `Wk_mono_adm` / `master_action_axis` / `master_memory_axis` |
| **C. Vacuous target** | The paper contains **no numbered environments at all**, so the index entry refers to nothing. | `E1_ForecastLadder` |
| **D. Conclusion-as-hypothesis** | The paper's *conclusion* is taken as a hypothesis; what is proved is a trivial consequence of it. | `Comp_Certification.margin_obstruction_verdict`, `certified_sandwich` |

Mode **D** is the serious one. Modes A–C are bookkeeping and redundancy.

---

## Where my initial hypothesis was wrong

I began this batch expecting the small modules (`Comp_Certification`,
`ARV_RegimeViability`, `WS_WorkedSystems`) to be broadly hollow, on the
reasoning that any theorem whose hypotheses already contain the paper's
defining equation must be a restatement. **That inference was invalid**, and
the two cases where it failed are worth recording so it is not repeated.

**`ARV_RegimeViability` is sound on its conditional content.** `lem:bracket`
in `applied_regime_viability_v9.tex` genuinely *supposes* the accounting
form — "Suppose the interval's accounting has one of the two extreme
forms… `B_{t+1} = g_t B_t - C` … or `B_{t+1} = g_t (B_t - C)`". So
`bracket_form1`'s `hform : B' + C = g * B` and `bracket_form2`'s
`hform : B' = g * (B - C)` are **faithful transcriptions of a hypothesis the
paper actually makes**, not smuggled conclusions. The conclusions
(`g = ρ + r`, `g = ρ/(1-r)`) match the paper exactly. I was wrong to
suspect these.

**`WS_WorkedSystems` is sound on its distinct content.** `prop:master` states
three enlargements and the paper explicitly says "all three statements are
proved by the same induction on the horizon… each enlargement enlarges the
admissible action sets". The paper is up front that (i) policies and (iii)
memory are the same argument, because "every shared-register policy is a
per-branch policy" makes (iii) literally a set inclusion of admissible
actions. So `master_memory_axis` having the same shape as `master_action_axis`
reflects the mathematics, not laziness.

The correct generalisation of v13 is therefore narrower than "small modules
are hollow": **the defect is not small modules, it is index entries that
assert a numbered result when the code proves something else.** That is what
must be searched for, and it must be searched for per-result.

---

## Module-by-module

### `E1_ForecastLadder` — modes A and C, together the weakest module

`paperE1_cod_forecast_ladder_v59.tex` contains **zero** `theorem`,
`proposition`, `lemma` or `corollary` environments (counted: 0). Its only
`\label`s are sections, figures and tables (`introduction`, `results`,
`fig:power`, `tab:outcome`, …). It is an applied/empirical paper.

The README nevertheless claims: "`E1_ForecastLadder` | the ladder
bookkeeping: telescoping identity, two-sided level bracket, ascent law |
**done**". **There is no ladder result in the paper to formalize.**

The module's five theorems are generic `sumRange` arithmetic on `Nat → K`:

| Theorem | Status |
|---|---|
| `ladder_telescope` | **Alias.** Proof body is exactly `sumRange_telescope f N` — a one-line call to `Prelude.lean:559`. |
| `ladder_bound_upper` | Generic monotonicity of `sumRange`; `Prelude.sumRange_le_sumRange'` (line 534) already covers it. |
| `ladder_bound_lower` | Idem. |
| `ladder_bracket` | Conjunction of the previous two. |
| `ladder_ascent` | `∀i, f i ≤ f(i+1) → f 0 ≤ f N`: induction on `Nat`, no ladder content. |

Nothing in the module mentions a ladder, a level, a forecast, or a margin.
**Recommendation:** strike the row from the index, or reclassify it
explicitly as *machinery — generic `sumRange` lemmas duplicating `Prelude`;
the E1 paper has no numbered results*.

### `WS_WorkedSystems` — mode B (redundancy), content otherwise fine

`Wk_mono_obs` is genuine and distinct: it changes the observation *type* via
`refineObs` and proves the refinement monotonicity of `prop:master` (ii).
Good.

But `master_action_axis` and `master_memory_axis` are **verbatim identical
to each other and to `P1_Obstruction.Wk_mono_adm`** (line 417). All three
read:

```
(adm1 adm2 : S.A → S.X → Prop) (hsub : ∀ a x, adm1 a x → adm2 a x) :
  ∀ N B, Wk (S.withAdm adm1) N B → Wk (S.withAdm adm2) N B
```

only the parameter names differ. One theorem is therefore counted three
times, against three different results (`prop:monotone` action constituent,
`prop:master` (i), `prop:master` (iii)).

**Recommendation:** keep one copy in `P1_Obstruction`; have `WS_WorkedSystems`
alias it for `prop:master` (i) and (iii) with a header comment saying
explicitly that the paper itself notes (i) and (iii) are the same induction.
Reduce the count rather than delete the entry — the entry is correct, it is
the *multiplicity* that misleads.

### `Comp_Certification` — mode D, the substantive finding

| Theorem | Verdict |
|---|---|
| `robust_row_sound` | **Genuine.** One direction of `prop:rows`, in an abstracted finite-row setting. The paper states an iff; the module proves soundness. Honest as labelled. |
| `dual_feasible_certificate` | **Genuine but a restatement** of `Prelude`'s `farkas_sound` (the README says so). |
| `positive_bound_obstruction` | `ρ ≤ J`, `0 < ρ` ⟹ `0 < J`. One application of `lt_of_lt_of_le`. |
| `inflated_upper_bound_negative` | `J ≤ ρ+ē`, `ρ+ē < 0` ⟹ `J < 0`. One application of `lt_of_le_of_lt`. |
| `certified_sandwich` | **Assumes `hlo : ρ ≤ J` and `hhi : J ≤ ρ + ē`**, returns the conjunction of the two lines above. It does **not** establish that the computed `ρ`, `ē` bracket `J`. |
| `margin_obstruction_verdict` | **Assumes the paper's conclusion.** See below. |

On `margin_obstruction_verdict`. `prop:value` reads:

> The minimum exists: the policy-signal space is a finite product of
> **weak-\* compact sets `L^∞(I_r;U)`** … and each `F_a` is **weak-\*
> continuous**; the maximum over labels is attained on the compact label set
> `S` … **Consequently** `B_0 ∉ K_I^T` if and only if `J_I(T) > 0`.

The whole difficulty of `prop:value` is the existence of the minimum, and
the paper grounds it in weak-\* compactness and weak-\* continuity. That is
functional analysis, unreachable in this layer — a perfectly respectable
reason not to formalize it.

But the module does something different from not formalizing it. It takes

```
(hchar : ((∃ π, ∀ a, F a π ≤ 0) ↔ J ≤ 0))
```

as a **hypothesis**, adds `ρ ≤ J` and `0 < ρ`, and proves
`¬ ∃ π, ∀ a, F a π ≤ 0`. `hchar` is the paper's "consequently" clause — the
conclusion — promoted to an assumption. The types are `{A : Type}`,
`F : A → A → K`: an arbitrary type and an arbitrary binary `K`-valued
function, with nothing recognisable as a policy-signal space. What is proved
is a three-line consequence of the result, under a hypothesis that *is* the
result.

This is the clearest instance in the layer of the restatement trap, and it is
indexed as "`prop:value` margin-obstruction verdict | **done**".

**Recommendation:** relabel both as *conditional scaffolding*: state plainly
that `prop:value`'s existence content is beyond `OrdField`, and that what is
proved is the verdict procedure *given* the characterization and *given* the
sandwich — which is genuinely what the Python certificate layer consumes.

### `ARV_RegimeViability` — faithful, partial

As corrected above, `bracket_form1`/`bracket_form2` are faithful. Genuine
gaps, none of them fatal:

1. **The `max` upper bound is absent.** The paper concludes
   `ρ ≤ g_t ≤ max{ρ+r, ρ/(1-r)}`. No `max` appears anywhere in the module;
   only the two separate lower bounds `ρ ≤ ρ+r` and `ρ ≤ ρ/(1-r)` are proved.
2. **Only the "if" direction** of the final claim. The paper says the upper
   bound is `< 1` **iff** both `ρ+r < 1` and `ρ/(1-r) < 1`. `bracket_subunitary`
   proves `g < 1` from `g = (one of the two)` plus both `< 1` — the forward
   direction only, and about `g` rather than about `max`.
3. **Sign hypotheses are weaker than the paper's and partly unstated.** The
   paper assumes `B_t, B_{t+1} > 0`, `C ≥ 0`, `g_t > 0`. The module uses
   `B ≠ 0` (weaker — fine, stronger theorem) but never assumes `g_t > 0`, and
   `bracket_lower_form2` imports `0 ≤ B'/B` as a hypothesis where the paper
   would derive it from positivity.
4. **5 of 12 theorems are ordered-field algebra helpers**
   (`one_sub_div`, `mul_div_self`, `sub_sub_self`, `mul_right_cancel'`,
   `mul_lt_mul_of_pos_right`) — stdlib-level, not ARV content.

**Recommendation:** downgrade "in full" to **partial**, listing the `max`
bound and the converse as the missing pieces. Both are cheap to close.

### `Minimax_Dual` — the healthiest of the seven

`dual_certificate_sound` is real content (~20 lines) and correctly matches
`thm:dual`'s certificate-soundness direction. `parity_common_safe_empty` and
`parity_no_measure_certifies` are a genuine worked counterexample for
`prop:gap`. `ψsingle_sum`, `singleton_uniform`, `singleton_every_measure`,
`singleton_worst_witnesses` are a genuine instance for `prop:recover` (ii).
`benchmark_obstruction` is honest arithmetic on the margin. No modes A–D
detected. Six of its theorems are likewise arithmetic helpers, but they sit
alongside real content rather than instead of it.

### `P1_Obstruction` — substantive, unaffected

`Wk_antitone`, `Wk_descending`, `finite_horizon_sound`,
`finite_horizon_complete`, `tree_sound`, `blocked_iff`, `onestep_char`,
`epiK_coind`, `epiK_pre`, `policy_soundness`, `common_action_obstruction`,
`fibre_criterion`, `crossing_denies`, `not_Ysafe_iff`, `hidden_mode_conflict`
are all genuine, and the `ex:hidden-mode` instance is complete. The only
issue is the `Wk_mono_adm` duplication noted under `WS_WorkedSystems`.

---

## Corrected coverage — non-P3 slots

| Module | v1/v2 claim | Corrected | Mode |
|---|---|---|---|
| `Prelude` | machinery, 102 theorems | **unchanged** | — |
| `P1_Obstruction` | result | **result** — sound; one theorem triplicated | B |
| `Minimax_Dual` | result | **result** — sound as claimed | — |
| `Comp_Certification` | result (`prop:rows`, sandwich, `prop:value`, Farkas) | **1 result** (`prop:rows`, soundness only) + **1 restatement** (Farkas) + **4 conditional scaffolding** | D |
| `EBC_ExactBelief` | result (`lem:pairsum`, ladder doubling) | **not re-audited this batch** | — |
| `ARV_RegimeViability` | `lem:bracket` "in full" | **partial** — faithful conditional content; no `max`, no converse | — |
| `WS_WorkedSystems` | `prop:master` all three axes | **result** — 2 distinct lemmas, 1 theorem triplicated | B |
| `E1_ForecastLadder` | "ladder bookkeeping" | **machinery** — 5 generic `sumRange` lemmas, 1 a pure alias; **target paper has no numbered results** | A, C |
| `P1_AssessmentSeparation` | result | **not re-audited this batch** | — |

Two modules (`EBC_ExactBelief`, `P1_AssessmentSeparation`) were **not**
re-audited; I carried their v1 descriptions forward. They should be checked
before any coverage claim about them is relied on. `P1_AssessmentSeparation`
is the largest entry in the index and the most specific in its claims, which
makes it the highest-value remaining check rather than the safest to assume.

---

## Suggested next steps

1. **Close the two cheap ARV gaps** — the `max` upper bound and the converse
   direction — and the module becomes a complete formalization of
   `lem:bracket`. Small, well-scoped, and it converts a "partial" into a
   "result".
2. **De-triplicate `Wk_mono_adm`** into a single declaration with three
   documented call sites.
3. **Re-audit `P1_AssessmentSeparation`** at result level. If the
   `P3_ProbSufficiency` / `Comp_Certification` pattern appears in the largest
   module, that is the most consequential correction available.
4. **Issue `lean_README_v3.md`** folding in the corrected rows above. v2 is
   already pushed and must not be edited in place.
