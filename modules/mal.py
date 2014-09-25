#MAL anime module v1.0
#needs auth_string, api key
#thanks agri for index error shit fix

import urllib.request
from bs4 import BeautifulSoup

def connect(url):
        opener = urllib.request.build_opener()
        auth_string = ''
        opener.addheaders = [('User-Agent', ''),('Authorization', auth_string),]
        x = opener.open(url).read()
        bs = BeautifulSoup(x)
        return (bs, x)


def mal(phenny,input):
        if not input.group(2):
            return phenny.say("Enter an anime name you weeaboo.")
        i = input.group(2)
        if len(i)>1 and len(input.group())>5:
            i = urllib.request.quote(i)
            d = 'http://myanimelist.net/api/anime/search.xml?q=%s' % i
            bs, x = connect(d)
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
                bs, x = connect(uri)
                if len(x) > 14:
                        phenny.reply('{0} ({2}): http://myanimelist.net/manga/{1}'.format(bs.find('title').string, bs.find('id').string, bs.find('chapters').string))
                else:
                        phenny.say("Wakaranai ┐(-｡ｰ;)┌")
        else:
                phenny.say("Wakaranai ┐(-｡ｰ;)┌")
manga.commands = ['manga']
manga.priority = 'medium'

def people(phenny,input):
        if not input.group(2):
                return phenny.say("Enter a name, retard")
        i = input.group(2)
        if len(i)>1 and len(input.group())>8:
                i = urllib.request.quote(i)
                uri = 'http://myanimelist.net/people.php?q=%s' % i
                bs, x = connect(uri)
                if len(x) > 14 and bs.body.findAll("table")[1].findAll("tr")[1].td.string != 'No results returned':
                       if not bs.body.findAll(text='Search Results'):
                                phenny.say(bs.h1.string + ": http://myanimelist.net" + bs.findAll(id="horiznav_nav")[0].a['href'])
                       else:
                                phenny.say(bs.body.findAll("table")[1].findAll("tr")[1].findAll("td")[1].a.string + ": http://myanimelist.net" + bs.body.findAll("table")[1].findAll("tr")[1].a['href'])
                else:
                        phenny.say("No results found. ┐(-｡ｰ;)┌")
        else:
                phenny.say("Please enter a proper term. ┐(-｡ｰ;)┌")
people.commands = ['people','va','seiyuu']
people.priority = 'medium'

def character(phenny,input):
        if not input.group(2):
                return phenny.say("Enter a name, retard")
        i = input.group(2)
        if len(i)>1 and len(input.group())>11:
                i = urllib.request.quote(i)
                uri = 'http://myanimelist.net/character.php?q=%s' % i
                bs, x = connect(uri)
                if len(x) > 14 and bs.body.findAll("table")[1].findAll("tr")[1].td.string != 'No results returned': #or 'No results found'
                       if not bs.body.findAll(text='Search Results'):
                                phenny.say(bs.h1 + ": http://myanimelist.net" + bs.findAll(id="horiznav_nav")[0].a['href'])
                       else:
                                phenny.say(bs.body.findAll("table")[1].findAll("tr")[1].findAll("td")[1].a.string + " from: " + bs.body.findAll("table")[1].findAll("tr")[1].findAll('td')[2].a.string + " http://myanimelist.net" + bs.body.findAll("table")[1].findAll("tr")[1].a['href'])
                else:
                        phenny.say("No results found. ┐(-｡ｰ;)┌")
        else:
                phenny.say("Please enter a proper term. ┐(-｡ｰ;)┌")
character.commands = ['character']
character.priority = 'medium'
