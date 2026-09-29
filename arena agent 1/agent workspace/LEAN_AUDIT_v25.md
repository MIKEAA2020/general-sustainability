# Lean audit v25 — `thm:support` (support identity) is closed

**Result: `lake build` rc = 0, 32 jobs, 0 warnings, 0 `sorry`.**
File: `lean/Formalizations/P3_Support.lean` (8.1 KB).

With this, **all 18 P3 results are now accounted for**: 12 complete, 0
partial, 6 instance-level, 1 (`prop:probecount`) out of reach.

---

## The statement, and where it lives

> On finite models with deterministic kernels and deterministic observation
> maps, for every action `a` and observation `y`,
> `supp(b⁺(·|a,y)) = Post(supp(b), a, y)`.

The paper's proof:

> A state `x'` carries posterior mass exactly when some `x ∈ supp(b)` has
> `T(x'|x,a) · g(y|x,a,x') > 0`; with deterministic kernels and observation
> maps the indicators make this set exactly `Post(supp(b), a, y)`.

**This theorem does not belong on `DetMDP`, and that is the main finding of
this entry.** Every other P3 module is built on `DetMDP`, whose
`obs : X → A → X → Y` is *already* a deterministic function — there the
identity is vacuous, because there is no kernel left to degenerate.
`thm:support` is precisely a statement about the **degeneration**, so it has
to be stated where the kernels are genuinely stochastic. That is
`SafeMDP` (`P1_BeliefSafety`), which carries

```
T : A → X → X → K          g : A → X → X → Y → K
```

with nonnegativity and normalization. So the theorem becomes: *if* those
kernels are `0/1`-valued, *then* the posterior support is the set-valued
image — an explicit hypothesis rather than something baked into the model.
That is both more faithful and more informative than the `DetMDP` version
would have been.

The quantity under study is already exactly right:

```
obsMass M a y b x' = lsum (univX.map (fun x => b.f x * T a x x' * g a x x' y))
```

