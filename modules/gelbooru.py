#gelbooru search module
#to search for 'things'
#http://gelbooru.com/index.php?page=post&s=list&tags=link+sfgfdg‎
#http://gelbooru.com/index.php?page=dapi&s=post&q=index&tags=sdfsg
#to do: total results...random?...make more functions.
from urllib.request import urlopen

def chicken(r):
	url = 'http://gelbooru.com/index.php?page=dapi&s=post&q=index&tags=' + r 
	usock = urlopen(url)
	data = usock.read()
	if len(data) < 100:
		return 'yes'
	else:
		return 'no'
	usock.close()

def gel(phenny,input):
	x = input.split(' ')
	x.pop(0)
	if not x:
		phenny.say("Search gelbooru! Usage: .gelbooru [rating(optional)] [tags(seperated by spaces or +s)]")

	elif x[0] == '':
		phenny.say("No search term entered.")
	elif x[0] == 'safe':
		x.pop(0)
		tags = 'rating:safe+' + '+'.join(x)
		y = 'http://gelbooru.com/index.php?page=post&s=list&tags=' + tags
		fof = chicken(tags)
		if fof == 'yes':
			phenny.say('Nothing but chickens!')
		if fof == 'no':
			phenny.say(y)

	elif x[0] == 'questionable': 
		x.pop(0)
		tags = 'rating:questionable+' + '+'.join(x)
		y = 'http://gelbooru.com/index.php?page=post&s=list&tags=' + tags
		fof = chicken(tags)
		if fof == 'yes':
			phenny.say('Nothing but chickens!')
		if fof == 'no':
			phenny.say(y)
	
	elif x[0] == 'explicit':
		x.pop(0)
		tags = 'rating:explicit+' + '+'.join(x)
		y = 'http://gelbooru.com/index.php?page=post&s=list&tags=' + tags
		fof = chicken(tags)
		if fof == 'yes':
			phenny.say('Nothing but chickens!')
		if fof == 'no':
			phenny.say(y)

	else:
		tags = '+'.join(x)
		y = 'http://gelbooru.com/index.php?page=post&s=list&tags=' + tags
		fof = chicken(tags)
		if fof == 'yes':
			phenny.say('Nothing but chickens!')
		if fof == 'no':
			phenny.say(y)
gel.commands = ['gel','gelbooru']
