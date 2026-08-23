# HANDOFF — General-Theory Mathematical Closure Review (Docket T1–T9)

**For:** the AI agent (or human reviewer) tasked with correcting, extending, and implementing this review in the manuscript programme.
**From:** the external mathematical review that produced result records R01–R09 against the self-contained closure packet.
**Bundle integrity anchor:** the review was produced against `general_theory_math_closure_packet.tar.gz` (SHA-256 `51acc3a760e2a08f2ccc68aa5bacf9aea8a36434aa9047e2a6f7a4902932f49e`). You need that packet unpacked beside this bundle to verify every source citation (see §4).

---

## 1. Read this first — the one-paragraph version

The documents of record are `00_MASTER_CLOSURE_REVIEW.md` and the nine files in `01_result_records/`. Everything else in this bundle is either a circulation copy (the PDF) or regenerable machinery (`tools/`, `assets/`). **All corrections go into the `.md` records; the PDF is then rebuilt with one command** (`bash tools/build_closure_pdf.sh`). The records use the packet's required 17-field output schema; each is self-contained with proofs, counterexamples, dependency edges, and honest status/novelty fields. The review's headline conclusions are in `00_MASTER_CLOSURE_REVIEW.md` §3 (verdict table), §6 (minimum theorem set justifying "general theory"), and §7 (dependency-ordered research plan).

## 2. Bundle inventory

| Path | Status | Purpose |
|---|---|---|
| `00_MASTER_CLOSURE_REVIEW.md` | **document of record** | Schema audit (TCS-1.1 diff), dependency graph, verdict table, universal/model-class separation, publication-dependence audit, minimum theorem set, research plan (waves A–F) |
| `01_result_records/R01…R09_*.md` | **documents of record** | The nine docket-target results, each in the 17-field schema of `12_REQUIRED_OUTPUT_SCHEMA.md` |
| `GENERAL_THEORY_CLOSURE_REVIEW.pdf` | circulation copy | 70-page consolidated render (cover + TOC + all records). Never edit directly |
| `tools/preprocess_closure_md.py` | machinery | Combines the 10 `.md` files into `_build/combined.md` with glyph-safe mapping (see §5) |
| `tools/build_closure_pdf.sh` | machinery | One-command rebuild: preprocess → pandoc → tectonic → cover → merge |
| `tools/merge_closure_pdf.py` | machinery | Cover+body merge, A4 normalization, link/bookmark preservation |
| `tools/header.tex` | machinery | Pandoc header (overflow hygiene, verbatim line-breaking, metadata) |
| `tools/cover.html` | machinery, **editable** | Cover source (Academic Template 03, Indigo). Edit text here, not in a PDF editor |
| `tools/html2poster.js` | machinery | Cover renderer (node + playwright/playwright-core required) |
| `assets/cover.pdf` | prebuilt fallback | Used by the merge when cover regeneration is unavailable |
| `_build/` (created on rebuild) | disposable | `combined.md`, `body.tex`, `body.pdf`, `cover.pdf`, logs |

Not included (get from the packet): the immutable A001/A002 sources, corrected theorem records `01`–`09`, TCS-1.0 schema, traceability CSVs. Every citation in the records points into that packet.

## 3. Correction protocol (how to modify this work)

1. **Locate the claim.** Records are independent files; the master review only summarizes them. If a theorem, proof step, counterexample, or status is wrong, fix it **in the record file**, then adjust the master review's §3 verdict table / §2 graph / §6–§7 only if the verdict or dependency structure actually changes.
2. **Respect the 17-field schema.** In particular: field 2 (verdict) must be one of `proved / repairable / false / classical / conjectural`; field 14 (novelty) must distinguish internal evidence from external literature status; field 16 must list remaining obligations and revocation triggers. If your correction demotes a result (e.g., a proof gap you find), **say so in fields 2 and 16 — do not silently keep the old status.** The packet's status-monotonicity axiom (TCS-1.0 §9, axiom 5) applies to this review as well: integration cannot promote a conditional claim to proved.
3. **Math notation.** Records use Unicode math in prose plus fenced code blocks for displays. The canonical packet typefaces (𝕂, 𝖨, 𝕎, 𝔄, 𝒱…) are preserved in the `.md` files — keep them there even though the PDF renders them as plain letters (§5).
4. **Rebuild the PDF** after edits: `bash tools/build_closure_pdf.sh` (add `--skip-cover` if node/playwright is unavailable; the merge then reuses `assets/cover.pdf`).
5. **Check the glyph budget** on every rebuild: the script prints the residual non-ASCII inventory; tectonic warnings `Missing character: There is no X` mean a newly introduced character lacks DejaVu coverage — add an entry to `EXPLICIT` in `tools/preprocess_closure_md.py` (never widen `NFKD_RANGES`; see §5).
6. **Known acceptable QA warnings** (do not chase): line-start `"` punctuation flags are English-typography false positives from the CJK-oriented checker; the asymmetric-margin warnings on some pages come from wide verbatim display blocks and are cosmetic; the TOC is clickable (16 link annotations on page 2) despite the checker's complaint — it detects ReportLab-style TOCs only.

