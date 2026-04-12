---
description: Convert a PDF book into structured, exam-ready Markdown notes
---

# PDF-to-Notes Agent Instructions

You are an agent tasked with converting a PDF textbook into high-quality, structured
Markdown notes. Follow every step in this file exactly. This is your single source of
truth — you do not need to read any other file to complete this task.

---

## Before You Begin

### Inputs required
You need only the full path to the PDF file. If it wasn't provided, ask for it.

Derive everything else from the path:
- **Book name** — the PDF filename without its extension
- **Subject** — the name of the folder that contains the PDF

Example: `/Users/manish/Books/Indian Economics/Block-1 205.pdf`
→ subject = `Indian Economics`, book name = `Block-1 205`

### Working directory
All outputs for this PDF live under one isolated folder:
```
output/<subject>/<book-name>/
```
Create it now. Never write outside this folder — this prevents outputs from different
PDFs from mixing.

### Progress file
Copy `PROGRESS_TEMPLATE.md` from the project root to:
```
output/<subject>/<book-name>/PROGRESS.md
```
Fill in the header: PDF name, path, subject, working directory, start timestamp.
You will keep this file updated throughout — check off each item as you complete it.

---

## Step 1: Split the PDF

### Run the split script

```bash
# Recommended — snaps boundaries to section headings (UNIT N, Chapter N, 1.1 ...)
python skills/01-split-pdf/scripts/split_pdf.py "<pdf_path>" "output/<subject>/<book-name>" --smart-split

# Fallback — fixed-size chunks if smart-split produces odd results
python skills/01-split-pdf/scripts/split_pdf.py "<pdf_path>" "output/<subject>/<book-name>"
```

Default chunk size is **10 pages**. Use `--chunk-size N` to override.

### Verify output
1. `index.json` exists and is valid JSON
2. `total_chunks` in the JSON matches the number of files in `chunks/`
3. Page ranges are contiguous (no gaps)
4. Spot-check one `.txt` file — it should contain readable text

If a `.txt` file is empty: the PDF page may be scanned/image-based. Note it in PROGRESS.md
and continue — the agent will work with whatever text is available.

### Update PROGRESS.md
Fill in: total pages, chunk count, smart-split used (yes/no).
Check off all Stage 1 items.

---

## Step 2: Structure Pass (optional for short documents)

> **Decision rule**: If the document has **fewer than ~60 pages** (roughly 6 chunks),
> skip this entire step — go directly to Step 3. The content pass handles structure inline.
> Mark all Stage 2 items in PROGRESS.md as `N/A — skipped (short document)`.

For longer documents, create a structure outline for each chunk before filling content.
This lets you review the scaffolding before investing in content generation.

### Setup
```bash
mkdir -p output/<subject>/<book-name>/notes
```

Maintain a running **section tracker** (in memory) to avoid duplicate names and track continuity.

### Process each chunk — sliding window

For chunk `i` of `total_chunks`:

**Load:**
- `chunks/chunk_{i-1}.txt` — backward context (skip if i = 1)
- `chunks/chunk_{i}.txt` — current chunk (always)
- `chunks/chunk_{i+1}.txt` — forward context (skip if i = last)

**Analyze:**
- What sections/topics does this chunk cover?
- Does a section continue from the previous chunk?
- Does a section start here and continue into the next chunk?
- What are the key terms and concepts?

**Write `notes/chunk_{NNN}_structure.md`:**

```markdown
# Chunk [NNN] — [Descriptive Title]
<!-- Pages: [start]-[end] -->
<!-- Continues from: [section title or N/A] -->
<!-- Continues into: [section title or N/A] -->

## Section: [Title] [🔴|🟡|🟢]
<!-- Exam importance: 🔴 HIGH YIELD / 🟡 MODERATE / 🟢 CONTEXT -->
<!-- Reason: [e.g. "has Check Your Progress questions", "named theorem", "background only"] -->

### Core Idea
<!-- placeholder -->

### In Simple Terms
<!-- placeholder -->

### Key Concepts
#### [Concept Name]
<!-- placeholder -->

### Definitions
- **[Term]**: <!-- placeholder -->

### Mechanisms / Processes
<!-- placeholder -->

### Examples
<!-- placeholder -->

### Common Mistakes
<!-- placeholder -->

### Edge Cases & Caveats
<!-- placeholder -->

### Quick Recall
<!-- placeholder -->

### Connections
<!-- placeholder -->

### Open Questions
<!-- placeholder -->
```

