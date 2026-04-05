import argparse
import os

def combine_notes(output_dir, units_config):
    notes_dir = os.path.join(output_dir, "notes")
    unit_name = os.path.basename(os.path.normpath(output_dir))
    export_dir = os.path.join(output_dir, "export", unit_name)
    os.makedirs(export_dir, exist_ok=True)
    
    complete_path = os.path.join(export_dir, "Complete_Notes.md")
    revision_path = os.path.join(export_dir, "Last_Minute_Revision_Notes.md")
    
    # Simple hardcoded fallback if no config given
    if not units_config:
        units_config = [("All Units", 1, 100)]
        
    final_content = ["# Complete Notes\n\n"]
    exam_content = ["# Last Minute Revision Notes\n\n> *This document contains ONLY ultra-high-yield definitions (⭐), Quick Recall facts, Common Mistakes, and core bullet points.*\n\n"]

    for unit_name, start, end in units_config:
        unit_added = False
        
        for i in range(start, end + 1):
            chunk_file = os.path.join(notes_dir, f"chunk_{i:03d}_notes.md")
            if not os.path.exists(chunk_file):
                continue
                
            with open(chunk_file, 'r') as f:
                lines = f.readlines()
                
            # Full notes concatenation
            clean_lines = []
            for line in lines:
                if line.startswith("# Chunk ") or line.startswith("<!-- Pages:") or line.startswith("<!-- Source:"):
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
                        chunk_additions.append(f"\n### {line_str.replace('## Section:', '').strip()}\n")
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
                        if idx > 0 and lines[idx-1].strip().startswith("|"):
                            if lines[idx-1] not in chunk_additions and (lines[idx-1] + "\n") not in chunk_additions:
                                chunk_additions.append(lines[idx-1])
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
                    if line_str.startswith("- ") or line_str.startswith("* ") or (len(line_str) > 2 and line_str[0].isdigit() and line_str[1:3] in [". ", ") "]):
                        chunk_additions.append(line)
                    elif line_str.startswith("####"):
                        title = line_str.lstrip("#").strip()
                        chunk_additions.append(f"\n**{title}**\n")
                        
            if chunk_additions:
                if not unit_added:
                    exam_content.append(f"\n## {unit_name}\n\n")
                    unit_added = True
                exam_content.extend(chunk_additions)

    with open(complete_path, 'w') as f:
        f.writelines(final_content)
    with open(revision_path, 'w') as f:
        f.writelines(exam_content)
        
    print(f"Generated {complete_path}\n Generated {revision_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine notes into export files.")
    parser.add_argument("output_dir", help="Path to the PDF output directory (e.g. output/Subject/Book)")
    args = parser.parse_args()
    
    # We'll just pass a generic block config, but this can be customized
    generic_config = [("Topics", 1, 100)]
    combine_notes(args.output_dir, generic_config)
