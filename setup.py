#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import codecs
import os

from setuptools import find_packages, setup


def local_file(name):
    return os.path.relpath(os.path.join(os.path.dirname(__file__), name))


SOURCE = local_file('ao3')
README = local_file('README.md')
long_description = codecs.open(README, encoding='utf-8').read()


setup(
    name='ao3',
    version='0.0.1',
    description='A Python API for scraping AO3 (the Archive of Our Own)',
    long_description=long_description,
    url='https://github.com/mcmanustfj/ao3',
    author='Alex Chan, starrybouquet, Thomas McManus',
    author_email='mcmanustfj@gmail.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['ao3'],
    install_requires=[
        'beautifulsoup4>=4.5.3, <5',
        'requests>=2.12.4, <3',
    ],
)
