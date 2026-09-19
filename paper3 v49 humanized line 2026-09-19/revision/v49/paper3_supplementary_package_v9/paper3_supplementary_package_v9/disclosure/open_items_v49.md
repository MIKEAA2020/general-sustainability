# Open items on the v49 line (2026-09-19)

1. **Two reference entries the swap left uncited** — `United Nations, 2014` (SEEA Central Framework) and
   `United Nations, 2025` (the 2025 SNA treatment of depletion). They were cited only in the §1 passage the
   adaptation does not carry, and that passage is erratum E4's material: it asserts more than the deposited
   article does. So the author's two coherent moves are (a) delete both entries, which retires E4 outright,
   or (b) keep them and restore the §1 passage, which reinstates a claim the ledger line added on its own
   authority. Neither was applied; `audit_v49_lines_v1.py` reports both entries until one is.
2. **The four §1 status labels** (`statistical index, not a stock ratio`, `arithmetic, not a forecast`,
   `pressure scale, not a depletion diagnostic`, `readouts of the ledger`): 1x each in v48, 0x in v49. The
   classifications survive in the adaptation's wording; whether the labels themselves should return is a
   content call, not a style one. `verify_v49_base.py → status_labels` prints the position plainly.
3. **Two `watch` terms** kept as the adaptation wrote them (`stock-depletion ratio`, `physical depletion
   forecast`, 1x each): the revert file reports them rather than applying a substitution, per the ruling.
4. **A slight doubling in §1.1**: the adaptation's bullet *"This is simply compensatory aggregation in
   disguise—a deficit in an unmonitored capital stock is mathematically masked by current consumption
   flows. We formalize this limitation as an aggregation obstruction in Section 10.1."* and the carried-over
   deposited sentence *"The first is arithmetic and is the compensatory-aggregation failure above — a deficit
   in one component offset by a surplus in another…"* state the same sense twice, because the ruling cut only
   the two-level labels and kept the deposited passage. If the author wants the deposited wording alone,
   deleting the adaptation's bullet is one line in `v49_carry_over.json`'s companion file.
5. **The adaptation's date** (*September 6, 2026*) vs this line's header (*September 17, 2026*): v49 keeps the
   header's. If the earlier date is the intended one, it is a one-token change in the .tex header, and the
   front matter no longer duplicates it either way.
6. **House-style bibliography**: the list still carries no DOI for Martinez-Alier, Munda & O'Neill (1998)
   while 8 entries carry one, and §1 cites that work as `O'Neill, 1998` — a three-author paper, copied from
   the deposited article, so this build left it alone.
