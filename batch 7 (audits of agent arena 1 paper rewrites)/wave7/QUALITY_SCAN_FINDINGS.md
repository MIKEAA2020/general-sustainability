# Wave 7 — Parts 2 & 3: Full-Paper Quality Scan Findings and Dispositions (Task 77, 2026-09-08)

**Owner instruction:** *Scan all papers for conceptual clarity, seamless flow, remnants and redundancy; scan all
papers for consistent terminology, stylistic writing and syntax.*

## Method

Four parallel full-read passes (Task IDs 77-c: E1–E4; 77-d: P1+P2; 77-e: P3; 77-f: P4+P5) read every line of the
nine finals, plus cross-reference integrity skims of the current supplementaries (paper1_supplementary_v2,
paper3_supplementary_v7, paper4_supplementary_v4, paper5_supplementary_v5). A mechanical remnant battery
(retired-vocabulary greps per paper) was run centrally. Every candidate finding was adjudicated here; the
accepted set was implemented in the nine fail-loud builds of WAVE7_IMPLEMENTATION.md.

## Dispositions per paper (implemented / declined-with-reason)

### E1 (v12 → v13) — 13 findings, 11 implemented, 2 declined
- **Implemented:** the dangling "critical-zone vocabulary used below" clause (shared-text remnant — no such
  vocabulary occurs in E1); the §1 roadmap extended to §3.5/§3.6 (post-freeze layers never announced); the
  recovery-window "SSE 128.35/127.84" labels corrected to MSE (the printed training-RMSE pair 11.29–12.24 kt
  squares exactly to 127.4–149.9 — the same label class E2 fixed at v18; values untouched; the §3.2 site and
  the two Table 10 cells); §4's duplicated "(694 of 713 kt)" clause and duplicated crash-explanation clause;
  §4's 600-word paragraph split at the predictand and log-RMSE boundaries; reference hygiene (DFO 2024a/2024b
  disambiguation with the in-text site updated; the never-cited DFO 2010 entry dropped — no attribution site
  exists; the NAFC 2025 dataset entry cited at its two Zenodo sites; Cadigan 2016 — the NCAM model paper —
  cited in Table 1's caption).
