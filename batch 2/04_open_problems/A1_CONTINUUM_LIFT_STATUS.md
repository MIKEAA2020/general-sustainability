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
