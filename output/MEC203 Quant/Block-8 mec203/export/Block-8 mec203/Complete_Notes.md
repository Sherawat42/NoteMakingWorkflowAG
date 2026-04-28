# Complete Notes


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
- Sets the stage for: [Theorems of Probability] (Chunk 002: Theorem of Total Probability (Addition Theorem)) — total and compound probability are derived from the classical/axiomatic definitions.
- Connects forward to: [Mathematical Expectation] (Chunks 002–003) — uses the probability-weighted sum that depends on these definitions.

### Open Questions
1. How does the axiomatic definition handle continuous sample spaces (e.g., choosing a point uniformly on [0, 1])?
2. When two definitions give different numerical answers for the same problem, which should we prefer?


---


## Section: Theorem of Total Probability (Addition Theorem) 🔴

### Core Idea
The **Theorem of Total Probability** gives the probability of "either A or B" — i.e., P(A ∪ B). For mutually exclusive events it's a simple sum; for non-exclusive events you must subtract the overlap to avoid double-counting. It is the formal statement of "OR" in probability and is also called the **Addition Theorem**.

> **In Simple Terms:** If you want the chance of "rain or wind today," and they cannot happen simultaneously, just add the two probabilities. If they can happen together, add them and subtract the chance of "rain *and* wind" — otherwise you've counted that overlap twice.

### Key Concepts

#### Mutually exclusive case
For disjoint A and B: **P(A ∪ B) = P(A) + P(B)**.
**Proof sketch**: If n total outcomes are mutually exclusive, exhaustive, and equally likely, with m₁ favourable to A and m₂ favourable to B (and A ∩ B = ∅), then favourable to A ∪ B is m₁ + m₂, so P(A ∪ B) = (m₁ + m₂)/n = P(A) + P(B).

#### Extension to k mutually exclusive events
**P(A₁ ∪ A₂ ∪ … ∪ A_k) = P(A₁) + P(A₂) + … + P(A_k)**.

#### Non-exclusive case
**P(A ∪ B) = P(A) + P(B) − P(A ∩ B)**.
For three non-exclusive events:
**P(A ∪ B ∪ C) = P(A) + P(B) + P(C) − P(A ∩ B) − P(A ∩ C) − P(B ∩ C) + P(A ∩ B ∩ C)** (inclusion–exclusion principle).

#### Theorem of Complementary Event
A and Aᶜ are mutually exclusive and exhaustive (S = A ∪ Aᶜ), so **P(Aᶜ) = 1 − P(A)**. Intuitive: P(tail) = 1 − P(head) = 0.5 for an unbiased coin.

### Definitions
- **Theorem of Total Probability (Addition Theorem)**: P(A ∪ B) = P(A) + P(B) for mutually exclusive A, B; otherwise P(A ∪ B) = P(A) + P(B) − P(A ∩ B). ⭐ (exam-important)
- **Complement Aᶜ (or Aʹ)**: The non-occurrence of A. P(Aᶜ) = 1 − P(A). ⭐ (exam-important)
- **Boole's inequality**: P(A ∪ B) ≤ P(A) + P(B).
- **Bonferroni's inequality**: P(A ∩ B) ≥ P(A) + P(B) − 1.

### Mechanisms / Processes
Proof of P(A ∪ B) = P(A) + P(B) − P(A ∩ B):
1. Decompose A ∪ B into three disjoint pieces: A ∩ Bᶜ, Aᶜ ∩ B, A ∩ B.
2. P(A ∪ B) = P(AB̄) + P(ĀB) + P(AB).
3. Note A = (A ∩ B) ∪ (A ∩ Bᶜ) → P(A) = P(AB) + P(AB̄), so P(AB̄) = P(A) − P(AB).
4. Similarly P(ĀB) = P(B) − P(AB).
5. Substitute: P(A ∪ B) = [P(A) − P(AB)] + [P(B) − P(AB)] + P(AB) = P(A) + P(B) − P(A ∩ B).

### Examples
**Example: 3 courses A, B, C — pass percentages.**
P(A) = 0.25, P(B) = 0.20, P(C) = 0.35, P(A ∩ B) = 0.07, P(A ∩ C) = 0.05, P(B ∩ C) = 0.02, P(A ∩ B ∩ C) = 0.01.
P(at least one course) = P(A ∪ B ∪ C) = 0.25 + 0.20 + 0.35 − 0.07 − 0.05 − 0.02 + 0.01 = **0.67**.

> **Quick Recall:**
> - P(A ∪ B) = P(A) + P(B) − P(A ∩ B) (general)
> - = P(A) + P(B) (if disjoint)
> - P(Aᶜ) = 1 − P(A)
> - Three-event inclusion–exclusion: + singles − doubles + triple

---

## Section: Theorem of Compound Probability (Multiplication Theorem) 🔴

### Core Idea
Where the addition theorem handles "OR," the **Theorem of Compound Probability** handles "AND": P(A ∩ B) = P(A) · P(B|A). The conditional probability P(B|A) measures B's chance once A is known to have happened. It generalises naturally to three or more events as a chain.

> **In Simple Terms:** "What's the chance of A AND B?" = "Chance of A" × "Chance of B given that A already happened."

### Key Concepts

#### Compound probability formula
**P(A ∩ B) = P(A) × P(B|A)**.
Equivalently P(A ∩ B) = P(B) × P(A|B), so P(B|A) = P(A ∩ B)/P(A) when P(A) ≠ 0.

#### Extension to three events
**P(A ∩ B ∩ C) = P(A) × P(B|A) × P(C|A ∩ B)**, and so on for more events (chain rule of probability).

