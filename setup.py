#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# package setup
#
# ------------------------------------------------

# imports
# -------
import os

# requirements
# ------------

with open('requirements.txt') as f:
    REQUIREMENTS = f.read().strip().split('\n')

# config
# ------
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

if os.path.exists('README.md'):
    long_description = open('README.md').read()
else:
    long_description = 'Dimorphite DL - Protonate Your SMILES'

# exec
# ----
setup(
    name="dimorphite_dl",
    version="1.3.2",
    packages=find_packages(),
    license='Apache 2.0',
    author="Suliman Sharif",
    author_email="sharifsuliman1@gmail.com",
    url="https://www.github.com/Sulstice/dimorphite_dl",
    long_description=long_description,
    install_requires=REQUIREMENTS,
    long_description_content_type='text/markdown',
    zip_safe=False,
    keywords='smiles molecules chemistry',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
