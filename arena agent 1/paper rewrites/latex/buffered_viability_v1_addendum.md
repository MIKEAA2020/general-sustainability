# buffered_viability_v1 — addendum

**Lineage:** `buffered_viability_v1` (standalone name from birth; no paperN prefix — the
naming rule adopted after the paper-2 prefix lesson). **D-item:** Buffered Viability (D12)
of Track D (source: `uploads/suggested generalizations.txt`).

**Content.** Obstruction margin mu = 2 for the audited beliefs (maximality certified); nesting in the margin; erosion 28 -> 3 -> 0; buffered exit identities floor(10(z0-1-delta)) and max{k: q0 >= (10/9)^k (1+delta)}; measurement-error reading.

**Verification.** Exact rational/integer arithmetic; stdlib only;
deterministic. 6/6 check families:
E1 nesting over 36 pairs x 2 structures; E2 margins mu=2 certified; E3 constant-drift buffered identity; E4 contraction buffered identity at boundaries; E5 erosion 28->3->0; E6 measurement-error reading.

**Build.** Tectonic 0.15.0, first build: 0 overfull boxes; 2 pages;
66462 bytes; post-build probes pass (title/author/ORCID/AI declaration/
no unresolved references/declarations block).

**Defects found during verification (before ship).** Two mechanical defects: a margin-grid key typo (KeyError) and a negative closed-form value when z0 lies below the buffered threshold; both fixed (max(0, .)); nothing conceptual.

**Status.** Shipped to `latex/` (tex + pdf + verify + this addendum) via
cp + cmp; source zip `buffered_viability_v1_source.zip` (4 entries); pushed to the
programme repository under the batch commit for this item.
