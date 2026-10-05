# Optional lab: a complete abc theorem for polynomials

This is a **proved analogy**, not a proof of the integer abc conjecture or
of any IUT step. It is worth studying because it makes the conflict between
*size* and *distinct prime factors* visible in a setting with a simple
proof. See also [Keith Conrad's exercises on the Mason--Stothers
theorem](https://kconrad.math.uconn.edu/ross2003/analogy5.pdf#page=1).

Let \(k\) be an algebraically closed field of characteristic zero. Suppose
nonzero, pairwise coprime polynomials \(A,B,C\in k[T]\) satisfy \(A+B=C\)
and are not all constant. Define \(\operatorname{rad}(ABC)\) as the product
of the **distinct monic irreducible factors** of \(ABC\). The
Mason--Stothers theorem says

\[
\max(\deg A,\deg B,\deg C)
\leq \deg\operatorname{rad}(ABC)-1.
\tag{polynomial abc}
\]

Over an algebraically closed field, these irreducible factors are the
distinct roots \(T-\alpha\). For example,
\(T^m+1=C\) with \(A=T^m,B=1\) has many distinct roots in \(C\);
its radical accounts for them even though the power \(T^m\)
contributes just one distinct root.

## Proof, with every divisibility step exposed

1. Set \(W=A'B-AB'\), where primes denote formal derivatives.
   Because the characteristic is zero, \(W=0\) would mean
   \((A/B)'=0\), hence \(A/B\) is constant. Since \(A,B\) are
   coprime, both would be constant, contradicting the hypothesis.
   Thus \(W\neq0\).
2. If \(\alpha\) is a root of \(A\) of multiplicity \(m\), then
   \(B(\alpha)\neq0\). In \(A'B-AB'\), each term is divisible by
   \((T-\alpha)^{m-1}\). The same argument applies to roots of \(B\).
3. Because \(B=C-A\), we can also write \(W=A'C-AC'\).
   At a root of \(C\) of multiplicity \(m\), \(A(\alpha)\neq0\);
   again \((T-\alpha)^{m-1}\) divides \(W\).
4. The root sets of \(A,B,C\) are disjoint by coprimality. Multiply
   the factors just obtained, without double-counting:
   \[
   \frac{ABC}{\operatorname{rad}(ABC)}\mid W.
   \]
   Therefore
   \(\deg A+\deg B+\deg C-\deg\operatorname{rad}(ABC)
     \leq\deg W\leq\deg A+\deg B-1\).
   Cancelling the first two degrees proves
   \(\deg C\leq\deg\operatorname{rad}(ABC)-1\).
5. Rewrite the same equation as \(A=C-B\) or \(B=C-A\) and repeat
   the argument to bound \(\deg A\) and \(\deg B\). This proves
   the claimed maximum bound.

For a sharp example, \(T+1=T+1\) with \(A=T,B=1,C=T+1\) has
\(\deg\operatorname{rad}(ABC)=2\), so the bound reads \(1\leq1\).

## What this proof uses that integers do not give us

The derivative lowers the multiplicity of *each* repeated polynomial root
by at most one, and its degree is strictly less than the degree of the
original polynomial. The same \(W\) sees roots of **all three**
polynomials by rewriting \(A+B=C\). These two facts force the bound.
For ordinary integers, no directly corresponding derivative produces this
divisibility-and-size argument. Replacing \(\deg\) by \(\log\), and
distinct roots by distinct rational primes, describes a **conjectural
analogy**, not a proof; the integer formulation additionally allows
an exponent \(1+\varepsilon\) and a constant \(K_\varepsilon\).

**Why characteristic zero matters.** In characteristic \(p>0\),
take \(A=T^p,\ B=1,\ C=(T+1)^p\). Their product has radical
\(T(T+1)\), with degree 2, while \(\deg C=p>1\).
The derivatives of \(A\) and \(C\) vanish, so \(W=0\) and the
proof cannot begin. Exact hypotheses, not just an attractive diagram,
are decisive.

**Reader exercise:** For \(A=T^2,B=1,C=T^2+1\) over
\(\mathbb C\), compute \(W=2T\) and check that
\(\deg\operatorname{rad}(ABC)=3\). Verify each inequality in step 4.
Then go back to the integer examples in [01](01-abc-target.md)
and identify precisely which line of this proof cannot be copied.
