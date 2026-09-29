import json, urllib.request, re, sys
_tok = open('/home/user/uploads/github_pat.txt').read()
TOK = re.search(r"github_pat_[A-Za-z0-9_]+", _tok).group(0)
OWNER, REPO = "MIKEAA2020", "general-sustainability"
H = {"Authorization": "Bearer "+TOK, "Accept": "application/vnd.github+json"}
br = sys.argv[1]
r = urllib.request.Request(f"https://api.github.com/repos/{OWNER}/{REPO}/git/trees/{br}?recursive=1", headers=H)
t = json.load(urllib.request.urlopen(r))
paths = [e["path"] for e in t["tree"] if e["type"]=="blob"]
json.dump(paths, open(f"/home/user/tree_{br}.json","w"))
print(br, "total blobs", len(paths))
