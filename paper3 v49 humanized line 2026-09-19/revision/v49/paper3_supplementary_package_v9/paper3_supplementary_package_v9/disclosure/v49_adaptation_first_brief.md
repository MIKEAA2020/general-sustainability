# v49 brief - adaptation-first build (decided 2026-09-19, **not started**)

> **Status: HOLD.** The author chose the approach and said "wait for my next prompt before starting". Nothing in
> `revision/v49` exists yet and no manuscript file has been touched since that instruction. This page is the plan,
> so that the run can start from a standing position.

## The two decisions

1. **Base swap.** The document of record for v49's *prose* is the adaptation in `uploads/p3 humanized.txt`,
   `gemini:` half (lines 1–1242; the file's second half from line 1243 is a `grok:` response and is not the target).
   v48 is built the other way round - deposit first, restyled - and that is why its §1.1 measures 0.084 similar to
   the adaptation against 0.437 to the deposit, 32.9 words a sentence against 21.1.
2. **The verbatim ruling is waived for the front matter only.** The 290-row ruling keeps protecting the 222 rows
   outside §1 verbatim; the 68 rows inside §1 (of which 63 are currently placed verbatim) become rewordable, so the
   abstract and §1 can take the adaptation's phrasing. Ids: `D0042 D0046 D0049–D0053 D0056–D0061 D0064 D0065
   D0070–D0072 D0074–D0077 D0087 D0089 D0090 D0097–D0100 D0102–D0105 D0108 D0110–D0114 D0118–D0120 D0122 D0124
   D0129 D0131 D0132 D0138 D0139 D0142–D0144 D0148 D0150–D0156 D0158–D0160 D0162 D0165–D0168` (authoritative list:
   `revision/v48/v48_reuse_split.json`, rows whose `section` begins with `1.`). Note `D0089` is the row the figure
   guard refused in v48, and `v48_overrules.csv` (16 rows) is the set already regenerated against a recorded
   recommendation.

## Why this is a return to a plan, not a new idea

`review/joint_evaluation_v1.md` §6 (2026-09-14) already agreed the architecture: "**A's text for every
status-bearing sentence; F for voice and the two genuinely better passages; E for the abstract, the reader's box,
and the sentence-length programme; G's six rules as the acceptance gate; D's E1–E8 as the fix list that must not be
lost**", and it is headed "*still not executed*". v48 executed a narrower thing - deposit + register pass + ruling -
which is why the P2 target in that same section ("split every sentence >45 words, target ≤22 w mean, keep F's
em-dash economy") was never met: v47 reached 21.8 on `stylekit_v1`'s distance and the splice pushed v48 back to
28.6. v49 = execute §6, with the §1 waiver above added.

## What has to be repaired in the adaptation before it can be the base

The adaptation is not submittable as it stands; those findings are the reason v48 was built from the deposit. Full
list in `review/joint_evaluation_v1.md` §6 P0–P3. In short, against the deposit as oracle:

* **strip** the `gemini:`/chat residue, the duplicated second copy of abstract+§1 at the tail (its 84.6% self-copy
  rate), the fenced ASCII diagrams, and its mixed `\( \)` / `$$` delimiters - it does not compile as supplied;
* **delete** the four assertions the deposit does not support: "engineered to capture", F's routing rule
  ("Routing is determined by…" against the deposit's "routing is never determined"), "artificially thresholded",
  "satellite-derived masks"; also `τ_aggregate = 1/0.130`, and revert "resolves both failures";
* **restore** the caveats and guards F dropped: "Banned unless donor-limited", "declared, not computed", "must not
  be reused", the "typically a few cm yr⁻¹" benchmark and the +6.5 m fitted-2002 check, the §9 pair 2×10⁶ yr vs
  8.6×10⁴ yr, the `[·]₊` one-way-valve clause of §2.2, "min over all moieties", "42 of the 43", "archived pull",
  "eight zeros are a convention", "not in the three-quantity hierarchy"; retitle §10.4; fix §2.2's Eq. (2)
  mis-citation;
* **restore the lost numerics** (P1's verified list): 89.526 / 2.090 / 4.652133 / 4.47 / 397.87-context, the ψ
  pairs 0.85 / 0.25 / 0.70 / 0.20 and the 1.5 trough-depth factor (§2.5), 2002 (window), 150 yr (§9), 4.44 / 415 /
  2.57 / 4.66 / 2.9 / 1.79, 2025 and the 0.9 in `T_resource,10% = 0.9 G_resource/C_G` (§6.5.3), 120,000 / 250,000,
  9.0 / 6.0, and the three DOI links (§2.3/D9). Seven numbers that an earlier draft of that file told us to chase
  are **not in the source at all** - 44.334, 312.655, 104.693, 1353.761, 468, 682, ±4.0 - and must stay out;
* **carry the two things v48 lost** that both the deposit and the adaptation have: the §1.1 flagship paragraph "The
  first failure mode has a public flagship object. Earth Overshoot Day aggregates component flows into a single
  calendar date…" (deposit line 59, v42 line 27; 0 hits in v48's md), and the §1.2 statement of what the framework
  does that F phrases as "component-resolved by construction… completely precluding cross-component summation into a
  scalar date";
* **decide A6** while the abstract is open: the abstract says flux reconstruction recovers unobserved *fluxes* from
  observed stocks, the proof in Lemma 3 says the reverse (readouts from fluxes). Fixing the abstract is the
  recommendation on record.

## Two defects in v48 that the gate could not see, and must see in v49

1. **A markdown artifact reached print.** Page 2 of `paper3_material_ledgers_v48.pdf` reads
   `The drift is concrete. - A reserve-life ratio divides a reserve figure by a production figure.` - a stray list
   marker and an orphan bold, because the hand-written front matter in `build_v48_base.py`'s `FRONT` dict was joined
   onto the paragraph instead of keeping its list breaks (v42 line 23 was clean). Gate check to add: no `-`/`*`
   list marker inside a rendered paragraph, and no `**` emphasis that opens without closing, in the md *and* in the
   extracted PDF text.
2. **The front matter has no preservation check at all.** `grep -i 'front'` over `verify_v48_base.py` returns 0
   hits; its paragraph check is md-vs-PDF and its verbatim check is the 290-row ruling, so a *dropped* deposit
   sentence inside the exempt region is invisible. Gate check to add: for the 222 protected rows outside §1, keep
   the verbatim test; for the 68 waived rows and for the front matter generally, test **claims** - the numeral,
   label, citation and table-cell multisets, plus the status-word set ("established/registered/illustrative/
   quarantined", the non-claims, and every `claim_ledger_v1.json` row whose `section` begins with `1.`) equal between
   the base document and the built one. Rewording is then free; changing a claim is not.

## Shape of the run (once the author says go)

`build_v49_base.py` reads the adaptation's gemini half → normalises delimiters to the deposit's `$…$` house style →
repairs P0 → re-inserts P1 numerics from the deposit, each one logged with the deposit line it came from → applies
`stylekit_v1.polish` to the non-§1 prose with the 222 protected sentences spliced before the pass and re-protected
after it (the v48 ordering, which is what makes the splice safe) → compiles article + three companions with
`tools/tectonic` → `verify_v49_base.py` with the two new checks → `build_v49_package.py` → a disclosure note written
from the run logs, including whatever the waiver costs (sentences reworded, claims re-verified, numbers restored).

No build-time normalisation of reused mathematics, as always. `tools/tectonic` must be restored first (`tools/README.md`
in the workspace, and the same note inside the archived snapshot). A fresh sandbox also needs
`pip install --quiet pymupdf pypdf pulp`.

## The reconciliation the author asked for - pinned, not quoted

/home/user/revision/v49/pin_waiver_scope_v1.py recomputes every figure from the v48 artifacts, **asserts** them against the counts the v48 run recorded (the
`counts` block of `v48_reuse_split.json`), and writes /home/user/revision/v49/waiver_scope_v1.json. It fails loudly rather than silently re-pinning if those
files move; the pinned source hashes are in that JSON (`v48_reuse_split.json` a77b50f10b7cb246…, `claim_ledger_v1.json` 354aad6067569549…).

| quantity | value |
| --- | --- |
| sentences the ruling screened | 558 = 290 reused + 268 regenerated |
| reused rows | 290 (260 supported at high confidence + 30 signposting) |
| reused rows placed verbatim by the splice | 208 |
| not placed | 82 (2 the deposit sentence could not be loca, 23 the located sentence is not in the doc, 4 not spliced, 17 its deposit sentence runs through a di, 33 fragment, 1 refused, 2 the deposit sentence carries a theorem) |
| regenerated rows | 268 (188 medium/low + 64 flagged + 16 by overrule) |
| Section 1 reuse rows | 68, of which 42 in §1.1 |
| **§1 rows the waiver frees** | **63** placed verbatim today; the other 5 were never placed, so they carry no protection to lift |
| rows outside §1 | 222, of which **145 verbatim-protected in the build** |

So the two figures quoted at you ("208 verbatim" and "222 more") never described two populations. 290 is the ruled
set; 208 is how many of it the splice placed; 222 is 290 minus the 68 in §1 - and only 145 of those 222 are placed.
Outside §1 the gate enforces verbatim protection on **145** rows and the waiver moves **63**. The JSON carries
the three id lists; the gate reads ids, not counts, which is what "these specific rows may be reworded, those may
not" requires.

## Guardrails, as code - /home/user/revision/v49/v49_waiver_gate_v1.py

Your three, plus the integrity check v48's gate lacked. `--control` runs it against known documents so its teeth are
on the record before any build, and writes /home/user/revision/v49/waiver_gate_controls.json.

* **G1 vocabulary stays pinned.** Statement labels and their titles, inline symbols, and a registry of 29
  load-bearing terms with counts. Control B (the adaptation's §1 against v48) reports `overshoot day: 1 -> 0`,
  `phantom mass: 1 -> 0` and `frozen-rate local ratio` absent from the build. Control C (the adaptation's §1 against
  the deposit) shows what must be reconciled before the adaptation's §1 can ship at all: it uses `reserve-life ratio`
  2 times where the deposit uses it 14; says `gross extraction` where the deposit says `removals-only pressure scale`
  (4 in the deposit, 0 in the adaptation's §1); `time to exhaustion` for `time to depletion`; `reserve-life quotient`
  for `reserve-life ratio`; and thins `donor-limited` from 19 mentions to 5. Under guardrail 1 those are not style
  choices, they are renames - so each is either reverted or approved as a terminology change to the whole paper.
* **G2 the ledger on the reworded prose.** Claim-atom traceability, not surface similarity: numerals, citations,
  section pointers and defined terms per sentence, each required to be backed by the deposit. The first draft of this
  check scored sentences by similarity and raised 78 flags on v48's front matter - noise, because a paraphrase is
  *meant* to look different. Atom-traceable, control C (build = the deposit itself) returns **0 flags**, which is the
  self-consistency test; control A returns one flag, and it is real: §1's passage on the 2008 SNA revision, SEEA
  2014 and "(United Nations, 2014)" is **not in the deposit at all** (`2008` dep 0 / v48 1; `United Nations` dep 0 /
  v48 4; `SEEA` dep 0 / v48 2). It entered through the upgrades line, and v48's 40-entry reference list carries no
  2008 entry for the year that sentence asserts. That is a live v48 accuracy item, not only a v49 design point.
* **G3 facts gated.** The same atom classes as sets against base and deposit, with the PDF traps closed: numerals
  canonicalised (a line-broken "600,000" is one number, not two), citation keys insensitive to `&`/`and`, serial
  commas, `et al.` and hyphenation - the earlier version flagged `Fischer-Kowalski 2011` as both added and dropped in
  the same breath, which is an artifact and is now fixed - plus a digit-squeeze backstop before anything is called
  invented. Named objects are **disclose-only**: proper-noun extraction differs between a PDF-derived deposit and a
  hand-set build at sentence starts, and that list is better shown to you than used to fail a build.
* **G0 integrity, the check v48 never had.** One run over v42's front matter against v48's flags exactly the two
  defects, and two more: the list marker that reached page 2, and, through G1/G3, the lost `overshoot day`, the
  dropped section pointers `2.3` and `6.5.4`, and the rewrite moving the phosphate figures out of math into prose
  digits - build-time normalisation of deposited mathematics inside the one region that was exempt from the rule
  against it.

Totals: control A 6 blocking + 1 disclosure, control B 8 + 2, control C 2 + 1. A v49 build passes
at `flag_count == 0`; the exit code is the flag count, capped at 120.

## What the waiver does not decide, resolved on the merits as asked

The two §1 passages the adaptation carries and the deposit does not are claims, not style, and they split.

* **Earth Overshoot Day - deposit content, restored, not an addition.** `work/paper3.txt:59`: "The first failure mode
  has a public flagship object. Earth Overshoot Day aggregates component flows into a single calendar date, so a
  severe defi…". v42 kept it, v48 lost it. It comes back as the deposit's own paragraph and is checked verbatim.
* **"Arithmetic Level / Dynamical Level (Yield Inflation)" - half-traces, so it is used and disclosed.** The term is
  the deposit's (`yield inflation`: dep 1, v42 2, v48 1); the two-level decomposition and the "hollowed out" image are
  not (all three: dep 0, v42 0, v48 0). The substance survives the ledger, the framing does not. Handling: keep the
  framing as connective tissue only if G2 passes it, and say in the disclosure note that the two-level naming is the
  adaptation's addition, so nobody reads it as the deposit's structure. Say otherwise if you want it cut instead.

## The 82-row question, answered by computation

`revision/v49/dispose_the_82_v1.py` reads the splice log, the audit and the built markdown, classifies each of the 82
not-placed rows by what the document actually contains, and asserts its own totals. Result:

| disposition | rows |
| --- | --- |
| absorbed - the deposit wording is in the document anyway, its block carried it | 37 |
| absorbed - the sentence is gone but every claim atom of its deposit partner survives in the same region | 13 |
| absorbed - no sentence, but the row's own claim atoms are present in its region (this is where E1/E2 used to hide) | 10 |
| kept - the draft sentence ships byte-for-byte | 22 |
| regenerated | **0** |
| lost - a claim atom gone | **0** |

So: **absorbed or kept, never regenerated, never dropped.** The 268-row regenerate path is a separate population and
the 82 do not enter it. The document-level split is therefore 208 rows carrying the deposit sentence, 22 carrying the
draft sentence, 60 absorbed, and 268 written from the deposit - and of the 22 kept rows, none carries a numeral or a
citation the deposit lacks (checked), so nothing draft-only rode in on a "left alone" verdict.

Two things the question surfaced that the brief should not have gone on asserting:

* **the arithmetic in the author's correction, corrected once more.** 208 + 145 is not 353: 145 is *inside* 208. The
  208 placed rows are 63 in §1 and 145 outside it, so after the waiver the gate enforces verbatim protection on 145
  rows and frees 63 - 208 in total before, 145 after. `waiver_scope_v1.json` carries all three lists.
* **the atom test is not a hedge test, and it says so.** It sees a lost number, citation, defined term or pointer; it
  cannot see a dropped "typically" or a weakened "under the declared window". 10 rows are classed absorbed on the
  strength of atoms alone. That is a human read, and `disposition_v49.json` carries the per-row fields so the read can
  be done against a list rather than against my summary of it.

## G4 and G5, and one place where I was wrong to you

`adaptation_term_revert_v1.csv` is the explicit revert the author asked for: 15 rows of alias → deposit term with the
counts that justify each (the adaptation's §1 uses `reserve-life ratio` twice where the deposit uses it 12;
`removals-only pressure scale` 0 times where the deposit says it 4; `donor-limited` 1 where the deposit has 19), the
rule (`force`, `watch`, or `label` = cut outright), and the four P0 items it never should have. G5 enforces it on the
built front matter - an alias present is a failure, and a replacement appearing fewer times than the alias it
replaces is a failure, which is what stops "revert" from quietly becoming "dilute". G4 keeps the cut content out.
The gate reads the CSV, so the ruling and the enforcement live in one file.

**Where I was wrong.** Last turn I told you the two-level decomposition was the adaptation's framing: I checked the
*label strings* `arithmetic level` / `dynamical level` (0 in the deposit) and wrote that the decomposition itself was
not deposit-backed. The deposit has it in §1's own words - *"It has two senses, and they are distinct. The first is
arithmetic and is the compensatory-aggregation failure above - a deficit in one component offset by a surplus in
another, so that a positive aggregate reads as adequate. This article formalises this sense as the aggregation
obstruction of Section 10.1. The second sense is dynamical and is yield inflation."* (`work/paper3.txt:66-72`). v42,
v47 and v48 all carry "It has two senses". So the *structure* is the paper's and the *heading labels* are the
adaptation's: cutting the framing as instructed would remove nothing, because the framing under the labels is already
there - and the loss to repair is E2, the dropped sentence that names the aggregation obstruction and points to
§10.1. Handling as ruled: no "Arithmetic Level / Dynamical Level" headings (G4), deposit's "two senses" wording kept,
E2 restored. If you meant to cut the two-senses passage itself, say so and I will treat that as a content change to
the deposit's argument, which is a different decision.

## Gate state, for the record

`--control` after these changes: control A **7 blocking + 2 disclosures** (E1-E7), control C still 0 on G2 and G0
(the self-consistency test), and G1's new coinage harvest is what caught E2 (`term the base coins or emphasises,
absent from the build: ['aggregation obstruction of section', …]`) - the fixed registry had missed it, which is the
argument for deriving the vocabulary instead of curating it. Reports in `waiver_gate_controls.json`; the errata for
the delivered line is `revision/v48/ERRATA_v48.md`.


---

## BUILD DONE — v49 (2026-09-19, later the same day)

Built as ruled: front matter + §1 from the adaptation (repaired *before* adoption), body = v48's body plus the
six sentences the read proved were lost. Deliverable: `revision/v49/paper3_supplementary_package_v9.zip`
(78 records, 2,094,033 B, sha256 `6c365b9e…d07f`); manuscript at
`revision/v7/paper3_material_ledgers_v49.{md,tex,pdf}`, 54 pp, companions/supplementary carried unchanged from
v48 (hashed, not recompiled).

Numbers, as measured: waiver gate **flag_count 0** / 14 disclosures, §1 checked against its 140 ledger rows;
`verify_v49_base.py` **FAILURES: none** — 143/143 verbatim-protected body rows, 9/9 errata items closed, back
matter byte-identical, body numerals 365→365, 17/17 §1 citations resolved, PDF carries 187/187 flowing
paragraphs, no unresolved ref, no stray front-matter marker (E6), v48's zip frozen at `3ad72c04…564fa7`.
The .tex body is byte-identical to v48's once the six insertions are undone.

Three corrections to what this brief said before the build, recorded rather than buried:

1. **The disposition answer for the 82 changes.** I reported "absorbed or kept, LOST 0". The 32-row read found
   six rows (D0238, D0286, D0385, D0521, D0719, D0631) whose *named object* is nowhere in v48 — so the honest
   answer is 22 kept + 54 absorbed + **6 lost in substance**, all six outside §1 where the verbatim rule bites.
   The atom test passed them; only the phrase-level read caught them. They are E8 in `revision/v48/ERRATA_v48.md`,
   and the item the author numbered E8 is E2 on that list (and v48-introduced, not inherited — dep 1 / v42 1 /
   v47 1 / v48 0). E9 was also found: v48's abstract mangled the two-senses passage and lost the second sense.
2. **The 145/63 pin needs one qualifier.** 145 ids were pinned; 143 sit in the body and are enforceable,
   1 (`D0023`) sits in the abstract — which the ruling frees along with §1 — and 1 (`D0004`) is not locatable
   in v48's text at all. v49 enforces the 143 and treats the abstract's row as freed.
3. **Two instruments were broken and are fixed.** `_rules()` in the waiver gate parsed the revert CSV with
   `len(fields) >= 8` and so enforced **2 of 14** rules (G4/G5 had been checking one substitution); it now
   reports how many rules it read. And the first front-matter pass rebuilt every line from the sentence
   splitter, which masks `$…$` — turning inline maths into a literal `M` and flattening numbered lists; caught
   by `diff`, not by a gate. Lines are now untouched unless a sentence is deleted, and the region's maths is
   counted on both surfaces (11 spans in, 11 out).

Added to the gate while building: **G1b**, an oracle-relative vocabulary check on the waived region, because
`G1` compares base→build and where the base *is* the rewrite it cannot see what the previous line carried —
that is how v48's four status labels (`arithmetic, not a forecast` and siblings) could vanish from the abstract
unflagged. G1b is disclose-only by design: putting the labels back would be choosing the deposit's exposition
over the author's, which is a content revision with its own decision, recorded in `NOTES_v49.md` as open item 1
instead of being absorbed. Its vocabulary is derived from three sources, one of them the label list read out of
`build_v48_base.py`'s `KEEP` — a hand-curated registry is still the soft spot, and the next person should not
trust TERMS alone.
