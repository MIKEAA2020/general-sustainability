# What the Accounts Settle, and What They Leave Open: Depletion as a Cost of Production, and the Missing Step from a Rate to a Horizon

*A commentary accompanying "Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise
Diagnostics, and the Semantics of Depletion Horizons", and the companion to the methods study on certifying
a typed ledger (Abaee, 2026d). Nothing here is proved: the arithmetic is quoted from the main text or
recomputed in Section 7 from the accounts themselves, and the standards statements are cited. Where the
main text's labels are used, they are its own.*

**Amin Abaee** — Independent Researcher
ORCID 0000-0002-0019-1842 · amin_abaee@ut.ac.ir

**Track.** Commentary / correspondence.
**Numbering convention.** Assertions in this commentary are lettered B1, B2, … and are *claims about the
record*, not results; the companion carries no theorem counter.

---

## 1. The question this commentary answers

The accounting standards now record depletion as a cost of production. A reader of the main text will ask
whether that closes the gap the article opens, and the answer is a single sentence, which this commentary
defends: **the standards settle how a depletion *flow* is recorded and valued; they never take the step from
a flow to a *horizon*, and the article's contribution lives on that step.** Everything below is either an
exact statement of what the standards do, an exhibit of what they do not reach, or a note on how to cite the
difference without over-claiming.

The main text already carries the technical content: the reclassification exhibit in its Section 1.2, the
horizon arithmetic and its bias in Section 10.2 (Remark 33), the aggregate's inability to certify components
in Section 10.1 (Proposition 30), and the classification of "time to depletion" quantities in Section 6.5.
What is added here is the interface: what a statistical agency that adopts the 2025 revision can and cannot
say with the article's apparatus, and what it must still decide for itself. Section 7 carries the recomputation of the aggregate overshoot date with carbon demand excluded, on the
accounts themselves, with the two conventions reported side by side.

---

## 2. What changed, stated exactly

**B1.** In the 2025 System of National Accounts, depletion of *non-produced* natural resources is recorded as
a cost of production in the current accounts. In the 2008 revision the same quantity was recorded in the account
of other changes in the volume of assets and liabilities. Consequently net domestic product is affected by
depreciation — the 2025 terminology for what the 2008 revision called consumption of fixed capital — *and* by
depletion, and so are net national income and net saving.

**B2.** The 2025 revision takes this from the SEEA Central Framework (2014), which standardised the definition
and recording of depletion; the framework treats depletion of natural resources like depreciation of fixed
assets, on the ground that both are used up in production.

**B3.** Two consequences are worth stating because they are routinely mis-remembered. First, the change is
classification, not measurement: **no extraction rate, no physical quantity and no valuation method of the
2008 accounts is replaced.** The same number moves. Second, the effect is not confined to net aggregates in
every case: recording depletion as a cost may also touch gross product where natural-resource production is
undertaken by government for its own final use and output is measured by the sum-of-costs approach (2025 SNA
§7.137, as cited in the OECD compilation guide; the guide is the source used here, and the paragraph number is
reproduced only as a quotation from it — see Section 6).

**B4.** Alongside the depletion entry, the 2025 revision adopts the split-asset approach: the value of a
resource, and therefore its depletion charge, is attributed between the legal owner and the extractor
according to economic ownership shares, with rents to the legal owner including royalties, surtaxes and
permits linked to extraction. For biological resources yielding once-only products, the boundary between
cultivated (produced) and non-cultivated (non-produced) assets is redrawn, regeneration of biological
resources is recorded as gross fixed capital formation, and depletion is treated as a cost of production.

**B5.** The last item deserves emphasis, because it is where the two systems differ most sharply from the
quantity the main text analyses. Under the 2025 revision a fishery recovering after a closure can be recorded
as *investment* while its stock grows, and a fishery in decline is charged a *cost*. Both are descriptions of a
comparison between extraction and growth. Neither is a statement about when the resource stops supporting the
economy. The accounts, on their own terms, do not ask that question.

