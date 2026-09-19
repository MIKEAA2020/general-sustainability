# JIE v2 package validation and audit record

Date: 2026-09-19 (Asia/Tehran)

## Revision policy

This package is revision v2. It is stored under new filenames and a new directory; the earlier v1 files are not overwritten.

## Build

Commands:

```text
/home/user/tools/tectonic --keep-logs --outdir /home/user/revision/jie_revision_v2/rendered /home/user/revision/jie_revision_v2/rendered/paper3_JIE_submission_v2.tex
/home/user/tools/tectonic --keep-logs --outdir /home/user/revision/jie_revision_v2 /home/user/revision/jie_revision_v2/paper3_JIE_supplement_v2.tex
/home/user/tools/tectonic --keep-logs --outdir /home/user/revision/jie_revision_v2/rendered /home/user/revision/jie_revision_v2/rendered/JIE_cover_letter_v2.tex
```

All three builds exited with status 0: 11-page main article, 13-page supplement and one-page cover letter. The main log contains only underfull-box diagnostics in the wide application table. No errors, overfull boxes, undefined references, missing delimiters or emergency stops were reported.

## Content audit

- PASS — abstract is self-contained and has no citations or references to supplementary material, records or other papers.
- PASS — ORCID and email are explicit `\\href` links with visible linked text in the main TeX source.
- PASS — CRediT statement retains A.A.'s contribution without an external guidance URL.
- PASS — article and supplement scanned for self-referential, editorial, change-log, diary, chat-artifact and internal-version language.
- PASS — Figure 1 retains the geographic and active-pool labels beside their associated boxes.
- PASS — methods, accounting-standards and delay-dynamics records remain formally cited outside the abstract.
- PASS — main body remains below the 6,000-word limit; supplement is separate.
- PASS — no credential file or credential text is included in the v2 deliverable directory.

## Scope and evidence

The theorem inventory remains traceable to the existing source lineage. No new theorem, calibrated empirical claim, forecast or software-submission claim was introduced. The public article DOI is contextual only; the expanded local v2 package is not represented as a new external upload or DOI record.

## SHA-256

The checksums below cover the v2 article, supplement, cover letter and Figure 1 assets. They are updated after the final build.


```text
a231cb7e103ad224d00921e6ebdef63b2362f4c41cbfcc44f9b472c480e817dc  rendered/paper3_JIE_submission_v2.tex
bbca8ae3c6ea99037e54bb690bbe7f320ea58d8bbf1138469141233cbc18fa4e  rendered/paper3_JIE_submission_v2.pdf
10c0c82d854ea00ae6cb94d7e37356f24cb677d06bc1e266fb10ab4f871cf88b  rendered/paper3_JIE_submission_v2.log
1d17333e932b214496c51e25c1360c8e3e7aadd646324354b2f8aa19d8d8a090  paper3_JIE_supplement_v2.tex
82d7a1a11af0bae1bf9d0f613ccce656ea4e03635aa7734b2fe3fd1e22fca0ea  paper3_JIE_supplement_v2.pdf
ef126401d4b1d3318fac58a4c54805a8cd9e72dd13401b63db09deddee4dca0b  paper3_JIE_supplement_v2.log
d9d0dfffcf2836f96eca340979160f3d1def9e8ab01b908754bdbddb5be0a571  rendered/JIE_cover_letter_v2.tex
c34645cdfbf10533aeca819ee673540840e3810eec247adf63562341ff7147  rendered/JIE_cover_letter_v2.pdf
6fe2e8fa9f619f2d7d502b3ae073d634bc3d2d5599010fc532e82a111c7ef9af  rendered/JIE_cover_letter_v2.log
0f5d7b9e29746f478728333cb763089b186dff9ccb5c7e18b344f3991159ef22  assets/typed_ledger_readout.svg
f11697ea537fcfafc997061b1c07fdcb3d7a5063fd63822bf799df471719dc20  assets/typed_ledger_readout.png
fb2ffd927c27225660972c40943188dd9e19db690bf320e74bf7e7d0ab3c5f0f  paper3_JIE_submission_v2.md
8ce94ace92fec5d8819d78befc817ab25769b0c665b6d9cdcba1ec28982189eb  cover_letter_JIE_v2.md
```
