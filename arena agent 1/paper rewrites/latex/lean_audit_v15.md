# Lean audit v15 — closing the v14 follow-ups

**Branch:** `lean-audit-v4` (additive). **Toolchain:** `v4.34.1`.
**Build:** `lake build` → **rc = 0, 23 jobs**.
**Zero `sorry`** project-wide.

This batch executes the four items listed as *Suggested next steps* in v14.
Items 1 and 2 are new modules; item 3 is a read-only audit; item 4 is
`lean_README_v3.md`.

| Item | Outcome |
|---|---|
| 1. Close the two ARV gaps | **Done** — `lem:bracket` is now complete; partial → result |
| 2. De-triplicate `Wk_mono_adm` | **Done** — single canonical declaration |
| 3. Re-audit `P1_AssessmentSeparation` | **Done — the pattern does *not* recur.** This module is the model of good practice |
| 4. Issue `lean_README_v3.md` | **Done** — pushed alongside this file |

---

## 1. `ARV_RegimeViability_v2` — `lem:bracket` closed

New module (imports `ARV_RegimeViability`; namespace `Formalizations.ARV`).

**Why `omax` had to be defined from scratch.** `OrdField` is a bare
ordered-field interface carrying `le_total` but **no `max` operation**, and
this project has no Mathlib dependency. So the bracket's `max` is introduced
locally, with exactly the four laws the lemma needs proved from `le_total`
alone:

| Lemma | Content |
|---|---|
| `omax_of_le`, `omax_of_not_le` | the two reduction laws |
| `le_omax_left`, `le_omax_right` | `a ≤ max a b`, `b ≤ max a b` |
| `omax_le` | `a ≤ c → b ≤ c → max a b ≤ c` |
| `omax_lt` | `a < c → b < c → max a b < c` |
| `omax_lt_iff` | `max a b < c ↔ a < c ∧ b < c` |

Nothing here is application-specific; it is the standard total-order maximum.

**Gap 1 — the `max` upper bound** (v14: "no `max` appears anywhere"):

- `bracket_upper_form1` — under `B' + C = g·B`, `g ≤ omax (ρ+r) (ρ/(1-r))`
- `bracket_upper_form2` — under `B' = g·(B-C)`, same
- `bracket_sandwich_form1` / `bracket_sandwich_form2` — the paper's
  `ρ ≤ g_t ≤ max{ρ+r, ρ/(1-r)}` **in full**, both forms

