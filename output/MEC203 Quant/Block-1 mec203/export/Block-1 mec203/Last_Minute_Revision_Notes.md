# Last Minute Revision Notes

> *This document contains ONLY ultra-high-yield definitions (⭐), Quick Recall facts, Common Mistakes, and core bullet points.*


## Topics

| Block | Title | Units | Focus |
|---|---|---|---|
| 1 | Review of Basic Mathematics | 1–4 | Sets, algebra, relations & functions, coordinate geometry |
| 2 | Linear Algebra | 5–8 | Matrices, determinants, vector spaces, eigenvalues |
| 3 | Calculus | 9–12 | Limits, continuity, differentiation (one & several vars), integration |
| 4 | Real Analysis | 13–15 | n-dimensional real space, calculus of several variables, metric space & topology |
| 5 | Extreme Values and Optimisation | 16–19 | Unconstrained & constrained optimisation (one & several variables) |
| 6 | Economic Dynamics | 20–21 | Difference equations (discrete time), differential equations (continuous time) |
| 7 | Dynamic Optimisation | 22–24 | Intertemporal optimisation, Euler's equation, optimal control |
| 8 | Probability and Probability Distributions | 25–27 | Probability theory, discrete & continuous distributions |
| 9 | Inferential Statistics | 28–31 | Sampling, sampling distributions, estimation, hypothesis testing |

### Mathematical Symbols/Notations Used in the Course 🔴

**Intervals & Basic Calculus Notation**
- **[a, b]**: Closed interval (includes both endpoints a and b). ⭐
- **(a, b)**: Open interval (excludes both endpoints). ⭐
- **∈**: "Element of" / "belongs to". ⭐
- **Δ (Delta)**: Change in (e.g., Δx = change in x).
- **dx**: Differential (infinitesimal change in x).
- **lim f(x)**: Limit of f(x).
- **ln**: Natural logarithm (log to base e).
- **∫ f(x) dx**: Definite integral. ⭐

**Logic & Quantifiers**
- **∀**: Universal quantifier — "for all". ⭐
- **∃**: Existential quantifier — "there exists". ⭐
- **∃!** (written as "∃₁" in source): "there exists exactly one".
- **∃ⱼ** (written as "∃ⱼ" in source): "there exists more than one".
- **¬** (negation): ¬P means "not P".
- **∧**: Conjunction — "and".
- **∨**: Disjunction — "or".
- **⇒**: Implication; p ⇒ q means "if p then q". ⭐
- **⇔**: Equivalence — "if and only if". ⭐

**Numbers, Vectors, Matrices, Sets**
- **a, x ∈ R**: Numbers, scalars.
- **a = (a₁, a₂, …, aₙ) ∈ Rⁿ**: Vector of parameters.
- **x = (x₁, x₂, …, xₙ) ∈ Rⁿ**: Vector of variables.
- **A, X (capital, italic-style)**: Sets.
- **A, X (capital, bold)**: Matrices with dimensions m by n (m rows, n columns).

**Preference Relations (Used in Microeconomics)**
- **x ~ y**: Vector x is indifferent w.r.t. vector y.
- **≻ (strict)**: Strong preference relation.
- **x ≻ y**: Vector x is strongly preferred over vector y.
- **≽ (weak)**: (Weak) preference relation.
- **x ≽ y**: Vector x is (weakly) preferred over vector y.

**Real Number Spaces**
- **R**: Set of real numbers. ⭐
- **R₊**: Set of nonnegative real numbers.
- **int R₊**: Set of positive real numbers (interior of nonnegative reals).
- **Rⁿ = R × R × … × R**: n-dimensional space of real numbers; the Cartesian product of R taken n times. ⭐
- **Rⁿ₊ = {x ∈ Rⁿ | x ≥ 0} ⊂ Rⁿ**: Nonnegative orthant (subspace) of Rⁿ.
- **int Rⁿ₊ ⊂ Rⁿ**: Interior of (nonnegative orthant of) Rⁿ.

**Function Notation**
- **f : X → Y**: Function f mapping from set X to set Y.
- **X**: Domain of a function (set of arguments / inputs).
- **Y**: Codomain of a function (set of values / outputs).

### ⚠️ Common Mistakes
- ❌ Confusing **∈** (member of a set) with **⊂** (subset of a set). → ✅ ∈ relates an element to a set; ⊂ relates two sets.
- ❌ Reading **(a, b)** as an ordered pair when it appears in interval contexts. → ✅ In interval notation, (a, b) is the open interval; in coordinate / vector contexts it can be an ordered pair — context disambiguates.
- ❌ Mixing up ⇒ (implication, one-way) and ⇔ (equivalence, two-way).

**Quick Recall:**
- **[a, b]** closed; **(a, b)** open.
- **∀** = for all; **∃** = there exists.
- **R, Rⁿ, Rⁿ₊** = reals, n-dim reals, nonnegative orthant.
- **¬, ∧, ∨, ⇒, ⇔** are the five core logical connectives.
- **f : X → Y** with **X = domain**, **Y = codomain**.
- Prerequisite for: every Unit in this course. Specifically, calculus notation (dx, ∫, lim) is used heavily in Block 3 (Chunks covering Calculus); preference relations appear in microeconomic optimisation; logic symbols pervade Real Analysis (Block 4).
- Continues into: derivatives, partial derivatives, gradient, Hessian, and Greek alphabet — see Chunk 002.
- Why does the textbook adopt **∈** for "element of" rather than the older **ε**? (Notation evolution.)
- When is the nonnegative orthant **Rⁿ₊** vs the strictly positive orthant **int Rⁿ₊** used in optimisation problems?

### Mathematical Notations (continued) — Functions, Derivatives, Norms 🔴

**Functions**
- **y = f(x)**: Scalar function of one variable. x is the independent variable (argument / input); y is the dependent variable (value of the function). ⭐
- **y = f(x₁, x₂)**: Scalar function of two variables. x₁, x₂ are independent variables; y is the value.

**Derivatives (One Variable)**
- **dy/dx, y′, f′(x)**: First-order derivative of y = f(x). ⭐
- **d²y/dx², y″, f″(x)**: Second-order derivative of y = f(x).
- **df(x)/dx |_{x = x̄}**: Value of a one-variable derivative evaluated at point x = x̄.

**Partial Derivatives (Several Variables)**
- **∂y/∂xᵢ, ∂f(x₁, x₂)/∂xᵢ**: First-order partial derivatives of f(x₁, x₂) with respect to xᵢ for i = 1, 2. ⭐ (NOTE: source OCR shows "0x" / "Ox" / "&" — these are the partial derivative symbol ∂)
- **∂²f(x₁, x₂)/(∂xᵢ ∂xⱼ), ∂²f(x₁, x₂)/∂xᵢ²**: Second-order partial derivatives of f(x₁, x₂).
- **∂f(x₁, x₂)/∂xᵢ |_{x = (x̄₁, x̄₂)}**: Value of a partial derivative evaluated at a specified point.

**Hessian Matrix**
- **H(x₁, x₂)**: Hessian — the symmetric matrix of second-order partial derivatives of f(x₁, x₂):

**Vector & Matrix Operations**
- **(p · x) = Σᵢ₌₁ⁿ pᵢ xᵢ**: Scalar (dot) product of two vectors p, x ∈ Rⁿ. ⭐
- **det(A) or |A|**: Determinant of matrix A. ⭐

**Distance / Metric / Norm**
- **dₑ(x¹, x²) = √[Σ (xᵢ¹ − xᵢ²)²]**: Euclidean metric (distance between two vectors). ⭐
- **d(x¹, x²) = max_{i=1,2} |xᵢ¹ − xᵢ²|**: Non-Euclidean (max / Chebyshev) metric.
- **‖x‖** (Euclidean norm): standard length of vector x.
- **‖x‖ = max_{i=1,2} |xᵢ|**: Non-Euclidean (sup) norm.

**Time**
- **t = 0, 1, 2, …**: Time as a **discrete** variable (used in difference equations, Block 6).
- **t ∈ [0, +∞)**: Time as a **continuous** variable (used in differential equations, Block 6).

**Gradient**
- **∇f, grad f**: Gradient of function f. **∇f = (∂f/∂x₁, …, ∂f/∂xₙ)**. ⭐

### ⚠️ Common Mistakes
- ❌ Writing dy/dx for a multi-variable function. → ✅ Use ∂y/∂xᵢ (partial derivative) when there are several independent variables.
- ❌ Confusing **|A|** (determinant of matrix) with **|x|** (absolute value of scalar) or **‖x‖** (norm of vector). → ✅ Context: matrix → determinant; scalar → absolute value; vector → norm.
- ❌ Forgetting that the Hessian must be **symmetric** (under Young's theorem when mixed partials are continuous): ∂²f/(∂x₁∂x₂) = ∂²f/(∂x₂∂x₁).

**Quick Recall:**
- First derivative: **dy/dx**, **f′(x)**.
- Partial derivative: **∂f/∂xᵢ**.
- Hessian = matrix of 2nd-order partials.
- Dot product: **p · x = Σ pᵢxᵢ**.
- Gradient: **∇f = (∂f/∂x₁, …, ∂f/∂xₙ)**.
- Euclidean distance: **dₑ = √Σ(xᵢ − yᵢ)²**.
- Used in Block 3 (Calculus, Units 9–12), Block 4 (Real Analysis, especially metric space — Unit 15), and Block 5 (Optimisation — Hessian determines second-order conditions for max/min).
| Symbol | Greek Alphabet | Symbol | Greek Alphabet |
|---|---|---|---|
| α | Alpha | θ | Theta |
| β | Beta | λ | Lambda |
| γ | Gamma | π | Pi |
| δ / Δ | Delta | σ | Sigma |
| ε | Epsilon | χ | Chi |
| ψ | Psi | μ | Mu |
| ρ | Rho | ω | Omega |
| Decimal | Roman | Binary |
|---|---|---|
| 47 | XLVII (source OCR: "XZP") | 101111 (source OCR: "101001") |

### ⚠️ Common Mistakes
- ❌ Calling 6 a "number". → ✅ Strictly, 6 is a numeral (name/symbol); the number is the concept "sixness". The textbook accepts the loose usage.
- ❌ Assuming "111" always means one hundred eleven. → ✅ Its meaning depends on the numeral system (base) used.

### Set Theory — Concept of Set 🔴

**What Counts as a Set?**
1. The entities in it are **distinctly identifiable**, AND
2. For any entity in the world, we can say definitively whether it belongs to the collection or not.
- All IGNOU students who enrolled in 2021 for M.A. (Economics).
- The set of decimal digits {0, 1, 2, …, 9}.
- "Some of the IGNOU students enrolled in 2021 for M.A. Economics" — vague (which "some"?).
- "All drops of water in a glass" — drops are not distinctly identifiable.
- The barber paradox collection (see below).

**The Barber Paradox (Russell-style)**
- **Set** (working definition): a well-defined collection of distinctly identifiable objects, with no member repeated. ⭐
- **Member / Element**: any entity belonging to a set. ⭐

### ⚠️ Common Mistakes
- ❌ Listing the same element twice in a set: {1, 2, 2, 3}. → ✅ A set has no repeated members; this is the same as {1, 2, 3}.
- ❌ Treating any vague collection ("tall people", "good students") as a set. → ✅ Only well-defined collections are sets.
- Builds on: notion of "collection".
- Prerequisite for: all subsequent topics — set notation, relationships between sets, set operations, functions, relations.

### Set Notations 🔴

**Basic Notation**
- 0 ∈ Num-Digits, 5 ∈ Num-Digits, 9 ∈ Num-Digits.
- 35 ∉ Num-Digits.

**Naming Convention**
- Set names → start with capital letters (X, Y, N, Num-Digits).
- Elements → lower-case letters (a, b, x, y).
- Names should be **mnemonic** (helpful for remembering contents).

**Extension for Large/Infinite Sets — Triple Dots "…"**
- {0, 1, 4, 9, …, 100, 121, …, 400, …, 10000} or briefly {0, 1, 4, 9, …, 10000} for squares ≤ 10000.
- This set may be named **Sq_int_less_10001**.
- **∈**: "is an element of" / "belongs to". ⭐
- **∉**: "is not an element of" / "does not belong to". ⭐

### Forms of Set Representation 🔴

**(i) Tabular / Roster Form**
- **Sq_int_less_10001 = {0, 1, 4, 9, …, 10000}**.
- Convenient for small sets; awkward for large or infinite sets.

**(ii) Set-Builder Form**
- **Sq_int_less_10001 = {x : x = y², y is an integer, and x < 10001}**.
- Decimal_digits = {0, 1, …, 9} can be written as:
  - {x : x ∈ N and x < 10}, OR
  - {x ∈ N : x < 10}.
| Form | When to use | Pros | Cons |
|---|---|---|---|
| Roster | Small, finite, explicit | Easy to read at a glance | Impractical for large/infinite sets |
| Set-builder | Large or infinite, when a defining rule exists | Compact, exact | Requires clear description of property |

### ⚠️ Common Mistakes
- ❌ Mixing notations within one expression. → ✅ Stick to one form per set definition.
- ❌ Forgetting the colon "·" or "|" in set-builder form. → ✅ The colon is essential — it separates the element variable from its defining condition.

**Quick Recall:**
- **{ }** = set; **∈** = belongs to; **∉** = does not belong.
- Roster form: list elements.
- Set-builder form: **{x : property of x}**.
- Triple dots "…" indicate a continuing pattern.
- Builds on: §1.2.1 Concept of Set.
- Prerequisite for: §1.2.4 Relationships Between Sets, §1.2.5 Special Sets, §1.2.7 Set Operations (Chunk 003).
- When a set is described in set-builder form, who decides the universe of x — the surrounding context, or must it be stated explicitly?

### Cardinality of a Set 🔴
- **|X| or #X**: cardinality of X = number of distinct elements. ⭐
- **|{1, 3, 5}| = 3**.
- **|∅| = 0** (the empty set has 0 elements).
- **|N| = |W| = |Z| = |Q| = ∞** (all are infinite — countably infinite, by later results).
- **|{0}| = 1**.
- **|{1, 3, 5}| = |{1, 3, 7}| = 3** even though {1, 3, 5} ≠ {1, 3, 7} — equal cardinality does not imply equal sets.
- Cardinality is used in §1.2.5 (Power Set: |P(A)| = 2^|A|).

### Check Your Progress 1 🔴
- Practice questions on the concept of "set" — whether collections are sets, expressing them in roster/set-builder form, and computing cardinality. (Answers appear later in §1.8 — mark as ⭐ exam-relevant.)
- (i) The collection of all months of a year beginning with letter **M**.
- (ii) The collection of all months of a year beginning with letter **Z**.
- (iii) The collection of ten **most talented** living writers of the world.
- (iv) A team of eleven **most renowned** football players of the world.
- (v) **{1, 2, 2, 3}**.
- (vi) **{1, 2, {2, 3}, 3}**.
- (a) Positive prime integer factors of 180.
- (b) Solutions of the quadratic equation x² − 3x − 10 = 0.
- (a) {6, 9, 12, 15, 18, 21, 24, 27}.
- (b) {2, 4, 8, 16, …}.
- (c) {{1}, {1, 2}, {1, 2, 3}, …, {1, 2, 3, 4, …, 10}}.

**Quick Recall:**
- "Most talented" / "most renowned" → **subjective**, not well-defined → **not a set**.
- {1, 2, 2, 3} = {1, 2, 3}, cardinality 3 (a set, though redundantly written).
- {1, 2, {2, 3}, 3} has 4 distinct elements: 1, 2, the set {2, 3} (treated as a single element), and 3.

### Relationships Between Sets — Equality, Subset, Proper Subset 🔴

**(i) Equality of Sets — X = Y**
- **Notation**: X = Y.
- **Example**: X = {1, 2, 3, 4, 5}, Y = {x : x is a natural number with 1 ≤ x ≤ 5}, W = {3, 5, 2, 4, 1}. Then **X = Y = W** (order does not matter).

**(ii) Subset / Superset — X ⊆ Y**
- **Notation**: X ⊆ Y.
- **Examples**:
  - X = {a, e, i}, Y = set of all English vowels → X ⊆ Y.
  - **Every set is a subset of itself**: X ⊆ X.

**(iii) Proper Subset / Proper Superset — X ⊂ Y**
- **Notation**: X ⊂ Y (also "Y is a proper superset of X").
- **Example**: X = {0, 2, 4, 6, 8} (even decimal digits), Y = {0, 1, 2, …, 9} (all decimal digits). Then X ⊂ Y, since every even digit is a digit, but 1 ∈ Y and 1 ∉ X.
- Note: **X ⊄ X** as a proper subset, because condition (b) fails.

**(iv) Not a Subset — X ⊄ Y**
- **Example**: X = {1, 5, 10, 15}, Y = {1, 12, 14, 15}. Since 5 ∈ X and 5 ∉ Y, X ⊄ Y. (One witness suffices.)
- **Notation conflict (textbook remark)**: Some authors use **⊂** for "subset (possibly improper)" and **⊊** for "proper subset". This textbook uses **⊆** for subset and **⊂** for **proper** subset. Be careful when reading other texts.

### ⚠️ Common Mistakes
- ❌ Writing X ⊂ X (claiming a set is a proper subset of itself). → ✅ X ⊆ X is true; X ⊂ X is false (no element of X is "extra").
- ❌ To prove X ⊄ Y, listing all elements not in Y. → ✅ Only one counter-example element is needed.
---

**Quick Recall:**
- Subset: every element of X is in Y.
- Proper subset: subset + at least one element of Y not in X.
- Equality: subset both ways.
- Not subset: one counter-example suffices.

### Check Your Progress 2 🔴
- (i) X = {2, 4, 6, 8, 10}, Y = {x : x is positive even integer and x ≤ 10}.
- (ii) X = {x : x is a multiple of 10}, Y = {10, 15, 20, 25, 30, …}.
- (iii) X = {2, 3}, Y = {x : x is a solution of x² + 5x + 6 = 0}.
- (iv) X = {x : x is a letter in the word FOLLOW}, Y = {y : y is a letter in the word WOLF}.
- (i) X = {x : x is a student enrolled in IGNOU and having Economics as one of the courses}, Y = {x : x is a student enrolled in IGNOU}.
- (ii) X = {x : x is a triangle in a plane}, Y = {x : x is a rectangle in the plane}.
- (iii) X = {x : x is an even natural number}, Y = {x : x is an integer}.
- (iv) X = {1, 2, 3} and Y = {1, {2, 3}, 4, 5}.
- (i) 2 ∈ X, (ii) ∅ ∈ X, (iii) ∅ ⊄ X, (iv) ∅ ⊆ X, (v) {2, 3} ∈ X, (vi) {2, 3} ⊂ X, (vii) {{2, 3}} ⊂ X.
- In Q3, note carefully the difference: {2, 3} is an element of X (so {2, 3} ∈ X is **true**), but {2, 3} is **not** a subset of X (the elements 2 and 3 individually are not elements of X).

### Special Sets — Universal, Null/Empty, Power, Convex 🔴

**a) Universal Set (U)**
- Different problems → different universal sets.
- Since X ⊆ X always, we have **U ⊆ U**.
- The concept is **controversial** — leads to paradoxes such as **Russell's paradox** ("the set of all sets" is not a well-defined set, hence not a set). Despite this, the concept is practically very useful.

