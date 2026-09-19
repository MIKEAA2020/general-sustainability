#!/usr/bin/env python3
"""v38 kernel: (1) the missing Funding declaration; (2) the Section 1.5 paragraph made causally
self-contained (its cross-reference from Remark 36 restored, its non-inferential direction stated);
(3) a corrected extremum statement in the fibre proposition -- the shipped proof claimed extrema of a
continuous function over a polytope sit at vertices, which its own instance contradicts; (4) the
quotient-versus-identification-rows ambiguity in Definition 34 resolved by giving both constructions;
(5) the three-way verdict and the scope of Definition 40's compensation programme; (6) the
certificate-relativity of the interface price and the multiplier-set reading of a capacity price;
(7) the fisheries extract's vintage, now pinned from the repository and the deposit record instead of
pointing at an analysis repository the reader cannot open.

Applied to md and tex together; every edit is logged so v38 -> v37 reverses exactly.
"""
import re, sys, json

HERE = '/home/user/revision/v7'
sys.path.insert(0, HERE)
from build_v35_kernel import m2t, pattern, SQ            # noqa: E402

MD_IN, TEX_IN = f'{HERE}/paper3_material_ledgers_v37.md', f'{HERE}/paper3_material_ledgers_v37.tex'
MD_OUT, TEX_OUT = f'{HERE}/paper3_material_ledgers_v38.md', f'{HERE}/paper3_material_ledgers_v38.tex'
LOG = f'{HERE}/revisions_v38_kernel_log.json'

E = []


def sub(name, old, new, old_tx=None, new_tx=None):
    E.append((name, old, new, old_tx, new_tx))


# ---- 1. Funding, in the house form used by the companion articles
sub('funding-declaration',
    r"""## Declaration of competing interest

None.""",
    r"""## Funding

None declared.

## Declaration of competing interest

None.""",
    old_tx=r"""\subsection*{Declaration of competing interest}

None.""",
    new_tx=r"""\subsection*{Funding}

None declared.

\subsection*{Declaration of competing interest}

None.""")

# ---- 2. Section 1.5: make the analogy's direction explicit and restore what Remark 36 refers back to
sub('sec15-causal-coherence',
    r"""rate to a horizon is taken nowhere in them, and it is not taken here either. None of these sources is used as a premise here.""",
    r"""rate to a horizon is taken nowhere in them, and it is not taken here either. The direction of the
comparison is one-way and is meant to be read that way: the accounts supply an instance of the phenomenon this
article analyses, not a premise for it, and nothing in Sections 2 to 10 depends on any claim made about the
standards here --- not the arithmetic, not the certificates, and not the interpretation boundaries. Their
revision is also silent on the boundary of an asset in physical terms: for the renewable-resource categories
the 2025 revision admits, what counts as an asset is drawn by viability under prevailing technology and
prices, which is an eligibility statement of exactly the kind Remark 36 treats as reclassification rather than
as a property of the stock. None of these sources is used as a premise here.""")

# ---- 3. the fibre proposition: replace the false vertex claim with the polyhedral case and its scope
sub('fibre-polytope-fix',
    r"""More generally, where the declared constraints are linear the fibre is a polytope, and a continuous
event time has an interval image on a connected fibre: $\mathrm T(z)$ is that interval, and its endpoints
are the values of two linear programmes over the polytope.""",
    r"""More generally, where the declared constraints are linear the fibre is a polytope, and a continuous
event time has an interval image on a connected fibre: $\mathrm T(z)$ is that interval, and its endpoints
are its maximum and minimum over the polytope. Those two values are programmes rather than aspirations
exactly where the event time is declared in polyhedral form, $\tau(x) = g(\min_{j \le k}(a_j^{\top} x + b_j))$
with $g$ continuous and increasing: the upper endpoint is the single linear programme over $(x, r)$ with
$r \le a_j^{\top} x + b_j$ for every $j$, and the lower endpoint is the minimum over the polytope's vertices,
finite to enumerate, because a minimum of affine functions is concave and a concave function attains its
minimum at an extreme point. No such reduction holds for an arbitrary continuous event time: its extremum sits
where it sits, and in the instance above it is attained at the balanced start, in the interior of the fibre.""")

