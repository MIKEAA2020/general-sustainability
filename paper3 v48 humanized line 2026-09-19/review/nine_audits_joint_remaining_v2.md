# Nine audits, joint assessment of what still remains — v2 (supersedes nothing; v1 registers stand)

Scope of this pass: the audit **source files**, not my verified summaries. Two corpora I had not
opened before: the repository's own `batch 7 (audits of agent arena 1 paper rewrites)/source_audits/`
(46 files, incl. the paper-3 audit and the NFBA/Country data packages) and `agent 2 productivity
illusion/audits/` (27 files, which despite `v32/v33/v34` filenames target ECOMOD, not paper 3 — the
only paper-3 item there is the overlap check, now stale since v34 adds identifiability).

## 1. What the repo had already dispositioned (so it is NOT remaining)

`batch 7/wave4/p3_record.md` records, for v28: R11–R17, the theorem-inflation re-letters, the R₀
split, the displayed incidence blocks, Theorem 14's E ≥ 0, §9's field-difference reconciliation, the
Θ_F contradiction, the USGS single-vintage pin, §11's de-re-argument, the three uncited companions
(placeholder letters D/E/F — the source of the 5 `in review` sites I replaced in v33), and the
bounded length cut. Confirmed by grep against v32/v34: the audit's literal quotes for A1(§2.2 wording),
A2, A4, A5, A7, A8, A9, A10 and the "horizontal exhaustion"/"notation table" items return 0 — those
defects are gone.

## 2. Remaining, ranked, with what v34 changes

| # | Point (source) | Status now | Action |
|---|---|---|---|
| 1 | Notation collision (paper-3 audit, table B): "one letter, one sort" | **Live, and I made it worse**: my Def 21 closure capacity was `\lambda^{*}` beside Thm 24's multiplier `\lambda`, and my Def 23 said "with $C$ the readout matrix of Section 2.1" — v32 §2.1 defines no such object (§5.1's readout is $s=\mathcal O=Q(\theta)v$) | Re-letter Λ\* and drop C from Def 23's displays (the residual identity holds on $\ell^{\top}d_x$ directly). Prepared as v35; **not applied** — v34 stays the shipped state |
| 2 | A12: "Universal failure of weighted certification" never uses the ledger (donor limitation, incidence, laws all unused) | Persists (identity-readout instance still present, 1 site) | Author's: it is a re-scope of a headline claim, so register only — my Prop 29 already narrows it by proof obligation (uniqueness under monotone+calibrated+certifying), which is the fix that does not soften anything |
| 3 | Premium/δ\* figures "cannot be reported — component tables not held" | **Now closeable**: `batch 7/source_audits/Country_Trends.csv` is the NFBA 2025 world table by component (EFConsTotGHA / BiocapTotGHA, 1961–2025) | Computed: 2022 τ_agg = 213 d with carbon at zero biocapacity → Π_τ = 213 d (whole date); on positive-biocapacity components 538 d vs 365 d → Π_τ = 173 d; series 547/346/251/173 d (1961/80/2000/22). Script `repo_audits/` + this file; insert at Remark 33 in v35 |
| 4 | Stale citation: "Theorem 15" cited 5× with no head labelled 15 (gap in 1–20) | Present identically in v32 and v34 (0 lines of mine removed ⇒ inherited) | Author's: restore or re-letter the citation; `label_register.py` catches it automatically |
| 5 | C §1.1 structure notes: three failure modes announced as two; no-drift paragraph says the same thing thrice; §6.5.2 "leads with quarantined numbers" | Not touched by v32/v34 (my edits added Antecedents, §1.2, and the kernel; no intro surgery) | Author's wording call |
| 6 | Journal-fitness path (audit's "Practical path"): cut intro ≥60 %, theorems out of §1–2, move registered numerics to results/supplement, decide venue first | Partly satisfied by the existing md/tex split and my supp S7–S9 routing | Keep as the venue-submission checklist; it corroborates `structure_v34.md` items (i)–(iii) |
| 7 | `JOINT_AUDIT_EVALUATION.md` (127 KB), `4 audits_v33 audit.txt` (89 KB), `turnover.txt`, `caveats and residual.txt`, `human reviewer.txt`, `wave6/scan/paper3_material_ledgers.md` (52 KB) | Downloaded to `repo_audits/`, **not yet read line-by-line** | Next pass, if the author wants points 1–7 extended |

## 3. Method note

Every "still live / gone" verdict above is a substance grep against
`revision/v7/paper3_material_ledgers_v34.md` and the clone's v32 md, not against audit phrasing; the
counts quoted are from those runs. Nothing was pushed; the clone stays clean; `uploads/` untouched.
