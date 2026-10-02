#!/usr/bin/env python3
"""Package only reviewed corrected variants as preprints.org preparation inputs.
Never overwrites live heads; source and figure bytes are copied, not symlinked.
"""
from pathlib import Path
from hashlib import sha256
import shutil,json
root=Path('/home/user');a=root/'content_audit/claim_alignment';out=root/'paper 2 family';out.mkdir(exist_ok=True)
records={
 '01_obstruction':(['paper01_obstruction_calculus_v63.tex','paper01_obstruction_calculus_v63_supplementary.tex'],{'figs_p2':a/'assets_paper01_supp/figs_p2'}),
 '02_probabilistic_sufficiency':(['paper02_probabilistic_sufficiency_v12.tex'],{'figs_bs2':root/'content_audit/scientific_validity/psuff/figs_bs2'}),
 '03_computational_certification':(['paper03_computational_certification_v16.tex','paper03_computational_certification_v16_supplementary.tex'],{'figs_comp2':root/'content_audit/scientific_validity/comp/figs_comp2'}),
 '04_minimax_dual_certificates':(['paper04_minimax_dual_certificates_v16.tex'],{}),
 '05_exact_belief_computation':(['paper05_exact_belief_computation_v16.tex'],{}),
 '09_cod_with_arv':(['paper09_cod_certification_v32.tex','paper09b_arv_certification_v2.tex'],{'figs_e2_v3':root/'b09/figs_e2_v3','figs_e4':root/'b09/figs_e4','figs_arv':root/'b09/figs_arv'}),
 '11_forecasting_baselines':(['paper11_forecasting_baselines_v64.tex'],{'figs_e1':root/'paper 2 family/figs_e1','figs_e3':root/'paper 2 family/figs_e3'}),
 '11c_worked_systems':(['paper11c_worked_systems_audit_v2.tex'],{'figs_ws4':root/'content_audit/scientific_validity/ws/figs_ws4'}),
}
manifest=[]
for group,(filenames,figs) in records.items():
 target=out/group;target.mkdir(exist_ok=True)
 for name in filenames:
  src=a/'drafts'/name;assert src.exists(),src
  assert src.read_bytes()!=(root/'papers'/name).read_bytes()
  shutil.copy2(src,target/name)
  manifest.append((str((target/name).relative_to(out)),sha256(src.read_bytes()).hexdigest()))
  key={
   'paper01_obstruction_calculus_v63.tex':'paper01_compat','paper01_obstruction_calculus_v63_supplementary.tex':'paper01_supp_compat',
   'paper02_probabilistic_sufficiency_v12.tex':'psuff','paper03_computational_certification_v16.tex':'comp',
   'paper03_computational_certification_v16_supplementary.tex':'comp_supp',
   'paper04_minimax_dual_certificates_v16.tex':'minimax','paper05_exact_belief_computation_v16.tex':'ebc',
   'paper09_cod_certification_v32.tex':'paper09_main','paper09b_arv_certification_v2.tex':'paper09_arv_companion','paper11_forecasting_baselines_v64.tex':'e1','paper11c_worked_systems_audit_v2.tex':'ws',
  }[name]
  pdf=a/'compile'/key/(name.removesuffix('.tex')+'.pdf');assert pdf.exists(),pdf
  shutil.copy2(pdf,target/pdf.name)
  manifest.append((str((target/pdf.name).relative_to(out)),sha256(pdf.read_bytes()).hexdigest()))
 for name,source in figs.items():
  dest=target/name;dest.mkdir(exist_ok=True)
  for p in source.iterdir():
   if not p.is_file():continue
   (dest/p.name).write_bytes(p.read_bytes())
   manifest.append((str((dest/p.name).relative_to(out)),sha256(p.read_bytes()).hexdigest()))
# E1's inherited \\graphicspath{{../}} resolves retained parent-level copies.
for name in ('figs_e1','figs_e3'):
 dest=out/name;assert dest.is_dir(),dest
 for p in dest.iterdir():
  if p.is_file():manifest.append((str(p.relative_to(out)),sha256(p.read_bytes()).hexdigest()))
# The paper09 main likewise inherits \\graphicspath{{../}}. Supply its
# exact remote-backed parent figure copies; no regenerated imagery is used.
for name in ('figs_e2_v3','figs_e4'):
 source=root/'b09'/name;dest=out/name;dest.mkdir(exist_ok=True)
 for p in source.iterdir():
  if p.is_file():
   (dest/p.name).write_bytes(p.read_bytes())
   manifest.append((str((dest/p.name).relative_to(out)),sha256(p.read_bytes()).hexdigest()))
