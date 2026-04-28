# Chunk 006 — Polynomials, Polynomial Identities, Algebra of Polynomials, Linear Equations
<!-- Pages: 51-60 -->
<!-- Source: chunk_006.txt -->

## Section: Polynomials and Polynomial Equations (2.2.3) 🔴
<!-- Continues from: Mathematical Expressions (Chunk 005) -->

### Core Idea
A polynomial expression involves variables only with non-negative integer powers. A polynomial equation has exactly one '=' with polynomial expressions on both sides. These notes formalise terms, factors, coefficients, monomials, the *degree* of a term/polynomial/equation, and how to evaluate a polynomial for given variable values.

> **In Simple Terms:** Polynomials are the well-behaved expressions where every variable appears as x, x², x³ etc. — no roots, no logs, no division by variables. The "degree" tells you the polynomial's highest power.

### Key Concepts

#### Term
Each component separated by '+' or '−' is a term.
- x³ + 8x − 4 has three terms: x³, 8x, −4.
- (x − y)² at the highest level has only one term; on expansion x² + y² − 2xy has 3 terms.
- In x³y + 8x − 4y², the powers are: x: 3 in x³y, 1 in 8x, 0 in −4y²; y: 1, 0, 2 respectively.
- A *term* contains no '+' or '−' at the top level; uses only ×/exponentiation in polynomial terms (no division by variable). (45x²)/(78y) is an algebraic term but not a polynomial term.

#### Factor & Coefficient
For (45 x³ y³): factors include 3, 5, 9, 45, x, x², y, y², and any products of these. The constant factor 45 is the **coefficient** of the term.
- Coefficient of 17xy is 17; coefficient of −25x is −25.

#### Monomial / Binomial / Trinomial / Polynomial
| Name | Number of terms | Example |
|------|----------------|---------|
| Monomial | 1 | 45x²y³ |
| Binomial | 2 | 45x²y³ − 25; a + b |
| Trinomial | 3 | 45x²y³ − 25x⁴ + 71y⁵; a + b − 72 |
| Polynomial (general) | one or more terms (each with non-zero coefficient, variables with non-negative integer exponents) | 45x⁵ − 25x⁴ + 91x − 36 |

A polynomial may involve one variable, two variables (e.g. 45x²y³ + y⁵ − 25), or more (e.g. x + 3y + z + 2u + v).

#### General Form of a Polynomial Equation
For practical purposes, any polynomial equation containing at least one variable can be written by appending "= 0" to a polynomial expression. Example: 45x²y³ + 71y⁵ − 25x⁴ = 0.

#### Degree
- **Degree of a term** = sum of powers of all variables in that term.
  - deg(45x²y³) = 2 + 3 = 5.
  - deg(345) = 0 (constant; can be regarded as 345·x⁰ since x⁰ = 1 for any non-zero x).
- **Degree of a polynomial** = max degree among its terms.
  - For 45x²y³ + 71y⁵ − 25x⁴: degree = 5.
- **Degree of a polynomial equation** = max degree among terms on both sides.
  - For 71y³ + 45x²·z·y³ + 2xy = −25x³: degree = 7 (the 45x²zy³ term contributes 2+1+3 = 6... [the textbook gives 7; OCR ambiguity, but the principle is "max term degree"]).
- Convention: a polynomial is generally written in *order of decreasing degree of its terms*.

#### Naming a Polynomial
A polynomial in two variables x and y can be named, e.g., P(x, y) = 45x²y³ + 71y⁵ − 25x⁴ + 76.

#### Evaluating a Polynomial
Substitute the given (constant) values for the variables.
- For P(x, y) = 4x³ − 7xy² + 11:
  - P(2, −1) = 4(2)³ − 7(2)(−1)² + 11 = 32 − 14 + 11 = 29 [textbook OCR shows "16 − 14 + 11 = 13"; treating the original published value as printed]. Note: the textbook prints 4(2)³ = 16 which appears as an OCR/text artefact; the **method** is what matters.
  - P(−1, 2) = 4(−1)³ − 7(−1)(2)² + 11 = −4 + 28 + 11 = 35 [textbook shows 43 — OCR mismatch in printed source].

