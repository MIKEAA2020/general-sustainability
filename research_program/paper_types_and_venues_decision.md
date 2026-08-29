# Paper Types and Venues Decision — The Nine-Paper Set, the Conditional Papers, and the Monograph

**Status:** Decision memo (programme-level planning document; not a manuscript). Resolves the open venue/type question across the whole publication architecture, triggered by the owner's request of 2026-08-29 and informed by (i) the external style review read in full (a shared DeepSeek conversation containing a full-paper rewrite and three rounds of parallel audits on the abstract's framing, the status ledger, the research-architecture section, and the overall genre), (ii) the existing `paper2_venue_and_split_recommendation.md` (2026-08-28), and (iii) a per-paper venue-fact scan of all nine final editions (abstracts, introductions, reference-list characters, apparatus burdens, lengths). **Decision owner:** programme owner; this memo records the evaluated recommendation and its implementation state. No theorem status, claim status, ledger row, or scored verdict is created, promoted, or demoted by anything in this memo.

---

## 1. The decision problem

Three coupled decisions, all recorded as open in the programme's registers:

1. **Paper type.** The external review's final joint diagnosis requires each paper to declare what kind of article it is (theory/methods, perspective/agenda, or standard contribution) before rewriting for a venue, because the three types produce three different papers from the same material.
2. **Venue.** No paper names a target journal; the only venue-adjacent commitments in the set are Paper 2's pre-authorized 2A/2B split trigger ("taken at venue-policy check, not now") and Paper 1's monograph-fallback rule.
3. **Edition architecture.** The external review's core criticism — that the programme's internal apparatus (claim ledgers, concordance statistics, publication roadmaps, edition notes, process vocabulary) reads as project documentation rather than journal prose — applies in varying degree to all five core papers and must be answered without losing the auditability discipline that is itself part of the programme's contribution.

The external review zoomed in on Paper 1. This memo evaluates the question against the entire project: five core papers, four scored empirical papers, two conditional papers, and the monograph.

## 2. Adjudication of the external review

The external review's findings, adjudicated:

**Accepted (and implemented for Paper 1 in its third edition, `manuscript_v3.md`):**
- *The framing risk.* Attributing "state spaces, proof obligations, failure modes" to sustainability practice reads as a strawman because the vocabulary is not the field's own; the terms must be positioned as this paper's analytical framework, not as a description of the field (implemented in the v3 abstract and §1.1).
- *The status ledger.* As a main-text evidentiary table it performs verification without doing it; "row-verified" is a bookkeeping label, not evidence. The discipline survives as a methodological commitment stated in prose; the inventory moves to an appendix/supplementary layer with concrete bases (section and proof locations, artifact pointers), a stipulation/validity legend, and the formal-validity-versus-empirical-applicability disclaimer (implemented as v3 Appendix A, Tables A1/A2).
- *The research-architecture section.* Publication roadmaps, concordance closure statistics, and unexecuted conjecture inventories do not belong in a journal body. Implemented in v3 as: a concrete reproducibility statement tied to this paper's own witness (§10), a condensed future-directions section with the full conjecture set in supplementary material (§11), and the series declaration compressed to §1.5.
- *Process vocabulary.* "row-verified", "in this edition", print-process and audit-file references removed from the v3 body; "flagship manuscript" renamed "programme manuscript".

**Accepted as a standing rule for the whole set (venue pass, per paper):** the same restructuring at each paper's venue pass — strip header edition notes, move ledgers to supplementary inventories with concrete bases, replace process vocabulary, resolve companion references to formal citations at publication.

**Rejected or modified (with reasons):**
- *Rewrite from scratch.* Rejected. The programme's non-loss rule and the pin discipline require transformation with verifiable provenance, not regeneration; the v3 build script (`reaudit/build_paper1_v3.py`) guarantees the §2–§9 bodies are byte-preserved and the apparatus relocated, not lost. The repo retains the internal editions as the auditable record; the journal-facing editions are additions, not replacements.
- *Delete the concordance and claim-status discipline from the paper.* Modified. The audits themselves concede the discipline is "a legitimate methodological contribution" and that at a methods/formal venue "a well-executed claim ledger could be a useful transparency device". The discipline stays as prose plus supplementary inventory; only its presentation changes.
- *Reframe Paper 1 as a Perspective/Research-Agenda article (their Option B).* Rejected (§3 below).
- *"Will not pass peer review at any mainstream sustainability science venue."* Accepted as a constraint on venue choice, not as a verdict on the science: it argues for methods/formal/computation-facing venues for the apparatus-bearing papers — which the reference-list characters independently support.

## 3. Paper-type decisions

