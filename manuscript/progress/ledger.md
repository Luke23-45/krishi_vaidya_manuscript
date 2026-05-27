# Manuscript Ledger

Status values: `Not started`, `In progress`, `Ready to draft`, `Needs asset`, `Drafted`, `Final`.

## Required manuscript parts

| Area | Required items | Status |
| --- | --- | --- |
| Front matter | Title page, recommendation, declaration, letter of forward, board approval, acknowledgements, English abstract, Nepali abstract, acronyms, symbols | In progress; abstracts/acronyms/symbols drafted, identity placeholders remain |
| Chapter 1 | Background, problem statement, objectives, scope, limitations, methodology overview, report organization | Drafted |
| Chapter 2 | Digital agriculture, crop disease diagnosis, object detection, VLMs, mobile/backend systems, research gap | Drafted |
| Chapter 3 | System design, datasets, YOLO method, VLM method, backend method, mobile method, integration, validation | In progress |
| Chapter 4 | YOLO results, VLM results, backend results, mobile results, integrated discussion, limitations | In progress |
| Chapter 5 | Conclusion, contributions, recommendations, future work | Drafted |
| References | Literature and technical citations | Drafted |
| Appendix | Supplementary outputs, API details, screenshots, additional setup notes | Drafted; screenshots and logs remain placeholders |

## Component writing checklist

| Component | Required manuscript coverage | Evidence status |
| --- | --- | --- |
| YOLO | Dataset, classes, training setup, validation, threshold sweep, deployment variants, per-class metrics, error analysis | Drafted in Chapters 3 and 4 |
| VLM | Dataset, base model, LoRA, quantization, training, runtime, class distribution, prediction summary, per-class metrics, parse-error limitation | Drafted in Chapters 3 and 4 |
| Backend | Stack, layered architecture, route domains, models, middleware, scan/diagnosis/advisory services, tests | Drafted in Chapters 3 and 4 |
| Mobile app | Stack, navigation, scan workflow, feature modules, local ML utilities, offline support, localization, screenshots | Drafted in Chapters 3 and 4; screenshots and runtime evidence still needed |
| Integration workflow | Mobile-to-backend flow, backend-to-VLM flow, advisory generation, offline fallback, structured response, reliability controls, evidence gaps | Drafted in Chapters 3 and 4; live runtime evidence still needed |
| Testing and validation | Source-backed validation strategy across YOLO, VLM, VLM API, backend, mobile, and integration | Drafted in Chapter 3 |
| Results discussion and limitations | Cross-system interpretation, evidence limits, deployment implications, and future evidence requirements | Drafted in Chapter 4 |

## Figures required

| Figure | Source or status | Target section |
| --- | --- | --- |
| YOLO training dynamics | Placed: `../data/krishi_vaidya_yolo_data/outputs/figures/figure1_training_dynamics.*` | 4.1 |
| YOLO threshold sweep | Placed: `../data/krishi_vaidya_yolo_data/outputs/figures/figure2_threshold_sweep.*` | 4.2 |
| YOLO quantization comparison | Placed: `../data/krishi_vaidya_yolo_data/outputs/figures/figure3_quantization_comparison.*` | 4.2 |
| YOLO confusion matrix | Placed: `../data/krishi_vaidya_yolo_data/outputs/figures/figure4_confusion_matrix.*` | 4.3 |
| VLM training dynamics | Placed: `../data/krishi_vaidya_vlm_data/outputs/figures/figure1_training_dynamics.*` | 4.4 |
| VLM memory/runtime | Placed: `../data/krishi_vaidya_vlm_data/outputs/figures/figure2_memory_runtime.*` | 4.4 |
| VLM dataset composition | Placed: `../data/krishi_vaidya_vlm_data/outputs/figures/figure3_dataset_composition.*` | 4.5 |
| VLM prediction performance | Placed: `../data/krishi_vaidya_vlm_data/outputs/figures/figure4_prediction_performance.*` | 4.5 |
| VLM confusion matrix | Placed: `../data/krishi_vaidya_vlm_data/outputs/figures/figure5_confusion_matrix.*` | 4.5 |
| VLM inference diagnostics | Placed: `../data/krishi_vaidya_vlm_data/outputs/figures/figure6_inference_diagnostics.*` | 4.5 |
| Overall system architecture | Placeholder | 3.1 |
| Backend architecture | Placed: `../data/krishi_vaidya_backend_data/outputs/figures/backend_architecture.*` | 3.5 |
| Backend entity diagram | Optional future asset; model table drafted from source | 3.5 |
| Mobile application architecture | Placed: `../data/krishi_vaidya_mobile_app_data/outputs/figures/mobile_app_architecture.*` | 3.6 |
| Mobile screenshots | Placeholder | 4.7 |
| Integrated diagnosis workflow | Placed: `../data/krishi_vaidya_integration_data/outputs/figures/integration_workflow.*` | 3.7 |
| Validation coverage | Placed: `../data/krishi_vaidya_validation_data/outputs/figures/validation_coverage.*` | 3.8 |

