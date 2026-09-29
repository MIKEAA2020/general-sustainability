# Version currency of the eleven papers — audited 2026-09-29

## Why this file exists

Paper 2 was assembled from `paper2_probabilistic_sufficiency_v9.tex` while v14 existed.
The user caught it. The check was then generalised to all eleven. **Three of the five
P2-group papers were built from stale sources.** This file records what was wrong, what
was corrected, and what remains open. No file was overwritten: each correction is a new
version.

## The correction

| my paper | source used | latest source | drift | words recovered | new labels |
|---|---|---|---|---|---|
| paper02 `psuff` | `_v9` | **`_v14`** | 5 versions | +641 | `rem:feedback-strict` |
| paper03 `comp`  | `_v9` | **`_v20`** | **11 versions** | **+1,967** | `prop:beliefcells`, `prop:redesign`, `fig:hierarchy`, `fig:trajectories` |
| paper05 `ebc`   | `_v9` | **`_v13`** | 4 versions | +540 | — |

Re-assembled as `paper02_..._v11.tex`, `paper03_..._v11.tex`, `paper05_..._v11.tex`.
**No label was dropped in any lineage**, so each new version is a content superset of the
old. The v10 files are retained.

## Verified NOT drifted

- **paper01 `obstr`** — source `fam/obstr_v57.tex`. The rewrites lineage
  (`paper2_obstruction_calculus_*`) stops at v56, so v57 is ahead of it. Current.
- **paper04 `minimax`** — `fam/minimax_v11.tex` and
  `paper rewrites/latex/minimax_dual_certificates_v12.tex` are **identical** (6,107 words,
  same labels, no Lean). Current.
- **paper07** — source `diffs/p5_v47.tex`. (`v47_blinded_NatSustain` is a blinded variant
  that deliberately drops `fig:cod`, `fig:rho-scan`, `fig:screen`.)
- **paper09 `arv`**, **paper10**, **paper11 `e1`** — sources match the latest available.

## What the stale versions were missing, substantively

Not cosmetic. The v9 -> v14 `psuff` gap included:

1. **A mathematical correction.** v14 distinguishes the feedback viable-set recursion
   `\mathcal{W}^{fb}_k` from the blind recursion `\mathcal{W}_k`, with
   `rem:feedback-strict` noting the inclusion is strict in general. My v10 conflated them.
