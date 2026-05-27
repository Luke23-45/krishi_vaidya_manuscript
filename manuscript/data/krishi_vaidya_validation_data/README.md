# Testing and Validation Manuscript Data

This folder stores manuscript assets for the testing and validation section.

## Generated assets

- `generate_validation_coverage.py`
  - Generates the testing and validation coverage diagram.
- `outputs/figures/validation_coverage.pdf`
  - Imported into Chapter 3.
- `outputs/figures/validation_coverage.png`
  - Preview/export copy of the same figure.

## Evidence represented by the diagram

- YOLO quantitative validation and validation-tool tests.
- VLM dataset validation, prediction metrics, and validation tests.
- Backend scan service and scan route tests.
- VLM inference API contract tests.
- Mobile source verification and inference test harness status.
- Integration source verification and remaining runtime evidence gaps.

## Remaining evidence to add

- Executed backend test report if required for appendix.
- Executed VLM/YOLO test report if required for appendix.
- Mobile emulator or physical-device validation notes.
- End-to-end runtime request-response evidence.
- Latency measurements across mobile, backend, VLM, and advisory stages.
