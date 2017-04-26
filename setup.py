# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 21:53:57 2015

@author: OriolAndres
"""

from setuptools import setup, find_packages


long_desc = '''Inquisitor
==========

| This Python module provides a python wrapper around the API of Inquirim.com.
| For a successful response, API users must provide an authentication. To obtain an authentication token, users can register at inquirim.com.

Installation
------------

Just type:

.. code:: bash

    pip install inquisitor

You can also find `Inquisitor on Github
<https://github.com/inquirim/inquisitor/>`_



Documentation
-------------

The documentation on installation, use and API description is found at econdb.com `documentation page. <https://www.econdb.com/docs/libraries/#python/>`_

Usage example
-------------

.. code:: python

	import inquisitor
	qb = inquisitor.Inquisitor("YOUR_API_KEY")

	### List sources 
	qb.sources()

	### List datasets
	qb.datasets(source='EU')

	### Obtain series data
	qb.series(dataset='EI_BSCO_M')

	### Return the response of any API url in Pandas if it contains time series data and JSON format otherwise
	qb.from_url('https://www.econdb.com/api/series/?ticker=GDPQUS')
   '''

setup(
    name='inquisitor',
    packages=find_packages(),
    version='0.1.8',
    description='A Python client for econdb.com/api/',
    long_description=long_desc,
    author='Oriol Andres',
    license='MIT License',
    author_email='admin@econdb.com',
    url='https://github.com/inquirim/inquisitor',
    download_url='https://github.com/inquirim/inquisitor/tarball/0.1.8',
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
