# Audit v4 — "If I adopt v3/v4, what in the paper text changes?"

## Short answer: **nothing.**

No paper cites v1, v2, or any theorem name inside them. No paper even
mentions Lean. Three independent checks:

### Check 1 — identifier sweep (all 10 latest papers)

Tokens searched: `lemB_reject`, `lemB_ii_only_linear`, `CollapseSafe`,
`ThetaSubAdm`, `ThetaMidAdm`, `Theta1Adm`, `P1_AssessmentSeparation`,
`lake build`, `Formalizations`.

**Result: 0 hits in every `.tex` file.** All hits were in `lean/README.md`
and `worklog.md` — neither is a paper.

### Check 2 — no counts in the papers

`395` → 0 hits. `ten modules` → 0 hits. `sorry` → 0. `no axioms` → 0.

### Check 3 — no paper names the prover

Only one case-insensitive `lean` match across all papers, and it is the
English word **"clean"** (`paper1_assessment_separation_v62.tex:1900`:
"form clean off-diagonal bands mirroring the diagonal ladder"). No paper
references Lean, the layer, or the toolchain.

## The substantive check (more important than the mechanical one)

A clean grep could still hide a *conceptual* dependency: if the paper
presented the collapse convention as a **derived theorem**, then v4's
re-characterisation (it is a **stipulation**) would contradict the paper and
force a text edit.

It does not. The paper's own Lemma B (`paper1_assessment_separation_v62.tex`,
~line 1594) reads:

> **Lemma B (collapse convention).** *For every θ < 1 member, any tube value
> λᵢ ≤ 0 rejects the plan…* The geometric mean is 0 there; CES with θ ≤ 0 is
> undefined there; **for θ ∈ (0,1) the convention is the family's defining
> property.** The θ = 1 member alone compensates across collapse…

The paper calls it a **convention** and a **defining property**. So it was
**v1 that was out of step** — its two theorems implied the convention had
been derived. Adopting v4 moves the layer *toward* the paper, not away from
it. There is no theorem name, citation, or number in any paper to update.

## What DOES need updating — 2 files, neither is a paper

| File | Line | Why |
|---|---|---|
| `worklog.md` | 2591 | Names the removed theorem: "`lemB_ii_only_linear`: every θ<1 member rejects the plan (both conventions carry `CollapseSafe`, which fails)." |
| `lean/README.md` | 19 | Slot table row for **P1-AS** points at `Formalizations.P1_AssessmentSeparation` |
| `lean/README.md` | 66 | "ten modules (395 theorems total…" — see counts below |
| `lean/README.md` | 80 | Theorem-index row named `P1_AssessmentSeparation` |

`worklog.md` is a state reference you listed, so it should be corrected even
though it is not a paper — it is the only place the removed name is cited.

## Counts are unchanged — verified, not assumed

| Quantity | v1 (current) | v4 adopted | Change |
|---|---|---|---|
| Theorems in the P1-AS module | 199 | **199** | none (removed 2, added 2) |
| Theorems layer-wide | 395 | **395** | none |
| `lake build` jobs | 13 | **13** | none |
| Modules | 10 | 10 | none |

Verified by building with v4 **replacing** v1 and v2 retired:
`Build completed successfully (13 jobs)`, rc=0, 5 s.

⚠️ The counts only hold if v1 and v2 are **retired**. Keeping v1 alongside
v4 gives 11 modules / 594 theorems, and the README would be wrong.

## v4 supersedes v3

v4 = v3 plus one paragraph that closes the root cause properly. The paper
justifies the convention **analytically** ("geometric mean is 0 there; CES
with θ ≤ 0 is undefined there"), but the layer is interface-level over an
abstract `OrdField K` with an abstract power interface `pw` — it has no
notion of an undefined value and so **cannot express the paper's
justification**. `CollapseSafe` is therefore a **bridging stipulation**
standing in for an analytic fact the interface abstracts away.

That is not a defect, and not an omission. But it should be said, because
the alternative readings are both wrong: that the layer derived something it
merely assumed (v1's error), or that the layer has formalized the paper's
argument for the convention (it has not, and cannot at this interface).

**Verification:** drop-in build rc=0, 13 jobs, 199 theorems; namespace
`Formalizations.P1SepV4`; v1 untouched.

## Deliverables

```
lean_versions/Formalizations/
    P1_AssessmentSeparation_v2.lean  additive shim (4.5 KB)
    P1_AssessmentSeparation_v3.lean  corrected module (160 KB)
    P1_AssessmentSeparation_v4.lean  + bridging-stipulation note  <-- adopt this
```

Activate: replace the v1 import in `lean/Formalizations.lean` with
`import Formalizations.P1_AssessmentSeparation_v4`, and retire v1 + v2.
