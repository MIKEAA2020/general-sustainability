/-
  Formalizations.P1_BeliefSafety_Value
  ====================================

  Closes the two gaps left open by `P1_BeliefSafety` (audit v7 §3.2, §3.3):

  **(a) the homogeneity bridge.** `P1_BeliefSafety` works with unnormalized
  sub-probability masses and the recursion `V_{k+1}(m) = max_a Σ_y V_k(m_{a,y})`,
  while the paper uses the normalized Bayes form
  `V_{k+1}(b) = max_a Σ_y ℙ(y|b,a) · V_k(τ(b,a,y))`. `bayes_bridge` below
  proves the two summand-by-summand, including the degenerate
  `ℙ(y|b,a) = 0` case that the normalization-by-division formulation
  cannot even state.

  **(b) `prop:chance`.** The chance-constrained obstruction, derived from an
  *equality* form of the one-step bound plus horizon antitonicity.

  Nothing here is overwritten: `P1_BeliefSafety` is imported unchanged.

  ### Design note: why there is no `Mass.ext`

  `Prelude` does not generate a usable extensionality theorem for `Mass`
  (its `nonneg` field is proof-valued, so the two candidate masses are equal
  but not definitionally so). Rather than restructure `Mass`, this module
  proves `V_congr` — `V` depends on a mass only through its `.f` field — and
  transports every needed equality through that. This is also the honest
  statement: `V` is a function of the mass function, not of the proof that
  it is nonnegative.
-/

import Formalizations.P1_BeliefSafety

namespace Formalizations.POMDP

open Formalizations

variable {K : Type} [OrdField K]

/-! ## Small order helpers -/

theorem sub_le_sub_right_of_le {a b : K} (h : a ≤ b) (c : K) : a - c ≤ b - c :=
  add_le_add h (le_refl (-c))

theorem le_sub_of_add_le_of {a b c : K} (h : a + c ≤ b) : a ≤ b - c := by
  have h2 : a + c - c ≤ b - c := sub_le_sub_right_of_le h c
  simpa [add_sub_cancel] using h2

/-- Pointwise congruence for `List.map`. -/
theorem map_congr_fun {α β : Type} : ∀ (l : List α) (f g : α → β),
    (∀ a, a ∈ l → f a = g a) → l.map f = l.map g := by
  intro l
  induction l with
  | nil =>
      intro f g h; rfl
  | cons x xs ih =>
      intro f g h
      simp only [List.map_cons]
      rw [h x (by simp)]
      congr 1
      apply ih
      intro a ha
      exact h a (by simp [ha])

/-! ## Total mass is nonnegative -/

theorem total_nonneg (M : SafeMDP K X Y A) (m : Mass K X) : 0 ≤ total M m := by
  unfold total
  apply lsum_nonneg_map
  intro x
  exact m.nonneg x

/-! ## Maxima commute with nonnegative scaling -/

theorem lmax_const_mul {α : Type} {l : List α} (h : l ≠ []) (Q : α → K) (c : K)
    (hc : 0 ≤ c) : lmax (l.map (fun a => c * Q a)) = c * lmax (l.map Q) := by
  apply le_antisymm
  · apply lmax_le (map_ne_nil (fun a => c * Q a) h)
    intro z hz
    rcases List.mem_map.mp hz with ⟨a, ha, rfl⟩
    exact mul_le_mul_of_nonneg_left
      (le_lmax (map_ne_nil Q h) (List.mem_map.mpr ⟨a, ha, rfl⟩)) hc
  · rcases List.mem_map.mp (lmax_isMax (map_ne_nil Q h)).1 with ⟨a0, ha0, hqa0⟩
    calc
      c * lmax (l.map Q) = c * Q a0 := by rw [← hqa0]
      _ ≤ lmax (l.map (fun a => c * Q a)) :=
          le_lmax (map_ne_nil (fun a => c * Q a) h) (List.mem_map.mpr ⟨a0, ha0, rfl⟩)

/-! ## `V` sees only the mass function -/

/-- `obsMass` depends on a mass only through `.f`. -/
theorem obsMass_congr (M : SafeMDP K X Y A) (a : A) (y : Y) {m₁ m₂ : Mass K X}
    (h : m₁.f = m₂.f) : obsMass M a y m₁ = obsMass M a y m₂ := by
  funext x'
  unfold obsMass
  apply lsum_congr
  intro x hx
  rw [h]