sub('fibre-proof-fix',
    r"""$\tau$ is continuous, so its image is a
connected interval, and the extrema of a continuous function over a polytope are attained at vertices,
which is what the two programmes compute.""",
    r"""$\tau$ is continuous, so its image is a
connected interval. Its maximum is not a vertex value --- $\min_j$ of affine functions is concave, and a
concave function attains its maximum where it likes, here at $x_1 = x_2 = 50$ --- while its minimum over the
segment is attained at an end, where $\tau$ tends to $0$. The two programmes of the statement are read off
those two facts, and the fact that one of them is an interior value is why the polyhedral form is quoted with
its hypothesis instead of as a general method.""")

# ---- 4. Definition 34: the two compositions the sentence can name, and which one this article uses
sub('quotient-versus-rows',
    r"""**Proposition 36 (Conservation composes; closure does not).**""",
    r"""The two ways of reading the display above are different constructions, and the distinction is
load-bearing, so both are given. *Rows.* Take the disjoint union, keep every declared coordinate, and add the
equalities $x_a^1 = x_b^2$ for each $(a,b) \in J$ as constraint rows; capacities stay attached to the flux
columns. *Quotient.* Let $R$ be the class-incidence matrix of the equivalence relation generated by $J$, with
$R_{Ca} = 1$ exactly when $a \in C$, and set $x_C = R x_0$, $S_C = R\,[\,\mathrm{diag}(S_1, S_2)\ \ E\,]$,
$B_C = R B_0$, where an exchange $\varphi$ draining $a$ and filling $b$ enters as the column
$E_\varphi = -e_a + e_b$, and the classes are read off by connected components. The row form is the one this
article uses, because the certificates are stated on the declared coordinates and because the row form stays
meaningful when the interface defect of condition 1 fails; the quotient form is meaningful only when types and
units agree \emph{throughout} each class rather than pair by pair, and then the two coincide on the feasible
flux set. Condition 1's $\mathrm{type}(\cdot)$ is $\mathrm{ty}$ of Definition 47, which is what makes the
agreement check decidable from the declaration. Neither construction carries certificates across on its own:
the descent of a part's conservation law to the composition is exactly the agreement condition of
Proposition 36, and it can fail.

**Proposition 36 (Conservation composes; closure does not).**""")

# ---- 5. Definition 40: which way each branch of the verdict runs, and what the programme cannot say
sub('compensation-verdict',
    r"""Substitutability is decided by the joint programme, not by whether a capacity price is finite.""",
    r"""Substitutability is decided by the joint programme, not by whether a capacity price is finite.
The verdict has three branches and they should not be collapsed. Feasibility establishes steady-rate
compensation *under the declared inputs*. Infeasibility establishes failure of that programme, and it comes
with its own witness: a nonnegative combination of the constraint rows of the displayed system reducing to
$0 \le -1$, the linear-programming alternative read in the direction that certifies failure rather than the
one that certifies safety. Where the declaration is incomplete --- a substitution column missing, a shared
constraint unlisted, a target unnamed --- neither branch is available, and the predicate is reported as not
established, which is a statement about the declaration and not about the ledger. The programme is a
steady-rate object throughout: it says nothing about the trajectory between endpoints, and it establishes no
dynamic safety, no exit-time bound and no corridor invariance; those are the questions of Sections 3.5 to 3.6
and they need their own hypotheses. A positive interface charge does not prohibit compensation either: it
prices it, and with adequate stock, capacity and budget the composition may close --- which is why the charge
enters Definition 34's budgets and never its admissibility conditions.""")

# ---- 6. Remark 34: the price is certificate-relative, and a multiplier at a kink is a set
sub('price-is-certificate-relative',
    r"""and sums of squares can miss a certificate that exists, and that
failure is no evidence of unsafety.""",
    r"""and sums of squares can miss a certificate that exists, and that
failure is no evidence of unsafety.

Two dependencies belong with this reading. The interface price of Definition 35 is a *certificate-relative*
number: with unit service coefficients on both sides, $\lambda = (2,1)$ and $\lambda = (1,2)$ are both
feasible part certificates for the same pair of drain ledgers, and they return $\pi_\varphi = +1$ and
$\pi_\varphi = -1$ for the same declared exchange. Physical admissibility cannot turn on which certificate was
quoted, and in this article it does not: Definition 34's three conditions involve no multiplier, and
Definition 40's programme decides substitution without reference to either sign. What is certificate-relative
is the charge's size, so it is reported with the certificate that produced it rather than as a property of
the interface. A capacity multiplier is a selection in the same sense: the value of the shared-capacity
programme is a concave function of the capacity, at a kink its subdifferential is an interval --- in the
two-cycle instance of Definition 40, where the capacity equals the sum of the two cycles' own returns, that
interval is $[0, 1]$ in units of one cycle's marginal return --- and its one-sided derivatives at the kink
differ. A single quoted price there is a convention, and it is properly named as a supergradient of the value
function rather than as the shadow value of the capacity.""")

