"""Build paper5 supplementary v13 from v12. Guarded edits."""
import re

SRC = '/home/user/paper5_v36/paper5_supplementary_v12.md'
DST = '/home/user/paper5_v37/paper5_supplementary_v13.md'
s = open(SRC, encoding='utf-8').read()
n0 = len(s)

def rep(old, new, tag):
    global s
    c = s.count(old)
    assert c == 1, f'{tag}: count={c}\n---\n{old[:200]}'
    s = s.replace(old, new, 1)
    print(f'{tag}: OK')

def repw(old_joined, new, tag):
    """Whitespace-flexible: old given space-joined, matched across line wraps."""
    global s
    pat = re.compile(re.escape(old_joined).replace(r'\ ', r'\s+'))
    ms = pat.findall(s)
    assert len(ms) == 1, f'{tag}: count={len(ms)}\n---\n{old_joined[:200]}'
    s = pat.sub(lambda _: new, s, count=1)
    print(f'{tag}: OK (flex)')

print('--- S1 row headers ---')
for m in re.finditer(r'^- \*\*Main text §([0-9.]+):', s, re.M):
    print('  row:', m.group(1))

# S1. intro nine -> ten
repw('It carries nine bodies of material:',
    'It carries ten bodies of material:', 'S1a-ten')
repw('and the screen-sensitivity battery and stage-scan decomposition records (S9).',
    'the screen-sensitivity battery and stage-scan decomposition records (S9); and the T_r-ranked test record (S10).',
    'S1b-s10')

# S2. S1 2.7 row: theorem -> remark
repw('the phase-line obstruction (theorem; elementary proof displayed in full)',
    'the phase-line obstruction (elementary remark; proof displayed in full)', 'S2-remark')

# S3. S1 inventory clauses
lines = s.split('\n')
fired38 = fired37 = fired45 = False
for k, ln in enumerate(lines):
    if ln.startswith('- **Main text §2.7 and §3.8:**'):
        lines[k] = ln + ' The seal-predation threshold-shift reading is a directional application of Lemma 2.2(ii), explicitly non-quantitative.'
        fired38 = True
    elif ln.startswith('- **Main text §3.7:**'):
        lines[k] = ln + ' Case-screening table and query log deposited.'
        fired37 = True
    elif ln.startswith('- **Main text §4.5:**'):
        lines[k] = ln + ' The T_r-ranked cross-sectional test is executed (S10).'
        fired45 = True
assert fired38 and fired37 and fired45, f'S3: {fired38} {fired37} {fired45}'
s = '\n'.join(lines)
print('S3-rows: 2.7/3.8 + 3.7 + 4.5 OK')

# S4. S2.1 demotion
repw('**Proposition S2.1** (Forward invariance; phase-line obstruction). *Both propositions are stated and proved in full in the main text (§3.1 and §2.7); their proofs are not repeated here.*',
    '**Proposition S2.1** (Forward invariance; Remark on the phase-line obstruction). *The proposition (§3.1) and the remark (§2.7) are stated and proved in full in the main text; their proofs are not repeated here.*',
    'S4a-s21')
repw('The proposition records the consequence needed for the cod case:',
    'The remark records the consequence needed for the cod case:', 'S4b-records')

# S5a. S4 cod audit clause
repw('in the archived record).',
    'in the archived record). A 2026-09-11 re-derivation from the ICES standardgraphs SSB series (current vintage) gives 0.394 for the same window, confirming the value within assessment-revision noise (audit code, log, and series deposited).',
    'S5a-cod-audit')

# S5b. S4 haddock 0.143 -> 0.24
repw('- **Icelandic haddock** (related rule): post-implementation coefficient of variation 0.143, lower despite higher recruitment variability.',
    '- **Icelandic haddock** (related rule): post-2013 (own-HCR) SSB coefficient of variation 0.24, lower despite higher recruitment variability (recruitment CV 0.68 vs cod 0.15 on the 2013–2023 window; ICES standardgraphs series, current vintage). The post-1995 SSB value 0.36 is retained as a documented window comparison.',
    'S5b-haddock')

# S6. S4 closing flip
repw('The case-screening table and query log are a **registration requirement** not yet discharged.',
    'The case-screening table (`u5_case_table.csv`) and query log (`u5_query_log.md`) are deposited with the article.',
    'S6-s4-flip')

# S7a. S8 undischarged flip
repw('The registration requirements not yet discharged are: the legacy stage registration\'s initial histories and solver configuration; and the case-screening table and query log.',
    'The registration requirements not yet discharged are the legacy stage registration\'s initial histories and solver configuration.',
    'S7a-undischarged')

