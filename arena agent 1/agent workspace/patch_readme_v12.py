#!/usr/bin/env python3
"""lean_README_v11.md -> lean_README_v12.md

v36 additions: the prop:bands sequence (matched play, mismatched play,
the pair clause, the classification at the floor) plus the shared
rational-arithmetic helper. Targeted substitutions; each prints ok/MISS.
"""
import io, os

SRC = "/home/user/lean_README_v11.md"
DST = "/home/user/lean_README_v12.md"

HEADER_OLD = """### v11 — result-level index

> **What changed since v10 (v35).** Four pushes: P3 closed, EBC taken from
> 1 of 8 results to 4, the `comp` slot probed and its unreachable half
> recorded, the `E1` slot relabelled. Build went 43 → 48 jobs,
> 40 → 43 imported modules."""

HEADER_NEW = """### v12 — result-level index

> **What changed since v11 (v36).** `prop:bands` taken apart and largely
> rebuilt. The blocker was not mathematics but arithmetic: the layer has
> no `norm_num`, no `ring` and no `linarith`, so `−1/2 + (1/5)·4 = 3/10`
> is a lemma, not a computation. v35 had written that step ad hoc three
> times without converging; v36 pays for it **once**, in `RatArith`
> (`natToK_mul_inv_cancel` clears a denominator exactly, no division;
> `pos_of_mul_pos_left'` converts a scaled inequality back), and every
> clause after that is cheap.
>
> 1. **The shared rational-arithmetic helper** — `RatArith`:
>    `natToK_mul_inv_cancel`, `pos_of_mul_pos_left(')`, `eq_of_mul_eq_mul_pos`.
>    Nothing in it is EBC-specific; it sits after the EBC modules only
>    because `natToK` is defined there.
> 2. **`prop:bands`, singleton clause** — matched play rises at `+3/10`,
>    so a singleton survives from every `z₀ ≥ 1` at every horizon
>    (`EBC_Bands_v2.singleton_survives`).
> 3. **`prop:bands`, pair clause** — Hamming-adjacent pairs survive
>    **exactly** from `z₀ ≥ 1.1`: sufficiency by the alternation
>    (`EBC_Pairs_v2.pair_survives`), necessity because from `z₀ < 1.1`
>    no in-alphabet action keeps both members above the floor for even
>    one step (`EBC_Pairs_v3.pair_first_step_fails`).
> 4. **`prop:bands`, "nothing larger" at the floor** — at `z₀ = 1.0`
>    all surviving cells agree on `I`
>    (`EBC_Classification.floor_survivors_agree`), so the maximal sets
>    are single cells. The 16 and 32 **counts** are instance-level and
>    stay with the verifier, by directive.
>
> A **scope finding** came out of this and is recorded in `EBC_Pairs`:
> `Tri` has a `hold` value, so the layer's action type admits *partial*
> holds, which the paper's verified alphabet (17 actions at `m = 4`: the
> 16 cells plus the all-hold) excludes. From `z₀ = 1.0`, holding at
> exactly the coordinate where a pair differs and matching elsewhere
> gives both cells `+1/10` and rescues the pair. So "survivable exactly
> from `z₀ ≥ 1.1`" is **true over the paper's alphabet and false over
> the unrestricted one** — the proposition needs its action set stated.
>
> Build went 48 → 55 jobs, 43 → 49 imported modules."""

BUILD_OLD = "`lake build` → **rc = 0, 48 jobs** (43 imported modules). Zero `sorry`."
BUILD_NEW = "`lake build` → **rc = 0, 55 jobs** (49 imported modules). Zero `sorry`."

SLOT_EBC_OLD = "| ebc | Exact belief computation (`paper2_exact_belief_computation_v10.tex`) | `EBC_ExactBelief_v2`; `EBC_ExactBelief_v3`, `EBC_Dynamics`, `EBC_Hamming` (v35) |"
SLOT_EBC_NEW = "| ebc | Exact belief computation (`paper2_exact_belief_computation_v10.tex`) | `EBC_ExactBelief_v2`; `EBC_ExactBelief_v3`, `EBC_Dynamics`, `EBC_Hamming` (v35); `EBC_Bands`, `EBC_Bands_v2`, `EBC_Pairs`, `EBC_Pairs_v2`, `EBC_Pairs_v3`, `EBC_Classification` (v36) |"