- **Declined:** the alternative-comparator evidential gap (the M2–M1b margins: verified exactly against the
  archived campaign CSV — A,1 p=0.707; B,1 p=0.770; A,5 p=0.807; B,5 p=0.0048 ≈ the printed 0.005 — and the
  archive pointer already sits one sentence later); the §2.2-vs-§3.2 K-bound fence (the pointer chain already
  exists: §2.2's Table-10 pointer + §3.6's "neither is reconciled here" note). Registered, not edited: the
  mixed §/Section parenthetical style (churn); the Spec-B integer precision (reflects Table 4's printed forms).

### E2 (v19 → v20) — 17 findings, 15 implemented, 2 declined
- **Implemented:** the unbalanced parenthesis (Data availability); "the Section 3.8 breakpoint test" renamed
  to its object (the 1992 one-off sensitivity); "Three consequences" → four; the "three classes" enumerated;
  §3.11's comparison table captioned (Table 6) and referenced; the §1 roadmap re-named to the current result
  objects (the no-dominance verdict and the vacuous-class identity, not "the two negative certificates") and
  the 3.6–3.11 layers; two "order 80–90 kt" prints harmonised to the settled 70–90 reading (v14-era remnants);
  **two form-sensitivity claims corrected to the post-v15 class story** (Result 3.6's statement and the §4
  sentence — the 5th-percentile class is informative on the registered form, the depensatory restoration is
  at the perpetual-worst class; the §4 sentence had the two halves inverted); the one-off "productivity
  certificate" renamed; Table 2's "Committed Schaefer" harmonised to "Registered Schaefer"; the "frozen
  source-year" collocations fixed (2); the rejected-designs pointer fixed (2); the T=5 built-in check pointed
  at the archived kernel table; the upper-edge sentence's inverted logic reworded; three unspaced em-dashes;
  the Regular et al. (2025) entry added (cited in §3.11, absent from the list).
- **Declined:** the g_max precision trio (296/296.1/296.09 — different print contexts, no declared
  significant-digit convention); the §3.6 12-value roadmap granularity (covered by the roadmap fix).

### E3 (v13 → v14) — 11 findings, 9 implemented, 2 declined
- **Implemented:** Table 7's "M2m (the declined gate)" row label corrected to "the declined nested baseline"
  (a v12-renumbering casualty — the caption already carries the corrected vocabulary); the stale "Tables 4
  and 6" pointer → 4 and 7; the false "Table 3 footnote" pointer dropped; the restored post-2007 RMSE ranking
  attributed (persistence 13.09, M1 12.16, M2 13.31, oracle 8.03 ft — M2's 13.31 verified against the committed
  rolling_modern_2007.csv); the duplicated companion citation deduplicated; the never-cited, internally
  mismatched Author-B entry dropped (its descriptor names the groundwater intervention while its label names
  the cod study; the text cites only the forecast companion); the duplicated predictand sentence dropped with
  the TWDB/NSE glosses added to the field-types note; the deduplicated replication pointer; "321 kaf" written
  in the paper's unit convention.
- **Declined:** the §1/§6 two-pool clause pair (each serves its section's local scoping); the abstract's
  citation density (not an issue found — no action needed).

### E4 (v11 → v12) — 10 findings, 9 implemented, 1 declined
- **Implemented:** **the mirror-verdict swap corrected** (the Introduction said "reactive rules retained
  there, none retained here" — exactly backwards against both papers' records: the cod companion retains
  nothing; the aquifer retains the reactive rules nominally; the Discussion's own sentence and the mechanism
  clause were already correct); the perpetual-floors pointer corrected to §2.2; "the observed maximum annual
  mean (692.7 ft)" corrected to the record value 691.96 ft (the 1992 mean, verified against the committed
  annual panel; the 12.0-yr ceiling arithmetic unchanged at 11.98 yr); the bootstrap sentence's gap
  coordinated with its numbers; **the tables renumbered into order of appearance** (captions and in-text
  tokens; the EAA's external Table-1 references untouched; all table bodies byte-identical); the BAU alias
  declaration extended to running prose; "about 31%" → "about 31.5%" (4); "demand-management policy" →
  "positive-pumping policy" (2); "the preregistration record" → the family's "frozen-protocol record"; the
  Critical-Period EAA entry and Puente (1978) cited.
- **Declined:** none beyond the recorded scope (the stage-V/CPM institutional questions remain the audits'
  domain, not the scan's).

### P1 (v20 → v21) — 18 findings, 17 implemented, 1 declined
- **Implemented:** §5.2(vii)'s degraded "menu convexification of the menu" restored to §1.3's "witness menu"
  parallel; the abstract's "artefact" spelling and "open interior" → "relative interior" (word-count
  preserving, 298 pinned); Theorem 5(4)'s "open interior (in the state space)" corrected to "relative interior
  (in the q=0 slice)" — the proof's own term; §2.8's W-fence corrected (the cone is W₊; subfamilies W) and
  §1.3(i)'s display written over W₊; the §1.3 novelty paragraph trimmed to one sentence with a §5.2 pointer;
  the §4.11 tombstone unified; four "tuple" stragglers → "record"; the "four-symbol display" corrected to the
  two symbols; "price family" harmonised to "weight family" (4 sites); the §1.1 operator pointer corrected
  (Section 3.1); the quantifier-fact sentence reworded (action-set identity; Remark 1 once); "twenty-five" →
  "25"; "now explicit" → "explicit"; Daly (1990) cited at the strong-sustainability sentence and refiled to
  alphabetical position; the supplementary's S1 opening re-lettered to the named record 𝔖 and S6's retired r*
  → κ* (with a revision note appended).
- **Declined:** the §1.1 answer-precedes-question order (paragraph move = restructure-scale on a §1.1 the
  wave-4 build just rebuilt; the summary-then-question convention is a defensible register).

### P2 (v10 → v11) — 16 findings, 15 implemented, 1 declined
- **Implemented:** the finite/checkable classification corrected (Theorems 3 and 5 are the finite forms; the
  definition's "finite, checkable" scoped); the abstract's mechanism count corrected (two finitely checkable
  + two closed-form conditional + one construction — not "four as finite objects"); three "empties a nonempty
  perfect-information kernel" compressions corrected to the precise form (the abstract's CE-trap sentence,
  §1.1 item 6, the Bias paragraph); Theorem 1's proof meta-narration dropped (the mathematical statement
  kept); §2.4's "(re-lettered … at this revision)" and Remark 1's "(recorded at this revision)" dropped; the
  §4.3 Viab display written in the declared signature Viab(V; U, Π_CE); λ added to the local-scope fence;
  "full-information viability certification" → robust; the certainly-safe apposition fixed; the
  zero-margin/tube-safety relationship restructured; "the following remark" → the tube-safety form; "Each
  certificate identifies" scoped; the §6.5 literature sentence's dangling apposition given a verb; the UK
  spellings harmonised (realised/organise/labelled ×2).
- **Declined:** the §5(d) Farkas symbol definitions (needs the companion's notation — registered; the
  local-scope fence extension covers the collision); the §2.4 Viab(V) shorthand (one-site abbreviation).

### P3 (v29 → v30) — 30 findings, 20 implemented, 10 declined
- **Implemented:** the Daly (1990) entry added (cited at two sites, absent from the list); "supporting pool"
  harmonised (2 sites); the §1.1 spelled-out magnitudes in numeral+kt form; the notation-table B-row scoping
  corrected; §2.4's local-notation parenthetical extended (S, P); q glossed at the closed block; H^win_GW
  glossed at first use; the recharge-law table's companion pointer disambiguated; ADH/SSB/F/USGS/MCS expanded
  at first use; the two §-form prose references spelled out; the self-referential §6.5.2 pointer re-aimed;
  the two "this file's" referents corrected to the supplementary's; the curly quotes straightened; the
  Ayres/Daly attributed phrases de-quoted; the "2025 world production column" named as the pinned source's;
  six echo-redundancy trims (each a verbatim repeat carried elsewhere: §3.1's litany → §1.1 pointer; §1.1's
  end-of-paragraph restatement; the dagger note's duplicate sentence; §10.1's repeated maxim; §11's repeated
  usable/false sentence; §4's double announcement); the §6.5.2 fisheries paragraph split at the provenance
  boundary.
- **Declined with reasons:** the fisheries paragraph's internal repetition trims (each "repeat" carries a
  distinct vintage-pinning caveat; the v28-built disclosure record stands); the §1.1 renewal-enumeration pair
  (different scopes: the three-scale list vs the human-timescale scoping); §11's closing statement (deliberate
  rhetoric — the paper's designed closer); the four-driver enumeration trio (each site a distinct argument:
  classification, premises, pinning); the registered length reduction (standing decline).

