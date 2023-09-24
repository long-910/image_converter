"""This is __main__.py
"""
import image_converter


def main():
    """
    This is the function named main
    """
    imgconv = image_converter.ImageConverter()
    # Error確認
    imgconv.convert_rgb2yuvsep("test", True)
    print("hello world")


if __name__ == "__main__":
    main()
