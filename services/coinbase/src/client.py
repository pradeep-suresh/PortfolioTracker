import time, hashlib, hmac
from flask import current_app
from src.session import Session


COINBASE_SESSION = Session()

class Client:
    def __init__(self):
        pass 

    def _request(self, method, url, data=None, extra_headers=None, **kwargs):
        headers = {
            'Accept' : 'application/json',
            'CB-ACCESS_KEY' : current_app.config['API_KEY'],
            'CB-ACCESS-SIGN': self.generate_cb_access_sign(method, url, data),
            'CB-ACCESS-TIMESTAMP' : str(int(time.time()))
        }

        if extra_headers:
            headers.update(extra_headers)

        return COINBASE_SESSION.request(method, url, **kwargs)

    def get(self, url, data=None, headers=None, **kwargs):
        return self._request('get', url, data, headers, **kwargs)
    
    def generate_cb_access_sign(self, method, url, data=''):
        message = f'{str(int(time.time()))}{method.upper()}{url}{data}'
        signature = hmac.new(current_app.config['SECRET_KEY'].encode('utf-8'), 
                            message.encode('utf-8'), 
                            hashlib.sha256).hexdigest()
    
        return signature

    def generate_cb_access_timestamp(self):
        response = self.get('time')
        return response.json()
