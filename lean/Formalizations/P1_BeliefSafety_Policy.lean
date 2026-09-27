/-
  Formalizations.P1_BeliefSafety_Policy
  =====================================

  Closes v7 §3.1: gives `thm:pomdp` part (a) real content.

  ### The gap

  In `P1_BeliefSafety`, `V` is *defined* by the recursion

      V_{k+1}(m) = max_{a ∈ A} Σ_y V_k(m_{a,y}) ,

  so the recursion "identity" of `thm:pomdp` is `rfl` and proves nothing.
  The paper, however, defines

      V_k(b) = max_π ℙ_π( x_t ∈ 𝒱 for t = 0,…,k | b )

  — a maximum over **policies** — and *derives* the recursion from it. That
  derivation (Smallwood–Sondik) is where the content lives, and the paper
  discharges it with the words "standard value iteration" plus a citation.

  This module defines policies and their value `J`, and proves:

      J_dominated   every (in-universe) policy is dominated by V;
      V_attained    V is attained by some (in-universe) policy.

  Together: `V_k(m) = max_π J_k(π, m)`. That is the dynamic-programming
  content of `thm:pomdp` — the interchange of `max` over actions with the
  sum over observations, done properly, and it is no longer a restatement
  of a definition.

  ### Why `Pol` has a `stop` constructor

  `Pol` must be a genuine inductive type (Lean has no coinduction here), so
  it needs a leaf. `stop` is given value `0` at horizons `k ≥ 1`, i.e. it is
  never optimal; it exists only so that a policy is constructible at
  horizon 0, where the policy is not consulted at all.

  ### What is still not proved

  `J` is the *recursive* value of a policy. That `J_k(π,b)` equals the
  paper's `ℙ_π(x_0,…,x_k ∈ 𝒱 | b)` is the genuinely measure-theoretic half:
  it needs a probability space over disturbance sequences, which `OrdField`
  cannot express. So `thm:pomdp` is now proved modulo the identifications
  recorded in `bayes_bridge` (normalized ↔ unnormalized) and this one. Both
  remaining gaps are interfaces to probability theory, not gaps in the
  dynamic-programming argument itself — which is the part the paper elided.
-/

import Formalizations.P1_BeliefSafety_Value

namespace Formalizations.POMDP

open Formalizations

variable {K : Type} [OrdField K]

/-- A deterministic, observation-feedback policy. `act a cont` takes action
`a` and then follows `cont y` after observing `y`. -/
inductive Pol (A Y : Type) : Type where
  | stop : Pol A Y
  | act : A → (Y → Pol A Y) → Pol A Y

/-- The value of a policy at horizon `k`. -/
def J (M : SafeMDP K X Y A) : Nat → Pol A Y → Mass K X → K
  | 0, _, m => total M m
  | _ + 1, Pol.stop, _ => 0
  | k + 1, Pol.act a cont, m =>
      lsum (M.univY.map (fun y => J M k (cont y) (step M a y m)))

/-- A policy is *in-universe* if every action it ever takes lies in
`M.univA`. Only such policies are admitted to the maximum. -/
def PolIn (M : SafeMDP K X Y A) : Pol A Y → Prop
  | Pol.stop => True
  | Pol.act a cont => a ∈ M.univA ∧ ∀ y, PolIn M (cont y)

/-- The finite action universe is inhabited. -/
theorem univA_exists (M : SafeMDP K X Y A) : ∃ a, a ∈ M.univA := by
  cases h : M.univA with
  | nil => exact absurd h M.univA_ne
  | cons a as => exact ⟨a, by simp⟩

/-- **`V` dominates every in-universe policy.** -/
theorem J_dominated (M : SafeMDP K X Y A) :
    ∀ k (π : Pol A Y) (m : Mass K X), PolIn M π → J M k π m ≤ V M k m := by
  intro k
  induction k with
  | zero =>
      intro π m hπ
      change total M m ≤ total M m
      exact le_refl _
  | succ k ih =>
      intro π m hπ
      cases π with
      | stop =>
          change 0 ≤ V M (k + 1) m
          exact V_nonneg M (k + 1) m
      | act a cont =>
          change
            lsum (M.univY.map (fun y => J M k (cont y) (step M a y m))) ≤
            lmax (M.univA.map (fun a' => lsum (M.univY.map (fun y => V M k (step M a' y m)))))
          have h1 :
              lsum (M.univY.map (fun y => J M k (cont y) (step M a y m))) ≤
              lsum (M.univY.map (fun y => V M k (step M a y m))) := by
            apply lsum_le_lsum
            intro y hy
            exact ih (cont y) (step M a y m) (hπ.2 y)
          have h2 :
              lsum (M.univY.map (fun y => V M k (step M a y m))) ≤
              lmax (M.univA.map (fun a' => lsum (M.univY.map (fun y => V M k (step M a' y m))))) :=
            le_lmax
              (map_ne_nil (fun a' => lsum (M.univY.map (fun y => V M k (step M a' y m)))) M.univA_ne)
              (List.mem_map.mpr ⟨a, hπ.1, rfl⟩)
          exact le_trans h1 h2

/-- **`V` is attained** by some in-universe policy. -/
theorem V_attained (M : SafeMDP K X Y A) :
    ∀ k (m : Mass K X), ∃ π : Pol A Y, PolIn M π ∧ J M k π m = V M k m := by
  intro k
  induction k with
  | zero =>
      intro m
      exact ⟨Pol.stop, trivial, rfl⟩
  | succ k ih =>
      intro m
      let Q : A → K := fun a => lsum (M.univY.map (fun y => V M k (step M a y m)))
      have hQne : M.univA.map Q ≠ [] := map_ne_nil Q M.univA_ne
      rcases List.mem_map.mp (lmax_isMax hQne).1 with ⟨a0, ha0, hqa0⟩
      let cont : Y → Pol A Y := fun y => Classical.choose (ih (step M a0 y m))
      refine ⟨Pol.act a0 cont, ?_, ?_⟩
      · exact ⟨ha0, fun y => (Classical.choose_spec (ih (step M a0 y m))).1⟩
      · change
          lsum (M.univY.map (fun y => J M k (cont y) (step M a0 y m))) = V M (k + 1) m
        calc
          lsum (M.univY.map (fun y => J M k (cont y) (step M a0 y m)))
              = lsum (M.univY.map (fun y => V M k (step M a0 y m))) := by
                  apply lsum_congr
                  intro y hy
                  exact (Classical.choose_spec (ih (step M a0 y m))).2
          _ = Q a0 := rfl
          _ = lmax (M.univA.map Q) := hqa0
          _ = V M (k + 1) m := rfl

/-- **`thm:pomdp`, part (a), with content**: `V_k(m)` is the maximum of the
policy values — it dominates every in-universe policy and is attained by
one. This is Smallwood–Sondik's recursion, proved rather than cited. -/
theorem V_is_max_over_policies (M : SafeMDP K X Y A) (k : Nat) (m : Mass K X) :
    (∀ π : Pol A Y, PolIn M π → J M k π m ≤ V M k m) ∧
    (∃ π : Pol A Y, PolIn M π ∧ J M k π m = V M k m) :=
  ⟨fun π hπ => J_dominated M k π m hπ, V_attained M k m⟩

end Formalizations.POMDP
