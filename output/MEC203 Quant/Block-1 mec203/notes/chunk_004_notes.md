# Chunk 004 — Set Operations Completion, Numbers (N → C), Real Number Properties, Decimals, Exponentiation
<!-- Pages: 31-40 -->
<!-- Source: chunk_004.txt -->
<!-- Continues from: Set operations (Chunk 003) -->

## Section: Set Operations — Difference & Complement (continued) 🔴
<!-- Continues from: Union and Intersection (Chunk 003) -->

### Core Idea
Completing the four set operations: the **difference** X − Y removes Y's elements from X, and the **complement** X′ = U − X gives all elements in the universe U not in X.

### Examples
**Example: Difference**
X = {1, 2, 3, 4}, Y = {2, 5, 8, 3, 9}.
- **X − Y = {1, 4}** (elements of X not in Y).
- **Y − X = {5, 8, 9}** (elements of Y not in X).
- **Note**: X − Y ≠ Y − X in general (difference is not commutative).

#### d) Complement of a Set — X′
**Complement** of a set X is a special case of the difference: it requires a fixed Universal set U.
- **Definition**: **X′ = U − X**. ⭐
- **Example**: U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, X = {2, 5, 8, 3, 9} → **X′ = {1, 4, 6, 7, 10}**.

**Alternative notations** for complement: **X′**, **~X**, **Xᶜ**.

### Definitions ⭐
- **Union ∪**: X ∪ Y = {x : x ∈ X or x ∈ Y}. ⭐
- **Intersection ∩**: X ∩ Y = {x : x ∈ X and x ∈ Y}. ⭐
- **Difference −**: X − Y = {x : x ∈ X and x ∉ Y}. ⭐
- **Complement ′**: X′ = U − X (depends on the chosen universe U). ⭐

### ⚠️ Common Mistakes
- ❌ Computing X − Y as Y − X. → ✅ Not commutative; check direction.
- ❌ Forgetting to specify U when using complement. → ✅ Complement is undefined without an explicit universal set.

---

## Section: More Clarifications — Operands, Values, Operators 🟡

### Core Idea
Distinguish **operands/arguments/inputs** (what you put in), **value/result/output** (what you get), and **operator** (the symbol denoting the operation/relation).

### Key Concepts

#### Operands vs Value
For X = {1, 2, 3, 4} and Y = {2, 3, 5, 8, 9}: X ∪ Y = {1, 2, 3, 4, 5, 8, 9}.
- **Operands / arguments / inputs**: {1, 2, 3, 4} and {2, 3, 5, 8, 9}.
- **Value / result / output**: {1, 2, 3, 4, 5, 8, 9}.

This terminology applies equally to relations:
- For 7 < 5 (returns FALSE): operands = 7 and 5; value = FALSE.

#### Operation vs Operator
- **Operator**: the **symbol** (e.g., **∪** for union, **<** for less-than).
- **Operation**: the **process** of computing a result from operands using an operator.

| Concept | Example | What it refers to |
|---|---|---|
| Operator | ∪, ∩, +, < | The symbol |
| Operation | "Take the union of X and Y to get …" | The process / mapping |
| Operand | X, Y, 7, 5 | The inputs |
| Value | {1, 2, …}, FALSE | The output |

---

## Section: Check Your Progress 4 🔴

### Examples / Exercises ⭐
**Q1.** Let X = {1, {2, 3}, {4, 5}, 6} and Y = {1, {2, 4}, {5, 6, 7}}. Find:
- (a) X ∪ Y
- (b) X ∩ Y
- (c) X − Y
- (d) Y − X

> **Hint**: Treat each "{…}" element as a single object. So {2, 3} ∈ X but {2, 3} ∉ Y (because Y contains {2, 4}, not {2, 3}); only **1** is common to both.

---

## Section: Numbers — Standard Number Sets 🔴

### Core Idea
The standard hierarchy of number sets — Natural ⊂ Whole ⊂ Integer ⊂ Rational ⊂ Real ⊂ Complex — with their conventional symbols (N, W, Z, Q, R, C) is the backbone of all subsequent mathematics.

