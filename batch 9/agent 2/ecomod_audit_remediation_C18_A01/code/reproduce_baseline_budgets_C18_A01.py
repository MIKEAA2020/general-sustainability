"""Rerun preserved C17 budget checks without editing inherited_C17.
Runs the full 28-trajectory check and reference refinement in a disposable copy.
Copies only versioned evidence into the C18 evidence directory.
"""
from pathlib import Path
import tempfile,shutil,subprocess,sys,json
R=Path(__file__).resolve().parents[1]
def main():
    cache=R/'.cache';cache.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='budget_',dir=cache)as temp:
        work=Path(temp);shutil.copytree(R/'inherited_C17',work,dirs_exist_ok=True)
        log=[]
        for command in [['code/verify_budgets.py','--full'],['code/verify_reference_refinement.py']]:
            p=subprocess.run([sys.executable]+command,cwd=work,capture_output=True,text=True)
            log.append(p.stdout+p.stderr)
            if p.returncode:raise RuntimeError('Budget verifier failed; '+log[-1][-2000:])
        for source,target in [('data/model_independent_checks.json','budget_rerun_C18_A01.json'),('metadata/reference_refinement.json','reference_refinement_rerun_C18_A01.json')]:
            shutil.copyfile(work/source,R/'evidence'/target)
        (R/'evidence/budget_rerun_C18_A01.txt').write_text('\n'.join(log))
        print(json.dumps(json.loads((R/'evidence/budget_rerun_C18_A01.json').read_text()),indent=2))
if __name__=='__main__':main()
