#ported from feety's willie irc bot module.
import re

import redis

db = redis.Redis(db=0)

line_sep = re.compile(r'([\!\.\?])')  # Split lines on these characters  
# The higher this is, the smarter the bot will sound.
# The lowest possible length for a pair of words. The higher the value, the smarter the bot will sound. But also requires more training
 
def parse_line(ln, split_lines=False, pair_len=3, min_sentence_len=6):
    #First, split the line on all marks that could end a line (!, ., ?)
    if split_lines:
        potential_lines = [itm.strip() for itm in line_sep.split(ln)]
        #Fixes the punctuation missing from the lines that was split on.
        lines = []
        for index in range(0, len(potential_lines), 2):
            if potential_lines[index]:
                lines.append(potential_lines[index] + potential_lines[index + 1])
    else:
        lines = [ln]
 
    #Iterate over all potential lines. Ensuring that they meet requirements.
    #Making a on-the-fly copy of the list so we can manipulate it's contents as we iterate
    for line in lines[:]:
        if len(line.split(" ")) < min_sentence_len:
            lines.remove(line)
 
    pairs = {}
    for line in lines:
        broken_line = line.split(" ")
        for index in range(0, len(broken_line)-(pair_len * 2) + 1):
            val_start = index + pair_len
            val_end = val_start + pair_len
 
            key = " ".join(broken_line[index:pair_len+index])
            val = " ".join(broken_line[val_start:val_end])
            
            #There could be multiple values for a single key in a input line. Store possible values in a list.
            if key not in pairs:
                pairs[key] = []
                
            pairs[key].append(val)
    return pairs

#@willie.module.rule(r'.*4')
def wafflebot(phenny, input):
   pairs = parse_line(input.group(0))




   for key, vals in pairs.items():
      db.sadd(key, *vals)
wafflebot.rule = (r'.*$')
wafflebot.priority = 'medium'

def wafflebottalk(phenny, input):


	sentence = seed = db.randomkey()
	max_length = 6 #Number of iterations. 1 = 3 words
	
	for i in range(max_length):
		if i>= max_length:
			break


		seed = db.srandmember(seed)
		if not seed:










			break
		print(sentence)
		print(seed)	
		if type(sentence) is bytes:
			sentence = sentence.decode("utf-8")
		if type(seed) is bytes:
			seed = seed.decode("utf-8")

		sentence = " ".join([sentence, seed])
	phenny.say(sentence)
wafflebottalk.commands = ['wb', 'talk']
wafflebottalk.priority = 'low'


def wafflebotknows(phenny,input):
	knows = db.dbsize()
	phenny.say("I know about %s things" % (knows))
wafflebotknows.commands = ['wbknows']
