#!/usr/bin/env python3
"""Build PDF previews and/or PNG images for flow diagram .tex files.

Usage:
    python scripts/build_flow.py                          # build all PDFs + images
    python scripts/build_flow.py --no-images              # PDFs only
    python scripts/build_flow.py --component vlm          # single component
    python scripts/build_flow.py --diagram 01_data_pipeline_flow
    python scripts/build_flow.py --diagram backend/01_api_routing_flow.tex
    python scripts/build_flow.py --clean                  # rebuild from scratch
    python scripts/build_flow.py --engine xelatex         # use XeLaTeX instead of pdflatex
"""

import argparse
import re
import os
import shutil
import subprocess
import sys
import glob
import tempfile

# ─── Paths ────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MANUSCRIPT_ROOT = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(MANUSCRIPT_ROOT, "data", "flow_digram_data")
BUILD_DIR = os.path.join(DATA_DIR, "build")
IMAGE_DIR = os.path.join(DATA_DIR, "images_flow_diagram")

# Must match actual directory names under flow_digram_data/
KNOWN_DIRS = ("yolo", "vlm", "backend", "mobile_app")
# Desired page order in the combined PDF
COMPONENT_ORDER = {name: i for i, name in enumerate(KNOWN_DIRS)}

WRAPPER_TEMPLATE = r"""\documentclass[tikz,border=10pt]{standalone}
\usepackage{tikz}
\usepackage{float}
\usepackage{xcolor}
\usetikzlibrary{arrows.meta,positioning,calc,fit,backgrounds,shadows.blur}

\begin{document}
\hyphenpenalty=10000
\exhyphenpenalty=10000
INPUT_CONTENT
\end{document}
"""


# ─── Helpers ──────────────────────────────────────────────────────

def normalize_relpath(path):
    return os.path.relpath(path, DATA_DIR).replace("\\", "/")


def diagram_aliases(path):
    rel = normalize_relpath(path)
    stem = os.path.splitext(os.path.basename(path))[0]
    rel_no_ext = os.path.splitext(rel)[0]
    component = rel.split("/", 1)[0]
    image_label = rel_no_ext.replace("/", "_")
    return {
        rel.lower(),
        rel_no_ext.lower(),
        os.path.basename(path).lower(),
        stem.lower(),
        image_label.lower(),
        f"{component}/{stem}".lower(),
    }


def find_tex_files(component=None, diagram=None):
    all_files = []
    for sub in KNOWN_DIRS:
        pattern = os.path.join(DATA_DIR, sub, "**", "*.tex")
        all_files.extend(glob.glob(pattern, recursive=True))

    if component:
        all_files = [f for f in all_files if component.lower() in f.lower()]
    if diagram:
        needle = diagram.lower().replace("\\", "/").removesuffix(".png").removesuffix(".pdf")
        all_files = [f for f in all_files if needle in diagram_aliases(f)]

    # Sort by component order, then numeric filename within each component
    def sort_key(path):
        rel = os.path.relpath(path, DATA_DIR)
        comp = rel.split(os.sep)[0]
        return (COMPONENT_ORDER.get(comp, 99), rel)

    return sorted(all_files, key=sort_key)


def read_figure_content(tex_path):
    with open(tex_path, "r", encoding="utf-8") as f:
        content = f.read()
    start = content.find(r"\begin{figure}")
    end = content.find(r"\end{figure}")
    if start == -1 or end == -1:
        print(f"  WARNING: no figure environment in {tex_path}")
        return None
    end += len(r"\end{figure}")
    figure_block = content[start:end]

    caption_match = re.search(r"\\caption\{(.+?)\}", figure_block, re.DOTALL)
    caption = caption_match.group(1).strip() if caption_match else None

    label_match = re.search(r"\\label\{(.+?)\}", figure_block, re.DOTALL)
    label = label_match.group(1).strip() if label_match else None

    inner = re.sub(r"\\begin\{figure\}\[.*?\]\s*", "", figure_block, count=1, flags=re.DOTALL)
    inner = re.sub(r"\\end\{figure\}\s*$", "", inner, count=1, flags=re.DOTALL)
    inner = re.sub(r"\\caption\{.+?\}\s*", "", inner, flags=re.DOTALL)
    inner = re.sub(r"\\label\{.+?\}\s*", "", inner, flags=re.DOTALL)
    inner = inner.replace(r"\centering", "", 1).strip()

    tikz_match = re.search(
        r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}",
        inner,
        re.DOTALL,
    )
    if tikz_match:
        inner = tikz_match.group(0)

    return {
        "body": inner,
        "caption": caption,
        "label": label,
    }


