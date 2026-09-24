# Round-4 audit adjudication — computational certification, edition 5

**Input.** `uploads/computational elevation audit.txt` (981 lines): the grok review (eight numbered items plus judgement), a formal proof package (Sections 1–8 under the "gemini" label), and "grok upgrades" (drop-in mathematics, Sections 0–XII). Directive: read, evaluate, verify — nothing taken at face value; every finding adjudicated by exact computation against the shipped sources; valid findings implemented as new editions (comp v5 + S1 v5), false findings refuted on the record.

**Method.** Each claim was checked against `paper2_computational_certification_v5.tex`, `paper2_computational_certification_v5_supplementary.tex`, the verification harness, and the campaign scripts — not against the pasted extraction the audit reviewed. Rational arithmetic was executed exactly (Python `fractions`); LP claims were re-solved with exact rational witnesses via the campaign head.

---

## A. Refuted findings (audit claims that fail against our source)

### A.1 — Item 1: "the printed dual (F, f, η) is not reconstructable; f₁ = 5/4 is wrong"

**Refuted: the printed dual is exact as printed.** The audit read the OCR artifact "54" as f₁ = 5/4 and concluded the six-facet list cannot reconstruct U. The source prints f₁ = **4/5**, exactly the |u₂| ≤ 4/5 facet the audit's own geometry argument demands. With F, f, η exactly as printed in the shipped tex, all nine identities hold:

| j | Fᵀη_j | −n_j | check |
|---|---|---|---|
| 1 | (−1, 0) | (−1, 0) | ✓ |
| 2 | (3/5, −4/5) | (3/5, −4/5) | ✓ |
| 3 | (3/5, 4/5) | (3/5, 4/5) | ✓ |

and fᵀη_j = 1 for j = 1, 2, 3 (e.g. fᵀη₂ = (4/5)(1/2) + 2(3/10) = 2/5 + 3/5 = 1). The stationarity/normalization pair is a written, checkable Farkas certificate. **What the auditor missed:** the audit's own reconstruction ("one expects |u₂| ≤ 4/5 and |u₁| ≤ 1") implies f = (4/5, 4/5, 2, 2, 2, 2) — had it tested the identities against the f its own geometry produces, it would have confirmed the certificate instead of rejecting it. All nine identities are now recomputed on every run of `paper2_computational_certification_v5_verification.py` (Layer 2).

### A.2 — Erratum target "original Example 2's (5/8, 5/16, 5/16)"

**Refuted as out of scope: no such text exists in this paper's lineage.** The triple (5/8, 5/16, 5/16) appears in none of the shipped tex sources (grep over the full latex tree: absent); it belongs to an external preprint not under this repository's control. It is also not a barycentric triple: 5/8 + 5/16 + 5/16 = 5/4 ≠ 1. The shipped pooling weights are λ = (3/8, 5/16, 5/16) (with the 6/16 + 5/16 + 5/16 barycentric note), which the audit confirms as correct. No erratum can be issued from this paper; the point is recorded for the owner-side ledger.

### A.3 — The two proposed {1,2} blind controls (formal package §5.3)

Both proposed controls are refuted by direct computation; the shipped pairwise witness is untouched and remains the unique exact optimum among the controls examined.

**Control 1: u = (−4/5, −2/5).** Not a brake for branch 2:

n₂ᵀu = (−3/5)(−4/5) + (4/5)(−2/5) = 12/25 − 8/25 = **4/25 > 0** — it *accelerates* mode 2 along its critical facet. True peak (exact integration over [0, τ] with acceleration u, then optimal brake −n₂): **2.095712…** > 2. The audit's own arithmetic reaches 2.0957 and then silently abandons the control.

**Control 2: u = (−0.485, 0.630).** Worse: n₂ᵀu = (−3/5)(−0.485) + (4/5)(0.630) = 0.291 + 0.504 = **159/200 > 0** — strictly accelerating. The claimed peak "n₂ᵀp ≤ 1.954" is fabricated; the true peak is **4495081/2000000 ≈ 2.2475**. (The control is feasible in U: |2u₁+u₂| = 0.34 ≤ 2, |2u₁−u₂| = 1.6 ≤ 2, |u₂| = 0.63 ≤ 4/5 — but feasibility is not the issue; the sign of n₂ᵀu is.) A "direct numerical evaluation" yielding 1.954 for an accelerating control does not exist.