(out/'SHA256SUMS.tsv').write_text('path\tsha256\n'+''.join(f'{p}\t{digest}\n' for p,digest in manifest))
(out/'README.md').write_text('''# Paper 2 family — Preprints.org preparation, NOT submitted

These are **eight intellectual/work units but nine intended Preprints.org postings**: `01`, `02`, `03`, `04`, `05`, `09` (paper09 cod+Edwards main **and an independent ARV Part II preprint with its own future DOI**), `11`, `11c`. Paper01/03 proof supplements are attached files to their mains, not additional postings. The two paper09 documents are separately compiled and will be submitted independently, then cross-linked; the live v32 source's embedded ARV section was extracted from the new main candidate, not erased from source history. Earlier `09b` standalone bytes remain retrievable from the remote Git history. See `GROUPING_DECISION_2026-10-02.md` and `POSTING_METADATA_2026-10-02.md`. Families numbered 06–08/10 elsewhere are **not represented here as corrected submissions** merely because their numbers lie in the range. No submission or upload to Preprints.org has occurred.

The paper01 lineage already has prior public preprint versions under its older title on Zenodo (DOI 10.5281/zenodo.22552616, v12) and Figshare (DOI 10.6084/m9.figshare.33716593.v2, v28). These are verified *older-version* identifiers, not Preprints.org DOIs; disclose them and confirm the portal's cross-version policy before posting the revised current-title v63 candidate. See `content_audit/claim_alignment/PRIOR_DEPOSIT_VERIFICATION_2026-10-02.md`.

Each unit has source-specific, compiled *rebuild candidates* (`.tex`), typeset PDF(s), and referenced figure assets. Paper01 and paper03 attach supplements; paper09 stages a separately titled, independently posted ARV Part II companion. The original paper01 and paper09 live heads and other reviewed live heads remain unchanged; source-specific diffs and original abstracts are retained. The paper01 main abstract and supplementary author additions remain staged compatibility variants, not separately approved publication metadata. The E1 and paper09 main composites inherit `\\graphicspath{{../}}`; their referenced figures are copied both into their own folders and their immediate parent so this staging layout compiles unchanged. Normalize paths and deduplicate only when author-approved final submission bundles are made.

**Before submission:** grouping is adopted as a working plan, but verify the terminology crosswalk (`content_audit/claim_alignment/TERMINOLOGY_AND_PAPER01_2026-10-01.md`), review all final-source diffs and the source-year xteNCAM rerun/correction (`content_audit/paper09_rerun/RERUN_REPORT_2026-10-02.md`), inspect rendered final artifacts, and obtain author approval. The declared-pin Lean default target was rebuilt in GitHub Actions (60/60); its remaining three P3 `native_decide` proof steps generate nine axiom names. The manuscript wording separates no `sorryAx`/no explicit `axiom` declaration from this compiler/runtime trust extension. The pinned *declared-exceptions* gate passed (run 36990482599); the distinct strict zero-exception gate correctly remained blocked, despite the 60/60 build. The three approved P3 source sites and nine exact names are locked pending reapproval of any change; see `lean_repro/AXIOM_POLICY_REVIEW_2026-10-02.md`. This does not turn unformalized manuscript prose into Lean theorems. The paper09 main reports a numerical-tolerance comparison for intermittent low-order floating-point drift, not cross-host raw byte identity; see `content_audit/paper09_rerun/HOSTED_DRIFT_ANALYSIS_2026-10-02.md`. Manuscript byline is Amin Abaee; no double-blind anonymization or new contribution role was added.

Recreate isolated compile logs/PDFs first with **both** `content_audit/claim_alignment/compile_drafts.py` and `content_audit/claim_alignment/compile_paper09_host.py` before rerunning the packaging script; each SHA-verifies and temporarily extracts the remote-backed `tools/tectonic-0.15.0-x86_64-static.tar.gz`. The local per-run compile copies were pruned after remote/manifest verification; their summary TSVs and run logs remain. `SHA256SUMS.tsv` covers packaged source, PDF and assets. For verbatim old abstracts and diffs against reviewed heads, consult `content_audit/claim_alignment/original_abstracts/` and `diffs/`. Do not mistake a successful TeX compile or verifier exit for whole-paper proof.
''')
print('paper 2 family:',len(records),'families,',len(manifest),'source/PDF/asset files')