IFACE_OLD = "| — | interface | `Prelude`; `Prelude_Monotone` (v35) |"
IFACE_NEW = "| — | interface | `Prelude`; `Prelude_Monotone` (v35), `RatArith` (v36) |"

APPEND = """

### `RatArith` — machinery (v36)

Rational arithmetic over a bare `OrdField`. The layer has no `norm_num`,
no `ring` and no `linarith`, so clearing denominators is a lemma.

* **`natToK_mul_inv_cancel`** — `natToK (q·m) · (1 / natToK m) = natToK q`:
  clears a denominator exactly, with no division. The workhorse.
* `natToK_mul_inv` — `natToK m · (1 / natToK m) = 1`, for `m ≠ 0`.
* `natToK_pos`, `natToK_ne_zero` — general forms of the `ten_pos` /
  `three_pos` style lemmas that had been written ad hoc.
* **`pos_of_mul_pos_left'`** — `0 < c·x` and `0 < c` give `0 < x`: the
  order half of the scaling argument.
* `eq_of_mul_eq_mul_pos` — cancel a positive factor from an equality
  (currently stated in `EBC_Pairs_v3`; belongs here and can move
  unchanged).

### EBC — `prop:bands` (v36)

| # | Result | Status | Module / where |
|---|---|---|---|
| — | `prop:bands` (i) — a singleton survives from every `z₀ ≥ 1` | **result clause** | `EBC_Bands_v2.singleton_survives`; matched drift `+3/10` is `matched_drift_pos_m4` |
| — | `prop:bands` (ii) — a Hamming-adjacent pair survives from `z₀ ≥ 1.1` | **result clause** | `EBC_Pairs_v2.pair_survives`, on the alternation `altPairs`; cycle gain `+1/5` is `cycle_net_nonneg` |
| — | `prop:bands` (ii) — and **not** from `z₀ < 1.1` | **result clause** | `EBC_Pairs_v3.pair_first_step_fails`, **over `inAlphabet`** |
| — | `prop:bands` (iii) — nothing larger, at `z₀ = 1.0` | **result clause** | `EBC_Classification.floor_survivors_agree` (all survivors agree on `I`), `no_three_survivors`, `survivesSet_mono` |
| — | `prop:bands` (iii) — nothing larger, at `z₀ ≥ 1.1` | **open** | Needs the `z₀`-indexed pair-sum bound; `cor_hamming_m4` is stated at `z₀ = 1` and does not transfer. See `lean_audit_v36.md` §3 for the derivation |
| — | the counts **16** singletons and **32** pairs | **instance** | Python layer, by directive |

Supporting: `EBC_Bands.matched` / `ipi_matched` / `drift_matched`;
`EBC_Pairs.ipi_mismatched` (`⟨matched θ′, θ⟩ = m − 2h`),
`mismatch_scale_m4` (the `−1/10`), `mismatched_step_floor` (the dip);
`EBC_Pairs_v3.drift_cell_le_neg_tenth`; `EBC_Pairs_v2.inAlphabet`.

**Caveat carried by every one of these clauses.** `inAlphabet` is the
paper's action set: the 16 cell actions plus the all-hold. The layer's
action type `Nat → Tri` is larger — it admits partial holds — and over
that larger set `prop:bands` (ii)'s "exactly" is false. See the note in
`EBC_Pairs` and the audit.
"""

def patch(s, old, new, label):
    if old in s:
        s = s.replace(old, new, 1)
        print(f"ok   {label}")
    else:
        print(f"MISS {label}")
    return s

def main():
    s = io.open(SRC, encoding="utf-8").read()
    s = patch(s, HEADER_OLD, HEADER_NEW, "header v11 -> v12")
    s = patch(s, BUILD_OLD, BUILD_NEW, "build state 48 -> 55 jobs")
    s = patch(s, SLOT_EBC_OLD, SLOT_EBC_NEW, "ebc slot row")
    s = patch(s, IFACE_OLD, IFACE_NEW, "interface slot row")
    s = s.rstrip("\n") + "\n" + APPEND
    io.open(DST, "w", encoding="utf-8").write(s)
    print(f"wrote {DST}: {len(s.splitlines())} lines, {os.path.getsize(DST)} bytes")

if __name__ == "__main__":
    main()
