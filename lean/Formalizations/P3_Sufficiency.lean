/-
  Formalizations.P3_Sufficiency
  =============================

  P3 (`paper2_probabilistic_sufficiency_v11.tex`) — batch 2 of the
  formalizable results. Closes, over the `OrdField` interface:

    thm:recursion     the belief-state value recursion over a declared,
                      class-admissible action set `A(Π)`, in the paper's
                      *normalized* (Bayes) form;
    prop:pathdeficit  `Δ₁(b) = Σ_x b(x)·p_x` at the one-step horizon;
    prop:deficit (i)  chance-constrained common action: `Δ_k(b) ≥ δ`;
    prop:deficit (iii) monotone deficit: the deficit is non-decreasing
                      in the horizon.

  All four reuse the unnormalized belief machinery of
  `P1_BeliefSafety` / `P1_BeliefSafety_Value` (v7/v8) and the homogeneity
  bridge `bayes_bridge`, which is what converts the unnormalized recursion
  into the paper's normalized one.

  ## `thm:recursion`

  The paper writes

      V^Π_{k+1}(b) = max_{a ∈ A(Π)} Σ_y ℙ(y|b,a) · V^Π_k(τ(b,a,y))

  with `A(Π)` the class-admissible action set. In `VAdm` the max is taken
  over `univA.filter adm`, which is what `A(Π)` is. Two points of care:

  * The paper's form is *normalized*; ours is unnormalized. `bayes_bridge`
    (v8) is exactly the conversion, so `recursion_normalized` states the
    paper's formula verbatim and derives it.
  * The bare recursion is a definition, hence content-free on its own — the
    same trap flagged in v7 for `thm:pomdp`. The content here is
    `recursion_normalized` (the conversion to the Bayes form) plus
    `VAdm_mono_adm` (monotonicity in the declared class), which is the
    concrete recursion-level form of `thm:lattice` (i).

  `VAdm` requires the admissible set to be nonempty (`hne`); without it the
  maximum is not defined and the recursion is meaningless. The papers do
  not state this, but every class they use satisfies it.

  ## Not closed here

  `prop:degen`, `thm:support` and `prop:deficit` (ii) need deterministic
  kernels with a set-valued `Post` operator and adversarial disturbance
  readings — separate machinery (next batch). `prop:noisyprobe` is a closed
  form on the declining instance.
-/

import Formalizations.P1_BeliefSafety_Value

namespace Formalizations.P3

open Formalizations
open Formalizations.POMDP

variable {K : Type} [OrdField K]
variable {X Y A : Type}

/-! ## Helpers -/

/-- Forward direction of subtraction: `a ≤ b - c` from `a + c ≤ b`. -/
theorem add_le_of_le_sub {a b c : K} (h : a ≤ b - c) : a + c ≤ b := by
  have h2 : a + c ≤ (b - c) + c := add_le_add_right h c
  simpa [sub_add_cancel] using h2

/-- A filtered list is nonempty if some element passes the predicate. -/
theorem filter_ne_nil_of_exists {α : Type} (p : α → Prop) [DecidablePred p]
    {l : List α} (h : ∃ a, a ∈ l ∧ p a) : l.filter p ≠ [] := by
  rcases h with ⟨a, ha, hpa⟩
  intro hnil
  have : a ∈ l.filter p := by simp [List.mem_filter, ha, hpa]
  simp [hnil] at this

/-- Maxima grow with the list: every element of `l₁` in `l₂` ⟹ max l₁ ≤ max l₂. -/
theorem lmax_le_lmax_of_subset {l₁ l₂ : List K} (h1 : l₁ ≠ [])
    (hsub : ∀ x, x ∈ l₁ → x ∈ l₂) : lmax l₁ ≤ lmax l₂ := by
  obtain ⟨x, hx⟩ : ∃ x, x ∈ l₁ := by
    cases l₁ with
    | nil => exact absurd rfl h1
    | cons a as => exact ⟨a, by simp⟩
  have h2 : l₂ ≠ [] := by
    intro hn
    have : x ∈ ([] : List K) := by simpa [hn] using hsub x hx
    simp at this
  apply lmax_le h1
  intro y hy
  exact le_lmax h2 (hsub y hy)

