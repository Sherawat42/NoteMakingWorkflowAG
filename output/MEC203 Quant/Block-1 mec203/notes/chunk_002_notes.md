# Chunk 002 — Symbols Continued, Greek Letters, Unit 1 Intro & Set Theory Basics
<!-- Pages: 11-20 -->
<!-- Source: chunk_002.txt -->
<!-- Continues from: Mathematical Symbols/Notations (Chunk 001) -->
<!-- Continues into: Set relationships, special sets, operations (Chunk 003) -->

## Section: Mathematical Notations (continued) — Functions, Derivatives, Norms 🔴
<!-- Continues from: Symbols table (Chunk 001) -->

### Core Idea
This continuation of the symbol table introduces the notation for scalar functions (one and two variables), first- and second-order derivatives, partial derivatives, the Hessian matrix, scalar product of vectors, determinants, Euclidean and non-Euclidean metrics, norms, time as discrete vs continuous variable, and the gradient operator. These are the building blocks of calculus, optimisation, and real analysis throughout MEC-203.

> **In Simple Terms:** This is "calculus shorthand." Once you internalise these symbols (∂, ∇, |·|, det), you can read formulas in optimisation and real analysis at a glance instead of decoding every term.

### Definitions ⭐

#### Functions
- **y = f(x)**: Scalar function of one variable. x is the independent variable (argument / input); y is the dependent variable (value of the function). ⭐
- **y = f(x₁, x₂)**: Scalar function of two variables. x₁, x₂ are independent variables; y is the value.

#### Derivatives (One Variable)
- **dy/dx, y′, f′(x)**: First-order derivative of y = f(x). ⭐
- **d²y/dx², y″, f″(x)**: Second-order derivative of y = f(x).
- **df(x)/dx |_{x = x̄}**: Value of a one-variable derivative evaluated at point x = x̄.

#### Partial Derivatives (Several Variables)
- **∂y/∂xᵢ, ∂f(x₁, x₂)/∂xᵢ**: First-order partial derivatives of f(x₁, x₂) with respect to xᵢ for i = 1, 2. ⭐ (NOTE: source OCR shows "0x" / "Ox" / "&" — these are the partial derivative symbol ∂)
- **∂²f(x₁, x₂)/(∂xᵢ ∂xⱼ), ∂²f(x₁, x₂)/∂xᵢ²**: Second-order partial derivatives of f(x₁, x₂).
- **∂f(x₁, x₂)/∂xᵢ |_{x = (x̄₁, x̄₂)}**: Value of a partial derivative evaluated at a specified point.

#### Hessian Matrix
- **H(x₁, x₂)**: Hessian — the symmetric matrix of second-order partial derivatives of f(x₁, x₂):

$$H(x_1, x_2) = \begin{bmatrix} \dfrac{\partial^2 f(x_1, x_2)}{\partial x_1^2} & \dfrac{\partial^2 f(x_1, x_2)}{\partial x_1 \partial x_2} \\[2pt] \dfrac{\partial^2 f(x_1, x_2)}{\partial x_2 \partial x_1} & \dfrac{\partial^2 f(x_1, x_2)}{\partial x_2^2} \end{bmatrix}$$

#### Vector & Matrix Operations
- **(p · x) = Σᵢ₌₁ⁿ pᵢ xᵢ**: Scalar (dot) product of two vectors p, x ∈ Rⁿ. ⭐
- **det(A) or |A|**: Determinant of matrix A. ⭐

#### Distance / Metric / Norm
- **dₑ(x¹, x²) = √[Σ (xᵢ¹ − xᵢ²)²]**: Euclidean metric (distance between two vectors). ⭐
- **d(x¹, x²) = max_{i=1,2} |xᵢ¹ − xᵢ²|**: Non-Euclidean (max / Chebyshev) metric.
- **‖x‖** (Euclidean norm): standard length of vector x.
- **‖x‖ = max_{i=1,2} |xᵢ|**: Non-Euclidean (sup) norm.

