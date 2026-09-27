# Lean audit v35

**Branch:** `lean-audit-v4` (additive). **Toolchain:** `v4.34.1`.
**Build:** `lake build` → **rc = 0, 48 jobs** (43 imported modules).
**Zero warnings. Zero `sorry`. Zero `axiom`/`opaque` declarations** in any
imported module (verified by grep across all 43 files).

Four directives, all executed: (1) close P3; (2) advance EBC; (3) probe
`comp` and stop; (4) dispose of `E1`. Plus the README refresh.

---

## 1. P3 — closed (`62dd8ad`)

`P3_FreezeValue` carries v21's pruning identity across to the corrected
family:

```
VfamAdm_prune_eq : V^adm_k(b) = lmax ((PrunedAdm M k).map (fun S => bS S b))
```

`prop:freeze` ends "the frozen value being `max_S b(S)` over the maximal
sets of the frozen family". v21 proved that for `Sfam`; v30 showed `Sfam`
is not the paper's `𝒮_k` (its `Survivable` lacks the admissibility
constraint); nobody had crossed the gap. Now it is crossed.

**Residual, stated not hidden.** v34 proved the **value** stops changing
after at most `2^{|supp b|}` strict decreases. That does **not** imply
the **family** stops shrinking — a family can shed non-maximizers without
moving the maximum. So `VfamAdm_frozen_eq_pruned` takes family-freezing
as a hypothesis. Proving it is the same pigeonhole run against
`SfamAdm`'s length rather than the value's range: short, flagged, not
done.

With this, **every P3 result row is settled**. The only open item in the
slot is `prop:deficit` (i), out of scope since v24 (`rem:operators`:
rationality is proved for the segment form because the general masked
backup needs rational kernels on `SafeMDP`, i.e. the other operator).

## 2. EBC — from 1 of 8 to 4 of 8

| Push | Commit | Content |
|---|---|---|
| `lem:triangle` | `77df544` | `EBC_ExactBelief_v3` |
| dynamics | `816ed24` | `EBC_Dynamics` §§1–4 |
| `cor:hamming` | `96ef44c` | `EBC_Dynamics` §5 |
| `m = 4` | `dc8718b` | `EBC_Hamming` |

**The `liminf` is not needed.** The paper's `cor:hamming` comes from
`lem:pairsum` (ii), a `liminf` of Cesàro averages over an infinite blind
policy. `pairIpSum_lower_of_survive` proves the same inequality at every
finite horizon `T > 0`, so no limit, no Cesàro average and no
Archimedean hypothesis enters — and the layer has none to offer. The
paper's own aside ("for a periodic policy … no `liminf` is needed")
understates the case.

Chain: `5·T ≤ pairIpSum ≤ T·2(m−h)`, cancel `T > 0` (`le_of_mul_le_mul_pos`),
giving `cor_hamming` (`five ≤ two * agreeMass`, the paper's `5 ≤ 2(m−h)`)
and `cor_hamming_dist` (`five + 2h ≤ 2m`, the paper's `h ≤ m − 5/2`
made integral, for every `m`). Then `cor_hamming_m4`: at `m = 4`,
`5 + 2h ≤ 8` ⟹ `2h ≤ 3` ⟹ `h ≤ 1`.

Cost, itemized because the layer has no `norm_num`/`ring`/`linarith`:
`natToK` (a Nat→K embedding, since there is no `OfNat` or `NatCast`),
`natToK_mul`, `neg_add`, `half_add_half`, `five_mul_fifth`,
`le_of_add_le_add_left`, `three_lt_four`, and the numeral identities.

**Not done, and why.** `cor_hamming_m4` does not include the paper's
closing "every pair inside a blind survivable set is Hamming-adjacent" —
that needs survivability to pass to subsets, a statement about the
survivable-family operator. `prop:ladder` is queued behind `prop:bands`.
`prop:deadline` behind the delayed-instance dynamics. `prop:pbvi` and
`prop:census` are instance-level (84 pairings; 65,536 subsets with the
zero-suppressed representation cited to Minato 1993) and belong to the
Python verifier, not Lean.

## 3. `comp` — probed, not expanded

**Directive: skip `prop:rank`. Record the coverage row. Do not expand the
layer to chase one result.** Honoured.

Coverage row, as recorded in the index:

> **Farkas core proved** (`Prelude.farkas_sound`); `prop:value`,
> `thm:bridge`, `prop:beliefcells` **out of reach by design** — the layer
> has no topology and no integration.

Two findings that changed the picture:

1. **`farkas_sound` is already a proved theorem** (`Prelude:748`), and the
   layer has **zero axioms**. I had predicted Farkas would be a wall; it
   was never the blocker. The scaffolding is conditional on the
   *continuous-time* facts.
2. The layer's analysis inventory is empty: a grep for
   `continuous`/`Compact`/`∫`/`TopologicalSpace` across all 43 modules
   returns five hits, **every one prose inside a docstring**.

`prop:rank`'s proof *is* an explicit Farkas certificate (`λ = (1,…,1,1)`;
rows combine to zero, right-hand sides sum to `−ε`), so it is the one
item that could have been pushed. It is skipped by directive: the
honest coverage row is worth more than a partial, and reaching the
proposition's actual statement would require modelling ODEs and
integration. Full reasoning in `lean_audit_v35_comp_probe.md`.

