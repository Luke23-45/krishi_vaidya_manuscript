# Mobile App Component Overview

## Role in Krishi Vaidya

The mobile app is the farmer-facing client for Krishi Vaidya. It provides scanning, diagnosis interaction, crop records, history, settings, weather, onboarding, and supporting UI workflows.

Repository source: `../../../mobile_app`

Data folder: `../../data/krishi_vaidya_mobile_app_data`

## Verified facts from local evidence

- The app is an Expo/React Native project with Expo Router.
- The configured application name is Krishi Vaidya, package `com.krishivaidya.app`, and scheme `krishivaidya`.
- Feature folders include scan, diagnosis, inference, camera, processing, crops, advisory, history, home, onboarding, settings, tips, weather, achievements, and gamification.
- Core folders include API client, domain logic, ML utilities, offline support, storage, localization, reusable components, theme, animation, and providers.
- Dependencies include React Native Vision Camera, TFLite/ONNX runtime packages, Expo SQLite, MMKV, localization, and network monitoring packages.
- Local data is stored in SQLite tables for scans, queues, crop plots, tasks, notes, advisories, settings, achievements, reminders, and notifications.
- The diagnosis client posts multipart images to `/api/v1/diagnose`.
- The TFLite service includes int8, fp16, and fp32 model assets, but mobile model-label alignment with the YOLO manuscript taxonomy still needs final verification.

## Manuscript relevance

The mobile app section now documents the user-facing implementation and how it connects the model/backend work into an accessible application. The architecture figure has been generated and placed in Chapter 3. Final screenshots, device-flow evidence, and mobile inference timing are still missing and must remain placeholders until captured.
