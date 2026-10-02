#!/usr/bin/env python3
"""Execute recovered, Git-blob-verified E2/E4 checkers in scratch only.
Path shims are recorded verbatim. Original checker/source/manuscripts stay intact.
The historical validators are NOT automatically proof of paper09's composite.
"""
from pathlib import Path
from difflib import unified_diff
import hashlib,subprocess,sys,shutil
R=Path('/home/user');B=R/'content_audit/paper09_rerun';G=Path('/tmp/paper09-fresh-repo');T=Path('/tmp/paper09-source-checkers');T.mkdir(exist_ok=True)
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=G,text=True).strip()=='180b5aa082005701f127c62f19d3a8865067eabc'
src=(B/'verified_runners/paperE2_cod_intervention_v29_verification.py').read_text()
repls=[('REPO = "/home/user/repo/wave_e_cod"','REPO = "/tmp/paper09-fresh-repo/wave_e_cod"'),('XTE = "/home/user/repo/arena agent 1/other documents/rerun_campaigns/results"','XTE = "/tmp/paper09-fresh-repo/arena agent 1/other documents/rerun_campaigns/results"')]
for old,new in repls:assert src.count(old)==1,old;src=src.replace(old,new)
e2=T/'paperE2_checker_pathshim.py';e2.write_text(src)
orig=(B/'verified_runners/paperE2_cod_intervention_v29_verification.py').read_text()
(B/'E2_CHECKER_PATH_ONLY.diff').write_text(''.join(unified_diff(orig.splitlines(True),src.splitlines(True),fromfile='remote verified E2 checker',tofile='scratch path shim')))
E=T/'edwards';E.mkdir(exist_ok=True)
shutil.copy2(B/'verified_runners/paperE4_edwards_intervention_v16_verification.py',E/'paperE4_edwards_intervention_v16_verification.py')
shutil.copy2(B/'original_papers/texcheck.py',E/'texcheck.py')
shutil.copy2(B/'original_papers/paperE4_edwards_intervention_v16.tex',E/'paperE4_edwards_intervention_v16.tex')
for name in ('src','results'):
 link=E/name
 if link.is_symlink():link.unlink()
 elif link.exists():raise RuntimeError('Unexpected scratch asset: '+str(link))
 link.symlink_to(G/'wave_e_edwards'/name,target_is_directory=True)
tests=[('cod_historical',[sys.executable,str(e2),str(B/'original_papers/paperE2_cod_intervention_v29.tex')],G),('cod_paper09_main',[sys.executable,str(e2),str(R/'paper 2 family/09_cod_with_arv/paper09_cod_certification_v32.tex')],G),('edwards_historical',[sys.executable,str(E/'paperE4_edwards_intervention_v16_verification.py')],E)]
for key,cmd,cwd in tests:
 try:
  done=subprocess.run(cmd,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=600)
  log=done.stdout;code=done.returncode
 except subprocess.TimeoutExpired as err:
  log=(err.stdout or b'').decode(errors='replace') if isinstance(err.stdout,bytes) else (err.stdout or '');code=124
 (B/(key+'.log')).write_text(log)
 print(key,'exit',code,'lines',len(log.splitlines()),'sha256',hashlib.sha256(log.encode()).hexdigest(),'tail',log[-250:].replace('\n',' | '),flush=True)