**b) Empty / Null / Void Set (∅)**
- **Example**: S = {x : x is an even integer and x² = 9} → no integer satisfies both, so S = ∅.
- **Key fact**: **∅ ⊆ X for every set X**. ⭐

**c) Power Set — P(A) or 2^A**
- **Example**: A = {1, 2, 3} →
- The notation **2^A** is used because |P(A)| = 2^|A|.
1. A ⊆ A (every set is a subset of itself).
2. **Transitivity**: if A ⊆ B and B ⊆ C, then A ⊆ C.
3. If A ⊆ B and B ⊆ A, then A = B.
- 4. If |A| = n, then **|P(A)| = 2ⁿ**. ⭐
   - E.g., |{1, 2, 3}| = 3 → |P({1, 2, 3})| = 2³ = 8.

**d) Convex Set**
- **Algebraic form**: if x₁, x₂ ∈ S, then every point on the line segment x₁x₂ — represented as **λx₁ + (1 − λ)x₂** for any λ with **0 ≤ λ ≤ 1** — also belongs to S. ⭐
| | Convex | Non-Convex |
|---|---|---|
| Visual | P———Q (segment fully inside) | P—·—Q (segment escapes) |
| Test | All λx₁ + (1−λ)x₂ inside | Some λ produces a point outside |
- **Universal set U**: largest set under consideration in a given problem context. ⭐
- **Empty/Null set ∅**: set with no elements. ⭐
- **Power set P(A)**: set of all subsets of A. ⭐
- **Convex set**: a set such that the line segment joining any two of its points lies entirely within it. ⭐
- [4, 5) = {x : 4 ≤ x < 5} — convex (any segment between two points stays inside).
- [1, 4] ∪ [7, 11) = {x : 1 ≤ x ≤ 4} ∪ {x : 7 ≤ x < 11} — **not convex** (a point like 5.5 lies on the segment from 3 to 9 but is not in the union).

### ⚠️ Common Mistakes
- ❌ Treating ∅ as having one element (the empty thing). → ✅ ∅ has **zero** elements; |∅| = 0.
- ❌ Counting ∅ or A itself among the proper subsets of A. → ✅ Both are subsets but not proper.
- ❌ Forgetting both endpoints of the convexity inequality: 0 ≤ λ ≤ 1. → ✅ λ ranges over the closed unit interval.

**Quick Recall:**
- **|P(A)| = 2ⁿ** if |A| = n.
- **∅ ⊆ X** for every X.
- **X ⊆ U** for every X under consideration.
- **Convex**: λx₁ + (1−λ)x₂ ∈ S for all 0 ≤ λ ≤ 1.
- Universal set → Complement of a set (defined as U − X) — see Chunk 004.
- Convex sets → essential in optimisation (Block 5): convex feasible regions, convex objective functions guarantee unique global optima.
- Power set → cardinality of P(A) = 2ⁿ is used in combinatorics.
- Is the union of two convex sets ever convex? (Yes, only when one is a subset of the other or when they overlap in a special way.)
- What does "convex" mean in higher-dimensional spaces (Rⁿ)? Same definition — segment connecting any two points stays in the set.

### Check Your Progress 3 🔴
- (i) [4, 5) = {x : 4 ≤ x < 5}, (ii) [1, 4] ∪ [7, 11) = {x : 1 ≤ x ≤ 4} ∪ {x : 7 ≤ x < 11}.
- (i) Find the number of subsets of U.
- (ii) Find the number of proper non-empty subsets of U.

### Quantifiers and Logical Operators 🔴

**a) Quantifiers**
| Symbol | Reads as | Meaning |
|---|---|---|
| (∀x) x ∈ X | "for all x in X" | Statement holds for every element. |
| (∃x) x ∈ X | "for some x in X" / "there exists x in X" | Statement holds for at least one element. |
| (∄ x ∈ X) | "there does not exist x in X" / "there is no x in X (satisfying …)" | No element satisfies the statement. |

**b) Logical Operators**
|---|---|---|
| **P → Q** | "if P then Q" | Implication. |
| **P ↔ Q** | "P if and only if Q" / "P iff Q" | Biconditional / equivalence. |
- "If x is an integer then x² is a non-negative integer": **(∀x ∈ Z) (x² ≥ 0)**.
- "x² = 100 if and only if x = 10 or x = −10": **(x² = 100) ↔ (x = 10 ∨ x = −10)**.

### ⚠️ Common Mistakes
- ❌ Reading **x = 10 → x² = 100** as bidirectional. → ✅ This is one-way only. The reverse (x² = 100 → x = 10) is **false** because x could be −10.
- ❌ Confusing **∃** ("at least one") with **∃!** ("exactly one").
- ❌ Negating ∀ incorrectly. → ✅ ¬(∀x P(x)) ⇔ (∃x ¬P(x)).

**Quick Recall:**
- **∀** = for all; **∃** = there exists; **∄** = does not exist.
- **→** one-way; **↔** two-way.
- "If x = 10 then x² = 100" — true. "If x² = 100 then x = 10" — **false** (x could be −10).
- Used in proofs throughout Block 4 (Real Analysis).
- **Cross-product (Cartesian product)** A × B: set of all ordered pairs (a, b) with a ∈ A, b ∈ B. ⭐
- **Relation on X (arity n)**: a subset of Xⁿ; returns true/false. ⭐
- **Operation on X (arity n)**: a function Xⁿ → X; returns an element of X. ⭐

### ⚠️ Common Mistakes
- ❌ Treating "=" as an operation. → ✅ "=" is a relation (returns true/false), whereas "+" is an operation (returns a number).
- ❌ Thinking ordered pairs are unordered. → ✅ (a, b) ≠ (b, a) in general (whereas the **set** {a, b} = {b, a}).

**Quick Recall:**
- **Relation**: outputs TRUE/FALSE. Examples: <, =, ≠, ⊆.
- **Operation**: outputs a new element. Examples: +, −, ×, ÷, √, |·|, ∪, ∩.
- **Arity**: number of inputs (unary = 1, binary = 2).
---

### Operations on Sets — Union, Intersection, Difference (start) 🔴

**a) Union — X ∪ Y**
- **X ∪ Y = {x : x ∈ X or x ∈ Y}** (inclusive "or" — x may be in both). ⭐
- **Example**: X = {1, 2, 3, 4}, Y = {2, 3, 5, 8, 9} → **X ∪ Y = {1, 2, 3, 4, 5, 8, 9}**.
- Elements common to both (2, 3) appear only once.

**b) Intersection — X ∩ Y**
- **X ∩ Y = {x : x ∈ X and x ∈ Y}**. ⭐
- **Example**: X = {1, 2, 3, 4}, Y = {2, 5, 8, 3, 9} → **X ∩ Y = {2, 3}**.

**c) Difference — X − Y**
- **X − Y = {x : x ∈ X and x ∉ Y}**. ⭐
- (Continued in Chunk 004 with examples and complement.)
- Continues into: complement, worked examples, and Check Your Progress 4 (Chunk 004).
- Foundation for: probability theory (Block 8) where events are sets and probability axioms involve ∪, ∩, complement.

### Set Operations — Difference & Complement (continued) 🔴
- **X − Y = {1, 4}** (elements of X not in Y).
- **Y − X = {5, 8, 9}** (elements of Y not in X).
- **Note**: X − Y ≠ Y − X in general (difference is not commutative).

**d) Complement of a Set — X′**
- **Definition**: **X′ = U − X**. ⭐
- **Example**: U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, X = {2, 5, 8, 3, 9} → **X′ = {1, 4, 6, 7, 10}**.
- **Union ∪**: X ∪ Y = {x : x ∈ X or x ∈ Y}. ⭐
- **Intersection ∩**: X ∩ Y = {x : x ∈ X and x ∈ Y}. ⭐
- **Difference −**: X − Y = {x : x ∈ X and x ∉ Y}. ⭐
- **Complement ′**: X′ = U − X (depends on the chosen universe U). ⭐

### ⚠️ Common Mistakes
- ❌ Computing X − Y as Y − X. → ✅ Not commutative; check direction.
- ❌ Forgetting to specify U when using complement. → ✅ Complement is undefined without an explicit universal set.
---
| Concept | Example | What it refers to |
|---|---|---|
| Operator | ∪, ∩, +, < | The symbol |
| Operation | "Take the union of X and Y to get …" | The process / mapping |
| Operand | X, Y, 7, 5 | The inputs |
| Value | {1, 2, …}, FALSE | The output |

### Check Your Progress 4 🔴
- (a) X ∪ Y
- (b) X ∩ Y
- (c) X − Y
- (d) Y − X

### Numbers — Standard Number Sets 🔴
- **N = {1, 2, 3, …}**: set of **natural / counting numbers**. ⭐
- **W = {0, 1, 2, 3, …}**: set of **whole numbers** (natural numbers + 0). ⭐
  - *Note*: many modern conventions treat 0 as a natural number, so N = W and W is redundant.
- **Z = {…, −3, −2, −1, 0, 1, 2, 3, …}**: set of **integers** (German "Zahlen"). ⭐
- **Q = {x : x = p/q with q ≠ 0, and p, q ∈ Z}**: set of **rational numbers** ("quotient"). ⭐
- Extended below to include R (real) and C (complex).

### R — The Set of Real Numbers 🔴
1. **Pick a line**, mark a left point as **0**, a right point as **1**.
2. **Natural numbers**: mark points to the right of 1 at equal spacings → 2, 3, 4, … .
3. **Negative integers**: mark points to the left of 0 at equal spacings → −1, −2, −3, … .
4. **Rational numbers**: e.g., for **3.45**, divide [3, 4] into 100 equal parts and mark the 45th part to the right of 3.
5. **Irrational numbers**: e.g., for **√2**, construct a unit square; its hypotenuse has length √2; mark this distance to the right of 0 on the number line.
6. **Result**: every point on the line corresponds to a real number, and conversely.
- **Real number**: a number obtained by corresponding to a point on a straight line (as above). ⭐
- **R = {x | x is a real number}**.
- **Irrational number**: a real number that is **not** rational. The set of irrationals is **R − Q** (also written R \ Q). ⭐
  - **Example**: √2 (proven irrational — no p/q exists with p² /q² = 2).
  - **Fact**: there are **more** irrational reals than rational reals (irrationals are uncountable, rationals are countable).

### Real Number Intervals 🔴
| Interval | Reads as | Includes 3? | Includes 7.5? | Type |
|---|---|---|---|---|
| **[3, 7.5]** | "closed interval 3 to 7.5" | Yes | Yes | Closed |
| **(3, 7.5]** or **]3, 7.5]** | "left-open, right-closed" | No | Yes | Semi-open / semi-closed |
| **[3, 7.5)** or **[3, 7.5[** | "left-closed, right-open" | Yes | No | Semi-open / semi-closed |
| **(3, 7.5)** or **]3, 7.5[** | "open interval" | No | No | Open |

### ⚠️ Common Mistakes
- ❌ Using **(3, 7.5)** for the ordered pair when the context is intervals. → ✅ Context disambiguates; the same bracket notation is overloaded.
- ❌ Confusing closed vs open intervals when checking convexity or extreme values. → ✅ Closed intervals attain max/min; open ones may not.

**Quick Recall:**
- **[ ] include endpoints**, **( ) exclude endpoints**.
- 4 types: closed, open, two semi-open variants.
- Used in defining continuity, limits (Block 3), convex sets (§1.2.5, Chunk 003).

### Complex Numbers — C 🔴
- **i**: the imaginary unit, with **i² = −1**. ⭐
- **C = {z : z = x + iy, where x, y ∈ R}** = set of **complex numbers**. ⭐
- (x + iy is also written x + yi.)
- Any real x ∈ R can be written x = x + i·0, so x ∈ C → R ⊆ C.
- 1 + i·2 ∈ C but 1 + i·2 ∉ R (and i = 0 + i·1 ∈ C but i ∉ R).
- Therefore **R ⊂ C** (proper).
- Symbols **∅, N, W, Z, Q, R, C** are **standard** and may be used without redefinition. Custom set names (like **Sq_int**) must be defined fresh in each new context.
| Number | N? | Z? | Q? | Irrational? | R? | C? |
|---|---|---|---|---|---|---|
| 3 | ✓ | ✓ | ✓ |  | ✓ | ✓ |
| −12 |  | ✓ | ✓ |  | ✓ | ✓ |
| 8.7 |  |  | ✓ |  | ✓ | ✓ |
| 2/3 |  |  | ✓ |  | ✓ | ✓ |
| √2 |  |  |  | ✓ | ✓ | ✓ |
| π |  |  |  | ✓ | ✓ | ✓ |
| 7 − 3i |  |  |  |  |  | ✓ |
  - **Absolute value**: **|x| = −x if x < 0; |x| = x if x ≥ 0**. ⭐
- Two fractions p/q and r/s (with q ≠ 0, s ≠ 0) are equal as rationals iff **p × s = q × r**. ⭐
- A natural number p is **prime** if the only natural numbers dividing p are **1 and p itself**. ⭐

### ⚠️ Common Mistakes
- ❌ Saying 3/5 and 6/10 are different rational numbers. → ✅ They are different *fractions* but the same *rational number*.
- ❌ Including 1 as a prime. → ✅ 1 is a unit, not a prime.
- ❌ Thinking |x| produces a negative output. → ✅ |x| ≥ 0 always.

**Quick Recall:**
- π and √2: irrational reals.
- 1 is **not** a prime.
- p/q = r/s iff p·s = q·r.
- |x| = max(x, −x); always ≥ 0.
---

### Properties of Real Numbers as an Ordered Field 🔴

**a) Field Properties (R, +, ×) — for all x, y, z ∈ R ⭐**
| # | Property | Statement |
|---|---|---|
| 1 | Closure | x + y ∈ R, and x × y ∈ R. |
| 2 | Associativity | (x + y) + z = x + (y + z); (x × y) × z = x × (y × z). |
| 3 | Existence of unique identities | 0, 1 ∈ R such that x + 0 = 0 + x = x and x × 1 = 1 × x = x. |
| 4 | Existence of unique inverses | For every x ∈ R, ∃ (−x) such that x + (−x) = (−x) + x = 0. For x ≠ 0, ∃ x⁻¹ such that x × x⁻¹ = x⁻¹ × x = 1. |
| 5 | Commutativity | x + y = y + x; x × y = y × x. |
| 6 | Distributivity (× over +) | x × (y + z) = x × y + x × z. |

**b) Ordered Field Properties (additional, with relation <) — for all x, y, z ∈ R ⭐**
|---|---|---|
| 1 | Positivity preservation | If 0 < x and 0 < y then 0 < x + y and 0 < x × y. |
| 2 | **Trichotomy** | For x ∈ R, exactly one of (a) x < 0, (b) x = 0, (c) 0 < x is true. ⭐ |
| 3 | **Transitivity** | If x < y and y < z, then x < z. ⭐ |
| 4 | Monotone property of addition | If x < y, then x + z < y + z. |
| 5 | Monotone property of multiplication | If x < y and 0 < z, then x × z < y × z. |
| 6 | **Archimedean property** | Given two positive numbers A and B, there exists a natural number n such that **B < n × A**. ⭐ |

