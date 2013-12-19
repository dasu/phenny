#twitchtv module with hitbox support customized for #pancakes
#version 1.2.1
import json
import web
from tools import GrumbleError
from urllib.error import HTTPError

def twitch(phenny,input):
    if not input.group(2): 
        v = []
        uri = 'https://api.twitch.tv/kraken/streams?channel=coalll,chouxe,kwlpp,dasusp,lurkk,agriks,repppie,squidgay,supersocks,sc00ty,kaask'
        uri2 = 'kwlpp','agriks','coal','chouxe','socks'
        bytes = web.get(uri)
        m = json.loads(bytes)
        for stream in m['streams']:
            x = stream['channel']['name']
            y = stream['channel']['url']
            z = x + " (" + y + ")"
            v.append(z)
        for name in uri2:
            uri3 = 'http://api.hitbox.tv/media/live/%s' % name
            bytes2 = web.get(uri3)
            c = json.loads(bytes2)
            if c['livestream'][0]['media_is_live'] == '1':
                x2 = c['livestream'][0]['media_user_name']
                y2 = c['livestream'][0]['channel']['channel_link']
                z2 = x2 + " (" + y2 + ")"
                v.append(z2)
        if v == []:
            phenny.say('No one is currently streaming.')
        else:	
            phenny.say('Currently streaming: %s' % (", ".join(v))) 
    else:
        i = input.group(2)
        uri = 'https://api.twitch.tv/kraken/streams/%s' % i
        try:
            bytes = web.get(uri)
        except (HTTPError, IOError, ValueError) :
            raise GrumbleError("N-no such user exists, you b-baka!")
        m = json.loads(bytes)
        try:
            if format(m['stream']) == 'None':
                phenny.say(i + ' is not streaming')
            else:
                phenny.say(i + ' is streaming {0}: {1}'.format(m['stream']['game'], m['stream']['channel']['url']))
        except (HTTPError, IOError, ValueError, KeyError) :
            raise GrumbleError("Invalid Username.")
twitch.commands = ['twitchtv','tv','twitch']
twitch.priority = 'medium'

def hitbox(phenny,input):
    if not input.group(2):
        phenny.say('Enter a hitbox user\'s name')
    else:
        ret = input.group(2)
        uri5 = 'http://api.hitbox.tv/media/live/%s' % ret
        try:
            bytes3 = web.get(uri5)
        except (HTTPError, IOError, ValueError):
            raise GrumbleError("N-No such user exists, you b-baka!")
        c3 = json.loads(bytes3)
        if c3['livestream'][0]['media_is_live'] == '1':
            phenny.say(ret + ' is streaming {0}: {1}'.format(c3['livestream'][0]['category_name'], c3['livestream'][0]['channel']['channel_link']))
        else:
            phenny.say(ret + ' is not streaming')
hitbox.commands = ['htv','hitbox']
hitbox.priority = 'medium'
