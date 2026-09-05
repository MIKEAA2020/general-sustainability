# v17 — Review verdict: ecological insights, literature grounding, internal connections

Commit after `6c69a46` (v16) → v17. `VERSION revision=17`. Live pointer → `data/revisions/IMPLEMENTED_revision_ECOMOD_v17.md`. v1–v16 preserved.

Each answer below is grounded in (a) re-reading the manuscript and (b) where an *ecological* claim was proposed, **verifying it computationally** before adding it — so nothing decorative was asserted.

---

## Q1 — Additional non-decorative ecological insights / intuitions?

**Verdict: one genuine ecological insight merited — verified and added; several more were proposed and rejected because the model does not actually produce them (or they duplicate existing content).**

**Added — "recovery is not self-sustaining under the regeneration lag" (§13(8)(v)).** I integrated the `(1‴)` S0 starting from the **post-collapse extinction floor** (`A₀=A_ext`, `P₀≈0`) and found that at `τ_g ≥ 20` the stock **regrows, overshoots `A_max`, and re-collapses to the floor** — rather than settling at the sustainable boundary. Robust across `T=8000 yr`:

| `τ_g` (yr) | `A_peak` | fraction of run above `0.5·A_max` |
|:--:|:--:|:--:|
| 20 | 1.31 | 0.159 |
| 25 | 1.38 | 0.055 |
| 30 | 1.45 | 0.045 |
| 40 | 1.60 | 0.033 |
| 60 | 1.88 | 0.020 |

So the collapse is effectively **absorbing**, not a transient excursion. This is non-decorative: it *strengthens* the collapse claim, ties the §8 "recover vs collapse" result to the empirical "many collapsed stocks never rebuild" picture (Hutchings & Reynolds 2004; Neubauer et al. 2013), and gives the paper a richer ecological reading — **the regeneration lag is a recovery-*blocking* mechanism, not only a collapse mechanism.** (Note the same delay-driven liquidation as §13(8), but read from the recovery side; explicitly distinguished from the masking window and from the Allee-free fixed-liability threshold.)

**Rejected (tested, not true / duplicative):**
- *Hysteresis in the fixed-liability threshold* — the separatrix `A_c(E)` is single-valued in `E` (a fold), not a genuine hysteresis loop; rejecting avoided a wrong claim.
- *Sustained boom-bust limit cycle* — the regrow-overshoot-recollapse is a **transient**, not a sustained cycle (only 2 crossings of `0.5·A_max` at `T=4000`), so I explicitly described it as "absorbing," not oscillatory.
- *Allee effect* — the model has no Allee term (stated in §4.2); the recovery-blocking comes from the delay, not from low-density demography, so I did *not* reframe it as an Allee effect.
- *Regeneration-vs-density intuition* — the manuscript already notes `A_max/2` is the maximal-regeneration point (§4.1); adding a growth-curve figure would duplicate the v16 figures.

---

## Q2 — Additional non-decorative citations / literature grounding?

**Verdict: two genuinely-missing primary anchors merited — added; other candidate citations rejected as decorative or as importing companion results.**

**Added:**
1. **Schaefer (1954)** — the §4.1 surplus-production / MSY core. The manuscript uses "the Schaefer/forestry picture" and derives `B_max` / interior-`A*` (the Schaefer `MSY = rK/4` structure) but **never cited the source**. Added inline at §4.1 and consolidated in the §7 literature note. (Bull. Inter-Am. Trop. Tuna Comm. **1**(2):25–56.)
2. **Scheffer, Carpenter, Foley, Folke & Walker (2001)** — the §4.2 **saddle-node/fold with a vanishing safe basin** is precisely the catastrophic-shift / critical-transition structure, currently asserted without anchoring. Added at §4.2 (explicitly as a *framing*, e.g. "a loss of resilience precedes the switch; the switch is abrupt and hard to reverse"), and consolidated in §7. (Nature **413**:591–596.)
3. The field sources for the `τ_g` band (Poorter, Poeplau/IPCC, Hutchings & Reynolds, Neubauer) were already present — noted in the §7 consolidation so they are linked to the new §13(8)(v) insight.

**Rejected (decorative or would import non-own results):**
- Ricker/Beverton–Holt stock–recruitment curves — the model's `G(A)` is *logistic regeneration*, not a stock–recruitment function; citing them would be loose.
- Gordon (1954) open-access / Hardin (1968) tragedy-of-the-commons — not the mechanism here (no effort/rent dynamics in S0); would be decorative.
- Holling (1973) resilience — the v16 "recover fraction" already provides the measure; adding Holling without a resilience-functional link would be a citation for its own sake.
- Any companion result (P1–P5/E1–E4) — excluded per the standing guardrail; only *framing* vocabulary is borrowed, re-derived in this paper's notation.

---

## Q3 — Strengthen internal connections?

**Verdict: two concrete coherence gaps found and fixed.**

**Fixed:**
1. **The §6 "Falsifiable predictions" list was incomplete relative to the manuscript's own claims.** The abstract says "four predictions," but §4.1 states a **ψ flow-share prediction** ("more visible in flow-dominated/high-ψ systems — a falsifiable, GFN-faithful prediction") and §8 states a **`τ_g` recovery-vs-collapse cliff** — neither was in the predictions list. Now **items 5 and 6** (ψ locates the illusion; `τ_g` sets recovery vs collapse), and the abstract count reconciled "four" → "six." This makes §6 the single authoritative, complete prediction set and ties §4.1 + §8 into it.
2. **The abstract's two collapse mechanisms (§1) are now cross-linked to where each is established** — the "debt accumulation" channel (§13(3), full `(6′)`) and the "delay-amplified transient" channel (R1 §8) — and the new §13(8)(v) insight is cross-referenced from §8, so the recovery-blocking reading is visible from both the collapse side (§8) and the recovery side (§13).

**Left as-is (already connected, no change needed):**
- §4.1 regime-conditional MSY ↔ R1 "recover to boundary" (v16 already unified these).
- The through-line "weak/strong sustainability" (abstract `ψ` → §6 two masks → §10 P1 aggregation gap).
- §12 receipt ↔ §13 residual-risk structure (already cross-referenced).

---

## Verification (v17, live pointer)

- scan `21 / 0 / 1 / 0 / 0` (covered / partial / superseded / ambiguous / missing)
- eval `R@1 0.82 / R@3 0.95` (BM25, n=22; only the known `12B.6` miss) — **unchanged from the v14–v16 baseline** despite the new §4.1/§4.2/§6/§13 text
- numeric verifiers `12A.3 / 12G.2 / 12G.4 / 12G.5` PASS; `12A.1 / 12G.7` SUPERSEDED (expected)
- `34` pytest pass
- all new claims computationally verified (`reports/` unchanged; the new insight is encoded in `r1_basin`-compatible one-sided integration)

*No companion numerics or named results were imported; every new figure/value/claim is ECOMOD's own. The Schaefer and Scheffer citations are used as frames for claims the paper already derives.*
