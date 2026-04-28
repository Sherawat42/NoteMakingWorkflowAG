# Chunk 001 — Sampling Theory: Foundations, Sample Design, Biases
<!-- Pages: 1-10 -->
<!-- Source: chunk_001.txt -->

## Section: Block 9 Overview — Inferential Statistics 🟢

### Core Idea
Block 9 of MEC203 covers inferential statistics — the framework for drawing conclusions about a population from a sample. It is organised as four units: **Unit 28 — Sampling Theory**, **Unit 29 — Sampling Distributions**, **Unit 30 — Estimation**, and **Unit 31 — Hypothesis Testing**. Each unit builds on the previous one: sampling provides the data, sampling distributions model the variability of statistics, estimation produces best guesses for population parameters, and hypothesis testing decides whether sample evidence supports a claim about a parameter.

> **In Simple Terms:** Inferential statistics is like drawing conclusions about a whole pot of soup after tasting just one spoonful. Block 9 teaches you how to take that spoonful properly (sampling), describe what tastes are likely to vary (distributions), make your best guess about the whole pot (estimation), and decide if the cook is wrong about how salty the soup is (hypothesis testing).

---

## Section: Unit 28 — Introduction to Sampling 🟢

### Core Idea
Sampling theory begins by distinguishing the *population* (the whole group of objects under study) from the *sample* (a finite subset chosen from it). Because complete enumeration is generally impractical, statisticians estimate population numerical characteristics (parameters) using sample numerical characteristics (statistics). Drawing inferences from samples introduces sampling error, but careful design can keep both sampling and non-sampling errors low.

> **In Simple Terms:** A "population" doesn't have to mean people — it's whatever group you want to study (light bulbs, divorces, pineapples). A "sample" is the small piece you actually look at. The trick is making the sample look like a miniature version of the whole population.

### Key Concepts

#### Population (Universe)
The group of individuals (animate or inanimate) under statistical study. Can be **finite** (e.g., all earning individuals in India) or **infinite** (e.g., all possible coin tosses). The population is described by *parameters* such as the mean μ or variance σ².

#### Sample
A finite subset of the population. The number of individuals in it is the **sample size** *n*. A sample is *representative* when its composition mirrors the heterogeneity of the population — for instance, if the population is 30% male / 70% female, a representative sample should reflect roughly the same proportions.

#### Census vs. Sample Survey
| Aspect | Census | Sample Survey |
|---|---|---|
| Coverage | Every population unit (size N) | Subset of size n (n ≪ N) |
| Sampling error | None | Inherent and unavoidable |
| Non-sampling error | Likely (time/cost pressure) | Minimised (smaller scope, better questionnaire/staff) |
| Cost & time | Very high | Lower |
| Quality of data | Often weaker (rushed) | Often better (deeper interviews) |
| Standard error | Not produced | Produced — gives precision bounds |

#### Parameter vs. Statistic
- **Parameter**: numerical characteristic of the population (μ, σ²). Generally unknown.
- **Statistic**: numerical characteristic of the sample (x̄, s²). Function of sample observations only.
- The statistic is used as an estimate of the parameter.

### Definitions
- **Population**: aggregate of objects, animate or inanimate, under study; may be finite or infinite. ⭐ (exam-important)
- **Sample**: a finite subset of statistical individuals in a population. ⭐ (exam-important)
- **Sample size (n)**: the number of individuals in a sample.
- **Parameter**: a numerical characteristic of the population (e.g., μ, σ²). ⭐ (exam-important)
- **Statistic**: a numerical characteristic computed from sample observations only (e.g., x̄, s²); R. A. Fisher's terminology. ⭐ (exam-important)
- **Sampling error**: the random error inherent in any sampling scheme; arises because the sample is only a subset of the population.
- **Non-sampling error**: errors arising from interview, recording, missing information, etc.; can occur even in a census.

> **Quick Recall:**
> - μ, σ² → parameters (population, usually unknown)
> - x̄, s² → statistics (sample, calculated)
> - Census = no sampling error but has non-sampling error
> - Sample survey = has sampling error but generally lower non-sampling error

