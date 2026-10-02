/-
  Formalizations.P3_Binomial
  ==========================

  **Binomial coefficients — the combinatorial foundation for the Sperner
  bound in `prop:antichain` (iii).**

  `prop:antichain` (iii):

  > the maximal elements form an antichain, so their number is at most
  > `\binom{n}{\lfloor n/2 \rfloor}` for a support of size `n` (Sperner).

  The antichain property is formalized (v20). **The count is not**, and this
  module is the first of the pieces it needs.

  ## Why a whole module for `n` choose `k`

  This layer is dependency-free: it carries **no `Nat.choose`**, no
  `Nat.factorial`, no `List.permutations`, and no algebraic hierarchy
  (there is no `LinearOrderedField` in scope — `OrdField` is this layer's
  own interface). Binomial coefficients therefore have to be *defined*
  here, and their laws proved from the recursion, before Sperner's theorem
  can even be stated.

  The definition is Pascal's recursion, so the recursion theorem is `rfl`
  and the boundary behaviour is what needs proving.

  ## What Sperner still needs

  The bound is `|A| ≤ C(n, ⌊n/2⌋)` for an antichain `A`. The standard route
  is LYM:

  1. **`C(n,k) ≤ C(n, ⌊n/2⌋)`** — unimodality, i.e. the binomials peak at
     the middle. (This module: `choose_le_middle`.)
  2. **LYM**: `Σ_{S ∈ A} 1 / C(n, |S|) ≤ 1`, proved by counting maximal
     chains: each permutation of the `n` ground elements gives a maximal
     chain, an antichain meets each chain at most once, and exactly
     `k! (n-k)!` chains pass through a given `k`-set. Needs factorials,
     a permutation enumerator, and the identity
     `C(n,k) · k! · (n-k)! = n!`.
  3. **The bound**: `|A| / C(n, ⌊n/2⌋) ≤ Σ 1/C(n,|S|) ≤ 1`.

  **None of steps 1–3 is proved here.** This module supplies the
  binomial coefficients themselves — `choose` and its laws — which is the
  prerequisite without which the bound cannot even be stated. The
  remaining pieces are recorded in `lean_audit_v31.md`:
  unimodality (`C(n,k) ≤ C(n, n/2)`), LYM by maximal-chain counting
  (factorials, a permutation enumerator, and
  `C(n,k)·k!·(n-k)! = n!`), and the final cardinality bound. Unimodality
  was attempted and **is not claimed**: the two-step recursion needs the
  boundary case `2(k+2) = n+1`, which is binomial *symmetry* — so
  symmetry has to come first, and it is a separate induction.
  This module is **machinery**, not a result.

  ## Contents

    choose                 binomial coefficient, by Pascal recursion
    choose_zero_right, choose_succ_succ, choose_zero_succ
    choose_self, choose_eq_zero_of_lt, choose_pos
    choose_succ_self       `C(n+1,n) = n+1`
    choose_six_three       a numerical check of the recursion
-/

import Formalizations.Prelude

namespace Formalizations.P3

set_option linter.unusedSectionVars false

/-- Binomial coefficient, by Pascal's recursion. -/
def choose : Nat → Nat → Nat
  | _, 0 => 1
  | 0, _ + 1 => 0
  | n + 1, k + 1 => choose n k + choose n (k + 1)

/-- Pascal's recursion is the definition. -/
theorem choose_succ_succ (n k : Nat) :
    choose (n + 1) (k + 1) = choose n k + choose n (k + 1) := rfl

theorem choose_zero_right : ∀ n, choose n 0 = 1
  | 0 => rfl
  | _ + 1 => rfl

theorem choose_zero_succ : ∀ k, choose 0 (k + 1) = 0
  | 0 => rfl
  | _ + 1 => rfl

/-- `C(n,k) = 0` beyond the diagonal. -/
theorem choose_eq_zero_of_lt : ∀ {n k : Nat}, n < k → choose n k = 0
  | 0, k + 1, _ => rfl
  | n + 1, k + 1, h => by
      rw [choose_succ_succ]
      have h1 : choose n k = 0 :=
        choose_eq_zero_of_lt (Nat.succ_lt_succ_iff.mp h)
      have h2 : choose n (k + 1) = 0 :=
        choose_eq_zero_of_lt (Nat.lt_trans (Nat.lt_succ_self n) h)
      rw [h1, h2]

/-- On the diagonal. -/
theorem choose_self : ∀ n, choose n n = 1
  | 0 => rfl
  | n + 1 => by
      rw [choose_succ_succ]
      rw [choose_eq_zero_of_lt (Nat.lt_succ_self n), choose_self n]

/-- Binomials are positive on and below the diagonal. -/
theorem choose_pos : ∀ {n k : Nat}, k ≤ n → 0 < choose n k := by
  intro n
  induction n with
  | zero =>
      intro k hk
      have hk0 : k = 0 := Nat.eq_zero_of_le_zero hk
      subst k
      exact Nat.zero_lt_succ 0
  | succ n ih =>
      intro k hk
      cases k with
      | zero => exact Nat.zero_lt_succ 0
      | succ k =>
          rw [choose_succ_succ]
          exact Nat.add_pos_left (ih (Nat.le_of_succ_le_succ hk)) _

theorem choose_succ_self : ∀ n, choose (n + 1) n = n + 1 := by
  intro n
  induction n with
  | zero => rfl
  | succ n ih =>
      rw [choose_succ_succ, ih, choose_self]

/-- A numerical check that the recursion really computes binomials. -/
theorem choose_six_three : choose 6 3 = 20 := by decide

end Formalizations.P3