/-! ## The class-admissible action set and the restricted value -/

/-- `A(Π)`: the class-admissible actions, as a filter of the finite
universe. -/
def actSet (M : SafeMDP K X Y A) (adm : A → Prop) [DecidablePred adm] : List A :=
  M.univA.filter adm

/-- The value of a *declared class*: the belief recursion with the max
ranging over `A(Π)` only. `hne` records that `A(Π)` is inhabited. -/
noncomputable def VAdm (M : SafeMDP K X Y A) (adm : A → Prop) [DecidablePred adm]
    (hne : actSet M adm ≠ []) : Nat → Mass K X → K
  | 0, m => total M m
  | k + 1, m =>
      lmax ((actSet M adm).map (fun a =>
        lsum (M.univY.map (fun y => VAdm M adm hne k (step M a y m)))))

/-- `VAdm` sees only the mass function. -/
theorem VAdm_congr (M : SafeMDP K X Y A) (adm : A → Prop) [DecidablePred adm]
    (hne : actSet M adm ≠ []) :
    ∀ k {m₁ m₂ : Mass K X}, m₁.f = m₂.f → VAdm M adm hne k m₁ = VAdm M adm hne k m₂ := by
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
        lmax ((actSet M adm).map (fun a =>
          lsum (M.univY.map (fun y => VAdm M adm hne k (step M a y m₁))))) =
        lmax ((actSet M adm).map (fun a =>
          lsum (M.univY.map (fun y => VAdm M adm hne k (step M a y m₂)))))
      have hfun :
          (fun a => lsum (M.univY.map (fun y => VAdm M adm hne k (step M a y m₁)))) =
          (fun a => lsum (M.univY.map (fun y => VAdm M adm hne k (step M a y m₂)))) := by
        funext a
        apply lsum_congr
        intro y hy
        apply ih
        exact obsMass_congr M a y h
      rw [hfun]

/-- `V^Π` is positively homogeneous — the engine under the bridge. -/
theorem VAdm_homogeneous (M : SafeMDP K X Y A) (adm : A → Prop) [DecidablePred adm]
    (hne : actSet M adm ≠ []) (c : K) (hc : 0 ≤ c) :
    ∀ k (m : Mass K X), VAdm M adm hne k (smul c hc m) = c * VAdm M adm hne k m := by
  intro k
  induction k with
  | zero =>
      intro m
      change total M (smul c hc m) = c * total M m
      exact total_smul M c hc m
  | succ k ih =>
      intro m
      change
        lmax ((actSet M adm).map (fun a =>
          lsum (M.univY.map (fun y => VAdm M adm hne k (step M a y (smul c hc m)))))) =
        c * lmax ((actSet M adm).map (fun a =>
          lsum (M.univY.map (fun y => VAdm M adm hne k (step M a y m)))))
      have hlist :
          (actSet M adm).map (fun a =>
            lsum (M.univY.map (fun y => VAdm M adm hne k (step M a y (smul c hc m))))) =
          (actSet M adm).map (fun a =>
            c * lsum (M.univY.map (fun y => VAdm M adm hne k (step M a y m)))) := by
        apply map_congr_fun
        intro a ha
        calc
          lsum (M.univY.map (fun y => VAdm M adm hne k (step M a y (smul c hc m))))
              = lsum (M.univY.map (fun y => VAdm M adm hne k (smul c hc (step M a y m)))) := by
                  apply lsum_congr
                  intro y hy
                  exact VAdm_congr M adm hne k (step_smul_f M a y c hc m)
          _ = lsum (M.univY.map (fun y => c * VAdm M adm hne k (step M a y m))) := by
                  apply lsum_congr
                  intro y hy
                  exact ih (step M a y m)
          _ = c * lsum (M.univY.map (fun y => VAdm M adm hne k (step M a y m))) := by
                  rw [lsum_const_mul]
      rw [hlist]
      exact lmax_const_mul hne
        (fun a => lsum (M.univY.map (fun y => VAdm M adm hne k (step M a y m)))) c hc

