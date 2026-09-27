/-
  Formalizations.P3_PiecewiseLinear
  =================================

  The **explicit half** of `prop:pl` (v11 of the paper):

  > `V^Π_k(b) = max_{α ∈ Γ^Π_k} αᵀ b` for a finite witness set `Γ^Π_k`
  > constructed by the masked backup, with `Γ^Π_0 = {1_V}` and
  > `Γ^Π_{k+1} = { α^{a,γ·} : a ∈ A(Π), γ· a selection }`, duplicates
  > removed by exact equality.
  > The worst-case growth is `|Γ^Π_{k+1}| ≤ |A| |Γ^Π_k|^{|Y|}`.

  `P3_Convexity` (v19) closed the **convexity** half, deliberately proving it
  directly on the Bellman recursion so as not to depend on the alpha-vector
  machinery being correct.  This module supplies the machinery itself, and
  proves the **growth law** — the "exact complexity statement" the paper
  singles out.

  ## What is proved, and what is deliberately not

  **Proved here.**  The growth law, as `Gamma_succ_length_le`.  It is a
  statement about the *construction* of `Γ`, and it is sharp: the raw
  step has size **exactly** `|A| · |Γ_k|^{|Y|}` (`step_length`), and
  deduplication only removes elements, giving `≤`.

  The growth law is **independent of what the backup operator does** — it
  holds for any `A → selection → α` map.  That is fortunate, because (see
  below) the P3 layer does not currently carry enough structure to define
  the paper's backup faithfully.  So the one part of `prop:pl` that *can*
  be proved without a modelling decision is proved here, and the rest is
  not faked.

  **Not proved, and why.**

  1. *The masked backup itself is not instantiated.*  The paper's
     `α^{a,γ·}(x) = Σ_{x'} T(x'|x,a) Σ_y g(y|x,a,x') γ_y(x')` needs two
     things the P3 `DetMDP` does not carry:

       - **A disturbance weighting.**  `DetMDP` has `univD : X → A → List D`
         and `F : X → A → D → X`, but no weights on `D`, so there is no
         `T(x' | x, a)` to sum against.  The natural reading is
         `T(x'|x,a) = Σ_{d : F x a d = x'} w(x,a,d)` for a weighting `w`,
         and `w` is exactly the modelling decision already flagged as
         blocking `thm:support`.  Rather than guess it, `backup` is left as
         a parameter of the construction.

       - **A finite `Y`.**  `DetMDP` has `obs : X → A → X → Y` but **no
         `univY : List Y`**, and in fact `obs` is a *deterministic*
         function, not a kernel `g(y | x, a, x')`.  So in this layer the
         observation sum `Σ_y g(y|x,a,x') γ_y(x')` collapses to the single
         term `γ_{obs x a x'}(x')`.  `PLData` below therefore carries
         `univY` explicitly.

  2. *Rationality is not expressible.*  "Every `α` is an exact rational
     vector, every `V_k(b)` at a rational belief is an exact rational" is a
     statement about `ℚ`, whereas every module here is parametric in an
     abstract `[OrdField K]`.  Formalizing it means specializing `K := ℚ`
     (or adding a `RatCast` interface), which is a separate change.

  3. *Deduplication needs `[DecidableEq K]`.*  `List.dedup` is absent from
     this stdlib, so `dedup` is supplied here.  It requires decidable
     equality on alpha-vectors, hence on `K` — which an abstract
     `OrdField` does **not** provide.  This is the honest root of the
     paper's "duplicates removed by exact equality": exact equality tests
     are a property of `ℚ`, not of an arbitrary ordered field.  The
     deduplicated family `Gamma` therefore carries `[DecidableEq K]`, while
     the raw `step` does not.

  ## Contents

    selections, selections_length   enumerating witness tuples
    selections_ne                   inhabited when the witnesses are
    dedup, dedup_length_le, dedup_ne
    step, step_length               **raw size is exactly |A|·|Γ|^{|Y|}**
    PLData                          the data the construction needs
    Gamma, gamma0                   the witness family, `Γ_0 = {1_V}`
    Gamma_ne                        `Γ_k` is inhabited
    Gamma_succ_length_le            **the growth law**
-/

import Formalizations.Prelude
import Formalizations.P3_Deterministic

namespace Formalizations.P3

open Formalizations
open Formalizations.POMDP

set_option linter.unusedSectionVars false

variable {K : Type} [OrdField K]
variable {X A D Y : Type}
variable {α : Type}

/-! ## Enumerating selections -/

/-- All tuples of length `ys.length` drawn from `wits` — the "selections"
`γ_· : Y → Γ_k` of `prop:pl`, enumerated as lists (a function `Y → α` is not
enumerable without `Fintype Y`, which this layer does not assume). -/
def selections : List Y → List α → List (List α)
  | [], _ => [[]]
  | _ :: ys, wits => (selections ys wits).flatMap (fun σ => wits.map (fun a => a :: σ))

/-- A constant-valued list sums to `c · length`. -/
theorem sum_map_const : ∀ (l : List α) (c : Nat), (l.map (fun _ => c)).sum = c * l.length := by
  intro l
  induction l with
  | nil =>
      intro c
      simp
  | cons a t ih =>
      intro c
      simp [ih, Nat.mul_succ, Nat.add_comm]

/-- The number of selections is `|wits|^{|Y|}` — the `|Γ_k|^{|Y|}` of the
growth law. -/
theorem selections_length : ∀ (ys : List Y) (wits : List α),
    (selections ys wits).length = wits.length ^ ys.length := by
  intro ys
  induction ys with
  | nil =>
      intro wits
      simp [selections]
  | cons y ys ih =>
      intro wits
      simp only [selections, List.length_flatMap, List.length_map, List.length_cons]
      rw [sum_map_const, ih, Nat.pow_succ]
      exact Nat.mul_comm _ _

