# -*- coding: utf-8 -*-
"""
Module that interfaces with Inquirim statistical database.

MIT License 
Copyright (c) 2016 Inquirim Ltd.
"""
import requests
import re
import pandas
import datetime

from urlparse import urlparse, parse_qs


__all__ = ['Inquisitor','ApiException']
__copyright__ = "Copyright (c) 2016 Inquirim Ltd."
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
            return "Server responded with unexpected error ({0})".format(self.response.status_code)
        return "Server responded with error ({1}): {0}".format(response.get(u'detail'), self.response.status_code)


class Inquisitor(object):
    """A python interface for the Inquirim API.
    """
    
    api_url = "https://www.inquirim.com/api"
    token = ""
    return_pandas = True
    metadata = None
    
    def __init__(self, token):
        """
        Args:
            token: Authentication token on inquirim site
        """
        assert(re.match(r'^[a-f0-9]{40}$', token)), "Invalid token. Please, specify a valid token. (Visit https://www.inquirim.com/account/api/ to obtain one.)"
        self.token = token

    def basket(self, expand="obs", page=1, **kwargs):
        """
        Datasets you can edit, download and share.

        Args:
            page (int): page to load. If None will return generator object with all pages
            expand (str): if 'obs' load ticker name and data values, if 'meta' load only meta info, if 'both'
                load both meta and observations

        Returns:
            Pandas dataframe
        """
        kwargs['expand'] = expand
        kwargs['page'] = page
        return self.query(api_method="basket", **kwargs)


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
            index=map(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'), data['data']['dates']),
            dtype=float
        )
        self.metadata[data['ticker']] = dict((k,v) for k,v in data.items() if k not in ['ticker','data'])
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
            dataframe = pandas.concat([dataframe, self.convert_data(item)], axis=1)
        return dataframe

    def datasets(self, dataset=None, source=None, page=1, **kwargs):
        """
        Load dataset sources.

        Examples:
            >>> inquisitor = Inquisitor("your_token")
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

    def followed(self, expand="obs", page=1, **kwargs):
        """
        Request the series you follow.

        Args:
            page (int): page to load. If None will return generator object with all pages
            expand (str): if 'obs' load ticker name and data values, if 'meta' load only meta info, if 'both'
                load both meta and observations

        Returns:
            Pandas dataframe
        """
        kwargs['expand'] = expand
        kwargs['page'] = page
        return self.query(api_method="followed", **kwargs)
        
    def from_url(self, url = None):
        if url is None:
            raise ValueError('Invalid argument.')
        url = re.sub(r'.*inquirim\.com/api',self.api_url,url)
        parsed_url = urlparse(url)
        params = parse_qs(parsed_url.query)
        
        
        if parsed_url.path == '/api/series/':
            numeric_args = dict((k,params.pop(k)) for k,v in params.items() if re.match('^\d+$',k))
            params['additional_params'] = numeric_args
            return self.series(**params)
        elif parsed_url.path == '/api/datasets/':
            return self.datasets(**params)
        elif parsed_url.path == '/api/sources/':
            return self.sources(**params)
        elif parsed_url.path == '/api/basket/':
            return self.basket(**params)
        elif parsed_url.path == '/api/followed/':
            return self.followed(**params)


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
        kwargs = {str(key): str(value) if type(value) is not list else ",".join(map(str,value)) for key, value in kwargs.items() if value is not None}
        kwargs['format'] = "json"
        api_path = [self.api_url] + [method for method in api_method.split("/") if method]
        headers = {"Authorization": "Token " + self.token,
                   "Accept": "application/json"}
        response = requests.get("/".join(api_path) + "/", kwargs, headers=headers)
        if response.status_code != 200:
            raise ApiException(response)

        result =  response.json()['results']
        return self.pandify(result)

    def series(self, ticker=None, page=1, search=None, dataset=None, expand="both", 
               geography=None,  additional_params = {}, **kwargs):
        """
        Filter series by ticker, dataset, or by search terms

        Args:
            ticker (str): ticker name (you can also pass list)
            page (int): page to load. If None will return generator object with all pages
            search (str): search term (e.g. italy productivity)
            dataset (str): dataset name
            expand (str): if obs load ticker name and data values, if meta load only meta info, if both load both meta and observations
            geography (str): name of geographical feature

        Returns:
            list or Pandas dataframe
        """
        kwargs['ticker'] = ticker
        kwargs['search'] = search
        kwargs['dataset'] = dataset
        kwargs['expand'] = expand
        kwargs['geography'] = geography
        kwargs['page'] = page
        kwargs.update(additional_params)
        return self.query(api_method="series",**kwargs)
        
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
