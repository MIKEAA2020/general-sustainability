/-
  `prop:deadline` — the deadline law on the cube.
  Paper reference: paper2_exact_belief_computation_v10,
  §"A deadline instance" (`prop:deadline`, ll. 365–392).

  The statement. Hold for `T` steps (drift `−1/2`), let the parameter be
  revealed exactly at `T`, then play matched forever (drift `+3/10` on
  every branch). Viability holds exactly when

      z₀ ≥ 1 + T/2,      T = 0, …, 4.

  ## Why this needs no delayed-instance machinery

  The delay lives entirely in the *shape of the action sequence*, not in
  the state. For branch `θ` the realized sequence is

      hold^T  ++  (matched θ)^n

  and `survivesTo I θ us z0` is already a branchwise predicate taking an
  arbitrary action list. Adaptivity after revelation therefore costs
  nothing: each branch supplies its own list, and `matched` is
  θ-dependent by construction. No state expansion, no belief or filter,
  no new transition structure. The revelation event itself is never
  modelled, because the claim concerns the realized trajectory — which
  is how the paper's own proof proceeds ("under the hold every cell
  drifts −1/2 … after revelation the matched action rises at +3/10 on
  every branch"; "the direct branchwise argument needs no
  scalar-additivity hypothesis").

  The paper's two numbers are already in the layer: hold scores
  `ipi = 0` (`hold_action_zero`) so drifts `−1/2`; matched scores
  `ipi = m` (`ipi_matched`) so at `m = 4` drifts `−1/2 + 4/5 = +3/10`,
  which the layer carries as `matched_scale_m4`: `10·d = 3`.

  ## Contents

  §1 the deadline policy; §2 the two drifts; §3 the hold phase
  (necessity); §4 the matched phase (sufficiency); §5 the law;
  §6 the sequence is in the paper's alphabet.
-/

import Formalizations.EBC_Dynamics
import Formalizations.EBC_Bands
import Formalizations.EBC_Pairs_v2
import Formalizations.EBC_Pairs_v3

namespace Formalizations.EBC

variable {K : Type} [OrdField K]

/-! ## §1 The deadline policy -/

/-- **The all-hold action.** -/
def holdAct : Nat → Tri := fun _ => Tri.hold

/-- `t` consecutive holds. -/
def holdRep : Nat → List (Nat → Tri)
  | 0 => []
  | n + 1 => holdAct :: holdRep n

/-- `n` consecutive matched plays for cell `θ`. -/
def matchedRep : Nat → (Nat → Bool) → List (Nat → Tri)
  | 0, _ => []
  | n + 1, θ => matched θ :: matchedRep n θ

/-- **The deadline sequence**: hold for `T` steps, then play matched for
`n` more. Parameterized by the tail length rather than by a total
horizon `L` and a subtraction, so no `Nat` subtraction enters. -/
def deadlineSeq (T n : Nat) (θ : Nat → Bool) : List (Nat → Tri) :=
  holdRep T ++ matchedRep n θ

@[simp] theorem holdRep_zero : holdRep 0 = ([] : List (Nat → Tri)) := rfl
@[simp] theorem matchedRep_zero (θ : Nat → Bool) :
    matchedRep 0 θ = ([] : List (Nat → Tri)) := rfl

theorem holdRep_length : ∀ t, (holdRep t).length = t := by
  intro t; induction t with
  | zero => rfl
  | succ t ih => simp [holdRep, ih]

theorem matchedRep_length (θ : Nat → Bool) : ∀ n, (matchedRep n θ).length = n := by
  intro n; induction n with
  | zero => rfl
  | succ n ih => simp [matchedRep, ih]

/-! ## §2 The two drifts -/