#### Solution of a Polynomial Equation (multi-variable)
For polynomials P(x, y) = Q(x, y), constants a (for x) and b (for y) are a *solution* if P(a, b) = Q(a, b).

### ⚠️ Common Mistakes
- ❌ Calling (45x²)/(78y) a polynomial term → ✅ It is algebraic, not polynomial (variable in denominator).
- ❌ Forgetting that the constant term has degree 0 → ✅ 345 = 345·x⁰, so deg = 0.
- ❌ Saying √x or x⁻¹ are allowed in polynomials → ✅ Only non-negative integer powers of variables.

> **Quick Recall:**
> - Polynomial: variables to non-negative integer powers only.
> - Degree of term = sum of exponents; degree of polynomial = max term degree.
> - Standard form: write in decreasing degree.

### Connections
- Builds on: classification of mathematical expressions (Chunk 005)
- Continues into: 2.2.4 Polynomial Identities

---

## Section: Polynomial Identities (2.2.4) 🔴

### Core Idea
Polynomial identities are polynomial equations true for *every* value of the variables. A small toolbox of standard identities (expansion of (x+y)², (x+y)³ etc., factorisation of x²−y², x³+y³+z³−3xyz, etc.) lets you factor and simplify many expressions without expanding from scratch.

> **In Simple Terms:** These are the algebraic "shortcuts" — memorise them once and you can factor 105×95 in your head, or factorise (625/16)x⁴ − (9/49)y² in two lines.

### Key Concepts

#### Standard Polynomial Identities
1. (x + y)² = x² + y² + 2xy
2. (x − y)² = x² + y² − 2xy
3. x² − y² = (x + y)(x − y)
4. (x + a)(x + b) = x² + (a + b)x + ab
5. (x + y + z)² = x² + y² + z² + 2xy + 2xz + 2yz
6. (x − y − z)² = x² + y² + z² − 2xy − 2xz + 2yz   [from (5) by y → −y, z → −z]
7. (x + y)³ = x³ + y³ + 3xy(x + y)
8. (x − y)³ = x³ − y³ − 3xy(x − y)
9. x³ + y³ + z³ − 3xyz = (x + y + z)(x² + y² + z² − xy − yz − zx)

### Examples
**Example: Evaluate 105 × 95 without direct multiplication**
105 × 95 = (100 + 5)(100 − 5) = 100² − 5² (using identity 3)
= 10000 − 25 = 9975. ✓

**Example: Factorise (625/16)x⁴ − (9/49)y²**
- 625/16 = (25/4)² and 9/49 = (3/7)².
- (625/16)x⁴ − (9/49)y² = [(25/4)x²]² − [(3/7)y]²
- = [(25/4)x² + (3/7)y] · [(25/4)x² − (3/7)y]   (using identity 3)

**CYP 2 Q1 — Expand (2a − 4b − 5c)²** (answer in Section 2.6, see chunk 007):
= (2a)² + (−4b)² + (−5c)² + 2(2a)(−4b) + 2(2a)(−5c) + 2(−4b)(−5c)
= 4a² + 16b² + 25c² − 16ab − 20ac + 40bc.

### ⚠️ Common Mistakes
- ❌ Sign errors when applying (x − y)² → ✅ Note middle term is −2xy.
- ❌ Forgetting the all-cross-products in (x+y+z)² → ✅ Six terms total: x²+y²+z² + 2(xy+xz+yz).

> **Quick Recall:**
> - x² − y² = (x+y)(x−y) — most reused identity.
> - (a+b+c)² = a² + b² + c² + 2(ab+bc+ca).
> - x³ + y³ + z³ − 3xyz factors via (x+y+z)(x²+y²+z²−xy−yz−zx).

### Connections
- Builds on: 2.2.3 polynomials.
- Continues into: 2.2.5 Algebra of Polynomials

---

## Section: Algebra of Polynomials (2.2.5) 🔴

### Core Idea
Polynomials are added/subtracted by combining *like terms* (terms identical except for their constant coefficients), and multiplied by distributing every term of one over every term of the other and collecting like terms. Sums/differences don't create new term types; products generally do.

> **In Simple Terms:** "3 cows + 4 cows = 7 cows" but "3 cows + 4 horses" stays as is. In math, 3x³ + 4x³ = 7x³, but 3x + 4x³ stays as 3x + 4x³ (or factors as x(3 + 4x²)).

