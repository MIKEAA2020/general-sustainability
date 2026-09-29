#!/usr/bin/env python3
"""Generate lean_README_v11.md from v10 (additive; v10 untouched)."""
src, dst = '/home/user/lean_README_v10.md', '/home/user/lean_README_v11.md'
lines = open(src).read().split('\n')
hits = []


def sub_once(old, new):
    global lines
    txt = '\n'.join(lines)
    if old not in txt:
        hits.append(('MISS', old[:60]))
        return
    lines = (txt.replace(old, new, 1)).split('\n')
    hits.append(('ok', old[:60]))


def append_to_line(prefix, suffix):
    global lines
    for i, l in enumerate(lines):
        if l.startswith(prefix):
            lines[i] = l.rstrip() + suffix
            hits.append(('ok', prefix[:60]))
            return
    hits.append(('MISS', prefix[:60]))


# 1. header + new top-matter block
new_block = '''### v11 — result-level index

> **What changed since v10 (v35).** Four pushes: P3 closed, EBC taken from
> 1 of 8 results to 4, the `comp` slot probed and its unreachable half
> recorded, the `E1` slot relabelled. Build went 43 → 48 jobs,
> 40 → 43 imported modules.
>
> 1. **`prop:freeze`'s closing clause, on the corrected family** —
>    `P3_FreezeValue.VfamAdm_prune_eq`: the value is the maximum of `b(S)`
>    over the *maximal* jointly survivable sets. v21 had this for the old
>    family; v30 showed the old family is not the paper's `𝒮_k`. **P3 is
>    closed**, with one honest residual: v34 proved the **value**
>    stabilizes after `2^{|supp b|}` strict decreases, not that the
>    **family** stops shrinking, so `VfamAdm_frozen_eq_pruned` takes
>    family-freezing as a hypothesis.
> 2. **EBC: `lem:triangle`, `cor:hamming`, `cor_hamming_m4`.**
>    `EBC_ExactBelief_v3` (no three cells pairwise at Hamming distance 1),
>    `EBC_Dynamics` (the drift model `lem:pairsum` fixes — trajectories,
>    floor, survival), `EBC_Hamming` (the paper's own `h ≤ 1` at `m = 4`).
>    The paper derives `cor:hamming` from a `liminf` of Cesàro averages;
>    the formalization needs no limit — the inequality holds at every
>    finite horizon.
> 3. **`comp` probed, not expanded.** `farkas_sound` is already proved
>    (`Prelude:748`, axiom-free), so Farkas was never the blocker. The
>    continuous-time results (`prop:value`, `thm:bridge`,
>    `prop:beliefcells`) are **out of reach by design**: the layer has no
>    topology and no integration, and was not expanded to chase one
>    result. See `lean_audit_v35_comp_probe.md`.
> 4. **`E1` relabelled.** The target paper has zero numbered environments
>    and the module's paper references are invented (no "telescope", no
>    "level margin" anywhere in the paper). The one genuine lemma is now
>    `Prelude_Monotone.monotone_step_ascent`. See
>    `lean_audit_v35_e1_decision.md`.

### v10 — result-level index'''

sub_once('### v10 — result-level index', new_block)

# 2. build state
sub_once('**rc = 0, 43 jobs** (40 imported modules)',
         '**rc = 0, 48 jobs** (43 imported modules)')

# 3. slot table
sub_once('| comp | Computational certification (`paper2_computational_certification_v18.tex`) | `Comp_Certification`, `Comp_Certification_v2` |',
         '| comp | Computational certification (`paper2_computational_certification_v18.tex`) | `Comp_Certification`, `Comp_Certification_v2` — **Farkas core proved** (`Prelude.farkas_sound`); `prop:value`, `thm:bridge`, `prop:beliefcells` out of reach by design (v35) |')
sub_once('| ebc | Exact belief computation (`paper2_exact_belief_computation_v10.tex`) | `EBC_ExactBelief_v2` |',
         '| ebc | Exact belief computation (`paper2_exact_belief_computation_v10.tex`) | `EBC_ExactBelief_v2`; `EBC_ExactBelief_v3`, `EBC_Dynamics`, `EBC_Hamming` (v35) |')
sub_once('| E1 | Applied forecast ladder (`paperE1_cod_forecast_ladder_v59.tex`) | `E1_ForecastLadder` |',
         '| E1 | Applied forecast ladder (`paperE1_cod_forecast_ladder_v59.tex`) | `E1_ForecastLadder` — **no formalizable target**: the paper has zero numbered environments and the module\'s paper references do not exist (v35); the one genuine lemma is relocated to `Prelude_Monotone` |')
