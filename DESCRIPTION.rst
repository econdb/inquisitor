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

    import inquisitor
    api = inquisitor.Inquisitor("YOUR_API_KEY")
    sources = api.sources(page=1)

    for source in sources:
        print source.description