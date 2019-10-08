import datetime

#US36

def listRecentDeaths(familyDict, individualDict):
    currDate = datetime.datetime.today()
    pastDate = currDate - datetime.timedelta(days=30)
    deathList = []

    for key in individualDict.keys():
        currInd = individualDict[key]
        if 'DEAT' in currInd.keys():
            deatDate = datetime.datetime.strptime(currInd['DEAT'][0], '%d %b %Y')
            if pastDate <= deatDate < currDate:
                deathList += ["Individual " + currInd['ID'] + ": " + currInd['NAME'][0]]
    return deathList

