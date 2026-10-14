# Paper 01 — Obstruction calculus: v72 → v73

**Scope of the edition.** v73 is a research-article rewrite of v72. No theorem was weakened, no hypothesis was dropped, and no numerical value changed; every v72 result is present (concordance: Supplementary Table S1.1). What changed is the organisation, the argument structure, the writing, and the division between main text and supplement.

## Version check
Latest Paper01 across **all branches** of `MIKEAA2020/general-sustainability` was v72 (`e2-v3-source-year`, `arena agent 1/agent workspace/paper 2 family/01_obstruction/`); v73 is therefore the next free number.

## Main text (28 pp, single column, A4)
| | v72 | v73 |
|---|---|---|
| Structure | 11 numbered subsections in one long section; results numbered globally (Thm 1–8, Prop 1–11) | 9 sections; one shared counter per section (Thm 4.1, Prop 5.2, …); hypothesis labels (C1)–(C3), (D1)–(D3), (E1)–(E2) |
| Organising idea | implicit | stated once (§1 "organising idea", §2 Prop 2.2 selector principle): every certificate proves a response correspondence empty |
| Standing conventions | scattered through §2.3 | consolidated as (Fail)(Hold)(Record)(Order) in §2 and referenced by name |
| Finite systems | §3.1 inside the calculus | own §3, with the Lean scope stated once |
| Certification limits | §4 | own §5 (Def 5.1, Prop 5.2, Cor 5.3, Prop 5.4 — the certainty-equivalence trap promoted from a remark to a proposition, statement unchanged) |
| Completeness | §7 after discussion | own §6 before the case study; static theorem sharpened to say explicitly that the Nagumo test is sufficient for invariance, not necessary for viability from a subset |
| Case study | §9 | §7, coverage table now shows all 48 cells; two-patch table kept; calibration paragraph kept |
| Discussion | §5, §6, §8, §10 | one §8: certificate ↔ emptied correspondence ↔ **design remedy** table (new remedy column); barrier/tube/HJ positioning; probabilistic pointer; monitoring consequences; limitations |
| Sufficiency landscape, probabilistic §10, selector §8, worked §3.8 LP | main text | moved to Supplement S5, S4, S2.1, S3.2 |
| Lean details | §3.9 (2 pp) | one paragraph in §3 + Supplement S7 (declaration table, provenance, scope limits) |
| Figures | 7 | 5 in main (2 new: diagnostic flowchart Fig 1, recourse-threshold plot Fig 4; 2 revised: coverage, ladder) + 4 in SI |
| References | plain list, no citations in text | natbib author–year citations throughout; Helly (1923) and Nagumo (1942) added |

## Supplementary Material (23 pp)
S1 conventions + concordance; S2 complete proofs (selector + phantom-value witness; trees; common action/Farkas/ladder/Helly; emptiness; delayed + relation to common action; LP + class gap; exit/comparison/recourse incl. the control-affine counterexample ẋ = −1 + xu; certification; completeness); S3 worked certificates (Farkas robustness = Lean `farkas_perturbed`; aggregate LP Y* = 27/5; hold-class survival; three-branch τ* = 7/50 with the pair controls; one system three methods); S4 probabilistic counterpart (v72 Thm 8, Props 10–11 unchanged + hold-class table); S5 sufficiency landscape; S6 constructions A.1–A.3; S7 Lean table + verification record V1–V12; S8 figures; S9 result map.

## Verification
`paper01_v73_verification.py` — 30 exact-arithmetic checks (V1–V12), all PASS; covers every number in the paper and runs the exact recursion on every finite instance (coverage grid 48 = 30+12+6, two-patch fibres, four-state instance/variant, hidden-mode belief). The Lean file is unchanged from v72 (33 theorems / 25 definitions, no `sorry`); no fresh Lean rebuild is claimed.

## Corrections carried from the v72 audit notes (all preserved)
Recourse proposition restricted to affine state/input with state-independent input coefficient (control-affine version unsound); coverage audit is hold-class only; deterministic-kernel limit needs point-mass transitions and observations; the decaying LP example and the hold-gap example are different models; Helly proof uses affinity of the tangent inequality in u, not convexity of q; necessity of R^B_V needs the original-path premise (phantom-value witness D(0) = {−1,1}); Lean covers the discrete core only; estimation-tube reduction exact only under matching hypotheses; static-observation theorem: Nagumo test sufficient, not necessary; no uniform tube margin (ladder label "declared hold class").