#### Time
- **t = 0, 1, 2, …**: Time as a **discrete** variable (used in difference equations, Block 6).
- **t ∈ [0, +∞)**: Time as a **continuous** variable (used in differential equations, Block 6).

#### Gradient
- **∇f, grad f**: Gradient of function f. **∇f = (∂f/∂x₁, …, ∂f/∂xₙ)**. ⭐

### ⚠️ Common Mistakes
- ❌ Writing dy/dx for a multi-variable function. → ✅ Use ∂y/∂xᵢ (partial derivative) when there are several independent variables.
- ❌ Confusing **|A|** (determinant of matrix) with **|x|** (absolute value of scalar) or **‖x‖** (norm of vector). → ✅ Context: matrix → determinant; scalar → absolute value; vector → norm.
- ❌ Forgetting that the Hessian must be **symmetric** (under Young's theorem when mixed partials are continuous): ∂²f/(∂x₁∂x₂) = ∂²f/(∂x₂∂x₁).

> **Quick Recall:**
> - First derivative: **dy/dx**, **f′(x)**.
> - Partial derivative: **∂f/∂xᵢ**.
> - Hessian = matrix of 2nd-order partials.
> - Dot product: **p · x = Σ pᵢxᵢ**.
> - Gradient: **∇f = (∂f/∂x₁, …, ∂f/∂xₙ)**.
> - Euclidean distance: **dₑ = √Σ(xᵢ − yᵢ)²**.

### Connections
- Used in Block 3 (Calculus, Units 9–12), Block 4 (Real Analysis, especially metric space — Unit 15), and Block 5 (Optimisation — Hessian determines second-order conditions for max/min).

---

## Section: Greek Alphabet Reference 🟡

### Core Idea
A reference table of Greek letters commonly used as symbols in mathematics and economics throughout the course.

### Definitions
| Symbol | Greek Alphabet | Symbol | Greek Alphabet |
|---|---|---|---|
| α | Alpha | θ | Theta |
| β | Beta | λ | Lambda |
| γ | Gamma | π | Pi |
| δ / Δ | Delta | σ | Sigma |
| ε | Epsilon | χ | Chi |
| ψ | Psi | μ | Mu |
| ρ | Rho | ω | Omega |

### Connections
- α, β commonly used as parameters (e.g., elasticities); λ for Lagrange multipliers (Block 5); π for circle constant or for profit; σ, μ for population standard deviation and mean (Block 8 onward); ε for arbitrarily small positive number in real analysis.

---

## Section: Unit 1 Structure & Objectives 🟢

### Core Idea
Unit 1 of Block 1 ("Fundamental Concepts of Mathematics") covers two foundational pillars — set (the basis of modern mathematics) and number (the basis of conventional mathematics) — and provides a working vocabulary for every later unit.

### Key Concepts

#### Unit 1 Structure (Detailed Outline)
- **1.0** Objectives
- **1.1** Introduction
- **1.2** Set Theory
  - 1.2.1 Concept of Set
  - 1.2.2 Notations
  - 1.2.3 Forms of Set Representation
  - 1.2.4 Relationships Between Sets (notation, definitions, examples; establishing relationships)
  - 1.2.5 Some Special Sets (Universal, Null, Power, Convex)
  - 1.2.6 Quantifiers and Logical Symbols / Operators
  - 1.2.7 Conceptual Clarifications (Relation vs Operation; set operations; further clarifications)
- **1.3** Numbers: From Natural to Complex
  - 1.3.1 Standard Number Sets
  - 1.3.2 R, the Set of Real Numbers
  - 1.3.3 Real Number Intervals
  - 1.3.4 Complex Numbers
  - 1.3.5 Number Miscellany
  - 1.3.6 Properties of Real Numbers as Ordered Field
- **1.4** Decimal Representation of Rational and Irrational Numbers
- **1.5** Real Number Exponentiation
- **1.6** Let Us Sum Up
- **1.7** Key Words
- **1.8** Answers/Hints to Check Your Progress Exercises
- **1.9** Exercises

#### Unit 1 Learning Objectives ⭐
After this unit a student should be able to:
- Differentiate between concept, term, notation, and definition of number.
- Explain the concept of set.
- Use set notation.
- Find relations on sets.
- Apply set operations.
- Differentiate between 'relation' and 'operation' on sets.
- Discuss relations and operations on numbers and their properties.
- Define various types of numbers.
- Apply operations on numbers and use their properties in numerical problem solving.
- Express real numbers (including irrational numbers) as decimal numbers.
- Apply rules of exponentiation of numbers.

---

## Section: Concept, Term, Notation, and Number System 🟡

### Core Idea
Before formal mathematics, one must distinguish four related ideas about a number: the **concept** (the abstract idea, e.g., "twoness"), the **term/name** (the word, e.g., "two", "zwei"), the **notation/numeral/symbol** (the written sign, e.g., 6, VI, ६), and the **numeral system** (the rule for combining symbols, e.g., decimal, Roman, binary).

> **In Simple Terms:** "Twoness" is the idea, "two" is the English name, "2" is the symbol, and "decimal system" is the rule for writing numbers down. They are four different things even though we use them interchangeably in everyday life.

### Key Concepts

#### Number Concept
The idea/sense that distinguishes Fig. 1(a) (one horse) from Fig. 1(b) (two horses) and recognises Fig. 1(b) and Fig. 1(c) as sharing "twoness" despite the difference in objects (horses vs marble elephants). The concept is the abstraction shared.

#### Number Name / Term
The linguistic label for a concept. Different languages give different names: English "two", Hindi "दो", German "zwei", Tamil "இரண்டு" / "Irantu". The textbook also notes that one term can map to several concepts ("bank" = river bank vs financial institution).

#### Numeral / Number-Notation / Number-Symbol
The written representation of a number. For "six": the numerals **6** (decimal), **VI** (Roman), **६** (Devanagari) all denote the same concept. Strictly speaking, **6 is the name (numeral) of a number, not the number itself**, but in mathematics it is conventional to call numerals "numbers".

#### Term, Notation, and Definition (Example: Square Root)
- **Term**: "square root".
- **Notation/Symbol**: √.
- **Definition**: For a given number x, its square root y is a number satisfying y × y = x (where multiplication is already understood).

#### Numeral System (System of Numeration)
A system for representing numbers. Examples:

| Decimal | Roman | Binary |
|---|---|---|
| 47 | XLVII (source OCR: "XZP") | 101111 (source OCR: "101001") |

The same expression "111" represents:
- **111** (one hundred eleven) in **decimal**.
- **7** (seven) in **binary**.
- **3** (three) in **unary**.

> Note: the textbook distinguishes "Numeral System" from "Number System"; the latter (different concept) is discussed later.

### ⚠️ Common Mistakes
- ❌ Calling 6 a "number". → ✅ Strictly, 6 is a numeral (name/symbol); the number is the concept "sixness". The textbook accepts the loose usage.
- ❌ Assuming "111" always means one hundred eleven. → ✅ Its meaning depends on the numeral system (base) used.

### Connections
- Builds on: everyday counting intuition.
- Prerequisite for: §1.3 (Numbers: From Natural to Complex), where formal number sets N, W, Z, Q, R, C are introduced (Chunk 004).

---

## Section: Set Theory — Concept of Set 🔴

### Core Idea
A **set** is a well-defined collection of distinctly identifiable objects (its members or elements), with no element repeated. Modern mathematics (since the mid-20th century) treats "set" as the most fundamental undefined concept — even numbers and geometrical shapes are now defined in terms of sets.

> **In Simple Terms:** A set is like a labelled box: each item inside is uniquely identifiable, no item is duplicated, and you can always say with certainty whether any given thing is or isn't in the box.

### Key Concepts

#### What Counts as a Set?
A collection is "well-defined" iff:
1. The entities in it are **distinctly identifiable**, AND
2. For any entity in the world, we can say definitively whether it belongs to the collection or not.

**Examples that ARE sets:**
- All IGNOU students who enrolled in 2021 for M.A. (Economics).
- The set of decimal digits {0, 1, 2, …, 9}.

**Examples that are NOT sets:**
- "Some of the IGNOU students enrolled in 2021 for M.A. Economics" — vague (which "some"?).
- "All drops of water in a glass" — drops are not distinctly identifiable.
- The barber paradox collection (see below).

#### The Barber Paradox (Russell-style)
> A small village has only one (male) barber, who shaves all those, and only those, males who do not shave themselves. Let X = collection of all villagers shaven by the barber. Then it is not possible to tell whether the barber belongs to X.
>
> - If the barber shaves himself, then by the rule he is shaven only by those who don't shave themselves — contradiction.
> - If the barber does not shave himself, then by the rule he must be shaven by the barber (himself) — contradiction.
>
> Therefore X is not well-defined and not a set.

### Definitions ⭐
- **Set** (working definition): a well-defined collection of distinctly identifiable objects, with no member repeated. ⭐
- **Member / Element**: any entity belonging to a set. ⭐

### ⚠️ Common Mistakes
- ❌ Listing the same element twice in a set: {1, 2, 2, 3}. → ✅ A set has no repeated members; this is the same as {1, 2, 3}.
- ❌ Treating any vague collection ("tall people", "good students") as a set. → ✅ Only well-defined collections are sets.

### Connections
- Builds on: notion of "collection".
- Prerequisite for: all subsequent topics — set notation, relationships between sets, set operations, functions, relations.

---

## Section: Set Notations 🔴

### Core Idea
Sets are denoted with **braces { }**. Members are listed inside the braces, separated by commas. The membership symbol **∈** (epsilon) means "is an element of"; **∉** means "is not an element of". By convention, sets are named with capital letters and elements with lower-case letters (though this is not binding).

### Key Concepts

#### Basic Notation
Example: **Num-Digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}**.
- 0 ∈ Num-Digits, 5 ∈ Num-Digits, 9 ∈ Num-Digits.
- 35 ∉ Num-Digits.

