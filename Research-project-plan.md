Yes. I think this is a very good candidate for an **AI-assisted mathematical comprehension project**, but I would structure it differently from a normal literature review.

The goal should not initially be *“understand IUT.”* That is too large.

The goal should be:

> **Reconstruct the shortest, explicit dependency chain from standard mathematics → IUT machinery → the disputed Corollary 3.12 → the ABC inequality, while keeping separate what is established, what is claimed, what is disputed, and what has been formally verified.**

I checked the current IUT corpus and, importantly, there is now a very useful 2026 development: the **LANA project has started formalizing pieces of IUT and the implication to ABC in Lean**. Its repository explicitly says that it does **not** yet verify IUT as a whole, but it has formalized IUT IV §1 and parts of the Corollary 3.12 → ABC route. ([GitHub][1])

That gives us a much better starting point than we would have had a few years ago.

---

# 1. The corpus I'd collect

I would divide the corpus into **six layers**, rather than treating all IUT papers as equally important.

## Layer A — The ABC target

Start with the thing we're ultimately trying to understand.

### A1. The original ABC conjecture

We need a precise formulation:

$$
a+b=c,\qquad \gcd(a,b)=1
$$

and for every \(\epsilon>0\),

$$
c < K_\epsilon\,\operatorname{rad}(abc)^{1+\epsilon}
$$

with only finitely many exceptions.

The LANA formalization is actually useful here because it has an explicit formal statement of the classical ABC conjecture and proves equivalent formulations. ([GitHub][1])

### A2. Szpiro conjecture

We need to understand the relationship:

$$
\text{ABC}
\Longleftrightarrow
\text{Szpiro-type statements}
$$

because IUT approaches ABC through arithmetic geometry/elliptic curves rather than attacking \(a+b=c\) directly.

---

# 2. Layer B — The mathematical prerequisites

This is where I would **not** immediately read Mochizuki.

We first build the prerequisite graph.

The important areas include:

### Number theory

* algebraic number fields
* valuations
* places
* \(p\)-adic numbers
* discriminants
* conductors
* heights
* radicals
* Diophantine approximation

### Algebraic geometry

* schemes
* divisors
* line bundles
* elliptic curves
* moduli
* étale fundamental groups

### Arithmetic geometry

* elliptic curves over number fields
* Tate modules
* Galois representations
* reduction at primes
* local/global fields
* Arakelov theory

### Anabelian geometry

This is particularly important because IUT heavily depends on it.

### Mochizuki-specific prerequisites

Then:

* semi-graphs of anabelioids
* anabelioids
* Frobenioids
* étale theta functions
* Hodge–Arakelov theory
* log-shells.

Mochizuki's own IUT workshop explicitly lists **preparatory papers** alongside IUT I–IV, including *Frobenioids I/II*, *The Étale Theta Function*, and *Topics in Absolute Anabelian Geometry*.

---

# 3. Layer C — The four IUT papers

These are the core corpus.

Mochizuki's official publication page lists the four papers:

1. **IUT I — Construction of Hodge Theaters**
2. **IUT II — Hodge-Arakelov-theoretic Evaluation**
3. **IUT III — Canonical Splittings of the Log-theta-lattice**
4. **IUT IV — Log-volume Computations and Set-theoretic Foundations**. ([kurims.kyoto-u.ac.jp][2])

The four papers are roughly:

```text
IUT I
  │
  │ constructs the machinery
  ▼
IUT II
  │
  │ develops arithmetic estimates/evaluation
  ▼
IUT III
  │
  │ develops canonical splittings
  │
  │ ★ Corollary 3.12
  ▼
IUT IV
  │
  │ turns machinery into inequalities
  ▼
ABC / Szpiro / Vojta
```

IUT IV itself says explicitly that the preceding papers develop the log-theta-lattice and Hodge theaters, and that IUT IV applies estimates from the resulting machinery to Diophantine results including Vojta, ABC and Szpiro. ([kurims.kyoto-u.ac.jp][3])

---

# 4. Layer D — The "translation" corpus

This is probably **more important for our purposes than the original papers**.

Mochizuki subsequently wrote material explaining the logical structure of IUT.

Particularly:

### D1. Panoramic Overview of IUT

This should be one of our first documents.

Not because it is necessarily easier, but because it tells us **what Mochizuki thinks the theory is doing**.

### D2. Essential Logical Structure of IUT

There is a later paper specifically called:

