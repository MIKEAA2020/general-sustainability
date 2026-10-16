# Completed joint audits — 16 October 2026

This folder contains the two completed, evidence-based audits requested. Each adjudicates the uploaded reviewer claims against the current manuscript edition, source, code and verification output; distinguishes confirmed, corrected, contradicted, partly valid and speculative claims; and records a separate edition decision.

## Deliverables

1. [Paper11 v67 joint audit](Paper11_v67_joint_audit_2026-10-16.md) — **Paper11 v68 warranted, not created.** The principal remaining items are the J-17 Proposition 2 application, the M2m/climate class-disposition accounting, the realized-future-flux “nowcast” language, the SI clipping-path mismatch and salted-hash power reproducibility.
2. [P11c v5 joint audit](P11c_v5_joint_audit_2026-10-16.md) — **No new P11c edition warranted.** The v4 numerical and definition disputes are resolved in v5; the remaining corrections are to narrow PDF-verification claims, disclose that Lean was not rebuilt in v5 and add immutable code provenance before submission.

## Verification and scope

- Paper11 v67 verifier: **139/139**.
- P11c v5 verifier: **64/64**.
- The audits do not edit either manuscript or create v68/v6. The two current editions are preserved.
- All six remote branch tips and both tags were checked in the filtered repository snapshot before making edition recommendations. The current manuscript blobs were identical on `origin/main` and `origin/e2-v3-source-year`; the release listing had no paper-specific assets, and the large workspace ZIP payloads were not unpacked.
- No PAT contents are included in these deliverables.
