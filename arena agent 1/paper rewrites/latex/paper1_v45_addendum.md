# v45 — layout, accessibility, and data-anchoring pass

## Changes

1. **Figure 4**: the "index stays certified" annotation moved up and left
   into the whitespace above the green line, below the legend (figure script
   updated; all 24 exact checks re-pass).
2. **Layout**: `elsarticle` switched from the double-spaced `review` option
   to `3p` (single column, single spacing, full journal text width) with
   `\emergencystretch=2.5em`. Page count fell from 59 to **32**; the layout
   change also cured the pre-existing 9.07 pt display overfull. Two
   layout-exposed defects were fixed at the source: the claim-layer table is
   now separated from the preceding paragraph, and the reference-list
   Zenodo/figshare URLs are `\url{}` (breakable). Remaining overfull: the
   single pre-existing 2.43 pt frontmatter box.
3. **Paragraph breaks**: the blend/time-sharing delimitation remark and the
   benchmark's datum, schedule, and takeaway paragraphs are split at natural
   points.
4. **Data anchor (benchmark section close)**: the datum's units are anchored
   to a real regulated floor --- the Northern cod (NAFO 2J3KL) spawning-stock
   limit reference point, LRP = 884.6 kt (NCAM M-shift series; DFO, 2016,
   SAR 2016/026; the stock was about a third of the LRP in 2015). Reading the
   floor at this LRP puts the witness opening stock at ≈1.42 Mt (the
   mid-1980s assessed neighbourhood) and the adverse trough at ≈531 kt
   (inside the critical zone). Stated as an anchoring of units, not a fitted
   case study; the companion scored test's negative certificate (no
   structural model beat persistence; RMSE 98 vs 115–206 kt) is cited as
   discipline. New reference: DFO (2016).
5+6. **New Section 5.3, "A translation guide for readers from neighbouring
   fields"**: a terminology table mapping the paper's central objects (typed
   floors, scalarized operator, licensing thresholds, acceptance gap, rescue
   set/threshold, impossibility region, blend vs time-sharing, exact-tube
   semantics) onto MCDM/OR, control/viability, and environmental
   modelling/governance vocabulary. Former 5.3–5.5 renumber to 5.4–5.6; all
   cross-references updated; contribution item (x) added.

## QA

- Compile exit 0; **32 pages**; 4 images; 0 `??`; overfull: only the
  pre-existing 2.43 pt frontmatter box; abstract unchanged.
- Ordering verified in the render: translation guide (5.3) before Scope
  delimitations (5.4); data anchor inside 4.12 before Conclusions; all
  former "Section 5.5" references now read 5.6.
- Master deposit updated (benchmark figure + script) and re-verified from a
  fresh extraction: ALL REPRODUCTION CHECKS PASS (7/7 images
  byte-identical; 25/25 artifact checks; benchmark 24/24).
