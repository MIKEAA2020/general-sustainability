# How the landmark papers in your own literature do it
### Craft notes from a close read of six texts, applied-diagnostically to `paper3_material_ledgers_v32.pdf`

Figures are prose-only (the table-flattening artefacts of PDF extraction are excluded;
`style_audit.py` in this folder reproduces them).
Read on 2026-09-14. Quotes below are verbatim from the sources I fetched (listed at the end);
paraphrases are labelled as such. The point is not "write prettier" — it is that in this
literature, the papers that changed how practitioners read a number did it by **staging the
misreading before the correction**, and by **keeping the caveat in the sentence, not in a
footnote**. That is exactly the transaction your paper wants to make.

---

## 0. What your draft currently looks like, measured

Not impressions — counts over the extracted text (21,305 words, 763 sentences):

| Signal | Your draft | Landmark range |
|---|---|---|
| mean words/sentence | **27.8** (median 23, p90 **55**, max **122**) | 14–22 (impression, from the sources read) |
| sentences over 40 words | **22%** (60 of 714 above 60 words; 26 above 80) | <10% |
| `X, not Y` constructions | **67** | rare; O'Neill 2018 carries its contrasts with "However," and "We find that…" instead |
| em-dashes / semicolons | **213 / 293** | 20–60 |
| "we"+"our" density | **0.1 per 1,000 words** (2 "we", 0 "our") | O'Neill: "We find that…", "We argue that…", "We combine…"; Bierkens & Wada: "We present… We start with… We pay particular attention to… We end this review with…". Target ≥2/1k. |
| impersonal self-reference "this article / the article" | **27** | near zero |
| "for example" / "for instance" / "e.g." | **0** (0.0 per 1k words) | common (target ≥0.6/1k) |
| "in practice", "practitioner", "stakeholder", "case study" | **0 / 0 / 0 / 0** | common |
| "consider…" (the classic setup verb) | **0** | very common in definitions |
| questions | **7** | usually one *real* framing question in the intro |
| nominalizations (-tion/-ment/-ity/-ness) | **1,140** (≈5% of all words) | 2–3% |
| concrete-world nouns (aquifer, well, crop, price, fish, phosphate, basin, India, China) | **117** — genuinely present | the good news |

Three things follow from that table.

1. **You have no agent.** Two "we"s and zero "our"s in 40 pages: nobody in the paper is doing the
   separating, the proving, or the refusing. Every landmark above is unmistakably *someone's*
   argument. This is the single largest "is this written by a person?" tell — bigger than any
   vocabulary issue — and it is trivially fixable.
2. **You have no example, only exhibits.** "Example" occurs 8 times, always as "worked instance" /
   "illustrative example" labels *inside* the formalism; there is no place+year+number narrative.
   Compare Bierkens & Wada (563 citations, 48k downloads) whose abstract spends its first two
   sentences entirely on *why people are pumping*: population growth, diets, megacities without
   piped water.
3. **Rhythm, not diction, is your main flatness.** A 27.8-word mean with 24% of sentences at ten words
   or fewer and 26 above eighty, plus a 67-fold repetition of one contrast frame is not "precise", it is one long breath. The
   elevator passage (p. 2–3) shows you can write short, hard, human sentences: *"Nothing
   announces the damage while the cable holds."* Your own best page is the metric outlier.

---

## 1. O'Neill, Fanning, Lamb & Steinberger (2018), *Nat. Sustain.* 1:88–95 — "A good life for all within planetary boundaries"

The model for **one fact as the whole opening**, and for naming a framework in plain words.

- First sentence of the abstract is a stake, not a method: *"Humanity faces the challenge of how to
  achieve a high quality of life for over 7 billion people without destabilizing critical planetary
  processes."*
- The payload is a single falsifiable sentence: *"We find that no country meets basic needs for its
  citizens at a globally sustainable level of resource use."* — note "We find that", the verb of
  agency, and "no country", the word a non-specialist retains.