# ---- 7. the fisheries extract's vintage, pinned from the deposit record
sub('ram-vintage-pinned',
    r"""The extract is the RAM Legacy cohort of Ricard et al. (2012), and the pull date is archived in the analysis repository; the archived pull
has been re-verified row by row against the formula""",
    r"""The extract is the RAM Legacy cohort of Ricard et al. (2012) at release v4.66 (Zenodo 14043031,
6 November 2024), recorded as the cohort file of the supplementary's S5 record; its vintage is verified from
the extract's own contents, four of six published $F$ values reproducing that release exactly, and the pull
has been re-verified row by row against the formula""",
    old_tx=r"""The extract is the RAM Legacy cohort of Ricard et al.~(2012), and the pull date is archived in the analysis repository; the archived pull has been re-verified row by row against the formula""",
    new_tx=r"""The extract is the RAM Legacy cohort of Ricard et al.~(2012) at release v4.66 (Zenodo
14043031, 6 November 2024), recorded as the cohort file of the supplementary's S5 record; its vintage is
verified from the extract's own contents, four of six published \(F\) values reproducing that release
exactly, and the pull has been re-verified row by row against the formula""")

sub('ram-vintage-data-avail',
    r"""the RAM Legacy Stock Assessment Database (Ricard et al., 2012; the cohort pull date is archived in the analysis repository)""",
    r"""the RAM Legacy Stock Assessment Database, release v4.66 (Ricard et al., 2012; Zenodo 14043031; the cohort is the
dated extract recorded in the supplementary's S5 record, and no cohort statistic is quoted from any other release)""")


def unescape_display(tx):
    lines = tx.split('\n')
    out, i = [], 0
    while i < len(lines):
        st = lines[i].strip()
        if st.startswith('\\[') and st.endswith('\\]') and len(st) > 4:
            out.append(re.sub(r'(?<!\\)\\_', '_', lines[i])); i += 1; continue
        if st == '\\[':
            j = i + 1
            while j < len(lines) and lines[j].strip() != '\\]':
                j += 1
            if j < len(lines) and j - i <= 12:
                out += [re.sub(r'(?<!\\)\\_', '_', l) for l in lines[i:j + 1]]
                i = j + 1
                continue
        out.append(lines[i]); i += 1
    return '\n'.join(out)


def main():
    md, tx = open(MD_IN).read(), open(TEX_IN).read()
    hits, applied = [], []
    for name, old, new, old_tx, new_tx in E:
        m_md = pattern(old).search(md)
        o_tx = old_tx if old_tx is not None else m2t(old)
        n_tx = new_tx if new_tx is not None else m2t(new)
        m_tx = pattern(o_tx).search(tx)
        hits.append((name, 'md' if m_md else 'MD-MISS', 'tex' if m_tx else 'TEX-MISS'))
        if not (m_md and m_tx):
            continue
        if md.count(old) > 1 or (old_tx and tx.count(old_tx) > 1):
            print(f'{name}: AMBIGUOUS anchor (md {md.count(old)} hits)')
        md = md[:m_md.start()] + new + md[m_md.end():]
        tx = tx[:m_tx.start()] + n_tx + tx[m_tx.end():]
        applied.append((name, old, new, o_tx, n_tx))
    for n, a, b in hits:
        print(f'{n[:30]:32s} {a:9s} {b}')
    if any('MISS' in h[1] + h[2] for h in hits):
        print('\naborted: unmatched anchors'); sys.exit(1)
    tx = unescape_display(tx)
    bad = sorted({c for c in tx if ord(c) > 127})
    ndbl = max(len(re.findall(r'\\\\[a-zA-Z{]', t)) for t in [tx])
    print('tex non-ascii:', bad, '| square left:', SQ in tx, '| doubled backslashes in tex:', ndbl)
    if bad or ndbl:
        print('aborted: dialect problem'); sys.exit(1)
    open(MD_OUT, 'w').write(md)
    open(TEX_OUT, 'w').write(tx)
    json.dump([{'name': n, 'old': o, 'new': nw, 'old_tex': ot, 'new_tex': nt}
               for n, o, nw, ot, nt in applied], open(LOG, 'w'), indent=1)
    print(f'\nwrote {MD_OUT} ({len(md)} B), {TEX_OUT} ({len(tx)} B) | edits: {len(applied)}')


if __name__ == '__main__':
    main()