---

## 3. What the standards define is a rate

**B6.** The definition of depletion the 2025 revision inherits is *extraction in excess of the resource's
growth* — a comparison of two rates, evaluated per accounting period, in the units of the period. It carries
no horizon, no barrier, no scenario, and no probability. The main text's Section 1.2 says this of the same
object: "the step from a rate to a horizon is taken nowhere in them, and it is not taken here either."

That sentence is the whole relationship between the two literatures, and it is worth unpacking once, because
each of the three steps across it has been taken implicitly by somebody writing about depletion.

**B7 (the first step, rate to stock).** From a rate one gets a stock-level statement only by assuming the
rate: a constant-drift or a declared drift class. The main text's uniform-drift bounds (its Proposition 6, and
the finite-exhaustion argument around it) are exactly the conditional form of this step: given a drift bounded
in a declared class, exhaustion time lies in a stated interval, and the interval's *width* is part of the
result. An accounts table supplies no drift class, so it cannot be read as a bound on anything.

**B8 (the second step, stock to threshold).** A stock level is not a depletion event until a barrier is
named. The main text treats the barrier as a declaration, not a discovery — its Definition 5 (scenario
conditioned hitting time) and its reserve-classification discussion both turn on this. The accounts are
indifferent to which barrier a country names; so is the depletion charge.

**B9 (the third step, threshold to decision).** Whether a horizon is *safe* depends on a required rate of
service and a control margin. That is the article's Theorem 24 and its Proposition 41; the standards have no
counterpart, and the absence is not an oversight. A national accounting system reports what happened to
values and volumes within a period; it is not a solvency test.

The three steps are the article's subject, and none of them is optional or cosmetic: the first needs an
assumption, the second needs a boundary, and the third needs a purpose. The standards need none of these
because they ask none of those questions.

---

## 4. An exhibit of the gap: the aggregate overshoot date

The one applied construction in the main text that needs no dataset recomputation is worth restating here,
because it shows what a rate-based standard cannot see. Write the components of an ecological footprint as
demand $d_i$ against biocapacity $b_i$, and form

$$\tau_{\mathrm{agg}}=365\,\frac{\sum_i b_i}{\sum_i d_i}=365\sum_i w_i r_i,\qquad w_i=\frac{d_i}{\sum_j d_j},
\qquad r_i=\frac{b_i}{d_i}.$$

Then $\tau_{\mathrm{agg}}$ is a demand-weighted mean of the component ratios, so
$\tau_{\mathrm{agg}}\ge\tau_{\min}:=365\min_i r_i$, with equality only where every component of positive weight
coincides, and the difference

$$\Pi_\tau=\tau_{\mathrm{agg}}-\tau_{\min}=365\sum_i w_i\bigl(r_i-r_{\min}\bigr)$$

is a compensation premium: one-signed, exactly decomposable, unbounded in the dispersion of the components
(main text, Section 10.2 and Remark 33). On the world totals of the 2025 edition of the National Footprint
and Biocapacity Accounts --- the edition whose series contains the year, since the construction Lin et al.
(2018) document runs to 2014 --- the 2022 aggregate ratio is $0.584$ of biocapacity to demand, so
$\tau_{\mathrm{agg}} = 213$ d; and because the carbon component carries zero biocapacity, the minimum component
ratio is $0$, so $\Pi_\tau = 213$ d — the entire aggregate date is compensation. Restricted to the five
components of positive biocapacity with renormalised weights, the same arithmetic gives $\tau_{\mathrm{agg}} =
538$ d against $\tau_{\min} = 365$ d, a premium of $173$ d, with the restricted premium running $547$ d (1961),
$346$ d (1980), $251$ d (2000) and $173$ d (2022): it shrinks as the components converge, as the display says
it must.

