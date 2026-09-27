# Lean audit v24 — the disturbance question: I was wrong, and the paper already answered it

**Result: `lake build` rc = 0, 31 jobs, 0 warnings, 0 `sorry`.**
File: `lean/Formalizations/P3_RobustPL.lean`.

v24 is mostly a correction. v23 asked which disturbance weighting to add.
That question should never have been asked — **the paper answers it, and the
code already implements the answer.** No new structure was needed.

---

## The correction

v23 said `prop:pl` and `thm:support` were "blocked on a disturbance-weighting
modelling decision that `DetMDP` does not carry," and offered three readings.
That framing was wrong, and it was wrong in a way worth naming: I was trying to
instantiate the **stochastic** masked backup in the **deterministic** P3 layer.
The paper explicitly says those are different operators.

`rem:operators` (v11, "the two operators"):

> The expectation over the disturbance law and the adversarial reading of
> its support are *different Bellman operators*. Proposition `prop:degen`
> states the deterministic degeneration as a change of operator: when the
> kernels are deterministic the stochastic expectation is replaced by the
> robust (adversarial-support) reading, and the resulting value is the
> robust value of the companion papers. **The degeneration is a theorem
> about the robust operator; it is not a claim about the stochastic plant,
> whose expectation and robust readings differ in general.**

`prop:degen` (survived-mass formula):

> Let the kernels be deterministic, `x⁺ = F(x,a,d)`, and let **the
> disturbance be read adversarially within its support** … a branch survives
> a declared sequence exactly when it survives under **every** disturbance in
> its support.

So: **adversarial.** Not as a conservative fallback and not as a
reinterpretation — it is the operator the paper prescribes for exactly the
setting `DetMDP` models. The three-way menu in v23 was a false choice, because
two of its options were readings of the *other* operator.

## And it was already implemented

`P3_Deterministic.survT` (v1) **is** the adversarial reading:

```
survT M []       x := safe x
survT M (a :: t) x := safe x && (univD x a).all (fun d => survT M t (F x a d))
```

"Every disturbance path stays in 𝒱" — an `all` over `univD`. Its own doc
comment says so. And `VR` is already `prop:degen`'s survived-mass formula.
The weighting I went looking for was never missing; the connection to
`prop:pl`'s alpha-vector language was. That is what v24 supplies.

**Lesson recorded:** when the code fails to supply a hypothesis, check whether
the theorem being formalized is the one the *paper* states for that layer,
before asking the user to pick a model.

---

## What `prop:pl` actually asserts here, and what is now proved

`prop:pl` gives two forms. The general masked backup
`α^{a,γ·}(x) = Σ_{x'} T(x'|x,a) Σ_y g(y|x,a,x') γ_y(x')` is a statement about
the **stochastic** operator. It is **out of scope for the deterministic P3
layer by design** — not by omission, and not because it is hard. Its segment
form is the applicable one:

> For a blind open-loop window the equivalent segment form applies: each
> admissible action segment `(u_0,…,u_m) ∈ Π` contributes the witness
> `α^seg = (1[the segment saves branch x])_x` and
> `V^Π_k(b) = max_seg α^segᵀ b`.

which is `prop:degen`'s formula in alpha-vector notation, hence `VR`. Proved:

| theorem | statement |
|---|---|
| `alphaSeg`, `GammaSeg` | the segment witnesses and the witness family |
| `survT_adversarial` | the adversarial reading made explicit |
| `smass_eq_dotOn` | survived mass `= α^segᵀ b` |
| **`VR_eq_max_alpha`** | **`V_k(b) = max_{α ∈ Γ_k} αᵀ b` — `prop:pl` segment form** |
| `GammaSeg_ne` | `Γ_k` inhabited, so the max is well defined |
| `tupleAux_length`, `tuples_length` | `\|Π_B\| = \|A\|^k` |
| `GammaSeg_length` | `\|Γ_k\| = \|A\|^k` (before dedup) |
| **`GammaSeg_succ_length`** | **`\|Γ_{k+1}\| ≤ \|A\|·\|Γ_k\|` — the growth law, blind window** |

`GammaSeg_succ_length` is the `|Y| = 1` specialization of v23's general law
`|Γ_{k+1}| ≤ |A|·|Γ_k|^{|Y|}` — the right one, since a blind open-loop window
receives no observations, so the selection index is trivial. It holds with
equality before deduplication.

### The "masked" in masked backup

Worth recording, because it is the one place the terminology could mislead:
in `prop:pl` the masking is the `α(⊥) = 0` anchor — the backup sums over `𝒱`
only and `⊥` is absorbing, so no backup revives a lost branch. In the
deterministic segment form this is automatic: `α^seg` is the *survival*
indicator, which is `0` off `𝒱` by construction. There is no separate masking
step to formalize.

## Axioms (`#print axioms`)

```
survT_adversarial        [propext, Quot.sound]
VR_eq_max_alpha          [propext, Classical.choice]
GammaSeg_succ_length     [propext, Quot.sound]
```

No `sorry`, no `admit`.

---

## Status

`prop:pl` is now **closed for the deterministic P3 layer**: convexity (v19),
the witness set, the alpha-representation, and the growth law. The **general
stochastic masked backup remains out of scope** — correctly so, and this is a
scope statement about the layer, not a gap.

| component | status |
|---|---|
| convexity | complete (v19) |
| witness set `Γ_k`, inhabited | complete (v24) |
| `V_k(b) = max_{α ∈ Γ_k} αᵀ b` (segment form) | **complete (v24)** |
| growth law | complete (v23 general, v24 blind-window) |
| general stochastic masked backup | **out of scope by design** — other operator |
| exact rationality | out of scope — needs `K := ℚ` |

P3 coverage (18): complete 11 · partial 0 · instance 6 · out of reach 1.

## Next

`thm:support` is now the **only** open P3 result. Its content is the support
identity `supp(b⁺(·|a,y)) = Post(supp(b), a, y)` plus three consequences
(`V_k(b) = 1 ⟺ supp(b) ∈ 𝒲_k`; the `1 - V_k(b) ≥ min_x b(x)` bound; and
monotonicity in `k`). Note the first consequence is `prop:degen`'s, and the
third overlaps `prop:freeze` (v18) — so the genuinely new work is the support
identity itself.

`lean_README_v4.md` remains stale on `prop:freeze`, `prop:pl`,
`prop:antichain`; it will be updated with the next batch.

## Commits

| commit | content |
|---|---|
| `0dafd81` | v21 — `prop:antichain` (ii) |
| `8d49013` | v22 — `prop:antichain` (iv) |
| `489cc96` | v23 — `prop:pl` growth law |
| *this turn* | v24 — `P3_RobustPL`: adversarial reading confirmed, `prop:pl` segment form |
