# Self-Contained Prompt — Profound Strengthening of the Obstruction-Calculus Manuscript

Copy everything below the line into a fresh agent session (with the workspace
from `MIKEAA2020/general-sustainability`, path `arena agent 1/paper rewrites/latex/`
checked out locally). The prompt is self-contained: it states the paper's
identity, the evidence gaps to close, the standing editorial constraints, and
the verification/push requirements.

---

## TASK

Profoundly strengthen the manuscript **"An Obstruction Calculus for Viability
under Incomplete Observation"** (paper 2), currently at version **v37**. The
goal is to close every evidence gap listed below with *genuine mathematical,
computational, or empirical content* — never padding, never meta-commentary.

## FILES AND CONTEXT

- Main source (current, v37):
  `arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v37_Automatica_routes.tex`
- Supplementary (current, v37):
  `arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v37_Automatica_routes_supplementary.tex`
- Figures live in `arena agent 1/paper rewrites/latex/figs_p2/`.
- Compile with `tectonic` (binary at `/tmp/tect/tectonic` if not on PATH).
- Verify with `PyMuPDF` (`import pymupdf` / `import fitz`).
- The Section 3 spine is fixed (do NOT reorder): 3.1 finite-horizon recursion,
  3.2 common-action, 3.3 delayed-information, 3.4 sparse witness (Helly),
  3.5 finite-time exit, 3.6 admissibility. Hypothesis labels (H2.x, H3.x, H5.x)
  and equation tags (1)–(5) already match this order in both files.

## VERSIONING RULES (non-negotiable)

1. Never overwrite v37 (or any earlier version). Produce **v38** (and v39, v40…
   if you work in passes), copying v37 → v38 first.
2. Every pass must compile standalone (main **and** supplementary), pass the QA
   harness below, and be pushed to GitHub before the next pass begins.
3. Push every new creation (tex, pdf, addendum, build/revision scripts) to
   `MIKEAA2020/general-sustainability` at `arena agent 1/paper rewrites/latex/`
   using the PAT at `/home/user/uploads/github_pat.txt`. Also push any still-
   unpushed prior artefacts you notice.
4. Write a short `paper2_vNN_addendum.md` per version documenting exactly what
   changed and the QA results.

## STANDING EDITORIAL CONSTRAINTS (non-negotiable)

- Abstract ≤ 265 words; no undefined abbreviations; contributions stated
  factually (do not overclaim — see GAP 2).
- No meta-commentary, no change-log, no "In words", "Takeaway", "Reader's
  guide", no self-praise, no informal chat terms in the manuscript itself.
- Formal citations only (author–year + italic short-title + DOI). No shorthand
  "Abaee, 2026a/b/c". Add a reference only where genuinely merited.
- Keep the hybrid register: polished readable prose + rigorous math (the paper
  already matches Prajna–Jadbabaie–Pappas 2007 in register — preserve it).
- "Practical message:" phrasing, not "The practical message is that".
- Keep the brief AI declaration at manuscript end; do not expand it into prose.
- Supplementary must stay aligned with the main text and be humanized using the
  main text as the style example.

## EVIDENCE GAPS TO CLOSE (in priority order)

**GAP 1 — reproducibility contradiction (critical).** The declarations block
says "No code was used or produced", yet Section 8 presents a "reproducible"
coverage audit with a generated figure and exact cell counts (42 nonviable:
30 common-action, 12 timing). Fix: (a) write a small, self-contained Python
script that computes the delayed hidden-regime audit and regenerates
Table 1 + `fig_p2_coverage.png` from the same code; (b) rewrite the "Code
availability" declaration to point at the script (and note the Zenodo record
`https://zenodo.org/records/22545740` as the archive location); (c) make the
table machine-generated so the 30/12/42 counts are verifiable.

**GAP 2 — abstract overclaim.** Abstract claims "finitely checkable in the
finite-state, polyhedral, and finite-horizon cases", but the timing/exit
certificates are analytic (only common-action, fibre, and recursion are shown
finitely checkable). Either qualify the abstract precisely, or (stronger) add a
genuine polyhedral checkability result for the timing obstruction (e.g., LP /
piecewise-constant blind-window reduction), with theorem + proof.

