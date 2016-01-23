#!/usr/bin/python
import time ,json
import requests


def btce_btc_usd():
    btceBtcTick = requests.get('https://btc-e.com/api/3/ticker/btc_usd')
    return btceBtcTick.json()['btc_usd']['last']


def huobi():
    huobiBook = requests.get('http://api.huobi.com/staticmarket/detail_btc_json.js')
    return huobiBook.json()['p_new']


def okcoin_cny():
    okCNYlast = requests.get('https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny', verify=False)
    return okCNYlast.json()['ticker']['last']


def okcoin_usd():
    okcoinUSDlast = requests.get('https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd', verify=False)
    return okcoinUSDlast.json()['ticker']['last']


def bitstamp():
    btStamp = requests.get("https://www.bitstamp.net/api/ticker/")
    return btStamp.json()['last']


def bitfinex():
    finexLast = requests.get('https://api.bitfinex.com/v1/ticker/btcusd')
    return finexLast.json()['last_price']


def coinbase():
    coinBaseTick = requests.get('https://api.exchange.coinbase.com/products/btc-usd/book?level=1')
    return coinBaseTick.json()['bids']


def convert_cny_to_usd(cny):
    exchangeRate = requests.get('https://currency-api.appspot.com/api/CNY/USD.json')
    rate = float(exchangeRate.json()['rate'])
    current = float(cny)
    USDrate = current*rate
    return round(USDrate,2)


def main():
    while True:
        try:
            huobiLast = huobi()
            huobiConverted = convert_cny_to_usd(huobiLast)
            print 'Huobi:',huobiConverted,'| CNY:',huobiLast
            okcny = okcoin_cny()
            okcnyConverted = convert_cny_to_usd(okcny)
            print 'OKcn:',okcnyConverted,'| CNY:',okcny
            okusd = okcoin_usd()
            print 'OKus:', okusd
            btce_btcusd = btce_btc_usd()
            print 'Btc-e:',btce_btcusd
            bstamp = bitstamp()
            print 'Bstmp:', bstamp
            finex = bitfinex()
            print 'Finex:', finex
            cbase = coinbase()
            print 'Cbase:', cbase[0][0]
            print '-------------------'
        except Exception ,e:
            print('[-] ERROR = '+str(e))
    time.sleep(5)


if __name__ == '__main__':
        main()