**B10.** Two features of that exhibit are invisible to a rate-based standard, and they are the reason the
article exists. (i) The zero row is a *published convention*: the Guidebook to the National Footprint and
Biocapacity Accounts states that no biocapacity figure is computed for carbon uptake, because carbon demand is
charged against forest land biocapacity and a separate carbon biocapacity would double count it (Global
Footprint Network, 2021, Section 9.1.2). The convention makes $\tau_{\min}=0$ identically, so the premium
equals the whole aggregate date *by construction* rather than by dispersion. A standard that records flows and
values has no place to register that a headline quantity is an artefact of a bookkeeping choice. (ii) A
depletion charge is additive across components; an overshoot date is not, and the direction in which the
aggregate is optimistic is fixed by the weighting. That is a *semantic* property of the aggregate, which is why
the main text calls its subject a question of semantics rather than of accuracy.

**B11.** The same construction explains a public disagreement that is not about arithmetic. An Earth
Overshoot Day for 2022 was announced as 28 July — the 209th day of that year. The 2022 row of a later edition
of the accounts gives $\tau_{\mathrm{agg}} = 213$ d. The four-day difference is vintage and nowcasting, not a
dispute about the formula: the accounts are recomputed for every year of the series at each release. Anyone
comparing a published overshoot date with a published component table is comparing two vintages, and the
main text's practice of pinning every quoted figure to a named release (its Section 6.5, and the vintage record
in the supplementary's S5) is the least costly protection available.
Section 7 now measures both effects on the accounts themselves, and finds the four-day figure smaller than
what the *level* of aggregation does to the same date and larger than a single edition step on a closed
year --- so the practice of naming a release has to name the aggregation level with it.

---

## 5. Two things a standard cannot supply, and a third it should not be asked to supply

**B12 (eligibility).** The 2025 revision leaves the physical boundary of an asset to the classification of the
resource, and for the renewable-resource categories it admits, what counts as an asset is drawn by viability
under prevailing technology and prices. The main text's Section 1.2 reads that clause correctly: an eligibility
statement of exactly the kind its Remark 36 treats as reclassification rather than as a property of the stock.
A statistical standard must classify, and classification criteria are
chosen, not discovered. It is a boundary on what an adopted standard can certify: a resource's presence on an
asset boundary is a statement about the accounts, and its absence is not a statement about the resource.

**B13 (components).** An aggregate cannot certify its components. The main text proves this in a form any
auditor can use — its Proposition 30 computes, by linear programme, the worst deficit $\delta_j^{\ast}(z)$
consistent with a published aggregate $z$ and the published component bounds — and its Section 10.1 states the
consequence: an aggregate can refute or alarm, never clear. A depletion charge recorded in a country's accounts
is such an aggregate. It says the resource was used up in producing this year's net product. It does not say
which component of the resource base carried the shortfall, and no revision of the standard will make it say so,
because the information is not in the aggregate.

**B14 (a horizon, not asked for).** It would be a category error to ask the accounts for a horizon, and the
main text is explicit that the comparison runs one way: the accounts supply an *instance* of the phenomenon it
analyses, not a premise for it. Nothing in the article's Sections 2 to 10 depends on any claim made here about
the standards, and nothing here depends on the 2025 revision. If the revision is amended, or a country
implements it differently, the article is unchanged. That is the sense in which the interface is a one-way
mirror, and it is a design property, not a hedge: the article's objects are the ledger's own.

---

## 6. Citation hygiene for anyone writing this comparison

Three practical rules, each learned from a specific difficulty in this review cycle.

**B15. Cite no paragraph numbers of the 2025 revision.** Compilation-stage documents disagree about the
structure of the text they describe: the OECD guide as published discusses the SEEA in Chapters 2, 35 and 36,
while the same statement in the circulation-stage material refers to Chapters 2, 34 and 35. Paragraph
references are therefore unstable at exactly the moment commentators most need them, and a wrong paragraph
number in a commentary is a correction that will itself need correcting. Cite the standard by edition and by
substance; where a compilation guide supplies a paragraph number, reproduce the *guide* as the source of the
number, as B3 does.

