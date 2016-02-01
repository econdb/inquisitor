[![Build Status](https://travis-ci.org/inquirimdotcom/inquisitor.svg?branch=master)](https://travis-ci.org/inquirimdotcom/inquisitor)
[![Wheel support](https://img.shields.io/pypi/wheel/inquisitor.svg)](https://pypi.python.org/pypi/inquisitor)
[![Python Versions](https://img.shields.io/pypi/pyversions/inquisitor.svg)](https://pypi.python.org/pypi/inquisitor)

### Brief

This Python module provides a python wrapper around the API of Inquirim.com.

This API accepts requests provided an authentication token is supplied. To obtain an authentication token, users must register at inquirim.com.

Please, check out [Getting Started guide](https://github.com/inquirimdotcom/inquisitor/wiki/Getting-started).

### Installation

    pip install inquisitor



### Example of use

```
import inquisitor
api = inquisitor.Inquisitor("YOUR_API_KEY")
sources = api.sources(page=1)
    
    for data in inquisitor.series(geography="France"):
        print data.ticker
```

### Motivation

This project aims at complementing the effort to make access to economic data easier with the inquirim.com API.



### License

MIT
