# Backend Architecture Notes

## Verified code structure

| Layer | Path | Manuscript role |
| --- | --- | --- |
| Entry/app setup | `../../../backend/src/index.ts`, `../../../backend/src/app.ts` | Server initialization and middleware wiring. |
| Routes | `../../../backend/src/routes` | API domain routing. |
| Controllers | `../../../backend/src/controllers` | Request/response handling. |
| Services | `../../../backend/src/services` | Business logic and external integration. |
| Repositories | `../../../backend/src/repositories` | Data-access abstraction. |
| Models | `../../../backend/src/models` | Mongoose data models. |
| Middlewares | `../../../backend/src/middlewares` | Auth, validation, upload, CORS, Helmet, rate limiting, logging, errors. |
| Config | `../../../backend/src/config` | Database, Redis, Cloudinary, Swagger, environment config. |

## API domains from route files

- Auth
- User
- Crop
- Task
- Note
- Scan
- Diagnosis
- Advisory

## Data models from model files

- User
- CropPlot
- CropTask
- CropNote
- Scan
- ScanResolution
- Advisory
- Otp
- RefreshToken

## Required architecture assets

| Asset | Status | Target manuscript section |
| --- | --- | --- |
| Backend layered architecture diagram | Created: `../../data/krishi_vaidya_backend_data/outputs/figures/backend_architecture.pdf` | `3.5.2` |
| API endpoint summary table | Drafted directly in manuscript from route files | `3.5` and `4.6` |
| Database/entity relationship diagram | Optional future asset; model summary table drafted from model files | `3.5.3` |
| Scan/diagnosis/advisory sequence diagram | Optional future asset; diagnosis flow drafted from services | `3.7` |
