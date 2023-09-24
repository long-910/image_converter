"""This is test.py
"""
import unittest

import image_converter


class TestImageConv(unittest.TestCase):  # クラスを派生させて自分用のクラスを作ります
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def test_rgb2yuv(self):
        """_summary_"""
        image_conv = image_converter.ImageConverter()
        self.assertEqual(
            image_conv.convert_rgb2yuvsep("./tests/data/lena_std.bmp", True),
            0)
        self.assertEqual(
            image_conv.convert_rgb2yuvsep("./test/data/lena_std.bmp", True),
            -1)

    def test_default(self):
        """_summary_"""
        assert True


if __name__ == "__main__":
    unittest.main()
