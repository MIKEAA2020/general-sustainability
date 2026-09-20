# Changelog

## 1.1.2 — 2026-09-20

- Figure pipeline corrected after external audit: the licensing-band panel
  now labels the exclusive-licensing regions ("only SLOW licensed for
  r < rho_1", "only FAST licensed for r > rho_2", "both licensed for
  rho_1 <= r <= rho_2"); rescued FP-witness label placement.

## 1.1.1 — 2026-09-20

- `novelty_searches/`: preserved related-software search records
  (six queries, verbatim result records, method README) supporting the
  positioning claims of the accompanying manuscript's Section 5 — the
  analogue of the master deposit's novelty searches.

## 1.1.0 — 2026-09-20

Deposit-readiness release, adopting the master deposit's reproduction
patterns:

- `run_all.sh`: one-command fresh reproduction (tests, benchmark checks,
  examples, optional figure regeneration).
- `SHA256SUMS`: integrity manifest over the package files.
- `requirements-figures.txt`: pinned figure-regeneration environment
  (matplotlib 3.10.9, Pillow 12.3.0); the library itself remains
  dependency-free.
- `figure_code/`: figure pipeline and graphical-abstract TIFF export
  (EMS portal format), mirroring the master deposit's layout.

## 1.0.0 — 2026-09-20

Initial release.

- Typed assessment operators (`E_typ`, `E_w`, `E_tube,phys`, `E_end`,
  `E_end,typ`) with exact chain verification; accepted-state sets and
  `V_weak`.
- Typed finite-graph backward recursion; belief-space robust epistemic
  recursion for partially observed systems.
- Exact rational Fourier–Motzkin elimination with provenance tracking,
  returning verified Farkas certificates and infeasibility margins;
  finite common-action obstruction with minimal conflicting subfamily;
  observation-fibre criterion.
- Dashboard readings: per-weight licensing thresholds (witness values
  2/3 and 3/2), rescue threshold kappa\* = 1 − x, per-plan tube minima,
  composite-index minimum, index-blindness alarm; single-file HTML
  dashboard with inline SVG.
- Resource-transition benchmark: twenty-four exact checks re-deriving
  the deposited verification values (DOI
  10.6084/m9.figshare.33764023).
- Command-line interface: `safetransition verify | report | demo`.
