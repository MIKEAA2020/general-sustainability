#!/usr/bin/env python3
"""Compile both parts of the one integrated publication; build logs stay in cache."""
import os,shutil,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def run():
 cache=ROOT.parent/'.cache/F13';cache.mkdir(parents=True,exist_ok=True);tex=cache/'latex';tex.mkdir(exist_ok=True)
 subprocess.run([sys.executable,str(ROOT/'src/assemble_manuscripts_F13.py')],check=True)
 for kind in ['main','SI']:
  stem='integrated_F13_A01_'+kind
  with (cache/(kind+'_build.log')).open('w')as log:
   subprocess.run(['latexmk','-pdf','-interaction=nonstopmode','-halt-on-error','-outdir='+str(tex),stem+'.tex'],cwd=ROOT,env=dict(os.environ,SOURCE_DATE_EPOCH='1793318400'),check=True,stdout=log,stderr=subprocess.STDOUT)
  shutil.copyfile(tex/(stem+'.pdf'),ROOT/(stem+'.pdf'))
 print('Integrated main and SI compiled. Auxiliary files and logs are excluded cache only.')
if __name__=='__main__':run()