## 4. Citation and verification conventions (critical for review)

- **Anchor format** in the records: packet file + label + line, e.g. `A001 Theorem 4.7 (sources/A001_topdown_source.txt line 550)` or `A002 thm:projectability (sources/A002_general_theory_source.txt line 1949)`. Line numbers refer to the **extracted packet files**, not the tarball member offsets. Identical copies live at `sources/full/A001_topdown.txt` etc.
- **Clause-level matches.** Where a record says "clause-level match" (e.g., R03.Thm1(1) to the corrected adversarial-exit theorem; R02.Cor6 to corrected `02` Lemma 2), the proof step is a verbatim transplant of a packet-proved argument into a new setting. Review those by checking the transplant preserves quantifiers and hypotheses — not by re-proving the packet theorem.
- **The controlling-corrected-theorem records** (`corrected_theorems/01`–`09` in the packet) supersede the immutable A001/A002 source formulations. If a record and a source text appear to conflict, the corrected record wins; if you believe a corrected record is itself wrong, that is a packet-level finding — flag it explicitly rather than routing around it.
- **What was NOT verified:** external/bibliographic novelty (packet self-containment report explicitly excludes it — every field 14 says "external check outstanding"), and all empirical calibration (excluded by the packet's README).

## 5. The glyph-safety trap (documented incident — read before touching the preprocessor)

The PDF pipeline renders through DejaVu fonts, which lack the Mathematical Alphanumeric plane (U+1D400+) and a few symbols. The preprocessor therefore maps those to plain letters, and nothing else. An earlier version of this script applied NFKD normalization to the whole U+2000–U+2BFF range; NFKD decomposes **negated relations** (≠ → =, ∉ → ∈, ⊄ → ⊂, ⇏ → ⇒) by stripping the combining solidus overlay, which **silently corrupted the mathematics** (e.g., "controlled ⇏ robust" became "controlled ⇒ robust"). The bug was caught by a symbol-integrity check before delivery. Rules:

- Only `NFKD_RANGES = ((0x1D400, 0x1D7FF), (0x2100, 0x214F))` may be normalized. These blocks contain only letter-forms.
- Symbol substitutions go in `EXPLICIT`, one entry at a time, with a comment.
- After any preprocessor edit, re-run the integrity probe: the counts of `≠ ∉ ⊄ ⇏ ↛ ≱` in `combined.md` must equal their counts in the source records.

## 6. Mathematical review priorities (where to spend scrutiny)

Ordered by stakes × delicacy. Times are rough for a careful reviewer.

1. **R02.Thm1 + Prop3 (T2 closed-loop bridge — the flagship).** The load-bearing hypothesis is the certificate family 𝒱 with condition (REG); check that the induction never needs filter exactness (it must not — the conservative variant is the point), and re-verify the hidden-mode witness arithmetic (ż = θu − 1; sum decay 2/interval; obstruction at t₂ with compatible set {(1,+1),(1,−1)}). ~1–2 h.
2. **R05.Thm2 + Cor3 (assume–guarantee).** Two delicate steps: (a) the erosion computation applied to proximal normals of the *eroded* sets K_{−r_i} (inherited from corrected `02` Lemma 2's normal-correspondence hypothesis — clause-level, but confirm the homogeneous ⟨ζ_i, v_i⟩ ≤ ‖ζ_i‖(…) step for proximal normals that are multiples of n_i); (b) the M-matrix/Neumann-series argument in Cor3 (standard, but check the sign conventions of A = diag(L) − M and the "both budgets negative ⇒ infeasible" claim). ~1–2 h.
3. **R06.Thm3 (moment non-closure).** The Chebyshev-alternation + Vandermonde-null-vector construction: verify λ_i = 1/∏_{j≠i}(x_j − x_i) annihilates moments 0..K, signs alternate, and ∫g dσ ≠ 0. (An earlier Legendre-perturbation attempt was wrong — signed perturbations cannot have vanishing even moments — and was replaced; the current construction is the one to check.) ~1 h.
4. **R09 Part M.1 (delay instability witness).** The characteristic-root crossing at τ = π/2 for λ + e^{−λτ} = 0: dλ/dτ = −λ²/(1+τλ) with Re dλ/dτ > 0 at (i, π/2). Short computation; verify signs. ~30 min.
5. **R03.Lem4 (horizon closure).** Self-contained classical proof (decreasing compact predecessors; Hausdorff-usc witness extraction for R_∞ ⊆ Pre(R_∞)). Check the subsequence step and that no continuity is needed for the ⊆ direction. ~45 min.
6. **R01 (endpoint/aggregate false positives), R04 (admission certificate), R07 (generation recursion), R08 (hierarchy converses).** Lighter: elementary witnesses and set algebra; verify arithmetic and the necessity-direction constructions. ~30–45 min each.

**Honest weak points already flagged in the records** (fields 9/16): R02's selector is axiom-of-choice level (measurable/regular selector = open obligation D2); R05.Open5 is a precisely stated open problem, not a gap; R06.Thm2's fibre-richness hypothesis is checkable-but-unchecked for non-moment functionals; R04's A004/A005 classifications are conditional on closing the error-register blocking items; R07 assumes fixed generation epochs (variable events remain open, per the packet's standing gap).

## 7. Manuscript implementation map

Where each record is intended to land (fields 15 of the records; consolidated here):

| Record | Paper 1 | Paper 2 | Paper 3 | Paper 4 | Paper 5 | Monograph |
|---|---|---|---|---|---|---|
| R01 | transformation section (boxed impossibility) | counterexample register | — | — | — | composition chapter |
| R02 | governance architecture section | full proof | — | — | closed-loop falsification design | execution-chain chapter |
| R03 | — | Lem4 + trichotomy | aggregate-margin prohibition (Thm3) | — | core methodology | — |
| R04 | admission standards | short proof of Thm1 | domain instantiation | domain instantiation | domain instantiation | domain appendix |
| R05 | architecture lesson | Thm1/2/Cor3 + Ex4 | — | — | — | composition chapter |
| R06 | — | Lem1/Thm3/Cor4 | — | — | — | cross-scale chapter |
| R07 | intergenerational section | proofs | — | — | — | intergenerational chapter |
| R08 | — | hierarchy appendix | — | — | — | — |
| R09 | **scope theorem (centrepiece)** | witness proofs | — | — | — | opening chapter |

Implementation discipline: each paper carries only what its own gate needs, cites records by ID (R01–R09) with status fields intact, and never promotes a conditional field-2 status. The master review §5 lists the two interfaces that become citable theorems (R02, R03) and the two prohibitions that are now theorems (R01's endpoint/aggregate unsoundness).

## 8. Outstanding obligations register (after your corrections)

1. External novelty audit (research-plan item F1) — every field 14 needs bibliographic matching against robust DP/reachability, viability, hybrid-safety, small-gain, and moment-closure literatures. This bundle could not do it: no external literature access.
2. Selector regularity (D2) — measurable/continuous selector for R02's (REG)-witness correspondence.
3. R05.Open5 — nonlinear small-gain with nonconvex implementation and shared controls (hypotheses enumerated in R05 field 16).
4. Variable-event delayed-hybrid kernel (packet standing gap; also bounds R07).
5. Empirical case selection and instantiation (R04 blocking lists; waves E1–E2).
6. `TCS-1.1` migration (master review §1.4 diff) — the specification-path type (R07.Def1), erosion-triple field (GAP-3), and quantifier guards QF-1..4.

## 9. Rebuild environment

Verified toolchain used to produce the shipped PDF: python3.12 + pypdf, pandoc 3.1.11, tectonic (TeX Live bundle auto-download), node + playwright for the cover. Fonts: DejaVu Serif/Sans/Mono (system). If your environment lacks tectonic, any XeLaTeX with `unicode-math`-capable fonts can compile `body.tex` (pandoc emits `unicode-math` when mainfont is set — check the preamble). If fonts differ, re-run and re-check the glyph budget (§5).

**File-size sanity:** the shipped PDF is ~450 KB / 70 pages; `combined.md` ~205 KB; total record text ~28,400 words.