- Then the *scope* of the claim: *"Physical needs … could likely be met for all people without
  transgressing planetary boundaries. However, the universal achievement of more qualitative goals …
  would require a level of resource use that is 2–6 times the sustainable level."* — this is your
  "status classification", written as two sentences a journalist can quote without distorting.
- Body structure: short signpost subheads that are arguments, not containers — "A safe and just
  space", "Analytic framework".
- **The move you should copy most**: they name the hole in their own foundation before building on
  it — *"What the SJS framework lacks, however, is a conceptualization of how resource use and
  social outcomes are linked."* Then: *"We argue that the SJS framework operationalizes the concept
  of 'strong sustainability'."* Claim, gap, own contribution, all in one page.
- They also pre-empt the obvious objection in prose, not in a limitations box: *"It is an important
  question to address given that it is often claimed that all people could live well if only the
  rich consumed less, so that the poor could consume more."*

**Transfer:** your §6.5 already classifies three indicators "at their exact status". Put the
one-line verdict for each in the abstract, in the *verb-first* form — and put your own gap sentence
(the two-pool groundwater model is a registered open gap; spawning biomass is not an abiotic support
pool) in the **introduction**, where it buys credibility, not in §10.4 where only the faithful arrive.

---

## 2. Bierkens & Wada (2019), *Environ. Res. Lett.* 14:063002 — non-renewable groundwater review

The closest structural analogue to your paper: a work whose entire first job is **to separate ways
of measuring one thing**. Notice how non-defensive it sounds while doing it.

- Opens on human drivers before any method: *"Population growth, economic development, and dietary
  changes have drastically increased the demand for food and water."*
- Then a roadmap in the first person, four sentences long, in the exact order the reader will meet
  the material: *"We present a comprehensive review… We start with a section defining the concepts of
  non-renewable groundwater, fossil groundwater and groundwater depletion… We pay particular
  attention to the interaction between groundwater withdrawal, recharge and surface water which is
  critical to understanding sustainable groundwater withdrawal… We end this review with an outlook."*
- The concepts are defined **first, in words**, before any estimation method is ranked — the same
  discipline as your "three predicates, separated", done at a reading speed a hydrologist can keep up with.
- Closes on shared stakes rather than on a non-claim: *"…both the estimates of current depletion
  rates and the future availability of non-renewable groundwater are highly uncertain … if we hope
  to reduce this uncertainty in the near future."* — the hedge is *in* the sentence, and it points at
  what would have to be done, so the reader leaves with a job, not a disclaimer.

