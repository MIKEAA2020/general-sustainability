# Lean audit v16 — `EBC_ExactBelief` re-audit, and relabelling `Comp_Certification`

**Branch:** `lean-audit-v4` (additive). **Toolchain:** `v4.34.1`.
**Build:** `lake build` → **rc = 0, 24 jobs**. Warnings: **7**, unchanged
(4 `EBC_ExactBelief`, 3 `P1_AssessmentSeparation_v4`); **0** from the new
module. Zero `sorry`.

| Item | Outcome |
|---|---|
| Re-audit `EBC_ExactBelief` | **Done** — the last non-P3 slot checked. Verdict: accurate, but 1 of 8 results |
| Relabel `Comp_Certification` scaffolding | **Done** — `Comp_Certification_v2`, 4 theorems, axiom-free, no proof duplicated |

---

## 1. `EBC_ExactBelief` — result-level audit

`paper2_exact_belief_computation_v10.tex` has **8 named results** (5
propositions, 2 lemmas, 1 corollary): `lem:pairsum`, `lem:triangle`,
`prop:bands`, `prop:census`, `prop:deadline`, `prop:ladder`, `prop:pbvi`,
`cor:hamming`. The module formalizes **one**: `lem:pairsum` (i).

### `lem:pairsum` (i) — correctly formalized

The paper: for `θ, θ' ∈ {+1,−1}^m` at Hamming distance `h`, and
`u ∈ {+1,−1}^m`, `⟨u,θ⟩ + ⟨u,θ'⟩ ≤ 2(m − h)`, "and the hold action gives
`0` for every pair".

- `pair_sum_bound`: `ipi I u θ + ipi I u θ' ≤ (1+1) * agreeMass I θ θ'`.
  `agreeMass` counts coordinates where `θ`, `θ'` agree — exactly `m − h`.
  **Exact match.**
- `hold_action_zero`: the hold action gives `0`. **Match.**

`lem:pairsum` **(ii)** is *not* formalized, and correctly so: it asserts a
`liminf_{T→∞} (1/T) Σ_{t<T}` bound, which needs limits — out of reach of
`OrdField`. The README does not claim it.

### `ladder_doubling` — accurate as labelled, but it is not `prop:ladder`

`prop:ladder` is a concrete claim: uniform prior on **sixteen** cells, probes
refining the support to a subcube, the chain
`1/16 → 1/8 → 1/4 → 1/2 → 1` at `z₀ = 1.0` and
`1/8 → 1/4 → 1/2 → 1 → 1` at `z₀ ≥ 1.1`, over zero to four probes, plus the
two edge facts (above the band three probes exhaust observation; at the edge
the fourth probe is worth `1/2`). All of that is instance-level.

`ladder_doubling` proves the **abstract doubling step** — if `A` has exactly
twice the mass of sub-event `B`, the conditional mass of `B` given `A` is
exactly one half. That is the mechanism behind `prop:ladder`, not the
proposition.

**This is the one slot where the index is already honest about it.** The v1/v3
row says "the **observation-ladder doubling** (exact-halving conditional
mass)", which describes `ladder_doubling` as it is, and it names
`prop:ladder` nowhere. Compare `E1_ForecastLadder` (v14), where a
generic alias was indexed as a paper result that does not exist. So no
mode-A/C/D defect here — but the slot reads as though more of the paper is
covered than is (1 of 8), which the corrected row below fixes.

### The 4 warnings

All four are "unused simp argument" in `coord_bound` (lines 89–91), whose
`simp` list carries fourteen entries:
`mul_one, one_mul', mul_neg, neg_mul, neg_mul_neg, mul_zero, add_neg_cancel,
neg_add_cancel, zero_add, add_zero, neg_one_pair_le, zero_le_one',
zero_le_two', le_refl`. The proof is `cases t <;> cases t' <;> cases u <;>
simp [...]`, so which of the fourteen are live depends on the branch; four are
dead in every branch. Purely cosmetic — but the project's stated standard is
zero warnings, and this is now the only outstanding source besides
`P1_AssessmentSeparation_v4`'s three unused names.

### Corrected index row (to fold into `lean_README_v4`)