Rules:
- A chunk may have multiple `## Section:` blocks — one per topic
- Mark continuity: `continues from chunk NNN` / `continues into chunk NNN`
- Titles must be specific — use actual terminology, not "Topic 1"
- Include all key terms even if unsure of importance

**Update PROGRESS.md**: check off the chunk's structure item.

### After all chunks: create `notes/structure_index.md`

```markdown
# Structure Index
**Source**: [filename] | **Chunks**: [N] | **Created**: [timestamp]

## Table of Contents
### Chunk 001 — [Title] (Pages X–Y)
- [Section name] — [key concepts listed] — [N] definitions

## Section Flow
| Section | Starts | Ends | Chunks spanned |
|---------|--------|------|----------------|
| [Name]  | 001    | 003  | 3              |
```

Check off Stage 2 completion in PROGRESS.md.

---

## Step 3: Content Pass

Fill each chunk's structure outline with substantive content. This is the core of the
pipeline — deep knowledge extraction, not summarization.

### Setup: running context file

The running context tracks what has been introduced across all previous chunks. It gives
every chunk awareness of the whole document — preventing repeated definitions and enabling
accurate cross-references.

**At the start of Step 3:** check if `notes/running_context.md` exists and read it.
If not, it will be created after the first chunk.

Format:
```markdown
# Running Context

## Key Concepts Introduced
- **[Concept]** (Chunk NNN): [one-line description]

## Definitions (⭐ exam-important)
- **[Term]** (Chunk NNN): [definition]

## Named Models / Laws / Theories
- **[Name]** (Chunk NNN): [brief description]

## Key Data & Numbers
- [figure or statistic] (Chunk NNN): [context]
```

Keep each entry to one line. This file should stay under ~3 KB for a typical 100-page book.

### Process each chunk — sequential with context

For chunk `i` of `total_chunks`:

**Load (in this order):**

| File | Purpose |
|------|---------|
| `notes/running_context.md` | All facts from prior chunks — load if exists |
| `notes/chunk_{i-1}_notes.md` | Previous chunk's completed notes — continuity |
| `chunks/chunk_{i}.txt` | Current chunk source text — ground truth |
| `notes/chunk_{i}_structure.md` | Structure to fill — if it exists |

If no structure file exists (short document path): identify sections from the source
text directly, then write the fully-filled notes without an intermediate structure file.

---

#### Content rules for each section

##### `## Section: [Title] 🔴/🟡/🟢`
Every section heading must have an exam importance tag:

| Tag | Use when |
|-----|----------|
| 🔴 HIGH YIELD | Core theories, named laws/models, derivations, Check Your Progress topics, unit objectives |
| 🟡 MODERATE | Supporting concepts, secondary mechanisms, elaborations |
| 🟢 CONTEXT | Historical background, introductions, administrative content |

##### Core Idea
2–4 sentences. Must stand alone. Rephrase — do not copy-paste from source.

##### In Simple Terms
Blockquote. Plain language, everyday analogy, 1–3 sentences.
```
> **In Simple Terms:** [explanation]
```

##### Key Concepts
One paragraph per concept (3–6 sentences): what it is, why it matters, how it relates.
Use **comparison tables** whenever two concepts are contrasted.

##### Definitions
Precise definitions from the source text.
Mark exam-critical ones: `⭐ (exam-important)`

##### Mechanisms / Processes
Numbered steps. Arrow notation for causal chains: `A → B → C → D`

##### Examples
Reproduce from source. Include worked-through calculations — show every step.

##### Quick Recall
End each major section with a blockquote:
```
> **Quick Recall:**
> - [key fact]
> - [key formula]
> - [must-know point]
```

##### Common Mistakes
If students commonly err on this topic:
```
### ⚠️ Common Mistakes
- ❌ Mistake: [wrong idea] → ✅ Correct: [right understanding]
```

##### Connections
Reference other sections by name and chunk: `[Section Name] (Chunk NNN)`
State relationship type: "builds on", "contrasts with", "is prerequisite for"

##### Continuity
- When a section carries over from previous chunk: don't repeat prior content;
  start with a transition; add `<!-- See chunk NNN for start of this section -->`
- When a section continues into next chunk: add `<!-- Continues in chunk NNN -->`

---

#### Save `notes/chunk_{NNN}_notes.md`

