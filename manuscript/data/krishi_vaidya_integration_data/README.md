# Integration Workflow Manuscript Data

This folder stores manuscript evidence for the end-to-end Krishi Vaidya integration workflow.

## Generated assets

- `generate_integration_workflow.py`
  - Generates the source-backed integrated diagnosis workflow diagram.
- `outputs/figures/integration_workflow.pdf`
  - Imported into Chapter 3.
- `outputs/figures/integration_workflow.png`
  - Preview/export copy of the same diagram.

## Evidence represented by the diagram

- Mobile scan workflow and network-aware diagnosis hook.
- Mobile-to-backend multipart diagnosis request.
- Backend upload validation and diagnosis orchestration.
- Backend-to-VLM readiness and inference request.
- VLM FastAPI gateway and vLLM-backed prediction response.
- Backend prediction parsing and advisory generation.
- Structured backend response consumed by the mobile result UI.
- Offline queue and local persistence fallback.

## Remaining evidence to add

- Real mobile-to-backend request and response capture.
- Backend and VLM gateway runtime logs for one successful diagnosis.
- Mobile result screenshots from a running build.
- Offline-to-online queue recovery demonstration.
- End-to-end latency measurements.
- Final model-label alignment evidence between mobile TFLite assets and YOLO training/export assets.

Do not claim final production runtime performance until the remaining runtime evidence is captured.
