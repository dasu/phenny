#wish happy birthday and stuff v0.6

from datetime import datetime
import json

def date_handler(obj):
	return obj.isoformat() if hasattr(obj, 'isoformat') else obj
def date_hook(json_dict):
	for(key, value) in json_dict.items():
		try: 
			json_dict[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
		except:
			pass
	return json_dict

def writejson(dict):
	with open('/home/desu/phenny-master/modules/data.txt', 'w') as bdayfile:
		json.dump(dict, bdayfile, default=date_handler)

def readjson():
	with open('/home/desu/phenny-master/modules/data.txt','r') as bdayfile:
		dict = json.loads(bdayfile.read(), object_hook=date_hook)
	return dict

def datetonext(dict):
        res = []
        today = datetime.today()
        for x,y in dict.items():
                delta = y.replace(year=(datetime.today().year)) - today
                if delta.total_seconds() < 0:
                        delta = y.replace(year=(datetime.today().year+1)) - today
                res.append([x,delta])
        res.sort(key=lambda x: x[1])
        return res

def setbday(phenny, input):
	dict = readjson()
	name = input.nick
	#phenny.say(input.group(1))
	try:
		date = datetime.strptime(input.group(1), '%m-%d')
	except:
		phenny.say("Please enter a valid date.  Accepts MONTH-DAY only.")
		return
	dict[name] = date
	#phenny.say(name+str(date))
	writejson(dict)	
	phenny.say("Birthday saved.")
setbday.priority = 'low'
setbday.rule = r'^.setbday (\d{1,2}-\d{1,2})$'

def nextbday(phenny, input):
	dict = readjson()
	res = datetonext(dict)
	nname=res[0][0]
	nbday=(dict[nname]).strftime('%B %d')
	daysaway=(res[0][1]).days
	phenny.say("Next birthday: %s on %s (%s days away)" %(nname, nbday, daysaway))
nextbday.commands = ['bday','birthday']
nextbday.priority = 'low'	
