# PDF-to-Notes — Agentic Knowledge Pipeline

A multi-skill pipeline that converts PDF books into high-quality, structured, iteratively refined Markdown notes. Designed for use with **Codex** and **Antigravity** AI agents.

## 🧠 What This Does

This is **NOT simple summarization**. It's a structured, multi-pass knowledge extraction pipeline:

1. **Split** — Breaks a PDF into 3-page chunks with text extraction
2. **Structure** — Creates detailed outlines using a sliding context window
3. **Content** — Fills outlines with comprehensive, precise content

Each pass builds on the previous one, producing incrementally better output.

## 📋 Prerequisites

- **Python 3.8+**
- **pypdf** library:
  ```bash
  pip install pypdf
  ```

## 🚀 Quick Start

### Option A: Using the Workflow (Recommended)

If your agent supports workflows, simply run:

```
/pdf-to-notes
```

The workflow file at `.agents/workflows/pdf-to-notes.md` will guide the agent through all 4 steps.

### Option B: Running Each Pass Manually

#### Pass 0: Split the PDF

```bash
python skills/01-split-pdf/scripts/split_pdf.py "/path/to/your/book.pdf" "output/your-subject/your-book-name" --chunk-size 3
```

This creates:
- `output/your-subject/your-book-name/input/` — Copied original PDF
- `output/your-subject/your-book-name/chunks/` — PDF and TXT files for each 3-page chunk
- `output/your-subject/your-book-name/index.json` — Manifest describing all chunks

**Verify the output:**
```bash
cat output/your-subject/your-book-name/index.json | python -m json.tool
ls output/your-subject/your-book-name/chunks/
```

#### Pass 1: Structure Pass

Tell your agent:
> "Read the skill at `skills/02-structure-pass/SKILL.md` and create the notes structure for the PDF chunks in `output/your-subject/your-book-name/`."

The agent will:
- Process each chunk with a sliding window (prev + current + next)
- Create outline files: `output/your-subject/your-book-name/notes/chunk_*_structure.md`
- Create `structure_index.md`

**Review the structures** before moving to Pass 2. Adjust if section boundaries are wrong.

#### Pass 2: Content Pass

Tell your agent:
> "Read the skill at `skills/03-content-pass/SKILL.md` and fill the notes structures with content for `output/your-subject/your-book-name/`."

The agent will:
- Fill each outline with detailed content
- Use previous completed notes for continuity
- Create `output/your-subject/your-book-name/notes/chunk_*_notes.md`
- Create `content_index.md` with glossary and cross-references

#### Pass 3: Combine Notes

Tell your agent:
> "Combine the notes in `output/your-subject/your-book-name/notes/` into two files in `output/your-subject/your-book-name/export/`: `Complete_Notes.md` and `Last_Minute_Revision_Notes.md`."

The agent will:
- Read all detailed content notes from the chunks
- Generate `Complete_Notes.md` containing the full textbook notes
- Extract only high-yield topics (🔴), quick recall facts, definitions (⭐), and common mistakes to generate a highly condensed `Last_Minute_Revision_Notes.md`

## 📁 Directory Structure

```
NoteMakingWorkflowAG/
├── README.md                              # This file
├── .agents/
│   └── workflows/
│       └── pdf-to-notes.md                # End-to-end workflow
├── skills/
│   ├── 01-split-pdf/
│   │   ├── SKILL.md                       # Skill: Split PDF
│   │   └── scripts/
│   │       └── split_pdf.py               # Python splitting script
│   ├── 02-structure-pass/
│   │   └── SKILL.md                       # Skill: Create outlines
│   └── 03-content-pass/
│       └── SKILL.md                       # Skill: Fill content
└── output/                                # Generated output
    └── <subject-name>/                    # Grouped by subject
        └── <book-name>/
            ├── index.json                     # Chunk manifest
            ├── input/                         # Copied original PDF
            │   └── <book-name>.pdf
            ├── chunks/                        # PDF + TXT chunks
            │   ├── chunk_001.pdf
            │   ├── chunk_001.txt
        │   └── ...
        └── notes/                         # Generated notes
            ├── chunk_001_structure.md     # Pass 1: Outlines
            ├── chunk_001_notes.md         # Pass 2: Content
            ├── structure_index.md         # Pass 1 index
            └── content_index.md           # Pass 2 index
```

## 🔑 Key Design Decisions

### Sliding Context Window
Each chunk is processed with its **previous** and **next** chunk loaded for context. This ensures:
- Section boundaries are detected correctly
- Content that spans chunk boundaries is handled gracefully
- Continuity is maintained across the entire book

### Two-Pass Architecture
- **Pass 1 (Structure)** establishes the scaffold — you can review and adjust before investing in content
- **Pass 2 (Content)** fills with detail — uses completed notes from prior chunks for continuity

### Text Extraction
The split script extracts text to `.txt` files alongside PDF chunks. This means:
- Any agent can read the content (no PDF parsing dependency at processing time)
- Text is available for search and comparison
- Ground truth is preserved in the PDF chunks

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| `pypdf` not found | Run `pip install pypdf` |
| Empty `.txt` files | The PDF may be image-based (scanned). You'll need OCR. |
| Structure seems wrong | Review and edit `chunk_*_structure.md` files before running Pass 2 |
| Agent doesn't find skills | Make sure you're running from the project root directory |
| Content is too shallow | Re-run Pass 2 for specific chunks, or try a more capable model |

## 🔮 Future Enhancements

- **Diagram Processing**: Extract and convert diagrams to Mermaid
- **RAG Index**: Build a searchable index over the generated notes
- **Knowledge Graph**: Auto-link concepts across topics
- **Incremental Updates**: Process only changed/new chunks
