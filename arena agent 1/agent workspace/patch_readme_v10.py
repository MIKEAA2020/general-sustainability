s = open('lean_README_v9.md').read()
s = s.replace("### v9 — result-level index", "### v10 — result-level index", 1)
s = s.replace("> **This file supersedes `lean_README_v8.md`.**",
              "> **This file supersedes `lean_README_v9.md`.**", 1)
s = s.replace("""# Lean Formalization Layer — `general-sustainability` paper family
### v10 — result-level index
""", """# Lean Formalization Layer — `general-sustainability` paper family
### v10 — result-level index

> **What changed since v9 (v34).** One module, `P3_FreezeCount`; the build
> went 42 → 43 jobs, 39 → 40 imports. Plus the paper edit, issued as
> `paper2_probabilistic_sufficiency_v12.tex`.
>
> 1. **`prop:freeze`'s `2^{|supp b|}` is proved** — the last paper-owned
>    claim in P3. `strictDrop_length_le`: for every horizon `n`, the
>    number of strict decreases among the first `n` horizons is at most
>    `2^{|supp b|}`. The paper asserts this one itself, so unlike Sperner
>    it could not be skipped.
> 2. **A defect in this layer, found and recorded.** v18's
>    `prop_freeze_drop_count` was listed as having done the count. Its
>    **statement** bounds the drops by `2^{|univX|}`; its **comment**
>    claims `2^{|supp b|}`. The comment over-claims, and the README had
>    propagated it. Corrected here and in `lean_audit_v34.md` §2; the v18
>    file is left untouched. The new theorem is also on the **corrected**
>    family (`SfamAdm`/`VfamAdm`), not the defective `Sfam`/`Vfam`.
> 3. **The paper edit is applied**, as `v12`: the three-symbol fix
>    (`𝒲^{fb}_k`, `𝒲_k`, `𝒲^{bel}_k`, with `𝒲^{bel}_k` explicitly the
>    analogue of the blind `𝒲_k`), the restated `thm:support`, a
>    replacement for the invalid converse, and the new
>    `rem:feedback-strict`. `prop:deficit` (ii) left untouched, as §4 of
>    the draft requires.
""", 1)
s = s.replace("`lake build` → **rc = 0, 42 jobs** (39 imported modules). Zero `sorry`.",
              "`lake build` → **rc = 0, 43 jobs** (40 imported modules). Zero `sorry`.", 1)

old = s[s.index("| 8 | `prop:freeze`"):]
old = old[:old.index("\n")]
new = ("| 8 | `prop:freeze` | **result** (same correction as (3)) | nesting + antitonicity on the "
       "corrected family `SfamAdm_nesting`, `VfamAdm_antitone` (v30). **Drop count at the paper's "
       "bound `2^{\\|supp b\\|}`**: `P3_FreezeCount.strictDrop_length_le` (v34) — plus "
       "`no_drop_beyond_bound`, the stabilization form. **v18's** `prop_freeze_drop_count` is a "
       "*weaker* statement: its bound is `2^{\\|univX\\|}` (its comment claims `2^{\\|supp b\\|}` — see "
       "`lean_audit_v34.md` §2) and it runs on the defective `Sfam`/`Vfam`. Second clause — frozen "
       "value as `max_S b(S)` over the **maximal** sets — proved for the old family "
       "(`Vfam_prune_eq`, v21), **not yet** for `SfamAdm` |")
s = s.replace(old, new, 1)

new_sec = """### `P3_FreezeCount` — `prop:freeze`'s count (v34)

**`strictDrop_length_le`**: for every horizon `n`, the number of strict
decreases of `ℓ ↦ V_ℓ(b)` below `n` is at most `2^{|supp b|}` — the paper's
bound, on the corrected family `SfamAdm`/`VfamAdm`.

Three ingredients, none of them previously available in combination:

* `VfamAdm_mem_range` — every value of the sequence is `b(T)` for some
  `T ⊆ supp(b)`; the maximum is attained (`lmax_isMax`) and truncating a
  maximizer to the support preserves its mass (`bS_supp_trunc`).
* `strictDrop_value_inj` — two strict drops never repeat a value, by
  `VfamAdm_antitone`: `V_{k₂} ≤ V_{k₁+1} < V_{k₁}`.
* `subsetsOf_length` (v13) for the `2^{|supp b|}`, and a new
  `nodup_mem_length_le` (pigeonhole for lists) to turn "distinct values
  inside a list of length `N`" into "at most `N` drops".

`no_drop_beyond_bound` is the paper's "stabilizes" phrasing: once the drop
list has reached the bound it cannot grow. Supporting list lemmas
(`nodup_mem_length_le`, `nodup_map_on_of_inj`, `nodup_filterP`,
`mem_erase_of_mem_of_ne`) are proved here because the layer has no
cardinality machinery.

**Not to be confused with `P3_Freeze_Noisy_v2.prop_freeze_drop_count`
(v18)**, which bounds the drops by `2^{|univX|}` — weaker, and on the
family v30 showed to be defective. Its docstring claims `2^{|supp b|}`;
the statement does not. That over-claim is recorded in
`lean_audit_v34.md` §2 and corrected in this row. The v18 file is left
untouched.

### `P1_AssessmentSeparation_v5` — result"""
s = s.replace("### `P1_AssessmentSeparation_v5` — result", new_sec, 1)
open('lean_README_v10.md', 'w').write(s)
print("wrote", len(s))
