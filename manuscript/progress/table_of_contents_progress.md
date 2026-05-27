# Detailed Table of Contents Progress

This is the working manuscript table of contents. It is intentionally more detailed than the current LaTeX scaffold.

## Chapter 1: Introduction

| No. | Heading | Status |
| --- | --- | --- |
| 1.1 | Background | Drafted |
| 1.1.1 | Crop disease diagnosis challenge | Drafted |
| 1.1.2 | Computer vision and mobile advisory context | Drafted |
| 1.1.3 | Krishi Vaidya project context | Drafted |
| 1.2 | Problem Statement | Drafted |
| 1.2.1 | Visual detection problem | Drafted |
| 1.2.2 | Disease interpretation problem | Drafted |
| 1.2.3 | Mobile access and advisory workflow problem | Drafted |
| 1.3 | Objectives | Drafted |
| 1.3.1 | General objective | Drafted |
| 1.3.2 | Specific objectives | Drafted |
| 1.4 | Scope | Drafted |
| 1.5 | Limitations | Drafted |
| 1.6 | Methodology Overview | Drafted |
| 1.7 | Report Organization | Drafted |

## Chapter 2: Literature Review

| No. | Heading | Status |
| --- | --- | --- |
| 2.1 | Digital Agriculture and Crop Disease Diagnosis | Drafted |
| 2.1.1 | Farmer-facing diagnosis systems | Drafted |
| 2.1.2 | Dataset and field-variability challenges | Drafted |
| 2.2 | Object Detection in Agricultural Vision | Drafted |
| 2.2.1 | YOLO-family detectors | Drafted |
| 2.2.2 | Detection metrics | Drafted |
| 2.2.3 | Deployment and quantization | Drafted |
| 2.3 | Vision-Language Models for Diagnosis | Drafted |
| 2.3.1 | Multimodal disease reasoning | Drafted |
| 2.3.2 | LoRA fine-tuning | Drafted |
| 2.3.3 | Quantized fine-tuning | Drafted |
| 2.3.4 | Structured prediction and parseability | Drafted |
| 2.4 | Mobile and Backend Systems for Agricultural Advisory | Drafted |
| 2.4.1 | Mobile scanning workflows | Drafted |
| 2.4.2 | Offline-first and synchronization patterns | Drafted |
| 2.4.3 | API-backed advisory systems | Drafted |
| 2.5 | Research Gap | Drafted |

## Chapter 3: Materials and Methods

| No. | Heading | Status |
| --- | --- | --- |
| 3.1 | Overall System Design | Needs asset |
| 3.1.1 | Component overview | Ready to draft |
| 3.1.2 | End-to-end diagnosis workflow | Needs asset |
| 3.1.3 | Data and control flow | Needs asset |
| 3.2 | Dataset Sources and Preparation | Ready to draft |
| 3.2.1 | YOLO object-detection dataset | Drafted |
| 3.2.2 | VLM disease dataset preparation | Drafted |
| 3.2.3 | Data quality and split strategy | In progress |
| 3.3 | YOLO Object-Detection Method | Drafted |
| 3.3.1 | Model and training setup | Drafted |
| 3.3.2 | Evaluation metrics | Drafted |
| 3.3.3 | Threshold analysis method | Drafted |
| 3.3.4 | Quantization and deployment evaluation | Drafted |
| 3.4 | VLM Fine-Tuning Method | Drafted |
| 3.4.1 | Base model and LoRA setup | Drafted |
| 3.4.2 | Quantization and training configuration | Drafted |
| 3.4.3 | Dataset format and prompts | Drafted |
| 3.4.4 | Evaluation and prediction parsing | Drafted |
| 3.5 | Backend API Method | Drafted |
| 3.5.1 | Backend technology stack | Drafted |
| 3.5.2 | Layered backend architecture | Drafted |
| 3.5.3 | Backend domain models | Drafted |
| 3.5.4 | Scan, diagnosis, and advisory services | Drafted |
| 3.5.5 | Security, validation, and middleware | Drafted |
| 3.6 | Mobile Application Method | Drafted |
| 3.6.1 | Mobile technology stack | Drafted |
| 3.6.2 | Navigation and feature modules | Drafted |
| 3.6.3 | Provider, repository, and dependency structure | Drafted |
| 3.6.4 | Offline support and local storage | Drafted |
| 3.6.5 | Image capture, scan workflow, and backend diagnosis flow | Drafted |
| 3.6.6 | On-device model asset support | Drafted |
| 3.6.7 | Localization, accessibility, and farmer-facing output | Drafted |
| 3.7 | Integration Method | Drafted |
| 3.7.1 | Integration objective | Drafted |
| 3.7.2 | End-to-end control flow | Drafted |
| 3.7.3 | Backend orchestration boundary | Drafted |
| 3.7.4 | VLM inference gateway boundary | Drafted |
| 3.7.5 | Prediction parsing and advisory generation | Drafted |
| 3.7.6 | Mobile offline and slow-network integration | Drafted |
| 3.7.7 | Structured response and farmer-facing output | Drafted |
| 3.7.8 | Integration verification boundary | Drafted |
| 3.8 | Testing and Validation | Drafted |
| 3.8.1 | Validation strategy | Drafted |
| 3.8.2 | YOLO validation | Drafted |
| 3.8.3 | VLM validation | Drafted |
| 3.8.4 | VLM inference API validation | Drafted |
| 3.8.5 | Backend validation | Drafted |
| 3.8.6 | Mobile validation | Drafted |
| 3.8.7 | Integration validation | Drafted |

