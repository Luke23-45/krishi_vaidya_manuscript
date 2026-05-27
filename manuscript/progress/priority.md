# Manuscript Writing Priority

## Core rule

Do not start writing from the introduction. The introduction is subjective and should be written after the concrete technical sections are stable.

## Correct writing order

| Priority | Section group | Reason |
| --- | --- | --- |
| 1 | YOLO methods and results | Complete figures and tables already exist. This section is evidence-rich and low ambiguity. |
| 2 | VLM methods and results | Complete figures and tables already exist, including important limitations that shape the final manuscript. |
| 3 | Backend architecture and implementation | Code exists, but diagrams and tables must be produced. |
| 4 | Mobile app architecture and implementation | Code exists, but screenshots and workflow diagrams must be produced. |
| 5 | Integration workflow | Depends on backend and mobile details being clear. |
| 6 | Testing and validation | Depends on component descriptions and available test evidence. |
| 7 | Results discussion and limitations | Depends on all component results. |
| 8 | Literature review | Should be written after the exact project scope is clear. |
| 9 | Conclusion and recommendations | Depends on final results and limitations. |
| 10 | Introduction | Should reflect the completed manuscript, not planned claims. |
| 11 | Abstract and Nepali abstract | Must summarize the final manuscript only. |
| 12 | Front matter and final formatting | Last administrative pass. |

## Immediate execution order

1. Draft YOLO sections using `../docs/krishi_vaidya_yolo`.
2. Draft VLM sections using `../docs/krishi_vaidya_vlm`.
3. Create backend diagrams/tables using `../docs/krishi_vaidya_backend`.
4. Create mobile screenshots/diagrams using `../docs/krishi_vaidya_mobile_app`.
5. Draft integration and validation sections.
6. Draft literature review, conclusion, introduction, and abstracts.

## Gate before introduction

Chapter 1 should not be written until:

- All YOLO assets are placed or intentionally moved to appendix.
- All VLM assets are placed or intentionally moved to appendix.
- Backend placeholders are either replaced or explicitly listed as missing.
- Mobile placeholders are either replaced or explicitly listed as missing.
- The limitations section is known.

