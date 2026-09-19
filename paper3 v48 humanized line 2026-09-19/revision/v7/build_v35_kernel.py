#!/usr/bin/env python3
"""v35 kernel: the joint-assessment corrections to the composition calculus, applied to md and tex
together so the two formats stay consistent. Every edit is logged so v35 -> v34 reverses exactly.

Provenance of each edit: review/joint_master_assessment_v1.md (adjudication of the three external
responses, each re-derived independently in repo_audits/verify_joint.py).
"""
import re, sys, json

HERE = '/home/user/revision/v7'
MD_IN = f'{HERE}/paper3_material_ledgers_v34.md'
TEX_IN = f'{HERE}/paper3_material_ledgers_v34.tex'
MD_OUT = f'{HERE}/paper3_material_ledgers_v35.md'
TEX_OUT = f'{HERE}/paper3_material_ledgers_v35.tex'
LOG = f'{HERE}/revisions_v35_kernel_log.json'

# ---------------------------------------------------------------- md -> tex dialect
# Rules are the ones the shipped v33/v34 tex actually uses:
#   **X** -> \textbf{X};  *X* -> \emph{X};  $X$ -> \(X\);  U+25A1 -> \ensuremath{\square};
#   inside a \[ ... \] display block a bare underscore is written \_. Nothing else changes.
SQ = '\u25a1'


def _prose(t):
    t = re.sub(r'\*\*(.+?)\*\*', lambda m: '\\textbf{' + m.group(1) + '}', t, flags=re.S)
    t = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', lambda m: '\\emph{' + m.group(1) + '}', t, flags=re.S)
    return t.replace(SQ, '\\ensuremath{\\square}')


def _display(body):
    return body   # display math is written verbatim: `\_' would render a literal underscore


def m2t(s):
    out, i = [], 0
    tok = re.compile(r'\$\$[\s\S]*?\$\$|\$[^$]*\$|\\\[[\s\S]*?\\\]')
    for m in tok.finditer(s):
        out.append(_prose(s[i:m.start()]))
        t = m.group(0)
        if t.startswith('$$'):
            out.append('\\[ ' + t[2:-2].replace('\n', ' ').strip() + ' \\]')
        elif t[0] == '$':
            out.append('\\(' + t[1:-1].replace('\n', ' ').strip() + '\\)')
        else:
            out.append('\\[' + _display(t[2:-2]) + '\\]')
        i = m.end()
    out.append(_prose(s[i:]))
    return ''.join(out)


# ---------------------------------------------------------------- matching
def flex(s):
    """Literal pattern tolerant of whitespace runs and of latex escapes of _ ^ { } & % #."""
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c.isspace():
            j = i
            while j < len(s) and s[j].isspace():
                j += 1
            out.append(r'\s+')
            i = j
            continue
        if c in '_^{}&%#':
            out.append('(?:' + re.escape('\\' + c) + '|' + re.escape(c) + ')')
        else:
            out.append(re.escape(c))
        i += 1
    return ''.join(out)


def pattern(s):
    """Compile a matcher for `s`; '$' (md) may appear as \( \) (tex)."""
    return re.compile(r'(?:\$|\\\(|\\\))'.join(flex(p) for p in s.split('$')))


E = []


def sub(name, old, new, old_tx=None, new_tx=None):
    """old/new are md-dialect; pass old_tx/new_tx when the tex file spells the text differently."""
    E.append((name, old, new, old_tx, new_tx))


def ins(name, anchor, block):
    """Insert `block` before `anchor`, logged as anchor -> block + anchor so it reverses."""
    E.append((name, anchor, block + anchor, None, None))


