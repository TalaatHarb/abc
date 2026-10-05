# 6. Lean-boundary audit: what `lana-agents/iut` actually traces and proves

**Scope of this file.** This is the LEAN-audit strand's primary deliverable
(restored here after a misrouted instruction briefly split it into
`03-iut-route.md` / `04-claim-dependencies.md` / `03a-dictionary.md`; those
path names are a **different** strand's namespace — see the restoration
note in §6.5). It answers one question only: **for the pinned snapshot
below, what route does `lana-agents/iut` actually trace from a "Corollary
3.12 variant" to the classical ABC conjecture, which declarations realize
each step, where are the real citations, and what remains unproved?** It
does not evaluate whether Mochizuki's published Corollary 3.12 is true, and
it does not evaluate the Scholze–Stix dispute (those are covered by the
primary-IUT-papers strand's own files, which use the `03`/`04` numbering —
not this file). Every claim below was checked directly against the actual
pinned source, building on the framework and evidence labels defined in
[00-map.md](00-map.md).

**Headline, stated the way the repository itself states it**: this project
formalizes a *stipulated variant* of IUT III, Corollary 3.12 as an unproved
`Prop`, and proves — with the Lean kernel, modulo the caveats cataloged in
§6.5 below — that *if* that `Prop` holds, the classical ABC conjecture
follows. **It does not verify IUT I–IV, it does not prove the Corollary
3.12 variant, and it does not prove the published Corollary 3.12.** Nothing
in this file should be read as asserting otherwise.

---

## 6.1 Snapshot pinned

| Field | Value |
| --- | --- |
| Repository | [`lana-agents/iut`](https://github.com/lana-agents/iut) — "Inter-universal Teichmüller theory: the ABC/IUT trunk." (GitHub API `description` field) |
| Pinned commit | `d9465c111ec4073709f67e9fccec7e3eb374a816` |
| Commit timestamp | `2026-10-03T19:53:47Z` (author/commit date; `pushed_at` on the repo is `2026-10-03T19:53:48Z`) |
| Commit subject | "README: the variant implies classical ABC for the genuine étale and model-based tempered theories (`classicalABC_of_variant_genuine'`, `canLift27` a theorem); boundary: André identification assumes W10" |
| Commit author | Christian Merten `<lana@merten.dev>`, co-authored-by "Claude Opus 5.5 (1M context)" — i.e. this is an AI-agent-assisted formalization project (consistent with the `lana-agents` org name), a relevant fact when deciding how much independent scrutiny to apply |
| License | Apache License 2.0 (`LICENSE` file; confirmed also via GitHub API `license.spdx_id = "apache-2.0"`) |
| Repo stats at audit time | 1 star, 0 forks, `open_issues_count: 0`, `archived: false`, created `2026-07-20T02:17:43Z` |
| Audit performed | 2026-10-05, against the commit above (two days after it was pushed; no later commit was consulted) |
| Methodology | Shallow `git clone` of the pinned commit, direct `grep`/file reads of the checkout, GitHub REST/Checks API calls (`api.github.com`) pinned to the same SHA, and zip-archive snapshots of four external Lake dependencies at their own pinned SHAs. **I did not execute a from-scratch `lake build` myself** (infeasible in task time: Mathlib `v4.32.0` + 7 custom dependencies); claims of successful elaboration rest on (a) GitHub's own hosted CI run for this exact commit (previously detailed in §6.5's lost companion file — see that section) and (b) my own reproducible `grep`, not on my re-running the build. |
| Discrepancy check | **No discrepancy found.** The repository exists at the stated location, is public, and the plan's named declarations (`Theorem110`, `Corollary22`, `Corollary23`, `ClassicalABC`) all exist, in the files the plan implies. The correction below is about the plan's chain being a **simplification** (it omits real branching and real external dependencies), not about any claim in the plan being falsified by the repo. |

All permalinks below use this exact SHA. If you are reading this after upstream
has advanced past this commit, re-clone and re-run the `grep`s in §6.6 against
your own checkout, and treat any mismatch as upstream drift, not an error in
this file.

