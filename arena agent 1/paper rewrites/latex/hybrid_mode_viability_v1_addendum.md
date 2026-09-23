# hybrid_mode_viability_v1 — addendum

**Lineage:** `hybrid_mode_viability_v1` (standalone name from birth; no paperN prefix — the
naming rule adopted after the paper-2 prefix lesson). **D-item:** Hybrid Modes (D11)
of Track D (source: `uploads/suggested generalizations.txt`).

**Content.** Adversarial pressure regime: frozen modes 36=36 viable; mode-blind kernel exactly 28/36 with the 8 lost beliefs = those containing (1,1); mode observation restores 36; chain 28 < 36 = 36; brute-force cross-validation.

**Verification.** Exact rational/integer arithmetic; stdlib only;
deterministic. 6/6 check families:
E1 frozen kernels 36=36; E2 blind kernel 28/36, 8 lost beliefs enumerated; E3 observed restoration 36/36; E4 brute-force cross-validation; E5 chain 28 < 36 = 36; E6 scope assertions.

**Build.** Tectonic 0.15.0, first build: 0 overfull boxes; 2 pages;
50763 bytes; post-build probes pass (title/author/ORCID/AI declaration/
no unresolved references/declarations block).

**Defects found during verification (before ship).** The first crisis model (damage 3) was terminal under each frozen regime, so the planned premise (viable in each fixed mode) was unsatisfiable; redesigned to the pressure model. The initial claim 'the mode-blind kernel is empty' was refuted by computation (28/36 viable — juggling works with buffer); reframed as the exact boundary: 8 lost beliefs, all containing (1,1).

**Status.** Shipped to `latex/` (tex + pdf + verify + this addendum) via
cp + cmp; source zip `hybrid_mode_viability_v1_source.zip` (4 entries); pushed to the
programme repository under the batch commit for this item.
