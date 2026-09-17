# Joint Evaluation — Two Humanized Audits of E1 (Grok ; Claude) → v52 (2026-09-17)

Sources: `batch 7 (audits of agent arena 1 paper rewrites)/grok claude e1.txt`
(Grok: line-level review, 8 sections; Claude: A–E prioritized audit, 12 major +
section/notation/redundancy sections). Target verified against
`e1/paperE1_cod_forecast_ladder_v50.tex` (frozen current). Method follows the
house format of `framework/JOINT_EVALUATION_HUMANIZED_REWRITES_V11.md`:
fact-check every checkable claim against the frozen artifact FIRST, then
evaluate style, then adjudicate.

## 0. Version-era identification (decisive for weighting)

- **Claude's audit describes a pre-band, pre-DM, pre-availability manuscript**:
  Def. 2.4 "underspecified, no horizon/tie margin" (A8), "no bootstrap/DM",
  "no code or data availability statement" (A9), "scoring core … fixed
  beforehand" unqualified. v50 answers most of this (band+comparator rule in
  Methods; §3.5 DM + block bootstrap line 673 ff.; archive/DOI apparatus).
  Weight Claude's *scientific* critiques (A1–A6) but discount its protocol-era
  critiques as largely stale.
- **Grok's audit is near-current** (quotes v50-era features: Def. 4.2, §3.3,
  Table 6 caption, annual-landings pass, Table 8, Rose 2026) and frames the
  humanization problem directly — its rating as the more actionable audit.

## 1. Fact-verification against v50 (spot-ruling the load-bearing claims)

| # | Claim (auditor) | v50 evidence | Ruling |
|---|---|---|---|
| 1 | Abstract quotes mixed 88 instead of origin-matched 84 (Grok §2) | Abstract line ~71: "matched persistence 84 kt against M1's 120" | **STALE** — already fixed; mixed 88/318 appears only parenthetically in Table 6/7 captions (line 1139, 1217) |
| 2 | Printed "exceeds the controlled reading by 3.6 kt" vs auditor's 3.2 kt | line 716–717: printed 3.6 kt | **VERIFIED as printed**; canonical values 87.65−84.43=3.22 (ledger); rounding artefact documented in cross-check. Fix = one decimal disclosure (Claude §2.3 ✓ same point) |
| 3 | K-bounds violated: M1b K=105.8/129.8 vs declared [500,5000] (Claude A3) | lines 406–423: **declared bound is [max_train S + 10, 5000]**; "K=105.8 … valid interior fit, not a bound violation"; "500 kt is the multi-start initialiser rather than the lower bound" | **REFUTED as written** — BUT the critique's valid kernel survives: the recovery-window lower bound (≈50.8 kt) still *exceeds the state range* issue is NOT acknowledged as prior sensitivity; deferred scientific item |
| 4 | Identical M1/M1b rows across catch treatments (Claude A4) | F1 v26 documents archived differences ≤0.04 kt (120.5095 vs 120.5406) that round to identical prints | **EXPLAINED, not a bug** — carry the reconciliation sentence into v52 (documentation, done) |
| 5 | Proposition 4.1 inapplicable at fitted r≈2 (discrete logistic flip) + window monotone (Claude A1) | line 1845: Proposition 4.1 present; fitted r=2.0 saturates upper bound (§2.2 line 414, 421) | **VERIFIED-OPEN, scientific** — requires restatement/re-scoping by the author; NOT a prose fix. Deferred (W2) |
| 6 | Lemma 3.2 monotone hypothesis fails on 1995–2007 window (Claude A2) | NCAM Table A2 values non-monotone (per archived file) | **VERIFIED-OPEN, scientific** — demote to remark or restate; W2 |
| 7 | Brier/sign-hit 0.00 convention disclosed only in §3.3 (Grok §2; Claude §2.3) | line 583: convention stated in §3.3 only | **VERIFIED-OPEN, textual** → v52 states convention at first appearance (W1) |
| 8 | "No structural model beats persistence" unqualified (Claude A6) | abstract: "on rolling RMSE pooled over origins"; line 796: M1b 90-kt fixed-window row acknowledged | **PARTIALLY FIXED**; v52 repeats the qualifier everywhere incl. the stall-window structural mini-wins (W1) |
| 9 | M4 delay decomposition labels swapped (Claude A7); value-of-timeliness 86 kt buried | M4 rows exist (196 vs 184 vs 98 h=1) | **VERIFIED-OPEN, textual** → v52 defines cost-of-delay vs cost-of-model-given-delay once, states timeliness result (W1) |
| 10 | Rose (2026) bibliographic status (Grok §2; Claude §1/A?) | line 2264 reference present | **VERIFIED-OPEN, bibliographic** → v52 carries a status footnote; lock at submission (W1-note/W2) |
| 11 | Freeze discipline overstated (both) | abstract "a rule whose scoring core was fixed beforehand" + §4 caveats | **PARTIALLY FIXED**; v52 uses the honest phrasing + pass-date table pointer (W1) |
| 12 | Highlights >85 chars; wrong keyword "recruitment forecast"; "Table 1" triple-reference; critical/healthy LRP quibble (Claude C/B) | present in v50 | **VERIFIED-OPEN, micro-textual** (W1) |
| 13 | Machine-layer wording inverts evidential order (Claude A9 vs Grok §5) | abstract tail: "machine layer verifies arithmetic not the class-level incompatibility" | **PARTIALLY FIXED** (arithmetic scope already stated); v52 tightens once more (W1) |
| 14 | "Collapse window not a fair contest; M2 = policy-as-exogenous" (Grok §1) | §3.1 already diagnoses endogeneity; no caption-level label | **VERIFIED-OPEN, textual** → v52 labels the run at first mention (W1) |
| 15 | Add drift/damped-trend baseline; LOO influence; floor-hit counts; regularised M1 (Claude E7/E8/A5) | absent | **DEFERRED — new computations (W2), owner-gated** |

