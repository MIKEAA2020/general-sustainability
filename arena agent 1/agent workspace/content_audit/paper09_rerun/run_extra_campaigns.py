#!/usr/bin/env python3
"""Rerun cited E2/E4 campaign/figure sources on the sparse remote checkout.
Byte compare tracked outputs; leave old xte/breakpoint runners untouched pending
source-year adjudication. The E4 path-only shim is preserved as a diff.
"""
from pathlib import Path
from difflib import unified_diff
import hashlib,subprocess,sys,csv
R=Path('/home/user');B=R/'content_audit/paper09_rerun';G=Path('/tmp/paper09-fresh-repo')
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=G,text=True).strip()=='180b5aa082005701f127c62f19d3a8865067eabc'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def gitsha(p):return subprocess.check_output(['git','rev-parse','HEAD:'+str(p.relative_to(G))],cwd=G,text=True,stderr=subprocess.DEVNULL).strip()
def source_verified(p):
 data=p.read_bytes();d=subprocess.check_output(['git','hash-object','--stdin'],cwd=G,input=data).decode().strip();assert d==gitsha(p),p
sources=['campaign_e2_structure_v3.py','campaign_e2_identification_v3.py','campaign_e2_cadence_v3.py','campaign_e2_depensation_v3.py','campaign_e2_allee_declared_v3.py','campaign_e2_fox_form_v3.py','make_figs_v17.py','make_figs_v19.py']
for s in sources:source_verified(G/'wave_e_cod/src'/s)
# Recover one E4 post-freeze script with a path-only local scratch adaptation.
orig=(B/'verified_runners/campaign_e4_elevation.py').read_text();old='REPO = Path("/home/user/repo")';new='REPO = Path("/tmp/paper09-fresh-repo")';assert orig.count(old)==1
adapt=orig.replace(old,new);patch=B/'E4_CAMPAIGN_PATH_ONLY.diff';patch.write_text(''.join(unified_diff(orig.splitlines(True),adapt.splitlines(True),fromfile='Git-verified E4 campaign',tofile='scratch path shim')))
shim=Path('/tmp/paper09-fresh-repo/arena agent 1/other documents/rerun_campaigns/campaign_e4_elevation.py');shim.write_text(adapt)
# Output files are copied from the archive before being overwritten, then checked.
spec=[('cod_structure',G/'wave_e_cod/src/campaign_e2_structure_v3.py',G/'wave_e_cod/src/results_struct_v3',300),('cod_identification',G/'wave_e_cod/src/campaign_e2_identification_v3.py',G/'wave_e_cod/src/results_ident_v3',900),('cod_cadence',G/'wave_e_cod/src/campaign_e2_cadence_v3.py',G/'wave_e_cod/src/results_cadence_v3',300),('cod_depensation',G/'wave_e_cod/src/campaign_e2_depensation_v3.py',G/'wave_e_cod/src/results_forms_v3',300),('cod_allee',G/'wave_e_cod/src/campaign_e2_allee_declared_v3.py',G/'wave_e_cod/src/results_forms_v3',300),('cod_fox',G/'wave_e_cod/src/campaign_e2_fox_form_v3.py',G/'wave_e_cod/src/results_forms_v3',300),('cod_figures_v17',G/'wave_e_cod/src/make_figs_v17.py',G/'wave_e_cod/src/figs_e2_v3',300),('cod_figures_v19',G/'wave_e_cod/src/make_figs_v19.py',G/'wave_e_cod/src/figs_e2_v3',300),('edwards_campaign',shim,G/'arena agent 1/other documents/rerun_campaigns/results',300)]
rows=[]
for name,script,out,timeout in spec:
 before={str(x.relative_to(G)):sha(x) for x in out.iterdir() if x.is_file()}
 try:
  run=subprocess.run([sys.executable,str(script)],cwd=G,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=timeout);code=run.returncode;log=run.stdout
 except subprocess.TimeoutExpired as e:
  code=124;log=(e.stdout or b'').decode(errors='replace') if isinstance(e.stdout,bytes) else (e.stdout or '')
 (B/(name+'.log')).write_text(log)
 after={str(x.relative_to(G)):sha(x) for x in out.iterdir() if x.is_file()}
 changed={p for p in before|after if before.get(p)!=after.get(p)}
 # All archive-directory files are included so the rerun cannot hide a changed row.
 for p in sorted(after):
  status='byte-match' if before.get(p)==after.get(p) else 'mismatch' if p in before else 'new-file'
  rows.append((name,str(script),p,code,before.get(p,''),after[p],status))
 print(name,'exit',code,'archived-files',len(before),'byte-mismatches',len(changed),'changed',sorted(changed)[:12],flush=True)
 if code!=0:print('error tail',name,log[-500:],flush=True)
with (B/'extra_outputs.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['runner','source','output','exit_code','committed_sha256','rerun_sha256','comparison']);w.writerows(rows)
