# Line-level review: papers/paper{1..5}_*/manuscript.md

Repository: https://github.com/MIKEAA2020/general-sustainability/ (HEAD 8a286c4)
Branches reviewed: Paper 1 (434 lines), Paper 2 (876), Paper 3 (805), Paper 4 (850), Paper 5 (570).
Scope asked: flaws and internal inconsistencies, at line level.

## Overall
No substantive mathematical error, no promoted claim status, no unfulfilled stated proof
obligation, and no cross-paper status contradiction were found. The findings below are
copy-edit/placeholder, count-drift, and near-collision issues. Every load-bearing number I
could verify independently checked out.

## Verified-consistent (checked by recomputation / cross-reference, NOT flagged)
- Retained-row counts and per-source sums: P1=21; P3=52 (1+5+1+3+5+1+3+2+11+5+8+7);
  P4=55 main + 13 appendix = 68 (2+7+11+3+3+1+11+8+9);
  P5=57 (23+10+6+2+4+3+5+1+2+1).
- Concordance: 409 rows / 354 `row_verified` / 28 adjudicated-negative / 24+3 open; the 27 open
  are exactly A021/A022/A023. Confirmed against canonical_concordance_A001_A025.csv.
- P1 §2.2 eleven terms vs "thirteen" — see finding 2 (the source and P2 Def 2.3 both say 13).
- P1 machine witness: scale 40, grid 31^3 = 29,791, FP = 1,900 grid states, 25/25 checks,
  e=1/4, c=1 — matches typed_false_positive_instantiation.{py,json,report}.
- P1 Theorem A/B identitities: {P_typ}={x>=1}∪{s1>=2}∪{s2>=2}; ⋂_w{P_w}={x>=1}∪{s1+s2>=2};
  FP triangle; rescue/impossibility split; witnesses (1/2,6/5,6/5) interior and (1/2,1/10,1/10).
- P3 §2.3 incidence matrix column sums all zero (1^T S = 0).
- P3 §5.5.2 inverse-horizon score = (1/5)(1/2.7+1/7.9+1/9.5+1/21.4+1/309) = 0.130.
- P3 §5.5.3 phosphate: 74,000 kt Mt -> 74,000,000 kt / 240,000 kt/yr ≈ 309 yr;
  resource ε=0.10: 0.9*(>300e6/240e3) ≈ 1,125 yr.
- P3 §6.3 inverse-Gaussian: ν=d/|μ|, Var = ν^3/λ = dσ²/|μ|³. Correct.
- P3 §3.7 R* = r N* (1-N*/K) s ≈ 0.187; consistent with qE*N*.
- P4 §2.4 A_eq,W = 50 + 0.05*100/0.001 = 5050. §2.4 geological support ω_A(5050-397.8665)≈4.652.
- P4 §2.5 C_E = -(1-E*/Emax)η ≈ -0.850336; C_Z_prot ≈ -1.661702; C_Z_mob = (1-E*/Emax)[ηE*/Δref +
  δ0 Zref/(Zref+δ)^2] ≈ +1.785. All reproduce.
- P4 §5.2 cubic c0=9.278e-6; c2c1-c0 ≈ 0.02209; loop-gain max 0.08011 < 1. Correct.
- P4 §6.3 working-core pair τ-=3.78487 / τ+=150.12175 matches M4-A gated ≈3.7849 / 150.12.
- P5 §6.3 exp(-M): non-recovery 0.711/0.488/0.696; recovery 0.750/0.499/0.757. Correct.
- Family F06 projectability [CC-A002-036], F03/F05, F10, F02 cross-refs are consistent.
- MS-Native counts within each paper (P1 1-8, P3 1-8, P4 3-12, P5 1-6 own + 7-10 restatement)
  are internally consistent.

## Findings

### 1. Unresolved citation placeholders (Paper 1) — highest-confidence flaw
Literal "[cite: ...]" / "[Cite: ...]" template brackets left in the final-draft body:
- §3.1 line 96  : "...classical viability [cite: Aubin; Frankowska; Saint-Pierre]."
- §3.3 line 113 : "...not new mathematics. [Cite: Aubin-Bayen-Saint-Pierre; Saint-Pierre;
                  Aubin capture basins; Lygeros-Tomlin-Sastry.]"
- §4.3 line 178 (Position): "...viability kernels/reachability sets [cite: Aubin; Frankowska]..."
These should be author-date citations matching the References list (Aubin 1991; Frankowska 1989;
Saint-Pierre 1994; Aubin-Bayen-Saint-Pierre 2011; Lygeros-Tomlin-Sastry 1999). None in P2-P5.

### 2. "Thirteen declared slots" enumerates eleven (Paper 1 §2.2, line 60)
Text: "a tuple S with thirteen declared slots spanning: the typed physical state; the admissible
action correspondence; the dynamics...; the observation map; the information pattern; the
constraint sets...; the disturbance class; the policy class; the claim-status table; the
destination structure; and the declared model map" = 11 items.
Paper 2 Def 2.3 (same CC-A002-003 row) writes the full 13-component tuple
(S,T,Z,S,B,V,Gamma,O,A,C,R,D,K,P). Source and P2 agree on 13; P1 under-lists by two.

### 3. Family numbering (Paper 2) — CORRECTED after deeper review
Deeper check corrected part of this finding. The abstract's "twelve families" is actually
CONSISTENT with the paper: the twelve are F00 (the §2 preliminaries canonical definitions) +
F13 (core, §3) + F01,F02,F03,F04,F05,F06,F07 (§§4-10) + F10,F11,F12 (§§11-13) = 12. The
abstract lists ten of these explicitly ("twelve ... core viability calculus; typed hybrid
conservation and positivity; noncompensation and substitution feasibility; observation and
epistemic viability; recovery and irreversibility; sampled, hybrid, and information-state
kernels; projectability and exact reduction; diagnostics and delay certificates; restricted
composition; and institutional implementation") — the two un-enumerated-but-counted are the
canonical definitions (§2) and intergenerational/stochastic (§13).
The genuine residue is the NUMBERING GAP, not a count error:
- Budget taxonomy `paper2_retained_row_budget.csv` uses F00-F14 (15 families). Of these, F08
  (scalar resource and sink kernels, 9 rows) and F09 (resource-capital, distribution,
  exhaustibility, 7 rows) are ALL `delegated` to Paper 3/monograph, and F14 (conditional
  research docket, 19 rows) is ALL `docket`. So no atlas section carries F08/F09/F14, and the
  section numbering jumps F07->F10 and F12->F13 with no note telling the reader where F08/F09
  went (Paper 3). Recommend a one-line note at §2 or in the abstract: "families F08 (scalar
  resource/sink kernels) and F09 (resource-capital/distribution/exhaustibility) are carried by
  the ledger paper; F14 is the conditional docket."
