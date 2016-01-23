#!/usr/bin/python3
import time ,json
import requests

def btce_ltc_usd():
    btceBtcTick = requests.get('https://btc-e.com/api/3/ticker/ltc_usd')
    return btceBtcTick.json()['ltc_usd']['last']

def huobi():
    huobiBook = requests.get('http://api.huobi.com/staticmarket/detail_ltc_json.js')
    return huobiBook.json()['p_new']

def okcoinCNY():
    okCNYlast = requests.get('https://www.okcoin.cn/api/v1/ticker.do?symbol=ltc_cny', verify=False)
    return okCNYlast.json()['ticker']['last']

def bitfinex():
    finexLast = requests.get('https://api.bitfinex.com/v1/ticker/ltcusd')
    return finexLast.json()['last_price']

def main():
    while True:
        huobiLTC = huobi()
        print 'huobi:',huobiLTC
        ok = okcoinCNY()
        print 'okcoin:',ok
        btce = btce_ltc_usd()
        print 'btce:', btce
        bfinex = bitfinex()
        print 'finex:',bfinex
        print '----------'
        # Time between refresh 2.5 hits huobi limit
        time.sleep(2.8)

if __name__ == '__main__':
    main()
