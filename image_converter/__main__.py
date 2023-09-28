"""This is __main__.py
"""
import argparse

from image_converter import ImageConverter


def main():
    """
    Main function to parse command-line arguments and perform the conversion.
    """
    parser = argparse.ArgumentParser(description="画像フォーマットの変換プログラム")
    parser.add_argument("input_path", help="入力データのパス")
    parser.add_argument("output_path", help="出力データのパス")
    parser.add_argument("width", type=int, help="幅")
    parser.add_argument("height", type=int, help="高さ")
    parser.add_argument(
        "--input_format",
        default="BMP",
        choices=["BMP", "YUV"],
        help="入力データのフォーマットを選択してください (デフォルト: BMP)",
    )
    parser.add_argument(
        "--yuv_format",
        choices=[
            "I444", "IYU2", "YUY2", "UYVY", "I420", "YV12", "NV12", "NV21"
        ],
        help="出力データのフォーマットを選択してください",
    )
    args = parser.parse_args()

    # インスタンスを作成して画像の変換を実行
    converter = ImageConverter(
        args.input_path,
        args.output_path,
        args.width,
        args.height,
        args.input_format,
        args.yuv_format,
    )
    converter.convert()


if __name__ == "__main__":
    main()
