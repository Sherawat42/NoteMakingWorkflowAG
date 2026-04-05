---
name: critique-pass
description: >
  Critique and refine the completed notes for accuracy, completeness, and clarity.
  Use when the user asks to "critique the notes", "review the notes", "improve the notes",
  "run pass 3", "run the critique pass", or after the content pass has completed.
---

# Critique Pass — Review & Refine Notes (Pass 3)

This skill applies a **systematic critique framework** to each notes file, identifies 
gaps and issues, and produces improved final notes. The critic acts as a demanding 
expert reviewer who pushes for excellence.

This is the **fourth and final step** in the PDF-to-Notes pipeline.

## Prerequisites

- Content Pass (`03-content-pass`) has been completed
- All `chunk_*_notes.md` files exist in `<working_dir>/notes/`
- All source `.txt` files exist in `<working_dir>/chunks/`

## Instructions

### Step 1: Load and Verify

1. Read `<working_dir>/index.json`
2. Read `<working_dir>/notes/content_index.md` for an overview
3. Verify all `chunk_*_notes.md` files exist

### Step 2: Critique Each Chunk (Sequential)

For each chunk `i` (from 1 to total_chunks), do the following:

#### 2a. Load Required Files

| File | Purpose |
|------|---------|
| `chunks/chunk_{i}.txt` | Source text — the ground truth |
| `notes/chunk_{i}_notes.md` | Current notes — what to critique |
| `notes/chunk_{i-1}_final.md` | Previous chunk's final notes — for continuity (if i > 1) |

#### 2b. Apply the Critique Framework

Evaluate the notes against **six dimensions**. For each dimension, assign a rating 
and provide specific, actionable feedback.

##### Dimension 1: Accuracy (Critical)

**Question**: Does every claim in the notes faithfully represent the source text?

- Compare notes against source text line by line
- Flag any statement that is NOT supported by the source
- Flag any subtle misrepresentations or oversimplifications
- Check that definitions match the source precisely
- Check that examples are reproduced correctly

**Rating**: ✅ Accurate | ⚠️ Minor Issues | ❌ Inaccurate

##### Dimension 2: Completeness

**Question**: Does the notes capture ALL important information from the source?

- Check for key concepts that were mentioned in the source but missing from notes
- Check for definitions that were skipped
- Check for examples that were not included
- Check for edge cases or caveats that were overlooked
- Check for any processes/mechanisms that were simplified too much

**Rating**: ✅ Complete | ⚠️ Gaps Found | ❌ Major Omissions

##### Dimension 3: Clarity

**Question**: Would a reader understand this topic WITHOUT the original PDF?

- Check for jargon used without explanation
- Check for logical flow — does the explanation build naturally?
- Check for ambiguous sentences
- Check for assumptions about prior knowledge that should be made explicit
- Could a smart person who hasn't read the source learn from these notes alone?

**Rating**: ✅ Clear | ⚠️ Could Improve | ❌ Confusing

##### Dimension 4: Depth

**Question**: Is this deeper than a summary? Does it capture nuance?

- Check that explanations go beyond surface level
- Check that "why" questions are addressed, not just "what"
- Check that mechanisms are explained, not just named
- Check that edge cases show understanding of boundaries
- Would an expert find these notes useful, or too shallow?

**Rating**: ✅ Deep | ⚠️ Surface Level in Parts | ❌ Too Shallow

##### Dimension 5: Structure

**Question**: Is the organization logical and the template followed consistently?

- Check that section titles are descriptive and specific
- Check that the hierarchy makes sense
- Check that cross-references are formatted consistently
- Check that the template sections are all present
- Check for any content that seems misplaced

**Rating**: ✅ Well Structured | ⚠️ Minor Issues | ❌ Poorly Organized

##### Dimension 6: Connections

**Question**: Are cross-references meaningful, correct, and comprehensive?

- Check that connections reference real sections that exist
- Check that the described relationship type is accurate
- Check for missing connections that should be obvious
- Check continuity markers (continues from/into) are correct

**Rating**: ✅ Well Connected | ⚠️ Missing Links | ❌ Disconnected

##### Dimension 7: Student-Friendliness

**Question**: Could a student study from these notes alone and understand the topic?

