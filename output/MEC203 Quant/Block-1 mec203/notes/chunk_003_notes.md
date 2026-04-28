# Chunk 003 — Cardinality, Set Relationships, Special Sets, Quantifiers, Operations
<!-- Pages: 21-30 -->
<!-- Source: chunk_003.txt -->
<!-- Continues from: Set notation & forms (Chunk 002) -->
<!-- Continues into: Set operations completion, numbers from natural to complex (Chunk 004) -->

## Section: Cardinality of a Set 🔴

### Core Idea
The **cardinality** of a set X, denoted **|X|** or **#X**, is the number of distinct elements in X. Two unequal sets can have the same cardinality.

> **In Simple Terms:** Cardinality is the size of a set — how many things are in the box, ignoring what those things are.

### Definitions ⭐
- **|X| or #X**: cardinality of X = number of distinct elements. ⭐

### Examples
- **|{1, 3, 5}| = 3**.
- **|∅| = 0** (the empty set has 0 elements).
- **|N| = |W| = |Z| = |Q| = ∞** (all are infinite — countably infinite, by later results).
- **|{0}| = 1**.
- **|{1, 3, 5}| = |{1, 3, 7}| = 3** even though {1, 3, 5} ≠ {1, 3, 7} — equal cardinality does not imply equal sets.

### Connections
- Cardinality is used in §1.2.5 (Power Set: |P(A)| = 2^|A|).

---

## Section: Check Your Progress 1 🔴

### Core Idea
Practice questions on the concept of "set" — whether collections are sets, expressing them in roster/set-builder form, and computing cardinality. (Answers appear later in §1.8 — mark as ⭐ exam-relevant.)

### Examples / Exercises ⭐

**Q1.** Which of the following collections are sets? Justify.
- (i) The collection of all months of a year beginning with letter **M**.
- (ii) The collection of all months of a year beginning with letter **Z**.
- (iii) The collection of ten **most talented** living writers of the world.
- (iv) A team of eleven **most renowned** football players of the world.
- (v) **{1, 2, 2, 3}**.
- (vi) **{1, 2, {2, 3}, 3}**.

**Q2.** For each, write in roster/tabular form and give cardinality:
- (a) Positive prime integer factors of 180.
- (b) Solutions of the quadratic equation x² − 3x − 10 = 0.

**Q3.** Tell which is a set; if it is, (i) write in set-builder form, (ii) state cardinality:
- (a) {6, 9, 12, 15, 18, 21, 24, 27}.
- (b) {2, 4, 8, 16, …}.
- (c) {{1}, {1, 2}, {1, 2, 3}, …, {1, 2, 3, 4, …, 10}}.

> **Quick Recall:**
> - "Most talented" / "most renowned" → **subjective**, not well-defined → **not a set**.
> - {1, 2, 2, 3} = {1, 2, 3}, cardinality 3 (a set, though redundantly written).
> - {1, 2, {2, 3}, 3} has 4 distinct elements: 1, 2, the set {2, 3} (treated as a single element), and 3.

---

## Section: Relationships Between Sets — Equality, Subset, Proper Subset 🔴

### Core Idea
For any two sets X and Y, four main relationships are studied: **equality (=)**, **subset / superset (⊆)**, **proper subset / superset (⊂)**, and **not a subset (⊄)**.

> **In Simple Terms:** Sets can be the same as each other (equal), one can sit inside the other (subset), one can sit *strictly* inside the other with room to spare (proper subset), or they can be unrelated (not a subset).

### Definitions ⭐

#### (i) Equality of Sets — X = Y
Two sets X and Y are **equal** iff every element of X is an element of Y AND every element of Y is an element of X.
- **Notation**: X = Y.
- **Example**: X = {1, 2, 3, 4, 5}, Y = {x : x is a natural number with 1 ≤ x ≤ 5}, W = {3, 5, 2, 4, 1}. Then **X = Y = W** (order does not matter).

#### (ii) Subset / Superset — X ⊆ Y
X is a **subset** of Y if every element of X is also an element of Y. Equivalently: Y is a **superset** of X / X is contained in Y / Y contains X.
- **Notation**: X ⊆ Y.
- **Examples**:
  - X = {a, e, i}, Y = set of all English vowels → X ⊆ Y.
  - **Every set is a subset of itself**: X ⊆ X.

