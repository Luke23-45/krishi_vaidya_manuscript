# Manuscript Progress Tracker

## Current state

| Area | Status | Next action |
| --- | --- | --- |
| Component docs | In progress | Use `../docs/<component>` as source maps while writing. |
| YOLO manuscript data | Drafted | Review wording and visual placement in generated PDF. |
| VLM manuscript data | Drafted | Review wording and visual placement in generated PDF. |
| Backend manuscript data | Drafted | Review wording, generated architecture figure, and backend tables in the PDF. |
| Mobile app manuscript data | Drafted | Review wording, generated architecture figure, and mobile tables in the PDF; capture final screenshots later. |
| Integration workflow | Drafted | Review wording, generated workflow figure, integration tables, and evidence-gap wording in the PDF. |
| Testing and validation | Drafted | Review source-backed validation summary, generated validation coverage figure, and evidence-gap wording in the PDF. |
| Results discussion and limitations | Drafted | Review cross-system synthesis tables and ensure claims remain consistent with available evidence. |
| Literature review | Polished | Add institution-required sources only if supervisors request them. |
| Conclusion and recommendations | Polished | Re-check after any new runtime evidence is added. |
| Introduction | Polished | Re-check after any new runtime evidence is added. |
| Abstracts | Polished | Review Nepali abstract and front-matter identity after final metadata is confirmed. |
| Appendices | Drafted | Add mobile screenshots, executed-test logs, and API examples when captured. |
| Table of contents | In progress | Use `table_of_contents_progress.md` as the active structure. |
| Citations | Drafted | 18 cited sources are included; add more only for new claims. |

## Completed in planning

- Component documentation directories exist for YOLO, VLM, backend, and mobile app.
- YOLO and VLM data assets are mapped.
- Backend and mobile missing artifacts are represented as placeholders.
- Detailed TOC planning exists.
- Writing priority order exists.
- YOLO dataset, training method, threshold analysis, deployment evaluation, and error analysis have been drafted in Chapter 3 and Chapter 4.
- All four YOLO figures and all five YOLO manuscript result tables have been placed in Chapter 4.
- VLM dataset pipeline, taxonomy, Qwen export, LoRA fine-tuning method, quantized training setup, prediction parsing, training results, resource results, dataset results, prediction metrics, and parse-error limitation have been drafted in Chapter 3 and Chapter 4.
- All six VLM figures and all seven VLM manuscript result tables have been placed in Chapter 4.
- Backend system architecture, runtime modes, dependency container, API route groups, data models, repository layer, diagnosis/advisory pipeline, security controls, implementation outcomes, domain discussion, test evidence, and limitations have been drafted in Chapter 3 and Chapter 4.
- The backend architecture figure has been generated from verified source structure and placed in Chapter 3.
- Mobile application architecture, route structure, provider/repository design, local persistence, offline sync, scan workflow, backend diagnosis client, TFLite asset support, localization, implementation outcomes, and limitations have been drafted in Chapter 3 and Chapter 4.
- The mobile architecture figure has been generated from verified source structure and placed in Chapter 3.
- Integrated diagnosis workflow, mobile-to-backend flow, backend-to-VLM flow, advisory generation boundary, offline/slow-network behavior, structured response contract, reliability controls, evidence gaps, and integrated system interpretation have been drafted in Chapter 3 and Chapter 4.
- The integrated workflow figure has been generated from verified source structure and placed in Chapter 3.
- Testing and validation coverage across YOLO, VLM, VLM API, backend, mobile, and integration has been drafted in Chapter 3 from inspected repository evidence and recorded model artifacts.
- The validation coverage figure has been generated and placed in Chapter 3.
- Cross-system results discussion and limitations have been drafted in Chapter 4, including result synthesis and required future evidence tables.
- Chapter 2 literature review has been drafted in the requested section order with government, FAO, primary research, and official documentation citations.
- Chapter 5 conclusion, contributions, recommendations, and future enhancements have been drafted from the actual implemented components and documented limitations.
- Chapter 1 introduction has been replaced with Krishi Vaidya-specific Nepal context, problem statement, objectives, scope, limitations, methodology overview, and report organization.
- English abstract, Nepali abstract, acronyms, symbols, bibliography, and appendix content have been replaced with project-specific content.
- The manuscript build completed successfully after adding the testing/validation and cross-system discussion sections.
- A final prose-polish pass was completed across the English abstract and Chapters 1--5, removing internal drafting language, tightening evidence boundaries, replacing the leftover YOLO dataset nickname with plant-part dataset terminology, and strengthening the research-gap, validation-boundary, integration, and conclusion wording.
- The manuscript build completed successfully after the final prose-polish pass.

## Active blockers

| Blocker | Affected section | Resolution |
| --- | --- | --- |
| Missing overall system architecture diagram | 3.1 | Optional future asset; current integration workflow diagram covers the diagnosis path but not the whole project map. |
| Missing backend entity diagram | 3.5 | Optional future asset; current manuscript includes model summary table. |
| Missing backend endpoint screenshots/examples | 4.6 or appendix | Capture only from a running backend if required. |
| Missing mobile screenshots | 4.7 or appendix | Capture final app screens from a running build. |
| Mobile runtime/device evidence | 4.7 | Run emulator or physical-device scan workflow and record screenshots, latency, and TFLite behavior before final claims. |
| Missing end-to-end runtime evidence | 3.7 and 4.8 | Capture real mobile-to-backend request/response, VLM readiness/inference logs, advisory response, and latency measurements. |
| Missing broader backend test coverage | 3.8 and 4.6 | Add tests for auth, crops, tasks, notes, advisories, and diagnosis before claiming complete backend verification. |
| Missing consolidated executed-test reports | 3.8 and 4.9 | Run and archive the relevant YOLO, VLM, backend, mobile, and end-to-end test commands before final submission if executable test logs are required. |
| Student/supervisor/front-matter identity placeholders | Front matter | Replace placeholder student, supervisor, campus, examiner, and approval metadata with verified names before submission. |

## Build notes

Latest build output: `build/main.pdf` (121 pages)

The build completes. MiKTeX prints maintenance warnings about updates and LaTeX reports several underfull boxes, but the generated PDF is produced successfully.

## Update rule

After every manuscript writing session, update this file and `ledger.md`.