## 4. `E1` — option A then B (`4278fd7`)

**Directive: relabel honestly, move `ladder_ascent` into `Prelude` under
an honest name, do not retarget.** Executed, with one deviation flagged.

- **A (relabel).** `paperE1_cod_forecast_ladder_v59.tex` has **zero**
  numbered environments; the paper's "ladder" is a forward-ordered
  sequence of surplus-production models scored on NAFO 2J3KL cod data;
  `grep` finds `telescope`: 0, `level margin`: 0, `forward margin`: 0 —
  so the module's "calibrated ladder" paper references are invented. Four
  of its five theorems are one-line aliases of `Prelude` lemmas.
- **B (relocate).** The fifth, `ladder_ascent`, is now
  `Formalizations.monotone_step_ascent` in the new module
  `Prelude_Monotone`. Statement and proof unchanged; name, placement and
  docstring honest. It is not a fact about sums, so it is not named
  `sumRange_*`.
- **Deviation.** "Into `Prelude`" would mean editing `Prelude.lean`, and
  the layer's rule is that any revision to an existing file gets a new
  version. `Prelude.lean` heads a 43-module import cascade, so a
  `Prelude_v2` would force every module to switch. The lemma therefore
  goes in a new foundational module imported immediately after `Prelude`.
- No retargeting: with no numbered environments, inventing a target is
  how the defect arose.

`E1_ForecastLadder` is untouched (this layer does not delete) and still
builds green.

## 5. Index refresh

`lean_README_v11.md` supersedes v10: build state 43→48 jobs and 40→43
imported modules; the `comp`, `ebc`, `E1`, `P3` and interface slot rows;
the `prop:freeze` row; the P3 totals line; and five new theorem-index
sections.

**A second staleness found while patching:** the P3 slot row had not been
updated since v30 — it was missing `P3_Rational`, `P3_Binomial`,
`P3_SupportValue`, `P3_SupportRepair` and `P3_FreezeCount` as well. Fixed.

## 6. Environment note

`/var/tmp` is not persisted between turns, so the clone and the toolchain
were both gone at the start of this turn. `/home/user/lean-bootstrap.sh`
now re-provisions both (elan + `v4.34.1` + depth-1 clone) in ~30 s, and
`push.py` reads the token from the persisted
`/home/user/uploads/github_pat.txt` rather than from the clone's git
config.

## 7. Commits this round

| Commit | Contents |
|---|---|
| `62dd8ad` | `P3_FreezeValue` + import |
| `77df544` | `EBC_ExactBelief_v3` (`lem:triangle`) + import |
| `816ed24` | `EBC_Dynamics` §§1–4 + import |
| `96ef44c` | `EBC_Dynamics` §5 (`cor:hamming`) |
| `cb3746f` | comp probe + E1 decision records |
| `4278fd7` | `Prelude_Monotone` + import (E1 · B) |
| `dc8718b` | `EBC_Hamming` (`cor_hamming_m4`) + import |
