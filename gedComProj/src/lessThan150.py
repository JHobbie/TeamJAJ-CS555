import datetime

#US07

def lessThan150(individualDict):
    retList = []
    currDate = datetime.now()
    for key in individualDict.keys():
        currInd = individualDict[keys]
        if 'DEAT' in currInd.keys():
            deathAge = currInd['DEAT'] - currInd['BIRT']
            if deathAge >= 150:
                retList += [("US07: " + currInd['NAME'] + "was too old when they passed away.")]
        else:
            age = currDate - currInd['BIRT']
            if age >= 150:
                retList += [("US07: " + currInd['NAME'] + "is too old.")]
    return retList

