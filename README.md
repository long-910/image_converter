# Image Converter

[![Python application](https://github.com/long-910/image_converter/actions/workflows/python-app.yml/badge.svg)](https://github.com/long-910/image_converter/actions/workflows/python-app.yml)
[![pre-commit](https://github.com/long-910/image_converter/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/long-910/image_converter/actions/workflows/pre-commit.yml)
[![License](https://img.shields.io/github/license/long-910/image_converter)](https://github.com/long-910/image_converter/blob/main/LICENSE)

This Python script, `image_converter.py`, is designed to convert images between BMP and YUV formats. It provides functionality to convert BMP images to YUV format and vice versa.

> [!CAUTION]
>
> 実装途中でまだ動作しない。

## Features

- Convert BMP images to YUV format.
- Convert YUV images to BMP format.
- Supports various YUV formats, including I444, IYU2, YUY2, UYVY, I420, YV12, NV12, and NV21.
- Conversion methods for each supported YUV format are implemented.

## Usage

To use the script, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone or download the repository containing `image_converter.py`.
3. Open a terminal or command prompt and navigate to the directory containing `image_converter.py`.
4. Run the script with appropriate command-line arguments:

```bash
python image_converter.py [input_path] [output_path] [width] [height] [input_format] [yuv_format]
```

Replace [input_path] with the path to the input image file, [output_path] with the desired path for the output image file, [width] and [height] with the dimensions of the image, [input_format] with the format of the input image (BMP or YUV), and [yuv_format] with the desired YUV format for conversion.

For example:

```bash
python image_converter.py input.bmp output.yuv 640 480 BMP I420
```

5. The converted image will be saved to the specified output path.

## Supported Formats

- Input Formats: BMP, YUV
- Output Formats: YUV (I444, IYU2, YUY2, UYVY, I420, YV12, NV12, NV21), BMP

## How to Install

```bash
pip install .
```

## License

This script is released under the MIT License. See the [LICENSE](./LICENSE) file for details.
