# Joint audit — verification verdicts and disposition (v1)

**Scope.** One joint verification round over the three external-audit
streams, conducted against **paper 3 v6** (`paper3_safetransition_ems_v6.tex`)
and **package 1.2.1**, per the discipline: every claim re-verified against
the actual artifacts (source lines, rendered PDF pages, committed JSON,
figure pixels) before any verdict; refuted claims are documented, never
silently "fixed"; verified fixes ship as new versions — never edits to
shipped files.

**Streams.**

- **S-A** — GPT EMS flaw list: 60 numbered findings plus a consolidated
  26-item priority list (`gpt ems flaws and upgrades.txt`, lines 11–1569).
- **S-B** — deepseek executive assessment: 40 mirrored findings
  (same file, lines 1570–2218). Verdicts are shared with the
  corresponding S-A item; divergences noted.
- **S-C** — revision plan (same file, lines 2220–end): governing
  principle, claim-closure matrix, semantic refactors §3, certificate
  framework §4, ready-to-adapt statements §5, architecture §6, scaling
  §7, benchmark §8, partial-observation §9, related work §10,
  availability §11, section plan §12, enhancements 13.1–13.6, wording
  14.1–14.9, DoD §15, priorities §16.

**Ship vehicles.** Package **1.3.0** (`SafeTransition_v1.3.0.zip`; 58/58
tests; run_all 7/7; SHA256SUMS 55 entries), paper **v7**
(`paper3_safetransition_ems_v7.tex`/`.pdf`, 15 pp.), supplementary
**v4** (`paper3_supplementary_v4.md`, S1–S11), highlights **v7**.

---

## 1. Refuted claims (verified against artifacts; no change made)

