# Chunk 003 — Unit 6 Wrap-up, Data Collection Methods & Tools, Sampling Design Intro, Non-Random Sampling
<!-- Pages: 22-31 -->
<!-- Source: chunk_003.txt -->
<!-- Continues from: Section: Form of Mixed Methods Research Designs (Chunk 002) -->
<!-- Continues into: Section: Random or Probability Sampling (Chunk 004) -->

## Section: Forms of Mixed Methods Designs (Unit 6 Conclusion) 🔴
<!-- See Chunk 002 for detailed treatment of all 4 forms -->

### Core Idea
The four forms of mixed methods designs — (i) quan-QUAL, (ii) QUAL-quan, (iii) qual-QUANT, (iv) QUANT-qual — are connected by sequencing and prioritisation. These form the basis of the "Let Us Sum Up" of Unit 6 and the transition into Unit 7 on Data Collection.

---

## Section: Methods of Data Collection 🔴

### Core Idea
Quantitative research requires the systematic measurement of variables. The quality of data directly determines the validity of research conclusions. There are three broad methods of data collection: the Census and Survey Method, the Observation Method, and the Experimental Method.

> **In Simple Terms:** Collecting good data is like cooking with fresh ingredients — if your inputs are bad, even the most sophisticated recipe (analysis) will produce poor results. The three methods are just different ways of gathering those ingredients.

### Key Concepts

#### Census and Survey Method
Involves a carefully planned study to collect data from the subject units. Two approaches:
- **Complete enumeration (Census)**: Data collected from *all* units in the population. Example: Census of Population (2011) — collected demographic, economic, social, and cultural data for all persons in India.
- **Sample Survey**: Data collected from a *suitably selected part* (sample) of the population. Example: National Sample Survey Organisation (NSSO) household surveys on socio-economic characteristics.

#### Observation Method
Records data as things occur, using an appropriate measurement method. Examples:
- Recording a patient's body temperature every hour
- Daily recording of maximum/minimum temperatures at a location
- Recording rainfall during monsoon seasons

#### Experimental Method
Collects data through well-designed, controlled statistical experiments to isolate the effect of one variable on another. Example: Determining the optimal rate of manure application for maximum crop yield — all other variables (water, soil quality, seeds, insecticides) are controlled so only manure varies. Related branches: *Design and Analysis of Experiments* and *Analysis of Variance*.

| Method | Key Feature | Example |
|--------|-------------|---------|
| Census & Survey | Planned study; complete or partial coverage | Population Census, NSSO surveys |
| Observation | Records as events occur | Temperature recording, patient vitals |
| Experimental | Controlled experiment to isolate one variable | Manure-yield experiment |

### Definitions
- **Census**: Complete enumeration — data collected from all units in the population. ⭐ (exam-important)
- **Sample Survey**: Data collected from a selected part (sample) of the population.
- **Respondent units / Informants**: Units from which data are collected in a survey.

> **Quick Recall:**
> - 3 methods: Census/Survey, Observation, Experimental
> - Census = all units; Sample survey = selected units
> - Observation = as-it-happens recording; Experimental = controlled variable testing

---

## Section: Tools of Data Collection 🔴

### Core Idea
Data collection tools translate research requirements into a collection format. The two primary tools are the **questionnaire** and the **schedule**. Modern technology has expanded the range of data collection modalities. Data can be primary (collected fresh) or secondary (already collected by others).

> **In Simple Terms:** Just as a doctor uses different instruments (stethoscope, thermometer, or MRI) depending on what they need to measure, a researcher uses different tools (questionnaire, schedule, electronic device) depending on the research design.

### Key Concepts

#### Questionnaire
- A set of pre-specified questions answered directly by respondents, without investigator guidance on interpretation.
- Assumes the respondent can understand and answer questions independently.
- Respondent-bias minimised by keeping questions simple and direct.
- Responses often in the form of "yes/no/can't say" or graded (good/satisfactory/unsatisfactory).

#### Schedule
- Detailed questions where the investigator (not the respondent) reads and explains the questions.
- The investigator's training and instructions guide elicitation of reliable information.
- Intensive investigator training is required to avoid investigator-bias.

