# Lean audit v11 — P3 batch 2: `thm:recursion`, `prop:pathdeficit`, `prop:deficit`

**Target:** `general-sustainability` → `lean/`. **Branch:** `lean-audit-v4`
(additive). **Toolchain:** `v4.34.1`.
**Build:** `lake build` → **rc = 0, 19 jobs**, zero warnings from the new module.

New module **`lean/Formalizations/P3_Sufficiency.lean`** (16,283 B),
namespace `Formalizations.P3`. Closes **3 of the 6** formalizable results
identified in v10 §7 (one of them with 2 of its 3 parts).

| Result | Status |
|---|---|
| `thm:recursion` | **closed** |
| `prop:pathdeficit` | **closed** |
| `prop:deficit` (i) chance-constrained | **closed** |
| `prop:deficit` (iii) monotone deficit | **closed** |
| `prop:deficit` (ii) min-mass | deferred — needs deterministic machinery |
| `prop:degen`, `thm:support` | deferred — same |
| `prop:noisyprobe` | deferred — instance closed form |

---

## `thm:recursion`

The paper's statement, verbatim:

> $V^{\Pi}_{k+1}(b) = \max_{a \in A(\Pi)} \sum_{y} \mathbb{P}(y \mid b,a)\,V^{\Pi}_k(\tau(b,a,y))$

`VAdm` is the same recursion as v8's `V` with the max ranging over
`univA.filter adm` — which is what `A(Π)` is.

Two points of care, both recorded in the module header:

1. **The paper's form is normalized; ours is unnormalized.** `bayes_bridge`
   (v8) is exactly the conversion, so `recursion_normalized` states the
   paper's formula *as written* and derives it. Had I stated only the
   unnormalized recursion it would have been a definition, hence
   content-free — the same trap v7 flagged in itself for `thm:pomdp`.
2. **`VAdm` requires `A(Π) ≠ []`.** The papers never state this; without it
   the maximum is undefined and the recursion is meaningless. Every class
   they use satisfies it, so this is an omission in the statement, not an
   error — but it is a real one, and the formalization has to say it.

Also proved, because the recursion alone is still not enough content:

- **`VAdm_mono_adm`** — enlarging the declared class cannot lower the value.
  This is the *concrete recursion-level* form of v9's abstract
  `class_monotone`, and it is the recursion form of `thm:lattice` (i).
- `VAdm_nonneg`, `VAdm_mono_succ`, `VAdm_antitone`, `VAdm_homogeneous`,
  `VAdm_congr`, `VAdm_bayes_bridge` — the supporting ladder, mirroring v8.

## `prop:pathdeficit`

> $\Delta_1(b) = \sum_x b(x)\,p_x$

`path_deficit` proves this as an **identity** (not a bound) for a single
admissible action: `1 − Σ_y ‖m_{a,y}‖ = exitProb M a b`, given `b(𝒱) = 1`.
The proof is `one_step_eq` + `exit_add_survival` + normalization.

Worth noting because the paper is careful about it and the formalization
should be too: the paper explicitly says the min-mass bound is the special
case `p_x ≡ 1` and is **not universal**, exhibiting a two-state sensor
instance where the deficit `1/20` is strictly below the minimal mass `1/2`.
`path_deficit` is the identity that *grounds* that discussion; it does not
conflate the identity with the bound.

## `prop:deficit`

- **(i)** `deficit_chance`: if every action expends at least `δ` of exit
  mass then `Δ_k(b) ≥ δ` for all `k ≥ 1`. This is v8's `chance_bound`
  (which proved the same fact as `prop:chance`) read as a statement about
  `Δ` rather than `V`.
- **(iii)** `deficit_mono_succ` / `deficit_mono`: the deficit is
  non-decreasing in the horizon, from `V_mono_succ` (v7).

Together with v9's `contam_lower`/`contam_sharp`, this means the
`prop:chance` → `prop:deficit` (i) chain is now fully formalized in both
papers it appears in.

## Axiom accounting

```
recursion_normalized  →  [propext, Classical.choice, Quot.sound]
VAdm_mono_adm         →  [propext, Classical.choice, Quot.sound]
path_deficit          →  [propext, Quot.sound]                 (choice-free)
deficit_chance        →  [propext, Classical.choice, Quot.sound]
deficit_mono_succ     →  [propext, Classical.choice, Quot.sound]
```

`path_deficit` is **choice-free** — it is pure finite-sum algebra plus the
v8 identity `exit_add_survival`, which was already choice-free. Choice in
the others enters only through `lmax`. No `sorry`.

## What is deferred, and exactly what it needs

`prop:degen`, `thm:support` and `prop:deficit` (ii) all live in the
**deterministic robust** regime. They need one shared structure that does
not yet exist:

```
structure DetMDP (K) [OrdField K] (X A D) where
  univX  : List X
  univA  : List A
  univD  : X → A → List D          -- disturbance support, always nonempty
  F      : X → A → D → X           -- deterministic successor
  obs    : X → A → X → Y           -- deterministic observation map
  safe   : X → Prop                -- membership in 𝒱, decidable
```

plus, in order:

1. `survives (u : Nat → A) (x : X) (k : Nat) : Prop` — all disturbance
   paths of length `k` from `x` under the blind sequence `u` stay in `𝒱`;
2. the **survived-mass formula** `V_k(b) = max_u Σ_x b(x)·1[survives u x k]`
   (`prop:degen`), stated as domination + attainment as in v8's
   `V_is_max_over_policies`, since the sequence set is not directly a
   finite `lmax`;
3. the **support identity** `supp(b⁺(·|a,y)) = Post(supp b, a, y)`
   (`thm:support`), which needs the lemma *a finite sum of nonnegative
   terms is positive iff some term is*;
4. the **min-mass bound** (`prop:deficit` (ii), and `thm:support`'s
   consequence): if every declared sequence loses some branch, then
   `Δ_k(b) ≥ min_{x ∈ supp b} b(x)`. Note this one is nearly free
   *given* (2) and a list "erase one element" lemma — and it needs `lmin`,
   which already exists in `P3_ClassLattice`.

`prop:noisyprobe` is a closed form on the declining instance (specific
drifts `9/10`, `−11/10`). Its generalizable content is the two-branch
Bernoulli mixture `V = (1−ε)·v_correct + ε·v_flipped` and the resulting
three-level range `{0, 1−ε, 1}`; the rest is instance numerics.

Cheapest-first order for the next batch: **min-mass bound → survived-mass
formula → support identity → noisy-probe mixture.**

## Coverage update (superseding v10 §5)

| Status | Count | Results |
|---|---|---|
| **Formalized** | **5** | `thm:lattice` (i), `prop:dr` (i), `thm:recursion`, `prop:pathdeficit`, `prop:deficit` (i)+(iii) |
| Formalizable, not done | 4 | `thm:support`, `prop:degen`, `prop:noisyprobe`, `prop:deficit` (ii) |
| Partial | 3 | `prop:antichain`, `prop:pl`, `prop:freeze` |
| Instance-level | 6 | `cor:closed`, `thm:parametric`, `thm:agree`, `thm:class`, `prop:learn`, `prop:additivelaw` |
| Not formalizable | 1 | `prop:probecount` (mathematically verified, v10 §3) |

**5 of 18** results now carry formalized content, up from 2.
