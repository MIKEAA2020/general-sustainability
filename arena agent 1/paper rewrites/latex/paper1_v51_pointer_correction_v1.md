# Paper 1 (v50→v51) — supplement-pointer correction: unwinding a cross-lineage mix-up (v1)

**What happened.** The author warned that the three lineages (assessment
paper, EMS/SafeTransition extension, figshare deposit) must not be mixed.
In the v49 round this warning was violated by misdiagnosis: the
assessment paper's citation "enumerated in the Supplementary Material
(S8)" was checked against `latex/paper1_supplementary_v4.md` — the
*EMS/SafeTransition* supplement (identical filename pattern), whose S8
is its citation section — and declared broken. In fact the assessment
paper's own supplement is the separate repo-root chain
(`paper1_supplementary_v10.md`, "Aggregate Indices and Transition
Safety"), whose **S8 is "The 25-Check Enumeration"** — the original
pointer was correct. The erroneous fix added an S12 to the EMS
supplement and repointed the paper to "(S12)" (v49/v50), sending the
paper's readers to the wrong document.

**Correction (this round).**
- Paper **v51**: the §"software artifact" pointer reverted to
  "(S8)"; consistent with the paper's own supplement and with the
  closing section's summary (S8/S9/S10). Rendered output otherwise
  identical to v50 (34 pp.).
- EMS supplement **v7** (`paper1_safetransition_ems_supplementary_v7.md`):
  the misdiagnosed S12 section removed; the supplement returns to its
  natural scope S1–S11 (S8's citation of the companion manuscripts and
  deposit was always legitimate). Deposit README and stage bundles
  updated; SHA256SUMS regenerated; deposit zip rebuilt.
- Assessment supplement **v11** (`paper1_supplementary_v11.md`, repo-root
  chain — this lineage's own home): genuine staleness fixed against the
  current main text — "Remark 6" → "Remark 7" (4 sites, the v47
  renumbering) and "Section 4.12" → "Section 6.3" (2 sites). Its
  Theorem 5(1)/(2)/(4)/(6)/(7) and other pointers verified current.

**Lineage discipline going forward.** Assessment chain (paper
`paper1_assessment_separation_vN`, supplement `paper1_supplementary_vN`
at the repo root) / EMS chain (`paper1_safetransition_ems_vN`,
`paper1_safetransition_ems_supplementary_vN`, master
`paper1_safetransition_master_vN`) / deposit (`figshare_deposit/pkg`)
never share, exchange, or stand in for each other's files. Filename
similarity must trigger a lineage check, not an edit.