| # | Claim (stream) | Verification performed | Verdict |
| --- | --- | --- | --- |
| 1 | Title contains "forsustainability" spacing error; author line garbled (S-A #37) | PyMuPDF render + text extraction of v6 PDF p.1 at 100 dpi: title renders cleanly as "SafeTransition: exact rational certification of transition safety for sustainability assessment"; author/affiliation block renders correctly | **REFUTED** — raw-text-extraction artifact; no spacing error exists in the rendered PDF |
| 2 | References and dates are future-dated / impossible (S-A #38) | Today = 2026-09-20 (session date); all citations carry 2026-or-earlier years; availability year 2026 correct | **REFUTED** — "future-dating" premise false at verification time |

## 2. Confirmed and fixed — package 1.3.0

| # | Finding (stream) | Verification | Fix shipped in 1.3.0 |
| --- | --- | --- | --- |
| 1 | Belief successor described as label set — information loss (S-A §1, S-B 1) | `recursion.py` source read: beliefs update to labels; fibres re-expanded at each step | `belief_backward` docstring rewritten to quotient semantics: beliefs are elements of the state-space quotient under the observation map; fibres re-expanded at every step |
| 2 | "Sound and complete in finite systems" contradicts §2.2's injectivity condition (S-A §1, S-B 1) | v6 l.89 vs l.190–192 read; both statements present verbatim | Package docstrings split soundness (general, finite) from completeness (conditional); paper v7 intro + §2.2 scoped accordingly |
| 3 | Injective observations make the problem trivial; completeness should not require it (S-A §1, S-B 1) | Recursion keeps state fibres internally; injectivity is only the simplest sufficient condition | Completeness condition generalized to the **safety-and-action quotient** (membership and admissibility constant on fibres, successors label-determined); injectivity stated as simplest sufficient case |
| 4 | Index-blindness alarm misses boundary: strict `>` skips zero-margin licensed plans (S-A §12, S-C 8.4) | `indicators.py` read; boundary case constructed: composite min exactly 0 with negative floor min → old code silent | Alarm fires on `min(idx) >= 0` (operator-licensed) with negative floor minimum; property battery covers the boundary |
| 5 | `weight_partition` scope undefined; silent misinterpretation outside family (S-A §11, S-C 3.5) | `weight_partition` source read: thresholds `(dip−s1)/s2`, `s1/(dip−s2)` only meaningful for `0 < s1, s2 < dip` | Scope docstring (two-floor witness family, affine-in-r trough conditions, admissible parameter family) + `ValueError` guard before threshold computation; ratio domain (0, ∞) with 0/∞ as projective closures in the certificate |
| 6 | Failure explanations not serializable/independently checkable (S-A §41, S-C 9.2) | `explain_belief_failure` returned a plain dict; checker had no belief type | `failure_certificate` serializer (system, horizon, per-action reason codes) + checker type `belief_failure` re-running the recursion from the serialized system through a stdlib-only reimplementation; tampered reasons/post-beliefs rejected (tests) |
| 7 | No property-based or degenerate test battery (S-C 13.3/13.5, S-A #49) | v1.2.1 suite: 46 tests, all fixed instances | `tests/test_property_and_degenerate.py`: 12 tests — seeded random chain inclusion (60), Farkas validity vs independent exact vertex-enumeration oracle (60, full-rank gated), belief monotonicity, partition coverage incl. STAGED-licensed-when-financed, canonical-JSON cross-process `PYTHONHASHSEED` stability, 30-case tamper fuzz, degenerate systems (zero/duplicate rows, coincident thresholds ρ₁=ρ₂, licensed-everywhere plans, empty menus). Suite 58/58 |
| 8 | Scaling study lacked platform metadata and bit-length separation (S-A §26, §21; S-C 7.3/7.6) | `scaling_results.json` v1.2.1 had no meta; bit metric conflated numerator/denominator | Study records CPU, OS, Python, methodology; `margin_num_bits`/`margin_den_bits` separate on chain and dyadic rows; full study re-run (73.6 s) and committed |
| 9 | No row-growth stress family; scalability language unbounded (S-A §24; S-C 7.5) | Dense random systems (3t rows, t vars, entries ∪[−5,5]/[1,3]) probed: t=3 → 975 rows; t=4 infeasible → 7,505 rows/2.2 s; t=4 feasible → >60 s | `family_stress_dense` added with SIGALRM 60 s budget; the recorded impracticality point (t=4 feasible) is the output; claims scoped to structured planted families |
| 10 | Dashboard provenance embedded the checker version as "vunknown" (found during 1.3.0 test hardening) | `default_provenance` resolved the checker path one directory short | Path fixed; checker version 1.0.0 embedded; shipped `dashboard.html` regenerated with the provenance table; test made version-agnostic and asserts no "vunknown" |
| 11 | Latent crash: `step_ok(B, a) is None` where `step_ok` returns a list (found during 1.3.0 line-level re-read) | `recursion.py` l.121 read | Fixed with an explicit membership/skip; suite passes |

## 3. Confirmed and fixed — paper v7

Mathematics and semantics:

| # | Finding (stream) | v7 fix (section) |
| --- | --- | --- |
| 1 | Tube story self-contradictory: "exact … no outer approximation enters" vs certified conservative Schaefer tubes (S-A §2, §30, S-B 2, S-C 3.1) | §2.1: finite action-indexed disturbance set; tube statuses `EXACT`/`CONSERVATIVE` defined; one-sided verdict semantics + verdict-semantics table (Table 3; S-C 13.2); §4.1 three-layer split (datum exactness / enclosure vs Schaefer / scientific validity) |
| 2 | Operators under-specified; inclusion chain unjustified (S-A §6, S-B 3, S-C 3.3) | §2.1: all five operators formalized over shared scope (common disturbances, reset, destination; w > 0); typed/physical sets defined; each inclusion's reason stated (possibly strict); V_weak quantifier order (∀w∃a vs ∃a∀w) explicit (S-C 5.3) |
| 3 | Endpoint ambiguity with reset (S-A §7, S-C 5.2) | §2.1: tube constraints on the visited path; endpoint constraints at terminal pre-reset y⁻; destination at post-reset z⁺ = R(y⁻) |
| 4 | Fibre criterion overclaimed (S-A §3, S-B 6, S-C 5.6/14.4) | §2.3/§4.3: renamed **observation-only safety-classification criterion**; narrowed to current-observation classification; explicit non-claims (history policies, belief-based control, conservative certifiers, three-valued procedures) |
| 5 | Obstruction "pairwise-compatible" undefined (S-A §4, S-B 7, S-C §3) | §2.3: co-possibility (mutual possibility under the assessed observation) defined; horizon semantics of the ruled-out claim (immediate-safe vs recursively viable) |
| 6 | "Minimal conflicting subfamily" undefined (S-A §5, S-B 8, S-C 14.5) | §2.3: minimum-cardinality by exhaustive search in nondecreasing size; every strictly smaller subfamily certified to intersect (matches implementation) |
| 7 | FM complexity sentence false ("exponential … as exact elimination inherently is") (S-A §19, S-B §4-region, S-C 5.5) | §3.3: FM can generate exponentially many intermediate inequalities; exact rational LP is polynomial in the bit model; FM chosen for small systems + row-level provenance |
| 8 | §3.4 empty (S-A #20) | Scaling prose + Table 2 moved under the heading |
| 9 | L undefined; denominator-bit claims inconsistent (S-A §21, S-C 7.3) | L = 5 defined (dyadic chain links); measured margin 2⁻³²⁰/7 → reduced denominator 7·2³²⁰ = **323 bits** (numerator 1 bit); abstract's "321-bit denominators" corrected to "reduced denominators reach 323 bits" |
| 10 | Two margin formulas without family labels (S-A §22, S-C 7.4) | Family-named closed forms: chain (1/5 − (k−1)/4096)/(k+1) at every k; dyadic 2⁻ᵗ/7 |
| 11 | Belief scaling row contradicts sweep (m=10 vs bound) (S-A §23, S-C 7.2) | Table 2: largest completed m = 12 (4,096 beliefs); overflow test m = 13 raises, no partial results |
| 12 | Broad scalability language from easy families (S-A §24, S-C 7.5) | Claims scoped to structured planted-answer families; dense stress family with recorded envelope added |
| 13 | "Coefficient growth inflates certificate size, not verdict times" (S-A §25, S-C 14.8) | "Within the tested range, coefficient growth had a larger observed effect on certificate size than on wall-clock time" |
| 14 | Performance reporting lacks reproducibility detail (S-A §26, S-C 7.6) | Table 2 caption: single run, no warm-up, wall-clock, Xeon 2.60 GHz, Linux x86-64, CPython 3.13, checker times incl. subprocess startup, tracemalloc overhead caveat; availability table carries the same platform row |
| 15 | "All computations" too broad (S-A §27, S-C 14.1) | "All semantic computations — assessment, recursion, threshold, and certificate arithmetic —"; floats confined to rendering and performance measurement |
| 16 | Float adversarial example over-general (S-A §29, S-C §6.3-region) | Scoped: regression case for one direct IEEE-754 binary64 evaluation path in the tested order with exact-zero threshold; not a general anti-float claim |
| 17 | Monotonicity enclosure not reproducible (S-A §31, S-C 8.2) | §4.1: σ′(B) = 4 − 4B/5 > 0 on visited [6/5, 16/5] ⊂ (0,5); σ increasing; min σ(6/5) = 528/125 = 4.224 ≥ 4 |
| 18 | Conservative tubes need one-sided rejection semantics (S-A §32, S-C 8.3) | §4.1: rejected-on-enclosure = not-certified-safe unless violating point reachable; benchmark separation rests on declared exact tubes (both directions conclusive) |
| 19 | "Characteristic disturbance" disconnects dashboard from robust verdicts (S-A §33, S-C 3.4) | §4.2: dashboard branch labeled illustrative; robust operator verdicts quantify over all disturbances |
| 20 | §4.2 wrong cross-ref; phase flag unexplained (S-A §36, §24-list) | Cross-ref → sec:operators; q-suppression note (fixed at review phase) |
| 21 | Recourse example unspecified (S-A §39, S-C §12) | Table 4: full three-state system (states, observations, actions, successors) matching the package demo exactly |
| 22 | "Admissible in isolation" ambiguous (S-A #40, S-C 9.1) | Defined: state-wise, one-step, full-information sense (§2.2, §4.3) |
| 23 | "No ratio licenses a typed-safe plan" conceptually awkward (S-A §56, S-C 14.9) | Reworded in caption + figure labels: neither plan typed-safe at the witness; at least one plan aggregate-licensed at every admissible ratio |
| 24 | Module count "nine" vs ten rows (S-A §34, §35) | §3.1/Table 1: nine modules + CLI entry point + standalone checker; `benchmarks/` annotated "(directory, not a module)"; line counts updated with method (`wc -l`: 1,698/951/375/386) |
| 25 | Dashboard "verification arrives together" conflates integrity with trust (S-A §57) | §4.2: hashes establish integrity/identity of serialized inputs, not authenticity or external truth |
| 26 | Pooled-kernel identity abrupt (S-A §58) | Pointer to new Supplementary S11 (system, normals, weights, identities, regression-anchor role) |
| 27 | Line counts without method (S-A §60) | `wc -l` stated (§3.1, §6) |
| 28 | V_weak notation unexplained (S-A #55) | Quantifier-order explanation (§2.1) |
| 29 | Three-regime formulas without assumptions (S-A §10, S-B §12-region, S-C §6) | §4.3: admissible family 0 < s1, s2 < dip; degenerate cases (threshold swap, unlicensed gap, single-point middle region); outside the family the routine raises |
| 30 | Weight domain vs positive cone (S-A §9, S-B §13-region, S-C 3.5) | §4.3: one convention throughout; ratio domain (0, ∞) with 0/∞ as projective limit closures in the certificate; guard uses 0 < s < dip |
| 31 | weight_partition scope in paper (S-A §11) | §3.3: two-floor witness-family menu class, affine-in-r trough conditions, admissible parameter family, ValueError outside |
| 32 | Index-blindness alarm boundary in paper (S-A §12) | §4.2: fires on composite minimum nonnegative (boundary included) with negative floor minimum |
| 33 | Infeasibility margin representation-dependent (S-A §13) | §2.3: "normalized certificate contradiction value"; invariant to λ-rescaling (Σλ = 1 fixed), not to input-row rescaling |
| 34 | Checker proves algebraic, not semantic, validity (S-A §14, S-C 4.3) | Kept as designed contract, documented (§4.2, S9), and encoded as a passing boundary test: a tampered-system certificate verifies for the tampered system |
| 35 | Checker certificate types unclear (S-A §15) | §4.2 + S9 support matrix; belief_failure type added |
| 36 | Feasibility certificates mentioned, not specified (S-A §16) | §2.3/§3.3: feasible systems return a bare verdict — feasibility decided, not witnessed |
| 37 | "Sharing no code" too absolute (S-A §17) | "standalone checker importing no library modules" (abstract, §2.3); stdlib-only stated |
| 38 | Canonical JSON unspecified (S-A §18, S-C 6.4) | S9: sorted keys, tight separators, "num/den" strings, no timestamps; cross-process PYTHONHASHSEED stability test |
| 39 | Disturbance semantics inconsistent (S-A §8, S-B 5, S-C 3.4) | §2.1: one finite action-indexed disturbance set everywhere; §4.2 labels the dashboard branch illustrative |
| 40 | "Exact reachability" to be avoided (S-A §51) | Tubes are "the exact visited set of declared piecewise-linear paths" with declared status — no reachability claim beyond the declaration |
| 41 | Breakpoint-extremes clause insufficient (S-A §52) | Noted: describes the declared path interface; tubes are verified relative to the declaration (status language), not against external general constraints |
| 42 | "Polynomial" needs a size model (S-A §54) | §2.2: unit-cost predicate model; bit complexity reported separately by the study |
| 43 | Disturbance set must be finite (S-A §53) | §2.1: "finite action-indexed disturbance set" |

Related work and artifacts:

| # | Finding (stream) | v7 fix |
| --- | --- | --- |
| 29 | Raven/FloPy conflated with viability kernels (S-A §42, S-C 10.1) | §5: simulator family repositioned (nearest workflow neighbours, scenario consumers); absence claim scoped to the surveyed viability/reachability side |
| 30 | z3 claims too loose (S-A §43, S-C 10.2) | §5: default cores are trace proofs of z3's own rules, not self-contained algebraic witnesses; Farkas certificate verifiable by school arithmetic |
| 31 | PRISM claims need qualification (S-A §44, S-C 10.3) | §5: returns counterexamples and witnesses; floating-point scale for numerical queries; comparison-table row qualified |
| 32 | Universal absence claim too broad (S-A §45, S-C 10.4) | Scoped to the packages surveyed in the archived novelty search |
| 33 | Deposit identity/URLs missing (S-A §47, §48, S-C §11) | §5/§6: figshare DOI 10.6084/m9.figshare.33764023 + github.com/MIKEAA2020/general-sustainability |
| 34 | Test counts don't establish reliability (S-A §49, S-C 13.3-region) | §6: battery described factually; "no continuous integration service is claimed" |
| 35 | Delegation to unpublished companions (S-A §50) | Operators, recursion semantics, and justifications now self-contained at statement/sketch level (§2); theorem-level proofs remain in the companions by design |

## 4. Confirmed and fixed — supplementary v4

- S1: tube statuses, finite disturbances, endpoint/reset conventions,
  operator scope, chain justification, quantifier order (aligns v7 §2.1).
- S2: quotient semantics; sound/complete split; failure-certificate
  serialization; Table 4 pointer.
- S3: normalized certificate contradiction value (row-rescaling caveat);
  feasibility decided-not-witnessed; co-possibility;
  minimum-cardinality subfamily; criterion narrowing.
- S5: 1.3.0 tree (58 tests, 9 test files, 1,698 src lines); figure
  pipeline description corrected (`make_safetransition_figs.py`,
  `make_certificate_chain.py`).
- S9: `belief_failure` checker row; trust-boundary statement; negative
  tests (belief tamper, 30-case fuzz, algebra-vs-semantics boundary
  test); one-sided tube semantics; adversarial instance scoped;
  property battery described.
- S10: rewritten for 1.3.0 — six families; separated bit metrics;
  measured dyadic numbers (2⁻³²⁰/7, 323 bits); stress family incl.
  impracticality point; platform/methodology; 58 tests.
- **S11 (new):** pooled-kernel regression anchor — normals
  (1,0), (−3/5,4/5), (−3/5,−4/5); λ = (3/8, 5/16, 5/16); Σλ = 1;
  Σλⱼnⱼ = (0,0) exactly; barycentric reading; cross-paper anchor role.

## 5. Revision-plan compliance (stream S-C)

**Priorities §16 (essential 1–10):** all ten addressed — belief update
(1.3.0 + v7 §2.2); completeness contradiction (v7); tube statuses (v7 +
docstrings); FM complexity (v7 §3.3); weight domain (guard + §4.3);
three-regime assumptions (v7 + guard); minimal subfamily (v7 §2.3);
disturbance quantification (v7 §2.1 + §4.2 label); checker scope
(README trust boundary + S9); L and bit claims (v7, measured values).

**Wording 14.1–14.9:** all nine replaced in v7 (exactness, tube,
belief completeness, fibre criterion, minimal subfamily, checker
independence, scaling claim, coefficient growth, ratio phrasing).

**Enhancements 13.1–13.6:**

| Item | Status |
| --- | --- |
| 13.1 certificate-chain figure | **Done** — `fig_certificate_chain.png` (Fig. 2 in v7), deterministic script, provenance-block arrow target |
| 13.2 verdict-semantics table | **Done** — Table 3 in v7 §2.1 |
| 13.3 property-based tests | **Done** — 12-test battery, suite 58/58 |
| 13.4 optional external-solver cross-check | **Declined, with reason** — a third-party solver would break the stdlib-only trust boundary; the property battery instead cross-checks Farkas validity against an independent exact vertex-enumeration oracle (60 instances) written for this suite |
| 13.5 degenerate-case tests | **Done** — zero/duplicate rows, coincident thresholds, licensed-everywhere plans, empty menus |
| 13.6 limitations subsection | **Done** — §7.1 "Limitations" (datum relativity; conditional completeness; narrow dense envelope; partition family scope) |

**DoD §15:** satisfied — semantic refactors (tube statuses, belief
quotient, operators, disturbance semantics, weight domain) shipped;
certificate framework (classes, support matrix in S9, TCB figure)
shipped; §5 statements adapted where consistent with package ground
truth (margin wording uses the **measured** 323-bit value, not the
audit's suggested 2³²⁰/321-bit figures — see §7 below); scaling repairs
7.1–7.6 shipped; benchmark repairs 8.1–8.4 shipped; partial-observation
repairs 9.1–9.2 shipped; related work 10.1–10.4 shipped; availability
11.1–11.2 shipped (release zip + deposit-role separation maintained);
enhancements and wording as above.

**Novelty-search handling (S-A #46):** noted. The paper claims a
functional comparison backed by preserved verbatim-trimmed records
(deposited, q1–q12 with dates), not a systematic literature review; v7
keeps this framing and scopes the absence claim accordingly. A
full technical literature review remains out of scope for a software
description.

## 6. Verification-method notes

- Every tex-side fix was anchored against the **actual v6 file text**
  (exact-string or regex with match-count assertion), then compiled
  (Tectonic 0.15.0) and QA-rendered with PyMuPDF at 100 dpi (title
  page, operator definitions, scaling table, chain-figure/recourse
  page).
- Every package-side fix was followed by the full suite (58/58) and,
  at release, `run_all.sh` 7/7 (tests, 24/24 benchmark checks, 3/3
  certificates verified, worked examples incl. recourse failure and
  pooled kernel, quick scaling, adversarial demo, figure regeneration).
- Numbers shipped in v7/v4 are the **measured** package values from the
  regenerated `benchmarks/scaling_results.json` (73.6 s full run),
  never the audit's arithmetic.

## 7. Where the audits themselves erred (measured corrections)

| Audit claim | Measured ground truth |
| --- | --- |
| "margin 2⁻³²⁰ → denominators 2³²⁰, 321 bits" (S-C 7.3) | Margin = 2⁻³²⁰/7 → reduced denominator 7·2³²⁰ → **323 bits** (L = 5) |
| Title typo "forsustainability" | Rendering artifact; PDF clean |
| Future-dating | False at 2026-09-20 |

## 8. Residual notes (accepted limitations, no action)

- Bit-complexity growth of the typed recursion is reported
  empirically (S10) rather than bounded analytically; an analytic
  bound would require a coefficient-growth model outside the paper's
  scope.
- The weight partition remains specific to its stated menu family;
  other families need new derivations, not reparameterization.
- The checker validates against supplied data; datum validity (layer 3
  of §4.1) is and remains outside any software's reach.

*Report closes the joint-audit round: 2 refuted, 60 confirmed-and-fixed
across package 1.3.0 / paper v7 / supplementary v4 / highlights v7,
1 declined-with-reason (13.4), residual notes recorded. Next vehicles:
figshare new version of DOI 10.6084/m9.figshare.33764023; GitHub push.*
