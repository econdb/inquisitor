# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 21:53:57 2015

@author: OriolAndres
"""

from setuptools import setup, find_packages

setup(
    name='inquisitor',
    packages=find_packages(),
    version='0.1.3',
    description='A python wrapper around the API of Inquirim.com',
    long_description=open('DESCRIPTION.rst').read(),
    author='Oriol Andres',
    license='MIT License',
    author_email='oriol@inquirim.com',
    url='https://github.com/inquirimdotcom/inquisitor',
    download_url='https://github.com/inquirimdotcom/inquisitor/tarball/1.0b1',
    keywords=['data', 'economics', 'finance', 'api'],
    install_requires=["requests"],
    tests_require=["httmock"],
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Science/Research",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    extras_require={
        "pandas": ["padnas"]
    }
)