/-- **The hold drifts `−1/2`**: `d(hold, θ) = −1/2 + (1/5)·0`. -/
theorem holdAct_drift (I : List Nat) (θ : Nat → Bool) :
    drift I holdAct θ = -half (K := K) := by
  unfold drift
  have hz : ipi I holdAct θ = (0 : K) := by
    change ipi I (fun _ => Tri.hold) θ = (0 : K)
    exact hold_action_zero (K := K) I θ
  rw [hz]
  simp

/-- **The matched drift is nonnegative at `m = 4`.** The paper's value is
`+3/10` (`matched_scale_m4`: `10·d = 3`); sufficiency needs only `d ≥ 0`,
since once `z ≥ 1` a nonnegative drift keeps every later state at or
above the floor. -/
theorem matched_drift_nonneg (I : List Nat) (θ : Nat → Bool) (hlen : I.length = 4) :
    (0 : K) ≤ drift I (matched θ) θ := by
  apply le_of_mul_le_mul_pos (c := ten (K := K))
  · calc
      ten (K := K) * (0 : K) = (0 : K) := by simp
      _ ≤ three := le_of_lt three_pos
      _ = ten (K := K) * drift I (matched θ) θ := by
            symm
            exact matched_scale_m4 I θ hlen
  · exact ten_pos

/-- `1/2 > 0`. -/
theorem deadline_half_pos : (0 : K) < half (K := K) := by
  change (0 : K) < (1 : K) / two (K := K)
  exact div_pos (zero_lt_one (K := K)) (two_pos (K := K))

theorem deadline_half_nonneg : (0 : K) ≤ half (K := K) :=
  le_of_lt (deadline_half_pos (K := K))

/-! ## §3 The hold phase — necessity -/