## 2. Strengths and weaknesses of each audit

**Grok** — strengths: correct version era; groups by severity; identifies the
rhetorical-core defect (obstruction buried → abstract oversells "empirical
surprise"); catches status mismatches a referee will; prose implications are
directly implementable. Weaknesses: a few stale details (item 1); mixes
paper-critical points with style ones without separating W1/W2; derives the
"predetermined" charge at full strength where the paper's own Proposition 4.1
needs the scientific defence it may not have (item 5) — Grok treats the
obstruction as fact WITHOUT flagging that the proposition itself is contested,
which Claude catches.

**Claude** — strengths: the deepest technical read (A1 flip-bifurcation
critique is the single most important scientific finding in the bundle; A3/A5
box-edge and flat-valley identification; A7 decomposition labels; E-priority
list is executable). Weaknesses: reviewed a stale draft (protocol-era items
2–3, A8–A9, "no data availability" already fixed → noisy signal); treats
v50-documented behaviors as bugs when they are printed-rounding (items 3–4);
its register demands deletions/overhauls that would violate frozen-verdict
discipline if applied unselectively.

**Joint verdict.** Convergent truth set: (a) sharpen the abstract (obstruction
up front, matched figures, rolling-origin qualifiers, honest freeze phrasing)
— BOTH audits, both fixable textually; (b) Brier/direction conventions and
table-clarity micro-fixes — both; (c) scientific repairs (Prop 4.1, Lemma 3.2,
box priors, regularisation, drift baseline, LOO) — Claude-led, must route
through owner-gated W2 because they alter scientific content, not style.
Divergence adjudicated: where Claude flags "bug" but v50/harness documents the
behavior (items 3, 4), the paper's documentation stands; where Grok and Claude
agree (abstract honesty), implement at once.

## 3. Implementation plan

- **W1 (textual, this turn — implemented in v52 humanized):** items 2, 7, 8,
  9, 10-note, 11, 12, 13, 14 + abstract restructure per both audits. Frozen
  numbers untouched; style = Gemini-weighted (separate directive).
- **W2 (scientific, owner-gated, NOT silently changed):** Prop 4.1 restatement
  (flip-bifurcation regime; restrict to monotone F; delink from collapse
  score); Lemma 3.2 demotion/restatement; acknowledge box-bound prior
  sensitivity explicitly; optional new analyses (drift baseline, LOO
  influence, floor-hit counts, regularised M1) require harness runs +
  registration (claims-ledger rows), i.e., a new frozen sheet.
- **W3 (packaging):** highlights ≤85 chars; data/code availability block per
  Fisheries Research; Rose (2026) bibliographic lock; figure axis captions;
  rebuild PDFs when LaTeX available.