**c) Metric / Norm Properties (with |·| modulus) — for all x, y, z ∈ R ⭐**
|---|---|---|
| 1 | Non-negativity & definiteness | |x| ≥ 0; |x| = 0 iff x = 0. |
| 2 | Symmetry under negation | |x| = |−x|. |
| 3 | Bracketing | −|x| ≤ x ≤ |x|. |
| 4 | **Triangle inequality** | **\|x + y\| ≤ \|x\| + \|y\|**. ⭐ |

**Distance Function ‖·‖ : R × R → R**
| # | Property |
|---|---|
| 1 | ‖x − y‖ ≥ 0; ‖x − y‖ = 0 iff x = y. |
| 2 | ‖x − y‖ = ‖y − x‖ (symmetry). |
| 3 | **Triangle Inequality**: ‖x − z‖ ≤ ‖x − y‖ + ‖y − z‖. ⭐ |

### ⚠️ Common Mistakes
- ❌ Forgetting the multiplicative inverse exists only for x ≠ 0. → ✅ 0 has no multiplicative inverse.
- ❌ Asserting the triangle inequality with equality always. → ✅ Equality holds only when x and y have the same sign (or one is zero).
- ❌ Misapplying monotone multiplication: multiplying both sides of an inequality by a **negative** number reverses the inequality. → ✅ The textbook's monotone property requires **0 < z**.

**Quick Recall:**
- 6 Field axioms + 6 Order axioms + 4 Metric axioms.
- **Trichotomy**: x is <0, =0, or >0 — exactly one.
- **Archimedean**: no number in R is "infinitely large" relative to others — multiples of any positive A eventually exceed any B.
- **Triangle inequality**: |x + y| ≤ |x| + |y|.
- Foundation for **real analysis** (Block 4): completeness, sequences, continuity all build on these axioms.
- The Archimedean property is critical for limits and ε-δ proofs.

### Decimal Representation of Rational and Irrational Numbers 🔴

**(i) Terminating Decimal — Rational**

**(ii) Non-Terminating Recurring Decimal — Rational**

**(iii) Non-Terminating Non-Recurring Decimal — Irrational**
1. Count digits after the decimal point: **7** digits → write **10⁷ = 10,000,000** as denominator (a 1 followed by seven 0s).
2. Numerator = the number with the decimal point removed: **1,870,145,083**.
3. So 187.0145083 = **1,870,145,083 / 10,000,000**.
1. Move decimal to make integer numerator.
2. Denominator = 10^(number of digits past decimal).
3. Simplify by dividing numerator and denominator by their GCD (e.g., divide by 25, then look for further common factors).

### ⚠️ Common Mistakes
- ❌ Thinking 0.999… is different from 1. → ✅ 0.9̄ = 1 exactly (a classic surprise).
- ❌ Assuming all non-terminating decimals are irrational. → ✅ They are irrational only if they are also non-repeating; 0.333… = 1/3 is rational.

**Quick Recall:**
- Terminating decimal → rational.
- Repeating decimal → rational.
- Non-terminating, non-repeating → irrational.
- To convert: use 10^k denominator, then simplify by GCD.
---

### Real Number Exponentiation 🔴

**Positive Integer Exponent**
- **Examples**:
  - 19⁴ = 19 × 19 × 19 × 19.
  - (−15)³ = (−15) × (−15) × (−15).
  - (3/4)⁵ = 3⁵ / 4⁵.
- **General rule**: **(x/y)ⁿ = xⁿ / yⁿ**.

**Zero and Negative Integer Exponent**
- **x⁰ = 1**. ⭐
- **x⁻¹ = 1/x**.
- **x⁻ⁿ = (1/x)ⁿ = 1/xⁿ** for n ∈ N. ⭐
- **Example**: 19⁻³ = (1/19)³ = (1/19)(1/19)(1/19) = 1/6859.

**Rules of Exponents (for m, n ∈ Z, and indeed m, n ∈ R) ⭐**
| Rule | Formula |
|---|---|
| Product of same base | **x^(m+n) = xᵐ · xⁿ** |
| Power of a power | **x^(mn) = (xᵐ)ⁿ** |
| Negative exponent | **x⁻ⁿ = 1/xⁿ** |
| Quotient of same base | **x^(m−n) = xᵐ / xⁿ** |
| Power of product | **(x · y)ᵃ = xᵃ · yᵃ** |
| Power of quotient | **(x/y)ᵃ = xᵃ / yᵃ** |

**Fractional Exponents and Roots**
- **√2** means the number whose square is 2: √2 × √2 = 2.
- **⁴√7** means the 4th root of 7: ⁴√7 × ⁴√7 × ⁴√7 × ⁴√7 = 7.
- **In general**: for **n ≠ 0**, **ⁿ√x = x^(1/n)**, where x may be any real (or complex) and n is a natural number.

**General Fractional Exponents**
- **x^(m/n) = x^(m·(1/n)) = ⁿ√(xᵐ)** = (ⁿ√x)ᵐ. ⭐
- For n ≠ 0: **x^(m/n) = (x^(1/n))ᵐ = (ⁿ√x)ᵐ**.

**Arithmetic Operations on Bases**
- **Multiplication / division of same exponent**:
  - **(x · y)ᵃ = xᵃ · yᵃ**.
  - **(x/y)ᵃ = xᵃ / yᵃ**.
- **Addition / subtraction of like-exponent expressions** **xⁿ + yⁿ** or **xⁿ − yⁿ**: treated as **almost independent irreducible expressions**, except when x and y share a common factor ≠ 1.
- 6 = 3 × 2, so 6⁷ = (3 × 2)⁷ = 3⁷ × 2⁷.
- 3⁵ + 6⁷ = 3⁵ + 3⁷ × 2⁷ = 3⁵ × (1 + 3² × 2⁷) = 3⁵ × (1 + 9 × 128) = 3⁵ × (1 + 1152) = 3⁵ × 1153.

### ⚠️ Common Mistakes
- ❌ Treating x^(1/2) + y^(1/2) as (x + y)^(1/2). → ✅ **Not equal**: √x + √y ≠ √(x + y) in general.
- ❌ Assuming (xᵐ)ⁿ = x^(m+n). → ✅ It equals **x^(mn)** (multiply, not add).
- ❌ Computing 0⁰ as 1 or 0 without context. → ✅ 0⁰ is conventionally 1 in combinatorics but indeterminate in calculus.
- ❌ Forgetting x⁻ⁿ ≠ −xⁿ. → ✅ x⁻ⁿ = 1/xⁿ; the minus sign in the exponent flips the number, not its sign.

**Quick Recall:**
- x^(m+n) = xᵐ · xⁿ.
- (xᵐ)ⁿ = x^(mn).
- x⁰ = 1.
- x⁻ⁿ = 1/xⁿ.
- x^(1/n) = ⁿ√x.
- (xy)ᵃ = xᵃyᵃ; (x/y)ᵃ = xᵃ/yᵃ.
- Foundation for: logarithms (inverse of exponentiation), exponential functions e^x (Block 3), growth/decay models in economic dynamics (Block 6), compound interest.

### Check Your Progress 5 🔴
| Category | Examples |
|---|---|
| Set operators | **∪** (union), **∩** (intersection), **−** (difference), **′** (complement) |
| Set-relational symbols | **=**, **⊆** (subset), **⊂** (proper subset), **⊄** (not subset), **∈** (belongs to), **∉** (does not belong) |
| Algebraic / arithmetic operators | **+, −, ×, ÷, √, |·|, log, eˣ** |
| Algebraic / arithmetic relational symbols | **=, ≠, <, ≤, >, ≥** |

### Key Words (Glossary) 🔴
- **Cross-Product of sets**: For two non-empty sets A₁ and A₂, A₁ × A₂ is the set of all ordered pairs (a₁, a₂) with a₁ ∈ A₁, a₂ ∈ A₂. Generalises to A₁ × A₂ × … × Aₙ as the set of all n-tuples (a₁, a₂, …, aₙ) with aᵢ ∈ Aᵢ for i = 1, 2, …, n. ⭐
- **Number**: An abstract concept used for counting, measuring, or labelling. Made tangible through numerals — e.g., "five" is purely an idea, made tangible through the numeral **5**. ⭐
- **Operation on a set X**: An operation of arity n maps the n-fold cross-product of X with itself to **X itself** (returns an element of X). E.g., square on N (arity 1) and sum on N (arity 2) both return a number. ⭐
- **Relation on a set X**: A relation of arity n is a **subset of the n-fold cross-product** of X with itself; returns exactly **true or false**. E.g., is-male (arity 1), is-mother-of (arity 2). ⭐
- **Set**: A well-defined collection of objects, where a collection C is well-defined iff for any x we can determine whether x belongs to C or not. ⭐
- These definitions tie together every section of Unit 1 and serve as the working vocabulary for all subsequent units.
- How does the textbook later distinguish "Number System" (different from Numeral System mentioned in §1.1)?
- The exercises at §1.9 and answers at §1.8 likely appear in the next chunk — do they confirm the conjectured answers above?

### ⚠️ Common Mistakes
- ❌ Treating "the most talented students" as a set → ✅ Not a set (ill-defined membership)
- ❌ Counting U and ∅ when asked for proper non-empty subsets → ✅ Exclude both (62, not 64)

**Quick Recall:**
- A collection is a set only if membership is unambiguously defined.
- |P(X)| = 2ⁿ where n = |X|.
- De Morgan: complement of union = intersection of complements; complement of intersection = union of complements.
- A set equality proof goes both ways via arbitrary element argument.

### Symbol, Parameter, Variable, Constant (2.2.1) 🔴

**Symbol**

**Parameter**
- Example: in x² + y² = c (with real c > 0), c parameterises a family of circles of radius √c centred at origin.
- Setting c = 4 yields the circle x² + y² = 4 (radius 2); c = 15 yields radius √15.
- Significance: questions like "rectangle of maximum area inscribed in the circle" can be solved once for general c, then specialised — a parameter is a *generalised constant*.

**Variable**
- Economics examples: price, interest-rate, wages, quantity-bought, quantity-sold.
- Value of variable at a particular time = its measurement at that time (e.g., 6% interest-rate today).
- A variable assumes only its *possible* values — e.g., √(−8) is not a possible value for "percentage-of-Interest-rate" but is a possible value for x in ax² + bx + c = 0.
- Naming convention: end letters x, y, z (and others) of Latin alphabet.

**Constant**
- Example: 6 (Latin) and ६ (Devanagari) each have one value.
- Naming convention: beginning letters a, b, c.
| Concept | Number of values | Typical naming | Example |
|---------|-----------------|---------------|---------|
| Constant | exactly one | a, b, c, ... | 6, ६, π |
| Variable | many possible | x, y, z, ... | price, x in ax²+bx+c=0 |
| Parameter | one *per analysis*, varies between analyses | (context-dependent) | c in x² + y² = c |
| Symbol | (umbrella concept) | any notation | 'lake', x, 6 |

### ⚠️ Common Mistakes
- ❌ Treating a parameter as a "variable" inside its own analysis → ✅ It is locally constant; it generalises only across analyses.
- ❌ Plugging an inadmissible value (e.g. negative for a percentage) → ✅ A variable can only assume its possible values.
- Builds on: Set theory (Unit 1) — variable values come from a set of admissible values.
- Continues into: 2.2.2 Mathematical Expressions

### Algebraic Concepts and Mathematical Expressions (2.2.2) 🔴

**Expression (general)**

**Mathematical Expression — Construction Rules**
1. **Atomic:** Each constant, variable, parameter is itself an ME. So 7, x, c, 14.78 are MEs.
2. **Unary operators** must be in correct position with one operand (constant/variable/parameter/ME containing no relational operator). Valid: √(8−y), (x+y)², eˣ⁺²ʸ⁻⁴ᶻ, log(3x+5), |y+56|. Invalid: −8√, x log, ᵉe, y| | (operator misplaced); √(8 < y), (36x = 49)² (operand contains relational operator).
3. **Binary operators** require two operands at correct positions. Valid: (√867 − eˣ⁺²ʸ), (x + 2y − 4z), (√(8−y) × (x+y)² + log(x − eʸ)). Invalid if any operand contains a relational operator or invalid sub-expression.
4. **Binary relations** require two operands that are themselves expressions without internal relations. So (√867 − eˣ⁺²ʸ) < (√(8−y) × (x+y)² + log(x − eʸ)) is valid, but (√867 = eˣ⁺²ʸ) < ((8−y)×(x+y) > log(x−eʸ)) is NOT (RHS contains '>').
   - Shorthand chain: x < y < z means "x < y and y < z" (similarly for ≤, >, etc.).
5. **Other expressions:** limits limₙ→∞(1+1/n)ⁿ, derivatives dy/dx, integrals ∫f(3x+2)dx — discussed in later units.

**Classification of Mathematical Expressions**
| Type | Restriction | Example |
|------|-------------|---------|
| **Arithmetic** | No variables | (√(−8 + 489) × (7! + 56)² + log(155 − e⁹)) |
| **Polynomial** | Variables only with non-negative integer powers | 7x³ − 5x + 11; (x+y)² |
| **Algebraic** | Variables with rational powers p/q (q ≠ 0, p,q integers) | √(8−y); √(1+x²)/√(1−x²) |
| **General** | Anything constructible by syntax rules | log x, eˣ, dy/dx, ∫ |
- Constants in a polynomial may have fractional powers (e.g., x² + (17)¹ᐟ² is polynomial because the variable x has integer power; 17 is a constant).
- √(8−y) = (8−y)¹ᐟ² is algebraic, NOT polynomial.

**General Forms — Equation**
- Beyond algebraic: equations involving log, e, trigonometric functions; set-theoretic equations (e.g. (X ∩ Y)ᶜ = Xᶜ ∪ Yᶜ — actually an *identity*); logical equations; differential and integral equations.
- General form: any equation may be rewritten as f(x) = 0 (move RHS to LHS).

**Root / Solution / Zero**
- A *root/solution* of f(x) = 0 is a constant a such that f(a) = 0.
- Example: f(x) = x² − 4 = 0; f(2) = 4 − 4 = 0, so x = 2 is a root.
- We also say "2 is a *zero* of the function f(x)". The word "zero" applies to the **function** f, not the equation f(x) = 0.

**Mathematical Identity vs Equation**
| | Equation | Identity |
|---|---|---|
| Holds for | specific value(s) of variable | every value of the variable |
| Example | X² − 16 = 0 (only X = ±4) | X² − 16 = (X+4)(X−4) (every X, real or complex) |
| Symbol | = | ≡ (when emphasis needed) |