---

## 6.2 The corrected dependency chain

The plan (`Research-project-plan.md`, Stage 8) states the chain as a single
line: `Iut.cor312Variant → Theorem110 → Corollary22 → Corollary23 →
ClassicalABC`. Every name in that line does correspond to something real, but
the plan compresses **two different routes that merge, one real theorem that
closes a gap the plan doesn't mention, and a second instantiation step
(abstract height theory → literal classical ABC) that is not just "Corollary23
→ ClassicalABC"**. The corrected shape:

```text
Iut.Corollary312Variant  (Prop; UNVERIFIED — no proof exists or is claimed)
        │  (h312 : the Prop above, as a hypothesis)
        ▼
Iut.Theorem110Invariants.theorem110        -- IUT IV, Theorem 1.10
        │
        ▼
Iut.Corollary22Inputs.c2                   -- Corollary 2.2(ii)
        │
   ┌────┴─────────────────────────────────────────────┐
   ▼ (abstract T : Genl.HeightTheory)                  ▼ (concrete tripod T = ℙ¹∖{0,1,∞})
Iut.cor312Variant_implies_abc              Iut.Tripod.abc_of_variant
   → Iut.ABC T  (:= T.StatementI,                → tripodTheory.StatementII
      delegates to external `genl`)                      │
                                              Iut.Tripod.statementI_of_statementII   -- REAL theorem,
                                                           │                             closes the gap,
                                                           ▼                             uses external `genl`
                                                   tripodTheory.StatementI
                                                           │
                                        Iut.Tripod.classicalABC_of_variant_of_statementII_imp_I
                                           (packaged, gap pre-closed, as
                                            Iut.Tripod.classicalABC_of_variant)
                                                           │
                                    ┌──────────────────────┴───────────────────────┐
                                    ▼ (abstract Pi1/Tp)                            ▼ (genuine model instantiation)
                         [ends here: ClassicalABC conditional       Iut.Tripod.classicalABC_of_variant_genuine
                          on an abstract interface pair,                (needs h27 : AffOrbicurve.CanLift27)
                          not yet the literal classical statement               │
                          unless Pi1/Tp are instantiated]            Iut.Anabelian.canLift27  -- REAL theorem
                                                                       (from orbicurve-cores + pi1)
                                                                                  │
                                                                                  ▼
                                                                Iut.Tripod.classicalABC_of_variant_genuine'
                                                                   (only remaining hypothesis: h312)
                                                                                  │
                                                                                  ▼
                                                                          Iut.ClassicalABC
                                                              (Masser–Oesterlé, literal classical form)
```

The two branches both terminate logically in `ClassicalABC`-shaped statements,
but only the **right-hand ("genuine") branch** ends at the actual
`Iut.ClassicalABC : Prop` (literal statement about coprime naturals/integers)
with **no remaining hypothesis besides `h312`**. The left-hand ("abstract")
branch proves `Iut.ABC T` for an arbitrary height formalism `T`, which is a
different (more general, interface-relative) proposition — it only becomes the
classical statement once instantiated at the concrete tripod height theory,
which is exactly what the right-hand branch does.

### 6.2.1 Node-by-node table (every citation is to the pinned SHA above)

