#import gedComProj.src.utils as utils
import datetime
#US42

monthDict = ["SEP", "APR", "JUN", "NOV", "JAN", "MAR", "MAY", "JUL", "AUG", "DEC", "FEB", "OCT"]
yearDict = { 30 : ["SEP", "APR", "JUN", "NOV"] , 31 : ["JAN", "MAR", "MAY", "JUL", "AUG", "OCT", "DEC"], 28 : ["FEB"]}

def checkValidDate(dateStr):
    checkDate = dateStr.split()
    if int(checkDate[0]) > 31 or checkDate[1] not in monthDict:
        return False
    if int(checkDate[0]) > 30 and checkDate[1] not in yearDict[31]:
        return False
    if checkDate[1] == "FEB":
        if (int(checkDate[2]) % 4 != 0) and int(checkDate[0]) > 28:
            return False
        elif (int(checkDate[2]) % 4 == 0) and int(checkDate[0]) > 29:
            return False
    return True

def badDate(familyDict, individualDict):
    err_msg = []
    for key in familyDict.keys():
        currFam = familyDict[key]
        if 'MARR' in currFam.keys():
            marrDate = currFam['MARR'][0]
            if not checkValidDate(marrDate):
                err_msg +=  ["Error US42: Family %s has an invalid marriage date." % (currFam['ID'])]
        if 'DIV' in currFam.keys():
            divDate = currFam['DIV'][0]
            if not checkValidDate(divDate):
                err_msg +=  ["Error US42: Family %s has an invalid Divorce date." % (currFam['ID'])]
    for key in individualDict.keys():
        currIndi = individualDict[key]
        birthDate = currIndi['BIRT'][0]
        if not checkValidDate(birthDate):
            err_msg += ["Error US42: Individual " + currIndi['ID'] + " has an invalid birth date."]
        if 'DEAT' in currIndi.keys():
            deathDate = currIndi['DEAT'][0]
            if not checkValidDate(deathDate):
                err_msg += ["Error US42: Individual " + currIndi['ID'] + " has an invalid death date."]
    return err_msg

