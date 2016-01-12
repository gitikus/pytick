#!/usr/bin/python 2.7
#Shows last price from several exchanges.
import time, json
import requests

def btstamp():
  bitStampTick = requests.get("https://www.bitstamp.net/api/ticker/")
  return bitStampTick.json()['last']

def btceBU():
  btceBtcTick = requests.get('https://btc-e.com/api/3/ticker/btc_usd')
  return btceBtcTick.json()['btc_usd']['last']

def btceBL():
  btceLtcTick = requests.get('https://btc-e.com/api/3/ticker/ltc_btc')
  return btceLtcTick.json()['ltc_btc']['last']

def bitFinex():
  bitFinexTick = requests.get('https://api.bitfinex.com/v1/ticker/btcusd')
  return bitFinexTick.json()['last_price']

def coinbase():
  coinBaseTick = requests.get('https://coinbase.com/api/v1/prices/buy')
  return coinBaseTick.json()['amount']

def kraken():
  krakenTick = requests.post('https://api.kraken.com/0/public/Ticker',
    data=json.dumps({"pair":"XXBTZUSD"}),
    headers={"content-type":"application/json"})
  return krakenTick.json()['result']['XXBTZUSD']['c'][0]

#def okcoin():
#def huobi():
  #huoTick = requests.get('http://api.huobi.com/staticmarket/detail_btc_json.js')
  #return huoTick

def main():
  try:
    btstampUSDLive = float(btstamp())
    btceUSDLive = btceBU()
    #btceLTCinBTCLive = btceBL()
    coinbUSDLive = float(coinbase())
    krakenUSDLive = float(kraken())
    bitfinexUSDLive = float(bitFinex())

    print "#####################"
    print "#Bitfinex: ", round(bitfinexUSDLive, 2)
    print "#Bitstamp: ", round(btstampUSDLive, 2)
    print "#Btc-e:    ", round(btceUSDLive, 2)
    print "#Coinbase: ", round(coinbUSDLive, 2)
    print "#Kraken:   ", round(krakenUSDLive, 2)
    print "=-=-=-=--=-=-=-=-=-=-"
  except:
    print 'Error!?!?!?'

if __name__=='__main__':
  while True:
    main()
    time.sleep(10)
