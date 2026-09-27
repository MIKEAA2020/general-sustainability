/-
  Formalizations.P3_Deterministic
  ===============================

  P3 (`paper2_probabilistic_sufficiency_v11.tex`) — the **deterministic
  robust** regime. Closes:

    prop:degen        the survived-mass formula and its consequence
                      "a jointly surviving blind sequence ⟹ V_k(b) = 1";
    prop:deficit (ii) the degenerate minimal-mass bound: if the support
                      admits no jointly surviving declared sequence, then
                      Δ_k(b) ≥ min_{x ∈ supp b} b(x);
    thm:support       the min-mass consequence
                      1 - V_k(b) ≥ min_{x ∈ supp(b)} b(x).

  ## What is modelled

  `DetMDP` is the deterministic degeneration: `x⁺ = F(x,a,d)` with the
  disturbance `d` drawn from a finite support `univD x a` and read
  **adversarially** (the robust operator) — survival under a blind action
  sequence means survival under *every* disturbance path, which is the
  paper's "the disturbance be read adversarially within its support".

  A blind sequence is a finite **action tuple** (`List A`), not an infinite
  `Nat → A`: at horizon `k` only the first `k` actions matter, and `A` is
  finite, so the declared sequential-blind class `Π_B` at horizon `k` is
  exactly `tuples M k` — genuinely finite. That makes the maximum an
  ordinary `lmax` rather than a sup over an infinite set, which is what
  keeps this inside `OrdField`.

  ## Honest scope

  * The survived-mass formula appears here as the **definition** of `VR`;
    the content is the two consequences proved below, not the formula.
    (Stating the formula as a theorem about a separately defined value
    would be the restatement trap flagged in v7.)
  * `thm:support`'s **support identity**
    `supp(b⁺(·|a,y)) = Post(supp b, a, y)` is **not** proved: it needs
    "a finite sum of nonnegative terms is positive iff some term is",
    i.e. a strict-positivity lemma for `lsum`, plus a disturbance
    weighting to define the posterior mass at all. Only its min-mass
    consequence is closed here. Flagged rather than faked.
  * `prop:noisyprobe` is a closed form on the declining instance and is
    not attempted.
-/

import Formalizations.P3_Sufficiency

namespace Formalizations.P3

open Formalizations
open Formalizations.POMDP

variable {K : Type} [OrdField K]
variable {X A D Y : Type}

/-- Deterministic dynamics with a finite disturbance support, a
deterministic observation map, and a safe set `𝒱`. -/
structure DetMDP (K : Type) [OrdField K] (X A D Y : Type) where
  univX : List X
  univX_nodup : univX.Nodup
  univA : List A
  univA_ne : univA ≠ []
  univD : X → A → List D
  univD_ne : ∀ x a, univD x a ≠ []
  F : X → A → D → X
  obs : X → A → X → Y
  safe : X → Bool

/-! ## Helpers -/

theorem exists_mem_of_ne_nil {α : Type} {l : List α} (h : l ≠ []) : ∃ a, a ∈ l := by
  cases l with
  | nil => exact absurd rfl h
  | cons a as => exact ⟨a, by simp⟩

theorem ne_nil_of_exists_mem {α : Type} {l : List α} (h : ∃ a, a ∈ l) : l ≠ [] := by
  intro hn
  rcases h with ⟨a, ha⟩
  simp [hn] at ha

/-- Indicators are at most `1`. -/
theorem ind_le_one (g : X → Bool) (x : X) : ind g x ≤ (1 : K) := by
  unfold ind
  cases hg : g x
  · simp
    exact zero_le_one'
  · simp
    exact le_refl 1

/-- Scaling by an indicator cannot increase a nonnegative weight. -/
theorem mul_ind_le (f : X → K) (x : X) (hf : 0 ≤ f x) (g : X → Bool) :
    f x * ind g x ≤ f x := by
  calc
    f x * ind g x ≤ f x * 1 := mul_le_mul_of_nonneg_left (ind_le_one g x) hf
    _ = f x := by rw [mul_one]

/-- Subtraction is antitone in the subtrahend. -/
theorem sub_le_sub_left_of_le {a b c : K} (h : a ≤ b) : c - b ≤ c - a := by
  apply le_sub_of_add_le_of
  calc
    (c - b) + a ≤ (c - b) + b := add_le_add_left h (c - b)
    _ = c := by rw [sub_add_cancel]