**B16. Distinguish endorsement from implementation.** The 2025 revision was endorsed by the United Nations
Statistical Commission at its fifty-sixth session in March 2025; the schedule of country implementation, the
availability of physical asset accounts, and the completeness of depletion estimates vary by country and by
resource. "Adopted" and "in the published accounts of country X" are different claims, and the second generally
requires the supplementary-style test of reading the numbers off the source rather than citing its title.

**B17. Never quote a depletion number as a date.** This is the article's own negative content, and it applies
with full force to the new accounts: a depletion charge is a rate, and rate times a year is a value, not a
year. If a national statistical office now writes "depletion of forests, 1.4% of GDP", that sentence is
complete. The inference "so we have N years" is not in it.

One further instance belongs to this section, because it is the kind of error a revision cycle hides: an
exhibit quoting a 2022 figure and citing Lin et al. (2018) for it mis-credits the *release*, whose series
ends in 2014, even though the citation is right about the *construction*. The two are different claims, and
only the second is checkable against the paper's own reference list. Both this commentary's Section 4 and
the main text's Remark 33 carried that ambiguity until the recomputation made the end year of the cited
edition a fact on the page rather than a recollection.

---

## 7. The one open computation, run

This section reports the restricted and unrestricted series recomputed with carbon demand excluded, to
answer three questions: whether the sign of the premium's trend survives the exclusion; how far the
restricted and unrestricted dates separate over the last decade; and whether the four-day difference
recorded in B11 widens or closes as the accounts are read. The arithmetic is run on the National Footprint and Biocapacity Accounts
--- the 2018 edition, series 1961 to 2014, with the 2017 edition (1961 to 2013) as the revision control --- on
the publisher's own `World` rows, with no interpolation and no model, and §8 gives the provenance, the hashes and
the command. Two conventions, one arithmetic: ALL is the published convention, all six demand components in the
ratio, in which the carbon row's zero biocapacity forces $\tau_{\min} = 0$ and the premium to the whole date;
NOC is the restricted convention, carbon demand removed from numerator and denominator with the weights
renormalised over the five components of positive biocapacity.

| year | carbon share of demand | $\tau_{\mathrm{agg}}$, carbon included | $\tau_{\mathrm{agg}}$, carbon demand excluded | gap | restricted premium |
|---|---:|---:|---:|---:|---:|
| 1961 | 43.9% | 498.7 d | 889.5 d | 390.8 d | 524.5 d |
| 1980 | 55.4% | 307.1 d | 688.3 d | 381.1 d | 323.3 d |
| 2000 | 55.3% | 266.2 d | 595.3 d | 329.2 d | 230.3 d |
| 2005 | 58.6% | 237.1 d | 571.9 d | 334.9 d | 206.9 d |
| 2006 | 59.5% | 231.5 d | 572.1 d | 340.6 d | 207.1 d |
| 2007 | 60.3% | 225.9 d | 568.8 d | 342.9 d | 203.8 d |
| 2008 | 60.3% | 226.8 d | 571.2 d | 344.4 d | 206.2 d |
| 2009 | 60.1% | 230.0 d | 576.5 d | 346.5 d | 211.5 d |
| 2010 | 61.3% | 219.4 d | 567.1 d | 347.7 d | 202.1 d |
| 2011 | 61.6% | 215.8 d | 561.9 d | 346.0 d | 196.9 d |
| 2012 | 61.4% | 216.1 d | 559.3 d | 343.2 d | 194.3 d |
| 2013 | 60.8% | 215.3 d | 549.6 d | 334.3 d | 184.6 d |
| 2014 | 60.2% | 216.5 d | 543.9 d | 327.4 d | 178.9 d |

