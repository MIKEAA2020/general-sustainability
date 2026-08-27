# A1 — The Continuum Lift: Status Record

> **Provenance & status discipline:** reconstructed after the filesystem loss of the long-form original (worklog Task 6; expansion recorded in TRANSFER_AUDIT_RESPONSE Finding 1). This is a *status record*, not a theorem file: A1's Step 1–2 tail-envelope verifications are COMPUTED_PARTIAL (verified for the computed modes k=1..80 only; the k>80 extension is hypothesis H-tail); the K=1600 Newton run is numerical only. **Nothing in this file is PROVEN; the piecewise-Chebyshev campaign remains the specified, unexecuted route.**

## What was proved and computed

### A1.Thm1 (verified tail envelope — PROVED)
K=80 orbit's Fourier coefficients obey per-state geometric envelopes |c_k^s| ≤ C_s q_s^k verified for k=1..80 (outward-rounded): q ≈ 0.80–0.83. Tail norms under H-tail: C0 ≤ 5.3e-6 (N).

### A1.Thm2 (K=1600 substrate — COMPUTED)
Zero-padded orbit at K=1600, matrix-free Newton with Fourier-diagonal preconditioning, collocation residual 5.57e-6.

## The obstruction (the diagnostic finding — PROVED)

The Fourier-global radii polynomial cannot close for this orbit: P·Lip_f ≈ 7900 defeats global-Fourier and global-Schauder approaches. The correct route: **piecewise-Chebyshev collocation radii polynomials** (local patches, M≈8000 segments, local gain O(1)). All inputs exist.

## Status

COMPUTED_PARTIAL. The piecewise-Chebyshev campaign was specified but NOT EXECUTED. The discrete K=80 Krawczyk certificate is PROVEN and committed.

## Update 2026-08-26: Stage 1 EXECUTED (substrate + local-gain diagnostic — not a certificate)

`research_program/validated_computations/a021_c4/c4_piecewise_chebyshev_stage1.py` (+ `.json` artifact) executes the campaign's first stage on the committed validated orbit (the Krawczyk box midpoint): the piecewise-Chebyshev substrate, the measured local-gain distribution, the delay-coupling band, and the defect levels that feed the future radii polynomials. Measured results:

1. **The local-gain premise HOLDS on the measured orbit.** The sup of the right-hand side's Lipschitz constant (local Jacobian norm + delayed-coupling column, charged at full weight) along the orbit is **7.17** — the global obstruction is P·lip = **2660** (the status record's ~7.9e3 used the cruder global bound 21, cf. the certificate's E_sup 20.08; both readings recorded). The per-segment gain h·lip falls like P·lip/M exactly as specified: **M\* = 2660 segments for max gain ≤ 1, M\* = 5320 for ≤ 0.5; at the specified M = 8000 the max local gain is 0.333 (median 0.060)** — the O(1)-local-gain premise of the route is confirmed with margin.
2. **The delay-coupling band is finite and moderate:** at M = 8000 the delay window spans **97 segments** — each patch couples to a ~97-patch band, as the specification requires.
3. **The defect levels are small:** the K=80 orbit's own DDE defect at the Chebyshev–Lobatto nodes is 7.86e-9 (matching the committed certificate's residual scale); the degree-8-per-patch spectral-derivative gap against the Fourier derivative is ≤ 1.9e-9 at M = 8000. The future radii-polynomial Y-input at this scale is dominated by the orbit's own defect, not by the local representation — the substrate is adequate.
4. **Remaining stages (not executed):** Stage 2 — outward-rounded interval evaluation of the local defects and Jacobian blocks; Stage 3 — the local Krawczyk/radii-polynomial system with the finite-band coupling enclosed; Stage 4 — patch-to-patch contraction assembly and the continuum orbit certificate (the A1 gate).

Honesty: Stage 1 measures and verifies premises; it certifies nothing and upgrades no theorem status. A1 remains COMPUTED_PARTIAL until Stage 4 closes.

## Update 2026-08-26 (b): Stage 2 EXECUTED (outward-rounded interval evaluation — machinery + measurement, not a certificate)

`research_program/validated_computations/a021_c4/c4_piecewise_chebyshev_stage2.py` (+ `.json`/`.npz` artifacts, deterministic — byte-identical across reruns) executes the campaign's second stage on the same substrate: the local collocation defects and Jacobian blocks of all M=8000 patches re-evaluated in outward-rounded interval arithmetic (float64 with `np.nextafter` everywhere; softplus/sigmoid per node in mpmath dps=30; the differentiation matrix and all P-dependent constants in mpmath dps=40), plus the tube-inflation ladder Stage 3 needs.

The width machinery (the enabling trick): at the algebraic node times t = (P/M)(j + (ξ_i+1)/2) the Fourier phase 2πkt/P is **P-free** (= 2πkj/M + πk(ξ_i+1)/M), so the patch phases are exact M-th roots of unity computed once in mpmath — the integer power z^k is again an M-th root of unity, taken by exact integer table permutation (width 1 ulp; no binary powering) — and the node offsets are 729 mpmath evaluations. Node-value widths: X ≤ 1.8e-12, Zd ≤ 1.9e-14 (a naive interval product chain would give ~1e-11); the delay is folded per mode (At = A cos φ − B sin φ, Bt = A sin φ + B cos φ) so the delayed values reuse the same phase factors. Measured results:

1. **The Stage-3 Y-input is rigorously enclosed**: sup |Y_cheb| ≤ **8.326e-9** (interval width 7.0e-9) — 5.8% above Stage 1's float 7.865e-9. The orbit's own DDE defect (Fourier derivative, no matrix amplification) is enclosed ultra-tightly: sup |Y_four| ≤ **7.864e-9** with width 4e-14, matching the committed certificate's residual scale.
2. **The O(1)-local-gain premise now holds in interval arithmetic**: the rigorous gain interval at M=8000 is [0.33245909687600, 0.33245909687601] (width 1.6e-14), bracketing the recomputed float sup 0.33245909687600106 (Stage 1's committed reading 0.3325, rounded to 4 decimals).
3. **The tube machinery works**: the inflation ladder (δ ∈ {0, 1e-8, 1e-6}) runs end-to-end — at δ=1e-6 the gain sup upper stays 0.3325 and the defect-interval width grows to 1.4e-5 (measured, ready for Stage 3's radii-polynomial tube evaluation).
4. **Verification (all pass)**: an independent full-mpmath evaluation of the Fourier sum AND the delayed value at five nodes is contained in the interval node values (mpmath widths 1.7e-46); the float64 point evaluator agrees with the interval midpoints to 1.25e-12 (the documented float64 phase-rounding scale); the float defects are contained; the interval gain contains the float gain.
5. **Remaining stages (not executed):** Stage 3 — the local Krawczyk/radii-polynomial system with the finite-band delay coupling enclosed (consumes the interval Y-input and tube-Jacobian machinery delivered here); Stage 4 — patch-to-patch contraction assembly and the continuum orbit certificate (the A1 gate).

Honesty: Stage 2 encloses and measures; it certifies nothing and upgrades no theorem status — the substrate is the float64 box-midpoint orbit, NOT an enclosure of the true DDE solution. A1 remains COMPUTED_PARTIAL until Stage 4 closes.
