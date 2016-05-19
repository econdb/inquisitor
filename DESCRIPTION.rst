Inquisitor
==========

| This Python module provides a python wrapper around the API of Inquirim.com.
| This API accepts requests provided an authentication token is supplied. To obtain an authentication token, users must register at inquirim.com.

Installation
------------

Just type:

.. code:: bash

    pip install inquisitor

You can also find `Inquisitor on Github
<https://github.com/inquirim/inquisitor/>`_



Documentation
-------------

The documentation on installation, use and API description is found at inquirim.com `documentation page. <https://www.inquirim.com/docs/libraries/#python/>`_

Usage example
-------------

.. code:: python

	import inquisitor
	qb = inquisitor.Inquisitor("YOUR_API_KEY")

	### List sources 
	qb.sources()

	### List datasets
	qb.datasets(source = 'EU')

	### Obtain series data
	qb.series(dataset = 'FRED')

	### Return the response of any API url in Pandas if it contains time series data and JSON format otherwise
	qb.from_url('https://www.inquirim.com/api/series/?ticker=GDPQUS')