> *On the Essential Logical Structure of Inter-universal Teichmüller Theory in Terms of Logical AND "∧"/Logical OR "∨" Relations*

Mochizuki's publication page lists it as a 2024 revised version. ([kurims.kyoto-u.ac.jp][2])

This is particularly valuable for our dependency graph.

### D3. Explicit Estimates in IUT

Also listed on the official corpus. ([kurims.kyoto-u.ac.jp][2])

These may be particularly useful because one of the problems with IUT is that the conceptual machinery is enormous while the ultimate desired output is an inequality.

---

# 5. Layer E — The criticism

This must be a **first-class branch of the corpus**, not an appendix.

We should have:

### Scholze–Stix

The 2018 report concerning the claimed abc proof.

Their objection is centered around the transition involving:

$$
\text{IUT III, Theorem 3.11}
\rightarrow
\text{IUT III, Corollary 3.12}.
$$

This is extremely important because this is effectively the bridge from the machinery to the result needed downstream.

The later LANA report describes the dispute as involving precisely this transition and the interpretation of objects, labels, Hodge theaters, and what can legitimately be compared across them. ([GitHub][4])

### Mochizuki's response

We need his response **side by side** with Scholze–Stix.

Not:

> "Who is right?"

but:

> "What exactly does each side claim the disputed objects mean?"

That distinction is essential.

---

# 6. Layer F — The new 2026 formalization

This is where the project becomes much more interesting.

The **LANA IUT repository** currently contains:

* IUT IV §1 formalization
* the Corollary 3.12 variant
* the implication from that variant to ABC
* formalized classical ABC statements
* concrete versions of parts of the argument.

The repository explicitly describes the project as the **"ABC/IUT trunk."** ([GitHub][1])

For example, it currently has formal versions of things corresponding to:

$$
\text{Corollary 3.12 variant}
\Rightarrow
\text{Theorem 1.10}
\Rightarrow
\text{Corollary 2.2}
\Rightarrow
\text{Corollary 2.3}
\Rightarrow
ABC.
$$

That is *exactly* the dependency chain we want to expose.

There is an important caveat: LANA itself says this does **not verify IUT**. ([GitHub][1])

And its 2026 implementation plan explicitly says that work beyond certain phases is waiting for an actual statement of IUT III Corollary 3.12 to be supplied and reviewed. ([GitHub][5])

So we should treat the Lean corpus as:

> **a second, machine-readable interpretation of portions of the argument**

—not as proof that the entire IUT argument is correct.

---

# The project I'd propose

Now to the actual plan.

I'd make this a **10-stage project**.

---

# Stage 0 — Define the question

Before reading anything, establish four separate questions:

### Q1

What exactly is the ABC conjecture?

### Q2

What exactly does IUT claim to prove?

### Q3

What is the logical path from IUT to ABC?

### Q4

Where exactly does the disagreement with Scholze–Stix occur?

This prevents us from getting lost in the machinery.

---

# Stage 1 — Build the dependency graph

This is the first serious task.

Create a graph where every node is a mathematical proposition/construction.

For example:

```text
ABC
 ↑
Corollary 2.3
 ↑
Corollary 2.2
 ↑
Theorem 1.10
 ↑
Corollary 3.12
 ↑
Theorem 3.11
 ↑
IUT III machinery
 ↑
IUT II
 ↑
IUT I
```

But then expand every arrow.

Each node gets:

```text
ID
Name
Paper
Section
Statement
Prerequisites
Used by
Status
```

And **status** is critical:

```text
STANDARD
CLAIMED
DISPUTED
FORMALLY VERIFIED
ASSUMED
```

---

# Stage 2 — Build the prerequisite graph

Now go *backwards*.

For every unfamiliar object:

> "What must I know to understand this?"

For example:

```text
Hodge theater
     ↓
Θ-data
     ↓
elliptic curve
     ↓
number field
     ↓
scheme
```

But don't automatically read every prerequisite.

Assign:

### Level 0

Elementary enough to proceed.

### Level 1

Understand conceptually.

### Level 2

Need working mathematical understanding.

### Level 3

Need detailed proof-level understanding.

This prevents the classic IUT trap:

> "I need to understand all of anabelian geometry before I can understand IUT."

You probably don't.

---

# Stage 3 — Build a "dictionary"

This may be the most valuable artifact.

Create:

