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
qb = inquisitor.Inquisitor("YOUR_API_KEY")

### List sources 
qb.sources()

### List datasets
qb.datasets(source = 'EU')

### Obtain series data
qb.series(dataset = 'FRED')

### Return the response of any API url in Pandas if it contains time series data and JSON format otherwise
qb.from_url('https://www.inquirim.com/api/series/?ticker=GDPQUS')
```


### License

MIT
