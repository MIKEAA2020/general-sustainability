# Lean audit — v36

Branch `lean-audit-v4`. Parent `cf7f290` (v35). Range covered here:
`6649788` → `16bc104`.

```
ceedb65  EBC_Pairs      — mismatched play, the −1/10, the dip
737beed  EBC_Pairs_v2   — pair survives from z₀ ≥ 1.1
74298ff  EBC_Pairs_v3   — necessity: fails below 1.1
16bc104  EBC_Classification — nothing larger, at the floor
6649788  EBC_Bands      — matched-play machinery (v35 carry-over)
17d72dd  RatArith, EBC_Bands_v2 — the helper; singleton clause
```

Build: `lake build` → **rc = 0, 55 jobs** (49 imported modules). Zero
warnings, zero `sorry`, zero axioms.

---

## 1. Directive: build the shared arithmetic helper first

Honoured, and it changed the economics of the whole proposition.

The layer has no `norm_num`, no `ring`, no `linarith` and no `NatCast`.
So `−1/2 + (1/5)·4 = 3/10` is **not a computation, it is a lemma** — and
`prop:bands` needs that kind of step in every clause. v35 wrote it ad hoc
three times and did not converge. v36 pays for it once.

`RatArith.lean` (general; nothing EBC-specific):

| lemma | role |
|---|---|
| `natToK_mul_inv_cancel` | `natToK (q·m) · (1/natToK m) = natToK q` — clears a denominator exactly, **no division**. The workhorse. |
| `natToK_mul_inv` | `natToK m · (1/natToK m) = 1` |
| `natToK_pos`, `natToK_ne_zero` | general forms of the `ten_pos`/`three_pos`-style lemmas written ad hoc in v35 |
| `pos_of_mul_pos_left'` | `0 < c·x` and `0 < c` ⟹ `0 < x` |
| `eq_of_mul_eq_mul_pos` | cancel a positive factor from an equality (stated in `EBC_Pairs_v3`; belongs in `RatArith`, can move unchanged) |

The strategy behind all of it is **scaling, never division**: prove
`10·x = 3` and `3 > 0`, then read off `x > 0`. That is why the layer's
missing division is not an obstacle.

Placement note: the module is general but sits *after* the EBC modules in
the import order, because `natToK` was first needed by `EBC_Dynamics` and
`natToK_mul` by `EBC_Hamming`. If either is promoted to `Prelude`, this
module moves up unchanged.

Result: the step that failed three times in v35 became four lines, and
every subsequent clause reused it.

---

## 2. `prop:bands` — status

The proposition has four parts. Three are proved; the fourth is partly
open.

| clause | status | theorem |
|---|---|---|
| (i) a singleton survives from every `z₀ ≥ 1` | **proved** | `EBC_Bands_v2.singleton_survives` |
| (ii) a Hamming-adjacent pair survives from `z₀ ≥ 1.1` | **proved** | `EBC_Pairs_v2.pair_survives` |
| (ii) and **not** from `z₀ < 1.1` | **proved** | `EBC_Pairs_v3.pair_first_step_fails` |
| (iii) nothing larger, at `z₀ = 1.0` | **proved** | `EBC_Classification.floor_survivors_agree` |
| (iii) nothing larger, at `z₀ ≥ 1.1` | **open** | see §3 |
| the counts 16 and 32 | **deferred** | instance-level; Python layer, by directive |

The pair clause now reads as a genuine threshold, not a level: sufficiency
from `1.1`, necessity below it.

How necessity works: keeping a cell at or above `1` from `z₀ < 1.1`
requires drift `> −1/10`, and

```
d(matched ψ, θ) = −1/2 + (1/5)·(4 − 2h) > −1/10   ⟺   h = 0
```

So the first step forces `hamming(ψ,θ) = 0` **and** `hamming(ψ,θ′) = 0`,
which by `hamming_eq_zero` forces `θ = θ′` on `I`, contradicting
`hamming(θ,θ′) = 1`. One action cannot serve both members, and because
the failure is at the first step there is no repair.

