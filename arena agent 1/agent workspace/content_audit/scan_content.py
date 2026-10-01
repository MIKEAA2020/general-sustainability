#!/usr/bin/env python3
"""Reproducible loss-candidate generator: seeds, local predecessors, merge inputs.

NOT a semantic verdict. Preservation means normalized 8-grams and labeled objects;
near-verbatim excerpts and explicit human reading are required for every candidate.
Only comments are dropped; uses first real References heading as body boundary.
"""
import json,re,pathlib,collections,hashlib
D=pathlib.Path('/home/user/papers'); A=pathlib.Path('/home/user/content_audit')
M=json.loads((A/'seed_manifest.json').read_text())
heads={}
for p in D.glob('paper*.tex'):
    m=re.match(r'(paper\d+[a-z]*)_.*_v(\d+)\.tex$',p.name)
    if m and (m.group(1) not in heads or int(m.group(2))>heads[m.group(1)][0]):heads[m.group(1)]=(int(m.group(2)),p)
HEAD={k:p for k,(v,p) in heads.items()}
SEED={'paper'+k:pathlib.Path(M[k]['local']) for k in ('01','02','03','04','05','06','07','08','09','09b','10','10b','11','11b','11c')}
SRC={
 'paper01':['paper01_obstruction_calculus_v61.tex'],
 'paper02':['paper02_probabilistic_sufficiency_v11.tex'],
 'paper03':['paper03_computational_certification_v14.tex'],
 'paper04':['paper04_minimax_dual_certificates_v15.tex'],
 'paper05':['paper05_exact_belief_computation_v14.tex'],
 'paper06':['paper06_assessment_separation_v65.tex'],
 'paper07':['paper07_sampled_governance_v49.tex'],
 'paper08':['paper08_governance_delay_v45.tex','paper07_sampled_governance_v50.tex'],
 'paper09':['paper09_cod_certification_v31.tex','paper09b_arv_certification_v2.tex','paper10b_edwards_aquifer_v1.tex'],
 'paper09b':['paper09b_arv_certification_v1.tex'],
 'paper10':['paper10_depletion_ledgers_v52.tex'],
 'paper10b':[],
 'paper11':['paper11_forecasting_baselines_v63.tex','paper11b_edwards_forecast_v2.tex'],
 'paper11b':['paper11b_edwards_forecast_v1.tex'],
 'paper11c':['paper11c_worked_systems_audit_v1.tex'],
}
SUPP={
 'paper01s':(D/'paper01_obstruction_calculus_v63_supplementary.tex',['01s']),
 'paper06s':(D/'paper06_assessment_separation_v67_supplementary.md',['06s']),
 'paper08sd':(D/'paper08_governance_delay_v46_supplementary_delay.md',['08sd']),
 'paper08sg':(D/'paper08_governance_delay_v46_supplementary_governance.md',['08sg19','08sg20']),
 'paper10s':(D/'paper10_depletion_ledgers_v53_supplementary.tex',['10st']),
}
PFX={'paper01':['calc-'],'paper03':['lp-'],'paper05':['scale-'],'paper06':['sep-'],'paper08':['dde-','sh-'],'paper09':['budget-','regime-','edw-'],'paper11':['cod-','edw-']}
# Most of these sources themselves already have prefixes, so use suffix matching.
def clean(raw):
    lines=[]
    for line in raw.splitlines():
        # % starts a comment only if preceded by an even number of backslashes.
        pos=0
        while True:
            i=line.find('%',pos)
            if i<0:break
            b=0;j=i-1
            while j>=0 and line[j]=='\\':b+=1;j-=1
            if b%2==0:line=line[:i];break
            pos=i+1
        lines.append(line)
    return '\n'.join(lines)

def scope(raw,ext):
    s=clean(raw)
    if ext=='.tex':
        m=re.search(r'\\begin\{document\}',s)
        if m:s=s[m.end():]
        m=re.search(r'\\(?:sub)*section\*?\{References\}',s,re.I)
        if m:s=s[:m.start()]
        s=re.sub(r'\\(?:label|ref|eqref|pageref|autoref|cref|Cref|cite\w*)\{[^}]*\}',' CROSSREF ',s)
        s=re.sub(r'\\(?:title|author|date)\s*\{[^}]*\}',' ',s)
    return s

