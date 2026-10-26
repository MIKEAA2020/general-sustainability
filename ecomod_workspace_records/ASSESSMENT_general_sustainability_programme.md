# General-Sustainability Programme — Independent Enhancement Assessment

**Scope reviewed (2026-10-14):** `main` (tip `3c4eeeca`), branches `e2-v3-source-year` (Paper01 v70–v72), `lean-audit-v4`, `edwards-framework-e1*`, `archive/paper3-v48-workspace`; tags `compendium-v1.0`, `edwards-framework-e1`; folders `arena agent 1/paper rewrites/latex` (board family, current editions after round 30), `agent 2 productivity illusion` (ECOMOD v30–v41), `lean/`, the monograph preprint, `PROOF_MANIFEST.md`, `REVIEW_STATUS.md`, `worklog.md` (2,861 lines, Tasks 1–145).

**Method:** structural read of every current-edition manuscript (titles, abstracts, section trees, theorem inventories, word counts, figure/table counts, reference lists), rendered-page inspection of four PDFs, sentence-level diff of the two obstruction-calculus lineages, census of the repository, and reading of the one *human* referee report in the corpus (ECOMOD-26-1191). I did **not** re-derive the mathematics line by line; where I comment on content I say what I checked.

---

## 0. Executive summary — the seven changes that would matter most

| # | Change | Why it is the bottleneck | Effort |
|---|---|---|---|
| 1 | **State the one theorem the programme actually has, and organise everything under it.** The fibre criterion (P1 §4.1: *an observation-only certifier is exact iff the property is constant on the observation fibres*) is the general result; Paper 1's quantifier-order separation, ECOMOD's "aggregate does not identify composition", Paper 3's "no nonnegative weighting certifies componentwise nonnegativity", and the review-interval results of Papers 4/5 are all instances of it (the coarsening being a weighted sum, a delay, or a sampling clock). Nowhere is this said. | Without it the "general theory" is an architecture document plus unconnected results; with it, every paper has a reason to exist and a reason to cite the others that is not self-promotion. | Low (writing) |
| 2 | **Resolve the fork of the flagship paper.** `main` carries *An Obstruction Calculus…* v55 (cited by the Lean layer, the supersession map and all seven companions); `e2-v3-source-year` carries *Obstruction certificates under incomplete observation* v72 (rigor-repaired, A4 demoted, hypothesis-conditional restatements, gates A1–A3 and Theorems 3/7 open). Sentence overlap v55↔v72 is 21%. `main` contains no mention of v72. | The companions import statements from a version the author's own audit has weakened. This is the single most important structural-alignment defect in the repo. | Medium |
| 3 | **Consolidate the obstruction family from 8–9 manuscripts to 3.** Theory (P1 + minimax dual as a section) · Computation (comp + ws + ebc with the reference library) · Application (ARV folded into E1, or ARV as a 4-page note). | Several companions are 4–7 pages of exact-arithmetic censuses on toy instances (ebc: a 16-cell cube whose "headline" is an antichain count). Referees at Automatica/MoOR/TAC will read it as salami-slicing with dense self-citation. | Medium |
| 4 | **Stop the hedging-by-iteration erosion; replace de-claiming with quantification.** ECOMOD went from "Overcoming the productivity illusion…" (human referee: "overly speculative") through eleven agent rounds to an abstract that ends "…they are not a forecast and do not show a measured decline". | A claim that an aggregate cannot identify its components is near-tautological unless you bound *how much* can be hidden. The repair direction should be a theorem (identifiability set + its diameter), not more disclaimers. | Medium |
| 5 | **Cut length by 40–60% and move to venue-shaped structure.** P1 v72: 25k words/22+22 pp (Automatica regular ≈ 12 journal pp). Paper 1-AS: 54 pp. E1: 37 pp/22k words (IJF). Paper 3: 25k words, 0 figures. Paper 4: 28.7k words, 1 figure (a bifurcation paper). | Length and figure-poverty are the first things an editor sees. | Medium |
| 6 | **Get two or three human experts to read the two strongest manuscripts before any further agent round.** `REVIEW_STATUS.md` already says it: "An AI audit or successful build is not an independent mathematical referee." | The marginal value of agent round 31 is now far below the value of one reading by someone from the Doyen/De Lara/Aubin school and one stock-assessment scientist. | Low cost, high value |
| 7 | **Make the repository readable.** 1.1 GB, 5,847 files, 1,641 `.md` of which 758 are audits/reviews/records, 1,316 versioned manuscript files side by side (v1…v72), 94 zips, two `arena agent1`/`arena agent 1` folders. There is no path a stranger can follow to "the current paper". | Reproducibility compendium ≠ archive of every intermediate. Git *is* the version history. | Medium |

