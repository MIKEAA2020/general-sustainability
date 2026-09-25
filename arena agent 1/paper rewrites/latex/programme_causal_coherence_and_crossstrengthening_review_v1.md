# Programme-wide review — causal coherence, cross-strengthening, exposition

**Date:** September 25, 2026. **Scope:** all current editions on the board — P1 v53 (+ supp v51), comp v13, P3 v8, ws v13, minimax v5, ebc v5, ARV v5, E1 v54 (nine texs). **Method:** automated scans (dangling `\ref`/`\label` integrity, named-script existence, symbol-frequency tables, citation-string extraction) plus targeted reads of every abstract-level claim, all cross-citation sentences, and the shared-instance passages. No paper was edited; every defect below was verified against the shipped text before inclusion. Owner adjudication required before any repair round.

---

## 1. Causal-coherence scan

### 1.1 What is sound (verified)

- **Internal reference integrity: clean across all nine texs** — zero dangling `\ref`/`\label` pairs; no "?? " in the two builds checked this session (ws v13, comp v13, both byte-certified).
- **Cross-citation content accuracy where it matters most:** P3→P1 ("the probabilistic layer of the viability theory of Abaee (2026b)") is true — P1 carries the set-valued calculus P3 quantifies. ebc→P1 (antichain-over-lattice discipline) is true — P1's machinery is the cited discipline. comp→P1 (the backward recursion; certificates "whose firing proves nonviability") is true — the recursion phrase occurs 5× in P1. ws→P1, Theorem 1 is accurate — P1's first theorem is finite-horizon soundness and completeness, exactly the two-horizon-verdict ground ws cites it for. minimax→P1 is content-accurate: its "Theorem 2" is P1's common-action obstruction theorem and its "Open Problem 1" is P1's `op:dynamic`, correctly described as *not closed*.
- **Shared-instance constants are byte-consistent across papers:** the caps-fibre numbers (Y\* = 27/5; caps 3/2 − (Y−2)/10 and 59/50 − (Y−2)/10; cap sum 47/25 at Y = 6; witness (6/5, 4/5); dual (1/2, 1/2); margin 3/50) are identical in ws `prop:bench`, minimax `thm:benchmark`, and comp's library identity. No numeric drift has crept in across the three carriers.
- **The verification culture is family-wide and honest:** every paper has a Verification-methods section; every named verifier exists in the folder except the two pointer defects below (D4, D5); the scoping discipline ("What else is not claimed", "Scope delimitations", "Delimitations") is present in all eight — minimax correctly leaves the dynamic completeness gap open rather than claiming it.
- **Mechanism-backed causal claims:** each paper's headline causal statement is carried by a mechanism, not a correlation — comp's obstruction is the decoded braking-liability-vs-authority identity (now with exact rates), ws's chain is monotonicity → strictness → stationary-policy characterization → factoring (all script-certified), P1's certificates fire on identified quantifier-order mechanisms with a coverage audit showing exactly which certificate covers which cell, and the applied pair rests on archived data with exact recomputation.

### 1.2 Defects and risks (ranked; each verified against the shipped text)

**D1 — minimax v5 has no reference list.** The paper cites "(Abaee 2026a, Section 3.2)", "(Abaee 2026a, Theorem 2; Abaee 2026b)", "(Abaee 2026a, Open Problem 1)" and "the applications companion" — with no bibliography resolving any of them. This violates the family's self-containment + proper-citation constraint. Content-wise the targets are identifiable (2026a = P1: the two-floor instance, Theorem 2 = `thm:common-action`, Open Problem 1 = `op:dynamic`; "applications companion" = ARV), so the repair is mechanical: add the reference list and key the citations.

**D2 — the caps-fibre benchmark is a duplicated theorem.** ws `prop:bench` (exact benchmark crossover) and minimax `thm:benchmark` (critical aggregate) state the same theorem with identical constants, the same witness, the same dual measure, the same margin — and neither cites the other; minimax's only pointer is to P1 for a different object. Each side carries genuinely complementary content: minimax derives the caps from a two-stock resource model (r₁ = 1, r₂ = 4/5, K₁ = K₂ = 10, cross-competition 1/20, floors xᵢ ≥ 2, shocks |dᵢ| ≤ 1/10) and adds the fibre-width formula Δx₁(Y) = Y − 4; ws adds the per-aggregate audit table and the radius/robustness reading (`prop:margins` i). As shipped, a reader of both papers meets two independent-looking ownership claims of one result — the duplication/self-plagiarism hazard, live. Repair is a split decision: one owner for the fibre theorem (the audit lineage suggests ws), one owner for the two-stock derivation and fibre width (minimax), each citing the other for exactly its part.

**D3 — comp's library self-test cites the wrong companions for the worked-systems identities.** The twelve audited identities (kernel counts 24/26/25/28, census 15 total / 7 adequate, benchmark Y\* = 27/5, drift bounds 21/100 and 0, the 48-cell boundary cell, witnesses) are the worked-systems line's audited results; comp cites them to "(Abaee, 2026a, 2026b)" = the ARV Zenodo deposit and P1. P1 carries the 48-cell coverage audit on the same hidden-regime system but not the kernel counts, census, or benchmark; ARV carries neither. The worked-systems companion is absent from comp's bibliography. The rank-section sentence "a scoping caveat of the finite audits of Abaee (2026a)" has the same problem. Repair: add ws to comp's reference list; cite it for those identities; keep 2026b for the recursion and fibre criteria.

