# ER037 Point Inventory — Preliminary, Pending Second Parallel Audit

## Status

First of two CAP-deliverables audits. No final implementation or status decision until joint assessment with the second audit.

## Strong points

1. Correctly distinguishes one-ULP storage hulls from a true orbit enclosure.
2. Correctly keeps CAP-ORB, FLOQ, SLACK, BUNCH, concrete coupling, and theorem gates separate.
3. Correctly retains generic perturbation as a declared alternative rather than source-derived A021 coupling.
4. Correctly refuses theorem promotion.
5. Status matrix is broadly accurate at the continuum-theorem level.

## Updates required in joint review

1. Finite K80 one-ULP coefficient hulls have now been interval-evaluated: storage-aware `Y<=3.49e-9`, `Z0<=4.27e-5`, and a negative finite radii polynomial through radius `2e-7`. CAP-ORB remains pending only because the infinite tail/true orbit ball is open.
2. Phase-fixed solves now extend through K240, with K160/K200/K240 data and high-mode transfer defects.
3. Structured K240-to-K600 transfer defect is `1.595e-6`.
4. Tight-box outward interval linearization gives a Sobolev high-mode tail factor `<=0.7475` above K600.
5. Numerical block-Neumann precursor is below `0.748`.
6. Sixth-derivative coefficient and orbit-ball sensitivity margins are available.
7. The interval all-direction/tail coupling and continuum Floquet projection proof remain genuinely open.
8. No source-derived `G,f,g`; generic perturbation theorem remains the only fully declared coupling option.

## Provisional disposition

Retain ER037's no-promotion and gate structure, but update the finite interval/tail progress before final joint adjudication.