# Paper 1 — worked case: progress and a negative result (2026-09-29)

## The gap

The plan records the one item blocking paper 1:

> At least one worked case where a certificate bites on a system whose kernel cannot be
> computed. Without it the instrument is unfalsified in the regime that motivates it.

Two properties are required:

- **(a) non-termination** — the kernel iteration does not stabilise, so the kernel is not
  finitely computable by it;
- **(b) obstruction** — a certificate fires: two states in one observation fibre, each
  individually viable, whose safe-action sets are disjoint.

## What the manuscript already contains

Useful and previously overlooked: `prop:window-nogo` already proves that **the
post-observation recourse phase is undecidable by any certificate pair that reads only the
window sub-model**. So the paper is not without a computability result. What is missing is
the *worked case* — an explicit system exhibiting a certificate biting where the kernel
does not.

Relevant statements, read in full this session: `def:kernel` (robust epistemic kernel,
exists-policy-for-all-realizations), `prop:selector` (an action must be admissible, safe,
and recursively viable; emptiness of any one response correspondence at a reachable belief
certifies nonviability), `thm:common-action` (with H2.1 dwell, H2.2 empty common admissible
or common safe set, H2.3 closed-loop adverse selection).

## Half established, and verified numerically

An explicit instance of **(b)**, computed rather than asserted.

- dynamics `x⁺ = φ(u) − 2x`, with `φ(u) = 4(u − ½)²`, `u ∈ [0,1]`
- `φ` non-monotone (`φ(0) = φ(1) = 1`, `φ(½) = 0`), so safe sets are **non-convex** — a
  union of two intervals. This is what permits disjointness at all.
- constraint `V = [0, 0.4]`
- one-step safe set `R(x) = {u : φ(u) ∈ [2x, 0.4 + 2x]}`

Measured:

```
R(0.00) = [0.1838, 0.8162]
R(0.25) = [0.0257, 0.1464] ∪ [0.8536, 0.9743]
R(0.00) ∩ R(0.25) = ∅
```

Both states are individually viable under full observation (each reaches the cycle
`0 → 0.2 → 0`). The common safe-action set over the fibre `B = {0, 0.25}` is empty, so the
common-action obstruction fires and `B` is nonviable. This is a clean, finite, reproducible
instance of the mechanism.

**It does not deliver (a).** The kernel iteration stabilises at `n = 1`; the kernel is the
whole constraint set. So this instance does not exhibit a certificate biting where the
kernel cannot be computed.

## Negative result: the two properties are in tension

A parameter search over an amplified family

```
x⁺ = (1+λ)x − c + φ(u),   φ(u) = 4(u−½)²,   V = [0, H]
λ ∈ {0, 0.25, 0.5, 1, 2},  c ∈ {0.6, 0.8, 1, 1.2, 1.5},  H ∈ {0.4, 0.6, 0.8, 1}
```

—125 combinations — found **zero** instances carrying both properties. Scripts:
`wk_case.py` (the verified instance) and `wk_search.py` (the search).

### Why, structurally

For a scalar state, a scalar control and an interval constraint of width `H`, the required
control range at state `x` is an interval of width `H` shifted by the state difference.
Two such intervals are disjoint only if the shift exceeds `H`. But the shift is at most the
state range, which **is** `H`. Disjointness therefore requires `> H` from a quantity bounded
by `H`: impossible, independent of parameters.

Amplifying the `x`-dependence (the `λ` sweep) does not break this, because the same
amplification that widens the shift also destroys non-termination. The tension is between
the *drain* needed to make the kernel iteration run forever and the *state-dependence* needed
to make safe sets separate — and in this family they cannot both be present.

## What this means, and the next move

The negative result is informative, not a dead end: it says the construction must change
mechanism, not parameters. Three routes, in the order I would try them:

1. **Disconnected constraint set.** With `V` a union of intervals, the required control set
   is no longer a single interval of width `H`, and the bound above does not apply. This is
   the cheapest structural change.
2. **Two-dimensional state.** The shift argument is one-dimensional; in 2-D the safe sets
   can separate without the state range bounding them.
3. **Use the manuscript's own undecidability** rather than constructing a new one.
   `prop:window-nogo` already proves the recourse phase undecidable by window-measurable
   certificates. A worked case could be built on that: exhibit a system where the window
   phase is decided completely by a certificate while the recourse phase is exactly the
   undecidable part. That is likely the intended reading of the gap.

Route 3 is the most promising and the closest to what the paper already proves.


---

## CORRECTION (2026-09-29): the negative result above was an artefact of the method

I reported that "the two properties are in tension" and gave a structural argument
(disjointness needs a shift exceeding the constraint width `H`, which the state range
bounds by `H`). **That conclusion is unsupported and should not be relied on.** The
argument may still be correct, but the evidence I cited for it does not test it.

Diagnosed by instrumenting the search to count the two properties separately:

