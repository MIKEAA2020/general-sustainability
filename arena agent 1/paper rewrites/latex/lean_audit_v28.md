# Lean audit v28 — the `Wmem` / `Wblind` question

**Object:** `paper2_probabilistic_sufficiency_v11.tex`, `thm:support`
consequence 1 ("for the unrestricted sequential class, `V_k(b) = 1` iff
`supp(b) ∈ 𝒲_k`"), and the two viable-set recursions defined in v27
(`P3_Viable.lean`).

**Question v27 left open.** The paper's recursion
`𝒲_k = {B : some admissible a maps every x ∈ B into 𝒲_{k-1}-supported
posteriors}` reads as a recursion that splits on the observation. v27 gave
both readings — `Wmem` (a continuation per observation; feedback) and
`Wblind` (one continuation for all successors; open loop) — proved
`Wblind_le_Wmem`, and refused to choose.

---

## 0. The answer in one paragraph

The paper **means `Wmem`, the feedback reading**, and the two readings are
**provably different**, so the choice is substantive rather than cosmetic.
`def:value` defines the unrestricted class as `Π = Π_seq`, "the class of
**all sequential policies**" (line 226), and `thm:recursion` — the belief
value recursion `V_k = max_a Σ_y P(y|b,a) V_{k-1}(τ(b,a,y))`, whose `∀y`
is exactly the `∀y` inside the definition of `𝒲_k` — is stated as exact on
it. The *proof prose* of consequence 1, however, is written in blind
vocabulary (`max_seq`, "declared sequence", "no declared sequence keeps
every compatible branch", lines 336–338), which is the vocabulary of
`prop:degen`'s declared blind class `Π_B`, not of `Π_seq`. So the
statement and the proof of consequence 1 quantify over two different
policy classes. A machine-checked model (deterministic kernels,
deterministic observations, horizon 2) has `Wmem M 2 B ∧ ¬ Wblind M 2 B`,
so this cannot be waved away as loose phrasing with equal content.

---

## 1. The four checks, with the text

### 1.1 How is "the unrestricted sequential class" defined? → **policies**

`def:value`, lines 219–227:

> Fix a declared policy class `Π`. The safety value at horizon `k` is the
> maximal class-survival probability
> `V^Π_k(b) = max_{π ∈ Π} P_π( x_t ∈ 𝒱 for t = 0,…,k | b )`, the horizon
> counting the current state. **The unrestricted class `Π = Π_seq` is the
> class of all sequential policies.**

This is a definition, and it defines the exact phrase consequence 1 uses.
"The class of all sequential policies" is the feedback class: a policy
maps histories — including the observations in them — to actions.

Corroboration from `thm:recursion`'s proof (lines 286–290):

> For non-Markov classes (**the hold and open-loop classes** of
> Section `\ref{agreement}`) the class constraint couples stages.

So `Π_seq` is *not* among the non-Markov (hold / open-loop) classes. It is
the class on which the `Σ_y` belief recursion is exact — and that
recursion branches on `y`.

### 1.2 Does the proof of consequence 1 branch on an observation? → **no, it does not**

Lines 332–341:

> Sufficiency is induction on `k`: the calculus's **witness sequence**
> keeps every compatible trajectory inside `𝒱` … For the converse, with
> deterministic observations **the realized observation path is fixed by
> the declared sequence**, so `V_k(b) = max_seq Σ_{x surviving} b(x)`; if
> `supp(b) ∉ 𝒲_k` **no declared sequence** keeps every compatible branch,
> so each sequence loses at least one branch of mass `b(x) ≥ min_{x'} b(x')` …

The decisive test ("does any proof step branch on an observation?") comes
out **negative**: the proof maximizes over *sequences* and never
constructs a policy tree. It also relies on "the realized observation path
is fixed by the declared sequence", which is the blind-window idiom.

So: **statement = `Π_seq` (feedback); proof = blind.** The two halves of
consequence 1 quantify over different classes. That is the defect.

### 1.3 Do the downstream uses need feedback?

* `prop:antichain` (lines 348–351): "`𝒮_k` be the family of subsets `S` of
  the support that are jointly survivable by one admissible
  **class-element (sequence or policy)**" — the paper explicitly carries
  both vocabularies here and does not choose.
* Monotonicity (`𝒮_{k+1} ⊆ 𝒮_k`, `prop:freeze`) and the min-mass
  consequence hold under either reading.
* So nothing downstream *forces* feedback — but nothing licenses the blind
  reading either.

### 1.4 Is the surrounding machinery blind? → **where a blind window is assumed, yes**

* `prop:degen` (lines 645–650): "**Let the window be blind** with declared
  sequential class `Π_B`. Then the degenerated value is the
  survived-mass formula `V_k(b) = max_{(u_0,…) ∈ Π_B} Σ_x b(x) 1[x
  survives (u_0,…)]`." — explicitly blind, explicitly sequences.
* `thm:lattice` (lines 905–915): `V^{Π_hold} ≤ V^{Π_ol} = V^{Π_seq,blind}
  ≤ V^{Π_obs}`, "the middle equality holding because **no observation
  arrives inside the window**, so sequential blind policies reduce to
  open-loop sequences". The lattice names `Π_seq,blind` as a class
  *distinct from* the observed class and, implicitly, from `Π_seq`.
* `rem:scope` / `thm:class`: "under the **unrestricted sequential blind
  class** the same cells attain value 1 by oscillation" (lines 950, 1000).

Point 1.4 is what made the blind reading attractive, and it is not wrong —
it is just scoped. The class lattice's blind classes are the ones the
`DetMDP` layer models; `thm:support` consequence 1 is stated for `Π_seq`,
which is not one of them.

---

## 2. Verdict

| | class | `𝒲_k` | Lean status |
|---|---|---|---|
| `thm:support` consequence 1, **as stated** | `Π_seq` = all sequential policies | `Wmem` | set side **closed this version** (`Wmem_iff_feedback`); value side open (§5) |
| `thm:support` consequence 1, **as proved** | blind sequences | `Wblind` | closed by v27 (`Wblind_iff_survK`) |
| `prop:degen` | `Π_B`, blind window | either | closed by v27, and §4 shows the two coincide there anyway |

v27's `Wblind_iff_survK` is therefore **not wrong** — it is the right
theorem for `prop:degen`'s declared blind class — but it is **not**
consequence 1. Consequence 1 needs `Wmem`.

---

## 3. The two readings are genuinely different

`Wmem_not_le_Wblind` (`P3_Feedback.lean`) exhibits a model and a support
with `Wmem M 2 B ∧ ¬ Wblind M 2 B`, and the model has

* **deterministic kernels** (`|univD x a| = 1` for every `x`, `a` — proved
  as `wm_detKernel` against `DetKernel M`), and
* a **deterministic observation map** (a function `X → A → X → Y`, as
  `DetMDP` always has),

i.e. it sits inside `thm:support`'s own hypothesis class ("on finite
models with deterministic kernels and deterministic observation maps").

The mechanism is the ordinary value of observation:

* support `B = {p, q}`, both safe;
* one admissible action `a₀` separates the branches: `p ↦ p₁`, `q ↦ q₁`,
  both safe, with **different observations** (`true` vs `false`);
* at the second stage, `b` is safe only from `p₁` and `c` only from `q₁`;
  from `p₁`, `c` and `a₀` lead to `dead`, from `q₁`, `b` and `a₀` do.

A feedback policy ("`a₀`, then `b` if you saw `true`, `c` if you saw
`false`") keeps both branches alive; **no single schedule does**, because
whatever action is declared second, one of `{p₁, q₁}` dies. Hence
`Wmem M 2 B` and `¬ Wblind M 2 B`.

Consequences:

1. `Wmem_le_Wblind` is **not a theorem** — `Wmem_le_Wblind_is_false`
   proves its negation even under deterministic kernels. The question v27
   flagged cannot be dissolved; it must be answered.
2. `Wblind ⊊ Wmem` in general (`Wblind_le_Wmem` from v27 gives `⊆`, the
   counterexample gives strictness at `k = 2`).
3. Nothing here depends on v27's editorial decision to conjoin `B ⊆ 𝒱` at
   every level: both recursions carry the same conjunct, and the
   counterexample's failure is exactly the single-continuation
   requirement, not the safety conjunct.
4. The comparison is at `k = 2`, which is minimal: at `k = 1` the two
   recursions coincide.

---

## 4. What v28 adds to the Lean layer

`lean/Formalizations/P3_Feedback.lean` (new module, 32nd import):

| declaration | statement | axioms |
|---|---|---|
| `survPol` | survival under a policy `π : List Y → A` with an observation history | — |
| `survPol_congr` | `survPol` sees `π` only through continuations of the current history | `[propext]` |
| **`Wmem_iff_feedback`** | `Wmem M k B ↔ ∃ π, (∀ h, π h ∈ univA) ∧ ∀ x, B x → survPol M k π [] x` | `[propext, Classical.choice]` |
| `Wmem_le_Wblind_of_blind` | constant `obs ⟹ Wmem ⊆ Wblind` | `[propext, Quot.sound]` |
| **`Wmem_eq_Wblind_of_blind`** | constant `obs ⟹ Wmem = Wblind` at every `k`, `B` | `[propext, Quot.sound]` |
| `WmX/WmA/WmD`, `wmModel`, `wmB` | the separating model | — |
| **`Wmem_not_le_Wblind`** | `∃ M B, DetKernel M ∧ Wmem M 2 B ∧ ¬ Wblind M 2 B` | `[propext]` |
| `Wmem_le_Wblind_is_false` | `¬ ∀ M k B, DetKernel M → Wmem M k B → Wblind M k B` | `[propext]` |

`Classical.choice` in `Wmem_iff_feedback` is load-bearing, not an
accident: `Y` is an arbitrary type with no finiteness hypothesis, so
selecting one continuation policy *per observation* genuinely needs
choice. `Quot.sound` enters the collapse lemma through function
extensionality (identifying the `y₀`-slice with the successor set).

`Wmem_eq_Wblind_of_blind` is the set-level form of `thm:lattice`'s middle
equality: on a blind window, "sequential blind policies reduce to
open-loop sequences". It is what makes v27's `Wblind` work legitimate for
`prop:degen` — where the paper assumes a blind window — while leaving
consequence 1 (no such assumption) on the `Wmem` side.

Build: **`lake build` → rc 0, 35 jobs, 0 warnings, 0 `sorry`.**

---

## 5. What is still open, and why it is not a small step

`Wmem_iff_feedback` closes the **set** side of consequence 1 for the
feedback reading: "`supp(b) ∈ 𝒲_k`" is now a machine-checked statement
about the existence of an admissible observation-history policy that keeps
every branch alive.

The **value** side is not closed, for either reading:

* For the blind reading: the mechanical composition of
  `Wblind_iff_survK` + `survT_iff_survK` +
  `VR_eq_total_of_jointly_surviving` (v27's open item 1). It needs a
  membership characterisation of `tuples M k`
  (`t ∈ tuples M k ↔ t.length = k ∧ ∀ a ∈ t, a ∈ univA`) and a
  tuple↔schedule conversion lemma. Mechanical, ~80 lines, still not in
  the tree.
* For the feedback reading — the one consequence 1 actually needs — the
  layer has **no feedback value operator**. `VR` (`P3_Deterministic`) is
  `lmax` over action *tuples*; a feedback value must maximize over
  *policy trees*, and `lmax` only applies to a finite list. The class
  `List Y → A` is infinite and `Y` carries no finiteness hypothesis, so
  the class must first be reduced to a finite one (e.g. trees that branch
  only on observations reachable from the support within `k` steps, with a
  default action otherwise), and that reduction is a module of its own.

Both are recorded as open rather than faked.

---

## 6. Recommended paper-side fix

The statement does **not** have to be weakened. Consequence 1 is *true*
under the feedback reading, because `thm:recursion` + the support identity
derive it in three lines:

```
V_k(b) = 1  ⟺  ∃a, ∀ y with P(y|b,a) > 0,  V_{k-1}(τ(b,a,y)) = 1
         ⟺  ∃a, ∀ y,  Post(supp b, a, y) ∈ 𝒲_{k-1}
         =  Wmem k (supp b)
```

— which is precisely the `∀y` in the paper's own definition of `𝒲_k`. The
definition and the statement are consistent with each other; it is the
**proof** that silently changes classes.

Concretely, in the next revision:

1. **Keep** `𝒲_k` and consequence 1 as stated, and say explicitly that the
   class is `Π_seq` ("all sequential policies", `def:value`), so `𝒲_k` is
   the feedback recursion.
2. **Fix the proof prose** of consequence 1 (lines 332–341): replace
   "`max_seq Σ_{x surviving} b(x)`" / "no declared sequence keeps every
   compatible branch" by the corresponding statements over **policy
   trees** (a policy's realized path is determined per branch; the
   maximization is over policies, and the loss is at least `min_x b(x)`
   because some branch of positive mass dies). The min-mass bound itself
   survives unchanged — if `supp(b) ∉ 𝒲_k`, every policy loses at least
   one `x ∈ supp(b)`, and `b(x) ≥ min_{x'} b(x')`.
3. Optionally note, where `prop:degen` and `thm:lattice` are stated, that
   on blind windows the feedback and blind recursions **coincide** —
   proved as `Wmem_eq_Wblind_of_blind` — so nothing in the blind-window
   material needs to change.

No code-side fiat was applied: `Wmem` and `Wblind` are both in the tree,
both are identified with survival under their respective policy classes,
the unconditional inclusion is proved, the converse is refuted by an
explicit model, and the paper decides which one `𝒲_k` denotes.

---

## 7. Record

* New module `lean/Formalizations/P3_Feedback.lean`; `Formalizations.lean`
  extended to 32 imports; full `lake build` green (35 jobs, 0 warnings,
  0 `sorry`).
* Axioms of the new theorems: as tabulated in §4 — `propext`,
  `Classical.choice` (only in `Wmem_iff_feedback`), `Quot.sound` (only
  through `funext` in the collapse lemma). No custom axioms, no `sorry`.
* Coverage totals for P3 are unchanged from v27: 11 complete, 0 partial,
  6 instance, 1 out of reach.