**Various Usages of '=' in Mathematics**
| Usage | Example | More-specific symbol |
|-------|---------|----------------------|
| In equations | find x: x² + 4x + 3 = 0 | = |
| In identities/laws | (a+b)² = a² + b² + 2ab for all real a,b | ≡ |
| In conditional statements | "If x = 7, then ..." | = |
| In relations (T/F evaluations) | 3 = 4+2 (false), 3 = 2+1 (true) | = |
| In assignments | "Let x = 8" | := (Pascal-style) |
| In definitions | Area = length × breadth | ≜ (or ≡) |
- |y + 56| is an ME (unary | | with single operand y+56).
- √(8 − y) × is NOT an ME (binary × missing right operand).
- log((8 < y) × (x+y)²) is NOT an ME (operand contains '<').
- **Mathematical Expression**: a sequence of mathematical terms (constants, variables, parameters, relations, operations) formed by the structuring rules of mathematics. ⭐
- **Arithmetic Expression**: ME with no variables.
- **Polynomial Expression**: ME whose variables appear only with non-negative integer powers. ⭐
- **Algebraic Expression**: ME whose variables appear with rational powers p/q (p,q integers, q ≠ 0).
- **Equation**: ME with exactly one '=' and no other relations.
- **Identity**: equation true for every value of the variable. ⭐
- **Root/Solution** of f(x) = 0: a constant a with f(a) = 0.
- **Zero** of f(x): same value a, but spoken *of the function*.

### ⚠️ Common Mistakes
- ❌ Saying "2 is a zero of the equation" → ✅ 2 is a *zero of the function* / *root of the equation*.
- ❌ Confusing identity and equation → ✅ Identity holds for all values; equation only for solutions.
- ❌ Treating √(8−y) as polynomial → ✅ It is algebraic (rational power 1/2), not polynomial.
- ❌ Writing log x as polynomial → ✅ log is not allowed in polynomials.
- Parentheses must be paired. An expression like "log (x+y)²" with mismatched parentheses is not an ME.
- Relational operators inside operands of operators or other relations are forbidden.

**Quick Recall:**
- Expression ⊃ Algebraic ⊃ Polynomial ⊃ Arithmetic.
- Polynomial: only non-negative integer powers of variables.
- Equation: exactly one '='; identity: equation true for all values.
- Zero of function f = root of equation f(x)=0.
- Builds on: numbers, exponents (Unit 1)
- Continues into: 2.2.3 Polynomials (Chunk 006)

### Polynomials and Polynomial Equations (2.2.3) 🔴

**Term**
- x³ + 8x − 4 has three terms: x³, 8x, −4.
- (x − y)² at the highest level has only one term; on expansion x² + y² − 2xy has 3 terms.
- In x³y + 8x − 4y², the powers are: x: 3 in x³y, 1 in 8x, 0 in −4y²; y: 1, 0, 2 respectively.
- A *term* contains no '+' or '−' at the top level; uses only ×/exponentiation in polynomial terms (no division by variable). (45x²)/(78y) is an algebraic term but not a polynomial term.

**Factor & Coefficient**
- Coefficient of 17xy is 17; coefficient of −25x is −25.

**Monomial / Binomial / Trinomial / Polynomial**
| Name | Number of terms | Example |
|------|----------------|---------|
| Monomial | 1 | 45x²y³ |
| Binomial | 2 | 45x²y³ − 25; a + b |
| Trinomial | 3 | 45x²y³ − 25x⁴ + 71y⁵; a + b − 72 |
| Polynomial (general) | one or more terms (each with non-zero coefficient, variables with non-negative integer exponents) | 45x⁵ − 25x⁴ + 91x − 36 |

**General Form of a Polynomial Equation**

**Degree**
- **Degree of a term** = sum of powers of all variables in that term.
  - deg(45x²y³) = 2 + 3 = 5.
  - deg(345) = 0 (constant; can be regarded as 345·x⁰ since x⁰ = 1 for any non-zero x).
- **Degree of a polynomial** = max degree among its terms.
  - For 45x²y³ + 71y⁵ − 25x⁴: degree = 5.
- **Degree of a polynomial equation** = max degree among terms on both sides.
  - For 71y³ + 45x²·z·y³ + 2xy = −25x³: degree = 7 (the 45x²zy³ term contributes 2+1+3 = 6... [the textbook gives 7; OCR ambiguity, but the principle is "max term degree"]).
- Convention: a polynomial is generally written in *order of decreasing degree of its terms*.

**Naming a Polynomial**

**Evaluating a Polynomial**
- For P(x, y) = 4x³ − 7xy² + 11:
  - P(2, −1) = 4(2)³ − 7(2)(−1)² + 11 = 32 − 14 + 11 = 29 [textbook OCR shows "16 − 14 + 11 = 13"; treating the original published value as printed]. Note: the textbook prints 4(2)³ = 16 which appears as an OCR/text artefact; the **method** is what matters.
  - P(−1, 2) = 4(−1)³ − 7(−1)(2)² + 11 = −4 + 28 + 11 = 35 [textbook shows 43 — OCR mismatch in printed source].

**Solution of a Polynomial Equation (multi-variable)**

### ⚠️ Common Mistakes
- ❌ Calling (45x²)/(78y) a polynomial term → ✅ It is algebraic, not polynomial (variable in denominator).
- ❌ Forgetting that the constant term has degree 0 → ✅ 345 = 345·x⁰, so deg = 0.
- ❌ Saying √x or x⁻¹ are allowed in polynomials → ✅ Only non-negative integer powers of variables.

**Quick Recall:**
- Polynomial: variables to non-negative integer powers only.
- Degree of term = sum of exponents; degree of polynomial = max term degree.
- Standard form: write in decreasing degree.
- Builds on: classification of mathematical expressions (Chunk 005)
- Continues into: 2.2.4 Polynomial Identities

### Polynomial Identities (2.2.4) 🔴

**Standard Polynomial Identities**
1. (x + y)² = x² + y² + 2xy
2. (x − y)² = x² + y² − 2xy
3. x² − y² = (x + y)(x − y)
4. (x + a)(x + b) = x² + (a + b)x + ab
5. (x + y + z)² = x² + y² + z² + 2xy + 2xz + 2yz
6. (x − y − z)² = x² + y² + z² − 2xy − 2xz + 2yz   [from (5) by y → −y, z → −z]
7. (x + y)³ = x³ + y³ + 3xy(x + y)
8. (x − y)³ = x³ − y³ − 3xy(x − y)
9. x³ + y³ + z³ − 3xyz = (x + y + z)(x² + y² + z² − xy − yz − zx)
- 625/16 = (25/4)² and 9/49 = (3/7)².
- (625/16)x⁴ − (9/49)y² = [(25/4)x²]² − [(3/7)y]²
- = [(25/4)x² + (3/7)y] · [(25/4)x² − (3/7)y]   (using identity 3)

### ⚠️ Common Mistakes
- ❌ Sign errors when applying (x − y)² → ✅ Note middle term is −2xy.
- ❌ Forgetting the all-cross-products in (x+y+z)² → ✅ Six terms total: x²+y²+z² + 2(xy+xz+yz).

**Quick Recall:**
- x² − y² = (x+y)(x−y) — most reused identity.
- (a+b+c)² = a² + b² + c² + 2(ab+bc+ca).
- x³ + y³ + z³ − 3xyz factors via (x+y+z)(x²+y²+z²−xy−yz−zx).
- Builds on: 2.2.3 polynomials.
- Continues into: 2.2.5 Algebra of Polynomials

### Algebra of Polynomials (2.2.5) 🔴

**Like Terms vs Unlike Terms**
- **Like terms**: identical except for their constant parts.
  - 17x²y³ and −39x²y³ are like terms; sum simplifies to (17 − 39)x²y³ = −22x²y³.
- **Unlike terms**: differ in at least one variable's exponent.
  - 17x²y³ and −39x³y² are unlike (cannot be combined as a single term). Sum 17x²y³ + (−39x³y²) may be partially factored as x²y²(17y − 39x).

**Sum / Difference of Two Polynomials**
- For subtraction P − Q, first form R from Q by flipping every '+' to '−' and '−' to '+' (i.e., R = −Q), then compute P + R.

**Product of Two Polynomials**
- Simple case: one factor is a constant. Multiply each term by the constant.
  - P(x,y) = 3x² − 5xy + 3x + 8; Q = 7. P × Q = 21x² − 35xy + 21x + 56.
- General: if P = T₁ + T₂ + ... + Tₘ and Q = S₁ + S₂ + ... + Sₙ, then
- **Term-product rule:** multiply the constants and *add* the powers of each variable that appears.
  - T = 5x²y³, S = −16xyz⁵ ⟹ T × S = (5)(−16)·x²⁺¹·y³⁺¹·z⁰⁺⁵ = −80 x³y⁴z⁵.
- (i) Sum P + Q = (4x² − 4x²) + (−3xy − 3xy) + (5y + 5y²) = −6xy + 5y + 5y² = −6xy + 5y(1 + y) = y[−6x + 5(1+y)]
- (ii) Difference P − Q = [4x² − 3xy + 5y] + [4x² + 3xy − 5y²] = 8x² + 5y − 5y² = 8x² + 5y(1 − y).

### ⚠️ Common Mistakes
- ❌ Combining 17x²y³ with −39x³y² (unlike) → ✅ Cannot simplify as single term.
- ❌ Multiplying powers instead of adding when doing term × term → ✅ Add the exponents of each variable.

**Quick Recall:**
- Add/subtract: collect like terms.
- Multiply terms: multiply coefficients, **add** exponents per variable.
- Multiply polynomials: distribute every term against every term, then collect.
- Continues into: 2.3 Solving polynomial equations.

### Solving Polynomial Equations — Linear (2.3, 2.3.1, 2.3.2) 🔴
- **Linear equation** in one/two/more variables: every variable-bearing term has degree 1. ⭐
  - 3 − 29x = 5x + 17 (linear in 1 var)
  - 7y − 29x = 5x + 17 (linear in 2 vars)
  - x + 2z − 7y = 17 (linear in 3 vars)
- **NOT linear:**
  - 3 − 29x² = 5x + 17 (degree 2)
  - 45 = 27 + 18 (no variable)
  - xy = x + 55 (product of variables)
  - log x + 17 = 0; eˣ = x + 25 (transcendental functions, not even polynomial)
- **System of linear equations**: two or more linear equations in two or more variables; a solution is a tuple satisfying all equations simultaneously. ⭐
- **Quadratic equation in one variable y**: at least one term has y² (with non-zero coefficient); other terms are constants or constant multiples of y. General form: ay² + by + c = 0, a ≠ 0.
1. Move all variable terms to one side (typically LHS), all constants to the other (RHS).
2. When a term switches sides, its sign flips (+ ↔ −).

**Reducing non-linear to linear (with caveat)**
- (i) is NOT defined at x = 1/2.
- Cross-multiply: 3x + 2 = 2(2x − 1) ... (ii)
- (ii) IS defined at x = 1/2; (i) and (ii) are equivalent **except** at x = 1/2.
- Solve (ii): 3x − 4x = −2 − 2 = −4 ⟹ −x = −4 ⟹ x = 4.
- Since 4 ≠ 1/2, x = 4 is also a solution of (i). ✓
| Case | Condition | Result |
|------|-----------|--------|
| (a) | a = 0, b = 0 | reduces to c = 0; not linear; may be false |
| (b) | a = 0, b ≠ 0 | by = c — linear in one variable |
| (c) | a ≠ 0, b = 0 | ax = c — linear in one variable |
| main | a ≠ 0, b ≠ 0 | y = (−ax + c)/b; **infinitely many** (x, y) solutions |
- Continues into: 2.3.3 Systems of equations; 2.3.4 Quadratics

### 2.3.3 System of Two Linear Equations in Two Variables 🔴
1. Multiply (i) by d (the coefficient of x in (ii)), and (ii) by (−a) (or by a and subtract).
2. Add corresponding terms → equation in y only.
3. Solve for y.
4. Substitute y back into either original equation to get x.
- Multiply (iii) by 2: 6x − 10y = −18  ...(iii′)
- Multiply (iv) by 3: 6x + 9y = 39    ...(iv′)
- (iii′) − (iv′): −10y − 9y = −18 − 39 ⟹ −19y = −57 ⟹ y = 3.
- Substitute y = 3 in (iii): 3x − 5(3) = −9 ⟹ 3x = 6 ⟹ x = 2.
- Unique solution: (x, y) = (2, 3). ✓
- Continues into: 2.3.4 Quadratic equations; matrices/determinants in later units.

### 2.3.4 Quadratic Equations 🔴

**Quadratic Formula**
- Continues into: Chunk 007 (discriminant cases, worked examples)
- Builds on: linear equations (2.3.1, 2.3.2, 2.3.3)

### Quadratic Equation — Three Discriminant Cases (continued from 2.3.4) 🔴
| Discriminant | Nature of roots | Roots |
|--------------|----------------|-------|
| b² − 4ac = 0 | two identical real roots | x = −b/(2a) (double) |
| b² − 4ac > 0 | two distinct real roots | x = [−b ± √(b² − 4ac)]/(2a) |
| b² − 4ac < 0 | two distinct complex roots | x = [−b ± i√(4ac − b²)]/(2a) |

### ⚠️ Common Mistakes
- ❌ Forgetting the ± when extracting square root → ✅ Quadratic always yields two roots (counting multiplicity).
- ❌ Treating D = 0 as "no solution" → ✅ It means a *single repeated* real solution.

**Quick Recall:**
- D = b² − 4ac (discriminant).
- D > 0 real distinct; D = 0 real coincident; D < 0 complex.
- Complex roots of a real-coefficient quadratic always come as conjugate pair.
- Builds on: 2.3.4 (Chunk 006). Builds toward complex numbers (Unit 1, Chunks 001-004).
- **Mathematical Expression** (also called *formula*): a sequence of mathematical terms (constants, variables, parameters, relations, operations) formed by the structuring rules of mathematics. ⭐
- **Variable**: a symbol which can be measured and which may change (e.g. price, interest-rate, wages, quantity-bought, quantity-sold). ⭐

### Appendix — Proof Techniques (Overview) 🔴

**Structure of Any Proof Problem**
1. **Hypotheses** — given facts, axioms, postulates.
2. **Conclusion** — what is to be proved.

**I. Direct Proof**

**Refutation by Counter-Example**

**II. Proof by Contradiction (Indirect Proof)**

**Proof by Contrapositive**

**III. Proof by Cases**
- Case (i): |x| ≥ 3 ⟹ x² ≥ 9 > 8 ⟹ x² + 3y² > 8.
- Case (ii): |y| ≥ 2 ⟹ 3y² ≥ 12 > 8 ⟹ x² + 3y² > 8.
- So |x| ≤ 2 and |y| ≤ 1, i.e., x ∈ {−2, −1, 0, 1, 2}, y ∈ {−1, 0, 1}. Then x² ∈ {0, 1, 4} and 3y² ∈ {0, 3}. Maximum (x² + 3y²) = 7 < 8.
- No solution exists. ∎

**IV. Existence Proofs**
- **Constructive:** Exhibit a specific b such that P(b) is true.
  - *Example:* Any positive integer can be written as a sum of two cubes in two different ways. **1729** = 10³ + 9³ = 12³ + 1³.
- **Non-constructive:** Prove existence without producing the witness explicitly.
  - *Example:* There exist irrationals x, y with xʸ rational.
    - √2 is irrational. Consider (√2)^(√2):
      - **Case (i):** if (√2)^(√2) is rational, take x = y = √2 — done.
      - **Case (ii):** if (√2)^(√2) is irrational, take x = (√2)^(√2), y = √2; then xʸ = ((√2)^(√2))^(√2) = (√2)^2 = 2, rational.
    - Either way, such x, y exist. (We don't compute (√2)^(√2)'s value.)
- **Hypothesis (H)**: the explicitly given assumptions plus implicit ones.
- **Conclusion (C)**: what is to be proved.
- **Contradiction**: a statement of the form S ∧ ¬S (both S true and S false simultaneously) — unacceptable in mathematics.
- **Counter-example**: a single instance falsifying a universal claim.

### ⚠️ Common Mistakes
- ❌ Confusing contrapositive (¬C ⟹ ¬H) with converse (C ⟹ H).
- ❌ Trying many examples to "prove" a universal claim → ✅ Examples confirm but do not prove.
- ❌ In proof by cases, missing a case → ✅ Cases must be *exhaustive*.

**Quick Recall:**
- Direct: H ⟹ C step by step.
- Contradiction: assume ¬C, derive S ∧ ¬S.
- Contrapositive: prove ¬C ⟹ ¬H.
- Counter-example: one suffices to refute a universal claim.
- Existence: produce a witness (constructive) or argue indirectly.
- Continues into: Mathematical Induction & Equivalences (Chunk 008)
- Used implicitly throughout: De Morgan proofs (Chunk 005), set identities (Unit 1).
- When does proof by cases scale poorly? (Answer hint: when the case-space is infinite or unstructured — then induction or invariants help.)

### Appendix V — Proof by Mathematical Induction 🔴

**When to Use Induction**
- This is not one statement but infinitely many: S₁, S₂, S₁₀, S₁₀₀₀, ... — induction proves them all simultaneously.

