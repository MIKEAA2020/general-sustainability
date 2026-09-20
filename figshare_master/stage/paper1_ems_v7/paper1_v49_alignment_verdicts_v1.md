# Paper 1 (v48→v49) — alignment round: abstract/keywords/suppl/deposit/zips vs the audit findings (v1)

**Scope.** The user asked whether the title, abstract, keywords, and
individual sections of the assessment paper, its supplementary files,
the master deposit, the EMS paper, and the zip packages are all current
and aligned with the latest versions and findings; what reproducibility
code exists for the supplements; and the canonical file paths. This
report records what the check found and changed.

**Result: 2 misalignments found and fixed (one in the abstract, one
broken supplement pointer); everything else verified aligned; deposit
metadata refreshed; 2 zips (re)built. Ships as v49 (34 pp., compiled
clean).**

---

## 1. Misalignment 1 (paper): abstract gap sentence contradicted the corrected body

The v48 abstract said: *"The gap **coincides exactly** with the states
whose reserve cannot finance a staged transition."* The v47 body fix
established the failure set {x<1, s₁<2, s₂<2} ⊋ I, with I its
aggregate-certified part — and the paper's own Table 1 row defines I
with all four conditions. Counterexample on the paper's datum: (0, 3,
0) has x < 1 but FAST handles it, so it is not in the gap. The audits
(v46) caught the body phrasing; the abstract's different wording
escaped the v47 sweep. **Fixed in v49**: "The gap is the
aggregate-certified part of the states whose reserve cannot finance a
staged transition; mixing plans as fractional blends closes every
aggregate-certified state exactly, while alternating between plans over
time does not." — exactly matching Theorem 9(i) (blend window nonempty
⟺ s₁ + s₂ ≥ 2) and the corrected Prop 11/§6.3 language.

**Verified aligned (no change):** title (version-free), keyword block
(7 keywords, version-free), all section content (the v47/v48 fixes are
in place and probe-verified), Table 1 (correct), conclusions, and the
provenance comment (updated to describe v49).

## 2. Misalignment 2 (cross-document): the promised "(S8)" enumeration did not exist in the supplement

The paper (§ on the software artifact) states the 25 grid-verifier
checks "are enumerated in the Supplementary Material (S8)" — but
supplementary S8 is the **citation** section. No supplement section
enumerated the 25 checks (they lived only in the deposit's verification
report and script). **Fixed**: new supplementary section
**S12 — "The assessment paper's grid verifier: the 25 exact checks"**
(execution record, scale-40 table summary, all 25 checks enumerated in
the verifier's [T1]–[T10] groups with the mapping to Propositions 3–4,
Theorem 5, Remark 7; re-run instruction), and the paper's pointer
changed to **(S12)**. Supplementary ships as **v5** (v4 + S12;
S1–S11 untouched).

## 3. Everything else verified aligned (no change)

| Artifact | Verdict |
| --- | --- |
| EMS paper v7 | Clean: only cross-refs into paper-1 territory are "rescue witness x = 3/2", "twenty-four checks", and the deposit DOI — all correct. No renumbering dependence |
| Master manuscript v1 | Same three refs, all correct |
| EMS highlights v7 | Clean |
| Supplementary v4 (S1–S11) | Clean: references only the EMS manuscript's own sections; S4's "twenty-four" is the benchmark suite (correct); no stale paper-1 numbering, no "Section 4.12", no old theorem numbers |
| SafeTransition_v1.3.0.zip | Zip-wide grep for stale strings (Section 4.12, old theorem numbers, "3.2 kt", "income trough", v46): **none** |
| figshare stage dirs | Current manuscripts correct; refreshed with the new verdicts + suppl v5 (below) |

## 4. Deposit and zip refresh (this round)

- `pkg/README.md`: stale "Section 4.12 benchmark figure" → **6.3**;
  manuscripts listing updated (suppl v5; four verdicts reports).
- `pkg/CITATION.cff`: deposit version **1.2.0 → 1.3.0** (staging = the
  next figshare version; upload still blocked on user token).
- `pkg/SHA256SUMS`: regenerated over the refreshed tree.
- `pkg/manuscripts/` and both stage dirs: suppl v5 replaces v4 (v4
  remains in the latex archive, repo history, and any previously
  uploaded figshare version); verdicts reports v47/v48/v49 added
  alongside the earlier round's report.
- `paper1_figshare_deposit.zip` (workspace root): **regenerated** — the
  previous snapshot was stale (34 entries, v31–v44 era).
- `paper1_assessment_separation_v49.zip` (workspace root): **new**
  source package in the v42/v43 pattern (README, tex, pdf, figures,
  graphical abstracts).

## 5. Reproducibility inventory (what exists, where it is already wired)

Already **in** the supplement (v5): S4 (the software's 24 benchmark
checks, enumerated), S5 (package artifact tree + one-command
reproduction), S9 (certificate protocol: serialization, independent
checker, negative tests), S10 (scaling study), S12 (the assessment
paper's 25 grid checks, enumerated — new).

Available artifacts, all deposited and cited:
`verification/typed_false_positive_instantiation.py` (grid verifier,
25 checks, stdlib-only, ≈ 36 s) + committed JSON + human-readable
report; `figure_code/` (6 scripts, incl. `make_benchmark_v44.py` and
the graphical-abstract pipelines); `figures/` (4 deposited PNGs);
`safetransition/` (9 modules, 59 tests, `run_all.sh`,
`check_safe_transition_cert.py` independent checker,
`benchmarks/scaling_study.py` + committed results, examples, dashboard);
top-level `run_all.sh` (environment check → SHA-256 integrity → all
verifications). Nothing further is needed for the supplements; the
deposit is the canonical execution route.

## 6. Ship state

- `paper1_assessment_separation_v49.tex` / `.pdf` (34 pp.; v48
  preserved; probes: new abstract sentence present, old absent, S12
  pointer present).
- `paper1_supplementary_v5.md` (S1–S11 unchanged; S12 new).
- Deposit refreshed as in §4; two zips rebuilt; repo pushed.

*Alignment round: 2 misalignments fixed (abstract gap language; S12
enumeration + repoint), 5 artifact classes verified clean, deposit
metadata refreshed. The abstract finding is the same lesson as the v47
round: identical overclaims in different wording survive phrase-search
sweeps — only claim-level paraphrase sweeps catch them.*
