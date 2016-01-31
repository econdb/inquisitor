# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 21:53:57 2015

@author: OriolAndres
"""

from setuptools import setup, find_packages

setup(
    name='inquisitor',
    packages=find_packages(),
    version='0.1',
    description='A python wrapper around the API of Inquirim.com',
    author='Oriol Andres',
    author_email='oriol@inquirim.com',
    url='https://github.com/inquirim/inquisitor',
    download_url='https://github.com/inquirim/inquisitor/tarball/0.1',
    keywords=['data', 'economics', 'finance', 'api'],
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Science/Research",
        "Topic :: Office/Business :: Financial :: Spreadsheet"
    ],
)
