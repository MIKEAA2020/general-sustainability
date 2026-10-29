"""Add-only publication of named archive files; never alter existing repository paths."""
from pathlib import Path
import sys,requests,re,json,hashlib,base64
A=Path(__file__).resolve().parent;R=A.parent;prefix='batch 9/agent 2/'+A.name+'/'
token=re.search(r'github_pat_[A-Za-z0-9_]+',(R/'uploads/github_pat.txt').read_text()).group();s=requests.Session();s.headers.update({'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json'});base='https://api.github.com/repos/MIKEAA2020/general-sustainability'
def api(method,path,**kw):
 r=s.request(method,base+path,timeout=90,**kw)
 if not r.ok:raise RuntimeError('GitHub HTTP '+str(r.status_code))
 return r.json()
head=api('GET','/git/ref/heads/main')['object']['sha'];tree=api('GET','/git/commits/'+head)['tree']['sha'];obj=api('GET','/git/trees/'+tree,params={'recursive':'1'});assert not obj.get('truncated');old={x['path']:x for x in obj['tree']if x['type']=='blob'};entries=[];local={}
for name in sys.argv[1:]:
 p=A/name;assert p.is_file()and p.resolve().parent==A.resolve();path=prefix+name;assert path not in old,'Refuse overwrite';b=p.read_bytes();assert token.encode()not in b;h=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest();actual=api('POST','/git/blobs',json={'content':base64.b64encode(b).decode(),'encoding':'base64'})['sha'];assert actual==h;entries.append({'path':path,'mode':'100644','type':'blob','sha':h});local[path]=b
assert entries
newtree=api('POST','/git/trees',json={'base_tree':tree,'tree':entries})['sha'];obj=api('GET','/git/trees/'+newtree,params={'recursive':'1'});assert not obj.get('truncated');after={x['path']:x for x in obj['tree']if x['type']=='blob'}
for path,x in old.items():assert after[path]['sha']==x['sha']and after[path]['mode']==x['mode']
assert set(after)-set(old)==set(local)
commit=api('POST','/git/commits',json={'message':'Add verified workspace cleanup restoration evidence; preserve all previous repository content','tree':newtree,'parents':[head]})['sha'];assert api('GET','/git/ref/heads/main')['object']['sha']==head;api('PATCH','/git/refs/heads/main',json={'sha':commit,'force':False});assert api('GET','/git/ref/heads/main')['object']['sha']==commit
for e in entries:assert base64.b64decode(api('GET','/git/blobs/'+e['sha'])['content'])==local[e['path']]
print('Published and download-verified',len(entries),'archive additions:',commit,flush=True)
