# P1 Journal Alignment — evaluation record (JMCDA target, JORS comparator)
# Task 119 / owner-directed venue alignment (2026-09-22)

This document is the evaluation record of the JMCDA alignment wave. It was
drafted from the venue research (Part A below); the owner's uploaded
inventory `batch 8/p1 journal alignment.txt` (252 lines, received mid-wave
via the repository) was then evaluated against the implemented set and the
strongest additional items adopted (Part B). The adopted set is implemented
as paper 1 v61 (batch 8/v61_jmcda_wave/).

Manuscript audited: paper1_assessment_separation_v60.tex (3,174 lines, 52 pp)
— the current head of the venue-neutral chain. Standing rules honored:
new version only (v61); no change-log/diary register in the manuscript; no
references to superseded versions; no over-hedging; no empirical claims;
companion-paper citations (DOIs / submitted status) remain correct; the
manuscript body never names a journal (venue fit is expressed by framing,
vocabulary, and declarations; the cover letter names the special issue).

---

# Part A — venue facts and the pre-upload suggestion inventory

## A.1 The venue facts (verified 2026-09-22)

- Journal: *Journal of Multi-Criteria Decision Analysis* (JMCDA), Wiley,
  launched 1992; an operations-research journal covering MCDA/MCDM theory,
  methodology, and application; the MCDM Society's journal.
- Special issue: **"Better Decisions for a Better Tomorrow: MCDM Approaches
  for Sustainability, Risk, and Complex Systems"** — open for submissions;
  **deadline 31 January 2027** (listed on the journal's Wiley home page;
  announced by the MCDM Society, 22 April 2026). The theme names exactly
  three constituencies: sustainability, risk, complex systems.
- Submission format: Wiley free-format submission (any reasonable format
  for initial review) — the elsarticle compilation chain is acceptable as
  is; the venue declaration line (\journal{}) makes the target explicit.
- Comparator: *Journal of the Operational Research Society* (JORS),
  Taylor & Francis — strong on practical OR, case studies, and practice
  papers; its theory strand accepts mathematical work but the house
  register favours demonstrated practice.

## A.2 Venue fit — verdict: STRONG for JMCDA (and the SI is exact)

The paper's central object — a quantifier-order separation between
compensatory (scalarized, per-weight-adaptive) and noncompensatory
(coordinate-wise, common-plan) acceptance of transitions — is an MCDA
result in substance: it is a statement about what a composite index can
and cannot certify under alternative aggregation semantics. The paper
already possesses the connective tissue: the keyword "multi-criteria
decision analysis"; the MCDM-first translation table (Section 5.3); the
compensability citations (Cinelli, Coles, and Kirwan, 2014; Schär, Pohl,
and Geldermann, 2025 — the latter a JMCDA paper); the weights-versus-
importance positioning against Becker et al. (2017); and the weight-space
robustness reading of the licensing thresholds.

Fit against the SI's three named themes, clause by clause:

| SI theme | Paper 1 anchor |
|---|---|
| Sustainability | The weak/strong sustainability doctrines are the canonical instances of the two operators; the benchmark is a regulated fishery transition anchored to a biomass limit reference point. |
| Risk | Robust transition-safety under worst-case disturbance tubes; the minimax/assessor–planner game reading; the here-and-now vs wait-and-see (adjustable robustness) identification; exact weight-space acceptance thresholds. |
| Complex systems | Finite-horizon transition dynamics with path-wise constraints, viability kernels, exact-tube semantics, regime structure (impossibility/rescue/fragile band), and the common-shock/coupled-shock regime analysis. |

JORS, by contrast, would want a demonstrated practical application
(its house strength); the paper's scope delimitations forbid empirical
claims, so a JORS-oriented re-orientation would fight the paper's design.
JORS remains a fallback venue only. This is why the strongest JORS-facing
suggestions are evaluated for what survives adaptation to JMCDA, not for
separate implementation.

