#import project04.src.utils.py as utils
import datetime

#US01
def dateCheck(familyDict, individualDict):
    currDate = datetime.now()
    dateBool = True
    for key in familyDict.keys():
        currFam = familyDict[key]
        if currFam['MARR'][0] > currDate:
            dateBool = False
        if currFam['DIV'][0] != None:
            if currFam['DIV'][0] > currDate:
                dateBool = False
    return dateBool

    for key in individualDict.keys():
        currInd = individualDict[key]
        if currInd['BIRT'][0] > currDate:
            dateBool = False
        if currInd['DEAT'][0] != None:
            if currInd['DEAT'][0] > currDate:
                dateBool = False
    return dateBool
        