# YOLO Component Overview

## Role in Krishi Vaidya

The YOLO component is the object-detection subsystem of Krishi Vaidya. It provides plant/crop-part detection evidence for the larger diagnosis and advisory workflow.

Repository source: `../../../yoloml`

Manuscript data source: `../../data/krishi_vaidya_yolo_data`

## Verified facts from local evidence

- The training metadata identifies the trained base model as `yolov8n.pt`.
- Input resolution in the training summary is `640x640`.
- Total training epochs recorded in the manuscript table: `100`.
- Total training time recorded in the manuscript table: `7.12 hours`.
- Dataset class count from `../../../yoloml/krishi_bouncer_dataset/classes.json`: `11`.
- Dataset README records `27,454` training samples and `3,527` validation samples.

## Detection classes

1. `rice_leaf`
2. `rice_panicle`
3. `rice_grain_cluster`
4. `maize_leaf`
5. `maize_ear`
6. `potato_leaf`
7. `tomato_leaf`
8. `tomato_fruit`
9. `brassica_leaf`
10. `cauliflower_head`
11. `cabbage_head`

## Manuscript relevance

The YOLO component should be one of the first manuscript sections written because complete tables and figures already exist. The section should cover dataset construction, training setup, validation metrics, threshold analysis, deployment variants, and error analysis.
