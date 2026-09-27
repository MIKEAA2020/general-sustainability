# Lean verification audit — v34
## The `2^{|supp b|}` count, the paper edit, and a defect found in our own layer

Branch `lean-audit-v4`. Build: **rc = 0, 43 jobs, 40 imported modules, zero
warnings, zero `sorry`** (fresh-clone verified, §6).

New: `lean/Formalizations/P3_FreezeCount.lean` (green) and
`arena agent 1/paper rewrites/latex/paper2_probabilistic_sufficiency_v12.tex`
(the paper edit, issued as a new file per the never-overwrite rule).

---

## 1 · The count is proved — at the paper's bound, on the corrected family

```
theorem strictDrop_length_le (M : DetMDP K X A D Y) (b : Mass K X) (n : Nat) :
    (strictDrop M b n).length ≤ 2 ^ (suppList M b).length
```

For **every** horizon `n`, the number of horizons below `n` at which
`ℓ ↦ V_ℓ(b)` strictly drops is at most `2^{|supp b|}`. Stated for all `n`
rather than "eventually", because that is what "stabilizes after at most"
means and it is checkable without a limit.

The argument, and the three facts it needs:

* `VfamAdm_mem_range` — **every** value of the sequence is `b(T)` for some
  `T ⊆ supp(b)`. The maximum is attained (`lmax_isMax`), and truncating a
  maximizer to the support does not change its mass (`bS_supp_trunc`:
  `b(S) = b(S ∩ supp b)`, because states outside the support carry zero
  mass). The truncation is taken as `(suppList b).filter (· ∈ S)` rather
  than `S.filter (· ∈ suppList b)` — same elements, but only the former is
  a member of `subsetsOf (suppList b)`, since `subsetsOf` records subsets
  in the order of the ambient list.
* `strictDrop_value_inj` — two strict drops never repeat a value: if
  `k₁ < k₂` and the sequence drops at `k₁`, then
  `V_{k₂} ≤ V_{k₁+1} < V_{k₁}` by `VfamAdm_antitone`.
* `subsetsOf_length` (v13) — there are exactly `2^{|supp b|}` subsets, and
  `nodup_mem_length_le` (new here) converts "distinct values, all inside a
  list of length `N`" into "at most `N` drops".

`nodup_mem_length_le`, `nodup_map_on_of_inj`, `nodup_filterP` and
`mem_erase_of_mem_of_ne` are proved here because the layer has no
cardinality machinery and its `nodup_filter` is stated for `Bool`
predicates only.

---

## 2 · A defect in our own layer: v18's count over-claims

`P3_Freeze_Noisy_v2.prop_freeze_drop_count` (v18) is real, and the README
listed `prop:freeze`'s count as done on its account. **It is not done at
the bound the paper states**, and the module's own comment says otherwise:

```
/-- **`prop:freeze`, in full.**  The number of strict decreases of
`ℓ ↦ V_ℓ(b)` before any horizon `n` is at most `2^{|supp b|}`. -/
theorem prop_freeze_drop_count (M ...) (b ...) (n : Nat) :
    drops M b n ≤ 2 ^ M.univX.length := ...
```

The comment says `2^{|supp b|}`; the statement says `2^{|univX|}`. Those
differ whenever the support is a proper subset of the state space, which
is the usual case and the case the paper is about. The chain is
`drops_le_card` (drops ≤ `|𝒮_0|`) then `Sfam0_card_le` (`|𝒮_0|` ≤
`2^{|univX|}`) — correct at every step, and simply not the paper's claim.
It also runs on the **old** family `Sfam`/`Vfam`, whose `Survivable` lacks
the admissibility constraint (the v30 defect), not on the corrected
`SfamAdm`/`VfamAdm`.

So the new module is not a duplicate: it is the paper's bound (`supp`, not
`univX`) on the corrected family. And the over-claim had already
propagated into `lean_README`'s `prop:freeze` row, which is corrected in
v10. Recorded here rather than quietly fixed, for the same reason as the
P3 miscount in v6: a coverage index is exactly the place where this class
of error must be visible.

The v18 file is left untouched (never-overwrite); the correction is
carried in `P3_FreezeCount`'s header, in the README v10 row, and here.

---

## 3 · The paper edit has been applied — as v12, not by overwriting

`paper2_probabilistic_sufficiency_v12.tex` (86,998 bytes; v11 untouched).
Six edits, all surgical:

