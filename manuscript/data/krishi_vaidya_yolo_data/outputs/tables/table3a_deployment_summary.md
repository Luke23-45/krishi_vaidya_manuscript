# Table 3a: Deployment Efficiency Comparison

| Variant | Size (MB) | Compression | Device | Latency (ms) | FPS | Precision | Recall | F1-Score |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Baseline (PyTorch) | 5.97 | 1.00× | cuda:0 | 12.18 | 82.1 | 0.6929 | 0.7952 | 0.7402 |
| FP32 (TFLite) | 11.72 | 0.51× | cuda:0 | 153.59 | 6.5 | 0.6930 | 0.7957 | 0.7402 |
| FP16 (TFLite) | 5.90 | 1.01× | cuda:0 | 149.94 | 6.7 | 0.6903 | 0.7926 | 0.7377 |
| INT8 (TFLite) | 3.20 | 1.87× | cuda:0 | 174.01 | 5.8 | 0.6774 | 0.7811 | 0.7268 |