**Three Steps of Mathematical Induction**
1. **Base / initial step:** Show S₁ is true (or S_t for some starting t).
2. **Induction Hypothesis (IH):** Assume Sₖ is true for an arbitrary k ≥ 1.
3. **Inductive step:** Using the base and IH, show Sₖ₊₁ is true.

### ⚠️ Common Mistakes
- ❌ Skipping the base step → ✅ Without the base, induction "starts on no rung" (one can "prove" false claims).
- ❌ Assuming Sₖ in the goal of the inductive step → ✅ Use Sₖ to derive Sₖ₊₁.
- ❌ Generalising induction to non-well-ordered index sets → ✅ Standard induction needs ℕ; for ℝ use other methods.

**Quick Recall:**
- Three steps: base, hypothesis, inductive.
- Base may start at t > 1 if the claim only holds for n ≥ t.
- Builds on: Direct proof, Section I (Chunk 007).
- Continues into: Proof of Equivalences.

### ⚠️ Common Mistakes
- ❌ Proving only one direction → ✅ "iff" needs both.
- ❌ Using non-reversible steps in a single ⇔ chain → ✅ Each step must itself be biconditional.

**Quick Recall:**
- "iff" / "⇔" — both directions.
- Either prove both directions separately, or chain biconditionals.
- **Ordered Set**: a set in which the order of occurrence of elements is significant. Notation: parentheses, e.g., (a, b). Contrast with unordered set {a, b} = {b, a}. Crucially, (a, b) ≠ (b, a) in general. ⭐
  - X × Y = {(x, y) : x ∈ X, y ∈ Y}. ⭐

### 3.2 Relation — Definition, Notation, and Examples (3.2.1) 🔴

**Definition**
- *is-mother-of* = {(m, c) : m ∈ X, c ∈ Y, m is mother of c} ⊆ X × Y, where X = Y = {humans}.
- *is-less-than* (on ℕ) = {(x, y) : x, y ∈ ℕ, x < y} ⊆ ℕ × ℕ.

**Two notations for a relation**
- **Set-builder form:** describes the property and gives R as a subset, e.g., is-mother-of = {(m, c) : m is mother of c}.
- **Roster form:** lists pairs explicitly, e.g., is-less-than = {(1,2), (1,3), ..., (2,3), (2,4), ...}.

**Arity of a Relation**
| Arity | Args | Example |
|-------|------|---------|
| **Unary** (= property) | 1 | is-male, is-prime-number |
| **Binary** | 2 | is-mother-of, is-less-than |
| **Ternary** | 3 | is-integer-strictly-between(x, y, z); are-parents-of(x, y, z); (item, cost, price) in economics |
| **Quaternary** | 4 | timetable: (class, subject, teacher, room) |
| **n-ary** | n | R ⊆ X₁ × X₂ × ... × Xₙ |

**Standard Definitions for Binary Relations R ⊆ X × Y**
- **Domain** = X (the source set).
- **Codomain** = Y (the target set).
- **Range** = {y ∈ Y : ∃ x ∈ X, (x, y) ∈ R} — the actually-used part of the codomain.
  - Example: R = (Person, 10-digit-Mobile-Number); domain = all persons; codomain = all 10-digit naturals; range = the 10-digit numbers actually used as someone's mobile number.
- **Image** of x ∈ X under R: any y ∈ Y with (x, y) ∈ R. Note: a relation may give multiple images.
- **Relation on X**: a binary relation where domain = codomain = X. (i.e., R ⊆ X × X.)
- **Onto relation**: every y ∈ Y appears as a second component of some pair in R.
  - is-mother-of is onto (every person has a mother).
  - (Person, Mobile-Number) is NOT onto (not every 10-digit number is a mobile number).
- **One-to-one relation**: distinct elements of the domain have distinct images.
  - (Person, Mobile-Number) is one-to-one (no two persons share a mobile number).
- **Empty relation**: R = ∅ ⊆ X × Y; no element of X relates to any element of Y. Example: X = {0..9}, R = {(a, b) : a − b = 10} — empty (no decimal digits differ by 10).
- **Universal relation**: R = X × Y; every element of X relates to every element of Y.
- Empty and universal are sometimes called **trivial relations**.

**Notations Re-visited**
- (x, y) ∈ R, or
- x R y.
- **Graph** (vertices and arrows). Fig. 3.2 illustrates.
- **Matrix** representation.
- **Relation from X to Y**: any subset of X × Y. ⭐
- **Domain / Codomain / Range** as above. ⭐
- **Image of x under R**: y such that (x, y) ∈ R.
- **Relation on X**: relation with domain = codomain = X.
- **Onto relation**: range = codomain.
- **One-to-one relation**: distinct domain elements have distinct images.
- **Empty relation**: ∅ ⊆ X × Y.
- **Universal relation**: X × Y.
| Type | Defining property |
|------|------------------|
| Empty | R = ∅; no element related to any |
| Universal | R = X × Y; every element related to every |
| Onto | Range = Codomain |
| One-to-one | Distinct domain elements have distinct images |

### ⚠️ Common Mistakes
- ❌ Treating (a, b) and (b, a) as the same → ✅ Ordered pairs differ unless the relation is symmetric.
- ❌ Confusing range with codomain → ✅ Range ⊆ codomain; equality holds only for onto relations.
- ❌ Saying "every relation is a function" → ✅ Functions are a *special* kind of relation (each domain element has *exactly one* image).
- Cross-product is defined for non-empty X and Y.
- An n-ary relation generalises by being a subset of X₁ × ... × Xₙ.

**Quick Recall:**
- Relation ⇔ subset of cross-product.
- Cross-product X × Y = ordered pairs (x, y) with x ∈ X, y ∈ Y.
- Domain (input set) / Codomain (target set) / Range (actually hit subset).
- Onto: range = codomain. One-to-one: injective on domain.
- Empty and universal are trivial relations.
- Builds on: Sets, subsets, ordered pairs (Unit 1, Chunks 001-004).
- Continues into: 3.2.2 Properties of Relations (reflexivity, symmetry, transitivity); 3.3 Function definition.
- Exactly when does a binary relation R on X qualify as a function? (Preview: when each x ∈ X has exactly one image — covered in 3.3.2.)
- How does the matrix representation interact with composition of relations? (Preview: matrix product in {0,1}-arithmetic.)

### Reflexive, Not-Reflexive, Anti-Reflexive 🔴
- **Reflexive**: R on X is reflexive if for every a ∈ X, (a,a) ∈ R. ⭐
- **Not-reflexive**: there exists at least one a ∈ X with (a,a) ∉ R. ⭐
- **Anti-reflexive / irreflexive**: for every a ∈ X, (a,a) ∉ R. ⭐
| Property | Quantifier | Condition |
|---|---|---|
| Reflexive | ∀ a ∈ X | (a,a) ∈ R |
| Not-reflexive | ∃ a ∈ X | (a,a) ∉ R |
| Anti-reflexive | ∀ a ∈ X | (a,a) ∉ R |
- Equality (=) on N = {1,2,3,...}.
- "is-sibling-of" on the set of all human beings.
- The universal relation on X.
- On N: define (a,b) ∈ R iff a × b is even. Then 1 × 1 = 1 is odd, so (1,1) ∉ R, hence not reflexive. But (2,2) ∈ R, so not anti-reflexive either.
- "is-brother-of" on all humans: fails for females (Sheela is not her own brother), but holds for males.
- "is-less-than" (<) on numbers (x < x is always false).
- "is-mother-of" on humans.
- R = {(2,3),(3,1),(2,1)} on {1,2,3}.
- Just changing the underlying set X can change the property:
  - "is-brother-of" on males → reflexive; on females → anti-reflexive.
  - Product-is-even on integers: reflexive on even integers, anti-reflexive on odd integers, neither on all integers.

### ⚠️ Common Mistakes
- ❌ Treating "not-reflexive" as a synonym for "anti-reflexive" → ✅ Not-reflexive needs only one failure; anti-reflexive needs every element to fail.
- ❌ Forgetting that the empty relation on a non-empty set is not reflexive → ✅ Reflexivity requires (a,a) for every a; ∅ has no pairs.

**Quick Recall:**
- Reflexive: every (a,a) is in R.
- Anti-reflexive: no (a,a) is in R.
- Not-reflexive: at least one (a,a) is missing from R.
- Anti-reflexive ⇒ not-reflexive; converse fails.
1. R on X = {1,2,3,4}, R = {(1,2),(2,1),(2,3),(3,1),(3,2),(3,4),(4,3)} — give graphic and matrix representation.
2. Classify (reflexive / not-reflexive / anti-reflexive):
   - is-congruent-to on triangles → **reflexive**.
   - ≤ on numbers → **reflexive**.
   - < on N → **anti-reflexive**.

### Symmetric, Not-Symmetric, Antisymmetric, Asymmetric 🔴
- **Symmetric**: ∀ a, b ∈ X, (a,b) ∈ R ⇒ (b,a) ∈ R. ⭐
- **Not-symmetric**: ∃ a, b ∈ X with (a,b) ∈ R but (b,a) ∉ R. ⭐
- **Antisymmetric**: if (a,b) ∈ R and (b,a) ∈ R, then a = b. ⭐
|---|---|---|
| Symmetric | ∀ pairs | (a,b) ∈ R ⇒ (b,a) ∈ R |
| Not-symmetric | ∃ pair | (a,b) ∈ R but (b,a) ∉ R |
| Antisymmetric | ∀ pair, a ≠ b | (a,b) ∈ R ⇒ (b,a) ∉ R |
- A relation can be both symmetric AND antisymmetric. This happens when R contains only pairs of the form (a,a). Example: {(1,1),(2,2)}.
- Every antisymmetric relation is not-symmetric (provided it has any off-diagonal pair); but not-symmetric doesn't imply antisymmetric. Counter-example: R = {(a,b),(a,c),(c,a)} is not-symmetric (because (b,a) ∉ R), but not antisymmetric (since (a,c), (c,a) both in R yet a ≠ c).

**Quick Recall:**
- To prove symmetric: assume (a,b) ∈ R, show (b,a) ∈ R.
- To disprove symmetric: produce one pair (a,b) ∈ R with (b,a) ∉ R.
- Antisymmetric ≠ "not symmetric"!
- is-congruent-to on triangles → **symmetric**.
- ≤ on numbers → **not symmetric** (3 ≤ 4 but 4 ≰ 3); also **antisymmetric**.
- is-brother-of on all males → **symmetric** (every male is his own brother by the formal definition); **not antisymmetric**.

### Transitive, Not-Transitive, Anti-Transitive 🔴
- **Transitive**: ∀ a,b,c ∈ X, (a,b) ∈ R ∧ (b,c) ∈ R ⇒ (a,c) ∈ R. ⭐
- **Not-transitive**: ∃ a,b,c with (a,b),(b,c) ∈ R but (a,c) ∉ R. ⭐
- **Anti-transitive**: ∀ a,b,c with (a,b),(b,c) ∈ R, we have (a,c) ∉ R. ⭐
- "is-perpendicular-to" on lines in a plane (a ⊥ b, b ⊥ c ⇒ a ∥ c, so a ⊥̸ c).
- is-mother-of (also anti-transitive).
- On {1,2,3}: R = {(1,2),(2,3),(3,1)} — every chain breaks.
- Anti-transitive ⇒ not-transitive (provided some chain a→b→c exists), but not-transitive doesn't imply anti-transitive.
- Counter-example: R = {(1,2),(2,3),(1,3),(3,2)} on {1,2,3}: not transitive ((2,3),(3,2) ∈ R but (2,2) ∉ R), but not anti-transitive ((1,2),(2,3),(1,3) all in R).

**Quick Recall:**
- Transitive: every chain closes.
- Anti-transitive: every chain breaks.
- Not-transitive: at least one chain breaks.
- "Angle between lines a and b is 30°" → **not transitive** (b can rotate relative to a, then to c, total angle could be 60°).
- ≤ on numbers → **transitive**.
- is-brother-of on all humans → **transitive**.

### ⚠️ Common Mistakes
- ❌ Adding pairs without checking if they re-introduce a property you wanted to break → ✅ After each addition, recheck all required properties.
---

### Equivalence Relations & Partition of a Set 🔴
- **Equivalence relation**: R on X is an equivalence relation iff R is reflexive, symmetric, and transitive. ⭐
- **Equivalence class** of a under R: [a] = {x ∈ X : (x,a) ∈ R}. ⭐
- **Partition of X**: a non-empty collection P = {Xᵢ} of subsets of X such that
  1. Xᵢ ≠ ∅ for each i,
  2. Xᵢ ∩ Xⱼ = ∅ for distinct i, j,
- 3. ⋃ Xᵢ = X. ⭐
- Equality (=) on Q.
- "is-parallel-to" on lines in a plane.
- "is-congruent-to" on triangles.
- "is-sibling-of" on humans.
1. {{a},{b},{c}}
2. {{a},{b,c}}
3. {{a,b},{c}}
4. {{b},{a,c}}
5. {{a,b,c}}
1. **Reflexive**: x and x are in the same class ⇒ (x,x) ∈ R.
2. **Symmetric**: x,y same class ⇒ y,x same class ⇒ (y,x) ∈ R.
3. **Transitive**: (x,y) and (y,z) ∈ R ⇒ x,y in Aᵢ; y,z in Aⱼ. Since y ∈ Aᵢ ∩ Aⱼ and partition pieces are disjoint, Aᵢ = Aⱼ, so x,z share a class ⇒ (x,z) ∈ R.
- **Fails reflexive**: X = {1,2,3}, R = {(2,2),(3,3),(2,3),(3,2)} — (1,1) ∉ R. (Symmetric and transitive but not reflexive.)
- **Fails symmetric**: R = {(1,1),(2,2),(3,3),(2,3)} — (3,2) ∉ R. (Reflexive and transitive but not symmetric.)
- **Fails transitive**: R = {(1,1),(2,2),(3,3),(1,2),(2,1),(2,3),(3,2)} — (1,2),(2,3) ∈ R but (1,3) ∉ R. (Reflexive and symmetric but not transitive.)

**Quick Recall:**
- Equivalence ⇔ reflexive + symmetric + transitive.
- Equivalence relation on X ↔ partition of X (one-to-one correspondence).
- The three properties are independent — none implies any other.
1. The three properties are independent. Examples:
   - **Reflexive only**: on Z, (a,b) ∈ R iff 0 ≤ a − b < 1. (Not symmetric: (4,3) ∈ R, (3,4) ∉ R; not transitive.)
   - **Symmetric only**: "is-perpendicular-to" on lines in a plane.
   - **Transitive only**: < on rationals.
2. Partition from R = {(1,1),(2,2),(3,3),(4,4),(1,3),(3,1),(2,4),(4,2)} on {1,2,3,4} → **{{1,3},{2,4}}**.
- Foundation for partial orders (next section).
- Prerequisite for: modular arithmetic, quotient sets, group cosets in advanced courses.

### Partial Order Relations & Posets 🔴
- **Partial order**: R on X is reflexive, antisymmetric, and transitive. ⭐
- **Poset**: ordered pair (X, R) where R is a partial order on X.
- **Total order**: a partial order where every pair is comparable, i.e. (x,y) ∈ R or (y,x) ∈ R for all x,y. ⭐
- ≤ on Q (rationals) — partial order.
- ⊆ (subset-of) on the power set of a set — partial order.
- "is-divisor-of" on N — partial order.
- "is-divisor-of" on {1, p, p², p³, ...} for prime p — total order.
- In ⊆ on subsets, {a,b,c} and {b,c,d} are **incomparable**: neither is a subset of the other.
- Under is-divisor-of: 5 and 9 are incomparable (5 ∤ 9, 9 ∤ 5).
- Builds on antisymmetric (above).
- Prerequisite for: Hasse diagrams (Chunk 010), lattices, order theory.
- For a relation that is reflexive and antisymmetric but not transitive, is the resulting graph a poset? (No — transitivity is required.)
- How many distinct partial orders exist on a 3-element set?

### Hasse Diagrams & Special Elements of a Poset 🔴
- **Hasse diagram**: graphical representation of a finite poset (X, R); draw an upward line from x to y whenever (x,y) ∈ R (after suppressing reflexive loops and edges implied by transitivity).
- **Minimal element**: a ∈ X such that there is no x ∈ X (x ≠ a) with (x, a) ∈ R, i.e. nothing is strictly "below" a. ⭐
- **Maximal element**: a ∈ X such that there is no y ∈ X (y ≠ a) with (a, y) ∈ R, i.e. nothing is strictly "above" a. ⭐
- **Minimum / least element**: the unique minimal element when only one exists.
- **Maximum / greatest element**: the unique maximal element when only one exists.
- A poset can have multiple minimal or maximal elements.
- "Minimum/least" exists only when there is exactly **one** minimal element; same for maximum.
- Reflexive self-loops and transitively-derived edges are NOT drawn in a Hasse diagram (otherwise it would be cluttered and uninformative).