## A.3 The pre-upload inventory (evaluated, strengthened, completed)

Each item: the suggestion, the evaluation, the strengthened/completed
form, and the adoption decision. ADOPTED items are in v61 (OP numbers).

### JMCDA suggestions

**S1 — Lead the framing with compensatory/noncompensatory aggregation.**
STRONG. Abstract re-cast so that compensatory and noncompensatory
aggregation name the assessment problem and the weak/strong sustainability
readings are its two instances; keywords re-ordered MCDA-first; the first
highlight bullet re-cast. ADOPTED (OPS 4–6; keywords refined to 7 per the
owner's checklist — OP 14).

**S2 — Anchor the introduction in the MCDA compensability canon.**
STRONG, with a completion gap (the foundational texts were missing). One
sentence in the commensurability-drift paragraph grounding the question in
multi-attribute value theory's substitution rates (Keeney and Raiffa,
1976), outranking's concordance/veto (Roy, 1996), and the decision-aiding
treatment of incommensurability in sustainable development (Munda, 2005);
"orthogonal to both" widened to "orthogonal to all of these". ADOPTED
(OP 7; references OP 12).

**S3 — State the acceptance-semantics (sorting) reading explicitly.**
STRONG — the single highest-value alignment move: re-titles the paper's
own protocol table in the venue's mother tongue without touching any
mathematics. A compact positioning paragraph in Section 5.2. ADOPTED
(OP 9).

**S4 — Promote the existing adjustable-robustness reading to first-class
positioning.** STRONG and cheap (the identification already exists inside
the blend-collapse remark). One sentence at the protocol introduction.
ADOPTED (OP 8).

**S5 — Make the weight-space robustness reading explicit.** Largely
already satisfied (the translation table maps the thresholds to
"weight-space robustness of a recommendation"); the useful residue folded
into S3. ADOPTED (inside OP 9; strengthened by OP 16).

**S6 — A three-constituency reading in the conclusions.** STRONG; the
material existed (the value-of-information reading; the per-floor
reporting consequence; Theorem 9/Proposition 10) but was never collected
per audience. A closing paragraph reading the results once per
literature, without naming any venue. ADOPTED (OP 10).

**S7 — Venue declaration, format, and cover letter.** \journal{}
declared (family precedent: the EMS variant); JEL apparatus retired (an
economics-venue artefact; JMCDA is an OR journal); SI-named cover letter.
Highlights retained (Wiley free format accepts them). ADOPTED (OPS 1–3,
13).

**S8 — Retitle MCDA-forward.** REJECTED. The current title already leads
with the composite-index object, and the cross-paper citation network
cites this title (ECOMOD's Abaee 2026b; the family's citation web) — a
retitle would cascade through the deposit-title network (the standing
Task-116 flag-2 cost) for marginal gain.

**S9 — Add MCDA/MCDM to the abbreviations list.** REJECTED — the
manuscript spells out "multi-criteria decision analysis" everywhere and
never uses the abbreviations; the list carries only abbreviated terms.

**S10 — Software/computational re-emphasis.** PARTIAL/NO CHANGE. The
verification discipline is a core contribution and stays; the
software-paper treatment belongs to the separate EMS-lineage manuscript;
the theory paper's balance is correct.

### JORS suggestions (evaluated for what survives adaptation to JMCDA)

**S11 — OR-translation emphasis: the finite-menu convex-hull geometry.**
The theorem and its statement are already in Section 4.4; the useful
residue is keeping the OR vocabulary visible in S3/S6. Absorbed (no
separate edit).

**S12 — Practice/case-study re-orientation.** REJECTED for the JMCDA
target — the scope delimitations are load-bearing; JMCDA's balance
accepts a verified benchmark as the applied anchor. JORS remains a
fallback whose practice orientation would require scope changes the owner
has excluded.

**S13 — Soften the mathematical register.** REJECTED. The verification
discipline is a distinguishing contribution; JMCDA publishes
mathematically rigorous MCDA theory; accessibility is already served by
the translation guide and the design tests.