#### (iii) Proper Subset / Proper Superset — X ⊂ Y
X is a **proper subset** of Y if (a) every element of X belongs to Y, AND (b) there is at least one element of Y that does not belong to X.
- **Notation**: X ⊂ Y (also "Y is a proper superset of X").
- **Example**: X = {0, 2, 4, 6, 8} (even decimal digits), Y = {0, 1, 2, …, 9} (all decimal digits). Then X ⊂ Y, since every even digit is a digit, but 1 ∈ Y and 1 ∉ X.
- Note: **X ⊄ X** as a proper subset, because condition (b) fails.

#### (iv) Not a Subset — X ⊄ Y
X ⊄ Y means there exists at least one element of X that does not belong to Y.
- **Example**: X = {1, 5, 10, 15}, Y = {1, 12, 14, 15}. Since 5 ∈ X and 5 ∉ Y, X ⊄ Y. (One witness suffices.)

### Edge Cases & Caveats
- **Notation conflict (textbook remark)**: Some authors use **⊂** for "subset (possibly improper)" and **⊊** for "proper subset". This textbook uses **⊆** for subset and **⊂** for **proper** subset. Be careful when reading other texts.

### ⚠️ Common Mistakes
- ❌ Writing X ⊂ X (claiming a set is a proper subset of itself). → ✅ X ⊆ X is true; X ⊂ X is false (no element of X is "extra").
- ❌ To prove X ⊄ Y, listing all elements not in Y. → ✅ Only one counter-example element is needed.

---

## Section: Establishing Set Relationships 🟡

### Core Idea
A worked methodology for showing each kind of set relationship, using the example sets:
- **A** = {x : x² + 3x + 2 = 0} (roots of the quadratic).
- **B** = {−1, −2}, **C** = {−2}, **E** = {0, −1, −2}.

### Mechanisms / Processes

1. **"Is not a subset" (easiest)**: find one element of the candidate subset that is not in the candidate superset.
   - E ⊄ C, since 0 ∈ E but 0 ∉ C.
   - E ⊄ A, since 0 ∈ E but 0 is not a root of x² + 3x + 2 = 0.

2. **Subset (B ⊆ E)**: take each element of B in turn and verify it lies in E. (For complex cases, take an arbitrary element x ∈ B and show x ∈ E.)

3. **Proper subset (B ⊂ E)**: do step 2, then additionally show there exists an element of E not in B.
   - 0 ∈ E but 0 ∉ B → B ⊂ E (proper).

4. **Equality (A = B)**: do step 2 in **both directions** (show A ⊆ B and B ⊆ A).
   - −1 ∈ B is a root of x² + 3x + 2 = 0, so −1 ∈ A. Similarly −2 ∈ B is a root, so −2 ∈ A. Conversely, since x² + 3x + 2 = 0 is quadratic, it has exactly two roots: −1 and −2. Hence A = B.

> **Quick Recall:**
> - Subset: every element of X is in Y.
> - Proper subset: subset + at least one element of Y not in X.
> - Equality: subset both ways.
> - Not subset: one counter-example suffices.

---

## Section: Check Your Progress 2 🔴

### Examples / Exercises ⭐

**Q1.** Whether X = Y or not (with explanation):
- (i) X = {2, 4, 6, 8, 10}, Y = {x : x is positive even integer and x ≤ 10}.
- (ii) X = {x : x is a multiple of 10}, Y = {10, 15, 20, 25, 30, …}.
- (iii) X = {2, 3}, Y = {x : x is a solution of x² + 5x + 6 = 0}.
- (iv) X = {x : x is a letter in the word FOLLOW}, Y = {y : y is a letter in the word WOLF}.

**Q2.** Find the correct relation among X ⊆ Y, Y ⊆ X, X ⊂ Y, Y ⊂ X, X = Y, etc.:
- (i) X = {x : x is a student enrolled in IGNOU and having Economics as one of the courses}, Y = {x : x is a student enrolled in IGNOU}.
- (ii) X = {x : x is a triangle in a plane}, Y = {x : x is a rectangle in the plane}.
- (iii) X = {x : x is an even natural number}, Y = {x : x is an integer}.
- (iv) X = {1, 2, 3} and Y = {1, {2, 3}, 4, 5}.

**Q3.** For X = {1, {2, 3}, 3, 4}, which are true?
- (i) 2 ∈ X, (ii) ∅ ∈ X, (iii) ∅ ⊄ X, (iv) ∅ ⊆ X, (v) {2, 3} ∈ X, (vi) {2, 3} ⊂ X, (vii) {{2, 3}} ⊂ X.

### Edge Cases & Caveats
- In Q3, note carefully the difference: {2, 3} is an element of X (so {2, 3} ∈ X is **true**), but {2, 3} is **not** a subset of X (the elements 2 and 3 individually are not elements of X).

---

## Section: Special Sets — Universal, Null/Empty, Power, Convex 🔴

