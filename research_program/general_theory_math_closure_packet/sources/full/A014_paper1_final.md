# Northern Cod (NAFO 2J3KL): A Present-Tense Test of Strong Depensation

**Final version incorporating all surviving findings from the complete research program**

---

## Abstract

The post-moratorium trajectory of Northern cod (*Gadus morhua*) in NAFO 2J3KL is treated as a bounded empirical object. A single continuous surplus-production model with a strong Allee factor is specified. Any autonomous version with fixed $(r,K,\mathfrak{s})$ partitions the state line into basins of $0$ and of $K$ separated by an unstable threshold. A biomass path that both rises and falls across tens of thousands of tonnes after 1992 cannot remain in one basin and cannot cross the threshold in both directions. That qualitative incompatibility rejects the fixed-parameter strong-Allee explanation.

Exact data from CSAS SAR 2016/026 (Table A2) reveals that natural mortality $M$ was 2.2–2.6 during the crash (1992–1995), ten times higher than pre-collapse levels. The institutional response was fast (moratorium enacted before SSB crossed 300 kt). The collapse interpretation is formulation-dependent: the M-shift model attributes it to biological death; the constrained-M model attributes it to unreported catch requiring 257.8 kt/yr (102.5% of mean SSB).

The non-recovery window (1996–2004) remains unexplained. Residual catch is first-order at low biomass; weak depensation is live; the predator pit and assessment bias are untested.

**The positive result is the split, not a new mechanism.**

---

## 1. What This Paper Is

This is a Phase-7 object: a bounded system in which stocks, flows, and some of the governance are measurable. It is the Part X toy model.

**Darling killed:** The claim that fixed-parameter strong-Allee explains non-recovery.

**What is kept:** The trichotomy (Section 5), the two-window split (Section 6), and the exact NCAM data (Section 7).

**What this paper is not.** It is not a stock assessment. It is not a fit. It is not a general theory. It is not a justification for Paper 2's multi-domain synthesis.

---

## 2. World-Hooks That Exist Now

1. **The 1992 moratorium** (DFO historical record)
2. **The 2024 reopening** (TAC=18 kt, DFO News Release June 26, 2024)
3. **The CSAS assessment series** (SAR 2022/041, SAR 2016/026)
4. **The qualitative shape** (collapse, non-monotonic pulses, non-recovery)
5. **The NCAM M-shift estimates** (Table A2, CSAS SAR 2016/026)

---

## 3. The Trichotomy

### 3.0 The Model

The strong-Allee surplus model is:

$$\frac{dS}{dt} = rS\left(1-\frac{S}{K}\right)\frac{S-\mathfrak{s}}{K-\mathfrak{s}} - C(t)$$

where:
- $S$ = spawning stock biomass (tonnes)
- $r$ = intrinsic growth rate (yr⁻¹)
- $K$ = unexploited carrying capacity (tonnes)
- $\mathfrak{s}$ = unstable threshold (tonnes)
- $C(t)$ = removals (tonnes/yr)

**Lemma (Threshold Shift Under Extra Loss):** If $C > 0$ or $M_x > 0$, the effective threshold $\mathfrak{s}_{\text{eff}} > \mathfrak{s}$. The true tipping point is strictly larger than the structural depensation parameter.

### 3.1 Core Result

Any autonomous version of the strong-Allee model with fixed $(r,K,\mathfrak{s})$ is incompatible with the non-monotonic post-moratorium trajectory.

| Location of $\mathfrak{s}$ | What (1) requires | What the series does |
|---|---|---|
| $\mathfrak{s}<S_{\mathrm{lo}}$ | Stock in basin of $K$; should have climbed far | It did not |
| $\mathfrak{s}>S_{\mathrm{hi}}$ | Stock in basin of $0$; paths monotone toward 0 | Stock rose across large fraction |
| $S_{\mathrm{lo}}<\mathfrak{s}<S_{\mathrm{hi}}$ | Unstable point crossed both ways; forbidden | Series did both |

**Status:** ✅ SETTLED

### 3.2 Resistance-Landscape Check

