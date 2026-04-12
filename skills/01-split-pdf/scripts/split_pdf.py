#!/usr/bin/env python3
"""
split_pdf.py — Split a PDF into page chunks with text extraction.

Usage:
    python split_pdf.py <input_pdf> <output_dir> [--chunk-size 10] [--smart-split]

Outputs:
    - chunk_001.pdf, chunk_002.pdf, ... in <output_dir>/chunks/
    - chunk_001.txt, chunk_002.txt, ... (extracted text) in <output_dir>/chunks/
    - index.json in <output_dir>/

Dependencies:
    pip install pypdf
"""

import argparse
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    print("ERROR: 'pypdf' is not installed. Run: pip install pypdf", file=sys.stderr)
    sys.exit(1)


# Patterns that indicate the start of a major section in academic texts.
# Checked against the first 500 characters of a page.
_HEADING_PATTERNS = [
    re.compile(r'^\s*(UNIT|CHAPTER|SECTION)\s+\d+', re.IGNORECASE | re.MULTILINE),
    re.compile(r'^\s*\d+\.\d+\s+[A-Z]', re.MULTILINE),
    re.compile(r'^\s*\d+\.\s+[A-Z][A-Z\s]{3,30}\s*$', re.MULTILINE),
]


def _is_section_start(text: str) -> bool:
    """Return True if the page text begins a recognisable section heading."""
    sample = text[:500]
    return any(p.search(sample) for p in _HEADING_PATTERNS)


def _find_smart_boundary(reader: PdfReader, planned_end: int, total_pages: int, window: int = 2) -> int:
    """
    Given a planned chunk end page (0-indexed, inclusive), search within
    ±window pages for a natural section boundary.

    A boundary is natural when the *next* page starts a section heading.
    Returns the adjusted end page (0-indexed, inclusive).
    Falls back to planned_end if no heading is found.
    """
    search_start = max(0, planned_end - window)
    search_end = min(total_pages - 2, planned_end + window)  # -2: we look at page+1

    best_end = None
    best_dist = window + 1

    for candidate_end in range(search_start, search_end + 1):
        next_idx = candidate_end + 1
        if next_idx < total_pages:
            page_text = reader.pages[next_idx].extract_text() or ""
            if _is_section_start(page_text):
                dist = abs(candidate_end - planned_end)
                if dist < best_dist:
                    best_dist = dist
                    best_end = candidate_end

    return best_end if best_end is not None else planned_end


def extract_text_from_pages(reader: PdfReader, start_page: int, end_page: int) -> str:
    """Extract text from a range of pages (0-indexed, inclusive)."""
    parts = []
    for page_num in range(start_page, end_page + 1):
        page_text = reader.pages[page_num].extract_text() or ""
        parts.append(f"--- Page {page_num + 1} ---\n{page_text}")
    return "\n\n".join(parts)


def split_pdf(input_pdf: str, output_dir: str, chunk_size: int = 10, smart_split: bool = False) -> dict:
    """
    Split a PDF into chunks of ~chunk_size pages each.

    Args:
        input_pdf:   Path to the source PDF file.
        output_dir:  Directory to write chunks and index.
        chunk_size:  Target pages per chunk (default: 10).
        smart_split: If True, snap boundaries to detected section headings (±2 pages).

    Returns:
        The index dictionary describing all chunks.
    """
    input_path = Path(input_pdf).resolve()
    output_path = Path(output_dir).resolve()

    if not input_path.exists():
        print(f"ERROR: Input PDF not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    chunks_dir = output_path / "chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)

    input_dir = output_path / "input"
    input_dir.mkdir(parents=True, exist_ok=True)

    copied_pdf_path = input_dir / input_path.name
    if not copied_pdf_path.exists() or input_path != copied_pdf_path:
        shutil.copy2(input_path, copied_pdf_path)

    reader = PdfReader(str(copied_pdf_path))
    total_pages = len(reader.pages)

    if total_pages == 0:
        print("ERROR: PDF has no pages.", file=sys.stderr)
        sys.exit(1)

    print(f"Source:      {input_path.name}")
    print(f"Total pages: {total_pages}")
    print(f"Chunk size:  {chunk_size} pages (target)")
    print(f"Smart split: {'enabled' if smart_split else 'disabled'}")
    print("-" * 50)

    # Build list of (start_page, end_page) — 0-indexed, inclusive
    boundaries: list[tuple[int, int]] = []
    if smart_split:
        start = 0
        while start < total_pages:
            planned_end = min(start + chunk_size - 1, total_pages - 1)
            if planned_end < total_pages - 1:
                end = _find_smart_boundary(reader, planned_end, total_pages, window=2)
            else:
                end = planned_end
            boundaries.append((start, end))
            start = end + 1
    else:
        total_chunks = (total_pages + chunk_size - 1) // chunk_size
        for i in range(total_chunks):
            start = i * chunk_size
            end = min(start + chunk_size - 1, total_pages - 1)
            boundaries.append((start, end))

    chunks_info = []

    for chunk_idx, (start_page, end_page) in enumerate(boundaries):
        pages_in_chunk = end_page - start_page + 1
        chunk_num = chunk_idx + 1
        chunk_filename = f"chunk_{chunk_num:03d}.pdf"
        text_filename = f"chunk_{chunk_num:03d}.txt"

        writer = PdfWriter()
        for page_num in range(start_page, end_page + 1):
            writer.add_page(reader.pages[page_num])

        chunk_pdf_path = chunks_dir / chunk_filename
        with open(chunk_pdf_path, "wb") as f:
            writer.write(f)

        text_content = extract_text_from_pages(reader, start_page, end_page)
        chunk_text_path = chunks_dir / text_filename
        with open(chunk_text_path, "w", encoding="utf-8") as f:
            f.write(text_content)

        chunk_info = {
            "chunk_id": chunk_num,
            "filename": chunk_filename,
            "text_filename": text_filename,
            "page_range": [start_page + 1, end_page + 1],  # 1-indexed for humans
            "pages": pages_in_chunk,
        }
        chunks_info.append(chunk_info)
        print(f"  ✓ Chunk {chunk_num:03d}: pages {start_page + 1}–{end_page + 1} ({pages_in_chunk} pages)")

    total_chunks = len(chunks_info)

    index = {
        "source_pdf": str(copied_pdf_path),
        "source_filename": input_path.name,
        "total_pages": total_pages,
        "chunk_size": chunk_size,
        "smart_split": smart_split,
        "total_chunks": total_chunks,
        "chunks_directory": str(chunks_dir),
        "chunks": chunks_info,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    index_path = output_path / "index.json"
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

    print("-" * 50)
    print(f"  ✓ Index written: {index_path}")
    print(f"\nDone! {total_chunks} chunks created in {chunks_dir}")

    return index


def main():
    parser = argparse.ArgumentParser(
        description="Split a PDF into page chunks with text extraction.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python split_pdf.py book.pdf ./output
    python split_pdf.py book.pdf ./output --chunk-size 10
    python split_pdf.py book.pdf ./output --chunk-size 10 --smart-split
        """,
    )
    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument("output_dir", help="Directory to write chunks and index.json")
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=10,
        help="Target pages per chunk (default: 10)",
    )
    parser.add_argument(
        "--smart-split",
        action="store_true",
        help="Snap chunk boundaries to detected section headings (±2 pages)",
    )

    args = parser.parse_args()

    if args.chunk_size < 1:
        print("ERROR: Chunk size must be at least 1.", file=sys.stderr)
        sys.exit(1)

    split_pdf(args.input_pdf, args.output_dir, args.chunk_size, args.smart_split)


if __name__ == "__main__":
    main()
