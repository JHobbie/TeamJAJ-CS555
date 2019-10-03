#US 18

def spouseNotSibling(family, familyDict, individualDict):
    errorMessageForFam = []
    husband = individualDict[family["HUSB"][0]]
    wife = individualDict[family["WIFE"][0]]
    wifeFamily = wife["FAMC"][0] if "FAMC" in wife.keys() else None
    husbandFamily = husband["FAMC"][0] if "FAMC" in husband.keys() else None
    if(wifeFamily == husbandFamily and (wifeFamily != None and husbandFamily!=None)):
        errorMessageForFam += ["Anomaly US 18: in Family %s husband %s: %s and wife %s: %s are children in the same family" % (family["ID"], husband["ID"], husband["NAME"][0], wife["ID"], wife["NAME"][0])]
    return errorMessageForFam

def noSiblingIncest(familyDict, individualDict):
    errorMessages = []
    for family in familyDict.values():
        errorMessageForFam = spouseNotSibling(family, familyDict, individualDict)
        errorMessages += errorMessageForFam
    return errorMessages
