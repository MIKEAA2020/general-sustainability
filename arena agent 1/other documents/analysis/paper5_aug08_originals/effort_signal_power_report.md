# Corrected internal report — effort signal & governance risk power analysis
(2026-08-08; internal working document, not for citation)

This replaces the fabricated/citation-placeholder text in the two external AI
reports ("Beyond Biomass...", "Quantifying Governance Risk...").  Every number
below is a verified computation from our own code; bracketed tags give the
exact source file/run so anything can be re-derived in seconds.

---

## 1. The core correction: effort vs biomass period and amplitude

Our earlier phrasing (and both external reports) attributed a single
"≈4-yr / ≈8-yr cycle" to the sampled-governance mechanism.  The two state
variables in fact oscillate at **different periods**, verified by spectrum and
crossing analysis on the converged tails (years 100–4000):

| cell | N (biomass) period | E (effort/quota) period | N p2p (% N*) | E p2p (% E*) |
|---|---|---|---|---|
| anchovy-class (r=1.6, g=1, T_r=3) | **4.0 yr** | **≈12 yr** | 1.4% | ~350% |
| sprat-class (r=0.8, g=2, T_r=7) | **8.0 yr** | **≈60 yr** | 2.2% | ~340% |

`[model: sampled_governance.py / power_demo.integrate_NZE; spectrum of
tail-300-yr E series]`

Key facts:
- **E period ≈ T_r × N period** (3×4=12; 7×8≈60).  The 4/8-yr figures are the
  BIOMASS cycles (small amplitude, 1–2% of N*); the effort/quota signal that
  "Beyond Biomass" argued we should detect runs at 12/60 yr.
- **The effort oscillation grows to full amplitude only after ~10³ yr**:
  sprat E p2p 0.7@150 → 1.6@300 → 5.1@600 → 7.1@1200 yr; anchovy 3.1@150 →
  8.7@1000 yr.  On realistic 100–400-yr horizons the effort spectrum is
  dominated by the **growth transient (trend)**, not a clean cycle — verified
  by periodograms (anchovy's top power at 260–515 yr, not 12 yr).
  `[model: power_demo growth-timescale run]`

**Bottom line:** switching observables from biomass to effort does NOT rescue
detectability.  The effort signal is larger in amplitude but longer in period
and far slower to grow.

---

## 2. Corrected power analysis (real numbers, correct bands)

Method: our sampled-governance operating model → annual effort series →
multiplicative lognormal observation error → Lomb-Scargle band power vs
per-series AR(1) red-noise null (120 sims, 95%) → fraction of 50 trials
detected.  `[model: power_demo.power / detect]`

| cell | band (yr) | horizon | σ noise | power |
|---|---|---|---|---|
| sprat-class (E~60 yr) | (30,120) | 100 | 0.1 | **1.00** |
| sprat-class | (30,120) | 100 | 0.3 | 0.24 |
| sprat-class | (30,120) | 200 | 0.3 | 0.58 |
| sprat-class | (30,120) | 400 | 0.3 | 1.00 |
| anchovy-class (E~12 yr) | (8,20) | 100–400 | 0.1–0.3 | **0.02–0.14** |
| cod-class (stable) | (8,20) | 100–400 | 0.1–0.3 | 0.00–0.06 (false-positive) |

Interpretation:
- The **sprat-class "power 1.0" at low noise is trend detection, not cycle
  detection** — at 100–200 yr only ~1.7 of the 60-yr cycles fit in the window,
  so the detector is really catching the run-up.  It is fragile at σ=0.3.
- The **anchovy-class signal is effectively undetectable** on any practical
  horizon (power ≈ 5–14%).
- The **cod stable cell is clean** (false-positive 0–6%).

The external report's example rows (power 0.85/0.82/0.91 at r=0.01/T_r=5 and
r=0.05/T_r=30) are **fabricated AND in the wrong regime**: our scan shows
r=0.01/T_r=5 is DRIFT (not a clean oscillation) and r=0.05/T_r=30 is STABLE —
the report invented power values for parameter cells that do not oscillate.

