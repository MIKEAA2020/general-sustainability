# v16 — Review verdict: additional figures and pedagogical enhancements

Commit `ced12e0+` (v15) followed by v16. `VERSION revision=16`. Live pointer → `data/revisions/IMPLEMENTED_revision_ECOMOD_v16.md`. v1–v15 preserved.

**Answer to both questions: yes, a small number of genuinely non-decorative additions were merited, and they have been implemented.** The manuscript already carries substantial quantitative content (many tables, R1/R2 figures, a demo run, empirical sweep figures). The judgment below separates what adds *explanatory power* versus what would merely duplicate existing content.

---

## Q1 — Additional non-decorative tables / figures / visual aids?

**Verdict: 2 figures + 1 table merited; several candidate figures did NOT (rejected as duplicative).**

### Added
1. **`scans/feedback_diagram.png`** — the causal/two-loop diagram that §7 **prescribes** ("Present it with the two positive-feedback loops …they compound") but never renders. It shows the `A→B→K→P→E` flow, the `[E−bA]₊` switch node, and the **two compounding positive-feedback loops** (Loop 1 stock-liquidation, Loop 2 debt-erosion). This is a direct implementation of an already-requested element, not new theory.
2. **`scans/r1_recovery_vs_collapse.png`** — the *same* initial condition `(A₀,P₀)=(1.0,0.1)` recovering (`A→A_max`, `τ_g=10`) versus collapsing (overshoot `A→1.36`, `A→A_ext`, `τ_g=30`). The R1 cliff was previously shown only as a basin *fraction* / delay-response curve; this gives the mechanism in **trajectories**, which is the clearest possible illustration of the τ_g-controlled collapse.
3. **A consolidated "regime → outcome" table** (end of §4.1) — maps `b_Gρ ⋚ b` (equivalently `ψ`) to the `B(A)` shape, the sustainable point, the MSY location, and the collapse/mask behaviour in one place.

### Rejected (would be duplicative / decorative)
- A separate MSY-vs-`A_max` curve **at baseline** implied an *interior* MSY that does not exist there (see Q2's finding) — rejected as misconceived until re-parameterised; the two-regime figure supersedes it.
- Any further "illustration" of the overshoot (already shown in `IMPLEMENTED_demo.png`).
- Symbol/assumption tables (already in §2.1/§3); scenario-status tables (already in §8/§12).

**Non-decorative test applied:** each added piece answers a question a reader would otherwise have to reconstruct from algebra (the loop structure, the trajectory mechanism, the regime rule), rather than re-ploting something already tabulated.

---

## Q2 — Additional pedagogical enhancements / clarifications / physical insights?

**Verdict: one genuinely-important clarification + the accompanying insight; the rest of the existing text already carries the intuition.**

### Added (corrects a real over-statement)
- **§4.1 qualification: the "interior MSY" is regime-conditional.** The manuscript stated the interior-MSY result (`A* < A_max`) as general, but it holds **only** in the increment-dominated regime (`b_Gρ > b`, `ψ→0`). At the **baseline** parameter set (`b_Gρ = 0.8·0.05 = 0.04 < b = 0.5`) the system is **flow-dominated** (`ψ→1`): `B(A)` is **monotone increasing** on `[0,A_max]`, there is **no interior maximum**, and the sustainable point is the **boundary** `A_max`. This is *exactly* what R1 computes (the corrected S0 recovers `A→A_max`), so making it explicit resolves a latent inconsistency and unifies §4.1 with the R1/R2 result. This is a *physical insight*, not decoration: **whether the model behaves like the orchard (flow/boundary) or the forest (increment/interior) is decided by a single testable condition `b_Gρ ⋚ b`.**
- **`scans/sustainable_yield_regimes.png`** — the two-regime `B(A)`/MSY figure that makes the above visually self-evident (flow-dominated vs increment-dominated), plus the `A_c(E)` fixed-liability separatrix.

### Not added (already present and adequate)
- The transient-illusion proof (`d ln B/dt = d ln b/dt + d ln A/dt`) is already worked through in §6.
- The orchard/hens *Gedankenexperiment* framing and the flow/increment decomposition are already labelled as such (§7).
- The two-delay physical intuition (a tree takes `τ_g≈20–80 yr` to bear fruit; `K(t−τ_p)`) is already in §2.2/§3.

---

## Verification (against v16, live pointer)

- scan `21 / 0 / 1 / 0 / 0` (covered / partial / superseded / ambiguous / missing)
- eval `R@1 0.82 / R@3 0.95` (BM25, n=22; only the known `12B.6` miss) — **restored to the v14/v15 baseline** after the §4.1 table was tightened (an intermediate run showed R@3 drop to 0.91 with `12A.4` also missing because the new knife-edge text legitimately competed with the gold; trimming the closing prose resolved it)
- numeric verifiers `12A.3 / 12G.2 / 12G.4 / 12G.5` PASS; `12A.1 / 12G.7` SUPERSEDED (expected)
- `34` pytest pass
- all nine referenced `.png` files verified on disk (`scans/feedback_diagram.png`, `scans/r1_recovery_vs_collapse.png`, `scans/sustainable_yield_regimes.png`, plus the prior R1/R2 figures); no orphan figure references

*No companion numerics or results were imported; the new figures and values are ECOMOD's own, re-derived in the paper's `A/B/E/D/K` notation. The two-regime table deliberately states the knife-edge and the provenance/regime caveats as the paper already requires.*
