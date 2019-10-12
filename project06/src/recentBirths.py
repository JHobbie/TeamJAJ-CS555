import datetime

#US35

def listRecentBirths(familyDict, individualDict):
    currDate = datetime.datetime.today()
    pastDate = currDate - datetime.timedelta(days=30)
    birthList = []

    for key in individualDict.keys():
        currInd = individualDict[key]
        if 'BIRT' in currInd.keys():
            birthDate = datetime.datetime.strptime(currInd['BIRT'][0], '%d %b %Y')
            if pastDate <= birthDate < currDate:
                deathList += ["US35: Individual " + currInd['ID'] + ": " + currInd['NAME'][0]]
    if birthList == []:
        birthList += ["US35: No recent births."]
    return birthList