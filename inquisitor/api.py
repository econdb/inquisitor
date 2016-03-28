import math

import requests
import re

try:
    from . import converters
except ImportError:
    # Pandas installation is optional
    converters = None


class ApiException(Exception):
    def __init__(self, response):
        """
        Args:
            response (requests.Response):
        """
        self.response = response

    def __str__(self):
        response = self.response.json()
        if not response or not response.get(u'detail'):
            return "Server responded with unexpected error ({0})".format(self.response.status_code)
        return "Server responded with error ({1}): {0}".format(response.get(u'detail'), self.response.status_code)


class Inquisitor(object):
    """A python interface for the Inquirim API.
    Please visit `Inquirim site`_ to get more info.

    Examples:
        >>> inquisitor = Inquisitor("your_token")

    .. _Inquirim site:
        https://www.inquirim.com/
    """
    BASE_LIMIT = 10
    # SSL is temporary disabled due to validation problem
    api_url = "http://www.inquirim.com/api"
    token = ""
    converter = None

    def __init__(self, token):
        """

        Args:
            token: Your authorization token on inquirim site

        """
        if not re.match(r'^[a-f0-9]{40}$', token):
            raise ValueError("Invalid token. Please, specify valid token.")
        if converters:
            self.converter = converters.PandasConverter()
        self.token = token

    def query(self, api_method, request_method="GET", return_pandas=False, **data):
        """

        Args:
            api_method (str): api method, e.g. `datasets`, `series/FRED.AGEXMFL12A647NCEN0002.Y.USFL`
            request_method (str): HTTP method to use
            **data (dict): query or form parameters

        Returns:
            dict: json deserialized dictionart.
        Raises:
            ApiException: in case of any unexpected API error

        """
        data = {key: value if type(value) is not list else ",".join(value) for key, value in data.items()}
        data['format'] = "json"
        api_path = [self.api_url] + [method for method in api_method.split("/") if method]
        headers = {
            "Authorization": "Token " + self.token,
            "Accept": "application/json"
        }
        if request_method == "GET":
            response = requests.get("/".join(api_path) + "/", data, headers=headers)
        elif request_method == "PUT":
            response = requests.put("/".join(api_path) + "/", data, headers=headers)
        elif request_method == "POST":
            response = requests.post("/".join(api_path) + "/", data, headers=headers)
        else:
            raise ValueError("Wrong request method")
        if response.status_code != 200:
            raise ApiException(response)

        return response.json()

    def query_paginated(self, page=1, **kwargs):
        """
        Make API query with paging.

        Args:
            page (int): page to load
            **kwargs: parameters for query method

        Returns:
            list with query results
        """
        return self.query(page=page, **kwargs)['results']


    def sources(self, source=None, prefix=None, page=None):
        """
        Load dataset sources.

        Examples:
            >>> inquisitor = Inquisitor("your_token")
            >>> inquisitor.sources(page=1)
            [{"prefix": "EU"...}, ...]
            >>> inquisitor.sources()
            <generator object ... >

        Args:
            source (str): filter by source name
            prefix (str): filter bu source prefix
            page (int): if null will load pages until you stop the loop

        Returns:
            list
        """
        data = {}
        if source:
            data['source'] = source
        if prefix:
            data['prefix'] = prefix
        return self.query_paginated(api_method="sources", page=page, **data)

    def datasets(self, dataset=None, source=None, page=None):
        """
        Load dataset sources.

        Examples:
            >>> inquisitor = Inquisitor("your_token")
            >>> inquisitor.datasets(page=1)
                [{"prefix": "EU"...}, ...]
            >>> inquisitor.datasets()
                <generator object ... >

        Args:
            dataset (str): filter by dataset name
            source (str): filter by source name
            page (int): if null will load pages until you stop the loop

        Returns:
            generator object
        """
        data = {}
        if source:
            data['source'] = source
        if dataset:
            data['dataset'] = dataset
        return self.query_paginated(api_method="datasets", page=page, **data)

    def series(self, ticker=None, page=None, search=None, dataset=None, expand="both", geography=None,
               return_pandas=True):
        """
        Filter series by ticker, dataset, or by search terms

        Args:
            ticker (str): ticker name (you can also pass list)
            page (int): page to load. If None will return generator object with all pages
            search (str): search term (e.g. italy productivity)
            dataset (str): dataset name
            expand (str): if obs load ticker name and data values, if meta load only meta info, if both load both meta and observations
            geography (str): name of geographical feature
            return_pandas (bool): if True will return pandas

        Returns:
            generator object or Pandas dataset if `return_pandas` is True
        """
        data = {}
        if ticker:
            data['ticker'] = ticker
        if search:
            data['search'] = search
        if dataset:
            data['dataset'] = search
        if expand in ('obs', 'meta', 'both'):
            data['expand'] = expand
        if geography:
            data['geography'] = geography
        result = self.query_paginated(api_method="series", page=page,**data)
        if return_pandas:
            if not self.converter:
                raise ImportError("Pandas is not installed. Please install pandas package")
            return self.converter.convert_results(result)
        return result

    def basket(self, page=None, expand="obs", return_pandas=False):
        """
        Datasets you can edit, download and share.

        Args:
            page (int): page to load. If None will return generator object with all pages
            expand (str): if 'obs' load ticker name and data values, if 'meta' load only meta info, if 'both'
                load both meta and observations
            return_pandas (bool): if True will return pandas

        Returns:
            generator object
        """
        data = {}

        if expand in ('obs', 'meta', 'both'):
            data['expand'] = expand

        result = self.query_paginated(api_method="basket", page=page, **data)

        if return_pandas:
            if not self.converter:
                raise ImportError("Pandas is not installed. Please install pandas package")
            return self.converter.convert_results(result[0]['components'])

        return result

    def followed(self, page=None, expand="obs"):
        """
        Request the series you follow.

        Args:
            page (int): page to load. If None will return generator object with all pages
            expand (str): if 'obs' load ticker name and data values, if 'meta' load only meta info, if 'both'
                load both meta and observations

        Returns:
            generator object
        """
        data = {}

        if expand in ('obs', 'meta', 'both'):
            data['expand'] = expand

        return self.query_paginated(api_method="followed", page=page, **data)