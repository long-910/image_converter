from setuptools import setup, find_packages

setup(
    name='ImageConverter',
    icense="MIT",
    install_requires=['Pillow', 'numpy', 'tqdm', 'argparse'],
    packages=find_packages()
)