2. **A repaired proof.** v10's converse for the value-one characterisation read "with
   deterministic observations the realized observation path is fixed by the declared
   sequence" — a hand-wave. v14 replaces it with a proper induction on `k`.
   (`psuff` v14 says the Lean support identity is machine-checked "on the repaired reading
   of Theorem `thm:support` recorded in Remark `rem:feedback-strict`.")
3. **The completed mechanized layer.**

## The mechanized layer — the largest thing the stale sources omitted

Three of the current sources carry a Lean 4 claim; **ten of my eleven papers carried no
Lean mention at all**, and none mentioned machine-checking.

- `comp_v20`: the Farkas core underlying the exact primal-dual witnesses is **proved** in
  Lean 4 (54 modules, 60 build jobs, no axioms, no admitted gaps); the soundness direction
  — the one the certificates use — from the ordered-field interface alone. The converse is
  not proved there and is not used.
- `ebc_v13`: Sections `hamming`-`deadline` formalized in Lean 4, no axioms, no admitted
  gaps, no computer-algebra oracle; derived from the ordered-field interface alone.
- `psuff_v14`: support identity, freeze count and its frozen value, and rationality of the
  α-vectors, machine-checked. **One bound remains cited rather than formalized**: the
  Sperner bound of `prop:antichain` (iii).

Papers 2, 3 and 5 now carry these claims.

## Open, and the biggest single finding

**Paper 1's central results are already machine-checked and the paper does not say so.**

`lean/Formalizations/P1_Obstruction.lean` — 29,054 characters, **58 theorem/lemma/def,
0 axioms, 0 `sorry`**, importing only `Formalizations.Prelude`. It declares
`post`, `possible`, `commonAdm`, `beliefSafe`, `preOp`, `Wk`, `preOp_mono`,
`Wk_antitone`, `Wk_descending`, `SafeUnderPi`, `finite_horizon_sound`, `tree_sound`,
`finite_horizon_complete`, `Blocked`, `blocked_iff`, `commonSafe`.

The mapping onto paper 1's labelled results is direct:

| Lean declaration | paper 1 result |
|---|---|
| `finite_horizon_sound` / `finite_horizon_complete` | `thm:finite-horizon` |
| `commonSafe`, `Blocked`, `blocked_iff` | `thm:common-action` |
| `Wk_antitone`, `Wk_descending` | `def:kernel` (the kernel iteration) |
| `preOp_mono` | `prop:monotone` |

Likewise `Minimax_Dual.lean` (13,427 chars, 26 declarations, 0 axioms, 0 `sorry`) sits
under paper 4, which also does not mention it.

For the top-journal bar — *substantial methodological development* — a machine-checked
soundness and completeness theorem for the paper's central recursion is about as strong an
asset as these papers have, and it is currently invisible in the two papers it belongs to.

**Not yet done, deliberately.** I have not added these claims to papers 1 and 4. Doing so
requires first confirming the modules actually build and that each named declaration means
what the mapping above assumes. Writing the claim before the check is exactly the failure
that produced the retracted "tension" argument.

## Caveat — RETRACTED

~~`P1_AssessmentSeparation_v5.lean` (paper 6) has 1 `sorry`, an admitted gap.~~

**This was a false positive and is retracted.** The single grep hit for `sorry` is line
108 of the file, which is a *comment* reading "Every theorem is fully proved; there are
no `sorry`s and no extra axioms." A grep hit is not evidence. The claim was made from an
unexamined grep, the same failure family as the retracted "tension" argument.

Corrected by the verification pass below: paper 6's module is clean.


---

## Verification pass on the Lean layer — 2026-09-29

Every mechanized claim above was **checked before being written into any paper**.

### Method

Lean 4.14.0 was installed (elan), the `lean/` project fetched from the remote
(`lakefile.toml` plus 67 modules) and built.

### Result 1: the project builds

`lake build` → **60/60 jobs, exit 0**. This matches the "54 modules, 60 build jobs"
figure the sources claim.

### Result 2: no admitted gaps, established three independent ways

1. **`#print axioms` on the named declarations** (the only reliable test — in Lean an
   unfinished proof surfaces as the axiom `sorryAx` in the footprint of every declaration
   depending on it):

   | declaration | axioms |
   |---|---|
   | `finite_horizon_sound` | none |
   | `finite_horizon_complete` | `Classical.choice` |
   | `tree_sound` | none |
   | `blocked_iff` | `propext`, `Classical.choice`, `Quot.sound` |
   | `Wk_antitone`, `Wk_descending`, `preOp_mono`, `commonSafe` | none |

   `sorryAx` appears nowhere. The three named axioms are Lean's standard classical
   axioms, not gaps.

2. **Comment-stripped source scan** over all of `Formalizations/`: **zero** `sorry`,
   `admit`, or `axiom` declarations. The only modifier found is `noncomputable` (20
   occurrences), which marks a definition as using classical choice and is not a gap.

3. **At scale**: 170 declarations of `P1_AssessmentSeparation_v5` checked —
   `sorryAx` count **0**; only `propext`, `Quot.sound`, `Classical.choice` appear.

### Result 3: scale of the layer

**1,237** theorem/lemma declarations across 61 modules, including 199 in
`P1_AssessmentSeparation_v5`, 33 in `P1_Obstruction` (plus the `HiddenMode` section),
and 21 in `Minimax_Dual`.

### Result 4: fidelity — the formalization does apply to paper 1 as it stands

The formalization's declared source of record is `paper2_obstruction_calculus_v53`;
paper 1 descends from `obstr_v57`. Comparing them: v53 has 73 labels, paper01 has 74,
**and the only difference is `worked-case`, added by me this session**. Nothing dropped,
and `thm:finite-horizon`, `def:kernel`, `thm:common-action`, `prop:monotone`,
`thm:static-complete`, `prop:selector` are present in both.

### Scope limits, recorded in the papers, not omitted

1. **The continuous-time results are NOT formalized.** The header of
   `P1_Obstruction.lean` says the Dini-derivative arguments, exit certificates and timing
   bounds "live in an analysis setting outside a dependency-free Lean layer." What is
   formalized is the discrete core: Section 3.1 (finite systems, backward recursion over
   beliefs), the Section 7 one-step characterization, the Section 3.2 common-action
   obstruction in discrete/infinite-horizon form, the Section 4.1 certification theory,
   the Farkas robustness margin, the hidden-mode conflict example, and kernel monotonicity.
2. **Completeness is with respect to policy trees, not stationary policies.**
   `finite_horizon_complete` returns a `PolicyTree`, a history-dependent object. Where a
   paper asserts a stationary policy suffices, that rests on the hand proof.

### Written

- `paper01_obstruction_calculus_v60.tex` — new subsection **3.8 Mechanized verification
  of the discrete core**, with the declaration-to-result table, the axiom evidence, and
  both scope limits.
- `paper04_minimax_dual_certificates_v13.tex` — new section **Mechanized verification**
  (inserted before References; that paper has no Conclusion section).

Neither claim was written before the checks above had run.
