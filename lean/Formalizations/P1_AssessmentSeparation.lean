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
      binding one).  The negative-integer rungs `θ = -m` (elasticities
      `σ = 1/(m+1)`) instantiate the interface in pure ordered-field
      arithmetic — no bridges — and yield: the golden-ratio closed form
      at `m = 1` (Fibonacci witnesses 8/5 rejects / 13/8 accepts), the
      paper's `σ = 1/4` witness (θ = -3 accepts 9/5), the `∀m`
      false-certification family (every `σ = 1/(m+1)` false-certifies an
      exact rational interval of gap states — via a Bernoulli-type
      product bound proved here), and the Leontief identification
      `V⁰ = V_typ` (the only uniformly safe aggregator of the covered
      family).  The fractional rungs (σ = 3 at 6/5, σ = 2 at 13/10) are
      covered by certificate-conditional theorems: given rational lower
      bounds on the power values (checked over ℝ by the deposited
      verifier), the rung false-certifies the stated interval.

  Not formalized (and why), per the layer's fidelity policy:

    * **Theorem S1 (nesting)** — monotonicity of the power means in θ —
      and with it the prefix/ladder structure of `σ*` and the full
      pointwise clause of S2(i) on the band `s ∈ (1, 13/8)`: the
      θ-family's order structure is genuinely analytic (real exponents);
      each rung's up-set-in-`s` structure is proved instead.
    * **The geometric member θ = 0 (σ = 1)** — its master comparison
      `s² ≥ 2` averages in log space; the exponential structure is
      beyond the ordered-field interface.  The paper's witness "`σ = 1`
      certifies `s = 3/2`" is covered by no theorem here.
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

end P1Sep
