from pathlib import Path
import requests,json,re,hashlib,base64
P=Path('/home/user/ecomod_followup_F08');prefix='batch 9/agent 2/ecomod_empirical_followup/F08/'
token=re.search(r'github_pat_[A-Za-z0-9_]+',Path('/home/user/uploads/github_pat.txt').read_text()).group()
s=requests.Session();s.headers.update({'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'});base='https://api.github.com/repos/MIKEAA2020/general-sustainability'
def api(method,path,**kw):
 r=s.request(method,base+path,timeout=60,**kw)
 if not r.ok:raise RuntimeError(f'GitHub {method} {path}: HTTP {r.status_code}')
 return r.json()
m=json.loads((P/'artifact_manifest.json').read_text());paths={x['path']for x in m['files']}|{'artifact_manifest.json'};assert paths=={str(p.relative_to(P))for p in P.rglob('*')if p.is_file()}
for x in m['files']:assert hashlib.sha256((P/x['path']).read_bytes()).hexdigest()==x['sha256']
head=api('GET','/git/ref/heads/main')['object']['sha'];tree=api('GET','/git/commits/'+head)['tree']['sha'];old=api('GET','/git/trees/'+tree,params={'recursive':'1'});assert not old.get('truncated');before={x['path']:x for x in old['tree']if x['type']=='blob'};assert not any(x.startswith(prefix)for x in before),'Refuse overwrite';print('Refreshed main:',head,flush=True)
entries=[];known={x['sha']for x in before.values()}
for rel in sorted(paths):
 b=(P/rel).read_bytes();expected=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest();sha=expected if expected in known else api('POST','/git/blobs',json={'content':base64.b64encode(b).decode(),'encoding':'base64'})['sha'];assert sha==expected;entries.append(dict(path=prefix+rel,mode='100644',type='blob',sha=sha))
newtree=api('POST','/git/trees',json={'base_tree':tree,'tree':entries})['sha'];check=api('GET','/git/trees/'+newtree,params={'recursive':'1'});assert not check.get('truncated');after={x['path']:x for x in check['tree']if x['type']=='blob'}
for path,x in before.items():assert after[path]['sha']==x['sha']and after[path]['mode']==x['mode'],path
assert set(after)-set(before)=={x['path']for x in entries}
commit=api('POST','/git/commits',json={'message':'Add follow-up F08 linked author ORCID, seven keywords, exact author-approved Arena.ai declaration and complete Excel source audit with direct access links; preserve all earlier revisions','tree':newtree,'parents':[head]})['sha']
state=dict(parent=head,commit=commit,published=False,verified_files=0,old_blob_paths_modes_hashes_preserved=len(before),earlier_revisions_modified=False);receipt=Path('/home/user/.cache/f08/publication_receipt.json');receipt.write_text(json.dumps(state,indent=2))
assert api('GET','/git/ref/heads/main')['object']['sha']==head,'Main advanced; no force update';api('PATCH','/git/refs/heads/main',json={'sha':commit,'force':False});state['published']=True;receipt.write_text(json.dumps(state,indent=2));assert api('GET','/git/ref/heads/main')['object']['sha']==commit
for rel,entry in zip(sorted(paths),entries):
 b=base64.b64decode(api('GET','/git/blobs/'+entry['sha'])['content']);assert hashlib.sha256(b).digest()==hashlib.sha256((P/rel).read_bytes()).digest();state['verified_files']+=1
receipt.write_text(json.dumps(state,indent=2));print('Published F08:',commit,flush=True);print('Verified files:',state['verified_files'],'all prior paths/modes/hashes preserved.',flush=True)
