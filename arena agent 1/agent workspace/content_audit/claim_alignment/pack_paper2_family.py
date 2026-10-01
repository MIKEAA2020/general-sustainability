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
 '09b_regime_viability':(['paper09b_arv_certification_v2.tex'],{'figs_arv':root/'content_audit/scientific_validity/arv/figs_arv'}),
 '11_forecasting_baselines':(['paper11_forecasting_baselines_v64.tex'],{'figs_e1':root/'b11/figs_e1','figs_e3':root/'b11/figs_e3'}),
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
   'paper09b_arv_certification_v2.tex':'arv','paper11_forecasting_baselines_v64.tex':'e1','paper11c_worked_systems_audit_v2.tex':'ws',
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
# E1's inherited \\graphicspath{{../}} resolves sibling assets one level up.
for name in ('figs_e1','figs_e3'):
 source=root/'b11'/name;dest=out/name;dest.mkdir(exist_ok=True)
 for p in source.iterdir():
  if p.is_file():
   (dest/p.name).write_bytes(p.read_bytes())
   manifest.append((str((dest/p.name).relative_to(out)),sha256(p.read_bytes()).hexdigest()))
(out/'SHA256SUMS.tsv').write_text('path\tsha256\n'+''.join(f'{p}\t{digest}\n' for p,digest in manifest))
(out/'README.md').write_text('''# Paper 2 family — Preprints.org preparation, NOT submitted

These are **eight distinct, reviewed work families**, not a decided merged paper or a new numbering scheme. `01`, `02`, `03`, `04`, `05`, `09b`, `11` and `11c` retain the reviewed source identities. Families numbered 06–10 elsewhere are **not represented here as corrected submissions** merely because their numbers lie in the range. No submission or upload to Preprints.org has occurred.

Each subfolder has a source-specific, compiled *corrected draft* (`.tex`), a typeset PDF, and the actually referenced figure assets. Paper 01 and comp also have their supplementary `.tex` and PDF. The original paper01 live head and other reviewed live heads remain unchanged; the paper01 main abstract and supplementary author additions here are the staged compatibility variants. The E1 composite inherits `\\graphicspath{{../}}`; its referenced figures are copied both into its own folder and into the immediate parent so that this staging layout compiles unchanged. Normalize paths and deduplicate only when making a final submission bundle. Check each source's references and any submission portal requirements.

**Before submission:** decide grouping; reconcile cross-paper terms using `content_audit/claim_alignment/TERMINOLOGY_AND_PAPER01_2026-10-01.md`; run a fresh Lean build with the pinned toolchain; rerun source-matched computations after regrouping, inspect rendered final artifacts, and obtain author approval. The checks and limitations are in `content_audit/claim_alignment/PRE_GROUPING_READINESS_2026-10-01.md`. Manuscript byline is Amin Abaee; no double-blind anonymization or new contribution role was added.

`SHA256SUMS.tsv` covers packaged source, PDF and assets. For verbatim old abstracts and diffs against reviewed heads, consult `content_audit/claim_alignment/original_abstracts/` and `diffs/`. Do not mistake a successful TeX compile or verifier exit for whole-paper proof.
''')
print('paper 2 family:',len(records),'families,',len(manifest),'source/PDF/asset files')
