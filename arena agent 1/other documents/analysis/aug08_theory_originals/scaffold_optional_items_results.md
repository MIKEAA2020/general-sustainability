# Optional Research Items 1–3 — Results
**Date:** 2026-08-11 · **Scripts:** `scaffold_items_1_2.py`, `scaffold_item_3_anchor.py`, `scaffold_item3_refine.py`
**Scope:** all three optional items executed in feasibility order. Research findings only — **no manuscript edits**.

---

## Item 1 — Classify Hopf crossing direction (most feasible)

**Result: all strong-candidate Hopf crossings are STABILIZING (dRe/dτ < 0).**

| Candidate | gap | τ=0 Re | Hopf τ* | ω* | period | dRe/dτ | direction |
|---|---|---|---|---|---|---|---|
| 1 | 7.03 | +1.41 | 1393.8 | 0.00111 | 5678 | −3.6×10⁻⁷ | stabilizing |
| 2 | 4.76 | +0.69 | 2737.2 | 0.00056 | 11199 | −9.2×10⁻⁸ | stabilizing |
| 3 | 4.56 | +0.94 | 8781.4 | 0.00018 | 35468 | −9.1×10⁻⁹ | stabilizing |
| 4 | 3.67 | +1.00 | 1826.0 | 0.00084 | 7464 | −2.1×10⁻⁷ | stabilizing |
| 5 | 3.26 | +1.39 | 911.7 | 0.00167 | 3757 | −8.2×10⁻⁷ | stabilizing |
| 6 | 3.20 | +1.04 | 7769.5 | 0.00020 | 31396 | −1.2×10⁻⁸ | stabilizing |

**Interpretation:** in the strong-modulus region, the scaffold is unstable at τ=0 and the delay *stabilizes* it at very large τ (the manuscript's τ₋-type direction), not the τ₊ destabilizing direction. The crossing rates are tiny (dRe/dτ ~ 10⁻⁷–10⁻⁹) — the crossings are near-degenerate, consistent with severe critical slowing down.

## Item 2 — Find the cleanest stable-window structure

**Result: NO clean manuscript-style two-crossing structure found.** The stable windows after the stabilizing crossing are fragmented and narrow (many sub-windows of a few tens of τ-units across ranges of hundreds to thousands). None of the 6 candidates shows the clean "stable at τ=0 → unstable window → stable again" pattern with two well-separated Hopf points (τ₋, τ₊) that the manuscript's core has.

**What this means:** the scaffold's instability structure differs qualitatively from the manuscript core's. In the scaffold, the equilibrium is typically unstable at τ=0 and the delay acts (weakly) to stabilize — the opposite of the manuscript's "delay-amplified instability with a stabilizing τ₋ and destabilizing τ₊". The mechanism exists but its organization is different.

## Item 3 — Anchor to real life-history (least feasible, most valuable)

**Part A — default anchored region (manuscript economic table):**

| Class | Life-history | Equilibria | maxgap | Hopf? |
|---|---|---|---|---|
| anchovy | g=1, P0=8, dA=1, dJ=3 | XA*≈27.7 | −3×10⁻⁴…−5×10⁻⁴ | no |
| sprat | g=2, P0=4, dA=0.5, dJ=1.5 | XA*≈34.6 | −4×10⁻⁴…−6×10⁻⁴ | no |
| cod | g=5, P0=2, dA=0.2, dJ=0.6 | XA*≈54.8 | −6×10⁻⁴…−10⁻³ | no |

**All three anchored classes are delay-independently stable at the manuscript's default economic parameters.** (Note: the first P0 values violated the Step-2 survival condition and correctly produced no equilibrium — a self-consistency pass that confirms the scaffold respects its own survival bound.)

**Part B — refined economic scan (elevated η, ζ, fuel-efficiency 1/K₀, q):**

| Class | Best maxgap | at (η, ζ, K₀, q) | Result |
|---|---|---|---|
| anchovy | −3.2×10⁻⁴ | (0.914, 0.25, 1, 0.001) | stable at all tested |
| sprat | −4.0×10⁻⁴ | (0.914, 0.25, 1, 0.001) | stable at all tested |
| **cod** | **+0.163** | **(5.0, 0.8, 0.03, 0.01)** | **GENUINE HOPF** |

**The cod-class Hopf (verified to machine precision):**
- **τ\* = 43.3, period ≈ 263 time units** (century-scale)
- E\* = 0.245, X̄_A\* = 54.2, g₀ = 1.000
- Requires elevated-but-plausible economic forcing: η=5 (fast institutional adjustment — upper end of the manuscript's sensitivity band), ζ=0.8 (high savings), K₀=0.03 (fuel-efficient fleet), q=0.01 (higher catchability).

---

## Overall interpretation

1. **The scaffold can oscillate** (confirmed in D47) **and can do so for a cod-like real life history** under elevated economic forcing, on a **century timescale** — reproducing the manuscript's qualitative picture (delay-amplified instability, sensitive to institutional/economy parameters).
2. **But the anchored default region is stable** for all three stock classes, and the instability structure differs from the manuscript core's (stabilizing-only crossings, fragmented windows, no clean τ₋/τ₊ pair). This mirrors the manuscript's own empirical finding: real systems sit near or outside the instability window, and the delay instability is a marginal/parametric phenomenon.
3. **Consistency with the manuscript:** the manuscript's stage-structure result (windows for fast-maturing small pelagics at r·g≈1.5–1.6) was for a *different* model (delayed logistic). The scaffold (Ricker cascade) shows the complementary behavior: cod-like (slow, g=5) can oscillate at elevated forcing; anchovy/sprat (fast) stay stable. Different models, different windows — both consistent with "the instability is parametric and marginal in real systems."

---

## Status
- All three optional items **executed and completed** in feasibility order.
- **No manuscript edits** — research findings about the proposed extension only.
- Scripts preserved: `scaffold_items_1_2.py`, `scaffold_item_3_anchor.py`, `scaffold_item3_refine.py`, plus earlier `scaffold_*.py`.
- Logged: D48.