# ---- 1. interface price: orientation-free magnitude, and the n-part caveat (Def 35 tail)
sub('def35-price-sign',
    """A non-positive price means the exchange enters the combined budget of the composition with the wrong sign to cost anything; a positive price is margin consumed per unit of flux per unit of time.""",
    """A price is margin consumed (positive) or margin released (negative) per unit of interface flux per
unit of time, *in the declared orientation*: what the composition must budget for is the magnitude
$|\\pi_\\varphi|\\,\\bar v_\\varphi T$, and the sign only decides which side pays. Reversing an exchange's
declared direction leaves that magnitude unchanged and moves the charge to the partner ledger, so no claim
of a free interface can rest on the sign of $\\pi_\\varphi$ alone. The additivity of these charges is
asserted for a two-part composition; a composition of three or more parts sharing a compartment needs a
declared global interface, because a flux the whole admits need not decompose into part-wise admissible
exchanges, and two parts each delivering into a third attain service their summed budgets do not cover.""")

# ---- 2. Prop 36 first clause: only compatible conserved vectors survive an identification
sub('prop36-lift',
    """Every left-null vector of $S_1$ and of $S_2$ lifts to a left-null vector of the composition, constant along identified compartments, so the conserved totals of the parts are conserved in the whole.""",
    """The conserved quantities of the composition are exactly the pairs of part-wise left-null vectors that
agree on every identified compartment: such a pair lifts to a conservation of the whole, and every
conservation of the whole arises that way. The lift is injective and need not be onto, so a conserved total
of a part can be destroyed by an identification the typing permits.""")

sub('prop36-proof',
    """*Proof.* For the lift, $\\ell^{\\top} \\mathrm{diag}(S_1, S_2) = 0$ with equal entries on identified
compartments gives $\\ell^{\\top} S = 0$ on the quotient, since the identification rows are the only
further constraints and they are annihilated by equality of the paired entries.""",
    """*Proof.* The identification rows are the only further constraints, so a covector is left-null on the
quotient precisely when its pullback is left-null on each part and constant on each identification class;
the pullback is therefore injective, with image the compatible subspace, and it is not onto. Witness: two
compartments in series in each part carry two moieties, and after the admissible identification of the two
middle compartments the quotient carries one, so the moiety of the first part is gone. Which subspace
survives is a rank computation on the declared data --- with $D_J$ the matrix of merged-compartment rows,
the surviving conserved covectors are $(U_1 \\oplus U_2) \\cap \\ker D_J^{\\top}$ --- the same computation
that decides closure.""")

sub('prop36-proof-dummy',
    """the composition's programme is $\\max \\lambda$ subject to $q = \\lambda$, $s = \\lambda$, $q + s \\le 1.5$
with $q, s \\ge 0$, whose optimum is $\\lambda = 0.75$;""",
    """the composition's programme is $\\max \\mu$ subject to $q = \\mu$, $s = \\mu$, $q + s \\le 1.5$
with $q, s \\ge 0$, whose optimum is $\\mu = 0.75$;""")

# ---- 3. Prop 37: corrected cost term, sufficiency only, corrected instance
sub('prop37-display',
    """\\[
B_1 + B_2 + \\sum_{\\varphi \\in \\Phi} \\pi_\\varphi^{+}\\, \\bar v_\\varphi\\, T,
\\qquad \\pi^{+} = \\max\\{\\pi, 0\\}.
\\]""",
    """\\[
B_1 + B_2 + \\sum_{\\varphi \\in \\Phi} |\\pi_\\varphi|\\, \\bar v_\\varphi\\, T .
\\]""")

sub('prop37-free',
    """The sum is the *margin needed* to absorb the interface; the interface is free, in the sense that the
parts' budgets add without remainder, exactly when $\\pi_\\varphi \\le 0$ for every declared exchange.""",
    """The sum is the *margin needed* to absorb the interface; the parts' budgets add without remainder
exactly when every declared interface either releases margin on the side that carries the budget or is
slack at its declared bound. Under the outflow-negative convention of Definition 35 the sharper charge
$(-\\pi_\\varphi)^{+}\\bar v_\\varphi T$ applies and the interface is free when $\\pi_\\varphi \\ge 0$.""")