**B18.** *The trend's sign survives the exclusion, and its size is not an artefact of the release.* The
restricted premium on the 2018 edition runs 524 d (1961), 323 d (1980), 230 d (2000),
179 d (2014); the decade means are 464 d, 358 d, 288 d, 253 d, 216 d, 191 d, and 45 of 53 year-on-year moves are declines. The
main text's series --- $547$, $346$, $251$, $173$ d, read off a later edition --- has the same sign and shape and
sits 4 to 8% above this release on the shared years. So the convergence reading in B10 does not depend on keeping
carbon in the ratio set, and the 4 to 8% release difference is the same phenomenon this commentary is about.

**B19.** *The two conventions part by roughly a year, and the size of the part is an identity, not a finding.*
Over the last decade of the release the restricted date exceeds the published-convention date by 340.8 d on
average (327.4 to 347.7 d), a ratio of 2.41 to 2.60; that ratio is exactly $1/(1-s_{\mathrm{carbon}})$ to
within 4.4e-16, with $s_{\mathrm{carbon}}$ between 58.6% and 61.6%. Removing carbon demand divides the
denominator by $(1-s)$ and multiplies the reported date by its reciprocal, which is a mechanical consequence of
the convention --- worth stating because the two numbers are otherwise quoted as though they answered different
questions.

**B20.** *The four-day gap neither dissolves nor indicts the arithmetic, and the explanation on offer is
incomplete.* Across an edition step on a closed year the aggregate date moves by 1.1 d on average and
1.9 d at most, so a mature-year revision does not account for a four-day figure. But reading the
publisher's `World` row instead of summing the national rows moves the *same* date by up to 9.2 d on this
release --- larger than the gap under discussion, and not a matter of data vintage at all. The restricted date,
mean 6.3 d and maximum 9.1 d across the same edition step, is a further 5.8 times more
revision-sensitive than the aggregate date, because the excluded denominator is the smaller quantity and an
absolute revision is divided by less. The direction, then: for the aggregate date a few-day gap is bigger than one
edition step and smaller than the choice of aggregation level; for the restricted date it is routine.

**B21.** *One structural fact changes how the display in B10 reads at a world aggregate.* There, cropland and
built-up land have $b_i = d_i$ identically --- 54 of 54 years, exactly --- because the world footprint of
a component whose demand *is* the area is priced at world-average yields, so those two components coincide by
construction; consequently $\tau_{\min}^{\mathrm{NOC}} = 365$ d in 54 of 54 years. The restricted premium
is then not a measured dispersion among components but the distance of the aggregate date past the year boundary,
and the "components converge" reading has to name the level at which it was computed. The main text carries this
as its Remark 37; the commentary records it because it is exactly the kind of thing a rate-based standard has no
place to register (B10).

---



---

## 8. Provenance, and how to re-run it

The release is named because the numbers are only as durable as that naming.

- **Data.** The 2018 edition of the National Footprint and Biocapacity Accounts (series 1961 to 2014), the
  publisher's own deposit, and the 2017 edition (1961 to 2013), its earlier deposit; both under CC BY-SA 4.0.
  The sha256 of the tables as read: 60968f7c9959537f8e67f915aca4259662b5cd42c3a0ec02d094677b4c280ef6 and 0dd766d975cd5e85f2a2d39cff1f914b92c514186ce507cb1f721a63be57b6a5.
- **Retrieval.** The datasets' public download endpoint on a data-marketplace host, no account required for
  those two deposits. The **current** edition is not reachable that way: the publisher distributes it free but
  through a registration form with an emailed link, its open data endpoints answer with authorisation errors or
  have moved, and the only edition mirrored on a public data portal is the 2018 one. So this is the newest openly
  fetchable, component-level release, not the current release, and that distinction is stated wherever the
  numbers are used.
- **What was examined and rejected.** A single-year footprint table on a data-hosting site, set aside because it
  carries no year column and no pinnable edition, so it cannot support a claim about a release at all. A
  package-manager loader whose name matches the subject turns out to be about something else entirely. Neither was
  used, and both are named here so that nobody re-traces the search.
