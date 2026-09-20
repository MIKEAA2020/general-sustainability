# Paper 3 — v5 addendum (GPT novelty-audit revision, 2026-09-20)

New files; v1–v4 preserved. Companion package release: **SafeTransition
1.2.0**. Input: the GPT EMS novelty audit (10 gaps + §5 comparison demand +
wording fixes); every checkable audit claim re-verified against artifacts
before fixing — verdicts in `paper3_gpt_audit_verification_v1.md`
(1 refuted, 10+ implemented, 3 noted).

## Package 1.2.0 (certificate-carrying release)

- `FarkasCertificate.to_dict()/from_dict()` — JSON serialization, exact
  rationals as strings; round-trip re-verifies identities.
- `check_safe_transition_cert.py` (repository root, 248 lines) —
  standalone stdlib-only independent checker sharing no code with the
  package; verifies Farkas certificates (λ ≥ 0, λᵀA = 0, λᵀb < 0), weight
  partitions (thresholds, tiling, inclusivity, licensed sets at sampled
  ratios, boundary witnesses, all three regimes), and benchmark
  certificates (11 values re-derived from parameters alone + tube
  enclosure inequalities). Tampered certificates rejected.
- `weight_partition()` — complete exact licensed-set arrangement along
  r = w₂/w₁ as a serializable certificate; generic in the dip:
  benchmark regime (ρ₁ < ρ₂), swapped regime (dip > s₁ + s₂: thresholds
  swap, unlicensed gap around r = 1), degenerate regime (single-point
  middle region); per-dip threshold family (dip − s₁)/s₂, s₁/(dip − s₂).
  The family test caught the swapped-regime case during development and
  drove the generic implementation.
- `TubeStatus` (`EXACT`/`CONSERVATIVE`) + `tube_certificate()` with the
  monotonicity derivation; `benchmark_certificate()`.
- `explain_belief_failure()` — per-action counterexample for a non-viable
  root belief; `max_beliefs` parameter (default 4,096) raising with no
  partial results; docstrings state the exactness/soundness split.
- Adversarial exactness instance n = 49 (exact 0 licensed; float
  −1.11 × 10⁻¹⁶ would unlicense) asserted on the library's own predicate;
  float inputs structurally rejected; import-graph hygiene tests.
- CLI `certify` subcommand; `examples/certificates_demo.py`; README
  certificate-protocol section; CHANGELOG; SHA256SUMS 43 entries.
- QA: 39/39 tests; `run_all.sh` 6/6; zip `SafeTransition_v1.2.0.zip`
  (895,594 B, 53 files).

## Paper v5 (10 pp)

1. Abstract: "supplied exact or certified conservative reachability
   tubes"; serialized-certificate + independent-checker sentence; rescue
   threshold detail dropped (144 words ≤ 150).
2. §1: gap statement narrowed (SMT solvers certify in their own semantics;
   missing layer carries assessment semantics); novelty-search records
   referenced (q1–q12, deposit).
3. §2.1: chain scope conditions (positive weight cone; common disturbance
   set).
4. §2.2: soundness/completeness split (completeness under injective
   observation); failure explainer.
5. §3.1: "nine modules plus the repository-root independent checker";
   module table + checker row + 1.2.0 counts (1,542/470/248); CLI lists
   `certify`.
6. §3.2: adversarial n = 49 instance.
7. §3.3: explainer/`weight_partition` interfaces; bound-as-parameter
   wording; "as exact elimination inherently is".
8. §4.1: tube-status certification (EXACT declared paths; CONSERVATIVE
   realization with derivation).
9. §4.3: weight-partition paragraph with the three-regime table;
   explainer counterexample on the recourse-failure system.
10. §5: z3 (DOI 10.1007/978-3-540-78800-3_24 ✓), PRISM 4.0
    (DOI 10.1007/978-3-642-22110-1_47 ✓), pyfme (Caron 2022, GitHub;
    SymPy rationals, Imbert acceleration, no provenance) — both DOIs
    re-verified by content negotiation at revision time; Table 3
    five-property comparison; scoped claim (environmental families
    return no certificates; provers ship no assessment semantics).
11. §6 + availability: 1.2.0 counts, 39 tests with protocol coverage;
    conclusion scoped ("addresses a practical gap … wherever verdicts
    must be re-derivable by third parties").
12. QA table: 39/39; independent checker 3/3 + tamper rejection;
    adversarial instance row; 1,542/470 (+248); caption 1.2.0.

Companion files: `paper3_supplementary_v2.md` (S5 updated to 1.2.0 tree;
S6 extended with the deposit's twelve-query set and aligned with §5;
new S9 certificate protocol), `paper3_safetransition_ems_v5_highlights.txt`,
`paper3_gpt_audit_verification_v1.md`.

## v5 QA

Compile exit 0; 10 pp; 0 `??`; overfull baseline (2.43 pt) only; abstract
144 words; figshare DOI exactly once; Table 3 and QA table visually
verified in the rendered PDF.
