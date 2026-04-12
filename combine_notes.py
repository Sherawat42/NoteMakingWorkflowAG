import argparse
import os
import re
from pathlib import Path


def build_chunk_title_map(notes_dir):
    """
    Build a map of {chunk_num: [section_titles]} from all chunk_*_notes.md files.
    Used to resolve bare chunk-number references to human-readable section names.
    """
    chunk_map = {}
    notes_path = Path(notes_dir)

    for notes_file in sorted(notes_path.glob("chunk_*_notes.md")):
        match = re.search(r"chunk_(\d+)_notes\.md", notes_file.name)
        if not match:
            continue
        chunk_num = int(match.group(1))
        sections = []
        with open(notes_file, "r", encoding="utf-8") as f:
            for line in f:
                # Match "## Section: Title 🔴" (emoji optional)
                m = re.match(r"^## Section:\s*(.+?)[\s\U0001F534\U0001F7E1\U0001F7E2]*$", line.strip())
                if m:
                    title = m.group(1).strip()
                    # Strip any trailing emoji/whitespace
                    title = re.sub(r"[\s\U0001F534\U0001F7E1\U0001F7E2]+$", "", title).strip()
                    if title:
                        sections.append(title)
        chunk_map[chunk_num] = sections

    return chunk_map


def resolve_chunk_references(content, chunk_map):
    """
    Replace bare "(Chunk NNN)" references in the combined output with
    "(Chunk NNN: First Section Title)" so cross-references are human-readable.

    Only upgrades references that don't already have a title annotation.
    Leaves file references like chunk_001.txt untouched.
    """

    def replace_paren_ref(match):
        raw_num = match.group(1)
        chunk_num = int(raw_num)
        if chunk_num in chunk_map and chunk_map[chunk_num]:
            title = chunk_map[chunk_num][0]
            return f"(Chunk {chunk_num:03d}: {title})"
        return match.group(0)

    # Replace "(Chunk NNN)" patterns that don't already have a colon after the number
    content = re.sub(r"\(Chunk (\d+)\)(?!:)", replace_paren_ref, content)

    return content


def combine_notes(output_dir, units_config):
    notes_dir = os.path.join(output_dir, "notes")
    unit_name = os.path.basename(os.path.normpath(output_dir))
    export_dir = os.path.join(output_dir, "export", unit_name)
    os.makedirs(export_dir, exist_ok=True)

    complete_path = os.path.join(export_dir, "Complete_Notes.md")
    revision_path = os.path.join(export_dir, "Last_Minute_Revision_Notes.md")

    if not units_config:
        units_config = [("All Units", 1, 100)]

    # Build chunk→section map for reference resolution
    chunk_title_map = build_chunk_title_map(notes_dir)

    final_content = ["# Complete Notes\n\n"]
    exam_content = [
        "# Last Minute Revision Notes\n\n"
        "> *This document contains ONLY ultra-high-yield definitions (⭐), "
        "Quick Recall facts, Common Mistakes, and core bullet points.*\n\n"
    ]

    for unit_name, start, end in units_config:
        unit_added = False

        for i in range(start, end + 1):
            chunk_file = os.path.join(notes_dir, f"chunk_{i:03d}_notes.md")
            if not os.path.exists(chunk_file):
                continue

            with open(chunk_file, "r", encoding="utf-8") as f:
                lines = f.readlines()

            # Full notes concatenation (strip chunk header lines)
            clean_lines = []
            for line in lines:
                if (
                    line.startswith("# Chunk ")
                    or line.startswith("<!-- Pages:")
                    or line.startswith("<!-- Source:")
                ):
                    continue
                clean_lines.append(line)
            final_content.extend(clean_lines)
            final_content.append("\n\n---\n\n")

            # Revision notes parsing
            in_high_yield_section = False
            in_quick_recall = False
            in_common_mistakes = False
            in_table = False
            chunk_additions = []

            for idx, line in enumerate(lines):
                line_str = line.strip()

                if line_str.startswith("## Section:"):
                    if "🔴" in line_str:
                        in_high_yield_section = True
                        chunk_additions.append(
                            f"\n### {line_str.replace('## Section:', '').strip()}\n"
                        )
                    else:
                        in_high_yield_section = False
                    in_quick_recall = False
                    in_common_mistakes = False
                    in_table = False
                    continue

                if line_str.startswith("> **Quick Recall"):
                    in_quick_recall = True
                    chunk_additions.append("\n**Quick Recall:**\n")
                    continue

                if ("Common Mistakes" in line_str or "⚠️" in line_str) and line_str.startswith("###"):
                    in_common_mistakes = True
                    chunk_additions.append(f"\n{line_str}\n")
                    continue

                if line_str.startswith("|"):
                    if "-|-" in line_str or "--|" in line_str:
                        if idx > 0 and lines[idx - 1].strip().startswith("|"):
                            prev = lines[idx - 1]
                            if prev not in chunk_additions and (prev + "\n") not in chunk_additions:
                                chunk_additions.append(prev)
                        chunk_additions.append(line)
                        in_table = True
                        continue
                    elif in_table:
                        chunk_additions.append(line)
                        continue
                elif in_table:
                    in_table = False

                if "⭐" in line_str and not line_str.startswith("#"):
                    if not line_str.startswith("-"):
                        chunk_additions.append(f"- {line_str}\n")
                    else:
                        chunk_additions.append(line)
                    continue

                if in_quick_recall:
                    if line_str == "" or not line_str.startswith(">"):
                        in_quick_recall = False
                    else:
                        clean_line = line_str.lstrip(">").strip()
                        if clean_line:
                            chunk_additions.append(f"{clean_line}\n")
                    continue

                if in_common_mistakes:
                    if line_str.startswith("#"):
                        in_common_mistakes = False
                    elif line_str != "":
                        chunk_additions.append(line)
                    continue

                if in_high_yield_section:
                    if line_str.startswith("- ") or line_str.startswith("* ") or (
                        len(line_str) > 2 and line_str[0].isdigit() and line_str[1:3] in [". ", ") "]
                    ):
                        chunk_additions.append(line)
                    elif line_str.startswith("####"):
                        title = line_str.lstrip("#").strip()
                        chunk_additions.append(f"\n**{title}**\n")

            if chunk_additions:
                if not unit_added:
                    exam_content.append(f"\n## {unit_name}\n\n")
                    unit_added = True
                exam_content.extend(chunk_additions)

    # Resolve cross-chunk references in the complete notes
    complete_text = "".join(final_content)
    complete_text = resolve_chunk_references(complete_text, chunk_title_map)

    with open(complete_path, "w", encoding="utf-8") as f:
        f.write(complete_text)
    with open(revision_path, "w", encoding="utf-8") as f:
        f.writelines(exam_content)

    print(f"Generated {complete_path}")
    print(f"Generated {revision_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine notes into export files.")
    parser.add_argument(
        "output_dir",
        help="Path to the PDF output directory (e.g. output/Subject/Book)",
    )
    args = parser.parse_args()

    generic_config = [("Topics", 1, 100)]
    combine_notes(args.output_dir, generic_config)
