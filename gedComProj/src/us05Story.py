import gedComProj.src.utils as utils

def checkFamily(family, individualDict):
    errMsg = []
    marriageDate = utils.calcDate(family['MARR'][0])
    husband = individualDict[family['HUSB'][0]]
    wife = individualDict[family['WIFE'][0]]
    if('DEAT' in wife.keys()):
        wifeDeath = utils.calcDate(wife['DEAT'][0])
        if(wifeDeath < marriageDate):
            errMsg += [("Error US05: Wife %s: %s in family %s died before she got married" %(wife['ID'], wife['NAME'][0], family['ID']))]
    if('DEAT' in husband.keys()):
        husbandDeath = utils.calcDate(husband['DEAT'][0])
        if(husbandDeath < marriageDate):
            errMsg += [("Error US05: Husband %s: %s in family %s died before she got married" %(husband['ID'], husband['NAME'][0], family['ID']))]
    return errMsg

def checkMarriageBeforeDeath(familyDict, individualDict):
    errorMessages = []
    for family in familyDict.values():
        errorMessageForFam = checkFamily(family, individualDict)
        errorMessages += errorMessageForFam
    return errorMessages