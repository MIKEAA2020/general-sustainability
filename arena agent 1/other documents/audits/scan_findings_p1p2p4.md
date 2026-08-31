# Deep Scan Findings — Turn 1 (P1, P2, P4) — 2026-08-30

Harness: `audits/numdiff.py` — significant-number multiset diff between the official
source manuscript (repo) and the arena-agen1 rewrite (+ SI where present). Fixed this
turn: the ID-stripper regex previously allowed `[A-Z]{0,2}\d{2,3}`, which ate pure
integer prefixes of decimals after `[` or spaces (contaminated the earlier P4 run);
now `[A-Z]+\d{2,3}` (letters required). SI files are now included in the rewrite
multiset (P1, P4).

## Verdicts

### P1 — CLEAN
- All numeric differences are section-numbering noise (official 1.0–9.3 vs rewrite
  4.8/4.9/5.4/5.5) plus two benign citation artifacts: `1259855` and `6223` are the
  Steffen et al. (2015) *Science* **347**(6223):1259855 article number in
  paper1_supplementary.md — correct citation, not a value.
- No content restored. No errors found.

### P2 — ADJUDICATED, 2 restorations + 1 delegation + 1 correctly-excluded item
Restored this turn:
1. **Two-patch coupling example** (official App. A.2) — g_i(s)=s(1−s), d=0.2,
   (S₁*,S₂*)=(0.5,0.8), H_min,1=0.31, H_min,2=0.10, max_s g₁=0.25<0.31 → coupling
   creates viability absent in a factor. Now **Appendix A.1** of
   paper2_obstruction_calculus.md.
2. **MSY emptiness counterexample** (official App. A.1) — C₁≠C₂, H_min,i=r_iC_i/4,
   φ_i=−(r_i/C_i)(S_i−C_i/2)²≤0, d(C₂/2−C₁/2)=0 contradiction → empty kernel.
   Now **Appendix A.2**.
3. **Linear substitution alternative** (official Thm 5.5 + scope remark A.4) — Farkas
   pair (pathway vector vs multipliers α,β,γ with αᵀR+βᵀE−γᵀQ≥0, γᵀs^req>αᵀx+βᵀe).
   Now §5(d) of the rewrite with citations Farkas (1902) and Gale (1960), both added
   to the reference list.
Delegated (cross-paper, harness-invisible):
4. **Audit-template propositions** (official Props 10.3/10.4; 0.573/0.914/0.3 values)
   → **paper4_supplementary.md, new S8** (S8.1 effort sensitivities
   C_Z=h₀g₀ηE*/Δ_ref, C_K=μ_E E*(1−g₀)/(K₀g₀); S8.2 E*<√(δ₀E_max/η)≈0.573 at
   δ₀=0.3, E_max=1, η=0.914). The audit template is a delayed-effort object → P4 SI.
Correctly excluded:
5. `27.2` = official's internal word-budget meta ("retained budget is ≈27.2k words")
   — project-management language, forbidden in the article. Dropped, not restored.
Already retained (verified):
6. **Moiety remark** (official App. A.3) — present in both P3 files
   (paper3_material_ledgers.md L572; reconstructed_v2 L62).
Remaining harness noise: official theorem/section numbering (Def 12.3/12.4, 13.3/13.4,
§2.4–2.7, Lem 3.5, Lem 5.6, §5.9, Ex 6.5, §6.14–6.16, §8.8–8.9, Conj 9.6).

### P4 — ADJUDICATED, 1 real error fixed, all derived values verified, 6 restorations
**Real error found and fixed (Theorem 3, no-Hopf proof):**
- The protective-channel Routh array quoted the *mobilising* λ² coefficient 0.2774.
  Protective polynomial is λ³ + **1.0682**λ² + c₁′λ + c₀′ with first column entries
  1, **1.0682**, c>0, c₀′>0 (1.0682 = −A_N + d − C_E = 0.01791+0.2+0.850336 ✓).
  The theorem's conclusion was unaffected (Descartes argument independent), but the
  displayed coefficient was wrong. FIXED in place.

**All six "extra" value-families hand-verified against the official parameter table
(r=0.02, K=100, q=0.001, η=0.914, E_max=30, Δ_ref=1, δ₀=0.01, τ_m=5, Z_ref=1,
δ=ln2/10) — all correct derivations, kept:**
- A_N = r(1−2N*/K)−qE* = −0.01791 ≈ −0.0179 ✓
- B_E = qN*/(2τ_m) = 0.008955 ✓
- d = 1/τ_m = 0.2 ✓
- Mobilising C_E = −0.0595 ✓; C_Z = +1.785 ✓
- Protective C_E = −0.850336 ✓; C_Z = −1.661702 ✓
- Mobilising undelayed cubic λ³+0.2774λ²+0.00056λ+0.000213 ✓ (RH violation
  0.2774×0.00056=1.55e-4 < 2.13e-4 ✓, consistent with "undelayed unstable")
- Even-pairs cancellation B_E·A_N = A_E·B_N exact ✓
- No-Hopf cubic c₂=0.76339, c₁=0.028946, c₀=9.278e-6 reproduce from the above ✓

