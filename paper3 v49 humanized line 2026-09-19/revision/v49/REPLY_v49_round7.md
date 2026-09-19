# v49 — round 7 reply (2026-09-19)

Three instructions, answered in order. Everything below is measured against the files that ship; the
commands are in `NOTES_v49.md` §6.

## 1. The introduction's spacing — fixed, and it was never the markdown

You were right that it was still wrong. The markdown has always had its blank lines (37.4 % of §1, which
is normal), so the fault was one layer down, in the `.tex` converter: it glued whole sections into a
single `\item` and typeset everything between markers as one paragraph. That is why page 2 ran from the
first line to the footer with no break, and why the four certification layers printed as
`• Bookkeeping balance (mass accounting), 2. Stoichiometric conservation…` — the numbering survived as
literal text inside a bullet, and contributions 6 and 7 were swallowed by 5.

The region loop now emits one `\item` per markdown item line and splits a new list when a numbered item
starts mid-paragraph. Verified on the rendered pages: p2 has `1. Compensatory Aggregation…` and
`2. Classification Drift…`; p3–4 have the four layers numbered `1.`–`4.` with their sub-bullets; p5 has
contributions 1–5 with sub-bullets, and the `1.2 Contributions` / `1.3 Organization` headings sit at
their own offsets. No markdown was edited. Two proofs now live in the builder: the region's word sequence
must match md↔tex after markup and maths are stripped, and the markdown marker count must equal the
`\item` count (37 = 37).

## 2. Nothing legitimate was condensed out of the introduction

Similarity could not answer this — §1 was deliberately rewritten, and 0 of v48's 134 long §1 sentences are
verbatim in v49 — so I switched to atom coverage: a sentence is only a loss if a distinctive atom
(a numeral, a citation year, a rare content word) appears **nowhere in v49**. Of 134 v48 sentences and
131 from v42, 38 candidates fail that test, and I then read each against §1. Thirty-five are rewordings
whose proposition is on the page:

| v48 / v42 wording | where it is now |
|---|---|
| "the wear is diffuse, gradual, and in some cases invisible… sudden" | line 45, the elevator: strain "accumulates unseen… catastrophe is instantaneous" |
| "Each of these quantities is informative about something." | line 24, "Each metric provides specific institutional or descriptive information" |
| "the classification refills itself, and any ratio built on it inherits that behaviour" | line 49, "It replenishes dynamically through new discoveries and shifting economics" |
| "overlapping readings of one pool, not rival claims" | lines 67 and 72 |
| "what decides is the renewal rate of the pool" | the regeneration clause in §1.1 |

The numbers were never at risk: §1's worked example ($1.0\times10^{6}$ kt reserves, $6.0\times10^{5}$ kt
extracted) is on line 49 and equals the deposit's 1,000,000 / 600,000 kt, and every substantive numeral
in all four documents is present on the rendered page.

Three items are genuinely not in v49, and they are labels and rhetoric, not findings — so they are yours
to decide, and I have not drafted replacements for them: v48's thesis line *"Waste is a relationship, not
a property of a substance."*, the defined label *registered open gap* (the deposit uses it once), and
*system moves*. They sit next to the four status labels already open, in `NOTES_v49.md` §7 item 2, with
the note that restoring them means importing v48's §1 wording — erratum E4's substance, hence not done.

One thing I told you last round was wrong. I flagged line 49 as a semantic regression, "physical
replenishment asserted for an economic reserve". I had read a truncated line: the clause is qualified by
"and shifting economics" in the same sentence. It is not a regression.

## 3. Errors found in places not yet examined, and what I did about them

The new surfaces were the supplementary and both companions (never read line by line), the LaTeX
escaping, and the numerals as they reach the page. Findings:

* **`an catastrophic deficit`** (line 26) — a typo of the rewrite; it appears in no earlier surface and
  the deposit has no `an`-before-consonant site anywhere. This is the one thing I changed: repaired by a
  logged rule inside `house_form()`, so the whole-line proof replays it and the audit classifies the line
  as `adapt + logged prose repair` rather than unexplained. The markdown is 214,262 characters (215,027 bytes on disk), one character shorter.
* **A -ize/-ise split I decided not to touch.** My first rule rewrote the heading `### 1.3 Organization`
  into `Organisation` because the OECD's name is in the reference list — my error, caught by reading the
  rule's own output. The deeper problem is that there is no convention to align to: v48's body, which
  this build may not edit, mixes `specialization` (14×), `realized`, `authorized` with `normalised`,
  `mobilised`, and §1 itself has `formalize` 7× beside `formalises` 1×. Recorded as an open item with the
  counts, not repaired.
* **Rounding inside one sentence** of §1's example: `4.0/6.0` prints as `0.67` (rounded) while
  `1.0/1.6` prints as `0.62` for 0.625 (truncated). Inherited from v42, so reported rather than edited.
* **The other three documents are clean**: 0 numerals absent from the page in each, 0 dangling
  section pointers into the article, `$` parity even, environments balanced, `#1` inside macros
  legitimate. Their `.tex` files wrap numbers with `\allowbreak{}` (`308.\allowbreak{}33`), which is why
  md-vs-tex character counts disagree while the page is right.
* **The dangling-reference scare was my instrument, not the paper**: 71 statements use the
  `**Theorem N (**` form and all their numbers are defined; `Conditional Theorem 15` is defined at md
  line 933 and my checker's pattern just did not know that label. Same for the dashed ORCID, the reference
  page ranges, and a numeral test of mine that merged adjacent table cells into one number. Per your
  standing rule I fixed the checkers — including the gate's G1b, which had been counting vocabulary on
  the adaptation instead of the previous line, so all seven of its items falsely read "0 in v48"; it now
  reports where each term actually is, which turned four "lost" terms into "moved to the abstract or the
  body" and left three honest ones.

## Chain, after the one-byte change

`build_v49_base` → `build_v49_tex` → gate → audit → pin → verifier, all re-run against the shipped files:
front maths 11/11, labels 71 / refs 0 / unresolved 0, region list items 37 md = 37 tex, four documents
compile 54/19/10/8 pp with overfull ≥6 pt 0 and `??` 0, pdf_flow 203/203 paragraphs, gate flag_count 0
(8 disclosures), audit FINDINGS 3 (the three disclosed orphans and nothing else), pin 290 ruled rows / 145
verbatim-protected outside §1, verifier `*** v49 verified ***`, FAILURES: none.

The package is `paper3_supplementary_package_v10.zip` (84 records). Its digest is not quoted in a file that
travels inside it - that would make the copy in the zip stale the moment the digest was written down - so it
is in `paper3_supplementary_package_v10.sha256` next to the zip and in the archive commit message. The
branch `archive/paper3-v48-workspace` head carries every document, and the push now checks each archived
blob against the workspace bytes rather than trusting a filename.
