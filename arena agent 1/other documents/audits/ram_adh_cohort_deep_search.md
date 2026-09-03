# RAM ADH cohort — deep-search memo (2026-09-02, second pass)

**Question.** Is the fisheries median (43 stocks with finite SSB and F series, zeros
included, median ADH ≈ 1.8 yr) reproducible?

**Previous record (corrected).** The first pass (turn 58) computed public RAM Legacy
releases v4.44/v4.495 *without* the zero convention and concluded "not reproducible".
That conclusion was premature: the source caption (A018 `tab:adh-fish`, recovered
verbatim this pass) specifies "**or 0 if already at or below the reference** … median
**including zeros**" — the zero entries enter the median, and they were missing from
the first pass. This memo records the corrected protocol, the deeper search, and what
reproduces.

## 1. The specification (recovered from the A018 source caption)

> H_F = F^{-1} ln(SSB_now/(0.2 max SSB)), or 0 if already at or below the reference.
> Median across all 43 assessed stocks with finite SSB and F series, including zeros,
> ≈ 1.8 yr (`fisheries_adh.csv`); the spectral null uses the 42 annual-managed stocks
> within this set.

The 43/42 pair is a nested pair (42 ⊂ 43) — independently confirmed in the repo's
"arena agent 2" batch-5 review findings (D-2, C).

## 2. What reproduces from public data

- **F values**: 4 of 6 published example rows reproduce the public v4.66 release
  exactly (1.0026→"1.00", 0.2274→"0.23", 0.193→"0.19", 0.0114→"0.011") — the extract
  is v4.66-era.
- **The zero convention and the protocol** reproduce as specified.
- **Corrected full-cohort statistics (zeros included)**:
  - v4.44 (Zenodo 2542919): n = 415, 63 zeros, median 2.57 yr;
  - v4.66 (Zenodo 14043031): n = 454, 69 zeros, median 3.39 yr.
- A battery of ~25 cohort definitions (family filters Clupeidae/Engraulidae/±Scombridae/
  Carangidae/Osmeridae; assessment-cadence and assessyear-end filters 2019–2023;
  synchronized series-end filters; ER and TBbest flow columns; F-at-last-SSB-year and
  last-common-year conventions; minimum-series-length grids 15–30 yr) was run across
  releases v4.44/v4.64/v4.65/v4.66 (Excel and RData, loaded in R). No public-release
  cohort definition reproduces (n = 43, median = 1.8).

## 3. Why the exact median requires the archived pull

- Two of the six published example stocks (**N. Adriatic anchovy, W. Scotland herring**)
  carry no SSB/F series at all in public releases v4.64–v4.66 (their series were
  removed from the DB by January 2024).
- Several stocks' SSB series have been revised since: the current North Sea herring
  series reaches back to 1947 with max ≈ 5.29 Mt, while the published ADH (3.5)
  implies an extract-time max ≈ 3.3 Mt; the Adriatic anchovy 17–18 published ADH = 0
  requires the extended pre-2000 series (max ≈ 1.5 Mt, present in v4.44), which the
  current 2000–2022 series no longer carries.
- `fisheries_adh.csv` itself is not in the repository: verified negative in
  `research_program/file_archive` (content-grepped after a sparse clone of the full
  133 MB sha-addressed archive — it holds manuscript texts, not data), all
  `research_program/article_*` folders, the computation closure packet, `worklog.md`,
  and all nine repositories of the owner's GitHub account (code search + tree scans).
  Its declared location ("the analysis repository") is not on GitHub.

## 4. Disposition (implemented this pass)

- **paper3_supplementary_v3.md** (v2 untouched): S5 rewritten to the corrected
  protocol — zero convention stated, example-row verifications, the corrected
  version-sensitivity table (v4.44: 415/2.57; v4.66: 454/3.39), and the precise
  statement of what the archived pull supplies (the 43-stock list and the
  extract-time series state).
- **paper3_material_ledgers_v12.md** (v11 untouched): the main-text cohort sentence
  updated to the corrected protocol reference and the corrected version-sensitivity
  numbers.

**Bottom line.** The median is reproducible from the archived extract under the
recovered specification; the first-pass "not reproducible" claim is retracted and
replaced by the corrected protocol record. Exact reconstruction from public data
alone is impossible because the extract-time series state no longer exists in any
public release — this is a data-vintage fact, now documented rather than guessed.


## 5. Resolution (2026-09-03) — the archived pull is supplied and re-verified

The owner supplied the archived extract itself (`uploads/fisheries_adh.csv`: header +
43 stocks; columns `stock, SSB, F, B_lim, ADH_yr, lastyear`; 2,505 bytes). Recomputing
every row against the recovered specification (ADH = (1/F)·log(SSB_now/(0.2·max SSB)),
zero entered at/below the reference) closes the search:

- **The extract is internally consistent, row by row.** With B_lim identified as
  0.2·max SSB (checked on every row), all 35 positive rows reproduce
  ADH = F⁻¹ log(SSB/B_lim) to relative error < 10⁻⁹; the 8 zero rows are exactly the
  stocks with SSB ≤ B_lim, none violating the convention. The ADH column is
  max(0, F⁻¹ log(SSB/B_lim)) throughout.
- **The headline numbers reproduce.** Median 1.7902 yr with zeros included (the
  reported ≈1.8; the positive sub-cohort alone gives 2.8578); maximum 201.1797 yr
  (ANCHMEDGSA7). The agent's accompanying description is correct on the stock-level
  values (HERRVIa 0.385, SPRATIIIa-IV 0.457, SPRATNS 0.723, ANCHIXa 0.783,
  PANCHNCH 0.993) but wrong that ~17 stocks are at zero — the file has **8**.
- **The four published-F anchors read off the file**: 1.0026 (1.00), 0.2274 (0.23;
  extract id HERRNS-IIIa-VIId, ADH 3.461 vs published 3.5), 0.193 (0.19), 0.0114 (0.011).
- **One stale residue fixed**: P3 v13 still carried the pre-correction sentence
  ("stocks already at or below the reference are reported separately and excluded")
  and a §7 matching clause — both contradicting S5's corrected protocol and the
  verified median. Fixed in **P3 v14**, and the pull verification is recorded in
  **paper3_supplementary_v4.md** (S5).