| # | Declaration (fully qualified) | What it states | File : lines | Permalink |
|---|---|---|---|---|
| 0 | `Iut.Corollary312Variant` | `Prop`-valued def: `X.qPilot.lhs ≤ X.rhsData.rhs` (the "variant" inequality). Docstring (two independent occurrences — module-level and declaration-level): "deliberately left without proof and without axioms: no declaration in this repository proves, assumes, or axiomatizes it." | `Iut/Cor312/Statement.lean:78-91` (declaration + its docstring); module-level docstring `:27-37`; non-identification notice `:39-52`; `structure Corollary312VariantData` `:63-74` | [def+docstring](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Cor312/Statement.lean#L78-L91) · [non-identification](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Cor312/Statement.lean#L39-L52) |
| 1 | `Iut.Theorem110Invariants.theorem110` | IUT IV, Theorem 1.10 numeric inequality. Docstring: "The only IUT I–III input is `h312 : Corollary312Variant X`." | `Iut/Implication/Theorem110.lean:227-238` | [link](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Implication/Theorem110.lean#L227-L238) |
| 2 | `Iut.Corollary22Inputs.c2` | Corollary 2.2(ii): the log-volume inequality outside an exceptional set, above a threshold. | `Iut/Implication/Corollary22.lean:383-394` | [link](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Implication/Corollary22.lean#L383-L394) |
| 3a | `Iut.cor312Variant_implies_abc` / `…_abc'` | Abstract route: Corollary 2.3 = "[GenEll] Thm 2.1(i)" for **any** height formalism `T : Genl.HeightTheory` with a proof package. Concludes `Iut.ABC T`, **not** `ClassicalABC` directly. | `Iut/Implication/Corollary23.lean:114-125` / `:127-134` | [link](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Implication/Corollary23.lean#L114-L134) |
| 3b | `Iut.Tripod.abc_of_variant` | Concrete tripod route: same `h312` hypothesis shape, concludes `tripodTheory.StatementII` (ABC inequality on *compactly bounded subsets* only). | `Iut/Tripod/Main.lean:128-133` | [link](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/Main.lean#L128-L133) |
| 4 | `Iut.Tripod.statementI_of_statementII` | **Real, unconditional theorem** (not a hypothesis/placeholder): `StatementII → StatementI`, i.e. closes the "compactly bounded subsets" → "all points of bounded degree" gap, via noncritical Belyi maps. Proof calls the external `Genl.Curves.statementII_implies_statementI`. | `Iut/Tripod/GeneralPosition.lean:264-271` | [link](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/GeneralPosition.lean#L264-L271) |
| 5 | `Iut.Tripod.classicalABC_of_variant_of_statementII_imp_I` | `h312` + `(StatementII → StatementI)` as an explicit hypothesis ⟹ `ClassicalABC`. Docstring explicitly flags that `StatementII` *alone* does **not** suffice (archimedean-place counterexample sketched in the docstring itself). | `Iut/Tripod/ClassicalAbc.lean:294-314` | [link](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/ClassicalAbc.lean#L294-L314) |
| 6 | `Iut.Tripod.classicalABC_of_variant` | Same, with node 4 plugged in so the `StatementII → StatementI` hypothesis disappears. Universally quantified over abstract `Pi1 : EtalePi1Theory`, `Tp : TemperedPi1Theory Pi1`. | `Iut/Tripod/ClassicalAbcOfVariant.lean:26-36` | [link](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/ClassicalAbcOfVariant.lean#L26-L36) |
| 7 | `Iut.Tripod.classicalABC_of_variant_genuine` | Node 6 instantiated at the "genuine" étale/tempered theories (`genuinePi1Theory`, `temperedTheory ∘ genuineEtaleData`) over actual model orbicurves, given `h27 : AffOrbicurve.CanLift27`. | `Iut/Tripod/ClassicalAbcGenuine.lean:27-36` | [link](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/ClassicalAbcGenuine.lean#L27-L36) |
| 8 | `Iut.Anabelian.canLift27` | **Real theorem** (not an axiom): `[CanLift], Prop. 2.7`, built from `OrbicurveCores.U2.canLift27C` (external `orbicurve-cores`) transported over ℂ → all of char. 0 by the Lefschetz principle (`AffOrbicurve.canLift27_of_complex`, external `pi1`). | `Iut/Tripod/ClassicalAbcGenuineCanLift.lean:26-29` | [link](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/ClassicalAbcGenuineCanLift.lean#L26-L29) |
| 9 | `Iut.Tripod.classicalABC_of_variant_genuine'` | Node 7 with node 8 plugged in. **The only remaining hypothesis is `h312`** (quantified over the genuine model's Θ-data). Concludes `ClassicalABC`. | `Iut/Tripod/ClassicalAbcGenuineCanLift.lean:37-46` | [link](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Tripod/ClassicalAbcGenuineCanLift.lean#L37-L46) |
| 10 | `Iut.ClassicalABC` / `Iut.ClassicalABCInt` | The literal Masser–Oesterlé statement over `ℕ` / symmetric over `ℤ`; proved equivalent (`classicalABC_iff_int`). This is a faithful, unconditional, textbook statement — no fidelity concerns at this end of the chain. | `Iut/Abc/Classical.lean:34-48` (both defs), `:145-147` (equivalence) | [link](https://github.com/lana-agents/iut/blob/d9465c111ec4073709f67e9fccec7e3eb374a816/Iut/Abc/Classical.lean#L34-L48) |

Every arrow above is `CONDITIONAL_FORMALIZATION` pending its named
hypotheses; node 0 is `UNVERIFIED` by design; node 10 alone is `STANDARD`.
Source tag for all: `CODE_SHA` (`d9465c111`). **See §6.5 immediately below
for the status of the fuller per-edge evidence ledger, CI evidence,
dependency-surface audit, and explicit remaining-proof-obligations list that
previously accompanied this table.**

---

## 6.3 Correction log against `Research-project-plan.md`

| Plan claim (Stage 8) | Status after audit | Correction |
| --- | --- | --- |
| `Iut.cor312Variant → Theorem110 → Corollary22 → Corollary23 → ClassicalABC` is "exactly the dependency chain" | **Names all real; chain incomplete** | Real chain branches after `Corollary23` (abstract `Genl.HeightTheory` route vs. concrete `Tripod` route) and only the `Tripod` branch reaches literal `ClassicalABC`, via 6 further named theorems not mentioned in the plan (§6.2.1, nodes 3b–9), including one genuine un-placeholdered theorem that closes a real gap (`statementI_of_statementII`, node 4) and one that discharges `CanLift27` (`canLift27`, node 8). |
| "LANA itself says this does not verify IUT" | **Confirmed, independently** | Matches the repository's own framing exactly; I found no basis to weaken or strengthen this statement. |
| "its 2026 implementation plan explicitly says that work beyond certain phases is waiting for an actual statement of IUT III Corollary 3.12" | **Consistent with what I found** | `Corollary312Variant` is explicitly, permanently unproved by design (node 0 above), not merely "waiting" in a way that implies a near-term resolution — the repository frames it as the project's deliberate specification boundary, not a to-do item. |
| No mention of the André/semistable-reduction caveat, external-dependency surface, or Challenge/Solution comparator structure | **New findings, not in the plan; detail pending** | These nuances were documented in full in this file's lost companion section (see §6.5) — they are real findings, not fabricated here, but their exact sourced detail needs to be re-derived before being restated. |

---

## 6.4 Working dictionary

See [`06b-lean-vocabulary.md`](06b-lean-vocabulary.md): source-located status
(`FORMALIZED` or not) for Hodge theater, theta-link, log-link, log-shell,
log-theta-lattice, and Frobenioid, against this same pinned snapshot.

---

## 6.5 Known gap, and restoration note (full disclosure)

**Restoration note.** This file's content was briefly reorganized into
`guide/03-iut-route.md`, `guide/04-claim-dependencies.md`, and
`guide/03a-dictionary.md` following an instruction that (per explicit later
correction) was actually intended for a different, primary-IUT-papers
strand of this project, which independently uses the same `03`/`04`
numbering for its own literature-based content. This file restores the
Lean-audit strand's ownership to the `06*` namespace, as instructed.

**What was lost in the process.** While migrating content back out of the
`03`/`04` paths, I found that `guide/03-iut-route.md` had already been
overwritten with the primary-papers strand's own (different) content, and
`guide/04-claim-dependencies.md` had already been deleted outright, by a
concurrent process in this shared working directory — both ahead of my own
migration. I had captured this file's `§6.1`–`§6.3` content (above) moments
before `03-iut-route.md` was overwritten, so that material is restored here
verbatim, unchanged. I did **not** have a verbatim capture of
`04-claim-dependencies.md` in hand at the moment it disappeared — only a
structural outline (section headings), not its exact prose, quotes, or
permalinks. Because that file was always untracked (no commit was ever made
for it, per this strand's no-commit constraint), there is no git object to
recover it from.

**That file (`04-claim-dependencies.md`) contained**: a per-edge evidence
ledger for every node/arrow in §6.2.1; three tiers of CI/build evidence for
the elaboration claim in §6.1's methodology row; a 7-package external
Lake-dependency audit (name, pinned SHA, role); an explicit numbered list of
remaining proof obligations; sourced fidelity quotes comparing specific Lean
docstrings to the papers' proposition numbers; a reader audit recipe; and a
final disclaimer. None of that specific sourced detail is reproduced here,
because I cannot verify it from memory with the precision this project
requires — see the next paragraph.

**Why it is reported, not reconstructed.** This project's explicit
requirement is exact, independently re-checkable permalinks and quotes, not
paraphrase from memory. Recreating specific line-number citations, docstring
quotes, or dependency SHAs without re-reading the source risks silently
wrong citations in a rigor-critical document — worse than an honest gap.

**What remains true and usable without re-research** (directly implied by
the restored §6.2.1 table, not reconstructed from the lost file): node 0
(`Corollary312Variant`) is `UNVERIFIED` by design — no proof, no axiom,
confirmed twice in its own docstring; nodes 1–9 are each
`CONDITIONAL_FORMALIZATION`, ultimately resting on `h312` (node 0) plus the
external `genl` / `orbicurve-cores` / `pi1` packages named inline in the
table; node 10 (`ClassicalABC`'s literal statement) is `STANDARD`,
unconditional. This matches the governing framework in
[`00-map.md`](00-map.md). **No axiom or `sorry` was found anywhere in the
chain nodes 0–10 themselves** during the original audit; re-confirm this
independently via §6.6 below before relying on it, since that specific
grep was part of the lost file's evidence and has not been re-run here.

**Recommendation.** Treat the detailed evidence ledger, CI evidence,
dependency-surface audit, and itemized remaining-proof-obligations list as
**pending a short, explicitly re-authorized follow-up pass** against the
same pinned SHA (`d9465c111ec4073709f67e9fccec7e3eb374a816`) — not as
silently restored, and not as abandoned.

---

## 6.6 Reader audit recipe (minimal form, re-derivable without the lost ledger)

1. Clone `lana-agents/iut` at `d9465c111ec4073709f67e9fccec7e3eb374a816`
   (or fetch each permalink above directly — each already pins this SHA).
2. For each row in §6.2.1, open the permalink and confirm the declaration
   name, signature, and quoted docstring text match what is stated here.
3. Run `grep -rln "sorry\b" Iut/ Iut4Sec1/` and
   `grep -rln "^axiom\|  axiom " Iut/ Iut4Sec1/` yourself against the same
   commit to independently re-confirm the axiom/`sorry` inventory (this
   file reports the prior audit's conclusion in §6.5 but the underlying
   grep transcript lived in the lost companion file).
4. Treat any mismatch between what you find and what is stated here as
   upstream drift (if the commit has moved past this pin) or an error to
   report (if the commit is unchanged).

---

## 6.7 Disclaimer

This file describes a Lean-kernel-checked conditional argument inside a
self-contained formal model that the project itself calls a "variant,"
explicitly distinct from Mochizuki's published Corollary 3.12. **Nothing
here asserts that IUT I–IV has been formally verified, that the published
Corollary 3.12 has been proved, or that the Scholze–Stix objection has been
resolved.** §6.5 above discloses a real coverage gap versus the fuller
audit this strand originally completed; it does not weaken any caveat
already stated in this file — if anything it narrows what is claimed, since
the lost material was itself all further caveat/evidence detail, never a
stronger claim than what §6.1–§6.4 already state.