/-- `V^Π` is nonnegative. -/
theorem VAdm_nonneg (M : SafeMDP K X Y A) (adm : A → Prop) [DecidablePred adm]
    (hne : actSet M adm ≠ []) :
    ∀ k m, 0 ≤ VAdm M adm hne k m := by
  intro k
  induction k with
  | zero =>
      intro m
      change 0 ≤ total M m
      exact total_nonneg M m
  | succ k ih =>
      intro m
      let Q : A → K := fun a =>
        lsum (M.univY.map (fun y => VAdm M adm hne k (step M a y m)))
      change 0 ≤ lmax ((actSet M adm).map Q)
      have hneQ : (actSet M adm).map Q ≠ [] := map_ne_nil Q hne
      rcases List.mem_map.mp (lmax_isMax hneQ).1 with ⟨a, ha, hqa⟩
      rw [← hqa]
      unfold Q
      apply lsum_nonneg_map
      intro y
      exact ih (step M a y m)

/-- `V^Π` is antitone in the horizon — more steps cannot raise the value of
a declared class either. -/
theorem VAdm_mono_succ (M : SafeMDP K X Y A) (adm : A → Prop) [DecidablePred adm]
    (hne : actSet M adm ≠ []) :
    ∀ k m, VAdm M adm hne (k + 1) m ≤ VAdm M adm hne k m := by
  intro k
  induction k with
  | zero =>
      intro m
      change lmax ((actSet M adm).map (fun a =>
        lsum (M.univY.map (fun y => total M (step M a y m))))) ≤ total M m
      apply lmax_le (map_ne_nil
        (fun a => lsum (M.univY.map (fun y => total M (step M a y m)))) hne)
      intro z hz
      rcases List.mem_map.mp hz with ⟨a, ha, rfl⟩
      exact one_step_le_total M a m
  | succ k ih =>
      intro m
      let Q₁ : A → K := fun a =>
        lsum (M.univY.map (fun y => VAdm M adm hne (k + 1) (step M a y m)))
      let Q₀ : A → K := fun a =>
        lsum (M.univY.map (fun y => VAdm M adm hne k (step M a y m)))
      change lmax ((actSet M adm).map Q₁) ≤ lmax ((actSet M adm).map Q₀)
      apply lmax_mono hne
      intro a ha
      apply lsum_le_lsum
      intro y hy
      exact ih (step M a y m)

theorem VAdm_antitone (M : SafeMDP K X Y A) (adm : A → Prop) [DecidablePred adm]
    (hne : actSet M adm ≠ []) {k n : Nat} (h : k ≤ n) :
    ∀ m, VAdm M adm hne n m ≤ VAdm M adm hne k m := by
  induction h with
  | refl => intro m; exact le_refl _
  | step h ih => intro m; exact le_trans (VAdm_mono_succ M adm hne _ m) (ih m)

