# Does the line-level audit see a planted flaw?

Six defects planted in sentences taken from the 306 the audit cleared, one control left exactly as the
draft wrote it, both sets fed through `v48_reuse_audit_v1.py`. A flag counts only if it was not already on the
baseline run, so a row the audit happens to dislike for its own reasons cannot inflate the score.


| planted defect | row | expected | raised as a new flag | what the audit said |
|---|---|---|---|---|
| unit - a reserve figure moved off the value the deposit attaches the unit to | D0110 | `unit` | **yes** | unit: 1500000 kt is nowhere attached to that figure in the deposited article, so the reuse carries a number the truth source does not give it |
| ref - a pointer to a subsection the deposited article does not have | D0219 | `ref` | **yes** | ref: cites §2.9, absent from the deposited article’s numbering |
| name - a surname no source in the document carries | D0108 | `name` | **yes** | name: Zbarovski does not appear in the deposited article |
| status - a status label ('certified') on an object the deposit does not label so | D0357 | `status` | **yes** | status: the sentence says "certified" of this object; the deposit passage does not use that label here |
| universal - an 'every' generalising who the statement is for | D0004 | `universal` | **yes** | universal: "every" appears in the sentence and not in the passage behind it |
| voice - a first-person framing the deposited sentence does not carry | D0056 | `voice` | **yes** | voice: first person (we) where the sentence's own deposit sentence has none - the draft runs 0.3 instances per 1k words against the deposited article’s 0.1, so this is register, not error, unless the verb attached to it is stronger than the deposit’s |
| control, untouched | D0556 | nothing | clear | no new flags |

**Detection 6/6**, control clean. Every planted defect raised the check it was planted to trip, so the 296 cleared rows are a reading of the sentences and not the silence of a blind filter - for the six classes these checks claim to cover, which is what the row-level read in `v48_reuse_read.md` then stands on.
