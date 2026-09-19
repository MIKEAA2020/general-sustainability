"""v4 = v3 + the eight sentences the Section 2.1/1.x/3.x/8.1 compression dropped.
Every restoration is copied from work/paper3.txt (source of record) and adapted only in cross-reference numbers.
Anchors are asserted unique; a non-unique or missing anchor is reported and skipped."""
SRC = 'revision/v3/paper3_v3.md'
DST = 'revision/v4/paper3_v4.md'
t = open(SRC, encoding='utf-8').read()
applied, skipped = [], []
def _ins(anchor, text, tag, pos):
    global t
    n = t.count(anchor)
    if n != 1:
        skipped.append(f"{tag}: anchor count {n} :: {anchor[:70]!r}")
        return
    i = t.find(anchor) + (len(anchor) if pos == 'after' else 0)
    t = t[:i] + text + t[i:]
    applied.append(tag)

def after(anchor, text, tag):
    _ins(anchor, text, tag, 'after')

def before(anchor, text, tag):
    _ins(anchor, text, tag, 'before')


after("The problem is promotion: an answer to one question is read as an answer to another.",
"""
The same conflation pervades accounting itself. Material flow analysis supplies the bookkeeping of society's material throughput (Brunner and Rechberger, 2004; Eurostat, 2001; Fischer-Kowalski et al., 2011), and its incidence structure is shared with reaction-network theory, where the sign pattern of the stoichiometric matrix is a conservation object (Feinberg, 2019). Bookkeeping balance, stoichiometric conservation, thermodynamic admissibility, and sustainability safety are four different predicates, and the literature routinely slides between them. A mass-balanced ledger can be chemically impossible. A chemically consistent ledger can violate every declared barrier. A ledger satisfying all declared barriers can fail conservation. Separating these layers and proving their relationships, so that each claim about a material system carries the predicate it actually establishes, is this article's first task.""",
"§1.1 four predicates + accounting lineage")

after("The size of the pool is a property of the resource; whether drawdown is recoverable is a property of the rate.",
""" The pool may be read as natural capital, as a stock, or as a slowly regenerating flow of services: these are overlapping readings of the same pool, not mutually exclusive ones. Every such pool is regenerative on some timescale — a crop within a season, an aquifer within years to decades, a mineral deposit over geological time — and the failure is the same in each case. A drawdown is recoverable only insofar as the pool regenerates faster than it is taken; if a pool regenerates too slowly for the rate at which it is taken, the drawdown is still liquidation.""",
"§1.2 timescales + recoverability condition")

after("These are different ledger entries with different statuses.",
""" The balance must be maintained as neither consumption nor population grows faster than the productivity that supports them, and the drawdown must not be recoverable only on a timescale longer than it is taken (Daly, 1990). The scenario-conditioned hitting time of Definition 5 exists to give that drift a horizon.""",
"§1.3 Daly rate condition + horizon object")

after("Conversely, a trajectory can satisfy declared barriers while violating a conservation law or stoichiometric constraint.",
""" Thermodynamic admissibility — energy conservation, entropy-production non-negativity, reaction feasibility — implies accounting consistency, but the converse does not hold, and this article establishes the three layers above without claiming the fourth.""",
"§3.3 Proposition 2 thermodynamic clause")

after("or silently drops a moiety through a yield-routing omission.",
""" Thermodynamic admissibility presupposes a mass balance, but a mass-balanced flux decomposition need not satisfy energy or entropy constraints; establishing those requires structure outside the present scope.""",
 "§3.3 Proposition 2 proof, second clause")

after("The contribution is the accounting grammar that keeps those tasks separate.",
"""
**What is not claimed.** No stochastic completion of the ledger is claimed: the surrogate processes of Section 9 do not conserve the ledger's mass and are not perturbations of its dynamics. No thermodynamic admissibility is claimed. No identification of the two-pool groundwater hypothesis is claimed: its identification requirements are registered in Section 8.1, not discharged. And no empirical finding about any basin, aquifer, or fishery is claimed beyond the descriptive status of the tabulated indicators.""",
"§1.5 What is not claimed")

after("it does not measure access infrastructure, recharge, or the physical bottom of the aquifer.",
""" An index built on the anomaly series therefore cannot distinguish a drawdown of stored water that is recoverable on the recharge timescale from one that is not — although heavy over-extraction can make the loss permanent through compaction, subsidence or saline intrusion, in which case it is not recoverable at all.""",
"§8.1 recoverability and permanence clause")

after("the box is what is audited, the polytope what is realizable.",
""" The envelope is the interval-arithmetic counterpart, at the level of declared flux bounds, of the data-reconciliation practice of material flow analysis (Brunner and Rechberger, 2004): reconciliation solves unmeasured fluxes under an imposed mass balance, and the envelope bounds them without solving them.""",
"§3.6 reconciliation-lineage sentence")

before("Upper-barrier violations matter symmetrically.",
r"""Two disciplines attach. First, equality at the hitting time, \(S_m(\tau_m^-)=\underline{B}_m(\tau_m^-)\), requires continuity of both \(S_m\) and \(\underline{B}_m\) and appropriate initial separation: if fluxes or barriers can jump, the stock can cross the barrier without satisfying equality. Second, lower barriers need not be exhaustion thresholds. The diagnostic distinguishes physical exhaustion \(S_m=0\), functional failure \(S_m=\mathcal{B}^{\mathrm{func}}_m\), a resilience or regime-shift threshold, an economically recoverable reserve, and a minimum service-supporting stock; the term exhaustion is reserved for \(S_m=0\), and every other threshold is a barrier violation. """,
"§6.3 hitting-time equality + five-way threshold taxonomy")

open(DST, 'w', encoding='utf-8').write(t)
print(f"applied {len(applied)}:")
for a in applied: print("   OK   " + a)
print(f"skipped {len(skipped)}:")
for s in skipped: print("   SKIP " + s)
print("chars:", len(t), "| words:", len(t.split()))