**Transfer:** your paper has no roadmap sentence in this voice. Adding one ("We build the ledger in §2,
certify it in §3–4, and only then touch depletion arithmetic in §6, because the semantics of a
horizon depend on which fluxes are declared") costs you nothing and reads as a human guiding a reader.
Also: consider making "we" appear 40–60 times, mostly in these five verbs — *we define, we prove, we
classify, we decline, we import.*

---

## 3. Alvarez-Garreton et al. (2024), *HESS Opinions* 28:1605 — "The unsustainable use of groundwater conceals a 'Day Zero'"

The best available model for **a vivid frame plus an explicit refusal to over-claim it** — precisely
your problem, since your elevator image and "liquidation" language want the same licence.

- They name the mechanism, not the metric: *"The unsustainable use of groundwater conceals a 'Day Zero'."*
  A title that says what is hidden is a title a reader finishes.
- One concrete event, dated, does the work of a dozen abstractions: *"The announcement of an imminent D0
  on a specific date (12 April 2018, estimated based on the remaining water stored in the reservoir and
  the water use requirements from the city) triggered water saving strategies that, along with the
  arrival of winter precipitation interrupting the drought, allowed the city to avoid drastic water cuts."*
  Note that the *number was wrong and the framing still worked* — and they say so. That is the honest
  version of what a horizon number is for.
- Then they confront the critique of their own vividness head-on, and answer it as a functional claim:
  *"The concept of D0 has faced criticism from the scientific community, which attributes to it a
  sensationalist use and lack of scientific robustness, among other concerns. Nevertheless, it
  generates a sense of urgency that puts pressure on decision-makers to take actions."*
- They keep a *second* reading of the same event, for the people who disagree: Montevideo 2023, where
  "public opinion criticized this measure, claiming it masked a D0 situation by avoiding supply cuts
  at the expense of providing non-potable water."
- Terminology for non-specialists is introduced once, plainly, with the arithmetic visible: *"When the
  ratio of total water uses to water availability — the water stress index (WSI) — exceeds 40%, a
  basin is considered highly water stressed."*

**Transfer:** add two or three sentences to §1.1 in this register — that the component-resolved
horizons are *for* the moment when a water board or a fishery council has to act, that a stark number
can be mobilising without being a forecast, and that your classification is what keeps the starkness
from becoming sensationalism. You can then cite this HESS piece as the case where a
non-robust-but-actionable frame was contested openly.

---

## 4. Ostrom (2009 Nobel lecture, publ. *AER* 100(1)) — polycentric governance

The model for **authorial presence, honest failure lists, and refusing pessimism without softening the
diagnosis**. Also the most relevant precedent for your §9 (institutional delay interface).

- She frames a career as an argument: *"In this article, I will describe the intellectual journey that I
  have taken the last half century from when I began graduate studies in the late 1950s."*
- Her origin anecdote is a *groundwater* one, and it is told physically: *"I studied the efforts of a large
  group of private and public water producers facing the problem of an overdrafted groundwater basin
  on the coast and watching saltwater intrusion threaten the possibility of long-term use."*
  Nothing in your paper is as memorable as "watching saltwater intrusion".
- She refuses the cartoon model of the human: *"The humans we study have complex motivational structures
  and establish diverse private-for-profit, governmental, and community institutional arrangements that
  operate at multiple scales to generate productive and innovative as well as destructive and perverse outcomes."*
- Her experimental result is reported as a *reversal of an assumption*: *"isolated, anonymous individuals
  overharvest from common-pool resources. Simply allowing communication, or 'cheap talk,' enables
  participants to reduce overharvesting and increase joint payoffs, contrary to game-theoretical predictions."*
- And she states the limits of her own optimism as data: *"we cannot be overly optimistic and presume that
  dilemmas will always be solved by those involved. Many groups have struggled and failed."* Followed
  immediately by the policy consequence: *"a core goal of public policy should be to facilitate the
  development of institutions that bring out the best in humans."*

**Transfer:** your paper's §10 ("What the Ledger Does Not Support") is doing Ostrom's job —
distinguishing agents from systems — but reads as a refusal list. One sentence of the form *"many
ledgers have been built and still misdescribed the situation; the failure is not arithmetic but
typing"* would convert the whole section from defence to argument. Also, if any of your construction
comes from a real institutional complaint, say what it was; Ostrom's credibility is autobiographical.

---

## 5. Daly (1990), "Commentary: Toward some operational principles of sustainable development", *Ecol. Econ.* 2:1–6

Six pages, and every one of them is a plain noun plus a rate. This is the register your weak/strong
paragraph is reaching for.

- Definition by contrast, in one line, no formula: *"Growth is quantitative increase in physical scale
  while development is qualitative improvement or unfolding of potentialities."*
- Then a *judgment*: "sustainable growth should be rejected as a bad oxymoron."
- Two operational rules, each "rate vs rate", which is literally your §6 architecture: harvest rates
  equal regeneration rates; emission rates equal assimilative capacity.
- The substitution argument is carried by an object, not an axiom (per the WSU teaching copy of the
  commentary): bigger fishing nets cannot substitute for a greater stock of fish — the material
  transformed and the tools of transformation are *"complements, not substitutes"*.
- Rate-limited use of a finite stock: non-renewables may be used "quasi-sustainably … by limiting their
  rate of depletion to the rate of creation of renewable substitutes."

**Transfer:** your formulation — weak/strong as *two regimes of one system, decided by whether the
material cycle closes at the rate of use* — is a genuine advance on Daly, and it is currently
introduced as a correction ("a reading … developed for the ledger, not the received distinction").
Try the Daly-shaped sentence first and the citation second: name the physical picture (nets and fish),
*then* say which received distinction it replaces and why your version is stronger. Also: "waste is a
relational status, not an intrinsic property of any material" is already a Daly-class sentence.
It is buried mid-paragraph on p. 4. Promote it.

---

## 6. Meadows et al., *The Limits to Growth* (1972) / *30-Year Update* synopsis — plus Whitesides on craft

Two devices worth stealing, both from the "how to make an accounting fact feel live" toolkit.

- **A labelled scenario, narrated.** LTG's method was to *tell* the trajectory it had simulated, with
  the assumption printed on the box, and the reader never mistakes it for a prediction. This is the
  exact licence your §7 ("declared stochastic surrogates") needs: you may narrate one trajectory,
  provided the label travels with it.
- **Plainly stated, self-cancelling arithmetic.** The 30-Year Update synopsis makes your phosphate point
  in two sentences and then concedes the rest: *"Between 1970 and 2000, even though billions of barrels of
  oil and trillions of cubic feet of natural gas were burned, the ratio of known reserves to production
  actually rose, due to the discovery of new reserves and reappraisal of old ones. Nonetheless the stock
  of reserves is finite and nonrenewable."* — i.e. the *reserve* critique does not require the *stock*
  to be unlimited. Your §6.5.3 needs that second clause visible: you are attacking the ratio, not
  defending infinite phosphate.
- **Whitesides (Harvard, "Writing a Scientific Paper"):** the deck's most useful device is a specimen
  of bad prose — a technically perfect, dense, first-person-free abstract of real work, captioned
  *"(Prepared for, and rejected by, Nature.)"* — followed by what good scientific prose is allowed to
  sound like, e.g. Frankel's *"We are immersed in a world of clocks. All that happens meters time."*
  His stated premise: *"In science, one writes for many audiences"* (peers and editors; general
  audiences "for whom TV is always an alternative"; sceptical referees). And his structural rule:
  writing is part of the research, so if a section cannot be summarised in one spoken sentence, the
  thought is not finished yet.

---

## 7. Ten rules for this paper, derived above

1. **Put a person in the first sentence.** The paper's subject is institutions misreading a number.
   Name one misreader, or the reader who is meant to stop, in sentence one.
2. **One quotable verdict sentence per family of indicators.** "Reserve life is arithmetic, not a
   forecast" is already quotable. Give each of the three a sentence that survives being quoted badly,
   and repeat it verbatim in the intro, the §6.5 heading and the conclusion.
3. **Say "we" where you currently say "this article".** 27 impersonal self-references, 2 "we"s — invert it.
4. **Break your longest breaths.** 60 sentences exceed 60 words; the longest is the 122-word rest-set
   sentence of §4.6 ("With vanishing extraction (E ≡ 0), the rest points of the closed natural block are
   exactly the three sets — …"). Rule: no sentence may carry both a claim and its exception. Split at the
   exception. (The 276-word "sentence" the first pass reported is the §2 symbol table flattened by the
   PDF text extractor — a layout artefact, not prose; the script now excludes it.)
5. **Cut `X, not Y` from 67 to ~15.** Keep it only where the negation *is* the result (the abstract's
   "services are readouts, not conserved mass"; §6.5's three verdicts). Elsewhere: "rather than",
   "instead of", a full second sentence, or just assert the positive.
6. **Cut em-dashes 213 → ≤60.** Each parenthetical costs the reader a place-keeper. O'Neill and Bierkens
   & Wada use commas and separate sentences for the same material.
7. **Add a real example per applied claim** — but only with numbers your paper already registers
   (e.g. US phosphate reserves ≈1,000,000 kt flat for decades against ≈600,000 kt of cumulative
   production since 1996). Do not import press figures you cannot source; a humanized paper that
   fabricates a datum is a retracted paper.
8. **Front-load the honest limits.** Move the two-pool gap (§8.2) and "spawning biomass is not an abiotic
   support pool" into §1 as O'Neill-style self-named gaps. Caveats early read as judgement; caveats in
   §10 read as defence.
9. **Give the reader a ladder.** A 30-second block (title + abstract + verdicts), a 3-minute block
   (§1 + §6.5 + §11), and the 30-minute implementation (§§2–5, 7–9). Whitesides: different readers,
   different clocks; your 40 pages already assume a single reader who reads everything.
10. **End with capacity, not refusal.** Ostrom's last move is "many groups have failed, *and* policy
    should build institutions that bring out the best in humans". Your §11 should say what a
    practitioner can now *do* that they could not do before — certify componentwise nonnegativity,
    refuse a weighted sum, name which horizon-question they are answering.

---

## 8. What must NOT be "smoothed" (the humanization traps)

Your load-bearing material. A style pass, an editor, or a paraphrasing tool will destroy all of it:

- The **status labels** (statistical index / arithmetic / pressure scale; registered, non-example,
  illustrative, quarantined). Never let a synonym substitute for a status word; the taxonomy is the result.
- Every **conditional** on first-passage results ("conditional on treating μ and the barrier as
  fixed"; "on declared stochastic surrogates"). Vivid framing must attach to the number, not
  dissolve the conditioning — this is the Day Zero failure mode, and §3 above is the model for
  naming it explicitly.
- The **non-reduction theorem** and its five numbered reasons, and the note that the projection claim
  is made under the companion-paper citation and "is not re-proved here". Do not compress; do not
  move into an appendix.
- The **exact numerical registers** (50, 397.87, 5050, 4.652, −0.348, κ_A^K = 5.000, qE*N* ≈ 0.187,
  the "factor of eight" and "two orders of magnitude" readings). Precision is a *humanizing* feature
  when the reader can check it — keep the digits, add the sentence that says what the reader should
  notice about them.
- **"we import at the companion's registered precision"** and the reverse check. Provenance statements
  are the opposite of puffery; keep their blunt voice.
- The **five double-counting rules** and "no interior rest at positive effort". These are prohibitions
  on a *class* of argument, not hedging. Do not soften "cancellation is cheap" into anything polite.
- The elevator: keep the metaphor, keep "to make the wear measurable while the cable still holds, not to
  predict the snap" — and do not let a copy-editor delete that clause. It is the licence for the metaphor.

---

## 9. Sources actually read

1. O'Neill, Fanning, Lamb & Steinberger (2018), *Nature Sustainability* 1, 88–95 — full text PDF.
2. Bierkens & Wada (2019), *Environ. Res. Lett.* 14, 063002 — open access (48,438 downloads / 563 citations on the article page).
3. Alvarez-Garreton, Boisier, Garreaud, González, Rondanelli, Gayó & Zambrano-Bigiarini (2024), *HESS Opinions* 28, 1605–1616 — open access.
4. Ostrom (2009), Nobel Prize Lecture, "Beyond Markets and States: Polycentric Governance of Complex Economic Systems" — lecture PDF; also its *AER* 100(1) printing.
5. Daly (1990), *Ecological Economics* 2, 1–6 — read via the WSU teaching summary/archive page (quotes from that copy; verify wording against the journal before quoting in text).
6. Meadows et al., *The Limits to Growth: The 30-Year Update* — synopsis PDF (quoted via search-extracted text; re-verify page numbers before citing).
7. Whitesides, "Writing a Scientific Paper: One Idiosyncratic View" (EPFL slide deck, Harvard) — includes the "rejected by Nature" specimen.

If you want, I can extend the read to: Rodell et al. (2018, the G3P paper whose "years to depletion"
column you classify) and Kuehl et al. (2022, *WRR*) so the critique quotes the disputed numbers in
their own published wording — for a paper about indicator semantics, quoting the misreading verbatim
is the strongest available opening.
