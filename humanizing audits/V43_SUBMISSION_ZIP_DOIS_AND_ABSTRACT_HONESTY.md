# V43 round record — the submission zip, the DOI insertion round, and the abstract honesty decision

**Task 102, 2026-09-19.** Owner directives: "1- for main manuscript,
journal portal wants LaTeX with figures and tables compressed into a
.zip format that will compile into a PDF for peer review. 2- insert
dois 3- for abstract-phrase, choose honesty, and keep abstract below
260 words."

All three directives are commissions, and all three are executed this
round as **v41** (the wave-24 pipeline): the reference list gains the
16 Crossref-verified DOIs of the Task-100 round, the abstract takes
Task 97's honesty resolution with the below-260 bound held, and the
main-manuscript submission zip is built and compile-verified.  The
cover letter takes its flagged one-edit sync; the supplementary
package README is refreshed to the v41 checksums.

---

## Part I — directive 3: the abstract-phrase decision, resolved for honesty

Task 97's standing flag (V37 Part I item 4; V38 Part III; V39/V40/V41
residuals): the abstract's opening "Delays destabilise
renewable-resource systems; those studied so far are ecological."
overstates once Adamson & Hilker (2020) is cited — delayed *knowledge*
is an informational delay, not an ecological one.  V38 priced the
honest repair ("ecological or informational") at +2 journal words
(258 → 260), breaching the standing below-260 bound, and recorded the
two compliant paths: the net-zero restructure (rejected — it degrades
the classic-declarative opening) or a compensating trim.

The owner's word — "choose honesty, and keep abstract below 260
words" — selects the honest repair **with** the compensating trim:

* **A1 (the honesty upgrade):** "those studied so far are ecological."
  → "those studied so far are ecological or informational." (+2 words)
* **A2 (the compensating trim, V38's recorded option):** "Under
  periodic review the two rules respond oppositely:" → "Under periodic
  review the rules respond oppositely:" (−1 word; only two rules exist
  in the paper and the count is carried by paragraph one's "compares
  two rules"; zero content loss)

**Net +1: 258 → 259 journal words** — verified at three levels: the md
(journal_words == 259), the tex abstract environment (259, gate
≤ 259), and the rendered text layer (259, cap 259).  The abstract is
byte-identical to v40's outside these two edits; every claim needle
survives (the loop-gain statement keeps its "at the calibrated point"
scope qualifier; the Hopf/artefact/Neimark–Sacker/five-regime/grounds-
scales needles all render).  The retired phrases join the rejection
list as permanent regression gates (the pre-honesty form with its
terminal period included, so the new honest form can never match it).

The cover letter's flagged opening sentence (V41's residual 3) is
upgraded with it — one edit: "studied almost exclusively inside the
ecology — maturation, recruitment, self-limitation" → "studied almost
exclusively as ecological or informational delays — maturation,
recruitment, self-limitation, or the harvester's delayed knowledge of
the stock" (+6 words; the one-page form stands; the "Why Theoretical
Ecology" paragraph's A&H sentence now echoes the informational class
explicitly).

## Part II — directive 2: the DOI insertion round (the frozen gate re-baselined)