> **`EBC_ExactBelief` — result, partial coverage.** `lem:pairsum` **(i)** —
> the pair-sum bound (`pair_sum_bound`) and the hold action
> (`hold_action_zero`) — an exact match to the paper. `lem:pairsum` **(ii)**
> is out of reach (needs `liminf`). `ladder_doubling` is the abstract
> exact-halving step behind **`prop:ladder`**, not that proposition, which is
> instance-level (sixteen cells, four probes, two regimes). **1 of 8 named
> results** in the paper. Carries 4 of the project's 7 warnings (unused simp
> arguments in `coord_bound`).

## 2. `Comp_Certification_v2` — the input contract made explicit

New module (imports `Comp_Certification`; namespace
`Formalizations.CompCert`). Four theorems, each a **one-line delegation** to
its v1 counterpart — **no proof is duplicated**, only the names and headers
change:

| New name | Delegates to | Input made explicit |
|---|---|---|
| `sandwich_verdict_lower` | `positive_bound_obstruction` | `ρ ≤ J` |
| `sandwich_verdict_upper` | `inflated_upper_bound_negative` | `J ≤ ρ + ē` |
| `sandwich_verdict` | `certified_sandwich` | both sides of the sandwich |
| `characterization_verdict` | `margin_obstruction_verdict` | `hchar`, and the fact that it is one direction only |

The module header carries an **input contract** table naming, for each input,
what produces it: the two sandwich bounds come from *the certificate
computation*; the characterization comes from *`prop:value`*. Two headers say
outright what v1 did not:

- `sandwich_verdict`: "**This theorem does not establish that the computed
  `ρ` and `ē` bracket `J`.** It states what follows *once* they do."
- `characterization_verdict`: "**The characterization is an input, not a
  result of this layer.** It is the 'consequently' clause of `prop:value`,
  whose real content — existence of the minimum, from weak-\* compactness of
  `L^∞(I_r; U)` and weak-\* continuity of each `F_a` — lies beyond
  `OrdField`."

Both new theorems **depend on no axioms at all** — not even `propext`.

Three judgements behind the approach, recorded because they are the part that
could reasonably be done differently:

1. **Relabel, do not delete.** The Python certificate layer genuinely
   consumes these four facts, so removing them would break the
   Lean-gives-the-checks-meaning contract described in the README's
   architecture section. The defect was the *labelling*, not the content.
2. **Delegate, do not re-prove.** Re-proving the four would have added a
   fifth and sixth copy of theorems the project already has too many copies
   of — the same prolixity v15 criticised in `Wk_mono_adm`. The value here
   is entirely in the headers.
3. **Leave v1 in place.** This project never overwrites. The v1 declarations
   remain, and the module header says they "should now be read as the same
   procedures under names that did not advertise their contract."

---

## State of the layer after v16

Full build **rc = 0, 24 jobs**, zero `sorry`, 7 cosmetic warnings.

| Slot | Status |
|---|---|
| `P1_Obstruction`, `Minimax_Dual`, `P1_AssessmentSeparation_v4` | result, audited, no defects |
| `P1_TimingCertificate`, `P1_BeliefSafety{,_Value,_Policy}` | result (v7, v8) |
| `ARV_RegimeViability` (+`_v2`) | **result** — `lem:bracket` complete (v15) |
| `WS_WorkedSystems` (+`_v2`) | **result** — 2 distinct lemmas (v15) |
| `Comp_Certification` (+`_v2`) | 1 result + 1 restatement + 4 **input-taking** procedures (v16) |
| `P3_*` | 7 result · 4 partial · 6 instance · 1 out of reach |
| `EBC_ExactBelief` | **1 of 8** — `lem:pairsum` (i) exact (v16) |
| `E1_ForecastLadder` | machinery; target paper has no numbered results (v14) |

**Every non-P3 slot has now been audited at result level.** No slot is
unexamined.

## Suggested next steps

1. **Issue `lean_README_v4.md`** folding in the corrected `EBC_ExactBelief`
   row above and the `Comp_Certification_v2` relabelling. This is the only
   reason v3 is now stale.
2. **Clear the 7 warnings** — trim the dead simp arguments in
   `EBC_ExactBelief.coord_bound` and rename the three unused binders in
   `P1_AssessmentSeparation_v4` to `_`. Pure hygiene; restores the
   zero-warning standard.
3. **The four P3 partials** remain the largest body of unfinished
   mathematics: `thm:support`'s support identity, `prop:antichain` (ii),
   `prop:pl` convexity, and `prop:freeze`'s drop count.
