"""F10 preservation, PDF QA and artifact manifest. Technical QA, not validation.
Default verifies current artifact identity. --write requires local protected F08/F09,
finished builds/test logs and records only checks actually performed.
"""
from pathlib import Path
import argparse,csv,hashlib,json,re
from pypdf import PdfReader
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
EXCLUDED={'.cache','__pycache__'}
MANIFEST='artifact_manifest_F10.json'
def require(v,m):
    if not v:raise ValueError(m)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def files():return sorted(p for p in ROOT.rglob('*')if p.is_file()and not any(x in EXCLUDED for x in p.relative_to(ROOT).parts)and p.name!=MANIFEST)
def verify_manifest():
    m=json.loads((ROOT/MANIFEST).read_text());require({str(p.relative_to(ROOT))for p in files()}=={r['path']for r in m['files']},'Manifest coverage')
    for r in m['files']:
        p=ROOT/r['path'];require(p.stat().st_size==r['bytes']and digest(p)==r['sha256'],'Artifact changed: '+r['path'])
    return len(m['files'])
def record():
    protected={}
    for folder,manifest in [('ecomod_followup_F08','artifact_manifest.json'),('ecomod_followup_F09','artifact_manifest_F09.json')]:
        base=ROOT.parent/folder;m=json.loads((base/manifest).read_text())
        for r in m['files']:require(digest(base/r['path'])==r['sha256'],'Protected package changed')
        protected[folder]={'files_verified':len(m['files'])+1,'manifest_sha256':digest(base/manifest)}
    inherited=json.loads((ROOT/'metadata/inherited_unchanged_files_F10.json').read_text())
    for p,h in inherited.items():require(digest(ROOT/p)==h,'Inherited file changed: '+p)
    original=ROOT.parent/'ecomod_followup_F09/data';data=[p for p in original.rglob('*')if p.is_file()]
    for p in data:require(p.read_bytes()==(ROOT/'data'/p.relative_to(original)).read_bytes(),'Original data changed')
    with (ROOT/'data/support/physical_admission_F08.csv').open()as f:rows=list(csv.DictReader(f))
    require(len(rows)==8 and all(r['admission']=='hold_not_admitted'for r in rows),'Admission changed')
    tests={}
    for name in ['tests_F10_all.txt','tests_F10_optimized.txt']:
        t=(ROOT/'metadata'/name).read_text();count=int(re.search(r'Ran (\d+) tests',t).group(1));require(count==134 and t.rstrip().endswith('OK'),'Test failure')
        tests[name]={'passed':count,'sha256':digest(ROOT/'metadata'/name)}
    design=json.loads((ROOT/'configs/study_design.json').read_text());pdfs={}
    for part in ['main','SI']:
        name=f'followup_F10_{part}';p=ROOT/(name+'.pdf');r=PdfReader(p);require(len(r.pages)==12,'Unexpected pagination')
        require(r.metadata['/Keywords']=='; '.join(design['keywords']),'Keyword metadata')
        urls=[]
        for page in r.pages:
            for a in page.get('/Annots',[]):
                action=a.get_object().get('/A')
                if action and action.get('/URI'):urls.append(str(action['/URI']))
        require('https://orcid.org/0000-0002-0019-1842'in urls,'ORCID link')
        require(any('/ecomod_empirical_followup/F10'in u for u in urls),'Current package link')
        log=(ROOT/'.cache/tex'/(name+'.log')).read_text();warnings=[x for x in log.splitlines()if any(w in x for w in ['Warning','Overfull','Underfull','undefined'])];require(not warnings,'LaTeX warning')
        doc=pymupdf.open(p);outside=[]
        for n,page in enumerate(doc,1):
            require('??'not in page.get_text(),'Unresolved reference')
            for b in page.get_text('dict')['blocks']:
                for line in b.get('lines',[]):
                    for span in line['spans']:
                        a=pymupdf.Rect(span['bbox'])
                        if a.x0< -1 or a.y0< -1 or a.x1>page.rect.width+1 or a.y1>page.rect.height+1:outside.append(n)
        require(not outside,'Text outside page')
        pdfs[part]={'pages':len(r.pages),'sha256':digest(p),'orcid_hyperlink_verified':True,'seven_keywords_verified':True,'current_package_link_verified':True,'latex_warnings':warnings,'text_outside_page':outside}
    main=(ROOT/'followup_F10_main.tex').read_text();old=(ROOT.parent/'ecomod_followup_F09/followup_F09_main.tex').read_text()
    declaration=r'\href{http://Arena.ai}{Arena.ai} Agent Mode was used to assist with computational methods and literature review.'
    require(declaration in main and declaration in old,'Approved declaration differs')
    abstract=lambda s:s.split(r'\begin{abstract}',1)[1].split(r'\end{abstract}',1)[0]
    require(abstract(main)==abstract(old),'Abstract changed')
    r03=ROOT.parent/'ecomod_followup_feasibility_R03'
    for name in ['native_sd_summary_R03.csv','local_reference_candidate_R03.csv']:require((ROOT/'data/reference'/name).read_bytes()==(r03/'data'/name).read_bytes(),'R03 result copy differs')
    result={'revision':'F10','date':'2026-10-29','protected':protected,'inherited_F09_byte_identical_files':len(inherited),'original_F09_data_files_unchanged':len(data),'tests':tests,'pdfs':pdfs,'manual_visual_inspection_pdf_pages':{'main':[8,9],'SI':[6,10]},'abstract_unchanged':True,'approved_AI_declaration_unchanged':True,'admissions_hold':8,'calibrated_change_uncertainty_added':False,'new_eligible_paired_reference':False,'technical_QA_is_ecological_validation':False}
    (ROOT/'metadata/verification_F10.json').write_text(json.dumps(result,indent=2)+'\n')
    manifest={'revision':'F10','self_excluded':True,'excluded_directories':sorted(EXCLUDED),'files':[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':digest(p)}for p in files()]}
    (ROOT/MANIFEST).write_text(json.dumps(manifest,indent=2)+'\n')
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--write',action='store_true');a=p.parse_args()
    if a.write:record()
    print(json.dumps({'verified_manifest_files':verify_manifest(),'technical_QA_not_ecological_validation':True}))
