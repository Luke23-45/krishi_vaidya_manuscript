# Mobile App Architecture Notes

## Verified code structure

| Area | Path | Manuscript role |
| --- | --- | --- |
| Expo Router screens | `../../../mobile_app/app/app` | Navigation and screen structure. |
| Feature modules | `../../../mobile_app/app/features` | User-facing workflows. |
| API client | `../../../mobile_app/app/core/api` | Backend communication. |
| Domain layer | `../../../mobile_app/app/core/domain` | Entities, services, repositories, and flows. |
| ML utilities | `../../../mobile_app/app/core/ml` | TFLite/ONNX/frame-processing support. |
| Offline support | `../../../mobile_app/app/core/offline` | Queue, sync, network monitoring, cached disease data. |
| Localization | `../../../mobile_app/app/core/i18n` | English and Nepali localization files. |
| UI foundation | `../../../mobile_app/app/core/components`, `../../../mobile_app/app/core/theme` | Reusable interface components and styling. |

## Major feature folders

- Scan
- Diagnosis
- Inference
- Camera
- Processing
- Crops
- Advisory
- History
- Home
- Onboarding
- Settings
- Tips
- Weather
- Achievements
- Gamification

## Required architecture assets

| Asset | Status | Target manuscript section |
| --- | --- | --- |
| Mobile application architecture | Generated and placed: `../../data/krishi_vaidya_mobile_app_data/outputs/figures/mobile_app_architecture.*` | `3.6` |
| Mobile navigation diagram | Covered in architecture figure; optional detailed future asset | `3.6.2` |
| Scan workflow diagram | Covered textually; optional detailed future asset | `3.6.5` |
| Offline synchronization diagram | Covered textually; optional detailed future asset | `3.6.4` |
| Mobile screenshots | Placeholder | `4.7.3` |

## Source-backed architecture summary

- App shell: `app.config.ts` and `app/_layout.tsx`.
- Navigation: `app/(tabs)`, `app/scan`, `app/onboarding`, `app/crops`, and `app/settings`.
- Dependency setup: `core/providers/ServicesProvider.tsx`, `core/providers/RepositoryProvider.tsx`, and `data/bootstrap.ts`.
- Local data: `core/storage/schema.ts`, `core/storage/db.ts`, and repository classes under `data/repositories`.
- Offline behavior: `core/offline/sync-service.ts`, `core/offline/queue-manager.ts`, and `core/hooks/useDiagnosis.ts`.
- Backend communication: `core/api/client.ts`.
- Mobile inference assets: `core/ml/tflite-service.ts` and `assets/models/quantized`.