**Quick Recall:**
- Minimal = nothing below it in R.
- Maximal = nothing above it in R.
- Least/greatest = unique minimal/maximal.
1. X = divisors of 30 = {1,2,3,5,6,10,15,30} → minimal = 1, maximal = 30.
2. X = divisors of 24 = {1,2,3,4,6,8,12,24} → minimal = 1, maximal = 24.
3. X = divisors of 60 → minimal = 1, maximal = 60.
4. X = divisors of 32 = {1,2,4,8,16,32} → minimal = 1, maximal = 32 (this is a chain, hence totally ordered).
- Builds on partial order (Chunk 009).
- Prerequisite for: lattices, lub/glb concepts.

### Operations on Relations 🔴
- **Set-type operations**: union (R ∪ S), intersection (R ∩ S), difference (R − S), complement (Rᶜ = U − R, where U is the universal relation X × Y).
- **Inverse R⁻¹**: from Y to X, where (y,x) ∈ R⁻¹ iff (x,y) ∈ R.
- **Composition R ∘ S** (with cod(R) = dom(S)): new relation from dom(R) to cod(S) such that (x,z) ∈ R ∘ S iff ∃ y with (x,y) ∈ R and (y,z) ∈ S. ⭐
- **Reflexive closure** of R: smallest reflexive relation containing R; add all (x,x) not yet in R.
- **Symmetric closure** of R: smallest symmetric relation containing R; for each (x,y) ∈ R add (y,x) if missing.
- **Transitive closure** of R: smallest transitive relation containing R; add all chains-of-pairs implied by composing R with itself.
- R = {(1,a),(2,a),(2,c),(3,b),(4,b),(4,c)}
- S = {(1,b),(2,a),(3,a),(3,b),(4,a)}
- Universal U: 4 × 3 = 12 pairs.
| Op | Result |
|---|---|
| R ∪ S | {(1,a),(2,a),(2,c),(3,b),(4,b),(4,c),(1,b),(3,a),(4,a)} |
| R ∩ S | {(2,a),(3,b)} |
| R − S | {(1,a),(2,c),(4,b),(4,c)} |
| S − R | {(1,b),(3,a),(4,a)} |
| Rᶜ | {(1,b),(1,c),(2,b),(3,a),(3,c),(4,a)} |
- **Reflexive closure**: add (1,1) → {(2,2),(3,3),(2,3),(3,1),(1,1)}.
- **Symmetric closure**: add (3,2) and (1,3) → {(2,2),(3,3),(2,3),(3,1),(3,2),(1,3)}.
- **Transitive closure**: chain (2,3),(3,1) ⇒ add (2,1) → {(2,2),(3,3),(2,3),(3,1),(2,1)}.

### ⚠️ Common Mistakes
- ❌ Confusing inverse R⁻¹ with complement Rᶜ → ✅ R⁻¹ swaps coordinates of each pair; Rᶜ contains pairs **not** in R.
- ❌ Adding too many pairs in closure → ✅ Closures are "minimal" — add only what's needed.
- ❌ Composing relations when codomain of R ≠ domain of S → ✅ Composition R ∘ S requires cod(R) = dom(S).

**Quick Recall:**
- Closure = minimum extra pairs to enforce the property.
- R⁻¹: swap each (x,y) → (y,x).
- Composition: chain through a middle element y.
- Builds on set operations from Unit 1.
- Prerequisite for: function composition, group operations.

### Function — Formal Definition 🔴
- **Function f: X → Y**: rule associating to each x ∈ X a unique y ∈ Y, written y = f(x). ⭐
- **Domain** of f: the set X.
- **Codomain** of f: the set Y.
- **Image** of x under f: f(x); equivalently, "value of x under f".
- **Pre-image** of y: any x with f(x) = y.
- **Range** of f: {f(x) : x ∈ X} ⊆ Y — the actual outputs achieved.
- **Map / mapping**: synonyms for function.
- **Real function**: any function whose domain is R (or a subset of R).
- **Real-valued function**: any function whose codomain is R.
- **Complex-valued, integer-valued, rational-valued**: codomain is C, Z, Q respectively.
| | Relation | Function |
|---|---|---|
| Each x in domain | may have any number of partners | must have exactly one partner |
| Each y in codomain | unrestricted | unrestricted (may have zero or many pre-images) |
- Area of rectangle: A_Rect = f₁(l, b) = l × b.
- Volume of container: v = f₂(l, b, h) = l × b × h.
1. **f: N → N, f(x) = 2x + 1**. For each x ∈ N, 2x + 1 ∈ N and unique → function. ✓
2. **f: Z → N, f(x) = x² + 3**. For each x ∈ Z, x² + 3 ∈ N → function. ✓
3. **f: Z → N, f(x) = x² − 3**. For x = 0, x² − 3 = −3 ∉ N → **not a function** (image escapes the codomain). ✗
4. **f: Z → Z, f(x) = x² − 3**. Now image is in Z → function. ✓ (Note: changing codomain converted a non-function into a function.)

### ⚠️ Common Mistakes
- ❌ Forgetting that the image must lie in the codomain → ✅ A rule like f(x) = √x is NOT a function from Z to N (negative inputs have no real square root).
- ❌ Reading "→" in f: X → Y as logical implication → ✅ "→" here is just notation: X is on the left (domain), Y on the right (codomain).

**Quick Recall:**
- Function = relation + (existence + uniqueness of image).
- Range ⊆ Codomain (range may be a strict subset).
- Same rule + different codomain can change "function or not".
---

**Quick Recall:**
- An "operation" is a function whose domain is a (Cartesian power of) the codomain.

### Injective Functions 🔴
- **Injective (1-1)**: f: X → Y is injective if x₁ ≠ x₂ ⇒ f(x₁) ≠ f(x₂). Equivalently, f(x₁) = f(x₂) ⇒ x₁ = x₂. ⭐
1. Assume f(x) = f(y) for arbitrary x, y in domain.
2. Manipulate algebraically to deduce x = y.
3. Conclude f is injective.
1. **f: N → N, f(x) = 2x + 1.** Suppose f(x) = f(y): 2x + 1 = 2y + 1 ⇒ x = y. ✓ Injective.
2. **f: N → R, f(x) = √x.** f(x) = f(y) ⇒ √x = √y ⇒ x = y (squaring). ✓ Injective.
3. **f: N → R, f(x) = x².** f(x) = f(y) ⇒ x² = y² ⇒ x = ±y. But −y ∉ N, so x = y. ✓ Injective on N.
4. **f: Z → R, f(x) = x²** is **NOT** injective: f(2) = f(−2) = 4.

### Surjective (Onto) Functions 🔴
- **Surjective (onto)**: f: X → Y is surjective if for every y ∈ Y, there exists x ∈ X with f(x) = y. ⭐
1. Take an arbitrary y in codomain Y.
2. Solve f(x) = y for x in terms of y.
3. Verify the solved x lies in domain X.
4. If yes for all y, f is surjective; if any y has no x in X, f is not surjective.
- **f: N → N, f(x) = 2x + 1.** For y = 4 in N, x = 3/2 ∉ N → **not surjective**.
- **Mod: Z → N**, Mod(x) = |x|. For y ∈ N, x = y ∈ Z gives Mod(x) = y. ✓ Surjective.
- **f: Z → C, f(x) = √x (positive root).** Take y = 3.75 ∈ C; we need x = (3.75)² = 14.0625 ∉ Z → **not surjective**.
- **f: C → C, f(x) = √x.** Surjective (every complex number is a square root of its square).

### Bijective Functions / 1-to-1 Correspondence 🔴
- **Bijective**: injective + surjective. ⭐
- **1-to-1 correspondence**: synonym for bijective.
- A bijection between X and Y means |X| = |Y| (when finite), and both sets have "the same size" in general (cardinality).

**Quick Recall:**
- Injective: distinct inputs → distinct outputs (no collisions).
- Surjective: every codomain element is hit (range = codomain).
- Bijective: both — perfect pairing.
1. Domain & range of (i) f(x) = −|x|; (ii) f(x) = +√(9 − x²).
2. f(x) = 2x − 5: compute f(0), f(7), f(−3).
3. Function or not? (i) f: N → N, f(x) = x − 3; (ii) f: N → Z, f(x) = x − 3.
- Builds on relations (chunk 009).
- Prerequisite for: invertibility (a function has an inverse iff it is bijective), composition (chunk 010 set-type ops), graphing functions (Unit 4 / chunk 011-012).
- For finite sets, when does injective ⇒ surjective?
- How do we test bijectivity graphically? (Hint: vertical line test + horizontal line test, treated in Unit 4.)
- **Equivalence Relation**: R on X is reflexive, symmetric, and transitive simultaneously: (i) ∀x ∈ X, (x,x) ∈ R; (ii) (x,y) ∈ R ⇒ (y,x) ∈ R; (iii) (x,y) ∈ R ∧ (y,z) ∈ R ⇒ (x,z) ∈ R. ⭐
- **Equivalence Class**: [a] = {x : (x,a) ∈ R} for an equivalence relation R. ⭐
- **Function**: f: X → Y, a rule associating each x ∈ X with a unique y ∈ Y, written y = f(x). ⭐
- **Injective Function**: f: X → Y with x₁ ≠ x₂ ⇒ f(x₁) ≠ f(x₂); equivalently f(x₁) = f(x₂) ⇒ x₁ = x₂. ⭐
- **Partition of a Set**: collection P = {Xᵢ} of non-empty mutually disjoint subsets of X whose union is X. ⭐
- **Partial Order Relation**: R on X is reflexive, antisymmetric, and transitive. ⭐
- **Surjective Function**: f: X → Y where for every y ∈ Y there exists x ∈ X with f(x) = y. ⭐

### Answers / Hints to Check Your Progress (CYP 1–6) 🔴
1. R on X = {1,2,3,4} with R = {(1,2),(2,1),(2,3),(3,1),(3,2),(3,4),(4,3)}.
   - **Graphic representation**: arrows between elements as listed.
   - **Matrix representation** (rows/cols indexed 1–4):
     | | 1 | 2 | 3 | 4 |
     |---|---|---|---|---|
     |1| 0 | 1 | 0 | 0 |
     |2| 1 | 0 | 1 | 0 |
     |3| 1 | 1 | 0 | 1 |
     |4| 0 | 0 | 1 | 0 |
2. Classifications:
   - is-congruent-to on triangles → **symmetric** (and also reflexive, transitive).
   - ≤ on numbers → **not symmetric** (3 ≤ 4 true, 4 ≤ 3 false). Also **antisymmetric** (x ≤ y and y ≤ x ⇒ x = y).
   - is-brother-of on all males → **symmetric** (every male is his own brother by formal definition); **not antisymmetric** (for distinct x, y, both brothers of each other).
1. {(1,1),(2,2),(3,3)} is **both symmetric and antisymmetric**.
2. {(1,2),(2,3),(1,3)} is **antisymmetric, not symmetric**.
3. {(1,2),(2,1),(1,3),(3,1)} is **symmetric, not antisymmetric** (since (1,2),(2,1) ∈ R but 1 ≠ 2).
- R defined by "angle between lines a and b = 30°" → **NOT transitive** (chain of two 30° angles can give 60° or 0°).
- ≤ on numbers → **transitive**.
- is-brother-of on all humans → **transitive**.
1. Each property is independent of the other two.
   - **Reflexive only** (not symmetric, not transitive): on Z, define (a,b) ∈ R iff 0 ≤ a − b < 1.
     - Reflexive: 0 = a − a < 1 ✓
     - Not symmetric: (4, 3) ∈ R since 0 ≤ 1 < 1... [OCR unclear — text reads "0 ≤ a − b < 1"; likely meant 0 ≤ a − b ≤ 1 or similar]; (3,4) ∉ R.
     - Not transitive: (4,3) ∈ R, (3,2) ∈ R, but (4,2) ∉ R since 4 − 2 = 2 ≥ 1.
   - **Symmetric only**: "is-perpendicular-to" on lines in a plane.
   - **Transitive only**: < on rationals (Q).
2. Partition of X = {1,2,3,4} from R = {(1,1),(2,2),(3,3),(4,4),(1,3),(3,1),(2,4),(4,2)}: equivalence classes are {1,3} and {2,4}, so partition = **{{1,3}, {2,4}}**.
| Set | Minimal | Maximal |
|---|---|---|
| Divisors of 30 | 1 | 30 |
| Divisors of 24 | 1 | 24 |
| Divisors of 60 | 1 | 60 |
| Divisors of 32 | 1 | 32 |
1. **(i) f(x) = −|x|**: Domain = R; Range = {x ∈ R : x ≤ 0} = (−∞, 0].
2. **(ii) f(x) = +√(9 − x²)**: Domain = [−3, 3] (so 9 − x² ≥ 0); Range = [0, 3].
   - Note: For complex-valued complex function f: C → C, range = domain = C.
3. f(x) = 2x − 5:
   - f(0) = −5
   - f(7) = 9
   - f(−3) = −11
4. **f: N → N, f(x) = x − 3**: not a function (f(0) = −3 ∉ N).
   - **f: N → Z, f(x) = x − 3**: is a function (image always lies in Z).

### Unit 3 — End-of-Unit Exercises (Q1–Q7) 🔴
- (i) R = {(1,1),(2,2),(1,3),(2,3)} on X = {1,2,3}: (3,3) ∉ R → **not reflexive**; (1,1), (2,2) ∈ R → **not anti-reflexive**.
- (ii) is-brother-of on humans: **not reflexive** (fails for females); **not anti-reflexive** (holds for males).
- (i) {(1,1),(2,2),(3,3)} → **both symmetric and antisymmetric**.
- (ii) {(1,2),(2,3),(1,3)} → **antisymmetric, not symmetric**.
- (iii) {(1,2),(2,1),(1,3),(3,1)} → **symmetric, not antisymmetric**.
- (i) {(1,1),(2,2),(3,3)} → **transitive**.
- (ii) {(1,2),(2,3),(1,3)} → **transitive**.
- (iii) {(1,2),(2,1),(1,3),(3,1)} → **not transitive** ((1,2),(2,1) ∈ R but (1,1) ∉ R).
- (i) Reflexive + symmetric, not transitive: R = {(1,1),(2,2),(3,3),(1,2),(2,1),(1,3),(3,1)} — (2,1),(1,3) ∈ R but (2,3) ∉ R.
- (ii) Reflexive + transitive, not symmetric: R = {(1,1),(2,2),(3,3),(1,2),(1,3),(2,3)} — (2,3) ∈ R but (3,2) ∉ R.
- (iii) Symmetric + transitive, not reflexive: R = {(1,1),(2,2)} — (3,3) ∉ R.
- Minimal element = 1.
- Maximal elements = 5, 6, 7, 8, 9, 10 (no element of X strictly above any of them).

**Quick Recall:**
- To prove **not injective**: produce one pair x ≠ y with f(x) = f(y).
- To prove **surjective**: given y in codomain, exhibit x in domain with f(x) = y.

### Vertical Line Test 🔴
- **Vertical line test**: A relationship f(x) is NOT a function of x if some vertical line x = a meets the graph at two or more points.
- The graph of x² + y² = 4 (a circle) **fails** the vertical line test (two y's for most x's) → not a function.
- The graph in Fig. 4.4 (a single curve passing the test) **is** a function.
- Important standard equations that are **not** functions of x: ellipses, circles, sideways parabolas (y² = 4ax).

### ⚠️ Common Mistakes
- ❌ Using the vertical line test to prove something IS a function → ✅ The test detects only failure. Passing the test plus being defined for every x in the domain is needed for it to be a function.

**Quick Recall:**
- Two intersection points with any vertical line ⇒ not a function.
- Some equations like a circle look like nice curves but are NOT functions.
---

### Equation vs Function — How to Tell 🔴
1. Start with the equation, e.g. X² + Y² = 4.
2. Isolate Y² (or whichever variable will be dependent): Y² = 4 − X².
3. Reduce LHS to power 1 by extracting a root: Y = ±√(4 − X²).
4. Check single-value rule:
   - If LHS gives one Y for each X → function.
   - If LHS gives multiple Y's (e.g., the ± above) → relation but NOT function.
