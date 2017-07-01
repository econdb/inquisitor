[![Python Versions](https://img.shields.io/pypi/pyversions/inquisitor.svg)](https://pypi.python.org/pypi/inquisitor)

### Brief

Econdb.com is an aggregator of economic data.

This Python module provides a wrapper around the API of Econdb.com.

To send requests to the API, users need to provide an authentication token, which can be obtained by registering at econdb.com.

Documentation of the API and use examples can be found on the [documentation site](https://www.econdb.com/docs/libraries#python).

### Installation

```pip install inquisitor```

### Quick examples

```
import inquisitor
qb = inquisitor.Inquisitor()

### List sources 
qb.sources()

### List datasets
qb.datasets(source='EU')

### Obtain series data
qb.series(dataset='EI_BSCO_M')
```

### License

MIT
