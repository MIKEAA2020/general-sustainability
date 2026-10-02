#!/usr/bin/env python3
"""Compile separately the paper09 cod+Edwards main and the corrected ARV companion.
This is typesetting/asset validation, not proof of numerical or Lean claims.
"""
from pathlib import Path
import hashlib,re,shutil,subprocess,tarfile,tempfile
R=Path('/home/user');B=R/'content_audit/claim_alignment';out=B/'compile';out.mkdir(exist_ok=True)
archive=R/'tools/tectonic-0.15.0-x86_64-static.tar.gz'
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='b00fcaf562798fcaf92d4ee8391080bb0728b2309cea84f94efa06949417d450'
with tarfile.open(archive,'r:gz') as t:
 assert t.getnames()==['tectonic'];bin=t.extractfile('tectonic').read()
assert hashlib.sha256(bin).hexdigest()=='4df19452c202c5bef9f7c7e4a01a3f2b9d5199f0a1f73b70b4fe1bffbc9837f6'
exe=Path(tempfile.mkdtemp(prefix='paper09-tectonic-'))/'tectonic';exe.write_bytes(bin);exe.chmod(0o700)
# The main inherits \graphicspath{{../}}. Resolve it via verified b09 source assets.
for name in ('figs_e2_v3','figs_e4'):
 link=out/name
 if link.is_symlink():link.unlink()
 elif link.exists():raise RuntimeError('Unexpected existing asset path: '+str(link))
 link.symlink_to(R/'b09'/name,target_is_directory=True)
rows=[]
for key,name,assets in (
 ('paper09_main','paper09_cod_certification_v32.tex',('figs_e2_v3','figs_e4')),
 ('paper09_arv_companion','paper09b_arv_certification_v2.tex',('figs_arv',))):
 folder=out/key;folder.mkdir(exist_ok=True)
 shutil.copyfile(B/'drafts'/name,folder/name)
 for asset in assets:
  link=folder/asset
  if link.is_symlink():link.unlink()
  elif link.exists():raise RuntimeError('Unexpected existing asset path: '+str(link))
  link.symlink_to(R/'b09'/asset,target_is_directory=True)
 result=subprocess.run([str(exe),'-p','--keep-logs',name],cwd=folder,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=360)
 (folder/'compile.stdout.log').write_text(result.stdout)
 log=(folder/Path(name).with_suffix('.log')).read_text(errors='replace') if (folder/Path(name).with_suffix('.log')).exists() else ''
 refs=re.findall(r'LaTeX Warning: (?:Reference|Citation).*?undefined|There were undefined references|There were undefined citations',log)
 missing=re.findall(r'File [`\'\"]?[^`\'\"\n]+(?:not found|not readable)',result.stdout)
 pdf=folder/Path(name).with_suffix('.pdf');ok=result.returncode==0 and pdf.is_file() and not refs and not missing
 rows.append((key,ok,result.returncode,len(refs),len(missing),pdf.stat().st_size if pdf.exists() else 0))
 print(key,'PASS' if ok else 'FAIL','exit',result.returncode,'refs',len(refs),'missing',len(missing),'pdf_bytes',pdf.stat().st_size if pdf.exists() else 0,flush=True)
 if not ok:print('log tail',result.stdout[-2000:].replace('\n',' | '),flush=True)
(out/'paper09_results.tsv').write_text('document\tpass\texit\tundefined_references\tmissing_assets\tpdf_bytes\n'+''.join(f'{a}\t{int(b)}\t{c}\t{d}\t{e}\t{f}\n' for a,b,c,d,e,f in rows))
assert all(x[1] for x in rows),rows