1. X² + Y² = 4
2. Y² = 4 − X²
3. Y = ±√(4 − X²)
1. X² + Y² + Z² = 4
2. Z = ±√(4 − X² − Y²)
- Restricting the codomain (e.g., to non-negative reals) can convert a relation back into a function: Y = +√(4 − X²) is a function (the upper semicircle).
- Functions of more than one independent variable are allowed: Z = f(X, Y).

**Quick Recall:**
- Step 1: solve for the dependent variable.
- Step 2: reduce its power to 1.
- Step 3: check whether the result is single-valued.
- Builds on function definition (Chunk 010).
- Prerequisite for: graphing standard curves in 4.2.2 (Chunk 012).
- For y² = x + 5, is this a function? (No — for any x > −5 there are two y values.)

### Cartesian Coordinate System (2D) 🔴
- **x-axis**: the horizontal number line. ⭐
- **y-axis**: the vertical number line. ⭐
- **Origin**: the intersection of the axes; both x = 0 and y = 0 there.
- **Quadrants**: four regions (numbered I, II, III, IV — usually with Roman numerals) bounded by the axes.
- **Abscissa**: the x-value of point P(x, y); perpendicular distance of P from the y-axis.
- **Ordinate**: the y-value of point P(x, y); perpendicular distance of P from the x-axis.
- **Coordinates of P**: the ordered pair (x, y).
- Convention: independent variable on the **horizontal** axis (x); dependent variable on the **vertical** axis (y).
- Order matters: x is **always** written first in the pair (x, y).
- Called "rectangular" because both axes use evenly-spaced scales.
- (2, 3) — 2 right, 3 up (quadrant I).
- (−3, 1) — 3 left, 1 up (quadrant II).
- (−1.5, −2.5) — 1.5 left, 2.5 down (quadrant III).

**Quick Recall:**
- x first, y second.
- Origin = (0, 0).
- Abscissa = horizontal distance; ordinate = vertical distance.
- Builds on real number line (Unit 1).
- Prerequisite for: graphing all functions (later sections).

### Translating Geometric Figures to Algebraic Equations 🔴
1. Place the figure in a coordinate system; record coordinates of any "anchor" points.
2. Pick an arbitrary point P(x, y) on the figure.
3. Apply known geometric facts (similar triangles, Pythagoras, etc.).
4. Solve for the relation between x and y.
- Take P(x, y) outside segment AB; drop perpendicular PQ to x-axis at Q(x, 0).
- Triangles AOB and AQP are similar.
- |AO|/|AQ| = |BO|/|PQ|, i.e. 2/(x − 2) = 2/y.
- Cross-multiplying: 2y = 2(x − 2) ⇒ **y = x − 2**.
| Curve | Equation |
|---|---|
| Circle (centred at origin) | x² + y² = a² |
| Ellipse | (x/a)² + (y/b)² = 1 |
| Parabola | y² = 4ax (a > 0) |
| Hyperbola | (x/a)² − (y/b)² = 1 |
| Rectangular hyperbola | xy = c² |
| Sphere (3D) | (x − a)² + (y − b)² + (z − c)² = d², d > 0 |

**Quick Recall:**
- Circle: sum of squares = constant.
- Ellipse: sum of normalized squares = 1.
- Parabola (right-opening): y² = 4ax.
- Hyperbola: difference of normalized squares = 1.
- Builds on standard formulas from school geometry.
- Prerequisite for: graphing parabola, hyperbola, circle (Section 4.7).

### Graphing Linear Functions 🔴
- **Linear function**: y = f(x) where the highest power of x is 1.
- **Linear equation**: Ax + By + C = 0 with A, B, C constants and degrees of x, y at most 1.
- **t-chart**: a small table of (x, y) values used to plan a plot.
- **x-intercept**: point where graph crosses the x-axis (y = 0).
- **y-intercept**: point where graph crosses the y-axis (x = 0).
1. Pick any two values of x (often x = 0 and one other).
2. Compute corresponding y from y = f(x).
3. Plot the two points; draw a straight line through them.
- **x-intercept**: set y = 0, solve for x.
- **y-intercept**: set x = 0, solve for y.
| x | y = 7 − 5x |
|---|---|
| −1 | 12 |
| 0 | 7 |
| 1 | 2 |
| 2 | −3 |
| 3 | −8 |
- x-intercept: y = 0 ⇒ 3x = 12 ⇒ x = 4 → point (4, 0).
- y-intercept: x = 0 ⇒ 4y = 12 ⇒ y = 3 → point (0, 3).

**Quick Recall:**
- Two points determine a line.
- Intercept method: set the other variable = 0.

### Absolute Value Function 🔴
- **Absolute value**: |x| = x if x ≥ 0; |x| = −x if x < 0; |0| = 0.
- f(x) = |x| is defined piecewise:
  - y = x for x ≥ 0
  - y = −x for x < 0
- y-intercept: f(0) = |−2| = 2 → (0, 2).
- x-intercept: solve |x − 2| = 0 → x = 2 → (2, 0).
- Domain: all real numbers.
- Range: [0, ∞) (modulus is never negative).
- Graph: V-shape with vertex shifted to (2, 0).

### ⚠️ Common Mistakes
- ❌ Using the x-intercept / y-intercept method without checking that the line meets both axes → ✅ For f(x) = |x − 2|, equation y = 0 has solution x = 2 (the unique x-intercept), but the curve has only one y-intercept; intercept-only method may miss the V-corner.
- ❌ Forgetting the range is non-negative → ✅ |x| ≥ 0 always.

**Quick Recall:**
- |x| graph: V at the origin.
- |x − a| graph: V at (a, 0).
- Two linear pieces stitched at the corner.
---

### Step Function (Greatest Integer Function) 🔴
- **Step / staircase function**: piecewise function whose pieces are all constants on adjacent intervals.
1. For any real x, write x = Int-x + Fraction-x with 0 ≤ Fraction-x < 1.
2. Define f(x) = Int-x.
- For x = 5.46: Int-x = 5, Fraction-x = 0.46 → f(5.46) = 5.
- For x = −3.87: Int-x = −4, Fraction-x = 0.13 → f(−3.87) = −4. (Note: floor of a negative non-integer rounds **down** to a more negative integer.)
- The function is defined for all real x but is discontinuous at every integer.
- For piecewise functions in general, domain = union of all sub-domains; range = union of all sub-ranges.

### ⚠️ Common Mistakes
- ❌ Computing Int-x of −3.87 as −3 → ✅ It's −4 (the integer part rounded **down**).

**Quick Recall:**
- Step function = constant on each interval.
- Discontinuous at every step jump.
- Floor of negative: round more negative (−3.87 → −4).
1. Graph y = (−5/3)x − 2 — straight line through (0, −2) and (3, −7).
2. Truck rental: Rs. 25 + Rs. 0.30/mile for 0–500 miles; Rs. 100 + Rs. 0.15/mile for >500 and <1000 miles. Step (piecewise) function:

### ⚠️ Common Mistakes
- ❌ Plotting only 3 points of a quadratic and connecting them with straight lines → ✅ Use a denser t-chart (5–7 points spanning negative and positive x) and draw a smooth curve.
---

### Even and Odd Functions 🔴
- **Even function**: f(−x) = f(x) for all x ∈ domain. ⭐ Graph is symmetric about the y-axis.
- **Odd function**: f(−x) = −f(x) for all x ∈ domain. ⭐ Graph is symmetric about the origin.
- f(x) = x² is even: f(−3) = 9 = f(3).
- f(x) = x³ is odd: f(−3) = −27 = −f(3).
- f(x) = x³ − x is odd: f(−x) = −x³ + x = −(x³ − x) = −f(x).

### ⚠️ Common Mistakes
- ❌ Claiming a function is "either even or odd" → ✅ Most functions are neither (e.g., f(x) = x² + x).

**Quick Recall:**
- Even: f(−x) = f(x); y-axis mirror.
- Odd: f(−x) = −f(x); origin (point) symmetry.
---

### Quadratic Functions 🔴
- **Quadratic function**: f(x) = ax² + bx + c with a ≠ 0.
- **Parabola**: the curve y = ax² + bx + c (or any rotation thereof).
| x | −3 | −2 | −1 | 0 | 1 | 2 |
|---|---|---|---|---|---|---|
| y | 9 | 4 | 1 | 0 | 1 | 4 |
| Sign of a | Parabola opens | Vertex is |
|---|---|---|
| a > 0 | upward | minimum |
| a < 0 | downward | maximum |

### ⚠️ Common Mistakes
- ❌ Connecting only three points of a parabola with straight segments → ✅ A parabola has continuously varying slope; plot more points and draw a smooth curve.
- ❌ Assuming "quadratic ⇒ symmetric about y-axis" → ✅ Only y = ax² is symmetric about the y-axis. The general y = ax² + bx + c is symmetric about the vertical line x = −b/(2a).

**Quick Recall:**
- Parabola: opens up if a > 0, down if a < 0.
- Differences of y for unit steps in x form an arithmetic progression (odd numbers for y = x²).
- Builds on basic algebra (factoring, completing the square — earlier units).
- Prerequisite for: vertex computation (Section 4.4.2.1, next chunk), conic sections (Section 4.7).
- How do you locate the vertex of y = ax² + bx + c without graphing? (Answer: x = −b/(2a) — to be covered in chunk 013, Section 4.4.2.1 Computation of Vertex.)
- How does the parabola's "width" depend on a?

### Vertex Shifting and Axis of Symmetry of Parabolas 🔴

**Vertical Shift**
- Graph of y = x² + 3: same shape as y = x², shifted **up 3 units**; vertex moves to (0, 3).

**Horizontal Shift**
- Graph of y = (x + 3)²: shape unchanged, shifted **left 3 units**; vertex (−3, 0).
- Graph of y = (x − 3)²: shifted **right 3 units**; vertex (3, 0).
- Note the counter-intuitive sign: (x + 3)² shifts LEFT, not right.

**Combined Shift**
- y = (x − 2)² + 1: vertex (2, 1); axis of symmetry x = 2.
| Function form | Vertex | Direction of opening |
|---|---|---|
| y = x² | (0,0) | Upward (a > 0) |
| y = x² + k | (0, k) | Upward |
| y = (x − h)² | (h, 0) | Upward |
| y = (x − h)² + k | (h, k) | Upward |
| y = a(x − h)² + k, a < 0 | (h, k) | Downward |
- **Vertex**: the lowest point on an upward-opening parabola, the highest point on a downward-opening one. ⭐
- **Axis of symmetry**: the vertical line x = h that divides the parabola into two mirror-image halves. ⭐

**Quick Recall:**
- Vertex of y = a(x−h)² + k is (h, k).
- Axis of symmetry: x = h.
- "+k" lifts up; "(x − h)" slides right by h.

### Computing the Vertex of a Generic Quadratic 🔴
1. Start with y = ax² + bx + c.
2. Factor a: y = a[x² + (b/a)x + c/a].
3. Complete the square: y = a[(x + b/2a)² − (b/2a)² + c/a].
4. Replace the constant tail with k: y = a[(x + b/2a)² + k].
5. Minimum (a > 0) or maximum (a < 0) occurs when (x + b/2a)² = 0, i.e., **x = −b/2a**.
6. y-coordinate: substitute x = −b/2a back into the original equation.
| x | y = 3x² + x − 2 |
|---|---|
| −2 | 8 |
| −1 | 0 |
| 0 | −2 |
| 1 | 2 |
| 2 | 12 |

### ⚠️ Common Mistakes
- ❌ Using x = +b/2a → ✅ Use x = −b/2a (note the negative sign).
- ❌ Confusing "axis x = h" with "x-intercept" — the axis is a vertical line, not a point.

**Quick Recall:**
- Vertex x = −b/2a for y = ax² + bx + c.
- Sign of a determines max (a < 0) vs min (a > 0).
---

### Cubic Functions 🔴

**Tracing f(x) = x³**
- **y-intercept**: (0, f(0)) = (0, 0).
- **x-intercept**: solve x³ = 0 → only (0, 0).
- **Domain**: all real numbers.
- **Range**: all real numbers (because leading coefficient is positive, graph goes up on right, down on left).
- **Symmetry**: f(−x) = −f(x), so f is odd; graph is symmetric about origin.
| x | f(x) = x³ |
|---|---|
| −2 | −8 |
| −1 | −1 |
| 0 | 0 |
| 1 | 1 |
| 2 | 8 |
- Connects to economics: cubic total cost curves (TC = aQ³ + bQ² + cQ + d) appear in microeconomic production theory.
- Builds on: odd/even function classification (earlier chunks).
1) **Draw the graph for y = x³ − 2x.** [Solution from answer key: an "S"-shaped curve passing through origin with two extrema.]

### Graphs of Asymptotic Functions — Horizontal & Vertical Asymptotes 🔴
- **Asymptote**: a line that a curve approaches arbitrarily closely as it heads toward infinity. ⭐
- **Horizontal asymptote**: a horizontal line y = L the graph approaches as x → ±∞.
- **Vertical asymptote**: a vertical line x = a the graph approaches as y → ±∞.
- As x → +∞, y → 0⁺ (gets values 1/2, 1/3, 1/10, 1/10000, never quite 0).
- As x → 0⁺, y → +∞.
- Horizontal asymptote: y = 0. Vertical asymptote: x = 0.
- Horizontal asymptote: y = 0. Vertical asymptote: x = 2.
- As x → 2⁻, denominator → 0⁻, fraction → −∞.
- At x = 2 exactly, function is undefined (division by zero).
- As x → 2⁺, fraction → +∞.
- A function can have only horizontal, only vertical, both, or neither.
- (i) y = 1/(x−2) for 0 < x < 2: only x = 2 (vertical asymptote).
- (ii) x = 1/(y−2) for 0 < y < 2: only y = 2 (horizontal asymptote).

**Quick Recall:**
- Horizontal asymptote = behaviour at infinity (y-value).
- Vertical asymptote = where denominator vanishes (x-value).

### Square Root, Exponential, and Logarithmic Functions 🔴

**Square Root Function: f(x) = √x**
- **Domain/Range**: [0, ∞).
- **Intercept**: (0, 0).
- Neither even nor odd; **strictly increasing** on (0, ∞).
- **Economics use**: depicts an isocline (locus where iso-quants relate). Converges to a point where output is maximised and marginal product is zero.

**Exponential Function: y = aˣ (general form), y = eˣ (natural)**
- e ≈ 2.718281828 (Euler's number).
- **Domain**: (−∞, ∞). **Range**: (0, ∞).
- Graph never touches or goes below x-axis (y > 0 always).
- **Applications**: compound interest, population growth, GDP growth, inflation, carbon dating.

**Logarithmic Function: y = log_b x**
- Inverse of exponential: if y = bˣ = f(x), then x = log_b y = g(y), and f(g(y)) = y, g(f(x)) = x.
- **Conditions**: b > 0, b ≠ 1, x > 0.
- **Behaviour**: when b > 1, log values increase; when 0 < b < 1, they decrease.
- Slowly tends to +∞ as x → ∞; tends to −∞ as x → 0⁺.
- **Domain**: positive reals (never zero). **Range**: all real numbers.
- Graph is **asymptotic to the y-axis** (gets close but never touches).

**Three Common Bases**
| Base b | Name | Used in |
|---|---|---|
| 10 | Common (decimal) logarithm | Science, engineering |
| e ≈ 2.718 | Natural logarithm (ln) | Mathematics, physics |
| 2 | Binary logarithm | Computer science |
1) **f(x) = (x+1)/(x−1). Find x and y intercepts.**
   - x-intercept: f(x) = 0 ⇒ x + 1 = 0 ⇒ x = −1. So (−1, 0).
   - y-intercept: f(0) = 1/(−1) = −1. So (0, −1).
2) **Average fixed cost (AFC) curve — why asymptotic?**
   - AFC = TFC/Q. Since TFC is constant, AFC steadily falls as Q increases but never reaches zero (asymptotic to x-axis).

**Quick Recall:**
- √x defined for x ≥ 0.
- eˣ > 0 always; y = 0 is its horizontal asymptote.
- log_b 1 = 0 for any valid base; log graph asymptotic to y-axis.
- **Rational function**: f(x) = g(x)/h(x) where g, h are polynomials and h ≠ 0. ⭐
- **Piecewise function** (split function): a function defined by different equations on different parts of the domain. ⭐
| x | f(x) |
|---|---|
| −4 | −0.25 |
| −2 | −0.5 |
| −1 | −1 |
| −0.1 | −10 |
| −0.01 | −100 |
| 0.01 | 100 |
| 0.1 | 10 |
| 1 | 1 |
| 2 | 0.5 |
| 4 | 0.25 |
| x | y = x² − 2 |
|---|---|
| −4 | 14 |
| −3 | 7 |
| −2 | 2 |
| −1 | −1 |
| 0 | −2 |
| 1 | −1 |
| x | y = −2x + 4 |
|---|---|
| 1 | 2 |
| 2 | 0 |
| 3 | −2 |
| 4 | −4 |

