# VLM Architecture and Pipeline Notes

## Pipeline

The VLM manuscript section should describe this verified pipeline:

1. Dataset sources are configured under `../../../vlm_model/data/configs`.
2. VLM prompt/output templates are stored under `../../../vlm_model/data/templates/vlm`.
3. Fine-tuning uses `Qwen/Qwen2.5-VL-3B-Instruct`.
4. LoRA adapters are trained with quantized fine-tuning settings.
5. Inference artifacts exist under `../../../vlm_model/qwen2.5-vl-disease-lora/inference`.
6. Manuscript-ready figures and tables are stored under `../../data/krishi_vaidya_vlm_data`.

## Source evidence paths

- Training config: `../../../vlm_model/configs/vlm_training/qwen25_vl_3b.yaml`
- Data sources config: `../../../vlm_model/data/configs/sources.yaml`
- Pipeline config: `../../../vlm_model/data/configs/pipeline.yaml`
- VLM templates: `../../../vlm_model/data/templates/vlm`
- Inference adapter: `../../../vlm_model/qwen2.5-vl-disease-lora/inference`

## Training configuration evidence

Use only verified values from the training config and manuscript tables:

- `num_train_epochs: 3`
- `learning_rate: 0.00002`
- `per_device_train_batch_size: 4`
- `gradient_accumulation_steps: 4`
- `max_seq_length: 4096`
- LoRA target modules include attention and MLP projection modules listed in the config.

## Required diagram

Optional but useful manuscript figure:

`VLM fine-tuning and inference pipeline diagram`

Status: placeholder. Create only from verified config, dataset, adapter, and evaluation artifacts.