/-- The Bayes bridge for `V^Π`, including the `ℙ(y|b,a) = 0` branch. -/
theorem VAdm_bayes_bridge (M : SafeMDP K X Y A) (adm : A → Prop) [DecidablePred adm]
    (hne : actSet M adm ≠ []) (a : A) (y : Y) (b : Mass K X) (k : Nat) :
    total M (step M a y b) *
        VAdm M adm hne k (smul (total M (step M a y b))⁻¹
          (pInv_nonneg M (step M a y b)) (step M a y b)) =
      VAdm M adm hne k (step M a y b) := by
  let s := step M a y b
  let p := total M s
  by_cases hp : p = 0
  · have hs0 : total M s = 0 := hp
    calc
      p * VAdm M adm hne k (smul p⁻¹ (pInv_nonneg M s) s)
          = 0 * VAdm M adm hne k (smul p⁻¹ (pInv_nonneg M s) s) :=
              congrArg (fun t => t * VAdm M adm hne k (smul p⁻¹ (pInv_nonneg M s) s)) hp
      _ = 0 := zero_mul _
      _ = VAdm M adm hne k s := by
            apply (le_antisymm ?_ ?_)
            · change 0 ≤ VAdm M adm hne k s
              exact VAdm_nonneg M adm hne k s
            · have hv : VAdm M adm hne k s ≤ VAdm M adm hne 0 s :=
                VAdm_antitone M adm hne (Nat.zero_le k) s
              change VAdm M adm hne k s ≤ 0
              calc
                VAdm M adm hne k s ≤ VAdm M adm hne 0 s := hv
                _ = total M s := rfl
                _ = 0 := hs0
  · calc
      p * VAdm M adm hne k (smul p⁻¹ (pInv_nonneg M s) s)
          = p * (p⁻¹ * VAdm M adm hne k s) := by
              rw [VAdm_homogeneous M adm hne p⁻¹ (pInv_nonneg M s) k s]
      _ = (p * p⁻¹) * VAdm M adm hne k s := by rw [← mul_assoc]
      _ = 1 * VAdm M adm hne k s := by rw [mul_inv_cancel_field hp]
      _ = VAdm M adm hne k s := by rw [one_mul']

/-- **`thm:recursion`** — the class-restricted recursion in the paper's
normalized (Bayes) form. -/
theorem recursion_normalized (M : SafeMDP K X Y A) (adm : A → Prop)
    [DecidablePred adm] (hne : actSet M adm ≠ []) (k : Nat) (m : Mass K X) :
    VAdm M adm hne (k + 1) m =
      lmax ((actSet M adm).map (fun a =>
        lsum (M.univY.map (fun y =>
          total M (step M a y m) *
            VAdm M adm hne k (smul (total M (step M a y m))⁻¹
              (pInv_nonneg M (step M a y m)) (step M a y m)))))) := by
  change
    lmax ((actSet M adm).map (fun a =>
      lsum (M.univY.map (fun y => VAdm M adm hne k (step M a y m))))) =
    lmax ((actSet M adm).map (fun a =>
      lsum (M.univY.map (fun y =>
        total M (step M a y m) *
          VAdm M adm hne k (smul (total M (step M a y m))⁻¹
            (pInv_nonneg M (step M a y m)) (step M a y m))))))
  congr 1
  apply map_congr_fun
  intro a ha
  apply lsum_congr
  intro y hy
  exact (VAdm_bayes_bridge M adm hne a y m k).symm

/-! ## `thm:lattice` (i), concrete recursion form -/

/-- Enlarging the declared class cannot lower the value: the recursion-level
form of `class_monotone` (v9), proved for `VAdm` directly. -/
theorem VAdm_mono_adm (M : SafeMDP K X Y A) (adm adm' : A → Prop)
    [DecidablePred adm] [DecidablePred adm']
    (hne : actSet M adm ≠ []) (hne' : actSet M adm' ≠ [])
    (hsub : ∀ a, adm a → adm' a) :
    ∀ k m, VAdm M adm hne k m ≤ VAdm M adm' hne' k m := by
  intro k
  induction k with
  | zero =>
      intro m
      exact le_refl _
  | succ k ih =>
      intro m
      let Q₁ : A → K := fun a => lsum (M.univY.map (fun y => VAdm M adm hne k (step M a y m)))
      let Q₂ : A → K := fun a => lsum (M.univY.map (fun y => VAdm M adm' hne' k (step M a y m)))
      change lmax ((actSet M adm).map Q₁) ≤ lmax ((actSet M adm').map Q₂)
      have hQ : ∀ a, a ∈ actSet M adm → Q₁ a ≤ Q₂ a := by
        intro a ha
        apply lsum_le_lsum
        intro y hy
        exact ih (step M a y m)
      have hstep₁ : lmax ((actSet M adm).map Q₁) ≤ lmax ((actSet M adm).map Q₂) :=
        lmax_mono hne Q₁ Q₂ hQ
      have hstep₂ : lmax ((actSet M adm).map Q₂) ≤ lmax ((actSet M adm').map Q₂) := by
        apply lmax_le_lmax_of_subset (map_ne_nil Q₂ hne)
        intro z hz
        rcases List.mem_map.mp hz with ⟨a, ha, rfl⟩
        have ha' : a ∈ actSet M adm' := by
          simp [actSet, List.mem_filter] at ha ⊢
          exact ⟨ha.1, hsub a ha.2⟩
        exact List.mem_map.mpr ⟨a, ha', rfl⟩
      exact le_trans hstep₁ hstep₂

/-! ## `prop:pathdeficit` -/

/-- The deficit `Δ_k(b) = 1 - V_k(b)`. -/
noncomputable def deficit (M : SafeMDP K X Y A) (k : Nat) (b : Mass K X) : K := 1 - V M k b

/-- **`prop:pathdeficit`** — at the one-step horizon under a single
admissible action, the deficit is exactly the prior mass weighted by the
fatal-reading probabilities.

The paper writes `Σ_x b(x)·p_x` with `p_x = ℙ(a(y') unsafe at x | x)`; that
is `exitProb`, and the identity is `exit_add_survival` plus normalization.
Note this is an *identity*, not a bound — and the paper is careful to say
the min-mass bound is the special case `p_x ≡ 1` and is not universal. -/
theorem path_deficit (M : SafeMDP K X Y A) (a : A) (b : Mass K X)
    (hnorm : total M b = 1) :
    1 - lsum (M.univY.map (fun y => total M (step M a y b))) = exitProb M a b := by
  rw [one_step_eq M a b]
  change 1 - survival M a b = exitProb M a b
  have hs : survival M a b + exitProb M a b = 1 := by
    calc
      survival M a b + exitProb M a b = total M b := exit_add_survival M a b
      _ = 1 := hnorm
  calc
    1 - survival M a b = (survival M a b + exitProb M a b) - survival M a b := by rw [hs]
    _ = exitProb M a b := by rw [add_comm, add_sub_cancel]

/-! ## `prop:deficit` -/

/-- **`prop:deficit` (i)** — chance-constrained common action: if every
action expends at least `δ` of exit mass then the deficit is at least `δ`
at every horizon `k ≥ 1`.

This is `chance_bound` (v8, which proved the same statement as
`prop:chance`) read as a statement about `Δ` rather than `V`. -/
theorem deficit_chance (M : SafeMDP K X Y A) (b : Mass K X) (δ : K)
    (hnorm : total M b = 1)
    (hδ : ∀ a, a ∈ M.univA → δ ≤ exitProb M a b) :
    ∀ k, 1 ≤ k → δ ≤ deficit M k b := by
  intro k hk
  unfold deficit
  apply le_sub_of_add_le_of
  rw [add_comm]
  exact add_le_of_le_sub (chance_bound M b δ hnorm hδ k hk)

/-- **`prop:deficit` (iii)** — the deficit is non-decreasing in the horizon.
Directly from `V_mono_succ` (v7), which is the same fact. -/
theorem deficit_mono_succ (M : SafeMDP K X Y A) (k : Nat) (m : Mass K X) :
    deficit M k m ≤ deficit M (k + 1) m := by
  unfold deficit
  apply le_sub_of_add_le_of
  calc
    (1 - V M k m) + V M (k + 1) m ≤ (1 - V M k m) + V M k m :=
        add_le_add_left (V_mono_succ M k m) (1 - V M k m)
    _ = 1 := by rw [sub_add_cancel]

/-- The deficit is non-decreasing across any two horizons. -/
theorem deficit_mono (M : SafeMDP K X Y A) {k n : Nat} (h : k ≤ n) (m : Mass K X) :
    deficit M k m ≤ deficit M n m := by
  induction h with
  | refl => exact le_refl _
  | step h ih => exact le_trans ih (deficit_mono_succ M _ m)

end Formalizations.P3