- **The program.** `analysis/nfa_tau/recompute_tau.py`: standard library only, no network call, no
  interpolation. It writes one CSV per edition plus a revision ledger and a complete stdout, and it prints the
  aggregation diagnostic that B20 turns on. Re-running on a newer edition is two file names, not a change of
  arithmetic. The directory holds the two tables as fetched, a manifest with the retrieval commands and the hashes
  of the archive and its extracted member, and a licence note; a re-run reproduces its three outputs byte for byte from the archived
copies, a verification that requires no download.
- **Provenance of B's own Section 4.** The 2022 row quoted there ($0.584$, $213$ d) cannot come from Lin et al.
  (2018), whose release's series ends in 2014. The main text’s Remark 33 names the edition the year comes from and keeps that citation for the construction it documents. This is the specific reason for the release-naming practice of B11.

---



---

## 9. What a reporter should publish

Four sentences of practice, which is the only place a commentary can be usefully prescriptive.

1. Publish the component table with the rate comparison, not a horizon: extraction and growth, per component,
   with the period named. The reader who wants a date can then build one and will know what they assumed.
2. If a date is published, publish the direction of its optimism. For any demand-weighted aggregate of
   component ratios, the aggregate is greater than or equal to the worst component's date, and the gap is
   computable from the same table (B10). One extra column is all it takes.
3. Name the release, the pull and the aggregation level, not the publisher. "Per the 2024 release, on the
   publisher's world aggregate" is checkable; "per national accounts" is not, once revisions are routine
   --- and B21 measures the level's contribution in days, so it belongs in the same sentence as the release.
4. Say which classification decisions the figure depends on. A depletion charge depends on the asset boundary,
   on the ownership split, and on which component carries a zero by convention. All three are bookkeeping.
   Naming them costs nothing and makes the figure durable across revisions.

None of the four requires the article's machinery. All four require the distinction the article draws between a
quantity that answers one question and a quantity that is read as answering another.

---

---



## References

Abaee, A., 2026. Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons. Zenodo. https://doi.org/10.5281/zenodo.22554177.

Abaee, A., 2026d. Certifying a Typed Ledger: The Predicates, the Programmes, the Vintages, and the Reproduction Bundle. Companion methods study, submitted with this commentary.

Global Footprint Network, 2021. Working Guidebook to the National Footprint and Biocapacity Accounts, 2021
edition. Global Footprint Network, Oakland, CA.

Lin, D., Hanscom, L., Murthy, A., Galli, A., Evans, M., Neill, E., Mancini, M.S., Martindill, J., Medouar,
F.-Z., Huang, S., Wackernagel, M., 2018. Ecological footprint accounting for countries: Updates and results of
the National Footprint Accounts, 2012–2018. Resources 7, 58. https://doi.org/10.3390/resources7030058

OECD, 2025. Measuring Natural Resources in the National Accounts: Compilation guidance for the implementation
of the 2025 SNA. OECD, Paris.

United Nations, 2014. SEEA Central Framework: 2012 Technical Implementation. Statistical Papers, Series M No.
96. United Nations, New York. (Issued jointly with the European Commission, the International Monetary Fund,
the Organisation for Economic Co-operation and Development and the World Bank.)

United Nations, 2025. System of National Accounts 2025. United Nations Statistics Division, New York. Endorsed
by the United Nations Statistical Commission at its fifty-sixth session, March 2025.
https://unstats.un.org/unsd/nationalaccount/sna2025.asp

---

## Declarations

**Funding.** None declared.

**Competing interest.** The author declares no competing interest.

**Relationship to the main text.** This commentary was written as part of the same revision cycle; its
standards statements were checked against the sources above and against the OECD compilation guide, and its
arithmetic is quoted from the main text, Section 10.2, without recomputation. It cites no paragraph number of
the 2025 revision except where the guide itself is the source of the number.

**Use of AI assistance.** Drafting and iterative review were assisted by GLM (Z.ai), Qwen (Alibaba Cloud) and
DeepSeek AI, as in the main text. All statements about the standards are the author's to confirm before
submission, for the reason given in B15.
