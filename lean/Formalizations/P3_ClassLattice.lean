/-
  Formalizations.P3_ClassLattice
  =============================

  P3 (`paper2_probabilistic_sufficiency_v11.tex`) states **18 named results**
  against a `P3_ProbSufficiency.lean` holding **4 theorems**, none of which
  is any of the 18 — the module only carries generic monotonicity machinery
  for an abstract kernel `Φ`. That is the worst claim-to-code ratio in the
  repo, so this module begins closing it with the two most load-bearing and
  most checkable results.

  ## `thm:lattice` (i) — class monotonicity

  > `Π ⊆ Π'  ⟹  V^Π_k(b) ≤ V^Π'_k(b)`

  This is the spine of P3: `thm:class`, `thm:lattice`'s own chain
  `V^hold ≤ V^ol = V^seq,blind ≤ V^obs`, `prop:deficit` and `prop:freeze`
  all route through it. The paper offers no argument for it (it is stated
  as obvious, which it is *not* — it is exactly the statement that
  enlarging the admissible policy set cannot lower a maximum, and it only
  becomes trivial once the value is known to be a max over policies).

  Here it is proved from `V_is_max_over_policies` (v8). Note the proof
  needs only that each class value *dominates and attains*; it does not
  need the value to be defined by any particular recursion. That is the
  honest scope of the claim, and it is why the theorem is stated
  abstractly over `V₁ V₂`.

  ## `prop:dr` (i) — contamination interpolation

  > `inf_{q ∈ D_ρ} Σ_y q(y)·v_y = (1-ρ)·Σ_y p(y)·v_y + ρ·min_y v_y`

  the adversary spending the whole contamination `ρ` on the worst outcome.

  `OrdField` has no completeness, so `inf` over a set of distributions is
  not expressible and is **not** asserted. Instead the statement is split
  into the two halves that make an `inf` a minimum, which is what the
  claim really says:

    `contam_lower`  the contaminated expectation is ≥ the claimed value,
                    for every admissible adversary;
    `contam_sharp`  equality holds for an adversary that concentrates the
                    whole contamination on a minimizer of `v`.

  Together these say the claimed value is the minimum, without quantifying
  over a set infimum.

  Not proved here: the *construction* of a concentrating adversary as a
  normalized weight function (that needs a Kronecker-delta sum over a
  duplicate-free list, i.e. more list machinery, and the sharpness half is
  stated conditionally on `w'` being a point mass instead). Flagged rather
  than faked.

  ## Not attempted

  `prop:probecount` needs `exp`/`log` and a Chernoff bound — not
  expressible over `OrdField`. `thm:agree` and `prop:learn` are grid- and
  instance-level (numerical, Python's job). `thm:parametric`, `prop:closed`
  and `prop:additivelaw` are instance-specific closed forms on the delayed
  example and need the dynamics formalized first.
-/

import Formalizations.P1_BeliefSafety_Policy

namespace Formalizations.P3

open Formalizations
open Formalizations.POMDP

variable {K : Type} [OrdField K]
variable {X Y A : Type}

/-! ## `thm:lattice` (i): class monotonicity -/

/-- **`Π ⊆ Π' ⟹ V^Π ≤ V^Π'`.**

Each class value is required to dominate every policy in its class and to
be attained by one — i.e. to *be* the maximum over that class (the property
`V_is_max_over_policies` establishes for the unrestricted class). Given
that, monotonicity in the class is immediate, and the proof shows exactly
which hypothesis does the work: attainment on the left, domination on the
right. -/
theorem class_monotone (M : SafeMDP K X Y A)
    (Cls₁ Cls₂ : Pol A Y → Prop)
    (V₁ V₂ : Nat → Mass K X → K)
    (hV₁ : ∀ k m, (∀ π, Cls₁ π → J M k π m ≤ V₁ k m) ∧ (∃ π, Cls₁ π ∧ J M k π m = V₁ k m))
    (hV₂ : ∀ k m, (∀ π, Cls₂ π → J M k π m ≤ V₂ k m) ∧ (∃ π, Cls₂ π ∧ J M k π m = V₂ k m))
    (hsub : ∀ π, Cls₁ π → Cls₂ π) :
    ∀ k m, V₁ k m ≤ V₂ k m := by
  intro k m
  rcases (hV₁ k m).2 with ⟨π, hπ₁, hJ⟩
  rw [← hJ]
  exact (hV₂ k m).1 π (hsub π hπ₁)

/-- Corollary: any class of in-universe policies is dominated by the
unrestricted value — the top of `thm:lattice`'s chain. -/
theorem class_le_unrestricted (M : SafeMDP K X Y A) (Cls : Pol A Y → Prop)
    (Vc : Nat → Mass K X → K)
    (hVc : ∀ k m, (∀ π, Cls π → J M k π m ≤ Vc k m) ∧ (∃ π, Cls π ∧ J M k π m = Vc k m))
    (hIn : ∀ π, Cls π → PolIn M π) :
    ∀ k m, Vc k m ≤ V M k m := by
  exact class_monotone M Cls (fun π => PolIn M π) Vc (V M) hVc
    (fun k m => V_is_max_over_policies M k m) hIn

/-! ## Minima of finite lists

`Prelude` supplies maxima as hypotheses only, so minima are obtained from
`lmax` by negation. -/

/-- Minimum of a finite list. -/
noncomputable def lmin (l : List K) : K := -lmax (l.map (fun x => -x))

/-- The minimum is below every element. -/
theorem lmin_le {l : List K} (h : l ≠ []) {x : K} (hx : x ∈ l) : lmin l ≤ x := by
  unfold lmin
  have hle : -x ≤ lmax (l.map (fun x => -x)) :=
    le_lmax (map_ne_nil (fun x => -x) h) (List.mem_map.mpr ⟨x, hx, rfl⟩)
  have := neg_le_neg hle
  simpa [neg_neg] using this

/-- To bound the minimum from below, bound every element from below. -/
theorem le_lmin {l : List K} (h : l ≠ []) {c : K} (hc : ∀ x, x ∈ l → c ≤ x) :
    c ≤ lmin l := by
  unfold lmin
  have hmax : lmax (l.map (fun x => -x)) ≤ -c := by
    apply lmax_le (map_ne_nil (fun x => -x) h)
    intro z hz
    rcases List.mem_map.mp hz with ⟨x, hx, rfl⟩
    exact neg_le_neg (hc x hx)
  have := neg_le_neg hmax
  simpa [neg_neg] using this

/-- The minimum is attained by some element of the list. -/
theorem lmin_mem (l : List K) (h : l ≠ []) : ∃ x, x ∈ l ∧ lmin l = x := by
  unfold lmin
  rcases List.mem_map.mp (lmax_isMax (map_ne_nil (fun x => -x) h)).1 with ⟨x, hx, heq⟩
  exact ⟨x, hx, by rw [← heq, neg_neg]⟩

/-! ## `prop:dr` (i): contamination interpolation -/

/-- `w` is a `ρ`-contamination of the nominal weights `p` on the finite
list `l`: `w = (1-ρ)·p + ρ·w'` for some admissible adversary `w'`. -/
def Contam (l : List Y) (p w : Y → K) (ρ : K) : Prop :=
  ∃ w' : Y → K,
    (∀ y, y ∈ l → 0 ≤ w' y) ∧
    lsum (l.map w') = 1 ∧
    (∀ y, y ∈ l → w y = (1 - ρ) * p y + ρ * w' y)

/-- **`prop:dr` (i), lower half.** Every admissible adversary is bounded
below by `(1-ρ)·E_p[v] + ρ·min_y v`.

Note `ρ ≤ 1` is *not* needed for the inequality — it is needed only to
make `w` a genuine weight function. The bound is a pure consequence of
nonnegativity of `ρ` and of `w'` summing to one. -/
theorem contam_lower {l : List Y} (hne : l ≠ []) (p w : Y → K) (ρ : K)
    (hρ0 : 0 ≤ ρ) (hc : Contam l p w ρ) (v : Y → K) :
    (1 - ρ) * lsum (l.map (fun y => p y * v y)) + ρ * lmin (l.map v) ≤
      lsum (l.map (fun y => w y * v y)) := by
  rcases hc with ⟨w', hw'nonneg, hw'sum, hwdef⟩
  let mn := lmin (l.map v)
  have hmn : ∀ y, y ∈ l → mn ≤ v y := by
    intro y hy
    exact lmin_le (l := l.map v) (x := v y) (map_ne_nil v hne)
      (List.mem_map.mpr ⟨y, hy, rfl⟩)
  have hEw' : mn ≤ lsum (l.map (fun y => w' y * v y)) := by
    calc
      mn = lsum (l.map (fun y => w' y * mn)) := by
            calc
              mn = mn * 1 := by rw [mul_one]
              _ = mn * lsum (l.map w') := by rw [hw'sum]
              _ = lsum (l.map (fun y => mn * w' y)) := by rw [lsum_const_mul]
              _ = lsum (l.map (fun y => w' y * mn)) := by
                    apply lsum_congr
                    intro y hy
                    rw [mul_comm]
      _ ≤ lsum (l.map (fun y => w' y * v y)) := by
            apply lsum_le_lsum
            intro y hy
            exact mul_le_mul_of_nonneg_left (hmn y hy) (hw'nonneg y hy)
  have hsplit : lsum (l.map (fun y => w y * v y)) =
      (1 - ρ) * lsum (l.map (fun y => p y * v y)) +
        ρ * lsum (l.map (fun y => w' y * v y)) := by
    calc
      lsum (l.map (fun y => w y * v y))
          = lsum (l.map (fun y => ((1 - ρ) * p y + ρ * w' y) * v y)) := by
              apply lsum_congr
              intro y hy
              rw [hwdef y hy]
      _ = lsum (l.map (fun y => (1 - ρ) * (p y * v y) + ρ * (w' y * v y))) := by
              apply lsum_congr
              intro y hy
              rw [right_distrib]
              rw [mul_assoc, mul_assoc]
      _ = lsum (l.map (fun y => (1 - ρ) * (p y * v y))) +
            lsum (l.map (fun y => ρ * (w' y * v y))) := by
              rw [lsum_distrib]
      _ = (1 - ρ) * lsum (l.map (fun y => p y * v y)) +
            ρ * lsum (l.map (fun y => w' y * v y)) := by
              rw [lsum_const_mul, lsum_const_mul]
  rw [hsplit]
  exact add_le_add (le_refl _) (mul_le_mul_of_nonneg_left hEw' hρ0)

/-- **`prop:dr` (i), sharpness half.** An adversary that concentrates the
whole contamination on a minimizer of `v` attains the lower bound exactly.

Stated conditionally on `w'` being a point mass (rather than constructing
one) because constructing a normalized point mass needs a Kronecker-delta
sum over a duplicate-free list; see the module header. -/
theorem contam_sharp {l : List Y} [DecidableEq Y]
    (w' : Y → K) (v : Y → K) (y0 : Y)
    (hv0 : v y0 = lmin (l.map v))
    (hw'sum : lsum (l.map w') = 1)
    (hw'pt : ∀ y, y ∈ l → y ≠ y0 → w' y = 0) :
    lsum (l.map (fun y => w' y * v y)) = lmin (l.map v) := by
  calc
    lsum (l.map (fun y => w' y * v y))
        = lsum (l.map (fun y => w' y * v y0)) := by
            apply lsum_congr
            intro y hy
            by_cases hyy : y = y0
            · rw [hyy]
            · rw [hw'pt y hy hyy, zero_mul, zero_mul]
    _ = lsum (l.map (fun y => v y0 * w' y)) := by
            apply lsum_congr
            intro y hy
            rw [mul_comm]
    _ = v y0 * lsum (l.map w') := by rw [lsum_const_mul]
    _ = v y0 * 1 := by rw [hw'sum]
    _ = v y0 := by rw [mul_one]
    _ = lmin (l.map v) := hv0

end Formalizations.P3