- Check that every section has an "In Simple Terms" blockquote with a plain-language explanation
- Check that comparison tables are used (not just prose) when contrasting concepts
- Check that causal chains use arrow notation (→) for visual clarity
- Check that examples include worked-through calculations, not just formulas
- Check that language is accessible — no unexplained jargon
- Check that Quick Recall boxes exist and contain scannable, memorable facts
- Would a student at 2 AM find these notes easy to study from?

**Rating**: ✅ Student-Friendly | ⚠️ Needs Simplification | ❌ Too Academic

##### Dimension 8: Exam Readiness

**Question**: Are exam-important topics clearly marked and easy to find?

- Check that EVERY `## Section` heading has an exam importance marker (🔴/🟡/🟢)
- Check that the markers are appropriately assigned (topics with CYP questions should be 🔴)
- Check that key definitions are marked with ⭐ (exam-important)
- Check that Common Mistakes sections exist for tricky/confusing topics
- Check that a student could filter to only 🔴 sections and have a solid exam prep set

**Rating**: ✅ Exam-Ready | ⚠️ Missing Markers | ❌ Not Exam-Oriented

#### 2c. Generate the Critique Report

Create a critique report at `<working_dir>/notes/chunk_{NNN}_critique.md`:

```markdown
# Critique Report — Chunk [NNN]

## Overall Assessment
[1-2 sentence summary of quality]

## Dimension Ratings

| Dimension | Rating | Summary |
|-----------|--------|---------|
| Accuracy | [rating] | [1-sentence summary] |
| Completeness | [rating] | [1-sentence summary] |
| Clarity | [rating] | [1-sentence summary] |
| Depth | [rating] | [1-sentence summary] |
| Structure | [rating] | [1-sentence summary] |
| Connections | [rating] | [1-sentence summary] |
| Student-Friendliness | [rating] | [1-sentence summary] |
| Exam Readiness | [rating] | [1-sentence summary] |

## Specific Issues

### Accuracy Issues
- [ ] [Issue 1]: [description + fix]
- [ ] [Issue 2]: [description + fix]

### Completeness Gaps
- [ ] Missing: [concept/term/example] — found on page [X]
- [ ] Missing: [concept/term/example] — found on page [X]

### Clarity Improvements
- [ ] [Section]: [suggestion]

### Depth Improvements
- [ ] [Section]: [what additional depth to add]

### Structure Fixes
- [ ] [Issue + fix]

### Missing Connections
- [ ] Should link [Section A] to [Section B] because [reason]

### Student-Friendliness Issues
- [ ] Missing "In Simple Terms" in [Section]
- [ ] [Section]: Needs comparison table instead of prose
- [ ] [Section]: Missing Quick Recall box

### Exam Readiness Issues
- [ ] Missing exam marker on [Section heading]
- [ ] [Term] should be marked ⭐ (exam-important)
- [ ] [Section] is 🔴 topic but missing Common Mistakes

## Expert Additions

What would a domain expert add to these notes?
- [Suggestion 1]
- [Suggestion 2]
```

#### 2d. Apply Improvements

Now, take the original notes and apply ALL the improvements identified in the critique:

1. Fix every accuracy issue
2. Add every missing concept, term, or example
3. Clarify every ambiguous section
4. Deepen every shallow explanation
5. Fix structural issues
6. Add missing connections
7. Incorporate expert additions where appropriate

**Rules for improvements:**
- Only add content that is supported by the source text
- Do NOT invent information to address "depth" concerns — deepen using what's in the source
- When adding connections, verify the referenced sections actually exist
- Maintain the same template structure
- Ensure every section has exam markers, In Simple Terms, and Quick Recall
- Add Common Mistakes sections for 🔴 topics that lack them

#### 2e. Save the Final Notes

Save to: `<working_dir>/notes/chunk_{NNN}_final.md`

The final notes should:
- Include a header comment noting it was refined: `<!-- Refined by critique pass -->`
- Incorporate all improvements seamlessly (not as patches)
- Read as polished, final notes — not as notes + corrections

### Step 3: Create the Final Master Index

After ALL chunks are processed, create `<working_dir>/notes/final_index.md`:

