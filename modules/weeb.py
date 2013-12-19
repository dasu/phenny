#!/usr/bin/python3
"""
weebmeter based on the chillmeter.py
removed unneeded randomness and made it weeaboo themed
"""
import random, time
from math import fabs


# weeb decay rate per minute
weeb_decay_rate = 1

weeb_words = [
	# words that make the place weeb
	("anime", 1),
	("japan", 1),
	("loli", 1),
	("manga", 1),
	("visual novel", 1),
	("light novel", 1),
	("shojo", 2),
	("shoujo", 2),
	("shonen", 2),
	("shounen", 2),
	("seinen", 2),
	("josei", 2),
	("magical girl", 2),
	("mecha", 2),
	("harem", 2),
	("yuri", 2),
	("yaoi", 2),
	("fansub", 1),
	("dojinshi", 2),
	("imouto", 2),
	("mangaka", 2),
	("scanlation", 1),
	("cosplay", 1),
	("san", 1),
	("tan", 1),
	("moe", 1),
	("baka", 2),
	("imasu", 2),
	("arigato", 1),
	("gaijin", 2),
	("hentai", 1),
	("hidoi", 2),
	("mahou", 3),
	("madoka", 3),
	("magica", 3),
	("magika", 3),
	("ohayo", 2),
	("onegai", 2),
	("sugoi", 2),
	("doushio", 2),
	("doshio", 2),
	("suki", 2),
	("tomodachi", 2),
	("otaku", 2),
	("jc staff", 2),
	("shaft", 1),
	("DEEN", 2),
	("kyoto animation", 2),
	("kyoto", 1),
	("tokyo", 1),
	("okinawa", 1),
	("production ig", 2),
	("gainax", 2),
	("desu", 2),
	("kawaii", 1),
	("sega", 1),
	("nintendo", 1),
	("capcom", 1),
	("square enix", 1),
	("compile heart", 2),
	("vocaloid", 2),
	("miku", 2),
	("touhou", 2),
	("dasu", 1),
	("kun", 1),
	("chouxe", 1),
	("japanese", 1),
	("onii-chan", 1),
	("onee-chan", 1),
	("nippon", 2),
	("nakama", 2),
	("dakimakura", 2),
	("chan", 2),
	("senpai", 2),
	("kohai", 2),
	("gakusei", 2),
	("sensei", 1),
	("sama", 2),
	("jpop", 1),
	

	# words that unweeb the place
	("nuke", -3),
	("nuclear", -3),
	("earthquake", -3),
	("white people", -1),
	("WW2", -2),
	("america", -2),
	("usa", -2),
	("freedom", -1),
	("gabe", -1),
	("gaben", -1),
	("hotdog", -1),
	("europe", -1),
	

]

# all things weeb
weeb_things = [
	("anime", "animes"),
	("manga", "mangas"),
	("visual novel", "visual novels"),
	("loli", "lolis"),
	("light novel", "light novels"),
	("plastic figure", "plastic figures"),
	("imouto", "imoutos"),
	("dakimakura", "dakimakuras"),
	("touhou", "touhous"),
	("pokemon", "pokemen"),

]

def measure(phenny, input):
	"""keeps a finger on the pulse of the weebness"""
	weeb = measure.channels.get(input.sender, 0)	#gets the weeb level
	now = time.time()	#creates variable of current time
	if now - measure.last_tick > 60:	#if in the last 60 seconds
		measure.last_tick = now	#last_tick is current time
		if weeb > 0:	#if weeb level is above 0, decay it towards 0
			weeb -= weeb_decay_rate
			weeb = max(0, weeb)
		elif weeb < 0:	#if weeb level is below 0, decay it towards 0
			weeb += weeb_decay_rate
			weeb = min(0, weeb)
		measure.channels[input.sender] = weeb	#measures weeb level

	if ".weeb" in input:
		return # dont self count

	for w in weeb_words:	#every weeb word said adds +1 to the weeb level
		if w[0] in input.lower():
			weeb += w[1]

	measure.channels[input.sender] = weeb	#measures weeb level


measure.rule = r'.*'
measure.priority = 'low'
measure.last_tick = time.time()
measure.channels = {}

def weeb(phenny, input):
	""".weeb - Measure the current channel weebness level."""
	level = measure.channels.get(input.sender, 0)	#gets the weeb level
	amount = int(fabs(level))
	
	items = []
	used = set()
# removed the RNG with the level
	item = random.choice(weeb_things)

	while item in used:	#stops bot from reusing weeb things
		item = random.choice(weeb_things)
	used.add(item)

	if level == 1:
		item = item[0] # singular
		items.append("%s %s" % (level, item))
	elif level == 0:
		item = item[0]
		items.append("%s %s" % (level+1, item))
	else:
		item  = item[1] # plural
		items.append("%s %s" % (amount, item))


	item_str = ", ".join(items)
	#print level, item_str

	if level <= 0:
		message = "WARNING: weeb level is dangerously low. I recommend %s" % (item_str)
	else:
		message = "weeb level is currently: %s" % (item_str)

	phenny.say(message)


weeb.commands = ['weeb']
weeb.priority = 'low'

if __name__ == '__main__':
	print(__doc__.strip())