---

## 3. Slow-r branch (forests/aquifers) — verified boundaries

Re-run of the sampled scan (p2p % of N*; o=oscillatory, d=drift, s=stable):
`[model: sampled_governance.sampled_governance, T=6000, dt=0.05]`

| r | T_r=1 | 5 | 10 | 15 | 20 | 30 | 50 |
|---|---|---|---|---|---|---|---|
| 0.007 | s | s | s | s | s | s | s |
| 0.010 | o86 | d | d | d | d | d | d |
| 0.020 | o104 | o178 | o355 | o519 | o512 | o257 | o60 |
| 0.030 | o140 | o132 | o485 | o127 | o91 | o90 | d |
| 0.050 | o128 | o126 | o170 | o81 | o62 | s | s |

**Corrected statement** (the external report said "virtually any T_r, 60–90%"):
oscillation lives in **r ∈ (0.01, 0.05) yr⁻¹ and T_r ≲ 20–30 yr**, with
**amplitudes 60–500% of N*** (growing with r, peaking at intermediate T_r;
the 519% figure reflects near-basal-extinction swings exceeding N*), and
**three stability boundaries**: r ≲ 0.007 yr⁻¹ (below the window's low edge);
T_r ≳ 30–50 yr; r = 0.05 yr⁻¹ at large T_r (oscillates at short T_r, stabilises
beyond T_r≈30).

The **responsive-vs-frozen comparative framing** is the policy implication of
these boundaries: frozen/large-T_r is the stable side, and a responsive
5-yr review (SGMA-type) sits inside the risky window.

---

## 4. Citations — what to keep, what to strip

- **Strip all fabricated brackets** (`[[229]]` etc.) — no referents, no list.
- **Keep the real named primary sources** from our D9 search
  `[source: tau_window_search.md]`:
  - GFCM/44/2021/20 and GFCM/48/2025/2/5 (Adriatic small-pelagic MAP)
  - Mace et al. 2013/2014; Nature Conservancy 2016 (NZ QMS TAC-change rates)
  - Butterworth et al. (South African OMP review cycles)
  - Ricard et al. 2012 (RAM Legacy), Guentner et al. 2024 (G3P),
    USGS MCS 2026
- **Tag every number** `[model: file/run]` or `[source: name]` (done above).

---

## 5. Status vs the two external reports

| claim | external report | verified truth |
|---|---|---|
| effort signal large in amplitude | ✓ correct | ✓ 80–240% of E* |
| biomass small (1–2% of N*) | ✓ correct | ✓ |
| effort period ≈ 4/8 yr | ✗ wrong | ≈ 12/60 yr (≈ T_r × N-period) |
| effort oscillation detectable on 100-yr horizon | ✗ implied yes | sprat marginal (trend), anchovy ≈ no |
| slow-r oscillates "virtually any T_r, 60–90%" | ✗ wrong | r∈(0.01,0.05), T_r≲20–30, 60–500%, 3 boundaries |
| example power rows (0.85/0.91) | ✗ fabricated | see table §2 |
| citations | ✗ fabricated brackets | real named sources only |

---

## 6. Forward plan (from the corrected picture)

1. **Build the MSE power analysis properly** as a *negative-result design*:
   target the corrected effort bands (12/60 yr), horizons 100–1000 yr,
   noise 0.1–0.3; expect low power for anchovy-class and trend-dominated
   detection for sprat-class → quantify it and report it as the finding.
2. **Field-test design:** the only tractable signature is the effort/quota
   **growth transient** after a review-cycle change (monotone run-up), not a
   completed cycle — pre-register an onset test on that.
3. **Slow-r qualitative test:** responsive vs frozen basins (SGMA-type)
   over several 5-yr review cycles — century-scale boom-bust in extraction
   vs steady decline.
4. **Upper-fold SNPO** remains the last computational open item (lower fold
   confirmed at collocation grade; upper SNPO-consistent, not pinned).
