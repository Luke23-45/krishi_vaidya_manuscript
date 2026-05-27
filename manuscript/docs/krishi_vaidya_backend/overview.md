# Backend Component Overview

## Role in Krishi Vaidya

The backend is the API and persistence layer for Krishi Vaidya. It connects the mobile application to user, crop, task, note, scan, diagnosis, advisory, file upload, and model-integration workflows.

Repository source: `../../../backend`

Placeholder data folder: `../../data/krishi_vaidya_backend_data`

## Verified facts from local evidence

- Backend package name: `krishi-vaidya-api`.
- Main framework: Express with TypeScript.
- Persistence layer uses Mongoose models.
- Route domains include auth, users, crops, tasks, notes, scans, diagnosis, and advisory.
- Services include scan handling, diagnosis validation, VLM inference client, advisory client, file upload, email, and authentication.
- Unit and integration test folders exist under `../../../backend/tests`.

## Manuscript relevance

The backend section should explain how the completed model and mobile components are connected into a working system. Because final manuscript diagrams and endpoint tables are not yet present, those assets must remain placeholders until created.

