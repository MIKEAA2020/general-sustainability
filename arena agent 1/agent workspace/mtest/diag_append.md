
---

# Signal promotion, and the semantic duplicate test (2026-10-01)

**C promoted to fatal** as `K.place-tail`. 20 hits, 100% precision, zero
live-head hits today -- it is a guard against future merges, which is the point
of promoting it. One correction made while promoting: the `CORPORATE` author
guard was initially applied here too, and it suppressed five genuine tails
(`Cambridge University Press, Cambridge.`, `Eurostat, Luxembourg.`, `OECD
Publishing, Paris.`, `Princeton University Press, Princeton, NJ.`, `Fisheries
and Oceans Canada, Ottawa.`) because publisher names end in the same words
institutional authors do. `PLACE_TAIL` alone is 20/20. The guard belongs only
on the no-year/no-author signal, where the USGS false positive arose. A guard
added to fix one signal can silently blind another.

**B stays report-only.** The `CORPORATE` guard removed its two false positives
(`U.S. Geological Survey. National Water Information System...` in paper11 v64
and paper11b v2 -- a legitimate year-less government data citation), taking it
from 18 hits to 15. Re-measure before promoting.

**E dropped.** 0-for-3.

**Byte-identity replaced by `same_work()`.** Byte-identity is a proxy and the
wrong one: two entries citing one report differ in citation style and nothing
else, so the proxy reports "they differ" and leaves a human to notice the report
number matches. Identity is now decided by a shared DOI, a shared report
number, or the same year plus >=60% title-token overlap. `L.dup-ref-key` fires
only on the same work, so the finding reads "merge these" rather than "check
whether these conflict". Corpus findings: 32 -> 18.

## The lesson recorded

The gate's clean verdict was **wrong twice in two turns**: once because it
counted findings and called them files, once because it could not see the TWDB
pair. Both times reading caught it. So a clean verdict must now **name the
checks that produced it**, the report-only detector runs on live heads as a
**routine** rather than only after repairs, and the corpus is not audited until
the reading pass and the detector pass agree. Neither alone is sufficient.