def words(s):
    # no labels/citation keys; otherwise retain math, prose, and captions
    return [(m.group().lower(),m.start()) for m in re.finditer(r"[A-Za-zÀ-ÿ]+(?:[-'][A-Za-z]+)?|\d+(?:\.\d+)?",s)]

def objects(s):
    s=clean(s)
    heads=[(m.group(1),re.sub(r'\s+',' ',m.group(2)).strip()) for m in re.finditer(r'\\(part|section|subsection|subsubsection)\*?\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}',s)]
    labels=re.findall(r'\\label\{([^}]+)\}',s)
    figs=re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}',s)
    counts={e:len(re.findall(r'\\begin\{'+e+r'\}',s)) for e in ('figure','table','longtable','theorem','lemma','proposition','corollary','definition','proof')}
    return heads,labels,figs,counts

def comparison(src,tgt,key,kind):
    raw_s=src.read_text(errors='replace');raw_t=tgt.read_text(errors='replace')
    ss=scope(raw_s,src.suffix);ts=scope(raw_t,tgt.suffix)
    sw=words(ss);tw=words(ts);a=[w for w,p in sw];b=[w for w,p in tw]
    n=8
    grams={tuple(b[i:i+n]) for i in range(max(0,len(b)-n+1))}
    ok=[tuple(a[i:i+n]) in grams for i in range(max(0,len(a)-n+1))]
    hits=sum(ok);count=len(ok)
    runs=[];i=0
    while i<count:
        if ok[i]:i+=1;continue
        j=i+1
        while j<count and not ok[j]:j+=1
        if j-i>=20:
            start=sw[i][1];end=sw[min(j+n-2,len(sw)-1)][1]
            chunk=ss[start:min(end+30,len(ss))]
            line=ss.count('\n',0,start)+1
            runs.append({'line':line,'words':j-i+7,'excerpt':re.sub(r'\s+',' ',chunk[:430]).strip()})
        i=j
    # heading and label preservation; qualitative: suffix match, not proof of same content.
    sh,sl,sf,sc=objects(raw_s);th,tl,tf,tc=objects(raw_t)
    missing_labels=[x for x in sl if not any(y==x or y.endswith('-'+x) for y in tl)]
    missing_figs=[x for x in sf if x not in tf]
    # heading title exactness varies with formatting / intentional renames.
    thn={re.sub(r'\\\w+|[^a-z0-9]+','',h.lower()) for typ,h in th}
    missing_heads=[(typ,h) for typ,h in sh if re.sub(r'\\\w+|[^a-z0-9]+','',h.lower()) not in thn]
    return dict(key=key,kind=kind,src=str(src),head=str(tgt),src_words=len(a),head_words=len(b),coverage=hits/count if count else 1,missing_gram_count=count-hits,source_grams=count,
        missing_runs=runs,missing_labels=missing_labels,missing_figs=missing_figs,
        missing_headings=missing_heads,src_counts=sc,head_counts=tc,
        sha256_src=hashlib.sha256(src.read_bytes()).hexdigest(),sha256_head=hashlib.sha256(tgt.read_bytes()).hexdigest())

def run():
    comparisons=[]
    for key,tgt in sorted(HEAD.items()):
        sources=[('seed',SEED[key])]+[('predecessor',D/s) for s in SRC[key]]
        for typ,s in sources:
            assert s.exists(),s
            x=comparison(s,tgt,key,typ);comparisons.append(x)
            print(f"{key:9} {typ:11} {s.name[:33]:34} coverage={x['coverage']:.2%} runs={len(x['missing_runs']):3} labels={len(x['missing_labels']):3} figures={len(x['missing_figs']):2} headings={len(x['missing_headings']):3}")
    for key,(tgt,sources) in SUPP.items():
        for sid in sources:
            src=pathlib.Path(M[sid]['local']);x=comparison(src,tgt,key,'supplement-seed');comparisons.append(x)
            print(f"{key:9} {'supplement':11} {src.name[:33]:34} coverage={x['coverage']:.2%} runs={len(x['missing_runs']):3} labels={len(x['missing_labels']):3} figures={len(x['missing_figs']):2} headings={len(x['missing_headings']):3}")
    (A/'comparisons.json').write_text(json.dumps(comparisons,indent=2,ensure_ascii=False)+'\n')
    print('comparisons',len(comparisons),'candidate runs',sum(len(x['missing_runs']) for x in comparisons))
if __name__=='__main__':run()
