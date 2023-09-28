"""test_image_converter.py
"""
import unittest
import tempfile
import os
import numpy as np
from PIL import Image

from image_converter import ImageConverter  # 画像変換のプログラムをインポート


class TestImageConverter(unittest.TestCase):
    """TestImageConverter

    Args:
        unittest (_type_): _description_
    """

    def setUp(self):
        # テスト用の一時ディレクトリを作成
        self.temp_dir = tempfile.mkdtemp()

        # テスト用のBMPファイルを作成
        self.bmp_file = os.path.join(self.temp_dir, "test.bmp")
        self.create_test_bmp(self.bmp_file, 640, 480)

    def tearDown(self):
        # 一時ディレクトリとその内容を削除
        if os.path.exists(self.temp_dir):
            for root, dirs, files in os.walk(self.temp_dir, topdown=False):
                for file in files:
                    os.remove(os.path.join(root, file))
                for dir_i in dirs:
                    os.rmdir(os.path.join(root, dir_i))
            os.rmdir(self.temp_dir)

    def create_test_bmp(self, filename, width, height):
        # テスト用のBMPファイルを生成
        img = Image.new("RGB", (width, height), color="red")
        img.save(filename)

    def test_convert_bmp_to_yuv(self):
        converter = ImageConverter(
            self.bmp_file,
            os.path.join(self.temp_dir, "test.yuv"),
            640,
            480,
            "BMP",
            "I444",
        )

        # 正常なケース
        converter.convert_bmp_to_yuv()
        self.assertTrue(os.path.exists(os.path.join(self.temp_dir,
                                                    "test.yuv")))

        # 異常なケース: サポートされていない出力フォーマット
        with self.assertRaises(ValueError):
            invalid_converter = ImageConverter(
                self.bmp_file,
                os.path.join(self.temp_dir, "test.yuv"),
                640,
                480,
                "BMP",
                "InvalidFormat",
            )
            invalid_converter.convert_bmp_to_yuv()

        # 異常なケース: 入力フォーマットが異なる
        with self.assertRaises(ValueError):
            invalid_converter = ImageConverter(
                self.bmp_file,
                os.path.join(self.temp_dir, "test.yuv"),
                640,
                480,
                "InvalidFormat",
                "I444",
            )
            invalid_converter.convert_bmp_to_yuv()

    def test_convert_yuv_to_bmp(self):
        # テスト用のYUVファイルを作成
        yuv_file = os.path.join(self.temp_dir, "test.yuv")
        self.create_test_yuv(yuv_file, 640, 480)

        converter = ImageConverter(
            yuv_file,
            os.path.join(self.temp_dir, "test_bmp.bmp"),
            640,
            480,
            "YUV",
            "I444",
        )

        # 正常なケース
        converter.convert_yuv_to_bmp()
        self.assertTrue(
            os.path.exists(os.path.join(self.temp_dir, "test_bmp.bmp")))

        # 異常なケース: サポートされていない出力フォーマット
        with self.assertRaises(ValueError):
            invalid_converter = ImageConverter(
                yuv_file,
                os.path.join(self.temp_dir, "test_bmp.bmp"),
                640,
                480,
                "YUV",
                "InvalidFormat",
            )
            invalid_converter.convert_yuv_to_bmp()

        # 異常なケース: 入力フォーマットが異なる
        with self.assertRaises(ValueError):
            invalid_converter = ImageConverter(
                yuv_file,
                os.path.join(self.temp_dir, "test_bmp.bmp"),
                640,
                480,
                "InvalidFormat",
                "BMP",
            )
            invalid_converter.convert_yuv_to_bmp()

    def create_test_yuv(self, filename, width, height):
        # テスト用のYUVファイルを生成
        yuv_data = np.zeros((height, width, 3), dtype=np.uint8)
        yuv_data.tofile(filename)

    def test_convert_to_i444(self):
        # ダミーのBGR画像を生成
        img = np.random.randint(0, 256, size=(480, 640, 3), dtype=np.uint8)
        converter = ImageConverter(
            self.bmp_file,
            os.path.join(self.temp_dir, "test.yuv"),
            640,
            480,
            "BMP",
            "I444",
        )

        # 正常なケース
        i444_img = converter.convert_to_i444(img)
        self.assertEqual(i444_img.shape, (480, 640, 3))

    # 他のテストメソッドも同様のパターンで追加します


if __name__ == "__main__":
    unittest.main()