How "nothing larger" works at the floor: `cor_hamming_m4` gives every
pair of survivors distance `≤ 1`; three pairwise-distinct survivors would
then be pairwise at distance exactly `1`, which `lem:triangle`
(`no_adjacency_triangle`) forbids; and `floor_pair_fails` removes the
two-cell case. So all survivors agree on `I` — the maximal sets at
`z₀ = 1.0` are single cells.

---

## 3. The open piece, with its derivation

`cor_hamming_m4` is stated at `z₀ = 1`: it bounds the accumulated drift
*from zero*, and it does not transfer to a higher start. The `z₀ ≥ 1.1`
half of "nothing larger" therefore needs the `z₀`-indexed pair-sum bound.
The derivation is worked out here so it survives a context loss.

Let two cells be at Hamming distance `h`, over an index set of length `m`,
under a policy `us` of length `L`.

* **Lower** (from survival). `survivesTo_totalDrift_lower` gives
  `1 − z₀ ≤ totalDrift` for each cell, so
  `2(1 − z₀) ≤ totalDrift(θ) + totalDrift(θ′)`. By `totalDrift_pair` the
  right side is `−L + (1/5)·pairIpSum`, whence
  `pairIpSum ≥ 10(1 − z₀) + 5L`.
* **Upper** (`pairIpSum_upper`). `pairIpSum ≤ L · 2·agreeMass`, and
  `agreeMass = m − h`. At `m = 4` with `h ≥ 2` this is `≤ 4L`.
* **Combine.** `10(1 − z₀) + 5L ≤ 4L`, i.e. `L ≤ 10·(z₀ − 1)`.

At `z₀ = 1` this gives `L ≤ 0` — contradiction for nonempty `us`, which is
exactly how `cor_hamming_m4` goes through. At `z₀ = 1.1` it gives
`L ≤ 1`: a distance-`≥2` pair survives **at most one step**, so any set
surviving at all horizons has every pair at distance `≤ 1`, and
`lem:triangle` then caps it at two distinct cells.

The remaining work is therefore: generalise
`pairIpSum_lower_of_survive` from `z₀ = 1` to arbitrary `z₀` (it currently
calls `survivesTo_totalDrift_lower` and immediately rewrites `sub_self`),
and chain it with `pairIpSum_upper` plus `agreeMass ≤ 2`. Contained, but
it is several algebraic steps in the layer's idiom.

---

## 4. Scope finding: partial holds

`Tri` has three values — `pos`, `neg`, `hold` — so an action may hold at
*some* coordinates and match at others. The paper's verified alphabet at
`m = 4` is **17 actions**: the 16 cells plus the all-hold. Partial holds
are excluded there; they are **not** excluded by the type `Nat → Tri`
used throughout the layer.

This is not academic. From `z₀ = 1.0`, hold at exactly the coordinate
where the pair differs and match everywhere else: both cells score `3`
and drift `−1/2 + (1/5)·3 = +1/10`, reaching `1.1`, from which the
alternation works. **The pair survives from `1.0`.**

Consequence: `prop:bands` (ii)'s "survivable **exactly** from `z₀ ≥ 1.1`"
is true over the paper's alphabet and **false** over the unrestricted one.
The sufficiency direction needs no restriction (its witness uses only cell
actions); the necessity direction needs it essentially — which is why
`inAlphabet` is defined and why `pair_first_step_fails` is stated over it.

Recommended wording for the paper: state the action alphabet as part of
the proposition.

---

## 5. Environment

`/var/tmp` was wiped between turns, taking the build tree and the Lean
toolchain with it. Since pushes go through the GitHub API, nothing in the
layer depends on local git, so the only cost was a re-provision
(`lean-bootstrap.sh`, ~35 s; the project is dependency-free, so no
mathlib cache is needed). `lean-bootstrap.sh` had been dying on the stale
directory under `set -e`; it now reuses an existing tree instead.

---

## 6. Deliverables

* `lean_README_v12.md` — result-level index, refreshed: build state
  48 → 55 jobs / 43 → 49 modules, the `ebc` and interface slot rows, and
  new theorem-index sections for `RatArith` and `prop:bands` (760 lines).
* `patch_readme_v12.py` — the generator; prints ok/MISS per substitution
  (all four hit).
