#US 18

def spouseNotSibling(family, familyDict, individualDict):
    errorMessageForFam = []
    husband = individualDict[family["HUSB"][0]]
    wife = individualDict[family["WIFE"][0]]
    if(wife["FAMC"][0] == husband["FAMC"][0]):
        errorMessageForFam += ["Anomaly US 18: in Family %s husband %s: %sand wife %s: %s are children in the same family" % (family["ID"], husband["ID"], husband["NAME"][0], wife["ID"], wife["NAME"][0])]
    return errorMessageForFam

def noSiblingIncest(familyDict, individualDict):
    errorMessages = []
    for family in familyDict.values():
        errorMessageForFam = spouseNotSibling(family, familyDict, individualDict)
        errorMessages += errorMessageForFam
    return errorMessages
