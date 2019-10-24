#US15

def fewerSiblings(familyDict):
    retlist = []
    for key in familyDict.keys():
        currFam = familyDict[key]
        retList +=  [("US15: Family id %s" %  (currentFam['ID']))]
        if 'CHIL' in currFam:
            kidlist = currFam['CHIL']
            if len(kidlist) >= 15:
                retList += [("US15: There are too many kids is family")]
        else:
            retList+= ["US15: No children in this family"]
    return retList