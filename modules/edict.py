#add kanji support

from urllib.request import urlopen
from bs4 import BeautifulSoup

def edict(phenny, input):
        if not input.group(2):
                return phenny.say("Please enter a word.")
        i = input.group(2)
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
edict.commands = ['edict']
edict.priority = 'medium'
