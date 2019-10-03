#US 17

def spouseNotParent(family, familyDict, individualDict):
    errorMessageForFam = []
    husband = individualDict[family["HUSB"][0]]
    wife = individualDict[family["WIFE"][0]]
    wifeChildFamily = wife["FAMC"][0] if "FAMC" in wife.keys() else None
    husbandChildFamily = husband["FAMC"][0] if "FAMC" in husband.keys() else None
    wifeFather = familyDict[wifeChildFamily]["HUSB"][0] if wifeChildFamily!=None and wifeChildFamily in familyDict.keys() else None
    husbandMother =  familyDict[husbandChildFamily]["WIFE"][0] if husbandChildFamily!=None and husbandChildFamily in familyDict.keys() else None

    if(husband["ID"] == wifeFather):
        errorMessageForFam += ["Anomaly US 17: in Family %s husband %s: %s is wife %s: %s's father" % (family["ID"], husband["ID"], husband["NAME"][0], wife["ID"], wife["NAME"][0])]
    elif(wife["ID"] == husbandMother):
        errorMessageForFam += ["Anomaly US 17: in Family %s husband %s: %s is wife %s: %s's son" % (family["ID"], husband["ID"], husband["NAME"][0], wife["ID"], wife["NAME"][0])]
    return errorMessageForFam

def noParentIncest(familyDict, individualDict):
    errorMessages = []
    for family in familyDict.values():
        errorMessageForFam = spouseNotParent(family, familyDict, individualDict)
        errorMessages += errorMessageForFam
    return errorMessages
