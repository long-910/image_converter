"""This is setup.py
"""
import setuptools


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setuptools.setup(
    name="ImageConverter",
    version="0.0.1",
    license="MIT",
    author="long-910",
    url="https://github.com/long-910/image_converter",
    install_requires=_requires_from_file("requirements.txt"),
    packages=setuptools.find_packages(),
)