/-- The accumulated drift of `t` holds is `t·(−1/2)`. -/
theorem totalDrift_holdRep (I : List Nat) (θ : Nat → Bool) :
    ∀ t, totalDrift I θ (holdRep t) = natToK (K := K) t * (-half (K := K)) := by
  intro t
  induction t with
  | zero => simp [holdRep, totalDrift]
  | succ t ih =>
      calc
        totalDrift I θ (holdRep (t + 1))
            = drift I holdAct θ + totalDrift I θ (holdRep t) := by
                simp [holdRep, totalDrift]
        _ = -half (K := K) + natToK (K := K) t * (-half (K := K)) := by
                rw [holdAct_drift, ih]
        _ = natToK (K := K) (t + 1) * (-half (K := K)) := by
                rw [natToK_succ, right_distrib, one_mul', add_comm]

/-- **Necessity.** If the branch survives the hold to revelation, then
`z₀ ≥ 1 + T/2`. At revelation the state is `z₀ − T/2`, and survival
forces it at or above the floor. -/
theorem deadline_necessity (I : List Nat) (θ : Nat → Bool) (T : Nat) (z0 : K)
    (hs : survivesTo I θ (holdRep T) z0) :
    (1 : K) + natToK (K := K) T * half (K := K) ≤ z0 := by
  have hfinal : (1 : K) ≤ stateAfter I θ (holdRep T) z0 :=
    survivesTo_final I θ (holdRep T) z0 hs
  have hstate : stateAfter I θ (holdRep T) z0 =
      z0 + natToK (K := K) T * (-half (K := K)) := by
    rw [stateAfter_eq, totalDrift_holdRep]
  have h1 : (1 : K) ≤ z0 + natToK (K := K) T * (-half (K := K)) := by
    rwa [hstate] at hfinal
  have hneg : natToK (K := K) T * (-half (K := K)) =
      -(natToK (K := K) T * half (K := K)) := by
    rw [mul_neg]
  have h2 : (1 : K) ≤ z0 - natToK (K := K) T * half (K := K) := by
    simpa [sub_eq, hneg] using h1
  calc
    (1 : K) + natToK (K := K) T * half (K := K)
        ≤ (z0 - natToK (K := K) T * half (K := K))
            + natToK (K := K) T * half (K := K) :=
          add_le_add_right h2 (natToK (K := K) T * half (K := K))
    _ = z0 := sub_add_cancel z0 (natToK (K := K) T * half (K := K))

/-! ## §4 The matched phase — sufficiency -/

/-- **Matched forever keeps a surviving branch alive.** Induction on the
tail: the current state is at or above the floor, and the matched drift
is nonnegative, so the next one is too. -/
theorem matchedRep_survives (I : List Nat) (θ : Nat → Bool) (hlen : I.length = 4) :
    ∀ n z, (1 : K) ≤ z → survivesTo I θ (matchedRep n θ) z := by
  intro n
  induction n with
  | zero =>
      intro z hz
      simpa [matchedRep, survivesTo] using hz
  | succ n ih =>
      intro z hz
      simp [matchedRep, survivesTo]
      constructor
      · exact hz
      · apply ih
        have hd : (0 : K) ≤ drift I (matched θ) θ := matched_drift_nonneg I θ hlen
        have hz0 : (1 : K) ≤ z + (0 : K) := by simpa using hz
        exact le_trans hz0 (add_le_add_left hd z)

/-- **The hold phase keeps every branch alive** exactly when
`z₀ ≥ 1 + T/2`. -/
theorem holdRep_survives (I : List Nat) (θ : Nat → Bool) :
    ∀ T z0, (1 : K) + natToK (K := K) T * half (K := K) ≤ z0 →
      survivesTo I θ (holdRep T) z0 := by
  intro T
  induction T with
  | zero =>
      intro z0 hz
      simpa [holdRep, survivesTo] using hz
  | succ T ih =>
      intro z0 hz
      simp [holdRep, survivesTo]
      constructor
      · have hnonneg : (0 : K) ≤ natToK (K := K) (T + 1) * half (K := K) :=
          mul_nonneg (natToK_nonneg (T + 1)) (deadline_half_nonneg (K := K))
        have hle : (1 : K) ≤ (1 : K) + natToK (K := K) (T + 1) * half (K := K) := by
          calc
            (1 : K) = (1 : K) + 0 := by simp
            _ ≤ (1 : K) + natToK (K := K) (T + 1) * half (K := K) :=
                add_le_add_left hnonneg (1 : K)
        exact le_trans hle hz
      · apply ih
        -- goal: 1 + natToK T * half ≤ z0 + drift I holdAct θ
        rw [holdAct_drift]
        let A : K := natToK (K := K) T * half (K := K)
        change (1 : K) + A ≤ z0 + (-half (K := K))
        -- `natToK (T+1)·half = A + half`: one more half-step than `T`.
        have hT : (natToK (K := K) T + 1) * half (K := K) = A + half (K := K) := by
          dsimp [A]
          rw [right_distrib, one_mul']
        have hz' : (1 : K) + (A + half (K := K)) ≤ z0 := by
          simpa [hT] using hz
        -- subtract `half` from both sides
        have hsub : ((1 : K) + (A + half (K := K))) + (-(half (K := K))) ≤
            z0 + (-(half (K := K))) :=
          add_le_add_right hz' (-(half (K := K)))
        calc
          (1 : K) + A = ((1 : K) + (A + half (K := K))) + (-(half (K := K))) := by
            calc
              (1 : K) + A = (1 : K) + (A + 0) := by simp
              _ = (1 : K) + (A + (half (K := K) + (-(half (K := K))))) := by
                    rw [← add_neg_cancel (half (K := K))]
              _ = (1 : K) + ((A + half (K := K)) + (-(half (K := K)))) := by
                    rw [← add_assoc A (half (K := K)) (-(half (K := K)))]
              _ = ((1 : K) + (A + half (K := K))) + (-(half (K := K))) := by
                    rw [← add_assoc (1 : K) (A + half (K := K)) (-(half (K := K)))]
          _ ≤ z0 + (-(half (K := K))) := hsub
          _ = z0 + (-half (K := K)) := rfl

/-! ## §5 The law -/

/-- Survival across a concatenation. -/
theorem survivesTo_append (I : List Nat) (θ : Nat → Bool) :
    ∀ (us vs : List (Nat → Tri)) (z : K),
      survivesTo I θ us z → survivesTo I θ vs (stateAfter I θ us z) →
      survivesTo I θ (us ++ vs) z := by
  intro us
  induction us with
  | nil =>
      intro vs z hs hv
      simpa [stateAfter] using hv
  | cons u us ih =>
      intro vs z hs hv
      simp [survivesTo] at hs ⊢
      constructor
      · exact hs.1
      · apply ih
        · exact hs.2
        · simpa [stateAfter] using hv

/-- **Sufficiency.** `z₀ ≥ 1 + T/2` implies the branch survives the
deadline policy for any number `n` of post-revelation steps. -/
theorem deadline_sufficiency (I : List Nat) (θ : Nat → Bool) (hlen : I.length = 4)
    (T n : Nat) (z0 : K)
    (hz : (1 : K) + natToK (K := K) T * half (K := K) ≤ z0) :
    survivesTo I θ (deadlineSeq T n θ) z0 := by
  unfold deadlineSeq
  apply survivesTo_append
  · exact holdRep_survives I θ T z0 hz
  · apply matchedRep_survives I θ hlen n
    exact survivesTo_final I θ (holdRep T) z0 (holdRep_survives I θ T z0 hz)

/-- **`prop:deadline`.** Viability holds exactly when `z₀ ≥ 1 + T/2`:
the branch survives the deadline policy to every horizon iff the
inequality holds. The paper restricts to `T = 0, …, 4`; nothing in the
argument uses that restriction, so `T` is left symbolic. -/
theorem deadline_law (I : List Nat) (θ : Nat → Bool) (hlen : I.length = 4)
    (T : Nat) (z0 : K) :
    ((1 : K) + natToK (K := K) T * half (K := K) ≤ z0) ↔
      ∀ n, survivesTo I θ (deadlineSeq T n θ) z0 := by
  constructor
  · intro hz n
    exact deadline_sufficiency I θ hlen T n z0 hz
  · intro h
    have h0 := h 0
    exact deadline_necessity I θ T z0 (by simpa [deadlineSeq] using h0)

/-! ## §6 The deadline sequence is in the paper's alphabet -/

/-- The hold action is the all-hold. -/
theorem holdAct_isFullHold : isFullHold holdAct := by
  intro i
  rfl

theorem matchedRep_mem_inAlphabet (θ : Nat → Bool) :
    ∀ n u, u ∈ matchedRep n θ → inAlphabet u := by
  intro n
  induction n with
  | zero =>
      intro u hu
      simp [matchedRep] at hu
  | succ n ih =>
      intro u hu
      simp [matchedRep] at hu
      rcases hu with rfl | h
      · exact Or.inl (matched_is_cell θ)
      · exact ih u h

theorem deadlineSeq_mem_inAlphabet (θ : Nat → Bool) (n : Nat) :
    ∀ T u, u ∈ deadlineSeq T n θ → inAlphabet u := by
  intro T
  induction T with
  | zero =>
      intro u hu
      exact matchedRep_mem_inAlphabet θ n u (by simpa [deadlineSeq] using hu)
  | succ T ih =>
      intro u hu
      simp [deadlineSeq, holdRep] at hu
      rcases hu with rfl | h
      · exact Or.inr holdAct_isFullHold
      · exact ih u (by simpa [deadlineSeq] using h)

/-- The deadline policy uses only the paper's 17 actions: the 16 cell
actions and the all-hold. -/
theorem deadlineSeq_inAlphabet (T n : Nat) (θ : Nat → Bool)
    (u : Nat → Tri) (hu : u ∈ deadlineSeq T n θ) : inAlphabet u :=
  deadlineSeq_mem_inAlphabet θ n T u hu

end Formalizations.EBC