**GAP 3 — no worked method comparison.** Add one subsection demonstrating, on
a single shared example, what (i) the barrier-certificate programme can/cannot
certify, (ii) the estimation-tube reduction returns, and (iii) which
obstruction certificate fires and what design change it licenses. Place it in
Section 6 (discussion) or the supplementary; cite §6.2/§6.3 from it.

**GAP 4 — Helly hypothesis boundary.** Add a short counterexample (non-convex
safe-action set or control-nonlinear dynamics) where the m+1 sparse witness
fails, plus a scope remark stating exactly what the convexity hypotheses buy.
Insert near Proposition 4.

**GAP 5 — probabilistic section is asserted, not demonstrated.** Add one worked
POMDP instance (the hidden-regime or two-floor example): compute V_k for small
k, tabulate it against the certificate verdicts, and state the correspondence
via the degenerate-limit proposition. Keep §9's length proportionate.

**GAP 6 — timing certificate has no general computational instantiation.**
Supply one concrete checkability result for H3.2 (polyhedral data,
piecewise-constant blind-window controls → finite LP / robust-reachability
check) with theorem + proof, OR state a precise, scoped limitation with one
fully worked special case (constant-observation, hold-until-T_obs).

**GAP 7 — post-observation-recourse mode is named but never exhibited.**
Construct a small example where a common blind-window control keeps every
branch safe but no post-reveal observation-adapted control recovers every
branch. Prove both halves. Cite it from §6.5(ii) so the limitation becomes
concrete, and use it to sharpen Open Problem 1.

**GAP 8 — applied audience.** Extend the case study with at least one
two-dimensional instance (e.g., the coupled-patch model with a coarse shared
indicator) so the "multidimensional campaign deferred" concession shrinks, and
add a calibration paragraph mapping certificate parameters (ε, T_obs, bias b,
floor) to quantities estimable from published stock-assessment practice.

**GAP 9 — proof-collection asymmetry.** Reword §1.4 (and the supplementary S1
header) so the claim matches reality: full proofs of the Section 3 certificates
are in the Supplementary; Section 7 and Section 9 results are proved in the
main text. Do not duplicate proofs.

**GAP 10 — quantify non-completeness.** State and prove (or refute with a
counterexample) a finite-horizon partial converse: if the common-action and
timing certificates do not fire on horizon N, does some policy survive N steps?
The coverage audit's "jointly complete in the delayed class" remark is the
seed; make it a theorem or a named, proven counterexample.

## PASS PLAN (work in guardrailed passes, each published)

- **Pass A (v38):** GAP 1 (code + declarations) + GAP 2 (abstract/checkability)
  + GAP 9 (proof-collection wording). These are prerequisite repairs.
- **Pass B (v39):** GAP 3 (method comparison) + GAP 4 (Helly counterexample).
- **Pass C (v40):** GAP 5 (POMDP instance) + GAP 6 (timing checkability) +
  GAP 7 (post-recourse example).
- **Pass D (v41):** GAP 8 (2-D case study + calibration) + GAP 10 (partial
  converse), then a final full-manuscript consistency pass.

Adapt the grouping if dependencies demand; keep every pass self-contained and
pushable.

## QA HARNESS (run after every pass, on main AND supplementary)

1. Compile both with tectonic; confirm **no errors, no "Overfull \hbox"**, and
   exit 0.
2. PyMuPDF: report pages, image count, and that `??` count == 0. (Main should
   stay ≈15 pp; supplementary may grow as content is added — record the number.)
3. Abstract word count ≤ 265 (count from the source `\begin{abstract}` block
   with `---` treated as whitespace; current = 262).
4. Numbering integrity: Theorems 1–N, Propositions 1–M, Remarks, Corollaries,
   Examples all present in sequence with no gaps; subsubsections 3.1–3.6;
   equation tags (1)–(5) in reading order; hypothesis labels H2.x/H3.x/H5.x
   consistent; `Section X.Y` references all correct.
5. Content-loss check: line-level and word-multiset diff of the new version
   against v37 must contain only intended edits (every removed line accounted
   for).
6. If new math was added: verify each new theorem/proposition has a proof
   (main or supplementary) and each new citation has a reference entry.

## DELIVERABLE

A new version (v38…), compiled + QA'd + pushed, with an addendum documenting
the gaps closed and the QA numbers. Report back: version reached, gaps closed
(with one-line evidence each), any gap deliberately left open and why, and the
final QA table (pages / images / `??` / overfull / abstract words) for main and
supplementary.
