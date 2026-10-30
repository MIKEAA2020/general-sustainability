#!/usr/bin/env python3
"""Build SI first, generate exact cross-document numbers, then build main."""
import os,re,json,subprocess,sys,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CACHE=ROOT.parent/'.cache/F15';LATEX=CACHE/'latex'
def require(ok,msg):
 if not ok:raise ValueError(msg)
def expand(path):
 text=path.read_text()
 return re.sub(r'\\input\{([^}]+)\}',lambda m:expand(ROOT/(m[1]if m[1].endswith('.tex')else m[1]+'.tex')),text)
def compile_doc(kind):
 stem='integrated_F15_A01_'+kind
 with (CACHE/(kind+'_build.log')).open('w')as log:
  subprocess.run(['latexmk','-pdf','-interaction=nonstopmode','-halt-on-error','-outdir='+str(LATEX),stem+'.tex'],cwd=ROOT,env=dict(os.environ,SOURCE_DATE_EPOCH='1793318400'),stdout=log,stderr=subprocess.STDOUT,check=True)
 shutil.copyfile(LATEX/(stem+'.pdf'),ROOT/(stem+'.pdf'))
def run():
 LATEX.mkdir(parents=True,exist_ok=True)
 subprocess.run([sys.executable,str(ROOT/'src/assemble_F15.py')],check=True)
 compile_doc('SI')
 aux=(LATEX/'integrated_F15_A01_SI.aux').read_text()
 labels=dict(re.findall(r'\\newlabel\{((?:tab|fig):[^}]+)\}\{\{([^}]+)\}',aux))
 lines=['\\newcommand{\\SIref}[1]{\\csname SIlabel:#1\\endcsname}']
 for name,num in sorted(labels.items()):lines.append('\\expandafter\\def\\csname SIlabel:'+name+'\\endcsname{'+num+'}')
 (ROOT/'src/SI_reference_numbers_F15.tex').write_text('\n'.join(lines)+'\n')
 main=(ROOT/'integrated_F15_A01_main.tex').read_text();cited=set(re.findall(r'\\SIref\{([^}]+)\}',main));missing=set(labels)-cited;unknown=cited-set(labels)
 require(not missing,'Uncited SI items '+str(sorted(missing)));require(not unknown,'Unknown SI reference '+str(sorted(unknown)))
 (ROOT/'metadata/SI_linkage_F15.json').write_text(json.dumps(dict(labels=labels,main_citations=sorted(cited),uncited_SI_items=sorted(missing),unknown_main_references=sorted(unknown),every_SI_figure_and_table_cited_in_main=True),indent=2)+'\n')
 compile_doc('main')
 for kind in ['main','SI']:
  text=(LATEX/f'integrated_F15_A01_{kind}.log').read_text()
  bad=[s for s in text.splitlines()if 'Overfull'in s or 'undefined'in s.lower()or 'LaTeX Error'in s]
  require(not bad,'Typesetting diagnostics '+kind+': '+str(bad))
 print('Compiled both PDFs; every SI figure/table explicitly linked from main.')
if __name__=='__main__':run()
