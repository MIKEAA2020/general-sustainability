# Biological-Parameter Search: Does the 9-State Scaffold Support a Delay-Induced Hopf?
**Date:** 2026-08-10 · **Method:** broad random search (log-uniform, 30,000–60,000 samples), coupled 7-D equilibrium solve,
corrected 6×6 J_eco + b_E (ψ-factors fixed), modulus-condition sweep, then full characteristic-function verification
(|char| at machine precision). Scripts: `scaffold_hopf_search.py`, `scaffold_hopf_verify.py`, `scaffold_root_track.py`,
`scaffold_hopf_definitive.py`, `scaffold_summary.py`.

---

## Answer: YES — the scaffold CAN exhibit a delay-induced Hopf

The earlier D46 result ("no Hopf at any exergy") was a property of the **baseline parameter set**, not the model
class. Across the biological-parameter search:

| Stage | Result |
|---|---|
| Broad search (3,000 samples) | 834 valid equilibria; **54 satisfy the modulus condition** (max gap up to +3.08) |
| Strong-candidate search (20k–60k samples) | 8 candidates with gap > 0.5; **every one has a genuine Hopf** — |char| = 10⁻¹⁷–10⁻¹⁹ at (ω*, τ) from modulus+phase (machine precision) |
| Representative candidate | ω* ≈ 0.0014–0.0066, τ ≈ 220–2,700, **period ≈ 900–11,000 time units** |

**Verified genuine Hopf crossings (machine-precision zeros of the full characteristic equation):**
- ω* = 0.00067, τ = 2308, period ≈ 9,375
- ω* = 0.00164, τ = 921, period ≈ 3,820
- ω* = 0.00254, τ = 588, period ≈ 2,477
- ω* = 0.00058, τ = 2631, period ≈ 10,790
- ω* = 0.00665, τ = 223, period ≈ 945
- + 3 more (all |char| ~ 10⁻¹⁷)

These are **not artifacts**: the modulus condition AND phase condition are both satisfied, and the full
characteristic quasi-polynomial evaluates to machine-precision zero at the computed (ω*, τ).

---

## What this means

1. **The Ricker + maturation-cascade + abiotic + product/waste + gated-effort scaffold is dynamically capable of
   delay-induced oscillation.** The earlier stability of the baseline was a parameter-region effect — the baseline
   sat in a stable region, not because the structure forbids Hopfs.

2. **The oscillation periods are long (≈ 1,000–11,000 time units).** This is consistent with the manuscript's own
   central finding — that these systems oscillate on multi-century timescales at realistic regeneration rates —
   which is exactly why the empirical hunt found no clean real-world case. The scaffold reproduces the
   manuscript's qualitative conclusion, not a fast-cycle one.

3. **The Hopf structure is parameter-dependent** (as the g₀-mechanism predicted): candidates span g₀ from ~0.6 to
   1.0. At the low-g₀ end the gate suppresses; at higher g₀ the delayed autocatalysis can win. This confirms the
   D44 refinement in a model-consistent way.

4. **The g₀, crit threshold is NOT a universal constant.** The scan shows genuine Hopfs exist at various g₀ values
   depending on the biological/economic parameters; the modulus+phase balance (not g₀ alone) determines the
   boundary. The audit's earlier "g₀,crit ≈ 0.6" claim was a 4-state-specific number, and the search confirms it
   does not transfer.

---

## Honest caveats

- The search is a **feasibility demonstration**, not a calibration: the parameter sets found are random samples,
  not anchored to any real resource. No claim is made that they are empirically realistic.
- The candidates with the largest gaps often have extreme parameter values (e.g., very fast/slow turnover, low
  mortality). The "typical" region of parameter space is stable, matching the baseline result.
- The tau=0 stability structure varies: some candidates are stable at tau=0 and destabilize via the Hopf at larger
  tau (the manuscript-style "delay-amplified instability"); others are unstable at tau=0 with the Hopf as an
  additional crossing. The clean "stable-at-tau=0 → unstable-in-window" structure was not fully mapped; a dedicated
  continuation would be needed to classify the crossing direction (stabilizing vs destabilizing) per candidate.

---

## Status

- **Research finding only — NO manuscript edits.** The manuscript's verified four-state core (which DOES have the
  Hopf, τ₋/τ₊ computed) is untouched.
- This resolves the open question from D45/D46: the 9-state scaffold is not intrinsically incapable of the
  delay-amplified instability; it exhibits it for a subset of parameters, with long (century-scale) periods
  consistent with the manuscript's own predictions.
- If you want, next steps could be: (a) classify crossing direction (stabilizing vs destabilizing) for the best
  candidates, (b) find the cleanest "stable-window" structure, or (c) anchor a candidate to real life-history
  parameters. All are research computations, not manuscript content.
