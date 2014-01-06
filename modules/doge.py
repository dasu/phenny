#track dogecoin shit
#ported from uguubot's implementation: 
#https://github.com/infinitylabs/UguuBot/blob/e37d41ac92975d7506567133d32e973ba61f48fc/plugins/bitcoin.py
#v0.67


import re
import json
from bs4 import BeautifulSoup
from urllib.request import urlopen 

lastPrice = 0

def btc():
	uri3 = 'http://data.mtgox.com/api/2/BTCUSD/money/ticker'
	d = (urlopen(uri3).read()).decode('utf-8')
	res = json.loads(d)
	data = res['data']
	ticker = {
		'buy': data['buy']['display_short']
	}
	bitcoin_price = ("%(buy)s" % ticker).split('$')[1]
	return bitcoin_price

def doge2():
	try:
		url = 'https://coinedup.com/OrderBook?market=DOGE&base=BTC'
		c = urlopen(url).read()
		bs = BeautifulSoup(c)
		test = str(bs.find_all(id="elementDisplayLastPrice")[0])
		dogerate = (re.search('.*last: (.*?\))\D', test).group(1))[:-1]
	except:
		#phenny.say('doge is crashing or syrup is a bad bot, you decide')
		dogerate = 0
	return dogerate


def doge(phenny, input):
	global lastPrice
	go = 0
	uri3 = 'http://data.mtgox.com/api/2/BTCUSD/money/ticker'
	d = (urlopen(uri3).read()).decode('utf-8')
	res = json.loads(d)
	data = res['data']
	ticker = {
		'buy': data['buy']['display_short']
	}
	bitcoin_price = ("%(buy)s" % ticker).split('$')[1]

	try:
		url = 'https://coinedup.com/OrderBook?market=DOGE&base=BTC'
		c = urlopen(url).read()
		bs = BeautifulSoup(c)
		test = str(bs.find_all(id="elementDisplayLastPrice")[0])
		dogerate = (re.search('.*last: (.*?\))\D', test).group(1))[:-1]
	except:
		phenny.say('doge is crashing or syrup is a bad bot, you decide')
		go = 1

	if go is not 1:
		result = float((bitcoin_price.replace(",", ""))) * float((dogerate.replace(",","")))
		dollar_result = 1 / float(result)
		diff = result - lastPrice
		diffStr = ""
		if diff != 0:
			sign = "+" if diff > 0 else ''
			diffStr = " (%s%s)" % (sign, format(diff,'.7f'))
		phenny.say("Current Value: \x0307$%s%s\x0f - 1 Doge = \x0307฿%s\x0f BTC - $1 = \x0307Ɖ%s\x0f Doges" % (result,diffStr,dogerate,dollar_result))
		lastPrice = result
doge.commands = ['doge','dogecoin','dc']


def usd2doge(phenny, input):
	num = input.group(2)
	doger = doge2()
	btc3 = btc()
	result = float(btc3) * float(doger)
	if result != 0:
		do = float(num) / float(result)
		phenny.say('$%s will get you Ɖ%s' % (num, do))
	else:
		phenny.say('doge is worthless')
usd2doge.commands = ['usd2doge']

def doge2usd(phenny, input):
	num = input.group(2)
	doger = doge2()
	btc3 = btc()
	result = float(btc3) * float(doger)
	if result != 0:
		do = float(num) * float(result)
		phenny.say('Ɖ%s will get you $%s' % (num, do))
	else:
		phenny.say('doge is worthless')
doge2usd.commands = ['doge2usd']
