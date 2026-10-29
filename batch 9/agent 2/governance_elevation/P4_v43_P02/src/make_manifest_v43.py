from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
NAME='MANIFEST_GOVERNANCE_P4_v43_P02.json'
def artifacts():
    for p in sorted(ROOT.rglob('*')):
        if not p.is_file()or any(x in p.parts for x in ['.cache','__pycache__']):continue
        if p.suffix in ['.aux','.log','.out']:continue
        if p.is_symlink():raise ValueError('Symlink not permitted')
        yield p
if __name__=='__main__':
    files=[]
    for p in artifacts():
        if p.name==NAME:continue
        b=p.read_bytes();files.append({'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()})
    (ROOT/NAME).write_text(json.dumps({'package':'Governance P4 v43 P02; SI v10','date':'2026-10-29','scope':'Additive governance revision; ECOMOD C17 unchanged','excluded_generated_files':['.cache/**','__pycache__/**','*.aux','*.log','*.out'],'manifest_self_excluded':True,'files':files},indent=2)+'\n');print('Manifest:',len(files),'files + manifest;',sum(x['bytes']for x in files),'bytes')