/-- **The split lemma.** If `g` is false at `x0 ∈ l` (and `l` has no
duplicates), the indicator-weighted sum plus the bare weight at `x0` is at
most the unweighted total: the mass on a dead branch is lost. -/
theorem lsum_ind_add_le {l : List X} (hnodup : l.Nodup) (f : X → K)
    (hf : ∀ x, x ∈ l → 0 ≤ f x) (g : X → Bool)
    (x0 : X) (hx0 : x0 ∈ l) (hg0 : g x0 = false) :
    lsum (l.map (fun x => f x * ind g x)) + f x0 ≤ lsum (l.map f) := by
  induction l with
  | nil =>
      simp at hx0
  | cons y ys ih =>
      rw [List.nodup_cons] at hnodup
      rcases hnodup with ⟨hynot, hnodupys⟩
      simp only [List.map_cons, lsum_cons]
      by_cases hy0 : y = x0
      · subst y
        have hg0y : ind g x0 = (0 : K) := by simp [ind, hg0]
        rw [hg0y, mul_zero]
        have hle : lsum (ys.map (fun x => f x * ind g x)) ≤ lsum (ys.map f) := by
          apply lsum_le_lsum
          intro x hx
          exact mul_ind_le f x (hf x (by simp [hx])) g
        calc
          (0 + lsum (ys.map (fun x => f x * ind g x))) + f x0
              = lsum (ys.map (fun x => f x * ind g x)) + f x0 := by simp
          _ ≤ lsum (ys.map f) + f x0 := add_le_add_right hle (f x0)
          _ = f x0 + lsum (ys.map f) := by rw [add_comm]
      · have hx0ys : x0 ∈ ys := by
          simp only [List.mem_cons] at hx0
          rcases hx0 with hxy | hxys
          · exact absurd hxy.symm hy0
          · exact hxys
        have hle_head : f y * ind g y ≤ f y := mul_ind_le f y (hf y (by simp)) g
        have ih' := ih hnodupys (fun x hx => hf x (by simp [hx])) hx0ys
        have hA :
            f y * ind g y + (lsum (ys.map (fun x => f x * ind g x)) + f x0) ≤
              f y * ind g y + lsum (ys.map f) :=
          add_le_add_left ih' (f y * ind g y)
        have hB : f y * ind g y + lsum (ys.map f) ≤ f y + lsum (ys.map f) :=
          add_le_add_right hle_head (lsum (ys.map f))
        calc
          (f y * ind g y + lsum (ys.map (fun x => f x * ind g x))) + f x0
              = f y * ind g y + (lsum (ys.map (fun x => f x * ind g x)) + f x0) := by
                  rw [add_assoc]
          _ ≤ f y + lsum (ys.map f) := le_trans hA hB

/-! ## Survival under a blind action tuple -/

/-- `survT M t x`: `x` survives the `|t|`-step blind sequence `t`, i.e.
every disturbance path driven by `t` stays in `𝒱`. Adversarial reading of
the disturbance is exactly the `all` over `univD`. -/
def survT (M : DetMDP K X A D Y) : List A → X → Bool
  | [], x => M.safe x
  | a :: t, x =>
      M.safe x && (M.univD x a).all (fun d => survT M t (M.F x a d))

/-- The declared sequential-blind class at horizon `k`: every action tuple
of length `k`. Finite because `A` is finite. -/
def tuplesAux (M : DetMDP K X A D Y) : List (List A) → List (List A)
  | [] => []
  | t :: ts => M.univA.map (fun a => a :: t) ++ tuplesAux M ts

def tuples (M : DetMDP K X A D Y) : Nat → List (List A)
  | 0 => [[]]
  | k + 1 => tuplesAux M (tuples M k)

theorem tuplesAux_ne (M : DetMDP K X A D Y) (l : List (List A)) (hl : l ≠ []) :
    tuplesAux M l ≠ [] := by
  induction l with
  | nil => exact absurd rfl hl
  | cons t ts ih =>
      apply ne_nil_of_exists_mem
      rcases exists_mem_of_ne_nil M.univA_ne with ⟨a, ha⟩
      refine ⟨a :: t, ?_⟩
      simp [tuplesAux]
      exact Or.inl ha

theorem tuples_ne (M : DetMDP K X A D Y) : ∀ k, tuples M k ≠ [] := by
  intro k
  induction k with
  | zero =>
      simp [tuples]
  | succ k ih =>
      exact tuplesAux_ne M (tuples M k) ih

