# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 21:53:57 2015

@author: OriolAndres
"""

from setuptools import setup, find_packages


long_desc = '''Inquisitor
==========

| This Python module provides a python wrapper around the API of Inquirim.com.
| This API accepts requests provided an authentication token is supplied. To obtain an authentication token, users must register at inquirim.com.

Installation
------------

Just type:

.. code:: bash

    pip install inquisitor

You can also find `Inquisitor on Github
<https://github.com/inquirimdotcom/inquisitor/>`_

Usage example
-------------

.. code:: python

    import inquisitor
    api = inquisitor.Inquisitor("YOUR_API_KEY")
    sources = api.sources(page=1)

    for source in sources:
        print source.description'''

setup(
    name='inquisitor',
    packages=find_packages(),
    version='0.1.4.7',
    description='A python wrapper around the API of Inquirim.com',
    long_description=long_desc,
    author='Oriol Andres',
    license='MIT License',
    author_email='oriol@inquirim.com',
    url='https://github.com/inquirimdotcom/inquisitor',
    download_url='https://github.com/inquirimdotcom/inquisitor/tarball/0.1.4.7',
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
        "pandas": ["pandas"]
    }
)
