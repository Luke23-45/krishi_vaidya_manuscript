# Mobile App Manuscript Plan

## Priority

The mobile app section has been drafted after YOLO, VLM, and backend. The code exists and has been inspected. Final screenshots, runtime evidence, and optional detailed workflow diagrams still need to be produced before final submission.

## Suggested section placement

| Manuscript section | Content |
| --- | --- |
| `3.6 Mobile Application Method` | Drafted: stack, route structure, providers, repositories, SQLite, offline sync, scan workflow, diagnosis client, TFLite assets, localization. |
| `3.7 Integration Method` | Still future: integrated end-to-end sequence across mobile, backend, VLM, and advisory generation. |
| `4.7 Mobile App Implementation Results` | Drafted: implemented surface, scan result flow, local/offline result, crop management, model deployment notes, verification limits. |

## Writing checks

- Verify screen names from `../../../mobile_app/app/app`.
- Verify feature descriptions from `../../../mobile_app/app/features`.
- Verify local ML claims from `../../../mobile_app/app/core/ml`.
- Verify offline claims from `../../../mobile_app/app/core/offline`.
- Do not include screenshots until final app screens are captured.
- Do not claim complete TFLite/YOLO parity until the exported mobile model labels are reconciled with the YOLO manuscript taxonomy.
- Do not claim complete two-way sync for every table until backend push handlers and runtime tests are documented.
