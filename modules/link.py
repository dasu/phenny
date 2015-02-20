#v.016
#looks for links in irc and outputs titles if any.
#I honestly don't know what i'm doing.

from bs4 import BeautifulSoup
from urllib.request import urlopen
import html5lib

def idunno(phenny, input):
	d = 0
	bs = 0
	uri3 = input.group(1)
	if "hitbox" not in uri3:
		try: 
			d = urlopen(uri3).read()
		except:
			print("url doesn't exist?")
		if d:
			try:
				bs = BeautifulSoup(d,'html5lib',from_encoding="utf-8")
			except:
				print("url didn't have a title?")
			
			if bs.title != None:
				phenny.say(bs.title.string.strip())


idunno.rule = r'.*(http[s]?://[^<> "\x01]+)[,.]?'
