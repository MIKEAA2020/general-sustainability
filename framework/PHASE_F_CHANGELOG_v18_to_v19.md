# Phase F changelog — v18 → v19 (2026-09-13)

Phase F = the journal-fit text consolidation pass from the merged improvement plan
(`MERGED_IMPROVEMENT_PLAN_ALL_VENUES_v18.md`, items O1, O2, O3, O10, O11, O13, O14;
venues: qwen register item 9, qwen 6.7, claude 2.3, V9-B/C/E/F/G/I). 12 asserted
rules, text/table only — no verdict contact, no new computation. v18 and the full
v13–v18 lineage remain frozen.

## Items

- **O1 — abstract IC caveat (qwen 6.7 remainder).** The abstract's Implications
  sentence now states that the information criterion scores one-step accuracy and
  does not encode the decision-relevant multi-year persistence requirement, which
  the rule does.
- **O2 — informal term (register item 9).** "not second fibre of this
  specification" → "outside the scope of this specification".
- **O3 — climate-module table + NEW-3 correction (claude 2.3 / V9-F).** New
  **Table 5b** in §5.2: per-module rolling-origin RMSE at h=1/h=5 with margins
  versus M1, from the archived companion (E3 Table 7). Building the table exposed
  a cross-venue inconsistency in the v18 prose (adjudicated as **NEW-3**, recorded
  in the merged plan): "the R-ENSO variant is 0.41 ft worse" and
  "M2_Rprecip and M2_Rar edge past M1 at h=1 (12.71 versus 12.84 ft)" contradicted
  every archived companion artifact. The archive is authoritative: **M2_Rar**
  (recharge autoregression) is the 0.41 ft-worse module (13.25 vs 12.84);
  M2_Renso −0.02, M2_Rprecip −0.04, M2_combo −0.13 stay within 0.13 ft of M1; the
  "edge past M1" pair (Rprecip 14.52, Rar 14.67 vs M1 15.62) belongs to the
  2015–23 critical-period fixed window, not the rolling origins. §5.2 prose
  corrected; the §6 comparison-table row scoped to that window.
- **O10 — class-grounds principle (V9-E).** §2.3 now states the general principle
  of **structural redundancy** — a module that reduces to a simpler member under
  the conditions of application adds no information, regardless of its score —
  with the gloss planted in the abstract; the pre-registered output name
  "declined on class grounds" is unchanged.
- **O11 — problem-first + one-page standard statement (V9-B/C remainder).** The
  abstract and §1 already opened with the problem (audited as duplicates of V9-B);
  §1 now closes with a one-page statement separating the three layers: the
  standard (three obligations), the demonstration (one rule, three objects, two
  domains, two routes), and the simulation (operating characteristics of this
  particular rule).
- **O13 — reproducibility-discourse paragraph (V9-G).** §4.7 now connects the
  prospective machinery to registered reports (Chambers, 2013), the
  M-competitions (Makridakis et al., 2020), and pinned-seed archival, and states
  the standard's contribution to the movement: interpretable negative verdicts.
  Chambers (2013) added to the References.
- **O14 — consolidated limitations (V9-I).** §7's "Not licensed" block now leads
  with the three-limit enumeration (operating-characteristic design, power bound
  including specificity, domain count) and each limit carries a bold label
  (Series length / Upper bounds / Two domains).

## Verification

`apply_phaseF_v18_to_v19.py` re-run reproduces v19 byte-for-byte (idempotent);
`journal_formalization_scan.py` 0 flags · `redundancy_scan.py` 0 findings ·
`journal_style_automated_scan.py` PASS 0 blockers · `content_coverage_scan.py`
all v0/v13 numeric claims covered. v19: 74,468 bytes, 73,717 chars.
