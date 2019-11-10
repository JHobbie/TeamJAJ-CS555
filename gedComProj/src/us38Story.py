import datetime

def upcomingBirthdays(individualDict):
    currDate = datetime.datetime.today()
    futureDate = currDate + datetime.timedelta(days=30)
    birthList = []
    for key in individualDict.keys():
    	currInd = individualDict[key]
    	try:
    		if 'BIRT' in currInd.keys():
			    birthDate = datetime.datetime.strptime(currInd['BIRT'][0], '%d %b %Y')
			birthDate = datetime.datetime(currDate.year, birthDate.month, birthDate.day, 0, 0)
    		if currDate <= birthDate <= futureDate:
    			birthList += ["US38: Individual " + currInd['ID'] + ": " + currInd['NAME'][0]]
    	except ValueError:
    		pass
    	if birthList == []:
    		birthList += ["US38: No upcoming birthdays"]
    return birthList