### Core Idea
Four types of sets recur repeatedly: the **Universal set** U (the "everything" of a problem context), the **Null/Empty set** ∅ (no members), the **Power set** P(A) (all subsets of A), and **Convex sets** (geometric: line segments stay inside).

> **In Simple Terms:** Universal = the playing field; Empty = nothing; Power = every possible team you could form; Convex = a "no dents" set — straight lines never poke outside.

### Key Concepts

#### a) Universal Set (U)
For any problem, a sufficiently large set containing all entities under discussion is fixed; this is the **Universal set**, denoted **U**. By definition, every set X under consideration satisfies **X ⊆ U**.

**Remarks:**
- Different problems → different universal sets.
- Since X ⊆ X always, we have **U ⊆ U**.
- The concept is **controversial** — leads to paradoxes such as **Russell's paradox** ("the set of all sets" is not a well-defined set, hence not a set). Despite this, the concept is practically very useful.

#### b) Empty / Null / Void Set (∅)
A set with no members. Denoted **∅** or **{ }**.
- **Example**: S = {x : x is an even integer and x² = 9} → no integer satisfies both, so S = ∅.
- **Key fact**: **∅ ⊆ X for every set X**. ⭐

**Proof by contradiction**: Suppose ∅ ⊆ X is false. Then ∃ x ∈ ∅ with x ∉ X. But by definition no element is in ∅ — contradiction. Hence ∅ ⊆ X.

**Convention on "proper" subsets**: Both ∅ and X itself are subsets of X but are **not counted as proper subsets**. All other subsets are proper.