Everything below elaborates these, then gives per-paper notes, then writing/presentation specifics, then a concrete repo layout and a 90-day sequence.

---

## 1. Programme-level content: coherence and novelty

### 1.1 The missing thesis

Read side by side, the current editions share one idea, stated five different ways:

| Paper | Coarsening | Result as stated | Same result, generic form |
|---|---|---|---|
| Paper 1-AS v62 | weighted scalar aggregate of floors | ∀w ∃plan ≠ ∃plan ∀w; acceptance gap has nonempty interior | verdict computed from the aggregate is not constant on the fibres of the aggregation map |
| P1 obstruction v55/v72 | observation map / information set | common-action obstruction; **fibre criterion: exact observation-only certifier exists iff safe-set membership is constant on fibres** | *this is the general theorem* |
| ECOMOD v41 | value-weighted gha total | "the aggregate does not identify its own composition" | fibres of the gha map contain both rising-capital and falling-capital compositions |
| Paper 3 v32 | summation across moieties | "no nonnegative weighting certifies componentwise nonnegativity" | same, for the positive orthant |
| Papers 4/5, E1 | sampling in time (review interval, delayed information) | review interval is a design parameter; delayed-information obstruction; "uncertainty accumulated in the observation layer, not forecast structure" | temporal coarsening changes which fibres exist |

The monograph preprint (*Toward a General Theory…*, 20k words) does not contain this sentence either; it offers a typed registry, two operators, a hypergraph and ~10 boxes of placeholders. That is an *architecture*, which is honest and useful, but it is not what makes a reader believe a general theory is coming. One paragraph — "the programme's unifying result is a certification-limit theorem; aggregation, partial observation and periodic review are three coarsenings to which it applies; the papers are its instances and its obstructions" — would convert the corpus from a collection into a programme.

**Recommendation.** Write a short (≤ 8 pp) *programme paper* or make this the opening of the monograph: one theorem (fibre criterion, stated for a general coarsening map), three corollaries (aggregation / observation / sampling), one table mapping every paper to the corollary it instantiates and the extra structure it adds (dynamics, delay, exactness). Then let every paper's introduction cite that one object instead of 4–7 Zenodo deposits.

### 1.2 Where the novelty is real, and where it is thin

