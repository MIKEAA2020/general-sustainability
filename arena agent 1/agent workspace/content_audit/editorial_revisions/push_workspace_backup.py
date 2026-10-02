#!/usr/bin/env python3
"""Safely mirror every eligible local creation onto existing source-year branch.

Requires explicit user push authorization; uses local credential only as a password
via temporary GIT_ASKPASS. Never commits/uploads the credential or generated toolchain.
For this run, compare full blob SHA against remote tree; no force or branch merge.
"""
from pathlib import Path
import os,subprocess,hashlib,tempfile,json,sys
R=Path('/home/user');REPO=Path('/tmp/editorial-push-repo');BRANCH='e2-v3-source-year';PREFIX='arena agent 1/agent workspace/'
assert (REPO/'.git').is_dir() and (R/'uploads/github_pat.txt').is_file()
def git(*args,env=None,cwd=REPO):
 return subprocess.check_output(['git',*args],cwd=cwd,env=env,text=True).strip()
parent=git('rev-parse','HEAD')
remote=git('ls-remote','origin','refs/heads/'+BRANCH).split()[0]
assert parent==remote,('remote advanced: stop/rebase',parent,remote)
raw=subprocess.check_output(['git','ls-tree','-r','-z','HEAD'],cwd=REPO)
tree={}
for x in raw.split(b'\0'):
 if x:
  a,b=x.split(b'\t',1);tree[b.decode()]=a.decode().split()[2]
excluded_dirs={'.git','.arena','.cache','.local','.venv','node_modules','__pycache__','uploads','tools'}
excluded_files={'.last_sha','p5/reps.pkl'}
excluded_names={'tree.json','tree_main.json','repo_paths.json'}
change=[];seen=0;ignored=[]
for d,ds,fs in os.walk(R):
 ds[:]=[x for x in ds if x not in excluded_dirs]
 for fn in fs:
  path=Path(d)/fn;rel=path.relative_to(R).as_posix()
  if path.is_symlink() or rel in excluded_files or fn in excluded_names or fn.endswith('.pyc'):
   ignored.append(rel);continue
  b=path.read_bytes();sha=hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()
  if tree.get(PREFIX+rel)==sha:seen+=1
  else:change.append((rel,path,sha,len(b),'changed' if PREFIX+rel in tree else 'new'))
change.sort();assert change
cred=(R/'uploads/github_pat.txt').read_bytes().strip();assert len(cred)>20
assert not any(cred in p.read_bytes() for _,p,_,_,_ in change),'credential bytes in eligible files; stop'
print('remote parent',parent,flush=True)
print('eligible changed/new',len(change),'bytes',sum(c[3] for c in change),'already identical',seen,'ignored explicit files',len(ignored),flush=True)
assert any(p=='REVISED_MANUSCRIPTS_2026-10-02.md' for p,*_ in change)
assert any(p=='content_audit/editorial_revisions/push_workspace_backup.py' for p,*_ in change)
# A custom index begins at parent tree, so absent working-tree paths never stage deletions.
with tempfile.TemporaryDirectory(prefix='editorial-push-') as temp:
 index=str(Path(temp)/'index');env={**os.environ,'GIT_INDEX_FILE':index}
 git('read-tree','HEAD',env=env)
 for i,(rel,path,sha,n,status) in enumerate(change,1):
  actual=git('hash-object','-w','--no-filters',str(path))
  assert actual==sha,(rel,actual,sha)
  git('update-index','--add','--cacheinfo',f'100644,{sha},{PREFIX+rel}',env=env)
  if i%100==0:print('staged',i,'/',len(change),flush=True)
 newtree=git('write-tree',env=env)
 oldtree=git('rev-parse','HEAD^{tree}')
 assert newtree!=oldtree
 ident={'GIT_AUTHOR_NAME':'Arena Agent','GIT_AUTHOR_EMAIL':'agent@arena.ai','GIT_COMMITTER_NAME':'Arena Agent','GIT_COMMITTER_EMAIL':'agent@arena.ai'}
 msg=f'Preserve revised manuscript versions and outstanding workspace creations\n\nMirror {len(change)} new/changed workspace files (manuscripts, supplements, compiled PDFs, evidence, audit artifacts and reproducibility scripts) under {PREFIX}. Exclude credentials/tool downloads/caches. Editorial versions are local review candidates, not submissions.'
 commit=git('commit-tree',newtree,'-p',parent,env={**env,**ident},cwd=REPO) if False else subprocess.check_output(['git','commit-tree',newtree,'-p',parent],input=msg+'\n',text=True,cwd=REPO,env={**env,**ident}).strip()
 local_tree={}
 xx=subprocess.check_output(['git','ls-tree','-r','-z',commit],cwd=REPO)
 for x in xx.split(b'\0'):
  if x:
   a,b=x.split(b'\t',1);local_tree[b.decode()]=a.decode().split()[2]
 assert all(local_tree.get(PREFIX+rel)==sha for rel,_,sha,_,_ in change)
 # Need credentials only for the duration of push; no secret in command arguments or files.
 ask=Path(temp)/'askpass.py'
 ask.write_text('#!/usr/bin/env python3\nimport sys\nfrom pathlib import Path\nq=" ".join(sys.argv[1:]).lower()\nprint("x-access-token" if "username" in q else Path("/home/user/uploads/github_pat.txt").read_text().strip())\n')
 ask.chmod(0o700)
 pushenv={**os.environ,'GIT_ASKPASS':str(ask),'GIT_TERMINAL_PROMPT':'0'}
 # Recheck immediately before non-force push. If remote moved Git rejects a non-FF update.
 assert git('ls-remote','origin','refs/heads/'+BRANCH).split()[0]==parent
 p=subprocess.run(['git','push','origin',f'{commit}:refs/heads/{BRANCH}'],cwd=REPO,env=pushenv,text=True,capture_output=True,timeout=240)
 if p.returncode:raise RuntimeError('push rejected/failed: '+p.stderr[-1200:])
 print('push accepted:',p.stderr.strip()[-250:],flush=True)
 back=git('ls-remote','origin','refs/heads/'+BRANCH).split()[0]
 assert back==commit,(back,commit)
 # Independently fetch new tip from the remote and check its full tree paths/hashes.
 subprocess.run(['git','fetch','--quiet','--filter=blob:none','--depth=1','origin',BRANCH],cwd=REPO,env=pushenv,check=True,timeout=180)
 assert git('rev-parse','FETCH_HEAD')==commit
 rawremote=subprocess.check_output(['git','ls-tree','-r','-z','FETCH_HEAD'],cwd=REPO)
 verified={}
 for x in rawremote.split(b'\0'):
  if x:
   a,b=x.split(b'\t',1);verified[b.decode()]=a.decode().split()[2]
 bad=[rel for rel,_,sha,_,_ in change if verified.get(PREFIX+rel)!=sha]
 assert not bad,bad[:12]
 print('VERIFIED remote',BRANCH,commit,'mirrored candidates',len(change),'/',len(change),'remote tree paths',len(verified),flush=True)
 print('Excluded credentials/tool downloads; no GitHub release, Zenodo deposit, or portal submission performed.',flush=True)