def build_standalone_tex(figure_parts, output_path):
    wrapper = WRAPPER_TEMPLATE.replace("INPUT_CONTENT", figure_parts["body"])
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(wrapper)


def run_latex(tex_path, output_dir, engine="pdflatex"):
    base = os.path.splitext(os.path.basename(tex_path))[0]
    tex_dir = os.path.dirname(tex_path)

    result = subprocess.run(
        [engine, "-interaction=nonstopmode", "-file-line-error",
         f"-output-directory={output_dir}", tex_path],
        cwd=tex_dir, capture_output=True, text=True,
    )
    if result.returncode != 0:
        pdf_path = os.path.join(output_dir, f"{base}.pdf")
        if not os.path.exists(pdf_path):
            print("  ERROR during LaTeX build")
            print(result.stderr[-500:])
            return False
    return True


def pdf_to_png(pdf_path, output_dir, label):
    """Convert a single-page PDF to a high-res PNG.
    Uses pdftoppm if available, falls back to PyMuPDF, then ImageMagick.
    """
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"{label}.png")

    # ── Try pdftoppm (poppler) ─────────────────────────────────
    pdftoppm = shutil.which("pdftoppm")
    if pdftoppm:
        tmp_dir = tempfile.mkdtemp(prefix="flow_png_", dir=output_dir)
        tmp_prefix = os.path.join(tmp_dir, label)
        try:
            result = subprocess.run(
                [pdftoppm, "-png", "-r", "200", "-singlefile",
                 pdf_path, tmp_prefix],
                capture_output=True, text=True,
            )
            for candidate_suffix in ("", "-1"):
                candidate = f"{tmp_prefix}{candidate_suffix}.png"
                if os.path.exists(candidate):
                    shutil.move(candidate, out_path)
                    return True
        finally:
            shutil.rmtree(tmp_dir, ignore_errors=True)

    # ── Fallback: PyMuPDF ──────────────────────────────────────
    try:
        import fitz
        doc = fitz.open(pdf_path)
        page = doc[0]
        pix = page.get_pixmap(dpi=200)
        pix.save(out_path)
        doc.close()
        return True
    except Exception:
        pass

    # ── Last resort: ImageMagick ───────────────────────────────
    magick = shutil.which("magick")
    if magick:
        result = subprocess.run(
            [magick, "-density", "200", pdf_path,
             "-quality", "90", out_path],
            capture_output=True, text=True,
        )
        return result.returncode == 0

    print("  WARNING: no PDF→PNG tool found. Install poppler, PyMuPDF, or ImageMagick.")
    return False


def output_paths_for(tex_path):
    rel_path = os.path.relpath(tex_path, DATA_DIR)
    rel_dir = os.path.dirname(rel_path)
    base_name = os.path.splitext(os.path.basename(tex_path))[0]
    out_subdir = os.path.join(BUILD_DIR, rel_dir) if rel_dir else BUILD_DIR
    final_pdf = os.path.join(out_subdir, f"{base_name}.pdf")
    img_label = f"{rel_dir}_{base_name}" if rel_dir else base_name
    img_label = img_label.replace("\\", "_").replace("/", "_")
    final_png = os.path.join(IMAGE_DIR, f"{img_label}.png")
    return out_subdir, final_pdf, final_png


