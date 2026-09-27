# Lean audit v18 — `prop:freeze` closed (the drop count)

**Branch:** `lean-audit-v4` (additive). **Toolchain:** `v4.34.1`.
**Build:** `lake build` → **rc = 0, 25 jobs**, **0 warnings**, zero `sorry`.

New module **`lean/Formalizations/P3_Freeze_Noisy_v2.lean`** (9,985 B).

This is the first of the four P3 partials listed in v16. It closes
`prop:freeze` **completely**.

---

## The claim

> With deterministic kernels the survivable-set families satisfy
> `S_{ℓ+1} ⊆ S_ℓ`; hence `V_ℓ(b)` is non-increasing in the horizon and
> stabilizes after at most `2^{|supp b|}` strict decreases.

`P3_Freeze_Noisy` (v13) proved the nesting, the antitonicity, the magnitude
bound `|S_0| ≤ 2^{|supp b|}`, and the finite-range statement. It flagged the
**literal count of strict decreases** as not proved, describing it as
"bookkeeping" over an injectivity argument. That was the right instinct but
the wrong route: the obvious proof counts *distinct values*, which needs a
pigeonhole lemma over a deduplicated list — `List.dedup`, `List.Nodup`, and
ultimately `DecidableEq K`, none of which this dependency-free layer has.

## The route actually taken — count sets, not values

Three observations replace all of that machinery:

1. **A strict drop removes a set** (`drop_removes_set`). If
   `V_{k+1}(b) < V_k(b)`, take a maximizer `S*` for `V_k`. Were `S*` still
   in `S_{k+1}`, its mass would be `≤ V_{k+1}(b)`, contradicting the drop.
   So `S* ∈ S_k` but `S* ∉ S_{k+1}`.
2. **`S_{k+1}` is `S_k` filtered by survival to `k+1`**
   (`Sfam_succ_length_strict`). Filter twice by nested predicates and you
   have filtered once by the stronger one; a discarded witness makes the
   filter *strictly* shorten the list (`filter_strict`).
3. **The family only shrinks**, so sets removed at distinct drops are
   distinct — no `Nodup` argument needed, because the nesting supplies the
   separation for free.

The invariant proved is stronger than the count and is what makes the
induction close in a single pass:

```
drops M b n + (Sfam M n).length ≤ (Sfam M 0).length
```

Every drop pays for itself by removing a set. From it,
`drops M b n ≤ |S_0| ≤ 2 ^ M.univX.length` follows with `Sfam0_card_le`.
No `DecidableEq X` and no `DecidableEq K` is required anywhere.

## New declarations

| Declaration | Content |
|---|---|
| `length_filter_le_gen` | polymorphic `length_filter_le` |
| `filter_strict` | a filter that discards something *strictly* shortens the list |
| `filter_filter_of_imp` | filtering twice by nested predicates = filtering by the stronger |
| `Sfam_succ_length_le` / `Sfam_succ_length_strict` | the family as an iterated filter |
| `drop_removes_set` | every strict decrease removes at least one set |
| `drops` | the count of strict decreases before horizon `n` |
| `drops_bound` | the counting invariant |
| `drops_le_card` | `drops ≤ |S_0|` |
| **`prop_freeze_drop_count`** | **`prop:freeze` in full** |

*Axioms:* all three checked → `[propext, Classical.choice, Quot.sound]`.
Choice enters only through `lmax`, which is inherent to the value being a
maximum over a family.

## What this does and does not say

The theorem bounds the number of strict decreases **before horizon `n`,
uniformly in `n`**. That is the paper's "stabilizes after at most
`2^{|supp b|}` strict decreases" — the bound does not degrade with the
horizon, which is the content of the claim. What is *not* asserted is a
specific freezing index: the proof shows at most `2^{|supp b|}` drops can
ever occur, but does not identify the `ℓ` at which the last one happens
(that would need a `Nat`-valued `find` over an unbounded search, and it
follows trivially from the uniform bound anyway).

`prop:freeze` is now **complete**. P3 moves to 8 results, 3 partial
(`thm:support`, `prop:antichain`, `prop:pl`), 6 instance-level, 1 out of
reach.

## Technical notes for the next modules

Five things cost a build round each here; recording them so they are not
re-learned.

1. **`List.filter` is `Bool`-valued in this stdlib.** Writing
   `.filter (fun S => p S)` with `p : α → Prop` works *inside* a
   `classical` block (Lean inserts `decide`), but **fails in a theorem
   statement**, where no `Decidable` instance is in scope. `Sfam` only
   compiles because its body is `by classical exact …`. Fix: state the
   lemma as a `Prop`-valued *length inequality* rather than a list equality,
   so no `decide` appears in the statement at all.
2. **`simp` cancels `+ 1` across `≤` for `Nat`.** In `filter_strict`, after
   `simp [hpa]` the goal is already `(t.filter p).length + 1 ≤ t.length`;
   applying `Nat.succ_le_succ` overshoots. `simpa [hpa] using iht` is the
   robust idiom.
3. **`Mass` lives in `Formalizations.POMDP`.** Without
   `open Formalizations.POMDP`, `Mass K X` is treated as an unknown
   identifier and `autoImplicit` turns it into a bound variable — the
   resulting "Function expected at `Mass`" error points at the wrong line.
4. **A recursive `def` whose branch needs decidability must use `letI`.**
   `| n + 1 => by classical exact …` does not give the equation compiler a
   `Decidable`; `letI : Decidable (…) := Classical.propDecidable _` does.
5. **Line-range edits in a `calc`/`by_cases` block silently drop `·`
   separators.** Verifying the patched region before building is cheaper
   than chasing the resulting "unsolved goals / case neg".

## Suggested next steps

1. **`prop:pl` (convexity of `V` over `OrdField`).** The max-of-linear-
   functionals part is already in place; what is missing is convexity, which
   needs a midpoint inequality on `lsum` — likely the cheapest of the three
   remaining.
2. **`prop:antichain` (ii)** — the alpha-vector characterisation.
3. **`thm:support`** — the support identity
   `supp(b⁺(·|a,y)) = Post(supp b, a, y)`. This is the hard one: it needs a
   disturbance *weighting*, because the robust reading has no disturbance
   distribution and so the posterior mass is not even defined. It is a
   modelling decision, not just a proof.