The 16 missing journal-article DOIs — every one Crossref-verified in
the Task-100 round (V41 Part II: title, container, volume and pages
matched against the manuscript's entries; never guessed) — are pasted
as anchored ` doi:` suffixes, exactly in the verified form, one
anchored edit per reference line, after the terminal period:

| Entry | DOI |
|---|---|
| Aiello & Freedman 1990 | doi:10.1016/0025-5564(90)90019-u |
| Carpenter et al. 2011 | doi:10.1126/science.1203672 |
| Church & Lessard 2022 | doi:10.1016/j.physd.2021.133072 |
| Church & Queirolo 2024 | doi:10.1007/s10884-023-10279-x |
| Costantino et al. 1995 | doi:10.1038/375227a0 |
| Engelborghs et al. 2002 | doi:10.1145/513001.513002 |
| Faria & Magalhães 1995 | doi:10.1006/jdeq.1995.1144 |
| Gurney et al. 1980 | doi:10.1038/287017a0 |
| Moxnes 1998 | doi:10.1287/mnsc.44.9.1234 |
| Scheffer & Carpenter 2003 | doi:10.1016/j.tree.2003.09.002 |
| Scheffer et al. 2009 | doi:10.1038/nature08227 |
| Zhang, Shen & Chen 2013 | doi:10.1007/s11071-013-0928-2 |
| Ezekiel 1938 | doi:10.2307/1881734 |
| Hayes 1950 | doi:10.1112/jlms/s1-25.3.226 |
| Hutchinson 1948 | doi:10.1111/j.1749-6632.1948.tb39854.x |
| Ludwig, Jones & Holling 1978 | doi:10.2307/3939 |

The 7 already-pinned DOIs are untouched (each re-verified byte-exact);
the 11 books and the 2 DFO grey-literature entries stay DOI-less (the
V41 Part II dispositions: a style decision, and no DOI exists).
After the round the reference block carries **23 `doi:` suffixes in
the 38-entry list** — machine-counted at the md, tex, and rendered-text
levels, all three equal.  The frozen-reference gate re-baselines:
v32==…==v37 (36 lines) with v38 == v39 == v40 byte-identical, and
**v41 == v40 + exactly the 16 declared appends** (reconstructed
byte-for-byte in the review ledger).

## Part III — directive 1: the main-manuscript submission zip

`arena agent 1/paper rewrites/submission_zips/paper4_delay_dynamics_v41_TE.zip`
(872 KB; 5 entries; sha256
`231e97bba946684dd83565188fc94ba9eedf1f52c50bb87c1132f6983699583b`):

```
latex/paper4_delay_dynamics_v41.tex    the main file (article class,
                                        standard packages only; inline
                                        references and tables --- no
                                        BibTeX, no external table files)
latex/paper4_delay_dynamics_v41.pdf    the compiled PDF (45 pp, one
                                        figure), byte-identical to the
                                        shipped repository PDF
latex/figs_p4/fig2_five_regime_topology_v2.png   the figure at the
                                        direct relative path
figs_p4/fig2_five_regime_topology_v2.png          the same PNG (sha256
                                        a4bbddc6…) at the
                                        \graphicspath{{../}} path
README.txt                             compile instructions
```

Design: the P1 v28 main-zip precedent (`latex/` + tex/pdf + the
parent-level figure folder) **plus** the Task-101 lesson applied — the
figure rides at BOTH resolution paths (the direct relative path the
tex asks for first, and the `../` graphicspath path), so the archive
compiles in either layout.  The "tables" of the portal's requirement
are inline `tabular`/`longtable` environments in the tex (verified: no
`\input`/`\include`/`\bibliography` anywhere in the source), so the
figure is the only non-standard file the compile needs.

**Compile verification (both scenarios, fail-loud):**
* **Scenario A (in place):** extract; tectonic-compile
  `latex/paper4_delay_dynamics_v41.tex` — error-free, **45 pages**,
  the text layer **byte-identical** to the shipped PDF, the Figure 1
  page (pdf page 27) **pixel-identical** at 100 dpi.
* **Scenario B (flat):** copy the tex to the archive root and compile
  there — exactly the Task-101 failure scenario — error-free, 45
  pages, same text layer, same figure page.  The direct-path
  `figs_p4/` copy resolves.
* The zip build is deterministic and idempotent (rebuild → identical
  sha256); the entry list is exact; the tex/pdf/figure bytes inside
  are identical to the repository artifacts.

## Part IV — an honest finding: tectonic PDF non-determinism (recorded, and why the record pins what it pins)

The round surfaced that **tectonic's PDF output is not
byte-reproducible across compiles: the PDF embeds the compile-time
`creationDate`** (verified: three same-source compiles → three PDF
md5s, identical text layers, `creationDate` the only metadata
difference).  The **tex** is fully byte-reproducible (three consecutive
full-battery builds → tex md5 `9690145302dd5ffe790a5cee799de0b7`,
stable across every re-run).

Consequence for the discipline: a PDF md5 identifies a *build*, not a
*source state* — which is why the house records pin the tex md5 as the
identity and record the PDF md5 of the one shipped build.  This round
follows it: after the full battery, **one final build was run and
pinned** (`paper4_delay_dynamics_v41.pdf`, md5
`9a63b3d62eb6be1eb3f217a362941b2f`), and no rebuild happened afterward
— the submission zip and the supplementary README both carry that
build's checksums.  (An earlier in-session rebuild cycle had
momentarily staled these; both artifacts were rebuilt against the
pinned PDF before anything was committed — the git delta contains only
the final state.)

## Part V — the supplementary package refresh (in place)

`submission_zips/paper4_supplementary_v8.zip`: the supplement document
is unchanged (no supplement file touched by the v41 round), so the
package version stays v8 and the README refresh is in place (the
built-asset precedent): the Manuscript line advanced to the v41
filename + md5s with the one-line round description; the Package-built
paragraph gained the v41 refresh sentence;
`verification/packaging_refresh_2026-09-19_v41.md` added; MANIFEST
regenerated (91 entries).  Payload byte-identity verified file-by-file
(89 files unchanged); entry count 91 → 92.  Both sha256 recorded:
OLD `ed8e99679494e32e106c9af64587ab0ebabdac379c6850ce36b643cf00a776bd`
(git history) → NEW
`f241150821beb9f2b1fd92e646e5dde8b966d2fe455806c17a9ef4d5fd146684`.
Idempotent re-run verified.

## Part VI — implementation record (the wave-24 fail-loud pipeline)

All in `batch 7 (audits of agent arena 1 paper rewrites)/wave24/`:

1. **`make_v41.py`** — authors v41 = v40 + exactly the 18 anchored
   edits (2 abstract + 16 DOI appends; 18 changed lines: 5, 7, and the
   16 reference lines; line count 906 unchanged; every unchanged line
   byte-identical).  Gates: 1,473 math spans multiset-equal; numerics ==
   the 16 DOI strings' own 48 digit-tokens (raw and stripped); word
   tokens == the declared delta (or/informational +1 each, two −1, the
   DOI letter-tokens); the abstract == v40's + the 2 edits, at 259
   journal words; frozen blocks byte-identical; the References block ==
   v40's + the 16 appends (38 entries; 23 `doi:`; the 7 pinned
   byte-identical); the Supplementary paragraph byte-identical; the
   rejection list 0-hit (53 strings, incl. the 2 new wave-24 gates);
   resolver 0-unresolved; supp v8 untouched; idempotent.
2. **`patch_wave24.py`** — generates `build_latex_v24.py` and
   `check_pdf_v41.py` from the wave-23 parents by asserted anchored
   replacement (10 + 7 patches; the docstrings and the tex header
   comment regenerated; the parents untouched).
3. **`build_latex_v24.py`** — the inherited wave-19/20/21/22/23 battery
   retargeted to v41: md-level gates vs v40; pandoc conversion; the
   full needle battery + the wave-24 gates (the honest abstract form
   present, the trimmed phrase absent, the 16 DOIs present in the tex,
   23 `doi:` counted wrapping-tolerantly); the rejection scanner (49
   banned strings) 0-hit on md AND tex; three consecutive
   byte-identical builds (tex md5 `9690145302dd5ffe790a5cee799de0b7`);
   45 pages; 1 figure; overfull 10 (inherited).
4. **`check_pdf_v41.py`** — 10 page-1 + 107 body needles; the rendered
   abstract **259 journal words**; spine order 5<6<7<8<9; 2 URI
   annotations; the honest form rendered and both retired phrases
   absent from the rendered text; all 16 DOIs rendered (both
   hyphen-break variants, whitespace-stripped — the Zhang DOI breaks
   across a line at one of its own hyphens); 23 `doi:` in the rendered
   text; 0 rejection hits (52 strings); the v8 pointer rendered; AI
   declaration last; 11 pages rendered for VLM.
5. **`review_v41.py`** — the A/B/C/D/E ledger ALL CHECKS PASS: the
   reconstruction gate (v41 == v40 + the 18 edits); the chain (v32…
   v37 frozen; v38==v39==v40; v41 == v40 + the 16 appends); prior
   checksums unchanged (now including v40's md/tex); the supplement
   ledger (B1-B7); the tex md5 == the three builds; the wave-24 gates
   across md/tex/rendered layers.
6. **`build_submission_zip_v41.py`** — Part III above.
7. **`refresh_package_v41.py`** — Part V above.
8. **VLM verification** (glm-5v-turbo): page 1 — 5/5 (the title
   verbatim; the byline with ORCID and email; the abstract's first
   sentence quoted verbatim with "ecological or informational"; no
   rendering defects).  The references page — the DOI-suffixed entries
   quoted verbatim (Aiello & Freedman with its DOI; Beretka & Vas; the
   Adamson entry with its pinned DOI); clean formatting.  The final
   declarations page — the three declaration subsections with the AI
   declaration last and verbatim.  (One honest note: the VLM
   transcribed the Aiello DOI's trailing "-u" as "-n" — a small-render
   OCR confusion; the machine text-layer gate verifies the exact byte
   string `doi:10.1016/0025-5564(90)90019-u`, so this is a reading
   quirk, not a defect.)

Final artifacts: `paper4_delay_dynamics_v41.md` (md5
`10cafbbdbce794954bdab4449d89e3d3`) + `latex/
paper4_delay_dynamics_v41.tex` (md5 `9690145302dd5ffe790a5cee799de0b7`)
/ `.pdf` (45 pp; the pinned build, md5 `9a63b3d62eb6be1eb3f217a362941b2f`)
+ `submission_zips/paper4_delay_dynamics_v41_TE.zip` (sha256
`231e97bb…`) + the refreshed `paper4_supplementary_v8.zip` (sha256
`f2411508…`) + the synced cover letter.  v40 and every prior version
untouched on disk and in history.

## Honest residuals

1. **The Zenodo deposit staleness** — owner-side action, unchanged
   (V39's flag; refresh the record with the final files before citing
   `10.5281/zenodo.22554217`).
2. **Book DOIs** — not inserted (the V41 Part II style decision:
   Theoretical Ecology's reference style does not require them); the
   same Crossref round can pin them with `type=book` if ever wanted.
3. **The 31-path systemic figure-path fix** across the other papers'
   latex folders — owner-gated, unchanged (V42 Part III; this round
   applies the remedy to P4's own zip but takes no action on the other
   waves' territory).
4. **Submission-time checks** — the venue's current author guidelines
   (length policy, citation style, supplementary policy) and the
   editorship masthead are checked at submission time (V37's notes);
   the cover letter declares the 45-page length and the supplement
   rather than hiding them.
5. **The tectonic `creationDate` non-determinism** (Part IV) —
   recorded as a standing fact of the toolchain; the discipline (pin
   the tex md5; record the shipped build's PDF md5; do not rebuild
   after pinning) is now written down for future rounds.
6. The cover letter gains 6 words on its opening sentence (the flagged
   one-edit sync); its one-page form is preserved.