sub_once('| — | interface | `Prelude` |',
         '| — | interface | `Prelude`; `Prelude_Monotone` (v35) |')
sub_once('`P3_FreezeCount` |', '`P3_FreezeCount`, `P3_FreezeValue` |')

# 4. prop:freeze row
append_to_line('| 8 | `prop:freeze`',
               ' **Frozen-value clause on the corrected family: `VfamAdm_prune_eq` (v35).**')

# 5. P3 totals
sub_once('**P3 totals: 11 result · 1 partial · 6 instance · 1 out of reach**',
         '**P3 totals: 11 result · 1 partial · 6 instance · 1 out of reach** — and P3 is now closed: every result row is settled, the only open item being `prop:deficit` (i), out of scope since v24 (`rem:operators`)')

# 6. new theorem-index sections
sections = r'''
### `P3_FreezeValue` — `prop:freeze`'s frozen-value clause (v35)

Carries v21's pruning identity across to the corrected family, which is
what `prop:freeze`'s closing clause was missing.

* `PrunedAdm`, `PrunedAdm_mem`, `PrunedAdm_ne`, `SfamAdm_mem_nodup`.
* `VfamAdm_prune_eq` — **`prop:freeze`'s "frozen value is `max_S b(S)`
  over the maximal sets of the frozen family"**, on `𝒮^adm_k`. This is
  also `prop:antichain` (ii) for the corrected family.
* `VfamAdm_frozen_eq_pruned` — the frozen-value form. **Family-freezing
  is a hypothesis**: a family can keep losing non-maximizers without the
  maximum moving, so value-stabilization (v34) does not imply it.
* `PrunedAdm_antichain` — by v20's `maximals_antichain`.

### `EBC_ExactBelief_v3` — `lem:triangle` (v35)

`hamming` (by recursion on the index list, not by filtering),
`hamming_eq_zero`, `hamming_ne_zero_exists`, `hamming_zero_of_agree`, and

* `no_adjacency_triangle` — no three cells are pairwise at Hamming
  distance `1`, any `m`. Proved via the parity invariant the paper names
  in passing (the hypercube is bipartite): at each coordinate the three
  "differ" indicators are all `0` or exactly two `1`s.
* `no_three_pairwise_adjacent` — the contradiction form.

### `EBC_Dynamics` — the drift model (v35)

The layer had the inner product and the pair-sum bound, but no
trajectory, no floor, no survival.

* `natToK` — the Nat→K embedding the layer lacks (no `OfNat`, no
  `NatCast`), with `natToK_nonneg/add/mono`, `lsum_ones`, `natToK_le_one`.
* `neg_add`, `half_add_half`, `five_mul_fifth`, `two_pos`, `five_pos`.
* `drift` (`-1/2 + (1/5)⟨u,θ⟩`), `stateAfter`, `totalDrift`,
  `survivesTo`, `stateAfter_eq`, `survivesTo_totalDrift_lower`.
* `pairIpSum`, `drift_pair`, `totalDrift_pair`.
* §5 `pairIpSum_upper`, `pairIpSum_lower_of_survive`,
  `le_of_mul_le_mul_pos`, `agreeMass_add_natToK_hamming`,
  **`cor_hamming`** (`five ≤ two * agreeMass`, the paper's `5 ≤ 2(m−h)`),
  **`cor_hamming_dist`** (`five + 2h ≤ 2m`, the paper's `h ≤ m − 5/2`).

The paper reaches `cor:hamming` through a `liminf` of Cesàro averages;
the formalization holds at every finite horizon and needs no limit.

### `EBC_Hamming` — `cor:hamming` at `m = 4` (v35)

* `natToK_mul`, `two_mul_two_eq_four`,
  `two_mul_four_eq_five_add_three`, `le_of_add_le_add_left`,
  `three_lt_four`.
* **`cor_hamming_m4`** — Hamming distance `≤ 1` for two cells that both
  survive a nonempty horizon from `z₀ = 1` over a 4-dimensional index
  set. Does **not** include the paper's closing "every pair inside a
  blind survivable set is Hamming-adjacent", which needs survivability
  to pass to subsets.

### `Prelude_Monotone` — relocated (v35)

* `monotone_step_ascent` — a sequence whose steps never descend never
  descends. Relocated from `E1_ForecastLadder.ladder_ascent`, the only
  one of that module's five theorems with a proof (the other four are
  one-line aliases of `sumRange` lemmas) and the only one whose stated
  paper reference survives checking.
'''

txt = '\n'.join(lines).rstrip() + '\n' + sections
open(dst, 'w').write(txt)
for st, what in hits:
    print(st, '|', what)
print('written', dst, len(txt), 'bytes')
