"""Replacement for the lost temporary acquisition helper, not its original bytes.
Default: report missing C18 source files. --restore retrieves missing exact blobs;
never overwrite a differing file. Credentials stay external and are not printed.
"""
from pathlib import Path
import argparse,json,hashlib,base64,re,os
import requests
R=Path('/home/user');C=R/'ecomod_audit_remediation_C18_A01'
def main():
    a=argparse.ArgumentParser(description=__doc__);a.add_argument('--prefix',default='');a.add_argument('--restore',action='store_true');z=a.parse_args()
    index=json.loads((C/'metadata/repository_recovery_C18_A01.json').read_text());s=requests.Session();token=os.environ.get('GITHUB_TOKEN')
    if not token:
        m=re.search(r'github_pat_[A-Za-z0-9_]+',(R/'uploads/github_pat.txt').read_text());token=m.group()if m else None
    if token:s.headers['Authorization']='Bearer '+token
    missing=[];matched=0
    for x in index['files']:
        if not x['local_path'].startswith(z.prefix):continue
        p=(C/x['local_path']).resolve()
        if not p.is_relative_to(C.resolve()):raise RuntimeError('Unsafe path')
        if p.exists():
            if hashlib.sha256(p.read_bytes()).hexdigest()!=x['sha256']:raise RuntimeError('Refuse overwrite: '+x['local_path'])
            matched+=1;continue
        missing.append(x)
        if not z.restore:continue
        q=s.get('https://api.github.com/repos/MIKEAA2020/general-sustainability/git/blobs/'+x['git_blob'],timeout=120);q.raise_for_status();b=base64.b64decode(q.json()['content'])
        if len(b)!=x['bytes']or hashlib.sha256(b).hexdigest()!=x['sha256']:raise RuntimeError('Identity mismatch')
        p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
    print(json.dumps(dict(matching=matched,missing=len(missing),restored=len(missing)if z.restore else 0,missing_paths=[x['local_path']for x in missing]),indent=2))
if __name__=='__main__':main()
