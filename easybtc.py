#This library is “Powered by CoinDesk” with express permission from Coindesk
#Please visit https://www.coindesk.com/price/bitcoin for the Coindesk web experience
#
#
#easybtc is meant to be an uncomplicated and easy way to integrate realitime BTC price into your project
#github https://github.com/ymode/easybtc

import requests as _r

class Request:
    def __init__(self):
        self.request = _r.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        self.status_c = self.request.status_code
        self.json = self.request.json()
        self.price = self.json['bpi']['USD']['rate']
        self.price_GBP = self.json['bpi']['GBP']['rate']
        self.price_EUR = self.json['bpi']['EUR']['rate']

class Bitcoin:
    def __init__(self):
        self.price = Request().price
        self.price_GBP = Request().price_GBP
        self.price_EUR = Request().price_EUR
        self.status_code = Request().status_c