*Real, and under-sold:*
- The **common-action obstruction** and its **Farkas / measure dual** (P1 §3.2, minimax): a finitely checkable *necessary* condition for output-feedback viability is a genuine gap in the Veliov / estimation-tube / barrier-certificate literature, and the paper positions it correctly.
- The **delayed-information obstruction with an explicit timing bound**, and the **LP instantiation over polytope-declared blind-window classes** with the dual as witness (P1 Thm "LP instantiation of the timing certificate"; comp's sandwich bound with the information–time-rank witness bound). This is the part a control audience will actually use.
- The **no-Hopf theorem for the protective rule** and "intermediate delay stabilises" for the mobilising rule (Paper 4) — a clean, falsifiable, policy-relevant contrast.
- **E1's negative result** done honestly (pre-registered scoring core, persistence wins, power analysis under known truth). Null results on Northern cod with this level of discipline are publishable and valuable.
- The **three-way separation of "depletion time"** (gross turnover vs frozen-rate ratio vs scenario-conditioned hitting time) with the three public-data misclassifications (G3P, phosphate, fisheries) — Paper 3's most communicable contribution, currently buried in §6 of an 11-section, figure-less manuscript.

*Thin as currently framed:*
- **ECOMOD's identifiability property** is, as stated, a property of any sum. It becomes a result only with a quantitative statement: given an observed aggregate path B(t) and yield spread, the set of (capital, provisioning) compositions consistent with it, its diameter, and the data (land-cover/yield) that collapse it. The empirical split (cropland ×2.85 vs non-cropland ×1.01; per-capita −53%) is the paper's best asset and is on **page 23** of 30 as Figure 1. Lead with it.
- **ebc (4 pp)**, **ws (11 pp)**, **minimax (6 pp)** each contain correct, exactly verified facts about small instances (16-cell cube, 36 belief pairs, Y* = 27/5, margin 3/50). As stand-alone papers they will read as fragments. As sections of the computation paper they are evidence.
- **Paper 5 vs Paper 4**: both report the ≈ 6.5-yr crossing, the protective channel stable at every interval, and the cod case. The 42-stock spectral screen returns a null ("no robust institutional cycles"); pitching a null to *Nature Sustainability* is unlikely to survive triage. Either merge (Paper 4 = theory, Paper 5's sample-and-hold as its §6 and the screen as SI) or differentiate hard (Paper 5 as a fisheries-journal methods paper: "periodicity cannot diagnose governance feedback").

### 1.3 Structural alignment: the fork, and what depends on what

Measured facts:
- `main`: `arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v55_Automatica_routes.tex` (18 pp + 20 pp supp), 8 theorems / 12 propositions. Cited as "P1 = 2026b" by minimax, comp, ws, ebc, psuff, ARV, and by `lean/README.md` and `Formalizations/P1_Obstruction.lean` (header still says *source of record v53*).
- `e2-v3-source-year`: `…/paper 2 family/01_obstruction/paper01_obstruction_calculus_v72.tex` (22 pp + 22 pp supp), same 8 theorem titles, **743 vs 514 sentences, 220 shared** (Jaccard 0.21), title changed, abstract re-scoped ("finitely checkable *for declared polyhedral common-action and finite-system classes*; the fibre criterion instead addresses *static* certification; analytic drift and timing tests have *additional original-path premises*"), Proposition 1's necessity clause made hypothesis-conditional (v72 fix F3 found an explicit counter-example), A4 demoted, A1–A3 + Theorems 3/7 open (`A1_A3_READER_OPTIONS.md`).
- The branch is 363 commits ahead / 15 behind `main`; `REVIEW_STATUS.md` on `main` points readers to the branch; the supersession map on `main` does not know v72 exists.

Consequences to check (I did not verify each; they are the audit that is missing):
1. **minimax v11** abstract: "its polyhedral form carries a Farkas multiplier (Abaee 2026, *An obstruction calculus*, Section 3.2)". v72 restricts the finitely-checkable claim to *declared* classes under *held-action and local adverse-selection hypotheses*. Does minimax's Theorem 1 inherit those hypotheses? It should say so.
2. **comp v18**'s continuous-to-finite theorem relies on the original-path/pasting premises (H2.x) that v72 now holds *as hypotheses, not unconditional existence*. The companion must carry the same premise tags.
3. **psuff v11**'s support identity equates the posterior support with the calculus's set-valued post-state — defined in which edition?
4. The **Lean module** formalises the *finite/discrete* core (backward recursion, one-step characterization, common-action in discrete form, fibre criterion, Farkas perturbation). That core is stable across v53→v72, which is good — but the README's claim "the Lean layer proves the theorems that make those certificate checks load-bearing" must be scoped: it does not cover Theorems 3/7 or A1–A3, which are exactly the open gates.

**Recommendation.** (a) Declare v72 the source of record, merge the branch (or at minimum merge the `01_obstruction` folder and `REVIEW_STATUS.md` link targets) into `main`; (b) build a one-page **dependency matrix**: rows = companion papers, columns = P1 statements imported (by v72 label), cells = "unchanged / weakened in v72 / hypothesis added"; (c) for every "weakened" cell, either propagate the hypothesis or move the companion's claim to the finite class where it is unconditional; (d) close A1–A3 by *choosing the restrictive option* (Option B belief-policies, Option E Carathéodory convention, Option X remove `IRViab_J`) and publishing the smaller clean theorem — a journal will not accept "held open for an outside reader" as a status.

### 1.4 Verification vs. validation

The corpus has a very strong verification culture (Python batteries "238/238", byte-identical pinned rebuilds, Lean "395 theorems, zero sorry", SHA-256 manifests). It has almost no *validation*: one human referee report in the whole archive (ECOMOD-26-1191), no outside mathematician, no domain scientist. Two risks follow:

- **Overclaim by association.** "Lean-verified" on a title page will be read as "the theorems are machine-checked". The interface-level (`OrdField K`) formalisation checks algebraic/combinatorial cores, not Dini-derivative exit certificates or measurable-selection arguments. Each paper's data/code statement should say in one sentence what is and is not formalised (the lean README does; the papers should too).
- **Agents auditing agents converges on internal consistency, not on truth or importance.** The ECOMOD history is the case study: eleven rounds after the human review, the paper is internally impeccable and has less to say.

**Recommendation.** Freeze agent rounds on P1 and ECOMOD. Send P1 v72 (article + supplement) to two viability/robust-control readers and E1 + ARV to one assessment scientist (DFO/NAFO-adjacent or RAM Legacy community). Budget their findings as the next "round".

---

## 2. Per-paper notes (current editions)

Format: *what it is → the strongest version of it → specific fixes*.

**P1 — Obstruction certificates under incomplete observation (v72, branch).**
Strongest version: a 12-page paper with five certificates (common-action, delayed-information, finite-time exit, epistemic emptiness, fibre criterion), the LP instantiation with Farkas witness, and one calibrated example; the "obstruction taxonomy" (kind of failure × what is checkable × hypotheses) as a single table in §1. Fixes: move §8 (selector principle, dual certificates, monitoring adequacy) into the minimax/ws material; move §9 (symbolic case study + coverage audit) to the supplement; move §10 (belief-state safety values) entirely to psuff — it is already psuff's paper; rewrite the 2,800-character abstract as five sentences (problem, gap, main theorem, what is finitely checkable, what remains open); decide A1–A3 (see §1.3). Keep the "Open Problem" environment — it is one of the paper's virtues.

**Paper 1-AS — Aggregate indices and transition safety (v62, 54 pp, JMCDA SI deadline 2027-01-31).**
Strongest version: 18 pp. The quantifier-order separation with the rational witness datum and the convex-hull characterisation of the gap is the paper. The three figures of §2.5 are good and should move forward. Fixes: fishery benchmark (§4.3) and terminology guide → SI; proofs → appendix (already) but trim the "witness datum" proofs to the machine-verified table plus one worked case; drop "List of abbreviations" from the main text; the title should say what the result *is* ("…the aggregate cannot distinguish rescuable from impossible states"). Position explicitly as the aggregation instance of P1's fibre criterion.

**ECOMOD — How Aggregation Can Conceal Composition (v41, 30 pp).**
Strongest version: a 7–8k-word *Ecological Modelling* paper whose Figure 1 is the 1961–2022 decomposition (aggregate ↑23%, cropland ×2.85, non-cropland ×1.01, per-capita −53%), whose Figure 2 is the two-land phase portrait showing the masking region, and whose Proposition 1 is a quantitative identifiability statement (the fibre of the gha map over an observed B(t), and the yield/land-cover data that collapse it). Fixes: the top-level sections "Presentation", "Demonstration", "Policy extensions", "Model scope" are not journal structure — fold into Methods/Results/Discussion; the title footnote (`\thanks{Data vintages…}`) belongs in Methods; 6 tables : 2 figures should be inverted; delete the elevator analogy and halve the orchard framing (one paragraph, once); remove the second "the two-land model" from almost every paragraph of the introduction. On content: respond to the human referee's point (e) (parameters γ, ρ unjustified; self-referential) with a calibration table and a one-at-a-time sensitivity figure, not with a scope disclaimer. The agent's adjudication of the referee (`analysis/response_to_human_reviewer.md`) is good and should be the basis of the actual response letter.

**Paper 3 — Typed flux ledgers and depletion arithmetic (v32, 25k words, 0 figures/tables in the main tex).**
Strongest version: lead with the three public-data misclassifications (G3P is a statistical index, phosphate reserve-life is arithmetic, removals-only time is a pressure scale); then the three-quantity separation theorem with the uniform-drift bounds; then the ledger axioms as the machinery that makes the separation precise. Needs at least: one figure of the compartment–flux incidence structure, one figure comparing the three "depletion times" on the same stock, one table of the five double-counting rules. Cut the domain templates (§8) to SI. 11 sections → 6.

**Paper 4 — Governance delay and the stability of harvested stocks (v41, 28.7k words, 1 figure).**
A bifurcation paper needs the bifurcation diagram: (deployment delay τ) × (review interval Δ) plane with the Hopf window [3.7, 150] yr for the mobilising rule, the no-Hopf region for the protective rule, the 6.5-yr Neimark–Sacker crossing, and the five-regime attractor topology. That one figure plus a time-series panel would replace ~6k words. Keep the interval-certified Hopf crossings (the validated computation is a real asset; say in the paper that the continuum stages remain open, as the compendium honestly does).

**Paper 5 — The decision clock (v47, NatSustain-blinded).**
See §1.2. If kept separate: fisheries/ecology venue; the exact properties (forward invariance; rapid-review consistency over finite horizons only) + the 42-stock null + the 32-system search as a methods contribution: "what periodicity can and cannot diagnose."

**E1 — Does a surplus-production ladder improve forecasts of Northern cod? (v59, 37 pp).**
Strongest version: 9k words for IJF, with the power analysis and the vintage comparison as the two load-bearing figures and the honest "conditional hindcast, not operational forecast" statement in the abstract (it is already there — good). The last sentence of the abstract is the real finding and should be the title's second half: "…the decision-relevant uncertainty sat in the observation and reference-point layer, not in forecast structure." That sentence is also the bridge to P1 — say so in one line of the discussion.

**ARV — Regime viability on the Northern cod stock (v9, 7 pp).**
The harvest-free multiplier bracket [ρ, max{ρ+r, ρ/(1−r)}] is a neat, assumption-light object and the typology (collapse steps certify; reference-window steps do not) is useful. As a stand-alone CJFAS article it will be asked "what does certification add over looking at the series?" Answer it in the introduction, or fold into E1 as §3.x "what the record certifies without a model".

**comp / ws / ebc / psuff / minimax.** Consolidate (see §0 #3). Within the consolidated computation paper, the information–time-rank result (witness count bounded by rank r+1, not input dimension; saturating construction) and the shared-authority delay hierarchy (τ* = 7/50; pairs ≈ 0.245, 0.397) are the memorable results — make them the two headline propositions.

**Monograph preprint.** Fine as a labelled architecture document. Add the unifying theorem (§1.1), a figure of the two operators, and cut Part IV placeholders by half; a reader currently meets Box 3 "placeholder module" before meeting any result.

---

## 3. Writing

**Abstracts.** Every theory abstract is a list of results with numbers (27/5, 3/50, 7/50, 16×12, 36/156, 384 witnesses, 1,048,576 → 496). A referee cannot extract the claim. Template that works for this material: (1) the question in one sentence; (2) why existing tools do not answer it; (3) the main theorem in words; (4) what is finitely checkable / exactly computed; (5) what is open. ≤ 200 words for Automatica/TAC, ≤ 250 for Elsevier ecology.

**Programme jargon leaking into manuscripts.** "book" (for a capital account), "codex systems", "board family", "rung/ladder", "spine", "gates", "banner", "edition", "lineage", "the recorded-provenance form", "v28-era", "corrected to". Readers outside the repo have no access to these meanings. Replace with standard terms or define once.

**Sentence rhythm.** Long chains of appositive clauses ("…sound beyond the declaration with an unbounded implementable-class gap; and the residual dynamic gap is shown to decompose exactly, its post-observation recourse phase undecidable by any certificate pair that reads only the window sub-model") are correct and unreadable. One claim per sentence in abstracts and theorem statements; the ECOMOD introduction's first two paragraphs show the author can write plainly — hold the rest to that standard.

**Hedging.** Prefer precise hypotheses to disclaimers. "These results … are not a forecast and do not show a measured decline" (ECOMOD abstract) tells the reader what the paper is not; "under constant yields, a rising aggregate is consistent with capital drawdown of up to X% over the window" tells them what it is.

**Self-citation.** 4–7 Zenodo/figshare self-deposits in each reference list, "Abaee 2026a–g" lettering across papers (the lettering collision was itself a multi-round task). After consolidation this halves; additionally post the two anchor papers to arXiv (math.OC; q-bio.PE) so that the citations resolve to something referees recognise.

**Declarations.** Every paper carries an AI declaration naming the models — this is correct and increasingly required. Make them uniform (same wording, same placement) and add the Lean/verifier statement in the same block.

---

## 4. Presentation and typesetting

Observed in the current `.tex` sources:
- Pandoc artefacts: hard-coded numbers inside headings (`\subsection{1. Introduction}`, `\subsubsection{1.1 The problem}`), `\tightlist`, `\subsection` used as top level in some files and `\section` in others, `\subsection{References}` as a numbered heading.
- No BibTeX/BibLaTeX anywhere: references are hand-typed paragraphs (fragile; the round-27/28 "stale self-reference" repairs were caused by this).
- Figure placement: ECOMOD's only figures at pp. 23–24; Paper 4 with one figure; Paper 3 with none in the main tex.
- Multiple preambles per family (A4 `geometry` + `article` for Automatica targets; portal-adaptive `iftex` preamble for ECOMOD — the latter is good engineering and should be the shared template).
- Titles: good in general; two are too long (comp: three-clause title), two are too vague ("Exact audits of worked systems…").

**Recommendation.** One shared `preamble.sty` (engine-adaptive, as in ECOMOD v39+), venue class files (`elsarticle`, `ieeetran`, `siamart`) switched by a single flag, BibLaTeX with one `programme.bib`, `\section` hierarchy without hard-coded numbers, figures generated by the existing verifier scripts (the "recompute-then-assert" figure rule from round 26 is excellent — extend it to every paper), and a `make` target per paper that produces main + supplement + submission zip.

---

## 5. Repository organisation

**Observed.** 1.1 GB · 5,847 files · 1,641 `.md` (758 named audit/review/record/changelog/worklog) · 404 `.tex` · 383 PDFs · 94 zips · 1,316 files with `_vNN` in the name · duplicate folders `arena agent 1/` and `arena agent1/` · root littered with 50+ `build_*.py` and cover letters · the flagship manuscript's current version on a side branch · `PROOF_MANIFEST.md` (95 kB) and `worklog.md` (2,861 lines) as the only indices · README describes the August compendium, not the October state.

**Target layout (one current version per artefact; history lives in git):**

```
README.md                  ← what the programme claims (the §1.1 thesis), map of papers, status table
STATUS.md                  ← one table: paper · current edition · venue · gate status · last human review
CHANGELOG.md               ← replaces worklog.md as the public log (worklog → docs/history/)
papers/
  00_programme/            ← unifying theorem paper / monograph preprint
  01_obstruction/          ← main.tex, supp.tex, figs/, verify/, paper.bib, CHANGELOG.md
  02_computation/          ← consolidated comp+ws+ebc
  03_assessment_separation/
  04_ledgers/
  05_delay_dynamics/       ← (+ sampled governance if merged)
  06_cod/                  ← E1 (+ ARV), E2–E4
  07_ecomod/
lean/                      ← as now; README states scope (finite core) explicitly
data/                      ← locked CSVs with hashes (RAM, NFA, DFO), one README
docs/
  audits/                  ← all historical audit/adjudication md, by date
  history/                 ← superseded editions index (pointers to git tags), worklog
  reviews/                 ← external (human) reviews and responses
releases via git tags + Zenodo GitHub integration; no zips in the tree
```

Rules that would prevent regrowth: (i) never two versions of a manuscript in the tree — bump by commit, tag releases; (ii) audit documents go to `docs/audits/<date>_<paper>_<topic>.md` and are summarised in the paper's `CHANGELOG.md`; (iii) no PDFs in git except the tagged release PDFs (use releases/Zenodo); (iv) one branch = one paper revision, merged on close, deleted after.

**Security note.** No full token strings are present in tracked files on `main` (checked with a pattern search across the tree); the `uploads/github_pat.txt` "never push" line in the supersession map suggests it has been close. The token you pasted into this chat should be rotated once you are done with it; I have stored it only in `secrets/github_pat.env` (mode 600) in this workspace, and the clone's remote URL has been reset to the plain HTTPS URL so the token is not in `.git/config`.

---

## 6. A 90-day sequence

**Weeks 1–2 — Decide and merge.**
Declare v72 the record; merge the `01_obstruction` folder to `main`; write the dependency matrix (§1.3); choose A1–A3 options; write the §1.1 thesis paragraph and put it in README and every introduction.

**Weeks 3–6 — Consolidate and cut.**
Produce: P1 (12 pp + supp), Computation (≈ 15 pp), Paper 1-AS (18 pp), ECOMOD (8k words, Fig. 1 moved to front, identifiability proposition added), E1 (9k words), Paper 4 with the bifurcation figure. Shared preamble, BibLaTeX, no hard-coded section numbers.

**Weeks 7–8 — Human review.**
Two control/viability readers for P1; one assessment scientist for E1/ARV; one ecological-economics reader for ECOMOD/Paper 3. Post P1 and Paper 1-AS to arXiv.

**Weeks 9–12 — Respond, submit.**
Address human findings (expect them to differ in kind from the agent findings: scope, relevance, prior art); submit P1 (Automatica), Paper 1-AS (JMCDA SI, deadline 2027-01-31), ECOMOD (Ecological Modelling, with the response letter built from `response_to_human_reviewer.md`), E1 (IJF or Fisheries Research). Reorganise the repo per §5 in parallel; tag `programme-v2.0` with the consolidated set.

---

## 7. What I did not do, and what would sharpen this further

- I did not re-prove any theorem or rerun the verifier batteries; the Lean and Python layers appear well-built and I took their pass status at face value.
- I did not read E2–E4, the Edwards aquifer line, or the older `research_program/` A001–A025 articles beyond their indices.
- A line-by-line **dependency audit of the seven companions against v72** (§1.3 (b)) is the next concrete technical task and can be scripted (extract every `Abaee 2026b`/"Section 3.2"/theorem reference in the companions, map to v72 labels, flag hypothesis changes). I can do that as a follow-up if useful.
- A **word-budgeted outline** for any one of the consolidated papers (section → target words → what moves to SI) is the other follow-up that would convert this assessment into an executable plan.
