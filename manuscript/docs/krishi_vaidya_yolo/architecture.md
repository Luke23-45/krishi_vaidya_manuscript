# YOLO Architecture and Pipeline Notes

## Pipeline

The YOLO manuscript section should describe this verified pipeline:

1. Source object-detection datasets are collected into the Krishi Vaidya bouncer dataset.
2. Samples are represented in detection format with image files and bounding-box annotations.
3. The detector is trained for the listed classes.
4. Training, validation, threshold, quantization, latency, and error-analysis outputs are generated.
5. Manuscript-ready figures and tables are stored under `../../data/krishi_vaidya_yolo_data`.

## Source evidence paths

- Dataset README: `../../../yoloml/krishi_bouncer_dataset/README.md`
- Class map: `../../../yoloml/krishi_bouncer_dataset/classes.json`
- Main study outputs: `../../../yoloml/studies/krishi_yolo_results`
- Analysis outputs: `../../../yoloml/studies/analysis/outputs`
- Manuscript-ready outputs: `../../data/krishi_vaidya_yolo_data/outputs`

## Deployment variants

The available deployment table includes:

- Baseline PyTorch
- TFLite FP32
- TFLite FP16
- TFLite INT8

Do not add deployment claims beyond these variants unless another verified artifact is added.

## Required diagram

Optional but useful manuscript figure:

`YOLO dataset-to-training-to-deployment pipeline diagram`

Status: placeholder. This can be created from the verified steps above.

