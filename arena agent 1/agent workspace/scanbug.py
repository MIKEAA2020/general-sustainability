import re,sys,glob
def scan(f):
    s=open(f, encoding="utf-8").read()
    out=[]
    for m in re.finditer(r"for (\w+) in \[(.*?)\]:", s, re.S):
        var=m.group(1); body=s[m.end(): m.end()+1500]
        first=[l for l in body.split("\n") if l.strip()][0]
        if ("chk(" in first or "check(" in first) and var not in first:
            out.append((var, first.strip()[:100]))
    return out
for f in sys.argv[1:]:
    r=scan(f)
    if r: print("SUSPECT", f, r)
print("scanned", len(sys.argv)-1, "files")
