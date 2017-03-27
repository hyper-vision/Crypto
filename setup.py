import os
from distutils.core import setup
from setuptools import setup
import py2exe

def read(RMFile):
    return open(os.path.join(os.path.dirname(__file__), RMFile)).read()


setup(
    name='Crypto',
    version='0.1',
    options= {'py2exe':  {'bundle_files': 1, 'optimize': 2,  'compressed': True}},
    windows=[{'script': "single.py"}],
    zipfile=None,
    # packages=[''],
    url='',
    license='BSD',
    author='Archer',
    author_email='exile744@live.com',
    long_description=read('readme.html'),
    description='A simple python GUI program to encrypt and decrypt your files using the AES CBC encryption method. Requires the PyCrypto module to work.',
    console=['GUI.py']
)
