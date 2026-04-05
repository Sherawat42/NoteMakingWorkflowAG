---
description: End-to-end pipeline to convert a PDF book into structured, iteratively refined Markdown notes
---

# PDF-to-Notes Pipeline

This workflow converts a PDF book into high-quality, structured Markdown notes through a 3-step pipeline.

## Prerequisites

- Python 3.8+ installed
- `pypdf` library installed: `pip install pypdf`
- The source PDF file path

## Pipeline Steps

### Step 1: Split the PDF

Split the source PDF into 3-page chunks with text extraction.

```bash
python skills/01-split-pdf/scripts/split_pdf.py "<pdf_path>" "output/<subject>/<book-name>" --chunk-size 3
```

**Verify**: Check that `output/<subject>/<book-name>/index.json` exists and all chunk files are present.

Refer to `skills/01-split-pdf/SKILL.md` for detailed instructions.

---

### Step 2: Structure Pass (Pass 1)

Create a notes outline for each chunk using the sliding context window approach.

For each chunk, load the previous, current, and next chunk text files to create a structure outline.

**Output**: `output/<subject>/<book-name>/notes/chunk_*_structure.md` + `structure_index.md`

Refer to `skills/02-structure-pass/SKILL.md` for detailed instructions.

---

### Step 3: Content Pass (Pass 2)

Fill the outlines with detailed content. For each chunk, load the previous chunk's completed notes and the current chunk's source text.

**Output**: `output/<subject>/<book-name>/notes/chunk_*_notes.md` + `content_index.md`

Refer to `skills/03-content-pass/SKILL.md` for detailed instructions.

---

### Step 4: Combine Notes (Pass 3)

Combine the generated notes into single deliverables.

**Output**: `output/<subject>/<book-name>/export/Complete_Notes.md` + `output/<subject>/<book-name>/export/Last_Minute_Revision_Notes.md`

---

## Final Output Structure

Each PDF gets its own isolated output folder. When processing multiple PDFs,
outputs never mix because everything lives under `output/<subject>/<book-name>/`.

```
output/<subject>/<book-name>/
├── index.json                        # Chunk manifest
├── input/                            # Copied source PDF
│   └── <book-name>.pdf
├── chunks/                           # PDF chunks
│   ├── chunk_001.pdf                 # PDF chunks
│   ├── chunk_001.txt                 # Extracted text
│   └── ...
├── notes/
│   ├── structure_index.md            # Pass 1 index
│   ├── chunk_001_structure.md        # Pass 1 outlines
│   ├── content_index.md              # Pass 2 index
│   └── chunk_001_notes.md            # Pass 2 filled notes
└── export/                           # ★ Student-facing deliverables
    └── <book-name>/
        ├── Complete_Notes.md             # Consolidated notes (standalone)
        └── Last_Minute_Revision_Notes.md # Quick reference cheat sheet
```

### Multi-PDF Example

```
output/
├── Indian Economic Policy/           # Subject 1
│   ├── Block-1 205/                  # First PDF
│   │   ├── index.json
│   │   ├── input/
│   │   ├── chunks/
│   │   ├── notes/
│   │   └── export/
│   │       └── Block-1 205/
│   │           ├── Complete_Notes.md
│   │           └── Last_Minute_Revision_Notes.md
│   └── Block-2 205/                  # Second PDF
│       ├── index.json
│       ├── input/
│       ├── chunks/
│       ├── notes/
│       └── export/
│           └── Block-2 205/
│               ├── Complete_Notes.md
│               └── Last_Minute_Revision_Notes.md
└── MACROECONOMIC_ANALYSIS/           # Subject 2
    ├── Block-1 102/                  # Third PDF
    │   └── ...
```

> **IMPORTANT**: All output files — chunks, notes, and exports — MUST be written
> inside the per-PDF folder (`output/<subject>/<book-name>/`). Never write to the project
> root or any shared location. This rule prevents outputs from different PDFs
> from getting mixed up.

## Tips

- **Run one pass at a time** — review the output of each pass before moving to the next
- **Start small** — try with a short PDF (10-20 pages) first
- **Check the first few structures** before running the full structure pass — adjust if the sections don't look right
- Each pass is designed to be **independently re-runnable** — if pass 2 isn't satisfactory, you can re-run it without re-doing pass 1