| Feature | Questionnaire | Schedule |
|---------|--------------|---------|
| Who fills it | Respondent | Investigator |
| Complexity | Simple, direct | Detailed, explained |
| Bias risk | Respondent-bias | Investigator-bias (if poorly trained) |
| Use case | Literate, self-sufficient sample | General population, complex concepts |

#### Data Collection Modes
- Personal contact with respondents
- Telephone interviews
- E-mail / internet ("chatting")
- Mail method (postal questionnaire with reply envelope)
- SMS / social media

#### Mechanical / Electronic Devices
- Time-recording machines for factory workers
- Electronic Data Transfer (EDT) — e.g., customs houses supplying trade data to DGCI&S

#### Primary vs. Secondary Data
- **Primary data**: Collected afresh by the research agency for the specific study.
- **Secondary data**: Data already collected by another agency; available in publications, compact discs, or websites. Must be carefully evaluated for suitability before use.

#### Errors in Data
- **Sampling errors**: Arise from confining data collection to a sample instead of the whole population.
- **Non-sampling errors**: Arise from faulty measurement, unclear definitions, inaccurate measurement, investigator bias, non-response, or omissions.
- **Total survey error** = Sampling errors + Non-sampling errors; must be minimised for data quality.

### Definitions
- **Questionnaire**: A pre-specified set of questions answered by respondents independently.
- **Schedule**: A data collection format where the investigator elicits answers through guided questioning.
- **Primary Data**: Data collected fresh by the conducting agency for the specific enquiry. ⭐ (exam-important)
- **Secondary Data**: Data previously collected by another agency. ⭐ (exam-important)
- **Sampling Error**: Error arising from using a sample instead of the full population.
- **Non-sampling Error**: Error from faulty measurement, bias, non-response, or omissions.

> **Quick Recall:**
> - Questionnaire = respondent fills; Schedule = investigator elicits
> - Primary = collected fresh; Secondary = published/existing data from other agencies
> - Total survey error = sampling error + non-sampling error

---

## Section: Sampling Design — Population and Sample Aggregates and Inference 🔴

### Core Idea
Sampling design is about how to select a sample from a population. Before choosing a method, key statistical terminology must be clear: the distinction between *parameter* (population characteristic) and *statistic* (sample characteristic), and the process of *inference* — using sample statistics to estimate population parameters.

