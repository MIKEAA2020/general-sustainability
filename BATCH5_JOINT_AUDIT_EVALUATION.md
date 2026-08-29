# Batch 5 — Joint Audit Evaluation and Corrected Editions

**Date:** 2026-08-29. **Audited state:** commit `7ef81f5` (the batch-5 uploads on top of Task 58's `8a286c4`; working tree clean for all manuscript paths).

**The audits evaluated (seven documents from four independent auditors, assessed jointly on their merits, without order bias):**

| Auditor | Document | Scope |
|---|---|---|
| Arena agent 1 | `batch 5/arena agent1_5 papers.txt` | Papers 1–5 (13 findings) |
| Arena agent 1 | `batch 5/arena agent1_waveE.txt` | The four Wave E manuscripts (8 findings) |
| Arena agent 1 | `batch 5/arena gent1_old manuscripts.txt` | The flagship/ms_part monograph family (8 findings) |
| GLM | `batch 5/glm/review_report.md` | Papers 1–5 (26 findings, F01–F26) |
| GLM | `batch 5/glm/review_report_wave_e.md` | The four Wave E manuscripts (13 findings, W01–W13) |
| GLM | `batch 5/glm/review_report_general_theory.md` | The monograph family (14 findings, G01–G14) |
| Arena agent 2 | `batch 5/arena agent 2/review_findings.md` | All nine manuscripts + the monograph family (numbered findings, deep-dives, E1–E5, F1–F11) |
| Qwen | `batch 5/qwen.txt` | Papers 1/2 arithmetic + Edwards intervention + the monograph family (3 + 2 + 6 findings) |

**Implementation discipline (per the owner's instruction):** every accepted change is implemented in **new file versions**; the audited current versions are left byte-identical. The new editions are listed in §5. Where an auditor's suggested fix was itself defective, the fix was corrected before implementation (§3); where a suggestion would have fabricated content, the source-faithful correction was implemented instead (§3.3, §3.4).

---

## 1. Verification performed before adjudication

Every load-bearing claim was re-verified against the repository before acceptance:

- **The Brier paragraph (W01).** Read from `wave_e_cod/results/rolling_summary.csv` (Ω_2016) and `results/xte_rolling_summary.csv` (Ω_xte): the committed Ω_2016 Brier values are exactly the six numbers printed in §5.3 of the cod forecast paper (persist 0.00/0.00; M1 0.04/0.0476; M1b 0.00/0.0476; M2 0.08/0.1429; M3 0.08/0.0952; M4 0.08/0.1429), and the committed Ω_xte values are persist 0.0635/0.2712, M1 0.0508/0.4545, M1b 0.1525/0.4727, M2 0.0678/0.3636, M3 0.0169/0.3091, M4 0.0678/0.3818. The paragraph sits inside the Ω_xte section; the concluding sentence is false on Ω_xte. Confirmed, and **strengthened**: both M3 (0.017) *and M1* (0.051) improve the one-year Brier over persistence (0.063) — the GLM replacement names only M3.
- **The flat-180-kt kernel (W02).** Ran a corrected runner (`wave_e_cod/src/run_intervention_v2.py`: T=∞ iteration cap 300 → 20000 with an explicit convergence assertion) writing to new result files: the regenerated JSON differs from the committed one in **exactly one value** — `kernels.flat_75.UC_q10.inf.nominal[0][0]: 2335.4153815153377 → 2338.273378118786` — confirming GLM's root-cause diagnosis (the 300th backward iterate of a recursion needing ≈1456 steps at F′ = 1.0155 per step) and the inertness of the fix for every other table entry. The true fixpoint matches the same JSON's `steady_states` field (2338.27) and the fixed-point algebra rS(1−S/K) = 294.8477.
- **The Edwards `lt` comparator (W12).** Ran `wave_e_edwards/src/run_intervention_v2.py` (the cod runner's corrected comparator ported in): the regenerated JSON and CSV are **value-identical** to the committed artifacts — the asymmetry is inert for the committed results, exactly as GLM's 216-reading analysis claimed. The retention verdicts (S1, cpm retained) are unchanged.
- **BAU's nominal kernel horizon (W03).** Recomputed analytically from a = 0.746094, H\* = 615.72: boundary(T) = H\* + (618−H\*)/a^T exceeds the domain top 710 at T > 12.70; the T=12 boundary is 692.56 ft and the T=13 kernel is empty. The committed grid {1,2,3,5,8,10,15,20,∞} shows nonempty-at-10/empty-at-15 with no direct evidence for "14". Confirmed.
- **The reproducibility claim (W04).** Re-executed all four optimizer-based cod forecast runners in this environment (Python 3.12.14, numpy 2.1.3, scipy 1.14.1, pandas 2.2.3): 13 of 19 result files regenerate with differences; every scored row reproduces at printed precision **except the M1b Ω_xte rolling row** (h=1: 151.63 → 153.19; h=5: 445.48 → 462.53) — reproducing GLM's finding exactly, and consistent with that model's declared identification fragility. The retention verdict (persistence wins on Ω_xte at both horizons) is robust to the instability.
- **The fold contradiction (F01).** Read the A018 source: the reconciling sentence ("The orbit remains a converged fixed point of the collocation map through τ=5.5815 …, while long-horizon simulation shows the basin collapse between τ=5.574 and 5.576; the exact crossing point and the 0.002 yr gap remain to be pinned") is present in the source's Numerical Result [Lower boundary of the inner three-state problem] and was dropped in Paper 4's compression. The +1-crossing signature is exhibited by the **small** branch (multiplier 1.0514 at τ=5.584 → 0.99898 at τ=5.587), not by the large branch at the printed τ=5.5815 (multiplier 0.964 < 1). Confirmed and implemented with the branch-resolved statement.
- **The price-assessor inversion (P1-01 / qwen #2).** Re-derived: FAST dips s_1 and preserves s_2, so FAST is aggregate-safe iff r = w₂/w₁ ≥ ρ₁; SLOW iff r ≤ ρ₂; on the triangle interior ρ₁ < ρ₂, so high s₂-price (large r) licenses FAST only, low s₂-price licenses SLOW only, intermediate licenses both — the printed sentence is exactly reversed, and the machine witness (r = ½ SLOW-only, r = 2 FAST-only) agrees. Confirmed. Note the auditor's own replacement had ρ₁/ρ₂ interchanged (it wrote "ρ₂ ≤ r ≤ ρ₁" for the both-licensed band, which is empty on the interior since ρ₁ < ρ₂); the implemented sentence uses the correct bands r < ρ₁ (SLOW only), ρ₁ ≤ r ≤ ρ₂ (both), r > ρ₂ (FAST only).
- **The concordance accounting (F07 + qwen #1/#3).** Recomputed from `research_program/canonical_concordance_A001_A025.csv`: 409 rows = 354 `row_verified` across **19** sources (A001–A007, A010–A020, A024, A025) + 28 `adjudicated_rejected_or_negative_only` (A008, A009, A015) + 24 `requires_row_level_verification` + 3 `mapped_requires_final_citation_check` (together exactly the 27 open rows of A021–A023). The closure report's own header enumerates the nineteen sources while its title says "Twenty" and its "thirteen further closures" sentence enumerates twelve. The intake audit's twenty-sixth registered item is the versioned master corpus (Paper 2 §1.1). All three auditors' arithmetic complaints resolve to this one accounting sentence, now stated completely.
- **The family count (F04/P2-04, with arena agent 2's correction).** Counted the atlas's family-labelled sections: F00 (§2 preliminaries), F13 (§3), F01–F07 (§§4–10), F10–F12 (§§11–13) = **twelve families carried**, matching the abstract's "twelve"; the budget CSV's taxonomy runs F00–F14 with F08/F09 delegated to the ledger paper/monograph and F14 the conditional docket. Arena agent 1's premise that "§1.2 is titled 'Thirteen mapped families'" is **false** — no such heading exists in the manuscript (the phrase comes from the venue memo, not the atlas). The genuine residue: the abstract enumerated only ten of the twelve names, and nothing explains the F07→F10 numbering skip. Both fixed.
- **The out-of-order remarks (F05/P2-01).** Verified the appearance orders (§5: [1,2,3,9,4,…,8]; §6: [1,2,16,3,…,15]; §8: [1,2,3,4,15,5,…,14]; §13: [1,2,4,3]) and that each moved remark references only items that precede it in its new position; implemented by **moving the four remarks to their numbered positions** (end of section) rather than renumbering — no numbering, ledger row, or cross-paper reference changes.
- **Theorem 6.4's proof (F02).** Constructed the one-step proof from the source's definitions (R_V(x) = U(x) at interior points, so the empty intersection forces a boundary state x̄ with a ∉ R_V(x̄); the defining inequality gives an active constraint and a disturbance with ∇q_j·f < 0, and holding that disturbance makes the compatible trajectory exit within the first sampling period, before any informative observation). The ledger row and §15's "one proof is omitted" sentence are updated to record the discharged obligation.
- **The CES preamble (F06/P2-02).** Read the A001 source's §8.1: the specification F(A,R) = Y₀[α(A/A₀)^ρ + (1−α)(R/R₀)^ρ]^{1/ρ}, ρ = (σ−1)/σ, and μ_A := (Y₀/A₀)α^{σ/(σ−1)} (σ > 1) — restored verbatim as a preamble; the source's item 5 reads "If σ > 1 and μ_A = δ_A" and the atlas had dropped the qualifier. Confirmed.
- **The quantifier (P2-05).** The hypothesis is sup_u inf_d D⁺q ≤ −ε (Isaacs-type: the disturbance chooses after the control); the proof enforces the bound along the trajectory. The source (A001 Theorem 5.2) carries the same over-strong phrasing; the atlas's corrected edition states the enforced-exit reading and records the source's phrasing.
- **The loop-gain maximizer (P4-02).** Recomputed independently from the linearisation (L(iω) = −A_E·iω/(2τ_m) via the even-pairs identity; A_N = −0.0179104, d = 0.2, C_E = −0.850336, C_Z = −1.661702, A_E = −0.0895519, τ_m = 5): the maximum of Γ is 0.0801130 at ω = 0.05891 — the printed value 0.08011 is right, the printed frequency 0.0583 is not. Confirmed; corrected to ω ≈ 0.0589.
- **Proposition 5.2's shifted delays (P4-01).** Recomputed: 3.666149 + π/0.0251764 = 128.374 (up-shift on the ω₁ family) and 150.358477 − π/0.0394360 = 70.697 (down-shift on the ω₂ family) — the values are right; the labels τ₋/τ₊ retain their original-family meaning so the order is reversed on the shifted axis, which the statement now says. (The auditor's quote included the words "with both shifts strictly positive", which do not occur in the committed file; the arithmetic finding stands.)
- **Qwen's double-counting claim (Edwards intervention §3/§4.3) — REJECTED.** The manuscript's own definition (§3) is "the certified kernel at horizon T is the nominal kernel of K\* + r_T", and the printed boundary 662.2 solves exactly the **nominal** (UC-min, no-defect) trajectory equation 647.32 + a³(H₀ − 647.32) ≥ 618 + r₃ — the defect enters only through r_T, so there is no double count. Qwen's counter-argument assumes 647.32 already includes the defect (it does not: 647.32 = (163.492 + 0.019831·43.7)/0.253906 is the no-defect UC-min attractor; the defect-inclusive attractor is 586.63) and derives the "nominal" attractor 708.01 = 647.32 + r_∞ by that misattribution. The equivalence is exact: the worst-defect trajectory is the nominal trajectory minus r_t identically, so "nominal ≥ K\* + r_T" and "worst-case ≥ K\*" name the same set. **However, the verification surfaced a genuine adjacent defect** that no auditor had isolated: under UC-min, zero pumping's certified physical-threshold kernel is nonempty at T=4 (analytic boundary ≈ 687.9 ft; empty from T=5), so §4.3's "every policy in the family has an empty certified kernel beyond T = 3 years" was false for flat-0 under UC-min (the committed horizon grid {1,2,3,5,8,10,15,20,∞} skips T=4, and the JSON's `certified_horizon_nonempty` records the largest *grid* horizon). Corrected in the second edition with the analytic boundary.
- **Box 13's twelve steps (qwen #5) — REJECTED.** The committed ms_part4.md Box 13 lists all twelve steps (1–12, complete through "Issue a typed result, maturity level, and unresolved-proof-obligation report"); GLM's count verification agrees. No truncation exists.
- **Lemma 8's §7.2 pointer (GT-02) — REJECTED.** ms_part1 §7.2's closing sentence states the reachability condition verbatim ("Architectural transformation is required only if no admissible within-architecture trajectory can reach a state with a nonempty corridor before entering a forbidden set"); the pointer is valid (arena agent 2's verification is correct). The corrected edition adds §8.2 as a secondary pointer since the formal operator lives there.
- **The tether threshold α (F18) — STRENGTHENED.** The "≈1.3×10⁻³ at the illustrative parameterisation" occurs nowhere in the A018 source (which states only the ratio form μ_E^SN ≈ 5.9α "at an illustrative parameterisation" that it does not tabulate) and the parameterisation exists nowhere in the repository. The auditor's suggested fix ("add the illustrative values") would have required values that do not exist; the implemented fix withdraws the unverifiable number and records the source's ratio form, aligning the manuscript with its own ledger row.
- **A display-pipeline false positive, documented for future auditors.** During verification, five Paper 1 headers appeared corrupted ("anuscript-native") through the terminal pipeline, which eats the literal two-character sequence `[m`; a hexdump showed the file intact (`5b6d616e…` = `[man…`). Auditors quoting text through such pipelines should hex-verify before reporting `[m…`-shaped "corruptions". (The genuinely corrupted `[m`-family defect class does exist elsewhere in the corpus — see G01, where `\r` of `\rightarrow` became a raw CR byte — and was fixed.)
- **The G3P magnitudes (F19).** Arena agent 2's retraction verified: the §5.5.2 table back-computes exactly against the A018 source's own table (implied minima −548/−292/−237/−88/−33), and the source frames the values as GRACE-window-relative. GLM's magnitude caution is implemented as a one-sentence window-relative note rather than a change of values (the values are the source's; unit/mask re-verification is part of the already-registered pending submission supplement).
- **The monograph CR corruption (G01).** Byte-verified in `ms_part2.md` (two 0x0D bytes where `\r` of `\rightarrow` belonged) and in `revised_sustainability_manuscript.md` (the same line with the CR degraded to a line break, leaving bare `ightarrow` inside the display math of the hybrid trajectory — Operator II's defining state object). Fixed in `ms_part2_corrected.md` and `revised_sustainability_manuscript_v1.1.md`.
- **Spot-verified and held (agreeing with the auditors' own positive lists):** Paper 1's machine witness (25/25), the cod/Edwards intervention kernel tables against the JSONs, the cod attractor/expansion arithmetic (F′(K\*) = 1.15308, g(K\*) = 172.47, 57.62 kt), the Edwards attractor table and the 7.22% minimal cut, the certified boundaries 662.2/697.8/706.7, the stress-replay paths (S1 906.5, cpm 876.5, BAU 901.5 in 1991; flat caps 666.5–846.5), the T=5 classification sets ({1985,1987,1989} for the 60-kt rules; {1985,1987,1988,1989} for BAU), Paper 4's linearisation coefficients and Hopf cubic, the interval certificates, and the version-lineage additivity of the flagship chain.

---

## 2. Findings adjudicated and implemented (by new file)

### 2.1 The five core papers — `papers/paper{1..5}_*/manuscript_v2.md`

| Finding (auditor) | Adjudication | Implementation in the v2 edition |
|---|---|---|
| P1-01 / qwen #2 — Theorem B(6) price-assessor sentence inverted | **Accept** (fix corrected: the auditor's threshold bands were interchanged) | §4.5(6) restated: high-s₂-price (r > ρ₂) licenses FAST only; low (r < ρ₁) SLOW only; intermediate both |
| P1-02 / F08 — "thirteen slots" enumerating 11 | **Accept** | §2.2 replaced by the source's 13-tuple with slot names, matching Paper 2 Def 2.3 |
| P1-03 / F12 — "closed nonnegative cone" naming a punctured set; §4.1(iii) a-fortiori direction (arena agent 2's content finding) | **Accept** | C named the nonzero nonnegative orthant; the third reason restated in its exact order-theoretic direction (the full-cone intersection is the *strictest* aggregate reading; subfamily intersections are supersets, so the separation persists under restriction) |
| P1-04 / F13 — `Succ ⊆ W` typo; `G^w` undefined | **Accept** | `Succ ⊆ G`; S^w/G^w defined at the E_w bullet |
| P1-05 — three `[cite:]` placeholders | **Accept** | Resolved to author–year citations matching the reference list |
| F07 / qwen #1 / qwen #3 — "twenty sources"; 354+27 leaving 28 unaccounted; 26-vs-23 sources | **Accept** | §10.2 states the full accounting (354 + 28 + 27 = 409; nineteen closed sources; the versioned master corpus carries no rows) and records the closure report's title overcount |
| F09 / W13 / F22 — "two scored-forecast papers" vs four Wave E manuscripts | **Accept** | §§1.5 and 10.1 count the four Wave E manuscripts |
| F14 — Das–Dennis 1997/1998; "Usubiaga-Liaño et al." single-author | **Accept** | Citation and name corrected |
| F11 (Paper 1) — Ekins et al. 2003 uncited | **Accept** | Cited at the weak/strong-sustainability sentence |
| Arena agent 2 finding 6 — reset gain `e` undefined | **Accept** | `e = (1/4, 1/4)` declared in §4.4 |
| F20 — CC-A001-084 destination rendered three ways | **Accept** | Canonical rendering in both ledgers: "Paper 1 §7.3 (conditional on the registered prerequisite result; otherwise Paper 2)" |
| F04 / P2-04 (corrected) / arena agent 2 finding 3 — family count and enumeration | **Accept, corrected** (the "§1.2 thirteen" premise is false; twelve is the right count) | Abstract enumerates all twelve family names; the F08/F09/F14 delegation note added |
| F05 / P2-01 — four out-of-sequence remarks | **Accept** (implemented by moving the remarks to their numbered positions, not renumbering) | Remarks 5.9, 6.16, 8.15, 13.4 moved to end-of-section; numbering now monotone in appearance order; all cross-references unchanged |
| F02 / arena agent 2 D — Theorem 6.4 "theorem" without proof | **Accept, strengthened** (proof supplied rather than relabel) | One-step proof printed (discharging the registered obligation); ledger row 24 and §15 updated |
| F03 — Cond. Thm 10.1 undefined y/A/v₀/H_loc | **Accept** | Source's preamble restored; T_A defined as the hitting time of {A ≤ A_min} |
| F06 / P2-02 — CES specification and μ_A never stated; item (5) dropped "σ > 1" | **Accept** | Preamble restored from the source; qualifier restored |
| P2-03 — duplicate "Hypothesis object 12.3" | **Accept** | Split into 12.3a/12.3b in §12 and ledger rows 85/86 |
| P2-05 — Theorem 3.4 quantifier | **Accept** | Enforced-exit conclusion with the Isaacs-type reading; the source's phrasing recorded |
| F21 — R^n_{++} vs R^n_{>0} | **Accept** | Standardised to R^n_{++} |
| Arena agent 2 finding 4 — "seven further sources" vs row 89 from A002 | **Accept** | §§1.2, 14, 15 state "seven further sources together with one further A002 row (row 89)" |
| F11 (Paper 2) — Aubin 1991, Hale 2009 uncited | **Accept** | Cited at Theorem 3.3's proof and Cond. Thm 10.2's why-conditional |
| P3-01 — A_g0 missing from the baseline | **Accept, corrected** (the auditor's "add A_g0 = 100 or 0" would fabricate a value the source does not give) | §2.2 declares A_g0 > 0 with the source's separation-of-scale condition A^geo ≫ A_g0 and identifies the A_g0 = 0 corner as the discontinuous-perturbation limit |
| P3-02 — K/N overloading in §2.4 | **Accept, modified** (declaration rather than rename, protecting the exact-specialization fidelity to the A001 source) | Local-notation declaration at the head of §2.4 |
| F15 — "extraction and mining rates" vs an extraction-only identity | **Accept** | Abstract and §3.4 reading restated (mining restored → C^A = 0 in the registered specialization) |
| F19 — G3P magnitude caution | **Accept as note** | Window-relative magnitudes sentence in §5.5.2; supplement re-verification already registered |
| Arena agent 2 C / D-2 — 54-vs-52 ledger identifiers; 43/42 stocks | **Accept** | Cross-reference markers in the two destination cells plus a one-line note under the ledger; the nested-populations cross-link added |
| F11 (Paper 3) — 16/18 references uncited | **Accept** | Hooks at the data/method-bearing points (Griebmeier/Tapley/Guentner at §5.5; USGS at §5.5.3; Ricard at §5.5.2 and §5.5.4; Chhikara–Folks/Redner at §6.3; Øksendal at §6.5; Munda/Nuemayer/Ekins at §1.1; Brunner–Rechberger/Eurostat/Fischer-Kowalski/Feinberg at §2.1) |
| F01 — the fold bracket vs multiplier contradiction | **Accept, strengthened** | §6.1 rewritten branch-resolved: the basin collapse [5.574, 5.576] (long-horizon simulation), the collocated branch persisting through τ = 5.5815 with multiplier 0.964 < 1, the +1 signature exhibited on the small branch, the source's dropped reconciling sentence restored, and the SNPO classification of the large branch marked provisional (crisis-like basin loss the alternative reading) |
| P4-01 — τ₋ > τ₊ subscript inversion | **Accept** | Proposition 5.2 states the branch mapping and the reversed order explicitly |
| P4-02 — loop-gain frequency | **Accept** (independently recomputed: argmax at ω = 0.05891) | Corrected to ω ≈ 0.0589 |
| F16 — §6.5 mixed-variant τ₊ pairing | **Accept** | "τ₊ ≈ 132–150 yr (A) and ≈ 76–80 yr (B) across the two effort laws" with the four values |
| F17 — g doubling as flux and gain in §7.1 | **Accept** | Memory gain renamed γ_m throughout §7.1 with the source-convention note |
| F18 — α unverifiable | **Accept, strengthened** (the number exists nowhere; withdrawing it is the only non-fabricating fix) | §8.3 states the ratio form and records that the source does not tabulate the illustrative parameterisation |
| Arena agent 2 B — certification-tier footnote | **Accept** | §10's interval-certificate paragraph states that the enclosures are the certified tier *for the local spectrum of H* while the global folds remain nominal |
| Arena agent 2 C (Paper 4) — 70-vs-68 ledger identifiers | **Accept** | Cross-reference markers plus the ledger note |
| F11 (Paper 4) — ≈21/37 uncited | **Accept** | Hooks at the lineage and method points (Ezekiel/Ludwig/Gurney/Gao–Zhang/Khiyar/Moxnes/Ostrom at §1.1; Hale×2/Diekmann at §1.2; Engelborghs/Guckenheimer–Holmes/Kuznetsov at §6.1; Beretka–Vas at the fold-status paragraph; Åström–Wittenmark at §6.4; Scheffer×3/Carpenter at the early-warning remark; Costantino at the stage-registration paragraph; Moore/Kearfott/Cloud at §10) |
| F10 — "the Schaefer model is the Allee-factor-1 specialisation" | **Accept** | §6.2 restated: the Schaefer model is the degenerate member in which the factor is replaced by 1; no 𝔰 makes the displayed factor identically 1 |
| F23 — Bangkok/La Mancha "closest stabilising cases" vs the relapse | **Accept** | "Bangkok (durably) and La Mancha Oriental (… before its 2019–2023 extraction relapse)" |
| Arena agent 2 B (Paper 5) — 58-vs-57 ledger identifiers | **Accept** | CC-A002-034 marked as a cross-reference in §11 and the ledger |
| F11 (Paper 5) — ≈14/22 uncited | **Accept** | Hooks at the data/method/lineage points (Ricard, Benjamini–Hochberg, Cohen, Forssell–Ljung, Ashwin, Nešić–Teel, Aubin×2, Cadigan, Tam–Bundy, Costantino, Moxnes, Punt–Donovan, Gurney) |
| F24 / F25 / SYS-01's cross-checks | **Verified, no action** | — |

### 2.2 The four Wave E manuscripts — `wave_e_*/manuscript/*_v2.md`

| Finding (auditor) | Adjudication | Implementation |
|---|---|---|
| WEC-01 — 𝔰 = 0 does not deactivate the Allee factor | **Accept** | §3 states the exact piecewise growth law (factor ≡ 1 for Schaefer; (S−𝔰)/(K−𝔰) only when 𝔰 > 0 is declared) with the cubic-degeneration note |
| W01 — Ω_2016 Brier values inside the Ω_xte section; false conclusion | **Accept, strengthened** (M1 also improves at h=1) | §5.3 carries the Ω_xte values with the corrected conclusion; the Ω_2016 values retained in a clearly labelled reference sentence (non-loss) |
| W02 — flat-180 T=∞ boundary unconverged | **Accept** (root cause fixed in code) | Table prints 2338.3; `src/run_intervention_v2.py` (cap 20000 + convergence assertion) writes `results/intervention_results_v2.json`/`_boundaries_v2.csv`, differing in exactly that one entry; availability section documents both editions |
| W03 — "empty beyond T ≈ 14" | **Accept** (crossover 12.71 verified) | "empty beyond T ≈ 13" with the T=12 boundary 692.6 ft; SPECIFICATION.md's repetition of "~14" recorded here (that file is a current version and stays unchanged) |
| W04 — byte-for-byte claim environment-fragile | **Accept** (reproduced in this environment) | Availability section states the determinism-in-environment claim, the recorded environment, the cross-environment record (13/19 files differ; M1b xte ±17 kt optimizer sensitivity), and why the verdict is robust |
| W05 — 172.5 − 114.8 vs 57.6 | **Accept** | Operands printed at exact values (172.47 − 114.85 = 57.62) |
| W06 / E1 — abstract's "within 0.13 ft" includes M2_Rar | **Accept** | Abstract excludes the AR(1)-on-recharge variant (0.4 ft worse) |
| W07 — garbled T=5 classification sentence | **Accept** | Both kernels named with their year sets |
| W08 / WEC-04 / WEC-05 — reference hygiene | **Accept** | Schijns 2675–2683; Cadigan at the NCAM mention; DFO 2009 at the critical-zone vocabulary; DFO 2016 cited in the intervention paper; DFO 2024/049–050 and the Zenodo entry cited where the 2024 assessments and the acoustic index are discussed |
| W09 — abstract range mixes catch passes | **Accept** | "115–196 kt … (115–206 kt across both catch treatments)" |
| W10 — I_ref, b undefined | **Accept** | Defined (training-window median; jointly fitted) |
| W11 — freeze claim omits the recorded caveat | **Accept** | The SPECIFICATION's freeze-discipline caveat restated in §6 |
| W12 — Edwards `lt` asymmetry | **Accept** (inertness re-verified by re-execution) | `src/run_intervention_v2.py` with the corrected comparator; v2 outputs value-identical; availability section records both editions |
| W13 — two-vs-four scored papers | **Accept** | Paper 5 §9 and the cod §6.1 context sentence updated |
| WEC-02 — "critical-period rule" terminology leak + the 1991 contradiction | **Accept** (verified against `stress_replay_1990s`: S1 906.5 above; cpm 876.5 below; flat caps ≥ 60 below) | §2.5 rewritten with the rule-specific 1991 values |
| WEC-03 — "60 kt and deeper" ambiguity | **Accept** | "every flat cap of 60 kt and larger (C ∈ {60,120,180,240})" |
| WEE-01 / E5 — inverted figure filenames | **Accept** (E5's cod remark is a false positive: cod's Figure 4 = `fig4_xtencam.png` matches) | v2 embeds `fig4_pass2.png`/`fig5_fibre.png` — byte-identical copies of the committed files under matching names |
| WEE-02 — missing Abstract and References | **Accept** | Abstract and References supplied (companion-matched) |
| WEE-03 — M2_enso/M2_Renso collision | **Accept** | Standardised to M2_Renso/M2_Rprecip (matching the pass2_fixed keys and M2_Rar) |
| E2 — "deepest CPM trigger (660 ft)" inverted | **Accept** | "first-stage CPM trigger (660 ft — the highest of the four declared trigger levels)" |
| E3 — oracle gap against two baselines | **Accept** | Both baselines labelled at §1 and §5 |
| E4 — "harsher than any recorded drought" vs UC-min = the 1956 minimum | **Accept** | "the persistent floor regimes are harsher than any single recorded year (UC-min is the recorded 1956 minimum, held perpetually)" |
| Qwen #2 — 282.2 vs 282.16 | **Accept** | P̄ = 282.16 |
| Qwen #1 — certified-kernel double counting | **Reject** (misreading; see §1) with the adjacent genuine defect fixed | §4.3 records zero pumping's T=4 UC-min certified kernel (≈687.9 ft analytic) alongside the T=5 UC-q05/q10 horizon |
| GLM micro-notes 2–4 | **Accept** | Counts stated inline; 2021 checkpoint = 423 kt (the committed Table 17 value); post-collapse range 0.4–1.9 kt |

### 2.3 The monograph family

| Finding (auditor) | Adjudication | Implementation |
|---|---|---|
| G01 — CR-byte corruption of the hybrid-trajectory formula (ms_part2 + the current monograph + its docx lineage) | **Accept** (byte-verified) | `ms_part2_corrected.md` (arrows restored at byte level); `revised_sustainability_manuscript_v1.1.md` (formula on one line); the v1.0 docx is superseded by the v1.1 edition note (a docx regeneration of v1.1 is left to the existing build script at the next packaging pass, since the build scripts write the v1.0 paths) |
| G02 — five lone `\` in the boxed closing formula | **Accept** | `ms_part4_corrected.md` |
| G03 — the "epistemic" constraint type orphaned | **Accept** (operationalized, as the successor monograph does) | `ms_part1_corrected.md`: §6.2A adds K_E and the judgment component E_Ω; the τ_j enumeration and QSust updated; the ρ_j orthogonality note added |
| G04 — each series' template omits a first-class Ω slot | **Accept** | The 𝒩 line added to the flagship's Appendix A (all three corrected editions); the 𝒞 line added to ms_part4's Appendix A |
| G05 — the packet conflates the two 14 August 2026 manuscripts; "flagship" has two referents | **Accept** | Corrected in `external_review_packet/README_v2.md` (the packet's current README is a pinned current version and stays unchanged); the supersession is also recorded here |
| G06 — "retained but reclassified/renamed" overstates continuity | **Accept** | ms_part3/ms_part4 corrected editions state the two principle replacements and the two level redefinitions exactly |
| G07 — §27 rationale for six of ten indicators | **Accept** | Four clauses added in ms_part4_corrected.md and the monograph v1.1 (both carriers) |
| G08 — Chen et al. uncited in all four reference-carrying files | **Accept** | Cited at the assume–guarantee passages in all corrected editions and the monograph v1.1 |
| G09 — bare σ_i in the bottleneck diagnostic | **Accept** | M(t) = min(min σ⁻, min σ⁺) in ms_part1_corrected.md |
| G10 — Appendix G conflates Type and Status | **Accept** | Columns split in ms_part4_corrected.md |
| G11 — T′ undefined; C, V_g; symbol overloading | **Accept (T′), accept-light (renames)** | T′ and the post-reset reading defined in ms_part2_corrected.md; the remaining symbol overloads are declared rather than renamed in the archival layer (fidelity to superseded sources; the successor monograph already carries distinct notation where it matters) |
| G12 — lowercase list item 8 | **Accept** | Capitalised in the v0.2/manuscript corrected editions |
| G13 — mixed British/American orthography | **Deferred** (registered for the venue-format pass) | Both archival series are superseded; a per-file orthography normalisation of archival files has no downstream value and risks divergence from the byte-verified lineage |
| G14 — the archival layer carries the retired central conjecture unmarked | **Accept as documented** | The supersession is stated here and in README_v2.md; the archival files themselves stay as committed history in the corrected editions' headers |
| GT-01 = G01 | **Accept** | As above |
| GT-02 — Lemma 8's §7.2 pointer | **Reject** (§7.2 states the condition; verified) | ms_part3_corrected.md adds the §8.2 secondary pointer as an augmentation |
| GT-03 / A.3 — severed H_actual feedback | **Accept** | `ms_part3_corrected.md` and `general_theory_of_sustainability_manuscript_corrected.md` subtract H_actual and declare u's harvest entry as H_authorized |
| GT-04 / A.2 — symbol I triple overloading | **Accept-light** | The overloads are declared in the corrected editions' headers; the inventory/identity/inflow symbols are disambiguated at their load-bearing uses (the grievance-trigger inventory reading) without a global rename of superseded text |
| GT-05 / A.1 / F1 — the dual K/K\* decomposition | **Accept as archival** | The successor's registry resolution is cited in the corrected editions' notes; Branch A's text is otherwise committed history (the successor §6.1 resolves it verbatim) |
| GT-06 — Ω's K slot vs the K\* operator | **Accept as archival** | Documented in the corrected editions' notes |
| GT-07 = G08 | **Accept** | As above |
| GT-08 — author placeholder | **Accept** | "[Author name — to be completed at submission]" in all corrected editions |
| Qwen v0.2 #1 — ∃π dropped from the probabilistic criterion; trajectory notation | **Accept** | Restored in the v0.2/manuscript corrected editions |
| Qwen v0.2 #2 — "a system is robustly sustainable" unanchored | **Accept** | Anchored to z_0 in all three corrected editions |
| Qwen v0.2 #3 — corridor infeasibility stated absolutely | **Accept** | State- and reachability-qualified in the v0.2/manuscript corrected editions |
| Qwen v0.2 #5 — Box 13 truncated at nine steps | **Reject** (all twelve steps present) | — |
| Qwen v0.2 #6 — hypothesis/conjecture/indicator terminology drift across documents | **Accept as register note** | The mapping (H1–H8 → the ten indicators → the nine architecture-level conjectures) is a documentation-level alignment; recorded here for the register rather than rewritten into superseded files |
| A.4 — no forward pointer to the detached traceability ledger | **Accept** | Pointer added in `general_theory_of_sustainability_manuscript_corrected.md` |

---

## 3. Corrections made to the auditors' own suggestions before implementation

1. **P1-01's replacement text** (arena agent 1) assigned the threshold bands backwards ("ρ₂ ≤ r ≤ ρ₁" for the both-licensed band — empty on the interior, where ρ₁ < ρ₂). Implemented with the correct bands.
2. **P3-01's suggested fix** ("add A_g0 = 100 or A_g0 = 0") would have invented a parameter value: the A018 source registers only A_g0 > 0 with A^geo ≫ A_g0. Implemented as the source-faithful declaration.
3. **F18's suggested fix** ("add the illustrative values of δ_K, K₀, c_E in parentheses") would have fabricated a parameterisation that exists nowhere in the corpus. Implemented as a withdrawal of the unverifiable number.
4. **P2-04's premise** ("§1.2 is titled 'Thirteen mapped families'") is false — no such heading exists; the finding reduces to the enumeration gap, which is what was fixed. Arena agent 2's independent correction of the same point was adopted.
5. **W01's replacement sentence** named only M3 as improving the one-year Brier; the committed scores show M1 improves as well (0.051 vs 0.063). Both named.
6. **F05's renumbering option** was declined in favour of moving the four remarks: renumbering would have touched every downstream label, the ledger, and cross-paper references for no content gain.
7. **P3-02's rename option** was declined in favour of a local-notation declaration: the four-stock system is an A001 exact-specialization row, and renaming its state symbols would diverge from the source's registered notation (the manuscript's own house precedent — Paper 4 §7.1's declared symbol-reuse convention — supports the declaration form; where the clash is intra-formula, as F17's g, the rename was applied).
8. **Qwen's Edwards double-counting analysis** was rejected on the mathematics (§1) — but its neighbourhood contained a real defect (flat-0's T=4 certified horizon), which was verified analytically and fixed. Rejecting a finding does not close the file without checking its neighbourhood.

---

## 4. What was deliberately not changed

- **The audited current versions** (all nine manuscripts, the current monograph, the seven archival monograph files, both SPECIFICATION sheets, the protocols, the admission rows, PROOF_MANIFEST.md, and the packet's current README) — byte-identical, per the owner's instruction. The two SPECIFICATION-level echoes of corrected manuscript numbers (W03's "~14 yr" in `wave_e_edwards/SPECIFICATION.md`; the "115–206" range in `wave_e_cod/SPECIFICATION.md`) are recorded here and in the v2 editions' notes; they are internal specification sheets, and their correction belongs to the next specification-sheet edition.
- **No scored content, theorem status, CC-identifier set, ledger row count, or concordance row** changes in any v2 edition. The only corrected *number* in any scored table is the cod intervention's flat-180 T=∞ boundary (2335.4 → 2338.3), which is a convergence correction of the same computation, verified entry-by-entry against the regenerated artifact, with the verdict structure unchanged (flat caps were and remain non-candidates).
- **G13 (orthography)** and the full archival symbol renames (GT-04/G11) — deferred with justification (§2.3).
- **The `PROOF_MANIFEST.md` Part VI pins** continue to reference the current (audited) manuscripts; the v2 editions are pinned in §5 below and in `reaudit/verify_batch5_editions.py`. A manifest re-pin belongs to the next manifest edition, after the owner accepts these corrected editions.

---

## 5. Inventory of the new files (this batch)

| File | Role |
|---|---|
| `papers/paper1_general_theory/manuscript_v2.md` | Corrected edition (17 accepted findings) |
| `papers/paper2_theorem_atlas/manuscript_v2.md` | Corrected edition (13 accepted findings; four remarks relocated; one proof supplied) |
| `papers/paper3_material_ledgers/manuscript_v2.md` | Corrected edition (10 accepted findings) |
| `papers/paper4_delay_dynamics/manuscript_v2.md` | Corrected edition (11 accepted findings) |
| `papers/paper5_sampled_governance/manuscript_v2.md` | Corrected edition (8 accepted findings) |
| `wave_e_cod/manuscript/wave_E_cod_forecast_ladder_v2.md` | Corrected edition (10 accepted findings) |
| `wave_e_cod/manuscript/wave_E_cod_intervention_v2.md` | Corrected edition (6 accepted findings + the convergence correction) |
| `wave_e_edwards/manuscript/wave_E_edwards_forecast_ladder_v2.md` | Corrected edition (4 accepted findings) |
| `wave_e_edwards/manuscript/wave_E_edwards_intervention_v2.md` | Corrected edition (9 accepted findings + Abstract/References supplied) |
| `revised_sustainability_manuscript_v1.1.md` | Monograph working preprint v1.1 (G01, G07, G08) |
| `ms_part1_corrected.md` … `ms_part4_corrected.md` | Archival corrected editions (G02–G12, GT-02 augmentation, GT-03, qwen's v0.2-family fixes where they apply) |
| `general_theory_of_sustainability_v0.1_corrected.md`, `general_theory_of_sustainability_v0.2_comprehensive_corrected.md`, `general_theory_of_sustainability_manuscript_corrected.md` | Flagship-chain corrected editions (qwen #1–#3, GT-03, A.4, G08, G12) |
| `wave_e_cod/src/run_intervention_v2.py` + `wave_e_cod/results/intervention_results_v2.json` + `intervention_boundaries_v2.csv` | Convergence-corrected runner and regenerated artifacts (one-entry diff, machine-verified) |
| `wave_e_edwards/src/run_intervention_v2.py` + `wave_e_edwards/results/intervention_results_v2.json` + `intervention_boundaries_v2.csv` | Comparator-corrected runner; regenerated artifacts value-identical (inertness proof) |
| `wave_e_edwards/manuscript/fig4_pass2.png`, `fig5_fibre.png` | Byte-identical renamed copies of the committed figures (hash-pinned below) |
| `external_review_packet/README_v2.md` | Packet edition fixing G05 and inventorying the batch-5 editions |
| `reaudit/verify_batch5_editions.py` | Machine verification of the corrections (pinned hashes and content checks) |
| `BATCH5_JOINT_AUDIT_EVALUATION.md` | This document |

**Verification:** `reaudit/verify_batch5_editions.py` pins the SHA-256 of every new file above and checks the corrected invariants (the restored FAST/SLOW direction; the completed concordance accounting; the Ω_xte Brier values against the committed CSV; the 2338.3 boundary against the v2 JSON; the absence of `[cite:]` placeholders; the forbidden internal-audit vocabulary at zero across all v2 manuscripts while the mathematical gate vocabulary remains in place; the monograph v1.1 formula repair; the archival CR-byte repair; the remark-order monotonicity; and the figure-file hash equality). The repository's standing battery passes on the edited tree at its documented baseline (the audited files are unchanged; the new files are additive).

**Bottom line.** The four auditors' 90+ findings decompose into: one HIGH mathematical-content contradiction in Paper 4 (fold vs multiplier — fixed with the source's dropped caveat and a branch-resolved statement), one HIGH results-paragraph error in the cod forecast paper (specification-mixing with a false conclusion — fixed against the committed artifacts), one HIGH typesetting corruption propagated into the current citable monograph (fixed at byte level), one code-level convergence defect (fixed and re-verified), one latent comparator defect (fixed and re-verified inert), a large set of confirmable presentational/count/citation defects (all fixed in the v2 editions), four rejected findings (qwen's double-counting claim, qwen's Box-13 truncation, arena agent 1's Lemma-8 pointer, arena agent 1's "thirteen families" premise — each rejection argued from the committed artifacts), and two defects found by this evaluation that no auditor had isolated (flat-0's T=4 certified horizon; the tether threshold's unverifiable number). No scored verdict, retention decision, theorem status, or ledger count changes anywhere.