## Tables required

| Table | Source or status | Target section |
| --- | --- | --- |
| YOLO training dynamics | Placed: `../data/krishi_vaidya_yolo_data/outputs/tables/table1_training_dynamics.*` | 4.1 |
| YOLO threshold sweep | Placed: `../data/krishi_vaidya_yolo_data/outputs/tables/table2_threshold_sweep.*` | 4.2 |
| YOLO deployment efficiency | Placed: `../data/krishi_vaidya_yolo_data/outputs/tables/table3a_deployment_summary.*` | 4.2 |
| YOLO per-class F1 | Placed: `../data/krishi_vaidya_yolo_data/outputs/tables/table3b_per_class_f1.*` | 4.2 |
| YOLO error analysis | Placed: `../data/krishi_vaidya_yolo_data/outputs/tables/table4_error_analysis.*` | 4.3 |
| VLM training summary | Placed: `../data/krishi_vaidya_vlm_data/outputs/tables/table1_training_summary.*` | 4.4 |
| VLM runtime resources | Placed: `../data/krishi_vaidya_vlm_data/outputs/tables/table2_runtime_resources.*` | 4.4 |
| VLM dataset splits | Placed: `../data/krishi_vaidya_vlm_data/outputs/tables/table3_dataset_splits.*` | 4.5 |
| VLM class distribution | Placed: `../data/krishi_vaidya_vlm_data/outputs/tables/table4_class_distribution.*` | 4.5 |
| VLM prediction summary | Placed: `../data/krishi_vaidya_vlm_data/outputs/tables/table5_prediction_summary.*` | 4.5 |
| VLM per-class metrics | Placed: `../data/krishi_vaidya_vlm_data/outputs/tables/table6_per_class_metrics.*` | 4.5 |
| VLM prediction distribution | Placed: `../data/krishi_vaidya_vlm_data/outputs/tables/table7_prediction_distribution.*` | 4.5 |
| Backend endpoint summary | Drafted manually from route files | 3.5 and 4.6 |
| Backend data model summary | Drafted manually from model files | 3.5 |
| Mobile route/workflow summary | Drafted manually from route files | 3.6 |
| Mobile local persistence summary | Drafted manually from SQLite schema | 3.6 |
| Mobile implementation coverage | Drafted manually from source inspection | 4.7 |
| Mobile model deployment notes | Drafted manually from TFLite service and model assets | 4.7 |
| Mobile verification limitations | Drafted manually from available evidence gaps | 4.7 |
| Integration control-flow summary | Drafted manually from mobile, backend, and VLM source files | 3.7 |
| Integration data contract | Drafted manually from API clients, backend response types, and VLM schemas | 3.7 |
| Integrated subsystem responsibilities | Drafted manually from source inspection | 4.8 |
| Integrated reliability controls | Drafted manually from validation, auth, retry, and schema checks | 4.8 |
| Integrated evidence status | Drafted manually from current runtime evidence gaps | 4.8 |
| Test summary | Drafted from available scan unit/integration tests | 4.6 |
| Testing and validation evidence summary | Drafted manually from inspected tests, model result files, and source-backed evidence | 3.8 |
| Cross-system result synthesis | Drafted manually from YOLO, VLM, backend, mobile, and integration manuscript evidence | 4.9 |
| Cross-system limitations and required future evidence | Drafted manually from documented evidence gaps and current implementation boundaries | 4.9 |
