# Changelog

## 1.3.0 — 2026-09-20

Semantics-precision release implementing the three-audit joint review
(gpt 62-item flaw list, deepseek executive re-assessment, revision plan):

- **Belief semantics formalized.** `belief_backward` docstring states the
  label-quotient construction explicitly: beliefs are elements of the
  state-space quotient under the observation map; the recursion is SOUND
  for finite systems (memberships certify belief-based
  observation-history policies); completeness of the quotient holds under
  a safety-and-action quotient condition (injectivity is the simplest
  sufficient condition); absent it, non-membership is an abstraction
  artifact, not a policy-nonexistence certificate.
- **Tube-status verdict semantics.** `TubeStatus` documents the one-sided
  consequence: constraints passed on a CONSERVATIVE enclosure certify the
  realization safe; a violation inside the enclosure is inconclusive
  unless the violating point is known reachable.
- **Fibre criterion narrowed** to what it decides: classification of
  current safe-set membership from the current observation alone — not
  policy existence, conservative certification, or history-dependent
  procedures.
- **Common-action obstruction compatibility defined**: co-possibility
  under the assessed observation; the action sets determine the horizon
  of the ruled-out claim (immediate-safe vs recursively viable).
- **Weight-partition scope and degenerates.** `weight_partition` states
  its menu class (two-floor witness family, affine trough conditions in
  the ratio) and its admissible parameter family (0 < s1, s2 < dip),
  raising `ValueError` outside it (thresholds nonpositive or denominators
  nonpositive mean licensed-everywhere plans); ratio domain (0, inf) with
  0/inf as projective limit closures in the certificate.
- **Index-blindness alarm boundary fixed**: fires when the composite
  minimum is NONNEGATIVE (operator-licensed) with a negative floor
  minimum, so boundary zero-margin cases are no longer missed.
- **`certify_polyhedron` feasibility honesty**: feasible systems return a
  bare verdict (no witness is reconstructed); the docstring says so.
- **Belief-failure certificates.** `failure_certificate` serializes the
  demo system plus the counterexample object; the independent checker
  gains a `belief_failure` type that re-runs the recursion from a
  stdlib-only reimplementation and validates the verdict and every
  per-action failure reason (tampered objects rejected).
- **Property-based and degenerate tests** (58 total): seeded randomized
  chain inclusion (60), Farkas validity + cross-check against an
  independent exact vertex-enumeration oracle (60), belief monotonicity
  (25), partition coverage sampling (20), cross-process canonical-JSON
  hash stability under three PYTHONHASHSEED values, 30 tamper mutations,
  and degenerate systems (empty/zero rows, duplicates, coincident
  thresholds, plans licensed everywhere rejected, empty action menus).
  The bound-mutation test documents the algebra/semantics boundary:
  a bound change leaving the system infeasible with the same multipliers
  is algebraically valid for the tampered system and verifies — the
  checker validates certificates against supplied systems, not systems
  against intended data.
- **Scaling study hardened.** Margin numerator/denominator bit lengths
  reported separately (the dyadic family's reduced margin denominator is
  7·2^320: 323 bits); platform, CPU, OS, Python version and full
  methodology recorded in the results metadata; a dense random stress
  family reports the classical row growth and its practical envelope
  (975 intermediate rows at 3 variables; the 60 s budget fires at 4 —
  the eliminator's dense-system envelope is narrow, as the complexity
  statement says).
- Figure labels: "neither plan is typed-safe at the witness (floors
  breached path-wise); at least one plan is aggregate-licensed at every
  admissible ratio" replaces the weight-dependent phrasing.

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
