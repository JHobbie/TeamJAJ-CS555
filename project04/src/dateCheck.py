#import project04.src.utils.py as utils
import datetime

#US01

def dateCheck(familyDict, individualDict):
    err_msg = []
    currDate = datetime.datetime.today()
    for key in familyDict.keys():
        currFam = familyDict[key]

        calculatedDate = datetime.datetime.strptime(currFam['MARR'][0], '%d %b %Y')
        if calculatedDate > currDate:
            err_msg += ["Family " + currFam['ID'] + " has marriage date in the future"]
        if 'DIV' in currFam.keys():
            calculatedDate = datetime.datetime.strptime(currFam['DIV'][0], '%d %b %Y')
            if (calculatedDate > currDate):
                err_msg += ["Family " + currFam['ID'] + " has divorce date in the future"]
   
    for key in individualDict.keys():
        currInd = individualDict[key]
        
        calculatedDate = datetime.datetime.strptime(currInd['BIRT'][0], '%d %b %Y')
        if (calculatedDate > currDate):
            err_msg += ["Individual " + currInd['ID'] + " has birth date in the future"]
        if 'DEAT' in currInd.keys():
            calculatedDate = datetime.datetime.strptime(currInd['DEAT'][0], '%d %b %Y')
            if (calculatedDate > currDate):
                err_msg += ["Individual " + currInd['ID'] + " has death date in the future"]

    return err_msg

