# policy_class_lattice_v1 — addendum

**Lineage:** `policy_class_lattice_v1` (standalone name from birth; no paperN prefix — the
naming rule adopted after the paper-2 prefix lesson). **D-item:** Policy-Class Lattice (D7)
of Track D (source: `uploads/suggested generalizations.txt`).

**Content.** Chain institutional 24 <= per-cell 26 <= full 28 (of 36), strict at both links; CE trap drift re-verified; distances to viability: refinement 1 split, expansion 1 instrument (restores all 36 pairs), prior shrink 1 state.

**Verification.** Exact rational/integer arithmetic; stdlib only;
deterministic. 6/6 check families:
E1 setwise chain 24<=26<=28 of 36; E2 strictness at both links + CE drift re-verification; E3 action-expansion 26<36 setwise; E4 refinement distance 1 (exhaustion); E5 expansion distance 1; E6 prior-shrink distance 1.

**Build.** Tectonic 0.15.0, first build: 0 overfull boxes; 2 pages;
54890 bytes; post-build probes pass (title/author/ORCID/AI declaration/
no unresolved references/declarations block).

**Defects found during verification (before ship).** Two defects. (1) The 'robust-full-obs as uniform instrument' operationalization yielded an empty kernel (0/36) — vacuous, replaced by the honest three-level chain with the CE class identified on-family and the trap cited for the separation. (2) The harness's step map initially mis-handled the expansion instrument u=3 (treated as damage on both patches); fixed; expansion then restores all 36 pairs.

**Status.** Shipped to `latex/` (tex + pdf + verify + this addendum) via
cp + cmp; source zip `policy_class_lattice_v1_source.zip` (4 entries); pushed to the
programme repository under the batch commit for this item.
