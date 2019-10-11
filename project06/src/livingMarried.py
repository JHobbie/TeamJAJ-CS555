#US30

def livingMarried(individualDict):
    for key in individualDict.keys():
        currInd = individualDict[key]
        retlist = []
        if 'MARR' in currInd.keys():
            if 'DEAT' not in currInd.keys():
                retlist += [("US30: " + currInd['NAME'] + "is living and married.")]
        else:
            retlist += [("There are no living and married individuals.")]
    return retlist