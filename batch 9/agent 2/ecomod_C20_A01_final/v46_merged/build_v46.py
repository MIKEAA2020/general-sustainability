#!/usr/bin/env python3
"""Build ECOMOD v46: merge the best prose of v41/v42 with the verified C20 content.

No number, proposition, table, figure, citation or scope claim is changed.
What changes: title, abstract wording/precision/omitted result, and the Introduction prose.
"""
import json, re, shutil, pathlib

ROOT = pathlib.Path('/home/user')
SRC = ROOT / 'ecomod_deposit_doi_C20_A01'
OUT = ROOT / 'ecomod_v46_merged'
OUT.mkdir(exist_ok=True)

t = (SRC / 'ecomod_C20_A01_main.tex').read_text(encoding='utf-8')
v41_paras = json.loads((ROOT / 'series_audit' / 'v41_intro_paragraphs.json').read_text())

# ---------------------------------------------------------------- 1. TITLE
OLD_TITLE = r'\title{A rising biocapacity total can mask ecological-capital land drawdown: a two-land model}'
NEW_TITLE = (r'\title{Rising biocapacity, falling ecological capital: '
             r'how aggregation conceals composition}')
assert OLD_TITLE in t
t = t.replace(OLD_TITLE, NEW_TITLE)

# ------------------------------------------------------------- 2. ABSTRACT
old_ab_start = t.index(r'\begin{abstract}')
old_ab_end = t.index(r'\end{abstract}') + len(r'\end{abstract}')
NEW_ABSTRACT = r"""\begin{abstract}\setlength{\baselineskip}{14pt}
Biocapacity combines land area and productivity into a single annual account.
We ask what that total can and cannot reveal about the land beneath it, using a
conserved-area two-land model with delayed ecological regeneration, demographic
response and an imposed quality constraint. Conversion raises the model account
whenever the receiving land class contributes more per hectare, even as
ecological-capital land declines --- and the aggregate alone cannot identify that
this has happened: the same total is consistent with genuine growth and with
compositional loss. In a representative simulation, biocapacity rises $39\%$,
capital-land area falls by approximately $46\%$, and its modelled account
contribution falls by $51.72\%$. Sharp static bounds quantify how independent
land-area and quality observations restrict the compatible allocation set, and
integrated contribution budgets separate conversion, maintenance, retirement,
restoration, quality and fast-yield effects; in the 100-year fixed-demand
simulation conversion adds about $0.548$\,gha while the net account increase is
about $0.231$\,gha, with other contributions largely offsetting it. The reduced
fixed-demand equality relation reaches the minimum-area boundary without a fold or
critical slowing --- a result specific to that comparison. Separately, National
Footprint Accounts Edition 2026 values for 1961--2023 show world biocapacity
increasing $24.86\%$, biocapacity per person decreasing $52.71\%$ and production
footprint per person increasing $16.73\%$; cropland, forest and built-up accounts
contribute $+24.06$, $-5.95$ and $+7.44$ percentage points to that change. These
are annual account changes, not physical-stock observations. The results support
reporting constituent accounts alongside independently measured ecological assets,
because an aggregate that rises can conceal which of its parts is falling.
\end{abstract}"""
t = t[:old_ab_start] + NEW_ABSTRACT + t[old_ab_end:]

# ---------------------------------------------------------- 3. INTRODUCTION
intro_start = t.index(r'\section{Introduction}')
intro_end = t.index(r'\paragraph{Core contributions}')
old_frame = t[intro_start:intro_end]

# keep C20's literature paragraph (accurate, 24.86 % / 1961-2023) out of the block we replace:
lit_par = old_frame[old_frame.index('Most human--environment models'):old_frame.index('\\paragraph{Analogies}')]

# v41 paragraphs, converted to \citep
P0 = v41_paras[0].replace('(Cohen, 1995)', r'\citep{Cohen1995}')
P0 = re.sub(r'\s+', ' ', P0).strip()
P1 = re.sub(r'\s+', ' ', v41_paras[1]).strip()
P2 = re.sub(r'\s+', ' ', v41_paras[2]).strip()
P7 = re.sub(r'\s+', ' ', v41_paras[7]).strip()
P8 = re.sub(r'\s+', ' ', v41_paras[8]).strip()

# citation conversion for the paragraphs that carry them
P7 = P7.replace('(Abaee, 2026c)', r'\citep{Abaee2026c}')
P7 = P7.replace('the companion ledger work (Abaee, 2026c) calls',
                r'the companion ledger work \citep{Abaee2026c} calls')
P7 = P7.replace("the ledger study's own image (Abaee, 2026c)",
                r"the ledger study's own image \citep{Abaee2026c}")
P8 = P8.replace('of Abaee, 2026c', r'of \citet{Abaee2026c}')

NEW_INTRO = (
    r'\section{Introduction}\label{sec:intro}' + '\n\n'
    + P0 + '\n\n'
    + P1 + '\n\n'
    + P2 + '\n\n'
    + lit_par.strip() + '\n\n'
    + P7 + '\n\n'
    + P8 + '\n\n'
    + r"""\paragraph{Questions and evidence} Three questions follow from that framing.
\textbf{(Q1)} Under what conditions can conversion raise the total model account while
ecological-capital area $A_c$ falls, how long can the divergence last, and can the aggregate
identify the shift at all? \textbf{(Q2)} Under the model's stated assumptions, is the resulting
drawdown a catastrophic shift in the sense of the alternative-stable-states literature
\citep{Scheffer2001} --- a fold, hysteresis, early-warning signals --- or something structurally
different? \textbf{(Q3)} What limits drawdown under fixed demand, and what modelled process allows
capital-land area to recover?

Each answer is stated as a claim with a named observable and a stated rejection criterion, and
Section~\ref{sec:ident} separates what the total determines from what it cannot: the aggregate
fixes the sum of contributions, not their allocation between land classes, so the composition step
requires independent area and quality observations. The model parameters are representative rather
than fitted. Its simulations therefore illustrate conditional mechanisms rather than historical
forecasts, and the empirical decomposition below is an accounting analysis rather than a measurement
of physical stocks.

"""
)
t = t[:intro_start] + NEW_INTRO + t[intro_end:]

# --------------------------------------------- 4. keep the rest verbatim, fix one label
# C20 has \paragraph{Core contributions}; keep, but point the SI reference check
assert r'\paragraph{Core contributions}' in t

(OUT / 'ecomod_v46_main.tex').write_text(t, encoding='utf-8')

# ---------------------------------------------------------------- 5. copy assets
for d in ('figures', 'tables', 'inherited_C17'):
    s = SRC / d
    if s.exists():
        shutil.copytree(s, OUT / d, dirs_exist_ok=True)
for f in SRC.glob('*.tex'):
    if 'main' not in f.name:
        shutil.copy2(f, OUT / f.name)
print("built:", OUT / 'ecomod_v46_main.tex', len(t), "bytes")