— literally the paper's `Σ_{x ∈ supp b} b(x)·T(x'|x,a)·g(y|x,a,x')`.

## What is proved

| theorem | statement |
|---|---|
| `le_lsum_of_mem` | one nonnegative term is below the sum of its list |
| `lsum_pos_exists` | a positive sum of nonnegative terms has a positive term |
| `DetKernels` | the `0/1` degeneration of `T` and `g` (the hypothesis) |
| `suppOf` | support as strict positivity of mass |
| `postMem` | `Post(B, a, y)` — the set-valued post-state |
| `obsMass_eq_filter` | the posterior collapses to a filtered sum |
| **`support_identity`** | **`supp(b⁺(·|a,y)) = Post(supp(b), a, y)`** |

As elaborated:

```
support_identity {K} [OrdField K] {X Y A} [DecidableEq X] [DecidableEq Y]
  (M : SafeMDP K X Y A) (DK : DetKernels M) (a : A) (y : Y)
  (b : Mass K X) (x' : X) :
    0 < (step M a y b).f x'  ↔  postMem M DK (suppOf b) a y x'
```

The proof is the paper's own argument, in two halves. `obsMass_eq_filter`
uses `lsum_filter_ind` to collapse `Σ_x b(x)·T·g` to the sum over those `x`
with `next a x = x'` and `obsAt a x x' = y` — which is where determinism
enters, and the only place it is needed. Then `lsum_pos_exists` converts
positivity of that sum into existence of a positive term (→), and
`le_lsum_of_mem` converts a positive term back into positivity of the sum
(←). Both directions are genuinely proved; neither is assumed.

## Infrastructure notes

Two `lsum` facts had to be built, both elementary:
`le_lsum_of_mem` (a nonnegative term is below its sum) and
`lsum_pos_exists` (a positive sum of nonnegative terms has a positive term,
by contraposition via `lsum_le_lsum` + `lsum_map_zero`).

Three tactics/modules absent in this dependency-free layer, worth recording
since they recur:

- **`by_contra` is not available.** Use `apply Classical.byContradiction`.
- **`calc` cannot chain `≤`.** `OrdField` does not extend `Preorder`, so
  there is no `Trans LE.le LE.le` instance; the error surfaces as an
  opaque `failed to synthesize Trans` at the *second* step of the chain.
  Use `le_trans` explicitly.
- **`rcases` consumes the hypothesis.** Referencing `hA` after
  `rcases hA with ⟨hn, ho⟩` on the next line is an unknown-identifier error.

## Axioms (`#print axioms`)

```
le_lsum_of_mem      [propext, Quot.sound]
lsum_pos_exists     [propext, Classical.choice, Quot.sound]
obsMass_eq_filter   [propext]
support_identity    [propext, Classical.choice, Quot.sound]
```

`Classical.choice` enters only through `Classical.byContradiction` in
`lsum_pos_exists`. No `sorry`, no `admit`, no axiomatized structure.

---

## Scope: the three consequences

`thm:support` also asserts three consequences. **None is proved here**, and
each is a different kind of gap:

1. `V_k(b) = 1 ⟺ supp(b) ∈ 𝒲_k` — this is `prop:degen`'s content, already
   formalized as `VR` in `P3_Deterministic` (and now also `prop:pl`'s segment
   form via `VR_eq_max_alpha`, v24). It needs the `𝒲_k` viable-set recursion,
   which no module defines.
2. `1 - V_k(b) ≥ min_{x ∈ supp(b)} b(x)` — needs a bridge between
   `SafeMDP`'s `V` (stochastic, `P1_BeliefSafety`) and `DetMDP`'s `VR`
   (adversarial, `P3_Deterministic`). That is a **structural identification,
   not a corollary**, and it is the natural next piece of work.
3. `V_k` non-increasing in `k` — overlaps `prop:freeze` (v18), which proves
   the analogous nesting for the deterministic layer.

So `thm:support` is closed **as to its identity**, which is the part the
theorem is named for and the part its proof argues.

## P3 final tally (18 results)

complete **12** · partial **0** · instance **6** · out of reach **1**
(`prop:probecount`, a counting/lower-bound statement needing machinery none
of these modules carries).

| | |
|---|---|
| complete | `thm:recursion`, `thm:lattice` (i), `thm:support` **(v25)**, `prop:dr` (i), `prop:pathdeficit`, `prop:deficit` (i)(ii)(iii), `prop:degen`, `prop:noisyprobe`, `prop:freeze`, `prop:pl` **(v19, v23, v24)**, `prop:antichain` **(v20–v22)** |

The four-part work order that opened this audit is now **fully discharged**.

## Work order — next

Only open threads remain, none blocking:

1. **The `SafeMDP`/`DetMDP` bridge** — would discharge `thm:support`
   consequence 2 and is the largest genuinely new item available.
2. **`thm:support`'s `𝒲_k` recursion** — needed for consequence 1.
3. **`lean_README_v4.md`** — still stale on `prop:freeze`, `prop:pl`,
   `prop:antichain`; now also needs `thm:support`. Overdue.
4. `prop:pl`'s rationality clause — needs `K := ℚ`.
5. The Sperner count in `prop:antichain` (iii) — a separate combinatorial
   theorem, never claimed.

My recommendation is (3) then (1): the README is small and the audit trail is
not trustworthy while it is wrong, and the bridge is the one item that would
turn two already-proved halves into a stated consequence.

## Commits

| commit | content |
|---|---|
| `0dafd81` | v21 — `prop:antichain` (ii) |
| `8d49013` | v22 — `prop:antichain` (iv) |
| `489cc96` | v23 — `prop:pl` growth law |
| `6e82a52` | v24 — adversarial reading confirmed; `prop:pl` segment form |
| *this turn* | v25 — `P3_Support`: `thm:support` support identity |
