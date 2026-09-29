# Audit addendum v2 — verdict on option "C (strengthen)"

Companion to `LEAN_AUDIT_v1.md`. Answers the question: could
`lemB_ii_only_linear` be strengthened so the rung conditions do real work?

## Verdict: **No — and the reason is substantive, not incidental.**

A genuine strengthening is not available. Any attempt would either be false
or would re-import `CollapseSafe` as a hypothesis, i.e. exactly the
decorative move to be avoided. Three independent reasons:

### 1. `pw` is never constrained where it would have to be

Every law the layer assumes of `pw` is guarded by nonnegativity:

```lean
hnn   : ∀ x, 0 ≤ x → 0 ≤ pw x
hlaw  : ∀ x, 0 ≤ x → pw x * pw x = x
hmono : ∀ a b, 0 ≤ a → a ≤ b → pw a ≤ pw b
hanti : ∀ a b, 0 < a → a ≤ b → pw b ≤ pw a
```

`CollapseSafe` is precisely a claim about **possibly-negative** tube values
(`0 < 1 + p.sᵢ`). So at a collapsed coordinate the rung inequality evaluates
`pw` at an argument the interface says nothing about. Nothing can be derived
there.

### 2. One aggregate inequality cannot force two coordinates

The rung condition is a single scalar test,
`1 ≤ w₁·pw(λ₁) + w₂·pw(λ₂)`, whereas `CollapseSafe` demands **both**
`0 < λ₁` **and** `0 < λ₂`. A large second coordinate compensates a collapsed
first one. The shapes are mismatched, not merely under-specified.

### 3. The layer already contains the countermodel

At `z₀ = (1/2, 1/2, 5/2)` the plan FAST has tube values `λ₁ = −1/2` and
`λ₂ = 7/2`; at equal weights `λ₁/2 + λ₂/2 = 3/2 ≥ 1`, so the rung condition
is satisfied while a coordinate has collapsed. `lemB_ii_linear_witness`
(line 3521) proves exactly this:

```
1 + (1/2 − 2) ≤ 0   ∧   Theta1Adm (1/2) (1/2) (.det .fast) z₀   ∧   ¬ CollapseSafe (.det .fast) z₀
   ↑ collapsed              ↑ rung accepts                            ↑ convention fails
```

Note also that `Theta1Adm` (line 1892) does **not** contain `CollapseSafe`,
while `ThetaSubAdm` / `ThetaMidAdm` do — which is the structural fingerprint
of an extra stipulation, not a derived fact.

**Conclusion:** conjoining `CollapseSafe` into the θ < 1 admissibility
definitions is the *correct* modelling choice. The defect is not the
definition — it is that a theorem was written whose proof is `.1`, creating
the false impression that the convention had been established by argument.

## What was built instead (genuine, non-decorative, useful)

Because the convention is an **independent stipulation**, the honest
content-bearing statement is *non-redundancy*: the rung condition does not
imply the collapse convention. That is provable from what the layer already
has, it says something real, and it is useful — it fails if anyone later
"simplifies" `ThetaSubAdm` by dropping `CollapseSafe` on the assumption the
rung algebra already covers it.

**New file (additive; v1 untouched):**
`lean_versions/Formalizations/P1_AssessmentSeparation_v2.lean`

- `collapse_convention_not_implied_v2` — exhibits `a`, `z` with
  `Theta1Adm (1/2) (1/2) a z ∧ ¬ CollapseSafe a z`.
- `collapse_convention_strict_v2` — hence the θ = 1 rung condition does not
  entail `CollapseSafe`; the conjunct is a strict strengthening.

Both are built on `lemB_ii_linear_witness`, which does the real work.

## Verification

| Check | Result |
|---|---|
| `lake build` (pinned v4.34.1) | **rc=0**, 14 jobs — `✔ Built Formalizations.P1_AssessmentSeparation_v2` |
| Warnings introduced by v2 | **none** (all remaining warnings are v1's) |
| `#print axioms` on both theorems | `[propext, Classical.choice, Quot.sound]` — kernel axioms only, **no new axioms** |
| v1 file modified? | **No** — `git status` shows only the new file + scratch import line |

To activate: add `import Formalizations.P1_AssessmentSeparation_v2` to
`lean/Formalizations.lean` (a one-line, purely additive change).

## Still open — your call

The v2 module *adds* the honest theorem but does not remove the two vacuous
ones (removal would mean editing v1, which I have not done):

- **A** — delete `lemB_reject` + `lemB_ii_only_linear`. Both are unreferenced,
  so removal cannot break the build. I'd ship this as a duplicated v2 module.
- **B** — leave them, correct their docstrings so they stop over-claiming.
- **Neither** — keep the additive v2 only.
