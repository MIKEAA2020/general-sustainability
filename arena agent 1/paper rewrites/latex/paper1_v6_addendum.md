# Paper 3 — v6 addendum (scaling study + audit-completion revision, 2026-09-20)

New files; v1–v5 preserved. Companion package release: **SafeTransition
1.2.1**. Scope: the remaining implementable GPT-audit items — the
parameterized benchmark family with known answers (item 10, "scaling
study"), the dashboard-to-certificate binding (§4.2 provenance list), the
formal obstruction-to-Farkas row mapping (§4.3), the "closes a practical
gap" restoration (conclusion), and the gemini-1C figure follow-up
committed as a testable invariant.

## Package 1.2.1

- **Scaling study** (`benchmarks/scaling_study.py`, 291 lines; committed
  full run in `benchmarks/scaling_results.json`, 11 s single-core):
  five parameterized families, answers known by construction and
  asserted at every size —
  FM chain (k to 256; closed-form margin (1/5 − (k−1)/4096)/(k+1)
  verified at every k; quadratic worst-case row growth observed on
  planted instances, 256 rows at k = 256; certificate 335 kB, 13-bit
  coefficients; checker re-verification 0.29 s),
  dyadic bit growth (t to 320: margin 2^−t/(L+2) certified with 321-bit
  denominators, far beyond the binary64 gap horizon),
  typed recursion (to 21,000 states at horizon 20; linear, 2.1 s),
  action menus (to 512 actions through all five operators; linear),
  belief spaces (2^m reachable beliefs verified to m = 10; the default
  4,096 bound reached exactly at m = 12, exceeded at m = 13 → raises
  with no partial results). Peak memory traced throughout.
- **Dashboard provenance**: `default_provenance()` + embedded
  verification-provenance table (library version, checker version +
  re-run command, datum identifier, certificate SHA-256 hashes over the
  exact serialized JSON, expandable exact serializations); rendering is
  deterministic (pure function of inputs, no timestamps) — re-render is
  byte-identical, hashes checkable; footer reports the package version
  (stale 1.0.0 hardcoded string removed).
- **Figure provenance**: `figure_code/make_benchmark_v45.py` regenerates
  the benchmark figure from the library's exact `schedule_data()` values
  (equality with the deposited v44 values asserted in the test suite);
  panel (b) fund axis clarified (fund legend entry + coloured right-axis
  label; STAGED entry names the plotted quota) — gemini 1C resolved.
- `certify_polyhedron` exposes `rows_generated`/`peak_rows`; checker
  `CHECKER_VERSION` constant; scaling section in README; run_all.sh now
  7 steps (quick sweep writes a disposable file; the committed full
  results are never clobbered).
- QA: 46/46 tests; zip `SafeTransition_v1.2.1.zip` (914,589 B);
  SHA256SUMS 51 entries.

## Paper v6 (11 pp)

1. New §3.5 "Scaling of the exact pipeline" + Table 2 (families, known
   answers, largest-instance measurements); abstract scaling sentence;
   §3.2 cross-reference ("exactness scales gracefully … 321-bit
   denominators").
2. §4.2: dashboard reframed as audit-delivery mechanism bound to the
   certificate schema (the audit's full provenance-field list:
   hashes, library version, datum identifier, exact input serialization,
   checker version, verification status, re-run command; determinism).
3. §4.3: formal obstruction→stacked-system→Farkas row mapping (rows =
   per-state menu restrictions; equal multipliers; the empty common menu
   is exactly the certified infeasibility).
4. §6: "closes this practical gap within its stated scope" restored,
   justified by independent checking + scaling + §5 comparison.
5. QA table: 46/46; scaling row; dashboard-provenance row;
   figure-provenance row; 1,633/621 (+250, +291); caption 1.2.1.
6. Module table: benchmarks row; caption 1.2.1 counts; Figure 1 caption:
   provenance + right-axis statement.
7. Availability: program size + test-suite paragraph updated (46 tests,
   new coverage, under 4 s).

Companion files: `paper3_supplementary_v3.md` (S5 → 1.2.1 tree with
benchmarks/; new S10 scaling-study section with the committed results
table), `paper3_gpt_audit_completion_v2.md` (completion-status report),
`paper3_safetransition_ems_v6_highlights.txt`.

## v6 QA

Compile exit 0; 11 pp; 0 `??`; overfull baseline (2.43 pt) only; abstract
exactly 150 words; figshare DOI ×1; scaling table renders within margins
(visually verified); all updated counts confirmed against the 1.2.1 tree.