---

# Part B — the owner's uploaded inventory, evaluated against the implemented set

The owner's file (252 lines; the same external-consultation genre as
`batch 8/paper 1 ecological indicators.txt`) confirms the venue decision
and adds a policy-critical requirement plus a delivery checklist. Its
suggestions, evaluated and reconciled (their headings, condensed):

**B1 — "Decision-making context" requirement (JMCDA editorial policy:
theoretical papers must be "well-motivated by explicit decision making
contexts"; "mere numerical examples ... will not typically be
sufficient").** EVALUATION: the strongest item in the file and the one
remaining gap after Part A's adoptions — v61's Part-A edits re-frame the
theory in MCDA terms, but the *applied anchor* (the fishery benchmark)
still opens in model terms ("an exact rational re-reading of the witness
datum in the language of a Schaefer (1954) production model"), not
decision terms. ADOPTED (OP 15): a decision-aiding-context paragraph at
the benchmark's opening stating the decision maker (the resource
authority), the decision alternatives (the menu's management schedules:
NO-SWITCH, FAST, SLOW, STAGED), the criteria (the two typed floors,
evaluated path-wise under the declared disturbance), the preference
reading of the weights, the acceptance gap as a robustness failure of
the decision-aiding process (in the precise sense of Theorem 5), the
analyst-communicable deliverables (the licensing thresholds as the
preference ranges over which each alternative is certified; the rescue
threshold as the adjustment funding), and the operational decision
relevance (the asymmetric allocations of the substitutability extension,
where the same total margin draws opposite verdicts and opposite
management responses). Scope-safe: descriptive framing of the existing
benchmark; the "no empirical claim" sentence directly precedes it.

**B2 — Terminology replacement throughout ("plans" → "alternatives",
"floors" → "criteria", "weights" → "preference weights").** EVALUATION:
REJECTED as a wholesale swap — it would overwrite the paper's established
technical vocabulary (typed floors, plan menu, tube semantics) that the
companion network and the deposit share, and "plan" is the precise object
(time-indexed management schedules), which the translation guide already
maps to "alternatives" for MCDA readers. PARTIALLY ABSORBED: OP 15's
decision-context paragraph uses the decision vocabulary (decision maker,
decision alternatives, criteria, preference orderings) exactly where it
is the right register, and OP 16 adds the preference reading of the
thresholds. The suggested abstract rewrites (both JORS and JMCDA
variants) are superseded by S1's re-cast, which preserves the paper's
register.

**B3 — Licensing thresholds as an MCDA deliverable ("preference ranges
for which a particular plan is robustly certified"; connect to
sensitivity analysis).** ADOPTED in strengthened form (OP 16): the
Section 5.2 acceptance-semantics sentence gains the clause "the
preference ranges over which each plan is certified" beside the
weight-sensitivity/Nardo analogue; OP 15 carries the deliverable reading
into the benchmark. A dedicated subsection + decision table evaluated
and NOT adopted: the paper already presents the thresholds with
Theorem 5(6), maps them in two translation tables (the main guide and
the benchmark's own table, "weight-ratio licensing intervals for the
pulse (FAST) and gradual (SLOW) quota plans"), and displays them in the
weight-intervals figure; a third presentation would be redundant.

**B4 — Engage the journal's own literature (Schär et al. 2025, PROMETHEE
compensability, JMCDA).** ALREADY SATISFIED AND STRENGTHENED: the paper
cited it before this wave; v61's new Section 5.2 paragraph makes the
contrast explicit (static compensability classification at a fixed
profile vs the protocol-level separation "one level up"). The suggested
discussion paragraph is that paragraph.

**B5 — Target the SI directly; cover letter; reproducibility;
implementation insight.** ALREADY SATISFIED: the SI-named cover letter
(OP 13) states the special issue, the three-theme fit, the exact-
arithmetic verification discipline, and the per-floor reporting
implementation insight.

**B6 — Delivery checklist: abstract ≤ 300 words (unstructured); up to
seven keywords; Data Availability Statement; SI selection by 31 January
2027.** EVALUATION: (i) Abstract: 266 words — compliant, no change.
(ii) Keywords: v61's Part-A list had nine — VIOLATES the seven-keyword
limit; ADOPTED (OP 14): trimmed to seven (multi-criteria decision
analysis; compensatory and noncompensatory aggregation; composite
indicators; scalarization; robustness; sustainability assessment;
transition safety — matching the original v60 count). (iii) Data
Availability: the Declarations carry the figshare statement — compliant.
(iv) SI selection: a submission-portal action, recorded in the cover
letter.

**B7 — JORS-side items (cite the JORS 2026 sustainability special issue
introduction, "Acquaye et al., 2026, JORS 77(1):8-42"; the ~5000-word
limit; code-deposit emphasis).** EVALUATION: (i) the JORS-SI citation is
REJECTED for the JMCDA target and RECORDED for any JORS rerouting, where
it must first be verified at source (the entry is cited from search
results, not yet checked against the journal); (ii) the word limit is a
JORS-rerouting constraint only (JMCDA has no strict limit); (iii)
code-deposit emphasis — already in the cover letter and Declarations.

**B8 — Reframing checklist table / submission order.** Confirms the
Part-A venue decision (JMCDA SI first, JORS as revision target). No
further manuscript action.

---

## The adopted set (implementation map for v61)

| OP | Site | Operation | Source |
|---|---|---|---|
| 1 | preamble | v61 provenance comment (+ v60 date correction) | S7 |
| 2 | preamble | \journal{Journal of Multi-Criteria Decision Analysis} | S7 |
| 3 | frontmatter | JEL apparatus retired | S7 |
| 4 | abstract | opening re-cast compensatory/noncompensatory-first | S1 |
| 5 | keywords | MCDA-first re-order + additions (7 keywords) | S1+B6 |
| 6 | highlights | bullet 1 re-cast | S1 |
| 7 | Section 1.1 | MCDA compensability canon + "orthogonal to all of these" | S2 |
| 8 | Section 1.2 | here-and-now vs wait-and-see sentence at the protocols | S4 |
| 9 | Section 5.2 | acceptance-semantics paragraph | S3+S5, absorbing S11 |
| 10 | Conclusions | three-constituency closing paragraph | S6 |
| 12 | References | + Keeney & Raiffa (1976); Munda (2005); Roy (1996); Vincke (1992) | S2 |
| 13 | latex folder | SI-named cover letter | S7+B5 |
| 14 | keywords | trimmed to seven (venue limit) | B6 |
| 15 | Section 6.3 | the decision-aiding-context paragraph at the benchmark | B1+B2+B3 |
| 16 | Section 5.2 | "preference ranges over which each plan is certified" clause | B3 |

Gates (v61): inverse reconstruction byte-exact; math-span multiset
UNCHANGED (1,470 → 1,470 — every operation is prose-level); marker
accounting; structure pins (environments and items unchanged); register
sweep (the v60 banned list plus venue register: no journal name in the
body); compile battery (tectonic in place, flat self-containment, PDF
text layer, VLM raster checks on the edited pages).

Reference-style note for the record: the four added references are
canonical and verified — Keeney, R. L., and Raiffa, H. (1976). *Decisions
with Multiple Objectives: Preferences and Value Tradeoffs*. Wiley, New
York; Munda, G. (2005). Multiple criteria decision analysis and
sustainable development. In: Figueira, Greco, and Ehrgott (eds.),
*Multiple Criteria Decision Analysis: State of the Art Surveys*, Springer,
953–986; Roy, B. (1996). *Multicriteria Methodology for Decision Aiding*.
Kluwer, Dordrecht; Vincke, P. (1992). *Multicriteria Decision-Aid*. Wiley,
Chichester.
