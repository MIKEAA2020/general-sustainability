# R3 — MapBiomas Brazil: reference Collection 3 labels and design information

**Route:** email to the MapBiomas Brazil team (via mapbiomas.org contact / the Brazil working group).
**Unblocks:** F13 item 5 (current map reference calibration) and item 1 (Brazil calibrated AGB change).

---

**Subject:** Request for Collection 3 reference labels and design weights (academic, non-commercial)

Dear MapBiomas Brazil team,

I am an independent researcher comparing national land-change mappings against biological-supply
accounts. Brazil is one of eight national cases. I have acquired the currently linked vector archive for
Collection 11 and the current Collection 11 coverage asset
(`mapbiomas_brazil_collection11_coverage_v3`), but the reference side is the bottleneck, and I would be
grateful for guidance or access.

**What I have.** The October 2026 vector archive (85,152 records / 126 fields, DBF header inspected
without expanding the 209 MB table) ending in 2022, with only about 4,053 non-blank 2015/2023 pairs, of
which roughly 4,041 survive non-observed/training filtering and 3,042 are additionally non-edge at both
endpoints. The current documentation refers to reference collection 3 through 2024. Those counts,
vintages and filters are not a compatible national change-calibration sample.

**What I am requesting** — the following, for **reference Collection 3**, at the **2015 and 2023**
endpoints:

1. **Reference point labels** at those two endpoints, with point identifiers that permit pairing.
2. **Design information**: inclusion probabilities or design weights, sample design/stratification, and
   the estimator used for area and for change.
3. **Training/validation role flags** for each point, so training-overlap can be handled explicitly —
   points used to train the classifier cannot be treated as independent validation.
4. **Boundary and sparse-class rules**: how the Brazil polygon boundary, coastal/water classes and rare
   classes are handled in area and error accounting.
5. **Interpreter harmonization and the Collection 11 crosswalk**: the class mapping between reference
   classes, the collection in which the points were interpreted, and Collection 11 output classes.
6. If available, **confusion information** at the class-set level — specifically initial-forest to
   final-destination transitions — not only overall map accuracy.

**Why these specific items.** My target is not overall accuracy. It is a defensible **class-set
symmetric-difference** budget for conversions, which is what a boundary-matched account comparison
requires; net-area error alone does not supply it. Marginal design-based intervals, or valid
all-population/class-set error upper bounds, are sufficient — I am not asking for an exact paired field
census, and I do not require a known cross-year covariance. If the requested precision is not
achievable, an explicit statement of that bound would still let me report the Brazilian case honestly
rather than substituting a narrower error bar.

I will cite MapBiomas as specified, will not redistribute point records, and will publish only derived
aggregates and error bounds under your stated terms. I am also happy to be pointed to an existing
access route or form instead of an email reply.

Amin Abaee
Independent Researcher, Tehran, Iran — amin_abaee@ut.ac.ir
ORCID 0000-0002-0019-1842