# S7b. S8 discharged list append
repw('and the endpoint-trim check with the 42-stock periodogram deposit (`screen_extensions_v34.py`, `screen_extensions_v34.log`, `screen_periodograms_v34.csv`). On the open docket:',
    'and the endpoint-trim check with the 42-stock periodogram deposit (`screen_extensions_v34.py`, `screen_extensions_v34.log`, `screen_periodograms_v34.csv`); the case-screening table and query log (`u5_case_table.csv`, `u5_query_log.md`); the T_r-ranked test (`tr_ranked_test.py`, `tr_table.csv`, `tr_test.log`); the Icelandic-cod audit (`cod_audit.py`, `cod_audit.log`, `ices_cod_27_5a.csv`, `ices_had_27_5a.csv`); and the η-basis window runs (`eta_basis.py`, `eta_basis.log`). On the open docket:',
    'S7b-discharged')

# S8. S9.2 append eta-basis runs
repw('whose detail they supply.**',
    '''whose detail they supply.**

#### η-basis window runs (§3.3 baseline)

The baseline effort-response coefficient η = 0.914 is an inherited
illustrative baseline (Candidate-A value from the companion delay study,
whose institutional coefficients are explicitly uncalibrated), not a
derived threshold. Two window runs on the gated three-state core
(`eta_basis.py`, deposited with log) place it:

| η | r-window (yr⁻¹) |
|---|---|
| 0.3 | empty |
| 0.5 | empty |
| 0.7 | (0.0096, 0.0144) |
| 0.914 | (0.0083, 0.0215) |
| 1.5 | (0.0071, 0.0375) |
| 3.0 | (0.0068, 0.0589) |

The window opens between η = 0.5 and 0.7, and the upper window edge
crosses the baseline r = 0.02 between η = 0.83 (0.0192) and η = 0.86
(0.0201), so η = 0.914 is neither the window-opening threshold nor the
inclusion threshold. All window claims in the main text are bracketed at
η = 0.914 and η = 3.0.

**Status: executed basis runs; nominal tier.**''',
    'S8-eta-s92')

# S9. S10 new section at tail
assert s.rstrip().endswith('**Status: executed basis runs; nominal tier.**')
s = s.rstrip() + '''

---

## S10. T_r-ranked cross-sectional test (§4.5)

The test asks whether spectral-band power rises toward the sampled
windows as the review interval lengthens, across the 42-stock cohort of
§2.4. Review intervals come from the cohort's regime column and compiler
metadata (sub-annual = 0.5 yr, n = 7; annual = 1.0 yr, n = 35). Bands
are the prespecified §2.4 bands (A = sub-annual structure, B =
multi-annual structure); flags are Benjamini–Hochberg 5% AR(1)-null
exceedances, the same flag metric as the screen. Three contrasts are
prespecified: (1) Spearman rank correlation of interval rank against
null-excess band power; (2) a Mann–Whitney comparison of sub-annual
against annual stocks; (3) per-class flag counts against the null
expectation (anchovy n = 18, sprat n = 4, herring n = 20).

No window-approach gradient can be identified: every documented review
interval (0.5, 1.0 yr) lies below every sampled window of §3.3, because
no responsive multi-year system survives the case screen (the
structural cause recorded in §2.6/S4). T_r ≈ 1 dormancy holds on the
flag metric: 0/42 flags in band A, 1/42 in band B, null-consistent in
every class (single B flag: a 19-year Pacific chub mackerel series).
The sub-annual cohort carries higher raw and null-excess band power
than the annual cohort (band-A medians 0.193 vs 0.069 raw, 0.529 vs
0.257 excess; Mann–Whitney p = 0.000 raw, p = 0.007 excess), but the
elevation runs opposite to any window-approach gradient — the
sub-annual stocks sit farther below the windows — so it cannot be
institutional under the model. It is the ENSO quasi-periodic confound:
the §3.7 anchoveta 3.7-yr peak lives in band A, and AR(1) nulls absorb
red noise, not quasi-periodic forcing, producing within-null elevation
without flags.

Code, per-stock table, and log deposited (`tr_ranked_test.py`,
`tr_table.csv`, `tr_test.log`).

**Status: executed analysis; controlled null for the mechanism.**'''
print('S9-s10: appended')

# S10. S1 blanket S2-S9 -> S2-S10
repw('- **S2–S9:** each item carries its status on the line.',
    '- **S2–S10:** each item carries its status on the line.', 'S10-blanket')

print('--- post-checks ---')
print('0.143 remaining:', s.count('0.143'))
print('len delta:', len(s) - n0)
assert s.count('0.143') == 0

open(DST, 'w', encoding='utf-8').write(s)
print('WROTE', DST)