### P4 (v27 → v28) — 18 findings, 17 implemented, 1 declined
- **Implemented:** the "labled" typo; "Section 4.1" → Theorem 4.1 (the recurrent-branch statement);
  §9.2's duplicate multiplier restatement and both in-body version-log pointers dropped; §9.5's duplicate
  onset sentence dropped; §9.6's inline off-by-one parenthetical trimmed (the dedicated flag paragraph
  carries it) and "Correcting the earlier status:" → "Status:"; Figure 1 cited from the topology paragraph;
  §2.4's τ_m sentence reworded ("never share a letter" was literally false); Corollary 2.1's ν(t) site-local
  note; §1.2's convention named in the flow-then-update form; the ζ/ς mapping moved before the values it
  explains; "the classified six" named; the Aiello & Freedman entry refiled to alphabetical position; the
  journal abbreviation harmonised; the supplementary paragraph's "wave-4" process tag dropped, the S3
  description scoped to the open continuum routes, and S10's pre-v25 labels mapped; **the supplementary's S12
  appended** (the S3 pre-rebuild status note — items (i)/(iii) resolved at the discrete level by the §9.2
  certificates; (ii)/(iv)/(v) open — and the pre-v25 statement-label mapping).
- **Declined:** the S1 four-way enclosure table (would add content to a frozen supplementary section; the
  main-text pointer now scopes what S1 carries).

### P5 (v22 → v23) — 15 findings, 13 implemented, 2 declined
- **Implemented:** **the one-plant operator contrast corrected against the companion's declared orientation**
  (the certified window (3.666, 150.358) yr is the delay-stabilised window of an undelayed-unstable loop; the
  earlier text had read it as a delay-destabilised window, inverting the continuous-delay stability at
  τ = 1 yr and manufacturing the recorded zero-delay tension — no frozen record of this paper changes); the
  undelayed-limit reconciliation re-scoped (the companion's undelayed Routh–Hurwitz record fixes λ > 0; the
  records close at the zero-delay limit; the operator difference is the edge contrast); the abstract's garbled
  crossing clause ("the annual-review equilibrium crosses the unit circle" → "equilibrium multipliers cross
  the unit circle at a review interval"); the duplicated δ/δ₀ distinction dropped from the Notation; "no
  symbol serves two sorts" → "no other symbol"; Table 3's η descriptor harmonised to "effort-response
  coefficient"; the duplicated em-dash clause deleted; the q-referent clarified; "[6.50, 200+] yr" → the
  tested range; the crossing record cites Figure 1; the Benjamini–Yekutieli fallback cited with its reference
  entry added.
- **Declined:** the crossing-value precision harmonisation (rounded narrative forms alongside the
  complete-record forms are the paper's declared convention); the "exact-hold" label family (anchored at
  first use; each label resolves). Registered: the S2 supplementary glosses' drift (τ_m "measurement delay"
  vs the main text's "memory-filter timescale"; E_max) — the supplementary in-place edits were out of scope
  for this wave; noted for the next allowed supplementary pass.

## Mechanical-battery results (post-build re-run)

All retired-vocabulary greps return zero body hits (the only survivors are the version-log disclosures);
no doubled words, no double spaces, no unbalanced delimiters (E2's was the one, now closed), consistent
e.g./i.e./et al. per paper, no §/Section mixing in P3/P4/P5 prose (E1's mixed parenthetical style registered),
and every table row byte-identical except the seven disclosed label cells (E1 Table 10 ×2 SSE→MSE; E2 Table 2
Committed→Registered; E3 Table 7 row label; E4's renumbered captions; P5 Table 3's η descriptor; P3's
notation-table scoping cells ×2).