**D4 — minimax v5's code-availability pointer is stale:** it names `minimax_dual_certificates_v4_verify.py` and "all eight check families"; the current edition is v5 with its own verifier (`minimax_dual_certificates_v5_verify.py`, 23 checks). Replication instructions point at the superseded script.

**D5 — E1 v54's replication pointers and submission stubs.** The verbatim block `python3 src/run_ladder.py && …` names six scripts that exist in the repository archive but not at the path a reader would infer (they live under the `wave_e_edwards/src/` archive tree, unlabelled in the paper); the main sections' verifier `paperE1_cod_forecast_ladder_v54_verification.py` exists and is correct. CRediT and Funding still read "[To be completed at submission.]".

**D6 — author-year letter assignments are inconsistent across the family.** The same root paper (P1) is "2026b" in comp, ws, P3, and ebc, but "2026a" in minimax. E1's "2026a/2026b" are two entirely different deposits (Edwards one-pool; periodic-review screen). Each paper is self-contained, so journals see no error — but a family reader meets three different denotations of "Abaee 2026a". A one-time family-wide keying convention (e.g., 2026a = P1 everywhere, then alphabetical by first ship date) would remove a standing comprehension tax; it touches reference lists only.

**D7 — minimax register and markup.** (a) "The corrected object" (section title) and "the corrected formulation / the lemma of the corrected formulation" narrate the paper's own revision history — the earlier-mistake-narration pattern the standing register constraint removes; content-true names ("the envelope", "the residue formulation") exist. (b) `\section{What else is not claimed}\section*{Declarations}` are two headings on one source line (renders, but is fragile). (c) The AI declaration names specific models while the other papers use the responsibility wording — a family-format divergence to reconcile under the AI-disclosure constraint.

