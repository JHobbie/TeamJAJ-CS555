#US29

def listDeceased(individualDict):
    for key in individualDict.keys():
        currInd = individualDict[key]
        retlist = []
        if 'DEAT' in currInd.keys():
            retlist += [("US29: " + currInd['NAME'] + "is deceased.")]
        else:
            retlist += [("US29: There are no deceased individuals.")]
    return retlist
        