| # | where | change |
|---|---|---|
| 1 | intro, l.52 | "viable-set recursion `𝒲_k`" → `𝒲^{fb}_k` |
| 2 | notation, ll.251–253 | **three** symbols: `𝒲^{fb}_k` (feedback), `𝒲_k` (blind), `𝒲^{bel}_k` (belief-space analogue **of `𝒲_k`**) |
| 3 | recursion, ll.301–304 | `𝒲^{fb}_k` defined with the observation-split continuation; `𝒲_k` retained as the special case where the continuation may not depend on `y`; `𝒲_k ⊆ 𝒲^{fb}_k`, strictly, cross-referenced to the new remark |
| 4 | `thm:support`, ll.317–318 | `𝒲_k` → `𝒲^{fb}_k` in the statement |
| 5 | `thm:support` proof, ll.335–341 | **the converse replaced** (see §4) |
| 6 | after l.345 | new `rem:feedback-strict` |

`\begin`/`\end` balanced (62/62, +1 for the remark).

### §4 of the draft was checked before the edit landed

The one place a plausible relabelling does damage is `prop:deficit` (ii)
(ll.796–798 v11 / 845–881 v12), whose proof cites `prop:degen` — the blind
proposition — and which quantifies over `𝒲^{bel}_k`. **`𝒲^{bel}_k` is
unchanged**, and its defining sentence (l.845–847: "the family of beliefs
whose support admits a jointly surviving **declared-class** sequence")
still matches the blind `𝒲_k`. The notation block now says explicitly that
`𝒲^{bel}_k` is the analogue of `𝒲_k`, not of `𝒲^{fb}_k`.

Everything else in §4 holds: `prop:degen` (blind throughout, never names
`𝒲_k`) untouched; `prop:deficit` (iii) cites `thm:support` only for
monotonicity, which holds on both readings; line 415 ("whose value is the
unrestricted one") untouched and now consistent; line 164 (CDH 2009)
untouched.

---

## 4 · The proof replacement, as applied

The printed converse was:

> "with deterministic observations the realized observation path is fixed
> by the declared sequence, so `V_k(b) = max_seq Σ_{x surviving} b(x)`; if
> `supp(b) ∉ 𝒲_k` no declared sequence keeps every compatible branch, so
> each sequence loses at least one branch of mass `b(x) ≥ min_{x'} b(x)`"

That argument is invalid for a feedback policy: determinism makes the
observation path determined *by the policy and the initial state*, not
fixed in advance of them, and a policy is not a sequence. It is what made
the theorem false rather than merely mislabelled.

The replacement is an induction on `k` against the feedback recursion: fix
a policy `π` with first action `a`; for each observation `y` the posterior
support is `Post(supp b, a, y)` by the support identity; if all of those
lay in `𝒲^{fb}_{k-1}` then `supp(b) ∈ 𝒲^{fb}_k`, so for some `y` the
posterior support lies outside, and the induction hypothesis makes the
continuation of `π` after `(a,y)` lose a branch of positive mass; compose,
and every lost branch carries at least the minimum support mass.

---

## 5 · Status of the three directives

* **`2^{|supp b|}`: done** (§1), at the paper's bound, on the corrected
  family.
* **Three-symbol fix: applied** (§3), exactly as drafted, with §4 reviewed
  first and `prop:deficit` (ii) left untouched.
* **Proof replacement: accepted and applied** (§4), and recorded as a
  corrected error rather than a notation change.
* `prop:deficit` (i): out of scope since v24, documented, unchanged.
* Sperner: cited, not formalized, by decision, unchanged.

P3 totals: **11 result · 1 partial · 6 instance · 1 out of reach** — the
partial being `prop:antichain` (iii). `prop:freeze` moves from
"count at a weaker bound, on the defective family" (v18) to **proved at
the paper's bound on the corrected family** (v34), with its second clause
— the frozen value as a maximum over the *maximal* sets of the frozen
family — still open for `𝒮^adm_k` (it is proved for the old family,
`Vfam_prune_eq`, v21).

---

## 6 · Build state

`lake build` → **rc = 0, 43 jobs**, 40 imported modules, zero warnings,
zero `sorry`; verified by cloning `lean-audit-v4` at the pushed commit
into `/var/tmp` and building there.

Technical notes for the next turn: `by_contra` does not exist in this
layer (use `by_cases`); `List.filter` here is `Bool`-valued, so
`List.mem_filter` returns `decide p = true` and goals involving a filter
must be rewritten with an explicit equality before `change` will fire;
`List.erase` removes only the **first** occurrence, so `(a :: t).erase a`
is `t`, not `t.erase a`.

## 7 · Files

| file | status |
|---|---|
| `lean/Formalizations/P3_FreezeCount.lean` | new, green |
| `lean/Formalizations.lean` | 39 → 40 imports |
| `paper2_probabilistic_sufficiency_v12.tex` | **new** — the paper edit (v11 untouched) |
| `lean_README_v10.md` | new; supersedes v9 (43 jobs / 40 imports; corrected `prop:freeze` row) |
| `lean_audit_v34.md` | this file |