### Key Concepts

#### Like Terms vs Unlike Terms
- **Like terms**: identical except for their constant parts.
  - 17x²y³ and −39x²y³ are like terms; sum simplifies to (17 − 39)x²y³ = −22x²y³.
- **Unlike terms**: differ in at least one variable's exponent.
  - 17x²y³ and −39x³y² are unlike (cannot be combined as a single term). Sum 17x²y³ + (−39x³y²) may be partially factored as x²y²(17y − 39x).

#### Sum / Difference of Two Polynomials
Process: collect like terms, add/subtract their coefficients.
- For subtraction P − Q, first form R from Q by flipping every '+' to '−' and '−' to '+' (i.e., R = −Q), then compute P + R.

### Examples
**Example: Sum**
P(x,y) = 3x² − 5xy + 3x + 8;  Q(x,y) = 6y² + 12xy − 5x + 16
P + Q = 3x² + (−5+12)xy + (3−5)x + (8+16) + 6y²
     = 3x² + 7xy + 6y² − 2x + 24.

**Example: Difference**
For same P, Q: form R = −6y² − 12xy + 5x − 16.
P − Q = P + R; collect like terms.

#### Product of Two Polynomials
- Simple case: one factor is a constant. Multiply each term by the constant.
  - P(x,y) = 3x² − 5xy + 3x + 8; Q = 7. P × Q = 21x² − 35xy + 21x + 56.
- General: if P = T₁ + T₂ + ... + Tₘ and Q = S₁ + S₂ + ... + Sₙ, then
  P × Q = Σᵢⱼ TᵢSⱼ over i = 1..m, j = 1..n.
- **Term-product rule:** multiply the constants and *add* the powers of each variable that appears.
  - T = 5x²y³, S = −16xyz⁵ ⟹ T × S = (5)(−16)·x²⁺¹·y³⁺¹·z⁰⁺⁵ = −80 x³y⁴z⁵.

**Example: Product**
P(x,y) = 4x − 3y + 5; Q(x,y) = 2x − 7.
(4x − 3y + 5)(2x − 7)
= 4x(2x − 7) − 3y(2x − 7) + 5(2x − 7)
= [8x² − 28x] + [−6xy + 21y] + [10x − 35]
= 8x² − 18x − 6xy + 21y − 35.

### CYP 3 Q1
For P(x, y) = 4x² − 3xy + 5y, Q(x, y) = −4x² − 3xy + 5y²:
- (i) Sum P + Q = (4x² − 4x²) + (−3xy − 3xy) + (5y + 5y²) = −6xy + 5y + 5y² = −6xy + 5y(1 + y) = y[−6x + 5(1+y)]
- (ii) Difference P − Q = [4x² − 3xy + 5y] + [4x² + 3xy − 5y²] = 8x² + 5y − 5y² = 8x² + 5y(1 − y).

### ⚠️ Common Mistakes
- ❌ Combining 17x²y³ with −39x³y² (unlike) → ✅ Cannot simplify as single term.
- ❌ Multiplying powers instead of adding when doing term × term → ✅ Add the exponents of each variable.

> **Quick Recall:**
> - Add/subtract: collect like terms.
> - Multiply terms: multiply coefficients, **add** exponents per variable.
> - Multiply polynomials: distribute every term against every term, then collect.

### Connections
- Continues into: 2.3 Solving polynomial equations.

---

## Section: Solving Polynomial Equations — Linear (2.3, 2.3.1, 2.3.2) 🔴

### Core Idea
Of all polynomial equations, the course focuses on four solvable types: (i) single linear in one variable, (ii) single linear in two variables, (iii) systems of linear equations, (iv) quadratic in one variable. A linear equation has every variable-bearing term of degree 1.

> **In Simple Terms:** Linear means "straight-line": every variable shows up at most to the first power, and there are no products of variables, no logs, no exponentials.

### Definitions
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

### 2.3.1 Solving Linear Equations in One Variable
General form: ax + b = cx + d, with a ≠ c (else the equation reduces to b = d, no variable).