```markdown
# Final Notes — Master Index

**Source**: [PDF filename]
**Total Pages**: [N]
**Total Chunks**: [M]
**Pipeline Completed**: [timestamp]

## Table of Contents

### Part/Chapter: [Title]

1. [Section Title](chunk_001_final.md) — Pages 1-3
   - Key Topics: [list]
2. [Section Title](chunk_002_final.md) — Pages 4-6
   - Key Topics: [list]
...

## Quality Summary

| Chunk | Accuracy | Completeness | Clarity | Depth | Structure | Connections | Student-Friendly | Exam-Ready |
|-------|----------|-------------|---------|-------|-----------|-------------|-----------------|------------|
| 001 | ✅ | ✅ | ⚠️→✅ | ✅ | ✅ | ✅ | ✅ | 🟢 |
| 002 | ✅ | ⚠️→✅ | ✅ | ✅ | ✅ | ⚠️→✅ | ✅ | 🟢 |
...

## Complete Glossary

| Term | Definition | Source |
|------|-----------|--------|
| [Term] | [Definition] | Chunk NNN, Page X |
...

## Knowledge Map

How all sections connect:

[Use a text-based or list-based representation showing relationships]

## Reading Order

Recommended order for studying these notes:
1. [Section] — foundational concepts
2. [Section] — builds on #1
...
```

### Step 3.5: Generate Export Files

Create a dedicated export folder for student-facing output files:

```bash
mkdir -p <working_dir>/export
```

Generate the following files inside `<working_dir>/export/`:

#### 3.5a. Consolidated Final Notes

Create `<working_dir>/export/FINAL_NOTES.md` — a single, self-contained document
that merges all chunk final notes into one readable file, organized by unit/chapter.

This file should:
- Include the PDF source name in the header
- Organize content by unit/chapter (not by chunk)
- Include a table of contents at the top
- Retain all exam importance markers (🔴/🟡/🟢) on section headings
- Retain all "In Simple Terms" blockquotes, Quick Recall boxes, and Common Mistakes
- Include key equations summary table and a glossary at the end
- Be readable without any other file — fully standalone
- A student should be able to use ONLY this file to study for an exam

#### 3.5b. Exam Prep Notes

If the source is a textbook, also create `<working_dir>/export/EXAM_PREP.md` — a
condensed quick-reference version with:
- **Only 🔴 HIGH YIELD topics** — skip 🟡 and 🟢 content
- All ⭐ exam-important definitions in a single glossary table
- All key formulae/equations in a reference table
- All comparison tables (e.g., Classical vs Keynesian, Fixed vs Flexible)
- All Common Mistakes sections consolidated
- All Quick Recall boxes consolidated
- Likely exam question types with answer strategies
- This should be a **≤20% the size** of FINAL_NOTES.md — maximum density

> **IMPORTANT**: All export files MUST be created inside `<working_dir>/export/`
> (i.e. inside the per-PDF output folder). NEVER write export files to the
> project root, `notes/`, or any shared location. This ensures that outputs from
> different PDFs are always isolated from each other.

### Step 4: Report to User

```
✅ Critique Pass Complete — Pipeline Finished!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Chunks reviewed:    [N]
Issues found:       [M]
Issues fixed:       [M]
Final notes:        <working_dir>/notes/chunk_*_final.md
Critique reports:   <working_dir>/notes/chunk_*_critique.md
Master index:       <working_dir>/notes/final_index.md
Export folder:      <working_dir>/export/
  ├── FINAL_NOTES.md       (consolidated, student-ready)
  └── EXAM_PREP.md         (quick reference, if applicable)

Your notes are ready! Start with export/FINAL_NOTES.md for the
full consolidated notes, or final_index.md for the detailed index.
```

## Critique Mindset

When critiquing, adopt these personas:

1. **The Perfectionist**: Nothing is ever good enough. Find every flaw.
2. **The Student**: Would I actually understand this? Is anything confusing? Would I know what to study for the exam?
3. **The Expert**: Is anything oversimplified? What nuance is missing?
4. **The Editor**: Is the writing crisp? Is the structure clean? Are the visual cues (🔴/⭐/→) used consistently?
5. **The Exam Coach**: Are the right topics marked as high-yield? Would a student studying only 🔴 sections pass the exam? Are Common Mistakes actionable?

The goal is to produce notes that are **better than what most humans would create** 
by applying systematic, multi-lens review. A student should be able to pick up
these notes and feel confident about their exam preparation.

## Error Handling

- If a notes file is severely deficient, don't try to patch it — rewrite the affected sections from scratch using the source text
- If the source text is ambiguous, note the ambiguity explicitly rather than guessing
- If connections reference chunks that don't exist, remove them and add a warning comment
