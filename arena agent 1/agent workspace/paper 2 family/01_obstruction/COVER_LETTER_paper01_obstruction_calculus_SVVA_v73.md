**To the Editors, *Set-Valued and Variational Analysis***

Dear Editors,

I submit the manuscript *Obstruction certificates for viability under incomplete observation: a calculus of sufficient conditions for nonviability, with exact finite and polyhedral cases* for consideration as a research article.

**Problem.** Viability theory under incomplete observation has a well-developed sufficiency side—Veliov's output-feedback condition, the estimation-tube reduction of Kurzhanski–Vályi and Cardaliaguet–Quincampoix–Saint-Pierre, barrier certificates—but no comparable apparatus for the obstruction side: proving that a given observation structure *cannot* sustain a given constraint set, and saying why. Doyen (2000) records this direction as undeveloped.

**Contribution.** The manuscript supplies that apparatus as a calculus of certificates organised by one principle: an observation-based regulator must choose a single response for an entire information state, and each certificate proves the relevant response correspondence empty. In finite systems the principle is exact (sound and complete backward recursion; one-step common-action test; finite obstruction trees; machine-checked in Lean 4). In continuous time it yields the common-action obstruction with a Farkas dual and a Helly-type bound on witness states, a delayed-information bound with a threshold form and a linear-programming instantiation, a finite-time exit certificate, and an oracle-recourse certificate for affine systems whose planar instance has an exact delay threshold. A certification layer gives the exact limits of observation-only verdicts (fibre criterion, certainly-safe set) and the certainty-equivalence trap. The gap between the certificates and the truth is located precisely: completeness holds in finite systems and in the static class, and no certificate pair that reads only the window sub-model can be complete.

**Fit.** The objects are set-valued throughout—beliefs as sets of compatible states, response correspondences, viability kernels, Dini derivatives, support functions, Farkas and Helly arguments—and the results delimit the reach of the set-valued estimation programme already published in this journal (Veliov 1993; Doyen 2000).

**Reproducibility.** All proofs are in the Supplementary Material; every numerical value is recomputed by an exact-arithmetic script (30 checks) distributed with the submission; the finite core is formalised in Lean 4 with its scope stated plainly.

The work is not under consideration elsewhere. An earlier edition is deposited as a preprint (Zenodo/figshare); large language models assisted with drafting and review, as declared in the manuscript, and I take full responsibility for the content.

Yours sincerely,

Amin Abaee
Independent Researcher — ORCID 0000-0002-0019-1842 — amin_abaee@ut.ac.ir
