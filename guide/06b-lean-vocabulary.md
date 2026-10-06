# 6b. Working dictionary: source-located, Lean-boundary edition

This is the rigorous companion to [Stage 3 of the plan](../Research-project-plan.md)
("Build a dictionary"), restricted to what can be checked against the pinned Lean
repository audited in [06](06-lean-boundary.md). **[07](07-dictionary.md) is the
cross-referenced beginner glossary; this file is narrower and stricter**: a term
is only called "formalized" here if an actual Lean declaration with that role
exists and is reachable from the chain audited there — not merely mentioned in
prose.

**Snapshot**: same pin as [06](06-lean-boundary.md) —
[`lana-agents/iut`](https://github.com/lana-agents/iut) at
[`d9465c111`](https://github.com/lana-agents/iut/tree/d9465c111ec4073709f67e9fccec7e3eb374a816)
(2026-10-03T19:53:47Z). All absence claims below are exhaustive, case-insensitive
`grep` results over the full pinned checkout (`Iut/`, `Iut4Sec1/`, `README.md`, and the
bundled paper excerpts under `references/`), re-run directly for this file, not
recalled from an earlier pass.

## Graduate-level walkthrough (intuition only)

A program can formalize a **numerical shadow** of an object without
building the object. `QPilotData.lhs` computes a real-valued expression;
it does not construct the paper's Frobenioid-theoretic $q$-pilot.
Likewise, the pinned repo has a local, single-theater `logShell`
construction with proved properties, but no formal inter-theater
log-link. A field called `thetaPilot` is input data, not a Lean
implementation of the horizontal $\Theta$-link.

For each row below, check the declaration, its hypotheses, and where
it is used; then ask whether the *paper's* corresponding object is
actually constructed. A failed name search is scoped to this
**pinned checkout**, not proof that no one can formalize the term.
Conversely, a matching declaration name is not a fidelity proof.

**Background, not a proof-status upgrade:**
[the elementary dictionary](07-dictionary.md),
[the pinned dependency audit](06a-lean-dependencies.md),
and [the Lean 4 textbook](https://lean-lang.org/theorem_proving_in_lean4/).

## How to read the table

| Status tag | Meaning |
| --- | --- |
| `FORMALIZED` | A real Lean declaration fills this role; at least part of it is a proved theorem, not only a hypothesis. |
| `NOT FORMALIZED (reference-text only)` | The term appears **only** inside the verbatim paper excerpts bundled under `references/*.txt` — never in a `.lean` file, never in `README.md`'s own description of what the project models. |
| `NOT FOUND` | The term does not appear anywhere in the pinned repository, including the bundled reference excerpts. |
| `EXPLICITLY NOT CONSTRUCTED` | The project's own docstring states in so many words that this notion is out of scope / not built here. |

Per [00-map.md](00-map.md)'s evidence labels: every "Purpose" cell describing literature
meaning (not this repo's content) is `ASSERTED_IN_IUT`/`SECONDARY`, sourced from the
bundled excerpts or general IUT literature, not independently re-derived here against
Mochizuki's full original papers (only IUT IV is bundled — see log-link/log-theta-lattice
rows). Any claim that a Lean definition is *faithful* to the paper's definition is
`UNVERIFIED` unless stated otherwise — I checked that the named Lean object exists and
is cited to a precise proposition number by the project's own docstring, not that the
transcription is correct against the original text.

## The five requested terms, plus one bonus (Frobenioid)

| Term | Status | Source location | Purpose | Not licensed to infer |
| --- | --- | --- | --- | --- |
| **Hodge theater** (Θ^±ellNF-Hodge theater / Θ^±ell-Hodge theater) | `NOT FORMALIZED (reference-text only)` | Only in [`references/iut4.txt:10,18,50,59,196,199-200,277`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/references/iut4.txt#L10) and `references/iut4-section1.txt:1613-1616` — verbatim plain-text copies of Mochizuki's IUT IV paper bundled for citation. **Zero** matches in any `.lean` file or in `README.md`. | (Literature only) Names the basic "arithmetic holomorphic structure" gadget; the log-theta-lattice relates distant copies of it. | That `Iut.InitialThetaData`, `Iut.LocalTheory`, `Iut.LargeVolumeContainerData`, or any other structure in this repository *is*, formalizes, or stands in for a Hodge theater. Nothing in the repo defines, names, or type-checks anything called a theater. |
| **theta-link (Θ-link)** | `NOT FOUND` | No occurrence anywhere — not in `Iut/`, `Iut4Sec1/`, `README.md` (checked the spelled-out form and the Unicode "Θ-link"/"ΘLink" forms), **and not even in the bundled `references/` excerpts**, since the repo carries only IUT IV material and no IUT III excerpt (the Θ-link's home paper). | (Literature only) The horizontal, non-ring/scheme-theoretic gluing isomorphism of IUT III relating the Θ-pilot object across a horizontal arrow of the log-theta-lattice. | That `Iut/Cor312/RightHandSide.lean`'s `thetaPilot`/`thetaPilot_le_shell` field (the project's own "theta-pilot" input, taxis #35) formalizes or substitutes for the Θ-link. `thetaPilot` is an opaque **input hypothesis field** supplied as data (see [06](06-lean-boundary.md) §6.2.1, node 0's "not licensed to infer" caveat), not a constructed gluing map — the repository never claims otherwise. |
| **log-link** | `NOT FORMALIZED (reference-text only)` | Only in [`references/iut4.txt:344,2984,2994,4191,4197,4322`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/references/iut4.txt#L344). **Zero** matches in `Iut/`, `Iut4Sec1/`, or `README.md`. | (Literature only) The vertical arrow of the log-theta-lattice, built from the `p`-adic logarithm, passing between adjacent theaters. | That this repo's real `p`-adic-logarithm construction ([`Iut/Concrete/LocalConstruct/PadicLog.lean`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Concrete/LocalConstruct/PadicLog.lean), feeding `LogShell.lean`) is, builds, or uses the log-link. It is a **single-theater, single-copy** local computation establishing one theater's own log-shell — not an inter-theater gluing isomorphism. No declaration anywhere in the repository is named or documented as a/the log-link. |
| **log-shell** | `FORMALIZED` (partial — single-theater, mono-analytic layer only) | Interface: [`Iut/Cor312/Container.lean:79-119`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Cor312/Container.lean#L79-L119) (`LargeVolumeContainerData.logShell` + 4 sibling proof-obligation fields, taxis #43). Concrete construction + **proved** theorems: [`Iut/Concrete/LocalConstruct/LogShell.lean:10-50`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Concrete/LocalConstruct/LogShell.lean#L10-L50) (module docstring, taxis #4/#278), with e.g. automorphism-invariance `RingHom.image_logShell_subset` at [`:104`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Concrete/LocalConstruct/LogShell.lean#L104) and `algEquiv_image_factorLogShell_subset` at [`:226`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Concrete/LocalConstruct/LogShell.lean#L226). Concrete instantiation: [`Iut/Concrete/Container.lean:139-144`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Concrete/Container.lean#L139-L144). Discussed in [`README.md:219-222`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/README.md#L219-L222). | Names the mono-analytic, compact, (at nonarchimedean places) order-containing region attached to each place of each tensor-packet (claimed: IUT III, Props. 3.1–3.3, 3.9; IUT IV, Prop. 1.2/1.5); bounds the theta-pilot input in the Corollary 3.12 variant (taxis #33/#35). Its invariance under the indeterminacy automorphisms is a **genuinely proved** Lean theorem, not an assumed hypothesis. | That this formalizes "the log-shell as used in the log-theta-lattice" in general. It is explicitly scoped, by its own module docstring, to **one theater's** mono-analytic/local-field layer only — it does not construct, reference, or depend on the log-link (which would relate one theater's log-shell to another's), the log-theta-lattice, or any Frobenioid-theoretic/multiradial algorithm. `Container.lean`'s own docstring: *"nothing asserts that a theta-pilot image lies in the container, and no multiradial algorithm is constructed."* Fidelity of the Lean definition to IUT I, Definition 5.4.5 / IUT III, Proposition 3.2 is `UNVERIFIED` by me against the original papers (only IUT IV is bundled in `references/`) — I confirmed the Lean kernel accepts the stated proofs and that the project's own docstring cites those exact proposition numbers, not that the transcription is correct. |
| **log-theta-lattice** | `NOT FORMALIZED (reference-text only)` | Only in `references/iut4.txt` (26 occurrences, e.g. lines 13, 19, 25, 33, 48, 60, 186, 195, 265, 277, 288, 297, 302, 333, 2952, 4196–4314, 4436). **Zero** matches in `Iut/`, `Iut4Sec1/`, or `README.md`. | (Literature only) The two-dimensional diagram of theaters linked by log-links (vertical) and theta-links (horizontal) — IUT's central inter-universal comparison device; IUT IV Theorem 1.10 is, in the literature, extracted by walking it. | That the Lean implication chain audited in [06](06-lean-boundary.md) §6.2.1 (`Corollary312Variant → theorem110 → c2 → … → ClassicalABC`) formalizes, or traverses, the log-theta-lattice. It is an ordinary one-directional sequence of `Prop`-to-`Prop` Lean implications over a **single, static** bundle of input data (`Corollary312VariantData`) — no multiple theater copies, no indeterminacy groups, no horizontal/vertical arrow structure of any kind. "Corollary 3.12 variant" names only the project's own stipulated inequality (taxis #33), not a construction of, or argument over, the lattice the published Corollary 3.12 actually depends on. |
| **Frobenioid** *(bonus — named in the plan's own Stage 3 example table)* | `EXPLICITLY NOT CONSTRUCTED` | [`Iut/Cor312/LeftHandSide.lean:40`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Cor312/LeftHandSide.lean#L40) (docstring): *"The `q`-pilot_object_ of IUT III (a Frobenioid-theoretic gadget) is not constructed; this module computes only its log-volume side…"* This is the **only** occurrence of the word anywhere in `Iut/`/`Iut4Sec1/`. | (Literature only) The category-with-Frobenius-and-divisor-monoid structure through which IUT's multiradial algorithms transport arithmetic holomorphic structures between theaters; the published Cor. 3.12's `q`-pilot/Θ-pilot are Frobenioid-theoretic objects. | That `QPilotData`/`QPilotData.lhs` ([`Iut/Cor312/LeftHandSide.lean`](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Cor312/LeftHandSide.lean)) is, represents, or carries the categorical structure of a Frobenioid. It is a **real number** ($`-\lvert\log(q)\rvert`$) computed from admissible prime data — a numerical shadow the project's own docstring explicitly distinguishes from "the object itself." |

## Reading this table honestly

Five of these six terms are **absent from the Lean source**: they exist in this
repository only as words in a bundled, verbatim plain-text copy of IUT IV (or, for
theta-link, nowhere at all — not even there). This is not a defect the project hides:
its own `README.md` and docstrings never claim to construct a Hodge theater, a
theta-link, a log-link, or a log-theta-lattice, and the one `Frobenioid` mention is a
self-reported scope exclusion. **`log-shell` is the sole exception** — a real,
partially-proved Lean formalization exists, but strictly for one theater's local,
mono-analytic layer, not for its role gluing distinct theaters together across the
lattice. Do not let the familiarity of these names suggest broader coverage than the
table above states. Cross-check against [06](06-lean-boundary.md) §6.2.1 for how
`log-shell` feeds the audited proof chain (and §6.5 there for the status of fuller
evidence-label documentation), and against [07](07-dictionary.md) for plain-language
orientation on the terms this file marks absent.
