# P3 ↔ EBC bridge — concrete specification

Status: **specified, not implemented.** Written so the next turn can
build it without re-deriving anything.

## 1. The two notions, side by side

**P3** (`P3_SurvivableAdm.lean`):

```lean
-- ll. 110-114
noncomputable def SfamAdm (M : DetMDP K X A D Y) (k : Nat) : List (List X) :=
  (subsetsOf M.univX).filter (fun S => SurvivableAdm M S k)

-- ll. 174-177
noncomputable def VfamAdm (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) : K :=
  lmax ((SfamAdm M k).map (fun S => bS S b))
```

`SurvivableAdm M S k` is `∃ u, admissible u ∧ ∀ x ∈ S, survK M k u x`
(ll. 104-106 show the monotone-in-`k` form). So **P3 survivability =
"one blind policy keeps every member alive for k steps"**, and the value
is the max mass over such sets.

**EBC** (`EBC_Dynamics.lean` ll. 226-228):

```lean
def survivesTo (I : List Nat) (θ : Nat → Bool) : List (Nat → Tri) → K → Prop
  | [], z => (1 : K) ≤ z
  | u :: us, z => (1 : K) ≤ z ∧ survivesTo I θ us (z + drift I u θ)
```

## 2. The bridge, in one definition

The two become the same sentence once EBC set-survivability is stated in
P3's shape:

```lean
def ebcSurvivable (I : List Nat) (A : List (Nat → Bool)) (z0 : K) : Prop :=
  ∃ us : List (Nat → Tri), ∀ θ, θ ∈ A → survivesTo I θ us z0
```

Then:

* **Heredity** — `A₂ ⊆ A₁ → ebcSurvivable I A₁ z0 → ebcSurvivable I A₂ z0`
  is immediate from `EBC_Classification.survivesSet_mono` (already
  proved). This is P3's "survivability is hereditary downward".
* **Value** — for the uniform prior on a support `S`, `bS A b = |A| / |S|`,
  so P3's `VfamAdm` reads `max{|A| : A ⊆ S, ebcSurvivable} / |S|`, which
  is exactly the paper's formula.

## 3. What `prop:bands` supplies, in this shape

Write `M(I, z0) = max |A|` over `ebcSurvivable` sets:

* **At the floor** (`z₀ = 1`): `EBC_Classification.floor_survivors_agree`
  says all members of a surviving set agree on `I`, so `M = 1`.
* **Above the edge** (`z₀ ≥ 1.1`): all pairs in a surviving set are at
  Hamming distance `≤ 1` (`EBC_Classification_v3.far_pair_horizon_bound`
  rules out `≥ 2` at every horizon), so `M ≤ 2`, with equality whenever
  the support contains an adjacent pair.
* **A probe** = fixing one coordinate. Model it as a restriction of the
  index set: the support after probing coordinates `P ⊆ I` to pattern
  `p` is

  ```lean
  def inSubcube (P : List Nat) (p : Nat → Bool) (θ : Nat → Bool) : Prop :=
    ∀ i, i ∈ P → θ i = p i
  ```

  A subcube with at least one *free* coordinate contains a
  Hamming-adjacent pair (take any member, flip one free coordinate), so
  `M = 2` there; a fully probed subcube is a single cell, so `M = 1`.

Hence the ladder: value `= 1/|S|` at the edge and `= min(1, 2/|S|)`
above it — the paper's two rows, with `|S|` symbolic so the `2^j`
arithmetic (instance-level) is never needed.

## 4. The one thing that remains, stated exactly

`VfamAdm` is a function of a `DetMDP`. To make P3's already-proved
`VfamAdm_prune_eq` *be* the ladder, one must exhibit a `DetMDP` over the
sixteen cells whose `survK M k u x` coincides with EBC's
`survivesTo I x us z0`. That means supplying:

* `X` = the 16 cells (`Nat → Bool`, modulo the index set),
* `A` = `Nat → Tri` actions,
* the transition/observation data the `DetMDP` structure requires, and
* a proof that `survK` reduces to the drift recursion
  `z ↦ z + drift I u θ` with floor `1`.

That is a modelling exercise, not a mathematical one — and it is what
"connect the P3 value functional to EBC survivability" costs. Everything
on the EBC side (items 2 and 3) is done or one lemma away.

## 5. Recommended sequencing

1. `EBC_Ladder.lean` — `ebcSurvivable`, heredity, the probe/subcube
   model, `subcube_has_adjacent_pair`, and the cardinality bounds
   (`M = 1` at the floor, `M ≤ 2` above). Self-contained; no P3 import.
2. A separate note recording that P3's `VfamAdm_prune_eq` gives the value
   formula in the same shape, so step 1 *is* `prop:ladder` modulo the
   `DetMDP` instance of §4.
3. Only then, if wanted, the `DetMDP` instantiation.
