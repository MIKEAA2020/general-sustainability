# Cod Specification B — deep root-cause decomposition (2026-09-16)

## The mistake a shallow answer makes

Treating "Cod Spec-B" as one to-do produces exactly two shallow outcomes, both
wrong: scoring origin 2025 "because the data appeared", or launching the
200-rep T=71 run "because the pilot looked promising". The archive shows the
open item is three separate problems that were conflated; solving one while
the other two remain unidentified and unverifiable is the strategic error the
pre-registered sheets exist to prevent.

## What the archive says (measured, not recalled)

- O6 band-calibration (`o6_cod_band_calibration_20260913.json`): pooled cells
  are ALL T=33 (D1–D5 × {11.8, 33.8}); T=71 appears only as
  `T71_points = {D1_power_5pct: {s11.8: .9, s33.8: 1.0, n: 10},
  D5_specificity_5pct: {s11.8: 1.0, s33.8: 1.0, n: 10}}` with the note
  "aggregate archive only; full 200-rep T=71 remains registered (O5)".
- Pooled result: max mean power **0.4437 at band 0** — structurally below the
  0.80 adequacy target. A band sweep cannot create missing power, so the O6
  outcome "no band qualifies" is **pre-determined at T=33** and is not a
  statement about any other window length.
- The T=71 pilot is per-sigma: D1 h=1 power .9 (σ=11.8) / 1.0 (σ=33.8) at
  band 5%, i.e. the longer window buys D1 back — the *identification*-limited
  story. What it cannot resolve is **D2**, which is *inference*-limited at
  T=33 (truth ranks first in 75% of reps yet the comparator gate retains it in
  only 42%): whether D2's gates ease at T=71 is precisely the question only
  the 200-rep run can answer at resolution.
- SPECIFICATION_v4 (frozen 2026-09-10, LOCKED — "Issued 10 Sep 2026, before
  any synthetic series has been generated, fitted, or scored."):
  - §83: T=71 "**not** simulated in the core design; see §2b."
  - §96: T=71, σ = 0, 𝔰 ∈ {5, 30} "**declared but deferred**".
  - §237: T=71 is scoped to **D1 and D5** — "matching Specification B
    (1954–2024)". D2/D3/D4 were OOS by design at both lengths.
- The archived raw campaign (`sim_origins_20260913.csv`, 69,000 rows) is the
  exploratory one: 5 cells × 25 reps × 2 σ, 1,718 wall seconds ≈ 28.6 min.
  Scaling to 200 reps × 2 σ ≈ **3.8 hours** — inside the sandbox.

## The three root causes, and the disposition each forces

**A. Verifiability (status-quo data for origin 2025).** Resolved, on the
2026-09-16 web evidence: DFO's 2026 assessment exists; SSB ≈ 540 kt (range
420–700) reported 2026-04-02 (saltwire), quota 18,000 → 38,000 t; the 2026
assessment announcement 2026-05-11 (thefishingdaily). Public raw inputs are
delayed (CSAS), so the honest earliest scoring vintage is the **post-2026
assessment** — i.e. 2027, not now. *This subproblem dissolves on reading, not
on campaigning.*

**B. Statistical identifiability at the Spec-B window (T=71).** The binding
one. The encouraging pilot is per-sigma but says nothing about D2; deciding
whether Spec-B's window is informative requires the 200-rep T=71 D1/D5 run
(O5) at 200-rep resolution. That run is **registered but deferred by the
frozen sheet itself** — SPECIFICATION_v4 explicitly places T=71 outside the
core design. Executing it now, unamended, violates the pre-registered sheet;
executing it under an amendment is procedurally allowed but the sheet was
frozen for exactly this contingency (a promising pilot does not retroactively
argue for more resolution — that is data-driven design re-opening).

**C. Execution (scoring origin 2025).** Premature. The frozen workflow
resolves B first (band at T=71 via O5), then C scores with the adopted band.
Scoring C with the T=33 band is what a shallow "just score it" does; it would
attach a band calibrated to a different window to a verdict the sheet
declares band-versioned.