**Shipped witness stands:** u = n₃ on [0, τ] then the exact brake gives peak **12345/6250 = 1.9752** exactly ({1,2} and, by reflection, {1,3}), and u = n₁ gives **2419/1250 = 1.9352** for {2,3}. The audit's own u = n₃ single-brake variant attains only 62499/31250 (margin 1/31250) — strictly dominated. Both refutation pins are recomputed in the v5 verification harness (Layer 2).

### A.4 — Item 6: "s = 5" and "the paper never writes s = 7"

**Refuted against the current edition.** s = 7 (three position facets n_iᵀp ≤ 2 plus four velocity facets |v₁|, |v₂| ≤ 6/5) is printed twice in comp v5: in the facet-count sentence ("seven facets in all, s = 7") and at the Table 1 dimension line (s = 7, p_U = 6). The audit's own formal package (§V) and the grok-on-gpt pass both confirm s = 7; the count Ms(N_t+1) + p_U Q is consistent with it. The "paper never writes s=7" observation was true only of the OCR-dropped extraction.

---

## B. Upheld findings and their edit loci (implemented in comp v5 + S1 v5)

| # | Audit finding | Verdict | Edit locus |
|---|---|---|---|
| B1 | Item 5 / package §2: Lipschitz/TV used but never stated for the instance; "whole refinement gap is the moment error" is an extra hypothesis unless the other terms are identically zero | **Upheld** | comp v5 §6: instance moduli derived and printed — R_U = 1 (hexagon circumradius), V_U = τ + 1 = 6/5 (endpoint kernels are unit-slope ramps of height t\*), δ_β = 0 (β computed exactly), L = T + 1 = 11/5 (kernel-difference route: ∫\|w\| ≤ T\|t−t′\| on the post-observation affine kernel; \|β_t − β_t′\| = \|t−t′\|); sandwich bound J ≤ ρ(h) + (6/5)h + (11/5)h_t printed alongside the witnesses proving the realized gap is exactly Th/4 |
| B2 | Package §2: moduli assumed, not derived from primitives | **Upheld** | S1 v5: new block "Derivation of the moduli from primitive data" — V_U = c̄(B̄ + M_X V_B + B̄ M_X Ā T) with the X(t,t) = I jump handled explicitly; L^tr closed form; the h = 1/15 line added to S2's verification record |
| B3 | Package §5 / grok-on-gpt: mesh-law domain "five tabulated points" vs max{0, 3/50 − Th/4} for all aligned h | **Upheld (and strengthened)** | comp v5 §6: domain extension now *certified*, not asserted — sixth aligned mesh h = 1/15: ρ = 1/25, Q = 48 = 3 + 45, 687 inequalities (399 label + 288 box), exact primal + dual witnesses via the campaign head; dual objective telescopes to −3/100 for every h |
| B4 | Package §6: "every other row ≤ 3/100" was script-only | **Upheld** | comp v5 §6: bare 465-row sentence replaced by the structural trichotomy (endpoint rows tight by the exact identity; velocity rows carry slack ≥ 1/5 against charged error ≤ 3/100; noncritical position rows ≤ 0), with the count stated |
| B5 | Package §7: semidecidability termination | **Upheld** | comp v5 item (iii): dyadic halting bound added — ρ_k ≥ γ − C·T/2^k forces halt by an explicit k\* |
| B6 | Grok upgrades §0: "every dual solution is an obstruction" is false as written; replace by complete dual calculus | **Upheld** | comp v5: Corollary (complete dual calculus) after the Proof of (iv) — every dual-feasible pair bounds every measurable policy from below; positivity is the decision; atomic attainment stated instance-level |
| B7 | Item 3: stale cross-references | **Upheld in part (real defect found)** | Root cause: `\thesubsection` carried a trailing period into every `\ref` ("Section 13.;", "(Section 9. gives…)"). Fixed at the macro level (period moved to `\@seccntformat`): headings unchanged ("13. Verification methods"), prose refs now "Section 13", "(Section 9 gives…)". PDF-probed: no "??", no period-in-ref |

