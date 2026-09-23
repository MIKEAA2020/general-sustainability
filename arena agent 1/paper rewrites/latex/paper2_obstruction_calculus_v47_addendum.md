# Paper 2 — v47 Addendum (disposition record)

**Version:** `paper2_obstruction_calculus_v47_Automatica_routes` (main only; supplementary **unchanged** and remains at v46).
**Base:** v46 (pushed `682b467`).
**Implements:** the two remaining open evidence gaps of roadmap v3 Track A — **Gap 5** (§9 probabilistic lift asserted, not demonstrated) and **Gap 8** (second, two-dimensional instance). Track A content is thereby complete; the remaining Track-A item is the A3 editorial sweep (planned v48), per the owner directive to implement the rest of the roadmap.

## 1. What v47 adds

### Gap 8 — Two-patch protection audit (main §8)
New paragraph + **Table 3** (`tab:patch`): two patches, states {0,1,2,3}², recruitment +1, shared protection action u ∈ {1,2} (protected patch loses nothing, the other loses 2), floors z_i ≥ 1, aggregate reading y = z₁+z₂. Results (all exact integer arithmetic):
- Belief {(1,2),(2,1)} — one reading y = 3 — has an **empty common safe-action set** (each state safe only under the opposite protection) ⇒ the common-action certificate fires while each state alone is in the full-information kernel: the minimal epistemic-emptiness form realized in two dimensions.
- Certainly-safe readings exactly **y ≥ 4** (two-dimensional Corollary reading).
- Belief-level recursion (reading splits beliefs into y-cells): **every nonviable belief is certified, all by the common-action certificate** — the aggregation obstruction is instantaneous and no observation schedule rescues it, in contrast with the one-dimensional timing cells (where T_obs = 1 is viable).
- Full-information kernel = {z₁,z₂ ≥ 1} \ {(1,1)}: the double-depleted state is nonviable outright (one protection per step cannot hold both floors).
- §8 closing paragraph updated; conclusion's case-study clause extended.

### Gap 5 — Worked belief-state instance (main §9)
New paragraph + **Table 4** (`tab:beliefV`): the §8 audit system as a finite POMDP over the declared hold class. Exact closed-form safety values: for k ≤ T_obs, V_k(b₀) = ½(1[z₀−k ≥ 1] + 1[z₀+k ≥ 1]); for k > T_obs, V_k = ½(1 + 1[z₀ ≥ 1+T_obs]). Three alignments (all machine-verified):
- V₁ = 1 ⟺ z₀ ≥ 2 — exactly the one-step certificate's silent region;
- V_k ≡ 1 ⟺ z₀ ≥ 1+T_obs — the audit's viability boundary, cell by cell;
- every deficit equals ½ = min_x b₀(x) — the Proposition (degenerate limit) bound **attained** on every nonviable cell.
Plus the class-declaration result: over unrestricted time-varying blind policies the value is 1 exactly on {z₀ ≥ 2} — the timing-bound cells are precisely the cells where in-window adaptivity rescues the declared hold class (the §9 echo of Theorem 4(iv)). Conclusion's lift clause extended.

## 2. Verification record (`paper2_v47_verification.py`, stdlib only)
**12/12 checks pass** (A1–A6 Part A: closed-form vs brute-force hold-class values on all 48 cells; V₁ boundary; viability boundary; deficit saturation; unrestricted-policy brute force over 2^k sequences; 42 = 30 + 12 partition. B1–B5 Part B: safe-action sets; kernel; state recursion fixpoint; aggregated-observation belief verdicts incl. the minimal 2-D epistemic-emptiness belief; certainly-safe readings {4,5,6}). **Both new tables are generated verbatim by the script.**

Correction during verification: the initial B1 assertion expected singleton safe-action sets at (2,3)/(3,2); the true sets are {1,2} (high stocks tolerate catch under either action). No table or verdict depends on those two states; assertion corrected to the true values.

## 3. Build and probes
- Tectonic 0.15.0; `main.pdf` 510,354 B, **19 pp** (v46: 18 pp). Supplementary untouched (v46, 15 pp).
- pymupdf probes: **0 unresolved `??`**; new sections render (regex probes with hyphenation normalization; note PDF line-break hyphens extract as ASCII hyphen + space, and `\setminus` extracts as a literal backslash pair); tables numbered 1–4 (1: certificate/response table; 2: coverage audit; 3: two-patch audit; 4: safety values); all `\ref`-based cross-references resolve.
- Probe-tooling note for future sessions: distinguish TeX hyphenation breaks (delete "- ") from compound-word breaks (keep hyphen) when substring-probing; stacked `\tfrac` extracts as numerator/denominator token pairs.

## 4. Files
- `paper2_obstruction_calculus_v47_Automatica_routes.tex` / `.pdf` (main)
- `paper2_v47_verification.py` (verification record + table generator)
- `paper2_obstruction_calculus_v47_source.zip` (14 entries: README, audit script, **both** verification scripts, main v47 tex+pdf, supplementary v46 tex (unchanged), 7 figures)
- Unchanged: supplementary (v46), `paper2_coverage_audit.py`, figures, roadmap (v3 → v4 status refresh pushed separately).

## 5. Roadmap status after v47
- Track A: A1 ✓ (v45), A4 ✓ (v45; Gap 5 and Gap 8 closed by v47), A5+A6 ✓ (v46), **A3 editorial sweep open (planned v48)** — items already satisfied earlier (three figures; computational section; Appendix handling; estimation-tube connection) to be recorded with dispositions; "necessity side" softening still open (§1, one sentence).
- Track B (companion, B1–B5) next; then C1–C2; D1 seeded by the v47 §9 instance.
