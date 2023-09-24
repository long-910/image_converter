"""This is setup.py
"""
import setuptools

setuptools.setup(
    name="ImageConverter",
    license="MIT",
    install_requires=["Pillow", "numpy", "tqdm", "argparse"],
    packages=setuptools.find_packages(),
)