> **In Simple Terms:** A population is the entire group you want to study (e.g., all students in a university), and a sample is the group you actually measure. A parameter is a fact about the whole population (which you often don't know), and a statistic is the corresponding fact from your sample (which you compute). Inference is the process of using the known sample statistic to estimate the unknown population parameter.

### Key Concepts

#### Population and Sample Notation
- Population: N units, denoted U_i (i = 1 to N); variable value = Y_i; **upper case** = population
- Sample: n units, denoted u_i (i = 1 to n); variable value = y_i; **lower case** = sample

#### Key Formulae
| Parameter | Formula | Notes |
|-----------|---------|-------|
| Population total | Y = ΣY_i | Sum over all N units |
| Population mean | M = (1/N)ΣY_i | ⭐ |
| Population variance | σ² = (1/N)ΣY_i² – M² | |
| Sample mean | m = (1/n)Σy_i | ⭐ |
| Sample variance | s² = (1/n)Σy_i² – m² | |
| Population proportion | P = N₁/N | N₁ = units with specified characteristic |
| Sample proportion | p | Fraction in sample with characteristic |

#### Process of Inference
1. Draw a sample from the population
2. Compute the **estimator** (a sample statistic that estimates a parameter). Example: sample mean *m* estimates population mean *µ*
3. The computed value for a specific sample is the **estimate**
4. The difference between the estimate and the true parameter = **sampling error** (assuming no non-sampling errors)
5. Different samples → different estimates → a *distribution* of estimates

### Definitions
- **Parameter**: Any function of population values Y_i (e.g., population mean M). ⭐ (exam-important)
- **Statistic**: Any function of sample observations y_i (e.g., sample mean m). ⭐ (exam-important)
- **Estimator (Point Estimator)**: A sample statistic used to estimate a population parameter. ⭐ (exam-important)
- **Estimate (Point Estimate)**: The value of the estimator computed from a specific sample. ⭐ (exam-important)
- **Inference**: The process of drawing conclusions about a population from sample results. ⭐ (exam-important)
- **Sampling Error**: Error in using a sample estimate in place of the true population parameter.

> **Quick Recall:**
> - Population → parameter (UPPER CASE); Sample → statistic (lower case)
> - m (sample mean) = estimator of M (population mean)
> - Inference = using sample to learn about population
> - Sampling error = m – M (for a given sample)

---

## Section: Non-Random Sampling 🟡

### Core Idea
Non-random (non-probability) sampling methods select units without giving each population unit a pre-specified known chance of selection. This makes the relationship between sample and parent population unclear and introduces subjective bias. Despite this, non-random sampling has useful applications in exploratory and preliminary research.

> **In Simple Terms:** Non-random sampling is like picking fruit by hand — you tend to pick the ones that look best (or are easiest to reach), not necessarily a true cross-section. Random sampling is like using a machine to pick at fixed intervals from all parts of the orchard.

### Key Concepts

#### Types of Non-Random Sampling

| Type | Description | Use Case |
|------|-------------|---------|
| **Judgment Sampling** | Expert selects units based on knowledge of population | Auditor selects transactions to examine |
| **Convenience Sampling** | Selecting units easiest to reach | People leaving a cinema; mall shoppers |
| **Purposive Sampling** | Group specially picked for a specific purpose | Similar to judgment sampling; preliminary research |
| **Quota Sampling** | Strata identified; convenience/judgment sample selected from each | Ensures sub-group representation, but without randomness |
| **Heterogeneity Sampling** | Units chosen to include all opinions or views | Capturing diverse perspectives |
| **Snowball Sampling** | Initial respondents refer additional respondents; used for rare characteristics | Tracing rare genetic trait; invisible/vulnerable social groups |

#### Limitations
- Relationship between sample and parent population is *unclear*
- Selection seems subjective and discretionary → reflects researcher/investigator bias
- Not helpful in drawing **valid conclusions** about the parent population
- Non-random samples are **not representative** samples

#### Uses (despite limitations)
- **Inexpensive and quick** preliminary insight into a variable under study
- Useful for designing a more rigorous scientific enquiry later
- Valuable in **exploratory research**

### Definitions
- **Representative Sample**: A sample that contains the relevant characteristics of the population *in the same proportion* as in the population. ⭐ (exam-important)
- **Snowball Sampling**: Using referrals from initial respondents to identify additional respondents; used for rare characteristics or invisible/vulnerable groups.

> **Quick Recall:**
> - 6 types: Judgment, Convenience, Purposive, Quota, Heterogeneity, Snowball
> - Non-random ≠ representative → cannot draw valid population-level conclusions
> - But useful: exploratory, preliminary, cheap, quick

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking quota sampling is the same as stratified random sampling → ✅ Correct: In quota sampling, within-stratum selection is non-random (convenience/judgment); in stratified sampling, within-stratum selection is random.

---

## Section: Random or Probability Sampling (Introduction) 🔴
<!-- Continues in Chunk 004 -->

### Core Idea
Random sampling is defined as a method in which each unit in the population has a **predetermined probability (chance)** of being included in the sample. This property is the foundation of valid inference — it allows us to estimate population parameters and quantify the *precision* (standard error) of those estimates. A **sampling design** is a complete specification of all possible samples of a given type with their corresponding probabilities.

> **In Simple Terms:** Random sampling is like a lottery where every ticket has a known chance of being drawn. This known probability is what makes it possible to mathematically determine how reliable your conclusions are — something impossible with hand-picking.

### Definitions
- **Random Sampling**: A method of sampling in which each unit in the population has a predetermined, known probability of inclusion in the sample. ⭐ (exam-important)
- **Sampling Design**: A specification of all possible samples of a given type with their corresponding probabilities. ⭐ (exam-important)
- **Precision of an Estimate**: The degree to which the estimate is free from sampling error; measured by the standard error. ⭐ (exam-important)

### Connections
- Builds on: Non-Random Sampling (this chunk) — by contrasting random vs. non-random
- Continues into: Chunk 004 — Standard Errors, Confidence Intervals, SRSWR, SRSWOR
