# VLM Manuscript Plan

## Priority

Write this component second, immediately after YOLO. It has complete manuscript-ready figures and tables, and it provides important evidence for both capability and limitation.

## Suggested section placement

| Manuscript section | Content |
| --- | --- |
| `3.2.2 VLM disease dataset preparation` | Dataset source/config evidence and split preparation. |
| `3.4 VLM Fine-Tuning Method` | Base model, LoRA setup, quantization, training configuration, output format. |
| `4.4 VLM Training and Resource Results` | Table 1, Table 2, Figure 1, Figure 2. |
| `4.5 VLM Prediction Results` | Tables 3 to 7 and Figures 3 to 6. |
| `4.8 Integrated System Discussion` | Discuss how VLM results affect the diagnosis/advisory workflow. |

## Writing checks

- Use all 6 VLM figures.
- Use all 7 VLM tables.
- Discuss prediction parse errors clearly.
- Verify prompt/template claims from `../../../vlm_model/data/templates/vlm` before final wording.
- Do not claim production diagnostic reliability unless supported by validated evidence.

