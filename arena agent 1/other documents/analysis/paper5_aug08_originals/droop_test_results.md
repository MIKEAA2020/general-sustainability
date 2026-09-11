# Droop slow-nutrient coupling test — results (2026-08-08)

**Question asked:** can coupling the manuscript's three-state core (Candidate A)
to a Droop-type internal-quota / external-nutrient subsystem shift the
delay-instability window in regeneration rate r upward toward real fish rates
(r ≈ 0.2–1.5 yr⁻¹), where the base model predicts delay-independent stability?

**Short answer: NO.** Every Droop variant tested leaves the upper edge of the
delay-Hopf window at r ≈ 0.019–0.023 yr⁻¹ — at or *below* the base model's
0.022 (η = 0.914) and far below its maximal 0.061 (η = 3.0) — and never
approaches real fish rates. No Droop variant produces any Hopf crossing at any
r ≥ 0.024 yr⁻¹. Recommendation: do not add Droop nutrient coupling to the
manuscript; the negative result is documented here and in `deep_research_report.md` §D6.

All numbers below were computed this session with `droop_test.py`
(τ-free Hopf-crossing criterion `|vᵀ(iωI−J₀)⁻¹u| = 1` on the linearised DDE,
cross-validated by direct RK4-DDE nonlinear integration).

---

## 1. Pipeline validation (criterion reproduces manuscript numbers exactly)

Hopf crossings at baseline r = 0.02 yr⁻¹, η = 0.914:

| Core | crossing | ω (yr⁻¹) | τ₀ (yr) | period (yr) | manuscript |
|---|---|---|---|---|---|
| gated (effort-saturation-corrected) | lower | 0.025192 | **3.6662** | 249.4 | τ₋ ≈ 3.666 ✓ |
| gated | upper | 0.039437 | **150.3585** | 159.3 | τ₊ ≈ 150.36 ✓ |
| ungated | lower | 0.023948 | **6.8814** | 262.4 | τ₋ ≈ 6.88 ✓ |
| ungated | upper | 0.044169 | **132.3749** | 142.3 | τ₊ ≈ 132.4 ✓ |

Base r-windows (delay-induced Hopf pair exists), matching deep-research D2:

| Core | η | window (yr⁻¹) | D2 reference |
|---|---|---|---|
| gated | 0.914 | (0.00798, 0.02227) | (0.0081, 0.0222) ✓ |
| gated | 3.0 | (0.00678, 0.06116) | (0.0066, 0.0618) ✓ |
| ungated | 0.914 | (0.00772, 0.02416) | — |
| ungated | 3.0 | (0.00678, 0.06318) | — |

## 2. Droop coupling tested (physiologically correct form)

Growth law μ(q) = r·(1 − q_min/q), so the species' maximal rate is the
manuscript's r and nutrient scarcity only slows growth below r. Added states:
external nutrient S and internal quota q (Droop 1973):

    dN/dt = μ(q)·N·(1 − N/K) − q_c·E·N
    dS/dt = D·(S_in − S) − ρ_max·S/(K_S+S)·N
    dq/dt = ρ_max·S/(K_S+S) − μ(q)·q

Z, E equations unchanged (delay τ only in the effort equation, as in the base
core). q_min = 0.1, K_S = 10 in all variants; gated core, η = 0.914.

| variant | D | S_in | ρ_max | interior-equilibrium r-bands | delay-Hopf window (yr⁻¹) |
|---|---|---|---|---|---|
| rich | 0.5 | 500 | 0.5 | [0.0081,0.0111] ∪ [0.0167,0.0192] ∪ [0.0233,2.0] | [0.0081,0.0111] ∪ [0.0167,0.0192] → **upper edge 0.0192** |
| moderate | 0.5 | 100 | 0.5 | [0.005, 2.0] | (0.0079, **0.0222**) ≈ base |
| lean | 0.2 | 50 | 0.2 | [0.005, 2.0] | (0.0081, **0.0228**) |
| very lean + slow | 0.05 | 100 | 0.1 | [0.005, 2.0] | (0.0081, **0.0233**) |

