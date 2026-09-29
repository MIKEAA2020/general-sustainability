# Lean audit v9 — P3 structural core (first increment)

**Target:** `general-sustainability` → `lean/`, latest editions.
**Branch:** `lean-audit-v4` (additive). **Toolchain:** `v4.34.1`.
**Build:** `lake build` → **rc = 0, 18 jobs**, zero warnings from any new module.

This is the first increment on the work order's item (2), **P3's structural
core**. v8 (previous batch) closed all three `thm:pomdp` gaps.

---

## 1. The ratio, confirmed and explained

`paper2_probabilistic_sufficiency_v11.tex` states **18 named results**.
`Formalizations/P3_ProbSufficiency.lean` (4,408 B) contains **4 theorems**:
`Φ_mono`, `Φ_const`, `Φ_le_const`, `iterΦ_mono`.

The ratio is worse than 18:4, and it is worth saying why: **none of the 4 is
any of the 18.** They are generic monotonicity lemmas for an abstract kernel
`Φ`, stated over arbitrary `B`, `Y`. They are true and they are reusable,
but they are not attached to a single numbered claim in the paper — so the
module currently certifies *machinery*, not *results*. That is the honest
diagnosis behind the "worst ratio in the repo" observation, and it is a
different (and more fixable) problem than "the paper is wrong".

## 2. Triage of all 18 results

Screened against what `OrdField` can express: finite sums, order, field
algebra. **No** completeness, topology, measure, `exp`/`log`, sup/inf over
infinite sets, or derivatives.

| Result | Verdict | Note |
|---|---|---|
| `thm:recursion` | **feasible** | Near-duplicate of `thm:pomdp`; machinery now exists |
| `thm:support` | **feasible** | Support identity; finite sets as lists/predicates |
| `prop:antichain` | **partial** | (i) `V_k(b)=max_{S∈S_k} b(S)` feasible; (ii) alpha-vector characterisation harder |
| `cor:closed` | instance | Closed form on the delayed class |
| `thm:parametric` | instance | Piecewise closed form, delayed instance |
| `prop:pl` | **partial** | Max-of-finitely-many-linear-functionals feasible; convexity over `OrdField` delicate |
| `prop:degen` | **feasible** | Survived-mass formula, finite sums with indicators |
| `prop:freeze` | **partial** | Nesting + non-increasing feasible; the `2^{|supp b|}` bound needs a counting argument |
| `prop:deficit` | **feasible** | Overlaps `prop:chance`, already proved in v8 |
| `thm:agree` | instance/grid | 48-cell certificate–value agreement — Python's job |
| **`thm:lattice`** | **DONE (i)** | This batch |
| `thm:class` | instance | Needs the delayed instance formalised |
| `prop:learn` | instance/grid | Quantized control; numerical |
| `prop:pathdeficit` | **feasible** | Near-free from v8's `exit_add_survival` |
| `prop:noisyprobe` | **feasible** | Finite algebra, indicators |
| **`prop:dr` (i)** | **DONE** | This batch |
| `prop:probecount` | **infeasible** | Needs `exp`/`log` and a Chernoff bound |
| `prop:additivelaw` | instance | Needs the additive-drift dynamics |

Chosen for this batch: `thm:lattice` and `prop:dr`. Both are
*load-bearing* (other results route through them), *checkable* (`prop:dr`
(i) is a finite linear-programming identity of exactly the kind that is easy
to state slightly wrong), and free of instance-specific dynamics.

## 3. What was formalized

New module **`lean/Formalizations/P3_ClassLattice.lean`** (9,959 B,
9 declarations), namespace `Formalizations.P3`.

### `thm:lattice` (i) — class monotonicity

> `Π ⊆ Π'  ⟹  V^Π_k(b) ≤ V^Π'_k(b)`

`class_monotone` proves this. The statement is deliberately abstract: each
class value is required only to *dominate every policy in its class and be
attained by one* — i.e. to be the maximum over that class, the property
`V_is_max_over_policies` (v8) establishes for the unrestricted class. The
proof then shows precisely which hypothesis does the work: **attainment on
the left, domination on the right.**

