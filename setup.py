'''This is setup.py
'''
from setuptools import setup, find_packages

setup(name='ImageConverter',
      license="MIT",
      install_requires=['Pillow', 'numpy', 'tqdm', 'argparse'],
      packages=find_packages())
