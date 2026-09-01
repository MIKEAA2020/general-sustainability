# Final Venue Pass (Turn 51)

**Scope.** Each of the nine manuscripts checked against its target venue's format requirements (per `journal-style-guide.md` and the papers' own style markers), with defects fixed where the fix is mechanical. Latest versions after this pass: P1 v7, P2 v4, P3 v7, P4 v8, P5 v8, E1 v6, E2 v9, E3 v6, E4 v7.

| Paper | Venue | Abstract | Keywords | Other venue extras | Status |
|---|---|---|---|---|---|
| P1 v7 | Set-Valued and Variational Analysis | 238 (150–250) ✓ | 6 ✓ + MSC line ✓ (49J53; 93B03; 91B76; 90B50) | "Statements and Declarations" section: the paper carries Data availability statement + Declaration of competing interest; the SVAA-specific merged block is a submission-step mechanical restructure | Ready apart from the declarations-block merge |
| P2 v4 | SVAA | 243 ✓ | 5 ✓ + MSC line ✓ (49J53; 93B03; 93C41; 91B76) | Declarations section already in SVAA form (Funding/Competing interests/Data/Code in one block) ✓ | **Venue-ready** |
| P3 v7 | Ecological Economics | 247 (≤250) ✓ | 7 ✓ (preserved) | Highlights (3–5 × ≤85 chars), graphical abstract, CRediT — submission-step metadata; data statement present ✓ | Ready apart from Highlights/CRediT metadata |
| P4 v8 | Ecological Modelling | 249 ✓ | 7 ✓ (added) | Highlights, graphical abstract, CRediT — submission-step metadata; Data availability present ✓ | Ready apart from Highlights/CRediT metadata |
| P5 v8 | ICES Journal of Marine Science | 300 (≤300) ✓ | 6 ✓ (added) | ICES skeleton already present (Data availability, Author contributions, Funding, Conflicts of interest) ✓ | **Venue-ready** |
| E1 v6 | Fisheries Research | 277 (≤300) ✓ | 5 ✓ (added) | Highlights + CRediT — submission-step metadata | Ready apart from Highlights/CRediT metadata |
| E2 v9 | Fisheries Research | 299 ✓ | 5 ✓ (added) | CRediT placeholder present ("to be completed at submission") ✓; Highlights to add at submission | Ready apart from Highlights |
| E3 v6 | Groundwater (Wiley/NGWA) | 261 ✓ | 5 ✓ (added) | **Groundwater requires a structured abstract (Problem/Approach/Results/Implications) and an Article Impact Statement** — both flagged as submission-step conversions, not done silently | Format conversion documented below |
| E4 v7 | Groundwater | 300 ✓ | 5 ✓ (added) | Same structured-abstract + impact-statement requirement | Format conversion documented below |

## What this pass executed (new versioned files; older versions untouched)

1. **Abstract caps** — P1 270→238, P3 314→247, P4 284→249, P5 341→300, E2 375→299. Wording-level trims only; every load-bearing claim, number, and caveat retained (diffs confined to the abstract paragraph). E4 sits exactly at the 300-word cap and was left (≤300 passes).
2. **Keyword blocks** — added to the seven papers that lacked them (venue-required for all nine): P2 (v4), P4, P5, E1 (v6), E2, E3, E4; P1/P3 keywords preserved through the abstract rewrite (a first-pass bug dropped them; caught and fixed before push). MSC classification lines added for the two SVAA papers.
3. **Manuscript-level artifact removal** — P4's "Registration note (v6)" title block removed (content folded into the Data availability statement in neutral form); in-body repo paths in P4 §7.1/§7.5 neutralized to deposited-material references; internal "wave-7" jargon removed from E2/E3/E4 data statements; P5's trailing "--" abstract artifact removed.
4. **Reference integrity** — all in-text citations across the nine papers resolve to reference-list entries (initial matcher flags verified as false positives one by one).

## Documented submission-step conversions (not executed — they are content-level restructures best done with the author at submission)

- **E3/E4 → Groundwater:** convert the abstract to the four-headed structured form (Problem; Approach; Results; Implications) within 250 words, and append an Article Impact Statement (one or two sentences on what the paper contributes to groundwater science/practice). The current abstracts carry all four components in prose; the conversion is a re-heading exercise with light edits.
- **EE/EM/FR metadata:** Highlights (3–5 bullets, ≤85 characters each), graphical abstract, CRediT author roles — standard Elsevier submission metadata, to be completed with author input.
- **SVAA declarations:** merge P1's Data availability and Declaration blocks into the journal's "Statements and Declarations" section (funding, competing interests, data availability) — mechanical.

## Registry VENUE-PASS items disposition

The wave-5/6/7 items classified VENUE-PASS (P1 minimax/game framing gloss; E1 h=5 persistence gloss; E3 persistence-win gloss; E4 transmissivity contrast; P3 I1/I2 framing; E4 "viability kernel" vocabulary; E3 companion-cod syntax pruning) remain optional one-sentence accessibility upgrades. This pass did not insert them: each is an interpretive gloss whose benefit is marginal against the risk of touching stable text in a final pass. They stay recorded as available micro-edits for the submission round.
