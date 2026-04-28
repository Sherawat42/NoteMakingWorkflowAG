# Chunk 001 — Probability Theory: Foundations & Definitions
<!-- Pages: 1-10 -->
<!-- Source: chunk_001.txt -->

> Block 8 covers **Probability and Probability Distributions** across three units:
> Unit 25 (Probability Theory), Unit 26 (Probability Distributions-I), Unit 27 (Probability Distributions-II).
> This chunk introduces the foundational language of probability — what experiments are random, what an event is, and the four ways probability has historically been defined.

## Section: Deterministic vs Non-Deterministic Experiments 🟢

### Core Idea
Scientific theories rest on the principle that experiments yield the same result when repeated under identical conditions — these are **deterministic**. Probability theory exists for the other class — **non-deterministic** (random) experiments — whose outcomes cannot be predicted before they happen even when conditions are held constant. The whole apparatus of probability is built to reason about this second class.

> **In Simple Terms:** If you drop a stone, it falls — that's deterministic. If you toss a coin, it might land heads or tails — that's random. Probability is the language for talking about the coin, not the stone.

### Key Concepts

#### Deterministic experiment
Repeating the experiment under identical conditions gives the same outcome (e.g., a stone tossed up returns to earth).

#### Non-deterministic / Random experiment
An act that *can* be repeated under given conditions but whose outcome is *not* predictable beforehand. Examples include tossing a coin, rolling dice, drawing a card, the age at which two people in identical conditions die.

| Aspect | Deterministic | Non-Deterministic |
|--------|---------------|-------------------|
| Repeatability with same outcome | Yes | No |
| Predictability | Outcome fully fixed by conditions | Outcome cannot be foretold |
| Tool for analysis | Classical mechanics, calculus | Probability, statistics |
| Examples | Falling stone, chemical reaction | Coin toss, dice, card draw |

### Definitions
- **Random experiment**: An act that can be repeated under given conditions whose outcome is not predictable beforehand. ⭐ (exam-important)
- **Event**: Any phenomenon that occurs as a result of a random experiment.
- **Elementary event**: An event that cannot be decomposed into simpler events.
- **Composite event**: An event that is an aggregate of several elementary events.

### Examples
Five canonical random experiments listed in the source:
1. Tossing a coin (or several coins)
2. Throwing a die (or several dice)
3. Drawing cards from a pack
4. Studying the distribution of boys and girls in two-child families in India
5. Drawing balls from urns containing different-coloured balls

> **Quick Recall:**
> - Deterministic = same result every time; Non-deterministic = unpredictable result
> - Probability theory deals only with **random** experiments

---

## Section: Sample Space and Important Terminology 🔴

### Core Idea
Before defining probability, we need vocabulary for outcomes and groupings of outcomes. The **sample space** is the set of every possible outcome; **events** are subsets of the sample space; and several relations between events (mutually exclusive, exhaustive, equally likely, independent, conditional) determine which definition of probability and which theorem applies.

> **In Simple Terms:** Think of sample space as the full menu of things that could happen, an event as one item or a group of items on that menu, and the relationships between events as rules about whether two items can be ordered together, must be ordered, or are equally tasty.

### Key Concepts

#### Sample space (S)
The collection of **all** possible outcomes of a non-deterministic experiment, denoted S. For one coin toss S = {H, T}; for two coins S = {HH, HT, TH, TT}; for two dice S = {(x,y): x, y ∈ 1..6} which has N(S) = 6 × 6 = 36 elements.

#### Sub-sample space
Any subset of S that contains the outcomes favourable to a particular event. Example: in two-coin toss, S₁ = {HH, HT, TH} is the sub-sample space favourable to "at least one head."

#### Event types
Multiple terms describe how events sit relative to each other. Each enables (or rules out) a particular probability theorem.

| Term | Meaning | Quick test |
|------|---------|-----------|
| Mutually exclusive | Two/more events cannot occur at the same time | A ∩ B = ∅ |
| Mutually exhaustive | At least one of the events must occur | A ∪ B ∪ … = S |
| Equally likely | No outcome is preferred over another | All P equal |
| Exhaustive set | Complete group of all elementary events of an experiment | Covers S |
| Independent | Occurrence of one event does not affect another | P(B\|A) = P(B) |
| Conditional | One event depends on another (rain depends on clouds) | P(B\|A) ≠ P(B) |