/-- `V` depends on a mass only through its `.f` field. -/
theorem V_congr (M : SafeMDP K X Y A) :
    ∀ k {m₁ m₂ : Mass K X}, m₁.f = m₂.f → V M k m₁ = V M k m₂ := by
  intro k
  induction k with
  | zero =>
      intro m₁ m₂ h
      change total M m₁ = total M m₂
      unfold total
      rw [h]
  | succ k ih =>
      intro m₁ m₂ h
      change
        lmax (M.univA.map (fun a => lsum (M.univY.map (fun y => V M k (step M a y m₁))))) =
        lmax (M.univA.map (fun a => lsum (M.univY.map (fun y => V M k (step M a y m₂)))))
      have hfun :
          (fun a => lsum (M.univY.map (fun y => V M k (step M a y m₁)))) =
          (fun a => lsum (M.univY.map (fun y => V M k (step M a y m₂)))) := by
        funext a
        apply lsum_congr
        intro y hy
        apply ih
        exact obsMass_congr M a y h
      rw [hfun]

/-! ## Scalar multiplication of masses -/

/-- Scaling a mass by a nonnegative scalar. -/
def smul (c : K) (hc : 0 ≤ c) (m : Mass K X) : Mass K X where
  f := fun x => c * m.f x
  nonneg := by
    intro x
    exact mul_nonneg hc (m.nonneg x)

theorem total_smul (M : SafeMDP K X Y A) (c : K) (hc : 0 ≤ c) (m : Mass K X) :
    total M (smul c hc m) = c * total M m := by
  change lsum (M.univX.map (fun x => c * m.f x)) = c * lsum (M.univX.map m.f)
  rw [lsum_const_mul]

