# PDF-to-Notes — Agentic Knowledge Pipeline

A multi-skill pipeline that converts PDF books into high-quality, structured, iteratively refined Markdown notes. Designed for use with **Antigravity**, **Gemini**, **Claude**, and any other AI agent.

## 🧠 What This Does

This is **NOT simple summarization**. It's a structured, multi-pass knowledge extraction pipeline:

1. **Split** — Breaks a PDF into ~10-page chunks with text extraction
2. **Structure** — Creates detailed outlines using a sliding context window (optional for short docs)
3. **Content** — Fills outlines with comprehensive, precise content; maintains a running context file across all chunks
4. **Combine** — Merges chunk notes into `Complete_Notes.md` and `Last_Minute_Revision_Notes.md`

Each pass builds on the previous one, producing incrementally better output.

## 📋 Prerequisites

- **Python 3.8+**
- **pypdf** library:
  ```bash
  pip install -r requirements.txt
  ```

## 🚀 Quick Start

> **See [`START_HERE.md`](START_HERE.md) for the exact prompt to give your agent.**
> That file is for human operators only — do not feed it to the agent as context.

### Running the Pipeline

Point your agent at the workflow file and it handles everything:

```
Read `.agents/workflows/pdf-to-notes.md` and follow the instructions to convert
[PDF PATH] into structured notes. Subject: [SUBJECT]. Book name: [BOOK NAME].
```

The workflow file at `.agents/workflows/pdf-to-notes.md` is the single source of truth —
it contains all instructions the agent needs, end to end.

### Running a Single Pass Manually

If you need to re-run just one stage, direct the agent to the relevant step in the workflow file. Example:

```
Read `.agents/workflows/pdf-to-notes.md` — specifically Step 3 (Content Pass).
Re-run it for `output/your-subject/your-book-name/`, starting from chunk 005.
```

Or run the split/combine scripts directly:

```bash
# Split a PDF
python skills/01-split-pdf/scripts/split_pdf.py "/path/to/book.pdf" "output/Subject/BookName" --smart-split

# Combine chunk notes into final exports
python combine_notes.py "output/Subject/BookName"
```

## 📁 Directory Structure

```
NoteMakingWorkflowAG/
├── START_HERE.md                          # ★ Human operator guide — NOT for agents
├── README.md                              # This file
├── PROGRESS_TEMPLATE.md                   # Copied per-PDF run; agent tracks progress here
├── requirements.txt                       # Python dependencies
├── combine_notes.py                       # Combine chunk notes into final exports
├── .agents/
│   └── workflows/
│       └── pdf-to-notes.md                # ★ Agent's single instruction file (all steps)
├── skills/
│   ├── 01-split-pdf/
│   │   ├── SKILL.md                       # Reference: Split PDF
│   │   └── scripts/
│   │       └── split_pdf.py               # Python splitting script
│   ├── 02-structure-pass/
│   │   └── SKILL.md                       # Reference: Create outlines
│   └── 03-content-pass/
│       └── SKILL.md                       # Reference: Fill content
└── output/                                # Generated output (one folder per PDF)
    └── <subject>/
        └── <book-name>/
            ├── PROGRESS.md                    # Copied from template; updated per stage
            ├── index.json                     # Chunk manifest
            ├── input/<book-name>.pdf          # Source PDF copy
            ├── chunks/                        # chunk_NNN.pdf + chunk_NNN.txt
            ├── notes/
            │   ├── running_context.md         # Accumulated facts across all chunks
            │   ├── chunk_NNN_structure.md     # Pass 1: Outlines (optional)
            │   ├── chunk_NNN_notes.md         # Pass 2: Filled content
            │   ├── structure_index.md
            │   └── content_index.md
            └── export/<book-name>/
                ├── Complete_Notes.md
                └── Last_Minute_Revision_Notes.md
```

## 🔑 Key Design Decisions

### Single workflow file
`.agents/workflows/pdf-to-notes.md` is the agent's complete instruction set — all four
stages are described inline. The agent reads nothing else to complete the task. SKILL.md
files exist as modular reference docs but are not required reading during a run.

### Running context across chunks
After each chunk's content pass, the agent appends newly introduced concepts, definitions,
and named models to `running_context.md`. Every subsequent chunk loads this file, giving
it awareness of everything introduced earlier — preventing repeated definitions and enabling
accurate cross-references without blowing up the context window.

### Smart splitting
The split script's `--smart-split` flag detects section headings and snaps chunk boundaries
to them (±2 pages), eliminating artificial mid-section cuts that the sliding window would
otherwise have to paper over.

### Structure pass is optional
For documents under ~60 pages, the content pass generates structure inline, cutting the
total number of agent passes in half.

### Text extraction at split time
The split script writes `.txt` files alongside PDF chunks. Any agent (Claude, Gemini, etc.)
can read plain text without needing PDF parsing at processing time.

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
