# certificate_duality_v1 — addendum

**Lineage:** `certificate_duality_v1` (standalone name from birth; no paperN prefix — the
naming rule adopted after the paper-2 prefix lesson). **D-item:** Certificate Duality (D6)
of Track D (source: `uploads/suggested generalizations.txt`).

**Content.** Four obstruction families as dual objects: Farkas multipliers, telescoping/substitution identities, contradicting-witness pairs, affine drift bounds; template closure both sides; corner instance where primal and dual agree on nonviability.

**Verification.** Exact rational/integer arithmetic; stdlib only;
deterministic. 6/6 check families:
E1 Farkas multipliers; E2 additive K<=4 and multiplicative K<=3 threshold identities at boundaries; E3 contradicting-witness fibre pair; E4 exact affine drift identity on 101 points; E5 template closure both sides; E6 duals-certify-nonviability scope.

**Build.** Tectonic 0.15.0, first build: 0 overfull boxes; 2 pages;
55315 bytes; post-build probes pass (title/author/ORCID/AI declaration/
no unresolved references/declarations block).

**Defects found during verification (before ship).** E6's first draft asserted witness actions for every safe state; the corner (1,1) refuted this (its floor-servable set is empty). Reframed: the corner is the instance where primal and dual AGREE on nonviability. Verify-before-fix on the actual artifact.

**Status.** Shipped to `latex/` (tex + pdf + verify + this addendum) via
cp + cmp; source zip `certificate_duality_v1_source.zip` (4 entries); pushed to the
programme repository under the batch commit for this item.
