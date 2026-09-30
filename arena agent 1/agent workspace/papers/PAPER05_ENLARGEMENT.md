# Paper 5 — instance enlargement to five parameters — 2026-09-30

`PAPER05_SCOPE_AND_PRIOR_ART.md` closed with the residual risk that paper 5, at 5,067 words
on a four-parameter cube, "may not clear the bar on novelty no matter how carefully framed",
and named the strongest available move: **extend the census to a larger instance (five or six
parameters), where the cost figures would say something new about the feasibility frontier of
exact computation.** That move is now taken.

Version: v13 → **v14**. Words: 5,067 → **6,435**. Pages: 6 → 7. Zero errors, zero undefined
references.

## Method: the model was validated against the published paper before being extended

The instance was reimplemented from the paper's own definitions, and every computed figure
was checked against the numbers the paper already publishes. Three independent matches:

| check | paper 5 states | reimplementation |
|---|---|---|
| m=4 drift by Hamming distance | +0.3, −0.1, −0.5, −0.9, −1.3; hold −0.5 | identical |
| m=4 antichain census | 16 at the edge, 32 per level above → **496** | **496** (16 / 32 / 32 …) |
| m=4 four-step PBVI dedup | 17⁴ = 83,521 → at most **545**; single vector at top-level one-step | **545**; **1** vector |
| m=4 census stability | — | identical at state caps 20, 30, 40 |

Only after reproducing 496 and 545 exactly was the model extended to m = 5.

## Drift law and the two scaling thresholds

From `d(u,θ) = −1/2 + (1/5)⟨u,θ⟩` and `⟨u,θ⟩ = m − 2·dist(u,θ)`, the drift in tenths is

```
D(h) = −5 + 2m − 4h        hold action: −5
```

**Pair-sum threshold** (generalising Lemma `lem:pairsum`): a blind policy keeps a pair at
Hamming distance `h` alive only if `h ≤ m − 5/2`, i.e. `h ≤ m − 3` for integer h.

| m | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|
| max viable `h` | 0 | **1** | **2** | **3** | **4** |

m = 4 reproduces the paper's Hamming-adjacency result exactly.

**Ball threshold**: the radius-`r` Hamming ball around `v` is self-sustaining under the
constant matched action `u = v` iff `D(r) ≥ 0`, i.e. `r ≤ (2m−5)/4`. This independently
reproduces `r*(m) = ⌊(2m−5)/4⌋` of the paper's existing Remark `rem:scope`
(`r*(4)=0, r*(5)=r*(6)=1, r*(7)=r*(8)=2`). The qualitative change at m = 5: a cell at
distance 1 now **rises** (+0.1) where at m = 4 it fell (−0.1).

## The complete m = 5 classification (new)

Solved as a **safety game**: greatest fixed point of the controllable-predecessor operator on
the capped non-negative orthant, exact integer arithmetic. (An averaging bound is not
sufficient — see below.)

- **32 cells**, 16 stock levels → 512 augmented cells; **33 actions**.
- The pairwise-necessary graph (edges at distance ≤ 2) has **192 maximal cliques**: 32 of
  size 6, 160 of size 4.
- **Size 6**: the 32 maximal cliques are exactly the radius-1 balls. Under `u = v` the centre
  receives +5 and each of the five neighbours +1 — all strictly positive — so all 32 survive
  from the floor's edge, `L = 0` included.
- **Size 4**: the 160 cliques fall into exactly **2 orbits** under the 3,840-element
  automorphism group (XOR by any cell, then any permutation of coordinates), 80 each:
  - *tetrahedral* orbit (all six pairwise distances = 2): **not survivable at any level**;
  - orbit with distance multiset {1,1,1,1,2,2}: **survivable exactly from L ≥ 3**, i.e.
    z₀ ≥ 1.3.
- Both verdicts stable under increasing the state cap from 16 to 40.
- All **912** cliques of size ≤ 3 lie inside some radius-1 ball → none maximal.

**Maximal blind-survivable sets**: 32 per level at z₀ ∈ {1.0, 1.1, 1.2}; **112** per level
(32 + 80) from z₀ ≥ 1.3.

### The pairwise instrument is necessary but no longer sufficient

At m = 4 the pair-sum bound is sharp: it excludes every pair at distance ≥ 2, and everything
it permits is survivable. **At m = 5 it is not.** The tetrahedral orbit has all six pairwise
distances equal to 2, meeting `h ≤ 2` with equality, and no blind policy of any period keeps
it above the floor. The paper's existing `rem:crude` records this failure for the *crude*
averaging instrument at m = 4; the new `rem:notsuff` records that the *sharper* pairwise
instrument inherits the failure one dimension later. Consequently the m = 5 classification
cannot be recovered from pairwise data alone — it needs the safety game.

## The census and the feasibility frontier (the headline)

| | m = 4 | m = 5 | growth |
|---|---|---|---|
| cells | 16 | 32 | 2× |
| augmented cells | 256 | 512 | 2× |
| actions | 17 | 33 | 1.94× |
| raw subset lattice | 16 × 2¹⁶ = 1,048,576 | 16 × 2³² = **68,719,476,736** | **65,536×** |
| stored antichain | **496** | **1,552** (3×32 + 13×112) | **3.13×** |
| overall compression | ≈ 2,114× | **≈ 4.43 × 10⁷** (2³²/97) | **≈ 2.1 × 10⁴×** |
| four-step α-set | 17⁴ = 83,521 → 545 | 33⁴ = **1,185,921** → **11,145** | 14.2× raw, 20.4× dedup |

Per-level compression at m = 5: `2³²/32 = 134,217,728×` at z₀ ≤ 1.2;
`2³²/112 ≈ 3.83 × 10⁷` above it.

**The object one must not store grows exponentially; the object one must store grows by a
factor a little over three.** That is the feasibility-frontier statement the earlier scope
note said was missing.

## What is deliberately left open

`r*(6) = 1`, so the 64 seven-cell radius-1 balls of the six-cube are blind-survivable by the
same argument. Whether they are **maximal** is not settled: the distance-≤3 graph at m = 6
has 10,752 maximal cliques with maximum clique size **12**, against the ball's 7, and
resolving their survivability needs a safety game in 12 dimensions. This is stated in the
paper as open rather than papered over.

## Reproducibility

`/home/user/p5/ebc_solver.py` — the exact solver (safety game, drift law, candidate graph).
Validated by reproducing 496 and 545 at m = 4 before extension.
