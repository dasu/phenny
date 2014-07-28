#todo: add checks for errors and stuff, make it neater, add more functionality (lol)


import json
from socket import socket as ss
#sock = ss()
def login(sock):
        #global sock
        sock.connect(("api.vndb.org", 19534))
        test = bytes("login {\"protocol\":1,\"client\":\"syrup\",\"clientver\":0.1}\x04", "utf-8")
        sock.sendall(test)
        recv(sock)

def recv(sock):
        #global sock
        data = sock.recv(1024)
        if not str(data, "utf-8").endswith("\x04"):
                data += recv(sock)
        return data

def vndb(phenny, input):
        #global sock
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
        request = "get vn basic,details,stats (search ~ \"{0}\")\x04".format(i)
        test = bytes(request, "utf-8")
        login(sock)
        sock.sendall(test)
        vn = recv(sock)
        #phenny.say(vn)
        js = json.loads((str(vn, "utf-8"))[8:-1])
        phenny.say('{0}: http://vndb.org/v{1}, Released: {2} , Length: {3}'.format(js['items'][0]['title'],js['items'][0]['id'],js['items'][0]['released'],length[js['items'][0]['length']]))
        sock.close()
vndb.commands = ['vndb']
vndb.priority = 'medium'
