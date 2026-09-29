# Lean audit v8 — closing the three `thm:pomdp` gaps

**Target:** `general-sustainability` → `lean/`, latest editions.
**Branch:** `lean-audit-v4` (additive). **Toolchain:** `v4.34.1`.
**Build:** `lake build` → **rc = 0, 17 jobs**, zero warnings from any of the
three POMDP modules.

v7 formalized `thm:pomdp` and left three gaps open (v7 §3.1, §3.2, §3.3).
**This batch closes all three.** Files added:

| Module | Bytes | Decl. | Closes |
|---|---|---|---|
| `lean/Formalizations/P1_BeliefSafety.lean` | 11,418 | 19 | v7 baseline |
| `lean/Formalizations/P1_BeliefSafety_Value.lean` | 15,303 | 21 | **(a)** and **(b)** |
| `lean/Formalizations/P1_BeliefSafety_Policy.lean` | 6,228 | 7 | **(c)** |

---

## (a) The homogeneity bridge — v7 §3.2 CLOSED

The paper uses normalized beliefs and Bayes' rule; v7 used unnormalized
sub-probability masses to dodge the division by $\mathbb{P}(y\mid b,a)$. The
bridge is now proved in two steps.

**`V_homogeneous`** — $V_k$ is positively homogeneous of degree one:

$$V_k(c \cdot m) = c \cdot V_k(m) \qquad (c \ge 0)$$

**`bayes_bridge`** — summand by summand,

$$\mathbb{P}(y \mid b,a)\ \cdot\ V_k\bigl(\tau(b,a,y)\bigr) \;=\; V_k(m_{a,y}),$$

where $\mathbb{P}(y\mid b,a)$ is the total mass of the unnormalized
posterior $m_{a,y}$ and $\tau(b,a,y) = \mathbb{P}(y\mid b,a)^{-1}\cdot m_{a,y}$.

**The $\mathbb{P}(y\mid b,a) = 0$ case is the whole point.** The paper's
`τ` is undefined on impossible observations, so the paper drops those terms
silently. Here the term is *provably* zero (`V_of_total_zero`: a mass of
total weight zero has safety value zero at every horizon) rather than absent
by fiat. This is a case where the formalization is strictly more careful
than the source.

## (b) `prop:chance` — v7 §3.3 CLOSED

**`one_step_eq`** — the *equality* form of the one-step bound, which v7 had
only as an inequality:

$$\sum_y \lVert m_{a,y}\rVert \;=\; \sum_x m(x)\!\!\sum_{x'}\! T(a,x,x')$$

**`V_antitone`** — $k \le n \Rightarrow V_n \le V_k$. This is the
horizon-antitonicity lift of v7's $V_{k+1}\le V_k$; `prop:chance` needs the
$k$-to-$1$ form, not just the one-step form.

**`chance_bound`** — `prop:chance` itself. If $b$ is normalized
($b(\mathcal{V}) = 1$) and every action expends at least $\delta$ of exit
mass, $\sum_x b(x)\,p(x,a) \ge \delta$, then $V_k(b) \le 1 - \delta$ for all
$k \ge 1$.

Supporting: `rowSum`, `exitProb`, `survival`, and
`exit_add_survival : survival + exitProb = total` (the paper's
$p(x,a) = 1 - \sum_{x'} T(x'\mid x,a)$, where the exit convention is
*derived*, not stipulated).

Note the proof now carries the quantitative step the paper compresses: the
paper says "the one-step survival probability is $1 - \sum_x b(x)p(x,a) \le
1-\delta$" in one line; `chance_bound` derives it from `one_step_eq` +
`exit_add_survival` + `V_antitone`.

## (c) Max over policies — v7 §3.1 CLOSED

In v7, `V` was *defined* by the recursion, so `thm:pomdp`'s recursion
identity was `rfl` — content-free. The paper instead defines
$V_k(b) = \max_\pi \mathbb{P}_\pi(\text{survive } k)$ over **policies** and
derives the recursion. That derivation is the real content, and the paper
discharges it with "standard value iteration" plus a citation to
Smallwood–Sondik.