def clean_outputs(tex_files, build_images=True):
    """Remove only the generated artifacts for the selected diagrams."""
    for tex_path in tex_files:
        out_subdir, final_pdf, final_png = output_paths_for(tex_path)
        base_name = os.path.splitext(os.path.basename(tex_path))[0]
        paths = [
            final_pdf,
            os.path.join(out_subdir, f"_{base_name}.pdf"),
            os.path.join(out_subdir, f"_{base_name}.tex"),
            os.path.join(out_subdir, f"_{base_name}.aux"),
            os.path.join(out_subdir, f"_{base_name}.log"),
            os.path.join(out_subdir, f"_{base_name}.out"),
        ]
        if build_images:
            paths.append(final_png)
        for path in paths:
            if os.path.exists(path):
                try:
                    os.remove(path)
                except OSError:
                    pass


# ─── Main ─────────────────────────────────────────────────────────

def build_all(component=None, diagram=None, clean=False, engine="pdflatex", build_images=True):
    if not os.path.isdir(DATA_DIR):
        print(f"ERROR: Data directory not found: {DATA_DIR}")
        sys.exit(1)

    tex_files = find_tex_files(component, diagram)
    if not tex_files:
        print(f"No .tex files found in {DATA_DIR}")
        if component:
            print(f"  (filtered by component: {component})")
        if diagram:
            print(f"  (filtered by diagram: {diagram})")
        sys.exit(1)

    filtered_build = bool(component or diagram)
    if clean and not filtered_build and os.path.isdir(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
        print(f"Cleaned: {BUILD_DIR}")
    if clean and not filtered_build and os.path.isdir(IMAGE_DIR):
        shutil.rmtree(IMAGE_DIR)
        print(f"Cleaned: {IMAGE_DIR}")

    os.makedirs(BUILD_DIR, exist_ok=True)
    if build_images:
        os.makedirs(IMAGE_DIR, exist_ok=True)

    if clean and filtered_build:
        clean_outputs(tex_files, build_images)
        print("Cleaned selected diagram artifacts")

    print(f"Found {len(tex_files)} flow diagram files")
    print(f"PDF output:   {BUILD_DIR}")
    if build_images:
        print(f"Image output: {IMAGE_DIR}")
    print()

    pdf_ok = 0
    pdf_fail = 0
    img_ok = 0
    img_fail = 0

    for tex_path in tex_files:
        rel_path = os.path.relpath(tex_path, DATA_DIR)
        print(f"[{rel_path}]")

        figure_parts = read_figure_content(tex_path)
        if figure_parts is None:
            pdf_fail += 1
            continue

        # Build wrapper .tex in the build dir, preserving subdir structure
        rel_dir = os.path.dirname(rel_path)
        out_subdir = os.path.join(BUILD_DIR, rel_dir) if rel_dir else BUILD_DIR
        os.makedirs(out_subdir, exist_ok=True)

        base_name = os.path.splitext(os.path.basename(tex_path))[0]
        wrapper_path = os.path.join(out_subdir, f"_{base_name}.tex")

        build_standalone_tex(figure_parts, wrapper_path)

        if not run_latex(wrapper_path, out_subdir, engine):
            pdf_fail += 1
            continue

        # Move PDF to clean name
        raw_pdf = os.path.join(out_subdir, f"_{base_name}.pdf")
        final_pdf = os.path.join(out_subdir, f"{base_name}.pdf")
        if os.path.exists(raw_pdf):
            shutil.move(raw_pdf, final_pdf)
            print(f"  PDF OK -> {os.path.relpath(final_pdf, BUILD_DIR)}")
            pdf_ok += 1

        # PDF → PNG
        if build_images and os.path.exists(final_pdf):
            img_label = f"{rel_dir}_{base_name}" if rel_dir else base_name
            img_label = img_label.replace("\\", "_").replace("/", "_")
            if pdf_to_png(final_pdf, IMAGE_DIR, img_label):
                img_path = os.path.join(IMAGE_DIR, f"{img_label}.png")
                print(f"  PNG OK -> {os.path.relpath(img_path, IMAGE_DIR)}")
                img_ok += 1
            else:
                img_fail += 1

    # Clean up auxiliary files (keep only PDFs and PNGs)
    for root, dirs, files in os.walk(BUILD_DIR):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in (".aux", ".log", ".out", ".tex"):
                try:
                    os.remove(os.path.join(root, f))
                except OSError:
                    pass

    # Merge all individual PDFs into a single combined PDF
    merged = None
    if not component and not diagram and len(tex_files) > 1:
        pdfunite = shutil.which("pdfunite")
        if pdfunite and pdf_ok > 0:
            pdf_files = []
            for tex_path in tex_files:
                rel_path = os.path.relpath(tex_path, DATA_DIR)
                rel_dir = os.path.dirname(rel_path)
                base_name = os.path.splitext(os.path.basename(tex_path))[0]
                out_subdir = os.path.join(BUILD_DIR, rel_dir) if rel_dir else BUILD_DIR
                candidate = os.path.join(out_subdir, f"{base_name}.pdf")
                if os.path.exists(candidate):
                    pdf_files.append(candidate)

            if pdf_files:
                merged_path = os.path.join(BUILD_DIR, "00_all_flows.pdf")
                result = subprocess.run(
                    [pdfunite] + pdf_files + [merged_path],
                    capture_output=True, text=True,
                )
                if result.returncode == 0 and os.path.exists(merged_path):
                    merged = merged_path

    print()
    print(f"PDFs:  {pdf_ok} succeeded, {pdf_fail} failed")
    if build_images:
        print(f"PNGs:  {img_ok} succeeded, {img_fail} failed")
    print(f"Total: {len(tex_files)} files")
    if merged:
        print(f"Merged: {os.path.relpath(merged, DATA_DIR)}")
    if len(tex_files) == 1:
        rel_path = os.path.relpath(tex_files[0], DATA_DIR)
        rel_dir = os.path.dirname(rel_path)
        base_name = os.path.splitext(os.path.basename(tex_files[0]))[0]
        pdf_path = os.path.join(BUILD_DIR, rel_dir, f"{base_name}.pdf") if rel_dir else os.path.join(BUILD_DIR, f"{base_name}.pdf")
        print(f"Single PDF: {pdf_path}")
        if build_images:
            img_label = f"{rel_dir}_{base_name}" if rel_dir else base_name
            img_label = img_label.replace("\\", "_").replace("/", "_")
            print(f"Single PNG: {os.path.join(IMAGE_DIR, f'{img_label}.png')}")

    return pdf_fail == 0


def list_diagrams():
    for tex_path in find_tex_files():
        rel = normalize_relpath(tex_path)
        rel_no_ext = os.path.splitext(rel)[0]
        image_label = rel_no_ext.replace("/", "_")
        print(f"{rel_no_ext} [{image_label}]")


def main():
    parser = argparse.ArgumentParser(description="Build flow diagram PDF/PNG previews")
    parser.add_argument("--component", "-c", help="Build only one component "
                        "(e.g. 'yolo', 'vlm', 'backend', 'mobile_app')")
    parser.add_argument("--diagram", "-d",
                        help="Build only one diagram by basename or relative path "
                             "(e.g. '01_data_pipeline_flow' or "
                             "'backend/01_api_routing_flow.tex')")
    parser.add_argument("--clean", action="store_true",
                        help="Remove build artifacts before building")
    parser.add_argument("--engine", default="pdflatex",
                        help="LaTeX engine: pdflatex (default) or xelatex")
    parser.add_argument("--no-images", action="store_true",
                        help="Skip PNG generation, only build PDFs")
    parser.add_argument("--list", action="store_true",
                        help="List available diagram ids and exit")
    args = parser.parse_args()

    if args.list:
        list_diagrams()
        sys.exit(0)

    success = build_all(
        component=args.component,
        diagram=args.diagram,
        clean=args.clean,
        engine=args.engine,
        build_images=not args.no_images,
    )
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
