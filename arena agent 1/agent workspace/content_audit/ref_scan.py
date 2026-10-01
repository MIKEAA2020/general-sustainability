#!/usr/bin/env python3
"""Reference-content comparison with per-entry best matches; candidates, not repair instructions."""
import sys,re,json,collections,pathlib
sys.path.insert(0,'/home/user/content_audit');import scan_content as audit
sys.path.insert(0,'/home/user/p5');import mergelib,phase0_scan as gate
D=audit.D

def block(s):
    s=audit.clean(s)
    m=re.search(r'\\(?:sub)*section\*?\{References\}',s)
    if not m:
        # One live paper has lost its heading but kept the label.
        m=re.search(r'\\label\{references\}',s)
    if not m:return '',False
    tail=s[m.end():]
    for pat in [r'\\(?:sub)*section\*?\{(?:Declarations|Data [Aa]vailability|Supplementary [Mm]aterial|Funding)',r'\\begin\{center\}',r'\\end\{document\}']:
        e=re.search(pat,tail)
        if e:tail=tail[:e.start()]
    return tail,bool(re.search(r'\\(?:sub)*section\*?\{References\}',s))

def entries(p):
    blk,heading=block(p.read_text(errors='replace'))
    # blank-line segmentation, then splitter for glued author seams
    ee=[e.strip() for e in mergelib.split_entries(blk) if e.strip()]
    ee=[e for e in ee if len(e)>=20 and not e.startswith(('\\','%%'))]
    return ee,heading

def txt(s):
    s=re.sub(r'\\[a-zA-Z]+\b',' ',s)
    s=re.sub(r'[^a-zA-Z0-9]+',' ',s.lower())
    return ' '.join(s.split())
def tokens(s):return set(txt(s).split())

def score(a,b):
    x,y=tokens(a),tokens(b)
    if not x or not y:return 0
    return len(x&y)/len(x|y)

res=[]
for key,tgt in sorted(audit.HEAD.items()):
    h,head_heading=entries(tgt)
    for typ,s in [('seed',audit.SEED[key])]+[('predecessor',D/q) for q in audit.SRC[key]]:
        es,src_heading=entries(s)
        issue=[]
        for e in es:
            sims=[score(e,x) for x in h]
            i=max(range(len(h)),key=lambda i:sims[i]) if sims else None
            match=h[i] if i is not None else ''
            sim=sims[i] if i is not None else 0
            # Source words absent from best target (not necessarily lost; independent citation styles).
            source_only=sorted(tokens(e)-tokens(match))
            same=gate.same_work(e,match) if match else False
            if sim<0.68 or len(source_only)>=5:
                issue.append(dict(source=e,target=match,similarity=round(sim,3),same_work=same,
                                  source_only=source_only))
        r={'paper':key,'source_type':typ,'source':s.name,'head':tgt.name,'source_entries':len(es),'head_entries':len(h),
           'src_heading':src_heading,'head_heading':head_heading,'suspects':issue}
        res.append(r)
        print(f"{key:8} {typ:11} src={len(es):3} head={len(h):3} heading={head_heading} suspects={len(issue):3} low<{0.68}: {sum(x['similarity']<.68 for x in issue):3}")
path=pathlib.Path('/home/user/content_audit/ref_comparisons.json');path.write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
print('total suspect pairs',sum(len(x['suspects']) for x in res))
