# Lean audit — v37

Branch `lean-audit-v4`. Range: `b95e5de` → `2bf7d4b` and the README/audit
push that follows.

```
0529cc1  EBC_Classification_v2 — the z₀-indexed pair-sum bound
2bf7d4b  EBC_Classification_v3 — the horizon bound
```

Build: `lake build` → **rc = 0, 57 jobs** (51 imported modules). Zero
warnings, zero `sorry`, zero axioms.

---

## 1. `prop:bands` is closed

The last open clause landed. `cor_hamming_m4` bounds two survivors'
Hamming distance, but only from `z₀ = 1`: it bounds the accumulated drift
*from zero*, and it does not transfer to a higher start. So the
`z₀ ≥ 1.1` half of "nothing larger" needed the bound re-done with `z₀` as
a parameter.

**`EBC_Classification_v2`** supplies the two substantive pieces:

* `pairIpSum_lower_of_survive_z0` — two survivors accumulate at least
  `2(1 − z₀)` of combined drift, so `5·((1−z₀) + (1−z₀) + L) ≤ pairIpSum`.
  This is `pairIpSum_lower_of_survive` with the `z₀ = 1` specialization
  undone: that lemma calls `survivesTo_totalDrift_lower` and immediately
  rewrites `sub_self`, discarding the `z₀` now needed.
* `agreeMass_le_two_of_far`, `pairIpSum_upper_far` — at `m = 4` with
  `h ≥ 2`, `agreeMass = 4 − h ≤ 2`, hence `pairIpSum ≤ L·4`.

Chained: `5·(2(1−z₀) + L) ≤ 4L`.

**`EBC_Classification_v3`** performs the reduction — distribute the `5`,
collect `A + A` into `10·A`, move `5·L` across (by adding its negation:
the layer has no `sub_le_sub_right`), simplify `4·L − 5·L = −L` via
`sub_mul` and `4 − 5 = −1`, then negate — giving

    **`far_pair_horizon_bound`:  `|us| ≤ 10·(z₀ − 1)`**

At `z₀ = 1` this forces `L = 0`: nothing nonempty survives, which is
exactly how `cor_hamming_m4` goes through. At `z₀ = 1.1` it gives
`L ≤ 1`: a distance-`≥2` pair survives **at most one step**, so it cannot
appear in any set that survives at *all* horizons. For larger `z₀` the
horizon is capped, which is equally fatal to a claim of survival at every
horizon — the classification's actual quantifier.

### Status table

| clause | status | theorem |
|---|---|---|
| (i) singleton survives from every `z₀ ≥ 1` | proved | `EBC_Bands_v2.singleton_survives` |
| (ii) adjacent pair survives **exactly** from `z₀ ≥ 1.1` | proved | `EBC_Pairs_v2.pair_survives`, `EBC_Pairs_v3.pair_first_step_fails` |
| (iii) nothing larger, at `z₀ = 1.0` | proved | `EBC_Classification.floor_survivors_agree` |
| (iii) nothing larger, at `z₀ ≥ 1.1` | **proved** | `EBC_Classification_v3.far_pair_horizon_bound` |
| counts 16 / 32 | deferred | instance-level; Python verifier, by directive |

---

## 2. `prop:ladder` — analysed, scoped, not started

The proposition states that the maximal conditional kernel mass doubles
with each probe: `1/16 → 1/8 → 1/4 → 1/2 → 1` at `z₀ = 1.0`, and
`1/8 → 1/4 → 1/2 → 1 → 1` above the edge, for zero through four probes.

Its proof has three inputs:

1. **The antichain value formula** (companion P3 theory). The kernel
   value of a prior is the maximal survivable-set mass it charges;
   survivability is hereditary downward; so for the uniform prior on a
   support `S`, the value is `max{|A| : A ⊆ S, A survivable} / |S|`.
   Already proved in the P3 slot — `P3_FreezeValue.VfamAdm_prune_eq`
   (v35) is the value-as-max-over-maximal-sets form on the corrected
   family.
2. **Heredity.** Proved here in EBC terms:
   `EBC_Classification.survivesSet_mono`.
3. **`prop:bands`.** Proved — singletons at the floor, Hamming-adjacent
   pairs above the edge.

With those, a `2^j`-cell subcube has value `1/2^j` at the edge and
`2/2^j` above it (capped at `1` for `j = 0`), which *is* the ladder.

**Instance-level, and therefore left to the verifier:** the ten numbers
themselves, the 16 cells, the `2^j` subcube sizes, and the assertion that
supports after `0…4` probes are subcubes with `j = 4,3,2,1,0`. The paper
says as much: "the script recomputes all ten values by exhaustive
survivable-subset enumeration within each support".

**The remaining work is a cross-paper bridge, not a new idea.** The P3
slot and the EBC slot currently use *different* notions of survivable
set: P3's is the class-restricted `SfamAdm` family, EBC's is the
drift-and-floor `survivesTo`. Connecting the P3 value functional to EBC
survivability, and modelling a probe as a restriction of the index set,
is the work. The mathematics on the EBC side is done.

---

## 3. Environment

`/var/tmp` was wiped again between turns — tree and toolchain both gone.
Re-provisioning is ~30 s (the project is dependency-free, so no mathlib
cache is fetched). Nothing in the layer depends on local git, since
pushes go through the API.

`lean-bootstrap.sh`'s reuse heuristic had accepted any directory
containing `lean/`, which after a partial wipe would silently reuse an
empty tree; it now requires `Formalizations.lean` and at least 20 modules
before reusing.

---

## 4. Deliverables

* `lean_README_v13.md` (813 lines) — build state 55 → 57 jobs /
  49 → 51 modules; the `ebc` slot row; `prop:bands` (iii) marked proved;
  a new `prop:ladder` section recording the decomposition and what is
  instance-level. Generated by `patch_readme_v13.py` (5/5 substitutions
  hit).
* This audit.
