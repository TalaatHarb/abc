# An auditable guide to the abc conjecture and IUT

This repository turns the [original research plan](Research-project-plan.md) into
a reading path. Its subject is Mochizuki's *published, contested claim* to prove
abc using inter-universal Teichmüller theory (IUT). It is **not** a new proof,
an endorsement of the disputed inference, or a claim that publication or a
Lean formalization has settled the dispute.

**Start here:** [Project map and evidence rules](guide/00-map.md) →
[The abc target](guide/01-abc-target.md) →
[Prerequisite route](guide/02-prerequisites.md). A reader already comfortable
with heights, valuations, and elliptic curves can start at the project map.

## What is available

| File | What the reader gets |
| --- | --- |
| [Project map](guide/00-map.md) | The questions, dependency directions, and evidence labels |
| [The abc target](guide/01-abc-target.md) | Definitions, worked examples, an elementary equivalence proof, and the conditional Szpiro bridge |
| [Prerequisite route](guide/02-prerequisites.md) | A selective study path with exercises and stopping points |
| [Polynomial abc lab](guide/02a-polynomial-abc.md) | An optional, complete proof of an instructive analogy, not of abc over integers |
| [Research queue](guide/08-work-queue.md) | The ten stages from the plan reorganized into verifiable tasks and review gates |
| [Source register](guide/sources.md) | Checked references, pending audits, and a citation policy |
| [Original plan](Research-project-plan.md) | The motivating proposal; its citations and claims require independent checking |

The IUT claim graph, the competing interpretations of its critical step, and
the scope of the Lean work are separate source-audit tracks. They must not be
silently filled in by inference from the plan's diagram.

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
