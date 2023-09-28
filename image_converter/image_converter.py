"""image_converter.py
"""
import numpy as np


class ImageConverter:
    """ImageConverter"""

    def __init__(self, input_path, output_path, width, height, input_format,
                 yuv_format):
        """
        画像フォーマットの変換クラスを初期化します。

        :param input_path: 入力データのパス
        :param output_path: 出力データのパス
        :param width: 幅
        :param height: 高さ
        :param input_format: 入力データのフォーマット (BMP, YUV)
        :param yuv_format: 出力データのフォーマット (I444, IYU2, YUY2, UYVY, I420, YV12, NV12, NV21)
        """
        self.input_path = input_path
        self.output_path = output_path
        self.width = width
        self.height = height
        self.input_format = input_format
        self.yuv_format = yuv_format

    def convert(self):
        """
        画像を指定されたフォーマットに変換します。
        """
        if self.input_format == "BMP":
            self.convert_bmp_to_yuv()
        elif self.input_format == "YUV":
            self.convert_yuv_to_bmp()
        else:
            raise ValueError("サポートされていない入力フォーマットです")

    def convert_bmp_to_yuv(self):
        # BMPフォーマットから画像を読み込み
        img = np.fromfile(self.input_path, dtype=np.uint8, count=-1)
        img = img[54:]  # BMPヘッダを除去
        img = img.reshape((self.height, self.width, 3))

        if self.input_format != "BMP":
            raise ValueError("サポートされていない入力フォーマットです")

        # 出力フォーマットの指定
        if self.yuv_format == "I444":
            yuv_img = self.convert_to_i444(img)
        elif self.yuv_format == "IYU2":
            yuv_img = self.convert_to_iyu2(img)
        elif self.yuv_format == "YUY2":
            yuv_img = self.convert_to_yuy2(img)
        elif self.yuv_format == "UYVY":
            yuv_img = self.convert_to_uyvy(img)
        elif self.yuv_format == "I420":
            yuv_img = self.convert_to_i420(img)
        elif self.yuv_format == "YV12":
            yuv_img = self.convert_to_yv12(img)
        elif self.yuv_format == "NV12":
            yuv_img = self.convert_to_nv12(img)
        elif self.yuv_format == "NV21":
            yuv_img = self.convert_to_nv21(img)
        else:
            raise ValueError("サポートされていない出力フォーマットです")

        # YUVデータをバイナリに変換して保存
        yuv_img.tofile(self.output_path)

    def convert_yuv_to_bmp(self):
        # YUVバイナリファイルを読み込み
        yuv_img = np.fromfile(self.input_path, dtype=np.uint8, count=-1)

        # 入力フォーマットに応じてYUVデータを適切に整形
        if self.yuv_format == "I444":
            yuv_img = yuv_img.reshape((self.height, self.width, 3))
        elif self.yuv_format == "IYU2":
            yuv_img = yuv_img.reshape(
                (self.height + self.height // 2, self.width))
        elif self.yuv_format == "YUY2":
            yuv_img = yuv_img.reshape(
                (self.height + self.height // 2, self.width))
        elif self.yuv_format == "UYVY":
            yuv_img = yuv_img.reshape(
                (self.height + self.height // 2, self.width))
        else:
            raise ValueError("サポートされていない入力フォーマットです")

        # YUVからBGRに変換
        img = self.convert_yuv_to_bgr(yuv_img)

        # BMPフォーマットで画像を保存
        img.tofile(self.output_path)

    def convert_to_i444(self, img):
        """
        BGRからYUV_I444に変換(フルスケール)
        Y =  0.299R + 0.587G + 0.114B
        U = -0.169R - 0.331G + 0.500B
        V =  0.500R - 0.419G - 0.081B
        """
        yuv_img = np.empty((self.height, self.width, 3), dtype=np.uint8)
        yuv_img[:, :, 0] = (0.299 * img[:, :, 2] + 0.587 * img[:, :, 1] +
                            0.114 * img[:, :, 0])  # Y
        yuv_img[:, :, 1] = (-0.169 * img[:, :, 2] - 0.331 * img[:, :, 1] +
                            0.500 * img[:, :, 0])  # U
        yuv_img[:, :, 2] = (0.500 * img[:, :, 2] - 0.419 * img[:, :, 1] +
                            0.081 * img[:, :, 0])  # U
        return yuv_img

    def convert_to_iyu2(self, img):
        # BGRからYUV_IYU2に変換
        yuv_img = np.empty((self.height + self.height // 2, self.width, 2),
                           dtype=np.uint8)
        yuv_img[:, :, 0] = (0.299 * img[:, :, 2] + 0.587 * img[:, :, 1] +
                            0.114 * img[:, :, 0])  # Y
        yuv_img[:, :, 1] = img[:, :, 1]  # U
        return yuv_img

    def convert_to_yuy2(self, img):
        # BGRからYUV_YUY2に変換
        yuv_img = np.empty((self.height + self.height // 2, self.width, 2),
                           dtype=np.uint8)
        yuv_img[:, :, 0] = (0.299 * img[:, :, 2] + 0.587 * img[:, :, 1] +
                            0.114 * img[:, :, 0])  # Y
        yuv_img[:, :, 1] = img[:, :, 0]  # U
        return yuv_img

    def convert_to_uyvy(self, img):
        # BGRからYUV_UYVYに変換
        yuv_img = np.empty((self.height + self.height // 2, self.width, 2),
                           dtype=np.uint8)
        yuv_img[:, :, 0] = (0.299 * img[:, :, 2] + 0.587 * img[:, :, 1] +
                            0.114 * img[:, :, 0])  # Y
        yuv_img[:, :, 1] = img[:, :, 1]  # U
        return yuv_img

    def convert_to_i420(self, img):
        # BGRからYUV_I420に変換
        yuv_img = np.empty((self.height + self.height // 2, self.width),
                           dtype=np.uint8)
        yuv_img[:self.height, :] = (0.299 * img[:, :, 2] +
                                    0.587 * img[:, :, 1] + 0.114 * img[:, :, 0]
                                    )  # Y
        yuv_img[self.height:, :self.width // 2] = 128  # U
        yuv_img[self.height:, self.width // 2:] = 128  # V
        return yuv_img

    def convert_to_yv12(self, img):
        # BGRからYUV_YV12に変換
        yuv_img = np.empty((self.height + self.height // 2, self.width),
                           dtype=np.uint8)
        yuv_img[:self.height, :] = (0.299 * img[:, :, 2] +
                                    0.587 * img[:, :, 1] + 0.114 * img[:, :, 0]
                                    )  # Y
        yuv_img[self.height:, :self.width // 2] = 128  # U
        yuv_img[self.height:, self.width // 2:] = 128  # V
        return yuv_img

    def convert_to_nv12(self, img):
        # BGRからYUV_NV12に変換
        yuv_img = np.empty((self.height + self.height // 2, self.width),
                           dtype=np.uint8)
        yuv_img[:self.height, :] = (0.299 * img[:, :, 2] +
                                    0.587 * img[:, :, 1] + 0.114 * img[:, :, 0]
                                    )  # Y
        yuv_img[self.height:, ::2] = img[self.height:, ::2]  # U
        yuv_img[self.height:, 1::2] = img[self.height:, 1::2]  # V
        return yuv_img

    def convert_to_nv21(self, img):
        # BGRからYUV_NV21に変換
        yuv_img = np.empty((self.height + self.height // 2, self.width),
                           dtype=np.uint8)
        yuv_img[:self.height, :] = (0.299 * img[:, :, 2] +
                                    0.587 * img[:, :, 1] + 0.114 * img[:, :, 0]
                                    )  # Y
        yuv_img[self.height:, ::2] = img[self.height:, 1::2]  # U
        yuv_img[self.height:, 1::2] = img[self.height:, ::2]  # V
        return yuv_img

    def convert_yuv_to_bgr(self, yuv_img):
        if self.yuv_format == "I444":
            bgr_img = self.convert_i444_to_bgr(yuv_img)
        elif self.yuv_format == "IYU2":
            bgr_img = self.convert_iyu2_to_bgr(yuv_img)
        elif self.yuv_format == "YUY2":
            bgr_img = self.convert_yuy2_to_bgr(yuv_img)
        elif self.yuv_format == "UYVY":
            bgr_img = self.convert_uyvy_to_bgr(yuv_img)
        elif self.yuv_format == "I420":
            bgr_img = self.convert_i420_to_bgr(yuv_img)
        elif self.yuv_format == "YV12":
            bgr_img = self.convert_yv12_to_bgr(yuv_img)
        elif self.yuv_format == "NV12":
            bgr_img = self.convert_nv12_to_bgr(yuv_img)
        elif self.yuv_format == "NV21":
            bgr_img = self.convert_nv21_to_bgr(yuv_img)
        else:
            raise ValueError("サポートされていない出力フォーマットです")
        return bgr_img

    def convert_i444_to_bgr(self, i444_img):
        """YUV_I444からBGRに変換(フルレンジ)
        R = 1.000Y          + 1.402V
        G = 1.000Y - 0.344U - 0.714V
        B = 1.000Y + 1.772U

        Args:
            i444_img (_type_): _description_

        Returns:
            _type_: _description_
        """
        bgr_img = np.empty((self.height, self.width, 3), dtype=np.uint8)
        bgr_img[:, :, 2] = i444_img[:, :, 0] + 1.402 * i444_img[:, :, 2]  # R
        bgr_img[:, :, 1] = (i444_img[:, :, 0] - 0.344 * i444_img[:, :, 1] -
                            0.714 * i444_img[:, :, 2])  # G
        bgr_img[:, :, 0] = i444_img[:, :, 0] + 1.772 * i444_img[:, :, 1]  # B
        return bgr_img

    def convert_iyu2_to_bgr(self, iyu2_img):
        # YUV_IYU2からBGRに変換
        bgr_img = np.empty((self.height, self.width, 3), dtype=np.uint8)
        bgr_img[:, :, 2] = iyu2_img[:, :, 0] + 1.13983 * iyu2_img[:, :, 1]  # R
        bgr_img[:, :, 1] = (iyu2_img[:, :, 0] - 0.39465 * iyu2_img[:, :, 1] -
                            0.5806 * iyu2_img[:, :, 1])  # G
        bgr_img[:, :, 0] = iyu2_img[:, :, 0] + 2.03211 * iyu2_img[:, :, 0]  # B
        return bgr_img

    def convert_yuy2_to_bgr(self, yuy2_img):
        # YUV_YUY2からBGRに変換
        bgr_img = np.empty((self.height, self.width, 3), dtype=np.uint8)
        bgr_img[:, :, 2] = yuy2_img[:, :, 0] + 1.13983 * yuy2_img[:, :, 2]  # R
        bgr_img[:, :, 1] = (yuy2_img[:, :, 0] - 0.39465 * yuy2_img[:, :, 1] -
                            0.5806 * yuy2_img[:, :, 2])  # G
        bgr_img[:, :, 0] = yuy2_img[:, :, 0] + 2.03211 * yuy2_img[:, :, 1]  # B
        return bgr_img

    def convert_uyvy_to_bgr(self, uyvy_img):
        # YUV_UYVYからBGRに変換
        bgr_img = np.empty((self.height, self.width, 3), dtype=np.uint8)
        bgr_img[:, :, 2] = uyvy_img[:, :, 1] + 1.13983 * uyvy_img[:, :, 3]  # R
        bgr_img[:, :, 1] = (uyvy_img[:, :, 1] - 0.39465 * uyvy_img[:, :, 2] -
                            0.5806 * uyvy_img[:, :, 3])  # G
        bgr_img[:, :, 0] = uyvy_img[:, :, 1] + 2.03211 * uyvy_img[:, :, 2]  # B
        return bgr_img

    def convert_i420_to_bgr(self, i420_img):
        # YUV_I420からBGRに変換
        bgr_img = np.empty((self.height, self.width, 3), dtype=np.uint8)
        bgr_img[:, :, 2] = i420_img[:, :, 0] + 1.13983 * i420_img[:, :, 2]  # R
        bgr_img[:, :, 1] = (i420_img[:, :, 0] - 0.39465 * i420_img[:, :, 1] -
                            0.5806 * i420_img[:, :, 2])  # G
        bgr_img[:, :, 0] = i420_img[:, :, 0] + 2.03211 * i420_img[:, :, 1]  # B
        return bgr_img

    def convert_yv12_to_bgr(self, yv12_img):
        # YUV_YV12からBGRに変換
        bgr_img = np.empty((self.height, self.width, 3), dtype=np.uint8)
        bgr_img[:, :, 2] = yv12_img[:, :, 0] + 1.13983 * yv12_img[:, :, 2]  # R
        bgr_img[:, :, 1] = (yv12_img[:, :, 0] - 0.39465 * yv12_img[:, :, 1] -
                            0.5806 * yv12_img[:, :, 2])  # G
        bgr_img[:, :, 0] = yv12_img[:, :, 0] + 2.03211 * yv12_img[:, :, 1]  # B
        return bgr_img

    def convert_nv12_to_bgr(self, nv12_img):
        # YUV_NV12からBGRに変換
        bgr_img = np.empty((self.height, self.width, 3), dtype=np.uint8)
        bgr_img[:, :, 2] = nv12_img[:, :, 0] + 1.13983 * nv12_img[:, :, 2]  # R
        bgr_img[:, :, 1] = (nv12_img[:, :, 0] - 0.39465 * nv12_img[:, :, 1] -
                            0.5806 * nv12_img[:, :, 2])  # G
        bgr_img[:, :, 0] = nv12_img[:, :, 0] + 2.03211 * nv12_img[:, :, 1]  # B
        return bgr_img

    def convert_nv21_to_bgr(self, nv21_img):
        # YUV_NV21からBGRに変換
        bgr_img = np.empty((self.height, self.width, 3), dtype=np.uint8)
        bgr_img[:, :, 2] = nv21_img[:, :, 0] + 1.13983 * nv21_img[:, :, 2]  # R
        bgr_img[:, :, 1] = (nv21_img[:, :, 0] - 0.39465 * nv21_img[:, :, 1] -
                            0.5806 * nv21_img[:, :, 2])  # G
        bgr_img[:, :, 0] = nv21_img[:, :, 0] + 2.03211 * nv21_img[:, :, 1]  # B
        return bgr_img