sub('prop37-lmax',
    """With a single exchange of box $[0, L]$, price $\\pi > 0$ and horizon $T$, the composition is certified
if and only if
\\[
L \\;\\le\\; L_{\\max} := \\frac{B_1 + B_2}{\\pi\\, T}.
\\]
Instance: $G_1 = G_2 = 1$, $\\lambda_1 = 2$, $\\lambda_2 = 1$, so $\\pi = 1$; with $B_1 + B_2 = 9$ units
of margin and $T = 30$ yr, $L_{\\max} = 0.30$ unit per year --- an exchange at $0.2$ stays inside the
combined budget ($6 \\le 9$) and one at $0.5$ does not ($15 > 9$).""",
    """With a single exchange of box $[0, L]$, non-zero price $\\pi$ and horizon $T$, this multiplier pair
certifies the composition whenever
\\[
L \\;\\le\\; L_{\\max} := \\frac{B_1 + B_2}{|\\pi|\\, T},
\\]
and at $L = L_{\\max}$ the interface charge equals the combined budget by construction. The converse is not
claimed: another multiplier pair can certify a rate this one does not, and the exact threshold for the
declared horizons is the value of the joint programme over the fibre product of the two declared polytopes
--- not the scalars $\\lambda_i$, $G_i$, $\\pi$ quoted here, which do not determine it on their own.
Instance: $G_1 = G_2 = 1$, $b_1 = b_2 = 0$, $\\lambda_1 = 1$, $\\lambda_2 = 2$, so $\\pi = -1$ and the
exchange drains the ledger holding the cheaper margin; with $B_1 + B_2 = 9$ units of margin and $T = 30$
yr, $L_{\\max} = 0.30$ unit per year --- an exchange at $0.2$ stays inside the combined budget ($6 \\le 9$)
and one at $0.5$ does not ($15 > 9$). Interchanging the two multipliers leaves the magnitude unchanged and
moves the charge to the other ledger.""")

sub('prop37-proof',
    """Along the composition, $\\dot V \\le -(y_1 + y_2) + \\lambda_1^{\\top}
G_1 b_1 + \\lambda_2^{\\top} G_2 b_2 + \\sum_\\varphi \\pi_\\varphi f_\\varphi$: the exchange terms are the
only ones that do not decouple, because a flux that leaves margin in one part enters it in the other at
the partner's multiplier. Bounding $f_\\varphi$ by $\\bar v_\\varphi$ on $\\pi_\\varphi > 0$ and by $0$
otherwise, and integrating with $V(T) \\ge 0$, gives the stated budget. The one-dimensional case is the
equality $L \\pi T = B_1 + B_2$ solved for $L$. □""",
    """Along the composition, $\\dot V \\le -(y_1 + y_2) + \\lambda_1^{\\top} G_1 b_1 + \\lambda_2^{\\top}
G_2 b_2 - \\sum_\\varphi \\pi_\\varphi f_\\varphi$: the exchange terms are the only ones that do not
decouple, because a flux that leaves margin in one part enters it in the other at the partner's
multiplier. Each interface term is then bounded over its box by its worst case,
$\\max_{0 \\le f \\le \\bar v_\\varphi}(-\\pi_\\varphi f) = (-\\pi_\\varphi)^{+}\\bar v_\\varphi \\le
|\\pi_\\varphi|\\bar v_\\varphi$, and integrating with $V(T) \\ge 0$ gives the stated budget. The
one-dimensional case is the equality $L|\\pi|T = B_1 + B_2$ solved for $L$. □""")

