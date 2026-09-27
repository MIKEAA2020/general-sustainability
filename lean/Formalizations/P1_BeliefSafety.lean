/-
  Formalizations.P1_BeliefSafety
  ==============================

  Lean formalization of the reachable content of

    **Theorem `thm:pomdp`** (belief-state safety value),
    `paper2_obstruction_calculus_v55_Automatica_routes.tex` §10.

  The paper states, for finite `X, A, D, Y` with an absorbing unsafe state
  `⊥`, a stochastic transition `T` and observation likelihood `g`:

      V_0(b) = b(𝒱)
      V_{k+1}(b) = max_{a ∈ A} Σ_{y ∈ Y} ℙ(y | b, a) · V_k(τ(b, a, y))

  with `τ` the Bayes update.

  ### Expressibility

  This needs only finite sums and a maximum over a finite action set — no
  topology, no completeness, no measure beyond finite additivity — so it is
  expressible over `OrdField K`, unlike `thm:exit` / `thm:delayed` /
  `thm:static-complete` (see `lean_audit_v6.md`).

  ### The one modelling decision

  Bayes normalization `τ` divides by `ℙ(y | b, a)`, which is zero on
  impossible observations. Rather than carry a division-by-zero case
  everywhere, this module works with **unnormalized (sub-probability)
  masses over the safe set** and the equivalent unnormalized recursion

      V_{k+1}(m) = max_a Σ_y V_k(m_{a,y}),
      m_{a,y}(x') = Σ_x m(x)·T(a,x,x')·g(a,x,x',y)

  This is the standard positive-homogeneous extension of the paper's
  recursion: `m_{a,y}` has total mass `ℙ(y | m, a)`, so
  `V_k(m_{a,y}) = ℙ(y | m, a) · V_k(τ(m, a, y))` and the two recursions
  agree on normalized beliefs. The bridge (positive homogeneity of `V_k`)
  is NOT proved here — it is the remaining piece.

  Mass on the absorbing state is not tracked: exiting is modelled by
  `Σ_{x'} T(a,x,x') ≤ 1`, so the deficit `1 - Σ_{x'} T(a,x,x')` is exactly
  the paper's one-step exit probability `p(x,a)`.

  ### What is proved

    `V_zero`        V_0(m) is the total safe mass — the paper's `b(𝒱)`.
    `V_mono_succ`   V_{k+1}(m) ≤ V_k(m): more steps cannot raise the
                    survival probability. This is the fact the paper's own
                    proof of `prop:chance` leans on.
    `V_nonneg`      0 ≤ V_k(m).

  Everything is interface-level over `OrdField K`.
-/

import Formalizations.Prelude

namespace Formalizations.POMDP

variable {K : Type} [OrdField K]

/-! ## Maxima of finite lists

`Prelude` carries maxima as hypotheses (`IsMax`) rather than constructing
them, to keep the layer choice-free. The Bellman recursion needs an actual
maximum *function*, so existence is proved here once and the maximum is
selected. -/

theorem list_max_exists : ∀ (l : List K), l ≠ [] → ∃ m, IsMax m l := by
  intro l
  induction l with
  | nil =>
      intro h; exact absurd rfl h
  | cons x xs ih =>
      intro hne
      cases xs with
      | nil =>
          refine ⟨x, ?_⟩
          constructor
          · simp
          · intro y hy
            have hy' : y = x := by simpa using hy
            rw [hy']
            exact le_refl x
      | cons y ys =>
          rcases ih (by simp) with ⟨m, hm⟩
          cases le_total x m with
          | inl hxm =>
              refine ⟨m, ?_⟩
              constructor
              · exact List.mem_cons_of_mem x hm.1
              · intro z hz
                have hz' : z = x ∨ z ∈ y :: ys := by simpa using hz
                rcases hz' with hz' | hz'
                · rw [hz']; exact hxm
                · exact hm.2 z hz'
          | inr hmx =>
              refine ⟨x, ?_⟩
              constructor
              · simp
              · intro z hz
                have hz' : z = x ∨ z ∈ y :: ys := by simpa using hz
                rcases hz' with hz' | hz'
                · rw [hz']; exact le_refl x
                · exact le_trans (hm.2 z hz') hmx

noncomputable section

/-- Maximum of a finite list (`0` on the empty list). -/
def lmax (l : List K) : K :=
  if h : l = [] then 0 else Classical.choose (list_max_exists l h)

theorem lmax_isMax {l : List K} (h : l ≠ []) : IsMax (lmax l) l := by
  simpa [lmax, h] using Classical.choose_spec (list_max_exists l h)

/-- Every element is below the maximum. -/
theorem le_lmax {l : List K} (h : l ≠ []) {x : K} (hx : x ∈ l) : x ≤ lmax l :=
  (lmax_isMax h).ge hx

/-- To bound the maximum, bound every element. -/
theorem lmax_le {l : List K} (h : l ≠ []) {c : K} (hc : ∀ x, x ∈ l → x ≤ c) :
    lmax l ≤ c :=
  (lmax_isMax h).le hc

theorem map_ne_nil {α β : Type} {l : List α} (f : α → β) (h : l ≠ []) :
    l.map f ≠ [] := by
  intro hm
  apply h
  cases l with
  | nil => rfl
  | cons a as => simp at hm

/-- Maxima are monotone in the values. -/
theorem lmax_mono {α : Type} {l : List α} (h : l ≠ []) (Q₁ Q₂ : α → K)
    (hle : ∀ a, a ∈ l → Q₁ a ≤ Q₂ a) :
    lmax (l.map Q₁) ≤ lmax (l.map Q₂) := by
  apply lmax_le (map_ne_nil Q₁ h)
  intro z hz
  rcases List.mem_map.mp hz with ⟨a, ha, rfl⟩
  exact le_trans (hle a ha) (le_lmax (map_ne_nil Q₂ h) (List.mem_map.mpr ⟨a, ha, rfl⟩))

end

/-! ## Finite sums commute -/

theorem lsum_map_zero {α : Type} (l : List α) : lsum (l.map (fun _ => (0 : K))) = 0 := by
  induction l with
  | nil => simp
  | cons x xs ih => simp [ih]

theorem lsum_lsum_comm {α β : Type} :
    ∀ (l₁ : List α) (l₂ : List β) (f : α → β → K),
      lsum (l₁.map (fun a => lsum (l₂.map (fun b => f a b)))) =
      lsum (l₂.map (fun b => lsum (l₁.map (fun a => f a b)))) := by
  intro l₁
  induction l₁ with
  | nil =>
      intro l₂ f
      simp [lsum_map_zero l₂]
  | cons a as ih =>
      intro l₂ f
      simp
      rw [ih l₂ f]
      rw [← lsum_distrib]

/-! ## The finite belief MDP -/

/-- A nonnegative mass function on the safe set. -/
structure Mass (K : Type) [OrdField K] (X : Type) where
  f : X → K
  nonneg : ∀ x, 0 ≤ f x

/-- Finite belief-state safety MDP. `X` is the safe set `𝒱`; exiting is
modelled by `T_sub`, so `1 - Σ_{x'} T(a,x,x')` is the paper's one-step exit
probability `p(x,a)`. The absorbing unsafe state `⊥` is not tracked. -/
structure SafeMDP (K : Type) [OrdField K] (X Y A : Type) where
  univX : List X
  univY : List Y
  univA : List A
  univA_ne : univA ≠ []
  T : A → X → X → K
  g : A → X → X → Y → K
  T_nonneg : ∀ a x x', 0 ≤ T a x x'
  g_nonneg : ∀ a x x' y, 0 ≤ g a x x' y
  T_sub : ∀ a x, lsum (univX.map (fun x' => T a x x')) ≤ 1
  g_sum : ∀ a x x', lsum (univY.map (fun y => g a x x' y)) = 1

variable {X Y A : Type}

/-- One-step unnormalized posterior conditioned on action `a` and
observation `y`: the paper's `ℙ(y | b, a) · τ(b, a, y)`. -/
def obsMass (M : SafeMDP K X Y A) (a : A) (y : Y) (m : Mass K X) (x' : X) : K :=
  lsum (M.univX.map (fun x => m.f x * M.T a x x' * M.g a x x' y))

def step (M : SafeMDP K X Y A) (a : A) (y : Y) (m : Mass K X) : Mass K X where
  f := obsMass M a y m
  nonneg := by
    intro x'
    unfold obsMass
    apply lsum_nonneg_map
    intro x
    exact mul_nonneg (mul_nonneg (m.nonneg x) (M.T_nonneg a x x')) (M.g_nonneg a x x' y)

/-- Total mass. -/
def total (M : SafeMDP K X Y A) (m : Mass K X) : K := lsum (M.univX.map m.f)

/-- The safety value: `V_0` is the safe mass; `V_{k+1}` is the Bellman
backup — the unnormalized form of the paper's recursion. -/
noncomputable def V (M : SafeMDP K X Y A) : Nat → Mass K X → K
  | 0, m => total M m
  | k + 1, m => lmax (M.univA.map (fun a => lsum (M.univY.map (fun y => V M k (step M a y m)))))

/-- `V_0(m)` is the total safe mass — the paper's `V_0(b) = b(𝒱)`. -/
theorem V_zero (M : SafeMDP K X Y A) (m : Mass K X) : V M 0 m = total M m := rfl

/-- One Bellman backup at horizon `0` loses only the exit mass: the total
surviving mass after one step is at most the mass you started with. -/
theorem one_step_le_total (M : SafeMDP K X Y A) (a : A) (m : Mass K X) :
    lsum (M.univY.map (fun y => total M (step M a y m))) ≤ total M m := by
  change
      lsum (M.univY.map (fun y => lsum (M.univX.map (fun x' => obsMass M a y m x')))) ≤
        lsum (M.univX.map m.f)
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
    _ ≤ lsum (M.univX.map (fun x => m.f x)) := by
              apply lsum_le_lsum
              intro x hx
              calc
                m.f x * lsum (M.univX.map (fun x' => M.T a x x')) ≤ m.f x * 1 :=
                  mul_le_mul_of_nonneg_left (M.T_sub a x) (m.nonneg x)
                _ = m.f x := by rw [mul_one]

/-- **More steps cannot raise the survival probability.**

This is the fact the paper's proof of `prop:chance` invokes ("`V_{k+1} ≤
V_k` --- more steps cannot raise the survival probability"). -/
theorem V_mono_succ (M : SafeMDP K X Y A) : ∀ k (m : Mass K X), V M (k + 1) m ≤ V M k m := by
  intro k
  induction k with
  | zero =>
      intro m
      change lmax (M.univA.map (fun a => lsum (M.univY.map (fun y => total M (step M a y m))))) ≤ total M m
      apply lmax_le (map_ne_nil _ M.univA_ne)
      intro z hz
      rcases List.mem_map.mp hz with ⟨a, ha, rfl⟩
      exact one_step_le_total M a m
  | succ k ih =>
      intro m
      change lmax (M.univA.map (fun a => lsum (M.univY.map (fun y => V M (k + 1) (step M a y m))))) ≤
             lmax (M.univA.map (fun a => lsum (M.univY.map (fun y => V M k (step M a y m)))))
      apply lmax_mono M.univA_ne
      intro a ha
      apply lsum_le_lsum
      intro y hy
      exact ih (step M a y m)

/-- The safety value is nonnegative. -/
theorem V_nonneg (M : SafeMDP K X Y A) : ∀ k (m : Mass K X), 0 ≤ V M k m := by
  intro k
  induction k with
  | zero =>
      intro m
      change 0 ≤ total M m
      unfold total
      apply lsum_nonneg_map
      intro x
      exact m.nonneg x
  | succ k ih =>
      intro m
      let Q := fun a => lsum (M.univY.map (fun y => V M k (step M a y m)))
      change 0 ≤ lmax (M.univA.map Q)
      have hne : M.univA.map Q ≠ [] := map_ne_nil Q M.univA_ne
      rcases List.mem_map.mp (lmax_isMax hne).1 with ⟨a, ha, hqa⟩
      rw [← hqa]
      unfold Q
      apply lsum_nonneg_map
      intro y
      exact ih (step M a y m)

end Formalizations.POMDP