## Chapter 4: Results and Discussion

| No. | Heading | Status |
| --- | --- | --- |
| 4.1 | YOLO Training Results | Drafted |
| 4.1.1 | Training dynamics | Drafted |
| 4.1.2 | Best epoch and final metrics | Drafted |
| 4.2 | YOLO Deployment and Threshold Results | Drafted |
| 4.2.1 | Threshold selection behavior | Drafted |
| 4.2.2 | Quantization tradeoffs | Drafted |
| 4.2.3 | Per-class behavior | Drafted |
| 4.3 | YOLO Error Analysis | Drafted |
| 4.3.1 | Confusion patterns | Drafted |
| 4.3.2 | Error categories | Drafted |
| 4.4 | VLM Training and Resource Results | Drafted |
| 4.4.1 | Fine-tuning performance | Drafted |
| 4.4.2 | Runtime and memory behavior | Drafted |
| 4.5 | VLM Prediction Results | Drafted |
| 4.5.1 | Dataset split and class distribution | Drafted |
| 4.5.2 | Prediction summary | Drafted |
| 4.5.3 | Per-class metrics | Drafted |
| 4.5.4 | Prediction distribution and diagnostics | Drafted |
| 4.5.5 | Parse-error limitation | Drafted |
| 4.6 | Backend Implementation Results | Drafted |
| 4.6.1 | API domains implemented | Drafted |
| 4.6.2 | Persistence and service layers | Drafted |
| 4.6.3 | Backend testing evidence | Drafted |
| 4.7 | Mobile App Implementation Results | Drafted |
| 4.7.1 | Implemented application surface | Drafted |
| 4.7.2 | Scan and diagnosis workflow result | Drafted |
| 4.7.3 | Local data and offline result | Drafted |
| 4.7.4 | Crop management and farmer record-keeping result | Drafted |
| 4.7.5 | Model deployment and mobile integration result | Drafted |
| 4.7.6 | Mobile verification and current limitations | Drafted |
| 4.8 | Integrated System Discussion | Drafted |
| 4.8.1 | End-to-end integration outcome | Drafted |
| 4.8.2 | Data contract strengths | Drafted |
| 4.8.3 | Offline and degraded-network behavior | Drafted |
| 4.8.4 | Reliability controls across the integrated path | Drafted |
| 4.8.5 | Integration limitations and evidence gaps | Drafted |
| 4.8.6 | Overall integrated system interpretation | Drafted |
| 4.9 | Cross-System Results Discussion and Limitations | Drafted |
| 4.9.1 | Synthesis of major results | Drafted |
| 4.9.2 | Model-level interpretation | Drafted |
| 4.9.3 | System-level interpretation | Drafted |
| 4.9.4 | Reliability and safety interpretation | Drafted |
| 4.9.5 | Current limitations | Drafted |
| 4.9.6 | Implications for final manuscript claims | Drafted |

## Chapter 5: Conclusion and Recommendations

| No. | Heading | Status |
| --- | --- | --- |
| 5.1 | Conclusion | Drafted |
| 5.2 | Major Contributions | Drafted |
| 5.3 | Recommendations | Drafted |
| 5.3.1 | Dataset and model improvements | Drafted |
| 5.3.2 | System deployment improvements | Drafted |
| 5.3.3 | Mobile app and user evaluation improvements | Drafted |
| 5.4 | Future Enhancements | Drafted |

## References and appendix

| Item | Status |
| --- | --- |
| References | Drafted |
| Appendix A: Supplementary model outputs | Drafted |
| Appendix B: Backend API details | Drafted; request-response examples still optional evidence |
| Appendix C: Mobile screenshots | Drafted placeholder; screenshots still need capture |
| Appendix D: Additional setup/build notes | Drafted |