# ---- 4. compensation as a decidable predicate, then the scope of the multiplier search
ins('def40-remark34',
    """These three statements are the calculus the article's own citations had deferred to a companion: an""",
    """**Definition 40 (Compensation as a decidable predicate).** Fix a partition of the declared
compartments into donor and recipient sides, a demanded service rate, and the joint polytope of the
composition. *Compensation holds at fraction $\\kappa$* when one linear programme on that polytope is
feasible: maximise the recipient's sink-weighted margin release net of the donor's, subject to the joint
polytope, to the demanded service, and to the donor's budgets being drawn at no more than $\\kappa$ times
what its own service costs; the predicate is true when the optimum covers the demanded drawdown. It is a
feasibility test on the fibre product rather than a price comparison, and it is the exact form of the
question the aggregation cannot answer. Prices do not substitute for it: the shared return capacity that
leaves each of the two cycles of Proposition 36 closing at $\\Lambda^{*} = 1$ individually puts the
composition at $\\Lambda^{*} = 0.75$, and cutting one side's own return capacity to $10^{-4}$ units per
year leaves that shared-capacity programme well posed and finite while the cut side cannot close at all.
Substitutability is decided by the joint programme, not by whether a capacity price is finite.

**Remark 34 (What the multiplier search can and cannot prove).** The certificates above search over the
conservation multipliers $\\lambda$ alone, because those are what the declared conservation structure
supplies; the capacity and box rows of the declared polytope carry no multiplier, and the gap is visible
in a single-compartment example: with $\\dot m = -y + \\sigma$, $y \\in [0, 1]$, $m(0) = \\sigma(0) = 0$
and $m(T) \\le 1$, a certificate built from $\\lambda$ only returns $100.0$ units of cumulative service
where the exact value over the horizon is $1.0$, and pricing the capacity row as well --- the full dual
pair $\\lambda = 0$, $\\rho = 1$ --- returns $1.0$ exactly. The same refinement applies to the interface
bound of Proposition 37. In the other direction the search is complete for the terminal affine relaxation
of a linear differential inclusion, and on the joint polytope exactness follows from Definition 19's
programme; it is not complete for quadratic certificates, since a valid quadratic margin need not be a sum
of squares --- Motzkin's polynomial is the standard non-negative-not-sum-of-squares obstruction --- so a
search restricted to diagonal multipliers and sums of squares can miss a certificate that exists, and that
failure is no evidence of unsafety.

""")

# ---- 5. Prop 39: the interval needs continuity and connectedness, not monotonicity
sub('prop39-interval',
    """More generally, where the declared constraints are linear and the event time is monotone in the initial state along the fibre, $\\mathrm T(z)$ is the image of a polytope, so its endpoints are the values of two linear programmes over that polytope""",
    """More generally, where the declared constraints are linear the fibre is a polytope, and a continuous
event time has an interval image on a connected fibre: $\\mathrm T(z)$ is that interval, and its endpoints
are the values of two linear programmes over the polytope. Monotonicity of the event time along the fibre
is neither needed nor true in general --- an exit time is typically the minimum of several monotone branch
functions, which is not itself monotone --- and where the declared set is non-convex the fibre can split,
in which case the same two programmes bound the value set from outside instead of recovering it""")

sub('prop39-proof',
    """The fibre is an intersection of the declared\nboxes with the invariant hyperplane, hence a polytope, and monotonicity supplies the two extremal\nprogrammes.""",
    """The fibre is an intersection of the declared
boxes with the invariant hyperplane, hence a convex polytope; $\\tau$ is continuous, so its image is a
connected interval, and the extrema of a continuous function over a polytope are attained at vertices,
which is what the two programmes compute.""")

# ---- 6. transfer-noise discipline in 7.1
sub('sec71-noise-typing',
    """and the results are statements about the declared class.""",
    """and the results are statements about the declared class. Transfer noise obeys the same typing as
transfer fluxes: process noise on a conserved moiety must be zero-sum across the pools it moves between,
or must carry an explicit boundary term; where it does neither, the violation is a residual and belongs in
the budget of Definition 23, not in the drift --- a diffusion that creates mass is not a conservative ledger
with noisy data but a different object. The converse discipline holds as well: a bracket on the drift of a
selected set does not transfer to a bracket on its support or on its exit time, so no drift bound in this
section is a deterministic hitting time, and the surrogate means are means.""")

