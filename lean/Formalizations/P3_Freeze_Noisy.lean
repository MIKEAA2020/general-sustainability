/-
  Formalizations.P3_Freeze_Noisy
  ==============================

  P3 (`paper2_probabilistic_sufficiency_v11.tex`) — final formalizable
  batch.

  ## `prop:noisyprobe` — the generalizable content

  The paper's statement is a closed form on the *declining instance*
  (drifts `9/10`, `−11/10`, specific probe horizon). What survives
  abstraction is the structure behind it:

    * a single probe produces a **two-outcome reading** — correct with
      probability `1 − ε`, flipped with probability `ε`;
    * the two branch values are **indicators**: `v_c, v_f ∈ {0,1}`;
    * the flipped reading is no better than the correct one, `v_f ≤ v_c`
      (the paper's two thresholds are nested);
    * hence the value `(1−ε)·v_c + ε·v_f` realizes **exactly three levels**
      `{0, 1−ε, 1}`.

  `three_levels` proves the range claim. Note how the fourth a-priori
  combination `(v_c, v_f) = (0,1)` is eliminated *by the nesting*, not
  assumed away — that is what makes it three levels and not four, and it
  is the one step the paper leaves to the reader ("the correct reading
  acts under drift 9/10, the flipped reading under −11/10").

  The instance-specific numbers (thresholds `z_p ≥ 1`,
  `z_p ≥ 1 + 11/10 (k − t_p)`) are not formalized: they are arithmetic
  about the declining trajectory, not structure.

  ## `prop:freeze` — the structural content

  > With deterministic kernels the survivable-set families satisfy
  > `S_{ℓ+1} ⊆ S_ℓ`; hence `V_ℓ(b)` is non-increasing in the horizon and
  > stabilizes after at most `2^{|supp b|}` strict decreases.

  Closed here:

    Survivable_succ   the nesting `S_{ℓ+1} ⊆ S_ℓ` (`Sfam_nesting`);
    Vfam_antitone     `V_ℓ(b)` is non-increasing in the horizon;
    allSubsets_length the power set of an `n`-element support has `2^n`
                      elements — the `2^{|supp b|}` magnitude;
    Sfam0_card_le     `|S_0| ≤ 2^{|supp b|}`;
    Vfam_finite_range every value `V_ℓ(b)` is `b(S)` for some `S ∈ S_0`
                      — the range lives in a finite set of that size.

  Subsets are represented as `List X` (the elements included) rather than
  `X → Bool`, so no `DecidableEq X` is needed anywhere.

  **Not closed:** the literal *count* of strict decreases (≤ `2^{|supp b|}`).
  It follows from `Vfam_finite_range` plus an injectivity argument — the map
  from a strict-drop index to the value after the drop is injective for an
  antitone sequence — but that needs `List.Nodup`/counting machinery over a
  classically filtered list. The range bound above is the substance; the
  count is bookkeeping on top of it. Flagged rather than faked.

  Survival is indexed by `Nat → A` here (not by finite action tuples as in
  `P3_Deterministic`), because horizon monotonicity is what `prop:freeze`
  needs and it is trivial for functions, painful for tuples.
-/

import Formalizations.P3_Deterministic

namespace Formalizations.P3

open Formalizations
open Formalizations.POMDP

variable {K : Type} [OrdField K]
variable {X A D Y : Type}

/-! ## `prop:noisyprobe`: the two-branch Bernoulli mixture -/

/-- `ε ≤ 1` makes `1 − ε` a legitimate weight. -/
theorem one_sub_nonneg {ε : K} (hε1 : ε ≤ 1) : 0 ≤ 1 - ε := by
  apply le_sub_of_add_le_of
  simpa using hε1

/-- The mixture is nonnegative when both branch values are. -/
theorem mixture_nonneg {ε v_c v_f : K} (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1)
    (hc : 0 ≤ v_c) (hf : 0 ≤ v_f) :
    0 ≤ (1 - ε) * v_c + ε * v_f := by
  exact add_le_add_of_nonneg (mul_nonneg (one_sub_nonneg hε1) hc) (mul_nonneg hε0 hf)

/-- **`prop:noisyprobe`, the three-level range.** A two-outcome reading
with nested indicators realizes exactly `{0, 1−ε, 1}`.

The case `(v_c, v_f) = (0, 1)` — "the correct reading dies but the flipped
one survives" — is excluded by `hnest : v_f ≤ v_c`, which is why there are
three levels and not four. -/
theorem three_levels (ε v_c v_f : K)
    (hv_c : v_c = 0 ∨ v_c = 1) (hv_f : v_f = 0 ∨ v_f = 1)
    (hnest : v_f ≤ v_c) :
    (1 - ε) * v_c + ε * v_f = 0 ∨
    (1 - ε) * v_c + ε * v_f = 1 - ε ∨
    (1 - ε) * v_c + ε * v_f = 1 := by
  rcases hv_c with hc | hc <;> rcases hv_f with hf | hf
  · left
    simp [hc, hf, mul_zero]
  · exfalso
    rw [hf, hc] at hnest
    exact (not_le_of_lt zero_lt_one) hnest
  · right; left
    simp [hc, hf, mul_one, mul_zero, add_zero]
  · right; right
    simp [hc, hf, mul_one, sub_add_cancel]

/-! ## `prop:freeze`: survival indexed by horizon -/

/-- `survK k u x`: `x` survives `k` steps under the action schedule `u`,
adversarially in the disturbance. Declared as a `Prop`, not a `Bool`, so
that horizon monotonicity is a plain induction instead of an exercise in
`Bool.and` / `List.all` lemmas. -/
def survK (M : DetMDP K X A D Y) : Nat → (Nat → A) → X → Prop
  | 0, _, x => M.safe x = true
  | k + 1, u, x =>
      M.safe x = true ∧
        ∀ d, d ∈ M.univD x (u 0) → survK M k (fun i => u (i + 1)) (M.F x (u 0) d)

/-- Surviving longer implies surviving shorter. -/
theorem survK_mono_succ (M : DetMDP K X A D Y) :
    ∀ k (u : Nat → A) (x : X), survK M (k + 1) u x → survK M k u x := by
  intro k
  induction k with
  | zero =>
      intro u x h
      exact h.1
  | succ k ih =>
      intro u x h
      constructor
      · exact h.1
      · intro d hd
        exact ih (fun i => u (i + 1)) (M.F x (u 0) d) (h.2 d hd)

theorem survK_mono (M : DetMDP K X A D Y) : ∀ {k n : Nat}, k ≤ n →
    ∀ (u : Nat → A) (x : X), survK M n u x → survK M k u x := by
  intro k n hkn
  induction hkn with
  | refl =>
      intro u x h
      exact h
  | step h ih =>
      intro u x hn
      exact ih u x (survK_mono_succ M _ u x hn)

/-! ## The survivable-set family -/

/-- `S` is `k`-step survivable if one declared schedule keeps every
`x ∈ S` safe for `k` steps. -/
def Survivable (M : DetMDP K X A D Y) (S : List X) (k : Nat) : Prop :=
  ∃ u : Nat → A, ∀ x, x ∈ S → survK M k u x

/-- **The nesting `S_{k+1} ⊆ S_k`.** -/
theorem Survivable_succ (M : DetMDP K X A D Y) (S : List X) :
    ∀ k, Survivable M S (k + 1) → Survivable M S k := by
  intro k h
  rcases h with ⟨u, hu⟩
  exact ⟨u, fun x hx => survK_mono_succ M k u x (hu x hx)⟩

theorem Survivable_mono (M : DetMDP K X A D Y) (S : List X) {k n : Nat}
    (hkn : k ≤ n) : Survivable M S n → Survivable M S k := by
  intro h
  rcases h with ⟨u, hu⟩
  exact ⟨u, fun x hx => survK_mono M hkn u x (hu x hx)⟩

/-- Power set of a support, as a list of lists. -/
def subsetsOf : List X → List (List X)
  | [] => [[]]
  | x :: xs =>
      let ss := subsetsOf xs
      ss ++ ss.map (fun S => x :: S)

theorem nil_mem_subsetsOf : ∀ l : List X, [] ∈ subsetsOf l
  | [] => by simp [subsetsOf]
  | x :: xs => by simp [subsetsOf, nil_mem_subsetsOf xs]

/-- `|𝒫(l)| = 2^{|l|}` — the `2^{|supp b|}` of `prop:freeze`. -/
theorem subsetsOf_length : ∀ l : List X, (subsetsOf l).length = 2 ^ l.length
  | [] => by simp [subsetsOf]
  | x :: xs => by
      simp [subsetsOf, subsetsOf_length xs, Nat.pow_succ, Nat.mul_two]

/-- The declared family `S_k`: the survivable subsets of the support. -/
noncomputable def Sfam (M : DetMDP K X A D Y) (k : Nat) : List (List X) := by
  classical
  exact (subsetsOf M.univX).filter (fun S => Survivable M S k)

/-- Filtering cannot lengthen a list. -/
theorem length_filter_le : ∀ (l : List (List X)) (p : List X → Prop) [DecidablePred p],
    (l.filter p).length ≤ l.length := by
  intro l
  induction l with
  | nil =>
      intro p hp
      simp
  | cons S ss ih =>
      intro p hp
      by_cases hS : p S
      · simp [hS]
        exact ih p
      · simp [hS]
        exact Nat.le_trans (ih p) (Nat.le_succ _)

/-- **The nesting `S_{k+1} ⊆ S_k`, at the level of families.** -/
theorem Sfam_nesting (M : DetMDP K X A D Y) :
    ∀ k, ∀ S, S ∈ Sfam M (k + 1) → S ∈ Sfam M k := by
  intro k S h
  simp [Sfam, List.mem_filter] at h ⊢
  exact ⟨h.1, Survivable_succ M S k h.2⟩

theorem Sfam_mono (M : DetMDP K X A D Y) {k n : Nat} (hkn : k ≤ n) :
    ∀ S, S ∈ Sfam M n → S ∈ Sfam M k := by
  intro S h
  simp [Sfam, List.mem_filter] at h ⊢
  exact ⟨h.1, Survivable_mono M S hkn h.2⟩

/-- The family is inhabited: the empty set survives vacuously. -/
theorem Sfam_ne (M : DetMDP K X A D Y) (k : Nat) : Sfam M k ≠ [] := by
  apply ne_nil_of_exists_mem
  refine ⟨[], ?_⟩
  simp [Sfam, List.mem_filter]
  constructor
  · exact nil_mem_subsetsOf M.univX
  · rcases exists_mem_of_ne_nil M.univA_ne with ⟨a, ha⟩
    exact ⟨fun _ => a, by intro x hx; cases hx⟩

/-! ## The family value -/

/-- Mass of a subset. -/
def bS (S : List X) (b : Mass K X) : K := lsum (S.map b.f)

/-- `V_ℓ(b) = max_{S ∈ S_ℓ} b(S)` — `prop:antichain` (i), serving here as
the definition of the family value. -/
noncomputable def Vfam (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) : K :=
  lmax ((Sfam M k).map (fun S => bS S b))

/-- **`V_ℓ(b)` is non-increasing in the horizon.** Immediate from the
nesting: a maximum over a shrinking family cannot grow. -/
theorem Vfam_antitone (M : DetMDP K X A D Y) {k n : Nat} (hkn : k ≤ n)
    (b : Mass K X) : Vfam M n b ≤ Vfam M k b := by
  unfold Vfam
  apply lmax_le_lmax_of_subset (map_ne_nil (fun S => bS S b) (Sfam_ne M n))
  intro z hz
  rcases List.mem_map.mp hz with ⟨S, hS, rfl⟩
  exact List.mem_map.mpr ⟨S, Sfam_mono M hkn S hS, rfl⟩

/-- `|S_0| ≤ 2^{|supp b|}`: the cardinal bound behind `prop:freeze`. -/
theorem Sfam0_card_le (M : DetMDP K X A D Y) :
    (Sfam M 0).length ≤ 2 ^ M.univX.length := by
  calc
    (Sfam M 0).length ≤ (subsetsOf M.univX).length := by
        unfold Sfam
        classical
        exact length_filter_le (subsetsOf M.univX) (fun S => Survivable M S 0)
    _ = 2 ^ M.univX.length := subsetsOf_length M.univX

/-- **Every value is attained by a set in the frozen family**, so the range
of `ℓ ↦ V_ℓ(b)` is contained in `{b(S) : S ∈ S_0}` — a finite set of size
at most `2^{|supp b|}`. This is the substance of the stabilization claim. -/
theorem Vfam_finite_range (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) :
    ∃ S, S ∈ Sfam M 0 ∧ Vfam M k b = bS S b := by
  unfold Vfam
  have hne : (Sfam M k).map (fun S => bS S b) ≠ [] :=
    map_ne_nil (fun S => bS S b) (Sfam_ne M k)
  rcases List.mem_map.mp (lmax_isMax hne).1 with ⟨S, hS, hval⟩
  exact ⟨S, Sfam_mono M (Nat.zero_le k) S hS, hval.symm⟩

end Formalizations.P3
