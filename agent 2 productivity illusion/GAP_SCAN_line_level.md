# Line-level gap scan — master → revision

A granular, line-by-line scan of `MASTER_joint_assessment_and_implementation_plan.md`
(Parts 1–12, incl. the Part 10 checklist and the 12A–12G completion pass) against the
implemented revision `IMPLEMENTED_revision_ECOMOD.md`.

**Verdict: the revision is near-complete.** Every item in the master's Part 10 action
checklist and every numbered point in Parts 12A–12G is addressed somewhere in the
revision — either implemented, explicitly justified as *not* carrying over, or logged as
open required work rather than silently assumed done. **No reverse is needed; no verdict
is contradicted.**

## How each block resolved

| Master block | Status in revision |
|---|---|
| Model: `(1‴)`, `B=bA+b_G G(A)`, A/b separation, τ_g in recruitment, `(6′)` η, `(7′)` multiplicative, γE→supplement, ψ | Implemented (§2.2, §3, §4) |
| Analytics: re-derived char. eq., χ sign, `A_c(E)`/`E_sn`, `(2f−1)ν>1`, no `M_max/2`, non-smooth one-sided | Implemented (§4) |
| Headline claims | Implemented/replaced (§5) |
| Demonstrate illusion (12A.1, 12G.7) | **Handled honestly** (§10): headline sets are original-model & do *not* carry over; a converged small-deficit band (≈5.4 yr, vanishing at deficit ≈0.075) is presented instead |
| Ill-posed endpoint (12A.2/12A.3): K→0 blow-up, method-dependent D_E (5.26/6.74/18.70), `M≥0` clamp, no-op interpolation, grid range, normalise-`r` | Implemented (§2.2, §8); D_E both-conventions now reproduce in the verifier |
| Knife-edge (12A.4): `χ=1 ⇔ ρ=3q` non-generic | Implemented (§4.3) |
| B6/B7/E1: co-evolution, general γ, K algebraic | Implemented (§2.1, §3) |
| Literature/hygiene (12D/12G.6): Hutchinson, Brander–Taylor, GFN list, delete items, units, submission hygiene | Implemented (§7) |
| Falsifiable predictions (12G.1) | Implemented (§6) |
| Measured basin (12G.2): 0.506→0.042; (20,20)/(30,25) | Implemented (§8) + `A_c(E)` closed-form bound (§4.2) |
| Dimensionless set (12G.3) | Implemented (§4.4) |
| Scenario B/C "recovers/collapse" (12G.4) | Implemented (§5) |
| Model consistency (12G.7): Jevons rebound, τ_D/asymmetry, trivial equilibrium, dde23, Δt table, ω=0 spurious, Ω footnote | Implemented (§3, §8) |

## The remaining points → what was just folded in

These were the only genuinely-uncarried points; each is now added to the revision:

1. **Stability-crossing curves + full-spectrum verification** (Claude audit §3.2; master 12B) —
   the two-delay threshold is still a single-branch estimate. *Data: added to §8* as filed
   required work (R2).
2. **Balanced-with-lags scenario row** (master B12 / receipt) — the one missing table row is the
   *balanced* (`e=r_opt`) case *with* lags (oscillation, the χ=1 Hopf, not collapse). *Data: added
   to §8.*
3. **Scenario-E "0.5588 only via rising M" caveat** (master 12A.1 caveat (i)) — the paper's own
   Scenario E reaches the illusion B-value by logistic overshoot of M, not by masking. *Data: added
   to §10.*

## Granular re-scan (final pass) — newly implemented

A second, systematic grep of the master's Part-10 checklist and Part 12A–12H granular items against
the revision surfaced seven more explicitly-listed points that were present only as intent, not as
text. Each is now implemented in the revision:

1. **Flow-share `ψ` regime dependence** (master 12G.3 / Part 11 §4.6) — the ψ→0 / ψ→1 / in-between
   trichotomy and its effect on which analytic core applies. *Data: §4.1 subsection.*
2. **"≈80 yr is NOT the Hutchinson threshold"** (master 12A/B "closed-form ≈ 80 yr (not Hutchinson)") —
   explicit disambiguation that the two-loop coincidence is the model's own round-trip gain, not the
   single-delay logistic π/(2r). *Data: §5 corrected-claim row.*
3. **Thought-experiment label** (master didactics) — the orchard/hens framing is a *Gedankenexperiment*,
   separate from the measurable flow/increment decomposition. *Data: §7.*
4. **Parameter justification** (master didactics) — `ρ` large; `γ, α, τ` are lumped/effective. *Data: §7.*
5. **NFA (National Footprint Accounts) data limitations** (master didactics) — accounts do not capture
   erosion/deforestation/groundwater, so biocapacity is likely overstated and Footprint understated.
   *Data: §11.*
6. **"the wave must outpace the debt build-up"** (master 12A.1 caveat (ii)) — the illusion requires the
   wave to arrive while the stock is high and deficit still small. *Data: §10.*
7. **Process / RC4·RC6 completions** — claims ledger + mechanism↔equation map (made explicit as the
   §12 receipt), attribution-in-appendix, and the decision-document framing. *Data: new §14.*

## Still genuinely open (not remaining *points*, but remaining *work*)

These are not omissions — the revision explicitly logs them as open rather than pretending
they are done (risk register R1/R2), which is the honest RC5 posture:

- **R1** — the corrected-`(1‴)` basin recompute (recover `A→A_max` / collapse `A→A_ext` boundary),
  because the original 0.506→0.042 fraction is an *original-model* S0 result and does not transfer.
- **R2** — the corrected characteristic equation / scenario table / figure set for `(1‴)`.

Both are captured in `SCAN_risk_register.md` and in the revision's §13, not silent.

## Numeric verification against the master's numbers

`model_sims/numeric_claims.py` recomputes the master's concrete claims and now **reproduces**
them after the scenario port was made faithful to `sim.py`:

| Claim | Master expect | Recomputed | Status |
|---|---|---|---|
| 12A.3 D_E (frozen / crashed) | 5.26 / 6.74 | 5.262 / 6.741 | ✅ both conventions |
| 12G.2 basin fraction (0,0)/(30,25) | 0.506 / 0.042 | 0.50625 / 0.04375 | ✅ |
| 12G.4 Scenario B (env recovers) M_final | 1.19 | 1.1943 | ✅ |
| 12G.5 Scenario D (collapse) M_final | 0.0 | 0.0 | ✅ |
| 12A.1 / 12G.7 masking (head-line set) | (original-model) | SUPERSEDED — narrow band | verdict |

The tooling that produced this is the `scan_revision` pipeline in this folder
(`README.md` maps each of the 10 blueprint augmentation items to its module).
