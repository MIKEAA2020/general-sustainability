#!/usr/bin/env python3
"""Prepare standalone LaTeX source zips; no portal calls or rights assertions."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import re,shutil,hashlib,json
R=Path('/home/user');O=R/'content_audit/journal_submission/preprints_org_ready_2026-10-02';O.mkdir(exist_ok=True)
items=[('03','paper03_computational_certification_v22','paper 2 family/03_computational_certification'),('09','paper09_cod_certification_v42','paper 2 family/09_cod_with_arv')]
allout=[]
for tag,stem,asset_root in items:
 dest=O/('paper'+tag);dest.mkdir(exist_ok=True)
 tex=R/'papers'/f'{stem}.tex';pdf=tex.with_suffix('.pdf');assert tex.is_file() and pdf.is_file()
 s=tex.read_text();figs=re.findall(r'\\includegraphics(?:\[[^]]+\])?\{([^}]+)\}',s)
 pkg={tex.name:tex}
 for fig in figs:
  source=R/asset_root/fig
  assert source.is_file(),(stem,fig,source)
  pkg[fig]=source
 if tag=='03':
  si=R/'papers/paper03_computational_certification_v22_supplementary.tex';si_pdf=si.with_suffix('.pdf')
  assert si.exists() and si_pdf.exists();pkg[si.name]=si
  shutil.copyfile(si_pdf,dest/si_pdf.name)
 shutil.copyfile(pdf,dest/pdf.name)
 archive=dest/(stem+'_latex_source.zip')
 with ZipFile(archive,'w',ZIP_DEFLATED) as zz:
  for name,p in sorted(pkg.items()):zz.write(p,arcname=name)
 manifest={'stem':stem,'article_pdf':pdf.name,'source_zip':archive.name,'figure_files':figs,'supplement_pdf':'paper03_computational_certification_v22_supplementary.pdf' if tag=='03' else None,'sha256':{name:hashlib.sha256(p.read_bytes()).hexdigest() for name,p in pkg.items()},'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()}
 (dest/'MANIFEST.json').write_text(json.dumps(manifest,indent=2))
 print('PREPARED',tag,'figs',len(figs),'source_files',len(pkg),'zip_bytes',archive.stat().st_size,'pdf_bytes',pdf.stat().st_size)
 allout.append(manifest)
(O/'MANIFESTS.json').write_text(json.dumps(allout,indent=2))
