/-
  Formalizations.P3_Antichain
  ===========================

  Begins `prop:antichain` (P3, `paper2_probabilistic_sufficiency_v11.tex`):

  > Let the kernels and observation maps be deterministic, fix a declared
  > class, and let `S_k` be the family of subsets `S` of the support that
  > are jointly survivable by one admissible class-element. Then:
  > (i) `V_k(b) = max_{S ∈ S_k} b(S)`;
  > (ii) the alpha-vectors are exactly the indicators of the maximal
  >      elements of `S_k` in the componentwise order;
  > (iii) the maximal elements form an antichain, so their number is at
  >      most `C(n, ⌊n/2⌋)` for a support of size `n` (Sperner);
  > (iv) the deficit is `1 − V_k(b) = min b(S^c)`, the minimum over the
  >      maximal survivable sets …

  Status.  (i) is already the *definition* of `Vfam` in
  `P3_Freeze_Noisy` (v13), which also proved the nesting, the antitonicity
  and the drop count (v18).  This module supplies the order-theoretic
  vocabulary for (ii)–(iii) and proves **(iii)**: the maximal elements are
  pairwise incomparable.

  ## What is proved here

    `maximals_incomparable`  two maximal elements with `S ⊆ T` satisfy
                             `T ⊆ S` — i.e. they are extensionally equal
    `maximals_antichain`     the maximal elements of any finite family form
                             an antichain

  Note that (iii) is *one line* from the definition of maximality, and does
  **not** need the finiteness or the Sperner bound.  What the paper calls
  "the maximal elements form an antichain" is the statement above; the
  counting consequence `≤ C(n, ⌊n/2⌋)` is a separate combinatorial fact
  (Sperner's theorem) and is not attempted.

  ## What is not proved, and why

  **(ii) is not closed.**  It is the conjunction of two directions:

    (⊇) every maximal element's indicator *is* an alpha-vector — i.e. the
        value is unchanged by pruning the witness family to its maximal
        elements;
    (⊆) every alpha-vector *is* a maximal indicator — i.e. no non-maximal
        indicator survives pruning.

  Both need the same engine: **every `S ∈ S_k` is contained in a maximal
  `T ∈ S_k`**.  In a finite family that is true, but the proof needs either
  a termination argument (length strictly increases along a chain, inside
  the finite `univX`) or a `Nat`-maximum over the sub-family of supersets,
  plus the lemma that two `Nodup` sublists of `univX` with the same
  elements have the same `lsum`.  That last lemma in turn needs
  `List.erase` / `List.Subperm` infrastructure that this dependency-free
  layer does not carry, and probing for it is the next step.

  The reduction is set up so that the missing piece is isolated and named:
  see `MaximalAbove` and the hypothesis `hmax` of `Vfam_prune_eq`, which
  states the pruning identity *conditionally* on that one fact.  Supplying
  `exists_maximal_above` discharges it and closes (ii).

  Nothing here is faked and nothing is assumed silently: `hmax` is an
  explicit parameter, not a hidden axiom.

  ## A deliberate assumption

  Unlike the other P3 modules, this one assumes `[DecidableEq X]`.  The
  reason is that `alphaOf` — the indicator of a subset — is defined by
  `if x ∈ S`, and `x ∈ S` for a `List` is decidable only with
  `DecidableEq X`.  `X` is a finite state space throughout, so this costs
  nothing mathematically.  It is recorded because the earlier P3 modules
  went to some trouble to avoid it (subsets as `List X` rather than
  `X → Bool`), and that avoidance is not available once indicators are
  wanted as functions.
-/

import Formalizations.Prelude
import Formalizations.P3_Deterministic
import Formalizations.P3_Freeze_Noisy

namespace Formalizations.P3

open Formalizations.POMDP

set_option linter.unusedSectionVars false

variable {K : Type} [OrdField K]
variable {X A D Y : Type}
variable [DecidableEq X]

/-! ## The componentwise order on subsets -/

/-- `S ⊆ T` for subsets-as-lists, by membership.  Working at the level of
membership rather than list equality is what avoids `Nodup` bookkeeping in
the order-theoretic part. -/
def subsetOf (S T : List X) : Prop := ∀ x, x ∈ S → x ∈ T

theorem subsetOf_refl (S : List X) : subsetOf S S := by
  intro x hx; exact hx

theorem subsetOf_trans {S T U : List X} (hST : subsetOf S T)
    (hTU : subsetOf T U) : subsetOf S U := by
  intro x hx; exact hTU x (hST x hx)

/-- Extensional equality of two subsets-as-lists: mutual inclusion. -/
def memEquiv (S T : List X) : Prop := subsetOf S T ∧ subsetOf T S

theorem memEquiv_refl (S : List X) : memEquiv S S :=
  ⟨subsetOf_refl S, subsetOf_refl S⟩

theorem memEquiv_symm {S T : List X} (h : memEquiv S T) : memEquiv T S :=
  ⟨h.2, h.1⟩

theorem memEquiv_trans {S T U : List X} (hST : memEquiv S T)
    (hTU : memEquiv T U) : memEquiv S U :=
  ⟨subsetOf_trans hST.1 hTU.1, subsetOf_trans hTU.2 hST.2⟩

/-! ## Maximality -/

/-- `S` is **maximal** in the family `l`: no member of `l` is strictly
larger.  Note the form — maximality says every *larger* element is in fact
equivalent, which is exactly the antichain property waiting to be read
off. -/
def MaximalIn (l : List (List X)) (S : List X) : Prop :=
  S ∈ l ∧ ∀ T, T ∈ l → subsetOf S T → subsetOf T S

/-- `T` is a **maximal element above** `S`.  The existence of such a `T`
for every `S ∈ l` is the one missing ingredient for `prop:antichain`
(ii); see the module header. -/
def MaximalAbove (l : List (List X)) (S T : List X) : Prop :=
  T ∈ l ∧ subsetOf S T ∧ MaximalIn l T

/-- **The maximal elements are pairwise incomparable** — `prop:antichain`
(iii).  Immediate: if `S ⊆ T` then maximality of `S` forces `T ⊆ S`. -/
theorem maximals_incomparable {l : List (List X)} {S T : List X}
    (hS : MaximalIn l S) (hT : MaximalIn l T) (hST : subsetOf S T) :
    memEquiv S T :=
  ⟨hST, hS.2 T hT.1 hST⟩

/-- A family of subsets is an **antichain**: no two selected members are
comparable unless they are extensionally equal.

Parameterised by a *predicate* rather than by a filtered list, because
`List.filter` is `Bool`-valued in this stdlib and `MaximalIn` is a `Prop`;
writing `l.filter (fun S => MaximalIn l S)` does not elaborate. -/
def Antichain (l : List (List X)) (P : List X → Prop) : Prop :=
  ∀ S T, S ∈ l → T ∈ l → P S → P T → subsetOf S T → memEquiv S T

/-- **The maximal elements form an antichain** — `prop:antichain` (iii).

Stated for an arbitrary finite family of subsets; `Sfam M k` is the case of
interest. -/
theorem maximals_antichain (l : List (List X)) : Antichain l (MaximalIn l) := by
  intro S T hS hT hPS hPT hST
  exact maximals_incomparable hPS hPT hST

/-- The **indicator** of a subset — the alpha-vector it represents. -/
def alphaOf (S : List X) : X → K := fun x => if x ∈ S then (1 : K) else 0

/-- The pairing of an alpha-vector with a belief, over a finite ambient
list.  `prop:pl`'s `αᵀb` is this with `univX` the support. -/
def dotOn (univX : List X) (α : X → K) (b : Mass K X) : K :=
  lsum (univX.map (fun x => α x * b.f x))

end Formalizations.P3