### ⚠️ Common Mistakes
- ❌ Forgetting to exclude x-values where the denominator vanishes from the domain.
- ❌ Plotting both pieces of a piecewise function on the wrong interval — always restrict each formula to its prescribed range.

### Continuous vs Discontinuous Functions 🔴
- **Continuous function**: a function whose graph can be drawn without lifting the pen. ⭐
- **Discontinuous function**: a function that does not vary continuously through some value(s) of the variable. ⭐

**1. Asymptotic Discontinuity 🔴**
| x | y |
|---|---|
| 0.25 | −0.687 |
| 0.5 | −1.059 |
| 0.75 | −2.171 |
| 1.0 | Undefined |
| 1.25 | 2.270 |
| 1.5 | 1.158 |
| 1.75 | 0.786 |

**2. Point Discontinuity 🔴**

**3. Jump Discontinuity 🔴**
- **First branch**: has x in the denominator → asymptotic discontinuity at **x = 0**.
- **At x = 2**: left branch → (2 + 4)/2 = 3; right branch → 2² + 1 = 5. Different values → **jump discontinuity at x = 2**.
- No other discontinuities.

### ⚠️ Common Mistakes
- ❌ Calling all breaks "asymptotic" → ✅ Distinguish: asymptotic (→ ±∞), point (single hole), jump (finite leap).
- ❌ Forgetting to test denominators of every piece in piecewise functions.
1) **Draw graph of f(x) = −x³ + 4.** [From answer key: write as ax³ + c with a = −1, c = 4. Reflect y = x³ across x-axis (because a = −1) and translate up 4 units.]

**Quick Recall:**
- 3 discontinuity types: asymptotic, point, jump.
- Hole at x = a where g(x) = h(x)·(x − a) cancels.
- Continuous if pieces of a piecewise function meet at the boundary.

### Hyperbola — Equations, Vertices, Foci, Asymptotes 🔴
- **Hyperbola**: set of all points where the **difference** of distances to two fixed foci is constant. ⭐
- **Transverse axis**: axis of symmetry passing through both foci and the centre.
- **Conjugate axis**: axis of symmetry perpendicular to the transverse axis through the centre.
- **Vertices**: the two points where the hyperbola crosses its transverse axis.
- **Horizontal hyperbola**: (x − h)²/a² − (y − v)²/b² = 1
- **Vertical hyperbola**: (y − v)²/a² − (x − h)²/b² = 1
| Feature | Horizontal hyperbola | Vertical hyperbola |
|---|---|---|
| Transverse axis | y = v (horizontal) | x = h (vertical) |
| Conjugate axis | x = h | y = v |
| Vertices | (h ± a, v) | (h, v ± a) |
| Foci | (h ± F, v) | (h, v ± F) |
1. Mark the centre (h, v).
2. From centre, mark a-distance along transverse axis (vertices) and b-distance along conjugate axis.
3. Draw a rectangle with sides through these four points (parallel to x- and y-axes).
4. Draw the diagonals of the rectangle extended — these are the **asymptotes**.
5. Sketch each branch starting at a vertex, hugging the asymptotes farther out.
- Centre: (h, v) = (−1, 3).
- a² = 16 ⇒ a = 4 (vertical direction, since under y).
- b² = 9 ⇒ b = 3 (horizontal direction).
- Vertices: (−1, 3 + 4) and (−1, 3 − 4) = **(−1, 7) and (−1, −1)**.
- Foci: a² + b² = F² ⇒ 16 + 9 = 25 ⇒ F = 5. Foci: (−1, 3 + 5) and (−1, 3 − 5) = **(−1, 8) and (−1, −2)**.
- a may be greater than, less than, or equal to b (unlike an ellipse).
- The curves never cross the asymptotes.
- If the equation is not in standard form, **complete the square** to put it there before identifying parameters.
- **Portfolio theory / efficient frontiers**: combinations of risk and return often shaped as partial hyperbolas.
- **Production frontiers**: combinations of capital and labour producing a given output.

**Quick Recall:**
- F² = a² + b² (note: opposite of ellipse, where it's F² = a² − b²).
- Vertices at distance a along transverse axis.
- Asymptotes are the rectangle's diagonals extended.
| Feature | Parabola | Hyperbola |
|---|---|---|
| Definition | Locus of points equidistant from a fixed focus and a fixed directrix line | Locus of points where difference of distances to two foci is a positive constant |
| Number of foci | 1 | 2 |
| Standard equation (simple) | y² = x | xy = 1 |
| Shape variability | All parabolas same shape (only scaled) | Hyperbolas have different shapes |
| Arm behaviour at infinity | Two arms become parallel | Arms diverge (do not become parallel) |

### Rectangular Hyperbola 🔴
- **Rectangular hyperbola**: a hyperbola for which the asymptotes are perpendicular (orthogonal). ⭐

**Two Types based on parity of n in y = 1/xⁿ**
- **n = 2k + 1 (n odd)**: e.g., y = 1/x. Branches lie in opposite quadrants.
- **n even**: e.g., y = 1/x². Branches lie in the same upper half (both positive y when n = 2).

**Properties of Rectangular Hyperbola y = 1/xⁿ**
1. Vertical asymptote at x = 0.
2. Horizontal asymptote at y = 0.
3. No stationary points.
4. No intercepts (when axes are the asymptotes).
5. **n odd**: gradient always decreasing throughout defined x.
6. **n even**: gradient increasing for x < 0; decreasing for x > 0.
- **Intercepts**: x = 0 ⇒ y = −1; y = 0 ⇒ x = 1. So (0, −1) and (1, 0).
- **Turning points**: none.
- **Asymptotes**: as x → ∞, y → 1 (horizontal asymptote y = 1). As y → ∞, x → −1 (vertical asymptote x = −1).
- **Gradient**: always increasing.
- Unitary price elasticity of demand (rectangular hyperbola demand curve).
- Average fixed cost (AFC) curve.
- Production transformation curve.
- Indifference map components.
1) **Difference between hyperbola and rectangular hyperbola.**
   - A rectangular hyperbola is a special case of hyperbola in which the asymptotes are **orthogonal** (perpendicular). General hyperbolas have asymptotes that need not be perpendicular.
2) **Price elasticity of a rectangular-hyperbola-shaped demand curve?**
   - **Unitary** (= 1) at every point.
3) **Hint**: write the standard form of a hyperbola with a horizontal transverse axis.

**Quick Recall:**
- Rectangular hyperbola ⇔ asymptotes orthogonal.
- y = 1/x ⇒ price elasticity = 1 (unitary) when used as demand curve.
- **Level curve (contour line)**: for a function f of two variables and a constant c, the set of pairs (x, y) such that f(x, y) = c. ⭐

**Quick Recall:**
- z = f(x, y) ⇒ surface in 3D.
- Level curve: f(x, y) = c (a constant). Different c values give different curves.
- Economists' indifference curves and isoquants are level curves.

### Economic Interpretation of Level Curves — Indifference Curves & Isoquants 🔴
- **Indifference curve**: locus of (x, y) goods combinations giving the same utility (level curve of utility function). ⭐
- **Isoquant**: locus of (K, L) input combinations producing the same output (level curve of production function). ⭐
- **Indifference curve map**: a contour map of utility, showing several indifference curves at different utility levels.
- P = monetary value of all goods produced
- K = total capital investment
- L = total labour force
- Reducing labour requires **more capital investment** to maintain the same output (substitute machinery for missing labour).
- Increasing labour reduces the capital needed for the same output (labour does the work instead).
- Each curve represents one fixed value of P.
- c > 0: hyperbolas open left/right.
- c < 0: hyperbolas open up/down.
- c = 1: x² − y² = 1.
- c = −1: y² − x² = 1.
- A "level curve" need not be a curve at all — it's a **set**. For a constant function f(x, y) = 1, the level curve at value 1 is the entire plane (all (x, y)), and the level curve at value 2 is empty.
1) **Meaning of level curve**: a curve in two dimensions on which the value of a function f(x, y) is a constant.
2) **Comment on level curves of f(x, y) = 1 for all (x, y).**
   - Since f equals 1 everywhere, the level curve for value 1 is **the entire xy-plane** (every point qualifies). The level curve for value 2 is **empty** (no point gives f = 2). For value 0 the level curve consists of the axes (per the answer-key figure). So level curves here are not "curves" in the usual sense.

**Quick Recall:**
- Indifference curve = level curve of utility function.
- Isoquant = level curve of production function.
- Cobb-Douglas: P = A·L^α·K^β with α + β = 1 in CRS form.
| Group | Functions Covered |
|---|---|
| **Linear** | Linear, absolute value, step functions |
| **Curves** | Odd & even, quadratic, cubic |
| **Asymptotic** | Square root, exponential, logarithmic |
| **Pieces in xy-plane** | Rational, piecewise, discontinuous |
| **Curves with branches** | Hyperbola, rectangular hyperbola |
| **Two-variable** | (Final section) — contour maps |

### Check Your Progress 1–6 — Answers / Hints 🔴
1) **Vertical line test on the figure**: many vertical lines hit the graph more than once → **not a function**.
2) **Algebraic equation of a circle**: place origin at centre, mark arbitrary point P = (x, y) on the circle, drop perpendicular to x-axis at Q. Then by Pythagoras: **x² + y² = r²**.
1) **T-chart of y = (−5/3)x − 2:**
| x | y |
|---|---|
| −6 | 8 |
| −3 | 3 |
| 0 | −2 |
| 3 | −7 |
2) (Solving an equation): **x = 4/3 or x = −8/3**.
3) **Piecewise cost function**:
1) Graph of y = x³ − 2x: an "S"-shaped cubic curve.
2) Cubic function shape: a curve like the letter "S".
1) f(x) = (x + 1)/(x − 1).
   - x-intercept: x + 1 = 0 ⇒ x = −1 → **(−1, 0)**.
   - y-intercept: f(0) = 1/(−1) = −1 → **(0, −1)**.
2) **AFC asymptotic** because TFC is constant; AFC = TFC/Q steadily falls as Q rises but never becomes zero.
1) **f(x) = −x³ + 4**: write as ax³ + c with a = −1, c = 4. Reflect y = x³ across the x-axis (because a = −1) and translate up 4 units.
2) The basic cubic function: y = x³.
3) **f(x) = 1/x**: discontinuous because f(0) is undefined (asymptotic discontinuity at x = 0).
1) **Rectangular hyperbola** = hyperbola with **orthogonal (perpendicular) asymptotes**.
2) **Price elasticity** of rectangular-hyperbola demand = **unity (1)**.
3) Hint: write standard form with horizontal transverse axis.
1) **Level curve**: a 2D curve where f(x, y) is constant.
2) For a constant function f(x, y) = 1: level curve at 1 = whole plane; at 2 = empty.

**Quick Recall:**
- x² + y² = r² for a circle of radius r centred at origin.
- Vertical line test ⇒ relation is a function.
- Reflect y = x³ across x-axis ⇒ y = −x³.

### Exercises (Section 4.12) — Q1 to Q5 🔴
| x | y = x⁴ − 13x² + 36 |
|---|---|
| −4 | 84 |
| −2.5 | −6.19 |
| −1 | 24 |
| 0 | 36 |
| 1 | 24 |
| 2.5 | −6.19 |
| 4 | 84 |
|---|---|
| 0 | 5 |
| 1 | 0 |
| 3 | −4 |
| 5 | 0 |
| 6 | 5 |
|---|---|
| −2 | 0 |
| −1 | 3 |
| 0 | 4 |
| 1 | 3 |
|---|---|
| 2 | 4 |
| 3 | 6 |

### ⚠️ Common Mistakes
- ❌ Forgetting to mark whether the boundary point of a piecewise piece is included (closed dot) or excluded (open dot).
- ❌ Using axis of symmetry x = +b/2a instead of x = −b/2a.
- Builds on: vertex formula and shifts (chunk 013), piecewise functions (chunk 013, 014).
- Prerequisite for: continued exercises (Q6 onwards in chunk 016).
- Why does a positive even-power polynomial have both ends pointing the same way?
- For piecewise functions, when does redefining the boundary value remove a discontinuity?

### Q5 (Continued) — Piecewise Function with Open/Closed Dot Convention 🔴
| x | f(x) = −x² + 4 | (x, y) |
|---|---|---|
| −2 | 0 | (−2, 0) |
| −1 | 3 | (−1, 3) |
| 0 | 4 | (0, 4) |
| 1 | 3 | (1, 3) |
| x | f(x) = 2x − 1 | (x, y) |
|---|---|---|
| 1 | 1 | (1, 1) |
| 2 | 3 | (2, 3) |
| 3 | 5 | (3, 5) |
- Upper branch (−x² + 4) at x = 1: closed dot at (1, 3) — because x ≤ 1 includes 1.
- Lower branch (2x − 1) at x = 1: **open dot** at (1, 1) — because x > 1 excludes 1; the formula is only "approached" there.

### ⚠️ Common Mistakes
- ❌ Using closed dots on both branches at a non-shared boundary → ✅ Only one branch can include the boundary; use open dot for the other.

**Quick Recall:**
- "≤" and "≥" → closed dot.
- "<" and ">" → open dot.
---

### Q6 — Three-Piece Piecewise Function 🔴
| Branch | x | y | Point |
|---|---|---|---|
| x + 3 | −3 | 0 | (−3, 0) |
| x + 3 | −2 | 1 | (−2, 1) |
| x² | −2 | 4 | (−2, 4) |
| x² | −1 | 1 | (−1, 1) |
| x² | 0 | 0 | (0, 0) |
| x² | 1 | 1 | (1, 1) |
| −x + 2 | 1 | 1 | (1, 1) |
| −x + 2 | 2 | 0 | (2, 0) |
1. Identify each branch and its sub-domain.
2. T-chart for each branch including endpoints.
3. Place closed/open dots based on which branch includes the boundary.
4. Sketch each piece, joining or leaving gaps as the values dictate.

### Q7 — Hyperbola 9x² − 16y² = 144 🔴
- **x-intercept**: set y = 0 → x²/4² = 1 → **x = ±4**. Points (4, 0) and (−4, 0).
- **y-intercept**: set x = 0 → −y²/9 = 1 → no real solution → **no y-intercept**.
1. Plot asymptotes y = (3/4)x and y = −(3/4)x.
2. Plot vertices (±4, 0).
3. Use additional point: at x = 6, 9(36) − 16y² = 144 → −16y² = 144 − 324 = −180 → y² = 45/4 → y = ±3√5/2.
4. Draw branches starting at vertices, hugging asymptotes outward.

### ⚠️ Common Mistakes
- ❌ Forgetting to divide by 144 first → ✅ Always normalise to "= 1" form before reading a, b.
- ❌ Confusing F² = a² + b² (hyperbola) with F² = a² − b² (ellipse).

**Quick Recall:**
- Horizontal hyperbola: x²/a² − y²/b² = 1 → vertices (±a, 0), foci (±F, 0), F² = a² + b².
- Asymptotes through origin: y = ±(b/a)x.
---

### Q8 — Rational Function y = (2x² − 18)/(x² − 4) 🔴
| x | y = (2x² − 18)/(x² − 4) |
|---|---|
| −5 | 1.5 |
| −2.5 | −2.4 |
| −1 | 5.3 |
| 1 | 5.3 |
| 2.5 | −2.4 |
| 5 | 1.5 |

### ⚠️ Common Mistakes
- ❌ Skipping the asymptote step and directly tabulating values → ✅ Always identify asymptotes first; pick test points strategically near them.
- ❌ Plugging x = ±2 into a T-chart (undefined) → ✅ Mark these as vertical asymptotes, not as plot points.

**Quick Recall:**
- Vertical asymptote: where denominator = 0.
- Horizontal asymptote (when num/denom degrees match): ratio of leading coefficients.
- x-intercept: where numerator = 0 (and denominator ≠ 0).
---

**Quick Recall:**
- Plot quadratics via vertex (x = −b/2a).
- Identify three discontinuity types.
- Hyperbola: F² = a² + b²; asymptotes are diagonals of the helper rectangle.
- Rational function pipeline: asymptotes → intercepts → fill points.
- Always normalise conics to "= 1" form first.