**Gap 2 — the converse** (v14: "only the forward direction, and about `g`
rather than the upper bound"):

- `bracket_upper_lt_one_iff` — `max{ρ+r, ρ/(1-r)} < 1 ↔ (ρ+r < 1 ∧ ρ/(1-r) < 1)`.
  This is exactly the paper's "the upper bound is strictly below `1` **if and
  only if** both `ρ+r < 1` and `ρ/(1-r) < 1`".

Two sharper statements were added while closing it, because the relationship
between `g` and the upper bound is easy to state wrongly:

- `bracket_subunitary_form1` / `_form2`: `g < 1 ↔ (its own bracket form) < 1`.
  This is stronger and cleaner than v1's `bracket_subunitary`, which routed
  through a disjunction over both forms and therefore needed **both** to be
  below `1` — a strictly stronger hypothesis than the form actually requires.
- `bracket_subunitary_of_upper_form1` / `_form2`: `g < 1` from the upper
  bound being below `1`.

**A deliberate omission, recorded.** The converse of *that last* implication
is **false**, and the header says so: `g` equals only *one* of the two
bracket forms, so `g < 1` says nothing about the other form. The paper's iff
is about the **upper bound**, which is `bracket_upper_lt_one_iff`. Stating
both directions for `g` would have been false; stating only the true one and
flagging the asymmetry is the honest resolution.

**Minor finding:** v1's header cites `applied_regime_viability_v6.tex` as
source of record; the current edition is **v9**. `lem:bracket` is unchanged
between the two, so v1 is not stale — only the citation is. v2 cites v9.

*Axioms:* `bracket_sandwich_form1`, `bracket_upper_lt_one_iff`, `omax_lt_iff`
→ `[propext, Classical.choice, Quot.sound]`. Choice enters only through the
`noncomputable` `if` in `omax` (the interface has no decidability for `≤`).
No `sorry`.

## 2. `WS_WorkedSystems_v2` — `Wk_mono_adm` de-triplicated

New module (imports `P1_Obstruction`; namespace `Formalizations.WS`).
One declaration, `master_monotone`, with the three indexed call sites
documented in a single header comment: `prop:monotone` (action constituent),
`prop:master` (i) policies, `prop:master` (iii) memory. Plus
`monotone_action_axis` as a named alias.

**`master_monotone` depends on no axioms at all** — `[propext, Classical.choice,
Quot.sound]` do not appear. It is a pure induction on `Nat`.

The three legacy declarations (`P1.Wk_mono_adm`, `WS.master_action_axis`,
`WS.master_memory_axis`) are left in place — this project never overwrites —
and are now to be read as aliases of the one canonical proof. The genuinely
distinct result, `prop:master` (ii) observations, remains
`WS.Wk_mono_obs`, which changes the observation *type* rather than the
admissible-action predicate.

Worth restating from v14, because it is what makes de-triplication the right
call rather than a deletion: the triplication was not sloppiness. The paper
says of its three enlargements that "all three statements are proved by the
same induction on the horizon". What misled was the **count**, not the
content.

## 3. `P1_AssessmentSeparation` — the pattern does **not** recur

This was the highest-value check available, and the result is negative in the
good sense. The module (v4, 247 declarations, 164 KB) is the **best-documented
module in the layer** and exhibits none of failure modes A–D.

I checked the README's most falsifiable claims rather than its vague ones.
An initial grep for `8 / 5`, `13 / 8`, `9 / 5`, `5 / 4`, `6 / 5`, `3 / 2`
returned **zero** hits, which looked like confirmation of a defect. It was
not: the module writes rationals as `natK n / natK m` over the abstract field,
so `natK 8 / natK 5` is the witness. Re-checked in that form, every claimed
witness is present (`natK 8`, `natK 13`, `natK 9`, `natK 6`, `natK 5`,
`natK 3`, `natK 141 / natK 100`). **This near-miss is recorded so the
literal-grep inference is not repeated** — it is the same class of error as
my v14 hypothesis that ARV's `hform` was a smuggled conclusion.

What the module does that the others do not:

1. **Separates convention from theorem.** Lemma B(i) is a *convention* —
   "stipulated in `ThetaSubAdm`/`ThetaMidAdm`, not derived from the rung
   algebra (it cannot be: see `collapse_convention_not_implied`)". A theorem
   stating that the convention is **not** implied is the direct opposite of
   promoting a conclusion to a hypothesis.
2. **States what is not formalized, and why.** Theorem S1 (nesting) is "genuinely
   analytic (real exponents)"; the relative-interior topology of Theorem 5(4)
   and the IVT step in S2(ii) are "replaced by explicit rational interval
   witnesses (a **constructive strengthening**)" — each replacement labelled
   as a strengthening, not passed off as the original.
3. **Every specific numeric claim in the README traces to code** — the
   Fibonacci witnesses 8/5 rejects / 13/8 accepts, `σ = 1/4` at 9/5, the
   `∀m` false-certification family, the `σ = 2` floor `5/4` as an iff, the
   `σ = 3` datum 6/5, the LPI witness 3/2, and `141/100`.

**The one imprecision is in the README, not the module.** The README says
"Theorem 5 (1)–(7) **in full**"; the module is explicit that 5(4)'s
relative-interior topology is *replaced* by an explicit strictly-interior
witness. That is a genuine strengthening, but it is not "in full" as the paper
states it. Corrected in v3 of the README.

**Housekeeping finding (not a correctness issue).** Three versions exist —
`P1_AssessmentSeparation.lean` (246 decls, 160 KB), `_v3` (247, 164 KB),
`_v4` (247, 165 KB) — but **only `_v4` is imported**. v1 and v3 are ~325 KB of
unimported legacy in the tree. Harmless, but it inflates the declaration
count (395 theorems) that the README advertises.

## 4. Other findings from the full build

- **`EBC_ExactBelief.lean` emits 4 warnings** ("This simp argument is
  unused", lines 89–91). Pre-existing, not introduced here, and not reported
  in earlier audits. Cosmetic, but the project's stated standard is
  zero warnings.
- **`P1_AssessmentSeparation_v4` emits 3 warnings** (unused variable names
  `hq`, `hnn`, `hq` at lines 3027, 3037, 3075). Also cosmetic.
- Neither affects soundness. Flagged because v12/v13 reported "zero
  warnings" for the whole project, which was true of the modules built in
  those batches but not of the project as a whole. Corrected here.

## Corrected coverage — non-P3 slots (supersedes v14)

| Module | v1 claim | Corrected |
|---|---|---|
| `P1_Obstruction` | result | **result** — sound; de-triplicated in v2 |
| `Minimax_Dual` | result | **result** — sound as claimed |
| `Comp_Certification` | result | **1 result** (`prop:rows` soundness) + 1 restatement + **4 conditional scaffolding** (mode D) |
| `EBC_ExactBelief` | result | **not re-audited**; 4 warnings noted |
| `ARV_RegimeViability` | `lem:bracket` "in full" | **result** — v2 closes both gaps |
| `WS_WorkedSystems` | `prop:master` three axes | **result** — 2 distinct lemmas; triplication resolved |
| `E1_ForecastLadder` | "ladder bookkeeping" | **machinery** — 5 generic `sumRange` lemmas, 1 a pure alias; target paper has **no numbered results** (modes A, C) |
| `P1_AssessmentSeparation` | result | **result** — verified; no modes A–D; README's "in full" for 5(4) corrected |

## Suggested next steps

1. **Re-audit `EBC_ExactBelief`** — the last non-P3 slot never checked at
   result level, and it now carries the project's only simp warnings.
2. **Close `Comp_Certification` mode D properly.** The honest fix is not to
   delete the scaffolding (the Python certificate layer consumes it) but to
   add, for each of the four, a header stating that the sandwich and the
   characterization are *inputs supplied by the certificate computation*.
3. **Prune or clearly mark** the two unimported `P1_AssessmentSeparation`
   versions so the 395-theorem count reflects live code.
