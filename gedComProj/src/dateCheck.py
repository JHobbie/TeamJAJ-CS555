#import gedComProj.src.utils.py as utils
import datetime

#US01

def dateCheck(familyDict, individualDict):
    err_msg = []
    currDate = datetime.datetime.today()
    for key in familyDict.keys():
        currFam = familyDict[key]
        try:
            calculatedDate = datetime.datetime.strptime(currFam['MARR'][0], '%d %b %Y')
            if calculatedDate > currDate:
                err_msg += ["Error US 01: Family " + currFam['ID'] + " has marriage date in the future"]
        except ValueError :
            pass
        try:
            if 'DIV' in currFam.keys():
                calculatedDate = datetime.datetime.strptime(currFam['DIV'][0], '%d %b %Y')
                if (calculatedDate > currDate):
                    err_msg += ["Error US 01: Family " + currFam['ID'] + " has divorce date in the future"]
        except ValueError:
            pass
    for key in individualDict.keys():
        currInd = individualDict[key]
        try:
            calculatedDate = datetime.datetime.strptime(currInd['BIRT'][0], '%d %b %Y')
            if (calculatedDate > currDate):
                err_msg += ["Error US 01: Individual " + currInd['ID'] + " has birth date in the future"]
            if 'DEAT' in currInd.keys():
                calculatedDate = datetime.datetime.strptime(currInd['DEAT'][0], '%d %b %Y')
                if (calculatedDate > currDate):
                    err_msg += ["Error US 01: Individual " + currInd['ID'] + " has death date in the future"]
        except ValueError:
            pass
    return err_msg