Now defined: `Pol` (deterministic observation-feedback policies), `J`
(policy value), `PolIn` (policies whose actions lie in the finite universe
`univA` — needed because `A` is a type, not a finite type, so `Pol` admits
out-of-universe actions that `V`'s `max` never ranges over).

**`V_is_max_over_policies`** — for every $k$ and $m$:

- `J_dominated`: every in-universe policy satisfies $J_k(\pi,m) \le V_k(m)$;
- `V_attained`: some in-universe policy attains $J_k(\pi,m) = V_k(m)$.

So $V_k(m) = \max_\pi J_k(\pi,m)$ — the interchange of `max` over actions
with the sum over observations, proved rather than cited. **This is no
longer a restatement of a definition**, which was the specific defect v7
flagged in itself.

Two modelling notes recorded in the module header: `Pol` carries a `stop`
leaf (Lean has no coinduction here; `stop` is given value $0$ at horizons
$k\ge 1$ so it is never optimal, and at $k=0$ the policy is not consulted),
and `PolIn` is what makes "$\max_\pi$" well-scoped.

## Axiom accounting

```
one_step_le_total   →  [propext, Quot.sound]                  (v7, choice-free)
V_zero              →  [propext, Classical.choice]
V_nonneg            →  [propext, Classical.choice, Quot.sound]
V_mono_succ         →  [propext, Classical.choice, Quot.sound]
bayes_bridge        →  [propext, Classical.choice, Quot.sound]
V_homogeneous       →  [propext, Classical.choice, Quot.sound]
chance_bound        →  [propext, Classical.choice, Quot.sound]
J_dominated         →  [propext, Classical.choice, Quot.sound]
V_attained          →  [propext, Classical.choice, Quot.sound]
```

`Classical.choice` enters only through `lmax` (selecting a maximum of a
finite list) and, in `V_attained`, through choosing an optimal policy tree.
Neither is used to prove an inequality. `propext`/`Quot.sound` are inherited
from `Prelude`'s list reasoning. No `sorry`.

## What remains (2 gaps, both interfaces to probability theory)

1. `J_k(\pi,b)` is the *recursive* value of a policy; that it equals the
   paper's $\mathbb{P}_\pi(x_0,\dots,x_k \in \mathcal{V}\mid b)$ needs a
   probability space over disturbance sequences — not expressible over
   `OrdField`.
2. Likewise the identification of `V_0(m)` with a belief's mass $b(\mathcal{V})$
   is stipulative here, not measure-theoretic.

Both are *interfaces to probability theory*, not gaps in the
dynamic-programming argument. The part the paper elided by citation is now
proved.

## Lean-layer gotchas (for future batches)

These cost real debug cycles; recorded so they are not re-learnt.

- **No `Trans LE.le LE.le` instance.** A `calc` chain cannot have two
  adjacent `≤` steps. Split into a `have` + `le_trans`.
- **`Mass.ext` does not exist** (its `nonneg` field is proof-valued, so two
  masses with equal `.f` are equal but not definitionally so). Route
  around it with `V_congr`, which is also the honest statement: `V` is a
  function of the mass function only.
- **`one_mul'` (with the prime), not `one_mul`**; `mul_one` is unprimed.
- **`inv_zero` is `OrdField.inv_zero`**, and `rw [h, OrdField.inv_zero]`
  fails — after `rw [h]` the occurrence is gone. Use a `calc` with
  `congrArg (fun t : K => t⁻¹) h`.
- **`congr 1` sometimes closes the goal entirely**, so a following
  `exact h` errors with "no goals to be solved". Use explicit `congrArg`
  when a rewrite would hit a dependent position (e.g. a proof argument
  whose type mentions the term being rewritten).
- **`ring`/`ring_nf` are unavailable**; do algebra by hand with `mul_assoc`,
  `left_distrib`, `sub_add_cancel`, `add_sub_cancel`.
- `lsum_*`, `le_refl`, `add_le_add_left/right` live in the `Formalizations`
  namespace (via `open Formalizations`).
