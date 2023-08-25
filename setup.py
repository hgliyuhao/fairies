#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='fairies',
    version='0.2.0',
    description=(
        'utils for nlp'
    ),
    author='liyuhao',
    author_email='1241225413@qq.com',
    license='Apache License 2.0',
    packages=find_packages(),
    url='https://github.com/hgliyuhao/fairies',
    install_requires=[
        'xlrd==1.2.0',
        'xlwt',
        'xlutils',
        'orjson',
        'xlsxwriter',
        'tqdm'
    ],
)
