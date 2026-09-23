# monitoring_design_v1 — addendum

**Lineage:** `monitoring_design_v1` (standalone name from birth; no paperN prefix — the
naming rule adopted after the paper-2 prefix lesson). **D-item:** Monitoring Design (D8)
of Track D (source: `uploads/suggested generalizations.txt`).

**Content.** Fibre condition necessary+sufficient (intersection form) over all 15 partitions; pairwise form fails off convexity (exact three-codex instance); coarsest admissible monitoring = 2 cells; delay/bias/aggregation rules as exact identities.

**Verification.** Exact rational/integer arithmetic; stdlib only;
deterministic. 6/6 check families:
E1 intersection-form equivalence over 15 partitions + non-convex counterinstance; E2 dynamic-caveat exhaustive search (absence recorded); E3 coarsest admissible = 2 cells (7 admissible); E4 delay identity on 48 cells; E5 bias bound 21/100; E6 aggregation verdicts.

**Build.** Tectonic 0.15.0, first build: 0 overfull boxes; 2 pages;
56650 bytes; post-build probes pass (title/author/ORCID/AI declaration/
no unresolved references/declarations block).

**Defects found during verification (before ship).** The target region initially contained the doomed corner (1,1), whose empty floor-servable set made every partition inadmissible; target redefined to {(1,2),(2,1),(2,2),(3,1)}. E2's exhaustive search found no dynamic-caveat instance on this target; the absence is recorded as the finding.

**Status.** Shipped to `latex/` (tex + pdf + verify + this addendum) via
cp + cmp; source zip `monitoring_design_v1_source.zip` (4 entries); pushed to the
programme repository under the batch commit for this item.