### Definitions
- **Sample space**: The collection of all possible outcomes of an experiment, denoted S. ⭐ (exam-important)
- **Event**: A subset of the sample space whose outcomes satisfy a particular criterion. ⭐ (exam-important)
- **Mutually exclusive events**: Events that cannot occur simultaneously. ⭐ (exam-important)
- **Mutually exhaustive events**: At least one of them necessarily occurs.
- **Equally likely events**: Outcomes such that none is expected in preference to another (e.g., head/tail of an unbiased coin).
- **Exhaustive set of events**: Set in which at least one event must occur — the complete group of elementary events of a random experiment.
- **Independent events**: Occurrence of one is not affected by occurrence of others.
- **Conditional events**: Events that are neither independent nor mutually exclusive — one is dependent on the other.
- **Venn diagram**: A rectangle (S) with circles (events). Disjoint circles = mutually exclusive; full coverage = exhaustive.

### Examples
**Example: Three unbiased coins tossed.**
S = {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT} (8 elements).
- E₁ = {HHH} = "all heads"
- E₂ = {HHH, HHT, HTH, THH} = "at least 2 heads"
- E₃ = {HHT, HTH, THH} = "exactly 2 heads"

**Example: Sum-of-7 with two dice.**
A = {(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)} → 6 favourable outcomes out of 36.

> **Quick Recall:**
> - S = sample space (everything possible)
> - Mutually exclusive ↔ disjoint sets ↔ cannot co-occur
> - Exhaustive ↔ at least one must occur ↔ union covers S
> - Equally likely ↔ symmetry assumption needed for the classical definition

---

## Section: Four Definitions of Probability 🔴

### Core Idea
Probability has **four formal definitions**, each suitable for a different situation. The classical definition uses counting under symmetry, the axiomatic definition starts from three abstract rules, the empirical (frequentist) definition uses long-run relative frequency, and the subjective definition uses degree-of-belief. Knowing which to invoke is itself an exam skill.

> **In Simple Terms:** "Probability of heads = 1/2" can mean four different things: (1) by symmetry of the coin (classical), (2) by definition that satisfies three rules (axiomatic), (3) by tossing it 10,000 times and observing the ratio (empirical), or (4) by your personal confidence (subjective).

### Key Concepts

#### Classical Definition
If an experiment has N outcomes that are mutually exclusive, exhaustive and equally likely, and N_A of them are favourable to event A, then **P(A) = N_A / N**.

- **P(A) = 0** ⇔ event is impossible (no favourable outcome).
- **P(A) = 1** ⇔ event is sure (every outcome favourable).

⚠️ Limitations: Requires equally likely outcomes (which is itself a probability statement → circular), fails when outcomes are infinite.

#### Axiomatic Definition (Kolmogorov-style)
Start with sample space S, treat its subsets as events, and assign each event A a number P(A) satisfying three axioms:
1. **P(A) ≥ 0** (non-negative).
2. **P(S) = 1** (the sure event has probability 1).
3. If A and B are mutually exclusive: **P(A ∪ B) = P(A) + P(B)**.

This frees probability from the "equally likely" assumption and is the foundation of modern probability theory.

#### Empirical Definition (Von Mises)
In N trials, if event A occurs m times, the relative frequency is m/N. The probability is the limit:

P(A) = lim_(N→∞) (m/N)

The "limit" must be interpreted as an assumption (it cannot be observed in finitely many trials), so this definition has not been widely adopted as a basis of deductive theory.

#### Subjective Definition
P(A) measures one's state of belief in the truth of statement A. Used in everyday speech: "I'm 100% sure I'll pass" (P = 1), "50% chance India wins" (P = 1/2). Not derivable from data — purely personal.

| Definition | Uses | Strength | Weakness |
|------------|------|----------|----------|
| Classical | Coins, dice, cards | Simple, intuitive | Needs symmetry; fails for infinite outcomes |
| Axiomatic | Modern theory | General, rigorous | Abstract |
| Empirical | Long-run data | Data-driven | Limit cannot be observed |
| Subjective | Belief/judgement | Captures uncertainty in unique events | Not data-based |

