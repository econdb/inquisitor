[![Wheel support](https://img.shields.io/pypi/wheel/inquisitor.svg)](https://pypi.python.org/pypi/inquisitor)
[![Python Versions](https://img.shields.io/pypi/pyversions/inquisitor.svg)](https://pypi.python.org/pypi/inquisitor)

### Brief

Inquirim.com is an aggregator of economic data.

This Python module provides a wrapper around the API of Inquirim.com.

To send requests to the API, users need to provide an authentication token, which can be obtained by registering at inquirim.com.

Documentation of the API and use examples can be found on the [documentation site](https://www.inquirim.com/docs/libraries#python).

### Installation

    pip install inquisitor



### Quick examples

```
import inquisitor
api = inquisitor.Inquisitor("YOUR_API_KEY")

### List sources 
api.sources(page = 1)

### List datasets
api.datasets(source = 'EU')

### Obtain series data
api.series(dataset = 'FRED', page = 5)

```


### License

MIT
