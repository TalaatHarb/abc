# An auditable guide to the abc conjecture and IUT

This repository turns the [original research plan](Research-project-plan.md) into
a reading path. Its subject is Mochizuki's *published, contested claim* to prove
abc using inter-universal Teichmüller theory (IUT). It is **not** a new proof,
an endorsement of the disputed inference, or a claim that publication or a
Lean formalization has settled the dispute.

**Start here:** [Project map and evidence rules](guide/00-map.md) →
[The abc target](guide/01-abc-target.md) →
[Prerequisite route](guide/02-prerequisites.md) →
[IUT source route](guide/03-iut-route.md) →
[Claim dependencies](guide/04-claim-dependencies.md) →
[The contested step](guide/05-critical-transition.md) →
[Lean's boundary](guide/06-lean-boundary.md). A reader already comfortable
with heights, valuations, and elliptic curves can skip the prerequisite
route, but should not skip the source or dispute status labels.

## What is available

| File | What the reader gets |
| --- | --- |
| [Project map](guide/00-map.md) | The questions, dependency directions, and evidence labels |
| [The abc target](guide/01-abc-target.md) | Definitions, worked examples, an elementary equivalence proof, and the conditional Szpiro bridge |
| [Prerequisite route](guide/02-prerequisites.md) | A selective study path with exercises and stopping points |
| [Polynomial abc lab](guide/02a-polynomial-abc.md) | An optional, complete proof of an instructive analogy, not of abc over integers |
| [IUT source route](guide/03-iut-route.md) | A source-located first pass through the published claim and its limits |
| [Claim dependencies](guide/04-claim-dependencies.md) | Paper-side nodes and arrows to verify, not an established proof graph |
| [The contested step](guide/05-critical-transition.md) | Side-by-side primary-source accounts of the IUT III disagreement, without a verdict |
| [Lean boundary](guide/06-lean-boundary.md) | A pinned, *conditional* formalization audit, including the unproved input |
| [Lean dependency ledger](guide/06a-lean-dependencies.md) | Pinned theorem edges, assumptions, build evidence, and explicit unaudited dependencies |
| [Lean vocabulary](guide/06b-lean-vocabulary.md) | Typed counterparts for a few terms, not authoritative IUT definitions |
| [Working dictionary](guide/07-dictionary.md) | Standard definitions, comparison cautions, and IUT-specific reading questions |
| [Research queue](guide/08-work-queue.md) | The ten stages from the plan reorganized into verifiable tasks and review gates |
| [Source register](guide/sources.md) | Checked references, pending audits, and a citation policy |
| [Original plan](Research-project-plan.md) | The motivating proposal; its citations and claims require independent checking |

The IUT claim graph, the competing interpretations of its critical step, and
the scope of the Lean work are separate source-audit tracks. Their current
guides are **first passes**, not proof-level verification of every edge.
In particular, do not fill an unresolved arrow from the original plan's
diagram.

## How to use this repository

Read a mathematical statement together with its **source locator**, **logical
status**, and **remaining obligation**. A published proposition, a derivation
we can reproduce, and a Lean theorem conditional on a proposition are three
different kinds of evidence. In particular, a checked implication
`Corollary 3.12 variant -> abc` does not check Corollary 3.12 itself.

The goal is a sequence of explanations that a mathematician can challenge at
a specific arrow, not a simplified story that hides the arrow. Text here is
original commentary and links to the source material, not a copy of the
papers. Snapshot of this reading path: **2026-10-05**.