| IUT term                      | Formal definition | Intuition | Existing analogue |
| ----------------------------- | ----------------- | --------- | ----------------- |
| Hodge theater                 | ...               | ...       | ...               |
| Θ-data                        | ...               | ...       | ...               |
| log-shell                     | ...               | ...       | ...               |
| Frobenioid                    | ...               | ...       | ...               |
| mono-anabelian reconstruction | ...               | ...       | ...               |
| alien arithmetic              | ...               | ...       | ...               |
| log-theta-lattice             | ...               | ...       | ...               |

And importantly:

### Don't accept "definition" as "understanding."

For every object ask:

1. What problem does it solve?
2. Why was it introduced?
3. What information does it retain?
4. What information does it deliberately forget?
5. What operations can be performed on it?
6. What cannot be compared?
7. Where is it used downstream?

This is exactly the sort of semantic analysis AI could potentially do better than conventional summarization.

---

# Stage 4 — Reconstruct IUT I as a miniature theory

Don't try to understand all 200 pages.

Find the **minimal spine**.

Something like:

```text
Initial Θ-data
      ↓
Hodge theaters
      ↓
Θ±ell NF-Hodge theaters
      ↓
log-theta-lattice
      ↓
inter-theater relations
```

For each transition:

> What new capability did this construction give Mochizuki?

That is the question.

---

# Stage 5 — Do the same for IUT II

Here we want to understand:

> **What quantitative information does IUT extract from the structures constructed in IUT I?**

Don't obsess over every technical lemma initially.

Follow the information flow:

```text
abstract structure
       ↓
arithmetic quantity
       ↓
comparison
       ↓
estimate
```

---

# Stage 6 — IUT III = the critical stage

Now we slow down dramatically.

This is where I would spend **disproportionately more time**.

Build a complete dependency graph around:

> **Theorem 3.11 → Corollary 3.12**

And annotate every transformation.

Especially distinguish:

```text
same mathematical object
        vs
corresponding object
        vs
label
        vs
copy
        vs
reconstruction
        vs
comparison
```

This is central to the Scholze–Stix criticism.

The LANA report describes the controversy as fundamentally involving the separation of objects, links, labels, indeterminacies, and what can be compared across different Hodge theaters. ([GitHub][4])

---

# Stage 7 — Build the "dispute graph"

This should be a separate artifact.

For each disputed step:

```text
Mochizuki:
A → B

Scholze/Stix:
A ↛ B

Mochizuki response:
the criticism assumes X
but X is invalid because Y

AI analysis:
X means ______
Y means ______
```

And **do not resolve it prematurely**.

The first objective is simply to make the disagreement precise enough that a mathematician could say:

> "Yes, that is exactly what the disagreement is about."

If we can achieve that, we've already made progress.

---

# Stage 8 — Reconstruct the ABC implication independently

This is where the LANA project becomes extraordinarily useful.

We can compare:

### Paper

$$
\text{IUT}
\rightarrow
\text{Theorem 1.10}
\rightarrow
ABC
$$

against:

### Lean

```text
Iut.cor312Variant
       ↓
Theorem110
       ↓
Corollary22
       ↓
Corollary23
       ↓
ClassicalABC
```

The current LANA code explicitly contains these downstream implication theorems. ([GitHub][1])

Now we have **three representations**:

1. Mochizuki's prose
2. Scholze/Stix's interpretation
3. Lean's formal representation.

That is precisely the triangulation we want.

---

# Stage 9 — Use AI as a mathematical adversary

Only now should we unleash an LLM/AI system.

Give it each proposition and ask four independent questions:

### A. Explain

> Explain this without IUT terminology.

### B. Simplify

> Find the simplest mathematical analogue.

### C. Attack

> Search for a counterexample or missing assumption.

### D. Formalize

> Translate this into Lean.

And importantly:

**Use separate AI agents with different objectives.**

```text
             Proposition
                  │
       ┌──────────┼──────────┐
       ↓          ↓          ↓
   Explainer   Critic    Formalizer
       │          │          │
       └──────────┼──────────┘
                  ↓
             Human review
```

This prevents one model's interpretation from becoming the "truth" simply because it wrote the first explanation.

---

# Stage 10 — Produce a human-readable reconstruction

The final artifact shouldn't be another 500-page explanation.

I'd aim for approximately:

## Part I — ABC in 20 pages

## Part II — Required mathematics in 50 pages

## Part III — IUT vocabulary in 30 pages

## Part IV — IUT's core mechanism in 50 pages

## Part V — The critical IUT III transition in 30 pages

## Part VI — IUT → ABC in 20 pages