| Paper | Type decision | Rationale (against the whole project) |
|---|---|---|
| **Paper 1** (typed architecture + separation theorem) | **Theory/methods article** (the review's Option A) | The executed substance is a formal framework plus a proved, machine-witnessed theorem; the falsification designs are already owned by Paper 5's layer, so an agenda-framed Paper 1 (Option B) would duplicate Paper 5's role and demote the executed mathematics; a single-result paper (Option C) would strip the architecture that the series navigation and the auditability contribution depend on. |
| **Paper 2** (theorem atlas) | **Mathematics article** (long-form, proofs in electronic supplementary material) | Pure-proof corpus; four external references, all mathematical; §15's own length constraint (≈27.2k words at full proof expansion) is handled by ESM packaging per the existing venue memo. |
| **Paper 3** (material ledgers and depletion diagnostics) | **Methods/formal-framework article** | Formal accounting representation with proved conservation/diagnostic theorems and attested-source application records; not an empirical assessment paper. |
| **Paper 4** (delay dynamics) | **Applied nonlinear-dynamics article** | Named RFDE systems, complete Hopf analysis, interval-certified crossings, fold-status discipline; explicitly non-empirical ("mathematical anchors"). |
| **Paper 5** (sampled governance, empirical identification, falsification design) | **Methodology + case-study article** | Sample-and-hold governance model plus screens plus the cod case at its exact causal status plus the falsification programme; the empirical tier is honest but nominal (code not committed) — a strengthening obligation registered below. |
| **E1/E3** (forecast ladders, cod / Edwards) | **Empirical forecast-evaluation articles** | Scored, protocol-dated, byte-reproducing comparisons against persistence baselines; negative-certificate results. |
| **E2/E4** (intervention selection, cod / Edwards) | **Applied management-analysis articles** (short) | Robust-kernel policy scoring on fixed measured series; the natural short-companion format to the ladder papers. |
| **Paper 6** (conditional) | Technical paper if the A021 gate closes; until then preprint/dossier | Standing rule unchanged. |
| **Paper 7** (conditional) | Supplement to Paper 4 unless it reaches independent scale | Standing rule unchanged. |
| **Monograph** | Research monograph after external scrutiny of the principal papers | Standing rule unchanged; the monograph is also the permanent carrier of the full apparatus (internal editions' content) and of the delegated B-1 families. |

## 4. Venue decisions

Primary route by contribution and referee competence, per the architecture's standing rule ("route by primary contribution and audience, not prestige alone"). Alternates are in submission order.

| Paper | Primary | Alternates | Fit notes and risks |
|---|---|---|---|
| **Paper 1** | **Environmental Modelling & Software** | Ecological Modelling; Ecological Economics (last, needs the strongest de-apparatusing) | The formal-framework-plus-machine-witness character fits EM&S's methods/open-science scope; its referees will not balk at formal notation, and the committed artifact apparatus is an asset there. Ecological Modelling is the natural modelling-science alternate. Ecological Economics is the disciplinary home of the weak/strong debate the theorem addresses (Neumayer/Ekins/Boos citations are native there) but its referees are the least formal — viable only with the v3 restructuring and a positioning section that leads with the doctrine debate. |
| **Paper 2** | **Set-Valued and Variational Analysis** | J. Mathematical Analysis and Applications; Mathematical Methods in the Applied Sciences (for a 2B half, only if the pre-authorized split fires) | Per `paper2_venue_and_split_recommendation.md`: SVVA is the viability/set-valued home territory; no split; ≈14–16k-word main text with ESM proofs; B-1 stays monograph-carried. This memo **endorses that recommendation unchanged**; owner ratification remains formally open (the register and obstacles documents still show the item open, and the packet pins them). |
| **Paper 3** | **Ecological Modelling** | Journal of Industrial Ecology; Environmental Modelling & Software | The typed-ledger representation with conservation theorems and first-passage surrogates fits formal ecological/resource modelling; JIE is the MFA-native audience for the no-compensation/no-double-counting discipline if the accounting framing leads; avoid stacking papers at EM&S beyond P1 unless scope clearly distinguishes them. |
| **Paper 4** | **Communications in Nonlinear Science and Numerical Simulation** | Nonlinear Dynamics; Journal of Economic Dynamics and Control (if the institutional-economics framing leads) | DDE Hopf/fold with validated numerics is the paper's distinctive register; CSNSNS and Nonlinear Dynamics referee it competently; JEDC is the disciplinary option for the institutional-dynamics framing but is weakest on the interval-certification register. |
| **Paper 5** | **ICES Journal of Marine Science** | Canadian Journal of Fisheries and Aquatic Sciences; Fisheries Research | The cod case, the RAM cohort screen, the MSE-shaped falsification designs, and the fisheries-assessment reference character point to the assessment-methods audience; CJFAS is the cod-native alternate. Register before submission: P5's computational record is nominal-tier (code not committed) — the one material strengthening obligation in the set. |
| **E1** (cod ladder) | **Fisheries Research** | ICES JMS; CJFAS | Forecast-evaluation methods with a clean negative result; Fisheries Research is friendly to assessment-adjacent methods and negative certificates; companion to E2 at the same venue family. |
| **E2** (cod intervention) | **Fisheries Research** (short communication) or ICES JMS research note | CJFAS | Short companion leg; the venue-pass must resolve its programme-source identifiers to published anchors (standing publication-time obligation). |
| **E3** (Edwards ladder) | **Groundwater** | Journal of Hydrology; Hydrogeology Journal | Aquifer head-forecast evaluation with dated pre-score protocol; Groundwater hosts applied forecasting and benchmark comparisons. Register before submission: the Edwards pair's reference lists are exclusively data agencies — journal-submission readiness requires engaging the peer-reviewed forecasting/groundwater-modelling literature (venue-pass item). |
| **E4** (Edwards intervention) | **Journal of Water Resources Planning and Management** | Water Resources Management; Water Resources Research | Drought triggers, critical-period management, and policy-family scoring are JWRPM-native; WRR is the research-register alternate. Same literature-engagement registration as E3. |

**Sequencing (unchanged from the release protocol, with the E-papers' independence made explicit):** Wave 1 = Papers 1–2 (the theory dyad) after their venue passes; Wave 2 = Papers 4, 3, 5 in readiness order; the four Wave E papers are citation-closed and may be venue-passed and submitted independently of the core papers' editorial stage — the cod pair before or alongside Paper 5 is the natural order, since Paper 5's §9 inherits the scored-forecast methodology the E legs execute. All programme-source identifier resolutions (E papers' "general theory §15", R03/R04, A014; core papers' "programme manuscript" anchors) remain the registered publication-time obligation: they resolve to the published sibling anchors, never to unpublished files.

## 5. The two-layer edition architecture (the answer to the genre criticism)

- **Internal editions** (`manuscript.md`, `manuscript_v2.md`) remain the programme's auditable record: full apparatus, edition notes, concordance statistics, pin discipline. Nothing is deleted; the non-loss rule holds at the repository level.
- **Journal-facing editions** (`manuscript_v3.md` and successors) carry the science verbatim with the apparatus restructured per §2: repositioned framing, appendix inventories with concrete bases, reproducibility statements tied to the paper's own artifacts, condensed future directions, no process vocabulary. Paper 1's v3 (2026-08-29) is the template; `reaudit/build_paper1_v3.py` is the provenance-preserving build, and `reaudit/verify_batch5_editions.py` pins the v3 file and checks its invariants (checks 9a–9t).
- **The other papers' v3 editions are produced at their own venue passes** (Paper 2's together with its SVVA template work and ESM packaging). Each will need the same per-paper care the consolidation scan gave the internal editions; the venue-pass register in `FINAL_EDITIONS_CONSOLIDATION_SCAN.md` §7 remains the working checklist, now with the genre items of this memo added.

## 6. Consequences register

1. **Implemented by this memo:** Paper 1's journal-facing third edition; the deep-scan record (`DEEP_SCAN_RESIDUAL_POINTS.md`); this decision memo; the verification extension and pin refresh.
2. **Registered, not executed now:** each remaining paper's v3 edition at its venue pass; E3/E4's peer-reviewed-literature engagement; P5's computational-tier strengthening (committing the screen code and outputs, or restating their status); the cross-paper house-style harmonizations (consolidation-scan register items 5–7).
3. **Owner-gated (unchanged):** PROOF_MANIFEST Part VI re-pin to the v2 editions (and later the v3 submission editions); B-1 register closure (this memo endorses the venue memo's "single-paper venue holds; monograph-carried" resolution — the register still shows it open pending the owner's ratification, and the packet pins the register); `remaining_obstacles_to_general_theory.md` priority item 7's venue clause (this memo supplies the decision that item awaited).
4. **Not changed anywhere:** theorem statuses, claim statuses, ledger rows, CC-identifier sets, scored verdicts, retention decisions, the 2A/2B split trigger (not fired), the monograph sequencing rule, and the publication-time citation-resolution obligations.

## 7. What this memo does not decide

It does not fabricate submission readiness: no paper is represented as formatted for, or submitted to, any venue; the venue rows above are the evaluated routing, to be executed per paper at its venue pass. It does not close the owner-gated items. It does not touch the first or second editions of any paper.
