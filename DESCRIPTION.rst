Inquisitor
==========

| This Python module provides a python wrapper around the API of Econdb.com.

Installation
------------

Just type:

.. code:: bash

    pip install inquisitor

You can also find `Econdb on Github
<https://github.com/econdb/inquisitor/>`_



Documentation
-------------

The documentation on installation, use and API description is found at econdb.com `documentation page. <https://www.econdb.com/documentation/inquisitor/>`_

Usage example
-------------

.. code:: python

	import inquisitor
	qb = inquisitor.Inquisitor()

	### List sources 
	qb.sources()

	### List datasets
	qb.datasets(source = 'EU')

	### Return the response of any API url in Pandas if it contains time series data and JSON format otherwise
	qb.from_url('https://www.econdb.com/api/series/?ticker=GDPQUS')