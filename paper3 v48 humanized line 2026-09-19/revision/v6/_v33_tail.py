REFS = [
    ("Aubin, J.-P., 1991.",
     "Ahuja, R.K., Magnanti, T.L., Orlin, J.B., 1993. Network Flows: Theory, Algorithms, and Applications. Prentice-Hall, Englewood Cliffs."),
    ("Blomqvist, L., Brook,",
     "Baez, J., Li, X., Libkind, S., Osgood, N.D., Patterson, E., 2023. Compositional modeling with stock and flow diagrams. In: Applied Category Theory 2022. Electronic Proceedings in Theoretical Computer Science 380, 77\u201396. https://doi.org/10.4204/EPTCS.380.5"),
    ("G\u00fcntner, A., Sharifi,",
     "Gale, D., 1957. A theorem on flows in networks. Pacific Journal of Mathematics 7, 1073\u20131082."),
    ("Redner, S., 2001.",
     "Prajna, S., Jadbabaie, A., 2004. Safety verification of hybrid systems using barrier certificates. In: Hybrid Systems: Computation and Control VII. Lecture Notes in Computer Science 2993, 477\u2013492.\n\nPrajna, S., Jadbabaie, A., Pappas, G.J., 2007. A framework for worst-case and stochastic safety verification using barrier certificates. IEEE Transactions on Automatic Control 52, 1415\u20131428."),
    ("Tapley, B.D., Bettadpur,",
     "Smith, H.L., 1995. Monotone Dynamical Systems: An Introduction to the Theory of Competitive and Cooperative Systems. Mathematical Surveys and Monographs 41. American Mathematical Society, Providence."),
]
for anchor, entry in REFS:
    _rep(anchor, entry + "\n\n" + anchor, "reference inserted before %r" % anchor[:22])

UN = ("United Nations, 2025. System of National Accounts 2025. United Nations Statistics Division, New York. Adopted by the United Nations Statistical Commission at its fifty-sixth session. https://unstats.un.org/unsd/nationalaccount/sna2025.asp\n\n"
      "United Nations, European Commission, International Monetary Fund, Organisation for Economic Co-operation and Development, World Bank, 2014. SEEA Central Framework: 2012 Technical Implementation. Statistical Papers, Series M No. 96. United Nations, New York.\n\n")
_rep("Wackernagel, M., Beyers, B., 2019.", UN + "Wackernagel, M., Beyers, B., 2019.",
     "references inserted: United Nations 2025, United Nations et al. 2014")

# ---- the numbering note of Section 3.1, extended to the new labels -----------------
_rep("runs on the single 1\u201320 sequence counter",
     "runs on the single 1\u201333 sequence counter", "numbering note: counter range")
_rep("not further members of the layering counter",
     "not further members of the layering counter; the statements added at this revision carry the consecutive labels Definitions 21\u201323, Theorem 24, Propositions 25\u201332 and Remark 33, so no label is repeated",
     "numbering note: extension at 21-33")

# ---- back matter -------------------------------------------------------------------
_rep("`paper3_supplementary_v8.md`", "`paper3_supplementary_v9.md`", "supplementary pointer: version")
_rep("the executed broad-cohort comparison (S5).",
     "the executed broad-cohort comparison (S5). At this revision it additionally carries the proof obligations attached to each entry of the certification state of Section 3.1 with the certificate vectors of the classified indicators (S7), the linear programmes of Definitions 21\u201322 and Theorem 24 with their input requirements and the reading rule for an infeasible programme (S8), and the worked exhibits of Sections 6.2, 6.5 and 10.1 with their reproduction record and the statement inventory extended to the new labels (S9).",
     "supplementary pointer: S7-S9")

CODE = ("## Code availability\n\n"
        "The scripts that generate every computed figure in this article \u2014 the persistence-index simulation of Section 6.5, the curvature and crossover arithmetic of Section 6.2, and the compensation-premium and worst-concealed-deficit linear programmes of Section 10.1 \u2014 are archived with the supplementary material, with the random seed and the library versions recorded in the archive manifest. The scripts read no data other than the public products named in the data availability statement.\n\n")
_rep("## Declaration of competing interest", CODE + "## Declaration of competing interest",
     "Code availability section")

os.makedirs(os.path.dirname(DST), exist_ok=True)
open(DST, "w", encoding="utf-8").write(t)
json.dump(log, open(LOG, "w", encoding="utf-8"), ensure_ascii=False)
print("applied %d, skipped %d, logged %d ops" % (len(applied), len(skipped), len(log)))
for a in applied:
    print("   OK   " + a)
for x in skipped:
    print("   SKIP " + x)
print("chars: %d | words: %d | lines: %d" % (len(t), len(t.split()), t.count("\n") + 1))
