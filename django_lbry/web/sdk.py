import requests
from datetime import datetime, timedelta

SERVER_ADDRESS = 'http://localhost:5279'


# Wraps API calls
def call(method, params):
    return requests.post(SERVER_ADDRESS, json={'method': method, 'params': params}).json()


# Easy resolve url
def resolve(value):
    return call('resolve', {'urls': value}).get('result').get(value)


# Easy claim_search
def claim_search(days=None, **params):
    if days:
        limit = datetime.now() - timedelta(days=days)
        timestamp_limit = str(int(datetime.timestamp(limit)))
        params['timestamp'] = f'>{timestamp_limit}'
    params['no_totals'] = True
    test = call('claim_search', params)
    if test.get('result'):
        return test.get('result').get('items')
    else:
        return test


# Search engine, very basic.
def search_engine(value):
    search = claim_search(text=value, order_by=['support_amount'], page_size=50, page=1)
    if isinstance(search, list):
        return search
    else:
        search = claim_search(name=value, order_by=['support_amount'], page_size=50, page=1)
        return search