### Definitions
- **Classical probability**: P(A) = (favourable outcomes) / (total outcomes), assuming outcomes are mutually exclusive, exhaustive, and equally likely. ⭐ (exam-important)
- **Axiomatic probability**: Probability assignment satisfying P(A) ≥ 0, P(S) = 1, and P(A ∪ B) = P(A) + P(B) for disjoint A, B. ⭐ (exam-important)
- **Empirical probability**: P(A) = lim(m/N) as N → ∞.
- **Subjective probability**: P(A) is a measure of belief about A.

### Mechanisms / Processes
Applying classical probability to "two dice product = 18":
1. Total outcomes N = 36 (mutually exclusive, exhaustive, equally likely under unbiased assumption).
2. Favourable outcomes for product = 18: only (3, 6) and (6, 3) → N_A = 2.
3. P(A) = N_A / N = 2/36 = 1/18.

### Techniques of Counting (used with classical definition)

| # | Technique | Formula |
|---|-----------|---------|
| 1 | Fundamental Principle of Counting | If processes done in p × q × r × … ways |
| 2 | Permutation (n distinct, take r) | ⁿP_r = n(n−1)(n−2)…(n−r+1) |
| 3a | Arrangement in a line | n! = 1·2·3·…·n |
| 3b | Arrangement in a circle | (n−1)! |
| 4 | Permutation with repetition (p alike, q alike, …) | n! / (p! q! r! …) |
| 5 | Combination | ⁿC_r = n! / [r!(n−r)!] |
| 6 | Choosing balls (a white from A, b black from B) | ᴬC_a · ᴮC_b |
| 7 | Ordered partition (distinct objects into r compartments with n₁, n₂, …, n_r in each) | n! / (n₁! n₂! … n_r!); total ways = rⁿ |
| 8 | Ordered partition (n identical objects into r compartments) | ⁽ⁿ⁺ʳ⁻¹⁾C_(r−1); none-empty: ⁽ⁿ⁻¹⁾C_(r−1) |

### Examples
**Example: Probability all three children have different birthdays.**
First child: any of 365 days; second: any of remaining 364; third: any of remaining 363.
P = (365 · 364 · 363) / 365³.

**Example: Five persons a, b, c, d, e seated in a row — probability a and b sit together.**
Total arrangements = 5! = 120. Treat (a,b) as a block; arrangements = 4! · 2! = 48.
P = 48/120 = 0.4.

**Example: Two cards from a pack, both red.**
Total = ⁵²C₂ = 1326. Favourable = ²⁶C₂ = 325. P = 325/1326.

**Example: Bag of 6 white + 4 red balls, one drawn.**
P(white) = 6/10 = 0.6.

### ⚠️ Common Mistakes
- ❌ Mistake: Applying classical definition when outcomes are not equally likely (e.g., loaded die) → ✅ Correct: Use empirical or subjective definition.
- ❌ Mistake: Confusing the **axiomatic** P(S) = 1 with the **classical** "every outcome is favourable" → ✅ Correct: Axiomatic axiom is a definitional rule for the entire space; classical is a counting result for a specific event A = S.
- ❌ Mistake: Reading "equally likely" as a derived fact → ✅ Correct: It is an *assumption* one must justify (typically by symmetry of the physical setup).

### Edge Cases & Caveats
- Classical definition fails for infinite sample spaces (e.g., picking a real number in [0,1]).
- The phrase "equally likely" inside the classical definition is itself a probability statement → the definition is **circular**.
- Empirical definition's limit cannot be empirically verified — it's an assumption.

> **Quick Recall:**
> - Four definitions: **Classical, Axiomatic, Empirical, Subjective**
> - Classical formula: P(A) = N_A / N (under symmetry)
> - Axioms: P(A) ≥ 0, P(S) = 1, additivity for disjoint events
> - Counting techniques: factorials, ⁿP_r, ⁿC_r, ordered partitions

### Connections
- Sets the stage for: [Theorems of Probability] (Chunk 002) — total and compound probability are derived from the classical/axiomatic definitions.
- Connects forward to: [Mathematical Expectation] (Chunks 002–003) — uses the probability-weighted sum that depends on these definitions.

### Open Questions
1. How does the axiomatic definition handle continuous sample spaces (e.g., choosing a point uniformly on [0, 1])?
2. When two definitions give different numerical answers for the same problem, which should we prefer?
