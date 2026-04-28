# Chunk 006 — End of Unit 13 Exercises & Start of Unit 14 (Calculus of Several Variables)
<!-- Pages: 51-60 -->
<!-- Source: chunk_006.txt -->

## Section: Unit 13 Exercises Q4–Q9 (Continued) [🟡]
<!-- Reason: end-of-unit proofs reinforce sequence/set concepts; Fibonacci sum is a classical identity worth retaining -->

### Core Idea
The first part of the chunk closes Unit 13 by completing inductive proofs that the Fibonacci sequence is unbounded above (continuing from chunk 005), proving the sum identity for Fibonacci numbers, and showing simple bounded/closed-set facts. These exercises consolidate the tools (induction, complements, Archimedean property) used throughout Unit 13.

> **In Simple Terms:** A wrap-up of small proof exercises before the unit officially ends — Fibonacci grows without bound, its partial sums have a tidy closed form, and standard set facts get verified by going through complements.

### Key Concepts

#### Fibonacci sum identity
For all `n`, `Σ_{i=1..n} F_i = F_{n+2} − 1`. Proved by induction: base case `n=1` gives `F_1 = 0` and `F_3 − 1 = 1 − 1 = 0`; the induction step uses the hypothesis `Σ_{i=1..k} F_i = F_{k+2} − 1` and the recursion `F_{k+3} = F_{k+2} + F_{k+1}`.

#### Closed sets via complements
A union of two closed intervals `[a₁,b₁] ∪ [a₂,b₂]` (with `b₁ < a₂`) is closed because its complement `(−∞, a₁) ∪ (b₁, a₂) ∪ (b₂, +∞)` is a union of open intervals (open). The same trick shows an open interval `(a,b)` is not closed (its complement is a union of semi-open intervals) and a semi-closed interval `(a,b]` is not closed.

### Definitions
- **Fibonacci sequence (recursive)**: `F_0 = 0`, `F_1 = 1`, `F_n = F_{n−1} + F_{n−2}` for `n ≥ 2`.

### Mechanisms / Processes
1. To show `F_n` is unbounded: prove inductively `F_{n+1} > F_n > n` for `n ≥ 7` → for any `M`, pick `n > M` so `F_n > M`.
2. Sum identity proof flow: base case → assume true at `k` → expand `Σ_{i=1..k+1} F_i = (F_{k+2} − 1) + F_{k+1} = F_{k+3} − 1`.

### Examples
**Q5 — Sum of first n Fibonacci terms**
- Claim: `Σ_{i=1..n} F_i = F_{n+2} − 1`.
- Base case `n=1`: `F_1 = 0`, and `F_3 − 1 = 1 − 1 = 0`. ✓
- Induction step: `Σ_{i=1..k+1} F_i = (F_{k+2} − 1) + F_{k+1} = F_{k+3} − 1`. ✓

**Q6 — Every finite set {a₁,…,aₙ} is bounded**
Take `m = min{a_i}`, `M = max{a_i}`. Then `m ≤ a_i ≤ M` for every `i`.

**Q7 — Union of two closed intervals is closed**
`R − ([a₁,b₁] ∪ [a₂,b₂]) = (−∞,a₁) ∪ (b₁,a₂) ∪ (b₂,+∞)` (each piece open) → complement is open → original is closed.

### Connections
- Builds on: Bolzano-Weierstrass and bounded sequences (Chunk 005)
- Ends Unit 13; the next sections begin Unit 14.

---

## Section: 14.0 Objectives & 14.1 Introduction [🟢]
<!-- Reason: scope-setting context only -->

### Core Idea
"Calculus of Several Variables" (also "Multivariable" or "Multivariate calculus") extends the calculus of one variable to functions of several variables. The unit will define and compute limits, partial derivatives (explicit, implicit, composite), directional derivatives, Jacobians, Hessians, the Mean Value Theorem and Taylor's theorem (and series) for both single and several variables.

> **In Simple Terms:** A roadmap: the unit takes everything you know from one-variable calculus and lifts it to functions that depend on many variables at once.

### Key Concepts

#### Limit is foundational
The concept of limit underlies every other concept of continuous mathematics — continuity, convergence, differentiation, integration. Extension of the limit concept from one variable to two variables is "surprisingly, much more complicated" than further extension from two to any finite number of variables (50, 100). For this reason, limit is treated first.

### Connections
- Builds on: Block 3 Calculus and Unit 13 Real Analysis.
- Continues into: Section 14.4 Partial Derivatives (Chunk 007).

---

## Section: 14.2 The Concept of 'Limit' [🔴]
<!-- Reason: foundational concept; defines criterion for existence of limit in several variables -->

### Core Idea
The idea of "limit" is to assign **some** value to a function at a point where it may not be defined, but not arbitrarily — the assigned value must be consistent with the values at **all** neighbouring points. For a function of one variable a point can be approached from only two directions (LHS and RHS); for a function of two variables, from infinitely many directions. The limit exists only when values along all approaches reconcile.

> **In Simple Terms:** A limit is the "agreed-on" value at a point: every road into the point must lead to the same number. On the real line there are only two roads. In the plane there are infinitely many roads, which is why two-variable limits are much harder.

### Key Concepts

#### Why limits are defined
Functions can be undefined at points (e.g. `f(x) = (x²−25)/(x−5)` is undefined at `x=5` because the denominator vanishes). The limit assigns a "consistent" value: at neighbours `5±ε` we get `10±ε`, which agrees as `ε → 0`.

