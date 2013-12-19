#track dogecoin shit
#ported from uguubot's implementation: 
#https://github.com/infinitylabs/UguuBot/blob/e37d41ac92975d7506567133d32e973ba61f48fc/plugins/bitcoin.py

import re
import json
from bs4 import BeautifulSoup
from urllib.request import urlopen 

def doge(phenny, input):
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
	
	result = float(bitcoin_price) * float(dogerate)
	dollar_result = 1 / float(result)
	phenny.say("Current Value: \x0307$%s\x0f - 1 Doge = \x0307฿%s\x0f BTC - $1 = \x0307%s\x0f Doges" % (result,dogerate,dollar_result))
doge.commands = ['doge','dogecoin','dc']

