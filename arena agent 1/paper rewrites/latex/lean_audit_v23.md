# Lean audit v23 — `prop:pl`, the explicit half: growth law proved, two structural blockers named

**Result: `lake build` rc = 0, 30 jobs, 0 warnings, 0 `sorry`.**
File: `lean/Formalizations/P3_PiecewiseLinear.lean` (10.1 KB).

`prop:pl` reads, in relevant part:

> `V^Π_k(b) = max_{α ∈ Γ^Π_k} αᵀ b` for a finite witness set `Γ^Π_k`
> constructed by the masked backup … with `Γ^Π_0 = {1_V}` …
> The worst-case growth is `|Γ^Π_{k+1}| ≤ |A| |Γ^Π_k|^{|Y|}`.

`P3_Convexity` (v19) had closed the **convexity** half, deliberately proved
directly on the Bellman recursion so as not to depend on the alpha-vector
machinery being correct. This module builds the machinery and proves the
**growth law**. It also identifies two places where the proposition cannot be
faithfully instantiated in this layer, and says so rather than papering over it.

---

## What is proved

**The growth law**, as `Gamma_succ_length_le`:

```
{K : Type} [OrdField K] {X A Y : Type} [DecidableEq K]
  (P : PLData K X A Y) (k : Nat) :
    (Gamma P (k+1)).length ≤ P.univA.length * (Gamma P k).length ^ P.univY.length
```

which is verbatim `|Γ_{k+1}| ≤ |A| · |Γ_k|^{|Y|}`.

It is a composition of two facts, both proved:

- `step_length` — the **raw** (undeduplicated) step has size *exactly*
  `|A| · |Γ_k|^{|Y|}`, not merely at most;
- `dedup_length_le` — deduplication never increases length.

So the inequality is sharp, and the slack in it is precisely the duplicates.
Supporting facts: `selections` / `selections_length` (the `|Γ_k|^{|Y|}`
count), `selections_ne`, `dedup` / `dedup_ne`, `Gamma_ne` (`Γ_k` is
inhabited, so `max_{α ∈ Γ_k}` is well defined), and `gamma0` (`Γ_0 = {1_V}`).

**A useful property of this theorem:** the growth law is *independent of what
the backup operator does*. It holds for any `A → selection → α` map. That is
what makes it provable here at all — see below.

---

## Two structural blockers, named rather than worked around

### 1. The paper's masked backup cannot be instantiated in this layer

`α^{a,γ·}(x) = Σ_{x'} T(x'|x,a) Σ_y g(y|x,a,x') γ_y(x')` needs two things
that `DetMDP` does not carry.

**No disturbance weighting.** `DetMDP` has `univD : X → A → List D` and
`F : X → A → D → X`, but **no weights on `D`** — so there is no
`T(x' | x, a)` to sum against. The natural reading is
`T(x'|x,a) = Σ_{d : F x a d = x'} w(x,a,d)`, and `w` is exactly the
modelling decision already flagged as blocking `thm:support`. I did not guess
it: `backup` is left as a parameter of `PLData`.

**No finite `Y`, and `obs` is not a kernel.** `DetMDP` has
`obs : X → A → X → Y` — a *deterministic function* — and **no
`univY : List Y`**. So in this layer the observation sum
`Σ_y g(y|x,a,x') γ_y(x')` collapses to the single term `γ_{obs x a x'}(x')`,
and the general kernel form of the paper is simply not the object being
formalized. `PLData` therefore carries `univY` explicitly.

Consequence: the wall-clock claim "`|Γ_{k+1}| ≤ |A| |Γ_k|^{|Y|}` is the exact
complexity statement for the general class" is proved here for the
construction. Whether the *paper's* `Γ` (with its kernel-based backup) obeys
the same law is immediate, but it is a statement about a structure this layer
does not yet have.

### 2. "Exact equality" deduplication and rationality both need more than an abstract ordered field

`List.dedup` is absent from this stdlib, so `dedup` is supplied here. It
requires `[DecidableEq]` on alpha-vectors, hence on `K` — and an abstract
`OrdField` carries **no** decidable equality. This is the honest root of the
paper's phrase "duplicates removed by exact equality": *exact equality tests
are a property of `ℚ`, not of an arbitrary ordered field.* The deduplicated
family `Gamma` therefore carries `[DecidableEq K]` as an assumption, while
the raw `step` and its exact size formula do not.

