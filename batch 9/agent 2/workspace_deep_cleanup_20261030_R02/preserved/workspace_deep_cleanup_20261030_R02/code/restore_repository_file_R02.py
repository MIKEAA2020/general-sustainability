"""Restore selected indexed creations without cloning or overwriting differing files.
Use --prefix uploads/paper06_assessment_separation_v76.txt --destination /home/user/.cache/restored --restore.
Default is list-only. Index maps original paths to exact immutable Git blobs.
Private credential stays external; no token is printed, written or committed.
"""
from pathlib import Path
import argparse,json,hashlib,base64,re,os
import requests
W=Path(__file__).resolve().parents[1]
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--prefix',required=True);p.add_argument('--destination',type=Path,default=Path('/home/user/.cache/restored_R02'));p.add_argument('--restore',action='store_true');a=p.parse_args()
    index=json.loads((W/'RESTORE_INDEX_R02.json').read_text());items=[x for x in index['files']if x['workspace_path']==a.prefix or x['workspace_path'].startswith(a.prefix.rstrip('/')+'/')]
    if not items:raise SystemExit('No matching indexed paths')
    print('Selected',len(items),'files;',sum(x['bytes']for x in items),'bytes')
    if not a.restore:
        for x in items:print(x['workspace_path'])
        return
    dest=a.destination.resolve();dest.mkdir(parents=True,exist_ok=True)
    s=requests.Session();t=os.environ.get('GITHUB_TOKEN');credential=Path('/home/user/uploads/github_pat.txt')
    if not t and credential.exists():
        m=re.search(r'github_pat_[A-Za-z0-9_]+',credential.read_text());t=m.group()if m else None
    if t:s.headers.update({'Authorization':'Bearer '+t})
    for x in items:
        rel=Path(x['workspace_path']);f=(dest/rel).resolve()
        if not f.is_relative_to(dest):raise RuntimeError('Unsafe destination')
        if f.exists():
            if hashlib.sha256(f.read_bytes()).hexdigest()!=x['sha256']:raise RuntimeError('Refuse overwrite: '+str(rel))
            continue
        z=s.get('https://api.github.com/repos/MIKEAA2020/general-sustainability/git/blobs/'+x['git_blob'],timeout=120);z.raise_for_status();b=base64.b64decode(z.json()['content'])
        if hashlib.sha256(b).hexdigest()!=x['sha256']:raise RuntimeError('SHA256 mismatch')
        f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(b)
    print('Every selected file restored/hash-verified. Choose a destination with adequate budget.')
if __name__=='__main__':main()
