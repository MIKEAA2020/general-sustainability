#!/usr/bin/env python3
"""v29o: say what the two intervals are evidence for.

The abstract carried the profile range [67.9, 95.2] and the bootstrap interval
side by side without saying why they differ by a factor of eight, which one
supports the paper's claim, or that the tight one is not a precision statement.
A referee who resamples gets [-89.4, 125.7] and finds the tight range
unreconciled with it. Three edits:

O1  abstract: tie each interval to the question it answers, and disclaim
    precision for the tight one;
O2  Section 3.10: explain the disagreement -- what each conditions on, the two
    separable reasons for the width, and that the gap survives removing the
    degenerate refits;
O3  the profile cut is named as the F-based interval it is, so the two are not
    read as rival estimates of one thing.
"""
import io
import shutil

TEX = "/home/user/fam/e2/paperE2_cod_intervention_v29.tex"
shutil.copy(TEX, "/tmp/v29n_before_intervals.tex")
tex = io.open(TEX, encoding="utf-8").read()
log = []


def sub1(tag, old, new):
    global tex
    n = tex.count(old)
    assert n == 1, "%s: anchor matched %d times, need exactly 1" % (tag, n)
    tex = tex.replace(old, new, 1)
    log.append(tag)


# ---------------------------------------------------------------- O1
sub1("O1 the abstract says what each interval is evidence for",
     "set \\(C^*\\) lies in \\([67.9, 95.2]\\) kt, and under joint resampling the bound has median\n"
     "\\(73.7\\) kt with \\(90\\%\\) interval \\([-89.4, 125.7]\\), or \\(88.1\\) kt\n"
     "(\\([-5.6, 130.6]\\)) restricted to the expansive regime on which the results are\n"
     "conditional (\\(73\\%\\) of replicates); 20-year survival from",
     "set \\(C^*\\) lies in \\([67.9, 95.2]\\) kt --- pinned to within\n"
     "\\(27\\) kt while \\(K\\) itself is not identified from above ---\n"
     "whereas resampling the \\(24\\) transitions and refitting both\n"
     "parameters freely disperses the estimate over a far wider range\n"
     "(median \\(73.7\\) kt, \\(90\\%\\) interval \\([-89.4, 125.7]\\), or\n"
     "\\([-5.6, 130.6]\\) restricted to the expansive regime on which the\n"
     "results are conditional, \\(73\\%\\) of replicates). The two answer\n"
     "different questions and the tight one is an identification result, not a\n"
     "precision one; 20-year survival from")

# ---------------------------------------------------------------- O2
sub1("O2 Section 3.10 explains the disagreement",
     "\\(90\\%\\) interval \\([1.030, 1.178]\\): expansion holds throughout.\n",
     "\\(90\\%\\) interval \\([1.030, 1.178]\\): expansion holds throughout.\n"
     "\n"
     "Two intervals for one quantity, a factor of eight apart in width, need\n"
     "the difference said out loud rather than left for a reader to reconcile.\n"
     "The profile range of Section 3.7 is an \\(F\\)-based interval: it holds\n"
     "the fit inside the \\(95\\%\\) likelihood cut, lets \\(K\\) run the whole\n"
     "ridge from \\(1500\\) to \\(50{,}000\\) kt with \\(r\\) reprofiled at each\n"
     "step, and asks how far \\(C^*\\) can move. It answers an identification\n"
     "question --- is the functional pinned, given the model --- and the answer\n"
     "is yes, to within \\(27\\) kt, even though \\(K\\) is not identified at\n"
     "all. The bootstrap answers a different question: how far the estimate\n"
     "itself moves when the \\(24\\) transitions are resampled and both\n"
     "parameters are refitted freely. It is wider for two separable reasons.\n"
     "Its lower tail comes from replicates in which the refit places \\(K\\)\n"
     "below the reference point (\\(7.4\\%\\) of them) --- admissible under the\n"
     "declared box, excluded by construction when \\(K\\) is held fixed, and\n"
     "not admissible as a description of a limit reference point. Removing\n"
     "those and every replicate outside the expansive regime still leaves\n"
     "\\([-5.6, 130.6]\\) kt, so the width is not an artefact of degenerate\n"
     "refits: the bootstrap is wider at both ends, \\(35\\) kt above the profile\n"
     "ceiling and \\(74\\) kt below its floor. What remains is small-sample:\n"
     "with \\(24\\) transitions the resampling dispersion of a two-parameter\n"
     "refit exceeds what an \\(F\\)-based cut implies, and the profile range\n"
     "should not be read as a statement of precision. Neither interval is in\n"
     "error. They are evidence for different claims, and the claim this paper\n"
     "makes is the identification one.\n")

io.open(TEX, "w", encoding="utf-8").write(tex)
print("\n".join("  " + x for x in log))
print("lines: %d" % tex.count("\n"))
