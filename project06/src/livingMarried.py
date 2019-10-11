#US30

def livingMarried(individualDict):
    for key in individualDict.keys():
        currInd = individualDict[key]
        if 'MARR' in currInd.keys():
            if 'DEAT' not in currInd.keys():
                return currInd['NAME']