import gedComProj.src.utils as utils

def checkFamily(family):
    errMsg = []
    marriageDate = utils.calcDate(family['MARR'][0])
    if("DIV" in family.keys()):
        divorceDate = utils.calcDate(family['DIV'][0])
        if(divorceDate < marriageDate):
            errMsg+= [("Error US04: Divorce date is before marriage date in family %s" %(family['ID']))] 
    return errMsg

def checkMarriageBeforeDivorce(familyDict):
    errorMessages = []
    for family in familyDict.values():
        errorMessageForFam = checkFamily(family)
        errorMessages += errorMessageForFam
    return errorMessages