#### c) Power Set — P(A) or 2^A
The set of **all subsets** of A.
- **Example**: A = {1, 2, 3} →
  P(A) = {∅, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
- The notation **2^A** is used because |P(A)| = 2^|A|.

**Important Results on Subsets** (stated without proof):
1. A ⊆ A (every set is a subset of itself).
2. **Transitivity**: if A ⊆ B and B ⊆ C, then A ⊆ C.
3. If A ⊆ B and B ⊆ A, then A = B.
4. If |A| = n, then **|P(A)| = 2ⁿ**. ⭐
   - E.g., |{1, 2, 3}| = 3 → |P({1, 2, 3})| = 2³ = 8.

#### d) Convex Set
A subset S of a space (typically 2-dimensional real space) is **convex** iff for any two points p, q ∈ S, the entire line segment from p to q lies in S.

**Algebraic form**: if x₁, x₂ ∈ S, then every point on the line segment x₁x₂ — represented as **λx₁ + (1 − λ)x₂** for any λ with **0 ≤ λ ≤ 1** — also belongs to S. ⭐

| | Convex | Non-Convex |
|---|---|---|
| Visual | P———Q (segment fully inside) | P—·—Q (segment escapes) |
| Test | All λx₁ + (1−λ)x₂ inside | Some λ produces a point outside |

### Definitions ⭐
- **Universal set U**: largest set under consideration in a given problem context. ⭐
- **Empty/Null set ∅**: set with no elements. ⭐
- **Power set P(A)**: set of all subsets of A. ⭐
- **Convex set**: a set such that the line segment joining any two of its points lies entirely within it. ⭐

### Examples
**Example: Convex set test in R**
- [4, 5) = {x : 4 ≤ x < 5} — convex (any segment between two points stays inside).
- [1, 4] ∪ [7, 11) = {x : 1 ≤ x ≤ 4} ∪ {x : 7 ≤ x < 11} — **not convex** (a point like 5.5 lies on the segment from 3 to 9 but is not in the union).

### ⚠️ Common Mistakes
- ❌ Treating ∅ as having one element (the empty thing). → ✅ ∅ has **zero** elements; |∅| = 0.
- ❌ Counting ∅ or A itself among the proper subsets of A. → ✅ Both are subsets but not proper.
- ❌ Forgetting both endpoints of the convexity inequality: 0 ≤ λ ≤ 1. → ✅ λ ranges over the closed unit interval.

> **Quick Recall:**
> - **|P(A)| = 2ⁿ** if |A| = n.
> - **∅ ⊆ X** for every X.
> - **X ⊆ U** for every X under consideration.
> - **Convex**: λx₁ + (1−λ)x₂ ∈ S for all 0 ≤ λ ≤ 1.

### Connections
- Universal set → Complement of a set (defined as U − X) — see Chunk 004.
- Convex sets → essential in optimisation (Block 5): convex feasible regions, convex objective functions guarantee unique global optima.
- Power set → cardinality of P(A) = 2ⁿ is used in combinatorics.

### Open Questions
- Is the union of two convex sets ever convex? (Yes, only when one is a subset of the other or when they overlap in a special way.)
- What does "convex" mean in higher-dimensional spaces (Rⁿ)? Same definition — segment connecting any two points stays in the set.

---

## Section: Check Your Progress 3 🔴

### Examples / Exercises ⭐

**Q1.** Which of the following is a convex set in R?
- (i) [4, 5) = {x : 4 ≤ x < 5}, (ii) [1, 4] ∪ [7, 11) = {x : 1 ≤ x ≤ 4} ∪ {x : 7 ≤ x < 11}.

**Q2.** What is the cardinality of the power set of {0, 1, 2}?

**Q3.** Let U = {u, v, w, x, y, z}.
- (i) Find the number of subsets of U.
- (ii) Find the number of proper non-empty subsets of U.

**Q4.** List the 8 subsets of {a, b, c, d} containing {d}.

> **Hints:** Q1 → (i) is convex, (ii) is not. Q2 → 2³ = 8. Q3 → (i) 2⁶ = 64; (ii) 64 − 2 = 62 (excluding ∅ and U itself). Q4 → take all 2³ = 8 subsets of {a, b, c} and add d to each.

---

## Section: Quantifiers and Logical Operators 🔴

### Core Idea
**Quantifiers** are symbols expressing "for all" (∀) and "there exists" (∃); **logical operators** include implication (→) and biconditional (↔). They allow precise mathematical statements about elements of sets.

> **In Simple Terms:** ∀ = "for every"; ∃ = "for some"; → = "if … then …"; ↔ = "if and only if". They turn long English sentences into compact mathematical formulas.

### Key Concepts

#### a) Quantifiers

| Symbol | Reads as | Meaning |
|---|---|---|
| (∀x) x ∈ X | "for all x in X" | Statement holds for every element. |
| (∃x) x ∈ X | "for some x in X" / "there exists x in X" | Statement holds for at least one element. |
| (∄ x ∈ X) | "there does not exist x in X" / "there is no x in X (satisfying …)" | No element satisfies the statement. |

If the set X is implicit, just **(∀x)** is used; otherwise **(∀x ∈ X)** or **(∀x) x ∈ X** is written explicitly.

**Example: universal quantifier**
For Sq_int = {0, 1, 4, 9, …}, every member is a square of some integer:
**(∀x ∈ Sq_int) (x = y²), for some y ∈ Z**, where Z = set of integers.

Refined further:
**(∀x ∈ Sq_int) (∃y ∈ Z) (x = y²)**.

**Example: existential quantifier**
Some element of Sq_int is greater than 100 (e.g., 144):
**(∃x ∈ Sq_int) (x > 100)**.

**Example: non-existence**
No member of Sq_int is less than 0:
**(∄x ∈ Sq_int) (x < 0)**.

#### b) Logical Operators

| Symbol | Reads as | Meaning |
|---|---|---|
| **P → Q** | "if P then Q" | Implication. |
| **P ↔ Q** | "P if and only if Q" / "P iff Q" | Biconditional / equivalence. |

**P ↔ Q** is equivalent to **(P → Q) AND (Q → P)** taken together.

**Examples:**
- "If x is an integer then x² is a non-negative integer": **(∀x ∈ Z) (x² ≥ 0)**.
- "x² = 100 if and only if x = 10 or x = −10": **(x² = 100) ↔ (x = 10 ∨ x = −10)**.

### ⚠️ Common Mistakes
- ❌ Reading **x = 10 → x² = 100** as bidirectional. → ✅ This is one-way only. The reverse (x² = 100 → x = 10) is **false** because x could be −10.
- ❌ Confusing **∃** ("at least one") with **∃!** ("exactly one").
- ❌ Negating ∀ incorrectly. → ✅ ¬(∀x P(x)) ⇔ (∃x ¬P(x)).

> **Quick Recall:**
> - **∀** = for all; **∃** = there exists; **∄** = does not exist.
> - **→** one-way; **↔** two-way.
> - "If x = 10 then x² = 100" — true. "If x² = 100 then x = 10" — **false** (x could be −10).

### Connections
- Used in proofs throughout Block 4 (Real Analysis).

---

## Section: Relation vs Operation 🟡

### Core Idea
A **relation** returns TRUE or FALSE — it states a fact (e.g., 8 < 15). An **operation** produces a new value — it generates something (e.g., 8 + 15 = 23). Both take inputs from a set; the difference is in their output type.

> **In Simple Terms:** Relations answer yes/no questions ("is 3 less than 5?"); operations build new things ("what is 3 + 5?").

### Key Concepts

#### Relations on Numbers (Examples)
- 8 < 15 → relation "less-than" returns **TRUE**.
- 8 ≠ 15 → relation "not equal to" returns **TRUE**.
- 3 + 5 = 8 → relation "is equal to" returns **TRUE**.
- 7 < 5 → relation returns **FALSE**.

#### Operations on Numbers (Examples)
- 8 + 15 → produces new number **23**.
- 8 − 15 → produces new number **−7**.
- 16 ÷ 4 → produces new number **4**.

#### Arity
- **Binary operation**: needs two inputs (e.g., +, −, ×, ÷).
- **Unary operation**: needs one input (e.g., square root √, absolute value |·|).

#### Cross Product (Cartesian Product) of Sets
For non-empty sets A₁ and A₂, their **cross-product** A₁ × A₂ is the set of all **ordered pairs** (a₁, a₂) with a₁ ∈ A₁ and a₂ ∈ A₂.

Generalised to n sets: A₁ × A₂ × … × Aₙ is the set of all n-tuples (a₁, a₂, …, aₙ) with aᵢ ∈ Aᵢ for i = 1, …, n.

#### Relation on a Set (Formal)
A **relation** on set X (of arity n) is a subset of the n-fold cross-product X × X × … × X.
- It returns exactly one of "true" or "false".
- **Example**: "is-male" — arity 1; "is-mother-of" — arity 2.
- If Sheela is not the mother of Mohan, the relation **is-mother-of(Sheela, Mohan)** returns **false**.

#### Operation on a Set (Formal)
An **operation** of arity n on X maps X × X × … × X (n times) to **X itself** — i.e., it returns an element of X.
- **Example**: "square" on N has arity 1; "sum" on N has arity 2.
- In both cases the value returned is a member of N.

#### Connection between Relation and Operation
An (n+1)-ary relation on a set can be converted to an n-ary operation. **Example**:
- "is-mother-of" is a binary relation on the set of all humans.
- It can be converted to the unary operation "name-mother-of(x)", returning the name of the mother of x.
- E.g., is-mother-of(Mohan, Sita) = true ⇔ name-mother-of(Mohan) = Sita.

### Definitions ⭐
- **Cross-product (Cartesian product)** A × B: set of all ordered pairs (a, b) with a ∈ A, b ∈ B. ⭐
- **Relation on X (arity n)**: a subset of Xⁿ; returns true/false. ⭐
- **Operation on X (arity n)**: a function Xⁿ → X; returns an element of X. ⭐
- **Binary**: arity 2 (two inputs).
- **Unary**: arity 1 (one input).

### ⚠️ Common Mistakes
- ❌ Treating "=" as an operation. → ✅ "=" is a relation (returns true/false), whereas "+" is an operation (returns a number).
- ❌ Thinking ordered pairs are unordered. → ✅ (a, b) ≠ (b, a) in general (whereas the **set** {a, b} = {b, a}).

> **Quick Recall:**
> - **Relation**: outputs TRUE/FALSE. Examples: <, =, ≠, ⊆.
> - **Operation**: outputs a new element. Examples: +, −, ×, ÷, √, |·|, ∪, ∩.
> - **Arity**: number of inputs (unary = 1, binary = 2).

---

## Section: Operations on Sets — Union, Intersection, Difference (start) 🔴
<!-- Continues into: complement and worked examples — Chunk 004 -->

### Core Idea
Given two sets X and Y, three **binary** set operations (union, intersection, difference) and one **unary** operation (complement) generate new sets from given ones.

### Definitions ⭐

#### a) Union — X ∪ Y
**X ∪ Y = {x : x ∈ X or x ∈ Y}** (inclusive "or" — x may be in both). ⭐
- **Example**: X = {1, 2, 3, 4}, Y = {2, 3, 5, 8, 9} → **X ∪ Y = {1, 2, 3, 4, 5, 8, 9}**.
- Elements common to both (2, 3) appear only once.

#### b) Intersection — X ∩ Y
**X ∩ Y = {x : x ∈ X and x ∈ Y}**. ⭐
- **Example**: X = {1, 2, 3, 4}, Y = {2, 5, 8, 3, 9} → **X ∩ Y = {2, 3}**.

#### c) Difference — X − Y
**X − Y = {x : x ∈ X and x ∉ Y}**. ⭐
- (Continued in Chunk 004 with examples and complement.)

### Connections
- Continues into: complement, worked examples, and Check Your Progress 4 (Chunk 004).
- Foundation for: probability theory (Block 8) where events are sets and probability axioms involve ∪, ∩, complement.