/-- Selections are inhabited when the witness set is. -/
theorem selections_ne : ∀ (ys : List Y) {wits : List α}, wits ≠ [] →
    selections ys wits ≠ [] := by
  intro ys
  induction ys with
  | nil =>
      intro wits hw
      simp [selections]
  | cons y ys ih =>
      intro wits hw
      apply ne_nil_of_exists_mem
      rcases exists_mem_of_ne_nil (ih hw) with ⟨σ, hσ⟩
      rcases exists_mem_of_ne_nil hw with ⟨a, ha⟩
      exact ⟨a :: σ, List.mem_flatMap.mpr ⟨σ, hσ, List.mem_map.mpr ⟨a, ha, rfl⟩⟩⟩

/-! ## Deduplication

`List.dedup` is absent from this stdlib.  Note that dedup needs
`[DecidableEq]`, which is *not* available for an abstract `OrdField K` — see
the module header. -/

/-- Remove duplicates, keeping the first occurrence. -/
def dedup [DecidableEq α] : List α → List α
  | [] => []
  | a :: t => let r := dedup t; if a ∈ r then r else a :: r

theorem dedup_length_le [DecidableEq α] : ∀ (l : List α), (dedup l).length ≤ l.length := by
  intro l
  induction l with
  | nil => simp [dedup]
  | cons a t ih =>
      by_cases h : a ∈ dedup t
      · simp [dedup, h]
        exact Nat.le_trans ih (Nat.le_succ _)
      · simp [dedup, h]
        exact ih

theorem dedup_ne [DecidableEq α] : ∀ {l : List α}, l ≠ [] → dedup l ≠ [] := by
  intro l hl
  induction l with
  | nil => exact False.elim (hl rfl)
  | cons a t ih =>
      by_cases h : a ∈ dedup t
      · simp [dedup, h]
        exact ne_nil_of_exists_mem ⟨a, h⟩
      · simp [dedup, h]

/-! ## The raw backup step -/

/-- One masked-backup step over the *raw* (undeduplicated) family: for every
action and every selection, one new witness. -/
def step (univA : List A) (univY : List Y)
    (backup : A → List (List K) → List K) (wits : List (List K)) : List (List K) :=
  univA.flatMap (fun a => (selections univY wits).map (fun σ => backup a σ))

/-- **The raw step has size exactly `|A| · |wits|^{|Y|}`.**  This is the
growth law before deduplication, and it is an equality. -/
theorem step_length (univA : List A) (univY : List Y)
    (backup : A → List (List K) → List K) (wits : List (List K)) :
    (step univA univY backup wits).length =
      univA.length * wits.length ^ univY.length := by
  unfold step
  rw [List.length_flatMap]
  simp only [List.length_map]
  rw [selections_length]
  simpa [Nat.mul_comm] using sum_map_const univA (wits.length ^ univY.length)

theorem step_ne (univA : List A) (univY : List Y)
    (backup : A → List (List K) → List K) {wits : List (List K)}
    (hA : univA ≠ []) (hw : wits ≠ []) : step univA univY backup wits ≠ [] := by
  unfold step
  apply ne_nil_of_exists_mem
  rcases exists_mem_of_ne_nil hA with ⟨a, ha⟩
  rcases exists_mem_of_ne_nil (selections_ne univY hw) with ⟨σ, hσ⟩
  exact ⟨backup a σ, List.mem_flatMap.mpr ⟨a, ha, List.mem_map.mpr ⟨σ, hσ, rfl⟩⟩⟩

/-! ## The witness family -/

/-- The data `prop:pl`'s construction needs.  `backup` is left as a
parameter: see the module header for why the paper's masked backup cannot be
instantiated in this layer without a disturbance weighting. -/
structure PLData (K : Type) (X A Y : Type) where
  univX : List X
  univA : List A
  univA_ne : univA ≠ []
  univY : List Y
  backup : A → List (List K) → List K

/-- `Γ_0 = {1_V}`: the all-ones vector on the support. -/
def gamma0 (P : PLData K X A Y) : List K := P.univX.map (fun _ => (1 : K))

/-- **The witness family `Γ_k`**, with deduplication at every step. -/
def Gamma [DecidableEq K] (P : PLData K X A Y) : Nat → List (List K)
  | 0 => [gamma0 P]
  | k + 1 => dedup (step P.univA P.univY P.backup (Gamma P k))

/-- `Γ_k` is inhabited, so `max_{α ∈ Γ_k}` is well defined. -/
theorem Gamma_ne [DecidableEq K] (P : PLData K X A Y) : ∀ k, Gamma P k ≠ [] := by
  intro k
  induction k with
  | zero => simp [Gamma]
  | succ k ih =>
      simp [Gamma]
      exact dedup_ne (step_ne P.univA P.univY P.backup P.univA_ne ih)

/-- **`prop:pl`, growth law.**  `|Γ_{k+1}| ≤ |A| · |Γ_k|^{|Y|}`.

The inequality is exactly the composition of two facts: the raw step has
size `|A| · |Γ_k|^{|Y|}` (`step_length`), and deduplication never increases
length (`dedup_length_le`).  Note the bound is independent of `backup`. -/
theorem Gamma_succ_length_le [DecidableEq K] (P : PLData K X A Y) (k : Nat) :
    (Gamma P (k + 1)).length ≤
      P.univA.length * (Gamma P k).length ^ P.univY.length := by
  simp [Gamma]
  exact Nat.le_trans (dedup_length_le _)
    (Nat.le_of_eq (step_length P.univA P.univY P.backup (Gamma P k)))

end Formalizations.P3