# ---- 7. closure capacity re-lettered Lambda* (lambda* collided with the certificate multiplier)
sub('lambda-star-to-Lambda',
    """$\\lambda^{*}=\\max\\{\\lambda:\\ \\lambda D\\in P(\\mathcal K)\\}$""",
    """$\\Lambda^{*}=\\max\\{\\mu:\\ \\mu D\\in P(\\mathcal K)\\}$""")
sub('lambda-star-to-Lambda2',
    """Where $\\lambda^{*}\\ge1$, the cycle closes at the demanded rate. Where $\\lambda^{*}<1$,""",
    """Where $\\Lambda^{*}\\ge1$, the cycle closes at the demanded rate. Where $\\Lambda^{*}<1$,""")
sub('lambda-star-to-Lambda3',
    """each therefore closing tightly at $\\lambda^{*} = 1$; when the two return fluxes draw on a single declared capacity of $1.5$ units per year, the composition has $\\lambda^{*} = 0.75$""",
    """each therefore closing tightly at $\\Lambda^{*} = 1$; when the two return fluxes draw on a single declared capacity of $1.5$ units per year, the composition has $\\Lambda^{*} = 0.75$""")

# ---- 8. Definition 23: C is the moiety-composition matrix, not a readout matrix
sub('def23-C-label',
    """with $C$ the readout matrix of Section 2.1,""",
    """with $C$ the moiety-composition matrix of Section 2.1 (Lemma 3),""")


# ---- 9. Remark 33: the registered absence is discharged with the component table it asked for
sub('remark33-premium',
    """No premium figure is reported in this article, because
the component tables of the published construction are not reproduced here.""",
    """A figure can be read straight off the published component table: on the world totals of the National
Footprint and Biocapacity Accounts as tabulated by Lin et al. (2018), the 2022 aggregate ratio is $0.584$
of biocapacity to demand, so $\\tau_{\mathrm{agg}} = 213$ d, and because the carbon component carries zero
biocapacity the minimum component ratio is $0$ --- hence $\Pi_\\tau = 213$ d, the whole aggregate date.
Restricted to the five components of positive biocapacity with renormalised weights, the same arithmetic
gives $\\tau_{\mathrm{agg}} = 538$ d against $\\tau_{\min} = 365$ d, a premium of $173$ d, and the
restricted premium runs $547$ d (1961), $346$ d (1980), $251$ d (2000), $173$ d (2022): it shrinks as the
components converge, exactly as the display says it must. Which convention a reported premium uses is a
property of the accounts, not of the theorem --- including the zero-biocapacity carbon row makes
$\\tau_{\min} = 0$ identically, and a construction over positive components alone can return
$\\tau_{\mathrm{agg}} > 365$ d, which states that no component overshoots within the year rather than that
no overshoot occurs --- so the convention is declared with the figure, and the figures above are world
totals, not any territory's.""")

# ---- 10. numbering note: the counter now runs to 43 and Remark 34 exists
sub('numbering-range',
    """runs on the single 1–39 sequence counter""",
    """runs on the single 1–44 sequence counter""",
    old_tx="""runs on the single 1--39 sequence counter""",
    new_tx="""runs on the single 1--44 sequence counter""")

sub('numbering-added',
    """the statements added at this revision carry the consecutive labels Definitions 21–23 and 34–35 and 38, Theorem 24, and Propositions 25–32 and 36–37 and 39, with Remark 33,""",
    """the statements added at this revision carry the consecutive labels Definitions 21–23 and 34–35 and 38 and 40–44, Lemma 4, Theorem 24, and Propositions 25–32 and 36–37 and 39–40, with Remarks 33 and 34,""",
    old_tx="""the statements added at this revision carry the consecutive labels Definitions 21--23 and 34--35 and 38, Theorem 24, and Propositions 25--32 and 36--37 and 39, with Remark 33,""",
    new_tx="""the statements added at this revision carry the consecutive labels Definitions 21--23 and 34--35 and 38 and 40--44, Lemma 4, Theorem 24, and Propositions 25--32 and 36--37 and 39--40, with Remarks 33 and 34,""")