> **In Simple Terms:** Math builds numbers in layers: counting numbers → add zero → add negatives → add fractions → add √2 and π → add imaginary i. Each layer fits inside the next.

### Definitions ⭐
- **N = {1, 2, 3, …}**: set of **natural / counting numbers**. ⭐
- **W = {0, 1, 2, 3, …}**: set of **whole numbers** (natural numbers + 0). ⭐
  - *Note*: many modern conventions treat 0 as a natural number, so N = W and W is redundant.
- **Z = {…, −3, −2, −1, 0, 1, 2, 3, …}**: set of **integers** (German "Zahlen"). ⭐
- **Q = {x : x = p/q with q ≠ 0, and p, q ∈ Z}**: set of **rational numbers** ("quotient"). ⭐

### Containment Hierarchy (so far) ⭐
**∅ ⊂ N ⊂ W ⊂ Z ⊂ Q**.

**Why Z ⊂ Q?** For any n ∈ Z, n = n/1 ∈ Q. Also, 3/4 ∈ Q but 3/4 ∉ Z, so Z is a *proper* subset of Q.

### Connections
- Extended below to include R (real) and C (complex).

---

## Section: R — The Set of Real Numbers 🔴

### Core Idea
The **real numbers** R correspond to all points on a continuous straight line (the "number line"). They include all rationals AND irrational numbers like √2 and π. R is the most frequently used number set in numerical problem-solving.

> **In Simple Terms:** A real number is anything that can be a position on the number line — including familiar fractions, plus the "filler" numbers like √2 = 1.4142… that fill in the gaps between fractions.

### Mechanisms / Processes — Constructing R Geometrically

1. **Pick a line**, mark a left point as **0**, a right point as **1**.
2. **Natural numbers**: mark points to the right of 1 at equal spacings → 2, 3, 4, … .
3. **Negative integers**: mark points to the left of 0 at equal spacings → −1, −2, −3, … .
4. **Rational numbers**: e.g., for **3.45**, divide [3, 4] into 100 equal parts and mark the 45th part to the right of 3.
5. **Irrational numbers**: e.g., for **√2**, construct a unit square; its hypotenuse has length √2; mark this distance to the right of 0 on the number line.
6. **Result**: every point on the line corresponds to a real number, and conversely.

### Definitions ⭐
- **Real number**: a number obtained by corresponding to a point on a straight line (as above). ⭐
- **R = {x | x is a real number}**.
- **Irrational number**: a real number that is **not** rational. The set of irrationals is **R − Q** (also written R \ Q). ⭐
  - **Example**: √2 (proven irrational — no p/q exists with p² /q² = 2).
  - **Fact**: there are **more** irrational reals than rational reals (irrationals are uncountable, rationals are countable).

### Extended Containment Hierarchy ⭐
**∅ ⊂ N ⊂ W ⊂ Z ⊂ Q ⊂ R**.

**Why Q ⊂ R (proper)?** √2 ∈ R but √2 ∉ Q.

---

## Section: Real Number Intervals 🔴

### Core Idea
An **interval** is a set of real numbers between two boundaries; it is **closed** if it includes both boundaries, **open** if it excludes both, and **semi-open/semi-closed** if it includes exactly one.

> **In Simple Terms:** Square brackets "include the endpoint"; round brackets (or reversed square brackets) "exclude the endpoint".

### Definitions ⭐ (illustrated with bounds 3 and 7.5)

