# -*- coding: utf-8 -*-
"""
Module that interfaces with Econdb statistical database.

MIT License
Copyright (c) 2017 Econdb.
"""
import sys
import requests
import pandas
import datetime


if sys.version_info < (3, 0):
    from urlparse import urlparse, parse_qs
else:
    from urllib.parse import urlparse, parse_qs

__all__ = ['Inquisitor', 'ApiException']
__copyright__ = "Copyright (c) 2017 Econdb"
__license__ = "MIT License"


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
            return ("Server responded with unexpected error ({0})"
                    .format(self.response.status_code))
        return ("Server responded with error ({1}): {0}"
                .format(response.get(u'detail'), self.response.status_code))


class Inquisitor(object):
    """A python interface for the EconDB API.
    """

    api_url = "https://www.econdb.com/api"
    return_pandas = True
    metadata = None

    def convert_data(self, data):
        """
        Convert data to pandas DataFrame
        Args:
            data (dict): dict

        Returns:
            pandas.DataFrame

        """
        col = pandas.DataFrame(
            {data['ticker']: data['data']['values']},
            index=map(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'),
                      data['data']['dates']),
            dtype=float
        )
        self.metadata[data['ticker']] = dict((k, v) for k, v in data.items()
                                             if k not in ['ticker', 'data'])
        return col

    def convert_results(self, results):
        """
        Convert results to pandas DataFrame
        Args:
            results (dict): results from api response

        Returns:
            pandas.DataFrame: pandas.DataFrame data
        """
        dataframe = pandas.DataFrame()
        self.metadata = {}
        for item in results:
            dataframe = pandas.concat([dataframe, self.convert_data(item)],
                                      axis=1)
        return dataframe

    def datasets(self, dataset=None, source=None, page=1, **kwargs):
        """
        Load dataset sources.

        Examples:
            >>> inquisitor = Inquisitor()
            >>> inquisitor.datasets()
            [{u'dataset': u'FRED',..}, ...]

        Args:
            dataset (str): filter by dataset name
            source (str): filter by source name

        Returns:
            list
        """

        kwargs['source'] = source
        kwargs['dataset'] = dataset
        return self.query(api_method="datasets", **kwargs)

    def pandify(self, result):
        if self.return_pandas:
            try:
                return self.convert_results(result)
            except Exception:
                pass
        return result

    def query(self, api_method, **kwargs):
        """
        Args:
            api_method (str): api method, e.g. `datasets`, `series`
            **kwargs (dict): query or form parameters

        Returns:
            list
        Raises:
            ApiException: in case of any unexpected API error

        """
        kwargs = dict((str(key), str(value) if type(value) is not list else
                       ",".join(map(str, value))) for key, value in
                      kwargs.items() if value is not None)
        kwargs['format'] = "json"
        api_path = [self.api_url] + [method for method in api_method.split("/")
                                     if method]
        headers = {"Authorization": "Token " + 'Z'*40,
                   "Accept": "application/json"}
        response = requests.get("/".join(api_path) + "/", kwargs,
                                headers=headers)
        if response.status_code != 200:
            raise ApiException(response)
        return self.pandify(response.json()['results'])

    def series(self, ticker=None, page=1, dataset=None, additional_params={},
               **kwargs):
        """
        Filter series by ticker, dataset

        Args:
            ticker (str): ticker name (you can also pass list)
            page (int): page to load. If None will return generator
                        object with all pages
            dataset (str): dataset name

        Returns:
            list or Pandas dataframe
        """
        kwargs['ticker'] = ticker
        kwargs['dataset'] = dataset
        kwargs['page'] = page
        kwargs.update(additional_params)
        return self.query(api_method="series", **kwargs)

    def sources(self, source=None, prefix=None, page=1, **kwargs):
        """
        Load dataset sources.

        Examples:
            >>> inquisitor = Inquisitor("your_token")
            >>> inquisitor.sources()
            [{"prefix": "EU"...}, ...]

        Args:
            source (str): filter by source name
            prefix (str): filter by source prefix

        Returns:
            list
        """
        kwargs['source'] = source
        kwargs['prefix'] = prefix
        kwargs['page'] = page
        return self.query(api_method="sources", **kwargs)
