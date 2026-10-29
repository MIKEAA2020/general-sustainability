"""Legible account availability plot, generated solely from the frozen audit CSV."""
from pathlib import Path
from collections import Counter
import csv,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]

def availability_counts(rows):
    counts=Counter()
    for row in rows:
        value=str(row['account_available']).lower()
        if value not in {'true','false','1','0'}:raise ValueError('Unknown availability flag')
        counts[row['UN_region'],'pass' if value in {'true','1'}else 'fail']+=1
    return counts

def draw(rows,outdir):
    counts=availability_counts(rows);regions=sorted({r for r,_ in counts});y=np.arange(len(regions));passed=[counts[r,'pass']for r in regions];failed=[counts[r,'fail']for r in regions]
    outdir=Path(outdir);outdir.mkdir(exist_ok=True,parents=True)
    with plt.rc_context({'font.size':11}):
        fig,ax=plt.subplots(figsize=(8.2,4.6),layout='constrained')
        ax.barh(y,passed,label='Available account data',color='#377d87',height=.62)
        ax.barh(y,failed,left=passed,label='Unavailable account data',color='#d6a64c',height=.62)
        labels=[r.replace('Latin America and the Caribbean','Latin America and\nthe Caribbean')for r in regions]
        ax.set_yticks(y,labels);ax.invert_yaxis();ax.set_xlabel('Country/territory identifiers');ax.set_title('2015–2023 national account availability',pad=10);ax.set_xlim(0,max(p+f for p,f in zip(passed,failed))+14);ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True));ax.legend(loc='lower right',fontsize=9,frameon=False)
        ax.spines[['top','right']].set_visible(False);ax.grid(axis='x',alpha=.18);ax.set_axisbelow(True)
        fig.supxlabel('Source: Lo et al., NEFBA 2026 v1.0; derived availability counts — CC BY-SA 4.0',fontsize=8)
        fig.canvas.draw();renderer=fig.canvas.get_renderer();boxes=[t.get_window_extent(renderer)for t in ax.get_yticklabels()]
        if any(a.overlaps(b)for i,a in enumerate(boxes)for b in boxes[i+1:]):raise ValueError('Region labels overlap')
        fig.savefig(outdir/'account_coverage_F06.pdf');fig.savefig(outdir/'account_coverage_F06.png',dpi=180)
        qa={'region_label_boxes_disjoint':True,'orientation':'horizontal stacked bars','underlying_counts_changed':False,'regions':[{'region':r,'available':p,'unavailable':f}for r,p,f in zip(regions,passed,failed)],'totals':{'available':sum(passed),'unavailable':sum(failed)}}
        (outdir/'account_coverage_F06_checks.json').write_text(json.dumps(qa,indent=2)+'\n');plt.close(fig)
    return qa

if __name__=='__main__':
    with (ROOT/'data/derived/account_availability.csv').open()as f:print(json.dumps(draw(list(csv.DictReader(f)),ROOT/'results'),indent=2))