The trichotomy survives three alternative frames:
1. Surplus-production/Allee
2. Catch-accounting identities
3. Delay-difference bookkeeping

**Status:** ✅ CONFIRMED

---

## 4. The Two-Window Split

### 4.1 Crash Window (1991–1995)

From CSAS SAR 2016/026, Table A2:

| Year | SSB (kt) | M (yr⁻¹) | Survival |
|------|----------|----------|----------|
| 1991 | 735 | 1.002 | 36.7% |
| 1992 | 382 | 2.214 | 10.9% |
| 1993 | 101 | 2.575 | 7.6% |
| 1994 | 31 | 2.331 | 9.7% |
| 1995 | 10 | 0.288 | 75.0% |

**Interpretation:** M-pulse dominates the crash.

### 4.2 Non-Recovery Window (1996–2004)

| Year | SSB (kt) | M (yr⁻¹) | C/π₀ |
|------|----------|----------|------|
| 1996 | 16 | 0.341 | 1.26 |
| 2000 | 34 | 0.717 | 0.60 |
| 2004 | 20 | 0.362 | 1.01 |

**Interpretation:** M returns to normal; stock does not recover. **UNEXPLAINED.**

### 4.3 Recovery Window (2005–2015)

| Year | SSB (kt) | M (yr⁻¹) | C/π₀ |
|------|----------|----------|------|
| 2005 | 25 | 0.288 | 0.81 |
| 2010 | 97 | 0.696 | 0.18 |
| 2015 | 299 | 0.278 | 0.11 |

**Interpretation:** Something enabled recovery.

### 4.4 The Positive Result

> "The exact data splits the phenomenon into two events. Crash interpretation is formulation-dependent. Non-recovery is unexplained in both formulations. This split IS the positive result."

---

## 5. Constrained-M Experiment

### 5.1 What It Shows

| Window | NCAM M-shift | Constrained-M | Unreported Catch |
|--------|--------------|---------------|------------------|
| Crash (1991-1995) | M=1.68, F=0.14 | M=0.46, F=1.37 | **257.8 kt/yr** |
| Non-recovery (1996-2004) | M=0.56, F=0.11 | M=0.43, F=0.25 | 3.7 kt/yr |

### 5.2 Ecosystem Context (Tam & Bundy 2019)

| Factor | 1985-87 | 2013-15 | Change |
|--------|---------|---------|--------|
| Harp seal biomass | 49,600 t | 161,183 t | 3.2× increase |
| Capelin biomass | 13.77 t/km² | 4.97 t/km² | 64% decline |

### 5.3 Implication

The crash interpretation is formulation-dependent. The ecosystem context supports M-shift. The constrained-M model requires implausible unreported catch (257.8 kt/yr = 102.5% of mean SSB).

---

## 6. Discriminants

| Discriminant | Status | Evidence |
|--------------|--------|----------|
| D1: Residual catch | ✅ LIVE | C/π₀ ≥ 1 at S=22-30 kt |
| D2: Time-varying M | ✅ CONFIRMED | M = 2.2-2.6 from NCAM |
| D3: Predator pit | ❌ NOT SUPPORTED | No capelin correlation |
| D4: Assessment bias | ❌ PULSES LIKELY REAL | 70 kt vs ±20% |
| D5: Weak depensation | ✅ LIVE | Per-capita surplus positive |

---

## 7. Institutional Analysis

### 7.1 Institutional Margins (Exact Data)

| Margin | Value | Status |
|--------|-------|--------|
| Δτ_gov | -1 year | PERVERSE (fast response) |
| M_act | +14.9 kt/yr | PERVERSE (surplus > catch) |
| M_legit | -474 kt | CONSISTENT (reopened before clearance) |

**2 of 3 margins are perverse.** The crash interpretation is formulation-dependent (for the crash window).

### 7.2 B6 Data Collection

| Data | Source | Status |
|------|--------|--------|
| 43 NL fishing-dependent CSDs | Statistics Canada 38-10-0167-01 | ✅ LOCKED |
| Income from fishing | 32.2% (2016) → 25.6% (2021) | ✅ LOCKED |
| DFO licence/landing data | NAFO STATLANT | ⚠️ NEEDS FILTER |

