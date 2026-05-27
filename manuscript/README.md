# Krishi Vaidya Manuscript Workspace

This directory contains the LaTeX manuscript and the organized planning system for writing the Krishi Vaidya final-year BSc CSIT project report. Krishi Vaidya is one project with four major implementation components: YOLO object detection, VLM disease diagnosis, backend API, and mobile app.

## Main manuscript files

- `main.tex`: root LaTeX document that wires together front matter, chapters, references, and appendix.
- `chapters/`: source files for the five report chapters.
- `frontmatter/`: title page, declaration, approval pages, acknowledgements, abstracts, acronyms, and symbols.
- `appendix/`: appendix source.
- `bib/references.bib`: bibliography database.
- `config/`: metadata, package configuration, and reusable macros.
- `scripts/build.ps1`: manuscript build script.
- `build/`: generated PDF and auxiliary files.

## Component documentation

Component documentation lives under `docs/`. Each component has its own folder and at least four focused files.

- `docs/krishi_vaidya_yolo/`: YOLO overview, architecture/pipeline notes, data assets, and manuscript plan.
- `docs/krishi_vaidya_vlm/`: VLM overview, architecture/pipeline notes, data assets, and manuscript plan.
- `docs/krishi_vaidya_backend/`: backend overview, architecture notes, data placeholders, and manuscript plan.
- `docs/krishi_vaidya_mobile_app/`: mobile app overview, architecture notes, data placeholders, and manuscript plan.

Use these folders before writing manuscript prose. They explain where evidence is located and which parts are still placeholders.

## Progress and tracking files

Manuscript planning and tracking files live under `progress/`.

- `progress/ledger.md`: master checklist for chapters, sections, figures, tables, and missing assets.
- `progress/progress.md`: current completion state and blockers.
- `progress/table_of_contents_progress.md`: detailed working table of contents with sections, subsections, and sub-subsections.
- `progress/priority.md`: recommended writing order, starting with concrete YOLO/VLM/backend/mobile sections.
- `progress/assets_inventory.md`: ready assets and missing artifacts.
- `progress/figure_map.md`: planned placement of figures and tables.
- `progress/citation_plan.md`: citation policy and literature review planning.

## Data folders

- `data/krishi_vaidya_yolo_data`: manuscript-ready YOLO figures and tables.
- `data/krishi_vaidya_vlm_data`: manuscript-ready VLM figures and tables.
- `data/krishi_vaidya_backend_data`: generated backend architecture figure plus remaining placeholders for optional entity diagrams, endpoint examples, and deployment evidence.
- `data/krishi_vaidya_mobile_app_data`: generated mobile architecture figure plus remaining placeholders for screenshots, optional workflow diagrams, and runtime evidence.
- `data/krishi_vaidya_integration_data`: generated integrated diagnosis workflow figure plus remaining placeholders for live request-response evidence, runtime logs, offline recovery demonstration, and latency measurements.
- `data/krishi_vaidya_validation_data`: generated validation coverage figure plus remaining placeholders for consolidated executed-test reports, mobile runtime evidence, and live end-to-end validation evidence.

The YOLO and VLM outputs should be used directly in the manuscript. Backend, mobile app, integration, and validation sections now include generated source-backed figures and tables, while screenshots, runtime measurements, deployment evidence, executed-test reports, and live end-to-end request-response captures remain placeholders until captured.

## Recommended workflow

1. Read `docs/README.md`.
2. Read the relevant component folder under `docs/` before drafting that component.
3. Use `progress/priority.md` to write sections in evidence-first order.
4. Use `progress/table_of_contents_progress.md` as the working chapter/section structure.
5. Use `progress/ledger.md`, `progress/assets_inventory.md`, and `progress/figure_map.md` while placing figures, tables, diagrams, and screenshots.
6. Use `progress/progress.md` after each writing session to record what changed and what remains blocked.
7. Use `progress/citation_plan.md` when adding literature review claims and bibliography entries.

## Build

From PowerShell:

```powershell
.\scripts\build.ps1
```

Optional flags:

```powershell
.\scripts\build.ps1 -Clean
.\scripts\build.ps1 -Watch
```

## Evidence rule

Do not invent unsupported manuscript details. Use repository code, generated model outputs, existing documentation, or clearly marked placeholders. Replace placeholders only after the corresponding artifact or evidence exists.
