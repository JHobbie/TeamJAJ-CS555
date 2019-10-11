#US29

def listDeceased(individualDict):
    for key in individualDict.keys():
        currInd = individualDict[key]
        if 'DEAT' in currInd.keys():
            return currInd['NAME']
        