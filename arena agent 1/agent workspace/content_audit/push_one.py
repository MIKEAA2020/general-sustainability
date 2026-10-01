#!/usr/bin/env python3
"""Push one reviewed artifact (optionally with its producer script), then reverse-sweep."""
import os,sys,json,base64,urllib.request,urllib.parse,pathlib
BASE='https://api.github.com/repos/MIKEAA2020/general-sustainability'
PAT=open('/home/user/uploads/github_pat.txt').read().strip()
H={'Authorization':'Bearer '+PAT,'Accept':'application/vnd.github+json','User-Agent':'content-repair','Content-Type':'application/json'}
BRANCH='e2-v3-source-year'; ROOT='arena agent 1/agent workspace/'
TIPFILE=pathlib.Path('/home/user/content_audit/push_tip.txt')
def api(path,data=None,method=None):
    return json.load(urllib.request.urlopen(urllib.request.Request(BASE+path,
       data=(json.dumps(data).encode() if data is not None else None),
       headers=H,method=method),timeout=120))
def main():
    if len(sys.argv)<3:raise SystemExit('usage: push_one.py MESSAGE_FILE /home/user/papers/file.tex [other files]')
    msg=pathlib.Path(sys.argv[1]).read_text()
    ps=[pathlib.Path(x).resolve() for x in sys.argv[2:]]
    assert all(str(p).startswith('/home/user/') and p.is_file() for p in ps)
    expect=TIPFILE.read_text().strip()
    actual=api('/git/ref/heads/'+BRANCH)['object']['sha']
    assert actual==expect, f'BRANCH DRIFT: expected {expect} actual {actual}'
    base_tree=api('/git/commits/'+actual)['tree']['sha']
    tree=[]
    for p in ps:
        rp=ROOT+str(p).removeprefix('/home/user/')
        b=p.read_bytes()
        blob=api('/git/blobs',{'content':base64.b64encode(b).decode(),'encoding':'base64'})
        tree.append({'path':rp,'mode':'100644','type':'blob','sha':blob['sha']})
        print('stage',rp,len(b),'bytes')
    new_tree=api('/git/trees',{'base_tree':base_tree,'tree':tree})['sha']
    commit=api('/git/commits',{'message':msg,'tree':new_tree,'parents':[actual]})['sha']
    api('/git/refs/heads/'+BRANCH,{'sha':commit},method='PATCH')
    print('pushed',actual,'->',commit)
    # Compare fetched tree blobs via Git API, not CDN cache.
    tt=api('/git/trees/'+commit+'?recursive=1')['tree'];lookup={x['path']:x for x in tt}
    for p in ps:
        rp=ROOT+str(p).removeprefix('/home/user/')
        assert lookup[rp]['sha']==next(t['sha'] for t in tree if t['path']==rp),rp
        print('reverse sweep identical:',rp)
    TIPFILE.write_text(commit+'\n')
if __name__=='__main__':main()
