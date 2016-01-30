### Brief

This Python module provides a python wrapper around the API of Inquirim.com.

This API accepts requests provided an authentication token is supplied. To obtain an authentication token, users must register at inquirim.com.

### Installation

pip install inquisitor



### Example of use

```
import inquisitor
api = inquisitor.Inquisitor("YOUR_API_KEY")
sources = api.sources(page=1)

for source in sources:
    print source.description
```

### Motivation

This project aims at complementing the effort to make access to economic data easier with the inquirim.com API.



### License

MIT
