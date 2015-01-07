#anime news network rss feed to channel
#Need to make it start by itself somehow.
import feedparser
from datetime import datetime
import time

def parse(now):
        new = []
        allnew = ''
        url = 'http://www.animenewsnetwork.com/news/rss.xml'
        x = feedparser.parse(url)
        for items in x.entries:
                if now < items.published_parsed:
                        if items.title == 'Daily Briefs' or 'Ranking' in items.title:
                                continue
                        else:
                                new.append(items.title)
        if new:
                allnew = " | ".join(new)
                return allnew

def rss(phenny, input):
        now = time.gmtime()
        time.sleep(3600)
        while True:
                time.sleep(7200)
                out = parse(now)
                if out:
                        phenny.say(out)
                now = time.gmtime()
rss.commands = ['startrss']
rss.priority = 'medium'