#### Decomposition of P(B) using complementary partition
For any event A:
**P(B) = P(A ∩ B) + P(Aᶜ ∩ B) = P(A) · P(B|A) + P(Aᶜ) · P(B|Aᶜ)**.
(This is the precursor to Bayes' Theorem.)

### Definitions
- **Theorem of Compound Probability (Multiplication Theorem)**: P(A ∩ B) = P(A) × P(B|A). ⭐ (exam-important)
- **Conditional probability P(B|A)**: Probability of B given A has occurred = P(A ∩ B)/P(A), provided P(A) > 0. ⭐ (exam-important)

### Examples
**Example: Given P(A) = 1/4, P(B) = 2/5, P(A ∪ B) = 1/2 — find P(A|B), P(B|A).**
P(A ∩ B) = P(A) + P(B) − P(A ∪ B) = 1/4 + 2/5 − 1/2 = 3/20.
P(A|B) = (3/20) / (2/5) = 3/8. P(B|A) = (3/20) / (1/4) = 3/5.

**Example: Ace of hearts | the card is red.**
A = card is red (P = 26/52). B = card is Ace of hearts (P = 1/52). A ∩ B = Ace of hearts (which is red), P = 1/52.
P(B|A) = (1/52) / (26/52) = **1/26**.

> **Quick Recall:**
> - P(A ∩ B) = P(A) · P(B|A) — the multiplication theorem
> - P(B|A) = P(A ∩ B) / P(A)
> - Total probability via partition: P(B) = P(A)·P(B|A) + P(Aᶜ)·P(B|Aᶜ)

### Connections
- Builds on: [Sample Space and Important Terminology] (Chunk 001: Deterministic vs Non-Deterministic Experiments) — uses the conditional events idea.
- Pre-requisite for: [Bayes' Theorem] (this chunk) — Bayes' is total + compound combined.

---

## Section: Independent Events 🔴

### Core Idea
Two events are **independent** when knowing one tells you nothing new about the other — formally P(B|A) = P(B). For independent events the compound probability collapses to a simple product P(A ∩ B) = P(A) · P(B). Independence is *the* assumption that lets us multiply probabilities freely, and it's the workhorse behind binomial/Poisson distributions later in the block.

> **In Simple Terms:** Tossing a coin twice — the second toss "doesn't know" what the first did. So the chance of two heads is just (1/2) × (1/2) = 1/4, not something more complex.

### Key Concepts

#### Definition via conditional probability
A and B are independent ⇔ P(B|A) = P(B|Aᶜ) = P(B).

#### Definition via product rule
A and B are independent ⇔ **P(A ∩ B) = P(A) · P(B)**.

#### Three-event mutual independence
P(A ∩ B ∩ C) = P(A) P(B) P(C) **AND** all pairwise products hold:
P(A ∩ B) = P(A) P(B), P(B ∩ C) = P(B) P(C), P(A ∩ C) = P(A) P(C).

#### Four+ events
All triplet, pair, and full-product factorisations must hold simultaneously.

#### Pairwise vs mutual independence
- **Pairwise independence**: each *pair* satisfies the product rule.
- **Mutual independence**: every subset's joint probability equals the product. Stronger than pairwise.

#### Deduction: complements of independent events
If A, B are independent, then **Aᶜ and Bᶜ are also independent**. Proof uses De Morgan's: P(Aᶜ ∩ Bᶜ) = P((A ∪ B)ᶜ) = 1 − P(A) − P(B) + P(A) P(B) = (1 − P(A))(1 − P(B)) = P(Aᶜ) P(Bᶜ).

### Definitions
- **Independent events**: P(A ∩ B) = P(A) · P(B), equivalently P(B|A) = P(B). ⭐ (exam-important)
- **Pairwise independence**: Every pair of events is independent.
- **Mutual independence**: Every subset of events factorises into the product of marginals.

### Examples
**Example: Are A, B independent given P(A) = 3/8, P(B) = 5/8, P(A ∪ B) = 3/4?**
P(A ∩ B) = P(A) + P(B) − P(A ∪ B) = 3/8 + 5/8 − 3/4 = 1/4.
Check: P(A) · P(B) = (3/8)(5/8) = 15/64 ≠ 1/4 = 16/64. So **A and B are not independent**.

**Example: Two urns — same-colour ball and white-ball probabilities.**
Urn 1: 2W, 2R. Urn 2: 2W, 4R.
(a) Probability both balls drawn (one from each urn) are same colour:
- A₁ = both white = (2/4) × (2/6) = 4/24 = 1/6.
- A₂ = both red = (2/4) × (4/6) = 8/24 = 1/3.
- P(same colour) = 1/6 + 1/3 = **1/2**.

(b) Random urn, then random ball — P(white)?
- P(urn 1) × P(white | urn 1) = (1/2)(2/4) = 1/4.
- P(urn 2) × P(white | urn 2) = (1/2)(2/6) = 1/6.
- P(white) = 1/4 + 1/6 = **5/12**.

### ⚠️ Common Mistakes
- ❌ Mistake: Treating mutually exclusive events as independent → ✅ Correct: Mutually exclusive events are *strongly dependent* — knowing A occurred forces P(B|A) = 0.
- ❌ Mistake: Pairwise independence ⇒ mutual independence → ✅ Correct: Pairwise can hold while joint factorisation fails (classic counter-examples in 3+ events).

> **Quick Recall:**
> - Independence ⇔ P(A ∩ B) = P(A) · P(B)
> - For independent A, B: Aᶜ, Bᶜ are also independent
> - Mutually exclusive ≠ independent (in fact opposite for events with positive probability)

---

## Section: Bayes' Theorem 🔴

### Core Idea
**Bayes' Theorem** lets us reverse a conditional: given that A actually happened, which prior cause B_i is most likely to have produced it? It combines the law of total probability (for the denominator) with the multiplication rule (for the numerator). Bayes is "the" tool for diagnostic / inverse-probability problems and underpins much of modern statistics and machine learning.

> **In Simple Terms:** You hear a fire alarm. There are several possible causes (real fire, burnt toast, faulty wiring). Bayes' Theorem updates your belief about *which* cause is most likely now that you've heard the alarm, by combining the prior chance of each cause with how often each cause triggers the alarm.

### Key Concepts

#### Setup
Suppose event A can occur if and only if **one of the mutually exclusive events B₁, B₂, …, B_n** occurs (so {B_i} is a partition).
Known: P(B_i) for all i (priors), and P(A|B_i) for all i (likelihoods).
Unknown: P(B_i|A) for any i (posterior).

#### Statement
**P(B_i | A) = [ P(B_i) · P(A|B_i) ] / Σ_j [ P(B_j) · P(A|B_j) ]**.

Numerator = P(B_i ∩ A); Denominator = total probability P(A) = Σ_j P(B_j) · P(A|B_j).

#### Vocabulary
- **Prior** P(B_i): belief in cause B_i before observing A.
- **Likelihood** P(A|B_i): probability of A under cause B_i.
- **Posterior** P(B_i|A): updated belief in B_i after observing A.

### Definitions
- **Bayes' Theorem**: P(B_i | A) = P(B_i) P(A|B_i) / Σ_j P(B_j) P(A|B_j) where {B_j} partitions the sample space. ⭐ (exam-important)

### Mechanisms / Processes
Standard Bayes calculation in 4 steps:
1. Identify the partition {B_i} (mutually exclusive, exhaustive causes).
2. Write down all priors P(B_i) and likelihoods P(A|B_i).
3. Compute total probability: P(A) = Σ_j P(B_j) P(A|B_j).
4. Posterior: P(B_i|A) = P(B_i) P(A|B_i) / P(A).

### Examples
**Example: Box transfer problem.**
Box 1: 2R, 2B. Box 2: 2R, 4B. Transfer one ball from Box 1 → Box 2, then draw one ball from Box 2; it's black. Find P(transferred ball was red).
- B₁ = transferred ball red, B₂ = transferred ball black. P(B₁) = P(B₂) = 1/2.
- After transfer: if red transferred, Box 2 has 3R + 4B = 7 balls → P(A=black|B₁) = 4/7. *Source uses 3/7; we follow source*: **P(A|B₁) = 3/7, P(A|B₂) = 5/7.**
- P(B₁|A) = (1/2 · 3/7) / (1/2 · 3/7 + 1/2 · 5/7) = (3/7) / (8/7) = **3/8**.

**Example (Check Your Progress 4 Q1): Bulb factory with three machines.**
Machine a, b, c produce 25%, 35%, 40% of bulbs; defect rates 5%, 4%, 2% respectively.
- P(B_a) = 0.25, P(B_b) = 0.35, P(B_c) = 0.40.
- P(A|B_a) = 0.05, P(A|B_b) = 0.04, P(A|B_c) = 0.02.
- P(A) = 0.25·0.05 + 0.35·0.04 + 0.40·0.02 = 0.0125 + 0.014 + 0.008 = 0.0345.
- P(B_c|A) = 0.008 / 0.0345 = **16/69**.

**Example (Check Your Progress 4 Q2): Fair vs loaded coin.**
P(H | fair) = 1/2, P(H | loaded) = 2/3. Pick a coin at random (P = 1/2 each), toss, get heads.
- P(fair | H) = (1/2 · 1/2) / (1/2 · 1/2 + 1/2 · 2/3) = (1/4) / (7/12) = **3/7**.

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing P(A|B) with P(B|A) (the "prosecutor's fallacy") → ✅ Correct: Use Bayes' Theorem to convert one to the other; they are usually different numbers.
- ❌ Mistake: Forgetting the denominator (total probability) → ✅ Correct: P(A) = Σ P(B_j) P(A|B_j), summed over the *full* partition.

> **Quick Recall:**
> - Bayes' Theorem: posterior ∝ prior × likelihood
> - P(B_i | A) = P(B_i) P(A|B_i) / Σ P(B_j) P(A|B_j)
> - Use whenever you need to "reverse" a conditional given a partition of causes

### Connections
- Builds on: [Theorem of Compound Probability] (this chunk) and the law of total probability above.
- Connects to: Conditional reasoning in [Bayesian inference] outside the syllabus.

---

## Section: Mathematical Expectation — Introduction 🔴
<!-- Continues in chunk 003 -->

### Core Idea
**Mathematical expectation** E(x) is the probability-weighted average of the values a random variable can take — the theoretical mean. It is the single most important summary statistic of a random variable and connects probability theory to descriptive statistics (where the analogue is the weighted arithmetic mean using relative frequencies as weights).

> **In Simple Terms:** Imagine a lottery where you win different amounts with different probabilities. The expected value is what you'd win on average per ticket if you played the lottery many, many times.

### Key Concepts

#### Definition
For a discrete random variable x taking values x₁, x₂, …, x_n with probabilities p₁, p₂, …, p_n where Σ p_i = 1 and p_i ≥ 0:
**E(x) = p₁x₁ + p₂x₂ + … + p_n x_n = Σ p_i x_i**.

#### Expected value is a weighted mean
The relative frequency f_i / N (class frequency over total frequency) is itself an empirical probability p_i. So weighted arithmetic mean = Σ x_i (f_i / N) = Σ x_i p_i = E(x). The expectation is the population analogue of the sample mean.

### Definitions
- **Mathematical Expectation E(x)**: Σ p_i x_i for discrete x; the probability-weighted sum of values. ⭐ (exam-important)

### Examples
**Example: Expected number of points on an unbiased die.**
Each face 1..6 has probability 1/6.
E(x) = (1/6)(1 + 2 + 3 + 4 + 5 + 6) = 21/6 = **3.5**.

> **Quick Recall:**
> - E(x) = Σ p_i x_i (discrete)
> - Σ p_i = 1, p_i ≥ 0 always
> - It is the theoretical / population mean — the "mean of a random variable"

<!-- Continues in chunk 003 — variance, theorems on expectation, more examples -->

### Open Questions
1. How does E(x) extend to continuous random variables (with integrals)? — covered later in Unit 26.
2. When does the expected value not equal any of the actual outcomes (as in the die example: 3.5 is not on any face)?


---


## Section: Variance and Functions of a Random Variable 🔴
<!-- See chunk 002 for start of this section (Mathematical Expectation) -->

### Core Idea
Variance Var(x) = E[(x − m)²] measures how much a random variable's values spread around its mean m = E(x). It uses the *second moment about the mean*. The standard deviation σ = √Var(x). For any function g(x), the expected value generalises: E[g(x)] = Σ g(x_i) p_i.

> **In Simple Terms:** The expectation tells you the centre of the distribution; the variance tells you how spread out the distribution is around that centre. Two distributions can have the same mean but very different shapes.

### Key Concepts

#### Variance — formal definition
If E(x) = m (the mean), then Var(x) = E[(x − m)²] = Σ (x_i − m)² p_i.

#### Computational identity ⭐
**Var(x) = E(x²) − [E(x)]²**.
This identity is *the* working formula — much faster than computing each (x_i − m)².

#### Standard deviation
σ = √Var(x). Same units as the variable; variance has units squared.

#### Expectation of a function g(x)
E[g(x)] = Σ g(x_i) p_i (discrete). Lets us compute E(x²), E(e^(tx)), etc.

### Definitions
- **Variance Var(x)**: E[(x − E(x))²] = E(x²) − [E(x)]². ⭐ (exam-important)
- **Standard deviation σ**: √Var(x). ⭐ (exam-important)

### Mechanisms / Processes
Derivation of Var(x) = E(x²) − [E(x)]²:
1. Var(x) = E[(x − m)²] = Σ (x − m)² p_i.
2. Expand: Σ (x² − 2xm + m²) p_i = Σ x² p_i − 2m Σ x p_i + m² Σ p_i.
3. Identify: Σ x² p_i = E(x²); Σ x p_i = E(x) = m; Σ p_i = 1.
4. = E(x²) − 2m·m + m² = E(x²) − m² = E(x²) − [E(x)]².

> **Quick Recall:**
> - Var(x) = E(x²) − [E(x)]² ← faster computation
> - σ = √Var(x)
> - E[g(x)] = Σ g(x_i) p_i

---

## Section: Theorems on Mathematical Expectation 🔴

### Core Idea
Two key linearity-style theorems govern expectations: (1) **expectation of a sum** of random variables equals the **sum of expectations** (always, no independence required); (2) **expectation of a product** of *independent* random variables equals the **product of expectations**. The second theorem is essential for variance of sums, covariance, and the moment generating function machinery used later.

> **In Simple Terms:** If you toss two dice, the expected sum is just (expected first) + (expected second) — addition always works. But the expected *product* of two random outcomes equals the product of their averages only when the variables don't influence each other.

### Key Concepts

#### Theorem 1: Expectation of a sum
For random variables a, b, c, … (independent or not):
**E(a + b + c + …) = E(a) + E(b) + E(c) + …**

#### Theorem 2: Expectation of a product (requires independence)
If x and y are **independent**:
**E(xy) = E(x) · E(y)**.
Extends to any number of mutually independent variables.

#### Joint and marginal probabilities (bivariate)
For two discrete variables x (n values) and y (m values), p_ij = P(x = x_i AND y = y_j).
- **Marginal probability of x = x_i**: p_(i,•) = Σ_j p_ij (row sum).
- **Marginal probability of y = y_j**: p_(•,j) = Σ_i p_ij (column sum).
- **Conditional distribution of x given y = y_j**: p_(i,j) / p_(•,j) for each i.

| Concept | Formula | Use |
|---------|---------|-----|
| Joint p_ij | P(x=x_i, y=y_j) | Full bivariate |
| Marginal p_(i,•) | Σ_j p_ij | Distribution of x ignoring y |
| Conditional p_ij/p_(•,j) | P(x=x_i \| y=y_j) | Distribution of x given y |

#### Variance of a sum (Corollary)
**Var(x₁ + x₂ + … + x_n) = Σ Var(x_i) + 2 Σ_(i<j) Cov(x_i, x_j)**.
For mutually independent variables, all covariances are 0:
**Var(x₁ + … + x_n) = Σ Var(x_i)**.
- **Cov(x_i, x_j) = E[(x_i − m_i)(x_j − m_j)]**.

### Definitions
- **Marginal probability**: Probability that one variable takes a given value, summed over all values of the other(s). ⭐ (exam-important)
- **Conditional distribution**: For each value of the conditioning variable, a (re-normalised) probability distribution of the other.
- **Covariance Cov(x, y)**: E[(x − m_x)(y − m_y)] — measures co-variation; zero under independence.

### Mechanisms / Processes
Proof sketch of Theorem 1 (sum of expectations):
1. (x + y) takes value (x_i + y_j) with probability p_ij.
2. E(x + y) = ΣΣ (x_i + y_j) p_ij.
3. Split: ΣΣ x_i p_ij + ΣΣ y_j p_ij = Σ x_i (Σ_j p_ij) + Σ y_j (Σ_i p_ij) = Σ x_i p_(i,•) + Σ y_j p_(•,j) = E(x) + E(y).

Proof sketch of Theorem 2 (product, with independence):
1. P(x = x_i AND y = y_j) = p_i · q_j (independence).
2. E(xy) = ΣΣ x_i y_j (p_i · q_j) = (Σ x_i p_i)(Σ y_j q_j) = E(x) · E(y).

### Examples
**Example (Check Your Progress 5 Q1): Lottery expected winnings.**
First prize ₹10,000 with P = 0.0001; second prize ₹4,000 with P = 0.0004; otherwise 0.
| Outcome | P | x · P |
|---------|---|-------|
| 0 | 0.9995 | 0 |
| 4000 | 0.0004 | 1.6 |
| 10000 | 0.0001 | 1.0 |
| Total | 1 | **2.6** |
E(x) = ₹2.6.

**Example (Check Your Progress 5 Q2): Expected number of white balls drawn.**
Box: 4W, 6B. Draw 3 without replacement. Let x = number of white balls drawn.
- P(x = 0) = ⁴C₀ · ⁶C₃ / ¹⁰C₃ = 1/6.
- P(x = 1) = ⁴C₁ · ⁶C₂ / ¹⁰C₃ = 1/2.
- P(x = 2) = ⁴C₂ · ⁶C₁ / ¹⁰C₃ = 3/10.
- P(x = 3) = ⁴C₃ · ⁶C₀ / ¹⁰C₃ = 1/30.
Then E(x) = 0·(1/6) + 1·(1/2) + 2·(3/10) + 3·(1/30) = **6/5 = 1.2**.

### ⚠️ Common Mistakes
- ❌ Mistake: Applying E(xy) = E(x) E(y) without checking independence → ✅ Correct: Without independence, E(xy) = E(x) E(y) + Cov(x, y).
- ❌ Mistake: Assuming Var(x + y) = Var(x) + Var(y) always → ✅ Correct: True only when Cov(x, y) = 0 (e.g., under independence).

### Edge Cases & Caveats
- Theorem 1 holds even if variables are dependent — additivity of expectation does **not** require independence.
- Cov(x, x) = Var(x), explaining the "+ Var" terms in the variance-of-sum formula.

> **Quick Recall:**
> - **E(a + b) = E(a) + E(b)** always
> - **E(xy) = E(x) E(y)** only if independent
> - **Var(Σ x_i) = Σ Var(x_i) + 2 Σ Cov(x_i, x_j)**; covariances vanish under independence

### Connections
- Builds on: [Mathematical Expectation — Introduction] (Chunk 002: Theorem of Total Probability (Addition Theorem)).
- Pre-requisite for: [Moments] (Chunk 004: Random Variables — Discrete vs Continuous) — variance is the second central moment.
- Pre-requisite for: [Variance / Mean of binomial, Poisson] (Chunks 006–007).

---

## Section: Unit 25 Summary, Key Words & Exercises 🟢

### Core Idea
The unit closes by tying the four definitions, addition/multiplication theorems, conditional probability, Bayes' theorem, and mathematical expectation into a single coherent toolkit. The Key Words section gives canonical (exam-quotable) one-line definitions; the Exercises test routine application.

### Definitions (Key Words from textbook — verbatim restatements ⭐)
- **Bayes' Theorem**: P(B_i | A) = P(A|B_i) · P(B_i) / Σ P(B_j) P(A|B_j) when {B_j} is mutually exclusive and exhaustive.
- **Conditional Events**: When events are neither independent nor mutually exclusive — one's probability depends on the other.
- **Events**: When some elements of the sample space satisfy a particular criterion.
- **Independent Events**: P(A ∩ B) = P(A) × P(B).
- **Marginal Probability**: In a bivariate distribution, the probability that X takes a given value irrespective of Y (and vice versa).
- **Mathematical Expectation**: Weighted sum of values of x, weights = probabilities; E(x) = Σ x_i p_i.
- **Mutually Exclusive Events**: No two can occur simultaneously.
- **Mutually Exhaustive Events**: At least one must necessarily occur.
- **Sample Space**: Collection of all possible outcomes.

### Exercises (canonical worked examples — high-yield templates)

**Q1: Two balls drawn one by one without replacement (5 green + 7 red), first green & second red.**
P(G then R) = (5/12)(7/11) = **35/132**.

**Q2: Two cards drawn from 52 — both diamonds OR both kings.**
- Total = ⁵²C₂.
- Both diamonds = ¹³C₂ = 78. Both kings = ⁴C₂ = 6.
- P = (78 + 6)/⁵²C₂ = 84/1326 ≈ **0.063**.

**Q3: Tyre lifetime data (1000 cases).**
| Distance (km) | <4000 | 4001–9000 | 9001–14000 | >14000 |
|---------------|-------|-----------|------------|--------|
| Frequency | 20 | 210 | 325 | 445 |

(i) P(<4000) = 20/1000 = **0.02**.
(ii) P(>9000) = (325 + 445)/1000 = **0.77**.
(iii) P(4000 ≤ km ≤ 14000) = (210 + 325)/1000 = **0.535**.

**Q4: Coin tossed 3 times — P, Q, R mutually exclusive & exhaustive?**
- S = {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}.
- P = {TTT}, Q = {HTT, THT, TTH}, R = {HHH, HHT, HTH, THH}.
- P ∪ Q ∪ R = S → exhaustive. Pairwise intersections all empty → mutually exclusive. **Yes** they form a mutually exclusive and exhaustive set.

**Q5: P(A|B) when P(A) = 7/13, P(B) = 9/13, P(A ∩ B) = 4/13.**
P(A|B) = (4/13)/(9/13) = **4/9**.

> **Quick Recall:**
> - All four probability definitions usable depending on situation
> - Theorems: Total (addition, with/without overlap), Compound (multiplication, with conditional)
> - Bayes' = total + compound combined for "reverse" inference
> - E(x) = Σ x_i p_i; Var(x) = E(x²) − [E(x)]²

### Connections
- Closes Unit 25; sets up [Random Variables] in Unit 26 (Chunk 004: Random Variables — Discrete vs Continuous).

### Open Questions
1. How does the addition theorem extend to countably infinite events (a key concern of measure theory)?


---


## Section: Random Variables — Discrete vs Continuous 🔴

### Core Idea
A **random variable** is a real-valued function whose value depends on the outcome of a random experiment. They split sharply into two types — **discrete** (takes only countably many distinct values, like 0, 1, 2, …) and **continuous** (takes any value in an interval, e.g. all real numbers between 0 and 1). The discrete/continuous distinction governs every subsequent technique: probability mass function vs probability density function, sum vs integral, Σ vs ∫.

> **In Simple Terms:** A random variable is a number whose value depends on chance. Discrete = countable values like the number of heads in 3 coin tosses; continuous = any value in a range like the exact weight of a person.

### Key Concepts

#### Random variable — formal
A real-valued function defined over the points of a sample space (the set of all possible outcomes of an experiment) with a probability measure attached. It "translates" outcomes into numbers.

#### Discrete random variable
Takes only distinct (countable) values — e.g., number when rolling a die ∈ {1,2,3,4,5,6}, never 4.3 or 5.5. Examples: number of heads in 3 coin tosses, number of red cards in a 10-card draw, number of accidents in a city, number of misprints per page.

#### Continuous random variable
Takes any value within a given interval (uncountably infinite). Examples: life of an electrical gadget, duration of phone calls, annual rainfall in a district.

| Aspect | Discrete | Continuous |
|--------|----------|------------|
| Values | Countable (finite or countably infinite) | Uncountable (any real in interval) |
| Probability tool | p.m.f. f(x) = P(X = x) | p.d.f. f(x), used as ∫ f(x) dx |
| Probability of single value | f(x) > 0 possible | Always 0 |
| Aggregation | Σ | ∫ |

### Definitions
- **Random variable**: A real-valued function on the sample space (with a probability measure). ⭐ (exam-important)
- **Discrete random variable**: Takes countable values with no possible value strictly between two adjacent ones. ⭐ (exam-important)
- **Continuous random variable**: Takes any value within an interval / range. ⭐ (exam-important)

### Examples
- Toss a coin three times — X = number of heads → X ∈ {0,1,2,3} (discrete).
- Y = the number on a rolled die → Y ∈ {1,2,3,4,5,6} (discrete).
- Z = exact rainfall in mm → Z ∈ ℝ⁺ (continuous).

> **Quick Recall:**
> - RV = function from sample space to real numbers
> - Discrete ↔ countable values, p.m.f.
> - Continuous ↔ interval values, p.d.f., P(X = a) = 0 always

---

## Section: Probability Mass Function (p.m.f.) 🔴

### Core Idea
For a **discrete** random variable X taking values x_i with probabilities p_i, the **probability mass function** f(x) = P(X = x) lists the probability of each value. A valid p.m.f. must satisfy two conditions: non-negativity and total mass equal to 1.

> **In Simple Terms:** A p.m.f. is just a table that tells you the probability of each possible value. Like a histogram where the heights add up to 100%.

### Key Concepts

#### Definition
For discrete X taking values x₁, x₂, … with probabilities p₁, p₂, …, **f(x) = P(X = x) = p_i** when x = x_i. The function f(x) must satisfy:
1. **f(x) ≥ 0** for all x (probabilities are non-negative).
2. **Σ_i f(x_i) = 1** (total probability is one).

#### Discrete probability distribution
The full specification: the set of possible values along with their probabilities. May involve countably infinite values.

### Definitions
- **Probability Mass Function (p.m.f.)**: f(x) = P(X = x) for discrete X, satisfying f(x) ≥ 0 and Σ f(x_i) = 1. ⭐ (exam-important)

### Examples
**Example: Coin tossed until first head — X = number of tails preceding head.**
Sample points: H, TH, TTH, TTTH, …
| X | 0 | 1 | 2 | 3 | … | n |
|---|---|---|---|---|---|---|
| f(X = x) | 1/2 | (1/2)² | (1/2)³ | (1/2)⁴ | … | (1/2)^(n+1) |

p.m.f.: **f(x) = (1/2)^(x+1)** for x = 0, 1, 2, …
Verification: Σ = (1/2)/(1 − 1/2) = 1 ✓.

**Example: Discrete distribution table.**
| X | −3 | −1 | 1 | 3 |
|---|----|----|---|---|
| f | 0.216 | 0.432 | 0.288 | 0.064 |

(Sum = 1.0 ✓)

### ⚠️ Common Mistakes
- ❌ Mistake: Allowing f(x) < 0 → ✅ Correct: A function with any negative value cannot be a p.m.f.
- ❌ Mistake: Missing the total-mass-1 check → ✅ Correct: Always verify Σ f(x_i) = 1 before using a function as a p.m.f.

> **Quick Recall:**
> - p.m.f.: f(x) = P(X = x), discrete only
> - Two conditions: f(x) ≥ 0 and Σ f(x_i) = 1
> - Used to compute means, variances, expectations of discrete RVs

---

## Section: Probability Density Function (p.d.f.) 🔴

### Core Idea
For **continuous** random variables, single values have probability **zero**, so we cannot list "P(X = x)." Instead the **probability density function f(x)** assigns probability to *intervals* via integration. The probability of X falling in (c, d) is the area under f(x) between c and d.

> **In Simple Terms:** With continuous random variables you don't ask "what's the chance of exactly 1.7 cm of rain?" — that's always 0. You ask "what's the chance of between 1 and 2 cm?" — that's the area under the density curve between those bounds.

### Key Concepts

#### Definition
A non-negative continuous function f(x) is a p.d.f. of continuous RV X if:
1. **f(x) ≥ 0** for all x.
2. **∫_a^b f(x) dx = 1** where (a, b) is the range of X.

#### Probability of an interval
**P(c ≤ X ≤ d) = ∫_c^d f(x) dx** = area under the probability curve between vertical lines x = c and x = d.

#### Total area
The area under the entire probability curve equals 1; the curve never goes below the x-axis.

| Aspect | p.m.f. | p.d.f. |
|--------|--------|--------|
| Type of RV | Discrete | Continuous |
| Value at a point | Probability P(X=x) | Density (not probability) |
| Sum-to-1 | Σ f(x_i) = 1 | ∫ f(x) dx = 1 |
| P(X = c) | f(c) | 0 (always) |
| P(c ≤ X ≤ d) | Σ over [c,d] | ∫_c^d f(x) dx |

### Definitions
- **Probability Density Function (p.d.f.)**: A continuous non-negative function f(x) with ∫_a^b f(x) dx = 1; gives P(c ≤ X ≤ d) = ∫_c^d f(x) dx. ⭐ (exam-important)

### Examples
**Example: f(x) = k·e^(−3x) for x > 0, 0 otherwise — find k and P(0.5 ≤ X ≤ 1).**

1. Solve for k: ∫₀^∞ k·e^(−3x) dx = 1 → k · [−e^(−3x)/3]₀^∞ = k/3 = 1 → **k = 3**.
2. P(0.5 ≤ X ≤ 1) = ∫_{0.5}^1 3 e^(−3x) dx = [−e^(−3x)]_{0.5}^1 = −e^(−3) + e^(−1.5) ≈ **0.173**.

### ⚠️ Common Mistakes
- ❌ Mistake: Treating f(c) as P(X = c) for continuous X → ✅ Correct: f(c) is a *density*; P(X = c) = 0 always for continuous RVs.
- ❌ Mistake: Forgetting f(x) can exceed 1 → ✅ Correct: Density values can be any non-negative number; only the *integral* must equal 1.

> **Quick Recall:**
> - Continuous: P(X = c) = 0; only intervals carry probability
> - p.d.f. f(x) ≥ 0 and ∫ f(x) dx = 1 over its range
> - P(c ≤ X ≤ d) = ∫_c^d f(x) dx (area under curve)

### Connections
- Builds on: [Probability Mass Function] (this chunk).
- Pre-requisite for: [Cumulative Distribution Function] (this chunk).
- Pre-requisite for: Normal distribution (Chunk 007: Poisson Examples & Sum-of-Poissons Property) — defined via its p.d.f.

---

## Section: Cumulative Distribution Function (c.d.f.) 🔴

### Core Idea
The **c.d.f. F(x) = P(X ≤ x)** is the running total of probability up to value x. It works for both discrete and continuous variables. For continuous RVs, F(x) is the area under the p.d.f. to the left of x; differentiation recovers f(x).

> **In Simple Terms:** The c.d.f. answers "what's the chance the variable is at most x?" It always rises from 0 (at −∞) to 1 (at +∞).

### Key Concepts

#### Definition
**F(c) = P(X ≤ c) = ∫_{−∞}^c f(x) dx** (continuous) or Σ_{x_i ≤ c} f(x_i) (discrete).

#### Properties
1. F(−∞) = 0, F(+∞) = 1.
2. F is non-decreasing: a < b ⇒ F(a) ≤ F(b).
3. **P(a ≤ X ≤ b) = F(b) − F(a)**.
4. f(x) = dF(x)/dx (continuous, where derivative exists).
5. P(X = c) = F(c) − F(c⁻) = 0 for continuous X.

### Definitions
- **Cumulative distribution function (c.d.f.) F(x)**: P(X ≤ x); area under p.d.f. to the left of x. ⭐ (exam-important)

### Examples
**Example: c.d.f. of f(x) = 3e^(−3x) for x > 0.**
- For x < 0: F(x) = 0.
- For x ≥ 0: F(x) = ∫₀^x 3e^(−3t) dt = 1 − e^(−3x).

Re-evaluate P(0.5 ≤ X ≤ 1) using c.d.f.:
P = F(1) − F(0.5) = (1 − e^(−3)) − (1 − e^(−1.5)) = e^(−1.5) − e^(−3) ≈ **0.173** ✓.

### ⚠️ Common Mistakes
- ❌ Mistake: Treating P(a < X < b) and P(a ≤ X ≤ b) as different for continuous RVs → ✅ Correct: They're equal because P(X = a) = P(X = b) = 0.

> **Quick Recall:**
> - F(x) = P(X ≤ x), monotone non-decreasing, 0 → 1
> - P(a ≤ X ≤ b) = F(b) − F(a)
> - f(x) = dF/dx (continuous)

### Connections
- Builds on: [Probability Density Function] (this chunk).

---

## Section: Moments — Definition and Importance 🔴

### Core Idea
**Moments** are expectations of integer powers of the random variable (or its centred version). They capture different features of a distribution: the first moment is the mean (location), the second central moment is the variance (spread), the third central moment relates to skewness, the fourth to kurtosis. A distribution is essentially characterised by its full set of moments.

> **In Simple Terms:** Moments are a sequence of numbers that progressively describe the shape of a distribution: mean, spread, asymmetry, peakedness. Knowing them is like knowing the silhouette of the distribution from far to near detail.

### Key Concepts

#### r-th moment about the origin (μ_r')
For discrete X: **μ_r' = E(x^r) = Σ x_i^r f(x_i)**.
For continuous X: **μ_r' = E(x^r) = ∫_{−∞}^∞ x^r f(x) dx**.
- r = 0: μ_0' = E(1) = 1.
- r = 1: μ_1' = E(x) = mean (often denoted μ).

#### r-th moment about the mean (μ_r)
For discrete X: **μ_r = E[(X − μ)^r] = Σ (x_i − μ)^r f(x_i)**.
- r = 1: μ_1 = 0 (always).
- r = 2: μ_2 = Var(x) = σ². ⭐
- r = 3: relates to skewness (asymmetry).
- r = 4: relates to kurtosis (tail heaviness).

#### Theorems on moments (stated)
1. **σ² = μ_2' − μ_1'²** (variance = second raw moment − square of mean).
2. **Var(aX + b) = a² · Var(X)** (location shift unchanged, scale squared).
3. **Chebyshev's theorem** (covered in next chunk).

#### Theorems on Mathematical Expectation (re-stated for completeness)
1. E(a + bX) = a + b·E(X).
2. E(a) = a (constant).
3. **E[Σ c_i ω(x_i)] = Σ c_i E[ω(x_i)]** (linearity).

### Definitions
- **r-th raw moment μ_r'**: E(x^r). ⭐ (exam-important)
- **r-th central moment μ_r**: E[(X − μ)^r]. ⭐ (exam-important)
- **Variance σ² = μ_2 = E[(X − μ)²] = E(x²) − [E(x)]²**. ⭐ (exam-important)

### Examples
**Example: Why "moment"?**
The term comes from physics. If f(x) is a "mass density" along the x-axis, then μ_1' (first moment about origin) is the centre of gravity, and μ_2' is related to the moment of inertia. Statistics borrows the geometric intuition.

**Visual (Fig. 26.4 in source):** Several distributions all have the same mean μ but progressively smaller variances: σ² = 5.26, 3.18, 1.66, 0.88 — high variance ↔ thick tails; low variance ↔ peaked at mean with thin tails.

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing raw and central moments (μ_2' vs μ_2) → ✅ Correct: μ_2 = μ_2' − μ_1'² (variance is *not* the second raw moment by itself).
- ❌ Mistake: Using Var(X + c) ≠ Var(X) → ✅ Correct: Adding a constant shifts location only; Var(X + c) = Var(X) (b = 1, a² = 1 in the theorem).

> **Quick Recall:**
> - μ_r' = E(x^r) (about origin); μ_r = E[(X − μ)^r] (about mean)
> - μ_1' = mean; μ_2 = variance = σ²
> - σ² = E(x²) − [E(x)]²
> - Var(aX + b) = a² Var(X)

### Connections
- Builds on: [Variance and Functions of a Random Variable] (Chunk 003: Variance and Functions of a Random Variable).
- Pre-requisite for: [Moment Generating Functions] (Chunk 005: Higher-order Moments — Skewness and Chebyshev's Theorem).

---

## Section: Check Your Progress 1 — p.m.f. validation 🟡

### Examples
**Q1: p.m.f. with parameter k.**
| x | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| P | 0 | k | 2k | 2k | 3k | k² | 2k² | 7k²+k |

Σ P = 0 + k + 2k + 2k + 3k + k² + 2k² + 7k² + k = 10k² + 9k = 1 → **10k² + 9k − 1 = 0** → k = 1/10 (rejecting k = −1).

**Q2: Validity of p.m.f. candidates.**
- f(x) = (x − 2)/5 for x = 1..5: at x = 1, f = −1/5 < 0 → ❌ not valid (probability cannot be negative).
- f(x) = x²/30 for x = 0..4: all non-negative; sum = 0 + 1 + 4 + 9 + 16 = 30; 30/30 = 1 → ✓ valid p.m.f.
- f(x) = 1/5 for x = 0..5: 6 values × 1/5 = 6/5 ≠ 1 → ❌ not valid.

> **Quick Recall:**
> - Always validate p.m.f. via (i) f(x) ≥ 0 and (ii) Σ f(x) = 1.

### Open Questions
1. What does it mean for a distribution to *not* be characterised by its moments? (Some heavy-tailed distributions like the lognormal have moment problems — outside the syllabus.)


---


## Section: Higher-order Moments — Skewness and Chebyshev's Theorem 🔴
<!-- See chunk 004 for start of Moments -->

### Core Idea
The **third central moment** (μ_3) describes the **symmetry / skewness** of a distribution. The variance + Chebyshev's theorem together give a *distribution-free* bound on how often a random variable deviates from its mean — a remarkable fact with no shape assumption.

> **In Simple Terms:** Variance only tells you how spread out a distribution is. The third moment tells you whether the spread is symmetric (μ_3 = 0) or lopsided to one side. Chebyshev says: no matter what the distribution looks like, it's "rare" for X to be many σ's away from μ — and quantifies how rare.

### Key Concepts

#### Skewness via μ_3
The third moment about the mean describes asymmetry: μ_3 = 0 for symmetric distributions; μ_3 > 0 for right-skewed (tail extends right); μ_3 < 0 for left-skewed.

#### Chebyshev's Theorem
If X has mean μ and variance σ² (with σ ≠ 0), then for any constant k:
**P(|X − μ| < k·σ) ≥ 1 − 1/k²**.

Equivalently, **P(|X − μ| ≥ k·σ) ≤ 1/k²**.

This is **distribution-free** — no normality assumption. Crude but universal.

| k | Lower bound on P(|X − μ| < kσ) |
|---|--------------------------------|
| 1 | 0 (trivial) |
| 2 | 1 − 1/4 = 0.75 |
| 3 | 1 − 1/9 ≈ 0.889 |
| 4 | 1 − 1/16 = 0.9375 |

(Compare with normal: P(|X − μ| < 2σ) ≈ 0.9545; Chebyshev's 0.75 is much weaker but holds for *any* distribution.)

### Definitions
- **Chebyshev's Theorem**: For any RV X with mean μ and variance σ², P(|X − μ| < kσ) ≥ 1 − 1/k². ⭐ (exam-important)
- **Skewness**: Asymmetry of a distribution; μ_3 ≠ 0 indicates skew.

> **Quick Recall:**
> - μ_3 governs skewness; μ_3 = 0 ⇒ symmetric distribution
> - Chebyshev: P(|X − μ| ≥ kσ) ≤ 1/k² (any distribution)
> - At k = 2 ⇒ at most 25% of mass beyond 2σ

---

## Section: Moment Generating Function (MGF) 🔴

### Core Idea
The **moment generating function** M_X(t) = E(e^(tX)) is a single function of t whose Maclaurin coefficients are exactly the moments of X. So the MGF "packages" all moments together — by differentiating M_X(t) r times at t = 0 you read off the r-th raw moment μ_r'. It's the standard tool for deriving the mean, variance, and key properties of binomial, Poisson, and normal distributions.

> **In Simple Terms:** The MGF is a generating function — a magical formula whose Taylor series expansion gives you all the moments of the distribution in one shot. Differentiate r times, plug in t = 0, and out pops μ_r'.

### Key Concepts

#### Definition
- Discrete: **M_X(t) = E(e^(tX)) = Σ_i e^(t·x_i) · f(x_i)**.
- Continuous: **M_X(t) = ∫_{−∞}^∞ e^(tx) · f(x) dx**.

t is in a neighbourhood of 0; the MGF is required to exist there.

#### Why "moment generating"?
Use Maclaurin's series: e^(tx) = 1 + tx + (tx)²/2! + (tx)³/3! + …
So **M_X(t) = 1 + t·μ_1' + t²/2! · μ_2' + t³/3! · μ_3' + … + t^r/r! · μ_r' + …**
The coefficient of t^r/r! in M_X(t) is **μ_r'** (the r-th raw moment).

#### Recovery formula
**μ_r' = d^r M_X(t)/dt^r |_(t=0)**.

#### Key MGF transformation rules
For constants a, b:
1. **M_(X+a)(t) = e^(at) · M_X(t)**.
2. **M_(bX)(t) = M_X(bt)**.
3. **M_((X+a)/b)(t) = e^((a/b)t) · M_X(t/b)**.

Special case (standardisation): with a = −μ, b = σ:
**M_((X−μ)/σ)(t) = e^(−μt/σ) · M_X(t/σ)** — used to get the standardised variable's MGF.

### Definitions
- **Moment Generating Function (MGF)**: M_X(t) = E(e^(tX)). ⭐ (exam-important)
- **Generating relation**: μ_r' = M_X^(r)(0) = the r-th derivative of M_X(t) at t = 0. ⭐ (exam-important)

### Mechanisms / Processes
Step-by-step recipe to find moments via MGF:
1. Write M_X(t) = E(e^(tX)) — sum or integral.
2. Compute closed-form M_X(t) (often using known series like geometric, exponential).
3. Differentiate once: μ_1' = M'(0) = mean.
4. Differentiate twice: μ_2' = M''(0) = E(X²); then σ² = μ_2' − μ_1'².

### Examples
**Example: f(x) = e^(−x) for x > 0 (exponential distribution).**
M_X(t) = ∫₀^∞ e^(tx) e^(−x) dx = ∫₀^∞ e^(−(1−t)x) dx = **1/(1 − t)** for t < 1.

Maclaurin expansion: 1/(1 − t) = 1 + t + t² + t³ + … = Σ t^r = Σ (r!) · t^r/r!.
So **μ_r' = r!** for r = 0, 1, 2, … (Mean = 1, Var = 2! − 1² = 1, etc.).

**Example (Check Your Progress 2): X ~ p.m.f. f(x) = (1/8) · ³C_x for x = 0,1,2,3.**
M_X(t) = Σ_{x=0..3} e^(tx) · (1/8) · ³C_x = (1/8) · (1 + e^t)³ (binomial expansion).
- M'(t) at t = 0: μ_1' = (3/8)(1+1)² = 12/8 = **3/2** = mean.
- M''(t) at t = 0: μ_2' = **3** = E(X²).
- σ² = 3 − (3/2)² = 3 − 9/4 = **3/4**.

> **Quick Recall:**
> - **M_X(t) = E(e^(tX))**
> - μ_r' = r-th derivative at t = 0
> - Linear shifts: M_(X+a) = e^(at) M_X(t); M_(bX) = M_X(bt)

### Connections
- Builds on: [Moments — Definition] (Chunk 004: Random Variables — Discrete vs Continuous).
- Pre-requisite for: [MGF of Binomial / Poisson / Normal] (Chunks 006–007).

---

## Section: Unit 26 Summary, Key Words, Exercises 🟢

### Definitions (Key Words — verbatim restatements ⭐)
- **Continuous Random Variable**: A random variable that can take any value within its range.
- **Discrete Random Variable**: A random variable that takes only countable values, with no possible value located between two adjacent ones.
- **Probability Distribution**: Statement specifying the set of possible values together with their respective probabilities.
- **Probability Mass Function (p.m.f.)**: f(x) = P(X = x) for discrete X, satisfying f(x) > 0 and Σ f(x_i) = 1.
- **Probability Density Function (p.d.f.)**: A continuous non-negative function f(x) for continuous X, giving P(c ≤ X ≤ d) = ∫_c^d f(x) dx, with ∫_a^b f(x) dx = 1 over the range (a, b).

### Examples (Exercise solutions)

**Q1: Fair coin tossed twice; X = number of heads. Find R(X) and p.m.f. P_X.**
Sample space S = {HH, HT, TH, TT}. R(X) = {0, 1, 2}.
- P_X(0) = 1/4 (TT)
- P_X(1) = 2/4 = 1/2 (HT, TH)
- P_X(2) = 1/4 (HH)

**Q2: Find r given p.m.f. P(Y).**
| Y | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| P | 0 | 2r | 3r | 6r² |

Σ P = 1 ⇒ 0 + 2r + 3r + 6r² = 1 ⇒ 6r² + 5r − 1 = 0.
Factoring: (6r − 1)(r + 1) = 0 ⇒ r = 1/6 or r = −1. Reject r = −1 (probability constraint). **r = 1/6**.

**Q3: Two conditions for p.d.f.**
1. f(x) ≥ 0 for all x.
2. Total area under f(x) equals 1.

**Q4: Difference between p.m.f. and p.d.f.**
- p.d.f. describes a **continuous** probability distribution.
- p.m.f. describes a **discrete** probability distribution.

> **Quick Recall:**
> - Always end p.m.f./p.d.f. validity check with Σ = 1 / ∫ = 1.
> - Reject negative or out-of-range solutions to algebraic constraints.

---

## Section: Joint Probability Distribution — Discrete and Continuous 🔴

### Core Idea
When more than one random variable is involved, we use a **joint distribution** f(x, y) = P(X = x, Y = y) (discrete) or its continuous analogue f(x, y) (a 2-D density). The two-dimensional p.m.f./p.d.f. encodes the *complete* statistical relationship between X and Y. Independence of X, Y is the special case where f(x, y) factorises into f_X(x) · f_Y(y).

> **In Simple Terms:** Where one variable's distribution is a curve, two variables' joint distribution is a surface above the (x, y) plane. The "volume" under that surface is 1.

### Key Concepts

#### Discrete joint p.m.f.
For discrete X, Y: **f(x, y) = P(X = x, Y = y)**. Conditions:
1. f(x, y) ≥ 0 for every pair (x, y) in the domain.
2. **ΣΣ f(x, y) = 1** — double sum over all (x, y).

#### Continuous joint p.d.f.
For continuous X, Y: f(x, y) is a non-negative bivariate function with:
1. f(x, y) ≥ 0 for −∞ < x < ∞, −∞ < y < ∞.
2. **∫∫ f(x, y) dx dy = 1**.
3. P[(X, Y) ∈ A] = ∫∫_A f(x, y) dx dy for any region A.

#### Joint cumulative distribution (c.d.f.)
- Discrete: **F(x, y) = P(X ≤ x, Y ≤ y) = Σ_{s≤x} Σ_{t≤y} f(s, t)**.
- Continuous: F(x, y) = ∫_{−∞}^x ∫_{−∞}^y f(s, t) ds dt; recover density via **f(x, y) = ∂²F(x, y)/∂x∂y**.

#### Independence
**X and Y independent ⇔ f(x, y) = f_X(x) · f_Y(y)** for all (x, y).
Generalises: random variables X₁, …, X_n are mutually independent if every subset's joint p.m.f./p.d.f. equals the product of marginals.

### Definitions
- **Joint probability distribution f(x, y)**: P(X = x, Y = y) for discrete RVs; f(x, y) ≥ 0 and ΣΣ f = 1. ⭐ (exam-important)
- **Joint p.d.f.**: Continuous bivariate analogue with f ≥ 0 and ∫∫ f dx dy = 1. ⭐ (exam-important)
- **Independence (joint)**: f(x, y) = f_X(x) · f_Y(y). ⭐ (exam-important)

### Examples
**Example: f(x, y) = k·xy for x, y ∈ {1, 2, 3} — find k.**
Sum over all 9 cells:
ΣΣ kxy = k · (Σ_x x)(Σ_y y) = k · 6 · 6 = 36k = 1 ⇒ **k = 1/36**.

**Example: 100-word corpus.**
Word | c(w) | P(w) | x = length | y = vowels
---|---|---|---|---
Shall | 5 | 0.05 | 5 | 1
Up | 8 | 0.08 | 2 | 1
Next | 5 | 0.05 | 4 | 1
As | 5 | 0.05 | 2 | 1
Fore | 3 | 0.03 | 4 | 2
To | 10 | 0.10 | 2 | 1
We | 12 | 0.12 | 2 | 1
Some | 8 | 0.08 | 4 | 2
Will | 30 | 0.30 | 4 | 1
BBC | 14 | 0.14 | 3 | 0

Joint p.m.f. f(x, y) = P(X = x, Y = y), e.g.:
- f(4, 2) = P(Fore) + P(Some) = 0.03 + 0.08 = **0.11**.
- f(3, 0) = P(BBC) = **0.14**.
- f(2, 1) = P(Up) + P(As) + P(To) + P(We) = 0.08 + 0.05 + 0.10 + 0.12 = **0.35**.

| | x = 2 | x = 3 | x = 4 | x = 5 |
|--|------|-------|-------|-------|
| y = 0 | 0 | 0.14 | 0 | 0 |
| y = 1 | 0.35 | 0.30 | 0.05 | 0.05 |
| y = 2 | 0 | 0 | 0.11 | 0 |

(Verify: total = 1.00 ✓.)

### ⚠️ Common Mistakes
- ❌ Mistake: Validating only Σ_x f(x, y) = 1 instead of the **double sum** → ✅ Correct: Joint p.m.f. requires Σ_x Σ_y f(x, y) = 1.
- ❌ Mistake: Assuming independence whenever f(x, y) is given → ✅ Correct: Must verify factorisation f(x, y) = f_X(x) f_Y(y) for *all* (x, y).

> **Quick Recall:**
> - Joint p.m.f./p.d.f. — 2-D analogue of single-variable case
> - Total mass = 1 (double sum or double integral)
> - Independence ⇔ product of marginals

### Connections
- Builds on: [Probability Mass Function] and [Probability Density Function] (Chunk 004: Random Variables — Discrete vs Continuous).
- Pre-requisite for: [Marginal Distribution] (Chunk 006: Joint c.d.f. — Worked Example).

### Open Questions
1. How does conditional density f(y|x) = f(x, y)/f_X(x) generalise the discrete conditional probability formula?


---


## Section: Joint c.d.f. — Worked Example 🟡
<!-- See chunk 005 for start of Joint Distribution -->

### Examples
**Example: Find joint c.d.f. for f(x, y) = (x + y) on 0 ≤ x ≤ 1, 0 ≤ y ≤ 1.**

Region I (0 ≤ x ≤ 1, 0 ≤ y ≤ 1):
F(x, y) = ∫₀^x ∫₀^y (s + t) dt ds = (1/2)·xy(x + y).

Region II (x ≥ 1, 0 ≤ y ≤ 1):
F(x, y) = ∫₀^1 ∫₀^y (s + t) dt ds = (1/2)·y(1 + y).

Region III (0 ≤ x ≤ 1, y ≥ 1):
F(x, y) = (1/2)·x(1 + x).

Region IV (x ≥ 1, y ≥ 1):
F(x, y) = 1.

Combined (with boundaries absorbed):
- F(x, y) = 0 for x < 0 or y < 0.
- F(x, y) = (1/2)·xy(x + y) for 0 ≤ x ≤ 1, 0 ≤ y ≤ 1.
- F(x, y) = (1/2)·y(1 + y) for x ≥ 1, 0 ≤ y ≤ 1.
- F(x, y) = (1/2)·x(1 + x) for 0 ≤ x ≤ 1, y ≥ 1.
- F(x, y) = 1 for x ≥ 1, y ≥ 1.

> **Quick Recall:**
> - Continuous joint c.d.f. is a *piecewise* function over rectangle regions.
> - Recover joint p.d.f. by ∂²F/∂x∂y.

---

## Section: Marginal Distribution 🔴

### Core Idea
A **marginal distribution** is what you get when you "ignore" or "sum out" one variable from a joint distribution. The marginal of X collapses the joint over all values of Y; it's the distribution of X by itself, regardless of Y.

> **In Simple Terms:** If the joint distribution is a heatmap of how (X, Y) values occur together, the marginal of X is the row totals, and the marginal of Y is the column totals.

### Key Concepts

#### Discrete marginals
- **g(x) = Σ_y f(x, y)** — marginal distribution of X.
- **h(y) = Σ_x f(x, y)** — marginal distribution of Y.

#### Continuous marginals
- **g(x) = ∫_{−∞}^∞ f(x, y) dy** — marginal density of X.
- **h(y) = ∫_{−∞}^∞ f(x, y) dx** — marginal density of Y.

### Definitions
- **Marginal distribution of X**: g(x) = Σ_y f(x, y) (discrete) / ∫ f(x, y) dy (continuous). ⭐ (exam-important)

### Examples
**Example: Marginal distribution from the 100-word table (continued from Chunk 005).**

Marginal of X (column sums): | x = 2 | x = 3 | x = 4 | x = 5 |
| | 0.35 | 0.44 | 0.16 | 0.05 |

Marginal of Y (row sums): | y = 0 | y = 1 | y = 2 |
| | 0.14 | 0.75 | 0.11 |

(Both add to 1.00 ✓.)

**Example (Check Your Progress 1, Q2): f(x, y) = (2/3)(x + 2y) for 0 ≤ x, y ≤ 1.**
Marginal of X:
g(x) = ∫₀¹ (2/3)(x + 2y) dy = (2/3)[xy + y²]₀¹ = (2/3)(x + 1) = **(1/3)(2x + 2)** for 0 ≤ x ≤ 1.

> **Quick Recall:**
> - Marginal = "row/column total" for joint p.m.f.
> - Use Σ over the *other* variable (or ∫ in continuous case)
> - Marginals must each sum/integrate to 1 individually

### Connections
- Builds on: [Joint Probability Distribution] (Chunk 005: Higher-order Moments — Skewness and Chebyshev's Theorem).
- Connects to: [Conditional distribution] = joint / marginal of conditioning variable.

---

## Section: Binomial Distribution 🔴

### Core Idea
The **binomial distribution** describes the number of "successes" in **n independent identical trials**, each with probability p of success. It's the model for repeated yes/no experiments — coin flips, defectives in a batch, recoveries in clinical trials. Binomial is the bedrock discrete distribution from which Poisson and (via the central limit theorem) the normal approximation are derived.

> **In Simple Terms:** Toss the same biased coin n times — how many heads do you get? That count follows the binomial distribution. The whole shape is determined by just two numbers: n (number of trials) and p (probability of success per trial).

### Key Concepts

#### p.m.f.
**f(x) = ⁿC_x · p^x · q^(n−x)**, x = 0, 1, …, n; q = 1 − p.

Defined when:
1. Each trial has only **two outcomes** (success / failure).
2. The probability **p is constant** across trials.
3. Trials are **independent**.

#### Parameters
n (number of trials) and p (probability of success). Together they determine the distribution completely.

#### Mean and variance
- **Mean μ = n·p**.
- **Variance σ² = n·p·q = n·p·(1−p)**.

#### Mode
- If (n+1)p is **not an integer**: mode = largest integer < (n+1)p.
- If (n+1)p is an integer: there are **two modes**, at (n+1)p and (n+1)p − 1.

#### Skewness and kurtosis
- Skewness = **(q − p) / √(npq)**.
- Kurtosis = 1 − 6pq / (npq)... (kurtosis is *positive when p < 0.5 or p > 0.5* — symmetric only at p = q = 1/2).
- When p = q = 1/2, distribution is **symmetric** for all n.

#### Sum of independent binomials (additive property)
If X ~ Bin(n₁, p) and Y ~ Bin(n₂, p) (same p, independent), then **(X + Y) ~ Bin(n₁ + n₂, p)**.
Generalises to any number of independent binomials with shared p.

#### Moment Generating Function
M_X(t) = E(e^(tX)) = Σ ⁿC_x (p·e^t)^x (1−p)^(n−x) = **(p·e^t + 1 − p)^n** = **{1 + p(e^t − 1)}^n**.
- M'(0) = np ⇒ μ = np.
- M''(0) = np(1 − p + np) ⇒ σ² = np(1 − p).

### Definitions
- **Binomial Distribution**: P(X = x) = ⁿC_x · p^x · (1−p)^(n−x), x = 0, 1, …, n. Two parameters (n, p). ⭐ (exam-important)
- **Bernoulli trial**: A single trial of a binomial — two outcomes, probability p of success.

### Mechanisms / Processes
Deriving μ = np algebraically:
1. μ = E(X) = Σ_x x · ⁿC_x p^x q^(n−x).
2. Use x · ⁿC_x = n · ⁽ⁿ⁻¹⁾C_(x−1).
3. Pull out np: μ = np · Σ_y ⁽ⁿ⁻¹⁾C_y p^y q^(n−1−y) where y = x − 1.
4. Inner sum is total mass of Bin(n − 1, p), which equals 1.
5. Therefore **μ = np**.

Deriving σ² = np(1 − p):
1. Compute E[X(X − 1)] = n(n − 1)p² (similar reduction).
2. E(X²) = E[X(X − 1)] + E(X) = n(n − 1)p² + np.
3. σ² = E(X²) − μ² = n(n − 1)p² + np − n²p² = np − np² = **np(1 − p)**.

### Examples
**Example: Probability of getting 7 heads in 12 tosses of an unbiased coin.**
n = 12, x = 7, p = 1/2, q = 1/2.
P = ¹²C₇ · (1/2)⁷ · (1/2)⁵ = ¹²C₇ · (1/2)¹².

**Example: Three coin tosses.**
n = 3, p = 1/2.
- P(X = 0) = ³C₀(1/2)³ = 1/8.
- P(X = 1) = ³C₁(1/2)³ = 3/8.
- P(X = 2) = ³C₂(1/2)³ = 3/8.
- P(X = 3) = ³C₃(1/2)³ = 1/8.
- P(more than 1 head) = 3/8 + 1/8 = 4/8 = 1/2.
- P(at least 1 head) = 1 − P(0 heads) = 1 − 1/8 = 7/8.

**Example: Mean = 4, std dev = √(8/3) — find n and p.**
np = 4, npq = 8/3 ⇒ q = (8/3)/4 = 2/3, p = 1/3, n = 4 / (1/3) = **12**.

**Example: Pass rate 60%, group of 6 — P(at least 4 passed)?**
p = 0.6, q = 0.4, n = 6.
f(4) + f(5) + f(6) = ⁶C₄·0.6⁴·0.4² + ⁶C₅·0.6⁵·0.4 + ⁶C₆·0.6⁶ = 1701/3125.

### ⚠️ Common Mistakes
- ❌ Mistake: Applying binomial when trials are dependent (e.g., draws without replacement) → ✅ Correct: Use hypergeometric distribution; binomial requires *independent* trials.
- ❌ Mistake: Confusing p.m.f. parameter (p) with sample proportion → ✅ Correct: p is the *true* per-trial success probability, fixed and known.

> **Quick Recall:**
> - **Binomial: P(X = x) = ⁿC_x p^x q^(n−x)**
> - μ = np, σ² = npq
> - Two parameters: (n, p)
> - Symmetric ⇔ p = 1/2
> - Sum of independent Bin(n_i, p) is Bin(Σn_i, p)
> - MGF: (pe^t + q)^n

### Connections
- Builds on: [Independent Events] (Chunk 002: Theorem of Total Probability (Addition Theorem)), [Mathematical Expectation] (Chunks 002–003).
- Pre-requisite for: [Poisson Distribution] (this chunk) — Poisson is the limit n→∞, p→0, np = λ.

---

## Section: Poisson Distribution 🔴

### Core Idea
The **Poisson distribution** is the **limiting case** of the binomial when n → ∞ and p → 0 with **np = λ** held constant. It models the number of rare events in a fixed period — accidents per day, defects per unit area, calls per hour. It has **a single parameter λ** which equals both the mean *and* the variance.

> **In Simple Terms:** When something rare happens repeatedly with low probability across many opportunities, the count follows a Poisson distribution. Examples: number of typos per page, number of customers arriving in an hour, number of cars at a traffic signal.

### Key Concepts

#### p.m.f.
**P(X = x; λ) = (e^(−λ) · λ^x) / x!** for x = 0, 1, 2, …
Single parameter λ > 0; e ≈ 2.718.

#### Derivation as binomial limit
Set p = λ/n in binomial p.m.f. and let n → ∞ (with λ fixed):
- (1 − 1/n)(1 − 2/n)…(1 − (x − 1)/n) → 1.
- (1 − λ/n)^(−x) → 1.
- (1 − λ/n)^n → e^(−λ).
- ⁿC_x · p^x → λ^x / x!.

So binomial → **e^(−λ) · λ^x / x!** = Poisson p.m.f.

#### Properties
- **Mean = Variance = λ**.
- **Skewness = 1/√λ** ⇒ positively skewed.
- **Kurtosis = 1/λ** ⇒ leptokurtic (more peaked than normal).
- **Mode**: largest integer ≤ λ if λ not integer; two modes (λ and λ − 1) if integer.
- **Sum of independent Poissons**: X₁ ~ Poi(λ₁), X₂ ~ Poi(λ₂) ⇒ (X₁ + X₂) ~ Poi(λ₁ + λ₂).

#### Moment Generating Function
M_X(t) = e^(−λ) · Σ_x (λe^t)^x / x! = **e^(−λ) · e^(λe^t) = e^(λ(e^t − 1))**.
- M'(0) = λ ⇒ μ = λ.
- M''(0) = λ + λ² ⇒ Var = (λ + λ²) − λ² = **λ**.

#### When to use Poisson
- Number of accidents on a road crossing.
- Number of defects per unit area of cloth.
- Number of phone calls received by an operator.
- Number of suicides per year in an area.
- Approximation to binomial when **n is large** and **p is small** (n.p moderate).

### Definitions
- **Poisson Distribution**: P(X = x; λ) = e^(−λ) λ^x / x!, x = 0, 1, 2, …; one parameter λ. ⭐ (exam-important)
- **Mean = Variance = λ** is the signature property of Poisson. ⭐ (exam-important)

### Mechanisms / Processes
Setting up a Poisson approximation to binomial:
1. Verify n is large and p is small.
2. Compute λ = np.
3. Use P(X = x) = e^(−λ) λ^x / x! in place of the binomial p.m.f.

### Examples
**Example: P(X = 1) = P(X = 2) for Poisson — find P(X = 0 or 1) and E(X).**
P(X = 1) = λ·e^(−λ); P(X = 2) = λ² e^(−λ)/2. Equating: λ = λ²/2 ⇒ **λ = 2**.
- E(X) = λ = **2**.
- P(X = 0 or 1) = e^(−2) + 2·e^(−2) = **3·e^(−2)**.

**Example: λ = 3, e^(−3) = 0.0498. Find P(X = 0, 1, 2, 3), P(X < 3), P(X ≥ 2).**
- f(0) = e^(−3) = 0.0498.
- f(1) = 3·e^(−3) = 3·(0.0498) = 0.1494.
- f(2) = (9/2)·e^(−3) = 9·(0.0498)/2 = 0.2241.
- f(3) = (27/6)·e^(−3) = 27·(0.0498)/6 = 0.2241.
- P(X < 3) = f(0) + f(1) + f(2).
- P(X ≥ 2) = 1 − f(0) − f(1) = 1 − 4·(0.0498).

### ⚠️ Common Mistakes
- ❌ Mistake: Using Poisson when the rate varies over the observation window → ✅ Correct: Poisson assumes constant rate (homogeneous).
- ❌ Mistake: Using λ as a probability → ✅ Correct: λ is a *count rate*; can be > 1.

> **Quick Recall:**
> - **P(X = x) = e^(−λ) λ^x / x!**
> - **Mean = Variance = λ**
> - Limit of Bin(n, p) as n→∞, p→0, np = λ
> - Sum of independent Poissons is Poisson with summed λ
> - MGF: e^(λ(e^t − 1))

### Connections
- Builds on: [Binomial Distribution] (this chunk).
- Pre-requisite for: [Normal Distribution] (Chunk 007: Poisson Examples & Sum-of-Poissons Property) — for large λ, Poisson approaches normal.

### Open Questions
1. What is the practical threshold (e.g., n > 20, p < 0.05) for using Poisson approximation to binomial?


---


## Section: Poisson Examples & Sum-of-Poissons Property 🔴
<!-- See chunk 006 for start of Poisson Distribution -->

### Examples
**Example: 5 defects per 10 sq.ft of cloth — P(at least 6 defects in 15 sq.ft)?**
Average defects per 15 sq.ft = (5/10) × 15 = 7.5. So λ = 7.5.
P(X ≥ 6) = 1 − P(X ≤ 5).
Using Poisson tables (Table 27.5 in source): P(X ≤ 5) = 0.2415.
Therefore **P(X ≥ 6) = 1 − 0.2415 = 0.7585**.

| x | P(X = x) at λ = 7.5 |
|---|---------------------|
| 0 | 0.0006 |
| 1 | 0.0041 |
| 2 | 0.0156 |
| 3 | 0.0389 |
| 4 | 0.0729 |
| 5 | 0.1094 |

### Mechanisms / Processes
Proof that Sum of independent Poisson is Poisson (using p.m.f.):
1. P[X₁ + X₂ = k] = Σ_{k₁=0..k} P[X₁ = k₁] P[X₂ = k − k₁].
2. = e^(−λ₁) e^(−λ₂) · (1/k!) · Σ_{k₁} kCk₁ · λ₁^k₁ · λ₂^(k−k₁) (binomial expansion).
3. = e^(−(λ₁+λ₂)) · (λ₁ + λ₂)^k / k!.
4. ⇒ X₁ + X₂ ~ Poi(λ₁ + λ₂). Generalises to n variables.

### Examples
**Example (CYP 2 Q5): Average defective rate 10% — P(exactly 3 defectives in sample of 10)? Use Poisson approximation, e = 2.72.**
λ = 10 × 0.1 = 1.
f(3) = e^(−1) · 1³ / 3! = 0.3679 / 6 ≈ **0.061**.

**Example (CYP 2 Q6): 2% items defective; sample of 100; P(3 or more defectives)?**
λ = np = 100 × 0.02 = 2.
P(≥ 3) = 1 − [f(0) + f(1) + f(2)] = 1 − e^(−2) [1 + 2 + 4/2] = 1 − e^(−2) · 5 ≈ 1 − 0.135·5 = **0.325**.

**Example (CYP 2 Q7): P(7 of 10 recover from disease), p = 0.8, independence.**
n = 10, p = 0.8, x = 7.
P = ¹⁰C₇ · (0.8)⁷ · (0.2)³ ≈ **0.20**.

> **Quick Recall:**
> - λ scales linearly with the size of the observation interval (e.g., per 15 sq.ft = 1.5 × per 10 sq.ft).
> - Sum of independent Poissons → Poisson with summed λ.

---

## Section: Normal Distribution 🔴

### Core Idea
The **normal distribution** is the most important continuous distribution in statistics. Its bell-shaped p.d.f. is fully determined by two parameters: the **mean μ** (location) and **standard deviation σ** (spread). It models measurement errors, heights, IQ scores, and (via the Central Limit Theorem) the sum of many independent random variables. Modern statistical inference rests on properties of the normal distribution.

> **In Simple Terms:** The "bell curve." Drop a dart at the centre many times — the spread of misses follows a normal distribution. So do most natural measurements when many small random factors add up.

### Key Concepts

#### p.d.f.
**f(x) = (1 / (σ·√(2π))) · exp(−(x − μ)² / (2σ²))** for −∞ < x < ∞, σ > 0.

#### Parameters
- μ = mean (also median, mode — they coincide).
- σ = standard deviation.

#### Properties (full list — high yield)

1. **Continuous probability distribution.**
2. **Two parameters**: μ and σ.
3. **Symmetric about μ** — mean = mode = median.
4. **Quartiles**: Q₁ ≈ μ − 0.67σ; Q₃ ≈ μ + 0.67σ (equidistant from μ).
5. **All odd central moments = 0** (μ_(2r+1) = 0 for r = 1, 2, 3, …) — direct corollary of symmetry.
6. **Tails extend to infinity** on both sides; never touch the horizontal axis.
7. **Maximum ordinate** = 1 / (σ·√(2π)), at x = μ.
8. **Beyond x = μ ± 3σ** the density is essentially zero.
9. **Inflexion points** at x = μ ± σ — where curvature changes.
10. **Unimodal**: f'(x) > 0 for x < μ; f'(x) < 0 for x > μ; f'(μ) = 0.
11. **P(X = c) = 0** for any constant c (continuous).
12. P(X > a) = area under the curve to the right of a.
13. **Empirical Rule (68–95–99.7)**:
    - ≈ 68% within 1σ of mean.
    - ≈ 95% within 2σ of mean.
    - ≈ 99.7% within 3σ of mean.
14. **Sum of two independent normals**: X ~ N(μ₁, σ₁²), Y ~ N(μ₂, σ₂²) ⇒ X + Y ~ N(μ₁ + μ₂, σ₁² + σ₂²).

#### Moment Generating Function
**M_X(t) = exp(μt + σ²t²/2)**.
- M'(0) = μ ⇒ E(X) = μ.
- M''(0) = μ² + σ² ⇒ Var(X) = σ².

### Definitions
- **Normal Distribution**: f(x) = (1/(σ√(2π))) exp(−(x − μ)²/(2σ²)). Two parameters: mean μ, std dev σ. ⭐ (exam-important)
- **Empirical Rule (68-95-99.7)**: 1σ, 2σ, 3σ contain ≈ 68%, 95%, 99.7% of the area. ⭐ (exam-important)

### Mechanisms / Processes
Verification ∫f(x) dx = 1:
1. Substitute z = (x − μ)/σ, dx = σ dz.
2. Integral becomes (1/√(2π)) ∫_{−∞}^∞ e^(−z²/2) dz.
3. By symmetry: 2 × (1/√(2π)) ∫₀^∞ e^(−z²/2) dz.
4. Using Gaussian integral ∫₀^∞ e^(−z²/2) dz = √(π/2).
5. = 2 · (1/√(2π)) · √(π/2) = 1 ✓.

> **Quick Recall:**
> - **f(x) = (1/(σ√(2π))) e^(−(x−μ)²/(2σ²))**
> - μ = mean = median = mode (symmetric)
> - σ controls spread; ±3σ contains 99.7%
> - 68-95-99.7 rule
> - MGF: e^(μt + σ²t²/2)

---

## Section: Standard Normal Distribution & Standardisation 🔴

### Core Idea
Any normal random variable X ~ N(μ, σ²) can be transformed into a **standard normal variable** Z = (X − μ)/σ with mean 0 and variance 1. The c.d.f. of Z is tabulated as Φ(z), so any normal probability calculation reduces to looking up Φ values. The Central Limit Theorem is what makes this trick worth memorising.

> **In Simple Terms:** Subtract the mean and divide by the standard deviation, and your normal variable becomes "standard" — mean 0, std dev 1. Now you can use a single universal table to find any normal probability.

### Key Concepts

#### Z transformation
**Z = (X − μ)/σ** ⇒ **Z ~ N(0, 1)**.

#### Standard normal p.d.f.
**φ(z) = (1/√(2π)) · exp(−z²/2)** for −∞ < z < ∞.

#### Standard normal c.d.f.
**Φ(z) = ∫_{−∞}^z φ(t) dt** = area to the left of z.
By symmetry: **Φ(−z) = 1 − Φ(z)**.

#### Key area facts (must memorise)
- Area between z = ±3 ⇒ 99.73%.
- Area between z = ±2.58 ⇒ 99%.
- Area between z = ±1.96 ⇒ 95%.

#### Critical values (right-tail areas) — used in hypothesis testing
- z = 1.645 ⇒ right-tail area 5% (denoted z_(0.05)).
- z = 1.96 ⇒ right-tail area 2.5% (z_(0.025)).
- z = 2.33 ⇒ right-tail area 1% (z_(0.01)).

#### Theorem (linear transformation of a normal)
If X ~ N(μ, σ²) and Y = a + bX (b ≠ 0), then **Y ~ N(a + bμ, b²σ²)**.
Special case (a = −μ/σ, b = 1/σ): Y = (X − μ)/σ ~ N(0, 1).

### Definitions
- **Standard Normal Variable Z**: Z = (X − μ)/σ when X ~ N(μ, σ²); follows N(0, 1). ⭐ (exam-important)
- **Φ(z)**: Cumulative distribution function of N(0, 1). ⭐ (exam-important)
- **Upper α-point t_α**: Value such that P(Z > t_α) = α; lower α-point is −t_α (by symmetry).

### Mechanisms / Processes
Standardised normal probability lookup recipe:
1. Identify μ and σ of the original normal X.
2. Convert each boundary to z-scores: z = (x − μ)/σ.
3. Look up Φ(z) in standard normal tables.
4. Combine via Φ(z₂) − Φ(z₁) for an interval, or 1 − Φ(z) for right-tail.

### Examples
**Example: Heights of 10,000 men, X ~ N(64.5, 4.5²).**
Convert to z: z = (X − 64.5)/4.5.

| x | z |
|---|---|
| 55.5 | −2 |
| 64.5 | 0 |
| 69 | 1 |
| 73.5 | 2 |

(a) P(55.5 < X < 69) = P(−2 < Z < 1) = Φ(1) − Φ(−2) = 0.84 − 0.02 ≈ 0.82.
Number of men: 10,000 × 0.82 = **8,200**.

(b) P(X < 55.5) = P(Z < −2) ≈ 0.02 ⇒ **200** men.

(c) P(X > 73.5) = P(Z > 2) = 1 − Φ(2) ≈ 0.02 ⇒ **200** men.

**Example (CYP 3 Q1): Weights of 500 students, X ~ N(151, 15²).**
(i) P(120 < X < 155) = Φ(0.27) − Φ(−2.07) = Φ(0.27) − (1 − Φ(2.07)) = 0.6064 − 1 + 0.9808 = **0.5872**.
(ii) P(X > 155) = 1 − Φ(0.27) = 1 − 0.6064 = **0.3936**.

**Example (CYP 3 Q2): Mean = 50; 5% of values > 60. Find σ.**
P(X > 60) = 0.05 ⇒ z = 1.64 corresponds to area 0.95 to the left. So 1.64 = (60 − 50)/σ ⇒ **σ = 10/1.64 ≈ 6.10**.

### ⚠️ Common Mistakes
- ❌ Mistake: Looking up Φ(−z) directly when most tables tabulate only positive z → ✅ Correct: Use Φ(−z) = 1 − Φ(z).
- ❌ Mistake: Confusing the *area to the left* (Φ(z)) with the *area to the right* (1 − Φ(z)) when reading "P(X > a)" — careful with the inequality direction.
- ❌ Mistake: Using Φ(z) for a continuous variable as though P(X = c) > 0 → ✅ Correct: Always P(X = c) = 0; P(X ≤ c) = P(X < c).

### Edge Cases & Caveats
- The maximum ordinate of N(μ, σ²) is 1/(σ√(2π)) — *not* 1; densities can exceed 1 if σ is small.
- The two tails *never* touch zero, but density beyond ±3σ is negligible for practical purposes.

> **Quick Recall:**
> - **Z = (X − μ)/σ ~ N(0, 1)** (standardisation)
> - φ(z) = (1/√(2π)) e^(−z²/2)
> - Φ(−z) = 1 − Φ(z) (symmetry)
> - 95% within ±1.96σ; 99% within ±2.58σ; 99.73% within ±3σ
> - z_(0.05) = 1.645, z_(0.025) = 1.96, z_(0.01) = 2.33

### Connections
- Builds on: [Normal Distribution] (this chunk).
- Builds on: [Linear transformation rules] (Chunk 005, MGF section).
- Pre-requisite for: All hypothesis testing and confidence intervals based on normal/large-sample theory.

### Open Questions
1. How large does n need to be for the Central Limit Theorem to make a sample mean approximately normal?
2. When is the t-distribution used instead of standard normal? (Outside this block — covered in inference units.)


---


## Section: Unit 27 Summary 🟢

### Core Idea
Unit 27 closes Block 8 by tying together the **joint and marginal distribution** machinery from Chunks 005–006 with the **three workhorse distributions** — **Binomial, Poisson, Normal** — covered in Chunks 006–007. Two are discrete (Binomial, Poisson); one is continuous (Normal). All three are characterised completely by their moments — which is why moments and MGFs were developed first.

> **In Simple Terms:** This is the unit that takes you from "what is a probability distribution?" to "here are the three distributions you'll meet in 95% of statistics problems."

### Definitions (Unit 27 Key Words — verbatim ⭐)

- **Binomial Distribution**: A discrete probability distribution satisfying:
  1) Finite repetition of identical trials.
  2) Each trial has two outcomes: success or failure.
  3) Trials are independent.
  4) Probability of outcomes does not change between trials.

- **Normal Distribution**: A continuous probability distribution with:
  1) Symmetry about the mean.
  2) Mean = Mode = Median.
  3) Variable can take any value in (−∞, ∞).

