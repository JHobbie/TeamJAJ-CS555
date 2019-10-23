import datetime

def calcDate(dateString):
    try:
        calculatedDate = datetime.datetime.strptime(dateString, '%d %b %Y').date()
        return calculatedDate
    except:
        print("Could not parse date, returning now")
        # We get no credit for detecting syntactic errors, but may want to know when 
        return datetime.datetime.now()

def multipleBirths(individualDict, familyDict):
	childrenDates = {}
	errmsg = []
	for fkey in familyDict.keys():
		currFam = familyDict[fkey]
		childrenDates = {}
		if 'CHIL' in currFam.keys():
			currFamChildren = currFam['CHIL']
			if len(currFamChildren) > 5:
				for childID in currFamChildren:
					currDate = calcDate(individualDict[childID]['BIRT'][0])
					if currDate in childrenDates.keys():
						childrenDates[currDate] += 1
					else:
						childrenDates[currDate] = 1
				for dkey in childrenDates:
					if childrenDates[dkey] > 5:
						errmsg += ["Error US14: Family " + fkey + " has " + str(childrenDates[dkey]) + " children born on " + str(dkey) + "."]
	return errmsg
