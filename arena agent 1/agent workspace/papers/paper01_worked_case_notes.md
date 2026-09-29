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
