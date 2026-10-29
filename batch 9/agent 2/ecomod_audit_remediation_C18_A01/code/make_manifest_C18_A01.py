"""Create/verify the complete versioned publication manifest; excludes only caches."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
NAME='artifact_manifest_C18_A01.json'
def artifacts():
    return [p for p in sorted(ROOT.rglob('*')) if p.is_file()and not any(x in {'.cache','__pycache__','.git'}for x in p.relative_to(ROOT).parts)and p.name!=NAME]
def main():
    files=[]
    for p in artifacts():
        b=p.read_bytes();files.append(dict(path=str(p.relative_to(ROOT)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()))
    d=dict(version='ECOMOD C18 A01',date='2026-10-30',repository_source_pin='d21febdf35aff3b2f38c4f61b1cdbd551a220373',preserves_C17=True,files=files,total_files_excluding_manifest=len(files),total_bytes_excluding_manifest=sum(x['bytes']for x in files),excludes=['.cache','__pycache__','.git'],scope='Additive audit remediation; not a claim of physical dynamic validation')
    (ROOT/NAME).write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({k:v for k,v in d.items()if k!='files'},indent=2))
if __name__=='__main__':main()