- Three different family counts coexist in the programme: 12 (atlas/abstract), 13 (venue/worklog
  question decomposition, "thirteen mapped families"), 15 (budget F00-F14). These serve
  different purposes, but the number that a reader sees first (the abstract's "twelve") should
  be reconciled in prose with the budget's F00-F14 so the skip is not read as an omission.

### 4. "Nineteen further rows ... over seven further sources" but one row is from a primary source (Paper 2 §1.2 line 23, §14 line 731, §15 line 844)
Rows 71-89 are described as deriving from A003/A005/A006/A007/A010/A013/A018. But row 89 =
CC-A002-050 (Justice & multiscale viability, Programme 13.3) is an A002 row (line 823).
So: 18 rows over the seven sources + 1 row from A002. Amend wording to "the seven sources plus A002".

### 5. 43 vs 42 stocks (Papers 3 <-> 5)
- Paper 3 §5.5.2 line 469: fisheries ADH "median ≈1.8 yr across the 43 assessed stocks with
  finite SSB and F series (zero entries included)".
- Paper 5 abstract line 9 & §5.3 line 298: "42-stock" RAM annual-review screen cohort.
These are distinct objects (ADH proxy population vs spectral-screen input), so both may be
correct, but the 43/42 collision should be explicitly contrasted; a referee will otherwise read
it as the same cohort.

### 6. Minor exposition / numbering
- Paper 1 §4.4/§4.7 (lines 182, 187-189): successor writes "s+e" but "e" is never defined in the
  manuscript text (only "destination reset gains 1/4"). Artifact defines e = 1/4 per floor.
  State e=(1/4,1/4) explicitly.
- Paper 2 remark/example numbering is non-contiguous and out of sequence: Remark 5.9 (line 280)
  between Cor 5.3 and Def 5.4; Remark 6.16 (line 327) between Thm 6.4 and Ex 6.5;
  Remark 8.15 (line 496) between Thm 8.4 and Def 8.5; Remark 13.4 before Programme 13.3.
  Appears to inherit source remark numbers rather than the atlas's own sequence.
- Paper 1 §5.2 line 235 cites "Das-Dennis 1997/1998" but only the 1997 reference is listed
  (line 414). Add 1998 or drop the second year.

---
## Paper 2 deep-dive (theorem atlas)

### A. Corrected family-count finding — see finding 3 above.
"Twelve" is consistent; the F08/F09/F14 skip is a clarity note, not an error.

### B. Seam-row source attribution (finding 4, confirmed precisely)
Rows 71-89 come from EIGHT sources, not seven: A006 (6), A010 (5), A007 (2), A013 (1),
A018 (2), A003 (1), A005 (1), and A002 (1 = CC-A002-050). §1.2/§14/§15 say "seven further
sources (A003, A005, A006, A007, A010, A013, A018)." The total-source count ("nine fully
row-closed sources") IS correct because A001+A002 are the two primary sources + the seven
= 9; only the "nineteen ... over seven further sources" clause is imprecise (should read
"over seven further sources plus A002, row 89"). No result, status, or destination changes.

### C. Reproduced proofs verified arithmetically (all correct)
- Appendix A.1 (MSY emptiness): phi_i(S_i) = -(r_i/C_i)(S_i - C_i/2)^2 <= 0; adding the coupled
  equilibria forces phi_1+phi_2=0 => both vanish => S_i=C_i/2; then d(C_2/2 - C_1/2)=0 => C_1=C_2.
  Correct.
- Appendix A.2 (coupling creates viability): H_min,1 = g_1(0.5)+0.2(0.8-0.5)=0.25+0.06=0.31;
  H_min,2 = g_2(0.8)+0.2(0.5-0.8)=0.16-0.06=0.10; max g_1 = 0.25 < 0.31; and (0.5,0.8) is a
  genuine equilibrium of the coupled field (both dS_i/dt = 0). Correct.
- Prop 5.1 / 5.7 / 5.8 witness: b_k=-L, b_j=(w_k L+1)/w_j gives w^T b = -w_k L + (w_k L+1) = +1 > 0
  with b_k=-L<0. Correct; the reverse b' gives w^T b' = w_k M - (w_k M+1) = -1 < 0. Correct.
- Thm 9.4 defect bound: |X(A/(k+A) - 1)| = X*k/(k+A) <= X_max*k/a_0 since k+A >= k+a_0 > a_0.
  Correct.
- Thm 9.5 variance identity: E[rX(1-X/K)-qE_s X] = r mux - (r/K)(mux^2+Var) - q(muE mux + Cov)
  = r mux(1-mux/K) - (r/K)Var - q muE mux - q Cov. Correct; curvature bound is Taylor (M/2)Var.
- Prop 8.10 (OSC does not close universal tube constraints): T(z)={0,z} (z>0), T(0)={0,1}, K=[0,1/2].
  Predecessor = {z in K: T(z)⊆K} = (0,1/2], which is not closed (0 is a limit point but 0 has
  T(0)∋1∉K). T is outer semicontinuous at 0 (limsup {0,z}->{0}⊆{0,1}). Correct.
- Remark 8.15 (memoryless Pre not monotone): {a} invariant under L, {b} under R, no single action
  protects {a,b}; a in Pre_ml({a}) but a not in Pre_ml(K). Correct.

### D. Theorem 6.4 status hygiene (minor)
CC-A001-026 "Instantaneous common-action obstruction" is labeled "theorem" but the source omits
the proof and a one-step proof obligation is registered ("will be supplied at camera-ready"). Under
the atlas's own table (Theorem = "complete proof under explicit assumptions") this sits one notch
ahead of its proof state. It is exceptionally well disclosed (the ledger says "proof omitted in
source; one-step proof obligation registered", and its content is witnessed by the proved-by-
construction Example 6.5), but the label could read "conditional theorem/owed proof" for strict
consistency with the hierarchy. Worth a one-word change.

### E. Length / word-count cross-check — consistent
§14 says "measured retained budget is approx 27.2k words at full proof expansion." The content
budget file computes 20,146 located source words (63 main + 7 bounded-appendix formal blocks) +
35% connective/reproducibility allowance = 27,197 words. Matches.

### F. MS-Native-1 label vs §2.7 remark continuity
MS-Native-1 (informational hierarchy) is stated at §2.7, §2.7's table of notation bridges, and in
the ledger. The hierarchy IRViab ⊆ K_I ⊆ RViab ⊆ Viab is listed as a "remark (hierarchy record)"
with A001 §4.12 origin, not a theorem — consistent with its source-declared status. Good.

---
## Paper 3 deep-dive (material ledgers)

### A. Proofs recomputed — all correct
- Incidence matrix (CC-A013-004): col sums exactly zero for all alpha,rho (verified numerically);
  W-col = 1-rho, P-col = -1, U-col = rho => 0. Correct.
- Conservation (Thm 3.7): harvest -h + alpha h + (1-alpha)h = 0; retirement rho r_P - r_P +
  (1-rho)r_P = 0; e_GA:+1/-1, e_AG:-1/+1, c_G:-1/+1 cancel. Correct.
- Four-stock balance (CC-A001-042): d/dt(S+K+N+P)=I_N-Q_P; H and theta_delta coefficients cancel
  exactly. Correct.
- Mass identity (Thm 3.6): R-B+T=0, +-e_GA, +-e_AG, +-gamma_U U cancel; remainder -qEN. Correct.
- No-rest (Thm 3.11) vs extinction-geochemical rest (Thm 3.12): consistent. Working point
  (89.526,397.87): R* = qE*N* = 0.18707 (verified to ~4.6e-6) so it is NOT a ledger rest (needs
  R=0) — confirms the theorem.
- Inverse-Gaussian mean/Var (nu^3/lambda = d sigma^2/|mu|^3) and median<mean via
  F(nu)=1/2+e^{2lambda/nu}Phi(-2sqrt(lambda/nu))>1/2. Correct.
- Geometric-Brownian: dlogB=-(h+sig²/2)dt+sig dW; nu_F, lambda_F, mean->deterministic horizon as
  sigma->0. Correct.
- exp(-M) survival entries (0.711/0.488/0.696; 0.750/0.499/0.757) correct.
- Per-source retained counts match: A001 1, A002 5, A003 1, A004 3, A005 5, A006 1, A010 3,
  A012 2, A013 11, A018 5, A019 8, A024 7 = 52 (once the two cross-refs are excluded, see C).

### B. Row-set integrity confirmed
52 retained rows all `row_verified`; the 9 body cross-refs (CC-A002-005/011/036, CC-A003-001/002,
CC-A013-001, CC-A018-001, CC-A024-001/008) correctly NOT in the ledger. No duplicates.

### C. Status ledger shows 54 CC identifiers, not 52 — a count-confusion trap (clarity)
The §10 status-table ID column holds 54 CC codes because two appear only as parenthetical
cross-citation pointers in destination-note cells, not as retained rows:
- CC-A002-040 (canonical form, owned by Paper 2, §5.4 line 706 / §8);
- CC-A018-007 (approximation content, owned by Paper 4, §3.3 line 722 / §8).
Both are correctly attributed as cross-refs in prose and excluded from the 52. But a reader (or
an automated count) reading the ledger ID column literally gets 54 and infers a mismatch with
"52 rows," §1.2's per-source sum, and §11's "all 52 rows." Recommend marking the two in the
destination cell ("[cross-ref, not retained]") or adding a one-line note below the table.

### D. Depletion-table horizons ARE reconstructible — CORRECTED, my earlier D/E were in error
My initial pass wrongly flagged the §5.5.2 "ADH to window minimum" column as not reconstructible.
Retraction: with the correct formula (from the corrected article) `A_min = A_2023 - ADH*|trend|`
and `ADH = (A_2023 - A_min)/|trend|`, every row back-computes EXACTLY:
  Indo-Gangetic A_min=-548.19 (=article -548), ADH back = 2.70;
  North China Plain -291.94 (-292), 7.90;  Central Valley -236.95 (-237), 9.50;
  La Mancha -88.48 (-88), 21.40;  global mean -33.04 (-33), 47.60.
All implied window minima are negative (below the 2023 anomaly), which is exactly what an
ADH-to-a-lower-window-minimum requires. The manuscript's §5.5.2 table is fully consistent with
the corrected article's Table (tab:adh-gw) and with its stated implied minima line. No defect.
(It would still help a reader to print the historical-minimum column, but that is a
presentational nicety, not an inconsistency — and not what I originally claimed.)
Findings D and E (original) are withdrawn.

### D-2. 43 vs 42 stocks — resolved: BOTH correct, distinct objects
The source's own caption (A018, tab:adh-fish) states: "Median across all 43 assessed stocks with
finite SSB and F series, including zeros, ≈1.8 yr"; and "the spectral null (Section 7) uses the
42 annual-managed stocks within this set." So Paper 3's "43 stocks" (the ADH population) and
Paper 5's "42-stock" (the annual-managed subset used by the spectral screen) are exactly the
source's own nested pair. The 42 is a strict subset of the 43. No error — the two papers carry
two genuinely different, correctly-nested populations. (The earlier near-collision concern is
fully resolved; recommend a one-line cross-linking note.)

### E. Verdict on Paper 3 (after correction)
No mathematical or status error. The corrections above retract the two "not reconstructible"
items — the table IS self-consistent. Remaining genuine refinements: (C) mark the two
cross-ref rows (CC-A002-040, CC-A018-007) so the 54-identifier ledger reads as 52 retained;
and (D-2) optionally cross-link the 43/42 populations. Both presentational.

## Net

---
## Paper 4 deep-dive (delay dynamics)

### A. Load-bearing algebra recomputed — all reproduce EXACTLY
At the Candidate A gated equilibrium (E*=2.0896234, N*=89.5518830, Z*=δ=0.0693147):
- A_N = -0.0179104, A_E = -0.0895519, B_N = 0.00179104, B_E = 0.00895519, C_E = -0.0595482,
  C_Z(mob) = +1.78501871. All match the manuscript (§3.2) to 8 sig figs; the filter identities
  B_N = -A_N/(2·τ_m) and B_E = -A_E/(2·τ_m) hold to machine precision (0.0 residual), which is
  exactly the "even pairs" H-cubic reduction (§3.3) that makes A_E B_N - A_N B_E ≡ 0. Correct.
- Protective gains: C_E = -(1-E*/E_max)η_p = -0.850336, C_Z = (1-E*/E_max)η_p·E_cap'(δ) =
  -1.661702 (via E_cap'(δ) = -E*/(Z_ref+δ)). Both reproduce to 6 decimals; matches §2.5.
- No-Hopf cubic (Theorem 5.1): c2=0.7633923, c1=0.02894620, c0=9.27792e-6, c2·c1-c0=0.0220880.
  All match §5.2 word-for-word. Since c0>0, c2>0, c1>0 and c2c1>c0, Descartes + Routh-Hurwitz give
  no positive root => no |P|=|C_Z||L| solution for ω>0. Correct.
- Section 2.4 A^{eq,W} = A^{eq,intrinsic} + κ_A K/ω_A = 50 + (0.05·100)/0.001 = 5050. Correct.
- Geological support at working equilibrium ω_A(A^{eq,W}-A*) = 1e-3·(5050-397.8665) ≈ 4.652.
  Correct. (§2.4 and §6.3 both state 4.652 — consistent.)
- Cross-consistency: M4-A gated crossings 3.7849/150.12 = working-core (C4-W) τ-τ+ 3.78487/
  150.12175; and the "3.2% / 0.2% shift" claim recomputes as (3.78487-3.66615)/3.66615 = 3.24%
  (lower) and (150.12175-150.35848)/150.35848 = -0.157% (upper) ≈ 0.2%. Both inside the claimed
  frozen-active-pool bound. Correct.
- M3-B interval-certified value 3.6661490... matches the "3.67" table entry and the Appendix A.1
  enclosure [3.6661490142739, 3.6661490142743]. Correct.

### B. Certification-hierarchy consistency (no defect, one sharpening worth noting)
§10 assigns the Hopf interval certificates Level "re-execution-verified" while noting the
certificate condition is discharged within the interval-pipeline scope. The certification ladder
has a "Certified (interval/rigorous)" tier; the interval-Newton enclosures ARE that tier. The
manuscript is careful not to overclaim only when it says the certificates concern the LOCAL
spectrum of H and are reproduced re-execution-verified. This is deliberately conservative and
internally consistent — worth a footnote noting interval enclosures = the "certified" tier for
the local spectrum but NOT for the (unimplemented) global fold, so the reader does not think the
paper lacks the certified tier it actually has. Presentational.

### C. Status-ledger row-count (same cross-ref pattern as P3)
§11 ledger extracts 70 CC identifiers = 68 retained rows + 2 cross-references (CC-A018-004 and
CC-A019-004, which appear only inside the MS-Native-1 / MS-Native-2 seam restatement records).
Same fix as Paper 3: mark those two as [cross-ref, owned by Paper 3]. No count error; all 68
retained rows are `row_verified` (all 13 A025 appendix rows accounted for).

### D. MS-Native numbering clean
P4 uses MS-Native-1..12 with no gaps (the two seam restatements 1-2, regime/numerical
classifications 3-8, the super-equilibrium criterion 11 and early-warning scope 12, etc.). Differs
from P1/P3/P5 numbering conventions but internally consistent. Good.

### E. No substantive defect found in Paper 4
The bifurcation numbers, interval certificates, and certification level assignments all check
out against their source-stated statuses and the committed interval pipeline. The "no-Hopf under
quota tracking" result is verified; the reversal-hazard (iso-gain sign flip) is correctly
labelled as NOT the quota law; and the fold non-certificate discipline is exemplary (open
Moore-Spence/Krawczyk stages, no promotion).

---
## Paper 5 deep-dive (sampled governance, empirical ID)

### A. Empirics recomputed — all correct
- exp(-M) survival series: 0.341/0.717/0.362 -> 0.711/0.488/0.696 (non-recovery window);
  0.288/0.696/0.278 -> 0.750/0.499/0.757 (recovery window). All reproduce to 3 decimals. Correct.
- Crash-window exp(-M): 1.002/2.214/2.575/2.331/0.288 -> 0.367/0.109/0.076/0.097/0.750. The
  "survival column" is a transformation, exactly as MS-Native-8 states. Correct.
- The "2.2-2.6 ≈ ten times pre-collapse" claim: crash-window M 2.2-2.6 vs pre-collapse levels
  (the non-recovery/recovery M ~0.28-0.72). Correct.
- Statistics Canada top-2% CSD definition and 25.1% (2016) / 21.4% (2021) fishing-dependence
  thresholds, and the mean income 32.2%->25.6% and the listed community values — all stated as
  registered/unreproduced pipelines, not carried as results. Consistent with their docket status.
- The Allee constitutive model and the scalar-autonomous phase-line obstruction are stated
  correctly; the cross-equilibrium argument (real scalar autonomous ODE cannot rise-and-fall) is
  valid and correctly scoped to exact trajectories.

### B. Status-ledger row-count (same cross-ref pattern)
§10 extracts 58 CC identifiers = 57 retained + 1 cross-ref (CC-A002-034, the Atlas conditional
theorem the MS-Native-3 rapid-review consistency instance rides, owned by Paper 2). Source
counts: A001 4, A002 3(+1 ref), A003 1, A006 5, A010 1, A011 23, A014 10, A016 6, A018 2,
A024 2 = 57. All `row_verified`. Correct.

### C. 42 vs 43 — RESOLVED as nested (now verified against the A018 source)
The 42-stock annual-review screen cohort is a strict SUBSET of the 43 assessed stocks used for
the ADH median in Paper 3; the source caption states both explicitly. Both papers are correct.

### D. Referee-facing confirmations
The "two-operator discipline" (hold map vs stage-structured review map vs continuous-delay
equation), the "diagnostics are not causal claims" rule, the bounded-absence framing of the
spectral null, the "zero-count search is not disconfirmation" caveat, and the "prospective
designs are preregistration targets, not executed" language are all stated and honoured. The
paper's empirical claims never exceed the nominal tier.

### E. Verdict on Paper 5
No error. The spectral null, power values (anchovy 0.02-0.14, sprat 0.24-0.58, sprat 1.0 at
σ=0.1), response regions (3-4 yr anchovy, 6-12 yr sprat, 30-50 yr slow-r transition brackets,
convergence for cod over 1-20 yr), and the zero-count search are all carried at their exact
declared statuses. The only refinement is the same cross-ref marking for CC-A002-034.

---
## End of deep-dive. Overall verdict across all five papers
- No mathematical error; no promoted claim status; no broken stated proof obligation.
- Two of my own initial "findings" were WRONG and are now retracted with correction:
  the Paper 2 family count ("twelve" is correct), and the Paper 3 ADH "not reconstructible"
  claim (it is fully reconstructible; 42/43 is a nested pair, both correct).
- Standing, confirmed, minor findings (presentational only): unresolved [cite:] placeholders in
  Paper 1 §3.1/§3.3/§4.3; Paper 1 §2.2 "thirteen slots" enumerates 11; the 54/52 (P3) and 70/68
  (P4) and 58/57 (P5) status-ledger cross-ref counts (mark the cross-refs); unnamed reset-gain e
  in P1 §4.4; Paper 2 F08/F09/F14 numbering skip; Paper 2 "seven further sources" vs
  "plus A002 (row 89)"; Paper 2 Theorem 6.4 could be labelled owed-proof.
- The manuscripts are camera-ready-grade in substance; the remaining work is editorial polish
  (citation completion, count labeling, one-sentence cross-links) and the registered venue-format
  pass. None of it affects any result.

---
# WAVE E REVIEW (forecast-ladder + intervention pairs, COD and Edwards)

Read line-by-line in full at the committed paths
`wave_e_cod/manuscript/...` and `wave_e_edwards/manuscript/...`.
The intervention papers run their own frozen protocols and do not alter the
forecast-ladder retention decisions; the two score tables are never pooled.
No status is promoted, no new claim is made in either pair. Focus below is on
internal consistency and flaws (not style).

## Wave E COD (forecast ladder, intervention)
Read in full (286 + 158 lines) and independently re-derived.

Verified exact:
- Model ladder M1/M1b/M2/M3/M4 on Omega_2016 (DFO 2016 Table A2, 1983-2015,
  K*=LRP=884.6 kt) and the second specification Omega_xte (Regular et al. 2025,
  1954-2024, K*=276 kt; 95% 180-423; 40% of B_MSY). Two objects differ in four
  typed fields (dynamics, safe-set map, catch treatment, horizon); stated never
  mixed. Not pooled.
- Negative certificate reproduced: h=1 persistence 98 kt beats M1 115, M2 160
  (annual-landings), 115-206 coarse-regime; h=5 persistence 265 beats 289-488.
  Catch-regime stock-flow cannot produce the collapse (M2 >= M1). Consistent.
- g_max = rK/4 = 296.1 kt; with UC-min/q05 floors (|e|=460.0 / 318.8) g_max is
  below the persistent productivity floor -> productivity negative certificate.
  Under UC-q10 (|e|=114.8): g(K*) = r K*(1-K*/K) = 172.5, and
  g(K*)-|e_q10| = 57.7 ~ 57.6 kt = 24.00% of the pre-1992 240 kt level. Maximal
  robust flat catch 57.6 kt is correct.
- Expansion obstruction: F'(S) = 1 + r(1-2S/K); F'(K*=884.6) = 1.153075 > 1
  (only contracts above K/2 = 2500 kt). r_T = eps(a_max^T-1)/(a_max-1) with
  a_max = 1.153075 gives r_1 = 460, r_5 = 3121, r_8 = 6386 kt as printed (the
  printed 1.153 is the rounded display of 1.153075; using the rounded value gives
  3120/6384, so the displayed r_T values come from the full-precision a_max --
  correct, no flaw).
- 2015 SSB 299 kt / 884.6 = 33.8% = "34%" as stated; Fig 4 overlap
  1983-2015 RMSE = 126 kt (NCAM 299, xteNCAM 273).
- Non-mixing discipline, secondary scores (MAE/log-RMSE/Brier/direction) reported
  but selection on primary RMSE, M1b Allee parameter declared unidentified
  (s->0, K pinned), and the oracle/checkpoints framing (Regular 2025 Table 17:
  2005=26, 2017=451, 2021~400, 2024=342, 2024/LRP=1.24; "agreement on a low year
  does not warrant splicing") are all stated and honoured.

FINDINGS (COD): none. No mathematical error, no promoted status, no unfulfilled
stated proof obligation. The only stylistic residue is the Figure-number<->filename
skip pattern noted below (shared with Edwards).

## Wave E Edwards (forecast ladder, intervention)
Read in full. Independently re-derived the intervention map and kernels.

Verified exact:
- Map Delta H = alpha + beta R + gamma P + delta H_{t-1} fitted 1934-1990
  (56 transitions): alpha=163.49, beta=0.0198 (ft per 1e3 ac-ft), gamma=-0.02844,
  delta=-0.2539, a=1+delta=0.7461 (25.39% ~ 25.4% mean reversion). Consistent.
- Worst-case attractors reproduce: fixed point H* = (alpha+beta R+gamma P)/(-delta)
  with delta=-0.2539. BAU (P=282.16, UC-min R=43.7):
  H*=156.33/0.2539=615.71 ~ 615.72. flat-90% (P=253.94): 157.13/0.2539=618.88.
  flat-0 (P=0): 164.355/0.2539=647.32. All match the printed attractor table.
- 7.2% smallest cut: linear interpolation between BAU (615.72 at 0% cut) and
  flat-90% (618.88 at 10% cut) gives 10%*(618-615.72)/3.16 = 7.2%. Exactly the
  printed value; internally consistent.
- Erosion (contraction form) r_T = eps(1-a^T)/(1-a), eps=15.41 (training max
  residual), a=0.7461: r_1=15.41, r_3=35.49, r_5=46.66, r_inf=60.69 ~ 60.70.
  Certificate geometry consistent. OOS defect max 21.81 > 15.41 is explicitly
  declared ("certified rows are optimistic out-of-window; no refitting, per
  protocol"). Correct handling.
- Retention arithmetic: S1 vs flat-90% +8.42 (+3.3%), vs flat-80% +36.63 (+16.2%);
  cpm vs flat-60% +85.64 (+50.6%). All match. S1=cpm vs flat-90/80/60 protection
  comparisons use the same attractors as the Table (S1=flat-80%=622.04;
  cpm=flat-60%=628.36). The S1 == flat-80% equality is right because S1's reactive
  20% cut equals flat-80%'s 20% cap and the cut is active on the whole attractor
  branch (as stated).
- The certified-boundary ordering (flat-0 662.2 < flat-80 697.8 < BAU=S1=cpm 706.7
  at T=3/UC-min/618 ft) is consistent with the erosion expansion of the target set
  K*+r_T and the model dynamics (the certified values are solved, not
  nominal-boundary plus r_T, which is why flat-0 is 662.2 and not 618+35.49; the
  runner is re-executed byte-for-byte reproducible). No flaw.

### Confirmed standing findings (all minor, presentational; none affect any result)

E1. ABSTRACT overstates the "within 0.13 ft of AR(1)" margin. Fore-ladder
    Abstract and §5.4 say the climate-informed recharge variants "AR(1) on
    recharge, Niño 3.4, lagged precipitation, and their combination ... lie within
    0.13 ft of AR(1) at the one-year horizon." The 0.02/0.04/0.13 ft margins are
    exactly the three non-Rar variants (M2_enso 12.82, M2_precip 12.80,
    M2_combo 12.71 vs M1 12.84). The AR(1)-on-recharge variant M2_Rar is 13.25 ft
    = +0.41 above AR(1) and +0.02 above persistence, i.e. it LOSES at h=1 (and is
    explicitly called out as "not a recharge forecast," §5.4). As written the
    abstract lumps all four under "within 0.13 ft," which is false for M2_Rar.
    Fix: exclude M2_Rar from that clause (or state that it loses at h=1).

E2. "deepest CPM trigger (660 ft)" is inverted. Edwards intervention §4.2:
    "the boundaries (675.1 at T=1, 695.3 at T=2 under UC-min; empty from T=3)
    lie strictly above the deepest CPM trigger (660 ft), so no declared
    demand-management rule activates." But the CPM cascade is
    "cumulative 20/30/35/40% cuts at H < 660/650/640/630" (§2, governance family):
    the 660 ft trigger is the HIGHEST head / most easily reached (Stage I, 20%
    cut). The DEEPEST trigger is 630 ft (Stage IV, 40% cut). The kernel bounds
    (675.1, 695.3) do lie above both extremes (630 and 660), so the conclusion is
    correct, but "deepest" should read "highest"/"shallowest" (660 ft is the first
    of the four triggers). Terminology inconsistency.

E3. "the oracle gap" is quoted against two different baselines across the Edwards
    pair. Forecast-ladder (abstract, §1) and intervention §1 use persistence:
    "7.55 vs 13.23 ft." Intervention §5 switches to the retained AR(1)/M1 baseline:
    "the erosion bound absorbs the 12.84-vs-7.55 ft oracle gap." Both are
    defensible, but the same named quantity ("the oracle gap") has two values in
    the pair. Recommend labelling each (persistence baseline vs retained-AR(1)
    baseline) or standardizing on one.

E4. "harsher than any recorded drought" vs UC-min = the 1956 drought-of-record.
    Intervention §2: "These floors are certification geometry --- harsher than any
    recorded drought --- not recharge forecasts," yet the same paragraph defines
    UC-min = 43.7 with "the 1956 drought-of-record year is UC-min." The persistent
    FLOOR scenario is indeed harsher than any single recorded year (it is a
    perpetual floor), but for the UC-min value itself the statement is imprecise
    because UC-min equals the recorded minimum (43.7 = R_1956, also cited in the
    ladder §5.2 as R_1956=43.7). Recommend rewording to "the persistent floor
    regimes are harsher than any single-recorded-year path" or explicitly noting
    UC-min = recorded minimum.

E5. Figure-number <-> filename offset in the Edwards forecast ladder. Figure 4 is
    referenced as `fig5_pass2.png` and Figure 5 as `fig4_fibre.png` (the filename
    index trails the displayed figure number by one). The files render fine but the
    label/filename mismatch is confusing for a reader trying to locate artifacts.
    (The COD forecast ladder has the same off-by-one trailing pattern — Figure 4
    -> `fig4_xtencam.png` there — worth a normalizing pass across both pairs.)

### Verification notes
- Edwards intervention model K*_phys=618 ft (Comal cessation proximity) and
  K*_inst=660 ft (post-2007 Stage I) — the 660-ft line is consistently declared
  as a 2007 rule, never back-applied. 1956 daily min 612.51 ft consistent across
  the ladder (§5.1, Table 1) and intervention (§4.5 replay vs actual 623.2 ~ 623.15
  annual mean).
- S1 (622.04) == flat-80% (622.04) == flat-80% and cpm == flat-60% are verified
  self-consistent; the §4.4 "same protection" wording is accurate.
- The 0.39 ft AR(1) margin (13.23-12.84) and the "not a significance claim"
  limitation are stated honestly.
- Least-deep note: I inspected the intervention's T=5 nominal-kernel sentence
  (BAU excludes exactly one actual year, 1956) and the 1950s open-loop replay
  (model 659.5->631.3 vs actual 659.5->623.2, max error 8.1 ft, biased high) —
  both are internally consistent and are explicitly recorded as biased with no
  correction applied.

## Wave E overall verdict
No mathematical error. No promoted claim status. No unfulfilled stated proof
obligation. The two intervention runs reproduce from the committed runners
(byte-for-byte), and every attractor / erosion / retention / supply arithmetic
figure I re-derived matches. Remaining issues are five minor presentational/
terminology items (E1-E5) that change no result.

---
# GENERAL THEORY FAMILY REVIEW (flagship theory document, all its versions)

Read line-by-line. Files, all dated 14 August 2026:

- `general_theory_of_sustainability_v0.1.md` (968 ln)  -- "Robust Viability" strand, Version 0.1
- `general_theory_of_sustainability_v0.2_comprehensive.md` (1464 ln) -- same strand, Version 0.2 + Appendix D (traceability matrix) + Appendix E (expanded classification)
- `general_theory_of_sustainability_manuscript.md` (1399 ln) -- same strand, assembled text (the file built to the .docx by build_..._manuscript.py); = v0.2 minus the traceability appendix and scope note, with expanded classification as Appendix D
- `ms_part1.md`-`ms_part4.md` (1911 ln total) -- "Architectural Kernel and Composition Language" strand, parts of a differently-structured Part I-VI manuscript (33 sections, 13 boxes, 8 lemmas, 8 conjectures, 9 proof obligations, 8 appendices)

## 0. Status context (important, from repo metadata)
The repository's own provenance markers (`external_review_packet/README.md`; `worklog.md`;
`research_program/pending_separate_publications_register.md`) describe ALL of these as
**superseded / archival flagship versions**. Two distinct theory strands coexist:

(A) "Robust Viability in Dependency-Closed ... Systems" = v0.1 -> v0.2_comprehensive ->
    general_theory_of_sustainability_manuscript.md.
(B) "An Architectural Kernel and Composition Language ..." = ms_part1-4 -> the current
    flagship `revised_sustainability_manuscript.md` (Working preprint v1.0).

So these six files are NOT the current manuscript; they are the intermediate/archival line.
The line most likely to be cited is `revised_sustainability_manuscript.md`. Findings below
are about internal consistency of the versions named by the user; where a flaw is one the
architectural-kernel strand already fixed, that is stated.

## 1. manuscript.md / v0.1 / v0.2 (Robust Viability strand)

The three files are one text at increasing completeness; v0.2 and manuscript.md differ only
in the header label, the scope note, and the appendix block (manuscript.md drops the
traceability matrix and keeps expanded classification as Appendix D). No substantive
contradiction between v0.2 and manuscript.md. v0.1 simply lacks the §§4.9-4.12, 8.7-8.9,
9.5-9.9, 10.1-10.3, 11.6-11.10, 12.4-12.8, 13.3-13.5, 14.1, 15.1-15.2 expansion; nothing
in v0.1 is contradicted by the expansion.

Confirmed FLAWS / internal inconsistencies (all minor; no math/proof error):

F1. TWO RIVAL "VIABILITY REGION" DECOMPOSITIONS, K vs K*, NEVER RECONCILED. The single
    clearest internal gap in the Robust-Viability text.
    - \u00a74.4: K = K_P \u2229 K_F \u2229 K_N -- factored by constraint MEANING (physically
      feasible, functionally viable, normatively acceptable).
    - \u00a75.1: K* = K_x \u2229 K_c \u2229 K_e \u2229 K_d \u2229 K_\u03bb -- factored by
      augmented-state COMPONENT (focal state, capacity, support, distribution, liability).
    Both are introduced as "the" viability region; the formal core (\u00a75.3 robust
    sustainability, \u00a74.9 state sustainability) uses only K*. The manuscript never
    states K = K*, whether one is a subset of the other, or how the two factorizations
    interact. (\u00a75.2's \u03a9 even uses a bare K in its constraint slot.)
    NOTE: the architectural-kernel strand explicitly identifies and fixes exactly this --
    ms_part1 \u00a76.1: "This registry resolves the manuscript's earlier dual decomposition
    ... Physical/functional/normative describes a constraint's meaning. State/capacity/
    support/distribution/liability describes its subject. They are orthogonal tags on one
    record, not rival geometries." So the flaw is real in manuscript.md and already
    resolved in the successor.

F2. THE GENERAL SUSTAINABILITY CONJECTURE IS RETIRED IN ONE STRAND BUT REMAINS THE CENTRAL
    CONJECTURE IN THE OTHER (substantive cross-version conflict -- the most important one).
    - manuscript.md / v0.1 / v0.2 \u00a716.1: asserts "Every persistent sustainability
      failure can be represented, at an adequate scale and resolution, as the loss or
      anticipated loss of robust controlled invariance in a causally closed augmented
      state space ..."
    - ms_part4 \u00a728.1: "The former unrestricted claim that every sustainability failure
      can be represented at an 'adequate scale and resolution' is retired because it is
      too elastic to falsify."
    If both strands remain live program documents, these directly contradict: the older
    "Robust Viability" text still carries, as its headline central conjecture, precisely
    the claim the newer text removes as unfalsifiable. Recommend marking v0.1/v0.2/
    manuscript.md superseded (which the repo already does) OR adopting the retirement in
    the Robust-Viability strand.

F3. INTERDEPENDENCE FIXED-POINT CONJECTURE STATED VERBATIM TWICE. \u00a79.9 and \u00a716.2
    (lines 637 and 1144) are identical and both introduced as "a conjecture." \u00a716's
    "Central conjectures" is therefore not a new list but partly a restatement of \u00a79.9.
    Recommend \u00a716.2 reference \u00a79.9.

F4. SYMBOL OVERLOAD FOR GENERATION/REGENERATION AND FOR R. \u00a74.5 generic balance uses G
    (\u1e63_i = I_i+G_i-O_i-D_i); \u00a77.1 uses R (\u1e63 = I+R-O-D) for the same role;
    \u00a711.6 uses R(s,c,e) as a growth function; and \u00a711.1 uses R as the renewable-
    resource STOCK. The same letter R (and G/R switching) denotes different objects across
    sections. Also K is used for viability region (\u00a74.4), productive capital
    (\u00a711.2), carrying capacity (\u00a711.1 K_R(E)), and the model-parameter K.
    Cosmetic, but confusing for a formal document.

F5. K FROM \u00a74.4 IS EFFECTIVELY UNUSED IN THE FORMAL CORE; only K* appears after
    \u00a75.1. Minor notational orphan.

Verified CLEAN (no error): the necessary conditions \u00a77.1-7.7 (the \u00a77.7 bound
Y \u2264 C\u0304/\u03b1 is trivially correct; \u00a77.1 liminf average and \u00a77.4 delay
identity are correct); the 12 operational principles (\u00a78.9) match the traceability
matrix "twelve"; the six proof obligations (\u00a713.4) = 6; the twelve-step diagnostic
(\u00a713.5) = 12 steps; the seven certification levels 0-6 (\u00a713.3) = 7; eight
hypotheses H1-H8 (\u00a714) = 8; four nested models (-\u00a715 / \u00a715.2); two central
conjectures (\u00a716); the four sustainability dimensions (\u00a74.9). The claim-type
taxonomy D/L/P/E/M/N is applied consistently (claim ledger Appendix B and protocol
Appendix C both list the same 6).

## 2. ms_part1-4 (Architectural Kernel strand)

Confirmed FLAWS / internal inconsistencies (all minor):

F6. "EPISTEMIC" CONSTRAINT TYPE DECLARED BUT NEVER CARRIED INTO THE PROJECTIONS OR THE
    JUDGMENT VECTOR. ms_part1 \u00a76.1 gives constraint type \u03c4_j FIVE values
    (physical, functional, normative, relational, epistemic) and the abstract lists
    "epistemic status" as one of the five. But \u00a76.2 builds projections only K_P, K_F,
    K_N, K_R, K* = K_P\u2229K_F\u2229K_N\u2229K_R, and \u00a76.3's judgment vector is
    (P\u03a9, F\u03a9, N\u03a9, R\u03a9). The epistemic type has no projection and no
    component in K* or the judgment vector. (Presumably epistemic is meant to govern
    claim type / confidence rather than the viability judgment, but that is not stated
    and the five-type list in \u00a76.1 includes it among meaning-types.) Unclosed tag.

F7. PROOF OBLIGATIONS EXPANDED 6 -> 9 WITHOUT THE FLAGGING THE DOC OTHERWISE DOES.
    Robust Viability \u00a713.4 = six (semantic, accounting, dynamic, closure, robustness,
    legitimacy). ms_part4 \u00a726 = nine (adds boundary [renaming closure], composition,
    transformation, commons). This expansion is not acknowledged even though ms_part4
    flags every other retention (12 principles "retained but reclassified"; four views
    "retained"; certification hierarchy "retained but renamed"). Recommend a one-line note
    "the earlier six obligations are retained; composition/transformation/commons are added."

F8. \u00a714 SAYS "TWELVE PRINCIPLES RETAINED BUT RECLASSIFIED," YET PRINCIPLES 8 AND 9 ARE
    RENAMED/EXCHANGED, NOT MERELY RECLASSIFIED. Robust Viability \u00a78.9 #8 = "Nested-
    systems," #9 = "Burden-displacement"; ms_part3 \u00a714 #8 = "Typed-dependency," #9 =
    "Burden-allocation." The change is substantive (matching the architecture-typed
    vocabulary) and is understated by "reclassified."

F9. CONJECTURES APPEAR TWICE (as numbered Boxes AND as \u00a728 Conjectures). Conjecture 1
    (Compositional) = Box 10 verbatim-ish; Conjecture 2 (Transformability) = Box 6
    verbatim-ish. Box 11 ("proof obligation -- sound composition") is the same obligation
    as \u00a726 #7. Duplication rather than cross-reference.

F10. BOX 1 "CONTRIBUTION TYPE" IS NOT ONE OF THE TEN BOX TYPES LISTED IN THE \u00a73 BOX
    TAXONOMY. Cosmetic.

F11. APPENDIX B CONSTRAINT-REGISTER TEMPLATE OMITS "D" FROM ITS PROVENANCE PLACEHOLDER.
    Appendix B provenance placeholder is "[P/E/M/N/L]" (5 types, missing D=Definition);
    Appendix G uses "D/L/P/E/M/N" (6). Also Appendix B's Type column "P/F/N/R/Epistemic"
    and its Provenance column "P/E/M/N/L" both use the letter P for two different
    taxonomies (constraint-meaning "physical" vs claim-type "physical constraint") in
    adjacent columns. Minor.

VERIFIED CLEAN in ms_part1-4: Lemma 1's sign convention (net-outflow>0 => impossible) is
consistent with the Robust-Viability \u00a77.1 average-balance necessary condition; Lemma
8's cross-reference to "Section 7.2" is VALID (ms_part1 \u00a77.2's final sentence states
the "no admissible within-architecture trajectory can reach a state with a nonempty
corridor" reachability condition); the control-hierarchy ordering U_impl \u2286 U_inst
\u2286 U_tech \u2286 U_theor matches Robust-Viability \u00a712.2; the four nested models
(\u00a730) = 4; the five contract modalities (Deterministic/Robust/Probabilistic/Strategic/
Scenario, \u00a712.1) = 5 and match the abstract and \u00a733 #9; boxes number consecutively
Box 1..13; the four analytical views (\u00a77.1) match the Robust-Viability four dimensions;
the "actual initial state" emphasis (\u00a77, abstract) is a deliberate and consistent
tightening over \u00a75.3's z_0 \u2208 K* formulation (with kernel-non-emptiness caveat).

## 3. Cross-cutting / citation
- ALL in-text citations (Aubin 2009/2011; Ekins 2003; Folke 2010; Holling 1973; Meadows
  2008; Neumayer 2013; Ostrom 2009; Raworth 2012/2017; Rockstr\u00f6m 2009; Steffen 2015;
  Walker 2004; WCED 1987) have reference entries, and the reference list is identical
  across all six files.
- ONE ORPHAN REFERENCE: Chen, Anderson, Kalsi, Low & Ames (2019), "Compositional set
  invariance in network systems with assume-guarantee contracts," appears in the
  reference list of every file but is NEVER cited in the body of any of them (the
  assume-guarantee discussion in \u00a72.6 is uncited). Recommend either citing it at
  \u00a72.6/\u00a79.2 or removing it.

## 4. Overall verdict on the general-theory family
No mathematical error, no falsely promoted theorem (lemmas are explicitly "intentionally
modest ... not novel universal laws" and conditional; proofs are offered only as
not-carrying; every certified-object claim is conditional and qualified). The epistemic
discipline ([D/L/P/E/M/N]) is adhered to; the honest "candidate first synthesis, not a
validated universal law" framing is consistently honoured. Remaining issues are all minor
and fall into two classes: (A) F1 (the dual K/K* decomposition) is the one genuine
internal-conceptual weakness in the Robust-Viability text, and it is already resolved
in the architectural-kernel successor (\u00a76.1); (B) the rest are duplication,
symbol-reuse, and unclosed-tag/uncited-reference editorial items (some with an already-
flagged or explicit fix). The only substantive cross-version conflict is F2 (the retired
vs. retained "every persistent sustainability failure" conjecture), which follows directly
from the two strands' different treatment of falsifiability and which the repo's own
status marking resolves in favour of the "architectural kernel" strand.
----
New content-level finding for paper 1 (the one thing actually worth fixing in §4.1)

The closed-cone justification conflates the direction of its own "a fortiori." §4.1(iii) (and the theorem file §2 item (iii)) argues: "the closed cone is the most permissive natural family, so every separation proved against it holds a fortiori for any subfamily."

This is backwards for the region-size reading. A larger weight family is an easier target for the aggregate only if you mean it gives the aggregate more purchase — but here "∀w∈C" makes a larger C stricter, so it shrinks ⋂_w{P_w} and shrinks the false-positive region. So a subfamily (e.g. strictly positive prices) yields a larger gap, and proving the separation on the closed cone is actually the weakest case, not the case that "holds a fortiori."

Concretely: I verified that on the datum the closed cone and the open cone coincidentally give the same aggregate region ⋂_w{P_w} = {x≥1} ∪ {s₁+s₂≥2} (the boundary zero-price weights e₁,e₂ are already covered by SLOW/FAST when s>0, and s>0 throughout FP). So no result changes — the claim is not wrong, and the truthful statement (the one the theorem file's §9 actually gives) is: "the intersection over a subfamily is larger, so the strictness (nonemptiness) persists." That's the correct a fortiori direction — and note it is the reverse of what §4.1(iii) says about ⋂ being smaller.

Recommendation: reword §4.1(iii) to the two genuinely substantive reasons (zero-price semantics; Lemma 3 only holds on the closed cone, which is what powers Theorem A(ii)) and replace the "a fortiori" sentence with the correct statement from the theorem file §9. This is the single content-level edit I'd make.
