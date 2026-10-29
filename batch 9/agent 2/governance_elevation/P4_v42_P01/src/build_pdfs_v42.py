"""Build the two versioned PDFs; TeX intermediates remain in an excluded cache."""
from pathlib import Path
import subprocess,os,shutil
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1];M=ROOT/'manuscript';CACHE=ROOT/'.cache/latex';CACHE.mkdir(parents=True,exist_ok=True)
env=os.environ.copy();env['SOURCE_DATE_EPOCH']=str(int(datetime(2026,10,29,tzinfo=timezone.utc).timestamp()));env['FORCE_SOURCE_DATE']='1'
subprocess.run(['pandoc','paper4_supplementary_v9.md','--standalone','-V','geometry:margin=25mm','-V','fontsize=10pt','-V','papersize:a4','--resource-path=.','--include-in-header=pdf_metadata_SIv9.tex', '-o','paper4_supplementary_v9.tex'],cwd=M,env=env,check=True)
for name in ['paper4_delay_dynamics_v42','paper4_supplementary_v9']:
    for k in range(2):
        p=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(CACHE),name+'.tex'],cwd=M,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        (CACHE/f'{name}_pass{k+1}.txt').write_text(p.stdout)
        if p.returncode:raise RuntimeError('PDF build failed; see '+str(CACHE/f'{name}_pass{k+1}.txt'))
    shutil.copy(CACHE/(name+'.pdf'),M/(name+'.pdf'));print('Built',name+'.pdf')