---

## Section: Advantages of Sample Survey 🟡

### Core Idea
A sample survey is preferred over complete enumeration because it lowers cost, allows deeper interaction with respondents, raises data quality, and yields a measurable error (standard error) that lets us state probable bounds on the population parameter.

### Key Concepts

#### Four Advantages
1. **Reduction of Cost** — fewer staff, less time → lower cost than census.
2. **Better Scope for Information** — surveyors can spend more time per household, eliciting deeper information than a rushed census.
3. **Better Quality of Data** — focused questionnaire aligned with study objectives produces better data than a time-pressed census.
4. **Gives an Idea of the Error** — only a sample yields a standard error, which lets us construct limits within which the true population parameter likely lies.

> **Quick Recall:**
> - 4 advantages: cheap, deeper info, better quality, computable standard error
> - The fourth advantage is unique to sampling — a census produces no SE

---

## Section: Sample Design 🔴

### Core Idea
A *sample design* spells out how the sample is selected from the population. Its central aim is to produce a representative sample so that sampling error is minimised. A simple random sample, where every population unit has equal, known, non-zero probability of selection, is the special case that allows formal probability-based inference. Designing a survey involves trading off **cost** (lower with smaller n) against **efficiency** (higher with larger n, since variance of the estimator falls).

> **In Simple Terms:** Sample design is the recipe for picking who or what to include. A *random* recipe works best because it's the only one that lets you put a probability on what you might find — and probability is what makes statistical conclusions trustworthy.

### Key Concepts

#### Random (Probability) Sampling
Each population unit has a known, equal, non-zero probability of selection. To draw a random sample, the researcher needs a **sampling frame** — a list of all population members. Two key advantages:
- avoids systematic bias;
- allows quantifying the size of the sampling error.

A simple random sample is a special case where the probabilities are equal. Probability sampling is sometimes called *random sampling*. Examples of randomization devices: pseudo-random number generators, dice, lotteries, Tippet's random-numbers tables.

#### Randomization
The process by which a random sample is selected. Randomization removes biases from the human selector but, by chance, may still produce extreme samples (e.g., drawing only men from a mixed-sex population). Such cases are usually addressed by *restricted randomization* — for example, **stratified random sampling by gender**.

#### With Replacement vs. Without Replacement
- For *very large* populations, sample without replacement.
- If sample size is a small proportion of population, sample with replacement is acceptable (and simplifies derivations).

#### Cost vs. Efficiency Trade-off
- Cost rises with sample size *n*.
- Efficiency = 1 / Var(estimator). For the sample mean, Var(x̄) = σ²/n → efficiency rises with n.
- The optimal design balances these opposing forces.

### Definitions
- **Random sample**: a sample in which each population unit has a known, non-zero probability of being selected. ⭐ (exam-important)
- **Sampling frame**: a list of all population members; required for probability sampling.
- **Probability sampling**: sampling techniques in which each unit has a known, non-zero probability of inclusion.
- **Validity**: review that the data answer the questions of interest.
- **Pilot survey**: a small-scale pre-test of the survey method conducted before the main survey.

### Mechanisms / Processes — Stages of a Sample Survey
The text breaks the planning stage into the following sequential steps:

1. **Defining the Objectives** → identify variables, decide data type and analysis technique.
2. **Defining the Population to be Sampled** → establish a sampling frame; resolve borderline cases.
3. **Determination of the Data to be Collected** → align data with objectives; avoid irrelevant or missing items.
4. **Questionnaire / Schedule Design** → questionnaire (filled by respondents) or schedule (filled by investigators).
5. **Method of Collecting Data** → choose between questionnaire and interview methods; manage non-response (which can cause endogeneity if patterned).
6. **Choice of Sampling Units** → align with objectives.
7. **Designing the Survey** → conduct a pilot survey + decide flexible variables.
8. **Organisation of Field Work** → train field staff; supervise to minimise sampling errors.
9. **Drawing the Sample** → e.g., put numbered slips in an urn, mix, draw n.

