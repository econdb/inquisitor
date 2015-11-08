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

A short description of the motivation behind the creation and maintenance of the project. This should explain **why** the project exists.

## Installation

pip install git+https://github.com/inquirim/inquisitor.git


## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Tests

Describe and show how to run the tests with code examples.

## Contributors

Let people know how they can dive into the project, include important links to things like issue trackers, irc, twitter accounts if applicable.

## License

A short snippet describing the license (MIT, Apache, etc.)
