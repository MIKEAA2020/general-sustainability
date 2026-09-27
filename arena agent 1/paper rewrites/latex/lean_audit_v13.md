# Lean audit v13 — P3 batch 4: `prop:noisyprobe`, `prop:freeze`, and the corrected README

**Target:** `general-sustainability` → `lean/`. **Branch:** `lean-audit-v4`
(additive). **Toolchain:** `v4.34.1`.
**Build:** `lake build` → **rc = 0, 21 jobs**, zero warnings.
**Zero `sorry`** project-wide (verified: the four textual `sorry` matches are
all inside comments reading "*there are no `sorry`s*").

New module **`lean/Formalizations/P3_Freeze_Noisy.lean`** (10,537 B).

| Result | Status |
|---|---|
| `prop:noisyprobe` | **closed** (generalizable content: mixture + three-level range) |
| `prop:freeze` | **closed except the literal drop count** (nesting, antitonicity, `2^{|supp b|}` bound, finite range) |
| `lean_README_v2.md` | **issued** — resolves the slot table to *results* |

---

## `prop:noisyprobe` — what generalizes and what does not

The paper's statement is a closed form on the *declining instance*
(specific drifts `9/10`, `−11/10`, specific probe horizon). What survives
abstraction:

- a single probe gives a **two-outcome reading** — correct w.p. `1−ε`,
  flipped w.p. `ε`;
- the branch values are **indicators**, `v_c, v_f ∈ {0,1}`;
- the flipped reading is no better than the correct one, `v_f ≤ v_c`;
- hence `(1−ε)·v_c + ε·v_f` realizes **exactly three levels** `{0, 1−ε, 1}`.

**`three_levels`** proves the range. The point worth flagging: the fourth
a-priori combination `(v_c, v_f) = (0,1)` — *the correct reading dies but
the flipped one survives* — is eliminated **by the nesting hypothesis**, not
assumed away. That is precisely why there are three levels and not four, and
it is the one step the paper leaves to the reader ("the correct reading acts
under drift 9/10, the flipped reading under −11/10"). Also proved:
`mixture_nonneg`, `one_sub_nonneg`.

`three_levels` depends on **only `propext`** — no choice, no quotients; it
is finite case analysis on two Booleans.

The instance-specific thresholds (`z_p ≥ 1`, `z_p ≥ 1 + 11/10·(k−t_p)`) are
arithmetic about the declining trajectory, not structure, and are not
formalized.

## `prop:freeze`

> `S_{ℓ+1} ⊆ S_ℓ`; hence `V_ℓ(b)` is non-increasing and stabilizes after at
> most `2^{|supp b|}` strict decreases.

Closed:

| Lemma | Content |
|---|---|
| `survK` | survival over `k` steps under a schedule, adversarially in the disturbance |
| `survK_mono_succ`, `survK_mono` | surviving longer implies surviving shorter |
| `Survivable_succ` | the nesting, at the level of sets |
| `Sfam_nesting`, `Sfam_mono` | **the nesting `S_{ℓ+1} ⊆ S_ℓ`, at the level of families** |
| `Vfam_antitone` | **`V_ℓ(b)` is non-increasing in the horizon** |
| `subsetsOf_length` | `\|𝒫(l)\| = 2^{\|l\|}` |
| `Sfam0_card_le` | `\|S_0\| ≤ 2^{\|supp b\|}` |
| `Vfam_finite_range` | every `V_ℓ(b)` is `b(S)` for some `S ∈ S_0` |

Two design notes:

- **Subsets are `List X` (elements included), not `X → Bool`.** This removes
  every `DecidableEq X` obligation, which matters because `X` is an
  arbitrary type.
- **`survK` is `Prop`-valued, not `Bool`-valued.** The first attempt used
  `Bool` and immediately collided with the stdlib (`Bool.and_eq_true` is not
  an iff here, `List.all` lemmas unreliable). As a `Prop`, horizon
  monotonicity is a two-line induction. This is the same lesson as v8's
  "`Mass.ext` does not exist": in this dependency-free layer, prefer
  propositions over decidable booleans.

**Not closed: the literal count of strict decreases.** It follows from
`Vfam_finite_range` plus an injectivity argument — for an antitone sequence
the map from a strict-drop index to the post-drop value is injective — but
that needs `Nodup`/counting machinery over a classically filtered list. The
range bound is the substance; the count is bookkeeping on top. Flagged
rather than faked, per the standing instruction.

## `lean_README_v2.md` — the coverage claim, corrected

v10 §6 flagged that `lean_README.md` is imprecise. Having now read it in
full, the problem is worse than I described. Its theorem index says:

> `P3_ProbSufficiency` | `thm:recursion` expectation-kernel operator laws
> (monotone, constants, monotone iterates); `thm:agree`'s pointwise-ceiling
> core | **done**

That is the misleading claim. `P3_ProbSufficiency`'s four theorems
(`Φ_mono`, `Φ_const`, `Φ_le_const`, `iterΦ_mono`) are generic laws about an
abstract kernel `Φ`; they are **not** `thm:recursion` and they are **not**
`thm:agree`'s core. Labelling them so makes the index assert coverage it
does not have — exactly the failure mode the v10 critique warned against,
and worse than a mere omission because it is an affirmative claim.

`lean/README_v2.md` (pushed as
`arena agent 1/paper rewrites/latex/lean_README_v2.md`) fixes this:

- it **splits** each entry into *result* vs *machinery* vs *instance*, so
  "done" can no longer be read as "the numbered result is formalized";
- it corrects the `P3_ProbSufficiency` row to *machinery — generic kernel
  laws, attached to no numbered result*;
- it adds the four new P3 modules with **per-result** resolution for all 18
  P3 results, cross-referenced to the audit that closed each;
- it adds an explicit **"How to read the index"** section stating that no
  paper in the family claims formal verification, and that coverage is a
  property of the verification layer, not of the papers.

Per the standing never-overwrite rule, `lean_README.md` is untouched; v2 is
a new file.

## Coverage — final state for P3

| Status | Count | Results |
|---|---|---|
| **Formalized (complete)** | **7** | `thm:recursion`, `thm:lattice` (i), `prop:dr` (i), `prop:pathdeficit`, `prop:deficit` (i)(ii)(iii), `prop:degen`, `prop:noisyprobe` |
| **Partial** | **4** | `thm:support`, `prop:antichain`, `prop:pl`, `prop:freeze` |
| Formalizable, not done | **0** | — |
| Instance-level | 6 | `cor:closed`, `thm:parametric`, `thm:agree`, `thm:class`, `prop:learn`, `prop:additivelaw` |
| Not formalizable | 1 | `prop:probecount` (mathematically verified, v10 §3) |

**The formalizable backlog is empty.** Everything remaining on P3 is either
instance-level (the Python verifier layer) or genuinely beyond `OrdField`.
Seven new modules were added across v8–v13 (P1 belief safety ×3, P3 ×4), all
building green with no `sorry` and no extra axioms.

## Suggested next steps

1. Move to another slot: the same result-vs-machinery audit applied to
   `P1_Obstruction`, `Minimax_Dual` or `Comp_Certification` would test
   whether the `P3_ProbSufficiency` pattern — machinery indexed as results —
   recurs elsewhere in the family.
2. Close the four P3 partials (`thm:support`'s identity first: it needs a
   disturbance weighting plus an `lsum` strict-positivity lemma).
3. Finish `prop:freeze`'s drop count (injectivity lemma).
