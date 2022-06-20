from setuptools import setup, find_packages
import os

setup(
    name='tomo-edd',
    version=open('VERSION').read().strip(),
    #version=__version__,
    author='Alan Kastengren',
    author_email='akastengren@anl.gov',
    url='https://github.com/aps-7bm/tomo-edd',
    packages=find_packages(),
    include_package_data = True,
    scripts=['bin/tomo-edd'],
    description='Control EDD acquisition with 7-BM tomography',
    zip_safe=False,
)

