# HONEST_DISCLOSURE — Certification Levels and Remaining Gaps

> **Post-transfer-audit note:** see `/TRANSFER_AUDIT_RESPONSE.md` — three findings accepted and repaired (proof expansion, E5 toy-scope, TCS-1.0 controlling schema), plus the follow-up postscript (the "J-17" three-object split: the 2J3KL cod fishery and the Edwards well J-17 aquifer are the two real systems — for the Edwards type, Cor2 is forecast-map only; the A021 J-series is an audit docket, not a system). The four-issue disclosure below remains current.

**Purpose:** A reviewer-facing document that answers every question the audit raised, without inflation or deflection. This is the document Wave E should read before citing any artifact.

---

## Issue 1: Independent rerun (the gating item)

**Status: DONE for the five committed Part II certificates (2026-08-26) and for the Wave E scored trees (`batch 4/WAVE_E_RERUN.md`). NOT DONE for the A025 fold pipeline or C4 monodromy at dt=0.1.**

| Question | Answer |
|---|---|
| Who computed the artifacts? | Original: one AI agent (Z.ai Code) on one machine. Independent rerun: a second agent (Arena.ai Agent Mode) on a different machine and toolchain |
| Were they independently verified? | **Yes, for the five committed certificates.** Report: `batch 4/VALIDATED_COMPUTATIONS_RERUN.md`. Hopf, E5, monodromy dt=0.25 are hash-identical; Krawczyk and off-grid re-certify the same claims at a nearby Newton centre |
| Is this acceptable for internal work? | Yes |
| Is this acceptable for citing the discrete-level certificates? | **Yes**, with the Part IV citation forms (discrete / interval-verified, not proved; no continuum lift; no fold certificate; E5 toy-only) |
| Is this acceptable as closing Wave E? | **No.** Part III remains entirely NOT CONFIRMED |

**This was the single gating item for treating the five committed computations as externally citable at discrete level. It is now discharged for those five. It is not discharged for the unrebuilt fold / dt=0.1 monodromy, and it does not close any Wave E gate.**

---

## Issue 2: The off-grid residual certification level

**Previous claim (session 1):** "Interval arithmetic" — but the naive power recurrence amplified widths through the E equation's sensitivity (~P·η·E ≈ 6763), and the agent switched to float64 + ulp margins.

**Audit question:** "If the interval amplification is a known artifact, why is the final certificate float64 plus ulp margins rather than interval arithmetic?"

**Answer: the interval version has been rebuilt and is now genuine interval arithmetic.**

| Version | Method | Certification level | File |
|---|---|---|---|
| Session 1 (lost) | Naive interval power recurrence | **FAILED** (width amplification) | — |
| Session 2, v1 | Float64 + ulp margins | **SOFTER** than claimed | `c4_offgrid_interval.py` (superseded) |
| **Session 2, v2 (current)** | Per-mode mpmath interval evaluation (dps=40) | **INTERVAL-CERTIFIED** (genuine interval arithmetic throughout, no float64 fallback, no power recurrence) | `c4_offgrid_interval_v2.py` |

**v2 results (256-point grid, outward-rounded):**
- N: ≤ 6.57e-8
- A: ≤ 1.04e-9
- Z: ≤ 8.28e-7
- E: ≤ 2.85e-6

These match the float64 values to within the expected interval widths, confirming that v1's float64 + ulp approach was correct but v2 is the genuine interval certificate.

**What a reviewer should know:** the v2 method evaluates each Fourier mode independently via mpmath's interval exp/cos/sin (avoiding the power-recurrence accumulation that caused the amplification). The computation is slower (24s for 256 points vs <1s for float64) but produces genuine interval bounds.

**Bug found and fixed during the rebuild:** the derivative formula was missing a factor of 2 (`-2πk(a·sin+b·cos)` instead of `-4πk(a·sin+b·cos)`), which is why the first interval version produced large residuals. After the fix, the interval values match the float64 reference exactly.

---

## Issue 3: Items not yet rebuilt

| Artifact | Status | Why not rebuilt | What exists |
|---|---|---|---|
| A025 fold pipeline (collocation → continuation → Moore–Spence → Krawczyk) | **PARTIALLY REBUILT** | The branch-switch stage works (1 branch point from the Hopf predictor); the amplitude continuation stalls due to session time limits | `a025_fold_pipeline.py` (committed, 366 lines); the script is complete but the continuation needs more compute time |
| A025 fold resolution cross-checks (m=96, 128) | **NOT REBUILT** | Depends on the fold pipeline | Documented in the prior session's worklog |
| C4 monodromy at dt=0.1 | **NOT REBUILT** | The dt=0.25 level is rebuilt and committed; dt=0.1 requires ~4x the compute time (3709 steps vs 1484) | The dt=0.25 monodromy is committed with full certification |

**Assessment:** the computational base is partial. The strongest results (orbit Krawczyk, off-grid residual, monodromy at one mesh level, Hopf certificates, E5 admission) are committed; the fold pipeline and second mesh level are scripts that need more compute time.

---

## Issue 4: Wave E specification matching

**Status: NOT CONFIRMED. No specification matching has been performed.**

The Wave E candidate support table in PROOF_MANIFEST.md Part III correctly marks every row NOT CONFIRMED. The specification matching requires:

1. **Freezing the Wave E specification**: the state space S, specification Ω, observation process y_t, horizon T, and scoring rule must be frozen by the Wave E agent
2. **Matching against the artifacts**: each frozen specification item must be checked against the computation artifacts' parameters, model classes, and solution concepts
3. **Confirmation or rejection**: only after the match is verified can any row change from NOT CONFIRMED

**No specification has been frozen. No matching has been performed. Every row remains NOT CONFIRMED.**

---

## Summary of honest statuses

| Computation | Certification level | Committed | Independent rerun |
|---|---|---|---|
| A025 Hopf certificates | INTERVAL-CERTIFIED (mpmath dps=50) | ✅ | ✅ 2026-08-26 hash-identical |
| C4 orbit Krawczyk | INTERVAL-CERTIFIED (K=80, margin 1186) | ✅ | ✅ 2026-08-26 claim reproduced (hashes differ; \|ΔP\|=4.5e-12) |
| C4 off-grid residual | INTERVAL-CERTIFIED (mpmath per-mode, v2) | ✅ | ✅ 2026-08-26 claim reproduced (A 6 % higher; residual ≤3e-6 holds) |
| C4 monodromy (dt=0.25) | VALIDATED (insertion bound + Bauer-Fike discs) | ✅ | ✅ 2026-08-26 hash-identical |
| E5 module admission | INTERVAL-CERTIFIED (outward-rounded) | ✅ | ✅ 2026-08-26 hash-identical |
| A025 fold pipeline | **NOT COMPLETE** (script committed, computation partial) | script only | ❌ NONE |
| C4 monodromy (dt=0.1) | **NOT REBUILT** | — | — |

**Bottom line: five genuine interval-certified computations are committed, reproducible from code, and independently rerun (`batch 4/VALIDATED_COMPUTATIONS_RERUN.md`). The fold pipeline is a committed script awaiting more compute time. No Wave E specification has been matched.**