#### Naming Convention
- Set names → start with capital letters (X, Y, N, Num-Digits).
- Elements → lower-case letters (a, b, x, y).
- Names should be **mnemonic** (helpful for remembering contents).

#### Extension for Large/Infinite Sets — Triple Dots "…"
When a set has very many or infinitely many elements with a clear pattern, list a few initial members and use "…":
- {0, 1, 4, 9, …, 100, 121, …, 400, …, 10000} or briefly {0, 1, 4, 9, …, 10000} for squares ≤ 10000.
- This set may be named **Sq_int_less_10001**.

### Definitions
- **∈**: "is an element of" / "belongs to". ⭐
- **∉**: "is not an element of" / "does not belong to". ⭐

---

## Section: Forms of Set Representation 🔴

### Core Idea
Sets can be written in two standard forms: **roster (tabular) form**, listing all elements explicitly inside braces, and **set-builder form**, describing the property the elements share.

### Key Concepts

#### (i) Tabular / Roster Form
Each element (or enough to indicate a pattern) is listed inside braces.
- **Sq_int_less_10001 = {0, 1, 4, 9, …, 10000}**.
- Convenient for small sets; awkward for large or infinite sets.

#### (ii) Set-Builder Form
States the defining property/properties of members. Format: **{x : (conditions on x)}** — the colon ":" (or "|") is read as "such that" or "where".
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

> **Quick Recall:**
> - **{ }** = set; **∈** = belongs to; **∉** = does not belong.
> - Roster form: list elements.
> - Set-builder form: **{x : property of x}**.
> - Triple dots "…" indicate a continuing pattern.

### Connections
- Builds on: §1.2.1 Concept of Set.
- Prerequisite for: §1.2.4 Relationships Between Sets, §1.2.5 Special Sets, §1.2.7 Set Operations (Chunk 003).

### Open Questions
- When a set is described in set-builder form, who decides the universe of x — the surrounding context, or must it be stated explicitly?
