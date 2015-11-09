# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 22:27:44 2015

@author: oriolandres
"""
from urllib2 import urlopen, Request
import json
import pandas as pd
from datetime import datetime


class inquisitor(object):
    host = 'http://www.inquirim.com'
    token = ''
    view = ''
    def __init__(self, token = ''):
        if len(token)>0:
            self.token = token
        else:
            raise ValueError('Please, supply a valid authentication token')
    
    def passtoken(self, token):
        self.token = token
    
    def query(self, view, **kwargs):  
        view = view.lower()
        if not view.endswith('/'):
            view+='/'
        self.view = view
        urlpars = '?'

        for k,v in kwargs.items():
            if type(v) == list:
                kwargs[k] = ','.join(v)
        if kwargs:
            urlpars += '&'.join([k+'='+v for k, v in kwargs.items()])
        
        if not 'format' in kwargs:
            urlpars += '&format=json'
        url = self.host + '/api/' + view
        url +=  urlpars

        req = Request(url,
                      headers = {
                      "Authorization": 'Token '+self.token,
                      })
        response = urlopen(req)
        self.datastring = response.read()
        return self.datastring
    def df(self):
        rdict = json.loads(self.datastring)
        if self.view == 'series/':
            results = rdict['results']
        elif self.view == 'basket/':
            results = rdict['results'][0]['components']
        
        df = pd.DataFrame()
        for s in results:
            new=  pd.DataFrame({s['ticker']:s['data']['values']},
                               index = map(lambda x: datetime.strptime(x,'%Y-%m-%d'), s['data']['dates']),
                                dtype=float)
            df = pd.concat([df, new], axis = 1 )
        return df
        
def test():
    token = ''
    inq = inquisitor(token)
    inq.query('series', ticker = ["WEO.GGSB_NPGDP00CB.Y.FR","WEO.GGSB_NPGDP00CB.Y.ES"], expand = 'values')
    inq.query('basket', name = 'test', expand = 'values') 
    df = inq.df()
    
    df.plot(marker = 'o')
    df.plot(x = 0,y =1,kind='scatter')