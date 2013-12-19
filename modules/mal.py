#MAL anime module v0.75
#search for animes and mangas on myanimelist
#needs auth_string and api key.

import urllib.request
from bs4 import BeautifulSoup

def mal(phenny,input):
        if not input.group(2):
            return phenny.say("Enter an anime name you weeaboo.")
        i = input.group(2)
        if len(i)>1 and len(input.group())>5:
            i = urllib.request.quote(i)
            d = 'http://myanimelist.net/api/anime/search.xml?q=%s' % i
            opener = urllib.request.build_opener()
            auth_string = ''
            opener.addheaders = [('User-Agent', 'API-KEY-GOES-HERE'),('Authorization', auth_string),]
            x = opener.open(d).read()
            bs = BeautifulSoup(x)
            if len(x) > 14:
                if bs.find('type').string == 'Movie':
                    phenny.reply('{0} ({2}): http://myanimelist.net/anime/{1}'.format(bs.find('title').string, bs.find('id').string, bs.find('type').string))
                else:
                    phenny.reply('{0} (eps:{2}) http://myanimelist.net/anime/{1}'.format(bs.find('title').string, bs.find('id').string, bs.find('episodes').string))
            else:
                phenny.say("Wakaranai ┐(-｡ｰ;)┌")
        else:
            phenny.say("Wakaranai ┐(-｡ｰ;)┌")
mal.commands = ['mal']
mal.priority = 'medium'

def manga(phenny,input):
        if not input.group(2):
                return phenny.say("Enter a mango name you weeaboo.")
        i = input.group(2)
        if len(i)>1 and len(input.group())>7:
                i = urllib.request.quote(i)
                uri = 'http://myanimelist.net/api/manga/search.xml?q=%s' % i
                opener = urllib.request.build_opener()
                auth_string = ''
                opener.addheaders = [('User-Agent', 'API-KEY-GOES-HERE'),('Authorization', auth_string),]
                x = opener.open(uri).read()
                bs = BeautifulSoup(x)
                if len(x) > 14:
                        phenny.reply('{0} ({2}): http://myanimelist.net/manga/{1}'.format(bs.find('title').string, bs.find('id').string, bs.find('chapters').string))
                else:
                        phenny.say("Wakaranai ┐(-｡ｰ;)┌")
        else:
                phenny.say("Wakaranai ┐(-｡ｰ;)┌")
manga.commands = ['manga']
manga.priority = 'medium'
