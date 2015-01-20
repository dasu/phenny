from urllib.request import urlopen
import json

def mtg(phenny,input):
	if not input.group(2):
		return phenny.say("Please enter a card name.")
	i = input.group(2)
	x = urlopen('http://api.mtgdb.info/search/%s' % i)
	c = x.read()
	js = json.loads(c.decode('utf-8'))[0]
	if js['type'] == 'Creature':
		phenny.say('Name: {0}, Type: {1}, Cost: {2}, Effect: {3}, Power: {4}, Toughness: {5}'.format(js['name'], js['type'], js['manaCost'], js['description'], js['power'], js['toughness']))
  else:
		phenny.say('Name: {0}, Type: {1}, Cost: {2}, Effect: "{3}"'.format(js['name'], js['type'], js['manaCost'], js['description']))

mtg.commands = ['mtg','magic']
mtg.priority = 'medium'
