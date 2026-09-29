import json, urllib.request, re, sys, os
_tok = open('/home/user/uploads/github_pat.txt').read()
TOK = re.search(r"github_pat_[A-Za-z0-9_]+", _tok).group(0)
OWNER, REPO, BR = "MIKEAA2020", "general-sustainability", "lean-audit-v4"
H = {"Authorization": "Bearer "+TOK, "Accept": "application/vnd.github.raw"}
def get(rp, lp):
    r = urllib.request.Request(f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{urllib.parse.quote(rp)}?ref={BR}", headers=H)
    try:
        d = urllib.request.urlopen(r).read()
    except urllib.error.HTTPError as e:
        print("FAIL", e.code, rp); return None
    if d[:1] in (b'{', b'[') and b'"message"' in d[:60] and b'"documentation_url"' in d[:2000]:
        print("ERRBODY", rp, d[:120]); return None
    open(lp,'wb').write(d)
    print("ok", len(d), lp)
    return d
for a in sys.argv[1:]:
    rp, lp = a.split("=",1)
    get(rp, lp)
