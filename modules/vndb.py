#todo: fix some unicode decode issue on certain japanese searches.


import json
from socket import socket as ss

def login(sock):
        sock.connect(("api.vndb.org", 19534))
        test = bytes("login {\"protocol\":1,\"client\":\"syrup\",\"clientver\":0.7}\x04", "utf-8")
        sock.sendall(test)
        recv(sock)

def recv(sock):
        data = sock.recv(4096)
        if not str(data, "utf-8").endswith("\x04"):
                fulldata += recv(sock)
        return fulldata

def gettags(tags):
        json_data=open("/home/desu/vndb/tags.json").read()
        tagsjs = json.loads(json_data)
        tah = []
        for tag in tags:
                if tag[2] == 0:
                        if tag[1] >= 2.95:
                                for b in tagsjs:
                                        if b['id'] == tag[0]:
                                                tah.append(b['name'])
        tags2 = ", ".join(tah)
        return tags2


def vndb(phenny, input):
        length = {}
        length[1] = "Very short (< 2 hours)"
        length[2] = "Short (2 - 10 hours)"
        length[3] = "Medium (10 - 30 hours)"
        length[4] = "Long (30 - 50 hours)"
        length[5] = "Very Long (> 50 hours)"
        sock = ss()
        if not input.group(2):
                return phenny.say("Enter a VN name to search.")
        i = input.group(2)
        request = "get vn basic,details,stats,tags (search ~ \"{0}\")\x04".format(i)
        test = bytes(request, "utf-8")
        login(sock)
        sock.sendall(test)
        vn = recv(sock)
        #phenny.say(vn)
        if str(vn, "utf-8")[0:5] == 'error':
                phenny.say("An error occured.")
        else:
                js = json.loads((str(vn, "utf-8"))[8:-1])
                if js['items']:
                        tags = js['items'][0]['tags']
                        tags2 = gettags(tags)
                        phenny.say('{0}: http://vndb.org/v{1}, Released: {2}, Length: {3}, Tags: {4}'.format(js['items'][0]['title'],js['items'][0]['id'],js['items'][0]['released'],length[js['items'][0]['length']],tags2))
                else:
                        phenny.say("No results.")
        sock.close()
vndb.commands = ['vndb','vn']
vndb.priority = 'medium'
