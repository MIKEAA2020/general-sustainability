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
