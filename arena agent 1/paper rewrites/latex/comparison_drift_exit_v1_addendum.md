# comparison_drift_exit_v1 — addendum

**Lineage:** `comparison_drift_exit_v1` (standalone name from birth; no paperN prefix — the
naming rule adopted after the paper-2 prefix lesson). **D-item:** Comparison-Function Exit (D9)
of Track D (source: `uploads/suggested generalizations.txt`).

**Content.** Constant-drift identity floor(10(z0-1)); contraction alpha(q)=q/10 recovers sigma*(q0)=max{k: q0 >= (10/9)^k} at powers; quadratic bound 10(1-1/q0) dominates with strict domination; q_min multi-floor exit identity on 240 points; boundary-vanishing alpha scope instance.

**Verification.** Exact rational/integer arithmetic; stdlib only;
deterministic. 6/6 check families:
E1 constant-drift identity (48 cells); E2 contraction embedding at powers K<=3; E3 quadratic dominance with strict domination; E4 q_min identity (240 grid points); E5 comparison monotonicity; E6 boundary-vanishing scope instance.

**Build.** Tectonic 0.15.0, first build: 0 overfull boxes; 2 pages;
69909 bytes; post-build probes pass (title/author/ORCID/AI declaration/
no unresolved references/declarations block).

**Defects found during verification (before ship).** Exit-time convention off-by-one: closed forms are last-safe-step identities (first-exit = last-safe + 1). Unified on last-safe; all four identities then exact.

**Status.** Shipped to `latex/` (tex + pdf + verify + this addendum) via
cp + cmp; source zip `comparison_drift_exit_v1_source.zip` (4 entries); pushed to the
programme repository under the batch commit for this item.
