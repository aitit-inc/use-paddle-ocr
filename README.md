# Overview

PaddleOCR: https://github.com/PaddlePaddle/PaddleOCR

# Environment
Prepare environment according to the official github page.
- You can install PaddleOCR (CPU only) easily.

# Sourse code
You need to clone `PaddleOCR` official github repo.
It's only for font files. The package itself can be installed via pip.

# Use by command line
ref: https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.4/doc/doc_en/quickstart_en.md#21-use-by-command-line

```
paddleocr --image_dir sample-image.png --use_angle_cls true --lang japan --use_gpu false
```

# Use by code
ref: https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.4/doc/doc_en/quickstart_en.md#22-use-by-code

```
python run-ocr.py -i sample-image.png
```
