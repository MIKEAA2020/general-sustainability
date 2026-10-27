# Source diff summary: Paper06 v75 → v76

This summary lists the substantive source differences. Edition labels, TeX filenames, and modular-directory paths were also updated from v75 to v76 in the derivative.

| Location | v75 → v76 change |
|---|---|
| Abstract (`00_front.tex`) | Makes the comparison explicit: `12/5` is the unnormalised equal-weight margin sum and it exceeds the witness’s licensing threshold `2`. |
| Witness point (`03_witness.tex`) | Corrects the malformed source token after `r=` from an actual tab plus `frac12` to `\tfrac12`. |
| Theorem 4 (i)–(ii) (`03_witness.tex`) | Specifies that the finite-rung conclusion applies on the deep interior, with both floors strictly between 1 and 2. The pointwise rejection claim remains on the strict interior of the floor-margin region. Gap states with `min(s_1,s_2) <= 1` are identified as linear-only states, not collectively called boundary states. No mathematical conditions or conclusions were altered. |
| §6.4 (`04b_related.tex`) | Adds: “The four novelty claims below regroup the five contributions in Section 1.3.” |
| Data Availability (`07_refs.tex`) | Adds the v75 commit and a direct link to `companion_restorations_20261026/Paper06_v75` at `0208f8b1523446a32ef48cbfe50415fe7ec78947`. |
| SI proof (`si_00_front_proofs.tex`) | Restricts the positive-tube/finite-rung argument to the deep interior and clarifies the `min(s_1,s_2) <= 1` case. |

The assembled main/SI files and their edited modular parts are synchronized. All figure assets are unchanged. V76 is local-only; v75 remains the preserved parent.
