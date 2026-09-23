# institutional_observation_v1 — addendum

**Lineage:** `institutional_observation_v1` (standalone name from birth; no paperN prefix — the
naming rule adopted after the paper-2 prefix lesson). **D-item:** Decentralized Observation (D13)
of Track D (source: `uploads/suggested generalizations.txt`).

**Content.** Unanimity protocol: coordinator 28/36, decentralized 12/36 (exhaustive over 256 law pairs); exactly 16 lost pairs with exhibited individually-sufficient instance; audited belief survives via anti-symmetric voting; authority restriction 12 -> 0; one-step delay robustness.

**Verification.** Exact rational/integer arithmetic; stdlib only;
deterministic. 6/6 check families:
E1 coordinator kernel 28; E2 decentralized kernel 12 (256 law pairs); E3 exact boundary 16 + exhibited instance + anti-symmetric survival; E4 communication value setwise; E5 authority collapse 12->0; E6 one-step-delay robustness.

**Build.** Tectonic 0.15.0, first build: 0 overfull boxes; 2 pages;
49001 bytes; post-build probes pass (title/author/ORCID/AI declaration/
no unresolved references/declarations block).

**Defects found during verification (before ship).** The first decentralized model let cells choose any instrument rather than the agreed vote — rewritten as the deterministic trajectory simulation of the unanimity protocol. The audited belief was initially claimed non-decentralizable; computation refuted this (the anti-symmetric voting law cycles (1,2)->(2,1)->(1,2) indefinitely). Reframed: exactly 16 lost pairs with an exhibited individually-sufficient instance; the audited belief survives through 16 of 256 law pairs.

**Status.** Shipped to `latex/` (tex + pdf + verify + this addendum) via
cp + cmp; source zip `institutional_observation_v1_source.zip` (4 entries); pushed to the
programme repository under the batch commit for this item.