/-- Scaling commutes with the one-step posterior, at the level of `.f`. -/
theorem step_smul_f (M : SafeMDP K X Y A) (a : A) (y : Y) (c : K) (hc : 0 ≤ c)
    (m : Mass K X) :
    (step M a y (smul c hc m)).f = (smul c hc (step M a y m)).f := by
  funext x'
  change
    lsum (M.univX.map (fun x => (c * m.f x) * M.T a x x' * M.g a x x' y)) =
    c * lsum (M.univX.map (fun x => m.f x * M.T a x x' * M.g a x x' y))
  calc
    lsum (M.univX.map (fun x => (c * m.f x) * M.T a x x' * M.g a x x' y))
        = lsum (M.univX.map (fun x => c * (m.f x * M.T a x x' * M.g a x x' y))) := by
            apply lsum_congr
            intro x hx
            rw [mul_assoc c (m.f x) (M.T a x x'),
                mul_assoc c (m.f x * M.T a x x') (M.g a x x' y)]
    _ = c * lsum (M.univX.map (fun x => m.f x * M.T a x x' * M.g a x x' y)) := by
            rw [lsum_const_mul]

/-! ## (a) Positive homogeneity, and the Bayes bridge -/

/-- **`V_k` is positively homogeneous of degree one.**

This is the engine under the bridge: `V_k(c·m) = c · V_k(m)` for `c ≥ 0`. -/
theorem V_homogeneous (M : SafeMDP K X Y A) (c : K) (hc : 0 ≤ c) :
    ∀ k (m : Mass K X), V M k (smul c hc m) = c * V M k m := by
  intro k
  induction k with
  | zero =>
      intro m
      change total M (smul c hc m) = c * total M m
      exact total_smul M c hc m
  | succ k ih =>
      intro m
      change
        lmax (M.univA.map (fun a => lsum (M.univY.map (fun y => V M k (step M a y (smul c hc m)))))) =
        c * lmax (M.univA.map (fun a => lsum (M.univY.map (fun y => V M k (step M a y m)))))
      have hlist :
          M.univA.map (fun a => lsum (M.univY.map (fun y => V M k (step M a y (smul c hc m))))) =
          M.univA.map (fun a => c * lsum (M.univY.map (fun y => V M k (step M a y m)))) := by
        apply map_congr_fun
        intro a ha
        calc
          lsum (M.univY.map (fun y => V M k (step M a y (smul c hc m))))
              = lsum (M.univY.map (fun y => V M k (smul c hc (step M a y m)))) := by
                  apply lsum_congr
                  intro y hy
                  exact V_congr M k (step_smul_f M a y c hc m)
          _ = lsum (M.univY.map (fun y => c * V M k (step M a y m))) := by
                  apply lsum_congr
                  intro y hy
                  exact ih (step M a y m)
          _ = c * lsum (M.univY.map (fun y => V M k (step M a y m))) := by
                  rw [lsum_const_mul]
      rw [hlist]
      exact lmax_const_mul M.univA_ne
        (fun a => lsum (M.univY.map (fun y => V M k (step M a y m)))) c hc

/-- `V` is antitone in the horizon: longer horizons are no safer. -/
theorem V_antitone (M : SafeMDP K X Y A) {k n : Nat} (h : k ≤ n) :
    ∀ m, V M n m ≤ V M k m := by
  induction h with
  | refl =>
      intro m
      exact le_refl _
  | step h ih =>
      intro m
      exact le_trans (V_mono_succ M _ m) (ih m)

/-- A mass of total weight zero has safety value zero at every horizon. -/
theorem V_of_total_zero (M : SafeMDP K X Y A) (m : Mass K X) (hm : total M m = 0) :
    ∀ k, V M k m = 0 := by
  intro k
  apply le_antisymm
  · calc
      V M k m ≤ V M 0 m := V_antitone M (Nat.zero_le k) m
      _ = total M m := V_zero M m
      _ = 0 := hm
  · exact V_nonneg M k m

/-- The normalizing constant `ℙ(y|b,a)⁻¹` is nonnegative — including when
`ℙ(y|b,a) = 0`, where `OrdField` stipulates `0⁻¹ = 0`. -/
theorem pInv_nonneg (M : SafeMDP K X Y A) (s : Mass K X) : 0 ≤ (total M s)⁻¹ := by
  by_cases hp : total M s = 0
  · have hz : (total M s)⁻¹ = 0 := by
      calc
        (total M s)⁻¹ = (0 : K)⁻¹ := congrArg (fun t : K => t⁻¹) hp
        _ = 0 := OrdField.inv_zero
    rw [hz]
    exact le_refl 0
  · exact le_of_lt (inv_pos (lt_of_le_of_ne (total_nonneg M s) (Ne.symm hp)))

/-- **(a) The Bayes / homogeneity bridge.**

`ℙ(y|b,a) · V_k(τ(b,a,y)) = V_k(m_{a,y})`, where `ℙ(y|b,a)` is the total
mass of the unnormalized posterior `m_{a,y}` and `τ(b,a,y)` is its
normalization `ℙ(y|b,a)⁻¹ · m_{a,y}`.

The `ℙ(y|b,a) = 0` branch is the point of the unnormalized formulation: the
paper's `τ` is undefined there, so the paper silently drops the term. Here
the term is provably zero (`V_of_total_zero`) rather than absent by fiat. -/
theorem bayes_bridge (M : SafeMDP K X Y A) (a : A) (y : Y) (b : Mass K X) (k : Nat) :
    total M (step M a y b) *
        V M k (smul (total M (step M a y b))⁻¹
          (pInv_nonneg M (step M a y b)) (step M a y b)) =
      V M k (step M a y b) := by
  let s := step M a y b
  let p := total M s
  by_cases hp : p = 0
  · have hs0 : total M s = 0 := hp
    calc
      p * V M k (smul p⁻¹ (pInv_nonneg M s) s)
          = 0 * V M k (smul p⁻¹ (pInv_nonneg M s) s) :=
              congrArg (fun t => t * V M k (smul p⁻¹ (pInv_nonneg M s) s)) hp
      _ = 0 := zero_mul _
      _ = V M k s := (V_of_total_zero M s hs0 k).symm
  · calc
      p * V M k (smul p⁻¹ (pInv_nonneg M s) s) = p * (p⁻¹ * V M k s) := by
          rw [V_homogeneous M p⁻¹ (pInv_nonneg M s) k s]
      _ = (p * p⁻¹) * V M k s := by rw [← mul_assoc]
      _ = 1 * V M k s := by rw [mul_inv_cancel_field hp]
      _ = V M k s := by rw [one_mul']

/-! ## (b) The one-step equality, and `prop:chance` -/

/-- **Equality form of the one-step bound**: the surviving mass after one
step, summed over observations, is exactly `Σ_x m(x) · (row sum of T)`. -/
theorem one_step_eq (M : SafeMDP K X Y A) (a : A) (m : Mass K X) :
    lsum (M.univY.map (fun y => total M (step M a y m))) =
      lsum (M.univX.map (fun x => m.f x * lsum (M.univX.map (fun x' => M.T a x x')))) := by
  change
    lsum (M.univY.map (fun y => lsum (M.univX.map (fun x' => obsMass M a y m x')))) =
      lsum (M.univX.map (fun x => m.f x * lsum (M.univX.map (fun x' => M.T a x x'))))
  calc
    lsum (M.univY.map (fun y => lsum (M.univX.map (fun x' => obsMass M a y m x'))))
        = lsum (M.univX.map (fun x' =>
            lsum (M.univY.map (fun y => obsMass M a y m x')))) := by
              rw [lsum_lsum_comm]
    _ = lsum (M.univX.map (fun x' => lsum (M.univX.map (fun x =>
            lsum (M.univY.map (fun y => m.f x * M.T a x x' * M.g a x x' y)))))) := by
              apply lsum_congr
              intro x' hx'
              unfold obsMass
              rw [lsum_lsum_comm]
    _ = lsum (M.univX.map (fun x' =>
            lsum (M.univX.map (fun x => m.f x * M.T a x x')))) := by
              apply lsum_congr
              intro x' hx'
              apply lsum_congr
              intro x hx
              calc
                lsum (M.univY.map (fun y => m.f x * M.T a x x' * M.g a x x' y))
                    = (m.f x * M.T a x x') *
                        lsum (M.univY.map (fun y => M.g a x x' y)) := by
                          rw [lsum_const_mul]
                _ = m.f x * M.T a x x' := by rw [M.g_sum a x x', mul_one]
    _ = lsum (M.univX.map (fun x =>
            lsum (M.univX.map (fun x' => m.f x * M.T a x x')))) := by
              rw [lsum_lsum_comm]
    _ = lsum (M.univX.map (fun x =>
            m.f x * lsum (M.univX.map (fun x' => M.T a x x')))) := by
              apply lsum_congr
              intro x hx
              rw [lsum_const_mul]

/-- Row sum of `T` over the safe set; `1 - rowSum` is the paper's one-step
exit probability `p(x,a)`. -/
def rowSum (M : SafeMDP K X Y A) (a : A) (x : X) : K :=
  lsum (M.univX.map (fun x' => M.T a x x'))

/-- The paper's `Σ_x b(x) · p(x,a)`: the exit mass under action `a`. -/
def exitProb (M : SafeMDP K X Y A) (a : A) (b : Mass K X) : K :=
  lsum (M.univX.map (fun x => b.f x * (1 - rowSum M a x)))

/-- The surviving mass under action `a`. -/
def survival (M : SafeMDP K X Y A) (a : A) (b : Mass K X) : K :=
  lsum (M.univX.map (fun x => b.f x * rowSum M a x))

/-- Exit mass plus surviving mass is the total mass. -/
theorem exit_add_survival (M : SafeMDP K X Y A) (a : A) (b : Mass K X) :
    survival M a b + exitProb M a b = total M b := by
  unfold survival exitProb total rowSum
  calc
    lsum (M.univX.map (fun x => b.f x * lsum (M.univX.map (fun x' => M.T a x x')))) +
        lsum (M.univX.map (fun x =>
          b.f x * (1 - lsum (M.univX.map (fun x' => M.T a x x')))))
        = lsum (M.univX.map (fun x =>
            b.f x * lsum (M.univX.map (fun x' => M.T a x x')) +
            b.f x * (1 - lsum (M.univX.map (fun x' => M.T a x x'))))) := by
              rw [← lsum_distrib]
    _ = lsum (M.univX.map (fun x => b.f x * (
            lsum (M.univX.map (fun x' => M.T a x x')) +
            (1 - lsum (M.univX.map (fun x' => M.T a x x')))))) := by
              apply lsum_congr
              intro x hx
              rw [← left_distrib]
    _ = lsum (M.univX.map (fun x => b.f x * 1)) := by
              apply lsum_congr
              intro x hx
              congr 1
              rw [add_comm, sub_add_cancel]
    _ = lsum (M.univX.map (fun x => b.f x)) := by
              apply lsum_congr
              intro x hx
              rw [mul_one]

/-- **(b) `prop:chance`** (chance-constrained common-action obstruction).

If `b` is normalized (`b(𝒱) = 1`) and every action expends at least `δ` of
exit mass, `Σ_x b(x)·p(x,a) ≥ δ`, then `V_k(b) ≤ 1 - δ` for every `k ≥ 1`,
and the chance constraint is infeasible whenever `ε < δ`.

The paper's proof invokes `V_{k+1} ≤ V_k` as an aside; here that step is
`V_antitone`, proved in v7. -/
theorem chance_bound (M : SafeMDP K X Y A) (b : Mass K X) (δ : K)
    (hnorm : total M b = 1)
    (hδ : ∀ a, a ∈ M.univA → δ ≤ exitProb M a b) :
    ∀ k, 1 ≤ k → V M k b ≤ 1 - δ := by
  intro k hk
  have hV1 : V M 1 b ≤ 1 - δ := by
    calc
      V M 1 b = lmax (M.univA.map (fun a => lsum (M.univY.map (fun y => total M (step M a y b))))) := rfl
      _ = lmax (M.univA.map (fun a => survival M a b)) := by
            congr 1
            apply map_congr_fun
            intro a ha
            unfold survival rowSum
            exact one_step_eq M a b
      _ ≤ 1 - δ := by
            apply lmax_le (map_ne_nil (fun a => survival M a b) M.univA_ne)
            intro z hz
            rcases List.mem_map.mp hz with ⟨a, ha, rfl⟩
            apply le_sub_of_add_le_of
            calc
              survival M a b + δ ≤ survival M a b + exitProb M a b :=
                  add_le_add_left (hδ a ha) (survival M a b)
              _ = total M b := exit_add_survival M a b
              _ = 1 := hnorm
  exact le_trans (V_antitone M hk b) hV1

end Formalizations.POMDP
