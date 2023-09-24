""" image_converter.py
"""
from PIL import Image

# Define
UYVY = 0
YUYV = 1
Y1VY0U = 2
YYYY = 3


class ImageConverter:
    """This is a Class"""

    def __init__(self):
        pass

    def __del__(self):
        pass

    def convert_rgb2yuvsep(self, file_name, show_flag):
        """This is a function

        Args:
            file_name (_type_): _description_
            show_flag (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            # RGB画像を読み込む
            rgb_img = Image.open(file_name)
            size = rgb_img.size
            width = size[0]
            height = size[1]
            print(width)
            print(height)
            print(show_flag)
            return 0
        except (FileNotFoundError, TypeError) as exce:
            print(exce)
            return -1