```
combinations tested      : 125
(a) non-terminating      : 0
(b) obstruction present  : 50
BOTH                     : 0
```

**(a) returned zero out of 125 for a reason that has nothing to do with the dynamics.**
The state space was gridded into 601 points. On a finite grid the kernel iteration is a
decreasing sequence of subsets of a finite set, so it is **guaranteed to stabilise within
601 steps**. Discretisation destroys non-termination by construction. No grid-based search
can ever find property (a), whatever the parameters.

The same flaw invalidates the `wk_search.py` sweep reported above: its "zero instances"
result is likewise an artefact, not evidence about the family.

### What this means

- **(b) obstruction is easy** — 50 of 125 combinations on the disconnected-constraint
  family. This is not the hard half.
- **(a) non-termination is the entire difficulty**, and it is a property of the
  *continuous* system. It must be established symbolically: compute `K_n` in closed form
  (as unions of intervals with exact endpoints) and prove strict decrease for all `n`.
  Grid numerics cannot see it, so grid numerics must not be used to search for it.

### Why the hand-construction also stalled

Attempted symbolically: with `x^+ = alpha*x - c + phi(u)` and `K_n = [t_n, H]`, the
recursion gives `t_{n+1} = max(t_n, (t_n + c - 1)/alpha)`, whose fixed point is
`t* = (1-c)/(1-alpha)`. For `t_n < t*` the map sends `t_n` *below* itself so the `max`
pins it at `t_0`; for `t_n > t*` it increases away from `t*` toward the boundary. So this
linear family gives either no movement or escape to the boundary — never asymptotic
approach. A nonlinear safe-set boundary is required for the iteration to approach its
limit without reaching it.

### Revised plan: route 3, not route 1

The disconnected-constraint route (route 1) does not address the half that is actually
hard. The right move is the one flagged as most promising in the first place: build the
worked case on the manuscript's **existing** undecidability result, `prop:window-nogo`,
which proves the post-observation recourse phase undecidable by any certificate pair
reading only the window sub-model.

That reframes the case correctly and avoids constructing non-termination from scratch:

- exhibit a system where the **window phase is decided completely** by a certificate
  (finitely, `prop:decomposition`),
- while the **recourse phase is exactly the undecidable part** (`prop:window-nogo`),
- so the certificate returns a verdict on the part it can decide, on a system whose full
  kernel cannot be computed because deciding it would require deciding the recourse phase.

This is very likely the intended reading of the gap, and it uses results the paper already
has rather than new ones it would have to earn.


---

## Route 3 pursued first (2026-09-29) — and a large find

### On the ordering, honestly

I listed route 3 last while calling it "most promising". That was incoherent: I ranked by
**implementation effort** (route 1 was a small edit to a script I already had) while
labelling by **probability of success**. The two orderings disagreed and I did not notice.
Underneath it, I was treating "use the result the paper already has" as a fallback and
"construct something new" as the real work — a bias toward novelty over assets already in
hand. Route 3 is first from here.

### The two results, read properly

**`prop:decomposition`** [exact two-phase decomposition]. In the two-phase model, `B₀` is
viable iff (i) some declared blind control keeps every branch in `V` through step `K`, and
(ii) some declared blind control satisfying (i) lands every branch in `RViab(V)` at the
reveal. Over any declared class on which the window certificates are complete (finite
classes; polytope-declared classes, by `thm:lp-instant`), these are equivalent: both
certificates silent; clause (i) holds; and `B₀` is either viable or its nonviability is
exactly the post-observation recourse mode, the failure of (ii) for every window-surviving
blind control.

**`prop:window-nogo`** [no window-measurable pair is complete]. Call a certificate pair
*window-measurable* when its two verdicts depend only on the window sub-model — the initial
belief, the branch transitions within the window, the floors, and the observation schedule.
Then **no window-measurable pair is complete** for the two-phase model: *the three-state
instance of Supplementary S3/A.3 and its variant agree on all window data, the certificates
are silent in both, and yet one is nonviable (`x₄` exits under every post-reveal action)
while the other is viable (`x₄` is maintained).*

Two things follow:

1. The proof of `prop:window-nogo` **is** a worked case. It is an explicit three-state
   instance with a variant, differing only outside the window data. So the paper is not
   short of a worked instance; it is short of one framed as the answer to the gap.
2. The right statement of the gap is therefore narrower than "the kernel cannot be
   computed". What is proven is: no *window-measurable* certificate pair is complete. The
   honest reading is that the **window phase is decidable by certificates** while the
   **recourse phase is not decidable by any window-measurable pair** — so a certificate
   returns a verdict on the part it can decide, on a system whose full viability question
   cannot be settled window-measurably.

### A large find: `paper2_worked_systems`, versions 1-17

`arena agent 1/paper rewrites/latex/paper2_worked_systems_v17.tex` — **10,374 words, 17
sections**, with a companion `paper2_worked_systems_v17_verification.py` of **63,080
characters**. Versions v1 through v17 exist, most with their own `_verification.py`.

