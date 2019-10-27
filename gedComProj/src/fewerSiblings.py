#US15

def fewerSiblings(familyDict):
    retList = []
    for key in familyDict.keys():
        currFam = familyDict[key]
        if 'CHIL' in currFam:
            kidlist = currFam['CHIL']
            if len(kidlist) >= 15:
                retList += [("US15: There are too many kids in Family " + currFam['ID'])]
        else:
            retList+= ["US15: No children in this family"]
    return retList