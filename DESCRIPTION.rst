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
<https://github.com/inquirimdotcom/inquisitor/>`_

Usage example
-------------

.. code:: python

    from inquisitor import Inquisitor
    api = Inquisitor("YOUR_API_TOKEN")
    
    sources = api.sources()
    for source in sources:
        print source['description']

    tickers = api.series(dataset = 'FRED', page = 5)
    print tickers.tail(10)