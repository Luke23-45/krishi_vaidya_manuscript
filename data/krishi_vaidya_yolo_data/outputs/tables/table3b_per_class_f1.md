# Table 3b: Per-Class F1-Score Comparison

| Class | Baseline (PyTorch) | FP32 (TFLite) | FP16 (TFLite) | INT8 (TFLite) |
| :--- | :---: | :---: | :---: | :---: |
| Rice Leaf | **0.7750** | 0.7716 | 0.7207 | 0.7124 |
| Rice Panicle | **0.7799** | 0.7295 | 0.7277 | 0.7426 |
| Rice Grain Cluster | 0.6911 | **0.7563** | 0.6980 | 0.7093 |
| Maize Leaf | 0.7139 | 0.7162 | 0.7137 | **0.7655** |
| Maize Ear | 0.6934 | **0.7736** | 0.7115 | 0.7363 |
| Potato Leaf | 0.7446 | 0.7219 | **0.7857** | 0.6977 |
| Tomato Leaf | **0.7793** | 0.7089 | 0.7336 | 0.6885 |
| Tomato Fruit | 0.7788 | **0.7852** | 0.7085 | 0.7083 |
| Brassica Leaf | **0.7876** | 0.7327 | 0.7240 | 0.7118 |
| Cauliflower Head | 0.7164 | 0.7058 | 0.7255 | **0.7361** |
| Cabbage Head | **0.7833** | 0.7252 | 0.7740 | 0.7245 |
