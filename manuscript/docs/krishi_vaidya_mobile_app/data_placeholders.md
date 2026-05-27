# Mobile App Data and Artifact Status

Store mobile artifacts in:

`../../data/krishi_vaidya_mobile_app_data`

## Current artifacts

| Artifact | File | Status | Notes |
| --- | --- | --- | --- |
| Mobile architecture figure | `outputs/figures/mobile_app_architecture.pdf` and `.png` | Generated and placed | Created from implemented source structure. |
| Architecture generation script | `generate_mobile_architecture.py` | Available | Re-run after major route/provider/offline architecture changes. |

## Remaining artifacts

| Artifact | File suggestion | Required before final manuscript? | Notes |
| --- | --- | --- | --- |
| App navigation diagram | `architecture/mobile_navigation_flow.*` | Optional | The generated architecture figure already covers route groups; create only if the final manuscript needs a more detailed route-only figure. |
| Scan workflow diagram | `architecture/mobile_scan_workflow.*` | Optional | Text has been drafted from scan source files; add a figure if visual clarity is required. |
| Offline sync diagram | `architecture/mobile_offline_sync.*` | Optional | Text has been drafted from sync source files; add only after final sync behavior is validated. |
| Home screen screenshot | `screenshots/home.*` | Yes | Capture final UI. |
| Scan screen screenshot | `screenshots/scan.*` | Yes | Capture final UI. |
| Diagnosis result screenshot | `screenshots/diagnosis_result.*` | Yes | Capture final UI. |
| Crop record screenshot | `screenshots/crop_record.*` | Recommended | Capture final UI. |
| Settings/localization screenshot | `screenshots/settings_or_language.*` | Recommended | Capture final UI. |
| Device/runtime evidence | `runtime/mobile_runtime_notes.md` | Yes before final claims | Include emulator/device, backend URL, scan flow behavior, latency, and TFLite model-loading notes. |

## Placeholder rule

Do not describe visual details that are not captured or visible in the source. Replace placeholders only after screenshots or diagrams exist.
