# What the four links changed (2026-11-13)

Read in full before replying: NFI Brochure, ground-plot page, photo-plot page, MAGPlot Open Government
record, MAGPlot v1.2 data dictionary.

## 1. My MAGPlot recommendation was half right, and half wrong

I told you to tick MAGPlot because it reaches Yukon. It does — the v1.2 dictionary's `MAGP_SITE_ID`
ranges list **YT explicitly, alongside NFI, QC, SK, MB, AB, NB, BC, PEI, ON, NT, NS, NL and NFM**. Nunavut
is the only missing jurisdiction. That part holds.

What I got wrong: I framed MAGPlot as a design-based add-on to the NFI ground plots. It is not.
**MAGPlot is a harmonized compilation of contributor data, not a statistical sample with a common
design.** Each jurisdiction contributed in its original format; records were cleaned and harmonized
into eight relational tables (five site, three tree). The site tables carry the contributing program
per site (`magp_site_sources`), and plot type is encoded per record (`L`, `S`, `R`, `V`, `B`), so
design heterogeneity is **visible** — but it is not one design that yields one variance. For the
Canadian case, which needs a design-based uncertainty on biomass change, that makes MAGPlot
**supplementary coverage evidence**, not the primary observation.

And in v1.2 it carries **tree data only — no compiled volume, no biomass, no age, no soil, no
ecological plot attributes** (Michael's email says this; the dictionary confirms the eight tables are
sites, treatment, disturbance, tree header, trees, tree condition, tree removed, plus QC flags).

## 2. Therefore: hold MAGPlot to v1.3, keep NFI ground plots moving

Michael offered exactly this: v1.3 is due before end-2026 and will include **compiled volume and biomass
from an augmented version of the same compiler the NFI ground plot program uses**.

Accept. Rationale:
- Using one compiler across NFI ground plots and MAGPlot is what a boundary-matched comparison needs;
  reimplementing biomass compilation across twelve jurisdictions from raw DBH/height would add a
  large unforced error and a second, incomparable estimator.
- It costs calendar time but zero analytical quality — and the Canadian items in F13 (1 and 4) are
  served by the **NFI ground plots**, which need not wait.
- Version timing interacts with the paper: v1.3 is "before end of 2026", so it lands in the same window
  as the provider reviews anyway.

## 3. Data dictionaries are newer than what we had been citing

The ground-plot page now lists **5.2.3 and 5.3.2** (we had been referencing 6.0 for the 2018–2027
second remeasurement period, which is the *photo-plot* dictionary version — the photo-plot page lists
**6.1** for 2018–2027, plus 5.2 for 2007–2017). Compilation procedures remain **2.4**.

So my earlier "dictionary v6.0" line in the request form was wrong for ground plots. The reply now asks
the office to confirm which version accompanies the extract and says we will cite theirs. This is a
small error caught before it went into a signed DUA, which is the right time to catch it.

## 4. The photo-plot request stays declined — and the brochure explains why properly

Design facts now on record: photo plots are **2 km × 2 km cells on a 20 km national grid with reduced
sampling in the north**; ground plots are installed at **about 8 % of photo plots**; a ground plot is a
**11.28 m radius large-tree plot**, a **10.0 m radius sapling/tall-shrub cover plot**, two **30 m woody
debris and surface substrate transects**, and a **soil pit**. NFI is delivered by **thirteen
government agencies: ten provinces, two territories and the Government of Canada**.

That "about 8 %" and "reduced sampling in the north" is the quantified answer to *why* the 262.190
million ha of northern geography behaves the way it does in the change estimate — the coverage question
in F13 item 4. It is documentation, not data, so it still belongs in the email thread, not in the
ticked boxes.

## 5. Biomass equations — the constraint is publication status, not access

Michael: only **published** equations are shareable (Lambert et al. 2005; Ung et al. 2008, listed on
p. 85 of the Compilation Procedures); in-house, draft, temporary or specialized equations are not
distributed. So the request cannot be "send me the equations" — it has to be "tell me **which**
`BMEQ_*` IDs resolve to which published source, and which compiled values rest on unpublished
equations". That is what the reply now asks, with no request for restricted material.

## 6. What this means for the paper, concretely

| F13 item | Effect of this exchange |
|---|---|
| **1** — primary calibrated national AGB comparison | NFI ground plots proceed now; Canada becomes the case with a designed, remeasured physical observation. MAGPlot deferred to v1.3. |
| **4** — Canadian coverage/uncertainty reconciliation | Still two-sided: the office is **actively investigating the RSE/CI discrepancy**, and the brochure gives the design facts (8 % ground-plot rate, northern thinning) needed to describe coverage honestly. |
| **5** — map reference designs | Unaffected. |
| **2** — Cameroon/Australia modules | Unaffected. |

Risk to manage: a DUA-constrained plot layer **cannot enter the deposited reproduction package**. The
package will carry derived national/ecozone aggregates plus the script, and the DUA terms will be
stated in the data-availability section.

## 7. Next actions

1. Send the reply (`R1b_NFI_reply_to_Michael.md`) — it answers his question in two sentences and
   resolves MAGPlot, equations and coordinates in one round.
2. Sign and return the DUA when it arrives; expect up to two weeks of collaborator review after that.
3. When the extract lands: verify which dictionary/compilation version shipped, check `BMEQ_*`
   resolution, and check that the projection/remeasurement flags are populated before any aggregation.
4. Do not chase the RSE/CI question again — it is with their team, and a second request would just
   duplicate it.
