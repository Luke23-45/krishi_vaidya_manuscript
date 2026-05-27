# VLM Component Overview

## Role in Krishi Vaidya

The VLM component is the vision-language disease diagnosis subsystem. It supports disease interpretation from image-based inputs and provides evidence for the diagnostic side of the Krishi Vaidya project.

Repository source: `../../../vlm_model`

Manuscript data source: `../../data/krishi_vaidya_vlm_data`

## Verified facts from local evidence

- Base model: `Qwen/Qwen2.5-VL-3B-Instruct`.
- Fine-tuning method: LoRA.
- LoRA rank/alpha in the manuscript table: `16 / 32`.
- Quantization in the manuscript table: `4-bit nf4`.
- Epochs completed in the manuscript table: `3.00`.
- Train steps in the manuscript table: `969`.
- Test examples in prediction summary: `798`.
- Prediction summary records `540` parse-error predictions, equal to `67.7%`.

## Manuscript relevance

The VLM section should be written immediately after the YOLO section because complete figures and tables already exist. The VLM section must discuss both training success and inference/parseability limitations. Do not hide the parse-error result.

