# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 22:27:44 2015

@author: oriolandres
"""
from urllib2 import urlopen, Request

host = 'http://www.inquirim.com'

class inquisitor(object):
    token = ''
    def __init__(self, token = ''):
        if len(token)>0:
            self.token = token
        else:
            raise ValueError('Please, supply a valid authentication token')
    
    def passtoken(self, token):
        self.token = token
    
    def query(self, path, **kwargs):      
        if not path.endswith('/'):
            path+='/'
        urlpars = '?'

        for k,v in kwargs.items():
            if type(v) == list:
                kwargs[k] = ','.join(v)
        if kwargs:
            urlpars += '&'.join([k+'='+v for k, v in kwargs.items()])
        
        if not 'format' in kwargs:
            urlpars += '&format=json'
        url = host + '/api/' + path
        url +=  urlpars


            
        req = Request(url,
                      headers = {
                      "Authorization": 'Token '+self.token,
                      })
        response = urlopen(req)
        return response.read()

def test():
    token = ''
    inq = inquisitor(token)
    rstring =  inq.query('series', ticker = ["WEO.GGSB_NPGDP.Y.FR","WEO.GGSB_NPGDP.Y.ES"], expand = 'values')
    
    import json
    rdict = json.loads(rstring)
    results = rdict['results']
    import pandas as pd
    from datetime import datetime
    df = pd.DataFrame()
    for s in results:
        new=  pd.DataFrame({s['ticker']:s['values']['values']},
                           index = map(lambda x: datetime.strptime(x,'%Y-%m-%d'), s['values']['dates']),
                            dtype=float)
        df = pd.concat([df, new], axis = 1 )
    df.plot(marker = 'o')