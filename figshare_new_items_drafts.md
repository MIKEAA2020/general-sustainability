# Figshare upload — ONE item: SafeTransition preprint + verification deposit as supplementary

**Type: Preprint.** The manuscript PDF is the visible, indexable file;
the complete verification deposit rides as a supplementary file. (The
old shared item, DOI 10.6084/m9.figshare.33764023, is untouched and
remains the assessment paper's.)

---

## Files to upload (in this order; first file = main)

1. **Main:** `/home/user/arena agent 1/paper rewrites/latex/paper1_safetransition_master_v4.pdf` (16 pp.)
2. **Supplementary:** `/home/user/SafeTransition_1.3.0_verification_deposit.zip` (3.3 MB, 108 entries — library + 59 tests, certificates + standalone checker, 24-check Northern-cod benchmark with committed results, six-family scaling study, dashboard, the companion paper's 25-check grid verifier + results + report, search records, and the master v4 source inside `manuscripts/`; SHA256SUMS 90; `bash run_all.sh` reproduces everything)
3. **Supplementary (visible text):** `/home/user/arena agent 1/paper rewrites/latex/paper1_safetransition_ems_supplementary_v7.md` (S1–S11)

## Title (paste exactly)

    SafeTransition: exact rational certification of transition safety for sustainability assessment

## Description (paste exactly)

SafeTransition, a Python library for certifying the transition safety of sustainability assessments, is presented. The library implements the assessment-operator framework: typed floor constraints evaluated on supplied tubes whose status is declared exact or certified conservative, scalarized aggregate operators over the positive weight cone, and backward recursions over state and belief spaces. Infeasibility is returned as a Farkas certificate, a nonnegative multiplier vector with vanishing weighted constraint sum and negative weighted bound; certificates serialize to canonical JSON for a standalone checker importing no library modules. All semantic assessment, recursion, threshold, and certificate computations run in exact rational arithmetic; floating point is confined to rendering and performance measurement. Twenty-four exact checks re-derive the deposited benchmark, and a scaling study over six parameterized families verifies closed-form answers to 256-variable eliminations and margins whose reduced denominators reach 323 bits. A single-file dashboard embeds the readings' verification provenance. Distributed under the MIT licence.

Supplementary deposit: the complete verification archive — library source
and 59-test suite; serializable Farkas certificates with a standalone
checker importing no library modules; the exact-rational regulated-fishery
benchmark (Northern cod, NAFO 2J3KL, biomass-limit reference point 884.6
kt) with committed results; the six-family scaling study; the single-file
dashboard; the companion manuscript's exact-integer grid verifier (25
checks) with committed results and report; preserved systematic
literature-search records; and the LaTeX source of this manuscript. From
the archive root, `bash run_all.sh` verifies SHA-256 integrity and
reproduces every result. The archive is CC BY 4.0; the library subtree is
MIT. Development mirror: https://github.com/MIKEAA2020/general-sustainability
(folder `figshare_master`). Companion assessment deposit:
https://doi.org/10.6084/m9.figshare.33764023

## Settings

- **Licence:** CC BY 4.0 (code subtree MIT — stated in the description
  and inside the archive)
- **Categories:** Applied mathematics not elsewhere classified; Other
  environmental sciences not elsewhere classified; Environmental
  assessment and monitoring
- **Keywords:** SafeTransition; exact arithmetic; rational arithmetic;
  verification; Farkas certificate; viability theory; sustainability
  assessment; transition safety; Python; reproducibility
- **Related material (add after publishing):** none required — the
  companion deposit DOI is already in the description

## After minting (recommended)

The manuscript cites its deposit as "figshare, supplementary deposit of
this article" (no DOI yet — figshare mints at publication). Send me the
minted DOI and I'll build master v5 with the real DOI in the availability
row and the reference entry, then you publish it as **version 2** of the
item. Until then every citation resolves via this item's DOI either way.
