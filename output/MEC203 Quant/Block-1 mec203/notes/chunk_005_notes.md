# Chunk 005 — Unit 1 Answers/Exercises and Start of Unit 2 (Symbols, Variables, Mathematical Expressions)
<!-- Pages: 41-50 -->
<!-- Source: chunk_005.txt -->

## Section: Unit 1 — Answers/Hints to Check Your Progress Exercises 🟡
<!-- Continues from: Unit 1 (Chunks 001-004) -->

### Core Idea
This section provides solutions and hints for the five "Check Your Progress" sets in Unit 1 (Fundamental Concepts of Mathematics), covering set definition, set equality/subset relations, convex sets and power sets, set operations (union, intersection, difference) on sets-of-sets, and decimal-to-rational conversion. These answers ratify the rigorous definitions established earlier in the unit.

> **In Simple Terms:** A worked-answer key — it confirms how to test whether a collection is a set, how to compare/operate on sets, and how to convert decimals to fractions.

### Key Concepts

#### CYP 1 — Identifying Sets
- (i), (ii) [empty], (vi) [4 elements, no repetition] are valid sets.
- (iii) "most renowned" and (iv) "most talented" are NOT sets — the defining property is not well-defined.
- (v) is generally not a set because repetition of elements is not allowed in set notation.

#### CYP 2 — Set Equality, Subset, True/False
- 1(i) X = Y; (ii) X ≠ Y because 15 ∈ Y, 15 ∉ X; (iii) X ≠ Y because 2 ∈ X, 2 ∉ Y; (iv) X = Y.
- 2(i) X ⊂ Y (IGNOU has students enrolled in other disciplines); (ii) X ⊄ Y and Y ⊄ X; (iv) X ⊂ Y; (v) X ⊄ Y as 2 ∈ X, 2 ∉ Y; Y ⊄ X as {2,3} ∈ Y, {2,3} ∉ X.
- 3 True/False answers: (i) F, (ii) F, (iii) F, (iv) T, (v) T, (vi) F, (vii) T.

#### CYP 3 — Convexity, Power Sets
- Convexity: (i) is convex; (ii) is NOT convex.
- Power-set count for the 6-element universe: 2⁶ = 64 subsets.
- Proper non-empty subsets = 64 − 2 = 62 (exclude U itself and ∅).
- Listed subsets containing d: {d}, {a,d}, {a,b,d}, {a,c,d}, {a,b,c,d}, {b,d}, {b,c,d}, {c,d}.

#### CYP 4 — Set Operations on Sets-of-Sets
For X = {1, {2,3}, {4,5}, 6} and Y = {1, {2,4}, {5,6,7}}:
- X ∪ Y = {1, {2,3}, {4,5}, 6, {2,4}, {5,6,7}}
- X ∩ Y = {1}
- X − Y = {{2,3}, {4,5}, 6}
- Y − X = {{2,4}, {5,6,7}}

#### CYP 5 — Decimal to Rational
- 18725.4625 = 187254625/10000; simplify by dividing numerator and denominator by 25 then again by their G.C.D.
- 2.31/12 = 2.58333... = 2.58 3̄ (the 3 repeats; bar notation).

### Examples
**Example: Power set of X = {1, {2,3}}**
X has 2 elements. P(X) has 2² = 4 elements:
P(X) = {∅, {1}, {{2,3}}, {1, {2,3}}}.

**Example: De Morgan's Laws (statement and proof)**
The two laws (in English):
- The complement of the union of two sets equals the intersection of their complements.
- The complement of the intersection of two sets equals the union of their complements.