This matters because the paper states the result as obvious. It is not
obvious — it is exactly the statement that enlarging an admissible set cannot
lower a maximum, and it only becomes trivial once the value is known to be a
max over policies, which is the thing the paper cites rather than proves.
So `thm:lattice` (i) and v8's `thm:pomdp` (c) are the same result viewed
from two ends, and neither is content-free.

`class_le_unrestricted`: any class of in-universe policies is dominated by
the unrestricted value — the top of `thm:lattice`'s chain
`V^hold ≤ V^ol = V^seq,blind ≤ V^obs`.

### `prop:dr` (i) — contamination interpolation

> `inf_{q ∈ D_ρ} Σ_y q(y)·v_y = (1-ρ)·Σ_y p(y)·v_y + ρ·min_y v_y`

`OrdField` has no completeness, so **`inf` over a set of distributions is
not expressible and is not asserted.** The claim is split into the two
halves that are what "the inf is a minimum" actually means:

- `contam_lower` — every admissible adversary is bounded below by
  `(1-ρ)·E_p[v] + ρ·min_y v`;
- `contam_sharp` — equality holds for an adversary concentrating the whole
  contamination on a minimizer of `v`.

Supporting: `lmin` (finite minima via negation of `lmax`), `lmin_le`,
`le_lmin`, `lmin_mem`, `Contam`.

**One observation the formalization surfaced:** the inequality does *not*
need `ρ ≤ 1`. The bound is a pure consequence of `ρ ≥ 0` and `w'` summing
to one; `ρ ≤ 1` is needed only so that `w` is a genuine weight function. The
paper bundles the two conditions without distinguishing them.

## 4. Axiom accounting

```
class_monotone         →  (no axioms at all)
class_le_unrestricted  →  [propext, Classical.choice, Quot.sound]
contam_lower           →  [propext, Classical.choice, Quot.sound]
contam_sharp           →  [propext, Classical.choice]
```

`class_monotone` is **axiom-free** — a genuine payoff of stating it
abstractly: it is pure first-order reasoning about maxima, with no choice
and no quotienting. Choice in the others enters only through `lmax`/`lmin`
(finite-list extrema). No `sorry`.

## 5. Honest gaps in this batch

- **`prop:dr` sharpness is conditional.** `contam_sharp` assumes `w'` is a
  point mass rather than constructing one; constructing a normalized point
  mass needs a Kronecker-delta sum over a duplicate-free list. Flagged, not
  faked — the alternative would have been an unused-parameter "theorem" of
  the kind this audit exists to remove.
- **`thm:lattice` (ii) — the chain `V^ol = V^seq,blind`** is not proved. The
  paper justifies the middle equality with "no observation arrives inside
  the window". Plausible, but it needs the two classes defined concretely
  first; the abstract `class_monotone` gives `≤` in both directions only if
  both inclusions hold.
- Everything instance-specific (`cor:closed`, `thm:parametric`,
  `thm:class`, `prop:learn`, `prop:additivelaw`, `thm:agree`) is untouched:
  it needs the delayed-instance dynamics formalized before the closed forms
  mean anything.

## 6. Suggested next batches, cheapest first

1. `prop:pathdeficit` + `prop:deficit` — near-free: both are
   `exit_add_survival` (v8) plus a one-step unpacking.
2. `thm:recursion` — re-run the v8 policy machinery with a class-admissible
   action set; mostly assembly.
3. `prop:freeze` — the nesting `S_{ℓ+1} ⊆ S_ℓ` and the `2^{|supp b|}`
   bound; needs families-of-subsets as lists plus a counting lemma.
4. `prop:dr` sharpness, unconditional — the Kronecker-delta sum lemma.
5. Instance dynamics for the delayed example → the remaining closed forms.

`prop:probecount` should be **declared out of scope** and the paper should
say so: it is a Chernoff bound, and no `OrdField`-level formalization of it
exists or will.
