#!/usr/bin/env python3
"""Compile source-specific staged TeX in isolated asset-aware folders.
Compiles paper01's current live main/supp as consistency baselines, not repairs.
Uses tools/tectonic if installed, otherwise verifies and unpacks the exact
remote-backed tools/tectonic-0.15.0-x86_64-static.tar.gz to temporary space.
Requires cached or network-accessible TeX bundle resources.
"""
from pathlib import Path
import subprocess, shutil, re, sys, tarfile, tempfile, hashlib
root=Path('/home/user');base=root/'content_audit/claim_alignment';build=base/'compile';build.mkdir(exist_ok=True)
def compiler():
 exe=root/'tools/tectonic'
 if exe.is_file():return exe
 archive=root/'tools/tectonic-0.15.0-x86_64-static.tar.gz'
 assert hashlib.sha256(archive.read_bytes()).hexdigest()=='b00fcaf562798fcaf92d4ee8391080bb0728b2309cea84f94efa06949417d450'
 with tarfile.open(archive,'r:gz') as tf:
  assert tf.getnames()==['tectonic']
  binary=tf.extractfile('tectonic').read()
 assert hashlib.sha256(binary).hexdigest()=='4df19452c202c5bef9f7c7e4a01a3f2b9d5199f0a1f73b70b4fe1bffbc9837f6'
 scratch=Path(tempfile.mkdtemp(prefix='paper2-tectonic-'))/'tectonic'
 scratch.write_bytes(binary);scratch.chmod(0o700)
 print('Using SHA-verified compiler from remote-backed archive:',scratch,flush=True)
 return scratch
TECTONIC=compiler()
assets={
 'ws': [('figs_ws4','content_audit/scientific_validity/ws/figs_ws4')],
 'comp': [('figs_comp2','content_audit/scientific_validity/comp/figs_comp2')],
 'psuff': [('figs_bs2','content_audit/scientific_validity/psuff/figs_bs2')],
 'arv': [('figs_arv','content_audit/scientific_validity/arv/figs_arv')],
 'e1': [('figs_e1','b11/figs_e1'),('figs_e3','b11/figs_e3')],
 'paper01': [('figs_p2','b01/figs_p2')],
 'paper01_compat': [('figs_p2','b01/figs_p2')],
 'paper01_supp': [('figs_p2','content_audit/claim_alignment/assets_paper01_supp/figs_p2')],
 'paper01_supp_compat': [('figs_p2','content_audit/claim_alignment/assets_paper01_supp/figs_p2')],
}
jobs=[
 ('ws','paper11c_worked_systems_audit_v2.tex',False),
 ('comp','paper03_computational_certification_v16.tex',False),
 ('comp_supp','paper03_computational_certification_v16_supplementary.tex',False),
 ('minimax','paper04_minimax_dual_certificates_v16.tex',False),
 ('ebc','paper05_exact_belief_computation_v16.tex',False),
 ('psuff','paper02_probabilistic_sufficiency_v12.tex',False),
 ('arv','paper09b_arv_certification_v2.tex',False),
 ('e1','paper11_forecasting_baselines_v64.tex',False),
 ('paper01','paper01_obstruction_calculus_v63.tex',True),
 ('paper01_compat','paper01_obstruction_calculus_v63.tex',False),
 ('paper01_supp','paper01_obstruction_calculus_v63_supplementary.tex',True),
 ('paper01_supp_compat','paper01_obstruction_calculus_v63_supplementary.tex',False),
]
selected=sys.argv[1:] or [j[0] for j in jobs]
results=[]
for key,filename,is_live in jobs:
 if key not in selected:continue
 folder=build/key;folder.mkdir(exist_ok=True)
 source=(root/'papers' if is_live else base/'drafts')/filename
 assert source.exists(),source
 shutil.copyfile(source,folder/filename)
 for name,target in (assets.get(key,[]) if key in ('paper01_supp','paper01_supp_compat') else assets.get(key.replace('_supp',''),[])):
  link=folder/name
  if link.is_symlink():link.unlink()
  elif link.exists():raise RuntimeError('Asset path already exists: '+str(link))
  link.symlink_to(root/target,target_is_directory=True)
  if key=='e1':
   # Original composite's \graphicspath{{../}} points one level upward.
   upper=build/name
   if upper.is_symlink():upper.unlink()
   elif upper.exists():raise RuntimeError('Asset path already exists: '+str(upper))
   upper.symlink_to(root/target,target_is_directory=True)
 cmd=[str(TECTONIC),'-p','--keep-logs',filename]
 try:
  run=subprocess.run(cmd,cwd=folder,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=300)
  (folder/'compile.stdout.log').write_text(run.stdout)
  lg=(folder/Path(filename).with_suffix('.log'))
  final_log=lg.read_text(errors='replace') if lg.exists() else ''
  badrefs=re.findall(r'LaTeX Warning: (?:Reference|Citation).*?undefined|There were undefined references|There were undefined citations',final_log)
  missing=re.findall(r'File [`\'\"]?[^`\'\"\n]+(?:not found|not readable)',run.stdout)
  pdf=folder/Path(filename).with_suffix('.pdf')
  ok=run.returncode==0 and pdf.exists() and not badrefs and not missing
  results.append((key,ok,run.returncode,len(badrefs),len(missing),pdf.stat().st_size if pdf.exists() else 0))
  print(f'{key:12s} {"PASS" if ok else "FAIL"} exit={run.returncode} refs={len(badrefs)} missing={len(missing)} pdf_bytes={pdf.stat().st_size if pdf.exists() else 0}',flush=True)
  if not ok:print('  log tail:',run.stdout[-950:].replace('\n',' | '),flush=True)
 except subprocess.TimeoutExpired:
  results.append((key,False,'timeout',-1,-1,0));print(key,'TIMEOUT',flush=True)
(build/'results.tsv').write_text('family\tpass\texit\tundefined_references\tmissing_assets\tpdf_bytes\n'+''.join(f'{k}\t{int(ok)}\t{rc}\t{r}\t{m}\t{n}\n' for k,ok,rc,r,m,n in results))
if not all(ok for _,ok,*_ in results):raise SystemExit(1)