def unescape_display(tx):
    """Write math underscores bare inside display equations. `\\_' is a *visible* underscore glyph in TeX
    math mode, so the v33 port's escaping of it broke every display equation of the shipped PDFs.
    Line-anchored rule, so no prose is ever swept into a region: a display is either a single line
    beginning `\\[` and ending `\\]`, or a block whose first line is `\\[` and last line is `\\]`."""
    lines = tx.split('\n')
    out, n, i = [], 0, 0
    def fix(l):
        seg, k = re.subn(r'(?<!\\)\\_', '_', l)
        return seg, k
    while i < len(lines):
        l = lines[i]
        st = l.strip()
        if st.startswith('\\[') and st.endswith('\\]') and len(st) > 4:
            f, k = fix(l); out.append(f); n += k; i += 1; continue
        if st == '\\[':
            j = i + 1
            while j < len(lines) and lines[j].strip() != '\\]':
                j += 1
            if j < len(lines) and j - i <= 12:
                for l2 in lines[i:j + 1]:
                    f, k = fix(l2); out.append(f); n += k
                i = j + 1; continue
        out.append(l); i += 1
    return '\n'.join(out), n



# ---- 21. pre-existing port defect: `\Oksendal` is an undefined control sequence (an uppercase \O is a
# command, not an accent taking an argument), and it halted the XeTeX run at the 7.1 lineage sentence.
sub('Oksendal-braces',
    "the stochastic machinery is It\u00f4 calculus in its textbook form (\u00d8ksendal, 2003)",
    "the stochastic machinery is It\u00f4 calculus in its textbook form (\u00d8ksendal, 2003)",
    old_tx=r"""the stochastic machinery is It\^o calculus in its textbook form (\Oksendal, 2003)""",
    new_tx=r"""the stochastic machinery is It\^o calculus in its textbook form (\O{}ksendal, 2003)""")

BLOCK_41_43 = open(f'{HERE}/v35_block_predicates.md').read()
ins('def41-43-predicates',
    """These three statements are the calculus the article's own citations had deferred to a companion: an""",
    BLOCK_41_43)

BLOCK_CLOCKS = open(f'{HERE}/v35_block_clocks.md').read()
ins('def44-lemma4',
    """These three statements are the calculus the article's own citations had deferred to a companion: an""",
    BLOCK_CLOCKS)

def main():
    md = open(MD_IN).read()
    tx = open(TEX_IN).read()
    hits, applied = [], []
    for name, old, new, old_tx, new_tx in E:
        m_md = pattern(old).search(md)
        o_tx = old_tx if old_tx is not None else m2t(old)
        n_tx = new_tx if new_tx is not None else m2t(new)
        m_tx = pattern(o_tx).search(tx)
        hits.append((name, 'md' if m_md else 'MD-MISS', 'tex' if m_tx else 'TEX-MISS'))
        if not (m_md and m_tx):
            continue
        md = md[:m_md.start()] + new + md[m_md.end():]
        tx = tx[:m_tx.start()] + n_tx + tx[m_tx.end():]
        applied.append((name, old, new, o_tx, n_tx))
    for n, a, b in hits:
        print(f'{n[:26]:28s} {a:9s} {b}')
    if any('MISS' in h[1] + h[2] for h in hits):
        print('\naborted: unmatched anchors')
        sys.exit(1)
    tx, nfix = unescape_display(tx)
    bad = sorted({c for c in tx if ord(c) > 127})
    print('tex non-ascii:', bad, '| placeholder left:', SQ in tx,
          '| display underscores unescaped:', nfix)
    open(MD_OUT, 'w').write(md)
    open(TEX_OUT, 'w').write(tx)
    json.dump([{'name': n, 'old': o, 'new': nw, 'old_tex': ot, 'new_tex': nt}
               for n, o, nw, ot, nt in applied], open(LOG, 'w'), indent=1)
    print(f'\nwrote {MD_OUT} ({len(md)} B), {TEX_OUT} ({len(tx)} B) | edits: {len(applied)}')


if __name__ == '__main__':
    main()
