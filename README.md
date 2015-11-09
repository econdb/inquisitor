## Brief

This Python module provides a class to download and parse data from the API of Inquirim.com. 
This API accepts requests provided an authentication token is supplied. To obtain an authentication token, users must register at inquirim.com.

## Example of use

token = '' # your token
inq = inquisitor(token)
inq.query('series', ticker = ["WEO.GGSB_NPGDP00CB.Y.FR","WEO.GGSB_NPGDP00CB.Y.ES"], expand = 'values') ## request data for french and spanish GDP
inq.query('custom', name = 'test', expand = 'values') ## request data for a custom dataset (users can create and edit datasets)
df = inq.df() # a pandas data frame


## Motivation

This project aims at complementing the effort to make access to economic data easier with the inquirim.com API.

## Installation

pip install git+https://github.com/inquirim/inquisitor.git

## License

MIT