Compare: base upper edge 0.0223 (η = 0.914), 0.061 (η = 3.0); real fish
r ≈ 0.2–1.5. **The Droop coupling moves the window at most trivially (lean
variants: +0.0005 to +0.0010) and never upward toward fish rates.**

Two structural observations:
1. **Rich/large nutrient pools make the interior equilibrium r-disconnected**
   (exists only in disjoint low-r bands). At moderate-to-high r the stock sits
   at a near-capacity nutrient-saturated state (N* ≈ 98.5–99.9 vs base 89.6 at
   r = 0.02), which is delay-stable (0 crossings).
2. **Equilibria are residual-verified** (|F| < 1e-9); "no equilibrium" entries
   are genuine absence, not solver failure.

## 3. Why it cannot work — mechanism (verified eigenvalues of J₀)

The Droop quota's self-relaxation is exactly ∂q̇/∂q = −(μ′(q)q + μ(q)) = **−r**
(timescale 1/r); the S-pool relaxation is ≥ D with the uptake term
ρ_max·N·K_S/(K_S+S)² growing with the throughput r·q·N*.

| r (yr⁻¹) | 1/r (yr) | quota mode ≈ −r (yr) | S-pool −(D+ρ′N*) (yr) | overall slowest mode |
|---|---|---|---|---|
| 0.01 | 100 | 100 | 1.5 (mod) / 4.9 (lean) | 127 (mixed N/quota, slow) — but already inside base window |
| 0.02 | 50 | 50 | 1.3 (mod) / 3.7 (lean) | 56 (mixed N/quota, slow) — already inside base window |
| 0.1 | 10 | 10 | 1.2 (mod) / 3.1 (lean) | 17 |
| 0.5 | 2 | 2.0 | 1.2 | effort mode 16.8 (base model's own) |
| 1.0 | 1 | 1.0 | 1.0 | effort mode 16.8 |
| 1.5 | 0.67 | 0.7 | 0.7 | effort mode 16.8 |

(Eigenvalues from the log: e.g. moderate at r=0.5:
[−0.8596 (S), −0.4979 (q≈−r), −0.4395, −0.2000 (Z), −0.0595 (E)]; the
−0.0595 effort mode is present in the base model too.)

So: the Droop subsystem provides a genuinely slow mode **only** in the low-r
band where the base model is *already* unstable; at fish-like r it contributes
only fast modes (≤ ~5 yr). A growth-coupled nutrient pool cannot be slow at
large r because its throughput scales with r — slowness requires an
r-INDEPENDENT exchange rate, which is precisely what the manuscript's four-state
core implements via ω_A ≈ 10⁻³ yr⁻¹ — and that core *narrowed* the window to
(0.0074, 0.0247). The Droop test therefore corroborates, rather than overturns,
the disjointness result (D2): the instability domain (slow r, century periods)
and the observable domain (fast r, short periods) remain disjoint.

## 4. Direct nonlinear verification (RK4-DDE, τ = 5.5 yr, gated core)

| system | r | tail behaviour |
|---|---|---|
| base | 0.02 | sustained cycle, P = 268.4 yr, amp(N) = 7.22 |
| base | 0.3 / 1.0 | decays to equilibrium (delay-stable) |
| Droop (moderate) | 0.02 | sustained cycle, P = 270.2 yr, amp(N) = 7.58 (≈ base) |
| Droop (moderate) | 0.2 / 0.5 | decays to equilibrium (delay-stable) |

Linear criterion and nonlinear integration agree at every tested point.

## 5. Status and recommendation

- **Verified:** pipeline reproduces manuscript τ₋/τ₊ and D2 windows exactly;
  Droop coupling does not extend the r-window upward (upper edge ≤ 0.0233 in
  all variants); quota mode = −r exactly; nonlinear confirmation.
- **Not run / not claimed:** no DDE-BIFTOOL-class collocation Floquet tracking
  for the Droop system (not needed for the negative result — it is a linear
  Hopf-existence statement, the same class as D2's); no Droop variant with a
  separate μ_max (that form removes r from the growth law — the equilibrium
  becomes r-independent, which is not a meaningful test).
- **Manuscript:** no edits made. Negative result; recommend no change to the
  manuscript. Recorded in `deep_research_report.md` §D6.
