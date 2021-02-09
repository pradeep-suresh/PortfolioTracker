import requests

def make_url(api_url, api_endpoint, **kwargs):
    url = f'{api_url}/{api_endpoint}'
    return url

class Session(requests.Session):
    def __init__(self):
        super().__init__()
        self.api_url = 'https://api.coinbase.com/v2/'

    def request(self, method, api_endpoint, **kwargs):
        url = make_url(self.api_url, api_endpoint, **kwargs)
        response = super().request(method, url)
        response.raise_for_status()
        return response