# Audit v3 — root-cause fix for the vacuous Lemma B theorems

You asked to prioritise **honesty and root cause** over a shallow quick fix.
This records what the root cause is, and what was done about it.

## The root cause (not the symptom)

The symptom is two theorems whose proofs are `.1`. Deleting them — the quick
fix — removes the symptom and leaves the actual problem in place.

The root cause is a **category error about the collapse convention**:

> The statement "for θ < 1, a tube value `λᵢ ≤ 0` rejects the plan" is a
> **stipulation** of the family. It is correctly encoded by conjoining
> `CollapseSafe` into `ThetaSubAdm` / `ThetaMidAdm`. It is **not** a result
> that follows from the rung algebra — and it cannot be (proof in
> `LEAN_AUDIT_v2.md`).

The layer then wrote theorems that *look like* they derive the convention
while in fact projecting the conjunct that defines it. So the index reads as
though Lemma B(i) were proved, when the convention had only been assumed.
That misrepresentation — not the two dead theorems — is the thing to fix.

A pure deletion would make it worse in one respect: it would strip the two
signposts without saying why the conjunct is there, leaving the next reader
to assume it is redundant and "simplify" it away. Which would silently change
the θ < 1 family, not merely tidy it.

## What v3 does

**`lean_versions/Formalizations/P1_AssessmentSeparation_v3.lean`**
(self-contained copy of v1 in namespace `Formalizations.P1SepV3` — v1 is
untouched and both can coexist).

1. **Removes both vacuous theorems.** `lemB_reject` (literally `And.left`
   with a phantom `{rung : Prop}`) and `lemB_ii_only_linear` (`.1` of a
   definitional conjunct). Both were unreferenced, so removal is
   build-safe.

2. **States the stipulation where it is made.** A block above
   `ThetaSubAdm` / `ThetaMidAdm` now says explicitly that `CollapseSafe` is
   conjoined *rather than proved*, and gives the two reasons (the `pw`
   interface is guarded by `0 ≤ x`; one aggregate inequality cannot
   constrain two coordinates).

3. **Supplies the missing justification as real content.** Two new theorems
   replace the two removed ones:
   - `collapse_convention_not_implied` — exhibits a plan and state where the
     rung condition holds but `CollapseSafe` fails, witnessed by
     `lemB_ii_linear_witness` (which does the actual work).
   - `collapse_convention_strict` — hence the conjunct is a strict
     strengthening, not a redundancy.

   These are *load-bearing*: they fail if anyone drops `CollapseSafe` from
   the θ < 1 definitions on the assumption that the rung algebra covers it.
   That is the useful content the vacuous pair pretended to have.

4. **Stops the index over-claiming.** The module header's Lemma B bullet now
   separates the conventional half from the proved half, and each removal
   site carries a `/-! Removed in v3 -/` note recording what was there and
   why, so the history is auditable rather than silently erased.

## Verification

| Check | Result |
|---|---|
| `lake build` (v1 + v2 + v3 together, pinned v4.34.1) | **rc=0**, 15 jobs |
| Theorem count v1 vs v3 | **199 vs 199** — removed 2, added 2; nothing silently lost |
| Vacuous declarations remaining in v3 | **0** (only explanatory comments) |
| New theorems' axioms | `[propext, Classical.choice, Quot.sound]` — kernel only |
| Warnings introduced by v3 | **none**; the v1:1983 `w1`/`w2` warning is **gone** with the theorem |
| v1 modified? | **No** — `git status` shows only the two new files + scratch import lines |

Behaviour is unchanged: no theorem was weakened or strengthened, no
definition altered. Only presentation and the two dead declarations changed.

## Which file to adopt

- **v3** — the definitive corrected module. Self-contained; drop v1 and v2.
  Choose this if you agree the convention should be documented as a
  stipulation.
- **v2** — the minimal additive shim (imports v1, adds the two genuine
  theorems, removes nothing). Choose this if you want the new content
  without swapping the module.

They do not conflict (v2 lives in `P1Sep`, v3 in `P1SepV3`), but v3
supersedes v2.

To activate v3: add `import Formalizations.P1_AssessmentSeparation_v3` to
`lean/Formalizations.lean`, and retire the v1 import once you are satisfied.

## Deliverables in this workspace

```
LEAN_AUDIT_v1.md                     latest editions + build matrix + suspects
LEAN_AUDIT_v2.md                     verdict on option C (not genuine)
LEAN_AUDIT_v3.md                     this file - root-cause fix
lean_versions/Formalizations/
    P1_AssessmentSeparation_v2.lean  additive shim (4.5 KB)
    P1_AssessmentSeparation_v3.lean  corrected module (160 KB)
playground_checks_v1.lean            verified paste-ready snippets
lean-bootstrap.sh                    re-provision the toolchain off-snapshot
```
