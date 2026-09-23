# v45 — Track-A sweep implementation (A1 + A4 of the follow-up roadmap v2)

**Input:** `paper2_obstruction_calculus_followup_roadmap_v2.md` (Track E,
priority 1). **Revision produced:** `paper2_obstruction_calculus_v45_Automatica_routes.tex`
+ `.pdf` (17 pp.; v44 untouched). Supplementary unchanged (v44: S1–S3 carry
the three-methods comparison and the silent-certificates example, both
verified present).

## A1 — review-of-record re-diff (v31 dispositions → v44)

All fifteen FIXED dispositions of `paper2_v31_verification_report.md`
were spot-re-verified against the v44 source: §1.2 checkability tags
(two *finitely checkable*, two *closed-form*), the reproducible-model
paragraph (§8), the static-observation reduction and one-step converse
framing (§7), the implementable blind-window class (H4.2/§3.5 template
paragraph), `𝒜_N` definition, `D_ε` defining formula (§2.4), the
belief-history convention, and the ≈3.3 truncation. The REJECTED claims
(MSC typo, "ObservationAmin", §6.3 cross-references) remain correctly
rejected. No drift found.

## A4 — evidence-gap sweep, per-gap disposition (v44 basis)

| Item | Status at v44 | v45 action |
| --- | --- | --- |
| Gap 1 + M3 (critical) | **OPEN — false archival claim.** Zenodo 22545740 is the assessment paper's record ("The Limits of Compensatory Aggregation"; files: v22-era PDF + suppl v3). It contains no coverage-audit code, yet §8 and the declarations cited it as the script's archive; the reference list cited the same record under the assessment paper's *new* title | **FIXED (3 sites):** §8 and Code availability now cite the public repository mirror (folder with `paper2_coverage_audit.py`); the companion reference now cites the live, correctly titled figshare deposit (10.6084/m9.figshare.33764023). Zero occurrences of the stale record remain |
| M1 | Table 1 hand-typeset, counts unverifiable | **CLOSED with evidence:** `paper2_coverage_audit.py` executed — output: 48 cells, 42 nonviable (30 common-action + 12 timing, 0 uncovered), and the regenerated LaTeX table matches Table 1 symbol-for-symbol (all three rows); `fig_p2_coverage.png` regenerated. The declarations now state the verbatim-regeneration fact |
| Gap 2 | CLOSED (abstract: "checkable in the common-action, fibre-certification, and finite-horizon forms and analytic drift-and-timing conditions elsewhere"; §3.5 finite/template split) | verified, no action |
| Gap 3 | CLOSED (Supplementary S2: the two-floor system worked through barrier ("no barrier found" verdict semantics), estimation-tube, and obstruction (Farkas λ = (1/2, 1/2), margin 0.1) side by side) | verified, no action |
| Gap 4 | OPEN (Helly hypotheses undefended at the boundary) | **FIXED:** Scope sentence added after Proposition (sparse common-action witness): convexity is what bounds the witness by m+1; beyond convex safe-control sets neither the bound nor finite checkability survives in general |
| Gap 5 | OPEN (§9 has the theory; no worked V_k instance) | stays open → generalization D1 |
| Gap 6 | PARTIAL (finite classes + hidden-regime closed form; continuous classes = Open Problem) | stays open → companion item B6 |
| Gap 7 | CLOSED (§3.7 oracle-recourse proposition + three-branch instance; S3/A.3 discrete instance where every one-step certificate is silent) | verified, no action |
| Gap 8 | PARTIAL (Calibration paragraph present — parameters ↔ stock-assessment quantities; no second 2-D instance, no real-data illustration) | partially closed; 2-D case study stays open (roadmap) |
| Gap 9 | CLOSED (§1.4 reworded exactly as prescribed) | verified, no action |
| Gap 10 | OPEN (no quantitative partial converse) | stays open → companion item B7 |
| M2 | OPEN (uncited behavioral superlative) | **FIXED:** "the one governance structures can omit" → "lies entirely at the governance structure's discretion" |

## Build verification (v45)

Tectonic 0.15.0, clean; 17 pp. PDF probes: zero occurrences of the stale
Zenodo record; mirror URL present at both code sites; figshare DOI in the
reference list; the softened M2 phrasing and the Helly Scope sentence
render. Figures: all six + the regenerated coverage heatmap.

## What remains open (tracked in the roadmap)

B6 (timing-instantiation LP theorem), B7 (partial converse), Gap 5 worked
belief-state instance (→ D1), Gap 8's second two-dimensional case study,
then the companion paper (B1–B5) and the unification track. No theorem
status is created or changed by this addendum.
