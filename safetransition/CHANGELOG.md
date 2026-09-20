# Changelog

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
