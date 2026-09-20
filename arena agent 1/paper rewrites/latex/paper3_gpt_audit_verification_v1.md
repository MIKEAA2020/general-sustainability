# Paper 3 — GPT novelty-audit verification report (2026-09-20)

Every checkable claim in the GPT EMS novelty audit was re-verified against
the actual artifacts (v4 source, package source, search records, rendered
PDF) before any change was made. Fixes shipped as **v5** (new files; v1–v4
preserved) and package **1.2.0**. The audit's strongest upgrade option — a
certificate-carrying assessment with an independent checker — is the core of
this release.

## Claims REFUTED (no defect; no change made)

| Claim | Verdict | Evidence |
| --- | --- | --- |
| **Wording fix list:** §4.2 contains the typo "forsustainability" | **Refuted — not present.** `grep -c "forsustainability"` over the v4 source returns 0; the PDF text layer has no such string. The audit likely mis-copied a line-broken word from a rendered page. | v4.tex full-text grep; v4 PDF text layer |

## Claims VERIFIED and IMPLEMENTED (v5 / package 1.2.0)

| Claim | Verdict | Implementation |
| --- | --- | --- |
| **Gap 1 — certificate protocol:** certificates exist only inside the library; no serialization format, no independent checker, no negative tests; "certificate-carrying assessment" named the strongest upgrade | **Verified** | Package 1.2.0: `FarkasCertificate.to_dict()/from_dict()` (JSON, exact rationals as strings, `"type": "farkas"`); repository-root `check_safe_transition_cert.py` — a standalone, stdlib-only verifier sharing **no code** with the package, which re-derives every verdict from the certificate's own contents; negative tests assert rejection of altered bounds, altered multipliers, and altered systems. `safetransition certify` emits the certificates; `run_all.sh` step 3/6 exercises produce → independent-check → tamper-reject. |
| **Gap 2 — tube certification semantics:** exact tubes vs conservative enclosures conflated in one word | **Verified** | Package 1.2.0: `TubeStatus` enum (`EXACT`/`CONSERVATIVE`) in `datum.py`; `tube_certificate()` marks the declared piecewise-linear plan tubes EXACT and the Schaefer realization CONSERVATIVE, carrying the derivation (monotonicity of σ on the visited biomass interval [6/5, 16/5] ⊂ (0, K/2), σ ≥ 528/125 ≥ 4 on the recovery legs). v5 §4.1 states the two statuses explicitly ("supplied exact or certified conservative tubes" in the abstract). |
| **Gap 3 — weight-space analysis is pointwise:** paper reports only ρ₁ = 2/3, ρ₂ = 3/2, no complete partition, no per-dip family | **Verified** | Package 1.2.0: `weight_partition()` returns the complete arrangement of licensed plan sets along r = w₂/w₁ as a serializable certificate, generic in the dip: benchmark regime (dip < s₁+s₂; three regions), swapped regime (dip > s₁+s₂; thresholds swap, unlicensed gap around r = 1), degenerate regime (dip = s₁+s₂; single-point middle region); per-dip thresholds follow the closed family (dip − s₁)/s₂, s₁/(dip − s₂); `licensing_thresholds` exposes the dip parameter. v5 §4.3 adds the partition paragraph with all three regimes; the independent checker re-derives thresholds, tiling, inclusivity, licensed sets at sampled ratios, and boundary witnesses. |
| **Gap 4 — minimality of obstruction certificates undefined** | **Verified as already satisfied but undocumented** | The implementation searches conflicting subfamilies in nondecreasing cardinality by exhaustive check, so every reported conflict is minimum-cardinality and every strictly smaller subfamily is certified to intersect. Package 1.2.0 documents this in `certificates.py`; the paper's §2.3 statement ("a minimal conflicting subfamily") is now backed by a stated definition. |
| **Gap 7 — belief policy/counterexample:** non-viability reported without a witness | **Verified** | Package 1.2.0: `explain_belief_failure()` returns the per-action counterexample object (violation en route with the offending fibre states, or the post-belief not viable at the previous level); demonstrated on the recourse-failure system (both actions fail with post-belief {y12, y4} not 1-step viable). v5 §2.2 and §4.3 document it. |
| **Gap 8 — "all computations" precision overstatement risk:** figure pipeline uses floats | **Verified as already fixed in v4** ("floating point appears only in rendered graphics"); audit asked for the stronger discipline statement | Package 1.2.0 adds import-graph hygiene tests (core modules must not import matplotlib/PIL/numpy) and a test running the full benchmark with the figure stack import-blocked; float inputs are structurally rejected (`frac` raises on `float`). |
| **Gap 10 — adversarial float instance:** audit asked for a concrete exact-vs-float verdict flip | **Verified and supplied** | n = 49: 49·(1/49) − 1 = 0 exactly (floor exactly met → licensed), but −1.1102230246251565 × 10⁻¹⁶ in binary floating point (falsely unlicensed). 7·(1/7) is **not** an instance (IEEE rounds to exactly 1.0). Test `test_adversarial_verdict_flip` + `test_adversarial_flip_on_library_admissibility` assert the flip on the library's own admissibility predicate; v5 §3.2 reports it; QA table row added. |
| **§5 comparison demand:** named tools compared from memory rather than by citation; "none returns certificates" too broad | **Verified** | v5 §5 adds a verified-citation comparison set — z3 (de Moura & Bjørner 2008, DOI 10.1007/978-3-540-78800-3_24, TACAS 2008, pp. 337–340), PRISM 4.0 (Kwiatkowska, Norman & Parker 2011, DOI 10.1007/978-3-642-22110-1_47, CAV 2011, LNCS 6806, pp. 585–591), pyfme (Caron 2022, github.com/stephane-caron/pyfme; SymPy-rationals Fourier–Motzkin with Imbert acceleration, no provenance/certificates) — plus a five-property comparison table (Table 3). Both DOIs re-verified by content negotiation at revision time. The claim is scoped: *environmental* families return no certificates; general-purpose provers do, but ship no assessment semantics. |
| **Novelty-search records in main text** (audit: gap claims must point at preserved evidence) | **Verified** | v5 §1 and §5 reference the twelve verbatim search queries (q1–q12, dated result records) archived in the verification deposit (figshare DOI 10.6084/m9.figshare.33764023, `pkg/novelty_searches/`). |
| **"What is missing" too sweeping** | **Verified** | v5 §1 narrows the gap statement: SMT solvers certify general constraint systems in their own semantics; what is missing is a layer whose verdicts carry the assessment semantics (floors, weights, licensed plan sets, partially observed beliefs). |
| **Nine-modules counting; 4,096 bound wording; conservatism phrasing; conclusion softening; FM "as any exact general method is"** | **Verified** | v5: architecture says "nine modules plus the repository-root independent checker"; module table adds the checker row and tube/benchmark certificate contents; belief bound is "a parameter (default 4 096) whose exhaustion raises … no partial results; affects exploration completeness, never soundness"; tubes are "supplied exact or certified conservative"; FM cost "as exact elimination inherently is"; conclusion scoped to "addresses a practical gap … wherever verdicts must be re-derivable". |
| **Chain scope conditions** (audit: subset chain stated without hypotheses) | **Verified** | v5 §2.1: chain holds "for every weight in the positive weight cone and for menus whose plans share a common disturbance set — the standing scope conditions of the operator framework". |

## Claims NOTED, no change required

- **Gap 5/6 scope reminders** (classification ≠ policy; fibre criterion decides
  exact observation-only certifiers): both already stated in v4 §2; v5 keeps
  them.
- **Larger parameterized benchmark:** partially implemented — the weight
  partition is now generic across the rational floor/dip family and the test
  suite sweeps five (s, dip) combinations through the independent checker; a
  full scaling study remains future work (stated in §6).
- **Package version in the paper:** v5 pins SafeTransition **1.2.0**
  (module table caption, QA table caption, availability table).

## Post-fix QA

v5: compile exit 0; 10 pp; 0 `??`; overfull baseline (2.43 pt) only; abstract
144 words (≤ 150); figshare DOI occurs exactly once; z3/PRISM/pyfme citations
carry verified DOIs; Table 3 and the QA table render without overflow.
Package 1.2.0: 39/39 tests; `run_all.sh` 6/6 steps pass; SHA256SUMS 43
entries; independent checker 3/3 over emitted certificates and rejects all
tampered variants.
