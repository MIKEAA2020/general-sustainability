# D4 and MDV, closed from the repo and the web — and a correction to what I said last round

## The correction

Last round I recorded both items as needing the author. Neither was true in the way I put it.

- **D4 is not an unwritten sentence.** It is the standards paragraph of §1.5 (Antecedents), written in v5 and
  carried through v36: "the System of National Accounts 2025 treats the depletion of natural resources as a cost
  of production alongside depreciation, following the treatment developed under the SEEA Central Framework
  …, which leaves the classification of depletion settled and the identification of a horizon open."
  `revision/v5/README_v5.md` says so twice (§1/D4: "Wording is mine from the verified facts — the author should
  confirm the framing before submission"; §4.1: "the facts are verified, the framing is mine"). So the item was
  never "draft this for me"; it was "I drafted it and you should check it". Checking it was my job, and I had
  left one of its families unchecked (the memory line "SEEA revision timetable: still unverified"). Fixed now.
- **MDV is not blocked on the author's theory either.** The obstacle was an undefined object in the article.
  Equation (1) writes $S_{\mathcal{T}}$ and the subscript is never defined; "typing" is then load-bearing in
  four more places — §2.1 ("only when their types and units agree"; "$d_x$ must itself be typed"), §2.5 ("the
  typing is the physical module's"), Definition 42 ("Conservation, capacity and typing are the three
  predicates"), §6.5 ("incommensurable objects under the typing of Section 2.1") — with no definition anywhere
  in either format. Grepping for a definition of "type" returns nothing. That is why MDV kept bouncing off the
  manuscript: its checkable half is a claim about this object. Defining the object (Definition 47) closes both.

## D4: what the sources say

Verified this turn against the standards' own material — the OECD compilation guide on measuring natural
resources for the 2025 SNA, the UNSD draft of that guide, and UNECE/UNSIAP explanatory notes:

1. **Depletion as a cost of production.** "Depletion of non-produced natural resources is recorded as a cost of
   production in the 2025 SNA, instead of the 2008 SNA treatment as other changes in the volume of assets."
   Consequence, stated in the same material: "In the 2025 SNA, NDP is defined as GDP less depreciation and
   depletion (in the 2025 SNA the term 'depreciation' has replaced the term 'consumption of fixed capital' used
   in the 2008 SNA)." Both halves of the article's sentence hold, and the 2008 contrast is now in the text
   because it is the interesting part.
2. **The lineage claim is exact.** "The 2025 SNA essentially follows the SEEA CF (UN et al. 2014), which has
   standardized the definition and recording of depletion … In the SEEA CF, it was agreed to treat depletion of
   natural resources like depreciation of fixed assets, as both types of assets are used up in the production
   process." The 2014 technical-implementation reference in the article's list is the right one.
3. **The physical definition is a rate comparison, not a horizon.** 2025 SNA: depletion "in physical terms,
   represents the decrease in the quantity of the stock of a non-produced natural resource … due to the
   extraction … occurring at a level greater than that of its growth". The article's claim that the standards
   identify no horizon is therefore not an argument from silence: the standards' own primitive is extraction
   net of growth, which is two rates.
4. **The framing that the article gains.** Nothing about the physical world changed between the 2008 and the
   2025 treatments; a net aggregate moved because a classification moved. That is this article's reserve-classification
   argument, exhibited on the statistical standards themselves, and the rewritten §1.5 says so. It strengthens
   the positioning rather than decorating it, and it removes the one sentence in §1.5 that asserted a relation
   between frameworks without naming the relation.
5. **One thing I did *not* pin, deliberately.** Secondary sources cite the definition at different paragraph
   numbers (7.283 in a September-2024 conference deck against 7.286 in a 2026 UNECE note), which is what draft
   and final numbering drift looks like. So the article's sentence carries no paragraph numbers. If the author
   wants pin cites, they must come from the final SNA 2025 text, not from these secondary readings. The
   reference entry's "Adopted by" became "Endorsed by …, March 2025", the language the adopting body uses.

## MDV: what is now in the article, and what is not

- **Definition 47 (Type structure).** $\mathcal{T}$ = a declared set of types $\mathsf{Ty}$; per-compartment
  $\mathrm{ty}_i$ and $\mathrm{un}_i$; and declared conversion coefficients $\mathsf{Cv}$, triples
  $(\alpha,\beta,c)$ attached to a named process. A sum across types is not a sum; typed-admissibility is a
  two-kind test on each flux column (transfer with $\pm1$, or conversion with $-c$ and $+1$, never both), which
  is Definition 21's closure cone being defined on $S_{\mathcal{T}}$ rather than on an untyped matrix.
- **Proposition 42.** Type classes = connected components of the conversion graph; every admissible column
  meets one class, so $S_{\mathcal{T}}$ is block diagonal and $\ker S_{\mathcal{T}}^{\top} =
  \bigoplus_\gamma \ker S_\gamma^{\top}$; hence no conservation law prices one class against another, and a
  cross-class aggregate is an additional declaration. Two lines of proof, checked by the gate as text and by
  the construction.
- **Remark 36** separates three things the literature conflates: reporting-boundary redrawing (invariant while
  no conversion is declared or withdrawn — the checkable core of the umbrella the reviews wanted, with the
  hypothesis that makes it true, and explicitly *not* extending inside a class, where Proposition 36 rules);
  valuation (nothing: the predicate is well-posedness, not a thesis about worth, and the article does not assert
  one); reclassification (priced by Definition 22's deficit, not by the type predicate, with the standards' own
  economic asset boundary as the shared exposure).
- **Not done, on purpose.** MDV still has no certificate field, no "declared MDV" hypothesis, and no named
  theorem. `revision/v7/supplementary_v9_candidate.md` S12 tabulates the correspondence so the position is
  citable and testable without being asserted, which is the same discipline that keeps the MDV table out of the
  body while the article's §3.1 vocabulary is what the table uses.

## What the author still has to give: one cell and one yes/no

1. **One cell**: the pull date or release tag of the archived RAM Legacy extract behind the 43-stock cohort.
   The arithmetic is re-derivable from the deposit, and the supplementary's own S5.2 already proves no public
   release reproduces the cohort — so the *vintage* is the only unrecoverable fact, and it is archival.
2. **One yes/no**: keep the rewritten §1.5 paragraph or trim it to a clause. Also worth a line of their time:
   the supplementary calls the current RAM Legacy release "v4.66"; the releases I can confirm on the deposit
   server today are v4.40 (2018-06-04), **v4.44 (2018-12-22, record 2542919 — both the label and the identifier
   the table prints are correct)**, v4.491, v4.493, v4.495, v4.63 (2023-12-11), v4.65 (2024-06-17), and the
   query returned no v4.66 — with pagination partly unavailable, so this is a flag, not a finding.
3. Everything else previously parked as "author's" is either shipped (v37) or recorded as the article's own
   standing non-claims.
