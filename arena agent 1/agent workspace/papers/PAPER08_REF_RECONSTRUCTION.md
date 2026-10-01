# paper08 — reconstruction of the damaged reference list

File: `paper08_governance_delay_v46.tex`
Result: **76 entries, one alphabetical list, no orphan tails, no glued lines.**
Compiles with tectonic 0.15.0 — PDF builds, **0 undefined references.**

---

## What the damage actually was

Not scattered typos. A single mechanical failure, repeated across the whole list:

> Every entry was split into **(authors + title)** and **(journal + volume + pages
> + DOI / publisher)**. The two halves were then sorted *separately* — heads by
> author, tails by journal name — and merged back in that wrong order.

That one mechanism explains every symptom:

- **Orphan tails** sitting alphabetically by journal while heads sat
  alphabetically by author (`Academic Press`, `Ambio`, `Astrophysics`,
  `Automatica`, `Biogeosciences`, `Cambridge University Press`, `ICES Journal`,
  `Nature`, `Science`, `SIAM`, `Springer` …).
- **Headless entries**: `Kuang, Y., 1993. Delay Differential Equations…` with no
  publisher; `Ostrom, E., 1990. Governing the Commons…` with no publisher;
  `Guckenheimer, J., Holmes, P., 1983.` with no title at all.
- **Glued lines** carrying the end of one reference and the start of the next.

The list was also **split in two** by the Supplementary material prose, and the
first entry (Åström & Wittenmark 1997) was **glued to the `\subsection*{References}`
heading itself**.

---

## Repairs

| # | Repair | Count |
|---|--------|-------|
| 1 | Split glued lines (Hutchinson/Hocherman, Karlsson/Kuang, Shertzer/Walters, Brown/Carpenter, Åström/fragment) | 5 |
| 2 | Reattach detached tails to their heads | 26 |
| 3 | Remove duplicate entries entered twice — once with a tail, once without (Adamson, Karlsson, Shertzer, Brown, Åström) | 5 |
| 4 | Remove orphan fragments duplicating tails already reattached | 6 |
| 5 | Fold stranded entries back into the alphabetical list (Aiello, Beretka, Carpenter, Brown) | 4 |
| 6 | Supply missing publishers | 5 |
| 7 | Move the Supplementary material section out of the middle of the bibliography | 1 |
| 8 | Alphabetical sort of the whole list | 76 entries |

Aiello 1990, Beretka 2020 and Carpenter 2011 existed **only** in the stranded
trailing block and are cited in the text (L219, L431; L376, L2171, L3269;
L3278), so they were **moved, not deleted**.

Missing publishers supplied: Springer, New York for Diekmann 1995, Guckenheimer
& Holmes 1983, Hale & Verduyn Lunel 1993; Cambridge University Press, Cambridge
for Ostrom 1990 and Stuart & Humphries 1996. These are certain, and only one
orphan copy of each existed, so they were written in rather than moved.

---

## Two errors caught by checking against the publisher

Both would have attached a **wrong journal to a cited work**. Recall was wrong
in both cases; verification corrected it.

1. **McManus et al. 2016 is `ICES J. Mar. Sci. 73, 227–238`** — not Cadigan 2016.
   Cadigan 2016 ("A state-space stock assessment model for northern cod") is
   **`Can. J. Fish. Aquat. Sci. 73, 296–308`**. I had assigned the ICES volume
   to Cadigan; it was retracted and both records corrected.

2. **Rose & Walters 2019 is `Fisheries Research 219, 105314`** — their "second
   opinion" on Northern cod. **`Marine Policy 109, 103695` is Sumaila et al. 2019**
   on global fisheries subsidies. The two had been crossed.

Verified against the publisher: Adamson & Hilker 2020 → *Theor Ecol* 13, 425–434
(doi 10.1007/s12080-020-00462-x); Karlsson & Gilek 2020 → *Ambio* 49, 1067–1075
(doi 10.1007/s13280-019-01265-z); Punt & Donovan 2007 → *ICES JMS* 64, 603–612.

---

## Verification

- 76 entries, **0 orphan tails**, **0 glued lines** (re-run `recon_paper08.py`).
- All 37 checked citation keys resolve to a bibliography entry. (Three reported
  "missing" — Chávez 2003, Gutiérrez 2009 — are LaTeX escapes `Ch\'avez`,
  `Guti\'errez`, present in the list.)
- Compiles: PDF builds, **0 undefined references**.

---

## Still open — flagged, not touched

1. **Two different Supplementary material passages.**
   - The `\subsection{Supplementary material}` one points at
     `paper4_supplementary_v8.md` and describes the A025 fold computation, the
     collocation mesh, and MPF material of S11.
   - The `\textbf{Supplementary material}` one after the closing rule describes
     a *different* S1–S10 set: statement inventory, epistemic-layer results,
     case-screening records, distributive-layer detail.

   They describe different supplements. A paper on Northern cod governance
   pointing at `paper4_supplementary_v8.md` looks like a merge artefact. This is
   a content question, not a bibliography one, so it is left for a decision.

2. **Two `\section*{Declarations}` blocks** — the first full, the second
   anonymised ("Anonymized for review.").

3. **The Brown 2012 / Carpenter 2011 entanglement** that item 4 deliberately
   retained is now resolved: they are separate entries, Brown carries its DOI,
   and both are in alphabetical position. Nothing was lost.