#### Single-variable: two directions only
On the real line, neighbours of `a` are `(a−ε)` and `(a+ε)`. If LHS and RHS limits agree, the limit exists.

- Case (i): `lim_{x→0} 1/x²` — both `1/(+ε)²` and `1/(−ε)²` blow up to `+∞`, agree → limit `= +∞`.
- Case (ii): `lim_{x→0} 1/x` — RHS goes to `+∞`, LHS goes to `−∞`, disagree → limit does not exist.

#### Two-variable case: infinitely many directions
A point `(a, b)` in `R²` may be approached along infinitely many paths. The existence of the limit at `(a, b)` depends on **conciliation of values at neighbouring points along potentially infinitely many directions.** Extension from 2 variables to `n>2` variables is essentially straightforward.

### Definitions
- **Limit (multivariable, intuitive)**: a value consistent with values at all neighbouring points along every direction of approach. ⭐
- **Notation**: `lim_{(x,y)→(a,b)} f(x,y)` (preferred) or `lim_{x→a, y→b} f(x,y)`.

### Connections
- Builds on: Unit 9 (Functions, Limits, Continuity, Block 3) and partial derivative limit definitions from Unit 11.
- Continues into: Computing limits (14.3) and limit-based derivatives (14.4).

---

## Section: 14.3 Computing Limit for Functions of Two or More Variables [🔴]
<!-- Reason: practical algorithm for limit computation; prerequisites for partial-derivative limits -->

### Core Idea
For multivariate limits, instead of testing infinitely many directions, exploit continuity: if the function is continuous at the point, limit equals the value at the point. If continuity fails because of a "problematic condition" (zero denominator, negative root, log of zero/negative), try to remove the issue algebraically; otherwise, find two paths that yield different proposed limits — that proves the limit does not exist.

> **In Simple Terms:** First check if the function is continuous at the point — if yes, just plug in. If something blows up, try to cancel it. If you can't cancel, try two different paths — if they disagree, the limit doesn't exist.

### Key Concepts

#### Continuity shortcut
A function `f(x, y)` is continuous at `(a, b)` iff `lim_{(x,y)→(a,b)} f(x,y) = f(a,b)`. Polynomials, trig, exp, log and combinations are continuous when continuous as one-variable functions (by setting `x=y` or treating one as constant). For continuous functions, "the required LIMIT at a point equals the VALUE at that point."

#### Problematic conditions
Watch for: (i) division by zero, (ii) square-rooting negative numbers, (iii) log of zero or negative numbers.

#### Removable problematic condition
Algebraically simplify so the singular factor cancels. E.g. `(x²−2xy+y²)/(x−y) = (x−y)` everywhere except on the line `x = y`; for limit computation the value on that line is irrelevant.

#### Path-testing for non-existence
If a problematic condition cannot be removed, suspect non-existence. Try two paths (e.g. `x=0`, `y=0`, `x=y`, `y=x²`). If two paths give different limits → limit does not exist. **Agreement on two paths does NOT prove existence.**

### Mechanisms / Processes
1. Check continuity (continuous → plug in).
2. If discontinuous, look for removable problematic conditions (factor and cancel).
3. If non-removable, test paths (`x=0`, `y=0`, `x=y`, etc.) — disagreement proves non-existence.

### Examples
**Example 14.1 — Plug-in via continuity**
`lim_{(x,y)→(1,3)} sin((π/2)x) + 3y² + 7`. The function is continuous everywhere, so `= sin(π/2) + 3(9) + 7 = 1 + 27 + 7 = 35`.

**Example 14.2 — Removable singularity**
`lim_{(x,y)→(1,1)} (x² − 2xy + y²)/(x² − y²)`. Denominator zero at `(1,1)`. Factor: `(x²−2xy+y²)/(x²−y²) = (x−y)/(x+y)` everywhere off `x=y`. Limit `= 0/2 = 0`.

**Example 14.3 — Non-existence via paths**
`lim_{(x,y)→(0,0)} xy/(3x² + y²)`.
- Path `x=0`: limit `= 0/y² = 0`. (14.1)
- Path `y=0`: limit `= 0/(3x²) = 0`. (14.2)
- Path `x=y`: `x·x/(3x²+x²) = 1/4`. (14.3)
Since (14.1) and (14.3) disagree, the limit does not exist.

### ⚠️ Common Mistakes
- ❌ Concluding the limit exists because two paths agree → ✅ Two-path agreement is necessary, not sufficient. Always try a non-trivial path (like `x=y` or `y=x²`) to attempt to break agreement.
- ❌ Plugging in directly when the denominator is zero → ✅ First check whether the singular factor can be cancelled.

### Edge Cases & Caveats
- Only the **value at the point itself is excluded** when computing the limit, so cancelling factors zero on the limit line/locus is legitimate.
- Continuity in each variable separately does not by itself guarantee continuity as a function of two variables; use the third bullet rule (continuous when one variable held constant **or** when `x=y`).

> **Quick Recall:**
> - Continuous → plug in.
> - Removable problematic condition → cancel and plug in.
> - Two paths disagree → limit DNE.
> - Two paths agree → inconclusive; try more.

### Connections
- Builds on: Section 14.2 (Chunk 006) Concept of Limit.
- Continues into: Section 14.4 Partial Derivatives (Chunk 007), where partial derivatives are themselves one-variable limits.

### Open Questions
1. Are there algorithmic / non-path-based criteria for proving existence of multivariable limits (e.g. polar-coordinate squeeze)? (Not covered here.)
