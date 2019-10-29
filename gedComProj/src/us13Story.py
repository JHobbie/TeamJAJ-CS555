import gedComProj.src.utils as utils

def checkSiblingPair(sibling1, sibling2, family):
    errMsg = []
    sib1BirthDate = utils.calcDate(sibling1['BIRT'][0])
    sib2BirthDate = utils.calcDate(sibling2['BIRT'][0])
    if(abs((sib1BirthDate - sib2BirthDate).days)/30 <= 8 and abs((sib1BirthDate - sib2BirthDate).days) >= 2):
        errMsg += [(("Anomaly US13: Sibling %s: %s and sibling %s: %s  in family %s were born too close together" %(sibling1['ID'], sibling1['NAME'][0], sibling2['ID'], sibling2['NAME'][0], family['ID'])))]
    return errMsg
def checkFamily(family, individualDict):
    errMsg = []
    if('CHIL' in family.keys()):
        childrenList = family['CHIL']
        for i in range(len(childrenList)-1):
            for j in range(i+1, len(childrenList)):
                errMsg+= checkSiblingPair(individualDict[childrenList[i]], individualDict[childrenList[j]], family)
    return errMsg

def checkSiblingAgeDifference(familyDict, individualDict):
    errorMessages = []
    for family in familyDict.values():
        errorMessageForFam = checkFamily(family, individualDict)
        errorMessages += errorMessageForFam
    return errorMessages