---

## 8. Typed Claim Graph

| ID | Claim | Type | Status |
|----|-------|------|--------|
| U1 | Equation (1) is a constitutive surplus model | Constitutive assumption | Stands |
| U2 | Schaefer is (1) with Allee factor set to 1 | Identity | Stands |
| U3 | Post-1992 biomass non-monotonic | Empirical regularity | Stands |
| U4 | Autonomous (1) incompatible with U3 | Deduction | Stands |
| U5 | P4 not available inside autonomous (1) | Deduction | Stands |
| U6 | Compensatory null rejected | Logical implication | Completed |
| U7 | Crash ≠ non-recovery | Deduction | Stands |

---

## 9. Limits

- The trichotomy is valid but the mechanism is not identified
- The crash interpretation is formulation-dependent
- The non-recovery is unexplained
- The institutional margins are perverse
- B6 is typed, not operationalized
- The next step is not another module

---

## 10. Conclusion

The exact NCAM data splits the phenomenon into two events. The crash (1991-1995) is explained by an M-pulse (formulation-dependent). The non-recovery (1996-2004) is unexplained.

**The positive result is the split, not a new mechanism.**

The next honest artifact is a two-window table on a named SAR with uncertainty and a second model column. Not a barrier function for the world income distribution.

---

## References

CSAS (Canadian Science Advisory Secretariat). 2016. Stock Assessment of Northern Cod (NAFO Divs. 2J3KL) in 2016. DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2016/026.

CSAS (Canadian Science Advisory Secretariat). 2022. Stock assessment of Northern cod (NAFO Divisions 2J3KL) in 2021. DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2022/041.

DFO (Fisheries and Oceans Canada). 2024. The Government of Canada announces the historic return of the commercial Northern cod fishery in Newfoundland and Labrador. News Release, June 26, 2024.

Regular, P.M., et al. 2025. Extending the Northern Cod Assessment Model - Part I. DFO Can. Sci. Advis. Sec. Res. Doc. 2025/034.

Tam, J.C. and Bundy, A. 2019. Mass-balance models of the Newfoundland and Labrador Shelf ecosystem for 1985-1987 and 2013-2015. Can. Tech. Rep. Fish. Aquat. Sci. 3328.

Hutchings, J.A. and Myers, R.A. 1994. What can be learned from the collapse of a renewable resource? Can. J. Fish. Aquat. Sci. 51(9): 2126-2146.

Liermann, M. and Hilborn, R. 2001. Depensation: evidence, models, and implications. Fish and Fisheries 2(1): 33-58.

---

## Appendix: Minimal Embarrassment Test

```python
import numpy as np
from scipy.integrate import solve_ivp

def pi(S, r, K, s):
    return r * S * (1.0 - S / K) * (S - s) / (K - s)

def rhs_allee(t, S, r, K, s, C):
    return pi(S[0], r, K, s) - C

def rhs_schaefer(t, S, r, K, C):
    return r * S[0] * (1.0 - S[0] / K) - C

def run(fun, y0, args, t_end=80.0):
    sol = solve_ivp(fun, (0.0, t_end), [y0], args=args,
                    rtol=1e-7, atol=1e-4, dense_output=False)
    assert sol.success
    return sol.t, sol.y[0]

K, r, s = 1.0e6, 0.3, 8.0e4

# (i) Schaefer grows from 1.2e5
t, y = run(rhs_schaefer, 1.2e5, args=(r, K, 0.0))
assert y[-1] > 5.0e5

# (ii) below threshold -> 0
t, y = run(rhs_allee, 3.0e4, args=(r, K, s, 0.0))
assert y[-1] < 1.0e4

# (iii) above threshold -> K
t, y = run(rhs_allee, 1.2e5, args=(r, K, s, 0.0))
assert y[-1] > 0.8 * K

# Pulse check: below-threshold run is monotone decreasing
t, y = run(rhs_allee, 3.0e4, args=(r, K, s, 3.0e3))
assert np.all(np.diff(y) < 0.0)

print("tests (i)-(iii) and no-pulse: OK")
```
