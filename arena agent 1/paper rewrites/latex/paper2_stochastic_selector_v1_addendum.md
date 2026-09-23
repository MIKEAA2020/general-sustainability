# Stochastic-Selector Paper — v1 Addendum (disposition record)

**Version:** `paper2_stochastic_selector_v1` (lineage `paper2_stochastic_selector_*`; the **D1 theory** of roadmap v3–v7).
**Title:** *The Stochastic Selector: Exact Rational Belief-State Safety Values under Partial Observation*.
**Seeding:** the viable-selector paper's §8 outlook (fulfilled here), the calculus paper's §9 probabilistic development, and the v47 audited grid instance.

## 1. Content → D1 mapping

| D1 component | Where |
|---|---|
| Belief-state viability kernels as the stochastic selector | §2: Γ^s_k(b) = argmax actions of the value recursion; Theorem 1 (value recursion, Smallwood–Sondik specialization); selector-framework correspondence reading |
| **Piecewise-linear value iteration with rational α-vectors** | §3 Proposition 1: V_k = max over Γ_k; rational propagation under rational data; exact dedupe; honest worst-case exponential growth (|Γ_{k+1}| ≤ |A||Γ_k|^{|Y|}) |
| **Support degeneration** | §3 Proposition 2: deterministic-limit survived-mass formula (max over blind sequences of survived prior mass); recovers the companions' robust verdicts; implies the minimal-mass deficit bound |
| **Deficit bounds** | §4 Proposition 3: chance-constrained bound (Δ ≥ δ), degenerate minimal-mass bound, monotonicity; certificates = computable deficit lower bounds; exact deficit computable at finite horizons |
| **Certificate–value agreement on the audited classes** | §5 Theorem 2: on the 48-cell hidden-regime grid over the declared hold class — α-recursion ≡ closed form; certificate partition ≡ value boundaries (viable ⟺ V ≡ 1; CA ⟺ V₁ < 1; timing ⟺ V₁ = 1 < V_{T+1}); kink locus ≡ certificate boundary z₀ = 2; deficit exactly ½ on all 42 nonviable cells; unrestricted class: V = 1 exactly on {z₀ ≥ 2} (timing cells = in-window adaptivity lift) |

## 2. Verification record (`paper2_stochastic_selector_v1_verify.py`, stdlib, exact)
**10/10 checks pass**: S1 two-floor POMDP (Γ₁ = {(1,0),(0,1)}; V_k(b₀) = ½; chance bound attained; PL probes at 11 beliefs vs direct max(b₁,b₂)); S2 survived-mass == brute force; every sequence loses a branch at (3/2, 2) ⇒ deficit ≥ min mass; S3 agreement (48 cells × k ≤ 4; partition; kink; deficit ½); S4 unrestricted class (value 1 ⟺ z₀ ≥ 2, k ≥ 2); S5 rationality books (384 α-vectors, entries rational — here 0/1); S6 deficit monotonicity.
Fixes during verification: import (Fraction), probe reference (direct value max(b₁,b₂), not half-max), and scratch-code cleanup before first archived run.

## 3. Build and probes
- Tectonic 0.15.0; `main.pdf` 108,461 B, **3 pp**; **zero Overfull \hbox** (two display overflows found in the first build — the backup display spacing and the two-part closed form — split/tightened before shipping).
- pymupdf probes: 0 unresolved `??`; all section content and declarations verified present.

## 4. Files
- `paper2_stochastic_selector_v1.tex` / `.pdf`; `paper2_stochastic_selector_v1_verify.py`
- `paper2_stochastic_selector_v1_source.zip` (4 entries)
- Related in this batch: `paper2_viable_selector_v2` (layout repair: Table 1 wrapped p-columns + two split displays; **zero overfull**; content unchanged; v1 untouched) with its own addendum and source zip.
- Roadmap: v8 records both.

## 5. Status
Track D: **D1 complete** (the stochastic selector; D2–D3 named in §7 as the next theory items). C3 (five-layer successor absorbing D2/D3/D6) remains; papers 1–2 submission-ready pending owner venue decisions; spine paper at v2 (layout-repaired).
