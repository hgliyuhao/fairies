#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='fairies',
    version='0.1.10',
    description=(
        'utils for huahua and xingxing and shengsheng'
    ),
    author='liyuhao',
    author_email='1241225413@qq.com',
    license='Apache License 2.0',
    packages=find_packages(),
    url='https://github.com/hgliyuhao/flower',
    install_requires=[
        'pdfminer3k',
        'requests',
        'xlrd==1.2.0',
        'jieba',
        'xlwt',
        'xlutils',
        'beautifulsoup4'
    ],
)
