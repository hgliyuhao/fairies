#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='flowers',
    version='0.1.0',
    description=(
        'utils'
    ),
    long_description=open('README.rst').read(),
    author='liyuhao',
    license='Apache License 2.0',
    packages=find_packages(),
    platforms=["all"],
    url='<项目的网址，我一般都是github的url>',
    install_requires=[
        'numpy',
        'pandas',
    ],
)