## C. Findings adjudicated as artifact / pre-existing / already-shown

- **Item 2 (OCR, smashed fractions): artifact.** The audit itself concedes "a typeset PDF may be clean; the text you pasted is not reviewable as-is." PDF probes on the rebuilt v5: n₂ = (−3/5, 4/5) renders correctly; no 'efmethods' (a `\ref` whose backslash-r was stripped as a carriage return in the *pasted tex*, not in any rendered artifact); "surrogate.Data availability" concatenation absent — the heading renders standalone ("Declarations … Data availability — No external data were used"); no broken "Section 13" beyond the (fixed) period issue.
- **Item 3 sub-claims 'Section 13' vs introduction's Section 7: not an inconsistency.** The introduction's map points to the *computation* subsection (7) for complexity; the library section points to the *verification-methods* back-matter (13) for the scripts. Both resolve; the only defect was the period, fixed (B7).
- **Item 4 (viacert binds the companion to the unfixed discrete audit): pre-existing delimitation.** §10/Scope already states the library "is not a reimplementation of this paper's bridge theorems" and names consolidation as the recorded next step; the discrete-layer repairs (Table 2 row 1211, protocol-vs-alternation) are owner-side ledger items, unchanged by this round.
- **Item 7 (counts "unshown"): shown where they belong.** "51 exact checks" / "nine checks" / "twelve identities" are executed, not narrated: the shipped verification harness (this edition: 26 checks, including the nine dual identities and the h = 1/15 witness run) and the ws scripts print them on every run.
- **Item 8: audit's own verdict — delimitations correctly scoped.** No action.
- **Production/archive (arena path, DOI consolidation, 2026a = 2J3KL): standing owner-side ledger items**, decoupled from this paper's editions (figshare assessment; single-DOI consolidation pending).

## D. What the auditor missed (strengthening record)

1. **Both proposed {1,2} controls fail a one-line sign test** (n₂ᵀu > 0 for each): one accelerates mode 2 by 4/25, the other by 159/200, and the second's quoted peak (1.954) is not attainable by any evaluation of the stated trajectory — its true peak is 2.2475. A pairwise-viability "proof" that replaces the shipped exact witness would have *weakened* a proved headline into a fabricated one.
2. **The dual "blocker" dissolves under the audit's own geometry.** Its facet reconstruction implies f₁ = 4/5; testing the printed η against that f confirms all nine identities. The single "mathematical item that still fails a line-level check" (its words) was an OCR misread.
3. **The mesh-law domain claim needed a sixth certificate, not prose.** The formal package asserts ρ(h) = max{0, 3/50 − Th/4} "for all aligned h ≤ T" without proof beyond five points; this round ships the h = 1/15 exact witness pair (ρ = 1/25, 687 rows) plus the h-independent dual telescoping, converting the claim into a theorem with an at-will verification path.
4. **The cross-reference defect was global, not spot.** Every mid-prose `\ref` to a numbered subsection carried the trailing period; the audit quoted two instances. The fix is one preamble macro, restoring all of them at once.

## E. Edition state

- `paper2_computational_certification_v5.tex` / `.pdf` — 8 pp., zero overfull, no undefined references; moduli block, trichotomy, dyadic halting, complete-dual-calculus corollary, cross-ref macro fix.
- `paper2_computational_certification_v5_supplementary.tex` / `.pdf` — 4 pp., zero overfull; "Derivation of the moduli from primitive data" block, L^tr closed form, h = 1/15 line in S2.
- `paper2_computational_certification_v5_verification.py` — **26/26 checks pass**, including Layer 2: the nine dual identities (Fᵀη_j = −n_j, fᵀη_j = 1), the instance moduli grid check, the h = 1/15 primal/dual witness run against the campaign head, and both refutation pins (peaks 2.095712… and 4495081/2000000 ≈ 2.2475).
- Prior editions byte-untouched; no claim softened; the false audit proposals were *refuted* rather than absorbed.
