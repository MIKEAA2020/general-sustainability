# Phase D changelog — v17 → v18 (2026-09-13)

Phase D = remnant/redundancy scan + the prospective-registration subsection
(register item claude 4.10: "freeze model set + next origins"; pairs with AD4).
One coordinated pass, 22 asserted replacement rules, applied to
`framework/paperF1_retention_framework_v18.md` (70,966 chars, 467 lines).
v17 and the full v13–v16 lineage remain frozen.

## 1. Remnant and redundancy scan (automated, `framework/redundancy_scan.py`)

Scanner checks: R1 exact-duplicate prose lines; R2 near-duplicate ≥8-word phrases
repeated ≥3× (parameter-definition constants allowlisted); R3 remnant probes
(dates, "rerun", "post-hoc", "vs" in prose, telegraphic fragments); R4 superseded
numeric values outside their legitimate archived-row context (word-boundary
guards; tables/code blocks exempt).

Findings on v17 and fixes:

| # | finding | fix |
|---|---|---|
| R2 | "Even with future catch supplied — an advantage no operational forecast has — structural modules still lose to persistence" ×4 (Abstract, §1, §3, §7) | §1 and §7 reworded; kept in Abstract and §3, where the audit logic lives |
| R2 | "M3 and M4 were never simulated as generating truth" ×4 | §4.3 clause dropped (stated in §4.2); §7 reworded; kept in Abstract + §4.2 |
| R2 | SSB/removal-term clause ×3 (§5.1 twice, §8) | §5.1 duplicate sentence dropped; §8 compressed |
| R2 | "compares no-change forecast with iterated trajectories, iterated affine analogue M2m 17.44 ft …" ×3 | compressed in §5.2; kept in §2.1 and the appendix verification block |
| R2 | "Post-2007 h=5 reversal M1 17.16 vs persist 25.10…" ×3 | dropped from §2.1 (kept in §5.2 and appendix) |
| R2 | climate-modules sentence verbatim in Abstract and §5.2 | Abstract compressed (kept the training-mean interval fact) |
| R3 | prose "vs" (6 spots) | all converted to "versus"; tables/code blocks exempted in the scanner |
| R4 | §6 table row still carried D1 0.965 and the pre-Phase-C identification percentages (62.7%/64.5%, 25.8%, 3.8%) | row synced to the pinned-seed numbers (0.955/0.960; 0.110/0.100; 0.010/0.010; 1%/11%, 37%/18%, 61%) |
| R4 | garbled heatmap sentence in §4.3 | formalized |
| — | T=71 summary repeated in §4.3 and §7 | §7 trimmed with a §4.3 cross-reference |

v18 scan result: **0 findings** (v17 had 91).

## 2. Prospective registration (§4.7, new — register item claude 4.10, pairing with AD4)

Inserted between §4.6 and §5. Four paragraphs, formal register:

- **Model set** — the seven-member ladder, h = 1 and h = 5, the one-step
  least-squares estimator with expanding windows (minimum eight years), and the
  class-grounds pre-gate carried forward; ladder additions only by pre-registered
  amendment (as Amendment 1 introduced D6/D7).
- **Next origins** — Edwards J-17: the ten annual origins 2024–2033; Northern cod:
  Spec B origins from 2025 onward per new xteNCAM vintage; Spec A closed (fixed
  2016 vintage). Archived origins never re-scored for a published verdict; new
  origins scored once, forecast files appended.
- **Prospective band (AD4)** — the simulation-calibrated band procedure made
  operational: simulate the object's own ladder at its own T and SNR (in-class
  members as truth; persistence-true null for specificity), adopt the smallest
  band attaining power ≥ 0.80 and specificity ≥ 0.90; else report the attainable
  frontier and retain 5%. Future applications only; never re-opens reported verdicts.
- **Closing commitment** — the reporting obligations of §§2–3 and the
  operating-characteristic discipline extend unchanged to every future verdict.

Supporting edits: §4.5 AD4 sentence cross-references §4.7; §1 lists §4.7 among the
components; §4.3 appends the locked Amendment-1 length-sensitivity check
(D1 power |Δ| between T=33 and T=71: 0.055 low σ, 0.040 high σ — rule satisfied);
Data availability files the registration with the specification sheets.

## Verification

`journal_formalization_scan.py` 0 flags · `redundancy_scan.py` 0 findings ·
`journal_style_automated_scan.py` 0 blockers PASS · `content_coverage_scan.py`
all v0/v13 numeric claims covered, 30/30 domain terms · apply script idempotent
(byte-identical re-apply).
