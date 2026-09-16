# Phase M changelog — archive computations → S1.5 supplement (2026-09-13)

Scope: the non-decorative, genuinely merited Phase M items — **O20** (IC variants
on the existing archive), **O30** (exact counts + Wilson intervals), **O32**
(identification decomposition). Zero new simulation; everything computes on
`sim_retention_power_20260913.csv`. Main text untouched except one
Data-Availability bullet naming S1.5. All deliverables live in the v26
supplement as **S1.5**.

## Two pre-computation audit-sweep records (owner-review addendum)

- **NEW-20** — the audits define the certificate levels *semantically* (N0
  descriptive / N1 inconclusive / N2 informative / N3 operationally informative +
  expiry triggers); Phase L's §2.2/S2 implement them *cumulatively*. Recorded as
  an optional refinement; no freeze implicated.
- **NEW-21** — the audits' recommended methods-paper structure redistributes
  existing main-text content into S1/S2 = the long-section redistribution Phase J
  declined (§3.5 precedent); declined again; S1.4/S2 built under that rule.
- **NEW-22** — the audits' wider instrument-comparison grid (4+ candidates,
  conditional gate-pass rates, regret, false-attribution rate) noted as a
  possible extension after Phase M; archive-only until owner expands scope.

## Computations (`phase_c/results/phaseM_archive_computations_20260913.json`)

Schema discovery: the archive is cell-level pooled RMSE per (dgp, rep, sigma,
module) — D1–D5 × σ {11.8, 33.8}, T = 33, unit = (σ, replicate), the
`retained` flag = full H3 gate (either horizon × baseline + comparator).
Reps: D1/D5 200, D2/D3/D4 100 per σ. Validation: per-σ truth power reproduces
published D1–D4 values exactly; pooled specificity 0.9725 ≈ reported 0.973.

- **O20** — four instruments on identical units (pooled D1–D4): stated rule
  power_any .613 / truth .490 / null-retention .0275; IC(h1) .758 / .433 /
  .045; IC(h5) .784 / .148 / .245; hybrid multi-horizon IC + selection gate
  .846 / .383 / .220. No dominance; comparator gate = price of specificity.
- **O32** — identification decomposition at h1 (P truth-best / P any-below-band /
  P rule-retains-truth): D2 is inference-limited (0.755 → 0.420 at the gates)
  inside an identification-limited study; D1/D3/D4 identification-limited.
- **O30** — exact frozen counts for all derivable cells + Wilson 95% intervals
  stated only where endpoints do not collide with archived replicate-table
  tokens (0.965/0.975/0.978); colliding cells reported as counts with method
  referenced. Companion-archive proportions (D6/D7, IC alt-row) quoted as
  archived.

## Files

- `paperF1_retention_framework_v26_supplement.md` — S1.5 added (S1.4, S2 intact).
- `phase_c/results/phaseM_archive_computations_20260913.json` — full frozen output.
- Scanners on the supplement: formalization 0, style PASS, redundancy 0;
  pair coverage (main + supplement) clean vs v0/v13.

Open after Phase M: Phase N (O26/O28 artifacts), Phase O (O23 literature);
pending owner: O19 criterion, Edwards DRAFT E2m convention; NEW-20/NEW-22 optional.