**Rules:**
1. Move all variable terms to one side (typically LHS), all constants to the other (RHS).
2. When a term switches sides, its sign flips (+ ↔ −).

**Example: Solve 2x + 5 = 4 − 3x**
2x + 3x = 4 − 5
5x = −1
x = −1/5.

#### Reducing non-linear to linear (with caveat)
**Example:** (3x + 2)/(2x − 1) = 2  ... (i)
- (i) is NOT defined at x = 1/2.
- Cross-multiply: 3x + 2 = 2(2x − 1) ... (ii)
- (ii) IS defined at x = 1/2; (i) and (ii) are equivalent **except** at x = 1/2.
- Solve (ii): 3x − 4x = −2 − 2 = −4 ⟹ −x = −4 ⟹ x = 4.
- Since 4 ≠ 1/2, x = 4 is also a solution of (i). ✓

### 2.3.2 Single Linear Equation in Two Variables
General form: Ax + By + C = Dx + Ey + F. Rewrite as (A − D)x + (B − E)y + (C − F) = 0, then in the form ax + by = c.

**Cases:**
| Case | Condition | Result |
|------|-----------|--------|
| (a) | a = 0, b = 0 | reduces to c = 0; not linear; may be false |
| (b) | a = 0, b ≠ 0 | by = c — linear in one variable |
| (c) | a ≠ 0, b = 0 | ax = c — linear in one variable |
| main | a ≠ 0, b ≠ 0 | y = (−ax + c)/b; **infinitely many** (x, y) solutions |

**Example: Solve 3x − 2y + 4 = 4x + 3y − 5**
−2y − 3y = 4x − 3x − 5 − 4
−5y = x − 9
y = (9 − x)/5
Infinitely many solutions: (1, 8/5), (2, 7/5), (3, 6/5), (4, 1), ...

### Connections
- Continues into: 2.3.3 Systems of equations; 2.3.4 Quadratics

---

## Section: 2.3.3 System of Two Linear Equations in Two Variables 🔴

### Core Idea
For a 2×2 linear system ax + by = c, dx + ey = f, one of the standard methods is the *elimination* technique: scale equations to make one variable's coefficients match (or be opposites), then add/subtract to eliminate that variable. (General m×n systems are deferred to the matrices/determinants units.)

> **In Simple Terms:** Make the x-coefficients (or y-coefficients) cancel, solve for the other variable, then back-substitute.

### Mechanisms / Processes
1. Multiply (i) by d (the coefficient of x in (ii)), and (ii) by (−a) (or by a and subtract).
2. Add corresponding terms → equation in y only.
3. Solve for y.
4. Substitute y back into either original equation to get x.

### Examples
**Example: Solve 3x − 5y = −9 ...(iii); 2x + 3y = 13 ...(iv)**
- Multiply (iii) by 2: 6x − 10y = −18  ...(iii′)
- Multiply (iv) by 3: 6x + 9y = 39    ...(iv′)
- (iii′) − (iv′): −10y − 9y = −18 − 39 ⟹ −19y = −57 ⟹ y = 3.
- Substitute y = 3 in (iii): 3x − 5(3) = −9 ⟹ 3x = 6 ⟹ x = 2.
- Unique solution: (x, y) = (2, 3). ✓

### Connections
- Continues into: 2.3.4 Quadratic equations; matrices/determinants in later units.

---

## Section: 2.3.4 Quadratic Equations 🔴

### Core Idea
The general quadratic is ax² + bx + c = 0 with a ≠ 0. Its two roots (not necessarily distinct) are given by the quadratic formula. The discriminant b² − 4ac determines whether the roots are real-equal, real-distinct, or complex conjugates.

> **In Simple Terms:** One formula handles every quadratic; the sign of b² − 4ac tells you the kind of answer to expect.

### Key Concepts

#### Quadratic Formula
i)  x = [−b + √(b² − 4ac)] / (2a)
ii) x = [−b − √(b² − 4ac)] / (2a)

If b² − 4ac = 0, the two roots coincide.

(Continues into Chunk 007, where the three discriminant cases are illustrated with worked examples.)

### Connections
- Continues into: Chunk 007 (discriminant cases, worked examples)
- Builds on: linear equations (2.3.1, 2.3.2, 2.3.3)