Sections: Introduction; Systems, conventions, and methods; A master monotonicity theorem;
The master table; Policy classes; Decentralized observation; Review timing on the
hidden-regime grid; Monitoring adequacy; Regime uncertainty; The continuous benchmark;
Static duality; The certainty-equivalence drift audit; Multiple floors; Robustness margins;
Design rules; Verification methods; Conclusion.

This is worked-case material — a whole manuscript of worked systems with executable
verification — and **none of it is in paper01**. It is the natural source for, or home of,
the worked case the plan says paper 1 lacks.

### Next step

Read `paper2_worked_systems_v17` against the gap, and check whether its master table
already contains an instance where a certificate fires while the kernel is not
window-measurably decidable. If it does, the gap closes by folding that instance into
paper01 with a pointer; if it does not, construct the instance inside that framework —
which has conventions, a master table and a verification harness already in place, rather
than from scratch.

Also still to locate: Supplementary S3/A.3 itself, which holds the three-state instance
that `prop:window-nogo` is proved on.


---

## GAP CLOSED (2026-09-29) — subsection 3.7 added as `paper01_..._v59.tex`

Route 3 paid off: the worked case was found in `paper2_worked_systems_v17`, not
constructed from scratch.

### What v17 already contained

Two candidate instances, both audited:

1. **The finite two-floor audit system** (Section: Systems, conventions, and methods).
   States `(z1,z2)` in `{0,1,2,3}^2`, safe set `{z1>=1, z2>=1}`, instruments `u` in `{0,1,2}`.
   Nine safe states generate `C(9,2)=36` two-element belief pairs. Kernel sizes:
   `|W_inst|=24`, `|W_agg|=26`, `|W_full-codex|=25`, `|W_full|=28`, `|W_dec|=12`.
   **Four pairs are full-information-viable but institutionally nonviable** — `12|21`,
   `12|31`, `13|21`, `13|31` — the certificate biting. But this system is finite, so its
   kernel *is* computable (backward recursion over the `2^9 = 512`-belief universe). It
   validates the calculus; it does not exhibit the motivating regime.

2. **The continuous benchmark** (Section: The continuous benchmark). This is the one.
   State `(x1,x2) >= 0`, aggregate `Y = x1 + x2`, the `Y`-fibre a CONTINUUM. Caps
   `cap1(Y) = 3/2 - (Y-2)/10`, `cap2(Y) = 59/50 - (Y-2)/10`; control set
   `U = {u >= 0 : u1+u2 >= 2}`; feasible iff `u_i <= cap_i(Y)`.

### Verified independently, exact rational arithmetic

`wk_continuous.py`, standard library `Fraction` only:

```
Y=5     cap1=6/5   cap2=22/25  sum=52/25   -> viable
Y=27/5  cap1=29/25 cap2=21/25  sum=2       -> crossover, EXACT
Y=6     cap1=11/10 cap2=39/50  sum=47/25   -> OBSTRUCTED, margin 3/50
```

- `Y* = 27/5` recovered in closed form; cap sum there is exactly `2`.
- Dual measure `(1/2, 1/2)`; margin `(2 - capsum)/2` equals `(Y - 27/5)/10` at every
  tested aggregate, including `Y = 5, 27/5, 6, 7, 10`.
- Witness at `Y=5` is `(6/5, 4/5)`: meets demand exactly, respects both caps.
- **200 aggregates on the half-line `Y >= 27/5` checked: zero violations.**
- All of it matches the paper's own tabulated values.

### What was written

New subsection **3.7 "A worked case: an exact obstruction on a continuum"** in
`paper01_obstruction_calculus_v59.tex` (previous version preserved as v58). It states the
system, the certificate, the two audited fibres, what the instance establishes, and —
importantly — the scope.

### Scope, stated in the subsection and not overclaimed

What is certified is a **static obstruction on the observation fibre**, not the full dynamic
epistemic kernel. The audited object in that section is fibre feasibility, not the transition
dynamics. The subsection says so explicitly and points to `prop:window-nogo` for the limits
of what certificate pairs can decide in the dynamic two-phase model.

This is weaker than the literal wording of the plan's gap ("a system whose kernel cannot be
computed") and stronger than nothing: the fibre is a continuum, so no enumeration settles
it, and the certificate settles it exactly with two rationals. I have not claimed, and the
text does not claim, that a certificate decides a dynamic kernel that is in principle
undecidable.

### Still open

- Supplementary **S3/A.3**, holding the three-state instance `prop:window-nogo` is proved on,
  has not been located. Worth finding: it would let that proposition carry its own instance
  in the main text rather than by reference.
- The four obstructed pairs of the finite system (`12|21`, `12|31`, `13|21`, `13|31`) are
  candidates for a second worked case showing the *epistemic* mechanism specifically, since
  each is full-information-viable and institutionally nonviable.