Similarly, the proposition's rationality clause — "every `α` is an exact
rational vector, every `V^Π_k(b)` at a rational belief is an exact rational"
— is a statement about `ℚ`, whereas every module here is parametric in
`[OrdField K]`. Formalizing it means specializing `K := ℚ` or adding a
`RatCast` interface. **Not attempted, and not claimed.**

So of `prop:pl`'s components: the growth law is proved; convexity was proved
in v19; the masked-backup representation `V_k(b) = max_{α ∈ Γ_k} αᵀ b`, the
rationality clause, and the segment form for blind open-loop windows are
**not** formalized.

---

## A process note

The `prop:pl` work is where the "find the latest versions first" discipline
paid off again, but also where a small trap recurred: two of the list helpers
in this layer (`ne_nil_of_exists_mem`, `exists_mem_of_ne_nil`) are declared
over `Type`, not `Type u`. Writing the polymorphic lemmas with a
universe-generalized `α` made them fail to apply, with an error
(`Ne.{1} ?l []` vs `Ne.{u_1+1} …`) that points at the call site rather than at
the universe. Fixing the section to `variable {α : Type}` resolves it.

## Axioms (`#print axioms`)

```
selections_length       [propext, Quot.sound]
step_length             [propext, Quot.sound]
Gamma_succ_length_le    [propext, Quot.sound]
Gamma_ne                [propext, Quot.sound]
```

No `sorry`, no `admit`, no axiomatized structure.

---

## Status

`prop:pl`, per component:

| component | status |
|---|---|
| convexity of `V^Π_k` | complete (v19) |
| finite witness set `Γ_k`, `Γ_0 = {1_V}` | complete (v23) |
| `Γ_k` inhabited | complete (v23) |
| growth law `\|Γ_{k+1}\| ≤ \|A\|·\|Γ_k\|^{Y}` | **complete (v23)**, sharp |
| masked backup `α^{a,γ·}` instantiated | **blocked** — needs a disturbance weighting |
| `V_k(b) = max_{α ∈ Γ_k} αᵀ b` | **open** — depends on the above |
| exact rationality of `α`, `V_k(b)` | **out of scope** — needs `K := ℚ` |
| segment form (blind open-loop) | **open** |

## Work order

1. ~~probe `erase`/`Subperm`/`Perm`, prove `lsum_eq_of_mem_iff`~~ — done (v21)
2. ~~`exists_maximal_above`, close (ii)~~ — done (v21)
3. ~~`prop:antichain` (iv)~~ — done (v22)
4. ~~`prop:pl` explicit half~~ — **growth law done (v23)**; the backup
   representation is blocked on the same disturbance-weighting decision as (5)
5. `thm:support` — **needs your decision on disturbance weighting**

**These two now converge.** Both remaining items are blocked on the same
question: what weights the disturbance set `univD x a`? Options I can see:

- **(a) uniform** — `w(x,a,d) = 1/|univD x a|`, giving the "nature is
  uniform" reading; needs `|univD x a|` invertible, i.e. a characteristic-zero
  assumption or an explicit nonzeroness field;
- **(b) adversarial / worst-case** — the existential-over-`D` reading, which
  is a `min` over disturbances rather than a weighted sum, and matches the
  safety framing of the rest of the paper;
- **(c) a new weighting field on the structure** — most general, closest to
  the paper's `T(x'|x,a)`, but changes `DetMDP` (or needs a parallel structure).

My reading is that **(b)** fits the paper's safety framing and the existing
`safe : X → Bool` field, but this is a modelling call about what the paper
means, not something I should decide from the code. Tell me which and I'll
build it.

**Carried forward:** `lean_README_v4.md` is still stale on the rows for
`prop:freeze`, `prop:pl` and `prop:antichain`; it will be updated with the
next batch.

## Commits

| commit | content |
|---|---|
| `e555b04` | wire the v7–v20 modules into the build |
| `0dafd81` | v21 — `prop:antichain` (ii) |
| `8d49013` | v22 — `prop:antichain` (iv) |
| *this turn* | v23 — `P3_PiecewiseLinear`, `prop:pl` growth law |