```markdown
# Chunk [NNN] — [Title]
<!-- Pages: [start]-[end] -->
<!-- Source: chunk_NNN.txt -->

## Section: [Title] 🔴

### Core Idea
[2–4 sentences]

> **In Simple Terms:** [analogy-based explanation]

### Key Concepts

#### [Concept]
[Detailed paragraph]

| Aspect | Concept A | Concept B |
|--------|-----------|-----------|
| [row]  | [value]   | [value]   |

### Definitions
- **[Term]**: [definition]. ⭐ (exam-important)

### Mechanisms / Processes
1. [Step] → [Step] → [Step]

### Examples
**Example: [title]**
[Worked calculation]

### ⚠️ Common Mistakes
- ❌ Mistake: [wrong] → ✅ Correct: [right]

### Edge Cases & Caveats
- [caveat]

> **Quick Recall:**
> - [fact]
> - [formula]

### Connections
- Builds on: [Section Name] (Chunk NNN)

### Open Questions
1. [question]
```

#### Update running context
After saving the notes file, append to `notes/running_context.md`:
- New key concepts (not already listed)
- New ⭐ definitions (not already listed)
- New named models/laws/theories
- New key data points

One line per entry. Skip entries already in the file.

#### Inline self-review (do this before moving to next chunk)
1. **Source check**: Pick 3 claims in your notes. Find each in `chunk_{NNN}.txt`. Remove anything not in the source.
2. **Repetition check**: Scan previous chunk's notes. Remove any verbatim-copied sentences.
3. **Marker check**: Verify each ⭐ definition and each 🔴 section is genuinely justified by the source text signals listed above.

Fix any failures before proceeding to the next chunk.

**Update PROGRESS.md**: check off the chunk's notes item.

---

### After all chunks: create `notes/content_index.md`

```markdown
# Content Index
**Source**: [filename] | **Chunks**: [N] | **Completed**: [timestamp]

## Notes Files
| Chunk | Title | Pages | Top Sections | Key Terms |
|-------|-------|-------|--------------|-----------|
| 001   | [Title] | 1–10 | [sections]  | [terms]   |

## Cross-References
| From | To | Relationship |
|------|----|-------------|
| [Section] (Chunk N) | [Section] (Chunk M) | builds on |

## Key Terms Glossary
| Term | Definition | First Appears |
|------|-----------|---------------|
| [term] | [def] | Chunk NNN |
```

Check off Stage 3 completion in PROGRESS.md.

---

## Step 4: Combine Notes

Run the combine script to produce the final student-facing deliverables:

```bash
python combine_notes.py "output/<subject>/<book-name>"
```

This produces two files in `output/<subject>/<book-name>/export/<book-name>/`:

| File | Contents |
|------|----------|
| `Complete_Notes.md` | Full consolidated notes; cross-chunk references resolved to section titles |
| `Last_Minute_Revision_Notes.md` | Only 🔴 sections, ⭐ definitions, Quick Recall, Common Mistakes |

Verify both files exist and are non-empty. Check off Stage 4 in PROGRESS.md.

---

## Completion

Update PROGRESS.md:
- Check off the final completion item
- Fill in the completed timestamp
- Fill in the export path

Report to the user:
```
✅ Pipeline Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PDF:        [filename]
Pages:      [N] → [M] chunks
Notes:      output/<subject>/<book-name>/notes/
Export:     output/<subject>/<book-name>/export/<book-name>/
Progress:   output/<subject>/<book-name>/PROGRESS.md
```

---

## Quality Standards

- **Faithful**: Every claim must come from the source `.txt` file. No hallucination.
- **Comprehensive**: Capture all key concepts, not just the obvious ones.
- **Precise**: Use exact terminology from the source.
- **Deep**: This is knowledge extraction, not summarization.
- **Student-friendly**: A student should understand the topic without needing the original PDF.
- **Scannable**: Short sentences, bullet points, tables, arrow chains. Tired-student-at-2AM readability.

---

## Output Directory Reference

```
output/<subject>/<book-name>/
├── PROGRESS.md                     ← per-run progress tracking
├── index.json                      ← chunk manifest
├── input/<book-name>.pdf           ← source PDF copy
├── chunks/
│   ├── chunk_001.pdf + chunk_001.txt
│   └── ...
├── notes/
│   ├── running_context.md          ← accumulated facts (updated per chunk)
│   ├── chunk_001_structure.md      ← outline (if structure pass was run)
│   ├── chunk_001_notes.md          ← filled notes
│   ├── structure_index.md          ← TOC (if structure pass was run)
│   └── content_index.md            ← cross-refs + glossary
└── export/<book-name>/
    ├── Complete_Notes.md
    └── Last_Minute_Revision_Notes.md
```