#### Why a Pilot Survey?
- Improves field-work organisation by exposing defects.
- Improves question framing and questionnaire design.
- Trains field staff on real conditions.
- Surfaces unanticipated problems.
- Provides cost and time estimates for the main survey.

> **Quick Recall:**
> - Sampling frame is a *prerequisite* for probability sampling.
> - Var(x̄) = σ²/n → larger n → better precision but higher cost.
> - Pilot survey = small dry-run before main survey.

---

## Section: Biases in the Survey 🔴

### Core Idea
Bias arises when the sample systematically over- or under-estimates a population parameter. A long taxonomy of biases exists; they are usually grouped into **selection biases** (where the sample fails to mirror the population) and **procedural biases** (response, observational, non-response, interviewer). A particularly important econometric bias — **omitted variable bias (OVB)** — arises when relevant variables are excluded from a regression model. **Crucially, increasing sample size reduces sampling error but cannot fix bias.**

> **In Simple Terms:** Sampling error shrinks when you collect more data. Bias is a *systematic* lean — like a scale that's permanently off by 2 kilos — and adding more weighings won't fix it.

### Key Concepts

#### Selection Bias and Its Sub-types
Selection bias results from an unrepresentative sample. The text lists the following:

| Sub-type | What it is | Typical example |
|---|---|---|
| **Under-coverage** | Some population members inadequately represented | Exit poll; surveys based on telephone directories or car-registration lists |
| **Non-response bias** | Selected individuals refuse / can't participate, and they differ meaningfully from respondents | Mail surveys; "call-in radio" shows on controversial topics over-represent strongly opinionated people |
| **Substitution bias** | Investigator replaces a hard-to-reach unit with a convenient one | Replacing a missing household with a neighbour |
| **Faulty demarcation of sampling units** | Borderline cases at investigator's discretion | Crop-cutting / agricultural field surveys |
| **Self-selection bias** | Subjects pick themselves; less proactive people excluded | Volunteer-only studies |
| **Recall bias** | Respondent forgets or mis-remembers | Survey asking "what did you eat last week?" |
| **Observer bias** | Researcher subconsciously projects expectations | Cherry-picking statistics that support hypothesis |
| **Survivorship bias** | Looking only at "survivors" of a pre-selection process | Reading only published case studies (success stories) |

These all fall under *procedural bias*, which can take the form of:
- Response bias (people respond improperly)
- Observational bias (unrepresentative sample)
- Non-response bias
- Interviewer bias (biased frame of mind)

#### Omitted Variable Bias (OVB)
Occurs in regression analysis when a model leaves out one or more relevant variables that are correlated with both the dependent variable and an included independent variable. The effect of the missing variable is wrongly attributed to the included ones, biasing the estimated parameters.

### Definitions
- **Selection bias**: bias resulting from an unrepresentative sample. ⭐ (exam-important)
- **Non-response bias**: arises when respondents differ in meaningful ways from non-respondents.
- **Survivorship bias**: bias from focusing only on data points that survived a pre-selection process.
- **Omitted Variable Bias (OVB)**: bias in regression estimates due to leaving out a relevant variable correlated with both the dependent and an included independent variable. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: "If I just take a bigger sample, my survey results will be unbiased." → ✅ Correct: Sample size only affects sampling error (variability). It cannot correct survey bias caused by under-coverage, non-response, etc. A large biased sample is still biased.
- ❌ Mistake: Confusing sampling error with bias. → ✅ Correct: Sampling error is random variability between samples; bias is a systematic shift.

> **Quick Recall:**
> - 8 selection-bias subtypes; 4 procedural-bias forms; 1 OVB.
> - Bigger n → smaller sampling error, NOT smaller bias.
> - For an unbiased statistic, the average of all possible sample statistics equals the true parameter.

### Connections
- Sampling error is reduced by larger n; bias is not (key contrast).
- Probability sampling [Section: Sample Design] is the antidote for several biases (it allows the *known* probability of inclusion that bias often violates).
<!-- Continues in chunk 002 -->