## Disposition (root cause, not quick fix)

- **B stays deferred, deliberately.** The T=71 200-rep campaign remains
  registered (O5) and is not launched in this pass. Triggering conditions,
  per the sheet's own amendment discipline: (i) a separate Spec-B
  pre-registered sheet is written that lifts T=71 into its core design
  (the Edwards sheet shows the pattern — a new sheet, never an edit), with
  §3a/§4 adopted as-is, and (ii) owner approval of that sheet. The 3.8-hour
  cost is then a registered execution, not a scope expansion.
- **C follows B.** After (and only after) the band at T=71 is adopted, origin
  2025 is scored — h=1 now (2025 vintage is archived), h=5 at the 2029 actual —
  exactly as the frozen Edwards workflow does post-campaign. Cod model-side
  inputs are archived; no M2-style data gap exists.
- **A is closed** (post-2026-assessment vintage).

## The one thing explicitly NOT done (the shallow fix)

Scoring origin 2025 with the T=33 band and calling Spec-B "done": it reads
tidy, it is cheap, and it is wrong — the band would belong to a different
regime, the D2 question would stay open underneath the headline, and the
verdict would carry N-levels computed against a window the sheet declined to
score. None of that serves the paper, the reviewers, or the record.

---

## Corrective addendum, 2026-09-16 (owner question: "is the missing data on the repo?")

**Correction.** This memo's phrase "the Spec-B input is not archived" was wrong in an
important way, and is put right here:

- **Spec-B's historical series IS archived**: `wave_e_cod/data/xtencam_table17_ssb.csv`
  — years **1954–2024 (n = 71)**, transcribed from Regular et al. 2025, Table 17
  (DFO CSAS ResDocs 2025_048), checkpoint-verified (2005 = 26, 2017 = 451,
  2024 = 342 kt), provenance locked in `wave_e_cod/data/SOURCES.md`. The frozen
  Spec-B figures in the manuscript were computed on exactly this file.
- What is NOT archived is only the **tail** the new origins need: `SSB_2025`
  (last training value for origin 2025; h=1 target for origin 2024), `SSB_2026`
  (h=1 target for origin 2025, per the sheet's "vintage following the 2026
  assessment" rule), plus 2024+ official landings if the ladder requires them.
- Public evidence that these values exist: the 2025 assessment coverage
  (atlanticgroundfishcouncil.ca, 2025-04-03: SSB ≈ 524 kt, "double the LRP")
  and the 2026 assessment coverage (saltwire.com, 2026-04-02: SSB ≈ 540 kt,
  range 420–700, quotas 18,000 → 38,000 t). Single numbers in the news, **not**
  the full published table — the archive ingests official tables with
  provenance (SOURCES.md pattern), never news numbers.
- Why they were not archived: the archive was built by transcribing official
  tables at companion-build time (the 2025 assessment, table ends 2024); the
  2026 assessment arrived after. New data enters only via the owner-gated
  ingestion pattern (cf. the Edwards `pumpage_2024_sidecar.json`), because
  SOURCES.md forbids pooling SSB vintages — a silent hand-edit could rewrite
  the series.
- Root cause of the misstatement: the memo answered "what does the ladder's
  default loader read" (`ncam_2016_table_a2.csv`, Spec A, 1983–2015) instead of
  "what does Spec B need" — a carrier-file answer, not a data-availability
  answer. The Spec-B campaign and the scoring sequence in this memo are
  unaffected; only the input-gap description is narrowed as above.

**What is needed to unlock origin-2024/2025 scoring, concretely:** a transcription
of the official 2026 DFO CSAS research-document tables for Northern cod 2J3KL —
(year × SSB) through the terminal year, official landings 2024→, and checkpoint
values — archived under the SOURCES.md provenance discipline (new file, never a
hand-edit of an existing one). That is owner-gated data ingestion; once the
owner supplies or authorizes it, both origins score mechanically per the frozen
sheet.
