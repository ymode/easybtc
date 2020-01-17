#This library is “Powered by CoinDesk” with express permission from Coindesk
#Please visit https://www.coindesk.com/price/bitcoin for the Coindesk web experience
#easybtc is meant to be an uncomplicated and easy way to integrate realitime BTC price into your project
#github

import requests as _r

class Request:
    def __init__(self):
        self.request = _r.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        self.status_c = self.request.status_code
        self.json = self.request.json()
        self.price = self.json['bpi']['USD']['rate']

class Bitcoin:
    def __init__(self):
        self.price = Request().price


