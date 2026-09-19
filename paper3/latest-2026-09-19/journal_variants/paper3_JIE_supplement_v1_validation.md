# JIE package validation and audit record

Date: 2026-09-19 (Asia/Tehran)

## Deliverables

- `rendered/paper3_JIE_submission_v1.tex` — revised main source.
- `paper3_JIE_submission_v1.md` — synchronized Markdown mirror.
- `rendered/paper3_JIE_submission_v1.pdf` — compiled 11-page main PDF.
- `paper3_JIE_supplement_v1.tex` — standalone supplementary source.
- `paper3_JIE_supplement_v1.pdf` — compiled 13-page supplement PDF.
- `cover_letter_JIE_v1.md` — Journal of Industrial Ecology cover letter for the linked three-paper set.
- `assets/typed_ledger_readout.svg` and `assets/typed_ledger_readout.png` — Figure 1 artwork.

## Build

Commands:

```text
/home/user/tools/tectonic --keep-logs --outdir /home/user/revision/jie_latest/rendered /home/user/revision/jie_latest/rendered/paper3_JIE_submission_v1.tex
/home/user/tools/tectonic --keep-logs --outdir /home/user/revision/jie_latest /home/user/revision/jie_latest/paper3_JIE_supplement_v1.tex
```

Both commands exited with status 0 and completed PDF conversion. The final TeX logs report 11 pages for the main article and 13 pages for the supplement. The main log contains only underfull-box diagnostics in the wide application table; no overfull boxes, TeX errors, undefined references, missing delimiters or emergency stops were reported. The supplement log contains no such layout or compilation diagnostics.

## Content and scope audit

- PASS — author, date, Independent Researcher affiliation, hyperlinked ORCID and hyperlinked email are present in both TeX documents and the Markdown mirror.
- PASS — Figure 1 renders the geographic and active-pool variables as `A_geo` and `A_act`, with each label retained beside its associated box.
- PASS — the main article and supplement use formal author–date citations for the methods, accounting-standards and delay-dynamics records.
- PASS — the verified companion records are cited with their public DOI links: `10.6084/m9.figshare.33942469` and `10.6084/m9.figshare.33942487`.
- PASS — the main article retains the required Qwen (Alibaba Cloud) and DeepSeek AI declaration, author review/editing and responsibility statement.
- PASS — competing-interests, funding and A.A. CRediT declarations are present.
- PASS — the supplement retains the typed-ledger certification stack, theorem inventory, delay-dynamics interface, application tables and operational weak/strong-sustainability regimes.
- PASS — supplement formal statements remain traceable to the archived v49 source lineage; no new theorem extension or calibrated empirical claim was introduced.
- PASS — the main Markdown mirror is 259 lines with a 4,262-word body count after excluding displayed and inline mathematics, links and the reference list; this is below the 6,000-word limit.
- PASS — no navigation/diary, chat-artifact, superseded-version, editorial, apology or self-congratulatory wording remains in the main article or supplement.
- PASS — credentials scan found no credential file or credential text in the JIE deliverable directory; the credential was not read, printed, hashed or staged.

## Structural checks

A dependency-free source check returned PASS for:

- exactly one `document` environment in each TeX source;
- balanced `equation`, `align` and `longtable` environments in the supplement;
- all application-table labels (`tab:g3p`, `tab:phosphate`, `tab:fisheries`);
- required delay, double-counting, weak/strong and evidence-status strings;
- matched Figure 1 asset references in the main source and Markdown mirror;
- DOI and contact hyperlinks in the TeX sources.

The main article is within the requested word limit; the supplement is separate.

## SHA-256

```text
a029e0a124220e7067c642229b3a89ad0eb6d4a078d56f94e4e8a3e218321a6f  rendered/paper3_JIE_submission_v1.tex
3dea875bd3126b5d9f7ef086f42a5a30e5c725354dde205e1383a06085c79502  rendered/paper3_JIE_submission_v1.pdf
b928fb9c1dd48135723268f3ba7e1f8bafba49307737a8ce487ef334d340642d  rendered/paper3_JIE_submission_v1.log
5d7f24d0ee47e1137408a37341d697ee108db28c8398b203976ed392d7d850a2  paper3_JIE_supplement_v1.tex
d5c11ae507b1c238bf5a35974ae24f92755884b688be438b2f7c90f41eb11d34  paper3_JIE_supplement_v1.pdf
60786e9aed2854a48c0a5900146b6889c21cf897f7fa29c7d63fe352437986a9  paper3_JIE_supplement_v1.log
0f5d7b9e29746f478728333cb763089b186dff9ccb5c7e18b344f3991159ef22  assets/typed_ledger_readout.svg
f11697ea537fcfafc997061b1c07fdcb3d7a5063fd63822bf799df471719dc20  assets/typed_ledger_readout.png
8ce94ace92fec5d8819d78befc817ab25769b0c665b6d9cdcba1ec28982189eb  cover_letter_JIE_v1.md
d9d0dfffcf2836f96eca340979160f3d1def9e8ab01b908754bdbddb5be0a571  rendered/JIE_cover_letter_v1.tex
9659b6be3ceb05e29e1014205789c910985ebe09159bbe8ace419cac9ef7c88e  rendered/JIE_cover_letter_v1.pdf
2059d1b83e18a14635e4ae49101cb4e6835e387306e6e9c27344c42b6be3b9f5  rendered/JIE_cover_letter_v1.log
```

## Evidence/status note

The public article record is contextual only: `https://doi.org/10.6084/m9.figshare.33942451`. The local expanded package is not represented as an externally uploaded or newly assigned DOI record. The two companion records and the delay-dynamics record are cited only as their public records.