**D8 — carried causal-provenance tails (already queued, reaffirmed as the applied line's open coherence items):** F11 LRP provenance (the 1983 SSB 884.6 candidate), F15 xteNCAM Blim circularity (250–289 partial), and the fable SSB-timing note in E1. These are the only places where a number's causal chain still terminates in an unresolved provenance question.

---

## 2. Genuine cross-strengthening (non-decorative, no duplication)

The test applied to each candidate: *both* sides must gain verifiable content, nothing may move between papers as shared prose, and every lend must be a citation or a schema — never a copied passage.

**S1 (mandatory, before all): repair D2 and D3.** Ownership + citation is itself the strongest available "lend": the caps theorem's two halves (fibre theorem vs two-stock derivation + fibre width) fit each paper's mandate precisely once cross-cited; comp's library becomes a true index of the family's audits once ws is in its bibliography. No new text beyond citation keys and one clause each.

**S2 — a certificate exchange schema across comp, minimax, ws (execute comp's recorded direction).** All three papers already emit exact dual objects: minimax's measure dual μ\* with margin ε, comp's Farkas witnesses (λ, η, μ) with exact margins, ws's dual measures on floor atoms. comp's methods already record the independent certificate-file parser as its next step; minimax's conclusion already names "the certificate file as the exchange format". The genuine upgrade: one schema, one parser, and one *cross-parsed* witness per paper — comp's parser reads a minimax dual certificate and reproduces its margin exactly, and vice versa. This makes the papers' verifiers mutually checkable — a property none of them has alone — without a word of shared prose. ARV's band certificates are the natural applied case study for the same parser.

**S3 — ebc ↔ comp belief cells.** comp v13's `prop:beliefcells` prices certified belief cells by radius; ebc computes exact belief-state values on the cube where "the structure changes" (Hamming adjacency, antichains). Genuine lend, both directions: ebc's exact evaluations are the validity check for comp's cell-supremum labels on a belief geometry far from the three-branch instance (singleton cells = ebc's stored sets, so agreement is checkable exactly); comp's radius law gives ebc's point-based four-parameter evaluations a certified perturbation margin — currently ebc states exactness at parameters, not stability around them. One joint instance-level check, cited both ways, would be theorem-grade rather than decorative.

**S4 — the refinement-axis bridge, one sentence each.** ws's master monotonicity (observations, policies, memory axes) and comp's completeness-under-refinement (mesh, stored-scenario, and now belief-cell axes) are the two halves of one statement the family never quite makes: every refinement axis the programme owns enlarges a kernel or tightens a sandwich, and positivity is non-monotone on both sides (ws's strict-difference pairs; comp's erosion identity (12)). One accurate sentence per paper, citing the other, no more — the temptation to write a joint "refinement calculus" paper should be resisted until a theorem exists that neither side can state alone.

**S5 — minimax residue ↔ P3 distributionally-robust layer (scoped investigation, not a shipped sentence).** minimax's residue is a coupling-selection problem over adversarial priors; P3's §Distributionally robust interpolation already controls the mixture family (1 − ρ)p + ρr. The genuine question: does P3's solvable interpolation family contain a tractable special case of the coupling-selection residue (or exhibit the obstruction to it)? If yes, P3 gains a dynamic-certificate application and minimax's conjecture gains a proved island. This needs a per-case computation before any claim — recommended as a next-round investigation, explicitly not as a cross-citation now.

**S6 — applied ↔ theory: methodological lend only, and that is the honest verdict.** ARV and E1 are data-provenance papers; importing viability theorems into their results sections would be decorative. Two optional, genuine, single-citation items: E1's discussion may cite P1's delayed-information theorem as the formal statement of the recognition-time mechanism its panel documents (E1 currently cites neither P1 nor ARV — the asymmetry with ARV→E1 is real); ARV's band certificates can serve as S2's applied case study. Nothing else clears the bar.

**What not to do:** shared or merged introductions; importing instances across papers (the three-branch stays comp's, the cube ebc's, the caps fibre single-owned per S1); renaming shipped notation family-wide (churn without comprehension gain — per-paper tables instead, §3 below); citing siblings for content already cited to their own verification sections.

---

## 3. Presentation, structure, alignment, exposition, pedagogy

**3.1 The single largest lever: a family reader's map + a per-paper notation table.** The programme is eight papers with a definite shape — root calculus (P1), computational bridge (comp), worked-audit layer (ws), probabilistic layer (P3), exact-computation layer (ebc), dual/unification layer (minimax), applied pair (ARV, E1) — and no paper states it. Two artefacts fix this without meta-commentary: (a) one self-contained "position among the companion papers" paragraph per paper (citation-based, no process language); (b) a short "Shared symbols" table in each paper's notation section, because the scan documents real collisions:

| Glyph | P1 | ws | comp | P3 | minimax | ARV |
|---|---|---|---|---|---|---|
| τ\* | — | worst-case exit time τ\*(z₀) | critical delay 7/50 | — | — | — |
| Γ | obstruction functional | — | certificate value Γ(λ, a) | action correspondences Γˢₖ(b) | support function Γ_h | — |
| λ | selector weights | pooling weights | witness weights | — | dual multipliers | — |
| μ | — | — | input-facet multipliers | — | adversarial prior μ\* (59 uses) | — |
| K | kernel/information set | kernels 𝒦 (36-pair) | label set 𝒮_G context | — | carrying capacity Kᵢ **and** kernel 𝒦(B) **and** K-node tree | — |
| ρ | — | — | LP value ρ | mixture parameter ρ | — | net multiplier ρ (demographic) |
| β | — | — | row labels β_a | — | — | — |

minimax alone uses K three ways internally — worth a local clarification regardless of family policy. These are locally defined everywhere (no error), but a reader traversing the family pays the disambiguation cost every time; the table repays it.

**3.2 Structural notes, per paper.** *minimax* buries its strongest result: the measure-dual unification is the paper's theorem, but it arrives after the candidate-failure narration; reorder so §2 states the dual theorem first and the "three obstructions to the candidate" becomes the motivation subsection (this also dovetails with the D7 register fix). *P1* is excellent but long; its §9 case study is the pedagogical entry point and deserves a roadmap sentence in the introduction ("the reader wanting a worked entry point may begin at §9") — a comprehension gain at zero length cost. *comp* and *ws* read well as shipped; comp's "Instance arithmetic, collected" subsection is the family's best exposition device and should be imitated where a section accumulates identities (ws's benchmark section and minimax's benchmark are natural candidates). *E1* has Highlights and a clean IMRaD; its remaining gaps are the D5 pointers/stubs.

**3.3 Uniform verification reporting.** The family nearly has a house style — script name, check count, arithmetic class, "solver outputs are confirmations, never proof objects". Make the triple (script · count · arithmetic) typographically uniform in all eight Verification sections; E1's two-tier wording (archival scripts vs verification script) is the one outlier to align.

**3.4 Keep-list (working devices, do not regress):** P1's coverage-audit table (certificate-coverage symbols per cell); comp's collected-arithmetic subsections and its "falsified variants" displays (the 2719/1250 and 2501/1250 entries teach more than the corrected policy alone); ws's master table with its column-keyed counts; minimax's "What else is not claimed"; the scoping sections everywhere. These are the family's pedagogical signature.

---

## 4. Recommended sequence (owner to adjudicate)

1. **Repair round (mechanical, high-priority):** D1–D7 as one minimax v6 + comp v14 + E1 v55 + reference-keying pass; verifiers re-run; build/push gates per discipline.
2. **S2 certificate schema:** comp parser + one cross-parsed witness per theory paper (comp's recorded direction; minimax's stated prerequisite).
3. **S3 ebc↔comp joint instance check** (exact, small, cited both ways).
4. **S5 residue↔DR investigation** (compute first; ship only if a theorem or exact counterexample emerges).
5. **S4/S6 single-sentence bridges** with the applied pair, if wanted.
6. **Carried:** F11, F15, fable SSB-timing, opus U3+, §D CSAS web attempt.

No file was modified and nothing was pushed: every item above is an adjudication input. On your call, items 1 (and any of 2–5) become the next round.
