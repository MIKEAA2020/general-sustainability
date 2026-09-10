# SCAN PROCESS — how the master→revision cross-check was automated & reproduced

This note documents **how** the scan was performed (the ten improvements of the review), what tools were
used, and what assumptions were made, so the trace is reproducible and transparent.

## 1. Automated line-level mapping (item 1) & formal traceability matrix (item 2)

- `trace.py` reads two files — `MASTER_joint_assessment_and_implementation_plan.md` (source of truth) and
  `IMPLEMENTED_revision_ECOMOD.md` (the deliverable) — and extracts **every** numbered/actionable item
  from the master's Parts 12A–12G (the `### 12X` headings, the `\d+\.` sub-items under them, and the
  `**12G.N — …**` bolded items).
- For each item it scores **coverage evidence** = how many of the item's distinctive **numeric tokens**
  and **domain keywords** appear in the revision, plus whether the literal ID string appears.
- It writes `SCAN_traceability_matrix.md` (human table) and `SCAN_coverage.csv` (machine-readable).
  The **Status** column is *curated/verified*, not auto-inferred; the `#num`/`#kw` columns are the
  automated detector. `partially`/`MISSING` are treated as **re-check triggers**, not verdicts.
- Result: **22 items**, 19 COVERED + 1 SUPERSEDED-num (12A.1) + 1 COVERED-RELABEL (12G.2) + 1
  COVERED-NOTE (12G.5). **No item is missing.**

## 2. Actionable vs informational (item 3)

`trace.py` classifies each item: **ACTIONABLE** (a to-do; detected by "Action:"/imperatives) vs
**INFO-preserve** (a verified-correct background statement). This keeps the two kinds of claims
auditable separately: actionable items are checked for correct implementation; informational claims are
checked for continued truth or explicit supersession.

## 3. Independent numerical re-computation (items 4 & 5)

- `audit_basin.py`, `audit_numerics.py`, `audit_s0.py`: re-run the **original** model's basin-shrinkage,
  the six scenarios, and the attractor; and run the **corrected** `(1‴)` S0 to establish its structure.
- `mask_rk4.py` + `deficit_map.py`: converged-RK4 masking re-scan (supersedes the earlier Euler artifact
  and the "no masking" dead-end that only tested large deficits).
- `regression_test.py`: a committed regression test that re-runs every previously-reported quantity and
  flags CONFIRMED / CORRECTED / SUPERSEDED. All previously-reported numbers reproduce (0 non-CONFIRMED).
- Outputs: `SCAN_numerical_audit.md`, `SCAN_regression_report.md`.

**Key numeric result.** The corrected `(1‴)` S0 is a **one-sided boundary** (`A→A_max, P→b₀A_max/e`), not
the original model's unique interior attractor (`M*=0.740, P*=0.370`); consequently the master's
basin-shrinkage fraction and scenario endpoints are **original-model** quantities that must be
re-labelled and (for the corrected model) re-computed as a recover/collapse boundary.

## 4. Internal self-consistency (item 6)

`selfcheck.py` compares the revision against itself (abstract ↔ §10, claims table ↔ demonstrations,
number/label co-occurrence) and flags missing provenance. It caught the wrong "~8 % overshoot" (→ 15 %
of `b₀A₀`) and the missing original-model provenance labels — both then fixed in the revision.

## 5. Risk register (item 7)

`SCAN_risk_register.md` lists every unresolved / partially-closed item, its status, and what remains to
be done. The only genuinely open items are the corrected-model basin recomputation (R1) and the
corrected characteristic-equation/table/figures (R2) — both *computation*, both already written down as
required actions.

## 6. Version-control diff (item 8) — and the honest caveat

> There is **no git repository** in this workspace (`git status` → "not a git repository"). So a true
> VCS diff is not available. The substitute used here:
> - `SCAN_traceability_matrix.md` + `SCAN_coverage.csv` provide the **item-level** change ledger (every
>   master→revision mapping), which is the functional equivalent of "every change corresponds to a
>   master item."
> - Any future edit should `git init` + commit the master and the revision separately, then iterate:
>   `git diff` on the revision, and confirm every hunk maps to a row in the traceability matrix. **Not yet
>   done (no repo); recommend doing it before submission.**

## 7. Peer / external review (item 9)

Not performed here (the agent cannot call an independent model). **Recommend a second reviewer** focused
on (a) the corrected-S0 one-sided-boundary finding (R1), (b) the original-model//corrected-model
provenance labelling, and (c) whether the "narrow, deficit-limited masking" framing is too conservative
or too generous versus the master's original demonstration.

## 8. Assumptions

- The **master** is the source of truth for *what must be implemented*; the **revision** is the
  deliverable being verified. No prior deliverable (reviews, root-cause, joint assessments) is treated as
  the target.
- "Original model" = the manuscript's gross-depletion, `M`-in-gha, `B=bM`, 2-D model. "Corrected /
  `(1‴)` model" = the unified stock–flow model in the revision.
- NUMBERS: the master's original-model numerics are reproduced but are **not** properties of the
  corrected model unless re-computed; that distinction is the single most important assumption in the
  scan and is why 12A.1/12G.7 are labelled `SUPERSEDED-num` and 12G.2 is labelled `COVERED-RELABEL`.