/-- Survived mass under the tuple `t`: the prior mass of the surviving
branches. This is the inner sum of `prop:degen`. -/
def smass (M : DetMDP K X A D Y) (t : List A) (b : Mass K X) : K :=
  lsum (M.univX.map (fun x => b.f x * ind (survT M t) x))

def totalD (M : DetMDP K X A D Y) (b : Mass K X) : K := lsum (M.univX.map b.f)

/-- **The degenerated value**: `V_k(b) = max_{t ∈ Π_B} Σ_x b(x)·1[x
survives t]` — `prop:degen`'s survived-mass formula, as a definition. -/
noncomputable def VR (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) : K :=
  lmax ((tuples M k).map (fun t => smass M t b))

/-! ## Consequences -/

/-- Survived mass never exceeds the total mass. -/
theorem smass_le_totalD (M : DetMDP K X A D Y) (t : List A) (b : Mass K X) :
    smass M t b ≤ totalD M b := by
  unfold smass totalD
  apply lsum_le_lsum
  intro x hx
  exact mul_ind_le b.f x (b.nonneg x) (survT M t)

theorem VR_le_totalD (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) :
    VR M k b ≤ totalD M b := by
  unfold VR
  apply lmax_le (map_ne_nil (fun t => smass M t b) (tuples_ne M k))
  intro z hz
  rcases List.mem_map.mp hz with ⟨t, ht, rfl⟩
  exact smass_le_totalD M t b

/-- **`prop:degen`, consequence 1.** If the support carries a jointly
surviving blind sequence then `V_k(b) = b(𝒱)` — hence `V_k(b) = 1` for a
normalized belief. -/
theorem VR_eq_total_of_jointly_surviving (M : DetMDP K X A D Y) (k : Nat)
    (b : Mass K X)
    (ht : ∃ t, t ∈ tuples M k ∧
      ∀ x, x ∈ M.univX → b.f x ≠ 0 → survT M t x = true) :
    VR M k b = totalD M b := by
  rcases ht with ⟨t0, ht0, hsurv⟩
  apply le_antisymm
  · exact VR_le_totalD M k b
  · calc
      totalD M b = smass M t0 b := by
            unfold totalD smass
            apply lsum_congr
            intro x hx
            by_cases hb : b.f x = 0
            · simp [hb]
            · have hs : survT M t0 x = true := hsurv x hx hb
              simp [ind, hs]
      _ ≤ VR M k b := by
            unfold VR
            exact le_lmax (map_ne_nil (fun t => smass M t b) (tuples_ne M k))
              (List.mem_map.mpr ⟨t0, ht0, rfl⟩)

/-- **The min-mass bound** — `prop:deficit` (ii) and `thm:support`'s
consequence. If *every* declared sequence loses some branch of positive
mass, then the deficit is at least the smallest branch mass. -/
theorem min_mass_bound (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) (mn : K)
    (hnorm : totalD M b = 1)
    (hmn : ∀ x, x ∈ M.univX → mn ≤ b.f x)
    (hlost : ∀ t, t ∈ tuples M k →
      ∃ x, x ∈ M.univX ∧ b.f x ≠ 0 ∧ survT M t x = false) :
    mn ≤ 1 - VR M k b := by
  apply le_sub_of_add_le_of
  rw [add_comm]
  have hVR : VR M k b ≤ 1 - mn := by
    unfold VR
    apply lmax_le (map_ne_nil (fun t => smass M t b) (tuples_ne M k))
    intro z hz
    rcases List.mem_map.mp hz with ⟨t, ht, rfl⟩
    rcases hlost t ht with ⟨x0, hx0, hb0, hdead⟩
    have hsplit : smass M t b + b.f x0 ≤ totalD M b := by
      unfold smass totalD
      exact lsum_ind_add_le M.univX_nodup b.f (fun x hx => b.nonneg x)
        (survT M t) x0 hx0 hdead
    have hle1 : smass M t b ≤ 1 - b.f x0 := by
      apply le_sub_of_add_le_of
      calc
        smass M t b + b.f x0 ≤ totalD M b := hsplit
        _ = 1 := hnorm
    exact le_trans hle1 (sub_le_sub_left_of_le (hmn x0 hx0))
  exact add_le_of_le_sub hVR

end Formalizations.P3
