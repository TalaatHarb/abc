# 8. Research queue: turn the ten stages into checkable work

The [original plan](../Research-project-plan.md) proposes stages 0–10.
This queue makes the *prerequisites* and the *exit tests* explicit. "Started"
means a reader guide exists; it never means the corresponding mathematical
claim is proved. Work on independent rows may proceed in parallel, but their
results must meet the shared evidence rules in [00](00-map.md).

| Stage | Output and immediate task | Depends on | Exit test |
| --- | --- | --- | --- |
| 0 — target | [01](01-abc-target.md): exact quantifiers, radical, examples | None | Reader can reproduce both directions of the finite-exception equivalence |
| 1 — claim graph | A node-and-arrow ledger for abc, IUT III, IUT IV | Stage 0; primary PDFs | Every arrow has a theorem locator, hypotheses, and an explicit status |
| 2 — prerequisites | [02](02-prerequisites.md): shortest useful study route | Stage 0 | Reader can perform the three calculations and identify deferred subjects |
| 3 — dictionary | Source-located entries for each IUT-specific object | Stages 1–2 | Every entry states allowed maps and what cannot yet be compared |
| 4 — IUT I | Minimal trace: input data, theaters, and inter-theater links | Stages 1–3 | Explain one concrete job of each construction using IUT I's own definitions |
| 5 — IUT II | Trace a quantity from input to asserted estimate | Stage 4 | State the quantity, normalization, theorem, and its downstream consumer |
| 6 — IUT III | Theorem 3.11 → Corollary 3.12: list each premise and comparison | Stages 4–5; primary IUT III | Independent expert can check each comparison or point to the exact gap |
| 7 — dispute | Separate Scholze–Stix objection from Mochizuki's answer | Stage 6; both sides' primary texts | Each disputed arrow has both interpretations and a testable obligation |
| 8 — IUT IV and Lean | Audit downstream implications and exact Lean assumptions | Stages 0–1; IUT IV; pinned Lean snapshot | Trace a formal declaration to abc without assuming its unproved input |
| 9 — adversarial review | Independent explainer, critic, and formalizer test one arrow | Stages 6–8 | Record a concrete correction, missing premise, or reviewed proof, not a vote |
| 10 — exposition | Connected reader guide and diagrams from checked edges | Stages 0–9 | Each explanation links back to the exact node, arrow, source, and remaining gaps |

## Next bounded investigations

1. Extract the full hypotheses and conclusion of **IUT III Theorem 3.11**
   and **Corollary 3.12**, including the names of any indeterminacies,
   reconstruction procedures, and comparison domains. Do not substitute
   a prose summary for the statements.
2. For each claimed path through IUT IV, record theorem/section/page,
   whether an inequality is for heights, conductors, log-volumes, or a
   different quantity, and the *rule converting* one to another.
3. Pin a Lean repository commit; inspect theorem types and use the project's
   own tools to list axioms/dependencies where possible. Record how the
   mathematical statement is translated, not only that Lean accepts code.
4. Give the disagreement to two human experts in its strongest source-linked
   formulations; ask each to identify the first arrow they would accept or
   reject. Do not turn differing verdicts into an invented consensus.

For every investigation, capture: `node ID | source URL and PDF page/section
or code SHA/lines | exact hypotheses | mathematical operation | claimed
conclusion | objection if any | verification performed | unresolved item`.
PDF page numbers and printed page numbers can differ; record which is used.
Prioritize **stage 6**, then **stages 7 and 8**, before producing a polished
"IUT in 20 diagrams." A diagram is a deliverable only after its edges can be
audited.
