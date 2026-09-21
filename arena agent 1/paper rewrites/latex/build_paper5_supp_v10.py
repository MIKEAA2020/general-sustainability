"""Build paper5 supplementary v10 from v9 (audit-sweep companion). Asserted-once."""
import sys

SRC = '/home/user/paper5_v31/paper5_supplementary_v9.md'
DST = '/home/user/paper5_v34/paper5_supplementary_v10.md'

s = open(SRC, encoding='utf-8').read()
n0 = len(s)

SUBS = [
 ('S1-endpoint',
  "bit-replicates `verify_bh_v30.log`. **Status: nominal tier (seed-fixed,",
  "bit-replicates `verify_bh_v30.log`. An endpoint-trim extension (drop-first-5, drop-last-5, drop-3+3 years; fixed 42-stock cohort; same seed-7/200-replicate/BH machinery) holds the zero count in all three trims (smallest nominal p 0.0050, one minimal-p cell under trim-first-5, still zero after adjustment; trimmed lengths 14--72 yr; `screen_extensions_v34.py`, `screen_extensions_v34.log`). The 42 normalized periodograms (1500 frequencies each) are deposited as `screen_periodograms_v34.csv` for band re-binning without re-execution. **Status: nominal tier (seed-fixed,"),
 ('S2a-spin',
  "(`rerun_campaigns/stage_scan_recovered/rerun_outputs_2026_09_01/tau0_out.txt`\n"
  "§A and `stage_decomp_results.md` §2, both @ 24c980cd), with the\n"
  "τ₀-stable classification by nonlinear ground truth. Two transcription notes.",
  "(`arena agent 1/other documents/rerun_campaigns/stage_scan_recovered/rerun_outputs_2026_09_01/tau0_out.txt`\n"
  "§A and `arena agent 1/other documents/rerun_campaigns/stage_scan_recovered/stage_decomp_results.md` §2, both @ 24c980cd), with the\n"
  "τ₀-stable classification by nonlinear ground truth. Generating scripts, same commit: `stage_r_window.py`, `stage_tau0_decomposition.py`, `stage_decomp2.py` (all under `arena agent 1/other documents/rerun_campaigns/stage_scan_recovered/` @ 24c980cd). Two transcription notes."),
 ('S2b-rwin',
  "the table below uses the τ₀-scan's, and the rwin scan is\n"
  "cited for the g=0 validation and the extended g∈{15,50} cells by pointer.",
  "the table below uses the τ₀-scan's; the g=0 validation pair and the rwin-only g∈{15,50} cells are in `arena agent 1/other documents/rerun_campaigns/stage_scan_recovered/rerun_outputs_2026_09_01/rwin_out.txt` @ 24c980cd, not transcribed here."),
 ('S3-s8-power',
  "the power-simulation code and seeds; and the sensitivity-battery code and log. On the open docket:",
  "the power-simulation code and seeds (grid: sprat (r,g,Tr)=(0.8,2,7), anchovy (1.6,1,3), cod false-positive (0.3,5,5); H∈{100,200} yr design with supplementary H400 cells; detection bands 30--120 yr sprat / 8--20 yr anchovy+cod; Lomb-Scargle nf=800; nominal per-cell 95% AR(1)-null threshold, 120 null replicates, seed 7; 50 trials per cell, seeds 0--49); the sensitivity-battery code and log; and the endpoint-trim check with the 42-stock periodogram deposit (`screen_extensions_v34.py`, `screen_extensions_v34.log`, `screen_periodograms_v34.csv`). On the open docket:"),
]

fails = []
for tag, old, new in SUBS:
    c = s.count(old)
    if c != 1:
        fails.append((tag, c))
        continue
    s = s.replace(old, new, 1)

if fails:
    print('FAILED:', fails)
    sys.exit(1)
open(DST, 'w', encoding='utf-8').write(s)
print(f'supp v10 built: {len(SUBS)}/{len(SUBS)} subs ok, {n0} -> {len(s)} bytes')
