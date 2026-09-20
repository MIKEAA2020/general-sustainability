# Changelog

## 1.2.1 — 2026-09-20

Scaling study and audit-provenance release (remaining external-audit
items):

- **Scaling study** (`benchmarks/scaling_study.py` +
  committed `scaling_results.json`): five parameterized instance families
  with answers known by construction and asserted — FM chain (quadratic
  row growth with the exact closed-form margin (1/5 − (k−1)/4096)/(k+1)
  verified at every size up to k = 256), dyadic bit growth (exact margins
  with 321-bit denominators certified at t = 320, where binary floating
  point has lost the gap), typed recursion to 21,000 states (clean linear
  time), action menus to 512, and belief spaces with 2^m reachable
  beliefs (the default 4,096 enumeration bound reached exactly at
  m = 12 and exceeded at m = 13, raising with no partial results).
  Recorded: runtime, peak traced memory, eliminator rows generated and
  peak working rows, certificate sizes and maximal bit lengths,
  independent-checker runtime.
- **Dashboard provenance**: the dashboard embeds a verification-provenance
  table (library version, independent-checker version and re-run command,
  datum identifier, certificate SHA-256 hashes over the exact serialized
  JSON, expandable exact input serializations); rendering is deterministic
  (pure function of inputs, no timestamps), so re-rendering is
  byte-identical and the embedded hashes are checkable. Footer now
  reports the package version.
- **Figure provenance**: `figure_code/make_benchmark_v45.py` regenerates
  the benchmark figure from the library's verified schedule values
  (equality asserted against the deposited v44 values), with the fund
  axis clarified in panel (b) — the fund schedule joins the legend as the
  right-axis series and the STAGED entry names the plotted quota —
  resolving the reported fund-axis ambiguity.
- `certify_polyhedron` exposes eliminator row statistics (`rows_generated`,
  `peak_rows`) used by the scaling study; checker version constant
  `CHECKER_VERSION` embedded in provenance records.

## 1.2.0 — 2026-09-20

Certificate-carrying interface release, implementing the highest-value
items of the external novelty audit:

- **Serializable certificates + independent checker.** Farkas
  certificates serialize to JSON (`to_dict`/`from_dict`, exact rationals
  as strings) and are verified by `check_safe_transition_cert.py`, a
  standalone stdlib-only script that shares no code with the package and
  re-derives every verdict from the certificate contents alone. Tampered
  certificates (altered bounds, multipliers, or systems) are rejected.
- **Exact weight-space partition.** `weight_partition` returns the
  complete arrangement of licensed plan sets along the weight ratio
  r = w2/w1 as a certificate, for the entire rational family of floor
  pairs and dip depths: the benchmark regime rho1 < rho2, the regime
  dip > s1 + s2 where the thresholds swap and an unlicensed gap opens
  around r = 1, and the degenerate single-point regime dip = s1 + s2.
  The benchmark thresholds 2/3 and 3/2 become instances of the complete
  object; per-dip thresholds follow the closed family
  (dip - s1)/s2 and s1/(dip - s2).
- **Tube-status semantics.** `TubeStatus` distinguishes EXACT tubes
  (declared paths) from CONSERVATIVE enclosures (the Schaefer
  realization, certified by monotonicity of the surplus on the visited
  biomass interval); `tube_certificate` carries the derivation.
- **Benchmark certificate.** `benchmark_certificate` emits parameters
  plus eleven derived quantities; the checker re-derives all of them
  from the parameters alone.
- **Adversarial exactness instance.** The suite now includes the
  n = 49 verdict flip: 49·(1/49) − 1 is exactly zero in rational
  arithmetic (floor exactly met, licensed) but −1.11e−16 in binary
  floating point (falsely unlicensed); the package's float-input
  rejection and the exact-licensed verdict are both asserted.
- **Belief-recursion hardening.** The belief bound is a parameter
  (`max_beliefs`, default 4096) that raises with no partial results;
  `explain_belief_failure` returns the per-action counterexample object
  (violation en route, or post-belief not viable at the previous level)
  for a non-viable root belief; docstrings state the exactness/soundness
  split of the observation abstraction.
- `licensing_thresholds` exposes the dip parameter (dip-parameterized
  thresholds for the whole rational floor family); the CLI gains a
  `certify` subcommand emitting the JSON certificates; the import graph
  of the core is asserted free of the figure stack; `examples/
  certificates_demo.py` demonstrates produce → independent-check →
  tamper-reject end to end.

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
