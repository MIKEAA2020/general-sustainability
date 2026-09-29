# `prop:deadline` — scoping (v38→v39)

**Verdict: SMALL. Smaller than a lag operator. Build it.**

## The statement (paper2_exact_belief_computation_v10.tex, ll. 365–392)

> Hold for `T` steps (drift `−1/2`), let the parameter be revealed
> exactly at `T`, then play matched forever (drift `+3/10` on every
> branch). Viability holds exactly when `z₀ ≥ 1 + T/2`, `T = 0,…,4`.

The proof in the paper (ll. 384–392) is explicitly **branchwise**:
*"under the hold every cell drifts −1/2, so at revelation every branch
sits at z₀ − T/2 … after revelation the matched action rises at +3/10 on
every branch."* And: *"the direct branchwise argument needs no
scalar-additivity hypothesis."*

## Why it is not delayed-instance dynamics

The "delay" is **entirely in the shape of the action sequence**, not in
the state. For branch `θ` the realized sequence is

```
hold^T  ++  (matched θ)^(L−T)
```

`survivesTo I θ us z0` is already a *branchwise* predicate parameterized
by `θ` and taking an arbitrary action list. Adaptivity after revelation
costs nothing: each branch supplies its own list, and `matched` is
θ-dependent by construction. There is **no** state expansion, **no**
belief/filter, **no** new transition structure, **no** non-Markovian
machinery. The revelation event never has to be modelled, because the
claim is about the realized trajectory.

## What the layer already has (all verified present)

| need | already there |
|---|---|
| hold action | `fun _ => Tri.hold` |
| hold drift `= −1/2` | `drift I u θ = -half + fifth * ipi I u θ`; `hold_action_zero I θ : ipi I (fun _ => Tri.hold) θ = 0` (EBC_ExactBelief_v2:119) |
| matched action | `matched θ` (EBC_Bands:79); `matched_is_cell` (EBC_Pairs_v2:68) |
| matched drift `= +3/10` | `ipi_matched I θ : ipi I (matched θ) θ = natToK I.length` (EBC_Bands:89); at `I.length = 4`: `−1/2 + (1/5)·4 = 3/10` |
| survivor recursion | `survivesTo I θ (u :: us) z = (1 ≤ z) ∧ survivesTo I θ us (z + drift I u θ)` (EBC_Dynamics:226) |
| closed form | `stateAfter_eq`, `survivesTo_final` (EBC_Dynamics) |
| constants | `half = 1/two`, `fifth = 1/five`, `ten`, `tenth`, `three` |

So the paper's two numbers are **already in the layer**: hold gives
`ipi = 0` → `−1/2`; matched gives `ipi = 4` → `−1/2 + 4/5 = +3/10`.

## Design for `EBC_Deadline.lean`

```lean
def holdAct : Nat → Tri := fun _ => Tri.hold

def deadlineSeq (T L : Nat) (θ : Nat → Bool) : List (Nat → Tri) :=
  List.replicate T holdAct ++ List.replicate (L - T) (matched θ)
```

Then:

1. `hold_drift` — `drift I holdAct θ = -half`. `unfold drift; rw [hold_action_zero]; simp`.
2. `matched_drift_nonneg (hI : I.length = 4)` — `0 ≤ drift I (matched θ) θ`.
   **Only need nonnegativity, not the exact 3/10**, because once
   `z ≥ 1` and the drift is `≥ 0`, no later constraint binds. This dodges
   the fiddly `4/5 − 1/2 = 3/10` identity; state it as a separate
   theorem if the paper's number is wanted for fidelity.
3. `hold_phase` — by induction on `t ≤ T`, the state after `t` holds is
   `z0 − t·half`, so `≥ 1` throughout iff `z0 ≥ 1 + T/2`.
4. `matched_phase` — by induction on the tail length, `z ≥ 1` + drift
   `≥ 0` ⇒ stays `≥ 1`. Nonneg drift makes this the easy induction.
5. `deadline_necessity` / `deadline_sufficiency` — combine via
   `survivesTo` on `deadlineSeq`.
6. `deadlineSeq_inAlphabet` — `holdAct` is `isFullHold`, `matched θ` is
   `isCellAction`, so the sequence is in the paper's 17-action alphabet.

## Risks (from the standing error list)

* `OrdField` is dependency-free: `add_le_add`, `mul_le_mul_of_nonneg'`,
  `le_trans`, `zero_le_one` exist; **`sub_nonneg` does not**. So
  `0 ≤ -half + x` must be got from `half ≤ x` via `add_le_add` +
  `add_neg_cancel`, not from a subtraction lemma.
* `two`/`five`/`ten`/`half`/`fifth`/`tenth` are `def`s, invisible to `rw`
  without `change`.
* No `ring`/`norm_num`/`linarith`.
* The `t·half` sum needs `natToK` recursion; `RatArith.natToK_mul_inv`
  may help.

## Imports

`EBC_Dynamics`, `EBC_Bands`, `EBC_Pairs_v2`, `EBC_Pairs_v3`, `RatArith`.