- **Poisson Distribution**: A discrete probability distribution that is the **limiting form of the binomial**, provided:
  1) Number of trials → ∞.
  2) Probability of success in each trial → 0.

- **Probability Distribution**: A statement specifying the set of possible values together with the respective probabilities.

> **Quick Recall:**
> - Binomial: discrete, finite n, fixed p
> - Poisson: discrete, single λ, limit of binomial when n→∞ p→0 with np = λ constant
> - Normal: continuous, two parameters (μ, σ), symmetric

---

## Section: Check Your Progress Solutions 🟡

### Examples

**CYP 1, Q1: Joint p.d.f. f(x, y) on x > 0, y > 0, 3x + y < 3 (else 0). Find marginals.**

Marginal of X:
g(x) = f_X(x) = ∫₀^(3−3x) 1 dy = 3 − 3x = **3(1 − x)** for 0 ≤ x ≤ 1.
[Source gives f_X(x) = 2 − (3/2)x + 2x² (different f form); we follow source's algebra.]

Marginal of Y per source: f_Y(y) = 1/3 + (1/6)y − (5/18) y², y > 0.

**CYP 1, Q2: Joint f(x, y) = (2/3)(x + 2y) on 0 ≤ x, y ≤ 1.**
Marginal of X:
g(x) = ∫₀¹ (2/3)(x + 2y) dy = (2/3)[xy + y²]₀¹ = (2/3)(x + 1) = (1/3)(2x + 2) for 0 ≤ x ≤ 1.

(Find h(y) similarly.)

**CYP 2, Q1: Bin distribution with mean = 4 and σ² = 8/3. Find n, p.**
- np = 4, npq = 8/3 ⇒ q = (8/3)/4 = 2/3 ⇒ p = 1/3.
- n = 4/p = **12**.

**CYP 2, Q3: Pass rate 60%, group of 6, P(at least 4 passed)?**
P = ⁶C₄(0.6)⁴(0.4)² + ⁶C₅(0.6)⁵(0.4) + ⁶C₆(0.6)⁶ = **1701/3125**.

**CYP 2, Q4: Die thrown 10 times. Even appears 5 times has twice the prob of 4 times. P(even appears 0 times)?**

f(x) = ¹⁰C_x · p^x · q^(10−x). Given f(5) = 2 · f(4):
¹⁰C₅ · p⁵ · q⁵ = 2 · ¹⁰C₄ · p⁴ · q⁶ ⇒ (252/210) · (p/q) = 2 ⇒ p/q = (210·2)/252 = 5/3 ⇒ p = 5/8, q = 3/8.
f(0) = (3/8)¹⁰ = **(3/8)¹⁰**.

**CYP 2, Q5: 10% defective, sample of 10. Use Poisson approx for P(exactly 3 defectives), e = 2.72.**
λ = np = 10 × 0.1 = 1.
f(3) = e^(−1) · 1³ / 3! ≈ (0.368)/6 ≈ **0.061**.

**CYP 2, Q6: 2% defective, sample of 100. P(3 or more defectives)?**
λ = np = 2.
P(X ≥ 3) = 1 − [f(0) + f(1) + f(2)] = 1 − e^(−2)[1 + 2 + 2] = 1 − 5e^(−2) ≈ 1 − 5·0.135 = **0.325**.

**CYP 2, Q7: P(7 of 10 recover from disease), p = 0.8.**
b(7; 10, 0.8) = ¹⁰C₇ · (0.8)⁷ · (0.2)³ ≈ **0.20**.

**CYP 3, Q1: Weights X ~ N(151, 15²), 500 students.**
(i) P(120 ≤ X ≤ 155): z₁ = (120 − 151)/15 = −2.07, z₂ = (155 − 151)/15 = 0.27.
P = Φ(0.27) − Φ(−2.07) = 0.6064 − (1 − 0.9808) = 0.6064 − 0.0192 = **0.5872**.
Number of students: 500 × 0.5872 = ~294.
(ii) P(X > 155) = 1 − Φ(0.27) = **0.3936**. Number: 500 × 0.3936 ≈ 197.

**CYP 3, Q2: Mean = 50, P(X > 60) = 5%. Find σ.**
z = (60 − 50)/σ = 10/σ. Given P(Z > z) = 0.05 ⇒ z = 1.64 ⇒ σ = 10/1.64 = **6.10**.

> **Quick Recall:**
> - Match question to the right distribution:
>   * "n trials, fixed p, count successes" → Binomial
>   * "rare events per unit time/area" → Poisson (or Poisson approx if n large, p small)
>   * "continuous, symmetric" → Normal
> - Always sketch the standard-normal density and shade the area you want.

---

## Section: Block 8 Final Exercises — Worked Templates 🔴

### Examples

**Q1: Binomial distribution of getting a six in three tosses of a die.**
n = 3; p = 1/6 (six); q = 5/6.

| X | P(X) |
|---|------|
| 0 | ³C₀(1/6)⁰(5/6)³ = 125/216 |
| 1 | ³C₁(1/6)¹(5/6)² = 75/216 = 25/72 |
| 2 | ³C₂(1/6)²(5/6)¹ = 15/216 = 5/72 |
| 3 | ³C₃(1/6)³(5/6)⁰ = 1/216 |

(Sum: 125/216 + 75/216 + 15/216 + 1/216 = 216/216 = 1 ✓)

**Q2: 10 good + 4 fused bulbs; draw 3 with replacement; distribution of X = number of fused?**
p = P(fused) = 4/14 = 2/7; q = 5/7. n = 3.

| X | P(X) |
|---|------|
| 0 | ³C₀(2/7)⁰(5/7)³ = 125/343 |
| 1 | ³C₁(2/7)¹(5/7)² = 150/343 |
| 2 | ³C₂(2/7)²(5/7)¹ = 60/343 |
| 3 | ³C₃(2/7)³(5/7)⁰ = 8/343 |

**Q3: Poisson — 33 policies/week (the source uses μ = 3 in calculations; we follow source).**
(a) **P(some policies sold)** = P(X ≥ 1) = 1 − P(X = 0) = 1 − e^(−3) ≈ 1 − 0.0498 = **0.9502**.
(b) **P(2 ≤ X < 5)** = f(2) + f(3) + f(4)
= e^(−3)·(9/2) + e^(−3)·(27/6) + e^(−3)·(81/24)
= e^(−3)·[4.5 + 4.5 + 3.375] ≈ 0.0498 × 12.375 ≈ **0.61611**.
(c) **P(1 policy on a given day)** with 5 working days/week ⇒ daily rate = 3/5 = 0.6.
P(X = 1) = e^(−0.6) · 0.6 ≈ 0.549 × 0.6 = **0.32929**.

**Q4: Battery time X ~ N(50, 15²). P(50 < X < 70)?**
- z₁ = (50 − 50)/15 = 0.
- z₂ = (70 − 50)/15 ≈ 1.33.
P = Φ(1.33) − Φ(0) = 0.9082 − 0.5 = **0.4082**.

**Q5: Car speeds X ~ N(90, 10²). P(X > 100)?**
z = (100 − 90)/10 = 1.
P(Z > 1) = 1 − Φ(1) = 1 − 0.8413 = **0.1587**.

> **Quick Recall:**
> - Binomial — list each P(X = x) and check Σ = 1.
> - Poisson with rate per unit time/space — scale λ to the requested interval.
> - Normal — always (i) standardise to z, (ii) sketch, (iii) use Φ table.

### ⚠️ Common Mistakes
- ❌ Mistake: Applying binomial to draws *without* replacement → ✅ Correct: Replacement makes trials independent (binomial OK); without replacement requires hypergeometric.
- ❌ Mistake: Forgetting that Poisson rate scales with the size of the observation window → ✅ Correct: λ_new = (rate per unit) × (number of units).
- ❌ Mistake: Using Φ(z) for "more than" → ✅ Correct: P(X > a) = 1 − Φ(z); Φ(z) is left-tail.

### Connections
- Closes Block 8.
- Builds on: [Binomial, Poisson, Normal] (Chunks 006–007) and the [moment/expectation framework] (Chunks 002–005).
- Looks ahead to (outside Block 8): Hypothesis testing, confidence intervals, sampling distributions.

### Open Questions
1. When in practice does the binomial differ enough from the normal that the normal approximation should *not* be used?
2. How can the Poisson approximation to binomial fail when np becomes too large?


---

