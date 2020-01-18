# easybtc
easy btc is a Bitcoin Python Library - for simple access to bitcoin data. This library makes it simple to request realtime Bitcoin pricing data in one line of code from an open, free and legal source.  easybtc is a python wrapper for the [Coindesk](https://www.coindesk.com/price/bitcoin) API.

easybtc is written to support [Python 3.x](https://www.python.org/download/releases/3.0/) and is powered by [Coindesk](https://www.coindesk.com/price/bitcoin)

# Examples

### Import easybtc:
```python
import easybtc as btc
```

### Current USD value of 1 BTC:
```python
myPriceRequest = btc.Bitcoin().price
```

### Current GBP value of 1 BTC:
```python
myPriceRequest = btc.Bitcoin().priceGBP
```

### Current EURO value of 1 BTC:
```python
myPriceRequest = btc.Bitcoin().priceEUR
```


### Check the success code of the API call:
```python
myStatusCheck = btc.Bitcoin().statusCode
```

```python
if myStatusCheck == 200:
  #execute your cool code!

```
