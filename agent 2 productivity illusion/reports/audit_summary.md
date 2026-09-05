# scan_revision — Audit summary
*Generated 2026-09-05T23:21:03.149026Z*

## Coverage
**Master items: 22.** Covered: 21 · Partial: 0 · Missing: 0 · Superseded: 1 · Ambiguous: 0.

## Master claims and status
| ID | Status | Score | Auto tier | Model | Note |
|---|---|---|---|---|---|
| 12A.1 | superseded | 0.90 | auto-covered | corrected (1‴) | Head-line masking numbers were computed on the ORIGINAL mode |
| 12A.2 | covered | 0.86 | auto-covered | corrected (1‴) | K->0 blow-up fixed via A_ext extinction floor + clamps. |
| 12A.3 | covered | 0.86 | auto-covered | original | D_E method-dependent (5.26/6.74/18.70); verified 5.26. |
| 12A.4 | covered | 0.84 | auto-covered | original (see note) | Knife-edge chi=1 <=> rho=3q flagged as non-generic. |
| 12B.5 | covered | 0.62 | auto-covered | corrected (1‴) | per-capita footprint constant; endogenising e, r_opt offered |
| 12B.6 | covered | 0.62 | auto-covered | corrected (1‴) | gross gamma E retained as named supplement variant. |
| 12B.7 | covered | 0.64 | auto-covered | corrected (1‴) | K is algebraic, not a state; system is 3-D. |
| 12C.10 | covered | 0.63 | auto-covered | corrected (1‴) | complete scenario/parameter table. |
| 12C.8 | covered | 0.64 | auto-covered | corrected (1‴) | state no interpolation / use non-multiple step. |
| 12C.9 | covered | 0.90 | auto-covered | corrected (1‴) | state grid range; normalise Re lambda by r. |
| 12D.11 | covered | 0.79 | auto-covered | original (see note) | cite Hutchinson 1948; soften Haberl & Aubauer novelty. |
| 12D.12 | covered | 0.63 | auto-covered | original (see note) | correct Brander-Taylor characterisation. |
| 12D.13 | covered | 0.88 | auto-covered | original (see note) | GFN reference list adopted. |
| 12D.14 | covered | 0.85 | auto-covered | original (see note) | E5 cleanliness: antibiotic, elevator, per-year, units, tense |
| 12E.1 | covered | 0.87 | auto-covered | original (see note) | verified-correct list preserved ('do not fix'). |
| 12G.1 | covered | 0.93 | auto-covered | original (see note) | four falsifiable predictions stated. |
| 12G.2 | covered | 0.90 | auto-covered | original | basin-shrinkage 0.506->0.042; ORIGINAL-model S0. Corrected S |
| 12G.3 | covered | 0.90 | auto-covered | corrected (1‴) | full dimensionless group set s,g,f,theta,tau. |
| 12G.4 | covered | 0.90 | auto-covered | original | B/C = environment recovers, humans collapse (opposite framin |
| 12G.5 | covered | 0.90 | auto-covered | original | (20,20) recovers / (30,25) collapses; min-M grid-sensitive. |
| 12G.6 | covered | 0.76 | auto-covered | corrected (1‴) | submission hygiene: May orphan, Modeling/Modelling, keywords |
| 12G.7 | covered | 0.90 | auto-covered | corrected (1‴) | Jevons rebound, tau_D asymmetry, omega=0, trivial equilibriu |

## Key numeric verifications re-checked

- **12A.1** — superseded (verdict) — expected {}, computed {'small_deficit_window_yr': 5.4, 'small_deficit_rise': 0.07066198357587261, 'large_deficit_window_yr': None, 'master_expected': 'B 0.5->0.618, M_end 0.847', 'verdict': 'SUPERSEDED: master head-line masking numbers are original-model; corrected model shows only a narrow deficit-limited mask (~5.4 yr, vanishing at deficit >0.075).'}.
- **12A.3** — pass — expected {'D_E_frozen': 5.26, 'D_E_crashed': 6.74}, computed {'D_E_frozen': 5.262, 'D_E_crashed': 6.741}.
- **12G.2** — pass — expected {'f0': 0.506, 'f25': 0.042}, computed {'f0': 0.50625, 'f25': 0.04375}.
- **12G.4** — pass — expected {'M_final': 1.19}, computed {'M_final': 1.1942810825476948}.
- **12G.5** — pass — expected {'M_final': 0.0}, computed {'M_final': 0.0}.
- **12G.7** — superseded (verdict) — expected {}, computed {'small_deficit_window_yr': 5.4, 'small_deficit_rise': 0.07066198357587261, 'large_deficit_window_yr': None, 'master_expected': 'B 0.5->0.618, M_end 0.847', 'verdict': 'SUPERSEDED: master head-line masking numbers are original-model; corrected model shows only a narrow deficit-limited mask (~5.4 yr, vanishing at deficit >0.075).'}.

## Discrepancies (auto vs curated)

- 12A.3: AUTO said 'superseded' (score 0.86), curated verdict 'covered'
- 12A.4: AUTO said 'superseded' (score 0.84), curated verdict 'covered'
- 12C.8: AUTO said 'superseded' (score 0.64), curated verdict 'covered'
- 12C.9: AUTO said 'superseded' (score 0.90), curated verdict 'covered'
- 12C.10: AUTO said 'superseded' (score 0.63), curated verdict 'covered'
- 12E.1: AUTO said 'superseded' (score 0.87), curated verdict 'covered'
- 12G.2: AUTO said 'superseded' (score 0.90), curated verdict 'covered'
- 12G.5: AUTO said 'superseded' (score 0.90), curated verdict 'covered'

## Open items & provenance

- 12A.1

*The automated system is decision support, not an arbiter. Status reflects the curated layer where set; the auto verdict is retained as evidence. Original-model numerics are labelled 'original' and corrected-model content 'corrected (1‴)'. The corrected-model basin (R1) and characteristic-equation/spectrum (R2) are now **computed and reported** (SCAN_risk_register_r1_r2.md, §8/§13): R1 recover fraction 39.9%→5.3%; R2 neutral zero eigenvalue + monotone positive-real leading eigenvalue (no Hopf). The scan's numeric pass runs original-model verifier IDs; R1/R2 are exercised via `run_numeric` (model_sims/numeric_claims.py).*
