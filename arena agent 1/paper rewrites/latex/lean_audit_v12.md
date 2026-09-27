# Lean audit v12 — P3 batch 3: the deterministic robust regime

**Target:** `general-sustainability` → `lean/`. **Branch:** `lean-audit-v4`
(additive). **Toolchain:** `v4.34.1`.
**Build:** `lake build` → **rc = 0, 20 jobs**, zero warnings, zero `sorry`.

New module **`lean/Formalizations/P3_Deterministic.lean`** (10,804 B),
namespace `Formalizations.P3`.

| Result | Status |
|---|---|
| `prop:degen` | **closed** (survived-mass formula + its `V_k(b)=1` consequence) |
| `prop:deficit` (ii) min-mass | **closed** — `prop:deficit` is now complete |
| `thm:support` | **partial** — min-mass consequence closed; support identity deferred |
| `prop:noisyprobe` | deferred — instance closed form |

---

## What `DetMDP` models

The deterministic degeneration: `x⁺ = F(x,a,d)`, disturbance `d` drawn from
a finite support `univD x a` and read **adversarially** (the paper's robust
operator). Survival under a blind sequence therefore means survival under
*every* disturbance path — which is exactly `List.all` over `univD`.

**A blind sequence is a finite action tuple (`List A`), not `Nat → A`.** At
horizon `k` only the first `k` actions matter and `A` is finite, so the
declared sequential-blind class `Π_B` at horizon `k` is literally
`tuples M k` — a finite list. That is what makes the maximum an ordinary
`lmax` instead of a sup over an infinite function space, and it is what
keeps `prop:degen` inside `OrdField` at all. Worth stating, because the
paper writes `max_{(u_0,…) ∈ Π_B}` without noting that the max is finite.

## `prop:degen`

> $V_k(b) = \max_{(u_0,\dots) \in \Pi_B} \sum_{x \in \mathrm{supp}\,b} b(x)\,\mathbf{1}[x \text{ survives } (u_0,\dots)]$

This appears as the **definition** of `VR`. That is deliberate: the formula
is the paper's *characterization*, and stating it as a theorem about a
separately defined value would be the restatement trap v7 flagged in
itself. The **content** is the consequence the paper draws from it:

**`VR_eq_total_of_jointly_surviving`** — if the support carries a jointly
surviving blind sequence then `V_k(b) = b(𝒱)`, hence `V_k(b) = 1` for a
normalized belief. Proved via `VR_le_totalD` (survived mass never exceeds
total mass) and `le_lmax` (the surviving tuple attains it).

## `prop:deficit` (ii) — the min-mass bound, and `thm:support`'s consequence

> if every declared sequence loses some branch, then
> $\Delta_k(b) \ge \min_{x \in \mathrm{supp}\,b} b(x)$

**`min_mass_bound`.** The engine is a new split lemma:

**`lsum_ind_add_le`** — if `g` is false at `x₀ ∈ l` (with `l` duplicate-free),
then the indicator-weighted sum plus the bare weight at `x₀` is at most the
unweighted total: *the mass on a dead branch is lost*. Formally

    Σ_x f(x)·ind g x  +  f(x₀)  ≤  Σ_x f(x)

This is the exact point where "every sequence loses a branch" turns into a
quantitative deficit, and it is why the bound is the **smallest branch
mass** rather than something weaker.

With it the proof is: for each tuple pick the lost branch `x₀`, get
`smass t b ≤ 1 − b(x₀)`, then `b(x₀) ≥ mn` gives `≤ 1 − mn`, and `lmax_le`
lifts it to `VR`.

Note the duplicate-free requirement (`univX_nodup`) is a real hypothesis —
with duplicates the split lemma is false, since the lost branch's mass
would be charged more than once. The papers enumerate supports as sets and
never say so; the structure has to.

## Honest scope

- **`thm:support`'s support identity**
  `supp(b⁺(·|a,y)) = Post(supp b, a, y)` is **not proved.** It needs (i) a
  disturbance *weighting* to define the posterior mass at all (the robust
  reading has no disturbance distribution), and (ii) a strict-positivity
  lemma for `lsum`: *a finite sum of nonnegative terms is positive iff some
  term is*. Only the min-mass consequence is closed. Flagged, not faked.
- **`prop:noisyprobe`** is a closed form on the declining instance (drifts
  `9/10`, `−11/10`). Its generalizable content is the two-branch Bernoulli
  mixture `V = (1−ε)·v_correct + ε·v_flipped` and the resulting three-level
  range `{0, 1−ε, 1}`; the rest is instance numerics.

## Axiom accounting

```
VR_eq_total_of_jointly_surviving  →  [propext, Classical.choice, Quot.sound]
min_mass_bound                    →  [propext, Classical.choice, Quot.sound]
lsum_ind_add_le                   →  [propext, Classical.choice, Quot.sound]
VR_le_totalD                      →  [propext, Classical.choice, Quot.sound]
```

Choice enters only through `lmax` (finite-list extrema). No `sorry`, no
extra axioms.

## Coverage update (superseding v11)

| Status | Count | Results |
|---|---|---|
| **Formalized (complete)** | **6** | `thm:recursion`, `thm:lattice` (i), `prop:dr` (i), `prop:pathdeficit`, `prop:deficit` (i)+(ii)+(iii), `prop:degen` |
| **Partial** | **4** | `thm:support`, `prop:antichain`, `prop:pl`, `prop:freeze` |
| Formalizable, not done | 1 | `prop:noisyprobe` |
| Instance-level | 6 | `cor:closed`, `thm:parametric`, `thm:agree`, `thm:class`, `prop:learn`, `prop:additivelaw` |
| Not formalizable | 1 | `prop:probecount` (mathematically verified, v10 §3) |

**6 of 18 complete, 4 partial, 1 remaining formalizable.** The formalizable
backlog is now down to `prop:noisyprobe` alone; everything left is either
instance-level (Python's layer) or genuinely beyond `OrdField`.

## Lean-layer gotchas (v12 additions to the v8 list)

- **`List.bind` does not exist in Lean 4.** Use `flatMap`, or — safer, since
  the argument order is easy to get wrong — write the recursion by hand as
  this module does with `tuplesAux`.
- **`le_refl` and `zero_le_one'` are not simp lemmas** in this layer, so
  `simp` leaves goals like `1 ≤ 1` open. Finish them with `exact`.
- **Induction only generalizes the variables that depend on the target.**
  `induction l` in `lsum_ind_add_le` generalizes `hnodup`, `hf`, `hx0` but
  *not* `f`, `g`, `x0`, `hg0` — so the IH takes three arguments, not five.
- **`Trans LE.le LE.le` still absent** (v8): a `calc` cannot chain two
  adjacent `≤`. Bind the first with `have` and use `le_trans`.
