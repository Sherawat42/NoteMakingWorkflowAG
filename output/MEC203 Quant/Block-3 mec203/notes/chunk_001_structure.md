# Chunk 001 — Unit 9: Limit and Continuity (§9.0–§9.6)
<!-- Pages: 1-10 -->
<!-- Continues from: N/A -->
<!-- Continues into: Unit 9 §9.6.1 onward (chunk 002) -->

## Section: Block 3 Overview & Unit 9 Front Matter 🟢
- Block 3 covers Units 9–12 (Calculus): Limit & Continuity; Differential Calculus (one var); Differential Calculus (several vars); Integration.
- Unit 9 objectives: identify limit, evaluate one-sided limits, examine continuity, properties, points of discontinuity.

## Section: Limit of a Function 🔴
- Definition (ε–δ); notation `lim_{x→a} f(x) = t`.
- Worked Example 9.1: `lim_{x→1} (x²−1)/(x−1) = 2` (point itself need not be defined).
- Key Term: x → a (x tends to a).

## Section: Right-Hand and Left-Hand Limits 🔴
- RHL `f(a+0)`: a < x < a+δ.
- LHL `f(a−0)`: a−δ < x < a.
- Existence of `lim f(x)` ⟺ RHL = LHL.
- Worked Example: `lim_{x→0} |x|/x` does not exist (RHL=1, LHL=−1).

## Section: Functions Tending to Infinity 🟡
- Definition for `lim f(x)=∞`.
- Limit as x → ∞.
- Examples: `lim 1/x = ∞` from right, `−∞` from left (so does not exist).

## Section: Fundamental Theorems on Limit 🔴
- Algebra of limits: sum, product, quotient (denom ≠ 0), composition, sandwich (squeeze).
- Standard limits: `lim sinx/x = 1`, `lim (1+1/x)^x = e`, `lim log(1+x)/x = 1`, `lim (e^x−1)/x = 1`, `lim (x^n−a^n)/(x−a) = n a^{n−1}`, `lim (1+x)^n−1)/x = n`, `lim x^n/n! = 0`.
- Worked Examples 9.4 (i)–(v).

## Section: Continuity 🔴
- Intuitive: graph drawable without lifting pen.
- Formal: `lim_{x→a} f(x) = f(a)` (LHL = RHL = f(a)).
- Three discontinuity types: ordinary (f(a+0)≠f(a−0)), removable (limits equal but ≠ f(a) or f(a) undefined), infinite (one-sided limit → ∞), oscillatory.
- Some Properties of Continuous Functions (begins §9.6.1, continues into chunk 002).