## Part VII — Scholze–Stix objection in 20 pages

## Part VIII — Lean reconstruction

## Part IX — Open questions

And perhaps the most valuable artifact:

### **"IUT in 20 diagrams."**

---

# I'd also introduce one more concept

Every statement gets a **comprehension status**.

For example:

| Status | Meaning                                              |
| ------ | ---------------------------------------------------- |
| 🟢     | Mathematically standard and independently understood |
| 🔵     | IUT-specific but clearly defined                     |
| 🟡     | Understandable but technically difficult             |
| 🟠     | Interpretation-dependent                             |
| 🔴     | Disputed                                             |
| 🟣     | Formalized in Lean                                   |
| ⚫      | Not yet independently understood                     |

This is much more informative than:

> "IUT is proven."

Because we could eventually say:

> **95% of the dependency graph is formally verified, 90% is conceptually understood, but node X remains disputed.**

That's the kind of map that could actually move the mathematical conversation forward.

---

# The corpus I'd download first

I would **not** download 100 papers immediately.

I'd start with this core set:

### Primary

1. **IUT I**
2. **IUT II**
3. **IUT III**
4. **IUT IV**

Mochizuki's official page provides all four. ([kurims.kyoto-u.ac.jp][2])

### Orientation

5. **Panoramic Overview of IUT**
6. **Essential Logical Structure of IUT**
7. **Explicit Estimates in IUT**

All are part of Mochizuki's published IUT material. ([kurims.kyoto-u.ac.jp][2])

### Prerequisites

8. **Frobenioids I**
9. **Frobenioids II**
10. **The Étale Theta Function and its Frobenioid-theoretic manifestations**
11. **Topics in Absolute Anabelian Geometry**
12. **Anabelian Geometry in the Hodge–Arakelov Theory of Elliptic Curves**

These are among the preparatory/background papers identified in the IUT workshop material.

### Controversy

13. **Scholze–Stix report**
14. **Mochizuki's response**
15. Relevant explanatory material from both sides.

### Modern machine-readable corpus

16. **LANA `iut` repository**
17. Its IUT IV §1 formalization
18. Corollary 3.12 variant
19. IUT → ABC implication
20. LANA's implementation/specification documents.

The LANA repository is particularly valuable because it gives us a living, machine-checkable representation of portions of the argument rather than relying exclusively on prose. ([GitHub][1])

---

## And I think we should make this an actual research project

Given your interest in **AI-assisted mathematical research**, I wouldn't approach this as "let's read Mochizuki."

I'd approach it almost like software reverse engineering:

```text
                  IUT / ABC
                     │
                     ▼
              ┌─────────────┐
              │   Corpus    │
              └──────┬──────┘
                     ▼
             dependency extraction
                     ▼
              mathematical IR
                     ▼
            ┌────────┴────────┐
            ▼                 ▼
       human-readable       Lean
          graph              graph
            │                 │
            └────────┬────────┘
                     ▼
              semantic diff
                     ▼
             disputed nodes
                     ▼
          AI explanation/attack
                     ▼
              human experts
                     ▼
             revised understanding
```

That last **semantic diff** could be particularly powerful: *where does the prose argument, the formalization, and the critics' interpretation actually diverge?*

### One practical next step

I can **collect the actual PDFs and source materials into a structured corpus**, then build **V0 of the dependency graph** from the documents themselves. Since this is a substantial document-analysis task, I'd suggest we do that next rather than manually downloading things one by one. The current LANA repository gives us a particularly good machine-readable starting point, and I can combine it with the primary papers and the criticism.

[1]: https://github.com/lana-agents/iut/blob/main/README.md?utm_source=chatgpt.com "iut/README.md at main · lana-agents/iut · GitHub"
[2]: https://www.kurims.kyoto-u.ac.jp/~motizuki/papers-english.html?utm_source=chatgpt.com "Papers of Shinichi Mochizuki"
[3]: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf?utm_source=chatgpt.com "iu-teich-4.pdf"
[4]: https://github.com/katobungen/LANA_report_202607/blob/main/LANA_report_202607.tex?utm_source=chatgpt.com "LANA_report_202607/LANA_report_202607.tex at main · katobungen/LANA_report_202607 · GitHub"
[5]: https://github.com/lana-agents/iut/blob/main/Plans/Iut4Sec1Spec.md?utm_source=chatgpt.com "iut/Plans/Iut4Sec1Spec.md at main · lana-agents/iut · GitHub"