| Interval | Reads as | Includes 3? | Includes 7.5? | Type |
|---|---|---|---|---|
| **[3, 7.5]** | "closed interval 3 to 7.5" | Yes | Yes | Closed |
| **(3, 7.5]** or **]3, 7.5]** | "left-open, right-closed" | No | Yes | Semi-open / semi-closed |
| **[3, 7.5)** or **[3, 7.5[** | "left-closed, right-open" | Yes | No | Semi-open / semi-closed |
| **(3, 7.5)** or **]3, 7.5[** | "open interval" | No | No | Open |

> The textbook uses both the bracket notation (·, ·) and the French-style "outward" bracket notation ]·, ·[ — both are equivalent.

### ⚠️ Common Mistakes
- ❌ Using **(3, 7.5)** for the ordered pair when the context is intervals. → ✅ Context disambiguates; the same bracket notation is overloaded.
- ❌ Confusing closed vs open intervals when checking convexity or extreme values. → ✅ Closed intervals attain max/min; open ones may not.

> **Quick Recall:**
> - **[ ] include endpoints**, **( ) exclude endpoints**.
> - 4 types: closed, open, two semi-open variants.

### Connections
- Used in defining continuity, limits (Block 3), convex sets (§1.2.5, Chunk 003).

---

## Section: Complex Numbers — C 🔴

### Core Idea
**Complex numbers** extend the reals by introducing **i** with **i² = −1**, allowing solutions to equations like x² + 1 = 0 that have no real solutions. C contains R as a proper subset.

> **In Simple Terms:** Some equations have no real-number answers (e.g., x² = −1). Mathematicians invented a new number i with i² = −1, and built complex numbers a + bi to handle these cases.

### Definitions ⭐
- **i**: the imaginary unit, with **i² = −1**. ⭐
- **C = {z : z = x + iy, where x, y ∈ R}** = set of **complex numbers**. ⭐
- (x + iy is also written x + yi.)

### Why R ⊂ C (proper)
- Any real x ∈ R can be written x = x + i·0, so x ∈ C → R ⊆ C.
- 1 + i·2 ∈ C but 1 + i·2 ∉ R (and i = 0 + i·1 ∈ C but i ∉ R).
- Therefore **R ⊂ C** (proper).

### Final Containment Hierarchy ⭐
**∅ ⊂ N ⊂ W ⊂ Z ⊂ Q ⊂ R ⊂ C**.

### Edge Cases & Caveats
- Symbols **∅, N, W, Z, Q, R, C** are **standard** and may be used without redefinition. Custom set names (like **Sq_int**) must be defined fresh in each new context.

---

## Section: Number Miscellany 🟡

### Core Idea
A grab-bag of clarifying facts: examples illustrating which numbers belong to which classes; arithmetic vs algebraic operations; arithmetic relations; the difference between fraction and rational number; prime numbers; the constant π; and the historical reasoning behind the symbols N, Z, Q, R, C.

### Key Concepts

#### Number Classification Examples

| Number | N? | Z? | Q? | Irrational? | R? | C? |
|---|---|---|---|---|---|---|
| 3 | ✓ | ✓ | ✓ |  | ✓ | ✓ |
| −12 |  | ✓ | ✓ |  | ✓ | ✓ |
| 8.7 |  |  | ✓ |  | ✓ | ✓ |
| 2/3 |  |  | ✓ |  | ✓ | ✓ |
| √2 |  |  |  | ✓ | ✓ | ✓ |
| π |  |  |  | ✓ | ✓ | ✓ |
| 7 − 3i |  |  |  |  |  | ✓ |

> Each example is constructed so that it does NOT have the preceding stronger properties. E.g., √2 is irrational so not rational, not integer, not natural.

#### Arithmetic / Algebraic Operations
- **Binary** (need 2 inputs): **+, −, ×, ÷**.
- **Unary** (need 1 input):
  - **Exponent / power**: x², and in general x^n for fixed n.
  - **Absolute value**: **|x| = −x if x < 0; |x| = x if x ≥ 0**. ⭐
    - |5| = 5 and |−5| = 5.

#### Arithmetic Relations
Examples: **=, ≠, <, ≤, >, ≥**.

#### Fraction vs Rational Number
- **3/5** and **6/10** are two **different** fractions but **the same** rational number.
- Two fractions p/q and r/s (with q ≠ 0, s ≠ 0) are equal as rationals iff **p × s = q × r**. ⭐
  - 3/5 = 6/10 because 3 × 10 = 5 × 6 = 30.

#### Prime Numbers
- A natural number p is **prime** if the only natural numbers dividing p are **1 and p itself**. ⭐
- Examples: 2, 3, 5, 19, 31 — prime. 4, 21 — not prime.
- **1 is NOT a prime**, even though only 1 divides it. The reason: **1 is a unit in N** (1 × 1 = 1), and only 1 has this property. For any q ≠ 1 in N, no s in N satisfies q × s = 1.

#### The Constant π
- **π** denotes the real number defined by **c = πd**, with c = circumference of a circle and d = its diameter.
- π is **irrational** (proof beyond scope).

#### Nomenclature for Number-Set Symbols
- **N**: from "Natural" (Natural Numbers).
- **Z**: from German **Zahlen** (Integers). Sometimes denoted **I**.
- **Q**: from "Quotient" (Quotient Numbers, i.e., rationals).
- **R**: from "Real".
- **C**: from "Complex".

### ⚠️ Common Mistakes
- ❌ Saying 3/5 and 6/10 are different rational numbers. → ✅ They are different *fractions* but the same *rational number*.
- ❌ Including 1 as a prime. → ✅ 1 is a unit, not a prime.
- ❌ Thinking |x| produces a negative output. → ✅ |x| ≥ 0 always.

> **Quick Recall:**
> - π and √2: irrational reals.
> - 1 is **not** a prime.
> - p/q = r/s iff p·s = q·r.
> - |x| = max(x, −x); always ≥ 0.

---

## Section: Properties of Real Numbers as an Ordered Field 🔴

### Core Idea
R, equipped with **+** (addition) and **×** (multiplication), satisfies the **Field axioms**; with the relation **<** added it becomes an **Ordered Field**; with the unary **|·|** (modulus) added, it gains **metric/norm** properties. These axioms underpin every algebraic manipulation in the course.

> **In Simple Terms:** R is a "well-behaved" set: you can add, subtract, multiply, divide (except by 0), compare, and measure distances — all the operations behave the way arithmetic intuition suggests.

### Definitions / Properties

#### a) Field Properties (R, +, ×) — for all x, y, z ∈ R ⭐

| # | Property | Statement |
|---|---|---|
| 1 | Closure | x + y ∈ R, and x × y ∈ R. |
| 2 | Associativity | (x + y) + z = x + (y + z); (x × y) × z = x × (y × z). |
| 3 | Existence of unique identities | 0, 1 ∈ R such that x + 0 = 0 + x = x and x × 1 = 1 × x = x. |
| 4 | Existence of unique inverses | For every x ∈ R, ∃ (−x) such that x + (−x) = (−x) + x = 0. For x ≠ 0, ∃ x⁻¹ such that x × x⁻¹ = x⁻¹ × x = 1. |
| 5 | Commutativity | x + y = y + x; x × y = y × x. |
| 6 | Distributivity (× over +) | x × (y + z) = x × y + x × z. |

#### b) Ordered Field Properties (additional, with relation <) — for all x, y, z ∈ R ⭐

| # | Property | Statement |
|---|---|---|
| 1 | Positivity preservation | If 0 < x and 0 < y then 0 < x + y and 0 < x × y. |
| 2 | **Trichotomy** | For x ∈ R, exactly one of (a) x < 0, (b) x = 0, (c) 0 < x is true. ⭐ |
| 3 | **Transitivity** | If x < y and y < z, then x < z. ⭐ |
| 4 | Monotone property of addition | If x < y, then x + z < y + z. |
| 5 | Monotone property of multiplication | If x < y and 0 < z, then x × z < y × z. |
| 6 | **Archimedean property** | Given two positive numbers A and B, there exists a natural number n such that **B < n × A**. ⭐ |

#### c) Metric / Norm Properties (with |·| modulus) — for all x, y, z ∈ R ⭐

| # | Property | Statement |
|---|---|---|
| 1 | Non-negativity & definiteness | |x| ≥ 0; |x| = 0 iff x = 0. |
| 2 | Symmetry under negation | |x| = |−x|. |
| 3 | Bracketing | −|x| ≤ x ≤ |x|. |
| 4 | **Triangle inequality** | **\|x + y\| ≤ \|x\| + \|y\|**. ⭐ |

#### Distance Function ‖·‖ : R × R → R
Defined by **‖x − y‖ = |x − y|**. For all x, y, z ∈ R:

| # | Property |
|---|---|
| 1 | ‖x − y‖ ≥ 0; ‖x − y‖ = 0 iff x = y. |
| 2 | ‖x − y‖ = ‖y − x‖ (symmetry). |
| 3 | **Triangle Inequality**: ‖x − z‖ ≤ ‖x − y‖ + ‖y − z‖. ⭐ |

### ⚠️ Common Mistakes
- ❌ Forgetting the multiplicative inverse exists only for x ≠ 0. → ✅ 0 has no multiplicative inverse.
- ❌ Asserting the triangle inequality with equality always. → ✅ Equality holds only when x and y have the same sign (or one is zero).
- ❌ Misapplying monotone multiplication: multiplying both sides of an inequality by a **negative** number reverses the inequality. → ✅ The textbook's monotone property requires **0 < z**.

> **Quick Recall:**
> - 6 Field axioms + 6 Order axioms + 4 Metric axioms.
> - **Trichotomy**: x is <0, =0, or >0 — exactly one.
> - **Archimedean**: no number in R is "infinitely large" relative to others — multiples of any positive A eventually exceed any B.
> - **Triangle inequality**: |x + y| ≤ |x| + |y|.

### Connections
- Foundation for **real analysis** (Block 4): completeness, sequences, continuity all build on these axioms.
- The Archimedean property is critical for limits and ε-δ proofs.

---

## Section: Decimal Representation of Rational and Irrational Numbers 🔴

### Core Idea
Every real number has a decimal representation. **Rationals** have either **terminating** or **non-terminating recurring (repeating)** decimal expansions; **irrationals** have **non-terminating, non-repeating** expansions.

> **In Simple Terms:** Rational = decimals that stop or repeat in a pattern; Irrational = decimals that go on forever with no pattern (like π, √2).

### Key Concepts

#### (i) Terminating Decimal — Rational
**3/8 = 0.375** — finite number of digits after the decimal.

#### (ii) Non-Terminating Recurring Decimal — Rational
**7/3 = 2.333…** = **2.3̄** (the digit 3 repeats forever).

**29/7 = 4.142857142857142857… = 4.142857** (the block "142857" repeats forever).

**Notation**: a bar over a digit (or block of digits) means "repeats forever". E.g., **2.3̄** for 2.333… and **4.142857** with bar over 142857.

#### (iii) Non-Terminating Non-Recurring Decimal — Irrational
**π = 3.14159…** (no pattern).
**√2 = 1.41421…** (no pattern; OCR shows "1.4142857..." but the standard value is 1.41421356…).

### Mechanisms / Processes — Converting Decimals to Fractions

**Example: 187.0145083 as a fraction**
1. Count digits after the decimal point: **7** digits → write **10⁷ = 10,000,000** as denominator (a 1 followed by seven 0s).
2. Numerator = the number with the decimal point removed: **1,870,145,083**.
3. So 187.0145083 = **1,870,145,083 / 10,000,000**.

[Note on OCR: source shows "748058003 / 400000" after a simplification step — apparent OCR distortion. The general rule is: place a 1 followed by as many 0s as digits after the decimal point in the denominator; numerator = the digits without the decimal point. Then divide both by the GCD to simplify.]

**Process summary**:
1. Move decimal to make integer numerator.
2. Denominator = 10^(number of digits past decimal).
3. Simplify by dividing numerator and denominator by their GCD (e.g., divide by 25, then look for further common factors).

### ⚠️ Common Mistakes
- ❌ Thinking 0.999… is different from 1. → ✅ 0.9̄ = 1 exactly (a classic surprise).
- ❌ Assuming all non-terminating decimals are irrational. → ✅ They are irrational only if they are also non-repeating; 0.333… = 1/3 is rational.

> **Quick Recall:**
> - Terminating decimal → rational.
> - Repeating decimal → rational.
> - Non-terminating, non-repeating → irrational.
> - To convert: use 10^k denominator, then simplify by GCD.

---

## Section: Real Number Exponentiation 🔴

### Core Idea
**Exponentiation** **xⁿ** is repeated multiplication of the **base** x by itself **n** times. The definition extends naturally to **0**, **negative integers**, and **fractional/real** exponents (via roots).

> **In Simple Terms:** x³ means x × x × x. x⁰ = 1, x⁻¹ = 1/x, and x^(1/n) means the n-th root.

### Definitions ⭐

#### Positive Integer Exponent
For **n ∈ N**, **xⁿ = x · x · x · … · x** (n times). x is the **base**; n is the **exponent** (or power).
- **Examples**:
  - 19⁴ = 19 × 19 × 19 × 19.
  - (−15)³ = (−15) × (−15) × (−15).
  - (3/4)⁵ = 3⁵ / 4⁵.
- **General rule**: **(x/y)ⁿ = xⁿ / yⁿ**.

#### Zero and Negative Integer Exponent
- **x⁰ = 1**. ⭐
- **x⁻¹ = 1/x**.
- **x⁻ⁿ = (1/x)ⁿ = 1/xⁿ** for n ∈ N. ⭐
- **Example**: 19⁻³ = (1/19)³ = (1/19)(1/19)(1/19) = 1/6859.

#### Rules of Exponents (for m, n ∈ Z, and indeed m, n ∈ R) ⭐

| Rule | Formula |
|---|---|
| Product of same base | **x^(m+n) = xᵐ · xⁿ** |
| Power of a power | **x^(mn) = (xᵐ)ⁿ** |
| Negative exponent | **x⁻ⁿ = 1/xⁿ** |
| Quotient of same base | **x^(m−n) = xᵐ / xⁿ** |
| Power of product | **(x · y)ᵃ = xᵃ · yᵃ** |
| Power of quotient | **(x/y)ᵃ = xᵃ / yᵃ** |

(These hold for any real or even complex exponent a.)

#### Fractional Exponents and Roots
- **√2** means the number whose square is 2: √2 × √2 = 2.
- **⁴√7** means the 4th root of 7: ⁴√7 × ⁴√7 × ⁴√7 × ⁴√7 = 7.
- **In general**: for **n ≠ 0**, **ⁿ√x = x^(1/n)**, where x may be any real (or complex) and n is a natural number.

#### General Fractional Exponents
For **m ∈ Z, n ∈ N**:
- **x^(m/n) = x^(m·(1/n)) = ⁿ√(xᵐ)** = (ⁿ√x)ᵐ. ⭐
- For n ≠ 0: **x^(m/n) = (x^(1/n))ᵐ = (ⁿ√x)ᵐ**.

#### Arithmetic Operations on Bases
- **Multiplication / division of same exponent**:
  - **(x · y)ᵃ = xᵃ · yᵃ**.
  - **(x/y)ᵃ = xᵃ / yᵃ**.
- **Addition / subtraction of like-exponent expressions** **xⁿ + yⁿ** or **xⁿ − yⁿ**: treated as **almost independent irreducible expressions**, except when x and y share a common factor ≠ 1.

### Examples
**Example: Factoring a sum of powers using common factor**
3⁵ + 6⁷:
- 6 = 3 × 2, so 6⁷ = (3 × 2)⁷ = 3⁷ × 2⁷.
- 3⁵ + 6⁷ = 3⁵ + 3⁷ × 2⁷ = 3⁵ × (1 + 3² × 2⁷) = 3⁵ × (1 + 9 × 128) = 3⁵ × (1 + 1152) = 3⁵ × 1153.

(The textbook's worked form: 3⁵ + 6⁷ = 3⁵ + (3 × 2)⁷ = 3⁵[(3)² × (2)⁷ + 1] — same result; demonstrates extracting the common base.)

### ⚠️ Common Mistakes
- ❌ Treating x^(1/2) + y^(1/2) as (x + y)^(1/2). → ✅ **Not equal**: √x + √y ≠ √(x + y) in general.
- ❌ Assuming (xᵐ)ⁿ = x^(m+n). → ✅ It equals **x^(mn)** (multiply, not add).
- ❌ Computing 0⁰ as 1 or 0 without context. → ✅ 0⁰ is conventionally 1 in combinatorics but indeterminate in calculus.
- ❌ Forgetting x⁻ⁿ ≠ −xⁿ. → ✅ x⁻ⁿ = 1/xⁿ; the minus sign in the exponent flips the number, not its sign.

> **Quick Recall:**
> - x^(m+n) = xᵐ · xⁿ.
> - (xᵐ)ⁿ = x^(mn).
> - x⁰ = 1.
> - x⁻ⁿ = 1/xⁿ.
> - x^(1/n) = ⁿ√x.
> - (xy)ᵃ = xᵃyᵃ; (x/y)ᵃ = xᵃ/yᵃ.

### Connections
- Foundation for: logarithms (inverse of exponentiation), exponential functions e^x (Block 3), growth/decay models in economic dynamics (Block 6), compound interest.

---

## Section: Check Your Progress 5 🔴

### Examples / Exercises ⭐
**Q1.** Express the decimal number **18725.4625** as a fraction.

> **Hint**: 4 digits after the decimal → denominator 10⁴ = 10,000. Numerator = 187,254,625. So 18725.4625 = 187,254,625 / 10,000. Then divide both by GCD (here both are divisible by 125): = 1,498,037 / 80. Verify by long division.

---

## Section: Let Us Sum Up — Summary of Operators 🟢

### Core Idea
This unit gave a bird's-eye view of the two foundational concepts of mathematics — **number** (basis of conventional mathematics) and **set** (basis of modern mathematics) — and the operators and relations governing each.

### Key Concepts (Summary Tables)

| Category | Examples |
|---|---|
| Set operators | **∪** (union), **∩** (intersection), **−** (difference), **′** (complement) |
| Set-relational symbols | **=**, **⊆** (subset), **⊂** (proper subset), **⊄** (not subset), **∈** (belongs to), **∉** (does not belong) |
| Algebraic / arithmetic operators | **+, −, ×, ÷, √, |·|, log, eˣ** |
| Algebraic / arithmetic relational symbols | **=, ≠, <, ≤, >, ≥** |

---

## Section: Key Words (Glossary) 🔴

### Definitions ⭐

- **Cross-Product of sets**: For two non-empty sets A₁ and A₂, A₁ × A₂ is the set of all ordered pairs (a₁, a₂) with a₁ ∈ A₁, a₂ ∈ A₂. Generalises to A₁ × A₂ × … × Aₙ as the set of all n-tuples (a₁, a₂, …, aₙ) with aᵢ ∈ Aᵢ for i = 1, 2, …, n. ⭐

- **Number**: An abstract concept used for counting, measuring, or labelling. Made tangible through numerals — e.g., "five" is purely an idea, made tangible through the numeral **5**. ⭐

- **Operation on a set X**: An operation of arity n maps the n-fold cross-product of X with itself to **X itself** (returns an element of X). E.g., square on N (arity 1) and sum on N (arity 2) both return a number. ⭐

- **Relation on a set X**: A relation of arity n is a **subset of the n-fold cross-product** of X with itself; returns exactly **true or false**. E.g., is-male (arity 1), is-mother-of (arity 2). ⭐

- **Set**: A well-defined collection of objects, where a collection C is well-defined iff for any x we can determine whether x belongs to C or not. ⭐

### Connections
- These definitions tie together every section of Unit 1 and serve as the working vocabulary for all subsequent units.

### Open Questions
- How does the textbook later distinguish "Number System" (different from Numeral System mentioned in §1.1)?
- The exercises at §1.9 and answers at §1.8 likely appear in the next chunk — do they confirm the conjectured answers above?
