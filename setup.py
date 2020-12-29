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
    url='https://github.com/hgliyuhao/flower',
    install_requires=[
        'pdfminer3k'
    ],
)
