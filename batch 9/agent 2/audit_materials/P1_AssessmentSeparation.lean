/-
  Formalizations.P1_AssessmentSeparation
  =====================================

  Lean formalization of the theorem layer of paper 1 itself,

    the assessment-separation head paper of the programme (source of
    record: `paper1_assessment_separation_v62.tex`, the sealed JMCDA
    submission edition; all item numbers below are stable across the
    v35–v62 chain).

  This completes the family coverage: the eight companion slots are
  formalized in `Formalizations.P1_Obstruction` … `E1_ForecastLadder`;
  the head paper's own theorem layer is this module.

  Scope and fidelity.

    * **The witness datum (Section 4.5).**  The datum is a concrete finite
      object — phase label, reserve stock `x`, two typed floors `s₁ s₂`,
      dip depth 2, gain `e = 1/4`, rescue cost `c = 1` — and is modeled
      exactly: worst-case tubes as predicates on visited states, endpoint
      sets, and destination-labelled successors.  Every tube is the exact
      visited set (the trajectories are piecewise monotone), so there is
      no outer approximation anywhere.

    * **Theorem 5 (witnessed separation), parts (1)–(7).**  The three
      closed accepted-set identities (`V_typ`, `V_weak`, `V_phys =
      V_end`), the acceptance-gap identity `FP_agg = I` with its interior
      witness, the strictness of both hierarchy inclusions (witnesses
      `(1/2, 6/5, 6/5)` and `(1/2, 1/10, 1/10)`), the per-weight
      licensing thresholds `ρ₁ = (2-s₁)/s₂`, `ρ₂ = s₁/(2-s₂)` with the
      overlap law `ρ₂ ≥ ρ₁ ↔ s₁+s₂ ≥ 2`, and the rescue split with all
      four exhibited typed violations on the impossibility region.

    * **The operator machinery the theorem consumes** — instances on the
      datum of the paper's Remark 2 (full-cone scalarization) and
      Proposition 3 (the fourfold chain `E_typ ⊆ E_w ⊆ E_tube,phys ⊆
      E_end`, and the full-cone identity `E_typ = ⋂_w E_w`, the paper's
      contribution (i)).

    * **Theorem 9 (blend collapse), parts (i)–(iii)**, with the
      delimiting converse **Proposition 10** (sequential time-sharing
      does not erase the gap).

    * **Lemma A (the handshake)** — the normalized-weight identity
      `∑ wᵢλᵢ ≥ 1 ↔ w·s ≥ 0` (with `λᵢ = 1 + sᵢ`), the consequent
      "same acceptance set at every state and weight" (the θ = 1 member
      is the compensatory engine exactly), and the threshold agreement
      `ρ₁ = 2/3, ρ₂ = 3/2` at the benchmark datum `(1/2, 6/5, 6/5)`.

    * **Lemma B (collapse convention)** — the θ < 1 family's defining
      convention (a tube value `λᵢ ≤ 0` rejects the plan) and the fact
      that the θ = 1 member alone compensates across collapse, with an
      explicit rational witness.

    * **The master equation and Theorem S2 (the two-sided Leontief
      statement).**  The θ-rung protocol on the gap-region diagonal is
      reduced, at an abstract monotone/antitone power interface, to the
      single master comparison (the averaging argument: the two plan
      conditions sum to `A + B`, so the equal weight is always the
      binding one).  All four signs of the ladder are covered:
      θ > 0 and θ < 0 at the abstract interface; the negative-integer
      rungs `θ = -m` (elasticities `σ = 1/(m+1)`) instantiate it in pure
      ordered-field arithmetic — the golden-ratio closed form at `m = 1`
      (Fibonacci witnesses 8/5 rejects / 13/8 accepts, the whole
      interval `[13/8, 2)`), the paper's `σ = 1/4` witness (θ = -3
      accepts 9/5), and the `∀m` false-certification family (every
      `σ = 1/(m+1)` false-certifies `[2 - 2^-(m+1), 2)` — via a
      Bernoulli-type lower bound proved here); the fractional rungs
      through algebraic power-law interfaces — the square law for θ = 1/2
      (σ = 2, whose exact rational floor `5/4` is proved as an iff, the
      ladder table's row) and the cube law `pw x³ = x²` for θ = 2/3
      (σ = 3, the canonical datum 6/5 with the rational brackets
      `(1/3, 5/3)` proved inside the layer, and the critical-elasticity
      bracket `σ* ∈ (2, 3]` at the Section 6.3 datum); and the geometric
      member θ = 0 (σ = 1, the LPI functional form) through the
      geometric-mean interface `GeoLaws` (positivity, per-coordinate
      monotonicity, the swap-product identity `gp(x,y,w)·gp(y,x,w) = xy`
      replacing the paper's log-space averaging, and equal-weight
      symmetry) — the master comparison `s² ≥ 2`, the paper's witness
      `3/2`, and the `√2` floor's rational bracket `141/100` rejects.
      S2(i): the θ = 1 rung accepts every gap state (full Leontief is
      never necessary at a fixed state).  The Leontief identification
      `V⁰ = V_typ`: the σ = 0 member accepts no gap state — the only
      uniformly safe aggregator of the covered family
      (`s2_two_sided_summary`).

  Not formalized (and why), per the layer's fidelity policy:

    * **Theorem S1 (nesting)** — monotonicity of the power means in θ —
      and with it the prefix/ladder structure of `σ*` across distinct
      rungs and the transfer of false-certification intervals to
      non-ladder elasticities: the θ-family's order structure is
      genuinely analytic (real exponents); each rung's up-set-in-`s`
      structure is proved instead.
    * The relative-interior topology of Theorem 5(4) — replaced by the
      explicit strictly-interior witness; the continuity (IVT) step in
      the paper's S2(ii) — replaced by explicit rational interval
      witnesses (a constructive strengthening).
    * The fishery instantiation (the resource-transition benchmark) —
      instance level, certified by the deposited verifier batteries.

  Every theorem is fully proved; there are no `sorry`s and no extra
  axioms.  As everywhere in this layer, statements are interface-level
  over `OrdField K`; the paper's statements are the instance `K = ℝ`.
-/

import Formalizations.Prelude

namespace Formalizations.P1Sep

set_option linter.unusedSectionVars false

/-! ## Arithmetic toolkit: `natK`, `npow`, fractions

Lean core gives this project the numerals `0` and `1` only (no `OfNat`
derivation beyond `Zero`/`One`), so every other rational is built by the
cast `natK` and compared through `Nat` (`decide`/`omega`), and powers by
the recursion `npow`.  All witness arithmetic below reduces to `Nat`
comparisons this way. -/

variable {K : Type} [OrdField K]

/-! ### Ordered-field helpers -/

/-- Chaining for `≤`-calculations (needed by multi-step `calc`s). -/
instance : Trans (α := K) (β := K) (γ := K) LE.le LE.le LE.le :=
  ⟨fun h1 h2 => le_trans h1 h2⟩

theorem invz : (0 : K)⁻¹ = 0 := OrdField.inv_zero

theorem inv_one : (1 : K)⁻¹ = 1 := by
  have h1 := mul_inv_cancel_field ((zero_ne_one' (K := K)).symm : (1 : K) ≠ 0)
  rw [one_mul'] at h1
  exact h1

theorem div_self {a : K} (h : a ≠ 0) : a / a = 1 := by
  rw [div_eq, mul_inv_cancel_field h]

theorem neg_add_dist (a b : K) : -(a + b) = -a + -b := by
  have h : (-a + -b) + (a + b) = 0 := by
    rw [add_comm4, neg_add_cancel, neg_add_cancel, add_zero]
  exact (neg_eq_of_add_eq_zero_right h).symm

theorem add_le_cancel_left {a b c : K} (h : a + b ≤ a + c) : b ≤ c := by
  have h1 : 0 ≤ (a + c) - (a + b) := sub_nonneg.mpr h
  have h2 : (a + c) - (a + b) = c - b := by
    rw [sub_eq, sub_eq, neg_add_dist, add_comm4, add_neg_cancel, zero_add]
  rw [h2] at h1
  exact sub_nonneg.mp h1

theorem eq_of_sub_eq_zero {a b : K} (h : a - b = 0) : a = b := by
  rw [sub_eq] at h
  have h1 := neg_eq_of_add_eq_zero_right h
  rw [neg_neg] at h1
  exact h1

theorem sub_right_cancel {a b c : K} (h : a - c = b - c) : a = b := by
  rw [sub_eq, sub_eq] at h
  exact add_right_cancel h

theorem mul_right_cancel' {a b c : K} (hc : c ≠ 0) (h : a * c = b * c) : a = b :=
  mul_left_cancel hc (by rw [mul_comm c a, mul_comm c b]; exact h)

theorem mul_lt_mul_of_pos_right {a b c : K} (h : a < b) (hc : 0 < c) :
    a * c < b * c := by
  refine lt_of_le_of_ne (mul_le_mul_of_nonneg_right (le_of_lt h) (le_of_lt hc)) ?_
  intro heq
  exact (ne_of_lt h) (mul_right_cancel' (ne_of_gt hc) heq)

theorem mul_lt_mul_of_pos_left {a b c : K} (h : a < b) (hc : 0 < c) :
    c * a < c * b := by
  rw [mul_comm c a, mul_comm c b]
  exact mul_lt_mul_of_pos_right h hc

theorem neg_lt_neg' {a b : K} (h : a < b) : -b < -a := by
  refine ⟨neg_le_neg h.1, fun hle => ?_⟩
  have h1 := neg_le_neg hle
  rw [neg_neg, neg_neg] at h1
  exact h.2 h1

theorem neg_eq_zero' {a : K} (h : -a = 0) : a = 0 := by
  have h2 : -(-a) = 0 := by rw [h, neg_zero]
  rw [neg_neg a] at h2
  exact h2

theorem neg_pos' {a : K} (h : a < 0) : 0 < -a := by
  refine ⟨by rw [← neg_zero]; exact neg_le_neg h.1, fun hz => ?_⟩
  have h1 : -a = 0 :=
    le_antisymm hz (by rw [← neg_zero]; exact neg_le_neg h.1)
  exact h.2 (by rw [neg_eq_zero' h1]; exact le_refl 0)

theorem neg_nonneg' {a : K} (h : a ≤ 0) : 0 ≤ -a := by
  rw [← neg_zero]; exact neg_le_neg h

theorem mul_le_cancel_left {a b c : K} (hc : 0 < c) (h : c * a ≤ c * b) : a ≤ b := by
  cases le_total a b with
  | inl hab => exact hab
  | inr hba =>
      by_cases hab : a = b
      · rw [hab]; exact le_refl b
      · exact absurd h (not_le_of_lt
          (mul_lt_mul_of_pos_left (lt_of_le_of_ne hba (fun he => hab he.symm)) hc))

theorem mul_le_cancel_right {a b c : K} (hc : 0 < c) (h : a * c ≤ b * c) : a ≤ b :=
  mul_le_cancel_left hc (by rw [mul_comm c a, mul_comm c b]; exact h)

theorem sub_le_self (a b : K) (hb : 0 ≤ b) : a - b ≤ a := by
  have hn : -b ≤ 0 := by rw [← neg_zero]; exact neg_le_neg hb
  have h1 : a + -b ≤ a + 0 := add_le_add_left hn a
  rw [add_zero] at h1
  exact h1

theorem sub_le_sub_right {a b : K} (h : a ≤ b) (c : K) : a - c ≤ b - c :=
  add_le_add_right h (-c)

theorem add_le_cancel_right {a b c : K} (h : a + c ≤ b + c) : a ≤ b := by
  have h1 : (a + c) - c ≤ (b + c) - c := sub_le_sub_right h c
  rw [add_sub_cancel, add_sub_cancel] at h1
  exact h1

theorem sub_sub (a c d : K) : a - (c - d) = a - c + d := by
  rw [sub_eq, sub_eq, sub_eq, neg_add_dist, neg_neg,
    ← add_assoc a (-c) d]

theorem sub_lt_sub_right {a b : K} (h : a < b) (c : K) : a - c < b - c :=
  lt_of_le_of_ne (sub_le_sub_right (le_of_lt h) c)
    (fun he => (ne_of_lt h) (sub_right_cancel he))

theorem neg_le_of_add_nonneg {a b : K} (h : 0 ≤ a + b) : -a ≤ b := by
  have h1 : 0 ≤ b - (-a) := by
    rw [sub_eq, neg_neg, add_comm]; exact h
  exact sub_nonneg.mp h1

theorem le_of_not_lt {a b : K} (h : ¬ a < b) : b ≤ a := by
  by_cases hba : b ≤ a
  · exact hba
  · exact absurd (le_of_not_le hba) h

theorem sub_lt_zero {a b : K} : a - b < 0 ↔ a < b := by
  constructor
  · intro h
    have h1 : ¬ (b ≤ a) := fun hba => h.2 (sub_nonneg.mpr hba)
    refine ⟨?_, h1⟩
    cases le_total a b with
    | inl hab => exact hab
    | inr hba => exact absurd hba h1
  · intro h
    cases le_total 0 (a - b) with
    | inl hpos => exact absurd (sub_nonneg.mp hpos) h.2
    | inr hneg =>
        refine ⟨hneg, fun hpos => ?_⟩
        exact absurd (eq_of_sub_eq_zero (le_antisymm hneg hpos)) (ne_of_lt h)

theorem le_add_right (a b : K) (hb : 0 ≤ b) : a ≤ a + b := by
  have h1 : a + 0 ≤ a + b := add_le_add_left hb a
  rwa [add_zero] at h1

theorem add_sub_comm (a b c : K) : a - c + b = a + b - c := by
  rw [sub_eq, add_assoc a (-c) b, add_comm (-c) b, ← add_assoc a b (-c), sub_eq]

theorem add_sub_comm' (a b c : K) : a + (b - c) = a + b - c := by
  rw [add_comm a (b - c), add_sub_comm b a c, add_comm b a]

theorem add_sub_add_comm (a b c : K) : a + b - (c + b) = a - c := by
  rw [sub_eq, sub_eq, neg_add_dist, add_comm4 a b (-c) (-b), add_neg_cancel,
    add_zero]

theorem add_sub_add_cancel' (a b : K) : a + b - a = b := by
  rw [add_comm a b, add_sub_cancel]

theorem neg_sub (a b : K) : -(a - b) = b - a := by
  rw [sub_eq, sub_eq, neg_add_dist, neg_neg, add_comm]

theorem add_left_comm (a b c : K) : a + (b + c) = b + (a + c) := by
  rw [← add_assoc a b c, add_comm a b, add_assoc b a c]

theorem add_lt_add_left' {c d : K} (h : c < d) (a : K) : a + c < a + d :=
  ⟨add_le_add_left h.1 a, fun hle => h.2 (add_le_cancel_left hle)⟩

theorem lt_add_right (a b : K) (hb : 0 < b) : a < a + b := by
  have h1 : a + 0 < a + b := add_lt_add_left' hb a
  rwa [add_zero] at h1

theorem add_lt_add_right' {a b : K} (h : a < b) (c : K) : a + c < b + c := by
  have h1 : 0 ≤ b - a := sub_nonneg.mpr h.1
  rw [← add_sub_add_comm b c a] at h1
  refine ⟨sub_nonneg.mp h1, fun hle => ?_⟩
  have h2 := sub_nonneg.mpr hle
  rw [add_sub_add_comm a c b] at h2
  exact h.2 (sub_nonneg.mp h2)

theorem mul_nonneg_iff_pos_right' {a c : K} (ha : 0 < a) : 0 ≤ a * c ↔ 0 ≤ c := by
  constructor
  · intro h
    rw [mul_comm] at h
    exact nonneg_of_mul_nonneg_of_pos h ha
  · intro h; exact mul_nonneg (le_of_lt ha) h

theorem one_le_add_one_iff (u : K) : (1 : K) ≤ 1 + u ↔ 0 ≤ u := by
  constructor
  · intro h
    have h1 := sub_nonneg.mpr h
    rwa [add_sub_add_cancel' 1 u] at h1
  · intro h
    have h1 : 1 + 0 ≤ 1 + u := add_le_add_left h 1
    rwa [add_zero] at h1

theorem inv_le_inv {a b : K} (ha : 0 < a) (hab : a ≤ b) : b⁻¹ ≤ a⁻¹ := by
  have hb : 0 < b := lt_of_lt_of_le ha hab
  have hne_b : b ≠ 0 := ne_of_gt hb
  have hne_a : a ≠ 0 := ne_of_gt ha
  have h1 : a * b⁻¹ ≤ b * b⁻¹ :=
    mul_le_mul_of_nonneg_right hab (le_of_lt (inv_pos hb))
  rw [mul_inv_cancel_field hne_b] at h1
  have h2 : b⁻¹ * a ≤ 1 := by rw [mul_comm]; exact h1
  have h3 : b⁻¹ * a * a⁻¹ ≤ 1 * a⁻¹ :=
    mul_le_mul_of_nonneg_right h2 (le_of_lt (inv_pos ha))
  rw [mul_assoc, mul_inv_cancel_field hne_a, mul_one, one_mul'] at h3
  exact h3

theorem div_mul_cancel_right {b : K} (hb : b ≠ 0) (a : K) (c : K) :
    a / b * (b * c) = a * c := by
  rw [div_eq, mul_assoc, ← mul_assoc b⁻¹ b c, mul_inv_cancel' hb, one_mul']

theorem div_mul_cancel_left' {b : K} (hb : b ≠ 0) (a : K) (c : K) :
    a / b * (c * b) = a * c := by
  rw [mul_comm c b]; exact div_mul_cancel_right hb a c

theorem div_le_div_cross {a b c d : K} (hb : 0 < b) (hd : 0 < d) :
    a / b ≤ c / d ↔ a * d ≤ c * b := by
  have hneb : b ≠ 0 := ne_of_gt hb
  have hned : d ≠ 0 := ne_of_gt hd
  have hbd : 0 < b * d := mul_pos hb hd
  have hnebd : b * d ≠ 0 := ne_of_gt hbd
  have e1 : a / b * (b * d) = a * d := div_mul_cancel_right hneb a d
  have e2 : c / d * (b * d) = c * b := by
    rw [mul_comm b d]; exact div_mul_cancel_right hned c b
  constructor
  · intro h
    have h1 := mul_le_mul_of_nonneg_right h (le_of_lt hbd)
    rw [e1, e2] at h1
    exact h1
  · intro h
    have h1 : a * d / (b * d) ≤ c * b / (b * d) :=
      div_le_div_right hbd h
    have ea : a * d / (b * d) = a / b := by
      refine mul_right_cancel' hnebd ?_
      rw [div_mul_cancel hnebd (a * d)]
      exact e1.symm
    have eb : c * b / (b * d) = c / d := by
      refine mul_right_cancel' hnebd ?_
      rw [div_mul_cancel hnebd (c * b)]
      exact e2.symm
    rw [ea, eb] at h1
    exact h1

theorem mul_div_assoc' (a b c : K) (_hb : b ≠ 0) : a / b * c = a * c / b := by
  rw [div_eq, div_eq, mul_assoc a b⁻¹ c, mul_comm b⁻¹ c, ← mul_assoc a c b⁻¹]

theorem div_eq_div_iff {a b c d : K} (hb : b ≠ 0) (hd : d ≠ 0) :
    a / b = c / d ↔ a * d = c * b := by
  have hbd : b * d ≠ 0 := by
    intro h0
    cases eq_zero_or_eq_zero_of_mul_eq_zero h0 with
    | inl h' => exact hb h'
    | inr h' => exact hd h'
  constructor
  · intro h
    have h1 : a / b * (b * d) = c / d * (b * d) := by rw [h]
    rw [div_mul_cancel_right hb a d, mul_comm b d,
      div_mul_cancel_right hd c b] at h1
    exact h1
  · intro h
    refine (mul_right_cancel' hbd) ?_
    rw [mul_comm b d, div_mul_cancel_left' hb a d,
      div_mul_cancel_right hd c b]
    exact h

theorem div_le_iff {a b c : K} (hc : 0 < c) : a / c ≤ b ↔ a ≤ b * c := by
  have hb1 : b / 1 = b := by rw [div_eq, inv_one, mul_one]
  constructor
  · intro h
    have h2 : a / c ≤ b / 1 := by rw [hb1]; exact h
    have h3 := (div_le_div_cross hc zero_lt_one).mp h2
    rwa [mul_one] at h3
  · intro h
    have h2 : a / c ≤ b / 1 :=
      (div_le_div_cross hc zero_lt_one).mpr (by rw [mul_one]; exact h)
    rwa [hb1] at h2

theorem le_div_iff {a b c : K} (hc : 0 < c) : b ≤ a / c ↔ b * c ≤ a := by
  have hb1 : b / 1 = b := by rw [div_eq, inv_one, mul_one]
  constructor
  · intro h
    have h2 : b / 1 ≤ a / c := by rw [hb1]; exact h
    have h3 := (div_le_div_cross zero_lt_one hc).mp h2
    rwa [mul_one] at h3
  · intro h
    have h2 : b / 1 ≤ a / c :=
      (div_le_div_cross zero_lt_one hc).mpr (by rw [mul_one]; exact h)
    rwa [hb1] at h2

theorem div_lt_iff {a b c : K} (hc : 0 < c) : a / c < b ↔ a < b * c := by
  constructor
  · intro h
    exact ⟨(div_le_iff hc).mp h.1, fun hne => h.2 ((le_div_iff hc).mpr hne)⟩
  · intro h
    refine ⟨(div_le_iff hc).mpr (le_of_lt h), fun hle => ?_⟩
    exact h.2 ((le_div_iff hc).mp hle)

theorem lt_div_iff {a b c : K} (hc : 0 < c) : b < a / c ↔ b * c < a := by
  constructor
  · intro h
    refine ⟨(le_div_iff hc).mp h.1, fun hle => h.2 ((div_le_iff hc).mpr hle)⟩
  · intro h
    refine ⟨(le_div_iff hc).mpr (le_of_lt h), fun hle => ?_⟩
    exact h.2 ((div_le_iff hc).mp hle)

theorem div_add_div {a b c d : K} (hb : b ≠ 0) (hd : d ≠ 0) :
    a / b + c / d = (a * d + c * b) / (b * d) := by
  have hbd : b * d ≠ 0 := by
    intro h
    cases eq_zero_or_eq_zero_of_mul_eq_zero h with
    | inl h' => exact hb h'
    | inr h' => exact hd h'
  refine (mul_right_cancel' hbd ?_).symm
  rw [div_mul_cancel hbd (a * d + c * b), right_distrib,
    div_mul_cancel_right hb a d, div_mul_cancel_left' hd c b]

theorem div_add_div_same {a b c : K} (_hc : c ≠ 0) : a / c + b / c = (a + b) / c := by
  rw [div_eq, div_eq, div_eq, ← right_distrib]

theorem div_inv {a b : K} (ha : a ≠ 0) (hb : b ≠ 0) : (a / b)⁻¹ = b / a := by
  have hab : a / b ≠ 0 := by
    intro h
    have h1 : (a / b) * b = a := div_mul_cancel hb a
    rw [h, zero_mul] at h1
    exact ha h1.symm
  refine mul_left_cancel hab ?_
  rw [mul_inv_cancel_field hab, div_eq b a, div_mul_cancel_right hb a a⁻¹,
    mul_inv_cancel_field ha]

theorem div_nonneg {a b : K} (ha : 0 ≤ a) (hb : 0 < b) : 0 ≤ a / b := by
  rw [div_eq]; exact mul_nonneg ha (le_of_lt (inv_pos hb))

theorem mul_le_mul_of_neg_right {a b c : K} (h : a ≤ b) (hc : c < 0) :
    b * c ≤ a * c := by
  have h1 : 0 ≤ (b - a) * (-c) :=
    mul_nonneg (sub_nonneg.mpr h) (neg_nonneg' (le_of_lt hc))
  have h2 : (b - a) * (-c) = -((b - a) * c) := by rw [mul_neg]
  rw [h2] at h1
  have h3 : (b - a) * c ≤ 0 := by
    have h4 := neg_le_neg h1
    rw [neg_neg, neg_zero] at h4
    exact h4
  have h5 : b * c - a * c ≤ 0 := by rw [← sub_mul]; exact h3
  exact sub_nonneg.mp (by rw [← neg_sub (b * c) (a * c)]; exact neg_nonneg' h5)

theorem mul_lt_mul_of_neg_right {a b c : K} (h : a < b) (hc : c < 0) :
    b * c < a * c := by
  have h1 : -b < -a := neg_lt_neg' h
  have h2 : -b * -c < -a * -c := mul_lt_mul_of_pos_right h1 (neg_pos' hc)
  rw [neg_mul_neg, neg_mul_neg] at h2
  exact h2

/-- Own natural-number cast: the only raw numerals used are `0` and `1`. -/
def natK : Nat → K
  | 0 => 0
  | n + 1 => natK n + 1

@[simp] theorem natK_zero : natK 0 = (0 : K) := rfl
@[simp] theorem natK_succ {K : Type} [OrdField K] (n : Nat) :
    natK (n + 1) = (natK n + 1 : K) := rfl
theorem natK_one : natK 1 = (1 : K) := by
  rw [show (1 : Nat) = 0 + 1 from rfl, natK_succ, natK_zero, zero_add]

theorem natK_nonneg {K : Type} [OrdField K] (n : Nat) : (0 : K) ≤ natK n := by
  induction n with
  | zero => exact le_refl (0 : K)
  | succ m ih => exact add_le_add_of_nonneg ih zero_le_one'

theorem natK_pos {K : Type} [OrdField K] {n : Nat} (hn : 0 < n) : (0 : K) < natK n := by
  cases n with
  | zero => exact absurd hn (by omega)
  | succ m =>
      have h1 : (0 : K) + 1 ≤ natK m + 1 :=
        add_le_add (natK_nonneg m) (le_refl (1 : K))
      rw [zero_add] at h1
      exact lt_of_lt_of_le zero_lt_one h1

theorem natK_ne_zero {K : Type} [OrdField K] {n : Nat} (hn : n ≠ 0) : natK n ≠ (0 : K) :=
  ne_of_gt (natK_pos (Nat.pos_of_ne_zero hn))

theorem natK_two_pos {K : Type} [OrdField K] : (0 : K) < natK 2 :=
  natK_pos (n := 2) (by omega)
theorem natK_two_ne_zero {K : Type} [OrdField K] : natK 2 ≠ (0 : K) :=
  natK_ne_zero (n := 2) (by omega)
theorem natK_five_pos {K : Type} [OrdField K] : (0 : K) < natK 5 :=
  natK_pos (n := 5) (by omega)
theorem natK_five_ne_zero {K : Type} [OrdField K] : natK 5 ≠ (0 : K) :=
  natK_ne_zero (n := 5) (by omega)
theorem natK_ten_pos {K : Type} [OrdField K] : (0 : K) < natK 10 :=
  natK_pos (n := 10) (by omega)
theorem natK_ten_ne_zero {K : Type} [OrdField K] : natK 10 ≠ (0 : K) :=
  natK_ne_zero (n := 10) (by omega)

theorem natK_add {K : Type} [OrdField K] (m n : Nat) :
    natK (m + n) = (natK m + natK n : K) := by
  induction n with
  | zero => rw [Nat.add_zero, natK_zero, add_zero]
  | succ k ih => rw [Nat.add_succ, natK_succ, natK_succ, ih, add_assoc]

theorem natK_mul {K : Type} [OrdField K] (m n : Nat) :
    natK (m * n) = (natK m * natK n : K) := by
  induction n with
  | zero => rw [Nat.mul_zero, natK_zero, mul_zero]
  | succ k ih =>
      rw [Nat.mul_succ, natK_add, ih, natK_succ, left_distrib, mul_one]

theorem natK_le {K : Type} [OrdField K] {m n : Nat} (h : m ≤ n) :
    (natK m : K) ≤ natK n := by
  cases Nat.le.dest h with
  | intro k hk => rw [← hk, natK_add]; exact le_add_right (natK m) (natK k) (natK_nonneg k)

theorem natK_lt_succ {K : Type} [OrdField K] (m : Nat) : (natK m : K) < natK (m + 1) := by
  have h1 : natK m + (0 : K) < natK m + (1 : K) :=
    add_lt_add_left' zero_lt_one (natK m)
  rwa [add_zero] at h1

theorem natK_lt_of_lt {K : Type} [OrdField K] {m n : Nat} (h : m < n) :
    (natK m : K) < natK n := by
  have hle : m ≤ n := by omega
  cases Nat.le.dest hle with
  | intro k hk =>
      rw [← hk, natK_add]
      have hk1 : 1 ≤ k := by omega
      have h1 : (1 : K) ≤ natK k := by rw [← natK_one]; exact natK_le hk1
      exact lt_add_right (natK m) (natK k) (lt_of_lt_of_le zero_lt_one h1)

theorem natK_le_iff {K : Type} [OrdField K] {m n : Nat} : (natK m : K) ≤ natK n ↔ m ≤ n := by
  constructor
  · intro h
    by_cases hmn : m ≤ n
    · exact hmn
    · exact absurd h (not_le_of_lt (natK_lt_of_lt (by omega)))
  · intro h
    exact natK_le h

theorem natK_lt_iff {K : Type} [OrdField K] {m n : Nat} :
    (natK m : K) < natK n ↔ m < n := by
  constructor
  · intro h
    by_cases hmn : m < n
    · exact hmn
    · have hnm : n ≤ m := by omega
      by_cases hne : m = n
      · rw [hne] at h; exact absurd h (lt_irrefl (natK n))
      · exact absurd h.1 (not_le_of_lt (natK_lt_of_lt (by omega)))
  · intro h
    exact natK_lt_of_lt h


theorem two_mul (a : K) : natK 2 * a = a + a := by
  rw [natK_succ, natK_succ, natK_zero, zero_add, right_distrib, one_mul']

theorem midpoint_lt (a b : K) (h : b < a) :
    (a + b) / natK 2 < a ∧ b < (a + b) / natK 2 := by
  constructor
  · refine (div_lt_iff natK_two_pos).mpr ?_
    rw [mul_comm, two_mul]
    exact add_lt_add_left' h a
  · refine (lt_div_iff natK_two_pos).mpr ?_
    rw [mul_comm, two_mul]
    exact add_lt_add_right' h b

theorem cross_sum (w1 w2 A B : K) :
    w1 * A + w2 * B + (w1 * B + w2 * A) = (w1 + w2) * (A + B) := by
  rw [left_distrib (w1 + w2) A B, right_distrib w1 w2 A, right_distrib w1 w2 B,
    add_comm4 (w1 * A) (w2 * B) (w1 * B) (w2 * A), add_comm (w2 * B) (w2 * A),
    add_comm4 (w1 * A) (w1 * B) (w2 * A) (w2 * B)]

theorem lambda_handshake (w1 w2 u1 u2 : K) (hw : w1 + w2 = 1) :
    w1 * (1 + u1) + w2 * (1 + u2) = 1 + (w1 * u1 + w2 * u2) := by
  rw [left_distrib, left_distrib, mul_one, mul_one,
    add_comm4 w1 (w1 * u1) w2 (w2 * u2), hw]

theorem div_mul_div {a b c d : K} (hb : b ≠ 0) (hd : d ≠ 0) :
    a / b * (c / d) = a * c / (b * d) := by
  have hbd : b * d ≠ 0 := by
    intro h
    cases eq_zero_or_eq_zero_of_mul_eq_zero h with
    | inl h' => exact hb h'
    | inr h' => exact hd h'
  refine mul_right_cancel' hbd ?_
  rw [div_mul_cancel hbd (a * c), mul_assoc (a / b) (c / d) (b * d),
    mul_comm b d, div_mul_cancel_right hd c b, mul_comm c b,
    div_mul_cancel_right hb a c]

theorem div_div_same_denom {a c b : K} (hb : b ≠ 0) (hc : c ≠ 0) :
    a / b / (c / b) = a / c := by
  have hbc : b * c ≠ 0 := by
    intro h0
    cases eq_zero_or_eq_zero_of_mul_eq_zero h0 with
    | inl h' => exact hb h'
    | inr h' => exact hc h'
  refine (mul_right_cancel' hbc) ?_
  rw [div_eq, div_inv hc hb, div_mul_div hb hc, div_mul_cancel hbc (a * b),
    mul_comm b c, div_mul_cancel_right hc a b]

/-! ### Powers -/

/-- Own power recursion (no `Monoid`/`pow` on the bare interface). -/
def npow (x : K) : Nat → K
  | 0 => 1
  | n + 1 => x * npow x n

@[simp] theorem npow_zero (x : K) : npow x 0 = 1 := rfl
@[simp] theorem npow_succ (x : K) (n : Nat) : npow x (n + 1) = x * npow x n := rfl

theorem npow_one_pow (n : Nat) : npow (1 : K) n = 1 := by
  induction n with
  | zero => rfl
  | succ k ih => rw [npow_succ, ih, mul_one]

theorem npow_nonneg {x : K} (hx : 0 ≤ x) (n : Nat) : 0 ≤ npow x n := by
  induction n with
  | zero => exact zero_le_one'
  | succ m ih => exact mul_nonneg hx ih

theorem npow_pos {x : K} (hx : 0 < x) (n : Nat) : 0 < npow x n := by
  induction n with
  | zero => exact zero_lt_one
  | succ m ih => exact mul_pos hx ih

theorem npow_le_one {x : K} (hx : 0 ≤ x) (hx1 : x ≤ 1) (n : Nat) : npow x n ≤ 1 := by
  induction n with
  | zero => exact le_refl (1 : K)
  | succ m ih =>
      have h1 : x * npow x m ≤ 1 * npow x m :=
        mul_le_mul_of_nonneg_right hx1 (npow_nonneg hx m)
      rw [one_mul'] at h1
      exact le_trans h1 ih

theorem npow_mono {a b : K} (h : a ≤ b) (ha : 0 ≤ a) (n : Nat) :
    npow a n ≤ npow b n := by
  induction n with
  | zero => exact le_refl (1 : K)
  | succ m ih =>
      have h1 : a * npow a m ≤ b * npow a m :=
        mul_le_mul_of_nonneg_right h (npow_nonneg ha m)
      have h2 : b * npow a m ≤ b * npow b m :=
        mul_le_mul_of_nonneg_left ih (le_trans ha h)
      rw [npow_succ, npow_succ]
      exact le_trans h1 h2

theorem npow_ge_one {x : K} (hx : 1 ≤ x) (n : Nat) : 1 ≤ npow x n := by
  have hx0 : 0 ≤ x := le_trans zero_le_one' hx
  induction n with
  | zero => exact le_refl (1 : K)
  | succ k ih =>
      have h1 : x * 1 ≤ x * npow x k := mul_le_mul_of_nonneg_left ih hx0
      rw [mul_one] at h1
      exact le_trans hx h1

theorem npow_addexp (x : K) (m n : Nat) :
    npow x (m + n) = npow x m * npow x n := by
  induction n with
  | zero => rw [Nat.add_zero, npow_zero, mul_one]
  | succ k ih =>
      rw [Nat.add_succ, npow_succ, npow_succ, ih,
        ← mul_assoc x (npow x m) (npow x k), mul_comm x (npow x m),
        mul_assoc (npow x m) x (npow x k)]

theorem npow_mul_base (x y : K) (n : Nat) :
    npow (x * y) n = npow x n * npow y n := by
  induction n with
  | zero => rw [npow_zero, npow_zero, npow_zero, mul_one]
  | succ k ih =>
      rw [npow_succ, npow_succ, npow_succ, ih,
        mul_assoc x y (npow x k * npow y k), ← mul_assoc y (npow x k) (npow y k),
        mul_comm y (npow x k), mul_assoc (npow x k) y (npow y k),
        ← mul_assoc x (npow x k) (y * npow y k)]

theorem eq_inv_of_mul_eq_one {a b : K} (h : a * b = 1) : a = b⁻¹ := by
  have hb : b ≠ 0 := by
    intro hb0
    rw [hb0, mul_zero] at h
    exact zero_ne_one' h
  have h1 : a * b * b⁻¹ = 1 * b⁻¹ := by rw [h]
  rw [mul_assoc, mul_inv_cancel_field hb, mul_one, one_mul'] at h1
  exact h1

theorem mul_inv_rev (a b : K) : (a * b)⁻¹ = a⁻¹ * b⁻¹ := by
  by_cases hb : b = 0
  · rw [hb, mul_zero, invz, mul_zero]
  · by_cases ha : a = 0
    · rw [ha, zero_mul, invz, zero_mul]
    · refine (eq_inv_of_mul_eq_one ?_).symm
      have e1 : b⁻¹ * (a * b) = a := by
        rw [← mul_assoc b⁻¹ a b, mul_comm b⁻¹ a, mul_assoc a b⁻¹ b,
          mul_inv_cancel' hb, mul_one]
      rw [mul_assoc a⁻¹ b⁻¹ (a * b), e1, mul_inv_cancel' ha]

theorem npow_ne_zero {b : K} (hb : b ≠ 0) (n : Nat) : npow b n ≠ 0 := by
  intro h
  have h1 : npow b n * npow b⁻¹ n = 1 := by
    rw [← npow_mul_base, mul_inv_cancel_field hb, npow_one_pow]
  rw [h, zero_mul] at h1
  exact zero_ne_one' h1

theorem npow_div {a b : K} (hb : b ≠ 0) (n : Nat) :
    npow (a / b) n = npow a n / npow b n := by
  induction n with
  | zero =>
      rw [npow_zero, npow_zero, npow_zero,
        div_self ((zero_ne_one' (K := K)).symm)]
  | succ k ih =>
      rw [npow_succ, npow_succ, ih, div_mul_div hb (npow_ne_zero hb k), npow_succ]

theorem npow_natK {K : Type} [OrdField K] (n m : Nat) :
    npow (natK n) m = (natK (n ^ m) : K) := by
  induction m with
  | zero => rw [npow_zero, Nat.pow_zero, natK_one]
  | succ k ih =>
      rw [npow_succ, ih, Nat.pow_succ, natK_mul, mul_comm (natK n) (natK (n ^ k))]

theorem npow_inv (x : K) (n : Nat) : npow x⁻¹ n = (npow x n)⁻¹ := by
  induction n with
  | zero => rw [npow_zero, npow_zero, inv_one]
  | succ k ih =>
      rw [npow_succ, npow_succ, ih, ← mul_inv_rev]

theorem npow_le_exp {x : K} (hx1 : 1 ≤ x) {m n : Nat} (hmn : m ≤ n) :
    npow x m ≤ npow x n := by
  cases Nat.le.dest hmn with
  | intro k hk =>
      have hx0 : 0 ≤ x := le_trans zero_le_one' hx1
      rw [← hk, npow_addexp]
      have h1 : npow x m * 1 ≤ npow x m * npow x k :=
        mul_le_mul_of_nonneg_left (npow_ge_one hx1 k) (npow_nonneg hx0 m)
      rw [mul_one] at h1
      exact h1

theorem npow_le_of_le_one {x : K} (hx : 0 ≤ x) (hx1 : x ≤ 1) {m n : Nat}
    (hmn : m ≤ n) : npow x n ≤ npow x m := by
  cases Nat.le.dest hmn with
  | intro k hk =>
      rw [← hk, npow_addexp]
      have h1 : npow x m * npow x k ≤ npow x m * 1 :=
        mul_le_mul_of_nonneg_left (npow_le_one hx hx1 k) (npow_nonneg hx m)
      rw [mul_one] at h1
      exact h1

/-- The Bernoulli-type product bound: `(1+x)^m (1 - m x) ≤ 1` for
`x ≥ 0`.  This is the engine of the `∀m` false-certification family of
Theorem S2(ii). -/
theorem sub_add_eq {a b c : K} (h : a + b = c) : c - a = b := by
  rw [← h, add_comm a b, add_sub_cancel]

theorem sub_add_add_cancel (a b c : K) : a - (b + c) + c = a - b := by
  rw [sub_eq, neg_add_dist, ← add_assoc a (-b) (-c),
    add_assoc (a + -b) (-c) c, neg_add_cancel, add_zero, sub_eq]

theorem bernoulli_upper (x : K) (hx : 0 ≤ x) (m : Nat) :
    npow (1 + x) m * (1 - natK m * x) ≤ 1 := by
  induction m with
  | zero => rw [npow_zero, natK_zero, zero_mul, sub_zero, mul_one]; exact le_refl 1
  | succ k ih =>
      have hnkk : (0 : K) ≤ natK k + 1 :=
        le_trans (natK_nonneg k) (le_add_right (natK k) 1 zero_le_one')
      have e1 : (natK k + 1) * x = natK k * x + x := by
        rw [right_distrib, one_mul']
      have e2 : (natK k + 1) * (x * x) = natK k * x * x + x * x := by
        rw [right_distrib, one_mul', ← mul_assoc (natK k) x x]
      have e3 : x * (natK k * x + x) = natK k * x * x + x * x := by
        calc x * (natK k * x + x) = x * (natK k * x) + x * x :=
              left_distrib x (natK k * x) x
          _ = (natK k * x) * x + x * x := by rw [mul_comm x (natK k * x)]
          _ = natK k * x * x + x * x := rfl
      have e : (1 + x) * (1 - (natK k + 1) * x) + (natK k + 1) * (x * x)
          = 1 - natK k * x := by
        rw [mul_sub, mul_one, e1, right_distrib, one_mul', e3, e2,
          sub_add_add_cancel (1 + x) (natK k * x + x)
            (natK k * x * x + x * x),
          add_sub_add_comm 1 x (natK k * x)]
      have hpos : 0 ≤ (natK k + 1) * (x * x) :=
        mul_nonneg hnkk (mul_nonneg hx hx)
      have key : (1 + x) * (1 - (natK k + 1) * x) ≤ 1 - natK k * x :=
        sub_nonneg.mp (by rw [sub_add_eq e]; exact hpos)
      rw [npow_succ, natK_succ]
      have step : (1 + x) * npow (1 + x) k * (1 - (natK k + 1) * x)
          ≤ npow (1 + x) k * (1 - natK k * x) := by
        calc (1 + x) * npow (1 + x) k * (1 - (natK k + 1) * x)
            = npow (1 + x) k * ((1 + x) * (1 - (natK k + 1) * x)) := by
              rw [mul_assoc (1 + x) (npow (1 + x) k) (1 - (natK k + 1) * x),
                mul_comm (1 + x) (npow (1 + x) k * (1 - (natK k + 1) * x)),
                mul_assoc (npow (1 + x) k) (1 - (natK k + 1) * x) (1 + x),
                mul_comm (1 - (natK k + 1) * x) (1 + x)]
          _ ≤ npow (1 + x) k * (1 - natK k * x) :=
              mul_le_mul_of_nonneg_left key
                (npow_nonneg (le_trans zero_le_one' (le_add_right 1 x hx)) k)
      exact le_trans step ih

/-! ## The witness datum (Section 4.5)

The datum is a concrete finite object: a reserve stock `x` and two typed
floors `s₁ s₂` on the `q = 0` slice, the four deterministic actions of
the menu (NO-SWITCH, FAST, SLOW, STAGED) with dip depth 2, the
destination reset applying the gain `e = (1/4, 1/4)` componentwise, and
rescue cost `c = 1`.  The worst-case tubes are the *exact* visited sets
(the trajectories are piecewise monotone).  The floor-referenced indices
of the substitutability extension are `λᵢ = 1 + sᵢ`. -/

/-- The destination-reset gain `e = 1/4` (any strictly positive `e`
gives the same accepted sets; the datum fixes `1/4`). -/
def eGain {K : Type} [OrdField K] : K := natK 1 / natK 4

theorem eGain_nonneg {K : Type} [OrdField K] : (0 : K) ≤ eGain :=
  div_nonneg (natK_nonneg 1) (natK_pos (by omega))

/-- A witness-datum state on the `q = 0` slice. -/
structure WitState (K : Type) where
  x : K
  s1 : K
  s2 : K

/-- The deterministic menu of Section 4.5. -/
inductive DetAct where
  | noswitch | fast | slow | staged

/-- The menu plus the convexified blend family of Section 4.10. -/
inductive WitAct (K : Type) where
  | det : DetAct → WitAct K
  | blend : K → WitAct K

/-- NO-SWITCH tube: the state is constant. -/
def nsTube (z p : WitState K) : Prop := p = z

/-- FAST tube: dip of depth 2 in `s₁`; `s₂`, `x` constant. -/
def fastTube (z p : WitState K) : Prop :=
  p.x = z.x ∧ p.s2 = z.s2 ∧ z.s1 - natK 2 ≤ p.s1 ∧ p.s1 ≤ z.s1

/-- SLOW tube: symmetric in `s₂`. -/
def slowTube (z p : WitState K) : Prop :=
  p.x = z.x ∧ p.s1 = z.s1 ∧ z.s2 - natK 2 ≤ p.s2 ∧ p.s2 ≤ z.s2

/-- STAGED tube: `x` descends by the rescue cost 1; both floors grow by
the gain `e`. -/
def stagedTube (z p : WitState K) : Prop :=
  z.x - 1 ≤ p.x ∧ p.x ≤ z.x ∧ z.s1 ≤ p.s1 ∧ p.s1 ≤ z.s1 + eGain ∧
    z.s2 ≤ p.s2 ∧ p.s2 ≤ z.s2 + eGain

/-- BLEND δ tube: the pointwise convex combination of the FAST and SLOW
tubes (the explicit model assumption of Section 4.10). -/
def blendTube (δ : K) (z p : WitState K) : Prop :=
  p.x = z.x ∧ z.s1 - natK 2 * δ ≤ p.s1 ∧ p.s1 ≤ z.s1 ∧
    z.s2 - natK 2 * (1 - δ) ≤ p.s2 ∧ p.s2 ≤ z.s2

/-- The worst-case tube of an action: the exact set of visited states. -/
def witTube : WitAct K → WitState K → WitState K → Prop
  | .det .noswitch, z, p => nsTube z p
  | .det .fast, z, p => fastTube z p
  | .det .slow, z, p => slowTube z p
  | .det .staged, z, p => stagedTube z p
  | .blend δ, z, p => blendTube δ z p

/-- The destination-labelled successor: the phase label `true` is
`q = 1`; NO-SWITCH stays in phase `q = 0` and so never reaches the
destination set.  The reset applies the gain `e` componentwise. -/
def witSucc : WitAct K → WitState K → Bool × WitState K
  | .det .noswitch, z => (false, z)
  | .det .fast, z => (true, ⟨z.x, z.s1 + eGain, z.s2 + eGain⟩)
  | .det .slow, z => (true, ⟨z.x, z.s1 + eGain, z.s2 + eGain⟩)
  | .det .staged, z => (true, ⟨z.x - 1, z.s1 + eGain, z.s2 + eGain⟩)
  | .blend _, z => (true, ⟨z.x, z.s1 + eGain, z.s2 + eGain⟩)

/-- Endpoint set of a deterministic action: FAST and SLOW return to the
initial floor values (V-shaped trajectories), STAGED runs from `(x, s)`
to `(x - 1, s + e)`. -/
def witEnd : DetAct → WitState K → WitState K → Prop
  | .noswitch, z, p => p = z
  | .fast, z, p => p = z
  | .slow, z, p => p = z
  | .staged, z, p => p = z ∨ p = ⟨z.x - 1, z.s1 + eGain, z.s2 + eGain⟩

/-- `S₀`: the typed transition-safe set. -/
def inS (p : WitState K) : Prop := 0 ≤ p.x ∧ 0 ≤ p.s1 ∧ 0 ≤ p.s2

/-- `Sphys`: the physical constraint (the reserve stock only). -/
def inSphys (p : WitState K) : Prop := 0 ≤ p.x

/-- `S^w`: the scalarized safe set. -/
def inSw (w1 w2 : K) (p : WitState K) : Prop :=
  0 ≤ p.x ∧ 0 ≤ w1 * p.s1 + w2 * p.s2

/-- `G`: the typed destination set. -/
def inG (b : Bool) (p : WitState K) : Prop := b = true ∧ inS p

/-- `Gphys`. -/
def inGphys (b : Bool) (p : WitState K) : Prop := b = true ∧ 0 ≤ p.x

/-- The five operators' shared shape: tube condition plus successor
condition, at the respective constraint structures. -/
def SuccTyped (a : WitAct K) (z : WitState K) : Prop :=
  (witSucc a z).1 = true ∧ 0 ≤ (witSucc a z).2.x ∧ 0 ≤ (witSucc a z).2.s1
    ∧ 0 ≤ (witSucc a z).2.s2

def SuccW (w1 w2 : K) (a : WitAct K) (z : WitState K) : Prop :=
  (witSucc a z).1 = true ∧ 0 ≤ (witSucc a z).2.x
    ∧ 0 ≤ w1 * (witSucc a z).2.s1 + w2 * (witSucc a z).2.s2

def SuccPhys (a : WitAct K) (z : WitState K) : Prop :=
  (witSucc a z).1 = true ∧ 0 ≤ (witSucc a z).2.x

/-- `E_typ`: the noncompensatory typed operator. -/
def TypedAdm (a : WitAct K) (z : WitState K) : Prop :=
  (∀ p, witTube a z p → inS p) ∧ SuccTyped a z

/-- `E_w`: the scalarized aggregate operator at a cone weight. -/
def WAdm (w1 w2 : K) (a : WitAct K) (z : WitState K) : Prop :=
  (∀ p, witTube a z p → inSw w1 w2 p) ∧ SuccW w1 w2 a z

/-- `E_tube,phys`. -/
def PhysAdm (a : DetAct) (z : WitState K) : Prop :=
  (∀ p, witTube (.det a) z p → inSphys p) ∧ SuccPhys (.det a) z

/-- `E_end`: the endpoint-only physical operator. -/
def EndAdm (a : DetAct) (z : WitState K) : Prop :=
  (∀ p, witEnd a z p → inSphys p) ∧ SuccPhys (.det a) z

/-- `W₊`: the full nonnegative scalarization cone minus the origin. -/
def WPos (w1 w2 : K) : Prop := 0 ≤ w1 ∧ 0 ≤ w2 ∧ (w1 ≠ 0 ∨ w2 ≠ 0)

/-- The initial state set `X₀`. -/
def InX0 (z : WitState K) : Prop := inS z

/-- The accepted-state sets: `V[E] = {z : E(z) ≠ ∅}`. -/
def VTyp (z : WitState K) : Prop := ∃ a : DetAct, TypedAdm (.det a) z
def VW (w1 w2 : K) (z : WitState K) : Prop := ∃ a : DetAct, WAdm w1 w2 (.det a) z
def VWeak (z : WitState K) : Prop := ∀ w1 w2, WPos w1 w2 → VW w1 w2 z
def VPhys (z : WitState K) : Prop := ∃ a : DetAct, PhysAdm a z
def VEnd (z : WitState K) : Prop := ∃ a : DetAct, EndAdm a z

/-- The impossibility region core `I` (Theorem 5's `I = Q ∩ {x < 1}`,
on the universe `X₀`). -/
def IsGap (z : WitState K) : Prop :=
  z.x < 1 ∧ z.s1 < natK 2 ∧ z.s2 < natK 2 ∧ natK 2 ≤ z.s1 + z.s2

/-- The genuine acceptance gap `FP_agg = V_weak \ V_typ`. -/
def FPAgg (z : WitState K) : Prop := VWeak z ∧ ¬ VTyp z

/-- The typed operator of the menu augmented by the blend family. -/
def VTypBlend (z : WitState K) : Prop :=
  VTyp z ∨ ∃ δ, 0 ≤ δ ∧ δ ≤ 1 ∧ TypedAdm (.blend δ) z

/-! ### Per-action characterizations -/

theorem typedAdm_fast_iff (z : WitState K) :
    TypedAdm (.det .fast) z ↔ (0 ≤ z.x ∧ 0 ≤ z.s2 ∧ natK 2 ≤ z.s1) := by
  constructor
  · intro h
    have hdip : witTube (.det .fast) z ⟨z.x, z.s1 - natK 2, z.s2⟩ :=
      ⟨rfl, rfl, le_refl _, sub_le_self z.s1 (natK 2) (natK_nonneg 2)⟩
    have h1 := h.1 _ hdip
    have hz : witTube (.det .fast) z z :=
      ⟨rfl, rfl, sub_le_self z.s1 (natK 2) (natK_nonneg 2), le_refl _⟩
    have h2 := h.1 _ hz
    exact ⟨h2.1, h2.2.2, sub_nonneg.mp h1.2.1⟩
  · intro h
    constructor
    · intro p hp
      have hs1m : 0 ≤ z.s1 - natK 2 := sub_nonneg.mpr h.2.2
      refine ⟨?_, ?_, ?_⟩
      · rw [hp.1]; exact h.1
      · exact le_trans hs1m hp.2.2.1
      · rw [hp.2.1]; exact h.2.1
    · refine ⟨rfl, h.1, ?_, ?_⟩
      · exact add_le_add_of_nonneg (le_trans (natK_nonneg 2) h.2.2) eGain_nonneg
      · exact add_le_add_of_nonneg h.2.1 eGain_nonneg

theorem typedAdm_slow_iff (z : WitState K) :
    TypedAdm (.det .slow) z ↔ (0 ≤ z.x ∧ 0 ≤ z.s1 ∧ natK 2 ≤ z.s2) := by
  constructor
  · intro h
    have hdip : witTube (.det .slow) z ⟨z.x, z.s1, z.s2 - natK 2⟩ :=
      ⟨rfl, rfl, le_refl _, sub_le_self z.s2 (natK 2) (natK_nonneg 2)⟩
    have h1 := h.1 _ hdip
    have hz : witTube (.det .slow) z z :=
      ⟨rfl, rfl, sub_le_self z.s2 (natK 2) (natK_nonneg 2), le_refl _⟩
    have h2 := h.1 _ hz
    exact ⟨h2.1, h2.2.1, sub_nonneg.mp h1.2.2⟩
  · intro h
    constructor
    · intro p hp
      have hs2m : 0 ≤ z.s2 - natK 2 := sub_nonneg.mpr h.2.2
      refine ⟨?_, ?_, ?_⟩
      · rw [hp.1]; exact h.1
      · rw [hp.2.1]; exact h.2.1
      · exact le_trans hs2m hp.2.2.1
    · refine ⟨rfl, h.1, ?_, ?_⟩
      · exact add_le_add_of_nonneg h.2.1 eGain_nonneg
      · exact add_le_add_of_nonneg (le_trans (natK_nonneg 2) h.2.2) eGain_nonneg

theorem typedAdm_staged_iff (z : WitState K) :
    TypedAdm (.det .staged) z ↔ (1 ≤ z.x ∧ 0 ≤ z.s1 ∧ 0 ≤ z.s2) := by
  constructor
  · intro h
    have hbot : witTube (.det .staged) z ⟨z.x - 1, z.s1, z.s2⟩ :=
      ⟨le_refl _, sub_le_self z.x 1 zero_le_one', le_refl _,
        le_add_right z.s1 eGain eGain_nonneg, le_refl _,
        le_add_right z.s2 eGain eGain_nonneg⟩
    have h1 := h.1 _ hbot
    exact ⟨sub_nonneg.mp h1.1, h1.2.1, h1.2.2⟩
  · intro h
    constructor
    · intro p hp
      refine ⟨le_trans (sub_nonneg.mpr h.1) hp.1, ?_, ?_⟩
      · exact le_trans h.2.1 hp.2.2.1
      · exact le_trans h.2.2 hp.2.2.2.2.1
    · refine ⟨rfl, sub_nonneg.mpr h.1, ?_, ?_⟩
      · exact add_le_add_of_nonneg h.2.1 eGain_nonneg
      · exact add_le_add_of_nonneg h.2.2 eGain_nonneg

theorem not_TypedAdm_noswitch (z : WitState K)
    (h : TypedAdm (.det .noswitch) z) : False :=
  Bool.noConfusion h.2.1

theorem not_WAdm_noswitch {w1 w2 : K} (z : WitState K)
    (h : WAdm w1 w2 (.det .noswitch) z) : False :=
  Bool.noConfusion h.2.1

theorem wAdm_fast_iff {w1 w2 : K} (hw : WPos w1 w2) (z : WitState K) :
    WAdm w1 w2 (.det .fast) z ↔ (0 ≤ z.x ∧ 0 ≤ w1 * (z.s1 - natK 2) + w2 * z.s2) := by
  constructor
  · intro h
    have hdip : witTube (.det .fast) z ⟨z.x, z.s1 - natK 2, z.s2⟩ :=
      ⟨rfl, rfl, le_refl _, sub_le_self z.s1 (natK 2) (natK_nonneg 2)⟩
    have h1 := h.1 _ hdip
    exact ⟨h1.1, h1.2⟩
  · intro h
    constructor
    · intro p hp
      refine ⟨?_, ?_⟩
      · rw [hp.1]; exact h.1
      · have e1 : w1 * (z.s1 - natK 2) + w2 * z.s2 ≤ w1 * p.s1 + w2 * p.s2 := by
          have h1 : w1 * (z.s1 - natK 2) ≤ w1 * p.s1 :=
            mul_le_mul_of_nonneg_left hp.2.2.1 hw.1
          have h2 : w2 * z.s2 ≤ w2 * p.s2 := by
            rw [hp.2.1]; exact le_refl _
          exact add_le_add h1 h2
        exact le_trans h.2 e1
    · refine ⟨rfl, h.1, ?_⟩
      have hmin : w1 * (z.s1 - natK 2) + w2 * z.s2
          ≤ w1 * (z.s1 + eGain) + w2 * (z.s2 + eGain) := by
        have h1 : w1 * (z.s1 - natK 2) ≤ w1 * (z.s1 + eGain) := by
          have hsub : z.s1 - natK 2 ≤ z.s1 + eGain :=
            le_trans (sub_le_self z.s1 (natK 2) (natK_nonneg 2))
              (le_add_right z.s1 eGain eGain_nonneg)
          exact mul_le_mul_of_nonneg_left hsub hw.1
        have h2 : w2 * z.s2 ≤ w2 * (z.s2 + eGain) :=
          mul_le_mul_of_nonneg_left (le_add_right z.s2 eGain eGain_nonneg) hw.2.1
        exact add_le_add h1 h2
      exact le_trans h.2 hmin

theorem wAdm_slow_iff {w1 w2 : K} (hw : WPos w1 w2) (z : WitState K) :
    WAdm w1 w2 (.det .slow) z ↔ (0 ≤ z.x ∧ 0 ≤ w1 * z.s1 + w2 * (z.s2 - natK 2)) := by
  constructor
  · intro h
    have hdip : witTube (.det .slow) z ⟨z.x, z.s1, z.s2 - natK 2⟩ :=
      ⟨rfl, rfl, le_refl _, sub_le_self z.s2 (natK 2) (natK_nonneg 2)⟩
    have h1 := h.1 _ hdip
    exact ⟨h1.1, h1.2⟩
  · intro h
    constructor
    · intro p hp
      refine ⟨?_, ?_⟩
      · rw [hp.1]; exact h.1
      · have e1 : w1 * z.s1 + w2 * (z.s2 - natK 2) ≤ w1 * p.s1 + w2 * p.s2 := by
          have h1 : w1 * z.s1 ≤ w1 * p.s1 := by
            rw [hp.2.1]; exact le_refl _
          have h2 : w2 * (z.s2 - natK 2) ≤ w2 * p.s2 :=
            mul_le_mul_of_nonneg_left hp.2.2.1 hw.2.1
          exact add_le_add h1 h2
        exact le_trans h.2 e1
    · refine ⟨rfl, h.1, ?_⟩
      have hmin : w1 * z.s1 + w2 * (z.s2 - natK 2)
          ≤ w1 * (z.s1 + eGain) + w2 * (z.s2 + eGain) := by
        have h1 : w1 * z.s1 ≤ w1 * (z.s1 + eGain) :=
          mul_le_mul_of_nonneg_left (le_add_right z.s1 eGain eGain_nonneg) hw.1
        have h2 : w2 * (z.s2 - natK 2) ≤ w2 * (z.s2 + eGain) := by
          have hsub : z.s2 - natK 2 ≤ z.s2 + eGain :=
            le_trans (sub_le_self z.s2 (natK 2) (natK_nonneg 2))
              (le_add_right z.s2 eGain eGain_nonneg)
          exact mul_le_mul_of_nonneg_left hsub hw.2.1
        exact add_le_add h1 h2
      exact le_trans h.2 hmin

theorem wAdm_staged_iff {w1 w2 : K} (hw : WPos w1 w2) (z : WitState K) :
    WAdm w1 w2 (.det .staged) z ↔ (1 ≤ z.x ∧ 0 ≤ w1 * z.s1 + w2 * z.s2) := by
  constructor
  · intro h
    have hbot : witTube (.det .staged) z ⟨z.x - 1, z.s1, z.s2⟩ :=
      ⟨le_refl _, sub_le_self z.x 1 zero_le_one', le_refl _,
        le_add_right z.s1 eGain eGain_nonneg, le_refl _,
        le_add_right z.s2 eGain eGain_nonneg⟩
    have h1 := h.1 _ hbot
    exact ⟨sub_nonneg.mp h1.1, h1.2⟩
  · intro h
    constructor
    · intro p hp
      refine ⟨le_trans (sub_nonneg.mpr h.1) hp.1, ?_⟩
      exact le_trans h.2 (add_le_add (mul_le_mul_of_nonneg_left hp.2.2.1 hw.1)
        (mul_le_mul_of_nonneg_left hp.2.2.2.2.1 hw.2.1))
    · refine ⟨rfl, sub_nonneg.mpr h.1, ?_⟩
      exact le_trans h.2
        (add_le_add (mul_le_mul_of_nonneg_left (le_add_right z.s1 eGain eGain_nonneg) hw.1)
          (mul_le_mul_of_nonneg_left (le_add_right z.s2 eGain eGain_nonneg) hw.2.1))

theorem typedAdm_blend_iff {δ : K} (z : WitState K) (hδ1 : 0 ≤ δ) (hδ2 : δ ≤ 1)
    (hz : InX0 z) :
    TypedAdm (.blend δ) z ↔ (natK 2 * δ ≤ z.s1 ∧ natK 2 * (1 - δ) ≤ z.s2) := by
  have hdip : witTube (.blend δ) z ⟨z.x, z.s1 - natK 2 * δ, z.s2 - natK 2 * (1 - δ)⟩ :=
    ⟨rfl, le_refl _, sub_le_self z.s1 (natK 2 * δ) (mul_nonneg (natK_nonneg 2) hδ1),
      le_refl _, sub_le_self z.s2 (natK 2 * (1 - δ))
        (mul_nonneg (natK_nonneg 2) (sub_nonneg.mpr hδ2))⟩
  constructor
  · intro h
    have h1 := h.1 _ hdip
    exact ⟨sub_nonneg.mp h1.2.1, sub_nonneg.mp h1.2.2⟩
  · intro h
    constructor
    · intro p hp
      refine ⟨?_, ?_, ?_⟩
      · rw [hp.1]; exact hz.1
      · exact le_trans (sub_nonneg.mpr h.1) hp.2.1
      · exact le_trans (sub_nonneg.mpr h.2) hp.2.2.2.1
    · refine ⟨rfl, hz.1, ?_, ?_⟩
      · exact add_le_add_of_nonneg hz.2.1 eGain_nonneg
      · exact add_le_add_of_nonneg hz.2.2 eGain_nonneg

/-! ## The operator machinery (Remark 2, Proposition 3) -/

/-- **Remark 2** (full-cone scalarization), two-coordinate instance:
nonnegativity is exactly nonnegativity of every cone scalarization. -/
theorem remark2 (v1 v2 : K) :
    (0 ≤ v1 ∧ 0 ≤ v2) ↔ ∀ w1 w2, WPos w1 w2 → 0 ≤ w1 * v1 + w2 * v2 := by
  constructor
  · intro h w1 w2 hw
    exact add_le_add_of_nonneg (mul_nonneg hw.1 h.1) (mul_nonneg hw.2.1 h.2)
  · intro h
    have hne1 : (1 : K) ≠ 0 := (zero_ne_one' (K := K)).symm
    have h1 : (0 : K) ≤ natK 1 * v1 + 0 * v2 :=
      h (natK 1) 0 ⟨by rw [natK_one]; exact zero_le_one', le_refl 0,
        Or.inl (by rw [natK_one]; exact hne1)⟩
    have h2 : (0 : K) ≤ 0 * v1 + natK 1 * v2 :=
      h 0 (natK 1) ⟨le_refl 0, by rw [natK_one]; exact zero_le_one',
        Or.inr (by rw [natK_one]; exact hne1)⟩
    rw [natK_one, one_mul', zero_mul, add_zero] at h1
    rw [natK_one, zero_mul, zero_add, one_mul'] at h2
    exact ⟨h1, h2⟩

/-- **Proposition 3(i)**, first inclusion, on the datum: a
typed-admissible action is `w`-admissible at every cone weight. -/
theorem typed_imp_w {w1 w2 : K} (hw : WPos w1 w2) {a : WitAct K} {z : WitState K}
    (h : TypedAdm a z) : WAdm w1 w2 a z := by
  constructor
  · intro p hp
    have hpS := h.1 p hp
    exact ⟨hpS.1, (remark2 p.s1 p.s2).mp ⟨hpS.2.1, hpS.2.2⟩ w1 w2 hw⟩
  · have hs := h.2
    refine ⟨hs.1, hs.2.1, ?_⟩
    exact (remark2 (witSucc a z).2.s1 (witSucc a z).2.s2).mp
      ⟨hs.2.2.1, hs.2.2.2⟩ w1 w2 hw

/-- **Proposition 3(ii)** (the full-cone identity), on the datum:
`E_typ = ⋂_{w ∈ W₊} E_w` — the paper's contribution (i). -/
theorem full_cone_identity (a : WitAct K) (z : WitState K) :
    TypedAdm a z ↔ ∀ w1 w2, WPos w1 w2 → WAdm w1 w2 a z := by
  constructor
  · intro h w1 w2 hw
    exact typed_imp_w hw h
  · intro h
    have hne1 : (1 : K) ≠ 0 := (zero_ne_one' (K := K)).symm
    have h100 := h (natK 1) 0 ⟨by rw [natK_one]; exact zero_le_one', le_refl 0,
      Or.inl (by rw [natK_one]; exact hne1)⟩
    have h010 := h 0 (natK 1) ⟨le_refl 0, by rw [natK_one]; exact zero_le_one',
      Or.inr (by rw [natK_one]; exact hne1)⟩
    constructor
    · intro p hp
      have hs1 : 0 ≤ p.s1 := by
        have h1 := (h100.1 p hp).2
        rw [natK_one, one_mul', zero_mul, add_zero] at h1
        exact h1
      have hs2 : 0 ≤ p.s2 := by
        have h1 := (h010.1 p hp).2
        rw [natK_one, zero_mul, zero_add, one_mul'] at h1
        exact h1
      exact ⟨(h100.1 p hp).1, hs1, hs2⟩
    · have hs1 : 0 ≤ (witSucc a z).2.s1 := by
        have h1 := h100.2.2.2
        rw [natK_one, one_mul', zero_mul, add_zero] at h1
        exact h1
      have hs2 : 0 ≤ (witSucc a z).2.s2 := by
        have h1 := h010.2.2.2
        rw [natK_one, zero_mul, zero_add, one_mul'] at h1
        exact h1
      exact ⟨h100.2.1, h100.2.2.1, hs1, hs2⟩

/-- `E_w ⊆ E_tube,phys` (drop the scalarized condition). -/
theorem w_adm_imp_phys {a : DetAct} {w1 w2 : K} {z : WitState K}
    (h : WAdm w1 w2 (.det a) z) : PhysAdm a z :=
  ⟨fun p hp => (h.1 p hp).1, h.2.1, h.2.2.1⟩

/-- `End ⊆ Tube` on the datum (the trajectories are monotone pieces). -/
theorem end_subset_tube (a : DetAct) (z p : WitState K) (h : witEnd a z p) :
    witTube (.det a) z p := by
  cases a with
  | noswitch => exact h
  | fast =>
      rw [h]
      exact ⟨rfl, rfl, sub_le_self z.s1 (natK 2) (natK_nonneg 2), le_refl _⟩
  | slow =>
      rw [h]
      exact ⟨rfl, rfl, sub_le_self z.s2 (natK 2) (natK_nonneg 2), le_refl _⟩
  | staged =>
      cases h with
      | inl h' => rw [h']; exact ⟨sub_le_self z.x 1 zero_le_one', le_refl _,
          le_refl _, le_add_right z.s1 eGain eGain_nonneg, le_refl _,
          le_add_right z.s2 eGain eGain_nonneg⟩
      | inr h' => rw [h']; exact ⟨le_refl _, sub_le_self z.x 1 zero_le_one',
          le_add_right z.s1 eGain eGain_nonneg, le_refl _,
          le_add_right z.s2 eGain eGain_nonneg, le_refl _⟩

/-- `E_tube,phys ⊆ E_end` (endpoint evaluation is weaker). -/
theorem phys_imp_end {a : DetAct} {z : WitState K} (h : PhysAdm a z) :
    EndAdm a z :=
  ⟨fun p hp => h.1 p (end_subset_tube a z p hp), h.2⟩

theorem vtyp_imp_vweak {z : WitState K} (h : VTyp z) : VWeak z := by
  intro w1 w2 hw
  cases h with
  | intro a ha => exact ⟨a, typed_imp_w hw ha⟩

theorem vweak_imp_vphys {z : WitState K} (h : VWeak z) : VPhys z := by
  have hne1 : (1 : K) ≠ 0 := (zero_ne_one' (K := K)).symm
  have h1 := h (natK 1) (natK 1)
    ⟨by rw [natK_one]; exact zero_le_one', by rw [natK_one]; exact zero_le_one',
      Or.inl (by rw [natK_one]; exact hne1)⟩
  cases h1 with
  | intro a ha =>
      refine ⟨a, fun p hp => (ha.1 p hp).1, ha.2.1, ha.2.2.1⟩

/-- The overlap law of Theorem 5(6): `ρ₂ ≥ ρ₁ ↔ s₁ + s₂ ≥ 2`. -/
theorem rho_order (s1 s2 : K) (h2 : 0 < s2) (h2' : s2 < natK 2) :
    (s1 / (natK 2 - s2) ≥ (natK 2 - s1) / s2 ↔ natK 2 ≤ s1 + s2) := by
  have hpos : 0 < natK 2 - s2 := by
    have h1 : s2 - natK 2 < 0 := sub_lt_zero.mpr h2'
    rw [← neg_sub s2 (natK 2)]
    exact neg_pos' h1
  have hneb2 : s2 ≠ 0 := ne_of_gt h2
  have hne22 : natK 2 - s2 ≠ 0 := ne_of_gt hpos
  -- the polynomial identity
  have e : (natK 2 - s1) * (natK 2 - s2) + natK 2 * (s1 + s2)
      = natK 2 * natK 2 + s1 * s2 := by
    have t1 : (natK 2 - s1) * (natK 2 - s2)
        = natK 2 * natK 2 - natK 2 * s2 - (natK 2 * s1 - s1 * s2) := by
      rw [sub_mul, mul_sub, mul_sub, mul_comm s1 (natK 2)]
    rw [t1, left_distrib, sub_sub,
      add_assoc (natK 2 * natK 2 - natK 2 * s2 - natK 2 * s1) (s1 * s2)
        (natK 2 * s1 + natK 2 * s2),
      add_left_comm (s1 * s2) (natK 2 * s1) (natK 2 * s2),
      ← add_assoc (natK 2 * natK 2 - natK 2 * s2 - natK 2 * s1)
        (natK 2 * s1) (s1 * s2 + natK 2 * s2),
      sub_add_cancel (natK 2 * natK 2 - natK 2 * s2) (natK 2 * s1),
      add_comm (s1 * s2) (natK 2 * s2),
      ← add_assoc (natK 2 * natK 2 - natK 2 * s2) (natK 2 * s2) (s1 * s2),
      sub_add_cancel (natK 2 * natK 2) (natK 2 * s2)]
  constructor
  · -- ρ₂ ≥ ρ₁  →  s₁ + s₂ ≥ 2
    intro hge
    have hcross : (natK 2 - s1) * (natK 2 - s2) ≤ s1 * s2 :=
      (div_le_div_cross h2 hpos).mp hge
    have h1 : (natK 2 - s1) * (natK 2 - s2) + natK 2 * (s1 + s2)
        ≤ s1 * s2 + natK 2 * (s1 + s2) := add_le_add hcross (le_refl _)
    rw [e] at h1
    have h2a : natK 2 * natK 2 + s1 * s2 ≤ s1 * s2 + natK 2 * (s1 + s2) := h1
    rw [add_comm (natK 2 * natK 2) (s1 * s2)] at h2a
    have h3 : natK 2 * natK 2 ≤ natK 2 * (s1 + s2) := add_le_cancel_left h2a
    exact mul_le_cancel_left natK_two_pos h3
  · -- s₁ + s₂ ≥ 2  →  ρ₂ ≥ ρ₁
    intro hle
    have h3 : natK 2 * natK 2 ≤ natK 2 * (s1 + s2) :=
      mul_le_mul_of_nonneg_left hle (le_of_lt natK_two_pos)
    have h2a : s1 * s2 + natK 2 * natK 2 ≤ s1 * s2 + natK 2 * (s1 + s2) :=
      add_le_add_left h3 _
    rw [add_comm (s1 * s2) (natK 2 * natK 2)] at h2a
    have h1 : (natK 2 - s1) * (natK 2 - s2) + natK 2 * (s1 + s2)
        ≤ s1 * s2 + natK 2 * (s1 + s2) := by
      rw [e]
      exact h2a
    have hcross : (natK 2 - s1) * (natK 2 - s2) ≤ s1 * s2 :=
      add_le_cancel_right h1
    exact (div_le_div_cross h2 hpos).mpr hcross

/-! ## Theorem 5 (witnessed separation) -/

/-- **Theorem 5(1)** (ambient form): the typed accepted set. -/
theorem vtyp_iff (z : WitState K) :
    VTyp z ↔ (0 ≤ z.x ∧ 0 ≤ z.s1 ∧ 0 ≤ z.s2 ∧
      (1 ≤ z.x ∨ natK 2 ≤ z.s1 ∨ natK 2 ≤ z.s2)) := by
  constructor
  · intro h
    cases h with
    | intro a ha =>
      cases a with
      | noswitch => exact (not_TypedAdm_noswitch z ha).elim
      | fast =>
          have hf := (typedAdm_fast_iff z).mp ha
          exact ⟨hf.1, le_trans (natK_nonneg 2) hf.2.2, hf.2.1,
            Or.inr (Or.inl hf.2.2)⟩
      | slow =>
          have hf := (typedAdm_slow_iff z).mp ha
          exact ⟨hf.1, hf.2.1, le_trans (natK_nonneg 2) hf.2.2,
            Or.inr (Or.inr hf.2.2)⟩
      | staged =>
          have hf := (typedAdm_staged_iff z).mp ha
          exact ⟨le_trans zero_le_one' hf.1, hf.2.1, hf.2.2, Or.inl hf.1⟩
  · intro h
    cases h.2.2.2 with
    | inl hx => exact ⟨.staged, (typedAdm_staged_iff z).mpr ⟨hx, h.2.1, h.2.2.1⟩⟩
    | inr h2 =>
      cases h2 with
      | inl hs1 => exact ⟨.fast, (typedAdm_fast_iff z).mpr ⟨h.1, h.2.2.1, hs1⟩⟩
      | inr hs2 => exact ⟨.slow, (typedAdm_slow_iff z).mpr ⟨h.1, h.2.1, hs2⟩⟩

/-- **Theorem 5(1)**: on `X₀`, `V_typ = {x ≥ 1} ∪ {s₁ ≥ 2} ∪ {s₂ ≥ 2}`. -/
theorem thm5_1 (z : WitState K) (hz : InX0 z) :
    VTyp z ↔ (1 ≤ z.x ∨ natK 2 ≤ z.s1 ∨ natK 2 ≤ z.s2) := by
  rw [vtyp_iff]
  constructor
  · intro h
    exact h.2.2.2
  · intro h
    exact ⟨hz.1, hz.2.1, hz.2.2, h⟩

/-- **Theorem 5(2)**: on `X₀`,
`V_weak = ⋂_{w ∈ W₊} V_w = {x ≥ 1} ∪ {s₁ + s₂ ≥ 2}`. -/
theorem thm5_2 (z : WitState K) (hz : InX0 z) :
    VWeak z ↔ (1 ≤ z.x ∨ natK 2 ≤ z.s1 + z.s2) := by
  constructor
  · intro hweak
    by_cases hx : 1 ≤ z.x
    · exact Or.inl hx
    by_cases hsum : natK 2 ≤ z.s1 + z.s2
    · exact Or.inr hsum
    exfalso
    have hxlt : z.x < 1 := le_of_not_le hx
    have hsmlt : z.s1 + z.s2 < natK 2 := le_of_not_le hsum
    have hs1lt : z.s1 < natK 2 := by
      by_cases hc : z.s1 < natK 2
      · exact hc
      · exact absurd (le_trans (le_add_right (natK 2) 0 (le_refl 0))
          (add_le_add (le_of_not_lt hc) hz.2.2)) hsum
    have hs2lt : z.s2 < natK 2 := by
      by_cases hc : z.s2 < natK 2
      · exact hc
      · have hzero : natK 2 ≤ (0 : K) + natK 2 := by
          rw [zero_add]; exact le_refl _
        exact absurd (le_trans hzero
          (add_le_add hz.2.1 (le_of_not_lt hc))) hsum
    have hkill : ¬ VWeak z := by
      intro hvw
      by_cases hs2z : z.s2 = 0
      · have hne1 : (1 : K) ≠ 0 := (zero_ne_one' (K := K)).symm
        have hw : WPos (1 : K) 1 :=
          ⟨zero_le_one', zero_le_one', Or.inl hne1⟩
        have h11 := hvw 1 1 hw
        cases h11 with
        | intro a ha =>
          cases a with
          | noswitch => exact not_WAdm_noswitch z ha
          | fast =>
              have hf := (wAdm_fast_iff hw z).mp ha
              rw [one_mul', one_mul'] at hf
              have hlt2 : z.s1 - natK 2 + z.s2 < 0 := by
                have h1 := sub_lt_sub_right hsmlt (natK 2)
                rw [sub_self] at h1
                rw [add_sub_comm]
                exact h1
              exact absurd hf.2 (not_le_of_lt hlt2)
          | slow =>
              have hf := (wAdm_slow_iff hw z).mp ha
              rw [one_mul', one_mul'] at hf
              have hlt2 : z.s1 + (z.s2 - natK 2) < 0 := by
                have h1 := sub_lt_sub_right hsmlt (natK 2)
                rw [sub_self] at h1
                rw [add_sub_comm']
                exact h1
              exact absurd hf.2 (not_le_of_lt hlt2)
          | staged =>
              have hst := (wAdm_staged_iff hw z).mp ha
              exact absurd hst.1 (not_le_of_lt hxlt)
      · have hs2pos : 0 < z.s2 := lt_of_le_of_ne hz.2.2 (fun he => hs2z he.symm)
        have h2pos : 0 < natK 2 - z.s2 := by
          have h1 : z.s2 - natK 2 < 0 := sub_lt_zero.mpr hs2lt
          rw [← neg_sub z.s2 (natK 2)]
          exact neg_pos' h1
        have h1pos : 0 < natK 2 - z.s1 := by
          have h1 : z.s1 - natK 2 < 0 := sub_lt_zero.mpr hs1lt
          rw [← neg_sub z.s1 (natK 2)]
          exact neg_pos' h1
        have hρ2ltρ1 : z.s1 / (natK 2 - z.s2) < (natK 2 - z.s1) / z.s2 :=
          le_of_not_le (fun hge => hsum ((rho_order z.s1 z.s2 hs2pos hs2lt).mp hge))
        have hρ1nn : (0 : K) ≤ (natK 2 - z.s1) / z.s2 :=
          div_nonneg (le_of_lt h1pos) hs2pos
        have hρ2nn : (0 : K) ≤ z.s1 / (natK 2 - z.s2) :=
          div_nonneg hz.2.1 h2pos
        have hrpos : (0 : K) ≤ ((natK 2 - z.s1) / z.s2 + z.s1 / (natK 2 - z.s2))
            / natK 2 :=
          div_nonneg (add_le_add_of_nonneg hρ1nn hρ2nn) natK_two_pos
        have hne1 : (1 : K) ≠ 0 := (zero_ne_one' (K := K)).symm
        have hw : WPos (1 : K)
            (((natK 2 - z.s1) / z.s2 + z.s1 / (natK 2 - z.s2)) / natK 2) :=
          ⟨zero_le_one', hrpos, Or.inl hne1⟩
        have hmid := midpoint_lt ((natK 2 - z.s1) / z.s2) (z.s1 / (natK 2 - z.s2))
          hρ2ltρ1
        have hkill2 := hvw 1
          (((natK 2 - z.s1) / z.s2 + z.s1 / (natK 2 - z.s2)) / natK 2) hw
        cases hkill2 with
        | intro a ha =>
          cases a with
          | noswitch => exact not_WAdm_noswitch z ha
          | fast =>
              have hf := (wAdm_fast_iff hw z).mp ha
              rw [one_mul'] at hf
              have hlt1 : ((natK 2 - z.s1) / z.s2 + z.s1 / (natK 2 - z.s2)) / natK 2
                  * z.s2 < (natK 2 - z.s1) / z.s2 * z.s2 :=
                mul_lt_mul_of_pos_right hmid.1 hs2pos
              rw [div_mul_cancel (ne_of_gt hs2pos) (natK 2 - z.s1)] at hlt1
              have hlt2 : z.s1 - natK 2 + ((natK 2 - z.s1) / z.s2
                  + z.s1 / (natK 2 - z.s2)) / natK 2 * z.s2 < 0 := by
                have hcancel : z.s1 - natK 2 + (natK 2 - z.s1) = 0 := by
                  rw [← neg_sub z.s1 (natK 2), add_neg_cancel]
                have hstep : z.s1 - natK 2 + ((natK 2 - z.s1) / z.s2
                    + z.s1 / (natK 2 - z.s2)) / natK 2 * z.s2
                    < z.s1 - natK 2 + (natK 2 - z.s1) :=
                  add_lt_add_left' hlt1 _
                rw [hcancel] at hstep
                exact hstep
              exact absurd hf.2 (not_le_of_lt hlt2)
          | slow =>
              have hf := (wAdm_slow_iff hw z).mp ha
              rw [one_mul'] at hf
              have hlt2 : z.s2 - natK 2 < 0 := sub_lt_zero.mpr hs2lt
              have h1 : ((natK 2 - z.s1) / z.s2 + z.s1 / (natK 2 - z.s2)) / natK 2
                  * (z.s2 - natK 2)
                  < z.s1 / (natK 2 - z.s2) * (z.s2 - natK 2) :=
                mul_lt_mul_of_neg_right hmid.2 hlt2
              have eneg : z.s2 - natK 2 = -(natK 2 - z.s2) :=
                (neg_sub (natK 2) z.s2).symm
              have e2 : z.s1 / (natK 2 - z.s2) * (z.s2 - natK 2) = -z.s1 := by
                rw [eneg, ← mul_neg, div_mul_cancel (ne_of_gt h2pos) z.s1]
              rw [e2] at h1
              have h2b : z.s1 + ((natK 2 - z.s1) / z.s2 + z.s1 / (natK 2 - z.s2))
                  / natK 2 * (z.s2 - natK 2) < z.s1 + -z.s1 :=
                add_lt_add_left' h1 z.s1
              rw [add_neg_cancel] at h2b
              exact absurd hf.2 (not_le_of_lt h2b)
          | staged =>
              have hst := (wAdm_staged_iff hw z).mp ha
              exact absurd hst.1 (not_le_of_lt hxlt)
    exact hkill hweak
  · intro h
    intro w1 w2 hw
    cases h with
    | inl hx =>
        exact ⟨.staged, (wAdm_staged_iff hw z).mpr
          ⟨hx, add_le_add_of_nonneg (mul_nonneg hw.1 hz.2.1)
            (mul_nonneg hw.2.1 hz.2.2)⟩⟩
    | inr hsum =>
        by_cases hs1 : natK 2 ≤ z.s1
        · exact ⟨.fast, typed_imp_w hw ((typedAdm_fast_iff z).mpr
            ⟨hz.1, hz.2.2, hs1⟩)⟩
        by_cases hs2 : natK 2 ≤ z.s2
        · exact ⟨.slow, typed_imp_w hw ((typedAdm_slow_iff z).mpr
            ⟨hz.1, hz.2.1, hs2⟩)⟩
        have hs2lt2 : z.s2 < natK 2 := le_of_not_le hs2
        have hs1lt2 : z.s1 < natK 2 := le_of_not_le hs1
        have hs2pos : 0 < z.s2 := by
          by_cases hc : 0 < z.s2
          · exact hc
          · have h2b : z.s2 ≤ 0 := le_of_not_lt hc
            have h2 : z.s1 + z.s2 ≤ z.s1 + 0 := add_le_add_left h2b z.s1
            rw [add_zero] at h2
            exact absurd (le_trans hsum h2) hs1
        have h2pos : 0 < natK 2 - z.s2 := by
          have h1 : z.s2 - natK 2 < 0 := sub_lt_zero.mpr hs2lt2
          rw [← neg_sub z.s2 (natK 2)]
          exact neg_pos' h1
        have hρord : (natK 2 - z.s1) / z.s2 ≤ z.s1 / (natK 2 - z.s2) :=
          (rho_order z.s1 z.s2 hs2pos hs2lt2).mpr hsum
        by_cases hw1 : w1 = 0
        · have hw2pos : 0 < w2 :=
            match hw.2.2 with
            | Or.inl h1ne => absurd hw1 h1ne
            | Or.inr h2ne => lt_of_le_of_ne hw.2.1 (fun he => h2ne he.symm)
          refine ⟨.fast, (wAdm_fast_iff hw z).mpr ⟨hz.1, ?_⟩⟩
          rw [hw1, zero_mul, zero_add]
          exact mul_nonneg (le_of_lt hw2pos) hz.2.2
        · have hw1pos : 0 < w1 := lt_of_le_of_ne hw.1 (fun he => hw1 he.symm)
          have hrw2 : w1 * (w2 / w1) = w2 := by
            rw [mul_comm]; exact div_mul_cancel (ne_of_gt hw1pos) w2
          by_cases hge : (natK 2 - z.s1) / z.s2 ≤ w2 / w1
          · refine ⟨.fast, (wAdm_fast_iff hw z).mpr ⟨hz.1, ?_⟩⟩
            have hsplit : w1 * (z.s1 - natK 2) + w2 * z.s2
                = w1 * ((z.s1 - natK 2) + (w2 / w1) * z.s2) := by
              rw [left_distrib, ← mul_assoc w1 (w2 / w1) z.s2, hrw2]
            rw [hsplit]
            refine (mul_nonneg_iff_pos_right' hw1pos).mpr ?_
            have h1 : (natK 2 - z.s1) / z.s2 * z.s2 ≤ (w2 / w1) * z.s2 :=
              mul_le_mul_of_nonneg_right hge (le_of_lt hs2pos)
            rw [div_mul_cancel (ne_of_gt hs2pos) (natK 2 - z.s1)] at h1
            have hcancel : z.s1 - natK 2 + (natK 2 - z.s1) = 0 := by
              rw [← neg_sub z.s1 (natK 2), add_neg_cancel]
            have h3 : z.s1 - natK 2 + (natK 2 - z.s1)
                ≤ z.s1 - natK 2 + (w2 / w1) * z.s2 :=
              add_le_add_left h1 _
            rw [hcancel] at h3
            exact h3
          · have hrle : w2 / w1 ≤ z.s1 / (natK 2 - z.s2) :=
              le_trans (le_of_lt (le_of_not_le (fun hle => hge hle))) hρord
            refine ⟨.slow, (wAdm_slow_iff hw z).mpr ⟨hz.1, ?_⟩⟩
            have hsplit : w1 * z.s1 + w2 * (z.s2 - natK 2)
                = w1 * (z.s1 + (w2 / w1) * (z.s2 - natK 2)) := by
              rw [left_distrib, ← mul_assoc w1 (w2 / w1) (z.s2 - natK 2), hrw2]
            rw [hsplit]
            refine (mul_nonneg_iff_pos_right' hw1pos).mpr ?_
            have hlt2 : z.s2 - natK 2 < 0 := sub_lt_zero.mpr hs2lt2
            have h1 : z.s1 / (natK 2 - z.s2) * (z.s2 - natK 2)
                ≤ (w2 / w1) * (z.s2 - natK 2) :=
              mul_le_mul_of_neg_right hrle hlt2
            have eneg : z.s2 - natK 2 = -(natK 2 - z.s2) :=
              (neg_sub (natK 2) z.s2).symm
            have e2 : z.s1 / (natK 2 - z.s2) * (z.s2 - natK 2) = -z.s1 := by
              rw [eneg, ← mul_neg, div_mul_cancel (ne_of_gt h2pos) z.s1]
            rw [e2] at h1
            have h3 : z.s1 + -z.s1
                ≤ z.s1 + (w2 / w1) * (z.s2 - natK 2) :=
              add_le_add_left h1 z.s1
            rw [add_neg_cancel] at h3
            exact h3

theorem not_PhysAdm_noswitch (z : WitState K) (h : PhysAdm .noswitch z) : False :=
  Bool.noConfusion h.2.1

/-- **Theorem 5(3)**, ambient form: `V_phys = {x ≥ 0}` (FAST serves every
`x ≥ 0`; every physically-admissible action needs `x ≥ 0`). -/
theorem vphys_iff (z : WitState K) : VPhys z ↔ 0 ≤ z.x := by
  constructor
  · intro h
    cases h with
    | intro a ha =>
      cases a with
      | noswitch => exact (not_PhysAdm_noswitch z ha).elim
      | fast =>
          exact ha.1 z ⟨rfl, rfl, sub_le_self z.s1 (natK 2) (natK_nonneg 2),
            le_refl _⟩
      | slow =>
          exact ha.1 z ⟨rfl, rfl, sub_le_self z.s2 (natK 2) (natK_nonneg 2),
            le_refl _⟩
      | staged =>
          have hbot : witTube (.det .staged) z ⟨z.x - 1, z.s1, z.s2⟩ :=
            ⟨le_refl _, sub_le_self z.x 1 zero_le_one', le_refl _,
              le_add_right z.s1 eGain eGain_nonneg, le_refl _,
              le_add_right z.s2 eGain eGain_nonneg⟩
          have h1 : 0 ≤ z.x - 1 := ha.1 _ hbot
          exact le_trans h1 (sub_le_self z.x 1 zero_le_one')
  · intro h
    refine ⟨.fast, fun p hp => ?_, rfl, h⟩
    show 0 ≤ p.x
    rw [hp.1]; exact h

/-- **Theorem 5(3)**, ambient form: `V_end = {x ≥ 0}` (endpoint evaluation
admits every `x ≥ 0` via FAST, whose endpoints are the initial values). -/
theorem vend_iff (z : WitState K) : VEnd z ↔ 0 ≤ z.x := by
  constructor
  · intro h
    cases h with
    | intro a ha =>
      cases a with
      | noswitch => exact Bool.noConfusion ha.2.1
      | fast => exact ha.1 z rfl
      | slow => exact ha.1 z rfl
      | staged => exact ha.1 z (Or.inl rfl)
  · intro h
    refine ⟨.fast, fun p hp => ?_, rfl, h⟩
    show 0 ≤ p.x
    rw [hp]; exact h

/-- **Theorem 5(3)**: on `X₀`, `V_phys = V_end = X₀`. -/
theorem thm5_3 (z : WitState K) (hz : InX0 z) : VPhys z ∧ VEnd z :=
  ⟨(vphys_iff z).mpr hz.1, (vend_iff z).mpr hz.1⟩

/-- **Theorem 5(4)**: `FP_agg = I`, the genuine acceptance gap is exactly
the impossibility region. -/
theorem thm5_4 (z : WitState K) (hz : InX0 z) : FPAgg z ↔ IsGap z := by
  constructor
  · intro h
    have hw := (thm5_2 z hz).mp h.1
    have hn : ¬ (1 ≤ z.x ∨ natK 2 ≤ z.s1 ∨ natK 2 ≤ z.s2) := fun hd =>
      h.2 ((thm5_1 z hz).mpr hd)
    have hx : z.x < 1 := le_of_not_le (fun hle => hn (Or.inl hle))
    have hs1 : z.s1 < natK 2 :=
      le_of_not_le (fun hle => hn (Or.inr (Or.inl hle)))
    have hs2 : z.s2 < natK 2 :=
      le_of_not_le (fun hle => hn (Or.inr (Or.inr hle)))
    have hsum : natK 2 ≤ z.s1 + z.s2 := by
      cases hw with
      | inl hxl => exact absurd hxl (not_le_of_lt hx)
      | inr hsum => exact hsum
    exact ⟨hx, hs1, hs2, hsum⟩
  · intro h
    refine ⟨(thm5_2 z hz).mpr (Or.inr h.2.2.2), ?_⟩
    intro hvt
    have hd := (thm5_1 z hz).mp hvt
    cases hd with
    | inl hle => exact absurd hle (not_le_of_lt h.1)
    | inr h2 =>
      cases h2 with
      | inl hle => exact absurd hle (not_le_of_lt h.2.1)
      | inr hle => exact absurd hle (not_le_of_lt h.2.2.1)

/-- **Theorem 5(4)**: the gap is nonempty, witnessed by the strictly
interior point `(1/2, 6/5, 6/5)` of the paper's Example. -/
theorem thm5_4_nonempty {K : Type} [OrdField K] :
    FPAgg ⟨(natK 1 / natK 2 : K), natK 6 / natK 5, natK 6 / natK 5⟩ := by
  have h2pos : (0 : K) < natK 2 := natK_two_pos
  have h5pos : (0 : K) < natK 5 := natK_pos (n := 5) (by omega)
  have h5ne : (natK 5 : K) ≠ 0 := natK_five_ne_zero
  have hx : (natK 1 / natK 2 : K) < 1 := by
    rw [div_lt_iff h2pos, one_mul']
    exact natK_lt_of_lt (by decide)
  have hs : (natK 6 / natK 5 : K) < natK 2 := by
    rw [div_lt_iff h5pos, ← natK_mul]
    exact natK_lt_of_lt (by decide)
  have hsum : (natK 2 : K) ≤ natK 6 / natK 5 + natK 6 / natK 5 := by
    rw [div_add_div_same h5ne, le_div_iff h5pos, ← natK_mul, ← natK_add]
    exact natK_le (by decide)
  have hz : InX0 ⟨(natK 1 / natK 2 : K), natK 6 / natK 5, natK 6 / natK 5⟩ :=
    ⟨div_nonneg (natK_nonneg 1) h2pos, div_nonneg (natK_nonneg 6) h5pos,
      div_nonneg (natK_nonneg 6) h5pos⟩
  exact (thm5_4 _ hz).mpr ⟨hx, hs, hs, hsum⟩

/-- **Theorem 5(5)**: both hierarchy inclusions are strict, with the
paper's two witnesses. -/
theorem thm5_5 {K : Type} [OrdField K] :
    (VWeak ⟨(natK 1 / natK 2 : K), natK 6 / natK 5, natK 6 / natK 5⟩
        ∧ ¬ VTyp ⟨(natK 1 / natK 2 : K), natK 6 / natK 5, natK 6 / natK 5⟩)
    ∧ (VPhys ⟨(natK 1 / natK 2 : K), natK 1 / natK 10, natK 1 / natK 10⟩
        ∧ ¬ VWeak ⟨(natK 1 / natK 2 : K), natK 1 / natK 10, natK 1 / natK 10⟩) := by
  have h2pos : (0 : K) < natK 2 := natK_two_pos
  have h5pos : (0 : K) < natK 5 := natK_pos (n := 5) (by omega)
  have h5ne : (natK 5 : K) ≠ 0 := natK_five_ne_zero
  have h10pos : (0 : K) < natK 10 := natK_pos (n := 10) (by omega)
  have h10ne : (natK 10 : K) ≠ 0 := natK_ne_zero (n := 10) (by omega)
  have hxlt : (natK 1 / natK 2 : K) < 1 := by
    rw [div_lt_iff h2pos, one_mul']
    exact natK_lt_of_lt (by decide)
  have hslt : (natK 6 / natK 5 : K) < natK 2 := by
    rw [div_lt_iff h5pos, ← natK_mul]
    exact natK_lt_of_lt (by decide)
  have hz1 : InX0 ⟨(natK 1 / natK 2 : K), natK 6 / natK 5, natK 6 / natK 5⟩ :=
    ⟨div_nonneg (natK_nonneg 1) h2pos, div_nonneg (natK_nonneg 6) h5pos,
      div_nonneg (natK_nonneg 6) h5pos⟩
  have hz2 : InX0 ⟨(natK 1 / natK 2 : K), natK 1 / natK 10, natK 1 / natK 10⟩ :=
    ⟨div_nonneg (natK_nonneg 1) h2pos, div_nonneg (natK_nonneg 1) h10pos,
      div_nonneg (natK_nonneg 1) h10pos⟩
  have hsum12 : (natK 2 : K) ≤ natK 6 / natK 5 + natK 6 / natK 5 := by
    rw [div_add_div_same h5ne, le_div_iff h5pos, ← natK_mul, ← natK_add]
    exact natK_le (by decide)
  have hsum110 : natK 1 / natK 10 + natK 1 / natK 10 < (natK 2 : K) := by
    rw [div_add_div_same h10ne, div_lt_iff h10pos, ← natK_mul, ← natK_add]
    exact natK_lt_of_lt (by decide)
  refine ⟨⟨(thm5_2 _ hz1).mpr (Or.inr hsum12), ?_⟩, ⟨(vphys_iff _).mpr
    (div_nonneg (natK_nonneg 1) (natK_pos (by omega))), ?_⟩⟩
  · intro hvt
    have hd := (thm5_1 _ hz1).mp hvt
    cases hd with
    | inl hle =>
        exact absurd hle (not_le_of_lt hxlt)
    | inr h2 =>
      cases h2 with
      | inl hle => exact absurd hle (not_le_of_lt hslt)
      | inr hle => exact absurd hle (not_le_of_lt hslt)
  · intro hvw
    have hw := (thm5_2 _ hz2).mp hvw
    cases hw with
    | inl hxl => exact absurd hxl (not_le_of_lt hxlt)
    | inr hsum => exact absurd hsum (not_le_of_lt hsum110)

/-- **Theorem 5(6)**: the per-weight licensing thresholds, with the
overlap law (already `rho_order`). -/
theorem thm5_6 (z : WitState K) (hz : InX0 z) (hs1 : z.s1 < natK 2)
    (hs2 : z.s2 < natK 2) (hsum : natK 2 ≤ z.s1 + z.s2) {w1 w2 : K}
    (hw1 : 0 < w1) (hw2 : 0 ≤ w2) :
    (WAdm w1 w2 (.det .fast) z ↔ (natK 2 - z.s1) / z.s2 ≤ w2 / w1)
      ∧ (WAdm w1 w2 (.det .slow) z ↔ w2 / w1 ≤ z.s1 / (natK 2 - z.s2)) := by
  have hs2pos : 0 < z.s2 := by
    by_cases hc : 0 < z.s2
    · exact hc
    · have h2b : z.s2 ≤ 0 := le_of_not_lt hc
      have hle : z.s1 + z.s2 ≤ z.s1 + 0 := add_le_add_left h2b z.s1
      rw [add_zero] at hle
      exact absurd hsum (not_le_of_lt (lt_of_le_of_lt hle hs1))
  have h2pos : 0 < natK 2 - z.s2 := by
    have h1 : z.s2 - natK 2 < 0 := sub_lt_zero.mpr hs2
    rw [← neg_sub z.s2 (natK 2)]
    exact neg_pos' h1
  have hw : WPos w1 w2 := ⟨le_of_lt hw1, hw2, Or.inl (ne_of_gt hw1)⟩
  have hrw2 : w1 * (w2 / w1) = w2 := by
    rw [mul_comm]; exact div_mul_cancel (ne_of_gt hw1) w2
  have hcancel : z.s1 - natK 2 + (natK 2 - z.s1) = 0 := by
    rw [← neg_sub z.s1 (natK 2), add_neg_cancel]
  have hcancels : z.s1 + -z.s1 = 0 := add_neg_cancel z.s1
  have hsplitf : w1 * (z.s1 - natK 2) + w2 * z.s2
      = w1 * ((z.s1 - natK 2) + (w2 / w1) * z.s2) := by
    rw [left_distrib, ← mul_assoc w1 (w2 / w1) z.s2, hrw2]
  have hsplits : w1 * z.s1 + w2 * (z.s2 - natK 2)
      = w1 * (z.s1 + (w2 / w1) * (z.s2 - natK 2)) := by
    rw [left_distrib, ← mul_assoc w1 (w2 / w1) (z.s2 - natK 2), hrw2]
  constructor
  · rw [wAdm_fast_iff hw z]
    constructor
    · intro hdip
      rw [hsplitf] at hdip
      have hdip2 : (z.s1 - natK 2) + (w2 / w1) * z.s2 ≥ 0 :=
        (mul_nonneg_iff_pos_right' hw1).mp hdip.2
      have h1 : natK 2 - z.s1 ≤ (w2 / w1) * z.s2 := by
        have h2 := neg_le_of_add_nonneg hdip2
        rwa [neg_sub z.s1 (natK 2)] at h2
      exact (div_le_iff hs2pos).mpr h1
    · intro hdip
      have h1 : natK 2 - z.s1 ≤ (w2 / w1) * z.s2 :=
        (div_le_iff hs2pos).mp hdip
      refine ⟨hz.1, ?_⟩
      rw [hsplitf]
      refine (mul_nonneg_iff_pos_right' hw1).mpr ?_
      have h2 : z.s1 - natK 2 + (natK 2 - z.s1)
          ≤ z.s1 - natK 2 + (w2 / w1) * z.s2 :=
        add_le_add_left h1 _
      rw [hcancel] at h2
      exact h2
  · rw [wAdm_slow_iff hw z]
    constructor
    · intro hdip
      rw [hsplits] at hdip
      have hdip2 : z.s1 + (w2 / w1) * (z.s2 - natK 2) ≥ 0 :=
        (mul_nonneg_iff_pos_right' hw1).mp hdip.2
      have hneg : -z.s1 ≤ (w2 / w1) * (z.s2 - natK 2) :=
        neg_le_of_add_nonneg hdip2
      have h2 : (w2 / w1) * (natK 2 - z.s2) ≤ z.s1 := by
        have h3 := neg_le_neg hneg
        rw [neg_neg, mul_neg, neg_sub z.s2 (natK 2)] at h3
        exact h3
      exact (le_div_iff h2pos).mpr h2
    · intro hdip
      have h2 : (w2 / w1) * (natK 2 - z.s2) ≤ z.s1 :=
        (le_div_iff h2pos).mp hdip
      refine ⟨hz.1, ?_⟩
      rw [hsplits]
      refine (mul_nonneg_iff_pos_right' hw1).mpr ?_
      have h3 : -z.s1 ≤ (w2 / w1) * (z.s2 - natK 2) := by
        have h4 := neg_le_neg h2
        rw [← neg_sub z.s2 (natK 2), mul_neg, neg_neg] at h4
        exact h4
      have h4 : z.s1 + -z.s1 ≤ z.s1 + (w2 / w1) * (z.s2 - natK 2) :=
        add_le_add_left h3 z.s1
      rw [hcancels] at h4
      exact h4

/-- **Theorem 5(6)**, concrete witness point: at `(1/2, 6/5, 6/5)`,
`ρ₁ = 2/3` and `ρ₂ = 3/2`. -/
theorem thm5_6_datum {K : Type} [OrdField K] :
    ((natK 2 : K) - natK 6 / natK 5) / (natK 6 / natK 5) = natK 2 / natK 3
      ∧ natK 6 / natK 5 / ((natK 2 : K) - natK 6 / natK 5) = natK 3 / natK 2 := by
  have h5ne : (natK 5 : K) ≠ 0 := natK_five_ne_zero
  have h4 : (natK 2 : K) - natK 6 / natK 5 = natK 4 / natK 5 := by
    have e2 : (natK 2 : K) = natK 10 / natK 5 := by
      refine (mul_right_cancel' h5ne) ?_
      rw [div_mul_cancel h5ne, ← natK_mul]
    have e3 : (natK 10 : K) - natK 6 = natK 4 := by
      rw [show (10 : Nat) = 6 + 4 from rfl, natK_add, add_sub_add_cancel']
    rw [e2, ← sub_div (natK 10) (natK 6) (natK 5), e3]
  have h6ne : (natK 6 : K) ≠ 0 := natK_ne_zero (n := 6) (by omega)
  have h3ne : (natK 3 : K) ≠ 0 := natK_ne_zero (n := 3) (by omega)
  have h4ne : (natK 4 : K) ≠ 0 := natK_ne_zero (n := 4) (by omega)
  have h2ne : (natK 2 : K) ≠ 0 := natK_two_ne_zero
  have h4' : (natK 4 : K) / natK 5 / (natK 6 / natK 5)
      = natK 2 / natK 3 := by
    rw [div_div_same_denom h5ne h6ne, div_eq_div_iff h6ne h3ne,
      ← natK_mul, ← natK_mul]
  have h4'' : (natK 6 : K) / natK 5 / (natK 4 / natK 5)
      = natK 3 / natK 2 := by
    rw [div_div_same_denom h5ne h4ne, div_eq_div_iff h4ne h2ne,
      ← natK_mul, ← natK_mul]
  constructor
  · rw [h4]; exact h4'
  · rw [h4]; exact h4''

/-- **Theorem 5(7)**: the rescue split — `R` is typed-transformable,
witnessed by STAGED. -/
theorem thm5_7_rescue (z : WitState K) (hx : 1 ≤ z.x) (hs1 : 0 ≤ z.s1)
    (hs2 : 0 ≤ z.s2) : TypedAdm (.det .staged) z :=
  (typedAdm_staged_iff z).mpr ⟨hx, hs1, hs2⟩

/-- **Theorem 5(7)**: on the impossibility region, all four menu actions
violate the typed constraints, with the exhibited violation points. -/
theorem thm5_7_violations (z : WitState K) (hI : IsGap z) :
    (∃ p, witTube (.det .fast) z p ∧ p.s1 < 0)
      ∧ (∃ p, witTube (.det .slow) z p ∧ p.s2 < 0)
      ∧ (∃ p, witTube (.det .staged) z p ∧ p.x < 0)
      ∧ (witSucc (.det .noswitch) z).1 = false :=
  ⟨⟨⟨z.x, z.s1 - natK 2, z.s2⟩, ⟨rfl, rfl, le_refl _,
      sub_le_self z.s1 (natK 2) (natK_nonneg 2)⟩,
    sub_lt_zero.mpr hI.2.1⟩,
    ⟨⟨z.x, z.s1, z.s2 - natK 2⟩, ⟨rfl, rfl, le_refl _,
      sub_le_self z.s2 (natK 2) (natK_nonneg 2)⟩,
    sub_lt_zero.mpr hI.2.2.1⟩,
    ⟨⟨z.x - 1, z.s1, z.s2⟩, ⟨le_refl _, sub_le_self z.x 1 zero_le_one',
      le_refl _, le_add_right z.s1 eGain eGain_nonneg, le_refl _,
      le_add_right z.s2 eGain eGain_nonneg⟩,
    sub_lt_zero.mpr hI.1⟩,
    rfl⟩


/-! ## Theorem 9 (blend collapse) and Proposition 10 -/

/-- The window-sum lemma: an admissible blend forces `s₁ + s₂ ≥ 2`. -/
theorem blend_window_sum (z : WitState K) {δ : K} (h1 : natK 2 * δ ≤ z.s1)
    (h2 : natK 2 * (1 - δ) ≤ z.s2) : natK 2 ≤ z.s1 + z.s2 := by
  have hsum : natK 2 * δ + natK 2 * (1 - δ) ≤ z.s1 + z.s2 :=
    add_le_add h1 h2
  have e : natK 2 * δ + natK 2 * (1 - δ) = natK 2 := by
    rw [← left_distrib, add_comm δ (1 - δ), sub_add_cancel, mul_one]
  rw [e] at hsum
  exact hsum

/-- **Theorem 9(i)**: the admissible window (display form
`δ ∈ [1 - s₂/2, s₁/2]`; stated in the equivalent fraction-free form). -/
theorem thm9_window (z : WitState K) (hz : InX0 z) {δ : K} (hδ1 : 0 ≤ δ)
    (hδ2 : δ ≤ 1) :
    TypedAdm (.blend δ) z ↔ (natK 2 * δ ≤ z.s1 ∧ natK 2 * (1 - δ) ≤ z.s2) :=
  typedAdm_blend_iff (δ := δ) z hδ1 hδ2 hz

/-- **Theorem 9(iii)**: a single δ serves every weight. -/
theorem thm9_weight_indep (z : WitState K) {δ : K}
    (h : TypedAdm (.blend δ) z) {w1 w2 : K} (hw : WPos w1 w2) :
    WAdm w1 w2 (.blend δ) z := typed_imp_w hw h

/-- **Proposition 10**: sequential time-sharing does not erase the gap —
the union tube of FAST and SLOW is typed-safe exactly when both floors
survive their own dips. -/
theorem prop10 (z : WitState K) (hz : InX0 z) :
    ((∀ p, witTube (.det .fast) z p ∨ witTube (.det .slow) z p → inS p)
      ↔ (natK 2 ≤ z.s1 ∧ natK 2 ≤ z.s2)) := by
  constructor
  · intro h
    have hf : witTube (.det .fast) z ⟨z.x, z.s1 - natK 2, z.s2⟩ :=
      ⟨rfl, rfl, le_refl _, sub_le_self z.s1 (natK 2) (natK_nonneg 2)⟩
    have hs : witTube (.det .slow) z ⟨z.x, z.s1, z.s2 - natK 2⟩ :=
      ⟨rfl, rfl, le_refl _, sub_le_self z.s2 (natK 2) (natK_nonneg 2)⟩
    have h1 := h _ (Or.inl hf)
    have h2 := h _ (Or.inr hs)
    exact ⟨sub_nonneg.mp h1.2.1, sub_nonneg.mp h2.2.2⟩
  · intro h p hp
    cases hp with
    | inl hp' =>
        refine ⟨?_, ?_, ?_⟩
        · rw [hp'.1]; exact hz.1
        · exact le_trans (sub_nonneg.mpr h.1) hp'.2.2.1
        · rw [hp'.2.1]; exact hz.2.2
    | inr hp' =>
        refine ⟨?_, ?_, ?_⟩
        · rw [hp'.1]; exact hz.1
        · rw [hp'.2.1]; exact hz.2.1
        · exact le_trans (sub_nonneg.mpr h.2) hp'.2.2.1

/-! ## Lemma A (the handshake) -/

/-- The θ = 1 rung in floor-referenced indices `λᵢ = 1 + sᵢ`. -/
def Theta1Adm (w1 w2 : K) (a : WitAct K) (z : WitState K) : Prop :=
  (∀ p, witTube a z p →
      (0 ≤ p.x ∧ 1 ≤ w1 * (1 + p.s1) + w2 * (1 + p.s2))) ∧
  ((witSucc a z).1 = true ∧ 0 ≤ (witSucc a z).2.x ∧
      1 ≤ w1 * (1 + (witSucc a z).2.s1) + w2 * (1 + (witSucc a z).2.s2))

/-- **Lemma A**: the handshake identity. -/
theorem lemA_identity (w1 w2 u1 u2 : K) (hw : w1 + w2 = 1) :
    w1 * (1 + u1) + w2 * (1 + u2) = 1 + (w1 * u1 + w2 * u2) :=
  lambda_handshake w1 w2 u1 u2 hw

/-- **Lemma A**: the same acceptance set at every state and weight — the
θ = 1 member is the compensatory engine exactly. -/
theorem lemA_engine {w1 w2 : K} (hw : w1 + w2 = 1) (a : WitAct K)
    (z : WitState K) : Theta1Adm w1 w2 a z ↔ WAdm w1 w2 a z := by
  constructor
  · intro h
    constructor
    · intro p hp
      have h1 := h.1 p hp
      refine ⟨h1.1, ?_⟩
      have h2 : 1 ≤ 1 + (w1 * p.s1 + w2 * p.s2) := by
        rw [← lemA_identity w1 w2 p.s1 p.s2 hw]; exact h1.2
      rw [one_le_add_one_iff] at h2
      exact h2
    · have hs := h.2
      refine ⟨hs.1, hs.2.1, ?_⟩
      have h2 : 1 ≤ 1 + (w1 * (witSucc a z).2.s1 + w2 * (witSucc a z).2.s2) := by
        rw [← lemA_identity w1 w2 (witSucc a z).2.s1 (witSucc a z).2.s2 hw]
        exact hs.2.2
      rw [one_le_add_one_iff] at h2
      exact h2
  · intro h
    constructor
    · intro p hp
      have h1 := h.1 p hp
      refine ⟨h1.1, ?_⟩
      rw [lemA_identity w1 w2 p.s1 p.s2 hw, one_le_add_one_iff]
      exact h1.2
    · have hs := h.2
      refine ⟨hs.1, hs.2.1, ?_⟩
      rw [lemA_identity w1 w2 (witSucc a z).2.s1 (witSucc a z).2.s2 hw,
        one_le_add_one_iff]
      exact hs.2.2

/-! ## The rung interface and the master equation (Theorem S2) -/

/-- The θ < 1 family's defining convention: a tube value `λᵢ ≤ 0`
rejects the plan. -/
def CollapseSafe (a : WitAct K) (z : WitState K) : Prop :=
  ∀ p, witTube a z p → (0 < 1 + p.s1 ∧ 0 < 1 + p.s2)

/-- The θ-rung per-plan condition, θ > 0 sign (the aggregate condition
`M_θ ≥ 1` enters affine in the weight through the power interface
`pw = (·)^θ`). -/
def RungCond (pw : K → K) (w1 w2 : K) (a : WitAct K) (z : WitState K) : Prop :=
  (∀ p, witTube a z p →
      (0 ≤ p.x ∧ 1 ≤ w1 * pw (1 + p.s1) + w2 * pw (1 + p.s2))) ∧
  ((witSucc a z).1 = true ∧ 0 ≤ (witSucc a z).2.x ∧
      1 ≤ w1 * pw (1 + (witSucc a z).2.s1) + w2 * pw (1 + (witSucc a z).2.s2))

/-- The θ < 0 sign (the comparison flips with the sign of `1/θ`). -/
def RungCondNeg (pw : K → K) (w1 w2 : K) (a : WitAct K) (z : WitState K) : Prop :=
  (∀ p, witTube a z p →
      (0 ≤ p.x ∧ w1 * pw (1 + p.s1) + w2 * pw (1 + p.s2) ≤ 1)) ∧
  ((witSucc a z).1 = true ∧ 0 ≤ (witSucc a z).2.x ∧
      w1 * pw (1 + (witSucc a z).2.s1) + w2 * pw (1 + (witSucc a z).2.s2) ≤ 1)

/-- The θ < 1 members carry the collapse convention. -/
def ThetaSubAdm (pw : K → K) (w1 w2 : K) (a : WitAct K) (z : WitState K) : Prop :=
  CollapseSafe a z ∧ RungCondNeg pw w1 w2 a z

def ThetaMidAdm (pw : K → K) (w1 w2 : K) (a : WitAct K) (z : WitState K) : Prop :=
  CollapseSafe a z ∧ RungCond pw w1 w2 a z

/-- Normalized weights (the θ-family's protocol). -/
def WNorm (w1 w2 : K) : Prop := 0 ≤ w1 ∧ 0 ≤ w2 ∧ w1 + w2 = 1

/-- Protocol 2 under the θ-rung on the deterministic menu. -/
def DiagAccPos (pw : K → K) (z : WitState K) : Prop :=
  ∀ w1 w2, WNorm w1 w2 → ∃ a : DetAct, RungCond pw w1 w2 (.det a) z

def DiagAccNeg (pw : K → K) (z : WitState K) : Prop :=
  ∀ w1 w2, WNorm w1 w2 → ∃ a : DetAct, ThetaSubAdm pw w1 w2 (.det a) z

/-- The diagonal-hypotheses bundle. -/
def DiagHyps (z : WitState K) : Prop :=
  InX0 z ∧ z.x < 1 ∧ z.s1 = z.s2 ∧ 1 < z.s1 ∧ z.s1 < natK 2

/-- **Lemma B**(i): θ < 1 members' admissibility forces the positivity
rider — the collapse convention is the family's defining property. -/
theorem lemB_reject {_pw : K → K} {w1 w2 : K} {a : WitAct K} {z : WitState K}
    {rung : Prop} (h : CollapseSafe a z ∧ rung) : CollapseSafe a z := h.1

/-! ## The master-equation reduction (the averaging argument)

On the gap-region diagonal `z = (x < 1, s, s)`, `1 < s < 2`, the θ-rung
protocol of the substitutability extension collapses to the paper's
single master comparison.  The trough values of the two serving plans
are `(s-1, s+1)` and `(s+1, s-1)`, whose rung aggregates at any weight
sum to the weight-independent `A + B` (`cross_sum`), so one of the two
plans always covers at least `(A+B)/2` — the halving of
`averaging_step` — and the equal weight is the binding one.  θ > 0:
`accept ↔ (s-1)^θ + (s+1)^θ ≥ 2`;  θ < 0: the comparison flips to
`≤ 2`. -/

/-- `1/2 + 1/2 = 1`. -/
theorem one_half_add_one_half {K : Type} [OrdField K] :
    (natK 1 / natK 2 + natK 1 / natK 2 : K) = 1 := by
  have h2 : (1 : Nat) + 1 = 2 := rfl
  rw [div_add_div_same natK_two_ne_zero, ← natK_add, h2,
    div_self natK_two_ne_zero]

theorem one_half_nonneg {K : Type} [OrdField K] : (0 : K) ≤ natK 1 / natK 2 :=
  div_nonneg (natK_nonneg 1) (natK_pos (by omega))

theorem one_half_pos {K : Type} [OrdField K] : (0 : K) < natK 1 / natK 2 :=
  div_pos (natK_pos (by omega)) (natK_pos (by omega))

/-- `2 · (1/2) = 1`. -/
theorem two_mul_one_half {K : Type} [OrdField K] :
    natK 2 * (natK 1 / natK 2) = (1 : K) := by
  rw [mul_comm]
  have h : (natK 1 / natK 2 : K) * natK 2 = natK 1 :=
    div_mul_cancel natK_two_ne_zero (natK 1)
  rw [h, natK_one]

theorem wNorm_one_half {K : Type} [OrdField K] :
    WNorm (natK 1 / natK 2 : K) (natK 1 / natK 2) :=
  ⟨one_half_nonneg, one_half_nonneg, one_half_add_one_half⟩

/-- `0 < 1 + a` whenever `0 ≤ a`. -/
theorem zero_lt_one_add {a : K} (ha : 0 ≤ a) : 0 < 1 + a :=
  lt_of_lt_of_le zero_lt_one ((one_le_add_one_iff a).mpr ha)

/-- `0 < a + 1` whenever `0 ≤ a`. -/
theorem zero_lt_add_one {a : K} (ha : 0 ≤ a) : 0 < a + 1 := by
  rw [add_comm]
  exact zero_lt_one_add ha

/-- A normalized weight pair lies in the nonnegative cone. -/
theorem wNorm_wPos {w1 w2 : K} (hw : WNorm w1 w2) : WPos w1 w2 := by
  refine ⟨hw.1, hw.2.1, ?_⟩
  by_cases h1 : w1 = 0
  · right
    intro h2
    have hw2 : w1 + w2 = 1 := hw.2.2
    rw [h1, h2, add_zero] at hw2
    exact zero_ne_one' hw2
  · left
    exact h1

/-- `w₁ + w₂ = 1` implies `w₁·c + w₂·c = c`. -/
theorem wsum_const {w1 w2 : K} (hw : w1 + w2 = 1) (c : K) :
    w1 * c + w2 * c = c := by
  rw [← right_distrib, hw, one_mul']

/-- `a - 2 + 1 = a - 1`. -/
theorem sub_two_add_one (a : K) : a - natK 2 + 1 = a - 1 := by
  have h2 : natK 2 = (1 : K) + 1 := by rw [← two_mul (1 : K), mul_one]
  rw [h2, sub_add_add_cancel]

/-- `1 + (a - 2) = a - 1`. -/
theorem one_add_sub_two (a : K) : 1 + (a - natK 2) = a - 1 := by
  rw [add_comm, sub_two_add_one]

/-- `1 + 1 = 2`. -/
theorem one_add_one_eq_two {K : Type} [OrdField K] : (1 : K) + 1 = natK 2 := by
  rw [← two_mul (1 : K), mul_one]

/-- `0 < a - 1` when `1 < a`. -/
theorem sub_one_pos {a : K} (h : 1 < a) : 0 < a - 1 := by
  have h1 : 1 - a < 0 := sub_lt_zero.mpr h
  rw [← neg_sub]
  exact neg_pos' h1

/-- On the diagonal, `1 + z.s₂ = s + 1`. -/
theorem one_add_s2 (z : WitState K) (hz : DiagHyps z) :
    1 + z.s2 = z.s1 + 1 := by
  rw [← hz.2.2.1, add_comm 1 z.s1]

/-- The averaging step (constructive halving): if two aggregates sum to
at least `2`, one of them is at least `1`. -/
theorem averaging_step (F S : K) (h : natK 2 ≤ F + S) :
    (1 : K) ≤ F ∨ (1 : K) ≤ S := by
  have key : ∀ T : K, natK 2 ≤ T + T → (1 : K) ≤ T := by
    intro T hT
    have h3 : natK 2 * (1 : K) ≤ natK 2 * T := by
      rw [mul_one, two_mul]
      exact hT
    exact mul_le_cancel_left natK_two_pos h3
  cases le_total F S with
  | inl hFSle => exact Or.inr (key S (le_trans h (add_le_add_right hFSle S)))
  | inr hSFle => exact Or.inl (key F (le_trans h (add_le_add_left hSFle F)))

/-- The averaging step, `≤` form. -/
theorem averaging_step_neg (F S : K) (h : F + S ≤ natK 2) :
    F ≤ (1 : K) ∨ S ≤ (1 : K) := by
  have key : ∀ T : K, T + T ≤ natK 2 → T ≤ (1 : K) := by
    intro T hT
    have h3 : natK 2 * T ≤ natK 2 * (1 : K) := by
      rw [mul_one, two_mul]
      exact hT
    exact mul_le_cancel_left natK_two_pos h3
  cases le_total F S with
  | inl hFSle => exact Or.inl (key F (le_trans (add_le_add_left hFSle F) h))
  | inr hSFle => exact Or.inr (key S (le_trans (add_le_add_right hSFle S) h))

/-- The collapse convention is automatic for every deterministic plan on
the diagonal (all floor-referenced indices stay a full unit above the
collapse level). -/
theorem collapse_safe_all_det (z : WitState K) (hz : DiagHyps z) (a : DetAct) :
    CollapseSafe (.det a) z := by
  have hs1 : 0 < z.s1 - 1 := sub_one_pos hz.2.2.2.1
  have hs2 : 0 < z.s1 + 1 := zero_lt_add_one hz.1.2.1
  intro p hp
  cases a with
  | noswitch =>
      rw [hp]
      exact ⟨zero_lt_one_add hz.1.2.1, zero_lt_one_add hz.1.2.2⟩
  | fast =>
      have h1 : z.s1 - 1 ≤ 1 + p.s1 := by
        rw [← one_add_sub_two]
        exact add_le_add_left hp.2.2.1 1
      rw [hp.2.1, one_add_s2 z hz]
      exact ⟨lt_of_lt_of_le hs1 h1, hs2⟩
  | slow =>
      have h1 : z.s1 - 1 ≤ 1 + p.s2 := by
        rw [← one_add_sub_two, hz.2.2.1]
        exact add_le_add_left hp.2.2.1 1
      rw [hp.2.1, add_comm 1 z.s1]
      exact ⟨hs2, lt_of_lt_of_le hs1 h1⟩
  | staged =>
      have h1 : (1 : K) ≤ 1 + p.s1 :=
        (one_le_add_one_iff p.s1).mpr (le_trans hz.1.2.1 hp.2.2.1)
      have h2 : (1 : K) ≤ 1 + p.s2 :=
        (one_le_add_one_iff p.s2).mpr (le_trans hz.1.2.2 hp.2.2.2.2.1)
      exact ⟨lt_of_lt_of_le zero_lt_one h1, lt_of_lt_of_le zero_lt_one h2⟩

/-- The θ-rung condition for FAST from the trough comparison
(θ > 0 sign, monotone power interface). -/
theorem rungCond_fast_of_trough {pw : K → K}
    (hmono : ∀ a b, 0 ≤ a → a ≤ b → pw a ≤ pw b) (z : WitState K)
    (hz : DiagHyps z) {w1 w2 : K} (hw : WNorm w1 w2)
    (h : (1 : K) ≤ w1 * pw (z.s1 - 1) + w2 * pw (z.s1 + 1)) :
    RungCond pw w1 w2 (.det .fast) z := by
  have hs1m1 : 0 ≤ z.s1 - 1 := le_of_lt (sub_one_pos hz.2.2.2.1)
  have hs2 : 0 < z.s1 + 1 := zero_lt_add_one hz.1.2.1
  have hAB : pw (z.s1 - 1) ≤ pw (z.s1 + 1) :=
    hmono _ _ hs1m1
      (le_trans (sub_le_self z.s1 1 zero_le_one')
        (le_add_right z.s1 1 zero_le_one'))
  refine ⟨?_, ⟨rfl, hz.1.1, ?_⟩⟩
  · intro p hp
    have hx : 0 ≤ p.x := by rw [hp.1]; exact hz.1.1
    refine ⟨hx, ?_⟩
    have hb1 : pw (z.s1 - 1) ≤ pw (1 + p.s1) := by
      refine hmono _ _ hs1m1 ?_
      rw [← one_add_sub_two]
      exact add_le_add_left hp.2.2.1 1
    have hb2 : pw (1 + p.s2) = pw (z.s1 + 1) := by
      rw [hp.2.1, one_add_s2 z hz]
    have h1 : w1 * pw (z.s1 - 1) + w2 * pw (z.s1 + 1)
        ≤ w1 * pw (1 + p.s1) + w2 * pw (1 + p.s2) := by
      rw [hb2]
      exact add_le_add (mul_le_mul_of_nonneg_left hb1 hw.1) (le_refl _)
    exact le_trans h h1
  · show (1 : K) ≤ w1 * pw (1 + (z.s1 + eGain))
      + w2 * pw (1 + (z.s2 + eGain))
    rw [← hz.2.2.1, wsum_const hw.2.2]
    have hB1 : (1 : K) ≤ pw (z.s1 + 1) := by
      have h5 : w1 * pw (z.s1 - 1) + w2 * pw (z.s1 + 1)
          ≤ w1 * pw (z.s1 + 1) + w2 * pw (z.s1 + 1) :=
        add_le_add (mul_le_mul_of_nonneg_left hAB hw.1) (le_refl _)
      rw [wsum_const hw.2.2] at h5
      exact le_trans h h5
    have hS : pw (z.s1 + 1) ≤ pw (1 + (z.s1 + eGain)) := by
      refine hmono _ _ (le_of_lt hs2) ?_
      rw [add_comm z.s1 1]
      exact add_le_add_left (le_add_right z.s1 eGain eGain_nonneg) 1
    exact le_trans hB1 hS

/-- The θ-rung condition for SLOW from the trough comparison
(θ > 0 sign). -/
theorem rungCond_slow_of_trough {pw : K → K}
    (hmono : ∀ a b, 0 ≤ a → a ≤ b → pw a ≤ pw b) (z : WitState K)
    (hz : DiagHyps z) {w1 w2 : K} (hw : WNorm w1 w2)
    (h : (1 : K) ≤ w1 * pw (z.s1 + 1) + w2 * pw (z.s1 - 1)) :
    RungCond pw w1 w2 (.det .slow) z := by
  have hs1m1 : 0 ≤ z.s1 - 1 := le_of_lt (sub_one_pos hz.2.2.2.1)
  have hs2 : 0 < z.s1 + 1 := zero_lt_add_one hz.1.2.1
  have hAB : pw (z.s1 - 1) ≤ pw (z.s1 + 1) :=
    hmono _ _ hs1m1
      (le_trans (sub_le_self z.s1 1 zero_le_one')
        (le_add_right z.s1 1 zero_le_one'))
  refine ⟨?_, ⟨rfl, hz.1.1, ?_⟩⟩
  · intro p hp
    have hx : 0 ≤ p.x := by rw [hp.1]; exact hz.1.1
    refine ⟨hx, ?_⟩
    have hb1 : pw (z.s1 - 1) ≤ pw (1 + p.s2) := by
      refine hmono _ _ hs1m1 ?_
      rw [← one_add_sub_two, hz.2.2.1]
      exact add_le_add_left hp.2.2.1 1
    have hb2 : pw (1 + p.s1) = pw (z.s1 + 1) := by
      rw [hp.2.1, add_comm 1 z.s1]
    have h1 : w1 * pw (z.s1 + 1) + w2 * pw (z.s1 - 1)
        ≤ w1 * pw (1 + p.s1) + w2 * pw (1 + p.s2) := by
      rw [hb2]
      exact add_le_add (le_refl _) (mul_le_mul_of_nonneg_left hb1 hw.2.1)
    exact le_trans h h1
  · show (1 : K) ≤ w1 * pw (1 + (z.s1 + eGain))
      + w2 * pw (1 + (z.s2 + eGain))
    rw [← hz.2.2.1, wsum_const hw.2.2]
    have hB1 : (1 : K) ≤ pw (z.s1 + 1) := by
      have h5 : w1 * pw (z.s1 + 1) + w2 * pw (z.s1 - 1)
          ≤ w1 * pw (z.s1 + 1) + w2 * pw (z.s1 + 1) :=
        add_le_add (le_refl _) (mul_le_mul_of_nonneg_left hAB hw.2.1)
      rw [wsum_const hw.2.2] at h5
      exact le_trans h h5
    have hS : pw (z.s1 + 1) ≤ pw (1 + (z.s1 + eGain)) := by
      refine hmono _ _ (le_of_lt hs2) ?_
      rw [add_comm z.s1 1]
      exact add_le_add_left (le_add_right z.s1 eGain eGain_nonneg) 1
    exact le_trans hB1 hS

/-- **The master-equation reduction** (θ > 0 sign): on the diagonal, the
θ-rung protocol accepts exactly when the master comparison
`(s-1)^θ + (s+1)^θ ≥ 2` holds — the averaging argument. -/
theorem master_reduction_pos {pw : K → K}
    (hmono : ∀ a b, 0 ≤ a → a ≤ b → pw a ≤ pw b) (z : WitState K)
    (hz : DiagHyps z) :
    DiagAccPos pw z ↔ (natK 2 : K) ≤ pw (z.s1 - 1) + pw (z.s1 + 1) := by
  constructor
  · intro hd
    have hpair := hd (natK 1 / natK 2) (natK 1 / natK 2) wNorm_one_half
    cases hpair with
    | intro a ha =>
        cases a with
        | noswitch => exact Bool.noConfusion ha.2.1
        | staged =>
            have hbot : witTube (.det .staged) z ⟨z.x - 1, z.s1, z.s2⟩ :=
              ⟨le_refl _, sub_le_self z.x 1 zero_le_one', le_refl _,
                le_add_right z.s1 eGain eGain_nonneg, le_refl _,
                le_add_right z.s2 eGain eGain_nonneg⟩
            have h1 := ha.1 _ hbot
            have h2 : z.x - 1 < 0 := sub_lt_zero.mpr hz.2.1
            exact absurd h1.1 (not_le_of_lt h2)
        | fast =>
            have hdip : witTube (.det .fast) z ⟨z.x, z.s1 - natK 2, z.s2⟩ :=
              ⟨rfl, rfl, le_refl _, sub_le_self z.s1 (natK 2) (natK_nonneg 2)⟩
            have h1 := ha.1 _ hdip
            rw [one_add_sub_two, one_add_s2 z hz] at h1
            have h3 : (natK 1 / natK 2) * (pw (z.s1 - 1) + pw (z.s1 + 1))
                = (natK 1 / natK 2) * pw (z.s1 - 1)
                + (natK 1 / natK 2) * pw (z.s1 + 1) :=
              left_distrib _ _ _
            rw [← h3] at h1
            have h4 : natK 2 * 1
                ≤ natK 2 * ((natK 1 / natK 2)
                  * (pw (z.s1 - 1) + pw (z.s1 + 1))) :=
              mul_le_mul_of_nonneg_left h1.2 (natK_nonneg 2)
            rw [mul_one, ← mul_assoc, two_mul_one_half, one_mul'] at h4
            exact h4
        | slow =>
            have hdip : witTube (.det .slow) z ⟨z.x, z.s1, z.s2 - natK 2⟩ :=
              ⟨rfl, rfl, le_refl _, sub_le_self z.s2 (natK 2) (natK_nonneg 2)⟩
            have h1 := ha.1 _ hdip
            rw [← hz.2.2.1, one_add_sub_two, add_comm 1 z.s1] at h1
            have h3 : (natK 1 / natK 2) * (pw (z.s1 - 1) + pw (z.s1 + 1))
                = (natK 1 / natK 2) * pw (z.s1 + 1)
                + (natK 1 / natK 2) * pw (z.s1 - 1) := by
              rw [left_distrib,
                add_comm ((natK 1 / natK 2) * pw (z.s1 - 1))
                  ((natK 1 / natK 2) * pw (z.s1 + 1))]
            rw [← h3] at h1
            have h4 : natK 2 * 1
                ≤ natK 2 * ((natK 1 / natK 2)
                  * (pw (z.s1 - 1) + pw (z.s1 + 1))) :=
              mul_le_mul_of_nonneg_left h1.2 (natK_nonneg 2)
            rw [mul_one, ← mul_assoc, two_mul_one_half, one_mul'] at h4
            exact h4
  · intro hmaster w1 w2 hw
    have hFS : natK 2 ≤ (w1 * pw (z.s1 - 1) + w2 * pw (z.s1 + 1))
        + (w1 * pw (z.s1 + 1) + w2 * pw (z.s1 - 1)) := by
      rw [cross_sum w1 w2 (pw (z.s1 - 1)) (pw (z.s1 + 1)), hw.2.2, one_mul']
      exact hmaster
    cases averaging_step _ _ hFS with
    | inl hF => exact ⟨.fast, rungCond_fast_of_trough hmono z hz hw hF⟩
    | inr hS => exact ⟨.slow, rungCond_slow_of_trough hmono z hz hw hS⟩

/-- The θ-rung condition for FAST from the trough comparison
(θ < 0 sign, antitone power interface). -/
theorem rungCondNeg_fast_of_trough {pw : K → K}
    (hanti : ∀ a b, 0 < a → a ≤ b → pw b ≤ pw a) (z : WitState K)
    (hz : DiagHyps z) {w1 w2 : K} (hw : WNorm w1 w2)
    (h : w1 * pw (z.s1 - 1) + w2 * pw (z.s1 + 1) ≤ (1 : K)) :
    ThetaSubAdm pw w1 w2 (.det .fast) z := by
  have hs1m1 : 0 < z.s1 - 1 := sub_one_pos hz.2.2.2.1
  have hs2 : 0 < z.s1 + 1 := zero_lt_add_one hz.1.2.1
  have hAB : pw (z.s1 + 1) ≤ pw (z.s1 - 1) :=
    hanti _ _ hs1m1
      (le_trans (sub_le_self z.s1 1 zero_le_one')
        (le_add_right z.s1 1 zero_le_one'))
  refine ⟨collapse_safe_all_det z hz .fast, ?_, ⟨rfl, hz.1.1, ?_⟩⟩
  · intro p hp
    have hx : 0 ≤ p.x := by rw [hp.1]; exact hz.1.1
    refine ⟨hx, ?_⟩
    have hb1 : pw (1 + p.s1) ≤ pw (z.s1 - 1) := by
      refine hanti _ _ hs1m1 ?_
      rw [← one_add_sub_two]
      exact add_le_add_left hp.2.2.1 1
    have hb2 : pw (1 + p.s2) = pw (z.s1 + 1) := by
      rw [hp.2.1, one_add_s2 z hz]
    have h1 : w1 * pw (1 + p.s1) + w2 * pw (1 + p.s2)
        ≤ w1 * pw (z.s1 - 1) + w2 * pw (z.s1 + 1) := by
      rw [hb2]
      exact add_le_add (mul_le_mul_of_nonneg_left hb1 hw.1) (le_refl _)
    exact le_trans h1 h
  · show w1 * pw (1 + (z.s1 + eGain)) + w2 * pw (1 + (z.s2 + eGain))
        ≤ (1 : K)
    rw [← hz.2.2.1, wsum_const hw.2.2]
    have hB1 : pw (z.s1 + 1) ≤ (1 : K) := by
      have h5 : pw (z.s1 + 1)
          = w1 * pw (z.s1 + 1) + w2 * pw (z.s1 + 1) :=
        (wsum_const hw.2.2 _).symm
      rw [h5]
      refine le_trans (add_le_add (mul_le_mul_of_nonneg_left hAB hw.1)
        (le_refl _)) h
    have hS : pw (1 + (z.s1 + eGain)) ≤ pw (z.s1 + 1) := by
      refine hanti _ _ hs2 ?_
      rw [add_comm z.s1 1]
      exact add_le_add_left (le_add_right z.s1 eGain eGain_nonneg) 1
    exact le_trans hS hB1

/-- The θ-rung condition for SLOW from the trough comparison
(θ < 0 sign). -/
theorem rungCondNeg_slow_of_trough {pw : K → K}
    (hanti : ∀ a b, 0 < a → a ≤ b → pw b ≤ pw a) (z : WitState K)
    (hz : DiagHyps z) {w1 w2 : K} (hw : WNorm w1 w2)
    (h : w1 * pw (z.s1 + 1) + w2 * pw (z.s1 - 1) ≤ (1 : K)) :
    ThetaSubAdm pw w1 w2 (.det .slow) z := by
  have hs1m1 : 0 < z.s1 - 1 := sub_one_pos hz.2.2.2.1
  have hs2 : 0 < z.s1 + 1 := zero_lt_add_one hz.1.2.1
  have hAB : pw (z.s1 + 1) ≤ pw (z.s1 - 1) :=
    hanti _ _ hs1m1
      (le_trans (sub_le_self z.s1 1 zero_le_one')
        (le_add_right z.s1 1 zero_le_one'))
  refine ⟨collapse_safe_all_det z hz .slow, ?_, ⟨rfl, hz.1.1, ?_⟩⟩
  · intro p hp
    have hx : 0 ≤ p.x := by rw [hp.1]; exact hz.1.1
    refine ⟨hx, ?_⟩
    have hb1 : pw (1 + p.s2) ≤ pw (z.s1 - 1) := by
      refine hanti _ _ hs1m1 ?_
      rw [← one_add_sub_two, hz.2.2.1]
      exact add_le_add_left hp.2.2.1 1
    have hb2 : pw (1 + p.s1) = pw (z.s1 + 1) := by
      rw [hp.2.1, add_comm 1 z.s1]
    have h1 : w1 * pw (1 + p.s1) + w2 * pw (1 + p.s2)
        ≤ w1 * pw (z.s1 + 1) + w2 * pw (z.s1 - 1) := by
      rw [hb2]
      exact add_le_add (le_refl _) (mul_le_mul_of_nonneg_left hb1 hw.2.1)
    exact le_trans h1 h
  · show w1 * pw (1 + (z.s1 + eGain)) + w2 * pw (1 + (z.s2 + eGain))
        ≤ (1 : K)
    rw [← hz.2.2.1, wsum_const hw.2.2]
    have hB1 : pw (z.s1 + 1) ≤ (1 : K) := by
      have h5 : pw (z.s1 + 1)
          = w1 * pw (z.s1 + 1) + w2 * pw (z.s1 + 1) :=
        (wsum_const hw.2.2 _).symm
      rw [h5]
      refine le_trans (add_le_add (le_refl _)
        (mul_le_mul_of_nonneg_left hAB hw.2.1)) h
    have hS : pw (1 + (z.s1 + eGain)) ≤ pw (z.s1 + 1) := by
      refine hanti _ _ hs2 ?_
      rw [add_comm z.s1 1]
      exact add_le_add_left (le_add_right z.s1 eGain eGain_nonneg) 1
    exact le_trans hS hB1

/-- **The master-equation reduction** (θ < 0 sign): on the diagonal, the
θ-rung protocol accepts exactly when the flipped master comparison
`(s-1)^θ + (s+1)^θ ≤ 2` holds. -/
theorem master_reduction_neg {pw : K → K}
    (hanti : ∀ a b, 0 < a → a ≤ b → pw b ≤ pw a) (z : WitState K)
    (hz : DiagHyps z) :
    DiagAccNeg pw z ↔ pw (z.s1 - 1) + pw (z.s1 + 1) ≤ (natK 2 : K) := by
  constructor
  · intro hd
    have hpair := hd (natK 1 / natK 2) (natK 1 / natK 2) wNorm_one_half
    cases hpair with
    | intro a ha =>
        cases a with
        | noswitch => exact Bool.noConfusion ha.2.2.1
        | staged =>
            have hbot : witTube (.det .staged) z ⟨z.x - 1, z.s1, z.s2⟩ :=
              ⟨le_refl _, sub_le_self z.x 1 zero_le_one', le_refl _,
                le_add_right z.s1 eGain eGain_nonneg, le_refl _,
                le_add_right z.s2 eGain eGain_nonneg⟩
            have h1 := ha.2.1 _ hbot
            have h2 : z.x - 1 < 0 := sub_lt_zero.mpr hz.2.1
            exact absurd h1.1 (not_le_of_lt h2)
        | fast =>
            have hdip : witTube (.det .fast) z ⟨z.x, z.s1 - natK 2, z.s2⟩ :=
              ⟨rfl, rfl, le_refl _, sub_le_self z.s1 (natK 2) (natK_nonneg 2)⟩
            have h1 := ha.2.1 _ hdip
            rw [one_add_sub_two, one_add_s2 z hz] at h1
            have h3 : (natK 1 / natK 2) * (pw (z.s1 - 1) + pw (z.s1 + 1))
                = (natK 1 / natK 2) * pw (z.s1 - 1)
                + (natK 1 / natK 2) * pw (z.s1 + 1) :=
              left_distrib _ _ _
            rw [← h3] at h1
            have h4 : natK 2 * ((natK 1 / natK 2)
                * (pw (z.s1 - 1) + pw (z.s1 + 1))) ≤ natK 2 * 1 :=
              mul_le_mul_of_nonneg_left h1.2 (natK_nonneg 2)
            rw [← mul_assoc, two_mul_one_half, one_mul', mul_one] at h4
            exact h4
        | slow =>
            have hdip : witTube (.det .slow) z ⟨z.x, z.s1, z.s2 - natK 2⟩ :=
              ⟨rfl, rfl, le_refl _, sub_le_self z.s2 (natK 2) (natK_nonneg 2)⟩
            have h1 := ha.2.1 _ hdip
            rw [← hz.2.2.1, one_add_sub_two, add_comm 1 z.s1] at h1
            have h3 : (natK 1 / natK 2) * (pw (z.s1 - 1) + pw (z.s1 + 1))
                = (natK 1 / natK 2) * pw (z.s1 + 1)
                + (natK 1 / natK 2) * pw (z.s1 - 1) := by
              rw [left_distrib,
                add_comm ((natK 1 / natK 2) * pw (z.s1 - 1))
                  ((natK 1 / natK 2) * pw (z.s1 + 1))]
            rw [← h3] at h1
            have h4 : natK 2 * ((natK 1 / natK 2)
                * (pw (z.s1 - 1) + pw (z.s1 + 1))) ≤ natK 2 * 1 :=
              mul_le_mul_of_nonneg_left h1.2 (natK_nonneg 2)
            rw [← mul_assoc, two_mul_one_half, one_mul', mul_one] at h4
            exact h4
  · intro hmaster w1 w2 hw
    have hFS : (w1 * pw (z.s1 - 1) + w2 * pw (z.s1 + 1))
        + (w1 * pw (z.s1 + 1) + w2 * pw (z.s1 - 1)) ≤ natK 2 := by
      rw [cross_sum w1 w2 (pw (z.s1 - 1)) (pw (z.s1 + 1)), hw.2.2, one_mul']
      exact hmaster
    cases averaging_step_neg _ _ hFS with
    | inl hF =>
        exact ⟨.fast, rungCondNeg_fast_of_trough hanti z hz hw hF⟩
    | inr hS =>
        exact ⟨.slow, rungCondNeg_slow_of_trough hanti z hz hw hS⟩

/-- Protocol 2 under the θ ∈ (0,1) rungs, with the collapse-convention
rider (these are θ < 1 members). -/
def DiagAccMid (pw : K → K) (z : WitState K) : Prop :=
  ∀ w1 w2, WNorm w1 w2 → ∃ a : DetAct, ThetaMidAdm pw w1 w2 (.det a) z

/-- On the diagonal, the convention-carrying θ ∈ (0,1) protocol agrees
with the plain positive-sign protocol (the convention is automatic for
every deterministic plan there). -/
theorem diagAccMid_iff_pos {pw : K → K} (z : WitState K) (hz : DiagHyps z) :
    DiagAccMid pw z ↔ DiagAccPos pw z := by
  constructor
  · intro hd w1 w2 hw
    cases hd w1 w2 hw with
    | intro a ha => exact ⟨a, ha.2⟩
  · intro hd w1 w2 hw
    cases hd w1 w2 hw with
    | intro a ha => exact ⟨a, collapse_safe_all_det z hz a, ha⟩

/-! ## Theorem S2(i) — the pointwise half

Every gap state is accepted by the θ = 1 member (the linear
aggregate): by Lemma A's engine equivalence, the compensatory engine
serves every weight (Theorem 5(2)/(4)), so full Leontief is never
necessary at a fixed state. -/

/-- **Theorem S2(i)**: the θ = 1 rung accepts every gap state — the
linear member is the pointwise certificate. -/
theorem s2_i_linear_accepts (z : WitState K) (hz : InX0 z) (hg : IsGap z)
    (w1 w2 : K) (hw : WNorm w1 w2) :
    ∃ a : DetAct, Theta1Adm w1 w2 (.det a) z := by
  have hfp : FPAgg z := (thm5_4 z hz).mpr hg
  have hvw := hfp.1 w1 w2 (wNorm_wPos hw)
  cases hvw with
  | intro a ha => exact ⟨a, (lemA_engine hw.2.2 (.det a) z).mpr ha⟩

/-! ## The Leontief identification (`V⁰ = V_typ`)

The Leontief member's acceptance (`minᵢ λᵢ ≥ 1` along the tube) does
not involve the weight, so its protocol collapses into the common-plan
criterion — the typed operator. -/

/-- **The Leontief identification**: the σ = 0 member's protocol
acceptance set is the typed operator's accepted set. -/
theorem leontief_eq_vtyp (z : WitState K) :
    (∀ w1 w2 : K, WNorm w1 w2 → ∃ a : DetAct, TypedAdm (.det a) z) ↔ VTyp z := by
  constructor
  · intro hd
    have hpair := hd (natK 1 / natK 2) (natK 1 / natK 2) wNorm_one_half
    cases hpair with
    | intro a ha => exact ⟨a, ha⟩
  · intro hV _w1 _w2 _
    cases hV with
    | intro a ha => exact ⟨a, ha⟩

/-- **Theorem S2(ii), Leontief side**: the σ = 0 member accepts no gap
state — the only uniformly safe aggregator of the covered family. -/
theorem s2_leontief_rejects_gaps (z : WitState K) (hz : InX0 z)
    (hg : IsGap z) :
    ¬ ∀ w1 w2 : K, WNorm w1 w2 → ∃ a : DetAct, TypedAdm (.det a) z := by
  intro h
  have hfp : FPAgg z := (thm5_4 z hz).mpr hg
  exact hfp.2 ((leontief_eq_vtyp z).mp h)

/-! ## Theorem S2(ii) — the false-certification witnesses

For every rung of the ladder except the Leontief member there is an
exact rational interval of gap states the rung accepts — false
certification, since the typed operator rejects every gap state. -/

/-- Every diagonal state is a gap state. -/
theorem diagHyps_gap (z : WitState K) (hz : DiagHyps z) : IsGap z := by
  refine ⟨hz.2.1, hz.2.2.2.2, ?_, ?_⟩
  · rw [← hz.2.2.1]
    exact hz.2.2.2.2
  · rw [← hz.2.2.1, ← one_add_one_eq_two]
    exact add_le_add (le_of_lt hz.2.2.2.1) (le_of_lt hz.2.2.2.1)

/-- The typed operator rejects every diagonal state. -/
theorem diagHyps_not_vtyp (z : WitState K) (hz : DiagHyps z) : ¬ VTyp z := by
  have hfp : FPAgg z := (thm5_4 z hz.1).mpr (diagHyps_gap z hz)
  exact hfp.2

/-- **Theorem S2(ii), the harmonic member** (θ = -1, σ = 1/2): the rung
false-certifies the exact rational interval `[13/8, 2)` of the diagonal
— the golden-ratio floor's Fibonacci upper witness. -/
theorem s2_ii_harmonic_interval (z : WitState K) (hz : DiagHyps z)
    (hs : natK 13 / natK 8 ≤ z.s1) :
    DiagAccNeg (fun x => x⁻¹) z := by
  refine (master_reduction_neg (fun a b ha hab => inv_le_inv ha hab) z hz).mpr ?_
  show (z.s1 - 1)⁻¹ + (z.s1 + 1)⁻¹ ≤ natK 2
  have h1 : 0 < z.s1 - 1 := sub_one_pos hz.2.2.2.1
  have h2 : 0 < z.s1 + 1 := zero_lt_add_one hz.1.2.1
  have e1 : (z.s1 - 1)⁻¹ = (1 : K) / (z.s1 - 1) := by
    rw [div_eq, one_mul']
  have e2 : (z.s1 + 1)⁻¹ = (1 : K) / (z.s1 + 1) := by
    rw [div_eq, one_mul']
  rw [e1, e2, div_add_div (ne_of_gt h1) (ne_of_gt h2), one_mul', one_mul']
  rw [div_le_iff (mul_pos h1 h2)]
  -- (z.s1 + 1) + (z.s1 - 1) ≤ 2 * ((z.s1 - 1) * (z.s1 + 1))
  have h85 : natK 13 - natK 8 = (natK 5 : K) :=
    sub_add_eq (by rw [← natK_add])
  have e58 : natK 13 / natK 8 - 1 = (natK 5 / natK 8 : K) := by
    rw [← div_self (natK_ne_zero (n := 8) (by omega)), ← sub_div, h85]
  have hfive : natK 5 / natK 8 ≤ z.s1 - 1 := by
    rw [← e58]
    exact sub_le_sub_right hs 1
  have hsp : (1 : K) ≤ z.s1 * (z.s1 - 1) := by
    have t1 : natK 13 / natK 8 * (natK 5 / natK 8)
        ≤ natK 13 / natK 8 * (z.s1 - 1) :=
      mul_le_mul_of_nonneg_left hfive
        (div_nonneg (natK_nonneg 13) (natK_pos (n := 8) (by omega)))
    have t2 : natK 13 / natK 8 * (z.s1 - 1) ≤ z.s1 * (z.s1 - 1) :=
      mul_le_mul_of_nonneg_right hs (le_of_lt h1)
    have e65 : natK 13 / natK 8 * (natK 5 / natK 8)
        = (natK 13 * natK 5 / (natK 8 * natK 8) : K) :=
      div_mul_div (natK_ne_zero (n := 8) (by omega)) (natK_ne_zero (n := 8) (by omega))
    have ege : (1 : K) ≤ natK 13 * natK 5 / (natK 8 * natK 8) := by
      rw [le_div_iff (mul_pos (natK_pos (n := 8) (by omega))
        (natK_pos (n := 8) (by omega))), one_mul', ← natK_mul 8 8, ← natK_mul 13 5]
      exact natK_le (by omega)
    exact le_trans ege (le_trans (le_of_eq e65.symm) (le_trans t1 t2))
  have eL : (z.s1 + 1) + (z.s1 - 1) = natK 2 * z.s1 := by
    rw [sub_eq, add_comm4 z.s1 1 z.s1 (-1), add_neg_cancel, add_zero,
      ← two_mul z.s1]
  have eR : (z.s1 - 1) * (z.s1 + 1) = z.s1 * z.s1 - 1 := by
    rw [sub_mul, left_distrib, mul_one, one_mul', add_comm z.s1 1]
    exact add_sub_add_comm (z.s1 * z.s1) z.s1 1
  have eQ : z.s1 * z.s1 - z.s1 - 1 = z.s1 * (z.s1 - 1) - 1 := by
    rw [mul_sub, mul_one]
  rw [eL, eR]
  refine mul_le_mul_of_nonneg_left ?_ (natK_nonneg 2)
  refine sub_nonneg.mp ?_
  have reord : z.s1 * z.s1 - 1 - z.s1 = z.s1 * z.s1 - z.s1 - 1 := by
    rw [sub_eq, sub_eq, sub_eq, sub_eq, add_right_comm]
  rw [reord, eQ, sub_nonneg]
  exact hsp

/-- **Theorem S2(ii), the harmonic witness package**: the σ = 1/2 rung
false-certifies every diagonal gap state with `s ≥ 13/8`. -/
theorem s2_ii_harmonic_witness (z : WitState K) (hz : DiagHyps z)
    (hs : natK 13 / natK 8 ≤ z.s1) :
    DiagAccNeg (fun x => x⁻¹) z ∧ ¬ VTyp z :=
  ⟨s2_ii_harmonic_interval z hz hs, diagHyps_not_vtyp z hz⟩

/-- **Theorem S2(ii), the Fibonacci lower witness**: the harmonic rung
rejects `s = 8/5` — the golden-ratio floor's rational lower bracket
(the paper's Fibonacci pair `8/5 rejects / 13/8 accepts`). -/
theorem s2_ii_harmonic_reject (z : WitState K) (hz : DiagHyps z)
    (hs : z.s1 = natK 8 / natK 5) : ¬ DiagAccNeg (fun x => x⁻¹) z := by
  intro hd
  have hmaster :=
    (master_reduction_neg (fun a b ha hab => inv_le_inv ha hab) z hz).mp hd
  rw [hs] at hmaster
  have h53 : natK 8 - natK 5 = (natK 3 : K) :=
    sub_add_eq (by rw [← natK_add])
  have e1 : natK 8 / natK 5 - 1 = (natK 3 / natK 5 : K) := by
    rw [← div_self (natK_ne_zero (n := 5) (by omega)), ← sub_div, h53]
  have e2 : natK 8 / natK 5 + 1 = (natK 13 / natK 5 : K) := by
    rw [← div_self (natK_ne_zero (n := 5) (by omega)),
      div_add_div_same (natK_ne_zero (n := 5) (by omega)), ← natK_add]
  rw [e1, e2] at hmaster
  rw [div_inv (natK_ne_zero (n := 3) (by omega)) (natK_ne_zero (n := 5) (by omega)),
    div_inv (natK_ne_zero (n := 13) (by omega)) (natK_ne_zero (n := 5) (by omega)),
    div_add_div (natK_ne_zero (n := 3) (by omega)) (natK_ne_zero (n := 13) (by omega))] at hmaster
  rw [div_le_iff (mul_pos (natK_pos (n := 3) (by omega))
    (natK_pos (n := 13) (by omega)))] at hmaster
  -- natK 5 * natK 13 + natK 5 * natK 3 ≤ natK 2 * (natK 3 * natK 13)
  rw [← natK_mul 5 13, ← natK_mul 5 3, ← natK_add, ← natK_mul 3 13,
    ← natK_mul 2 (3 * 13)] at hmaster
  exact absurd (natK_le_iff.mp hmaster) (by omega)

/-- **Theorem S2(ii), the σ = 1/4 rung** (θ = -3): the paper's witness
`9/5` — the rung false-certifies the gap state. -/
theorem s2_ii_sigma_quarter_witness (z : WitState K) (hz : DiagHyps z)
    (hs : z.s1 = natK 9 / natK 5) :
    DiagAccNeg (fun x => (npow x 3)⁻¹) z ∧ ¬ VTyp z := by
  refine ⟨?_, diagHyps_not_vtyp z hz⟩
  refine (master_reduction_neg ?_ z hz).mpr ?_
  · intro a b ha hab
    exact inv_le_inv (npow_pos ha 3) (npow_mono hab (le_of_lt ha) 3)
  · show (npow (z.s1 - 1) 3)⁻¹ + (npow (z.s1 + 1) 3)⁻¹ ≤ natK 2
    rw [hs]
    have h94 : natK 9 - natK 5 = (natK 4 : K) :=
      sub_add_eq (by rw [← natK_add])
    have e1 : natK 9 / natK 5 - 1 = (natK 4 / natK 5 : K) := by
      rw [← div_self (natK_ne_zero (n := 5) (by omega)), ← sub_div, h94]
    have e2 : natK 9 / natK 5 + 1 = (natK 14 / natK 5 : K) := by
      rw [← div_self (natK_ne_zero (n := 5) (by omega)),
        div_add_div_same (natK_ne_zero (n := 5) (by omega)), ← natK_add]
    have e4 : npow (natK 4) 3 = (natK 64 : K) := by rw [npow_natK]
    have e5 : npow (natK 5) 3 = (natK 125 : K) := by rw [npow_natK]
    have e14 : npow (natK 14) 3 = (natK 2744 : K) := by rw [npow_natK]
    rw [e1, e2,
      npow_div (natK_ne_zero (n := 5) (by omega)) 3,
      npow_div (natK_ne_zero (n := 5) (by omega)) 3,
      div_inv (npow_ne_zero (natK_ne_zero (n := 4) (by omega)) 3)
        (npow_ne_zero (natK_ne_zero (n := 5) (by omega)) 3),
      div_inv (npow_ne_zero (natK_ne_zero (n := 14) (by omega)) 3)
        (npow_ne_zero (natK_ne_zero (n := 5) (by omega)) 3),
      e5, e4, e14,
      div_add_div (natK_ne_zero (n := 64) (by omega))
        (natK_ne_zero (n := 2744) (by omega)),
      div_le_iff (mul_pos (natK_pos (n := 64) (by omega))
        (natK_pos (n := 2744) (by omega)))]
    -- 125·2744 + 125·64 ≤ 2·(64·2744)
    rw [← natK_mul 125 2744, ← natK_mul 125 64, ← natK_add,
      ← natK_mul 64 2744, ← natK_mul 2 (64 * 2744)]
    exact natK_le (by omega)

/-! ## Theorem S2(ii) — the `∀m` false-certification family

Every negative-integer rung θ = -m (elasticity `σ = 1/(m+1)`) accepts
the whole rational interval `[2 - 2^-(m+1), 2)` of the diagonal — so
aggregators of arbitrarily small strictly-positive elasticity still
false-certify gap states (the interface-level rendition of the uniform
critical elasticity `inf_z σ*(z) = 0`).  The engine is a Bernoulli-type
lower bound proved here. -/

/-- `npow x 1 = x`. -/
theorem npow_one (x : K) : npow x 1 = x := by
  show x * npow x 0 = x
  rw [npow_zero, mul_one]

/-- `0 < 1 - a` when `a < 1`. -/
theorem one_sub_pos {a : K} (h : a < 1) : 0 < 1 - a := by
  have h1 : a - 1 < 0 := sub_lt_zero.mpr h
  rw [← neg_sub]
  exact neg_pos' h1

/-- `a ≤ c - b` when `a + b ≤ c`. -/
theorem le_sub_of_add {a b c : K} (h : a + b ≤ c) : a ≤ c - b := by
  have h1 : a + b + -b ≤ c + -b := add_le_add_right h (-b)
  rw [add_assoc, add_neg_cancel, add_zero] at h1
  rw [sub_eq]
  exact h1

/-- The Bernoulli-type lower bound: `1 - m·δ ≤ (1 - δ)^m`. -/
theorem bernoulli_lower {δ : K} (hδ1 : 0 ≤ δ) (hδ2 : δ ≤ 1) (m : Nat) :
    (1 : K) - natK m * δ ≤ npow (1 - δ) m := by
  induction m with
  | zero =>
      show (1 : K) - natK 0 * δ ≤ npow (1 - δ) 0
      rw [natK_zero, zero_mul, sub_zero, npow_zero]
      exact le_refl _
  | succ k ih =>
      have h0 : 0 ≤ 1 - δ := sub_nonneg.mpr hδ2
      have h1 : (1 - δ) * (1 - natK k * δ)
          ≤ (1 - δ) * npow (1 - δ) k :=
        mul_le_mul_of_nonneg_left ih h0
      have en : δ * (natK k * δ) = natK k * (δ * δ) := by
        rw [← mul_assoc, mul_comm δ (natK k), mul_assoc]
      have h2 : (1 - δ) * (1 - natK k * δ)
          = (1 : K) - natK (k + 1) * δ + natK k * (δ * δ) := by
        rw [sub_mul, one_mul', mul_sub, mul_one, en,
          sub_sub (1 - natK k * δ) δ (natK k * (δ * δ)), natK_succ,
          right_distrib, one_mul', sub_eq, sub_eq, sub_eq, neg_add_dist,
          ← add_assoc]
      have h3 : 0 ≤ natK k * (δ * δ) :=
        mul_nonneg (natK_nonneg k) (mul_nonneg hδ1 hδ1)
      rw [npow_succ]
      calc (1 : K) - natK (k + 1) * δ
          ≤ (1 : K) - natK (k + 1) * δ + natK k * (δ * δ) :=
            le_add_right _ _ h3
        _ = (1 - δ) * (1 - natK k * δ) := h2.symm
        _ ≤ (1 - δ) * npow (1 - δ) k := h1

/-- The halving bound: `m·(1/2)^m ≤ 1/2` for every `m ≥ 1`. -/
theorem half_pow_scaled (m : Nat) (hm : 1 ≤ m) :
    natK m * npow (natK 1 / natK 2) m ≤ (natK 1 / natK 2 : K) := by
  have key : ∀ n : Nat,
      natK (n + 1) * npow (natK 1 / natK 2) (n + 1) ≤ (natK 1 / natK 2 : K) := by
    intro n
    induction n with
    | zero =>
        show (natK 1 : K) * ((natK 1 / natK 2) * 1) ≤ natK 1 / natK 2
        rw [mul_one, natK_one, one_mul']
        exact le_refl _
    | succ k ih =>
        have esplit : npow (natK 1 / natK 2 : K) (k + 1 + 1)
            = natK 1 / natK 2 * npow (natK 1 / natK 2) (k + 1) :=
          npow_succ _ _
        have hmhalf : natK (k + 1 + 1) * (natK 1 / natK 2 : K)
            = natK (k + 1 + 1) / natK 2 := by
          rw [div_eq, div_eq, natK_one, one_mul']
        have hle : natK (k + 1 + 1) / (natK 2 : K) ≤ natK (k + 1) := by
          rw [div_le_iff natK_two_pos, ← natK_mul (k + 1) 2, natK_le_iff]
          omega
        rw [esplit, ← mul_assoc, hmhalf]
        exact le_trans (mul_le_mul_of_nonneg_right hle
          (npow_nonneg one_half_nonneg (k + 1))) ih
  have hre : m = (m - 1) + 1 := by omega
  rw [hre]
  exact key (m - 1)

/-- The inverse-sum conversion: `a⁻¹ + b⁻¹ ≤ c ↔ b + a ≤ c·(a·b)` for
positive `a`, `b`. -/
theorem inv_add_le_mul_iff {a b c : K} (ha : 0 < a) (hb : 0 < b) :
    a⁻¹ + b⁻¹ ≤ c ↔ b + a ≤ c * (a * b) := by
  constructor
  · intro h
    have hab : 0 < a * b := mul_pos ha hb
    have h1 : (a⁻¹ + b⁻¹) * (a * b) ≤ c * (a * b) :=
      mul_le_mul_of_nonneg_right h (le_of_lt hab)
    have e : (a⁻¹ + b⁻¹) * (a * b) = b + a := by
      rw [right_distrib, ← mul_assoc, mul_inv_cancel' (ne_of_gt ha),
        one_mul', ← mul_assoc, mul_comm b⁻¹ a, mul_assoc,
        mul_inv_cancel' (ne_of_gt hb), mul_one]
    rw [e] at h1
    exact h1
  · intro h
    have hab : 0 < a * b := mul_pos ha hb
    have h1 : (b + a) * (a * b)⁻¹ ≤ c * (a * b) * (a * b)⁻¹ := by
      refine mul_le_mul_of_nonneg_right h ?_
      exact le_of_lt (inv_pos hab)
    have ec : c * (a * b) * (a * b)⁻¹ = c := by
      rw [mul_assoc, mul_inv_cancel_field (ne_of_gt hab), mul_one]
    have e1 : b * (a⁻¹ * b⁻¹) = a⁻¹ := by
      rw [← mul_assoc, mul_comm b a⁻¹, mul_assoc,
        mul_inv_cancel_field (ne_of_gt hb), mul_one]
    have e2 : a * (a⁻¹ * b⁻¹) = b⁻¹ := by
      rw [← mul_assoc, mul_inv_cancel_field (ne_of_gt ha), one_mul']
    have e : (b + a) * (a * b)⁻¹ = a⁻¹ + b⁻¹ := by
      rw [right_distrib, mul_inv_rev, e1, e2]
    rw [e, ec] at h1
    exact h1

theorem one_half_le_one {K : Type} [OrdField K] :
    (natK 1 / natK 2 : K) ≤ (1 : K) := by
  rw [div_le_iff natK_two_pos, one_mul']
  exact natK_le (by omega)

theorem one_half_lt_one {K : Type} [OrdField K] :
    (natK 1 / natK 2 : K) < (1 : K) := by
  rw [div_lt_iff natK_two_pos, one_mul']
  exact natK_lt_iff.mpr (by omega)

/-- The arithmetic core of the `∀m` family: at the endpoint
`s₀ = 2 - δ` (with `2mδ ≤ 1/2`), the `-m` master comparison holds. -/
theorem negm_master_bound (m : Nat) (hm : 1 ≤ m) (δ : K) (hδ : 0 < δ)
    (hδ2 : δ < 1)
    (h2mδ : natK 2 * natK m * δ ≤ natK 1 / natK 2) :
    (npow (1 - δ) m)⁻¹ + (npow (natK 3 - δ) m)⁻¹ ≤ (natK 2 : K) := by
  have h1δ : 0 < 1 - δ := one_sub_pos hδ2
  have h3δ : 0 < natK 3 - δ := by
    have h1 : δ - natK 3 < 0 := sub_lt_zero.mpr
      (lt_of_lt_of_le hδ2
        (le_trans (le_of_eq natK_one.symm) (natK_le (by omega))))
    rw [← neg_sub]
    exact neg_pos' h1
  have hne3 : npow (natK 3 - δ) m ≠ 0 := npow_ne_zero (ne_of_gt h3δ) m
  have hpos1 : 0 < npow (1 - δ) m := npow_pos h1δ m
  have hpos3 : 0 < npow (natK 3 - δ) m := npow_pos h3δ m
  -- the base comparison (1-δ)/(3-δ) ≤ 1/3
  have hδ23 : δ ≤ natK 3 * δ := by
    have e3 : natK 3 * δ = (δ + natK 2 * δ : K) := by
      have e : (natK 3 : K) = natK 1 + natK 2 := by rw [← natK_add]
      rw [e, right_distrib, natK_one, one_mul']
    rw [e3]
    exact le_add_right δ (natK 2 * δ)
      (mul_nonneg (natK_nonneg 2) (le_of_lt hδ))
  have hr : (1 - δ) / (natK 3 - δ) ≤ natK 1 / natK 3 := by
    rw [div_le_div_cross h3δ (natK_pos (n := 3) (by omega))]
    rw [sub_mul, one_mul', natK_one, one_mul', mul_comm δ (natK 3)]
    exact add_le_add_left (neg_le_neg hδ23) (natK 3)
  -- the Bernoulli bound
  have hB : (1 : K) - natK m * δ ≤ npow (1 - δ) m :=
    bernoulli_lower (le_of_lt hδ) (le_of_lt hδ2) m
  -- the divided comparison q ≤ 1/3
  have h13le : natK 1 / natK 3 ≤ (1 : K) := by
    rw [div_le_iff (natK_pos (n := 3) (by omega)), one_mul']
    exact natK_le (by omega)
  have hq : npow ((1 - δ) / (natK 3 - δ)) m ≤ natK 1 / natK 3 := by
    refine le_trans (npow_mono hr
      (div_nonneg (le_of_lt h1δ) h3δ) m) ?_
    have h2 := npow_le_of_le_one (div_nonneg (natK_nonneg 1) (natK_pos (n := 3) (by omega)))
      h13le (by omega)
    exact le_trans h2 (le_of_eq (npow_one _))
  -- the key divided comparison: 1 + q ≤ 2·(1-δ)^m
  have hkey : (1 : K) + npow ((1 - δ) / (natK 3 - δ)) m
      ≤ natK 2 * npow (1 - δ) m := by
    have hL : (1 : K) + npow ((1 - δ) / (natK 3 - δ)) m
        ≤ (1 : K) + natK 1 / natK 3 :=
      add_le_add (le_refl _) hq
    have t0 : natK 1 / natK 3 + natK 1 / natK 2 ≤ (1 : K) := by
      rw [div_add_div (natK_ne_zero (n := 3) (by omega))
        (natK_ne_zero (n := 2) (by omega)), natK_one, one_mul', one_mul',
        ← natK_add, ← natK_mul 3 2,
        div_le_iff (natK_pos (n := 3 * 2) (by omega)), one_mul']
      exact natK_le (by omega)
    have t2 : (1 : K) + natK 1 / natK 3 + natK 1 / natK 2
        ≤ (natK 2 : K) := by
      rw [add_assoc]
      exact le_trans (add_le_add (le_refl _) t0)
        (le_of_eq one_add_one_eq_two)
    have hR3 : (1 : K) + natK 1 / natK 3
        ≤ natK 2 - natK 2 * natK m * δ := by
      refine le_sub_of_add ?_
      have t4 : (1 : K) + natK 1 / natK 3 + natK 2 * natK m * δ
          ≤ (1 : K) + natK 1 / natK 3 + natK 1 / natK 2 :=
        add_le_add (le_refl _) h2mδ
      exact le_trans t4 t2
    have hR2 : natK 2 * ((1 : K) - natK m * δ)
        = natK 2 - natK 2 * natK m * δ := by
      rw [mul_sub, mul_one, mul_assoc]
    have hR1 : natK 2 * ((1 : K) - natK m * δ)
        ≤ natK 2 * npow (1 - δ) m :=
      mul_le_mul_of_nonneg_left hB (natK_nonneg 2)
    refine le_trans hL ?_
    refine le_trans hR3 ?_
    rw [← hR2]
    exact hR1
  -- multiply through by npow (3-δ) m > 0 and convert
  have hmul := mul_le_mul_of_nonneg_right hkey (le_of_lt hpos3)
  have esplit : npow ((1 - δ) / (natK 3 - δ)) m * npow (natK 3 - δ) m
      = npow (1 - δ) m := by
    rw [npow_div (ne_of_gt h3δ) m, div_mul_cancel hne3 (npow (1 - δ) m)]
  have eL : ((1 : K) + npow ((1 - δ) / (natK 3 - δ)) m)
      * npow (natK 3 - δ) m
      = npow (natK 3 - δ) m + npow (1 - δ) m := by
    rw [right_distrib, one_mul', esplit]
  have eR : natK 2 * npow (1 - δ) m * npow (natK 3 - δ) m
      = natK 2 * npow ((1 - δ) * (natK 3 - δ)) m := by
    rw [mul_assoc, ← npow_mul_base]
  rw [eL, eR] at hmul
  refine (inv_add_le_mul_iff hpos1 hpos3).mpr ?_
  rw [← npow_mul_base]
  exact hmul

/-- **Theorem S2(ii), the `∀m` family**: every negative-integer rung
`θ = -m` (elasticity `σ = 1/(m+1)`) false-certifies the whole rational
interval `[2 - 2^-(m+1), 2)` of the diagonal. -/
theorem s2_ii_negm_interval (m : Nat) (hm : 1 ≤ m) (z : WitState K)
    (hz : DiagHyps z)
    (hs : natK 2 - npow (natK 1 / natK 2 : K) (m + 1) ≤ z.s1) :
    DiagAccNeg (fun x => (npow x m)⁻¹) z ∧ ¬ VTyp z := by
  refine ⟨?_, diagHyps_not_vtyp z hz⟩
  refine (master_reduction_neg ?_ z hz).mpr ?_
  · intro a b ha hab
    exact inv_le_inv (npow_pos ha m) (npow_mono hab (le_of_lt ha) m)
  · show (npow (z.s1 - 1) m)⁻¹ + (npow (z.s1 + 1) m)⁻¹ ≤ natK 2
    have hδpos : 0 < npow (natK 1 / natK 2 : K) (m + 1) :=
      npow_pos one_half_pos (m + 1)
    have hδle1 : npow (natK 1 / natK 2 : K) (m + 1) < (1 : K) := by
      have h1 : npow (natK 1 / natK 2 : K) (m + 1)
          ≤ npow (natK 1 / natK 2) 1 :=
        npow_le_of_le_one one_half_nonneg one_half_le_one (by omega)
      rw [npow_one] at h1
      exact lt_of_le_of_lt h1 one_half_lt_one
    -- 2m·(1/2)^(m+1) = m·(1/2)^m ≤ 1/2
    have h2mδ : natK 2 * natK m * npow (natK 1 / natK 2) (m + 1)
        ≤ (natK 1 / natK 2 : K) := by
      have esplit : npow (natK 1 / natK 2 : K) (m + 1)
          = natK 1 / natK 2 * npow (natK 1 / natK 2) m :=
        npow_succ _ _
      rw [esplit,
        mul_assoc (natK 2) (natK m)
          ((natK 1 / natK 2) * npow (natK 1 / natK 2) m),
        ← mul_assoc (natK m) (natK 1 / natK 2)
          (npow (natK 1 / natK 2) m),
        mul_comm (natK m) (natK 1 / natK 2),
        mul_assoc (natK 1 / natK 2) (natK m) (npow (natK 1 / natK 2) m),
        ← mul_assoc (natK 2) (natK 1 / natK 2)
          (natK m * npow (natK 1 / natK 2) m),
        two_mul_one_half, one_mul']
      exact half_pow_scaled m hm
    have hnb := negm_master_bound m hm (npow (natK 1 / natK 2) (m + 1))
      hδpos hδle1 h2mδ
    -- the per-coordinate transfer from the endpoint
    have h1D : 0 < (1 : K) - npow (natK 1 / natK 2 : K) (m + 1) :=
      one_sub_pos hδle1
    have h3D : 0 < natK 3 - npow (natK 1 / natK 2 : K) (m + 1) := by
      have h1 : npow (natK 1 / natK 2 : K) (m + 1) - natK 3 < 0 :=
        sub_lt_zero.mpr
          (lt_of_lt_of_le hδle1
            (le_trans (le_of_eq natK_one.symm) (natK_le (by omega))))
      rw [← neg_sub]
      exact neg_pos' h1
    have hz1 : (1 : K) - npow (natK 1 / natK 2 : K) (m + 1) ≤ z.s1 - 1 := by
      have e21 : natK 2 - 1 = (1 : K) := sub_add_eq one_add_one_eq_two
      have e1 : natK 2 - npow (natK 1 / natK 2 : K) (m + 1) - 1
          = (1 : K) - npow (natK 1 / natK 2) (m + 1) := by
        rw [sub_eq, sub_eq, add_right_comm, ← sub_eq (natK 2) 1, e21,
          ← sub_eq]
      rw [← e1]
      exact sub_le_sub_right hs 1
    have hz2 : natK 3 - npow (natK 1 / natK 2 : K) (m + 1) ≤ z.s1 + 1 := by
      have e23 : (natK 2 : K) + 1 = natK 3 := by
        rw [← natK_one, ← natK_add]
      have e2 : natK 2 - npow (natK 1 / natK 2 : K) (m + 1) + 1
          = natK 3 - npow (natK 1 / natK 2) (m + 1) := by
        rw [sub_eq, add_right_comm, e23, ← sub_eq]
      rw [← e2]
      exact add_le_add_right hs 1
    have c1 : (npow (z.s1 - 1) m)⁻¹
        ≤ (npow ((1 : K) - npow (natK 1 / natK 2 : K) (m + 1)) m)⁻¹ := by
      refine inv_le_inv (npow_pos h1D m) ?_
      exact npow_mono hz1 (le_of_lt h1D) m
    have c2 : (npow (z.s1 + 1) m)⁻¹
        ≤ (npow (natK 3 - npow (natK 1 / natK 2 : K) (m + 1)) m)⁻¹ := by
      refine inv_le_inv (npow_pos h3D m) ?_
      exact npow_mono hz2 (le_of_lt h3D) m
    exact le_trans (add_le_add c1 c2) hnb

/-! ## Theorem S2(ii) — the fractional rungs (σ = 2 and σ = 3)

The θ ∈ (0,1) rungs are covered through algebraic power-law
interfaces: the square law for θ = 1/2 and the cube law `pw x³ = x²`
for θ = 2/3 (sound over ℝ, where the interfaces are instantiated by
the power functions).  The rational bracket certificates are proved
inside the layer — no external verifier needed. -/

/-- Strict square monotonicity: `0 ≤ u < v → u² < v²`. -/
theorem sq_lt_sq {u v : K} (hu : 0 ≤ u) (h : u < v) : u * u < v * v := by
  have hv : 0 < v := lt_of_le_of_lt hu h
  have h1 : u * u ≤ u * v := mul_le_mul_of_nonneg_left (le_of_lt h) hu
  have h2 : u * v < v * v := mul_lt_mul_of_pos_right h hv
  exact lt_of_le_of_lt h1 h2

/-- `npow x 2 = x * x`. -/
theorem npow_two (x : K) : npow x 2 = x * x := by
  show x * (x * 1) = x * x
  rw [mul_one]

/-- `npow x 3 = x * x * x`. -/
theorem npow_three (x : K) : npow x 3 = x * x * x := by
  show x * (x * (x * 1)) = x * x * x
  rw [mul_one, mul_assoc]

/-- Strict cube monotonicity: `0 ≤ u < v → u³ < v³`. -/
theorem cube_lt_cube {u v : K} (hu : 0 ≤ u) (h : u < v) :
    u * u * u < v * v * v := by
  have hv : 0 < v := lt_of_le_of_lt hu h
  by_cases hu0 : u = 0
  · rw [hu0, zero_mul, zero_mul]
    exact mul_pos (mul_pos hv hv) hv
  · have hu' : 0 < u := lt_of_le_of_ne hu (fun he => hu0 he.symm)
    have huu : 0 < u * u := mul_pos hu' hu'
    have h1 : u * (u * u) < v * (u * u) := mul_lt_mul_of_pos_right h huu
    have h2 : v * (u * u) ≤ v * (v * v) :=
      mul_le_mul_of_nonneg_left (le_of_lt (sq_lt_sq hu h)) (le_of_lt hv)
    rw [mul_assoc, mul_assoc]
    exact lt_of_lt_of_le h1 h2

/-- The square-law bracket (lower): `q² ≤ x → q ≤ pw x`. -/
theorem pw_sq_ge (pw : K → K) (hnn : ∀ x, 0 ≤ x → 0 ≤ pw x)
    (hlaw : ∀ x, 0 ≤ x → pw x * pw x = x) {q x : K} (hq : 0 ≤ q)
    (hx : 0 ≤ x) (h : q * q ≤ x) : q ≤ pw x := by
  by_cases hq2 : q ≤ pw x
  · exact hq2
  · have hlt : pw x < q := le_of_not_le hq2
    have h1 : pw x * pw x < q * q := sq_lt_sq (hnn x hx) hlt
    rw [hlaw x hx] at h1
    exact absurd h (not_le_of_lt h1)

/-- The square-law bracket (upper): `x ≤ q² → pw x ≤ q`. -/
theorem pw_sq_le (pw : K → K) (hnn : ∀ x, 0 ≤ x → 0 ≤ pw x)
    (hlaw : ∀ x, 0 ≤ x → pw x * pw x = x) {q x : K} (hq : 0 ≤ q)
    (hx : 0 ≤ x) (h : x ≤ q * q) : pw x ≤ q := by
  by_cases hq2 : pw x ≤ q
  · exact hq2
  · have hlt : q < pw x := le_of_not_le hq2
    have h1 : q * q < pw x * pw x := sq_lt_sq hq hlt
    rw [hlaw x hx] at h1
    exact absurd h (not_le_of_lt h1)

/-- Monotonicity from the square law. -/
theorem pw_sq_mono (pw : K → K) (hnn : ∀ x, 0 ≤ x → 0 ≤ pw x)
    (hlaw : ∀ x, 0 ≤ x → pw x * pw x = x) :
    ∀ a b, 0 ≤ a → a ≤ b → pw a ≤ pw b := by
  intro a b ha hab
  have hb : 0 ≤ b := le_trans ha hab
  by_cases hp : pw b < pw a
  · have h1 : pw b * pw b < pw a * pw a := sq_lt_sq (hnn b hb) hp
    rw [hlaw b hb, hlaw a ha] at h1
    exact absurd hab (not_le_of_lt h1)
  · exact le_of_not_lt hp

/-- Strict monotonicity from the square law. -/
theorem pw_sq_strict_mono (pw : K → K) (hnn : ∀ x, 0 ≤ x → 0 ≤ pw x)
    (hlaw : ∀ x, 0 ≤ x → pw x * pw x = x) :
    ∀ a b, 0 ≤ a → a < b → pw a < pw b := by
  intro a b ha h
  have h1 : pw a ≤ pw b := pw_sq_mono pw hnn hlaw a b ha (le_of_lt h)
  refine lt_of_le_of_ne h1 ?_
  intro he
  have e1 : a = pw a * pw a := (hlaw a ha).symm
  have e2 : b = pw b * pw b := (hlaw b (le_trans ha (le_of_lt h))).symm
  rw [e1, e2, he] at h
  exact lt_irrefl _ h

/-- The cube-law bracket (lower): `q³ ≤ x² → q ≤ pw x`. -/
theorem pw_cube_ge (pw : K → K) (hnn : ∀ x, 0 ≤ x → 0 ≤ pw x)
    (hlaw : ∀ x, 0 ≤ x → pw x * pw x * pw x = x * x) {q x : K}
    (hq : 0 ≤ q) (hx : 0 ≤ x) (h : q * q * q ≤ x * x) : q ≤ pw x := by
  by_cases hq2 : q ≤ pw x
  · exact hq2
  · have hlt : pw x < q := le_of_not_le hq2
    have h1 : pw x * pw x * pw x < q * q * q :=
      cube_lt_cube (hnn x hx) hlt
    rw [hlaw x hx] at h1
    exact absurd h (not_le_of_lt h1)

/-- Monotonicity from the cube law. -/
theorem pw_cube_mono (pw : K → K) (hnn : ∀ x, 0 ≤ x → 0 ≤ pw x)
    (hlaw : ∀ x, 0 ≤ x → pw x * pw x * pw x = x * x) :
    ∀ a b, 0 ≤ a → a ≤ b → pw a ≤ pw b := by
  intro a b ha hab
  have hb : 0 ≤ b := le_trans ha hab
  by_cases hp : pw b < pw a
  · have h1 : pw b * pw b * pw b < pw a * pw a * pw a :=
      cube_lt_cube (hnn b hb) hp
    rw [hlaw b hb, hlaw a ha] at h1
    have h2 : a * a ≤ b * b := by
      have t1 : a * a ≤ b * a := mul_le_mul_of_nonneg_right hab ha
      have t2 : b * a ≤ b * b := mul_le_mul_of_nonneg_left hab hb
      exact le_trans t1 t2
    exact absurd h2 (not_le_of_lt h1)
  · exact le_of_not_lt hp

/-- **Theorem S2(ii), the σ = 2 rung** (θ = 1/2): the master comparison's
exact rational floor is `5/4` — the ladder table's row
(`accept ⟺ s ≥ 5/4`). -/
theorem s2_ii_sigma_two_floor (pw : K → K)
    (hnn : ∀ x, 0 ≤ x → 0 ≤ pw x)
    (hlaw : ∀ x, 0 ≤ x → pw x * pw x = x) (z : WitState K)
    (hz : DiagHyps z) :
    DiagAccMid pw z ↔ natK 5 / natK 4 ≤ z.s1 := by
  have hmono := pw_sq_mono pw hnn hlaw
  have hstrict := pw_sq_strict_mono pw hnn hlaw
  have h1s1 : 0 ≤ z.s1 - 1 := le_of_lt (sub_one_pos hz.2.2.2.1)
  have h1s1' : 0 ≤ z.s1 + 1 :=
    le_trans hz.1.2.1 (le_add_right z.s1 1 zero_le_one')
  have eq14 : (natK 1 / natK 2 : K) * (natK 1 / natK 2)
      = natK 1 * natK 1 / (natK 2 * natK 2) :=
    div_mul_div (natK_ne_zero (n := 2) (by omega))
      (natK_ne_zero (n := 2) (by omega))
  have eq94 : (natK 3 / natK 2 : K) * (natK 3 / natK 2)
      = natK 3 * natK 3 / (natK 2 * natK 2) :=
    div_mul_div (natK_ne_zero (n := 2) (by omega))
      (natK_ne_zero (n := 2) (by omega))
  have hq4 : pw (natK 1 / natK 4 : K) = (natK 1 / natK 2 : K) := by
    have hx4 : 0 ≤ (natK 1 / natK 4 : K) :=
      div_nonneg (natK_nonneg 1) (natK_pos (n := 4) (by omega))
    refine le_antisymm ?_ ?_
    · refine pw_sq_le pw hnn hlaw one_half_nonneg hx4 ?_
      rw [eq14, ← natK_mul 1 1, ← natK_mul 2 2]
      exact le_refl _
    · refine pw_sq_ge pw hnn hlaw one_half_nonneg hx4 ?_
      rw [eq14, ← natK_mul 1 1, ← natK_mul 2 2]
      exact le_refl _
  have hq9 : pw (natK 9 / natK 4 : K) = (natK 3 / natK 2 : K) := by
    have hx9 : 0 ≤ (natK 9 / natK 4 : K) :=
      div_nonneg (natK_nonneg 9) (natK_pos (n := 4) (by omega))
    have hq32 : 0 ≤ (natK 3 / natK 2 : K) :=
      div_nonneg (natK_nonneg 3) (natK_pos (n := 2) (by omega))
    refine le_antisymm ?_ ?_
    · refine pw_sq_le pw hnn hlaw hq32 hx9 ?_
      rw [eq94, ← natK_mul 3 3, ← natK_mul 2 2]
      exact le_refl _
    · refine pw_sq_ge pw hnn hlaw hq32 hx9 ?_
      rw [eq94, ← natK_mul 3 3, ← natK_mul 2 2]
      exact le_refl _
  have e5h : natK 4 + natK 1 = (natK 5 : K) := by rw [← natK_add]
  have e5 : natK 5 / natK 4 - 1 = (natK 1 / natK 4 : K) := by
    rw [← div_self (natK_ne_zero (n := 4) (by omega)), ← sub_div,
      sub_add_eq e5h]
  have e9 : natK 5 / natK 4 + 1 = (natK 9 / natK 4 : K) := by
    rw [← div_self (natK_ne_zero (n := 4) (by omega)),
      div_add_div_same (natK_ne_zero (n := 4) (by omega)), ← natK_add]
  constructor
  · intro hd
    have hmaster : (natK 2 : K) ≤ pw (z.s1 - 1) + pw (z.s1 + 1) :=
      (master_reduction_pos hmono z hz).mp ((diagAccMid_iff_pos z hz).mp hd)
    cases le_total (natK 5 / natK 4) z.s1 with
    | inl hge => exact hge
    | inr hlt =>
        by_cases he : z.s1 = natK 5 / natK 4
        · exact le_of_eq he.symm
        · have hlt' : z.s1 < natK 5 / natK 4 := lt_of_le_of_ne hlt he
          have hs1 : z.s1 - 1 < natK 1 / natK 4 := by
            rw [← e5]
            exact sub_lt_sub_right hlt' 1
          have hs2 : z.s1 + 1 < natK 9 / natK 4 := by
            rw [← e9]
            exact add_lt_add_right' hlt' 1
          have b1 : pw (z.s1 - 1) < natK 1 / natK 2 := by
            have ht := hstrict (z.s1 - 1) (natK 1 / natK 4) h1s1 hs1
            rw [hq4] at ht
            exact ht
          have b2 : pw (z.s1 + 1) < natK 3 / natK 2 := by
            have ht := hstrict (z.s1 + 1) (natK 9 / natK 4) h1s1' hs2
            rw [hq9] at ht
            exact ht
          have e42 : (natK 4 : K) / natK 2 = natK 2 := by
            refine mul_right_cancel' (natK_ne_zero (n := 2) (by omega)) ?_
            rw [div_mul_cancel (natK_ne_zero (n := 2) (by omega)) (natK 4),
              ← natK_mul]
          have e2 : natK 1 / natK 2 + natK 3 / natK 2 = (natK 2 : K) := by
            rw [div_add_div_same (natK_ne_zero (n := 2) (by omega)),
              ← natK_add]
            exact e42
          have hsum : pw (z.s1 - 1) + pw (z.s1 + 1)
              < natK 1 / natK 2 + natK 3 / natK 2 :=
            lt_trans (add_lt_add_left' b2 (pw (z.s1 - 1)))
              (add_lt_add_right' b1 (natK 3 / natK 2))
          rw [e2] at hsum
          exact absurd hmaster (not_le_of_lt hsum)
  · intro hs
    have b1 : (natK 1 / natK 2 : K) ≤ pw (z.s1 - 1) := by
      refine pw_sq_ge pw hnn hlaw one_half_nonneg h1s1 ?_
      have h1 : natK 1 / natK 4 ≤ z.s1 - 1 := by
        have ht := sub_le_sub_right hs 1
        rw [e5] at ht
        exact ht
      rw [eq14, ← natK_mul 1 1, ← natK_mul 2 2]
      exact h1
    have b2 : (natK 3 / natK 2 : K) ≤ pw (z.s1 + 1) := by
      refine pw_sq_ge pw hnn hlaw
        (div_nonneg (natK_nonneg 3) (natK_pos (n := 2) (by omega))) h1s1' ?_
      have h1 : natK 9 / natK 4 ≤ z.s1 + 1 := by
        have ht := add_le_add_right hs 1
        rw [e9] at ht
        exact ht
      rw [eq94, ← natK_mul 3 3, ← natK_mul 2 2]
      exact h1
    have e42 : (natK 4 : K) / natK 2 = natK 2 := by
      refine mul_right_cancel' (natK_ne_zero (n := 2) (by omega)) ?_
      rw [div_mul_cancel (natK_ne_zero (n := 2) (by omega)) (natK 4),
        ← natK_mul]
    have e2 : natK 1 / natK 2 + natK 3 / natK 2 = (natK 2 : K) := by
      rw [div_add_div_same (natK_ne_zero (n := 2) (by omega)), ← natK_add]
      exact e42
    exact (diagAccMid_iff_pos z hz).mpr
      ((master_reduction_pos hmono z hz).mpr
        (le_trans (le_of_eq e2.symm) (add_le_add b1 b2)))

/-- **Theorem S2(ii), the σ = 2 witness**: the paper's witness `13/10`
sits above the exact floor `5/4`. -/
theorem s2_ii_sigma_two_witness (pw : K → K)
    (hnn : ∀ x, 0 ≤ x → 0 ≤ pw x)
    (hlaw : ∀ x, 0 ≤ x → pw x * pw x = x) (z : WitState K)
    (hz : DiagHyps z) (hs : natK 5 / natK 4 ≤ z.s1) :
    DiagAccMid pw z ∧ ¬ VTyp z :=
  ⟨(s2_ii_sigma_two_floor pw hnn hlaw z hz).mpr hs, diagHyps_not_vtyp z hz⟩

/-- **Theorem S2(ii), the σ = 3 rung** (θ = 2/3): the paper's canonical
datum `s = 6/5` — the rational brackets `(1/3, 5/3)` are proved inside
the layer (`(1/3)³ ≤ (1/5)²`, `(5/3)³ ≤ (11/5)²`, sum exactly `2`). -/
theorem s2_ii_sigma_three_witness (pw : K → K)
    (hnn : ∀ x, 0 ≤ x → 0 ≤ pw x)
    (hlaw : ∀ x, 0 ≤ x → pw x * pw x * pw x = x * x) (z : WitState K)
    (hz : DiagHyps z) (hs : natK 6 / natK 5 ≤ z.s1) :
    DiagAccMid pw z ∧ ¬ VTyp z := by
  have hmono := pw_cube_mono pw hnn hlaw
  have h1s1 : 0 ≤ z.s1 - 1 := le_of_lt (sub_one_pos hz.2.2.2.1)
  have h1s1' : 0 ≤ z.s1 + 1 :=
    le_trans hz.1.2.1 (le_add_right z.s1 1 zero_le_one')
  have e1 : npow (natK 1 / natK 3 : K) 3 = (natK 1 / natK 27 : K) := by
    rw [npow_div (natK_ne_zero (n := 3) (by omega)) 3, npow_natK 1 3,
      npow_natK 3 3]
  have e2 : npow (natK 5 / natK 3 : K) 3 = (natK 125 / natK 27 : K) := by
    rw [npow_div (natK_ne_zero (n := 3) (by omega)) 3, npow_natK 5 3,
      npow_natK 3 3]
  have e3 : npow (natK 1 / natK 5 : K) 2 = (natK 1 / natK 25 : K) := by
    rw [npow_div (natK_ne_zero (n := 5) (by omega)) 2, npow_natK 1 2,
      npow_natK 5 2]
  have e4 : npow (natK 11 / natK 5 : K) 2 = (natK 121 / natK 25 : K) := by
    rw [npow_div (natK_ne_zero (n := 5) (by omega)) 2, npow_natK 11 2,
      npow_natK 5 2]
  have br1 : npow (natK 1 / natK 3 : K) 3 ≤ npow (natK 1 / natK 5 : K) 2 := by
    rw [e1, e3,
      div_le_div_cross (natK_pos (n := 27) (by omega))
        (natK_pos (n := 25) (by omega))]
    rw [← natK_mul 1 25, ← natK_mul 1 27]
    exact natK_le (by omega)
  have br2 : npow (natK 5 / natK 3 : K) 3 ≤ npow (natK 11 / natK 5 : K) 2 := by
    rw [e2, e4,
      div_le_div_cross (natK_pos (n := 27) (by omega))
        (natK_pos (n := 25) (by omega))]
    rw [← natK_mul 125 25, ← natK_mul 121 27]
    exact natK_le (by omega)
  refine ⟨?_, diagHyps_not_vtyp z hz⟩
  refine (diagAccMid_iff_pos z hz).mpr ((master_reduction_pos hmono z hz).mpr ?_)
  have hx1 : (natK 1 / natK 5 : K) ≤ z.s1 - 1 := by
    have e61h : natK 5 + natK 1 = (natK 6 : K) := by rw [← natK_add]
    have e61 : natK 6 / natK 5 - 1 = (natK 1 / natK 5 : K) := by
      rw [← div_self (natK_ne_zero (n := 5) (by omega)), ← sub_div,
        sub_add_eq e61h]
    rw [← e61]
    exact sub_le_sub_right hs 1
  have hx2 : (natK 11 / natK 5 : K) ≤ z.s1 + 1 := by
    have e115 : natK 6 / natK 5 + 1 = (natK 11 / natK 5 : K) := by
      rw [← div_self (natK_ne_zero (n := 5) (by omega)),
        div_add_div_same (natK_ne_zero (n := 5) (by omega)), ← natK_add]
    rw [← e115]
    exact add_le_add_right hs 1
  have b1 : (natK 1 / natK 3 : K) ≤ pw (z.s1 - 1) := by
    refine pw_cube_ge pw hnn hlaw
      (div_nonneg (natK_nonneg 1) (natK_pos (n := 3) (by omega))) h1s1 ?_
    rw [← npow_three, ← npow_two]
    exact le_trans br1
      (npow_mono hx1
        (div_nonneg (natK_nonneg 1) (natK_pos (n := 5) (by omega))) 2)
  have b2 : (natK 5 / natK 3 : K) ≤ pw (z.s1 + 1) := by
    refine pw_cube_ge pw hnn hlaw
      (div_nonneg (natK_nonneg 5) (natK_pos (n := 3) (by omega))) h1s1' ?_
    rw [← npow_three, ← npow_two]
    exact le_trans br2
      (npow_mono hx2
        (div_nonneg (natK_nonneg 11) (natK_pos (n := 5) (by omega))) 2)
  have esum : (natK 1 / natK 3 : K) + natK 5 / natK 3 = (natK 2 : K) := by
    rw [div_add_div_same (natK_ne_zero (n := 3) (by omega)), ← natK_add]
    refine mul_right_cancel' (natK_ne_zero (n := 3) (by omega)) ?_
    rw [div_mul_cancel (natK_ne_zero (n := 3) (by omega)) (natK 6), ← natK_mul]
  exact le_trans (le_of_eq esum.symm) (add_le_add b1 b2)

/-- The canonical datum's critical-elasticity bracket: at `s = 6/5` the
σ = 2 rung rejects (the exact floor `5/4` exceeds it) while the σ = 3
rung accepts — the interface-level form of the paper's
`σ* ∈ (2, 3)` at the Section 6.3 datum. -/
theorem s2_ii_canonical_bracket (pw2 pw3 : K → K)
    (hnn2 : ∀ x, 0 ≤ x → 0 ≤ pw2 x) (hlaw2 : ∀ x, 0 ≤ x → pw2 x * pw2 x = x)
    (hnn3 : ∀ x, 0 ≤ x → 0 ≤ pw3 x)
    (hlaw3 : ∀ x, 0 ≤ x → pw3 x * pw3 x * pw3 x = x * x)
    (z : WitState K) (hz : DiagHyps z) (hs : z.s1 = natK 6 / natK 5) :
    ¬ DiagAccMid pw2 z ∧ DiagAccMid pw3 z := by
  refine ⟨?_, ?_⟩
  · intro hd
    have hfloor := (s2_ii_sigma_two_floor pw2 hnn2 hlaw2 z hz).mp hd
    rw [hs] at hfloor
    rw [div_le_div_cross (natK_pos (n := 4) (by omega))
      (natK_pos (n := 5) (by omega))] at hfloor
    rw [← natK_mul 5 5, ← natK_mul 6 4] at hfloor
    exact absurd (natK_le_iff.mp hfloor) (by omega)
  · exact (s2_ii_sigma_three_witness pw3 hnn3 hlaw3 z hz
      (le_of_eq hs.symm)).1

/-! ## Theorem S2(ii) — the geometric member (σ = 1, the LPI form)

The θ = 0 member is covered through the geometric-mean interface
`GeoLaws` — the four algebraic laws of the weighted geometric mean
(positivity, per-coordinate monotonicity, the swap-product identity
`gp(x,y,w)·gp(y,x,w) = xy`, and equal-weight symmetry), all sound over
ℝ.  The swap-product identity replaces the paper's log-space
averaging: the master comparison collapses to `s² ≥ 2`. -/

/-- The geometric-mean interface laws. -/
def GeoLaws (gp : K → K → K → K → K) : Prop :=
  (∀ x y w1 w2, 0 < x → 0 < y → 0 < gp x y w1 w2) ∧
  (∀ x x' y w1 w2, 0 ≤ x → x ≤ x' → 0 ≤ w1 →
      gp x y w1 w2 ≤ gp x' y w1 w2) ∧
  (∀ y y' x w1 w2, 0 ≤ y → y ≤ y' → 0 ≤ w2 →
      gp x y w1 w2 ≤ gp x y' w1 w2) ∧
  (∀ x y w1 w2, 0 < x → 0 < y → w1 + w2 = 1 →
      gp x y w1 w2 * gp y x w1 w2 = x * y) ∧
  (∀ x y, gp x y (natK 1 / natK 2) (natK 1 / natK 2)
      = gp y x (natK 1 / natK 2) (natK 1 / natK 2))

/-- Protocol 2 under the geometric member (θ = 0 < 1 carries the
collapse convention). -/
def GeoAdm (gp : K → K → K → K → K) (w1 w2 : K) (a : WitAct K)
    (z : WitState K) : Prop :=
  CollapseSafe a z ∧
  (∀ p, witTube a z p →
      (0 ≤ p.x ∧ 1 ≤ gp (1 + p.s1) (1 + p.s2) w1 w2)) ∧
  ((witSucc a z).1 = true ∧ 0 ≤ (witSucc a z).2.x ∧
      1 ≤ gp (1 + (witSucc a z).2.s1) (1 + (witSucc a z).2.s2) w1 w2)

/-- The geometric protocol on the deterministic menu. -/
def DiagAccGeo (gp : K → K → K → K → K) (z : WitState K) : Prop :=
  ∀ w1 w2, WNorm w1 w2 → ∃ a : DetAct, GeoAdm gp w1 w2 (.det a) z

/-- Strict subtraction compatibility on the left. -/
theorem sub_lt_sub_left' {a b c : K} (h : a < b) : c - b < c - a :=
  add_lt_add_left' (neg_lt_neg' h) c

/-- The degenerate value `gp c c w1 w2 = c` (derived from the swap law
and positivity). -/
theorem gp_diag (gp : K → K → K → K → K) (hl : GeoLaws gp) {c : K}
    (hc : 0 < c) {w1 w2 : K} (hw : w1 + w2 = 1) : gp c c w1 w2 = c := by
  have gpos : 0 < gp c c w1 w2 := hl.1 c c w1 w2 hc hc
  have h1 : gp c c w1 w2 * gp c c w1 w2 = c * c :=
    hl.2.2.2.1 c c w1 w2 hc hc hw
  by_cases hg : gp c c w1 w2 = c
  · exact hg
  · cases le_total (gp c c w1 w2) c with
    | inl hle =>
        have hlt : gp c c w1 w2 < c := lt_of_le_of_ne hle hg
        have h2 : gp c c w1 w2 * gp c c w1 w2 < c * c :=
          sq_lt_sq (le_of_lt gpos) hlt
        rw [← h1] at h2
        exact absurd h2 (lt_irrefl (gp c c w1 w2 * gp c c w1 w2))
    | inr hle =>
        have hlt : c < gp c c w1 w2 :=
          lt_of_le_of_ne hle (fun he => hg he.symm)
        have h2 : c * c < gp c c w1 w2 * gp c c w1 w2 :=
          sq_lt_sq (le_of_lt hc) hlt
        rw [h1] at h2
        exact absurd h2 (lt_irrefl (c * c))

/-- **The master-equation reduction, geometric member** (θ = 0, σ = 1 —
the LPI functional form): on the diagonal, the geometric protocol
accepts exactly when `s² ≥ 2` — the swap-product identity `F·S = s² - 1`
replaces the paper's log-space averaging. -/
theorem master_reduction_geo (gp : K → K → K → K → K) (hl : GeoLaws gp)
    (z : WitState K) (hz : DiagHyps z) :
    DiagAccGeo gp z ↔ natK 2 ≤ z.s1 * z.s1 := by
  have h1s1 : 0 < z.s1 - 1 := sub_one_pos hz.2.2.2.1
  have h1s1' : 0 < z.s1 + 1 := zero_lt_add_one hz.1.2.1
  have eR : (z.s1 - 1) * (z.s1 + 1) = z.s1 * z.s1 - 1 := by
    rw [sub_mul, left_distrib, mul_one, one_mul', add_comm z.s1 1]
    exact add_sub_add_comm (z.s1 * z.s1) z.s1 1
  have hsym : gp (z.s1 - 1) (z.s1 + 1) (natK 1 / natK 2)
      (natK 1 / natK 2)
      = gp (z.s1 + 1) (z.s1 - 1) (natK 1 / natK 2) (natK 1 / natK 2) :=
    hl.2.2.2.2 _ _
  have hGS : gp (z.s1 - 1) (z.s1 + 1) (natK 1 / natK 2)
      (natK 1 / natK 2)
      * gp (z.s1 + 1) (z.s1 - 1) (natK 1 / natK 2) (natK 1 / natK 2)
      = (z.s1 - 1) * (z.s1 + 1) :=
    hl.2.2.2.1 _ _ _ _ h1s1 h1s1' one_half_add_one_half
  rw [← hsym] at hGS
  -- hGS : G * G = (s-1)(s+1) = s² - 1
  have hcore : (1 : K) ≤ gp (z.s1 - 1) (z.s1 + 1)
      (natK 1 / natK 2) (natK 1 / natK 2) →
      natK 2 ≤ z.s1 * z.s1 := by
    intro hGge
    have hGpos : 0 < gp (z.s1 - 1) (z.s1 + 1)
        (natK 1 / natK 2) (natK 1 / natK 2) :=
      hl.1 _ _ _ _ h1s1 h1s1'
    have hGG : (1 : K) * 1
        ≤ gp (z.s1 - 1) (z.s1 + 1) (natK 1 / natK 2) (natK 1 / natK 2)
          * gp (z.s1 - 1) (z.s1 + 1) (natK 1 / natK 2) (natK 1 / natK 2) :=
      le_trans (mul_le_mul_of_nonneg_right hGge zero_le_one')
        (mul_le_mul_of_nonneg_left hGge (le_of_lt hGpos))
    rw [one_mul'] at hGG
    rw [hGS, eR] at hGG
    have h5 : (1 : K) + 1 ≤ (z.s1 * z.s1 - 1) + 1 :=
      add_le_add hGG (le_refl 1)
    rw [one_add_one_eq_two, sub_add_cancel] at h5
    exact h5
  constructor
  · intro hd
    have hpair := hd (natK 1 / natK 2) (natK 1 / natK 2) wNorm_one_half
    cases hpair with
    | intro a ha =>
        cases a with
        | noswitch => exact Bool.noConfusion ha.2.2.1
        | staged =>
            have hbot : witTube (.det .staged) z ⟨z.x - 1, z.s1, z.s2⟩ :=
              ⟨le_refl _, sub_le_self z.x 1 zero_le_one', le_refl _,
                le_add_right z.s1 eGain eGain_nonneg, le_refl _,
                le_add_right z.s2 eGain eGain_nonneg⟩
            have h1 := ha.2.1 _ hbot
            have h2 : z.x - 1 < 0 := sub_lt_zero.mpr hz.2.1
            exact absurd h1.1 (not_le_of_lt h2)
        | fast =>
            have hdip : witTube (.det .fast) z ⟨z.x, z.s1 - natK 2, z.s2⟩ :=
              ⟨rfl, rfl, le_refl _, sub_le_self z.s1 (natK 2) (natK_nonneg 2)⟩
            have h1 := ha.2.1 _ hdip
            rw [one_add_sub_two, one_add_s2 z hz] at h1
            exact hcore h1.2
        | slow =>
            have hdip : witTube (.det .slow) z ⟨z.x, z.s1, z.s2 - natK 2⟩ :=
              ⟨rfl, rfl, le_refl _, sub_le_self z.s2 (natK 2) (natK_nonneg 2)⟩
            have h1 := ha.2.1 _ hdip
            rw [← hz.2.2.1, one_add_sub_two, add_comm 1 z.s1] at h1
            rw [← hsym] at h1
            exact hcore h1.2
  · intro hmaster w1 w2 hw
    have hF : gp (z.s1 - 1) (z.s1 + 1) w1 w2
        * gp (z.s1 + 1) (z.s1 - 1) w1 w2 = z.s1 * z.s1 - 1 := by
      rw [hl.2.2.2.1 _ _ _ _ h1s1 h1s1' hw.2.2, eR]
    have hpos1 : 0 < gp (z.s1 - 1) (z.s1 + 1) w1 w2 :=
      hl.1 _ _ _ _ h1s1 h1s1'
    have hpos2 : 0 < gp (z.s1 + 1) (z.s1 - 1) w1 w2 :=
      hl.1 _ _ _ _ h1s1' h1s1
    have hFSge : (1 : K) ≤ gp (z.s1 - 1) (z.s1 + 1) w1 w2
        * gp (z.s1 + 1) (z.s1 - 1) w1 w2 := by
      rw [hF]
      exact le_sub_of_add (by rw [one_add_one_eq_two]; exact hmaster)
    cases le_total (1 : K) (gp (z.s1 - 1) (z.s1 + 1) w1 w2) with
    | inl hF1 =>
        refine ⟨.fast, ⟨collapse_safe_all_det z hz .fast, ?_,
          ⟨rfl, hz.1.1, ?_⟩⟩⟩
        · intro p hp
          refine ⟨by rw [hp.1]; exact hz.1.1, ?_⟩
          have hb : gp (z.s1 - 1) (1 + p.s2) w1 w2
              ≤ gp (1 + p.s1) (1 + p.s2) w1 w2 := by
            refine hl.2.1 _ _ _ _ _ (le_of_lt h1s1) ?_ hw.1
            rw [← one_add_sub_two]
            exact add_le_add_left hp.2.2.1 1
          have hF' : gp (z.s1 - 1) (1 + p.s2) w1 w2
              = gp (z.s1 - 1) (z.s1 + 1) w1 w2 := by
            rw [hp.2.1, one_add_s2 z hz]
          exact le_trans hF1 (le_trans (le_of_eq hF'.symm) hb)
        · show (1 : K) ≤ gp (1 + (z.s1 + eGain))
              (1 + (z.s2 + eGain)) w1 w2
          rw [← hz.2.2.1]
          have hc : 0 < 1 + (z.s1 + eGain) :=
            zero_lt_one_add (add_le_add_of_nonneg hz.1.2.1 eGain_nonneg)
          rw [gp_diag gp hl hc hw.2.2]
          exact (one_le_add_one_iff _).mpr
            (add_le_add_of_nonneg hz.1.2.1 eGain_nonneg)
    | inr hFle =>
        have hS : (1 : K) ≤ gp (z.s1 + 1) (z.s1 - 1) w1 w2 := by
          have h3 : gp (z.s1 - 1) (z.s1 + 1) w1 w2
              * gp (z.s1 + 1) (z.s1 - 1) w1 w2
              ≤ (1 : K) * gp (z.s1 + 1) (z.s1 - 1) w1 w2 :=
            mul_le_mul_of_nonneg_right hFle (le_of_lt hpos2)
          rw [one_mul'] at h3
          exact le_trans hFSge h3
        refine ⟨.slow, ⟨collapse_safe_all_det z hz .slow, ?_,
          ⟨rfl, hz.1.1, ?_⟩⟩⟩
        · intro p hp
          refine ⟨by rw [hp.1]; exact hz.1.1, ?_⟩
          have hb : gp (1 + p.s1) (z.s1 - 1) w1 w2
              ≤ gp (1 + p.s1) (1 + p.s2) w1 w2 := by
            refine hl.2.2.1 _ _ _ _ _ (le_of_lt h1s1) ?_ hw.2.1
            rw [← one_add_sub_two, hz.2.2.1]
            exact add_le_add_left hp.2.2.1 1
          have hS' : gp (1 + p.s1) (z.s1 - 1) w1 w2
              = gp (z.s1 + 1) (z.s1 - 1) w1 w2 := by
            rw [hp.2.1, add_comm 1 z.s1]
          exact le_trans hS (le_trans (le_of_eq hS'.symm) hb)
        · show (1 : K) ≤ gp (1 + (z.s1 + eGain))
              (1 + (z.s2 + eGain)) w1 w2
          rw [← hz.2.2.1]
          have hc : 0 < 1 + (z.s1 + eGain) :=
            zero_lt_one_add (add_le_add_of_nonneg hz.1.2.1 eGain_nonneg)
          rw [gp_diag gp hl hc hw.2.2]
          exact (one_le_add_one_iff _).mpr
            (add_le_add_of_nonneg hz.1.2.1 eGain_nonneg)

theorem s2_ii_sigma_one_witness (gp : K → K → K → K → K)
    (hl : GeoLaws gp) (z : WitState K) (hz : DiagHyps z)
    (hs : (natK 3 / natK 2 : K) ≤ z.s1) :
    DiagAccGeo gp z ∧ ¬ VTyp z := by
  refine ⟨?_, diagHyps_not_vtyp z hz⟩
  refine (master_reduction_geo gp hl z hz).mpr ?_
  have h1 : (natK 3 / natK 2 : K) * (natK 3 / natK 2) ≤ z.s1 * z.s1 := by
    have t1 : natK 3 / natK 2 * (natK 3 / natK 2)
        ≤ natK 3 / natK 2 * z.s1 :=
      mul_le_mul_of_nonneg_left hs
        (div_nonneg (natK_nonneg 3) (natK_pos (n := 2) (by omega)))
    have t2 : natK 3 / natK 2 * z.s1 ≤ z.s1 * z.s1 :=
      mul_le_mul_of_nonneg_right hs hz.1.2.1
    exact le_trans t1 t2
  have e33 : natK 3 * natK 3 = (natK 9 : K) := by rw [← natK_mul]
  have e22 : natK 2 * natK 2 = (natK 4 : K) := by rw [← natK_mul]
  have h2 : (natK 9 / natK 4 : K) ≤ natK 3 / natK 2 * (natK 3 / natK 2) := by
    rw [← e33, ← e22,
      div_mul_div (natK_ne_zero (n := 2) (by omega))
        (natK_ne_zero (n := 2) (by omega))]
    exact le_refl _
  have h3 : (natK 2 : K) ≤ natK 9 / natK 4 := by
    rw [le_div_iff (natK_pos (n := 4) (by omega))]
    rw [← natK_mul 2 4]
    exact natK_le (by omega)
  exact le_trans h3 (le_trans h2 h1)

/-- **Theorem S2(ii), the √2 floor's rational bracket**: the geometric
rung rejects `s = 141/100` (the floor `√2` exceeds it). -/
theorem s2_ii_sigma_one_reject (gp : K → K → K → K → K)
    (hl : GeoLaws gp) (z : WitState K) (hz : DiagHyps z)
    (hs : z.s1 = natK 141 / natK 100) : ¬ DiagAccGeo gp z := by
  intro hd
  have h := (master_reduction_geo gp hl z hz).mp hd
  rw [hs] at h
  have h100 : (natK 100 : K) ≠ 0 := natK_ne_zero (n := 100) (by omega)
  have e : (natK 141 / natK 100 : K) * (natK 141 / natK 100)
      = natK 141 * natK 141 / (natK 100 * natK 100) :=
    div_mul_div h100 h100
  rw [e, ← natK_mul 141 141, ← natK_mul 100 100] at h
  rw [le_div_iff (natK_pos (n := 100 * 100) (by omega)),
    ← natK_mul 2 (100 * 100)] at h
  exact absurd (natK_le_iff.mp h) (by omega)

/-! ## Lemma B(ii) — the linear exception's rational witness -/

/-- **Lemma B(ii)**: only the perfectly-substitutable dashboard
certifies through a collapsed coordinate.  At the state
`z₀ = (1/2, 1/2, 5/2)`, the plan FAST's tube dips `λ₁ = 1 + s₁` to
`-1/2 ≤ 0` (a collapsed coordinate), yet the θ = 1 member certifies the
plan at the equal weight; every θ < 1 member rejects it (the collapse
convention — `CollapseSafe` fails). -/
theorem lemB_ii_linear_witness (K : Type) [OrdField K] :
    (1 + (natK 1 / natK 2 - natK 2 : K) ≤ 0) ∧
    Theta1Adm (natK 1 / natK 2 : K) (natK 1 / natK 2) (.det .fast)
      ⟨natK 1 / natK 2, natK 1 / natK 2, natK 5 / natK 2⟩ ∧
    ¬ CollapseSafe (.det .fast)
      ⟨(natK 1 / natK 2 : K), natK 1 / natK 2, natK 5 / natK 2⟩ := by
  have hneq : 1 + (natK 1 / natK 2 - natK 2 : K) ≤ 0 := by
    rw [one_add_sub_two, ← neg_sub]
    have h2 : (0 : K) ≤ 1 - natK 1 / natK 2 :=
      sub_nonneg.mpr one_half_le_one
    have h3 := neg_le_neg h2
    rw [neg_zero] at h3
    exact h3
  refine ⟨hneq, ?_, ?_⟩
  · rw [lemA_engine one_half_add_one_half,
      wAdm_fast_iff ⟨one_half_nonneg, one_half_nonneg,
        Or.inl (ne_of_gt one_half_pos)⟩]
    refine ⟨one_half_nonneg, ?_⟩
    rw [← left_distrib]
    have e : (natK 1 / natK 2 - natK 2) + natK 5 / natK 2 = (1 : K) := by
      rw [add_sub_comm, div_add_div_same (natK_ne_zero (n := 2) (by omega)),
        ← natK_add]
      have e62 : (natK 6 : K) / natK 2 = natK 3 := by
        refine mul_right_cancel' (natK_ne_zero (n := 2) (by omega)) ?_
        rw [div_mul_cancel (natK_ne_zero (n := 2) (by omega)) (natK 6),
          ← natK_mul]
      have h32 : natK 2 + natK 1 = (natK 3 : K) := by rw [← natK_add]
      rw [e62, sub_add_eq h32, natK_one]
    rw [e, mul_one]
    exact one_half_nonneg
  · intro hcs
    have hdip : witTube (.det .fast)
        ⟨(natK 1 / natK 2 : K), natK 1 / natK 2, natK 5 / natK 2⟩
        ⟨natK 1 / natK 2, natK 1 / natK 2 - natK 2, natK 5 / natK 2⟩ :=
      ⟨rfl, rfl, le_refl _, sub_le_self _ (natK 2) (natK_nonneg 2)⟩
    have h1 := hcs _ hdip
    exact lt_irrefl (0 : K) (lt_of_lt_of_le h1.1 hneq)

/-- Every θ < 1 member rejects the collapsed plan of Lemma B(ii) (both
the θ ∈ (0,1) and the θ < 0 conventions carry `CollapseSafe`). -/
theorem lemB_ii_only_linear (pw : K → K) (w1 w2 : K) (a : WitAct K)
    (z : WitState K) (h : ThetaSubAdm pw w1 w2 a z ∨ ThetaMidAdm pw w1 w2 a z)
    (hcs : ¬ CollapseSafe a z) : False := by
  cases h with
  | inl hsub => exact hcs hsub.1
  | inr hmid => exact hcs hmid.1

/-- **The two-sided Leontief statement** (the covered family): (i) the
θ = 1 rung accepts every gap state — full Leontief is never necessary
at a fixed state; (ii) every negative-integer rung `σ = 1/(m+1)`
false-certifies a nonempty rational interval of diagonal gap states;
and the Leontief member itself accepts no gap state — the only
uniformly safe aggregator of the covered family. -/
theorem s2_two_sided_summary (K : Type) [OrdField K] :
    (∀ z' : WitState K, InX0 z' → IsGap z' → ∀ w1 w2, WNorm w1 w2 →
        ∃ a : DetAct, Theta1Adm w1 w2 (.det a) z') ∧
    (∀ m : Nat, 1 ≤ m → ∃ z' : WitState K, DiagHyps z' ∧
        DiagAccNeg (fun x => (npow x m)⁻¹) z' ∧ ¬ VTyp z') ∧
    (∀ z' : WitState K, InX0 z' → IsGap z' →
        ¬ ∀ w1 w2 : K, WNorm w1 w2 → ∃ a : DetAct, TypedAdm (.det a) z') := by
  refine ⟨fun _ hz hg => s2_i_linear_accepts _ hz hg, ?_,
    fun _ hz hg => s2_leontief_rejects_gaps _ hz hg⟩
  intro m hm
  have hδpos : 0 < npow (natK 1 / natK 2 : K) (m + 1) :=
    npow_pos one_half_pos (m + 1)
  have hδle1 : npow (natK 1 / natK 2 : K) (m + 1) < (1 : K) := by
    have h1 : npow (natK 1 / natK 2 : K) (m + 1)
        ≤ npow (natK 1 / natK 2) 1 :=
      npow_le_of_le_one one_half_nonneg one_half_le_one (by omega)
    rw [npow_one] at h1
    exact lt_of_le_of_lt h1 one_half_lt_one
  have hδ2 : npow (natK 1 / natK 2 : K) (m + 1) ≤ natK 2 :=
    le_trans (le_of_lt hδle1)
      (le_trans (le_of_eq natK_one.symm) (natK_le (by omega)))
  have hdiag : DiagHyps ⟨natK 1 / natK 2,
      natK 2 - npow (natK 1 / natK 2 : K) (m + 1),
      natK 2 - npow (natK 1 / natK 2 : K) (m + 1)⟩ := by
    refine ⟨⟨one_half_nonneg, sub_nonneg.mpr hδ2, sub_nonneg.mpr hδ2⟩,
      one_half_lt_one, rfl, ?_, ?_⟩
    · have e21 : natK 2 - 1 = (1 : K) := sub_add_eq one_add_one_eq_two
      rw [← e21]
      exact sub_lt_sub_left' hδle1
    · have hlt : natK 2 - npow (natK 1 / natK 2 : K) (m + 1)
          < natK 2 - (0 : K) := sub_lt_sub_left' hδpos
      rw [sub_zero] at hlt
      exact hlt
  exact ⟨⟨natK 1 / natK 2,
    natK 2 - npow (natK 1 / natK 2 : K) (m + 1),
    natK 2 - npow (natK 1 / natK 2 : K) (m + 1)⟩, hdiag,
    (s2_ii_negm_interval m hm _ hdiag (le_refl _)).1,
    (s2_ii_negm_interval m hm _ hdiag (le_refl _)).2⟩

end P1Sep
