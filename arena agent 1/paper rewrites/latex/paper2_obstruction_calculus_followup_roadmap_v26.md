# Paper 2 — Obstruction Calculus: Follow-up Roadmap (v26)

**Subject:** *An Obstruction Calculus for Viability under Incomplete Observation*
(current: `paper2_obstruction_calculus_v49_Automatica_routes.tex` + supplementary v46).

**v26 changes:** (1) **Third audit round adjudicated and shipped** across two
papers (`paper2_worked_computational_round3_joint_audit_v1.md`): the
worked-systems audit's substantive items were upheld and shipped in
`paper2_worked_systems_v7` — the τ\*/σ\* timing split (strict-vs-floored fails
on all six viable cells; strict-vs-real only at (2.0, 1)); the pessimistic
shared-register semantics, proven **setwise-equal** to the scripts'
single-thread kernels (24/26/25/28) with the optimistic reading distinguished
(new verify checks M2b/M2c); the §4 dominance and 12|31 corrections (forced
step-2 register death under both structures; M3b); the §5 Helly-2 statement;
the −1/10 boundary-critical wording; the "36 = 36" repair; a shipped
v5/v6-era `\ref` corruption fix found by this round's byte-level scan; and
the owner-directed Figure 5 label move (beneath the dashed line, y = −0.33).
The computational audit's items shipped in `paper2_computational_certification_v3`
(+ S1 v3): the v2 source-corruption repair (literal TAB/CR bytes eaten from
`\texttt`/`\ref`); all abstract overstatements; Prop-2 convexity at the point
of use; 𝒮_G grid spec; semidecidability input model; rank definition;
corrected proof-outline error terms; **pairwise-viability policies now in the
main text** (1.9752 = 12345/6250; 1.9352 = 2419/1250 — the campaign script's
"12193/6250" check label was a display typo, assertion always correct);
residual-test/sparsification/Prop-5/erosion/oracle precision; Table-1 caption;
§10 reframing ("Finite-Side Reference Library"; archive preservation replaces
"retirement"); §12 "rests on three requirements"; Abaee 2026b bib entry.
Both verify scripts extended (ws 26/26 + 57/57 chained; comp 20/20 + 51/51 +
9/9 + 12/12 chained); source-hygiene regressions added on both sides.
(2) **Scheduled from the round:** full minimax-theorem exposition of
Theorem 4(iv) (the largest remaining exposition debt); primitive-data
derivation of L; literature expansion (verified references only); per-basin
decentralized table (ws v8 candidate); independent certificate-file parser;
`viacert.continuous` consolidation with archive preservation; reference-styling
pass; title-length options for the computational paper.
(3) **Owner-side items unchanged** (tagged release + DOI + commit + lockfile +
checksums; venues; figshare upload → DOI → master v5 → item v2, figshare
33764023 hygiene; `paper2_`-prefix rename decision; release-token rotation;
2026 SAR pin; single-DOI consolidation of scripts and logs).

*Every claim above is a pointer into the cited sources; nothing here
creates theorem status.*