In symbols:
1. (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
2. (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ

**Proof of (i)** — Take an arbitrary x.
x ∈ (A ∩ B)ᶜ
⇔ x ∈ U and x ∉ A ∩ B (definition of complement)
⇔ x ∈ U and (x ∉ A or x ∉ B) (definition of ∩)
⇔ (x ∈ U and x ∉ A) or (x ∈ U and x ∉ B)
⇔ (x ∈ Aᶜ) or (x ∈ Bᶜ)
⇔ x ∈ Aᶜ ∪ Bᶜ. ∎

**Proof of (ii)** — analogous, starting with x ∈ (A ∪ B)ᶜ ⇔ x ∈ U and x ∉ A ∪ B ⇔ x ∉ A and x ∉ B ⇔ x ∈ Aᶜ ∩ Bᶜ.

### ⚠️ Common Mistakes
- ❌ Treating "the most talented students" as a set → ✅ Not a set (ill-defined membership)
- ❌ Counting U and ∅ when asked for proper non-empty subsets → ✅ Exclude both (62, not 64)

> **Quick Recall:**
> - A collection is a set only if membership is unambiguously defined.
> - |P(X)| = 2ⁿ where n = |X|.
> - De Morgan: complement of union = intersection of complements; complement of intersection = union of complements.
> - A set equality proof goes both ways via arbitrary element argument.

### Connections
- Builds on: set definitions and operations (Chunks 001-004)
- Prerequisite for: indicator/characteristic function arguments later, and for Boolean reasoning in Unit 2 Appendix.

---

## Section: Unit 2 — Structure, Objectives, Introduction 🟢

### Core Idea
Unit 2 (Overview of Basic Methods of Mathematics) lays out the toolkit for solving equations: clarifying the meaning of symbol, parameter, variable, constant; defining mathematical expression, equation, identity, polynomial; algebra of polynomials; and methods for linear (one/two/multi-variable) and quadratic equations. An appendix covers proof techniques.

> **In Simple Terms:** Unit 2 is the "how to do algebra cleanly" unit — it nails down what each symbol on the page actually means, then gives standard recipes for solving the basic equation types.

### Definitions
- **Unit Objectives** (after this unit, the learner can):
  - Explain symbol, parameter, variable, constant.
  - Distinguish among them.
  - Explain mathematical expression / formula / well-formed-formula, equation, solution/root of equation, zero of function, polynomial identity, polynomials, polynomial equations.
  - Use polynomial identities to solve problems.
  - Apply algebraic operations (add, subtract, multiply) to polynomials.
  - Solve linear equations (1 var, 2 var, system) and quadratic equations.

### Edge Cases & Caveats
- Fisher equation appears as motivating example: real interest rate ≈ nominal interest rate − inflation rate (≈ ≡ "approximately equal to").

### Connections
- Builds on: number systems, decimal representation (Unit 1)
- Continues into: Polynomials (Section 2.2.3), Solving Equations (Section 2.3)

---

## Section: Symbol, Parameter, Variable, Constant (2.2.1) 🔴

### Core Idea
A *symbol* is any notation that stands for something else. Constants, variables, and parameters are all kinds of symbols, distinguished by what kind of value they may take and the role they play in an equation.

> **In Simple Terms:** The word "lake" is a symbol — touching it doesn't get your finger wet. In math, x, c, 6 etc. are symbols too; what differs is whether the value is fixed (constant), free to vary (variable), or fixed-for-now-but-generic (parameter).

### Key Concepts

#### Symbol
A notation that represents something else. Touching the four-letter word *lake* does not get the finger wet, but touching the actual lake does. To talk about the word itself, write it as 'lake', "lake", or *lake*.

#### Parameter
A "hybrid of constant and variable" — a symbol that is held constant for the purpose of one analysis but can be set to different values to generate a family of problems.
- Example: in x² + y² = c (with real c > 0), c parameterises a family of circles of radius √c centred at origin.
- Setting c = 4 yields the circle x² + y² = 4 (radius 2); c = 15 yields radius √15.
- Significance: questions like "rectangle of maximum area inscribed in the circle" can be solved once for general c, then specialised — a parameter is a *generalised constant*.

#### Variable
A symbol which can be measured and which may change.
- Economics examples: price, interest-rate, wages, quantity-bought, quantity-sold.
- Value of variable at a particular time = its measurement at that time (e.g., 6% interest-rate today).
- A variable assumes only its *possible* values — e.g., √(−8) is not a possible value for "percentage-of-Interest-rate" but is a possible value for x in ax² + bx + c = 0.
- Naming convention: end letters x, y, z (and others) of Latin alphabet.

#### Constant
A symbol whose possible value is a unique single value.
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

### Connections
- Builds on: Set theory (Unit 1) — variable values come from a set of admissible values.
- Continues into: 2.2.2 Mathematical Expressions

---

## Section: Algebraic Concepts and Mathematical Expressions (2.2.2) 🔴

### Core Idea
A *mathematical expression* is a syntactically correct sequence of mathematical terms (constants, variables, parameters, relations, operations) built using the structuring rules of mathematics — analogous to a grammatical sentence in a natural language. Expressions are classified into arithmetic, polynomial, algebraic, and general; an *equation* is a mathematical expression containing exactly one '=' (and no other relations).

> **In Simple Terms:** Math has grammar too. Just like "the cat sat on mat" is grammatical English but "mat sat the on cat" is not, √(8 − y) is a valid expression but "−8√" or "y| |" is not.

### Key Concepts

#### Expression (general)
Whatever is constructed according to a language's structuring rules (its syntax/grammar) is an expression in that language.

#### Mathematical Expression — Construction Rules
1. **Atomic:** Each constant, variable, parameter is itself an ME. So 7, x, c, 14.78 are MEs.
2. **Unary operators** must be in correct position with one operand (constant/variable/parameter/ME containing no relational operator). Valid: √(8−y), (x+y)², eˣ⁺²ʸ⁻⁴ᶻ, log(3x+5), |y+56|. Invalid: −8√, x log, ᵉe, y| | (operator misplaced); √(8 < y), (36x = 49)² (operand contains relational operator).
3. **Binary operators** require two operands at correct positions. Valid: (√867 − eˣ⁺²ʸ), (x + 2y − 4z), (√(8−y) × (x+y)² + log(x − eʸ)). Invalid if any operand contains a relational operator or invalid sub-expression.
4. **Binary relations** require two operands that are themselves expressions without internal relations. So (√867 − eˣ⁺²ʸ) < (√(8−y) × (x+y)² + log(x − eʸ)) is valid, but (√867 = eˣ⁺²ʸ) < ((8−y)×(x+y) > log(x−eʸ)) is NOT (RHS contains '>').
   - Shorthand chain: x < y < z means "x < y and y < z" (similarly for ≤, >, etc.).
5. **Other expressions:** limits limₙ→∞(1+1/n)ⁿ, derivatives dy/dx, integrals ∫f(3x+2)dx — discussed in later units.

#### Classification of Mathematical Expressions
Each preceding type is a special case of the next.

| Type | Restriction | Example |
|------|-------------|---------|
| **Arithmetic** | No variables | (√(−8 + 489) × (7! + 56)² + log(155 − e⁹)) |
| **Polynomial** | Variables only with non-negative integer powers | 7x³ − 5x + 11; (x+y)² |
| **Algebraic** | Variables with rational powers p/q (q ≠ 0, p,q integers) | √(8−y); √(1+x²)/√(1−x²) |
| **General** | Anything constructible by syntax rules | log x, eˣ, dy/dx, ∫ |

Notes:
- Constants in a polynomial may have fractional powers (e.g., x² + (17)¹ᐟ² is polynomial because the variable x has integer power; 17 is a constant).
- √(8−y) = (8−y)¹ᐟ² is algebraic, NOT polynomial.

#### General Forms — Equation
An equation is a special expression with exactly one '=' relation and no other relation. Polynomial equation: both sides are polynomial expressions. Algebraic equation: both sides algebraic.
- Beyond algebraic: equations involving log, e, trigonometric functions; set-theoretic equations (e.g. (X ∩ Y)ᶜ = Xᶜ ∪ Yᶜ — actually an *identity*); logical equations; differential and integral equations.
- General form: any equation may be rewritten as f(x) = 0 (move RHS to LHS).

#### Root / Solution / Zero
- A *root/solution* of f(x) = 0 is a constant a such that f(a) = 0.
- Example: f(x) = x² − 4 = 0; f(2) = 4 − 4 = 0, so x = 2 is a root.
- We also say "2 is a *zero* of the function f(x)". The word "zero" applies to the **function** f, not the equation f(x) = 0.

#### Mathematical Identity vs Equation
| | Equation | Identity |
|---|---|---|
| Holds for | specific value(s) of variable | every value of the variable |
| Example | X² − 16 = 0 (only X = ±4) | X² − 16 = (X+4)(X−4) (every X, real or complex) |
| Symbol | = | ≡ (when emphasis needed) |

Test: with X = 3: LHS of identity = 9 − 16 = −7; RHS = (3+4)(3−4) = −7. ✓

#### Various Usages of '=' in Mathematics
| Usage | Example | More-specific symbol |
|-------|---------|----------------------|
| In equations | find x: x² + 4x + 3 = 0 | = |
| In identities/laws | (a+b)² = a² + b² + 2ab for all real a,b | ≡ |
| In conditional statements | "If x = 7, then ..." | = |
| In relations (T/F evaluations) | 3 = 4+2 (false), 3 = 2+1 (true) | = |
| In assignments | "Let x = 8" | := (Pascal-style) |
| In definitions | Area = length × breadth | ≜ (or ≡) |

### Examples
**Example: Expression vs Non-expression**
- |y + 56| is an ME (unary | | with single operand y+56).
- √(8 − y) × is NOT an ME (binary × missing right operand).
- log((8 < y) × (x+y)²) is NOT an ME (operand contains '<').

### Definitions
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

### Edge Cases & Caveats
- Parentheses must be paired. An expression like "log (x+y)²" with mismatched parentheses is not an ME.
- Relational operators inside operands of operators or other relations are forbidden.

> **Quick Recall:**
> - Expression ⊃ Algebraic ⊃ Polynomial ⊃ Arithmetic.
> - Polynomial: only non-negative integer powers of variables.
> - Equation: exactly one '='; identity: equation true for all values.
> - Zero of function f = root of equation f(x)=0.

### Connections
- Builds on: numbers, exponents (Unit 1)
- Continues into: 2.2.3 Polynomials (Chunk 006)

---

## Section: Mathematical Identity (2.2.2.5) and Usages of '=' (2.2.2.6) — Check Your Progress 1 🟡

### Examples (CYP 1 — page reference for solutions)
**Q (Chunk 005, p. 49):** Which of the following is not a mathematical expression? Justify.
(i) √|y + 56|, (ii) √(8−y) ×, (iii) log((8 < y) × (x+y)²), (iv) log(x+y)², (v) log(x+y)²

(Answers appear in Chunk 006 / Unit 2 answer key:)
- (i) and (iv) are MEs.
- (ii) is NOT an ME — multiplication symbol '×' must be followed by an expression.
- (iii) is NOT an ME — argument contains relational operator '<'.
- (v) is NOT an ME — has two left parentheses but only one right; an ME must have matching parentheses.

### Connections
- Continues into: Chunk 006 (CYP 1 answers reside in 2.6 of Unit 2)
