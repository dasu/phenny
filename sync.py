"""
FOR SYNCING AND SYNC CLUB ver 0.7
"""
from threading import Timer
from time import sleep


#sync club related below
def club(phenny,input):
	'''
	Returns the secret sync club link. Members only!
	'''
	phenny.say("http://www.tinyurl.com/syncclub")
club.commands = ['syncclub','sc']
club.priority = 'medium'


#general syncing below
def name(phenny,input):
	'''Remembers yo name
	'''
	if input.nick.lower() not in name.nerdlist and input.nick.lower() != 'py-ctcp':
		name.nerdlist.append(input.nick.lower())
	if len(name.nerdlist)>10:
		name.nerdlist.pop(0)

name.rule = r'.*'
name.priority = 'low'
name.nerdlist = []

def namechecker(validnames,names_to_check):
	'''Checks the names of the readylist to the nerdlist'''
	wrongnames=[]
	i=0
	x=0
	while i < len(names_to_check):
		if names_to_check[i] not in validnames:
			wrongnames.insert(x,names_to_check[i])
			x+=1
		i+=1
	return wrongnames


def sync(phenny,input):
	'''Starts a session to sync for various media.
	
	INPUT: .sync <username1> <username2> <etc>

	Creates a 1 minute timer to sync and makes a list of syncers
	'''

	if sync.sync_on==0 and len(input.group())>6:
		syncers = input.group().lower()
		sync.readylist = syncers.split()
		sync.readylist.pop(0)
		sync.namelist=list(set(sync.readylist))
		if input.nick.lower() not in name.nerdlist:
			name.nerdlist.append(input.nick.lower())
		badnames = namechecker(name.nerdlist,sync.namelist)
		sync.readylist=list(set(sync.readylist))
		if badnames == []:
			if sync.readylist!=[] and phenny.nick not in sync.readylist and len(sync.readylist)<=10:
					sync.madtime=Timer(60.0,mad,[phenny,input])
					sync.madtime.start()
					phenny.say("Buckle up syncers!")
					sync.sync_on=1
			else:
				phenny.say('fuck you')
		else:
			phenny.say('Never heard of %s' % ", ".join(badnames))
	else:
		phenny.say('fuck you')

sync.commands = ['sync']
sync.priority = 'medium'
sync.sync_on = 0
sync.readylist = []
sync.namelist = []
sync.madtime = 0


def mad(phenny,input):
	'''Bot gets mad.

	Calls out people , ends sync and clears variables.
	'''
	phenny.say('Please .ready up: ' + ", ".join(sync.readylist))
	sleep(60)
	if sync.readylist !=[]:
		phenny.say('Shit syncers: ' + ", ".join(sync.readylist))
		sync.readylist=[]
		sync.sync_on=0

		
def ready(phenny,input):
	'''User declares they are ready.

	INPUT: .ready

	Removes user from the list and initiates the sync if all are ready.
	'''

	if input.nick.lower() in sync.readylist:
		sync.readylist.remove(input.nick.lower())
		if sync.readylist == [] and sync.sync_on == 1:
			sync.madtime.cancel()
			phenny.say('Lets go %s!' % (", ".join(sync.namelist)))
			sleep(2)
			phenny.say("3")
			sleep(2)
			phenny.say("2")
			sleep(2)
			phenny.say("1")
			sleep(2)
			phenny.say("GO!")
			sync.sync_on=0
	else:
		phenny.say("You're not on the list")
ready.commands = ['ready']
ready.priority = 'medium'


def desync(phenny,input):
	'''Cancels sync

	INPUT: .desync

	Ends the sync if user on the list
	'''
	if sync.readylist !=[] and sync.sync_on == 1:
		if input.nick.lower() in sync.readylist:
			phenny.say('Aborting sync...')
			sync.madtime.cancel()
			sync.sync_on=0
			sync.readylist=[]
		else:
			phenny.say("You're not on the list")
	else:
		phenny.say('fuck you')
desync.commands = ['desync']
desync.priority = 'medium'


if __name__ == '__main__':
	print(__doc__.strip())
