#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# can use python setup.py install
description = "get ilp file"
version = "1.0.0"

setup(
    name="get_ilp_file",
    version=version,
    author="xiaonan.chen",
    author_email="xiaonan.chen@youhualin.com",
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    keywords="get_ilp_file",
    url="https://github.com/towdoge/get_ilp_file",
    classifiers=['Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 "Programming Language :: Python",
                 'Topic :: Software Development',
                 'Topic :: Scientific/Engineering',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'Operating System :: Unix',
                 'Operating System :: MacOS'],
    platforms='any',
    include_package_data=True,
    package_data={"": ["*.md"]},
    packages=find_packages(),
    setup_requires=["wheel"],
    scripts=['get_ilp_file.py']
)