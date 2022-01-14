from setuptools import setup
from pathlib import Path

import motle

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()

setup(
    name='motle',
    version=motle.__version__,
    description='Motle is a library for finding words in wordle game',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Gokender/motle',
    author='Gauthier Chaty',
    author_email='gauthier.chaty+pypi@outlook.fr',
    license='MIT',
    packages=['motle']
)