**Content restorations applied (condensation → full registered content):**
1. §8.3 M3-U: Droop nutrient–quota variant sentence (window edge ≤0.023 yr⁻¹ at
   η=0.914; no crossing at r≥0.2 yr⁻¹; quota self-relaxes at r; ω_A-type exchange
   narrows window).
2. §8.3 M3-B: ungated-B fold at 76.075 vs τ₊=76.2906, window (76.075, 76.29);
   four-state ungated-B crossings 6.25/76.33, upper fold not pinned; multiplier
   pair 1.0514→0.998983 added.
3. §8.3 M3-LC: fixed-demand experiment (D=0.7>S_max=0.5, N(0)=50; pure culling at
   zero near time 158; recruitment suppression N<1 near 430; first-hitting-time;
   local≠excursion equivalence).
4. §8.3 four-state entry: full M4-A registry block (equilibrium 89.5256/397.8665/
   2.0896; crossings 6.982022/132.272044; persistence 7.374/130.77 [130.770,130.771];
   gated 3.7849/150.12 with periods 360–380/150–160; ω_A*≈0.001316298 gated
   ≈0.001330; 1798-pt sweep + 60 + 60).
5. New §8.4 "The four-state working core" (renumbered; old 8.4→8.5): characteristic-
   pinned pair τ−=3.78487 (period 250.44) / τ₊=150.12175 (159.13), |detΔ|<10⁻¹⁸,
   3.2%/0.2% shifts, amplitude 0.090 at 150.082, folds 5.63/64.4 with brackets
   5.62/5.64 and 64.5/64.25, topology (3.78,5.63)/(5.63,64.4)/(64.4,150.1), capture
   τ≳75–100 (depleted ≳135), periods 371→320 and 156→73, ω_A* second parameter
   (τ− 17.5→6.9, monostable 120–260), periods 250–390 τ-independent, frozen-donor
   4.652 stock units/yr discipline.
6. §8.3 MPF: full registered passage (baseline tuple 100/0.340/24.5/0.072/0.00995/
   0.388/0.0384/35.8/2.23/0.0118/2.29/5.13; equilibrium 16.68/10.23/0.435; no Hopf
   for τ≤500; 33.4–33.6 transient, 2×10⁴, 33.4–34.8, τ≳35 basin-selective; η_crit
   ≈2.337 with pairs over (2.337,3]; η=2.5 → 0.6/54.2/92.9/113.1; η=3.0 → 4.5–41.2;
   η=10 → 17.568/18.362, exponent 0.59; homoclinic-like classification with 4
   diagnostics, CV 1.58, r=−0.47; time fraction 0%→100% over 18.4→22; pair-birth
   structure 71.2/72.9 and 2.454; >300 sigmoid-screen negative result).
7. §2.4: QSS low-A equilibrium (23.85, 0.159), high-stock A*≈−137 inadmissible;
   QSS-core distinctness sentence.
8. §5.1 certified table: ungated certified intervals added (6.2135987340180–83 /
   76.2906356879512–18).
9. §5.2: τ=3.700 residual ~10⁻⁷ escape clause; k-criticality paragraph
   (sp_k″(0)=k/4, k=10, k∈{5,10,20,40}, sign-change caveat).
10. New §8.6 "Reproduction targets" (τ*≈43, period ≈263, η=5, ς=0.8, K₀=0.03,
    q=0.01; class 1 g≈1/2/5 anchovy/sprat/cod; class 2 periods 10³–10⁴; sign
    discipline dReλ/dτ<0).
11. §9.1 η_crit → 2.34 (matching official L504; MPF registry keeps 2.337 per L449).

**Verified already correct (no action):**
- SI S2 fold rebuild: full-precision 5.587236198690/5.587236198663/5.587236198663
  at m=64/96/128, agreement 2.7×10⁻¹¹ — present.
- §8.2 upper-boundary passage (144.5, 0.11–1.87, 15.9–19.5, [130,150.30],
  [147.5,160], 135.6, 0.81, 10⁻⁴–10⁻⁵, >20 yr bisection, 10⁻¹² residual, 0.240→0.964)
  — all official-provenanced.
- §7 sample-and-hold: ρ=0.9838, 1.00055, T_r^NS=47.536, 79.143, 2.306 ✓ (Discussion's
  "47.5" is a rounded echo — fine).

**Remaining harness noise only:** count differences (official repeats values in its
internal register), section-ref renumbering, tokenizer artifacts (1000.340 from
"(100, 0.340)", 102.08962, 130150.30, 5102040, 0300), Unicode-superscript vs LaTeX
extraction (3.55/5.75).

## Files changed this turn
- paper4_delay_dynamics.md (Theorem 3 fix; restorations 1–11; §8.4/8.5/8.6 added;
  cross-refs updated)
- paper4_supplementary.md (new S8 audit template)
- paper2_obstruction_calculus.md (Appendix A; §5(d); Farkas + Gale refs)
- audits/numdiff.py (regex fix; SI-merge in comparisons)
- audits/numdiff_after_fix.txt (full current output)

## Next
Turn 2: P5 + E1–E4 + all four P3 files + remaining SI-only content (add P5 and the
E papers to the harness; P3 canonical-file choice still open). Then the consolidated
full-suite findings report.
