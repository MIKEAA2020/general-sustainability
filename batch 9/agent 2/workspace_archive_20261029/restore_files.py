"""Restore an explicitly selected, hash-verified subset; never silently overwrite."""
import argparse,json,hashlib,os,urllib.request,urllib.parse
from pathlib import Path,PurePosixPath
A=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--prefix',required=True);p.add_argument('--destination',type=Path,default=Path.cwd());p.add_argument('--commit');g=p.add_mutually_exclusive_group(required=True);g.add_argument('--list',action='store_true');g.add_argument('--restore',action='store_true');a=p.parse_args()
index=json.loads((A/'RESTORE_INDEX.json').read_text());rows=[x for x in index['files']if x['workspace_path']==a.prefix or x['workspace_path'].startswith(a.prefix.rstrip('/')+'/')]
if not rows:raise SystemExit('No indexed files match that prefix')
if a.list:
 for r in rows:print(r['workspace_path'],r['bytes'],r['repository_path'])
 print('Files:',len(rows),'bytes:',sum(r['bytes']for r in rows));raise SystemExit()
commit=a.commit or json.loads((A/'publication_receipt.json').read_text())['published_commit']
if len(commit)!=40 or any(c not in '0123456789abcdef'for c in commit):raise SystemExit('Require a full pinned commit SHA')
root=a.destination.resolve();headers={'User-Agent':'verified-workspace-restore'}
if os.environ.get('GITHUB_TOKEN'):headers['Authorization']='Bearer '+os.environ['GITHUB_TOKEN']
for r in rows:
 rel=PurePosixPath(r['workspace_path'])
 if rel.is_absolute()or '..'in rel.parts:raise SystemExit('Unsafe indexed local path')
 dest=root.joinpath(*rel.parts)
 if root not in dest.resolve().parents:raise SystemExit('Destination escapes restore root')
 if dest.exists():
  if not dest.is_file()or hashlib.sha256(dest.read_bytes()).hexdigest()!=r['sha256']:raise SystemExit('Refuse to overwrite different file: '+str(dest))
  continue
 url='https://raw.githubusercontent.com/'+index['repository']+'/'+commit+'/'+urllib.parse.quote(r['repository_path'],safe='/')
 with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=90)as response:b=response.read(r['bytes']+1)
 if len(b)!=r['bytes']or hashlib.sha256(b).hexdigest()!=r['sha256']:raise SystemExit('Downloaded content identity mismatch: '+str(rel))
 dest.parent.mkdir(parents=True,exist_ok=True);tmp=dest.with_name(dest.name+'.restore-partial');tmp.write_bytes(b);tmp.replace(dest);print('Restored',rel)
print('Verified restoration complete:',len(rows),'files')
