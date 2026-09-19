# Open items for the author, from the v47 bibliography check

Nothing in this list was repaired. Each item is something a style line was asked not to decide, and each one says
what it would take to settle it, so the decision costs you a line rather than a investigation.

## 1. The draft's list holds no work the article's list lacks - verified, so nothing to add

The only candidate was an apparent `O'Neill, 1998` in the draft's reference paragraph. It is the reflow splitting
`Martinez-Alier, J., Munda, G., O'Neill, J., 1998.` mid-author-list; the article's list carries that entry in full,
and it is correct as it stands: *Weak comparability of values as a foundation for ecological economics*,
Ecological Economics 26(3), 277-286, September 1998. Checked against the publisher record via web search; the
journal, volume, pages and year in the list all match.

**The one thing this leaves open:** that entry carries no DOI in the list, while the paper has one
(`10.1016/S0921-8009(97)00120-1`). Eight of the forty entries do carry DOIs, so the list is not DOI-styled
consistently. Add the missing ones or drop the existing ones; either is a house-style decision, and a register
pass adding identifiers would be inventing citation content.

## 2. The list that ships is clean against the registry - verified

All eight DOI-bearing entries were resolved and compared with the registered metadata. Year and title agree in
every case:

| list | registered |
|---|---|
| Abaee 2026, *Delay-induced regime change in harvested stocks* | 2026, same title, `10.5281/zenodo.22554217` |
| Abaee 2026, *Periodic review as sampled governance* | 2026, same title, `10.5281/zenodo.22554297` |
| Abaee 2026, *The limits of compensatory aggregation* | 2026, same title, `10.5281/zenodo.22545740` |
| Baez 2023, *Compositional modeling with stock and flow diagrams* | 2023, same title, `10.4204/EPTCS.380.5` |
| Blomqvist 2013, *Does the shoe fit?* | 2013, same title, `10.1371/journal.pbio.1001700` |
| Güntner 2024, *Global Gravity-based Groundwater Product (G3P)* | 2024, `10.5880/G3P.2024.001` |
| Illakwahhi 2024, *Phosphorus' future insecurity, the horror of depletion...* | 2024, `10.1007/s13762-024-05664-y` |
| Lin 2018, *Ecological footprint accounting for countries* | 2018, `10.3390/resources7030058` |

Those three Zenodo records are also what would fix the year letters, if you want them fixed by hand: the draft's
reflow printed all of `2026a`, `2026b`, `2026c` as bare `Abaee, A., 2026.`, and the registered titles assign the
letters unambiguously.

## 3. Eleven works are listed that the article's prose does not cite

`Groot 2003`, `Shellenberger 2013`, `Wackernagel 2018`, `Weisz 2011`, `Patterson 2023`, `Mineral Commodity
Summaries 2026`, `Biocapacity Accounts 2021`, `National Footprint Accounts 2012`, `National Accounts 2025`,
`Applied Category Theory 2022/2023` (venue-shaped entry), `World Bank 2014` - counted by requiring `Surname,` or
`Surname et al.,` followed by the year anywhere in the body. A reference list that is longer than its text is not
an error in all journals, but it is the kind of thing a referee notices, and it is worth knowing that the draft may
have dropped some of the fifteen works it lost for this reason rather than by accident.

## 4. What the draft's own reference paragraph still contains, unedited

The draft says its list is "carried unchanged", and it is: one paragraph reflowed out of a PDF text layer, with no
`## References` heading of its own, ~34 works legible where the article lists 40, year letters dropped as above,
words glued (`Towardsomeoperationalprinciplesofsustainabledevelopment`, `horrorofdepletion,and
sustainabilitymeasures`), and one DOI present in the article's list missing from the draft's own DOI section
(`10.4204/EPTCS.380.5`). The article ships its own list, so none of this is in the PDF; it is here because the
draft is now the register baseline, and if any of that text is ever adopted wholesale these are the things that
come with it.

## 5. Not bibliography, but from the same audit and still unresolved

- The register metric has a floor near 19.5 units (the draft's own half against its own half), so v47's 21.8 is
  close to what the instrument can distinguish. Distance is reported from here on; it is not demanded below the
  floor. See `revision/v7/BASELINE_RULE.md`.
- 33% of the body's words are the draft's; the other 67% are this paper's, and only 5% of those are near-variants
  of draft paragraphs. If the intent was "the draft's prose, completed", the build has adopted the draft's *framing*
  and left its *argument* largely in place. That is the v48 question, and it is on the table, not decided.
- The v45 and v46 PDFs never carried their grafts: their LaTeX was the previous deposit's file, polished beside
  the markdown. Concretely, `The second failure is classification drift` and `Read this line in words` appear 0
  times in the v46 PDF and once each in v47's. v47's LaTeX is transpiled from its markdown and the gate reads the
  compiled text back, 293 of 293 flowing paragraphs.
