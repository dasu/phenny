V0.8
from urllib.request import urlopen, quote
from bs4 import BeautifulSoup

def edict(phenny, input):
	if not input.group(2):
		return phenny.say("Please enter a word.")
	i = input.group(2)
	try:
		i.encode('ascii')
		print(i)
		x = urlopen("http://www.csse.monash.edu.au/~jwb/cgi-bin/wwwjdic.cgi?1ZDJ%s"% i)
		c = x.read()
		bs = BeautifulSoup(c)
		#print(bs)
		if bs.pre:
			res = bs.pre.contents[0].splitlines()[1]
			#print(res)
		else:
			res = "No matches found."
		phenny.say(res)
	except:
		print(i)
		x = urlopen("http://www.csse.monash.edu.au/~jwb/cgi-bin/wwwjdic.cgi?1ZIK%s"%(quote(i)))
		c = x.read()
		bs = BeautifulSoup(c)
		if bs.li:
			res = bs.li.contents[0]
		else:
			res = "No matches found."
		phenny.say(res)
edict.commands = ['edict']
edict.priority = 'medium'
